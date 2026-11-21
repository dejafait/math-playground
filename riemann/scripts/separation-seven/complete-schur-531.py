#!/usr/bin/env python3
"""One fixed separation-seven attempt: scalar certificate and finite locator.

The Decimal part certifies only the complete cross-operator bound and the
512-mode complementary diagonal floor. The NumPy part is NOT a sign
certificate: moments, special functions, eigenvalues and phase sampling
remain floating point, and the complete Schur covariance is unpaid.
"""
import json
import math
from decimal import Context, Decimal, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from pathlib import Path

PREC = 60
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
NEAR = Context(prec=PREC, rounding=ROUND_HALF_EVEN)


class I:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        assert self.lo <= self.hi

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, x):
        x = I.cast(x)
        return I(DOWN.add(self.lo, x.lo), UP.add(self.hi, x.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, x):
        return self + (-I.cast(x))

    def __rsub__(self, x):
        return I.cast(x) + (-self)

    def __mul__(self, x):
        x = I.cast(x)
        pairs = [(a, b) for a in (self.lo, self.hi) for b in (x.lo, x.hi)]
        return I(min(DOWN.multiply(a, b) for a, b in pairs),
                 max(UP.multiply(a, b) for a, b in pairs))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not self.lo <= 0 <= self.hi
        return I(DOWN.divide(Decimal(1), self.hi), UP.divide(Decimal(1), self.lo))

    def __truediv__(self, x):
        return self * I.cast(x).reciprocal()

    def __rtruediv__(self, x):
        return I.cast(x) / self

    def elementary(self, name):
        assert self.lo > 0
        fn = getattr(NEAR, name)
        return I(NEAR.next_minus(fn(self.lo)), NEAR.next_plus(fn(self.hi)))

    def ln(self):
        return self.elementary('ln')

    def sqrt(self):
        return self.elementary('sqrt')

    def json(self):
        return {'lo': str(self.lo), 'hi': str(self.hi)}


def prime_powers():
    ans = []
    for p in range(2, 82):
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            continue
        n = p
        while n < 81:
            if n > 27:
                ans.append((n, p))
            n *= p
    return sorted(ans)


def scalar_certificate():
    ell = I(3).ln() / 2
    powers = prime_powers()
    assert [n for n, _ in powers] == [29, 31, 32, 37, 41, 43, 47, 49,
                                     53, 59, 61, 64, 67, 71, 73, 79]
    data = [(n, p, I(p).ln() / I(n).sqrt(), 7 * ell - I(n).ln())
            for n, p in powers]
    events = [(I(0), 'left'), (ell, 'right')]
    for n, p, weight, delta in data:
        for endpoint, label in ((-delta, f'enter:{n}'), (ell-delta, f'exit:{n}')):
            if endpoint.lo > 0 and endpoint.hi < ell.lo:
                events.append((endpoint, label))
            else:
                assert endpoint.hi < 0 or endpoint.lo > ell.hi
    events.sort(key=lambda item: item[0].lo)
    rows = []
    for (left, ll), (right, rl) in zip(events, events[1:]):
        assert left.hi < right.lo
        sample = I(NEAR.divide(NEAR.add(left.hi, right.lo), Decimal(2)))
        active = []
        total = I(0)
        for n, p, weight, delta in data:
            point = sample + delta
            if point.lo > 0 and point.hi < ell.lo:
                active.append(n)
                total += weight
            else:
                assert point.hi < 0 or point.lo > ell.hi
        rows.append({'left': ll, 'right': rl, 'sample': sample.json(),
                     'active': active, 'weight_sum': total.json()})
    row = I(max(Decimal(r['weight_sum']['lo']) for r in rows),
            max(Decimal(r['weight_sum']['hi']) for r in rows))
    # c_j=2j+1/2, j>=1. The exact row integral is bounded by
    # sum exp(-6 ell c_j)/c_j <= exp(-15 ell)/[(5/2)(1-exp(-12 ell))].
    kappa = 1 / (I(2187) * I(3).sqrt() * I('2.5') * (1-I(1)/729))
    cross_upper = row + kappa
    # L744(8), k_n=n*pi/ell and pi>3: for all n>=512,
    # h(k_n)>=log(512/(2ell))-2ell^2/(512^2*pi^2).
    # Replacing pi^2 by 9 is a weaker certified bound.
    diagonal_lower = (512/(2*ell)).ln() - 2*ell*ell/(512*512*9)
    complement_lower = diagonal_lower - I('4.71')
    assert row.hi < Decimal('4.702')
    assert kappa.hi < Decimal('.000106')
    assert cross_upper.hi < Decimal('4.71')
    assert complement_lower.lo > Decimal('1.43')
    return {
        'certified_scope': 'scalar cross bound and full 512-mode complement floor only',
        'ell': ell.json(),
        'active_powers': [{'n': n, 'prime': p, 'weight': w.json(), 'delta': d.json()}
                          for n, p, w, d in data],
        'events': [{'label': label, 'interval': interval.json()} for interval, label in events],
        'all_row_cells': rows,
        'prime_row_max': row.json(),
        'continuous_norm_upper': kappa.json(),
        'complete_cross_norm_upper': cross_upper.json(),
        'diagonal_lower': diagonal_lower.json(),
        'complement_lower_using_cross_4_71': complement_lower.json(),
        'required_cross_bound': '4.71',
        'required_complement_bound': '1.43',
        'parameters': {'separation': 7, 'head_modes': 512, 'moment_penalty': 256},
        'full_inequality_certified': False,
        'unpaid': 'S_theta = M_theta - F_theta^* F_theta/1.43 must be PSD for every theta; F_theta includes every omitted mode and all mixed covariance.',
    }


def locator():
    import numpy as np
    ell = np.log(3.) / 2
    count, responses = 64, 65536
    n = np.arange(count)
    k = n * np.pi / ell
    norm = np.full(count, np.sqrt(2/ell))
    norm[0] = 1 / np.sqrt(ell)
    rnorm = np.sqrt(2) * norm
    parity = (-1.) ** n

    def psi(z):
        w = z + 32
        ans = np.log(w) - .5/w
        for j, b in enumerate([1/6, -1/30, 1/42, -1/30, 5/66,
                                -691/2730, 7/6, -3617/510], 1):
            ans -= b/(2*j*w**(2*j))
        for j in range(32):
            ans -= 1/(z+j)
        return ans

    h = psi(.25 + .5j*k).real - np.log(np.pi)
    response = np.zeros((count, count))
    same = parity[:, None] == parity[None, :]
    for start in range(0, responses, 1024):
        c = 2*np.arange(start, min(start+1024, responses)) + .5
        values = (rnorm[:, None]*c[None, :]
                  *np.sqrt(1-parity[:, None]*np.exp(-ell*c)[None, :])
                  /(k[:, None]**2+c[None, :]**2))
        response += (values @ values.T) * same
    cj = 2*responses + .5
    response += np.outer(rnorm, rnorm) * same / (2*cj)
    tail_error = float(np.sum(rnorm**2) * (
        1/cj**2 + 2*k[-1]**2*(1/(6*cj**3)+1/cj**4)
        + np.exp(-ell*cj)*(1/(2*cj)+1/cj**2)))
    energy = np.diag(h) + response

    prime = np.zeros_like(energy)
    nn, mm = k[:, None], k[None, :]
    for power, p in prime_powers():
        delta = 7*ell - np.log(power)
        lo, hi = max(0., -delta), min(ell, ell-delta)
        length, mid = hi-lo, (hi+lo)/2
        matrix = length/2 * (
            np.cos((nn-mm)*mid-mm*delta)*np.sinc((nn-mm)*length/(2*np.pi))
            + np.cos((nn+mm)*mid+mm*delta)*np.sinc((nn+mm)*length/(2*np.pi)))
        prime += np.log(p)/np.sqrt(power)*np.outer(norm, norm)*matrix

    continuous = np.zeros_like(energy)
    for j in range(1, 8):
        c = 2*j+.5
        iminus = norm*c*(1-parity*np.exp(-c*ell))/(c*c+k*k)
        iplus_scaled = norm*c*(parity-np.exp(-c*ell))/(c*c+k*k)
        continuous += np.exp(-6*ell*c)*np.outer(iminus, iplus_scaled)
    cont_tail = float(np.exp(-6*ell*16.5)/(16.5*(1-np.exp(-12*ell))))
    complete = prime + continuous
    moments = []
    for c in [.5, -.5]:
        moments.append(norm*c*(parity*np.exp(c*ell)-1)/(c*c+k*k))
    moments = np.array(moments)
    orth, _ = np.linalg.qr(moments.T, mode='complete')
    neutral = orth[:, 2:]
    en = neutral.T @ energy @ neutral
    tn = neutral.T @ complete @ neutral
    ev, vec = np.linalg.eigh(en)
    assert ev[0] > 0
    invroot = (vec / np.sqrt(ev)) @ vec.T
    relative = invroot @ tn @ invroot
    phases = []
    for theta in np.linspace(0, 2*np.pi, 65):
        direction = np.exp(1j*theta)
        herm = (direction*tn + direction.conjugate()*tn.T)/2
        eig = np.linalg.eigvalsh(en + herm)
        rh = (direction*relative + direction.conjugate()*relative.T)/2
        rev = np.linalg.eigvalsh(rh)
        phases.append({'theta': float(theta), 'finite_margin': float(eig[0]),
                       'relative_support': float(rev[-1])})
    return {
        'certified': False,
        'parameters': {'modes': count, 'response_prefix': responses, 'phase_samples': 65},
        'energy_matrix': energy.tolist(), 'prime_matrix': prime.tolist(),
        'continuous_matrix': continuous.tolist(), 'moment_matrix': moments.tolist(),
        'neutral_basis': neutral.tolist(), 'phases': phases,
        'energy_eigenvalues': ev.tolist(),
        'analytic_response_tail_error_bound_float': tail_error,
        'analytic_continuous_tail_bound_float': cont_tail,
        'maximum_moment_residual_float': float(np.max(np.abs(moments @ neutral))),
        'maximum_sampled_relative_support': max(p['relative_support'] for p in phases),
        'minimum_sampled_finite_margin': min(p['finite_margin'] for p in phases),
        'required_uniform_relative_bound': 1,
        'limitations': ['floating arithmetic and special function evaluation',
                       'finite phase sampling', 'numerical moment projection',
                       'finite form-domain tests are not compact smooth witnesses',
                       '512-mode head and complete Schur covariance not enclosed'],
    }


def main():
    folder = Path(__file__).parent
    scalar = scalar_certificate()
    scalar_path = folder / 'scalar-certificate-531.json'
    scalar_path.write_text(json.dumps(scalar, indent=2)+'\n')
    print('Certified scalar bound: ||T_7||<4.71; full complementary diagonal >1.43 at N=512.', flush=True)
    print(f'Actual bounds: cross upper={scalar["complete_cross_norm_upper"]["hi"]}; '
          f'complement lower={scalar["complement_lower_using_cross_4_71"]["lo"]}', flush=True)
    print(f'Scalar certificate: {scalar_path}', flush=True)
    diagnostic = locator()
    diagnostic_path = folder / 'finite-locator-531.json'
    diagnostic_path.write_text(json.dumps(diagnostic, indent=2)+'\n')
    print(f'Finite locator only: sampled relative support={diagnostic["maximum_sampled_relative_support"]:.12g}; '
          f'sampled margin={diagnostic["minimum_sampled_finite_margin"]:.12g}; required uniform ratio<=1.')
    print('Failures/unpaid: all-phase enclosures, exact finite moments, infinite mixed Schur covariance; no full sign or counterexample.')
    print(f'Full diagnostic: {diagnostic_path}')


if __name__ == '__main__':
    main()
