# Signed finite-divisor remainder — completed bounded source discovery

TARGET: Review signed Cauchy–Binet remainders after a finite verified Xi-zero divisor for one independently testable estimate toward unbounded-order coefficient positivity, without assuming residual PF_infinity.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step667 searched signed Cauchy–Binet remainders, PF factorization, quantitative Toeplitz perturbations, meromorphic Toeplitz asymptotics and exact reciprocal-Xi fixed-shift statements; compared L832/L833, L825, step659 and the ready hybrid/duality assessments. Queries, actual readings, overlap and access limitations appear below. No novelty inference is made.
SOURCE_EVIDENCE: Reuse inspected Pinkus Section1.1 pp.2–3 and Katkova Definition2/Theorem B/product passage; newly read Katkova math/0505174v1 Definition3/Theorems2–3 and reduction pp.4,6–9; Böttcher–Widom math/0604009v1 hypotheses/Theorems1.3–1.4 pp.1–3, Corollary2.3/proof p.4 and Section6 pp.9–10; Flajolet–Sedgewick ALCOMFT-TR-03-100 (27 November2003), TheoremIV.7 and both proofs pp.29–30; Platt–Trudgian 2004.09765v1 Theorem1/Section2 pp.2–3. Exact links and applicability follow.
COMPARISON: No inspected result supplies signed residual-minor domination at growing order after the finite divisor. Fixed-order shifted positivity and fixed-winding additive asymptotics have different quantifiers. Reciprocal duality plus a finite principal-part expansion supports a different fixed-shift, unbounded-rank test; an indexed fifteen-shift exposition overlaps that method but its theorem/certificate packet was not inspected or imported.
GAP: The original mechanism still lacks an actual signed residual-minor estimate relative to a positive term, uniformly in the desired growing order. The alternative must separately establish pole isolation/simplicity, leading determinant sign and relative matrix-error control. No such Xi inequality is proved in this literature turn.
REASON: One bounded review identifies a testable alternative and limits the original mechanism; neither a failed search nor the finite floor pays its signed remainder. Park direct signed-composition work pending a materially new estimate; nominate the independently sourced fixed-shift specialization for separate approval.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED scope changes nonnegative fixed-order composition to signed unbounded-order remainders. Existing finite-floor, hybrid and duality coverage is reused; newly needed asymptotic hypotheses and pole-expansion coverage are inspected once.
SCOPE: Literature-only discovery. No new lemma, mathematical script, determinant calculation, expansion specialization, zero-simplicity deduction or new sign theorem. The separate next assessment is a newly written ready nomination, not permission to execute mathematics in this turn.

## Question, relevance and stopping test

The main gap is actual-Xi all-degree mixed positivity. The reviewed
intermediate target was an independently checkable signed remainder after
removing a finite verified negative-real-zero divisor. It could potentially
extend signs beyond a fixed PF order. Continue that mechanism only with an
actual estimate, its order range, normalization and required relative
threshold. An exact expansion without such an estimate is insufficient.
Independent all-order signs, hybrid conditioning/reference sign and RH remain
open even if a bounded intermediate target succeeds.

L833's finite floor is audited, but its Cauchy–Binet summands are nonnegative
because the residual itself is PF6001. The proof does not estimate negative
summands at higher order. L832 likewise controls the minor order, not all
orders. The step659 record in
`ATTEMPTS/2026-11-05-first-hybrid-corner-unpaid-ratio.md` requires a paid
comparison of its determinant and cofactor; the new floor supplies neither.
The audited L825 obstruction excludes only its specified common Appell
symbol, not the pole mechanism considered here. No cross-notebook input.

Reused assessments: `2026-11-05-verified-divisor-minor-margin-scope.md`,
`2026-11-05-hybrid-saddle-determinant-stability-scope.md`, and
`2026-11-05-reciprocal-minor-duality-comparison.md` in this directory.
The reciprocal algebra stop in
`ATTEMPTS/2026-11-05-reciprocal-determinant-independent-sign-stop.md`
remains valid: duality alone is not an independent sign estimate. The
local-factor countermodel in the corresponding `reciprocal-local-premise-
index-stop.md` remains an obstruction to automatic index transfer.

## Inspected primary sources and their limits

1. Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
   [math/0505174v1](https://arxiv.org/pdf/math/0505174v1), Definition3
   p.4, Theorems2–3 p.6, and the reduction through TheoremD pp.7–9.
   APF_m concerns a shifted matrix with m rows; Theorem2 fixes m before
   its eventual threshold. Theorem3 fixes m before a smoothing parameter
   n0(m), using exp(nz) or cosh(n sqrt(z)). Neither statement provides
   unbounded-order positivity of a fixed deflated Xi series. Read the
   reduction's consecutive-minor integrals and quantifier passage; the
   later saddle estimates were not needed or newly audited. The prior
   TheoremB/product reading remains adequate for L832/L833.

2. A. Böttcher and H. Widom, *Szegő via Jacobi*,
   [math/0604009v1](https://arxiv.org/pdf/math/0604009v1), 1 April2006.
   Theorems1.3–1.4, pp.2–3, assume a nonvanishing circle symbol of zero
   winding in C^beta, beta>1/2, beta nonintegral, and fixed positive
   winding displacement kappa; the exact formula also requires the stated
   finite-section invertibility. Theorem1.4 has an additive O(n^(-3beta))
   error inside a fixed-size determinant comparison, not a relative
   lower bound for that determinant. Section6, pp.9–10, controls Hankel
   tails by polynomial approximation with kappa fixed. It supplies no
   simultaneous kappa/n estimate or actual hybrid conditioning.
   Reused Theorem2.1 and reread Corollary2.3/full proof p.4 give finite
   complementary minors; only the full matrix must be invertible, not
   either selected minor. This algebraic input can be used without an
   asymptotic sign assertion. General nonzero-winding asymptotics are
   therefore not imported as a solution of the signed-tail question.

3. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics —
   Basic Complex Asymptotics*, ALCOMFT-TR-03-100, first edition,
   27 November2003,
   [author PDF](https://algo.inria.fr/flajolet/Publications/FlSe03.pdf),
   TheoremIV.7, (22), and both proofs, printed pp.29–30 (PDF pp.37–38).
   A function meromorphic on a neighborhood of a closed disk, analytic
   at zero and on its boundary, has coefficient expansion as a finite
   sum of pole contributions plus O(R^(-n)). Each pole contributes a
   polynomial in n of degree its multiplicity minus one. The proof
   subtracts every principal part, then applies Cauchy's coefficient
   bound to the analytic remainder; the contour proof retains all
   crossed residues. This is an entry-level estimate, not a determinant
   relative-error theorem. Simplicity and a separating contour must be
   checked before replacing pole contributions by single exponentials.
   This precise source version uses IV.7; IV.10 in the later 2009 book
   was a search lead, not an inspected theorem in this turn. The full
   2009 PDF exceeded the retrieval size limit. No theorem is reproved.

4. Platt–Trudgian,
   [2004.09765v1](https://arxiv.org/pdf/2004.09765v1), Theorem1 p.2
   and Section2 pp.2–3, supply the verified height/count already used
   in L832/L833. Section2 counts distinct sign changes and checks the
   total by Turing's method. A later application needing simple poles
   must explicitly justify its use of this evidence; the RH statement
   alone does not assert simplicity. A disk separation must also compare
   the squared images of every possible off-line higher zero, not just
   list the first critical-line ordinates. Neither check is performed
   as a mathematical deduction here.

Pinkus, *Totally Positive Matrices* (2010), Section1.1 pp.2–3,
[publisher excerpt](https://assets.cambridge.org/97805211/94082/excerpt/9780521194082_excerpt.pdf),
is reused for finite Cauchy–Binet. Current fetch503 does not invalidate
its already-inspected finite identity; no new conclusion depends on access.
Full matching Mathlib coverage is not checked; no absence claim is made.

## Discovery evidence, overlap and blocked leads

Searches included `"Cauchy Binet" "signed" "Riemann"`,
`"Cauchy-Binet" "remainder" "total positivity"`,
`"Pólya frequency" "remainder" "zeros" Riemann`,
`"Toeplitz" "minors" "perturbation" total positivity bounds`,
`"Toeplitz determinants" "meromorphic" "poles" asymptotics Widom`,
`"xi" "Toeplitz" "fixed" "zeros" reciprocal coefficients`, and
`"Riemann" "6002" "Toeplitz"`. Narrow local searches found the named
hybrid and reciprocal stops, not a completed fixed-shift pole estimate.
This establishes no originality.

Bultheel, *The asymptotic behavior of Toeplitz determinants generated by
the Laurent coefficients of a meromorphic function*, SIAM J. Algebraic
Discrete Methods6 (1985),624–635,
[author PDF](https://nalag.cs.kuleuven.be/papers/ade/astoep/paper.pdf),
DOI10.1137/0606061, initially returned OCR of the hypotheses and first
results. Formula/proof follow-ups and screenshots repeatedly timed out;
a shell download also failed DNS. Ambiguous formulas and the essential
proof were not read. It is an unread stronger lead, not an import. Do not
repeat that access route. The independent finite-duality and meromorphic
coefficient sources above suffice for the narrower next test without it.

The indexed July22,2026 exposition
[The first fifteen Xi-coefficient shifts are nonnegative at every Toeplitz rank](https://kenan.works/posts/fifteen-shifts-of-xi/)
describes fixed-shift reciprocal poles, a Vandermonde leading matrix and a
relative inverse-error test, explicitly without growing-shift control.
Direct reads with and without the trailing slash returned502. The search
service exposed the exposition, but no underlying theorem/certificate packet
was inspected. Treat this as overlap evidence for the method, not a verified
actual-Xi theorem or a substitute for primary proof coverage. In particular
none of its numerical thresholds or all-rank signs is imported here.

## Decision and separate continuation

The direct signed Cauchy–Binet remainder mechanism is parked: no supported
actual bound uniform in its growing order was found. This is a limitation
of the inspected sources, not a mathematical impossibility theorem or a
ban on later work with a materially new estimate.

The independently testable alternative freezes coefficient shift k=6002
while letting rank r grow. Its proposed threshold is positivity of the
principal-pole determinant and ||Q_r^(-1)E_r||_infinity<1 eventually,
with full reciprocal normalization and contour error retained. This changes
which dimension is fixed; it does not claim growing-k control or an overlap
with finite PF bounds. It is a standard-method specialization, not a new
creative central mechanism. Its precise source coverage and stopping test
are nominated separately in `2026-11-05-fixed-shift-reciprocal-pole-test.md`.
That newly written ready continuation requires separate approval next turn.

Outcome: bounded source EXPLORATION. No Xi remainder inequality, lemma,
certificate, RH progress beyond inspected mathematics, or source theorem
verification is claimed. The creative blocker is still an independently
motivated estimate with both order parameters growing.
