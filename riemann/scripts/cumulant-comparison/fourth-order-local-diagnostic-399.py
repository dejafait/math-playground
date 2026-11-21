"""Noncertified confluent integrand diagnostic; not a smoothing theorem."""
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json


def det(a):
    out = D(0)
    for p in permutations(range(4)):
        term = D((-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1,4)))
        for i in range(4):
            term *= a[i][p[i]]
        out += term
    return out


q = [[Q(-3,2), Q(1)]]
for _ in range(6):
    out = [Q(0)] * (len(q[-1])+1)
    for k,c in enumerate(q[-1]):
        out[k] += k*c
        out[k+1] -= c
    q.append(out)


def poly(p,x):
    z = D(0)
    for c in reversed(p):
        z = z*x+D(c.numerator)/D(c.denominator)
    return z


rows = []
with localcontext() as ctx:
    ctx.prec=90
    for a,b in ((22,7),(4,1),(5,1),(8,1)):
        x=D(a)/D(b)
        base=[poly(p,x) for p in q]
        actual=[sum((D(n*n)*(-D(n*n-1)*x).exp()*poly(p,D(n*n)*x)
                     for n in range(1,9)),D(0)) for p in q]
        db=det([[base[i+j] for j in range(4)] for i in range(4)])
        dk=det([[actual[i+j] for j in range(4)] for i in range(4)])
        rows.append({'x':f'{a}/{b}', 'base_normalized':str(db),
                     'truncated_actual_normalized':str(dk),
                     'signed_ratio_K_over_B':str(dk/db),
                     'relative_error':str(abs(dk/db-1))})
result={'status':'NONCERTIFIED DIAGNOSTIC: rounding and n>=9 tail not enclosed',
        'scope':'confluent derivative-integrand comparison only; no m>=7 determinant evaluated',
        'n_max':8,'precision':90,'rows':rows,
        'required':'A uniform integrated relative bound<1/2 for all m>=M4 and u>=0',
        'failures':['Pointwise diagnostic alone cannot prove or refute any smoothing onset.']}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
for r in rows:
    print('x='+r['x']+', integrand K/B~'+r['signed_ratio_K_over_B'][:20]+', |error|~'+r['relative_error'][:20])
print('Required:',result['required'])
print('Limitation:',result['failures'][0])
print('Artifact:',path)
