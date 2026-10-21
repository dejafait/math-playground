#!/usr/bin/env python3
"""BSD-188 fixed N=36 audit supplement; imports neither producer nor checker.

Run after the full independent replay described in L038. Reconstructs
reflection without continued fractions and tests six altered certificates.
Full witnesses/reports are saved, while stdout contains bounded summaries.
"""
import copy
import hashlib
import json
import subprocess
import sys
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/conductor36-table/structural-critical-audit'
CERT = ROOT / 'scripts/conductor36-table/presentation.json'
OLD = ROOT / 'scripts/conductor36-table/presentation_verification.json'
VERIFIER = ROOT / 'scripts/general-relative/verify_certificate.py'
EXPECTED = {
    'scripts/general-relative/build_certificate.py': '414dee8b0124fa708e22a6f1cf609bfb961f7281929bc267e167614a98890f85',
    'scripts/general-relative/verify_certificate.py': '3829bd972ac9d213aea5e983580aa0f801f4b0dbd8564c95e0410de856ae4596',
    'scripts/conductor36-table/presentation.json': 'aaeb1c9f4e25bfd62aa17e7719e6142c087f801033f7fb4ee2a7431dc298a5e4',
    'scripts/conductor36-table/presentation_verification.json': '6408d132cb0c799d9c8bb51307e7dc6e6051f2e14cffbf5cc368c8390a963039',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def transpose(a):
    return list(map(list, zip(*a)))


def product(a, b):
    columns = transpose(b)
    require(len(a[0]) == len(b), 'independent product dimensions')
    return [[sum(x*y for x, y in zip(row, col)) for col in columns] for row in a]


def point(p, q):
    require(p != 0 or q != 0, 'nonzero projective point')
    if q == 0:
        return [1, 0]
    d = gcd(p, q) * (1 if q > 0 else -1)
    return [p//d, q//d]


def independent(cert):
    pr = cert['presentation']
    require(cert['inputs'] == {'N': 36, 'P': []}, 'fixed domain')
    require((pr['s'], pr['r'], pr['d']) == (72, 59, 13), 'fixed dimensions')
    require(pr['diagonal'] == [1]*59, 'unit pivots in this instance')
    A = cert['A']['entries']
    U = pr['U']['entries']
    K = pr['K']['entries']
    Pi, Q = pr['Pi']['entries'], pr['Q']['entries']
    # U A W = D implies A^t U^t = W^(-t) D^t.
    # All 59 pivots are one, hence these 59 combinations are exactly K.
    combinations = [row[:59] for row in transpose(U)]
    rebuilt_kernel = product(transpose(A), combinations)
    require(rebuilt_kernel == K, 'all saturated columns in raw integral lattice')
    lifts = cert['cosets']['lifts']
    reps = cert['cosets']['representatives']
    units = [u for u in range(36) if gcd(u, 36) == 1]
    witnesses, permutation, image_columns = [], [], []
    Y = cert['operators']['J']['Y']['entries']
    for i, (a, b, c, d) in enumerate(lifts):
        h = [a, -b, -c, d]  # conjugation by diag(-1,1)
        require(a*d-b*c == 1, 'lift determinant')
        matches = [(j, u) for j, (v, w) in enumerate(reps) for u in units
                   if (u*v+c) % 36 == 0 and (u*w-d) % 36 == 0]
        require(len(matches) == 1, 'unique conjugate lift unit/coset')
        j, u = matches[0]
        aa, bb, cc, dd = lifts[j]
        gamma = [a*dd+b*cc, -a*bb-b*aa,
                 -c*dd-d*cc, c*bb+d*aa]
        require(gamma[0]*gamma[3]-gamma[1]*gamma[2] == 1 and gamma[2] % 36 == 0,
                'direct conjugate lookup Gamma0')
        endpoints = [point(-b, d), point(a, -c)]
        original = [point(b, d), point(a, c)]
        reflected = [point(-p, q) for p, q in original]
        require(endpoints == reflected, 'unchanged endpoint order under reflection')
        recorded = cert['operators']['J']['paths'][i][0]
        require(endpoints == [recorded['start'], recorded['end']], 'saved reflected endpoints')
        coords = [row[j] for row in Pi]
        require(coords == [row[i] for row in Y] == recorded['coordinates'],
                'single reflected Manin generator equals complete saved path image')
        permutation.append(j)
        image_columns.append(coords)
        witnesses.append({'generator': i, 'conjugated_lift': h, 'coset': j, 'unit': u,
                          'gamma': gamma, 'endpoints': endpoints, 'coordinates': coords})
    require(sorted(permutation) == list(range(72)), 'direct reflection is a permutation')
    require(all(permutation[permutation[i]] == i for i in range(72)), 'permutation involution')
    direct_Y = transpose(image_columns)
    direct_B = product(direct_Y, Q)
    require(direct_B == cert['operators']['J']['B']['entries'], 'entire direct basis matrix')
    require(product(direct_B, Pi) == direct_Y, 'entire direct generator reconstruction')
    sign_witness = next(({'row': j, 'column': i, 'value': direct_Y[j][i]}
                         for j in range(13) for i in range(72) if direct_Y[j][i]), None)
    require(sign_witness is not None, 'reflection distinct from negative reflection')
    return {'raw_relation_combinations_for_K': combinations, 'reconstructed_K': rebuilt_kernel,
            'reflection_witnesses': witnesses, 'permutation': permutation,
            'direct_Y': direct_Y, 'direct_B': direct_B, 'sign_witness': sign_witness,
            'actual': {'integral_kernel_columns': 59, 'reflection_generators': 72,
                       'basis_matrix_entries': 169},
            'required': {'integral_kernel_columns': 59, 'reflection_generators': 72,
                         'basis_matrix_entries': 169}, 'failures': []}


def reject_case(cert, name, mutate, expected):
    altered = copy.deepcopy(cert)
    mutate(altered)
    source = OUT / (name + '.json')
    report_path = OUT / (name + '-report.json')
    save(source.name, altered)
    proc = subprocess.run([sys.executable, str(VERIFIER.relative_to(ROOT)),
                           str(source.relative_to(ROOT)), '--level', '36',
                           '--out', str(report_path.relative_to(ROOT))],
                          cwd=ROOT, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(proc.stdout + proc.stderr)
    report = json.loads(report_path.read_text())
    require(proc.returncode == 1, name + ': must reject')
    require(report['sha256'] == digest(source), name + ': input hash binding')
    require(report['failures'] == ['ReplayError: ' + expected], name + ': specific contract rejection')
    return {'name': name, 'returncode': proc.returncode, 'failures': report['failures'],
            'certificate': str(source.relative_to(ROOT)),
            'report': str(report_path.relative_to(ROOT)), 'sha256': digest(source)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    result = {'failures': [], 'rejections': []}
    before = {p: digest(ROOT / p) for p in EXPECTED}
    result['original_hashes_before'] = before
    try:
        require(before == EXPECTED, 'original files match approved snapshot')
        cert = json.loads(CERT.read_text())
        full = json.loads((OUT / 'full_replay.json').read_text())
        old = json.loads(OLD.read_text())
        require(full == old, 'complete fresh report equality, including every check label')
        require(full['failures'] == [] and full['checks_passed'] == len(full['checks']) == 149753,
                'complete successful full replay')
        require(full['sha256'] == before[str(CERT.relative_to(ROOT))], 'full replay hash binding')
        required = {'orbit_assignments': 864, 'cosets': 72, 'relations': 144,
                    'relation_lookups': 216, 'paths': 144, 'row_operations': 287,
                    'column_operations': 172, 'inverse_row_operations': 287,
                    'inverse_column_operations': 172, 'source_relation_images': 144,
                    'saturated_kernel_images': 59, 'reconstructed_generator_images': 72}
        require(full['required'] == required, 'independent fixed required domain')
        require(full['actual'] == dict(required, segments=626), 'all actual counts')
        result['full_replay'] = {'path': str((OUT / 'full_replay.json').relative_to(ROOT)),
                                 'sha256': digest(OUT / 'full_replay.json'),
                                 'checks_passed': full['checks_passed'],
                                 'actual': full['actual'], 'required': required,
                                 'equals_entire_production_report': True}
        evidence = independent(cert)
        save('independent_identities.json', evidence)
        result['independent'] = {'path': str((OUT / 'independent_identities.json').relative_to(ROOT)),
                                  'actual': evidence['actual'], 'required': evidence['required'],
                                  'sign_witness': evidence['sign_witness']}
        cases = [
            ('bad-unit-assignment', lambda x: x['cosets']['assignments'][0].__setitem__('unit', 0),
             'coset completeness: assignment complete and congruent'),
            ('bad-relation', lambda x: x['A']['entries'][0].__setitem__(0, x['A']['entries'][0][0]+1),
             'complete Manin relations: all relations including multiplicity'),
            ('bad-column-inverse', lambda x: x['presentation']['W_inverse']['entries'][0].__setitem__(
                0, x['presentation']['W_inverse']['entries'][0][0]+1),
             'unimodular replay: W_inverse reconstructed'),
            ('bad-generator-coordinate', lambda x: x['presentation']['generator_coordinates'][0].__setitem__(
                0, x['presentation']['generator_coordinates'][0][0]+1),
             'integral saturation: every generator integral coordinates'),
            ('reversed-reflection-path', lambda x: x['operators']['J']['paths'][0][0].update(
                start=x['operators']['J']['paths'][0][0]['end'],
                end=x['operators']['J']['paths'][0][0]['start']),
             'J entire operator: path endpoints'),
            ('negative-reflection-matrix', lambda x: x['operators']['J']['B'].__setitem__(
                'entries', [[-v for v in row] for row in x['operators']['J']['B']['entries']]),
             'J entire operator: basis matrix YQ'),
        ]
        for name, mutate, expected in cases:
            entry = reject_case(cert, name, mutate, expected)
            result['rejections'].append(entry)
            save('manifest.json', result)
            print(name + ': rejected at required contract check', flush=True)
        result['rejection_count'] = {'actual': len(result['rejections']), 'required': 6}
    except Exception as error:
        result['failures'].append(type(error).__name__ + ': ' + str(error))
    finally:
        after = {p: digest(ROOT / p) for p in EXPECTED}
        result['original_hashes_after'] = after
        result['original_bytes_preserved'] = before == after == EXPECTED
        if not result['original_bytes_preserved']:
            result['failures'].append('original byte preservation failed')
        result['audit_script_sha256'] = digest(Path(__file__))
        save('manifest.json', result)
    print('full replay: 144/144 paths, 626 segments; independent: 72/72 reflection images, 59/59 integral kernel columns'
          if 'independent' in result else 'independent audit incomplete')
    print(f"failures={len(result['failures'])}; original_bytes_preserved={result['original_bytes_preserved']}; "
          f"report={OUT.relative_to(ROOT) / 'manifest.json'}")
    for failure in result['failures']:
        print(failure)
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
