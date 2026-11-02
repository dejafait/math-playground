#!/usr/bin/env python3
"""Exact tensor sum with rational trig enclosures; see L577 for errors."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
NF, NB, SCALE, FINE = 16, 48, 2**24, 2**50


def atan_interval(q, n=32):
    x = F(1, q)
    p = sum(((-1)**k * x**(2*k+1) / (2*k+1) for k in range(n)), F(0))
    tail = x**(2*n+1) / (2*n+1)
    return p - tail, p + tail


def trig_interval(x, sine):
    # Taylor through degree 79 (sin), 78 (cos); use the degree-79
    # Taylor remainder in both cases, whose 80th derivative is <=1.
    p = sum(((-1)**k * x**(2*k+int(sine)) /
             factorial(2*k+int(sine)) for k in range(40)), F(0))
    e = abs(x)**80 / factorial(80)
    return p-e, p+e


def factorial(n):
    a = 1
    for k in range(2, n+1):
        a *= k
    return a


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def fs(x):
    return str(x.numerator) + '/' + str(x.denominator)


a0, a1 = atan_interval(5)
b0, b1 = atan_interval(239)
pi_lo, pi_hi = 16*a0-4*b1, 16*a1-4*b0
assert F(314159, 100000) < pi_lo < pi_hi < F(314160, 100000)
assert pi_hi < F(22, 7)
pi_mid = (pi_lo+pi_hi)/2
trig = []
for m in range(NB):
    signed_m = m if m <= NB//2 else m-NB
    x = F(2*signed_m, NB)*pi_mid
    angle_error = F(2*abs(signed_m), NB)*(pi_hi-pi_lo)/2
    row = {'m': m}
    for name, sine in [('cos', False), ('sin', True)]:
        lo, hi = trig_interval(x, sine)
        lo, hi = lo-angle_error, hi+angle_error
        low, high = floor(lo*FINE), ceil(hi*FINE)
        rounded = floor((lo+hi)*SCALE/2+F(1, 2))
        rounded = max(-SCALE, min(SCALE, rounded))
        err = max(abs(F(low, FINE)-F(rounded, SCALE)),
                  abs(F(high, FINE)-F(rounded, SCALE)))
        assert err <= F(1, SCALE)
        row[name] = {'low': low, 'high': high, 'rounded': rounded,
                     'error_bound': fs(err)}
    trig.append(row)

cos_values = ','.join(str(t['cos']['rounded']) for t in trig)
sin_values = ','.join(str(t['sin']['rounded']) for t in trig)
source = r'''
#include <cstdint>
#include <iostream>
#include <string>
using I = __int128_t;
std::string dec(I x) {
    if (!x) return "0";
    std::string s;
    while (x) { s = char('0'+x%10)+s; x/=10; }
    return s;
}
int main() {
    constexpr int nf=NF_VALUE, nb=NB_VALUE;
    const int64_t c[nb]={COS_VALUES}, s[nb]={SIN_VALUES};
    I total=0;
    uint64_t count=0, positive=0;
    std::cout << "[";
    for (int i=0; i<=nf; ++i) {
        I slice=0;
        uint64_t pos_slice=0;
        int wi=(i==0||i==nf)?1:2;
        for (int j=0; j<=nf; ++j) {
            int wj=(j==0||j==nf)?1:2;
            for (int k=0; k<=nf; ++k) {
                int wk=(k==0||k==nf)?1:2;
                int weight=wi*wj*wk;
                for (int a=0; a<nb; ++a)
                for (int b=0; b<nb; ++b)
                for (int d=0; d<nb; ++d) {
                    int64_t x=c[a]+c[b]+c[d];
                    int64_t z=int64_t(i*i)*c[a]+int64_t(j*j)*c[b]
                              +int64_t(k*k)*c[d];
                    int64_t y=int64_t(i)*s[a]+int64_t(j)*s[b]
                              +int64_t(k)*s[d];
                    int64_t raw=-x*z-y*y;
                    if (raw>0) { slice+=I(weight)*raw; ++pos_slice; }
                    ++count;
                }
            }
        }
        total+=slice;
        positive+=pos_slice;
        if(i) std::cout << ",";
        std::cout << "{\"i\":" << i << ",\"weighted_raw\":\""
                  << dec(slice) << "\",\"positive_nodes\":" << pos_slice << "}";
    }
    std::cout << "]\n" << dec(total) << "\n" << count << "\n"
              << positive << "\n";
}
'''
source = source.replace('NF_VALUE', str(NF)).replace('NB_VALUE', str(NB))
source = source.replace('COS_VALUES', cos_values).replace('SIN_VALUES', sin_values)
src = HERE/'tensor_sum.cpp'
src.write_text(source)
with tempfile.TemporaryDirectory(prefix='three-wave-') as temp:
    executable = Path(temp)/'tensor_sum'
    subprocess.run(['c++', '-std=c++17', '-O3', str(src), '-o', str(executable)],
                   check=True)
    out = subprocess.run([str(executable)], check=True,
                         capture_output=True, text=True).stdout.splitlines()
slices, total, count, positive = json.loads(out[0]), int(out[1]), int(out[2]), int(out[3])
assert len(slices) == NF+1
assert sum(int(t['weighted_raw']) for t in slices) == total
assert sum(t['positive_nodes'] for t in slices) == positive
assert count == (NF+1)**3*NB**3
assert all(t['i'] == i for i, t in enumerate(slices))
raw_bound = 18*NF**2*SCALE**2
aggregate_bound = 8*count*raw_bound
assert raw_bound < 2**63
assert aggregate_bound < 2**127
grid = F(2*total, 3*(2*NF)**5*SCALE**2*NB**3)
errors = {'trig_rounding': F(6, SCALE),
          'frequency_trapezoid': F(1, 4*NF**2),
          'phase_trapezoid': 2*F(22, 7)**2/(9*NB**2)}
upper = grid+sum(errors.values(), F(0))
required = F(1, 288)
cert = {
    'target': 'Exact S3 test in 2026-10-31-three-wave-stationary-bulk-review.md',
    'parameters': {'frequency_panels': NF, 'phase_panels': NB,
                   'trig_scale': SCALE, 'enclosure_scale': FINE},
    'pi': {'method': 'Machin: pi=16 atan(1/5)-4 atan(1/239); 32 alternating terms',
           'lower': fs(pi_lo), 'upper': fs(pi_hi),
           'phase_error_upper': '22/7', 'upper_below_22_over_7': pi_hi < F(22, 7)},
    'trig_enclosures': trig,
    'sum': {'slices': slices, 'weighted_raw_total': str(total),
            'grid_value': fs(grid), 'nodes': count, 'positive_nodes': positive,
            'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest()},
    'overflow': {'absolute_raw_bound': str(raw_bound), 'int64_limit': str(2**63),
                 'absolute_aggregate_bound': str(aggregate_bound),
                 'int128_limit': str(2**127), 'passed': True},
    'bounds': {'grid_decimal_preview': float(grid),
               'errors_exact': {k: fs(v) for k, v in errors.items()},
               'errors_decimal_preview': {k: float(v) for k, v in errors.items()},
               'expectation_upper': fs(upper), 'upper_decimal_preview': float(upper),
               'simple_upper': '13/4000',
               'upper_below_simple': upper < F(13, 4000),
               'required': fs(required), 'strictly_below_required': upper < required,
               'margin_exact': fs(required-upper)},
    'failures': [] if upper < required and upper < F(13, 4000) else ['threshold not certified']
}
path = HERE/'certificate.json'
path.write_text(json.dumps(cert, indent=2)+'\n')
print('exact weighted raw total:', total)
print('nodes:', count, 'positive nodes:', positive)
print('grid preview:', float(grid))
print('errors:', {k: float(v) for k, v in errors.items()})
print('actual upper:', float(upper), 'required:', float(required))
print('upper < 13/4000 < 1/288:', upper < F(13, 4000) < required)
print('failures:', cert['failures'])
print('certificate:', path)
