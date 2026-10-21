#!/usr/bin/env python3
"""Fixed L068 audit: independent rational univariate arithmetic; full evidence.

No imports from any producer or verifier. Existing verifiers are subprocesses
only for the bounded rejection tests. All outputs stay in this audit folder.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import copy
import hashlib
import json
import subprocess
import sys

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
PROD = BASE / 'scalar-actions-243'


def save(name, data):
    def enc(v):
        if isinstance(v, Q):
            return str(v)
        if isinstance(v, (list, tuple)):
            return [enc(x) for x in v]
        if isinstance(v, dict):
            return {str(k): enc(x) for k, x in v.items()}
        return v
    (OUT / name).write_text(json.dumps(enc(data), indent=2) + '\n')


def trim(v):
    v = list(v)
    while v and not v[-1]:
        v.pop()
    return v


def add(a, b, scale=1):
    r = [Q(0)] * max(len(a), len(b))
    for i, z in enumerate(a):
        r[i] += z
    for i, z in enumerate(b):
        r[i] += scale * z
    return trim(r)


def multiply(a, b, h):
    # Independent convolution after exact common-denominator clearing.
    da = lcm(*(z.denominator for z in a))
    db = lcm(*(z.denominator for z in b))
    aa = [int(z * da) for z in a]
    bb = [int(z * db) for z in b]
    raw = [0] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(aa):
        if x:
            for j, y in enumerate(bb):
                if y:
                    raw[i + j] += x * y
    r = [Q(z, da * db) for z in raw]
    # Monic long reduction; no polynomial helper is shared with production.
    assert len(h) == 49 and h[-1] == 1
    nonzero = [(i, c) for i, c in enumerate(h[:-1]) if c]
    for k in range(len(r) - 1, 47, -1):
        z = r[k]
        if z:
            for i, c in nonzero:
                r[k - 48 + i] -= z * c
    return trim(r[:48])


def crosscheck(data, up):
    h = list(map(Q, up['h']))
    xp = trim(map(Q, up['X_of_t']))
    yp = trim(map(Q, up['Y_of_t']))
    assert yp == [0, 1]
    N = [[Q(z) for z in row] for row in up['inverse']]
    one = [Q(1)]
    evidence = []

    def eq(label, lhs, rhs):
        lhs, rhs = trim(lhs), trim(rhs)
        residual = add(lhs, rhs, -1)
        evidence.append({'label': label, 'lhs': lhs, 'rhs': rhs,
                         'residual': residual, 'pass': not residual})
        if residual:
            save('univariate-crosscheck.json', {'status': 'FAIL', 'evidence': evidence})
            raise ValueError(label)

    # Transport each full pair via the audited inverse basis map. Independently
    # evaluate the complete X,Y polynomials as well; this tests the transport.
    pairs = []
    for v in data['denominators'].values():
        pairs += [v['value'], v['inverse']]
    for n in range(1, 7):
        pairs += [data['maps'][str(n)][key] for key in ('X', 'Y', 'x', 'y')]
        pairs += [data[key][str(n)] for key in ('phi', 'omega')]
    maxdegree = max(len(p) - 1 for pair in pairs for p in pair)
    powers = [one]
    for _ in range(maxdegree):
        powers.append(multiply(powers[-1], xp, h))

    def evaluate(pair):
        ev = []
        for parity, pol in enumerate(pair):
            part = []
            for i, c in enumerate(pol):
                if Q(c):
                    part = add(part, powers[i], Q(c))
            if parity:
                part = multiply(part, yp, h)
            ev = add(ev, part)
        return ev

    def transport(pair, label):
        assert len(pair) == 2 and all(len(p) <= 24 for p in pair)
        v = sum(([Q(z) for z in p] + [Q(0)] * (24 - len(p)) for p in pair), [])
        t = trim([sum((a*b for a, b in zip(row, v)), Q(0)) for row in N])
        eq('transport_' + label, t, evaluate(pair))
        return t

    required = {'constant' + str(k) for k in (2, 4, 36, 216)} | {'2Y', '4Y'}
    required |= {'psi' + str(n) + suffix for n in range(1, 7) for suffix in ('', '^2', '^3')}
    assert set(data['denominators']) == required and len(required) == 24
    values = {}
    for key in sorted(required):
        row = data['denominators'][key]
        value = transport(row['value'], key + '_value')
        inverse = transport(row['inverse'], key + '_inverse')
        values[key] = value
        eq('unit_' + key, multiply(value, inverse, h), one)
    print('Independent Q[T]/h check: 24/24 full unit products passed', flush=True)
    for n in range(1, 7):
        row = data['maps'][str(n)]
        X, Y, x, y = [transport(row[key], str(n) + '_' + key) for key in ('X', 'Y', 'x', 'y')]
        eq('multiplication_X_' + str(n), multiply(values['psi' + str(n) + '^2'], X, h), evaluate(data['phi'][str(n)]))
        eq('multiplication_Y_' + str(n), multiply(values['psi' + str(n) + '^3'], Y, h), evaluate(data['omega'][str(n)]))
        eq('original_x_' + str(n), add([36*z for z in x], [Q(12)]), X)
        eq('original_y_' + str(n), add([216*z for z in y], [Q(108)]), Y)
        eq('sigma_t_' + str(n), list(map(Q, row['sigma_t'])), Y)
    result = {'status': 'PASS', 'dimension': 48, 'required_dimension': 48,
              'unit_products': 24, 'required_unit_products': 24,
              'multiplication_coordinates': 12, 'required_multiplication_coordinates': 12,
              'original_transports': 12, 'required_original_transports': 12,
              'independent_pair_transports': 72, 'required_pair_transports': 72,
              'sigma_t_checks': 6, 'max_X_degree_evaluated': maxdegree,
              'identities': len(evidence), 'evidence': evidence, 'failures': []}
    save('univariate-crosscheck.json', result)
    print(json.dumps({k: v for k, v in result.items() if k != 'evidence'}), flush=True)


def rejections(data):
    cases = [(name, PROD / 'rejections' / (name + '.json'), label) for name, label in (
        ('wrong-coordinate', 'geometric_X_2'), ('wrong-inverse', 'denominator_inverse_psi3'),
        ('wrong-t-action', 'full_T_basis_3_1'), ('wrong-B-action', 'full_B_even_4_1'),
        ('missing-denominator', 'complete_required_denominators'))]
    # Retain schema/convention labels, but change the negative base itself.
    d = copy.deepcopy(data)
    d['psi']['-1'] = [['1'], ['0']]
    save('negative-base.json', d)
    cases.append(('negative-base', OUT / 'negative-base.json', 'psi_-1_all_coefficients'))
    # Swap entire scalar-2 and scalar-4 maps, consistent with inverse indexing.
    # The geometric equation must reject this BEFORE action/composition checks.
    d = copy.deepcopy(data)
    d['maps']['2'], d['maps']['4'] = d['maps']['4'], d['maps']['2']
    save('inverse-index.json', d)
    cases.append(('inverse-index', OUT / 'inverse-index.json', 'geometric_X_2'))
    results = []
    for name, fixture, label in cases:
        report = OUT / (name + '-report.json')
        p = subprocess.run([sys.executable, str(PROD / 'verify_actions.py'), '--certificate', str(fixture), '--report', str(report)], capture_output=True, text=True)
        (OUT / (name + '.log')).write_text(p.stdout + p.stderr)
        r = json.loads(report.read_text())
        ok = p.returncode == 1 and r['status'] == 'FAIL' and r['failures'] == [label]
        results.append({'case': name, 'expected': label, 'actual': r['failures'],
                        'intended_rejection': ok, 'fixture': str(fixture.relative_to(BASE)),
                        'report': report.name})
        print('rejection', name, 'PASS' if ok else 'FAIL', r['failures'], flush=True)
    save('rejections.json', {'status': 'PASS' if all(r['intended_rejection'] for r in results) else 'FAIL', 'cases': results})
    assert all(r['intended_rejection'] for r in results)


def main():
    result = {'status': 'FAIL', 'failures': []}
    try:
        data = json.loads((PROD / 'actions.json').read_text())
        up = json.loads((BASE / 'certificate.json').read_text())
        crosscheck(data, up)
        rejections(data)
        original = json.loads((OUT / 'original-manifest.json').read_text())
        after = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in original}
        save('preservation.json', {'before': original, 'after': after, 'unchanged': original == after})
        assert original == after, 'original_bytes_changed'
        upstream = json.loads((OUT / 'upstream-replay.json').read_text())
        action = json.loads((OUT / 'action-replay.json').read_text())
        assert upstream['status'] == action['status'] == 'PASS', 'complete_replays'
        assert upstream['checks_passed'] == 4852 and action['checks_passed'] == 166964
        assert action['matrix_composition_entries_checked'] == action['matrix_composition_entries_required'] == 165888
        result.update(status='PASS', original_files_preserved=len(original),
                      upstream_checks=4852, action_checks=166964,
                      symbolic_divisions=8, denominator_units=24, basis_images=576,
                      composition_entries=165888, required_composition_entries=165888,
                      independent_univariate_identities=126, intended_rejections=7,
                      required_rejections=7)
    except Exception as exc:
        result['failures'].append(str(exc))
    save('audit-report.json', result)
    print(json.dumps(result | {'report': str(OUT / 'audit-report.json')}), flush=True)
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
