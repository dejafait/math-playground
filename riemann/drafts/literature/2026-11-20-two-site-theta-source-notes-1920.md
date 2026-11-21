# Two-site theta control: source review1920

20 November 2026. Literature only. The target is review1919's fixed-degree
two-site cubic/quartic control question. No Jacobian, new inequality,
rank assertion or mathematical script is produced here.

## Scope and checkpoint

The main gap remains L030-L032/C032a actual-Xi all-degree positivity;
C028b's equivalent H_d=o(d) remains unpaid. The intermediate target is
independent local variation of the centered, equally weighted zero
invariants g=M_3/M_2^(3/2), k=M_4/M_2^2 for the monic orthogonal
polynomial of (mu_0+delta_a+delta_b)/3, a<b. Here mu_0 is exactly
C028q's full even theta probability, not a truncated or fitted law.
Possible use: an additional quartic adjustment after affine mean/variance
normalization. Local rank would not prove actual-target inclusion,
matching, small full residuals, or a degree-uniform cost estimate.

The proposed bounded continuation remains d=4 at (a,b)=(0,1), with no
parameter sweep. Its determinant must exclude zero rigorously to certify
rank. Exact degeneracy is informative; an enclosure containing zero is
inconclusive. No outcome of that test is asserted in this source review.

## Inspected sources and applicability

Reuse [source-notes1908](2026-11-20-one-point-theta-source-notes-1908.md)
for the complete arbitrary-site Uvarov theorem/proof and mixed-measure
zero theorem. Delgado--Fernandez--Perez--Pinar, *Multivariate Orthogonal
Polynomials and Modified Moment Functionals*, SIGMA12(2016),090,
DOI10.3842/SIGMA.2016.090,
[arXiv:1601.07194v2, Section3 pp8-10, Theorem3.1, (3.1)-(3.14)](https://arxiv.org/pdf/1601.07194v2)
allows distinct real sites and nonzero real masses. This review also
checked the primary setup (3.1)-(3.2). Specialize to one variable, two
sites, and both masses1. C028q's positive density and finite moments
give positive definite original and modified functionals. Dividing
the measure by3 changes no monic polynomial. Import the formula; do
not reprove a multi-site Uvarov theorem. Its invertibility statement
does not assert rank of the standardized zero-moment map.

Walter Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
Oxford University Press, 2004, Section2.1.1, Theorem2.1, (2.1.1)-(2.1.3),
printed pp52-54, [primary book scan, PDF pp63-65](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf).
Read the full determinant statement and its cofactor/orthogonality proof.
It represents the degree-n monic polynomial by a determinant divided
by the n-by-n Hankel determinant, using moments of orders0,...,2n-1.
For the degree-four test the required mixed-measure orders are0,...,7;
the base law is even, so only its orders0,2,4,6 need numerical input.
Odd base moments are exactly zero, while atom contributions must remain.
No order8 input or norm of the degree-four polynomial is required by
this coefficient formula. These are index/applicability checks of the
cited formula, not a computed Jacobian. Positivity must still justify
division, and any numerical implementation must enclose every divisor.

The official [DLMF18.2(ix), (18.2.26)-(18.2.29)](https://dlmf.nist.gov/18.2#ix)
identifies the same moment formula and attributes its proof to Gautschi
Theorem2.1. Its displayed determinant image/TeX was inaccessible through
the browser; the primary book statement and proof above resolve that
access issue. Reuse1908's inspected DLMF18.2(i)/(vi) mixed-measure and
simple-real-zero coverage. No Gauss weights enter the empirical moments.

## Stronger-looking moving-site conclusions

K. Castillo and F. R. Rafaeli, *On the discrete extension of Markov's
theorem on monotonicity of zeros*, ETNA44(2015),271-280,
[primary PDF](https://etna.ricam.oeaw.ac.at/vol.44.2015/pp271-280.dir/pp271-280.pdf).
Read Section2, Theorem2.2 pp272-274 and the relevant exterior-right
proof cases in Section3.1 pp274-276. It requires a positive fixed mass
at c outside the original open support interval; it proves zero
monotonicity in c and exterior asymptotics. The proof separates a root
in [c,c+epsilon) from the no-root case and uses exterior interlacing.
The theta law has convex hull R, so this theorem cannot certify either
site direction here. Even a zero-motion sign theorem would not itself
give rank of two centered standardized moment observables.

Followed that paper's reference[5]: D. K. Dimitrov,
*Monotonicity of zeros of polynomials orthogonal with respect to a
discrete measure*, [arXiv:1501.07235v1, 28 January 2015](https://arxiv.org/pdf/1501.07235),
Theorem2/Corollary3 p2 and complete proof pp3-4. Its unrestricted
single-site claim is not imported. The proof considers the weight
omega+M*N but checks the logarithmic derivative of N when invoking
TheoremA; this does not verify that theorem's stated weight hypothesis.
Also, fixing the other atom would leave an atomic background, outside
the stated nonatomic premise. No new counterexample is derived here.

Checked the primary follow-up K. Castillo, M. S. Costa and F. R. Rafaeli,
*On Markov's theorem on zeros of orthogonal polynomials revisited*,
Coimbra preprint17-43 (2017),
[Corollary3.5 and its displayed proof p11; Section4.2 pp12-14](https://www.mat.uc.pt/preprints/ps/p1743.pdf).
Corollary3.5 explicitly restricts the moving site to the exterior of A.
Section4.2 reports nonmonotone interior-site examples and explicitly
questions Theorem2/Corollary3 of arXiv:1501.07235. The numerical table
is a source warning, not our rigorous counterexample certificate.
No general derivative theorem from this follow-up is imported; its
full Theorem2.1 proof was not needed or assessed for a coefficient test.
This removes the apparent unrestricted monotonicity shortcut without
blocking the independent finite-coefficient calculation.

## Local overlap and recorded failures

Inspected C028q's empirical/affine convention and coefficient proof,
C028r's statement and imported-formula case, C028b's height criterion,
and L917/L037's enclosure hypotheses. C028r/C028s audit1919 pays a
one-site scalar matching premise under contracts; it supplies no quartic
control. Reuse its complete source comparison rather than repeating
the scalar certificate. The two-site test is outside the old one-site
asymptotic assessment and therefore needed this separate review.

Targeted searches in C028 proofs and the named theta assessments found
no existing two-site empirical cubic/quartic rank result. The failure
records for grid413, signed-Fourier435, quartic-field98 and scalar-only1919
were read. They concern, respectively, an exhausted atomic Turan grid,
rectangular Fourier error growth, a fixed finite quartic-law tail, and
repetition of the already accepted cubic scalar input. They do not
settle the changed full-theta modified reference. Their stops remain.
No cross-notebook result is used.

## Input coverage and remaining obligations

Gautschi's moment index count fits L917's accepted coverage through
order12. At lambda=0 its half-line moments M_0,M_2,M_4,M_6 give the
base probability moments M_(2j)/M_0 of C028q. Use the complete saved
panel0 intervals in scripts/heat/low-time-h2-uniform-195.json and retain
L917/audit197 and L037's Decimal-library contracts. The four-moment
H certificate1917 is not a Gram/Jacobian certificate; sharing input
moments does not transfer that scalar proof. No saved JSON was opened
or calculation run today. A later calculation must inspect full selected
endpoints and provenance, including the normalization denominator.

Essential local inputs for that continuation are L019/L021 for mu_0,
C028q for the empirical/affine convention, and L917/audit197 with L037
if those saved intervals are used. L025/L027/C028a/b/r/s explain actual
targets and relevance, but are not premises proving reference rank.
At fixed d>=4, finite coefficients and Newton identities are the
appropriate tools; no universal sample-skewness/kurtosis bound is
required for this local rank test. Wilkins1944 remains an unread lead,
not a theorem imported from a search snippet.

The next test must compute both observables with all centering and
empirical divisions by4 retained and differentiate the complete
coefficient system, including its denominator. Rigorous nonzero rank
would justify only local independent control; actual-target inclusion
needs a separately assessed argument. If the fixed enclosure is
inconclusive, save it and stop rather than sweep parameters or silently
refine source moments. If exact degeneracy is found, record its scope
and require a new independently testable target. Lower coefficients,
full companion cost, higher degrees and H_d=o(d) remain unresolved.
Full matching Mathlib coverage for this two-observable statement is
unchecked; supporting orthogonal-polynomial results alone would not
establish it. No new mathematical result is approved in this review.

## Bounded search record

Queries included:

- Uvarov modification orthogonal polynomials two moving mass points zeros derivatives
- "Uvarov" "Jacobian"
- "Uvarov" "two mass" "coefficients" zeros
- "Uvarov" "coefficient" "map" "rank"
- "Uvarov" "moving mass points"
- "orthogonal polynomials" "zero moments" "recurrence" Dehesa
- "orthogonal polynomials" "skewness" "kurtosis"
- "Uvarov" "skewness" "kurtosis"
- Dimitrov 1501.07235 monotonicity zeros error correction

No matching rank/range theorem was inspected or established by these
searches; this is not a novelty or nonexistence claim. Density-shape
skewness/kurtosis papers concern measure moments, not these equally
weighted zero moments. General rational/multivariate modification leads
were not imported. The finite Uvarov and primary moment formulas give
adequate coverage for the bounded specialization; more browsing is not
needed before that test. This review addresses changed two-observable
scope, not extra literature on the already ready scalar target.
