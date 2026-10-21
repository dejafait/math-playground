# Conductor-36 full generator recovery — completed source comparison

TARGET: Construct and independently verify the complete Neron-normalized real modular-symbol table on a full integral Manin generating set for E=[0,0,0,0,1] at N=36 using clearing integer 24 and arbitrary-cusp enclosures.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: BSD-175 searched exact 36a1 modular-symbol and complete numerical Manin-table terminology; inspected primary Section 6 and Theorem 13 of Wuthrich v2, Stein's presentation statement/proof cases and the official Sage numerical-Manin contract; scoped local comparison found only the fixed path and structural N=1,15 certificates, not a completed N=36 table.
SOURCE_EVIDENCE: Reuse inspected Stein (2007) equation (3.2.1), Propositions 3.10--3.11/Theorem 3.13 pp.40,42--44 and Cremona (1997) Propositions 2.2.1--2.2.3 pp.15--17; audited L038/L049/L050/L051/L052 and their assessments. Newly read Wuthrich arXiv:1608.06423v2 Section 6 (12), Section 6.1's nonunitary example and Section 6.2 opening hypotheses pp.13--14, plus Section 8.5/Theorem 13 with proof pp.21--22; official Sage numerical-symbol Algorithm, normalization note and manin_symbol contract accessed 2026-10-12. Exact citations and qualifications below.
COMPARISON: Complete numerical Manin evaluation is known; Theorem 13's semistability/Goldfeld hypotheses exclude its complexity bound here. The reusable arbitrary-cusp method and fixed all-cusp integer cover the proposed mathematical domain; the missing difference is exhaustive N=36 implementation evidence, not a new recovery theorem.
GAP: Produce and independently replay every integral generator's analytic containment and 24-scaled integer isolation, including zeros, with the complete saturated presentation and every relation; neither the fixed-path programs nor source return values supply this local certificate.
REASON: Separate comparison now approves the unchanged saved target for one subsequent RESEARCH/REPRODUCTION implementation attempt. Citations supply the algorithms, not the actual finite witnesses; no table, new lemma or mathematical script is produced in this literature turn.
LITERATURE_REASON: The start target was REVIEW_REQUIRED because combined full-generator execution was outside the single-path and mandatory N=1,15 implementation scopes; reusable theorem coverage is compared rather than re-browsed unchanged.
SCOPE: Only the supplied minimal E=[0,0,0,0,1], N=36, weight two/trivial character, total minimal real period, all original integral Manin generators modulo all torsion; both endpoint orientations, infinity, nonunitary cusps and zeros included. No Hecke-line production, complexity claim, coefficient or non-CM application.

## Reused primary coverage and applicability

The prior proposal required separate review; BSD-175 completes that review
without performing its proposed calculation. The main gap remains rational
rank equals complex order for arbitrary analytic order at least two. The
intermediate target is the exact TARGET above. Its plausible use is a
complete nonsquarefree-level normalization benchmark for the full-relative
recovery machinery, rather than another conditional denominator audit.

For the full integral domain, reuse
`drafts/2026-10-08-general-relative-construction-source-notes.md` and
`drafts/literature/2026-10-09-general-relative-certificate-implementation.md`.
[Stein, *Modular Forms, a Computational Approach*, GSM 79 (2007),
equation (3.2.1), Propositions 3.10--3.11 and Theorem 3.13,
pp.40,42--44](https://wstein.org/books/modform/stein-modform.pdf),
gives integral relative generation and all relations followed by removal
of torsion. The newly inspected [online v0.1 Theorem 3.13 and its
proof](https://wstein.org/books/modform/modform/weight_two.html) explicitly
retain that torsion quotient and both relation cases. Injectivity is
imported from the stated theorem; Manin's original Section 1.7 remains
unread and is not an extra premise. Composite-level cosets and coprime
lifts use [Cremona, corrected second edition (1997), Propositions
2.2.1--2.2.2, pp.15--16](https://johncremona.github.io/book/fulltext/chapter2.pdf).
L038's exact normal-form and coordinate witnesses are reused unchanged.
Its structural hypotheses allow positive composite N, with no elliptic
curve restriction. Its later non-CM eigenline application is not used.
The existing builder permits an empty supplied good-prime list; no
operator or eigenline calculation is needed to recover this table.

For analytic containment and zeros, reuse the completed assessment
`drafts/literature/2026-10-11-arbitrary-relative-exact-recovery.md` and
its separate audit assessment, not merely their headers. Inspected L049's
full construction through exact isolation: both endpoints, all transport
terms, positive-height evaluation, complete tails, independently refined
minimal-target periods and division across zero are within its scope.
Its precise inputs are Wuthrich v2 equation (2), Lemma 4 with proof and
Section 5.1 (11), pp.6--7,11--12; Cremona Proposition 2.2.3 with proof,
(2.4.1)/(2.9.1) and arbitrary-cusp remark, pp.16--19,31--32; Cremona
Section 3.7 (3.7.1), pp.97--98; and DLMF 19.8.1--19.8.5.
L049 already handles CM, additive reduction and integral sums, with exact
coefficients and complete generating paths supplied. L038 supplies the
paths; L050 supplies this model's arithmetic and the coefficient method.
Use the audited oriented closing formula, preserving the recorded suspect
source-display sign qualification. No new sign reproof is requested.

L052's conclusion explicitly gives K=24 on **every** rational-cusp path,
although its finite analytic recovery was for one path. Reuse its audited
specialization of [Cai--Chen--Liu, Trans. AMS 370 (2018), Section 3
opening, p.3732](https://archive.ymsc.tsinghua.edu.cn/pacm_download/632/12220-Heegner_points_on_modular_curves.pdf#page=12),
[Cesnavicius--Neururer--Saha, author PDF 2022-01-28, Theorems 1.2/7.2,
pp.3,45--46](https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf),
and Wuthrich Proposition 1's complete cusp-torsion proof pp.3--4.
No hypothesis changes: degree-one origin-preserving identification,
exact conductor 36, cube-free differential theorem, good split reductions
at 7 and 13, and total real-lattice projection all remain as audited.
Both endpoints are covered, independently of their being unitary or the
integral being zero. The clearing integer is an existence input before
rounding; no table value is inferred from a database or from -1/12.

## New comparison, existing implementations and exclusions

Queries were `"36a1" "modular symbols"`, `"modular symbols" "Manin"
"rigorous" numerical all cusps`, and `site:doc.sagemath.org "mod_sym_num"
denominator error non-unitary`. Search results are discovery only.
Inspected [Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423v2, 23 March 2017](https://arxiv.org/pdf/1608.06423v2),
Section 6 (12), Section 6.1's example and Section 6.2's opening
hypotheses pp.13--14: its Manin orientation
is from the transformed infinity endpoint to the transformed zero
endpoint, opposite Stein's generators. The unitary direct method assumes
unitary endpoint denominators; Section 6.1 even records an N=36 example
requiring nonunitary intermediate cusps. Do not replace arbitrary-cusp
coverage by that shortcut. Section 8.5/Theorem 13 pp.21--22 is about
complete evaluation, under semistability and Goldfeld's period conjecture.
Its statement and both short/long-coordinate proof branches were read.
Neither this complexity theorem nor the remark removing the period
conjecture removes semistability; no complexity bound is imported here.
These source results establish substantial algorithmic overlap, not a
new algorithm or a new theorem from the planned table.

The [official Sage numerical-symbol manual](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html),
accessed 2026-10-12, documents `manin_symbol(u,v,sign)` on projective
pairs, rational outputs, exact algebraic and numerical methods, and its
Manin-constant qualification outside Cremona's tables. Its normalization
uses the least positive real period and its infinity-based primitive.
This provides an existing evaluation facility, not the requested complete
independent finite certificate. Any optional comparison must first check
orientation and total-period conventions; unadjusted equality is not a
test. No source-code internals or current Sage installation were tested.

Scoped duplicate/failure checks covered the cited assessments,
`history/174-2026-10-12-nonunitary-exact-recovery-critical-audit.md`,
the fixed reduced-phase/recovery attempt notes, ATTEMPTS/025, and the
builder/verifier in `scripts/general-relative/` and
`scripts/nonunitary-cusp/`. The reduced-phase producer consumes a
single-path certificate; its verifier fixes r=1/6 and 38 transports.
The recovery producer likewise fixes that path. Their audited runs do
not certify another endpoint list. The general-relative programs accept
N as input, but the inspected completed instances are N=1,15. No full
N=36 table was found in these scoped paths; this is not a global absence
or novelty claim. ATTEMPTS/025's complex-power rectangle failure remains
preserved. Use independent reduced phases and positive attenuation,
checking actual widths; the old fixed 96-bit schedule is not a guarantee
for new points. L049 permits precision refinement; no generic reduced-
phase software correctness or runtime theorem is presumed.

## Approved finite evidence and continuation test

Import the named results and audited local inputs rather than reprove
presentation, cusp torsion, differential scale or period identities.
The permitted difference is executable assembly and full finite replay.
Save new outputs separately and preserve every previous certificate,
failure and unfinished derivation. Before lengthy computation checkpoint
the complete required endpoint list and any incomplete verification.

Require the complete L038 presentation: every primitive-pair/unit orbit,
coprime lift, both relation rows per generator, integer normal-form
transforms and inverses, entire diagonal/zero tail, saturated relation
basis, quotient section, every integral-generator coordinate and all
decomposition identities. Do not substitute a rational basis or discard
boundary directions. The existing structural checker must reconstruct
the whole domain at N=36; its previous instance results are insufficient.

For every original generator g_i{0,infinity}, retain both actual endpoints
and its own certified real integral interval (shared certified primitives
may be cached). Reconstruct all finite cusp closings and every required
transport matrix and positive-height point. Use L049's eligible good-prime
selection, coprime to all selected denominators; 37 is not automatically
eligible outside the old list. The already covered tau=i choice is
available; an optimized choice must satisfy the existing transportation
and enclosure hypotheses, checked explicitly rather than assumed from
the fixed-path replay. Retain all Fourier coefficients/recurrences and
counts through the largest required truncation, all reduced phases,
attenuation values, finite terms, tail bounds and outward operations.
Fixed polynomial degrees or precision may only be used with their
verified argument/remainder bounds and the actual resulting widths.

Replay the positive total minimal period, signed endpoint differences
and all four division endpoints. For each normalized interval J_i,
verify ceil(24 inf J_i)=floor(24 sup J_i)=m_i, then reduce m_i/24
exactly. This is L049's existing test with L052's integer; zero receives
the same containment and integer-isolation test, with denominator one.
An interval without an integer, with multiple integers, or without full
containment is a failure, not a rounded result. Refinement is permitted,
but no unverified 96-bit or truncation limit is a success criterion.

Check the exact recovered table against every source relation and every
saturated-kernel column, and against all quotient-coordinate reconstruction
identities from L038. Compute its reduced-denominator lcm from all entries.
Relation agreement supplements independent analytic containment; it
cannot replace it. The separate verifier must not import the producer,
trust its success flags, or skip malformed shapes, zero entries or unused
data. Reconstruct domain completeness before comparing recorded values.
Retain full certificates and failure reports, and print bounded actual/
required counts, isolation widths, failure totals and relative paths.

Continue only on complete zero-failure structural, analytic, integer and
relation replay for every original integral generator. A missing endpoint,
failed source hypothesis, ambiguous integer or omitted relation requires
specific repair; repeated unproductive implementation failures require
reassessment under the shared rules. Finite success would still need a
later separate critical audit. Do not broaden this approval to new curves,
an eigenline, complex-valued tables, coefficients or new analytic methods.

Independent unresolved steps are uniform production, nonzero useful
coefficients, rational directions, Sha defects and complex-order/rank
comparison. This CM benchmark cannot activate L027's non-CM premise.
No BSD candidate or mathematical value is produced by this review.
Full matching and supporting Mathlib coverage remains not checked,
as in L038/L049/L052; unknown coverage is not an absence claim.
