"""Exact rational certificate for the single C759b constant-envelope scalar."""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
N = 64
D = 10**12


def pair(interval):
    return [str(x) for x in interval]


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def outward(interval):
    lo, hi = interval
    return F((lo * D).__floor__(), D), F(ceil_fraction(hi * D), D)


logs = {}
log_evidence = {}
for p in (2, 3, 5, 7):
    z = F(p - 1, p + 1)
    terms = [2 * z**(2*k + 1) / (2*k + 1) for k in range(N)]
    s = sum(terms, F(0))
    tail = 2 * z**(2*N + 1) / ((2*N + 1) * (1 - z*z))
    logs[p] = outward((s, s + tail))
    log_evidence[str(p)] = {
        'z': str(z), 'terms': [str(x) for x in terms],
        'partial_sum': str(s), 'tail_upper': str(tail),
        'interval': pair(logs[p]),
    }
logs[4] = tuple(2 * x for x in logs[2])

roots = {}
root_evidence = {}
for n in (2, 3, 4, 5, 7):
    k = isqrt(n * D * D)
    hi = k if k*k == n * D * D else k + 1
    roots[n] = F(k, D), F(hi, D)
    root_evidence[str(n)] = {
        'interval': pair(roots[n]),
        'lower_square_le_n': k*k <= n * D * D,
        'upper_square_ge_n': hi*hi >= n * D * D,
    }

contributions = {}
lo = F(0)
hi = F(0)
checks = {}
for n in (2, 3, 4, 5, 7):
    p = 2 if n == 4 else n
    checks[f'positive_log_and_overlap_{n}'] = 0 < logs[p][0] and logs[n][1] < 2
    lower = logs[p][0] * (2 - logs[n][1]) / roots[n][1]
    upper = logs[p][1] * (2 - logs[n][0]) / roots[n][0]
    contributions[str(n)] = {
        'lambda_prime': p, 'log_n': pair(logs[n]),
        'lambda_n': pair(logs[p]), 'sqrt_n': pair(roots[n]),
        'interval': pair((lower, upper)),
        'decimal_outward': pair(outward((lower, upper))),
    }
    lo += lower
    hi += upper

checks['all_root_square_checks'] = all(
    v['lower_square_le_n'] and v['upper_square_ge_n']
    for v in root_evidence.values()
)
checks['log4_equals_twice_log2'] = logs[4] == tuple(2*x for x in logs[2])
checks['prime_power4_uses_log2'] = contributions['4']['lambda_prime'] == 2
checks['strict_lower_1745_over_1000'] = lo > F(1745, 1000)
checks['strict_upper_1747_over_1000'] = hi < F(1747, 1000)
checks['strict_margin_over_3_over_2_gt_49_over_200'] = lo - F(3, 2) > F(49, 200)
failures = [name for name, passed in checks.items() if not passed]
result = {
    'result': 'PASS' if not failures else 'FAIL',
    'formula': 'sum_(n=2,3,4,5,7) Lambda(n)/sqrt(n)*(2-log(n))',
    'method': 'exact Fraction; log=2 sum z^(2k+1)/(2k+1), geometric tail; integer square brackets',
    'series_terms': N, 'decimal_grid_denominator': D,
    'logs': log_evidence, 'sqrt': root_evidence,
    'contributions': contributions,
    'scalar': {'exact_interval': pair((lo, hi)),
               'decimal_outward': pair(outward((lo, hi))),
               'required_upper_coefficient': '3/2',
               'margin_exact_interval': pair((lo - F(3, 2), hi - F(3, 2))),
               'proved_margin_lower': '49/200'},
    'checks': checks, 'failures': failures,
    'scope': 'single constant-envelope arithmetic scalar; no frequency search, full-Q sign or RH conclusion',
    'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
}
OUT.write_text(json.dumps(result, indent=2) + '\n')
print(f"{result['result']}: scalar in {pair(outward((lo, hi)))}; required upper coefficient 3/2")
print(f"Strict margin >49/200: {checks['strict_margin_over_3_over_2_gt_49_over_200']}; failures: {failures}")
print(f"Certificate: {OUT.relative_to(HERE.parents[2])}")
raise SystemExit(bool(failures))
