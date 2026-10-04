# L047 — Exact pure factor-point correction region for Bogomolov

## Hypotheses

Retain L046's smooth projective fourfold X=S x S, full second
character beta=2[C]+B_c, cup-product pairing q, ample real class
h=omega_c and actual product Kahler class Omega=p_1^*h+p_2^*h.
Write s=q(h,h)>0 and e_1=eta tensor 1, e_2=1 tensor eta, where
integral_S eta=1. Thus e_i are codimension-two classes on X.

The mixed component of beta has self-adjoint correspondence operator
D with D h=2lambda h, where lambda is the positive root of
f(z)=z^3+z^2-2z-1, initially isolated by 1<lambda<3/2 in L046.
The two pure coefficients of beta are both four. For a,b in Q, set

\[
\beta_{a,b}=\beta+a e_1+b e_2.
\]

The proposed lower Chern data are c_1=0 and ch_2=beta_(a,b)
at arbitrary positive rank r. Keep the mixed component, chamber
and first Chern class fixed. This is a numerical necessary-condition
test; no bundle, K-class or higher Chern characters are prescribed.

## Conclusion

The corrected data satisfy the cited Bogomolov necessary inequality
at Omega if and only if

\[
a+b<-8-4\lambda.                                      \tag{1}
\]

No rational pair attains the boundary. Equivalently, for the
corrected pure coefficients p=4+a and t=4+b, the condition is
p+t<-4lambda. The region is nonempty, and the following thresholds
are exact numerical subcases:

- For integer a,b, condition (1) is a+b<=-13. Thus (-13,0),
  for example, passes the inequality, whereas any total correction
  -12 fails.
- For symmetric rational corrections a=b=u, the condition is
  u<-4-2lambda. The value u=-13/2 passes.
- For symmetric integer corrections, the condition is u<=-7.
  The least negative permitted integer u=-7 gives p=t=-3;
  u=-6 fails.

Every admitted rational pair has strictly positive discriminant
intersection, rather than equality. Passing this inequality does
not establish Chern-class integrality, rank truncation, local
freeness, stability or transverse transport. In particular it does
not revive L044's unchanged lower data or the fixed K-class stopped
by L045. The mixed action on T(S) is still 2U and no new algebraic
class, surface or RM direction is obtained.

This is an ADVANCE in the local numerical compatibility test,
classified as REPRODUCTION of the inspected inequality and standard
cup-product tools. It is not a claim beyond the checked literature.
The span remains 21 and the attained RM directions three against
four required; the universal rational Hodge gap remains unresolved.

## Proof

**Import the inequality and reuse the full contraction.** The source
already inspected for L046 is Arvid Perego, *Kobayashi-Hitchin
correspondence for twisted vector bundles*,
[arXiv:1910.01867v1, Corollary 6.42, p. 118](https://arxiv.org/pdf/1910.01867v1#page=118).
For a slope-semistable ordinary locally free bundle, by taking
trivial twisting and zero auxiliary B-field, its sign convention is

\[
\int_X\bigl((r-1)c_1^2-2r c_2\bigr)\Omega^2\leq0.
\tag{2}
\]

Polystability implies semistability by Definition 4.20, p. 65.
The real Kahler form is permitted directly, as recorded in the
saved assessment and L046; no rational replacement of Omega is
used. The identity ch_2=(c_1^2-2c_2)/2, supported by
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
gives c_2=-beta_(a,b). Hence (2) is equivalent, at every r>0, to
integral_X beta_(a,b) Omega^2<=0. No higher character enters.

L046 establishes integral_X beta Omega^2=(8+4lambda)s, retaining
both pure components and the full mixed tensor. On S, h^2=s eta,
so Omega^2=s(e_1+e_2)+2h tensor h. Since e_1^2=e_2^2=0,
integral_X e_1e_2=1 and e_i(h tensor h)=0, each added e_i
has contraction s. Linearity therefore gives

\[
\int_X\beta_{a,b}\Omega^2=(8+4\lambda+a+b)s.           \tag{3}
\]

Since s>0, the necessary inequality is a+b<=-8-4lambda.
The monic cubic f has no rational root: the only possibilities
are 1 and -1, with f(1)=-1 and f(-1)=1. Thus lambda is
irrational. For rational a,b equality would make lambda rational,
so the weak inequality is exactly (1). Its usual discriminant
2r c_2-(r-1)c_1^2 has intersection
-2r(8+4lambda+a+b)s, strictly positive for every admitted pair.
This is a numerical value, not an equality-case bundle theorem.

**Exact thresholds without decimal root approximations.** For z>=1,
f'(z)=3z^2+2z-2>0. Also f(1)=-1 and f(5/4)=1/64>0.
The positive root from L046 therefore satisfies

\[
1<\lambda<5/4,\qquad 12<8+4\lambda<13.                \tag{4}
\]

Consequently an integer a+b is below -8-4lambda precisely when
it is at most -13. Substituting a=b=u gives the rational symmetric
condition u<-4-2lambda. Its boundary lies strictly between -13/2
and -6, so u=-13/2 passes, u=-6 fails, and an integer u passes
precisely when u<=-7. These statements prove all the listed
subcases. There is no largest admitted rational total correction:
the allowed totals can approach the irrational boundary from below,
but cannot attain it.

**Scope and verification.** Adding e_1,e_2 changes no H^2 tensor
H^2 component and hence no correspondence action on H^2(S).
The pure classes are {point} x S and S x {point}, of codimension
two. Codimension-four point sheaves on X, including the singular
corrections in the previous Riemann--Roch calculations, cannot
change this ch_2 and are not being used as a repair here.

An exact Fraction calculation checked f(5/4)=1/64 and, using
L046's lambda^2 s=4lambda^2+12lambda+2, reduced (3) in
Q[z]/(f). For totals a+b=-12,-13,-14, the scaled contractions
are respectively 8-8lambda+16lambda^2,
6-20lambda+12lambda^2 and 4-32lambda+8lambda^2.
Their signs follow from (3)--(4), with -13 passing and -12
failing. The command and results are saved in
`drafts/2026-10-04-pure-point-bogomolov-calculation.md`.
The cohomological proof above supplies the necessary and sufficient
condition for this inequality; arithmetic checks certify no bundle.

## Mathlib

Coverage of this full numerical region: **not checked**. No matching
Mathlib declaration or absence from checked Mathlib sources is
asserted. Perego's directly linked corollary supports the necessary
inequality and the linked Stacks section supports its Chern-character
conversion. They are supporting results rather than matches for the
evaluated correction region. Kunneth, cup-product linearity and the
rational root theorem are standard supporting tools. This is a
reproduction with no certified originality or Hodge resolution claim.
