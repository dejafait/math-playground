"""Independent L078--L081 evidence audit; no construction-module imports.

Arithmetic uses polynomials in rho with H coefficients, multiplying H by
ordinary convolution and reducing pi first. Exact identities use Python
integers (numpy object); modular arithmetic uses bounded int64 values.
All existing input artifacts are read-only. Full audit report is separate.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import traceback
import numpy as np

HERE = Path(__file__).resolve().parent
REPORT = HERE / 'complete-independent-audit.json'
checks, results, hashes = {}, {}, {}
current = 'initialization'


def load(name):
    path = HERE / name
    data = path.read_bytes()
    hashes[name] = hashlib.sha256(data).hexdigest()
    return json.loads(data)


def check(name, value):
    checks[name] = bool(value)
    if not value:
        raise AssertionError(name)


def eq(a, b):
    return bool(np.array_equal(a, b))


def conv(a, b, modulus):
    c = np.convolve(a, b)
    out = c[:11].copy()
    out[:10] += 2*c[11:]
    return out % modulus if modulus else out


def shift(a, k):
    out = np.zeros(11, dtype=a.dtype)
    for i in range(11):
        out[(i+k) % 11] += int(2**((i+k)//11))*a[i]
    return out


def mul(a, b, modulus=8):
    # Intermediate modular values stay below 10^9, far below int64 limit.
    dtype = np.int64 if modulus else object
    a, b = np.asarray(a, dtype=dtype), np.asarray(b, dtype=dtype)
    if modulus:
        a, b = a % modulus, b % modulus
    c = np.zeros((5, 11), dtype=dtype)
    for j in range(3):
        for k in range(3):
            c[j+k] += conv(a[j], b[k], modulus)
    # rho^3 = pi + 3*pi^4*rho^2 - 2*pi^8*rho
    for k in (4, 3):
        c[k-3] += shift(c[k], 1)
        c[k-2] -= 2*shift(c[k], 8)
        c[k-1] += 3*shift(c[k], 4)
    return c[:3] % modulus if modulus else c[:3]


def raw(vec):
    assert len(vec) == 33 and all(isinstance(v, int) for v in vec)
    return np.array(vec, dtype=object).reshape(11, 3).T.copy()


def power(a, n, modulus=8):
    out = ONE.copy()
    for _ in range(n):
        out = mul(out, a, modulus)
    return out


def val(a, cap=99):
    vals = [cap]
    for j in range(3):
        for i in range(11):
            c = abs(int(a[j, i]))
            if c:
                vals.append(33*((c & -c).bit_length()-1)+3*i+j)
    return min(vals)


def center(mask):
    out = np.zeros((3, 11), dtype=np.int64)
    for i in range(mask.bit_length()):
        if mask >> i & 1:
            out[0, i % 11] += 2**(i//11)
    return out


ONE = np.zeros((3, 11), dtype=np.int64)
ONE[0, 0] = 1
PI, RHO = np.zeros_like(ONE), np.zeros_like(ONE)
PI[0, 1], RHO[1, 0] = 1, 1
DIGITS = list(range(1, 66, 2)) + [66]
RP = [power(RHO, n) for n in range(100)]
GEN = [((ONE+r) % 8) for n, r in enumerate(RP) if n in DIGITS]
representatives = {}


def representative(bits):
    assert isinstance(bits, int) and 0 <= bits < 2**34
    if bits not in representatives:
        out = ONE.copy()
        for i, g in enumerate(GEN):
            if bits >> i & 1:
                out = mul(out, g)
        representatives[bits] = out
    return representatives[bits]


def normal(unit, nf, label):
    assert nf['bits'] == label
    assert nf['digits'] == [d for i, d in enumerate(DIGITS) if label >> i & 1]
    rep = representative(label)
    assert eq(rep, raw(nf['representative']))
    root, residual = raw(nf['square_root_factor']), raw(nf['residual'])
    bound = val((residual-ONE) % 8)
    assert val(unit) == val(root) == 0 and bound > 66
    assert bound == nf['residual_minus_one_valuation_lower_bound']
    assert eq(unit, mul(mul(rep, mul(root, root)), residual))
    assert nf['reconstruction_mod_8'] is True
    return bound


def rank(labels):
    pivots = {}
    for x in labels:
        while x:
            i = x.bit_length()-1
            if i not in pivots:
                pivots[i] = x
                break
            x ^= pivots[i]
    return len(pivots)


def histogram_matches(hist, stored):
    return dict(hist) == {int(k): v for k, v in stored.items()}


def run():
    global current
    ar = load('arithmetic-certificate.json')
    af = load('affine-certificate.json')
    rc = load('reciprocal-certificate.json')
    pc = load('parameter-certificate.json')
    current = 'exact models and arithmetic'
    s = 4*ONE - 3*mul(power(PI, 7, None), RHO, None) + mul(power(PI, 3, None), power(RHO, 2, None), None)
    th = 28*ONE-26*s+6*mul(s, s, None)
    check('exact_pi_relation', eq(power(PI, 11, None), 2*ONE))
    check('exact_inverse_generator_maps', eq(mul(RHO, s, None), power(PI, 4, None)))
    check('exact_s_polynomial', eq(power(s, 3, None)-4*power(s, 2, None)+6*s-2*ONE, 0*ONE))
    check('exact_theta_polynomial', eq(power(th, 3, None)-4*power(th, 2, None)-160*th-1264*ONE, 0*ONE))
    check('inverse_theta_map', eq(-92*ONE-62*th+3*mul(th, th, None), 484*(s-ONE)))
    expected_th = -16*ONE+12*mul(power(PI, 7, None), RHO, None)-2*mul(power(PI, 3, None), power(RHO, 2, None), None)
    check('fixed_theta_all_sources', all(eq(th, raw(v)) for v in [ar['exact_coordinates']['theta'], af['exact_normalizers']['theta'], rc['inputs']['theta_exact'], pc['inputs']['theta_exact']]) and eq(th, expected_th) and eq(s, raw(ar['exact_coordinates']['s'])))
    A, B = raw(af['exact_normalizers']['A']), raw(af['exact_normalizers']['B'])
    check('exact_normalizers', eq(mul(power(RHO, 44, None), A, None), 4*ONE) and eq(mul(power(RHO, 44, None), B, None), -th))
    check('normalizer_valuations', [val(A), val(B), val(th)] == [22, 0, 44])
    check('rho_valuations', [val(r) for r in RP] == list(range(100)))
    check('square_basis_digits', ar['class_digits'] == DIGITS and ar['unit_class_dimension'] == 34 and ar['field_class_dimension'] == 35)
    for n in range(1, 67):
        q = ONE+RP[n] if n in DIGITS else mul(ONE+RP[n//2], ONE+RP[n//2])
        assert eq(mul(raw(ar['eliminators'][str(n)]), q), ONE)
        assert val((q-ONE) % 8) == n
    check('every_digit_eliminator_inverse_and_leading_term', True)
    assert len(ar['generator_records']) == 34 and len(ar['square_records']) == 33
    for i, rec in enumerate(ar['generator_records']):
        assert rec['digit'] == DIGITS[i] and eq(raw(rec['element']), GEN[i])
        normal(GEN[i], rec['normal_form'], 1 << i)
    for i, rec in enumerate(ar['square_records'], 1):
        root = (ONE+RP[i]) % 8
        assert rec['root_digit'] == i and eq(raw(rec['root']), root)
        square = mul(root, root)
        assert eq(raw(rec['square']), square)
        normal(square, rec['normal_form'], 0)
    fixed = {'one': ONE, 'u': (ONE-s) % 8, 'h': (5*ONE-th) % 8}
    fixed['uh'] = mul(fixed['u'], fixed['h'])
    labels = {'one': 0, 'u': 1 << 5, 'h': (1 << 27)+(1 << 33), 'uh': (1 << 5)+(1 << 27)+(1 << 33)}
    for key, unit in fixed.items():
        assert eq(unit, raw(ar['targets'][key]['element']))
        normal(unit, ar['targets'][key]['normal_form'], labels[key])
    check('all_arithmetic_examples_and_fixed_labels', True)
    results['arithmetic'] = {'generators': 34, 'square_examples': 33, 'fixed_elements': 4, 'eliminators': 66}
    print('Independent exact model and 137 arithmetic witness checks passed.', flush=True)

    current = 'affine records'
    records = load('affine-disks.json')
    seen, hist, actual_labels = set(), Counter(), {}
    increments = [mul(A, power(PI, i)) for i in range(15)]
    min_bound = 99
    for rec in records:
        mask, label = rec['x_pi_binary_digits'], rec['label']
        assert mask not in seen and 0 <= mask < 32768 and rec['depth'] == 15
        seen.add(mask)
        expected = B % 8
        for i in range(15):
            if mask >> i & 1:
                expected = (expected+increments[i]) % 8
        unit = raw(rec['unit_mod_8'])
        assert eq(unit, expected)
        min_bound = min(min_bound, normal(unit, rec['normal_form'], label))
        actual_labels[mask] = label
        hist[label] += 1
    check('all_affine_records_and_coverage', seen == set(range(32768)))
    check('all_affine_collisions', histogram_matches(hist, af['collision_histogram']))
    check('every_affine_representative', set(map(int, af['representative_masks'])) == set(hist) and all(actual_labels[m] == int(l) for l, m in af['representative_masks'].items()))
    witnesses = af['independent_label_witnesses']
    check('affine_cardinality_and_rank', len(hist) == 2048 and rank(hist) == 11 and len(witnesses) == rank([r['original_label'] for r in witnesses]) == 11 and all(actual_labels[r['x_pi_binary_digits']] == r['original_label'] for r in witnesses))
    results['affine'] = {'records': len(seen), 'required': 32768, 'classes': len(hist), 'required_classes': 2048, 'rank': 11, 'minimum_residual': min_bound}
    affine_labels = set(hist)
    del records
    print('All 32768 affine records verified; 2048 classes, rank 11.', flush=True)

    current = 'reciprocal records'
    seen, hist, decisions = set(), Counter(), Counter()
    possible = [mul(center(m), center(m)) for m in range(0, 16, 2)]
    for rec in rc['records']:
        mask = rec['z_pi_binary_digits']
        assert mask not in seen and mask in range(0, 256, 2) and rec['depth_H'] == 8
        seen.add(mask)
        z0 = center(mask)
        assert eq(z0, raw(rec['z_center_mod_8']))
        hits = sum(val((sq-z0) % 8) >= 24 for sq in possible)
        decisions[rec['decision']] += 1
        if rec['decision'] == 'REJECT':
            assert hits == 0 and rec['obstructing_odd_digits'] == [i for i in (1, 3, 5, 7) if mask >> i & 1]
            continue
        assert rec['decision'] == 'REALIZED' and hits == 1
        r = center(rec['square_root_z_pi_binary_digits'])
        assert np.any(r) and eq(r, raw(rec['square_root_z_mod_8']))
        z = mul(r, r)
        assert eq(z, raw(rec['realized_z_mod_8'])) and val((z-z0) % 8) >= 24
        R = (ONE-4*z-160*mul(z, z)-1264*power(z, 3)) % 8
        assert eq(R, raw(rec['R_mod_8']))
        assert val((R-ONE) % 8) == rec['R_minus_one_J_valuation_lower_bound'] >= 69
        unit = (ONE-mul(th, z)) % 8
        assert eq(unit, raw(rec['kummer_unit_mod_8']))
        label = rec['label']
        normal(unit, rec['normal_form'], label)
        assert actual_labels[rec['affine_representative_mask']] == label
        hist[label] += 1
    check('all_reciprocal_records_coverage_and_collisions', seen == set(range(0, 256, 2)) and decisions == {'REALIZED': 8, 'REJECT': 120} and histogram_matches(hist, rc['collision_histogram']))
    check('reciprocal_labels_and_infinity', hist == Counter({0: 2, 1073741824: 2, 4294967296: 2, 5368709120: 2}) and rc['exceptional']['infinity']['label'] == 0 and actual_labels[rc['exceptional']['infinity']['affine_representative_mask']] == 0)
    results['reciprocal'] = {'records': 128, 'required': 128, 'realized': 8, 'rejected': 120, 'classes': 4}
    print('All 128 reciprocal decisions verified; 8 realized, 120 rejected.', flush=True)

    current = 'parameter records'
    records = load('parameter-disks.json')
    seen, hist, annuli = set(), Counter(), Counter()
    min_bound = 99
    for rec in records:
        mask = rec['t_pi_binary_digits']
        assert mask not in seen and mask in range(0, 32768, 2) and rec['depth_H'] == 15 and rec['decision'] == 'REALIZED'
        seen.add(mask)
        k = (mask & -mask).bit_length()-1 if mask else 15
        t = center(mask if mask else 1 << 15)
        assert list(t[0]) == rec['realization_t_mod_64'] and k == rec['realization_t_valuation_H']
        v = np.zeros_like(ONE)
        v[0] = rec['v_mod_64']
        assert v[0, 0] % 2 == 1
        t2, t3, t4, t6 = [power(t, i, 64) for i in (2, 3, 4, 6)]
        b, c = (10*t4-t3) % 64, (20*t6) % 64
        vv = mul(v, v, 64)
        f = (v-ONE+mul(t2, v, 64)+mul(b, vv, 64)+mul(c, mul(vv, v, 64), 64)) % 64
        df = (ONE+t2+2*mul(b, v, 64)+3*mul(c, vv, 64)) % 64
        assert not np.any(f) and list(f[0]) == rec['F_residual_mod_64']
        assert list(df[0]) == rec['derivative_mod_64'] and df[0, 0] % 2 == 1
        m = min(0, 6*k-22)
        assert m == rec['q_valuation_J'] == rec['normalizing_square_rho_exponent'] and m % 2 == 0
        # Compute 4*q*rho^(-m) modulo 32; then divide coefficients by 4.
        # Exact divisibility plus precision 165-66=99 certifies the result.
        numerator = (4*v-mul(th, mul(t2, vv, 32), 32)) % 32
        numerator = mul(numerator, power(RHO, -m, 32), 32)
        assert np.all(numerator % 4 == 0)
        unit = numerator//4
        assert eq(unit, raw(rec['normalized_unit_mod_8']))
        label = rec['label']
        min_bound = min(min_bound, normal(unit, rec['normal_form'], label))
        assert actual_labels[rec['affine_representative_mask']] == label
        if mask == 0:
            assert label == 0
        hist[label] += 1
        annuli[k] += 1
    check('all_parameter_records_and_coverage', seen == set(range(0, 32768, 2)))
    check('all_parameter_collisions_and_affine_equality', histogram_matches(hist, pc['collision_histogram']) and set(hist) == affine_labels)
    check('all_parameter_annuli', histogram_matches(annuli, pc['parameter_valuation_histogram']) and sum(annuli[k] for k in range(1, 12)) == 16376)
    bounds = []
    for k in range(1, 15):
        beta, d = min(26+k, 30), min(26+k, 30, 15+2*k)
        m = min(0, 6*k-22)
        assert d > 11 and min(beta, 2*k+d+11) == beta
        bounds.append({'k': k, 't_square_difference_H': beta, 'root_difference_H': d, 'q_J_valuation': m, 'relative_difference_J': min(3*d, 3*beta-22)-m})
    check('all_parameter_strict_bounds', bounds == pc['constancy_bounds'] and min(r['relative_difference_J'] for r in bounds) == 67 and pc['zero_disk_relative_error_J'] == 68)
    results['parameter'] = {'records': len(seen), 'required': 16384, 'middle_annuli': 16376, 'classes': len(hist), 'minimum_residual': min_bound, 'bounds': bounds}
    results['precision'] = {'strict_threshold': 66, 'arithmetic': 99, 'affine_disk': 67, 'reciprocal_disk': 68, 'parameter_disk_minimum': 67, 'parameter_root_error_after_division': 132, 'independent_mod32_then_divide4': 99}
    check('honest_chart_scope', pc['coverage']['literal_Bruin_Stoll_X_disk_partition'] is False and rc['coverage']['full_two_chart_certificate'] is False)
    print('All 16384 parameter records verified; 16376 middle-annulus disks; same 2048 labels.', flush=True)


if __name__ == '__main__':
    failures = []
    try:
        run()
    except Exception as error:
        failures.append({'stage': current, 'error': repr(error), 'traceback': traceback.format_exc()})
    report = {'scope': 'independent full load-bearing evidence verification plus proof audit in L078--L081; no constructor or verifier imports', 'checks': checks, 'failures': failures, 'results': results, 'input_sha256': hashes}
    REPORT.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {len(failures)}')
    print('Precision actual/strict threshold: 99/>66; disk minimum 67/>66')
    print(f'Certificate: {REPORT.relative_to(Path.cwd())}')
    if failures:
        print(failures[0]['stage'], failures[0]['error'])
    raise SystemExit(bool(failures))
