#!/usr/bin/env python3
"""Summarize the preserved failed schedule; no new enclosure is produced."""
import json
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=HERE/'certificate.json'; d=json.loads(p.read_text()); D=d['scale']
rows=[]
for i,v in enumerate(d['primitives']):
    width=max(F(t[1]-t[0],D) for t in v['finite_sum'])
    q=v['q']; norm=sum(max(abs(a),abs(b)) for a,b in q)
    rows.append((width,i,norm))
w,i,norm=max(rows)
result={'failed_schedule':{'bits':d['bits'],'T':d['T'],'target_passed':d['result']['passed']},
 'worst_primitive':{'id':i,'x':d['primitives'][i]['x_reduced'],'y':d['primitives'][i]['y'],'H':d['primitives'][i]['H'],
                   'finite_coordinate_width':str(w),'q_rectangle_l1_upper':str(F(norm,D))},
 'required_width':d['result']['required_width'],'actual_normalized_width':d['result']['width'],
 'width_gt_2_to_2000':F(d['result']['width'])>2**2000,
 'all_tail_bounds_le_2_to_minus_38':all(F(v['tail_exact'])<=F(1,2**38) for v in d['primitives']),
 'normalization_period_positive':d['period']['total'][0]>0}
(HERE/'diagnosis.json').write_text(json.dumps(result,indent=2)+'\n')
print('diagnosis: width > 2^2000:',result['width_gt_2_to_2000'],
      'all tails <=2^-38:',result['all_tail_bounds_le_2_to_minus_38'],
      'worst primitive:',i,'H:',d['primitives'][i]['H'],
      'q L1 upper:',F(norm,D),'path:',HERE/'diagnosis.json')
