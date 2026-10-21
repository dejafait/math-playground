"""Independent serialized Hilbert checker; accepts no semantic/rewrite rules."""
import argparse
import hashlib
import gzip
import json
from pathlib import Path

class Invalid(ValueError): pass

def parse(s, mode):
    pos = 0
    def term():
        nonlocal pos
        if pos >= len(s): raise Invalid('unexpected end')
        if s[pos] != '(':
            begin = pos
            while pos < len(s) and (s[pos].isalnum() or s[pos] == '_'): pos += 1
            if pos == begin: raise Invalid('bad variable')
            return s[begin:pos], 1, 0
        pos += 1
        if pos < len(s) and s[pos] == '~':
            pos += 1
            a, count, depth = term()
            out = ('not', a), count+1, depth+1
        else:
            a, ca, da = term()
            op = '>' if mode == 'native' else '|'
            if pos >= len(s) or s[pos] != op: raise Invalid('wrong binary connective')
            pos += 1
            b, cb, db = term()
            out = ('imp' if mode == 'native' else 'or', a, b), ca+cb+1, max(da, db)+1
        if pos >= len(s) or s[pos] != ')': raise Invalid('missing close parenthesis')
        pos += 1
        return out
    tree, count, depth = term()
    if pos != len(s): raise Invalid('trailing syntax')
    return tree, count, depth

def serialize(t):
    if isinstance(t, str): return t
    if t[0] == 'not': return '(~'+serialize(t[1])+')'
    return '('+serialize(t[1])+('>' if t[0] == 'imp' else '|')+serialize(t[2])+')'

def pattern(rule, mode):
    # Deliberately independent definitions, with no compiler import.
    def neg(a): return ('not', a)
    def implies(a, b):
        return ('imp', a, b) if mode == 'native' else ('or', neg(a), b)
    a, b, c = '$A', '$B', '$C'
    if rule == 'ax1': return implies(a, implies(b, a))
    if rule == 'ax2': return implies(implies(a, implies(b, c)), implies(implies(a, b), implies(a, c)))
    if rule == 'ax3': return implies(implies(neg(a), neg(b)), implies(b, a))
    raise Invalid('unapproved rule '+rule)

def match(p, t, env):
    if isinstance(p, str):
        if p in env and env[p] != t: raise Invalid('inconsistent schema substitution')
        env[p] = t
    else:
        if not isinstance(t, tuple) or len(p) != len(t) or p[0] != t[0]:
            raise Invalid('axiom shape mismatch')
        for a, b in zip(p[1:], t[1:]): match(a, b, env)

def check(path, expected=None):
    formulas = []
    total_nodes = 0
    substitution_nodes = 0
    max_depth = 0
    max_nodes = 0
    max_record_nodes = 0
    digest = hashlib.sha256()
    byte_count = 0
    with (gzip.open(path, 'rb') if str(path).endswith('.gz') else Path(path).open('rb')) as stream:
        header_raw = stream.readline()
        digest.update(header_raw); byte_count += len(header_raw)
        header = json.loads(header_raw)
        mode = header['format']
        if mode not in ('native', 'not-or'): raise Invalid('unknown format')
        goal = header['goal']
        _, goal_nodes, goal_depth = parse(goal, mode)
        if expected is not None and goal != expected: raise Invalid('requested endpoint mismatch')
        for line_index, raw in enumerate(stream):
            digest.update(raw); byte_count += len(raw)
            try:
                row = json.loads(raw)
                t, nodes, depth = parse(row['f'], mode)
                total_nodes += nodes
                max_nodes = max(max_nodes, nodes)
                max_depth = max(max_depth, depth)
                rule = row['rule']
                row_substitution_nodes = 0
                if rule == 'mp':
                    if set(row) != {'f', 'rule', 'refs'}: raise Invalid('invalid MP record')
                    refs = row['refs']
                    if len(refs) != 2 or any(type(k) is not int or k < 0 or k >= line_index for k in refs):
                        raise Invalid('reference not strictly earlier')
                    antecedent, conditional = (formulas[k] for k in refs)
                    ct, _, _ = parse(conditional, mode)
                    if mode == 'native':
                        if isinstance(ct, str) or ct[0] != 'imp': raise Invalid('MP conditional shape')
                        a, b = ct[1], ct[2]
                    else:
                        if isinstance(ct, str) or ct[0] != 'or' or isinstance(ct[1], str) or ct[1][0] != 'not':
                            raise Invalid('translated MP conditional shape')
                        a, b = ct[1][1], ct[2]
                    if serialize(a) != antecedent or b != t: raise Invalid('MP antecedent/consequent mismatch')
                else:
                    if set(row) != {'f', 'rule', 'subs'}: raise Invalid('invalid axiom record')
                    env = {}
                    match(pattern(rule, mode), t, env)
                    if set(row['subs']) != {k[1:] for k in env}: raise Invalid('substitution keys')
                    for k, v in row['subs'].items():
                        st, sn, _ = parse(v, mode)
                        substitution_nodes += sn
                        row_substitution_nodes += sn
                        if st != env['$'+k]: raise Invalid('declared substitution mismatch')
                formulas.append(row['f'])
                max_record_nodes = max(max_record_nodes, nodes + row_substitution_nodes)
            except (KeyError, TypeError, ValueError) as err:
                raise Invalid('line '+str(line_index)+': '+str(err)) from err
    if not formulas or formulas[-1] != goal: raise Invalid('last line is not requested endpoint')
    project = Path(__file__).resolve().parents[2]
    try: display_path = str(Path(path).resolve().relative_to(project))
    except ValueError: display_path = str(path)
    return {'path': display_path, 'format': mode, 'accepted': True, 'lines': len(formulas),
            'bytes': byte_count, 'sha256': digest.hexdigest(), 'formula_nodes': total_nodes,
            'substitution_nodes': substitution_nodes, 'max_line_nodes': max_nodes,
            'max_record_nodes': max_record_nodes,
            'max_line_depth': max_depth, 'goal_nodes': goal_nodes, 'goal_depth': goal_depth}

def slot_goal(input_terms, pair, action, mode):
    """Construct the requested endpoint without importing any emitter/planner."""
    items = [parse(s, 'native')[0] for s in input_terms]
    m = len(items)
    if m < 2 or m & (m-1) or not 0 <= pair < m-1: raise Invalid('invalid slot request')
    def nt(a): return ('not', a)
    def im(a, b): return ('imp', a, b)
    def xor(a, b): return im(im(a, b), nt(im(b, a)))
    def balanced(seq):
        if len(seq) == 1: return seq[0]
        k = len(seq)//2
        return xor(balanced(seq[:k]), balanced(seq[k:]))
    target = list(items)
    if action == 'exchange': target[pair], target[pair+1] = target[pair+1], target[pair]
    elif action == 'cancel':
        if items[pair] != items[pair+1]: raise Invalid('nonidentical cancellation terms')
        target[pair:pair+2] = [nt(im('q', 'q'))]*2
    else: raise Invalid('unknown slot action')
    goal = nt(xor(balanced(items), balanced(target)))
    if mode == 'not-or':
        def image(t):
            if isinstance(t, str): return t
            if t[0] == 'not': return nt(image(t[1]))
            return ('or', nt(image(t[1])), image(t[2]))
        goal = image(goal)
    elif mode != 'native': raise Invalid('unknown format')
    return serialize(goal)

if __name__ == '__main__':
    argp = argparse.ArgumentParser()
    argp.add_argument('path')
    argp.add_argument('--expected-goal')
    argp.add_argument('--certificate')
    args = argp.parse_args()
    result = check(args.path, args.expected_goal)
    if args.certificate:
        Path(args.certificate).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, separators=(',', ':')))
