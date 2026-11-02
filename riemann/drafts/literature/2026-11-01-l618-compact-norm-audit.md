# Coverage for a separate audit of L618

TARGET: Audit L618's full-multiplier constants, weighted Fourier inversion and causal support compression, including the fixed-window quantifier limitation.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-target search and comparison in 2026-11-01-suzuki-large-parameter-compact-norm.md and the prior post-C499e screen; the audit stays within the same complete kernel, real theta>=2 and fixed finite T. No new search or novelty claim is made.
SOURCE_EVIDENCE: Suzuki arXiv:1907.07302v2 (6 March 2020), (1.1), (1.10), Theorem 1.2 (K-ii)/(K-iii), printed pp.2-3; its full (K-v) proof (3.14)-(3.15), printed p.8, was checked for scope but its implicit estimates are not imported. DLMF 5.9.13, Re(w)>0 with principal logarithm; standard L1 Fourier inversion and Hilbert--Schmidt inequality; L001/L005/L018 and the new L618 proof.
COMPARISON: The known sources supply the complete kernel and digamma integral, while L618 supplies the explicit parameter bounds. This continuation is a critical audit of that specialization and its source applicability, not a reproof of the kernel construction or a new sign mechanism.
GAP: L618 has not received a separate critical review. Check the derivative-series majorant, the rational/gamma/arithmetic contributions and constants, inversion integrability without a uniform source big-O, the infinite-domain support reduction, t=0 and real theta endpoints, and the order of quantifiers.
REASON: Separate literature approval completed on 2026-11-01: the imported statements match the saved audit scope. The next turn may audit the existing specialization; this approval neither validates L618's proof nor adds a mathematical result.
SCOPE: Only audit L618's stated fixed-window result, using its exact imported hypotheses and existing representations. No new growing-window estimates, fixed-parameter global contraction, sign transfer, RH-equivalent positivity or new mathematical target is approved here.

## Reused source scope

The [original assessment](2026-11-01-suzuki-large-parameter-compact-norm.md)
already compares this precise family and the two supporting digamma
representations. The calculation selected
[DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13), not an asymptotic
expansion with unspecified constants. The principal-logarithm domain
contains w=8-iu/2 for all real u.

[Suzuki v2](https://arxiv.org/pdf/1907.07302v2), Theorem 1.2,
provides the continuity, causality, fixed-parameter growth and weighted
Fourier identity stated in L618's hypotheses. The critical review must
compare these exact imported properties to their uses. An audit of
the source's entire construction is not claimed or required by this
bounded target; any concern about a needed property must be stated
explicitly rather than concealed or replaced by a theta-uniform claim.
The source's (K-v) proof was read through its Fubini justification;
L618 uses its own integrable multiplier bound and support compression.

The derivative of the Euler logarithm in L005 must be justified by the
displayed local derivative majorant in L618, not assumed from mere
pointwise convergence. Standard L1 Fourier inversion applies only
after both the weighted kernel and its transform are shown integrable.
The imported growth constant is allowed to depend on theta solely in
the first integrability check, while the resulting pointwise estimate
must be independent of that constant. The norm estimate must act on
the original infinite L2 space, using causality to justify restriction.

The audit passes only if the complete bound is valid for every real
theta>=2 and every fixed finite T>0, with no RH premise. Repair a
specific error if found, or mark the local proof unaudited/failed and
preserve its evidence. Neither a successful audit nor compact-norm
decay settles actual-Xi signs or fixed-theta all-window control.

## Separate source-scope approval (2026-11-01)

LITERATURE_REASON: The supervisor requires separate approval of this newly saved audit assessment; verify the essential imported statements before mathematical reliance, reusing the original search rather than repeating discovery.

Directly inspected [Suzuki v2](https://arxiv.org/pdf/1907.07302v2),
printed pp.1–3, equation (1.1), equation (1.10), and Theorem 1.2.
Its parameter is real theta>1. Parts (K-ii)/(K-iii) supply continuity,
growth, the transform on Im(z)>1/2, and negative-support vanishing.
These are precisely the properties imported by L618, for theta>=2.
No RH premise occurs in this theorem. Its determinant conclusion is
local and is not an input to the proposed audit. The source's growth
constant need not be uniform in theta. The proof of those imported
properties is not independently certified by this scope review.

Directly inspected [DLMF 5.9(ii)](https://dlmf.nist.gov/5.9#ii),
including its Re(z)>0 domain heading and equation 5.9.13 with the
principal logarithm. The equation matches L618's cited representation;
its use at Re(w)=8 stays within that domain. No asymptotic remainder
or new digamma bound is imported from this review.

Read L001/L005/L018 for input scope and L618 to identify its uses,
without replaying or approving its estimates. L005 supplies the
holomorphic Euler logarithm, not by itself L618's differentiated
series; the derivative convergence argument remains an audit item.
Standard L1 Fourier inversion requires both the function and its
transform in L1, and gives equality at continuity points. The
Hilbert--Schmidt inequality requires a square-integrable kernel on
the stated measure space. These named standard results suffice as
imports; all applicability, support reduction, constants and endpoints
remain to be checked in the mathematical audit.

Duplicate/failure coverage reuses the original assessment and the
post-C499e screen, with the central-screen and compact-norm histories
read narrowly. The known construction is not a new sign mechanism;
fixed-parameter global control and actual-Xi signed transfer remain
missing. No new search claim, source blocker or creative target arose.
The first scoped status output was truncated; it was used only to
notice existing work, not as mathematical or failure evidence.

DECISION remains SPECIALIZE, now approved for the exact TARGET above.
The approval supplies no new mathematical evidence and does not mark
L618 audited. Pass/fail remains the exact test in PROGRESS.md: either
verify its complete stated bound and quantifiers, repair a concrete
error, or retain a failed/unaudited result. No extension to growing
windows or fixed-parameter global contraction is covered.

## Mathlib

No new coverage check is needed for this analytic audit. Full kernel
and limit availability remains unverified; L001/L005 record supporting
Euler-product APIs only. A successful informal audit is not formal
verification.
