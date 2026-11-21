# Approved frequency-weighted Xi specialization — working record

2026-11-08, step115. One mathematical attempt under the unchanged
SPECIALIZE assessment in
[the source comparison](literature/2026-11-08-frequency-weighted-xi-defect-interpolation.md).
The target is its exact COVERED_TARGET, including the closed height square,
power 5 and exponential rate pi/2. No new source assessment is needed.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Possible use: absolute interpolation against independently proved positive
reference margins on frequency bands. Those margins, relative small-value
control and global/all-degree signs remain open.

Provisional reasoning saved before the final proof: use L320 (6) with
R=1, giving an entire even product bounded by
E_1(2+|x|)^(9/2) exp(-pi|x|/2) on the unit height circle. Cauchy bounds
each even Taylor coefficient by this quantity. For t=y^2, the series
for H'_x(y)/y has bounds 2M_x/(1-t)^2 and derivative
4M_x/(1-t)^3; t<=1/4 should give 32M_x/9 and 256M_x/27.
L898 identifies the removable value with C_0(x).

For the real normalizer, reuse L899 (6): the logarithmic sinhc
difference is at most p^2|t-s|/6. The real mean value theorem for
exp should bound the raw-density difference by
p^4 sinhc(p/2)Phi(u)Phi(w)|t-s|/6. Its integral is Q|t-s|/6,
with finite Q already justified in L899. Keep both quotient terms
and the lower bound A_0>=a=A_0(0)>0. No complex normalizer is divided.

Continue only if these estimates retain all original thresholds with
one finite constant; otherwise preserve the failed estimate and park
this envelope. No sign or Xi nonvanishing premise is allowed.

Existing changes were inspected only within this notebook. L898's
fixed-endpoint stop and the supplied comparison with L309/L312 remain
intact. The scoped exact-terminology search found no earlier matching
frequency-weighted normalized two-height lemma; this is not a novelty
claim. L899 is the unweighted benchmark. No mathematical script is needed.

Completed: the provisional route succeeds with all original thresholds.
The full proof and finite constant are now canonical in
[L900](../lemmas/L900-frequency-weighted-normalized-xi-defect-interpolation.md).
This working record is preserved; the separate audit is still pending.
