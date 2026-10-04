# Gaussian actual-frequency shrinking window — 2026-10-04

The saved large-frequency spectral target has ready SPECIALIZE coverage
in [the assessment](literature/2026-10-03-gaussian-regulated-first-spectrum.md).
This mathematical step reuses it; it does not start another source search.
The active notebook had no pre-existing changes, and other notebooks'
unfinished work is preserved.

The main gap is still actual-theta mixed positivity. The intermediate
target is actual realization of L363's displaced cancellation at the
same frequency as the gamma phase. An analytic negative value for every
sufficiently small regulator would stop this proposed first-sign
approximation certificate, while leaving RH and the actual-theta sign
unresolved. The required value error is O_R(1/log x), not a fixed
qualitative approximation error.

Proposed test: hold R fixed, freeze lambda at 1/omega(H), and choose
the L363 template with positive-real weighted derivative. On [H,2H]
omega changes by O(1), so this freezing costs o_R(1) in the cancellation
condition. Impose a fixed gamma-angle window, along with shrinking prime
phase windows. The Gaussian tail permits a cutoff
N=ceil(R sqrt(8 log log H)), eventually exceeding the template support.
Use L336's nonnegative finite Fourier bump to test visits to the joint
prime/gamma window. Prove its nonzero gamma harmonics are negligible
by an elementary stationary-phase split, retaining every prime harmonic.

Continue if the resulting arithmetic frequency bound proves a visit
or isolates a checkable substantially weaker arithmetic input. Stop
this implementation if its certified averaging budget exceeds the
window mass without such an input. The old coupled-endpoint failure
in L336 is a comparison, not an input asserting failure here: R is
fixed and the height is free in this different quantifier.

Unfinished checkpoint: derive the exact joint averaging bound, including
the infinite-tail error and the sign transfer. Compare its prime-log
separation requirement with the elementary integer-product bound.
Any stronger named logarithmic-form theorem is an unread lead until
a separate source assessment checks its statement and dimension growth.

## Completed test

The full proof is
[L364](../lemmas/L364-gaussian-joint-gamma-window-return-threshold.md).
Freezing lambda on a dyadic height interval costs o_R(1) in the
projected cancellation. A joint prime/gamma phase visit with width
delta_H proportional to 1/log H supplies an actual negative sign,
with the entire Gaussian tail controlled at that tolerance.

The finite Fourier average has error at most
2/(H Delta_H)+24/sqrt(H). The gamma term is adequate because
the window-mass lower bound beta_H has log(1/beta_H)=
O_R((log log H)^(3/2))=o(log H). The elementary integer-product
bound for Delta_H nevertheless cannot certify the required return:
its sufficient length exceeds H, even with optimized bump degree.
The outcome is NEGATIVE for that implementation, not for actual
occurrence. No actual negative value or new bad regulator is obtained.

The same proof isolates an explicitly conditional, weak prime-log
bound (LF). Its allowed separation constant grows like
exp(C N log(N+2)); at N=O_R(sqrt(log log H)) this would make
minus log Delta_H=o(log H) and suffice for the visit. No named
logarithmic-form theorem was read or applied. This is the precise
essential source need for the separate pending review, with
LITERATURE_REASON recorded in the compact checkpoint and assessment.

The step reproduces existing finite bump and gamma/sign tools and
supplies the elementary oscillatory split in full. No claim beyond
the checked literature, actual-theta positivity, or RH candidate is
made. The original phase-template distinction and all stopped
background and finite-scan attempts remain intact.
