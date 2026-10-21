# Exceptional completion on the five common excluded labels

Date: 2026-10-07. STEP_ID: 2026-10-07-mca-077-five-label-completion.

Approved target: Prove or refute that every L033 union-six pencil over F_(97^20) with no weight-three parameter has at most twelve valid additional finite incidences.

Reuse the unchanged EXPLORE assessment in
[the twelve-incidence review](literature/2026-10-07-six-coordinate-twelve-incidence-bound.md).
The main gap is arbitrary-family sixteen-count equality. This attempt
tests its exceptional branch after L035 and L036: use both actual
union-six clusters to determine the ten other supports on their common
five-label complement, and retain their exact polynomial compatibility.
The intermediate threshold is that all ten complement pairs must occur
once, with each exclusive tag selecting two disjoint pairs. This could
replace an arbitrary completion search by one uniform five-label
compatibility test. Continue if this produces a checkable restriction
beyond the single-cluster packing and four-pair involution; stop this
subtest if it merely restates those conditions. A refutation of the
approved bound still requires thirteen actual additional finite
incidences and every L010/L033 hypothesis. The all-disjoint branch,
universal extraction and challenge identification remain independent.

Read the complete proofs of L035 and L036, L034's distribution and
descent argument, L032's lift and rank arguments, and L010/L033's needed
kernel, equality, overlap, shortening and full-weight cases. Their uses
were checked, including distinct finite parameters and the nonzero
slopes in the second lift. No defect was found in those uses; this is
not a separate critical-audit completion. Targeted searches of L030–L036
and the six-coordinate drafts found no five-label completion reduction.
Reuse the existing duplicate/failure and primary-source comparison;
ATTEMPTS/017, /019 and /020 remain stopped. No broader source review,
finite sample, L015 enumeration or new mathematical script is used.

Unfinished reasoning saved before completion: let U and U' be L036's
two clusters sharing only x, put V=U minus {x}, V'=U' minus {x}, and
E=H minus (U union U'). There are six selected errors, four containing
x and two disjoint from the opposite cluster. Apply L033/L034 to the
second cluster without changing the original affine chart. Its unique
disjoint error should be the first cluster's error omitting x. Hence
the ten remaining errors meet each cluster in one exclusive tag and
have two labels in E. L035's packing should make their E pairs distinct;
ten pairs on five labels would then force every pair. For an error with
tags z,z' and pair {u,v}, write the two degree-seven shortened codewords
f(tau)-e and f'(tau)-e. Cancelling their three common roots should give
the exact identity
(X-u)(X-v)(q_0(X)+tau q_1(X))
= lambda product_(b in V' minus {z'})(X-b)
- lambda' product_(a in V minus {z})(X-a).
Check signs, polynomial equality rather than evaluations alone,
nonzero scalars, both lifts' tag multiplicities, and the disjoint-pair
condition before recording a result. Do not infer an orthogonal edge
coloring: two complement pairs might carry the same pair of tags.

Completed: [L037](../lemmas/L037-exceptional-five-label-completion.md)
proves the all-ten-pairs restriction, both tags' disjoint-pair conditions,
and exact quartic compatibility with the shared-coordinate equation.
The latter is essential: without it the polynomial identity may leave
a fifth error at x. The local converse checks all four nonzero weights,
all eight moments and same-support badness, keeping the original finite
chart. A necessary label determinant follows without assumptions on
rational affine parameters or weights.

One specified H-labeling with involution -X passes L036 but fails this
stronger necessary test: its required complement edge {12,47} has no
tag pair among all 25 possibilities. The full matrix, evaluation
vectors and product 67 mod 97 are in L037; the complete certificate is
`../scripts/exceptional-five-label/paired-label-test-result.json`,
reproduced by `python3 scripts/exceptional-five-label/paired_label_test.py`
from the notebook. All root-product evaluations were cross-checked by
coefficient expansion and Horner evaluation. The selected load-bearing
certificate value `/tests/1` was inspected in full, along with its tag
orders and complement. Other edges for this single labeling are saved
but unnecessary to the exclusion. This is no arbitrary-label sample
bound or actual-pencil construction.

The intermediate test succeeds: it gives a complete support shape and
excludes one involution-passing labeling by a field identity, beyond
the previous necessary test alone. Outcome ADVANCE / RESEARCH /
POTENTIALLY_NEW is local progress under the unchanged review, not
certified novelty. No new literature assessment was written, and no
uncovered external theorem was imported. Precise shortening citation
and seven-deletion applicability, plus unchecked Mathlib coverage, are
canonical in L037.

The twelve bound is neither proved nor refuted. Retain other exceptional
labelings, repeated ordered tag pairs and the all-disjoint branch. The
uniform compatibility of the ten quartic identities and shared x
remains the discriminating test for this mechanism; label determinants
alone are insufficient. L034–L037 still require separate critical
audits. Universal extraction and challenge identification remain open;
the global interval stays 11/q–16/q. Continue the same gate-approved
target, without reopening the recorded exhausted sampling criteria.
