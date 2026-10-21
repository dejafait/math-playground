"""Finite transcription checks for L025; the all-L proof is in the lemma."""
from fractions import Fraction
import json
from pathlib import Path

OUT = Path(__file__).with_name('certificate.json')

def T(n):
    return (3*n+1)//2 if n % 2 else n//2

def check(L):
    ternary, binary = 3**(L+3), 2**(L+1)
    modulus = ternary*binary
    residue = 47 + ternary*((-48)*pow(ternary, -1, binary) % binary)
    threshold = 12**L
    n = residue + max(0, (threshold-residue)//modulus+1)*modulus
    assert n > threshold and n % 243 == 47
    assert (n-47) % ternary == 0 and (n+1) % binary == 0
    endpoint = n
    trees, hits = [], []
    counts = {'nodes': 0, 'slope_below_one': 0, 'slope_equal_one': 0,
              'slope_above_one': 0, 'transferred_prefixes': 0}
    for t in range(L+1):
        assert endpoint == Fraction(3, 2)**t*(n+1)-1
        # Each entry retains an inverse word and its exact shifted affine map.
        states = [(endpoint, '', Fraction(3, 2)**t, Fraction(0))]
        layers = []
        for s in range(L+1):
            layer = []
            for c, word, slope, offset in states:
                counts['nodes'] += 1
                assert c > 0 and c+1 == slope*(n+1)-offset
                assert 0 <= offset <= 2**s-1
                a = word.count('O')
                assert slope == Fraction(2**s*3**t, 2**t*3**a)
                if slope > 1:
                    counts['slope_above_one'] += 1
                    assert slope-1 >= Fraction(1, 6**L) and c > n
                elif slope == 1:
                    counts['slope_equal_one'] += 1
                    assert s == t == a and offset == 0 and c == n
                else:
                    counts['slope_below_one'] += 1
                    assert s > t and a > t
                    c0 = slope*48-offset-1
                    assert c0.denominator == 1 and c0 < 47
                    c0 = int(c0)
                    assert (c-c0) % (27*2**(s-t)) == 0
                    actual, anchor = c, c0
                    forward = word[::-1]
                    for branch in forward[:s-t]:
                        assert actual % 2 == anchor % 2 == (branch == 'O')
                        actual, anchor = T(actual), T(anchor)
                    counts['transferred_prefixes'] += 1
                    formal = Fraction(anchor)
                    for branch in forward[s-t:]:
                        formal = (3*formal+1)/2 if branch == 'O' else formal/2
                    assert formal == Fraction(3, 2)**t*48-1
                    assert c0 % 27 != 20
                if c < n and c % 27 == 20:
                    hits.append({'c': c, 's': s, 't': t, 'inverse_word': word})
                layer.append({'c': c, 'inverse_word': word})
            layers.append(layer)
            if s < L:
                nxt = []
                for c, word, slope, offset in states:
                    nxt.append((2*c, word+'E', 2*slope, 2*offset+1))
                    if c % 3 == 2:
                        nxt.append(((2*c-1)//3, word+'O',
                                    Fraction(2, 3)*slope, Fraction(2, 3)*offset))
                states = nxt
        trees.append({'t': t, 'endpoint': endpoint, 'inverse_layers': layers})
        if t < L:
            assert endpoint % 2 == 1
            endpoint = T(endpoint)
    assert not hits
    return {'L': L, 'root': n, 'required_strict_lower_bound': threshold,
            'CRT_modulus': modulus, 'counts': counts, 'failures': hits, 'trees': trees}

cases = [check(L) for L in (1, 4, 8, 12, 20)]
OUT.write_text(json.dumps({'purpose': 'Finite checks only; not the all-L proof',
                           'cases': cases}, separators=(',', ':'))+'\n')
for case in cases:
    print('L={L}: root={root} > required={required_strict_lower_bound}; '
          'counts={counts}; failures={failures}'.format(**case))
print('Full certificate:', OUT)
