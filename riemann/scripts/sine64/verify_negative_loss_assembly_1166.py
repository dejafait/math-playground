"""Independent exact check of ALL cells in the negative-loss certificate.

Checks assembly from the certified primitive enclosures, not their
transcendental validity; that remains an explicit analytic audit input.
"""
import json
from fractions import Fraction as F
from pathlib import Path

source=Path(__file__).with_name('negative-loss-witness-1166.json')
c=json.loads(source.read_text())
S=int(c['scale'])
cells=c['cells']
checks={'2000_cells':len(cells)==2000,
        'source_checks_pass':not c['failures'] and all(c['checks'].values()),
        'consecutive_indices':[r['k'] for r in cells]==list(range(2000))}
cell_checks=[]
for k,r in enumerate(cells):
    z=r['transform_scaled']
    lo,hi=int(z['lo']),int(z['hi'])
    dist=0 if lo<=0<=hi else min(abs(lo),abs(hi))
    product=(F(1,1000)*F(int(c['parameters']['b']['lo']),S)
             *F(r['loss_cell_lower'])*F(r['amplitude_cell_lower'])**2
             /F(int(c['parameters']['pi']['hi']),S))
    tests={
        'midpoint':F(r['midpoint'])==F(77)+F(2*k+1,2000),
        'loss_lower':F(r['loss_cell_lower'])==max(F(0),F(int(r['v']['lo']),S)-F(109,2000)),
        'amplitude_lower':F(r['amplitude_cell_lower'])==max(F(0),F(dist,S)-F(3,2000)),
        'lower_product':F(int(r['contribution']['lo']),S)<=product,
    }
    cell_checks.append({'k':k,'checks':tests})
summed=sum(int(r['contribution']['lo']) for r in cells)
checks.update({
    'all_cells_pass':all(all(r['checks'].values()) for r in cell_checks),
    'complete_lower_sum':summed==int(c['complete_lower_integral']['lo']),
    'strict_threshold':10*summed>27*S,
})
failures=[key for key,value in checks.items() if not value]
certificate={
    'scope':'Complete exact assembly check; not an independent transcendental enclosure audit.',
    'source':str(source.relative_to(Path.cwd())),
    'actual_lower':str(F(summed,S)), 'required_sufficient_norm_bound':'< beta < 2',
    'compared_lower_threshold':'27/10',
    'checks':checks,'failures':failures,'cell_checks':cell_checks,
}
output=source.with_name('negative-loss-assembly-verification-1166.json')
output.write_text(json.dumps(certificate,indent=2)+'\n')
print(f'All {len(cells)} cells checked; actual lower >27/10, required norm <beta<2.')
print(f'Failures: {failures}; full certificate: {output.relative_to(Path.cwd())}')
raise SystemExit(bool(failures))
