"""Fixed positive-only K-conic experiment; finite failure proves no insolubility.

Decimal interpolation proposes roots. Only exact QQ[alpha]/A substitution
accepts; a positive output still needs independent maximal-order replay.
No existing producer, ledger or certificate is modified.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'rational-branch-positive-search-certificate.json'
A = [-109375, -32500, 150, 64, 1]
B = [[Q(1), Q(0), Q(1, 2), Q(31, 30)],
     [Q(0), Q(1), Q(7, 25), Q(179, 750)],
     [Q(0), Q(0), Q(1, 50), Q(239, 18750)],
     [Q(0), Q(0), Q(0), Q(1, 18750)]]
ONE = list(map(Q, [1, 0, 0, 0]))
DENOMS = [1, 2, 3, 5, 6, 10, 15, 30]
BOXES = [(-48, -47), (-34, -33), (-4, -3), (20, 21)]
SIGNS = list(product([-1, 1], repeat=4))
R = dict(completed=False, outcome='unfinished', failures=[], bindings={},
         checks=0, mask=132102, trials=[], accepted_point=None,
         bounds=dict(tuples_actual=0, tuples_cap=5000, zero_tuples=0,
                     v_actual=0, sign_proposals_actual=0,
                     sign_proposals_cap=80000, per_v_sign_cap=16,
                     precision=200, root_refinements_actual=0,
                     root_refinements_cap_per_root=450,
                     denominator_cap=10**12, rational_bits_actual=0,
                     rational_bits_cap=8192))


def ck(ok, name):
    R['checks'] += 1
    if not ok:
        raise AssertionError(name)


def obs(x):
    if isinstance(x, (list, tuple)):
        for a in x:
            obs(a)
    elif isinstance(x, (int, Q)):
        x = Q(x)
        bits = max(abs(x.numerator).bit_length(), x.denominator.bit_length())
        R['bounds']['rational_bits_actual'] = max(
            bits, R['bounds']['rational_bits_actual'])
        ck(bits <= 8192, 'rational bit cap')
    return x


def read(name):
    raw = (ROOT / name).read_bytes()
    R['bindings'][name] = sha256(raw).hexdigest()
    return json.loads(raw)


def bind_saved(c, single_helper):
    # Full JSON and implementation inputs, not merely saved success flags.
    for name, h in c.get('bindings', {}).items():
        ck(sha256((ROOT / name).read_bytes()).hexdigest() == h,
           'source binding ' + name)
        R['bindings'][name] = h
    helpers = c.get('helper_sha256', {})
    # The two dyadic producers store the sole two_adic_filter.py hash as
    # a string; the other two producers store filename-to-hash dictionaries.
    if isinstance(helpers, str):
        helpers = {single_helper: helpers}
    for name, h in helpers.items():
        ck(sha256((ROOT / name).read_bytes()).hexdigest() == h,
           'helper binding ' + name)
        R['bindings'][name] = h


def mul(a, b):
    z = [Q(0)] * 7
    for i in range(4):
        for j in range(4):
            z[i+j] += a[i] * b[j]
    for k in range(6, 3, -1):
        for j in range(4):
            z[k-4+j] -= z[k] * A[j]
    return obs(z[:4])


def solve(m, b):
    z = [list(row) + [v] for row, v in zip(m, b)]
    for j in range(4):
        k = next(k for k in range(j, 4) if z[k][j])
        z[k], z[j] = z[j], z[k]
        t = z[j][j]
        z[j] = [v / t for v in z[j]]
        for k in range(4):
            if k != j:
                t = z[k][j]
                z[k] = [v - t*w for v, w in zip(z[k], z[j])]
    return [row[-1] for row in z]


def inv(a):
    cols = [mul(a, [Q(i == j) for i in range(4)]) for j in range(4)]
    ans = obs(solve([[cols[j][i] for j in range(4)] for i in range(4)], ONE))
    ck(mul(ans, a) == ONE, 'exact field inverse')
    return ans


def powercoords(v):
    return obs([sum(B[i][j] * Q(v[j]) for j in range(4)) for i in range(4)])


def ev(p, x):
    v = x * 0
    for c in reversed(p):
        v = v*x + c
    return v


def dec(x):
    x = Q(x)
    return D(x.numerator) / D(x.denominator)


def main():
    # Authenticate the exact old conic families and their accepted replays.
    families = ['shukla-good-conics', 'shukla-dyadic-conics',
                'shukla-quartic-pair-conics', 'shukla-odd-pair-conics']
    certs = {}
    for stem in families:
        name = stem + '-certificate.json'
        c = read(name)
        v = read(stem + '-verification.json')
        ck(c['completed'] and not c['failures'], 'completed source ' + stem)
        ck(v['completed'] and not v['failures'], 'accepted replay ' + stem)
        ck(v['bindings'][name] == R['bindings'][name], 'replay binds ' + stem)
        producer = stem.replace('-', '_') + '.py'
        ck(c['source_sha256'] == sha256((ROOT / producer).read_bytes()).hexdigest(),
           'producer binding ' + stem)
        R['bindings'][producer] = c['source_sha256']
        bind_saved(c, 'two_adic_filter.py')
        bind_saved(v, 'verify_two_adic_filter.py')
        certs[stem] = c
    model = read('odd-model-support-certificate.json')
    columns = read('two-adic-filter-certificate.json')['witnesses']
    saved = read('odd-membership-35-certificate.json')
    ck(model['field']['alpha_polynomial'] == A, 'actual K')
    ck([[Q(v) for v in row] for row in model['field']['O_basis_in_alpha']] == B,
       'actual maximal-order basis')
    ck(len(columns) == 39, 'complete ordered column domain')
    q, b = Q(1), ONE[:]
    for j, w in enumerate(columns):
        ck(w['source'] == saved['places']['3']['witnesses'][j]['source'] ==
           saved['places']['5']['witnesses'][j]['source'], 'full source order')
        if 132102 >> j & 1:
            q = obs(q * Q(w['source']['inverse_norm']))
            b = mul(b, powercoords(w['source']['coefficients']))
    ck(q == Q(1, 26730000000000), 'full q')
    ck(b == list(map(Q, [41236, Q(356216, 25), Q(397568, 625), Q(4612, 625)])),
       'full b')
    ref = saved['selected_pair'][1]
    ck(ref['coefficients'] == 132102 and Q(ref['rational']) == q and
       powercoords(ref['quartic_O']) == b, 'whole selected representative')
    eta = list(map(Q, model['field']['eta_in_alpha']))
    ck(mul(eta, list(map(Q, [-50, 1, 0, 0]))) == [-907500, 0, 0, 0],
       'actual root map')
    old = certs['shukla-good-conics']['classes'][0]
    ck(old['mask'] == 132102 and Q(old['rational']) == q and
       list(map(Q, old['quartic_power'])) == b and
       list(map(Q, old['row']['second_root_power'])) == eta,
       'full original conic identity')
    g = [Q(9075) - eta[0]] + [-x for x in eta[1:]]
    ib = inv(b)
    c = mul(g, ib)
    a = obs([q*x for x in ib])
    ck(a == list(map(Q, old['row']['quaternion_a_power'])) and
       c == list(map(Q, old['row']['quaternion_c_power'])), 'saved target coefficients')
    R.update(alpha_polynomial=A, order_basis=B, rational=q, quartic_power=b,
             eta_power=eta, square_constant=c, square_v2_coefficient=a,
             domain=dict(denominators=DENOMS, coefficients=[-2, -1, 0, 1, 2],
                         order='denominator then lexicographic a0,a1,a2,a3',
                         signs=SIGNS, zero_omitted=True, deduplicated=False))
    with localcontext() as ctx:
        ctx.prec = 200
        roots = []
        root_boxes = []
        for lo, hi in BOXES:
            lo, hi = D(lo), D(hi)
            ck(ev(A, lo)*ev(A, hi) < 0, 'initial proposal bracket')
            for _ in range(450):
                mid = (lo + hi)/2
                if ev(A, lo)*ev(A, mid) < 0:
                    hi = mid
                else:
                    lo = mid
                R['bounds']['root_refinements_actual'] += 1
            roots.append((lo + hi)/2)
            root_boxes.append([str(lo), str(hi)])
        R['proposal_root_boxes'] = root_boxes
        R['proposal_roots'] = list(map(str, roots))
        matrix = [[r**j for j in range(4)] for r in roots]
        # Cache interpolation, with the same fixed precision as all proposals.
        invcols = [solve(matrix, [D(i == j) for i in range(4)]) for j in range(4)]
        for d in DENOMS:
            for coeff in product(range(-2, 3), repeat=4):
                R['bounds']['tuples_actual'] += 1
                ck(R['bounds']['tuples_actual'] <= 5000, 'tuple cap')
                if not any(coeff):
                    R['bounds']['zero_tuples'] += 1
                    continue
                v = powercoords([Q(x, d) for x in coeff])
                v2 = mul(v, v)
                target = obs([x + y for x, y in zip(mul(a, v2), c)])
                rec = dict(denominator=d, order_numerators=coeff, v_power=v,
                           target_power=target, proposals=[])
                R['trials'].append(rec)
                R['bounds']['v_actual'] += 1
                vals = [ev(list(map(dec, target)), r) for r in roots]
                if min(vals) < 0:
                    rec.update(status='unresolved_negative_approximation',
                               approximate_values=list(map(str, vals)))
                    continue
                vals = [x.sqrt() for x in vals]
                for signs in SIGNS:
                    R['bounds']['sign_proposals_actual'] += 1
                    ck(R['bounds']['sign_proposals_actual'] <= 80000, 'sign cap')
                    approx = [sum(invcols[j][i]*vals[j]*signs[j] for j in range(4))
                              for i in range(4)]
                    u = obs([Q(x).limit_denominator(10**12) for x in approx])
                    square = mul(u, u)
                    diff = obs([x-y for x, y in zip(square, target)])
                    rec['proposals'].append(dict(u_power=u, square_remainder=diff))
                    if diff == [0]*4 and any(u):
                        residual = obs([x-q*y+z-Q(9075)*(i == 0)
                                        for i, (x, y, z) in enumerate(zip(
                                            mul(b, square), v2, eta))])
                        ck(any(v) and residual == [0]*4, 'exact nonzero conic substitution')
                        rec['status'] = 'exact_point_pending_independent_replay'
                        R.update(completed=True, outcome='positive_pending_replay',
                                 accepted_point=dict(u_power=u, v_power=v,
                                                     conic_remainder=residual,
                                                     trial_index=len(R['trials'])-1,
                                                     signs=signs))
                        return
                rec['status'] = 'unresolved_no_exact_reconstructed_root'
    ck(R['bounds']['tuples_actual'] == 5000 and R['bounds']['v_actual'] == 4992,
       'whole prescribed finite domain visited')
    R.update(completed=True, outcome='fixed_domain_exhausted_no_point',
             limitation='No nonsquare or conic-insolubility conclusion; park this fixed experiment.')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        R['failures'].append(dict(message=str(e), traceback=traceback.format_exc()))
        R['outcome'] = 'unresolved_execution_failure'
    R['source_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(R, indent=2, default=str) + '\n')
    print(json.dumps(dict(completed=R['completed'], outcome=R['outcome'],
                          bounds=R['bounds'], checks=R['checks'],
                          failures=[x['message'] for x in R['failures']],
                          path=str(OUT))))
