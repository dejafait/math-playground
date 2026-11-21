"""One degree-three Favard test of actual L795; no fresh moment evaluation.

Finite Laurent-polynomial identities and exact Fraction interval arithmetic.
Original inputs are read-only. The audited L778 analytic/software contracts
are inherited through L791/step478, not established by this program.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
OUT = BASE / 'favard-prefix-certificate-504.json'


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        v = iv(other)
        return I(self.lo + v.lo, self.hi + v.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-iv(other))

    def __rsub__(self, other):
        return iv(other) + (-self)

    def __mul__(self, other):
        v = iv(other)
        p = [a*b for a in (self.lo, self.hi) for b in (v.lo, v.hi)]
        return I(min(p), max(p))

    __rmul__ = __mul__

    def __truediv__(self, other):
        v = iv(other)
        assert v.lo > 0 or v.hi < 0, 'denominator interval contains zero'
        return self * I(1/v.hi, 1/v.lo)

    def __rtruediv__(self, other):
        return iv(other) / self

    def pair(self):
        return [str(self.lo), str(self.hi)]


def iv(v):
    return v if isinstance(v, I) else I(v)


class S:
    """Laurent polynomials over Q in (a,b,c,x); inverses only of monomials."""
    def __init__(self, terms):
        self.terms = {k: F(v) for k, v in terms.items() if v}

    def __add__(self, other):
        v, terms = sy(other), dict(self.terms)
        for k, value in v.terms.items():
            terms[k] = terms.get(k, F(0)) + value
        return S(terms)

    __radd__ = __add__

    def __neg__(self):
        return S({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-sy(other))

    def __mul__(self, other):
        v, terms = sy(other), {}
        for k, value in self.terms.items():
            for l, w in v.terms.items():
                m = tuple(i+j for i, j in zip(k, l))
                terms[m] = terms.get(m, F(0)) + value*w
        return S(terms)

    __rmul__ = __mul__

    def __truediv__(self, other):
        v = sy(other)
        assert len(v.terms) == 1
        (k, value), = v.terms.items()
        return self * S({tuple(-i for i in k): 1/value})

    def __rtruediv__(self, other):
        return sy(other) / self


def sy(v):
    return v if isinstance(v, S) else S({(0, 0, 0, 0): F(v)})


def symbolic_check():
    a, b, c, x = [S({tuple(int(i == j) for i in range(4)): 1})
                  for j in range(4)]
    q0 = sy(1)
    q1 = x - 1/a
    q2 = x*x - 2*a*x/b + 1/b
    q3 = x*x*x - 3*b*x*x/c + 3*a*x/c - 1/c
    alpha0, alpha1, alpha2 = 1/a, 2*a/b-1/a, 3*b/c-2*a/b
    beta1, beta2 = 1/b-1/(a*a), 1/b+3*a/c-4*a*a/(b*b)
    delta = 1/c+1/(a*b)-2*a/(b*b)
    residuals = [x*q0-q1-alpha0*q0,
                 x*q1-q2-alpha1*q1-beta1*q0,
                 x*q2-q3-alpha2*q2-beta2*q1-delta*q0]
    assert all(not r.terms for r in residuals), 'symbolic recurrence mismatch'
    return {'variables': ['a', 'b', 'c', 'x'],
            'recurrence_residuals': [list(r.terms.items()) for r in residuals],
            'alpha': ['1/a', '2*a/b-1/a', '3*b/c-2*a/b'],
            'beta': ['1/b-1/a^2', '1/b+3*a/c-4*a^2/b^2'],
            'forbidden_Q0_coefficient': '1/c+1/(a*b)-2*a/b^2'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def coarse(v, scale=10**6):
    # Display bounds are outward rational enclosures too, never float summaries.
    return [str(F((v.lo*scale).__floor__(), scale)),
            str(F((v.hi*scale).__ceil__(), scale))]


def main():
    source = BASE / 'fixed-model-certificate-476.json'
    audit_path = BASE / 'audit-478/audit-report.json'
    data, audit = json.loads(source.read_text()), json.loads(audit_path.read_text())
    assert digest(source) == audit['original_hashes'][str(source.relative_to(ROOT))]
    assert audit['status'] == 'PASS' and audit['failures'] == []
    required = ([f'actual_a {j}' for j in range(4)]
                + [f'gamma {j}' for j in range(4)]
                + [f'gamma positivity {j}' for j in range(4)]
                + ['inherited source hash matches L791',
                   'inherited source hash matches L778 audit',
                   'inherited evaluator equals complete audited replay',
                   'prior L778 audit passed', 'complex Cauchy radius',
                   'inherited error positive and below stated bound',
                   'error interval retained unchanged'])
    selected = [check for check in audit['checks'] if check['name'] in required]
    assert len(selected) == len(required) and all(v['passed'] for v in selected)
    for name, expected in audit['original_hashes'].items():
        assert digest(ROOT / name) == expected, f'changed inherited file: {name}'
    gamma = [I(*v) for v in data['gamma'][:4]]
    assert all(v.lo > 0 for v in gamma)
    a, b, c = [v/gamma[0] for v in gamma[1:]]
    alpha = [1/a, 2*a/b-1/a, 3*b/c-2*a/b]
    beta = [1/b-1/(a*a), 1/b+3*a/c-4*a*a/(b*b)]
    delta = 1/c+1/(a*b)-2*a/(b*b)
    denominators = {'gamma0': gamma[0], 'a': a, 'b': b, 'c': c,
                    'a_squared': a*a, 'b_squared': b*b, 'a_times_b': a*b}
    assert all(v.lo > 0 for v in denominators.values())
    forbidden_nonzero = delta.hi < 0 or delta.lo > 0
    beta_nonpositive = [v.hi <= 0 for v in beta]
    report = {
        'scope': 'Actual L795 P0..P3 only; common nondegenerate positive-measure orthogonality',
        'method': 'Exact Fraction intervals; no rounding in arithmetic; Cartesian enclosure',
        'inherited_qualifications': 'L791 step478 imports audited L778 analytic evaluator and software contracts; no fresh backend verification',
        'provenance': {str(p.relative_to(ROOT)): digest(p)
                       for p in (source, audit_path, Path(__file__).resolve())},
        'inherited_original_hashes': audit['original_hashes'],
        'selected_audit_checks': selected,
        'input_gamma_decimal': data['gamma'][:4],
        'input_gamma_rational': [v.pair() for v in gamma],
        'normalization': 'R_j=gamma(j)/gamma(0)=j!*m_j/((2*j)!*m_0); P_n=sum (-1)^j binom(n,j)R_j x^j',
        'symbolic': symbolic_check(),
        'R1_R2_R3': [v.pair() for v in (a, b, c)],
        'denominators': {k: v.pair() for k, v in denominators.items()},
        'monic_leading_divisors_P0_to_P3': [I(1).pair(), (-a).pair(), b.pair(), (-c).pair()],
        'alpha': [v.pair() for v in alpha],
        'beta': [v.pair() for v in beta],
        'forbidden_Q0_coefficient': delta.pair(),
        'outward_display': {'alpha': [coarse(v) for v in alpha],
                            'beta': [coarse(v) for v in beta], 'delta': coarse(delta)},
        'requirements': {'forbidden_Q0_coefficient': '0', 'beta1': '>0', 'beta2': '>0'},
        'tests': {'symbolic_identities': True, 'positive_denominators': True,
                  'beta_proved_positive': [v.lo > 0 for v in beta],
                  'beta_proved_nonpositive': beta_nonpositive,
                  'forbidden_coefficient_excludes_zero': forbidden_nonzero},
        'criterion_failures': (['nonzero forbidden Q0 coefficient'] if forbidden_nonzero else [])
                              + [f'beta{j+1} nonpositive' for j, v in enumerate(beta_nonpositive) if v],
        'verification_failures': [],
        'outcome': 'ORTHOGONALITY_OBSTRUCTION' if forbidden_nonzero or any(beta_nonpositive) else 'INCONCLUSIVE',
    }
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('outcome:', report['outcome'])
    print('actual outward rational bounds:', report['outward_display'])
    print('required:', report['requirements'])
    print('criterion failures:', report['criterion_failures'])
    print('verification failures:', report['verification_failures'])
    print('complete certificate:', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
