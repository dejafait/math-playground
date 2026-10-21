"""Bounded L065/L064 witness search; no negative uniformity claim.

Store every representative and all projected row residuals, plus every
tested compatible pair. All 95 scalars are retained on both-zero rows.
An independent full replay is required before a uniform finite conclusion.
"""
from itertools import combinations, permutations
from pathlib import Path
import json

MOD = 97
H = tuple(x for x in range(1, MOD) if pow(x, 16, MOD) == 1)
INV = {x: pow(x, -1, MOD) for x in range(1, MOD)}
LIMIT = 8000


def prod(values):
    out = 1
    for x in values:
        out = out*x % MOD
    return out


def inv(x):
    return INV[x % MOD]


def pairings(nodes):
    if not nodes:
        yield ()
        return
    a = nodes[0]
    for i in range(1, len(nodes)):
        for tail in pairings(nodes[1:i]+nodes[i+1:]):
            yield ((a, nodes[i]),)+tail


def canonical(pairs):
    return tuple(sorted(tuple(sorted(pair)) for pair in pairs))


def determinant3(rows):
    a,b,c = rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0])) % MOD


def lagrange(x, nodes, t):
    return prod((t-u)*inv(x-u) for u in nodes if u != x)


def beta(K, P, pair, cx):
    return [-sum(cx[t]*t*prod(t-k for k in K)*lagrange(x,P,t)
                 for t in pair)*inv(x*prod(x-k for k in K)) % MOD
            for x in P]


def weight_rows(K, P, Y, Z, cx):
    by,bz = beta(K,P,Y,cx), beta(K,P,Z,cx)
    u = [v*inv(cx[x]) % MOD for x,v in zip(P,by)]
    v = [v*inv(cx[x]) % MOD for x,v in zip(P,bz)]
    rows = []
    for mu in range(1,96):
        w = ((1-v[0]+mu*u[0])*inv(1+mu) % MOD,
             (u[1]-v[1]*inv(mu)) % MOD, (v[2]-mu*u[2]) % MOD)
        rows.append({'mu':mu,'weights':w,'gated':all(x not in (0,1) for x in w)})
    return {'beta_Y':by,'beta_Z':bz,'u':u,'v':v,'rows':rows}


def numerator(P,Y,Z,cx,w,mu):
    p,q,r = w
    out = {x:-mu*cx[x] % MOD for x in Y}
    out.update({x:cx[x] for x in Z})
    out.update({P[0]:cx[P[0]]*(1-(1+mu)*p) % MOD,
                P[1]:-mu*cx[P[1]]*q % MOD, P[2]:cx[P[2]]*r % MOD})
    return out


def recover(K, coeff):
    omega = [inv(x)*sum(c*t*lagrange(x,K,t) for t,c in coeff.items()) % MOD
             for x in K]
    residual = [(sum(c*pow(x,j,MOD) for x,c in zip(K,omega))
                 - sum(c*pow(x,j,MOD) for x,c in coeff.items())) % MOD
                for j in range(1,9)]
    assert not any(residual)
    return omega,residual


def run():
    # Every scaling orbit has a representative containing 1. This is only
    # search economy: no negative completeness conclusion is used.
    projected_records, pair_tests, coverage = [], [], []
    counts = {'representatives':0,'independent':0,'projected_rows':0,
              'projected_survivors':0,'support_pairs':0,'role_tests':0,
              'scalar_rows':0,'compatible':0,'full_pairs':0}
    witness = None
    quartic_values = {K:{x:prod(x-k for k in K) for x in H}
                      for K in combinations(H,4)}
    for rest in combinations(H[1:],5):
        S = (1,)+rest
        complement = tuple(x for x in H if x not in S)
        ds = {x:inv(prod(x-t for t in S if t != x)) for x in S}
        for pairs in pairings(S):
            key = canonical(pairs)
            if key != min(canonical(tuple(tuple(h*x % MOD for x in pair)
                                                for pair in pairs)) for h in H):
                continue
            if counts['representatives'] >= LIMIT:
                break
            counts['representatives'] += 1
            quadratics = [(a*b % MOD, -(a+b) % MOD, 1) for a,b in key]
            det = determinant3(quadratics)
            cover = {'pairs':key,'quadratic_det':det,'projected_residuals':[]}
            coverage.append(cover)
            if not det:
                continue
            counts['independent'] += 1
            candidates = []
            for K in combinations(complement,4):
                counts['projected_rows'] += 1
                vals = quartic_values[K]
                sums = [sum(vals[x]*ds[x] for x in pair) % MOD for pair in key]
                cover['projected_residuals'].append(sums)
                if not any(sums):
                    candidates.append(K)
                    counts['projected_survivors'] += 1
            if candidates:
                projected_records.append({'pairs':key,'quadratic_det':det,
                                          'candidates':candidates})
            for K,L in combinations(candidates,2):
                union = set(K+L)
                if len(union) != 7:
                    continue
                counts['support_pairs'] += 1
                shared = tuple(x for x in complement if x not in union)
                assert len(shared)==3
                cx = {x:prod(x-h for h in union) for x in S+shared}
                for Y,Z,W in permutations(key):
                    for P in permutations(shared):
                        counts['role_tests'] += 1
                        left,right = (weight_rows(supp,P,Y,Z,cx) for supp in (K,L))
                        counts['scalar_rows'] += 190
                        by_weight = {tuple(row['weights']):row['mu'] for row in right['rows']
                                     if row['gated']}
                        # mu -> w is injective here because u_c != 0 by
                        # L064 (4): K and L contain no singleton pairs.
                        assert len(by_weight)==sum(r['gated'] for r in right['rows'])
                        successes = []
                        for row in left['rows']:
                            mu,w = row['mu'],tuple(row['weights'])
                            nu = by_weight.get(w)
                            if not row['gated'] or nu is None or mu==nu:
                                continue
                            counts['compatible'] += 1
                            omegaK,resK = recover(K,numerator(P,Y,Z,cx,w,mu))
                            omegaL,resL = recover(L,numerator(P,Y,Z,cx,w,nu))
                            result = {'weights':w,'mu':mu,'nu':nu,'omega_K':omegaK,
                                      'omega_L':omegaL,'residual_K':resK,'residual_L':resL,
                                      'full':all(omegaK) and all(omegaL)}
                            successes.append(result)
                            if result['full']:
                                counts['full_pairs'] += 1
                                rho = next(rho for rho in range(2,97)
                                           if all((rho-(1-rho)*m) % MOD for m in (mu,nu)))
                                witness = {'P':P,'Y':Y,'Z':Z,'W':W,'K':K,'L':L,
                                           'CX':cx,'quadratic_det':det,'gamma':[0,1,rho],
                                           'lambda':1, **result}
                                break
                        pair_tests.append({'P':P,'Y':Y,'Z':Z,'W':W,'K':K,'L':L,
                                           'left':left,'right':right,'compatible':successes})
                        if witness:
                            break
                    if witness:
                        break
                if witness:
                    break
            if witness:
                break
        if witness or counts['representatives']>=LIMIT:
            break
    result = {'scope':'Bounded witness search; rejected rows do not certify uniform nonattainment',
              'H':H,'representative_limit':LIMIT,'eligible_scalars_per_row_required':95,
              'counts':counts,'projected_records':projected_records,'pair_tests':pair_tests,
              'coverage':coverage,'witness':witness,'failures':[]}
    path = Path(__file__).with_name('independent-net-pair.json')
    path.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({'counts':counts,'representative_limit':LIMIT,
                      'witness_found':witness is not None,'full_pairs_required':1,
                      'failures_actual':0,'failures_required':0,'path':str(path)},sort_keys=True))


if __name__=='__main__':
    run()
