#!/usr/bin/env python3
"""One bounded exact ordered-pair presentation attempt; no incidence claim."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, signal, sys, time

ROOT=Path(__file__).resolve().parent
UP=ROOT.parent
sys.path.insert(0,str(UP))
import build_certificate as P

STAGE_SECONDS=180
BYTE_CAP=128*1024*1024
START=time.monotonic()
REPORT={'schema':'389-incidence-feasibility-v1','status':'IN_PROGRESS',
        'stage_seconds_cap':STAGE_SECONDS,'action_bytes_cap':BYTE_CAP,
        'required_dimensions':{'ordered_pairs':2016,'incidence':336,'lines':48},
        'completed_stages':[],'failures':[], 'target_completed':False}

def enc(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,(list,tuple)): return [enc(x) for x in v]
    if isinstance(v,dict): return {str(k):enc(x) for k,x in v.items()}
    return v

def save(name,obj):
    (ROOT/name).write_text(json.dumps(enc(obj),separators=(',',':'))+'\n')

def journal():
    REPORT['seconds']=round(time.monotonic()-START,3)
    save('feasibility.json',REPORT)

class StageLimit(Exception): pass
def alarm(signum,frame): raise StageLimit('individual exact arithmetic stage exceeded cap')
signal.signal(signal.SIGALRM,alarm)

def stage(label,fn):
    REPORT['active_stage']=label; journal(); t=time.monotonic()
    signal.alarm(STAGE_SECONDS)
    try: result=fn()
    finally: signal.alarm(0)
    REPORT['completed_stages'].append({'label':label,'seconds':round(time.monotonic()-t,3)})
    journal(); print('completed',label,flush=True)
    return result

def main():
    original={str(p.relative_to(UP)):hashlib.sha256(p.read_bytes()).hexdigest()
              for p in UP.rglob('*') if p.is_file() and ROOT not in p.parents
              and '__pycache__' not in p.parts}
    save('upstream-manifest.json',original)
    a=json.loads((UP/'certificate.json').read_text())
    actions=json.loads((UP/'scalar-actions-243/actions.json').read_text())
    f=list(map(F,a['f'])); cubic=[F(46224),F(-3024),F(0),F(1)]
    zero=[F(0)]; one=[F(1)]; x=[F(0),F(1)]
    def red(u): return P.divmodq(u,f)[1]
    def ca(u,v): return P.add(u,v)
    def cs(u,v): return P.sub(u,v)
    def cm(u,v): return red(P.mul(u,v))
    def ci(u):
        gcd,s,t=P.bezout(f,u)
        assert gcd==one
        return red(t)
    def ct(p):
        p=list(p)
        while len(p)>1 and p[-1]==zero:p.pop()
        return p
    def pa(u,v):
        return ct([ca(u[i] if i<len(u) else zero,v[i] if i<len(v) else zero)
                   for i in range(max(len(u),len(v)))])
    def ps(u,v):return pa(u,[P.scale(c,-1) for c in v])
    def pm(u,v):
        r=[zero for _ in range(len(u)+len(v)-1)]
        for i,z in enumerate(u):
            if z!=zero:
                for j,w in enumerate(v):
                    if w!=zero:r[i+j]=ca(r[i+j],cm(z,w))
        return ct(r)
    def ev(u,v):
        z=zero
        for w in reversed(u):z=ca(cm(z,v),w)
        return z
    roots=[]
    for i in [1,2,3]:
        xx=actions['maps'][str(i)]['X']
        assert all(F(z)==0 for z in xx[1])
        roots.append(list(map(F,xx[0])))
    def domain():
        # Monic synthetic division in C[U], not a division in a selected field.
        g=[[z] for z in f]
        for r in roots:
            q=[zero]*(len(g)-1);q[-1]=g[-1]
            for j in range(len(q)-2,-1,-1):q[j]=ca(g[j+1],cm(r,q[j+1]))
            assert ca(g[0],cm(r,q[0]))==zero
            g=ct(q)
        sep=[]
        for i in range(3):
            for j in range(i):
                z=cs(roots[i],roots[j]);w=ci(z)
                assert cm(z,w)==one
                sep.append({'i':i,'j':j,'value':z,'inverse':w})
        r=x
        v=ev(g,r);vi=ci(v)
        q=[zero]*(len(g)-1);q[-1]=g[-1]
        for j in range(len(q)-2,-1,-1):q[j]=ca(g[j+1],cm(r,q[j+1]))
        assert ca(g[0],cm(r,q[0]))==v
        inv=[P.scale(cm(z,vi),-1) for z in q]
        cert={'schema':'389-ordered-pairs-v1','upstream_sha256':hashlib.sha256((UP/'certificate.json').read_bytes()).hexdigest(),
              'actions_sha256':hashlib.sha256((UP/'scalar-actions-243/actions.json').read_bytes()).hexdigest(),
              'f':f,'cubic':cubic,'excluded_x':roots,'excluded_separation':sep,'g':g,
              'g_at_X':v,'g_at_X_inverse':vi,'secant_inverse':inv,
              'basis':{'order':'X^i U^j Y^e V^d, i fastest, then j, e, d',
                       'ranges':[24,21,2,2]},'dimension':2016,
              'claim':'ordered independent pairs only; no quotient or incidence maps'}
        save('ordered-pairs.json',cert)
        return g,inv
    g,inv=stage('ordered_pair_polynomial_and_secant_unit',domain)
    n=len(g)-1
    assert n==21
    REPORT['actual_ordered_pair_dimension']=24*n*4

    def kr(u):
        u=list(u)
        for k in range(len(u)-1,n-1,-1):
            z=u[k]
            if z!=zero:
                for j in range(n):u[k-n+j]=cs(u[k-n+j],cm(z,g[j]))
        return ct(u[:n])
    def km(u,v):return kr(pm(u,v))
    ko=[one];kz=[zero];kx=[x];ku=[zero,one]
    cX=[cubic];cU=[[v] for v in cubic]
    assert km(ps(ku,kx),inv)==ko

    # Elements of S in order 1,Y,V,YV; coefficients in C[U]/g.
    def sm(u,v):
        out=[kz,kz,kz,kz]
        for i,z in enumerate(u):
            if z!=kz:
                for j,w in enumerate(v):
                    if w==kz:continue
                    term=km(z,w)
                    if i&j&1:term=km(term,cX)
                    if i&j&2:term=km(term,cU)
                    out[i^j]=pa(out[i^j],term)
        return out
    def sp(u,n):
        out=[ko,kz,kz,kz]
        for _ in range(n):out=sm(out,u)
        return out
    def sminus(u,v):return [ps(z,w) for z,w in zip(u,v)]
    PX=[kx,kz,kz,kz];PY=[kz,ko,kz,kz]
    QX=[ku,kz,kz,kz];QY=[kz,kz,ko,kz]
    def translation():
        lam=[kz, [P.scale(c,-1) for c in inv],inv,kz]
        xx=sminus(sminus(sm(lam,lam),PX),QX)
        yy=sminus(sm(lam,sminus(PX,xx)),PY)
        save('translation-generators.json',{'X_sum':xx,'Y_sum':yy,
            'convention':'P -> P+Q, Q fixed','secant':'(V-Y)/(U-X)',
            'domain':'all ordered independent pairs','status':'UNVERIFIED'})
        return xx,yy
    xx,yy=stage('first_translation_coordinate_images',translation)
    # Check the group-law curve identity as the first full arithmetic test.
    def curve():
        lhs=sm(yy,yy)
        rhs=sp(xx,3)
        rhs[0]=pa(rhs[0],[[F(46224)]])
        rhs=[pa(z,[[F(-3024)*v for v in c] for c in w]) for z,w in zip(rhs,xx)]
        assert lhs==rhs
        return True
    stage('translation_curve_identity',curve)

    # A streaming complete-column presentation avoids retaining the full matrix.
    def flatten(s):
        return [s[e+2*d][j][i] if j<len(s[e+2*d]) and i<len(s[e+2*d][j]) else F(0)
                for d in range(2) for e in range(2) for j in range(n) for i in range(24)]
    powers=[[ko,kz,kz,kz]]
    out=ROOT/'translation-columns.jsonl'
    byte_count=0;count=0
    with out.open('w') as h:
        for i in range(24):
            if i:
                powers.append(stage('translation_X_power_'+str(i),lambda:sm(powers[-1],xx)))
            for e in range(2):
                z=powers[-1] if not e else stage('translation_X_power_Y_'+str(i),lambda:sm(powers[-1],yy))
                for d in range(2):
                    w=z if not d else [km(z[2],cU),km(z[3],cU),z[0],z[1]]
                    for j in range(n):
                        col=[kr([zero]*j+v) for v in w]
                        line=json.dumps({'input':[i,j,e,d],'values':enc(flatten(col))},separators=(',',':'))+'\n'
                        b=len(line.encode());
                        if byte_count+b>BYTE_CAP:
                            REPORT.update(status='STOP_ACTION_CERTIFICATE_BYTE_CAP',
                                action_bytes_written=byte_count,next_column_bytes=b,action_columns=count,
                                required_action_columns=2016,stopped_before_column=[i,j,e,d])
                            journal();return
                        h.write(line);h.flush();byte_count+=b;count+=1
            REPORT.update(action_bytes_written=byte_count,action_columns=count,required_action_columns=2016)
            journal();print('translation basis X exponent',i,'columns',count,'bytes',byte_count,flush=True)
    REPORT['status']='ACTION_PRODUCED_QUOTIENTS_UNFINISHED'
    journal()

if __name__=='__main__':
    try: main()
    except StageLimit as e:
        REPORT['status']='STOP_ARITHMETIC_STAGE_CAP'
        REPORT['failures'].append({'stage':REPORT.get('active_stage'),'reason':str(e),'required':'finish exact full-domain arithmetic within declared local stage budget'})
        journal()
    except Exception as e:
        REPORT['status']='STOP_PRESENTATION_CHECK_FAILURE'
        REPORT['failures'].append({'stage':REPORT.get('active_stage'),'type':type(e).__name__,'reason':str(e)})
        journal()
        raise
    finally:
        mp=ROOT/'upstream-manifest.json'
        if mp.exists():
            original=json.loads(mp.read_text());changed=[p for p,d in original.items() if not (UP/p).is_file() or hashlib.sha256((UP/p).read_bytes()).hexdigest()!=d]
            save('preservation.json',{'checked':len(original),'changed':changed,'passed':not changed})
        print(json.dumps({'status':REPORT['status'],'actual_pair_dimension':REPORT.get('actual_ordered_pair_dimension'),
              'required_pair_dimension':2016,'failures':REPORT['failures'],
              'certificate':str(ROOT/'ordered-pairs.json'),'report':str(ROOT/'feasibility.json')}),flush=True)
