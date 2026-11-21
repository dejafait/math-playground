#!/usr/bin/env python3
"""Independent original-moment and integer Gram/residual replay for740.

No constructor code is imported. Normalized finite power sums and
T_n(2x-3) are regenerated; all saved Gram error entries are checked
by exact integer interval arithmetic. No claimed all-work upper bound.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import comb
from hashlib import sha256
from pathlib import Path
import json
import sys
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve(); INPUT=HERE.with_name('lower-degree-fixed-740.json')
OUT=HERE.with_suffix('.json')
DN=Context(prec=320,rounding=ROUND_FLOOR); UP=Context(prec=320,rounding=ROUND_CEILING)
Z=D(0)
S=10**600

def enclose(f):
    f=F(f)
    return DN.divide(D(f.numerator),D(f.denominator)),UP.divide(D(f.numerator),D(f.denominator))
def add(a,b): return DN.add(a[0],b[0]),UP.add(a[1],b[1])
def scale(a,c):
    c=D(c)
    return (DN.multiply(a[0],c),UP.multiply(a[1],c)) if c>=0 else (DN.multiply(a[1],c),UP.multiply(a[0],c))
def mulpos(a,b): return DN.multiply(a[0],b[0]),UP.multiply(a[1],b[1])
def polys_x(n):
    ps=[[1],[-3,2]]
    for d in range(2,n+1):
        row=[0]*(d+1)
        for i,c in enumerate(ps[-1]): row[i]-=6*c; row[i+1]+=4*c
        for i,c in enumerate(ps[-2]): row[i]-=c
        ps.append(row)
    return ps

def regenerate(J,bern,periodic):
    h=F(1,J); u=1+h/4; v=2+h/4
    raw=[]; power_sums=[]
    for p in range(55):
        val=(v**(p+1)-u**(p+1)-sum((comb(p+1,l)*h**(p-l)*power_sums[l] for l in range(p)),F(0)))/(p+1)
        power_sums.append(val)
    ua,va=F(4*J+1,4),F(8*J+1,4)
    f1=(1/ua-1/va)/2
    f2=1/ua-1/va+(ua**-2-va**-2)/2
    for r in range(1,64):
        f1+=bern[2*r]*(ua**(-2*r)-va**(-2*r))/(2*r)
        f2+=bern[2*r]*(ua**(-2*r-1)-va**(-2*r-1))
    e1=periodic/(128*ua**128); e2=J*periodic/ua**129
    zz=enclose((va-ua)/(va+ua)); zz2=mulpos(zz,zz)
    power=zz; log=(Z,Z)
    for r in range(256):
        term=(DN.divide(power[0],D(2*r+1)),UP.divide(power[1],D(2*r+1)))
        log=add(log,scale(term,2)); power=mulpos(power,zz2)
    log=add(log,(Z,enclose(F(9,4*513*3**513))[1]))
    a=enclose(J*f2); b=enclose(f1)
    # Decimal unary minus would round in the ambient default context;
    # copy_negate preserves the full directed endpoint exactly.
    e2hi,e1hi=enclose(e2)[1],enclose(e1)[1]
    raw=[add(a,(e2hi.copy_negate(),e2hi)),add(add(b,log),(e1hi.copy_negate(),e1hi))]
    raw.extend(enclose(s) for s in power_sums)
    cm=[]
    for p in polys_x(56):
        total=(Z,Z)
        for i,c in enumerate(p): total=add(total,scale(raw[i],c))
        cm.append(tuple(F(t) for t in total))
    return cm

def fixed(value):
    value=F(value)*S
    assert value.denominator==1,'selected common decimal scale insufficient'
    return value.numerator

doc=json.loads(INPUT.read_text())
checks={'constructor_source_binding':doc['script_sha256']==sha256(INPUT.with_suffix('.py').read_bytes()).hexdigest(),'all61_blocks_present':[b['k'] for b in doc['blocks']]==list(range(11,72))}
assert all(checks.values())
R=[[fixed(v) for v in row] for row in doc['anchor_preconditioner']]
rnorm=max(sum(abs(v) for v in row) for row in R)
bern=[F(1)]
for n in range(1,129): bern.append(-sum((comb(n+1,j)*bern[j] for j in range(n)),F(0))/(n+1))
periodic=abs(bern[128])+sum((comb(128,j)*abs(bern[j]) for j in range(129)),F(0))
records=[]; failures=[]; extrema={'contraction':F(0),'epsilon_squared':F(0),'raw_residual':F(0),'minimum_positive_weight':F(100)}
product_terms=0
for block in doc['blocks']:
    k=block['k']; J=2**k
    fresh=regenerate(J,bern,periodic)
    saved=[tuple(F(t) for t in row) for row in block['original_moments']]
    contained=all(a<=c<=d<=b for (a,b),(c,d) in zip(saved,fresh))
    indices=[J+i*(J-1)//128 for i in doc['parameters']['labels']]
    nodes=[F(4*j+1,2*J)-3 for j in indices]
    node_ok=indices==block['indices'] and nodes==[F(v) for v in block['nodes_exact']] and len(set(indices))==35
    hs=[[(saved[i+j][0]+saved[abs(i-j)][0])/2,(saved[i+j][1]+saved[abs(i-j)][1])/2] for i in range(29) for j in range(29)]
    h=[[tuple(fixed(t) for t in hs[i*29+j]) for j in range(29)] for i in range(29)]
    es=block['validation']['error_intervals']
    all_entries=True; exact_row_bounds=[]
    for i in range(29):
        row_sum=0
        for j in range(29):
            lo=hi=0
            for c in range(29):
                r=R[i][c]; a,b=h[c][j]
                lo+=r*(a if r>=0 else b)
                hi+=r*(b if r>=0 else a)
                product_terms+=1
            delta=int(i==j)*S*S
            el,eh=delta-hi,delta-lo
            storedlo,storedhi=(fixed(t)*S for t in es[i][j])
            all_entries &= storedlo<=el<=eh<=storedhi
            row_sum+=max(abs(storedlo),abs(storedhi))
        exact_row_bounds.append(F(row_sum,S*S))
    stored_rows=[F(v) for v in block['validation']['error_row_upper']]
    rows_ok=all(a<=b for a,b in zip(exact_row_bounds,stored_rows))
    e=max(stored_rows)
    e_ok=e==F(block['validation']['contraction_upper']) and e<F(149,1000)
    weights=[F(v) for v in block['weights_decimal']]
    signs=all(w>=0 for w in weights) and sum(w>0 for w in weights)==29
    residual=[F(0)]*29
    for t,w in zip(nodes,weights):
        vals=[F(1),t]
        for d in range(2,29): vals.append(2*t*vals[-1]-vals[-2])
        for d in range(29): residual[d]+=w*vals[d]
    intervals=[(residual[d]-saved[d][1],residual[d]-saved[d][0]) for d in range(29)]
    stored_residual=[tuple(F(v) for v in pair) for pair in block['validation']['residual_intervals']]
    res_ok=all(a<=c<=d<=b for (a,b),(c,d) in zip(stored_residual,intervals))
    z=max(max(abs(a),abs(b)) for a,b in stored_residual)
    z_ok=z==F(block['validation']['raw_residual_upper'])
    bound=29*z*z*F(rnorm,S)/(1-e)
    bound_ok=bound==F(block['validation']['epsilon_squared_upper_exact']) and bound<F(1,10**360)<F(5,10**19)**2
    solver=block['solver']
    caps_ok=solver['state']=='RANK_LIMIT' and solver['main_visits']<=210 and solver['secondary_visits']<=105
    ck={'all57_regenerated_original_moments_contained':contained,'nodes_and_labels_exact':node_ok,'all841_gram_error_entries_enclose_exact_products':all_entries,'all29_row_bounds_valid':rows_ok,'contraction_below_0.149':e_ok,'exact29positive_and6zero':signs,'all29_original_residual_intervals_valid':res_ok,'raw_norm_valid':z_ok,'epsilon_below_1e-180':bound_ok,'candidate_caps':caps_ok}
    for name,passed in ck.items():
        if not passed: failures.append(str(k)+':'+name)
    extrema['contraction']=max(extrema['contraction'],e)
    extrema['epsilon_squared']=max(extrema['epsilon_squared'],bound)
    extrema['raw_residual']=max(extrema['raw_residual'],z)
    extrema['minimum_positive_weight']=min(extrema['minimum_positive_weight'],min(w for w in weights if w>0))
    records.append({'k':k,'checks':ck,'epsilon_squared_upper_exact':str(bound),'gram_contraction_exact':str(e),'raw_residual_exact':str(z)})
    if k%20==11: print('replay through k',k,'failures',len(failures),flush=True)
eps=F(5,10**19)
early=F(2**46)*sum((F(1,4*2**k) for k in range(8,11)),F(0))*(F(1,5**34)+eps*(1+F(1,5**34)))
later=F(2**46)*sum((F(1,4*2**k) for k in range(11,72)),F(0))*(F(1,5**28)+eps*(1+F(1,5**28)))
tail=F(2**46,4*2**72-3)
checks.update({'analytic_complete_sum_exact':str(early+later+tail)==doc['analytic']['total_exact'],'analytic_below_7.291e-8':early+later+tail<F(7291,10**11),'all61_finite_checks':not failures,'all1487729_product_terms':product_terms==61*29**3,'rank2130_inventory':256+3*35+61*29==2130})
for name,passed in checks.items():
    if not passed: failures.append(name)
report={'script_sha256':sha256(HERE.read_bytes()).hexdigest(),'input_sha256':sha256(INPUT.read_bytes()).hexdigest(),'checks':checks,'blocks':records,'extrema_exact':{k:str(v) for k,v in extrema.items()},'failures':failures,'gram_product_terms':product_terms,'complete_work_upper_bound':None,'complete_byte_storage_upper_bound':None,'qualification':'No replay/production/allocation/integer-internal upper ledger; all-cost gate remains open.'}
OUT.write_text(json.dumps(report,indent=2)+'\n')
display=Context(prec=12)
maxeps=extrema['epsilon_squared']
scientific=display.divide(D(maxeps.numerator),D(maxeps.denominator))
print('REPLAY',sum(checks.values()),'/',len(checks),'global;',sum(sum(b['checks'].values()) for b in records),'/',61*10,'block checks; failures',failures,'max epsilon_squared',scientific,'required',str(eps*eps),'certificate',OUT)
