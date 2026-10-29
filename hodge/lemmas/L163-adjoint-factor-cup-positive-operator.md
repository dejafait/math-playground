# L163 — Positive trace forms for the actual adjoint factor cup

## Hypotheses

Retain the complete conditional family of L071/L116/L117 on
X=S_1 x B, with identical marked projective K3 factors, their common
hyperkähler metric g and ordered triple (I,J_q,K_q). The hypothetical
locally free rank-two F is slope-polystable at the actual real product
class Omega, has integral c_1(F)=0 and

    ch(F)=2-14e_1-21e_2-tau_D+62e_1e_2.

Use L071's actual compatible unitary hyperholomorphic connection.
Put V=End_0(F), C=Rp_{2*}V, M_0=R^1p_{2*}V and W_0=R^2p_{2*}V.
These are the untwisted adjoint sheaves of L116/L117, not L147's
line-twisted sheaves. Retain their full finite, possibly empty split
set, actual triangle M_0[-1] -> C -> W_0[-2], inclusion j, and
trace retraction r. Write

    H=H^0(B,M_0), dim H=t,
    j_1:H -> H^1(X,V), j_3:H^2(B,M_0) -> H^3(X,V).

Both j_1 and j_3 are the actual isomorphisms induced by j. L117 gives
the actual J:H -> H^2(B,M_0), which is invertible, and Phi_1 with

    j_3 J=theta_2 cup j_1,   j_3 Phi_1=theta_1 cup j_1,
    K=J^{-1}Phi_1.

Here sigma_i=omega_{J_q,i}+i omega_{K_q,i}, and theta_i is the
pullback of [bar(sigma_i)]. Use this metric normalization on both
factors, so the sum is L117's product symplectic class. No independent
factor rotations, coefficient flatness, multiplicative splitting,
chosen value of t, or existence of F is assumed.

## Conclusion

There is a specified antilinear harmonic automorphism R of H^1(X,V)
with R^2=-Id. For the harmonic representatives alpha_u,alpha_v of
j_1u,j_1v define, with one common normalization,

    Q_i(u,v)=(1/8) integral_X sigma_1 wedge sigma_2 wedge theta_i
                                  wedge tr(alpha_u wedge R alpha_v).
                                                        (1)

In this integral theta_i means its actual closed form bar(sigma_i).
Both forms are Hermitian and positive definite when t>0, and satisfy

    Q_1(u,v)=Q_2(Ku,v).                                  (2)

Consequently K is self-adjoint and positive definite for Q_2; its
eigenvalues are real and strictly positive. In particular Phi_1 is
invertible and det(1+K)>0 in this normalization. For t=0 the vector
spaces are zero, all statements about nonzero vectors/eigenvalues
are vacuous and the determinant is 1.

The original derivation was a conditional local ADVANCE / REPRODUCTION
of the assessed harmonic and Serre framework. The separate critical
audit of 2026-10-25 (step 539) preserves the result, with outcome
EXPLORATION / REPRODUCTION and no substantive repair or stronger bound.
It strengthens L117's previously unevaluated entry but excludes no
allowed t, split cardinality or F. No independent incompatible
constraint, existence, transport, cycle construction or solution of
the Hodge conjecture is supplied.

## Proof

**Imported results and why this specialization is needed.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-25-adjoint-factor-cup-sign.md`, including
its exact covered target. Reuse M. Verbitsky, *Hyperholomorphic bundles
over a hyperkahler manifold*,
[alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993, Section 3's negative-adjoint real structure, PDF p. 11,
Section 4's real-operator convention, pp. 12–13, Theorem 4.1 and
Corollary 4.3 with its proof, pp. 15–16. They give harmonic preservation
for the quaternionic operator with parallel-real hyperholomorphic
coefficients. Definition 1.1, p. 2, allows the compact product and its
diagonal triple. No independent harmonic action for a factor is used.
The parallel projection to End_0(F) preserves the coefficient
connection and real structure. The source's scalar-ring shorthand,
middle-degree endpoint claim and any irreducible-base moduli theorem
are not inputs.

For harmonic Dolbeault representatives and coefficient Serre integration
use J.-P. Demailly, *L2 vanishing theorems for positive line bundles and
adjunction theory*,
[alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3),
28 February 1995, Section 4.A, (4.3)–(4.4'), PDF pp. 27–28.
X is compact Kähler and V is a holomorphic Hermitian vector bundle;
no flatness of its full connection is needed. The trace form identifies
V with V^vee: the scalar and trace-free parts of End(F) are orthogonal
and both nondegenerate in characteristic zero. Together with the
nowhere-vanishing holomorphic four-form sigma_1 wedge sigma_2 this
gives perfect Serre pairing H^3(X,V) x H^1(X,V) -> C. Its integration
normalization can be multiplied by any single nonzero constant.

These theorems do not give the two separate forms or the sign of K.
We compute the changed symmetric coefficient pairing explicitly;
L159's alternating determinant sign is not imported. The scalar-cup
identities and endpoint isomorphisms are the already proved actual
ones in L117, with L116's W_0 and retraction retained.

**The ordinary operator.** On coefficients let rho(A)=-A*, where *
is Hermitian adjoint for the actual unitary metric. It is parallel,
antilinear, isometric, trace-free preserving, and rho^2=Id. On scalar
(0,1)-forms put j_f(a)=J_q^*(bar(a)), where pullback on covectors is
J_q^*a(xi)=a(J_q xi). It is antilinear, isometric and j_f^2=-Id.
Define on the complex tensor product

    R(A tensor a)=rho(A) tensor j_f(a).                   (3)

The two antilinear factors make (3) balanced over C and antilinear
on the resulting tensor product; R^2=-Id. The cited theorem is
written for (p,0)-forms. Apply it to (-I,J_q,-K_q): its positive-type
forms and positive connection part are precisely the original
(0,p)-forms and bar-partial_V. The coefficient real structure is
the same rho. Its conjugate-J operator in degree one is (3), up to
an overall sign if covectors use the opposite convention. Equation
(3) fixes that sign uniformly on both factors. The theorem therefore
makes R preserve the ordinary Dolbeault harmonic forms for V.
It is an invertible antilinear map on H^1(X,V). No restriction of a
harmonic form to a fibre is claimed to be harmonic.

**The polarized frame calculation.** At either factor choose the
oriented real orthonormal frame (u,Iu,J_qu,K_qu), dual to
epsilon_0,...,epsilon_3, and put

    zeta_1=(epsilon_0+i epsilon_1)/sqrt(2),
    zeta_2=(epsilon_2+i epsilon_3)/sqrt(2).

The quaternionic multiplication rules give directly

    J_q^*zeta_1=-bar(zeta_2), J_q^*zeta_2=bar(zeta_1),
    sigma=2 zeta_1 wedge zeta_2,
    sigma wedge bar(sigma)=4 dvol.

For the component tangent to factor i, write
alpha_i=A bar(zeta_1)+B bar(zeta_2) and
beta_i=C bar(zeta_1)+D bar(zeta_2), with trace-free matrix
coefficients in a smooth unitary frame of F. Then

    R beta_i=C* bar(zeta_2)-D* bar(zeta_1),
    tr(alpha_i wedge R beta_i)
       =tr(AC*+BD*) bar(zeta_1) wedge bar(zeta_2)
       =(1/2)<alpha_i,beta_i> bar(sigma_i).                (4)

The inner product is the Hilbert–Schmidt coefficient metric and
covector metric, linear in the first argument. In particular its
diagonal is the sum of squared absolute matrix entries, not the
indefinite bilinear expression tr(A^2). The minus in rho and the
minus in j_f(bar(zeta_1)) cancel. This fixes the sign for both
factors without independent phase choices.

Decompose any harmonic alpha=alpha_1+alpha_2 by its cotangent
factor. R preserves these smooth cotangent summands. Wedging
tr(alpha wedge R beta) with theta_1 kills its first-factor and
mixed components, because that factor already has antiholomorphic
degree two. Thus only the component in factor two remains.
For theta_2 the roles are reversed. Holomorphic two-forms and the
antiholomorphic two-forms commute with each other with positive
exterior sign. Formula (4) and the product Riemannian volume give

    Q_1(u,v)=integral_X <alpha_{u,2},alpha_{v,2}> dvol_X,
    Q_2(u,v)=integral_X <alpha_{u,1},alpha_{v,1}> dvol_X.  (5)

Indeed each coefficient is (1/8)(1/2)(4)(4)=1. Both Q_i are
Hermitian positive semidefinite. Their radicals are exactly the
classes whose harmonic representatives have, respectively, zero
second and zero first component. Vanishing of the integral of a
continuous nonnegative squared norm forces pointwise vanishing.

All integrals in (1) are actual cup/trace pairings. The representatives
alpha and R beta are bar-partial_V closed, the trace pairing is
holomorphic, and theta_i and sigma_1 wedge sigma_2 are closed.
Replacing a closed representative by a bar-partial-exact one changes
the integral by an exact top-degree integral, which vanishes by
Stokes on compact X. R on a cohomology class is defined using its
unique harmonic representative; it is not applied arbitrarily to
an exact representative and asserted to descend as a chain map.

**Both radicals vanish.** First consider Q_2. If u is in its
radical, (1) says that theta_2 cup j_1u pairs to zero with Rj_1v
for every v in H under the perfect coefficient Serre pairing.
Both R and j_1 are surjective, so theta_2 cup j_1u=0. The actual
identity theta_2 cup j_1u=j_3 Ju and invertibility of j_3 and J
give u=0. A finite-dimensional positive semidefinite Hermitian
form with zero radical is positive definite. Equivalently, the
radical description in (5) and this argument show that no nonzero
harmonic class can have only its second-factor component.

For Q_1 a further geometric input matters. L071 gives polystability
of every second-factor restriction E_x=F|_{ {x} x B}, of charge 21,
at the original real h. Its split alternatives have charges 14r^2.
Since 21 is not such a charge, every E_x is stable. Import stable
simplicity from D. Huybrechts, *Lectures on K3 Surfaces*,
prepublication copy (2015 draft), Chapter 9 Section 3.1, Definition 3.1
and fact iii), printed/PDF pp. 175--176, in the inspected
[449-page primary-text mirror](https://ncatlab.org/nlab/files/HuybrechtsLecturesOnK3.pdf#page=175).
Its slope definition permits this real Kähler class h; no rational
polarization replacement is needed. Hence every holomorphic endomorphism
of E_x is scalar. In characteristic zero a scalar rank-two endomorphism
has trace zero only when it is zero, giving H^0(B,End_0(E_x))=0.
This imports the general theorem and checks its precise applicability;
it is not a vanishing theorem for the product coefficient.

Now suppose Q_1(u,u)=0. By (5), the harmonic representative alpha
has alpha_2=0. The product decomposition of the Dolbeault differential
on V is bar-partial_1+bar-partial_2. In bar-partial_V alpha=0 the
terms bar-partial_1 alpha_1 and bar-partial_2 alpha_1 have different
cotangent bidegrees, (2,0) and (1,1). Thus
bar-partial_2 alpha_1=0. Fix x in S_1 and a vector in T_x^{0,1}S_1.
Evaluating alpha_1 on that vector gives a smooth section of
End_0(E_x) on B, and this equality makes it holomorphic. The
preceding vanishing makes every such section zero. For every x
and vector, therefore, alpha_1 is zero. Hence alpha=0 and u=0.
This uses neither coefficient flatness nor fibrewise harmonicity.
It proves Q_1 positive definite, including its full radical test.

**Comparison with the actual operator.** Define

    S(z,w)=(1/8) integral_X sigma_1 wedge sigma_2
                                      wedge tr(z wedge Rw)

on H^3(X,V) x H^1(X,V), using any closed representatives of z and
Rw. It is a nondegenerate sesquilinear pairing by Serre duality
and invertibility of R. All cup degrees theta_i are even, so

    Q_i(u,v)=S(theta_i cup j_1u,j_1v).

L117's actual identities now give, without any change of endpoint
identifications,

    Q_1(u,v)=S(j_3 Phi_1u,j_1v)
            =S(j_3 JKu,j_1v)=Q_2(Ku,v).

In particular r[2]ell_1j is still the actual global Ext^2 entry.
It has not been set to zero by a fibre calculation. The finite
supported W_0 stays in the triangle: L116/L117 prove that j gives
both endpoint isomorphisms even with W_0 present. Nothing here
removes W_0 from C or assumes the splitting is multiplicative.

Finally Hermiticity gives

    Q_2(Ku,v)=Q_1(u,v)=overline(Q_1(v,u))=Q_2(u,Kv).

For u nonzero, Q_2(Ku,u)=Q_1(u,u)>0. The finite-dimensional
Hermitian spectral theorem makes K diagonalizable with positive
real eigenvalues. This proves the assertions about invertibility
and determinant. When H=0 the same identities hold on zero spaces.
No positive lower bound uniform over hypothetical F is asserted.
Positive eigenvalues are consistent with, and strengthen rather
than contradict, L117's condition det(1+K)!=0. Additional geometry
would be needed to turn this restriction into an exclusion.

**Separate critical audit, 2026-10-25 (step 539).** The prior SPECIALIZE
assessment is
`drafts/literature/2026-10-25-adjoint-factor-cup-critical-audit.md`.
This checks the displayed specialization using L071/L116/L117 as
retained inputs, rather than re-proving their ancestors. The general
operator, Dolbeault and Serre theorems above are reused, not reproved.
The stable-simple passage now cites the exact inspected real-Kähler
statement; its earlier elementary rank-two verification was sound.

First, (3) is well-defined on the complex tensor product: replacing
(A,a) by (cA,a) or (A,ca) gives in either case bar(c) times its image.
This verifies antilinearity, not complex linearity. Squaring gives
rho^2 tensor j_f^2=-Id. The triple (-I,J_q,-K_q) satisfies the
quaternionic relations and uses the same metric and unitary connection;
its (p,0) forms are the original (0,p) forms. Hyperholomorphicity and
the parallel negative-adjoint involution meet the cited harmonic
operator hypotheses for this triple. Reversing a covector-action
convention can only introduce the common degree-one minus, fixed by
(3); it cannot justify separate signs on the factors.

Second, in the stated oriented frame one has
J_q^*epsilon_0=-epsilon_2, J_q^*epsilon_1=epsilon_3,
J_q^*epsilon_2=epsilon_0 and J_q^*epsilon_3=-epsilon_1.
These give the two zeta identities and sigma=2 zeta_1 wedge zeta_2.
Also zeta_1 wedge bar(zeta_1)=-i epsilon_0 wedge epsilon_1 and
zeta_2 wedge bar(zeta_2)=-i epsilon_2 wedge epsilon_3; the one
interchange of bar(zeta_1) with zeta_2 therefore gives
sigma wedge bar(sigma)=4 dvol, with positive sign. Combining
rho(C)=-C* with J_q^*zeta_1=-bar(zeta_2) gives precisely the
positive tr(AC*+BD*) in (4). Mixed cotangent components vanish
after theta_i is inserted by antiholomorphic degree, and all
remaining two-form interchanges have positive sign. Thus the
single factor (1/8)(1/2)(4)(4)=1 verifies both polarized identities
(5), not merely their diagonal signs.

Third, a zero Q_2 diagonal gives a radical vector by (5).
The pairing with every Rj_1v then detects theta_2 cup j_1u by
perfect Serre duality: trace is nondegenerate on the trace-free
rank-two coefficient, the canonical four-form is nowhere zero,
and Rj_1 is onto. L117's actual J and j_3 force u=0. For Q_1,
the other component vanishes pointwise, and the mixed part of the
single equation bar-partial_V alpha=0 is bar-partial_2 alpha_1=0.
Upon fixing x and a cotangent evaluation, this is the holomorphic
section equation for End_0(E_x), with no derivative in the first
factor. Charge 21 excludes every split charge 14r^2, including zero;
L071's restrictions are polystable at every x, not merely generic x.
The cited simplicity theorem therefore kills each such section at
every x. No extension across an exceptional fibre or restricted
harmonic representative is needed. These are distinct valid radical
arguments, rather than strictness inferred from the total norm alone.

Finally, the actual endpoint identifications deserve an explicit
boundary check. For M_0[-1] -> C -> W_0[-2], the terms adjacent to
j_1 from W_0 are H^{-2}(W_0) and H^{-1}(W_0), both zero. At j_3
the relevant sequence is H^0(W_0) -> H^2(M_0) -> H^3(X,V)
-> H^1(W_0). The first arrow is zero by L116's actual retraction
and vanishing truncation boundary; the last group is zero by finite
support. Thus the same j induces both isomorphisms even when W_0
is nonzero. L117's global factorization and even-degree scalar
naturality then give exactly j_3 Phi_1=theta_1 cup j_1 and
j_3 J=theta_2 cup j_1. In the common Serre pairing these yield
(2) with no extra sign or change of endpoint bases. A harmonic
representative for theta_i cup alpha is unnecessary: closed
representatives suffice for that pairing. W_0 still contributes
to degree two; no multiplicative splitting is asserted.

The audit therefore preserves positive self-adjoint K and its
spectral consequences, including the vacuous t=0 case. It supplies
no additional numerical estimate, contradictory eigenvalue, or
actual F. ATTEMPTS/069's unsupported-local-entry stop and
ATTEMPTS/089,/090,/091's other obstructions remain unchanged.
The audit is a completed mathematical check, classified REPRODUCTION;
no progress beyond the assessed general sources is claimed.

## Mathlib

Full matching Mathlib coverage for the coefficient harmonic operator,
the actual derived cup comparison and this product-family positivity
has not been checked. The finite-dimensional Hermitian spectral theorem
is a standard supporting result; no specific Mathlib theorem match is
claimed here. Unknown coverage is not absence. This is an informal
conditional specialization, not a formal verification, certified novelty
claim, or complete Hodge-conjecture candidate. The separate informal
critical audit above checks the operator convention, strictness and
actual-map comparison; it is not a formal verification or a new audit
of all earlier lemmas.
