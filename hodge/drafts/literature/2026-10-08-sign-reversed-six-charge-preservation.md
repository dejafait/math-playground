# Sign-reversed six-charge preservation — completed scope review

TARGET: Test whether every admitted sign-reversed L071 input with a=-10 has an actual rank-two first higher direct image that is slope-polystable at the unchanged h.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused 2026-10-05-six-charge-direct-image-polystability.md; scoped comparison of L056, L071, sign-reversed assessments, ATTEMPTS/050 and histories 155/158 found the changed-sign preservation target still unwritten. No repeated broad discovery search was needed.
SOURCE_EVIDENCE: Freshly inspected Bartocci--Bruzzo--Hernandez Ruiperez, A hyperkahler Fourier transform, Differential Geometry and its Applications 8 (1998), 239--249, Sections 3.1--3.3, Definition 2, Lemmas 1--2 and Theorem 3, pp. 243--246; Bartocci--Jardim, arXiv:math/0312045v1, Theorem 2 and Theorem-Definition 3 with following remark, pp. 4--5. Base-change and real-metric coverage reused below.
COMPARISON: Published preservation covers a hermitian quaternionic-instanton product kernel with flat source line under all-fibre IT; no mixed-character positivity hypothesis occurs. L071 provides the changed-sign connection/factor framework, while L056's positive-sign statement cannot itself be applied to the new F.
GAP: Write the changed-sign applicability argument for every admitted b: all-fibre concentration, actual rank-two local freeness, holomorphic identification and unchanged-h polystability. No new preservation theorem or six-charge character calculation is needed or approved.
REASON: The pending review changed the kernel's mixed sign; inspecting the precise theorem and proof resolves coverage rather than deriving its new specialization in this literature turn.
SCOPE: L071's identical marked product and common metric, full integral -tau_D, locally free rank-two product-polystable F, c_1=0, a=-10 and every integer b admitted by L071; unrestricted initial higher characters. Only concentration, actual local freeness and slope-zero polystability of R^1 p_2*F are covered.
LITERATURE_REASON: Essential changed-sign applicability was outside the prior positive-sign scope and explicitly REVIEW_REQUIRED; reuse the ready transform coverage and inspect only its load-bearing hypotheses and identification cases.

## Gap, target and discriminating test

The main gap remains universal primitive rational Hodge-class algebraicity.
The immediate intermediate target is the saved preservation assertion,
which could support a later necessary surface-character test for the
negative-mixed six-charge slice. Continue if the actual conditional
hermitian kernel and flat source line satisfy the cited theorem, with
all-fibre IT and actual holomorphic identification justified. Abandon
this bridge upon a failed hypothesis; do not replace F by a virtual
class or add transform stability, equivalence or other-projection
stability. F existence, gluing, transport and universal algebraicity
remain independent unresolved steps.

L056 already proves the positive-sign analogue, so the planned work is
a specialization of known preservation, not a new transform result.
L071's conclusions and its stable-product/factor proof were inspected,
including the separate audit's invariant-curvature passage. They retain
the same metric and full tensor with reversed sign. L072 and its
ATTEMPTS/050 stop concern the five-charge line identity only; they are
not preservation inputs. L070's positive-tensor exclusion and the older
flat/charge-seven stops do not ban this changed-sign test. No
cross-notebook input is used.

## Primary-source inspection

The published [Bartocci--Bruzzo--Hernandez Ruiperez scan](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf)
was retrieved and its pp. 243--246 read, including both lemmas' proofs.
Definition 2 imposes even-cohomology vanishing at every parameter for
odd IT. Section 3.1 fixes compatible complex-structure spheres and the
product metric. Theorem 3 accepts a hermitian quaternionic-instanton
kernel and a source instanton satisfying IT on compact X. Lemma 1
transfers IT to the twistor projection; Lemma 2 identifies the natural
restriction morphism with a holomorphic hermitian isomorphism. The
following descent argument identifies the compatible connection with
the actual higher direct images. Neither a positive mixed Chern
operator nor a universal-moduli kernel is assumed. Section 4.1's
integral-metric examples impose no additional hypothesis on Theorem 3.
Import the theorem; no twistor reproof is justified here.

[Bartocci--Jardim, arXiv:math/0312045v1](https://arxiv.org/pdf/math/0312045v1),
pp. 4--5, corroborates the hermitian connection, actual holomorphic
identification and odd-index sign. Its following remark permits
reducible transforms and denies general invertibility. The printed
Theorem-Definition 3 target M conflicts with its projection to N and
Theorem 2; use the published theorem, not that typo, as the input.

## Coverage reused and exact research obligations

Reuse [the six-charge source assessment](2026-10-05-six-charge-direct-image-polystability.md)
for Verbitsky, arXiv:math/0107182v10, Theorem 3.9, Proposition 3.7 and
Lemma 3.8, pp. 12--14; Huybrechts, Lectures on K3 Surfaces,
author-hosted draft, Chapter 9 Section 3.1 and Theorem 4.9,
pp. 175--176 and 182; and Stacks Lemmas 36.30.1 (0A1H) and
36.31.3 (0BDH). These inputs address compatible invariant connections,
real-class Hermite--Einstein polystability, proper perfect base change
and single-degree local freeness. Their hypotheses have not changed.
The earlier assessment links their primary sources; no claim of a
fresh inspection of those unchanged sources is made.

The separate research turn must:

1. Use L071, rather than importing L056's sign-specific hypotheses,
   to check the conditional product connection and every p_2-fibre.
   Apply its charge-six stable case and its cited surface-cohomology
   argument; write all even vanishings and the remaining dimension
   explicitly on every fibre, retaining all admitted integers b.
2. Apply proper perfect base change and the single-degree locus
   criterion to the actual smooth projective p_2 and locally free F.
   Check the closed-point-to-all-points passage and GAGA identification
   to obtain actual G=R^1 p_2*F, rather than only its alternating index.
3. Set X=Y=S, P=F with that compatible unitary connection and source
   E=O_S with its flat connection. Check simultaneous product rotations,
   compactness and odd IT, then import Theorem 3 for the actual G.
   Retain the negative alternating class separately from the positive
   holomorphic bundle. Deduce zero contraction and polystability at
   the identical h using the reused surface/real-metric inputs.

These are licensed applicability obligations, not a proof of the saved
assertion in this turn. Sign reversal does not enlarge the theorem's
scope: its connection hypotheses, not a numerical sign convention,
control the comparison. No preservation conclusion, transformed
character or new lemma has been derived. No stability of G, equivalence,
kernel existence, new cycle, transverse surface or transport is covered.
Mathlib coverage of the full preservation theorem and specialization
is not checked; no absence claim is made. This review completes source
coverage, classified NOVELTY_UNCHECKED as literature; the subsequent
specialization should be classified REPRODUCTION.
