# Deeper-band arithmetic moving-saddle attempt

The approved target is the exact TARGET in
`literature/2026-10-24-deeper-band-moving-saddle-coverage.md`.
This is a RESEARCH / REPRODUCTION attempt using the already inspected
interpolation and simple-saddle mechanisms, not a new literature turn.
Existing unfinished work is preserved.

The main gap is initial low-index signs and global mixed positivity.
The intermediate target is a positive arithmetic margin on the closed
band 13/16<=m/r<=7/8, with a positive factorial-normalized scale having
sublinear logarithm and a complete relative o(1) remainder. A separate
theta reduction and height transfer could use it for lower logarithmic
indices; neither is part of this attempt. Continue only if every reserved
disk and contour contribution passes on this whole band with one onset.

Pre-completion checkpoint: L456's larger normalized-logarithm domain
allows R1=282/256 inside R2=284/256, with R0=255/256 and
R3=286/256. The exact inequality 282^16<255*284^15 gives an
interpolation power below 15/16. The nominal endpoint is 29/32,
at distance 280/256 from 2; adding 8d for d=1/4096 leaves
3/512 to R1. Thus fixed Cauchy reserves are available. Prospective
bounds are Q^(j)=O(r^(15/16)), saddle displacement O(r^(-1/16))
and |log M*|=O(r^(15/16)). These do not yet establish the full
arithmetic conclusion: factorial normalization, the shrinking annulus,
the complete middle range, both remote-height-zero neighborhoods,
unbounded rays and both original residues remain to be checked.

Essential inputs are L452, L456 and audited L457's method. The pinned
September 30 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a` remains a conditional
external input, with strict Re(s)>7/8, the allowed pole at one and
unaudited manuscript/import closure. The prior source/overlap assessment
and input register were read; the ready assessment's L323/L327/L331,
fixed-center and fixed-r/unit-phase comparisons were reused. They do
not decide this coupled moving-saddle target. No changed-band theta
estimate, initial-index sign, bounded-height result, mixed positivity or
selected-law/regulator realization is assumed.

Completed: the full derivation is canonical in
[L459](../lemmas/L459-deeper-band-uniform-moving-saddle-margin.md).
The changed logarithm exponent p=15/16 gives displacement O(r^(-1/16))
and |log M*|=O(r^(15/16)); the factorial scale remains positive.
The shrinking annulus has a quadratic relative decay estimate, while
the entire fixed outer region costs exp(-kappa*r+Cr^(15/16)).
Both remote-height-zero neighborhoods, both infinite rays and the
two original residues cost at most 2exp(-r^2) in total relative error.
The complete relative rate is O((log r)^3/sqrt(r)). All 17 exact
constant checks pass in the full disk certificate under
`scripts/deeper-band/`; its interpolation and complete check values were
inspected with the shared JSON inspector. These checks do not verify
the analytic argument or external premise. A separate critical audit
is nominated with REVIEW_REQUIRED scope; no audit is claimed here.
