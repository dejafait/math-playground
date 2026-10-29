# L129 — Covariant ordinary pushdown cannot give the proposed control

## Hypotheses

Use L123's original F=Q tower of smooth proper Shimura curves X_m,
m>=1, and Jacobians J_m, with the unchanged tame level. Retain its
modularity, conductor, residual-image, integral-CM and incoherence
assumptions: p>=5 is inert in K and split multiplicative for A;
the conductor is unramified in K, its inert part is square-free,
and its split exponents are at most two. The local argument below
does not use most of these restrictions; retaining them fixes the
actual tower under examination. Do not change the CM list, W, N,
P, M, R_0, I, invariant domains or projection maps of L128.

At p the level K_m is the projective image of matrices in
GL_2(Z_p) that are upper unipotent modulo p^m. Equivalently a
representative [[a,b],[c,d]] satisfies c in p^m Z_p and a/d in
1+p^m Z_p. The equivalence uses a common unit scalar; a and d
are units. All non-p components of K_m are independent of m.
Let pi_m:X_{m+1}->X_m be the forgetting map pi_1 of the source.
Write g for the finite adele with p-component diag(1,p) and
identity at every other finite place. Define U_m by the original
right-translation correspondence [K_m g K_m], with covariant
action on divisors, Jacobians and homology.

Choose the source's embedding into C. Put

\[
 L_m=H_1(X_m(\mathbf C),\mathbf Z)\otimes\mathbf Z_p,
 \qquad e_m=\lim_{r\to\infty}U_m^{r!}.
\]

For a disconnected curve take the direct sum over proper components.
Let mu be the prime-to-p diamond subgroup (of order p-1), put
e_mu=(p-1)^{-1} sum_{d in mu} d, and define

\[
 e_{0,m}=e_\mu e_m,\qquad C_m=e_{0,m}L_m.
\]

Every operator in these definitions is **covariant with the original
physical label**. In particular C_m is defined explicitly; it is
not identified with Fornea's controlled M_m^bullet by notation.
Products of maps mean composition, rightmost first. In right-module
notation the identity below is (x U_{m+1}) pi_m=p(x r_m);
changing notation does not replace g by g^{-1}.

Primary inputs already covered at step 535, specialized here:

- Michele Fornea, *Plectic Heegner classes*,
  [arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
  Section 2 immediately after (6), Section 2.1.2, (15),
  Definitions 2.4/2.8 and (21): the exact levels, covariant physical
  correspondence and projectors. Proposition 2.9 supplies the
  **pullback** compatibility; Section 2.4, Lemma 2.22 and Corollary
  2.23 supply the control statement against which the proposed
  replacement is tested. The control diagram is in the
  [PDF](https://arxiv.org/pdf/2603.28327v2), printed pp.17--18.
- J. S. Milne, *Jacobian Varieties*, corrected 12 June 2021,
  [Theorem 2.5, pp.7--8](https://www.jmilne.org/math/xnotes/JVs.pdf),
  for the integral Jacobian lattice; and *Abelian Varieties*, v2.0,
  16 March 2008, [I Remark 10.7, p.45](https://www.jmilne.org/math/CourseNotes/AV.pdf),
  for covariant comparison with T_p. We use the underlying geometric
  modules, not a Betti Galois action or a dual Tate action.
- E. C. Sertoz, J. Ouaknine and J. Worrell, *Computing transcendence
  and linear relations of 1-periods*,
  [arXiv:2505.20397v1, 26 May 2025](https://arxiv.org/html/2505.20397v1),
  (7.3.29)--(7.3.35), (7.4.37)--(7.4.42), with the integral transfer
  in (4.5.54)--(4.5.55). Take all markings and punctures empty.
  For finite maps between smooth proper curves, the Jacobian map
  f_{2,*} f_1^* corresponds to f_{2,*} f_1^! on homology.
  Apply componentwise; no etaleness assumption is needed.

## Conclusion

There is a finite degeneracy morphism

\[
 r_m:X_{m+1}\longrightarrow X_m,\qquad
 [z,b]_{K_{m+1}}\longmapsto[z,bg]_{K_m},
\]

and the following equality of covariant maps holds on Jacobians
and on their integral p-adic homology:

\[
       (\pi_m)_* U_{m+1}=p(r_m)_*.                 \tag{1}
\]

Consequently

\[
 (\pi_m)_*(C_{m+1})\subseteq pL_m,
 \qquad
 e_{0,m}(\pi_m)_*(C_{m+1})\subseteq pC_m.          \tag{2}
\]

If C_m is nonzero, the projected pushdown in (2) is not surjective.
In particular, there cannot be transition-compatible identifications
of these C_m with a nonzero controlled tower whose unnormalized
forgetting pushdowns have the surjectivity required in Lemma 2.22.
If the unprojected pushdown does preserve C_m, it too is not
surjective; if it does not, it already fails to define the proposed
restricted tower. This disjunction does not assume preservation.

This is an informative negative for the step-536 covariant replacement
of L128 Step 1 **with its unchanged pushdown transitions**. It does
not refute the source's control theorem in its own action conventions,
L128 (2)/(3), or possible relation transfer using a different, justified
comparison. It establishes no relation transfer to N_0, scalar,
rationality, nonvanishing, finite local membership or BSD assertion.
It is a known-method specialization (REPRODUCTION), written at step
536. **Separate conceptual audit (step 539): PASS in this restricted
integral scope.** The audit below accepts (1), (2) and the conditional
control incompatibility; it does not identify the source's transported
action. No novelty is claimed.

## Proof

**The degeneracy map exists with the original level.** Take a local
representative k=[[a,b],[c,d]] of K_{m+1}. Then

\[
 g^{-1}kg=\begin{pmatrix}a&pb\\c/p&d\end{pmatrix}.
\]

The lower-left entry lies in p^m Z_p, the determinant remains a unit,
and a/d is in 1+p^{m+1}Z_p, hence in 1+p^m Z_p. Thus
g^{-1}K_{m+1}g is contained in K_m at p. At every other finite
place the containment is equality. This proves that right translation
by g gives r_m. The usual level morphisms extend to smooth proper
curves (including the compactification in the split quaternion case).
No extra tame orientation subgroup or change of level is made.

**Multiplicity after forgetting.** Fornea's (15), at level m+1
and uniformizer p, gives the p point branches of U_{m+1} as

\[
 s_a=\begin{pmatrix}1&0\\a p^{m+1}&p\end{pmatrix},
       \qquad a=0,1,\ldots,p-1.
\]

The cosets s_a K_{m+1} are distinct; this is not an assertion that
their images are distinct at every special point. At level m, however,

\[
 g^{-1}s_a=\begin{pmatrix}1&0\\a p^m&1\end{pmatrix}
                 \in K_m,
 \qquad [z,bs_a]_{K_m}=[z,bg]_{K_m}.              \tag{3}
\]

Hence the composition which first applies U_{m+1} and then pi_m
has p copies of the graph of r_m. More formally, on the dense open
where the finite correspondence has its usual unramified point
description its pushed-forward cycle is p times that graph. The
correspondences are finite and every component dominates the source;
there is no component supported over a missing finite set. Taking
closures gives the same equality of cycles on the proper curves.
This also covers any ramified or cuspidal fibers, without replacing
their multiplicities by a count of distinct points. Covariant
functoriality on divisor classes gives (1) on Jacobians.

Under the cited integral curve/Jacobian homology comparison, a
correspondence's pullback leg becomes homological transfer and its
pushforward leg remains pushforward. Therefore exactly the same
composition and multiplicity give (1) on L_{m+1}->L_m. All maps
are defined integrally before tensoring with Z_p. There is no
division by p, degree normalization, reversed word or duality here.
This is the necessary specialization of the cited comparisons;
their general statements are not reproved.

**Restriction to the integral ordinary summand.** The finite-level
ordinary idempotent is an element of the finite physical Z_p-algebra,
so it acts on L_m as an integral idempotent. The diamond average is
integral because p-1 is a unit. It commutes with U_m. Thus C_m is
a direct summand of the finite free Z_p-module L_m and is itself
finite free.

U_m acts invertibly on e_m L_m, and hence on C_m. Explicitly,
U_m^{r!} tends to the identity on e_m L_m, so for a sufficiently
large r its reduction modulo p is invertible. The determinant of
U_m on this finite free summand is therefore a p-adic unit. Its
inverse preserves C_m because it commutes with the diamond average.

For x in C_{m+1}, choose y in C_{m+1} with U_{m+1}y=x. Equation
(1) gives

\[
          (\pi_m)_*x=p(r_m)_*y\in pL_m.
\]

Applying the integral e_{0,m} proves the second inclusion in (2).
If C_m is nonzero, C_m/pC_m is a nonzero finite-dimensional F_p
space. The map in (2) has zero image there, and so cannot be
surjective onto C_m. If pi_m actually preserves the covariant
ordinary summands, its restriction equals that projected map;
otherwise it is not a transition between them in the first place.

**The failed use of control.** The isomorphism asserted in Fornea's
Lemma 2.22 makes the underlying map from its upper homology module
to its lower one surjective: passage to the stated coinvariants is
already a surjection. The proposed covariant replacement needs the
same fact for the C_m and the same pi_m. Equation (2) excludes it
at every nonzero target. A transition-compatible isomorphism of
towers would preserve surjectivity, so cannot repair this conflict.
The finite-diamond projection has already been included and cannot
remove the factor p.

For the intended L128 application the controlled tower is nonzero:
its classical conductor-level fiber contains the weight-two A
constituent, ordinary at the split multiplicative p. This is the
retained modularity/Jacquet--Langlands input, made explicit in
Fornea Proposition 2.24 and the first identification in the proof
of Proposition 2.25, printed p.18. If a proposed C_m were zero,
it could not be identified with this nonzero controlled module;
if nonzero, (2) gives the transition contradiction. The argument
does not need a new assertion about the size of a physical quotient
or a faithful action on points.

The bound achieved is exact: the proposed projected pushdown has
zero reduction modulo p, whereas the required surjection onto a
nonzero free integral lattice has nonzero reduction. The first
failed handoff is therefore the import of pushdown control for
the original-label covariant ordinary summands. The finite-level
covariant comparisons themselves remain valid. Source Proposition
2.9 concerns pi_m^* on the coefficient **direct** system; it does
not assert the covariant pi_{m,*} control needed here. Its validity
does not contradict (1). Neither faithful Tate detection nor
completion is reached, so neither supplies a missing transfer.

No claim is made here to identify exactly the source's transported
homology convention or to refute its printed theorem. Determining
that convention or changing a transition would be a separate target.
This attempt stops at the prescribed first failed map. L128's old
dual-action argument and ATTEMPTS/061/062 retain their distinct
failure evidence; the new obstruction is the p-divisibility of the
unchanged covariant pushdown, not the old diamond-inverse observation.

### Separate conceptual audit, step 539 (2026-10-28)

**Scope and verdict.** PASS for (1), (2) and their conditional integral
control comparison. The following independent checks make the branch
count, proper-cycle multiplicity and ordinary restriction explicit.
They use the same g, K_m, pi_m and covariant actions as above. They
do not audit Fornea's entire control proof or reconstruct its transported
homology action. L128 remains on HOLD.

**Coset exhaustiveness and proper-map factorization.** Put n=m+1 and
H=K_n intersect g K_n g^{-1}. The condition g^{-1}kg in K_n says exactly
that the lower-left entry c of k is in p^{n+1} Z_p; the other conditions
are unchanged. This follows from the first displayed conjugation in
the proof and is unaffected by a common unit scalar.
For t_a=[[1,0],[a p^n,1]], every k=[[A,B],[C,D]] in K_n has a unique
class a modulo p such that C-a p^n A is in p^{n+1} Z_p, since A is a
unit. Then t_a^{-1}k lies in H: its lower-right entry is D-a p^n B,
and its diagonal ratio is still 1 modulo p^n. Conversely
t_b^{-1}t_a lies in H exactly when a=b modulo p. Thus

\[
 K_n=\coprod_{a\bmod p}t_aH,\qquad
 K_ngK_n=\coprod_{a\bmod p}t_agK_n,
 \qquad t_ag=s_a.
\]

This verifies the complete decomposition and its orientation against
Fornea (15), rather than checking only the displayed representatives.
Let Y be the smooth proper curve of level H, with maps
q:Y->X_n (forgetting) and v:Y->X_n (right translation by g).
The covariant correspondence is v_* q^*. The degree of q over each
target component, summing source components, is p: the p cosets give
its generic fiber, where the projective arithmetic action has trivial
stabilizer. Elliptic points and cusps do not alter the generic degree.
On the proper curves,

\[
             \pi_m\circ v=r_m\circ q.
\]

Indeed both maps send [z,b]_H to [z,bg]_{K_m} on the open Shimura
curve, and their extensions agree by separatedness. The image of
the correspondence in X_n times X_m is therefore supported on the
graph of r_m with total multiplicity p. Equivalently, on Jacobians,

\[
 (\pi_m)_*v_*q^*=(r_m)_*q_*q^*=p(r_m)_*.
\]

The norm/pullback identity q_*q^*=p counts ramification multiplicities
on divisors and holds on Pic^0, including disconnected components.
This verifies the cycle argument at all fibers without treating
ramified fibers as sets of distinct points. It is an alternative
verification of (1), not a new degeneracy map or normalization.

**Integral transfer and ordinary image.** Apply the cited Milne
Jacobian lattice comparison and Sertoz--Ouaknine--Worrell
(4.5.54)--(4.5.55), (7.3.31)--(7.3.35), (7.4.40)--(7.4.42) to q and v
with empty markings/punctures. The covariant operator becomes
v_*q^! on H_1, so q_*q^!=p integrally by the same comparison.
Smooth proper characteristic-zero components meet the hypotheses;
neither etaleness nor a rational basepoint nor good reduction at p
is required. Tensoring these integral identities with Z_p proves (1)
on the lattices. No dual action or rational-only comparison is used.

The finite physical algebra and its factorial-power idempotent are
the ones in Fornea Definition 2.8 and (21). The diamond elements
normalize K_n and are represented by diagonal matrices commuting
with g; conjugation therefore fixes K_ngK_n. Their covariant action
commutes with U_n. Since p-1 is a unit, e_{0,n} is an integral
idempotent, and C_n is a saturated direct summand of L_n.
The restriction of U_n^{r!} tends to the identity on C_n; reducing
modulo p shows that U_n is invertible there, with inverse over Z_p.
For x=U_n y in C_n, equation (1) gives pi_*x=p r_*y. Projecting by
e_{0,m} gives an element of p C_m. This argument does not require
r_*y to be ordinary or pi_* to preserve the ordinary summand.
If pi_* does preserve it, saturation also gives
C_m intersect p L_m = p C_m. Thus both branches of the conclusion's
preservation disjunction are justified. For C_m nonzero, freeness
implies C_m/p C_m nonzero, which is the exact failed surjectivity
threshold; inverting p would erase this test and is not authorized.

**Conditional control comparison.** Fornea Lemma 2.22 states that
the map induced by forgetting is an isomorphism after base change
along the surjection Lambda_{m+1}^bullet -> Lambda_m^bullet. The
canonical map to that base change is a quotient map: every tensor
x tensor a is (a' x) tensor 1 for a lift a' of a. Hence the underlying
forgetting map in that theorem is surjective. Its printed diagram
on PDF p.18 labels the horizontal arrows (pi_1)_*. This comparison
does not replace them by pi_2, normalize them by p^{-1}, or change
g to g^{-1}. The source's coefficient pullback compatibility in
Proposition 2.9, including both intermediate p-level cases, is a
different assertion and supplies none of those substitutions.

The controlled target needed in the proposed application is nonzero
already at level one. The modular weight-two constituent of A has
trivial character, is new at its conductor primes and is ordinary
at split multiplicative p. It therefore occurs in the classical
conductor-level space identified in the proof of Proposition 2.25;
the Eichler--Shimura identification in Proposition 2.24 gives nonzero
M_1^bullet tensor Q_p. This uses the stated source identifications,
not a new claim about the dimension of covariant C_1. A hypothetical
integral isomorphism C_1 -> M_1^bullet would force C_1 nonzero, and
commuting with the forgetting transition from level two would then
contradict (2). If C_1 is zero, that hypothetical isomorphism fails
already. Thus no nonzero-target case is being assumed away.

The primary version checked is Fornea arXiv:2603.28327v2, 13 April
2026: the levels after (6), (15), Proposition 2.9's complete proof,
(21), Remark 2.12, and Section 2.4 through the first identification
in Proposition 2.25. HTML omits the control diagram; PDF pp.17--18
text supplies its labels. The attempted PDF screenshot did not display
an image, so no visual verification is claimed. Surjectivity already
follows from the fully inspected theorem statement, independently
of diagram layout. The step-535 integral-comparison coverage is reused.

No substantive conclusion of step 536 was overturned. Its phrase
about distinct branches was clarified to distinct cosets, not every
special fiber. This audit validates a local known-method obstruction;
it neither proves an error in the source's theorem in its own
conventions nor restores L128's coefficient transfer, scalar or signs.

## Mathlib

The full Shimura-tower statement, the integral correspondence
comparison and the ordinary-projector control application are
**not checked**. Supporting matrix multiplication and finite free
module facts are not asserted to constitute a matching theorem.
No absence claim or formal verification is made. The mathematical
checks here are the displayed exact matrix identities, the cycle
multiplicity and the integral image argument; no numerical script
or computational certificate is needed.
