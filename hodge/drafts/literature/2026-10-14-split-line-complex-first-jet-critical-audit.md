# Split-line complex first jet — critical audit coverage

TARGET: Critically audit L101's determinant-fixed complex family and prescribed two-parameter first jet.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the realization/integration discovery and duplicate checks; read all of L101, the relevant audited L094 ranges, ATTEMPTS/061 and /046, history/261 and /268; inspected the proof-specific primary passages below. A targeted original-Artin search found a scan but supplied no readable theorem text.
SOURCE_EVIDENCE: BMM 1907.10690v2 Section 2 pp. 4--6, Definitions 2.1/2.2, minimal-model discussion/(2.3)--(2.4), Theorems 2.3/5.1 and p. 15 proof, https://arxiv.org/pdf/1907.10690v2; Buchdahl--Schumacher (2022) Lemma 2.5, Proposition 2.6/(2.4), pp. 83--84, https://d-nb.info/1262812674/34; Artin (1968) (1.2) via Rond (2018) Theorem 2.1, p. 122, https://www.journalofsingularities.com/volume17/rond.pdf.
COMPARISON: The inspected tools cover the formal-model, complex-slice and multivariable approximation methods needed to audit this existing proof; they do not directly certify its determinant restriction, obstruction comparison or exact prescribed jet. No stronger quaternionic conclusion is imported.
GAP: The mathematical audit must still verify each specialization and the compatibility of its actual maps, including cohomology normalization, complete equations, total holomorphic family and determinant trivialization; no audit verdict is made here.
REASON: This separately completed source comparison makes the unchanged critical-audit target ready without deriving or approving a repair in a literature-only turn.
LITERATURE_REASON: The saved audit target was REVIEW_REQUIRED; proof-specific minimal-model normalization and formal-to-analytic coverage had not received separate comparison after L101 was written.
SCOPE: One critical proof audit of L101 under audited L094's actual S,I,g,h,k,E,W, retaining its precise C^2 identification and first jet; no new integration, stability, common-kernel or separation target is covered.

## Relevance and reuse

The main gap remains algebraic realization of arbitrary primitive rational
Hodge classes. The intermediate target is verification of L101's actual
determinant-fixed complex family with its prescribed two-parameter first
jet. A verified complex prerequisite could inform later integration work;
it supplies neither a fixed-metric quaternionic germ nor a common kernel.

Reuse the [realization assessment](2026-10-14-split-line-complex-first-jet-realization.md)
and [integration comparison](2026-10-14-equality-split-line-analytic-integration.md)
for unchanged discovery, theorem versions and proof-case coverage. The
new work here compares their scope to the completed proof and records
the specific audit obligations. No novelty search is restarted.

## Primary passages inspected and their limits

Bandiera--Manetti--Meazzini, *Formality conjecture for minimal surfaces of
Kodaira dimension 0*, Compositio Math. 157 (2021), 215--235,
[1907.10690v2, 2 August 2020](https://arxiv.org/pdf/1907.10690v2),
Section 2, pp. 4--6: formality need not provide a direct strict DG-Lie
map. The minimal-model discussion gives a minimal model mapping to the
DG-Lie algebra and uniqueness up to L-infinity isomorphism; Definition
2.2 states the morphism identities. These are the appropriate source
passages for checking L101's cohomology normalization, rather than
assuming that an unspecified equivalence fixes tangents. Theorem 2.3's
sufficient case requires an injective inclusion with a module splitting.
Theorem 5.1, p. 15, requires a complex projective surface with trivial
canonical bundle and linearly reductive sheaf automorphisms. Its complete
proof uses an equivariant resolution, the cyclic pairing, an equivariant
splitting and rational finitely supported representations. The local
trace-free projection and its compatibility remain audit obligations.

Buchdahl--Schumacher, *Polystable bundles and representations of their
automorphisms*, Complex Manifolds 9 (2022), 78--113, DOI
10.1515/coma-2021-0131,
[Lemma 2.5, Proposition 2.6 and (2.4), pp. 83--84](https://d-nb.info/1262812674/34),
were read with the implicit-function construction and residual estimate.
The correction requires a small closed input, p>2 dim_C S, and the
orthogonal complement of the adjoint kernel. The estimate identifies
the complete holomorphic obstruction zero locus with integrability;
it does not merely identify its quadratic term. Lemma 2.5 records the
complex gauge equation. Section 1, p. 80, explains the passage from an
integrable semi-connection to a holomorphic bundle. The audit must
still check the restriction to trace-free coefficients and the total
family on S times U, including parameter regularity. No quotient
lifting or unitary ASD normal form is supplied by these passages.

Artin, *On the solutions of analytic equations*, Invent. Math. 5 (1968),
277--291, (1.2), remains the original citation. Directly inspected
[Rond, *Artin approximation*, J. Singularities 17 (2018), Theorem 2.1,
p. 122](https://www.journalofsingularities.com/volume17/rond.pdf),
with the preceding multivariable convention; reuse the inspected proof
reductions on pp. 123--126. The theorem requires convergent equations
over a characteristic-zero valued field and a formal solution vanishing
at zero. Approximation modulo the parameter ideal squared retains a
first jet. It requires a solution of the complete equations, not only
of their quadratic truncation, and does not assert convergence of a
chosen formal series or preserve extra differential constraints.

The query `"On the solutions of analytic equations" Artin 1968 pdf 277`
located [an original scan](https://mathweb.ucsd.edu/~toal/artin.pdf).
The web extraction returned no text, screenshot calls supplied no
inspectable image, and a local download failed on DNS. This scan is an
unread lead, not inspected original-proof evidence. The readable Rond
statement and previously assessed proof reductions cover the needed
approximation theorem; original-scan access is not an essential blocker
for this audit. No conclusion relies on search snippets.

## Bounded audit obligations and test

The following checks identify work for the separate mathematical audit;
they do not establish the listed bridges in this literature turn.

1. Retain actual E=L plus L^{-1}, k^2=-14 and k.h=0. Compare the
   automorphism group used in BMM with the determinant-one group, and
   verify a DG-module splitting, not merely a cohomology splitting.
2. Compare audited L094's complete Q|_W=0, both omega_J/omega_K
   pairings and its real/Dolbeault identification with L101's full
   trace-free Yoneda equation and exact complex basis b_1,b_2.
3. Check the direction of the minimal-model comparison, its induced
   graded Lie automorphism and normalization, and its compatible
   Maurer--Cartan series on all two-variable nilpotent quotients.
4. Check determinant-one formal gauge degree by degree, the degree-zero
   Green inverse modulo its kernel, coefficientwise Hodge decomposition
   and formal uniqueness for the very analytic slice used in (6)--(7).
   In particular, retain the surface-specific adjoint-kernel condition.
5. Check the complete finite convergent equations before approximation,
   its order-two jet precision, smooth/holomorphic parameter regularity
   of the total bundle, the actual determinant operator and the central
   identification. Check the precise first derivative as a representative
   as well as its cohomology class.

Continue if this audit preserves L101's actual complex family and exact
jet. If a bridge fails, identify that bridge and the smallest justified
limitation or repair; an uncovered repair requires separate review.
Do not infer a stronger integration or stability assertion from success.

Essential local input is L101 with audited L094 and the retained marked
data from L071. L081/L082 are comparison recipes only. L095/L096 remain
conditional context: no F, nonempty reducible locus, W=r(TB), punctured
stability, unitary/quaternionic realization or transport is assumed.
ATTEMPTS/061 retains the necessary second-order stop; ATTEMPTS/046 and
history/261 retain the distinct separation stops. L101 and history/268
record the new complex realization, not a prior independent audit.
None of these records duplicates this audit or globally bans integration.

Common F, global mixed action, original-image separation, reconstruction,
transport and universal primitive Hodge realization remain unresolved.
Matching Mathlib coverage is not checked. No lemma, mathematical script,
DAG edge or argument overview changes in this literature-only step.
SPECIALIZE approves the audit method and scope, not L101's correctness.
