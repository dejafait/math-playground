# Localized logarithmic amplitude — bounded attempt

Prepared STEP_ID: 2026-11-02-localized-logarithmic-research-03.
The unchanged invocation-start EXPLORE assessment is
`literature/2026-11-02-localized-logarithmic-joint-moment.md`.
This attempt tests exactly its paid-arc criterion, with no new source
approval or change of hypotheses.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs. Intermediate target: compare L658's maximum H of the complete
spatial logarithmic mean with L649's squared-residue diagonal D. The
criterion would supply L651's first-M moment bound and hence its joint
projection bound; Xi realization, matching upper bounds, signs and
independent audits remain separate.

Retain n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, common distinct
Re(a)=x poles with |a|<=R-eta and x included, positive integer residues
of total mass M<=n/3, every grid factor, the conjugated denominator
angle, normalized means and connected arcs of measure at least n^-2.
No separation, symmetry or coefficient-integrality hypothesis is added.

Inputs read: full L649, L657 and L658; L651's hypotheses, conclusions
and source/reduction conventions; the existing logarithmic working
notes and angular-evaluation, joint-moment and logarithmic-screen stops.
The supplied assessment already covers the primary root-integral and
integrability inputs. Historical pointwise Chebyshev cancellation does
not establish cancellation at every angular position. No finite screen
is being reopened.

Discriminating test: H >= (log D)/2-n/32+log n-O(1) would prove the
criterion via L658. An admissible asymptotic sequence with
2H-log D+n/16 tending to -infinity would obstruct every allowed arc.
The O(log n) gap between these tests remains. A quantitatively useful
family-specific amplitude bound is acceptable partial progress; another
localization-only reduction or a generic degree loss is not.

Unfinished reasoning saved before extended work: spatial denominator
clearing writes G as the difference between a rational weighted moment
generator and its full truncation tail. Its weights are complex, so
neither positivity of original residues nor N<=M supplies a Mahler
lower bound by itself. Investigate how angular variation and the
integer-mass census constrain this cancellation, retaining all spatial
roots and leading factors. No amplitude inequality is yet asserted.

## Refined amplitude test, still unfinished

Test a dense spread unit-residue lattice with its spacing determined by
the exact phase derivative at u=-1. Write a=x+i*y and

    lambda_n=1/d+sum_(1<=j<n)[1/(d-t_j)+t_j/(U-d*t_j)].

At u=-1 the expansion of log W_(x+i*y) starts i*lambda_n*y
minus a strictly positive quadratic term. Choose y_k=2*pi*k/lambda_n
for consecutive integers k symmetric about zero, with M about n/3.
The linear phases then agree exactly, rather than being omitted.
The intended test is whether the central O(sqrt(n)) terms give a
polynomial lower bound for c_0 while the full remaining lattice is
controlled. This is a varying admissible dense spread family, not
replacement of the original criterion by a pointwise generic bound.
To compare it with D, a uniform diagonal exponent strictly below 1/32
is also needed. L658 would then supply the paid arc. If either bound
fails, do not claim the criterion even for this subfamily.

A single-grid-factor diagnostic, independent of any sampled family,
is saved in `scripts/one-sided-hankel/logarithmic-amplitude-factor-diagnostic.json`.
It suggests that separately maximizing each factor over all angles and
real ordinates costs about 0.017489 per n after integration, below 1/32.
It has no error enclosure and supplies no proof. Its initial inline
version failed on an unavailable NumPy attribute; the saved version
uses an explicit trapezoid sum. This diagnostic is for selecting exact
inequalities, not reopening the closed finite-family screen.

## Completed result and remaining mechanism

The two estimates in the refined test are proved together in
[L659](../lemmas/L659-resonant-lattice-logarithmic-amplitude.md).
An exact four-endpoint, 22-cell rational certificate gives the uniform
bound |W_a(u)|<=exp(31n/1000+1), hence a bound on the actual squared
diagonal for every original family. The complete product expansion and
Gaussian tail control give c_0(-1)>=c*sqrt(n) on the prescribed unit
lattice with N=M=n/3 and nonshrinking support. L658 then pays the arc
cost, leaving a margin at least n/2000-2log n-C_1. This is a partial
amplitude comparison with D, not a uniform solution of the criterion.

All exact certificate cells, their complete Bernstein coefficients,
rate comparisons, the lower Riemann sum and geometric margins were
inspected. The full artifact is
`scripts/one-sided-hankel/logarithmic-amplitude-factor-certificate.json`.
The floating diagnostic is not used in the proof. The new lemma and
inherited analytic inputs remain independently unaudited.

The unsuccessful general comparison ideas remain unfinished: clearing
the spatial denominator leaves a complex numerator and a full tail;
integer residues do not by themselves control its Mahler mean. The
lattice calculation supplies exact phase matching, which arbitrary
pole locations need not have. Do not infer that all positive integer
families admit the same matching, or that a failure of matching would
refute the original criterion.

The concrete continuation retains the unchanged assessed criterion and
uses the new global diagonal bound while testing amplitude for arbitrary
support. With M<=n/3, a uniform H>=-n/8000-C would be sufficient by
L658 and (2) of L659 after enlarging the onset; the exact H-versus-D
threshold remains the primary test if that stronger estimate fails.
This is an unproved possible sufficient estimate inside the existing
target, not a new approved theorem. A repetition must address arbitrary
support or identify a quantitative obstruction to extending phase
matching; another engineered lattice or another localization estimate
is not the proposed continuation. Xi realization, matching upper bounds,
all-degree signs and audits remain separate.
