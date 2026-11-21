"""Independent exact-data audit of the complete C759b scalar certificate."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('odd-carrier-scalar-798.json')
CODE = HERE.with_name('odd-carrier-scalar-798.py')
OUT = HERE.with_suffix('.json')
c = json.loads(SOURCE.read_text())
checks = {}
details = {}


def check(name, predicate):
    checks[name] = bool(predicate)


def interval(value):
    return tuple(F(v) for v in value)


def enclose(lo, hi, den):
    low_num = lo.numerator * den // lo.denominator
    high_num = (hi.numerator * den + hi.denominator - 1) // hi.denominator
    return F(low_num, den), F(high_num, den)


den = 10**12
check('parameters', c['series_terms'] == 64 and c['decimal_grid_denominator'] == den)
check('source_hash', c['script_sha256'] == sha256(CODE.read_bytes()).hexdigest())
check('log_list', set(c['logs']) == {'2', '3', '5', '7'})
check('root_list', set(c['sqrt']) == {'2', '3', '4', '5', '7'})
check('contribution_list', set(c['contributions']) == {'2', '3', '4', '5', '7'})
logs = {}
expected_log_grid = {
    2: (693147180559, 693147180560),
    3: (1098612288668, 1098612288669),
    5: (1609437912434, 1609437912435),
    7: (1945910149055, 1945910149056),
}
for p in (2, 3, 5, 7):
    record = c['logs'][str(p)]
    z = F(p - 1, p + 1)
    check(f'log_{p}_z', F(record['z']) == z and 0 < z < 1)
    # Reconstruct all terms successively, rather than trusting the partial sum.
    power = z
    terms = []
    for j in range(64):
        terms.append(2 * power / (2*j + 1))
        power *= z*z
    check(f'log_{p}_all_64_terms', tuple(map(F, record['terms'])) == tuple(terms))
    total = sum(terms, F(0))
    tail = 2 * power / (129 * (1-z*z))
    check(f'log_{p}_sum', F(record['partial_sum']) == total)
    check(f'log_{p}_tail', F(record['tail_upper']) == tail and tail > 0)
    lo, hi = interval(record['interval'])
    check(f'log_{p}_outward', (lo, hi) == enclose(total, total+tail, den))
    check(f'log_{p}_containment', lo <= total < total+tail <= hi)
    check(f'log_{p}_displayed_grid', (lo, hi) == tuple(F(k, den) for k in expected_log_grid[p]))
    logs[p] = lo, hi
logs[4] = tuple(2*x for x in logs[2])
check('all_overlaps_and_upper_cutoff', 0 < logs[2][0] and logs[7][1] < 2 < 3*logs[2][0])

roots = {}
expected_root_grid = {
    2: (1414213562373, 1414213562374),
    3: (1732050807568, 1732050807569),
    4: (2*den, 2*den),
    5: (2236067977499, 2236067977500),
    7: (2645751311064, 2645751311065),
}
for n in (2, 3, 4, 5, 7):
    record = c['sqrt'][str(n)]
    lo, hi = interval(record['interval'])
    check(f'root_{n}_direct_squares', 0 < lo <= hi and lo*lo <= n <= hi*hi)
    check(f'root_{n}_displayed_grid', (lo, hi) == tuple(F(k, den) for k in expected_root_grid[n]))
    check(f'root_{n}_stored_flags', record['lower_square_le_n'] is True and record['upper_square_ge_n'] is True)
    roots[n] = lo, hi

lower = F(0)
upper = F(0)
expected_source_checks = {}
for n in (2, 3, 4, 5, 7):
    p = 2 if n == 4 else n
    record = c['contributions'][str(n)]
    check(f'contribution_{n}_inputs', record['lambda_prime'] == p
          and interval(record['lambda_n']) == logs[p]
          and interval(record['log_n']) == logs[n]
          and interval(record['sqrt_n']) == roots[n])
    positive = 0 < logs[p][0] and logs[n][1] < 2
    expected_source_checks[f'positive_log_and_overlap_{n}'] = positive
    check(f'contribution_{n}_positive', positive)
    a = logs[p][0] * (2-logs[n][1]) / roots[n][1]
    b = logs[p][1] * (2-logs[n][0]) / roots[n][0]
    check(f'contribution_{n}_exact_interval', interval(record['interval']) == (a, b) and a < b)
    check(f'contribution_{n}_rounding', interval(record['decimal_outward']) == enclose(a, b, den))
    details[str(n)] = [str(x) for x in enclose(a, b, den)]
    lower += a
    upper += b

s = c['scalar']
check('total_exact_interval', interval(s['exact_interval']) == (lower, upper))
rounded = enclose(lower, upper, den)
check('total_outward_rounding', interval(s['decimal_outward']) == rounded)
check('displayed_final_bounds', rounded == (F(1745850839151, den), F(1745850839159, den)))
check('exact_margin_interval', interval(s['margin_exact_interval']) == (lower-F(3, 2), upper-F(3, 2)))
check('required_and_proved_thresholds', F(s['required_upper_coefficient']) == F(3, 2)
      and F(s['proved_margin_lower']) == F(49, 200) and lower-F(3, 2) > F(49, 200))
expected_source_checks.update({
    'all_root_square_checks': all(a*a <= n <= b*b for n, (a, b) in roots.items()),
    'log4_equals_twice_log2': logs[4] == tuple(2*x for x in logs[2]),
    'prime_power4_uses_log2': c['contributions']['4']['lambda_prime'] == 2,
    'strict_lower_1745_over_1000': lower > F(1745, 1000),
    'strict_upper_1747_over_1000': upper < F(1747, 1000),
    'strict_margin_over_3_over_2_gt_49_over_200': lower-F(3, 2) > F(49, 200),
})
check('all_original_flags_recomputed', c['checks'] == expected_source_checks and all(expected_source_checks.values()))
check('original_status_and_failures', c['result'] == 'PASS' and c['failures'] == [])
check('projection_sum_of_squares', sum(j*j for j in range(1, 121)) == 583220)
failures = [k for k, passed in checks.items() if not passed]
report = {
    'result': 'PASS' if not failures else 'FAIL',
    'source_certificate': str(SOURCE.relative_to(HERE.parents[2])),
    'source_certificate_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
    'audit_script_sha256': sha256(HERE.read_bytes()).hexdigest(),
    'coverage': {'log_terms_verified': 256, 'log_tails_verified': 4,
                 'root_brackets_verified': 5, 'contributions_verified': 5},
    'checks': checks, 'failures': failures,
    'contributions_outward': details,
    'scalar_exact_interval': [str(lower), str(upper)],
    'scalar_outward': [str(x) for x in rounded],
    'required_upper': '3/2', 'strict_margin_lower': '49/200',
    'scope': 'Complete exact scalar evidence; analytic audit is recorded in C759b Section6.',
    'trust': 'Python integer/Fraction and JSON/file handling; not formal verification.',
}
OUT.write_text(json.dumps(report, indent=2) + '\n')
print(f"{report['result']}: {len(checks)} checks; all 256 log terms, 4 tails, 5 roots and 5 contributions checked")
print(f"R in ({rounded[0]}, {rounded[1]}); required upper 3/2; strict margin >49/200")
print(f"Failures: {failures}; certificate: {OUT.relative_to(HERE.parents[2])}")
raise SystemExit(bool(failures))
