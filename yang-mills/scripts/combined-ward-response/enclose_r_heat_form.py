"""L145 signed R heat form with complete R spatial and L082 time intervals.

Full certificates retain every matched signed term. --audit checks all
coverage, source identities and exact dyadic aggregation; tensor inclusion
uses L039's qualified IEEE induction, not independent BLAS verification.
"""
import argparse
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import numpy as np
import enclose_physical_h_contractions as ph
import enclose_r_spatial as coverage
from check_g_cutoff96_coverage import rows_record

ROOT = Path(__file__).parent
CERT = ROOT/'r-heat-enclosure-certificate.json'
AUDIT = ROOT/'r-heat-enclosure-audit.json'
en, rat, sr = ph.en, ph.rat, ph.sr
sha, fraction = ph.sha, ph.fraction
K, CR, A = 96, 160380, 82944
NORM = {3: 6050, 6: 1640736}
SCALAR = F(-61, 1000), F(-43, 1000)
types = lambda a: tuple('E' if j == a else 'V' for j in range(4))


def inputs():
    spatial_path = ROOT/'r-spatial-enclosure-certificate.json'
    spatial = json.loads(spatial_path.read_text())
    audit_path = ROOT/'r-spatial-enclosure-audit.json'
    audit = json.loads(audit_path.read_text())
    assert spatial['passed'] and not spatial['failures']
    assert audit['passed'] and not audit['failures']
    assert audit['certificate_sha256'] == sha(spatial_path)
    factors_path = ROOT/spatial['factor_archive']
    assert spatial['factor_sha256'] == sha(factors_path)
    for name, digest in spatial['hashes'].items():
        assert digest == sha(ROOT/name), ('spatial-input-hash', name)
    assert spatial['integer_entries_sha256'] == sha(ROOT/spatial['integer_entries'])
    keys, m, q = coverage.r_templates()
    assert spatial['R_rows'] == rows_record(m)
    for i in (3, 6):
        assert spatial[f'Q{i}_rows'] == rows_record(q[i])
    active = sorted({x for rows in [m, q[3], q[6]] for row in rows for x in row[3]})
    assert active == [r['id'] for r in spatial['spatial_matrices']]
    archive = np.load(factors_path)
    assert set(archive.files) == {f'spatial_{ix}_{p}' for ix in active for p in ('c', 'r')}
    matrices = {}
    for row in spatial['spatial_matrices']:
        ix = row['id']
        assert row['key'] == json.loads(json.dumps(keys[ix]))
        z = archive[f'spatial_{ix}_c'], archive[f'spatial_{ix}_r']
        left, _, right, _ = keys[ix]
        assert z[0].shape == z[1].shape == (K+(left[0]=='E'), K+(right[0]=='E'))
        assert z[0].shape == (row['rows'], row['cols'])
        assert np.all(np.isfinite(z[0])) and np.all(np.isfinite(z[1])) and np.all(z[1] >= 0)
        assert float(np.max(z[1])).hex() == row['max_radius_hex']
        matrices[ix] = z
    source_path = ROOT/'continuum-first-pair-enclosure-certificate.json'
    source = json.loads(source_path.read_text())
    assert not source['failures'] and (source['K'], source['degree']) == (96, 28)
    assert source['script_sha256'] == sha(Path(en.__file__))
    heat_path = ROOT/source['factor_archive']
    assert source['factor_archive_sha256'] == sha(heat_path)
    imported = np.load(heat_path)
    he = imported['heat_c'], imported['heat_r']
    weights = imported['weights_c'], imported['weights_r']
    assert he[0].shape == he[1].shape == (644, 97)
    assert weights[0].shape == weights[1].shape == (644,)
    for c, r in (he, weights):
        assert np.all(np.isfinite(c)) and np.all(np.isfinite(r)) and np.all(r >= 0)
        assert np.all(c-r >= 0)
    heat = {'E': he, 'V': (he[0][:, 1:], he[1][:, 1:])}
    # Both zero and positive edge indices use the same certified source arrays.
    tail_path = ROOT/'r-physical-reduction-certificate.json'
    tail = json.loads(tail_path.read_text())
    assert not tail['failures']
    scalar_path = ROOT/'g-scalar-enclosure-certificate.json'
    scalar_audit_path = ROOT/'g-scalar-enclosure-audit.json'
    scalar_audit = json.loads(scalar_audit_path.read_text())
    assert not scalar_audit['failures']
    assert scalar_audit['certificate_sha256'] == sha(scalar_path)
    sl, sh = (F(scalar_audit['bounds_replayed'][key]) for key in ('lower', 'upper'))
    assert SCALAR[0] < sl <= sh < SCALAR[1]
    hashes = {p.name: sha(p) for p in (spatial_path, audit_path, factors_path, source_path,
                                     heat_path, tail_path, scalar_path, scalar_audit_path,
                                     Path(__file__), Path(ph.__file__), Path(en.__file__),
                                     Path(sr.__file__), Path(coverage.__file__))}
    return keys, m, q, matrices, heat, weights, source, tail, hashes


def errors(source, tail, i):
    rq = F(factorial(28)**4, 57*factorial(56)**3)*(1+22*factorial(57))
    rt = en.ar.exp_negative(rat(108)).absolute_upper()
    assert rq == fraction(source['relative_quadrature_error'])
    assert rt == fraction(source['relative_time_tail'])
    rel = rq+rt
    te = CR*NORM[i]*A*A*(2*rel+rel*rel)
    omission = CR*NORM[i]*2717908992/F(20**27)
    assert omission == fraction(tail['tail']['B_actual_upper_bound'])*F(NORM[i],NORM[6])
    return rel, te, omission


def main(audit):
    keys, m, q, matrices, heat, weights, source, tail, hashes = inputs()
    expected, expected_features = [], set()
    for i in (3, 6):
        for im, (a, b, cm, mm) in enumerate(m):
            for iq, (qa, qb, cq, qq) in enumerate(q[i]):
                if (qa, qb) != (b, a):
                    continue
                expected.append((i, im, iq, str(cm*cq)))
                expected_features.update((mid, qid, types(a)[j], types(b)[j])
                                         for j, (mid, qid) in enumerate(zip(mm, qq)))
    cache, feature_records = {}, []
    finite_checks = 0

    def checked(z):
        nonlocal finite_checks
        assert np.all(np.isfinite(z[0])) and np.all(np.isfinite(z[1])) and np.all(z[1] >= 0)
        finite_checks += 1
        return z

    def feature(mid, qid, ta, tb):
        key = mid, qid, ta, tb
        if key not in cache:
            # The trace pairs M(alpha,beta) with Q(beta,alpha).
            prod = checked(sr.multiply(matrices[mid], en.trans(matrices[qid])))
            value = checked(sr.dot(checked(sr.dot(heat[ta], prod)), en.trans(heat[tb])))
            cache[key] = value
            feature_records.append(dict(M_matrix=mid, Q_matrix=qid, left_type=ta, right_type=tb))
        return cache[key]

    def integrate(z):
        total = en.exact(0.)
        for a in range(0, 644, 160):
            for b in range(0, 644, 160):
                aa, bb = min(a+160, 644), min(b+160, 644)
                block = z[0][a:aa, b:bb], z[1][a:aa, b:bb]
                wa = weights[0][a:aa], weights[1][a:aa]
                wb = weights[0][b:bb], weights[1][b:bb]
                total = checked(sr.add(total, checked(sr.dot(checked(sr.dot(wa, block)), wb))))
        return total

    if audit:
        data = json.loads(CERT.read_text())
        assert data['hashes'] == hashes and not data['failures']
        records, results, combined = data['tensor_terms'], data['results'], data['combined']
        actual = [(r['probe'], r['M'], r['Q'], r['coefficient']) for r in records]
        assert actual == expected and len(actual) == len(set(actual))
        actual_features = {(r['M_matrix'], r['Q_matrix'], r['left_type'], r['right_type'])
                           for r in data['coordinate_features']}
        assert actual_features == expected_features
        assert len(actual_features) == len(data['coordinate_features'])
    else:
        records, results, combined = [], [], []
        for i in (3, 6):
            total = en.exact(0.)
            for im, (a, b, cm, mm) in enumerate(m):
                for iq, (qa, qb, cq, qq) in enumerate(q[i]):
                    if (qa, qb) != (b, a):
                        continue
                    value = en.exact(np.ones((644, 644)))
                    for j, (mid, qid) in enumerate(zip(mm, qq)):
                        value = checked(sr.multiply(value, feature(mid, qid, types(a)[j], types(b)[j])))
                    term = integrate(checked(sr.multiply(value, en.enclosed(rat(cm*cq)))))
                    total = checked(sr.add(total, term))
                    records.append(dict(probe=i, M=im, Q=iq, coefficient=str(cm*cq), integral=en.pair(term)))
            rel, te, omission = errors(source, tail, i)
            c, r = F(float(total[0])), F(float(total[1]))
            error = r+te+omission
            lo, hi = c-error, c+error
            results.append(dict(probe=i, terms=sum(x['probe']==i for x in records), retained=en.pair(total),
                                time_error=en.rational(te), spectral_tail=en.rational(omission),
                                total_error=en.rational(error), lower=en.rational(lo), upper=en.rational(hi)))
            ends = [x*s for x in (lo, hi) for s in SCALAR]
            gl, gh = min(ends), max(ends)
            combined.append(dict(probe=i, lower=en.rational(gl), upper=en.rational(gh),
                                 sign='positive' if gl>0 else ('negative' if gh<0 else 'unresolved')))
            print(f'Probe {i}: B center {float(c):.12g}; spatial/arithmetic {float(r):.6g}; time {float(te):.6g}; omission {float(omission):.6g}; total {float(error):.6g}, required <1', flush=True)
            print(f'R {i}: ({float(gl):.12g}, {float(gh):.12g}); sign {combined[-1]["sign"]}', flush=True)
        assert [(r['probe'], r['M'], r['Q'], r['coefficient']) for r in records] == expected
        assert set(cache) == expected_features

    # Exact rational audit of all records and both endpoint products.
    endpoints = []
    failures = []
    assert [r['probe'] for r in results] == [3, 6]
    assert [r['probe'] for r in combined] == [3, 6]
    for row, combo in zip(results, combined):
        i = row['probe']
        terms = [r for r in records if r['probe']==i]
        assert row['terms'] == len(terms)
        ll=hh=F(0)
        for term in terms:
            c, r = (F(float.fromhex(term['integral'][key])) for key in ('center_hex', 'radius_hex'))
            assert r>=0
            ll+=c-r; hh+=c+r
        c, r = (F(float.fromhex(row['retained'][key])) for key in ('center_hex', 'radius_hex'))
        assert c-r<=ll<=hh<=c+r
        rel, te, omission = errors(source, tail, i)
        error = r+te+omission
        lo, hi = c-error, c+error
        assert fraction(row['time_error']) == te and fraction(row['spectral_tail']) == omission
        assert fraction(row['total_error']) == error
        assert fraction(row['lower']) == lo and fraction(row['upper']) == hi
        ends = [x*s for x in (lo, hi) for s in SCALAR]
        gl, gh = min(ends), max(ends)
        assert fraction(combo['lower']) == gl and fraction(combo['upper']) == gh
        assert combo['sign'] == ('positive' if gl>0 else ('negative' if gh<0 else 'unresolved'))
        if not error < 1:
            failures.append(f'physical-error-{i}-at-least-one')
        endpoints.append(dict(probe=i, terms=len(terms), physical_error_preview=float(error),
                              B_lower_preview=float(lo), B_upper_preview=float(hi),
                              R_lower_preview=float(gl), R_upper_preview=float(gh), sign=combo['sign']))
    if audit:
        assert fraction(data['relative_time_error']) == rel
        assert data['summary']['terms'] == len(expected)
        assert data['summary']['features'] == len(expected_features)
        out = dict(certificate_sha256=sha(CERT), passed=not failures, failures=failures,
                   terms_checked=len(expected), features_checked=len(expected_features), results=endpoints,
                   qualifications=['All signed records, dyadic aggregation, time/spectral allowances and scalar products checked.',
                                   'Complete R spatial replay imported; BLAS inclusion relies on L039 IEEE model, not independent tensor recomputation.'])
        AUDIT.write_text(json.dumps(out, indent=2)+'\n')
        print(f'Audit {"PASS" if not failures else "FAIL"}: {len(expected)} terms; {len(expected_features)} features; failures {len(failures)}; {AUDIT}', flush=True)
    else:
        out = dict(K=K, hashes=hashes, R_rows=rows_record(m),
                   Q3_rows=rows_record(q[3]), Q6_rows=rows_record(q[6]),
                   coordinate_features=feature_records, tensor_terms=records, results=results, combined=combined,
                   relative_time_error=en.rational(rel), heat_sums=dict(A=A, C_R=CR),
                   summary=dict(terms=len(records), features=len(cache), finite_radius_checks=finite_checks),
                   failures=failures, arithmetic_model='L039 IEEE binary64 add/product/FMA; no overflow; local underflow allowance 1e-290',
                   qualifications=['Imports complete R spatial intervals and L082 heat/weight intervals.',
                                   'Full signed tensor/time inclusion under the stated IEEE model; no independent processor verification.',
                                   'Triplet transverse-H, full compensation and interacting theory remain unresolved.'])
        CERT.write_text(json.dumps(out, indent=2)+'\n')
        print(f'Failures {len(failures)}; full certificate {CERT}', flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit', action='store_true')
    main(parser.parse_args().audit)
