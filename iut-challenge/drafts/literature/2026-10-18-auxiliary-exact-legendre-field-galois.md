# Auxiliary exactly generated Legendre field — normality source scope approved

TARGET: Determine whether L079's exactly generated auxiliary field G=Q(t)(iota,E_L[15]) is Galois over F_mod=Q, using its conjugate ordered-root Legendre models.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step313 searched conjugate Legendre division fields, normality, quadratic twists and the S_3-equivariance obstruction; compared L073/L074/L077/L078/L079, foundations/05 step272, the auxiliary assessments, history/304–312 and ATTEMPTS/027,028,031,032,033. Queries, inspected theorems and unread leads are distinguished in drafts/2026-10-18-auxiliary-exact-legendre-normality-source-notes.md; no exact specialized normality theorem was identified and no novelty is inferred.
SOURCE_EVIDENCE: Antieau–Meier https://arxiv.org/pdf/1608.00851v3 (5 May 2020), Proposition 4.5/Corollary 4.6 pp.14–15 and corrected torsor action/Lemma 4.7 with full proof pp.15–16; Milne FT https://www.jmilne.org/math/CourseNotes/FT.pdf v5.10 (September 2022), Definitions 3.7/3.9, Theorem 3.10 pp.37–38, Theorem 3.17(c,d) and both proof directions pp.39–40, Remark 3.18(a,b) p.40; Gonzalez-Jimenez–Lozano-Robledo–York https://arxiv.org/pdf/2408.04159v1, Lemma 3.4 proof pp.12–13, representation formula and part (1) only; Sutherland https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf Lecture 20 (1 May 2024), section 20.1 pp.1–2. Reuse step272/L074's full-coordinate kernel convention and qualified IUT I 3.1(b); freshly read IUT IV https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf 1.10 p.22 and Corollary 2.2 prescription pp.41–42. Direct links and hypotheses are in the source notes.
COMPARISON: Known corrected permutation/torsor action, pointed-coordinate maps, quadratic-twist representation formula and Galois correspondence cover an exact conjugate-field/kernel test. L079 identifies T and L078 supplies G's generators and completions, but neither identifies its conjugate full-coordinate fields. Antieau–Meier 4.7 supplies the previously unread twist action, not a normality verdict; the stronger division-field equality in arXiv:2408.04159v1 Lemma 3.4(2) remains unimported.
GAP: Source coverage is ready for the unchanged target; invariance of this actual G under every Q-conjugation, or a verified changing conjugation, remains unproved. No extra mod-two, radical-independence or joint-image hypothesis is supplied. If the witness data are insufficient, the next attempt must isolate the exact missing information.
REASON: This separate literature turn completes the changed-scope theorem comparison and imports the corrected action. The next turn may specialize the known methods to the same embedded field; no new result or normality verdict was derived during approval.
SCOPE: The same L073/L074/L077/L078/L079 auxiliary witness, roots, cross-residue ordering, D,s,t,E_L,F_aux,F',G and fixed Q-bar embedding. No reselection, normal closure replacing G, extra radical adjunction or original numerical comparison.

LITERATURE_REASON: The saved REVIEW_REQUIRED target tests G/Q normality, outside the prior completion and native-coefficient-field assessments; the essential corrected torsor action in Antieau–Meier 4.7 and its comparison with full kernels had not yet been assessed for this scope.

## Completed separate review — step313

The [source notes](../2026-10-18-auxiliary-exact-legendre-normality-source-notes.md)
record the newly inspected corrected S_3-action and the reused Galois
and twist methods, source versions, hypotheses, proof cases, overlap,
failures and Mathlib qualifications. Import the general results;
the later application must check their exact number-field, ordering,
coordinate and full-torsion hypotheses. No general theorem needs
reproving. Lemma 3.4(2)'s stronger equality remains outside the import;
one known fixing element does not replace the full-kernel test.
IUT IV Corollary 2.2 has additional hypotheses not verified for this
witness and is not imported as an independent normality certificate.

The decision approves one bounded mathematical attempt on TARGET,
including an honest endpoint identifying missing witness information.
It does not derive or approve a yes/no answer. The six possible
ordered-root models must not be assumed to be six actual Q-conjugates.
Matching the source's right-action convention is part of the later
specialization. No lemma, mathematical script, DAG or PROOF change
was made in this literature turn.

## Proposed comparison and discriminating test

Main gap: original finite B>=A. The proposed intermediate question
tests one native initial-data prerequisite for the auxiliary packet.
A passing normality result would permit subsequent independent
checks on that same G. A proved failure would stop its use under
this prerequisite, not disprove IUT or negate the field prescription.

The now-approved attempt should reuse L079's moduli source record and the precise
general coordinate and torsion-kernel sources cited in L074 and
L077/L078. Apply the covered conjugate Legendre division-field
and corrected twist methods to the actual generators.
L073's global witness data and L074's six models are
relevant inputs, but their original F_aux conclusions cannot be
silently transferred to G. L075 is a possible fixed-field contrast,
not an existing normality verdict. The general Galois and corrected
twist comparisons are covered above; their application remains open.

The later mathematical test would require either invariance of
the actual full-coordinate G under every Q-conjugation or one
verified conjugation that changes G. An abstract field isomorphism,
normality of T alone, a degree bound, or equality of local
completions would not settle it. Do not assume full mod-two image,
radical independence or a joint-image fact absent from L073.
If the stated witness hypotheses do not decide the test, isolate
the missing information instead of declaring normality or failure.
No part of this proposed test is derived or approved in step312.

Essential inputs: L073, L074, L077, L078 and audited L079, with
the source-version qualifications in foundations/05 step272 and
drafts/2026-10-18-auxiliary-two-torsion-field-source-notes.md.
Preserve ATTEMPTS/027,028,031,032,033; none is reopened by this
proposal. Other initial-data clauses, retained memberships/scalar
occurrence, marked all-image factorization, pilot transport,
essentiality and finite B>=A remain unresolved. Full matching
and supporting Mathlib coverage for this new target is not checked.

## Direct-source-URL recovery — step314

Added the existing primary URLs directly to SOURCE_EVIDENCE. The previous
assessment pointed to local source notes containing those URLs, which did
not satisfy the supervisor's direct-URL gate. Reopened Antieau–Meier v3,
printed pp.15–16 (corrected action and complete Lemma 4.7 proof), and
Milne v5.10, printed pp.39–40 (Theorem 3.17(c,d), both directions,
and Remark 3.18). The cited versions and scope agree with step313.
Reuse the remaining inspected source coverage, overlap and failure checks.
No new search, theorem comparison, specialization or normality verdict
was needed. TARGET, SPECIALIZE decision and all mathematical limits are
unchanged. This is a STALLED process repair, not a mathematical advance.
