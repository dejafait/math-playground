#!/usr/bin/env python3
"""Audit every primitive and panel in L566's exact interval certificate.

The independent exponential enclosure uses 192 bits, 48 Taylor terms,
and reduction to [0,1/2]. No floating-point arithmetic or external package.
Universal coefficient and PSD arguments are audited in the canonical lemma;
this script verifies the complete finite integration evidence only.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from pathlib import Path
import contextlib
import hashlib
import importlib.util
import io
import json

HERE = Path(__file__).parent
SOURCE = HERE / 'leading-block-boundary-certificate.py'
CERT = HERE / 'leading-block-boundary-certificate.json'
OUT = HERE / 'l566-certificate-audit.json'
spec = importlib.util.spec_from_file_location('boundary', SOURCE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
S, R = mod.S, 1 << 192
counts = {}
failures = []


def check(condition, label):
    counts[label] = counts.get(label, 0) + 1
    if not condition:
        failures.append(label)
        raise AssertionError(label)


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


@lru_cache(None)
def ref_exp(x):
    x = F(x)
    if x == 0:
        return R, R
    if x < 0:
        lo, hi = ref_exp(-x)
        return R * R // hi, ceil_fraction(F(R * R, lo))
    shifts = 0
    while x > F(1, 2):
        x /= 2
        shifts += 1
    lo_x, hi_x = (x * R).__floor__(), ceil_fraction(x * R)
    lo_t = hi_t = R
    lo_s = hi_s = R
    for k in range(1, 49):
        lo_t = lo_t * lo_x // (R * k)
        hi_t = ceil_fraction(F(hi_t * hi_x, R * k))
        lo_s += lo_t
        hi_s += hi_t
    # exp(1/2)<2 and x^49<=1: Lagrange remainder <=2/49!.
    hi_s += ceil_fraction(F(2 * R, factorial(49)))
    for _ in range(shifts):
        lo_s = lo_s * lo_s // R
        hi_s = ceil_fraction(F(hi_s * hi_s, R))
    return lo_s, hi_s


def exact_interval(a):
    return F(a[0], S), F(a[1], S)


def enclose(out, lo, hi, label):
    check(F(out[0], S) <= lo <= hi <= F(out[1], S), label)


def wrap(name):
    raw = getattr(mod, name)
    def audited(*args):
        out = raw(*args)
        if name == 'point':
            lo = hi = F(args[0])
        else:
            a, b = exact_interval(args[0])
            if name in ('add', 'sub', 'mul'):
                c, d = exact_interval(args[1])
                if name == 'add':
                    lo, hi = a + c, b + d
                elif name == 'sub':
                    lo, hi = a - d, b - c
                else:
                    products = [a*c, a*d, b*c, b*d]
                    lo, hi = min(products), max(products)
            elif name == 'scale':
                check(args[1] >= 0, 'nonnegative_scale')
                lo, hi = a * args[1], b * args[1]
            else:
                check(args[1] > 0, 'positive_divisor')
                lo, hi = a / args[1], b / args[1]
        enclose(out, lo, hi, name)
        return out
    setattr(mod, name, audited)


for name in ('point', 'add', 'sub', 'mul', 'scale', 'divide'):
    wrap(name)
raw_exp = mod.exp_point


@lru_cache(None)
def checked_exp(x):
    x = F(x)
    out = raw_exp(x)
    if x <= -128:
        # Analytic branch: exp(x)<2^-128, from exp(1)>2.
        enclose(out, F(0), F(1, 1 << 128), 'exp_clipped_tail')
    else:
        lo, hi = ref_exp(x)
        check(out[0] * R <= lo * S and hi * S <= out[1] * R,
              'exp_independent_enclosure')
    return out


mod.exp_point = checked_exp


def main():
    saved = CERT.read_bytes()
    with contextlib.redirect_stdout(io.StringIO()):
        mod.main()
    check(CERT.read_bytes() == saved, 'complete_certificate_replay_identical')
    c = json.loads(saved)
    check(c['status'] == 'PASS' and c['failures'] == [], 'original_status')
    check(len(c['panels']) == 3072, 'all_panels_present')
    totals = [[0, 0] for _ in range(3)]
    for j, panel in enumerate(c['panels']):
        check(panel['index'] == j, 'panel_order_no_omissions')
        for n, pair in enumerate(panel['integral_fixedpoint_intervals']):
            check(0 <= pair[0] <= pair[1], 'ordered_positive_panel')
            for endpoint in range(2):
                totals[n][endpoint] += pair[endpoint]
    check(totals == c['panel_integral_totals_fixedpoint'], 'complete_panel_sums')
    # Independent rational Machin branch and alternating-series check.
    t = F(1, 5)
    t2 = 2*t/(1-t*t)
    t4 = 2*t2/(1-t2*t2)
    check(t4 == F(120, 119), 'machin_double_angle')
    check((t4-F(1,239))/(1+t4/239) == 1, 'machin_subtraction')
    # 0<4 atan(1/5)-atan(1/239)<4/5<pi/2; the lower bound
    # follows from atan(x)>=x-x^3/3 and atan(x)<=x on [0,1].
    check(4*(F(1,5)-F(1,375))-F(1,239)>0, 'machin_branch_lower')
    check(F(4,5)<F(3,2), 'machin_branch_upper')
    def atan_interval(x, n):
        terms = [(-1)**k*x**(2*k+1)/(2*k+1) for k in range(n+1)]
        s = sum(terms[:-1], F(0))
        return sorted([s, s+terms[-1]])
    a, b = atan_interval(F(1,5),16), atan_interval(F(1,239),6)
    pi_bounds = [16*a[0]-4*b[1],16*a[1]-4*b[0]]
    check(pi_bounds == list(map(F,c['pi_bounds'])), 'complete_machin_bounds')
    check(3<pi_bounds[0]<pi_bounds[1]<4, 'pi_required_threshold')
    # Both full moment tails, independent rational reconstruction.
    check(16*F(1,1<<33)<F(1,2), 'theta_successive_ratio')
    theta_bound = 64*2*5**4*F(1,1<<75)
    check(theta_bound == F(80000,1<<75), 'entire_theta_tail_constant')
    L, a = F(6), F(5,4)
    rs = [1/(2*a*L)]
    rs.append(L/(2*a)+rs[0]/(2*a))
    rs.append(L**3/(2*a)+3*rs[1]/(2*a))
    exp_upper = F(checked_exp(F(-45))[1],S)
    for n in range(3):
        theta = 2*theta_bound*L**(2*n+1)/(2*n+1)
        spatial = 20000*rs[n]*exp_upper
        tail = c['omitted_tails'][n]
        check(F(tail['theta_rational_upper']) == theta, 'full_theta_moment_tail')
        check(F(tail['spatial_rational_upper']) == spatial, 'full_spatial_moment_tail')
        lower, upper = map(F,c['moment_bounds'][n])
        check(lower == F(2*totals[n][0],S), 'moment_lower_sum')
        check(upper >= F(2*totals[n][1],S)+theta+spatial,
              'moment_upper_covers_both_tails')
        denominator = 2**(2*n)*factorial(2*n)
        bl, bu = map(F,c['coefficient_bounds'][n])
        check(bl<=lower/denominator<=upper/denominator<=bu,
              'moment_coefficient_normalization')
        dl, du = map(F,c['coarse_b_bounds'][['b0','b2','b4'][n]])
        check(0<dl<=bl<=bu<=du, 'coarse_outward_positive')
    (b0lo,b0hi),(b2lo,b2hi),(b4lo,b4hi) = [list(map(F,c['coarse_b_bounds'][key]))
                                                        for key in ('b0','b2','b4')]
    upper = b2hi**2+16*b2hi*b4hi+96*b4hi**2-4*b0lo*b4lo
    lower = b2lo**2+16*b2lo*b4lo+96*b4lo**2-4*b0hi*b4hi
    check(F(c['decisive_test']['certified_upper']) == upper < 0,
          'strict_negative_exact_upper')
    check(F(c['decisive_test']['certified_lower']) == lower < upper,
          'exact_lower')
    check(b0lo>=F(12,25) and b2hi<=F(3,1000) and
          b4lo>=F(7,10**6) and b4hi<=F(8,10**6), 'short_bound_inputs')
    short = F(3,1000)**2+16*F(3,1000)*F(8,10**6)+96*F(8,10**6)**2-4*F(12,25)*F(7,10**6)
    check(short == F('-0.000004049856') < 0, 'short_exact_upper')
    report = {'status':'PASS', 'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'certificate_sha256':hashlib.sha256(saved).hexdigest(),
              'all_panels_checked':3072, 'primitive_counts':counts,
              'independent_exp_precision_bits':192,'independent_exp_order':48,
              'actual_q_upper':str(upper),'required_for_psd':'Q>=0',
              'short_q_upper':str(short),'failures':failures,
              'scope':'Full finite integration audit; universal algebra and PSD proof in L566.'}
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print('status:',report['status'],'; panels:',report['all_panels_checked'])
    print('exponential arguments independently enclosed:',counts['exp_independent_enclosure'])
    print('actual Q upper:',upper,'; required: Q>=0')
    print('failures:',failures,'; full audit:',OUT)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        OUT.write_text(json.dumps({'status':'FAIL','failures':failures,
                                   'error':str(error),'primitive_counts':counts},indent=2)+'\n')
        print('status: FAIL; full audit:',OUT)
        raise
