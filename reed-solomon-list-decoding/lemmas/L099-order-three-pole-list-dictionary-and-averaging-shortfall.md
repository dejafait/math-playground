# L099 — Order-three pole dictionary and class-averaging shortfall

## Hypotheses

Use C012a's instance: Q=65537, E=F_Q embedded in F=F_(Q^28),
H<=E^* of order n=1024, k=64, epsilon*=2^(-128), and m>=1.
Message rows belong to F[X] and have degree less than 64. Use the
closed simultaneous-column model in
[foundations/02](../foundations/02-pinned-list-model.md).
For a,b in E and c in E^*, define on H

\[
 Y_{a,b,c}(x)=((x^{67}+ax^2+bx+c)/x^3,0,\ldots,0).
\]

No received-word degree condition is imposed. For a 67-subset S of H,
put g_S(X)=product_(x in S)(X-x), and define

\[
 N(a,b,c)=|\{S\subset H:|S|=67,\quad
              g_S(X)\equiv aX^2+bX+c\pmod {X^3}\}|.
\]

## Conclusion

The entire list at Y_(a,b,c) with at least 67 simultaneous agreements
consists of the distinct evaluation tuples (f_S,0,...,0), for S counted
by N(a,b,c), where

\[
 f_S(X)=\frac{X^{67}+aX^2+bX+c-g_S(X)}{X^3}.       \tag{1}
\]

Each f_S belongs to E[X], has degree at most 63, and agrees exactly
on S. The list cardinality is N(a,b,c), independently of m. Nonempty
fibers have c in H; c outside H gives an empty list. With
T=65537^28/2^128, the finite class average gives

\[
 B_m(957/1024)\ge\max_{a,b\in E,c\in H}N(a,b,c)
       \ge L:=\left\lceil\frac{\binom{1024}{67}}
                                      {1024\cdot65537^2}\right\rceil,
 \qquad
 \frac{1571759}{10^9}\le\frac{L}{T}
                  <\frac{1571760}{10^9}<1.             \tag{2}
\]

This lower certificate does not certify unsafety at index 957. It gives
no upper bound on fibers or arbitrary-center lists, no safety conclusion,
and no change to the 955–957 bracket. The maximum fiber and a passing
witness remain unknown. This elementary specialization is REPRODUCTION,
not a claim of progress beyond the sources checked. The separate critical
proof audit below retains this statement and the averaging stop.

## Proof

**Known framework and applicability.** Gao,
[Asymptotic distributions of the number of zeros of random polynomials
in Hayes equivalence class over a finite field, arXiv:2203.06729v5](https://arxiv.org/html/2203.06729v5),
2024-01-07, definitions (1)–(2), (5)–(6), Section 3 Proposition 2,
and Theorem 3, (17)–(19), supply the arbitrary-domain class identity.
Take its field size q=65537, modulus Q_source=X^3, t=3, ell=0,
D=H, k_source=64 and j=67. The modulus is monic, D avoids its only
zero, and c!=0 ensures coprimality. Equation (17) has residual degree
zero, whose sole monic polynomial is 1; its W_67 is N(a,b,c).
Theorem 3 identifies the 67th binomial root moment with Q^(-64)N(a,b,c).
Since a degree-67 monic polynomial has at most 67 distinct roots, this
is its probability of 67 roots in H. Equations (5)–(6) give Q^64
degree-67 polynomials per class and (Q-1)Q^2 classes. These results
are imported without a generating-function reproof. Theorem 2 and
Proposition 3 require different domain/ell hypotheses and give no
quantitative estimate here.

The [prior SPECIALIZE assessment](../drafts/literature/2026-10-20-order-three-pole-67-agreements.md)
approves exactly this dictionary/averaging test. What remains is its
RS interpretation, extension completeness and smaller subgroup class
container. L019 is a comparison, not a premise. No character estimate
or uniformity is assumed.

**Signs and admissible classes.** Put P=product_(x in S)x,
u=sum_(x in S)x^(-1), v=sum_({x,y} subset S)(xy)^(-1). Factoring at zero,

\[
 g_S(X)=(-1)^{67}P\prod_{x\in S}(1-X/x)
       \equiv -P(1-uX+vX^2)\pmod {X^3}.
\]

Thus c=-P, b=Pu=-cu, a=-Pv=cv. These are in E, with P in H.
C012a gives a generator g with g^512=-1, so -1 is in H and c is in H.
For any nonzero c and a,b in E, c+bX+aX^2 is a distinct unit residue
modulo X^3, represented by the monic polynomial X^67+aX^2+bX+c.
The full Hayes class space has (Q-1)Q^2 elements. Our root products
land in the smaller container E^2 times H, of size nQ^2: the inverse
image of H under the constant-term homomorphism on (E[X]/(X^3))^*.
No claim of surjectivity of the 67-subset map or exact image size is
made. There are no extra prescribed leading coefficients or assumed
constraints on a,b.

**Division, strict degree and exact agreement.** For a subset in the
fiber, the numerator of (1) is zero modulo X^3, so its quotient is in
E[X]. Its degree-67 terms cancel, leaving degree at most 66 before
division and at most 63 afterwards, including the zero polynomial.
For x in H,

\[
 (x^{67}+ax^2+bx+c)/x^3-f_S(x)=g_S(x)/x^3.
\]

The denominator never vanishes on H. The right side vanishes exactly
at S, since g_S has precisely its 67 distinct linear factors. With
zero remaining rows, simultaneous agreement is exactly S, giving
distance 957/1024. For two different subsets in the same fiber, a
point of their symmetric difference is an agreement point for exactly
one tuple at this fixed center. Their evaluations are distinct. Lists
from different centers have not been combined.

**Entire-list converse over F.** Suppose a tuple (f_1,...,f_m) with
f_i in F[X] of degree at most 63 agrees on at least 67 columns. Then

\[
 G(X)=X^{67}+aX^2+bX+c-X^3f_1(X)
\]

is monic of degree 67, because deg(X^3f_1)<=66, and vanishes on all
agreement columns. L001's factor/root argument implies exactly 67
such columns, say S, and G=g_S: the monic degree-67 root product
divides G and has the same degree. Reduction modulo X^3 gives all
three required coefficients and forces c in H. Equation (1) then
forces f_1=f_S in E[X], even though it was allowed over F. Every
other row vanishes at those 67 points and has degree at most 63,
so it is zero. This proves completeness, descent and exact agreement
for every m without scalar projection or an exponent m. No extra
agreement or residual-factor correction occurs at this degree.

**Finite averaging and threshold failure.** The binomial(n,67)
subsets partition among the labels E^2 times H. Including any empty
fibers, their sizes sum exactly to binomial(n,67), so finite pigeonhole
counting proves (2)'s lower bound. No distributional approximation,
surjectivity or uniformity is needed.

The divisor is nQ^2=4398180729856. Exact integer division gives

```text
L = 3358693166267948129426257121648891065808354728156229705841256240561653258075795827260997640055.
```

With A=Q^28 and d=2^128, the saved certificate verifies

\[
 (L-1)nQ^2<\binom n{67}\le LnQ^2,
 \qquad
 1571759 A\le10^9dL<1571760 A.
\]

These integer inequalities prove the ceiling and ratio in (2), with
L<T strictly. Only this averaging certificate stops. An insufficient
lower bound cannot imply max N<=T. Independent arbitrary-center safety
at 67 or 68 agreements and the ABF/pinned-model comparison remain
unresolved. Stronger fiber estimates need separately assessed mechanisms.

**Verification and limitations.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/order_three_pole.py`.
The full values, exact margins, small-case lists and failures are in
`scripts/coefficient-fibers/order-three-pole-results.json`.
All 519 checks pass. Complete Pascal recursion and factorial-product
multiplication independently reconstruct the binomial. All load-bearing
fixed-instance certificate values were inspected in full, with comparisons
by integer cross multiplication rather than decimal approximations.

On the proper order-eight subgroup generated by 9 in F_17, take k=2
and five agreements. The script checks all 56 subsets, their three
ending coefficients, inverse-symmetric signs, quotient degrees and exact
supports. It then enumerates all 289 scalar messages at each of 58
centers: all 56 occupied centers, one empty admissible center and one
with c outside H. The complete lists match the dictionary, including
empty lists and distinctness. These finite checks support the algebra
and do not estimate large-domain fibers. Extension-field completeness
and arbitrary width rest on the symbolic converse, not enumeration.

**Separate critical audit (2026-10-20).** The complete proof above is
retained, with no changed hypotheses, new fiber estimate or new dependency.
The primary source's nonnegative ell permits ell=0; every element of H
avoids the modulus X^3, and c!=0 is exactly the coprimality condition.
The terminal j=67 term in (17) has monic residual 1. Equations (18)–(19)
include that term with factor Q^(-64); the root bound makes its binomial
moment an exact 67-root probability. The two quantitative source results
remain excluded. No limiting assertion is needed for this finite identity.

Independently, factoring at zero gives c=-P, b=-cu and a=cv. Nonzero
constant residues are units modulo X^3, and each pair (a,b) is free in
that unit space. Restricting c to H gives a container, not a statement
about which labels occur. Cancellation of coefficients 0,1,2 gives
division by X^3; cancellation of the monic degree-67 coefficient gives
degree at most 63. Equality to g_S forces exactly the 67 distinct roots
on H. For any ambient-field candidate, its monic degree-67 difference
has those same factors and hence equals g_S over F. This forces its
coefficients into E. Each other row has 67 roots and degree at most 63,
so is zero. This verifies the entire list for every m>=1, including
empty fibers, without assuming coefficient descent for arbitrary messages.
Distinct supports at this one center have distinct evaluations.

The independent checker
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/audit_order_three_pole.py`
reconstructs the binomial from factorials and checks every fixed value
in the original certificate. In addition to the full threshold and ratio
margins, it obtains the exact ceiling remainders

\[
 \binom{1024}{67}-(L-1)nQ^2=1503258448896>0,\qquad
 LnQ^2-\binom{1024}{67}=2894922280960\ge0.
\]

All decisive margins were inspected in full. Finite averaging uses all
nQ² labels including empty fibers. The positive exact shortfall
Q^28-2^128 L proves only failure of this lower certificate, not a
fiber upper bound. A maximum exceeding threshold is still possible.

For the small case, the independent reconstruction uses all elementary
symmetric coefficients e1,...,e5 of each five-subset. It checks
(a,b,c)=(-e3,e4,-e5) and f=-e2+e1 X via the whole polynomial identity
at all 17 field points. It separately enumerates all 289 messages at
each of the 58 saved centers by multiplying the agreement equation by
x³, without the constructor's root-product or inverse-evaluation code.
Every saved label, support and message agrees; all 56 occupied centers
and both empty tests are covered. All candidate supports have exactly
five points and distinct evaluations. The saved coverage count 519 and
empty failure list are also checked. All **1280 independent checks pass**;
the full reconstruction, check list and empty failures are in
`scripts/coefficient-fibers/order-three-pole-critical-audit.json`.
This finite audit supports the manuscript; the general extension and
tuple assertions follow from the root argument, not the small example.

## Mathlib

Full order-three-pole/list/threshold result and Hayes identity: **not
checked** in Mathlib. Supporting division, root bounds, subgroup closure,
pigeonhole and binomial coverage: **not checked**. The precise primary
citation supplies the known class framework, not a large subgroup fiber.
Pinned ArkLib definitions are **present** as recorded in foundations/02;
they specify the model rather than prove this specialization.
