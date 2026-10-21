# L105 — A cubic invariant selects a degree-one split-line family

## Hypotheses

Retain audited L094/L101's marked projective K3 surface S, complex
structure I, fixed hyperkähler metric g, real Kähler class h and line
bundle L with c_1(L)=k, k^2=-14 and k.h=0. Set E=L direct sum L^{-1},
with its fixed determinant-one direct-sum Hermite--Einstein connection
and determinant trivialization epsilon. Put d=bar-partial_A and
M=A^{0,*}(S,End_0 E). Identify H^1(M) with its actual harmonic forms,
and write H=H_+ direct sum H_-, where H_+=H^1(L^2), H_-=H^1(L^{-2}).
Each has dimension 26; H has no diagonal sector.

Use the unchanged first jet from L101. To avoid confusing coefficient
vectors with its b_1,b_2, write

\[
 a_i=B(e_i),\quad c_i=B(Je_i)\quad(i=1,2),\qquad
 \ell(s,t)=s a_1-t a_2+t c_1+s c_2.                 \tag{1}
\]

Both pairs are complex-linearly independent. The scale, source
coordinates and marked data in (1) are fixed. No product kernel F,
nonempty global reducible locus or quaternionic parameter family is
assumed. The ordinary analytic image means precisely L103's reduced
analytic GIT image, not a separately specified coarse-space structure.

## Conclusion

There is a choice of actual convergent determinant-trivial L101 family
with the same first jet (1) whose classifying germ is finite onto its
ordinary reduced analytic image and has generic degree one. Every
noncentral sufficiently small fibre is strictly slope-stable at h.

More precisely, one can choose u in H_+ outside span(a_1,a_2) and an
actual harmonic slice map satisfying the complete integrability equations
and

\[
 \alpha(s,t)=\ell(s,t)+s^2u+O((s,t)^3).             \tag{2}
\]

There are linear forms p on H_+ and q on H_- such that the full-vector
group invariant p(P_+alpha)q(P_-alpha) has zero terms of degree at most
two and degree-three term exactly s^3. This rules out L104's degree-two
alternative, with no normality assumption on the image.

This is a local ADVANCE / REPRODUCTION under the prior SPECIALIZE
assessment; the separate critical audit below preserves it. It specializes known
formality, slice, approximation and finite-image tools, with no
originality claim. It selects an existential choice among L101 families,
not the degree of every such family. It supplies neither a local
embedding nor global separation, coarse-space comparison, quaternionic
integration, common F, prescribed global mixed action, reconstruction,
transport or a new algebraic Hodge class. Universal primitive rational
Hodge realization remains unresolved.

## Proof

**Imported results and why a specialization is needed.** L101 establishes
formality of M by Bandiera--Manetti--Meazzini, *Formality conjecture for
minimal surfaces of Kodaira dimension 0*, Compositio Math. 157 (2021),
215--235, [1907.10690v2](https://arxiv.org/pdf/1907.10690v2),
Theorems 5.1 and 2.3, including the trace-free DG-module restriction.
Reuse this input and L101's complete fixed-metric slice equations.

Import Bandiera--Manetti--Meazzini, *Deformations of polystable sheaves
on surfaces: quadraticity implies formality*, Moscow Math. J. 22 (2022),
239--263, [1902.06486v3, 17 June 2020](https://arxiv.org/pdf/1902.06486v3),
Definition 4.19, Theorem 4.20 and Remark 4.21, pp. 16--17. Formality
upgrades to equivariant formality when the graded spaces and
Hom^j(Sym^n H,H), j=0,1 and n>=2, are semisimple modules. Its proof,
pp. 17--18 with Lemma 4.22, allows a chosen equivariant contraction and
strictifies the resulting minimal model with identity linear term.
Here and in that theorem the symmetric powers use the shifted grading.

Reuse Buchdahl--Schumacher, *Polystable bundles and representations of
their automorphisms*, Complex Manifolds 9 (2022), 78--113,
[Lemma 2.5, Proposition 2.6, Remark 3 and (2.4), pp. 83--85](https://d-nb.info/1262812674/34),
for the actual analytic slice. Reuse Artin, *On the solutions of analytic
equations*, Invent. Math. 5 (1968), 277--291, Theorem (1.2), through
the inspected arbitrary-order statement in Rond, *Artin approximation*,
J. Singularities 17 (2018),
[Theorem 2.1, p. 122, proof reductions pp. 123--126](https://www.journalofsingularities.com/volume17/rond.pdf).
We need approximation modulo (s,t)^3, rather than L101's (s,t)^2.
These general theorems are imported, not reproved. The work below checks
compatible higher data, its actual harmonic jet and the degree test;
none is supplied merely by tangent identity of a formal comparison.

**Compatible data to all orders in the strict cohomology model.**
L101 proves [ell,ell]=0 in H^2(M)[s,t]. The only degree-two cohomology
is the one-dimensional diagonal H^2(O_S). The product of two strictly
upper triangular coefficient matrices is zero; the same holds for two
strictly lower triangular ones. Thus the brackets of any two H_+
elements, or any two H_- elements, vanish. The cross bracket gives a
bilinear map H_+ times H_- to the diagonal H^2(M).

Choose an identification H^2(M)=C only to define the two linear
functionals [ -,c_1] and [ -,c_2] on H_+. Their common kernel K has
dimension at least 26-2=24. Since span(a_1,a_2) has dimension two,
there exists

\[
 u\in K\setminus\operatorname{span}(a_1,a_2).       \tag{3}
\]

No normalization or nondegeneracy of this cross pairing is needed
for that dimension argument. We have [u,a_i]=0, [u,c_i]=0 and [u,u]=0.
Consequently the polynomial

\[
 z(s,t)=\ell(s,t)+s^2u
\]

is a complete Maurer--Cartan solution in the strict cohomology DG Lie
algebra: its differential is zero and

\[
 [z,z]=[\ell,\ell]+2s^2[\ell,u]+s^4[u,u]=0.        \tag{4}
\]

The bracket of degree-one classes is symmetric, accounting for the
factor two. Equation (4) verifies all possible terms, in degrees two,
three and four, and there are no higher terms in this polynomial.
This is full compatible formal data, not an unextended second jet.

**Equivariant transfer with the actual harmonic linear term.** Let
G=C* act by the parallel determinant-one automorphisms diag(r,r^{-1}).
On each M^j the three coefficient sectors have characters 0,+2,-2.
Each sector, even though infinite-dimensional, is a sum of copies of
one character and the total representation has finite weight support.
The action is rational: each vector has finite-dimensional orbit span
and the coefficients are Laurent monomials in r. It preserves d, the
graded bracket and the trace-free subalgebra. Its cohomology is finite
dimensional (dimensions 1,52,1 in degrees 0,1,2). Every Hom space in
Theorem 4.20 is therefore a finite-dimensional rational G-module and
semisimple. These checks apply to M[1] with the shifted convention.
L101's formality and the imported theorem give equivariant formality.

The actual Hodge contraction can be used in the theorem's construction.
The coefficient splitting is orthogonal and parallel for the direct-sum
metric. On each block the complex G-action is multiplication by a
constant scalar, and d and d* preserve that block. Thus d*, the
Laplacian, its Green inverse and harmonic projection commute with G.
This statement does not require a nonunitary element of G to be an
isometry. The Hodge inclusion, projection and homotopy d*Green are
therefore equivariant, with inclusion given by the fixed harmonic
representatives.

Use that contraction in the first step of the cited proof of Theorem
4.20. Its minimal-model map has harmonic inclusion as its linear term.
The second step gives an equivariant strictification with identity
linear term; its inverse also has identity linear term. Composing that
inverse with the minimal-model map gives an equivariant L-infinity
quasi-isomorphism

\[
 F:(H^*(M),0,[\ ,\ ])\longrightarrow M
\]

whose F_1 is the harmonic inclusion, not just identity after cohomology.
For input degree-one classes, F_n has output in M^1; the usual shifted
symmetry makes F_2 symmetric on those inputs. Apply its MC pushforward
to (4) over C[[s,t]]. Parameter-adic convergence is formal: each
n-linear contribution has order at least n. The resulting integrable
formal connection coefficient is

\[
 \widehat a=F_*(z)
 =\ell+s^2u+\tfrac12F_2(\ell,\ell)+O((s,t)^3).
                                                               \tag{5}
\]

Here ell and u on the right are the actual harmonic forms. No analytic
convergence of F or of (5) is asserted.

**Track the second jet through determinant-one slice gauge.**
On H the weights are +2,-2. On Sym^2 H they are +4,0,-4.
Equivariance of F_2 implies that its restriction to Sym^2 H has only
diagonal (weight-zero) output in M^1: that space has no weight +4
or -4. Harmonic projection H_1 of a diagonal M^1 coefficient is zero,
because H^1(O_S)=0. In particular

\[
 H_1F_2(\ell,\ell)=0.                            \tag{6}
\]

Apply exactly L101's total-degree formal Coulomb gauge. At each degree
n, solve d*d phi_n=d*c_n on the orthogonal complement of ker d in M^0,
then conjugate by exp(phi_n); here c_n is the coefficient of the
current series in that degree. These trace-free Green solutions exist
as in L101 and preserve the determinant. At degree one, c_1=ell is
harmonic, so phi_1=0. At degree two, the sole change is -d phi_2;
commutators with ell have degree at least three. Thus after gauge the
second coefficient is

\[
 s^2u+\tfrac12F_2(\ell,\ell)-d\phi_2.
\]

Harmonic projection kills the exact last term and, by (6), the middle
term. Gauges of degrees at least three cannot change this answer.
It follows that the harmonic parameter of the complete gauged formal
solution satisfies

\[
 \widehat\alpha=\ell+s^2u+O((s,t)^3).             \tag{7}
\]

This does not set the entire second coefficient of the fibre operator
equal to s^2u: diagonal coexact terms may remain. It identifies exactly
the harmonic coordinates used in the analytic quotient.

L101's formal uniqueness in the fixed analytic slice identifies the
remaining coexact part with d*beta(widehat alpha), where beta is the
actual convergent implicit-function solution. Therefore
Psi(widehat alpha)=0 for the complete finite convergent equations,
not merely their quadratic truncation. The higher gauge construction
and this uniqueness require integrability to every order, supplied by
(4) and F; the second-jet calculation alone would not suffice.

**Retain the jet in an actual family.** Apply the cited Artin theorem
to these same finite equations Psi=0, with two independent variables
s,t and 52 harmonic dependent coordinates, to obtain a convergent
solution alpha congruent to widehat alpha modulo (s,t)^3. Equations
(2) and Psi(alpha)=0 follow. Shrink its domain into the fixed slice.
L101's parameter-regularity and total Dolbeault construction now give
an actual locally free holomorphic family on S times a C^2 neighborhood,
with determinant epsilon and first differential exactly (1). Its higher
coefficient choices need not respect G as a parameter symmetry; only
the retained jet and full equations are needed.

L102 applies to this family, since its prescribed first jet is unchanged
and its equations are complete. It supplies strict h-stability on a
punctured ball, whose radius may depend on this particular alpha.
L103 then gives the finite classifying germ and ordinary image-ring
inclusion A_img subset B_0=C{s,t}, with generic degree d in {1,2}.
Its pullback maximal ideal remains (s,t)^2; no coarse first derivative
is asserted nonzero.

**Actual invariant and degree selection.** By (3), choose a linear
functional p on H_+ with p(a_1)=p(a_2)=0 and p(u)=1. Independence of
c_1,c_2 gives a linear functional q on H_- with q(c_1)=0 and q(c_2)=1.
The polynomial on H defined by

\[
 \mathcal I(x,y)=p(x)q(y)
\]

is invariant under the full vector automorphism group: its effective
ratio z sends (x,y) to (zx,z^{-1}y), so the two factors cancel. This
is a linear combination of L103's invariant coordinate products,
and its actual pullback f therefore belongs to A_img. By (2),

\[
 p(P_+\alpha)=s^2+O((s,t)^3),\qquad
 q(P_-\alpha)=s+O((s,t)^3),\qquad
 f=s^3+O((s,t)^4).                                  \tag{8}
\]

Thus f has order exactly three, including the nonzero cubic coefficient
one and zero quadratic part. All unretained terms enter f in degree at
least four. No cubic correction to a nonzero quadratic initial term is
being used.

Suppose d=2. Apply audited L104 to this very convergent family and its
ordinary image. It gives a holomorphic involution tau of B_0 fixing
A_img pointwise and acting by -id on (s,t)/(s,t)^2. In the original
coordinates, tau(s)=-s+O((s,t)^2) and tau(t)=-t+O((s,t)^2).
Consequently (8) gives

\[
 \tau(f)=-s^3+O((s,t)^4),
\]

contradicting tau(f)=f over C. Equivalently, a tangent-identity change
to L104's sign coordinates preserves this nonzero odd initial form.
The test accounts for the nonlinear involution and needs no assertion
that all invariants have even expressions in the original coordinates.
Since L103 already restricts d to {1,2}, d=1 follows.

The result establishes generic local separation for a chosen complex
family, not injectivity at every point or smoothness of its image.
No comparison with a weak normalization or an algebraic coarse germ
is used. The existence of stable fibres individually does not imply a
smooth central unitary gauge, a quaternionic family or a global kernel.
Those independent obligations and the universal Hodge gap remain open.

**Separate critical audit, 2026-10-14 (step 286).** The existential
degree-one conclusion survives. This audit is EXPLORATION /
REPRODUCTION: no substantive error, stronger conclusion or additional
existence result was found. The preceding proof remains the argument.
The following checks use the unchanged approved coverage and the actual
slice, rather than a replacement quadratic analytic chart.

First, the input coordinates have the claimed sectors and signs:
B(Jv)=B(Je_1)-B(e_2)=c_1-a_2, while B(v)=a_1+c_2.
Thus the negative component of ell is t c_1+s c_2. L094 gives the
independence of each pair and L101 gives the entire cohomology equation
[ell,ell]=0, not just its restrictions to the axes. Off-diagonal
H^2 vanishes, so each condition [u,c_i]=0 imposes at most one scalar
linear condition. The common kernel has dimension at least 24, which
exceeds the dimension two of span(a_1,a_2), whether or not that span
lies in the kernel. Strictly upper triangular products give
[u,a_i]=[u,u]=0. Hence the coefficients of degrees two, three and
four in (4) all vanish and there are no omitted higher terms. This
does not merely specify a potentially obstructed truncated jet.

Second, the hypotheses and direction of equivariant transfer hold on
the actual smooth Dolbeault model. Each graded space is the direct sum
of its three scalar-character spaces; choosing vector-space bases in
them exhibits semisimplicity even in infinite dimension. Shifting
degrees does not change characters. The total cohomology has dimension
54, so all required graded Hom spaces of its fixed finite symmetric
powers are finite-dimensional rational torus representations. The
trace-free DG-module splitting in L101 supplies ordinary formality;
no associative formality or formality of an arbitrary subalgebra is
being assumed. The primary BMM 1902.06486v3 Theorem 4.20 proof,
pp. 17–18 including Lemma 4.22, was rechecked: it starts with an
invariant Hodge decomposition, transfers a minimal model, and constructs
an equivariant isomorphism from that model to its strict bracket with
identity linear part. Inverting this isomorphism before composing with
the transferred inclusion gives exactly the direction used in (5).

For this application the invariant decomposition can be the actual
Hodge decomposition. The complex-linear operator d* preserves each
parallel coefficient block. A constant block scalar therefore commutes
with d*, despite not generally preserving the Hermitian norm. The
same holds for the Laplacian, Green operator and harmonic projection.
The chosen contraction consequently gives F_1 equal to the fixed
harmonic inclusion. The construction is used formally on the
parameter-adic quotients only; arbitrary analytic continuity or
convergence of its infinite series is unnecessary.

Third, the quadratic transfer and gauge terms are accounted for
separately. Inputs from H^1 have unshifted output degree one under F_2;
their torus weights add to +4, 0 or -4. M^1 has only weights +2, 0,
-2, so only diagonal output can survive. Its harmonic projection is
zero since H^1(O_S)=0. In the total-degree gauge construction the
first correction phi_1 vanishes because ell is already harmonic and
the Green inverse is taken on the complement of ker d. Thus there
is no degree-two commutator involving a first-order gauge. The sole
degree-two change is -d phi_2, whose harmonic projection is zero by
orthogonality. Trace-free exponentials preserve the chosen determinant.
This verifies (7) for the harmonic coordinates, without discarding
diagonal coexact terms in the operator itself.

Fourth, integrability survives the complete formal transfer and gauge.
In L101's fixed slice write a'=alpha_hat+d*beta_hat. On a complex
surface the linear map dd* on degree-two forms perpendicular to
harmonics is invertible. Formal uniqueness for the same implicit
equation therefore gives beta_hat=beta(alpha_hat). Its harmonic
residual is precisely Psi(alpha_hat), so the complete convergent
equations have a formal solution before approximation is applied.
The reused Rond Theorem 2.1 allows precision (s,t)^3; it preserves
both linear and quadratic harmonic terms. L101's total Dolbeault
construction then gives an actual determinant-trivial locally free
family. L102's uniform punctured-ball argument applies to this chosen
convergent family because its first jet is unchanged, and L103's
finite-image argument allows all its higher coefficients. No uniform
radius across different approximations is required.

Finally, p annihilates the entire positive first-order plane and q
annihilates c_1, with q(c_2)=1. The specified quadratic term is positive
weight only. Consequently the actual product has initial homogeneous
form s^3 with coefficient one; unknown cubic harmonic terms contribute
to that product only at degree at least four. The full automorphism
group has effective character a/b, so the product is invariant for that
group, not merely for its determinant-one subgroup. It is a linear
combination of the actual quotient coordinates and hence belongs to
the ordinary convergent image ring. If its generic degree were two,
L104 supplies an involution fixing this ring and having tangent -id.
Substitution into an order-three function negates its degree-three
initial form; nonlinear terms in the involution cannot change that
degree. Equality would require 1=-1 over C. This excludes degree two
and leaves degree one by L103, without needing L104's further A1
identification or any normality assertion for the degree-one image.

The direct inputs remain L094/L101/L102/L103/L104. This verifies one
selected complex family only. It supplies no smooth central unitary
gauge, product hyperholomorphic connection, quaternionic integration,
coarse-space comparison, global kernel, prescribed global mixed action,
separation at every point, reconstruction or transport. The universal
primitive Hodge gap is unchanged. No numerical test is needed for
these exact formal, weight and local-ring checks.

## Mathlib

Full matching coverage for equivariant trace-free K3 formality, the
finite-jet analytic realization and this degree-selection specialization:
**not checked**. Unknown coverage is not evidence of absence. General
inputs are cited precisely above; the compatibility, weight, gauge,
jet and invariant computations are the necessary local specialization.
No numerical certificate or Lean verification is claimed.
