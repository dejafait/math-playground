"""Independent exact residual and affine-lift verification, no numerical solve."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'reduced-zero-plane-joint-verification.json'


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)),F(0))


def dec(A):
    return [[F(*v) for v in r] for r in A]


def tr(A):
    return list(map(list,zip(*A))) if A else []


def mm(A,B):
    assert not A or len(A[0])==len(B)
    return [[dot(a,b) for b in zip(*B)] for a in A]


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def determinant(A):
    if not A:
        return F(1)
    return sum(((-1)**j*v*determinant([r[:j]+r[j+1:] for r in A[1:]]) for j,v in enumerate(A[0]) if v),F(0))


def interval(x):
    k=x.numerator*10**6//x.denominator
    return [F(k,10**6),F(k+1,10**6)]


def main():
    names=['reduced-zero-plane-joint-results.json','zero-plane-positive-mode-compatibility-results.json',
           'zero-plane-fixed-face-results.json','fully-cancelling-separator-family-critical-audit.json',
           'eight-distance-full-base-kernel-results.json','zero-plane-joint-feasibility-results.json']
    paths=[ROOT/n for n in names]
    data,eq,face,src,col,old=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    for name,obj in zip(names,[data,eq,face,src,col,old]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    L,R,K,G=map(dec,[data['lift'],data['reverse'],data['reverse_identity_multipliers'],data['selected_constraints']])
    check('all_forward_equations',mm(G,L)==[[F(0)]*22 for _ in range(28)])
    check('all_reduced_reverse_identities',mm(R,L)==eye(22))
    check('all_original_reverse_identities',mm(K,G)==[[a-b for a,b in zip(x,y)] for x,y in zip(mm(L,R),eye(49))])
    check('lift_matches_reviewed_all_solution',L[4:]==[a[:4]+b for a,b in zip(dec(eq['particular_coefficients']),dec(eq['right_kernel']))])
    check('all_quadratic_coefficients_zero',all(not any(r[4:]) for r in dec(eq['particular_coefficients'])))
    selected=eq['selected_modes']
    check('all_selected_original_rows',G==[[-v for v in b[:4]]+a for a,b in zip(dec(eq['original_equalities']),dec(eq['rhs_coefficients']))])
    r=data['reconstruction']
    reduced=[F(*v) for v in r['reduced_coordinates']]
    lifted=[F(*v) for v in r['lifted_coordinates']]
    scales=[F(*v) for v in data['numerical_scaling']['coordinate_scales']]
    proposal=data['proposal']['x']
    rounded=[F(float(v)).limit_denominator(10**9) for v in proposal]
    check('single_declared_rounding',enc(rounded)==r['rounded_numerical_coordinates'] and reduced==[F(1)]+[s*v for s,v in zip(scales,rounded)])
    check('candidate_exact_lift',lifted==[dot(a,reduced) for a in L] and reduced==[dot(a,lifted) for a in R])
    q,z=lifted[:4],lifted[4:]
    s=F(*eq['stationary_t78'])
    point=q+[s]
    check('saved_point_and_moments',enc(q)==r['q'] and enc(z)==r['z'] and enc(point)==r['point'])
    family=[[F(*v)]+[F(*x) for x in row] for v,row in zip(col['affine']['intercept'],col['affine']['slopes'])]
    domain=[[v[0]+s*v[4]]+v[1:4] for v in family]
    factors=[dot(a,point) for a in family]
    check('all_domain_rows',len(domain)==85 and enc(domain)==data['domain'] and enc(factors)==r['domain_factors'])
    free=[(a,b) for a,b in it.product(range(9),repeat=2) if a+b>=8]
    p8=F(16792471,1181138102168120460)
    raw=[p8*v/F(C(8,a)*C(60,a)*C(8,b)*C(948,b)) for (a,b),v in zip(free,z)]
    check('all_45_original_raw_moments',len(raw)==45 and enc(raw)==r['raw_moments'])
    bounds,slacks,rawslacks,blocks,minor_values=[],[],[],[],[]
    for k,m in enumerate(src['modes']):
        a,b=divmod(k,9)
        norm=p8*C(68-2*a,8-a)*C(956-2*b,8-b)
        base=dec(m['source_base'])
        c=[dot(row,point) for row in dec(m['source_cross'])]
        inverse=[dot(row,point) for row in dec(m['inverse_affine'])]
        check('whole_original_range_'+str(k),[dot(row,inverse) for row in base]==c)
        bound=dot([F(*v) for v in m['forced']],point)-F(*m['anchor'])-dot(c,inverse)/norm
        A=[-F(beta(68,8,8,a,8-u)*beta(956,8,8,b,8-v),norm/p8*C(8,u)*C(60,u)*C(8,v)*C(948,v)) for u,v in free]
        slack=bound-dot(A,z)
        rawslack=sum((beta(68,8,8,a,8-u)*beta(956,8,8,b,8-v)*y for (u,v),y in zip(free,raw)),F(0))+norm*bound
        check('original_bound_'+str(k),enc(bound)==r['bounds'][k])
        check('original_mode_'+str(k),enc(A)==data['matrix'][k] and enc(slack)==r['mode_slacks'][k])
        check('original_raw_schur_'+str(k),rawslack==norm*slack and enc(rawslack)==r['raw_schur_slacks'][k])
        # Direct original block, without the constructor's saved pencil.
        bottom=dot([F(*v) for v in m['forced']],point)-F(*m['anchor'])-dot(A,z)
        block=[[v/norm for v in row]+[c[i]/norm] for i,row in enumerate(base)]+[[v/norm for v in c]+[bottom]]
        saved=r['original_blocks'][k]
        check('complete_original_block_'+str(k),enc(block)==saved['original_normalized_block'])
        ms=[]
        for size in range(1,len(block)+1):
            for I in it.combinations(range(len(block)),size):
                ms.append({'indices':list(I),'determinant':determinant([[block[i][j] for j in I] for i in I])})
        check('every_original_principal_minor_'+str(k),enc(ms)==saved['principal_minors'])
        check('all_failed_minors_'+str(k),[j for j,v in enumerate(ms) if v['determinant']<0]==saved['negative_minor_indices'])
        blocks.append({'mode':k,'block':block,'principal_minors':ms})
        minor_values += [v['determinant'] for v in ms]
        bounds.append(bound)
        slacks.append(slack)
        rawslacks.append(rawslack)
        # Every reduced affine coefficient comes from the original retained
        # pencil and the same L, including selected compressed empty blocks.
        rp=dec(old['blocks'][k]['original_base'])
        check('unchanged_source_base_'+str(k),rp==[[v/norm for v in row] for row in base])
        retained=data['retained_pencils'][k]
        n=len(retained[0])
        subst=[[[sum((F(*retained[j][i][h])*L[j][v] for j in range(49)),F(0)) for h in range(n)] for i in range(n)] for v in range(22)]
        expected=data['reduced_pencils'][k]['coefficients']
        if k in selected:
            kernel=dec(face['blocks'][k]['kernel_basis'])
            rr=len(kernel[0])
            compressed=[mm(mm(tr(kernel),P),kernel) if rr else [] for P in subst]
            check('all_reduced_coefficients_'+str(k),enc(compressed)==expected)
            eqrows=dec(next(v for v in data['face_equations'] if v['mode']==k)['original_coefficients'])
            check('all_mixed_removed_equations_'+str(k),not any(any(v) for v in mm(eqrows,L)) and enc(tr(eqrows))==face['blocks'][k]['face_equation_coefficients'])
        else:
            check('all_reduced_coefficients_'+str(k),enc(subst)==expected)
    negatives={'domain':[i for i,v in enumerate(factors) if v<0],
               'moments':[i for i,v in enumerate(z) if v<0],
               'modes':[i for i,v in enumerate(slacks) if v<0],
               'original_blocks':[v['mode'] for v in blocks if any(w['determinant']<0 for w in v['principal_minors'])]}
    check('all_failed_indices',negatives=={'domain':r['negative_domain_rows'],'moments':r['negative_moment_indices'],
                                        'modes':r['negative_modes'],'original_blocks':r['negative_original_blocks']})
    eqres=[dot(a,lifted) for a in G]
    check('all_28_original_equalities',not any(eqres) and all(slacks[k]==0 for k in selected) and enc(eqres)==r['selected_equality_residuals'])
    check('one_capped_proposal_one_reconstruction',r['passes']==data['summary']['numerical_runs']==1 and data['proposal']['iterations']<=data['iteration_cap_before_solve']==10000)
    feasible=not any(negatives.values())
    check('honest_verdict',data['summary']['full_domain_feasibility_decided']==feasible and data['summary']['verdict']==('RATIONAL_FEASIBLE_WITNESS' if feasible else 'INCONCLUSIVE'))
    fscales=[max(abs(f[0]),*(abs(v*F(1,10**11)) for v in f[1:])) or F(1) for f in domain]
    zscales=[F(*v) for v in old['numerical_scaling']['zscale']]
    bscales=[F(*v) for v in old['numerical_scaling']['blockscales']]
    minima={'domain':min(v/t for v,t in zip(factors,fscales)),
            'moments':min(v/t for v,t in zip(z,zscales)),
            'modes':min(v/t for v,t in zip(slacks,bscales))}
    report.update(checks=checks,failures=failures,domain_factors=factors,raw_moments=raw,
                  original_mode_slacks=slacks,raw_schur_slacks=rawslacks,original_blocks=blocks,
                  negative_rows=negatives,exact_normalized_minima=minima,
                  summary={'verdict':('VERIFIED_FEASIBLE_CANDIDATE' if feasible else 'VERIFIED_FAILED_CANDIDATE_ONLY') if not failures else 'FAILED',
                           'checks':len(checks),'failures':len(failures),
                           'negative_counts':{k:len(v) for k,v in negatives.items()},'selected_equalities_exact':not any(eqres),
                           'all_original_principal_minors':len(minor_values),'negative_principal_minors':sum(v<0 for v in minor_values),
                           'normalized_minimum_intervals':{k:interval(v) for k,v in minima.items()},
                           'required_minimum':0,'full_domain_verdict':'FEASIBLE' if feasible else 'UNDECIDED'})
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(enc(report['summary']),flush=True)
    print('Verification failures:',failures,'; certificate:',OUT.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
