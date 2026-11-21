#!/usr/bin/env python3
"""Exact Laurent-polynomial reduction; no enclosure or feasibility oracle.

Run from riemann. Denominators in the symbolic check are monomials in
A,C,D,E, all positive by the imported hypotheses. Every residual and
branch condition is retained on disk. Parameter examples test signs
only; neither example is asserted to be an actual-Xi zero sequence.
"""
from fractions import Fraction as F
from pathlib import Path
import json

NAMES = ('A', 'B', 'C', 'D', 'E', 'x', 'u')
ZERO = (0,) * len(NAMES)


class P:
    def __init__(self, value=0):
        self.t = ({e: F(c) for e, c in value.items() if c}
                  if isinstance(value, dict) else ({ZERO: F(value)} if value else {}))

    def __add__(self, other):
        other = other if isinstance(other, P) else P(other)
        terms = self.t.copy()
        for e, c in other.t.items():
            terms[e] = terms.get(e, F(0)) + c
        return P(terms)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.t.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, P) else -P(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, P) else P(other)
        terms = {}
        for e, c in self.t.items():
            for d, v in other.t.items():
                key = tuple(a + b for a, b in zip(e, d))
                terms[key] = terms.get(key, F(0)) + c*v
        return P(terms)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, P) else P(other)
        assert len(other.t) == 1, 'Only nonzero monomial division is implemented'
        (e, c), = other.t.items()
        return self * P({tuple(-v for v in e): 1/c})

    def __pow__(self, n):
        assert n >= 0
        ans = P(1)
        for _ in range(n):
            ans = ans*self
        return ans

    def at(self, values):
        return sum((c * product(F(values[n])**k for n, k in zip(NAMES, e))
                    for e, c in self.t.items()), F(0))

    def record(self):
        return {'terms': [{'exponents': list(e), 'coefficient': str(c)}
                          for e, c in sorted(self.t.items())],
                'zero': not self.t}


def product(items):
    ans = F(1)
    for item in items:
        ans *= item
    return ans


def var(i):
    e = list(ZERO)
    e[i] = 1
    return P({tuple(e): F(1)})


def entries(b):
    # C030y's nine general identities, in symmetric c_mn normalization.
    ans = {f'1,{n}': b[n] for n in range(1, 6)}
    ans.update({'2,2': b[3]+b[1]**2/2,
                '2,3': b[4]+b[1]*b[2],
                '2,4': b[5]+b[1]*b[3]+b[2]**2/2,
                '3,3': b[5]+b[1]*b[3]+b[2]**2+b[1]**3/3})
    return ans


def main():
    A, B, C, D, E, x, u = (var(i) for i in range(7))
    tau = (1-x)/A
    k = A/(2*C)
    v = u**2-k*(1+x)
    j = v-x*B/D
    w = u*j
    h = u*w-x*v*C/E+tau*u**2*B**2/(2*E)
    ell = -E*k*(1+x)+E*x*B/D+(1-x)*B**2/(2*A)
    need = A*(x**2+x+1)/3-E*k**2*(1+x)**2
    condition = u**2*ell-need
    b = {1: x, 2: -tau*u*B, 3: -tau*v*C, 4: -tau*w*D, 5: -tau*h*E}
    S = {2: A, 3: B, 4: C, 5: D, 6: E}
    weights = {1: P(1), 2: u, 3: v, 4: w, 5: h}
    coeff = entries(b)
    prescribed = {}
    residual = {}
    verify = {}
    for key, value in coeff.items():
        m, n = map(int, key.split(','))
        prescribed[key] = F(1, m) if m == n else F(0)
        prescribed[key] = prescribed[key]-tau*weights[m]*weights[n]*S[m+n]
        residual[key] = value-prescribed[key]
        verify[key] = residual[key]-(tau*condition if key == '3,3' else 0)

    # Exact sign-only compatible example at x=-1, p=u^2=1.
    # A=B=C=E=1, D=3/2, tau=2, weights=(1,1,1,5/3,11/3).
    ex = dict(zip(NAMES, (1, 1, 1, F(3, 2), 1, -1, 1)))
    sample_values = {name: str(poly.at(ex)) for name, poly in
                     {'tau': tau, 'd_2': u, 'd_3': v, 'd_4': w, 'd_5': h,
                      'L': ell, 'N': need, 'u^2*L-N': condition}.items()}
    sample_residuals = {key: str(poly.at(ex)) for key, poly in residual.items()}
    assert all(F(sample_values[name]) > 0 for name in ('tau', 'd_2', 'd_3', 'd_4', 'd_5'))
    assert all(F(value) == 0 for value in sample_residuals.values())

    # Exact all-positive incompatible example A=B=C=D=E=1.
    # Substitution in the symbolic ring, retaining x,u.
    def set_s_to_one(poly):
        out = P()
        for e, c in poly.t.items():
            out += P({ZERO[:5]+e[5:]: c})
        return out
    verify['ones_L'] = set_s_to_one(ell)
    verify['ones_N'] = set_s_to_one(need)-(x-1)**2/12
    failures = [key for key, poly in verify.items() if poly.t]
    certificate = {
        'variables': list(NAMES),
        'hypotheses': 'A=S_2,B=S_3,C=S_4,D=S_5,E=S_6>0; x<1,u>0; actual Xi undecided',
        'source': 'C030y general identities; Teo2003 hep-th/0305005v2 Sections2.1-2.2 pp2-6',
        'definitions': {key: poly.record() for key, poly in
                        {'tau': tau, 'v': v, 'j': j, 'w': w, 'h': h,
                         'L': ell, 'N': need, 'condition': condition}.items()},
        'all_nine_coefficients': {key: poly.record() for key, poly in coeff.items()},
        'all_nine_prescribed': {key: poly.record() for key, poly in prescribed.items()},
        'all_nine_residuals': {key: poly.record() for key, poly in residual.items()},
        'verification_residuals': {key: poly.record() for key, poly in verify.items()},
        'branches': {
            'common': 'x<1,p=u^2>0,V=p-A(1+x)/(2C)>0,J=V-xB/D>0,H=pJ-xVC/E+(1-x)pB^2/(2AE)>0',
            'L_nonzero': 'p=N/L; retain only p>0,V>0,J>0,H>0',
            'L_zero_N_nonzero': 'impossible',
            'L_zero_N_zero': 'p free subject to all common inequalities; never divide by L',
            'x_zero_or_minus_one': 'retained without division by x or 1+x',
            'x_one': 'excluded tau=0, not used as a witness',
            'zero_weights': 'excluded by strict common inequalities',
            'zero_jet_coefficients': 'no division by a_j or b_j; b_0 arbitrary real',
        },
        'sign_only_compatible_example': {'parameters': {key: str(value) for key, value in ex.items()},
                                         'values': sample_values, 'all_nine_residuals': sample_residuals,
                                         'scope': 'not actual Xi; not claimed to satisfy zero-location premises'},
        'sign_only_incompatible_example': 'A=B=C=D=E=1 gives L=0,N=(x-1)^2/12>0 for every x<1',
        'actual_required': 'an x<1 and p>0 satisfying pL=N and V,J,H>0, or an all-x contradiction',
        'actual_available': 'L025 reality/convergence and L027 strict finite signs; no actual L,N feasibility certified',
        'actual_result': 'UNDECIDED; signs alone do not decide this reduced test',
        'failures': failures,
    }
    dest = Path(__file__).with_name('positive-diagonal-degree-six-certificate-1304.json')
    dest.write_text(json.dumps(certificate, indent=2)+'\n')
    print('EXACT CHECK:', len(verify), 'verification residuals;', len(failures), 'failures')
    print('ACTUAL XI: UNDECIDED. REQUIRED: x<1,p>0,pL=N,V>0,J>0,H>0.')
    print('AVAILABLE: S_2,...,S_6>0. Exact sign-only examples yield both outcomes; neither is actual Xi.')
    print('FAILURES:', failures, 'CERTIFICATE:', dest)
    assert not failures


if __name__ == '__main__':
    main()
