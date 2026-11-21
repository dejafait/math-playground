# Signed first-zero margin: continuation for separate approval1728

TARGET: Critically audit C033g's uniform bound W/f^2<-1/2000 on [1,2], including low-zero normalization, relative errors and the complete-divisor E correction.
CHECKED: 2026-11-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse assessment1726, source-working1726 and comparisons1709/1721 for this unchanged signed-comparison scope; attempt1728 checked C032/C033 and the named November19 stops for duplicates. No matching signed theorem was identified in the bounded screen; this is not a novelty claim or a new literature search.
SOURCE_EVIDENCE: FLINT contract/example https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html and fixed implementation https://github.com/flintlib/flint/blob/1d432c3bba36d1a29f6453ebfaa00e43f58c278f/src/acb_dirichlet/isolate_hardy_z_zero.c ; Arias de Reyna Section2 https://ir.cwi.nl/pub/19724/19724D.pdf ; Bellotti--Wong v2 Theorem1.1/Section5 https://arxiv.org/pdf/2412.15470v2 ; inherited Sra fixed-v1 Theorem3.3 https://hexagonmath.org/pdf/2611.00345v1 and Platt--Trudgian Theorem1/Section2 https://arxiv.org/pdf/2004.09765v1 . Full relevant cases and qualifications are reused from source-working1726 and source-notes1721.
COMPARISON: The prior approved target already covered the signed first core, relative complete-divisor errors, E correction and endpoint normalization. C033g claims that same bound through elementary Gaussian shells and a removable-integral power series; no new source theorem or erfc asymptotic enters. Stop1711 and phase-only park1725 remain valid for their earlier estimates.
GAP: The fresh local analytic proof and its source applications require an independent critical audit; the rational script checks only arithmetic. General signed annihilators, constant-span completeness, positive output, moments and actual-Xi realization remain unresolved even if this two-point result passes.
REASON: A separate critical audit is necessary before relying on the new signed estimate. This continuation reuses unchanged essential source coverage and is newly saved for separate next-turn approval, not an audit or self-approval of C033g's proof.
SCOPE: Exactly C032j/m/n, C033f and C033g's full positive-ordinate divisor with multiplicity/conjugation, gamma>14, |delta|<1/2, s in [1,2], a=1/8, b=1/4, first simple real center in (14,15), all others above20, corrected inclusive count, fixed-v1 and V(3*10^12) qualifications.

## Bounded audit and decision test

Read the complete C033g proof, its small rational checker and full
relevant certificate values. Check the Gaussian half-normalization,
the shell counts and complete infinite geometric tails, direct width
derivative bounds before division by the tiny core, and the signed
weighted-mean comparison. In the E calculation, check both the compact
removable quotient and the entire subtraction in the noncompact part,
the coefficient exchanges, the cancellation of j=0 and the final
negative multiplication by a positive lower ratio bound. Verify both
width endpoints and the near-diagonal consequence in C032n(19).

Accept only if all analytic inequalities and source hypotheses justify
the strict uniform -1/2000 upper bound. If an error is found, identify
the failing line, repair only within this assessed scope if possible,
and record the resulting actual versus required bound. If the repaired
enclosure contains zero, park this comparison without weakening the
reported threshold or hiding the failure. A source-scope change needs
REVIEW_REQUIRED rather than an unassessed replacement theorem.

The low-zero calculation is imported, not independently rerun; FLINT's
generated-documentation caveat, fixed-code inspection, and historical
low-index input remain explicit. This is a conceptual analytic audit
of a local estimate, not a candidate RH audit or a creative mechanism.
No central creative target is ready: the remaining transfer from this
minor to actual-Xi all-degree positivity has no justified test yet.
Full matching Mathlib coverage is unchecked/unknown.

## Separate source-gate approval1729 — 19 November 2026

LITERATURE_REASON: The supervisor explicitly requires separate approval
of the newly saved audit continuation. This checks unchanged essential
source coverage; it is not a renewed search for a signed theorem.

Read source-working1726, comparison1726 including approval1727,
source-notes1721, comparison1709, nomination1725, the source-import
portion of C033g and history1728. Read the exact stop1711 and
phase-only park1725. These cover the same divisor, widths, first-core
separation, relative-error and E scope. Neither stopped inference
supplies the new margin, and neither prohibits its independent audit.
No new mathematical target or source hypothesis is introduced.

Reopened the official FLINT contract, low-index method description,
and complete checked example at the primary URL in SOURCE_EVIDENCE,
lines36-49 and57-120. It still specifies consecutive critical-strip
zeros, simplicity and completeness, the n<=126 Gram branch, and
first-two balls enclosing ordinates14.1347... and21.0220.... Retain
its generated-documentation caveat and the fixed-commit case inspection
in source-working1726. The external calculation and historical
Gram-law input remain imported, not independently replayed or proved.
Reopened the Bellotti--Wong v2 version record
https://arxiv.org/abs/2412.15470v2 confirming7 July2025; reuse the
already inspected Theorem1.1 and complete relevant Section5 cases in
source-notes1721 for constants and endpoint conventions, rather than
infer theorem coverage from the abstract. All other essential primary
proof cases are reused from the named notes. No new inaccessible lead
is made essential and no new external-computation capability is assumed.

DECISION remains EXPLORE for the unchanged exact TARGET above.
Source coverage is approved for the next conceptual audit. C033g's
first-core normalization, Gaussian shell estimates, relative width
errors, exchanges, removable/noncompact E cancellation and final
signed comparison are still unverified mathematical obligations.
Do not import their truth from this approval or the rational checker.
The stated acceptance test remains the full uniform bound below
-1/2000 against required sign threshold0, including both endpoints;
a repaired enclosure containing zero parks this comparison.

This approval repeats adequate coverage and is recorded STALLED,
not a mathematical advance or an informative negative. It spends no
mathematical exploration attempt. The next invocation defaults to the
approved audit; further literature needs changed essential scope.
Full matching Mathlib coverage remains unchecked/unknown. The minor's
unproved connection to actual-Xi all-degree positivity still blocks
a justified central creative test. No lemma, script, PROOF or DAG
was changed and no analytic estimate was derived in this turn.
