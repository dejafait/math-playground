# Copy ancestry and sparse simulation — source comparison

TARGET: Assess a sparse simulation chain over F₂ for endpoint-restricted versus whole-copy L035 graphs, preserving the three job-7 local modes with an explicit uniform support bound.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 519 searched weighted-automaton simulations, proper semirings, conjugacy, functional decomposition, trimming and sparse certificates; compared the exact statements below with L035/L036/L038, L097 §22, L110 §§1,3–5,21 and Attempts 044–046. No inspected theorem supplies the uniform C*S bound; no novelty is inferred.
SOURCE_EVIDENCE: Ésik–Maletti Simulation vs. Equivalence §3 Definition 3.1 and §4 Theorem 4.2/full proof/Corollaries 4.4–4.5, manuscript pp.2–3; arXiv:1005.2079v1 §§2–3, Lemmas 8–10/Theorem 11 pp.7–10; Sakarovitch Handbook draft 19-Sep-2008 Definition 11/Proposition 12/Definitions 12–13 pp.26–27 and Theorem 24/proof pp.58–59. Reuse the assessed Kiefer/Mohri/Raz–Shpilka passages below.
COMPARISON: Known results supply scalar-matrix simulation equations and qualitative common simulators over F₂. Functional factorization depends on the starting transfer matrix and extra states, not the proposed endpoint graph measure. The identified difference is an explicit ancestry-based sparse chain and uniform support accounting, not a reproof of soundness or pruning semantics.
GAP: No chain, uniform C, intermediate-size estimate or reception bound is proved. Separate construction must handle both deletion directions, endpoints, finite right closure, all three local modes and disjoint gadget interiors; occurrence checks and the fourth commutator comparison remain independent.
REASON: The comparison rejects generic qualitative existence or functional decomposition as a sufficient support-size argument, while providing coverage for one bounded structural specialization. The newly prepared construction continuation requires separate approval before execution.
LITERATURE_REASON: This proposed sparse simulation chain differs from the approved dense B,c,T contract and static implementation audit; essential transfer/sparsity theorem coverage is missing.

The proposal below was saved after step 518. Step 519 completed only its
literature comparison; the completed decision and scope follow the preserved
proposal. No mathematical construction was executed.

Main gap: uniform worst-case P versus NP. The nearer branch gap is a compact,
independently checkable certificate for the fixed construction's formal
identities. A sparse relation between the restricted W copies and the
independent whole-copy R reference might avoid searching dense invariant
rows. It could address W=R in free, zero-placeholder and axiom-substituted
modes; the separate R(x,A)=fg+gf comparison is explicitly outside this first
target and remains unresolved as a finite received equality.

Essential local inputs are L035 (2)/(4), L036 (5)–(9), L038's affine/local
transports, L097 §22's path-restriction proof and L110 §§2–5,20–24. Reuse the
ready assessments dated 2026-10-25 for selected-copy path restriction and
linear-algebra identity reception. Fixed-instance identifiers remain source
record 78, events 2642–2643 and output-493 jobs[7], with the exact eight
binding inputs in output-502/manifest.json if their data become necessary.
The first review should read the relevant proofs, not regenerate those files.
No cross-notebook input or historical-ledger reconstruction is needed.

Proposed bounded mathematical discriminator, only after separate approval:
consider a chain through explicit intermediate copies, permitting forward
and backward linear simulations so that deletion of unreachable vertices
and deletion of vertices unable to reach the designated exit are not silently
treated as the same map. Seek a uniform bound C*S on the total nonzero
entries in the chain's matrices, with explicit C independent of operand
size and S the total vertices, edges and affine-label occurrences of the
explicit source/target local-mode graphs. Account separately for intermediate
graph size, indices, initial/final vectors and verification work. A sparse
matrix alone is not a small wire or work certificate. Retain all ordered
edge occurrences, central branches and factor order; the original immutable
structural graph is never replaced by a parity quotient.

The review must determine the exact standard matrix equations/directions
and which hypotheses allow the proposed chain. Essential cases are dead
vertices on either side of a designated subpath, constants/right epsilon
closure, empty paths, coincident or nonextremal roots, parallel cancellation
over F₂, and fresh substitution-gadget interiors. Do not assume a path
bijection alone implies a sparse global intertwiner. Inspect primary theorem
statements and these proof cases before larger source passages; import any
matching result rather than reproduce it. Real-weight bisimulation sources
are unusable for F₂ without an explicit applicability argument.

Continue to a separately approved symbolic construction only if coverage
supports a concrete chain and a discriminating support-size test. A smallest
explicit copied/pruned graph violating the proposed equations, or a required
dense intermediate relation, would reject that precise mechanism. It would
not reject polynomial equality or other certificates. If known results
already settle the target, import them with the necessary specialization;
do not label that creative. No support bound, construction or counterexample
is derived here. No row search, receiver implementation, cap increase,
format mutation or production integration is authorized.

Attempts 042–045 and L110 §24 remain intact. Even a successful symbolic
chain would not pass their contracts, repair step 502's missing historical
work, establish the fourth comparison, fit a complete certificate below
200,000,000 bytes, or resolve later jobs, Boolean/K/H/nonzero-fJ, availability,
L087 W₂ or unrestricted complexity. Those require separate arguments and
assessments. Full matching Mathlib coverage is not checked.

## Completed comparison — step 519, 2026-10-26

The main gap remains uniform worst-case P versus NP. The intermediate target
is a sparse equality certificate for the copied/pruned L035 graphs. It could
replace large word tables or dense coordinates for W=R, without establishing
that arbitrary certificates exist.

### Inspected primary results

Zoltán Ésik and Andreas Maletti, [*Simulation vs. Equivalence*, author-hosted
four-page manuscript](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf),
2010 bibliographic version, revision date unestablished: read Definition 3.1
and soundness (p.2), Theorem 4.2's entire proof, Corollaries 4.4–4.5 and the
finite-semiring deterministic construction (p.3). For A=(α,M,β), B=(γ,N,δ),
a simulation A→B is an m×n scalar matrix X satisfying

    αX=γ,       M_a X=X N_a for each a,       β=Xδ.

The theorem gives a common simulator C→A, C→B for equivalent automata over
a Noetherian semiring. F₂ is directly covered as a finite semiring by
Corollary 4.5, without positivity or characteristic-zero assumptions.
The proof uses generators of paired reachable rows and coordinate matrices;
the deterministic variant enumerates reachable pairs. Neither asserts the
required linear support or intermediate-size bound in S. Import the equations
and soundness, not a small-certificate conclusion or a new existence proof.

Ésik and Maletti, [*Simulations of Weighted Tree Automata*,
arXiv:1005.2079v1, 12 May 2010](https://arxiv.org/pdf/1005.2079v1): inspected
§2 conventions, §3 simulation definitions, Lemma 8 including zero-sum padding
(pp.7–8), Lemma 9's row/column construction and Theorem 11's entire proof
(pp.8–10), including both final trim cases. Hypotheses are equisubtractivity
and additive generation by units. It factors an already supplied transfer
matrix through new indices and fiberwise transition constraints. This tree
theorem gives no bound in our endpoint measure; it is not used for a sparse
chain, empty fibers, epsilon closure or serial gadget replacement. No
tree/string encoding is assumed. Its positive/zero-sum-free branch is not
an F₂ argument. PDF numbering is used; regenerated HTML calls Theorem 11
Theorem 3.2. This source is comparison evidence, not an additional premise.

Jacques Sakarovitch, [*Rational and recognisable power series*, Handbook
chapter draft dated 19-Sep-2008](https://perso.telecom-paristech.fr/jsaka/ENSG/MPRI/Files/References/JS-HWA.pdf):
read §3.3.1 Definition 11, Proposition 12 and Definitions 12–13, printed
pp.26–27, and §5.3.3 Theorem 24 with its paired-representation proof,
pp.58–59. These distinguish oriented conjugacy, quotient and co-quotient,
and give common simulators over any (skew) field. The proof builds transfer
rows by joint reduction, without the requested C*S estimate. This corroborates
the qualitative comparison; reversing an arrow cannot simply reuse its matrix.

Reuse the October 25 assessments' unchanged primary coverage: Kiefer,
arXiv:2009.01217v1 §§1–3, Propositions 1.1/2.1/2.2/3.1 and Theorem 2.3,
pp.1–5; Mohri IJFCS 13(1):129–143 (2002), author manuscript Definitions
4–5/Theorem 1 and both remaining-path cases pp.4–6, acyclic case pp.10–11,
and Handbook §6.1/(28)–(31). See L110 §1 for direct primary links.
They give ordered word coefficients and finite constant-path semantics,
not sparse preservation under proposed maps. Reuse Raz–Shpilka Lemma 2
Steps 1,3,5, pp.5–6, only for serial/parallel and pruning precedents.
L097 §22 already proves arbitrary-root path preservation; another such
lemma would duplicate it. Full matching Mathlib coverage is **not checked**.

### Discovery, duplicates and failure comparison

Queries included `weighted automata simulations arbitrary field forward
backward simulation trim automata sparse matrices`; `weighted automata
simulation functional dual functional trim semiring partial identity matrix
epsilon elimination`; `weighted automata simulations proper Esik Maletti`;
`weighted automata conjugacy trim accessible coaccessible restriction
simulation matrix sparse`; and the exact-term combinations `weighted
automata simulation trimming matrix`, `weighted automata sparse simulation
certificate`, `automata simulation coaccessible matrix weighted`.
They located qualitative properness/conjugacy and ordered-semiring inequality
work, not an inspected full statement for C*S. No exhaustive absence or
novelty is claimed.

The CSR06 author PDF timed out at igm.univ-mlv.fr; its www-igm variant was
inaccessible and HAL hal-00619855 returned an access-denied challenge.
That proof remains unread. Accessible primary sources supply the necessary
scalar equations and qualitative comparison, so this is not an essential
source blocker. Boreale/Balle and quantitative partial execution remain
unread leads; no real-weight or ordered-semiring theorem is imported into F₂.

Read the relevant full local proof passages: L035 (2)/(4) and its four-copy
construction; L036 (5)–(9); L038's endpoint/splitting/gadget/right-closure
interface; L097 §22; L110 §§1,3–5 and §21's hypotheses/imports/copy primitives.
L097 proves path equality, L110 receives arbitrary dense invariant rows, and
its static correspondence remains conditional. None supplies this sparse
chain. Attempts 044–045 stop specific word/evidence interfaces; Attempt 046
parks historical administrative completion. Their preserved evidence does
not prohibit a symbolic certificate test. No archived finite data or sibling
notebook was needed. [Clay's primary page](https://www.claymath.org/millennium/p-vs-np/)
still marks the same problem unsolved. Its currently linked Stephen Cook,
[*The P Versus NP Problem*, §1, printed pp.1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf),
is the twelve-page description at that URL; no revision date is established.
Those pages were read and match the uniform worst-case machine/checking
definitions in foundations/01-model-and-target.md. No target change is made.

### Bounded specialization and stop test

Coverage suffices for a **separate** symbolic attempt, not an assertion that
it succeeds. Construct oriented maps satisfying the imported equations;
distinguish entry-unreachable vertices from vertices unable to reach an exit.
Check initial/final vectors and all transition equations. Prove any passage
through L110's finite **right** closure: epsilon-removal semantics alone is
not an intertwiner proof. Keep edge occurrences, parallel parity, roots,
factor order and fresh gadget interiors in free/zero/axiom modes.
Dead/no-path, coincident/nonextremal roots, constant-only, empty-word and
empty-central cases are mandatory. No trim or nonzero promise removes them.

Seek an explicit uniform C times the total vertices, edges and affine-label
occurrences of the six explicit W/R mode graphs before constant closure.
Count support across the whole chain, and separately bound intermediate
graphs, indices, boundary vectors and verification work. Sparse factors must
not be silently multiplied into a presumed sparse endpoint matrix. Continue
only after complete equations and a size bound survive these cases; abandon
the proposed maps on a completely specified failing equation or a
support/intermediate-size obstruction. No such construction or obstruction
was derived in this literature turn.

This is a structural specialization of known simulation/pruning algebra.
A genuinely creative next mechanism has not been justified; first test its
missing quantitative certificate claim. The exact construction continuation
is in `drafts/literature/2026-10-26-copy-ancestry-sparse-construction.md`;
it is newly written and awaits separate approval. Independent R construction,
occurrence checks, Dcomm, fitting wire/work/live bounds, a strict receiver,
later jobs, Boolean/K/H/nonzero-fJ, certificate availability, L087 W₂ and
unrestricted ER/Frege/SAT remain open. No lemmas, DAG, PROOF.md, mathematical
scripts, production format or historical evidence were changed.
