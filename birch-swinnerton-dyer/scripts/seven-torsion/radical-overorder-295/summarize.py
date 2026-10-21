"""Consolidate completed evidence metadata; no mathematical rerun."""
from pathlib import Path
import json
D=Path(__file__).resolve().parent
def read(name):return json.loads((D/name).read_text())
p=read('producer-report.json');v=read('verification-report.json')
pw=read('produce-watchdog.json');vw=read('verify-watchdog.json')
assert p['status']==v['status']=='PASS'
assert not pw['timeout'] and not vw['timeout'] and pw['returncode']==vw['returncode']==0
out={'status':'PASS','producer_internal_seconds':p['seconds'],
 'producer_external_seconds':pw['seconds'],'replay_internal_seconds':v['seconds'],
 'replay_external_seconds':vw['seconds'],'internal_seconds_limit_per_stage':180,
 'external_seconds_limit_per_stage':181,'frobenius_rank_actual_required':[v['frobenius_rank'],46],
 'radical_dimension_actual_required':[v['radical_dimension'],2],
 'action_rank_actual_required':[v['action_rank'],46],
 'action_kernel_dimension_actual_required':[v['action_kernel_dimension'],2],
 'index_actual_required':[v['index'],961],
 'old_product_slots_actual_required':[v['old_product_slots'],110592],
 'integral_action_slots_actual_required':[v['action_slots'],110592],
 'new_product_slots_actual_required':[v['new_product_slots'],110592],
 'replayed_invertible_row_operations':v['row_operations'],
 'original_files_preserved':v['original_files'],'failures':p['failures']+v['failures'],
 'artifact_directory':'scripts/seven-torsion/radical-overorder-295/',
 'full_evidence':['frobenius.json','radical-lattice.json','action-kernel.json',
  'numerator-lattice.json','basis.json','action-00.json through action-47.json',
  'product-00.json through product-47.json','preservation-producer.json','preservation-verifier.json'],
 'byte_limit':134217728}
assert max(p['seconds'],v['seconds'])<=180 and max(pw['seconds'],vw['seconds'])<=181
path=D/'summary.json'
assert not path.exists()
with path.open('x') as f:json.dump(out,f,separators=(',',':'))
size=sum(q.stat().st_size for q in D.iterdir() if q.is_file())
assert size+65536<=out['byte_limit']
print(json.dumps({**out,'aggregate_bytes_after_summary':size,'summary_path':str(path.relative_to(D.parents[2]))}))
