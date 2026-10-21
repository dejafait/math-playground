"""Complete saved-output comparison and shape inspection; no norm arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,sys
R=Path(__file__).resolve().parent;U=R.parent
report={'passed':False,'failures':[],'checks':[],'scope':'Full saved-evidence inspection after the two stages; no arithmetic replay.'}
def read(p):return json.loads(p.read_text())
def need(ok,label):
 if not ok:raise ValueError(label)
 report['checks'].append(label)
def vec(v,n):
 need(len(v)==n,'vector_shape_'+str(n));return tuple(map(Q,v))
def mat(a):
 need(len(a)==7 and all(len(r)==7 for r in a),'full_matrix_shape')
 return tuple(tuple(vec(v,48) for v in row) for row in a)
try:
 for stage,rep in (('build_norms','construction'),('verify_norms','verification')):
  a=read(R/(rep+'-report.json'));b=read(R/(stage+'-watchdog.json'))
  need(a['passed'] and not a['failures'] and not a['changed_or_missing'],'stage_pass_'+stage)
  need(a['seconds']<=180 and b['seconds']<=181 and b['returncode']==0 and not b['watchdog_fired'] and b['failure'] is None,'stage_bounds_'+stage)
 norms=read(R/'supplied-norms.json');verified=read(R/'verification-summary.json')
 pm=read(R/'supplied-matrices.json')['matrices'];vm=read(R/'independent-matrices.json')['matrices']
 labels=('a','b','a_prime','scalar2','zero')
 need(set(pm)==set(vm)==set(norms['norms'])==set(verified['norms'])==set(labels),'exact_five_elements')
 recurrence_count=0;minor_counts={}
 for label in labels:
  need(mat(pm[label])==mat(vm[label]),'all_2352_matrix_coefficients_'+label)
  n=vec(norms['norms'][label],48);need(n==vec(verified['norms'][label],48),'all_48_norm_coefficients_'+label)
  lap=read(R/('laplace-'+label+'.json'));res=read(R/('faddeev-'+label+'-result.json'))
  need(vec(lap['norm'],48)==vec(res['norm'],48)==n,'both_complete_determinants_'+label)
  need(lap['row_rule']=='7 - len(columns)' and vec(lap['empty_minor'],48)==(Q(1),)+(Q(0),)*47,'laplace_conventions_'+label)
  minors={k:vec(v,48) for k,v in lap['ordered_remaining_column_minors'].items()}
  need(minors[','.join(map(str,range(7)))]==n,'laplace_root_'+label);minor_counts[label]=len(minors)
  need(len(res['characteristic_coefficients'])==8 and len(res['recurrence_records'])==7,'complete_characteristic_and_records_'+label)
  coeff=[vec(v,48) for v in res['characteristic_coefficients']]
  ident=tuple(tuple((Q(1),)+(Q(0),)*47 if i==j else (Q(0),)*48 for j in range(7)) for i in range(7))
  prev=ident
  for k,path in enumerate(res['recurrence_records'],1):
   record=read(R/path);need(record['k']==k and path=='faddeev-'+label+'-'+str(k)+'.json','recurrence_order_'+label+'_'+str(k))
   need(mat(record['N_k'])==prev,'complete_adjacent_recurrence_matrices_'+label+'_'+str(k))
   mat(record['A_N_k']);vec(record['trace'],48)
   need(vec(record['c_k'],48)==coeff[k],'every_characteristic_coefficient_'+label+'_'+str(k))
   prev=mat(record['N_next']);recurrence_count+=1
  terminal=mat(res['terminal_zero_matrix'])
  need(terminal==prev and all(not any(v) for row in terminal for v in row),'all_terminal_zero_coefficients_'+label)
  need(tuple(-v for v in coeff[-1])==n,'odd_degree_determinant_sign_'+label)
 for key in ('lhs','rhs'):
  need(vec(norms['representative_change'][key],48)==vec(verified['representative_change'][key],48)==vec(norms['norms']['a_prime'],48),'full_recorded_representative_'+key)
 need(norms['positive_scalar_control']==verified['positive_scalar_control'] and norms['mixed_root_claim'] is False and verified['mixed_root_claim'] is False,'scalar_witness_and_mixed_qualification')
 si=read(R/'supplied-inputs.json')['elements'];pi=read(R/'input-pullbacks.json');vi=read(R/'independent-inputs.json')
 need(set(si)==set(pi)==set(vi['elements'])==set(('a','b','a_prime','scalar2')),'all_unit_input_labels')
 for label,row in si.items():
  for key in ('standard','inverse_standard','power','inverse_power'):vec(row[key],48)
  for key in ('element','inverse'):need(vec(pi[label][key],336)==vec(vi['elements'][label][key],336),'all_input_pullback_coefficients_'+label+'_'+key)
  need(vec(vi['source_products'][label],48)==(Q(1),)+(Q(0),)*47,'complete_source_inverse_product_'+label)
  need(vec(vi['elements'][label]['inverse_product'],336)==(Q(1),)+(Q(0),)*335,'complete_incidence_inverse_product_'+label)
 upstream=read(U/'incidence-269/complete-replay-evidence.json');audit=read(U/'incidence-audit-271/complete-replay-evidence.json');dense=read(U/'incidence-audit-271/dense-evidence.json')
 need(upstream==audit,'complete_accepted_incidence_replay_evidence')
 trans=read(R/'verification-transports.json');ct=read(R/'construction-transports.json')
 for key in ('point_standard_columns','point_power_columns','point_original_x','point_original_y','line_columns'):
  need(trans[key]==upstream[key]==dense[key],'complete_accepted_transport_'+key)
  if key!='line_columns':need(ct[key]==trans[key],'complete_producer_transport_'+key)
 for name in ('producer-rejections.json','rejections.json'):
  rows=read(R/name)
  need(len(rows)==5 and all(row['rejected'] and row['full_malformed_replay'] is False for row in rows),'five_limited_rejections_'+name)
 inv=read(R/'originals.json');changed=[p for p,h in inv.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=h]
 need(not changed,'all_original_hashes_preserved')
 sources=read(R/'source-hashes.json');need(all(hashlib.sha256((R/p).read_bytes()).hexdigest()==h for p,h in sources.items()),'executed_stage_source_hashes_preserved')
 report.update(passed=True,matrix_slots=11760,norm_slots=240,unit_input_count=4,recurrence_records=recurrence_count,laplace_minor_counts=minor_counts,preserved_files=len(inv),changed_or_missing=changed)
except Exception as exc:report['failures'].append(type(exc).__name__+': '+str(exc))
report['bytes_before_inspection_report']=sum(p.stat().st_size for p in R.rglob('*') if p.is_file());report['required_bytes']=134217728
s=json.dumps(report,separators=(',',':'))+'\n'
assert report['bytes_before_inspection_report']+len(s.encode())<=134217728
with (R/'complete-evidence-inspection.json').open('x') as f:f.write(s)
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
sys.exit(0 if report['passed'] else 1)
