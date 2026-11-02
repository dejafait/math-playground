# Anchor-line attempt — work in progress

Invocation target: Test the anchor-line C645g bound ||H_q||>=c exp(-n/32) at delta=1/4, eta=1/100 and M<=n/3, using a phase-sensitive Hardy functional or an admissible line-supported asymptotic counterfamily.

The unchanged EXPLORE assessment
`drafts/literature/2026-11-01-anchor-line-hankel-census.md` covers this
attempt. C645g's exact definitions/scaling and C645k's audited planar
stop were read, along with the reused primary Hardy/residue coverage.
Existing notebook changes are preserved. No cross-notebook input.

Main gap: actual-Xi signs/all-degree mixed positivity. This synthetic
test could supply or refute a detector for an isolated common-real-part
layer; isolation, other-pole control, census/clearance, realization,
independent upper bounds and signs would remain separate.

## Unfinished mechanism

Keep d=5/4, R=11/8, x=-d. Try n=3m with m odd, and m unit-residue
poles a_k=x+i*r*cos((2k-1)*pi/(2m)), 1<=k<=m, r=1/2. They are
distinct, include x, and satisfy |a_k|<=sqrt(d^2+r^2)<R-1/100.
Unlike the circle counterfamily, every real part is exactly x.

The finite average is the Gauss--Chebyshev node average. An elementary
residue kernel on an ellipse may bound its error from the arcsine
average with a factor rho^(-2m), retaining all complex B_n phases.
Tentative ellipse: horizontal semiaxis s=1/10, vertical semiaxis
sqrt(r^2+s^2), centered at x; rho=(sqrt(r^2+s^2)+s)/r. It appears
strictly inside |z|<R. Neither its uniform error nor a final rate has
yet been certified.

For the continuous arcsine average, try deforming the vertical cut to
the left arc of |v|=sqrt(d^2+r^2) joining x-i*r to x+i*r. On that arc,
the exact factor modulus is smallest at the upper endpoint. A gain
log|B_n(x+i*r)/B_n(x)|>n/32 would make this part small. Endpoint
square-root singularities must be handled explicitly; a scalar moment
or a finite numerical screen cannot settle the full-norm target.

Remaining bounded test: certify both exponential rates strictly above
1/32, and the full-boundary norm with constants uniform in n; otherwise
retain the precise failed estimate without asserting a counterfamily.
No bound or RH candidate is claimed at this checkpoint.

## Completion of this attempt

The unfinished calculations above were completed as
[C645l](../lemmas/C645l-anchor-line-chebyshev-hankel-counterfamily.md).
The exact four-quarter grid gain gives exponent 3/80, and the finite
Chebyshev-node error has exponent 37/897. The resulting bound is
||H_q||<720*n*exp(-3*n/80) for n=3m, m odd >=3. The claimed uniform
exp(-n/32) lower bound therefore has an explicit synthetic obstruction,
subject to the separate conceptual audit. The full proof, hypotheses,
source qualifications and verification record are canonical in C645l;
this draft preserves the pre-calculation checkpoint, not a second proof.

Exact-rational certificate:
`scripts/one-sided-hankel/anchor-line-chebyshev-check.json`.
All checks passed; the full relevant table, coefficient and rate values
were inspected. No numerical spectral screen or Xi realization was used.
