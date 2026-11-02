"""Replay C645w with additional invariants and audit every C645v/w cell.

Run the C645v generator first.  Original evidence is retained byte for byte;
the instrumented C645w replay writes its separate complete certificate.
"""
import contextlib
from fractions import Fraction as F
import hashlib
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
source = HERE / 'oblique-leading-saddle-certificate.py'
original = HERE / 'oblique-leading-saddle-certificate.json'
replay = HERE / 'oblique-leading-saddle-audit-replay.json'
report = HERE / 'oblique-saddle-audit.json'
checks, failures = [], []

def check(name, ok, actual, required):
    checks.append(dict(name=name, passed=bool(ok), actual=actual, required=required))
    if not ok:
        failures.append(name)

namespace = {'__file__': str(replay.with_suffix('.py'))}
code = source.read_text()
prefix, suffix = code.split('h0,hp0,hpp0,p0=phase(z0)', 1)
exec(compile(prefix, str(source), 'exec'), namespace)
base_log = namespace['log_series']
stats = dict(log_calls=0, midpoint_in_rectangle=0, midpoint_in_q_disk=0)
I, C, D = (namespace[k] for k in ('I', 'C', 'D'))

def audited_log(w, j=False):
    center = C(w.re.midpoint(), w.im.midpoint())
    q = w.absup()
    stats['log_calls'] += 1
    # Rounding of the chosen midpoint is harmless only after these checks.
    inside = (w.re.lo <= center.re.lo <= w.re.hi
              and w.im.lo <= center.im.lo <= w.im.hi)
    disk = center.absup() <= q
    assert inside and disk, 'logarithm midpoint/domain invariant'
    stats['midpoint_in_rectangle'] += int(inside)
    stats['midpoint_in_q_disk'] += int(disk)
    return base_log(w, j)

namespace['log_series'] = audited_log
log = io.StringIO()
with contextlib.redirect_stdout(log):
    exec(compile('h0,hp0,hpp0,p0=phase(z0)' + suffix, str(source), 'exec'), namespace)
(HERE / 'oblique-leading-saddle-audit-replay.log').write_text(log.getvalue())
new, old = json.loads(replay.read_text()), json.loads(original.read_text())
check('complete saddle certificate replay', new == old,
      hashlib.sha256(replay.read_bytes()).hexdigest(),
      hashlib.sha256(original.read_bytes()).hexdigest())
check('saddle failures', not new['failures'], new['failures'], [])
check('all original saddle comparisons', all(c['passed'] for c in new['checks']),
      len(new['checks']), 'every saved strict comparison passes')
check('logarithm midpoint domains', stats['log_calls'] == stats['midpoint_in_q_disk'],
      stats, 'every midpoint in its rectangle and certified q disk')

def audit_cover(rows, left, right, name):
    intervals = [(F(row['t'][0]), F(row['t'][1])) for row in rows]
    valid = (intervals[0][0] <= left and intervals[-1][1] >= right
             and all(a <= b for a, b in intervals)
             and all(intervals[k][1] >= intervals[k+1][0]
                     for k in range(len(intervals)-1)))
    check(name, valid, len(rows), 'closed cells cover the full interval without gaps')

cells = new['cells']
check('global indices', [r['j'] for r in cells] == list(range(1024)), len(cells), 1024)
audit_cover(cells, F(0), 2*F(new['pi'][1]), 'global continuous cover')
t0 = F('4.876972288459421')
audit_cover(new['local_cells'], t0-F('.21'), t0+F('.21'), 'local continuous cover')
outside, inside = [], []
for row in cells:
    lo, hi = map(F, row['t'])
    expected = hi <= t0-F('.2') or lo >= t0+F('.2')
    assert expected == row['outside']
    (outside if expected else inside).append(row)
check('all unexcluded cells covered locally',
      all(F(r['t'][0]) > t0-F('.21') and F(r['t'][1]) < t0+F('.21') for r in inside),
      len(inside), 'every non-complementary cell is inside the local curvature interval')
for name, actual, required in (
        ('all complementary phases', max(F(r['alias_real_upper']) for r in outside), F('.004')),
        ('all b0 phases', max(F(r['b0_real_upper']) for r in cells), F('-.06')),
        ('all local curvatures', max(F(r['real_second_upper']) for r in new['local_cells']), F('-.05'))):
    check(name, actual < required, str(actual), str(required))

tail_path = HERE / 'oblique-alias-tail-certificate.json'
tail = json.loads(tail_path.read_text())
check('tail failures', not tail['failures'], tail['failures'], [])
check('tail original strict comparisons', all(c['passed'] for c in tail['checks']),
      len(tail['checks']), 'all pass')
tail_cells = tail['cells']
check('tail cell indices', [r['j'] for r in tail_cells] == list(range(512)), len(tail_cells), 512)
audit_cover(tail_cells, F(0), F(1), 'tail closed-cell cover')
ks = [F(row['K']) for row in tail_cells]
check('tail monotone envelope', all(F(1) <= k < F(4) for k in ks)
      and all(a <= b for a, b in zip(ks, ks[1:])), str(max(ks)), '1 <= K_j < 4, nondecreasing')
check('all tail margins', all(F(v) > 0 for r in tail_cells for v in r['lower_margins'].values()),
      sum(len(r['lower_margins']) for r in tail_cells), 'all 2560 margins strictly positive')
log_roundings = []
for row, k in zip(tail_cells, ks):
    z = (k-1)/(k+1)
    exact = sum((z**(2*j+1)/F(2*j+1) for j in range(16)), F(0))
    exact += z**33/(33*(1-z*z))
    log_roundings.append(F(row['half_log_upper']) >= exact)
check('all rational logarithm tails and upward roundings', all(log_roundings),
      len(log_roundings), 512)
rate = sum((F(r['half_log_upper']) for r in tail_cells), F(0))/512
check('tail product rate', rate < F(31,100) and str(rate) == tail['summary']['product_exponent_upper'],
      str(rate), '< 31/100 and agrees with summary')
decay = F(4,3)*(F(3,10)-F(3,10)**3/6)-F(31,100)
check('whole alias decay', decay == F(21,250) and decay > F(1,32), str(decay), '21/250 > 1/32')

summary = dict(passed=not failures, checks=len(checks), saddle_cells=len(cells),
               local_cells=len(new['local_cells']), tail_cells=len(tail_cells),
               log_invariants=stats,
               limitations='Arithmetic replay and cell checks only; analytic audit is in C645v/w.')
report.write_text(json.dumps(dict(summary=summary, checks=checks, failures=failures,
                                 saddle_replay=replay.name, tail_certificate=tail_path.name), indent=2)+'\n')
print('Audit:', 'PASS' if not failures else 'FAIL', 'checks:', len(checks), 'failures:', failures)
print('Saddle: required > .005; actual lower', new['summary']['saddle_real_lower'])
print('Complement: required < .004; actual upper', new['summary']['complementary_phase_upper'])
print('Tail: required decay > 1/32; actual', decay)
print('Full audit:', report)
print('Complete saddle replay:', replay)
if failures:
    raise SystemExit(1)
