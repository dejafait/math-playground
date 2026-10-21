# Compatible-jet obstruction with the omitted first linear mean

TARGET: Test whether a joint-sign-avoiding law in L414's relaxation can also match L369's negative first Bcal mean while retaining every existing constraint.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 142 reused the step-138/140 moment and atomic assessments, compared L369/L414 and the scoped L410/L412/L413 failure records, and searched added first-moment/support-constrained mixed-moment terminology and exact discriminant/Hardy-statistic terms; no inspected matching feasibility theorem or separator was established.
SOURCE_EVIDENCE: Reinspected Bayer--Teichmann arXiv:math/0502473v2, Theorem 1, Corollaries 1--2, Remarks 1--2 and both proof cases, pp. 2--4; Bertsimas--Popescu final SIAM J. Optim. 15 (2005), Section 2/Theorems 2.1--2.2 and the weak-duality proof, pp. 784--785. Reused L369's audited (1)--(2) and its primary-source assessment, and the unchanged quartic/absolute-envelope coverage behind audited L414.
COMPARISON: The measurable-map theorem covers the extra signed coordinate conditionally on an existing integrable law, with at most 30 atoms preserving the listed integrals. It does not prove simultaneous feasibility. The existing law misses the new constant-scale mean; leading quartic coverage cannot supply its lower-order calibration. Strong duality, uniform atom positions and actual-family realization are not imported.
GAP: Construct and verify a law satisfying the entire enlarged list, or give a pointwise separating inequality with a gap surviving all stated errors; neither alternative is established in this review.
REASON: Essential source coverage now suffices for one bounded specialization of the finite-moment framework using the existing exact local identities; the support construction or separation remains mathematical work for a later turn, with no new zeta moment required.
LITERATURE_REASON: The added L369 first mean changes the selected-information scope and was explicitly excluded from the ready step-138 assessment; this review addresses that coordinate and its simultaneous normalization rather than refreshing unchanged quartic literature.
SCOPE: Exactly L414's stated local-jet relaxation plus L369 (2), with fixed constants and one onset for all sufficiently large real H; no uniform height marginal, actual response/global realization, new higher moment or regulator conclusion.
COVERED_TARGET: Test whether a joint-sign-avoiding law in L414's relaxation can also match L369's negative first Bcal mean while retaining every existing constraint.

The exact proposed extra constraint is

    E Bcal=-zeta(3)/(4pi)+O(1/log H+H^(-1/2)(log H)^2).

Retain all of L414's hypotheses, support, 21 matrix limits, five scalar
benchmarks, both jet envelopes, response bounds and exact curvature,
with fixed constants and one onset for all sufficiently large real H.
Do not silently impose a uniform height marginal, actual response
realization, a global function pair or further unproved moments.

The main gap remains actual clipping and the full regulator margin on
the route toward global mixed positivity. The intermediate target tests
whether an already known sign-sensitive input defeats the selected-law
obstruction. Its plausible downstream use is to distinguish an omitted
usable constraint from a need for stronger physical information. It
does not revive the unchanged implication already stopped by L414.

Essential inputs are L369 and L414, retaining the latter's
L367/L368/L370/L390/L393/L401/L405/L410 input scope. L410/L412/L413
remain distinct recorded failures. Reuse the existing moment and atomic
assessments where applicable; check specifically the added lower-order
mean and simultaneous normalization. No new zeta theorem is proposed.

The separately reviewed continuation requires either a
law meeting the entire enlarged list or a rigorous separating inequality
whose gap survives the stated errors. Failure of this particular law or
one atom ansatz is not a separator. Abandon that implementation if it
needs unavailable higher moments or an unproved actual joint law.
Actual clipping, L413's scale/full-error margin, common-zero upper counts
and global positivity remain independently unresolved in either case.

Step 141 proposed this target without approving or attempting it. Step
142 completes its source-scope review below; no new lemma, feasibility
claim, novelty claim or mathematical attempt is recorded here.

## Completed source comparison — step 142

The exact TARGET is unchanged. The earlier proposal is now covered for
one later bounded mathematical attempt. This literature turn does not
derive a new law or test an enlarged atom ansatz. Its outcome is
EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: usable scope is established,
but no feasibility result or new mathematical obstruction is claimed.

### Primary coverage and applicability

Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's Theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
DOI [10.1090/S0002-9939-06-08249-9](https://doi.org/10.1090/S0002-9939-06-08249-9),
[arXiv:math/0502473v2, Corollary 2, pp. 3--4](https://arxiv.org/pdf/math/0502473v2#page=3)
(4 May 2005): a positive measure concentrated on a measurable set and
an integrable N-coordinate measurable map admit at most N positive
atoms in that set preserving its integrals. Theorem 1's full-dimensional
and supporting-subspace cases and Corollary 2's pushforward/lifting proof
were reinspected. Import the theorem without reproof.

For a proposed law use the 30 coordinates

    (1,Bcal,Delta,Delta^2,Delta Bcal,Delta Bcal^2,|Bcal|^3,
     (Delta omega_i omega_j)_(i<=j),U^2,U^(3/2)).

This is L414's map with Bcal added. Its support is Borel and the map
measurable, with the same continuous envelope coefficients. Absolute
integrability is required; the existing third-absolute-moment constraint
also ensures integrability of Bcal by Holder. The constant retains mass
one. Applied separately at each H to an existing admissible law, the
citation preserves its actual finite integrals, hence their tolerances.
It proves no feasibility or uniform atom positions. No extra moments
or compactness hypothesis are needed for this conditional use.

Dimitris Bertsimas and Ioana Popescu, *Optimal Inequalities in Probability
Theory: A Convex Optimization Approach*, SIAM J. Optim. 15 (2005),
780--804, DOI [10.1137/S1052623401399903](https://doi.org/10.1137/S1052623401399903),
[final author PDF, Section 2, Theorems 2.1--2.2, pp. 784--785](https://web.mit.edu/dbertsim/www/papers/MomentProblems/Optimal-inequalities-in-probability-theory-A-convex-optimization-approach-SIAM15.pdf#page=5).
The weak-duality proof integrates a pointwise majorant. Strong duality
requires an interior feasible moment vector, and attainment is not
automatic. These passages were reinspected; their references to Isii,
Karlin--Studden and Shapiro are not newly imported theorems. No interior
condition is established for this sparse height-dependent problem.
The compact semialgebraic/SOS qualifications in the step-138 assessment
remain in force. A future separator must be proved pointwise on the
whole selected support and its integrated gap compared with every
allowed asymptotic error. Failed numerical or restricted-atom searches
do not establish infeasibility. No complete duality or SDP algorithm is
asserted here.

### Reused zeta coverage and the changed scale

L369 (1) defines exactly the ordinary-derivative normalized Bcal used
by L414, not a derivative of a normalized jet or a regulator curve.
Its (2) and completed October-5 critical audit supply the new mean with
H-independent error constant. Reuse
[the linear-mean audit assessment](2026-10-05-gaussian-linear-response-mean-audit.md)
and [its source comparison](2026-10-05-gaussian-linear-response-sign.md):
Arias de Reyna, [arXiv:2406.16667v1, Theorem 6 and proof, pp. 5--6](https://arxiv.org/pdf/2406.16667v1#page=5),
with its fixed-cutoff domain sigma>=0, 0<t<=x, and the cited
DLMF reflection/gamma inputs. Their previously inspected proof cases
are reused, not freshly retrieved or reproved. No stronger scalar
theorem is required for the abstract-law test.

Reuse the primary Hughes--Young/Bui--Hall/carrier and Curran--Heycock
coverage in
[the step-138 assessment](2026-10-15-jet-supported-moment-feasibility-review.md)
and [the step-140 audit assessment](2026-10-15-compatible-jet-law-critical-audit.md).
Critical jets still stop at order two; the matrix and the response
tails are unchanged. The later construction must retain every L414
constraint on the same law: all 21 exact leading matrix coefficients,
five scalar benchmarks, both U envelopes, ordinary/envelope conversion
with exact curvature, support including its axes, response errors and
annulus/lower bound, and fixed qualitative pointwise bounds. It must
retain both the E Delta mean and the added E Bcal mean. Existing
quartic-scale replacements may not be used to discard a constant-scale
error in the latter. One common onset must cover every real H beyond it.

L414's audited formula E Bcal=O(ell^(-2)) records only the failure of
its particular law to satisfy the added requirement. It is not a
separator. No signed mean of Bcal on either discriminant sign-set is
available from the imported citations; none is assumed.

### Bounded search and preserved stops

Fresh queries included `"moment problem" "mixed moments" "negative
mean" support probability`, `"Tchakaloff" "measurable" "Corollary 2"
Bayer Teichmann`, `"Hardy" "derivatives" "joint" "sign" moments zeta`,
`"discriminant" "zeta" "negative" "moment" Hardy`, `"Bayer"
"Teichmann" "first moment" measurable functions`, and `"moment
problem" prescribed moments support "sign" mixed moments`. Search
results were locators, not theorem evidence. The primary passages
above, rather than snippets, justify the approved framework. No exact
matching feasibility result was established. Core-variety refinements,
random-matrix joint moments and other general moment-problem articles
remain unused leads, not essential unread inputs; no novelty follows
from this bounded search.

Targeted local reads covered L369's statement/audit, full L414,
the step-141 draft, the step-138/140 assessments and the exact
L410/L412/L413 failure records. L410 omits this mean and the full
jet support. L414's tested scope explicitly omits this mean. L412
stops frozen scalar half-turn pairing, while L413 stops deriving the
shrinking-window margin from favorable joint signs alone. None decides
the enlarged feasibility question. These historical stops are preserved;
none is a global ban on testing an additional known constraint.

Continue with the unchanged TARGET only. A successful construction must
check every error scale and the fixed constants simultaneously; a
separator must survive their tolerances. Stop a particular implementation
if it requires an unavailable higher moment, actual joint distribution
or uncontrolled lower-order replacement, recording that failure without
calling it an infeasibility theorem. Actual clipping, the regulator
scale/full-error margin, common-zero upper counts and global mixed
positivity remain independent gaps in either outcome. No RH candidate
or change to PROOF.md or DAG.md follows from this source review.

Full matching Mathlib coverage for the enlarged construction, measurable-map
theorem and complete moment inputs remains **not checked**. Unknown
coverage is not absence or formal verification. No lemmas or mathematical
scripts were modified or run.
