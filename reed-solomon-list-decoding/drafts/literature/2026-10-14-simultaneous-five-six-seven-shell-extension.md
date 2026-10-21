# Simultaneous distance-seven columns — source scope approved

TARGET: Test whether all L066 distance-seven columns can be retained simultaneously in a PSD extension of the unchanged L061 anchored five/six-shell matrix with consistent nonnegative unordered moments.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched mixed-layer constant-weight SDP, equal-union constrained completion and prescribed-column completion; compared L061,L062,L065,L066, ATTEMPTS/043,048 and the ready five/six-shell and fixed-column assessments. Queries and inspected primary passages are recorded below; no inspected theorem evaluates this fixed simultaneous prescription.
SOURCE_EVIDENCE: Schrijver DOI 10.1109/TIT.2005.851748, author manuscript Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59) and III.B (64), printed pp. 5–7; Sano DOI 10.1007/s44146-026-00231-y, Section 2 Theorem 2.1, Corollary 2.2 and Theorem 2.6 with their proofs; Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1/proof and Section 1.2 averaging, pp. 2–3. Primary passages read 2026-10-15; reuse canonical foundations/09,10,12.
COMPARISON: The known mixed-layer algebra and whole-block singular-Schur criterion cover the finite real enlarged matrix. L066 gives isolated columns and L061 a smaller simultaneous matrix; neither evaluates new/new coefficients, their unordered identifications or joint PSD. Free-entry completion theorems do not enforce these moment constraints.
GAP: Research must check complete full-region consistency of the immutable prescriptions, justify any invariant reduction and its normalization, and certify every surviving mixed-layer block including new-only and singular modes. No joint feasibility or obstruction is established here.
REASON: Essential source coverage is adequate for one bounded exact specialization. The enlarged fixed prescription needs a new application and certificate, without reproof of the hierarchy, algebra or general completion criterion.
LITERATURE_REASON: Adding all distance-seven columns changes the scope beyond both the approved one-column energy test and the earlier simultaneous five/six-shell test; this separate review resolves that specific coverage gap.
SCOPE: Exactly TARGET with positive original rho, original pairs including p7=3539/248922676958508, every L062 dictionary entry and exactly L065/L066's u=v=0,w=-c_4/a^42_4 column at every new index. Only consistent nonnegative remaining moments and this complete included-anchor matrix; no retuning, extra scalar upper rows, labeled constraints or global feasibility claim.

Main gap: arbitrary-center safety at 67/68 agreements, finite bracket 955–957.
Intermediate target: a simultaneous extension retaining every fixed L066
column, with new/new entries consistent under all eligible anchor orders.
Downstream use: test joint compatibility that is not implied by isolated
one-column passes, before drawing any global feasibility conclusion.
Continue if exact nonnegative consistent new entries and full PSD can be
certified; an exact incompatibility or obstruction rejects only this fixed
simultaneous prescription. No feasible certificate or obstruction is derived
here. Prior ATTEMPTS/043 and /048 concern smaller retained slices and remain
valid; they do not settle this joint test.

The initial proposal above was REVIEW_REQUIRED at step 225. Step 226
approves only its source scope; no extension, obstruction or new lemma
has been derived in this literature turn.

## Primary theorem comparison

Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[eight-page author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
at the locations in SOURCE_EVIDENCE. Read the orthogonal block argument,
tensor change of basis and complete extension/reset proof of (58).
Unequal layer indices are allowed. With factor sizes 68 and 956,
layers 0,5,6,7 lie in the source ranges. Select these layer coordinates
and retain every source block meeting them. Formula (64) gives a
congruent beta form; use foundations/04's existing convention. The
suspect complement prefactor is unused. This algebra applies to invariant
matrices without a code or representing measure. It supplies no coefficient
values or signs for this prescription. Normalization and full-space
exhaustion must be verified in the application, including modes absent
from the smaller base.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum, version of record
27 February 2026, DOI 10.1007/s44146-026-00231-y,
[Section 2 publisher text](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For finite Hermitian [A,B;B*,C], Theorem 2.6 requires C PSD,
ker(C) contained in ker(B), and A-B C^dagger B* PSD. A may be an
entire block; singular C needs no maximal-rank assumption. The complete
proof uses the PSD square root for kernel necessity and Corollary 2.2's
invertible triangular congruence for both directions. Theorem 2.1's
range conditions and multiplication proof were also inspected.
Here C is the retained L061 base, B is the transpose of the proposed
cross block, and A is the new/new block. This identifies applicable
hypotheses, without evaluating the joint Schur remainder. Retain the
anchor throughout, or transport the whole matrix by congruence.
Do not transport a pseudoinverse alone or replace the remainder by
its diagonal energy tests. Foundations/10's range-inverse coverage
remains reusable; no new inverse theorem is needed.

Import Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and its complete indicator proof,
printed p. 2, and Section 1.2, p. 3. Its union-index matrices require
one coordinate for equal unions; nonnegativity and the constant-weight
qualification are as recorded in foundations/12. The displayed
Proposition ends with A(n,d), while its proof proves A(n,d,w); retain
the latter. The new indices belong to the singleton-conditioned
order-three matrix at n=1024,d=10,w=68. Its stronger A4/B4 programs
impose additional constraints, not a theorem completing arbitrary fixed
coordinates. Averaging requires a constraint-preserving group action;
verify that condition for this ordinary slice before using it.

Reuse the free-block completion comparison in foundations/10 and the
approved five/six assessment: Dreyer, arXiv:2112.03758v1, Theorem 5.2
and proof, pp. 10–11, leaves its cross block unrestricted. Grone–Johnson–
Sá–Wolkowicz, LAA 58 (1984), Theorem 7 with Proposition 2, concerns
partial PSD completion without equal-union or entrywise nonnegativity
requirements. These comparisons were reused, not freshly read. Their
hypotheses do not remove the present constraints. Albert (1969), Theorem 1
remains an unread original lead; Sano supplies the required primary proof.

## Exact specialization obligations

Essential inputs: L061,L062,L065,L066, transitive
L021,L053,L056,L059,L060 and foundations/09,10,12. Retain all original
pairs, positive rho and precisely the fixed column in SCOPE. For one
fixed D add every {D,G} with |D\G|=7; each diagonal and entry against
{D} is rho*p7. Keep every old entry and all cross-column prescriptions.
New/new entries must retain any L062 or fixed-column value encountered
under an eligible presentation, vanish for forbidden pair distances,
and otherwise use nonnegative moments shared by every equal unordered
full-region key. Boolean repetitions use their original lower-order
moments. No missing entry is assigned in this review.

First compare every eligible presentation and canonical unordered key,
including reanchoring that leaves the selected layers. An exact clash
already rejects this prescription; do not remove a presentation or
retune the three-parameter family. If consistent, justify any averaging
under point permutations fixing D by checking that all fixed entries,
zeros, identifications and nonnegativity are preserved. The existing
columns use full-region keys, but joint equivariance and consistency
remain application obligations. Actual subgroup-label restrictions are
outside this ordinary slice and cannot be averaged this way.

Then check the complete mixed-layer PSD reduction with both old layers,
the anchor, all singular cross-mode conditions and new-only modes.
Recover the unchanged base and column data exactly. A positive result
needs a complete rational assignment and exact full PSD certificate;
a negative result needs an exact conflicting value, negative quadratic
form or independently checkable dual contradiction. Failed numerical
search or solver status proves neither. Save complete relevant evidence.
No theorem is reproved: the required work concerns this fixed dictionary.

A pass parks this larger exclusion diagnostic; an obstruction rejects
only this simultaneous prescription. An unresolved bounded attempt must
save its concrete residual test. Other scalar rows, global moments/PSD,
labels, measures, packing and RS realization remain independent gaps.
Do not infer an unsafe RS list or change the 955–957 bracket.

## Search, duplicates and limits

Queries on 2026-10-15 were: "constant weight Schrijver semidefinite mixed
layers prescribed moments positive semidefinite completion"; "positive
semidefinite completion equal union moment constraints prescribed columns
generalized Schur complement"; "Schrijver constant-weight
block-diagonalization layers"; "semidefinite completion moment
constant-weight"; and "positive semidefinite prescribed columns
completion". Searches returned Polak's stronger four-point hierarchy,
general completion/moment literature and split-Terwilliger leads.
Only the primary passages identified above support this assessment.
No inspected theorem supplies the fixed verdict; that is not a novelty
claim. Laurent–Varvitsiotis constrained completion, split-Terwilliger
and matrix-valued flat-extension papers remain unread, nonessential
leads, with no result imported from snippets. The finite singular
criterion and mixed-layer theorem already cover the required mechanism.

The notebook-local search of foundations, assessments, ATTEMPTS and
history found only the proposed joint target and its step-225 routing.
L061 and ATTEMPTS/043 stop the smaller five/six diagnostic; L066 and
ATTEMPTS/048 stop one-column energy exclusion, now critically reviewed.
Neither is a duplicate joint verdict or a ban on this stronger test.
Preserve all earlier stops and unfinished work. The previous ready
assessments were reused for unchanged inputs rather than reopened as
independent research targets.

Approve one REPRODUCTION mathematical attempt at exactly TARGET under
this SPECIALIZE assessment. No lemmas or mathematical scripts were
written or run, and no feasibility result is claimed. Full matching
Mathlib mixed-layer, singular-Schur and Boolean-constrained completion
coverage is not checked; unknown availability is not evidence of absence.
