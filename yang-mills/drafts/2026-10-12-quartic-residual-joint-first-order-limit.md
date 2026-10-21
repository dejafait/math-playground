# Quartic residual: joint first-order limit attempt

The gate-approved target remains the complete quartic covariance for both
actual probes in `literature/2026-10-12-quartic-residual-insertion-cubic-scale.md`.
The main gap is the interacting reflected comparison and subsequent
continuum/infrared construction. This attempt tests existence of its
signed cubic limit, retaining all five contributions in L150(11).

Starting inputs are L149 L150 L151, L008's fixed-mode coefficient
convergence and L028's smooth forest lift. L085/L114 enter through the
local covariance comparisons already proved in L150/L151. L010/L011
fix the exact jets; L019 still prohibits assigning this isolated term
a forest-independent meaning. ATTEMPTS/009, /011 and /036 are preserved.
The unchanged ready assessment is reused, with no new literature search.

Reasoning saved before the proof: define a continuum exterior
two-point kernel from the full heat-mode sum of the normalized forest
columns. Establish uniform C^1 convergence on the compact insertion
support, keeping the constant axial prefix. Expand displacement and
exterior samples at their actual link midpoints; use L151 only on the
frozen covariance difference. The other differences and the two signed
insertion tensors should then have ordinary compact-support Riemann
limits. This would give a finite functional without assuming its value
or cancellation. The key audit is that convergence of the frozen exterior
kernel needs no O(a) rate: its coefficient is multiplied by a tensor
whose completely frozen contraction vanishes exactly at every mesh.

Continue if all remainders are uniform little-o after the a^3-scaled
sum, yielding a finite signed functional suitable for actual-probe
evaluation. Abandon this reduction if a surviving unsuppressed kernel
or uncontrolled first-order normalization prevents that limit. Existence
alone leaves the requested zero value, other response jets, finer powers
and logarithm, full compensation, matching and all construction gaps open.

Completed: [L152](../lemmas/L152-quartic-residual-joint-first-order-limit.md)
proves a finite real cubic limit Lambda_i for both actual probes. Its
formula (8) retains all five contributions and every exterior heat mode.
Uniform C^2 exterior-kernel convergence is obtained from L008's actual
coefficient comparison and the exact finite-prefix extension. No O(a)
rate for the frozen kernel is needed because its contraction vanishes
exactly at every mesh. L151 supplies the summed covariance-slope error.
No value, sign or zero limit has been established, and no mathematical
script was needed for this analytic reduction.

Continuation within the unchanged approved target: contract L152(8)
jointly with both actual probes, using L149's exact finite words and
L151's phase-correct local projection and slope. Essential inputs are
L008 L028 L114 L149 L150 L151 L152; L010/L011/L017/L018/L026 conventions
and L019's compensation constraint remain. Do not assume that surviving
first-order tensors vanish separately, that u is affine throughout its
support, that the constant axial prefix disappears, or that the complete
response is finite termwise. Any numerical tensor preview would still
need rigorous error control before establishing a value or sign.

The discriminating test is a signed cancellation of the full functional
for both actual probes, or a certified nonzero actual-probe value. A
tensor contraction identity may simplify the evaluation, but arbitrary
test vectors do not determine these two heat-weighted contractions.
If further parity alone only recovers finiteness, abandon that shortcut
and evaluate the retained tensor. All other jets and construction gaps
listed above remain independent and unresolved. No candidate exists.
