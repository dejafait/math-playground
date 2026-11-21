# Fixed summable profile: head-tail working record, step 115

Approved target: Assess the head-tail mechanism for A_n(e)>=A_n(0)-o(n) when L666 uses truncations of one fixed real l1 displacement sequence with cap 1/8, retaining L657's complete charges.

Invocation-start coverage is EXPLORE in
`drafts/literature/2026-11-03-summable-displacement-complete-log-transfer.md`.
The supplied assessment is reused unchanged. This is one mathematical
attempt; no new literature approval or theorem is inferred.

Main gap: actual-Xi all-degree mixed positivity. The nearer target is
finite complete-logarithm transfer for the fixed summable profile
subfamily. L694 provides such a profile with an infinite Fourier gap,
but supplies neither finite transfer nor a tail rate. Full independent
cube, H/support and Xi realization remain independent unresolved steps.

Inputs inspected: L666's family and path differentiation, L657's
clearing/integrability and complete charge proof, L690's uniform
baseline, L692's sparse proof and audit, and L694's audited statement.
The scoped step 105 failure and working record rule out repeating its
uncertified n-dependent finite optimization as an asymptotic test.
All pre-existing active-notebook changes are preserved.

Bounded mechanism: pay a fixed head using L692's sharper inequality;
then test whether an analytic bound on the remaining dense summable
tail controls the negative logarithmic part uniformly as n grows.
The target is the ordered positive-part loss in the saved assessment,
or a rigorous fixed-profile linear-loss subsequence. Neither is assumed.
No singular-log differentiation or interchange of n and head limits
is licensed by pointwise closeness.

## Work in progress

For a fixed integer head radius H>=0, set K=H+1. There are at most
2H+1<=2K changed indices in e^(H). Once q is large enough that
n>=10^6 and K<=n/40000, L692 (2) and L690 (2) give

    A_n(e^(H))-A_n(0)
      >= -log 2-4K*log(5*n^2/(2*K^2))-epsilon_n,
    epsilon_n=64*n^2*exp(22-n/500) -> 0.

Thus this head lower loss is o(n) for each fixed H. If the proposed
ordered tail loss vanishes, subtract its positive part and take liminf
in q at this fixed H, before taking H to infinity. This is sufficient
for the desired lower liminf. This is a direct use of the existing
sharper bound, not yet a bound for the dense tail.

The remaining attempt was unfinished at this interruption checkpoint.
No lemma or target estimate was claimed there. The completion below
records what the subsequent bounded attempt actually established.

## Completed attempt: NEGATIVE, REPRODUCTION

The canonical proof is
`lemmas/L695-fixed-summable-tail-absolute-angular-cost.md`.
It combines the existing sharper sparse-head bound with an elementary
product specialization. There is no new general source theorem or
certified novelty claim, and no separate critical audit is asserted.

The finite head also has an n-independent upper bound at fixed H.
Consequently its complete mean divided by n tends to zero, and the
proposed ordered tail loss is equivalent to the original lower-liminf
target. The order of limits is justified, but the target is not proved.

The tested tail closure was a direct absolute/dominated perturbation
of that finite head. One fixed allowed sequence,
e_m=1/[16(m+1)^2] for m>=0 and zero otherwise, refutes the necessary
absolute-tail smallness. At the actual angle u=i the real ordinate
derivative of log|W| is >=n/1000 on 0<=y<=1/1000. For
m_n=floor(n/10000), the full spatial contribution of this single tail
index has supremum >=exp(n/10000000)/(8800*n^2), although the l1
tail is <=1/[16(H+1)]. This holds for every sufficiently large
admissible n at each fixed H, with the explicit onset in L695.
It is analytic evidence for a fixed profile, not an n-dependent
optimized vector, a floating screen or an extrapolation.

All M moments enter the polynomial whose constant coefficient bounds
its supremum. The bound concerns the sum of absolute individual
contribution norms, not the norm of the signed sum. Thus it supplies
no A_n countersequence and no negative-logarithm estimate. L657's
complete charges continue to apply. The exact rational comparisons
are written in the proof; no mathematical script or numerical premise
is needed. Structural validation is recorded in the history only.

The new information rejects this absolute head-tail closure under
summability itself, extending the earlier unsummable outward-pair
contour stop in a different and explicitly qualified direction.
Do not repeat a termwise absolute transfer or claim the full signed
head-tail mechanism is exhausted. This is one informative negative
mathematical attempt, with no supervisor counters edited.

## Proposed continuation, not attempted or approved here

A different signed test is a finite scalar consequence of an infinite
Fourier gap at a prescribed central frequency. At u=1 the rational
factors suggest a positive-convolution representation, in contrast
to bounding their individual displacement errors. A primary review
must first check that representation, the centered Lev prescription,
the non-Schwartz Fourier pairing and finite truncation charges.
The proposed estimate is |c_0(1)|<=C*exp(-c*n) for fixed profile
and gap. This would be a concrete finite transfer test, but a single
small coefficient at one angle would leave all spatial moments,
angular means, A_n, H/support and Xi realization unresolved.

The exact pending target and unresolved hypotheses are saved in
`drafts/literature/2026-11-03-fourier-gap-positive-convolution-transfer.md`
with REVIEW_REQUIRED. No representation, concentration bound,
prescribed-center existence or scalar estimate is established by
this continuation proposal.
