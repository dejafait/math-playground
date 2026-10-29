# L180 — Polarized rank-two trace cups exclude the proposed endpoint

## Hypotheses

Retain the complete conditional family and actual maps of L116, L163
and L165. Thus X=S_1 x B consists of the identical marked projective
K3 factors with their common hyperkähler metric, ordered triple,
holomorphic forms sigma_1,sigma_2 and compatible connection. The
hypothetical locally free rank-two bundle F is slope-polystable at
the original real product class, has integral c_1(F)=0 and full character

    ch(F)=2-14e_1-21e_2-tau_D+62e_1e_2.

The full mixed tensor and marking are retained, not replaced by
numerical Chern data. Put V=End_0(F), p:X -> B, M=R^1p_*V and
W=R^2p_*V. Use the actual truncation inclusion j, trace-adjoint
retraction r and top projection a. The split set Z is finite and
reduced, and W has length one at each point of Z. Impose the approved
test endpoint

    s=|Z|=781,   H=H^0(B,M),   t=dim H=46.

L116 gives the actual isomorphism j_1:H -> H^1(X,V) and
E=H^2(X,V) of dimension 724+2t=816, with W retained. Use the
unhalved graded Yoneda bracket and L165's complex bilinear Serre
form Q on E. In L163's normalization, theta_i=[bar(sigma_i)].
Its specified harmonic antilinear map R has R^2=-1, its two actual
factor forms Q_1,Q_2 are strictly positive Hermitian forms, and
K=J^{-1}Phi_1 satisfies Q_1(u,v)=Q_2(Ku,v).

No section integrability, multiplicative Leray splitting, harmonicity
of products, metric compatibility of j or r, independent factor
harmonic action, or existence of this endpoint is assumed. R is
used only on harmonic representatives of degree-one cohomology.

## Conclusion

Let

    beta:Sym^2 H -> E,   beta(u odot v)=[j_1u,j_1v],
    G(x,y)=Q(beta(x),beta(y)).

The actual scalar trace cups and the rank-two coefficient identity
would force G to be nondegenerate. Consequently the hypothetical
endpoint would require

    rank G = dim Sym^2 H = 46*47/2 = 1081 > 816 = dim E,

which is impossible for a pulled-back bilinear form. Therefore no
F satisfying all the stated hypotheses has s=781,t=46.

This is a conditional local ADVANCE / REPRODUCTION of the assessed
trace and harmonic tools (step 606, 2026-10-29). The separate conceptual
audit (step 609, 2026-10-29) preserves the specialization and endpoint
exclusion, with outcome EXPLORATION / REPRODUCTION and no substantive
repair or stronger bound. The result
is not a new general matrix identity or a certified originality claim.
It tests every actual endpoint datum, not only L179's particular
finite witness. L179 remains a valid model for its smaller checklist.
No conclusion about other s,t is derived in this step, and no
construction or exclusion of F throughout the family, transport,
primitive cycle realization or Hodge-conjecture resolution follows.

## Proof

**Imported tools and the required specialization.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-28-rank-two-polarized-bracket-gram.md`.
Import the ordinary traceless 2-by-2 coefficient identity from
S. A. Vasyutkin and A. P. Chupakhin, *Constructing a Minimal Basis of
Invariants for Differential Algebra of 2 x 2 Matrices*, J. Appl. Ind.
Math. **16** (2022), 356–364, Section 2, traceless display following
(6), with equations (1),(4) and Assertion 1, pp.357–359,
[DOI 10.1134/S1990478922020156](https://doi.org/10.1134/S1990478922020156),
[inspected author text](https://www.researchgate.net/publication/365419265_Constructing_a_Minimal_Basis_of_Invariants_for_Differential_Algebra_of_2times_2_Matrices):

    2 tr(ABCD)=tr(AB)tr(CD)+tr(AD)tr(BC)-tr(AC)tr(BD).    (1)

Here A,B,C,D are ordinary traceless complex 2-by-2 matrices.
The coefficient-level polarized Cayley–Hamilton framework is also
covered by C. Procesi, *The invariant theory of n x n matrices*,
Adv. Math. **19** (1976), 306–381, Section 4, Corollary 4.4(c) and
Theorem 4.6 with their proofs, pp.319–323,
[primary text](https://abrochier.org/m2/Procesi.pdf#page=14).
Neither theorem is reproved or applied ungraded to odd forms.

For composition, graded commutators, the differential derivation
rule and graded trace, use E. Lepri and M. Manetti, *Connections and
L-infinity liftings of semiregularity maps*,
[arXiv:2102.05016v3](https://arxiv.org/pdf/2102.05016v3#page=3),
22 May 2021, Section 2, pp.3–4, Lemma 2.6 and proof, pp.6–7,
Definition 3.1/(3.2) and Example 3.3, pp.7–8. F is locally free
and is concentrated in internal degree zero, so its coefficient
trace is ordinary matrix trace; Dolbeault degree supplies the signs.
These tools do not assert the Gram rank below. The necessary
specialization is (1) with its exterior signs, followed by comparison
with L163's actual cups and a finite-dimensional rank argument.

**The four odd inputs.** For V-valued (0,1)-forms alpha,beta,gamma,
delta, write T(alpha,beta)=tr(alpha wedge beta). Graded trace gives
T(beta,alpha)=-T(alpha,beta). Expand the four forms in local frames
and apply (1) only to the degree-zero matrix coefficients. The
exterior order for the three scalar products on its right is,
respectively,

    alpha beta gamma delta: +1,
    alpha delta beta gamma: +1,
    alpha gamma beta delta: -1.

The last exterior sign cancels the minus in (1). Coefficientwise
multilinearity therefore gives the identity of scalar (0,4)-forms

    2 tr(alpha beta gamma delta)
      =T(alpha,beta)T(gamma,delta)
       +T(alpha,delta)T(beta,gamma)
       +T(alpha,gamma)T(beta,delta).                    (2)

Products here and below include exterior product and, for
endomorphism-valued factors, composition. The coefficient argument
includes coincident covector indices: the resulting repeated-index
exterior monomials vanish on both sides. It is thus an identity for
all forms, not just decomposable forms with distinct indices.

For completeness set P=T(alpha,beta)T(gamma,delta),
U=T(alpha,gamma)T(beta,delta), V_0=T(alpha,delta)T(beta,gamma).
The four rows of (2) in the bracket expansion are

    2 tr(alpha beta gamma delta) =  P+U+V_0,
    2 tr(beta alpha gamma delta) = -P+U+V_0,
    2 tr(alpha beta delta gamma) = -P+U+V_0,
    2 tr(beta alpha delta gamma) =  P+U+V_0.

Indeed all T's have even degree and commute, while interchanging
their two arguments negates them. The unhalved bracket of two
degree-one forms is [alpha,beta]=alpha beta+beta alpha. Its trace
is zero, so it is V-valued. Summing the four rows gives

    tr([alpha,beta][gamma,delta])
      =2(T(alpha,gamma)T(beta,delta)
          +T(alpha,delta)T(beta,gamma)).                (3)

There is no distinct-input restriction. For example the repeated
case gives tr([alpha,alpha][gamma,gamma])=4T(alpha,gamma)^2;
taking gamma=alpha makes both sides zero. Thus the usual diagonal
cyclicity identity is respected, without forcing the pairing between
different brackets to vanish.

**Descent and actual scalar cups.** The Dolbeault differential on
End(F)-valued forms is a graded derivation, and trace commutes with
it. Products of closed forms are closed; replacing one closed input
by an exact one changes its product or bracket by an exact form.
The same assertions hold for V since trace-free projection commutes
with the differential. Thus (3) descends to the actual cohomological
products. Integration against the closed form sigma_1 wedge sigma_2
is unchanged by an exact top-degree term on compact X.

For u,v in H define the scalar cohomology class

    tau(u,v)=tr(j_1u cup j_1v) in H^2(X,O_X).

This is alternating. The Dolbeault Kunneth theorem and
H^1(S_i,O)=0, H^2(S_i,O)=C theta_i for K3 surfaces give uniquely
defined alternating complex bilinear forms omega,eta on H with

    tau(u,v)=omega(u,v)theta_1+eta(u,v)theta_2.           (4)

In this actual scalar cohomology ring theta_1^2=theta_2^2=0 and
theta_1 theta_2 generates H^4(X,O_X). This uses no decomposition
of the End(F)-valued cohomology algebra.

Put Omega_hol=sigma_1 wedge sigma_2 and

    T_0=integral_X Omega_hol wedge theta_1 wedge theta_2.

In L163's common metric normalization sigma_i wedge bar(sigma_i)
=4 dvol_i, and interchanging two 2-forms has positive sign. Hence
T_0=16 Vol(X)>0. Transfer only the degree-one harmonic map to H:

    R_H=j_1^{-1} R j_1.

It is an antilinear bijection. Formula (4) in L163's definitions of
Q_i, with exactly the same representatives and the actual j_1, yields

    Q_2(u,v)=(T_0/8) omega(u,R_H v),
    Q_1(u,v)=(T_0/8) eta(u,R_H v).                       (5)

The reversal of the indices is essential: wedging with theta_2
selects the theta_1 coefficient, and conversely. The formulas do
not assert that R preserves products or that those products are
harmonic.

If omega(u,w)=0 for every w, surjectivity of R_H and (5) give
Q_2(u,v)=0 for every v. Positive definiteness of Q_2 gives u=0.
Thus omega is nondegenerate. The actual equality
Q_1(u,v)=Q_2(Ku,v), again with surjective R_H, gives

    eta(u,w)=omega(Ku,w) for every u,w in H.             (6)

L163 proves that K is diagonalizable over C with strictly positive
real eigenvalues. No eigenvalue or eigenbasis is prescribed here.
Alternation of eta also gives
omega(Ku,w)=omega(u,Kw); this is compatible with the complex
bilinear forms and is distinct from Hermitian self-adjointness.

**The symmetric-square form.** Write u odot v for
(u tensor v+v tensor u)/2. Define a symmetric bilinear form on
Sym^2 H by

    A_2(u odot v,w odot z)
      =omega(u,w)omega(v,z)+omega(u,z)omega(v,w).        (7)

Here and in the following calculation the notation beta denotes the
cohomological bracket map in the conclusion, not a form input of (2).
L165's Serre form is

    Q(x,y)=c_X integral_X Omega_hol wedge tr(x cup y)

for one nonzero normalization constant c_X. Its fixed trace
conventions only change this common constant. Applying (3),(4)
and theta_i^2=0 gives

    G(u odot v,w odot z)=2 c_X T_0 [
        omega(u,w)eta(v,z)+eta(u,w)omega(v,z)
       +omega(u,z)eta(v,w)+eta(u,z)omega(v,w)].          (8)

Define the operator D on Sym^2 H by

    D(u odot v)=Ku odot v+u odot Kv.

Substitution of (6) into (7) now proves, with every constant retained,

                     G(x,y)=2 c_X T_0 A_2(Dx,y).       (9)

There is no comparison between metric and Leray orthogonal
complements in this calculation; it occurs on X before any relative
interpretation of degree two.

We verify both nondegeneracy and invertibility rather than infer
them from a diagonal quartic. On H tensor H the form

    B(u tensor v,w tensor z)=omega(u,w)omega(v,z)

is nondegenerate because omega:H -> H^* is an isomorphism and its
tensor square is an isomorphism. B is symmetric, and the flip of
the tensor factors is self-adjoint for B. Its +1 and -1 eigenspaces
are therefore B-orthogonal. They are Sym^2 H and wedge^2 H and
sum to H tensor H over C. A vector of Sym^2 H in the radical of
the restricted form is consequently orthogonal to all H tensor H,
so is zero. Since A_2 is twice that restriction, A_2 is nondegenerate.

Choose an eigenbasis e_1,...,e_46 for the actual K, with eigenvalues
lambda_i>0 supplied by L163. The vectors e_i odot e_j, i<=j,
form a basis of Sym^2 H and have D-eigenvalues lambda_i+lambda_j.
All these sums are strictly positive, including i=j, so D is
invertible. Equation (9) and c_X T_0 != 0 imply that G is
nondegenerate on all of Sym^2 H.

**The endpoint contradiction and its limits.** If beta(x)=0,
then G(x,y)=0 for every y. The established nondegeneracy forces
x=0, so beta would be injective. Equivalently any pullback form
has rank at most the dimension of its target. Here this requires

    1081=46*47/2=rank G <= dim E=724+2*46=816,

an excess of 265, a contradiction. The ambient dimension includes
all point-supported contributions through L116; it is not
724-s+2t. Removing those contributions or imposing semiregularity
would be unnecessary additional constraints.

The argument holds for every datum under the approved endpoint
hypotheses. L179's zero pairings between all bracket coefficient
vectors therefore cannot be the actual multiplication together
with (1)–(6); the conclusion is stronger than refuting that one
model. No premise from that model is used. The stopped
scalar-isotropy, cyclicity and unsupported metric/Leray mechanisms
remain stopped. This argument has not tested other parameters or
the existence of cycles, so it supplies no complete main-target
candidate. Its graded specialization, actual-cup comparison and
rank argument are checked in the separate audit below.

**Separate conceptual audit, 2026-10-29 (step 609).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-29-rank-two-bracket-gram-critical-audit.md`.
The audited target is exactly the endpoint s=781,t=46. We retain
L116, L163 and L165 with their stated hypotheses and earlier audits;
this is not a new audit of every ancestor. L117 enters through L163.
The primary matrix, graded-product and harmonic/Serre results cited
above and the assessment's inspected proof cases are reused. No new
source hypothesis or theorem is needed for this specialization.

First check the coefficient-to-form passage independently. For one
term alpha=Aa, beta=Bb, gamma=Cc, delta=Dd, put
p=tr(AB)tr(CD), u=tr(AC)tr(BD), v=tr(AD)tr(BC), and use abcd as
the common exterior order. The imported coefficient identity gives
2tr(ABCD)=p-u+v. The three scalar-form products P,U,V_0 in the
proof have respective abcd coefficients p,-u,v: adbc is an even
permutation, whereas acbd is odd. Hence (2) has all three positive
signs, not the ungraded matrix signs. For the four bracket words,
the coefficients expressed in these same scalar-form products are

    abcd:  P+U+V_0,       bacd: -P+U+V_0,
    abdc: -P+U+V_0,       badc:  P+U+V_0.

The second and third rows each reverse the first trace pair or the
second pair; the remaining two products interchange and commute,
since their degree is two. The fourth reverses both pairs. Summing
these rows and dividing by 2 gives precisely the coefficient 2 in
(3). Equivalently, on these decomposable terms the two brackets
have coefficients AB-BA and CD-DC, and (3) has abcd coefficient
2(v-u), consistently with the same imported identity in the four
matrix orders. This check uses no commutativity of the coefficients.

Each side is separately multilinear in the four matrix-valued
forms, so expansion proves the identity for arbitrary forms even
when their component indices or entire inputs coincide. Repeated
exterior indices contribute zero. For alpha=beta and gamma=delta,
(3) gives 4T(alpha,gamma)^2; with all inputs equal it gives zero,
since graded trace makes T(alpha,alpha)=0. Trace-free closure also
follows from T(alpha,beta)+T(beta,alpha)=0. Thus the unhalved
bracket defines a complex-linear map on the whole Sym^2 H, with
no constraint that a degree-one class be integrable.

Second, all quantities descend to the claimed cohomology groups.
In a holomorphic frame the Dolbeault differential is a derivation
of the endomorphism product, and trace commutes with it. For a
closed degree-one beta and a degree-zero endomorphism f,
[bar-partial f,beta]=bar-partial[f,beta]; the corresponding scalar
cup difference is bar-partial tr(f beta). Applying the derivation
rule to each further closed factor treats the four-input identity.
Trace invariance under frame conjugation makes the local identities
global. Stokes, with the closed holomorphic volume form on compact
X, removes every resulting exact top term. The Kunneth decomposition
used in (4) is only that of scalar Dolbeault cohomology: K3 H^1(O)=0,
and its factor H^2(O) lines have generators theta_1,theta_2. Their
squares vanish by dimension, and their product is nonzero. None of
these statements splits the V-valued multiplication.

For the actual cup comparison, the harmonic representative of
j_1 R_H v is exactly R alpha_v, by the definition of R_H and L163's
harmonic preservation. Thus inserting (4) into L163's actual
integrals gives (5), with no representative change hidden inside R.
The theta_2 insertion selects omega, and theta_1 selects eta.
All interchanges of the degree-two scalar forms have positive sign;
sigma_i bar(sigma_i)=4 dvol_i gives T_0=16 Vol(X)>0. The same
factor T_0/8 occurs in both equations. Surjectivity of the single
R_H and strict positivity of Q_2 prove nondegeneracy of omega.
The equality Q_1=Q_2(K-,-) gives eta=omega(K-,-) on every pair,
not merely on a diagonal. L163 supplies the actual K with positive
real spectrum: Q_2 is strict using the actual J and j_3, while Q_1
is strict using stable second-factor restrictions of charge 21.
Those hypotheses are retained here. Neither arbitrary positive
forms nor independent harmonic operators have been substituted.

Third, the form Q in L165 is the actual trace/evaluation Serre form
on X with the fixed volume trivialization. Changing its trace
normalization supplies one common nonzero c_X; it cannot alter the
relative coefficients in (8). The degree-two classes commute, so
the theta_1 theta_2 coefficient of a product of the two scalar
cups is omega eta+eta omega with no further minus. Formula (3)
therefore gives exactly the four terms of (8). On the symmetric
tensor convention u odot v=(u tensor v+v tensor u)/2, the tensor
form B satisfies

    B(u odot v,w odot z)=A_2(u odot v,w odot z)/2.

Its flip is self-adjoint, its symmetric and alternating eigenspaces
are orthogonal, and they span the full tensor square in characteristic
zero. Nondegeneracy of B therefore implies nondegeneracy on each
eigenspace, in particular of A_2. Substituting eta=omega(K-,-)
in the four terms gives G=2c_X T_0 A_2(D-,-) with the displayed D.
For an eigenbasis of the actual K, D has eigenvalues lambda_i+lambda_j
on e_i odot e_j, i<=j. Strict positivity excludes zero for every
sum, including repeated indices. Hence G is nondegenerate. Its
vanishing on some decomposable diagonals does not produce a radical
and does not invalidate this full bilinear calculation.

Finally, L116 gives h^0(M)=h^0(N)=t because H^0(T_B)=0, and the
actual j_1 identifies this entire space with H^1(X,V). Its split
truncation gives h^2(X,V)=h^1(M)+h^0(W)=(724-s+2t)+s. At the
tested endpoint the two contributions are 35 and 781, hence 816.
No quotient, semiregularity kernel or point-free subspace replaces
E. The bracket is defined for every pair in H, and the universal
property of Sym^2 makes beta a linear map on a space of dimension
46*47/2=1081. For the pullback form, its linear map to the dual
factors as beta^vee Q^flat beta; its rank is at most dim E=816,
whether or not beta is surjective. The proven rank is 1081, an
excess of 265. This is the stated conditional contradiction.

All audited comparisons survive without substantive correction.
This completed check is EXPLORATION / REPRODUCTION, not a new bound
or new mathematics beyond the assessed sources. It excludes the
specified endpoint for every datum satisfying the hypotheses, not
just L179's formal witness. That witness and the distinct stops in
ATTEMPTS/057,/090,/092--096 remain intact. No claim for another t
or s, family-wide nonexistence, cycle construction or the main Hodge
target is established by this endpoint audit.

## Mathlib

Full matching Mathlib coverage for this graded rank-two trace
specialization with actual harmonic factor cups and endpoint
comparison has not been checked. Tensor and symmetric-power linear
algebra and the Hermitian spectral theorem are supporting standard
facts, not a claimed full matching formal theorem. The finite
linear-algebra arguments needed here are written out above; the
general source identities and L163 are imported with their stated
hypotheses. Unknown coverage is not absence. No Lean verification,
certified novelty or complete Hodge resolution is claimed. The
separate informal conceptual audit above verifies this specialization
conditional on its retained inputs; it is not a formal verification
or a fresh audit of the entire ancestry.

