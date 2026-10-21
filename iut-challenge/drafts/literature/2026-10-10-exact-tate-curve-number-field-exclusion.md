# Exact Tate curve — known-theorem application coverage

TARGET: Apply the inspected p-adic Mahler-Manin theorem and j-invariance to L042's exact curve, testing geometric realization by an elliptic curve over a number field.
CHECKED: 2026-10-10
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the exact-parameter search and theorem comparison in drafts/literature/2026-10-10-exact-tate-parameter-global-algebraicity.md; no broader target or new transcendence search is required.
SOURCE_EVIDENCE: Gramain JTNB 11(1) (1999), pp.73-74, https://www.numdam.org/item/JTNB_1999__11_1_73_0.pdf; Waldschmidt CNTA5 Carleton (1996), Theorem 1 p.2 and proof pp.3-8, https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/CNTA5.pdf; Milne EC2 (2021), III.3 (24)-(26) pp.102-103 and II.2.1(c) pp.50-51, https://www.jmilne.org/math/Books/EC2.pdf; prior proof coverage reused, direct endpoints and essential statements rechecked 2026-10-10.
COMPARISON: A known transcendence theorem and standard j-invariance cover this exact realization screen; only checking their hypotheses and writing the number-field implication is needed, with no reproof of either theorem.
GAP: The application has not been written as a canonical lemma; no statement about another curve with an isomorphic local torsion field, admissible global initial data or an original IUT flaw is covered.
REASON: Use the now-inspected known result to decide the exact-curve prerequisite before spending more work on its global initial-data realization.
SCOPE: Fixed C_3 and Q_3 closure of audited L042, primitive zeta_60, H=Q_3(zeta_60), q=3^30, standard untwisted E_q; compare with arbitrary number field F embedded in C_3 and an elliptic curve E/F whose C_3 base extension is isomorphic to E_q over C_3.

The [completed source comparison](2026-10-10-exact-tate-parameter-global-algebraicity.md)
contains queries, direct source links, theorem statements, proof-case
coverage, normalization checks and the original-publication access limit.
Use those citations in the canonical result. No original Inventiones
proof inspection or new transcendence proof may be claimed.

Essential local input is audited L042 only for the identity of the curve
and its parameter. Its full torsion and exact degrees are preserved but
do not prove global realization. The upcoming application must retain
algebraicity over Q, the p-adic absolute value, the full j-function and
geometric isomorphism. It must check the number-field field-of-definition
hypothesis rather than assume it for E_q. An abstract local field
isomorphism fixing Q_3 cannot silently change the exact rational q.

The main gap is still original finite B>=A. The intermediate target is
this one exact-curve realization screen; its downstream use is to stop
or justify that globalization direction. The discriminating test is
whether the cited transcendence conclusion conflicts with the j-value
required by a number-field curve. If it does, park exact-curve
globalization while preserving L042's local pass. Do not extend that
stop to torsion-field-only realization. Global F/F_0, prime-to-7 degree,
global rational 30-torsion, selected-place conditions, actual/native
input/action, pilot transport and essentiality remain unresolved.

## Direct-source recovery review — 2026-10-10

The supervisor reported missing direct URLs in this ready assessment.
The links are now explicit here rather than available only through the
preceding review. This repairs citation traceability; the IMPORT decision
and exact target are unchanged. No new theorem application is performed.

- [Gramain, published coauthor restatement](https://www.numdam.org/item/JTNB_1999__11_1_73_0.pdf), printed pp.73-74: the theorem is stated for algebraic q, and the following paragraph explicitly includes its p-adic analogue. The remainder of the exposition is complex; do not cite it as a p-adic proof.
- [Waldschmidt, CNTA5 author version](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/CNTA5.pdf), printed pp.1-2: C denotes either the complex field or C_p; Theorem 1 assumes 0<|q|<1 and asserts that q and J(q) cannot both be algebraic over Q. J=Q^3/Delta is the full normalized modular series. These statements were rechecked at the direct endpoint; the preceding assessment's inspected proof pp.3-8, including its explicit p-adic cases, is reused without a fresh proof audit.
- [Milne, EC2 second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf), III.3, printed pp.102-103, equations (24)-(26): standard Tate coefficients, full j-series, and identities valid p-adically; II.2.1(c), printed pp.50-51: invariance under geometric isomorphism in characteristic different from 2 and 3. These essential passages were rechecked. The p-adic paragraph explicitly covers rational-field parameters, sufficient for the fixed parameter in this assessment.

The original Inventiones article remains identified but not inspected;
its access limit does not block this already-inspected statement and
independent proof coverage. No new search for stronger transcendence
results or broader globalization was needed. Prior history/133-134 and
ATTEMPTS/022,025,026 were checked for duplicates and distinct-field stops;
none is an exact-curve number-field application. Preserve those stops.

The repaired ready continuation receives separate supervisor approval
next turn. Its eventual application classification is KNOWN_IMPORTED.
Full matching Mathlib coverage is not checked. No lemma, mathematical
script, DAG edge or PROOF assembly was changed.
