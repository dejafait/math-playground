"""Audit every saved L055 support row by direct moments and locator recurrences.

No producer or verifier imports. The existing complete scalar/r replay is
separately required; this consumes the complete saved verification certificate.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).parent
P = 97
H = tuple(x for x in range(1, P) if pow(x, 16, P) == 1)


def product_value(roots, x):
    result = 1
    for root in roots:
        result = result * (x - root) % P
    return result


def moment_vector(k, weights):
    return [sum(w * pow(x, j, P) for x, w in zip(k, weights)) % P
            for j in range(1, 9)]


def locator(roots):
    coeff = [1]
    for x in roots:
        new = [0] * (len(coeff) + 1)
        for i, c in enumerate(coeff):
            new[i] = (new[i] - x * c) % P
            new[i + 1] = (new[i + 1] + c) % P
        coeff = new
    return coeff


def recurrence(coeff, moments):
    return [sum(c * moments[i + j] for j, c in enumerate(coeff)) % P
            for i in range(4)]


def main():
    result = dict(scope='L055 saved support evidence; independent recurrence audit',
                  file_identity=[], seeds=[], failures=[])
    checks, totals = 0, Counter()
    try:
        before = json.loads((ROOT.parent.parent /
            'drafts/2026-10-10-saturated-singleton-audit-before.json').read_text())
        for relative, previous in before.items():
            actual = hashlib.sha256((ROOT.parent.parent / relative).read_bytes()).hexdigest()
            result['file_identity'].append(dict(path=relative, sha256=actual,
                                                unchanged=actual == previous['sha256']))
            assert actual == previous['sha256'], ('reproduction mismatch', relative)
        source = json.loads((ROOT / 'cross-tag-saturated-result.json').read_text())
        saved = json.loads((ROOT / 'cross-tag-saturated-verification.json').read_text())
        assert source['complete'] and source['stop_before'] is None
        assert saved['summary']['complete'] and not saved['summary']['failures']
        assert len(source['seeds']) == len(saved['seeds']) == 8
        for seed, verified in zip(source['seeds'], saved['seeds']):
            h, d, y1, y2 = (seed[x] for x in ('h', 'd', 'y1', 'y2'))
            z, w, p, q, r = (seed[x] for x in ('z', 'W', 'p', 'q', 'r'))
            expected_key = [z, w, y2, d, h, y1, p, q, r]
            assert verified['key'] == expected_key
            b = (h, d, y1, y2, 1, z)
            assert len(set(b) | set(w)) == 9
            assert p * q * (1 - p - q) * r * (1 - r) % P
            outside = [x for x in H if x not in set(b) | set(w)]
            c = [product_value(outside, x) for x in b]
            n0 = [v * a % P for v, a in zip(c, (q, 1-r, 0, 0, 1, 1))]
            n1 = [v * a % P for v, a in zip(c, (-p, -r, -1, -1, 0, 0))]
            m0, m1 = moment_vector(b, n0), moment_vector(b, n1)
            records = verified['all_support_records']
            expected_supports = list(combinations(H, 4))
            assert [tuple(row['K']) for row in records] == expected_supports
            excluded = [{h,d,y1,y2}, {h,d,1,z}, {h,*w}, {y1,y2,1,z}]
            evidence, admitted, counts = [], [], Counter()
            for row in records:
                k = row['K']
                aa, vv = row['intercept_weights'], row['slope_weights']
                assert len(aa) == len(vv) == 4
                assert all(isinstance(x, int) and 0 <= x < P for x in aa + vv)
                ma, mv = moment_vector(k, aa), moment_vector(k, vv)
                assert ma[:4] == m0[:4] and mv[:4] == m1[:4]
                assert row['residual_intercept'] == [(x-y) % P for x,y in zip(ma[4:],m0[4:])]
                assert row['residual_slope'] == [(x-y) % P for x,y in zip(mv[4:],m1[4:])]
                f = locator(k)
                rr, ss = recurrence(f, m0), recurrence(f, m1)
                out = dict(K=k, locator=f, recurrence_intercept=rr, recurrence_slope=ss)
                if not any(ss):
                    assert any(rr), ('persistent support', expected_key, k)
                    status = 'constant_inconsistent'
                else:
                    j = next(j for j, x in enumerate(ss) if x)
                    mu = -rr[j] * pow(ss[j], -1, P) % P
                    out['tested_mu'] = mu
                    if any((a + mu * v) % P for a, v in zip(rr, ss)):
                        status = 'inconsistent'
                    elif mu in (0, 96) or set(k) in excluded:
                        status = 'base_or_universal_excluded'
                    else:
                        status = 'admitted'
                        omega = [(a + mu * v) % P for a, v in zip(aa, vv)]
                        mm = [(a + mu * v) % P for a, v in zip(m0, m1)]
                        assert moment_vector(k, omega) == mm
                        assert row['tested_mu'] == mu and row['omega'] == omega
                        assert row['full_weight'] == all(omega) and all(omega)
                        assert set(k) & set(b) == {y1}
                        admitted.append(dict(K=k, mu=mu, omega=omega,
                                             moments=mm, full_weight=True))
                assert row['status'] == status, ('status mismatch', expected_key, k)
                out['status'] = status
                evidence.append(out)
                counts[status] += 1
                checks += 1
            assert admitted == verified['admitted']
            assert len(admitted) == len({a['mu'] for a in admitted}) == 3
            assert verified['distinct_nonuniversal_mu'] == 3
            assert verified['support_checks'] == 1820
            totals.update(counts)
            result['seeds'].append(dict(key=expected_key, status_counts=dict(counts),
                                        support_records=evidence, admitted=admitted))
        assert checks == 14560
        assert saved['summary']['maximum_nonuniversal_mu'] == 3
    except Exception as error:
        result['failures'].append(repr(error))
    maximum = max((len({a['mu'] for a in s['admitted']})
                   for s in result['seeds']), default=None)
    result['summary'] = dict(complete=not result['failures'], support_checks=checks,
                           required_support_checks=14560, status_counts=dict(totals),
                           maximum_nonuniversal_mu=maximum,
                           saturated_count_required=3, singleton_bound=8,
                           uniform_target_unproved=11)
    output = ROOT / 'cross-tag-saturated-audit.json'
    output.write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(f'Support checks {checks}/14560; saturated maximum {maximum}/3; '
          f'singleton bound 8; uniform target 11 remains unproved; '
          f'failures {len(result["failures"])}; certificate {output}')
    if result['failures']:
        print(result['failures'])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
