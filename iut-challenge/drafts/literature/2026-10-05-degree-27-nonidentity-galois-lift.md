# Degree-27 nonidentity-Galois lift — source comparison

TARGET: Test whether L017's compact involution can be induced on J by a full model MLF×-pair automorphism with a nonidentity G_K component, identifying source-backed restrictions on its effect on unit filtrations; keep original ind2 and tensor realization outside the conclusion.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched absolute-Galois automorphisms, ramification/unit filtrations, cyclotomic compatibility and reciprocity/norm terminology; checked L018 and ATTEMPTS/015 for overlap; found a primary absolute-norm reconstruction and its compatibility theorem rather than an unconditional higher-filtration theorem.
SOURCE_EVIDENCE: Hoshi, Introduction to Mono-anabelian Geometry, PMB (2021), DOI 10.5802/pmb.42, Lemma 1.7 pp. 15–16, Theorem 2.3 pp. 17–18, Propositions 3.11 and 4.2 pp. 22 and 25–26, Remark 3.15.2 p. 24, Theorem 7.6 with proof pp. 39–40; Hoshi, Topics in the Anabelian Geometry of Mixed-characteristic Local Fields, author-hosted June 2018 RIMS1882 revised text, Lemma 4.1 with proof pp. 33–34, Definitions 4.5–4.7 and Proposition 4.9(i) pp. 35–37, Definition 4.12/Remark 4.12.1 p. 39, Theorem 4.13(i) and its proof p. 40.
COMPARISON: General Galois automorphisms need not preserve higher ramification filtrations; the reconstructed absolute norm instead has a cited compatibility theorem applicable to an automorphism. Relating that reconstructed action to a specified full-pair logarithmic action still requires accounting for the known exponent ambiguity.
GAP: Specialize the norm-compatible reconstructed action and the full-pair torsor to J, justify logarithm descent and the trace/norm identity, and test the resulting necessary condition on L017's exact g; no such specialization or outcome is established this turn.
REASON: The changed G_K hypothesis required essential unread coverage. The inspected norm theorem supplies a materially different discriminating test without incorrectly extending L018's scalar-kernel valuation argument.
SCOPE: The unchanged degree-27 field, full model MLF×-pair, J and fixed L017 involution; arbitrary nonidentity G_K automorphisms. Covered technique is reconstructed reciprocity/cyclotomic norm, its exponent ambiguity and logarithmic specialization; higher-unit-filtration preservation may only be used under an explicit additional ramification-preservation hypothesis.

## Source hypotheses and versions

Use the [published PMB primary text](https://www.numdam.org/item/10.5802/pmb.42.pdf), retaining its 2021 volume and 2022 online-publication qualification from the prior assessment. Theorem 2.3 requires topological absolute-Galois isomorphisms of finite p-adic fields; filtration compatibility is equivalent to geometricity. Remark 3.15.2 records nonfiltered automorphisms in some fields, not specifically this K. Propositions 3.11/4.2 identify reconstructed units and logarithms via reciprocity. The complete proof of Theorem 7.6 constructs lifts by reconstruction and Kummer transport, then identifies their exponent ambiguity; it does not make all lifts geometric.

For the new input use the [author-hosted RIMS1882 revised PDF](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1882revised.pdf#page=33), whose title page says **June 2018**, 72 pages. The author's [publication list](https://www.kurims.kyoto-u.ac.jp/~yuichiro/papers_e.html) records the later Hiroshima Mathematical Journal 49 (2019), 323–398 version. Journal full/PDF endpoints exposed no mathematical text; theorem/page locators here refer to the inspected preprint, not an assumed page-for-page match with publication.

Lemma 4.1(iii) identifies the norm to the minimal MLF with χ_p-cyc(rec_k(a))^(-1) p^(f_k ord_k(a)). Its proof uses the Q_p cyclotomic/Lubin–Tate identification and reciprocity's norm compatibility. Proposition 4.9(i) identifies this with the reconstructed Nmabs. **No absolutely abelian hypothesis** occurs in these assertions, despite the section title. Remark 4.12.1 covers every open injection. Theorem 4.13(i) requires a cyclotomically compatible, surjective open homomorphism and preserves Nmabs under the canonical coefficient identification. Its relevant proof uses Proposition 3.4(iii) and Remark 3.5.1; parts (ii)–(iii)'s AAMLF hypotheses are unnecessary here. An automorphism satisfies the stated group-level conditions.

These are cited inputs, not new classifications. The ordinary logarithm/norm compatibility is to be justified using finite conjugates, the continuous logarithm already established in L016, and its homomorphism property; no reproof of local class field theory or a general lifting theorem is proposed.

## Bounded test authorized for a later research turn

Retain K=Q_3(pi), pi^27=3, kbar, G_K and the fixed logarithm coordinates. Inputs are L016's complete J and continuity, L017's g and q,w,z,A,B, and L018's restricted stop. No field, trivialization or tensor packet is changed.

First identify the reciprocity-based reconstructed lift and compare a full-pair lift with it through Theorem 7.6's torsor. Track the profinite exponent and its 3-adic unit component, including continuity and torsion when descending to J. Then establish or reject the proposed necessary relation

\[
\operatorname{Tr}_{K/\mathbb Q_3}\circ g
=\lambda_3\operatorname{Tr}_{K/\mathbb Q_3}\quad\text{on }J,
\qquad\lambda_3\in\mathbb Z_3^\times.
\]

This displayed relation is a **target for specialization**, not a proved lemma here. Test it on L017's exact q and its proved image, or on a verified trace-zero input; do not substitute valuation preservation. No evaluation is performed in this review. This is an independently testable necessary lift condition, useful for deciding whether the auxiliary witness can reach full source pair data while leaving other bridges unresolved.

If the justified condition fails, stop this exact full-pair witness route for all G_K components covered by the argument. If it passes, record only a passed necessary condition: Hoshi's existence of some lift does not specify this g. If the reconstruction-to-full-pair comparison cannot be justified, preserve that exact gap and abandon the inferred obstruction. Any different map or lifting mechanism needs separate coverage. Original ind2, forgotten/quotient-only actions, tensor/initial-data realization, ind3, marked pilot, essentiality and normalized finite B >= A remain outside the conclusion.

## Discovery record and qualifications

Queries included `local fields absolute Galois isomorphism units filtration characteristic ramification Mochizuki Hoshi`, `absolute Galois automorphism local field norm cyclotomic character units trace Hoshi`, and `MLF cyclotomic character`. Read the primary ranges above and the relevant proof cases; reuse adequate prior full-pair definitions/kernel coverage. Mochizuki's author-hosted local Grothendieck theorem and Sharifi's local-CFT notes confirmed terminology but add no essential input. Newer outer-automorphism/Hodge–Tate papers remain unread leads, not supporting theorems. No exact degree-27 lifting result was found or imported; this is not evidence of novelty.

The valuation-preservation shortcut is excluded; cyclotomic compatibility is weaker than preservation of the full ramification filtration. A norm restriction concerns a quotient character, not all unit layers. Mathlib coverage for the full-pair, reconstructed norm and this field-specific test is **not checked**. No lemma, mathematical script, DAG or mathematical argument overview is changed this turn.
