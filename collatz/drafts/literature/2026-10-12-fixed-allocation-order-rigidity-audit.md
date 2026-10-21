# Fixed allocation order rigidity: approved separate critical-audit scope

TARGET: Critically audit L063's all-order J-guard rigidity for L055's fixed allocation, including uniform cyclic-root bounds and complete first-displacement coverage.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the seven queries and inspected theorem comparison in 2026-10-12-fixed-allocation-j-guard-order-rigidity.md; read Attempts 027–031 and histories 178–179, L063's complete proof, and relevant L051/L055/L062 source and audit passages; no new external search or independent L063 audit is claimed.
SOURCE_EVIDENCE: Reused Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemmas 1/2 pp. 228–229 and inspected ordering comparisons; NIST DLMF 1.2.8 equation 4.6.4; read L055's canonical rational-log/remainder and independent-audit passages and L062's exponential-bound/audit passages.
COMPARISON: Inspected affine composition and logarithm sources cover the machinery; scalar ordering results do not certify L063's order-uniform root bound, shifted-offset sign, own-index guards or complete first-displacement coverage, which require independent local verification.
GAP: The critical audit remains unperformed: independently check the full L063 statement, every essential specialization and numerical input, literal existence and all required margins; source access and coverage do not verify them.
REASON: Separate literature-only approval now permits one RESEARCH/REPRODUCTION critical audit of the unchanged TARGET using existing coverage; no new mathematical result, broader target or source finding is asserted.
SCOPE: Audit L063 exactly for L055's fixed intact allocation, permutations of rows 0–23 with row 24 fixed last, L051's non-strict J guards and all 25 cyclic endpoints, including every subsidiary root/minimum/rotation claim; do not assemble downstream integer exclusion or extend allocations.
LITERATURE_REASON: L063's new critical-audit continuation was REVIEW_REQUIRED; compare its essential inputs and audit obligations once using ready sources rather than repeating theorem discovery.

Essential inputs: L051 (3)–(4); L055's intact table, counts, literal
existence and audited Lambda/logarithm bounds; L062's exact exponential
bounds; the new proof and full certificate of L063. No cross-notebook
input is needed. The original approved target remains recorded unchanged
in `2026-10-12-fixed-allocation-j-guard-order-rigidity.md`.

Proposed audit must check that arbitrary suffixes affect only the root,
whose bound is genuinely order-uniform; the final large tail remains in
closure but never in a growing prefix; and the exact shifted offset is
negative on all eligible rows. Check first displacement k<=22 and j>k,
the increasing J sequence, all 23 minimum margins and coverage of all 276
pairs, including the non-strict guard sign and own-index input pairing.
Recompute finite arithmetic independently instead of accepting saved flags.
Check L055's literal witness meets the exact subsystem and that the new
canonical DAG contains precisely the mathematical inputs actually used.

Acceptance requires no unresolved essential defect; a gap requires a
specific correction or qualification. Main gap remains universal eventual
descent. Potential later use of L056's nonintegrality is outside this
audit target. H/seed conditions are omitted from the uniqueness premise,
though the literal witness satisfies them; integer/parity/exact-tail and
primitive realization, different allocations, unrestricted cycles and
divergence remain unresolved. Existing published and unchecked Mathlib/build
qualifications persist. This audit is not a complete Collatz-candidate review.

## Separate source-to-audit approval — 2026-10-12

The preceding proposal records the scope supplied for this turn. This
section approves that unchanged scope, without performing the audit.
Read the prior all-order assessment in full, L063's complete proof,
L051's hypotheses (1)–(4), L055's literal table, cyclic construction,
root and own-index guard arguments, its rational-logarithm proof and
independent-audit passages, and L062's root/exponential arguments and
independent audit. Reuse the primary inspection and exact-target check
recorded in the prior assessment and the ready permuted-real-guard
assessments. No essential source is inaccessible. No new theorem search,
mathematical computation, lemma or mathematical-script write occurred.

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemmas 1/2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
is the reused primary affine input. The saved inspection records the
odd-denominator domain, nonempty binary word, one-letter case,
last-bit-zero induction and source's stated analogous last-bit-one case.
For length l and k one-bits, the formal composition and fixed-point
formula use the denominator 2^l-3^k. The proposed audit needs only formal
composition with l=N and k=K, not parity realization on arbitrary real
junctions. L063's coordinate specialization must still be checked against
L051 (4), including the 23/11 shift and both affine corrections. Known
composition alone does not certify its inequalities. Rechecking this
local match is necessary verification, not a reproof of general coding.

The prior comparison also inspected Halbeisen–Hungerbuehler Lemmas 3–5
and Corollary 1, pp. 229–231, including the prefix-domination and rotation
proof cases, and Kawase–Makino–Seimi,
[*Optimal Composition Ordering Problems for Piecewise Linear Functions*,
arXiv:1601.05480v1](https://arxiv.org/pdf/1601.05480v1), Theorem 1,
Definition 7, Lemmas 9/10/14(b), pp. 3, 6–8, 16. Equal word totals do
not supply the former's prefix-domination hypothesis; the latter's
nonnegative-slope, prescribed-input optimization is a scalar objective.
Neither supplies simultaneous own-index guard feasibility or its
uniqueness. These are inspected comparisons, not essential theorem
inputs to the audit. No additional ordering theorem is needed to review
the finite specialization already written in L063.

[NIST DLMF equation 4.6.4](https://dlmf.nist.gov/4.6.E4), version 1.2.8
(release 2026-09-15 as recorded in the reused inspection), supplies the
odd-power logarithm expansion on Re(z)>=0, z!=0. The positive real
arguments meet that domain. L055 gives the canonical finite-term,
integrated-remainder and rounding justification, followed by an
independent rational audit. L062 records and independently audits the
41-term positive exponential lower bound and the coarse exp(2) bound.
Those precise local inputs are available. Their reuse requires verifying
the fixed counts, source provenance and signs; a series citation alone
does not certify an enclosure or a finite comparison. No fresh enclosure
or exponential sum was evaluated in this review.

L051 defines the J guard and endpoint subsystem. Its actual-cycle
bridge has inherited published computational, continued-fraction and
Rhin/Crandall qualifications. No primitive-count theorem is necessary for
this fixed real-subsystem audit, and none may be imposed on real junctions
as an established integer-cycle fact. H guards and the seed are outside
the uniqueness premise; the literal existence input is L055's audited
stronger witness. Full matching Mathlib coverage and external Lean builds
remain unchecked; supporting log/exp facts do not prove this allocation's
all-order statement. Unknown coverage is not evidence of absence.

The narrow duplicate/failure check found L063's new argument and pending
audit, L055's audited literal witness, L062's audited single-order failure,
and Attempts 027–031. The modular stops do not supply rigidity; the
single-order guard failure does not supply an arbitrary-suffix bound.
Preserve all of them. The earlier seven-query comparison is adequate
because this audit changes no allocation, mathematical hypothesis or
essential technique. No new originality conclusion is justified.

The full certificate path in L063 is accessible. Its `/summary` was
inspected only as a labeled structural preview; that is not proof of
coverage, positivity or correctness. No generator was run and no saved
success flag was accepted as independently verified evidence.

SPECIALIZE approves exactly one following RESEARCH/REPRODUCTION proof
audit of TARGET. Essential inputs are L051 (3)–(4), L055's intact table,
counts, literal existence and audited Lambda/log intervals, L062's exact
exponential bounds, and L063's full written argument and certificate.
Audit all subsidiary conclusions as well as the rigidity verdict:
endpoint uniqueness and positivity; genuinely uniform bounds for any
suffix; the full closing tail and its exclusion from growing prefixes;
negative shifted offsets on eligible rows; all first-displacement cases,
strict/non-strict directions, all 23 weakest margins and all 276 pair
operands with their own-index pairing; and cyclic relabeling. Independently
recompute finite arithmetic from the canonical table and inspect complete
load-bearing values. Check the DAG's direct input uses mathematically.

Retain critical verification only if there is no unresolved essential
defect and every stated bound is justified. An erroneous bound, omitted
case or nonpositive required margin demands a concrete correction or
qualification; failure of a sufficient comparison alone does not refute
rigidity or Collatz. L056's potential integer-exclusion assembly remains
outside TARGET. Integer/parity/exact-tail/primitive realization, different
allocations and all universal gaps remain unresolved. No cross-notebook
input is needed and no complete candidate exists.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome STALLED: this is required
scope approval by source reuse, with no new theorem finding or mathematical
evidence. The audit is now actionable, not completed. This literature
step spends no mathematical exploration budget and does not reset it.
