# Global triple-moment source comparison — completed

TARGET: Review source coverage for a global degree-three moment upper certificate using all L020 determinant exclusions, with pair moments unrestricted.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped checks of foundations/04,08–09, the global-pair/cross-core assessments, L020–L023 and ATTEMPTS/019,021,033,034; five external queries and inspected primary passages are recorded below. No inspected source supplies the requested labeled finite-instance bound.
SOURCE_EVIDENCE: Freshly read Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 with complete proof, p. 2, and Section 1.2 averaging, p. 3; Brouwer–Polak arXiv:1709.02195v1 Section 2 (1)–(3), pp. 2–3; Schrijver author manuscript Section III.B (60)–(65), p. 7. Canonical degree-three input: foundations/12-global-degree-three-moment-source.md; reuse foundations/09 for pair spectra and Schur congruence.
COMPARISON: Known conditioned union-moment programs support a global labeled relaxation, but their full symmetric-group reduction requires invariant constraints. L021, L030 and the fixed prescriptions excluded by L051–L052 do not decide its free-pair optimum; L022–L023 do not test the changed triple zeros or the proposed small conditioned matrices.
GAP: A useful uniform dual bound, full conditioned PSD feasibility and a tractable label-preserving reduction remain unproved; the first bounded test is the separately saved small-principal-matrix witness diagnostic, not a full SDP solve.
REASON: Essential framework coverage is complete without a new hierarchy theorem; only the specified finite specialization is ready for separate approval, with no threshold or novelty claim.
SCOPE: Global moments through three support indicators on all 68-subsets of H; free pair coordinates in the bound, pair-conflict zeros, and every L020 nonsingular incidence triple. Ready continuation scope is limited to drafts/literature/2026-10-11-global-triple-small-principal-test.md; no full labeled optimization or permutation averaging is approved.
LITERATURE_REASON: The gate requires exact degree-three conditioning and actual-label restrictions to be compared separately after the fixed-pair audit; prior assessments covered different prescriptions or degree-four local moments.

Main gap: arbitrary-center 68-agreement safety, with 67-agreement safety
independently unresolved. The proposed intermediate direction is a uniform
global moment certificate that uses an RS-specific necessary restriction,
allowing pair values to vary. Its potential downstream use is a support
upper bound below the first unsafe integer
T=floor(65537^28/2^128)+1, hence at most floor(tau). No such bound is
claimed; neither L052's negative dual nor its particular pair values are
valid constraints on arbitrary lists.

Essential continuation inputs: L001's support injection; C001a's exact
threshold and bracket; L020's full incidence hypotheses and determinant
criterion; L021's ordinary pair optimum; foundations/09's source record.
Use L022–L026 only for targeted comparison with their prescribed global
assignment, and L027–L030 and L051–L052 as recorded obstructions, not
assumptions about every list. Read their detailed proofs only as needed
after the overview and DAG. The prior cross-core assessment covers a
different, now excluded fixed prescription and cannot approve this target.

The next source review should retrieve the exact primary degree-three
moment inequalities and any reductions applicable when actual labels are
retained, check for known bounds or obstructions at these parameters,
and choose one bounded quantitative test if coverage permits. Continue
only with a specified finite certificate or discriminating obstruction
whose hypotheses are covered. Abandon a proposed reduction if it requires
unjustified full permutation symmetry, reimposes an already excluded
pair prescription, or only reproduces a stopped local cap. Source access
alone and a restatement of an equivalent upper-bound program do not meet
the quantitative target. No proof or script for this direction was written.

Mathlib: matching labeled triple-moment certificate and supporting
coverage not checked. No absence or novelty claim is inferred.

## Completed review (step 167)

The preceding proposal is preserved as the startup research direction.
This completion changes only its source coverage and selects a test;
no moment inequality, feasibility result or quantitative bound was derived.
The exact original TARGET is retained.

The primary known input is recorded in
[foundations/12](../../foundations/12-global-degree-three-moment-source.md).
Use moment order three, independently of RS dimension 64 and tuple width m.
The ordinary universe has (n,d,w)=(1024,10,68), satisfying n>=2w.
L001's support selection and L020's exact tuple criterion are the relevant
local inputs; arbitrary centers and extra agreements remain permitted.
Import the known union-indexed matrices. Their specialization with extra
triple nonfaces still needs the indicator applicability check during
research; this review does not reprove or assert that specialization.

An ordinary degree-two unconditioned PSD matrix has no triple entries.
The order-three source additionally conditions on each single support.
Retaining all entries of those matrices would be enormous here. Its
polynomial-size symmetric-group implementation solves the ordinary
constant-weight problem. It supplies no reduction of the labeled RS
problem, whose zeros distinguish the nonsingular and singular cases in
L020. A fully symmetric *trial witness* is allowed: membership is checked
directly, rather than deduced by averaging an arbitrary labeled assignment.

The source's nonnegative moment convention, singular PSD cases, Boolean
diagonals and repeated-support entries must be retained. Pair feasibility
uses the augmented constant coordinate, not only Johnson eigenvalues.
Neither an order-three feasible point nor a numerical dual is a
representing distribution, ordinary packing or common-center RS list.

## Duplicate and failure comparison

L020's whole criterion and both examples were read. Only triples with
the stated 61-core, three disjoint pair-only two-sets and nonsingular
sum/product matrix are forbidden. No universal incidence exclusion is
an input. L021's hypotheses, imported pair inequalities and exact witness
proof were read; C001a's exact threshold and bracket were read. The
support injection was checked in L001's root-bound/counting proof.

ATTEMPTS/019 and 021 stop local caps, including all higher local moments.
They do not supply globally compatible moments. ATTEMPTS/033 and 034
stop fixed unthinned/thinned pairs. Free pairs are not constrained to those
values. L022's complete assignment definition and L023's extension
hypotheses were read for a reusable above-threshold *trial*, rather than
assumed feasibility of a changed extension. The prior assessments show
that the scalar/full-zero/mixed-block diagnostics L023–L026 retain their
old formulas. Changing triple entries is outside their conclusions.

The proposed bounded test is consequently distinct: retain the global
pair PSD condition, and test every anchor-containing three-index principal submatrix of
every singly conditioned matrix after a specified incidence-zero change.
It is weaker than the full labeled order-three program. Its pairs remain
free as optimization variables; a fixed trial merely tests nonexclusion
of this batch. Nothing reopens the earlier local-cap or fixed-pair stops.

## External evidence and limits

Queries on 11 October 2026:

- `constant weight codes A3 semidefinite bound triples hypergraph forbidden triples moment matrix`
- `Reed Solomon support determinant triples semidefinite list decoding upper bound`
- `"constant weight" "forbidden triples" semidefinite`
- `"Reed-Solomon" "semidefinite" determinant list decoding`
- `"1024" "68" "constant weight" semidefinite bound`

These bounded searches mainly returned the ordinary constant-weight
framework, Shangguan–Tamo's determinant dictionary already used by L020,
or irrelevant decoding work. No search snippet is imported as a theorem;
failure to find a match establishes no novelty. The primary versions and
passages actually read are those in SOURCE_EVIDENCE and foundations/12.
Reuse the existing Shangguan–Tamo inspection through L020, rather than
claiming a fresh reading. There is no essential source access blocker.

Schrijver's (60) directly constructs PSD matrices by included/excluded
anchor averages; the source note in foundations/04 retains the suspect
(61) complement prefactor. That prefactor is neither repaired nor used.
No complementary PSD matrix is added to the first test. Laurent's
graph-only zero-propagation lemma in foundations/08 is not a theorem for
cubic hyperedges and is not used to infer the labeled triple zeros.
Gijswijt–Mittelmann–Schrijver arXiv:1005.4959 and specialized sparse
hypergraph reductions remain unread, nonessential leads. Full matching
Mathlib coverage remains not checked.

## Selected continuation and decision rule

The precise trial and complete certificate requirements are in the
[new continuation assessment](2026-10-11-global-triple-small-principal-test.md).
It receives separate approval next turn. This review licenses no
calculation in the current turn and reports no achieved bound.
An exact above-threshold feasible trial stops this small-matrix batch
as a sufficient upper certificate, leaving larger conditioned matrices
open. A failed trial identifies only its actual failed principal matrix
or pair condition, not infeasibility of the free-pair program. Resource
failure is unfinished work. Continue only from that discriminating
evidence; do not claim full-SDP feasibility or repeat a stopped local cap.
