#!/usr/bin/env python3
"""Independent C034e algebra replay; the analytic audit is in C034e.

Differentiate sparse rational polynomials in v twice (not in t=v^2),
derive the four cleared factors by exact division, and translate the
bivariate polynomial by Horner composition (not binomial coefficients).
Only Python's standard library is used.
"""
import hashlib
import json
import re
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path


def clean(p):
    return {k: F(v) for k, v in p.items() if v}


def add(p, q):
    r = p.copy()
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
    return clean(r)


def scale(p, a):
    return clean({k: v*a for k, v in p.items()})


def mul(p, q):
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i+j] = r.get(i+j, 0) + a*b
    return clean(r)


def power(p, n):
    r = {0: F(1)}
    for _ in range(n):
        r = mul(r, p)
    return r


def derivative(p):
    return clean({k-1: k*v for k, v in p.items() if k})


def rational_derivative(n, d):
    return add(mul(derivative(n), d), scale(mul(n, derivative(d)), -1)), mul(d, d)


def divide(n, d):
    q, r = {}, clean(n)
    m = max(d)
    while r and max(r) >= m:
        k = max(r)-m
        c = r[max(r)]/d[m]
        q[k] = q.get(k, 0)+c
        r = add(r, scale({i+k: a for i, a in d.items()}, -c))
    return clean(q), r


def arr(p):
    return [int(p.get(i, 0)) if F(p.get(i, 0)).denominator == 1
            else str(p[i]) for i in range(max(p, default=0)+1)]


def even_to_t(p):
    if any(i % 2 for i in p):
        raise ValueError('Unexpected odd v power')
    return {i//2: a for i, a in p.items()}


def translate(p):
    r = {}
    for i in range(max(p, default=0), -1, -1):
        r = add(mul(r, {0: F(1), 1: F(1)}), {0: p.get(i, F(0))})
    return r


root = Path(__file__).resolve().parents[2]
original_script = root/'scripts/smoothed-law/laplace_complex_kernel_1851.py'
original_path = original_script.with_suffix('.json')
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
replay = subprocess.run([sys.executable, str(original_script)], cwd=root,
                        capture_output=True, text=True, check=False)
checks = {
    'original_replay_exit_zero': replay.returncode == 0,
    'original_certificate_unchanged': original_path.read_bytes() == original_bytes,
    'original_twenty_checks': len(original['checks']) == 20 and all(original['checks'].values()),
}

# The independent variable below is v, not t.
H = mul(power({2: 1}, 2), mul(power({2: 1, 0: 1}, 4), power({2: 1, 0: 2}, 4)))
factors, identity_remainders, derivative_differences = {}, {}, {}
cleared = {}
for j in (1, 2):
    n = {0: F(4*j*j), 2: F(12*j)}
    d = mul({2: 1}, power({2: 1, 0: j}, 2))
    n1, d1 = rational_derivative(n, d)
    n2, d2 = rational_derivative(n1, d1)
    claimed_n2 = {6: F(240*j), 4: F(120*j*j), 2: F(96*j**3), 0: F(24*j**4)}
    claimed_d2 = mul({4: 1}, power({2: 1, 0: j}, 4))
    delta = add(mul(n2, claimed_d2), scale(mul(claimed_n2, d2), -1))
    derivative_differences[str(j)] = arr(delta)
    checks[f'ordinary_v_second_derivative_{j}'] = not delta
    qh, rem_q = divide(mul(n, H), d)
    q2h, rem_q2 = divide(mul(n2, H), d2)
    identity_remainders[f'Q{j}_H'] = arr(rem_q)
    identity_remainders[f'Q{j}_second_H'] = arr(rem_q2)
    checks[f'exact_H_clearing_{j}'] = not rem_q and not rem_q2
    a, b = even_to_t(scale(qh, F(1, 4*j))), even_to_t(scale(q2h, F(1, 24*j)))
    factors[f'a{j}'], factors[f'b{j}'] = arr(a), arr(b)
    checks[f'factor_agreement_{j}'] = all(factors[k] == original['factors'][k]
                                       for k in (f'a{j}', f'b{j}'))
    cleared[j] = (even_to_t(qh), even_to_t(q2h))

# Form -K H(t)H(u) directly from the cleared Q's and ordinary derivatives.
raw = {}
for left, right, coefficient in (
    (cleared[2][0], cleared[1][1], F(1, 192)),
    (cleared[1][1], cleared[2][0], F(1, 192)),
    (cleared[1][0], cleared[2][1], F(-1, 192)),
    (cleared[2][1], cleared[1][0], F(-1, 192)),
):
    for i, a in left.items():
        for j, b in right.items():
            raw[i, j] = raw.get((i, j), 0)+coefficient*a*b
raw = {k: v for k, v in raw.items() if v}
checks['raw_integer_degree'] = all(a.denominator == 1 and 0 <= i <= 8 and 0 <= j <= 8
                                   for (i, j), a in raw.items())
raw_matrix = [[int(raw.get((i, j), 0)) for j in range(9)] for i in range(9)]
checks['entire_raw_matrix_matches'] = raw_matrix == original['raw_coefficients']
after_t = {}
for j in range(9):
    for i, a in translate({i: raw.get((i, j), F(0)) for i in range(9)}).items():
        after_t[i, j] = a
shifted = [[0]*9 for _ in range(9)]
for i in range(9):
    for j, a in translate({j: after_t.get((i, j), F(0)) for j in range(9)}).items():
        if a.denominator != 1:
            raise ValueError('Nonintegral shifted coefficient')
        shifted[i][j] = int(a)
lemma = (root/'lemmas/C034e-complex-strip-rational-kernel-sign.md').read_text()
printed = [[int(a) for a in line.split()] for line in
           re.search(r'```text\n(.*?)\n```', lemma, re.S).group(1).splitlines()]
checks['all_81_certificate_coefficients'] = shifted == original['shifted_coefficients']
checks['all_81_printed_coefficients'] = shifted == printed
negative = [[i, j, a] for i, row in enumerate(shifted) for j, a in enumerate(row) if a < 0]
checks['exceptional_block_exact'] = negative == [[7, 7, -100]] and shifted[8][6] == shifted[6][8] == 105
remainder = [row[:] for row in shifted]
remainder[7][7] += 100
remainder[8][6] -= 105
remainder[6][8] -= 105
checks['remainder_nonnegative_positive_constant'] = all(a >= 0 for row in remainder for a in row) and remainder[0][0] == 508032

a, theta, scale_min, v = F(671, 4), F(52, 671), F(671, 683), F(31, 20)
cos_lower = 1-v*v/2+v**4/24-v**6/720
scalars = {
    'Re_T_min': a, 'tan_theta_max': theta,
    'shift_scale_min': scale_min, 'shift_scale_surplus': scale_min-F(4, 5),
    'whole_angle_upper': 20*theta, 'whole_angle_threshold_gap': v-20*theta,
    'cosine_lower': cos_lower, 'exceptional_angle_upper': 6*theta,
    'exceptional_angle_threshold_gap': F(1, 2)-6*theta,
    'exceptional_cosine_bound': 1-(6*theta)**2/2,
    'block_margin': 2*105*F(7, 8)-100,
    'kernel_margin': 96*(2*105*F(7, 8)-100),
}
checks['exact_scalar_margins'] = all(scalars[k] > 0 for k in
    ('shift_scale_surplus', 'whole_angle_threshold_gap', 'cosine_lower', 'exceptional_angle_threshold_gap'))
checks['cosine_lower_matches'] = cos_lower == F(921148319, 46080000000)
checks['cosine_derivative_condition'] = v*v < 6 and v < 2
checks['exceptional_cosine_strict'] = scalars['exceptional_cosine_bound'] > F(7, 8)
checks['margin_8040'] = scalars['block_margin'] == F(335, 4) and scalars['kernel_margin'] == 8040

certificate = {
    'scope': 'Independent finite algebra/scalar audit of C034e only; full analytic audit in canonical lemma.',
    'original_sha256': hashlib.sha256(original_bytes).hexdigest(),
    'original_replay': {'exit_code': replay.returncode, 'stdout': replay.stdout, 'stderr': replay.stderr},
    'ordinary_second_derivative_differences': derivative_differences,
    'division_remainders': identity_remainders, 'independent_factors': factors,
    'independent_raw_coefficients': raw_matrix, 'independent_shifted_coefficients': shifted,
    'negative_coefficients': negative, 'remainder_coefficients': remainder,
    'exact_scalars': {k: str(a) for k, a in scalars.items()},
    'checks': checks, 'failures': [k for k, ok in checks.items() if not ok],
    'actual_bound': 'With the audited analytic argument: Re K < -8040 |T|^7 |U|^7 / (|H(z^2)| |H(w^2)|) < 0.',
    'required_bound': 'Re K < 0 on the entire independent closed product strip Re z,Re w>=13; |Im z|,|Im w|<=1/2.',
    'limitations': 'No contour deformation, R estimate, C034c(20), source-wide validation or RH conclusion.',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Original replay: {replay.returncode}; unchanged: {checks["original_certificate_unchanged"]}')
print(f'Independent checks: {sum(checks.values())}/{len(checks)}; failures: {certificate["failures"]}')
print(f'Actual: {certificate["actual_bound"]}\nRequired: {certificate["required_bound"]}')
print(f'Certificate: {out.relative_to(root)}')
if certificate['failures']:
    raise SystemExit(1)
