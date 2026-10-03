# L013 — Degree-one cyclotomic determinant descent with a Sha direction

## Hypotheses

This is a formal sufficiency test, not an elliptic-curve example. Fix
p >= 5, F = Q_p, Lambda = Z_p[[T]], and R = Lambda_(T). The residue
field of the augmentation DVR R is F. Let sigma be the cyclotomic
involution sigma(1+T) = (1+T)^(-1), and choose

\[
t=\frac{T}{1+T/2},\qquad \sigma(t)=-t.
\tag{1}
\]

Thus (t) = (T), including over Lambda. Write I = (t) in R and
bar t for its nonzero class in I/I^2. Complexes below are in
cohomological degrees one and two. Base cohomology means derived
specialization at I followed by identification of R/I with F.

Use Sano's **Definition 2.7, Proposition 2.10, and Theorem 2.13**,
*Derived Bockstein regulators and anticyclotomic p-adic Birch and
Swinnerton-Dyer conjectures*,
[arXiv:2308.08875v1, Section 2, PDF pages 10--16](https://arxiv.org/pdf/2308.08875v1#page=10),
for the known determinant descent construction. Its domain retains
the dual H^2 factor. This example verifies applicability and computes
that construction; it does not reprove the general descent theorem.
The [saved assessment](../drafts/literature/2026-10-03-cyclotomic-kato-derivative.md)
already screened this exact model test.

The meanings of finite, strict, and relaxed local conditions and their
adjoint maps are the mapping-fiber/Poitou--Tate conventions in
[the duality foundation](../foundations/10-selmer-bockstein-duality.md):
Nekovar, *Selmer complexes*, Theorem 6.3.4 and Section 11.1.3.
Here compatibility with that formal package is checked explicitly;
the complexes are not asserted to compute arithmetic cohomology.

## Conclusion

There is an explicit model with all the following properties:

- Global Iwasawa H^1 is free of rank one, global H^2 is R/(t), and
  their base cohomological dimensions are respectively two and one.
- The first global Bockstein is onto, with no higher-degree block.
  A determinant element descends to a nonzero degree-one leading
  class, with the H^2-dual factor and the descent square retained.
- A finite local line, a localization map, the ordinary and strict
  mapping fibers, and their inverse-parameter duals are compatible.
  The ordinary base Selmer space S has dimension two and nonzero
  finite p-localization.
- The ordinary Iwasawa dual X has characteristic generator t^2;
  the formal reciprocity scalar attached to the determinant element
  is also t^2. Thus Kato's characteristic divisibility holds, even
  with equality, and the scalar has a nonzero quadratic coefficient.
- The marked rational Kummer subspace W has dimension one, its
  localization is injective, and the marked V_p Sha quotient S/W
  has dimension one. The nonzero strict vector is outside W.

In fact the degree-one leading class itself belongs to W. Nevertheless
its determinant preimage has a nonzero image in
(W tensor_F (S/W)) tensor_F H^2(C_0)^dual. Since wedge^2 W = 0,
there is no nonzero rational exterior-square preimage.

Consequently the listed formal data, even together with rationality
of the leading vector, do not force rational rank two. This supplies
an informative negative result for that inference, not a counterexample
to BSD or to a statement about the actual Kato element. Existence,
degree, and nonvanishing of the actual derivative, its arithmetic
determinant preimage, and production from analytic rank two remain open.

## Proof

**Global and local complexes.** All matrices are already defined over
Lambda; localize at (T) for the determinant calculation. Put

\[
C=[R e_1\oplus R e_2\xrightarrow{\ d\ }R f],
\quad d(e_1)=0,\quad d(e_2)=t f.
\tag{2}
\]

The relaxed global complex is C. At p take L concentrated in degree
one with L^1 = R a + R b, and finite local complex U = R a, also
in degree one. Its local Tate form is the perfect sigma-sesquilinear
form

\[
\langle u a+v b,u'a+v'b\rangle
   =u\sigma(v')+v\sigma(u').
\tag{3}
\]

It is symmetric at the fiber: the degree-one cup-product sign and the
alternating coefficient pairing give two signs. In particular U is
its own annihilator and L/U is dual to U. Define a cochain localization
map ell_R:C -> L by

\[
\ell_R(e_1)=a+t b,\qquad\ell_R(e_2)=0.
\tag{4}
\]

This is a chain map since L^2 = 0. Its image is isotropic for (3):
the pairing of localizations of x_1 e_1+x_2 e_2 and y_1 e_1+y_2 e_2
is x_1 sigma(y_1)(sigma(t)+t) = 0. Thus the reciprocity identity is
retained, including the inverse parameter; an alternating form on
local H^1 would give the wrong identity here.

Choose mapping-fiber signs so its degree-two differential is the
global differential together with localization. The ordinary fiber
Fib(C direct-sum U -> L) is

\[
[R^2\oplus R a\longrightarrow R f\oplus R a\oplus R b],
\quad (x_1,x_2,u)\longmapsto (t x_2,x_1-u,t x_1).
\tag{5}
\]

Cancel the unit differential from u to the a-coordinate. This gives
the quasi-isomorphic ordinary complex

\[
C_f=[R^2\xrightarrow{t\,\mathrm{id}}(R^2)^dual],
\quad e_1^dual=b,\quad e_2^dual=f.
\tag{6}
\]

Equivalently this is the fiber of C -> L/U, whose degree-one map is
(x_1,x_2) |-> t x_1 b. The strict fiber C_00 = Fib(C -> L) is

\[
[R^2\longrightarrow R f\oplus R a\oplus R b],
\quad (x_1,x_2)\longmapsto(t x_2,x_1,t x_1).
\tag{7}
\]

**Duality and the triangles, not just dimensions.** For a two-term
complex [A -> B] use the signed inverse-parameter dual
[B^dual -> A^dual] with differential -sigma(d)^transpose.
Since sigma(t) = -t, (6) identifies with its dual by evaluation.
The signed dual of C is

\[
D=[R f^dual\xrightarrow{t e_2^dual}(R^2)^dual].
\tag{8}
\]

There is a quasi-isomorphism P:C_00 -> D given by

\[
P^1(x_1,x_2)=x_2 f^dual,\qquad
P^2(y,u,v)=(v-t u)e_1^dual+y e_2^dual.
\tag{9}
\]

Indeed P^2 d(x_1,x_2) = t x_2 e_2^dual = d_D P^1(x_1,x_2).
The kernel is the acyclic unit complex R e_1 -> R(a+t b).
The restriction of P^2 to L is exactly the adjoint of (4) under
(3), namely (u,v) |-> (v-t u)e_1^dual. Thus strict/relaxed
duality has the correct local boundary, rather than an arbitrary
pairing on unrelated vector spaces.

For completeness the map C_f -> C is the identity in degree one
and (alpha,beta) |-> beta f in degree two. Its dual maps f^dual
to e_2 and is the identity in degree two. Compose this dual map
with P. The resulting map C_00 -> C_f differs from the natural
map, (identity, (y,u,v) |-> (v,y)), by the chain homotopy

\[
h:R f\oplus R a\oplus R b\longrightarrow R^2,
\qquad h(y,u,v)=u e_1.
\tag{10}
\]

In degree one the difference is x_1 e_1 = h d(x_1,x_2);
in degree two it is t u e_1^dual = d_f h(y,u,v).
The local-condition maps therefore agree with the dual maps up to
this explicit homotopy. The ordinary/relaxed triangle and the
strict/ordinary triangle are the actual mapping-fiber triangles.

At the fiber, S = H^1(C_f,0) = F e_1 + F e_2,
H^2(C_f,0) = S^dual, and H^1(C_0) = S. Finite localization is
ell(x_1 e_1+x_2 e_2) = x_1 a. Its rank is one, and
H^1(C_00,0) = F e_2. The ordinary/relaxed exact sequence is

\[
0\longrightarrow S\xrightarrow{\mathrm{id}} S
\xrightarrow{0}F b
\xrightarrow{b\mapsto e_1^dual} S^dual
\xrightarrow{e_1^dual\mapsto0,\ e_2^dual\mapsto f}F f
\longrightarrow0.
\tag{11}
\]

The boundary is adjoint to finite localization, since
<a,b> = 1. In the strict/ordinary triangle finite localization
is onto U_0, so its next boundary is zero and the map on H^2
is an isomorphism. These checks retain both local conditions and
all relevant base duality maps. Conditions away from p may be
taken acyclic; no assertion about Galois realization is used.

**Degree and determinant descent.** From (2),

\[
H^1(C)=R e_1,\qquad H^2(C)=R/(t)f;
\quad H^1(C_0)=S,\quad H^2(C_0)=F f.
\tag{12}
\]

Thus the basic rank is one and e = dim H^2(C_0) = 1; this index is
cohomological and is not identified with the marked rational rank.
The first Bockstein is obtained by lifting a base cocycle and
dividing its differential by t:

\[
\beta(e_1)=0,\qquad \beta(e_2)=f\otimes\bar t.
\tag{13}
\]

It is onto. The only torsion augmentation block has length one,
so Sano's Proposition 2.10 gives degree varrho = 1. There is no
unaccounted higher Bockstein or first-cokernel defect. These free
two-term complexes and their free rank-one H^1 satisfy the localized
complex hypotheses for Theorem 2.13.

Use the cohomological determinant convention: for degrees one and
two the inverse determinant line is
det_R^(-1)(C) = wedge^2 C^1 tensor (C^2)^dual. With a common
orientation put delta = (e_1 wedge e_2) tensor f^dual in this line.
The generic determinant trivialization Theta sends it to

\[
z=\Theta(\delta)=t e_1\in H^1(C).
\tag{14}
\]

To compute this value, split C^1 as the kernel R e_1 and its
complement R e_2; the complement maps to t f, contributing t to
the determinant. This is a calculation of the particular normal
form, not another proof of the general descent theorem.

The specialized determinant domain is
wedge^2 S tensor (F f)^dual. For this orientation the first
regulator sends (v_1 wedge v_2) tensor phi to

\[
\bigl(\phi(\beta_1(v_2))v_1-
       \phi(\beta_1(v_1))v_2\bigr)\otimes\bar t,
\tag{15}
\]

where beta_1 is the f-valued coefficient in (13). In particular
the image of delta_0 is e_1 tensor bar t. The other path through
Sano's descent square takes Theta(delta), divides by t and
specializes, also giving e_1 tensor bar t. It is nonzero.
Changing the common orientation changes both signs, not the
conclusion. The f^dual factor was explicitly evaluated, not
discarded or confused with a second rational point.

**Characteristic divisibility and the marked Kummer quotient.**
From (6), X = H^2(C_f) = (R/(t))^2 and H^1(C_f) = 0. The same
complex over Lambda gives X_Lambda = (Lambda/(t))^2 with
characteristic generator t^2. It has no nonzero finite submodule,
and its augmentation specialization has dimension two after
inverting p. Its two augmentation blocks have length one, so
the augmentation semisimplicity defect is zero.

The quotient localization q_R:C -> L/U sends e_1 to t b.
Use b to trivialize this line. Then

\[
\mathcal L=q_R(z)=t^2=f_X\cdot1,
\qquad \operatorname{ord}_T\mathcal L=2.
\tag{16}
\]

The T^2 coefficient is exactly one since t = T + O(T^2).
This models the divisibility and scalar reciprocity data; it is
not identified with any elliptic curve's actual p-adic L-function.

Mark W = F e_1 as the rational Kummer image and A = S/W = F e_2
as the V_p Sha quotient. A rank-one rational lattice Z e_1 maps
injectively to W and its local logarithm sends n e_1 to n;
thus no nonzero rational lattice vector has zero logarithm.
One can also retain the base integral Kummer sequence by taking
the discrete Selmer group (F/Z_p)^2, its rational image
(F/Z_p)e_1, and Sha quotient (F/Z_p)e_2. The Tate module of
that quotient, tensored with F, is A. Exact base control is
compatible with X_Lambda/T X_Lambda = Z_p^2. No finiteness of
the marked Sha quotient is imposed.

The strict vector kappa = e_2 is nonzero but its image in A is
nonzero. The normalized leading vector z/t mod t = e_1 belongs
to W and has nonzero localization. Its unique nonzero determinant
preimage, however, is delta_0. For the exact sequence
0 -> W -> S -> A -> 0 there is a canonical identification
wedge^2 S = W tensor A: send e_1 wedge e_2 to e_1 tensor
(e_2 mod W). Consequently delta_0 has a nonzero mixed component
in (W tensor A) tensor (F f)^dual, whereas wedge^2 W is zero.

The achieved data are Selmer dimension two, characteristic order
two, no augmentation defect, and a nonzero degree-one descent.
The missing lower bound is still dim W >= 2: here dim W = 1
and dim A = 1. The marked rational rank has not improved. A new
arithmetic input would have to exclude the mixed W/Sha component
of the determinant preimage; rationality of its contracted leading
vector already holds in this model and does not do that.

This differs from L002's characteristic/Jordan-block ambiguity and
L011's anticyclotomic strict/relaxed test: the cyclotomic first
Bockstein, its exact degree-one descent, reciprocity, and compatible
local triangles have all been included. Those lemmas are contrasts,
not mathematical inputs to the present construction. Sano's formalism
is reproduced in a concrete model; no originality is claimed.

The exact polynomial checks are reproducible with
`python3 scripts/cyclotomic-determinant/check_model.py`. They verify
the chain maps, inverse-parameter duality, adjoint local boundary,
homotopy, fiber exactness, Bocksteins, determinant descent and
characteristic/scalar orders. The proof above establishes the model
over Lambda and R, rather than infer it from numerical samples.

## Mathlib

Full coverage of this marked-Kummer/Sha formal model: **not checked**.
Supporting mapping fibers, dual complexes, Bocksteins, determinant
lines, and exterior powers: **not checked**. Sano's Definition 2.7,
Proposition 2.10 and Theorem 2.13, and Nekovar's Theorem 6.3.4 with
the conventions linked above, support the construction and duality;
none is asserted as a full arithmetic rationality theorem or a
Mathlib match. No absence claim follows from an optional lookup
not being performed.
