# Retained Legendre descent: proposed conditional odd-torsion test

TARGET: For unchanged E_0,F and a specified Legendre descent over native F_tpd, derive the exact twist-character test for its full 15-torsion to be F-rational, retaining unresolved field identification and minimal generation.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed specified-model comparison in drafts/literature/2026-10-17-retained-global-field-equality-model-comparison.md and detailed search/unused-lead record in drafts/2026-10-17-retained-global-model-source-comparison.md; L045,L048 and ATTEMPTS/028 do not perform this Legendre twist-character application. No originality claim is made.
SOURCE_EVIDENCE: IUT IV Proposition 1.8(ii)-(iv),(vi) pp.18-21, Theorem 1.10 p.22 and Corollary 2.2 pp.41-42, https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf; Sutherland Lecture 21 (6 May 2024) section 21.2 p.2, https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf; Gonzalez-Jimenez/Lozano-Robledo/York arXiv:2408.04159v1 Lemma 3.4 proof p.12 displayed full-torsion twist formula only, https://arxiv.org/pdf/2408.04159v1; Yvon arXiv:2407.14370v1 Introduction p.2 full-coordinate kernel convention, https://arxiv.org/pdf/2407.14370v1; Sutherland Lecture 20 (1 May 2024) section 20.1 pp.1-2, https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf. These relevant statements and proof cases were inspected in step272; source-version byte identity remains unverified.
COMPARISON: Known twist classification and representation formula cover a conditional full-point torsion test over a common number field. The difference is checking their hypotheses and restricting the same geometric comparison to the retained G_F, using L045's full torsion. No new general division-field theorem is needed; IUT IV's two-model rationality condition may be applied only after the missing model's rationality is checked.
GAP: The retained application has not been performed. Native F_mod/T identification, the actual Legendre twist character, its value on G_F and equality of the minimal generated global fields remain unproved; no automatic passing verdict is anticipated.
REASON: This independently testable conditional obligation precedes exact field generation and uses ready source coverage without restarting persistent moduli-source retrieval or changing the curve/field. It can identify precisely what torsion rationality does and does not prove.
SCOPE: Exactly TARGET, conditional on the native T=F_tpd subset F setup and a specified E_L/T geometrically origin-preserving isomorphic to E_0; no F_mod=Q, T=Q(E_0[2]), field enlargement, curve reselection, sufficient initial data, global numerical application or source-marked transport.

This newly written ready continuation requires separate approval next
turn. Step272 performs only the source review, not this specialization.

Essential inputs are L045,L048 and foundations/05 step272. Preserve
L060 and foundations/05 step271 only for the conditional native setup,
not as proofs of a moduli identification. Keep the same E_0/Q,
F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), Omega, embedding, u,w,
H,N,M>=max(M_tors,31), full-coordinate torsion and changed q_0
with v_3(q_0)=30. A native Legendre descent E_L/T is a conditional
comparison object, not a replacement for E_0 or a newly chosen F.

The main gap remains finite B>=A. The intermediate target isolates
odd-torsion compatibility, which could support one later check of
the global field equality. Verify the common-field and
nonexceptional-j hypotheses before using quadratic-twist classification;
use the actual geometric pointed isomorphism to transport bases.
Apply the cited formula at n=15 and inspect the full kernel on G_F,
not only images or x-coordinates. Explain explicitly what a conditional
test leaves undecided when the actual twist character is not known.
Do not assume E_L[15] is rational to obtain the isomorphism used to
justify that same rationality. No reproof of the classification or
Galois correspondence is needed; only the retained substitution is
authorized after approval.

Continue to a later exact-generation comparison only if the test
passes for the specified model, with its hypotheses justified. A
nontrivial actual character gives a compatibility stop for that model;
an unidentified character leaves the test conditional. Neither case
refutes IUT or authorizes changing F. Equality over T(sqrt(-1)),
independent initial data, source-marked all-image factorization,
essentiality and original finite B>=A remain separate obligations.

Do not import arXiv:2408.04159v1 Lemma 3.4(2)'s stronger field-equality
clause or Hamakiotes arXiv:2408.16164v1 Lemma 3.5(2); the source notes
explain the unverified kernel step. The inspected coordinate formula
and full-coordinate kernel convention suffice for the proposed test.
Full matching and supporting Mathlib coverage are not checked.
