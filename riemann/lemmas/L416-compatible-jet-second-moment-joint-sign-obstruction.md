# Lemma 416: all six critical-jet second moments permit joint-sign avoidance

## Hypotheses

Use L415's selected local-jet relaxation, including all of L414's
pointwise constraints, exact ordinary/envelope conversion, both first
means, cubic tolerance, 23 quartic coordinates and absolute envelopes.
The constants in the qualitative pointwise bounds may be chosen once
independently of H, as in those lemmas. Put ell=log H and additionally
impose the six raw second moments of X=(x,y,z):

    E x^2=ell+O(1),        E xz=-ell/12+O(1),
    E y^2=ell/12+O(1),     E z^2=ell/80+O(1),
    E xy=O(H^(-2/3)ell^(-1)),
    E yz=O(H^(-2/3)ell^(-3)).                         (1)

These are raw moments, with no imposed first moments of x,y,z and no
prescribed constants in the four O(1) errors. The actual-family source
specialization is justified below. No uniform height marginal, actual
response realization, single global function pair, or regulator margin
is assumed. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-15-compatible-jet-second-moment-scope.md`.

## Conclusion

For every sufficiently large real H there is one law satisfying this
whole enlarged list, with fixed bound constants and one common onset.
It has exactly

    E Delta=-a_* ell, E Bcal=-b0, E xy=E yz=0,
    b0=zeta(3)/(4pi),                                (2)

and E(Delta Bcal)=beta_* ell^2+O(ell). All 23 quartic leading
coefficients are unchanged. Both absolute power-three bounds remain
O(ell^2). Its support avoids {Delta>0,Bcal<0}, and its negative-Bcal
clipped square mean is strictly negative.

Thus even these added second moments cannot force the joint sign or a
positive clipped mean from the selected information. This is a local
feasibility obstruction, validated by the separate step-149 critical audit
below. It is not
an actual-zeta law, an actual clipped-statistic conclusion, or a regulator
margin, common-zero bound, positivity extension or RH consequence.
POTENTIALLY_NEW records the limited prior source comparison, not certified
originality or a new Hardy moment theorem.

## Proof

### Imported second moments and sharp normalization

Import H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
Z(t)*, Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1, Introduction p. 1, equation (1) and preceding display](https://arxiv.org/pdf/2304.05178v1#page=1).
For fixed nonnegative j,k and J_jk(T)=integral_0^T Z^(j)Z^(k),
if j+k=2s and |j-k|=2d, their unconditional formula is

    J_jk(T)=(-1)^d T Q_(2s+1)(log(T/(2pi)))/(4^s(2s+1))
                 +O_(j,k)(T^(3/4)(log T)^(2s+1/2)),       (3)

where Q is monic of degree 2s+1. For odd j+k they state
J_jk(T)=O_(j,k)(T^(1/3)). These precise mixed statements are imported
directly; the underlying Hall theorem need not be reproved. L389 (3)
identifies f=F/A=-sigma Z with one constant sigma in {1,-1} on the
eventual connected ray, including at zeros. Hence products of two
ordinary derivatives of f equal the corresponding Hardy products.

Here is the needed specialization, with both sharp endpoints retained.
Write m=j+k, w_m(t)=log(2+t)^(-m). For even m, (3) gives

    J_jk(t)=C_jk t(log t)^(m+1)+R(t),
    R(t)=O(t(log t)^m+t^(3/4)(log t)^(m+1/2)),
    C_jk=(-1)^d/(4^s(2s+1)).

Partial summation on [H,2H] is the exact identity

    integral_H^(2H) w_m(t) dJ_jk(t)
       =[w_m(t)J_jk(t)]_H^(2H)-integral_H^(2H) w_m'(t)J_jk(t) dt.

On this interval w_m=O(ell^-m) and, for m>0,
|w_m'|=O(H^-1 ell^(-m-1)); for m=0 it is zero. The two residual
endpoint terms cost O(H+H^(3/4)ell^(1/2)), and the residual integral
costs O(H/ell+H^(3/4)ell^(-1/2)) when m>0. After division by H
these are O(1). The derivative of t(log t)^(m+1), multiplied by w_m,
is ell+O(1) uniformly on the interval. Thus the normalized mean is
C_jk ell+O(1). For odd m, the primitive bound in (3)'s preceding
display instead gives endpoint cost O(H^(1/3)ell^-m) and integral
cost O(H^(1/3)ell^(-m-1)); division by H gives
O(H^(-2/3)ell^-m). No absolute integral of a signed remainder is
inferred from its primitive bound. For (j,k)=(0,0),(0,2),(1,1),(2,2)
the coefficients are 1,-1/12,1/12,1/80; the two odd pairs are
(0,1),(1,2). This proves precisely the source applicability in (1).
The divisors are applied after differentiation; physical jets still
require L414's exact conversion.

### Preserve the rare component

Use unchanged the rare component constructed and audited in L414 and
retained in L415. All its output states have t=H, response
v=(ca,-ch/2,-ca/4), c=1/(4pi), and the exact converted physical jets.
Write L_H=log(2+H), r=q(H)/L_H^2, with r=O(H^-2 L_H^-2).
In L414's notation its mass is p=W_H/(lambda_H^4 ell^4)=O(ell^-4),
its critical norm is lambda_H ell^2, W_H=O(1), and lambda_H is bounded
above and below by positive constants. Its exact unnormalized integrals
are, using L415 (4),

    M_H=E_rare Delta=O(1), J_H=E_rare Bcal=O(ell^-2),
    R_ij=E_rare X_i X_j
         =lambda_H^-2 integral n_i n_j dmu_H=O(1).       (4)

The sign orientation cancels from every R_ij. Its cubic integral is
exactly beta_* ell^2, and its 23 quartic integrals already have the
required b_*, kappa_* and every Gamma_ij coefficient. Its support,
curvature, and absolute envelopes are unchanged. In particular it
already avoids the forbidden joint event. All integrals in (4) are
unnormalized rare integrals; no conditional expectation is substituted.
Put w=1-p, eventually at least 1/2.

### An eight-state bulk distribution

In the following finite probability space, choose independent signs
epsilon,eta, each equally likely to be +1 or -1, and independently set

    P(k=1/60)=5/9, P(k=1/6)=4/9.

These are choices in the model law, not assertions of independence of
actual phases. Direct rational arithmetic gives

    E k=1/12, E k^2=1/80,
    K_0=[[1,-1/12],[-1/12,1/80]], det K_0=1/180>0.    (5)

Give this bulk law total mass w, and at each state set

    x=sqrt(ell) epsilon, z=-k x,
    y=sqrt(ell/12) eta+u_H x+v_H z+e_H,
    (a,h)=(0,s_H), v=(0,-c s_H/2,0), t=H.             (6)

The v_H in y is a scalar shear coefficient, distinct from the response
triple v. Define all three calibration parameters and this shear by

    s_H^2=(a_* ell+M_H)/(c^2 w ell(1/12-r)), s_H>0,
    (u_H,v_H)^T=-(w ell)^(-1) K_0^(-1)(R_12,R_23)^T,
    e_H=(b0+J_H)/(w c s_H).                           (7)

We next verify these definitions, the response annulus, and exact support.

L410's constants give a_*/c^2=S/15, where
S=zeta(5)zeta(3)^2/zeta(6). Therefore s_H^2 tends to s_0^2=4S/5.
Write M_zeta=zeta(5/2). The strict elementary integral bounds

    zeta(3)<5/4, zeta(5)<67/64, zeta(6)>1,
    M_zeta>1+2^(-5/2)>7/6

follow by bounding the sum from n=3 onward above by integral_2^infinity
x^(-s) dx, and using sqrt(2)<3/2 for the last inequality. Also S>1
because zeta(5)>zeta(6) and zeta(3)>1. Consequently

    M_zeta^(-2)<36/49<4/5<s_0^2<335/256<49/36<M_zeta^2. (8)

This gives a fixed strict annular margin. By (4), p=o(1) and r=o(1),
the numerator and denominator for s_H^2 are positive eventually and
s_H^2 remains in that annulus. Hence s_H and its inverse are uniformly
bounded, u_H,v_H=O(ell^-1), and e_H=O(1), with e_H>0 eventually.

Use the exact product conversion of L414, including alpha=A'/A and q.
For a=0,h=s_H the identities of its audited equation (3) reduce to

    Ccal=c^2 s_H^2/4,
    Bcal=-c s_H y,
    Delta=c^2 s_H^2(xz+r x^2)
          =c^2 s_H^2 ell(-k+r).                     (9)

In particular every bulk state has Delta<0 once |r|<1/120, since
k>=1/60. This sign is independent of y and includes the exact curvature;
there is no approximate support argument. The first bulk Delta integral
is w c^2 s_H^2 ell(-1/12+r)=-a_* ell-M_H. The independent signs
give E_bulk,conditional y=e_H, so its Bcal integral is
-w c s_H e_H=-b0-J_H. Adding (4) proves both first means in (2).

### Every second moment, including the small odd errors

The conditional bulk (x,z) raw matrix is ell K_0. Its correlations
with the centered independent eta term and the constant e_H vanish.
Consequently its unnormalized odd cross moments are

    (E_bulk xy,E_bulk yz)^T=w ell K_0(u_H,v_H)^T
                            =-(R_12,R_23)^T.        (10)

After adding the rare component both are exactly zero, hence satisfy
even the two small power-saving errors in (1). No O(1) error is allowed
or used for these odd entries. The other three entries of this block are

    E x^2=w ell+R_11=ell+O(1),
    E xz=-w ell/12+R_13=-ell/12+O(1),
    E z^2=w ell/80+R_33=ell/80+O(1).                 (11)

Here p ell=O(ell^-3). The remaining diagonal is

    E y^2=w[ell/12+ell(u_H,v_H)K_0(u_H,v_H)^T+e_H^2]+R_22
         =ell/12+O(1),                              (12)

since the shear square is O(ell^-1) and e_H^2=O(1). This accounts for
all six constraints on the very same law; no finer even coefficients
have been imposed or claimed.

### Cubic tolerance, all quartics, and fixed bounds

Conditionally on k, the signs in (6) still have mean zero, while Delta
in (9) depends only on k. Thus the bulk cubic integral is exactly

    E_bulk(Delta Bcal)=-c s_H e_H E_bulk Delta
                      =c s_H e_H(a_* ell+M_H)=O(ell). (13)

Together with the unchanged rare integral this proves the required
beta_* ell^2+O(ell), an allowed o(ell^2) error. On every bulk state,
|X|=O(sqrt(ell)), |Bcal|=O(sqrt(ell)), |Delta|=O(ell), and
|omega|=O(sqrt(ell)), with uniform constants. Hence each of

    E_bulk Delta^2, E_bulk(Delta Bcal^2),
    E_bulk[Delta omega_i omega_j], 1<=i<=j<=6,

has absolute value O(ell^2)=o(ell^4). All 21 matrix entries, including
zero entries and off-diagonal signs, therefore retain exactly their
rare coefficients, as do the two scalar quartic entries. This step
uses audited L414's whole quartic measure without rounding, fitting,
or replacing any coefficient or its response collisions.

The bulk contributions to U^2, U^(3/2), |Bcal|^3 are respectively
O(ell^2), O(ell^(3/2)), O(ell^(3/2)). L414's unchanged rare
contributions are O(ell^4), O(ell^2), O(ell^2). These prove every
absolute envelope, including O(ell^2) for both power-three totals.

The exact model response is always v=(ca,-ch/2,-ca/4), and (8)
places the bulk response in the same fixed annulus as the rare part.
The model response errors are zero; this is an allowed state choice,
not a removal of actual errors in L414's quartic pushforward. The
fixed constants D_j,K=1 in L414 (14) bound every converted response.
Equation (9) gives Ccal>=c^2/(4 M_zeta^2) on the bulk, stronger than
the required c^2/(8 M_zeta^2); the rare part retains that required
bound from L414. Bounded alpha and q=O(H^-2) make the conversion
matrix uniformly bounded. The whole support has |X|=O(ell^2), so
|P_j| L_H^j/(1+H)^(1/2) tends uniformly to zero for j<=2.
Thus E_j=1 works after a common onset, as in L414. All constants are
fixed before H, and the maximum of finitely many onsets covers every
sufficiently large real H, not just a subsequence.

The rare component is a measurable bounded pushforward at each H, and
the bulk has eight states with positive weights. Their masses add to
one. Every listed signed, absolute and clipped moment is measurable
and absolutely integrable. The same exact Taylor-jet assignment as
L414 gives local compatibility of each state with the actual envelope.
It gives no single global pair realizing the law. No atomic replacement,
strong duality, optimizer, or new existence theorem is needed here.

Finally the rare part has nonpositive clipped integrand by support.
On the bulk, the eta=+1 states have y>0 for every sufficiently large H:
the leading term is sqrt(ell/12), the shear is O(ell^-1/2), and e_H
is bounded. These states have positive mass, Bcal<0 and Delta<0.
Every other bulk state also has Delta<0. Thus

    E[Delta Bcal^2 1_(Bcal<0)]<0.

This proves the enlarged local feasibility claim only. Actual/global
realization, a uniform height marginal, actual clipping, L413's
regulator-scale/full-error margin, common-zero upper counts and global
mixed positivity remain independently unproved. The finite moment
obstruction does not prove or disprove RH.

### Separate critical audit — 2026-10-15, step 149

This REPRODUCTION proof_audit uses the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-15-compatible-jet-second-moment-critical-audit.md`.
The construction passes within precisely its selected relaxation. The
audit imports the already assessed Bui--Hall mixed theorem cited above
and the audited L414/L415 construction, with L389's identification and
L410's constants. It checks their specialization and simultaneous use;
it proves no new Hardy moment theorem or claim of originality. No
essential source hypothesis changes, new atomic theorem or numerical
certificate are needed.

**Sharp source normalization.** The constant sign in L389 (3) cancels
in every product f^(j)f^(k), including at zeros. For m=j+k even,
the lower terms of the monic polynomial in (3), including the shift
by log(2pi), contribute O(t(log t)^m). With w=L^(-m), the boundary
error divided by H is O(1+H^(-1/4)ell^(1/2))=O(1); the integral
error divided by H is O(ell^(-1)+H^(-1/4)ell^(-1/2)) when m>0,
and is zero when m=0. Differentiating only the explicit main
primitive gives

    w(t) [t(log t)^(m+1)]'
       =(log t/L(t))^m [log t+m+1]=ell+O(1).

Thus both sharp endpoints and the full signed primitive error give
C_jk ell+O(1), with coefficients 1,-1/12,1/12,1/80 for the four
even pairs in (1). For odd m=1,3, the same exact integration by parts
uses J_jk=O(t^(1/3)); its boundary and integral errors divided by H
are respectively O(H^(-2/3)ell^(-m)) and
O(H^(-2/3)ell^(-m-1)). This proves exactly the two stated small
odd tolerances. No absolute integral of the derivative of the error
is used. These are raw X moments, not P moments or centered covariances.
The jet derivatives are taken before their divisors are applied; the
weight w is differentiated only in partial summation.

**Rare normalization and exact bulk algebra.** On the retained rare
component a degree-d homogeneous critical-jet observable has integral
lambda_H^(d-4) ell^(2d-4) times its oriented mu_H integral. At degree
two the orientation disappears. Hence its entire raw matrix is exactly
R_ij=lambda_H^(-2) integral n_i n_j dmu_H=O(1), and its first Delta
and Bcal integrals are M_H=O(1), J_H=O(ell^(-2)). At degree three
the orientation gives the exact integral beta_* ell^2; at degree four
the factor is ell^4. All are unnormalized rare integrals. The audited
lower bound on lambda_H follows from kappa_*>0 and compact boundedness
in L414 (7)--(8), independently of the bulk modification. Its mass
p=O(ell^(-4)) is unchanged.

The two-point k law satisfies, by exact rational arithmetic,

    (5/9)(1/60)+(4/9)(1/6)=1/12,
    (5/9)(1/3600)+(4/9)(1/36)=1/80,
    det K_0=1/80-1/144=1/180,
    K_0^(-1)=[[9/4,15],[15,180]].

Both eigenvalues of this fixed symmetric block are positive. Independence
of epsilon and eta, and their zero means, imply that the constant e_H
and the centered eta term contribute neither xy nor yz. Consequently
the total odd moments are exactly

    (R_12,R_23)^T+w ell K_0 (u_H,v_H)^T=(0,0)^T.

The inverse matrix and R_ij=O(1) give both shears O(ell^(-1)). This
exact cancellation meets (1); an O(1) residual bound alone would not.
The four even entries, on this same law, are

    E x^2=w ell+R_11,
    E xz=-w ell/12+R_13,
    E z^2=w ell/80+R_33,
    E y^2=w[ell/12+ell (u_H,v_H)K_0(u_H,v_H)^T+e_H^2]+R_22.

Here p ell=O(ell^(-3)), the shear-square term is O(ell^(-1)), and
e_H=O(1) as verified next. These are the required four O(1) errors;
no sharper coefficient or critical first moment is silently imposed.

**Both first means, annulus and curvature.** The exact conversion
from L414, expanded before making a response choice, is

    ell_F=y^2-xz-r x^2,
    Ccal=v_1^2-v_0 v_2-r v_0^2,
    Bcal=2y v_1-x v_2-z v_0-2r x v_0.

All alpha terms cancel. With v=(0,-c s_H/2,0), it follows exactly
that Bcal=-c s_H y, Ccal=c^2 s_H^2/4 and
Delta=c^2 s_H^2(xz+r x^2). Thus y's shears and shift do not change
the discriminant, even with the actual curvature r retained.
L410 gives a_*/c^2=S/15, so (7) gives s_H^2 ->4S/5.

To verify the strict annular margin without numerical zeta estimates,
the decreasing-integrand tail bound gives zeta(3)<5/4 and
zeta(5)<67/64. Monotonicity of zeta on (1,infinity) gives S>1.
Since zeta(6)>1, 4S/5<335/256. Finally
M_zeta>1+1/(4sqrt(2))>7/6. Therefore both ends of (8) are strict:
M_zeta^(-2)<36/49<4/5 and
335/256<49/36<M_zeta^2. In particular the limiting amplitude is
strictly inside the prescribed annulus. Uniform O(1) bounds on M_H,
p=o(1), and r=o(1) give one onset at which (7) is positive and s_H
is in that annulus; s_H and its inverse are uniformly bounded.
Since w>=1/2 and b0+J_H>=b0/2 eventually, e_H is positive and O(1).

For |r|<1/120 every bulk state has k-r>0, hence Delta<0. Its
unnormalized first means are exactly

    E_bulk Delta=w c^2 s_H^2 ell(-1/12+r)=-a_* ell-M_H,
    E_bulk Bcal=-w c s_H e_H=-b0-J_H.

Adding the rare integrals proves both equalities (2). In particular
the second equality meets the complete L369 error requirement in
L415 (1), not merely an unspecified o(ell) tolerance. No quartic
replacement is used at either first-mean scale.

**Cubic and all 23 quartic coordinates.** Conditional on each k,
the sign variables give mean y=e_H, while Delta depends only on k.
Thus the bulk cubic integral is exactly
-c s_H e_H E_bulk Delta=c s_H e_H(a_* ell+M_H)=O(ell).
It is o(ell^2), as required; L414's extra exact cubic equality was
not an imposed constraint on the enlarged law.

The rare quartics are unchanged, including their signs and response
collisions: common critical-jet reversal leaves Delta^2,
Delta Bcal^2 and every Delta omega_i omega_j invariant. Audited
L414 (7) bounds the actual-to-leading error for each by
C R_act^4/ell before integration, and its subsequent curvature
replacement costs O(|r|W_H) at normalized scale. Its limits are
exactly b_*, kappa_* and every Gamma_ij, including zero entries.
The present modification introduces no further rare replacement.

On the bulk omega=(0,0,0,s_H x,s_H y,s_H z). Fifteen of its
21 symmetric matrix coordinates vanish exactly; the six pairs with
indices in {4,5,6} have absolute Delta-weighted integrals O(ell^2),
because |X|=O(sqrt(ell)) and |Delta|=O(ell). Also the bulk Delta^2
and Delta Bcal^2 integrals are O(ell^2). Every addition is therefore
o(ell^4), regardless of the target coefficient's sign or vanishing.
This checks all 23 quartic coordinates without fitting coefficients,
using H-dependent test vectors or introducing an off-diagonal factor.

**Absolute bounds, support and uniform quantifiers.** Bulk U^2 is
O(ell^2), and bulk U^(3/2) and |Bcal|^3 are O(ell^(3/2)). The
unchanged rare integrals, by L414 (13), are respectively O(ell^4),
O(ell^2) and O(ell^2). Thus both power-three bounds are O(ell^2),
stronger than the imposed O(ell^(9/4)) bounds.

Every model response lies in the fixed annulus and has zero response
approximation errors; L414 (14)'s fixed D_j and K=1 therefore work.
Bulk Ccal>=c^2/(4M_zeta^2), and rare Ccal>=c^2/(8M_zeta^2), so
the required full-support lower bound holds. Since alpha is bounded
and q=O(H^(-2)), the exact conversion matrix is uniformly bounded.
Every critical triple has norm at most C ell^2, with C independent
of H. For each j<=2, ell^2 L_H^j/(1+H)^(1/2) tends to zero.
Thus E_j=1 works after a further onset. The maximum of finitely many
onsets proves the assertions for every sufficiently large real H;
neither convergence of mu_H nor passage to a subsequence is used.

The rare orientation is Borel, including its two zero boundaries,
and enforces Bcal>=0 whenever Delta>0. All bulk states have Delta<0.
Their positive weights sum to w, while the rare mass is p=1-w.
The support at each H is bounded, so all listed observables and the
clipped statistic are measurable and absolutely integrable. On bulk
eta=+1 states, y=sqrt(ell/12)+O(ell^(-1/2))+e_H>0 eventually,
uniformly over epsilon,k. They have total mass w/2>0, Bcal<0 and
Delta<0. The entire support has nonpositive clipped integrand,
and these states have strictly negative integrand. Its mean is
therefore strictly negative. L414's exact local Taylor assignment
justifies compatibility of each state separately with the envelope;
it supplies no compatibility along a single global function pair.

No defect, changed leading coefficient or new direct dependency was
found. The earlier audits of L414/L415 did not check these six extra
constraints, so this is a distinct completed audit. The selected-list
obstruction is validated, while actual response realization at the
output height, a uniform height marginal, actual clipping, L413's
regulator-scale/full-error margin, common-zero upper counts and global
mixed positivity remain unproved. No RH conclusion follows.

## Mathlib

Full matching coverage for this construction and the imported mixed Hardy
moment theorem has not been checked. Unknown coverage is not absence or
formal verification. The source theorem is cited precisely; only its
normalization and the new finite bulk construction are proved here.
No numerical solver, numerical fit or mathematical script is an input.
