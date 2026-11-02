# Joint angular/spatial Fourier dual: bounded attempt

Prepared STEP_ID: 2026-11-02-joint-fourier-dual-01.
Invocation-start coverage: `drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`, unchanged EXPLORE.
Task: RESEARCH / proof_attempt / creative.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Approved intermediate target: the uniform angular Hankel lower bound
at exponent 1/32 for the common-pole anchor-line family. The concrete
test is the previously nominated two-circle Fourier polynomial with
angular indices |k|<=2n and spatial modes -1 through -(2n+1).
Seek real unit-pole response >=1 at x and >=-3/(2n) everywhere on
the allowed line segment, with norm <=C exp(n/32). Positive integer
anchor residue and M<=n/3 would then pay for the allowed negative
responses. This is a sufficient test, not an equivalent criterion.

Downstream use: a detector for arbitrary admissible common-pole
families. Xi layer isolation, other-pole control, census/clearance,
simultaneous rotated realization, an independent norm upper bound and
all-degree signs remain unresolved. No RH candidate is proposed.

Inputs read: C645g's normalized symbol and constant-input inequality;
C645o's exact angular product and pole cases; C645p's projection and
ambient zero-evaluation cost. The last two supply recorded obstacles,
not positivity premises. The supplied ready assessment and the prior
joint-dual nomination are reused. Scoped searches of their working
notes and ATTEMPTS found the entrywise-positivity and zero-evaluation
stops, which this joint finite dual is intended to test differently.
No new source theorem is needed at this checkpoint.

Continuation/abandonment test: construct a uniform continuum-certified
witness at the required exponential cost, prove an informative lower
obstruction for this restricted dual class, or preserve a materially
refined mechanism. Finite numerical optimization alone is exploratory;
neither a grid of poles nor an angular sample certifies the target.
This note is a checkpoint before the mathematical attempt, not evidence
that the desired dual exists.

## Partial reasoning saved during the attempt

A possible obstruction to the proposed *linear* dual uses positive
fractional Gaussian lattice weights, with central weight one and total
mass O(sqrt(n)). These are not admissible integer residues and cannot
refute the angular detector. They can nevertheless test constraints
imposed separately on every unit-pole response: those inequalities also
sum against any positive real weights of the same total mass.

Take a_j=x+i*j/n, weights exp(-j^2/n), and retain |j/n|<.54. For
each spatial index 0<=ell<=2n, try a residue rectangle with vertical
sides Re(a)=-11/8 and -9/8 and horizontal sides halfway between
lattice nodes. The exact kernel 2*pi*n/(exp(2*pi*n*(a-x))-1) has
unit residues at the lattice. All poles of W_a as a function of a
are to the right of this rectangle. On its left side |a|>=R, so
|W_a|<=max_u |B_u(x)|; Gaussian growth costs exp(n/64).
C645n's candidate pointwise bound with rate lambda>.047 would leave
rate >.031375, just larger than the target .03125. The right side
has exponential lattice-kernel damping. Horizontal sides require a
uniform radial product lower bound, including the spatial modes.

This is incomplete: all four contour sides, finite-node cutoff,
normalization, total mass and the dual implication still need proof.
The saved numerical diagnostic suggests a usable horizontal margin
near height .54, but supplies no certificate. Its output is
`scripts/one-sided-hankel/joint-dual-contour-diagnostic.json`.

## Completed attempt

C645x contains the complete proof of an obstruction to this dual.
The finite Gaussian lattice has central weight one and total mass
<=n/3, but fractional noncentral weights and more than n/3 distinct
poles. Its spatial coefficients through degree 2n are uniformly
<=4n exp(-251n/8000). Summing the proposed unit-pole inequalities
against these weights forces dual norm
>=exp(251n/8000)/(8n sqrt(2n+1)), which exceeds C exp(n/32) eventually.
No admissible countersequence or full-symbol upper bound follows.

All 20 exact constant/rounding checks passed. The full selected
rounded bounds, all comparisons and the empty failures field were
inspected using the shared JSON inspector. The numerical diagnostic
was not used as proof. The analytic contour proof and dual implication
remain independently unaudited; outcome NEGATIVE records an informative
local method obstruction, not a new RH result.

The exact comparison is in C645x and its full certificate at
`scripts/one-sided-hankel/joint-dual-contour-certificate.json`.
The route is parked in
`ATTEMPTS/2026-11-02-joint-fourier-dual-fractional-lattice-stop.md`.
No continuation construction is attempted in this turn. The next
bounded task is to audit C645x's four contour cases and its implication
for the proposed dual under the unchanged ready angular target.
Its essential inputs are C645g's normalization, C645o's exact rotated
product and C645n's pointwise anchor maximum. The obstruction must not
be extended to integer-residue families or to the full operator norm.
