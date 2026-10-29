"""Replay new evidence in L145's audited O basis; no new producer import."""
from pathlib import Path
from math import comb
import json
import hashlib
import traceback
import verify_two_adic_filter as B

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'marked-dyadic-abel-verification.json'
R = dict(completed=False, failures=[], checks=0, bindings={}, rows=[])
Q = B.Q

def ck(value, name):
    R['checks'] += 1
    assert value, name

def read(name):
    raw = (ROOT/name).read_bytes()
    R['bindings'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def main():
    C = read('marked-dyadic-abel-certificate.json')
    ck(C['completed'] and not C['failures'], 'producer completion')
    inputs = {name: read(name) for name in C['bindings']}
    ck(all(R['bindings'][n] == h for n, h in C['bindings'].items()), 'all exact input hashes')
    local = inputs['two-adic-filter-certificate.json']
    audit = inputs['two-adic-filter-audit.json']
    ck(audit['completed'] and not audit['failures'] and
       audit['bindings']['two-adic-filter-certificate.json'] ==
       R['bindings']['two-adic-filter-certificate.json'], 'accepted arithmetic audit binding')
    base = read('quartic-class-certificate.json')
    ck(local['bindings']['quartic-class-certificate.json'] ==
       R['bindings']['quartic-class-certificate.json'], 'order multiplication binding')
    B.T = base['order']['table']
    B.PO = [B.vec(row) for row in local['field']['pi_to_O']]
    B.OI = [B.vec(row) for row in local['field']['O_to_pi']]
    B.PI = B.vec([1, 0, 1, 0])
    E = B.vec(local['field']['pi_polynomial'])
    B.PIINV = B.mv(B.PO, [-E[j+1]/E[0] for j in range(4)])
    ck(B.times(B.PI, B.PIINV) == B.ONE, 'uniformizer inverse')
    B.UM = {int(k): v for k, v in local['square_table']['unit_masks'].items()}
    eta = B.mv(B.PO, B.vec(local['field']['eta_pi']))
    b0 = B.plus([Q(9075), 0, 0, 0], B.scale(eta, -1))
    M = inputs['odd-model-support-certificate.json']
    g = B.vec(M['model']['G'])
    gc = B.vec([2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025])
    # Binomial expansion, independent of producer Horner composition.
    lhs = [Q(0)]*13
    for i, coefficient in enumerate(g):
        for j in range(i+1):
            lhs[2*j] += coefficient*comb(i, j)*Q(9075)**(i-j)*Q(3025)**j
    rhs = [Q(0)]*13
    for i, coefficient in enumerate(gc): rhs[i+2] = Q(3025)**4*coefficient
    ck(lhs == rhs and [x-y for x, y in zip(lhs, rhs)] ==
       B.vec(C['map']['full_curve_identity_residual']), 'entire vertical identity')
    ck(C['map']['X'] == [9075, 0, 3025] and
       C['map']['Y_multiplier'] == [0, 3025**2], 'complete composed maps')
    c = Q(-36300)
    ck(B.vec(C['marking_character']['numerator_left']) == [-3*c*c, -12*c] ==
       [-Q(660)**2*9075, Q(660)**2] ==
       B.vec(C['marking_character']['numerator_right']), 'full marked-character identity')
    ck(B.qclass(B.ev(g, Q(0))) != 0 and
       B.ev(g, Q(0)) == Q(C['marking_character']['X_zero_curve_value']), 'no Q2 X zero point')
    B.paircheck(C['branch'], B.ev(M['model']['H'], Q(9075)), b0)
    ck(C['branch']['mask'] == 352 and C['branch']['rational']['mask'] == 0, 'branch value')
    initial = [('t', a, 3) for a in (0, 2, 4, 6)] + [
        ('t', a, 4) for a in (3, 13)] + [('q', a, 3) for a in (0, 2, 4, 6)]
    ck(C['initial_partition'] == [list(x) for x in initial], 'complete L122 source partition')
    ck([(r['chart'], r['center'], r['depth']) for r in C['disks']] == initial and
       not C.get('refinements') and not C['unresolved'], 'all ten disks closed without refinement')
    for row in C['disks']:
        chart, a, k = row['chart'], row['center'], row['depth']
        m = 2**k
        if chart == 't':
            center = B.plus(b0, [Q(3025*a*a), 0, 0, 0])
            cs = [[Q(6050*a*m), 0, 0, 0], [Q(3025*m*m), 0, 0, 0]]
            q, polynomial = Q(1), gc
        else:
            center = B.plus([Q(3025), 0, 0, 0], B.scale(b0, a*a))
            cs = [B.scale(b0, 2*a*m), B.scale(b0, m*m)]
            q, polynomial = Q(3025), list(reversed(gc))
        mask = B.paircheck(row['evaluation'], q, center)
        ck(all(B.mv(B.PO, B.vec(x)) == y for x, y in
               zip(row['difference_coefficients'], cs)), 'full field difference coefficients')
        vals = [None if not any(x) else B.normalized(x)[0] for x in cs]
        n = B.normalized(center)[0]
        lower = min(v for v in vals if v is not None)
        ck(vals == row['coefficient_valuations'] and lower == row['difference_bound'] and
           row['strict_required'] == n+8 and lower > n+8, 'strict all-point square neighborhood')
        y2 = B.ev(polynomial, Q(a))
        ck(y2 == Q(row['curve_value']) and B.qclass(y2) == 0 and y2 != 0, 'actual source realization')
        sq = row['source_square_certificate']
        ck(Q(sq['value']) == y2 and sq['valuation'] == B.v2(y2) and
           sq['mask'] == 0 and sq['unit_mod8'] == 1, 'complete source square certificate')
        R['rows'].append(dict(chart=chart, center=a, modulus=m, field_valuation=n,
            difference_bound=lower, strict_required=n+8, mask=mask,
            field_unit_residue=row['evaluation']['quartic']['unit_mod_pi9'],
            curve_value=y2, source_valuation=B.v2(y2)))
    ck(C['exceptions']['source_infinities'] == [dict(Z=z, target='odd infinity', mask=0)
                                             for z in (-55, 55)], 'both proper source infinities')
    ck(B.qclass(Q(-3)) == C['exceptions']['conic_infinity']['rational_square_mask'] != 0,
       'conic-infinity absence over Q2')
    values = sorted({row['mask'] for row in R['rows']} | {352, 0})
    generators = [r['evaluation']['mask'] for r in local['generators']]
    ambient = sorted(B.xorcombo(generators, k) for k in range(8))
    result = C['result']
    ck(values == result['marked_point_masks'] and ambient == result['jacobian_masks'], 'complete exact sets')
    ck(len(values) == result['marked_count'] == 4 and len(ambient) == result['jacobian_count'] == 8,
       'actual and comparison cardinalities')
    ck(sorted(set(ambient)-set(values)) == result['excluded_masks'] and
       set(values) < set(ambient) and result['strict'], 'strict set comparison')
    ck(values == [x for x in ambient if x & 7 == 0] == result['rational_projection_zero_masks'],
       'no refinement beyond marked rational character')
    ck(C['bounds']['disks_processed'] == 10 and C['bounds']['max_depth'] == 4, 'actual disk usage')
    R.update(completed=True, result=result, all_rows_replayed=10,
        inherited_arithmetic_checks=B.R['checks'], max_rational_bits=B.R['max_rational_bits'],
        rational_bits_cap=8192, unresolved=[])

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        R['failures'].append(dict(type=type(e).__name__, message=str(e), traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R, indent=2, default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'], checks=R['checks'],
        failures=[f['message'] for f in R['failures']], result=R.get('result'),
        bits_actual=R.get('max_rational_bits'), bits_cap=8192, certificate=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
