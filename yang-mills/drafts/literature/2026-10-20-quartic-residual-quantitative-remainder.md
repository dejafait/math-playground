# Complete quartic residual — quantitative source comparison

TARGET: Assess source coverage for the complete quartic-residual remainder |kappa_0(f_(i,0),r_2)-a^(-3)Lambda_i|=O(N^(5/2) log(eN)^2) for both actual probes.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L149's complete insertion, L150's local covariance proof, L151/L152's full limit arguments, L114's relative heat comparison, L222's modal/probe estimates and L248's raw/heat comparisons; checked the old quartic and diagnostic assessments, selected quartic histories and ATTEMPTS/011,036. External queries and primary cases inspected are recorded below; no exact complete-rate match was established.
SOURCE_EVIDENCE: Reused the inspected Ward/flow/Symanzik and Adams--Lee scope records; inspected Lawler--Limic, Random Walk: A Modern Introduction (2010), author-posted 289-page PDF, section 1.1, Theorems 2.5.6 and 4.3.1, Proposition 4.6.2(a), and Lemma 6.3.3 with its transient proof. Reused the DLMF remainder comparison in the saved L222 assessment.
COMPARISON: L150/L151 already supply the quantitative local projection-row input, while the projected co-closed local covariance and L152's derivative/heat convergence remain qualitative. L222(2)--(7) match the underlying normalized modes, strains and both complete probe matrices; L248(3)--(11) match raw forest values and heat weights but do not state the required exterior-derivative rate. Scalar walk results support methods, not a direct import of this complete signed bare response.
GAP: Quantify L151's projected local co-closed covariance comparison and L152's exterior first-derivative and displacement/insertion comparisons, with a polynomial mode envelope before the full heat sum, then bound all five contributions against exactly L152(8). No such quantitative refinement is proved in this review.
REASON: Adequate standard and local source coverage supports one bounded signed-local refinement attempt; no essential inaccessible theorem is required. EXPLORE records the absence of an adequate match in the bounded search, not novelty or a rate theorem.
LITERATURE_REASON: Essential quantitative coverage for this distinct complete insertion is not supplied by the old cubic-limit assessment or completed L221--L253 component rates.
SCOPE: Unchanged relative SU(2) cube, lower-rooted direction-1 forest, even admitted N, a=8/N, tau=1/16, bare-first order, stored coordinates and complete actual probes 3,6. Only the quartic residual remainder is covered; all source/end rows, constants, two subtractions and complete heat sums remain.
COVERED_TARGET: Prove the complete quartic-residual remainder |kappa_0(f_(i,0),r_2)-a^(-3)Lambda_i|<=C_i N^(5/2) log(eN)^2 for both actual probes.

## Review completed, 2026-10-20

This is a literature-only EXPLORATION. No bound, new lemma, mathematical
script or proof audit was produced. The registered mathematical target
was preserved. The covered continuation is proposed for a separate
invocation and the supervisor's separate approval of newly ready scope.

The main gap remains the interacting reflected error <=c_box/2,
continuum axioms and finite positive infrared mass. The intermediate
target is the complete I_i^(4) remainder, not another evaluation of
Lambda_i. Its plausible use is to close one of the four missing complete
rate blocks in the L218 inventory. The other three blocks and all
interacting/construction requirements remain independent.

### Local comparison and duplicate/failure screening

L149(2),(7) fix the tensor, all twelve connected pairings and the two
insertion subtractions. L150 section 1 proves its single-row projection
estimate (5), including every normal end input. L151(11) already
records the resulting local j_* projection error
O(N^(-1/2)(log N)^(3/4)). This is existing quantitative coverage;
there is no reason to reproduce that projection theorem.

In contrast, L151(4) controls the projected co-closed local covariance
only by o(1). Its sections 1--2 give the exact heat representation,
uniform integrable tails, and parity decomposition, but its fixed-time
polynomial comparison is qualitative. The stationary even covariance
and absolute-value kink disappear only against the complete frozen
odd tensor; the axial slope survives. A future attempt must quantify
the comparison before that contraction, or justify a stronger joint
signed estimate. No global covariance approximation is authorized.

L152(12)--(15) identify the other required comparisons. Its uniform
C^2 convergence is enough for its limit, but supplies no quantitative
modulus for the exterior first derivatives. The frozen zero avoids an
unknown diagonal first-order coefficient; it does not remove the need
to compare the derivative term with the continuum functional at a rate.
The two insertion tensors and shifted Riemann sums also remain.

The exact normalization matches these supporting inputs:

| Existing input | Applicable part | Part still requiring proof |
| --- | --- | --- |
| L222(2)--(4) | Same relative product modes A_(k,a)=f_k/sqrt(lambda_(k,a)), dispersion gap, and fixed u,w,s coefficients; all zero own-direction indices retained. | Transfer the smooth coefficient estimates to L152's precise midpoint jets and required derivatives. |
| L222(6)--(7), L248(10)--(11) | Same full L008 triplet average of four products and both polarized shear clovers, with their normalizations; polynomial pair errors and heat-weight envelopes are stated before summing. | Use those matrices inside L152(6), rather than transfer either source's final diagnostic or trace bound. |
| L248(3)--(8) | Raw, unaveraged forest link values, exact prefix and constant axial case; the continuum column agrees with L152(5) on compact interior rows. | Its stated C^0 raw error is not a C^1 error for L152(7); check the exact sine primitive with differentiated remainders. No upper-pin continuation is permitted. |
| L150(5), L151(11), L114(4)--(6) | Actual relative incidence, projection heat calculus and compact-output walk comparison retain all inputs. | A quantitative bound for L151's entire projected two-level H_N-H_inf is not stated by these inputs. |

This matches only the listed supporting estimates. It does not audit
their proofs recursively, identify unrelated exteriors, or import the
final L222/L248 conclusions into the new response. Essential IDs are
L011 L149 L150 L151 L152 L153 L154; supporting IDs are L008 L028
L085 L114 L222 L248. Lambda_i is the full L152(8) coefficient,
identified in L153/L154, with no numerical sign premise needed here.

Scoped literature/history searches found the old cubic-limit assessment,
histories 181--182 and the new registration/inventory, but no completed
quantitative quartic remainder. L153/L154 evaluate the limiting
functional; evaluation is not remainder control. ATTEMPTS/036 stops
the unsigned local count, and ATTEMPTS/011 stops an O(1) raw-loop
premise. Both remain preserved. The new question refines the later
signed limit mechanism and does not reopen those failed shortcuts.

### Primary source checks

New bounded queries were:

- `discrete Green function lattice asymptotic derivative killed box heat kernel projection Lawler Limic theorem 4.3.1 pdf`
- `lattice Green function asymptotic expansion finite differences Martinsson Rodin 2002 lattice Green function`
- `"killed" "Green" "quartic" "forest" Yang Mills residual remainder`
- `"discrete Hodge" "projection" "Green" "convergence rate"`
- `"axial gauge" "quartic" "lattice" "remainder"`
- `Dirichlet lattice heat kernel interior comparison free heat kernel gradient boundary estimates`

Search returns did not establish an exact theorem for this response.
Martinsson--Rodin's infinite-lattice expansion and general continuum
Dirichlet heat-kernel papers remain unread leads, not imported results
or essential premises. No novelty inference follows from this search.

**Lawler and Limic, Random Walk: A Modern Introduction, Cambridge
University Press, 2010, [author PDF](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
289 pages, accessed 2026-10-20.** Section 1.1, printed pp. 9--11,
defines P_d as finite-range symmetric irreducible walks. Theorem 4.3.1,
pp. 81--83, gives the transient Green asymptotic with O(|x|^(-d))
error for p in P_d, d>=3. Proposition 4.6.2(a), p. 97, gives
G_A(x,y)=G(x,y)-E^x[G(S_(tau_A),y);tau_A<infinity]; its transient
proof retains the exit distribution. Lemma 6.3.3, pp. 127--128,
assumes B_(epsilon n) subset A proper subset Z^d, d>=2,
|x|>epsilon n and |y|<=r, and bounds first and symmetric second
differences by c n^(1-d) and c n^(-d). Its proof uses symmetry and
the exit identity. Theorem 2.5.6, pp. 58--59, is a one-dimensional
continuous-time local central limit estimate for |x|<=t/2, not an
all-displacement boundary bound. Statements and the relevant exit/
difference proof cases were read. Nearest-neighbor scalar walks meet
the hypotheses; time/generator normalizations must be matched.
None states a mixed relative-edge projected forest contraction.

These results need no reproof. Their scalar domain and difference
conditions must be checked if used; they do not replace L114's actual
relative extension or L151's nonlocal projection heat integral.

Reuse the precise DLMF Taylor/integral remainder and quadrature
assessment in `2026-10-17-finite-diagnostic-continuum-rate.md`,
section “Inspected quantitative inputs and comparison,” items 1--3.
The required smooth functions are the same finite trigonometric modes
and fixed compact cutoff. Higher derivative mode constants and the
full heat-summable envelope are the specialization still to establish.
Taylor's theorem and standard scalar walk results are not the research
target. No fresh general theorem is to be reproved merely to rename it.

The inspected flow/Ward/Symanzik and Adams--Lee comparisons in
`2026-10-12-quartic-residual-insertion-cubic-scale.md` and
`2026-10-20-complete-coefficient-remaining-rate-gaps-audit.md`
remain adequate and are reused without new browsing. Their pinned
geometry, complete-response and momentum-integral scope exclusions
are unchanged. None supplies the present bare local remainder. The
official Jaffe--Witten statement version remains the one recorded in
that inventory; no target hypothesis has changed.

### Bounded continuation and stopping test

Attempt only the COVERED_TARGET, starting from the exact L152(15)
decomposition and comparing against exactly its (8). First seek a
quantitative projected covariance comparison and a derivative mode
envelope strong enough for the normalized remainder
O(N^(-1/2)log(eN)^2). Then retain every term in the complete response;
a successful intermediate covariance comparison is useful even if
the independent exterior comparison remains unresolved.

No quantitative H_N-H_inf modulus, C^1 raw-link rate, or full
derivative heat envelope is assumed. These are proof obligations.
Use the existing projection-row estimate, not the stopped absolute
raw-loop bound. Keep both arguments of H distinct when differentiating,
the exact midpoint offsets, stationary/kink parity, axial slope,
constant prefix, both subtractions, every color and heat label, and
the single factor twelve with no outside factor 3.

Continue upon a rigorously bounded complete remainder or a relevant
independent comparison with an explicit adequate error envelope.
If a required comparison loses the threshold, record the actual bound
and the unresolved term; an upper-bound loss is not signed growth.
Abandon an attempt based only on qualitative limits, final-time damping
of the internal pair, full matched Ward formulas, or a global bounded
forest covariance. A newly necessary theorem outside this scope needs
REVIEW_REQUIRED before dependent work. Persistent essential source
blockage would park this target; none was encountered here.

Full matching Mathlib coverage and supporting discrete probability
coverage are **not checked**. Unknown availability is not absence.
This source step establishes no new mathematics and no candidate
Yang--Mills solution. PROOF.md and DAG.md are unchanged.

## Original registration (historical)

The main gap is interacting reflected error <=c_box/2, continuum axioms
and finite positive infrared mass. This remainder could close one of four
remaining complete-partition rate blocks, leaving the other three and
all interacting/construction requirements unresolved.

Essential inputs are L011 for the original coefficient, L149 for the
complete tensor and twelve connected pairings, L150 for exact frozen
cancellation, L151 for the covariance slope, L152 for the precise limit,
and L153/L154 for identification of Lambda_i. Inspect L222/L248 only
as possible supporting modal/raw comparisons. Transfer to this different
exterior and its derivatives is unresolved. No quantitative covariance
modulus or fully heat-summable error envelope is assumed.

Keep SU(2), the all-face relative cube, straight lower-rooted direction-1
forest, admitted even N, a=8/N, tau=1/16, stored coordinates, bare-first
order and probes i=3,6. Retain all colors, boundary/source rows, constant
modes, actual prefixes, both subtractions and the factor twelve once;
there is no outside factor 3. No numerical Lambda_i sign is needed.

Read exact L151/L152 hypotheses and relevant proof cases before larger
source extracts. Reuse primary comparisons; check precise known local
Green/projection rates and boundary hypotheses as needed. ATTEMPTS/036's
unsigned count and ATTEMPTS/011's bounded raw-loop shortcut remain
stopped. A signed local rate refinement is a different test.

Continue if source coverage matches the actual finite signed contraction
or identifies a bounded independent comparison with an error envelope
capable of meeting the target. Register the mathematical attempt for a
separate invocation. Reject imports covering only translation-invariant
momentum integrals, full matched Ward responses, or qualitative limits
without pinned/heat uniformity. Park dependent work on persistent
essential source blockage. Mathlib coverage is not checked.
