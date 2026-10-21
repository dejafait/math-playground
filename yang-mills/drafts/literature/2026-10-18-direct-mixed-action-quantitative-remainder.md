# Direct/mixed nonradial action — quantitative source comparison

TARGET: Assess whether L217's complete direct/mixed nonradial action response differs from its cubic limit by O(N^(5/2) log(eN)^2) for both actual probes.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L217 completely including its separate audit, the load-bearing ranges of L025 L200 L211 L214 L216 and supporting L222 modal estimates; checked the local rate assessments and ATTEMPTS/011--013. New bounded queries and inspected primary passages are recorded below; no matching response theorem was established.
SOURCE_EVIDENCE: Reused the complete-coefficient assessment's Adams--Lee comparison and scalar-source assessment; reinspected Lawler--Limic (2010), section 1.1, Theorem 4.3.1 with transient/bipartite proof and Proposition 4.6.2(a) with proof; inspected Braun--Hudson--Ortner (2022), sections 2.1--2.2, Theorem 3 and sections 6.2--6.3, especially (46)--(48). Reused the inspected DLMF Taylor input underlying L222.
COMPARISON: Known results supply quantitative scalar whole-space Green asymptotics, including differentiated expansions, but do not state the relative pinned, variable-coefficient, one-fiber response rate. L217's fixed-cluster comparison and successive collar/fiber/spatial limits remain qualitative as an assembled estimate. L222 supplies supporting mode estimates, not this response rate.
GAP: Obtain a finite-N comparison for L217(14),(17) that controls the joint kernel/fiber, coefficient variation, relative boundary rows and complete exterior heat sum at the requested threshold; constants in L217's successive limits are not yet jointly controlled.
REASON: Essential sources are accessible and sufficient for one bounded attempt on the unchanged target. EXPLORE licenses testing the remaining quantitative difference, not asserting the rate or originality; no source blocker requires another search turn.
LITERATURE_REASON: Mandatory first narrower review of the independent L217 rate gap, outside the completed co-closed-sector assessment and explicitly excluded from automatic assembly in the broader assessment.
SCOPE: SU(2) relative all-face cube, straight lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, probes i=3,6, bare expansion at fixed mesh first; exactly L217's direct/direct and both mixed blocks and their established cubic coefficient.

## Disposition and relevance

This completes the pending registration supplied at turn start. Its
REVIEW_REQUIRED decision is superseded by EXPLORE for the same target;
no mathematical estimate has been derived or approved here. A later
invocation, after the supervisor's separate approval of this changed
assessment, may make the bounded mathematical attempt below.

The main gap remains ultraviolet-uniform interacting matching with
reflected error <=c_box/2, continuum axioms and infrared finite positive
mass. This component rate could support a quantitative remainder after
cubic cancellation. Other component rates, the independent plateau
continuum comparison and a uniform interacting expansion remain open.
There is no construction candidate and no claim beyond inspected sources.

The current Clay page still links Jaffe--Witten, *Quantum Yang--Mills
Theory*, the 14-page PDF at
[the official source](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
Rechecked section 4, printed p. 6, and the compactness qualification,
footnote 2, printed p. 12, on 2026-10-18: the recorded target and finite
positive mass requirement are unchanged. No version date is printed
in that linked file; URL, length and passages identify the version used.

## Exact local comparison and duplicate/failure check

L025(6) fixes the -24 no-internal-action-pair contraction separately
from its 48-pair class. L214(4)--(9) splits each lifted row into a
direct selector minus the actual lower prefix. L217(14) retains the
direct/direct term and each mixed orientation once; its coefficient
is L217(6), with both translated half-fibers ending at axial link -1.
These finite identities and the accepted qualitative limit are inputs,
not proposed new lemmas. No reevaluation of L219's coefficient is needed.

L200 section 1, (4)--(5), supplies the actual relative component heat
and image comparison, including the even own-direction reflection,
three odd reflections and constant own-direction mode. L211 section 2,
(10)--(12), fixes the compact local factorization A=C^T J C and its
source-uniform differentiated kernels; section 3 supplies the product
convolution. The compact support belongs to J, not to covariance inputs.
L214(6)--(8) gives the complete boundary-uniform single-fiber bound.
These are ready local analytic inputs, imported within their scope.

L217 sections 1--3 already provide a fixed-interior-cluster Green error,
spatial product tail and single-fiber tail. Section 6 explicitly orders
mesh refinement before spatial, fiber and collar removal; its spatial
tail constant may depend on fiber length and finite-ball constants on
physical face distance. Substitution of growing cutoffs into that
limsup is not a rate proof. Neither the new differentiated source below
nor an infinite-grid tail supplies a relative boundary comparison.

L216(13)--(14) fixes the exact exterior normalization and full heat
majorant. L222(2)--(4),(7),(9) supplies already established eigenvalue,
product-mode, coefficient, actual probe-form and lower-prefix errors
with polynomial mode dependence. It concerns the same actual probes;
its diagnostic conclusion is not imported as a theorem for U here.
Matching these supporting bounds to all four traversal samples of
L216's exterior matrix, including endpoint rows and omitted mesh labels,
is still an applicability obligation of the later attempt.

The narrower pending record, broad quantitative assessment, direct/mixed
limit draft and L217 audit contain no existing full rate proof. L215's
O(N^(5/2)) error changes only the two-prefix block, and L216's plateau
limit is independent. No plateau rate is silently included in this target.
ATTEMPTS/011--012 stop bounded raw loops and bounded ordered local Wick
matrices; 013 stops smooth interior extension across the upper pin.
The proposed test uses differentiated residual kernels in their complete
contraction and retains that pin. These historical stops remain intact;
none is evidence that this rate is false.

## Primary sources and applicability boundaries

Lawler--Limic, [*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Cambridge (2010), author-hosted 289-page text accessed 2026-10-18:
section 1.1, printed pp. 9--11; Theorem 4.3.1, pp. 81--84;
Proposition 4.6.2(a), p. 97. Symmetric finite-range irreducible walks
in d>=3 have the stated Newtonian Green asymptotic with O(|x|^-d)
error; simple walk and its bipartite case are included. The proof
uses local central-limit errors and separate time ranges. The killed
Green identity follows by decomposing visits at exit. For the
unscaled nearest-neighbor scalar Laplacian the walk Green requires
its 2d generator normalization. This covers the scalar infinite kernel
in d=4. A killed scalar domain is not L200's relative edge domain;
no replacement of its mixed reflection law is justified by this citation.
These results do not estimate the response or its coefficient variation.
No reproof of these named scalar theorems is needed.

Braun, Hudson and Ortner, [*Asymptotic Expansion of the Elastic Far-Field
of a Crystalline Defect*](https://link.springer.com/article/10.1007/s00205-022-01810-3),
Arch. Ration. Mech. Anal. 245 (2022), 1437--1490, published 22 July
2022, publisher version accessed 2026-10-18: sections 2.1--2.2,
Theorem 3, sections 6.2--6.3, proof (46)--(48). For a stable homogeneous
Bravais-lattice Hessian with finite symmetric spanning interactions and
the stated inversion symmetry, the theorem gives differentiated
whole-space Green expansions with remainder
C_(j,p)(|ell|+2)^(-2p-d-j), away from the source. The proof keeps
finite-difference symbols before low-frequency expansion and Fourier
integration by parts; the complementary cutoff has rapid decay.
The scalar nearest-neighbor quadratic energy on Z^4 meets those
hypotheses. This supplies an optional sharper scalar input, not a
finite-box theorem. It does not cover J's variable multipliers,
relative reflected images, two ordered mixed fibers or the heat sum.
Its defect-equilibrium conclusions are not invoked. Any use should
cite Theorem 3 directly, rather than reprove its expansion.

Reuse the Adams--Lee 0709.0781v3 section II/Appendix A scope comparison
in `2026-10-17-complete-coefficient-quantitative-remainder.md` unchanged:
its translation-invariant momentum integrals have not been identified
with this pinned response. Reuse the DLMF v1.2.8 Taylor hypotheses
and exact source ranges in `2026-10-17-finite-diagnostic-continuum-rate.md`;
only smooth product modes and deterministic coefficients qualify,
not a rough projection or prefix covariance.

New queries were `discrete Green function lattice mixed boundary finite
box derivative quantitative estimates asymptotic expansion`, `"lattice"
"Green" "half-line" "variable coefficients" Feynman`, `"lattice"
"Green function" "asymptotic" Uchiyama 1998`, `Martinsson Rodin 2002
asymptotic expansions lattice Green functions pdf`, `"nonradial"
"action" "quantitative" "Yang" "Green"`, and `"lattice Green"
"weighted" "convolution" "asymptotic"`. No matching complete response
theorem was established. Martinsson--Rodin, stochastic boundary
homogenization and massive/parabolic Green papers were leads only;
their theorem hypotheses were not assessed. The Martinsson author-page
PDF link failed once; it is not essential given the inspected sources,
and is not a blocker or a reason for repeated dependent browsing.
No novelty or theorem-absence conclusion follows from these searches.

## One bounded mathematical continuation

Keep the exact TARGET. Starting from L217(14),(17), test a finite-N
error decomposition that sums the two differentiated kernels along
the actual single fibers before discarding their joint spatial tails.
Keep the original ordered finite-range J and both mixed placements.
Quantify its relative-image, coefficient-freezing, actual exterior and
quadrature errors with explicit dependence on every cutoff and heat
label. This is a proposed mechanism, not a claimed joint moment bound
or an already chosen successful cutoff schedule. If useful, import the
scalar theorem above; the existing L200 estimate needs no reproof.

Continue only if the complete error meets O(N^(5/2) log(eN)^2), or a
stronger bound, with an N-independent constant after the full heat sum.
An informative partial estimate may be saved while identifying the
remaining loss. Stop this particular quantitative transfer if tracking
its constants forces a larger allowance with no independently testable
signed improvement; report that allowance, not growth of the response.
Repeating the successive qualitative limits alone fails this test.

Essential local inputs: L025 L200 L211 L214 L216 L217; L222 supplies
only its explicitly matched modal estimates, and L215 is separate-block
context. Retain all colors, relative normal end rows, axial levels,
constant modes, full heat labels, both residual subtractions and the
upper jump. No positivity of the signed residual, coefficient
commutation, smooth upper extension, bounded infinite inverse on l2,
unproved joint cutoff modulus or uniform interacting expansion is
assumed. Independent component, construction and infrared gaps remain.
Mathlib coverage of this full rate and the cited inputs is not checked;
unknown coverage is not absence.
