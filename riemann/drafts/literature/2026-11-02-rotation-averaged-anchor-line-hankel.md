# Rotation-averaged anchor-line detector — completed source comparison

TARGET: Test the uniform rotation-averaged bound (mean_theta ||H_q_theta||^2)^(1/2)>=c exp(-n/32) for the saved common-pole anchor-line family at delta=1/4, eta=1/100 and M<=n/3, using angular Fourier/residue analysis or an admissible countersequence.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/stronger-statement searches for rotating Blaschke grids, angular averages of rational Hankel norms, vector-valued Nehari theory and Fourier energy; inspected the primary statements below and reused the local full-pole/line assessments. No matching quantitative theorem was identified in this scope; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Frazho--ter Horst--Kaashoek 1104.5358v1, Proposition 2.1/(2.1)--(2.5) and its complete proof, pp.3--5; Theorem 3.1/(C1)--(C2), pp.7--8. Levitt, Analyse de Fourier et applications, Theorem 1.3, Exercise 1.2, Theorem 1.11 and Corollary 1.12, printed pp.6,8 (retrieved PDF pp.12,14), with selected completeness proof p.53. Reuse BCQ 1501.01161v2 Section 4/(17)--(19), Theorem 2 and Section 5.2. Optional Hardy-means lead remains theorem-unread, as qualified below.
COMPARISON: Parseval covers scalar Hilbert-space energy; matrix-valued Nehari covers a single finite-dimensional matrix symbol and its approximation distance. Neither inspected statement evaluates the prescribed angular mean of largest norms with common poles and correlated inverse-grid amplitudes. C645l establishes a fixed-direction obstruction only; its quantitative proof has not been extended to rotations.
GAP: Establish the uniform c and onset at exponent 1/32, or an admissible common-pole sequence with exp(n/32) times the angular root mean square tending to zero. Actual-Xi layer isolation, remaining poles, census/clearance, simultaneous rotated realization, matching upper bound and signs remain independent gaps.
REASON: Essential bounded source comparison is complete for one angular/Fourier-residue test of the nominated family. Known identities do not decide its quantitative question. No new estimate, reduction, lemma or script is supplied in this literature turn; newly ready coverage needs separate supervisor approval before research.
LITERATURE_REASON: The target changes the fixed-grid operator to an angular quadratic mean retaining one common pole set and residues. Prior ready fixed-grid coverage did not cover that change; this is the requested essential review, not repeated browsing of a ready target.
SCOPE: Exactly the displayed family, normalization, largest operator norm, common Z and residues, and uniform threshold; Fourier/coefficient and residue/contour proof attempts or rigorous full-mean countersequences are covered. No restriction to separated, symmetric or equally spaced poles, no added realization hypothesis, and no replacement by least singular values is covered.

The invocation-start nomination asked to assess source coverage for this
same bound. This review preserves its research target and exact family;
TARGET now states the proposed mathematical continuation. EXPLORE is a
bounded-search decision, not mathematical approval or a proved estimate.

## Exact proposed family

Retain n>=5, delta=1/4, eta=1/100, x=-5/4, R=11/8 and
t_j=j/n, 0<=j<n. Let Z be a finite set of distinct poles on
Re(a)=x, containing x, with |a|<=R-eta, and assign positive integer
original simple-pole residues r_a with M=sum r_a<=n/3. Do not impose
separation, ordinate symmetry or positivity of the complex amplitudes.
The same Z and residues must be used for every theta in [0,2*pi].

For that angle define the rotated grid and its disk factors by

    B_n,theta(v) = product_j R*(v-i*exp(i*theta)*t_j)
                              /(R^2+i*exp(-i*theta)*t_j*v),
    q_theta(zeta) = sum_(a in Z) [r_a*B_n,theta(x)/(R*B_n,theta(a))]
                                  /(zeta-a/R),
    H_q_theta f = P_minus(q_theta*f).

Use C645g's normalized H2 and strictly negative exterior space. Grid
avoidance is required at every angle; the proposed line lies outside
the radius-one grid disk. Retain the conjugated angle in the factor
denominator: rotating only the numerator would define a different
object. No normalization depending on Z or theta is allowed beyond
the displayed anchor normalization.

The proposed threshold is

    [(1/(2*pi))*integral_0^(2*pi) ||H_q_theta||^2 dtheta]^(1/2)
        >= c*exp(-n/32)

for some c>0 and onset n_0 uniform over all these families and all
n>=n_0. This is a target, not a proved consequence of angular
orthogonality or of a positive original residue. The norm inside the
integral is the largest operator norm, not a least singular value or
a scalar residue sum.

## Relevance and discriminating test

The main gap is actual-Xi all-degree mixed positivity at unbounded
heights. The intermediate target is precisely the angular lower bound
above. A positive result could supply a common-pole detector that cannot
be suppressed in angular root mean square. It would still need an
actual-Xi common-real-part layer, control of the other poles, census and
clearance, simultaneous realization of the rotated samples and an
independent upper bound for this same angular norm before it could
contribute to signs. No such bridge is assumed or proved here.

Continue only with a proof giving a uniform positive c and onset, or a
rigorous admissible countersequence controlling the whole angular mean.
An isolated bad direction, an unevaluated finite matrix, a finite angular
screen, or positivity of the original residues does not meet that test.
If the first attempt provides neither decisive evidence nor a refined
mechanism, preserve its reasoning and reassess before repetition.

Essential local inputs for the continuation are C645g's exact normalized
spaces and symbol and C645l's audited fixed-grid counterfamily. No other
local result is treated as an angular lower bound. The hypotheses above
retain distinct poles, positive integer original residues (simple poles,
not higher-order poles), no separation, and the conjugated denominator
angle. The same pole set and residues must serve every angle.

## Source review performed — 2 November 2026

### Scoped duplicate and failure check

Read C645g's hypotheses, bounds and denominator-cost mechanism through
(13), and C645l's hypotheses and fixed-grid proof through (13), including
its arc geometry and factor gain. Checked the anchor-line and fixed-third
ATTEMPTS records, and searched rotation/angular/average/ensemble/Fourier
in the associated Hankel assessments and histories. No duplicate of the
angular target was identified in those paths. This is a scoped check.

Reused the [full-pole assessment](2026-11-01-full-pole-hankel-boundary-mechanism.md)
and the [anchor-line assessment](2026-11-01-anchor-line-hankel-census.md)
for scalar Nehari/AAK, finite rational model spaces, unweighted positive
partial fractions, discrete Hilbert transforms and segment-measure
comparisons. Their hypotheses and obstructions remain recorded there;
those sources were not all reread. C645g's small-census result is not a
result at M<=n/3. C645l's real-line arc estimate uses the fixed grid
orientation; no claim is made here that it does or does not extend.
Its audited stop is retained without a reproof or certificate replay.

### Search record

Queries actually issued (2026-11-02), in addition to the local searches:

- `Hankel operator rational symbol Blaschke products rotation average lower bound positive residues`
- `vector valued Hankel operator Nehari theorem reproducing kernels finite rank rational symbol`
- `arxiv 1501.01161v2 Hankel operator rational approximation`
- `"Hankel" "rotation" "averaging" Blaschke`
- `"Hankel" "angular average" norm`
- `"Blaschke" "positive residues" Hankel rotation`
- `Parseval theorem Hilbert space valued Fourier series lecture notes author`
- `"Hankel operators" "averaging" "rotations"`
- `"Blaschke products" "angular" "mean" rational approximation norm`
- `"rotation" "Nehari" "average"`
- `"Hardy Means of a Finite Blaschke Product and Its Derivative" pdf`
- `"Gluchoff" "Hartmann" "Hardy Means"`
- `"mean_modulus_paper.pdf"`
- `"Gluchoff" "Hartmann" "Theorem 1" "Hardy"`

Generic Hankel-transform/Bessel hits concern a different operator and
were not used. Search snippets, review articles, mirrors and general
book landing pages do not establish any theorem in this assessment.
No source identified in this bounded search states the displayed
common-pole angular threshold. That is not a claim of originality.

### Primary statements and applicability

**Scalar/rational operator conventions (reused).** L. Baratchart,
S. Chevillard and T. Qian, *Minimax principle and lower bounds in
H2-rational approximation*, J. Approx. Theory 206 (2016), 17--47,
[arXiv:1501.01161v2](https://arxiv.org/pdf/1501.01161v2), 24 March 2015,
[DOI](https://doi.org/10.1016/j.jat.2015.03.004), Section 4, (17)--(19),
Theorem 2, preprint pp.6--7. Checked the operator statement again;
the prior Section 5.2 model-space assessment is reused. For bounded
circle symbols, the Hankel singular values are uniform meromorphic
approximation distances; continuity gives compactness. This permits
the same convention at each angle, but gives no evaluated angular
lower bound. The rational rank counts distinct simple poles rather
than the residue sum M. No AAK theorem is reproved or numerical
singular-value representation substituted for a lower estimate.

**Matrix-valued Nehari comparison.** A. E. Frazho, S. ter Horst and
M. A. Kaashoek, *Optimal solutions to matrix-valued Nehari problems
and related limit theorems*, [arXiv:1104.5358v1](https://arxiv.org/pdf/1104.5358v1),
28 April 2011. Inspected definitions (1.6)--(1.9), Proposition 2.1,
(2.1)--(2.5) and its complete proof, pp.3--5. For finite positive matrix
dimensions, bounded symbol G and a subspace invariant under the backward
shift containing the constants, the restricted approximation distance
is attained and equals the restricted Hankel norm. Its lifting and
projection proof leaves that norm unevaluated. Theorem 3.1, pp.7--8,
requires finite rank and (C2): no nonzero maximizing vector in the
shifted Hardy space, and a maximizing-vector space of dimension p.
It gives convergence of central Nehari approximants for fixed G,
with symbol-dependent constant L and sufficiently large index. These
are not uniform bounds for this varying angular ensemble. No (C2)
hypothesis or identification with our target is established. A vector
or matrix packaging would require a justified relation to the stated
mean of largest norms; this review asserts none. The theorem does not
replace that mean by the norm of one stacked operator.

**Fourier energy.** A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
[chapter/version page](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/chap_SF.html)
(updated 19 October 2026; PDF retrieved 2 November 2026). Read Theorem
1.3/Exercise 1.2, printed p.6, Theorem 1.11/Corollary 1.12, p.8,
and the completeness proof of Exercise 1.6, p.53. Parseval--Bessel
requires an orthonormal family in a Hilbert space, with equality for
a complete family; the Fourier version concerns scalar L2 functions
on [-pi,pi]. The source uses unnormalized Lebesgue measure and
exponentials divided by sqrt(2*pi); any future application must adjust
to this notebook's normalized measure. The proof cases use orthogonal
projections and completeness, not residue positivity. This supplies
standard Fourier machinery, not values or noncancellation of the
family's angular coefficients. A future coefficient-based proof must
justify its scalar/Hilbert-space application and every interchange;
Parseval is not a theorem about a squared operator norm as a Hilbert
norm. No such specialization has been derived here.

**Optional theorem-unread lead, not an essential dependency.**
A. Gluchoff and F. Hartmann, *Hardy Means of a Finite Blaschke Product
and Its Derivative*, Fields Institute Communications 65 (2013),
175--186, [publisher](https://link.springer.com/chapter/10.1007/978-1-4614-5341-3_9),
DOI 10.1007/978-1-4614-5341-3_9. Only the publisher abstract and
[author publication link](https://homepage.villanova.edu/robert.jantzen/maple/ellipse/hartmann-resume.htm)
were inspected. The linked `BlaschkeMeanModulus/mean_modulus_paper.pdf`
returned 404; a guessed Villanova replacement was inaccessible. No
primary theorem or proof from this chapter was read or imported.
The abstract advertises scalar Hardy means of a finite product and
its derivative, not our correlated sum of inverse-product ratios or
mean of largest norms. This is an optional computational lead, not
missing essential coverage for a test using the inspected Fourier
and residue inputs. Any later reliance on its formulae requires a
fresh source read and comparison. No paywall bypass, purchase or
source-blocked dependent mathematical work is proposed.

### Ready scope, qualifications and next approval

DECISION EXPLORE covers one mathematical attempt on the exact target
and family above. It does not certify novelty. No inspected theorem
settles its quantitative bound; no source specialization is asserted
as a new result. The standard residue and contour rules already
inspected in the reused assessments remain available by citation;
there is no reason to reprove Nehari, Parseval or the residue theorem.
The quantitative angular estimate is the uncovered mathematical work.

This is newly completed coverage: request separate supervisor approval
next turn before a research invocation. After approval, default to the
bounded mathematical test rather than another general survey. Record
new hypotheses or an essential unread theorem as a changed source gate
if the attempt needs them. Full matching Mathlib coverage is unchecked;
no Mathlib absence claim is made. No lemma, mathematical script,
angular coefficient calculation or bound was produced in this turn.
