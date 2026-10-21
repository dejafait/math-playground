# Flat-image orthogonal residual — completed source comparison

TARGET: Determine whether relative Serre duality and orthogonal-bundle constraints exclude the rank-seven acyclic remainder forced by L058 at the exact h.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped duplicate/failure search and theorem searches for relative coefficient duality, graded pairing signs, K3 orthogonal-bundle existence, autodual Nahm transforms and real characteristic classes; queries and inspected primary statements are recorded below.
SOURCE_EVIDENCE: Stacks 48.19(2),(9), 48.3.6 (0A9Q), 48.15.7 (0BRT), 15.59 (0GWN); Perego (2021), Propositions 3.9--3.12 and 3.15, pp. 36--38; Cadek--Vanzura (1993), author manuscript Section 2, Theorems 1 and 3; Abuaf--Boralevi 1312.0963v1, Theorem 3.4; Bhosle (1986), introductory theorem, pp. 29--30.
COMPARISON: Known tools cover coefficient duality, its Koszul sign, connection-compatible holomorphic morphisms and a bounded orthogonal characteristic/index test; inspected existence theorems do not settle the rank-seven acyclic bundle at this exact S,h. No pairing or obstruction for K is established in this source-only step.
GAP: Specialize the determinant/relative-duality pairing to H, justify its sign and perfect restriction to K and connection compatibility, then test orthogonal topology and adjoint RR without imposing stable rank seven, zero c_1 on every summand, a spin lift or w_4=0.
REASON: Primary coverage now supports one separate bounded necessary-constraint attempt; no exact residual existence/exclusion theorem was matched, and no originality is inferred from the search. Further existence work remains outside this scope.
SCOPE: Exact L044 S,h,tau_D; hypothetical locally free rank-two product-polystable F with L048's full character at (-10,-17); L052 factor connections/line lattice; L056--L057 flat G; L058 H=O_S^2 plus acyclic K. Only determinant duality, holomorphic and parallel pairing descent, real orthogonal characteristic constraints and adjoint/exterior-square RR with all polystable cases are covered. No inverse, faithfulness, general orthogonal existence, curvature-positivity or reconstruction test is covered.

## Gap and preserved proposal

The main local gap is compatible global realization of the nonzero mixed
cubic action. Transverse transport and universal primitive rational Hodge
algebraicity remain independent gaps. The intermediate target is the
extra structure on L058's rank-seven acyclic residual, c_1=0,c_2=14.
A rigorous incompatibility could eliminate the flat exception; compatibility
would supply neither K nor F. The initial REVIEW_REQUIRED proposal
introduced this different mechanism after the two-projection/cohomology
stop, without assuming a pairing. This review preserves that target and
stop evidence, and establishes no new mathematical consequence for K.

## Inspected primary statements and essential cases

**Coefficient duality.** Read
[Stacks Section 48.19, parts (2) and (9)](https://stacks.math.columbia.edu/tag/0AU3),
with [Lemma 48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q)
and [Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT),
live versions accessed 2026-10-05. For a proper morphism of finite-type
separated schemes over a Noetherian base, (2) gives
Rf_* RHom(A,f^!B) = RHom(Rf_*A,B), with A bounded-above coherent
and B bounded-below quasicoherent. For smooth proper relative dimension
d, (9) identifies f^!B with Lf^*B tensor Omega^d[d].
Either projection here is smooth projective of relative dimension two
over a Noetherian K3; F is a vector bundle and the intended B is O_S.
These hypotheses fit without a generic or rational polarization.
The 0A9Q proof uses adjunctions and the projection formula, initially
asserting an isomorphism after quasicoherator DQ; 48.19 gives the proper
coherent formulation. The 0BRT proof uses the smooth diagonal's conormal
and retains the shift d. Earlier Stacks 0G8I was inspected but its
pairing for differential forms is not used as coefficient duality.
No relative pairing for H is derived in this turn.

**Symmetry convention.** Read
[Stacks Section 15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN),
the commutativity constraint and its differential check: swapping degrees
p,q contributes (-1)^(pq). This and the rank-two determinant wedge map
are the inputs to the future sign check. Self-duality alone specifies
neither symmetric nor alternating structure. The separate attempt must
justify det(F)=O_X using the exponential exact sequence, H^1(X,O_X)=0
for the K3 product, and actual integral c_1(F)=0. It must retain both
coefficient and cohomological signs and write the trace and perfectness
argument. No sign for H or K is asserted as a proved notebook result.

**Connection compatibility.** Read Arvid Perego,
*Kobayashi--Hitchin corrispondence for twisted vector bundles*, Complex
Manifolds 8 (2021), 1--95, published open-access version,
[Propositions 3.9--3.12 and 3.15 with proof, pp. 36--38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36).
Duals negate the Einstein function; tensor products add it. On the
compact Hermitian manifold, holomorphic morphisms between the specified
weak Hermite--Einstein bundles with target function at most the source
function are parallel, with constant rank and connection-preserving
kernel/image decompositions. The proof invokes the Bochner theorem
(Kobayashi, *Differential Geometry of Complex Vector Bundles*, III,
Theorem 1.9) on Hom with its induced Chern connection.
Use the untwisted specialization, cocycle one and B-field zero, at the
same compact K3 metric. L056/L058 provide zero Einstein contraction
for the actual transform connection; the functions must be checked
as zero. This source neither constructs the pairing nor identifies
an arbitrary metric orthogonal complement with K. Those applicability
arguments remain. Rational polarization and irreducibility are unnecessary.
Kobayashi's publisher preview stops before Chapter III; the imported
morphism statement is the inspected Perego proposition.

**Real characteristic test.** Read Martin Cadek and Jiri Vanzura,
*On the classification of oriented vector bundles over 5-complexes*,
Czechoslovak Math. J. 43 (1993), 753--764,
[author-hosted manuscript](https://www.math.muni.cz/~cadek/papers/so5.pdf):
Section 2, p. 2, Theorem 1 and its existence proof, p. 5, Theorem 3 and
Corollary 3 proof, pp. 9--10. Section 2 states for oriented real bundles
rho_4 p_1 = P(w_2)+i_*w_4. Theorem 1(i) realizes exactly these triples
in real rank five on connected CW complexes of dimension at most five.
Injectivity additionally requires no order-four element in H^4(Z) and
Sq^2 H^3(Z/2)=H^5(Z/2); existence does not. Theorem 3 realizes arbitrary
c_1,c_2 in complex rank two on such a complex. Corollary 3 uses
p_1(E_real)=c_1(E)^2-2c_2(E).
This allows a separate topological comparison on the real four-dimensional
K3, adding trivial real directions when needed. It supplies no holomorphic,
stable, acyclic or instanton structure. Neither w_2 nor w_4 of the
bundle can be discarded merely because the base is spin; rank-three
Theorem 2 has different data. Numerical evaluation is deferred.

**Existence results with different hypotheses.** Read Roland Abuaf
and Ada Boralevi, *Orthogonal bundles and skew-Hamiltonian matrices*,
[arXiv:1312.0963v1, 3 December 2013](https://arxiv.org/pdf/1312.0963),
Theorem 3.4, pp. 3 and 10, and monad setup, pp. 3--4. It treats stable
orthogonal bundles on P^2 with trivial general-line splitting, even
charge n, and ranks n (n>=4) or n-1 (n>=8). Both surface and rank/charge
scope differ; no K3 theorem is imported from its monads.

Followed the K3-specific lead to Usha N. Bhosle, *Nets of quadrics and
vector bundles on a double plane*, Math. Z. 192 (1986), 29--43,
[DOI](https://doi.org/10.1007/BF01162017),
[author-uploaded primary text, introductory theorem, pp. 29--30](https://www.researchgate.net/publication/225313414_Nets_of_quadrics_and_vector_bundles_on_a_double_plane).
It requires a smooth branched double plane, a fixed ineffective theta
characteristic, even rank 2n, involution action with prescribed
ramification eigenbundle, an O_X(-1)-valued nondegenerate quadratic
form, fixed determinant/charge, and semistable generic-line pullbacks.
Its sextic specialization is K3. These differ from the untwisted
odd-rank residual and exact real-metric stability. OCR of formulae is
imperfect; only the unambiguous rank, form value and extra hypotheses
are used for this mismatch, not a numerical Chern specialization.

Reuse L058/L052's already assessed arbitrary-rank surface RR,
dual-stability and exact line-lattice inputs. The exterior-square/adjoint
constraint is a new application, not a repetition of the stopped
projection-character test. The future attempt must retain every stable
decomposition, paired non-self-dual blocks and symmetric/alternating
self-dual blocks, with arbitrary permitted individual c_1. A formal
stable rank-seven branch cannot establish orthogonal existence.

## Search and duplicate/failure comparison

Local searches targeted L044, L048, L052 and L056--L058, relevant
flat-image assessments, history/109--110 and ATTEMPTS/042; a term search
in local literature/history/failures found no duplicate orthogonal
residual proof. Read L058's full argument and L056's connection argument.
No sibling notebook was read. The earlier inverse-kernel hypotheses and
cohomology stop are preserved, not reopened.

External queries included `relative Serre duality symmetric alternating
pairing H1 symplectic bundle surface orthogonal`, `orthogonal bundles K3
surface rank 7 second Chern class stable existence`, `"K3" "orthogonal
bundles" stable`, `"K3" "SO(7)" instantons`, `"orthogonal bundles"
"surfaces"`, `"Serre duality" "symplectic vector bundle" surface symmetric`,
`"symplectic" "Nahm transform" "orthogonal" K3 Serre`,
`Cadek Vanzura classification oriented vector bundles dimension 4
Pontryagin rank 5`, and exact-title queries for Abuaf--Boralevi, Bhosle
and Perego. Primary Stacks statements were followed to their proofs.
Four-torus/orientifold Nahm and curve orthogonal-bundle results were
search leads only, not theorem inputs. No matching rank-seven acyclic
exact-metric existence/exclusion theorem was located. This is bounded
search evidence, not a novelty or nonexistence claim.

## Bounded continuation and abandonment test

The exact TARGET is ready for one separate necessary-constraint attempt,
subject to the supervisor's separate approval of this changed assessment.
First construct and classify the actual relative pairing, justify perfect
descent and connection compatibility, then evaluate real orthogonal and
adjoint RR constraints for all remaining summand cases. Cite the above
theorems rather than reprove duality, Bochner, characteristic classification
or existence on other surfaces. Only determinant, sign, residual descent
and explicit specialization need local proof because the sources do not
state this kernel/residual case.

Continue if a constraint contradicts the exact data or exposes a further
concrete discriminating condition. If all tested constraints are compatible,
stop this bounded orthogonal parity/index mechanism while leaving geometric
residual and global kernel existence unresolved. Positive expected dimension
and topological realization are not stable acyclic bundle existence.
No holomorphic construction, stronger holonomy exclusion or inversion
argument is approved. Such a changed target needs REVIEW_REQUIRED coverage.
The full target is not matched by inspected sources; the supporting results
are known. This literature-only step derives no pairing, result or numerical
constraint and changes no lemma or mathematical script.

Mathlib coverage of the full pairing and orthogonal residual target:
**not checked**; no matching theorem or absence claim. The main Hodge gap
and attained cycle span are unchanged.
