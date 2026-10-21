# Two antipodal pairs — completed enlarged-scope comparison

TARGET: Determine whether triangles with Y={y,-y}, Z={z,-z} and an arbitrary disjoint singleton pair W have at most three isolated disjoint-P recovery scalars, retaining zero fourth weights and the original finite gates.
CHECKED: 2026-10-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Three new exact antipodal/triangle-count queries; reused the ready triangle-count and L067-audit searches; inspected L057 equations (5)–(12), L067 arbitrary-pair identities and restricted count scope, L066 threshold statement and ATTEMPTS/025. Exact searches and limits below.
SOURCE_EVIDENCE: Reused Hall Theorem 5.1.1 and interpolation pp. 63–65, Marquez-Corbella–Pellikaan section 5 Lemma 5.3 and shortening formula pp. 7–8; freshly retrieved Chojecki author TeX v9.2 dated July 17, 2026, DR0–DR8/DRC statements and full recurrence/compiler proofs, lines 2785–2935; inspected deltastar author-page statements section 3.1–3.3 only, with linked implementations unread.
COMPARISON: Recurrence and interpolation hypotheses survive arbitrary W, and audited L067 identities (1)–(3) and scaling explicitly cover arbitrary pairs; its finite maximum three requires three antipodal pairs. No inspected source supplies the two-antipodal simultaneous bound; broader ready comparisons supply no stronger applicable count.
GAP: Establish or refute the simultaneous maximum three in this enlarged fixed-H family with complete label/shared-role/support coverage and original restored equations; no new enumeration, algebraic restriction or maximum is established in this source turn.
REASON: The changed hypothesis has now received a bounded exact-scope comparison; unchanged standard ingredients are adequately covered, but no matching import was established. Approve exactly TARGET for one bounded mathematical attempt, without certifying novelty.

## Preserved proposal at checkpoint 154 (before this review)

Proposed hypotheses: F_(97^20), fixed H of order sixteen, nine distinct
labels with ordered shared roles P=(a,b,c), Y and Z disjoint antipodal
pairs, W any two-element subset of H outside them, and P outside all
six singleton labels. Retain original distinct finite gamma_i, lambda!=0,
p(1-p)q(1-q)r(1-r)!=0, mu!=0,-1 and E!=0. Count distinct isolated
scalars with a four-support disjoint from P, including zero fourth weights;
do not assume a rational original chart or that all recoveries are isolated.

Essential candidate inputs: audited L057's exact recovery criterion,
audited L067's arbitrary-pair evaluation identities (1)–(3) and subgroup
scaling only, and audited L066's conditional four-anchor requirement.
L010/L065 enter through L066 and L041 through audited inputs. L067's
antipodal finite count does not cover the proposed enlargement. Pending
L060–L064 audits, arbitrary extraction and ABF26 identification are not
premises. No cross-notebook result is proposed.

Downstream use if later approved and proved: a relaxed bound three would
contradict L066's four full anchors and exclude thirteen additional
recoveries in the enlarged family. It would leave fully arbitrary pairs,
other patterns, extraction and the challenge definitions unresolved.
A verified four-scalar fiber would instead refute this intermediate
three-bound; it would not disprove the twelve bound or the MCA target.

Review the changed hypothesis against the already inspected recurrence,
shortening and interpolation sources and stronger count comparisons.
Check L067 and ATTEMPTS/025: the historical failure concerns unstructured
selected-label sampling and formal common-root conditions. A proposed
complete structured family test is independently falsifiable, but its
new label scope must not be treated as already enumerated. No new
mathematics or calculation for this target has been performed here.

If separately approved, the continuation test is a complete coverage
certificate with scalar maximum at most three, or an actual four-scalar
fiber verified in the original eight moments and finite gates. Partial
label samples, projected rows alone and failure to find four do not settle
the claim. Full and supporting Mathlib coverage remain not checked.

## Completed separate comparison — step 155

LITERATURE_REASON: Step 154 saved a new target dropping W-antipodality with REVIEW_REQUIRED; this turn compares that changed scope and reuses ready ingredient assessments rather than refreshing unchanged mathematics.

The main local gap is the uniform triangle twelve-recovery bound, within
the unresolved arbitrary equality-family exclusion. The intermediate target
is exactly TARGET above. Its plausible use is L066's conditional four-anchor
contradiction; it leaves fully arbitrary singleton pairs, other patterns,
extraction and challenge definitions unresolved. This is source approval,
not a mathematical attempt or proof audit.

### Primary inputs and specialization

Reuse `2026-10-10-triangle-twelve-recovery-bound.md` and
`2026-10-11-antipodal-triangle-bound-audit.md`, read for this comparison.
J. I. Hall, *Notes on Coding Theory*, undated author-hosted
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 and proof pp. 63–64 and interpolation discussion p. 65;
and I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and following shortening formula
pp. 7–8, already cover distinct labels, unit multipliers and the seven
shortenings producing Q. Allowing a nonantipodal W changes none of those
hypotheses. Standard Lagrange interpolation still has six distinct singleton
nodes. No reproof or new standard theorem import is needed.

P. Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026, was retrieved October 11. Inspected DR0–DR8/DRC,
lines 2785–2935, including complete proofs. DR2 assumes distinct weighted
Vandermonde columns, nonzero multipliers and t<R; R=8,t=4,multiplier x
remain applicable. DR6–DRC compile support-span membership into a union
of transverse slopes and a zero-fiber cardinality bound, without a bound
three. Their zero full-direction case concerns the full recurrence, not
L057's quotient both-zero lifts. Reuse the ready broader comparison:
fixed-core/circuit restrictions, structured designs and random-domain
hypotheses are not supplied, and the inspected proximity/list bounds do
not give this count. This mutable TeX is not certified identical to ePrint
2026/1463. Its web text search for `antipod` returned no match; this is
not evidence of novelty or a complete theorem search.

The hypotheses of audited L057 were read along with projected vectors (5),
restored coefficients (6), isolated and both-zero tests (7)–(10), weight
recovery (11) and original scalar map (12). Isolated disjoint-P rows force
normalized weights into F_97 while gamma_i, lambda and rho remain in F.
Zero recovered fourth weights remain allowed. L067's identities (1)–(3)
and subgroup scaling were read: their text explicitly proves them for
arbitrary pairs before imposing antipodality. Reuse only those audited
parts for arbitrary W. Its enumerated count and coverage instead choose W
from antipodal pairs, and cannot be imported into this enlarged count.
L066's read threshold statement requires four full isolated disjoint-P
anchors only if thirteen additional recoveries exist. It is a conditional
application after a future count, not an assumed existence or count.

### Search, overlaps and failures

New queries on October 11:

- `"Reed Solomon" "antipodal" syndrome recovery`
- `"mutual correlated agreement" "isolated" triangle`
- `"Reed-Solomon" "two" "antipodal pairs"`

Most hits concerned complex codes, antipodal signaling or unrelated topics.
No search snippet is used as a theorem. The author page
[*Pinning δ*: Machine-Checked Thresholds for Mutual Correlated Agreement
of Smooth Reed–Solomon Codes*](https://deltastar.computer/), accessed
October 11, section 3.1's full displayed hypotheses give a per-witness
subsingleton and witness-count upper bound under a far-direction condition.
This supplies no estimate three for simultaneous restored triangle fibers.
Sections 3.2–3.3 distinguish arithmetic kernel claims from finite incidence
computations and a monomial/windowed-budget setting; no identification with
this target is supplied. Linked code, proofs and the page's broader reduction
claims were not inspected or imported. The page has no pinned source version
in this review; it is a qualified inspected lead, not essential coverage.

Local duplicate check uses L057, L066 and L067 in their read scopes and the
ready assessments' L060–L065 comparisons. L064's fixed-support-pair bound
is not a bound on scalars at a weight point; its pending audit is not assumed.
L060–L063 are selected label assignments. L065 bounds both-zero recoveries,
not these isolated rows. No source overlap establishes the proposed count.
These are scoped comparisons, not certified originality.

ATTEMPTS/025 was read in full. Formal common-root conditions and the 256
assignment samples left arbitrary labels untested; more unstructured samples
remain an exhausted continuation. The new target specifies a complete
structured family and a falsifiable threshold. L067's actual three-scalar
fiber already prevents reuse of the historical sampled maximum two. A
four-scalar fiber would refute this intermediate three-bound only; preserve
it and reassess before any twelve-bound or global claim.

### Approved next attempt and decision test

Approve exactly TARGET for one RESEARCH calculation, using audited L057,
L067's arbitrary-pair evaluation/scaling parts only and audited L066's
conditional anchor requirement. L010/L065 enter through L066 and L041
through the audited inputs. No pending L060–L064 audit, arbitrary extraction,
ABF26 identification or cross-notebook input is a premise.

Seek complete maximum at most three over every allowed W, ordered shared
role and disjoint-P four-support, with scalar deduplication, restored weight
gates and zero fourth weights; or stop on a four-scalar fiber verified in
all eight original moments with every finite gate. Any relaxed four-scalar
row set still requires original-chart verification before refuting TARGET.
Partial samples, projected compatibility and producer summaries cannot
prove an upper bound. Do not silently apply a rational original chart or
transfer L067's restricted finite count. Both-zero lifts remain relevant to
the downstream L066 assembly. If complete coverage is infeasible, save the
specific unfinished coverage and do not promote its preview to a result.

Full and supporting Mathlib coverage remain not checked; no absence claim.
No lemma, mathematical script, DAG or PROOF.md is changed in this turn.
