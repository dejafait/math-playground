# Continuation: conceptual audit of the fixed neutral screen rejection

TARGET: Audit C750a's fixed neutral good-frequency screen rejection, checking exact moments, complete-symbol sublevels and interval mass bounds.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed861 and recovery862's exact target searches, known-method comparison and scoped failure checks; no new theorem, window, witness, optimization or weighted observation target is nominated. Separate source-scope approval864 completed; the conceptual audit itself remains unexecuted.
SOURCE_EVIDENCE: Reuse https://arxiv.org/html/1802.07942v1 Section2 callback contract and step2 for real interval boxes; https://dlmf.nist.gov/5.5.E2 and https://dlmf.nist.gov/5.11.E2 with https://dlmf.nist.gov/5.11#ii for recurrence and complex remainder, as inspected in861/862; Plancherel and integral monotonicity. Local C750a, L744(6)-(8), L750 Proof1/3 and its step317 audit; certificate-315.cpp elementary routines, fixed-witness-863.cpp and its complete selected certificate fields.
COMPARISON: The witness, moment-ratio construction and integral methods are known. Audit the rescaled specialization and its rejection direction only; no general positivity theorem or concentration improvement is supplied or needed.
GAP: Independent conceptual verification of exact-a admissibility, whole-panel interval callbacks, all 31 prime powers, digamma sector errors, frequency reflection and sided mass comparison remains undone. The calculation reports rejection but is not independently audited.
REASON: Required separate literature approval864 confirms essential coverage for this exact audit; this repeats the known-method decision and claims no mathematical advance. The conceptual audit is now ready, without another approval turn.
SCOPE: Only C750a and its fixed T=4log3 witness, level1, complete symbol and selected J. No retuning, alternative witness, full good-set decomposition or inference of negative Weil energy/RH.

Coverage is reused from
`drafts/literature/2026-11-13-neutral-good-frequency-fixed-witness-861.md`.
That prior assessment was saved before step863 and authorized its concrete
calculation. This continuation changes the task to scrutiny of the resulting
proof and certificate; it introduces no uncovered mathematical mechanism.
The required separate approval was completed in step864 below; this paragraph preserves the original nomination context.

Inspect the exact hypotheses and proof in C750a, then the elementary routines
actually called by the new program. In particular verify the inherited
Taylor remainder domains and sector-remainder specialization, rather than
trusting a successful process exit or requested tolerance. Read the full
retained-box and prime-power evidence with the JSON inspector; previews do
not suffice. Spatial and frequency boxes enclose integrands over whole
panels, and stored dyadic endpoints are nominal integration intervals.
Enlarged callback evaluation ranges must not become extra integration mass.

The bounded acceptance test is whether one exact admissible witness and
all certified inclusions justify c_E<=317/330<36/37<=M/(M+1). Any unpriced
interval error, missing term, faulty moment identity or inequality-direction
error must invalidate or repair the local certificate before accepting the
screen stop. Passing means a verified negative result for this coarse
screen; it does not mean Q<0 or RH. No independent implementation is required
by this target, but the limits of reused arithmetic must remain explicit.

Essential input IDs: C750a, L744 and L750. The old T=8log3 numerical values
are not inputs. No RH, H2-prime tail, complement positivity, cross-notebook
input or Xi realization is assumed. Mathlib full matching coverage is not
checked. New source coverage is needed before any weighted signed mechanism;
none is approved by this audit continuation.

Recommended subsequent research routing: proof_audit/conceptual_audit,
deep_research/xhigh, REPRODUCTION. Exact neutrality, full symbol normalization,
interval Fourier mass and the reversed rejection comparison interact; an
ordinary arithmetic replay alone cannot audit the logical claim.


## Separate source-scope approval864 — 14 November 2026

LITERATURE_REASON: The invocation explicitly requires separate approval of
step863's newly written audit continuation. No additional research target
or changed mathematical hypothesis is introduced.

DECISION remains SPECIALIZE, now ready for the exact TARGET. This is source
approval only: C750a's reported rejection and implementation are unaudited.
Outcome STALLED honestly records no new mathematical evidence and no new
literature conclusion beyond the reused coverage. It does not undo step863.

Primary passages inspected directly in this approval:

- Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
  arXiv:1802.07942v1, 22 February 2018,
  [Section 2, callback contract and steps 2–3](https://arxiv.org/html/1802.07942v1),
  and Section 2.1. The direct-box branch requires enclosures over the entire
  interval; only the Gaussian branch imposes an analytic ellipse. Requested
  tolerances do not replace returned error bounds. This covers the chosen
  real-panel method, not the custom binary64 callbacks or any saved value.
- NIST DLMF, current online text accessed 14 November 2026,
  [5.5.2](https://dlmf.nist.gov/5.5.E2),
  [5.11.2](https://dlmf.nist.gov/5.11.E2) and
  [5.11(ii), first paragraph](https://dlmf.nist.gov/5.11#ii).
  Recurrence is used away from poles. The asymptotic expansion is stated
  in sectors separated from the negative real axis; the complex digamma
  remainder retains the secant multiplier with exponent 2n+1. Checking
  the truncation index, shifted argument and actual panel domains is the
  audit's obligation, not a result imported from an asymptotic symbol.

The exact-target discovery/overlap assessment861 and its source recovery862
are reused; no new searches or novelty claim are needed for the same scalar
inputs. C750a, L744(6)–(8), L750 Proof1/3 and the relevant step317 audit
passages were read to compare coverage. L750's old window values and energy
certificate are not inputs. The recorded strict-screen stop863 was checked
for scope: no universal energy obstruction or negative-energy conclusion
is authorized. Single-band concentration results remain background overlap,
not missing essential inputs. No essential source is blocked.

Next-turn obligations remain exactly those in the nominated audit: inspect
all relevant complete certificate records and actual called routines; check
exact-a admissibility, full prime-power list and symbol normalization,
whole-panel mass enclosures, reflection and comparison direction. Reusing
an arithmetic library is not independent verification of its application.
A failed load-bearing enclosure requires repair or withdrawal of this local
stop. No audit verdict is supplied here. Full matching Mathlib coverage
remains not checked. No lemmas, mathematical programs, PROOF or DAG changed.
