#!/usr/bin/env python3
"""Check the complete tolerance-capped trace using rational Bonnet evaluation.

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
SOURCE = HERE.with_name('certified-gauss-adaptive-692.json')
OUT = HERE.with_suffix('.json')
data = json.loads(SOURCE.read_text())
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


def derivative(n, lo, hi, a, values, allow_zero=False):
    pm, pn = check_values(n, a, values)
    m = F(a, D)
    ck(2*a == lo+hi, 'center exact')
    dp = n*(pm-m*pn)/(1-m*m)
    rad = F(hi-lo, 2*D)
    endpoint = F((n-1)*n*(n+1)*(n+2), 8)
    interior = F(4*n*n)/(1-F(hi,D)**2)**2
    M = min(endpoint, interior)
    dl, du = dp-M*rad, dp+M*rad
    if not allow_zero:
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
    target = max(width, F(D,2**560))
    ll, uu = lo, hi
    h = uu-ll
    iterations = record['conversion_failure']['completed_halvings'] if failed else record['binary_halvings']
    for _ in range(iterations):
        ck(h > target, 'each recorded halving required')
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
    ck(h <= target < 2*h, 'completed conversion stopping and size')
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
    ck(data['grid_bits'] == 640 and data['conversion_tolerance_width'] == '2^-560', 'prescription constants')
    ck(data['degrees'] == [63,81,117], 'prescribed degrees')
    positive_count = completed_count = newton_count = halving_count = 0
    max_nr = max_wr = F(0)
    complete_degrees = []
    for row in data['rows']:
        n = row['degree']
        mesh, signs = [], []
        for j, entry in enumerate(row['mesh_sign_evidence']):
            a = zi(entry['point'])
            ck(a == (16384-j*j)*(D//16384), 'mesh generation exact')
            _, p = check_values(n,a,entry['scaled_value'],False)
            sign = (p>0)-(p<0)
            ck(sign == entry['sign'] != 0, 'mesh sign exact and nonzero')
            mesh.append(a)
            signs.append(sign)
        ck(len(mesh) == 128, 'entire mesh evaluated')
        brackets = [(mesh[j+1],mesh[j],signs[j+1],signs[j])
                    for j in range(127) if signs[j] != signs[j+1]]
        ck(len(brackets) == (n-1)//2, 'complete positive root isolation')
        for i, root in enumerate(row['positive_roots']):
            positive_count += 1
            lo,hi,sl,su = brackets[i]
            ck(root['index_descending'] == i, 'root order exact')
            ck(gi(root['initial_grid_bracket']) == (lo,hi), 'initial bracket from mesh')
            ck(root['initial_signs'] == [sl,su], 'initial signs match')
            ck(1 <= len(root['adaptive_trials']) <= 17, 'bounded adaptive trials')
            bis = iter(root['bisections'])
            accepted_seed = False
            for j, trial in enumerate(root['adaptive_trials']):
                ck(gi(trial['old_grid_interval']) == (lo,hi), 'adaptive old interval exact')
                ck(trial['depth'] == 14+j, 'adaptive depth exact')
                a = zi(trial['point'])
                pn,dl,du,M = derivative(n,lo,hi,a,trial['scaled_adjacent_values'],True)
                ck(iv(trial['derivative_range']) == (dl,du), 'adaptive full derivative range exact')
                ck(rf(trial['second_derivative_bound']) == M, 'adaptive second derivative bound exact')
                dp = (dl+du)/2
                accepted = (dl > 0 or du < 0) and M*F(hi-lo,2*D) <= abs(dp)/8
                ck(trial['accepted'] == accepted, 'adaptive stopping guard exact')
                if accepted:
                    ck(j == len(root['adaptive_trials'])-1, 'accepted trial last')
                    accepted_seed = True
                    break
                ck(j < 16, 'fallback schedule available')
                step = next(bis)
                ck(zi(step['point']) == a and step['scaled_value'] == trial['scaled_adjacent_values'][1],
                   'fallback reuses exact midpoint evaluation')
                sign = (pn>0)-(pn<0)
                ck(sign == step['sign'] != 0, 'fallback sign exact')
                if sign == sl:
                    lo,sl = a,sign
                else:
                    hi,su = a,sign
                ck(sl*su == -1, 'fallback retains root bracket')
            ck(next(bis,None) is None, 'all fallback records consumed')
            ck(accepted_seed and len(root['adaptive_trials']) == len(root['bisections'])+1,
               'one accepted prefix after all fallbacks')
            depth = 14+len(root['bisections'])
            if root['newton']:
                first = root['newton'][0]
                trial = root['adaptive_trials'][-1]
                ck(all(first[k] == trial[k] for k in ('old_grid_interval','point',
                    'scaled_adjacent_values','derivative_range','second_derivative_bound')),
                    'first Newton step reuses accepted derivative evidence')
            for step in root['newton']:
                ck(depth < 640, 'old midpoint depth available')
                lo,hi = update(n,lo,hi,step)
                depth += step['binary_halvings']
                newton_count += 1
                halving_count += step['binary_halvings']
                ck(depth == step['depth'] < 640, 'accepted grid depth exact')
            if 'final' not in root:
                ck(data['result'] == 'PRESCRIPTION_STOPPED', 'incomplete root only on stop')
                summary['incomplete_root'] = {'degree': n, 'index_descending':i,
                    'bisections':len(root['bisections']), 'newton_updates':len(root['newton'])}
                continue
            ck(len(root['newton']) <= 12, 'bounded Newton schedule')
            ck(F(hi-lo,D) <= F(1,2**550), 'node output gate reached')
            final = root['final']
            ck(iv(final['node']) == (F(lo,D),F(hi,D)), 'output node exact')
            a = zi(final['derivative_point'])
            _,dl,du,M = derivative(n,lo,hi,a,final['scaled_adjacent_values'])
            ck(iv(final['derivative_range']) == (dl,du), 'final derivative exact')
            ck(rf(final['second_derivative_bound']) == M, 'final derivative bound exact')
            wl = 2/((1-F(lo,D)**2)*max(dl*dl,du*du))
            wu = 2/((1-F(hi,D)**2)*min(dl*dl,du*du))
            ck(iv(final['weight']) == (wl,wu), 'output weight exact')
            nr,wr = F(hi-lo,2*D),(wu-wl)/2
            ck(rf(final['node_radius']) == nr and rf(final['weight_radius']) == wr,
               'separate output radii exact')
            ck(nr <= F(1,2**512) and wr <= F(1,2**512), 'output meets both radii')
            ck(iv(root['negative_node']) == (F(-hi,D),F(-lo,D))
               and root['negative_weight'] == final['weight'], 'reflection output exact')
            max_nr,max_wr = max(max_nr,nr),max(max_wr,wr)
            completed_count += 2
        if 'zero_node' in row:
            ck(len(row['positive_roots']) == len(brackets) and
               all('final' in root for root in row['positive_roots']), 'all positive roots before zero output')
            zero = row['zero_node']
            pm,pn = check_values(n,0,zero['scaled_adjacent_values'])
            ck(pn == 0 and pm != 0, 'simple exact zero node')
            w0 = 2/(n*pm)**2
            ck(iv(zero['node']) == (0,0) and iv(zero['weight']) == (w0,w0), 'zero node and weight exact')
            ck(row['total_nodes'] == n, 'degree output inventory exact')
            complete_degrees.append(n)
            completed_count += 1
    work = data['scalar_work']
    ck(work['scheduled_charge'] == sum(work['by_category'].values()), 'charged ledger arithmetic')
    ck(work['required_upper'] == 5_000_000, 'required setup cap')
    if data['result'] == 'PASS_ALL_NODES_WEIGHTS_AND_SETUP_CAP':
        ck(complete_degrees == [63,81,117] and completed_count == 261, 'all261 nodes and weights')
        ck(work['scheduled_charge'] <= 5_000_000, 'full claimed ledger within cap')
        ck(data['failures'] == [], 'no construction failure')
        ck(data['summary']['accepted_newton_updates'] == newton_count and
           data['summary']['binary_conversion_halvings'] == halving_count, 'summary refinement counts exact')
        ck(rf(data['summary']['maximum_node_radius']) == max_nr and
           rf(data['summary']['maximum_weight_radius']) == max_wr, 'summary maximum radii exact')
    summary.update({'complete_degrees':complete_degrees, 'positive_roots_started':positive_count,
        'completed_nodes_and_weights':completed_count, 'accepted_newton_updates':newton_count,
        'conversion_halvings':halving_count, 'max_node_radius_upper_power_of_two':dyadic_exponent_bound(max_nr),
        'max_weight_radius_upper_power_of_two':dyadic_exponent_bound(max_wr),
        'scheduled_ledger':work['scheduled_charge'], 'required_setup_cap':5_000_000,
        'construction_result':data['result'], 'construction_failures':data['failures']})
except AssertionError:
    pass
result = {'result':'PASS_COMPLETE_RECORDED_TRACE' if not failures else 'FAIL',
    'summary':summary, 'checks_by_name':dict(sorted(counts.items())), 'failures':failures,
    'source_certificate_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
    'script_sha256':sha256(HERE.read_bytes()).hexdigest(),
    'qualification':'Exact unscaled rational replay; scalar ledger completeness needs a separate code-level argument'}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(result['result'])
print('Exact checks:',sum(counts.values()),'; failures:',failures)
print('Summary:',json.dumps(summary,sort_keys=True))
print('Full replay certificate:',OUT.relative_to(HERE.parents[2]))
if failures:
    raise SystemExit(1)
