# Restricted local-density source audit: proposed continuation

TARGET: Audit Maples--Rodgers v2 Proposition 2.5 at k=2 and c=1/4 for 1<=H<=T^(1/4) and 1/2<=sigma<=1, checking displacement normalization, indicator domination, multiplicities and uniform constants before any L471 kernel application.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed joint-Blaschke comparison and its exact Proposition 2.5/erratum searches; no earlier assessment was found by exact Maples--Rodgers/1404.3080 searches in active-notebook source notes, foundations, ATTEMPTS and history. The changed target is a restricted critical audit, not another search for the whole mass estimate; no novelty claim.
SOURCE_EVIDENCE: Maples--Rodgers, IJNT 11 (2015), 2087--2107, arXiv:1404.3080v2 (4 June 2016), https://arxiv.org/html/1404.3080v2 and https://arxiv.org/pdf/1404.3080v2: Theorem 2.4 and Proposition 2.5, p. 5; normalized displacement (8), p. 6; Corollaries 4.1--4.2 and complete proofs, (18)--(23), Lemma 4.3 and its complete proof, Section 4 pp. 8--12. Relevant full passages were read; Fujii/Selberg/Jutila arithmetic inputs remain cited without a manuscript audit.
COMPARISON: The desired count-only conclusion is explicitly known. Audit only its k=2,c=1/4 indicator specialization: the printed final substitution uses a displacement cutoff needing reconciliation with (8), its Cauchy-kernel domination needs normalization checks, and (19)'s unrestricted piecewise-continuous weight claim is not licensed as a premise. A restricted replay is justified by these specific source-proof concerns; no full general-weight reproof or new theorem is proposed.
GAP: Establish or reject the exact uniform indicator specialization using the source's stated global density and unweighted count moments, without adding RH, spacing, simplicity or a weighted sparse-neighborhood premise. No L471 mass or kernel saving is covered by this audit.
REASON: This is an independently testable source-input audit after the whole joint-suppression implementation fails its weighted sparse-coverage gate. A valid source-normalized input could support a later kernel-moment calculation; neither that application nor any saving is preapproved. Newly written readiness requires separate approval next turn.
SCOPE: Fixed k=2 and c=1/4; real T>=2 with a harmless fixed larger onset permitted, 1<=H<=T^(1/4), 1/2<=sigma<=1; multiplicities retained, strict beta>sigma and 0<gamma_0<U source conventions. Audit Section 4's upper-tail indicator case only. Import Theorem 2.4 and Corollary 4.2 within their stated hypotheses, retaining qualifications about their arithmetic inputs; do not import general-weight (19) or Lemma 4.3 without the restricted justification.

## Exact known conclusion to audit

The source defines N(sigma,U) as the multiplicity-counted number of
nontrivial zeta zeros beta+i gamma_0 with beta>sigma and 0<gamma_0<U.
Proposition 2.5 gives the k=2,c=1/4 case

    (1/T) integral_0^T
      |N(sigma,t+H/log T)-N(sigma,t)|^2 dt
        <= C H^2 T^(-(sigma-1/2)/4),

with C independent of T,H,sigma in the stated domain. This is the
source's claimed conclusion, not a newly derived result. An audit
must distinguish its open horizontal/vertical endpoint convention
from the closed-shell conventions in L467/C483a. No closed-endpoint
extension or padded dyadic application is part of this target.

Use Q(x)=1/[pi(1+x^2)] and the source's Q-norm and tail-error
definitions exactly. The macroscopic weight and the real-part cutoff
share the printed letter sigma; rename the weight in the replay to
avoid confusing their roles. The normalized displacement in (8)
depends on the same base T used in the moment integral. Its change
under the source's n^2 T dyadic padding must be accounted for.

The inspected proof has three concrete audit obligations: reconcile
the indicator cutoff following (23) with (8); justify an indicator
majorant by the Cauchy kernel with correct dilation and constants;
and obtain the upper-tail indicator estimate from the cumulative
density statement without relying on an unchecked arbitrary-weight
inference in (19). The two Holder steps, convolution bound and
far-tail error in Corollary 4.2 must remain in the uniformity check.
No repairs are supplied or approved as established mathematics here.

Continue only if a complete restricted replay recovers the displayed
uniform estimate from the named count-only inputs. Otherwise identify
the exact additional premise or surviving scale loss and park the
application. This is conceptual audit work, not a creative claim or
proof of the source's full manuscript. Save the replay canonically
only in a later research turn if warranted, with Hypotheses, Conclusion,
Proof and Mathlib sections and its exact import qualifications.

The plausible downstream use is to replace the global-count plus
pointwise unit-shell step of L483/C483a by a local L2 count input.
Whether that comparison improves the mesoscopic cutoff, and whether
it can handle |Z|^2 or pair-quotient weights, are uncalculated and
unapproved independent gaps. L471's negative-mass sufficiency and
the ultimate all-degree positivity gap remain unchanged. No external
fixed-half-plane result or cross-notebook input is required. Full
matching and supporting Mathlib coverage remain unchecked.
