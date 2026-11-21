# Lemma 944: the coarse direct-density enclosure cannot cover its endpoint

## Hypotheses

Use exactly L938's actual density v, twelve factors, 34 signed rows,
factorials and retained M_0^12 normalization. Reuse its audited degree
N=256 polynomial p on [0,8], root grid of size257, theta cutoff8,
coefficient grid10^-120 and precision200. The original numerical input
retains L938's directed Decimal and exponential contracts. No actual
crossing sign, parameter endpoint sign, contact, realization or RH
premise is assumed. The new computations use exact integers/rationals.

This result concerns the symmetric error enclosures defined below,
using the coarse common factor bound 8. It makes no assertion that
these error allowances are lower bounds on the actual errors.

## Conclusion

Define epsilon as in L938(15). Write eta_l for its complete coefficient
errors, d_l for its chosen Chebyshev coefficients, r=2/3, n=N+1, and

    S0=r^n/(1-r),
    S2=r^n[n^2/(1-r)+2nr/(1-r)^2+r(1+r)/(1-r)^3],
    delta=(10^9/2)(S2+N^2 S0)+sum_(l=0)^N eta_l l^2/4,
    B=sum_(l=0)^N |d_l|l^2/4+delta,
    A=12 epsilon 8^11,
    D=delta 8^11+11B epsilon 8^10,
    Z=(293/540)/(2^36 17!).                                      (1)

Then, on [0,8], |k'-p'|<=delta and |k'|,|p'|<=B, for
k(x)=K(sqrt(x)) with its analytic definition at zero. For 0<E<=8,

    |v(E)-v_p(E)|/pi^6 <= Z E^17 A=:a(E),
    |v'(E)-v_p'(E)|/pi^6 <= Z E^16(17A+ED)=:b(E).                (2)

At the closed endpoint E=4 the exact polynomial evaluations satisfy

    .0338 < [v_p(4)/pi^6]/a(4) < .0339,
    .000220 < -[v_p'(4)/pi^6]/b(4) < .000221.                    (3)

Thus both symmetric singleton enclosures from (2) contain zero
strictly. No closed-interval cover using these same radii and valid
polynomial range enclosures can cover E=4 by either a v-range
excluding zero or a strictly positive v'-range. This stops that fixed
implementation before subdivision. It does not refute the actual
crossing assertion, the direct-integration mechanism, or RH. Sharper
majorants using the same polynomial are not ruled out.

## Proof

### Derivative inclusion without differentiating a real error bound

L938 establishes analytic k on a neighborhood of the filled energy
ellipse rho=3/2, with |k|<10^9. Its Chebyshev series in y=x/4-1 has
coefficients bounded by 2*10^9 r^m for m>=1. The degree-N root-grid
interpolant of T_m is zero or a signed T_j with j<=N, by L938's
explicit alias identity. Modes m<=N are interpolated exactly.

The named identities are T_m'=m U_(m-1),
[DLMF18.9.21](https://dlmf.nist.gov/18.9#E21), and
|U_(m-1)(y)|<=m on [-1,1], the lambda=1 Gegenbauer case of
[DLMF18.14.4](https://dlmf.nist.gov/18.14#E4), using
[DLMF18.7.4](https://dlmf.nist.gov/18.7#E4) to identify U with C^1.
For m>=1 this gives |d/dx T_m(x/4-1)|<=m^2/4;
the constant mode has zero derivative. In particular an aliased mode
has derivative at most N^2/4, even when its actual degree is smaller.
Absolute uniform convergence of the differentiated series follows
from sum m^2 r^m<infinity. It justifies differentiation of the actual
analytic series and comparison with the finite interpolant. More
explicitly, interpolation is a finite linear combination of node
evaluations, so it commutes with the absolutely uniformly convergent
series. The derivatives of the interpolated tail also converge
absolutely uniformly, since their norms are bounded by N^2/4 times
the summable coefficient magnitudes. Thus differentiation is justified
on both sides of the tail comparison, including constant aliases.

Consequently the derivative of the omitted series minus its
interpolant is bounded by

    (10^9/2) sum_(m=N+1)^infinity (m^2+N^2)r^m.

Writing m=n+j and summing the geometric series and its first two
derivatives gives exactly S0 and S2 in (1). Replacing each exact
interpolation coefficient by d_l costs at most sum eta_l l^2/4.
These eta_l already pay the full theta tail, node arithmetic and
coefficient rounding in L938; no differentiated theta-tail estimate
or new cutoff is silently assumed. This proves the delta bound.
The same Chebyshev inequality bounds |p'| by the displayed sum in B;
the triangle inequality also bounds |k'| by B.

### Twelve factors, endpoint singularities and the energy prefactor

L938 proves 0<k<7 and |p|<=8. For t in the closed unit simplex,
write G(E,t)=product_i k(Et_i) and G_p(E,t)=product_i p(Et_i).
Telescoping twelve factors gives |G-G_p|<=A. Differentiate each
product in E. For its i-th term, first replace k'(Et_i) by p'(Et_i),
then replace the other eleven factors. Its absolute error is at most

    t_i[delta 8^11+B*11 epsilon 8^10].

Since sum t_i=1, summing yields |partial_E(G-G_p)|<=D, rather
than an additional unneeded factor twelve.

Apply these estimates separately to each of L938(9)'s 34 rows and
sum with |c_alpha|. All row weights are integrable, because their
Dirichlet parameters are k_i+1/2>0. The beta integral gives the
total absolute row weight, including 2^-12 and all (2k_i)! factors,
as pi^6 Z. The exact sum of |c_alpha|/product(k!)^alpha_k is
293/540, verified from all rows in L938 and in the new certificate.

Here is the precise dominated-differentiation argument, also covering
the stated outer endpoint. Fix E_0 in (0,8] and choose a small open
energy neighborhood J of E_0 with positive lower endpoint. L938's
analytic neighborhood of the filled ellipse contains a slightly
larger real interval than [0,8], so J can be chosen such that all
E t_i lie in a compact interval where k,k',p,p' are continuous and
bounded, even when E_0=8. Let U_0>=1 bound |k| and |p| there, and
let U_1 bound their first derivatives. On the open simplex, the
products are continuously differentiable in E and their derivative
difference has absolute value at most 2 U_1 U_0^11 sum_i t_i
=2 U_1 U_0^11. The mean value theorem therefore bounds every
sufficiently small difference quotient of G-G_p by this same
constant. Multiplication by each row's measurable Dirichlet weight
gives an integrable majorant independent of the difference quotient.
The boundary faces are null sets; their singular weights are retained
in the integrability argument, not discarded as bounded functions.
Lebesgue dominated convergence now differentiates each row integral;
the same argument applied separately to G and G_p gives both
derivatives. This is two-sided at E_0=4 and also at E_0=8. At the
evaluation point E_0<=8, the sharper bounds A,D already proved on
[0,8] apply; the enlarged-neighborhood constants only justify the
interchange. Differentiating E^17 contributes
17E^16 A, and differentiating the product contributes E^17 D.
This proves (2) directly from the integral; it does not differentiate
L938's integrated error inequality or assume L942's unaudited identity.

### Complete fixed-coefficient endpoint computation

L938(18) gives, with its saved integer R_l and common C,

    v_p(4)/pi^6=sum_l R_l 4^(17+l)/[C^12(17+l)!],
    v_p'(4)/pi^6=sum_l R_l 4^(16+l)/[C^12(16+l)!].                (4)

The second equality differentiates a finite polynomial. Both sums
are evaluated exactly: use the common factorial (3072+s)! for
s=17 or16, multiply each R_l by the integer factorial quotient,
and apply integer Horner evaluation at4, then multiply by4^s.
There is no floating cancellation or pi rounding in (3)-(4): the
positive constant pi^6 is divided out of both value and error.

Reproduction command:

    python3 scripts/heat/l938-direct-endpoint-enclosure-69.py

The full exact constants, two sums, radii, rational endpoints,
input hashes and every check are in
`scripts/heat/l938-direct-endpoint-enclosure-69.json`.
The script checks all 257 coefficient radii, all 34 beta weights,
fixed budgets and denominator, and both exact brackets (3).
It verifies that the three original producer/input hashes match
L938's separate step50 audit, reads every one of that audit's 5101
pass/fail entries, and checks its completed exact-polynomial residual.
The old theta-node and entire-polynomial proofs are reused from the
audited L938, not claimed to have been independently replayed here.

For scale only, the computed centers and allowances are approximately

    v_p(4)/pi^6  =  8.85584862764e-42,  a(4)=2.61965515575e-40,
    v_p'(4)/pi^6 = -8.02308777963e-41,  b(4)=3.63529404138e-37.

The exact comparisons (3), not these rounded displays, prove strict
zero containment. On any interval containing4, a valid polynomial
range contains its value at4, while the suprema of (2)'s radii are
at least their values at4. Adding the symmetric radius therefore
still contains the unresolved singleton range. Neither permitted
cover criterion can hold there. One singleton was tested; zero
subdivision intervals were examined, below depth12/8191 limits.
The whole target interval remains uncertified. No actual zero or
nonpositive actual derivative at a zero has been established.

This is a reproduction/specialization of known Chebyshev, beta and
interval-inclusion methods under the pre-existing SPECIALIZE scope.
The local negative result is the failure of these particular coarse
enclosures, not a discovery beyond those methods.

### Independent conceptual audit — 9 November 2026, step75

The prior SPECIALIZE scope
`drafts/literature/2026-11-09-l944-c944a-audit-scope-73.md`
was reused for this audit. The affine derivative factor, constant and
signed/zero aliases, both uniformly convergent derivative series,
both geometric tails, coefficient errors, simplex differentiation,
twelve factors and E^17 prefactor were checked. The neighborhood and
difference-quotient argument above makes the closed-endpoint claim
explicit. No mathematical constant, polynomial or budget changed.

Reproduce the independent rational audit with

    python3 scripts/heat/audit-l944-c944a-75.py

Its full certificate is `scripts/heat/l944-c944a-audit-75.json`.
All 15620 checks pass, with no failures. It checks every one of the
5101 inherited audit entries, all 529 coarse and 540 sharper endpoint
entries, all 257 complete coefficient allowances, and every one of
the 34 canonical table rows and their positive half-integer beta
factors. It checks the exact 10^-120 grid and power denominator.
All 3073 saved polynomial coefficients are read under matching input
hashes; their complete maximum and the full inherited coefficient
bound are recomputed by rebuilding the 1799 integer Q coefficients.
The complete inherited zero residual and strict uniqueness bound are
checked. The enormous polynomial-identity evaluation itself is reused
from audited L938/step50, not claimed to have been independently rerun.

For each of offsets 17 and16, the audit independently sums
R_l 4^(l+s)(3072+s)!/(l+s)!, splitting even and odd l and checking
every factorial division exactly. This differs from the producers'
descending Horner recurrence. Division by C^12(3072+s)! reproduces
both complete rational centers. Every radius, endpoint and strict
ratio comparison is recomputed exactly. Both reviewed endpoint
producers replay into separate `-replay-75.json` files and their full
reports equal the original reports. All original input hashes remain
unchanged. No new theta-node or transcendental-library verification
is claimed; the stated numerical execution contracts remain.

The audit's first run stopped on its own incorrect expected coarse
check count, 528 instead of529. Its report is preserved in
`scripts/heat/l944-c944a-audit-75-count-failure.json`; the rerun changes
only that assertion. This bookkeeping failure does not alter any
mathematical claim. The step73 reporting-bracket failure is also
retained and checked, as described in C944a. The audit validates the
existing local coarse obstruction and sharper singleton application;
it supplies no additional signs or compact crossing result.

## Mathlib

Full or supporting Mathlib coverage of this exact derivative enclosure
and certificate has not been checked. Availability is unknown.
The cited DLMF identities and the audited L938 inputs are informal
mathematical sources, not formal verification of this computation.
