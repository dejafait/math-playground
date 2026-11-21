#!/usr/bin/env python3
"""Replay the full saved exact evidence, without importing the producer."""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial, prod
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE/'l938-zero-superlevel-58.json'
OUT = HERE/'l938-zero-superlevel-replay-58.json'
data = json.loads(SOURCE.read_text())
checks = []
failures = []


def ck(name, condition):
    checks.append({'name': name, 'ok': bool(condition)})
    if not condition:
        failures.append(name)
        raise ValueError(name)


def poly(xs):
    return list(map(F, xs))


def ev(p, x):
    # Direct power sum, independent of the producer's Horner evaluation.
    return sum((c*x**j for j, c in enumerate(p)), F(0))


def sg(v):
    return int(v > 0)-int(v < 0)


def variations(signs):
    nz = [s for s in signs if s]
    return sum(nz[i] != nz[i-1] for i in range(1, len(nz)))


def endpoint(chain, record):
    x = F(record['q'])
    vals = [ev(p, x) for p in chain]
    signs = list(map(sg, vals))
    ck(f'endpoint {x}: every value/sign/variation',
       vals == poly(record['values']) and signs == record['signs'] and
       variations(signs) == record['variations'] and vals[0] != 0)
    return variations(signs)


def main():
    ck('producer failure list empty', data['failures'] == [])
    for rel, expected in data['input_sha256'].items():
        ck(f'input hash {rel}', sha256((ROOT/rel).read_bytes()).hexdigest() == expected)
    text = (ROOT/'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text()
    rows = [(int(c), tuple(map(int, a.split(',')))) for c, a in re.findall(
        r'^\|\s*(-?\d+)\s*\|\s*\(([^)]+)\)\s*\|\s*$', text, re.M)]
    ck('original 34 rows match certificate', rows == [(r['c'], tuple(r['alpha']))
                                                    for r in data['rows']])
    summary = []
    for m in range(1, 7):
        block = data['blocks'][str(m)]
        h = [F(0)]*13
        for row, (c, alpha) in enumerate(rows):
            state = {(0, 0): 1}
            for k, n in enumerate(alpha):
                nxt = {}
                for (used, degree), weight in state.items():
                    for take in range(min(n, m-used)+1):
                        key = (used+take, degree+k*take)
                        nxt[key] = nxt.get(key, 0)+weight*comb(n, take)
                state = nxt
            counts = [state.get((m, j), 0) for j in range(13)]
            factorials = prod(factorial(2*k)**n for k, n in enumerate(alpha))
            saved = data['rows'][row]['blocks'][str(m)]
            rh = [F(c*count, factorials*comb(12, m)) for count in counts]
            ck(f'm={m}, row={row+1}: independent coefficient reconstruction',
               counts == saved['counts'] and rh == poly(saved['H_coefficients']))
            h = [a+b for a, b in zip(h, rh)]
        while h and h[-1] == 0:
            h.pop()
        n = poly(block['integer_coefficients'])
        ck(f'm={m}: full coefficients and positive normalization',
           h == poly(block['H_coefficients']) and
           F(block['integer_positive_factor']) > 0 and
           n == [F(block['integer_positive_factor'])*c for c in h])
        ck(f'm={m}: zero/constant/excluded-zero cases',
           not block['zero_polynomial'] and not block['constant_polynomial'] and
           block['excluded_zero_multiplicity'] == 0 and n[0] != 0)
        record = block['sturm']
        chain = [poly(p) for p in record['polynomials']]
        s0, s1 = poly(record['initial_positive_factors'])
        ck(f'm={m}: Sturm initial positive rescaling', s0 > 0 and s1 > 0 and
           chain[0] == [s0*c for c in n] and
           chain[1] == [s1*i*n[i] for i in range(1, len(n))])
        ck(f'm={m}: division count', len(record['division_identities']) == len(chain)-1)
        for j, identity in enumerate(record['division_identities']):
            a, b = chain[j], chain[j+1]
            quotient = poly(identity['quotient'])
            nxt = poly(identity['next'])
            factor = F(identity['next_positive_factor'])
            ck(f'm={m}, division={j}: positive factor and strict degree',
               factor > 0 and len(nxt) < len(b) and
               nxt == (chain[j+2] if j+2 < len(chain) else []))
            # Check every coefficient of a = quotient*b - next/factor.
            for k in range(max(len(a), len(quotient)+len(b)-1, len(nxt))):
                rhs = sum((quotient[i]*b[k-i] for i in range(len(quotient))
                           if 0 <= k-i < len(b)), F(0))
                if k < len(nxt):
                    rhs -= nxt[k]/factor
                ck(f'm={m}, division={j}, coefficient={k}',
                   rhs == (a[k] if k < len(a) else 0))
        ck(f'm={m}: constant gcd rules out ALL multiple roots',
           len(chain[-1]) == 1 and chain[-1][0] != 0 and
           block['successive_gcds'] == [] and block['terminal_monic_gcd'] == ['1'])
        B = F(block['root_bound']['outer_integer'])
        bound = F(1)+max(abs(c/n[-1]) for c in n[:-1])
        ck(f'm={m}: complete outer bound',
           B > bound == F(block['root_bound']['monic_Cauchy']))
        vs = [endpoint(chain, r) for r in block['global_endpoints']]
        ck(f'm={m}: global count', vs[0]-vs[-1] == len(block['roots']) ==
           block['total_positive_roots'])
        previous = F(0)
        root_variations = []
        for root in block['roots']:
            a, b = F(root['lower']), F(root['upper'])
            ck(f'm={m}, root={root["index"]}: ordered nonroot isolator',
               previous < a < b < B and (b < 1 or a > 1))
            va, vb = endpoint(chain, root['left']), endpoint(chain, root['right'])
            ck(f'm={m}, root={root["index"]}: exactly one simple root',
               va-vb == 1 and root['multiplicity'] == 1)
            root_variations.append([va, vb])
            previous = b
        signs = []
        for i, interval in enumerate(block['open_intervals']):
            x = F(interval['sample'])
            left = F(0) if i == 0 else F(block['roots'][i-1]['upper'])
            right = B+1 if i == len(block['roots']) else F(block['roots'][i]['lower'])
            v = ev(h, x)
            ck(f'm={m}, interval={i}: entire sign via complete root table',
               left < x < right and v == F(interval['H_at_sample']) and
               sg(v) == interval['sign'] != 0)
            signs.append(sg(v))
        ck(f'm={m}: sign at one', ev(h, F(1)) == F(1, 371319795000))
        exits = 0
        for i, root in enumerate(block['roots']):
            inward = i+1 if F(root['upper']) < 1 else i
            ck(f'm={m}, root={i+1}: closed-set inward test',
               root['inward_interval'] == inward and root['inward_sign'] == signs[inward])
            exits += int(signs[inward] < 0)
        ck(f'm={m}: complete exit classification',
           exits == len(block['inward_exits']) and block['zero_superlevel_inward_preserved'] ==
           (exits == 0))
        summary.append({'m': m, 'B': str(B), 'V_0_1_B': vs,
                        'root_endpoint_variations': root_variations,
                        'interval_signs': signs, 'simple_roots': len(block['roots']),
                        'inward_exits': exits})
    w = data['witness']
    q0, q1, rho = F(w['q0']), F(w['q1']), F(w['rho'])
    t0, t1 = poly(w['t0']), poly(w['t1'])
    n = poly(w['integer_polynomial'])
    den = F(w['evaluation_denominator'])
    ck('witness exact integer evaluations',
       ev(n, q0)*den == F(w['N_q0_numerator']) > 0 and
       ev(n, q1)*den == F(w['N_q1_numerator']) < 0)
    ck('witness normalized positive simplex and inward majorization',
       0 < q0 < q1 < 1 and 0 < rho < 1 and
       sum(t0) == sum(t1) == 1 and min(t0+t1) > 0 and
       all(b == rho*a+(1-rho)/12 for a, b in zip(t0, t1)))
    for q, t, name in [(q0, t0, '0'), (q1, t1, '1')]:
        hq = ev(poly(data['blocks']['4']['H_coefficients']), q)
        ck(f'witness {name}: actual normalized value',
           F(w[f'H_q{name}']) == hq and F(w[f'Pbar_t{name}']) == hq/(4*q+8)**12 and
           t == [q/(4*q+8)]*4+[1/(4*q+8)]*8)
    return summary


result = {'input_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'replay_script_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
try:
    result['complete_tables'] = main()
except Exception as exc:
    failures.append({'exception': type(exc).__name__, 'message': str(exc)})
result.update(checks=checks, failures=failures, checks_count=len(checks))
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'result': 'PASS' if not failures else 'FAILED',
                  'checks': len(checks), 'failures': failures,
                  'complete_tables': result.get('complete_tables'),
                  'certificate': str(OUT.relative_to(ROOT))}, indent=2))
raise SystemExit(bool(failures))
