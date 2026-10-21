# L100 — Uniform upper certificate for the order-three-pole fibers

## Hypotheses

Use L099's instance and list dictionary: Q=65537, E=F_Q,
H=<19139> of order n=1024, F=F_(Q^28), k=64 and m>=1.
For a,b in E and c in E^*, N(a,b,c) counts the 67-subsets S of H
whose monic root product is aX²+bX+c modulo X³. Let
T=Q^28/2^128. The simultaneous-column, closed-ball convention is
[foundations/02](../foundations/02-pinned-list-model.md).

## Conclusion

Put C=binomial(1024,67), E_0=binomial(579,67), and

\[
 U=\frac{C}{1024Q^2}+(1-Q^{-2})E_0.
\]

For every a,b in E and c in H,

\[
 N(a,b,c)\le\lfloor U\rfloor<T,\qquad
 \frac{1571790}{10^9}<\frac U T<\frac{1571791}{10^9}<1.       \tag{1}
\]

For c outside H, N(a,b,c)=0 by L099. Consequently every center in
L099's family has an entire 67-agreement list below threshold, for
every tuple width m>=1. This excludes that family as a threshold-sized
unsafe-index-957 witness. It gives no arbitrary-center safety at 67 or
68 agreements, no exact maximum fiber and no boundary improvement.
The 955–957 bracket remains unchanged. This is a REPRODUCTION of the
assessed character/sieve tools with the subgroup specialization below;
no progress beyond the inspected sources' methods or novelty is claimed.
The separate critical proof audit below retains this family exclusion.

## Proof

**Imported inputs and the difference being proved.** Li and Wan,
*Distance Distribution in Reed-Solomon Codes*,
[arXiv:1806.00152v3](https://arxiv.org/html/1806.00152v3#S4),
2019-07-30, Section 4 Lemma 4.1, printed pp. 9–10, bounds the
degree-one monic sum of a nontrivial unit character modulo a monic
degree-d polynomial by (d-1)sqrt(Q), after extension by zero on
nonunits. Apply d=3; no squarefree-modulus hypothesis is required.
We do not use its separate even-character bound. Its complete proof,
including imprimitive characters, was inspected in the prior assessment.

Li and Wan, *Counting polynomial subset sums*,
[arXiv:1507.06329v1](https://arxiv.org/html/1507.06329v1#S2),
2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5, supply the
weighted distinct-coordinate sieve on arbitrary finite domains. The
Lemma 2.6 proof supplies its cycle exponential generating function.
These results are imported, without a sieve or character-bound reproof.
The [prior SPECIALIZE assessment](../drafts/literature/2026-10-20-order-three-pole-uniform-fiber-upper.md)
approves the restriction, exceptional-cycle and finite-threshold checks.
Neither source's full-field RS list theorem is being applied to H.

**The actual Fourier group.** Set R=E[X]/(X³) and G=R^*.
Each unit uniquely has the form c(1+uX+wX²), c in E^*.
Since 2 is invertible in E, the map

\[
 c(1+uX+wX^2)\longmapsto(c,u,v),\qquad v=w-u^2/2,
                                                               \tag{2}
\]

is an isomorphism from G to E^* times (E,+)². Indeed multiplication
sends u,u' to u+u' and w,w' to w+w'+uu', whose second logarithmic
coordinate is v+v'. Its inverse is c(1+uX+(v+u²/2)X²).
Let K be the inverse image of H under the constant-term map.
Thus K is H times (E,+)², of size D=nQ², and has index 64 in G.

For x in H, r_x=X-x modulo X³ belongs to K, because -1 is in H
by C012a. For a 67-subset S, its product of r_x is precisely the
residue of its monic root polynomial. Thus L099's label aX²+bX+c
with c in H is one specified element z of K, with coordinates
(c,b/c,a/c-(b/c)²/2). No surjectivity of the subset-product map is
assumed.

For completeness, all complex characters of K are

\[
 \chi(c,u,v)=\theta(c)\exp(2\pi i(\alpha u+\beta v)/Q),
 \quad\alpha,\beta\in E,\quad\theta\in\widehat H.       \tag{3}
\]

Here E is the prime field and its elements in the exponent are integer
residues modulo Q. The cyclic group H has n characters, so (3) gives
D distinct characters. The usual finite geometric sums in the three
coordinates prove their orthogonality: D^(-1) sum_chi chi(yz^(-1))
equals 1 for y=z and 0 otherwise. Define the unordered sum

\[
 W_\chi=\sum_{S\subset H,\ |S|=67}\prod_{x\in S}\chi(r_x).
\]

Orthogonality, with no list or tuple exponent, gives exactly

\[
 N(z)=D^{-1}\sum_{\chi\in\widehat K}\chi(z)^{-1}W_\chi.
                                                               \tag{4}
\]

The principal character contributes C/D.

**Extension and all restricted cycle sums.** First suppose
(alpha,beta)!=(0,0). Extend theta from H to E^*. Explicitly C012a
gives a generator t=3 of E^*, with h=t^64=19139 generating H.
If theta(h)=exp(2 pi i r/n), choose
theta_tilde(t)=exp(2 pi i r/(Q-1)). Formula (3) with this constant
character extends chi to a character chi_tilde of G.

The annihilator A of H in the character group of E^* has exactly 64
members: eta_l(t)=exp(2 pi i l/64), 0<=l<64. For y in E^*,
1_H(y)=64^(-1) sum_(eta in A) eta(y), by the geometric sum.
For each cycle length j=1,...,67 put
C_j(chi)=sum_(x in H) chi(r_x)^j. Since x in H iff -x in H,

\[
 C_j(\chi)=\frac1{64}\sum_{\eta\in A}\sum_{x\in E^*}
   (\widetilde\chi^{\,j}\cdot(\eta\circ\mathrm{ct}))(X-x).
                                                               \tag{5}
\]

Here ct is the constant-term homomorphism G to E^*, and the inner
character is extended by zero on nonunits. At x=0 its value on X is
zero, so adding x=0 makes the inner sum exactly the complete monic
degree-one sum required by Lemma 4.1. Every inner character is
nontrivial: on the additive factors its parameters are
(j alpha,j beta), nonzero because 1<=j<=67<Q. Twisting by eta changes
only the constant factor. Therefore Lemma 4.1 and (5) imply

\[
 |C_j(\chi)|\le 2\sqrt Q<513=:B\quad(1\le j\le67).    \tag{6}
\]

The strict rounding follows from 4Q=262148<263169=513².
The 64 terms and the factor 1/64 cancel in the upper bound; there is
no extra index factor. This verifies nontriviality after every power
and twist, including characters initially trivial on E^*.

**The constant-only exceptions are not bounded by (6).** When
(alpha,beta)=(0,0), chi=theta composed with ct. If theta has order d,
orthogonality on H gives C_j(chi)=0 unless d divides j, in which case
C_j(chi)=n. Indeed the summand is theta((-x)^j); when theta^j is
principal it is identically 1, including its minus sign. A nonprincipal
theta has order d=2^a for 1<=a<=10.

Apply the imported sieve to the symmetric product weight on H^67.
For a permutation sigma with c_j cycles of length j it gives

\[
 67!\,W_\chi=\sum_{\sigma\in S_{67}}(-1)^{67-\sum_jc_j}
                              \prod_{j=1}^{67}C_j(\chi)^{c_j}.
                                                               \tag{7}
\]

Each unordered subset has exactly 67! ordered presentations; variables
from distinct cycles are independently summed and are allowed to
coincide in a sieve term. For a nonprincipal constant-only character,
every potentially nonzero term would have all cycle lengths divisible
by d. It would force d to divide 67, impossible for d a positive even
power of two. Thus W_chi=0 for all n-1 such exceptions. This argument
includes orders greater than 67 and does not apply a nontrivial bound
to a principal character power.

**One absolute-sieve cap.** For the remaining n(Q²-1) characters,
(6), (7) and the imported cycle generating function give

\[
 |W_\chi|\le\frac1{67!}\sum_{\sigma\in S_{67}}B^{\#\mathrm{cycles}(\sigma)}
 =[t^{67}]\exp\left(B\sum_{j\ge1}\frac{t^j}{j}\right)
 =[t^{67}]\,(1-t)^{-B}=\binom{B+66}{67}=E_0.            \tag{8}
\]

The series is formal; only lengths at most 67 affect the coefficient.
The binomial is rising here, not binomial(B,67). Taking absolute
values only after keeping the exceptional characters exact, (4)
therefore yields

\[
 |N(z)-C/D|\le\frac{n(Q^2-1)}{D}E_0=(1-Q^{-2})E_0.    \tag{9}
\]

In particular N(z)<=U; integrality gives its floor. Empty fibers cause
no exception. For c outside H, L099 already proves emptiness.
Equation (9) is a justified uniform discrepancy bound, not an assumed
uniform distribution or a phase-aligned lower estimate.

**Exact threshold and RS consequence.** The cap in reduced form is

\[
 U=\frac{14426195933424467700072419659454573514564383200115189412792705476585199688197588087702772665848181058395}
          {4295098369}.
\]

The certificate verifies (1) by integer cross multiplication. With
U=A_U/d_U and T=Q^28/2^128, the positive exact safety margin is

\[
 Q^{28}d_U-2^{128}A_U
 =3118268909517042305655815753448246718669818625587637707248146912292458765508093702976318414710329418457693119936258469104997110404353312948092929>0.
\]

For the ratio interval it checks
1571790 Q^28 d_U < 10^9 2^128 A_U
< 1571791 Q^28 d_U. Thus the cap is strictly below the actual
ambient-field threshold, and the required test passes.

L099's entire-list converse applies over F and for every m>=1, so
the list at each of its centers has exactly N(a,b,c) elements; no
additional extension-field rows occur. This proves the family exclusion.
It says nothing about other centers, including independent pole families,
nor arbitrary-center lists. It does not alter the finite boundary.

**Verification.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/order_three_pole_uniform_upper.py`.
The full certificate is
`scripts/coefficient-fibers/order-three-pole-uniform-upper-results.json`.
All 234 checks pass: independent binomial reconstructions, complete
absolute and principal cycle coefficients through 67, every possible
exceptional order, exact threshold/ratio comparisons and all 56
small-field root products in the proper order-eight subgroup of F_17.
The small case checks normalized logarithmic coordinates, constant
fibers and extensions using integer residues, not floating phases.
The symbolic proof establishes the large-domain character bound;
small cases and arithmetic are not a replacement for it. The selected
full cap, sieve error, threshold and safety margin were inspected.

Additionally run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_order_three_pole_uniform_upper.py`.
All 214 independent arithmetic reconstruction checks pass, saved in
`scripts/coefficient-fibers/order-three-pole-uniform-upper-verification.json`.
This reconstructs the complete exceptional coefficients from
(1-t^d)^(1024/d), the absolute coefficients from products, all decisive
fixed values and every small residue from elementary symmetric sums.
For even d, the stated exceptional polynomial follows from the signed
cycle generating function with C_j=n if d divides j and zero otherwise:
its exponent is -(n/d) sum_(l>=1)t^(dl)/l.
These are arithmetic checks during construction, distinct from the
separate critical proof audit below.

**Separate critical audit (2026-10-20).** The proof and its hypotheses
are retained without a new bound or mathematical dependency. The
previously saved [audit assessment](../drafts/literature/2026-10-20-order-three-pole-uniform-upper-critical-audit.md)
supplies the inspected primary hypotheses and proof cases; no stronger
character theorem, squarefree-modulus assumption or full-field list
theorem is introduced.

First, the group in (4) really is K, not G: a unit c+bX+aX² has
coordinates (c,b/c,a/c-b²/(2c²)), and the inverse in (2) recovers all
three coefficients. Under multiplication the cross term in w cancels
the cross term in u²/2. Since Q is an odd prime, these two additive
coordinates have precisely Q² distinct characters. Together with the
1024 constant characters, they exhaust K's dual. Orthogonality therefore
has denominator 1024Q², even if the subset map has empty fibers. For
r_x, the coordinates are (-x,-x^(-1),-x^(-2)/2), so there is no sign
or inversion change between the subset-product class and the weight.

The constant-character extensions have indices r+ell*n in the cyclic
dual of E^*, for 0<=r<n and 0<=ell<64. Restriction multiplies the
index by 64 modulo Q-1 and gives precisely r on H. The annihilator
indices ell*n exhaust its 64 elements, so their average is exactly
the indicator of H. Its argument in (5) is the constant term -x,
which is in H exactly when x is, because -1 belongs to H. For every
1<=j<=67 and every twist, the additive pair is j(alpha,beta).
Multiplication by j is invertible in E, so this pair cannot vanish
when the original pair is nonzero. Constant twists cannot change it.
Thus all 64 complete sums for every such j satisfy the cited
nontrivial-character hypothesis. The extra monic polynomial X is a
nonunit modulo X³ and contributes zero. The 64 complete bounds are
averaged, giving 2 sqrt(Q), rather than multiplied by 64.

For the constant-only characters, order d occurs d/2 times for each
d=2,4,...,1024, accounting for all 1023 nonprincipal cases. When
d divides j the summand is identically 1, including the sign -x;
otherwise its sum over H is zero. Consequently a nonzero cycle term
would partition 67 into multiples of d, which is impossible. This
also treats orders above 67 and powers that become principal.
Equivalently, their signed generating polynomial is
(1-t^d)^(1024/d), whose coefficient at degree 67 is zero. None of these
exceptions uses (6). The sole principal character has coefficient
binomial(1024,67), not the rising coefficient used for absolute values.

The symmetric product weight satisfies exactly the hypotheses of the
imported weighted sieve. A permutation with c_j cycles produces the
product of C_j^(c_j); allowing different cycles to coincide is part of
that sieve term. Each unordered subset occurs 67! times in the ordered
distinct sum. After that division, the all-positive absolute coefficient
is binomial(513+67-1,67). There are n(Q²-1) bounded characters and
n-1 zero characters besides the principal one. Taking absolute values
in (4) therefore gives exactly (9), with coefficient 1-Q^(-2).
No Fourier phase or actual fiber uniformity is assumed.

The independent audit command is
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/audit_order_three_pole_uniform_upper.py`.
Its complete certificate is
`scripts/coefficient-fibers/order-three-pole-uniform-upper-critical-audit.json`.
All **6439 checks pass**, with no failures. It exhausts all constant
extension indices and all 4288 power/twist pairs, checking the additive
inverse multiplier for each power. Unsigned cycle-count polynomials
independently reconstruct both the signed principal and absolute
coefficients through degree 67, including the factorial normalization.
Every saved coefficient for all ten exceptional orders is reconstructed.
All 56 small-case records, including their complete logarithmic
coordinates and constant-fiber distribution, are checked by direct
elementary symmetric sums and sums of individual logarithmic jets.
These finite checks support the general symbolic arguments above.

Every fixed value in the constructor certificate and every decisive
value in the independent construction verifier is reconstructed exactly.
The full manuscript numerator, denominator and positive safety margin
agree. The two ratio-endpoint margins are respectively

```text
10^9*2^128*A_U - 1571790*Q^28*d_U
 = 322773039212255329226421758875772089424986786207377390921244641605272005433965467377292246656784538426241352258737637223128632819682822504842290 > 0;
1571791*Q^28*d_U - 10^9*2^128*A_U
 = 2800404850402677871497214728393220918640751575705117542946383460783485026093985559177019436992079574812784274193163017070017539029249556687223759 > 0.
```

The decisive values and these margins were inspected in full. They
establish U<T, not merely a decimal approximation or the weaker
floor comparison. Empty fibers and nonzero c outside H remain covered.
The family here requires c!=0; no additional c=0 center is silently
included.

Finally, L099's imported converse holds over the ambient extension:
X^67+aX²+bX+c-X³f_1 is monic of degree 67, so 67 agreement points
force it to equal their monic root product. It has no residual factor
or extra root. The other degree-at-most-63 rows each have 67 roots
and hence vanish. Thus the entire list, for every m>=1, is the same
scalar fiber. The threshold remains |F|/2^128, not |F|^m/2^128.
The audit retains only this family exclusion. Arbitrary centers,
67/68 safety, the 955–957 boundary and the ABF-model comparison remain
unresolved. This is critical validation of a known-method specialization,
not a new estimate or a claim of novelty.

## Mathlib

Full subgroup unit-character/sieve specialization and uniform fiber
cap: **not checked** in Mathlib. Supporting finite character
orthogonality, quotient units, the truncated logarithm, weighted sieve
and Dirichlet character bound: **not checked**. No absence is inferred.
The precise primary citations above provide the imported mathematical
tools. The pinned ArkLib definitions specify the list model only.
