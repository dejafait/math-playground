# 005 — 2026-09-25 — Radius-dependent certificate multiplicity

Completed one induction and counting step in the frozen affine-line model.
The [saved assessment](../drafts/2026-09-25-certificate-multiplicity.md)
records the gap, target, downstream use, redundancy check, and discriminating
test. The [official statement](https://proximityprize.org/) and
[paper metadata](https://eprint.iacr.org/2026/680) were reread; no source bridge
is asserted and failed PDF retrieval was not repeated. Existing work remains.

[L004](../lemmas/L004-radius-dependent-certificate-multiplicity.md) proves
the proposed multiplicity by deletion induction and uses disjoint certificate
families to obtain a radius-dependent error bound. The bound reaches the
actual 2^-128 budget on a smooth length-256, rate-1/2 code over F_(257^32)
at every delta < 90/256, where the previous all-radius sufficient test fails.
It does not determine the maximal safe radius or the error on the next cell.
The local multiplicity is sharp; simultaneous sharpness of the global count
does not follow. The proof uses L003's interpolation characterization, which
is the new row's only direct lemma input; earlier DAG rows are preserved.

Outcome: ADVANCE for a relevant mathematical input, with exploration turns
reset to zero and STATUS kept IN_PROGRESS. The reason for the subsequent
direction is observed slack at support cutoff n-1: for q=5, n=5, k=2,
enumeration gives a maximum of 2 bad challenges while the new bound allows 3.
Quotient-space geometry could distinguish realizable challenge intersections
from abstract certificate counts. This is motivation, not a proved formula;
the sole concrete next action is in PROGRESS.md. No complete challenge
candidate is present, and the source and maximality gaps remain.

Validation: `python3 scripts/certificate-multiplicity/check.py` passed
111,013 noncode-support cases across nine parameter sets and 31,994 input-pair
classes across seven sets, with direct polynomial membership on every support
and challenge. The exact example thresholds also passed. Enumeration is
auxiliary to the induction and partition proof. The original support-size
requirement, challenge-dependent supports, zero directions, integer floor,
and strict radius endpoint were reviewed directly.

`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
passed with 5 nodes, 2 edges, valid links, and compact overviews;
`git diff --check -- .` also passed. These structural checks do not certify
the mathematics or the paper-to-model correspondence.
