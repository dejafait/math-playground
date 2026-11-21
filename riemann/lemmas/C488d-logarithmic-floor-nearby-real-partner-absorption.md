# Corollary 488d: logarithmic-floor nearby real-partner absorption

## Hypotheses

Use the actual theta family H_t in C488a and C488c, with
H_0(z)=xi((1+iz)/2)/8. Fix any real a, any real R>=200 and
0<=t<=1/5. Every zero sum counts multiplicity. Define

    s(x)=sqrt(x^2+R^2), L(x)=log(2+s(x)),
    w(x)=exp(-sqrt(1+((x-a)/R)^2)),
    eta(x)=1/(1000 L(x)), p(x)=w(x)eta(x).

The derivative p' is with respect to x, with a and R fixed.
Let z_j=x_j+i y_j be any nonreal zero copy of H_t, so y_j!=0.
No simplicity, separation, positive minimum |y_j|, RH, or restriction
on a is assumed. Retain the closed cutoff |x_k-x_j|<=R.

## Conclusion

The nearby real-partner count contribution satisfies

    sum_(k: y_k=0, |x_k-x_j|<=R)
       2(x_j-x_k)p'(x_j)/((x_j-x_k)^2+y_j^2)
       <= (3/25) w(x_j)/|y_j|
       < w(x_j)/(2|y_j|).                                  (1)

In fact the sum of the absolute values of these summands satisfies
the same non-strict upper bound. In the central regime |x_j|<2R
the coefficient 3/25 can be replaced by 93/12500.

Thus this modified floor retains C488a(7)'s half-loss absorption,
uniformly on the entire stated domain. This is a quantitative
specialization of the known nearby mixed-pair argument. It pays only
this particular p' cost. It is not a total transport inequality,
all-height reality statement, or actual-Xi mixed positivity result.

## Proof

### Imported count inputs and scope

Use the two established, time-uniform bounds with their actual domains:

    #{k: |x_k|<=u}<=(u+20)log(4u+40), u>=0,                (2)
    #{k: |x_k-x|<=r}<=100r log(2+|x|), |x|>=2r>=400.      (3)

Equation (2) is C488a(4), whose count proof holds for every u>=0
and 0<=t<=1/5 independently of the finite-head center and scale
used elsewhere in that corollary. Equation (3) is C488c(2), including
its conceptual audit2115 and C488b counting reduction. Both bounds
count all complex zero copies in closed windows, not only real zeros.
They therefore also upper-bound the real-partner subcount below.
Neither is a difference of two global upper counts.

The source mechanism is bramble_trace, *An unsigned strip bound for
the de Bruijn--Newman constant*, rStation paper186, v1,
20 November2026, [Appendix B, nearby mixed-pair and own-conjugate
cases, (B.1)-(B.4)](https://rstation.ai/problems/riemann_hypothesis/papers/186),
as audited in C488a. The local-count input specializes D. H. J.
Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function, and a new upper bound for the de Bruijn--Newman
constant*, Research in the Mathematical Sciences 6 (2019), article31,
[arXiv1904.12438v2, Section9/(105), Proposition9.1(ii), and the
effective inputs specified in C488c](https://arxiv.org/html/1904.12438v2).
Its qualitative O constant is not assigned the numerical value100
by citation alone; the numerical specialization and closed time
endpoint are precisely those proved in C488c.

The calculation below is needed because these sources and C488a(7)
do not state this changed floor or arbitrary a and R. No new count
theorem is reproved here. The prior source assessment is
`drafts/literature/2026-11-21-local-count-absorption-review-2115.md`.

### Derivative of the changed floor

Put v=(x-a)/R. For every real x,

    w'(x)/w(x)=-v/(R sqrt(1+v^2)), |w'(x)|<=w(x)/R,
    s'(x)=x/s(x), L'(x)=x/[s(x)(2+s(x))].                 (4)

As s(x)>=R and |x|<=s(x), |L'(x)|<=1/(2+s(x))<=1/R.
Also L(x)>=log(202)>5. For an exact elementary justification of the
last comparison, C488a's scalar proof gives e<11/4 and
11^5=161051<206848=202*4^5; hence e^5<202.
Differentiation now gives

    p'=w'/(1000L)-w L'/(1000L^2),
    |p'|<=w/(1000RL)(1+1/L)
          <=(6/5)w/(1000RL).                             (5)

These bounds are independent of a. They retain the derivative of
the logarithmic denominator; it has not been dropped.

### Paying the count in the two spatial regimes

Write x=x_j, Y=|y_j|>0, and let M count the real copies in the
closed interval [x-R,x+R]. The count is finite by (2).

If |x|>=2R, (3) with r=R applies, including equality at |x|=2R.
Since |x|<=s(x), it gives

    M<=100R log(2+|x|)<=100R L(x).

Together with (5), this yields

    M |p'(x)| <= (3/25)w(x).                             (6)

If |x|<2R, every counted partner has |x_k|<=|x|+R<3R.
Using the larger closed global window in (2) gives

    M<=(3R+20)log(12R+40).

For every real R>=200, 20<=R/10, and

    (R+2)^2-(12R+40)=R(R-8)-36>=200*192-36>0.

Therefore log(12R+40)<=2log(R+2)<=2L(x), and

    M <= (31/5)R L(x),
    M |p'(x)| <= (93/12500)w(x) <= (3/25)w(x).            (7)

Equations (6)-(7) cover every real x without an uncounted boundary.
They use the local count only in its allowed regime. The central
payment uses no off-center count assumption.

### The mixed kernel and qualifications

For each counted real partner put d=x-x_k. The elementary square
(|d|-Y)^2>=0 gives

    2|d|Y<=d^2+Y^2,
    |2d p'(x)/(d^2+Y^2)|<=|p'(x)|/Y.                    (8)

The denominator is nonzero even at d=0. Summing this finite
inequality over the M real copies and invoking (6) or (7) proves
the absolute-value bound and hence (1), since 3/25<1/2 and w/Y>0.
Every multiplicity is already included in M. No limiting passage as
Y tends to zero is used: (8) holds for every Y>0 with the same
coefficient. The endpoint t=0 follows directly from (2)-(3), rather
than from continuity of a sharp zero count.

At a simple selected zero and a regular time the expression in (1)
is the nearby real-partner contribution to the derivative of p(x_j)
under the velocity law reproduced in C488a. Its reserved own-conjugate
linear-height loss is -w(x_j)/Y, so (1) uses less than half that loss.
At a multiple selected zero this proof asserts only the displayed
static finite-sum bound; it supplies no velocity for individual
colliding copies. A later transport theorem must justify regular-time
summation and collision passage separately for the changed statistic.

Other p-derivative terms, nonreal pairs, distant tails, summability,
initial mass and all-height overlap are outside this proof. The
whole-plane moving-supremum obstruction and the main mixed-sign gap
are not removed. No computation or sampled-zero evidence is used.

### Independent audit — 21 November2026, step2118

The stated inequality passes an independent analytic replay under the
unchanged SPECIALIZE assessment. C488a(4) was checked in its count
proof, independently of that corollary's fixed finite-head parameters;
its variable u is an arbitrary nonnegative window radius. C488c(2)
and the completed C488b/C488c audit supply exactly the closed local
window, time endpoint and all-copy count needed in (3). Their existing
proofs are reused as inputs, not new count assertions in this audit.
The H_t normalization agrees with C488a and L058 throughout.

Direct differentiation of log p gives

    p'/p = -v/(R sqrt(1+v^2)) - x/[s(2+s)L].

Here s>=R>=200 and |x|<=s. Consequently each term is bounded
respectively by 1/R and 1/(RL), proving (5) with L>5.
The exact comparison 161051<206848 verifies e^5<202 from the
cited e<11/4 bound. No a-dependent bound is required.

The off-center multiplication is exactly
100*(6/5)/1000=3/25. Centrally, 3R+20<=(31/10)R and
12R+40<(R+2)^2, so (2) gives M<=(31/5)RL; the corresponding
coefficient is (31/5)*(6/5)/1000=93/12500. The split assigns
|x|=2R to (3), where 2R>=400; R=200 is included. Both count
inputs already include partners on the endpoints and every repeated
real copy. The sum is finite, and termwise (8) is valid also at
d=0 for every Y>0. Thus the signed sum is bounded by its absolute
sum, with no cancellation premise, limit interchange or lower Y.
Strict half-loss follows from 3/25<1/2 and w/Y>0.

The count input is valid at t=0 directly. The final velocity
interpretation requires the stated simple selected zero and regular
time; neither this audit nor the static inequality differentiates a
multiple selected copy. No extra mathematical input, altered bound,
or changed DAG edge is needed. This verifies a local reproduction of
the checked source mechanism, with all other transport and mixed-sign
obligations still open; it is not an advance beyond those sources.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
No Mathlib declaration is invoked for the actual heat-family counts.
The supporting operations are real differentiation, monotonicity of
logarithm, a quadratic square inequality and finite sums. The analytic
counts remain the precise canonical inputs (2)-(3).
