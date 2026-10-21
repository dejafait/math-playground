"""Independent original/raw certificate check; never invokes Phase I.

Rebuilds selected original beta/Schur rows from ancestral full-anchor data.
No tableau status or floating residual is mathematical evidence here.
"""
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
OUT=ROOT/'affine-sign-phase-one-verification.json'


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b) if x and y),F(0))


def dec(a):
    return [[F(*v) for v in r] for r in a]


def mm(a,b):
    return [[dot(r,c) for c in zip(*b)] for r in a]


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def main():
    names=['affine-sign-phase-one-results.json',
           'fully-cancelling-separator-family-critical-audit.json',
           'eight-distance-full-base-kernel-results.json',
           'zero-plane-positive-mode-compatibility-results.json']
    paths=[ROOT/n for n in names]
    data,src,col,eq=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    for name,obj in zip(names,[data,src,col,eq]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p8=F(16792471,1181138102168120460)
    s=F(*src['stationary_t78'])
    family=[[F(*v)]+[F(*w) for w in row] for v,row in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('ancestral_family',enc(family)==src['family'])
    domain=[[r[0]+s*r[4]]+r[1:4] for r in family]
    selected=[9*a+b for a in range(7) for b in range(4)]
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    volumes=[F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    G,rawG,bounds=[],[],[]
    for idx in selected:
        mode=src['modes'][idx]
        a,b=divmod(idx,9)
        D=F(C(68-2*a,8-a)*C(956-2*b,8-b))
        base,cross,inverse=map(dec,[mode['source_base'],mode['source_cross'],mode['inverse_affine']])
        check('original_range_'+str(idx),mm(base,inverse)==cross)
        c=[[r[0]+s*r[4]]+r[1:4] for r in cross]
        x=[[r[0]+s*r[4]]+r[1:4] for r in inverse]
        fixed=[F(*v) for v in mode['forced']]
        fixed[0]-=F(*mode['anchor'])
        f=[fixed[0]+s*fixed[4]]+fixed[1:4]
        cost=[[dot([r[i] for r in c],[r[j] for r in x])/(p8*D) for j in range(4)] for i in range(4)]
        Q=[[-(cost[i][j]+cost[j][i])/2 for j in range(4)] for i in range(4)]
        Q[0][0]+=f[0]
        for i in range(1,4):
            Q[0][i]+=f[i]/2
            Q[i][0]+=f[i]/2
        bb=[Q[0][0]]+[2*Q[0][i] for i in range(1,4)]
        quadratic=[Q[i][j]*(1 if i==j else 2) for i in range(1,4) for j in range(i,4)]
        check('all_six_absent_quadratic_terms_'+str(idx),quadratic==[0]*6)
        raw=[F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        row=[-v/(D*V) for v,V in zip(raw,volumes)]
        g=[-v for v in bb]+row
        G.append(g)
        # Equality rawG*w_raw=0 is the unnormalized Schur remainder.
        rawG.append([p8*D*v for v in bb]+raw)
        check('all_original_selected_coefficients_'+str(idx),enc(g)==data['equalities'][len(G)-1] and enc(bb+quadratic)==eq['rhs_coefficients'][len(G)-1])
        bounds.append({'mode':idx,'affine':bb,'plane_quadratic':Q,'raw_beta':raw,'D':D})
    H=[r+[F(0)]*45 for r in domain]+[eye(49)[j+4] for j in range(45)]
    Hraw=[r+[F(0)]*45 for r in domain]+[eye(49)[j+4] for j in range(45)]
    check('all_130_original_rows',enc(H)==data['original_inequalities'] and len(H)==130)
    check('all_85_domain_rows',enc(domain)==data['domain'])
    L,R,K=map(dec,[data['lift'],data['reverse'],data['reverse_identity_multipliers']])
    check('whole_equality_forward',mm(G,L)==[[0]*22 for _ in range(28)])
    check('whole_equality_reverse_left_inverse',mm(R,L)==eye(22))
    check('whole_original_reverse',mm(K,G)==[[x-y for x,y in zip(r,t)] for r,t in zip(mm(L,R),eye(49))])
    pulled=mm(H,L)
    check('all_130_pulled_rows',enc(pulled)==data['pulled_inequalities'])
    signs=[F(1) if row[0]>=0 else F(-1) for row in pulled]
    standard=[[sg*v for v in [-v for v in row[1:]]+row[1:]+eye(130)[i]] for i,(row,sg) in enumerate(zip(pulled,signs))]
    b0=[sg*row[0] for sg,row in zip(signs,pulled)]
    check('exact_free_variable_slack_conversion',enc(standard)==data['standard_matrix'] and enc(b0)==data['standard_rhs'] and enc(signs)==data['row_signs'])
    check('single_bounded_phase_one',data['limits']=={'pivots':10000,'seconds':300,'runs':1} and data['phase_one']['pivots']<=10000)
    verdict=data['summary']['verdict']
    if verdict=='RATIONAL_FEASIBLE_WITNESS':
        w=[F(*v) for v in data['witness']['original']]
        raw=[F(*v) for v in data['witness']['raw_moments']]
        values=[F(*v) for v in data['witness']['standard_values']]
        check('standard_solution_independent_substitution',min(values)>=0 and not any(values[172:]) and [dot(r,values[:172]) for r in standard]==b0)
        check('original_constant_coordinate',w[0]==1)
        domain_values=[dot(row,w[:4]) for row in domain]
        eqres=[dot(row,w) for row in G]
        raww=w[:4]+raw
        rawres=[dot(row,raww) for row in rawG]
        check('all_85_original_domain_rows',min(domain_values)>=0)
        check('all_45_original_signs',min(w[4:])>=0)
        check('all_45_raw_signs_and_scaling',min(raw)>=0 and raw==[p8*z/V for z,V in zip(w[4:],volumes)])
        check('all_28_original_equalities',eqres==[0]*28)
        check('all_28_raw_unnormalized_equalities',rawres==[0]*28)
        report.update(original_point=w,raw_point=raww,domain_values=domain_values,
                      original_equality_residuals=eqres,raw_equality_residuals=rawres,
                      summary={'verdict':'VERIFIED_RATIONAL_SUBSYSTEM_WITNESS',
                               'domain_positive':sum(v>0 for v in domain_values),'domain_zero':sum(v==0 for v in domain_values),
                               'zero_domain_indices':[i for i,v in enumerate(domain_values) if v==0],
                               'moments_positive':sum(v>0 for v in raw),'moments_zero':sum(v==0 for v in raw),
                               'zero_moment_indices':[i for i,v in enumerate(raw) if v==0],
                               'required_minimum':0,'actual_domain_minimum':min(domain_values),
                               'actual_raw_moment_minimum':min(raw),'equality_residuals_nonzero':sum(v!=0 for v in eqres+rawres)})
    elif verdict=='RATIONAL_ORIGINAL_FARKAS_CERTIFICATE':
        sep=data['separator']
        lam=[F(*v) for v in sep['inequality_weights']]
        mu=[F(*v) for v in sep['equality_multipliers']]
        agg=[dot(lam,c)+dot(mu,d) for c,d in zip(zip(*H),zip(*G))]
        # Raw signs have different positive diagonal scaling; rawG includes
        # the negative mode-dependent factor -p8*D relative to G_raw.
        rawlam=lam[:85]+[v*V/p8 for v,V in zip(lam[85:],volumes)]
        rawmu=[-v/(p8*bound['D']) for v,bound in zip(mu,bounds)]
        rawagg=[dot(rawlam,c)+dot(rawmu,d) for c,d in zip(zip(*Hraw),zip(*rawG))]
        check('all_130_nonnegative_inequality_weights',len(lam)==130 and min(lam)>=0)
        check('original_48_coefficients_cancel',agg[1:]==[0]*48)
        check('strict_original_rhs',agg[0]<0 and enc(agg)==sep['original_certificate'])
        check('all_raw_inequality_weights_nonnegative',min(rawlam)>=0)
        check('raw_48_coefficients_cancel',rawagg[1:]==[0]*48)
        check('strict_raw_rhs',rawagg[0]==agg[0]<0)
        report.update(inequality_weights=lam,equality_multipliers=mu,original_certificate=agg,
                      raw_inequality_weights=rawlam,raw_unnormalized_equality_multipliers=rawmu,raw_certificate=rawagg,
                      summary={'verdict':'VERIFIED_STRICT_ORIGINAL_RAW_FARKAS',
                               'actual_strict_rhs':agg[0],'required_rhs_upper_bound':0,
                               'nonzero_original_variable_coefficients':sum(v!=0 for v in agg[1:]),
                               'nonzero_raw_variable_coefficients':sum(v!=0 for v in rawagg[1:])})
    else:
        report['summary']={'verdict':'SUBSYSTEM_UNDECIDED','saved_solver_verdict':verdict}
    report.update(checks=checks,failures=failures,domain=domain,equalities=G,raw_equalities=rawG,bounds=bounds)
    report['summary'].update(checks=len(checks),failures=len(failures),other_53_modes_decided=False,rs_boundary=[955,957])
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(enc(report['summary']),flush=True)
    print('Failures:',failures,'; certificate:',OUT.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
