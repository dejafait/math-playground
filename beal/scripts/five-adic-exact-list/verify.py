"""Replay every certificate row with separate arithmetic; not a proof audit."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
c = json.loads((BASE/'certificate.json').read_text())
H, n, q = c['model']['H'], 11, 5**11
zero, one = [0]*11, [1]+[0]*10
checks = {}


def add(a, b, m=125): return [(x+y) % m for x, y in zip(a, b)]
def scale(a, k, m=125): return [x*k % m for x in a]


def multiply(a, b, m=125):
    result = [0]*21
    for k in range(21):
        result[k] = sum(a[i]*b[k-i] for i in range(max(0, k-10), min(10, k)+1)) % m
    for k in reversed(range(11, 21)):
        for j in range(11): result[k-11+j] = (result[k-11+j]-result[k]*H[j]) % m
    return result[:11]


def power(a, exponent, m=125):
    value = one
    for digit in bin(exponent)[2:]:
        value = multiply(value, value, m)
        if digit == '1': value = multiply(value, a, m)
    return value


def evaluate(p, x, m=125):
    value, xpower = zero, one
    for coefficient in p:
        value = add(value, scale(xpower, coefficient, m), m)
        xpower = multiply(xpower, x, m)
    return value


def invariant(a):
    v = power(a, q-1, 25)
    assert [x % 5 for x in v] == one
    return [((x-int(i == 0)) % 25)//5 for i, x in enumerate(v)]


def pmul(a, b, m=5):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] = (out[i+j]+x*y) % m
    return out


def remainder(a, b):
    a = [x % 5 for x in a]
    while len(a) > 1 and a[-1] == 0: a.pop()
    while len(a) >= len(b) and a != [0]:
        j, v = len(a)-len(b), a[-1]*pow(b[-1], -1, 5) % 5
        for i, x in enumerate(b): a[i+j] = (a[i+j]-v*x) % 5
        while len(a) > 1 and not a[-1]: a.pop()
    return a


def fpow(a, e, f):
    z = [1]
    while e:
        if e & 1: z = remainder(pmul(z, a), f)
        a = remainder(pmul(a, a), f)
        e >>= 1
    return z


def gcd(a, b):
    while b != [0]: a, b = b, remainder(a, b)
    return [(x*pow(a[-1], -1, 5)) % 5 for x in a]


def irreducible(f):
    degree = len(f)-1
    x = remainder([0, 1], f)
    if fpow(x, 5**degree, f) != x: return False
    for p in range(2, degree+1):
        if degree % p == 0 and all(p % j for j in range(2, p)):
            z = fpow(x, 5**(degree//p), f)
            z += [0]*max(0, len(x)-len(z))
            for i, v in enumerate(x): z[i] = (z[i]-v) % 5
            if gcd(f, z) != [1]: return False
    return True


src = c['source_polynomials']
# Exact integer convolution, independent of the modular helper above.
def integer_mul(a, b):
    return [sum(a[i]*b[k-i] for i in range(max(0, k-len(b)+1), min(k, len(a)-1)+1))
            for k in range(len(a)+len(b)-1)]
h3 = integer_mul(integer_mul(src['h'], src['h']), src['h'])
checks['source_matches_canonical_complete_coefficients'] = src == json.loads((BASE.parent/'five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
checks['model_H2_exact'] = H == c['factors']['2']['degree_eleven'] and H == [3,1,2,0,4,4,2,3,1,4,3,1]
checks['model_irreducible'] = irreducible(H)
for r in [2, 4]:
    fac = c['factors'][str(r)]
    ff = [fac['linear'], fac['degree_eleven']] if r == 2 else fac['factors']
    prod = [1]
    for f in ff: prod = pmul(prod, f)
    checks[f'{r}_complete_factors'] = prod == fac['F_mod5']
    checks[f'{r}_all_irreducible'] = all(irreducible(f) for f in ff)
    checks[f'{r}_coprime'] = all(gcd(f, g) == [1] for i, f in enumerate(ff) for g in ff[:i])
    checks[f'{r}_b_coprime'] = gcd(prod, [v % 5 for v in src['b']]) == [1]
records, classes = c['records'], c['classes']
expected = {(s, i) for s in range(125) if s % 5 == 2 for i in range(11)}
checks['coverage_all_275_pairs_exactly_once'] = len(records) == 275 and {(row['s'], row['embedding']) for row in records} == expected
roots = c['factors']['2']['roots']
checks['all_eleven_residue_embeddings'] = len({tuple(x) for x in roots}) == 11 and all(evaluate(H, x, 5) == zero for x in roots)
checks['all_records'] = True
for row in records:
    s, x, y, f = [row[k] for k in ['s', 'x', 'y', 'f']]
    F = [h3[i]+(s*src['jcoef'][i] if i < 12 else 0)-(s*s*src['d'][i] if i < 12 else 0) for i in range(13)]
    actual_f = add(multiply(add(x, scale(one, -4)), y), add(scale(multiply(x, x), -4), add(scale(x, 30), scale(one, -55))))
    okay = (evaluate(F, x) == zero and add(multiply(y, y), y) == evaluate(src['g'], x)
            and add(evaluate(src['a'], x), multiply(evaluate(src['b'], x), y)) == scale(evaluate(src['d'], x), s)
            and actual_f == f and any(v % 5 for v in f) and invariant(f) == row['label']
            and [v % 5 for v in x] == row['residue_x'] == roots[row['embedding']])
    if not okay: checks['all_records'] = False; raise ArithmeticError(('record', row))
checks['all_norms_and_rational_components'] = True
for s in sorted({r['s'] for r in records}):
    rows = [r for r in records if r['s'] == s]
    norm = one
    for row in rows: norm = multiply(norm, row['f'])
    assert norm[1:] == zero[1:] and norm[0] % 5
    assert all(row['norm'] == norm[0] and row['rational_representative']*norm[0] % 125 == 121 for row in rows)
checks['all_partition_members'] = sorted(i for cls in classes for i in cls['members']) == list(range(275))
checks['all_class_representatives'] = all(cls['f'] == records[cls['representative_record']]['f'] and cls['label'] == invariant(cls['f']) and cls['rational_representative'] == records[cls['representative_record']]['rational_representative'] for cls in classes)
checks['all_explicit_representatives'] = all(cls['explicit_U_representative'] == add(one, scale(cls['label'], -5)) and multiply(power(cls['explicit_representative_fifth_root'], 5), cls['explicit_U_representative']) == cls['f'] for cls in classes)
checks['five_seed_frobenius_orbits'] = True
for s in [2, 7, 12, 17, 22]:
    seed = next(r for r in records if r['s'] == s and r['residue_x'] == [0, 1]+[0]*9)['label']
    orbit, z = [], seed
    for _ in range(11):
        orbit.append(z)
        z = power(z, 5, 5)
    assert {tuple(z) for z in orbit} == {tuple(r['label']) for r in records if r['s'] == s}
checks['all_collision_witnesses'] = len(c['collisions']) == 275
assert sorted(w['record'] for w in c['collisions']) == list(range(275))
for witness in c['collisions']:
    row, cls = records[witness['record']], classes[witness['class']]
    assert row['class_index'] == witness['class'] and witness['record'] in cls['members']
    assert multiply(power(witness['U_fifth_root'], 5), cls['f']) == row['f']
    assert pow(witness['Q5_fifth_root'], 5, 125)*cls['rational_representative'] % 125 == row['rational_representative']
    assert row['label'] == cls['label']
checks['all_noncollision_pairs'] = {(v['i'], v['j']) for v in c['noncollisions']} == {(i, j) for i in range(len(classes)) for j in range(i)} and len(c['noncollisions']) == len(classes)*(len(classes)-1)//2
for witness in c['noncollisions']:
    i, j, k = [witness[key] for key in ['i', 'j', 'coordinate']]
    assert (classes[i]['label'][k]-classes[j]['label'][k]) % 5 == witness['difference'] != 0
checks['all_original_checks'] = all(c['checks'].values()) and c['failures'] == []
checks['result_55_classes_five_members_each'] = len(classes) == 55 and all(len(cls['members']) == 5 for cls in classes)
summary = {'records_verified': len(records), 'classes_verified': len(classes),
           'collision_witnesses_verified': len(c['collisions']),
           'noncollision_pairs_verified': len(c['noncollisions']),
           'required_records': 275, 'prior_bound': 600}
out = {'summary': summary, 'checks': checks, 'failures': [k for k, v in checks.items() if not v],
       'exact_list': [{'class': i, 'label': cls['label'], 'rational_representative': cls['rational_representative'],
                       's': records[cls['representative_record']]['s'],
                       'embedding': records[cls['representative_record']]['embedding'],
                       'U_representative': cls['explicit_U_representative'],
                       'members': cls['members']} for i, cls in enumerate(classes)]}
path = BASE/'verification.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print('Verified:', summary)
print('Checks:', len(checks), 'failures:', out['failures'])
print('Full verification:', path.relative_to(BASE.parent.parent))
assert not out['failures']
