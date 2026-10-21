"""One bounded slot suite; writes complete proofs, trace, bounds and corruptions."""
import hashlib
import gzip
import json
import math
from pathlib import Path
import compiler as emit
import checker as verify

HERE = Path(__file__).resolve().parent
OUT = HERE/'output'

def join(a, b): return ('x', a, b)
def is_join(t): return isinstance(t, tuple) and t[0] == 'x'
def native(t):
    return emit.X(native(t[1]), native(t[2])) if is_join(t) else t
def leaves(t): return leaves(t[1])+leaves(t[2]) if is_join(t) else [t]
def height(t): return 1+max(height(t[1]), height(t[2])) if is_join(t) else 0
def balanced(items):
    if len(items) == 1: return items[0]
    m = len(items)//2
    return join(balanced(items[:m]), balanced(items[m:]))
def at(t, path):
    for k in path: t = t[k]
    return t
def replace(t, path, replacement):
    if not path: return replacement
    if path[0] == 1: return join(replace(t[1], path[1:], replacement), t[2])
    return join(t[1], replace(t[2], path[1:], replacement))

class Slot:
    def __init__(self, p, library, items, pair, action):
        assert len(items) >= 2 and len(items) & (len(items)-1) == 0
        assert 0 <= pair < len(items)-1
        if action == 'cancel': assert items[pair] == items[pair+1]
        self.p, self.lib = p, library
        self.initial = self.tree = balanced(items)
        self.events = []
        self.eq = p.instance(library['refl'], {'A': native(self.tree)})
        self.original_pair = pair
        self.action = action
        self.forward_rotations = []

    def theorem(self, name, env): return self.p.instance(self.lib[name], env)

    def combine(self, left, middle, right, ab, bc):
        law = self.theorem('trans', {'A': left, 'B': middle, 'C': right})
        return self.p.mp(bc, self.p.mp(ab, law))

    def rewrite(self, path, replacement, eq, description):
        old = self.tree
        oldsub = at(old, path)
        newsub = replacement
        assert self.p.rows[eq][0] == emit.E(native(oldsub), native(newsub))
        # Lift the already established equality once at each literal ancestor.
        for length in range(len(path), 0, -1):
            parent = at(old, path[:length-1])
            side = path[length-1]
            sibling = parent[3-side]
            law = self.theorem('congL' if side == 1 else 'congR',
                {'A': native(oldsub), 'B': native(newsub), 'C': native(sibling)})
            eq = self.p.mp(eq, law)
            oldsub = parent
            newsub = join(newsub, sibling) if side == 1 else join(sibling, newsub)
        self.tree = replace(old, path, replacement)
        assert newsub == self.tree
        self.eq = self.combine(native(self.initial), native(old), native(self.tree), self.eq, eq)
        self.events.append({'kind': description, 'path': list(path),
                            'temporary_height': height(self.tree),
                            'before': emit.text(native(old)), 'after': emit.text(native(self.tree))})

    def rotate(self, path, direction, save=True):
        old = at(self.tree, path)
        if direction == 'right':
            # ((A XOR B) XOR C) -> (A XOR (B XOR C)).
            a, b, c = old[1][1], old[1][2], old[2]
            new = join(a, join(b, c))
            eq = self.theorem('assoc', {'A': native(a), 'B': native(b), 'C': native(c)})
        else:
            a, b, c = old[1], old[2][1], old[2][2]
            new = join(join(a, b), c)
            forward = self.theorem('assoc', {'A': native(a), 'B': native(b), 'C': native(c)})
            reverse = self.theorem('symm', {'A': native(new), 'B': native(old)})
            eq = self.p.mp(forward, reverse)
        self.rewrite(path, new, eq, 'rotate-'+direction)
        if save: self.forward_rotations.append((path, direction))

    def expose(self, path, pair):
        t = at(self.tree, path)
        left_count = len(leaves(t[1]))
        if pair+1 < left_count: return self.expose(path+(1,), pair)
        if pair >= left_count: return self.expose(path+(2,), pair-left_count)
        assert pair == left_count-1
        # Isolate the last left leaf and the first right leaf. All other
        # subtrees stay opaque copied blocks, never complete list flattening.
        while is_join(at(self.tree, path+(1,))) and is_join(at(self.tree, path+(1,))[2]):
            self.rotate(path+(1,), 'left')
        while is_join(at(self.tree, path+(2,))) and is_join(at(self.tree, path+(2,))[1]):
            self.rotate(path+(2,), 'right')
        t = at(self.tree, path)
        left_internal, right_internal = is_join(t[1]), is_join(t[2])
        if left_internal:
            self.rotate(path, 'right')
            if right_internal:
                self.rotate(path+(2,), 'left')
                return path+(2, 1)
            return path+(2,)
        if right_internal:
            self.rotate(path, 'left')
            return path+(1,)
        return path

    def run(self):
        pair_path = self.expose((), self.original_pair)
        oldpair = at(self.tree, pair_path)
        assert is_join(oldpair) and not is_join(oldpair[1]) and not is_join(oldpair[2])
        a, b = oldpair[1:]
        if self.action == 'exchange':
            eq = self.theorem('comm', {'A': a, 'B': b})
            self.rewrite(pair_path, join(b, a), eq, 'exchange')
        else:
            assert a == b
            first = self.theorem('cancel', {'A': a})
            second = self.theorem('zero_slots', {})
            eq = self.combine(emit.X(a, a), emit.Z, emit.X(emit.Z, emit.Z), first, second)
            self.rewrite(pair_path, join(emit.Z, emit.Z), eq, 'cancel-expand-zero-slots')
        for path, direction in reversed(self.forward_rotations):
            self.rotate(path, 'left' if direction == 'right' else 'right', save=False)
        expected = leaves(self.initial)
        k = self.original_pair
        if self.action == 'exchange': expected[k], expected[k+1] = expected[k+1], expected[k]
        else: expected[k:k+2] = [emit.Z, emit.Z]
        assert self.tree == balanced(expected), 'slot shape was not restored'
        assert self.p.rows[self.eq][0] == emit.E(native(self.initial), native(self.tree))
        return self.eq

def corruptions(path, expected):
    with gzip.open(path, 'rt') as f: lines = f.read().splitlines()
    records = [json.loads(x) for x in lines[1:]]
    first_ax = next(k for k,r in enumerate(records) if r['rule'] != 'mp')
    first_mp = next(k for k,r in enumerate(records) if r['rule'] == 'mp')
    tests = []
    def test(name, index, row=None, header=None):
        copy = list(lines)
        if row is not None: copy[index+1] = json.dumps(row, separators=(',', ':'))
        if header is not None: copy[0] = json.dumps(header, separators=(',', ':'))
        target = OUT/('corrupt-'+name+'.jsonl.gz')
        with gzip.open(target, 'wt') as f: f.write('\n'.join(copy)+'\n')
        try:
            verify.check(target, expected)
        except verify.Invalid as err:
            tests.append({'name': name, 'rejected': True, 'reason': str(err), 'path': str(target.relative_to(HERE))})
        else: tests.append({'name': name, 'rejected': False, 'path': str(target.relative_to(HERE))})
    # Alter one occurrence inside an otherwise correctly shaped axiom;
    # matching must detect inconsistent repeated schema variables.
    row = dict(records[first_ax], f=records[first_ax]['f'].replace('p0', 'p_CORRUPT', 1))
    test('axiom-occurrence', first_ax, row)
    row = dict(records[first_mp], refs=[0, len(records)])
    test('forward-reference', first_mp, row)
    # Every other line is unchanged; substitute a different valid earlier
    # theorem as the MP antecedent, guaranteeing a literal mismatch.
    k = next(k for k,r in enumerate(records) if r['rule'] == 'mp' and
             any(records[j]['f'] != records[r['refs'][0]]['f'] for j in range(k)))
    other = next(j for j in range(k) if records[j]['f'] != records[records[k]['refs'][0]]['f'])
    row = dict(records[k], refs=[other, records[k]['refs'][1]])
    test('mp-antecedent', k, row)
    header = json.loads(lines[0]); header['goal'] = 'p_WRONG_ENDPOINT'
    test('endpoint', 0, header=header)
    assert all(t['rejected'] for t in tests)
    return tests

def main():
    p = emit.Proof(); p.build_helpers()
    library = {}
    lib_checks = {}
    for name, goal in emit.schemas().items():
        root = p.prove_fixed(goal); library[name] = root
        lib_checks[name] = {}
        for image, suffix in [(False, 'native'), (True, 'not-or')]:
            path = OUT/(name+'.'+suffix+'.jsonl.gz')
            p.write(root, path, image)
            lib_checks[name][suffix] = verify.check(path, emit.text(goal, image))
        print('library', name, 'accepted', lib_checks[name]['native']['lines'], flush=True)
    # Fixed-library constants are measurements, not fitted asymptotic constants.
    lc = max(v['native']['lines'] for v in lib_checks.values())
    constants = {'L': lc, 'native': {}, 'not-or': {}}
    for mode in ('native', 'not-or'):
        constants[mode] = {'D': max(v[mode]['max_line_depth'] for v in lib_checks.values()),
                           'S': max(v[mode]['max_record_nodes'] for v in lib_checks.values())}
    (OUT/'fixed-library-checks.json').write_text(json.dumps({'constants': constants, 'checks': lib_checks}, indent=2)+'\n')
    cases = [
        ('m2-exchange', ['p0', 'p1'], 0, 'exchange'),
        ('m2-cancel', [emit.I('p_repeat','p_suffix')]*2, 0, 'cancel'),
        ('m4-root-exchange', ['p0', emit.N('p1'), emit.I('p2','p3'), 'p4'], 1, 'exchange'),
        ('m4-root-cancel', [emit.Z, emit.I('p_repeat','p_suffix'), emit.I('p_repeat','p_suffix'), emit.I('q','q')], 1, 'cancel'),
        ('m8-root-exchange', ['p0', 'p1', emit.Z, emit.I('q','q'), emit.N('p4'), 'p5', 'p6', 'p7'], 3, 'exchange'),
        ('m8-root-cancel', ['p0','p1','p2',emit.Z,emit.Z,'p5','p6','p7'], 3, 'cancel'),
        ('m8-interior-exchange', ['p0','p1','p2','p3','p4','p5','p6','p7'], 1, 'exchange'),
    ]
    all_results = []
    for name, items, pair, action in cases:
        slot = Slot(p, library, items, pair, action)
        root = slot.run()
        m, h = len(items), int(math.log2(len(items)))
        events = len(slot.events)
        event_bound = 4*h+3
        height_bound = 3*h+2
        line_bound = (1+event_bound*(3*h+8))*(lc+2)
        result = {'name': name, 'M': m, 'pair': pair, 'action': action,
                  'events': events, 'required_events_max': event_bound,
                  'max_temporary_height': max([h]+[x['temporary_height'] for x in slot.events]),
                  'required_temporary_height_max': height_bound, 'proofs': {}}
        for image, mode in [(False, 'native'), (True, 'not-or')]:
            path = OUT/(name+'.'+mode+'.jsonl.gz')
            expected = verify.slot_goal([emit.text(t) for t in items], pair, action, mode)
            p.write(root, path, image)
            measured = verify.check(path, expected)
            term_stats = [verify.parse(emit.text(t, image), mode)[1:] for t in items+[emit.Z]]
            tmax, dmax = max(t[0] for t in term_stats), max(t[1] for t in term_stats)
            expansion_depth = 6 if image else 3
            depth_bound = constants[mode]['D'] + expansion_depth*height_bound + dmax
            argument_nodes_bound = 8*(4**(height_bound+1))*(tmax+1)
            names = set().union(*(emit.variables(t) for t in items+[emit.Z]))
            raw_payload_max = max(len(n.encode('ascii')) for n in names)
            record_nodes_bound = constants[mode]['S']*argument_nodes_bound
            byte_bound = (line_bound+2)*((raw_payload_max+4)*record_nodes_bound+256+64*math.ceil(math.log2(line_bound+2)))
            bounds = {'required_lines_max': line_bound, 'required_depth_max': depth_bound,
                      'required_record_nodes_max': record_nodes_bound, 'required_bytes_max': byte_bound,
                      'actual_bits': 8*measured['bytes'], 'required_bits_max': 8*byte_bound,
                      'term_nodes_max': tmax, 'term_depth_max': dmax, 'raw_name_bytes_max': raw_payload_max}
            checks = [measured['lines'] <= line_bound, measured['max_line_depth'] <= depth_bound,
                      measured['max_record_nodes'] <= record_nodes_bound, measured['bytes'] <= byte_bound]
            assert all(checks), (name, mode, measured, bounds)
            result['proofs'][mode] = {'measurement': measured, 'bounds': bounds, 'bounds_pass': all(checks)}
        assert events <= event_bound and result['max_temporary_height'] <= height_bound
        (OUT/(name+'.trace.json')).write_text(json.dumps({'case': name, 'events': slot.events,
             'input_terms': [emit.text(t) for t in items], 'restored_output_terms': [emit.text(t) for t in leaves(slot.tree)]}, indent=2)+'\n')
        all_results.append(result)
        n, o = result['proofs']['native']['measurement'], result['proofs']['not-or']['measurement']
        print(name, 'accepted native/image', 'lines actual/max', n['lines'], line_bound,
              o['lines'], line_bound, 'depth actual/max',
              n['max_line_depth'], result['proofs']['native']['bounds']['required_depth_max'],
              o['max_line_depth'], result['proofs']['not-or']['bounds']['required_depth_max'],
              'record-nodes actual/max', n['max_record_nodes'], result['proofs']['native']['bounds']['required_record_nodes_max'],
              o['max_record_nodes'], result['proofs']['not-or']['bounds']['required_record_nodes_max'],
              'uncompressed-bytes actual/max', n['bytes'], result['proofs']['native']['bounds']['required_bytes_max'],
              o['bytes'], result['proofs']['not-or']['bounds']['required_bytes_max'],
              'paths', n['path'], o['path'], flush=True)
    corrupt = corruptions(OUT/'m2-exchange.native.jsonl.gz',
                          emit.text(emit.E(emit.X('p0','p1'),emit.X('p1','p0'))))
    # Also test the translated checker, preserving all corrupted files separately.
    saved = {x['name']: (OUT/('corrupt-'+x['name']+'.jsonl.gz')).read_bytes() for x in corrupt}
    corrupt_image = corruptions(OUT/'m2-exchange.not-or.jsonl.gz',
                                emit.text(emit.E(emit.X('p0','p1'),emit.X('p1','p0')), True))
    for x in corrupt_image:
        old = OUT/('corrupt-'+x['name']+'.jsonl.gz')
        new = OUT/('corrupt-not-or-'+x['name']+'.jsonl.gz')
        old.rename(new)
        x['path'] = str(new.relative_to(HERE))
    for name, data in saved.items(): (OUT/('corrupt-'+name+'.jsonl.gz')).write_bytes(data)
    summary = {'all_accepted': True, 'all_bounds_pass': True, 'failures': [], 'fixed_library': constants,
               'cases': all_results, 'corruptions': {'native': corrupt, 'not-or': corrupt_image},
               'qualification': 'Bounded slot component only. Not whole receiver, certificate existence or SAT transfer.'}
    (OUT/'certificate.json').write_text(json.dumps(summary, indent=2)+'\n')
    print('failures none; corruptions rejected', len(corrupt)+len(corrupt_image),
          'certificate', str((OUT/'certificate.json').relative_to(HERE.parent.parent)))

if __name__ == '__main__': main()
