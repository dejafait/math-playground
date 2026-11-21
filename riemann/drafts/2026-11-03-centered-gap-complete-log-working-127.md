# Complete logarithmic centered-gap attempt — step 127

Invocation target: assess whether every fixed L698 profile satisfies
limsup A_(12q+3)/(12q+3)<0, retaining the full angular complement and
all M spatial moments. Prior ready assessment:
`literature/2026-11-03-centered-gap-complete-logarithmic-sign.md`
(EXPLORE, supplied at invocation). One mathematical attempt; no new
source assessment is being substituted for it.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
a paid signed full-mean estimate for this fixed centered-gap family.
Downstream use: decide whether L698's arc decay challenges the
fixed-profile complete-mean mechanism; H/support and Xi realization
remain independent unresolved gaps.

Inputs read: L698 hypotheses/conclusion and fixed-arc mechanism;
L666 family/rational continuation; L657 clearing, integrability and
complete divisor identity; L690 anchor comparison; L697 complex
factors; L694 summable-profile hypotheses and construction interface;
L683 finite spatial identity. Recorded comparisons: L695 absolute-tail
stop and the parked step-105 signed finite screen. Neither supplies
a centered-gap counterprofile. No cross-notebook input.

Test: bound the signed angular complement at order n, using its actual
rational structure. Continue only with a paid complete-mean inequality
or an admissible fixed-gap counterprofile. An informative quantified
compensation bound is a permissible intermediate result. Stop if the
estimate depends on absolute tails, unproved cancellation, omitted
roots, or a generic growing-degree propagation loss. A positive upper
bound does not refute the universal negative-rate assertion.

Preserved initial reasoning: L657 gives A_n=m_0+Z_n-P_n and absolute
logarithmic integrability for each finite n, including torus zeros and
cancelled poles. L698 supplies a negative linear upper bound on one
arc. The complement cannot be discarded. A fixed finite-head comparison
does not justify a logarithmic limit for an l1 tail. Any full-mean
argument must either keep that cancellation or pay its lost charge.

The direct extension of L697/L698 remains unpaid: its normalized positive
convolution law and exponentially small escape probability are local
to the selected angular arc. Off that arc the product of complex-measure
variation masses is not controlled by the gap estimate. No signed
complement bound follows. This is not an additional obstruction theorem.

Bounded discriminating calculation: approximate L694/L696's same
prescribed-center Picard construction on two Fourier grids, then
evaluate the complete finite G at several increasing allowed n. Record
the actual finite gap residual, profile cap, all shifts, angular and
spatial quadrature refinements, signed arc/complement contributions,
and independent product/root checks. The nominal cutoff width is not
certified against L694's existential coefficient constant; finite
Fourier residuals do not certify a distributional gap for an infinite
profile. Thus this screen is directional evidence only, never an
admissible counterprofile, even if its approximate full mean is positive.
The same largest-grid shift array is fixed before every tested n.

## Completed bounded calculation

Outcome: EXPLORATION; completed kind RESEARCH, classification REPRODUCTION,
actual task type calculation. The construction and finite G formulas
reproduce existing local inputs; the screen establishes no new lemma,
asymptotic sign, admissible counterprofile or progress beyond those inputs.
The analytic full-mean question remains open. PROOF.md and DAG.md are
unchanged by this step.

The full diagnostic and every retained shift, Picard iteration, sampled
frequency residual and angular spatial-log mean are in
`scripts/one-sided-hankel/centered-gap-complete-log-127.json`.
Reproduction commands from the notebook root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/one-sided-hankel/centered-gap-complete-log-127.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/one-sided-hankel/centered-gap-complete-log-127.py --verify
```

The optional `--scalar-probe` mode records the same probe without replaying
the independent product checks. No dependency was installed. `mpmath`
was unavailable; the independent point checks instead use Python Decimal
at 60 digits and direct finite products/sums.

### Profile approximation and its essential qualification

The prescribed center is omega_*=1.0850734174001688, or
c_*=0.17269479799685228 cycles. A smooth cutoff equals one on the
central half of each support interval, with nominal half-support width
w=0.03815583839748182 cycles and gap radius pi*w=0.11987010160108824.
Use L694's Phi, equal to one on [-3/8,3/8] and supported in
[-7/16,7/16], and its exact reflected data
Q(t)=-exp(-pi*i*t)*chi(t)/(2*pi*i*t), with zero value near t=0.
The sampled Picard map is L694's T -> Q-R(coefficients(T)), with the
nonlinear exponential series retained through degree 14. The FFT grids
have 4096 and 8192 points. This describes the implemented finite
approximation, not a convergence theorem for it.

The larger-grid maximum shift is about 0.104257, below 1/8; its finite
signed correction 1+sum_m exp(i*v*(m+1/2))*expm1(i*v*e_m), checked at
61 off-grid frequencies across the nominal gap, has maximum modulus
8.66e-15. The smaller-grid residual is 1.26e-10. Central 1024 shifts
change by at most 1.12e-15 between these two grids. The same larger-grid
profile is fixed before all tested n; it is not optimized separately
for n. The complete arrays and finite l1 sums are saved.

These are approximation checks only. The chosen w is not verified
against L694's existential coefficient constant C_Lev and invariant-ball
radius. No infinite Fourier tail, exact distributional gap or contraction
error bound is certified. In particular, extending the saved finite
array by zero does NOT produce a proved L698 profile. Small sampled
Fourier residuals cannot replace that hypothesis. L694/L696 establish
existence of other exact sufficiently narrow profiles; they do not
identify this numerical array as one of them.

### Complete finite response and logarithmic screen

For each n retain exactly -2q<=m<2q, the fixed anchor, unit masses,
the j=0 product factor, angle 1/u and M=n/3 spatial coefficients.
The script forms the actual finite rational W values and all M
coefficients, evaluates the complete polynomial by FFT on the spatial
circle, and averages log modulus without a logarithmic regularizer.
It uses angular/spatial grids 256x512 and 512x1024 with different
angular offsets, and 1024x2048 at n=771. No spatial root or angular
pole is analytically discarded by this computation; the samples are
not a rigorous quadrature of the singular logarithm or a zero census.

Largest-grid estimates at each n:

| n | approximate A_n | approximate A_n/n |
|---|---:|---:|
| 51 | -0.506402 | -0.00992944 |
| 99 | -0.778338 | -0.00786200 |
| 195 | -0.799044 | -0.00409766 |
| 387 | -0.947309 | -0.00244783 |
| 771 | -1.055945 | -0.00136958 |

At n=771, the angular positive and negative contributions to the
sampled spatial-log mean are approximately +0.530570 and -1.586515.
Thus both signs occur; a negative-arc plot would omit positive
compensation. The fixed diagnostic arc |theta|<=0.10 is not asserted
to be L698's existential arc. Its sampled contribution and the full
complement are separately saved at every tested size. Their sum equals
the total to roundoff. No compensation rate is proved.

The final n=771 quadrature refinement changes the estimate by
0.000109921. The earlier refinements at n=195 and 387 change it by
about 0.00362 and 0.00398, respectively. Such differences are not
error enclosures. At n=51 and 99, all spatial roots at 256 angular
samples are additionally evaluated with both complete root formulas;
their residuals and comparison errors are saved. In particular the
n=99 spatial root mean differs from its spatial-grid approximation
by 7.28e-7. These root checks do not certify the angular integral.

The largest scalar cancellation condition at n=771 is about 25381.2
on the 512-angle grid and 26777.8 on the final 1024-angle grid.
Three independent direct-product, direct-finite-spatial-sum
checks at 60 decimal digits have relative discrepancies 2.07e-11,
1.01e-10 and 4.95e-14 against the floating implementation, below the
diagnostic threshold 1e-6. They include theta=0 and the angle with
largest scalar cancellation on the 512-angle grid. All 11 complete sampled-mean arrays
are finite; arc/complement and positive/negative accounting errors
are at most 2.23e-16. Both saved diagnostic failure lists are empty.
These point and accounting checks are not interval certificates.

### Decision and bounded continuation

The evidence cannot distinguish a small negative limiting rate from
a zero rate, and it does not provide a rigorously admissible profile.
Do not extrapolate the decrease of |A_n|/n or extend this finite screen
as the next research step. The direct complex-variation extension is
also left unpaid. Preserve the exact universal full-mean target as
open, together with L695's distinct absolute-tail stop.

A scalar probe of the same n=771 approximation gives angular mean
log|c_0| about -1.057417, versus -1.055835 for the full polynomial on
the same 512-angle grid. This motivates a narrower prospective
counterprofile certificate based on the scalar whole-circle logarithm.
L666 Section 4 already provides the pointwise spatial Jensen comparison;
its primary input is Brunault--Zudilin, *Many Variations of Mahler
Measures*, Propositions 1.4--1.5, pp.6--7, including boundary roots,
with the precise citation and qualifications canonical in L657/L666.
Any scalar whole-circle lower-bound application must retain logarithmic
integrability and scalar angular zeros. No such asymptotic bound is
derived or approved here.

The sole next action is the exact scalar target in the pending
`literature/2026-11-03-centered-gap-scalar-complete-log-lower.md`.
That different observable requires a separate literature comparison;
the assessment remains REVIEW_REQUIRED. Inputs are L666/L657 for the
finite family and logarithms and L694/L696 for an exact fixed-gap
profile. L698 motivates the compensation problem. The finite numerical
profile is not an input satisfying their gap hypotheses. This is one
mathematical EXPLORATION attempt in the continuing compensation route;
narrowing the observable does not reset its budget.

Mathlib: no new matching coverage was checked. Reuse only the supporting
one-variable Mahler/root-formula references recorded canonically in
L657/L690; neither this numerical experiment nor the proposed scalar
asymptotic is a formal theorem. No absence claim is made.
