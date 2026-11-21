#!/usr/bin/env python3
"""Held-out necessary diagnostic of the SAME fixed candidate, no refit."""
from decimal import localcontext
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import numpy as np
p=Path(__file__).with_name('l938-conditioned-endpoints-67.py')
s=importlib.util.spec_from_file_location('fit67',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
OUT=Path(__file__).with_suffix('.json')
def main():
 fitted=Path(__file__).with_name('l938-conditioned-endpoints-67.json')
 prior=Path(__file__).with_name('l938-full-field-screen-66.json')
 data=json.loads(fitted.read_text());old=json.loads(prior.read_text())
 used={tuple(r['t']) for r in data['samples']}
 held=[r for r in old['samples'] if tuple(r['t']) not in used]
 # Genuinely held-out simplex points at both endpoints and the midpoint.
 # One verification of the same fixed candidate, not a second fit.
 energies=(F(1,4),F(17,8),F(4))
 transforms=[{int(k):F(v) for k,v in tr.items()} for tr in data['exact_conditioning']['transforms']]
 coeff=[F(float(x)) for x in data['screen']['coefficients']]
 report={'scope':'necessary held-out evaluation of fixed step67 candidate; no uniform proof or second fit',
  'input_sha256':{str(q.relative_to(m.ROOT)):sha256(q.read_bytes()).hexdigest() for q in (p,Path(__file__),fitted,prior)},
  'energies':list(map(str,energies)),'samples':held,'checks':[],'failures':[]}
 with localcontext() as ctx:
  ctx.prec=80
  t=np.array([[m.dec(F(x)) for x in r['t']] for r in held],dtype=object)
  a,d=m.build_matrix(t,old['Pbar_rows'],old['basis'],transforms,energies)
  residual=d+sum((a[:,j]*m.dec(c) for j,c in enumerate(coeff)),np.full(len(d),m.D(0),dtype=object))
  report['endpoint_and_midpoint']=[]
  for j,E in enumerate(energies):
   rr=residual[j*len(t):(j+1)*len(t)];ix=min(range(len(t)),key=lambda i:rr[i])
   rec={'E':str(E),'minimum':str(rr[ix]),'negative_count':sum(x<0 for x in rr),'minimum_sample_index':ix,'minimum_sample':held[ix]}
   report['endpoint_and_midpoint'].append(rec)
   if rec['negative_count']:report['failures'].append({'name':'necessary held-out sample positivity','E':str(E),'negative_count':rec['negative_count']})
  report['qualification']='80-digit Decimal, eight theta terms; no directed-rounding/tail contract; endpoint/midpoint samples do not cover continuum'
  report['result']='fixed candidate fails necessary held-out diagnostic' if report['failures'] else 'fixed candidate survives this diagnostic only'
  OUT.write_text(json.dumps(report,indent=2)+'\n')
  np.savez_compressed(OUT.with_suffix('.npz'),residual=np.array(residual,dtype=float))
 print(report['result'])
 for row in report['endpoint_and_midpoint']:print('E',row['E'],'minimum',row['minimum'],'negative_count',row['negative_count'])
 print('samples',len(held),'record',OUT.relative_to(m.ROOT))
if __name__=='__main__':main()
