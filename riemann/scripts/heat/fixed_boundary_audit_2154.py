"""Audit the immutable step2152 certificate: exact checks and full replay.

Inclusion is proved in C919b; replay alone is not an independent proof.
No original artifact is overwritten and no numerical test is changed.
"""
import hashlib
import importlib.util
import json
import platform
from collections import Counter
from decimal import Decimal
from fractions import Fraction as Q
from pathlib import Path

BASE = Path(__file__).parent
SCRIPT = BASE / 'fixed_boundary_2152.py'
CERT = BASE / 'fixed-boundary-2152.json'
INTEGRITY = BASE / 'fixed-boundary-integrity-2152.json'
OUT = BASE / 'fixed-boundary-audit-2154.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def interval(x):
    lo, hi = Q(x['lo']), Q(x['hi'])
    assert lo <= hi
    return lo, hi


def min_square(x):
    lo, hi = interval(x)
    return Q(0) if lo <= 0 <= hi else min(lo*lo, hi*hi)


def differences(a, b, path=''):
    if type(a) is not type(b):
        return [{'path': path, 'saved': a, 'replay': b}]
    if isinstance(a, dict):
        ans = []
        for k in sorted(a.keys() | b.keys()):
            if k not in a or k not in b:
                ans.append({'path': path+'/'+k, 'saved': a.get(k),
                            'replay': b.get(k), 'missing_key': True})
            else:
                ans.extend(differences(a[k], b[k], path+'/'+k))
        return ans
    if isinstance(a, list):
        if len(a) != len(b):
            return [{'path': path, 'saved_length': len(a), 'replay_length': len(b)}]
        return [d for i, (x, y) in enumerate(zip(a, b))
                for d in differences(x, y, path+'/'+str(i))]
    return [] if a == b else [{'path': path, 'saved': a, 'replay': b}]


def main():
    d, old = json.loads(CERT.read_text()), json.loads(INTEGRITY.read_text())
    original_hashes = {p.name: sha(p) for p in (SCRIPT, CERT, INTEGRITY)}
    spec = importlib.util.spec_from_file_location('fixed2152', SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    report = {'status': 'IN_PROGRESS', 'runtime': platform.python_version(),
              'hashes_before': original_hashes, 'global_checks': [],
              'boxes': [], 'failures': [],
              'scope': 'Exact saved-data validation and full unchanged replay; inclusion proof in C919b',
              'required_margin': '18367/100000',
              'contexts': {name: str(getattr(m, name)) for name in ('DN', 'UP', 'RN')}}

    def check(name, ok, evidence):
        item = {'name': name, 'passed': bool(ok), 'evidence': evidence}
        report['global_checks'].append(item)
        if not ok:
            report['failures'].append(item)

    check('original integrity hashes',
          old['certificate_sha256'] == original_hashes[CERT.name] and
          old['script_sha256'] == original_hashes[SCRIPT.name], original_hashes)
    check('original integrity records complete and successful',
          len(old['checks']) == 6150 and all(c['passed'] for c in old['checks'])
          and old['failures'] == [], {'checks': len(old['checks']), 'failures': old['failures']})
    check('fixed budget and runtime', d['runtime'] == platform.python_version() == '3.15.2'
          and d['precision'] == m.PREC == 100 and
          d['series'] == {'machin_terms': 96, 'log_terms': 128,
                         'sine_nonzero_terms': 128, 'cosine_nonzero_terms': 128}, d['series'])
    check('complete grid and no failures',
          [(b['j'], b['k']) for b in d['boxes']] ==
          [(j, k) for j in range(32) for k in range(64)] and not d['failures'],
          {'boxes': len(d['boxes']), 'failures': d['failures']})
    # Independent exact rational construction of both Machin bounds.
    def atan(q):
        s = sum((Q((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(96)), Q(0))
        return s, s+Q(1, 193*q**193)
    a, b = atan(5), atan(239)
    exact = [16*a[0]-4*b[1], 16*a[1]-4*b[0]]
    saved_exact = [Q(int(x['num']), int(x['den'])) for x in d['pi_exact']]
    pl, ph = interval(d['pi'])
    check('Machin bounds and decimal conversion', exact == saved_exact and
          pl <= exact[0] <= exact[1] <= ph and d['pi'] == m.PI.data(), d['pi'])
    cutoff = (m.R+m.I(0, m.I.rat(Q(1, 5)).hi)/16).sqrt()
    cl, ch = interval(d['cutoff_guard']['sqrt_range'])
    check('constant cutoff with exact squared checks',
          d['cutoff_guard'] == {'sqrt_range': cutoff.data(), 'N': 3, 'passed': True}
          and 3 < cl < ch < 4 and cl*cl <= 200/(4*ph)
          and ch*ch >= 200/(4*pl)+Q(1, 80), d['cutoff_guard'])
    counts_total = Counter()
    for i, saved in enumerate(d['boxes']):
        j, k = divmod(i, 64)
        tl, th, yl, yh = Q(j, 160), Q(j+1, 160), Q(k, 64), Q(k+1, 64)
        t = m.I(m.I.rat(tl).lo, m.I.rat(th).hi)
        y = m.I(m.I.rat(yl).lo, m.I.rat(yh).hi)
        replay = {'j': j, 'k': k, 't_rational': [f'{j}/160', f'{j+1}/160'],
                  'y_rational': [f'{k}/64', f'{k+1}/64'],
                  't': t.data(), 'y': y.data(), 'N': 3, 'guards': []}
        m.ACTIVE = replay['guards']
        replay.update(m.evaluate(t, y))
        mismatch = differences(saved, replay)
        l, e, margin = (Q(saved[key]) for key in ('modulus_lower', 'error_upper', 'margin_lower'))
        al, ah = interval(saved['error23']); el, eh = interval(saved['error24'])
        stl, sth = interval(saved['t']); syl, syh = interval(saved['y'])
        checks = {'exact_coverage': stl <= tl <= th <= sth and syl <= yl <= yh <= syh,
                  'modulus_lower': l >= 0 and l*l <= min_square(saved['f']['re'])+min_square(saved['f']['im']),
                  'complete_error_upper': al >= 0 and el > 0 and e >= ah+eh,
                  'margin': margin <= l-e and margin > Q(18367, 100000),
                  'all_fields_replayed': not mismatch}
        guard_errors = []
        for g in saved['guards']:
            name, ev = g['name'], g['evidence']; ok = g['passed'] is True
            counts_total[name] += 1
            if name == 'complex divisor away from zero':
                ok &= interval(ev)[0] > 0
            elif name == 'log imaginary sign':
                a, b = interval(ev); ok &= a > 0 or b < 0
            elif name == 'log series radius':
                a, b = interval(ev); ok &= 0 <= a <= b < 1
            elif name == 'principal log rotation':
                ok &= interval(ev)[0] > 0
            elif name == 'trig reduction':
                a, b = interval(ev['reduced']); ok &= max(abs(a), abs(b)) <= 4 and type(ev['integer']) is int
            elif name == 'nonzero explicit normalizer':
                ok &= interval(ev['s_imaginary']) == (Q(-100), Q(-100))
                interval(ev['log_B']['re']); interval(ev['log_B']['im'])
            else:
                ok = False
            if not ok:
                guard_errors.append(g)
        checks['guards'] = not guard_errors
        entry = {'index': i, 'j': j, 'k': k, 'checks': checks,
                 'guards': len(saved['guards']), 'margin_lower': saved['margin_lower'],
                 'mismatches': mismatch, 'guard_failures': guard_errors}
        report['boxes'].append(entry)
        if not all(checks.values()):
            report['failures'].append(entry)
        if k == 63:
            report['completed_boxes'] = i+1
            OUT.write_text(json.dumps(report, indent=2)+'\n')
        if (i+1) % 512 == 0:
            print(f'Replayed {i+1}/2048 boxes; failures={len(report["failures"])}', flush=True)
    m.ACTIVE = None
    stats = {key: str(v) if isinstance(v, Decimal) else v for key, v in m.STATS.items()}
    check('all statistics reproduced including sqrt checks', stats == d['statistics'], stats)
    report['guard_counts'] = dict(counts_total)
    report['guard_count'] = sum(counts_total.values())
    worst = min(d['boxes'], key=lambda b: Q(b['margin_lower']))
    report['worst_bounds'] = {key: worst[key] for key in
                             ('j', 'k', 'f', 'modulus_lower', 'error_upper', 'margin_lower')}
    check('minimum and all-box summary', d['summary']['minimum_margin_lower'] == worst['margin_lower']
          and d['summary']['all_passed'] and d['summary']['positive_boxes'] == 2048,
          {'actual': worst['margin_lower'], 'required': '18367/100000'})
    report['hashes_after'] = {p.name: sha(p) for p in (SCRIPT, CERT, INTEGRITY)}
    check('original artifacts unchanged', original_hashes == report['hashes_after'], report['hashes_after'])
    report['status'] = 'PASS' if not report['failures'] else 'FAIL'
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'boxes': len(report['boxes']),
                      'guard_count': report['guard_count'], 'failures': len(report['failures']),
                      'actual_minimum': worst['margin_lower'], 'required': '18367/100000',
                      'path': str(OUT.relative_to(Path.cwd()))}, indent=2))
    assert not report['failures']


if __name__ == '__main__':
    main()
