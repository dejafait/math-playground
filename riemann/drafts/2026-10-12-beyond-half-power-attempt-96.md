# Step 96 — stronger scalar moment specialization

The gate-approved target is the unchanged beyond-half-power test in
`literature/2026-10-12-beyond-half-power-positive-discriminant-large-values.md`
(prior SPECIALIZE). The supplied overview/DAG and source assessment were
used before reading L403 in full and the necessary L390/L391/L401 ranges.
Narrow October 12 records show no prior use of the stronger scalar input
in a local concentration proof. L394/L399/L400's weight failures remain
preserved; this uses L401's already positive exact direction.

Working calculation, not yet a completed result: put d=520/445121,
fix epsilon=d/2, and p=2-d/2. The cited scalar twelfth moment has budget
H^p. The pole-canceled entire Gaussian window from audited L403 has right
boundary O(H), smaller than H^p since p>1. Its two left-boundary tails
have summable factors 2^((12+p)j) exp(-4*4^j), so no height saving is
lost. Uniform small-shift functional equation and normalized Cauchy
transfer should give integral U^6=O(H^p) for ordinary orders 0,1,2.
With complete Y=Delta[Re(R zeta(5/2+it))f]^2, the bounds |Y|<=C U^2
and integral Y>=c H log^4 H would yield
meas{D>0}>=c H^((3-p)/2) log^6 H.

Pass condition: check every analytic-strip hypothesis, both infinite
tails, all radius-1/log H shifts and the Omega' term with H-independent
constants and all-real-H quantifiers. Stop if any height-power loss
consumes d/2. No lower weight bound, independent carrier or response
truncation is permitted. This could constrain discarding positive
discriminant exceptions, but global mixed positivity, the total L367
margin and actual common-zero upper counts remain independent gaps.

The scalar input is de Faveri–Pandey arXiv:2610.01035v1, Theorem 10.1,
p. 18, imported as an unconditional preprint theorem as covered by the
saved assessment; its full proof is not independently audited here.
Do not claim a stronger local result until the applicability argument
is written in a canonical lemma and checked.

## Completion

The full applicability argument is now canonical in
`../lemmas/L404-beyond-half-power-positive-discriminant-measure.md`.
It proves (1)-(3) with p=2-260/445121 and delta=130/445121, so
the target is met with K=0. The tail sum, right-boundary comparison,
small shifts, normalized ordinary jets and exact physical Holder
restriction introduce no height-power loss. This is a local known-tool
reproduction; separate critical audit is pending. The preliminary
calculation above is retained as the pre-completion checkpoint, not a
second canonical proof. No mathematical script was needed.
