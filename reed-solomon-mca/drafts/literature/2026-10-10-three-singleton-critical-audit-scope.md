# Three-disjoint-singleton exclusion — completed audit coverage

TARGET: Critically audit L053's three-disjoint-singleton recovery exclusion, including label coverage, extension-field reduction and complete certificates.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed simultaneous-count discovery queries and inspected design/MCA comparisons; read complete L053, L043 hypotheses, criterion and audit, L010's kernel passage, both new programs' coverage loops, saved recurrence/polynomial extracts, ATTEMPTS/022–023 and history/118. No fresh external search or certificate replay.
SOURCE_EVIDENCE: Reused inspected Chojecki live author TeX v9.2 (July 17, 2026), lines 2785–2935, DR2/DR6–DRC with proofs and zero-direction cases; Hall Theorem 5.1.1, pp. 63–64; supporting Mathlib factor/root statements previously inspected on 2026-10-08. Precise references and applicability below.
COMPARISON: Known recurrence covers fixed-support full-moment membership and the polynomial results cover factor/root reasoning. Neither these nor the inspected design/MCA results supply the simultaneous fixed-H exclusion, certify its enumeration, or justify its renaming automatically; these remain critical-audit obligations.
GAP: Validate the five-value necessary reduction, extension-field passage, both singleton-tag renamings, all label/scalar cases and complete rejected-case evidence before treating L053 as audited.
REASON: Separate source comparison finds adequate essential ingredient coverage for one bounded REPRODUCTION proof/certificate audit of the exact TARGET; no mathematical correctness or originality is certified by this approval.
SCOPE: F_(97^20), fixed order-sixteen H in F_97^*, k=8, pinned cell; L010 and audited L043 (including L041–L042), three distinct same-singleton-tag nonuniversal candidates under every original triple and (4)–(7) gate, zero recovered weights allowed, arbitrary original finite chart. Audit L053 and both complete certificates/programs without L052 as a premise.
LITERATURE_REASON: L053's new label normalization, same-tag renaming and rejection-certificate coverage were not separately assessed as a critical-audit target by the earlier counting review; reuse adequate standard coverage rather than repeat browsing.

## Gap, intermediate target and downstream use

Uniform eleven for L043's relaxed nonuniversal candidates remains open
in the zero/one-d profiles; arbitrary-family extraction and challenge
definition are independent gaps. The intermediate target is exactly
the critical audit in TARGET. A successful audit would make L053's
conditional exclusion available for later simultaneous counting and
rule out the disjoint singleton-row shape motivating L052. It does
not exclude intersecting rows, force a two-d branch or improve the
global interval 11/q–16/q.

The startup assessment was REVIEW_REQUIRED. This literature-only step
approves its unchanged audit target separately from completed step 118.
The completed counting assessment remains unchanged in
`2026-10-08-nine-union-simultaneous-recovery-count.md`. No proof audit,
new derivation or certificate execution is performed in this turn.

## Reused primary results and specialization

Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[live author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026, source lines 2785–2935, anchors
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler`
(DR6–DRC). Reuse the complete hypothesis/proof-case extraction inspected
2026-10-08 in `2026-10-08-nine-union-fourth-support-incidence.md`,
“Primary recurrence input and applicability”, and the simultaneous-count
assessment. No fresh retrieval or identity with ePrint 2026/1463 is
claimed; this is a mutable author source.

For distinct weighted Vandermonde columns with nonzero multipliers,
redundancy R and support size t<R, span membership is equivalent to
the R-t locator recurrences. The inspected proof identifies the
annihilator with multiples of the support polynomial using MDS rank.
The compiler includes nonzero projected direction with a proportionality
pivot, zero direction with no intersection, and common-intersection
cases. Here R=8,t=4, eta_j=s_(j+1) for j=0,...,7 and the column
multiplier is x in H, hence nonzero. Arbitrary F-valued syndromes are
allowed. L043's audited missing-column equations (7), in addition to
its projected tests, are essential for full-moment membership before
the nonzero-weight gate (9). This unchanged specialization is covered;
no decoder or annihilator reproof is needed. The source does not state
L053's simultaneous three-recovery exclusion.

J. I. Hall, *Notes on Coding Theory*, undated
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
section 5.1, Theorem 5.1.1 and full proof, printed pp. 63–64, inspected
2026-10-05 and extracted in
`2026-10-05-two-block-moment-obstruction.md`, “Primary theorem and
applicability”. Distinct evaluation points, nonzero multipliers and
0<k<=n over any field give GRS dimension k and distance n-k+1.
n=16,k=8 and unit multipliers satisfy these hypotheses over F. The
inspected cases include injective evaluation, the root bound and
product attainment. L010's already proved moment kernel identifies
zero-moment words with degree-at-most-seven evaluations; the audit
uses that local input rather than repeating its proof. L041's shortened
setup is inherited through audited L043, so no new shortening theorem
or changed shortening hypotheses are required.

Reuse the primary polynomial inspection in
`2026-10-08-same-d-single-intersection-critical-audit.md`:
[Mathlib Div.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Div.lean#L566),
`Polynomial.mul_divByMonic_eq_iff_isRoot` and
`Polynomial.dvd_iff_isRoot`, statements/proofs at lines 566–576 under
`[CommRing R]`; and
[Mathlib Roots.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Roots.lean#L65),
`Polynomial.card_roots`, `Polynomial.card_roots'`,
`Polynomial.mem_roots`, `Polynomial.card_le_degree_of_subset_roots`,
lines 65–74, 98–99, 121–123 under `[CommRing R] [IsDomain R]`, retaining
nonzero-polynomial hypotheses. Previously inspected 2026-10-08 on mutable
master without a pinned commit or Lean compilation. F satisfies these
ring/domain hypotheses. They support factor/root arguments; checking
L053's nonzero polynomial, seven distinct roots and exact scalar factor
remains a proof-audit task. Full matching Mathlib coverage for L053 and
its finite exclusion is not checked; no absence claim is made.

## Known comparisons, duplicates and preserved failures

Reuse the discovery evidence and inspected primary comparisons in
`2026-10-08-nine-union-simultaneous-recovery-count.md`. Its actual
queries include `"Reed-Solomon" "syndrome" "simultaneous" support incidence`,
`"Reed-Solomon" "simultaneous recovery" support` and
`"Reed-Solomon" "eleven" "MCA"`; the disjoint-d audit assessment adds
`"split cubics" "evaluation" "disjoint" finite field`.
No fresh queries are claimed here. Guruswami–Kopparty, *Explicit
Subspace Designs*, March 2013 author manuscript, section 4.2 Theorem 14
and Claims 15–16, pp. 9–10, needs structured disjoint root blocks.
Goyal–Guruswami–Sun–Wootters, arXiv:2607.08516v1, Theorem 3.27(1)
needs an established design inequality; Theorem 5.6 uses random RS
evaluation points. Their inspected conclusions do not supply this
fixed-H relaxed recovery exclusion. No matching import was established
by the recorded bounded search, and search failure establishes no
novelty. Parked ABF26, campaign/ePrint and other unread leads remain
unread and are not essential premises for this conditional audit.

L043 certifies each support's recovery, not simultaneous counting.
L049's same-d ratio obstruction is related but is not the present
same-singleton-tag theorem or a direct input. L051's audited two-d
branch does not address this zero/one-d motivation. L016's saved-label
count does not cover arbitrary H-labelings. L052 supplies an abstract
motivation only. No new theorem is imported from any of these contrasts.

ATTEMPTS/022 stops summing isolated cubic degrees, which leaves room
for twelve. ATTEMPTS/023 stops support-only recentering, with its
canonical incidence survivor in L052. L053 couples actual complete
moment equations across supports and adds fixed-H root splitting;
the audit does not reopen either exhausted mechanism or derive further
couplings. History/118 preserves the completed result and its unaudited
qualification. No cross-notebook input is used.

## Ready bounded audit and decision test

L010 and audited L043 are the direct mathematical inputs; L041–L042
are included in L043's established scope. Read L053 in full and inspect
both `scripts/simultaneous-recovery/three_singleton.py` and
`scripts/simultaneous-recovery/verify_three_singleton.py` in full next
turn. The coverage loops were read for scope here, without certifying
their correctness. Check the following obligations independently:

- All eight moments must imply the claimed degree-seven polynomial;
  nonzero singleton coefficients and seven roots must justify its
  nonzero scalar factor. Check every cancellation and nonzero divisor
  in equations (1)–(3), allowing zero recovered weights.
- Validate the local prime-field passage of u,mu,r without descending
  the original chart, and the correspondence between distinct mu and
  distinct eligible finite parameters under L043 (4)–(5). E=0 and
  mu=0,-1 remain excluded in the actual hypothesis.
- Validate subgroup scaling by z_1^(-1), exchanging the two y labels,
  and the stated base-index interchange for z tags, including changes
  to p,q,r,lambda, the reciprocal scalar, all gates and original finite
  parameters. These are audit claims, not consequences certified here.
- Justify W=S exclusion and the four-member ratio threshold. Check all
  fifteen z values, every cubic membership, unordered disjoint triple,
  remaining W and ordered y_2,d choice. Dropping h,p,q,E and the remaining
  B-label restrictions must enlarge the actual family, never remove it.
- Replay producer then verifier, inspect the complete relevant evidence
  in `scripts/simultaneous-recovery/three-singleton-result.json` and
  `scripts/simultaneous-recovery/three-singleton-verification.json`, and
  check exact key sets, uniqueness, all retained/rejected cases and
  cross-multiplied equations. Reported targets are 5,460 memberships,
  704 triples, 28,688 cases (504 scalar rejections and 28,184 r rejections),
  no common gated r, and no failures. These are claims to audit, not
  independently verified outcomes of this literature turn. The unused
  witness branch supplies no premise; a preview or zero counter is
  insufficient evidence.

Coverage passes: no essential new source or changed standard hypothesis
is missing. The next invocation may perform one REPRODUCTION proof_audit
under this EXPLORE assessment. Continue using L053 as an audited input
only if the reductions, renamings, original-chart qualifications and full
certificate coverage survive. A missing case, bad denominator, failed
record or unjustified extension-field passage blocks the affected claim;
repair or qualify it while preserving the proof and certificates.
A surviving relaxed configuration defeats this necessary-condition
certificate, not the eleven bound or MCA challenge, and still needs
the dropped actual gates before it becomes an actual witness.

Full L044–L046, L040, a finite universal lift, rational original
parameters, twelve-count completion, universal extraction and ABF26
identification remain unassumed. Intersecting singleton rows and other
tag profiles remain open even after a clean audit. Mathematical
exploration usage stays zero after step 118. This completed turn is
EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: useful scope approval,
with no new mathematical input or certification of L053.
