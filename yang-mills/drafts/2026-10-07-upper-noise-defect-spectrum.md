# Upper-face conditional defect — working record

Approved target: Compute the g^2 log(sqrt(tau)/a) coefficient of the remaining response Cov(O_i, V_a S_g - J_3 - J_6) for L010's two Wilson-flow probes, including action, measure, and flow corrections.

STEP_ID: YM-20261007-065-upper-noise-defect-spectrum

Main gap: cutoff-uniform interacting normalization and reflected error
<=c_box/2 remain unproved, independently of continuum and infrared gaps.
Intermediate test within the unchanged SPECIALIZE assessment: resolve the
operator I-K in L049's Z, retaining all transverse end edges, before
trying to bound the complete -kappa(f,r,Z+R)+E group at a^2 scale.
Downstream use: separate the exactly suppressed gradient part from the
undamped curl part and identify a possible boundary-symbol estimate.
Continue on an exact spectral rate usable in contractions; abandon a
uniform small-defect shortcut if an actual high-frequency sector retains
an O(1) defect. No cumulant sign or compensation follows from a norm alone.

Existing coverage: drafts/literature/2026-09-26-current-target.md, SPECIALIZE,
unchanged before invocation. L049 already proves only 0<=K<=I and
I-K>=P/N. L026/L029 supply the actual spectrum and zero-axial-mode lift;
ATTEMPTS/011–013 stop raw-link, tensor-only and interior-extension bounds,
not this boundary covariance calculation. No duplicate exact defect
symbol was found in the relevant local proofs/drafts. Standard
finite-dimensional spectral functional calculus is reused; the specific
all-face boundary block must be computed rather than copied from a bulk
flow-renormalization theorem.

Unfinished reasoning saved before calculation: let Delta_T be the relative
transverse edge Hodge Laplacian and P=T3 G3 T3^T. The last axial edge
cosine weights and last axial vertex sine weights obey sine^2=lambda_n
cosine^2 for n>0. A prospective identity is
I-K=P/N+b_N(Delta_T)(I-P), with
b_N(lambda)=1/N+(2lambda/N) sum_(n=1)^(N-1)
cos^2(n*pi/(2N))/(lambda+4sin^2(n*pi/(2N))).
This is not yet established here. End edges and zero component indices
must be checked before using it. R, E, cross-plaquette pairs, other jets,
and the complete power/logarithmic coefficient remain unresolved.

Completed: L050 proves the prospective full-edge identity, its scalar
hyperbolic resolvent formula and the bound b_N(lambda)<=1/N+sqrt(lambda).
Low physical modes have an O(a) defect; a zero-divergence eigenmode and,
more decisively, a realizable four-vertex Q circulation rule out uniform
smallness. The latter gives Z/q_A>=7/16 at every N>=4. The fractional
energy representation replaces the stopped blanket-smallness shortcut;
it does not control the full random product or its signed cumulant.
Seven exact rational, three exact integer and five numerical diagnostics
pass with no failures in the saved upper-noise-spectrum certificate.
No actual-probe contraction, scaled cancellation or logarithm is computed.

Continuation under unchanged ready coverage: contract L050's explicit
b_N(Delta_T) kernel against the actual f_(i,0),r_0 exterior matrices in
L049's Z+R group, retaining E and all remaining plaquette pairs. Essential
inputs are L011, L018, L026, L029, L048, L049, L050; L030/L047 set the
a^(-2) comparison and L019 governs the full nonlinear jet compensation.
The fractional product energy, derivative terms and cross-plaquette
response have no established scaled bounds or limits. Continue only on
a justified signed bound/limit; abandon replacing the full Q by its low
spectral projection or dropping R/E. Independent continuum, reflection,
infrared and finite-mass gaps remain. ATTEMPTS/011–017 are preserved.
