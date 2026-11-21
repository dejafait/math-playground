# Far-left theta-Mellin bound: conceptual audit nomination

TARGET: Critically audit L803's standalone far-left theta-Mellin bound on all D, including Mellin-power monotonicity, the complete-series majorant, h=0 convergence, endpoint phase payment and exact normalization.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step530's exact-target, Gaussian-sum and endpoint search and duplicate/failure comparison in 2026-11-05-mellin-far-left-horizontal-segment-scope.md; the integral, D, branches and allowance are unchanged. This audit introduces no new analytic target or novelty inference.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), 5.9.1 with its hypotheses, 20.2.3/20.2(ii) and 2.5.1; bramble_trace paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23. Exact inspected primary passages, links and limitations are recorded in the completed step530 scope assessment; L803 uses only the cited real Gaussian integral as an external formula.
COMPARISON: Standard gamma integration and elementary decreasing-sum comparison support the method; neither the source allowance nor theta analyticity establishes L803's uniform angular, endpoint and normalization claims. Review the local specialization instead of importing its constants.
GAP: Independently verify or identify the first failure in L803's proof of absolute convergence and T_F<56u^(5/2)sqrt(47Q/(20pi))exp(-Q/8), which implies the approved 600 allowance, on the entire closed D.
REASON: The completed proof is new local work within already assessed method coverage and needs separate scrutiny of its actual-saddle sign argument and the use of the finite-left tangent only at u/2. Citation alone does not audit these steps.
SCOPE: Literature gate completed in step532; the unchanged exact target is ready for a separate conceptual audit classified REPRODUCTION. Coverage is approved, not the mathematical conclusion; the original nomination and bounded audit obligations are retained below.
LITERATURE_REASON: The supervisor requires separate approval of step531's newly written nomination; the previously unread source-use passages of completed L803 must be compared with step530's coverage before auditing. No additional external browsing is needed or performed.

## Completed coverage review — step532, 5 November 2026

This literature-only step compares the saved nomination with the completed
proof's hypotheses, conclusion, external-formula passage and Mathlib
qualification. It does not reconstruct or endorse the intervening
analytic estimates. The target text and SPECIALIZE decision are unchanged.

The primary-source record reused is
`drafts/literature/2026-11-05-mellin-far-left-horizontal-segment-scope.md`,
completed in step530. It records the inspected DLMF version, theorem
hypotheses, primary links, paper23 equations, exact searches and limits.
No new live-source inspection is claimed. In L803's Gaussian-majorant
passage, the only external evaluated integral is explicitly attributed
to [DLMF 5.9.1](https://dlmf.nist.gov/5.9#E1): mu=2, nu=1,
z=tau/2>0. The recorded primary conditions Re(nu)>0, mu>0,
Re(z)>0 and principal powers cover that stated real-integral use.
This is a source-hypothesis comparison, not verification that every
occurrence of tau in the proof meets its claimed lower bounds.

Unlike the broader method options assessed in step530, completed L803
does not invoke Euler–Maclaurin, Abel–Plana, a uniform boundary-theta
theorem or a Mellin-continuation theorem. Its decreasing-sum comparison
and weighted-sum estimates are written locally and must be checked in
the mathematical audit. Interior convergence and endpoint geometry are
assigned to L797/L798/L799/L802. Reviewing their uses, including the
endpoint-only application of L802's tangent inequality, remains part of
the saved audit; citation coverage cannot discharge it.

The existing local duplicate/failure comparison is adequate for this
unchanged target. Step530's recorded search found no inspected matching
standalone theorem; this is not a novelty conclusion. The completed
step531 history identifies L803 as the local proof now needing audit.
The narrowly reread stop
`ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`
concerns unpaid global uniform domination and unread supplements.
No such supplement or global theorem is an input here, so that stop
neither blocks this standalone audit nor becomes resolved by it.

Decision: retain SPECIALIZE and approve the exact saved audit target's
source coverage. No essential source blocker was identified within this
scope. Full matching Mathlib coverage remains unchecked. The audit must
still independently check every listed analytic obligation and the direct
mathematical inputs in the local DAG. No lemma, mathematical script,
PROOF or DAG is changed by this review. Outcome STALLED records that
this separate gate confirms existing coverage without new mathematical
evidence or a changed research decision. The next turn defaults to the
already specified mathematical audit, not another literature approval.

## Retained audit specification

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate result is the already specified far-left integral, not a
new contour split or a global Mellin identity. A successful audit could
make this component available for separately assessed assembly with
L800/L801/L802. No sufficient sign implication is established.

Essential input IDs: L797, L798, L799 and L802, with L803 as the proof
under review. Their roles are the actual saddle and strict clearance,
phase and root normalization, normally convergent complete P, and
outward endpoint geometry plus the tangent inequality at u/2.
L800/L801 are downstream context only. No other notebook is an input.

Reuse the existing primary-source assessment without further browsing
unless a specific changed hypothesis or essential unread input is
identified. The recorded global-import stop remains in force; no
Derivation42/43/65/87 or source circle estimate is imported.

The bounded audit must reconstruct these load-bearing steps:

1. Verify the actual endpoint, principal Log and h=0 convergence using
   s=u(Q-c)>0. Distinguish pointwise existence from the uniform bound.
2. Retain the angular factor in W(v). For h>0 check t=Im(s)>0 and,
   when sigma=Re(s)<0, the inequality
   sigma v+t y_L>=sigma u+t h=|x|^2 Re(q-c)>0.
   Check h<0 by conjugation and h=0 directly.
3. Check the complete Gaussian sums for every tau>0, including the
   decreasing-integral comparison, the maxima used in exponent
   splitting, all constants and the 28u^(5/2)exp(-v/2) bound for P.
   No tau>3 premise or complex sign may enter.
4. Use L802's tangent inequality only at its valid endpoint u/2.
   Recompute the +tau_0 term in the exact W normalization, the
   805/4096-1/14=1/8+3/28672 margin and the exact C factor.
5. Check both closed boundaries, both signs of h, the h->0 regime and
   unbounded u. Verify the comparison with the original allowance and
   the direct mathematical inputs recorded in the local DAG.

Continue only if the full proof survives or a precise repairable
failure is identified. An error in this sufficient estimate does not
disprove T_F or RH. No global contour, vertical endpoint, quotient,
inversion, certificate or sufficient-sign conclusion may be inferred.
Those remain independent unresolved assumptions for future assembly.
Full matching Mathlib coverage is unchecked.

No justified central creative sign mechanism follows from this
component proof. The missing sufficient-sign connection remains the
blocker; the necessary conceptual audit is the concrete continuation.

