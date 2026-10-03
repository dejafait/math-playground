# Kato auxiliary-prime relations and the mixed determinant component

TARGET: Test whether auxiliary-prime Kolyvagin relations for Kato's cyclotomic Euler system exclude L013's nonzero mixed rational/Sha determinant component, without assuming finite p-primary Sha.
CHECKED: 2026-10-03
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: No new search for this target was performed in the completed mathematical model step; the saved derivative assessment's earlier searches concern determinant descent and related nonvanishing results, not this exact auxiliary-prime constraint.
SOURCE_EVIDENCE: Reused scope record only: Castella--Sano, https://arxiv.org/pdf/2601.14504v1, Theorem A and Sections 2.2/2.3.1 were inspected in the earlier assessment for Selmer/main-conjecture conclusions. The Kolyvagin relations and any claimed rational-image consequence have not been read and compared for this target.
COMPARISON: L013 satisfies the known degree-one descent, scalar divisibility and compatible local duality, even with a rational leading vector, but has a nonzero mixed rational/Sha determinant component. The previously inspected results control Selmer data; no available assessment identifies auxiliary-prime Euler-system relations as an exclusion of that component.
GAP: Locate the precise auxiliary-prime relations and their primitivity/local hypotheses, then determine whether they constrain the rational Kummer image rather than only Selmer modules, characteristic/Fitting ideals or nonzero character specializations.
REASON: This is additional arithmetic structure absent from the completed formal model and outside its approved coverage. A separate theorem-level source comparison is needed before deriving or importing an exclusion; no novelty or readiness is claimed.

## Proposed scope and discriminating test

Retain the cyclotomic, non-CM, good-ordinary p >= 5 setting and the
conditional dimension-two Selmer branch. Keep rational rank, finite
p-primary Sha and rational determinant membership unproved. Hypotheses
on residual images, auxiliary primes and primitivity must be recorded
from actual source statements rather than inferred from the scalar
characteristic equality already met by L013.

The proposed arithmetic constraint must exclude the mixed component
of the determinant preimage. Rationality of the contracted leading
vector alone is insufficient, since it already holds in L013. An
implication to Selmer dimension two or the cyclotomic main conjecture
also does not exclude the model. A source that assumes finite Sha,
rational rank two or the conjectural rational leading-term formula
would not supply the missing implication under the retained hypotheses.

Review the actual relations, the relevant Selmer structure and their
known consequences. If only module consequences are obtained, preserve
that exclusion and identify a concrete, independently testable arithmetic
condition rather than repeat this formal model or the parked Eisenstein
source blocker. No auxiliary-prime calculation or mathematical lemma
for this new target has been attempted in the completed step.

## Mathlib

Full coverage of this proposed arithmetic exclusion: **not checked**.
Supporting Euler systems, Kolyvagin relations and rational Kummer
membership: **not checked**. The cited primary paper is a previously
inspected related source, not a full statement match or a claimed
Mathlib reference for TARGET.
