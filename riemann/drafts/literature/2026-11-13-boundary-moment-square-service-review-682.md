# Boundary-moment square service — completed source comparison683

TARGET: Certify C998i's single-density moment evaluation and propagation to the unchanged three-column square, testing error<=1e-10 and total work<=20000000.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison683 searched certified logarithmic/oscillatory quadrature, Petras/ball integration, weight primitives and node setup; reused655/comparison656,658,670,675,679,681 and prescription stops652/657/660/662/672. Exact queries, inspected sources and unread leads are in drafts/literature/2026-11-13-boundary-moment-numerical-source-notes-683.md. No matching full fixed-data service or novelty conclusion.
SOURCE_EVIDENCE: Trefethen2013 Chapter19 Theorem19.3/(19.8), PDFpp153-154 https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf ; Johansson Sections2/2.1/3.2 https://arxiv.org/pdf/1802.07942v1 ; Arb2.23.0 callback/integration contract https://arblib.org/acb_calc.html ; DLMF25.12.1-4/principal branches https://dlmf.nist.gov/25.12#i ; pinned series/tail https://raw.githubusercontent.com/flintlib/arb/2.23.0/acb_hypgeom/dilog_zero_taylor.c and transformation branches1-4 https://raw.githubusercontent.com/flintlib/arb/2.23.0/acb_hypgeom/dilog_transform.c ; Johansson midpoint/radius arithmetic Section4 https://arxiv.org/pdf/1611.02831v1 ; Johansson-Mezzarobba Sections1-2 Proposition3/proof and recurrence(9) https://arxiv.org/pdf/1802.03948v1 . Reuse655/656 and source-notes683 for full inspected scope/qualifications; direct URLs retrieved684. C998i/audit682 remains the analytic input.
COMPARISON: Known bounded-holomorphic Gauss error and interval arithmetic cover a manually truncated, finitely prescribed one-variable moment method, subject to proved local domains/constants and counted primitive setup. Global SE/DE image-domain bounds are not established and those methods are not imported. Neither adaptive tolerance, asymptotic operation counts nor the analytic identities certify the requested service; stopped direct tensor counts do not transfer.
GAP: Quantitatively specialize ONE trimmed-endpoint/interior-Gauss moment prescription, including stable primitive/branch evaluation, all undotted/dotted data and W/V endpoints, every entry case, exact frozen neutral contraction, rounding and complete scalar setup/work. Error<=1e-10 and work<=20000000 remain entirely unproved.
REASON: Separate literature-only comparison683 removes essential source-coverage gaps without deriving a local bound. The identified difference is effective finite specialization of known methods; no general theorem needs reproof or inaccessible source is essential. A bounded REPRODUCTION feasibility attempt is ready, not a promised certificate.
LITERATURE_REASON: Quantitative moment evaluation and propagated error/work were expressly excluded by analytic assessment680; this completes the essential review required by the saved REVIEW_REQUIRED target.
SCOPE: Finite square service only, both parities and all products of the three unchanged frozen columns, C999q exact completion and C998g's coefficient1/4, using the method and obligations in source-notes683. No coefficient retuning, unassessed DE/Filon fallback, broader residual claim or signed-S3 inference. All future local specializations must be proved.

Direct-source repair684 (2026-11-13): the supervisor required a direct
source URL in a ready assessment. Source-notes683 already contained
these URLs, but this assessment's SOURCE_EVIDENCE field did not. The
eight URLs above were retrieved successfully; theorem19.3/(19.8), the
Arb cumulative-error warning, DLMF branch exclusions, the pinned series
tail/transform code and the node paper's Proposition3/Theorem1 passages
were checked against the existing notes. Theorem1 is asymptotic under
p~n, and is still not a concrete scalar-work certificate. Reuse the
already inspected proofs/cases in683; no new source method is imported.
TARGET, SPECIALIZE decision, method scope and all obligations are
unchanged. This is a source-locator/process repair, not new mathematical
coverage, an achieved bound or a renewed exploration budget. The next
invocation may assess the repaired gate; no mathematics is performed684.

Completed683: the text below preserves the original nomination's scope and
stopping evidence. Its requests for a separate numerical-method review
are discharged by source-notes683, not by a second analytic audit. The
unchanged TARGET is now source-ready for one mathematical attempt. No
new numerical prescription, bound, lemma or script was produced here.

The main gap remains L030-L032/C032a actual-Xi positivity and signed S3
remote-plus-induced coupling. This service could supply one necessary
component of the complete residual ledger. C998i's independent audit
is complete; another identity audit is not the proposed work.

The exact three-column square and work convention are in C998g's
hypotheses/conclusion. Error1e-10 refers to each complete square
contraction entry S_ij, not merely an unweighted B_nm entry or the
error of one moment. Work20000000 is total scalar work for this
service, including necessary setup and finite arithmetic; C998f's
separate diagonal reserve does not pay it. Preserve the free modes
and binary rationals in scripts/separation-seven/frozen-reference-proposal-652.npz
(SHA2562b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6).
The witness was not loaded or changed in682.

Essential inputs for later research are C998i(3)-(8)/audit682,
C998h/audit678, C998a(4)/audit655, C998g Section1/audit674, and C999q
for exact completion and contraction. Use C998e(6)-(8) only through
that audited C998g scope. The C999/audit650 and C999y/audit642 inverse
contracts, original C744v/w/z,C999k,C999z/audit646 contracts, and
C998f/audit669 remain separate; their upstream hypotheses are not
revalidated by the scalar square service.

For the separate review, reuse the inspected quadrature source where
its actual hypotheses suffice and retrieve any essential validated
arithmetic or oscillatory/singular-weight theorem before relying on
it. A smooth bounded-ellipse error formula alone does not settle the
zero-end logarithms or cancellation in A1,A2,Q near a. A library's
reported numerical precision is not a certified total error bound.
Do not infer an applicable method from a title, abstract or this
proposal. No particular quadrature, precision, degree or panel set
is approved here.

Bounded continuation test after coverage: specify one complete method,
propagate its rigorous moment and endpoint enclosures through ALL
terms of C998i(6)-(8), including lambda_n*dot H_n, both W/V endpoints
and all four diagonal residue classes, and then through the exact
frozen coefficient contraction with the prescribed normalizations.
Before a large evaluation, establish that the error and work ledger
can meet the two caps. Continue only with that evidence; stop the
prescription at an unpaid error source or an unavoidable cost over
the cap. No sweep, repeated tensor batch or unsupported speed claim
is justified. Analytic closure alone is not an evaluated entry.

Preserve652/657/660/662/672 prescription stops and673/675 source stops.
The new input is the audited independent moment representation, not
a changed name for a failed direct-node contraction. A-square, BOTH
mixed terms, projection, full100000000 work, residual/inverse debt,
signed S3, higher/mixed signs, C744q/H2, non-neutral and global Xi
assembly remain open even if the square service passes. Mathlib full
match is unchecked. No cross-notebook input is proposed.

No justified creative central sign target arose from this bounded
audit: a square representation does not bound the signed coupling.
This proposed numerical prerequisite is not labeled a creative
mechanism. It requires source coverage before any mathematical attempt.
