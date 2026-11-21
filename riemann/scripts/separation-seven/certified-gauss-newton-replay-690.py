#!/usr/bin/env python3
"""Check the complete relevant stopped trace using rational Bonnet evaluation.

This is proof verification, not an additional setup prescription. No
rounding rule, precision, node or numerical schedule is changed.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('certified-gauss-newton-690.json')
OUT = HERE.with_suffix('.json')
data = json.loads(SOURCE.read_text())
first = json.loads(HERE.with_name('certified-gauss-newton-first-run-690.json').read_text())
D = 2**data['grid_bits']
counts = Counter()
failures = []


def ck(condition, name):
    counts[name] += 1
    if not condition:
        failures.append(name)
        raise AssertionError(name)


def zi(a):
    return int(a['odd_hex'], 16) << a['shift']


def rf(a):
    return F(zi(a['num']), zi(a['den']))


def iv(a):
    return tuple(map(rf, a))


def gi(a):
    return tuple(map(zi, a))


def pol(n, a):
    #Independent unscaled exact rational recurrence, no construction import.
    x = F(a, D)
    prev, p = F(1), x
    for k in range(1, n):
        prev, p = p, ((2*k+1)*x*p-k*prev)/(k+1)
    return prev, p


def check_values(n, a, values, pair=True):
    pm, pn = pol(n, a)
    if pair:
        ck(pm == F(zi(values[0]), factorial(n-1)*D**(n-1)), 'adjacent value exact')
        q = values[1]
    else:
        q = values
    ck(pn == F(zi(q), factorial(n)*D**n), 'polynomial value exact')
    return pm, pn


def derivative(n, lo, hi, a, values):
    pm, pn = check_values(n, a, values)
    m = F(a, D)
    ck(2*a == lo+hi, 'center exact')
    dp = n*(pm-m*pn)/(1-m*m)
    rad = F(hi-lo, 2*D)
    endpoint = F((n-1)*n*(n+1)*(n+2), 8)
    interior = F(4*n*n)/(1-F(hi,D)**2)**2
    M = min(endpoint, interior)
    dl, du = dp-M*rad, dp+M*rad
    ck(dl > 0 or du < 0, 'full derivative excludes zero')
    return pn, dl, du, M


def update(n, lo, hi, record, failed=False):
    ck(gi(record['old_grid_interval']) == (lo, hi), 'old interval continuity')
    a = zi(record['point'])
    p, dl, du, M = derivative(n, lo, hi, a, record['scaled_adjacent_values'])
    ck(iv(record['derivative_range']) == (dl, du), 'full derivative range exact')
    ck(rf(record['second_derivative_bound']) == M, 'chosen second derivative bound exact')
    il, iu = sorted((F(a,D)-p/dl, F(a,D)-p/du))
    jl, ju = max(il,F(lo,D)), min(iu,F(hi,D))
    ck(iv(record['raw_newton_image']) == (il,iu), 'raw Newton image exact')
    ck(iv(record['intersected_image']) == (jl,ju), 'Newton intersection exact')
    ck(jl < ju, 'strictly positive image width')
    width, center = (ju-jl)*D, (ju+jl)*D/2
    ll, uu = lo, hi
    h = uu-ll
    iterations = record['conversion_failure']['completed_halvings'] if failed else record['binary_halvings']
    for _ in range(iterations):
        ck(h > width, 'each recorded halving required')
        ck((ll+uu) % 2 == 0 and h % 2 == 0, 'each recorded halving exact')
        mid = (ll+uu)//2
        if mid <= center:
            ll = mid
        else:
            uu = mid
        h //= 2
    if failed:
        failure = record['conversion_failure']
        ck(gi(failure['cell_grid_interval']) == (ll,uu), 'failed cell exact')
        ck(zi(failure['cell_grid_width']) == h == uu-ll, 'failed cell width exact')
        ck(rf(failure['image_width_in_grid_units']) == width, 'failed requested width exact')
        ck(record['old_depth']+iterations == failure['depth'] == 640, 'grid depth exhausted exactly')
        ck(h > width > 0 and h % 2 == 1 and (ll+uu) % 2 == 1,
           'next exact halving unavailable on fixed grid')
        return ju-jl, h, ll, uu
    ck(h <= width < 2*h, 'completed conversion stopping and size')
    nl, nu = max(lo,ll-h), min(hi,uu+h)
    ck(gi(record['new_grid_interval']) == (nl,nu), 'outward converted interval exact')
    ck(F(nl,D) <= jl <= ju <= F(nu,D), 'entire image covered')
    ck(0 < nu-nl < hi-lo, 'strict accepted contraction')
    return nl,nu


def dyadic_exponent_bound(q):
    """Return e with 2^(e-1)<q<=2^e, using exact integer comparisons."""
    ck(q > 0, 'positive reported width')
    e = q.numerator.bit_length()-q.denominator.bit_length()
    if q > F(2)**e:
        e += 1
    ck(F(2)**(e-1) < q <= F(2)**e, 'dyadic exponent bound exact')
    return e


summary = {}
try:
    ck(data['result'] == first['result'] == 'PRESCRIPTION_STOPPED', 'same stopped result')
    ck(data['rows'] == first['rows'] and data['scalar_work'] == first['scalar_work']
       and data['guard_counts'] == first['guard_counts'], 'evidence-only rerun unchanged')
    ck(data['failures'] == ['binary conversion grid not exhausted'], 'only recorded failure')
    ck(len(data['rows']) == 1 and data['rows'][0]['degree'] == 63, 'no other degree attempted')
    row, n = data['rows'][0], 63
    mesh, signs = [], []
    for j, entry in enumerate(row['mesh_sign_evidence']):
        a = zi(entry['point'])
        ck(a == (16384-j*j)*(D//16384), 'mesh generation exact')
        _, p = check_values(n,a,entry['scaled_value'],False)
        s = (p>0)-(p<0)
        ck(s == entry['sign'] != 0, 'mesh sign exact and nonzero')
        mesh.append(a)
        signs.append(s)
    brackets = [(mesh[j+1],mesh[j],signs[j+1],signs[j])
                for j in range(127) if signs[j] != signs[j+1]]
    ck(len(mesh) == 128 and len(brackets) == 31, 'all 31 positive roots isolated')
    ck(len(row['positive_roots']) == 2, 'only two positive roots started')
    for i, root in enumerate(row['positive_roots']):
        lo,hi,sl,su = brackets[i]
        ck(gi(root['initial_grid_bracket']) == (lo,hi), 'initial bracket from mesh')
        ck(root['initial_signs'] == [sl,su], 'initial signs match')
        ck(len(root['bisections']) == 16, 'exactly 16 prescribed bisections')
        for step in root['bisections']:
            a = zi(step['point'])
            ck(2*a == lo+hi, 'bisection center exact')
            _,p = check_values(n,a,step['scaled_value'],False)
            s = (p>0)-(p<0)
            ck(s == step['sign'] != 0, 'bisection sign exact and nonzero')
            if s == sl:
                lo,sl = a,s
            else:
                hi,su = a,s
            ck(sl*su == -1, 'root bracket retained')
        depth = 30
        for step in root['newton']:
            lo,hi = update(n,lo,hi,step)
            depth += step['binary_halvings']
            ck(depth == step['depth'], 'accepted grid depth exact')
        if i == 0:
            final = root['final']
            ck(iv(final['node']) == (F(lo,D),F(hi,D)), 'first output node exact')
            a = zi(final['derivative_point'])
            _,dl,du,M = derivative(n,lo,hi,a,final['scaled_adjacent_values'])
            ck(iv(final['derivative_range']) == (dl,du), 'final derivative exact')
            ck(rf(final['second_derivative_bound']) == M, 'final derivative bound exact')
            wl = 2/((1-F(lo,D)**2)*max(dl*dl,du*du))
            wu = 2/((1-F(hi,D)**2)*min(dl*dl,du*du))
            ck(iv(final['weight']) == (wl,wu), 'first output weight exact')
            nr,wr = F(hi-lo,2*D),(wu-wl)/2
            ck(rf(final['node_radius']) == nr and rf(final['weight_radius']) == wr,
               'separate first output radii exact')
            ck(nr <= F(1,2**512) and wr <= F(1,2**512), 'first output meets both radii')
            ck(iv(root['negative_node']) == (F(-hi,D),F(-lo,D))
               and root['negative_weight'] == final['weight'], 'reflection output exact')
            summary['completed_positive_nodes'] = 1
            summary['completed_reflected_nodes'] = 1
            summary['first_node_radius_upper_power_of_two'] = dyadic_exponent_bound(nr)
            summary['first_weight_radius_upper_power_of_two'] = dyadic_exponent_bound(wr)
        else:
            failure = data['failure_context']
            ck(failure['degree'] == n and failure['positive_root_index_descending'] == i
               and failure['newton_update_index'] == len(root['newton']) == 5,
               'failure location exactly sixth update of second root')
            ck(failure['old_depth'] == depth == 534, 'failure incoming depth 534')
            image_width,h,ll,uu = update(n,lo,hi,failure,True)
            summary.update({
                'failed_degree': n, 'failed_positive_root_index_descending': i,
                'failed_newton_update_one_based': 6,
                'incoming_depth': depth, 'completed_conversion_halvings': 106,
                'failed_cell_width_grid_units': h,
                'failed_cell_lower_grid_index_parity': ll%2,
                'failed_cell_upper_grid_index_parity': uu%2,
                'image_width_upper_power_of_two': dyadic_exponent_bound(image_width),
                'incoming_node_width_upper_power_of_two': dyadic_exponent_bound(F(hi-lo,D)),
                'failed_cell_width_upper_power_of_two': dyadic_exponent_bound(F(h,D)),
                'node_gate_was_not_yet_met': F(hi-lo,D) > F(1,2**550),
                'all_node_service_failed': True,
                'full_setup_work_upper_not_established': True})
    ck(data['scalar_work']['charged_upper'] == sum(data['scalar_work']['by_category'].values())
       == 183800 < 5_000_000, 'partial charged ledger arithmetic')
except AssertionError:
    pass

result = {'result': 'PASS_COMPLETE_RELEVANT_STOP_TRACE' if not failures else 'FAIL',
          'summary': summary, 'checks_by_name': dict(sorted(counts.items())),
          'failures': failures, 'source_certificate_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
          'qualification': 'Checks stopped prefix, not all-node success or completeness of a full setup-work upper bound'}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(result['result'])
print('Exact checks:',sum(counts.values()),'; failures:',failures)
print('Node/weight setup: FAILED at fixed-grid safeguard; all-node target remains unpaid.')
print('Summary:',json.dumps(summary,sort_keys=True))
print('Full replay certificate:',OUT.relative_to(HERE.parents[2]))
if failures:
    raise SystemExit(1)
