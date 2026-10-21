"""Complete L140 cutoff-96 spatial inclusion; no time or G-value evaluation.

Full integer entry certificates are streamed to gzip JSONL. --audit replays
every entry, dyadic inclusion, and independent axial product-to-sum formulas.
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
CERT = ROOT/'g-spatial-enclosure-certificate.json'
ENTRIES = ROOT/'g-spatial-integer-entries.jsonl.gz'
FACTORS = ROOT/'g-spatial-enclosure-factors.npz'
AUDIT = ROOT/'g-spatial-enclosure-audit.json'
K, en, rat, I, S = 96, ph.en, ph.rat, ph.I, ph.S
ZERO = rat(0)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


class Spatial(ph.Spatial):
    @lru_cache(None)
    def basis(self, typ, kind, n):
        if kind == 'dd':
            # Includes E_0''=0, without a division by its frequency.
            assert n > 0 or typ == 'E'
            if not n:
                return {}
            freq = rat(n)*self.omega
            factor = -(freq*freq)
            return {key: (value[0]*factor, value[1]*factor)
                    for key, value in super().basis(typ, 'b', n).items()}
        if kind != 'upper':
            return super().basis(typ, kind, n)
        assert typ == 'V' and 1 <= n <= K
        freq = rat(n)*self.omega
        # Each shifted cosine exponential contributes 1/(4 freq).
        out = {}
        for sign in (-1, 1):
            phase = ((1, 0), (0, 1), (-1, 0), (0, -1))[(sign*n) % 4]
            out[sign*n, 0] = (rat(phase[0])/(rat(4)*freq),
                              rat(phase[1])/(rat(4)*freq))
        out[0, 0] = (-rat((-1)**n)/(rat(2)*freq), ZERO)
        return out

    def weighted_phase(self, n, coefficients, part):
        """Integral of polynomial*rho times shifted sine/cosine."""
        total = (ZERO, ZERO)
        for h, coefficient in coefficients.items():
            moment = self.moments[h, n]
            total = self.add(total, (rat(coefficient)*moment[0],
                                     rat(coefficient)*moment[1]))
        phase = ((1, 0), (0, 1), (-1, 0), (0, -1))[n % 4]
        return self.multiply(total, (rat(phase[0]), rat(phase[1])))[part]

    def independent_axial(self, right, n, m):
        """Direct real product-to-sum, independent of polynomial convolution."""
        freq = rat(n)*self.omega
        endpoint = rat((-1)**n)
        if m:
            sine = lambda q: self.weighted_phase(q, {2: 1, 1: 4}, 1)
            value = ((sine(m+n)+sine(m-n))/rat(2)-endpoint*sine(m))/(rat(4)*freq)
            if right == ('E', 'prefix'):
                value = value/(rat(m)*self.omega)
            else:
                assert right == ('V', 'b')
            return value
        assert right == ('E', 'prefix')
        # ell*f*p0 = x(x+4)^2 rho/sqrt(8).
        coefficients = {3: 1, 2: 8, 1: 16}
        cosine = self.weighted_phase(n, coefficients, 0)
        constant = self.weighted_phase(0, coefficients, 0)
        return self.norm0*(cosine-endpoint*constant)/(rat(2)*freq)


def exact_basis_checks():
    """Rational complex coefficients with omega factored out."""
    rows = []
    def mul(z, w):
        return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]
    for n in range(1, K+1):
        cosine = {}
        sine = {}
        for sign in (-1, 1):
            phase = ((1, 0), (0, 1), (-1, 0), (0, -1))[(sign*n) % 4]
            cosine[sign] = mul((F(1, 4), F(0)), phase)
            sine[sign] = mul((F(0), F(-sign, 4)), phase)
        # j derivative: multiply cosine/(n omega) by i sign n omega.
        differences = [tuple(x+y for x, y in zip(mul(cosine[s], (0, s)), sine[s]))
                       for s in (-1, 1)]
        endpoint = tuple(sum(mul(cosine[s], ((1, 0), (0, 1), (-1, 0), (0, -1))[(s*n) % 4])[p]
                             for s in (-1, 1))- (F((-1)**n, 2) if p == 0 else 0)
                         for p in (0, 1))
        passed = all(x == 0 for z in differences+[endpoint] for x in z)
        rows.append(dict(n=n, derivative_differences=[[str(x) for x in z] for z in differences],
                         endpoint_difference=[str(x) for x in endpoint], passed=passed))
    return rows


def inputs():
    source_path = ROOT/'continuum-first-pair-enclosure-certificate.json'
    extra_path = ROOT/'physical-h-enclosure-certificate.json'
    scope_path = ROOT/'g-cutoff96-coverage-certificate.json'
    source = json.loads(source_path.read_text())
    extra = json.loads(extra_path.read_text())
    scope = json.loads(scope_path.read_text())
    assert not source['failures'] and not extra['failures'] and not scope['failures']
    assert extra['moment_source_sha256'] == sha(source_path)
    assert source['script_sha256'] == sha(Path(en.__file__))
    assert extra['script_sha256'] == sha(Path(ph.__file__))
    assert source['input_sha256'] == sha(ROOT/'stored-fourier-enclosure-certificate.json')
    assert (source['K'], extra['K'], scope['cutoff'], int(source['scale'])) == (K, K, K, S)
    spatial = Spatial(source)
    for row in extra['added_moments']:
        key = row['h'], row['n']
        assert key not in spatial.moments
        spatial.moments[key] = en.read(row['real']), en.read(row['imag'])
    assert len(spatial.moments) == 1348
    assert set(spatial.moments) == {tuple(k) for k in scope['certified_domain']}
    keys, m, q = coverage.g_templates()
    assert scope['G_rows'] == coverage.rows_record(m)
    for i in (3, 6):
        assert scope[f'Q{i}_rows'] == coverage.rows_record(q[i])
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
    checks = exact_basis_checks()
    failures = [f'basis-{r["n"]}' for r in checks if not r['passed']]
    indices = {'E': range(K+1), 'V': range(1, K+1)}
    saved = json.loads(CERT.read_text()) if audit else None
    archive = np.load(FACTORS) if audit else {}
    if audit:
        assert saved['hashes'] == hashes and saved['factor_sha256'] == sha(FACTORS)
        assert saved['integer_entries_sha256'] == sha(ENTRIES)
        assert saved['basis_checks'] == checks
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
                if left == ('V', 'upper'):
                    assert weight == 'f' and ell
                    independent = spatial.independent_axial(right, n, mm)
                    difference = z-independent
                    if not difference.lo <= 0 <= difference.hi:
                        failures.append(f'axial-product-to-sum-{ix}-{n}-{mm}')
                    # Enclose both equivalent formulas, so independent checks
                    # remain corroboration rather than a numerical premise.
                    axial += 1
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
    assert total == scope['summary']['entries_checked'] == 259682
    assert len(active) == 28 and axial == 18528
    assert spatial.used <= set(spatial.moments)
    required = F(1, 1000000)
    if F(max_radius) >= required:
        failures.append('max-spatial-radius-at-least-1e-6')
    summary = dict(matrix_count=len(active), entries_checked=total,
                   independent_axial_entries=axial, max_radius_hex=max_radius.hex(),
                   max_radius_upper_decimal=float(max_radius), required_max_radius='1/1000000',
                   used_moment_count=len(spatial.used), G_rows=len(m), Q3_rows=len(q[3]), Q6_rows=len(q[6]))
    if audit:
        assert json.loads(json.dumps(matrix_rows)) == saved['spatial_matrices']
        assert summary == saved['summary']
        assert [list(x) for x in sorted(spatial.used)] == saved['used_moments']
        result = dict(certificate_sha256=sha(CERT), summary=summary, failures=failures, passed=not failures,
                      qualification='Full same-program entry replay and independent axial identities; not formal verification.')
        AUDIT.write_text(json.dumps(result, indent=2)+'\n')
        print(f'Audit {"PASS" if not failures else "FAIL"}; failures {len(failures)}; {AUDIT}')
    else:
        np.savez_compressed(FACTORS, **archive)
        result = dict(K=K, scale=str(S), hashes=hashes, factor_archive=FACTORS.name,
                      factor_sha256=sha(FACTORS), integer_entries=ENTRIES.name,
                      integer_entries_sha256=sha(ENTRIES), basis_checks=checks,
                      G_rows=coverage.rows_record(m), Q3_rows=coverage.rows_record(q[3]),
                      Q6_rows=coverage.rows_record(q[6]), spatial_matrices=matrix_rows,
                      used_moments=[list(x) for x in sorted(spatial.used)], summary=summary,
                      failures=failures, passed=not failures,
                      qualification='Spatial factors only; no time/tensor enclosure, B_G value, sign or compensation.')
        CERT.write_text(json.dumps(result, indent=2)+'\n')
        print(f'Spatial {"PASS" if not failures else "FAIL"}; max radius {max_radius:.12g}; required <1e-6; failures {len(failures)}; {CERT}; {ENTRIES}; {FACTORS}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit', action='store_true')
    main(parser.parse_args().audit)
