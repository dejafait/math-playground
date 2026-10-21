"""Exact finite checks for the fixed-valuation coalescence obstruction.

The all-horizon proof is L026. Trees are complete through each tested
horizon, with both zero clocks and no pruning by size or slope.
"""
from fractions import Fraction
import json
from pathlib import Path

OUT = Path(__file__).with_name('certificate.json')


def T(n):
    return (3*n+1)//2 if n % 2 else n//2


anchor = [47]
while anchor[-1] != 1:
    anchor.append(T(anchor[-1]))
assert len(anchor) == 67 and anchor[59] == 40
assert max(anchor[59:] + [2]) == 40
comparisons = []
for h in range(1, 54):
    b = 0
    while 3**b <= 2**h:
        b += 1
    margin = 243*3**b - 244*2**h
    assert margin > 0
    comparisons.append({'h': h, 'least_b': b, 'strict_margin': margin})
maximum = max(comparisons, key=lambda row: Fraction(2**row['h'], 3**row['least_b']))
assert maximum['h'] == 19 and maximum['least_b'] == 12


def check(L):
    ternary, binary = 3**(L+4), 2**(L+1)
    binary_residue = -97*pow(81, -1, binary) % binary
    modulus = ternary*binary
    residue = 47 + ternary*((binary_residue-47)*pow(ternary, -1, binary) % binary)
    threshold = 12**L
    n = residue + max(0, (threshold-residue)//modulus+1)*modulus
    assert n > threshold and n % 243 == 47 and n % 32 == 15
    assert (n-47) % (64*ternary) == 0
    assert (81*n+97) % binary == 0
    endpoint, trees, hits = n, [], []
    counts = {'nodes': 0, 'slope_above_one': 0, 'slope_equal_one': 0,
              'slope_below_one': 0, 'residue20_anchor_checks': 0}
    for t in range(L+1):
        q = Fraction(1) if t <= 4 else Fraction(97, 81)
        coefficient = Fraction(3**t, 2**t) if t <= 4 else Fraction(3**(t-1), 2**t)
        Y = coefficient*(47+q)-1
        assert endpoint+1 == coefficient*(n+q)
        states, layers = [(endpoint, '', coefficient, Fraction(0))], []
        for s in range(L+1):
            layer = []
            for c, word, slope, offset in states:
                counts['nodes'] += 1
                assert c > 0 and c+1 == slope*(n+q)-offset
                assert 0 <= offset <= 2**s-1
                a, h = word.count('O'), s-t
                assert slope == coefficient*Fraction(2**s, 3**a)
                if slope > 1:
                    counts['slope_above_one'] += 1
                    assert slope-1 >= Fraction(1, 6**L) and c > n
                else:
                    counts['slope_equal_one' if slope == 1 else 'slope_below_one'] += 1
                    c0 = slope*(47+q)-offset-1
                    assert h >= (0 if t <= 4 else -2)
                    assert c0.denominator == 1 and c0 <= 47
                    c0 = int(c0)
                    assert (c-c0) % (27*2**(h+6)) == 0
                    p = min(s, h+6)
                    actual, at_anchor = c, c0
                    forward = word[::-1]
                    for branch in forward[:p]:
                        assert actual % 2 == at_anchor % 2 == (branch == 'O')
                        actual, at_anchor = T(actual), T(at_anchor)
                    formal = Fraction(at_anchor)
                    for branch in forward[p:]:
                        formal = (3*formal+1)/2 if branch == 'O' else formal/2
                    assert formal == Y
                    if c % 27 == 20 and c < n:
                        counts['residue20_anchor_checks'] += 1
                        assert c0 <= 20 or c0 == 47
                        if c0 == 47:
                            assert t >= 5 and slope < 1
                            assert slope >= Fraction(243, 244) and h >= 54
                        assert at_anchor <= 40
                        bound = 41*Fraction(3, 2)**(s-p)-1
                        assert formal <= bound < Y  # would contradict equality
                if c < n and c % 27 == 20:
                    hits.append({'c': c, 's': s, 't': t, 'inverse_word': word})
                layer.append({'c': c, 'inverse_word': word})
            layers.append(layer)
            if s < L:
                nxt = []
                for c, word, slope, offset in states:
                    nxt.append((2*c, word+'E', 2*slope, 2*offset+1))
                    if c % 3 == 2:
                        nxt.append(((2*c-1)//3, word+'O', Fraction(2, 3)*slope,
                                    Fraction(2, 3)*offset))
                states = nxt
        trees.append({'t': t, 'endpoint': endpoint, 'inverse_layers': layers})
        if t < L:
            assert endpoint % 2 == (0 if t == 4 else 1)
            endpoint = T(endpoint)
    assert not hits
    return {'L': L, 'root': n, 'required_strict_lower_bound': threshold,
            'initial_valuation': 4, 'required_initial_valuation': 4,
            'CRT_modulus': modulus, 'counts': counts, 'failures': hits, 'trees': trees}


cases = [check(L) for L in (6, 8, 12, 20)]
certificate = {'purpose': 'Finite exact evidence supporting L026; not an all-horizon enumeration',
               'anchor_orbit': anchor, 'anchor_tail_from': 59, 'anchor_tail_bound': 40,
               'slope_comparisons': comparisons, 'maximal_small_h_slope': maximum,
               'cases': cases}
OUT.write_text(json.dumps(certificate, separators=(',', ':'))+'\n')
print('Anchor: T^59(47)=40, tail maximum=40, T^66(47)=1; required tail bound <=40.')
print('All 53 slope margins positive; maximum below-one slope = 2^19/3^12 < 243/244.')
for case in cases:
    print('L={L}: root={root} > required={required_strict_lower_bound}; '
          'v2(n+1)={initial_valuation}, required={required_initial_valuation}; '
          'counts={counts}; failures={failures}'.format(**case))
print('Full certificate:', OUT)
