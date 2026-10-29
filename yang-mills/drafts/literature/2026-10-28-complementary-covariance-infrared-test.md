# Complementary-covariance infrared test — completed coverage comparison

TARGET: Test whether the complete complementary-covariance tail R_N(G)-R_N(G-H_r), differentiated in both sources, cancels L296's leading infrared obstruction at r=r_N.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L296 hypotheses/conclusion and section 1, L280(18)--(20), ATTEMPTS/047--050 and the two prior assessments named below; searched Gaussian covariance addition, effective potentials, mixed heat contractions and two-source lattice-gauge boundary responses. No exact leading-response theorem or completed local test was located in this bounded comparison; no novelty inference.
SOURCE_EVIDENCE: Newly read Bauerschmidt--Brydges--Slade arXiv:1907.05474v2, chapter 2 pp. 29--35, especially Proposition 2.1.6 with proof, Proposition 2.1.9 with both support cases, Corollary 2.1.11 with proof and Definition 2.2.1; section 5.1.1 pp. 65--66 and sections 5.2.1/5.2.3 pp. 70--75 including Definition 5.2.5 and Lemma 5.2.6 with proof. Checked author errata dated 2024-04-18; reused the versioned Bałaban/Bauerschmidt and finite-matrix readings specified below.
COMPARISON: Finite Gaussian convolution/Wick calculus and ordered matrix derivatives cover the algebraic tools for a direct test. They supply no mesh-uniform two-source relative-cube estimate and do not identify the registered scalar difference with a full Wilsonian effective action. L296's all-tail obstruction and L291's uncut cancellation decide neither its complete leading response nor cancellation with mixed lines.
GAP: The complete mixed-covariance/source accounting and normalized leading response at r_N remain unproved. Any uniform mixed Wilson estimate, high-spectrum remainder, boundary passage or effective-action identification must be justified in the later attempt; none is imported from the general Gaussian identities.
REASON: Admit one separate direct mathematical attempt at exactly TARGET, using the existing Wilson tensors and density and cited finite-dimensional tools. There is no essential inaccessible theorem for that attempt; any stronger theorem transfer or expanded target requires separate coverage. This review proves no new estimate.
LITERATURE_REASON: The changed target retains mixed complementary/tail contractions absent from the audited all-tail expression; effective Gaussian integration and its two-source relative-boundary specialization need a target-specific comparison.
SCOPE: Essential starting inputs L003 L279 L280 L282 L287 L296; exact SU(2), even N>=2, a=8/N, counting measure, all-face pins/fixed gauges, every normal endpoint, exact reflected bump, own-slice Wilson jets/full density, open real source domain and both source orders. No unproved uniform remainder, boundary replacement or changed physical observable.
COVERED_TARGET: Test whether the complete complementary-covariance tail R_N(G)-R_N(G-H_r), differentiated in both sources, cancels L296's leading infrared obstruction at r=r_N.

## Initial registration retained (step 530)

## Exact proposed target, not a result

Use L296's A(s,t), H_r(s,t), r_N and lambda_0,N and L280's
G(s,t)=Q A(s,t)^-1 Q*. Write R_N(X;s,t) for the polynomial on
the right side of L296(3) with X in every covariance slot, retaining
the same affine T(s,t), U(s,t) and complete D_N. Put
C_r(s,t)=G(s,t)-H_r(s,t). The proposed quantity is

\[
\tau_N(r)=\left.\partial_s\partial_t
 \{R_N(G(s,t);s,t)-R_N(C_r(s,t);s,t)\}\right|_{s=t=0}.
\]

Both sources act on every covariance, including its heat factor,
and on both insertion tensors. The proposed bounded test is
whether tau_N(r_N)/[N^(1/2)(log N)^2] tends to zero, or instead
has a nonzero leading response. It does not assert either outcome.
The difference is intended to retain all mixed covariance assignments,
as occur when accounting for Gaussian modes already integrated out;
no Wilsonian effective-action theorem or endpoint estimate is being
imported by that motivation. Deriving and checking the complete
expression belongs to a later approved mathematical attempt.

The plausible downstream use is to decide whether mixed contractions
can remove the specific infrared obstruction that stops R_N(H_r).
A zero normalized limit would be only a necessary first improvement:
uniform O(1) tails/shells, quantitative uncut growth and a uniform
higher remainder would remain unresolved. A nonzero complete leading
response would stop this proposed leading-cancellation mechanism at
the stated scale. Density-only bounds or an uncontrolled difference
of large terms decide neither case. An unresolved remainder must
be recorded explicitly rather than interpreted as cancellation.

## Separate source comparison

Reuse the prior primary readings where adequate. Compare the exact
finite Gaussian high/low integration and complete source derivatives
with the known effective-action statements and their source,
subtraction, boundary and locality hypotheses. Inspect only the needed
primary cases or changed coverage; no automatic repeat browsing is
required. Check the local signed-cancellation and gauge-identity
failures in ATTEMPTS/047--050. L291's uncut o(N^2) conclusion is a
contrast, not a ready estimate for tau_N; any additional canonical
asymptotic input must be named and its applicability justified.
No cross-notebook input is proposed. Full/supporting Mathlib coverage
is not checked.

The separate literature decision should admit only the defined
leading-response test if coverage is adequate, or identify the precise
missing source/assumption. Do not expand it to a uniform bound at all
scales or a continuum construction. The present step only registers
REVIEW_REQUIRED and derives none of this previously uncovered target.

## Completed source comparison (step 531, 2026-10-28)

### Primary Gaussian input and effective-action comparison

R. Bauerschmidt, D. C. Brydges and G. Slade, *Introduction to a
Renormalisation Group Method*, LNM 2242 (2019),
[arXiv:1907.05474v2, 11 November 2019](https://arxiv.org/pdf/1907.05474v2).
Page numbers here are the preprint's printed pages. Chapter 2 uses any
finite index set and real symmetric positive semidefinite covariance,
including singular support. Proposition 2.1.6 (p. 31) gives the finite
Wick/heat-operator formula for polynomials of degree at most 2p; its
proof uses uniqueness of a finite polynomial ODE. Proposition 2.1.9
(p. 32) includes the support-restricted case. Corollary 2.1.11 (p. 33)
proves covariance addition for independent Gaussian fields and the
convolution identity (2.1.19). Definition 2.2.1 (pp. 34--35) permits
formal cumulants when exponential moments are unavailable.

Section 5.1.1, (5.1.3)--(5.1.5), retains the unintegrated field in
progressive integration. Sections 5.2.1/5.2.3 (pp. 70--75), Definition
5.2.5 and Lemma 5.2.6, retain localisation and explicit remainder terms;
the simplified case requires a zero-sum covariance. Read its Taylor
remainder proof and both cases. These hierarchical scalar-model results
give no Wilson relative-box estimate. The
[author errata, 18 April 2024](https://personal.math.ubc.ca/~slade/brief-errata.pdf)
list no correction to these selected identities; later contraction
estimates are not used.

Applicability and limits for the saved target:

- L280/L296 already specify a finite, fixed transverse space and the
  extended color-diagonal covariance. The Gaussian theorem imposes no
  spatial geometry, so singular longitudinal extension is within its
  stated scope; it does not add a longitudinal integration. A later
  application to the split must verify the covariance hypotheses for
  both pieces on the real source domain, including any degenerate
  endpoint used. No such verification or mixed expansion is performed
  in this literature turn.
- The target is an explicitly defined finite polynomial. Wick calculus
  can be cited without reproving it. The required specialization is
  the actual Wilson tensors, full D_N and complete mixed source
  bookkeeping, followed by a mesh-uniform estimate. Formal cumulants
  do not justify convergence of an exponential of truncated cubic or
  quartic jets or a uniform perturbative remainder.
- Gaussian convolution acts on a function of the remaining field.
  The registered scalar difference must not be called that function
  or its logarithm by analogy. No equality with a full effective action,
  exact RG flow, running vertex or counterterm is approved. The direct
  diagnostic does not require such an equality.

### Reused source coverage and its exclusions

Reuse `2026-10-27-complete-coefficient-dyadic-shell-test.md`, completed
primary comparison: Bałaban, CMP 109 (1987), 249--301,
[DOI 10.1007/BF01215223](https://doi.org/10.1007/BF01215223),
Theorems 1/3 (pp. 259/264), (0.22)--(0.30), and the localisation and
polarisation cases (4.34)--(4.45), (5.1)--(5.8). Its small-field,
torus and subtracted-effective-action hypotheses remain different
from the bare source-pair expression here. Reuse Bauerschmidt,
[arXiv:1206.2212v3](https://arxiv.org/pdf/1206.2212v3), Theorem 1.2,
Remarks 1.7--1.8 and section 2.1: positive finite-range decompositions
do not themselves estimate these mixed Wilson contractions, and its
parameter-family hypothesis is not assumed for the two nonconstant
source weights. Earlier one-loop/background-field and slab comparisons
remain restricted as recorded there. No repeat of those unchanged
primary readings is necessary.

Reuse `2026-10-27-bare-heat-tail-obstruction-critical-audit.md`, primary
matrix calculus comparison: Schweitzer,
[arXiv:2203.03930v1](https://arxiv.org/pdf/2203.03930v1), Lemma 1 and
Theorem 2, section 2.1 pp. 2--3, supplies analytic matrix derivatives
as ordered resolvent products summed over permutations. Higham--Lin
MIMS 2013.73, Definition 3.3, and Al-Mohy--Higham (2009), Theorems
2.1/3.1, supply the recorded finite matrix calculus. A contour must
enclose the spectrum within an analytic domain, excluding zero for
the inverse/heat function. Noncommuting source directions cannot be
replaced by a scalar derivative; fixed dimension analyticity supplies
no N-uniform bound. The previously inspected Schatten inequalities
may be cited with their stated exponents; useful estimates for mixed
lines remain obligations of the later attempt.

### Bounded search, duplicates and failures

Queries on 2026-10-28 included:

- `Bauerschmidt Brydges Slade introduction rigorous renormalisation group Gaussian convolution perturbative expectation covariance addition effective potential`
- `Polchinski renormalization effective lagrangian Gaussian covariance decomposition connected expansion primary`
- `"Yang Mills" "heat" "covariance" "mixed" renormalization Gaussian boundary`
- `"lattice gauge" "complementary" covariance two source`
- `"lattice gauge" "Gaussian convolution" effective action boundary`
- `"Wilson" "heat covariance" renormalization`
- `"Yang-Mills" "covariance decomposition" "sources"`
- `"lattice gauge" "two sources" perturbation boundary`

The primary book above was inspected; the original Polchinski paper
and other RG papers surfaced as leads but were not read or used as
premises. Broad hits concerning flowed observables, other dimensions,
different boundary sectors or claimed solutions were not treated as
matching theorems. The bounded search established no matching result
for this exact mixed derivative/relative cube/scale. This is neither
a completeness claim nor evidence of originality.

Local searches were restricted to the specified assessments, heat-tail
work/audit records, histories 528/530 and ATTEMPTS/047--050. No completed
test of this difference was found there. ATTEMPTS/047 leaves the same
uncontrolled internal expectation after integration by parts; /048's
absolute norm loses the signed cancellation; /049 excludes using
generic gauge identities as sufficient; /050 records the separately
audited obstruction only for R_N(H_r). These restrictions survive.
The changed mechanism must exploit Wilson-specific mixed contractions,
not repeat those arguments under new notation. L291 remains contrast
only; L294/L295 do not replace full-box control.

The [current Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
was reopened and still links the same 14-page Jaffe--Witten
[official description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
The target version recorded in the foundation is retained; no new
physical observable or route to a complete construction is asserted.
Full matching/supporting Mathlib coverage for this tail test is not
checked. No absence claim or new library dependency is made.

### Admitted continuation and discriminating test

The TARGET and SCOPE are unchanged. EXPLORE admits one later direct
proof attempt, classified POTENTIALLY_NEW only in the limited sense
that the inspected sources do not establish this Wilson-specific
leading response. Import the general Gaussian and matrix results by
the citations above. No general theorem reproof is needed. The new
work, if undertaken, is the mixed Wilson/source specialization and
its uniform asymptotics, not Gaussian convolution itself.

Essential inputs remain L003 L279 L280 L282 L287 L296. Before taking
the limit, the attempt must retain all covariance assignments and
both source orders on every covariance/heat factor and affine jet,
the full density, colors, all finite domains and normal endpoints.
It must compare the complete response to N^(1/2)(log N)^2 at the
source-independent r_N of L296(4); r_N is held fixed during source
differentiation. Treat any unresolved high-mode or mixed Wilson
remainder explicitly as unresolved. No conclusion may be obtained
by subtracting two uncontrolled asymptotic errors.

A zero normalized limit would pass only this necessary first test
of leading cancellation. A nonzero complete leading response stops
this mechanism at the stated scale; a single-group failure does not.
An uncontrolled remainder means the test is unfinished, not zero.
The downstream use remains deciding whether the complementary
organization can escape the specific L296 obstruction. Uniform O(1)
tails/shells, quantitative uncut growth, uniform higher remainder,
the interacting lower bound, continuum field axioms/nonzero sector
and positive infinite-volume mass remain independent gaps.

Completed outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED.
This step adds source-level coverage and qualifications, not a new
mathematical result or an evaluated response. Mathematical exploration
usage is zero for this source review. Recommend the exact saved target
as proof_attempt/creative, deep_research/max: the bounded central test
is whether complete mixed Wilson contractions remove the audited
infrared obstruction at its leading scale. No lemma, mathematical
script, DAG edge or main-argument change is made.
