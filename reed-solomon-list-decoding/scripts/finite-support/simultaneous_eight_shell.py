"""Frozen L076 columns, complete joint included-anchor test.

Decimal simplex only proposes a basis. Every verdict uses exact original
mode rows, full-key presentations and a coherent direct-action check.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

from simultaneous_five_six_shell import c, beta, eigen, propose, solve
from eight_distance_full_base_kernel import enc, transition
from seven_distance_full_base_kernel import atoms, atom_orders

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'simultaneous-eight-shell-results.json'
LAYERS = [5, 6, 7, 8]
beta = lru_cache(None)(beta)
eigen = lru_cache(None)(eigen)


def eliminate(B, t):
    """Full singular PSD/range test, with a rational inverse-on-range cost."""
    H = [list(row) for row in B]
    u = list(t)
    pivots, ranges, cost = [], [], F(0)
    for k in range(len(H)):
        p = H[k][k]
        pivots.append(p)
        if p < 0:
            raise ValueError('negative old pivot')
        if p == 0:
            residual = H[k][k+1:]+[u[k]]
            ranges.append(residual)
            if any(residual):
                raise ValueError('failed singular range')
        else:
            cost += u[k]**2/p
            for i in range(k+1, len(H)):
                u[i] -= H[i][k]*u[k]/p
                for j in range(k+1, len(H)):
                    H[i][j] -= H[i][k]*H[k][j]/p
    return cost, pivots, ranges


def main():
    names = ['maximizer-excluded-anchor-results.json',
             'eight-distance-full-base-kernel-results.json',
             'eight-distance-full-base-kernel-critical-audit.json',
             'eight-distance-fixed-column-energy-results.json',
             'eight-distance-fixed-column-energy-critical-audit.json']
    paths = [ROOT/n for n in names]
    src, col, audit, energy, eaudit = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}

    def save(stage):
        out.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for name, data in zip(names, [src, col, audit, energy, eaudit]):
        check('clean_'+name, data['failures'] == [])
        for rel, digest in data.get('input_hashes', data.get('source_hashes', {})).items():
            check('hash_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(*v) for v in src['pairs_through_14']]
    check('original_positive_normalization', F(*src['rho']) > 0 and p[8] == F(16792471, 1181138102168120460) > 0)
    check('same_pairs', col['pairs_through_14'] == src['pairs_through_14'])
    base = {tuple(row['type']): F(*row['y']) for row in src['entries']}
    check('270_original_types', len(base) == 270)
    affine = col['affine']
    intercept = [F(*v) for v in affine['intercept']]
    slopes = [[F(*v) for v in row] for row in affine['slopes']]
    active = [27, 33, 56, 63]
    t = solve([slopes[j] for j in active], [-intercept[j] for j in active])
    f = [v+sum(a*b for a,b in zip(row,t)) for v,row in zip(intercept,slopes)]
    check('original_active_set', col['active_zero_indices'] == active)
    check('original_column_solution', enc(f) == col['solution'] and min(f) == 0)
    check('original_compatibility', all(sum(F(*a)*x for a,x in zip(row,f)) == F(*b)
          for row,b in zip(col['equations'],col['rhs'])))
    column = [p[8]*f[row['variable']] if row['kind']=='free' else F(*row['value']) for row in col['column']]
    check('original_complete_column', enc(column) == col['complete_column'])
    for row,y in zip(col['column'][1:],column[1:]):
        l,i,j = row['orbit']
        base[l,8,i,j] = y
    frozen = dict(base)
    dictionary = {}
    for typ,y in base.items():
        key = min(map(tuple,atom_orders(atoms(*typ))))
        check('immutable_key_'+str(typ), key not in dictionary or dictionary[key] == y)
        dictionary[key] = y
    records, free = [], []
    D = set(range(68))
    for l,m in it.combinations_with_replacement(LAYERS,2):
        U,V = set(range(m)),set(range(68,68+m))
        G = (D-U)|V
        for i,j in it.product(range(l+1),repeat=2):
            E = (D-(set(range(i))|set(range(m,m+l-i))))|(set(range(68,68+j))|set(range(68+m,68+m+l-j)))
            supports = [D,E,G]
            orders = []
            assigned, details = [], []
            for perm in it.permutations(range(3)):
                ss = [supports[k] for k in perm]
                aa = [sum(sum(bit for bit,s in zip([4,2,1],ss) if x in s)==q for x in range(1024)) for q in range(8)]
                ab,ac,bc = len(ss[0]-ss[1]),len(ss[0]-ss[2]),len(ss[1]-ss[2])
                orders.append(aa)
                y,origin = None,None
                if 0 in [ab,ac,bc]:
                    y,origin = p[max(ab,ac,bc)],'Boolean'
                elif any(1<=h<=4 for h in [ab,ac,bc]):
                    y,origin = F(0),'forbidden'
                else:
                    typ = (*sorted([ab,ac]),aa[4],aa[3])
                    if typ in frozen:
                        y,origin = frozen[typ],'immutable'
                if y is not None:
                    assigned.append(y)
                details.append({'atoms':aa,'distances':[ab,ac,bc],'origin':origin,'value':y})
            check('actual_six_atoms_'+str((l,m,i,j)),orders==atom_orders(atoms(l,m,i,j)))
            key = min(map(tuple,orders))
            if key in dictionary:
                assigned.append(dictionary[key])
            check('consistent_'+str((l,m,i,j)),len(set(assigned))<=1)
            if assigned:
                y = assigned[0]
                base[l,m,i,j] = y
                dictionary[key] = y
                check('nonnegative_'+str((l,m,i,j)),y>=0)
            else:
                y = None
                check('only_eight_eight_free_'+str((l,m,i,j)),l==m==8)
                free.append((8-i,8-j))
            records.append({'type':(l,m,i,j),'key':key,'presentations':details,'value':y})
    free.sort()
    out.update(rho=src['rho'],pairs=src['pairs_through_14'],records=records,free=free)
    save('consistency_checked')
    print('Consistency:',len(records),'types;',6*len(records),'presentations;',len(free),'free; failures:',failures,flush=True)
    if failures:
        return

    # Source symmetric beta blocks, with complete anchor transport.
    sizes = {l:c(68,l)*c(956,l) for l in LAYERS}
    modes,A,rhs = [],[],[]
    for a,b in it.product(range(9),repeat=2):
        ls = [l for l in [5,6,7] if max(a,b)<=l]
        def block(l,m):
            l,m = sorted([l,m])
            v = sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*base[l,m,i,j]
                    for i,j in it.product(range(l+1),repeat=2))
            return v-p[l]*p[m]*sizes[l]*sizes[m] if a==b==0 else v
        B = [[block(l,m) for m in ls] for l in ls]
        cross = [block(l,8) for l in ls]
        cost,pivots,ranges = eliminate(B,cross)
        D8 = c(68-2*a,8-a)*c(956-2*b,8-b)
        required = cost/(p[8]*D8)
        fixed = sum(y/p[8]*eigen(68,8,a,8-i)*eigen(956,8,b,8-j)
                    for (l,m,i,j),y in base.items() if l==m==8)
        anchor = p[8]*sizes[8] if a==b==0 else F(0)
        row = [-F(eigen(68,8,a,r)*eigen(956,8,b,q),c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        A.append(row);rhs.append(fixed-anchor-required)
        modes.append({'mode':(a,b),'layers':ls,'base':B,'cross':cross,'pivots':pivots,
                      'ranges':ranges,'D8':D8,'required':required,'fixed':fixed,'anchor':anchor})
    multiplicity = lambda a,b:(c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
    trace = p[8]**2+p[8]*sum(multiplicity(*r['mode'])*r['required'] for r in modes)/sizes[8]
    check('reviewed_L077_energy_trace', trace==F(*energy['energy']))
    for l in LAYERS:
        check('complete_dimension_'+str(l),sum(multiplicity(a,b) for a,b in it.product(range(l+1),repeat=2))==sizes[l])
    out.update(matrix=A,rhs=rhs,modes=modes,trace_energy=trace)
    save('complete_original_system_saved')
    print('Complete source system:',len(modes),'modes;',len(free),'variables; trace agrees:',trace==F(*energy['energy']),flush=True)

    # Independently construct direct subset actions and check one coherent
    # positive congruence of each whole four-layer block.
    bases,norms,gamma,sigma = {},{},{},{}
    transitions = []
    for n in [68,956]:
        for l in LAYERS:
            wt = [c(8,i)*c(n-8,l-i) for i in range(l+1)]
            hs,ns = [],[]
            for a in range(l+1):
                h = [F(i**a) for i in range(l+1)]
                for v,norm in zip(hs,ns):
                    coef = sum(w*x*y for w,x,y in zip(wt,h,v))/norm
                    h = [x-coef*y for x,y in zip(h,v)]
                norm = sum(w*x*x for w,x in zip(wt,h))
                check('positive_norm_'+str((n,l,a)),norm>0)
                hs.append(h);ns.append(norm)
            bases[n,l],norms[n,l] = hs,ns
        for l,m in it.product(LAYERS,repeat=2):
            for k in range(min(l,m)+1):
                T = [[transition(n,l,m,i,u,k) for u in range(m+1)] for i in range(l+1)]
                check('transition_row_total_'+str((n,l,m,k)),all(sum(row)==c(l,k)*c(n-l,m-k) for row in T))
                actions = []
                for a in range(m+1):
                    action = [sum(x*y for x,y in zip(row,bases[n,m][a])) for row in T]
                    if a>l:
                        check('absent_action_'+str((n,l,m,k,a)),not any(action))
                        actions.append({'degree':a,'action':action,'absent':True})
                        continue
                    coef = sum(c(8,i)*c(n-8,l-i)*x*y for i,(x,y) in enumerate(zip(action,bases[n,l][a])))/norms[n,l][a]
                    check('direct_action_'+str((n,l,m,k,a)),action==[coef*x for x in bases[n,l][a]])
                    gamma[n,l,m,a,k] = coef
                    actions.append({'degree':a,'action':action,'coefficient':coef,'absent':False})
                    be = beta(n,l,m,a,k)
                    if be:
                        ratio = norms[n,l][a]*coef/be
                        check('positive_consistent_scale_'+str((n,l,m,k,a)),ratio>0 and sigma.get((n,l,m,a),ratio)==ratio)
                        sigma[n,l,m,a] = ratio
                    else:
                        check('zero_beta_action_'+str((n,l,m,k,a)),coef==0)
                transitions.append({'indices':(n,l,m,k),'matrix':T,'complete_actions':actions})
        for a in range(9):
            ls = [l for l in LAYERS if l>=a]
            check('new_diagonal_scale_'+str((n,a)),sigma[n,8,8,a]==norms[n,8][a]/c(n-2*a,8-a))
            for l,m in it.product(ls,repeat=2):
                check('coherent_triangle_'+str((n,l,m,a)),sigma[n,l,m,a]*sigma[n,8,8,a]==sigma[n,l,8,a]*sigma[n,m,8,a])
    out.update(direct_factor_bases=[{'n':n,'layer':l,'basis':bases[n,l],'norms':norms[n,l]} for n in [68,956] for l in LAYERS],
               complete_direct_transitions=transitions,
               coherent_scales=[{'indices':k,'value':v} for k,v in sigma.items()])
    for mode in modes:
        a,b = mode['mode'];ls = mode['layers']
        def weighted(l,m):
            ybase = base if l<=m else {(mm,ll,i,j):v for (ll,mm,i,j),v in base.items()}
            v = sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*ybase[l,m,i,j]
                    for i,j in it.product(range(min(l,m)+1),repeat=2))
            if a==b==0:
                v -= p[l]*p[m]*sizes[m]
            return norms[68,l][a]*norms[956,l][b]*v
        B = [[weighted(l,m) for m in ls] for l in ls]
        t = [weighted(l,8) for l in ls]
        cost,pivots,ranges = eliminate(B,t)
        N8 = norms[68,8][a]*norms[956,8][b]
        check('direct_weighted_symmetry_'+str((a,b)),all(B[i][j]==B[j][i] for i in range(len(ls)) for j in range(len(ls))))
        check('original_weighted_cost_'+str((a,b)),cost/(p[8]*N8)==mode['required'])
        mode.update(weighted_base=B,weighted_cross=t,weighted_pivots=pivots,weighted_ranges=ranges)
    save('coherent_normalization_checked')
    print('Direct actions and coherent normalization checked; failures:',failures,flush=True)
    if failures:
        return

    discovery = propose(A,rhs)
    out['discovery'] = discovery
    save('basis_proposal_saved')
    n,m = len(free),len(modes)
    rows = [i for i in range(m) if n+i not in discovery['basis']]
    columns = sorted(j for j in discovery['basis'] if j<n)
    exact,verdict = {},'INCONCLUSIVE'
    if discovery['status']=='feasible_proposal' and -1 not in columns:
        xs = solve([[A[i][j] for j in columns] for i in rows],[rhs[i] for i in rows])
        z = [F(0)]*n
        for j,x in zip(columns,xs):
            z[j] = x
        slacks = [b-sum(a*x for a,x in zip(row,z)) for row,b in zip(A,rhs)]
        valid = min(z+slacks)>=0
        exact = {'kind':'PRIMAL','active_rows':rows,'active_columns':columns,'z':z,'slacks':slacks,'valid':valid}
        if valid:
            verdict = 'FEASIBLE'
    elif discovery['status']=='infeasible_proposal' and -1 in columns:
        M = [[F(-1) if j==-1 else A[i][j] for j in columns] for i in rows]
        ys = solve(list(map(list,zip(*M))),[F(-1) if j==-1 else F(0) for j in columns])
        y = [F(0)]*m
        for i,v in zip(rows,ys):
            y[i] = v
        sums = [sum(y[i]*A[i][j] for i in range(m)) for j in range(n)]
        fixed = sum(y[i]*rhs[i] for i in range(m))
        valid = min(y+sums)>=0 and fixed<0
        # Raw moment variable Y_j=p8*z_j/V_j: reconstruct original rows.
        raw_sums = [s*c(8,r)*c(60,r)*c(8,q)*c(948,q)/p[8] for s,(r,q) in zip(sums,free)]
        exact = {'kind':'FARKAS','active_rows':rows,'active_columns':columns,'dual':y,
                 'column_sums':sums,'raw_moment_column_sums':raw_sums,'fixed_value':fixed,'valid':valid}
        if valid:
            verdict = 'EXCLUDED'
    out.update(exact=exact,summary={'verdict':verdict,'types':len(records),'presentations':6*len(records),
               'free':len(free),'modes':len(modes),'checks':len(checks),'failures':len(failures)})
    save('completed' if verdict!='INCONCLUSIVE' else 'inconclusive_basis')
    print('Exact verdict:',verdict,'; proposal:',discovery['status'],'; valid:',exact.get('valid'),flush=True)
    if exact.get('kind')=='FARKAS':
        v=exact['fixed_value'];k=v.numerator*10**6//v.denominator
        print('Fixed separator in [',F(k,10**6),',',F(k+1,10**6),'); required >=0; positive weights:',sum(x>0 for x in y),'; zero columns:',sum(x==0 for x in sums),'/',n,flush=True)
    elif exact.get('kind')=='PRIMAL':
        print('Signs:',sum(x>=0 for x in z),'/',n,'; slacks:',sum(x>=0 for x in slacks),'/',m,'; minimum:',min(slacks),flush=True)
    print('Full certificate:',OUT.relative_to(NB),flush=True)


if __name__=='__main__':
    main()
