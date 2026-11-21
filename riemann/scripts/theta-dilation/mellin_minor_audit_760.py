"""Replay existing certificate, then independently integrate its step bounds.
No new minor. Integer polynomial sums avoid fixed-grid intermediate rounding.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import getcontext
import hashlib, importlib.util, json
BASE=Path(__file__).resolve().parent
SRC=BASE/'mellin_minor_758.py'
ORIGINAL=BASE/'mellin-minor-certificate-758.json'
REPLAY=BASE/'mellin-minor-replay-760.json'
OUT=BASE/'mellin-minor-audit-760.json'
S=10**40

def main():
    report={'step':760,'status':'INCOMPLETE','checks':{},'failures':[]}
    def check(name, condition):
        report['checks'][name]=bool(condition)
        if not condition: report['failures'].append(name)
        assert condition,name
    try:
        original_hash=hashlib.sha256(ORIGINAL.read_bytes()).hexdigest()
        spec=importlib.util.spec_from_file_location('minor758',SRC)
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        m.OUT=REPLAY
        old_exp=m.exp
        stats={'calls':0,'max_endpoint_digits':0,'min_raw':0,'max_raw':0}
        def audited_exp(arg):
            a=m.cv(arg)
            stats['calls']+=1
            for v in (a.lo,a.hi):
                digits=len(str(abs(v)))
                assert digits<=60,'inexact endpoint conversion possible'
                assert abs(v)<10000*S,'exponent range bound failed'
                stats['max_endpoint_digits']=max(stats['max_endpoint_digits'],digits)
                stats['min_raw']=min(stats['min_raw'],v)
                stats['max_raw']=max(stats['max_raw'],v)
            return old_exp(a)
        ctx=getcontext()
        report['decimal_context']={'Emin':ctx.Emin,'Emax':ctx.Emax,'rounding':ctx.rounding,'clamp':ctx.clamp}
        check('Decimal exponent range ample',ctx.Emin<=-10000 and ctx.Emax>=10000 and ctx.clamp==0)
        m.exp=audited_exp
        m.main()
        report['exp_calls']=stats
        a=json.loads(ORIGINAL.read_text());b=json.loads(REPLAY.read_text())
        check('original bytes preserved',hashlib.sha256(ORIGINAL.read_bytes()).hexdigest()==original_hash)
        check('program digest matches',a['program_sha256']==hashlib.sha256(SRC.read_bytes()).hexdigest())
        check('entire replay equals original',a==b)
        check('original PASS no failures',a['status']=='PASS' and not a['failures'])
        check('all analytic checks',all(a['analytic_checks'].values()))
        check('fixed expected mesh',a['N']==262144 and a['X']==2 and a['theta_terms']==4)
        n=a['N'];d=n//2
        check('all cells present',len(a['cells'])==n)
        # Exact positive step envelopes. All moments are accumulated with
        # common integer denominators; the triangle formulas are expressed
        # as positive integer polynomials of the cell index.
        half={j:[0,0] for j in (0,2,4)}
        norm={j:[0,0] for j in (0,2)}
        f0=[0,0];f2=[0,0];bh=[0,0];ba=[0,0]
        for i,c in enumerate(a['cells']):
            assert F(c['l'])==F(i,d) and F(c['r'])==F(i+1,d)
            vals=[F(x)*S for x in c['K']]
            assert all(v.denominator==1 for v in vals)
            lo,hi=map(int,vals)
            assert 0<=lo<=hi
            w={j:(i+1)**(j+1)-i**(j+1) for j in (0,1,2,3,4)}
            for side,k in enumerate((lo,hi)):
                for j in half:half[j][side]+=k*w[j]
                for j in norm:norm[j][side]+=k*k*w[j]
                # BH rectangle denominator 2*S^2*d^3;
                # triangle denominator 6*S^2*d^3.
                bh[side]+=3*k*w[1]*f0[side]+k*k*(3*i+2)
                # BA rectangle /4 has denominator 48*S^2*d^5:
                # 3*k*w3*f0 - 2*k*w1*f2, f2=sum(k*w2).
                # diagonal denominator 240*S^2*d^5.
                rect=15*k*w[3]*f0[side]-10*k*w[1]*f2[side]
                assert rect>=0
                ba[side]+=rect+k*k*(20*i*i+25*i+8)
                f0[side]+=k
                f2[side]+=k*w[2]
        check('all cells partition and bounds audited',True)
        P={j:[F(v,S*(j+1)*d**(j+1)) for v in half[j]] for j in half}
        NN={j:[F(v,S*S*(j+1)*d**(j+1)) for v in norm[j]] for j in norm}
        import math
        T=lambda j:sum(math.comb(j,l)*2**(j-l)*math.factorial(l) for l in range(j+1))
        for j in P:P[j][1]+=F(1,10**29)*T(j)
        for j in NN:NN[j][1]+=F(1,10**58)*T(j)
        BH2=[F(v,6*S*S*d**3) for v in bh];BH2[1]+=181*F(1,10**29)*T(1)
        BA2=[F(v,240*S*S*d**5) for v in ba];BA2[1]+=F(181,4*10**29)*T(3)
        def mul(x,y):
            v=[a*b for a in x for b in y];return [min(v),max(v)]
        def scale(x,q):return [v*q for v in x]
        def sub(x,y):return [x[0]-y[1],x[1]-y[0]]
        def div(x,y):
            assert y[0]>0
            return mul(x,[1/y[1],1/y[0]])
        M={j:scale(x,2) for j,x in P.items()}
        H0=scale(NN[0],2);A0=scale(NN[2],2)
        BH=[scale(mul(M[0],M[0]),F(1,4)),BH2,scale(mul(M[0],M[2]),F(1,8))]
        BA=[scale(mul(M[0],M[2]),F(1,8)),BA2,scale(sub(mul(M[0],M[4]),mul(M[2],M[2])),F(1,32))]
        q=[div(mul(div(x,y),H0),A0) for x,y in zip(BA,BH)]
        D=sub(mul(q[0],q[2]),mul(q[1],q[1]))
        inside=lambda x,y:F(y[0])<=x[0]<=x[1]<=F(y[1])
        check('positive normalizations and integrals',all(v[0]>0 for v in [H0,A0]+BH+BA))
        check('independent half moments inside original',all(inside(P[j],a['positive_half_moments'][str(j)]) for j in P))
        check('independent normalizations inside original',inside(H0,a['H0']) and inside(A0,a['A0']))
        check('independent Mellin integrals inside original',all(inside(x,y) for x,y in zip(BH,a['BH'])) and all(inside(x,y) for x,y in zip(BA,a['BA'])))
        check('independent ratios inside original',all(inside(x,y) for x,y in zip(q,a['q'])))
        check('independent D inside original',inside(D,a['D']))
        check('independent strict finite pass',D[0]>0)
        def outward(x):
            out=[]
            for side,v in enumerate(x):
                z=v*S
                k=z.numerator//z.denominator if side==0 else -((-z.numerator)//z.denominator)
                sign='-' if k<0 else '';u,r=divmod(abs(k),S)
                out.append(f'{sign}{u}.{r:040d}')
            return out
        report['original_values']={k:a[k] for k in ('pi','positive_half_moments','H0','A0','BH','BA','q','D','analytic_checks')}
        report['independent_values']={'H0':outward(H0),'A0':outward(A0),'BH':list(map(outward,BH)),'BA':list(map(outward,BA)),'q':list(map(outward,q)),'D':outward(D)}
        report['threshold']='0'
        report['original_sha256']=original_hash
        report['replay_sha256']=hashlib.sha256(REPLAY.read_bytes()).hexdigest()
        report['source_sha256']=hashlib.sha256(SRC.read_bytes()).hexdigest()
        report['audit_program_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        report['status']='PASS'
    except Exception as e:
        report['failures'].append(repr(e));raise
    finally:
        OUT.write_text(json.dumps(report,indent=2)+'\n')
        print('audit',report['status'],'failures',report['failures'])
        if 'independent_values' in report:print('independent D',report['independent_values']['D'],'required > 0')
        print('full audit:',OUT.relative_to(BASE.parent.parent))
if __name__=='__main__':main()
