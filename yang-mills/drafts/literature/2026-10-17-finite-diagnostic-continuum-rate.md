# Finite diagnostic to continuum — quantitative coverage

TARGET: Determine whether L080's finite diagnostic obeys |D_(i,a)-D_i| <= C_i N^(-1) for both actual probes, retaining the full heat spectrum and constant axial prefix.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L080 completely, L008 sections 1,2,4, L026 through (9), L070 section 6 through (9), the original diagnostic draft/history and ATTEMPTS/024–025; searched diagnostic/rate assessments for duplicates and searched quantitative finite-difference heat, Euler–Maclaurin and boundary gradient-flow results as recorded below.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), section 1.4(vi), (1.4.35)–(1.4.37), and section 2.10(i), (2.10.1), hypotheses and remainders read; Persson's author-hosted Math 228B notes, finite-difference construction and Dirichlet eigenpairs read; Rubeo–Sint, PoS(LATTICE2016)388, sections 2–4 and section 5's boundary qualification read.
COMPARISON: Taylor and Euler–Maclaurin provide quantitative smooth-function approximation inputs; the related finite-volume flow source has a different observable and boundary geometry. No inspected source supplies this complete diagnostic rate. L080 specifies every retained factor but proves only qualitative convergence; L221 excludes this rate. A mode-weighted specialization, rather than a reproof of the standard calculus results, is needed.
GAP: Prove a mesh-uniform polynomial-in-mode error envelope for L080's complete heat-weighted summand and control omitted mesh labels, including B_(i,a), upper curvature, actual lower prefix, strains and spatial quadrature; then obtain the requested N^(-1) bound for both probes.
REASON: Essential source coverage is now sufficient for one bounded specialization attempt on the unchanged target; this review establishes no diagnostic rate and no novelty claim.
LITERATURE_REASON: The new diagnostic-to-continuum rate was expressly outside the ready L221 assessment; this is its first separate source comparison, not additional literature on an already ready target.
SCOPE: SU(2), relative pinned cube, straight lower-rooted direction-1 forest, a=8/N on sufficiently fine admitted even meshes, tau=1/16, i=3,6, exactly L070/L079's D_(i,a) and L080's D_i. Fixed smooth displacement and fixed positive flow time only; no interacting or shrinking-flow-time assertion.

## Review performed, 2026-10-17

This separate literature turn approves a later mathematical attempt on
the exact TARGET. It does not prove that target. The proposed rate was
preserved throughout; no lemma or mathematical script was written.

Local duplicate check: `drafts/2026-10-08-first-pair-diagnostic-continuum.md`
and `history/101-2026-10-08-first-pair-diagnostic-continuum.md` record only
qualitative convergence. The original broad assessment
`drafts/literature/2026-09-26-current-target.md` concerns interacting
response/matching, not this quantitative approximation. Its saved source
descriptions were reused, without reopening those papers. The two
2026-10-17 L221 rate/audit assessments explicitly exclude the present
target. The narrowly searched diagnostic assessments yielded no completed
proof of this rate. This is a scoped duplicate check, not a novelty claim.

ATTEMPTS/024–025 stop deletion of the upper Dirichlet correction and an
axial-profile-only absolute-norm gain. The proposed specialization keeps
L080(8)–(10), including the zero axial frequency, exactly as stated.
Those stops therefore remain evidence against different shortcuts;
neither forbids this quantitative comparison.

External queries included:

- `finite difference heat semigroup sine eigenvalues error smooth data rectangular domain convergence rate`
- `Euler Maclaurin summation formula remainder first derivative DLMF 2.10`
- `"Yang Mills" "diagnostic" "lower" "prefix" convergence`
- `"heat" "finite difference" "eigenvalues" "sine" "error estimates" semigroup rectangular`
- `"finite difference" "heat trace" "convergence" rate`
- `"heat semigroup" "finite difference" "O(h" Dirichlet`
- `"Wilson" "flow" "tree level" "boundary" cutoff effects O(a) O(a2)`

No exact matching result emerged from this bounded search. Search snippets
and unrelated semilinear/fractional evolution results were not imported.

## Inspected quantitative inputs and comparison

1. NIST, [DLMF section 1.4(vi)](https://dlmf.nist.gov/1.4#vi),
   equations (1.4.35)–(1.4.37), version 1.2.8, released 2026-09-15,
   accessed 2026-10-17. Taylor's theorem assumes f in C^(n+1) on the
   closed interval and gives both Lagrange and integral remainders.
   These are the imported remainder formulas, not asymptotic series
   without error control. L008's fixed bump and L080's mode functions
   supply smooth scalar inputs. The later attempt must track their
   derivative constants as labels grow, apply the formulas to the
   staggered samples and dispersion, and use the existing spectral gap
   when comparing inverse square roots. No uniform-in-mode diagnostic
   estimate follows from this citation alone.

2. NIST, [DLMF section 2.10(i)](https://dlmf.nist.gov/2.10#i),
   equation (2.10.1), same version/access date. The Euler–Maclaurin
   formula is stated for integer endpoints n>a, positive integer m and
   absolutely integrable f^(2m), with endpoint corrections and a
   periodic-Bernoulli integral remainder. Use its smooth-function case.
   For the eventual spatial quadrature, each coordinate slice must be
   rescaled to the integer grid, all endpoint terms accounted for, and
   the four coordinate sums compared successively. L008/L080 place the
   coefficient support away from the faces. This theorem has no
   forest, gauge or boundary-trace assertion; those factors must remain
   explicit in the specialization.

3. P.-O. Persson, [*Finite Difference Methods for PDEs*, Math 228B](https://persson.berkeley.edu/math228b/html/finite_difference_methods_for_PDEs.html),
   live author-hosted notes, accessed 2026-10-17; no revision date stated.
   Read “Method of Undetermined Coefficients,” “Local Truncation Error”
   and “Stability Analysis.” The scalar Dirichlet example on (0,1)
   gives the centered second-difference matrix, its sine eigenvectors
   and eigenvalues 2h^(-2)(cos(p pi h)-1). Its truncation example uses
   smooth fourth/higher derivatives. This confirms standard numerical
   terminology and method; it does not cover mixed relative components,
   constant edge modes, the prefix or the present diagnostic. L026's
   exact relative eigenpairs are retained as the local input instead.

4. A. Rubeo and S. Sint, [*Perturbative O(a^2) effects in gradient flow
   couplings with SF and SF-open boundary conditions*](https://pos.sissa.it/256/388/pdf),
   published proceedings PoS(LATTICE2016)388, accessed 2026-10-17.
   Read printed pp. 2–5, (2.4)–(2.10), (3.1)–(3.6), (4.1)–(4.7),
   numerical comparison and footnote 2. Their finite-volume geometry
   is spatially periodic, with temporal SF or SF-open conditions;
   the observable is magnetic energy at the midpoint. Their Wilson
   momentum is 2 sin(ap_mu/2)/a. The displayed cutoff comparisons use
   numerical evaluation and tree-level time-boundary improvement.
   This is useful precedent, not a rigorous uniform bound for the
   present signed two-probe diagnostic on a cube pinned at all faces.
   In particular their omitted temporal component is needed here.
   Their reference [5], Ramos–Sint, arXiv:1508.05552, is an unread lead
   in this review, not an essential input to the explicit-mode route.

## Authorized specialization and discriminating test

L080 sections 1–5 already identify all finite and limiting quantities.
The remaining work is quantitative, and is authorized only for this
diagnostic:

- Keep the ordinary/physical normalization in L080(5) and the exact
  finite B entries in (6); quantify L008's polarized triplet average
  of squares and shear clover form separately.
- Compare the positive upper row using L080 section 2's actual relative
  endpoint values. Do not extend the interior forest potential through
  its separately pinned upper value or import a generic random trace.
- Use the full lower prefix in (8)–(10), treating axial index zero
  separately. Keep its physical distance, transverse derivatives and
  normal end rows; do not substitute a bulk axial profile.
- Quantify the smooth strains and the actual four-dimensional vertex
  quadrature. Bounds must concern the same staggered positions and
  coefficient supports as the definitions, including both probe sectors.
- Control the dispersion inside the heat exponent and the labels absent
  from the finite mesh. Establish an explicit summable, polynomially
  mode-weighted error envelope before summation. L080(13)'s qualitative
  majorant by itself is insufficient for a rate. No mesh-dependent
  cutoff may be justified by a fixed-cutoff convergence statement.

These are proof obligations for the next attempt, not results established
by this review. A short specialization is needed because none of the
inspected sources treats this assembled observable; rederiving Taylor,
Euler–Maclaurin or the already exact local eigenpairs is unnecessary.
The anticipated completed classification is REPRODUCTION under SPECIALIZE.

Essential input IDs: L008 L026 L070 L080 for the explicit construction;
L071 supplies the optional existing sector cancellation, L079 the trace
identification, and audited L221 the downstream quantitative comparison.
Their existing hypotheses and qualifications remain imported, without a
new upstream audit. No cross-notebook input is used.

Continuation/abandonment test: the later attempt succeeds only with a
uniform C_i N^(-1) bound after the complete heat sum for i=3 and 6.
Continue this mechanism if all local errors have controlled polynomial
mode dependence compatible with that sum. If an actual retained boundary,
prefix or form error cannot meet that threshold, preserve the precise
uncontrolled term and reassess this mechanism; a failed upper estimate
does not prove signed growth or disprove the requested rate.

A successful estimate could combine with L221 to quantify this selected
trace's comparison to 2 gamma D_i. It would leave the independent
L101 and other component rates, L220's pending recombination audit,
coupling-uniform control, matched reflected error <=c_box/2,
continuum axioms and finite positive infrared mass unresolved.
Mathlib coverage of the full diagnostic rate and supporting quantitative
quadrature results: not checked. No matching declaration or absence claim
is asserted. This literature-only EXPLORATION resolves coverage for a
bounded attempt; the mathematical target remains open.
