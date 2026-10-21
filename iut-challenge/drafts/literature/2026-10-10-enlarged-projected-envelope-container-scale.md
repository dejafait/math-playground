# Enlarged projected envelope versus scaled integral container — coverage approved

TARGET: Determine the least integer k such that every finite-word Gamma image of q(T) lies in 3^(-k)q(C), for each admitted presentation, and test attainment of failure at the preceding scale.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three focused external queries for p-adic orbit lattices, quotient singular values and elementary-divisor containment; scoped comparison of L034/L036, L026's finite-sum attainment passage, histories 097/103/105/107 and ATTEMPTS/020,022–024 found no completed matching sharp-container test. Searches found general tools, not an inspected exact-target theorem; no novelty inference.
SOURCE_EVIDENCE: Reused inspected Voight (2021), Theorem 9.3.9 and the L036 audit assessment; freshly inspected Bürgisser–Kulkarni–Lerario (2026), section 2.2 pp. 13–14, Definition 3.1.3 and Lemmas 3.1.4/3.1.5 pp. 22–23, Propositions 4.1.1/4.1.2 and complete relevant proofs pp. 35–36, https://d-nb.info/1395945926/34. Source versions and qualifications below.
COMPARISON: Known same-space relative factors, quotient-only interlacing and integral-map criteria cover projected embedded containment over Q_3/Z_3. Audited L036 supplies the finite-sum span; L026 supplies a local finite-sum attainment precedent. None states the requested exact enlarged-field threshold, which remains a separate specialization.
GAP: Apply the full L034 factors to the actual common quotient, retain the extremum needed for reverse containment, compare L036's embedded span to the scaled container, and return noncontainment to an actual finite-word image. No scale value or witness is established here.
REASON: Essential theorem coverage is adequate for one separate bounded known-method proof attempt with unchanged field, actual line and action; no new general theorem or normal-form reproof is needed.
LITERATURE_REASON: The supplied gate requires separate assessment of the changed sharp-container target; the previous span-audit scope explicitly deferred this comparison and attainment.
SCOPE: Exactly TARGET with audited L031/L033–L036, Q_3/Z_3 lattice containment and existential finite-word attainment for each admitted presentation. No explicit word construction, chosen line coordinates, field valuation on the quotient, extra group action or IUT numerical prescription.

## Gap, relevance and stopping test

The main gap is the original finite B>=A inference. The intermediate target
is the least integer dilation of the projected integral container enclosing
the specified auxiliary envelope orbit, including actual failure at the
preceding integer scale. Its plausible downstream use is to quantify
L035's qualitative container obstruction for the independently specified
envelope, rather than transfer a singleton field radius.

Continue if the existing complete factors and ordinary finite-sum span
settle the sharp embedded comparison uniformly over admitted presentations.
If the needed quotient extremum is not forced without hidden line
coordinates, record the exact remaining line condition and abandon the
uniform shortcut. An existential word is sufficient for the saved target;
constructing a particular word would require a changed assessment.

Use L=Q_3(zeta_20,pi), pi^27=3, J=log(O_L^times), V=ker(Tr),
M=J intersect V, T=(pi J/6) intersect V, C=O_L intersect V,
W=Q_3 y_1, q:V->V/W and P=q(M). Essential inputs are audited L031
(genuine complete logarithm and tails), L033 (actual primitive line and
exact finite-word reference subgroup), L034 (full relative factors),
L035 (same-space projected lattices) and L036 (ordinary span P/81).
No new lemma or mathematical certificate was produced or verified here.

## Precise imported sources and applicability

Reuse John Voight, *Quaternion Algebras*, GTM 288 (2021), chapter 9,
section 9.3, **Theorem 9.3.9**
([primary chapter](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_9)),
as inspected in `drafts/2026-10-08-enlarged-projected-container-source-review.md`.
It supplies simultaneous relative factors for full lattices over a
Dedekind domain. Z_3 is the DVR specialization; nesting is unnecessary.
Its reference O'Meara 81:11 remains unread and is not a separate premise.

Peter Bürgisser, Avinash Kulkarni and Antonio Lerario,
*Nonarchimedean integral geometry*, Selecta Mathematica **32:10 (2026)**,
version of record published **5 January 2026**
([publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)), was retrieved at the
specific passages above. Definition 3.1.3 identifies integral maps by
nonnegative Smith exponents. Lemma 3.1.4 gives intersection and quotient
lattices; its proof is left to the reader. Lemma 3.1.5 proves complements
by Smith form. Proposition 4.1.2 gives target-only interlacing. Its proof
uses restriction minimax and duality; both minimax cases were read.
The minimax self-reference should be 4.1.1; Corollary 4.1.3 is not used.

Here the scalar field is Q_3, the ring Z_3, and both projected lattices
are full in the same quotient space. Apply the source to the identity
with domain C and target M, quotienting only the target by W. The
projected image is q(C), not an arbitrarily chosen complement. Its
relative factors can subsequently be used for either containment
direction; that numerical specialization is deferred.

The span identity is imported from audited L036, without rerunning
Nakayama or computing a new logarithm basis. L026's section “Return
from finite sums to an actual orbit point” explicitly treats containment
in a Z_3-module as well as valuation attainment. That elementary
finite-sum reasoning is the approved local method for the saved
existential attainment obligation. No orbit-set equality, closure of
Gamma, measure argument or coordinate witness is licensed. A later
proof must retain actual T-point lifts of q(T) and finite words.

## Duplicate, failure and discovery checks

Read the complete L036 argument and the relevant L034 hypotheses,
factors and projection proof, plus L026's complete attainment passage.
Histories 097/103 concern homothety and qualitative escape; 105/107
concern the span and its audit. The prior span assessment expressly
leaves sharp-container comparison and orbit attainment for later work.
These scoped checks found no duplicate completed proof of this target.
No full certificate was loaded because no new certificate claim is made.

External queries were: `"p-adic" "orbit" "lattice" "irreducible"
containment`; `"Nonarchimedean integral geometry" "quotient" "singular
values"`; `"lattices" "elementary divisors" "containment" discrete
valuation`. The primary BKL publication was relevant and inspected.
Other hits concerned representation zeta functions, coadjoint orbits,
quadratic forms, exercise sheets or unrelated lattice problems; they
were not theorem-level inputs. No matching stronger theorem deciding
the exact field/input/action was inspected. Search failure does not
establish originality. Thompson (1979) remains an unread historical
lead in the prior source review; it is unnecessary given the inspected
quotient-only theorem.

Preserve ATTEMPTS/020 (unjustified prescribed reciprocal coordinates),
022 (unchanged selected-factor packet exclusion), 023 (false naive
O_U scalar transport), and 024 (whole-kernel reducibility). This target
uses the genuine enlarged J and the actual quotient subgroup; it neither
reopens nor erases those failed mechanisms. It does not assert that
every rational line is realized by an admitted presentation.

## Decision and limitations

SPECIALIZE approves a separate RESEARCH/REPRODUCTION proof attempt for
exactly TARGET. This literature turn supplies source comparison, not a
sharp-scale theorem or mathematical advance beyond checked sources.
Outcome EXPLORATION records a new bounded discovery/comparison for the
changed target, with no mathematical exploration budget spent.

Fixed-line control, actual/native input and action compatibility,
packet/global realization, pilot transport, essentiality and original
finite B>=A remain unresolved. No chosen reciprocal coordinates,
O_U-linearity, extra action, quotient field valuation or original
numerical prescription is assumed. Matching and supporting Mathlib
coverage for this target is **not checked**, not claimed absent.
