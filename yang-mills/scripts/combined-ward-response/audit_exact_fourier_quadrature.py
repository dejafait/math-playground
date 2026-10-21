"""Audit every saved cell, exact coefficient and error bound; no sampling."""
import json
from fractions import Fraction as F
from pathlib import Path


def value(z):
    return F(int(z['numerator']), int(z['denominator']))


def main():
    source = Path(__file__).with_name('exact-fourier-quadrature-certificate.json')
    data = json.loads(source.read_text())
    coefficients = [value(z) for z in data['rho_coefficients']]
    assert len(coefficients) == 201
    assert all(q.denominator & (q.denominator-1) == 0 for q in coefficients)
    assert data['rho_polynomial_degree']+data['phase_polynomial_degree']+1 == 287
    assert data['core_phase_degree']+1 == 287
    groups = {0: [], 1: [], 2: []}
    bounds = []
    for row in data['cells']:
        c, l = F(row['center']), F(row['halfwidth'])
        assert l > 0
        bound = value(row['bound'])
        assert 0 <= bound < F(348, 10**16)
        bounds.append(bound)
        if row['case'] == 'interior':
            r = F(row['radius'])
            u, v = 9-c*c, c*c-F(25, 4)
            assert r == min(c-F(5, 2), 3-c)/16
            assert 6*r+r*r <= min(u, v)/8
            assert 0 < l/r <= F(1, 4)
            remainder = value(row['analytic_remainder'])
            assert remainder >= 2*(l/r)**25/(1-l/r)
            assert bound == (value(row['taylor_residual'])+
                             value(row['polynomial_tail'])+remainder)
            groups[1].append((c-l, c+l))
        else:
            assert row['case'] == 'endpoint_collar'
            groups[0 if row['baseline'] == 1 else 2].append((c-l, c+l))
    endpoints = [(F(5, 2), F(5, 2)+F(1, 256)),
                 (F(5, 2)+F(1, 256), F(3)-F(1, 256)),
                 (F(3)-F(1, 256), F(3))]
    for group, (left, right) in zip(groups.values(), endpoints):
        intervals = sorted(group)
        assert intervals[0][0] == left and intervals[-1][1] == right
        assert all(a[1] == b[0] for a, b in zip(intervals, intervals[1:]))
    maximum = max(bounds)
    assert maximum == value(data['rho_residual_upper'])
    assert not data['rho_failures'] and data['cell_count'] == len(bounds) == 565
    delta = F(2*3**42, 3*4**86)
    core = F(2*3**207, 3*4**286)
    assert delta == value(data['phase_residual_upper'])
    assert core == value(data['core_residual_upper'])
    actual = [2*maximum+2*(1+maximum)*delta+10*core,
              6*maximum+6*(1+maximum)*delta+25*core]
    assert actual == [value(z) for z in data['quadrature_error_upper']]
    simple = [F(7, 10**14), F(21, 10**14)]
    required = [F(6, 10**12), F(9, 10**12)]
    assert all(a < b < c for a, b, c in zip(actual, simple, required))
    assert data['exact_quadrature_checks_passed']
    path = source.with_name('exact-fourier-quadrature-audit.json')
    result = dict(source=source.name, complete_cell_count=len(bounds),
                  group_cell_counts=[len(z) for z in groups.values()],
                  exact_coverage_and_all_disk_conditions=True,
                  all_recorded_bounds_checked=True, polynomial_degrees_checked=True,
                  simple_quadrature_bounds=[str(z) for z in simple],
                  required_bounds=[str(z) for z in required], failures=[],
                  qualification='Checks every certificate row and exact coverage; does not independently recompute its Taylor jets or validate binary64 transforms.')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(result, path=str(path))))


if __name__ == '__main__':
    main()
