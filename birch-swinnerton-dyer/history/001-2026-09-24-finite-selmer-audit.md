# 2026-09-24 — Initial scope and finite Selmer audit

The starting notebook had no local modifications, lemmas, or previous failed
routes. Existing changes outside this notebook were left untouched. The
[source audit](../foundations/01-target-and-scope.md) fixed the target as
Clay's rank assertion and separated its coefficient refinement. Named
[baseline results](../foundations/02-standard-inputs.md) locate the remaining
uniform problem beyond analytic rank one.

The discriminating test asked whether an arbitrarily long finite initial
Selmer tower could certify rank two after granting finite Sha and a full
nondegenerate alternating pairing. [L001](../lemmas/L001-finite-selmer-tower-rank-ambiguity.md)
answers negatively for the explicitly unmarked group data: ranks zero and
two fit the same observed tower, maps, and pulled-back pairings. The achieved
bound r <= 2 falls short of the required equality r = 2. This is an explicit
algebraic audit of the standard descent limitation, not a novelty claim or
an elliptic-curve counterexample.

Decision: stop that data-only inference. The main BSD gap is unchanged, but
this arithmetic shortcut is now excluded with precise hypotheses. A global
characteristic-series mechanism is the next direction because it can
potentially constrain an entire Selmer module. Its specialization, its
relation to analytic order, and the Sha defect still require separate
justification; no Iwasawa theorem is assumed in this step.

The [saved draft](../drafts/2026-09-24-finite-selmer-audit.md) records the
selection and test. The [exact finite-group checks](../scripts/finite-selmer/check-results.json)
pass for p = 2,3 and observation depths 1,2: six levels, 7,011 pairing and
addition checks, 97 downward-map checks, and 13 upward-map checks. They
support the construction; the proof for arbitrary p,N is in L001.
The documentation checker passed with one node and no lemma edges using
`python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`.

Completed step BSD-2026-09-24-001-finite-selmer-audit is NEGATIVE. The budget
of exploration turns without an advance or informative negative result is
0 of 3. There is no candidate proof or disproof of the main target.
