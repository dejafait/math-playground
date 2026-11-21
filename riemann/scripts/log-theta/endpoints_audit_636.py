#!/usr/bin/env python3
"""Complete replay and independent rational audit of L826's origin data.

The existing lattice containment proof is reused at higher precision.
Derivative polynomials come from a generating series; Q3 comes directly
from the signed derivative determinant. Original artifacts are preserved.
"""
import contextlib
import hashlib
import io
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

import confluent_compact_audit_614 as ar
import endpoints_634 as source

HERE = Path(__file__).resolve().parent
OUT = HERE / 'endpoints_audit_636.json'
REPLAY = HERE / 'endpoints_replay_636.json'


def add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, F(0)) + v
    return {k: v for k, v in r.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(p, q):
    r = {}
    for k, v in p.items():
        for l, w in q.items():
            key = tuple(a+b for a, b in zip(k, l))
            r[key] = r.get(key, F(0)) + v*w
    return {k: v for k, v in r.items() if v}


def smul(p, q):
    return [sum_poly(mul(p[k], q[j-k]) for k in range(j+1))
            for j in range(len(p))]


def sum_poly(items):
    r = {}
    for p in items:
        r = add(r, p)
    return r


def sexp(f, dimensions):
    assert not f[0]
    e = [{(0,)*dimensions: F(1)}]
    for n in range(1, len(f)):
        e.append(scale(sum_poly(scale(mul(f[k], e[n-k]), k)
                                for k in range(1, n+1)), F(1, n)))
    return e


def derivative_polynomials():
    # exp(t/2) [8 a^2 exp(4t)-12 a exp(2t)]
    #                * exp(-a(exp(2t)-1)), modulo t^9.
    prefactor = [{(2,): F(8*4**n, math.factorial(n)),
                  (1,): F(-12*2**n, math.factorial(n))} for n in range(9)]
    outer = [{(0,): F(1, 2**n*math.factorial(n))} for n in range(9)]
    exponent = [{}] + [{(1,): F(-2**n, math.factorial(n))} for n in range(1, 9)]
    result = smul(smul(prefactor, outer), sexp(exponent, 1))
    return [{str(k[0]): str(v*math.factorial(n)) for k, v in sorted(p.items())}
            for n, p in enumerate(result)]


def formal_observables():
    zero = (0,)*4
    f = [{zero: F(1)}] + [{tuple(int(i == j) for i in range(4)): F(1)}
                         for j in range(4)]
    inverse = [{zero: F(1)}]
    for n in range(1, 5):
        inverse.append(scale(sum_poly(mul(f[k], inverse[n-k])
                                      for k in range(1, n+1)), -1))
    # f'/f generates the logarithm coefficients, with zero constant.
    log = [{}]
    for n in range(1, 5):
        log.append(scale(sum_poly(scale(mul(f[k], inverse[n-k]), k)
                                  for k in range(1, n+1)), F(1, n)))
    # D_v^k H/(K(0)u/m0) has coefficients (2j+1)^k f_j.
    jets = [[scale(f[j], (2*j+1)**k) for j in range(5)] for k in range(5)]
    det = [{} for _ in range(5)]
    for perm in itertools.permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        product = smul(smul(jets[perm[0]], jets[1+perm[1]]), jets[2+perm[2]])
        det = [add(a, scale(b, (-1)**inversions)) for a, b in zip(det, product)]
    q = [scale(p, -1) for p in smul(det, smul(smul(inverse, inverse), inverse))]
    serial = lambda ss: [[{'powers': list(k), 'coefficient': str(v)}
                         for k, v in sorted(p.items())] for p in ss]
    return serial(log), serial(q)


def main():
    original = HERE / 'endpoints_634.json'
    original_bytes = original.read_bytes()
    saved = json.loads(original_bytes)
    report = {'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
              'program_sha256': hashlib.sha256((HERE/'endpoints_634.py').read_bytes()).hexdigest(),
              'arithmetic_program_sha256': hashlib.sha256((HERE/'confluent_compact_audit_614.py').read_bytes()).hexdigest(),
              'failures': []}
    failures = report['failures']

    def check(ok, label):
        if not ok:
            failures.append(label)
        return bool(ok)

    source.OUT = REPLAY
    with contextlib.redirect_stdout(io.StringIO()) as replay_stdout:
        source.main()
    replay = json.loads(REPLAY.read_text())
    report['replay_all_fields_equal'] = check(replay == saved, 'complete replay differs')
    report['original_preserved'] = check(original.read_bytes() == original_bytes, 'original changed')
    report['replay_stdout'] = replay_stdout.getvalue().splitlines()

    polys = derivative_polynomials()
    report['independent_derivative_polynomials'] = polys
    check(len(saved['derivatives']) == 9, 'derivative row count')
    check(polys == [row['polynomial'] for row in saved['derivatives']], 'generating series P0..P8')
    log, q = formal_observables()
    report['independent_log_series'] = log
    report['direct_signed_determinant_series'] = q
    check(log == saved['log_series'], 'independent logarithm coefficients')
    check(q == saved['Q3_series'], 'direct determinant Q3 coefficients')

    # Same proved integer-lattice operations, strictly finer lattice and pi.
    # These module constants are process-local, never changes to the source.
    ar.BITS, ar.S, ar.TERMS = 1536, 1 << 1536, 320
    B, S = ar.Box, ar.S
    old_scale = int(saved['arithmetic']['scale'])
    check(old_scale == 1 << 1024, 'saved scale')
    a, b = ar.atan(5, 160)
    c, d = ar.atan(239, 60)
    pi = B(B.of(16*a-4*d).lo, B.of(16*b-4*c).hi)
    report['independent_arithmetic'] = {'bits': ar.BITS, 'scale': str(S),
                                       'Taylor_degree': ar.TERMS, 'Machin_terms': [160, 60]}
    comparisons = []

    def inside(value, old, label):
        ok = int(old[0])*S <= value.lo*old_scale <= value.hi*old_scale <= int(old[1])*S
        comparisons.append({'field': label, 'contained': check(ok, label+' containment')})

    inside(pi, saved['pi'], 'pi')
    check(3*S < pi.lo <= pi.hi < 4*S, '3<pi<4')
    ratio = B.of(F(10, 9)**20)*ar.exp_box(B.of(-57))
    inside(ratio, saved['tail_ratio'], 'tail_ratio')
    check(2*ratio.hi < S, 'origin geometric ratio')
    report['pi'], report['tail_ratio'] = pi.data(), ratio.data()
    rows, full = [], []
    for r, (p, old) in enumerate(zip(polys, saved['derivatives'])):
        p = {int(k): F(v) for k, v in p.items()}
        norm = sum(abs(v) for v in p.values())
        check(norm == F(old['coefficient_norm']), 'P'+str(r)+' norm')
        check(max(p) == r+2, 'P'+str(r)+' degree')
        check(len(old['finite_terms']) == 8, 'finite term count '+str(r))
        terms = []
        for n in range(1, 9):
            x = pi*(n*n)
            # Direct monomial sum, independent of source's Horner evaluator.
            value = sum((coef*x**k for k, coef in sorted(p.items())), B.of(0))*ar.exp_box(-x)
            inside(value, old['finite_terms'][n-1], f'P{r}/term{n}')
            terms.append(value)
        finite = sum(terms, B.of(0))
        tail = B.of(2*norm*4**(r+2)*9**(2*r+4))*ar.exp_box(B.of(-243))
        value = finite + B(-tail.hi, tail.hi)
        inside(finite, old['finite_sum'], f'P{r}/finite_sum')
        inside(value, old['full'], f'P{r}/full')
        check(tail.hi*old_scale <= int(old['tail_upper'])*S, f'P{r}/tail upper')
        full.append(value)
        rows.append({'r': r, 'norm': str(norm), 'finite_terms': [x.data() for x in terms],
                     'finite_sum': finite.data(), 'tail': tail.data(), 'full': value.data()})
    report['derivatives'] = rows
    check(full[0].lo > 0, 'K0 positive denominator')
    coeff = [full[2*j]/math.factorial(2*j)/full[0] for j in range(1, 5)]
    for j, v in enumerate(coeff):
        inside(v, saved['normalized_even_coefficients'][str(2*j+2)], f'c{2*j+2}')
    leading = -256*coeff[0]*coeff[1]
    next_term = 768*coeff[0]*(coeff[0]*coeff[1]-3*coeff[2])
    inside(leading, saved['origin_leading'], 'C6')
    inside(next_term, saved['origin_u8'], 'C8')
    bounds = [('K0', full[0], 1, 2), ('c2', coeff[0], -10, -9),
              ('c4', coeff[1], 37, 39), ('C6', leading, 90000, 91000)]
    report['coarse_bounds'] = [{'name': name, 'actual': value.data(),
                              'required': [str(lo), str(hi)],
                              'passed': check(lo*S < value.lo <= value.hi < hi*S, name+' strict bounds')}
                             for name, value, lo, hi in bounds]
    report['normalized_even_coefficients'] = {str(2*j+2): v.data() for j, v in enumerate(coeff)}
    report['origin_leading'], report['origin_u8'] = leading.data(), next_term.data()
    report['complete_interval_comparisons'] = comparisons

    # Check every infinity coefficient norm and the integer constants.
    r_polys = ar.independent_polys()
    majorants = [20, 160, 1760, 24640, 418880]
    infinity_rows = []
    for j, p in enumerate(r_polys):
        norm = sum(abs(x) for x in p.values())
        ok = norm <= majorants[j] and all(i <= j and h+k <= j+2 for i, h, k in p)
        infinity_rows.append({'j': j, 'actual_norm': norm, 'majorant': majorants[j],
                              'degree_and_norm_passed': check(ok, 'infinity R'+str(j))})
    E = [160]
    for j in range(1, 5):
        E.append(majorants[j]*2**(2*j+3) +
                 sum(math.comb(j, k)*(majorants[k]//4)*E[j-k] for k in range(1, j+1)))
    F2 = E[2]+E[1]**2
    F3 = E[3]+3*E[1]*E[2]+2*E[1]**3
    F4 = E[4]+4*E[1]*E[3]+3*E[2]**2+12*E[1]**2*E[2]+6*E[1]**4
    C0 = 2*2200**2+2*2053*(2200**2+2200*6+36)
    Cstar = 4400*F3+F3**2+2200*(F2+F4)+F2*F4+6*2200**2*F2+6*2200*F2**2+2*F2**3
    report['infinity_constants'] = {'R_checks': infinity_rows, 'E': E,
                                    'F2_F3_F4': [F2, F3, F4], 'C0': C0, 'Cstar': Cstar,
                                    'geometric_ratio_rational_check': check(F(15**3, 6) > 2*F(3, 2)**12, 'infinity ratio')}
    report['analytic_scope'] = 'All-u differentiated estimates and limits are proved in L826 audit; this certificate does not replace them.'
    report['result'] = 'PASS' if not failures else 'FAIL'
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('Complete replay:', report['replay_all_fields_equal'], '; independent interval containments:', len(comparisons))
    print('Formal P0..P8, logarithm and direct determinant through u^8:', 'PASS' if not failures else 'see failures')
    for name, value, lo, hi in bounds:
        print(f'{name}: actual approximately [{float(F(value.lo,S)):.15g}, {float(F(value.hi,S)):.15g}]; required strictly ({lo},{hi}); exact check retained')
    print('Failures:', failures)
    print('Full certificate:', OUT.relative_to(HERE.parent.parent))
    print('Preserved-source replay:', REPLAY.relative_to(HERE.parent.parent))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
