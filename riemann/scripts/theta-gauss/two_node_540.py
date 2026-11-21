"""One actual-moment Gaussian compression test; no fresh theta evaluation.

All arithmetic after the inherited decimal input is exact Fraction arithmetic.
Inherited L778/L791 analytic/software contracts remain premises.
"""
import hashlib
import json
from fractions import Fraction as F
from math import factorial, isqrt, comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('two-node-certificate-540.json')


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, v):
        v = iv(v)
        return I(self.lo+v.lo, self.hi+v.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, v):
        return self + (-iv(v))

    def __rsub__(self, v):
        return iv(v) - self

    def __mul__(self, v):
        v = iv(v)
        ends = [a*b for a in (self.lo, self.hi) for b in (v.lo, v.hi)]
        return I(min(ends), max(ends))

    __rmul__ = __mul__

    def __truediv__(self, v):
        v = iv(v)
        assert v.lo > 0 or v.hi < 0, 'zero in denominator'
        return self * I(1/v.hi, 1/v.lo)

    def pair(self):
        return [str(self.lo), str(self.hi)]


def iv(v):
    return v if isinstance(v, I) else I(v)


def power(v, n):
    r = I(1)
    for _ in range(n):
        r = r*v
    return r


def sqrt_box(v):
    assert v.lo > 0
    scale = 10**40
    a = isqrt((v.lo*scale*scale).__floor__())
    b = isqrt((v.hi*scale*scale).__floor__()) + 1
    ans = I(F(a, scale), F(b, scale))
    assert ans.lo**2 <= v.lo and ans.hi**2 >= v.hi
    return ans


def coarse(v, scale=10**6):
    return [str(F((v.lo*scale).__floor__(), scale)),
            str(F((v.hi*scale).__ceil__(), scale))]


class P:
    """Exact polynomials in t1,t2,t3,v1,v2, only for finite identities."""
    def __init__(self, terms):
        self.terms = {k: F(v) for k, v in terms.items() if v}

    def __add__(self, v):
        v = poly(v)
        terms = dict(self.terms)
        for k, a in v.terms.items():
            terms[k] = terms.get(k, F(0)) + a
        return P(terms)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -a for k, a in self.terms.items()})

    def __sub__(self, v):
        return self + (-poly(v))

    def __mul__(self, v):
        v, terms = poly(v), {}
        for k, a in self.terms.items():
            for l, b in v.terms.items():
                m = tuple(i+j for i, j in zip(k, l))
                terms[m] = terms.get(m, F(0)) + a*b
        return P(terms)

    __rmul__ = __mul__


def poly(v):
    return v if isinstance(v, P) else P({(0,)*5: F(v)})


def symbolic():
    t1, t2, t3, v1, v2 = [P({tuple(int(i == j) for i in range(5)): 1})
                           for j in range(5)]
    d, n = t2-t1*t1, t3-t1*t2
    bnum = n*t1-d*t2
    residuals = {
        'weight_sum_cleared': (v2-t1)+(t1-v1)-(v2-v1),
        'moment1_cleared': (v2-t1)*v1+(t1-v1)*v2-t1*(v2-v1),
        'orthogonality0_cleared': d*t2-n*t1+bnum,
        'orthogonality1_cleared': d*t3-n*t2+bnum*t1,
        'moment2_recurrence_cleared': n*t1-bnum-d*t2,
        'moment3_recurrence_cleared': n*t2-bnum*t1-d*t3,
    }
    assert all(not p.terms for p in residuals.values())
    coefficient_residuals = [(-1)**j*F(comb(3, j)*factorial(j), factorial(2*j))
                             * F(factorial(2*j), factorial(j))
                             - (-1)**j*comb(3, j) for j in range(4)]
    assert all(v == 0 for v in coefficient_residuals)
    return {'variables': ['t1', 't2', 't3', 'v1', 'v2'],
            'residuals': {name: [] for name in residuals},
            'cubic_coefficient_residuals_in_Rj': [str(v) for v in coefficient_residuals],
            'formulas': {'D': 't2-t1^2', 'N': 't3-t1*t2',
                         'A': 'N/D', 'B': '(N*t1-D*t2)/D=A*t1-t2',
                         'moment_recurrence': 's_(j+2)=A*s_(j+1)-B*s_j',
                         'reference': '1-3*v*x/2+v^2*x^2/4-v^3*x^3/120'}}


def h(y):
    return y*y*y-30*y*y+180*y-120


def root_bracket(lo, hi):
    lo, hi = F(lo), F(hi)
    assert h(lo)*h(hi) < 0
    for _ in range(50):
        mid = (lo+hi)/2
        if h(mid) == 0:
            return I(mid)
        if h(lo)*h(mid) < 0:
            hi = mid
        else:
            lo = mid
    assert h(lo)*h(hi) < 0
    return I(lo, hi)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source = ROOT / 'scripts/central-jacobi/fixed-model-certificate-476.json'
    audit_path = ROOT / 'scripts/central-jacobi/audit-478/audit-report.json'
    data, audit = json.loads(source.read_text()), json.loads(audit_path.read_text())
    assert digest(source) == '2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e'
    assert audit['status'] == 'PASS' and audit['failures'] == []
    for name, expected in audit['original_hashes'].items():
        assert digest(ROOT/name) == expected, f'changed inherited input: {name}'
    required = ([f'actual_a {j}' for j in range(4)]
                + [f'gamma {j}' for j in range(4)]
                + [f'gamma positivity {j}' for j in range(4)]
                + ['inherited source hash matches L791',
                   'inherited source hash matches L778 audit',
                   'inherited evaluator equals complete audited replay',
                   'prior L778 audit passed', 'complex Cauchy radius',
                   'inherited error positive and below stated bound',
                   'error interval retained unchanged'])
    selected = [v for v in audit['checks'] if v['name'] in required]
    assert len(selected) == len(required) and all(v['passed'] for v in selected)
    gamma = [I(*v) for v in data['gamma'][:4]]
    assert all(v.lo > 0 for v in gamma)
    t = [I(1)] + [gamma[j]/gamma[0]*F(factorial(2*j), factorial(j)) for j in range(1, 4)]
    d = t[2]-t[1]*t[1]
    assert d.lo > 0
    a = (t[3]-t[1]*t[2])/d
    b = a*t[1]-t[2]
    disc = a*a-4*b
    sqrt_disc = sqrt_box(disc)
    nodes = [(a-sqrt_disc)/2, (a+sqrt_disc)/2]
    separation = nodes[1]-nodes[0]
    weights = [(nodes[1]-t[1])/separation, (t[1]-nodes[0])/separation]
    denominators = {'gamma0': gamma[0], 'D': d, '2': I(2),
                    'v1': nodes[0], 'v2': nodes[1], 'v2_minus_v1': separation,
                    '120': I(120)}
    assert all(v.lo > 0 for v in denominators.values())
    assert b.lo > 0 and disc.lo > 0 and all(v.lo > 0 for v in weights)
    assert (t[1]-nodes[0]).lo > 0 and (nodes[1]-t[1]).lo > 0
    moment_boxes = [weights[0]*power(nodes[0], j)+weights[1]*power(nodes[1], j)
                    for j in range(4)]
    residual_boxes = [moment_boxes[j]-t[j] for j in range(4)]
    assert all(v.lo <= 0 <= v.hi for v in residual_boxes)
    # Interval residual containment alone is not exactness: symbolic() and
    # the node equation/recurrence supply the exact mathematical identities.
    symbolic_evidence = symbolic()
    ref_roots = [root_bracket(0, 1), root_bracket(7, 8), root_bracket(22, 23)]
    assert all(v.lo > 0 for v in ref_roots)
    assert all(ref_roots[j].hi < ref_roots[j+1].lo for j in range(2))
    lists = [[r/node for r in ref_roots] for node in nodes]
    # v1 < v2 and positive reference roots: list0[j] > list1[j].
    # Required: max lower roots <= min upper roots in each of two slots.
    gaps = [lists[1][j+1]-lists[0][j] for j in range(2)]
    pair_pass = all(v.lo >= 0 for v in gaps)
    criterion_failures = [f'interlacer slot {j+1}: upper-minus-lower strictly negative'
                          for j, v in enumerate(gaps) if v.hi < 0]
    outcome = ('COMMON_INTERLACING_OBSTRUCTION' if criterion_failures else
               'COMMON_INTERLACING_CERTIFIED' if pair_pass else 'INCONCLUSIVE')
    report = {
        'scope': 'actual degree-three theta average, exact two-node Gauss rule only',
        'method': 'Exact Fraction boxes; sqrt by integer square bounds; cubic rational sign isolation',
        'inherited_qualifications': 'L791 step478 and L778 analytic evaluator/Decimal contracts; not formal verification',
        'provenance': {str(p.relative_to(ROOT)): digest(p) for p in (source, audit_path, Path(__file__).resolve())},
        'inherited_original_hashes': audit['original_hashes'],
        'selected_audit_checks': selected,
        'input_gamma_decimal': data['gamma'][:4],
        'input_gamma_rational': [v.pair() for v in gamma],
        'normalization': 't_j=(2j)!*gamma(j)/(j!*gamma(0)); t0=1 exactly',
        'conversion_factors': [str(F(factorial(2*j), factorial(j))) for j in range(4)],
        'raw_moments': [v.pair() for v in t],
        'symbolic': symbolic_evidence,
        'node_polynomial': {'A': a.pair(), 'B': b.pair(), 'D': d.pair(),
                            'discriminant': disc.pair(), 'sqrt_discriminant': sqrt_disc.pair(),
                            'sqrt_endpoint_square_checks': [sqrt_disc.lo**2 <= disc.lo, sqrt_disc.hi**2 >= disc.hi]},
        'denominators': {k: v.pair() for k, v in denominators.items()},
        'nodes': [v.pair() for v in nodes],
        'weights': [v.pair() for v in weights],
        'mean_between_nodes': [(t[1]-nodes[0]).pair(), (nodes[1]-t[1]).pair()],
        'moment_evaluation_boxes': [v.pair() for v in moment_boxes],
        'moment_residual_boxes_not_exactness_proof': [v.pair() for v in residual_boxes],
        'reference_polynomial': 'h(y)=y^3-30y^2+180y-120=-120*F_(3,1)(y)',
        'reference_roots': [v.pair() for v in ref_roots],
        'reference_endpoint_values': [[str(h(v.lo)), str(h(v.hi))] for v in ref_roots],
        'scaled_root_lists': [[v.pair() for v in row] for row in lists],
        'interlacer_gaps_upper_minus_lower': [v.pair() for v in gaps],
        'outward_display': {'nodes': [coarse(v) for v in nodes],
                            'weights': [coarse(v) for v in weights],
                            'scaled_roots': [[coarse(v) for v in row] for row in lists],
                            'interlacer_gaps': [coarse(v) for v in gaps]},
        'requirements': {'both_interlacer_gaps': '>=0; endpoint equality allowed',
                         'nodes_weights_denominators': '>0',
                         'polynomial_identity': 'exact coefficient equality, not small interval residuals'},
        'criterion_failures': criterion_failures,
        'verification_failures': [],
        'outcome': outcome,
    }
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('outcome:', outcome)
    print('actual outward rational bounds:', report['outward_display'])
    print('required:', report['requirements'])
    print('criterion failures:', criterion_failures)
    print('verification failures:', report['verification_failures'])
    print('complete certificate:', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
