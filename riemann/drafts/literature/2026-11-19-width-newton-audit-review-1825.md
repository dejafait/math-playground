# Width Newton specialization: independent audit source approval1826

TARGET: Audit C033z extension1825's uniform width inverse-root error<=2^-60 and complete<=100-operation contract, including initialization, endpoints, the1802 input perturbation and panel clamps.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused1823's exact-statement, stronger-result and obstruction search; inspected C033z lines1-42,416-474,1463-1623 and the1823/1824/1825 execution/source/construction histories. The audit preserves the assessed target domain and arithmetic model; no broad search repeated.
SOURCE_EVIDENCE: Reopened Brent-Zimmermann, Modern Computer Arithmetic v0.5.9(2010-10-07), Lemma3.14 and its complete printed proof, p112(PDF page128), plus Section4.2.3(4.9), p129(PDF page145); reused1823's Algorithm3.9/Lemma3.15 and Kornerup-Muller exclusions.
COMPARISON: The primary exact-error statement matches the theorem imported in1825. Its positivity hypotheses and existential intermediate theta are explicit; it supplies neither this rational initializer nor the eight-step bound,94-operation ledger or1802/clamp interface. Those remain independent local audit obligations.
GAP: No essential literature gap remains for this bounded audit. Independently verify normalization/endpoints, positive iterates and theorem applicability, first-step estimate, seven error-envelope updates, the complete count and1802 perturbation/clamps; no audit conclusion is certified here.
REASON: Separately approved the saved audit scope by reusing adequate source coverage and checking the exact primary statement against the new constructor. This completes a source gate without new mathematical evidence or a novelty claim.
SCOPE: Audit of the exact width-only constructor on rational[1,2^30] in C033z's rational-operation model. It excludes any global evaluator cost, bit complexity, rounding other quantities, scalar execution, interpolation and actual-Xi inference.

## Source comparison and retained limits

Primary source: [Brent-Zimmermann, version0.5.9, Lemma3.14,
printed p112](https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf#page=128).
The inspected statement assumes a,x>0, sets rho=a^(-1/2), and bounds
rho-x' for the exact update x'=x+(x/2)(1-a*x^2), with theta between
x and rho. Its complete proof uses Taylor's theorem for a-t^(-2).
Equation(4.9) identifies the same iteration. No extra closeness or radix
hypothesis occurs in this lemma; positivity of each subsequent input
still needs the local induction. The source does not certify the local
contract by itself, so SPECIALIZE rather than IMPORT is appropriate.
Do not reprove the general error theorem during its application audit.

The exact discovery queries, inspected seed-analysis qualifications and
unread leads remain in1823's assessment. No changed source hypothesis
requires a new search. The relevant failure remains the1823 unrounded
execution stop:15/780 profiles,0/8 scalars, six independently replayed
profiles in1823b. It is not a Newton impossibility theorem and supplies
no numerical input here. This source review neither reopens that stopped
execution nor approves denominator/runtime control. No independent
signed-height/actual-Xi mechanism is available from this bounded scope;
routine width arithmetic does not justify a creative nomination.

## Approved audit evidence and test

Canonical proof: C033z, "Optional width-only Newton replacement1825".
Exact checks and complete evidence:
`scripts/smoothed-law/width_newton_1825.py` and
`scripts/smoothed-law/width_newton_1825.json`.
The original source assessment already distinguishes the exact lemma from
integer Algorithm3.9, rounded arithmetic and approximate-seed optimization.
The separate approval1826 reuses this coverage. This document approves
the audit scope; it is not an independent proof or a passing audit.

The decisive audit test is simultaneous validity of the uniform error
and full<=100 count, with original width perturbation/clamps paid and
endpoints included. A failure should identify the precise invalid claim
and its effect, preserving the constructor and all historical evidence.
Retain C033y's divisor/conjugation/multiplicity, excluded ordinate0,
strict strip/gamma>14, counting/real-zero/tail and heat qualifications,
both fixed-v1 qualifications, zero drift/killing and Gaussian half-variance.
No1823 suffix value is an input. Conditioning, weights, TV<=2,
observation coverage, signed-height cancellation and actual-Xi realization
remain independent gaps. Full matching Mathlib coverage is unchecked.
