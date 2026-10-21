# L017 — Cofactor-weighted energy and a sixth-moment upper cap

## Hypotheses

Use L015's instance Q=65537, E=F_Q, ambient F=F_{Q^28}, H of order
n=1024, message dimension k=64, and A=66 agreements. Centers have a
degree-exactly-67 scalar polynomial over E in their first row, with all
other rows zero, and interleaving width m>=1. Put tau=Q^28/2^128.
Use L016's unnormalized sums F_A(u), R(u), additive character psi and
moment-coordinate incidence count I(v), for u,v in E^3.

For j=1,...,A let

\[
 S_j(u)=\sum_{x\in H}\psi(j(u_1x+u_2x^2+u_3x^3)).
\]

Let J_3=sum_{v in E^3} I(v)^2. Let I_2 be the projection of I to
its first two coordinates, obtained by summing the third coordinate,
and put J_2=sum_{v in E^2} I_2(v)^2. These count ordered pairs of
subset/cofactor incidences with equal first three or first two moments,
respectively; repeated residual roots are included.

Write s(A,c) for the unsigned Stirling number of the first kind, counting
permutations of A elements with c cycles. Set w=770, r=769 and

\[
 e_1=n,\quad e_2=2n^2-n,\quad e_3=6n^3-9n^2+4n,\qquad
 (b_1,b_2,b_3)=(33,1448,80207),
\]

so sqrt(e_h)<b_h. Define

\[
 G=\frac r{A!}\sum_{c=1}^A s(A,c)w^{\max(0,c-3)}b_{\min(c,3)},
 \qquad C=\binom nA,\quad
 L_2=\frac{513(Q-1)}{Q^2}\binom{579}{66}.
\]

## Conclusion

The exact cofactor-weighted cubic energy is

\[
 \mathcal K=Q^{-3}\sum_{u_3\ne0}|F_A(u)R(u)|^2
             =J_3-J_2/Q\ge0.                         \tag{1}
\]

For every center v, the absolute cubic Fourier contribution is at most
sqrt((Q-1)K/Q). Consequently its entire list size satisfies

\[
 M(v)\le I(v)\le C/Q^2+L_2+\sqrt{(Q-1)\mathcal K/Q}
                \le C/Q^2+L_2+G=:U_{\rm energy}.     \tag{2}
\]

The effective cap has the exact rational comparisons

\[
 56.273<G/\tau<56.274,\qquad
 56.385<U_{\rm energy}/\tau<56.386.                  \tag{3}
\]

It improves the prior support cap, whose ratio exceeds 1050, but still
fails to certify this family below threshold. No unsafe list is supplied
and the full-code grid bound is unchanged. A sufficient, **unproved**
remaining estimate would be

\[
 \mathcal K\le\frac Q{Q-1}(\tau-C/Q^2-L_2)^2.         \tag{4}
\]

Its right side, relative to the bulk scale C^2/Q, lies between
2.208*10^{-13} and 2.209*10^{-13}. This is a requirement on the excess
collision energy, not a bound proved for that energy. The loss in the
proved cap occurs when the signed sieve is bounded by an L2 triangle
inequality. Equation (1) preserves that cancellation before this step.

## Proof

**Imported inputs and purpose of specialization.** The saved
[EXPLORE assessment](../drafts/literature/2026-10-04-correlated-cubic-cofactor-error.md)
approves precisely this weighted-energy test. Import finite-group
orthogonality, Parseval and Cauchy–Schwarz, with the normalization
specified in Tao's
[245C Notes 2 (2009-04-06)](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
Section 1 Exercises 14 and 16, Section 2 Lemma 17 and Corollary 22.
Import the weighted signed sieve from Li and Wan,
[Counting polynomial subset sums, arXiv:1507.06329v1](https://arxiv.org/pdf/1507.06329v1#page=5),
Theorem 2.1 and Corollary 2.2, printed p. 5.
L016 supplies its local Fourier normalization, the caps |S_j(u)|<770
and |R(u)|<769 for cubic u, and the quadratic contribution bound L_2.
L015 supplies M=I-66P_67, extension-field completeness, normalization of
all assessed centers, and the every-m transfer.

The local derivation checks the changed weighted norm, its projected
collision interpretation, low-moment normalization and finite constants.
It is REPRODUCTION of standard tools; it does not claim a result beyond
the checked literature or a new character-sum theorem. In particular the
sieve itself is cited, not reproved.

**Exact coupled energy.** From L016,

\[
 I(v)=Q^{-3}\sum_u\psi(-u\cdot v)F_A(u)R(u).
\]

Equivalently, I is convolution of the A-subset moment distribution with
the residual moment curve z maps to (z,z^2,z^3). Orthogonality with
unnormalized sums gives

\[
 \sum_{u\in E^3}|F_A(u)R(u)|^2=Q^3J_3.
\]

The Fourier transform of I_2 is exactly F_A(u_1,u_2,0)R(u_1,u_2,0).
Two-coordinate Parseval thus gives the restricted sum Q^2J_2.
Subtracting and dividing by Q^3 proves (1). This retains every cross
term of the signed sieve; no absolute cycle sum has yet been taken.
Since there are Q^2(Q-1) cubic parameters, Cauchy–Schwarz gives

\[
 \left|Q^{-3}\sum_{u_3\ne0}\psi(-u\cdot v)F_A(u)R(u)\right|
 \le\sqrt{(Q-1)\mathcal K/Q}.                        \tag{5}
\]

The trivial Fourier term is C/Q^2. The complete residual sum vanishes
for degree-one phases, and the quadratic part is bounded by L_2 as in
L016. L015's nonnegative subtraction 66P_67 may be dropped for this
upper test; I is not equated with the list. These facts prove the first
inequalities in (2), and (4) would suffice for family safety.

**Low moments of cycle sums.** For h=1,2,3, full three-coordinate
orthogonality gives

\[
 Q^{-3}\sum_{u\in E^3}|S_j(u)|^{2h}
 =|\{(x,y)\in H^h\times H^h:
                  \sum_i x_i^t=\sum_i y_i^t\ (t=1,2,3)\}|.
                                                               \tag{6}
\]

Here j!=0 in E, so multiplication by j permutes the character parameters.
For h<=3, Newton identities (2 and 3 are invertible) imply that the
ordered tuples on the right have the same multiset. Conversely equal
multisets have equal moments. For h=1 the count is n. For h=2, distinct
multisets contribute 4*binomial(n,2), and double roots contribute n,
giving e_2. For h=3, three distinct entries contribute 36*binomial(n,3),
a repeated entry and a distinct entry contribute 9n(n-1), and three
equal entries contribute n. The sum is e_3. These include repeated
coordinates, as the sieve's cycle variables require.

Define the restricted normalized norm

\[
 \|T\|_{2,\rm cub}^2=Q^{-3}\sum_{u_3\ne0}|T(u)|^2.
\]

For a permutation with c cycles of lengths j_1,...,j_c, its cofactor
term is R product_{i=1}^c S_{j_i}. If c<=3, Holder on c factors,
(6), and |R|<r yield

\[
 \left\|R\prod_{i=1}^c S_{j_i}\right\|_{2,\rm cub}
 \le r\left(Q^{-3}\sum_{u\in E^3}
                             \prod_{i=1}^c|S_{j_i}(u)|^2\right)^{1/2}
 \le r\sqrt{e_c}.
\]

If c>3, cap c-3 factors by w on the cubic set and apply Holder to the
remaining three factors, extending only those nonnegative sixth-moment
sums to all E^3. The resulting norm is at most r w^{c-3} sqrt(e_3).
No bound |S_j(0)|<=w is used: zero is excluded for the capped factors,
and the retained low moments include it exactly.

**Where the signed information is lost.** The imported sieve is

\[
 F_A(u)=\frac1{A!}\sum_{\sigma\in\mathfrak S_A}
       (-1)^{A-c(\sigma)}\prod_{\gamma\text{ cycle of }\sigma}
                                      S_{|\gamma|}(u).
\]

Apply the L2 triangle inequality only now, after multiplying by R and
restricting to cubic phases. The preceding norm bounds give

\[
 \sqrt{\mathcal K}\le\frac r{A!}\sum_{c=1}^A
     s(A,c)w^{\max(0,c-3)}\sqrt{e_{\min(c,3)}}<G.
\]

Equation (5) has prefactor sqrt((Q-1)/Q)<1; dropping it proves the
last inequality in (2). The distinction matters: the collision identity
is exact, but this effective estimate separates signed terms. Its failure
to reach threshold does not prove that exact K is large or that every
possible use of Parseval fails.

**Arithmetic and independent identity audit.** The recurrence
s(a,c)=s(a-1,c-1)+(a-1)s(a-1,c), with s(0,0)=1, computes the cycle
counts exactly. The identity sum_c s(A,c)w^c=A!*binomial(w+A-1,A)
checks that recurrence against the prior cycle polynomial. At n=1024,
(e_1,e_2,e_3)=(1024,2096128,6433017856); the displayed integer b_h
are strict square-root upper bounds. Rational arithmetic after clearing
denominators proves (3), positivity of the margin in (4), and the
relative threshold stated there. No large fiber is sampled or enumerated.

Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_cofactor_weighted_energy.py`.
Its saved output is
`scripts/coefficient-fibers/cofactor-weighted-energy-results.json`.
On the order-8 subgroup of F_17 with A=4, it independently enumerates
the ordered low-moment collisions, checks the signed group-ring sieve
and cofactor convolution, and computes J_2 and J_3. It then sums the
squared Fourier amplitudes over all cubic parameters in Z[zeta_17],
using the cyclotomic relation rather than floating-point arithmetic, and
checks Q^3J_3-Q^2J_2 exactly. This validates the projection subtraction,
factorial and energy normalization on that instance; it does not estimate
the fixed 1024-point collision counts.

## Mathlib

Full proper-subgroup weighted-energy threshold statement: **not checked**.
Supporting finite-group Parseval, Cauchy–Schwarz, Holder, Newton identities,
Stirling recurrence and character orthogonality: **not checked** in Mathlib.
The cited primary sources supply supporting results, rather than a full
matching theorem. The pinned ArkLib model definitions remain **present**
as recorded in foundations/; they define the list, not this upper cap.
