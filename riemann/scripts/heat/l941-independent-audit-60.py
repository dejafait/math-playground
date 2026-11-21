#!/usr/bin/env python3
"""Independent exact audit of L941; no producer/replay code is imported.

Read both entire step58 certificates. Rebuild rows by a labelled-slot
generating recurrence and verify all load-bearing saved arithmetic, including
endpoint-record linkage and the canonical lemma's transcriptions.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial, prod
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = Path(__file__).with_suffix('.json')
checks, failures, tables = [], [], []
inputs = {}


def read(rel):
    p = ROOT / rel
    raw = p.read_bytes()
    inputs[rel] = sha256(raw).hexdigest()
    return raw.decode()


def ck(name, ok, actual=None, required=None):
    item = {'name': name, 'ok': bool(ok)}
    if actual is not None:
        item.update(actual=actual, required=required)
    checks.append(item)
    if not ok:
        failures.append(item)
        raise AssertionError(name)


def poly(xs):
    return [F(x) for x in xs]


def ev(p, x):
    return sum((c * x**i for i, c in enumerate(p)), F(0))


def sign(x):
    return (x > 0) - (x < 0)


def variation(ss):
    ss = [s for s in ss if s]
    return sum(a != b for a, b in zip(ss, ss[1:]))


def endpoint(chain, rec, x, label):
    values = [ev(p, x) for p in chain]
    signs = [sign(v) for v in values]
    v = variation(signs)
    ck(label + ': coordinate, every value/sign, nonroot and variation',
       F(rec['q']) == x and poly(rec['values']) == values and
       rec['signs'] == signs and rec['variations'] == v and values[0] != 0)
    return v


def main():
    data = json.loads(read('scripts/heat/l938-zero-superlevel-58.json'))
    replay = json.loads(read('scripts/heat/l938-zero-superlevel-replay-58.json'))
    text = read('lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md')
    lemma = read('lemmas/L941-two-block-zero-superlevel-balancing-obstruction.md')
    ck('original producer checks complete and all successful',
       len(data['checks']) == 879 and all(c['ok'] is True for c in data['checks'])
       and data['failures'] == [])
    ck('original replay checks complete and all successful',
       len(replay['checks']) == replay['checks_count'] == 906 and
       all(c['ok'] is True for c in replay['checks']) and replay['failures'] == [])
    for rel, digest in data['input_sha256'].items():
        read(rel)
        ck('producer input hash: ' + rel, inputs[rel] == digest)
    read('scripts/heat/l938-zero-superlevel-replay-58.py')
    ck('replay input and implementation hashes',
       replay['input_sha256'] == inputs['scripts/heat/l938-zero-superlevel-58.json'] and
       replay['replay_script_sha256'] == inputs['scripts/heat/l938-zero-superlevel-replay-58.py'])
    old = json.loads(read('scripts/heat/l938-schur-obstruction-56.json'))
    rows = [(int(c), tuple(map(int, a.split(',')))) for c, a in re.findall(
        r'^\|\s*(-?\d+)\s*\|\s*\(([^)]+)\)\s*\|\s*$', text, re.M)]
    ck('exactly 34 distinct input rows', len(rows) == len({a for _, a in rows}) == 34)
    ck('certificate has exactly 34 rows and six blocks',
       len(data['rows']) == 34 and set(data['blocks']) == set(map(str, range(1, 7))))
    hs = {m: [F(0)] * 13 for m in range(1, 7)}
    balanced = F(0)
    for i, (c, alpha) in enumerate(rows):
        r = data['rows'][i]
        ks = [k for k, n in enumerate(alpha) for _ in range(n)]
        denom = prod(factorial(2*k) for k in ks)
        ck(f'row {i+1}: all twelve slots, weight and factorial denominator',
           len(alpha) == 7 and all(n >= 0 for n in alpha) and len(ks) == sum(ks) == 12
           and (r['row'], r['c'], tuple(r['alpha']), F(r['factorial_denominator'])) ==
           (i+1, c, alpha, denom))
        # Coefficients of product over TWELVE labelled slots (1+z*y^k).
        # Update one slot at a time; neither subset enumeration nor the old
        # binomial-multiplicity recurrence is reused.
        e = {(0, 0): 1}
        for k in ks:
            nxt = dict(e)
            for (m, j), count in e.items():
                nxt[m+1, j+k] = nxt.get((m+1, j+k), 0) + count
            e = nxt
        balanced += F(c, denom)
        for m in range(1, 7):
            counts = [e.get((m, j), 0) for j in range(13)]
            rh = [F(c*n, denom*comb(12, m)) for n in counts]
            ck(f'row {i+1}, m={m}: complete original and saved coefficient identities',
               sum(counts) == comb(12, m) and sum(rh) == F(c, denom) and
               counts == r['blocks'][str(m)]['counts'] and
               rh == poly(r['blocks'][str(m)]['H_coefficients']) and
               rh == poly(old['rows'][i]['blocks'][str(m)]['H_coefficients']))
            hs[m] = [a+b for a, b in zip(hs[m], rh)]
    # Independent rational evaluation of the stated finite Newton recurrence.
    q = [F((-1)**k, factorial(2*k)) for k in range(7)]
    ss = [F(0)]
    for n in range(1, 7):
        ss.append(-n*q[n] - sum(ss[j]*q[n-j] for j in range(1, n)))
    a, b, c, d, e = ss[2:7]
    det = a*c*e - a*d*d - b*b*e + 2*b*c*d - c*c*c
    ck('balanced value: rows and independent Newton determinant',
       balanced == det == F(1, 371319795000), str(balanced), '1/371319795000')
    canonical_coeffs = re.findall(r'm=(\d+), d=(\d+):\s*\(([^)]+)\)', lemma)
    ck('canonical coefficient table has exactly six entries', len(canonical_coeffs) == 6)
    summary_blocks = []
    for m in range(1, 7):
        label = f'm={m}'
        block = data['blocks'][str(m)]
        h = hs[m][:]
        ck(label + ': full previous polynomial including trailing zeros',
           h == poly(old['block_polynomials'][str(m)]['H_coefficients']))
        while h[-1] == 0:
            h.pop()
        n, factor = poly(block['integer_coefficients']), F(block['integer_positive_factor'])
        cm, cd, cc = canonical_coeffs[m-1]
        ck(label + ': full positive integer scaling and canonical coefficients',
           factor > 0 and n == [factor*x for x in h] and
           h == poly(block['H_coefficients']) and
           int(cm) == m and F(cd) == factor and
           poly(cc.replace('\n', '').split(',')) == n)
        degree = len(n)-1
        ck(label + ': degree and excluded degeneracies',
           len(n) > 1 and n[-1] != 0 and n[0] != 0 and
           degree == block['degree'] and block['excluded_zero_multiplicity'] == 0
           and block['zero_polynomial'] is False and block['constant_polynomial'] is False)
        record = block['sturm']
        chain = [poly(p) for p in record['polynomials']]
        s0, s1 = poly(record['initial_positive_factors'])
        ck(label + ': positive initial polynomial and derivative scales',
           s0 > 0 and s1 > 0 and chain[0] == [s0*x for x in n] and
           chain[1] == [s1*j*n[j] for j in range(1, len(n))])
        ck(label + ': complete nonzero canonical chain and division count',
           all(p and p[-1] != 0 for p in chain) and
           len(record['division_identities']) == len(chain)-1)
        for j, identity in enumerate(record['division_identities']):
            aa, bb = chain[j:j+2]
            qq, nn = poly(identity['quotient']), poly(identity['next'])
            f = F(identity['next_positive_factor'])
            ck(label + f', division {j}: linked next, positive scale and degree',
               f > 0 and nn == (chain[j+2] if j+2 < len(chain) else []) and
               len(nn) < len(bb) and identity['identity_verified'] is True)
            # Verify all coefficients as sparse rational polynomial identities.
            residual = {k: x for k, x in enumerate(aa)}
            for k, x in enumerate(qq):
                for ell, y in enumerate(bb):
                    residual[k+ell] = residual.get(k+ell, F(0)) - x*y
            for k, x in enumerate(nn):
                residual[k] = residual.get(k, F(0)) + x/f
            ck(label + f', division {j}: every rational residual coefficient zero',
               all(x == 0 for x in residual.values()))
        ck(label + ': Euclidean terminal constant, gcd and all multiplicities',
           len(chain[-1]) == 1 and chain[-1][0] != 0 and
           poly(block['primary_last_remainder']) == chain[-1] and
           block['terminal_monic_gcd'] == ['1'] and block['successive_gcds'] == [])
        bound = 1 + max(abs(x/n[-1]) for x in n[:-1])
        B = F(block['root_bound']['outer_integer'])
        ck(label + ': strict global Cauchy bound',
           B.denominator == 1 and B > bound == F(block['root_bound']['monic_Cauchy']),
           str(B), '> ' + str(bound))
        ck(label + ': exactly three global endpoints', len(block['global_endpoints']) == 3)
        vs = [endpoint(chain, rec, x, label + f' global {x}') for rec, x in
              zip(block['global_endpoints'], [F(0), F(1), B])]
        roots = block['roots']
        ck(label + ': global completeness and root count',
           vs[0]-vs[-1] == len(roots) == block['total_positive_roots'])
        prev, root_vars, isolators = F(0), [], []
        for j, r in enumerate(roots):
            lo, hi = F(r['lower']), F(r['upper'])
            ck(label + f' root {j+1}: index, disjoint ordering and side of one',
               r['index'] == j+1 and prev < lo < hi < B and (hi < 1 or lo > 1))
            va = endpoint(chain, r['left'], lo, label + f' root {j+1} lower')
            vb = endpoint(chain, r['right'], hi, label + f' root {j+1} upper')
            ck(label + f' root {j+1}: simple root and closed-set inclusion',
               va-vb == r['multiplicity'] == 1 and r['successive_gcd_counts'] == []
               and r['gcd_endpoints'] == [] and r['value_at_root'] == '0'
               and r['included_in_zero_superlevel'] is True)
            root_vars.append([va, vb])
            isolators.append([str(lo), str(hi)])
            prev = hi
        ck(label + ': correct number of complementary intervals',
           len(block['open_intervals']) == len(roots)+1)
        signs = []
        for j, interval in enumerate(block['open_intervals']):
            x = F(interval['sample'])
            lo = F(0) if j == 0 else F(roots[j-1]['upper'])
            hi = B+1 if j == len(roots) else F(roots[j]['lower'])
            val = ev(h, x)
            ck(label + f' interval {j}: linked interval and full rational sign value',
               interval['index'] == j and lo < x < hi and
               interval['left'] == ('0' if j == 0 else f'root_{j}') and
               interval['right'] == ('infinity' if j == len(roots) else f'root_{j+1}')
               and val == F(interval['H_at_sample']) and sign(val) == interval['sign'] != 0)
            signs.append(sign(val))
        ck(label + ': simple-root alternation and positive value at one',
           signs[0] == sign(n[0]) and all(a == -b for a, b in zip(signs, signs[1:]))
           and ev(h, F(1)) == balanced)
        expected_exits = []
        for j, r in enumerate(roots):
            inward = j+1 if F(r['upper']) < 1 else j
            ck(label + f' root {j+1}: correct inward side',
               r['inward_interval'] == inward and r['inward_sign'] == signs[inward])
            if signs[inward] < 0:
                interval = block['open_intervals'][inward]
                expected_exits.append({'root': j+1,
                    'q0_algebraic': f'unique root in ({F(r["lower"])},{F(r["upper"])})',
                    'q1': interval['sample'], 'q1_H': interval['H_at_sample']})
        exits = len(expected_exits)
        ck(label + ': every closed-set exit and preservation classification',
           block['inward_exits'] == expected_exits and
           block['zero_superlevel_inward_preserved'] == (exits == 0))
        tables.append({'m': m, 'degree': degree, 'B': str(B), 'V_0_1_B': vs,
                       'root_endpoint_variations': root_vars, 'isolators': isolators,
                       'interval_signs': signs, 'simple_roots': len(roots),
                       'roots_below_one': sum(F(r['upper']) < 1 for r in roots),
                       'exit_roots': [r['root'] for r in expected_exits]})
        expected_replay = {k: v for k, v in tables[-1].items() if k in
                           ['m', 'B', 'V_0_1_B', 'root_endpoint_variations',
                            'interval_signs', 'simple_roots']}
        expected_replay['inward_exits'] = exits
        ck(label + ': entire independent old replay table',
           replay['complete_tables'][m-1] == expected_replay)
        summary_blocks.append({'m': m, 'degree': degree, 'positive_roots': len(roots),
            'outer_root_bound': {'actual_B': str(B), 'required_strictly_greater_than': str(bound)},
            'multiplicities': [1]*len(roots), 'interval_signs': signs,
            'isolators': isolators, 'inward_exits': exits, 'preserved': exits == 0})
    # Compare both complete Markdown tables, including every rational isolator.
    printed_tables, printed_roots = [], []
    for line in lemma.splitlines():
        cells = [x.strip() for x in line.strip('|').split('|')]
        if len(cells) == 7 and cells[0].isdigit():
            printed_tables.append([int(cells[0]), int(cells[1]), cells[2],
                [int(x) for x in cells[3].split(',')], int(cells[4]),
                [1 if x == '+' else -1 for x in cells[5].split()], int(cells[6])])
        if len(cells) == 5 and cells[0].isdigit():
            printed_roots.append([int(cells[0]), int(cells[1]), cells[2], cells[3],
                                  [int(x) for x in cells[4].split(',')]])
    ck('canonical six complete root/sign/exit tables', printed_tables ==
       [[t['m'], t['degree'], t['B'], t['V_0_1_B'], t['simple_roots'],
         t['interval_signs'], len(t['exit_roots'])] for t in tables])
    ck('canonical sixteen complete isolators and endpoint variations', printed_roots ==
       [[t['m'], i+1, *iso, t['root_endpoint_variations'][i]]
        for t in tables for i, iso in enumerate(t['isolators'])])
    ck('canonical roots below one and exit identities',
       [t['roots_below_one'] for t in tables] == [0, 0, 0, 3, 1, 1] and
       [t['exit_roots'] for t in tables] == [[], [], [2], [2, 5], [3], []])
    ck('m=6 self reciprocity', hs[6] == hs[6][::-1])
    w = data['witness']
    q0, q1, rho = F(w['q0']), F(w['q1']), F(w['rho'])
    t0, t1 = poly(w['t0']), poly(w['t1'])
    n, f = poly(w['integer_polynomial']), F(w['integer_positive_factor'])
    ck('witness linked to actual m=4 polynomial and second isolator',
       w['m'] == 4 and n == poly(data['blocks']['4']['integer_coefficients']) and
       f == F(data['blocks']['4']['integer_positive_factor']) and
       [str(q0), str(q1)] == tables[3]['isolators'][1] == ['541/4096', '271/2048'])
    den = F(w['evaluation_denominator'])
    nums = [ev(n, q)*den for q in (q0, q1)]
    expected_nums = [240144996270454406660522410541398964574437280,
                     -240865490784023141273305086453025686705012736]
    ck('witness exact scaled integer evaluations and canonical numerators',
       den == 4096**12 and nums == expected_nums ==
       [F(w['N_q0_numerator']), F(w['N_q1_numerator'])] and
       all(str(x) in lemma for x in expected_nums))
    for q, t, j in [(q0, t0, 0), (q1, t1, 1)]:
        s = 4*q+8
        val = ev(hs[4], q)
        ck(f'witness endpoint {j}: normalized simplex and actual sign',
           t == [q/s]*4+[1/s]*8 and sum(t) == 1 and min(t) > 0 and
           F(w[f'H_q{j}']) == val and F(w[f'Pbar_t{j}']) == val/s**12 and
           sign(val) == (1 if j == 0 else -1))
    ck('canonical normalized vectors and mixture coefficient',
       t0 == [F(541, 34932)]*4+[F(1024, 8733)]*8 and
       t1 == [F(271, 17468)]*4+[F(512, 4367)]*8 and rho == F(5172847, 5174895)
       and all(s in lemma for s in ['541/34932', '1024/8733', '271/17468',
                                    '512/4367', 'rho=5172847/5174895']))
    ck('strict inward order and normalized-path mixture identity',
       0 < q0 < q1 < 1 and 0 < rho < 1 and
       rho == ((q1-1)/(12*(4*q1+8)))/((q0-1)/(12*(4*q0+8))) and
       all(y == rho*x+(1-rho)/12 for x, y in zip(t0, t1)))
    matrix = [[(rho if i == j else F(0))+(1-rho)/12 for j in range(12)]
              for i in range(12)]
    ck('every doubly stochastic matrix entry, row/column sum and image',
       min(min(row) for row in matrix) > 0 and all(sum(row) == 1 for row in matrix)
       and all(sum(matrix[i][j] for i in range(12)) == 1 for j in range(12))
       and [sum(row[j]*t0[j] for j in range(12)) for row in matrix] == t1)
    x, y = sorted(t0, reverse=True), sorted(t1, reverse=True)
    partials = [[str(sum(y[:k])), str(sum(x[:k]))] for k in range(1, 13)]
    ck('all eleven majorization inequalities and equal total independently',
       all(sum(y[:k]) <= sum(x[:k]) for k in range(1, 12)) and sum(x) == sum(y) == 1)
    ck('producer entire mathematical summary', data['summary'] == {
        'result': 'INWARD_EXIT_OBSTRUCTION',
        'required': 'no inward negative interval adjacent to any positive root',
        'blocks': summary_blocks, 'checks': 879, 'failures': 0,
        'witness': {'m': 4, 'q0': str(q0), 'q1': str(q1),
                    'actual_scaled_N_q0': str(nums[0]), 'actual_scaled_N_q1': str(nums[1]),
                    'required_signs': ['>0', '<0']},
        'certificate': 'scripts/heat/l938-zero-superlevel-58.json'})
    return {'scaled_witness_numerators': [str(x) for x in nums],
            'required_signs': ['>0', '<0'], 'rho': str(rho),
            'sorted_partial_sums_t1_t0': partials}


result = {'task': 'Independent exact and logical evidence audit of unchanged L941',
          'arithmetic': 'Python integers/Fraction; no producer code imported'}
try:
    result['witness'] = main()
except Exception as exc:
    failures.append({'exception': type(exc).__name__, 'message': str(exc)})
result.update(input_sha256=inputs, script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
              checks=checks, checks_count=len(checks), failures=failures, tables=tables)
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'result': 'PASS' if not failures else 'FAILED',
                  'checks': len(checks), 'failures': failures,
                  'root_counts': [t['simple_roots'] for t in tables],
                  'exit_roots': [t['exit_roots'] for t in tables],
                  'actual_total_roots': sum(t['simple_roots'] for t in tables),
                  'required_total_roots': 16,
                  'root_bounds': [{'block': c['name'].split(':')[0],
                                   'actual_B': c['actual'], 'required': c['required']}
                                  for c in checks
                                  if c['name'].endswith(': strict global Cauchy bound')],
                  'witness': result.get('witness', {}).get('scaled_witness_numerators'),
                  'certificate': str(OUT.relative_to(ROOT))}, indent=2))
raise SystemExit(bool(failures))
