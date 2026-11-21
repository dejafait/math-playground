"""Exact saved-evidence integrity checks; not the later independent audit."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

BASE = Path(__file__).parent
source = BASE/'fixed-boundary-2152.json'
raw = source.read_bytes()
d = json.loads(raw)
checks = []


def check(name, ok, evidence):
    checks.append({'name': name, 'passed': bool(ok), 'evidence': evidence})


def interval(x):
    lo, hi = Q(x['lo']), Q(x['hi'])
    assert lo <= hi
    return lo, hi


check('complete fixed grid', len(d['boxes']) == 2048 and
      [(b['j'], b['k']) for b in d['boxes']] ==
      [(j, k) for j in range(32) for k in range(64)], '32 x 64 in order')
check('no recorded failures', d['failures'] == [], d['failures'])
check('precision and series budget', d['precision'] == 100 and
      d['series'] == {'machin_terms': 96, 'log_terms': 128,
                     'sine_nonzero_terms': 128, 'cosine_nonzero_terms': 128},
      d['series'])
pl, ph = interval(d['pi'])
exact_pi = [Q(int(p['num']), int(p['den'])) for p in d['pi_exact']]
check('pi conversion encloses rational bounds',
      pl <= exact_pi[0] <= exact_pi[1] <= ph, d['pi'])
cl, ch = interval(d['cutoff_guard']['sqrt_range'])
check('global cutoff guard exact squared bounds', 3 < cl < ch < 4
      and cl**2 <= 200/(4*ph) and ch**2 >= 200/(4*pl)+Q(1, 80),
      d['cutoff_guard'])
guards_total = 0
for i, b in enumerate(d['boxes']):
    j, k = b['j'], b['k']
    tl, th = interval(b['t'])
    yl, yh = interval(b['y'])
    check(f'box {i} exact coverage',
          tl <= Q(j, 160) <= Q(j+1, 160) <= th and
          yl <= Q(k, 64) <= Q(k+1, 64) <= yh and
          b['t_rational'] == [f'{j}/160', f'{j+1}/160'] and
          b['y_rational'] == [f'{k}/64', f'{k+1}/64'] and b['N'] == 3,
          {'j': j, 'k': k})
    rl, rh = interval(b['f']['re'])
    il, ih = interval(b['f']['im'])

    def min_square(lo, hi):
        return Q(0) if lo <= 0 <= hi else min(lo**2, hi**2)

    l, e, m = (Q(b[key]) for key in
               ('modulus_lower', 'error_upper', 'margin_lower'))
    al, ah = interval(b['error23'])
    el, eh = interval(b['error24'])
    check(f'box {i} exact lower and upper bounds',
          l >= 0 and l*l <= min_square(rl, rh)+min_square(il, ih)
          and e >= ah+eh and al >= 0 and el > 0
          and m <= l-e and m > Q('0.18367'),
          {key: b[key] for key in
           ('modulus_lower', 'error_upper', 'margin_lower')})
    guard_failures = []
    for g in b['guards']:
        guards_total += 1
        name, ev = g['name'], g['evidence']
        ok = g['passed']
        if name == 'complex divisor away from zero':
            ok = ok and interval(ev)[0] > 0
        elif name == 'log imaginary sign':
            lo, hi = interval(ev)
            ok = ok and (lo > 0 or hi < 0)
        elif name == 'log series radius':
            lo, hi = interval(ev)
            ok = ok and 0 <= lo <= hi < 1
        elif name == 'principal log rotation':
            ok = ok and interval(ev)[0] > 0
        elif name == 'trig reduction':
            lo, hi = interval(ev['reduced'])
            ok = ok and max(abs(lo), abs(hi)) <= 4
        elif name == 'nonzero explicit normalizer':
            ok = ok and interval(ev['s_imaginary'])[1] < 0
            interval(ev['log_B']['re'])
            interval(ev['log_B']['im'])
        else:
            ok = False
        if not ok:
            guard_failures.append(g)
    check(f'box {i} all guard thresholds', not guard_failures,
          {'guard_count': len(b['guards']), 'failures': guard_failures})

worst_index = min(range(2048), key=lambda i: Q(d['boxes'][i]['margin_lower']))
worst = d['boxes'][worst_index]
check('summary minimum exact', Q(d['summary']['minimum_margin_lower']) ==
      Q(worst['margin_lower']), {'index': worst_index, 'j': worst['j'], 'k': worst['k']})
out = BASE/'fixed-boundary-integrity-2152.json'
report = {'certificate_sha256': hashlib.sha256(raw).hexdigest(),
          'script_sha256': hashlib.sha256((BASE/'fixed_boundary_2152.py').read_bytes()).hexdigest(),
          'checks': checks, 'guard_count': guards_total,
          'worst_index': worst_index,
          'worst_bounds': {key: worst[key] for key in
             ('j', 'k', 'modulus_lower', 'error_upper', 'margin_lower', 'error23', 'error24')},
          'failures': [c for c in checks if not c['passed']]}
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'checks': len(checks), 'guard_count': guards_total,
                  'failures': len(report['failures']), 'worst_index': worst_index,
                  'actual_minimum': worst['margin_lower'],
                  'required': '>0 on every box',
                  'integrity_path': str(out.relative_to(Path.cwd()))}, indent=2))
assert not report['failures']
