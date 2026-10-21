"""Replay L093's one specialization; no new residual or label search."""
import hashlib
import itertools
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
P = 97


def evaluate(coeffs, x):
    return sum(c * pow(x, i, P) for i, c in enumerate(coeffs)) % P


def determinant(rows):
    total = 0
    for perm in itertools.permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3)
                         for j in range(i + 1, 3))
        total += (-1)**inversions * rows[0][perm[0]] * rows[1][perm[1]] * rows[2][perm[2]]
    return total % P


def row(x, y):
    return [y, 1, 0] if x is None else [x*y, x+y, 1]


def main():
    certificate = HERE / 'd6-residual-certificate.json'
    before = hashlib.sha256(certificate.read_bytes()).hexdigest()
    runpy.run_path(str(HERE / 'd6_residual.py'), run_name='__main__')
    after = hashlib.sha256(certificate.read_bytes()).hexdigest()
    saved = json.loads(certificate.read_text())
    # These are the complete displayed values in L093, independent of
    # the producer's polynomial construction and remainder implementation.
    polys = dict(Q=[23, 66, 49], M=[48, 73], N=[71, 94], O=[22, 47],
                 Z=[76, 39, 61], W=[95, 76, 85], U=[93, 1],
                 V=[93, 62, 86], E=[92, 74, 18, 33, 35])
    quotient, remainder = [37, 41, 70], [17, 84]
    product = [0]*5
    for i, a in enumerate(quotient):
        for j, b in enumerate(polys['Q']):
            product[i+j] += a*b
    for i, a in enumerate(remainder):
        product[i] += a
    product = [a % P for a in product]
    failures = []

    def check(name, condition):
        if not condition:
            failures.append(name)

    check('unchanged complete producer certificate', before == after)
    check('every displayed coefficient', saved['polynomials'] == polys)
    check('full quotient identity', product == polys['E'])
    check('quotient and both remainder representations',
          saved['quotient'] == quotient and saved['remainder'] == remainder
          and saved['rho'] == remainder)
    check('normalization', saved['normalization'] ==
          dict(ell=75, t=17, u=34, alpha=92, beta=20, gamma=72))
    check('seeds', saved['seeds'] == dict(c=2, d=3, e=4, g=6, j=10, k=24))
    denominators = dict(one_minus_c=96, e_minus_d=1, j_minus_c=8,
                        j_minus_d=7, k_minus_g=18, ell=75, q2=49)
    check('specialization denominator domain', all(denominators.values()))
    delta = (49*17**2 - 66*17*84 + 23*84**2) % P
    check('nonzero Delta', delta == saved['delta'] == 42)
    check('complete scalar index set', [r['x'] for r in saved['rows']] == list(range(P)))
    rows = []
    for x in range(P):
        values = {name: evaluate(poly, x) for name, poly in polys.items()}
        scaled = determinant([[values['Z'], values['Z']+values['W'], values['W']],
                              row(10, (17*x+34) % P),
                              [24*values['M'], values['M']+24*75, 75]])
        expected = dict(x=x, Q=values['Q'], E=values['E'], cleared_D6=scaled,
                        N_den=values['O'], Z_den=values['W'])
        check(f'complete stored scalar row {x}', saved['rows'][x] == expected)
        check(f'cleared determinant {x}', scaled == values['E'])
        item = dict(x=x, cleared_D6=scaled, E=values['E'], finite_checks=None)
        if values['O'] and values['W']:
            m = values['M'] * pow(75, -1, P) % P
            n = values['N'] * pow(values['O'], -1, P) % P
            z = values['Z'] * pow(values['W'], -1, P) % P
            y = (17*x+34) % P
            gates = dict(D8=determinant([row(0, x), row(None, 24), row(m, 2)]),
                         D3=determinant([row(3, 4), row(0, m), row(6, n)]),
                         D2=determinant([row(2, 3), row(x, 10), row(z, n)]),
                         D6=determinant([row(1, z), row(10, y), row(m, 24)]))
            check(f'reconstruction gates {x}', all(gates[g] == 0 for g in ['D8', 'D3', 'D2']))
            check(f'unscaled D6 {x}', gates['D6'] * 75 * values['W'] % P == scaled)
            item['finite_checks'] = dict(m=m, n=n, z=z, Y=y, determinants=gates)
        rows.append(item)
    check('producer failures and scope', saved['failures'] == []
          and saved['H_assignments_tested'] == saved['rank_tests'] == 0)
    check('actual and required remainder bounds', saved['bound'] ==
          dict(actual_remainder_degree=1, required_maximum=1))
    report = dict(scope='L093 displayed one-seed specialization only; not a general proof',
                  producer_sha256_before=before, producer_sha256_after=after,
                  displayed_polynomials=polys, quotient=quotient, remainder=remainder,
                  quotient_identity_coefficients=product, seed_denominators=denominators,
                  delta=delta, actual_remainder_degree=1, required_maximum=1,
                  scalar_rows_checked=len(rows), rows=rows, failures=failures,
                  H_assignments_tested=0, rank_tests=0)
    path = HERE / 'd6-critical-audit.json'
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['actual_remainder_degree', 'required_maximum',
          'scalar_rows_checked', 'delta', 'failures', 'H_assignments_tested', 'rank_tests']}))
    print(f'Full audit certificate: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
