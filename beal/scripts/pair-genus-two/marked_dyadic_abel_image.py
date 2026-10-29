"""Approved marked point-image specialization using accepted L145 arithmetic."""
from pathlib import Path
import hashlib
import json
import traceback
from collections import deque
import two_adic_filter as A

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'marked-dyadic-abel-certificate.json'
D = dict(completed=False, failures=[], bindings={}, checks=[], disks=[],
         unresolved=[], bounds=dict(disk_cap=200000, disks_processed=0,
         depth_cap=64, max_depth=0, residue_table_cap=2**20,
         residue_table_actual=512, rational_bits_cap=8192))
Q = A.Q

def read(name):
    raw = (ROOT/name).read_bytes()
    D['bindings'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def ck(name, value):
    D['checks'].append(dict(name=name, passed=bool(value)))
    assert value, name

def polyadd(a, b):
    z = [Q(0)] * max(len(a), len(b))
    for i, c in enumerate(a): z[i] += Q(c)
    for i, c in enumerate(b): z[i] += Q(c)
    return z

def polymul(a, b):
    z = [Q(0)] * (len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b): z[i+j] += Q(c)*Q(d)
    return z

def compose(p, x):
    z = [Q(0)]
    for c in reversed(p): z = polyadd(polymul(z, x), [Q(c)])
    return z

def main():
    C = read('two-adic-filter-certificate.json')
    audit = read('two-adic-filter-audit.json')
    ck('accepted arithmetic', C['completed'] and not C['failures'] and
       audit['completed'] and not audit['failures'] and
       audit['bindings']['two-adic-filter-certificate.json'] ==
       D['bindings']['two-adic-filter-certificate.json'])
    M = read('odd-model-support-certificate.json')
    ck('bound exact odd model', C['bindings']['odd-model-support-certificate.json'] ==
       D['bindings']['odd-model-support-certificate.json'])
    A.E = list(map(Q, C['field']['pi_polynomial']))
    A.PIINV = [-A.E[i+1]/A.E[0] for i in range(4)]
    A.UNITMASK = {int(k): v for k, v in C['square_table']['unit_masks'].items()}
    eta = list(map(Q, C['field']['eta_pi']))
    b0 = A.add([Q(9075), 0, 0, 0], A.scale(eta, -1))
    g = list(map(Q, M['model']['G']))
    gc = list(map(Q, [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]))
    grev = list(reversed(gc))
    residual = polyadd(compose(g, [9075, 0, 3025]),
                       [0, 0] + [-Q(3025)**4*c for c in gc])
    ck('full vertical-map polynomial identity', all(c == 0 for c in residual))
    D['map'] = dict(X=[9075, 0, 3025], Y_multiplier=[0, 3025**2],
                    full_curve_identity_residual=residual)
    c = Q(-36300)
    character_left = [-3*c*c, -12*c]
    character_right = [-Q(660)**2*9075, Q(660)**2]
    ck('exact marking character', character_left == character_right)
    D['marking_character'] = dict(
        identity='3(4-(2+c/X)^2)=660^2*(X-9075)/X^2', c=c,
        numerator_left=character_left, numerator_right=character_right,
        X_zero_curve_value=A.evaluate(g, Q(0)),
        X_zero_square_class=A.rational_class(A.evaluate(g, Q(0))))
    ck('no local sextic infinity', D['marking_character']['X_zero_square_class']['mask'] != 0)
    branch = A.pair(A.evaluate(M['model']['H'], Q(9075)), b0)
    saved_branch = C['generators'][0]['evaluation']
    ck('branch is accepted class', branch['mask'] == saved_branch['mask'] and
       branch['quartic']['coefficients'] == list(map(Q, saved_branch['quartic']['coefficients'])) and
       branch['rational']['value'] == Q(saved_branch['rational']['value']))
    ck('branch rational component square', branch['rational']['mask'] == 0)
    D['branch'] = branch

    # These are L122's complete source-coordinate partition, not fake labels.
    initial = [('t', a, 3) for a in (0, 2, 4, 6)] + [
        ('t', a, 4) for a in (3, 13)] + [('q', a, 3) for a in (0, 2, 4, 6)]
    D['initial_partition'] = [list(x) for x in initial]
    todo = deque(initial)
    while todo:
        if D['bounds']['disks_processed'] >= D['bounds']['disk_cap']:
            D['unresolved'] = [list(x) for x in todo]
            raise AssertionError('disk cap with unresolved coverage')
        chart, a, depth = todo.popleft()
        D['bounds']['disks_processed'] += 1
        D['bounds']['max_depth'] = max(D['bounds']['max_depth'], depth)
        m = 2**depth
        # b(a+m*u)-b(a), in the full quartic field.
        if chart == 't':
            center = A.add(b0, [Q(3025*a*a), 0, 0, 0])
            coeff = [[Q(6050*a*m), 0, 0, 0], [Q(3025*m*m), 0, 0, 0]]
            qrep = Q(1)   # actual rational component is a square; branch separate
            curve_value = A.evaluate(gc, Q(a))
        else:
            center = A.add([Q(3025), 0, 0, 0], A.scale(b0, a*a))
            coeff = [A.scale(b0, 2*a*m), A.scale(b0, m*m)]
            qrep = Q(3025)
            curve_value = A.evaluate(grev, Q(a))
        ev = A.pair(qrep, center)
        bounds = [None if not any(c) else A.field_class(c)['valuation'] for c in coeff]
        actual = min(v for v in bounds if v is not None)
        required = ev['quartic']['valuation'] + 8
        if actual <= required:
            ck('refinement depth available', depth < D['bounds']['depth_cap'])
            todo.extend([(chart, a, depth+1), (chart, a+m, depth+1)])
            D.setdefault('refinements', []).append(dict(chart=chart, center=a, depth=depth,
                difference_bound=actual, strict_required=required))
            continue
        sq = A.rational_class(curve_value)
        ck('actual source center exists', sq['mask'] == 0 and curve_value != 0)
        ck('class lies in accepted eight-class image',
           A.reduce_mask(ev['mask'], C['image']['pivots']) == 0)
        D['disks'].append(dict(chart=chart, center=a, depth=depth, modulus=m,
            evaluation=ev, difference_coefficients=coeff,
            coefficient_valuations=bounds, difference_bound=actual,
            strict_required=required, curve_value=curve_value,
            source_square_certificate=sq,
            realization='two finite signs' if chart == 't' or a else
                        'two separate infinity points Z=+55,-55'))
    D['exceptions'] = dict(
        source_t_zero=dict(target='rational branch X=9075', evaluation=branch),
        source_infinities=[dict(Z=z, target='odd infinity', mask=0) for z in (-55, 55)],
        conic_infinity=dict(equation='t^2=-3', rational_square_mask=A.rational_class(Q(-3))['mask']),
        quartic_branch=dict(local_degree=4, rational_points=0),
        other_marking_zeros_poles='included on proper C; evaluation has no marking denominator')
    ck('no Q2 conic infinity', D['exceptions']['conic_infinity']['rational_square_mask'] != 0)
    values = sorted({r['evaluation']['mask'] for r in D['disks']} | {branch['mask'], 0})
    gens = [r['evaluation']['mask'] for r in C['generators']]
    ambient = sorted({__import__('functools').reduce(int.__xor__,
        (x for j, x in enumerate(gens) if (k >> j) & 1), 0) for k in range(8)})
    D['result'] = dict(marked_point_masks=values, marked_count=len(values),
        jacobian_masks=ambient, jacobian_count=len(ambient),
        excluded_masks=sorted(set(ambient)-set(values)), strict=set(values) < set(ambient),
        rational_projection_zero_masks=[x for x in ambient if not (x & 7)],
        new_rank_bound=None, independent_global_pruning_claimed=False)
    ck('rational marked character saturated',
       values == D['result']['rational_projection_zero_masks'])
    ck('all feasible disks closed', len(D['disks']) == 10 + len(D.get('refinements', [])))
    D['completed'] = True

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        D['failures'].append(dict(type=type(e).__name__, message=str(e), traceback=traceback.format_exc()))
    D['bounds']['max_rational_bits'] = A.D['bounds']['max_rational_bits']
    OUT.write_text(json.dumps(D, indent=2, default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'], failures=[f['message'] for f in D['failures']],
        result=D.get('result'), bounds=D['bounds'], certificate=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
