"""Floating-point rate screen at the proposed u_*; NOT a certificate."""
import json
import math
from pathlib import Path

d, R, U, A, Y = 1.25, 1.375, 121/64, 2.7, .45
p, q = .3, .4
N = 256
omega = A*(math.log(9/5)-.8+1.21*math.log(201/121))

def rate(x, c):
    total = 0.
    for j in range(N+1):
        t = j/N
        value = .5*math.log(
            (((d+p*t)**2+(q*t)**2)*((U*p+(d+c)*t)**2+(U*q-x*t)**2)) /
            (((U*p+d*t)**2+(U*q)**2)*((d+c+p*t)**2+(q*t-x)**2)))
        total += (1 if j in (0,N) else 4 if j%2 else 2)*value
    return total/(3*N)

rows = []
for c in [-.2, -.1, 0, .125, .15, .2, .3, .4]:
    values = [(k/100, rate(k/100, c)) for k in range(-600, 601)]
    x, value = max(values, key=lambda pair:pair[1])
    rows.append(dict(c=c, sampled_maximum=value, maximizing_grid_x=x,
                     bump_upper_screen=value+c*(omega+1/3000)/A,
                     high_frequency_screen=value+c*2.25/A,
                     samples=values))
peak = rate(0,.125)+.125*omega/A
endpoints = dict(negative=rate(-Y,0),positive=rate(Y,0))
tail_rate = max(row['sampled_maximum'] for row in rows if row['c']==0) \
            +math.log(math.sqrt(d*d+Y*Y)/R)/3
result = dict(purpose=__doc__, center=[p,q], omega=omega,
              peak_coefficient_rate=peak, endpoints=endpoints,
              finite_moment_upper_screen=tail_rate, horizontal_lines=rows,
              required='Strict signed peak > paid remainder, tails, and one spatial arc upper rate',
              failures=['Uncertified samples; full real-line enclosure and signed finite-response proof required'])
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'DIAGNOSTIC ONLY: candidate peak rate {peak:.12g}; endpoints {endpoints}; finite moment screen {tail_rate:.12g}')
for row in rows:
    print(f"c={row['c']}: sampled max {row['sampled_maximum']:.12g} at X={row['maximizing_grid_x']}; bump screen {row['bump_upper_screen']:.12g}; high-frequency screen {row['high_frequency_screen']:.12g}")
print(f"Required: {result['required']}; failures: {result['failures']}; full diagnostic: {path}")
