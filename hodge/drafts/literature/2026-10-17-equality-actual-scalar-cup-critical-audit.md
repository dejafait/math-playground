# Actual scalar cup factorization — critical-audit source assessment

TARGET: Critically audit L117's actual scalar cup-map factorization and the uncontrolled global Ext^2 entry.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected coefficient-Lefschetz assessment; targeted Stacks searches for derived scalar cup/projection formula, finite-support cohomology, perfect derived Hom and homological Hom located the precise inputs below; local L117/L116, ATTEMPTS/047/068/069 and the actual-map working note show that this is an audit of a completed reduction, not an unevaluated new exclusion target.
SOURCE_EVIDENCE: Reused Verbitsky alg-geom/9307008v1 Theorems 4.2/4.2.A and their inspected proof scope via the coefficient assessment; inspected live Stacks 20.44 (0B6A), 20.50.5--6 (0FP7), 30.9.10 (0B3J), 13.4.2 (0149), 20.31 setup and 20.31.1 with sign footnote (0FKU/0FP2), and 20.54.2.1/20.54.3 with proof (01E6/0B54); reused 08J5/01EY and prior global-Leray audit coverage.
COMPARISON: Standard results cover the derived Hom, finite-support vanishing, triangle exactness and scalar-action framework needed to audit L117; they neither compute its actual global fibre-cup entry nor supply a stronger exclusion. The exact actual-arrow comparison remains a separate proof audit.
GAP: Check L117's shifts, factorization and uniqueness through the actual split j[2], base scalar naturality, endpoint identifications and full-trivial-summand argument; no evaluation of Phi_1 or mathematical audit verdict is made in this review.
REASON: Essential source scope is now ready for one separate RESEARCH proof audit classified REPRODUCTION; cite the general results and check only this actual-family specialization, retaining the uncontrolled-entry stop unless a substantive error or independently controlled actual term changes it.
LITERATURE_REASON: The new audit target was REVIEW_REQUIRED; the coefficient theorem was ready, but its exact global Ext and scalar-naturality source scope had not been separately compared.
SCOPE: Same hypothetical equality F, original common metrics, full negative tensor, finite possibly empty Z, locally free M, finite-support W and actual j/retraction of L116; no multiplicative splitting, independent rotations, acyclicity or assigned section count.

## Relevance and bounded test

The main gap remains algebraic realization of arbitrary primitive rational
Hodge classes, already on arbitrary fourfolds. This intermediate target
checks the integrity of one necessary-condition reduction for the
hypothetical equality kernel. A repair could change which constraints on
that kernel remain usable downstream; a successful audit only validates
this conditional reduction. Kernel existence, other representatives,
transverse transport and universal realization remain independent gaps.

Essential local inputs are L117 and L116's actual inclusion j and trace
retraction, retaining L108/L109/L111/L115 and ancestors including L071.
The proposed audit must use those arrows and the unknown actual t and
Phi_1. Continue to a repair only for a demonstrated omitted derived term,
wrong shift/sign, unjustified endpoint identification or section argument,
or independent actual-class information already in those retained inputs.
Otherwise preserve ATTEMPTS/069's stop, without another dimension test.
This review supplies no new mathematical assertion about those arrows.

## Primary coverage and applicability

The ready assessment
[coefficient Lefschetz](2026-10-17-equality-coefficient-lefschetz-constraints.md)
is reused unchanged in mathematical scope. Its controlling source is
M. Verbitsky, *Hyperholomorphic bundles*,
[alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993, Theorems 4.2/4.2.A, PDF pp. 16--17. Retain its product,
trace-free, real-structure and (0,*) qualifications. Only the stated
symplectic Lefschetz isomorphism is imported: neither the printed
middle-degree one-step injection endpoint nor scalar-ring equality nor
independent factorwise harmonic Lefschetz actions. No rereading of that
unchanged inspected source is needed for this audit.

The following live primary statements were inspected on 2026-10-17;
section/theorem numbers refer to that live text, with stable links.

- [Stacks 20.44, 0B6A](https://stacks.math.columbia.edu/tag/0B6A)
  defines global derived Hom by derived global sections of internal
  derived Hom and identifies its cohomology with derived Ext.
  [20.50.5--6, 0FP7](https://stacks.math.columbia.edu/tag/0FP7)
  gives functorial perfect-dual/tensor/internal-Hom identifications and
  the symmetric monoidal derived category. Its proof reduces the
  internal-Hom comparison locally to finite projective terms and then
  finite free terms. Here M is finite locally free, a stronger hypothesis
  than perfectness. These inputs cover the proposed passage to global
  Ext; they do not justify replacing global Ext by its sheaf Ext stalks.
- [30.9.10, 0B3J](https://stacks.math.columbia.edu/tag/0B3J)
  applies to coherent sheaves of zero-dimensional support on a locally
  Noetherian scheme and gives higher-cohomology vanishing. Its proof
  passes to the scheme-theoretic support and affine components. B is
  smooth projective and W has finite support; tensoring W by the vector
  bundle M dual preserves coherence and this support condition. Empty
  support is allowed. No corresponding vanishing for End(M) is supplied.
- [13.4.2, 0149](https://stacks.math.columbia.edu/tag/0149)
  gives exactness of Hom from a fixed object on distinguished triangles;
  the proof constructs a factorization using the triangle axioms. This
  covers existence tests in the shifted truncation triangle. Uniqueness
  still requires checking L116's actual left inverse, not just exactness.
  Reuse the canonical truncation framework in
  [08J5](https://stacks.math.columbia.edu/tag/08J5) and derived-global-
  section/Leray comparison in [01EY](https://stacks.math.columbia.edu/tag/01EY),
  with the prior [global-Leray audit assessment](2026-10-17-equality-global-leray-critical-audit.md).
- [20.31, 0FKU](https://stacks.math.columbia.edu/tag/0FKU) and
  [20.31.1, 0FP2](https://stacks.math.columbia.edu/tag/0FP2)
  describe cup via tensoring the morphisms representing cohomology
  classes. The proof compares this with the counit construction of
  relative cup; its footnote explicitly retains tensor/shift signs.
  [20.54.2.1 and 20.54.3, 01E6](https://stacks.math.columbia.edu/tag/01E6)
  construct the natural projection map by adjunction and prove it an
  isomorphism for perfect base K. The proof reduces to shifted finite
  free modules. The base unit and its shifts are perfect; p is a
  morphism of ringed spaces. These are the framework for auditing the
  base scalar class as a morphism O_B -> O_B[2], its tensor action and
  compatibility with pushforward. Checking that L117 uses precisely
  this action with its fixed normalization remains mathematical work.

The endpoint and J arguments use L116's already audited cohomology and
full trivial summand, with ordinary K3 Serre duality; they require no new
existence theorem. The audit must check their application to the same j,
not choose independent identifications of the two endpoints. The
previous global-Leray audit assessment covers that standard duality.
No source imported here evaluates the actual fibre class or authorizes
a multiplicative Leray splitting. Full matching Mathlib coverage for
this actual-family statement remains unchecked, not established absent.

## Search, overlap and continuation decision

Queries included `site.stacks.math.columbia.edu derived category scalar
cohomology action cup product projection formula perfect complex Ext
locally free`, `site.stacks.math.columbia.edu coherent sheaf finite
support higher cohomology vanishes`, and exact follow-ups for global
derived Hom, Lemma 20.50.5, cup product 20.31.1 and homological Hom.
Only the primary Stacks statements above support the new coverage;
nonprimary search results and unrelated theorem hits are not inputs.
No full-matching stronger family theorem or evaluation of Phi_1 was
identified in this bounded comparison; that is not a novelty claim.

ATTEMPTS/047 retains unknown normal sections; ATTEMPTS/068 parks repeated
section/Euler/transgression tests; ATTEMPTS/069 names the actual global
entry left by coefficient Lefschetz. The actual-map working note and
history/338 contain the same reduction, not an independent audit or a
second value of that entry. This target therefore audits a canonical
result rather than introducing a duplicate lemma. It does not reopen
the stopped exclusion route. No persistent source blocker remains for
the audit itself.

DECISION SPECIALIZE approves exactly the TARGET above for one separate
proof audit, using citations rather than reproof of the standard inputs.
The completed literature step is EXPLORATION / REPRODUCTION: it adds
essential source comparison and a ready audit, but no mathematical
advance, error finding, new exclusion, bundle or cycle. L117's audit
remains pending; PROOF.md and the DAG need no change in this source turn.
