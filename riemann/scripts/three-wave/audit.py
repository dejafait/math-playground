#!/usr/bin/env python3
"""Independent L577 replay; writes complete exact checks to audit.json."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
cert = json.loads((HERE / 'certificate.json').read_text())
checks = {}
def require(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)
def fs(x):
    return str(x.numerator) + '/' + str(x.denominator)

def atan_box(q, terms):
    # Alternating-series enclosure: even partial sum is lower,
    # next (positive) term supplies the upper endpoint.
    assert terms % 2 == 0
    x = F(1, q)
    low = sum(((-1)**k * x**(2*k+1) / (2*k+1)
               for k in range(terms)), F(0))
    return low, low + x**(2*terms+1)/(2*terms+1)

a, aa = atan_box(5, 40)
b, bb = atan_box(239, 40)
pi_low, pi_high = 16*a-4*bb, 16*aa-4*b
require('independent_pi_inside_stored',
        F(cert['pi']['lower']) <= pi_low < pi_high <= F(cert['pi']['upper']))
require('pi_upper_below_22_over_7', pi_high < F(22, 7))
# Exact reconstruction of the old symmetric 32-term enclosure.
a32, a32up = atan_box(5, 32)
b32, b32up = atan_box(239, 32)
require('stored_pi_lower_exact', F(cert['pi']['lower']) == 16*(2*a32-a32up)-4*b32up)
require('stored_pi_upper_exact', F(cert['pi']['upper']) == 16*a32up-4*(2*b32-b32up))
parameters = cert['parameters']
n, nb = parameters['frequency_panels'], parameters['phase_panels']
m, fine = parameters['trig_scale'], parameters['enclosure_scale']
require('parameters', (n, nb, m, fine) == (16, 48, 2**24, 2**50))
require('all_phase_indices', [t['m'] for t in cert['trig_enclosures']] == list(range(nb)))
trig_checks = []
for row in cert['trig_enclosures']:
    index = row['m']
    signed_index = index if index <= nb//2 else index-nb
    factor = F(2*signed_index, nb)
    argument = factor*(pi_low+pi_high)/2
    argument_error = abs(factor)*(pi_high-pi_low)/2
    verified = {'m': index}
    for name, odd in [('cos', 0), ('sin', 1)]:
        # Independent longer polynomial (degree 99) at tighter pi midpoint.
        polynomial = sum(((-1)**k * argument**(2*k+odd)/factorial(2*k+odd)
                          for k in range(50)), F(0))
        error = abs(argument)**100/factorial(100) + argument_error
        exact_low, exact_high = polynomial-error, polynomial+error
        # Retain modest exact outward endpoints, not enormous Taylor fractions.
        audit_scale = 2**80
        low = F((exact_low*audit_scale).__floor__(), audit_scale)
        high = F((exact_high*audit_scale).__ceil__(), audit_scale)
        require(f'{index}_{name}_outward', low <= exact_low <= exact_high <= high)
        entry = row[name]
        old_low, old_high = F(entry['low'], fine), F(entry['high'], fine)
        rounded = F(entry['rounded'], m)
        require(f'{index}_{name}_enclosure', old_low <= low <= high <= old_high)
        actual_error = max(abs(old_low-rounded), abs(old_high-rounded))
        require(f'{index}_{name}_rounding', actual_error == F(entry['error_bound']) <= F(1,m))
        require(f'{index}_{name}_size', abs(rounded) <= 1)
        verified[name] = {'independent_lower': fs(low), 'independent_upper': fs(high),
                          'stored_lower': fs(old_low), 'stored_upper': fs(old_high),
                          'rounded': fs(rounded), 'error': fs(actual_error)}
    trig_checks.append(verified)
source_path = HERE/'tensor_sum.cpp'
source = source_path.read_text()
require('original_source_hash', hashlib.sha256(source_path.read_bytes()).hexdigest() == cert['sum']['source_sha256'])
arrays = re.search(r'c\[nb\]=\{([^}]+)\}, s\[nb\]=\{([^}]+)\}', source)
require('original_arrays_found', arrays is not None)
c = [int(x) for x in arrays.group(1).split(',')]
s = [int(x) for x in arrays.group(2).split(',')]
require('original_cosines', c == [r['cos']['rounded'] for r in cert['trig_enclosures']])
require('original_sines', s == [r['sin']['rounded'] for r in cert['trig_enclosures']])

# Independently expand the rounded polynomial into frequency-square and
# frequency-pair coefficients. Do NOT replace rounded c^2+s^2 by one.
audit_source = r'''
#include <cstdint>
#include <iostream>
#include <string>
using Z = __int128_t;
std::string decimal(Z value) {
    if(value==0) return "0";
    std::string answer;
    while(value>0) {answer.insert(answer.begin(), char('0'+value%10)); value/=10;}
    return answer;
}
int main() {
    const int64_t c[]={COSINES}, s[]={SINES};
    Z totals[17]={}; uint64_t positive[17]={};
    uint64_t nodes=0;
    // Phase-first order, with independent pair expansion; every product
    // is promoted before multiplication to signed 128-bit arithmetic.
    for(int a=0;a<48;++a) for(int b=0;b<48;++b) for(int d=0;d<48;++d) {
        Z A=Z(c[a])*c[a]+Z(s[a])*s[a]+Z(c[a])*c[b]+Z(c[a])*c[d];
        Z B=Z(c[b])*c[b]+Z(s[b])*s[b]+Z(c[b])*c[a]+Z(c[b])*c[d];
        Z C=Z(c[d])*c[d]+Z(s[d])*s[d]+Z(c[d])*c[a]+Z(c[d])*c[b];
        Z AB=2*Z(s[a])*s[b], AC=2*Z(s[a])*s[d], BC=2*Z(s[b])*s[d];
        for(int k=16;k>=0;--k) for(int j=16;j>=0;--j) for(int i=16;i>=0;--i) {
            Z raw=-(i*i*A+j*j*B+k*k*C+i*j*AB+i*k*AC+j*k*BC);
            int weight=(i==0||i==16?1:2)*(j==0||j==16?1:2)*(k==0||k==16?1:2);
            if(raw>0) {totals[i]+=weight*raw; ++positive[i];}
            ++nodes;
        }
    }
    Z total=0; uint64_t positives=0;
    std::cout<<"[";
    for(int i=0;i<=16;++i) {
        if(i) std::cout<<",";
        std::cout<<"{\"i\":"<<i<<",\"weighted_raw\":\""<<decimal(totals[i])
                 <<"\",\"positive_nodes\":"<<positive[i]<<"}";
        total+=totals[i]; positives+=positive[i];
    }
    std::cout<<"]\n"<<decimal(total)<<"\n"<<nodes<<"\n"<<positives<<"\n";
}
'''.replace('COSINES', ','.join(map(str,c))).replace('SINES', ','.join(map(str,s)))
audit_path = HERE/'audit_tensor_sum.cpp'
audit_path.write_text(audit_source)
replays = {}
with tempfile.TemporaryDirectory(prefix='l577-audit-') as temporary:
    for name, path, flags in [('original_sanitized', source_path,
                              ['-fsanitize=undefined', '-fno-sanitize-recover=all']),
                             ('independent_expanded', audit_path, [])]:
        executable = Path(temporary)/name
        subprocess.run(['c++', '-std=c++17', '-O3', *flags, str(path), '-o', str(executable)], check=True)
        replay = subprocess.run([str(executable)], check=True, capture_output=True, text=True)
        require(name+'_no_stderr', not replay.stderr)
        lines = replay.stdout.splitlines()
        require(name+'_complete_output', len(lines)==4)
        slices, total, count, positive = json.loads(lines[0]), int(lines[1]), int(lines[2]), int(lines[3])
        require(name+'_all_slices', slices == cert['sum']['slices'])
        require(name+'_total', total == int(cert['sum']['weighted_raw_total']) == sum(int(t['weighted_raw']) for t in slices))
        require(name+'_nodes', count == cert['sum']['nodes'] == (n+1)**3*nb**3)
        require(name+'_positive_nodes', positive == cert['sum']['positive_nodes'] == sum(t['positive_nodes'] for t in slices))
        replays[name] = {'slices': slices, 'total': str(total), 'nodes': count, 'positive_nodes': positive,
                         'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'stderr': replay.stderr}
        print(name, 'PASS; all', count, 'nodes and 17 slices match', flush=True)

# Bound every class of original 64-bit intermediate, not only final raw.
intermediates = {'frequency_square':n*n, 'x_partial':3*m,
                 'z_summand':n*n*m, 'z_partial':3*n*n*m,
                 'y_summand':n*m, 'y_partial':3*n*m,
                 'xz_product':9*n*n*m*m, 'y_square':9*n*n*m*m,
                 'raw_subtraction':18*n*n*m*m}
require('all_int64_intermediates', max(intermediates.values()) < 2**63)
raw_bound = intermediates['raw_subtraction']
aggregate_bound = 8*(n+1)**3*nb**3*raw_bound
require('aggregate_int128', aggregate_bound < 2**127)
require('stored_overflow_bounds', raw_bound == int(cert['overflow']['absolute_raw_bound']) and aggregate_bound == int(cert['overflow']['absolute_aggregate_bound']))
require('frequency_weights_normalized', sum(1 if i in (0,n) else 2 for i in range(n+1)) == 2*n)
grid = F(2*total,3*(2*n)**5*m*m*nb**3)
require('grid_normalization', grid == F(cert['sum']['grid_value']))
errors = {'trig_rounding':F(6,m), 'frequency_trapezoid':F(1,4*n*n),
          'phase_trapezoid':2*F(22,7)**2/(9*nb*nb)}
require('all_exact_errors', {k:fs(v) for k,v in errors.items()} == cert['bounds']['errors_exact'])
upper = grid+sum(errors.values(), F(0))
required = F(1,288)
require('exact_upper', upper == F(cert['bounds']['expectation_upper']))
require('exact_margin', required-upper == F(cert['bounds']['margin_exact']))
require('threshold', upper < F(13,4000) < required)
report = {'target':'L577 independent full-K and upper-certificate audit',
          'checks':checks, 'trig':trig_checks,
          'pi':{'lower':fs(pi_low),'upper':fs(pi_high),'terms':40},
          'replays':replays, 'original_int64_intermediate_bounds':{k:str(v) for k,v in intermediates.items()},
          'aggregate_bound':str(aggregate_bound),
          'bounds':{'grid':fs(grid),'errors':{k:fs(v) for k,v in errors.items()},
                    'upper':fs(upper),'simple_upper':'13/4000','required':fs(required),
                    'margin':fs(required-upper),'upper_decimal_preview':float(upper)},
          'failures':[]}
output = HERE/'audit.json'
output.write_text(json.dumps(report, indent=2)+'\n')
print('PASS:',len(checks),'exact checks; all 96 trig enclosures independently enclosed')
print('actual exact upper:',fs(upper),'required:',fs(required))
print('upper < 13/4000 < 1/288:',upper < F(13,4000) < required)
print('failures:',report['failures'])
print('complete certificate:',output)
