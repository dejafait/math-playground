#!/usr/bin/env python3
"""Independent exact replay. Imports only established structural checkers.
Never imports the dual-kernel builder. All assertions here use explicit checks.
"""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from fractions import Fraction
from math import isqrt, lcm, prod
from pathlib import Path


class Invalid(Exception):
    pass


class Check:
    def __init__(self):
        self.labels = []

    def need(self, label, condition):
        if not condition:
            raise Invalid(label)
        self.labels.append(label)

    def integer(self, x, label='integer'):
        self.need(label, type(x) is int)
        return x

    def rational(self, x):
        self.need('strict rational text', type(x) is str and re.fullmatch(r'-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?', x) is not None)
        q = Fraction(x)
        self.need('canonical rational', str(q) == x)
        return q

    def vector(self, x, n, rational=False):
        self.need('vector exact length', type(x) is list and len(x) == n)
        return [(self.rational(v) if rational else self.integer(v)) for v in x]

    def matrix(self, x, nr, nc):
        self.need('matrix exact schema', type(x) is dict and set(x) == {'rows', 'cols', 'entries'})
        self.integer(x['rows']); self.integer(x['cols'])
        self.need('matrix explicit shape', x['rows'] == nr and x['cols'] == nc)
        self.need('matrix row count', type(x['entries']) is list and len(x['entries']) == nr)
        return [self.vector(row, nc, True) for row in x['entries']]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_checker(path):
    spec = importlib.util.spec_from_file_location('structural_replay_'+path.parent.name.replace('-', '_'), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def arithmetic(ch, ar):
    ch.need('arithmetic exact schema', type(ar) is dict and set(ar) ==
            {'schema', 'model', 'conductor', 'certification', 'provenance', 'traces'})
    ch.need('arithmetic version', ar['schema'] == 'supplied-elliptic-arithmetic-v1')
    model = ch.vector(ar['model'], 5)
    a1, a2, a3, a4, a6 = model
    b2, b4, b6 = a1*a1+4*a2, 2*a4+a1*a3, a3*a3+4*a6
    b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    ch.need('nonsingular supplied equation', -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6 != 0)
    n = ch.integer(ar['conductor'])
    ch.need('positive conductor', n > 0)
    ch.need('supported arithmetic claim', ar['certification'] in ('L030_FIXED', 'SUPPLIED_CONDITIONAL'))
    pr = ar['provenance']
    ch.need('essential provenance fields', type(pr) is dict and set(pr) == {'minimal_model', 'nonCM', 'exact_conductor', 'newform'})
    ch.need('essential provenance supplied', all(type(v) is str and v.strip() for v in pr.values()))
    ch.need('traces list', type(ar['traces']) is list)
    primes, traces = [], []
    for entry in ar['traces']:
        ch.need('trace entry exact schema', type(entry) is dict and set(entry) == {'prime', 'trace', 'provenance'})
        p, a = ch.integer(entry['prime']), ch.integer(entry['trace'])
        ch.need('good prime', p >= 2 and n % p != 0 and all(p % q for q in range(2, isqrt(p)+1)))
        ch.need('integer Hasse bound', a*a <= 4*p)
        ch.need('trace provenance', type(entry['provenance']) is str and bool(entry['provenance'].strip()))
        primes.append(p); traces.append(a)
    ch.need('unique sorted primes', primes == sorted(set(primes)))
    if ar['certification'] == 'L030_FIXED':
        ch.need('fixed arithmetic identity', model == [0, 1, 1, -2, 0] and n == 389 and primes == [2] and traces == [-2])
    return n, primes, traces


def structural(ch, c, raw, adapter, ar, out):
    n, primes, traces = arithmetic(ch, ar)
    base = Path(__file__).resolve().parent.parent
    out.mkdir(parents=True, exist_ok=True)
    manifests = []
    if adapter == 'L030-fixed-v1':
        ch.need('fixed adapter input scope', n == 389 and primes == [2] and traces == [-2])
        ch.need('fixed schema marker', type(c) is dict and 'schema' not in c and
                all(k in c for k in ('arithmetic', 'projective_cosets', 'matrices', 'dual', 'integration_line')))
        ch.need('fixed model/conductor/trace binding', c['arithmetic']['model'] == ar['model'] and
                c['arithmetic']['conductor'] == n and c['arithmetic']['a2'] == traces[0])
        # Source bytes are copied only for checker API compatibility, preserving originals.
        snapshot = out/'structural-input.json'
        snapshot.write_bytes(raw)
        ch.need('assert-based established checker enabled', sys.flags.optimize == 0)
        # Audit shapes FIRST, before the established fixed verifier's list iteration.
        auditor = load_checker(base/'relative-t2/audit_certificate.py')
        auditor.SOURCE, auditor.OUT = snapshot, out/'fixed-audit.json'
        auditor.report = {'checks': {}, 'failures': []}
        try:
            auditor.audit()
        except Exception as error:
            auditor.report['failures'].append(type(error).__name__+': '+str(error))
            raise
        finally:
            auditor.OUT.write_text(json.dumps(auditor.report, indent=2)+'\n')
        verifier = load_checker(base/'relative-t2/verify_certificate.py')
        verifier.SOURCE, verifier.OUT, verifier.checks = snapshot, out/'fixed-verification.json', {}
        try:
            verifier.verify()
        except Exception as error:
            # The established verifier also uses bare path assertions. Those
            # do not call its check() writer: replace any earlier success
            # report and bind this failed replay to the actual input bytes.
            verifier.OUT.write_text(json.dumps({
                'certificate_sha256': digest(raw), 'checks': verifier.checks,
                'failures': [type(error).__name__+': '+str(error)],
                'results': None}, indent=2)+'\n')
            raise
        for report, path, script in [(auditor.report, auditor.OUT, base/'relative-t2/audit_certificate.py'),
                                     (json.loads(verifier.OUT.read_text()), verifier.OUT, base/'relative-t2/verify_certificate.py')]:
            ch.need('complete fixed structural report binding', report['certificate_sha256'] == digest(raw) and not report['failures'] and
                    all(report['checks'].values()))
            manifests.append({'report': str(path), 'program_sha256': digest(script.read_bytes()),
                              'report_sha256': digest(path.read_bytes()),
                              'checks': len(report['checks']), 'results': report['results']})
        p = c['presentation']
        d, s = p['dimension'], len(c['projective_cosets'])
        coords = p['integral_generator_coordinates']
        relations, saturated = c['relations'], p['saturated_relation_basis']
        matrices = {'J': c['matrices']['J'], 'T2': c['matrices']['H2']}
    elif adapter == 'L038-relative-v1':
        ch.need('general arithmetic retained conditional', ar['certification'] == 'SUPPLIED_CONDITIONAL')
        checker = load_checker(base/'general-relative/verify_certificate.py')
        obj = checker.Checker()
        failures, summary = [], None
        try:
            summary = checker.replay(obj, c, n, primes)
        except Exception as error:
            failures.append(type(error).__name__+': '+str(error))
            raise
        finally:
            path = out/'general-verification.json'
            path.write_text(json.dumps({'sha256': digest(raw), 'summary': summary, 'checks': obj.checks,
                                        'actual': obj.counts, 'required': obj.required, 'failures': failures}, indent=2)+'\n')
        manifests.append({'report': str(path), 'program_sha256': digest((base/'general-relative/verify_certificate.py').read_bytes()),
                          'report_sha256': digest(path.read_bytes()),
                          'checks': len(obj.checks), 'summary': summary, 'actual': obj.counts, 'required': obj.required})
        p = c['presentation']
        d, s = p['d'], p['s']
        coords = p['generator_coordinates']
        relations = c['A']['entries']
        saturated = [list(row) for row in zip(*p['K']['entries'])] if p['r'] else []
        matrices = {k: v['B']['entries'] for k, v in c['operators'].items()}
    else:
        raise Invalid('unsupported structural adapter')
    ch.need('entire operator set', set(matrices) == {'J'} | {'T'+str(p) for p in primes})
    ch.need('geometric convention scope', adapter in ('L030-fixed-v1', 'L038-relative-v1'))
    return {'d': d, 's': s, 'coords': coords, 'relations': relations, 'saturated': saturated,
            'matrices': matrices, 'P': primes, 'traces': traces, 'manifests': manifests}


def exact_determinant(ch, rows):
    # Fraction-free Bareiss after clearing each row's denominators.
    # This is distinct from the producer's rational Gaussian determinant.
    n = len(rows)
    denominators = [lcm(*(x.denominator for x in row)) for row in rows]
    a = [[int(rows[i][j]*denominators[i]) for j in range(n)] for i in range(n)]
    sign, previous = 1, 1
    for k in range(n-1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        current = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*current-a[i][k]*a[k][j]
                ch.need('Bareiss exact division', numerator % previous == 0)
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = current
    return Fraction(sign*a[-1][-1], prod(denominators)) if n else Fraction(1)


def linear(ch, cert, bundle, ar, sr, abr):
    ch.need('dual exact schema', type(cert) is dict and set(cert) ==
            {'schema', 'structural_adapter', 'arithmetic', 'domain', 'B', 'rref', 'row_operations', 'pivots',
             'rank', 'nullity', 'kernel_basis', 'generator_values', 'line', 'result', 'qualification', 'bindings'})
    ch.need('dual version', cert['schema'] == 'full-relative-dual-v1')
    ch.need('external arithmetic and byte bindings', cert['arithmetic'] == ar and cert['bindings'] ==
            {'structural_sha256': digest(sr), 'arithmetic_sha256': digest(abr)})
    d, s, primes = bundle['d'], bundle['s'], bundle['P']
    m = (len(primes)+1)*d
    ch.need('domain exact schema', type(cert['domain']) is dict and set(cert['domain']) == {'d', 's', 'P', 'blocks'})
    ch.integer(cert['domain']['d']); ch.integer(cert['domain']['s'])
    ch.vector(cert['domain']['P'], len(primes))
    ch.need('full domain and complete blocks', cert['domain'] ==
            {'d': d, 's': s, 'P': primes, 'blocks': ['J']+['T'+str(p) for p in primes]})
    # Shape checks on all structural matrices are supplied by their full replay.
    blocks = [('J', 1)]+[('T'+str(p), bundle['traces'][i]) for i, p in enumerate(primes)]
    b = [[Fraction(bundle['matrices'][name][j][i])-a*int(i == j)
          for j in range(d)] for name, a in blocks for i in range(d)]
    ch.need('every transpose/reflection/eigenvalue entry', ch.matrix(cert['B'], m, d) == b)
    reduced = [row[:] for row in b]
    operations = cert['row_operations']
    ch.need('operations list', type(operations) is list)
    for op in operations:
        ch.need('operation syntax', type(op) is list and len(op) in (3, 4) and op[0] in ('swap', 'scale', 'add'))
        kind, i = op[0], ch.integer(op[1])
        ch.need('operation index', 0 <= i < m)
        ch.need('operation arity', len(op) == (4 if kind == 'add' else 3))
        if kind in ('swap', 'add'):
            j = ch.integer(op[2])
            ch.need('distinct bounded source index', 0 <= j < m and j != i)
        if kind == 'swap':
            reduced[i], reduced[j] = reduced[j], reduced[i]
        else:
            q = ch.rational(op[-1])
            if kind == 'scale':
                ch.need('invertible scale', q != 0)
                reduced[i] = [q*x for x in reduced[i]]
            else:
                reduced[i] = [reduced[i][h]+q*reduced[j][h] for h in range(d)]
    ch.need('whole elimination replay', ch.matrix(cert['rref'], m, d) == reduced)
    ch.need('pivots list', type(cert['pivots']) is list)
    pivots = ch.vector(cert['pivots'], len(cert['pivots']))
    ch.need('sorted distinct bounded pivots', pivots == sorted(set(pivots)) and all(0 <= p < d for p in pivots))
    r = len(pivots)
    ch.need('rank bounded by rows', r <= m)
    for i, p in enumerate(pivots):
        ch.need('leading pivot', all(reduced[i][j] == 0 for j in range(p)) and reduced[i][p] == 1)
        ch.need('entire unit pivot column', all(reduced[k][p] == int(k == i) for k in range(m)))
    ch.need('complete zero tail', all(not any(row) for row in reduced[r:]))
    ch.integer(cert['rank']); ch.integer(cert['nullity'])
    ch.need('rank/nullity exact', cert['rank'] == r and cert['nullity'] == d-r)
    free = [j for j in range(d) if j not in pivots]
    basis = ch.matrix(cert['kernel_basis'], d-r, d)
    for i, v in enumerate(basis):
        ch.need('independent free coordinates', all(v[j] == int(k == i) for k, j in enumerate(free)))
        ch.need('all determined pivot coordinates', all(v[p] == -reduced[k][free[i]] for k, p in enumerate(pivots)))
        ch.need('every exact kernel residual', all(sum(b[k][j]*v[j] for j in range(d)) == 0 for k in range(m)))
    values = ch.matrix(cert['generator_values'], d-r, s)
    for t, v in enumerate(basis):
        expected = [sum(Fraction(bundle['coords'][i][j])*v[j] for j in range(d)) for i in range(s)]
        ch.need('every integral generator value', values[t] == expected)
        for rel in bundle['relations']+bundle['saturated']:
            ch.need('every source/saturated value relation', sum(Fraction(rel[i])*values[t][i] for i in range(s)) == 0)
    witness = d > 0 and d-r == 1
    ch.need('result threshold', cert['result'] == ('LINE_WITNESS' if witness else 'INCONCLUSIVE'))
    if witness:
        line = cert['line']
        ch.need('line exact schema', type(line) is dict and set(line) == {'v', 'residuals', 'minor'})
        v = ch.vector(line['v'], d, True)
        ch.need('nonzero complete nullvector', v == basis[0] and any(v))
        residuals = ch.vector(line['residuals'], m, True)
        ch.need('every line residual zero', residuals == [sum(row[j]*v[j] for j in range(d)) for row in b] == [0]*m)
        minor = line['minor']
        ch.need('minor exact schema', type(minor) is dict and set(minor) == {'row_indices', 'column_indices', 'matrix', 'determinant'})
        rows, cols = ch.vector(minor['row_indices'], d-1), ch.vector(minor['column_indices'], d-1)
        ch.need('distinct bounded minor selections', len(set(rows)) == len(rows) and len(set(cols)) == len(cols)
                and all(0 <= i < m for i in rows) and all(0 <= j < d for j in cols))
        entries = [[b[i][j] for j in cols] for i in rows]
        ch.need('complete independently selected minor', ch.matrix(minor['matrix'], d-1, d-1) == entries)
        det = exact_determinant(ch, entries)
        ch.need('exact nonzero rank lower witness', det == ch.rational(minor['determinant']) and det != 0)
        ch.need('nonzero generator functional', any(values[0]))
    else:
        ch.need('no diagnostic line claim', cert['line'] is None)
        det = None
    return {'d': d, 's': s, 'B_shape': [m, d], 'rank': r, 'line_required_rank': d-1,
            'nullity': d-r, 'line_required_nullity': 1, 'result': cert['result'],
            'minor_determinant': str(det) if det is not None else None,
            'all_generator_values_checked': (d-r)*s, 'operations_checked': len(operations),
            'source_relation_checks': (d-r)*len(bundle['relations']),
            'saturated_relation_checks': (d-r)*len(bundle['saturated']),
            'arithmetic_status': 'L030_FIXED_REPLAY' if ar['certification'] == 'L030_FIXED' else 'SUPPLIED_CONDITIONAL'}


def verify(cert_path, structural_path, arithmetic_path, out):
    ch, failures, result, bundle = Check(), [], None, None
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        sr, abr, cr = structural_path.read_bytes(), arithmetic_path.read_bytes(), cert_path.read_bytes()
        c, ar, cert = json.loads(sr), json.loads(abr), json.loads(cr)
        arithmetic(ch, ar)
        arithmetic(ch, cert['arithmetic'])
        ch.need('binding before expensive structural replay', cert['bindings'] ==
                {'structural_sha256': digest(sr), 'arithmetic_sha256': digest(abr)} and cert['arithmetic'] == ar)
        bundle = structural(ch, c, sr, cert['structural_adapter'], ar, out.parent/(out.stem+'-structure'))
        result = linear(ch, cert, bundle, ar, sr, abr)
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    report = {'checker_sha256': digest(Path(__file__).read_bytes()), 'certificate': str(cert_path), 'certificate_sha256': digest(cert_path.read_bytes()) if cert_path.exists() else None,
              'structural': str(structural_path), 'arithmetic': str(arithmetic_path),
              'summary': result, 'structural_replays': bundle['manifests'] if bundle else [],
              'checks_passed': len(ch.labels), 'checks': ch.labels, 'failures': failures}
    out.write_text(json.dumps(report, indent=2)+'\n')
    print('dual replay:', result, '; failures', failures, '; report', out)
    return report


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('certificate', type=Path)
    p.add_argument('--structural', type=Path, required=True)
    p.add_argument('--arithmetic', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    report = verify(args.certificate, args.structural, args.arithmetic, args.out)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
