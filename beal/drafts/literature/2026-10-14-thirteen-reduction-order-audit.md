# Exact thirteen-adic reduction-order audit — completed coverage review

TARGET: Critically audit L068's complete reduction count and the failure of Bruin Lemma 4.2's prime-to-thirteen order hypothesis.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready counting and elliptic-Chabauty assessments; targeted L068, history/207–209 and ATTEMPTS/029–031 for duplicate audits and failures; reopened the two primary PDFs at the exact theorem/proof passages, without repeating broad discovery searches.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), IV Proposition 9.9 p.155 and Theorem 9.10/Remark 9.11(a) p.156 (PDF pages 160–161); Bruin, J. reine angew. Math. 562 (2003), Lemma 4.2 and complete proof, printed p.44 (PDF page 19), correcting the earlier p.45 locator.
COMPARISON: The imported extension-count formula and Bruin's exact implication cover the entire proposed audit; only independent finite arithmetic and existing model/field applicability checks remain, with no new Frobenius or saturation theorem needed.
GAP: L068's count and certificate have not been independently verified by this literature step; rank, finite-index generators, coset zero tests, other classes and global power lifting remain missing.
REASON: Ready source coverage extends to a bounded reproduction audit; the primary reread resolves the citation locator and fixes the exact index implication, rather than introducing previously uncovered mathematics.
SCOPE: Independent audit of L068's full base-field enumeration, origin, smoothness, degree-twelve residue-field specialization, recurrence/matrix arithmetic and limited failed-premise conclusion; REPRODUCTION only.
COVERED_TARGET: Critically audit L068's complete reduction count and the failure of Bruin Lemma 4.2's prime-to-thirteen order hypothesis.
LITERATURE_REASON: The newly proposed audit was REVIEW_REQUIRED; this separate approval checks its exact scope and resolves a primary-source page discrepancy, reusing unchanged adequate coverage.

## Relevance and source reuse

The main gap is positive primitive integer emptiness, focused here on
the 54a1 branch of ordered (3,4,11). The intermediate target is an
independent check of the recorded reduction-order stop. Its downstream
use is reliable routing away from a failed sufficient index shortcut.
Continue if the complete evidence and hypotheses confirm the stop;
repair a specific discrepancy if they do not. Neither result would
decide the branch or supply the missing global point computation.

The ready assessments
[counting](2026-10-14-thirteen-reduction-order-index-test.md) and
[Chabauty scope](2026-10-14-fixed-class-elliptic-chabauty-scope.md)
remain adequate. No independent L068 audit was found in the targeted
history passages; history/209 explicitly leaves it pending.
ATTEMPTS/031 records this order shortcut's stop; ATTEMPTS/029–030
concern different class-removal mechanisms and remain in force within
their own scope. No new mathematical calculation was made here.

## Primary theorem coverage

[Milne, second edition (2021), IV, pp.155–156](https://www.jmilne.org/math/Books/EC2.pdf#page=160)
was reopened at Proposition 9.9, its proof, Theorem 9.10, its proof,
and Remark 9.11(a). For an elliptic curve over F_p, the remark gives
N_m=1+p^m-alpha^m-beta^m, with alpha+beta=p+1-N_1 and alpha beta=p.
N_1 counts projective points. No ordinarity or group-structure
hypothesis occurs. The proof uses divisor counts and the projective
zeta identity. Import this result; no reproof is warranted. The audit
must verify L068's particular arithmetic and full residue degree,
rather than infer them from the theorem or a certificate preview.

[Bruin, published author copy, Lemma 4.2, p.44](https://www.cecm.sfu.ca/~nbruin/bruin_crelle.pdf#page=19)
and its entire proof were reopened. Hypotheses: E over a number field
L; rational p>2 unramified in O_L; good reduction at every prime p_i
above p; each reduction-group order prime to p; points B_j reducing
to the origin at all p_i. If their subgroup has finite index divisible
by p in E(L), the lemma yields a nonzero mod-p relation among their
formal parameters modulo every p_i squared. Its proof uses the
prime-to-p order to force a point G with pG in the reduction kernel
to lie in that kernel. This identifies exactly the premise tested
by L068, not an equivalence between reduction-order and index
divisibility. The page-45 citation in L068 and earlier notes is a
locator error: repair the canonical lemma during the research audit.
No lemma file is edited in this literature turn.

## Applicability and audit boundary

Targeted canonical passages confirm that L033 displays the same E1
equation used in L068; L064 identifies the entire completion as one
unramified degree-twelve field; L067's whole-model argument supplies
unit discriminant and good reduction. These are existing inputs, not
independently reproved here. Use L033, L064, L067 and L068 with its
complete `scripts/thirteen-reduction-order/order-certificate.json`.
Inspect all 169 residues, the origin, smoothness evidence and every
load-bearing power sum/matrix value in the research audit, and use
independent arithmetic rather than importing the generating code.

Confirmation parks only Bruin's stated shortcut at thirteen. An actual
index, alternate saturation method, other prime or branch exclusion
is outside this approval. No rank, GRH, Selmer/point equality or common
global primitive power triple is assumed. Full matching and supporting
Mathlib coverage: not checked. No cross-notebook input is used.
