#!/usr/bin/env python3
"""One exact-rational, completely charged Gauss setup prescription.

The scalar ledger is an upper bound in C998g's arithmetic model, not a
bit-operation or wall-clock claim. No integer floor oracle is charged as
one real operation: dyadic interval conversion uses explicit binary search.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
CAP = 5_000_000
DEGREES = (63, 81, 117)
BITS = 640
NODE_GATE = F(1, 2**550)
TOL = F(1, 2**512)
CONVERSION_CAP = F(1, 2**560)
ledger = Counter()
checks = Counter()
report = {'prescription': 'working691, fixed before execution; output-tolerance cap',
          'degrees': list(DEGREES), 'grid_bits': BITS,
          'conversion_tolerance_width': '2^-560',
          'initial_bisections': 16, 'maximum_newton_updates': 12,
          'rows': [], 'failures': [], 'required': {
              'node_radius': '2^-512', 'weight_radius': '2^-512',
              'total_setup_work': CAP},
          'scope': 'Exact rational node/weight intervals only; no bank or square-service certificate'}


class Stop(Exception):
    pass


def pay(category, count):
    ledger[category] += count
    if sum(ledger.values()) > CAP:
        raise Stop('scalar setup cap exceeded')


def require(condition, name):
    checks[name] += 1
    if not condition:
        raise Stop(name)


def integer_record(a):
    # Lossless compression for proof serialization, outside service ledger.
    if not a:
        return {'odd_hex': '0x0', 'shift': 0}
    shift = (abs(a) & -abs(a)).bit_length() - 1
    return {'odd_hex': hex(a >> shift), 'shift': shift}


def rational_record(a):
    a = F(a)
    return {'num': integer_record(a.numerator),
            'den': integer_record(a.denominator)}


def interval_record(lo, hi):
    return [rational_record(lo), rational_record(hi)]


def ev(n, a):
    """Return exact scaled P_(n-1), P_n at a/D.

    Q_k=k! D^k P_k(a/D); Q_(k+1)=(2k+1)a Q_k-k^2 D^2 Q_(k-1).
    Four arithmetic operations, six register assignments, and three loop
    operations per stage:13. Table entries are operands, not extra copies.
    The24 overhead covers initialization, argument copies, final loop test,
    domain/sign guards, return copies and the caller's sign extraction.
    """
    pay('point_recurrence', 13*(n-1) + 24)
    require(0 <= a <= D, 'point in [0,1]')
    p, q = 1, a
    for k in range(1, n):
        u = A[k] * a
        v = u * q
        w = B[k] * p
        u = v - w
        p, q = q, u
    return p, q


def sign(a):
    return (a > 0) - (a < 0)


def derivative(n, lo, hi, depth):
    """Exact center values and a full derivative enclosure on [lo/D,hi/D]."""
    #120 covers center construction, domain/depth tests, P and derivative
    #conversion, both M bounds, radius, enclosure endpoints, zero exclusion,
    #and all register/argument/return copies. See canonical cost table.
    pay('derivative_enclosures', 120)
    require(depth < BITS, 'midpoint grid not exhausted')
    a = (lo + hi)//2
    require((lo+hi) % 2 == 0, 'exact grid midpoint')
    pm, pn = ev(n, a)
    x = F(a, D)
    p, prev = F(pn, DEN[n]), F(pm, DEN[n-1])
    d = n*(prev-x*p)/(1-x*x)
    r = F(max(a-lo, hi-a), D)
    h = F(hi, D)
    require(h < 1, 'interior upper endpoint')
    interior = F(4*n*n)/(1-h*h)**2
    M = min(GLOBAL[n], interior)
    dl, du = d-M*r, d+M*r
    require(dl > 0 or du < 0, 'derivative excludes zero')
    return a, p, d, dl, du, M, pm, pn


def quantize(jlo, jhi, oldlo, oldhi, depth):
    """Cover rational image by grid endpoints using only exact halving."""
    pay('binary_conversion_fixed', 40)
    pay('tolerance_cap_construction', 16)
    require(jlo <= jhi, 'nonempty intersected Newton image')
    if jlo == jhi:
        # No nonzero rational Legendre root is assumed absent. An exact
        #dyadic image could be handled, but this prescription stops here.
        raise Stop('zero-width rational image requires separate conversion')
    center = (jlo+jhi)*D/2
    width = (jhi-jlo)*D
    target_width = max(width, CONVERSION_CAP*D)
    ll, uu = oldlo, oldhi
    h = uu-ll
    steps = 0
    while h > target_width:
        #12 per pass: width comparison1, midpoint arithmetic/copies4,
        #center comparison1, endpoint copy1, h halving/copy2,
        #depth increment/copy2, grid-depth guard1.
        pay('binary_conversion_halvings', 12)
        if depth >= BITS:
            report['failure_context']['conversion_failure'] = {
                'cell_grid_interval': [integer_record(ll), integer_record(uu)],
                'cell_grid_width': integer_record(h), 'depth': depth,
                'completed_halvings': steps,
                'image_width_in_grid_units': rational_record(width),
                'next_halving_required': h > target_width,
                'root_image_still_contained': F(ll-h, D) <= jlo <= jhi <= F(uu+h, D)}
        require(depth < BITS, 'binary conversion grid not exhausted')
        mid = (ll+uu)//2
        require((ll+uu) % 2 == 0, 'conversion midpoint exact')
        if mid <= center:
            ll = mid
        else:
            uu = mid
        require(h % 2 == 0, 'conversion width halving exact')
        h //= 2
        depth += 1
        steps += 1
    require(uu-ll == h and h > target_width/2, 'rounding cell size invariant')
    nl, nu = max(oldlo, ll-h), min(oldhi, uu+h)
    require(F(nl, D) <= jlo <= jhi <= F(nu, D), 'outward binary conversion')
    require(nu-nl < oldhi-oldlo, 'strict rounded contraction')
    return nl, nu, depth, steps


def weights(n, lo, hi, depth):
    a, p, d, dl, du, M, pm, pn = derivative(n, lo, hi, depth)
    pay('weight_formation_and_output', 100)
    xlo, xhi = F(lo, D), F(hi, D)
    dsqlo, dsqhi = min(dl*dl, du*du), max(dl*dl, du*du)
    zlo, zhi = (1-xhi*xhi)*dsqlo, (1-xlo*xlo)*dsqhi
    require(0 < zlo <= zhi, 'positive weight denominator')
    wl, wu = 2/zhi, 2/zlo
    nr, wr = F(hi-lo, 2*D), (wu-wl)/2
    require(nr <= TOL, 'node radius target')
    require(wr <= TOL, 'weight radius target')
    return {'node': interval_record(xlo, xhi),
            'weight': interval_record(wl, wu),
            'node_radius': rational_record(nr),
            'weight_radius': rational_record(wr),
            'derivative_point': integer_record(a),
            'scaled_adjacent_values': [integer_record(pm), integer_record(pn)],
            'derivative_range': interval_record(dl, du),
            'second_derivative_bound': rational_record(M),
            'depth': depth}


def main():
    global D, A, B, DEN, GLOBAL
    #Generate all numerical constants. The only literals beyond control
    #sizes are small integers and exponents; no numerical table is read.
    #Six scalar operations per doubling include arithmetic, copies and loop.
    D = 1
    for _ in range(BITS):
        pay('grid_constant', 6)
        D *= 2
    #20 per index covers coefficient/denominator arithmetic, indexing,
    #assignments and loop control; constant arrays shared by all degrees.
    A, B, DEN = {}, {}, [1]
    pay('fixed_constant_and_output_administration', 10_000)
    pay('tolerance_constant_reserve', 4000)
    for k in range(1, max(DEGREES)+1):
        pay('recurrence_constant_tables', 20)
        A[k] = 2*k+1
        B[k] = k*k*D*D
        DEN.append(DEN[-1]*k*D)
    GLOBAL = {}
    for n in DEGREES:
        pay('degree_constants', 30)
        GLOBAL[n] = F((n-1)*n*(n+1)*(n+2), 8)
    mesh = []
    for j in range(128):
        pay('mesh_generation', 20)
        mesh.append((16384-j*j)*(D//16384))
    pay('mesh_domain_and_order', 600)
    require(all(0 < mesh[j] <= D for j in range(128)), 'positive mesh domain')
    require(all(mesh[j] > mesh[j+1] for j in range(127)), 'strict mesh order')

    max_nr, max_wr = F(0), F(0)
    inventory, total_newton, total_halvings = 0, 0, 0
    for n in DEGREES:
        row = {'degree': n, 'mesh_sign_evidence': [], 'positive_roots': []}
        report['rows'].append(row)
        signs = []
        for a in mesh:
            pay('mesh_evaluation_control', 12)
            _, q = ev(n, a)
            s = sign(q)
            require(s != 0, 'mesh endpoint nonzero')
            signs.append(s)
            row['mesh_sign_evidence'].append({'point': integer_record(a),
                                             'scaled_value': integer_record(q), 'sign': s})
        brackets = []
        for j in range(127):
            pay('sign_bracket_inventory', 12)
            if signs[j] != signs[j+1]:
                brackets.append((mesh[j+1], mesh[j], signs[j+1], signs[j]))
        pay('root_count_check', 20)
        require(len(brackets) == (n-1)//2, 'complete positive root count')
        for index, (lo, hi, sl, su) in enumerate(brackets):
            pay('root_initialization_and_output', 100)
            root = {'index_descending': index,
                    'initial_grid_bracket': [integer_record(lo), integer_record(hi)],
                    'initial_signs': [sl, su], 'bisections': [], 'newton': []}
            row['positive_roots'].append(root)
            depth = 14
            for _ in range(16):
                #Overhead40 covers every guard/sign test, branch, midpoint,
                #endpoint/sign update, depth counter and loop operation.
                pay('bisection_overhead', 40)
                a = (lo+hi)//2
                require((lo+hi) % 2 == 0, 'bisection midpoint exact')
                _, q = ev(n, a)
                s = sign(q)
                require(s != 0, 'bisection point nonzero')
                root['bisections'].append({'point': integer_record(a),
                                            'scaled_value': integer_record(q), 'sign': s})
                if s == sl:
                    lo, sl = a, s
                else:
                    hi, su = a, s
                depth += 1
            done = False
            for iteration in range(12):
                #90 includes loop/termination tests, image arithmetic,
                #intersection, endpoint selection and caller copies.
                pay('newton_image_and_control', 90)
                oldlo, oldhi = lo, hi
                a, p, d, dl, du, M, pm, pn = derivative(n, lo, hi, depth)
                m = F(a, D)
                u, v = m-p/dl, m-p/du
                il, iu = min(u, v), max(u, v)
                jl, ju = max(il, F(lo, D)), min(iu, F(hi, D))
                #Failure-only evidence; this does not change the numerical
                #prescription or its scalar ledger.
                report['failure_context'] = {
                    'degree': n, 'positive_root_index_descending': index,
                    'newton_update_index': iteration,
                    'old_grid_interval': [integer_record(oldlo), integer_record(oldhi)],
                    'old_depth': depth, 'point': integer_record(a),
                    'scaled_adjacent_values': [integer_record(pm), integer_record(pn)],
                    'derivative_range': interval_record(dl, du),
                    'second_derivative_bound': rational_record(M),
                    'raw_newton_image': interval_record(il, iu),
                    'intersected_image': interval_record(jl, ju)}
                lo, hi, depth, count = quantize(jl, ju, lo, hi, depth)
                del report['failure_context']
                record = {'old_grid_interval': [integer_record(oldlo), integer_record(oldhi)],
                          'point': integer_record(a),
                          'scaled_adjacent_values': [integer_record(pm), integer_record(pn)],
                          'derivative_range': interval_record(dl, du),
                          'second_derivative_bound': rational_record(M),
                          'raw_newton_image': interval_record(il, iu),
                          'intersected_image': interval_record(jl, ju),
                          'new_grid_interval': [integer_record(lo), integer_record(hi)],
                          'binary_halvings': count, 'depth': depth}
                root['newton'].append(record)
                total_newton += 1
                total_halvings += count
                if F(hi-lo, D) <= NODE_GATE:
                    final = weights(n, lo, hi, depth)
                    root['final'] = final
                    nr = F(hi-lo, 2*D)
                    wr = (decode(final['weight'][1])-decode(final['weight'][0]))/2
                    max_nr, max_wr = max(max_nr, nr), max(max_wr, wr)
                    done = True
                    break
            require(done, 'bounded Newton schedule succeeds')
            #Negative nodes and their weight intervals are explicitly output.
            pay('reflection_and_exact_output', 40)
            root['negative_node'] = interval_record(F(-hi, D), F(-lo, D))
            root['negative_weight'] = root['final']['weight'].copy()
            inventory += 2
        #Exact zero root, with its independent weight.
        pay('zero_root_and_weight', 80)
        pm, pn = ev(n, 0)
        require(pn == 0 and pm != 0, 'simple exact zero node')
        d0 = n*F(pm, DEN[n-1])
        w0 = 2/(d0*d0)
        row['zero_node'] = {'node': interval_record(0, 0),
                            'weight': interval_record(w0, w0),
                            'scaled_adjacent_values': [integer_record(pm), integer_record(pn)]}
        inventory += 1
        row['total_nodes'] = 2*len(brackets)+1
        require(row['total_nodes'] == n, 'all reflected and zero nodes output')
    pay('final_global_guards', 100)
    require(inventory == sum(DEGREES), 'total all-node inventory')
    report['summary'] = {
        'all_nodes': inventory, 'all_weights': inventory,
        'accepted_newton_updates': total_newton,
        'binary_conversion_halvings': total_halvings,
        'maximum_node_radius': rational_record(max_nr),
        'maximum_weight_radius': rational_record(max_wr),
        'node_radius_ratio_to_required': rational_record(max_nr/TOL),
        'weight_radius_ratio_to_required': rational_record(max_wr/TOL),
        'all_node_and_weight_radii_pass': max_nr <= TOL and max_wr <= TOL}


def decode_integer(a):
    return int(a['odd_hex'], 16) << a['shift']


def decode(a):
    return F(decode_integer(a['num']), decode_integer(a['den']))


try:
    main()
    report['result'] = 'PASS_ALL_NODES_WEIGHTS_AND_SETUP_CAP'
except Stop as exc:
    report['result'] = 'PRESCRIPTION_STOPPED'
    report['failures'].append(str(exc))
report['scalar_work'] = {'charged_upper': sum(ledger.values()),
                         'required_upper': CAP,
                         'headroom': CAP-sum(ledger.values()),
                         'by_category': dict(sorted(ledger.items())),
                         'model': 'exact rational scalar arithmetic; all explicit dyadic conversion steps charged; not bit complexity'}
report['guard_counts'] = dict(sorted(checks.items()))
report['script_sha256'] = sha256(HERE.read_bytes()).hexdigest()
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(report['result'])
print('Setup scalar work:', sum(ledger.values()), '; required <=', CAP,
      '; headroom', CAP-sum(ledger.values()))
if 'summary' in report:
    s = report['summary']
    print('All nodes/weights:', s['all_nodes'], '/', s['all_weights'])
    print('Radius requirements: <=2^-512 separately; all pass:', s['all_node_and_weight_radii_pass'])
    print('Newton updates:', s['accepted_newton_updates'],
          '; paid conversion halvings:', s['binary_conversion_halvings'])
print('Failures:', report['failures'])
print('Full certificate:', OUT.relative_to(HERE.parents[2]))
