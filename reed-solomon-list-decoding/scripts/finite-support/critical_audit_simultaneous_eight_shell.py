"""L078 dedicated audit: actual subsets, coherent congruence, manuscript dual.

Standard library only; run verify_simultaneous_eight_shell.py first.
No optimizer or notebook imports. Full exact evidence is written to disk.
"""
import hashlib
import itertools as it
import json
import re
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'simultaneous-eight-shell-critical-audit.json'
LS = [5, 6, 7, 8]


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a, b in zip(x, y)), F(0))


def solve(M, b):
    """Reverse variable order, forward elimination and back substitution."""
    n = len(b)
    assert len(M) == n and all(len(row) == n for row in M)
    a = [list(map(F, reversed(row)))+[F(r)] for row, r in zip(M, b)]
    pivots = []
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j])
        a[k], a[j] = a[j], a[k]
        p = a[j][j]
        pivots.append(p)
        for k in range(j+1, n):
            t = a[k][j]/p
            a[k] = [x-t*y for x, y in zip(a[k], a[j])]
    x = [F(0)]*n
    for j in reversed(range(n)):
        x[j] = (a[j][-1]-dot(a[j][j+1:n], x[j+1:]))/a[j][j]
    x.reverse()
    assert all(dot(row, x) == r for row, r in zip(M, b))
    return x, pivots


@lru_cache(None)
def beta(n, l, m, a, k):
    return sum((-1)**(t-k)*c(t,k)*c(n-2*a,t-a)*c(n-a-t,l-t)*c(n-a-t,m-t)
               for t in range(max(a,k),min(l,m,n-a)+1))


def eigen(n, a, r):
    return sum((-1)**s*c(a,s)*c(8-a,r-s)*c(n-8-a,r-s) for s in range(r+1))


@lru_cache(None)
def subset_histogram(l, i):
    """Enumerate actual subsets of U union X, with U of size eight."""
    U = set(range(8))
    X = set(range(i)) | set(range(8, 8+l-i))
    union = sorted(U | X)
    counts = Counter()
    for bits in range(1 << len(union)):
        Z = {x for j, x in enumerate(union) if bits >> j & 1}
        counts[len(Z & U), len(Z & X), len(Z)] += 1
    return len(union), counts


def main():
    names = ['simultaneous-eight-shell-results.json', 'simultaneous-eight-shell-verification.json',
             'maximizer-excluded-anchor-results.json', 'maximizer-completion-results.json',
             'maximizer-completion-verification.json', 'delsarte-lp-results.json',
             'seven-distance-full-base-kernel-results.json', 'alternative-product-zero-plane-results.json',
             'seven-shell-affine-fixed-dual-results.json', 'simultaneous-shell-ordinary-scalars-results.json',
             'eight-distance-full-base-kernel-results.json', 'eight-distance-fixed-column-energy-results.json']
    paths = [ROOT/name for name in names]
    data, ver, src, inc, iv, lp, seven, plane, square, old, col, energy = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    for name, obj in zip(names, [data, ver, src, inc, iv, lp, seven, plane, square, old, col, energy]):
        check('clean_'+name, not obj['failures'])
    for obj in [data, ver, src, inc, iv, col, energy]:
        for rel, digest in obj.get('input_hashes',obj.get('source_hashes',{})).items():
            check('binding_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    primal = [F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    check('pair_domain', len(primal) == 64 and lp['active_distances'] == list(range(5,69)))
    for j in range(1,65):
        row = [F(sum((-1)**h*c(j,h)*c(68-j,i-h)*c(956-j,i-h) for h in range(i+1)),c(68,i)*c(956,i)) for i in range(5,69)]
        check('original_pair_equation_'+str(j), dot(row,primal) == -1)
    p = [F(1)]+[F(0)]*4+[a/(2*c(68,h)*c(956,h)) for h,a in zip(range(5,69),primal)]
    rho = (F(c(1024,64),c(68,64))+1)/(2*c(1024,68))
    check('original_rho_pairs', rho > 0 and enc(rho) == src['rho'] == data['rho']
          and enc(p[:15]) == src['pairs_through_14'] == data['pairs']
          and p[8] == F(16792471,1181138102168120460))
    M = [[F(*v) for v in row] for row in square['objective_matrix']]
    N = [[F(*v) for v in row] for row in plane['plane_matrix']]
    params = [F(0),-N[0][2]/N[2][2],-M[0][3]/M[3][3]]
    f = [F(0)]*49
    f[27],f[33],f[42] = params
    check('maximizer_parameters', enc(params) == inc['parameters'] and M[3][3] < 0 and N[2][2] < 0)
    rr = [[F(*v) for v in row] for row in seven['equation_rref']]
    check('RREF_free_indices', [j for j in range(49) if j not in seven['equation_pivots']] == [27,33,42])
    for k,j in enumerate(seven['equation_pivots']):
        f[j] = rr[k][-1]-sum(rr[k][t]*f[t] for t in [27,33,42])
    check('original_49_column', enc(f) == inc['free_column'] and min(f) >= 0)
    for i,(row,b) in enumerate(zip(seven['equations'],seven['rhs'])):
        check('original_seven_equation_'+str(i), dot([F(*v) for v in row],f) == F(*b))
    entries = {tuple(r['type']):F(*r['y']) for r in old['types']}
    for row in seven['column']:
        l,i,j = row['orbit']
        if l:
            entries[l,7,i,j] = p[7]*f[row['variable']] if row['kind']=='free' else F(*row['value'])
    # Import the audited L073 original system, independently resolve its compact definition.
    defining = [0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,24,25,26,27,28,29,32,33,34,35,40,41,42,48,49,56]
    AA = [[F(*x) for x in row] for row in inc['matrix']]
    bb = [F(*x) for x in inc['rhs']]
    z7, piv7 = solve([AA[i] for i in defining]+[[F(j==28) for j in range(36)]], [bb[i] for i in defining]+[F(0)])
    check('original_36_completion', enc(z7) == inc['certificate']['z'] == iv['fresh_original_basis_solution'] and min(z7) == 0)
    free7 = [(r,q) for r,q in it.product(range(8),repeat=2) if r+q>=7]
    for r,q in it.product(range(8),repeat=2):
        h = r+q
        y = p[7] if h==0 else F(0) if h<=4 else entries[h,7,q,r] if h<=6 else p[7]*z7[free7.index((r,q))]/(c(7,r)*c(61,r)*c(7,q)*c(949,q))
        entries[7,7,7-r,7-q] = y
    source = {tuple(r['type']):F(*r['y']) for r in src['entries']}
    check('all_270_immutable_values', entries == source and len(entries) == 270)
    ci = [F(*v) for v in col['affine']['intercept']]
    cs = [[F(*v) for v in row] for row in col['affine']['slopes']]
    active = [27,33,56,63]
    t,piv8 = solve([cs[i] for i in active],[-ci[i] for i in active])
    f8 = [a+dot(row,t) for a,row in zip(ci,cs)]
    check('eight_active_set', col['active_zero_indices']==active and enc(f8)==col['solution'] and [i for i,x in enumerate(f8) if x==0]==active and min(f8)==0)
    column = [p[8]*f8[r['variable']] if r['kind']=='free' else F(*r['value']) for r in col['column']]
    check('eight_column', enc(column)==col['complete_column'] and column[0]==p[8])
    W = [1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in col['orbits'][1:]]
    kres = [dot([F(*x)*w for x,w in zip(row,W)],column) for row in col['kernel_basis']]
    check('all_90_original_weighted_residuals', len(kres)==90 and not any(kres))
    for row,y in zip(col['column'][1:],column[1:]):
        entries[(*row['orbit'][:1],8,*row['orbit'][1:])] = y
    # Consume every original presentation and independently permute its eight atoms.
    records, key_values, freekeys, sourcekeys = [], {}, {}, {}
    for saved, independently in zip(data['records'],ver['records']):
        typ = tuple(saved['type']); l,m,i,j = typ
        atoms = [956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        orders=[]
        for order in it.permutations(range(3)):
            aa=[0]*8
            for bit,size in enumerate(atoms):
                oldbits=[(bit>>t)&1 for t in [2,1,0]]
                newbit=sum(oldbits[order[k]] << (2-k) for k in range(3))
                aa[newbit]=size
            orders.append(aa)
        key=tuple(min(orders))
        check('all_six_atoms_'+str(typ), orders==[v['atoms'] for v in saved['presentations']])
        check('source_equality_class_'+str(typ), sourcekeys.setdefault((tuple(sorted([l,m,l+m-i-j])),i-j),key)==key)
        y = None if saved['value'] is None else F(*saved['value'])
        check('independent_record_'+str(typ), saved['key']==independently['key']==list(key) and saved['value']==independently['value'])
        check('unique_union_value_'+str(typ), key_values.setdefault(key,y)==y)
        if typ in entries:
            check('immutable_'+str(typ), y==entries[typ])
        if y is None:
            freekeys[typ]=key
        else:
            entries[typ]=y
        records.append({'type':typ,'key':key,'orders':orders,'value':y})
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    check('full_domain',len(records)==500 and len(freekeys)==len(set(freekeys.values()))==45
          and sorted((8-i,8-j) for l,m,i,j in freekeys)==free)
    for r,q in it.product(range(9),repeat=2):
        if r+q<=7:
            y=p[8] if r+q==0 else F(0) if r+q<=4 else entries[r+q,8,q,r]
            check('forced_eight_'+str((r,q)),entries[8,8,8-r,8-q]==y)
    report.update(parameters=params,original_RREF_column=f,completion=z7,completion_pivots=piv7,
                  eight_parameters=t,eight_active_pivots=piv8,column=column,kernel_residuals=kres,records=records)
    save('immutable_dictionary_checked')
    print('Immutable dictionary and all 3000 atom permutations checked; failures:',failures,flush=True)

    # Monic bases via moment equations, independently of Gram-Schmidt.
    bases,norms,gamma,sigma={},{},{},{}
    factors,transitions=[],[]
    saved_factors={(r['n'],r['layer']):r for r in data['direct_factor_bases']}
    for n,l in it.product([68,956],LS):
        weights=[c(8,i)*c(n-8,l-i) for i in range(l+1)]
        moments=[sum(w*i**d for i,w in enumerate(weights)) for d in range(2*l+1)]
        hs,ns=[],[]
        for a in range(l+1):
            coeff=[] if a==0 else solve([[F(moments[t+s]) for s in range(a)] for t in range(a)],[-F(moments[t+a]) for t in range(a)])[0]
            values=[F(i**a)+sum(x*i**s for s,x in enumerate(coeff)) for i in range(l+1)]
            norm=dot(weights,[x*x for x in values])
            check('orthogonal_norm_'+str((n,l,a)),norm>0 and all(dot(weights,[x*i**t for i,x in enumerate(values)])==0 for t in range(a)))
            hs.append(values); ns.append(norm)
        bases[n,l],norms[n,l]=hs,ns
        check('saved_factor_'+str((n,l)),enc(hs)==saved_factors[n,l]['basis'] and enc(ns)==saved_factors[n,l]['norms'])
        factors.append({'n':n,'layer':l,'weights':weights,'basis':hs,'norms':ns})
    saved_trans={tuple(r['indices']):r for r in data['complete_direct_transitions']}
    for n,l,m in it.product([68,956],LS,LS):
        for k in range(min(l,m)+1):
            T=[]
            for i in range(l+1):
                size,hist=subset_histogram(l,i)
                row=[sum(v*c(n-size,m-s) for (u0,k0,s),v in hist.items() if u0==u and k0==k) for u in range(m+1)]
                check('actual_subset_total_'+str((n,l,m,k,i)),sum(row)==c(l,k)*c(n-l,m-k))
                T.append(row)
            saved=saved_trans[n,l,m,k]
            check('entire_transition_'+str((n,l,m,k)),T==saved['matrix'])
            actions=[]
            for a in range(m+1):
                action=[dot(row,bases[n,m][a]) for row in T]
                check('saved_action_'+str((n,l,m,k,a)),enc(action)==saved['complete_actions'][a]['action'])
                if a>l:
                    check('absent_action_'+str((n,l,m,k,a)),not any(action))
                    actions.append({'degree':a,'action':action,'absent':True})
                    continue
                # Evaluate at a nonzero basis coordinate; no projected coefficient is assumed.
                j=next(i for i,x in enumerate(bases[n,l][a]) if x)
                g=action[j]/bases[n,l][a][j]
                check('all_action_coordinates_'+str((n,l,m,k,a)),action==[g*x for x in bases[n,l][a]])
                gamma[n,l,m,a,k]=g
                be=beta(n,l,m,a,k)
                if be:
                    ratio=norms[n,l][a]*g/be
                    check('signed_scale_'+str((n,l,m,k,a)),ratio>0 and sigma.setdefault((n,l,m,a),ratio)==ratio)
                else:
                    check('zero_beta_'+str((n,l,m,k,a)),g==0)
                actions.append({'degree':a,'action':action,'coefficient':g,'absent':False})
            transitions.append({'indices':(n,l,m,k),'matrix':T,'actions':actions})
    for n in [68,956]:
        for a in range(9):
            ls=[l for l in LS if l>=a]
            check('diagonal_scale_'+str((n,a)),sigma[n,8,8,a]==norms[n,8][a]/c(n-2*a,8-a))
            for l,m in it.product(ls,repeat=2):
                check('coherent_triangle_'+str((n,l,m,a)),sigma[n,l,m,a]*sigma[n,8,8,a]==sigma[n,l,8,a]*sigma[n,m,8,a])
                check('both_directions_'+str((n,l,m,a)),sigma[n,l,m,a]==sigma[n,m,l,a])
            for r in range(9):
                check('diagonal_beta_eigen_'+str((n,a,r)),beta(n,8,8,a,8-r)==c(n-2*a,8-a)*eigen(n,a,r))
    report.update(factors=factors,transitions=transitions,coherent_scales=[{'indices':k,'value':v} for k,v in sigma.items()])
    save('direct_actions_checked')
    print('All',len(transitions),'direct subset transitions and coherent scales checked; failures:',failures,flush=True)

    S={l:c(68,l)*c(956,l) for l in LS}
    modes=[]
    for a,b in it.product(range(9),repeat=2):
        ls=[l for l in [5,6,7] if l>=max(a,b)]
        present=ls+[8]
        N8=norms[68,8][a]*norms[956,8][b]
        D8=c(68-2*a,8-a)*c(956-2*b,8-b)
        ss={l:sigma[68,l,8,a]*sigma[956,l,8,b]/(N8/D8) for l in present}
        def weighted(l,m):
            ll,mm=sorted([l,m])
            val=sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*entries[ll,mm,i,j] for i,j in it.product(range(ll+1),repeat=2))
            if (a,b)==(0,0):
                val-=p[l]*p[m]*S[m]
            return norms[68,l][a]*norms[956,l][b]*val
        B=[[weighted(l,m) for m in ls] for l in ls]
        t=[weighted(l,8) for l in ls]
        sv=data['modes'][9*a+b]
        check('original_weighted_block_'+str((a,b)),enc(B)==sv['weighted_base'] and enc(t)==sv['weighted_cross'])
        for i,l in enumerate(ls):
            check('coherent_cross_'+str((a,b,l)),t[i]==F(*sv['cross'][i])*(N8/D8)*ss[l])
            for j,m in enumerate(ls):
                check('coherent_old_'+str((a,b,l,m)),B[i][j]==F(*sv['base'][i][j])*(N8/D8)*ss[l]*ss[m])
        # Reverse layer order and retain every zero-pivot row/cross residual.
        H=[list(reversed(row)) for row in reversed(B)]
        u=list(reversed(t)); cost=F(0); stages=[]; rank=0
        for k in range(len(H)):
            pivot=H[k][k]
            check('reverse_pivot_'+str((a,b,k)),pivot>=0)
            if pivot==0:
                check('complete_zero_row_'+str((a,b,k)),not any(H[k][k:]+[u[k]]))
            elif pivot>0:
                rank+=1; cost+=u[k]**2/pivot
                for i in range(k+1,len(H)):
                    u[i]-=H[i][k]*u[k]/pivot
                    for j in range(k+1,len(H)):
                        H[i][j]-=H[i][k]*H[k][j]/pivot
            stages.append({'pivot':pivot,'matrix':[row[:] for row in H],'cross':u[:]})
        required=cost/(p[8]*N8)
        check('reverse_range_energy_'+str((a,b)),required==F(*sv['required'])==F(*ver['modes'][9*a+b]['required']))
        # Entire eight/eight diagonal, as an affine function, in the direct action.
        fixed=sum(gamma[68,8,8,a,i]*gamma[956,8,8,b,j]*y/p[8] for (l,m,i,j),y in entries.items() if l==m==8)
        anchor=p[8]*S[8] if a==b==0 else F(0)
        row=[-F(gamma[68,8,8,a,8-r]*gamma[956,8,8,b,8-q],c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        rhs=fixed-anchor-required
        check('entire_direct_row_'+str((a,b)),enc(row)==data['matrix'][9*a+b]==ver['matrix'][9*a+b])
        check('entire_direct_bound_'+str((a,b)),enc(rhs)==data['rhs'][9*a+b]==ver['rhs'][9*a+b])
        modes.append({'mode':(a,b),'layers':ls,'scales':ss,'base':B,'cross':t,'rank':rank,'reverse_elimination':stages,'required':required,'fixed':fixed,'anchor':anchor,'row':row,'rhs':rhs})
    mult=lambda a,b:(c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
    for l in LS:
        check('source_mode_exhaustion_'+str(l),sum(mult(a,b) for a,b in it.product(range(l+1),repeat=2))==S[l])
    trace=p[8]**2+p[8]*sum(mult(*m['mode'])*m['required'] for m in modes)/S[8]
    check('full_anchor_energy_trace',trace==F(*energy['energy'])==F(*data['trace_energy']))
    report.update(modes=modes,trace_energy=trace)
    save('all_modes_checked')
    print('All 81 direct/source rows and reverse singular ranges checked; failures:',failures,flush=True)

    manuscript=(NB/'lemmas/L078-simultaneous-eight-shell-fixed-column-obstruction.md').read_text()
    part=manuscript.split('**Compact exact separator.**')[1].split('Define the 42-by-42')[0]
    I=[int(v) for v in re.search(r'I=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    J=[int(v) for v in re.search(r'J=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    check('manuscript_basis_dimensions',len(I)==len(J)==42 and len(set(I))==len(set(J))==42)
    A=[m['row'] for m in modes]; rhs=[m['rhs'] for m in modes]
    matrix=[[F(-1) if j==-1 else A[i][j] for i in I] for j in J]
    yi,pivots=solve(matrix,[F(-1) if j==-1 else F(0) for j in J])
    y=[F(0)]*81
    for i,v in zip(I,yi):
        y[i]=v
    check('all_original_dual_values',enc(y)==data['exact']['dual']==ver['dual'] and len(pivots)==42 and all(pivots))
    check('every_dual_sign',min(y)==0 and sum(v>0 for v in y)==27 and sum(y)==1)
    sums=[]; raw=[]
    for j,(r,q) in enumerate(free):
        s=sum(y[i]*A[i][j] for i in range(81))
        rr=-sum(y[9*a+b]*F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*c(68-2*a,8-a)*c(956-2*b,8-b)) for a,b in it.product(range(9),repeat=2))
        check('original_scaled_raw_'+str((r,q)),s>=0 and rr==s*c(8,r)*c(60,r)*c(8,q)*c(948,q)/p[8]
              and enc(s)==data['exact']['column_sums'][j]==ver['column_sums'][j]
              and enc(rr)==data['exact']['raw_moment_column_sums'][j]==ver['raw_moment_column_sums'][j])
        sums.append(s);raw.append(rr)
    check('sole_sign_dependence',[(rq) for rq,s in zip(free,sums) if s>0]==[(3,6)] and sum(s==0 for s in sums)==44)
    value=dot(y,rhs)
    parts={name:sum(y[i]*m[name] for i,m in enumerate(modes)) for name in ['fixed','anchor','required']}
    check('exact_fixed_pairing',value==parts['fixed']-parts['anchor']-parts['required'] and enc(value)==data['exact']['fixed_value']==ver['fixed_pairing'])
    gaps=[value-F(-153934054111800,10**6),F(-153934054111799,10**6)-value]
    check('strict_manuscript_interval',gaps[0]>=0 and gaps[1]>0 and value<0)
    split=Counter((len(m['layers']),m['rank']) for m in modes)
    summary={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
             'types':len(records),'presentations':6*len(records),'direct_transitions':len(transitions),'modes':81,
             'rank_cases':{str(k):v for k,v in sorted(split.items())},'positive_dual_weights':sum(v>0 for v in y),
             'zero_scaled_raw_columns':sum(x==0 for x in sums),'positive_sign_coordinate':[3,6],
             'fixed_pairing_interval':[-153934054111800,-153934054111799,10**6],'required_pairing_lower_bound':0,
             'minimum_dual_weight':min(y),'minimum_column_sum':min(sums)}
    report.update(manuscript_basis_rows=I,manuscript_basis_columns=J,reverse_basis_pivots=pivots,dual=y,
                  scaled_sums=sums,raw_sums=raw,fixed_pairing=value,pairing_parts=parts,interval_gaps=gaps,summary=summary)
    save('completed')
    print(enc(summary))
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
