# Periodic second-moment cone: source comparison

TARGET: Test whether L473's K lies in the relative interior of the cone of lag-one periodic second-moment matrices, allowing subtraction of L585's fixed carrier covariance.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for moment-cone relative interior/full-support measures, Richter finite representation and stationary derivative covariance located the primary sources below; reused the saved periodic occupation/fourth-carrier failure comparisons. No exact periodic-jet absorption theorem was located; this is not evidence of novelty.
SOURCE_EVIDENCE: Read Blekherman--Fialkow arXiv:1804.04276v1, setup p.1 and Proposition 2.1/Corollary 2.2 with proofs pp.5--6; Bayer--Teichmann math/0502473v2 Theorem 1/proof and Corollary 2 pp.2--3; Tao 245C Notes 2 Theorem 21 (torus proof), Corollary 22 and (3); Rockafellar--Wets Proposition 2.40/proof p.64; Rasmussen--Williams Sections 4.1.1/4.2.1, Theorem 4.1 pp.81--82. Exact URLs and scope below.
COMPARISON: Strict positivity implies interior and finite attainment by known moment-cone results; convex closure/interior equality is also known. The remaining specialization must identify the actual periodic cone, verify the common span across restricted/unrestricted frequencies, and check strict positivity for the explicit K. Ambient matrix positivity and Bochner realization do not discharge those hypotheses.
GAP: Apply the inspected criteria to all 21 ordinary lag-one second entries, then justify absorption of each fixed L585 covariance in the actual finite periodic cone; none of these local conclusions is proved in this literature turn.
REASON: Essential source coverage is now available for the unchanged bounded target. Continue with the explicit spectral/moment-cone specialization, importing standard convexity and Fourier theorems rather than reproving them; newly ready coverage receives separate approval before research.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes fourth-tensor feasibility to second-cone interiority; the prior ready assessments did not cover its essential spectral and strict-positivity hypotheses.
SCOPE: Real smooth periodic paths, unrestricted finite periods, nonnegative finite weights, ordinary derivatives through order two, fixed lag one, all 21 second entries, and L473's exact K. No positive clipped mass, prescribed spectral support for the completion, full law or Xi realization is assumed.

## Completed literature-only comparison, 31 October 2026

The main gap remains actual-Xi all-degree signs at unbounded heights.
The intermediate target is the exact TARGET above. Its plausible use is
derivative-preserving second completion of L585's fixed fourth carrier.
This review approves source scope for a future test, not its conclusion.
No lemma, mathematical script, certificate or argument overview changed.

### Primary inputs and hypotheses

1. Blekherman--Fialkow, *The core variety and representing measures in
   the truncated moment problem*, [arXiv:1804.04276v1](https://arxiv.org/pdf/1804.04276v1#page=6),
   Proposition 2.1 and Corollary 2.2, pp.5--6. The setup is a nonempty
   T1 space S and a finite-dimensional space E of real Borel functions.
   For its nonnegative-function cone, strict positivity of a functional
   characterizes the interior of the finite evaluation cone and gives
   finite atomic representation. Read the bipolar proof, the converse
   perturbation by an evaluation, and the final atom-insertion argument.
   The later standing assumption for core-variety iteration is not
   needed here (Remark 2.4). Applicability requires using an actual
   function space, removing identically zero coordinate combinations;
   positivity of K as a matrix is a different condition. The candidate
   E is the span of the real spectral entry functions in L473 (6),
   with S either R or the stated compact frequency interval. Their
   relation, and strict positivity of integration against that interval
   for the required S, remain verification tasks.

2. Bayer--Teichmann, *The proof of Tchakaloff's theorem*,
   [math/0502473v2](https://arxiv.org/pdf/math/0502473v2#page=2),
   Theorem 1 and Corollary 2, pp.2--3. The latter covers measurable
   maps into R^N whose push-forward has integrable first moments;
   it gives positive finite quadrature nodes in any full-measure
   subset. The proof's lower-dimensional reduction and strict
   supporting-plane case were read. This handles nonpolynomial
   spectral entries as well as polynomial ones. It does not ensure
   that nodes share a common period or that a larger frequency cone
   has the same span. Theorem 1's proof reduces to an essential
   subspace; it must not be cited as interiority in an arbitrarily
   larger prescribed span. Reuse it only after the required span
   comparison. No prescribed total weight follows unless the constant
   coordinate is included (Remark 2).

3. Tao, *245C, Notes 2: The Fourier transform*, 6 April 2009,
   [Section 2, Theorem 21 and Corollary 22](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
   For a compact abelian group with probability Haar measure,
   characters form an L2 orthonormal basis and bilinear Parseval holds.
   Read the torus Stone--Weierstrass proof and translation formula (3).
   Apply on R/PZ with normalized integral; verify frequency units,
   ordinary derivative factors, and lag-one phase signs locally.
   The future proof must justify all second-entry Fourier sums for
   smooth periodic paths, including zero frequency and real conjugate
   pairs. No pointwise convergence theorem is needed or imported.

4. Rockafellar--Wets, *Variational Analysis*, author-hosted third
   printing (2009), [Proposition 2.40, p.64](https://sites.math.washington.edu/~rtr/papers/rtr169-VarAnalysis-RockWets.pdf#page=72).
   For a nonempty finite-dimensional convex set, relative interiors
   agree before and after closure. Its proof translates and reduces
   to the affine hull, uses a maximal independent simplex, and invokes
   Theorem 2.33. Reuse the previously inspected Theorem 2.33 coverage
   in the L585 audit assessment. No closedness, compact generator set
   or new simplex lemma is needed. Membership in the same affine
   hull and interiority must still be established before use.

5. Rasmussen--Williams, *Gaussian Processes for Machine Learning*
   (MIT Press, 2006), [Sections 4.1.1 and 4.2.1, pp.81--82](https://gaussianprocess.org/gpml/chapters/RW4.pdf#page=3).
   Theorem 4.1 states Bochner's characterization using a finite
   positive spectral measure for a weakly stationary, mean-square
   continuous complex process. Section 4.1.1 gives covariance
   differentiation for mean-square derivatives, including the finite
   derivative-at-zero sufficient condition. These statements do not
   supply smooth periodic sample paths or finite mixtures of such
   paths. They are a comparison, not an extra realization premise;
   periodic Parseval is the appropriate input here.

Also inspected di Dio--Schmuedgen, *The multidimensional truncated
moment problem: The moment cone*, [arXiv:1809.00584v1](https://arxiv.org/pdf/1809.00584v1#page=9),
definitions in Section 2 and the statement/setup of Theorem 19,
pp.8--9. Richter's theorem covers finite families of measurable
functions and finite atomic representation. Its full induction proof
was not audited here; it is an overlapping lead, not needed in
addition to the inspected Bayer--Teichmann and Blekherman--Fialkow
inputs. No novelty follows from not locating the exact specialization.

### Bounded specialization to attempt after approval

Keep C(h), K and the fixed R exactly as in the nomination below.
Use the real part of the spectral integrand in L473 (6) to specify
the candidate spectral matrix curve; do not replace it by arbitrary
rank-one positive matrices. Check these obligations in sequence:

- Identify single-frequency periodic generators, their normalization
  and the treatment of frequency zero; use Parseval to compare the
  cone/closure for general smooth periodic paths. Finite sums may
  mix different periods: a common period is not a hypothesis.
- Verify the linear relations/common span of the restricted frequency
  curve and the unrestricted one. Test any candidate annihilator or
  supporting functional exactly; do not substitute a sampled rank.
  The entry functions' analytic form suggests an identity-theorem
  test, which has not been carried out in this turn.
- Verify the strict-positivity hypothesis for the functional defined
  by K in that same function space, then apply the cited interior
  and finite-attainment results. Only afterwards test subtraction
  of the particular fixed R and the quantifier for all sufficiently
  large real ell. No numerical R or effective onset is assumed.

Continue if these checks give exact interiority and finite periodic
attainment of ell K-R on one eventual ray. An exact separator,
span mismatch or boundary nonattainment excludes the proposed
absorption argument and requires a changed mechanism. An unresolved
hypothesis is to be recorded as such, not treated as feasibility.
No reproof of the imported convexity, cubature or Parseval theorems
is warranted; only the lag/derivative and cone specialization is new
local work. This is a standard-theorem application target, not an
approved creative RH mechanism.

### Scope, duplicates and remaining gaps

Read L473 through (6)--(7) and the start of Section 3, and L585's
hypotheses/conclusion (1). Reused the exact failure comparison in
`2026-10-31-bounded-periodic-occupation-moment-compensation.md`
and the source/attainment review in
`2026-10-31-l585-periodic-carrier-audit-scope.md`; narrowly searched
the saved rare-fourth and Whitney assessments for second-cone
coverage. L578/L579's fixed-packet restrictions, L581's exact-law
obstruction and L584's absolute-budget stop retain their scopes.
None permits an arbitrary six-coordinate repair to count as a
derivative-consistent periodic law. No sibling notebook was read.

Queries included `moment cone relative interior full support measure
Richter theorem finite dimensional continuous functions`, `stationary
process mean square derivatives covariance spectral fourth moment
theorem Bochner`, and `moment cone interior strictly positive continuous`.
The sources above were opened as primary text; no search snippet is
used as a theorem. A shell download failed DNS resolution; browser
retrieval supplied the needed complete passages, so access is not
blocked. Matching Mathlib coverage is not checked.

Even success would not settle probability normalization, uniform
phasewise support, fourth-error bookkeeping, positive clipped mass
or actual-Xi transfer. L473's arithmetic-source qualifications remain.

## Invocation-start nomination (historical; coverage superseded above)

This file nominates future work only. It does not approve a theorem,
derive an interior statement or modify the prior carrier assessment.
The exact mathematical target above must be retained while its source
coverage is assessed; an eventual IMPORT should cite the result and
limit research to the necessary application.

Use C(h)=P^(-1) integral_0^P J_h(s) J_h(s)^T ds, with L585's six
ordinary coordinates. The proposed cone consists of finite sums of
such matrices with nonnegative coefficients. K here denotes L473 (6),
not L585's fourth-tensor cone. For any one fixed representation supplied
by L585, let R=sum_i a_i C(h_i); it is finite, but no numerical R or
bound on its size has been supplied. The sought interior statement is
intended to justify a positive periodic completion of ell K-R on an
eventual ray; verify the needed common affine hull rather than relying
on positive definiteness in the ambient space of symmetric matrices.

Essential local inputs for the proposed continuation are L473 (6)--(7)
and L585 (1). The arithmetic identification of K retains L473's source
qualifications. The prior packet, exact-law and absolute-budget stops
must remain in force in their original scopes. No cross-notebook input
is proposed. This turn has not loaded additional proofs or tested the
new interior claim.

Continue if a precise source comparison approves a bounded test of
interiority and absorption in the actual periodic cone. If an exact
supporting functional or an unattained boundary excludes the required
direction, record that obstruction and change the mechanism. Even a
successful second-moment result would leave probability normalization,
uniform phasewise support and fourth-error bookkeeping to check, and
would not provide the clipped lower bound or actual-Xi transfer.
Matching Mathlib coverage remains unchecked.
