"""Independent L061 audit; reads every certificate record, imports no prior code.

All arithmetic uses exact integers and polynomial remainders. Uniform local
field and realization arguments are audited in L061, not inferred from a run.
"""
import hashlib
import json
from math import comb
from pathlib import Path

BASE = Path(__file__).resolve().parent
c = json.loads((BASE / 'certificate.json').read_text())
v = json.loads((BASE / 'verification.json').read_text())
checks, evidence = {}, {}


def check(name, value):
    checks[name] = bool(value)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b)))])


def scale(a, z):
    return trim([z * t for t in a])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def rem(a, f, modulus):
    a = trim([z % modulus for z in a])
    while len(a) >= len(f) and a != [0]:
        k = len(a)-len(f)
        z = a[-1]*pow(f[-1], -1, modulus) % modulus
        a = trim([(t - (z*f[i-k] if k <= i < k+len(f) else 0)) % modulus
                  for i, t in enumerate(a)])
    return a


def ppow(a, n, f, m):
    out = [1]
    for bit in bin(n)[2:]:
        out = rem(mul(out, out), f, m)
        if bit == '1':
            out = rem(mul(out, a), f, m)
    return out


def gcd(a, b):
    a, b = trim([z % 5 for z in a]), trim([z % 5 for z in b])
    while b != [0]:
        a, b = b, rem(a, b, 5)
    return [z*pow(a[-1], -1, 5) % 5 for z in a]


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))])


def ev(p, x):
    out = 0
    for z in reversed(p):
        out = out*x+z
    return out


H = [3, 1, 2, 0, 4, 4, 2, 3, 1, 4, 3, 1]
q = 5**11


def vec(a, m=125):
    a = rem(a, H, m)
    return a + [0]*(11-len(a))


def rmul(a, b, m=125):
    return vec(mul(a, b), m)


def rpow(a, n, m=125):
    return vec(ppow(a, n, H, m), m)


def rev(p, x, m=125):
    out = [0]
    for z in reversed(p):
        out = rem(add(mul(out, x), [z]), H, m)
    return vec(out, m)


def label(a):
    z = rpow(a, q-1, 25)
    assert vec(z, 5) == vec([1])
    return [((t-int(i == 0)) % 25)//5 for i, t in enumerate(z)]


src = c['source_polynomials']
canonical = json.loads((BASE.parent / 'five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
check('every_source_coefficient_matches_audited_L034', src == canonical)
a, b, d, h, J, g = [src[k] for k in ['a', 'b', 'd', 'h', 'jcoef', 'g']]
h3 = mul(mul(h, h), h)


def fs(s):
    return add(add(h3, scale(J, s)), scale(d, -s*s))


identity = add(add(mul(a, a), scale(mul(a, b), -1)),
               add(scale(mul(mul(b, b), g), -1), mul(d, h3)))
check('source_definitions_and_elimination',
      b == mul(src['b1'], src['b2']) and J == add(scale(a, 2), scale(b, -1))
      and d == [comb(11, i)*(-16)**(11-i) for i in range(12)]
      and h == [9789217, 4971236, 1333262, -52820, 1]
      and g == [-20, -10, -1, 1] and identity == [0]
      and src['F_at_1'] == fs(1)
      and src['f_numerator_at_1'] == add(mul([-55, 30, -4], b), mul([-4, 1], add(d, scale(a, -1)))))
evidence['integer_elimination_residual'] = identity
chart = {'h16': ev(h, 16), 'J16': ev(J, 16), 'b16': ev(b, 16),
         'a16': ev(a, 16), 'h16_cubed_minus_121J16': ev(h3, 16)-121*ev(J, 16),
         'Fminus121_at16': ev(fs(-121), 16),
         'T_numerator_residual': ev(a, 5)+5*ev(b, 5)+24729001*ev(d, 5),
         'twoT_numerator': ev(a, 16)-61*ev(b, 16),
         'threeT_numerator': ev(a, 16)+60*ev(b, 16)}
evidence['charts'] = chart
check('all_removable_and_exceptional_charts', chart['h16_cubed_minus_121J16'] == 0
      and chart['Fminus121_at16'] == 0 and chart['J16'] != 0
      and chart['b16'] % 5 != 0 and chart['twoT_numerator'] == 0
      and chart['T_numerator_residual'] == 0 and chart['threeT_numerator'] == 11**22
      and (-121) % 5 == (-24729001) % 5 == 4)
check('model_and_precision', c['model']['H'] == H and c['model']['modulus'] == 125
      and c['model']['residue_order'] == q)
evidence['factor_tests'] = {}
for s in (2, 4):
    stored = c['factors'][str(s)]
    factors = [stored['linear'], stored['degree_eleven']] if s == 2 else stored['factors']
    full, tests = [1], []
    for f in factors:
        full = mul(full, f)
        degree = len(f)-1
        seq = [[0, 1]]
        for _ in range(degree):
            seq.append(ppow(seq[-1], 5, f, 5))
        proper = gcd(f, add(ppow([0, 1], 5, f, 5), [0, -1])) if degree > 1 else [1]
        # Degrees here are 1, 5 or 11: the only proper divisor is one.
        tests.append({'factor': f, 'frobenius': seq, 'proper_degree_gcd': proper,
                      'separability_gcd': gcd(f, derivative(f))})
        check(f'factor_{s}_{len(tests)}_irreducible', degree in (1, 5, 11)
              and seq[-1] == rem([0, 1], f, 5) and proper == [1]
              and gcd(f, derivative(f)) == [1])
    actual = [z % 5 for z in fs(s)]
    evidence['factor_tests'][str(s)] = {'F': actual, 'tests': tests,
        'b_gcd': gcd(actual, b), 'derivative_gcd': gcd(actual, derivative(actual)),
        'degrees': [len(f)-1 for f in factors]}
    check(f'full_factors_{s}_from_source', [z % 5 for z in full] == actual == stored['F_mod5']
          and gcd(actual, b) == [1] and gcd(actual, derivative(actual)) == [1]
          and all(gcd(f, e) == [1] for i, f in enumerate(factors) for e in factors[:i]))
    check(f'full_degrees_{s}', [len(f)-1 for f in factors] == ([1, 11] if s == 2 else [1, 1, 5, 5]))
    if s == 4:
        check('stored_quintic_irreducibility_evidence', all(
            old['factor'] == new['factor']
            and old['frobenius'] == [[vec([z]) for z in p] for p in new['frobenius']]
            and old['proper_degree_gcds'] == ([] if len(new['factor']) == 2 else [[vec([1])]])
            for old, new in zip(stored['irreducibility'], tests)) and len(stored['irreducibility']) == 4)
roots = c['factors']['2']['roots']
orbit, z = [], vec([0, 1])
for _ in range(12):
    orbit.append(z)
    z = rpow(z, 5, 5)
check('model_frobenius_and_all_embeddings', orbit == c['model']['frobenius']
      and orbit[-1] == orbit[0] and len({tuple(z) for z in orbit[:-1]}) == 11
      and roots == sorted(orbit[:-1]) and c['factors']['2']['degree_eleven'] == H)
z, actual_orbit = roots[0], []
for _ in range(11):
    actual_orbit.append(z)
    z = rpow(z, 5, 5)
check('stored_root_orbit', actual_orbit == c['factors']['2']['frobenius_orbit']
      and z == roots[0] and c['factors']['2']['splitting_trials'] == [])
check('maximal_ring_separability', gcd(H, derivative(H)) == [1])

rows, classes = c['records'], c['classes']
check('all_275_scalar_embedding_pairs', len(rows) == 275 and
      {(r['s'], r['embedding']) for r in rows} == {(s, i) for s in range(2, 125, 5) for i in range(11)})
row_tests = []
for idx, row in enumerate(rows):
    s, x, y = row['s'], row['x'], row['y']
    f = vec(add(mul(add(x, [-4]), y), add(scale(mul(x, x), -4), add(scale(x, 30), [-55]))))
    residuals = {'F': rev(fs(s), x), 'curve': vec(add(add(mul(y, y), y), scale(rev(g, x), -1))),
                 'map': vec(add(add(rev(a, x), mul(rev(b, x), y)), scale(rev(d, x), -s)))}
    okay = all(t == vec([0]) for t in residuals.values()) and f == row['f']
    okay &= (vec(x, 5) == row['residue_x'] == roots[row['embedding']]
             and rev(derivative(fs(s)), x, 5) != vec([0]) and rev(b, x, 5) != vec([0])
             and vec(f, 5) != vec([0]) and label(f) == row['label'])
    row_tests.append({'record': idx, 'residuals': residuals, 'computed_label': label(f), 'passed': okay})
check('every_coordinate_value_and_label', all(r['passed'] for r in row_tests))
evidence['row_tests'] = row_tests

# Independently lift the rational point by exhaustive base-five digits.
# This cross-checks norm reconstruction against an actual full-fiber component.
rational_tests = []
for s in range(2, 125, 5):
    x, modulus = 0, 5
    for _ in range(2):
        candidates = [x+modulus*i for i in range(5) if ev(fs(s), x+modulus*i) % (5*modulus) == 0]
        assert len(candidates) == 1
        x, modulus = candidates[0], 5*modulus
    y = (s*ev(d, x)-ev(a, x))*pow(ev(b, x), -1, 125) % 125
    f = ((x-4)*y-4*x*x+30*x-55) % 125
    n = vec([1])
    relevant = [r for r in rows if r['s'] == s]
    for row in relevant:
        n = rmul(n, row['f'])
    beta = 121*pow(n[0], -1, 125) % 125
    ratio = f*pow(beta, -1, 125) % 125
    witnesses = [w for w in range(125) if w % 5 and pow(w, 5, 125) == ratio]
    okay = (n[1:] == [0]*10 and all(r['norm'] == n[0] and r['rational_representative'] == beta for r in relevant)
            and f % 5 != 0 and (y*y+y-ev(g, x)) % 125 == 0
            and f*n[0] % 125 == pow(11, 22, 125)*pow(s+24729001, 5, 125) % 125 and len(witnesses) == 5)
    rational_tests.append({'s': s, 'x': x, 'y': y, 'f': f, 'U_norm': n,
                           'beta': beta, 'ratio_fifth_roots': witnesses, 'passed': okay})
check('all_norms_direct_rational_points_and_classes', all(t['passed'] for t in rational_tests))
evidence['rational_tests'] = rational_tests

check('55_classes_and_full_partition', len(classes) == 55 and
      sorted(i for cls in classes for i in cls['members']) == list(range(275)) and
      all(len(cls['members']) == 5 for cls in classes))
class_tests = []
for i, cls in enumerate(classes):
    row = rows[cls['representative_record']]
    explicit = vec(add([1], scale(cls['label'], -5)))
    okay = (cls['f'] == row['f'] and cls['label'] == label(row['f'])
            and cls['rational_representative'] == row['rational_representative']
            and cls['explicit_U_representative'] == explicit and label(explicit) == cls['label']
            and rmul(rpow(cls['explicit_representative_fifth_root'], 5), explicit) == row['f']
            and {(rows[j]['s'], rows[j]['embedding']) for j in cls['members']} ==
                {(row['s']+25*k, row['embedding']) for k in range(5)}
            and row['s'] in (2, 7, 12, 17, 22) and row['class_index'] == i)
    class_tests.append({'class': i, 'label': cls['label'], 'beta': cls['rational_representative'], 'passed': okay})
check('all_55_representatives_and_exact_collision_pattern', all(t['passed'] for t in class_tests))
evidence['class_tests'] = class_tests
collision_tests = []
for w in c['collisions']:
    row, cls = rows[w['record']], classes[w['class']]
    U = rmul(rpow(w['U_fifth_root'], 5), cls['f'])
    rational = pow(w['Q5_fifth_root'], 5, 125)*cls['rational_representative'] % 125
    okay = (U == row['f'] and rational == row['rational_representative']
            and row['class_index'] == w['class'] and w['record'] in cls['members']
            and row['label'] == cls['label'] and vec(w['U_fifth_root'], 5) != vec([0])
            and w['Q5_fifth_root'] % 5 != 0)
    collision_tests.append({'record': w['record'], 'U_fifth_power_times_representative': U,
                            'rational_fifth_power_times_representative': rational, 'passed': okay})
check('all_275_collision_roots_in_both_factors', len(collision_tests) == 275
      and sorted(t['record'] for t in collision_tests) == list(range(275)) and all(t['passed'] for t in collision_tests))
evidence['collision_tests'] = collision_tests
noncollision_tests = []
for w in c['noncollisions']:
    i, j, k = w['i'], w['j'], w['coordinate']
    diff = (classes[i]['label'][k]-classes[j]['label'][k]) % 5
    noncollision_tests.append({'i': i, 'j': j, 'coordinate': k, 'difference': diff,
                              'passed': diff == w['difference'] and diff != 0})
check('all_1485_noncollision_pairs', len(noncollision_tests) == 1485
      and {(t['i'], t['j']) for t in noncollision_tests} == {(i, j) for i in range(55) for j in range(i)}
      and all(t['passed'] for t in noncollision_tests))
evidence['noncollision_tests'] = noncollision_tests
table = [(2, 38, [4,3,0,2,4,4,2,4,0,1,0]), (7, 123, [1,4,1,4,2,4,2,0,0,0,1]),
         (12, 108, [3,0,2,1,0,4,2,1,0,4,2]), (17, 118, [0,1,3,3,3,4,2,2,0,3,3]),
         (22, 28, [2,2,4,0,1,4,2,3,0,2,4])]
orbit_tests = []
for s, beta, w in table:
    pairs, z, x = [], w, vec([0, 1])
    okay = True
    for _ in range(11):
        row = next(r for r in rows if r['s'] == s and r['residue_x'] == x)
        okay &= row['label'] == z and row['rational_representative'] == beta
        pairs.append({'residue_x': x, 'label': z})
        x, z = rpow(x, 5, 5), rpow(z, 5, 5)
    okay &= z == w and len({tuple(p['label']) for p in pairs}) == 11
    orbit_tests.append({'s': s, 'beta': beta, 'orbit': pairs, 'passed': okay})
check('all_five_displayed_seed_orbits', all(t['passed'] for t in orbit_tests))
evidence['orbit_tests'] = orbit_tests
expected_list = [{'class': i, 'label': cls['label'], 'rational_representative': cls['rational_representative'],
                  's': rows[cls['representative_record']]['s'], 'embedding': rows[cls['representative_record']]['embedding'],
                  'U_representative': cls['explicit_U_representative'], 'members': cls['members']}
                 for i, cls in enumerate(classes)]
check('entire_prior_verification_list', v['exact_list'] == expected_list)
check('prior_summaries_and_checks', v['summary'] == {'records_verified': 275, 'classes_verified': 55,
      'collision_witnesses_verified': 275, 'noncollision_pairs_verified': 1485,
      'required_records': 275, 'prior_bound': 600} and c['summary'] == {
      'candidate_pairs': 275, 'exact_class_count': 55, 'required_pairs': 275,
      'excluded_scalar_residue': 4, 'prior_upper_bound': 600, 'checks': 26}
      and len(c['checks']) == 26 and len(v['checks']) == 23
      and all(c['checks'].values()) and all(v['checks'].values()) and c['failures'] == v['failures'] == [])
out = {'input_sha256': {name: hashlib.sha256((BASE/name).read_bytes()).hexdigest()
                       for name in ('certificate.json', 'verification.json')},
       'summary': {'actual_pairs': len(rows), 'required_pairs': 275, 'actual_classes': len(classes),
                   'required_class_comparisons': 55, 'collision_pairs': len(collision_tests),
                   'noncollision_pairs': len(noncollision_tests), 'required_noncollision_pairs': 1485,
                   'direct_rational_realizations': len(rational_tests), 'prior_upper_bound': 600},
       'checks': checks, 'failures': [name for name, ok in checks.items() if not ok], 'evidence': evidence}
path = BASE / 'audit-certificate.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print('Audit:', out['summary'])
print('Checks:', len(checks), 'failures:', out['failures'])
print('Full certificate:', path.relative_to(BASE.parent.parent))
assert not out['failures']
