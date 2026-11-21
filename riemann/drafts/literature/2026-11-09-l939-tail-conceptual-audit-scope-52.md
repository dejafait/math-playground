# Separate scope review for the new tail asymptotic

TARGET: Assess source coverage for an independent conceptual audit of L939's complete signed balanced-saddle asymptotic and relative remainder.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step53 reused the exact-object/terminology and duplicate/failure searches in 2026-11-09-l938-energy-tail-source-scope-50.md and 2026-11-09-l938-balanced-tail-attempt-51.md; narrowly searched their related histories and fixed-cell stop, then compared the new L939 application with the primary theorem. No broad discovery search or novelty inference.
SOURCE_EVIDENCE: Step53 directly inspected Katsevich arXiv:2406.12706v3, Assumptions2.1–2.3 pp8–9, Remark2.5 p9, Definitions2.6–2.11 pp9–11, complete Theorem2.12 p11, Lemma4.1 p20 and its AppendixE proof p37, Corollary4.3/Lemma4.4 and proofs pp23–25, and LemmaE.1 p38; https://arxiv.org/pdf/2406.12706v3 . Read complete L939 and L938 through its simplex formula/positive-parameter beta justification; earlier normalization coverage is reused.
COMPARISON: The cited local-regularity assumptions and Remark2.5 cover the proposed audit method, including a separate actual-outer bound; no global smoothness or amplitude positivity is imposed there. L939 supplies concrete claimed estimates for the extension, minimum, full theta and normalization. Their truth and uniform constants remain audit obligations; citation alone does not establish the asymptotic.
GAP: Independent verification of L939's full signed coefficient, exact prefactor, global constrained bound, boundary integrability, uniform local derivatives and three normalized errors remains undone. No essential source blocker remains for that audit; finite-energy and RH gaps persist.
REASON: Complete the saved source-scope comparison and nominate the exact covered conceptual audit below for separate next-turn approval. This is source coverage, not mathematical validation or a new asymptotic result.
LITERATURE_REASON: New concrete applicability claim: L939 extends its phase/amplitude measurably across singular simplex faces and replaces Katsevich Assumption2.3 by its own normalized full-theta outer bound. The separate audit must check the precise permitted hypotheses and signed error decomposition.
SCOPE: Source scope is ready for the exact REPRODUCTION conceptual audit below, subject to separate next-turn approval. Preserve all 34 rows, twelve factors and M_0^12 normalization; no compact-cell refinement, effective onset, higher-order fallback or additional variation result. Full/supporting Mathlib coverage remains unchecked.
COVERED_TARGET: Independently audit L939's complete signed balanced-saddle asymptotic, including its singular-boundary extension, full-theta uniformity and three normalized errors.

## Nomination context, preserved

The mathematical claim proposed in step52 is L939's
v(E)=B(sqrt(E/12))(1/371319795000+o(1)), with B>0 and a complete
relative remainder. It could supply the unbounded-energy part of
a future variation argument. Main L030–L032/C032a positivity and
finite-energy crossings, parameter endpoint signs, contacts, other
degrees, initialization, realization and continuation remain open.

The comparison should retain every one of L938's 34 rows and all
twelve factors. Relevant new proof obligations are L939 equations
(11)–(18): r^23 Jacobian/power accounting; z_r>=sum y_i^2/32 on
the entire constrained simplex; H_r and its determinant; the
integrable product of twelve square-root singularities; the full
theta q and its first two derivative bounds; local H-scaled C^2/C^4
uniformity with n=pi exp(2r), R=r; and the three separate errors
relative to the nonzero coefficient. The exact arithmetic evidence
is `scripts/heat/l938-balanced-coefficient-52.json`, with a displayed
Newton-recurrence check in L939. The certificate itself proves no
analytic tail estimate.

Essential input claims are L019's exact kernel and L938's analytic
density/polynomial. L058/L874/L917 supply the earlier normalization
and algebra through L938. L037's Decimal contracts are not premises
of L939. No cross-notebook input is needed. BKR remains parked;
its inaccessible proof is neither an input nor a reason for an
access loop. The fixed-cell and L915/L916/L922/L937 stop evidence
is preserved. Full/supporting Mathlib coverage remains unchecked.

Approve a later conceptual audit only if the existing primary theorem
scope covers this exact application and the new canonical proof has
all load-bearing estimates available for independent scrutiny.
Otherwise identify the precise source/hypothesis gap; do not silently
assume positivity or replace the actual outer integral by a Gaussian
tail. This review must not be reported as independent proof validation.


## Completed source-scope comparison — step53, 9 November 2026

This literature-only step inspected the new canonical proof to locate
its obligations, without verifying its mathematical estimates or running
its coefficient producer. No lemma, mathematical script, DAG or PROOF
was edited. Outcome EXPLORATION, classification NOVELTY_UNCHECKED:
new applicability comparison, with no newly proved input or sign obstruction.
The existing searches are adequate for this unchanged object and method;
additional broad browsing would repeat their coverage.

### Primary source and applicability limits

Anya Katsevich, *The Laplace asymptotic expansion in high dimensions*,
arXiv:2406.12706v3, posted 12 June 2025, title page 13 June 2025;
[versioned primary PDF](https://arxiv.org/pdf/2406.12706v3).
The printed-page references in SOURCE_EVIDENCE were inspected directly,
including the essential local Taylor and outer-integral proof cases.

Assumption2.1 requires a unique global minimum and positive Hessian;
Assumption2.2 requires amplitude C^(2L) and phase C^(2L+2) only on
the closed H-scaled local ball. Remark2.5 explicitly allows a separate
exponentially small bound for the normalized actual outer integral.
It does not require the pointwise growth inequalities when that bound
is supplied. Theorem2.12 retains the signed amplitude and separates
local, Gaussian-complement and actual-outer errors. Its constants are
controlled by L and the displayed derivative quantities. Lemma4.1's
change of variables and Corollary4.3/Lemma4.4's local Taylor proof do
not impose positivity or smoothness across distant boundary faces.
LemmaE.1 is the default outer estimate, not an extra local premise.

Thus global boundary discontinuity is not itself an uncovered theorem
hypothesis. Whether L939's extension and its claimed outer estimate
actually meet these requirements is a separate mathematical question.
This is an applicability reading of the source, not a verification of
those claims. No reproof of a general Laplace or convolution theorem
is needed; BKR remains nonessential and parked.

### Exact scope for the independent audit

L939's existing equations (1)–(18) supply explicit claims for every
load-bearing application step. The audit must check them rather than
infer them from the source. Retain the following questions together
as one audit of the existing asymptotic, without creating new targets:

- Does L938's labelled twelve-factor density become L939 (11) with
  exactly r^23, the twelve factors of 2, the exponential prefactor,
  and every factorial? Do all 34 signed rows enter (5)–(6), without
  multiplicities from permutation? Read the full selected arithmetic
  certificate evidence if it is used; a coefficient preview is not
  an independent verification.
- Do (12)–(14) prove the constrained global bound on the entire
  simplex, including negative coordinates and faces, and the claimed
  Hessian/determinant? Does the measurable extension preserve the
  unique minimum and the integral, with the closed local ball wholly
  inside the smooth region? These are still unverified local claims.
- Do (8)–(9) justify differentiating the complete theta series through
  order two with constants independent of r? Does (15) integrate all
  twelve singular factors, including simultaneous faces, and does
  the normalization in (16) include the full Hessian and n powers?
- Do the claimed C^2/C^4 estimates hold uniformly on the entire local
  ball, including the dependent twelfth coordinate and H-scaled
  derivative norms? Compare the barred bounds (2.9), A_2 (2.14) and
  errors (2.16)–(2.17) with the asserted (18); do not replace the
  actual outer error by a Gaussian complement. Finally check the
  full relative remainder against the fixed nonzero C_*, and the
  scale B(r), rather than just the unsigned size of the integral.

Inputs to scrutinize are L019 and L938; L058/L874/L917 enter through
the latter's already audited density construction. The analytic audit
need not reopen L037's Decimal implementation because L939 claims no
Decimal-dependent premise. The saved exact-rational coefficient record
is supplementary evidence for finite algebra, never evidence for a
tail remainder. No cross-notebook input or uninspected source is required.

Continue only if the independent audit pays every load-bearing claim;
a failed estimate blocks downstream use of L939 and must be corrected
or qualified. A missing essential theorem hypothesis returns that exact
scope to REVIEW_REQUIRED. No sign on the remaining bounded energy range,
no global crossing count and no RH conclusion follows even from success.
The fixed-cell and L915/L916/L922/L937 stop evidence is preserved.

A new central creative mechanism is not nominated merely to satisfy
routing cadence: the present gate requires coverage for this existing
unaudited input, and its audit remains essential before tail-based
variation work. A later discovery target must have its own discriminating
mechanism and coverage; this review supplies neither by relabeling the
tail specialization. Supervisor routing and counters are untouched.
