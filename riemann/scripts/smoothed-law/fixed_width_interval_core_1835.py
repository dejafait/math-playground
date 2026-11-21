"""One finite C033z W=2/W=1 test; rational comparisons only in evaluator.

Fraction normalization is representation of field primitives, not a free
floor/rounding algorithm. Bit inspections and old-data comparisons are
verification only. Full rounding cells and interval recurrences are saved.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter, defaultdict
import json, gzip, hashlib, time

BASE = Path(__file__).resolve().parent
OUT = BASE / 'fixed_width_interval_core_1835.json'
TRACE = BASE / 'fixed_width_interval_core_trace_1835.jsonl.gz'

class Stop(Exception): pass

class VM:
    def __init__(self):
        self.phase = 'constants'
        self.counts = defaultdict(Counter)
        self.max_bits = {'numerator': 0, 'denominator': 0}
        self.max_values = {}
        self.calls = 0
    def track(self, x):
        # Evidence instrumentation only; no branch here affects evaluator.
        if isinstance(x, F):
            for key, value in [('numerator', abs(x.numerator)), ('denominator', x.denominator)]:
                n = value.bit_length()
                if n > self.max_bits[key]:
                    self.max_bits[key] = n; self.max_values[key] = str(x)
        return x
    def op(self, k, a, b):
        self.counts[self.phase][k] += 1; self.calls += 1
        if k == '+': return self.track(a+b)
        if k == '-': return self.track(a-b)
        if k == '*': return self.track(a*b)
        if k == '/':
            # Every evaluator division has its own charged zero test.
            if self.cmp('==', b, F(0)): raise Stop('zero exact divisor')
            return self.track(a/b)
        raise ValueError(k)
    def cmp(self, k, a, b):
        self.counts[self.phase]['comparison'] += 1; self.calls += 1
        return {'<': lambda: a < b, '>': lambda: a > b, '==': lambda: a == b}[k]()
    def add(self,a,b): return self.op('+',a,b)
    def sub(self,a,b): return self.op('-',a,b)
    def mul(self,a,b): return self.op('*',a,b)
    def div(self,a,b): return self.op('/',a,b)


def main():
    if OUT.exists() or TRACE.exists(): raise SystemExit('Preserve evidence: refuses overwrite1835')
    started=time.monotonic(); v=VM(); failure=[]; cert={'status':'RUNNING','failures':failure}
    OUT.write_text(json.dumps(cert)+'\n')
    stream=gzip.open(TRACE,'wt'); trace_counts=Counter(); round_count=0; interval_count=0
    grid_ok=True; divs=[]; max_retained={'numerator':0,'denominator':0}
    def event(kind, obj):
        trace_counts[kind]+=1
        stream.write(json.dumps({'kind':kind, **obj},separators=(',',':'))+'\n')
    # Only 0 and 1 are primitive rational constants; build finite table.
    c=[F(0),F(1)]
    for _ in range(2,257): c.append(v.add(c[-1],c[1]))
    step=c[1]
    for _ in range(256): step=v.div(step,c[2])
    delta=c[1]
    for _ in range(60): delta=v.div(delta,c[2])
    eta=c[1]
    for _ in range(168): eta=v.div(eta,c[2])
    # Fixed conversion range [-64,64], width 2^7, 263 bisections.
    minus64=v.sub(c[0],c[64])
    def gridcheck(x):
        nonlocal grid_ok
        # Verification; never used to select a numerical result.
        grid_ok = grid_ok and (2**256 % x.denominator == 0)
        for k,n in [('numerator',abs(x.numerator).bit_length()),('denominator',x.denominator.bit_length())]:
            max_retained[k]=max(max_retained[k],n)
    def cell(x):
        nonlocal round_count
        start=v.calls
        if v.cmp('<',x,minus64) or v.cmp('>',x,c[64]): raise Stop('conversion range [-64,64]')
        lo,hi=minus64,c[64]; branches=[]
        for _ in range(263):
            mid=v.div(v.add(lo,hi),c[2])
            if v.cmp('<',x,mid): hi=mid; branches.append('0')
            else: lo=mid; branches.append('1')
        round_count+=1; gridcheck(lo); gridcheck(hi)
        event('round',{'id':round_count,'phase':v.phase,'raw':str(x),'lo':str(lo),'hi':str(hi),
                       'branches':''.join(branches),'calls':v.calls-start})
        return lo,hi
    def retain(lo,hi):
        nonlocal interval_count
        a=cell(lo)[0]; b=cell(hi)[1]
        interval_count+=1
        return (a,b)
    def point(x):
        a,b=cell(x); return a,b
    def iop(kind,a,b):
        start_round=round_count; start=v.calls
        if kind=='+': lo,hi=v.add(a[0],b[0]),v.add(a[1],b[1])
        elif kind=='-': lo,hi=v.sub(a[0],b[1]),v.sub(a[1],b[0])
        else:
            if kind=='/':
                # Both tests charged, no short-circuit skipped-test accounting.
                positive=v.cmp('>',b[0],c[0]); negative=v.cmp('<',b[1],c[0])
                divs.append({'phase':v.phase,'interval':[str(t) for t in b],
                             'positive':positive,'negative':negative})
                if not (positive or negative): raise Stop('interval divisor contains zero')
            fun=v.mul if kind=='*' else v.div
            xs=[fun(a[i],b[j]) for i,j in [(0,0),(0,1),(1,0),(1,1)]]
            lo=hi=xs[0]
            for x in xs[1:]:
                if v.cmp('<',x,lo): lo=x
                if v.cmp('>',x,hi): hi=x
        out=retain(lo,hi)
        event('interval',{'op':kind,'phase':v.phase,'a':list(map(str,a)),'b':list(map(str,b)),
                          'out':list(map(str,out)),'round_ids':[start_round+1,round_count],
                          'calls':v.calls-start})
        return out
    def clamp(x):
        if v.cmp('<',x,c[0]): return c[0]
        if v.cmp('>',x,c[1]): return c[1]
        return x
    def iclamp(a):
        out=(clamp(a[0]),clamp(a[1])); event('clamp',{'in':list(map(str,a)),'out':list(map(str,out))})
        return out
    def horner(coeff,x):
        a=coeff[-1]
        for q in reversed(coeff[:-1]): a=v.add(v.mul(a,x),q)
        return a
    def ihorner(coeff,x):
        a=coeff[-1]
        for q in reversed(coeff[:-1]): a=iop('+',iop('*',a,x),q)
        return a
    roots=[]; weights=[]; inputs=[]; contributions={}; sums={}
    try:
        v.phase='reference_construction'
        ps=[[c[1]],[c[0],c[1]]]
        for n in range(1,12):
            a,b=ps[-1],ps[-2]; p=[]
            for k in range(n+2):
                x=a[k-1] if 1<=k<=len(a) else c[0]; y=b[k] if k<len(b) else c[0]
                p.append(v.div(v.sub(v.mul(c[2*n+1],x),v.mul(c[n],y)),c[n+1]))
            ps.append(p)
        grid=[v.div(c[j],c[128]) for j in range(129)]
        values=[horner(ps[12],x) for x in grid]
        seeds=[]
        for j in range(128):
            if v.cmp('<',v.mul(values[j],values[j+1]),c[0]): seeds.append((grid[j],grid[j+1]))
        if len(seeds)!=6: raise Stop('P12 seed count')
        pos=[]
        for lo,hi in seeds:
            sign=v.cmp('>',horner(ps[12],lo),c[0])
            for _ in range(160):
                mid=v.div(v.add(lo,hi),c[2]); value=horner(ps[12],mid)
                if v.cmp('==',value,c[0]): lo=hi=mid
                elif v.cmp('>',value,c[0])==sign: lo=mid
                else: hi=mid
            pos.append((lo,hi))
        brackets=[(v.sub(c[0],hi),v.sub(c[0],lo)) for lo,hi in reversed(pos)]+pos
        roots=[v.div(v.add(lo,hi),c[2]) for lo,hi in brackets]
        for i,r in enumerate(roots):
            p=[c[1]]; den=c[1]
            for k,s in enumerate(roots):
                if k==i: continue
                p=[v.sub(c[0],v.mul(s,p[0]))]+[v.sub(p[j-1],v.mul(s,p[j])) for j in range(1,len(p))]+[p[-1]]
                den=v.mul(den,v.sub(r,s))
            integ=c[0]
            for j in range(0,len(p),2): integ=v.add(integ,v.div(v.mul(c[2],p[j]),c[j+1]))
            weights.append(v.div(integ,den))
        # Complete saved P12 algebraic comparison: verification only.
        old=json.loads((BASE/'direct_positive_real_inputs_1802.json').read_text())['rules'][0]
        replay=(list(map(str,ps[12]))==old['coefficients_ascending'] and
                all(str(lo)==z['left'] and str(hi)==z['right'] and str(r)==z['midpoint'] and str(w)==z['cardinal_weight']
                    for (lo,hi),r,w,z in zip(brackets,roots,weights,old['roots'])))
        isolation=(len(brackets)==12 and all(-1<lo<=hi<1 and (hi-lo)/2<=F(1,2**168)
                    and horner_verify(ps[12],lo)*horner_verify(ps[12],hi)<0 for lo,hi in brackets)
                   and all(brackets[i+1][0]-brackets[i][1]>F(1,32) for i in range(11)))
        if not(replay and isolation): raise Stop('complete P12 replay/isolation')
        cert['reference']={'coefficients':list(map(str,ps[12])),
            'brackets':[[str(x),str(y)] for x,y in brackets],'midpoints':list(map(str,roots)),
            'weights':list(map(str,weights)),'complete_saved_replay':replay,'isolation':isolation}
        v.phase='coefficients'
        facts=[c[1]]
        for n in range(1,42): facts.append(v.mul(facts[-1],c[n]))
        tc=[v.div(c[1],facts[k]) for k in range(41)]
        ec=[]; power=c[1]
        for k in range(1,17):
            power=v.mul(power,c[2]); ec.append(v.div(c[1],v.mul(power,facts[k])))
        uc=[v.div(c[1],facts[2*j+1]) for j in range(1,11)]
        cert['coefficients']={'T40':list(map(str,tc)),'E16':list(map(str,ec)),'U10':list(map(str,uc))}
        ti=list(map(point,tc)); ei=list(map(point,ec)); ui=list(map(point,uc))
        zero=(c[0],c[0]); one=(c[1],c[1]); two=(c[2],c[2]); minus16=(v.sub(c[0],c[16]),)*2
        v.phase='q_construction'
        lo,hi=c[0],c[1]; qbranches=[]
        for _ in range(64):
            mid=v.div(v.add(lo,hi),c[2]); test=v.mul(c[2],v.mul(mid,mid))
            if v.cmp('>',test,c[1]): hi=mid; qbranches.append('0')
            else: lo=mid; qbranches.append('1')
        q=v.div(v.add(lo,hi),c[2]); q=clamp(q)
        cert['q']={'W':'2','qhat':str(q),'bracket':list(map(str,(lo,hi))),
                   'branches':''.join(qbranches),'reference':'1',
                   'verified_squared_exclusion':2*lo*lo<=1<=2*hi*hi and hi-lo==F(1,2**64)}
        if not cert['q']['verified_squared_exclusion']: raise Stop('q enclosure')
        v.phase='input_gaussians'
        gauss_tail=v.div(c[48],facts[41]); node_error=v.div(eta,c[2])
        input_error_max=c[0]
        for panel in range(4):
            for i,r in enumerate(roots):
                x=v.add(c[panel],v.div(v.add(c[1],r),c[2])); w=clamp(v.div(weights[i],c[2]))
                xi=point(x); wi=point(w)
                arg=iop('/',iop('*',xi,xi),minus16)
                g=iclamp(ihorner(ti,arg))
                for _ in range(4): g=iop('*',g,g)
                e=g[0] # Dyadic approximate input; full width charged as error.
                gerr=v.add(v.add(v.sub(g[1],g[0]),gauss_tail),v.mul(c[8],node_error))
                if v.cmp('>',gerr,delta): raise Stop('Gaussian input error exceeds delta')
                if v.cmp('>',gerr,input_error_max): input_error_max=gerr
                data={'panel':panel,'node':i,'xhat':str(x),'what':str(w),'ehat':str(e),
                      'gaussian_poly_interval':list(map(str,g)),'true_gaussian_error':str(gerr),
                      'x_interval':list(map(str,xi)),'weight_interval':list(map(str,wi))}
                inputs.append(data)
        cert['inputs']=inputs; cert['max_gaussian_input_error']=str(input_error_max)
        for W,qhat in [(1,c[1]),(2,q)]:
            v.phase=f'core_W{W}'; qi=(qhat,qhat); total=zero; rows=[]
            for j,data in enumerate(inputs):
                xi=tuple(map(F,data['x_interval'])); wi=tuple(map(F,data['weight_interval'])); e=F(data['ehat'])
                a=iop('*',wi,(e,e)); z=iop('*',xi,qi); z2=iop('*',z,z)
                E=ihorner(ei,z); U=ihorner(ui,z2); T=iop('*',z,U)
                S=iop('+',one,iop('*',z,T)); den=iop('*',two,S)
                A=iop('/',iop('-',E,T),den); term=iop('*',a,A); total=iop('+',total,term)
                rows.append({'index':j,'z':list(map(str,z)),'S10':list(map(str,S)),
                             'divisor':list(map(str,den)),'A':list(map(str,A)),
                             'term':list(map(str,term)),'prefix':list(map(str,total))})
            sums[str(W)]=iop('*',qi,total); contributions[str(W)]=rows
        v.phase='final_error'
        diff=iop('-',sums['2'],sums['1'])
        # Uniform C033z(4),(5),(8), built with charged primitives.
        pow4=c[1]
        for _ in range(22): pow4=v.mul(pow4,c[4])
        dS=v.div(v.div(pow4,facts[23]),v.sub(c[1],v.div(c[16],v.mul(c[24],c[25]))))
        pow2=c[1]
        for _ in range(15): pow2=v.mul(pow2,c[2])
        dE=v.div(v.mul(c[8],pow2),facts[17]); dT=v.div(dS,c[4])
        dR=v.add(v.div(v.add(dE,dT),c[2]),v.mul(c[2],dS))
        # 2048=8*256; input error comparison uses 2*1024*delta.
        error=v.add(v.mul(c[8],dR),v.mul(v.mul(c[8],c[256]),delta))
        final=retain(v.sub(diff[0],error),v.add(diff[1],error))
        rad=v.div(v.sub(final[1],final[0]),c[2]); target=c[1]
        for _ in range(24): target=v.div(target,c[2])
        radius_pass=not v.cmp('>',rad,target)
        center=v.div(v.add(final[0],final[1]),c[2]) # Reporting center; not retained working endpoint.
        cert.update({'contributions':contributions,'sums':{k:list(map(str,t)) for k,t in sums.items()},
            'approximate_difference_interval':list(map(str,diff)),
            'error':{'dE':str(dE),'dS':str(dS),'dT':str(dT),'dR':str(dR),'total_allowance':str(error)},
            'final':{'lo':str(final[0]),'hi':str(final[1]),'radius':str(rad),'center':str(center),
                     'required_radius':str(target),'radius_pass':radius_pass},
            'grid':{'denominators_divide_2_pow_256':grid_ok,'retained_endpoint_max_bits':max_retained},
            'divisors':divs})
        if not radius_pass: raise Stop('final radius exceeds 2^-24')
        if not grid_ok: raise Stop('off-grid retained endpoint')
        cert['status']='FINITE_CORE_PASS_AUDIT_REQUIRED'
    except Stop as exc:
        failure.append(str(exc)); cert['status']='FAILED_SCHEDULE'
        cert.setdefault('inputs',inputs); cert.setdefault('contributions',contributions); cert['divisors']=divs
    finally:
        stream.close()
        cert['ledger']={'unit':'rational +,-,*,/,comparison; exact division includes separate zero comparison',
            'by_phase':{p:dict(ct) for p,ct in v.counts.items()},'total':v.calls,
            'rounding_conversions':round_count,'interval_retains':interval_count,
            'trace_events':dict(trace_counts),'comparison_conversion_each':1054,
            'scope':'fresh P12 generation, coefficients, inputs, W1/W2 core, error and radius; no transferred global cap',
            'verification_excluded':'old-data equality, isolation replay, bit inspection, serialization, hashes, loop indexing/storage'}
        cert['temporary_sizes']={'max_bits':v.max_bits,'max_witness':v.max_values,
            'scope':'all instrumented exact arithmetic and comparison-result operands constructed by evaluator; not an endpoint claim'}
        cert['evidence']={'trace':str(TRACE.relative_to(BASE.parent.parent)),
            'trace_sha256':hashlib.sha256(TRACE.read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'old_P12_sha256':hashlib.sha256((BASE/'direct_positive_real_inputs_1802.json').read_bytes()).hexdigest()}
        cert['elapsed_seconds']=round(time.monotonic()-started,3)
        OUT.write_text(json.dumps(cert,indent=2)+'\n')
        print(cert['status'],'failures:',failure)
        if 'final' in cert:
            print('Radius:',float(F(cert['final']['radius'])),'required <=',2**-24)
            print('Difference center:',float(F(cert['final']['center'])))
        print('Grid pass:',grid_ok,'denominator exponent <=256; interval divisors:',len(divs))
        print('Local primitive count:',v.calls,'conversions:',round_count,'no global cap claimed')
        print('Certificate:',OUT.relative_to(BASE.parent.parent),'trace:',TRACE.relative_to(BASE.parent.parent))


def horner_verify(coeff,x):
    y=F(0)
    for a in reversed(coeff): y=y*x+a
    return y

if __name__=='__main__': main()
