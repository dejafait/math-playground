# L084 — Both actual real images are signed spin-family indices

## Hypotheses

Assume precisely L079's conditional kernel F on X=S x S: S is its
marked projective K3 with the identical hyperkähler metric on both
factors, F is holomorphic locally free of rank two and slope-polystable
at Omega, c_1(F)=0 integrally, and

\[
\operatorname{ch}_2(F)=-9e_1-10e_2-\tau_D.
\]

Use L079's actual bundles G=R^1p_{2*}F and H=R^1p_{1*}F, their
induced Hermitian connections, and their symmetric Serre forms Q_G,
Q_H. Let R_G,R_H be their real reductions obtained by L079's positive
normalization. The determinant wedge and the two nonzero holomorphic
fibre two-forms used in these pairings may have any constant nonzero
normalization. The positive Hermitian metrics are linear in the first
argument. L071 supplies the actual compatible unitary connection on F.

Each projection fibre has its complex orientation and its unique spin
structure; H^1(S,Z/2)=0. Fix the spin pushforward convention as the
index of D^+:S^+ tensor F -> S^- tensor F, positive kernel minus
negative kernel. In complex dimension two, S^+ consists of even
Dolbeault degrees and S^- of odd degrees, with the trivial canonical
square-root factor understood. The rank-four spin pushforward with
quaternionic coefficients takes KSp^0(X) to KO^0(S); its Bott sign is
fixed by this analytic convention.

## Conclusion

The determinant wedge and this connection make F a parallel
quaternionic line, with class f in KSp^0(X). For this **same** class,

\[
(p_2)^{\mathrm{spin}}_!(f)=-[R_G],\qquad
(p_1)^{\mathrm{spin}}_!(f)=-[R_H]\quad\text{in }KO^0(S).
\tag{1}
\]

More precisely, the positive real Dirac kernels vanish and the
negative real kernels are real-bundle isomorphic to R_G and R_H,
respectively. The isomorphisms compare the actual normalized Serre
involutions with the harmonic spinor involutions; (1) is not inferred
from equality of complexifications. Their real ranks are five and
six, so the index ranks are -5 and -6. Orientations of the reductions
may be transported across these isomorphisms; KO does not record a
choice of orientation.

This is a conditional REPRODUCTION/specialization of the cited index,
spinor and transform machinery, preserved by the separate audit below. It
identifies no particular f from rational Chern data and computes no
joint attainable-pair set or Stiefel--Whitney class. It retains every
possible kernel lift. The individual E_4 and J_5 constructions are
not assumed to be these images. No F, cycle or transverse transport
is constructed, and the universal primitive Hodge gap is unchanged.

## Proof

**Imported machinery and scope.** Import Atiyah--Singer, *The index
of elliptic operators: V*, Annals of Mathematics (2) 93 (1971),
139--149, [Section 1, Theorem (1.5), pp. 140--143](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/as5.pdf):
the analytic and symbol/topological indices of a continuous real
elliptic family on compact smooth fibres agree. With constant kernel
and cokernel ranks, its analytic index is their real virtual
difference. We will exhibit that real family before applying it.
No injectivity of complexification on base-bundle K-theory is used.

For the spin/quaternionic coefficient type use Atiyah--Bott--Shapiro,
*Clifford modules*, Topology 3, Supplement 1 (1964),
[Sections 4--5 and 11--12](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/abs.pdf),
and Eschenburg--Hanke, *Bott--Thom isomorphism, Hopf bundles and Morse
theory*, [arXiv:2011.14368v2, Section 10, pp. 33--36](https://arxiv.org/pdf/2011.14368v2),
Propositions 10.4, 10.6 and Theorems 10.7(b), 10.9(a), with m=1.
The vertical tangent is oriented spin of rank four over a finite CW
space, and these are the real/quaternionic type-changing Thom maps.
In degree notation, the pushforward sends KO^{-4}(X)=KSp^0(X)
to KO^{-8}(S)=KO^0(S), using Bott periodicity with the convention
above. ABS's unshifted rank-8k display is not substituted for this
rank-four construction. Neither the index nor Thom theorem is
reproved here; the explicit module check below fixes the particular
real operator and its coefficient convention.

Import Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications 8 (1998),
239--249, [Section 3.3, Lemmas 1--2 and Theorem 3, pp. 244--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
For a compact hyperkähler source, compatible rotation spheres,
Hermitian instanton kernel and source, and all-parameter odd IT, its
Dirac/Dolbeault comparison identifies the actual odd image with the
negative complex Dirac kernel, with the induced projected connection.
L079 verifies all these hypotheses for F and the flat line source in
each direction. The Kähler Dirac operator, with trivialized parallel
canonical square root, is sqrt(2)(bar-partial_F+bar-partial_F^*).
The theorem does not supply the real Serre comparison; that is the
specialization proved next. These general inputs and their relevant
proof cases are covered by the unchanged identification assessment.

**One quaternionic coefficient on the whole product.** L079 proves
det(F)=O_X, not just rational first-class vanishing. Its determinant
connection is Hermite--Einstein of constant zero. A holomorphic
trivialization is parallel: for a holomorphically trivial Hermitian
line the zero-Einstein equation makes the logarithm of the metric
harmonic, hence constant on compact connected X. Equivalently use
the zero-Einstein parallel-morphism result already imported in L079.
Thus the determinant wedge A is parallel. Normalize it by a positive
constant to a unit determinant form A_0. In a unitary frame f_1,f_2
with A_0(f_1,f_2)=1, define the antilinear operator

\[
J_F f_1=-f_2,\qquad J_F f_2=f_1.
\tag{2}
\]

Intrinsically A_0(u,v)=h_F(u,J_Fv); hence (2) glues, is parallel
and antiunitary, and J_F^2=-1. This constructs f=[F,J_F], a
quaternionic line, on all of X. It is not the underlying real
rank-four coefficient used without its quaternionic action.
Changing the determinant phase multiplies J_F by a unit phase;
the resulting structures are isomorphic by a constant scalar with
the appropriate square. No classification or restriction of f by
its Chern character has occurred.

**Complex-oriented spinors and the real Clifford check.** Perform
the following construction on either copy of S. Normalize its
parallel holomorphic two-form to a unit form sigma_0 and choose
the corresponding parallel trivialization of its canonical square
root. This is the unique spin structure: the choices of spin
structure form a torsor under H^1(S,Z/2)=0. Locally take a unitary
(0,1) coframe a,b with w=a wedge b=bar(sigma_0). Then

\[
S^+=\langle1,w\rangle,\quad S^-=\langle a,b\rangle,
\quad C(1)=w,\ C(w)=-1,\ C(a)=-b,\ C(b)=a,
\tag{3}
\]

where C is antilinear. Unit determinant coframe changes are in SU(2).
They preserve (3): on the odd space it is the antiunitary operator
associated to its determinant alternating form; on the even space
1,w are fixed global parallel sections. Thus C is globally defined,
parallel, antiunitary, preserves chirality, and C^2=-1.

Here is a complete real Clifford sign check. Write
a=(x_1-i y_1)/sqrt(2), b=(x_2-i y_2)/sqrt(2) in an oriented real
orthonormal coframe (x_1,y_1,x_2,y_2), with I sending the dual
x_j-vector to the dual y_j-vector. If epsilon_j and iota_j are
exterior multiplication and its Hermitian adjoint, use

\[
c(x_j)=\epsilon_j-\iota_j,\qquad
c(y_j)=i(\epsilon_j+\iota_j).
\]

They satisfy c(v)^2=-|v|^2. On the ordered basis (1,a,b,w) their
values, and those of both compositions with C, are:

| operator | values on (1,a,b,w) | values of Cc=cC on (1,a,b,w) |
|---|---|---|
| c(x_1) | (a,-1,w,-b) | (-b,-w,-1,-a) |
| c(y_1) | (ia,i,iw,ib) | (ib,-iw,i,-ia) |
| c(x_2) | (b,-w,-1,a) | (a,1,-w,-b) |
| c(y_2) | (ib,-iw,i,-ia) | (-ia,-i,-iw,-ib) |

In computing the last column C conjugates i. This checks every
real generator, hence C commutes with real Clifford multiplication.
The complex-oriented chirality operator is
Gamma=-c(x_1)c(y_1)c(x_2)c(y_2); its values are (1,-a,-b,w).
Thus even degree really is positive chirality in this convention.
No fibre orientation or chirality is reversed for p_1.

**The actual real family.** On the complex twisted spinors set

\[
R=C\otimes J_F.
\tag{4}
\]

This is a well-defined antilinear operator on the complex tensor
product: moving a scalar between its two factors gives the same
conjugate scalar. It is antiunitary, R^2=1, preserves chirality and
commutes with real Clifford multiplication. It is parallel for the
tensor connection, vertically and horizontally (the spinor factor
is pulled back from the fixed fibre). Consequently it commutes
with the actual twisted Dirac operator and its adjoint. Restricting
them to the fixed real subbundles produces a real elliptic family
whose complexification is precisely the original Dirac family.

For clarity about the quaternionic tensor convention, regard a
spinor half as a right quaternionic line with s i=i s and s j=C s,
and the coefficient as a left line with i v=i v, j v=-J_Fv.
The latter is the same complex symplectic coefficient up to the
harmless sign isomorphism between J_F and -J_F. The map

\[
s\otimes v\longmapsto
\tfrac12(s\otimes v+C s\otimes J_Fv)
\tag{5}
\]

is real bilinear and balanced: its values on (i s,v) and (s,i v)
agree, and those on (C s,v) and (s,-J_Fv) both equal
(C s tensor v-s tensor J_Fv)/2. It therefore identifies the
quaternionic balanced tensor with the fixed real space in (4).
It is onto by projection onto the fixed space; both have real
dimension four for either spinor half. This checks the rank-four
Morita convention directly and rules out a factor of two from
using the underlying real coefficient instead.

L079 gives H^0=H^2=0 on every fibre of both projections, with
h^1=5 for p_2 and h^1=6 for p_1. The imported Dirac/Dolbeault
identification therefore gives ker(D^+)=0 and ker(D^-)=the
harmonic (0,1)-forms with values in F. Constant dimensions imply
smooth kernel bundles and smooth harmonic projections, as in the
imported transform construction. Since R commutes with D and
the Laplacian, these projections commute with R. The real negative
kernels are the R-fixed harmonic bundles; their complexifications
are G and H. The projected connections preserve R. It remains
to identify their real structures, not merely these complex bundles.

**Compare the actual Serre involutions.** On odd spinors the
alternating coefficient of u wedge v in w is

\[
u\wedge v=h_{S^-}(u,Cv)\,w.
\tag{6}
\]

Checking (a,b) gives 1 on both sides; the reversed pair gives -1,
and the equal pairs give zero. By complex bilinearity these four
checks prove (6) for all u,v. Likewise (2) gives the coefficient
form A_0. For decomposable F-valued odd forms alpha=u tensor s,
beta=v tensor t, the cup/wedge pairing has coefficient
A_0(s,t) times the coefficient of u wedge v. Thus (6) and (4)
give its pointwise value h(alpha,R beta) w. Linear extension
covers arbitrary forms, not only decomposables.

With the real orientation above,
w wedge sigma_0=dvol: indeed a wedge bar(a)=i x_1 wedge y_1,
b wedge bar(b)=i x_2 wedge y_2, and moving bar(a) past b
introduces the additional minus sign. Hence the pairing formed
with A_0,sigma_0 and integration is exactly

\[
\int_S h(\alpha,R\beta)\,dvol
=h_{L^2}(\alpha,R\beta).
\tag{7}
\]

To retain the actual Serre-trace convention, let kappa be the
nonzero constant expressing its Dolbeault trace on H^2(K_S)
as kappa times integration. It can equivalently be defined by
tr([w tensor sigma_0])=kappa Vol(S). This determines it without
an assumption about its sign or a convention for powers of 2pi i.
Both functionals are nonzero on this one-dimensional space, so
this equality applies to every top-degree representative. Write
the actual choices in L079 as A=t A_0 and sigma=s sigma_0.
Their scalars are constant: A is parallel on connected X, and
sigma is parallel on the fixed K3. Therefore the actual pairing
on harmonic representatives is

\[
Q(\alpha,\beta)=\gamma h_{L^2}(\alpha,R\beta),
\qquad \gamma=\kappa s t\ne0.
\tag{8}
\]

This proves equality with the actual cup/trace form, since the
Dirac/Dolbeault map is the natural harmonic cohomology map used
in L079. There is no exchange of the two odd arguments in (8).
The two minus signs (coefficient wedge and odd cup product)
give its symmetry; no extra sign is inferred from self-duality.

For a Hermitian metric linear in its first argument, (8) means
J_Q=bar(gamma) R. Hence J_Q^2=|gamma|^2 and L079's positive
normalization is exactly

\[
j_Q=\frac{\overline\gamma}{|\gamma|}\,R.
\tag{9}
\]

Choose a constant unit scalar z with z^2=bar(gamma)/|gamma|.
Multiplication by z maps Fix(R) isometrically onto Fix(j_Q):
j_Q(z v)=bar(gamma)|gamma|^{-1} bar(z)v=zv for Rv=v.
The same scalar on both chiralities intertwines the corresponding
real Dirac families. Thus even an opposite Serre trace sign
changes neither the real kernel isomorphism class nor the index
sign. No uncontrolled variable real structure has been introduced.

This computation uses the natural L2 metric underlying the induced
connection. If L079's normalization is made with another parallel
positive Hermitian metric, join the two by their positive convex
path. The same parallel Q and its positive normalization then
give a smooth family of real fixed bundles over S x [0,1]. Its
endpoint restrictions are isomorphic real bundles. One can see
the isomorphism directly: for the path j_t, solve T'_t=A_t T_t,
T_0=1, with A_t=(j'_t j_t)/2, a complex-linear operator. From
j_t^2=1 follows [A_t,j_t]=j'_t, so j_t=T_t j_0 T_t^{-1}.
All coefficients are parallel over S, hence T_t is as well.
Thus the KO identification does not depend on an unspecified
parallel metric choice in the original normalization.

**Both projections and the index sign.** Apply the same calculation
first with the first S as fibre for p_2 and then with the second
S as fibre for p_1. Each uses the positively complex-oriented
coframe and Gamma above and the same global J_F. The two fixed
fibre-form choices may give different constants gamma, absorbed
by separate constant scalars on their spinor families; this does
not replace the coefficient f. Both real Dirac families have
zero positive kernels and negative kernels isomorphic to R_G,
respectively R_H. The real analytic indices are therefore -[R_G]
and -[R_H], of ranks -5 and -6. Their complexifications have
classes -[G] and -[H], agreeing with L079's signed GRR, but this
last observation is only a consistency check.

The real families have compact smooth spin fibres and compact smooth
base, smooth symbols, and constant kernel/cokernel dimensions.
Atiyah--Singer's real family theorem applies. Their symbols are
the spin Clifford symbols with the single quaternionic coefficient
f, by (3)--(5), so the imported spin Thom construction identifies
their topological indices with the two spin pushforwards in (1).
This proves (1) in real K-theory itself. It imposes no values of
w_2 or w_4 and gives no finite-rank or holomorphic realization
of a prescribed pair. The independent-index stops of L079 remain
valid; using (1) for a joint topology test requires separate coverage.

### Separate critical audit — 2026-10-10

The audit uses the unchanged SPECIALIZE coverage in
`drafts/literature/2026-10-10-real-spin-index-critical-audit.md`.
Its threshold is both identities (1) in KO, including the actual real
reductions. The cited general index and Thom theorems are imported;
the following checks concern this proof's specialization. No joint
characteristic calculation is included.

**Actual inputs and global descent.** L079 supplies every-fibre odd
concentration, not merely a generic index, and the same compatible
connection supplied by L071 in both directions. Its determinant is
holomorphically trivial integrally. The determinant connection has
zero Einstein constant; the norm of a nowhere-zero holomorphic section
is constant by the compact harmonic-function argument. Thus (2) is
parallel on the whole product. Its definition is invariant under the
unit determinant unitary frame group, so there is one global J_F.
The spin canonical-square-root factor has a global parallel
trivialization on the simply connected K3. The unit determinant
coframe changes preserve C on the odd space and fix the parallel
even basis. This checks global spinor descent, not only one frame.

**Clifford signs, orientation and coefficient type.** Recompute the
table using iota_1(w)=b and iota_2(w)=-a. All sixteen displayed
generator values and their sixteen C-compositions agree. In particular
C(ia)=ib and C(-iw)=-i; omitting antilinearity would break the two
y-generator columns. The four-generator product has values
(-1,a,b,-w). Its negative is the asserted chirality operator for the
complex-oriented real coframe. The convention a=(x_1-i y_1)/sqrt(2)
has I^*a=-ia, as required for degree (0,1), when I sends the dual
x_1-vector to the dual y_1-vector.

The right action s j=C s has (s i)j=-i C s, while the left action
j v=-J_Fv anticommutes with i and squares to -1. These are legitimate
right and left quaternionic actions. Equation (5) is balanced for
both generators i,j, hence for the whole algebra. Its image spans
the fixed space because projection of arbitrary complex tensors
onto Fix(R) is surjective as a real map. Both spaces have real
dimension four per chirality; thus the map is an isomorphism.
Replacing J_F by -J_F is implemented by multiplication by i, so
this convention does not replace f by a different coefficient class.
The complexification of the real half is complex rank four, not
eight: no underlying-real coefficient doubling occurs.

The analytic sign convention in the hypotheses is retained when
importing the rank-four type-changing Thom map. At the Fourier-symbol
level the usual principal symbol is i c(xi). Since R is antilinear
and commutes with c(xi), conjugation sends it to -i c(xi)=i c(-xi).
This is precisely the antipodal vertical-symbol reality used in
Atiyah--Singer V, rather than an involution on the K3 base. The fixed
operator therefore has the required real elliptic symbol. Both
projections use this same complex orientation and coefficient; neither
interchanges the chiralities.

**Harmonic and Serre comparison.** R is parallel and commutes with
each real generator, so it commutes with D and D^2; it preserves the
harmonic subspaces and their projections. The natural harmonic map
to H^1(F) is the map in the actual Dirac/Dolbeault identification.
The two alternating forms on S^- and F multiply to the symmetric
coefficient pairing on their tensor product. Direct evaluation on
(a,b) and (f_1,f_2) gives +1 in each factor. Moving bar(a) through b
in a b bar(a) bar(b), together with i^2=-1, gives +dvol. This checks
(7) with the stated order, rather than assigning a sign from abstract
self-duality. The trace on H^2(K_S) and integration are nonzero
functionals on one fixed one-dimensional space, so their ratio is a
single nonzero constant. Parallel determinant and fibre-form choices
make gamma constant over the parameter surface. Equations (8)--(9)
then follow with the conjugate of gamma because the metric is linear
in its first argument. A constant square root z identifies the fixed
real spaces exactly as claimed, even when gamma is negative or has
nonreal phase. This establishes real-bundle equality before any use
of complexification.

**Arbitrary parallel metric.** For each member g_t of the positive
convex path, define J_t by Q(u,v)=g_t(u,J_t v). In a g_t-unitary
basis the symmetric matrix B_t gives J_t^2=B_t^*B_t>0. The positive
square root depends smoothly on t and the base, also at repeated
eigenvalues, by smooth functional calculus on positive matrices.
J_t commutes with it since J_t commutes with J_t^2 and the function
is real on its positive spectrum. Consequently
j_t=J_t(J_t^2)^(-1/2) is a smooth antilinear involution. All these
operators are parallel over the base: Q and g_t are parallel, and
functional calculus preserves parallelness. No scalar-square claim
is required here.

Differentiating j_t^2=1 gives j'_t j_t=-j_t j'_t. The complex-linear
operator A_t=j'_t j_t/2 therefore satisfies
A_t j_t-j_t A_t=j'_t. The global linear ODE T'_t=A_t T_t, T_0=1
has an invertible solution on the compact interval. Differentiation
gives (T_t^{-1}j_t T_t)'=0, hence T_t maps Fix(j_0) isomorphically
onto Fix(j_t). This proves the endpoint real-bundle identification
for any permitted parallel metric, even with reducible images.

Finally every-fibre H^0=H^2=0 makes the positive real kernel zero.
The negative real kernels have ranks five and six; their actual
fixed-space identifications give the negative signs in (1). The
compact smooth fibres/base, spin vertical bundles and constant
kernel dimensions meet the imported family theorem's hypotheses.
This audit found no substantive error or stronger obstruction.
Outcome: EXPLORATION / REPRODUCTION, a completed proof audit rather
than a new mathematical input. The full conditional conclusion
survives; common-kernel topology, holomorphic realization and Hodge
algebraicity remain unresolved. L059's normalization was checked
through L079's explicit use, without importing its unrelated rank-seven
conclusions.

## Mathlib

Full matching identification, real families-index theorem and the
spin/quaternionic Thom machinery: **not checked**. No absence claim
is made. The canonical proof above imports their precise published
forms and verifies the actual coefficient, Clifford, harmonic,
Serre-normalization and two-projection specialization. It is not
a formalized theorem or a solution of the Hodge conjecture.
