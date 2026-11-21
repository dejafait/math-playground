# Boundary-cancelled dual residual — completed source comparison

TARGET: Assess whether the CCM rank-two commutator can bound a boundary-cancelled Fourier dual residual without the full inverse spectral-gap loss, using L759's cell at z=i/4 as the first bounded test.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step362 exact local reduced-resolvent/goal-oriented/Loewner/dual-residual search and primary-source searches below found standard sensitivity identities and displacement algorithms, but no inspected bound for this Fourier row. Parent determinant and finite-audit coverage reused; no novelty inference from search silence.
SOURCE_EVIDENCE: CCM 2511.22755v1 Lemmas5.1-5.2, normalization before Lemma5.4 and its proof(i), Corollary5.6, Proposition5.9 with complete proof, Theorem5.10 normalization passage; Greenbaum--Li--Overton SIAM Review62(2020)463-482 Assumption1, Lemma1/(5), Theorems2-3, section3.3 proof pp.473-475 and section3.4 cases1-2 pp.475-477; Connes--van Suijlekom 2511.23257v1 Lemmas5.1-5.3 with relevant proofs, AppendixA qualifications; Embree--Ionita author manuscript section4 pp.8-10/(12)-(13).
COMPARISON: Simple-eigenvector sensitivity and change of normalization are known, retaining the reduced resolvent and nonzero normalization denominator. CCM's commutator pays a specific odd-direction identity, not the proposed complete dual norm. The Loewner source accelerates an inverse calculation, not its norm estimate, and its invertible pencil hypotheses do not directly cover the singular shifted CCM matrix.
GAP: An explicit transform-specific factorization with quantitatively controlled preimage is still missing. No bound eliminating the reciprocal-gap loss, quantitative boundary overlap, trial residual estimate or family limit is imported.
REASON: Essential finite-dimensional source scope is now inspected. Permit a bounded search for an actual commutator-assisted estimate, rather than treating normalization or low displacement rank as such an estimate. This review derives no new mathematical result and approves no family conclusion.
SCOPE: Finite CCM cell and Euclidean coefficient norm; standard analytic simple-eigenpair sensitivity only locally in a fixed matrix dimension. No transfer from differentiable sensitivity to a finite trial error without a separate identity/error estimate. A newly nominated factorization attempt has its own exact-target assessment, requiring separate approval next turn.
LITERATURE_REASON: The startup assessment was REVIEW_REQUIRED and essential sensitivity/normalization/structured-inverse coverage was unread; this completes that gate, without refreshing the ready finite audit.

## Exact proposed object and bounded decision test

For the source's finite arithmetic matrix A, let epsilon be its simple
even least eigenvalue, P the orthogonal projection off its ground line,
and R the inverse of A-epsilon on that complement, zero on the ground
line. Let b(v) be boundary evaluation and normalize xi by b(xi)=1.
Nonzero b(xi) is the source's argument before Lemma5.4, not a quantitative
lower bound. Let ell_z be the source Fourier-transform functional.
The proposed object is the norm of the row functional

    [ell_z - ell_z(xi) b] R P.

No bound is asserted. A future mechanism must exploit the rank-two
commutator rather than assume favorable norm control. The standard
estimate with ||R||, the reciprocal gap, is the comparison to beat;
it may be unavoidable. Source review must identify exact applicable
residual/sensitivity identities and known negative examples, and decide
whether the commutator adds any usable constraint.

First proposed mathematical discrimination, only after separate approval: at
lambda=sqrt(13), N=120 and z=i/4, compare a rigorous enclosure of this
dual norm against ||ell_z-ell_z(xi)b||/gap, retaining boundary-normalization
and eigenvector uncertainties. A material gain must have an identifiable
algebraic reason before pursuing any family estimate. Negligible gain,
an equivalent hidden ground-vector assumption or a structural counterexample
abandons this mechanism. A favorable finite value alone proves no limit.
The comparison below found neither a matching bound nor a rigorous obstruction
for this exact row. It does not infer that the bound exists or is original.

Essential input: audited L759. External inputs to assess precisely:
CCM Lemma5.2 and the normalization argument before Lemma5.4; standard
reduced-resolvent/eigenvector error estimates with boundary evaluation.
General parity, N/lambda limits, quantitative boundary overlap, actual
trial-vector residuals and locally uniform Xi transfer remain unresolved.
No cross-notebook input. Mathlib coverage unchecked.

## Primary inputs and exact applicability

1. Connes--Consani--Moscovici, *Zeta Spectral Triples*,
   [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1), 27 November 2025.
   In Lemma5.2, D=diag(j), eta=sum V_j, beta=sum b_j V_j;
   [D,A]=beta eta* - eta beta*. For T=A-epsilon I>=0 with one-dimensional
   even kernel, the normalization argument has two cases: D x=0 (the
   V_0 line), or D x is a nonzero odd vector outside the kernel.
   It proves nonzero eta-overlap, not a lower bound. Lemma5.4(i) gives
   T D x=-beta for eta*x=1. Theorem5.10 explicitly distinguishes
   x=xi/sqrt(L), where b(xi)=1 and b=eta*/sqrt(L). Do not substitute
   boundary-normalized xi into the eta-normalized identity unchanged.
   Proposition5.9/(5.25), for arbitrary finite coefficient vectors, is

       ell_z(v)=2 L^(-1/2) sin(zL/2) sum v_j/(z-2 pi j/L).

   Its proof integrates each basis vector, then cancels lattice poles;
   z=i/4 is off that lattice. This supplies the exact Fourier row.
   Shifting A changes neither its commutator nor eigenvectors; L759
   supplies the required finite simple-even hypothesis. No sign of
   unshifted A or uniform estimate is thereby obtained.

2. Greenbaum--Li--Overton, *First-Order Perturbation Theory for Eigenvalues
   and Eigenvectors*, SIAM Review 62(2) (2020), 463-482,
   [author's published copy](https://cs.nyu.edu/~overton/papers/pdffiles/EigVecPert.pdf).
   Assumption1 requires a simple eigenvalue and a locally analytic matrix
   family, with left/right vectors y*x=1. Theorem2/(7)-(8), p.467,
   gives x'=-S A' x and (y*)'=-y* A' S in its specified gauge;
   (5) identifies S and its inverse/projector identities. For the real
   symmetric finite matrix, the orthogonal complement gives the R in
   the proposed target. The stated diagonalizable bound, p.468,
   retains separation from the other eigenvalues. Section3.3's proof
   uses a separating contour, its spectral projection and a local
   analytic normalization; it is not uniform at a collision.
   Section3.4/(26)-(30), pp.476-477, treats normalization changes,
   including fixed nonzero coordinate evaluation. Boundary evaluation
   is a fixed linear functional: an orthonormal coordinate change puts
   it in that case, retaining its norm and its nonzero denominator.
   This applicability observation supplies no quantitative denominator
   or nonlinear finite-residual theorem. No reproof is needed.
   The arXiv v2 numbering differs in section3.4; use published numbers.

3. Connes--van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the
   Spectral Action*, [arXiv:2511.23257v1](https://arxiv.org/html/2511.23257v1),
   28 November 2025; Commun. Math. Phys.406:312 (2025).
   Lemmas5.1-5.3 contain the same commutator, normalized odd-direction
   identity, and rank-one determinant factorization. Their hypotheses
   retain Q>=0, an even nullvector and eta-overlap normalization.
   These are overlap with CCM, not a second quantitative eigenvector
   estimate. AppendixA gives a model and limiting double extrema
   (FactA.4/PropositionA.5). Crucially, finite-truncation simplicity
   is described there as a numerical observation, not a proved uniform
   theorem. Thus this passage warns against finite-to-limit inference;
   it is not imported as a rigorous counterexample to the proposed norm
   bound. No such counterexample was found in the passages inspected.

4. Embree--Ionita, *Pseudospectra of Loewner Matrix Pencils*,
   [author's pre-copyedited manuscript](https://personal.math.vt.edu/embree/embree_ionita.pdf),
   18-page version retrieved 4 November 2026. Section4, pp.8-10,
   (12)-(13) uses invertible Loewner L, a regular evaluation point and
   a small Woodbury inverse to accelerate inverse iteration. Those
   inverses remain in the formula. Its left/right interpolation sets
   are disjoint (section2, p.3); CCM has coincident row/column nodes,
   freely specified diagonal entries, and singular T. No direct theorem
   specialization is asserted. This known computational structure
   supplies no claimed gap-independent bound for q_z R P. The faster
   algorithm alone is not the proposed new mechanism.

## Bounded search, duplicates and failures

Queries actually issued included `eigenvector observable residual reduced
resolvent goal oriented eigenvalue error commutator rank two`,
`eigenvector perturbation reduced resolvent first order derivative simple
eigenvalue Greenbaum Li Overton 2020`, `"goal oriented" "eigenvector"
residual error estimator`, `"rank two" "commutator" "Zeta Spectral Triples"
resolvent`, `"boundary" "eigenvector" "reduced resolvent" normalization`,
`"Loewner matrices" "inverse" "displacement" eigenvector`, and exact
CCM/reference-title searches. Search snippets supplied leads only.
Goal-oriented PDE/eigenvalue estimators and Meyer--Stewart (1988), cited
by Greenbaum et al., remain unread leads; none is essential to the
limited finite row-factorization test, and none is claimed as coverage
of a finite trial-function error. General PDE discretization estimators
would not by themselves supply this matrix's missing norm estimate.

Local exact-identifier searches in spectral-triples/parity assessments,
step357/359-361 histories and ATTEMPTS found the parent construction and
audits, not a matching completed dual-row estimate. Exact terminology
searches across local literature/ATTEMPTS/history found only unrelated
Feshbach reduced-resolvent, Pick/Loewner-kernel and Suzuki order notes;
their matching ranges were inspected. They concern different operators
and do not approve this target. L759's unsuccessful floating screen and
first interval pass remain recorded in its section5; they obstruct neither
this analytic mechanism nor its rigorous finite diagnostic.

No persistent primary-source blocker: essential passages were read through
the web tool. Shell source retrieval failed at DNS for all three arXiv
URLs; no downloaded source file resulted. Failed direct NYU PDF access
was resolved by following the author's publication-page link to the
published copy. Screenshots yielded references without inspectable image
content in this interface; no claim relies on them. The theorem/formula
and proof passages used above were inspected as complete relevant text.

## Decision and continuation qualifications

This is EXPLORATION: new source comparison resolves scope, not the norm
bound. A citation suffices for standard sensitivity, normalization and
the existing commutator identities; it does not suffice for cancellation.
No new proof, lemma, numerical test or mathematical script was made.
Keep PROOF.md and DAG.md unchanged.

The separately nominated attempt in
`drafts/literature/2026-11-04-commutator-dual-factorization-test.md`
seeks an explicit controlled preimage of the dual row under T, using
the frequency resolvent and commutator rather than merely writing q_z R.
Its possible gain is an independently testable hypothesis, not an
assessed theorem. A ratio gain without an algebraic explanation does
not justify a family program. General parity, boundary overlap, actual
trial residuals, both limits and Xi transfer remain open. Mathlib's full
matching and supporting coverage was not checked; unknown is not absent.
