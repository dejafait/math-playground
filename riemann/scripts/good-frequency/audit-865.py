"""Replay C750a with actual-domain guards; preserve the original certificate.

Run: python3 scripts/good-frequency/audit-865.py
Analytic justification is in C750a's conceptual audit. This instruments the
same interval arithmetic; it is not an independent numerical implementation.
"""
from fractions import Fraction as Q
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "corrected-ims/certificate-315.cpp"
WRAPPER = HERE / "fixed-witness-863.cpp"
base = BASE.read_text()
wrapper = WRAPPER.read_text()
source = wrapper.replace('#include "../corrected-ims/certificate-315.cpp"', base)


def change(old, new):
    global source
    assert source.count(old) == 1, old
    source = source.replace(old, new)


change('#include <algorithm>', '#include <algorithm>\n#include <cfenv>')
change(
    'struct I { double l,h; I(double x=0):l(x),h(x){} I(double a,double b):l(a),h(b){} };',
    '''struct I {double l,h;
 I(double x=0):l(x),h(x){if(!isfinite(x))throw runtime_error("nonfinite point");}
 I(double a,double b):l(a),h(b){if(!isfinite(a)||!isfinite(b)||a>b)throw runtime_error("invalid interval");}
};
double trig_max865=0,atan_max865=0,exp_base_max865=0;
double log_min865=2,log_max865=1,exp_min865=0,exp_max865=0;
double symbol_min865=0,symbol_max865=0;
int symbol_calls865=0,exp_clips865=0;
''')
change('if(x < -100) return {0,4e-44};',
       '''exp_min865=min(exp_min865,x);exp_max865=max(exp_max865,x);
 if(x < -100){exp_clips865++;return {0,4e-44};}''')
change('while(abs(z)>.125){z*=.5;k++;}',
       '''while(abs(z)>.125){double prev=z;z*=.5;
 if(z*2!=prev)throw runtime_error("inexact power-of-two scaling");k++;}''')
change('I v(z),sum(1),term(1);',
       '''exp_base_max865=max(exp_base_max865,abs(z));
 if(abs(z)>.125)throw runtime_error("exp base");I v(z),sum(1),term(1);''')
change('I logUnit(I x){I t=',
       '''I logUnit(I x){if(x.l<1||x.h>2)throw runtime_error("log base");
 log_min865=min(log_min865,x.l);log_max865=max(log_max865,x.h);I t=''')
change('I atanSmall(I x){I t=',
       '''I atanSmall(I x){atan_max865=max(atan_max865,max(abs(x.l),abs(x.h)));
 if(atan_max865>.25)throw runtime_error("atan domain");I t=''')
for fn in ('sinSmall', 'cosSmall'):
    change(f'I {fn}(I x){{I term',
           f'''I {fn}(I x){{trig_max865=max(trig_max865,max(abs(x.l),abs(x.h)));
 if(trig_max865>4)throw runtime_error("trig domain");I term''')
change('I symbol(I xi){int shift=xi.l<512?256:0;',
       '''I symbol(I xi){symbol_calls865++;symbol_min865=min(symbol_min865,xi.l);
 symbol_max865=max(symbol_max865,xi.h);int shift=xi.l<512?256:0;
 if(shift!=256)throw runtime_error("unexpected digamma recurrence branch");''')
change('int main(){try{\n if(!numeric_limits<double>::is_iec559)',
       '''int main(){try{
 if(fegetround()!=FE_TONEAREST||numeric_limits<double>::digits!=53||numeric_limits<double>::radix!=2)
   throw runtime_error("binary64 environment");
 volatile double tiny=numeric_limits<double>::denorm_min(),one=1;
 if(!(tiny*one>0))throw runtime_error("subnormals flushed");
 if(!numeric_limits<double>::is_iec559)''')
change(' cerr<<setprecision(12)<<"Status: "',
       ''' ofstream dom("scripts/good-frequency/domains-865.json");dom<<setprecision(17);
 dom<<"{\\"status\\":\\"PASS\\",\\"round_to_nearest_binary64\\":true,\\"subnormals_preserved\\":true,"
    <<"\\"finite_ordered_intervals\\":true,\\"exact_binary_scaling\\":true,"
    <<"\\"trig_max\\":"<<trig_max865<<",\\"trig_required\\":4,"
    <<"\\"atan_max\\":"<<atan_max865<<",\\"atan_required\\":0.25,"
    <<"\\"exp_base_max\\":"<<exp_base_max865<<",\\"exp_required\\":0.125,"
    <<"\\"exp_input_range\\":["<<exp_min865<<","<<exp_max865<<"],\\"exp_clips\\":"<<exp_clips865<<","
    <<"\\"log_base_range\\":["<<log_min865<<","<<log_max865<<"],\\"log_required\\":[1,2],"
    <<"\\"symbol_calls\\":"<<symbol_calls865<<",\\"symbol_xi_range\\":["<<symbol_min865<<","<<symbol_max865<<"],"
    <<"\\"all_symbol_shifts\\":256,\\"pi\\":["<<PI.l<<","<<PI.h<<"],\\"failures\\":[]}\\n";
 cerr<<setprecision(12)<<"Status: "''')

generated = HERE / 'instrumented-865.cpp'
generated.write_text(source)
binary = '/private/tmp/riemann-good-frequency-audit-865'
subprocess.run(['clang++', '-O2', '-std=c++17', '-ffp-contract=off',
                str(generated), '-o', binary], check=True)
with (HERE / 'replay-865.json').open('w') as out:
    subprocess.run([binary], stdout=out, check=True)

original = json.loads((HERE / 'fixed-witness-863.json').read_text())
replay = json.loads((HERE / 'replay-865.json').read_text())
domains = json.loads((HERE / 'domains-865.json').read_text())


def prime_base(n):
    p = next((k for k in range(2, isqrt(n)+1) if n % k == 0), n)
    m = n
    while m % p == 0:
        m //= p
    return p if m == 1 else None


expected = [(n, prime_base(n)) for n in range(2, 81) if prime_base(n)]
actual = [(z['n'], z['prime']) for z in replay['prime_powers']]
boxes = replay['positive_bad_boxes']
skip = replay['skipped_boxes']
indices = list(range(16))+[45,46]
mass_checks = []
pi_lo, pi_hi = map(Q, domains['pi'])
for box in boxes:
    lo, hi = map(Q, box['centered_fourier'])
    s_lo = Q(0) if lo <= 0 <= hi else min(lo*lo, hi*hi)
    s_hi = max(lo*lo, hi*hi)
    # Reflected pair, exact nominal width: 2*(1/32)/(2*pi).
    mass_checks.append(Q(box['paired_mass'][0]) <= s_lo/(32*pi_hi)
                       and Q(box['paired_mass'][1]) >= s_hi/(32*pi_lo))

remainder_pairs = {
    'exp': (2*Q(1,8)**19/factorial(19), Q(1,2**100)),
    'log': (2*Q(1,3)**121/(121*(1-Q(1,9))), Q(1,2**180)),
    'atan': (Q(1,4)**181/181, Q(1,2**300)),
    'sin': (Q(4)**67/factorial(67), Q(1,2**160)),
    'cos': (Q(4)**66/factorial(66), Q(1,2**150)),
}
remainders = {k: {'bound': str(b), 'allowance': str(a),
                  'bound_over_allowance': str(b/a), 'pass': b<a}
              for k,(b,a) in remainder_pairs.items()}
e100_lower = sum((Q(100)**j/factorial(j) for j in range(257)), Q(0))
clip_product = e100_lower*Q(4e-44)
remainders['exp_clip'] = {'exp100_positive_partial_sum': str(e100_lower),
                         'stored_upper': str(Q(4e-44)),
                         'product': str(clip_product), 'pass': clip_product>1}
N = Q(replay['norm_squared'][1])
b = Q(replay['bad_mass_enclosure'][0])
m0 = Q(replay['m0'])
checks = {
    'instrumented_output_identical': replay == original,
    'actual_domains_pass': domains['status']=='PASS' and not domains['failures'],
    'all_31_prime_powers_once_with_correct_bases': actual == expected and len(expected)==31,
    'positive_moment_denominator': replay['M_plus_phi1'][0]>0,
    'strict_positive_norm': replay['norm_squared'][0]>0,
    'retained_exact_nominal_panels': [z['t'] for z in boxes] == [[j/32,(j+1)/32] for j in indices],
    'skipped_exact_nominal_panels': [z[:2] for z in skip] == [[j/32,(j+1)/32] for j in range(16,45)],
    'all_retained_symbol_upper_below_one': all(z['w'][1]<1 for z in boxes),
    'all_skipped_symbol_upper_at_least_one': all(z[2]>=1 for z in skip),
    'each_paired_mass_contains_exact_interval_formula': all(mass_checks),
    'sum_lower_is_outward': b <= sum((Q(z['paired_mass'][0]) for z in boxes),Q(0)),
    'sum_upper_is_outward': Q(replay['bad_mass_enclosure'][1]) >= sum((Q(z['paired_mass'][1]) for z in boxes),Q(0)),
    'all_48_symbol_calls_use_shift256': domains['symbol_calls']==48 and domains['all_symbol_shifts']==256,
    'scalar_m0_matches_negative_w0_upper': m0 == -Q(replay['w_zero'][1]),
    'U_upper_is_outward': Q(replay['actual_upper']) >= 1-b/N,
    'threshold_lower_is_outward': Q(replay['required_upper']) <= m0/(1+m0),
    'rational_bad_mass_gt_13_over_125': b>Q(13,125),
    'rational_norm_lt_66_over_25': N<Q(66,25),
    'rational_M_lower_gt_36': m0>36,
    'rational_rejection': 1-Q(13,125)/Q(66,25)==Q(317,330)<Q(36,37),
    'strict_computed_comparison': Q(replay['actual_upper'])<Q(replay['required_upper']),
    'all_remainder_allowances_pass': all(x['pass'] for x in remainders.values()),
    'original_failures_empty': not replay['failures'],
}
summary = {
    'status': 'PASS' if all(checks.values()) else 'FAIL', 'checks': checks,
    'failures': [k for k,v in checks.items() if not v],
    'actual_upper': replay['actual_upper'], 'required_upper': replay['required_upper'],
    'rational_bounds': {'c_E_upper': '317/330', 'threshold_lower': '36/37'},
    'exact_U_from_stored_bounds': str(1-b/N),
    'exact_threshold_from_stored_m0': str(m0/(1+m0)),
    'prime_powers': expected, 'retained_panel_indices': indices,
    'paired_mass_checks': mass_checks, 'remainder_checks': remainders,
    'sources_sha256': {str(p.relative_to(HERE.parents[1])): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in (BASE,WRAPPER,HERE/'fixed-witness-863.json')},
    'scope': 'C750a fixed-screen rejection only; same arithmetic implementation, with independent exact rational comparisons and prime-power factorization.',
}
path = HERE/'audit-summary-865.json'
path.write_text(json.dumps(summary,indent=2)+'\n')
print(f"{summary['status']}: U <= {summary['actual_upper']}; required <= {summary['required_upper']}")
print(f"Prime powers: {len(expected)}; retained pairs: {len(boxes)}; checks: {len(checks)}; failures: {summary['failures']}")
print('Full evidence: scripts/good-frequency/audit-summary-865.json, domains-865.json, replay-865.json')
raise SystemExit(0 if all(checks.values()) else 1)
