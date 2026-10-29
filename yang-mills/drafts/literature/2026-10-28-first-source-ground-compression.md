# First source derivative: completed compression source comparison

TARGET: Prove an O(N^-1 log(eN)^2) bound for both first-source-derivative ground compressions of L297's W_N on the exact relative cube.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded exact-term, stronger covariance-regularity and local-coupling searches below; checked recent local assessments/history and ATTEMPTS/047--050. No inspected theorem supplies the exact rate; failed searches do not establish novelty.
SOURCE_EVIDENCE: Read Adams--Kotecky--Mueller 1202.1158v1 Theorem 2.2 and section 5 proof assembly, and Runa 1510.07604v1 section 3/Theorem 3.1 and section 7; reuse the inspected Gaussian, matrix-calculus, scalar-boundary and anisotropic gauge comparisons. L297(6)--(14),(19)--(24), L298(3)--(21) and L299(3)--(5) fix the complete local object and distinguish existing estimates from the proposed rate.
COMPARISON: The primary covariance results concern periodic gradient systems, with constant coefficients or the stated smooth variable-coefficient restrictions; neither covers this pinned transverse Wilson contraction. L297 already supplies exact zero-source inverse derivatives and complete slot accounting, and L298 supplies actual cube kernels, so no new variable-coefficient theorem is an essential premise of a direct test.
GAP: Prove the quantitative source-weight localization error for every differentiated covariance/vertex slot, the complete external-curl contribution and the all-strata relative-boundary error; the frozen zero tensor alone supplies none of these estimates.
REASON: Source comparison is adequate for one later bounded direct attempt at the unchanged target using exact zero-source kernels. EXPLORE is readiness for separate continuation approval, not an imported bound, a new result or an originality finding. No lemma or mathematical script was written.
LITERATURE_REASON: The changed first-source target requires nonconstant inverse variation and relative-boundary comparison beyond the ready constant-weight and zero-source assessments.
SCOPE: Both fixed reflected sources, SU(2), even N, a=8/N, counting measure, fixed unweighted ker B*, ambient own-slice Wilson jets, complete unchanged density, boundary-fixed gauges and all variable normal endpoints. Only the stated ground compressions are covered for a future attempt, with all upstream qualifications retained.
COVERED_TARGET: Prove an O(N^-1 log(eN)^2) bound for both first-source-derivative ground compressions of L297's W_N on the exact relative cube.

## Exact proposed statement

Use L297's even N, a=8/N, counting measure, SU(2), exact reflected
product bump h_-,h_+, fixed unweighted transverse inclusion Q, and
all variable normal end links, with boundary-contained links pinned
and boundary-fixed gauges. Use the ambient own-slice jets and the
unchanged full D_N. Let P_N be L298's rank-four one-color ground
projection on H. For i in {-,+}, define the proposed object by

\[
 V_{i,N}=Q^*\left.\partial_i W_N(s,t)\right|_{s=t=0}Q,
 \qquad
 \|P_N V_{i,N}P_N\|\le C_f N^{-1}\log(eN)^2.
\]

The color identity is suppressed only after all internal colors are
contracted. W_N is exactly L297(7), so differentiation retains every
vertex and covariance slot; D_N is source independent. The constant
C_f may depend on the fixed specified bump, not on N or on i.
This is a proposed target, not an established estimate.

Essential local inputs for assessment are L279, L280, L282, L283,
L287, L289, L297, L298 and the now audited L299, retaining their
upstream premises. Reuse the exact anisotropic comparison and
ATTEMPTS/047--050; none of those failures settles this derivative
compression. Do not replace the inverse variation by differentiating
a frozen constant-weight formula without proving the localization
error. Finite-box pins and both normal endpoints require their actual
domains, and external-curl terms cannot be silently omitted.

## Relevance and bounded decision test

The main gap remains the interacting continuum construction and mass
gap. This intermediate bound could control the all-ground parts of
Tr((W_N)_- H_+) and Tr((W_N)_+ H_-) in L297(22).
Off-ground resolvent residues, the mixed-source W_N derivative,
the full tail, uncut coefficient and uniform higher remainder remain
independent unresolved steps. A successful compression estimate
alone would not establish any of those conclusions.

The originally requested source-review step was literature-only: retrieve exact hypotheses of any
candidate local-coefficient Green-kernel or lattice gauge result and
compare all differentiated slots and boundary domains. Approve a later
bounded test only if the necessary source coverage is adequate;
otherwise retain the precise missing input or source blocker. The
eventual mathematical test must reach the stated rate for both
compressions, or exhibit a rigorous obstruction/uncontrolled term
that changes the route. A formal derivative of L299's zero tensor,
ordinary convergence without a rate, or selected Fourier diagnostics
does not meet the target. No mathematical attempt on this target was
made in step 541. Full matching Mathlib coverage is not checked.

## Completed comparison: step 542, 2026-10-29

### Local coverage, duplicates and preserved stops

Read L297's hypotheses, (6)--(14), and (19)--(24), then L298's
hypotheses and sections 1--5, and L299's hypotheses, (3)--(5) and
closing qualifications. L280's hypotheses/(1)--(4) and L282's exact
bump (1) fix the source, slice and boundary conventions. These reads
preceded the external theorem comparison. The recent local screen
used the 2026-10-28 literature assessments and histories 531--541;
no duplicate of the first-source rate was found there. This is not a
claim about unsearched literature or notebooks.

L297(10) already expresses each first inverse derivative through the
same finite transverse covariance and its source insertion. Its (13)
is the complete labeled product rule: both cubic tensor factors and
both covariance slots are differentiated; the quartic has its two
factors, and D_N has zero nonempty source derivatives. L297(9) is a
uniform energy bound, not the requested small ground compression.
L298(9),(13),(16)--(21) give zero-source kernel, row, boundary and
external-curl estimates on the actual cube. They are useful inputs,
not statements of their source-differentiated counterparts. L299
requires constant rho and translation invariance; its uniform frozen
zero tensor does not identify a nonconstant-source derivative or
bound an error after freezing a source weight. In particular no
differentiated row-sum interchange is imported by this review.

Read ATTEMPTS/047--050. Integration by parts alone leaves an
unestimated expectation; the absolute-norm route loses the signed
cancellation; generic orbit identities admit the recorded nonlocal
comparison phase; and the bare heat-tail shell is rigorously
unbounded at its tested scale. None supplies an obstruction for the
present complete first-source ground bilinear form. The present
candidate test uses exact Wilson locality and kernels, not any of
those four stopped arguments. Their evidence remains unchanged.

### New primary comparison

S. Adams, R. Kotecky and S. Mueller, *Finite range decomposition for
families of gradient Gaussian measures*, J. Funct. Anal. **264**
(2013), 169--206; inspected [arXiv:1202.1158v1, 6 February 2012](https://arxiv.org/pdf/1202.1158v1),
Theorem 2.2, (2.21)--(2.24), PDF p. 6, and section 5,
(5.48)--(5.63), PDF pp. 29--30. For d>=2, constant symmetric
positive-definite A, the mean-zero torus of side L^n, n>=1 and odd
L>=16, it gives analytic covariance decompositions. Its coefficient
derivatives satisfy (2.24)'s factorial and scale bounds, with
ellipticity constant c_0 and unit operator-norm directions. Kernels
are constant beyond half the scale range, harmless on mean-zero
fields. The proof uses complex coercivity, Fourier bounds and
Cauchy's formula. This is not a nonconstant coefficient or
relative-boundary theorem; no identification with V_(i,N) is imported.

E. Runa, *Finite range decomposition for a general class of elliptic
operators*, [arXiv:1510.07604v1, 26 October 2015](https://arxiv.org/pdf/1510.07604v1),
section 3, (6)--(11), Theorem 3.1, PDF pp. 4--5, and section 7,
PDF pp. 24--25. Its d>=3 mean-zero torus gradient system uses
symmetric uniformly elliptic C^3 coefficients sampled at x/L^n.
Equations (7),(9) impose small scaled derivatives through order
three, including order zero as printed; the theorem also states
small E-norm restrictions. It asserts positive finite-range
decomposition and coefficient-derivative bounds. Section 7 sketches
complex coercivity and Cauchy estimates. Those restrictions are not
silently replaced by bounded ellipticity. There is no established
mapping from this periodic gradient system to our staggered,
relative transverse operator with Wilson contractions. It is a
screened lead, not a premise; resolving or extending its smallness
conventions is unnecessary for the proposed direct test.

Thus these sources cover coefficient regularity in their stated
settings, but neither supplies the exact boundary domains, complete
Wilson slot sums or desired compression rate. No theorem from
either paper is applied under changed hypotheses. A general
finite-range decomposition can remain a fallback method only after
its applicability and quantitative projection/contraction errors
receive their own assessment.

### Reused primary coverage and choice of test

Reuse the completed comparisons in
`2026-10-28-complementary-covariance-infrared-test.md`,
`2026-10-28-complementary-ground-compression-rate.md`, and
`2026-10-28-anisotropic-constant-field-bulk-cancellation.md`.
Their inspected finite Gaussian input is Bauerschmidt--Brydges--Slade,
LNM 2242 (2019), Propositions 2.1.6/2.1.9 and Corollary 2.1.11;
their matrix input is Schweitzer 2203.03930v1, Lemma 1/Theorem 2,
and Higham--Lin MIMS 2013.73, Definition 3.3. The covariances here
are finite positive semidefinite matrices on a fixed slice and their
inverses are taken only on H, exactly as verified in L297. Thus
those tools support the already written inverse/slot formulas;
analyticity at each N gives no uniform compression rate.

The Lawler--Limic scalar Green and killed-Green comparison, Brandt's
rectangle boundary restrictions, and the anisotropic
Burgio--Feo--Peardon--Ryan, Giordano and Luescher--Weisz comparisons
are reused with the exact hypotheses and inspected theorem/equation
ranges in those assessments. They supply neither the vector source
rate nor a gauge-equivalence/effective-action substitute. L298's
exact mixed-grid image kernels are the available local replacement
for an unproved general vector-boundary specialization. The official
Clay version check of 2026-10-28 recorded in the reused assessment
and `foundations/01-target-and-scope.md` is unchanged route coverage.

Three prospective ways of testing the same target were compared:
coefficient-dependent finite-range decomposition, complex-source
Cauchy estimates from a uniform source-family ground bound, and
direct localization of L297's zero-source differentiated slots with
L298's exact kernels. The first lacks a verified domain/projection
transfer; the second requires a source-uniform bound not in L298.
Prefer the third. This selects a future calculation; it establishes
no localization identity or rate. A reproof of finite Gaussian or
matrix differentiation facts is unnecessary. New work is justified
only on the Wilson-specific source and boundary comparison which
the inspected results do not supply.

### Bounded search and continuation decision

Queries on 2026-10-29 included:

- `finite range decomposition variable coefficients discrete elliptic systems derivatives covariance Adams Kotecky Muller Runa`
- `"lattice gauge" "space dependent" "coupling" "one loop" self energy`
- `discrete Green function variable coefficient perturbation gradient finite domain sensitivity derivative estimates`
- `"Wilson" "position dependent" "coupling" "one-loop"`
- `"lattice" "self-energy" "local coupling" boundary`
- `"Green" "variable coefficients" "finite range" "transverse"`
- `"Wilson" "ground" "compression" "source" lattice`

Search snippets located the two primary texts above. Continuum
random-coefficient, shape-derivative, supersymmetric Wilson-loop,
numerical/interface and nonprimary claimed-solution pages were not
used as theorem evidence. Runa's reference to the Adams--Kotecky--Mueller
paper was followed to its theorem and relevant proof cases. References
to general elliptic-system regularity inside Runa were not imported;
their detailed proofs remain unread and are not essential dependencies
of the chosen zero-source kernel test. This bounded search does not
establish novelty or exhaustion of the literature.

EXPLORE now covers exactly TARGET for one later mathematical attempt,
after separate continuation approval. Use L279 L280 L282 L283 L287
L289 L297 L298 L299 with their upstream premises, both actual bumps,
fixed Q, unchanged D_N and all relative endpoints. Start from L297's
complete differentiated slots and L298's cube kernels. Test a
quantitative comparison to frozen bulk data, retaining the inverse
insertion's actual nonconstant source, the complete external-curl
terms, all source sums and every boundary stratum. These are proof
obligations, not newly admitted estimates.

Success requires the stated uniform O(N^-1 log(eN)^2) bound for
both compressions. An explicit weaker bound is a partial result;
a rigorously slower signed contribution is an obstruction to the
target rate. An uncontrolled term must be saved with its exact
threshold and can justify refining or parking this mechanism, but
a failed absolute bound alone is not a disproof. Formal
differentiation of a constant-weight identity, a numerical Fourier
preview or qualitative convergence is insufficient. Off-ground and
mixed-source residues, the complete tail, uncut coefficient, higher
remainder and interacting continuum/mass construction stay open.

This completed step is LITERATURE / NOVELTY_UNCHECKED, with outcome
EXPLORATION: new source comparison and a concrete ready test, no
new mathematical result and no progress beyond the inspected sources
claimed. It spends zero mathematical exploration turns. Full
matching Mathlib coverage is **not checked**; no absence is inferred.
