# Lemma 472: complete second and fourth Hardy-jet moments permit positive clipped mass

## Hypotheses

For real H>1 put ell=log H. The actual ordinary Hardy jet on [H,2H]
is X_H(t)=(Z(t),Z'(t)/ell,Z''(t)/ell^2), with the divisor fixed
throughout this interval. An abstract state is (x,y,z) in R^3. Write
Q(x,y,z)=(xz-y^2)_+ and require exactly the following raw second
moments, with constants uniform for all sufficiently large real H:

    E x^2=ell+O(1), E xz=-ell/12+O(1),
    E y^2=ell/12+O(1), E z^2=ell/80+O(1),
    E xy=O(H^(-2/3)ell^(-1)),
    E yz=O(H^(-2/3)ell^(-3)).                         (1)

For each nonnegative (a,b,c) with a+b+c=4 also require

    E x^a y^b z^c=q_abc ell^4+O_abc(ell^3).            (2)

Here q_abc=h(j1,j2,j3,j4)/pi^2, where the sorted list j has a zeros,
b ones and c twos. The exact source coefficient h is specified below.
Thus (2) includes all fifteen monomials

    x^4, x^3 y, x^3 z, x^2 y^2, x^2 yz, x^2 z^2,
    xy^3, xy^2 z, xyz^2, xz^3, y^4, y^3 z, y^2 z^2, yz^3, z^4.

There are no imposed first or cubic moments, response variables,
prescribed constants in the even O(1) errors, exact lower quartic
coefficients, height marginal, or global analytic realization. No RH,
simplicity, hypothetical zero, or zero-free-region premise is assumed.
The existence assertion below imports the unconditional fixed-order
moment theorems and finite-measure atomic theorem cited in the proof.

## Conclusion

For every sufficiently large real H there is a probability law nu_H
on R^3 with at most 23 atoms satisfying (1) and (2) on that same law,
and in fact

    E_nu_H xy=E_nu_H yz=0,
    E_nu_H Q=ell/144+O(1)>=ell/288.                   (3)

All constants and one common onset can be chosen independently of H.
Every atom can be chosen in |(x,y,z)|<=ell^2. All stated observables
are absolutely integrable. The proof is an existence construction;
it does not give numerical atom locations or an effective onset.

Consequently the asymptotic data (1)--(2), with precisely their stated
errors and without further restrictions on the law, do not imply
E Q=o(ell). This is an abstract finite-moment obstruction, not an
actual-zeta law or a lower bound for actual negative first-sign mass.
It does not decide individual-height signs, higher/mixed positivity,
or RH. The separate critical application audit in Section 7 finds no
repair necessary; it does not independently audit the imported moment
theorems or the omitted proof of their Proposition 3.

## Proof

### 1. Imported moments and their exact scope

Import H. M. Bui and R. R. Hall, *On the derivatives of Hardy's
function Z(t)*, Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/html/2304.05178v1).
The second inputs are Introduction p. 1, equation (1) and the preceding
odd-order display. For fixed j,k with j+k=2s, |j-k|=2d they state

    J_jk(T)=integral_0^T Z^(j)(t) Z^(k)(t) dt
      =(-1)^d T Q_(2s+1)(log(T/(2pi)))/(4^s(2s+1))
          +O_(j,k)(T^(3/4)(log T)^(2s+1/2)),           (4)

where the polynomial Q_(2s+1) is monic. For odd j+k the preceding
display gives J_jk(T)=O_(j,k)(T^(1/3)). The dyadic difference divided
by H ell^(j+k) yields (1) for the actual jet. Indeed the leading term
for even j+k is (-1)^d ell/(4^s(2s+1)); lower polynomial terms cost
O(1), and the normalized analytic error is O(H^(-1/4)ell^(1/2))=O(1).
For odd j+k the same difference costs O(H^(-2/3)ell^(-(j+k))).
The four even coefficients are therefore 1,-1/12,1/12,1/80, and the
odd orders are 1 and 3. No differentiation of a remainder is used.

Theorem 3, its defining asymptotic on p. 4, Corollary 1, and Section 7
give, for fixed k,l,m,n and S=k+l+m+n,

    integral_H^(2H) Z^(k) Z^(l) Z^(m) Z^(n) dt
      =h(k,l,m,n) H ell^(S+4)/pi^2+O(H ell^(S+3)).    (5)

For completeness its coefficient definition is as follows, with
u=(u1,u2,u3,u4) in [0,1]^4:

    A=1/2+(u1-u2)u3-u1, B=1/2+(u2-u1)u3-u2,
    C=1/2+(u1-u2)u4-u1, D=1/2+(u2-u1)u4-u2,
    h(k,l,m,n)=3(-1)^(m+n) i^S
         integral_[0,1]^4 (u1-u2)^2 A^k B^l C^m D^n du. (6)

Corollary 1 gives h=0 when S is odd. Dividing (5) by H ell^S
proves (2) for X_H. In particular q_abc=0 if b is odd, since
S=b+2c. This is the cited parity statement, not an inference that
four independent random variables represent (6). All orders here
are fixed and form a finite set; the constants and onsets can be
maximized over that set. The source supplies the O(ell^3) errors,
not merely little-o(ell^4) asymptotics.

These statements and their Section 7 specialization were inspected in
the prior EXPLORE assessment
`drafts/literature/2026-10-27-hardy-jet-moment-feasibility-coverage.md`.
The published arithmetic results are imported, not reproved. Section
4.2 omits the proof of Proposition 3 used in that source's deduction;
there is no independent audit of that omitted proof here. The
established rare/bulk mechanism in L414 and L416 motivates this
construction; neither lemma's response-dependent conclusion is used
as a mathematical premise. The present fixed-divisor construction is
self-contained from (4)--(5) and the atomic theorem below.

### 2. A positive spherical measure retains all fourth moments

Write R_H(t)=|X_H(t)| and n_H(t)=X_H(t)/R_H(t) where R_H(t)>0.
At R_H=0 choose n_H=(1,0,0); its weight below is zero. Define the
finite positive Borel measure mu_H on S^2 by

    integral F(n) dmu_H(n)
      =(H ell^4)^(-1) integral_H^(2H) R_H(t)^4 F(n_H(t)) dt. (7)

Hardy's function and its derivatives are continuous on each positive
compact height interval, so this pushforward is well-defined. Let
W_H=mu_H(S^2). Expanding

    R_H^4=x^4+y^4+z^4+2x^2 y^2+2x^2 z^2+2y^2 z^2

and applying (5) shows

    W_H=q_400+q_040+q_004+2q_220+2q_202+2q_022+O(ell^(-1)). (8)

In particular 0<=W_H<=W_* for one finite constant W_*>0 and one
eventual ray. No lower bound for W_H or limiting probability law is
needed. Let S_y(n_x,n_y,n_z)=(n_x,-n_y,n_z) and put

    muhat_H=(mu_H+(S_y)_*mu_H)/2.                      (9)

It has the same mass W_H. Every odd-n_y monomial integrates to zero,
whereas every even-n_y monomial retains its mu_H integral. For every
homogeneous degree-four monomial M_abc, (7) gives exactly

    ell^4 integral M_abc(n) dmu_H
       =H^(-1) integral_H^(2H) M_abc(X_H(t)) dt.       (10)

### 3. Rare contribution, including the strict odd tolerances

For ell>=1 define the finite positive measure eta_H by pushing
ell^(-4) muhat_H forward under n -> ell^2 n. Its total mass is

    p_H=W_H ell^(-4)=O(ell^(-4)).                     (11)

All integrals against eta_H below are unnormalized contributions,
not conditional expectations. Its raw second matrix is

    R_ij=integral X_i X_j deta_H
        =integral n_i n_j dmuhat_H=O(1).              (12)

The bound is uniform, since |n_i n_j|<=1 and W_H<=W_*.
Reflection gives R_12=R_23=0 exactly. For the fourth entries, degree
four homogeneity, (10) and (5) give

    integral M_abc deta_H
      =ell^4 integral M_abc dmuhat_H
      =q_abc ell^4+O_abc(ell^3),                     (13)

with exact equality to the actual raw moment when b is even. When
b is odd the left side and q_abc are both zero; replacing the
actual odd moment by zero uses only its allowed O(ell^3) error.
Thus reflection changes no required leading coefficient, and no
O(1) odd second remainder is being tolerated.

Since Q is continuous, nonnegative and homogeneous of degree two,

    C_H:=integral Q deta_H=integral Q(n) dmuhat_H,
    0<=C_H<=W_H/2<=W_*/2.                            (14)

Here Q(n)<=(n_x^2+n_z^2)/2<=1/2 on S^2. Every rare state has
norm ell^2. For each H this is a bounded, integrable measure.

### 4. A twelve-state bulk with positive clipped mass

Choose three independent model variables: epsilon=+1 or -1 with
probability 1/2 each; k=1/12 with probability 1/6 or k=-7/60 with
probability 5/6; and v=0 with probability 1/2 or v=+/-1/sqrt(6)
with probability 1/4 each. These choices describe an abstract finite
law and are not independence assertions about actual Hardy jets.
Put B=(epsilon,v,k epsilon). Direct arithmetic gives

    E k=1/72-7/72=-1/12,
    E k^2=1/864+49/4320=1/80,
    E v=0, E v^2=1/12,
    E B B^T=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]]. (15)

For example E(epsilon v)=E epsilon E v=0 and
E(k epsilon v)=E k E epsilon E v=0. All diagonal and xz entries
are the displayed exact values. No covariance completion is assumed.
Moreover Q(B)=(k-v^2)_+. It is nonzero exactly when k=1/12 and
v=0; then its value is 1/12 and that event has probability 1/12.
For k=-7/60 it is zero, and when k=1/12, v^2=1/6 it is zero.
Consequently

    E Q(B)=1/144.                                    (16)

Every coordinate of B has absolute value at most 1, and
|B|^2<=1+1/6+49/3600<2. In particular each of its fifteen fourth
monomials has absolute expectation at most 1. Give the law of
sqrt(ell) B total mass w_H=1-p_H. Enlarge the one common onset so
that ell>=2 and p_H<=1/2. This is a positive measure of mass at
least 1/2, with exactly twelve states and norm less than ell^2.

### 5. Simultaneous errors, normalization and the fixed lower bound

Let nu_H^pre be the sum of eta_H and this bulk measure. Their masses
are p_H and 1-p_H, so it is a probability law. By (12) and (15),
its second matrix is w_H ell K+R, with K the matrix in (15).
For each even entry the difference from ell K is

    R_ij-p_H ell K_ij=O(1)+O(ell^(-3))=O(1).         (17)

Both odd entries are exactly zero in both components. This proves
every error in (1), including its two power-saving bounds. For each
of the fifteen fourth monomials the bulk adds

    w_H ell^2 E M_abc(B)=O(ell^2).                   (18)

Combining (18) with (13) retains the prescribed O(ell^3) remainder
for all fifteen entries on this one law. Odd-b bulk entries are
also exactly zero by the symmetry of v, although only O(ell^3)
is required for them. No tensor coordinate is omitted or fitted.

Finally (14), (16) and homogeneity give the exact expression

    E_nu_H^pre Q=(1-p_H)ell/144+C_H.                 (19)

Since p_H ell=O(ell^(-3)) and 0<=C_H<=W_*/2, this is
ell/144+O(1). Since p_H<=1/2 and C_H>=0, it is at least
ell/288. This lower bound holds for every sufficiently large real
H, not just a subsequence. Positivity, probability normalization,
all errors and the atom-size bound share a common onset by taking
the maximum of the finitely many preceding onsets.

### 6. Finite atomic replacement and the inference it obstructs

Import Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's
Theorem*, Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
[DOI 10.1090/S0002-9939-06-08249-9](https://doi.org/10.1090/S0002-9939-06-08249-9),
[arXiv:math/0502473v2, Corollary 2 and proof, pp. 3--4](https://arxiv.org/pdf/math/0502473v2).
For a positive measure concentrated on a measurable set and an
integrable measurable map to R^N, that corollary supplies at most N
positive atoms in the set preserving all coordinate integrals.
It applies to measurable nonpolynomial coordinates as well as
polynomials; no moment-duality or attainment claim is substituted.

For each H apply it to nu_H^pre on the closed ball |X|<=ell^2 and
the 23-coordinate map

    (1, x^2, xy, xz, y^2, yz, z^2,
       (x^a y^b z^c)_(a+b+c=4), Q(x,y,z)).            (20)

The count is 1+6+15+1=23. The law is already a feasible positive
probability measure. All these coordinates are continuous and
bounded on its ball, hence absolutely integrable. The theorem
therefore supplies nu_H with at most 23 positive atoms in that ball.
The constant preserves mass one, the other coordinates preserve
(1), (2) and the exact value in (19). Thus all uniform estimates
survive without any control on how the chosen atom locations vary
with H. This proves (3).

The missing inference is precise: a statement that *every* family
of probability laws satisfying only (1)--(2) has E Q=o(ell) is
false, since this family has E Q/ell -> 1/144. The construction
borrows actual quartic data to ensure a positive representing
measure, then changes its radii and adds a new bulk. It makes no
claim to reproduce the actual distribution, its lower-order moment
coefficients, further observables, or a single analytic function.

For relevance only, the already established L471 (7)--(9) identifies
the actual gamma-normalized negative first-sign mass with
H ell^2 times the actual mean of Q, up to O(ell/H). Thus an actual
o(H ell^3) estimate needs information beyond exactly these moment
constraints. L471 is not an input to the existence proof above.
The pair-divided route's retained failure is neither reopened nor
strengthened to an impossibility assertion for other methods.

### 7. Separate critical application audit, 28 October 2026

The complete construction was replayed under the previously saved
SPECIALIZE assessment
`drafts/literature/2026-10-27-l472-critical-audit-coverage.md`.
The following checks concern its application of cited inputs, not a new
Hardy moment theorem or a stronger finite-data obstruction.

**Source normalization.** Bui--Hall v1, Introduction (1) and its preceding
display, Theorem 3, Corollary 1 and Section 7 were directly checked at
the primary URL above. They retain the errors used in (4)--(5).
Section 4.2 explicitly omits Proposition 3's proof; that qualification
remains. The divisor here is the constant ell=log H, so no derivative
of a height-dependent divisor enters the application.

For each even second entry, write the monic polynomial of degree
r+1, r=j+k, as P. With fixed c=log(2pi),

    2P(ell+log 2-c)-P(ell-c)=ell^(r+1)+O(ell^r).

Dividing by ell^r leaves ell+O(1), and the divided analytic error is
O(H^(-1/4)ell^(1/2)). Thus the six entries, in the order
x^2,xy,xz,y^2,yz,z^2, have leading coefficients
1,0,-1/12,1/12,0,1/80. For xy and yz the primitive odd-order bound
instead gives exactly the power-saving tolerances in (1); the
constructed law has these entries zero, so it satisfies them without
absorbing any O(1) error. The source fourth error divides by H ell^S
to O(ell^3), including S=0. Since S=b+2c, Corollary 1 applies to
every odd-b entry. No separate representation of the signed integral
in (6) as a positive measure is needed: (7) uses actual real jets.

**Positive measures and scaling.** The zero-radius convention in (7)
is measurable and receives weight zero. For fixed H continuity on
[H,2H] gives finite integrals. Formula (8) uses only six of the covered
quartics, so one W_* bounds W_H on an entire eventual ray. Reflection
preserves this bound and positivity. Under the rare pushforward a
degree-d homogeneous observable receives multiplier ell^(2d-4):
d=0 gives mass W_H ell^(-4), d=2 gives its spherical integral, and
d=4 gives ell^4 times that integral. In particular second and clipped
contributions are unnormalized O(1), not O(ell^4) conditional moments.
The estimate 0<=Q(n)<=1/2 proves (14) with no sign cancellation.

**The bulk and every error.** Independence gives the exact second
matrix (15); E k=-1/12 and E k^2=1/80 hold with the displayed positive
weights. The event k=1/12,v=0 has probability (1/6)(1/2)=1/12,
independent of epsilon, and all other states have Q=0. This verifies
the coefficient 1/144. All twelve states are distinct and their
probabilities sum to one. For a quartic M=x^a y^b z^c,

    E M(B)=E epsilon^(a+c) E v^b E k^c.

If b is odd, a+c=4-b is odd and this is zero. If b is even its
absolute value is at most one. This checks the entire tensor:

| b | All monomials in this class | Rare contribution | Bulk contribution |
|---|---|---|---|
| 0 | x^4, x^3 z, x^2 z^2, xz^3, z^4 | actual raw moment | O(ell^2) |
| 1 | x^3 y, x^2 yz, xyz^2, yz^3 | 0, with q=0 | 0 |
| 2 | x^2 y^2, xy^2 z, y^2 z^2 | actual raw moment | O(ell^2) |
| 3 | xy^3, y^3 z | 0, with q=0 | 0 |
| 4 | y^4 | actual raw moment | O(ell^2) |

For the nine even-b entries, the source O(ell^3) error absorbs the
bulk O(ell^2). For the other six, the constructed value is exactly
zero. The second errors are R_ij-p_H ell K_ij for the four even
entries and zero for the two odd entries. Hence all 21 constraints
hold simultaneously, with no fitted coordinate or changed tolerance.

Choose H beyond the source onsets and so that ell>=2 and
ell^4>=2W_*. Then p_H<=1/2, all component masses are nonnegative,
and the bulk norm squared is <2ell<=ell^4. The rare norm is ell^2.
Formula (19) now gives both E Q>=ell/288 and
|E Q-ell/144|<=W_*/2+W_*ell^(-3)/144. These explicit comparisons
check one common onset and the asserted uniform O(1), without an
effective numerical value for W_* or that onset.

**Atomic theorem hypotheses.** Bayer--Teichmann v2 Corollary 2 and
Remark 2 were checked at the primary PDF above. Take Omega=A to be
the closed ball of radius ell^2, with its Borel sigma-algebra and the
restricted probability measure nu_H^pre. The map (20) is continuous;
every coordinate, hence its Euclidean norm, is integrable on this
compact ball. The map dimension is 23 already including the constant.
The corollary therefore supplies at most 23 positive weights and
points in this same ball. The constant coordinate fixes their sum at
one. Preservation is exact for Q as well as all polynomial coordinates,
so neither errors nor the lower threshold change. No uniform choice
of atoms as a measurable function of H is asserted or needed.

**Verdict and limits.** The stated existence and its limited inference
obstruction pass without correction. The empty L472 DAG row is
accurate: L414/L416 are historical mechanisms and L471 is contextual
scale only. The contextual scale follows from L471 (7)--(9) using
(ZZ''-Z'^2)_+=ell^2 Q(X_H); it is not an actual-law identification.
No new obstruction beyond L472, actual clipped lower bound, first or
cubic constraint, or global analytic realization is established by
this audit. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this H-dependent finite-moment construction
and clipped statistic has not been checked. The imported Bui--Hall
theorems and Bayer--Teichmann measurable-map corollary are cited above;
no matching Mathlib theorem is asserted. The finite probability
identities and scaling calculations are written out here. Unknown
formal coverage is not evidence of absence. POTENTIALLY_NEW refers
only to the prior assessment's not finding this exact clipped-mass
conclusion, not to certified originality or a new Hardy moment theorem.
