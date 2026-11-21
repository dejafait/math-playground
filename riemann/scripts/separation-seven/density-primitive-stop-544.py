#!/usr/bin/env python3
"""Certify the cost obstruction for one signed-density Young comparison.

This does not test the sign of the actual three-cell form. All interval
operations use the previously assessed Decimal contract of C744v.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Decimal
from pathlib import Path

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('interval544', BASE/'complete-schur-531.py')
interval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(interval)
I = interval.I


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prime_powers():
    # Independent prime-first enumeration, with exact integer cutoffs.
    powers = []
    for p in range(2, 4000):
        if any(p % d == 0 for d in range(2, math.isqrt(p)+1)):
            continue
        n = p
        while n < 4000:
            if 3**13 < n*n < 3**15:
                powers.append((n, p))
            n *= p
    assert 4000**2 > 3**15
    assert len(set(n for n, _ in powers)) == len(powers) == 334
    return sorted(powers, reverse=True)


def main():
    ell = I(3).ln()/2
    root4 = I(3).sqrt().sqrt()
    rho_min = 27*root4                    # 3^(13/4)
    rho_left = 27*root4*root4*root4        # 3^(15/4)
    cumulative = I(0)
    atoms, gaps = [], []
    extrema = [I(0)]
    last = -ell
    for n, p in prime_powers():
        delta = I(0) if n == 2187 else 14*ell-I(n).ln()
        assert last.hi < delta.lo and delta.hi < ell.lo
        length = delta-last
        assert length.lo > 0
        gaps.append(dict(left=last.json(), right=delta.json(), length=length.json()))
        weight = I(p).ln()/I(n).sqrt()
        continuous_mass = 2*(rho_left-I(n).sqrt())
        before = cumulative-continuous_mass
        after = before+weight
        atoms.append(dict(n=n, prime=p, delta=delta.json(), weight=weight.json(),
                          primitive_before=before.json(), primitive_after=after.json()))
        extrema.extend([before, after])
        cumulative += weight
        last = delta
    length = ell-last
    assert length.lo > 0
    gaps.append(dict(left=last.json(), right=ell.json(), length=length.json()))
    right_value = cumulative-2*(rho_left-rho_min)
    extrema.append(right_value)
    assert len(gaps) == 335

    # Between atoms F'=-rho. Paired points in each gap yield
    # integral_gap |F-c| >= rho_min*length^2/4 for EVERY constant c.
    square_sum = I(0)
    for gap in gaps:
        length = I(gap['length']['lo'], gap['length']['hi'])
        square_sum += length*length
    b_gap_bound = rho_min*square_sum/4
    b_simple_bound = rho_min*ell*ell/335
    assert b_gap_bound.lo > b_simple_bound.hi
    fmin = I(min(v.lo for v in extrema), min(v.hi for v in extrema))
    fmax = I(max(v.lo for v in extrema), max(v.hi for v in extrema))
    # A valid upper bound from choosing the midrange constant. Not claimed optimal.
    b_midrange_upper = ell*(fmax-fmin)

    # pi>3 suffices. C744z's full raw prime row bound is <30.
    derivative_cost_lower = b_simple_bound*(3*512/ell)
    required_b_upper = 30*ell/(3*512)
    assert derivative_cost_lower.lo > 30
    assert b_simple_bound.lo > required_b_upper.hi
    old_path = BASE/'shared-middle-scalar-certificate-543.json'
    old = json.loads(old_path.read_text())
    assert {(x['n'], x['prime']) for x in old['powers']} == set(prime_powers())
    assert Decimal(old['summary']['prime_row_max']['hi']) < 30
    assert Decimal(old['summary']['complete_remote_norm_upper']['hi']) < 30
    kappa = 1/(I(3**16)*root4*I('2.5')*(1-I(1)/3**13))

    certificate = dict(
        scope='Obstruction to constant-centered first-derivative Young payment only',
        inputs=[dict(path='complete-schur-531.py', sha256=sha(BASE/'complete-schur-531.py')),
                dict(path=old_path.name, sha256=sha(old_path))],
        arithmetic='60-digit directed Decimal; nearest ln/sqrt widened by one neighboring value',
        parameters=dict(separation=14, cosine_cutoff=512, density_scale=1),
        ell=ell.json(), rho_min=rho_min.json(), rho_left=rho_left.json(),
        atoms=atoms, gaps=gaps, right_primitive=right_value.json(),
        summary=dict(atom_count=len(atoms), primitive_gap_count=len(gaps),
            all_integer_and_interval_checks_passed=True,
            primitive_min=fmin.json(), primitive_max=fmax.json(),
            optimal_primitive_L1_lower_bound=b_simple_bound.json(),
            stronger_gap_L1_lower_bound=b_gap_bound.json(),
            midrange_primitive_L1_upper_bound=b_midrange_upper.json(),
            necessary_L1_threshold_upper_bound=required_b_upper.json(),
            derivative_cost_lower_on_Q512=derivative_cost_lower.json(),
            raw_complete_row_bound_upper='30',
            continuous_norm_upper=kappa.json(),
            threshold='Derivative cost must be below the raw prime row bound (<30) to improve it.',
            comparison_improvement=False, original_three_cell_sign='UNRESOLVED'),
        failures=[], limitations=[
            'The constant-centered full-line first-derivative Young comparison alone is stopped.',
            'Neither a lower bound on the actual operator nor a negative smooth triple is proved.',
            'Signed matrix covariance, frequency-localized comparisons and induced cancellation are untested.',
            'The full neutral inverse and both endpoint defects remain unpaid.'])
    out = BASE/'density-primitive-stop-544.json'
    out.write_text(json.dumps(certificate, indent=2)+'\n')
    print('All integer/interval checks passed; failures: 0.')
    print('Primitive L1 lower:', b_simple_bound.json())
    print('Necessary coefficient upper:', required_b_upper.json())
    print('Derivative cost lower on Q512:', derivative_cost_lower.json(), '; required <30.')
    print('Original three-cell sign: UNRESOLVED; certificate:', out.relative_to(BASE.parent.parent))


if __name__ == '__main__':
    main()
