# Corollary 938a: the actual row-mixture ratio cannot be globally nondecreasing

## Hypotheses

Use L019's actual continuous kernel K, including K(u)>0 for every
u>=0, and exactly L938(5)–(9): all 34 signed rows c_alpha, twelve
labelled factors per row, their factorials, and the M_0^12
normalization. For E>0 set

    V_plus(E)  = sum_(c_alpha>0) c_alpha h_alpha(E),
    V_minus(E) = sum_(c_alpha<0) (-c_alpha) h_alpha(E),
    R(E) = V_plus(E)/V_minus(E).

For the incompatibility conclusion only, import L938(3a)'s certified
B_0=integral_0^(1/4) v(E)dE<0. This retains L938's directed Decimal
basic-operation and correctly rounded nearest-exponential contracts,
outward widening, precision 200, rejected exceptional arithmetic,
exact integer arithmetic and rational square-root endpoint checks.
The step50 audit does not verify the underlying libraries independently.
The analytic denominator and limit conclusions below do not require
those numerical contracts. No monotonicity, contact, PSD, endpoint
sign in lambda, zero-location or RH assumption is made.

## Conclusion

Both V_plus and V_minus are finite, strictly positive and continuous
on (0,infinity), with finite strictly positive total masses. Define

    C = K(0)^12 pi^6/(2^36 17!),
    S_plus  = sum_(c_alpha>0) c_alpha / product_(k=0)^6 (k!)^alpha_k,
    S_minus = sum_(c_alpha<0) (-c_alpha) / product_(k=0)^6 (k!)^alpha_k.

These are finite constants, C>0 and S_plus=S_minus>0, and

    lim_(E down to 0) V_plus(E)/E^17  = C S_plus >0,
    lim_(E down to 0) V_minus(E)/E^17 = C S_minus >0,
    lim_(E down to 0) R(E) = 1.                                  (1)

Subject to the imported arithmetic contracts, some E_* in (0,1/4)
satisfies R(E_*)<1. Hence R is not nondecreasing on the whole open
half-line. This retires this particular global ratio-order sufficient
mechanism. It neither refutes nor proves the at-most-one-crossing
property of v, any sign of its transform, or RH.

## Proof

### Finite positive denominators and masses

For a row choose its twelve indices k_i as in L938(9), and put
w_alpha(t)=product_i t_i^(k_i-1/2) on the eleven-dimensional simplex.
Every k_i+1/2 is positive. Consequently w_alpha is positive on the
relative interior, and the Euler beta integral gives

    integral_Delta_11 w_alpha(t)dt
      = product_i Gamma(k_i+1/2)/Gamma(18),                        (2)

which is strictly positive and finite. For fixed E>0 the twelve
arguments sqrt(E t_i) lie in [0,sqrt(E)]. Continuity and strict
positivity of K give finite extrema 0<m_E<=K<=M_E on that interval.
Thus the integral in L938(9) lies between m_E^12 and M_E^12 times
(2), and its remaining prefactor is finite and strictly positive.
It follows that 0<h_alpha(E)<infinity for each row and E>0.
The singular factors with k_i=0 are covered by (2), not discarded.
Their values on boundary faces do not affect the integral.

L938(9)'s same compact majorant gives continuity of h_alpha.
There are rows of each sign, so the finite sums V_plus,V_minus are
strictly positive and continuous. L938(10) and its Tonelli argument
with b=r=0 give integral h_alpha<infinity for every row. Hence the
two total masses are finite; continuity and strict positivity on
any compact interior interval make each mass nonzero. No probability
normalization or probability-order theorem is needed below.

### Separate leading coefficients, with the singular weights retained

Fix E_0>0. For 0<E<=E_0 the product of kernel factors in (9) is
bounded by (max_[0,sqrt(E_0)] K)^12. Multiplying this constant by
w_alpha gives the integrable majorant (2). Every kernel factor tends
to K(0) as E decreases to zero. Dominated convergence, applied after
dividing (9) by E^17, therefore gives the separate row limit

    ell_alpha = K(0)^12/(2^12 Gamma(18))
                * product_i Gamma(k_i+1/2)/(2k_i)!.

The elementary half-integer gamma identity
Gamma(k+1/2)/(2k)!=sqrt(pi)/(4^k k!) follows from Gamma(1/2)=sqrt(pi)
and the gamma recurrence. Since there are twelve indices and their
sum is 12, with Gamma(18)=17!, this is exactly

    ell_alpha = C / product_(k=0)^6 (k!)^alpha_k.                  (3)

No multinomial factor occurs: each h_alpha is the convolution of
twelve labelled factors. In particular, the zero-index factors and
the A_0^6 factor retained by L938 remain in this calculation.
Finite summation of (3), separately over each sign, proves the first
two limits in (1) with the stated S_plus and S_minus.

These sums are nonzero individually, independently of cancellation.
For example, L938's row c=64, alpha=(9,0,0,0,3,0,0) contributes
64/(4!)^3=1/216 to S_plus. Its row c=-120,
alpha=(9,0,0,1,1,1,0) contributes 120/(3!4!5!)=1/144 to S_minus.
All other summands in these two sums are positive. The exact
constant-kernel cancellation at the end of L938's analytic proof,
also checked in its step50 audit, is

    sum_alpha c_alpha/product_k(k!)^alpha_k = 0.

It says S_plus=S_minus. Combined with the separate positive limits
already proved, it gives lim R=1 by the quotient limit law. This
does not divide v's vanishing leading coefficient by zero, and does
not assign a ratio at E=0, where both densities themselves vanish.

The analytic tools here are the dominated convergence theorem and
the Euler beta integral with positive parameters, precisely the
specialization already used in L938(9); the latter is
[NIST DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1). The row-specific
limits and positivity checks are necessary applicability work for
the approved endpoint test, not a reproof of a stochastic-order
theorem or a claimed new general result.

### The first cell contradicts global nondecreasing order

L938 gives the pointwise continuous representative

    v(E)=V_plus(E)-V_minus(E)=V_minus(E)(R(E)-1), E>0.

If R were nondecreasing, then for every fixed E>0 and 0<e<E we
would have R(e)<=R(E). Let e decrease to zero in (1). This yields
R(E)>=1, and therefore v(E)>=0 for every E>0. It would imply
B_0>=0, contradicting the imported strict sign. More explicitly,
the existing enclosure has the outward upper bound
B_0 < -3.657*10^-54 < 0. Continuity of v and B_0<0 supply a point
E_* in (0,1/4) with v(E_*)<0, so strict denominator positivity gives
R(E_*)<1. The limit 1 supplies a smaller e with R(e)>R(E_*), an
actual violation of nondecreasing order without locating either
point numerically.

The canonical source of this certified mass is L938(3a), its
"Sign criterion" section and its complete step50 audit. The full
first-cell interval is in
`scripts/heat/actual-h2-energy-cell-48.json`, JSON pointer
`/mass_test/cells/0/full_mass_interval`, checked by
`scripts/heat/audit-actual-h2-energy-cell-50.py` and recorded in
`scripts/heat/actual-h2-energy-cell-audit-50.json`. This proof imports
that audited result with its contracts; it does not certify a new
quadrature or claim independent validation of Decimal/exponential
implementations. No replay, enlarged grid, tail approximation or
derivative interchange is required by this endpoint contradiction.

The approved assessment is
`drafts/literature/2026-11-09-l938-ratio-endpoint-compatibility-scope-61.md`.
Its parent source review distinguishes known likelihood-ratio
diagnostics from actual-law order. This is a standard specialization
with new local negative evidence for the proposed mechanism; no
originality beyond the inspected sources is claimed. The full
density crossing bound, parameter endpoint signs, contacts, other
degrees, initialization, realization and continuation remain open.

## Mathlib

Full and supporting Mathlib coverage for this exact statement has
not been checked. Availability is unknown, not asserted absent.
The named integration tools do not formally verify the imported
numerical implementation contracts or the Xi positivity problem.
