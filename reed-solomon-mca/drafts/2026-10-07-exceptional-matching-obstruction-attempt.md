# Exceptional completion: compatibility of the two edge partitions

Date: 2026-10-07. STEP_ID: 2026-10-07-mca-078-exceptional-matching-obstruction.

Approved target: Prove or refute that every L033 union-six pencil over F_(97^20) with no weight-three parameter has at most twelve valid additional finite incidences.

Reuse the unchanged EXPLORE assessment in
[the twelve-incidence review](literature/2026-10-07-six-coordinate-twelve-incidence-bound.md).
The main gap is sixteen-count equality. The intermediate target is to
exclude its exceptional intersecting-tag branch using the compatibility
of L037's two partitions of the ten edges on E. This would leave only
L035's all-disjoint alternative in the union-six branch. Continue if
actual packing forbids repeated tag pairs and the resulting partitions
are impossible; abandon this subtest if such partitions exist, retaining
the full quartic and shared-coordinate tests. This does not assume a
universal union-six cluster or resolve challenge identification.

Before lengthy work, save the following unfinished reasoning. L035 says
the only intersecting same-tag pair for U has tag x. If two remaining
supports have the same tags z in V and z' in V', their outside triples
both contain z', contradicting that conclusion because z is not x.
Thus distinct ordered tag pairs seem forced, despite L037 deliberately
not asserting this. The two partitions of K_5 into five matchings of
size two would consequently have no common matching. Test that tiny
abstract assertion completely, rather than sampling field labelings.
Any finite verification must save all partitions and pair comparisons;
the canonical proof must justify exhaustiveness explicitly.

Inspected the needed L010 equality/kernel statements and proofs, L032's
fixed-block lift/classification proof, L033's full-weight shortening
cases, all of L034–L037, and the previous completion attempt/history.
Targeted searches for orthogonal partitions and repeated-tag restrictions
found no earlier proof of this exclusion. Reuse the source comparison
and failed-route checks in the saved assessment; ATTEMPTS/020's sampling
stop remains in force. This is a uniform support obstruction inside the
approved target, not a new source review, arbitrary-label sampling,
L015 enumeration, or a reopening of an exhausted mechanism. Elementary
finite case analysis is to be written out, with no originality claim
for the abstract graph fact and no reliance on an uninspected theorem.

Completed: [L038](../lemmas/L038-exceptional-completion-matching-exclusion.md)
excludes the whole exceptional branch. L035 forbids the repeated tag
pair; the complete five-label partition classification contradicts that
restriction. The elementary exhaustion fixes the matching avoiding one
vertex (three choices), then its two possible completions. All six rows
and all fifteen common-matching witnesses are canonical in L038. This
supersedes the need to eliminate exceptional labelings by their quartic
identities; those necessary identities and earlier labeled certificates
are preserved, not invalidated.

The supplementary exact script enumerated all 3003 five-subsets of the
fifteen matchings and independently recursed on the least uncovered edge.
Both procedures returned the same six partitions. Every distinct pair
has exactly one common matching; completion requires zero. No check
failed. The full certificate is
`../scripts/exceptional-five-label/matching-obstruction-result.json`;
L038 records its reproduction command. Its entire `/partitions` and
`/intersection_matrix` values were inspected with the JSON inspector's
`--full` option. No field-label sample or L015 calculation was used.

The continuation test succeeds with a uniform support obstruction,
rather than a necessary condition passing indefinitely through more
labelings. Outcome ADVANCE / RESEARCH / POTENTIALLY_NEW is local progress
toward the approved target, not certified originality of the application
or the elementary partition fact. No new literature assessment was
written. The exact prior EXPLORE target and assessment remain unchanged.

Only the all-disjoint branch of L035 survives when N_ext=13 and N_3=0.
The next bounded test should use its degree profiles and L032's forbidden
small unions; its existence and moment compatibility are unresolved.
Essential continuation inputs are L010, L032–L035 and L037–L038, with
the earlier conditional proofs and this new exclusion still awaiting
separate critical audits. Retain equality before balance/packing,
full weights, eight moments, nonpersistent D/locators, original finite
chart and same-support badness. Universal extraction and ABF26 remain
independent gaps. The twelve bound is neither proved nor refuted and
the global interval stays 11/q–16/q. This completes one coherent attempt.
