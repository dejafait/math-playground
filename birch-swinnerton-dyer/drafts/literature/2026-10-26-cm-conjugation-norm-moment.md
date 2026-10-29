# CM conjugation and the complete norm moment — source comparison

TARGET: Determine the complex-conjugation transformation of L123's complete norm moment from CM-point reciprocity, retaining every level correspondence, and test its implication for R.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: On 2026-10-26 searched Shimura CM points complex conjugation Atkin-Lehner reciprocity full level; Plectic Heegner classes conjugation; Nekovar Level Raising and Anticyclotomic PDF; and Blasius Guerberoff complex conjugation Shimura varieties. Checked the named local assessments and ATTEMPTS/003/004/030/058/059; no inspected matching complete-moment cancellation theorem was found, and no novelty is inferred.
SOURCE_EVIDENCE: Blasius-Guerberoff, Algebra & Number Theory 11 (2017), 2289-2322, https://msp.org/ant/2017/11-10/ant-v11-n10-p02-s.pdf, Sections 2.1-2.2, Lemmas 2.2.1/2.2.4 with proofs and the real-reflex-field paragraph on p.2297; Nekovar, Canad. J. Math. 64 (2012), 588-668, doi:10.4153/CJM-2011-077-6, Sections 1.3.2/1.3.4 and 1.8.1-1.8.2, pp.599-600/615; Fornea arXiv:2603.28327v2 (13 April 2026), (5)/(14)/(16)/(22)/(63)/(64)/(68), Corollary 3.9, Proposition 4.18 with proof and Corollary 4.24 with proof; prior construction coverage reused.
COMPARISON: The canonical-model outer action is available at finite level, independently of torus reciprocity; it changes the Shimura-datum coordinate and retains the finite adelic coordinate. These sources do not evaluate L123's weighted complete moment or supply an eigenvalue for its retained symmetrization.
GAP: Specialize the sourced action to the actual CM orientation, rational normalizer and complete level tower, retaining any changed level, Hecke correspondence and logarithmic constant, then compare the resulting integrated class with R; this specialization has not been performed.
REASON: The previously missing outer-action source is now inspected, so one bounded specialization attempt is justified; proving a new full-level cancellation theorem or assuming an Atkin-Lehner sign is not authorized by this assessment.
LITERATURE_REASON: At turn start the essential CM outer-conjugation input was unread and outside the prior construction/naturality review; this comparison supplies its primary statement and proof case without undertaking the dependent specialization.
SCOPE: L123's F=Q, inert split-multiplicative p>=5, w=infinity, conductor-one trivial-character setting, with all residual, conductor, incoherence and CM-embedding hypotheses retained.

## Review boundary

Originally written after step 515's completed conceptual audit as
REVIEW_REQUIRED. Step 516 completes its essential source comparison;
the exact target is unchanged. SPECIALIZE approves only the remaining
application described below, subject to the supervisor's next-turn gate.
No transformed moment or vanishing theorem is derived in this
literature-only turn. Reuse the existing construction and audit.

Essential local input: L123, including its complete J, the projected
class B over L_1, b=desc(B), and R=loc_p(b+cb) over K. Its
equation (7) specifies actual conjugate points, not a reciprocity
identity. ATTEMPTS/059 remains the scalar-sign/constant-mass stop;
ATTEMPTS/058 and the earlier rationality stops remain independent.
L005 and L122 are downstream motivation, not assumptions.

A useful reviewed theorem must handle the source's CM orientation,
full level, Abel–Jacobi normalization and transition maps. It must
distinguish an outer conjugation lift from an element of Gal(K^ab/K),
and must permit only operations defined on the completed integral.
Neither coefficientwise pr_A nor an arbitrary interchange of tensor
factors is admissible. No global oddness of B is presumed: it would
be a stronger condition than the required vanishing of its localized
symmetrization.

The discriminating test remains an explicit transformed complete moment
whose localization can be compared with R, or a precise obstruction
showing that the available relation leaves R unconstrained. A formula
merely rewriting C mu as the same unevaluated conjugate coefficients
does not count. Retain all constant terms until their source-supported
annihilation is justified. If essential coverage remains inaccessible,
park this dependent mechanism and select a materially different target;
do not keep repeating source recovery.

There are two mathematical exploration turns used, with no reset from
the audit. For the intended rank-two application, analytic order two
for A and a nonzero central twist value are still additional hypotheses;
general existence of admissible K,p, nonvanishing, rational Kummer
membership, the multiplicative-prime rank criterion and general BSD
remain unresolved. Mathlib coverage: not checked.

## Inspected primary inputs and qualifications

Blasius--Guerberoff, *Complex conjugation and Shimura varieties*,
[published primary PDF](https://msp.org/ant/2017/11-10/ant-v11-n10-p02-s.pdf),
doi:10.2140/ant.2017.11.2289, pp.2293-2297: Section 2.1 assumes a
Shimura datum with connected center splitting over a CM field and
sufficiently small compact open level. Lemma 2.2.1 trivializes the
conjugate group using the rational element sp(c); Remark 2.2.3 makes
the finite-adelic identification the identity. Lemma 2.2.4 proves
cx=x composed with conjugation on the Deligne torus, by comparing both
cocharacters on S(C). The following paragraph gives
phi([h,g])=[bar(h),g], where bar(h)=h composed with that conjugation.
For real reflex field it is the canonical-model involution at the
same level. This is an action on the Shimura datum, not a formula
conjugating entries of g. The real normalizer appearing on p.2297
must not be silently treated as a chosen rational normalizer.

For the present application the curve is defined over Q and the group
is quaternionic units modulo center. Its connected center is trivial,
so the center hypothesis adds no CM-field restriction. The local
notation K denotes the imaginary quadratic field; it is **not** the
reflex field E in Blasius--Guerberoff. The sufficiently-small-level
qualification must be checked for the levels used, or handled by
refining and descending through the finite level maps. Do not simply
assert neatness of the source's K_m. Coordinate identification with
Fornea's tau_infinity is an explicit applicability obligation of the
next attempt, not a new identity proved here.

Nekovar, *Level Raising and Anticyclotomic Selmer Groups for Hilbert
Modular Forms of Weight Two*,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2A11114CBB9FC75C2DBF56F766BFE7BF/S0008414X00009196a.pdf/level_raising_and_anticyclotomic_selmer_groups_for_hilbert_modular_forms_of_weight_two.pdf),
Section 1.8.2 (p.615), retains a chosen CM embedding and one of its
two complex fixed points. Its reciprocity law multiplies the finite
coordinate on the left by the embedded idele, with geometric-Frobenius
normalization. Sections 1.3.2/1.3.4 describe the double quotient and
the intersected levels for right-translation correspondences.
Section 1.8.1's nonsplitting and auxiliary-prime assumptions belong to
that paper's setup; its auxiliary ramified-prime specialization is
not imported into our w=infinity construction. Fornea (14) is the
direct reciprocity input here. Nekovar's statement supplies no outer
action by itself.

Fornea, [version 2 primary HTML](https://arxiv.org/html/2603.28327v2),
(5) has trivial action twist at infinity. Equations (14)/(64) concern
reciprocity over the CM field. Section 2.2 retains deep K_m levels and
diamonds; (22) fixes the Hecke-normalized maps to Jacobians. Corollary
3.9 gives the actual CM cells. Proposition 4.18's proof moves the
reduction vertex and compensating compact element before using Lemma
4.7 and Theorem 4.13 to remove eligible constants. Corollary 4.24
retains the complete sum (68) and proves its character descent. These
are sufficient construction inputs for the proposed specialization;
none asserts that its outer-conjugate weighted sum has a minus sign.

The source construction and its delicate projection domain are reused
from the retained-plus assessment and L123's step-515 audit. There is
no reason to reprove that construction. Only its explicitly missing
specialization is in scope. Mathlib coverage for this full-level CM
comparison has not been checked; this is not evidence of absence.

## Bounded application approved for a later research turn

Apply the cited outer action first to the genuine finite-level points
P_{t,xi,m}. Identify the CM orientation and justify a rational
normalizer, if used. Keep the resulting right coordinate and its
domain/codomain levels until the appropriate correspondence has been
identified. A formula at the shallow quotient alone is insufficient.
Then transport the **whole** CM sum and its norm kernel through the
level maps, completion, integration, Hecke localization, invariant
projection, descent and localization in L123's order. Any choice of
lift differing from its p-decomposition lift d needs the intervening
reciprocity action tracked; agreement after descent must be justified.

This permits a symbolic transformed integral or correspondence-valued
residual, not an unreviewed numerical implementation. Establishing that
an operator acts by a scalar on the relevant integrated specialization
is a required calculation, not an assumption licensed by a classical
Heegner-point sign formula. In particular, do not replace the entire
deep tower by its ordinary elliptic quotient before integration.

Continue only if this gives an explicit operator relation constraining
R, or isolates a specific unsupplied operator/moment needed to do so.
Stop the attempt if it merely reproduces C applied to the original
unevaluated cells, uses conjectural rationality, or has no control of
the level correspondence. If no advance or informative negative
results, this uses the third mathematical exploration turn and requires
mechanism reassessment; this literature turn does not reset the two
already used. Rational Kummer membership, nonvanishing, admissible
auxiliary choices and the multiplicative-prime rank criterion remain
independent gaps even after a successful local relation.

## Search and access record

The local duplicate/failure check used only L123, the named retained
assessments/audit and ATTEMPTS/003/004/030/058/059. Their stops concern
rationality, independence or scalar-only cancellation, not the newly
inspected canonical-model input. Classical CM-cycle conjugation and
Atkin-Lehner search hits are leads, not imported sign theorems for this
measure. No absence or novelty theorem follows from the search.

The author-hosted Nekovar Euler-system PDF returned HTTP 403. It is
an unread optional lead, not an essential blocker: Fornea's actually
cited Nek12 was identified correctly and retrieved from the publisher.
Milne's 1981 scanned PDF supplied no usable extracted theorem text;
its proof is not claimed read or imported. The later published
Blasius--Guerberoff Section 2.2 supplies the inspected outer-action
statement and the relevant proof case, so no further access-recovery
turn is required for this bounded target. No general BSD theorem or
complete norm-moment cancellation was found or claimed.
