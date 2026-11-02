# Angular residue functional — bounded working checkpoint

Ready input: `drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`, unchanged EXPLORE assessment. The target is its exact common-pole angular root-mean-square lower bound at exponent 1/32; this is one mathematical attempt, not a new source review.

Main gap: actual-Xi all-degree mixed positivity. A synthetic angular detector could be useful only after independent layer isolation, other-pole control, census/clearance, simultaneous realization, and a matching upper bound/sign argument. None is supplied here.

Inputs inspected: C645g's spaces, symbol and elementary coefficient conventions; C645l's line family, admissibility, and exact finite-node contour identity; C645m's failed ellipse majorant; the anchor-line, fixed-third and angular-envelope ATTEMPTS. Their stops are preserved. No matching angular result was found in those scoped records; the supplied source assessment is reused without a novelty claim.

For w=exp(i theta), each nonzero-grid factor of the weight is exactly

    ((x-i*w*t)/(a-i*w*t))*((R^2*w+i*t*a)/(R^2*w+i*t*x)).

Common poles w=-i*t*x/R^2 are inside the unit disk; poles w=a/(i*t) are outside. After removing the t=0 cancellation, the value at w=0 is x/a, but the unmodified function is meromorphic in the disk. Evaluating it at zero is not a mean-value argument. Multiplying all common poles by an inner denominator appears to impose a large exponential cost; its adequacy is unresolved.

Current test: seek a bounded scalar Hardy functional whose exact angular coefficients retain the common poles and whose output cannot be cancelled by positive original residues on Re(a)=x. As a baseline, applying H_q_theta to the inner function B_theta(R*zeta) removes the inverse-grid factors and leaves B_theta(x) times an unweighted positive-residue symbol; its angular exponent still has to be compared with 1/32. This is partial reasoning, not yet a verified estimate.

Decisive evidence: a uniform lower bound with exponent at most 1/32 and explicit positive constant/onset, or an admissible countersequence controlling the full angular mean. An inferior functional bound is not a counterexample. Preserve any remaining quantitative obstruction instead of extending the failed ellipse envelope.

## Completed attempt and retained continuation

The exact inner-input calculation and its full proof are canonical in
[C645n](../lemmas/C645n-angular-inner-input-rate-gap.md). Its angular
response has exponential rate lambda=0.04792001946... (proved between
47/1000 and 49/1000). It gives a uniform lower bound
c_* M n^(-1/4) exp(-lambda*n) for the actual angular norm, but the full
response of this input, multiplied by exp(n/32), tends to zero uniformly
when M<=n/3. This retires the inner-input cancellation mechanism at the
requested threshold. It neither settles the actual norm nor justifies
the earlier uncompleted disk-mean shortcut. Exact arithmetic is saved
in `scripts/one-sided-hankel/angular-inner-input-rate-check.json`.

The prescribed threshold is still unresolved. Reassessment after the
ellipse-envelope stop and this distinct input-response stop nominates
one different test within the unchanged ready Fourier/residue scope:
use the constant Hardy input and evaluate its angular Gram entries

    K(a,b)=mean_theta [W_a(theta)*conjugate(W_b(theta))]
                          /(R^2-a*conjugate(b)),
    W_a(theta)=B_theta(x)/B_theta(a).

The proposed sufficient quantity is sum_(a,b) r_a*r_b*K(a,b), at the
threshold c^2*exp(-n/16). The next attempt must justify this scalar
Fourier reduction and then evaluate the angular rational residues;
displaying a positive semidefinite Gram matrix is not a uniform lower
estimate. On the angular unit circle replace conjugate(w) by 1/w,
retaining both the common interior poles and any poles from the
conjugated factor, with cancellations justified exactly. No sign for
off-diagonal entries, angular orthogonality, or separation is assumed.
This is a proposed continuation, not a completed bound or new lemma.

Essential inputs: C645g normalization, C645n's exclusion of the full
inner-input shortcut, C645l's fixed-angle contrast, C645m's distinct
envelope stop, and the already inspected Fourier/residue sources in
the unchanged assessment. All original parameters, common-pole and
integer-residue conditions remain. Layer isolation, remaining poles,
census/clearance, rotated realization, upper bound and Xi signs remain
independent. No new assessment is written or approved in this turn.
