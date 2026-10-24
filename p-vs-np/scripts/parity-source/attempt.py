"""Bounded exact-source implementation experiment; never emits H.

Run from the notebook: python3 scripts/parity-source/attempt.py
Fixed-template synthesis is inherited from qualified L056, with every
native ax-3 replaced by an explicit proof in the requested source basis.
Only source streams accepted by the separate checker count as exports.
"""
import importlib.util
import itertools
import json
from pathlib import Path
import time

import checker

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output'
spec = importlib.util.spec_from_file_location('slot_component', HERE.parent / 'balanced-slot' / 'compiler.py')
slot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(slot)
N, I = slot.N, slot.I


def And(a, b):
    return N(I(a, N(b)))


class SourceProof(slot.Proof):
    def __init__(self):
        super().__init__()
        self.replacement_cache = {}

    def ax(self, tag, a, b, c=None):
        if tag == 'axS':
            f = I(I(N(a), N(b)), I(I(N(a), b), a))
            return self.add(f, 'axS', env={'A': a, 'B': b})
        if tag != 'ax3':
            return super().ax(tag, a, b, c)
        key = (a, b)
        if key in self.replacement_cache:
            return self.replacement_cache[key]
        # From h: (~a -> ~b) and b, derive ~a -> b by ax1;
        # the exact source second scheme then gives a. Discharge b,h.
        h = I(N(a), N(b))
        ph, pb = self.assume(h), self.assume(b)
        conditional = self.mp(ph, self.ax('axS', a, b))
        nb_to_b = self.mp(pb, self.ax('ax1', b, N(a)))
        pa = self.mp(nb_to_b, conditional)
        root = self.discharge(h, self.discharge(b, pa))
        assert self.rows[root][0] == I(h, I(b, a))
        assert not self.rows[root][4]
        self.replacement_cache[key] = root
        return root

    def instance(self, root, env):
        key = (root, tuple(sorted(env.items())))
        if key in self.instance_cache:
            return self.instance_cache[key]
        f, rule, refs, oldenv, deps = self.rows[root]
        assert not deps
        if rule == 'mp':
            out = self.mp(*(self.instance(j, env) for j in refs))
        else:
            assert rule in ('ax1', 'ax2', 'axS')
            e = {k: slot.sub(v, env) for k, v in oldenv.items()}
            out = self.ax(rule, e['A'], e['B'], e.get('C'))
        assert self.rows[out][0] == slot.sub(f, env)
        self.instance_cache[key] = out
        return out

    def ground(self, truth):
        return self.add('true' if truth else N('false'), 'true' if truth else 'not-false')

    def export(self, root, path):
        # Keep every completed assumption-free generated record, including
        # unused templates. Assumption-dependent tactic scratch is not a
        # source-proof assertion. No reachable-only pruning is performed.
        identity = self.identity(self.rows[root][0])
        order = [j for j, r in enumerate(self.rows) if not r[4]]
        remap = {j: k for k, j in enumerate(order)}
        lines = []
        for j in order:
            f, rule, refs, env, deps = self.rows[j]
            row = {'f': slot.text(f, True), 'rule': rule}
            if rule == 'mp':
                row['refs'] = [remap[k] for k in refs]
            elif env is not None:
                row['subs'] = {k: slot.text(v, True) for k, v in env.items()}
            lines.append(row)
        # An explicit final MP keeps the requested endpoint last even when
        # the constructor's formula cache reused an earlier occurrence.
        lines.append({'f': slot.text(self.rows[root][0], True), 'rule': 'mp',
                      'refs': [remap[root], remap[identity]]})
        header = {'format': 'exact-not-or', 'goal': lines[-1]['f']}
        with path.open('w') as stream:
            for row in [header] + lines:
                stream.write(json.dumps(row, separators=(',', ':')) + '\n')
        return dict(generated_tactic_records=len(self.rows),
                    omitted_assumption_dependent_scratch=len(self.rows)-len(order),
                    completed_records_retained=len(order),
                    unused_completed_records=len(set(order)-set(self.reachable(root))),
                    final_duplicate_mp=True)


def source_not(a):
    return ('n', a)


def source_or(a, b):
    return ('o', a, b)


def source_and(a, b):
    return source_not(source_or(source_not(a), source_not(b)))


def source_xor(a, b):
    return source_and(source_or(a, b), source_not(source_and(a, b)))


def source_eq(a, b):
    return source_and(source_or(source_not(a), b), source_or(source_not(b), a))


def implication_decode(t, opaque):
    """Reception diagnostic, not an additional rule or completeness test.

    Recognize literal ~A|B as A->B. A remaining OR is assigned a fresh
    opaque token. This is exactly what an implication-only component
    cannot inspect. No normalized formula is exported as the endpoint.
    """
    if isinstance(t, str):
        return t
    if t[0] == 'n':
        return N(implication_decode(t[1], opaque))
    if isinstance(t[1], tuple) and t[1][0] == 'n':
        return I(implication_decode(t[1][1], opaque), implication_decode(t[2], opaque))
    key = checker.spell(t)
    if key not in opaque:
        opaque[key] = 'opaque_' + str(len(opaque))
    return opaque[key]


def evaluate_native(t, assignment):
    if t == 'true':
        return True
    if t == 'false':
        return False
    if isinstance(t, str):
        return assignment[t]
    if t[0] == 'n':
        return not evaluate_native(t[1], assignment)
    return not evaluate_native(t[1], assignment) or evaluate_native(t[2], assignment)


def reception_test(source_formula):
    opaque = {}
    decoded = implication_decode(source_formula, opaque)
    vs = sorted(slot.variables(decoded) - {'true', 'false'})
    countervaluation = None
    for bits in itertools.product((False, True), repeat=len(vs)):
        env = dict(zip(vs, bits))
        if not evaluate_native(decoded, env):
            countervaluation = env
            break
    return dict(exact_formula=checker.spell(source_formula),
                decoded_native_formula=slot.text(decoded), opaque_OR=opaque,
                decoded_variables=vs, decoded_countervaluation=countervaluation,
                synthesis_invoked=False,
                limitation='Implication-only fixed-template synthesis refuses a non-tautological decoded input; no exact-OR bridge is available in this implementation.')


def fixture(rows, selected, tree):
    clauses = []
    for row in rows:
        for bits in itertools.product((0, 1), repeat=len(row['names'])):
            if sum(bits) % 2 != row['rhs']:
                clauses.append([v if bit == 0 else '(~'+v+')' for v, bit in zip(row['names'], bits)])
    return dict(rows=rows, **{'lambda': selected}, clauses=clauses,
                clause_tree_policy='right-associated actual trees; empty=false',
                global_tree=tree,
                L087_pair_provenance='NOT_IMPLEMENTED: original M and Q unverified')


def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n')


def corruption_checks(path, expected):
    original = [json.loads(s) for s in path.read_text().splitlines()]
    mp_index = next(j for j, r in enumerate(original[1:], 1) if r['rule'] == 'mp')
    ax_index = next(j for j, r in enumerate(original[1:], 1) if r['rule'] == 'axS')
    ground_index = next(j for j, r in enumerate(original[1:], 1) if r['rule'] == 'not-false')
    cases = ['axiom-occurrence', 'forward-reference', 'out-of-range-reference',
             'wrong-MP-premise', 'constant-misuse', 'header-endpoint',
             'last-endpoint', 'old-ax3-extra-rule', 'assumption-extra-rule']
    results = []
    for case in cases:
        rows = json.loads(json.dumps(original))
        if case == 'axiom-occurrence':
            rows[ax_index]['f'] = 'x'
        elif case == 'forward-reference':
            rows[mp_index]['refs'][0] = mp_index-1
        elif case == 'out-of-range-reference':
            rows[mp_index]['refs'][0] = len(rows)+5
        elif case == 'wrong-MP-premise':
            rows[-1]['refs'] = [rows[-1]['refs'][1], rows[-1]['refs'][0]]
        elif case == 'constant-misuse':
            rows[ground_index]['f'] = '(~true)'
        elif case == 'header-endpoint':
            rows[0]['goal'] = 'x'
        elif case == 'last-endpoint':
            rows[-1]['f'] = 'x'
        elif case == 'old-ax3-extra-rule':
            rows[ax_index]['rule'] = 'ax3'
        else:
            rows[ax_index] = {'f': 'x', 'rule': 'assume'}
        corrupt = OUT / ('corrupt-' + case + '.jsonl')
        corrupt.write_text(''.join(json.dumps(r, separators=(',', ':'))+'\n' for r in rows))
        try:
            checker.check(corrupt, expected)
            results.append(dict(case=case, rejected=False, path=str(corrupt.relative_to(HERE.parent.parent))))
        except checker.Invalid as err:
            results.append(dict(case=case, rejected=True, reason=str(err),
                                path=str(corrupt.relative_to(HERE.parent.parent))))
    return results


def main():
    OUT.mkdir(exist_ok=True)
    started = time.monotonic()
    p = SourceProof()
    library_root = p.ax('ax3', 'A', 'B')
    library_path = OUT / 'replacement-library.jsonl'
    library_retention = p.export(library_root, library_path)
    library = checker.check(library_path, slot.text(I(I(N('A'), N('B')), I('B', 'A')), True))
    library['retention'] = library_retention
    p.build_helpers()
    # A fixed two-variable constant-free tautology; never a growing
    # truth-table proof of the parity instance.
    projection = p.prove_fixed(I(N('d'), N(And('A', 'd'))))
    template_path = OUT / 'zero-projection-library.jsonl'
    template_retention = p.export(projection, template_path)
    template = checker.check(template_path, slot.text(I(N('d'), N(And('A', 'd'))), True))
    template['retention'] = template_retention
    p.ground(True)  # Deliberately unused, retained primitive record.
    nf = p.ground(False)
    fixtures = {
        'zero-direct': fixture([dict(names=[], rhs=1)], [1], 0),
        'zero-unused-rows': fixture([dict(names=[], rhs=0), dict(names=[], rhs=1),
                                     dict(names=[], rhs=0)], [0, 1, 0], 0),
        'zero-conjunction': fixture([dict(names=['x'], rhs=0), dict(names=[], rhs=1),
                                     dict(names=[], rhs=0)], [0, 1, 0], [0, 1]),
        'three-row': fixture([dict(names=['x', 'y'], rhs=0),
                              dict(names=['y', 'z'], rhs=0),
                              dict(names=['x', 'z'], rhs=1)], [1, 1, 1],
                             [[0, [1, 2]], [[3, 4], 5]])
    }
    results = {}
    for name, data in fixtures.items():
        save(name+'-input.json', data)
        expected = checker.fixture_endpoint(json.loads((OUT / (name+'-input.json')).read_text()))
        if name == 'three-row':
            results[name] = dict(status='FAILED_EXACT_OR_RECEPTION', expected=expected,
                                 endpoint_diagnostic=reception_test(checker.parse(expected)),
                                 emitted_stream=None, input_retained=True)
            continue
        root = nf
        if name == 'zero-conjunction':
            root = p.mp(nf, p.instance(projection, {'A': N('x'), 'd': 'false'}))
        path = OUT / (name+'.jsonl')
        retention = p.export(root, path)
        result = checker.check(path, expected)
        result.update(expected=expected, retention=retention,
                      stream_path=str(path.relative_to(HERE.parent.parent)), input_retained=True)
        results[name] = result
    # Save the exact first row-reception template that this component
    # would need, using L106's displayed X and E and actual row clauses.
    k = source_and(source_or('x', source_not('y')), source_or(source_not('x'), 'y'))
    r = source_xor(source_xor('x', 'y'), source_xor('false', 'false'))
    row_target = source_or(source_not(k), source_eq(r, 'false'))
    save('failed-row-template.json', reception_test(row_target))
    corruptions = corruption_checks(OUT/'zero-conjunction.jsonl', results['zero-conjunction']['expected'])
    # Corruption tests target an otherwise valid complete source stream.
    assert all(r['rejected'] for r in corruptions)
    source_input_bytes = sum((OUT/(name+'-input.json')).stat().st_size for name in fixtures)
    report = dict(status='PARTIAL_IMPLEMENTATION_WITH_EXACT_OR_RECEPTION_FAILURE',
                  actual_task_type='implementation', library=library, zero_projection_library=template,
                  fixtures=results, corruptions=corruptions,
                  elapsed_seconds=time.monotonic()-started,
                  source_input_bytes=source_input_bytes,
                  full_original_Q_integration='UNVERIFIED: no actual L087 pair/provenance was constructed',
                  required_source_bound='c Q^12, with one justified input-independent c',
                  measured_bound_verdict='UNVERIFIED: no c fitted; partial fixtures do not verify all-size bound',
                  downstream_H_generated=False,
                  failure_scope='Exact literal-OR reception by this implication-only fixed-template implementation; no proof of source nonderivability or changed-basis theorem claimed.')
    save('report.json', report)
    for name, result in results.items():
        print(name, result.get('status', 'ACCEPTED'),
              'records=', result.get('records'), 'bits=', result.get('bits'))
    print('corruptions rejected', sum(r['rejected'] for r in corruptions), '/', len(corruptions))
    print('required: c Q^12; original Q and uniform bound UNVERIFIED')
    print('full evidence: scripts/parity-source/output/report.json; failed-row-template.json; complete *.jsonl')


if __name__ == '__main__':
    main()
