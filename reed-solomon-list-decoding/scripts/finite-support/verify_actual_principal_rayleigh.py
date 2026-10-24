"""Independent global cell counts, direct small case, exact endpoint replay."""
import gzip
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import factorial
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
SOURCE = B/'actual-principal-rayleigh.json.gz'
OUT = B/'actual-principal-rayleigh-verification.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(q):
    return [q.numerator,q.denominator]


fac = [factorial(k) for k in range(1025)]


def choose(n,k):
    return fac[n]//(fac[k]*fac[n-k]) if 0<=k<=n else 0


def main():
    with gzip.open(SOURCE,'rt') as f:
        s = json.load(f)
    checks=Counter()
    report=dict(stage='in_progress',failures=[],source_sha256=sha(SOURCE),
                code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(checks.values()),checks_by_kind=dict(checks))
        OUT.write_text(json.dumps(report,indent=2)+'\n')

    def ck(kind,ok,detail=None):
        checks[kind]+=1
        if not ok:
            report['stage']='failed'
            report['failures'].append(dict(kind=kind,detail=detail))
            save()
            raise AssertionError((kind,detail))

    ck('constructor',s['stage']=='complete' and not s['failures'] and
       s['code_sha256']==sha(B/'actual_principal_rayleigh.py'))
    for path,digest in s['input_sha256'].items():
        ck('input_binding',sha(ROOT/path)==digest,path)
    for name,code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                      ('l114-critical-audit.json','critical_audit_l114.py'),
                      ('l120-critical-audit.json','critical_audit_l120.py')]:
        a=json.loads((B/name).read_text())
        ck('audit',a['stage']=='verified' and not a['failures'] and a['code_sha256']==sha(B/code))
        for path,digest in a['input_sha256'].items():
            ck('audit_binding',sha(ROOT/path)==digest,path)
    with gzip.open(B/'positive-factor-enclosure.json.gz','rt') as f:
        z=json.load(f)
    rv=json.loads((B/'positive-factor-enclosure-verification.json').read_text())
    audited=json.loads((B/'l120-critical-audit.json').read_text())
    ck('root',z['stage']=='exact_complete' and z['inclusion'] and rv['stage']=='verified' and
       not rv['failures'] and rv['input_sha256']==sha(B/'positive-factor-enclosure.json.gz'))
    ck('all_equations',z['coefficients']==audited['contraction_coefficients'] and
       len(z['coefficients'])==64 and sum(map(len,z['coefficients']))==81355)
    ck('frozen',s['frozen']=={k:z[k] for k in s['frozen']} and
       set(s['frozen'])=={'N','H','Q','radius','point','scale_powers','box'} and
       z['Q']==10**70 and z['radius']==10**25 and len(z['point'])==64)
    box={}
    for k in range(64):
        q=z['point'][k]
        ck('each_root_margin',z['box'][k]==[q-10**25,q+10**25] and
           min(z['krawczyk_image'][k][0]+10**25,10**25-z['krawczyk_image'][k][1])
           ==z['inclusion_margins'][k]==rv['inclusion_margins'][k]>0,k)
        power=z['scale_powers'][k]
        scale=F(10**power) if power>=0 else F(1,10**(-power))
        box[k+5]=[scale*F(q+t*10**25,10**70) for t in (-1,1)]
        ck('each_endpoint',list(map(enc,box[k+5]))==s['endpoints'][str(k+5)] and
           0<box[k+5][0]<box[k+5][1],k)
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    av=[F(q['numerator'],q['denominator']) for q in lp['exact']['primal']]
    N,H=65537**28//2**128+1,choose(1024,68)
    U=F(choose(1024,64),choose(68,64))
    c=[F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*choose(68,i)*choose(956,i))
                            for i in range(5,69)]
    ck('canonical_pairs',min(av)>0 and sum(av)==U-1 and s['N']==z['N']==N and
       s['H']==z['H']==H and s['rho']==enc(F(N,H)) and s['c']==z['c']==list(map(enc,c)) and
       sum(choose(68,i)*choose(956,i)*c[i] for i in range(69))==N)

    # Independent complete direct enumeration includes both marks, all layers,
    # coincidences and the zero-valued vector entries.
    n,w=9,4
    A=set(range(w))
    universe=[set(t) for t in itertools.combinations(range(n),w)]
    direct=Counter()
    for b in universe:
        i=w-len(A&b)
        for d in universe:
            j=w-len(A&d)
            h=w-len(b&d)
            direct[i,j,h]+=(int(0 in b)-int(1 in b))*(int(0 in d)-int(1 in d))
    for i in range(w+1):
        for j in range(w+1):
            same=[0]*(w+1)
            if 1<=i<w and 1<=j<w:
                for a in range(w-1):
                    anchor=choose(w-2,a)*choose(w-2-a,w-i-1-a)*choose(i-1,w-j-1-a)
                    for p in range(w+1):
                        outside=choose(n-w,p)*choose(n-w-p,i-p)*choose(n-w-i,j-p)
                        h=w-1-a-p
                        if 0<=h<=w:
                            same[h]+=2*anchor*outside
            for h in range(w+1):
                expected=same[h]-(same[h-1] if h else 0)
                ck('small_complete_direct',direct[i,j,h]==expected,[i,j,h])

    ni={i:choose(66,67-i)*choose(956,i) for i in range(5,68)}
    ck('all_layers',s['positive_layers']=={str(i):v for i,v in ni.items()} and
       choose(66,-1)==0 and len(s['counts'])==63**2)
    cubic=defaultdict(int)
    histograms=[]
    # Count ordered unmarked pairs by first selecting their common cell,
    # then B-only, then C-only; no fixed-B constructor count is imported.
    table=[[choose(n,k) for k in range(69)] for n in range(957)]
    for i in range(5,68):
        for j in range(5,68):
            same=[0]*69
            for a in range(max(0,68-i-j),min(67-i,67-j)+1):
                anchor=table[66][a]*table[66-a][67-i-a]*table[i-1][67-j-a]
                for p in range(min(i,j)+1):
                    outside=table[956][p]*table[956-p][i-p]*table[956-i][j-p]
                    same[67-a-p]+=2*anchor*outside
            row=s['counts'][(i-5)*63+j-5]
            ck('row_indices',row['i']==i and row['j']==j)
            ck('row_lengths',len(row['positive_C_per_B'])==len(row['ordered_signed'])==69)
            ck('same_class_total',sum(same)==2*ni[i]*ni[j],[i,j])
            signed=[]
            for h in range(69):
                ck('each_unsigned_count',same[h]==2*ni[i]*row['positive_C_per_B'][h],[i,j,h])
                coeff=same[h]-(same[h-1] if h else 0)
                ck('each_ordered_signed_count',coeff==row['ordered_signed'][h],[i,j,h])
                ck('each_diagonal_count',h!=0 or coeff==2*ni[i]*int(i==j),[i,j])
                signed.append(coeff)
                if h>=5:
                    cubic[tuple(sorted((i,j,h)))]+=coeff
            ck('signed_total',sum(signed)==0,[i,j])
            histograms.append(signed)
    for i in range(63):
        for j in range(63):
            ck('every_ordered_transpose',histograms[i*63+j]==histograms[j*63+i],[i,j])
    cubic={k:v for k,v in cubic.items() if v}
    ck('collected_keys',len(cubic)==len(s['cubic']) and
       set(cubic)=={tuple(t['key']) for t in s['cubic']})
    diag=sum(2*ni[i]*c[i] for i in ni)
    ck('diagonal_nonzero_vector',diag>0 and enc(diag)==s['diagonal'] and
       s['vector_norm_squared']==2*sum(ni.values())>0)
    # Independently evaluate each cubic as a positive endpoint product first,
    # then apply its signed integer coefficient.
    positive_lower=positive_upper=negative_lower=negative_upper=F(0)
    for term in s['cubic']:
        key=tuple(term['key'])
        coeff=cubic[key]
        pl=pu=F(1)
        for i in key:
            pl*=box[i][0]
            pu*=box[i][1]
        endpoints=sorted((coeff*pl,coeff*pu))
        ck('each_cubic_coefficient',coeff==term['coefficient'],key)
        ck('each_complete_term_interval',list(map(enc,endpoints))==term['interval'],key)
        if coeff>0:
            positive_lower+=endpoints[0]
            positive_upper+=endpoints[1]
        else:
            negative_lower+=endpoints[0]
            negative_upper+=endpoints[1]
    lo=diag+positive_lower+negative_lower
    hi=diag+positive_upper+negative_upper
    ck('full_interval',lo<=hi and s['quadratic_interval']==list(map(enc,(lo,hi))))
    norm=[lo/diag,hi/diag]
    ck('normalized_interval',s['normalized_interval']==list(map(enc,norm)))
    grid=[(norm[0]*10**6).__floor__(),(norm[1]*10**6).__ceil__()]
    verdict='NEGATIVE_DIRECTION' if hi<0 else 'VECTOR_PARKED_NONNEGATIVE' if lo>=0 else 'ESTIMATE_PARKED_STRADDLE'
    ck('verdict',s['verdict']==verdict and s['normalized_grid']==grid)
    report.update(stage='verified',verdict=verdict,normalized_grid=grid,
                  required_negative_upper=0,grid_denominator=10**6,
                  quadratic_interval=list(map(enc,(lo,hi))),
                  normalized_interval=list(map(enc,norm)),
                  diagonal=enc(diag),collected_cubics=len(cubic),
                  ordered_layer_pairs=len(histograms),direct_small_universe_size=len(universe),
                  signed_partial_sums=list(map(enc,(positive_lower,positive_upper,negative_lower,negative_upper))))
    save()
    print(json.dumps({k:report[k] for k in ['stage','verdict','checks','failures','normalized_grid',
                                          'grid_denominator','required_negative_upper']}))
    print('Certificate: '+str(OUT.relative_to(ROOT)))


if __name__=='__main__':
    main()
