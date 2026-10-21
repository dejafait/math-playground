# Coordinate-Haar cubic-scale critical audit

Approved target and prior assessment: determine whether L018's complete
coordinate-Haar response has a vanishing a^3-scaled limit for both actual
L010 probes in the straight lower-rooted forest;
`literature/2026-10-12-coordinate-haar-cubic-scale.md` is unchanged EXPLORE.

The main gap is still the ultraviolet-uniform interacting comparison,
followed by the continuum axioms and infrared/finite-mass construction.
This audit tests whether L148 legitimately removes this one same-forest
compensation source for L147. Accept its bound only if the normalization,
all-mode consistency and full pinned-row norm all hold. A missing power
that leaves only O(a^-3) would reopen the zero-limit claim. No other
response term is being estimated in this step.

Saved audit findings before final documentation:

- L011(7)--(8) gives the negative density insertion M2=|x|^2/12.
  L018(8)--(9) gives 8 for the quadratic third cumulant, hence -2 after
  three colors. Its lifted trace is used with its original factor order.
- L018's dimensionless covariance is a^-2 times the physical inverse.
  The probe and residual matrices each carry a^2. L148's whitening
  therefore leaves a^-2 in C=a^-2 Delta^-1/2 R_F* R_F Delta^-1/2.
  The coordinate conversion x=a A_stored and orthonormal vector
  A_orth=a^2 A_stored agrees with this independent check.
- L028 proof section 1 explicitly proves its estimate for every allowed
  mode. Centered differences, averages, coefficient products and reversed
  adjoints admit the stated telescoping Taylor remainder. The total
  derivative count is five. L009(15) supplies the zero continuum operator
  after polarization; the coefficient support removes boundary terms.
  L028's later restriction on smooth forest lifts is not used by L148.
- L026(6)--(7) retains the zero own-direction mode and three positive
  vertex indices. The physical gap 3/16 follows from sin(t)>=2t/pi on
  [0,pi/2]. The resulting polynomial Gaussian series controls the full
  one-sided trace norm with its a^2 rate, not merely individual entries.
- L026(2) pins the prefix potential on the upper face before incidence
  is applied. L148's prefix Cauchy--Schwarz and incidence-degree count
  include those rows. No smooth extension through that face is needed.
- L008 proof section 1 and (8)--(9) bound both whitened probe forms.
  The product in L148(10) uses E B, E R and C in their actual order;
  it puts no heat on C and needs no unsmoothed small residual norm.

No counterexample, missing hypothesis or incorrect power was found.
The completed canonical audit is in
[L148, proof section 5](../lemmas/L148-coordinate-haar-vanishing-cubic-scale.md).
It accepts the existing analytic bound without changing the argument,
so PROOF.md and the DAG require no changes. This is verification,
not a new estimate, error repair or originality claim. The step is
RESEARCH / REPRODUCTION / STALLED in the mathematical-progress taxonomy.

The proposed next target is the complete kappa_0(f_(i,0),r_2) term of
L011(6), whose polynomial is specified by L011(13). Local source screening
does not establish coverage of its isolated cubic scale. A separate
REVIEW_REQUIRED assessment records the target and essential inputs;
no derivation of that new term was attempted or approved here.
