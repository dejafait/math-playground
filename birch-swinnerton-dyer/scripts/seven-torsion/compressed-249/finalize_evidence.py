"""Scoped preservation and actual/required cost summary; no mathematical replay."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent;U=R.parent
manifest=json.loads((R/'original-manifest.json').read_text())
changed=[p for p,h in manifest.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=h]
cost=json.loads((R/'relation-feasibility.json').read_text())
replay=json.loads((R/'final-direction-replay.json').read_text())
reject=json.loads((R/'direction-rejections.json').read_text())
columns=sum(1 for _ in (R/'relation-columns.jsonl').open())
inventory={str(p.relative_to(R)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='final-preservation.json'}
report={'scope':'preservation and cost only; partial relation unverified','upstream_files_checked':len(manifest),'upstream_changed':changed,'direction_replay_passed':replay['passed'],'direction_rejections_passed':reject['passed'],'actual_direction_dimension':replay['dimension'],'required_direction_dimension':8,'actual_relation_columns':columns,'required_relation_columns':336,'column_count_matches':columns==cost['columns'],'actual_stage_seconds':cost['seconds'],'required_stage_seconds':180,'stage_failure':cost['failures'],'target_completed':False,'certificate_bytes_before_this_report':sum(p.stat().st_size for p in R.rglob('*') if p.is_file()),'required_max_bytes':128*1024*1024,'inventory':inventory}
assert not changed and replay['passed'] and reject['passed'] and columns==cost['columns']
(R/'final-preservation.json').write_text(json.dumps(report,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='inventory'}))
