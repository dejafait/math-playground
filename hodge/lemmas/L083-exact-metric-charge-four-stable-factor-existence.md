# L083 — An exact-metric stable locally free charge-four factor

## Hypotheses

Let S be precisely L052's smooth projective complex K3 surface and h
its real ample class, with integral Picard lattice satisfying

\[
\operatorname{NS}(S)\cap h^\perp=\mathbb Z k,
\qquad k=(-4,-2,1,2),\qquad k^2=-14.
\tag{1}
\]

Slope stability is strict stability for coherent torsion-free sheaves
against the indicated ample class. Let eta be the integral point class,
with integral_S eta=1. No product bundle or prescribed transform exists
by hypothesis. The target is the individual factor prerequisite only.

## Conclusion

There exists an algebraic locally free rank-two bundle E_4 on S with

\[
\det(E_4)\simeq\mathcal O_S,\qquad c_2(E_4)=4\eta,
\qquad E_4\text{ slope-stable at the exact real }h.
\tag{2}
\]

It is acyclic and its determinant wedge gives a perfect alternating
O_S-valued form. Thus it meets the individual E_4 requirements in
L079's t=1 repeated-block alternative. It supplies neither a common F
with the opposite image nor the prescribed mixed tensor or transport.
This is a REPRODUCTION/specialization of known tools, a local advance
toward a prerequisite, with no new Hodge-class algebraicity claimed.
The separate critical audit below preserves this specialization.

## Proof

**Precise imported inputs.** Use Yoshioka, *Irreducibility of moduli
spaces of vector bundles on K3 surfaces*,
[math/9907001v2, 7 February 2000](https://arxiv.org/pdf/math/9907001v2#page=5),
Corollary 0.3 (p. 2), the condition (♮) in Sections 0.2 and 1.1
(pp. 2, 4), and Lemma 1.5 (p. 5). The latter applies to arbitrary
positive-rank Mukai vectors at a general polarization and gives slope-
stable nonemptiness from slope-semistable nonemptiness when
v^2/2>=ell(v)^2, including equality. Here ell(v)=gcd(rank(v),c_1(v)).
Its all-rank-one filtration case is supported by Yoshioka,
*An application of exceptional bundles to the moduli of stable sheaves
on a K3 surface*,
[alg-geom/9705027v2, 18 June 1997](https://arxiv.org/pdf/alg-geom/9705027v2#page=11),
Lemma 4.4 and Remark 4.1, pp. 10–11, as inspected in the approved
assessment. We import Lemma 1.5 in full; neither its abbreviated
filtration calculation nor a primitive-only freeness theorem is being
substituted for it.

For bounded chambers use O'Grady, *Modular sheaves on hyperkähler
varieties*, Algebraic Geometry 9 (2022), 1–38,
[Definition 1.1, Definitions 3.1–3.3 and Propositions 3.4, 3.8, 3.10](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf#page=8),
pp. 2, 7–10. On a K3 surface n=1, the BBF form is the cup form,
the normalized Fujiki constant is c_S=1, and (-1)!!=1. Thus
Definition 1.1 is automatic with d(T)=integral_S Delta(T).
Here Delta(T)=2 rank(T)c_2(T)-(rank(T)-1)c_1(T)^2=16 eta,
so d(T)=16 and Definition 3.3 gives a(T)=rank(T)^2 d(T)/(4c_S)=16.
The 16-walls are orthogonal
to integral xi with -16<=xi^2<0; they are locally finite in the real
ample cone. Stability at integral ample rays is constant in an open
16-chamber. As in L053, only this divisor-class assertion is imported;
stability at the real endpoint will be proved below.

Use L052's exact perpendicular lattice and stable Euler test. The
surface Riemann–Roch, Serre duality and dual-stability inputs behind
that test are Huybrechts, *Lectures on K3 Surfaces*, author-hosted draft,
[Chapter 1, (2.5)–(2.6) and Proposition 2.4, pp. 11–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and [Chapter 9, Section 3.1, pp. 175–176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
The applicability checks that follow are needed because no inspected
theorem asserts the entire nonprimitive exact-h conclusion (2).

**An integral polarization satisfying the source hypotheses.** By
(1), any 16-wall through h has xi=rk, with nonzero integer r and
14r^2<=16. Its hyperplane is therefore k^perp. Choose a small convex
ball B about h within the real ample cone meeting no other 16-wall;
local finiteness permits this. Either component B_+ of B minus k^perp
lies in one open 16-chamber. Choose a rational ample alpha in B_+
and a positive integer multiple H that is an integral ample divisor
class. Scaling preserves slope comparisons and chambers. In particular
h itself is on an artificial wall of this bounded wall set; it has
not been treated as a point of an open chamber.

We verify (♮) and generality for v=(2,0,-2). If a rank-two slope-
semistable torsion-free sheaf T with c_1=0,c_2=4 has an equality-slope
rank-one subsheaf, its saturation cannot introduce a nonzero divisor:
that divisor would increase slope above zero and violate semistability.
After saturation the exact sequence has the form

\[
0\longrightarrow L\otimes I_Z\longrightarrow T
\longrightarrow L^{-1}\otimes I_W\longrightarrow0,
\qquad 4=\operatorname{length}(Z)+\operatorname{length}(W)-l^2,
\tag{3}
\]

where l=c_1(L). Indeed rank-one torsion-free sheaves on a smooth
surface are line bundles tensored with finite-point ideals, and the
displayed identity follows by taking Chern characters. If l.H=0
and l is nonzero, Hodge index and (3) imply -4<=l^2<0. Then
xi=2l satisfies -16<=xi^2<0 and xi.H=0, contrary to the choice
of H. Hence every equality-slope rank-one subsheaf has l=0, which
is precisely equality of normalized first classes as required by (♮).
There are no other proper positive ranks to check.

Every polarization wall where a semistable rank-two object acquires a
nonzero equality class is among these bounded walls by the same
calculation. With l=0 the remaining reduced Hilbert polynomial
comparison is independent of polarization: on a K3 the constant term
for L tensor I_Z is 2-length(Z), while T's is chi(T)/2=0.
Equality requires both lengths in (3) to be two and persists for
all polarizations. Such persistent equality is permitted for a
nonprimitive vector; it does not prevent H from being general in
Yoshioka's wall sense. Thus we have checked generality rather than
assumed a rational ray avoids an unspecified countable set.

**Nonprimitive slope-stable existence at equality.** The numerical
application is

\[
v=(2,0,-2)=2w,\quad w=(1,0,-1),\quad w^2=2,
\quad v^2=8,\quad \ell(v)=2,\quad v^2/2=4=\ell(v)^2.
\tag{4}
\]

Corollary 0.3 gives Gieseker-semistable nonemptiness at general H,
and hence slope-semistable nonemptiness. An explicit check is
I_Z direct sum I_Z for any length-two Z: its rank-one factors are
Gieseker-stable with vector w and identical reduced Hilbert polynomials.
This check supplies nonemptiness only, not the desired stable bundle.
Lemma 1.5 applies at the equality in (4), with properly slope-semistable
codimension lower bound 8/(2*2)-2+1=1. It therefore yields an
H-slope-stable torsion-free sheaf T of vector v. No primitive-only
existence, irreducibility or local-freeness assertion is used here.

**Every stable point has no point defect.** Put B_T=T**. On a smooth
surface a reflexive sheaf is locally free, and the quotient B_T/T
has finite length t>=0. For any rank-one subsheaf A of B_T,
A intersect T has the same rank and first Chern class: their quotient
injects into B_T/T and is supported at points. A slope at least zero
would therefore contradict H-stability of T. Consequently B_T is
H-stable, with c_1=0 and second Chern number 4-t.

The stable Euler argument does not depend on this particular real
polarization: at the ample H a section of B_T gives a rank-one
subsheaf of nonnegative slope, and dual stability kills sections of
B_T^vee as well. Serre duality gives H^0(B_T)=H^2(B_T)=0.
Riemann–Roch now says

\[
\chi(B_T)=4-(4-t)=t=-h^1(B_T)\le0.
\tag{5}
\]

Together with t>=0 this forces t=0. Thus T is itself locally free.
This argument excludes every defect length directly; there is no
need to repeat L053's Quot-dimension argument or to assume that two
separately nonempty loci intersect. Write E_4=T. Since H^1(O_S)=0,
the first-class map Pic(S) to H^2(S,Z) is injective by the exponential
sequence. Its integral c_1=0 therefore gives det(E_4)=O_S.

**Strict stability at the exact real h.** Take rational ample
alpha_j in B_+ converging to h. Each has an integral positive multiple,
and all their rays and H lie in the same open 16-chamber. The cited
chamber theorem gives slope stability of the fixed E_4 at each alpha_j.
For each fixed rank-one subsheaf A this says c_1(A).alpha_j<0.
Taking its individual limit gives c_1(A).h<=0. Since A was arbitrary,
E_4 is h-semistable. This passage exchanges no uniform bound or
infinite family of slope inequalities with a limit.

If strict stability failed, saturate an equality-slope rank-one
subsheaf. Its divisorial increase must again be zero by h-semistability
and ampleness. Equation (3) then applies to E_4, with l.h=0.
By (1), l=rk for an integer r, so

\[
4=\operatorname{length}(Z)+\operatorname{length}(W)+14r^2.
\tag{6}
\]

Thus r=0. This same subsheaf would have slope zero at H, contradicting
the original H-stability. Hence E_4 is strictly h-stable. The stable
Euler test now gives H^0(E_4)=H^2(E_4)=0 and chi(E_4)=0, so also
H^1(E_4)=0. Finally the rank-two wedge and the chosen determinant
trivialization give the asserted perfect alternating form.

**Qualifications and threshold.** Nonprimitive slope nonemptiness,
absence of every defect, integral determinant triviality and strict
exact-h stability have all passed, so (2) supplies the full individual
factor target. It is stronger than a numerical non-exclusion test.
It is still only one image-block prerequisite: even with the separately
audited J_5, no common kernel, prescribed mixed action, image
identification, transverse transport or universal primitive Hodge
algebraicity follows. L079's necessary-test stop, its t=2 alternatives,
and the flat (-10,-17) blocker remain intact.

**Separate critical audit (2026-10-10).** The approved audit checks the
written specialization, not a new construction or the general theorems.
No substantive error, stronger obstruction or stronger existence
conclusion was found. Outcome: EXPLORATION / REPRODUCTION.

The source scope is correct: math/9907001v2 Section 1.1 retains (♮),
and Lemma 1.5 on p. 5 explicitly permits an arbitrary vector and the
non-strict threshold. Equation (4) reaches that threshold exactly.
The all-rank-one case is included by that lemma, with the earlier
Lemma 4.4's exceptional r=1, ell=2 case as proof context. We do not
apply the earlier Picard-rank-one result to S. The displayed
I_Z direct sum I_Z independently verifies semistable nonemptiness;
the imported theorem, not this split example, provides stability.

For generality, every possible proper positive-rank equality test has
rank one. Saturation can add only an effective divisorial first class
and a point contribution. A nonzero divisorial addition contradicts
semistability, so the Chern identity (3) applies with the same equality
slope. Hodge index gives -4<=l^2<0 for nonzero l, and the integral
class 2l would put H on a forbidden 16-wall. When l=0 the polynomial
comparison is constant in H; the persistent length-two/length-two
equality for this divisible vector is allowed. The generality argument
therefore does not assume that every semistable sheaf is stable.

The modularity computation above explicitly verifies every parameter
needed for O'Grady Proposition 3.4(ii). Local finiteness and (1) leave
only k^perp through h, since 14r^2<=16 forces |r|=1. Positive rescaling
does not cross any of these homogeneous walls. Integral multiples of
all chosen rational rays thus satisfy the proposition's divisor-class
hypothesis. No real-boundary stability is imported from it.

For the hull, A intersect T differs from A only at points, preserving
rank and c_1; hence any destabilizer of T** would destabilize T.
Reflexivity on the smooth surface makes T** locally free. Stability,
dual stability and K_S=O_S kill its outer cohomology at H. Equation
(5) then forces t=0 for every finite defect, without a bounded-length
assumption, moduli-dimension argument or generic-freeness assertion.
The determinant argument uses integral c_1 and Picard injection.

Finally fix an arbitrary subsheaf before taking alpha_j to h. Its
limiting slope is nonpositive; this proves all h-semistability tests.
If one is equality, its saturation still has equality and a torsion-free
rank-one quotient. Equation (6) excludes every nonzero r because
14r^2>4. The remaining r=0 gives the same actual subsheaf slope zero
at H, contradicting H-stability. Thus strict endpoint stability holds,
and only thereafter do RR and determinant wedge supply acyclicity and
the alternating form. No uniform strict inequality in j is required.

The sole direct mathematical input remains L052, only for S,h and its
surface/lattice facts; no hypothetical product F is assumed. The audit
retains the individual E_4 prerequisite, with common-kernel realization,
the full prescribed mixed action, actual image identification and
transverse transport unresolved. No universal Hodge candidate results.

## Mathlib

Full matching nonprimitive slope-existence and locally free exact-real-
polarization conclusion: **not checked**. No matching declaration or
absence is asserted. This is an informal complex-algebraic proof using
the precisely cited sources, not a Lean formalization.
