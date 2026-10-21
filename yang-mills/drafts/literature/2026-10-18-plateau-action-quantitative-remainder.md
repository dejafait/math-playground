# Plateau action remainder — source comparison

TARGET: Assess whether L216's complete plateau response differs from a^(-3)P_i by O(N^(5/2) log(eN)^2) for both actual probes.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read all of L216, L101 sections 3--4, L215's exact plateau definition and bounds, L224 sections 1--4 and its audit's stencil/projection cases, and L222's quantitative mode hypotheses; compared the existing static-trace and direct/mixed assessments and ATTEMPTS/011--013/024--025. Five bounded external queries and the inspected primary passages are recorded below; no matching complete plateau-response theorem was established.
SOURCE_EVIDENCE: Reinspected Lawler--Limic (2010), section 1.1, Theorem 4.3.1 and its transient/bipartite proof cases, Corollary 4.3.3 and Theorem 6.3.8(a) with its harmonic-measure proof. Reused the recorded Adams--Lee, Gurevich and DLMF comparisons. L224 section 7 accepts its cumulative-stencil and energy-cutoff estimates relative to imported inputs; those estimates, rather than its different trace conclusion, are reusable here.
COMPARISON: L216 and L224 use exactly C_(j,N)=a A_<j with the same moving-cut endpoint and cumulative upper tail. L224 supplies coefficientwise O(a) and compact-source dipole-energy estimates, but its O(N^2) trace rate has a different exterior contraction and sources in a fixed transverse interior. L216 sums traversal sources throughout the transverse cube, so its collar and actual U normalization still require quantitative specialization.
GAP: Quantify L216(12)--(15) with source-distance dependence or a joint shrinking-collar estimate, matching all traversal entries of a^(-2)U to the actual modal bounds before the complete heat sum; preserve all cuts and signed cumulative coefficients. No complete plateau rate is imported.
REASON: Essential scalar sources and audited local coefficient/energy inputs are available. One bounded specialization is source-ready, with its remaining boundary, bilinear-freezing and exterior-matching obligations explicit; no new estimate is derived in this literature turn.
LITERATURE_REASON: Mandatory first comparison of the separate plateau-continuum rate, expressly excluded from the ready direct/mixed assessment; L224's applicability and canonical audit status needed checking.
SCOPE: Relative SU(2) cube, straight lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, actual probes i=3,6, fixed-mesh bare expansion first; exactly L216(2) minus a^(-3) times L216(9), with all traversal/color entries, cuts, transverse end rows and heat labels.

## Disposition and relevance

This completes the pending registration for the unchanged TARGET.
SPECIALIZE makes one later mathematical attempt source-ready, subject
to the supervisor's separate approval of this changed assessment. It
does not prove the rate or perform that attempt. No lemma or mathematical
script is changed. The source-comparison outcome is NEGATIVE for direct
import of L224's trace conclusion, with reusable estimates and a concrete
remaining test; it is not a mathematical counterexample or novelty claim.

The main gap remains ultraviolet-uniform interacting reflected control
<=c_box/2, continuum axioms and finite positive physical mass. The
intermediate target is a quantitative remainder for the complete
plateau block after subtracting its established cubic coefficient.
Together with L215 and the separate L230 block, success could close the
nonradial action component's proposed remainder scale. Other response
rates and a coupling-uniform interacting expansion would remain open.
Reuse the official Jaffe--Witten version/scope verified on 2026-10-18 in
the direct/mixed assessment; no change to the exact construction target
or its finite-positive-mass qualification is proposed.

## Exact comparison and reusable local inputs

L216(1)--(2) fixes the full finite plateau response. Its four traversal
dipoles share the same cut j. Equation (15) fixes the a^4 quadrature,
original -24, colors and normalizations a^(-2)U and a V^pl. There is no
Gaussian-tilt factor 2. L216(9) is the coefficient to subtract; this
review does not reevaluate it or use cubic cancellation to obtain a rate.

L101(13)--(15), imported in L216 section 1, and L224 section 1 concern
the identical scalar insertion C_(j,N)=a A_<j. L224(2)--(4) gives its
exact signed finite-range dipole decomposition, coefficientwise O(a)
comparison to smooth limiting coefficients, uniform C^1 bounds and
identification of m_E. The transverse coefficient support has a fixed
buffer for every axial cut. The quarter layer and moving-cut term are
retained. Compact transverse support is consistent with a cumulative
upper axial tail; compact axial support of C_(j,N) is unavailable.
These are already proved local inputs, not deductions made in this review.

L224 section 7 explicitly accepts those coefficient bounds, the
relative extension and the dipole best-approximation estimates relative
to its stated inputs. Its canonical audit resolves the stale pending
wording in the supplied PROOF overview. No duplicate audit, overview
rewrite or recursive upstream verification is needed for this step.

L224(5),(8)--(10) supplies scalar dipole gradient decay, a finite second
spatial l2 moment and an O(N^(-3/2)) energy projection error for sources
with a fixed transverse buffer. L216 section 2 already identifies its
finite scalar Green columns as energy projections. These are compatible
scalar vertex spaces; no scalar boundary condition is assigned to a
relative vector component. Fourier Plancherel and the Hilbert-space
orthogonal projection theorem are standard named inputs.

The difference that prevents IMPORT is substantive. L224's conclusion
is for L101's ordered trace with the Zeta/S_T exterior contraction; it
is not a theorem for L216's four-edge K:U:V^pl contraction. Moreover,
L224's stated cutoff constant uses a fixed source buffer supplied by
its coefficient-supported dipole centers. L216's traversal sources
range to all transverse faces, even though the insertion itself is
compactly supported transversely. One cannot silently give all these
sources that buffer. L216's fixed-collar limit is qualitative and has
to be quantified jointly with the interior comparison.

L224(12)--(13) and L222(2),(3),(7),(9) supply reusable smooth-mode,
prefix and actual-probe error estimates. L216(13)--(14) uses raw lifted
traversal samples, rather than L224's Bb/Bq path map or L222's finite
diagnostic. Match those raw samples and traversal signs explicitly;
the endpoint, constant axial mode, triplet average of products and
both polarized shear products remain. Supporting modal estimates may
be specialized; neither different trace conclusion may be transferred.

L215's complete two-prefix replacement already costs O(N^(5/2)); it
does not estimate the plateau's remaining continuum comparison.
L230 covers only direct/direct and both mixed blocks. It supplies
neither a plateau premise nor compact axial support for C_(j,N).

## Primary theorem hypotheses and essential proof cases

Lawler--Limic, [*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf)
(Cambridge, 2010), same 289-page author-hosted text accessed 2026-10-18:
section 1.1, printed pp. 9--11, defines symmetric finite-range irreducible
walks P_d. Theorem 4.3.1, pp. 81--84, treats d>=3; its proof separates
time ranges and explicitly reduces the bipartite case to the aperiodic
one. Corollary 4.3.3, p. 84, gives coordinate first Green differences
O(|x|^(1-d)) and repeated coordinate differences O(|x|^(-d)). Theorem
6.3.8(a), p. 131, bounds bounded-step differences of a signed harmonic
function on a ball by its supremum divided by radius (and second
differences by radius squared). Its proof uses an interior cube and
harmonic measure uniformly over exit points. Three-dimensional simple
walk qualifies; Delta=6(I-P_walk), so g_Delta=G_walk/6. These are scalar
inputs, not a pinned plateau-response theorem. L224 section 2 already
justifies mixed Green differences by harmonic balls avoiding the finite
dipole sources; repeated-coordinate estimates alone are not substituted.

Reuse the Adams--Lee 0709.0781v3 section II/Appendix A comparison in
`2026-10-17-complete-coefficient-quantitative-remainder.md`: the inspected
translation-invariant momentum theorem does not cover this pinned,
variable-coefficient heat-summed response. Reuse Gurevich 1504.02673v2
Conditions 2.1--2.3/Theorem 3.1 comparison in
`2026-10-17-e-static-trace-continuum-rate.md`: its whole-space parabolic
result has not been specialized to this cumulative finite-box pairing.
Neither is an essential missing theorem or an additional imported input.

Reuse the DLMF v1.2.8 section 1.4(vi), (1.4.35)--(1.4.37), assessment
underlying L222 for smooth product modes and deterministic coefficients.
Reproving scalar Green asymptotics or Taylor's theorem would add no
needed coverage. The required work is their quantitative applicability
to the actual plateau pairing, boundary sum and exterior normalization.

## Bounded search, duplicates and failures

New queries on 2026-10-18 were:

- `"lattice Green function" "dipole" "Dirichlet" convergence energy`
- `"lattice" "Green" "cumulative" "plateau" Yang Mills`
- `Lawler Limic random walk Corollary 4.3.3 Theorem 6.3.8 pdf`
- `discrete Green function dipole finite domain energy approximation error nearest neighbor lattice`
- `"lattice Green" "dipole" "convergence rate"`

The theorem query led to the inspected author-hosted primary text.
Other hits included electromagnetic discrete-dipole approximation,
bounded-domain lattice numerical methods and defect-computation papers;
their theorem hypotheses were not read and none is an imported input.
The exact plateau terminology did not establish a matching theorem.
This bounded search makes no novelty or global absence claim. Existing
static-trace and direct/mixed assessments are reused rather than
repeating their searches. No essential source is blocked.

The local comparison found L224's related audited rate, but no existing
rate for the complete expression L216(2). ATTEMPTS/011--012 exclude
bounded raw forest loops or bounded local Wick coefficients; neither
is needed for a normalized dipole-energy comparison. ATTEMPTS/013
excludes a smooth extension across the pinned upper face.
ATTEMPTS/024--025 exclude deletion of a surviving axial correction
and an absolute-profile shortcut in a different trace. The proposed
specialization keeps the exact plateau, original endpoint and actual
exterior contraction, so it does not reopen those disproved shortcuts.

## One bounded continuation and stopping test

Keep the exact TARGET. Starting from L216(1),(15), test an N-explicit
bilinear energy comparison for all four traversal dipoles, using the
audited signed cumulative stencil and scalar dipole estimates above.
Quantify source-distance dependence before choosing a shrinking
transverse collar, or give a complete summed boundary estimate.
Bound coefficient freezing in energy without commuting C_(j,N) through
G. Include actual raw exterior modal errors, omitted mesh labels,
normal end rows and physical quadrature before the complete heat sum.
This names proof obligations, not a new estimate or a chosen parameter
substitution into L216's qualitative limit.

Continue only if the complete finite-N error can be bounded by
C_i N^(5/2)log(eN)^2 (or better), equivalently the normalized error by
O_i(N^(-1/2)log(eN)^2), with constants independent of admitted N and
summable mode dependence. An explicit obstruction invalidating a needed
uniform comparison is also informative. Abandon a particular transfer
if its buffer/collar or heat-label dependence necessarily misses that
threshold; a generic weak norm allowance is not signed response growth.
Do not claim the rate from qualitative energy convergence or L224's
different trace conclusion. Failure of this test would leave the
established plateau limit and L230's separate rate intact.

Essential continuation IDs: L025 L028 L042 L065 L101 L214 L215 L216
L222 L224, with L008's probes and upstream relative definitions retained.
These accepted analytic inputs are hypotheses, not recursively audited
facts in this review. No new boundary uniformity, compact axial tail,
smooth rough prefix, interacting expansion or component-rate assembly
is assumed. All signed entries, both residual subtractions, constant
modes and full heat sums remain. No cross-notebook theorem is used.
Mathematical exploration usage remains zero: this literature turn spends
none of that budget. Full matching and supporting Mathlib coverage are
not checked; unknown availability is not absence.
