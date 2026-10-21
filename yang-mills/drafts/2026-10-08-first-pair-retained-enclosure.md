# Bounded retained-enclosure attempt

STEP_ID: YM-20261008-093-first-pair-retained-enclosure

The saved SPECIALIZE assessment `literature/2026-09-26-current-target.md`
is reused unchanged. Main gap: the complete interacting response and
logarithm, followed by matching and the reflected error <=c_box/2.
Intermediate target: enclose both L072 diagnostics at N=24 with total
absolute error <=1. Downstream use is guidance for the direct first-pair
analysis, conditional on the still unproved original-trace reduction.
Continue only on a fully retained enclosure; an interval excluding zero
certifies only this finite diagnostic, and an interval containing zero
does not certify zero. If the enclosure cannot be made concrete, reassess
this mechanism rather than substitute samples.

Inputs checked: L008's exact discrete coefficients, L070 section 6,
L071, L072, the preceding working records and ATTEMPTS/016 and 022.
L072 reuses L033's resolvent integral; existing integer interval and
midpoint-radius routines may be reused, but their continuum Fourier
error constants do not apply to the present lattice spectrum.

Unfinished plan saved before implementation: construct the one-dimensional
matrices with outward intervals, transform their finite tensor factors
using the explicit relative sine/cosine bases, and evaluate the double
heat integral by a positive Gauss rule on dyadic panels. Prove a uniform
single-resolvent quadrature bound before contracting the two copies.
Retain the edge zero modes, all components, prefix factors, transition
weights and both tails. No spectral truncation or random trace is allowed.

Essential inputs for continuation: L008, L018, L026, L033, L070, L071,
L072. Unresolved assumptions: centering/path replacement, axial
normalization and variable-coefficient/pinned-boundary trace errors.
Other mixed placements and response jets, the logarithm, continuum
fields, reflection positivity, infrared control and positive finite
mass remain open. No complete candidate is present.

Completed result: [L073](../lemmas/L073-first-pair-diagnostic-enclosure.md)
certifies -200.408<D_3<-200.362 and -20.752<D_6<-20.210 at N=24.
The actual total errors are below 0.022571 and 0.270823 versus 1.
The full certificate and factor archive are under
`scripts/combined-ward-response/first-pair-retained-enclosure-*`.
The final all-record audit has 22929 passing checks, 7680 primitive heat
entries, 1157704 saved factor entries and all 100 trace products.
An initial audit serialization error (NumPy boolean) was repaired; it
was not a mathematical failure. Independent finite-array M/Q comparisons
are implementation diagnostics only. The proof uses exact rule errors,
integer input enclosures and the explicitly qualified IEEE propagation.

L037/L039's interval and Gauss machinery was reused with fresh lattice
inputs and a separately justified uniform resolvent budget. Their old
continuum Fourier bounds were not imported. The outcome is ADVANCE /
RESEARCH / REPRODUCTION: a local finite-diagnostic threshold is now met,
with no claim of mathematical originality or an original response
coefficient. Mathematical exploration usage resets to 0 after L073.

The next bounded subtest under the same unchanged approved response
assessment is the original circulation/path centering defect: in
L070(1), replace only the exterior t_l,2,t_l,3 coefficients by the
sums/differences of opposite-edge averages on the same plaquette;
retain t_l,1 and every covariance, residual, axial factor and pinned row.
Derive its exact defect and test an O(N²) bound for its complete actual
heat sum. A proved bound would control one replacement step only;
L073's signs do not license any axial normalization or principal-trace
identification. If the estimate still loses a power, record the precise
uncanceled term and stop that replacement bound rather than declare a
nonzero original coefficient. Essential inputs: L018, L026, L064,
L066, L069, L070, L073; the assumptions listed above remain unresolved.
No new assessment was written or approved in this research step.
