# L086 — Simultaneous full mod-120 and mod-seven occurrence in the fixed auxiliary family

## Hypotheses

Retain L073's fixed local curve E_q, q=3^30, algebraic closure Omega
of Q_3, embedded fields H=Q_3(zeta_60) and
N=Q_3(zeta_420,3^(1/7)), and the algebraic closure Q-bar of Q in
Omega. Fix M>=max(M_tors,31), h=3^M, and the integers c,d_*,e_*
chosen there, before any coefficient box grows. In particular
c=1/4 modulo h and

    d_*=d_0 mod h, d_*=c^2/3 mod 89,
    e_*=e_0 mod h, e_*=c^3/27+1 mod 89.

The fractions in the last congruences are in F_89. Consider the
entire family, with u,v varying independently through Z,

    g_(u,v)=x^3+c x^2+(d_*+89h u)x+(e_*+89h v),
    E_(u,v): y^2=g_(u,v)(x), O=[0:1:0].

All torsion fields use both coordinates of every geometric torsion
point. Images below are over Q, not over a torsion extension.

## Conclusion

There is a member E_star of this unchanged family such that, for the
same curve,

    rho_(E_star,120)(G_Q)=GL_2(Z/120Z),
    rho_(E_star,7)(G_Q)=GL_2(F_7).

Its complete local 210-torsion module is G_Q_3-isomorphic to
E_q[210]; all its geometric 30-torsion is H-rational and
H(E_star[7])=N as embedded fields. Its original monic equation is
minimal over Q_3 with split multiplicative reduction and its own Tate
parameter q_star satisfies v_3(q_star)=30. It has good reduction
at 89 with 90 rational points, and one arithmetic Frobenius lift
sigma_star has square acting as [-89]=[31] on its full 120-torsion.

More precisely, every sufficiently large maximum-norm box of integral
short coefficients contains such a family member. The conclusion is
existential, with no effective coefficients or size bound. E_star is
a new choice: neither previously chosen witness, nor any previously
constructed global field, is identified with it. The separate step341
critical audit below validates this known-method specialization. No nonnormality
conclusion or essential IUT flaw is asserted here.

## Proof

### Imported theorem and specialization scope

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-19-auxiliary-full-mod120-occurrence.md`.
Import David Zywina, *Elliptic curves with maximal Galois action on
their torsion points*, Bull. London Math. Soc. 42 (2010), 811–826,
[DOI](https://doi.org/10.1112/blms/bdq039),
[author-hosted 15-page version](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf).
Numbering refers to that version: section 1.1, pp.1–2; Definition
5.1, p.6; Proposition 5.7 and its proof, p.8; the Q-case assertion
in Lemma 2.4's proof, p.5. For fixed k, coefficient norm and
positive integer m, Proposition 5.7 bounds the proportion of
nonsingular integral short models with m-torsion image not containing
SL_2(Z/mZ) by O(log R/R^([k:Q]/2)). For k=Q, SL_2 containment
gives full GL_2 image by the cyclotomic determinant criterion cited
there. The assessment checked the composite-level proof cases,
including the small-prime and 2-power cases. The theorem applies to
m=120 as well as m=7; it requires neither squarefree m, minimality,
good reduction nor non-CM hypotheses.

The general theorem is imported without reproof. L046 supplies the
pointed Q-coordinate change and the earlier level-seven application;
L073 supplies the fixed refined family and its count. The extra work
here is the union-bound comparison at the two assessed fixed levels
and the same-member local retention. L046 alone is not a theorem
about level 120. No adelic density or radical-independence assertion
is substituted for the composite-level theorem.

### One fixed lattice and two exceptional sets

For d=d_*+89h u and e=e_*+89h v, L046's invertible pointed Q-map

    X=9x+3c, Y=27y

gives Y^2=X^3+AX+B with

    A=81d-27c^2, B=729e-243cd+54c^3.

Thus the coefficient pairs form exactly L073's affine lattice

    (A_*,B_*)+(a u,-243c*89h u+b v),
    a=81*89h, b=729*89h, D=ab=89^2*3^(2M+10).

Here A_*=81d_*-27c^2 and B_*=729e_*-243cd_*+54c^3.
The parameter map is injective, first solving for u from A and then
for v from B. All offsets, steps and D are fixed. L073 proves
every member nonsingular by its unit discriminant at 89 and gives

    N_fam(R)=4R^2/D+O_(c,h)(R+1).

In particular, for sufficiently large R its audited lower bound is

    N_fam(R)>=4R^2/D-4R/a-4R/b-4.                 (1)

Let B_Q(R) denote all nonsingular integral short coefficient pairs
with max(|A|,|B|)<=R. For m=120 and m=7 let X_m(R) be the pairs
in B_Q(R) whose image fails SL_2(Z/mZ) containment. Since
|B_Q(R)|<=(2 floor(R)+1)^2=O(R^2), the imported proposition gives
constants C_120,C_7>=0 and R_0 such that, for R>=R_0,

    |X_120(R)|<=C_120 R^(3/2) log R,
    |X_7(R)|<=C_7 R^(3/2) log R.                (2)

The constants may depend on the two fixed levels and the chosen norm;
they do not depend on R. The bounds are on the whole box, so they
also bound each intersection with this family, irrespective of any
distribution or correlation of its exceptions. In particular

    #bad family pairs
      <=|X_120(R) union X_7(R)|
      <=(C_120+C_7)R^(3/2)log R.                (3)

This is a union bound, not an independence assumption. Combining
(1) and (3), a sufficient strict threshold for a surviving family
pair is

    (C_120+C_7)log R/sqrt(R)
      +4/(aR)+4/(bR)+4/R^2 < 4/D.             (4)

Every term on the left tends to zero as R tends to infinity; the
right side is a fixed positive number. Hence (4) holds for all
sufficiently large R, also satisfying the lower-bound and theorem
thresholds. For each such R, (1) minus the right side of (3) is
positive, so there is a pair outside both exceptional sets.
No limit in M or h is taken, and no effective value of either the
torsion precision or the exceptional constants is needed.

For this single short model the image contains SL_2 at both levels.
The imported Q-case criterion gives full GL_2 at each level. The
pointed Q-map and its inverse induce G_Q-equivariant isomorphisms
of the entire torsion modules at both levels. They therefore
transfer both full-image conclusions to its one original member
E_star. A change of torsion basis only conjugates a full group.
This selects one member once, rather than choosing separate curves
for the two image requirements.

### Local retention for the selected member

Every original family cubic is monic, has degree three, and is
coefficientwise congruent to L044's f modulo 3^M. Thus the same
chosen member satisfies L044's application of Bisatt–Dokchitser,
*Tame torsion and the tame inverse Galois problem*, Math. Ann. 381
(2021), 1439–1453, [Theorem 2.2 and proof, p.1441](https://doi.org/10.1007/s00208-021-02173-y).
That theorem includes the 3-primary part of level 210; no
prime-to-three restriction is introduced. Its G_Q_3-equivariant
isomorphism on full 210-torsion restricts to the full 30- and
7-torsion and to the actual G_H. By L044's pointwise-kernel
argument it gives all 30-torsion H-rational and precisely
H(E_star[7])=N inside Omega. This is embedded-field equality, not
a comparison of degrees or an equality of curves.

Likewise L048's invariant congruence and split-node argument applies
to every original monic member at the fixed M>=31. Applying it
to E_star gives minimality, unit c4, discriminant valuation 30,
split multiplicative reduction over Q_3 and v_3(q_star)=30.
These conclusions concern the original cubic, not the scaled short
equation. The Tate parameter is that of this changed curve; it is
not identified with 3^30 or either old witness's parameter.

Finally the two mod-89 congruences hold for every original member.
L073's complete finite-field calculation identifies its reduction
with y^2=z^3+1 over F_89, with discriminant -432=13 modulo 89
and exactly 90 rational points. Hence it has good reduction there
and a_89=0. L073's cited reduction and Frobenius theorem gives,
for one actual arithmetic Frobenius lift sigma_star at a place of
this member, sigma_star^2=[-89] simultaneously on all of E_star[120].
In particular its square has the stated joint scalar action.
This is not a claim that a single preselected element works for all
family members. No new congruence or post-selection adjustment has
been imposed on E_star in any of these retention steps.

All approved tests pass: the quadratic count strictly exceeds the
union of the two subquadratic exceptional bounds, the coordinate
map is over Q, and the universal original-model congruences retain
all local assertions on that same member. The surviving count tends
to infinity, though distinct Q-isomorphism classes are not needed.

### Qualifications and possible downstream use

This establishes occurrence in the fixed family, not full image for
either previously selected curve. L085's conditional normality screen
could be applied only after its ordered-root and exactly generated
field construction is justified for an E_star choice; this proof does
not transfer any later auxiliary lemma or replace its G. The old
G,H,N and ATTEMPTS/034's failed cyclic separator are preserved.
Jones's discriminant-character relation retained in the assessment
does not certify or obstruct a specified old image here; the argument
uses the assessed fixed-composite-level count itself.

Independent initial data, a native input/action, all-image
factorization, marked pilot transport, essentiality and the original
finite B>=A remain unresolved. This is local progress by a cited
known method, not progress beyond the sources checked or a candidate
resolution of the IUT challenge. The separate audit below concerns
only the stated occurrence and retention result.

### Separate critical audit — 2026-10-19, step341

**Verdict and source scope.** The stated conclusion passes the prior
SPECIALIZE assessment
`drafts/literature/2026-10-19-auxiliary-simultaneous-occurrence-critical-audit.md`.
Reuse its primary-source coverage and the earlier occurrence assessment,
including Proposition 5.7 at the actual composite level 120 and at
level seven. The general theorems are imported without reproof; this
audit checks their constrained specialization. No changed hypothesis,
new general theorem or new direct lemma input is required. In particular,
k=Q is permitted by that proposition; an exclusion in an adelic theorem
is not imported here.

**Exact map and family.** Substitution into the homogeneous short
equation gives

    Y^2 Z-X^3-A XZ^2-B Z^3
      =729(y^2 z-x^3-c x^2 z-d xz^2-e z^3)

under (X,Y,Z)=(9x+3cz,27y,z). The extraneous coefficients cancel
as 243c^2-243c^2=0, 27c^3-81c^3+54c^3=0 and
243cd-243cd=0. The projective matrix has nonzero determinant 243,
inverse (x,y,z)=((X-3cZ)/9,Y/27,Z), and fixes [0:1:0].
The cited pointed-isomorphism criterion therefore applies over Q.
It induces equivariant group isomorphisms on full torsion at both
levels, including the 2- and 3-primary parts of 120. These are
characteristic-zero curve isomorphisms; the coefficients of the map
need not be units modulo a torsion prime. No integral isomorphism of
reduction models is asserted.

The triangular coefficient matrix has positive diagonal a=81*89h,
b=729*89h and determinant D=ab. Its first coordinate recovers u
and its second recovers v, so fixing c leaves two free parameters
and one parameter pair per coefficient pair. All offsets and steps
are fixed before R grows. Each original equation reduces, after
translation modulo 89, to y^2=z^3+1; its discriminant -432 is
13 modulo 89. Hence every family member is nonsingular, and the
rational map puts every counted coefficient pair in B_Q(R).

**Uniform interval errors and inequality (4).** Put x_R=2R/a,
y_R=2R/b. The first-coordinate interval contains S integers with
|S-x_R|<=2. For each such u the second-coordinate interval has
length y_R, regardless of its center. Its integer count T_u
satisfies |T_u-y_R|<=2. For P=sum_u T_u, therefore,

    |P-x_R y_R|
      <=sum_u |T_u-y_R|+y_R |S-x_R|
      <=2S+2y_R<=2x_R+2y_R+4.

This gives precisely (1), with no translation-dependent error or
omitted singular-model subtraction. Multiplying the imported
proportional exceptional bound by
|B_Q(R)|<=(2 floor(R)+1)^2 gives (2) after increasing fixed
constants and taking R>=max(R_0,2). An exception inside the family
is an exception in the entire box. The number surviving both tests
is consequently at least

    4R^2/D-4R/a-4R/b-4
       -(C_120+C_7)R^(3/2)log R.

Its strict positivity condition divided by R^2 is exactly (4).
With all constants and M fixed, the left side of (4) tends to zero
and 4/D is positive. The lower bound is thus positive for every
sufficiently large R; the integer count supplies at least one actual
pair in every such box. This checks the conclusion's quantifier.
No effective threshold, independence of exceptions, uniformity in M
or distinct-isomorphism-class count is used. Neither a marginal
prime-level theorem nor the cyclic Frobenius replaces level 120.

For this one pair the cited Q-case criterion upgrades SL_2
containment to GL_2 at both levels: its determinant is the full
cyclotomic character over Q. That base-field hypothesis would not
automatically hold over a torsion extension. The pointed map and
inverse conjugate the entire representations, transferring both full
images to the single original E_star.

**Full local modules and embedded fields.** The selected original
cubic remains monic of degree three and congruent to f modulo 3^M:
the offsets have their original classes and 89h u,89h v are
divisible by h. Thus L044's squarefree finite-torsion neighborhood
applies at the fixed M>=M_tors. Its cited theorem includes the
3-primary part and, through the pointed Jacobian identifications,
gives a G_Q_3-equivariant bijection on full 210-torsion. For n=30,7
the subgroup killed by n inside this module is precisely E[n].
Restriction to the actual G_H in Omega preserves these bijections.

For each sigma in G_H, equivariance and injectivity imply that it
fixes all source n-torsion exactly when it fixes all target n-torsion.
For n=30 the target action is trivial, so all E_star[30] is
H-rational. For n=7 the full pointwise kernels are identical
subgroups of G_H. Each fixes precisely its finite field generated
by both coordinates of every torsion point. The embedded fixed-field
correspondence and L044's target field therefore give H(E_star[7])=N
inside Omega. No curve isomorphism with E_q, degree comparison or
symplectic compatibility of the module isomorphism is needed.

**Original-model reduction and parameter.** L048's integral formulas
apply before the short-model coordinate change:

    c4=16c^2-48d,
    Delta=16(c^2 d^2-4d^3-4c^3 e-27e^2+18cde).

They preserve coefficient congruences modulo 3^M. The full Tate
product gives Delta(f)=3^30 U with U a unit, and M>=31 prevents
cancellation by Delta(g)-Delta(f). Hence v_3(Delta(g))=30.
The original coefficients give c=1,d=e=0 modulo 3, so c4 is a
unit. The cited general Weierstrass transformation laws imply that
any integral equation with smaller discriminant valuation would have
nonintegral c4. Thus this original equation is minimal. Its reduction
has unique affine singularity (0,0), tangent cone (y-x)(y+x), and
smooth origin at infinity. The two distinct F_3-rational tangents
verify the split multiplicative criterion in characteristic three.
The cited Tate theorem supplies this curve's q_star over Q_3;
the complete integral Tate expression for q_star j is a unit, giving
v_3(q_star)=-v_3(j)=30. This invokes only L048's universal local
conclusion, not its later global field constructions. Neither the
scaled short equation nor finite-torsion constancy alone is used to
deduce the original model's reduction or parameter valuation.

**The 89 assertion and one lift.** The compatible congruences give
the full reduced equation y^2=z^3+1. Since gcd(3,88)=1, cubing
is bijective on F_89. Each of the 89 values of y gives exactly one
affine point, and the projective curve has one infinity point.
Thus the count is 90 and a_89=0. Good reduction and 89 not
dividing 120 permit the cited reduction theorem on all three primary
parts E_star[8], E_star[3], E_star[5]. One arithmetic Frobenius
lift in one decomposition group acts through the same reduced
Frobenius on these parts. The cited identity pi^2+[89]=0 gives
sigma_star^2=[-89] simultaneously on all three, hence on their
sum E_star[120]. Finally -89=31 modulo 120. This is the
endomorphism identity itself, not a trace-only inference or separate
lifts on marginal modules.

All local properties hold universally on the original congruence
family before the survivor is selected. No further choice is hidden
in their retention. The audit validates this previously provisional
known-method input and finds no mathematical correction. The argument
assembly and direct inputs are unchanged. Application of L085 to newly
constructed fields is still separate. Both old witnesses and their fields, the cyclic stop,
independent initial-data and native applicability gaps, and the
original finite B>=A gap remain unresolved. No progress beyond the
checked source methods or formal verification is claimed.

## Mathlib

Full matching and supporting Mathlib coverage for this constrained
simultaneous occurrence result has not been checked. Unknown coverage
is not absence. The source theorem and existing local constructions
are imported with the qualifications above; the finite union and
strict asymptotic comparison are written out. No mathematical script,
numerical witness or formal-verification claim is used.
