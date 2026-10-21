"""Frozen singleton-mixture diagnostic; exact arithmetic, no optimization.

Stores every orbit coefficient losslessly as two factor arrays per (i,j),
their source multinomials, all h aggregates, and all row residuals.
Independent inclusion-region counting checks every product coefficient.
Frozen PSD endpoint congruences are verified, then convexity is used.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).parent
OUT = BASE / 'fixed-cardinality-normalized-control-results.json'
W, V = 68, 956

def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]

def dec(x): return F(*x)

@lru_cache(None)
def fc(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k)) if 0 <= k <= n else 0

def multi(n, a, b, c):
    return factorial(n)//(factorial(a)*factorial(b)*factorial(c)*factorial(n-a-b-c))

def main():
    failures = []
    def need(ok, label):
        if not ok: failures.append(label)
    paths = ['delsarte-lp-results.json', 'free-pair-shell-batch-results.json',
             'full-zero-block-results.json', 'full-scalar-results.json']
    hashes = {s: hashlib.sha256((BASE/s).read_bytes()).hexdigest() for s in paths}
    lp, batch, full, scalar = [json.loads((BASE/s).read_text()) for s in paths]
    p = [F(1)]+[F(0)]*4+[F(r['numerator'],r['denominator'])/
         (2*comb(W,i)*comb(V,i)) for i,r in zip(range(5,69),lp['exact']['primal'])]
    g = [comb(W,i)*comb(V,i) for i in range(69)]
    U = F(comb(1024,64),comb(68,64))
    M = sum(a*b for a,b in zip(g,p))
    T = F(65537**28,2**128)
    exact_n = T.numerator//T.denominator+1
    alpha = F(exact_n-1, M-1)
    need(M==(U+1)/2 and 0<alpha<1, 'endpoint objective and mixing interval')
    need(p==list(map(dec,batch['p']))==list(map(dec,full['p']))==list(map(dec,scalar['p'])),
         'all frozen endpoint pairs agree')
    cp = [alpha*x+(1-alpha)*int(i==0) for i,x in enumerate(p)]
    need(sum(g[i]*cp[i] for i in range(69))==exact_n, 'exact-N control objective')
    need(cp[0]==1 and all(x==0 for x in cp[1:5]), 'normalization and pair zeros')
    result = {'stage':'in_progress','parameters':{'n':1024,'w':68,'v':956,'d':10},
              'input_sha256':hashes, 'N':exact_n,'T':enc(T),'M':enc(M),
              'alpha':enc(alpha),'p':list(map(enc,p)),'control_p':list(map(enc,cp)),
              'objective':enc(sum(g[i]*cp[i] for i in range(69))),
              'failures':failures}
    OUT.write_text(json.dumps(result)+'\n')

    # Reuse full source proofs L023/L097, checking their frozen complete
    # congruences here. No new source block or optimization is introduced.
    psd = []
    all_blocks = [(b['k'],b['l'],b['indices'],b['families']) for b in batch['blocks']]
    all_blocks.append((0,0,list(range(69)),full['families']))
    for k,l,inds,families in all_blocks:
        for family,data in enumerate(families):
            A = [[dec(x) for x in row] for row in data['matrix']]
            proof = data['certificate']
            E = [[dec(x) for x in row] for row in proof['congruence']]
            diag = list(map(dec,proof['diagonal']))
            size = len(inds)
            need(proof['psd'] and len(A)==len(E)==len(diag)==size,
                 'endpoint PSD dimensions')
            need(all(E[i][i]==1 and all(E[i][j]==0 for j in range(i)) for i in range(size)),
                 'unit triangular frozen congruence')
            ad = lcm(*(x.denominator for row in A for x in row))
            cd = [lcm(*(E[i][j].denominator for i in range(size))) for j in range(size)]
            ai = [[int(x*ad) for x in row] for row in A]
            ei = [[int(E[i][j]*cd[j]) for j in range(size)] for i in range(size)]
            ae = [[sum(ai[i][h]*ei[h][j] for h in range(j+1)) for j in range(size)] for i in range(size)]
            identities = all(sum(ei[h][i]*ae[h][j] for h in range(i+1)) ==
                             (ad*cd[i]*cd[j]*diag[i] if i==j else 0)
                             for i in range(size) for j in range(size))
            need(identities and all(x>=0 for x in diag), 'complete frozen PSD identity')
            # For the singleton endpoint only the all-repeated y survives.
            # Complemented family retains only h=0, hence is diagonal.
            ed = [(F(int(k==l==0 and i==0)) if family==0 else
                  F(fc(W-2*k,i-k)*fc(V-2*l,i-l)-int(k==l==0 and i==0))) for i in inds]
            need(all(x>=0 for x in ed), 'singleton PSD diagonal')
            mixed = [[alpha*A[i][j]+(1-alpha)*(ed[i] if i==j else 0)
                      for j in range(size)] for i in range(size)]
            psd.append({'k':k,'l':l,'indices':inds,'family':family,
                        'frozen_congruence_verified':identities,
                        'singleton_diagonal':list(map(enc,ed)),
                        'control_matrix':[[enc(x) for x in row] for row in mixed]})
    need(len(psd)==168, '166 batch and two full zero-index matrices')
    result['PSD_convex_certificates'] = psd
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Inherited PSD: complete frozen congruences and singleton diagonals:',len(psd),flush=True)

    pair_rows=[]
    for label in range(1,69):
        poly=[0]*69
        for r in range(69-label):
            c=fc(W-label,r)*fc(V-label,r)
            for h in range(label+1): poly[r+h]+=c*(-1)**h*fc(label,h)
        old_slack=1+sum(poly[i]*p[i] for i in range(5,69))
        new_slack=1+sum(poly[i]*cp[i] for i in range(5,69))
        need(old_slack>=0 and new_slack==alpha*old_slack+(1-alpha), 'pair convex row')
        if label<=64: need(old_slack==F(1,2),'L021 defining equation')
        pair_rows.append({'label':label,'coefficients':poly[5:],
                          'z_slack':enc(old_slack),'control_slack':enc(new_slack)})
    result['pair_rows']=pair_rows

    pd=lcm(*(x.denominator for x in p))
    pn=[int(x*pd) for x in p]
    yd=pd*pd*pn[68]
    cden=alpha.denominator*yd
    def zn(i,j,h):
        if any(0<a<5 for a in (i,j,h)): return 0
        if min(i,j,h)==0:
            a,b,c=sorted((i,j,h))
            need(b==c,'repeated distances')
            return pn[b]*pd*pn[68]
        return pn[i]*pn[j]*pn[h]
    def cn(i,j,h):
        return alpha.numerator*zn(i,j,h)+(alpha.denominator-alpha.numerator)*yd*int(i==j==h==0)
    cpn=[int(x*cden) for x in cp]
    # Scalar slack values depend only on (i,j,h); save every such value,
    # together with exact orbit multiplicities. t-s variables remain distinct.
    entries=[]; contractions=[]; scalar_values=[]
    actual_orbits=coefficient_checks=repeated=forbidden=0
    for i in range(69):
        total=0; actual_count=0; two_repeats=[]
        for j in range(69):
            ts=list(range(max(0,i+j-W),min(i,j)+1))
            ss=list(range(max(0,i+j-V),min(i,j)+1))
            af=[comb(i,t)*comb(W-i,j-t) for t in ts]
            bf=[comb(i,s)*comb(V-i,j-s) for s in ss]
            am=[multi(W,i-t,j-t,t) for t in ts]
            bm=[multi(V,i-s,j-s,s) for s in ss]
            need(all(a*comb(W,i)==m for a,m in zip(af,am)) and
                 all(b*comb(V,i)==m for b,m in zip(bf,bm)), 'source multinomial factors')
            hc={}; multiplicities={}
            for t,a in zip(ts,af):
                for s,b in zip(ss,bf):
                    h=i+j-t-s
                    coeff=a*b
                    # Independent direct inclusion of Z points in four regions.
                    direct=fc(i,i-t)*fc(W-i,W-i-j+t)*fc(i,s)*fc(V-i,j-s)
                    need(direct==coeff, 'independent four-region coefficient')
                    hc[h]=hc.get(h,0)+coeff
                    multiplicities[h]=multiplicities.get(h,0)+1
                    actual_count+=coeff
                    actual_orbits+=1; coefficient_checks+=1
                    if min(i,j,h)==0:
                        repeated+=1
                        need(t==s and coeff==(g[j] if i==0 else 1), 'repetition coefficient')
                        if i>0: two_repeats.append([j,t,s,coeff])
                    if any(0<a<5 for a in (i,j,h)): forbidden+=1
            need(sum(hc.values())==g[j], 'all third supports in shell j')
            entry={'i':i,'j':j,'t':ts,'s':ss,'inside_factors':af,'outside_factors':bf,
                   'source_inside_multinomials':am,'source_outside_multinomials':bm,
                   'h_coefficients':[[h,c] for h,c in sorted(hc.items())],
                   'h_orbit_multiplicities':[[h,c] for h,c in sorted(multiplicities.items())]}
            entries.append(entry)
            for h,c in sorted(hc.items()):
                y=cn(i,j,h); z=zn(i,j,h)
                singleton=int(i==j==h==0)
                control_slacks=[y,cpn[i]-y,cden+y-cpn[i]-cpn[j]]
                endpoint_slacks=[z,int(p[i]*yd)-z,yd+z-int(p[i]*yd)-int(p[j]*yd)]
                e_slacks=[singleton,int(i==0)-singleton,1+singleton-int(i==0)-int(j==0)]
                need(all(a>=0 for a in endpoint_slacks+e_slacks+control_slacks), 'all scalar signs')
                need(all(b==alpha.numerator*a+(alpha.denominator-alpha.numerator)*yd*e
                         for a,b,e in zip(endpoint_slacks,control_slacks,e_slacks)), 'scalar convex identities')
                scalar_values.append({'distances':[i,j,h],'orbits':multiplicities[h],
                                      'z_numerator':z,'singleton_value':singleton,
                                      'control_slack_numerators':control_slacks})
                total+=c*y
        residual=total-exact_n*cpn[i]
        if i>0: need(sorted(two_repeats)==[[0,0,0,1],[i,i,i,1]], 'both repeated third words')
        need(actual_count==comb(1024,68),'all third supports counted for fixed pair')
        contractions.append({'i':i,'ordered_pair_count':comb(1024,68)*g[i],
                             'third_support_count':actual_count,'repetition_orbits':two_repeats,
                             'lhs':enc(F(total,cden)),'rhs':enc(exact_n*cp[i]),
                             'residual':enc(F(residual,cden)),
                             'lhs_over_rhs':enc(F(total,exact_n*cpn[i])) if cpn[i] else None,
                             'holds':residual==0})
        if i%16==0 or i==68:
            print('Reconstructed cardinality/scalar rows through distance',i,flush=True)
    need(contractions[0]['holds'],'distance-zero objective contraction')
    need(all(r['holds'] for r in contractions[1:5]),'forbidden-distance contractions')
    need(actual_orbits==1500625 and repeated==205 and forbidden==10232,'full actual-orbit coverage')
    # All source permutations preserve the distance multiset. Both endpoint
    # value functions are symmetric in that multiset, so all required t-s
    # preserving equalities hold; no equality of free variables is added.
    for row in scalar_values:
        i,j,h=row['distances']
        need(cn(i,j,h)==cn(j,h,i)==cn(h,i,j), 'endpoint/control source symmetry')
    failed=[r['i'] for r in contractions[5:] if not r['holds']]
    ratios=[dec(r['lhs_over_rhs']) for r in contractions[5:]]
    result.update({'stage':'completed','coefficient_entries':entries,'contractions':contractions,
                   'scalar_denominator_z':yd,'scalar_denominator_control':cden,
                   'scalar_values':scalar_values,
                   'summary':{'inherited_controls_pass':not failures,'nonzero_rows_tested':64,
                              'nonzero_rows_failed':failed,'min_lhs_over_rhs':enc(min(ratios)),
                              'max_lhs_over_rhs':enc(max(ratios)),
                              'actual_ordered_orbits':actual_orbits,'coefficient_product_checks':coefficient_checks,
                              'expanded_scalar_rows':3*actual_orbits,'repeated_orbits':repeated,
                              'forbidden_orbits':forbidden,'PSD_matrices':len(psd),
                              'known_method_extra_condition':bool(failed) and not failures},
                   'failures':failures})
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Actual objective N:',exact_n,'; unsafe threshold:',T)
    print('Nonzero contraction failures:',len(failed),'of 64; required residual = 0')
    print('Inherited-control/coefficient failures:',len(failures),'; full certificate:',OUT)
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
