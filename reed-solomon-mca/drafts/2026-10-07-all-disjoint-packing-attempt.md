# All-disjoint union-six packing attempt

Date: 2026-10-07. STEP_ID: 2026-10-07-mca-079-all-disjoint-packing.

Approved target: Prove or refute that every L033 union-six pencil over F_(97^20) with no weight-three parameter has at most twelve valid additional finite incidences.

Reuse the unchanged EXPLORE assessment in
[the twelve-incidence review](literature/2026-10-07-six-coordinate-twelve-incidence-bound.md).
The main gap is arbitrary-family sixteen-count equality. Intermediate
target: test L035's remaining all-disjoint outside-triple profiles against
L032's forbidden actual triple unions. A profile exclusion could narrow
the union-six thirteen-incidence case before moment elimination. Continue
if an exact profile restriction or an explicit surviving packing is
obtained; stop this support-only test if all triple-union conditions
admit a packing, retaining moment compatibility as the next obstruction.
No abstract packing refutes the twelve-incidence assertion.

Inspected L032's fixed-block proof, L033's exact incidence statement,
all of L034/L035, and L038's complete argument. Local searches in the
six-coordinate drafts, current histories and L030–L038 found the prior
exceptional exclusion but no elimination of the all-disjoint profiles.
Reuse the recorded source comparison and ATTEMPTS/017, /019, /020;
neither universal cluster extraction nor cyclic containment or finite
field-label sampling is being reopened. The standard coding inputs retain
the citations and qualifications in L032/L033. No additional literature
is required for this unchanged approved target.

Unfinished reasoning saved before calculation: let a,b be the counts of
K_0 labels in the two disjoint triples with a common tag. Their union
with K_0 has 10-a-b outside labels and one tag. L032 should require
a+b<=2. Since all six such sums total twelve, each should equal two.
Two triples with two K_0 labels appear impossible by applying L032 to
them and K_0. If t=1, the W label in the unique two-K_0 triple seems
unable to occur in any one-K_0 triple, contradicting its degree four.
This suggests t=0 and four perfect matchings on W, with the leave a
fifth perfect matching. The derivation and a surviving disjoint-tag
pairing remain to be checked. Actual errors, full weights, all eight
moments, original finite chart, nonpersistent locators and N_3=0 are
still required; no field calculation or equality completion is claimed.

Completed: [L039](../lemmas/L039-six-coordinate-equality-four-matchings.md)
proves t=0 uniformly. The final proof directly excludes two two-K_0
triples and then excludes a unique such triple by its W-label degree;
it does not need the tentative same-tag sum argument above. The twelve
remaining triples are organized into four edge-disjoint perfect matchings
on W, with disjoint tag pairs. This is ADVANCE: a necessary equality
restriction, not a twelve-incidence bound or certified novelty.

The continuation test also identifies an exact support-only obstruction.
An explicit pairing exists, and the complete case proof in L039 shows
that every construction of this form with disjoint tag pairs has just
the selected union-six triple below union size nine. The supplementary
certificate `scripts/all-disjoint-packing/profile-witness-result.json`
checks all 560 triples and 8008 six-subsets of the displayed witness,
with zero failures and actual minimum six-support union eleven against
required at least nine. Complete factors, tagged triples, summary and
check flags were inspected; the numerical minimum is auxiliary, not a
proof premise. The certificate contains full check records, not samples.

Stop the support-only exclusion according to
[ATTEMPTS/021](../ATTEMPTS/021-all-disjoint-support-only-exclusion.md).
Continue the unchanged approved quantitative target through actual
moment compatibility of the remaining matching form. Inputs for that
attempt are L010, L032, L033, L034, L035, L038 and L039, with their
stated qualifications and unaudited conditional results retained. No
abstract witness supplies field labels compatible with moments, actual
nonzero error weights, finite parameters or nonpersistent locators.
N_3=0 and N_ext=13 remain hypotheses whenever equality is invoked.
Global fifteen, universal extraction and ABF26 identification are open.
