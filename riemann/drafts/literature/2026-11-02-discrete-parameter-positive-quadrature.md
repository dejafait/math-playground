# Discrete parameter-node positive quadrature — completed source comparison

TARGET: Test whether L673's exact phase-aligned nodes admit nonnegative weights w_(a,n), independent of u, and absolute epsilon>0, K>=0, Q such that ||W_(-R)-1-sum_(a!=x) w_(a,n)*W_a||_(L2(T),normalized)<=n^K*exp(-(1/100+epsilon)*n) for every q>=Q, using finite positive quadrature in the pole parameter.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 65 searched prescribed-node positive quadrature, Tchakaloff discretization, rational Gaussian rules and analytic sampling; exact queries and primary reading ranges appear below. Checked L666 (6), L673 Sections 1--2 and L680's point attenuation/scope against saved failures. No matching rate theorem was identified; this bounded search does not establish novelty.
SOURCE_EVIDENCE: Bayer--Teichmann math/0502473v2, Theorem 1 and Corollaries 1--2 with proofs, pp.2--4; Glaubitz 2108.02848v3, Theorem 3.5 and full positivity proof, Corollary 3.6, (4.2)--(4.8), pp.11--15; Cala Rodriguez et al., ETNA 9 (1999), (2.1)--(2.3), Theorems 2.2--2.3, pp.41--43; Trefethen--Weideman (2014), Theorem 5.1 with residue proof pp.400--403 and Theorem 9.1 statement pp.412--413. Reused the Moreau/ABR assessments without new browsing.
COMPARISON: General positive discretization selects nodes; least-squares positivity needs fixed-space norm convergence and gives no applicable uniform growing-family onset; rational Gaussian positivity selects orthogonal-polynomial nodes. Analytic sampling needs an eligible integral, growth control and a full sampling/tail argument; periodic uneven-node convergence supplies no positive weights. None evaluates this exact residual. L673's rate 1/200 and L680's continuum stop retain their narrower scopes.
GAP: A positive representation on exactly the prescribed parameter nodes with anchor coefficient one and a rigorously paid full continuous L2 error at a rate strictly greater than 1/100 remains unproved. The integration functional, exactness space, weight signs, growing-n constants and any complementary tails must be justified; no standard theorem checked supplies them automatically.
REASON: Essential theorem-level comparison is sufficient for one bounded family-specific attempt on unchanged TARGET, with no essential source blocker. EXPLORE authorizes a later test, not positive weights or an impossibility claim. The newly ready assessment remains subject to the supervisor's separate next-turn approval; no mathematics is performed in this literature invocation.
LITERATURE_REASON: The invocation-start nomination replaced continuum signs by positive quadrature supported only on prescribed discrete pole-parameter nodes. Existing cone/Poisson coverage omitted this technique; this review completes its essential primary comparison without repeating ready source work.
SCOPE: Exactly TARGET with L666's complete W, x=-5/4, R=11/8, n=12q+3 and L673's exact phase-aligned nodes. Covers one later positive-quadrature construction or exact sign/normalization/rate obstruction, retaining arbitrary nonnegative angle-independent weights and the full continuous L2 remainder. No changed nodes, automatic constant exactness, unproved positive measure, continuum signs or stopped fixed-gauge replay is approved.

The prospective scope below preserves the original nomination. The completed
comparison and current readiness are recorded in the fields above and the
source review below; neither asserts a construction.

## Precise proposed test and main-gap relevance

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate target is an explicit discrete positive quadrature for
the full angular action, tested by its continuous normalized L2 error.
Such a certificate could transfer signs at actual displacement nodes
to the paid parameter point -R, or provide a stronger auxiliary
nonnegative approximation relevant to the unresolved rate-1/100 cone
test. No original unit residue may be replaced by an auxiliary weight
when interpreting H. Cone-to-H, support, realization and Xi signs
remain separate obligations even if this intermediate test succeeds.

Use the exact L673 sequence, not rounded roots: h=27/(10n), and
for 0<=k<2q let s_k solve

    s_k=k+1/2+atan(1/(10*s_k))/pi,
    k+1/2<s_k<k+5/8,
    a_(+k)=x+i*h*s_k, a_(-k)=x-i*h*s_k.

The nonanchor weights in TARGET are arbitrary nonnegative real
numbers, with no mass cap and no dependence on u. The anchor
coefficient is exactly one. Retain all factors of L666 (6), including
j=0 and denominator angle 1/u, all angular modes, and continuous L2.
No symmetry of the weights, finite Fourier cutoff, strict sign margin,
new parameter zero or open-domain positivity is imposed. The point
W_(-R) is the actual full kernel; its attenuation is audited in L680.
No identity or error bound for the displayed residual is derived here.

## Source comparison needed before mathematics

Search exact and stronger prescribed-node positive quadrature,
analytic sampling and rational interpolation results. Retrieve primary
hypotheses and the essential positivity and error proof cases first.
Determine whether positive weights require freely chosen nodes,
different anchor normalization, a positive real kernel, restricted
test functions, or a growth norm unavailable for the actual W.
The quadrature is in the pole parameter a, not L666's angular
rational quadrature in u. Conflating these two variables would not
verify a theorem hypothesis. A continuous positive Poisson measure
does not by itself furnish the required finite weights and error.

Reuse the previously inspected Moreau and ABR results rather than
searching them again. The broad cone assessment permits sign-sensitive
attempts, but it did not compare this particular positive discretization
technique; any needed quadrature theorem must be assessed before use.
Import a matching theorem if found. Otherwise identify the exact
family-specific specialization or bounded construction left to test;
an unsuccessful search cannot certify novelty.

## Duplicates, failures and continuation decision

L673's existing positive interpolation is a useful baseline, not the
desired bound: its rate 1/200 misses 1/100. Its saved fixed-gauge
contour obstruction remains intact; merely rerunning that gauge or
rounding more finely is not a new mechanism. C673b's fixed-slack
stop and finite polar screens do not settle zero-margin node signs.
L680 rules out positivity on an entire segment, but this proposed
finite-node certificate does not assume those signs or use L679's
central-mass conclusion. The new input motivating this test is the
audited full-action parameter-point and signed-boundary comparison,
not a claim that its continuous measure already has the desired atoms.

After coverage is approved, continue only on a complete positive-weight
identity or construction with the stated strict exponential remainder,
or a useful intermediate statement with an independently quantified
error toward that threshold. Stop this particular quadrature mechanism
on an exact positivity/normalization obstruction or an unavoidable
remainder rate at most 1/100. A numerical fit or sampled angular norm
is insufficient. Failure of this quadrature would not settle the cone.

Essential inputs for the review: L666 (6), L673's exact admissible
nodes and rate baseline, and audited L680's point attenuation and
scope. L678 (1)/(14) is available if complementary rays are involved.
C673b is an unaudited comparison only. Unresolved assumptions are
existence and nonnegativity of the quadrature weights, exactness for
the full kernel, uniform constants and the entire L2 remainder.
Matching Mathlib coverage for this proposed quadrature is unchecked.
The original nomination made no new lemma, mathematical script or proof.
Step 65 completes only the source comparison below; a mathematical attempt
requires the supervisor's separate approval of this newly ready assessment.

## Completed source comparison — 2 November 2026, step 65

### Positive discretization with selectable support

C. Bayer and J. Teichmann, *The proof of Tchakaloff's Theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
[arXiv:math/0502473v2, 4 May 2005](https://arxiv.org/pdf/math/0502473v2).
Read Theorem 1, Corollaries 1--2 and their complete proofs, preprint
pp.2--4. Corollary 2 assumes a positive measure concentrated on a
measurable set A and a measurable map into R^D with integrable norm.
It produces at most D points in A and positive weights matching the
coordinate integrals. Its proof passes to the image measure and uses
the cone/Caratheodory argument; the lower-dimensional case is included.
Remark 2 permits adding the constant coordinate for finite measures.
It neither selects an arbitrary prescribed node set nor fixes one
weight to one. A positive measure and eligible finite exactness space
for this target have not been supplied. Complex coordinates could be
split into real and imaginary coordinates only after those hypotheses
are verified. No specialization is asserted here.

### Prescribed data and least-squares positivity

J. Glaubitz, *Construction and application of provable positive and
exact cubature formulas*,
[arXiv:2108.02848v3, 26 May 2022](https://arxiv.org/pdf/2108.02848v3),
[DOI](https://doi.org/10.1093/imanum/drac017).
Read Lemma 3.4's proof, Theorem 3.5's entire proof, Corollary 3.6,
and Section 4 through Lemma 4.1's proof, pp.10--15. Theorem 3.5
uses a bounded domain, a Riemann-integrable nonnegative weight
positive almost everywhere, a fixed finite-dimensional real space
of bounded continuous functions containing constants, unisolvent
data, and positive reference weights whose discrete inner products
converge to the continuous one for every pair in that space.
Positivity follows eventually from the correction in (3.32)--(3.35).
Corollary 3.6 uses equidistributed data. Equation (4.5) bounds error
by twice the measure mass times best uniform approximation error;
Lemma 4.1 adds analyticity and polynomial exactness on a hypercube.
Neither supplies a growing-family onset for these nodes, a positive
target integration functional, unit anchor, or uniform analytic
approximation cost for the n-dependent full W. Fixed-space eventual
positivity is insufficient for the proposed simultaneous limit.

### Rational Gaussian rules: prescribed poles are not prescribed nodes

F. Cala Rodriguez, P. Gonzalez-Vera and M. Jimenez Paiz,
*Quadrature formulas for rational functions*, ETNA 9 (1999), 39--52,
[primary PDF](https://etna.ricam.oeaw.ac.at/vol.9.1999/pp39-52.dir/pp39-52.pdf).
Read Section 2 through Theorem 2.3's complete printed proof/sketch,
pp.41--43. The construction uses pi_m(t) with prescribed poles
separated from [-1,1], a nonnegative integrable weight omega,
and Gaussian nodes for omega/|pi_m|^2, with the required orthogonal
polynomials defined. Multiplying Gaussian weights
by |pi_m|^2 gives positive exactness on
{p/|pi_m|^2: deg p<=2m-1}. Theorem 2.2 characterizes exactness
using orthogonality of the node polynomial. Theorem 2.3 proves
qualitative convergence using bounded total weights and density,
not the required evaluated rate. Here m denotes source quadrature
size, not the notebook's n. No eligible omega or orthogonality for
the prescribed phase nodes is known. The full angular family must
also fit a common exactness space. This screen establishes no
negative result about arbitrary positive weights. Theorem 2.2's
proof is referred to earlier literature; it is not imported as an
independently audited theorem in this notebook.

### Analytic sampling and perturbed grids

L. N. Trefethen and J. A. C. Weideman, *The Exponentially Convergent
Trapezoidal Rule*, SIAM Review 56(3) (2014), 385--458,
[author PDF](https://people.maths.ox.ac.uk/trefethen/publication/PDF/2014_149.pdf).
Read Theorem 5.1 and its residue proof, pp.400--403, and Section 9
through Theorem 9.1's statement, pp.412--413. Theorem 5.1 assumes
strip analyticity, uniform decay at infinity and a uniform horizontal
L1 bound M; its infinite lattice rule has error at most
2M/(exp(2*pi*a/h)-1). The residue proof controls both strip edges
and vanishing vertical sides; it does not require the unproved
Poisson-summation step acknowledged in the alternative proof outline.
Theorem 9.1 concerns a fixed periodic analytic integrand and uniformly
distributed grids, with limsup error^(1/N)<=exp(-a/2); it makes no
weight-positivity assertion. Its underlying cited interpolation proof
was not read. Neither supplies the target functional, these finite
nonperiodic nodes, a unit anchor, positive coefficients, or growing-n
norm/tail control. No theorem is applied to W in this turn.

### Search record, unused leads and reuse

Queries issued on 2026-11-02:

- `positive quadrature prescribed nodes analytic functions theorem weights positivity Tchakaloff`
- `quadrature formula prescribed nodes positive weights rational functions complex interpolation error`
- `Glaubitz positive interpolatory quadrature prescribed nodes theorem 2020 least squares equidistributed`
- `Bayer Teichmann proof Tchakaloff theorem 2006 pdf`
- `Bultheel Cruz Barroso Gonzalez Vera Van Barel quadrature formulas rational functions 1998 39 52 pdf`
- `"positive" "quadrature" "prescribed nodes" "analytic" rational`
- `"Blaschke" "positive" "quadrature" "prescribed" nodes`
- `Trefethen Weideman exponentially convergent trapezoidal rule theorem 5.1 pdf`

The ETNA primary PDF identifies its actual authors as above; the
Bultheel query was a discovery query, not a bibliographic attribution.
Search results also led to Peherstorfer's positive-rule characterization,
random-node Richter--Tchakaloff work (arXiv:2610.32699), randomized
least-squares work (arXiv:2609.09506), and Austin--Trefethen perturbed
trigonometric interpolation (arXiv:1612.04018). These are unread leads,
not inspected theorem coverage or evidence of impossibility. None is
an assumed input to the proposed explicit family-specific attempt;
invoking any of them later requires its precise primary hypotheses.
This bounded comparison does not claim an exhaustive search or novelty.

The existing Moreau and ABR assessments named in the nomination were
reused, not refreshed. They concern cone projection and continuous
representation, respectively. Neither identifies an eligible positive
finite measure already supported on these prescribed parameter nodes.
Shell PDF download failed on DNS; all essential primary reading above
was available through the web tool, so no essential blocker remains.

### Family-specific gap, discriminator and continuation

The target samples the pole parameter a while retaining the whole
angular function u. L666's exact angular quadrature is a different
operation. The proposal is not yet quadrature for an identified
positive measure: the weight-independent target value and fixed
anchor must be justified on the actual chosen test space. Importing
constant exactness or a total-mass normalization without checking
that space would change the problem. Conversely, failure of a
generic positive-measure representation would not automatically
rule out approximation of this restricted W family.

No inspected theorem is a matching import. EXPLORE therefore covers
one explicit parameter-quadrature construction or obstruction test
for the unchanged residual. A possible attempt must provide its
exact full-kernel identity, real nonnegative weights independent of u,
and all uniform remainder costs; a candidate formulation or finite
fit is not such a certificate. If it uses an integral representation,
pay its signed complement and discretization error as well as the
anchor normalization. Any invocation of a standard theorem is by
the citations above within their hypotheses, not by a new reproof.

Continue on a complete bound n^K*exp(-(1/100+epsilon)*n) with
absolute epsilon>0, K>=0 and onset, or a genuinely informative
intermediate estimate toward it. Stop this specific mechanism on
an exact positivity/normalization obstruction or a proved unavoidable
rate <=1/100. Inability to apply the general sources alone is not
that obstruction. Preserve L673's rate-1/200 baseline and its fixed
gauge/contour stop: rerunning it more finely does not qualify as a
new attempt. L680's continuum exclusion remains intact; no L679
mass conclusion follows from discrete signs. C673b remains an
unaudited comparison, not an essential input.

Essential continuation inputs: L666 (6), L673's exact nodes and
audited baseline, and audited L680's parameter-point attenuation
and scope. Read L678 (1)/(14) only if rays enter the construction.
Positive weights, anchor compatibility, full-kernel exactness and
uniform continuous L2 remainder are all unresolved. Even success
leaves cone-to-original-unit-residue H, support, realization and
actual-Xi mixed positivity open. No mathematical result, lemma,
script or RH candidate is produced by this review.

### Mathlib

Full matching coverage for the prescribed-node positive quadrature
and exponential residual was not checked. No absence claim is made.
The general cone/harmonic supporting coverage stays as qualified
in the reused assessments; it supplies no evaluated target bound.
