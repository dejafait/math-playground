# C489a application audit — approved source coverage

TARGET: Critically audit C489a's activation of L489 under failure of RH, checking the threshold quantifiers, normalization, common positive-time interval and retained source qualifications.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse drafts/literature/2026-10-30-global-transition-activation-coverage.md and drafts/literature/2026-10-30-global-transition-specialization.md for unchanged global statements; L058/L062/L488/L489 duplicate and endpoint-failure checks were already made. No new mechanism or source search is claimed.
SOURCE_EVIDENCE: Newman (1976), Theorem 3 p.247, via D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , introduction (1)–(4), paragraph after (4), and unconditional Theorem 1.1; these primary statements were directly reopened on 2026-10-30. L018/L058 and separately audited L488/L489 are the canonical local inputs; source-proof limitations remain in the activation assessment.
COMPARISON: The statements cover exactly the elementary application in C489a; audit only the local implication, accepting the cited global statements and L488/L489 with their qualifications. No new source-proof audit is covered.
GAP: Independently check C489a's elementary specialization, especially strict positivity of Lambda under the conditional premise and the two L489 quantifiers within one compact interval.
REASON: A separate check can detect a real applicability error in the newly canonical conditional reduction; it does not supply collision exclusion or claim mathematical novelty.
SCOPE: C489a application only. Separate literature-only source approval completed on 2026-10-30; the unchanged mathematical target is ready for a later audit. No application audit verdict or source-proof audit is supplied here.

The bounded audit must check the biconditional for all real source times,
the t=4lambda and spatial 2z scaling, 11/200<1/8, epsilon=b-lambda_*,
and lambda_j=lambda_*-(lambda_*-a)/(j+1) for integers j>=1. Check that
negating all-real zeros actually supplies a nonreal zero, that L058
excludes x_*=0, and that the strict spatial bound is imported from L489
rather than obtained by taking a strict inequality through a limit.
Retain finite multiplicity and the unaudited source proofs/certificates.
Pass only if no extra simplicity, infinite RH verification, effective
cutoff or uniform a->0 assumption enters. Otherwise repair the precise
application error without enlarging its conclusion. Full matching
Mathlib coverage remains unchecked.

## Direct-source recovery check

LITERATURE_REASON: The supervisor reported a missing direct source URL in
this ready assessment; this bounded source check repairs that coverage
field without reopening mathematical work.

Directly inspected the versioned primary HTML introduction: (1) specifies
H_0(z)=xi(1/2+iz/2)/8; (3)–(4) give the kernel and positive
Gaussian exponent for all real source times. The paragraph after (4)
asserts finite Lambda and the closed biconditional for all real t.
Theorem 1.1 states Lambda<=0.22; the accompanying paragraph identifies
numerical verification as part of its proof. Theorem 1.2's conditional
criterion is distinct and is not substituted for Theorem 1.1.

These are inspected theorem statements, not a replay of the numerical
proof or Newman's classification proof. Existing duplicate and failure
comparisons are reused unchanged. The audit must still verify the local
time/space substitution and quantifiers in C489a; this source check does
not itself establish any of those implications. Its possible downstream
use is to validate the reduction from failure of RH to a finite collision;
it cannot exclude that collision. Pass/fail criteria remain the bounded
checks above. Full matching Mathlib coverage remains unchecked.
