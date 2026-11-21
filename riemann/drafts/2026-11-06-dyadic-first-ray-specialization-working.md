# Dyadic first-ray specialization — working checkpoint

2026-11-06. One RESEARCH/proof_attempt under the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-11-06-dyadic-cubic-infinite-tail-first-ray.md`.
Only its exact weak first-ray target is being attempted. L030–L032/C032a
actual-Xi mixed positivity remains the main gap; higher shifts and Xi
realization are independent. No new source search or second mechanism.

Relevant finite proof and audit read: L840, m=1, theta=pi/3. The exact
polynomial is P(w)=1+2w+2w^2+w^3. Macdonald's normalized reciprocal
identity identifies its first ray with h_n=[t^n]1/P(-t), h_0=1.
L840 gives period six and h_0,...,h_5=1,2,2,1,0,0. Thus every factor
1/P(-2^(-j)t) has nonnegative coefficients, including its zero classes.
For F_M=product_(0<=j<M)P(2^(-j)z), coefficients of 1/F_M(-t) are
finite Cauchy convolutions at each fixed degree and are nonnegative.
This uses scalar coefficients, not a closure assertion for solid rays.

Remaining proof obligation before completion: compact convergence of
F_M, nonvanishing on |t|<1, reciprocal convergence on any closed disk
|t|<=rho<1, and Cauchy coefficient passage. Factorization uses elementary
parameters 1,exp(i*pi/3),exp(-i*pi/3), each scaled by 2^(-j); their
absolute values sum to 6. The assessed compact-product theorem applies.
For fixed r, pass both the reciprocal coefficient and the finite
determinant to the limit; no rank/product interchange or division by
a solid minor is needed. Do not extend this to strict signs, PF order,
full-support certification or k>=2 in this turn.

Known stops compared: the finite all-ray/PF stop in
`ATTEMPTS/2026-11-06-finite-pf-all-ray-weak-detector-stop.md` and the
all-fixed-shifts source assessment. Bultheel remains parked. The finite
zero residues do not obstruct convolution, but limiting transfer still
needs writing. Completion means a proof for every fixed integer r>=1;
otherwise record the exact failed passage and stop.

## Completion

The remaining compact convergence, nonvanishing, reciprocal convergence
and fixed-rank passage were completed in
`lemmas/L841-dyadic-cubic-product-nonnegative-first-ray.md`.
That canonical proof establishes the exact weak first-ray target for
all ranks; this preliminary reasoning is retained as the working record.
The higher-shift continuation is separately nominated REVIEW_REQUIRED;
it has not been derived or approved here.
