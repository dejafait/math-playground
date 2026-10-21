# Proposed critical audit of the fixed-label collision exclusion

TARGET: Critically audit L080's complete fixed-label exclusion of four linear isolated triangle anchors.
CHECKED: 2026-10-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed exact four-anchor comparison and L057/L059 audit assessments; read L080, L057 (1)–(14), L059 (1)–(4) and its original-chart proof, saved primary applicability extracts, ATTEMPTS/029 and history/188; no fresh external search or calculation.
SOURCE_EVIDENCE: Reused Chojecki author TeX v9.2 July 17, 2026 DR2/DR6–DRC lines 2785–2935 with previously inspected full proof cases, Hall Theorem 5.1.1 pp. 63–64 and interpolation p. 65, and Marquez-Corbella–Pellikaan section 5 pp. 7–8; inspected program interfaces and the imported Gaussian arithmetic to delimit the audit.
COMPARISON: Known inputs cover individual recovery and chart deletion under unchanged hypotheses; no inspected theorem supplies the fixed-label collision exclusion. The prior complete formula-path replay is evidence to audit, not an independent critical verdict.
GAP: Coverage is ready for the separate proof/certificate audit; complete enumeration, signs, gates, full fibers and chart-free superset passage remain to be critically verified.
REASON: Approve one bounded POTENTIALLY_NEW audit of the exact TARGET using ready ingredients; neither correctness nor originality is certified by this literature-only comparison.
SCOPE: Exact TARGET only; F_(97^20), fixed H and P=(64,75,33), Y=(1,96), Z=(18,79), W=(8,50), normalized w in (F_97 minus {0,1})^3, arbitrary distinct original finite gamma_i and lambda!=0; full isolated disjoint-P anchors only, no equality or arbitrary-label assumption.
LITERATURE_REASON: Newly written L080's separate critical audit was REVIEW_REQUIRED; compare its precise certificate obligations with ready source coverage without repeating external discovery.

Reuse `2026-10-12-four-linear-isolated-anchors.md` and its precise primary
source comparison. Do not reopen the incomplete enlarged sweep or the
ABF26/census source blockers. Essential inputs are L057 and L059. Check
L080's proof, complete support enumeration, all projected rank cases,
gated/ungated and full/lower-weight splits, independent seven-column
formula signs, all 492 numerator residuals, exact full fibers, all ten
pair intersections and all five quartet failures. Both programs and their
full JSON artifacts are named in L080. The original E gate is omitted
only to enlarge the set; establish that deletion cannot create a quartet
and distinct mu give distinct finite parameters when E survives. Scope:
P=(64,75,33), Y=(1,96), Z=(18,79), W=(8,50), w in G^3, and arbitrary
admissible original gamma_i and lambda over F_(97^20). No equality,
cross-notebook input, arbitrary-label inference or challenge solution is
assumed. Success validates this restricted exclusion only; a defect
requires preserving the evidence and repairing the specific issue.
No additional label sweep is a continuation of this audit.

## Separate scope comparison completed October 13

The main gap remains arbitrary sixteen-count equality-family exclusion,
including the uniform triangle twelve bound and arbitrary extraction.
The intermediate target is exactly TARGET. A successful audit makes this
fixed-assignment negative result reliable route evidence; it does not
improve 11/q–16/q. Other label assignments, other triangle patterns and
challenge-definition qualifications remain independent unresolved gaps.
Continue only if the complete proof and replay meet the obligations below;
a failed implication or certificate mismatch requires a specific recorded
repair. Neither outcome authorizes a larger label sweep.

### Primary inputs and specialization

Reuse P. Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[author TeX v9.2, July 17, 2026](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
DR2 (`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), lines 2785–2935. Their statements and full
proof cases were inspected in the earlier assessments. Read the saved
extraction in `2026-10-08-nine-union-fourth-support-incidence.md`,
“Primary recurrence input and applicability,” in this turn. Distinct
weighted Vandermonde columns, nonzero multipliers and t<R are essential:
R=8, t=4, eta_j=s_(j+1) and multiplier x!=0 fit the fixed H over F.
The compiler's full zero-direction cases do not replace the restored
three-column quotient equations. No source reproof is needed. This
review does not certify that the mutable source is unchanged today or
identical to ePrint 2026/1463.

Reuse J. I. Hall, *Notes on Coding Theory*,
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 with full proof pp. 63–64 and interpolation p. 65;
read the saved “Primary theorem and applicability” extraction in
`2026-10-05-two-block-moment-obstruction.md`. Arbitrary field, distinct
evaluation labels, nonzero multipliers and 0<k<=n give distance nine
at n=16,k=8. This supports the audited local inputs, not a quartet bound.

Reuse I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS
codes that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
section 5, Definitions 5.1–5.2, Lemma 5.3 and following unnumbered
GRS shortening formula, pp. 7–8 of the
[accepted manuscript dated 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
Read the saved “Primary shortening input” in
`2026-10-07-six-coordinate-triple-equality-obstruction.md`. Seven
successive deletions in the audited triangle input have dimensions
8 through 2 before deletion and nonzero retained label differences.
No new shortening proof or equality premise is needed.

L057 supplies the exact isolated ratio, restored equations, numerator
weights and original finite recovery; L059 supplies the chart/table
interpretation. Read their relevant complete statements and L059's
original-chart proof. L080 narrows these hypotheses to one labeling
and full isolated anchors; the sources do not supply its enumeration
or collision conclusion. L068 is a regression comparison, not an input.
L064, L066, L069 and L071 motivate other targets but are unnecessary
for this audit. No cross-notebook theorem is used. Full matching and
supporting Mathlib coverage remain not checked.

### Approved proof and certificate obligations

Inspect the full two programs named in L080 and the imported `invert`
and `mul` functions in `verify_fixed_union_table.py`. Their interfaces
and that arithmetic were read here only to delimit the evidence; the
programs were not critically audited or run. The next audit must check:

* The exact fixed labels, coefficient Q evaluations and complete ordered,
  duplicate-free 715-support set; every isolated, one-zero and both-zero
  case, mu=-1 rejection, base-weight gate and lower-weight split.
* The producer's L057 formula bridge and the verifier's seven-column
  inversion bridge, including residual orientation, restored signs and
  all divisions. Reconstruct all 492 gated numerator vectors and all
  eight moments, including the 64 lower-weight rows.
* Exact full-row comparison, all weight fibers and scalar deduplication,
  all ten simultaneous pairs and all five quartet rejections, rather
  than selected positives or summary counts alone.
* The passage from chart-free full rows to arbitrary original finite
  charts: E deletes rows only, its surviving scale is nonzero and
  distinct eligible mu represent distinct nonbase finite parameters.
  Both-zero and lower-weight rows are outside this target definition,
  not removed from a claimed full recovery bound.

Use the existing full artifacts
`scripts/triangle-recovery/four-linear-anchor-collisions.json` and
`scripts/triangle-recovery/four-linear-anchor-collisions-verification.json`.
Check their complete relevant evidence and replay both programs under
the notebook rules. Compare the producer hash with L080's recorded hash
and preserve/report any change or mismatch; a preview is not verification.
The two paths share Python and residue arithmetic, so their independence
is limited to formulas. Complete case equality and all rejection gates
are required in addition to a successful exit. This turn performs none
of those checks and asserts none of the recorded counts anew.

### Duplicate and failure boundary

Reuse the completed queries and stronger-result comparison in
`2026-10-12-four-linear-isolated-anchors.md`; no failed search certifies
novelty. Its known recurrence and coding results do not resolve a
simultaneous quartet. ATTEMPTS/029 and history/188 already stop the
fixed-assignment construction attempt. Earlier sampled-rank, formal-root,
balance-only extraction and forced-zero failures remain parked. The
proposed audit checks recorded complete evidence rather than reopening
those mechanisms. ABF26 and the classification-census sources remain
unread blockers for independent work, not essential coverage here.

EXPLORE approves one subsequent POTENTIALLY_NEW RESEARCH proof audit of
exact TARGET. This is coverage approval only, with no mathematical
advance beyond the sources checked, certificate verdict, new lemma,
script change or argument change.
