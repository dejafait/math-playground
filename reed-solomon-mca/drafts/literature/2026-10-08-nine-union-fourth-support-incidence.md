# Nine-union fourth-support incidence — completed scope review

TARGET: Determine an exact fourth-support incidence criterion for L041's tau=1 local family, retaining arbitrary H-labels, extension-field weights, full-weight gates and the original finite chart.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Five narrow fourth-support, quotient, affine-syndrome and recurrence searches; compared L016's analytic quotient and universal branch, L010, L041–L042 and ATTEMPTS/008–009; reused adequate nine-union and general-ray assessments rather than repeating a general MCA survey.
SOURCE_EVIDENCE: Inspected Chojecki, Shortening Bounds for Reed–Solomon MCA, live author TeX v9.2 dated July 17, 2026, on 2026-10-08, source lines 2785–2935: drc:lem-locator-recurrence (DR2) and drc:thm-exact-compiler (DR6–DRC), full hypotheses and proofs, direct URL below; reused Hall Theorem 5.1.1, pp. 63–64, and Marquez-Corbella–Pellikaan section 5, pp. 7–8, from saved inspected extracts.
COMPARISON: Known recurrence and rank tests cover fixed-support intersections; L016 already eliminates shared-coordinate columns for its saved labels at 0,1,2. Neither that count five nor L041–L042 gives an arbitrary-label additional-support classification with every weight gate. The remaining work is a local specialization of known machinery.
GAP: Obtain a usable reduced criterion in L041's free weights and original finite parameter, retaining all exceptional quotient ranks, universal systems and recovered fourth weights; additional-error counting and universal extraction remain independent.
REASON: Essential coverage is now ready for one bounded REPRODUCTION attempt on the unchanged TARGET; no new mathematical relation or calculation was derived in this literature-only review.
SCOPE: Exact TARGET only: F=F_(97^20), H order sixteen in F_97, k=8, pinned four-omission cell, L041 local converse tau=1 with singleton counts (2,2,3), three distinct original finite parameters, arbitrary F weights, nonzero lambda and every normalized weight gate; a distinct fourth four-support and parameter, full fourth weights, unrestricted original excluded direction. No equality or rational chart assumption.
LITERATURE_REASON: Checkpoint 090 proposed a changed additional-support target with REVIEW_REQUIRED coverage; this separate review compares its precise quotient and weight-gate scope against inspected primary recurrence results.

## Scope and use retained from checkpoint 090

The proposed essential input IDs are L010, L041 and L042. L016 is an
analytic comparison lead, not an imported finite bound. Fix F=F_(97^20),
H of order sixteen in F_97, k=8 and the pinned four-omission cell.
Use L041's tau=1 pattern with singleton counts (2,2,3), three distinct
original finite parameters, nonzero lambda and all normalized weight
gates. A candidate fourth support is a four-subset of H different from
the three given supports, and its parameter must be original finite
and different from all three selected parameters. All present error
weights must remain nonzero. Do not impose equality, rational parameters,
a rational excluded direction or a completion premise.

The desired criterion should resolve actual moment membership with these
gates in explicit equations or a justified quotient/rank test; merely
restating the eight moment equations is insufficient. A useful result
would make later additional-error counting or exclusion possible. To
reach sixteen from the three known parameters would still require
thirteen additional distinct parameters; the desired criterion alone
would not bound that number or supply universal extraction.

The comparison below completes the separate coverage review requested
at checkpoint 090. It approves an attempt, not an incidence assertion.
The existing local triple criterion and fixed-triple count are retained
with their original scope.

## Primary recurrence input and applicability

Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[live author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026; retrieved 2026-10-08. This mutable file is not
certified identical to ePrint 2026/1463. Read source lines 2785–2935,
including definitions, both complete proofs and all zero-direction cases.
Citation anchors are `drc:lem-locator-recurrence` (DR2) and
`drc:thm-exact-compiler` (DR6–DRC).

For RS redundancy R and distinct weighted Vandermonde columns with
nonzero multipliers, an error support of size t<R has span membership
exactly when its R-t locator recurrences vanish. The proof identifies
the annihilator with multiples of the monic support polynomial using
MDS column rank. For a fixed syndrome pair, a finite transverse
intersection requires a nonzero projected direction and proportional
projected syndromes; a pivot gives its unique parameter. A zero projected
direction gives either no intersection or a common intersection.

The source hypotheses fit L010's columns: R=8, t=4, exact agreement
a=12, multipliers x!=0, and coordinate eta_j=s_(j+1) for j=0,...,7.
There is no subfield condition on syndrome coefficients. Full-weight
and selected-parameter exclusions remain checks to be supplied locally.

## Reused inputs and exact remaining difference

Hall, *Notes on Coding Theory*, undated
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 and proof, printed pp. 63–64, gives the standard dimension
and distance under distinct evaluation points and nonzero multipliers.
Reuse the full inspected extraction in
`2026-10-05-two-block-moment-obstruction.md`, Primary theorem and applicability.
Here n=16,k=8 and unit multipliers meet its hypotheses over F.
No new distance proof is needed.

Marquez-Corbella–Pellikaan, *A characterization of MDS codes that have
an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript dated 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the following GRS shortening
formula, printed pp. 7–8. Reuse the inspected extraction in
`2026-10-07-six-coordinate-triple-equality-obstruction.md`, Primary shortening input,
and the seven-deletion applicability in L041. These cover its shortened
kernel; they need no fresh retrieval or reproof.

Read L016's analytic parameterization, full-triple gate, recurrence
converse, constant-column quotient, rank cases and universal branch.
Its proof already supplies more than raw moment equations: a reduced
parameter system, recovery of shared-coordinate variables and tests of
the actual fourth weights. Its finite table and count five are confined
to its stated supports at 0,1,2; they are not inputs to this target.
Read L041's local criterion and converse, L042's statement and audit
scope, and L010's moment kernel, uniqueness and pointwise identities.
The proposed attempt must give the corresponding reduced system and
weight recovery for arbitrary labels and original finite parameters.
No such formula, rank classification or rational descent is asserted here.

The source rank test can be imported without reproving the decoder or
annihilator theorem. Additional elimination is justified only to expose
L041's actual free weights and exceptional systems for later counting.
A source citation alone does not discharge those checks. This is why
the decision is SPECIALIZE and the mathematical classification is
REPRODUCTION, rather than a claim of a new theorem beyond checked sources.

Reuse the circuit and general MCA comparisons in
`2026-10-07-nine-coordinate-triple-compatibility.md` and
`2026-10-07-six-coordinate-twelve-incidence-bound.md`.
Those recorded conclusions require hypotheses or bounds unavailable
here. The parked ABF26/Jo and campaign leads remain unread and are not
essential premises for this local reduction; no priority claim is made.
Mathlib coverage of the exact criterion and supporting recurrence is
not checked. No absence or formal verification is inferred.

## Discovery record and preserved failures

Queries actually issued on 2026-10-08:

- `"Reed Solomon" "syndrome" "quotient" "affine" support recurrence`
- `"mutual correlated agreement" "fixed support" recurrence`
- `"Reed-Solomon" "syndrome ray" compiler`
- `"Reed-Solomon" "fourth support" syndrome`
- `"Reed-Solomon" "locator recurrence" "affine"`

Results included decoder references, affine-variety decoding, formal
coding-library and random-code leads. Their snippets are not theorem
coverage. The named author source was inspected directly instead.
No exact arbitrary-label gated criterion was established by these
searches, and failed discovery is not evidence of novelty.

ATTEMPTS/008 and /009 were read in full. The former's determinant-only
zero-syndrome-kernel blindness and incomplete extension-field coverage
remain load-bearing failure evidence. The latter stops the completed
fixed L016 generator, whose maximum five is below the eleven-count
witness. This target changes the label and chart scope and uses the
full L041 kernel; it does not rerun that stopped enumeration. Retain
ATTEMPTS/017, /019–021 and the prior assessments' failure comparisons;
no universal cluster extraction, positive-only sampling or support-only
completion is authorized. No cross-notebook input is used.

## Ready bounded continuation

One REPRODUCTION proof attempt on the exact TARGET is ready. Use
L010, L041 and L042 as essential local inputs and L016's analytic
quotient mechanism as the antecedent; cite the recurrence theorem.
Check every quotient rank and universal branch before inversion,
translate any affine parameter substitution back to the original chart,
recover all four actual weights, and retain the triple gates and every
parameter exclusion. Do not assume prime-field weights or parameters.

Continue if a necessary-and-sufficient reduced criterion with explicit
recovery and all gates follows, even if counting is still unresolved.
If the attempt only restates eight moments or the generic rank test,
misses an exceptional rank, or requires unjustified descent, save that
obstruction and reassess. A compatible fourth error is not a thirteen-error
completion: sixteen still requires thirteen additional distinct finite
parameters. Universal extraction and ABF26 identification remain open.
No lemma, mathematical script or new incidence relation was written here.
