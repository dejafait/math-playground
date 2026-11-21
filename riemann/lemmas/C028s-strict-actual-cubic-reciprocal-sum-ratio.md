# Corollary C028s: strict actual cubic reciprocal-sum ratio

## Hypotheses

Use the actual completion Xi of L018, the positive moments M_(2j) of
L021 and the absolutely convergent real sums S_k of L025. Put

    gamma_j=j!*M_(2j)/(2j)!, b_j=gamma_j/gamma_0, j=0,1,2,3.

Thus gamma_0=M_0>0 and b_0=1. Use L027's unconditional S_2,S_3>0.
The finite identities assume no RH, reality of actual zeros, numerical
coefficient enclosure or Laguerre-Polya premise. For the separate
computer-assisted strictness certificate1917 below, additionally use
L917's accepted moment enclosures under its L037 arithmetic contracts.
In particular Decimal-library correctness is assumed, not independently
verified. The separate proof/code audit1919 below accepts this certificate
under exactly these inherited contracts.

## Conclusion

Audit1913 qualification: the strict source import proposed in1911 is not
certified; its proof contains the diagonal defect detailed below. The
finite identities and the following implication remain valid:

    H>0 implies 0<S_3<S_2^(3/2).

Precisely, define

    H=4*(gamma_1^2-gamma_0*gamma_2)
         *(gamma_2^2-gamma_1*gamma_3)
                         -(gamma_1*gamma_2-gamma_0*gamma_3)^2.

Unconditionally, the exact identity is

    H/gamma_0^4=4*(S_2^3-S_3^2).

Certificate1917 supplies a different, computer-assisted strictness argument,
subject to L917/L037's hypotheses and accepted by audit1919. It gives

    7.0891180*10^(-15) <= H <= 7.8529158*10^(-15).

Thus, under those input contracts, H>0 pays C028r's strict scalar premise
and gives 0<S_3<S_2^(3/2). C028r's arbitrary-site matching argument
passes audit1913 conditionally. No bound on selected parameters, lower
coefficient residuals, full Schmeisser cost, uniform-in-degree behavior,
all-degree positivity or RH follows here. The failed original source
import is preserved below; this numerical argument does not repair its
proof or assert falsity of the source theorem.

## Proof

### Proposed strict import and actual normalization

D. K. Dimitrov and F. R. Lucas, *Higher order Turan inequalities for
the Riemann xi-function*, Proc. Amer. Math. Soc. **139** (2011),
1013-1022, [DOI 10.1090/S0002-9939-2010-10515-4](https://doi.org/10.1090/S0002-9939-2010-10515-4):
use coefficient definitions p.1014, (5)/(9) pp.1015-1016,
Theorem 1/Corollary 1 p.1017, and the strict conclusion of the proof
p.1021. The inspected [author-uploaded published text](https://www.researchgate.net/publication/257765645_Higher_order_Turan_inequalities_for_the_Riemann_xi-function)
states strict higher-order Turan positivity at the end of its proof for
the actual hatted coefficients, including k=1. The attempted import uses
that ending, rather than the non-strict displayed theorem or hyperbolicity alone. The
actual application is their Corollary 1 and Theorem B; no abstract
kernel hypothesis is inferred from a different local concavity claim.
Audit1913 below blocks this strict import. In this section every sign
inference from hat_H>0 is conditional on that unverified assertion;
the displayed normalization equalities do not depend on it.

In their notation, with half-line moments hat_b_j of their theta kernel,

    Xi(x/2)/8=sum_j (-1)^j*hat_b_j*x^(2j)/(2j)!,
    hat_gamma_j=j!*hat_b_j/(2j)!.

Comparing this convergent entire expansion with L021, and using L018
to identify the even completion, gives exactly

    hat_b_j=M_(2j)/(8*4^j),
    gamma_j=8*4^j*hat_gamma_j.                         (1)

There is no extra factorial in (1). At k=1 the source's expression (5)
is

    hat_H=4*(hat_gamma_1^2-hat_gamma_0*hat_gamma_2)
             *(hat_gamma_2^2-hat_gamma_1*hat_gamma_3)
                 -(hat_gamma_1*hat_gamma_2-hat_gamma_0*hat_gamma_3)^2.

Its strict sign was the proposed imported input. In detail, (9)'s half-line
moment expression at k=1 is

    tilde_H=20*(3*hat_b_1^2-hat_b_0*hat_b_2)
                  *(5*hat_b_2^2-3*hat_b_1*hat_b_3)
                      -3*(5*hat_b_1*hat_b_2-hat_b_0*hat_b_3)^2.

Substituting hat_gamma_0=hat_b_0, hat_gamma_1=hat_b_1/2,
hat_gamma_2=hat_b_2/12, hat_gamma_3=hat_b_3/120 gives
hat_H=tilde_H/43200. Theorem 1's whole-line moment convention,
if used instead, doubles every hat_b_j; tilde_H then multiplies by16.
Thus a justified strict conclusion would give the same half-line sign.
This is a normalization check, not a reproof of the kernel theorem.

The first parenthesis in H scales from its hatted counterpart by
8^2*4^2, the second by8^2*4^4, and the squared parenthesis by
(8^2*4^3)^2. Consequently

    H=8^4*4^6*hat_H.                                 (2)

### Reciprocal polynomial and centering

Let hat_J(t)=hat_gamma_0+3*hat_gamma_1*t
                      +3*hat_gamma_2*t^2+hat_gamma_3*t^3.
This is exactly the source's ascending g_(3,0), with no alternating
signs. Equation (1) gives J(t)=8*hat_J(4*t), where
J(t)=gamma_0+3*gamma_1*t+3*gamma_2*t^2+gamma_3*t^3.
Its reciprocal monic polynomial is C028a's

    P_3(x)=x^3*J(1/x)/gamma_0
          =x^3+3*b_1*x^2+3*b_2*x+b_3.

Here the right side defines the polynomial also at x=0. Both endpoint
coefficients gamma_0,gamma_3 are positive by L021. Thus reversal has
degree three and no zero endpoint; nonzero roots are reciprocated
without loss of multiplicity. A sign convention J(-t) would require
reflection before this reversal. Neither actual-root reality nor
infinite product reversal is used.

The root mean of P_3 is -b_1 by its coefficient of x^2, even if roots
are complex. Substitution x=y-b_1 gives

    P_3(y-b_1)=y^3-3*v*y+2*w,
    v=b_1^2-b_2, w=(b_3-3*b_1*b_2+2*b_1^3)/2.

C028a's locally convergent logarithm comparison with L025 establishes
v=S_2 and w=S_3. Thus this is exactly the centered actual cubic
y^3-3*S_2*y+2*S_3, rather than L823's differently centered ascending
polynomial. The formula Delta(y^3+p*y+q)=-4*p^3-27*q^2 gives its
discriminant 108*(S_2^3-S_3^2), consistent with 27*H/gamma_0^4 below.
For the standard discriminant formula see L. E. Dickson, *First Course
in the Theory of Equations* (1922), Chapter IV, Sections 44-45,
(11)-(12), pp.53-54 ([text](https://www.gutenberg.org/files/29785/29785-pdf.pdf)),
already assessed in source review1910 via L823. No root classification
is required here, and no sign is inferred from numerics.

### Exact sign conversion, conditional strictness

Solve for b_2=b_1^2-v and b_3=b_1^3-3*b_1*v+2*w. Directly,

    b_2^2-b_1*b_3=b_1^2*v+v^2-2*b_1*w,
    b_1*b_2-b_3=2*(b_1*v-w).

Since gamma_0>0, division of H by gamma_0^4 therefore gives

    H/gamma_0^4
      =4*v*(b_1^2*v+v^2-2*b_1*w)-4*(b_1*v-w)^2
      =4*(v^3-w^2)=4*(S_2^3-S_3^2).

L027 gives S_2,S_3>0. Consequently, IF H>0, taking the positive
square root gives 0<S_3<S_2^(3/2). A nonnegative sign alone leaves
the equality case and does not suffice for C028r's finite IVT argument.

### Conceptual audit1913: a diagonal gap in the strict source proof

The actual scaling (1), the factor43200, the positive scale in (2),
reciprocal centering and the identity H/gamma_0^4=4*(S_2^3-S_3^2)
all pass the finite algebra audit. In particular the normalized actual
series is exp(S_1*t-S_2*t^2/2+S_3*t^3/3+O(t^4)) locally, by
L025 and C028a; its second and third logarithmic coefficients give
exactly v=S_2 and w=S_3. There is no factorial, affine-sign or
degree-three endpoint error to repair.

The load-bearing strictness import fails this audit. In the same
published source, p.1020 immediately before (14), a mean-value argument
is applied to A_1,0(y,z)/A(y,z) over an arbitrary interval in z.
Equation (11), p.1018, makes its denominator zero when z=y. These
displays were checked in the [author-hosted published PDF, pp.1018,
1020-1021](https://www.researchgate.net/profile/Dimitar-Dimitrov-24/publication/257765645_Higher_order_Turan_inequalities_for_the_Riemann_xi-function/links/54fda31e0cf270426d12c703/Higher-order-Turan-inequalities-for-the-Riemann-xi-function.pdf),
as well as its extracted article text. The following local check concerns
that proof step only, not a reproof or disproof of the cubic theorem.

To avoid confusing kernels, write W for the source's K and set
r(t)=W'(t)/(t*W(t)). Its hypotheses give W>0, analyticity near every
y>0 and r'(y)<0. The determinant in source (11) is exactly

    A(y,z)=(z^2-y^2)*W(y)*W(z)*(r(y)-r(z)).

For fixed y>0, Taylor expansion at z=y gives

    A(y,y+e)=-2*y*W(y)^2*r'(y)*e^2+O(e^3),

with strictly positive quadratic coefficient. Off the diagonal,
logarithmic differentiation with respect to the FIRST variable gives

    F_y(z):=A_1,0(y,z)/A(y,z)
          =-2*y/(z^2-y^2)+W'(y)/W(y)+r'(y)/(r(y)-r(z)).

The first term is -1/(z-y)+O(1), and the last is
-1/(z-y)+O(1), since r'(y) is nonzero. Hence

    F_y(y+e)=-2/e+O(1),
    F_y(y-e)= 2/e+O(1)                 (e->0+).

Thus F_y is undefined at y, with left limit +infinity and right
limit -infinity. It has no continuous extension there. More decisively,
the source's curly-bracket divided difference, at z_1=y-e>0 and
z_2=y+e, equals

    (z_2-z_1)*(F_y(z_2)-F_y(z_1))=-8+O(e)<0

for all sufficiently small positive e. The derivative used on the
right side of the asserted mean-value equality is positive wherever
it is defined: directly from the last formula for F_y,

    dF_y(z)/dz=4*y*z/(z^2-y^2)^2
                  +r'(y)*r'(z)/(r(y)-r(z))^2>0, z!=y.

Its multiplication by (z_2-z_1)^2 is therefore positive, and cannot
equal the negative divided difference. The mean value theorem does
not apply across the pole. For each fixed y, the negative divided
difference persists on a neighborhood of such an off-diagonal pair
(z_1,z_2). This defect is not confined to the measure-zero diagonal.
Multiplying by A(y,z_1)*A(y,z_2) and the positive powers in the
integral does not repair that pointwise sign inference.

This proves an exact failure of the argument used to infer the integral
sign before the final strict conclusion. It does not determine that
integral's total sign, refute the published non-strict theorem, establish
equality for actual Xi, or refute the actual strict ratio. The displayed
Theorem1/Corollary1 asserts non-strict positivity/hyperbolicity; merely
restating it cannot replace the missing equality exclusion. No theorem
repair or alternative source is imported in this audit. This strict-source
route remains unverified. The separate enclosure argument below instead
adds explicit arithmetic hypotheses; it does not upgrade this import
or supply an unconditional composed conclusion.

### Saved-panel exact-rational strictness certificate1917

Use L917's enclosure conclusion and its accepted audit197, including its
complete theta/spatial tails and L036 finite-integration remainder under
L037's Decimal contracts. At lambda=0 its M_(2j)(lambda) is exactly
L021's M_(2j), by the defining integrals with L019's same kernel. The
saved closed parameter panel0 is [0,1/5120], so it includes zero.
Consequently its complete moment boxes enclose the four moments needed
here; using them at zero does not narrow their widths or evaluate a
new integral. Only those four input records are used. L917's stopped
third H2-minor test is a different expression and remains stopped.

The full decimal endpoints are the records `/panels/0/moments/0`,
`/panels/0/moments/2`, `/panels/0/moments/4` and
`/panels/0/moments/6` in `scripts/heat/low-time-h2-uniform-195.json`.
All digits of those records and `/panels/0/lambda` were inspected.
They are finite decimal strings, parsed as exact rational numbers,
without conversion to binary floating point or denominator truncation.
For the documented exact string conversion and rational operations use
[Python fractions.Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction),
as assessed in coverage1915/approval1916. This is conventional arithmetic
specialization, not a new strictness theorem beyond the sources checked.

For rational intervals X=[l,u] and Y=[a,b], evaluate subtraction as
[l-b,u-a], addition as [l+a,u+b], and multiplication by the minimum
and maximum of la,lb,ua,ub. Square X as [0,max(l^2,u^2)] if it contains
zero and [min(l^2,u^2),max(l^2,u^2)] otherwise. Scaling uses the ordered
scaled endpoints. These formulas enclose the corresponding real operations:
subtraction/addition are monotone in their respective arguments;
a bilinear function attains its rectangle extrema at corners; x^2
is minimized at zero if present and otherwise at the nearer endpoint.
They apply even when an intermediate interval crosses zero. Inclusion
under the finite composition therefore follows by induction, independently
of repeated appearances of the same moment; those dependencies may widen
an interval but cannot invalidate containment.

Scale each moment box by the positive exact rational j!/(2j)! to obtain
G_0,...,G_3; these factors are 1,1/2,1/12,1/120. Form, in this order,

    A=G_1^2-G_0*G_2,
    B=G_2^2-G_1*G_3,
    C=G_1*G_2-G_0*G_3,
    H_box=4*(A*B)-C^2.

These are interval expressions; the contained real value is exactly
the H in the Conclusion, with C028s's audited gamma convention. No
sign is presumed in computing the endpoint products or squares. The
complete trace records every scaled moment, product, difference and
square, including the exact final rational endpoints, in
`scripts/heat/cubic-saved-moment-propagation-1917.json`. Its `selected_inputs`
copies every input digit, and `source_sha256` identifies the producer
artifact used. Reproduce this propagation only with

```text
python3 scripts/heat/cubic-saved-moment-propagation-1917.py
```

The complete rational H endpoints were inspected, not just their preview.
Rounding them outward to multiples of 10^(-22), using integer floor for
the lower endpoint and integer ceiling for the upper endpoint, gives
exactly [0.0000000000000070891180,0.0000000000000078529158]. The script
checks these rational inequalities directly. Thus H_box has a strictly
positive lower endpoint, meeting the required threshold lower(H_box)>0.
The inherited input contracts and finite inclusion argument then give
H>0 for the actual moments at zero. L021 gives gamma_0>0, so the already
audited identity H/gamma_0^4=4*(S_2^3-S_3^2), together with L027's
S_2,S_3>0, gives the stated strict ratio.

As a consistency check only, the script also encloses
4*G_0^4*(v^3-w^2) using b_j=G_j/G_0, v=b_1^2-b_2 and
w=(b_3-3*b_1*b_2+2*b_1^3)/2. The strictly positive G_0 box makes
these divisions legal. Its full interval overlaps H_box. Neither
intersection nor a midpoint is used to narrow the primary enclosure;
overlap is not its proof. The saved failure list is empty.

This is one saved-box test, with no new quadrature, mesh refinement,
parameter sweep, altered tail or Decimal exponential. The finite rational
propagation adds no new transcendental-library assumption. It does retain
the original L917/L037 assumptions; the separate audit1919 is below.
The strict-source defect1913 and all
downstream lower-residual, full-cost and uniformity gaps remain.

### Independent exact proof/code audit1919 — 20 November 2026

The primary enclosure and strict sign pass this audit under the accepted
L917/audit197 inclusion and L037's library contracts. This verifies
certificate1917; it does not add a strictness discovery beyond it or
repair the published proof. Pre-existing SPECIALIZE assessment1917,
separately approved1918, covers this finite audit. No new quadrature runs.

**Input identity.** L917 defines M_k(lambda) as the integral of
u^k exp(lambda*u^2)K(u), with precisely L019's kernel. At lambda=0 the
tilt is identically one, so these are L021's half-line moments, without
a limiting operation. Its accepted closed-panel inclusion covers the
left endpoint zero. The copied panel is exactly [0,1/5120]. All eight
selected decimal-string endpoints agree digit for digit with both the
original panel0 and audit197's reproduced panel0. The producer's source
hash equals audit197's saved source hash, and all six input hashes in
audit197 agree with current files. Thus the accepted inclusion applies
to exactly these data. This reuses its analytic proof and arithmetic
hypotheses; it does not verify Decimal or rerun finite integration.

**Complete finite replay.** The separate script imports neither the
producer nor its interval class. It independently specifies all 44 graph
records, including names, operations and operands, and compares this
entire graph with the saved trace. It parses the full input strings as
Fractions and evaluates every exact endpoint; all 44 saved pairs agree.
The factorial multipliers are precisely 1,1/2,1/12,1/120. Subtraction
uses lower minus upper and upper minus lower; multiplication checks
all four products; scaling orders the two products. The square branch
uses zero precisely when the operand contains zero, otherwise the
smaller endpoint square. These formulas give the exact range of each
operation on its interval or rectangle. Induction therefore includes
the desired H despite repeated dependent inputs. Addition is
endpointwise. Reciprocal division occurs only in the secondary expression;
the divisor check excludes zero and 1/x is decreasing on either permitted
interval, yielding [1/upper,1/lower]. The positive G_0 makes its uses legal.
A separate direct primary evaluation, with different multiplication
order, also agrees exactly. All secondary operations are replayed, but
overlap is only a consistency check and does not narrow the primary box.

**Strict endpoint and rendering.** For x=n/d, d>0, the integer grid
indices floor(10^22*n/d) and -floor(-10^22*n/d) give its downward and
upward multiples of 10^-22. The producer implements these by integer
division and renders the sign and full 22-place remainder without float.
Independent recomputation gives exactly [7.0891180,7.8529158]*10^-15,
with the outward inequalities checked against complete fractions.
The primary exact numerators and denominators are positive, so its
exact lower endpoint exceeds the required zero. No midpoint, status
flag or intersection is used for this inference. There are zero failed
checks and the producer artifact is unchanged. Run the separate audit:

```text
python3 scripts/heat/cubic-saved-moment-audit-1919.py
```

Its full selected inputs, hashes, all 44 rational trace endpoints, both
final rational intervals and failures are in
`scripts/heat/cubic-saved-moment-audit-1919.json`. The complete primary
and secondary endpoints and full hash-check list were inspected.
Ordinary Fraction/integer arithmetic and the inherited documented
Decimal implementation remain trusted; this is no independent library
verification or formal proof. Full matching Mathlib coverage is unchecked.

**Strictness.** With gamma_0=M_0>0, the audited identity and L027's
S_2,S_3>0 give 0<S_3/S_2^(3/2)<1, without actual-zero reality.
The separate downstream application is recorded in C028r; that theorem
is not an input to this strictness proof. Its application retains
L917/L037's contracts. There is no uniform location or scale,
lower-residual bound, full-cost estimate or H_d=o(d) here.
Source-gap1913, L917's H2 stop and the main RH gap remain unresolved.

## Mathlib

Full matching theorem not checked; availability is unknown. The proposed
strict analytic source input is qualified by audit1913. Certificate1917
is not formally verified; its L917/L037 assumptions remain explicit after
the successful audit1919. Finite coefficient algebra, interval inclusion and
the local source obstruction are written out. No absence claim is made; see the
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
