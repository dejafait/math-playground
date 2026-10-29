#!/usr/bin/env python3
"""Exact, bounded feasibility certificate; does not enumerate Selmer classes.

Cremona, corrected 2nd ed., III.3.1--3.2 and III.3.6 pp.92--94.
Run from beal. Standard-library rational interval arithmetic only.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

OUT = Path('scripts/pair-genus-two/elliptic-quartic-workload-certificate.json')
checks = {}


def check(name, value):
    checks[name] = bool(value)


def factors(n):
    n = abs(n)
    ans = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0)+1
    return ans


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def of(x):
        return x if isinstance(x, Interval) else Interval(Q(x), Q(x))

    def __add__(self, x):
        x = self.of(x)
        return Interval(self.lo+x.lo, self.hi+x.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, x):
        return self + -self.of(x)

    def __rsub__(self, x):
        return self.of(x) + -self

    def __mul__(self, x):
        x = self.of(x)
        vals = [a*b for a in (self.lo, self.hi) for b in (x.lo, x.hi)]
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.of(x)
        assert x.lo*x.hi > 0
        return self * Interval(1/x.hi, 1/x.lo)

    def square(self):
        vals = [self.lo*self.lo, self.hi*self.hi]
        return Interval(0 if self.lo <= 0 <= self.hi else min(vals), max(vals))

    def sqrt(self):
        assert self.lo >= 0
        scale = 2**100

        def lower(x):
            return isqrt((x.numerator*scale**2)//x.denominator)

        low, high = lower(self.lo), lower(self.hi)+1
        result = Interval(Q(low, scale), Q(high, scale))
        assert result.lo**2 <= self.lo and result.hi**2 >= self.hi
        return result

    def compact(self):
        """Certified outward rational rounding, never float formatting."""
        scale = 10**12
        lower = (self.lo*scale).__floor__()
        upper = (self.hi*scale).__ceil__()
        result = Interval(Q(lower, scale), Q(upper, scale))
        assert result.lo <= self.lo <= self.hi <= result.hi
        return result


def invariant_data(ai):
    a1, a2, a3, a4, a6 = ai
    b2 = a1*a1+4*a2
    b4 = a1*a3+2*a4
    b6 = a3*a3+4*a6
    c4 = b2*b2-24*b4
    c6 = -b2**3+36*b2*b4-216*b6
    return c4, c6, Q(c4**3-c6**2, 1728)


A, B = -2874960, 1739350800
old_ai = [0, 0, 0, A, B]
old_c4, old_c6, old_delta = invariant_data(old_ai)
fac4, fac6 = factors(old_c4), factors(old_c6)
max_scaling = 1
for p in fac4.keys() & fac6.keys():
    max_scaling *= p**min(fac4[p]//4, fac6[p]//6)
check('all_possible_integer_scalings_divide_6', max_scaling == 6)
normalizations = []
for u in range(1, max_scaling+1):
    if max_scaling % u:
        continue
    c4, c6 = Q(old_c4, u**4), Q(old_c6, u**6)
    delta = (c4**3-c6**2)/1728
    integral = all(v.denominator == 1 for v in (c4, c6, delta))
    kraus = integral and c6 % 27 not in (9, 18) and (
        c6 % 4 == 3 or (c4 % 16 == 0 and c6 % 32 in (0, 8)))
    normalizations.append(dict(u=u, c4=c4, c6=c6, delta=delta,
                               integral_discriminant=delta.denominator == 1,
                               kraus_pass=bool(kraus)))
valid = [v['u'] for v in normalizations if v['kraus_pass']]
check('maximal_kraus_scaling_is_2', max(valid) == 2)
minimal_ai = [0, 0, 1, -179685, 27177356]
c4, c6, delta = invariant_data(minimal_ai)
check('minimal_invariants_exact', (c4, c6, delta) ==
      (8624880, -23481235800, Q(52212919952197125)))
check('scaled_invariants_match',
      (old_c4, old_c6, old_delta) == (2**4*c4, 2**6*c6, 2**12*delta))
# x=4X, y=8Y+4. Coefficients of the transformed equation,
# ordered as Y²,Y,X³,X,constant, must be 64 times the new equation.
transform_residual = [64-64, 64-64, -4**3+64,
                      -4*A-64*179685, 16-B+64*27177356]
check('rational_model_change_identity', transform_residual == [0]*5)
check('model_change_invertible_over_Q', 4*8 != 0)
mod7 = [(k**3+A*k+B) % 7 for k in range(7)]
check('monic_cubic_has_no_mod7_root', all(mod7))

I, J = c4, 2*c6
dyadic = dict(I_mod16=I % 16, J_mod64=J % 64,
              I_mod4=I % 4, J_mod8=J % 8,
              twoI_plus_J_mod16=(2*I+J) % 16)
check('basic_pair_not_dyadically_divisible', not (I % 16 == 0 and J % 64 == 0))
check('larger_pair_omission_criterion',
      I % 4 == 0 and J % 8 == 0 and (2*I+J) % 16 == 0)
disc = 4*I**3-J**2
check('positive_nonzero_quartic_discriminant', disc > 0)


def f(x):
    return x**3-3*I*x+J


root_records = []
roots = []
for left, right in [(-4000, -3000), (-3000, -2000), (5000, 6000)]:
    lo, hi = Q(left), Q(right)
    assert f(lo)*f(hi) < 0
    for _ in range(100):
        mid = (lo+hi)/2
        assert f(mid) != 0
        if f(lo)*f(mid) < 0:
            hi = mid
        else:
            lo = mid
    root = Interval(lo, hi).compact()
    assert f(root.lo)*f(root.hi) < 0
    roots.append(root)
    root_records.append(dict(interval=root,
                             endpoint_values=[f(root.lo), f(root.hi)]))
check('three_disjoint_root_brackets',
      roots[0].hi < roots[1].lo and roots[1].hi < roots[2].lo)
# The sign changes give three distinct real roots of a cubic, hence all roots.
phi3, phi2, phi1 = roots
K = (4*I-phi1.square())/3
sqrtK = K.sqrt()
denom1 = 3*sqrtK+phi1+2*phi2
check('type1_K_and_denominator_positive', K.lo > 0 and denom1.lo > 0)
bound1 = ((K+sqrtK*phi1)/denom1).compact()
bound2pos = ((I-phi2.square())/(3*(phi2-phi3))).compact()
bound2neg = ((I-phi2.square())/(3*(phi1-phi2))).compact()
regions = []
for name, bound in [('type1_positive', bound1),
                    ('type2_positive', bound2pos),
                    ('type2_negative', bound2neg)]:
    nlo, nhi = bound.lo.__floor__(), bound.hi.__floor__()
    check(name+'_a_floor_certified', nlo == nhi and nlo > 0)
    regions.append(dict(type=name, abs_a_bound=bound,
                        maximum_abs_a=nhi, b_convention='-2|a| < b <= 2|a|',
                        raw_ab_rows=2*nhi*(nhi+1)))

width1 = ((phi1-phi2)/2).compact()
check('type1_width_strictly_above_4044', width1.lo > 4044)
check('type1_includes_every_a_from_1_to_16', bound1.lo >= 16)
subset_rows = 2*16*17
triple_lower = subset_rows*4044
row_count = sum(v['raw_ab_rows'] for v in regions)
caps = dict(ab_rows=200000, abc_triples=2000000)
check('type1_rows_alone_exceed_row_cap', regions[0]['raw_ab_rows'] > caps['ab_rows'])
check('type1_subset_exceeds_triple_cap', triple_lower > caps['abc_triples'])

certificate = dict(
    target="Test whether an explicit two-descent on L112's elliptic model can certify rank E(Q) <= 1 without the parked class-group backend.",
    assessment='drafts/literature/2026-10-25-marked-elliptic-explicit-two-descent.md',
    sources=dict(minimality='Cremona III.3.1 Prop.3.1.1 and III.3.2 pp.63-65',
                 invariant_selection='Cremona III.3.6 Step 1 p.92',
                 coefficient_regions='Cremona III.3.6 Step 2 p.94'),
    input_hashes={'lemmas/L112-marked-elliptic-positive-rank.md':
                  sha256(Path('lemmas/L112-marked-elliptic-positive-rank.md').read_bytes()).hexdigest()},
    old_model=dict(ai=old_ai, c4=old_c4, c6=old_c6, delta=old_delta,
                   c4_factorization=fac4, c6_factorization=fac6),
    normalization=dict(candidates=normalizations, maximal_scaling=2,
                       minimal_ai=minimal_ai, c4=c4, c6=c6, delta=delta,
                       forward='x=4X,y=8Y+4', inverse='X=x/4,Y=(y-4)/8',
                       polynomial_residual=transform_residual),
    rational_two_torsion=dict(modulus=7, reduced_cubic=[1, 0, A % 7, B % 7],
                              values_on_all_residues=mod7, dimension=0),
    invariant_selection=dict(I=I, J=J, dyadic=dyadic, required_pairs=[[I, J]],
                             larger_pair_omitted=True, discriminant=disc),
    root_certificates=root_records,
    bounds=dict(K=K.compact(), sqrtK=sqrtK.compact(),
                type1_denominator=denom1.compact(), regions=regions,
                type3_applicable=False, type1_c_interval_width=width1),
    workload=dict(caps=caps, complete_raw_ab_row_count=row_count,
                  ab_rows_visited=0, abc_triples_enumerated=0,
                  type1_subset_a=[1, 16], type1_subset_rows=subset_rows,
                  integers_per_c_interval_at_least=4044,
                  certified_abc_triple_lower_bound=triple_lower,
                  full_abc_count_computed=False,
                  mechanism='Closed-form row count and interval-width lower bound; no truncated descent.',
                  result='STOP_UNSIEVED_REGION_OVER_CAP'),
    limitations=['No quartic reconstruction, syzygy sieve, local exclusion or class merge run.',
                 'No Selmer dimension, Sha claim, rank upper bound or Beal exclusion.',
                 'Raw workload is not a lower bound on inequivalent or locally soluble classes.'],
    checks=checks, failures=[k for k, v in checks.items() if not v])


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, Interval):
        return dict(lo=str(value.lo), hi=str(value.hi))
    raise TypeError(type(value).__name__)


OUT.write_text(json.dumps(certificate, default=encode, indent=2)+'\n')
print('Minimal model:', minimal_ai, '; rational 2-torsion dimension: 0')
print('Required invariant pairs:', [[I, J]])
print('Certified |a| maxima:', [v['maximum_abs_a'] for v in regions])
print('Complete raw (a,b) rows:', row_count, '; cap:', caps['ab_rows'])
print('Certified raw triple lower bound:', triple_lower, '; cap:', caps['abc_triples'])
print('Actual rows visited: 0; triples enumerated: 0; analytic counting only')
print('Checks:', len(checks), '; failures:', certificate['failures'])
print('Result: STOP_UNSIEVED_REGION_OVER_CAP; rank upper bound: unresolved')
print('Certificate:', OUT)
raise SystemExit(bool(certificate['failures']))
