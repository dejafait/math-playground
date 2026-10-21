# L101 — Complex two-parameter realization of the split-line first jet

## Hypotheses

Use the actual marked projective K3 surface S, fixed complex structure I,
hyperkähler metric g and real Kähler class h in audited L094. In particular
L is the holomorphic line bundle with integral class k, k^2=-14 and
k.h=0, and E=L direct sum L^{-1} has its determinant-one direct-sum
Hermite--Einstein connection A. Fix the multiplication trivialization
epsilon of det E. No product bundle F is assumed.

Use L094's real harmonic quaternionic operators I,J,K and its choice of
orthonormal positive-weight vectors e_1,e_2. Put v=e_1+Je_2 and
W=span_R(v,Iv,Jv,Kv). For a real skew-adjoint harmonic one-form w,
write B(w)=w^{0,1}. L094 proves B(Iw)=iB(w). Set

\[
b_1=B(v),\qquad b_2=B(Jv),\qquad
\ell(s,t)=s b_1+t b_2.                                      \tag{1}
\]

The prescribed identification T_0 C^2 with W sends the ordered real
basis (partial_Re s,partial_Im s,partial_Re t,partial_Im t) to
(v,Iv,Jv,Kv). It fixes the scale as well as the plane.

## Conclusion

There is a neighborhood U of zero in C^2 and an actual holomorphic
locally free rank-two family E_U on S times U, with an identification
of its central fibre with E and a holomorphic determinant trivialization
restricting to epsilon. Its Kodaira--Spencer map at zero sends
partial_s to [b_1] and partial_t to [b_2]. It is injective and realizes
exactly the prescribed first jet (1). In a smooth determinant-preserving
trivialization, its fibre Dolbeault operators have first-order term
ell(s,t), not merely a differently normalized cohomology basis.

This is a local ADVANCE / REPRODUCTION of the assessed formality, slice
and approximation tools. The separate critical audit below preserves it. There is
no assertion of a unitary ASD family at g, quaternionic integration,
punctured stability, an algebraic family over U, a common kernel F,
the global mixed class, original-image separation or transport. Those
independent gaps and universal primitive Hodge realization remain open.

## Proof

**Imported theorems and their scope.** Import Bandiera--Manetti--Meazzini,
*Formality conjecture for minimal surfaces of Kodaira dimension 0*,
Compositio Math. 157 (2021), 215--235,
[1907.10690v2, 2 August 2020](https://arxiv.org/pdf/1907.10690v2),
Theorem 5.1, p. 15, and Theorem 2.3, pp. 5--6. The former gives formal
derived endomorphisms for a coherent sheaf with linearly reductive
automorphisms on a complex projective surface with trivial canonical
bundle. The latter transfers formality to an injective DG Lie subalgebra
whose inclusion has a DG-module splitting over that subalgebra. Use also
the Maurer--Cartan/quasi-isomorphism interpretation recalled in Section 1,
p. 2. These general results are imported rather than reproved.

Import Buchdahl--Schumacher, *Polystable bundles and representations of
their automorphisms*, Complex Manifolds 9 (2022), 78--113,
DOI 10.1515/coma-2021-0131,
[Proposition 2.6 and (2.4), pp. 83--84](https://d-nb.info/1262812674/34).
Use its finite holomorphic obstruction equations for the fixed compact
Kähler metric and the polystable bundle E, at Sobolev exponent p>4.
Import Michael Artin, *On the solutions of analytic equations*, Invent.
Math. 5 (1968), 277--291, Theorem (1.2), p. 277, in its multivariable
form also stated in Guillaume Rond, *Artin approximation*, J. Singularities
17 (2018), 108--192,
[Theorem 2.1, p. 122, proof reductions pp. 123--126](https://www.journalofsingularities.com/volume17/rond.pdf).
The saved source review inspected Rond's statement and relevant proof
reductions; it did not newly retrieve Artin's original full proof.
Convergent equations over C and a formal solution permit a convergent
solution agreeing modulo any prescribed power of the parameter ideal.
Only agreement modulo (s,t)^2 is used here.

The ready assessment covers these exact hypotheses. The following work
justifies determinant restriction, quadratic comparison and jet matching;
it does not reprove the general theorems or import a quaternionic chart.

**Determinant-fixed formality.** Put d=bar-partial_A and
M=A^{0,*}(S,End_0 E), with the graded commutator bracket. L094 gives
H^0(L^{+/-2})=H^2(L^{+/-2})=0, H^1(O_S)=0, and both off-diagonal
H^1 dimensions equal to 26. Consequently Aut(E)=(C*)^2: the only
holomorphic automorphisms are independent nonzero diagonal scalars.
This is linearly reductive. S is projective and has trivial canonical
bundle, so BMM Theorem 5.1 applies to its full endomorphism DG Lie model
A^{0,*}(S,End E), which represents derived endomorphisms since E is
locally free.

Trace gives the coefficient decomposition

\[
A^{0,*}(End E)=M\oplus A^{0,*}(O_S)\operatorname{id},
\quad P(x)=x-\tfrac12\operatorname{Tr}(x)\operatorname{id}.    \tag{2}
\]

The differential commutes with P. The bracket of a trace-free
coefficient form and a scalar coefficient form is zero, with the
graded wedge sign included. Graded commutators have trace zero, so
M is a DG Lie subalgebra and P is an M-module morphism. Thus (2)
is a DG-module splitting and BMM Theorem 2.3 proves formality of M.
The determinant-fixed group is C*, not the full two-dimensional group;
the full group is used only for the hypothesis of Theorem 5.1.

M controls deformations with a chosen determinant trivialization:
d+a, for a in M^1, preserves epsilon, and integrability is
da+a wedge a=0. Its degree-zero gauge exponentials have determinant
one. Over an Artin base a smooth determinant-preserving trivialization
exists: local smooth trivializations lift through nilpotent extensions
and glue using the fine smooth endomorphism sheaf, and their determinant
can be corrected by a scalar square root congruent to one. This is the
usual Dolbeault model on the fixed smooth bundle, with the determinant
actually fixed rather than inferred from unchanged Chern classes.

**The complex quadratic equation really vanishes on the plane.**
For w in W, L094 proves Q(w)=0 for all three real ASD obstruction
components. w is off-diagonal, so c=w wedge w is diagonal trace-free,
and its (0,2) part is B(w) wedge B(w). Let D=diag(1,-1), so L094's
parallel generator xi=iD. The two obstruction pairings with
xi omega_J and xi omega_K give

\[
\int_S\operatorname{Tr}(D c)\wedge\omega_J=
\int_S\operatorname{Tr}(D c)\wedge\omega_K=0.               \tag{3}
\]

Indeed wedging against a self-dual form discards the anti-self-dual
part, and the L2 pairing in L094 differs from (3) only by a nonzero
constant. The holomorphic two-form sigma_g=omega_J+i omega_K is of
type (2,0) for I. Type on a complex surface therefore gives

\[
\int_S\operatorname{Tr}(D B(w)\wedge B(w))\wedge\sigma_g=0. \tag{4}
\]

All off-diagonal H^2 groups vanish, and H^2(End_0 E) is the single
diagonal copy of H^2(O_S). Its Serre pairing with sigma_g, using
Tr(D^2)=2, is perfect. B(w) is d-closed, so (4) proves its square
is zero in H^2(M). No real moment component is substituted for the
holomorphic equation: both omega_J and omega_K were used.

For arbitrary complex s,t, the real vector
w=(Re s)v+(Im s)Iv+(Re t)Jv+(Im t)Kv belongs to W and B(w)=ell(s,t).
Thus [ell(s,t) wedge ell(s,t)]=0 for all s,t. Polarization over C
shows that every coefficient of this quadratic polynomial in H^2(M)
vanishes. The linear element ell in H^1(M) tensor (s,t) is therefore
a Maurer--Cartan element of the strict cohomology DG Lie algebra
(H^*(M),0,[ , ]). This checks the complete complex quadratic equation.

**Normalize the formal comparison before transferring the jet.**
Formality yields an L-infinity quasi-isomorphism from strict H^*(M)
to M. Concretely one may take the minimal model on cohomology and
its map to M; formality identifies that minimal model with the strict
cohomology algebra. Its induced linear cohomology map A_1 is a graded
Lie automorphism, since an L-infinity morphism between zero-differential
cohomology models preserves the binary bracket in cohomology.
Precompose by the strict Lie automorphism A_1^{-1}. The resulting
comparison induces the identity on cohomology. This normalization
uses no metric or quaternionic compatibility of its higher terms.

Apply the normalized comparison to ell over R=C[[s,t]]. The
Maurer--Cartan pushforward series is well defined in the ideal-adic
topology: its n-linear term has parameter order at least n. It gives
an actual formal solution

\[
\widehat a\in(s,t)M^1[[s,t]],\quad
d\widehat a+\widehat a\wedge\widehat a=0,
\quad [\widehat a]_1=s[b_1]+t[b_2].                       \tag{5}
\]

Here the last equality concerns first-order cohomology. It has not
yet identified harmonic representatives or analytic coefficients.
The standard formal DG Lie interpretation is used only over the
nilpotent quotients R/(s,t)^N and their compatible inverse limit;
no convergence of (5) is claimed.

**Formal determinant-one gauge and the finite analytic slice.**
Trace-free and scalar coefficient spaces in (2) are orthogonal for
the fixed Hermitian metric. They are parallel, hence preserved by
d,d*, harmonic projections H_q and Green operators. For a small
harmonic alpha in H^1(M), the cited analytic slice is

\[
a(alpha)=alpha+d^*beta(alpha),\quad
beta\in(\ker d^*)^\perp\subset A^{0,2}(End E),
\]
\[
(1-H_2)\{dd^*beta+(alpha+d^*beta)\wedge(alpha+d^*beta)\}=0. \tag{6}
\]

On a surface ker d* in degree two equals the harmonic space because
there are no degree-three Dolbeault forms. The linearization dd* is
invertible on its orthogonal complement. The trace-free subspace
is preserved by the square of a degree-one form, which is half its
graded bracket. Restricting the analytic implicit-function construction
to that subspace gives a solution of (6); uniqueness in the full slice
identifies it with beta(alpha). Thus beta(alpha) is trace-free.
Its constant and linear terms vanish. The complete finite convergent
obstruction equations, in harmonic coordinates, are

\[
Psi(alpha)=H_2(a(alpha)\wedge a(alpha))=0.                 \tag{7}
\]

By (6), not merely by its quadratic Taylor term, (7) is equivalent
to integrability of d+a(alpha). Its target is the one-dimensional
H^2(M); its domain has dimension 52.

To place (5) in this very slice, proceed by total parameter degree.
Suppose d*widehat a vanishes in degrees below n. For each coefficient
c_n of total degree n solve

\[
d^*d phi_n=d^*c_n,\qquad phi_n\perp\ker d\subset M^0.      \tag{8}
\]

The right side is orthogonal to ker d by integration by parts.
The degree-zero Green operator gives the unique smooth trace-free
solution. Gauge by the exponential of the homogeneous degree-n
polynomial with these coefficients. In the convention
g(d+a)g^{-1}, the degree-n term changes by -d phi_n, while lower
degrees stay fixed. This kills its d*. Every gauge is determinant
one. Their product is well defined formally since finitely many
orders affect any quotient R/(s,t)^N. Integrability is preserved.

Write the resulting formal solution a' using coefficientwise Hodge
decomposition:

\[
a'=\widehat\alpha+d^*\widehat\beta,\quad
\widehat\alpha=H_1 a',\quad
\widehat\beta\perp\ker d^*.
\]

Its exact component vanishes because d*a'=0. All coefficients are
trace-free. Formal uniqueness for (6), degree by degree using its
invertible linearization, identifies widehat beta with the Taylor
substitution beta(widehat alpha). Therefore

\[
Psi(\widehat\alpha)=0,\qquad
\widehat\alpha=ell(s,t)+O((s,t)^2).                       \tag{9}
\]

At degree one integrability and the gauge equation make a'_1
harmonic. Normalization in (5) and uniqueness of harmonic
representatives make it exactly (1), not an unknown linear change.

**Analytic realization and determinant.** Apply Artin approximation
to (7) with independent variables s,t and 52 dependent harmonic
coordinates. All equations are convergent over C; (9) is a formal
solution vanishing at zero. Approximation modulo (s,t)^2 gives a
convergent alpha(s,t) satisfying the complete equations (7) and
alpha(s,t)=ell(s,t)+O((s,t)^2). Shrink U so it lies in the Sobolev
slice neighborhood required in the cited proposition.

Its actual family d+a(alpha(s,t)) is integrable on every fibre.
The coefficients are holomorphic in s,t, so adding the ordinary
base Dolbeault operator makes the total operator integrable as well:
the mixed base/fibre derivatives vanish. The analytic slice's elliptic
regularity and holomorphic bundle construction give a locally free
holomorphic family on S times U. Every coefficient is trace-free,
so the induced total determinant operator is the unchanged pullback
operator on det E, with epsilon a holomorphic trivialization.
Because beta has no linear term, the first-order fibre operator is
exactly ell(s,t). The real/Dolbeault isomorphism and L094's independent
real frame show [b_1],[b_2] are complex-linearly independent. This
proves the asserted Kodaira--Spencer map and its injectivity.

Artin has retained a finite jet, not proved convergence of the
particular formal series. The higher coefficients need not preserve
any real equation or quaternionic derivative. Integrability alone
gives neither polystability at h nor a compatible unitary connection.
Thus this conclusion satisfies the approved partial continuation
test and leaves all the listed independent gaps intact.

**Separate critical audit, 2026-10-14 (step 270).** The determinant-fixed
complex realization and its precisely identified first jet survive this
audit. The audit is EXPLORATION / REPRODUCTION: no substantive error,
new existence conclusion or stronger integration statement was found.
The following checks expand the existing bridges under the approved
scope; they do not replace any hypothesis by a stability or quaternionic
assumption.

First, the two line summands are nonisomorphic: otherwise 2k=0 in the
torsion-free K3 lattice, contradicting k^2=-14. The off-diagonal Hom
vanishing in L094 therefore gives the asserted full automorphism group.
Theorem 5.1 of BMM applies directly using this reductivity and the
projective K3 hypothesis, without substituting a real polarization into
a theorem stated only for integral polarizations. For homogeneous
coefficient forms x and f id, graded commutation gives [x,f id]=0;
also Tr([x,y])=0 and Tr(dx)=bar-partial Tr(x). Consequently P in (2)
commutes with d and satisfies P([m,x])=[m,P(x)] for m in M. This
checks precisely the DG-module sufficient case of BMM Theorem 2.3.
The fixed determinant group is used for gauge transformations only;
it need not be the group in the full-endomorphism formality theorem.

Second, B is complex-linear for the complex structure I on V, not for
coefficientwise conjugation of real skew-adjoint forms. In particular
I(Jv)=Kv makes the t-coordinate in (1) agree with the fourth vector
of the prescribed real frame. The two real equations (3) combine into
pairing with omega_J+i omega_K. Wedging against this (2,0)-form retains
exactly c^{0,2}=B(w) wedge B(w). The coefficient of D is the whole
trace-free degree-two cohomology, since both off-diagonal degree-two
groups vanish. Multiplication by D and trace multiply that coefficient
by 2, a nonzero number. Serre duality therefore detects it completely.
Every pair (s,t) corresponds to a real w in W by the displayed real
identification, so there is no restriction to real s,t before complex
polarization. This validates all three coefficients of the holomorphic
quadratic equation, including its cross term.

Third, BMM Section 2, pp. 4--6, supplies a minimal model with a map
*to* M. Formality and uniqueness of minimal models identify its source
with the strict graded cohomology Lie algebra. For the composite
F:H^*(M) to M, the arity-two morphism identity gives
H(F_1)([x,y])=[H(F_1)x,H(F_1)y]. Thus A=H(F_1) is an invertible
graded Lie map and precomposing by A^{-1} is a legitimate strict
automorphism on the entire source. It normalizes the cohomology map,
not an arbitrarily chosen harmonic representative. In the convention
of BMM Definition 2.2, the transferred series on a degree-one element
is sum_{n>=1} F_n(ell,...,ell)/n!. Each summand has parameter order
at least n. The morphism identities give its Maurer--Cartan equation
on each nilpotent quotient, and the one series makes those solutions
compatible. No inverse-limit choice of unrelated deformation classes
is involved.

Fourth, in the formal gauge calculation the equation for phi is complex
linear. No self-adjoint or unitary restriction is imposed on phi. For
every z in ker d on M^0, <d*c,z>=<c,dz>=0, so the degree-zero Green
inverse used in (8) exists despite the diagonal infinitesimal stabilizer.
Conjugation by exp(phi_n) changes order n by -d phi_n; its commutator
with a term of positive parameter order first enters order n+1. Trace
zero gives determinant one coefficientwise. Total-degree induction
works equally for the s^i t^j terms with i+j=n, and only finitely many
factors affect any fixed quotient. For the final Coulomb representative,
Hodge decomposition has no exact term: if the exact part is d u,
then d*d u=0 forces ||d u||^2=0. Its remaining coexact term is d*beta
with beta uniquely orthogonal to ker d*.

On this complex surface d is identically zero in degree two. Hence
ker d* in that degree is exactly H^2, and dd* is the Dolbeault
Laplacian on its orthogonal complement. The projections in (6) are
therefore the projections of Buchdahl--Schumacher Proposition 2.6,
not merely a quadratic approximation to them. The residual
R=dd*beta+a wedge a satisfies (1-H_2)R=0, while
H_2(dd*beta)=0; thus R=Psi(alpha). This also checks directly the
complete integrability criterion in the surface case. Formal uniqueness
for (6) follows by taking the first differing total degree: its difference
would lie in the kernel of that invertible dd*. It follows that the
formally gauged solution lands in these very finite analytic equations.
At order one it is both closed and coclosed, so normalized cohomology
identifies it with the actual harmonic form ell, with no residual
change of basis or scale.

Finally, the analytic construction supplies a total family, not only
unrelated holomorphic fibres. Here is a parameter-regularity check for
the last paragraph of the proof. Write G_2 for the Green operator on
degree-two forms. In the slice, (6) is equivalently

\[
 beta=-G_2(1-H_2)(a\wedge a),\qquad a=alpha+d^*beta.
\]

Initially beta is holomorphic into W^{2,p} and a into W^{1,p}, with
p>4. On the real four-manifold W^{r,p} is an algebra for r>=1.
If beta is holomorphic into W^{r+1,p}, this identity and the bounded
map G_2:W^{r,p} to W^{r+2,p} upgrade it to W^{r+2,p}, since alpha
is a finite sum of smooth harmonic forms. Induction takes place on
the same parameter neighborhood; no intersection of shrinking Sobolev
neighborhoods is required. After the convergent substitution alpha(s,t),
Sobolev embedding and Banach-valued holomorphic differentiation yield
joint smoothness on S times U and vanishing base bar-partial derivative.
The total Dolbeault operator therefore squares to zero. The standard
integrable semi-connection/holomorphic bundle correspondence, used in
Buchdahl--Schumacher Section 1, p. 80 (Koszul--Malgrange), applies on
this product and gives a locally free holomorphic bundle.

Artin approximation is used solely on the finite-dimensional equation
Psi=0, with independent variables (s,t), 52 dependent coordinates and
precision (s,t)^2, as in Rond Theorem 2.1, p. 122. This retains zero
constant term and both linear coefficients. Since beta has no linear
term, it retains those coefficients in the fibre operator too. The
determinant of the total operator is exactly the pullback determinant
operator plus Tr(a)=0; its base component is the ordinary one. Thus
the fixed smooth epsilon is holomorphic on the product and agrees
with the specified central trivialization. Linear independence of
[b_1],[b_2] follows from harmonic uniqueness and L094's four independent
real frame vectors. This proves the claimed injection with its original
normalization. None of these checks supplies the real ASD equation,
a quaternionic parameter map, punctured stability or a common F.

## Mathlib

Full matching coverage of trace-free K3 formality, this multivariable
analytic family and its prescribed jet: **not checked**. The saved
assessment likewise records matching coverage as not checked. Unknown
availability is not evidence of absence. The primary formality, analytic
slice and approximation inputs above are imported with their hypotheses;
their determinant and first-jet specializations are proved here. No
numerical certificate or Lean verification is claimed.
