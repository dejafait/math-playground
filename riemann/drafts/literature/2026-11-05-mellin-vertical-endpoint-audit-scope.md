# Continued vertical endpoint: conceptual-audit source gate

TARGET: Assess source coverage for an independent conceptual audit of L804's fixed-height continuation, pole qualifications, circle bound and normalized endpoint estimate on D, including h=0.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step537 reuses step534 exact-target searches and step535 URL repair, compares all L804 proof operations with that coverage, and narrowly searches Mellin histories/assessments and the global-import stop; no broad search or novelty inference. No mathematical audit is performed.
SOURCE_EVIDENCE: Reopened Zagier author PDF Section1 pp1–2, subtraction identity after (2), https://people.mpim-bonn.mpg.de/zagier/files/tex/MellinTransform/fulltext.pdf; DLMF 2.5.17/25 https://dlmf.nist.gov/2.5#ii, 1.9.30–31/48 and series M-test https://dlmf.nist.gov/1.9, 1.10.18–19/integral M-test https://dlmf.nist.gov/1.10#viii, 5.9.1 including conditions https://dlmf.nist.gov/5.9#E1. Reuse step534 paper23 v1 Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23, and post20 https://rstation.ai/r/riemann_hypothesis/posts/20; these author claims are not independent verification.
COMPARISON: The inspected standard methods cover the fixed-ray Taylor implementation and real Gaussian moments used by L804; its elementary sum, phase and limiting estimates are written locally and remain audit obligations. No unread circle-quotient derivation or global Mellin theorem is essential to this component audit.
GAP: Method coverage is approved; independently check the fixed-ray exponent/orientation, normal convergence, actual versus possible poles, full-series circle estimates, two phase regimes, both closed boundaries of D and the actual h=0 limit. Mathematical correctness and the sufficient-sign bridge remain unverified.
REASON: The separate literature gate for completed L804 finds no essential uncovered method; approve only a conceptual audit classified REPRODUCTION. Source coverage alone cannot certify the parameter-specific estimates or advance RH.


SCOPE: Coverage approval completed in literature-only step537; the exact covered audit below is ready for a later mathematical turn. No proof reconstruction, lemma edit or mathematical script was performed.
COVERED_TARGET: Critically audit L804's fixed-height meromorphic continuation and uniform normalized vertical endpoint bound on the closed domain D, including pole qualifications, both height regimes, conjugation and h=0 compatibility.
LITERATURE_REASON: The saved REVIEW_REQUIRED gate requests a separate source-hypothesis comparison for the completed Taylor-series proof, replacing a proposed compact-circle implementation; reuse the prior assessment and inspect only the relevant primary methods.

## Completed method-coverage comparison — step537

The original nomination is retained below as historical scope. The main
RH gap remains actual-Xi all-degree mixed positivity. The intermediate
target is independent scrutiny of the endpoint component, potentially
usable in a separately assessed Mellin assembly. This source gate
approves the audit method, not L804's inequality.

The source record is step534's completed endpoint-scope assessment,
its step535 repair and the Gaussian-method comparison in the far-left
horizontal scope. Those records give the source versions (DLMF v1.2.8,
15 September 2026; Zagier appendix to Zeidler, Springer 2006, pp305–323),
queries, inspected author claims and exact height/domain mismatch.
Step537 reopens only the relevant primary methods, accessed 5 November
2026, and reads L804 to identify its operations rather than verify them.
No new exact-theorem discovery is claimed.

[Zagier Section1, PDF pp1–2](https://people.mpim-bonn.mpg.de/zagier/files/tex/MellinTransform/fulltext.pdf),
identity after (2), subtracts a power expansion at zero. Its whole-ray
statement assumes rapid decay at infinity; only the finite-interval
subtraction is needed here. L804 proposes an analytic Taylor expansion
on a disc and rescaling of a fixed oriented ray. Checking its branch,
exponent change, order compatibility and residues is the audit's work.
No imaginary-ray decay theorem is required.

[DLMF2.5(ii), (2.5.17), (2.5.25)](https://dlmf.nist.gov/2.5#ii)
requires local integrability and a zero-end asymptotic expansion whose
real exponent parts strictly increase to infinity. Its truncated
transform has the stated principal parts. This corroborates the method;
the separate convolution and large-end assumptions are not imported.

[DLMF1.9.30–31](https://dlmf.nist.gov/1.9#iii) requires continuity
within/on the simple closed contour and analyticity inside. Together
with [1.9(vi), (1.9.48)](https://dlmf.nist.gov/1.9#vi) it covers
Taylor coefficients and absolute uniform convergence on smaller discs.
The series M-test is in 1.9(v). L804's proposed circle and clearance
must satisfy these hypotheses; the source gives no effective theta
circle constant.

[DLMF1.10(viii), (1.10.18)–(1.10.19) and integral M-test](https://dlmf.nist.gov/1.10#viii)
requires parameter analyticity and joint continuity; at a singular
endpoint convergence must be uniform on compact parameter sets.
An integrable majorant independent of the parameter suffices. The
statement treats a right-end singularity; reversing the finite interval
permits the zero endpoint here. The audit must check L804's proposed
compact majorants. It must not infer analyticity of the moving-height
composite from this fixed-parameter theorem.

[DLMF5.9.1](https://dlmf.nist.gov/5.9#E1) gives the gamma integral
with Re(nu)>0, mu>0, Re(z)>0 and principal powers. Its real Gaussian
cases cover the moment method used in L804, which cites L798's real
Gaussian integral and integrations by parts. Checking beta positivity,
the sum-to-integral comparison, boundary terms and constants remains
mathematical work. Euler–Maclaurin and Abel–Plana are not used by L804.

The inspected paper23/post20 comparison from step534 is unchanged:
the author's old detailed height/domain cases and later endpoint
assertion do not independently prove L804's actual-height estimate.
Derivation87 remains unread and is not needed to audit the local
Taylor proof. Its possible quotient-denominator singularities are no
longer a required proof case because L804 does not use that quotient.
The canonical proof instead asserts the Taylor poles, including an
actual pole at -1/2, which the audit must inspect without parity
cancellation assumptions.

Narrow Mellin-history/assessment searches identify L804 as the completed
component and L803 as a different, horizontal component. The automatic
global-import stop in ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md
remains valid; it is no obstruction to this standalone audit. No broad
source search, blocked-supplement retry or new duplicate theorem claim
is justified. Full matching Mathlib coverage remains unchecked.

The covered audit must independently replay L804's equations (2)–(23),
checking every use of L797/L798/L799/L802 in context, with special
attention to the complete P series, the circle strictly inside its
strip, negative real parts, conjugation and the limit as h tends to
zero with u unbounded. It must cover both closed boundaries of D and
the exact denominator, not a sampled or asymptotic substitute. These
are audit instructions, not verified conclusions of this review.

Continue only after a complete audit supports the stated exp(-Q/2)
allowance, or preserve a specific error with its scope and consequences.
A failed majorant is not a counterexample to the bound or RH. Global
contour equality/budget, quotient/inversion, certificates and sufficient
signs remain open. No justified new central creative mechanism follows
from the endpoint component: the missing sufficient-sign bridge is
the blocker. This gate completion supplies no new mathematical evidence;
record STALLED, without claiming an exploration or recovery reset.

## Original step536 nomination (historical, superseded by approval above)

The main gap remains actual-Xi all-degree mixed positivity. L804 is a
standalone endpoint component for a separately assessed Mellin assembly.
It is an unaudited source reproduction, not an RH candidate or evidence
of progress beyond the checked sources. The uniform endpoint proof is
the output of step536, and is not to be rederived in a literature turn.

The canonical result uses L797 for the saddle/domain, L798 for the
phase and Gaussian normalization/moments, L799 for the full holomorphic
P series, and L802 for the actual outward height. Its proof constructs
fixed-y continuation with possible poles s=-(n+1)/2, and residue p_n/2;
the actual pole condition is p_n!=0, without a parity assumption.
The chosen circle has radius pi/4-13/(224u). The proof pays a full
series bound and treats 0<|h|<=1/2 by the convergent integral and
|h|>1/2 by the continued Taylor series, followed by the actual h=0
compatibility argument. These are audit subjects, not independent
verification supplied by this nomination.

The source-gate test is whether the already inspected subtraction,
Cauchy, parameter-integral and Gaussian methods cover precisely these
operations. If yes, approve one independent conceptual audit with
explicit scope and exact target; if not, name the essential unread
hypothesis or theorem. Do not repeat broad browsing or unread-supplement
requests. Full matching Mathlib coverage remains unchecked.

The later mathematical audit should accept the stated endpoint bound
only after checking all load-bearing cases, or identify and preserve a
specific error. It must distinguish a failed estimate from a false
endpoint claim. Global contour equality and combined budget,
quotient/inversion, certificates and a sufficient actual-Xi sign
implication remain unresolved. L803 is downstream context only, with
no premise imported into L804; no cross-notebook result is used.

No central creative sign mechanism is justified by this endpoint
component alone. The missing sufficient-sign connection is the specific
blocker; the necessary audit is not to be relabeled creative.
