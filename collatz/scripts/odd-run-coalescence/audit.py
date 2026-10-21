"""Independent verification of the complete finite evidence used by L026.

Reads, but does not overwrite, check.py's certificate. Forward replay and
forward affine coefficients check each inverse-tree node independently.
This does not verify the all-horizon argument; see the canonical proof.
"""
from fractions import Fraction
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'certificate.json').read_text())
failures = []


def require(condition, label):
    if not condition:
        failures.append(label)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


rows = data['slope_comparisons']
require([r['h'] for r in rows] == list(range(1, 54)), 'slope range')
for r in rows:
    h, b = r['h'], r['least_b']
    require(3**(b-1) <= 2**h < 3**b, f'least exponent {h}')
    require(r['strict_margin'] == 243*3**b-244*2**h > 0,
            f'strict margin {h}')
proof = (HERE.parents[1] / 'lemmas/L026-fixed-valuation-residue47-coalescence-obstruction.md').read_text()
table_rows = re.findall(r'^\| (\d+)–(\d+) \| ([\d,]+) \| (\d+) \|$', proof, re.M)
require(len(table_rows) == 6, 'canonical slope table rows')
for low, high, exponents, margin in table_rows:
    selected = rows[int(low)-1:int(high)]
    require([r['least_b'] for r in selected] == list(map(int, exponents.split(','))),
            f'canonical exponent row {low}')
    require(min(r['strict_margin'] for r in selected) == int(margin),
            f'canonical margin row {low}')

orbit = data['anchor_orbit']
require(orbit[0] == 47 and len(orbit) == 67 and orbit[-1] == 1,
        'anchor endpoints and length')
for j, (x, y) in enumerate(zip(orbit, orbit[1:])):
    require(step(x) == y, f'anchor edge {j}')
require(orbit[59] == 40 and max(orbit[59:]+[2]) == 40,
        'anchor bound from step 59')
require(step(1) == 2 and step(2) == 1, 'anchor terminal cycle')

case_results = []
for case in data['cases']:
    L, n = case['L'], case['root']
    require(L >= 6 and n > 12**L, f'root height {L}')
    require((n-47) % 3**(L+4) == 0 and (81*n+97) % 2**(L+1) == 0,
            f'root congruences {L}')
    require((n+1) % 32 == 16, f'exact initial valuation {L}')
    require(len(case['trees']) == L+1, f'complete time range {L}')
    current, nodes, hits, transferred, exceptional = n, 0, 0, 0, 0
    for t, tree in enumerate(case['trees']):
        require(tree['t'] == t and tree['endpoint'] == current,
                f'actual root endpoint {L}/{t}')
        K = Fraction(3**t if t <= 4 else 3**(t-1), 2**t)
        q = Fraction(1) if t <= 4 else Fraction(97, 81)
        require(current+1 == K*(n+q), f'root affine {L}/{t}')
        expected = [(current, '')]
        require(len(tree['inverse_layers']) == L+1, f'complete depth range {L}/{t}')
        for s, layer in enumerate(tree['inverse_layers']):
            require([(r['c'], r['inverse_word']) for r in layer] == expected,
                    f'complete guarded layer {L}/{t}/{s}')
            following = []
            for row in layer:
                c, word = row['c'], row['inverse_word']
                nodes += 1
                require(c > 0 and len(word) == s, 'positive node and word length')
                x, alpha, beta = c, Fraction(1), Fraction(0)
                for symbol in reversed(word):
                    require((x % 2 == 1) == (symbol == 'O'), 'actual companion parity')
                    x = step(x)
                    if symbol == 'O':
                        alpha, beta = 3*alpha/2, (3*beta+1)/2
                    else:
                        alpha, beta = alpha/2, beta/2
                require(x == current and alpha*c+beta == current,
                        'complete forward replay and affine identity')
                slope = K/alpha
                offset = (beta+1)/alpha-1
                require(0 <= offset <= 2**s-1, 'offset bounds')
                if slope > 1:
                    require(c > n and slope-1 >= Fraction(1, 6**L), 'large slope')
                else:
                    c0 = (K*(47+q)-1-beta)/alpha
                    h = s-t
                    require(h >= (0 if t <= 4 else -2), 'prefix exponent nonnegative')
                    require(c0.denominator == 1 and c0 <= 47, 'integer anchor bound')
                    c0 = int(c0)
                    require((c-c0) % (27*2**(h+6)) == 0, 'anchor transfer congruences')
                    p = min(s, h+6)
                    a0, actual = c0, c
                    for _ in range(p):
                        require(a0 % 2 == actual % 2, 'transferred actual parity')
                        a0, actual = step(a0), step(actual)
                    transferred += 1
                    if c < n and c % 27 == 20:
                        exceptional += int(c0 == 47)
                hits += int(c < n and c % 27 == 20)
                following.append((2*c, word+'E'))
                if c % 3 == 2:
                    following.append(((2*c-1)//3, word+'O'))
            expected = following
        current = step(current)
    require(nodes == case['counts']['nodes'] and hits == 0, f'tree totals {L}')
    case_results.append({'L': L, 'actual_root': n, 'required_root_above': 12**L,
                         'nodes_replayed': nodes, 'actual_hits': hits, 'required_hits': 0,
                         'transferred_nodes': transferred, 'exceptional_nodes': exceptional})

result = {'scope': 'Independent complete finite evidence audit; all-horizon proof audited in L026',
          'slope_rows_checked': len(rows), 'required_slope_rows': 53,
          'minimum_strict_margin': min(r['strict_margin'] for r in rows),
          'anchor_edges_checked': len(orbit)-1, 'required_anchor_edges': 66,
          'actual_tail_bound': 40, 'required_tail_bound_at_most': 40,
          'cases': case_results, 'failures': failures}
out = HERE / 'audit-certificate.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print(f'Slope rows: {len(rows)}/53; minimum strict margin {result["minimum_strict_margin"]} > 0.')
print(f'Anchor edges: {len(orbit)-1}/66; tail bound 40 <= required 40 from step 59.')
for case in case_results:
    print(f'L={case["L"]}: root {case["actual_root"]} > {case["required_root_above"]}; '
          f'{case["nodes_replayed"]} complete node replays; hits {case["actual_hits"]}, required 0; '
          f'exceptional nodes exercised {case["exceptional_nodes"]}.')
print('Failures:', failures)
print('Full audit certificate:', out)
raise SystemExit(bool(failures))
