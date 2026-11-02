# Lemma 581: the full corrected law fails quartic stationarity

## Hypotheses

Use exactly L473's law nu_H, for real H sufficiently large, with
ell=log H held fixed, coordinate order
v=(x_0,y_0,z_0,x_1,y_1,z_1), and all its actual-Hardy inputs.
In particular retain its unnormalized rare measure eta_H, mass
p_H=W_H ell^(-4), w_H=1-p_H, covariance contribution R_H,
noncommuting correction A_H, and fixed bounded random vector B.
Thus, in the notation of L473 (14)--(18),

    nu_H=eta_H+w_H Law(sqrt(ell/w_H) A_H B),
    W_H<=W_*, w_H>=1/2, |B|<=M_0,
    ||A_H-I||<=C_A/ell, ||A_H||<=2.                         (1)

The constants W_*, M_0, C_A are fixed on one eventual ray of real H.
All matrix norms are Euclidean operator norms. Import the fixed-order
pointwise bound for the ordinary Hardy derivatives

    |Z^(k)(t)| <= C_k T^(1/6), k=0,1, t of order T,          (2)

from H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
Z(t)*, Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1, printed p. 1](https://arxiv.org/pdf/2304.05178v1#page=1),
Introduction immediately before (1). This is the inspected fixed-k
statement, not a bound uniform in derivative order. Only the two
positive endpoints H and 2H and k=0,1 are used. The bound's arithmetic
proof and L473's moment-source proofs remain imported, not audited here.
No RH, simplicity, stationarity of dyadic sampling, limit law or
process realization is assumed.

## Conclusion

For the homogeneous polynomial

    P(v)=x_0^3 z_0+3x_0^2 y_0^2,

the exact full-law defect satisfies

    D_H := integral P(v) dnu_H(v)
      = [Z(t)^3 Z'(t)]_H^(2H)/(H ell^2)
          +(ell^2/w_H) E P(A_H B),                          (3)
    D_H=ell^2/6+O(ell),
    lim_(H->infinity) D_H/ell^2=1/6.                        (4)

In particular D_H>=ell^2/12 on an eventual ray. For every H on that
ray there is no translation-invariant Borel probability law on
C2(R;R) whose ordinary jets at 0 and 1 have joint law nu_H. Already
the first jet marginal is impossible for such a stationary law.
This excludes this exact corrected construction, not general stationary
feasibility, nonstationary realization, a derivative-preserving
replacement, actual-Hardy clipped mass or an RH statement. The onset
is existential; no numerical height is certified.

## Proof

### Exact rare quartics and fixed-divisor boundary identity

L473 (14) retains every actual fourth monomial exactly. Since P is a
linear combination of two such monomials, with
Y_(0,j)(t)=Z^(j)(t)/ell^j, it follows without an asymptotic expansion that

    integral P deta_H
      =H^(-1) integral_H^(2H) P(Y(t)) dt
      =(H ell^2)^(-1) integral_H^(2H)
             [Z(t)^3 Z''(t)+3Z(t)^2 Z'(t)^2] dt
      =[Z(t)^3 Z'(t)]_H^(2H)/(H ell^2).                    (5)

This is the deterministic chain rule and fundamental theorem of
calculus in the transport specialization used in L580. Explicitly,
put f_H(s)=Z(H+s/ell), 0<=s<=H ell. Its ordinary derivatives are
f_H'(s)=Z'(H+s/ell)/ell and
f_H''(s)=Z''(H+s/ell)/ell^2. Thus

    (f_H^3 f_H')'=P(f_H,f_H',f_H''),
    (H ell)^(-1) integral_0^(H ell) P(f_H,f_H',f_H'') ds
      =[f_H^3 f_H']_0^(H ell)/(H ell).

Changing variables gives (5), including its additional factor 1/ell
in the boundary derivative. The actual Hardy function is smooth on
this compact interval. Every integral here is a finite ordinary
integral; neither random-path Fubini nor differentiation of ell is
involved. Both boundary values remain present.

At each endpoint t=H,2H, apply (2) with height parameter T=t.
Consequently |Z(t)^3 Z'(t)|<=C_0^3 C_1 t^(2/3). For a fixed
C_end=(1+2^(2/3))C_0^3 C_1, enlarged if necessary to have a common
onset, (5) implies the explicit absolute error bound

    |integral P deta_H|<=C_end H^(-1/3)ell^(-2).             (6)

No claim is made that each rare fourth moment is small. Their signed
combination is controlled by the exact boundary identity, not by
their O(ell^4) leading asymptotics or by the small mass p_H.

### The full covariance correction

For vectors u,v in R^6 let R=max{|u|,|v|}. The telescoping product
identity for four real factors gives

    |u_x^3 u_z-v_x^3 v_z|<=4R^3|u-v|,
    |u_x^2 u_y^2-v_x^2 v_y^2|<=4R^3|u-v|.

Indeed expand the difference by replacing one occurrence at a time;
each of the four summands has three coordinate factors of absolute
value at most R and one coordinate difference at most |u-v|.
After including the coefficient 3 in P, this proves

    |P(u)-P(v)|<=16R^3|u-v|.                               (7)

Use u=A_H B and v=B in (7). From (1), R<=2M_0 and
|u-v|<=C_A M_0/ell. Hence, for C_P=128 C_A M_0^4,

    |E P(A_H B)-E P(B)|<=C_P/ell.                         (8)

This estimates the actual six-coordinate matrix correction, even if
it mixes the two jets. It uses its operator norm bound only; R_H
and K need not commute and the correction need not preserve jet
dynamics. L580's exact first-marginal computation gives E P(B)=1/6.
Thus write E P(A_H B)=1/6+e_H with |e_H|<=C_P/ell.

The bulk measure has mass w_H, so fourth homogeneity gives exactly

    integral P d(w_H Law(sqrt(ell/w_H) A_H B))
      =(ell^2/w_H)(1/6+e_H).                              (9)

Adding (5) proves (3), retaining both components and their masses.
Since 1-w_H=p_H<=W_*ell^(-4) and w_H>=1/2,

    |1/w_H-1|=p_H/w_H<=2W_*ell^(-4).

Equations (6), (8) and (9) therefore give a quantitative full error:

    |D_H-ell^2/6|
      <=2C_P ell+(W_*/3)ell^(-2)
                       +C_end H^(-1/3)ell^(-2).           (10)

All constants are independent of real H beyond a common onset.
Dividing by ell^2 proves (4): the three error ratios are at most
2C_P/ell, W_*/(3ell^4), and
C_end H^(-1/3)ell^(-4), each tending to zero. They are eventually
at most 1/12 in sum, so D_H>=ell^2/12 there. This also explains
why L473's permitted O(ell^3) fourth-moment tolerance can conceal
this order-ell^2 stationary defect.

### Stationarity implication and limits

Fix any H on that eventual ray. L473 gives compact support
|v|<=ell^2 for nu_H. A hypothetical stationary Borel C2 path law
with this first jet marginal therefore has finite fourth moments
of its value, first derivative and second derivative at zero.
L580's finite-fourth stationary identity applies with precisely
these ordinary derivatives and requires E P=0. Equation (4), or
the eventual lower bound above, contradicts it. Prescribing both
jets would prescribe this first marginal and is equally impossible.
There is no additional height-uniform moment requirement on the
hypothetical process: the contradiction holds separately for each H.

This is a specialization of the known transport identity with the
already constructed local law. It is a new local comparison, not
a claim of progress beyond known arithmetic or transport theorems.
There is no complete RH candidate. General corrected laws, other
fourth-moment perturbations, stationary constructions with different
marginals, actual-Hardy clipped mass and actual-Xi positivity remain
unresolved. The independent application audit below verifies the
stated conclusion without enlarging these hypotheses.

### Independent application audit, 31 October 2026

This replay uses the separately approved SPECIALIZE assessment
`drafts/literature/2026-10-31-l581-critical-audit-scope.md`. The
arithmetic and transport sources retain their imported status; this
audits their application, not their proofs. No repair is needed.

**Rare measure and endpoint factors.** Directly from L473's measure
definition, a homogeneous quartic M receives the factor
ell^(-4) ell^8/(H ell^4)=1/H times its actual Y monomial.
The zero-radius convention contributes nothing. For this P both
monomials have derivative-divisor ell^2, giving precisely (5).
Independently, s=ell(t-H) gives ds=ell dt, an interval of length
H ell, and f_H'=Z'/ell. Its boundary quotient is therefore
[Z^3 Z'/ell]/(H ell), again (5). In particular the derivative
does not act on ell. The imported bounds at t=H and t=2H give
the absolute numerator bound C_0^3 C_1(1+2^(2/3))H^(2/3).
Thus (6) holds for their difference without assuming a cancellation
or discarding either endpoint. No other actual fourth moment needs
an absolute smallness estimate here.

**Full correction and marginal arithmetic.** Writing S_H=(I-E_H)^(1/2),
the transpose in A_H K A_H^T gives K^(1/2) S_H^2 K^(1/2),
not an interchange of K and R_H. For spectrum(E_H) in [0,1/2],
||S_H-I||<=||E_H||, so the exact L473 C_A bound and eventually
||A_H||<=2 apply to every coordinate, including jet-mixing terms.
For each quartic monomial four single-factor replacements bound its
difference by 4R^3|u-v|. The coefficients 1 and 3 in P give 16,
and R<=2M_0 then gives exactly 128 C_A M_0^4/ell in (8).
The first marginal remains (epsilon,v,k epsilon) before correction;
its polynomial is k+3v^2. Recomputing E k=1/72-7/72=-1/12
and E v^2=2(1/4)(1/6)=1/12 gives 1/6. No property of the
second marginal or independence after correction is used.

**Mixture and a single eventual ray.** The bulk's fourth multiplier
is w_H (sqrt(ell/w_H))^4=ell^2/w_H, whereas eta_H is already
unnormalized. Subtracting ell^2/6 leaves the perturbation cost at
most 2 C_P ell and the mass cost at most (W_*/3)ell^(-2).
Adding the absolute rare bound reproduces all three terms of (10).
After the common source/construction onset and ell>=1, sufficient
additional conditions for their normalized sum to be at most 1/12 are

    ell>=72 C_P, ell^4>=12 W_*,
    H^(1/3)ell^4>=36 C_end.

Each makes its corresponding normalized error at most 1/36. All
three hold on one eventual ray of real H; none requires a subsequence
or an effective arithmetic onset. This checks both the normalized
limit and the eventual ell^2/12 lower bound.

**Stationary implication.** Fix H separately. The support |v|<=ell^2
gives fourth moments at most ell^8 for each of the three first-jet
coordinates. Translation on C2 commutes with ordinary differentiation,
so stationarity transfers these moments to every time. Joint derivative
evaluation is continuous, hence the integrands in L580 are measurable.
Its Young bounds make the endpoints integrable and give a finite
time integral of the expected absolute quartic integrand. Thus Fubini
is applicable; the equal endpoint expectations and constant expected
integrand force E P=0. This contradicts the checked lower bound for
this fixed H. Constants for a hypothetical process need not be uniform
as H varies. The actual dyadic Hardy path is nowhere asserted stationary.

The conclusion, qualifications and direct mathematical inputs are
unchanged. This verifies a local specialization already stated here,
not a stronger arithmetic theorem or a general realization obstruction.

## Mathlib

Full matching coverage of this law, Hardy derivative input and
stationary obstruction has not been checked. L580 supplies the
previously justified stationary expectation/Fubini argument; the
finite-interval chain rule, fundamental theorem and explicit
polynomial/matrix estimates above supply this specialization.
No matching Mathlib theorem or absence claim is asserted.
