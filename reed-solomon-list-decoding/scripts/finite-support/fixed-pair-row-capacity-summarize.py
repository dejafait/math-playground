"""Small exact summary of all 69 already independently verified endpoint sums."""
import json
from fractions import Fraction as F
from pathlib import Path

B=Path(__file__).parent
d=json.loads((B/'fixed-pair-row-capacity-verification.json').read_text())
assert d['verified'] and not d['failures'] and len(d['rows'])==69
N=65537**28//2**128+1
assert d['rows'][0]['required_numerator']==N*d['denominator']
controls=all(r['lower_numerator']==r['required_numerator']==r['upper_numerator']
             for r in d['rows'][:5])
lower_two=all(r['lower_numerator']*N==2*r['required_numerator']
              for r in d['rows'][5:])
assert controls and lower_two and all(r['passes'] for r in d['rows'])
worst=min(d['rows'][5:],key=lambda r:F(r['upper_numerator'],r['required_numerator']))
ratio=F(worst['upper_numerator'],worst['required_numerator'])
floor=ratio.numerator*10**6//ratio.denominator
assert ratio>1 and floor==95274477053795357 and worst['i']==5
report=dict(nonzero_rows=64,all_lower_equal_two_pairs=lower_two,
            minimum_upper_over_required_row=worst['i'],
            minimum_upper_over_required=[ratio.numerator,ratio.denominator],
            minimum_upper_over_required_millionth_floor=floor,required_ratio=1,
            all_controls_collapsed_to_rhs=controls,
            combined_certificate_bytes=sum((B/name).stat().st_size for name in
                ['fixed-pair-row-capacity-results.json','fixed-pair-row-capacity-verification.json']))
out=B/'fixed-pair-row-capacity-summary.json'
out.write_text(json.dumps(report,separators=(',',':'))+'\n')
assert report['combined_certificate_bytes']+out.stat().st_size<256*2**20
print('64 strict row passes; 5 collapsed controls; all lower endpoints = 2*p_i.')
print('Minimum upper/required at i=5; millionth floor:',floor,'; required >=1000000.')
print('Exact summary:',out)
