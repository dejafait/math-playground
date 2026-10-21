# Sign-reversed mixed tensor — necessity-test source assessment

TARGET: Determine which integer pure factor-point corrections pass the rank-two topological, Bogomolov and factor-polystability tests when the mixed tensor is -tau_D at the same common metric.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Repeated the notebook-scoped sign/duplicate search and checked primary-source search leads for rank-two K3-product hyperholomorphic bundles, finite-rank quaternionic-line realization, Perego Corollary 6.42 and Verbitsky Theorem 3.9; queries, inspected passages and unread leads are distinguished below. No matching classification of the changed fixed-tensor correction region was identified; no novelty inference is made.
SOURCE_EVIDENCE: Read the corrected author-hosted Čadek--Crabb--Vanžura manuscript, Introduction and Section 8 Proposition 8.2/Corollary 8.4 including their proofs, pp. 1, 11--13; Perego arXiv:1910.01867v1, Definition 4.7, Corollary 6.42 and Theorem 5.1, pp. 59, 118, 66; Verbitsky arXiv:math/0107182v10, Definition 2.1, Definition 3.2, Proposition 3.7, Lemma 3.8 and the complete Theorem 3.9, pp. 9, 11, 13--14. Reuse assessed Huybrechts surface statements and Stacks character/HRR inputs with unchanged hypotheses; precise locators below.
COMPARISON: The primary criteria accept an integral second Chern class and invariant first two Chern classes without prescribing the mixed sign. They cover the framework, not this numerical region or holomorphic existence. Reuse L044's metric and integral tensor, L048--L050's full-lattice conventions and L051--L052's case analysis only after the changed-data applicability checks; recompute every output region rather than importing its old bounds. L070 and the negative-presentation warning retain their original scopes.
GAP: Evaluate the sign-reversed Bogomolov contraction and finite-rank characteristic number, justify the stable/split connection passage for the changed tensor, and intersect the necessary factor tests. No changed numerical region, excluded pair or existence conclusion is established by this source review.
REASON: Essential source coverage is ready for one bounded REPRODUCTION of the known frameworks on the changed lower-character data. It can reject impossible inputs or delimit a concrete later existence test; global holomorphic realization and transverse transport remain independent gaps.
LITERATURE_REASON: Changed mixed second-character tensor from +tau_D to -tau_D; prior sign-specific necessity assessments do not cover the new target verbatim.
SCOPE: All integer a,b with c_1=0 and ch_2=(a+4)e_1+(b+4)e_2-tau_D on L044's marked K3 product at the identical real common metric; rank two, locally free and slope-polystable for the conditional holomorphic tests, unrestricted initial higher characters/K-class. Covers necessary topological, Bogomolov and stable/split factor tests only, with no old numerical region imposed and no existence or transport assertion.

## Proposed scope and use

Keep the identical marked cubic RM K3 factors, L044's final common
hyperkahler metric h, the same integral tensor tau_D and self-adjoint
operator D, and the real product polarization. The proposed F is
rank two and locally free, slope-polystable, with c_1=0 and
ch_2=(a+4)e_1+(b+4)e_2-tau_D for integers a,b. Its higher characters
and initial K-class are unrestricted. No presentation, factor
stability, connection existence or transport is assumed without
checking the applicable theorem. The old a+b and congruence regions
are outputs to reassess, not hypotheses restricting the new test.

Essential input IDs: L044 for the final metric and full D; L048 and
L049 for Chern truncation/index conventions; L050 for the cited
finite-rank topological criterion; L046 and L047 for the old real-class
Bogomolov comparison; L051 and L052 for the product splitting and
factor-restriction framework; audited L070 for the stopped sign-specific
route. Read their relevant canonical ranges and the cited primary
hypotheses narrowly. Preserve all old conclusions in their original
scope. No cross-notebook input is proposed.

The main gap remains universal primitive rational Hodge algebraicity.
The downstream possibility is a kernel realizing an opposite cubic
correspondence action, whose rational cycle multiple could still be
useful for the original action. This is motivation, not a constructed
kernel, a realization claim or a transport theorem. Rank-two
holomorphic existence and transverse transport remain independent
unresolved steps even if necessary numerical tests have survivors.

Continuation test: approve one bounded calculation only if the exact
changed lower-Chern data fall within the primary theorem hypotheses
and every sign-sensitive comparison is identified. That later
calculation should determine an explicit integer region or prove it
empty; incompatibility stops this input. A nonempty necessity region
would justify a separate, concrete existence or further obstruction
target, without treating numerical compatibility as existence. If an
essential source is inaccessible, record SOURCE_BLOCKED and park the
dependent work. This proposal does not reopen the exhausted positive
fixed tensor, charge-seven metric-sign or flat-index routes.

## Source comparison completed on 2026-10-08

The exact TARGET above is now SPECIALIZE. This completes its separate
literature approval; it does not execute the numerical test. The next
research step should be classified REPRODUCTION. Known general theorems
are imported, and only their changed-data applicability and arithmetic
specialization require work. No general theorem needs a reproof.

### Primary topological criterion

Use Čadek--Crabb--Vanžura, *Obstruction theory on 8-manifolds*,
author's manuscript dated 5 December 2007, corrected 8 July 2008,
[Corollary 8.4, p. 13](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=13).
On a connected closed smooth spin-c eight-manifold M, choose a complex
line with first Chern class l reducing to w_2(TM). For integral
u in H^4(M,Z), a quaternionic line for that coefficient line, with
c_2=u, exists precisely when

\[
\operatorname{Sq}^2\rho_2(u)=\rho_2(lu),\qquad
\frac14\langle p_1(TM)u+2u^2-l^2u,[M]\rangle\equiv0\pmod{12}.
\]

The characteristic expression is integral under the first condition.
Read [Proposition 8.2 and proof, p. 12](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=12)
and the corollary's proof: the zero Euler class splits a quaternionic
summand, supplying complex rank two rather than just stable rank four.
The corrected author's copy, not the older arXiv v1, supplies these
locators. This remains a topological existence theorem only.

The manifold and spin hypotheses are unchanged from L050; the trivial
coefficient line is permitted. L049's full-tensor integrality, not a
rational NS/T splitting, is the input for the new u. The criterion has
linear and quadratic terms in u; their changed substitution and
mod-12 evaluation are deferred. No former congruence is imposed as a
hypothesis. Reuse L050's full-lattice Steenrod argument after verifying
that its domain includes the changed class.

### Real-metric stability and connection inputs

Use Perego, *Kobayashi-Hitchin correspondence for twisted vector
bundles*, [arXiv:1910.01867v1, Corollary 6.42, p. 118](https://arxiv.org/pdf/1910.01867v1#page=118).
For a slope-semistable rank-r holomorphic bundle on a compact Kähler
n-fold, its inequality is

\[
\int_X((r-1)c_1^2-2r c_2)\,\sigma_g^{n-2}\leq0.
\]

[Definition 4.7, p. 59](https://arxiv.org/pdf/1910.01867v1#page=59)
uses the degree against the real metric form. Trivial twisting and
zero auxiliary B-field give ordinary Chern classes. No rationality
of the Kähler class or prescribed Chern sign is required.
[Theorem 5.1, p. 66](https://arxiv.org/pdf/1910.01867v1#page=66)
also gives the polystability/Hermite--Einstein equivalence at that
metric. The class-character conversion and mixed contraction must be
performed for the new data; the old sum cutoff is not an input.

Use Verbitsky, *Hyperholomorphic connections on coherent sheaves and
stability*, [arXiv:math/0107182v10, Theorem 3.9, pp. 13--14](https://arxiv.org/pdf/math/0107182v10#page=13).
For a stable holomorphic bundle on a compact hyperkähler manifold at
an induced complex structure, a compatible hyperholomorphic connection
exists exactly when c_1,c_2 are SU(2)-invariant. Definition 2.1
(p. 9) allows the product metric: it does not require irreducibility.
Definition 3.2 (p. 11) identifies hyperholomorphicity with invariant
curvature. [Proposition 3.7 and Lemma 3.8, p. 13](https://arxiv.org/pdf/math/0107182v10#page=13)
give zero Kähler contraction of invariant two-forms.
These are connection statements conditional on an actual bundle.

For applicability, compare the new operator -D with L044's rotation
representation and L051's split-product argument. The criterion asks
for invariance, not a positive eigenvalue. The product line-sum branch
must still be excluded before invoking the stable theorem; total-class
invariance must not be assigned to arbitrary summands. Factor
polystability must still be obtained by the quaternionic-equivariant
curvature pullback of L051, not by assuming restriction stability.
This sign comparison authorizes checking that passage in research;
no connection or factor bundle is constructed here.

### Adequate source coverage reused

Reuse the Huybrechts author-hosted prepublication *Lectures on K3
Surfaces* statements already inspected in the
[factor assessment](2026-10-04-corrected-rank-two-factor-restrictions.md)
and [variable-region assessment](2026-10-04-nonsymmetric-factor-polystability-region.md):
[Chapter 1 (2.5)--(2.6), Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
for surface/line Riemann--Roch and Serre duality;
[Chapter 9 Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175)
for real-class slope and dual stability; and
[Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
for Hermite--Einstein/polystability. The metric, surface category and
rank have not changed. The attempted fresh web open failed; these
passages were not freshly retrieved today. Prior adequate coverage
is reused, with Perego's freshly read theorem also covering the
correspondence. There is no essential source blocker for this test.

Reuse L048--L049's assessed Stacks inputs:
[rank truncation, Tag 02TZ](https://stacks.math.columbia.edu/tag/02TZ),
[character polynomials, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
[Todd classes, Tag 02UN](https://stacks.math.columbia.edu/tag/02UN), and
[smooth proper HRR, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO).
The smooth proper variety and locally free category are unchanged.
Higher characters must be forced anew from rank two and c_1=0,
rather than imported from L045's fixed virtual K-class. Track the
linear and squared mixed contributions separately in all indices.
The exact zero-slope lattice of L052 depends on h, which is unchanged;
reuse its proof as an input, retaining both stable and split factor
alternatives, including their boundary and zero cases.

### Discovery, duplicates and bounded continuation

Queries performed today:

- `"rank two" "K3" "product" hyperholomorphic second Chern negative`
- `Cadek Crabb Vanzura Obstruction theory 8 manifolds Corollary 8.4 quaternionic line`
- `Perego 1910.01867 Corollary 6.42 Bogomolov`
- `Verbitsky hyperholomorphic Theorem 3.9 invariant Chern classes stable product`

Search discovery returned the inspected primary criteria, Verbitsky's
1993/1997 papers, a rank-two Fourier--Mukai paper and general K3
existence leads. Only the texts and passages specified above were
read today. The additional Fourier--Mukai/existence hits are unread
leads for other targets, not evidence of a matching region theorem
or of nonexistence. Reuse the earlier topological assessment's
comparison: the highly connected alternative does not apply to this
K3 product. No further existence search is needed for the saved
necessary-condition target.

The scoped duplicate search found only the proposal, its history and
the older negative-presentation warning. L050--L052 have positive
mixed-tensor hypotheses; their computed region is not the new result.
Attempt 049 and audited L070 remain stops for their positive tensor.
The new review does not flip that curvature proof into an existence
theorem. The presentation warning remains relevant if a later turn
selects an actual resolution, but no presentation is hypothesized now.

One bounded mathematical attempt is approved: evaluate all three
necessary filters over the full integer domain, supply their exact
intersection with justified stable/split cases, and compare achieved
conditions with actual holomorphic realization. Continue only on an
explicit non-exclusion set or informative new incompatibility; an
empty set stops this input. Passing these tests proves neither F's
existence nor transverse transport. No calculation, new lemma or
numerical survival verdict was performed in this literature turn.

## Mathlib

Full changed specialization: **not checked**. No matching declaration
or absence from inspected Mathlib sources is asserted. The named
primary theorems and already canonical full-lattice and exact-metric
calculations are the approved inputs for the next attempt.
