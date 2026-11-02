# Joint full-grid projection — correlated angular moment attempt

Prepared STEP_ID: 2026-11-02-joint-angular-moments-research-01.
The invocation-start EXPLORE assessment is
`literature/2026-11-02-joint-full-grid-polynomial-dual.md`, unchanged
and supplied verbatim. The exact approved target remains its joint
projection inequality; this is one bounded mathematical attempt.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs. Intermediate target: the uniform squared rate 1/16 for the
joint full-grid projection relative to L649's D_single,n. By L651
this is equivalent, with changed constants and onsets, to the same
rate for S_n=mean_u sum_(k<M)|c_k(u)|^2. A successful bound could
supply a sufficient constant-input detector comparison. Matching upper
bounds, Xi realization and signs remain independent unresolved steps.

Keep n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n; common distinct
Re(a)=x poles with |a|<=R-eta including x; original positive integer
residues r_a of total mass M<=n/3; all n grid factors, conjugated
denominator angle and normalized angular/spatial means. No separation,
symmetry, coefficient-integrality or fractional-mass relaxation.

Inspected L651's full proof, L649's coefficient/coisometry definitions
and proof, and L650's full polynomial response and cost. Reused the
ready primary-source comparison. Targeted local comparisons retain
the separate-column, prefix, exact-recovery, entrywise-positivity and
constant-grouping stops. The latter does not rule out an exponential
relative comparison. No stopped conclusion is promoted into a global ban.

Bounded test: retain all first-M spatial moments and the complete
angular correlations, then test whether the integer-mass constraint
limits cancellation at the required exponential rate. Continue only
with a uniform rate, a full admissible countersequence, or a further
quantitatively bounded response cost. An unevaluated Gram minimum,
nonvanishing or a finite numerical screen is not decisive.

Unfinished reasoning saved before lengthy work: the remaining matrix
is the angular Gram of W_a(u) times the first-M geometric spatial
kernel. Nearby poles make individual isolation costly, but L650 shows
that joint sums can remove that cost. The question is whether angular
concentration and cancellation for growing integer families can still
produce loss faster than exp(-n/16). I will first seek a finite-algebra
way of retaining the correlated phases, testing any proposed estimate
against the known Chebyshev and near-cluster mechanisms. No new bound
or counterexample is asserted at this checkpoint.

## Completed bounded calculation

Outcome: EXPLORATION. No uniform lower bound, admissible asymptotic
countersequence or new quantitatively bounded response cost was proved.
The main positivity gap and the rate-1/16 joint target are unchanged.
No lemma, DAG row, argument overview or source assessment was changed.

The calculation evaluated L651's complete first-M spatial moment energy
and L649's exact diagonal on sampled angular circles. In particular it
did not use a first-M grid prefix, normalize isolating columns, omit
spatial modes from S_n, discard signed cross terms, or replace the
original residues by fractional masses. These are new finite tests of
this relative quantity; they are not a mathematical advance or a claim
of originality beyond the source comparison.

Three parts tested the same cancellation mechanism:

- `scripts/one-sided-hankel/joint-angular-moment-screen.py` tested
  centered unit-residue Chebyshev families at n=51,99,195,387 and radii
  0.2,0.3,0.4,0.5,0.54, using all M=n/3 spatial moments and 1024
  angular samples. The largest apparent squared loss rate
  log(D_single,n/S_n)/n was about 0.025484, at n=51,r=0.3.
- `scripts/one-sided-hankel/joint-angular-shifted-screen.py` tested
  shifted Chebyshev clouds plus the required unit anchor. The 19
  center/radius pairs at each n=99,195,387 satisfy center+radius<=0.54.
  The total integer mass is n/3. The largest apparent rate was about
  0.018196, at n=387,center=0.05,radius=0.3. Shifting this tested cloud
  supplied no numerical evidence of a faster loss.
- `scripts/one-sided-hankel/joint-angular-location-descent.py` varied
  symmetric unit-residue pole locations at n=99,195 while fixing the
  anchor and keeping |Im(a)|<=0.54. Each descent used 512 angular
  samples, all M=n/3 moments, and at most 100 accepted steps. It used
  the differentiated finite product; no optimization theorem or
  global-minimum claim is invoked. All six selected derivative checks
  agreed with centered differences to absolute error below 5.3e-6.
  This is a floating-point implementation diagnostic, not a derivative
  enclosure or a proof of correctness on other data.

Each script saves its full data, limitations and pole parameters in
the adjacent `.json` file. The last script records every accepted
objective value and the complete final pole lists. Its final sampled
values on 2048 angular points were:

| n | S_n | D_single,n | log(D_single,n/S_n)/n | n/16+log(S_n/D_single,n) |
| --- | --- | --- | --- | --- |
| 99 | 0.4809096131 | 55.76825009 | 0.04801294 | 1.43421935 |
| 195 | 0.8306612037 | 219.60695682 | 0.02860191 | 6.61012735 |

The required loss rate is 1/16=0.0625. Even crossing that rate at one
finite n would not refute an inequality with an unspecified positive
constant and onset: a full admissible sequence and a vanishing scaled
ratio would be necessary. No such claim is made from these data.

The 1024- and 2048-point objective values agreed to displayed precision,
but neither floating-point rounding nor angular quadrature was enclosed.
Both descents hit their iteration limits. Their final gradient norms
were approximately 89.12 and 170.31, so neither is even reported as a
converged stationary point. The complete `/gradient_checks`, both
`/records/*/finer_grid_diagnostics`, both final history entries and the
selected n=99 pole list were inspected with the shared JSON inspector.
No sampled value is used as a proved inequality. The lack of SciPy was
handled with the saved bounded descent; it is not a source blocker.

The fixed-family comparisons reuse the inspected definitions and
qualifications of C645l/t/v/w: their absolute response results do not
decide the present diagonal-relative target. L647 excludes a constant
group comparison only, with zero exponential relative loss in its own
sequence. L646 and L648 continue to stop their specified full analytic
inputs, not all polynomial combinations in the joint space.

## Refined continuation within the unchanged approved target

Stop this finite-screen batch. The next proposed test is analytic and
P-dependent: form the rational reflected weight
W^sharp(z,u)=conjugate(W_(2x-conjugate(z))(u)), and test its degree<M
remainder modulo the actual multiplicity polynomial P, in the scaled
variable z=R*zeta, as a candidate s for P_+(b_u J s). This is a
proposed joint polynomial construction, not an established bound or
an approved new theorem. Its coefficient norm, angular cost, repeated
root cases, small correction and comparison with D_single,n all still
need to be evaluated. The elementary rational remainder can be treated
by finite polynomial algebra within the existing assessment's scope;
no new general interpolation theorem is presumed.

This refinement changes the tested polynomial, rather than repeating
L648's untruncated reflected input or L650's separately normalized
isolators. Required normalization tests are the single anchor, L650's
close pair and coalescing poles with unequal integer residues. Retain
all moments, the full Gram and the original integer mass. Continue only
if the complete response-to-cost estimate meets the uniform rate 1/16,
gives a quantitatively bounded remaining cost, or supplies a full
admissible obstruction to this joint certificate. A mere nonzero
remainder, a favorable finite sample or an interpolation table without
its norm does not decide it. The ready joint assessment remains
unchanged; if this construction needs a new general analytic estimate
outside its finite-algebra scope, that target requires separate review.

Essential continuation inputs are C645y (complete analytic component),
L649 (c,h,kappa and D_single,n), L650 (full polynomial response), and
L651 (uniform Gram bounds and negligible correction); C645g/o fix the
normalizations. L646--L648 are comparison stops, not lower-bound inputs.
Their audit qualifications and all actual-Xi, sign and uniform-onset
gaps remain. This completed attempt spends one mathematical EXPLORATION
turn; it does not reset the budget or edit supervisor state.
