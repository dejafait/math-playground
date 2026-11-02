# Nonpositive angular projection — bounded attempt

Prepared STEP_ID: 2026-11-02-angular-nonpositive-projection-01.
The unchanged ready EXPLORE assessment is
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
One mathematical attempt is made on its exact target and family.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Intermediate test: bound the two-circle L2 norm of the nonpositive
angular Fourier projection of the constant-input response below by
c exp(-n/32), uniformly in the prescribed common pole set and original
positive integer residues. This would suffice for the angular detector;
layer isolation, other poles, census/clearance, simultaneous realization,
an independent upper bound and Xi signs remain unresolved.

Retain n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100, t_j=j/n,
Re(a)=x, |a|<=R-eta, x in Z, distinct poles, M=sum r_a<=n/3,
and the conjugated denominator angle. C645g supplies normalization;
C645o supplies W_a, common poles p_j=t_j*x/U, residues R_j(a), and
mu_a=I(a,x). The latter result remains independently unaudited.
Its exact identity has been read; its negative-cross-entry certificate
is a contrast, not a premise for this test. Prior angular working notes
and the entrywise-positivity failure were checked. The ready assessment
and its inspected Fourier/residue sources are reused; no new browsing
or claim of certified novelty is needed.

Proposed calculation: partial fractions give

    P_(<=0) W_a(u) = mu_a + sum_j R_j(a)/(u-p_j).

The negative-mode series and the spatial exterior series should give
an exact finite Gram expression. A quantitative proof must control the
signed sums, including the zeroth mode; PSD alone does not suffice.
Test a bounded evaluation of this projected rational function or an
admissible asymptotic family. Success requires the stated uniform rate;
a rigorously smaller projected response stops this projection only,
not the full constant-input or operator target. An unevaluated formula
or nonrigorous finite screen is an incomplete attempt.

Checkpoint before further work: no new bound or lemma is established.

## Partial reasoning saved before write-up

The projected angular weight is exactly
mu_a+sum_j R_j(a)/(u-p_j); distinct interior poles are all simple,
and the remaining part has only strictly positive angular modes.
Thus the proposed complete projected energy has angular Gram entries
mu_a conjugate(mu_b)+sum_(j,k) R_j(a) conjugate(R_k(b))/(1-p_j*p_k),
multiplied by the spatial factor 1/(U-a*conjugate(b)). All signed
cross terms remain. This formula has not yet supplied the required bound.

At angular u=0, rational continuation of the projection has value x/a:
the omitted analytic part has zero constant term. Therefore the first
spatial coefficient there is (1/R)*sum_a r_a*x/a, whose real part is
at least M*d^2/[R*(R-eta)^2]. This is algebraic continuation, not
evaluation of an L2 Fourier series at an interior singularity.

Let beta_n(u)=product_(j=1)^(n-1) (u-p_j)/(1-p_j*u).
Multiplication by beta_n cancels every possible angular pole and
preserves boundary norm. The constant-term inequality gives
||P_(<=0)q|| >= |beta_n(0)|*||(P_(<=0)q)(0,.)||.
The exact transfer factor is
(d/U)^(n-1)*(n-1)!/n^(n-1). It is sharp in the ambient rational
space, because 1/beta_n has norm one and value 1/beta_n(0).
That extremizer is not shown to arise from an admissible original
positive-residue family. This does not stop the projection itself.

The finite screen in scripts/one-sided-hankel/angular-projection-screen.json
uses six Chebyshev families, n=9 through 195. No rounding, angular aliasing
or spatial-tail enclosure is supplied. The complete selected /records
field was inspected. It provides no asymptotic bound or counterexample
and is not used as proof.

The bounded attempt is now to finish the exact transfer-factor proof
and compare its rate to 1/32, without treating a weak lower bound as
an upper bound on the actual response.

## Completed result and continuation

The exact projection, complete signed Gram, noncancelling continued
value, sharp ambient evaluation norm and exponent comparison are now
canonical in
[C645p](../lemmas/C645p-angular-projection-zero-evaluation-cost.md).
They are unaudited specializations of standard Fourier/Blaschke facts,
not a claim of certified novelty. The transfer factor has rate
1+log(121/80)>1/32; even its full evaluated spatial response cannot
supply the required lower bound. The ambient extremizer has not been
realized by an admissible family. Only this generic zero-evaluation
method is stopped; the constrained projection remains unresolved.

Park that extraction unless additional family-specific structure is
identified. A materially different next test, within the unchanged
ready Fourier/coefficient scope, is a full angular upper bound for
radius-adjusted Chebyshev pole families: n=3m with m odd, unit residues,
and a_k=x+i*r*cos((2k-1)*pi/(2m)), 0<r<=1/2. First derive the angular
Hilbert--Schmidt energy as a majorant of the required mean largest norm;
retain all signed terms and both angular signs. Then seek a radius or
radius sequence with upper exponential rate strictly greater than
1/32, or a rigorous obstruction for that proposed majorant. This is a
proposed calculation, not an established upper bound or an approval
of uncovered mathematics. The radius-one-half finite screen provides
no certificate and does not decide other radii.

Essential continuation inputs: C645g normalization, C645l's audited
Chebyshev family/finite-node identity, C645o's angular integral formula
(independent audit pending), and the unchanged ready Fourier/residue
assessment. Smaller radii still need the explicit admissibility check.
C645m's particular radius-one-half ellipse envelope, C645n's inner input,
and C645p's ambient evaluation are contrasts. No new positivity,
separation, holomorphy or Xi realization assumption is introduced.
For a countersequence the entire angular operator mean must be bounded;
a small projection, one direction, or finite angular screen is insufficient.
