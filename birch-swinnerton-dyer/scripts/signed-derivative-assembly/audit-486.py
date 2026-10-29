"""Independent finite evidence audit; no producer or kernel integration imported."""
import json, hashlib, math, re, time
from pathlib import Path
from fractions import Fraction as F
OUT=Path('scripts/signed-derivative-assembly/step-486');OUT.mkdir(exist_ok=False)
root=Path('scripts/signed-derivative-assembly/step-484')
seen={}; checks=[]; stage='capture'
def read(p):
 p=str(p); b=Path(p).read_bytes(); h={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 if p in seen: assert seen[p]==h,p
 seen[p]=h
 return json.loads(b) if p.endswith('.json') else b.decode()
def require(v,label):
 if not v: raise ValueError(label)
 checks.append(label)
def q(v):
 require(type(v)==list and len(v)==2 and all(type(x)==int for x in v) and v[1]>0,'integer rational pair')
 return F(v[0],v[1])
def enc(v):return [v.numerator,v.denominator]
report={'start_utc':'2026-10-25 15:14:33 UTC','required_seconds':180,'required_bytes':134217728,'retry':False}
try:
 data=read(root/'selected-inputs.json'); cert=read(root/'certificate.json');pres=read(root/'preservation.json');fin=read(root/'finalization.json');source=read(root.parent/'assemble-484.py')
 for p,h in data['inventory'].items():read(p);require(seen[p]==h,'inventory '+p)
 require(len(data['inventory'])==110 and pres=={'all_match':True,'count':110,'files':data['inventory']},'complete preservation object')
 cp='scripts/finite-derivative-coefficients/certificate.json';co=read(cp);ci=read('scripts/finite-derivative-coefficients/step-410/initial-inventory.json')
 require(seen[cp]==ci[cp] and seen[cp]['sha256']=='9ad5f8b621dab84edeb97b891f5d4ed9cfe6d11c43b1b7b7f8e2b7147780363f','coefficient canonical/audit binding')
 require(co==data['coefficient_certificate'] and co['model']==[0,1,1,-2,0] and co['N']==389 and co['selected_attempt']==0 and co['normalization']=='a_1=1; full untwisted unnormalized newform coefficients','complete coefficient identity')
 require(co['upstream_path']=='scripts/twist-five/certificate.json' and co['upstream_sha256']=='7547b371d675441190256195270c9282213e888cdb666451ae21a062896e4415','upstream identity')
 rows=co['export_indices_1_through_128']; require([r['n'] for r in rows]==list(range(1,129)),'all export indices')
 require(all(type(r['a_n'])==int and r['a_n']==co['coefficients_with_index_zero_sentinel'][r['n']] for r in rows) and rows[0]['a_n']==1,'all coefficient slots')
 D=1<<256; par=read('scripts/first-rational-kernel/step-404/parameter.json');require(par==data['parameter'],'complete embedded parameter')
 cl,cu=(F(x,D) for x in par['c_grid']);delta=(cu-cl)/2
 require(F(3,10)<=cl<=cu<=F(1,2) and q(par['delta'])==delta and q(par['midpoint'])==(cl+cu)/2,'parameter geometry')
 s103=read(next(Path('lemmas').glob('L103-*.md')))
 require(all(str(x) in s103.split('## Conclusion')[0] for x in par['c_grid']),'canonical c endpoints')
 blocks=[(1,1,103,404,406),(2,2,104,412,415),(3,6,105,417,422),(7,10,106,424,446),(11,14,107,431,433),(15,18,108,435,437),(19,22,109,440,442),(23,26,110,449,451),(27,30,111,453,455),(31,34,112,457,459),(35,38,113,461,463),(39,42,114,468,470)]
 require([r['n'] for r in data['selected']]==list(range(1,43)),'selected indices')
 terms=[]; bindings=[]; M=math.lcm(*range(1,43));common=2*D*M
 for lo,hi,lid,prod,audit in blocks:
  lp=next(Path('lemmas').glob(f'L{lid}-*.md'));text=read(lp);con=text.split('## Conclusion')[1].split('## Proof')[0]
  base='scripts/first-rational-kernel' if lo==1 else 'scripts/second-rational-kernel' if lo==2 else 'scripts/four-rational-kernels'
  ai=read(f'{base}/step-{audit}/initial-inventory.json')
  for n in range(lo,hi+1):
   stage=f'binding n={n}'; r=data['selected'][n-1]; kp=f'{base}/step-{prod}'+('' if n<=2 else f'/n-{n}')
   require(r['kernel_path']==kp+'/kernel.json' and r['parameter_path']==kp+'/parameter.json' and r['canonical_lemma']==str(lp) and r['audit']==f'{base}/step-{audit}','independent path map '+str(n))
   k=read(kp+'/kernel.json');p=read(kp+'/parameter.json')
   require(seen[kp+'/kernel.json']==ai[kp+'/kernel.json'] and seen[kp+'/parameter.json']==ai[kp+'/parameter.json'],'original audit binding '+str(n))
   require(p==par and k==r['kernel'],'whole embedded records '+str(n))
   require(k['n']==n and k['grid_denominator']==D and k['complete_panels']==1016,'kernel identity '+str(n))
   l,u=k['final_grid'];require(type(l)==int and type(u)==int and l<=u,'ordered endpoints '+str(n))
   canonical=[int(re.search(r'^'+x+r'\*D = (\d+)',con,re.M)[1]) for x in ['l','u']] if n<=2 else [int(x) for x in re.search(r'^\| '+str(n)+r' \| (\d+) \| (\d+) \|',con,re.M).groups()]
   require(canonical==[l,u],'canonical conclusion endpoints '+str(n))
   j=F(l+u,2*D);e=F(u-l,2*D);a=rows[n-1]['a_n']
   require(q(r['l'])==F(l,D) and q(r['u'])==F(u,D) and q(r['j'])==q(k['midpoint'])==j and q(r['e'])==q(k['radius'])==e and 0<=e<F(1,2**183),'all rational fields '+str(n))
   require(r['a_n']==a and abs(a)<=n,'selected coefficient '+str(n))
   terms.append((n,a,l,u));bindings.append({'n':n,'lemma':str(lp),'audit':r['audit'],'kernel_hash':seen[kp+'/kernel.json'],'parameter_hash':seen[kp+'/parameter.json']})
 stage='independent arithmetic'
 # All accumulation here is integer on a separately fixed common denominator.
 numer=0;lo_num=0;hi_num=0;width_num=0
 for n,a,l,u in terms:
  scale=M//n;numer+=4*a*(l+u)*scale
  x=8*a*l*scale;y=8*a*u*scale
  lo_num+=min(x,y);hi_num+=max(x,y);width_num+=4*abs(a)*(u-l)*scale
 center=F(numer,common);width=F(width_num,common)
 require(F(lo_num,common)==center-width and F(hi_num,common)==center+width,'direct signed integer interval')
 allow={'original_analytic_remainders':F(1,2**43),'full_sum_parameter_transfer':200*delta,'discarded_block':F(130,387*2**14),'retained_kernel_widths':width}
 radius=sum(allow.values(),F(0));left=center-radius;right=center+radius
 for field,val in [('center',center),('radius',radius),('left',left),('right',right),('eta',F(0))]:require(q(cert[field])==val,'exact '+field)
 require(cert['allowances']=={k:enc(v) for k,v in allow.items()},'all allowances')
 require(F(1518612493225,10**12)<left<right<F(1518653498757,10**12),'outward enclosure')
 require(F(20502765,10**12)<radius<F(20502766,10**12)<F(1,2**14) and radius>F(1,2**40),'outward radius and thresholds')
 require(left>0 and cert['positive'] is True and cert['zero_excluded'] is True and cert['radius_below_2^-14'] is True and cert['radius_below_2^-40'] is False,'strict zero exclusion and flags')
 require(cert['comparisons']==dict.fromkeys(['direct_interval','integer_common_denominator','reverse_sum'],True),'comparison flags')
 require(cert['resource_contract_passed'] is False and fin['resource_contract_passed'] is False and fin['observed_elapsed_lower_bound_seconds']>180 and fin['retry'] is False,'historical cap remains failed')
 report.update(verdict='FINITE_CHECKS_PASS_PENDING_WRITTEN_AUDIT',bindings=bindings,integer_common_denominator=common,integer_center_numerator=numer,direct_integer_endpoints=[lo_num,hi_num],center=enc(center),radius=enc(radius),left=enc(left),right=enc(right),allowances={k:enc(v) for k,v in allow.items()},annotation_changes={'status':['ASSEMBLED_REQUIRES_SEPARATE_AUDIT',cert['status']],'added_resource_contract_passed':False},historical_source_identity='Current producer captured; no contemporaneous producer/output hash binding established. Independent audit certifies current finite data, not historical generation.')
except Exception as e:report.update(verdict='STOP',first_failure=str(e),stage=stage)
report['checks']=checks;report['inputs']=seen
for p,h in list(seen.items()):
 b=Path(p).read_bytes();require(h=={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()},'postcheck '+p)
(OUT/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(report['verdict'],report.get('first_failure',''),'; complete evidence:',OUT/'audit.json','; inputs:',len(seen),'; bytes:',(OUT/'audit.json').stat().st_size)
