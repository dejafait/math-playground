"""Replay L897 and check its complete rational evidence without changing step104."""
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)
folder = Path(__file__).resolve().parent
source = folder / 'countermodel-104.py'
original_path = source.with_suffix('.json')
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
replay_path = folder / 'audit-replay-106.json'
env = {'__name__': '__main__', '__file__': str(replay_path.with_suffix('.py'))}
with redirect_stdout(StringIO()):
    exec(compile(source.read_text(), str(source), 'exec'), env)
replay = json.loads(replay_path.read_text())

checks = {}
def check(name, condition):
    checks[name] = bool(condition)

check('original_bytes_preserved', original_path.read_bytes() == original_bytes)
check('replay_matches_complete_original', replay == original)
expected = dict(k=6002, J=6003, m=9000000000000,
                K=12363153437138, H=3000175332800,
                delta='1/1000000000000')
check('parameters_match_statement', original['parameters'] == expected)
check('series_lengths', original['method']['arctan_terms'] == 50
      and original['method']['log_terms'] == 50)

# Parse EVERY stored rational endpoint, not the previews or check flags.
intervals = {}
for section in ('bounds', 'Hm_terms'):
    for name, obj in original[section].items():
        if not isinstance(obj, dict):
            continue
        lo, hi = Q(obj['lower']), Q(obj['upper'])
        key = section + '/' + name
        intervals[key] = lo, hi
        check('ordered_' + key, lo <= hi)
        target = replay[section][name]
        check('exact_replay_' + key,
              lo == Q(target['lower']) and hi == Q(target['upper']))

def bound(name):
    return intervals['bounds/' + name]

k, J, m, K, H = (expected[key] for key in ('k', 'J', 'm', 'K', 'H'))
delta = Q(expected['delta'])
g = Q(10000)
T = g + delta
R = 2 * (g*g + T*T)
q = 2*g*g/(g*g + T*T)
a = R/(4*T*T)
s = (1+q)/2
eps = 1-q
check('packet_boundaries', 0 < Q(9999)+Q(1,k) < g < T < H-1 < H
      and K-J > 0 and H > 0)
check('scalar_domains', R > 0 and 0 < q < s < 1 and 0 < a < 1)
check('epsilon_identity', eps == (2*g*delta+delta*delta)/(g*g+T*T)
      and bound('epsilon') == (eps, eps))
check('epsilon_bound', 0 < eps < 3*delta/g < Q(1,10**15))
check('rank_factor', m+k+2 < 10**13)
check('U_9999_strict', bound('U_9999')[0] > 10152 > J)
check('U_Hminus1_strict', bound('U_Hminus1_minus_K')[0] > 11)
check('U_H_strict', bound('U_H_minus_K')[0] > 0)
check('derivative_uniform_witness', bound('derivative_9999')[0] > Q(117,100) > 1)
check('V_strict', bound('V')[0] > Q(17,100000) > 0)

term_names = ['B', '2logk', '(2k-2)log(1+q)', 'klog2',
              '-2klog(1-q)', '(m+k+2)logs']
check('all_six_terms_present', set(original['Hm_terms']) == set(term_names))
term_values = [intervals['Hm_terms/' + name] for name in term_names]
check('complete_signed_sum', bound('Hm') ==
      (sum((x[0] for x in term_values), Q(0)),
       sum((x[1] for x in term_values), Q(0))))
check('B_term_matches', term_values[0] == bound('B'))
check('first_five_terms_positive', all(lo > 0 for lo, hi in term_values[:5]))
check('log2_margin', term_values[3][0] > Q(k,2))
check('last_term_retained_negative', -Q(1,100) < term_values[-1][0]
      <= term_values[-1][1] < 0)
last_cost_bound = (m+k+2)*eps/(2-eps)
check('analytic_last_cost', 0 < last_cost_bound < (m+k+2)*eps < Q(1,100))
analytic_floor = Q(k,2)-Q(1,100)
check('analytic_threshold', analytic_floor == Q(300099,100) > 3000)
check('full_Hm_strict', bound('Hm')[0] > analytic_floor)

# Compact witnesses are OUTWARD exact rational enclosures of the stored
# full endpoints. They are consequences of the complete Fraction checks.
scale = 10**12
def coarse_interval(lo, hi):
    flo = (lo.numerator*scale)//lo.denominator
    cei = -((-hi.numerator*scale)//hi.denominator)
    out = Q(flo,scale), Q(cei,scale)
    assert out[0] <= lo <= hi <= out[1]
    return {'lower': str(out[0]), 'upper': str(out[1])}
witness_names = ['U_9999', 'U_Hminus1_minus_K', 'U_H_minus_K',
                 'derivative_9999', 'V', 'B', 'Hm']
witnesses = {name: coarse_interval(*bound(name)) for name in witness_names}
witnesses['last_term'] = coarse_interval(*term_values[-1])
witnesses['klog2'] = coarse_interval(*term_values[3])
witnesses['analytic_Hm_floor'] = str(analytic_floor)
witnesses['analytic_last_cost_upper'] = str(Q(1,100))

failed = [name for name, passed in checks.items() if not passed]
report = {
    'scope': 'Scalar certificate audit only; L897 contains the all-height and product audit.',
    'original': str(original_path.relative_to(folder.parent.parent)),
    'original_sha256': sha256(original_bytes).hexdigest(),
    'source_sha256': sha256(source.read_bytes()).hexdigest(),
    'replay': str(replay_path.relative_to(folder.parent.parent)),
    'full_rational_intervals_checked': len(intervals),
    'checks': checks, 'failures': failed, 'rational_witnesses': witnesses,
    'required_for_obstruction': 'H_m >= 0',
    'required_for_coarse_overlap': 'H_m < 0',
    'analytic_last_cost_exact': str(last_cost_bound),
}
out = folder / 'audit-106.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print('Complete rational intervals checked:', len(intervals))
print('Checks:', len(checks), 'passed:', sum(checks.values()), 'failures:', failed)
for name in ('U_9999','U_Hminus1_minus_K','derivative_9999','V','Hm','last_term'):
    print(name, witnesses[name])
print('H_m > 300099/100 > 3000; obstruction requires >= 0; overlap requires < 0.')
print('Original certificate preserved:', checks['original_bytes_preserved'])
print('Full replay:', replay_path)
print('Audit certificate:', out)
assert not failed
