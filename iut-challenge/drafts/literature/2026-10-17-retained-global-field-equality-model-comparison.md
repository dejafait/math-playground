# Retained global-field equality — completed source comparison

TARGET: Compare IUT IV Theorem 1.10's specified tripodal/Legendre descent and global field equality with the retained F=Q(zeta_60,E_0[30]), identifying the exact model and torsion-field compatibility obligations without changing E_0 or F.
CHECKED: 2026-10-17
DECISION: IMPORT
SEARCH_EVIDENCE: Read defining IUT IV references first; searched exact tripodal/Legendre/1.10 terminology, quadratic-twist division fields and full torsion kernels; compared L045,L048, foundations/05, the native-selected-model and parametric-section assessments and ATTEMPTS/028. Queries, inspected results and unused leads are recorded in drafts/2026-10-17-retained-global-model-source-comparison.md.
SOURCE_EVIDENCE: Direct author IUT IV https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf, retained April 2020 version label, Proposition 1.8(i)-(iv),(vi) pp.18-21 including relevant proofs, Theorem 1.10 p.22 and Corollary 2.2 pp.41-42 read; Sutherland Lecture 21 section 21.2 p.2 https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf; Gonzalez-Jimenez/Lozano-Robledo/York arXiv:2408.04159v1 Lemma 3.4 proof pp.12-13 https://arxiv.org/pdf/2408.04159v1 (only twist formula imported); Yvon arXiv:2407.14370v1 Introduction p.2 and Sutherland Lecture 20 section 20.1 pp.1-2 full-kernel conventions read. Author/reproduction byte identity remains unverified.
COMPARISON: The source defines F through F_tpd(sqrt(-1),E_L[15]) for a Legendre descent E_L/F_tpd; its F_mod/30 shorthand is not an arbitrary descent choice. Proposition 1.8(vi) allows a quadratic twist and (iv) requires rational odd torsion on both models before concluding an isomorphism. L045's full torsion on E_0 does not discharge those missing comparisons or minimal generation over F_tpd.
GAP: Source/model specification is now covered; actual odd-torsion compatibility of the indicated descent and exact embedded field generation remain unproved, as do native F_mod identification and independent global hypotheses. No retained-field equality is imported.
REASON: The source review replaces an unread-model obligation by precise cited hypotheses and a usable full-kernel/twist test; this is known-source applicability progress only. A bounded conditional specialization may follow after separate approval, without computing F_mod or changing E_0,F.

LITERATURE_REASON: The target changes from local field/root conventions to the essential unread tripodal/Legendre descent in IUT IV Theorem 1.10's global field equality.
SCOPE: Source comparison only. Preserve E_0,F,K_glob,Omega,u,w,H,N,q_0 and all prior stops; no field enlargement, curve reselection, new descent construction, root proof or marked-coordinate calculation is approved.

## Original bounded test (preserved)

The main gap is still original finite B>=A. The intermediate target is
an exact source-level comparison of the required global field with the
one actually constructed. It could identify a missing compatibility
hypothesis or a known import needed before using the global numerical
theorem. It does not imply such a theorem can presently be applied.

Start with the existing p.22 hypothesis and retrieve only the precise
model-defining references and essential comparison theorem hypotheses.
Distinguish any equality of torsion fields from an isomorphism of curves
or an equality of local completions. Retain native F_mod as specified;
this is not a repeat demand to compute F_mod through its previously
blocked source route. An explicit model-compatibility criterion is a
useful result even with that independent field identification unresolved.
If source access or model specification remains essential and blocked,
record that exact blocker without deriving a substitute equality.

Essential retained inputs for comparison are L045 and L048; L060 and
foundations/05 step271 supply only the conditional native setup. The
indicated native descent is not an input already constructed locally.
Sufficient initial Theta-data, other global hypotheses, source-marked
all-image factorization, essentiality and the original inequality remain
unresolved. ATTEMPTS/027,031,032 are not reopened. Full matching and
supporting Mathlib coverage are not checked.

## Completion — step 272

The source comparison is complete. The detailed inspected evidence and
unused stronger-result lead are in
`drafts/2026-10-17-retained-global-model-source-comparison.md`; canonical
citations and hypotheses are in foundations/05 step272. This is an
import of the source's model specification, not an application proving
the retained equality. The original bounded test above is preserved
as the question answered by this comparison.

The next conditional odd-torsion test has its own newly written
SPECIALIZE assessment,
`drafts/literature/2026-10-17-retained-legendre-odd-torsion-compatibility.md`.
It requires separate approval before mathematical invocation. No such
application, actual twist value, new theorem or field equality is
derived in this literature-only step.
