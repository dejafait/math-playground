#!/usr/bin/env python3
"""Exact integer replay of one failed lower-certificate direction, not F."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent
src = P/'joint-entrywise-600.npz'
with np.load(src) as q:
    a = q['partial_comparison_center']
    x = q['partial_lower_direction_direction']
    rows = q['partial_radius_rowsum_upper']
r = float(rows.max())
assert a.shape == (2044,2044) and x.shape == (2044,)
assert np.array_equal(a,a.T)
# One common power-of-two denominator for each saved dyadic array.
xp = [float(t).as_integer_ratio() for t in x]
ex = max(d.bit_length()-1 for _,d in xp)
xx = [n << (ex-(d.bit_length()-1)) for n,d in xp]
nonzero = np.abs(a[a!=0])
em = max(0,53-int(np.frexp(nonzero)[1].min()))
total = 0
for i in range(len(x)):
    n,d = float(a[i,i]).as_integer_ratio()
    total += (n << (em-(d.bit_length()-1)))*xx[i]*xx[i]
    subtotal = 0
    for j in range(i+1,len(x)):
        n,d = float(a[i,j]).as_integer_ratio()
        subtotal += (n << (em-(d.bit_length()-1)))*xx[j]
    total += 2*xx[i]*subtotal
norm2 = Fraction(sum(n*n for n in xx),1 << (2*ex))
center_q = Fraction(total,1 << (em+2*ex))
exact_q = center_q-(Fraction(r)+Fraction(999,1000000))*norm2
report = dict(
    result='NEGATIVE_SAVED_LOWER_DIRECTION' if exact_q<0 else 'NOT_NEGATIVE',
    matrix='partial center minus (saved radius norm upper + exact .000999) I',
    full_dimension=2044,all_entries_used=True,
    exact_quadratic=dict(numerator=str(exact_q.numerator),denominator=str(exact_q.denominator)),
    exact_norm_squared=dict(numerator=str(norm2.numerator),denominator=str(norm2.denominator)),
    decimal_diagnostic=float(exact_q),
    required='>=0 for this sufficient lower comparison',
    failures=[] if exact_q<0 else ['exact lower-direction sign not negative'],
    input_archive_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    qualification='Only the saved partial-output lower certificate; actual F and remaining outputs undecided.')
out = P/'joint-entrywise-direction-replay-600.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(report['result'],'exact full2044-square quadratic <0:',exact_q<0,
      'diagnostic',float(exact_q),'required >=0')
print('Full exact certificate',out)
