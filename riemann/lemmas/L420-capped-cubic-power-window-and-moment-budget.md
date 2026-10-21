# Lemma 420: power-window localization and the capped-cubic moment budget

## Hypotheses

Use L418's actual critical triple X0=(f,f'/L,f''/L^2), rho=|X0|,
D=Delta, B=Bcal, ell=log H and E=H^(-1) integral_[H,2H]. All
derivatives are ordinary derivatives before division by L=log(2+t).
The full actual response, including curvature, stays fixed at t.
Let lambda>0 be independent of H, M=lambda ell^2 and

    w_lambda=min(1,rho/M), F_lambda=E[|DB| w_lambda].

Use the unconditional moment and physical bounds of L390/L406 and
the source theorem cited below. H tends to infinity through real values.
No RH, independence, response relocation or restricted-moment law is
assumed. L409's positive signed-cubic coefficient is denoted beta_*.

## Conclusion

For every fixed p in [3,4],

    E rho^p <= C_p ell^(p^2/4).                            (1)

For every fixed delta in (0,1/2], the two parts outside the window
ell^(2-delta)<rho<ell^(2+delta) satisfy

    E[|DB| w_lambda 1_(rho<=ell^(2-delta))]
                            =O_(lambda,delta)(ell^(2-delta^2)),
    E[|DB| w_lambda 1_(rho>=ell^(2+delta))]
                            =O_delta(ell^(2-delta)).       (2)

Thus F_lambda differs from its restriction to that window by o(ell^2).
These are upper bounds, not an assertion of concentration with respect
to unweighted height measure or of a nonzero window coefficient.

At the exact cap split rho=M, the separate magnitude-moment bound
on either part, for fixed p in [3,4], is

    C C_p lambda^(3-p) ell^(2+(4-p)^2/4).                 (3)

The exponent has minimum 2, attained only at p=4. In fact the direct
pointwise bound gives F_lambda<=C C_4 ell^2/lambda. Consequently
this fixed-moment certificate supplies neither o(ell^2) nor the exact
beta_* coefficient. This is a limitation of (1) and the displayed
magnitude inequalities, not a lower bound on F_lambda, a failure of
its asymptotic, or a general impossibility theorem for moment methods.

This REPRODUCTION application of the inspected moment theorem does
not complete L418/L419's scalar condition. It supplies no actual
clipping estimate, regulator margin, global realization or RH result.

## Proof

The preexisting EXPLORE assessment is
`drafts/literature/2026-10-16-capped-rare-cubic-asymptotic.md`.
This is its bounded radial-split/fixed-moment test, not a new source
review or a new derivative-moment theorem.

### Imported moments and physical majorant

Import M. J. Curran and A. Heycock, *Sharp bounds for joint moments
of the Riemann zeta function*,
[arXiv:2403.00902v1, Theorem 1.1, equation (2), and Section 4](https://arxiv.org/html/2403.00902v1).
For fixed n, 0<=k<=2, h_j>=0 and sum h_j<=k, its unconditional
upper bound is H(log H)^(k^2+2 sum j h_j) for the integral of
|zeta|^(2k-2 sum h_j) product |zeta^(j)|^(2h_j).
Take n=2, k=p/2 in [3/2,2], and either all h_j=0 or the single
nonzero h_j=k for j=1 or 2. These choices are in the stated range,
including p=4. Equality sum h_j=k is permitted; no inverse power of
zeta occurs. On the sharp interval this gives, for j=0,1,2,

    E |zeta^(j)(1/2+it)/L^j|^p <= C_(p,j) ell^(p^2/4).

The factors L^(-jp)<=ell^(-jp) remove the source's derivative powers.
L406 (4)--(5) gives the exact ordinary-jet comparison with these three
complex derivatives, including the gamma phase derivative and its
second derivative. A fixed finite-dimensional norm inequality then
proves (1). The source theorem is imported, not reproved; this
specialization extends L406's p=3 application only to the fixed
parameters needed for the cap test. L390 also supplies its p=4 bound.
No assertion of uniformity as p varies with H is made.

L406 (6)--(7), equivalently L418's exact physical polynomial bounds,
gives |DB|<=C rho^3, with a constant independent of H. It contains
the entire response and both curvature contributions. All following
inequalities therefore concern the actual DB itself. If a leading
polynomial replacement is desired, the absolute-value contraction
and 0<=w_lambda<=1 give directly from L406

    |F_lambda-E[|d B0| w_lambda]|
        <=E|DB-d B0|=O(ell^(5/4))=o(ell^2).              (4)

The radial multiplier in (4) remains the original actual rho; it is
never factored from an expectation or replaced by an independent one.

### Both radial regions and the optimum fixed exponent

The exact split, assigning rho=M to the lower part, is

    F_lambda=M^(-1) E[rho |DB| 1_(rho<=M)]
                         +E[|DB| 1_(rho>M)].            (5)

For 3<=p<=4, on the first region rho^4<=M^(4-p)rho^p,
whereas on the second rho^3<=M^(3-p)rho^p. Thus each term of
(5) is at most C M^(3-p) E rho^p. Substitution of (1) and
M=lambda ell^2 gives (3), since

    p^2/4+2(3-p)=2+(4-p)^2/4.

For p<4 the exponent is strictly above 2; at p=4 it is exactly 2
with an unspecified constant. Using different fixed orders in the two
regions does not change either minimum. The p=4 estimate can be
applied without doubling its constant: pointwise
rho^3 min(1,rho/M)<=rho^4/M. This yields the stated total bound.
A fixed finite Holder interpolation of (1) cannot improve these
exponents: its exponent is a convex combination of q^2/4 at the
interpolated orders q, at least p^2/4 by convexity. This assertion
concerns those upper-bound certificates only.

Neither (3) nor a limit lambda->infinity supplies the required
fixed-lambda equality. In particular, the unspecified upper constant
cannot be equated to beta_*. L409 evaluates E(DB), not either term
in (5); its signed result does not remove the cap or absolute value.

### Localization on the logarithmic power scale

Fix delta in (0,1/2], set a=ell^(2-delta), b=ell^(2+delta), and
take p=4-2delta in [3,4). For fixed lambda, eventually a<M<b.
On rho<=a, (5)'s lower integrand and the majorant give

    E[|DB| w_lambda 1_(rho<=a)]
      <= C M^(-1) a^(4-p) E rho^p
      <= C_(lambda,delta)
              ell^(-2+(2-delta)(2delta)+(4-2delta)^2/4)
       = C_(lambda,delta) ell^(2-delta^2).

On rho>=b the cap is one, and rho^3<=rho^4/b, so L390's fourth
moment gives the second bound in (2). The strict middle window and
these two closed outer regions partition the domain; no assumption
about the measure of equality level sets is needed. Dividing the two
bounds by ell^2 proves the claimed o(ell^2) error for every fixed
delta and all sufficiently large real H. Each delta and lambda is
fixed before taking H to infinity; no diagonal limit is invoked.

The unresolved response-correlated middle-window mass includes the
cap transition itself. Its fourth-moment upper bound still permits
the full ell^2 scale. This explains why discarding the outer regions
does not evaluate a coefficient, prove convergence, or reject the
existence of a suitable fixed lambda. The bounded test stops here.

## Mathlib

Full matching coverage of the derivative-moment theorem and this
restricted physical observable has not been checked. Elementary
integral monotonicity and finite Holder inequalities support the
calculation but are not substitutes for that theorem or a capped
asymptotic. No formal verification or absence claim is made. The
exponent identities and inequalities above are exact; no numerical
certificate or mathematical script is used.
