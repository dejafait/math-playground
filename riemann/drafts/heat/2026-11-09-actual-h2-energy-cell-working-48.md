# Step48 working checkpoint — fixed actual H2 energy cells

The pre-existing EXPLORE assessment is
`drafts/literature/2026-11-09-actual-h2-energy-cell-test-46.md`.
This is one research attempt on its exact target; no source refresh,
parameter/degree/cell/precision sweep, optional positive multiplier or
reopening of stopped enclosures is authorized.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: the fixed convolution density for
M_0(lambda)^12 det H2(lambda), followed by the stipulated 32 cell masses.
A certified alternating triple would obstruct this normalization's
at-most-one-sign-change premise. Otherwise report uncertainties and
stop without refinement. A full crossing bound and independent endpoint
signs could support finite-degree contact exclusion; other degrees,
contact/tangency, initialization, realization and global continuation
remain independent gaps.

Essential inputs read: L019's exact positive theta kernel, L058's
compact domination, L874's local-log convention, and L917's six finite
Newton polynomials and determinant formula. The approved assessment's
duplicate and source reviews are reused. L915/L916/L922/L936/L937 are
contrasts only. No cross-notebook input. Existing changes are preserved.

Proposed construction, not yet verified: put
f_k(E)=E^(k-1/2)K(sqrt(E))/(2(2k)!), k=0,...,6.
Its exponential transform is M_(2k)/(2k)!. Expand the determinant in
normalized moments and homogenize to ordinary degree 12 with M_0.
Every monomial would then be a 12-fold one-sided convolution, with
weighted degree 12. Verify all coefficients before use. Singular
f_0 at zero requires a simplex domination proof; no univariate
quadrature theorem automatically covers this construction.

Outstanding: exact polynomial, full-kernel absolute exponential
moments, final continuity, a nonzero interval, and rigorous cell masses
with all theta and integration errors. No sign or representation is
claimed at this checkpoint. Mathematical scripts must save complete
certificates and concise actual/required bounds and failures.

## Algebra checked; single numerical budget fixed before invocation

The exact script independently expands the finite logarithm: all six
residuals vanish. There are 34 terms, weighted degree 12, and maximum
ordinary degree 6 before homogenization. Thus the prescribed M_0^12
works; do not remove its extra M_0^6 factor. The constant-K simplex
coefficient is exactly zero, so crude independent convolution bounds
would erase relevant cancellation.

Use one degree-256 Chebyshev interpolant to k(x)=K(sqrt(x)) on [0,8],
257 root nodes, theta terms 1 through 8, 200-digit directed arithmetic,
128-term Machin arctangents and cosine Taylor terms indexed 0 through 128.
Round its Chebyshev coefficients to integer multiples of 10^-120;
pay their full certified errors. No adaptive changes or reruns at a
different budget. The energy ellipse rho=3/2 maps under sqrt to
|Im u|<=1/sqrt(3), |Re u|<=5/sqrt(3)<3; even analytic extension and
the full theta series must justify the interpolation error. A proposed
safe complex bound is 10^9, with error <=8*10^9*(2/3)^256 before
coefficient errors. Real |K|<=7 must be proved separately.

Convert the rational interpolant to power coefficients exactly. Its
12-fold convolutions are exact finite beta integrals: integrate the
resulting polynomial on the 32 prescribed cells using integer/rational
arithmetic, keeping all cancellations. Propagate the uniform kernel
error through the complete 34-term polynomial using an explicit
absolute simplex bound. This does not invoke old univariate quadrature
code as a theorem for a new singular integral. If the bounds do not
certify a triple, stop without refinement and retain every uncertainty.

## First-pass arithmetic failure; same-budget repair

The exact-rational checker rejected cell 1: a Decimal endpoint was
negated with ambient precision 28 in two I(-er.hi,er.hi) expressions
(cosine remainder and final cell error). All first-pass signs and
approximation enclosures are invalidated. The script, main certificate,
exact polynomial and exact failure are preserved as
`scripts/heat/actual-h2-energy-cell-first-pass-48.py`,
`scripts/heat/actual-h2-energy-cell-first-pass-48.json`,
`scripts/heat/actual-h2-energy-cell-polynomial-first-pass-48.json`, and
`scripts/heat/actual-h2-energy-cell-first-pass-failure-48.json`.
Only exact `copy_negate` replaces those operations. Rerun the identical
degree/precision/theta/node/cell budget; this repairs invalid arithmetic,
not a failed valid sign bound or a numerical refinement. No output
sign is accepted until the complete final-enclosure checks pass.

## Completed fixed attempt

The corrected run passes 969 exact-rational consistency checks:
cells 0–1 negative, 2–14 positive, 15–31 uncertain; no alternating
triple. The full proof, exact normalization and all qualifications are
canonical in L938. This working file preserves the pre-calculation
budget and arithmetic recovery; it is not a second proof or current
next-action record. The independent conceptual audit remains pending.
