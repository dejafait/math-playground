# L474: proposed critical-audit scope

TARGET: Review source coverage and audit scope for L474's uniform cubic small-displacement pair-mass bound, including multiplicity suppression, gamma normalization, combined pole cancellation and clipped endpoints.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact/stronger-result and duplicate searches in 2026-10-28-zero-conditioned-small-displacement-coverage.md and its source notes; read L474 in full, L018, L465 Sections 1--2, L471 definitions/conclusions and both nominated ATTEMPTS stops. Reopened primary finite-factor, microscopic-moment and sector-digamma passages for applicability; no renewed discovery search or novelty claim.
SOURCE_EVIDENCE: Broughan II (2017) Theorem 3.3 proof (1),(4), printed pp. 26--27, https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48; Bettin arXiv:1111.0925v1 Theorem 1 p. 2 and small-shift proof completion pp. 9--10, https://arxiv.org/pdf/1111.0925v1#page=2; NIST DLMF 5.11.2 and 5.11(ii), https://dlmf.nist.gov/5.11. Relevant statements/cases were read, not the full arithmetic or infinite-factorization proofs.
COMPARISON: Sources cover finite zero division with multiplicities, deterministic bounded microscopic shifts with a combined coincidence prescription, and sector-uniform gamma estimates. They do not supply L474's pair-divided aggregation. Source scope suffices to attempt its independent application audit; correctness of (1)--(12) remains unverified.
GAP: Independently replay L474's specialization, retaining common C,T_0 for every epsilon, arbitrary multiplicity/clustering, real normalization, pole cancellation, bounded overlap and clipped windows. No essential source access gap remains for this application audit.
REASON: The previously REVIEW_REQUIRED nomination now has a source-to-claim comparison and a bounded conceptual-audit scope. This approves coverage only; it neither performs the mathematical audit nor rejects the completed application.
LITERATURE_REASON: Essential separate coverage of L474's newly written application and its uniformity claims was missing; reuse discovery and known theorem assessments while checking this exact audit scope.

## Original nomination (before this source review)

The nominated literature-only turn was to reuse existing source notes wherever
adequate, inspect the actual applicability and audit scope, and prepare
one ready proof-audit assessment. No new estimate or complement target
is nominated here. Essential mathematical inputs are L018, L465 and
L471. The precise result to audit is L474 (1), with common C,T_0 for
all 0<epsilon<=1; its critical claims are (7), (9)--(12). Check that
removing one pair leaves the multiplicity suppression, that the area
normalization costs exactly TL^2, and that the chi remainder vanishes
with y before division by y. A repair or a precise failure is useful;
the full B(T) saving, individual signs and RH stay outside this scope.

No cross-notebook inputs. Full matching Mathlib coverage is unknown.

## Completed source comparison, 28 October 2026

The main gap is initial-sign control at unbounded heights and global
mixed positivity. The intermediate target is an independent audit of
the uniform cubic bound already written in L474. Its plausible use is
a reliable small-displacement component of L471's sufficient mass
criterion; complementary mass and individual-height signs remain open.

### Finite-factor scope

Broughan's cited proof explicitly repeats a zero according to its
multiplicity in (1) and treats a zero at the disk origin in (4).
Only the finite quotient bound is needed. L474 uses entire functions
on closed local disks, avoiding a boundary-regularity issue when
invoking maximum modulus. Its selected roots need not exhaust all
disk zeros. The source's unimodular factor convention is harmless for
bounds, but the exact quotient identity must use L474's convention.
The infinite-product passages are unnecessary and were not audited.
The later audit must check that an unremoved central zero is allowed,
and that removing one pair retains all other copies.

### Shifted-moment scope

Bettin Theorem 1 allows complex shifts with real parts O(1/log U),
error O((sqrt(U)+sqrt(|Im a|)+sqrt(|Im b|))log^2 U), and a combined
pointwise limiting interpretation when a=b. The small-imaginary-
difference completion uses W_1/W_2 and integration by parts; this is
the relevant proof case. L474 proposes real a=-y,b=y at U=T/2 and
3T, keeping shifts fixed across the two evaluations. This stays within
the assessed microscopic class. Zero-sampled shifts, derivatives of
the error and separate bounds on polar terms are not licensed. Audit
(5)--(7) as a specialization: check chi's convention and the remainder
anchored at y=0 before division by y. The full arithmetic proof stays
imported, not independently audited.

### Gamma and area scope

[DLMF 5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11)
give the digamma expansion and complex remainder control in closed
sectors avoiding the negative real axis. L465 Sections 1--2 record
the upper/lower branches and prefactors. The microscopic domains use
that covered technique; chain rules, signs, constants and common onset
still need replay. L471 fixes A only on the real axis: a holomorphic
extension of its modulus must not be assumed. The named submean
inequality for squared modulus is standard supporting coverage, not
a zero-selected disk-sum theorem. Finite overlap and the area cost
remain L474 application claims.

### Duplicate/failure comparison and decisive audit test

Reuse the earlier bounded search: no inspected theorem supplies the
exact summed quotient bound, and no novelty is certified. The stop in
`ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md`
loses displacement after replacing the quotient; the stop in
`ATTEMPTS/2026-10-28-paired-hardy-moment-discriminator.md` lacks actual
zero constraints. Neither precludes this retained finite-factor audit.
Unread adjacent discrete-moment papers are not dependencies.

Replay all of L474, especially (7), (9)--(12), with no extra logarithm
or epsilon-dependent constant. Check single-pair removal at repeated
roots, cluster suppression, all epsilon simultaneously, real A ratios,
disk margins, finite overlap and both clipped endpoints, including
singleton windows. Continue with the bound only if common C,T_0 and
the cubic scale survive. A failure requires repair or narrowing; an
irreparable failure parks this application with its evidence preserved.
No mathematical verdict is made in this literature-only step.

The ready continuation is recorded separately in
`2026-10-28-l474-uniform-cubic-proof-audit.md` for next-turn approval.
No lemma, script, DAG or proof assembly changed. Matching Mathlib
coverage remains unchecked, not established absent.
