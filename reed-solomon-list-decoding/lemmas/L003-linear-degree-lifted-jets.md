# L003 — Linear degree bounds for nonsingular lifted jets

## Hypotheses

Let K be a field of characteristic zero or characteristic p>d. Fix integers
0<=s<=d, D>=0, B>=1, a point alpha in K, and

\[
 Q\in K[Z,X,Y_0,\ldots,Y_s],\qquad
 \deg_Z Q,\deg_X Q\le D,\quad \deg_Y^{\rm tot}Q\le B.
\]

The initial variables u=(Z,c_0,...,c_s) are algebraically independent. Assume
the polynomial

\[
 H(u)=\frac{\partial Q}{\partial Y_s}(Z,\alpha,c_0,\ldots,c_s)
\]

is nonzero. All assertions about points are restricted to H(u)!=0. Put
A=D+B, a=d-s, and L=max(0,2a-1). Degree below means total degree in u.

Introduce independent Taylor coefficients c_0,...,c_d and define

\[
 S_i(U)=\sum_{j=i}^d\binom ji c_jU^{j-i},\qquad
 F_t=[U^t]Q(Z,\alpha+U,S_0(U),\ldots,S_s(U)).
 \tag{1}
\]

Thus S_i is the ith Hasse derivative of the polynomial whose expansion at
alpha is sum_j c_j U^j. This identity follows by expanding (U+T)^j.

## Conclusion

There are polynomials N_t in K[u], for 1<=t<=a, such that the unique solution
of F_1=...=F_a=0 over any initial point with H!=0 is

\[
 c_{s+t}=\frac{N_t}{H^{2t-1}},\qquad
 \deg N_t\le A(2t-1). \tag{2}
\]

The denominators here need not be reduced. All noninitial coefficients can
also be written with denominator H^L and numerators of degree at most A L.

Let F_t^* denote substitution of (2) in F_t. For every t>=0,

\[
 R_t:=H^{BL}F_t^*\in K[u],\qquad
 \deg R_t\le E:=A(1+BL). \tag{3}
\]

Zero polynomials satisfy these degree bounds. We have R_t=0 identically for
1<=t<=a and t>D+Bd. On H!=0 the lifted polynomial solves Q identically in X
if and only if all R_t for t=0 and a<t<=D+Bd vanish. In particular, the base
equation F_0=Q(Z,alpha,c_0,...,c_s)=0 must still be imposed.

For fixed B, the coordinate and residual degree bounds are O_B((D+B)(d+1)).
They establish a local algebraic input, not a bound on the cumulative degree
of a global solution cover or on any Reed–Solomon list.

The source passage reviewed is Fernando Granha Jeronimo,
[TR26-169, September 5, 2026, Lemmas 5.6–5.7, printed pp. 23–24](https://eccc.weizmann.ac.il/report/2026/169/download#page=23),
read September 25. It states a quadratic numerator/residual estimate.
The simultaneous accounting below gives the stronger linear estimate (2)–(3).
No novelty is claimed. The source's additional B<p and primitivity assumptions
belong to its global decomposition; this local statement instead assumes
H!=0 explicitly and does not verify that decomposition.

## Proof

**Structure of the coefficient equations.** In every term of F_t, the
Z-degree is at most D and the number of Taylor-coefficient factors, counted
with multiplicity, is at most B. A factor c_(s+h), h>0, coming from S_i has
U-exponent s+h-i>=h, because i<=s. The other U-exponents, including those
from alpha+U, are nonnegative. Thus if a term contains noninitial factors
c_(s+h_1),...,c_(s+h_v), then

\[
 \sum_{j=1}^v h_j\le t. \tag{4}
\]

In particular F_t involves no c_j with j>s+t. For 1<=t<=a, an occurrence
of c_(s+t) must come from S_s, occur only once, and consume all t units of
U-exponent. All other factors must be constant terms. Summing the choices
of the factor differentiated in Q gives exactly

\[
 F_t=b_tHc_{s+t}+G_t,\qquad b_t=\binom{s+t}{s}, \tag{5}
\]

where G_t uses only c_0,...,c_(s+t-1). The characteristic hypothesis makes
b_t nonzero: in positive characteristic all factorial arguments are at most
d<p. No derivative of Q in X or another Y_i contributes to the displayed
coefficient, since such a term would require a positive additional U-exponent.

Every monomial of G_t can be written

\[
 g(u)\prod_{j=1}^v c_{s+h_j},
 \quad 1\le h_j<t,\quad \deg g\le A,\quad v\le B.
 \tag{6}
\]

If v=1 then h_1<=t-1. If v>=2, (4) holds. The case v=0 is allowed, with
empty products and sums. Consequently

\[
 e:=\sum_j(2h_j-1)\le 2t-2 \tag{7}
\]

for every such term, including t=1, when there are no noninitial factors.
Also deg H<=D+B-1<=A.

**Simultaneous numerator and denominator induction.** Suppose (2) has
already been constructed for h<t; this is an empty assumption for t=1.
After substituting those coefficients, the term (6) becomes

\[
 \frac{g(u)\prod_j N_{h_j}(u)}{H^e}.
\]

Multiplying it by H^(2t-2) gives a polynomial by (7). Its degree is at most

\[
 A+\sum_j A(2h_j-1)+(2t-2-e)A=A(2t-1). \tag{8}
\]

The exponents used for denominator clearing are the unused portion of the
same budget e; they are not an additional full budget for each factor.
Summing over all terms of G_t and setting

\[
 N_t=-b_t^{-1}H^{2t-2}G_t^*
\]

therefore defines a polynomial satisfying (2). Equation (5) then vanishes
after setting c_(s+t)=N_t/H^(2t-1). This proves the induction, including the
base case t=1. At every point H!=0, the coefficient b_tH in (5) is nonzero,
so successive solution is unique. No use of F_0=0 was made in this argument.

For t<=a the exponent 2t-1 is at most L. Replacing N_t by
N_t H^(L-(2t-1)) gives the asserted common denominator H^L and degree at
most A L. When a=0 there are no lifted coordinates and L=0.

**All residual equations.** Fix any coefficient F_t, with no restriction
on its order. Each term has the form (6), now allowing 1<=h_j<=a. Hence
e=sum_j(2h_j-1)<=BL. After substitution and multiplication by H^(BL), its
degree is at most

\[
 A+\sum_j A(2h_j-1)+(BL-e)A=A(1+BL).
\]

This proves (3). It also covers terms with no noninitial factors and the
case a=0. This estimate does not assume that residual Taylor order is at
most a: it uses the at-most-B factors and the fixed largest coefficient c_d.

Before substitution, the U-degree in (1) is at most D+Bd, so F_t=0 for all
larger t. The recursively solved equations vanish in K[u,H^(-1)], hence
their R_t are zero polynomials because this ring contains K[u] injectively.
On H!=0, multiplying an equation by H^(BL) is reversible. Thus the indicated
finite family of residual equations is equivalent to vanishing of the
entire substituted polynomial, including its constant coefficient.
Translation X=alpha+U preserves polynomial identities, proving the claimed
description of solutions.

**Scope checks.** The closed zero set of the R_t may acquire extra points
on H=0. Nothing above identifies those points as solutions or controls
their components; the open condition must be retained when constructing a
graph or taking its closure. If d>=p, b_t can vanish and the recursion need
not determine a coefficient. If H is zero, this chart gives no information
about singular solutions. These are missing hypotheses or separate branches,
not consequences supplied by the degree estimate.

## Mathlib

Full strengthened statement (2)–(3): **not checked** in Mathlib. Supporting
Hasse-derivative identities, polynomial localization, and degree inequalities:
**not checked**. The directly linked Lemmas 5.6–5.7 are mathematical source
references for the triangular recurrence and a weaker bound; they are not a
claim of Mathlib coverage or a match for the strengthened linear estimate.
