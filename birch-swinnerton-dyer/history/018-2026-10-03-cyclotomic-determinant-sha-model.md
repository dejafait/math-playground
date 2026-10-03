# 2026-10-03 — Degree-one cyclotomic descent with a Sha direction

Completed one mathematical step on the exact covered target in the
[saved SPECIALIZE assessment](../drafts/literature/2026-10-03-cyclotomic-kato-derivative.md),
without further literature work or changes to that assessment.
[L013](../lemmas/L013-cyclotomic-determinant-descent-with-sha-direction.md)
gives the full proof of the compatible model; the prior working note
now points to the completed calculation. Earlier changes and
unfinished arithmetic work are preserved.

The new information is that the degree-one determinant descent can
coexist with marked rational/Sha dimensions (1,1), even when its
leading vector is rational. The local-condition triangles, adjoint
boundary, inverse-parameter duality, first Bockstein, dual H^2 factor
and exact degree, and order-two scalar/characteristic equality are
all retained. This strengthens the previous formal insufficiency
evidence by including the new descent datum, rather than repeating
the characteristic-order or anticyclotomic models.

The formal rank inference is stopped in
[ATTEMPTS/014](../ATTEMPTS/014-cyclotomic-determinant-rank-inference.md).
The main lower bound r >= 2, actual Kummer membership, actual derivative
nonvanishing/degree, production from m(E) = 2 alone, and higher ranks
remain missing. No actual elliptic curve or Euler system is constructed,
and no complete candidate proof or disproof appears.

The next direction asks whether auxiliary-prime Kolyvagin relations
provide additional arithmetic information excluding the mixed
determinant component. Its
[new assessment](../drafts/literature/2026-10-03-kato-kolyvagin-mixed-component.md)
is REVIEW_REQUIRED because that exact constraint lies outside the
saved scope; no theorem or calculation for it is claimed now. The
exhausted Eisenstein route remains parked.

Step BSD-2026-10-03-018-cyclotomic-determinant-sha-model has outcome
NEGATIVE, kind RESEARCH and classification REPRODUCTION. Sano's
known descent formalism is cited and reproduced in this explicit
example; no discovery beyond the checked literature is claimed.
Exploration turns used remain 0 of 3. STATUS stays IN_PROGRESS.
The new DAG row has no lemma inputs: named sources and explicit
algebra supply the proof; L002 and L011 are only contrasts.

Validation: `python3 scripts/cyclotomic-determinant/check_model.py`
passed the exact polynomial checks. The shared checker passed with
13 nodes, 11 unique edges, an acyclic graph, complete file coverage,
valid local links and compact overviews. The literature validator
accepts the RESEARCH report with the unchanged prior SPECIALIZE
assessment and REVIEW_REQUIRED for the exact proposed follow-up.
All 81 entry files remain: only PROGRESS.md, PROOF.md and DAG.md
changed among them; earlier lemmas, scripts, assessments and history
are preserved. The local diff whitespace check passed. Mathematical
review checked the inverse determinant convention and confirmed that
L013 has no genuine prior-lemma inputs. Shared infrastructure and
other notebooks are not edited.
