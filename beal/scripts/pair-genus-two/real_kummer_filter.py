"""Fixed, reviewed real-place witness test. No upstream search or replay."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
from math import prod
from pathlib import Path
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'real-kummer-certificate.json'
D = dict(completed=False, failures=[], bindings={}, checks=[], refinements=[],
         bounds=dict(candidate_cap=187, coordinate_cap=5, column_cap=192,
                     bisections_per_root_cap=64, rational_bits_cap=4096,
                     max_rational_bits=0))


def observe(x):
    if isinstance(x, (int, Q)) and not isinstance(x, bool):
        z = Q(x)
        n = max(abs(z.numerator).bit_length(), z.denominator.bit_length())
        D['bounds']['max_rational_bits'] = max(n, D['bounds']['max_rational_bits'])
        if n > 4096:
            raise ArithmeticError('4096-bit cap')
    elif isinstance(x, (list, tuple)):
        for v in x:
            observe(v)
    elif isinstance(x, dict):
        for v in x.values():
            observe(v)
    return x


def add(x, y):
    return observe(x + y)


def mul(x, y):
    return observe(x * y)


def div(x, y):
    return observe(Q(x) / Q(y))


def check(name, value):
    D['checks'].append(dict(name=name, passed=bool(value)))
    if not value:
        raise AssertionError(name)


def read(name, expected=None):
    raw = (ROOT / name).read_bytes()
    h = sha256(raw).hexdigest()
    D['bindings'][name] = h
    if expected:
        check('hash ' + name, h == expected)
    return json.loads(raw)


def ev(p, x):
    z = Q(0)
    for c in reversed(p):
        z = add(mul(z, x), c)
    return z


def interval(p, box):
    lo, hi = Q(0), Q(0)
    for c in reversed(p):
        four = [mul(t, u) for t in (lo, hi) for u in box]
        lo, hi = add(min(four), c), add(max(four), c)
    return [lo, hi]


def determinant(matrix):
    z = 0
    for perm in permutations(range(4)):
        s = (-1) ** sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        t = s
        for i in range(4):
            t = mul(t, matrix[i][perm[i]])
        z = add(z, t)
    return z


def eliminate(rows):
    pivots, records = {}, []
    for index, row in enumerate(rows):
        z, used, combination = row, [], 1 << index
        for p in sorted(pivots):
            v, w = pivots[p]
            if (z >> p) & 1:
                z ^= v
                combination ^= w
                used.append(p)
        p = (z & -z).bit_length()-1 if z else None
        if z:
            pivots[p] = (z, combination)
        records.append(dict(input=row, used=used, output=z, pivot=p,
                            combination=combination))
    return dict(rank=len(pivots), records=records,
                pivots={str(k): list(v) for k, v in sorted(pivots.items())})


def main():
    base = read('quartic-class-certificate.json', 'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b')
    parity = read('quartic-parity-certificate.json', 'fdb376f96717188690de8c849197d8b64834afdcdc56d789f427f2cf186c5501')
    loc = read('localized-parity-certificate.json', 'eb7e393e385bf994d7398ed8162d307b3f2ff2d9f593b0133cf024684ea5e76f')
    model = read('odd-model-support-certificate.json', '22315e6ebcbaa4ff063206432a958935aeb01b07ea6652bcc51d851c45162193')
    for name, cert, status in [('quartic-class', base, 'completed'),
                               ('quartic-parity', parity, 'completed'),
                               ('localized-parity', loc, 'completed'),
                               ('odd-model-support', model, 'status')]:
        audit = read(name + '-audit.json')
        check(name + ' accepted status', cert[status] == ('PASS' if status == 'status' else True)
              and cert['failures'] == [] and audit[status] == cert[status] and audit['failures'] == [])
        binding = audit['bindings'] if status == 'status' else audit['input_sha256']
        key = ('scripts/pair-genus-two/' if status == 'status' else '') + name + '-certificate.json'
        check(name + ' audit binding', binding[key] == D['bindings'][name + '-certificate.json'])
        check(name + ' all audit comparisons', all(c.get('pass', c.get('passed')) is True for c in audit['checks']))
    S = loc['selected_indices']
    check('seven S indices', S == [1,26,27,28,29,30,31])
    check('entire ordered T lattices', parity['primes'] == base['generators'])
    check('localization exact prime identities', loc['selected_primes'] == [base['generators'][i] for i in S])
    check('S corresponds to precisely permitted rational primes',
          [i for i, p in enumerate(base['generators']) if p['p'] in (2,3,5,11)] == S)
    accepted = [e for e in parity['elements'] if e['decision'] == 'accepted']
    check('entire accepted domain', len(accepted) == 182 and
          [e['tuple_id'] for e in accepted] == parity['accepted_ids'] == loc['accepted_ids'])
    check('complete accepted valuations', [e['valuations'] for e in accepted] == loc['accepted_valuations'])
    D['input_accepted_records'] = accepted
    D['input_primes'] = base['generators']
    D['S_indices'] = S
    g = model['field']['alpha_polynomial']
    B = [[Q(x) for x in row] for row in model['field']['O_basis_in_alpha']]
    check('actual polynomial', g == [-109375,-32500,150,64,1])
    check('entire transported basis', B == [[Q(x) for x in row] for row in base['order']['basis']])
    check('literal basis polynomials', B == [[1,0,Q(1,2),Q(31,30)], [0,1,Q(7,25),Q(179,750)],
                                           [0,0,Q(1,50),Q(239,18750)], [0,0,0,Q(1,18750)]])
    D['g'], D['basis'], D['G'] = g, B, model['model']['G']
    selected, excluded = [], []
    for e in accepted:
        v = e['valuations']
        check('valuation length ' + str(e['tuple_id']), len(v) == 32 and all(type(x) is int and x >= 0 for x in v))
        bad = [i for i in range(32) if i not in S and v[i] % 2]
        if bad:
            excluded.append(dict(tuple_id=e['tuple_id'], excluded_odd_indices=bad))
            continue
        coeffs = [sum(mul(B[j][i], e['coefficients'][i]) for i in range(4)) for j in range(4)]
        observe(coeffs)
        norm = determinant(e['principal'])
        norm_abs = prod(p['p'] ** t for p,t in zip(base['generators'], v))
        observe(norm_abs)
        check('signed full norm ' + str(e['tuple_id']), abs(norm) == e['norm'] == norm_abs and norm != 0)
        rational_support = {str(p): sum(v[i] for i,P in enumerate(base['generators']) if P['p'] == p)
                            for p in sorted({P['p'] for P in base['generators']})}
        check('norm even outside S ' + str(e['tuple_id']), all(t % 2 == 0 for p,t in rational_support.items() if int(p) not in (2,3,5,11)))
        selected.append(dict(id='tuple-' + str(e['tuple_id']), coefficients=e['coefficients'],
                             power_coefficients=coeffs, valuations=v, signed_norm=norm,
                             inverse_norm=div(1,norm), norm_prime_exponents=rational_support))
    for a in (-1,2,3,5,11):
        selected.append(dict(id='rational-' + str(a), coefficients=[a,0,0,0],
                             power_coefficients=[a,0,0,0], signed_norm=a**4,
                             inverse_norm=div(1,a**4), support_reason='rational with primes only in S'))
    D['excluded'], D['witnesses'] = excluded, selected
    check('fixed candidate bound', len(selected) <= 187 and len(selected)+len(excluded) == 187)
    initial = [[Q(pair[0]) for pair in row] for row in base['signature']['intervals']]
    check('initial intervals', initial == [[-48,-47],[-34,-33],[-4,-3],[20,21]])
    boxes, counts = [x[:] for x in initial], [0]*4
    D['initial_intervals'] = initial
    for k in range(4):
        lo, hi = boxes[k]
        check('initial sign change ' + str(k), ev(g,lo)*ev(g,hi) < 0)
        while True:
            ranges = [interval(e['power_coefficients'], [lo,hi]) for e in selected]
            if all(a > 0 or b < 0 for a,b in ranges):
                break
            if counts[k] >= 64:
                raise ArithmeticError('64-bisection cap at root ' + str(k))
            mid = div(add(lo,hi),2)
            value = ev(g,mid)
            record = dict(root=k, before=[lo,hi], midpoint=mid, value=value)
            D['refinements'].append(record)
            counts[k] += 1
            if value == 0:
                record['decision'] = 'unexpected rational root; invalid field hypothesis'
                raise ArithmeticError(record['decision'])
            if ev(g,lo)*value < 0:
                hi = mid
            else:
                lo = mid
            record['after'] = [lo,hi]
        boxes[k] = [lo,hi]
    D['alpha_intervals'], D['bisections'] = boxes, counts
    # eta is increasing on all four intervals, all of which lie below 50.
    eta_boxes = [[div(-907500,add(t,-50)) for t in box] for box in boxes]
    root_boxes = [[Q(9075),Q(9075)]] + eta_boxes
    check('ordered disjoint actual G roots', all(box[1] < 50 for box in boxes) and
          all(root_boxes[i][1] < root_boxes[i+1][0] for i in range(4)))
    D['eta_intervals'], D['root_intervals'] = eta_boxes, root_boxes
    D['coordinate_order'] = ['rational-9075','alpha-0','alpha-1','alpha-2','alpha-3']
    for e in selected:
        ranges = [interval(e['power_coefficients'], box) for box in boxes]
        bits = [int(e['signed_norm'] < 0)] + [int(hi < 0) for lo,hi in ranges]
        check('strict signs and norm parity ' + e['id'], all(lo > 0 or hi < 0 for lo,hi in ranges)
              and sum(bits) % 2 == 0)
        e.update(alpha_value_intervals=ranges, sign_bits=bits,
                 mask=sum(b << i for i,b in enumerate(bits)))
    samples = [add(root_boxes[0][0],-1)]
    samples += [div(add(root_boxes[i][1],root_boxes[i+1][0]),2) for i in range(4)]
    samples += [add(root_boxes[-1][1],1)]
    local, gaps = [], []
    for j,x in enumerate(samples):
        value = ev(D['G'],x)
        bits = [int(j <= k) for k in range(5)]
        mask = sum(b << i for i,b in enumerate(bits))
        check('gap sign and nonbranch ' + str(j), value != 0 and (value < 0) == bool(sum(bits) % 2))
        gaps.append(dict(gap=j, sample=x, G_value=value, real_point=value>0, sign_bits=bits, mask=mask))
        if value > 0:
            local.append(mask)
    D['gaps'], D['infinity_mask'] = gaps, 0
    D['local_rows'] = local + [0]
    D['local_elimination'] = eliminate(D['local_rows'])
    check('Stoll complete real image dimension', D['local_elimination']['rank'] == 5-1-2)
    rows = D['local_rows'] + [e['mask'] for e in selected]
    check('matrix dimensions', len(rows) <= 192 and all(0 <= r < 32 for r in rows))
    D['combined_elimination'] = eliminate(rows)
    codim = D['combined_elimination']['rank'] - D['local_elimination']['rank']
    check('codimension within real norm kernel quotient', 0 <= codim <= 2)
    D['result'] = dict(accepted=182, retained_box=len(selected)-5, rejected_box=len(excluded),
                       rational_appended=5, witnesses=len(selected), coordinates=5,
                       matrix_columns=len(rows), local_rank=D['local_elimination']['rank'],
                       combined_rank=D['combined_elimination']['rank'], quotient_rank=codim,
                       ambient_dimension_constant=11, filtered_dimension_constant=11-codim,
                       class_contribution_upper_bound=2, rank_bound_constant=10-codim,
                       unconditional_rank_upper_bound=12-codim, required_rank_upper_bound=1)
    observe(D)
    D['completed'] = True


try:
    main()
except Exception as exc:
    D['failures'].append(dict(error=str(exc), traceback=traceback.format_exc()))
finally:
    OUT.write_text(json.dumps(D, default=str, indent=2) + '\n')
    print(json.dumps(dict(completed=D['completed'], result=D.get('result'),
                          bounds=D['bounds'], bisections=D.get('bisections'),
                          failures=D['failures'], certificate=str(OUT))))
if not D['completed']:
    raise SystemExit(1)
