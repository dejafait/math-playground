# Actual-theta overlap factor: bounded zero-jet continuation

TARGET: Determine the sign of V(0)V''''(0)-V''(0)^2 for V(t)=A(t)/C_k(2t) with L019/L239's actual theta k, using L233's normalization and rigorous complete-theta tail bounds.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-quotient/normalized-overlap, characteristic-factor and differential-inequality comparison in 2026-10-31-normalized-overlap-factor-source-scope.md; its queries and local duplicate/failure screen cover precisely this scalar and object. No inspected result determines its actual value or sign; no novelty claim follows.
SOURCE_EVIDENCE: Buescu-Paixao (2012), Proposition 2.5, printed p.159, https://revistas.usp.br/spjournal/en/article/download/74466/78087/100183 (complete statement rechecked 2026-10-31); Csordas v2 Theorem 3.1 and (3.5), https://arxiv.org/html/1309.0055v2 (statements rechecked); Durrett PTE version 5, Theorem 3.3.2, p.126, https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf (accessible; proof inspection reused from completed source-scope assessment).
COMPARISON: The necessary differential inequality and sufficient positive-definite product rule are known. Only the actual quotient's applicability and finite jet evaluation remain for this diagnostic. No inspected shape theorem, reciprocal-zero Hankel result or generic countermodel decides that scalar for actual theta.
GAP: Establish quotient well-definedness and local C4 regularity, then enclose the exact zero jet including all theta tails. Its sign and the full factor premise are unproved. A finite test cannot supply all-frequency positive definiteness or all-degree signs.
REASON: Direct-source recovery review confirms coverage for one bounded specialization/calculation. Direct differential coverage removes dependence on the inaccessible moment-converse source; only applicability and the actual scalar need mathematical work. A new exact-k application is not a reproof of Bochner, product closure or the cited derivative inequality.
SCOPE: Only the displayed zero jet for real t and the exact actual k. No auxiliary Jacobi profile, raw finite truncation, imaginary-axis positivity, zero simplicity or RH premise is allowed. Separate literature recovery review completed 2026-10-31; no research is invoked in this turn. The exact target is unchanged.

## Essential inputs and qualifications

Use L233's A(t)=integral_R s^2 k(s+t)k(s-t)ds and
C_k(h)=integral_R k(v+h)k(v)dv. L019 identifies actual k on the
positive half-axis and gives strict positivity and rapid decay;
L239 supplies its holomorphic even continuation and strip bound.
Do not confuse L019/L239's auxiliary A with L233's associated A.

Before computing, justify the denominator on the real axis, a positive
normalizing value at zero, and all needed differentiated-integral
envelopes. L239's strip estimates are available for a Cauchy-bound
argument for fixed derivatives; that application has not been written.
No claim of an entire quotient or global complex zero-free denominator
is needed. The fixed scalar only needs local C4. Its real values and
evenness, ordinary versus modulus squares and the factor 2 in C_k(2t)
must be retained explicitly.

Import the cited derivative inequality, using n=2, m1=0, m2=2, x=0,
only as a conditional necessity under positive definiteness. Do not
assume that premise while computing the scalar. The source already
covers local C4, so the unread Lukacs moment converse is not essential.
Use the source-scope assessment for exact references and its primary
access qualifications, including the normalization caution for
Csordas Theorem 3.2. No reproof of those standard theorems is warranted.

L233's first-spectrum Fourier identity explains the possible downstream
use if a full factor certificate were eventually found. The all-degree
gap is independent. L055/L057's generic shape and reciprocal-zero Hankel
countermodels, L233's comparison kernel and the separate parity-tail
failure are contrasts, not premises or evaluations of this quotient.
L600/L601 and the blocked optional Umihara source supply no input.
No cross-notebook theorem is proposed.

## One bounded mathematical attempt and decision test

Derive only the zero-jet expressions needed for the displayed scalar,
with dominated differentiation and quotient rules justified. Any
numerical enclosure must be rigorous: include discretization/integration
error, all omitted theta modes and unbounded real-variable tails. A
floating-point preview is not a certificate. Save full evidence to disk
and report the enclosure, threshold zero, failures and artifact paths.
If these bounds cannot be completed in one attempt, preserve the
unfinished formulas and report the unresolved enclosure honestly.

A strictly negative upper bound abandons this stronger factor mechanism
only, without refuting first-sign positivity or RH. A nonnegative lower
bound passes this necessary test only; it does not license an uncovered
global-factor proof in the same turn. An enclosure containing zero is
inconclusive and needs a concrete refinement before repetition. Preserve
any informative obstruction or unfinished reasoning. Do not create a
lemma merely to record a numerical preview or meet a quota.

This is routine finite-jet specialization/calculation, not a protected
creative central-gap attempt. A creative factor mechanism still needs
an independently testable all-frequency idea beyond this diagnostic.
Mathlib coverage for the exact quotient and supporting results is not
checked; no absence is asserted.

## Direct-source recovery review — 31 October 2026

The ready assessment omitted direct source URLs in this file. They are
now recorded in SOURCE_EVIDENCE; no mathematical obstruction was resolved
anew. Reopened Buescu-Paixao, printed pp.158-159, and checked complete
Propositions 2.4-2.5. The latter assumes positive definiteness on R and
C^(2n) regularity near zero. The saved n=2, m1=0, m2=2, x=0 comparison
is within its stated range. This confirms the previous comparison only;
it establishes neither hypothesis for actual V. Upstream proof-access
limitations in the source-scope assessment remain nonessential to this
cited import.

Reopened Csordas v2 Section 3: Theorem 3.1 and (3.5) retain the normalized
Bochner and unnormalized L2-overlap interfaces. Retain the existing (3.4)
normalization caution. Durrett's author PDF remains accessible; reuse the
prior product-proof assessment without a new survey. No quotient closure
is imported. The prior local duplicate/failure screen still applies to
the unchanged target and hypotheses. Mathlib coverage remains unchecked.

SPECIALIZE retained. This process repair supplies no new mathematical
evidence and does not renew exploration counters. Next turn should
calculate the saved scalar with rigorous complete tails.
