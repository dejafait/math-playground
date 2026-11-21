"""Exact rational logarithm bounds for the certified finite norm intervals."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

source=Path(__file__).with_name('robin-continuous-residual-certificate.json')
data=json.loads(source.read_text())
assert data['failures']==[] and all(c['passed'] for c in data['checks'])
rows,failures=[],[]


def log_bounds(v):
    assert v>1
    t=(v-1)/(v+1)
    lower=2*sum(t**(2*j+1)/Q(2*j+1) for j in range(80))
    return lower,lower+2*t**161/(161*(1-t*t))


scale=10**7
for row in data['rows']:
    lo,hi=map(Q,row['norm_interval'])
    n=row['n']
    lower=-log_bounds(hi)[1]/n
    upper=-log_bounds(lo)[0]/n
    rounded_lower=Q((lower*scale).__floor__(),scale)
    rounded_upper=Q((upper*scale).__ceil__(),scale)
    passed=rounded_lower<=lower<=upper<=rounded_upper<0<Q(1,100)
    if not passed:
        failures.append(f'q={row["q"]} effective exponent')
    rows.append(dict(q=row['q'],n=n,passed=passed,log_series_terms=80,
                     exact_lower=str(lower),exact_upper=str(upper),
                     outward_decimal_interval=[str(rounded_lower),str(rounded_upper)],
                     required_strict_lower='1/100'))
    print(f'q={row["q"]}: exponent in [{float(rounded_lower):.7f}, '
          f'{float(rounded_upper):.7f}], required >0.0100000')

out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(dict(source_certificate=source.name,
                               source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                               rows=rows,failures=failures),indent=2)+'\n')
print(f'Four exact logarithm checks; failures={failures}; certificate: {out}')
if failures:
    raise SystemExit(1)
