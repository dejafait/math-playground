"""Complete L145 cutoff-96 R spatial inclusion; no time/value evaluation.

Full integer entry certificates are streamed to gzip JSONL. --audit replays
every entry, dyadic inclusion, and moment-domain coverage.
The approved L082/L133 moment certificates are imported without regeneration.
"""
import argparse
import gzip
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

import numpy as np
import enclose_physical_h_contractions as ph
import check_g_cutoff96_coverage as coverage

ROOT = Path(__file__).parent
CERT = ROOT/'r-spatial-enclosure-certificate.json'
ENTRIES = ROOT/'r-spatial-integer-entries.jsonl.gz'
FACTORS = ROOT/'r-spatial-enclosure-factors.npz'
AUDIT = ROOT/'r-spatial-enclosure-audit.json'
K, en, rat, I, S = 96, ph.en, ph.rat, ph.I, ph.S
ZERO = rat(0)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


Spatial = ph.Spatial


def r_templates():
    keys, _, q = ph.templates()
    ids = {key: j for j, key in enumerate(keys)}
    types = lambda a: tuple('E' if j == a else 'V' for j in range(4))
    ordinary = lambda a: tuple((t, 'b') for t in types(a))
    def register(key):
        if key not in ids:
            ids[key] = len(keys)
            keys.append(key)
        return ids[key]
    def lift(a):
        rows = list(ordinary(0))
        rows[0], rows[a] = ('E', 'prefix'), ('V', 'd')
        return [(a, 1, ordinary(a)), (0, -1, tuple(rows))]
    m = []
    for a in (1, 2, 3):
        for alpha, sl, left in lift(a):
            for beta, sr, right in lift(a):
                mm = [register((ll, w, rr, False)) for ll, w, rr
                      in zip(left, ('f', 'r', 'fp', 'r'), right)]
                m.append((alpha, beta, F(sl*sr), mm))
    assert len(m) == 12 and len(q[3]) == 48 and len(q[6]) == 192
    return keys, m, q


def inputs():
    source_path = ROOT/'continuum-first-pair-enclosure-certificate.json'
    extra_path = ROOT/'physical-h-enclosure-certificate.json'
    scope_path = ROOT/'r-physical-reduction-certificate.json'
    source = json.loads(source_path.read_text())
    extra = json.loads(extra_path.read_text())
    scope = json.loads(scope_path.read_text())
    assert not source['failures'] and not extra['failures'] and not scope['failures']
    assert extra['moment_source_sha256'] == sha(source_path)
    assert source['script_sha256'] == sha(Path(en.__file__))
    assert extra['script_sha256'] == sha(Path(ph.__file__))
    assert source['input_sha256'] == sha(ROOT/'stored-fourier-enclosure-certificate.json')
    assert (source['K'], extra['K'], scope['tail']['cutoff'], int(source['scale'])) == (K, K, K, S)
    spatial = Spatial(source)
    for row in extra['added_moments']:
        key = row['h'], row['n']
        assert key not in spatial.moments
        spatial.moments[key] = en.read(row['real']), en.read(row['imag'])
    assert len(spatial.moments) == 1348
    assert set(spatial.moments) == ({(h,n) for h in (0,1,2) for n in range(-192,193)} | {(3,n) for n in range(-96,97)})
    keys, m, q = r_templates()
    for i in (3, 6):
        actual = [[a,b,str(c),[json.loads(json.dumps(keys[x])) for x in mm]] for a,b,c,mm in q[i]]
        expected = [[a,b,c,[extra['spatial_matrices'][x]['key'] for x in mm]]
                    for a,b,c,mm in extra['tensors'][f'Q_{i}']]
        assert actual == expected
    hashes = {p.name: sha(p) for p in (source_path, extra_path, scope_path, Path(__file__),
                                      Path(ph.__file__), Path(en.__file__), Path(coverage.__file__))}
    return spatial, keys, m, q, scope, hashes


def main(audit):
    spatial, keys, m, q, scope, hashes = inputs()
    active = sorted({ix for rows in [m, q[3], q[6]] for row in rows for ix in row[3]})
    checks = []
    failures = []
    required = set()
    for ix in active:
        key = keys[ix]
        left, _, right, _ = key
        for n in range(0 if left[0]=='E' else 1, K+1):
            for mm in range(0 if right[0]=='E' else 1, K+1):
                required.update(coverage.required_support(key,n,mm))
    assert required <= set(spatial.moments), ('uncovered-domain', sorted(required-set(spatial.moments)))
    indices = {'E': range(K+1), 'V': range(1, K+1)}
    saved = json.loads(CERT.read_text()) if audit else None
    archive = np.load(FACTORS) if audit else {}
    if audit:
        assert saved['hashes'] == hashes and saved['factor_sha256'] == sha(FACTORS)
        assert saved['integer_entries_sha256'] == sha(ENTRIES)
        assert saved['basis_checks'] == checks
        assert saved['required_moments'] == [list(x) for x in sorted(required)]
    entry_file = gzip.open(ENTRIES, 'rt' if audit else 'wt')
    total, axial, matrix_rows = 0, 0, []
    max_radius = 0.
    for ix in active:
        left, weight, right, ell = keys[ix]
        raw = []
        for ni, n in enumerate(indices[left[0]]):
            row = []
            for mi, mm in enumerate(indices[right[0]]):
                z = spatial.entry(left, weight, right, ell, n, mm)
                record = [ix, n, mm, str(z.lo), str(z.hi)]
                if audit:
                    assert json.loads(entry_file.readline()) == record
                    center, radius = F(float(archive[f'spatial_{ix}_c'][ni,mi])), F(float(archive[f'spatial_{ix}_r'][ni,mi]))
                else:
                    entry_file.write(json.dumps(record, separators=(',', ':'))+'\n')
                    cf, rf = en.sr.midpoint_radius(z)
                    center, radius = F(float(cf)), F(float(rf))
                if not center-radius <= F(z.lo, S) <= F(z.hi, S) <= center+radius:
                    failures.append(f'dyadic-inclusion-{ix}-{n}-{mm}')
                total += 1
                row.append(z)
            raw.append(row)
        c, r = en.enclosed(raw)
        if audit:
            assert np.array_equal(c, archive[f'spatial_{ix}_c'])
            assert np.array_equal(r, archive[f'spatial_{ix}_r'])
        else:
            archive[f'spatial_{ix}_c'], archive[f'spatial_{ix}_r'] = c, r
        if not np.all(np.isfinite(c)) or not np.all(np.isfinite(r)) or not np.all(r >= 0):
            failures.append(f'nonfinite-radius-{ix}')
        matrix_rows.append(dict(id=ix, key=keys[ix], rows=c.shape[0], cols=c.shape[1],
                                max_radius_hex=float(np.max(r)).hex(),
                                entries_checked=int(c.size), independent_axial=left[1] == 'upper'))
        max_radius = max(max_radius, float(np.max(r)))
        if len(matrix_rows) % 4 == 0 or len(matrix_rows) == len(active):
            print(f'{"Replayed" if audit else "Enclosed"} {len(matrix_rows)}/{len(active)} matrices; {total} entries', flush=True)
    if audit:
        assert not entry_file.readline()
    entry_file.close()
    assert total == sum(row['entries_checked'] for row in matrix_rows)
    assert spatial.used <= set(spatial.moments)
    radius_required = F(1, 1000000)
    if F(max_radius) >= radius_required:
        failures.append('max-spatial-radius-at-least-1e-6')
    summary = dict(matrix_count=len(active), entries_checked=total,
                   independent_axial_entries=axial, max_radius_hex=max_radius.hex(),
                   max_radius_upper_decimal=float(max_radius), required_max_radius='1/1000000',
                   used_moment_count=len(spatial.used), R_rows=len(m), Q3_rows=len(q[3]), Q6_rows=len(q[6]))
    if audit:
        assert json.loads(json.dumps(matrix_rows)) == saved['spatial_matrices']
        assert summary == saved['summary']
        assert [list(x) for x in sorted(spatial.used)] == saved['used_moments']
        result = dict(certificate_sha256=sha(CERT), summary=summary, failures=failures, passed=not failures,
                      qualification='Complete same-program integer entry replay and dyadic containment; not formal verification.')
        AUDIT.write_text(json.dumps(result, indent=2)+'\n')
        print(f'Audit {"PASS" if not failures else "FAIL"}; failures {len(failures)}; {AUDIT}')
    else:
        np.savez_compressed(FACTORS, **archive)
        result = dict(K=K, scale=str(S), hashes=hashes, factor_archive=FACTORS.name,
                      factor_sha256=sha(FACTORS), integer_entries=ENTRIES.name,
                      integer_entries_sha256=sha(ENTRIES), basis_checks=checks, required_moments=[list(x) for x in sorted(required)],
                      R_rows=coverage.rows_record(m), Q3_rows=coverage.rows_record(q[3]),
                      Q6_rows=coverage.rows_record(q[6]), spatial_matrices=matrix_rows,
                      used_moments=[list(x) for x in sorted(spatial.used)], summary=summary,
                      failures=failures, passed=not failures,
                      qualification='Spatial factors only; no time/tensor enclosure, B_R value, sign or compensation.')
        CERT.write_text(json.dumps(result, indent=2)+'\n')
        print(f'Spatial {"PASS" if not failures else "FAIL"}; max radius {max_radius:.12g}; required <1e-6; failures {len(failures)}; {CERT}; {ENTRIES}; {FACTORS}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit', action='store_true')
    main(parser.parse_args().audit)
