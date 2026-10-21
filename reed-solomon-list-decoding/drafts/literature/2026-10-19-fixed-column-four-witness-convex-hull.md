# Four frozen witnesses — bounded convex-hull source assessment

TARGET: Test whether the convex hull of the frozen L088,L090,L092,L094 moment witnesses at L086's columns meets all 81 original included-anchor mode inequalities, using exact barycentric feasibility or a rational separating row combination.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 349 searched active drafts/literature/2026-10-18* and 2026-10-19* plus ATTEMPTS/067–078 for convex-hull/barycentric overlap; read ATTEMPTS/067,068,071–078, canonical L088,L090,L092,L094 hypothesis/scaling and witness-location passages, L094 full-row formulas, and the supplied L095 audit assessment. External query: site.mit.edu convex hull nonnegative orthant Farkas lemma rational linear programming feasibility; retrieved the primary MIT sources below.
SOURCE_EVIDENCE: Freshly read Goemans, Lecture 3 (19 September 2001), MIT OCW Fall 2008, Theorems 1 and 3, printed pp.1–2, including Theorem 1 projection proof; MIT 6.854 2020 LP notes, standard-form conversion, Linear Equalities and Basic Feasible Solutions through tight-system reconstruction. Reuse inspected Schrijver/Sano/Polak coverage from the ready L095 assessment and foundations/10 polyhedral coverage.
COMPARISON: Finite rational LP alternatives cover the decision/certificate method; they do not decide the four notebook vectors. Canonical hypotheses specify identical frozen columns, coordinate order and raw scaling. Previous point rejections and capped unrestricted solves do not decide this restricted hull. No new general theorem or novelty claim is needed.
GAP: Essential source scope is ready; exact full-vector input binding, all 81 original/raw vertex remainders, barycentric feasibility or a strict rational separator, and independent certificate substitution remain mathematical work for a later turn. Ancestral matrix contracts remain conditional.
REASON: Approve exactly TARGET for a later RESEARCH / REPRODUCTION calculation; this separate literature comparison performs no hull calculation and changes no lemma or mathematical script.

LITERATURE_REASON: The saved continuation changes from critical audit of one assignment to mixing four frozen assignments. Target-specific finite-polyhedral comparison was missing; existing singular-matrix coverage is reused rather than reaudited.
SCOPE: Exactly the four frozen points at L086's columns; no free-moment solve, column variation, new witness outside their hull, full-plane/conic restart or broader separator search.

## Gap, use and stopping test

Main gap: arbitrary-center 67/68-agreement safety, with bracket 955–957.
Intermediate target: exactly TARGET. A passing mixture would preserve one
included-anchor candidate for further constraints; a strict separator would
park these four candidate directions together. Neither outcome is a uniform
bound over all moments or an RS realization.

Continue only with complete exact barycentric coordinates summing to one
and passing all original modes, or a complete rational nonnegative mode-row
combination strictly excluding every one of the four vertices. A verified
negative answer stops this hull only. Missing binding, range or residual
evidence makes the attempt inconclusive. Do not enlarge the hull, resume a
capped solve or reinterpret a failed search as infeasibility.

## Primary theorem comparison

Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September 2001,
scribes Abhinav Kumar and Nodari Sitchinava, distributed in MIT OCW Fall
2008, [primary PDF](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1 and 3, printed pp.1–2 (PDF pp.2–3). For finite real A,b,
Theorem 1 gives exactly one of Ax=b,x>=0 or A^T y>=0,b^T y<0;
Theorem 3 gives the free-variable inequality alternative. Read the full
projection argument through the strict negative conclusion and the
inequality variant statement. OCR corrupts some inequality signs and the
final y sign; the preceding definition and nonnegative-coordinate argument
fix the convention. Use the standard named Farkas lemma, not the corrupted
OCR. No strict feasibility hypothesis is required. The barycentric simplex
and nonnegative mode slacks admit this standard-form formulation; a general
semidefinite alternative is unnecessary. This source does not decide any
notebook coefficient or sign.

MIT 6.854, 2020 collection, [*Linear Programming* notes](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
sections Introduction, Linear Equalities and Basic Feasible Solutions,
through the tight-system reconstruction: read slack conversion, Cramer's
rule, the movement argument to a basic feasible solution and its rational
reconstruction. They support exact rational certificates for rational
finite systems. The collection mixes lecture years; no single lecture date
or theorem number is asserted. Do not import its informal general convex
separation or compactness claims. Rational input binding and direct
substitution, rather than floating solver status, remain essential.

Reuse Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748, [author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64).
Reuse Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, [27 February 2026 version of record](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7, including both singular
proof directions. Reuse Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 (1)–(3), Proposition 1.1 and indicator proof p.2, Section 1.2
p.3. These inspected inputs and qualifications are recorded in
`drafts/literature/2026-10-19-l095-fixed-witness-rejection-critical-audit.md`.
They justify the conditional mode framework, not the proposed hull verdict.
Fixed old PSD blocks and fixed cross vectors require whole-range checks;
then L094's displayed remainder is affine in the 45 free moments. Mixing
columns would change inverse costs and is outside this assessment. No
actual-label averaging, representing measure or free-entry completion
theorem is imported. No general theorem needs reproof.

## Input scope and duplicate/failure comparison

Essential input IDs: L021,L053,L073,L075,L076,L078,L082,L083,L086,
L088,L090,L092,L094,L095. L088,L090,L092,L094 Hypotheses explicitly use
the same L086 parameters, t78=L083's s, p8=16792471/1181138102168120460,
lexicographic (r,q) with 0<=r,q<=8,r+q>=8, and raw scaling
S=diag(p8/[C(8,r)C(60,r)C(8,q)C(948,q)]). This is a comparison of their
contracts; complete saved arrays have not been checked in this turn.

Bind complete `witness/z` and `witness/raw_moments` arrays in these
`scripts/finite-support/` artifacts before calculating:
- L088: `fixed-column-new-only-results.json`;
- L090: `fixed-column-zero-old-block-results.json`;
- L092: `zero-block-plus-3-4-results.json`;
- L094: `two-mixed-row-results.json`.

Retain 85 domain rows,90 kernel equations,500 types/3000 presentations,
36 forced entries,28 selected equalities,45 signs,81 original modes,
full anchor and whole singular ranges. Reconstruct shared rows in original
and raw coordinates and verify every vertex binding; do not assume L094's
extra mode controls hold at the other three vertices. If successful, check
the resulting full mixed vector directly against the original mode system.
If unsuccessful, a weighted row combination must have strictly negative
value at each vertex; weights must be nonnegative and all exact values
must be saved. This is the future certificate specification, not a
computed separator or a new lemma.

ATTEMPTS/067,068 stop the two particular numerical joint prescriptions;
ATTEMPTS/071 stops one capped unrestricted fixed-column Phase I without
an infeasibility verdict. The proposed four-vertex restriction is a
materially smaller independently testable LP, not another run of those
prescriptions. ATTEMPTS/072,074,076,077 retain necessary-subsystem
witnesses; ATTEMPTS/073,075,078 reject different complete assignments.
They do not establish common separation of the hull. Scoped searches found
no earlier hull test in these assessed recent records; this is not a
claim of novelty or an exhaustive notebook search.

The stronger free-entry completion route remains inapplicable because
shared union moments are not independently free entries, as compared in
the reused L095 assessment. New search hits on general convex analysis,
triangle algorithms and LMI certificates are unread leads, not imported
results; none is essential to this finite LP method.

Foundations/04,09,10,12 ancestral PSD,uniqueness,whole-kernel and
normalization remain conditional. Scalar upper rows,other anchors,
other columns/base/pairs,global moments,representing measures and RS
realization remain unresolved. Full matching and supporting Mathlib
coverage is not checked; unknown availability is not absence.

Step 349 is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED, actual
literature_comparison. It approves scope, establishes no finite hull
verdict, and uses no mathematical exploration turn. Next is the exact
approved calculation with REPRODUCTION classification.
