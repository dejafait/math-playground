"""L140 full unsplit-heat omission and containing moment scope at cutoff 96.

No retained integration or G sign is evaluated. The symbolic supports
are containing unions: coefficient cancellations can only reduce them.
The canonical proof supplies the analytic inequalities and row identities.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from pathlib import Path

from enclose_physical_h_contractions import templates

ROOT = Path(__file__).parent
CERT = ROOT / 'g-cutoff96-coverage-certificate.json'
AUDIT = ROOT / 'g-cutoff96-coverage-audit.json'
K = 96


def rational(v):
    v = F(v)
    return dict(numerator=str(v.numerator), denominator=str(v.denominator))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


@lru_cache(None)
def basis_support(typ, kind, n):
    if n == 0:
        assert typ == 'E' and kind != 'upper'
        if kind == 'b':
            return frozenset({(0, 0)})
        if kind == 'prefix':
            return frozenset({(0, 0), (0, 1)})
        assert kind in ('d', 'dd')
        return frozenset()
    assert kind in ('b', 'd', 'dd', 'prefix', 'upper')
    if kind == 'upper':
        assert typ == 'V'
        # [cos(n omega (x+4))-(-1)^n]/(2 n omega).
        return frozenset({(-n, 0), (n, 0), (0, 0)})
    if kind == 'prefix':
        assert typ == 'E'
    return frozenset({(-n, 0), (n, 0)})


def product_support(left, right):
    return {(n+m, h+j) for n, h in left for m, j in right}


def derivative_support(poly):
    # d[x^h exp(i n omega x)] has these two possibly nonzero terms.
    return ({(n, h) for n, h in poly if n}
            | {(n, h-1) for n, h in poly if h})


def required_support(key, n, m):
    left, weight, right, ell = key
    poly = product_support(basis_support(*left, n), basis_support(*right, m))
    if ell:
        poly = product_support(poly, {(0, 0), (0, 1)})
    base, count = {'r': (0, 0), 'f': (1, 0), 'rp': (0, 1),
                   'fp': (1, 1), 'fpp': (1, 2)}[weight]
    for _ in range(count):
        poly = derivative_support(poly)
    return {(h+base, freq) for freq, h in poly}


def g_templates():
    # Q is imported unchanged from L132/L133; old H physical rows are unused.
    keys, _, q = templates()
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
    weights = ('f', 'r', 'fp', 'r')
    for alpha in (1, 2, 3):
        j_rows = []
        for b in (1, 2, 3):
            if b == alpha:
                continue
            rows = list(ordinary(alpha))
            rows[0] = ('V', 'upper')
            rows[b] = (types(alpha)[b], 'dd')
            j_rows.append((alpha, -1, tuple(rows)))
        for a in (1, 2, 3):
            if a == alpha:
                continue
            rows = list(ordinary(alpha))
            rows[0] = ('V', 'upper')
            for axis in (a, alpha):
                rows[axis] = (types(alpha)[axis], 'd')
            j_rows.append((a, 1, tuple(rows)))
        for a, sl, left in j_rows:
            for beta, sr, right in lift(a):
                mm = [register((ll, w, rr, j == 0))
                      for j, (ll, w, rr) in enumerate(zip(left, weights, right))]
                m.append((alpha, beta, F(sl*sr), mm))
    return keys, m, q


def rows_record(rows):
    return [dict(left_component=a+1, right_component=b+1,
                 coefficient=rational(c), matrices=mm) for a, b, c, mm in rows]


def generate():
    failures = []
    taylor = sum((F(3**j, factorial(j)) for j in range(9)), F(0))
    if not taylor > 20:
        failures.append('positive-Taylor-lower-bound')
    c = F(9, 1024)
    s0, s1 = 12, 68
    t0 = F(1, 2*c*K)
    t1 = F(1, 2*c) + t0
    a_full = 4*s0**4
    b_full = 16*s1*s0**3
    a_tail_prefactor = 16*t0*s0**3
    b_tail_prefactor = 16*(t1*s0**3 + 3*t0*s1*s0**2)
    pair_prefactor = b_tail_prefactor*a_full + b_full*a_tail_prefactor
    cg = F(1296*7*165*3, 16)
    norm = {3: 6050, 6: 1640736}
    bounds = {}
    for i, ni in norm.items():
        b = cg*ni*pair_prefactor/20**27
        g = b/4
        bounds[str(i)] = dict(B_bound=rational(b), G_bound=rational(g),
                              passed=b < F(1, 10**9))
        if not bounds[str(i)]['passed']:
            failures.append(f'omitted-spectrum-{i}')

    source = ROOT/'continuum-first-pair-enclosure-certificate.json'
    extra = ROOT/'physical-h-enclosure-certificate.json'
    source_data = json.loads(source.read_text())
    extra_data = json.loads(extra.read_text())
    covered = {(r['h'], r['n']) for r in source_data['moments']}
    added = {(r['h'], r['n']) for r in extra_data['added_moments']}
    expected_source = {(h, n) for h in (0, 1) for n in range(-192, 193)}
    expected_source |= {(h, n) for h in (2, 3) for n in range(-96, 97)}
    expected_added = {(2, n) for n in range(-192, 193) if abs(n) > 96}
    source_ok = (covered == expected_source and len(source_data['moments']) == 1156)
    added_ok = (added == expected_added and len(extra_data['added_moments']) == 192)
    if not source_ok:
        failures.append('L082-saved-moment-domain')
    if not added_ok:
        failures.append('L133-saved-added-moment-domain')
    covered |= added
    keys, m, q = g_templates()
    active = sorted({idx for rows in [m, q[3], q[6]] for row in rows for idx in row[3]})
    matrices = []
    all_used = set()
    total_entries = 0
    for idx in active:
        key = keys[idx]
        used, witnesses, missing = set(), {}, []
        left, _, right, _ = key
        entries = 0
        for n in range(0 if left[0] == 'E' else 1, K+1):
            for mm in range(0 if right[0] == 'E' else 1, K+1):
                need = required_support(key, n, mm)
                entries += 1
                for h, freq in sorted(need):
                    used.add((h, freq))
                    witnesses.setdefault((h, freq), (n, mm))
                    if (h, freq) not in covered:
                        missing.append(dict(left_index=n, right_index=mm,
                                            moment=[h, freq]))
        all_used |= used
        total_entries += entries
        by_degree = {str(h): max(abs(n) for j, n in used if j == h)
                     for h in sorted({h for h, n in used})}
        matrices.append(dict(id=idx, left=left, weight=key[1], right=right,
                             ell=key[3], entries_checked=entries,
                             max_frequency_by_degree=by_degree,
                             required_moments=[dict(h=h, n=n, witness=list(witnesses[h, n]))
                                               for h, n in sorted(used)],
                             missing=missing, passed=not missing))
        if missing:
            failures.append(f'matrix-domain-{idx}')
    # These counts are an additional guard on the full unchanged probe scope.
    counts_ok = (len(m), len(q[3]), len(q[6])) == (24, 48, 192)
    if not counts_ok:
        failures.append('complete-row-counts')
    summary = dict(matrix_count=len(matrices), entries_checked=total_entries,
                   G_rows=len(m), Q3_rows=len(q[3]), Q6_rows=len(q[6]),
                   required_moment_count=len(all_used),
                   max_frequency_by_degree={str(h): max(abs(n) for j, n in all_used if j == h)
                                            for h in sorted({h for h, n in all_used})},
                   missing_moment_count=len(all_used-covered),
                   failed_matrix_count=sum(not r['passed'] for r in matrices))
    return dict(cutoff=K, qualification='Containing symbolic supports and complete omission only; no retained inclusion or G sign.',
                tail=dict(c=rational(c), polynomial_majorant='|k| <= sum_j k_j',
                          S0=s0, S1=s1, S0_analytic_upper=rational(1+F(32, 3)),
                          S1_analytic_upper=rational(F(512, 9)+F(32, 3)),
                          t0_prefactor=rational(t0), t1_prefactor=rational(t1),
                          A_full=a_full, B_full=b_full,
                          A_tail_prefactor=rational(a_tail_prefactor),
                          B_tail_prefactor=rational(b_tail_prefactor),
                          pair_prefactor=rational(pair_prefactor), C_G=rational(cg),
                          exponent=rational(c*K*K), taylor_e3_lower=rational(taylor),
                          e81_inverse_upper=rational(F(1, 20**27)),
                          required=rational(F(1, 10**9)), probes=bounds),
                sources=[dict(path=p.name, sha256=sha(p)) for p in (source, extra)],
                source_domain_passed=source_ok, added_domain_passed=added_ok,
                certified_domain=[list(k) for k in sorted(covered)],
                G_rows=rows_record(m), Q3_rows=rows_record(q[3]), Q6_rows=rows_record(q[6]),
                matrices=matrices, summary=summary, failures=failures, passed=not failures)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit', action='store_true')
    args = parser.parse_args()
    # Compare records in the same JSON schema (tuples serialize as lists).
    data = json.loads(json.dumps(generate()))
    if args.audit:
        saved = json.loads(CERT.read_text())
        failures = list(data['failures'])
        if data != saved:
            failures.append('complete-certificate-replay')
        audit = dict(certificate_sha256=sha(CERT), summary=data['summary'],
                     failures=failures, passed=not failures)
        AUDIT.write_text(json.dumps(audit, indent=2)+'\n')
        print(f"Replay {'PASS' if audit['passed'] else 'FAIL'}; failures {len(failures)}; {AUDIT}")
        if failures:
            raise SystemExit(1)
        return
    CERT.write_text(json.dumps(data, indent=2)+'\n')
    for i, row in data['tail']['probes'].items():
        b = F(int(row['B_bound']['numerator']), int(row['B_bound']['denominator']))
        print(f'Probe {i}: complete B omission <{float(b):.12g}; G omission <{float(b/4):.12g}; required B <1e-9')
    print(f"Coverage {data['summary']}; failures {len(data['failures'])}; {CERT}")
    if data['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
