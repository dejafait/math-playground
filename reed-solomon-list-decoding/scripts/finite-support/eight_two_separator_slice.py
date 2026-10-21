"""Bounded two-coordinate proposal and exact test, no global exclusion."""
import hashlib
import itertools as it
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from verify_simultaneous_eight_shell import cramer, enc
from eight_two_separator_intersection import dot, quadratic, interval

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'eight-two-separator-intersection-results.json'
OUT=ROOT/'eight-two-separator-slice-results.json'


def main():
    d=json.loads(SOURCE.read_text());checks=[];failures=[]
    def check(n,v):
        checks.append(n)
        if not v:failures.append(n)
    fs=[[F(*x) for x in r] for r in d['domain']]
    Ms=[[[F(*x) for x in r] for r in p['M']] for p in d['pairings']]
    s=-Ms[0][0][4]/Ms[0][4][4];scale=F(1,10**10)
    # t56=0, t78=s; remaining coordinates are scale*(u,v).
    z0=[F(1),F(0),F(0),F(0),s]
    G=[[Ms[1][i][j]*scale**2 for j in [2,3]] for i in [2,3]]
    g=[dot(Ms[1][i],z0)*scale for i in [2,3]]
    rows=[[dot(r,z0),r[2]*scale,r[3]*scale] for r in fs]
    norms=[max(map(abs,r)) for r in rows]
    aa=[[float(x/n) for x in r] if n else [0.,0.,0.] for r,n in zip(rows,norms)]
    norm=max(abs(x) for r in G for x in r)
    GG=[[float(x/norm) for x in r] for r in G];gg=[float(x/norm) for x in g]
    def solve2(A,b):
        det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
        if abs(det)<1e-14:return None
        return [(b[0]*A[1][1]-A[0][1]*b[1])/det,(A[0][0]*b[1]-b[0]*A[1][0])/det]
    proposals=[]
    def offer(x,kind,active):
        if x is None:return
        if min(c+a*x[0]+b*x[1] for c,a,b in aa)<-1e-9:return
        value=sum(GG[i][j]*x[i]*x[j] for i,j in it.product(range(2),repeat=2))+2*sum(gg[i]*x[i] for i in range(2))
        proposals.append({'kind':kind,'active':active,'x':x,'nonconstant_score':value})
    offer(solve2(GG,[-x for x in gg]),'interior',[])
    for j,(c,a,b) in enumerate(aa):
        if abs(a)+abs(b)<1e-14:continue
        x=[-c/a,0.] if abs(a)>=abs(b) else [0.,-c/b]
        v=[b,-a]
        den=sum(v[i]*GG[i][k]*v[k] for i,k in it.product(range(2),repeat=2))
        if den>=-1e-14:continue
        q=-sum(v[i]*(gg[i]+sum(GG[i][k]*x[k] for k in range(2))) for i in range(2))/den
        offer([x[i]+q*v[i] for i in range(2)],'edge',[j])
    for i,j in it.combinations(range(85),2):
        offer(solve2([aa[i][1:],aa[j][1:]],[-aa[i][0],-aa[j][0]]),'vertex',[i,j])
    proposals.sort(key=lambda p:p['nonconstant_score'],reverse=True)
    out={'input_hashes':{str(SOURCE.relative_to(ROOT.parent.parent)):hashlib.sha256(SOURCE.read_bytes()).hexdigest()},
         'slice':{'t56':F(0),'t78':s,'coordinate_scale':scale},'numeric_proposals':proposals,'checks':checks,'failures':failures}
    OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    if not proposals:
        out['summary']={'verdict':'NO_SLICE_PROPOSAL','checks':0,'failures':0}
    else:
        proposal=proposals[0];active=proposal['active']
        if proposal['kind']=='interior':x=cramer(G,[-v for v in g])
        elif proposal['kind']=='vertex':x=cramer([rows[j][1:] for j in active],[-rows[j][0] for j in active])
        else:
            j=active[0];c,a,b=rows[j]
            xx=[-c/a,F(0)] if a else [F(0),-c/b];v=[b,-a]
            den=dot(v,[dot(r,v) for r in G]);q=-dot(v,[dot(r,xx)+w for r,w in zip(G,g)])/den
            x=[u+q*w for u,w in zip(xx,v)]
        z=[F(1),F(0),scale*x[0],scale*x[1],s]
        signs=[dot(r,z) for r in fs];values=[quadratic(M,z) for M in Ms]
        check('exact_slice_domain',min(signs)>=0)
        check('old_pairing_at_positive_maximum',values[0]>0 and z[4]==s)
        # The second sign is evidence, never a failed solver assertion.
        verdict='COMMON_WITNESS' if min(signs)>=0 and min(values)>=0 else 'SLICE_TEST_INCONCLUSIVE'
        out.update(selected_proposal=proposal,point=z,column_factors=signs,pairings=values,
                   original_mode_rhs=[quadratic([[F(*v) for v in r] for r in m['quadratic']],z) for m in d['modes']])
        out['summary']={'verdict':verdict,'checks':len(checks),'failures':len(failures),'actual_domain_minimum':min(signs),'required_domain_minimum':0,'required_pairing_minimum':0,
                        'positive_factors':sum(v>0 for v in signs),'zero_factors':[i for i,v in enumerate(signs) if not v],
                        'pairing_intervals':[interval(v) for v in values],'selected_kind':proposal['kind'],'selected_active':active}
    OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    print(enc(out['summary']));print('Full certificate:',OUT.relative_to(ROOT.parent.parent))


if __name__=='__main__':main()
