"""L065: exact axial energy identity and actual-stencil diagnostics.

The analytic proof, not the floating diagnostics, supplies the uniform
operator bound. No mixed cumulant or cutoff coefficient is evaluated.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np
from haar_contraction import RelativeBox, gradient, average, average_adj


def exact_checks():
    rows = []
    for n in (2, 4, 8, 24):
        weights = [F(0)] + [F(j * (n-j), n*n) for j in range(1, n)] + [F(0)]
        # Test every coefficient of a homogeneous quadratic polynomial:
        # diagonal vectors and pairwise sums determine its symmetric matrix.
        failures = []
        count = 0
        for i in range(n):
            for j in range(i, n):
                y = [F(int(r == i) + int(r == j and i != j)) for r in range(n)]
                m = [F(0)] + [weights[r] * (y[r-1]+y[r])/2 for r in range(1, n)] + [F(0)]
                lhs = sum(y[r]*(m[r+1]-m[r]) for r in range(n))
                rhs = sum((weights[r+1]-weights[r])*y[r]**2/2 for r in range(n))
                count += 1
                if lhs != rhs:
                    failures.append(dict(i=i, j=j, defect=str(lhs-rhs)))
        rows.append(dict(N=n, basis_checks=count, actual_defect='0' if not failures else 'nonzero',
                         required_defect='0', failures=failures, passed=not failures))
    return rows


def stencil_checks():
    box = RelativeBox(24)
    rng = np.random.default_rng(650024)
    rows = []
    for label in ('all_frequency', 'axial_zero', 'axial_nonzero'):
        f = rng.normal(size=box.shapes[0])
        if label == 'axial_zero':
            f[:] = f[0]
        if label == 'axial_nonzero':
            f *= np.cos(5*np.pi*(np.arange(box.n)+0.5)/box.n)[:, None, None, None]
        x = box.zeros()
        x[0] = f
        k = box.generator(x)
        curls, k_curls = box.curl(x), box.curl(k)
        direct = sum(float(np.vdot(curls[p], k_curls[p])) for p in curls)
        h = average(f, 0)
        transport = sum(box.u[mu]*average(gradient(h, mu), mu)
                        for mu in (1, 2, 3))/box.a
        first = sum(float(np.vdot(gradient(h, mu), gradient(transport, mu)))
                    for mu in (1, 2, 3))
        weight_edge = gradient(box.u[0], 0)/(2*box.a)
        second = sum(float(np.sum(weight_edge*average(gradient(f, mu), mu)**2))
                     for mu in (1, 2, 3))
        defect = abs(direct-first-second)
        tolerance = 1e-11*max(1, abs(direct), abs(first), abs(second))
        rows.append(dict(input=label, actual_defect=defect, required_defect=tolerance,
                         direct=direct, transverse_transport=first,
                         axial_weight_difference=second, passed=defect <= tolerance))
    return rows


def main():
    exact, diagnostics = exact_checks(), stencil_checks()
    failures = [row for row in exact+diagnostics if not row['passed']]
    certificate = dict(scope='L065 scalar component-1 energy decomposition only',
                       exact_axial_identity=exact, actual_stencil_diagnostics=diagnostics,
                       actual_bound='Analytic uniform R_01 bound in L065; diagnostics only check decomposition',
                       required_bound='||R_01|| <= C independent of N', failures=failures,
                       qualifications='Exact rational quadratic-basis tests plus three binary64 N=24 inputs. No certified numerical norm, mixed response, scaled limit, or logarithm.')
    path = Path(__file__).with_name('mixed-axial-residual-certificate.json')
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f'Exact quadratic checks: {sum(r["basis_checks"] for r in exact)}; actual/required defect: 0/0')
    print(f'Actual-stencil diagnostics: {len(diagnostics)}; failures: {len(failures)}')
    for row in diagnostics:
        print(f'{row["input"]}: defect {row["actual_defect"]:.6g}, required <= {row["required_defect"]:.6g}')
    print('Actual/required analytic bound: ||R_01|| <= C / O(1), proved in L065.')
    print('Certificate:', path)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
