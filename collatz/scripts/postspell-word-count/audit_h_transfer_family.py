#!/usr/bin/env python3
"""Independent L084 audit: no import/execution of the construction program.

Reconstruct complete mathematical objects from a separate transcription and
compare every field and every named check, including failed tests. Save full
reconstruction, analytic errors, mismatches and proof-report comparisons.
"""
from fractions import Fraction as F
from itertools import accumulate
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INPUT = HERE / 'h-transfer-family-certificate.json'
OUTPUT = HERE / 'h-transfer-family-audit-certificate.json'
raw = INPUT.read_bytes()
stored = json.loads(raw)
PAIRS = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
         (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
         (8224,39104),(15494,73672),(29191,138802),(54998,261511),
         (103621,492705),(195229,928293),(367827,1748976),
         (693015,3295208),(1305695,6208431),(2460032,11697176),
         (4634896,22038409),(8732512,41522114),(16452748,78230965),
         (30998279,32670621)]
kappa, low, high = F(23,11), F(10584,10**14), F(10585,10**14)
ell, u, v = map(lambda n: F(n,10**12),
                (693147180559,1098612288669,1011600911679))
budget, cap = 9250245, F(20000000000)
failures, proof_checks = [], []
compared = 0


def compare(path, actual, expected):
    """Complete recursive equality, with exact rational rather than float parsing."""
    global compared
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            failures.append(dict(path=path, actual=actual, expected=expected))
            return
        for key in expected:
            compare(path+'/'+str(key), actual[key], expected[key])
    elif isinstance(expected, (list, tuple)):
        if not isinstance(actual, (list, tuple)) or len(actual) != len(expected):
            failures.append(dict(path=path, actual=actual, expected=expected))
            return
        for i, e in enumerate(expected):
            compare(path+'/'+str(i), actual[i], e)
    else:
        compared += 1
        a = F(actual) if isinstance(expected, F) else actual
        if a != expected:
            failures.append(dict(path=path, actual=actual, expected=expected))


def relation(a, op, b):
    return {'>': a > b, '>=': a >= b, '<': a < b,
            '<=': a <= b, '=': a == b}[op]


def prove(name, a, op, b):
    a, b = F(a), F(b)
    ok = relation(a, op, b)
    proof_checks.append(dict(name=name, actual=a, relation=op, required=b,
                             difference=a-b, passed=ok))
    if not ok:
        failures.append(dict(path='proof/'+name, actual=a, relation=op, expected=b))


def logarithm(x, count=100):
    z = (x-1)/(x+1)
    power, terms = z, []
    for k in range(count):
        terms.append(2*power/F(2*k+1))
        power *= z*z
    lo = sum(terms, F(0))
    rem = 2*power/F(2*count+1)/(1-z*z)
    return dict(argument=x, z=z, terms=terms, lower=lo,
                remainder_upper=rem, upper=lo+rem)


logs = {str(x): logarithm(x) for x in (F(2),F(3),F(11,4))}
exp_terms = {}
for t in (24,27):
    seq = [F(1)]
    for k in range(1,41):
        seq.append(seq[-1]*t/k)
    exp_terms[str(t)] = seq
exp_lower = {t: sum(seq,F(0)) for t,seq in exp_terms.items()}
compare('/logs', stored['logs'], logs)
compare('/exp_terms', stored['exp_terms'], exp_terms)
compare('/exp_lower', stored['exp_lower'], exp_lower)
source_path = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
source_raw = source_path.read_bytes()
source_rows = [list(map(int,m)) for m in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', source_raw.decode(), re.M)]
compare('/source/table', source_rows, [[i,*pair] for i,pair in enumerate(PAIRS)])
compare('/source', stored['source'], dict(path=str(source_path.relative_to(ROOT)),
        sha256=hashlib.sha256(source_raw).hexdigest()))
compare('/parameters', stored['parameters'],
        dict(r=25,B=budget,tau=2,m=1,d_min=1,d_max=37))
compare('/assessment', stored['assessment'],
        'drafts/literature/2026-10-19-h-transfer-family-sufficient-tests.md')

fresh = []
for d in range(1,38):
    pairs = list(PAIRS)
    pairs[0] = (8,40-d)
    pairs[24] = (30998279,32670621+d)
    rows = [[i,*pair] for i,pair in enumerate(pairs)]
    odd = [3*j+h for j,h in pairs]
    den = [4*j+h+2 for j,h in pairs]
    aa, dd = list(accumulate(odd,initial=0)), list(accumulate(den,initial=0))
    K, N = aa[-1], dd[-1]+18*budget
    lam = [N*logs['2']['lower']-K*logs['3']['upper'],
           N*logs['2']['upper']-K*logs['3']['lower']]
    prefixes = [dict(i=i,A=aa[i],D_tail2=dd[i]) for i in range(25)]
    checks = {}

    def test(pkg, name, a, op, b):
        a,b = F(a),F(b)
        key = (pkg,name)
        assert key not in checks
        checks[key] = dict(package=pkg,name=name,actual=a,relation=op,
            required=b,difference=a-b,verdict='PASS' if relation(a,op,b) else 'FAIL')

    def interval(pkg,name,a,b):
        assert a <= b
        key = (pkg,name)
        assert key not in checks
        checks[key] = dict(package=pkg,name=name,lower=a,upper=b,
            relation='>',required=F(0),
            verdict='PASS' if a>0 else 'FAIL' if b<=0 else 'INCONCLUSIVE')

    for name,a,op,b in [('K',K,'=',397573379),('N',N,'=',630138897),
        ('sum H',sum(h for j,h in pairs),'=',199390205),
        ('sum J',sum(j for j,h in pairs),'=',66061058),
        ('r lower',25,'>=',3),('budget lower',budget,'>=',0),
        ('cutoff within budget',2,'<=',budget),('survivor maximum',1,'=',min(budget,1)),
        ('complete odd exponent',aa[-1],'=',K),
        ('complete denominator with budget',dd[-1]+18*budget,'=',N)]:
        test('table',name,a,op,b)
    for i,(j,h) in enumerate(pairs):
        test('table',f'row{i} J domain',j,'>=',2)
        test('table',f'row{i} H domain',h,'>=',3)
        if i: test('table',f'row{i} increasing J',j,'>',pairs[i-1][0])
    for pkg in ('O','S','C','H'):
        for name,a,op,b in [('positive lambda lower',low,'>',0),
            ('Lambda lower enclosure',low,'<=',lam[0]),
            ('positive ell',ell,'>',0),('ell below log2',ell,'<=',logs['2']['lower']),
            ('u above log3',u,'>=',logs['3']['upper'])]:
            test(pkg,name,a,op,b)
        if pkg!='H':
            test(pkg,'v above log11over4',2 if pkg=='O' else v,'>=',logs['11/4']['upper'])

    order = dict(lambda_lower=low,T=27,ell=ell,u=u,v=2,cap=25*kappa/low+kappa,
                 offsets=[],margins=[])
    test('O','minimum cap below exp27 lower',order['cap'],'<=',exp_lower['27'])
    for i,(j,h) in enumerate(pairs):
        hf = min(h,72)
        off = F(81-12*F(3,2)**hf,44)
        order['offsets'].append(dict(i=i,H_floor=hf,offset_upper=off,exact_offset=h==hf))
        test('O',f'row{i} offset H floor',h,'>=',hf)
        test('O',f'row{i} tail2 offset upper',off,'<',0)
    for i in range(24):
        margin = (dd[i]+4*pairs[i+1][0])*ell-aa[i]*u-29
        order['margins'].append(dict(k=i,row=i+1,A=aa[i],D=dd[i],margin=margin))
        test('O',f'displacement{i}',margin,'>',0)

    residual_loss = F(552,2**62-23)
    support = dict(lambda_lower=low,U=cap,T=24,ell=ell,u=u,v=v,
        E=residual_loss,residual=low-residual_loss,
        cap=kappa/(low-residual_loss)+kappa,offsets=[],margins=[])
    test('S','residual positive',support['residual'],'>',0)
    test('S','residual root cap',support['cap'],'<=',cap)
    test('S','U below exp24 lower',cap,'<=',exp_lower['24'])
    for i,(j,h) in enumerate(pairs[:23]):
        hf = min(h,72)
        offset = 1+F(12,11)*F(3,2)**hf
        support['offsets'].append(dict(i=i,H_floor=hf,Q_lower=offset,
            exact_Q=hf==h,required=kappa*2**20))
        test('S',f'row{i} offset H floor',h,'>=',hf)
        test('S',f'row{i} tail20 Q lower',offset,'>',kappa*2**20)
        margin=(dd[i+1]+18+4*pairs[i+1][0])*ell-aa[i+1]*u-24-v
        support['margins'].append(dict(j=i,input=i+1,A=aa[i+1],D=dd[i+1],margin=margin))
        test('S',f'recipient{i}',margin,'>',0)

    eta = kappa-F(16,27)**8*(F(12,11)+F(2,3)**(40-d))
    domain = 2/high-2
    for name,a,op,b in [('Lambda upper enclosure',lam[1],'<=',high),
        ('lambda upper below one',high,'<',1),('positive e',2,'>',0),
        ('eta0 bound',eta,'>=',2),('eta_q J comparison',pairs[24][0],'>=',8),
        ('eta_q H comparison',pairs[24][1],'>=',40-d),('uniform domain',domain,'>=',47)]:
        test('C',name,a,op,b)

    scale = F(10**8)*F(2,3)**(d-1)
    lower_products = [F(1),scale]
    while len(lower_products)<25:
        lower_products.append(2*lower_products[-1])
    inverses = [1/x for x in lower_products]
    mass = kappa*sum(inverses,F(0))
    packages = {}
    for pkg,t in [('C',2),('H',1)]:
        tails = [2]*25
        tails[23] += 18*t
        tails[24] += 18*(budget-t)
        row_den = [4*j+h+tail for (j,h),tail in zip(pairs,tails)]
        actual_den = list(accumulate(row_den,initial=0))
        c0 = F(27,16)**8*F(3,2)**(40-d)/4
        factors = [dict(i=0,exact=c0,lower=scale)]
        test(pkg,'row0 c0 >= w',c0,'>=',scale)
        for i in range(1,24):
            lo = odd[i]*logs['3']['lower']-(row_den[i]+1)*logs['2']['upper']
            hi = odd[i]*logs['3']['upper']-(row_den[i]+1)*logs['2']['lower']
            factors.append(dict(i=i,A=odd[i],D=row_den[i],lower=F(2),log_ratio_interval=[lo,hi]))
            interval(pkg,f'row{i} log(c/2)',lo,hi)
        incoming = [dict(i=i,A=aa[i],D=actual_den[i],L=lower_products[i],
                         reciprocal=inverses[i]) for i in range(25)]
        for i in range(25):
            test(pkg,f'incoming{i} positive L',lower_products[i],'>',0)
            test(pkg,f'incoming{i} definition',lower_products[i],'=',
                 F(1) if i==0 else scale*2**(i-1))
            if i:
                test(pkg,f'incoming{i} induction',
                     lower_products[i-1]*factors[i-1]['lower'],'=',lower_products[i])
            test(pkg,f'row{i} tail lower',tails[i],'>=',2)
            test(pkg,f'row{i} tail congruence',tails[i]%18,'=',2)
        denominator = lower_products[24] if pkg=='C' else min(lower_products)
        needed = mass*(1/low+1)+kappa/denominator
        for name,a,op,b in [('full allocated tail sum',sum(tails),'=',50+18*budget),
            ('row23 actual tail',tails[23],'=',38 if pkg=='C' else 20),
            ('row24 actual tail',tails[24],'=',166504376 if pkg=='C' else 166504394),
            ('complete reciprocal cap',mass,'>=',kappa*sum(inverses,F(0))),
            ('normalized cap <= U',needed,'<=',cap),
            ('U below exp24 lower',cap,'<=',exp_lower['24']),
            ('complete closing odd exponent',aa[25],'=',397573379),
            ('complete closing denominator',actual_den[25],'=',N)]:
            test(pkg,name,a,op,b)
        packages[pkg] = dict(t=t,tails=tails,factors=factors,incoming=incoming,
            L=lower_products,L_min=min(lower_products),reciprocal_sum=sum(inverses,F(0)),
            Q=mass,cap_denominator=denominator,required_cap=needed,U=cap,T=24,
            lambda_lower=low,ell=ell,u=u)

    cutoff = aa[24]*u-(packages['C']['incoming'][24]['D']+4*pairs[24][0])*ell+24+v
    packages['C'].update(lambda_upper=high,e=2,eta0=eta,eta_q_lower=eta,
        eta_q_bound='Monotone in J,H; both bases are in (0,1)',domain_lower=domain,
        v=v,cutoff_margin=cutoff)
    test('C','strict cutoff margin',cutoff,'<',0)
    fs = []
    for i,(j,h) in enumerate(pairs):
        pos,neg=aa[i]+3*j,dd[i]+4*j+h
        bound=24+pos*u-neg*ell
        fs.append(dict(i=i,A=aa[i],D_at_0=dd[i],log3_coefficient=pos,
            negative_log2_coefficient=neg,F=bound,rejecting=bound<=0))
    rejected=[x['i'] for x in fs if x['F']<=0]
    packages['H'].update(F=fs,rejected_rows=rejected,
        rejection_test='Some F_i <= 0; evaluated independently of prerequisites')

    old_checks=stored['tables'][d-1]['checks']
    old_map={(x['package'],x['name']):x for x in old_checks}
    prove(f'd{d} unique stored comparison names',len(old_map),'=',len(old_checks))
    compare(f'/tables/{d-1}/checks',old_map,checks)
    # Use the old ordering only for list presentation after exact keyset equality.
    ordered=[checks[key] for key in old_map]
    verdicts={}
    for pkg in ('table','O','S','C','H'):
        status={x['verdict'] for x in checks.values() if x['package']==pkg}
        verdicts[pkg]='FAIL' if 'FAIL' in status else 'INCONCLUSIVE' if 'INCONCLUSIVE' in status else 'PASS'
    failed=[f"{x['package']}: {x['name']}" for x in ordered if x['verdict']=='FAIL']
    unclear=[f"{x['package']}: {x['name']}" for x in ordered if x['verdict']=='INCONCLUSIVE']
    verdict='DATA_TEST_FAILURE' if failed else 'INCONCLUSIVE' if unclear else 'EXCLUDED' if rejected else 'NO_REJECTING_F'
    summary=dict(d=d,verdict=verdict,package_verdicts=verdicts,failures=failed,
        inconclusive=unclear,rejected_rows=rejected,min_O=min(x['margin'] for x in order['margins']),
        min_S=min(x['margin'] for x in support['margins']),cutoff_margin=cutoff,F18=fs[18]['F'],
        O_row0=order['offsets'][0]['offset_upper'],S_row0_Q=support['offsets'][0]['Q_lower'],
        S_required_Q=kappa*2**20,C_required_cap=packages['C']['required_cap'],
        H_required_cap=packages['H']['required_cap'],L_min=min(lower_products),checks=len(checks))
    table=dict(d=d,rows=rows,counts=dict(K=K,N=N),Lambda_interval=lam,w=scale,
        prefixes=prefixes,O=order,S=support,C=packages['C'],H=packages['H'],
        checks=ordered,summary=summary)
    compare(f'/tables/{d-1}',stored['tables'][d-1],table)
    fresh.append(table)

    expected_fail=[]
    if d>=5: expected_fail.append('S: row0 tail20 Q lower')
    if d>=34: expected_fail += ['C: normalized cap <= U','H: normalized cap <= U']
    if d>=36: expected_fail.append('O: row0 tail2 offset upper')
    compare(f'/classification/d{d}/failures',sorted(failed),sorted(expected_fail))
    compare(f'/classification/d{d}/verdict',verdict,'EXCLUDED' if d<=4 else 'DATA_TEST_FAILURE')
    prove(f'd{d} L minimum',min(lower_products),'=',1)
    prove(f'd{d} exact reciprocal identity',sum(inverses,F(0)),'=',1+2/scale*(1-F(1,2**24)))
    prove(f'd{d} F18 closed form',fs[18]['F'],'=',-F(457745289,50000000000)-(d-1)*(u-ell))
    prove(f'd{d} cutoff closed form',cutoff,'=',-F(2102267684691,500000000000)-(d-1)*(u-ell))

success=fresh[:4]
report=dict(certified_min_O=min(x['summary']['min_O'] for x in success),
    certified_min_S=min(x['summary']['min_S'] for x in success),
    certified_max_C_margin=max(x['summary']['cutoff_margin'] for x in success),
    certified_max_H_F18=max(x['summary']['F18'] for x in success),
    certified_max_C_cap=max(x['C']['required_cap'] for x in success),
    certified_max_H_cap=max(x['H']['required_cap'] for x in success),
    all_min_L=min(x['H']['L_min'] for x in fresh),
    all_min_factor_log_ratio=min(f['log_ratio_interval'][0] for x in fresh
        for pkg in ('C','H') for f in x[pkg]['factors'][1:]),
    all_c0_over_w={str(x['d']):x['C']['factors'][0]['exact']/x['w'] for x in fresh})
compare('/report_bounds',stored['report_bounds'],report)
summary=dict(excluded=[1,2,3,4],data_test_failure=list(range(5,38)),inconclusive=[],
             no_rejecting_F=[],checks=sum(len(x['checks']) for x in fresh))
compare('/summary',stored['summary'],summary)
prove('table count',len(stored['tables']),'=',37)
prove('complete comparison count',summary['checks'],'=',21238)
prove('complete failed comparison count',sum(len(x['summary']['failures']) for x in fresh),'=',43)
for name,op,value in [('certified_min_O','>',F(1258,100)),
    ('certified_min_S','>',F(972,100)),('certified_max_C_margin','<',F(-420,100)),
    ('certified_max_H_F18','<',0),('certified_max_C_cap','<',19800000000),
    ('certified_max_H_cap','<',19800000000),('all_min_factor_log_ratio','>',0)]:
    prove(name,report[name],op,value)
for name,value in [('certified_min_O',F(629441541677,50000000000)),
    ('certified_min_S',F(2431999810929,250000000000)),
    ('certified_max_H_cap',F(385875994128308515163014926269,19532705955840000000))]:
    prove('quoted '+name,report[name],'=',value)
for d,value in enumerate([F(-457745289,50000000000),F(-41462001389,100000000000),
                         F(-410042561,500000000),F(-122555023011,100000000000)],1):
    prove(f'quoted F18 d{d}',fresh[d-1]['summary']['F18'],'=',value)
for d,cf,hf in [(34,20011074610,20011074612),(35,20138923465,20138923467),
                (36,20330696747,20330696749),(37,20618356671,20618356673)]:
    for pkg,integer in [('C',cf),('H',hf)]:
        value=fresh[d-1][pkg]['required_cap']
        prove(f'quoted {pkg} cap lower d{d}',value,'>=',integer)
        prove(f'quoted {pkg} cap upper d{d}',value,'<',integer+1)
for d,value in [(36,F(81,176)),(37,F(81,88))]:
    prove(f'quoted O offset d{d}',fresh[d-1]['summary']['O_row0'],'=',value)
prove('quoted S datum d4',fresh[3]['summary']['S_row0_Q'],'=',F(450284094869558387,188978561024))
prove('quoted S datum d5',fresh[4]['summary']['S_row0_Q'],'=',F(150094729786279633,94489280512))
prove('quoted domain',fresh[0]['C']['domain_lower'],'=',F(39999999995766,2117))
prove('row growth floor',F(3**117,2**170),'>',2)
prove('minimum eta',kappa-F(16,27)**8*(F(12,11)+F(2,3)**3),'>',2)
prove('O intermediate cap',fresh[0]['O']['cap'],'<',500000000000)
prove('O exponential lower',exp_lower['27'],'>',500000000000)
prove('H exponential lower',exp_lower['24'],'>',cap)

# Independent cancellation-sensitive analytic evaluation in a different basis.
alternative={str(x):logarithm(x,120) for x in (F(2),F(3,2))}
al=alternative['2']; bl=alternative['3/2']
alt_interval=[232565518*al['lower']-397573379*bl['upper'],
              232565518*al['upper']-397573379*bl['lower']]
prove('alternative Lambda lower',alt_interval[0],'>',fresh[0]['Lambda_interval'][0])
prove('alternative Lambda upper',alt_interval[1],'<',fresh[0]['Lambda_interval'][1])
prove('strict Lambda low',fresh[0]['Lambda_interval'][0],'>',low)
prove('strict Lambda high',fresh[0]['Lambda_interval'][1],'<',high)
prove('strict ell',ell,'<',logs['2']['lower'])
prove('strict u',u,'>',logs['3']['upper'])
prove('strict v',v,'>',logs['11/4']['upper'])
prove('v below two',v,'<',2)
errors=dict(lambda_width=fresh[0]['Lambda_interval'][1]-fresh[0]['Lambda_interval'][0],
    lambda_log2_error=630138897*logs['2']['remainder_upper'],
    lambda_log3_error=397573379*logs['3']['remainder_upper'],
    alternative_interval=alt_interval,
    h_margin_rounding=[dict(d=x['d'],rows=[dict(i=f['i'],
        excess_upper=f['log3_coefficient']*(u-logs['3']['lower'])+
                     f['negative_log2_coefficient']*(logs['2']['upper']-ell),
        excess_lower=f['log3_coefficient']*(u-logs['3']['upper'])+
                     f['negative_log2_coefficient']*(logs['2']['lower']-ell))
        for f in x['H']['F']]) for x in fresh])
for x in errors['h_margin_rounding']:
    for row in x['rows']:
        prove(f"d{x['d']} row{row['i']} outward H error",row['excess_lower'],'>',0)
        prove(f"d{x['d']} row{row['i']} H error order",row['excess_upper'],'>=',row['excess_lower'])

output=dict(input=str(INPUT.relative_to(ROOT)),input_sha256=hashlib.sha256(raw).hexdigest(),
    original_pairs=PAIRS,logs=logs,exp_terms=exp_terms,exp_lower=exp_lower,
    reconstructed_tables=fresh,report_bounds=report,alternative_logs=alternative,
    analytic_errors=errors,proof_checks=proof_checks,mismatches=failures,
    summary=dict(leaf_comparisons=compared,proof_checks=len(proof_checks),
        mismatches=len(failures),constructor_checks=summary['checks'],
        preserved_mathematical_failures=43,excluded=[1,2,3,4],
        data_test_failure=list(range(5,38)),inconclusive=[]))
OUTPUT.write_text(json.dumps(output,indent=2,default=str)+'\n')
print(f'Independent reconstruction: {compared} leaf comparisons; {len(proof_checks)} proof checks; {len(failures)} mismatches.')
print('All 21238 construction comparisons checked; 43 mathematical test failures preserved; no inconclusive interval.')
print('Exclusions: d=1..4; d=5..37: failed prerequisites, no feasibility verdict.')
print(f"O minimum {report['certified_min_O']} >12.58; S minimum {report['certified_min_S']} >9.72.")
print(f"Largest successful H cap {report['certified_max_H_cap']} <19800000000<20000000000.")
print(f"Least-negative certified F18 {report['certified_max_H_F18']} <0; Lambda strictly between 10584/10^14 and 10585/10^14.")
print('Full operands, actual/required bounds, preserved failures and audit mismatches:',OUTPUT.relative_to(ROOT))
if failures:
    print('First mismatch path:',failures[0]['path'])
    raise SystemExit(1)
