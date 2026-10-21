# Pair Jacobian lower-rank certificate — source review

2026-10-20. Literature-only review of the unchanged saved target:
Test whether rational divisor classes on L110's Jacobian certify
Mordell–Weil rank at least two.

The exact-instance rank is still unknown. The useful downstream test is
whether the strict rank-below-two Chabauty threshold is impossible. A
successful lower certificate would close that route only, leaving rational
points, the minus-three marking, degree-nine root recovery, remaining
factors, both L095 systems and minus-eleven unresolved.

Read L110's hypotheses/model and the completed independent-audit record;
reused the upper-rank assessment, including its exact-instance searches
and backend stop. Searched the local pair assessments and the relevant
old rank/S-class failures for duplicates. No existing lower-rank
certificate occurs in those inspected records. No backend availability
probe, point search, model transformation or mathematical script was run.

Primary passages now inspected: Stoll (2001), equation (1.1), Section 4
through Lemma 4.3 and the local functoriality; Müller, Lemmas 1.17–1.18,
Section 2.4 through Proposition 2.7 and its even-degree warning;
Stoll's 2025 rank-one note, Section 2; Magma's named search, torsion,
regulator and rank-bound interfaces; Conrad's simple-root Hensel theorem
and uniqueness proof; Ben Lynn's proof of Euler's criterion. The canonical
assessment contains citations, the future finite search caps and exact
certificate obligations. General theorems are imports; their application
and arithmetic remain work for the next research turn.

The selected detector uses localized Kummer square classes, with a
two-torsion allowance, rather than bare point reductions. It can be
implemented using exact rational/polynomial arithmetic and modular
exponentiation. Heights would need rigorously certified error intervals;
the existing inaccessible backend and decimal regulator examples do not
supply those intervals. Full Selmer/class/unit completeness is unnecessary
for this lower-bound test. Failure of bounded detection is not dependence
and supplies no rank upper bound.

Completed assessment:
[pair lower-rank test](literature/2026-10-20-pair-jacobian-rank-lower-test.md).
No new lemma, mathematical script, rank value or Beal advance is claimed.
