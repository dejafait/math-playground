# Quantitative prime-gap arithmetic discriminator — assessment1117

TARGET: Test whether modulated prime-gap probes detect Polson's finite off-line perturbation with an explicit positive signal and polynomial strip-norm cost, uniformly in the insertion height.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed comparison1117 screened three mechanisms and searched the exact perturbation, arithmetic-support defect and modulation terminology locally and externally; no matching quantitative bound was located. The source already gives qualitative detection, so no novelty claim is made.
SOURCE_EVIDENCE: Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24, https://arxiv.org/pdf/1708.02653v24, Theorem12.2(vi)/(53) pp36-37 and complete Fourier/support proof, Definition9.1/Proposition9.3 pp30-31; Tao, 245C Notes2, 6April2009, https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ Section3, Exercises29-30/38, Example33, equation(11) and its inversion proof.
COMPARISON: The cited source already excludes exact logarithm-supported arithmetic for its finite surgery. The changed requirements are an explicit height-uniform signal for the fixed modulated family and a polynomial cost in the source's fixed strip norm; known Fourier inversion/decay tools apply, but these two bounds were not derived during review.
GAP: Produce explicit constants and all parameter-uniform estimates, or identify failure of this exact probe/cost threshold. This would be a quantitative calibration, with no actual-Xi sign theorem, infinite-perturbation conclusion or positive-square representation.
REASON: Adequate source and overlap coverage exists for one bounded mathematical specialization after separate approval. Do not spend a turn merely reproducing nonzero defect or finite-block positivity.
SCOPE: Only the fixed bump/probe, finite surgery K, g>=G and 0<=B-A<=2 defined below; the delta=1/4 source strip norm. No all-degree positivity proof, zero verification, source stability reproof, arbitrary support campaign or mathematical script is required.

## Exact proposed mathematical test

Set a=4/5, b=9/10. Let chi(x)=Z^(-1)
exp(-1/((x-a)(b-x))) for a<x<b and zero otherwise, with
Z the positive normalizing integral. This fixes one smooth mass-one
bump; it is not an optimization variable. Its support lies inside
(log2,log3). Use the K,A,B,g of comparison1117, with
g=(A+B)/2, 0<=B-A<=2, and g sufficiently large. The source's
actual zero-occurrence hypotheses are retained whenever asserting
that K is the defect of its entire F; estimates for the displayed K
may be tested for every real A,B in this parameter domain.

On the real line define the even test

    eta_g(x)=chi(|x|) cos(gx),
    h_g(r)=integral_R eta_g(x) exp(irx) dx,
    phi_g(z)=h_g(sqrt(z)).

Seek explicit constants c_chi>0, C_chi<infinity and G_chi>=1000,
independent of A,B,g, for which, whenever g>=G_chi,

    integral_0^infinity eta_g(x) K(x) dx >= c_chi,
    ||h_g||_(1/4) <= C_chi (1+g)^3,

where the source norm is

    ||h||_(1/4)=sup_(|Im r|<=3/4) (1+|r|)^(9/4) |h(r)|.

Constants may be explicit expressions in finitely many specified
L1 norms of chi and its derivatives; existential Riemann-Lebesgue
onsets or unbounded-in-g constants do not pass. Verify entire even
extension, strip decay and membership of phi_g in the source class,
and keep the source's factor -2 in the arithmetic measure and factor
4 in the full zero-sum difference. Do not identify a full zero sum
with the reflection-paired half sum without its factor.
These are proposed thresholds and obligations, not established bounds.

## Why this specialization, and what is already known

The support argument and exact defect formula are imported from
Theorem12.2, rather than reproved as a new result. The source's
qualitative compact-test proof does not supply the height-uniform
constants or this norm bound. Those additional requirements justify
the quantitative calculation. It need not audit the finite heat-block
estimates, choose actual ordinates numerically, or use an RH premise.

Tao's Exercise30 assumes a function and its derivative in L1 with
the fundamental-theorem-of-calculus property; it gives the derivative
Fourier identity. Example33/Exercise38 concern smooth compact support
and Schwartz decay. Equation(11) applies to Schwartz functions; its
proof uses Gaussian approximation and continuity on Schwartz space.
His convention has 2pi in the exponent, so use the displayed probe
convention consistently. For strip bounds the calculation must check
the corresponding compactly supported exponential weights uniformly
for |Im r|<=3/4; real-axis decay alone is insufficient. The source's
pp36-37 proof supplies the entire/strip admissibility framework.
No unread Paley-Wiener statement is an essential premise.

The plausible downstream use is a measured arithmetic discriminator
that a future actual-Xi estimate must retain while finite heat signs
cannot distinguish this family. This is modest: qualitative exclusion
of these finite surgeries is already known. The probes are signed,
depend on the insertion height, and are not L030 polynomial squares.
No implication to Q positivity or to exclusion of infinite coordinated
changes is assumed. Graph realization and all degrees remain open.

Continue only if both quantitative thresholds and admissibility hold.
If the signal cannot be uniform, the norm costs more than the stated
polynomial, or only source-level qualitative detection is obtained,
record that failure without changing the probe or silently weakening
the target. Success merits a canonical qualified proof and one later
audit, not an automatic RH route. This is routine quantitative
specialization/reproduction, not a protected creative attempt.

Essential local context: L030/L032/C032a and C030b; source inputs
are the precise passages above. Mathlib matching coverage is not
checked, and no absence is asserted. No cross-notebook input.
This assessment was written in a literature-only turn; its ready
continuation requires separate next-turn approval, not same-turn work.
