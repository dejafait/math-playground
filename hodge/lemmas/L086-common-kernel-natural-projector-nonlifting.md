# L086 — Natural kernel endomorphisms do not lift the image projectors

## Hypotheses

Assume exactly the conditional hypotheses of L079: the marked K3
product with identical hyperkähler metrics, locally free holomorphic
rank-two Omega-polystable F, integral c_1(F)=0, and full character
ch_2(F)=-9e_1-10e_2-tau_D. Use its compatible connection from L071
and both actual compatible images G=R^1p_2*F, H=R^1p_1*F from L079.
No F existence, inverse transform or fullness is assumed. Retain all
L079 branches, with common trivial multiplicity t=1 or t=2.
For a bundle V with the specified Chern connection write End_parallel(V)
for its algebra of complex-linear parallel global endomorphisms.

## Conclusion

The natural complex-algebra maps

\[
\rho_2:End_{parallel}(F)\longrightarrow End_{parallel}(G),\quad
\rho_1:End_{parallel}(F)\longrightarrow End_{parallel}(H),
\qquad \rho_i(a)=R^1p_{i*}(a),
\]

have ranges exactly C id_G and C id_H respectively; their joint range
is {(c id_G,c id_H):c in C}. Their only image idempotents are zero
and identity. The parallel projections P_G and P_H onto the full
trivial isotypic summands are not in these ranges. In every branch,
rank(P_G)=rank(P_H)=t with 0<t<5 and 0<t<6.

Thus these projectors do not lift to parallel kernel endomorphisms,
even without requiring the proposed lifts to be idempotent. This stops
only natural projector lifting. It does not exclude F or either image,
construct a cycle, identify actual nontrivial blocks or establish transport.
This is a REPRODUCTION/specialization of the assessed known tools.

## Proof

**Scalar domain.** L071 proves stability of F under these exact
hypotheses: product line splitting would annihilate the holomorphic
mixed action, whereas the prescribed action is nonzero. Its compatible
unitary connection is already supplied there. A parallel endomorphism
is holomorphic because the (0,1) connection is the Dolbeault operator.
Use the stable scalar-endomorphism consequence of the parallel-morphism
and constant-rank splitting theorem in Perego, *Kobayashi--Hitchin
corrispondence for twisted vector bundles*, Complex Manifolds **8**
(2021), Propositions 3.9--3.12 and 3.15, pp. 36--38,
[inspected published text](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36).
Trivial twisting and zero B-field apply. The compact product is Kähler;
source and target are the same zero-Einstein bundle. In this parallel
case, a nonscalar endomorphism would have a nonzero proper parallel
kernel after subtracting one of its constant eigenvalues (including
a nonzero nilpotent part). Its connection-preserving orthogonal
complement splits F into holomorphic zero-slope subbundles, contrary
to stability. Thus End_parallel(F)=C id_F. All constant scalars are
indeed parallel. This is the necessary applicability argument, not a
reproof of preservation or inversion.

**Natural maps and connections.** Higher direct image is a covariant
C-linear functor on sheaf morphisms, so R^1p_i* preserves composition
and identity. L079 has already established everywhere odd concentration,
base change, local freeness and the actual compatible image connections,
using BBHR, *A hyperkahler Fourier transform*, Differential Geometry
and its Applications **8** (1998), Definition 2, Lemmas 1--2 and
Theorem 3, pp. 243--246,
[primary text](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
Those input hypotheses are unchanged. On every base-change fibre,
R^1p_i*(c id_F) is multiplication by c on H^1 of the restricted F.
Consequently it is globally c id on the actual image bundle. Such
an endomorphism is parallel for any C-linear connection, in particular
for these specified connections. This verifies connection compatibility
for the entire domain without asserting a broader unproved naturality
or reconstructing any kernel morphism. The two positive ranks are five
and six, so each range is exactly its scalar line, and the joint scalar
is the same c. The alternating derived class -[G] or -[H] does not
change the morphism on the positive R^1 bundle.

**Projectors in all branches.** L079 supplies polystability and the
complete trivial multiplicity t=1 or 2 in each image. Choose the
orthogonal projection onto its trivial isotypic subbundle; it is a
holomorphic endomorphism. On either factor the image connection has
zero Einstein function, so the same Perego parallel-morphism theorem
makes this projection parallel. Equivalently its Hermite--Einstein
summand decomposition is connection-preserving. The nontrivial residual
ranks are 5-t and 6-t, both positive for both allowed t. Hence each
projector has eigenvalue one on a nonzero summand and zero on a nonzero
complement. It cannot equal c id. Scalar idempotents satisfy c^2=c,
so the images contain only zero and identity as idempotents. No branch,
including repeated or dual-paired residual blocks, changes this rank
argument. Individual trivial-line projectors are also nonlifting.

**Known traps and limits.** The direct-image functor here varies the
kernel morphism, not its input object. No inverse, fully faithful functor
or whole-moduli identification is imported. Failure of surjectivity on
these morphism spaces is consistent with existence of F: a simple kernel
may have nonsimple direct images. No contradiction follows merely from
nonlifting. The full negative mixed tensor, identical metric and integral
first class have been retained; no positive-tensor stop or topological
index exclusion has been substituted.

## Mathlib

Full coverage of these natural parallel kernel-endomorphism maps and
this exact nonlifting specialization is not checked. The cited results
are mathematical inputs; unknown Mathlib coverage is not absence.
