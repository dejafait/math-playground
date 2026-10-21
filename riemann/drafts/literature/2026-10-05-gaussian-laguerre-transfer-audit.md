# Coupled first-Laguerre comparison — separate audit coverage

TARGET: Critically audit L367's product-error identity, signed response subtraction and shrinking-regulator bounds, including zeros and fixed-ε differentiation.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the four exact-target/terminology searches and inspected primary theorem passages in drafts/literature/2026-10-05-gaussian-coupled-laguerre-transfer.md, plus the scalar-source comparisons in drafts/literature/2026-10-04-gaussian-regulator-response-audit.md; no new external search or originality inference.
SOURCE_EVIDENCE: Csordas–Vishnyakova, CEJM 11(9) (2013), 1643–1650, DOI 10.2478/s11533-013-0269-x, Theorem 2.3, Remarks 1.3 and (1), pp. 1644–1646; Paris arXiv:1503.07329v1, §2 (2.1)–(2.6); NIST DLMF 5.11.3/9–13 and §5.11(ii), 5.15.8–9, 25.4.1–5; recorded primary-source domains reused, with local L357 product subtraction, L358 (3), audited L366 (1)–(2) and L320 (4).
COMPARISON: Existing coverage includes the scalar gamma estimates and unconditional completed-zeta growth needed for L367's coarse specialization; none of these sources validates its nonlinear algebra, signed margins or sufficient shrinking exponents without a separate mathematical audit.
GAP: The product and response identities, positive normalization, uniform constants, A² versus A²L² scaling and claimed α thresholds remain to be critically checked; no favorable arithmetic margin is supplied.
REASON: The newly named audit is within the already inspected supporting-source domains; prospective scope approval requires no new theorem or missing essential source, and does not certify L367.
LITERATURE_REASON: Separate approval is required for the newly named critical-audit scope, specifically its use of L320 (4) at R=1 and both signed transfer directions, rather than additional browsing of unchanged inputs.
SCOPE: Exact real L357 family, positive A of L358, audited L366 jets j=0,1,2, |ξ|≥40 and 0<ε≤1/(1+ξ²); audit only L367's claims and their stated sufficient subdomains, including zeros and fixed-ε derivatives. No higher-level or actual-theta sign theorem, phase-return rate or RH candidate.

## Source comparison and applicability obligations

This literature-only step read the previous ready coupled-transfer assessment
and separate response-audit assessment, L367, L320 through its strip proof,
L366's hypotheses and conclusions and recorded critical-audit qualification,
L358's normalization (3), and L357's concluding product-error argument.
These readings establish coverage of the proposed audit, not its correctness.
No new result is derived and no lemma or mathematical script is changed.

Csordas–Vishnyakova's [primary paper](https://d-nb.info/1372516522/34),
Theorem 2.3 and the recorded proof passages, require all generalized Laguerre
levels at every real point for the real-entire criterion. The first-level
warning remains relevant. This is a contrast, not an imported sign premise;
the prior theorem-level comparison is reused unchanged.

Paris's [v1 primary text](https://arxiv.org/html/1503.07329v1), §2,
(2.1)–(2.6), provides scalar inversion and retained contour remainders.
Its fixed-real-exponent theorem does not establish growing-complex-exponent
uniformity. That difference is supplied locally by audited L366, whose
frequency derivatives and normalization are the input claims being used.
No new application of Paris's full theorem is proposed.

The inherited DLMF version is v1.2.8 (2026-09-15), not independently refreshed.
[5.11.3](https://dlmf.nist.gov/5.11.E3),
[5.11.9–13 and remainder restrictions](https://dlmf.nist.gov/5.11#E9)
provide sector-controlled Stirling and bounded-real-part vertical modulus
estimates; the recorded K=1 exception and fixed-shift ratio restrictions
remain in force. [5.15.8–9](https://dlmf.nist.gov/5.15#E8) supports the
scalar differentiated estimates already assessed. [25.4.1–5](https://dlmf.nist.gov/25.4)
provides completion and reflection. None is a critical-line zeta lower bound.
Their cited books and Paris's monograph remain unread, unused leads.

L320 (4) has fixed strip parameter R with R>η>1/2 in its statement;
the strip proof uses the boundary condition 1/2+R>1. The audit must explicitly
retain these conditions when using R=1, and must check its Cauchy circle
against the full strip, imaginary-height change and exponential factor.
The existing proof uses the standard named maximum-modulus principle,
Euler summation and scalar Stirling, already within the prior assessment's
permission to use L018/L320 for absolute growth. No larger strip or
RH-dependent growth estimate is requested. Cauchy's derivative estimate
requires a holomorphic function on the closed disk neighborhood;
L366 identifies the entire completion and its factor of two.
These are audit obligations, not a new proof of the specialization.

The positive gamma scale uses a fixed real gamma argument 1/4 and
large real frequency. The bounded-real-part/vertical sector coverage is
adequate; extending a large-height estimate to |ξ|≥40 must retain
continuity and gamma's absence of zeros and poles there. It must not use
a lower bound for F_0 or ζ. No essential unread source is identified.

## Duplicates, failures and relevance

L357 already supplies the generic subtraction mechanism. Rechecking it
is REPRODUCTION, not discovery. L358 distinguishes actual derivative jets
from derivatives of F/A; L366 supplies uniform remainder and response
bounds, with constants independent of ξ and ε. L367's claimed α>1/4
and α>1/2 regimes are the audit targets, not results accepted in this step.

The recorded [common-threshold failure](../../ATTEMPTS/2026-10-04-gaussian-common-first-sign-threshold.md)
uses L365's negative signs at each fixed small regulator with a potentially
regulator-dependent onset. It rules out a common global sign threshold;
it does not rule out restricted coupled comparisons. The prior L366 audit
is recorded in history/2026-10-05-gaussian-response-critical-audit.md.
This audit should reuse that input instead of repeating its contour work
unless a specific inconsistency appears. L357's absolute convergence alone
still supplies no gamma-normalized relative margin.

The main gap is global actual-theta mixed positivity. The intermediate
target is reliability of L367's conditional comparison. Its plausible
use is a later sign transfer in the initial logarithmic/low-index range
motivated by L320, provided an independent actual arithmetic margin is
proved. Heights above forty, higher signs, the endpoint arithmetic margin
and regulator-uniform phase-return onset remain unresolved.

## One separate mathematical audit

Test the complete jet-product identity and both signed subtraction
directions, including the quadratic response and remainder products.
Check division by A²L² versus A², the fixed-ε convention even on a coupled
curve, zeros of F_0 and H, the full L320 growth specialization and gamma
lower scale, and uniform constants in both claimed shrinking regimes.
No division by a vanishing transform or differentiation of uncontrolled
big-O terms is permitted. The exact TARGET is approved prospectively as
SPECIALIZE; the later audit should be classified REPRODUCTION.

Continue downstream only if the complete stated comparison survives, or
a precisely qualified useful correction is established. If normalization,
uniformity or a claimed sufficient exponent fails, record the exact defect
and repair or narrow that comparison before any signing use. Even a
successful audit supplies no favorable sign margin and no RH conclusion.
This newly ready assessment receives separate supervisor approval next turn.

## Mathlib and outcome qualification

Full matching nonlinear comparison: not checked. The supporting Poisson
and smooth-series references recorded in L357–L366 do not cover the whole
statement; Cauchy/Stirling library coverage was not refreshed. Unknown
coverage is not evidence of absence. There is no new source import or
mathematical advance beyond the saved coverage in this turn; its honest
outcome is STALLED with a concrete ready audit continuation.
