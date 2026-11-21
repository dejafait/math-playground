"""Complete evidence check for1835, not an independent application audit.
Integer grid arithmetic is VERIFICATION ONLY, never the evaluator/ledger.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter, defaultdict
from math import factorial
import gzip, json, hashlib

BASE=Path(__file__).resolve().parent
P=BASE/'fixed_width_interval_core_1835.json'
OUT=BASE/'fixed_width_interval_core_check_1835.json'
H=2**256

def pair(a): return tuple(map(F,a))
def bounds(op,a,b):
    if op=='+': return a[0]+b[0],a[1]+b[1]
    if op=='-': return a[0]-b[1],a[1]-b[0]
    if op=='/': assert b[0]>0 or b[1]<0
    xs=[(x*y if op=='*' else x/y) for x in a for y in b]
    return min(xs),max(xs)
def rnd(x):
    i=x.numerator*H//x.denominator
    return F(i,H),F(i+1,H)
def retain(lo,hi): return rnd(lo)[0],rnd(hi)[1]
def io(op,a,b): return retain(*bounds(op,a,b))
def ihorner(c,x):
    y=c[-1]
    for a in reversed(c[:-1]): y=io('+',io('*',y,x),a)
    return y

def main():
    if OUT.exists(): raise SystemExit('Preserve evidence: refuses overwrite check1835')
    z=json.loads(P.read_text()); checks=Counter(); phases=defaultdict(Counter)
    def check(b,name):
        assert b,name
        checks[name]+=1
    rounds={}; interval_records=[]; counts=Counter(); minus64=F(-64); nround=0
    path=BASE.parent.parent/z['evidence']['trace']
    check(hashlib.sha256(path.read_bytes()).hexdigest()==z['evidence']['trace_sha256'],'trace_hash')
    with gzip.open(path,'rt') as stream:
        for line in stream:
            a=json.loads(line); kind=a['kind']; counts[kind]+=1
            if kind=='round':
                nround+=1; x=F(a['raw']); lo=F(a['lo']); hi=F(a['hi']); bits=a['branches']
                check(a['id']==nround and len(bits)==263 and set(bits)<=set('01'),'conversion_format')
                index=int(bits,2)
                check(lo==minus64+F(index,H) and hi-lo==F(1,H),'conversion_all_branches_cell')
                check(lo<=x and (x<hi or x==hi==64),'conversion_tie_and_containment')
                check(H%lo.denominator==0 and H%hi.denominator==0,'retained_grid')
                check(a['calls']==1054,'conversion_count')
                rounds[nround]=(x,lo,hi); phases[a['phase']]['rounds']+=1
            elif kind=='interval':
                lo,hi=bounds(a['op'],pair(a['a']),pair(a['b'])); k,m=a['round_ids']
                check(m==k+1 and rounds[k][0]==lo and rounds[m][0]==hi,'interval_unrounded_formula')
                check(pair(a['out'])==(rounds[k][1],rounds[m][2]),'interval_round_association')
                cost={'+':2,'-':2,'*':10,'/':16}[a['op']]+2*1054
                check(a['calls']==cost,'interval_count')
                phases[a['phase']][a['op']]+=1; interval_records.append(a)
            else:
                check(kind=='clamp' and pair(a['out'])==tuple(min(F(1),max(F(0),x)) for x in pair(a['in'])),'clamp')
    check(dict(counts)==z['ledger']['trace_events'],'complete_event_count')
    # Independent expression replay with integer grid conversion, all inputs.
    coeff=z['coefficients']; tc=[F(1,factorial(i)) for i in range(41)]
    ec=[F(1,2**i*factorial(i)) for i in range(1,17)]
    uc=[F(1,factorial(2*j+1)) for j in range(1,11)]
    check(list(map(str,tc))==coeff['T40'] and list(map(str,ec))==coeff['E16'] and list(map(str,uc))==coeff['U10'],'every_coefficient')
    ti=list(map(rnd,tc)); ei=list(map(rnd,ec)); ui=list(map(rnd,uc)); inputs=z['inputs']; r=z['reference']
    roots=list(map(F,r['midpoints'])); weights=list(map(F,r['weights']))
    for j,d in enumerate(inputs):
        p,i=divmod(j,12); x=F(p)+(1+roots[i])/2; w=min(F(1),max(F(0),weights[i]/2))
        check((d['panel'],d['node'])==(p,i) and F(d['xhat'])==x and F(d['what'])==w,'input_node_weight_association')
        xi=rnd(x); wi=rnd(w)
        check(xi==pair(d['x_interval']) and wi==pair(d['weight_interval']),'input_conversion')
        g=ihorner(ti,io('/',io('*',xi,xi),(F(-16),F(-16))))
        g=tuple(min(F(1),max(F(0),x)) for x in g)
        for _ in range(4): g=io('*',g,g)
        check(g==pair(d['gaussian_poly_interval']) and F(d['ehat'])==g[0],'complete_gaussian_expression')
        error=g[1]-g[0]+F(48,factorial(41))+F(8,2**169)
        check(error==F(d['true_gaussian_error']) and error<=F(1,2**60),'gaussian_input_radius')
    check(len(inputs)==48,'all_inputs')
    q=F(z['q']['qhat']); qlo,qhi=pair(z['q']['bracket']); lo,hi=F(0),F(1)
    for b in z['q']['branches']:
        mid=(lo+hi)/2; expected='0' if 2*mid*mid>1 else '1'
        check(b==expected,'q_all_branches')
        if b=='0': hi=mid
        else: lo=mid
    check((lo,hi)==(qlo,qhi) and q==(lo+hi)/2 and 2*lo*lo<=1<=2*hi*hi and hi-lo==F(1,2**64),'q_full_contract')
    sums={}; divisor_min=None
    for W,qhat in [(1,F(1)),(2,q)]:
        qi=(qhat,qhat); total=(F(0),F(0)); rows=z['contributions'][str(W)]
        check(len(rows)==48,'all_contributions')
        for j,d in enumerate(inputs):
            xi=pair(d['x_interval']); wi=pair(d['weight_interval']); e=F(d['ehat'])
            a=io('*',wi,(e,e)); x=io('*',xi,qi); x2=io('*',x,x)
            E=ihorner(ei,x); U=ihorner(ui,x2); T=io('*',x,U)
            S=io('+',(F(1),F(1)),io('*',x,T)); den=io('*',(F(2),F(2)),S)
            A=io('/',io('-',E,T),den); term=io('*',a,A); total=io('+',total,term)
            row=rows[j]
            for k,t in [('z',x),('S10',S),('divisor',den),('A',A),('term',term),('prefix',total)]:
                check(pair(row[k])==t,'full_core_expression_'+k)
            check(den[0]>0,'every_core_divisor')
            divisor_min=den[0] if divisor_min is None else min(divisor_min,den[0])
        sums[str(W)]=io('*',qi,total)
        check(sums[str(W)]==pair(z['sums'][str(W)]),'final_width_sum')
    diff=io('-',sums['2'],sums['1']); dS=F(4**22,factorial(23))/(1-F(16,24*25))
    dE=F(8*2**15,factorial(17)); dT=dS/4; dR=(dE+dT)/2+2*dS
    error=8*dR+F(2048,2**60)
    check([F(z['error'][k]) for k in ['dE','dS','dT','dR','total_allowance']]==[dE,dS,dT,dR,error],'all_error_allowances')
    final=retain(diff[0]-error,diff[1]+error); radius=(final[1]-final[0])/2
    check(final==(F(z['final']['lo']),F(z['final']['hi'])) and radius==F(z['final']['radius']) and radius<=F(1,2**24),'complete_final_enclosure')
    check(all((F(d['interval'][0])>0)==d['positive'] and (F(d['interval'][1])<0)==d['negative']
              and (d['positive'] or d['negative']) for d in z['divisors']),'every_saved_interval_divisor')
    # Each conversion: 263 additions/divisions/zero-tests/branch-tests,2 range comparisons.
    # Subtract traced primitive costs; save all remaining exact constructor/error work
    # for application audit instead of silently calling it validated by trace replay.
    residue={}
    for phase,ledger in z['ledger']['by_phase'].items():
        traced=Counter(); pp=phases[phase]; nr=pp['rounds']
        traced['+']+=263*nr; traced['/']+=263*nr; traced['comparison']+=(2*263+2)*nr
        for op in ['+','-']: traced[op]+=2*pp[op]
        traced['*']+=4*pp['*']; traced['comparison']+=6*pp['*']
        traced['/']+=4*pp['/']; traced['comparison']+=12*pp['/']
        remain={k:n-traced[k] for k,n in ledger.items()}
        check(all(n>=0 for n in remain.values()),'local_count_trace_consistency')
        residue[phase]=remain
    check(sum(sum(d.values()) for d in z['ledger']['by_phase'].values())==z['ledger']['total'],'ledger_addition')
    report={'status':'PASS_COMPLETE_EVIDENCE_REPLAY_APPLICATION_AUDIT_PENDING','failures':[],
            'checks':dict(checks),'total_checks':sum(checks.values()),'events_checked':dict(counts),
            'minimum_core_divisor':str(divisor_min),'radius':str(radius),'required_radius':'1/16777216',
            'ledger_total':z['ledger']['total'],'untraced_constructor_and_error_counts':residue,
            'scope':'complete conversions/interval expressions,48 inputs,96 contributions,144 interval divisors; ordinary evidence replay, not independent audit of imported bounds or all constructor counts',
            'certificate_sha256':hashlib.sha256(P.read_bytes()).hexdigest()}
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'],'checks:',report['total_checks'],'failures: []')
    print('Full events:',dict(counts),'all48 inputs/96 contributions/144 interval divisors checked')
    print('Radius:',float(radius),'required <=',2**-24,'minimum quotient divisor:',float(divisor_min))
    print('Certificate:',OUT.relative_to(BASE.parent.parent))

if __name__=='__main__': main()
