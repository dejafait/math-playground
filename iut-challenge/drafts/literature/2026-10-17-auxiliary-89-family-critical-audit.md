# Auxiliary p=89 family — proposed critical audit scope

TARGET: Critically audit L073's auxiliary p=89 Frobenius-square, fixing-field and refined-family specialization, including same-witness retention.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step287 read all of L073 and the completed step284/285 assessments, searched the exact L044/L045/L046/L048 source and retention passages, compared ATTEMPTS/027,028,031,032, and directly retrieved Milne and Zywina's cited primary passages. Reuse the existing targeted theorem searches; no novelty search or mathematical audit is claimed.
SOURCE_EVIDENCE: Prior inspected coverage: Milne (2021), https://www.jmilne.org/math/Books/EC2.pdf, II.6 Corollary 6.2 pp.70–71, IV.9 Theorem 9.4/proof p.150, V.7 Proposition 7.5/(46) p.217, V.8 Propositions 8.1/8.3 pp.220–221; Zywina, https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf, section 1.1 pp.1–2, Definition 5.1 p.6, Proposition 5.7/proof p.8 and Lemma 2.4 proof p.5; precise local-constancy and retention sources are recorded in L044/L045/L046/L048.
COMPARISON: The cited general theorems and audited local inputs cover this exact proof-audit scope; only the explicit specialization and its applicability require independent checking. Approve SPECIALIZE for an audit classified REPRODUCTION, without certifying L073 or claiming progress beyond the sources.
GAP: The independent mathematical audit of the finite-field count, full level-120 identity, fixing fields, refined count, domination and same-witness retention remains outstanding; no essential source gap was identified for that audit.
REASON: Step287 separately approves the previously proposed critical-audit source scope using unchanged ready coverage and direct primary checks. This is source approval, not completion of the proof audit or new mathematics.
LITERATURE_REASON: The startup gate requires separate approval of the new L073 critical-audit assessment; the precise source comparison was not previously completed for this audit target. No expansion of the mathematical target is made.
SCOPE: Exactly TARGET, all of L073 with direct inputs L044,L045,L046,L048, fixed c and fixed M>=max(M_tors,31); downstream L071/L072 applications and explicit coefficient searches are excluded.

## Scope proposed for separate approval

Read L073's whole proof, with inputs L044,L045,L046,L048 and the
existing source assessment. Check the exact elementary point count
and discriminant, all prime-power parts of E_aux[120], arithmetic
versus geometric Frobenius, the single actual lift, determinant
modulo 120, pointwise fixing of K_aux/F_aux, CRT independence and
the positive family count against the entire-box exceptional bound.
Verify that original 3^M precision is retained before the short
coordinate change, M stays fixed, and local modules, H,N and
v_3(q_aux)=30 concern the same new witness.

This is a proposal for one critical proof audit using imported general
theorems. It authorizes neither searching for explicit coefficients nor
applying L071/L072 to obtain additional radical conclusions in that
audit. Those are downstream possibilities. Preserve the old E_0,F,
K_glob, places and q_0. Native T/model, exact generation, independent
initial data, marked all-image factorization, pilot transport,
essentiality and finite B>=A remain unresolved. Mathlib coverage is
unchecked. No mathematical exploration budget is spent by approving
this source scope.

## Step287 separate source approval — 2026-10-17

The full L073 proof was read to identify its source obligations, not
to issue its pending mathematical verdict. Reused the completed
`2026-10-17-auxiliary-frobenius-joint-scalar-review.md` and
`2026-10-17-auxiliary-89-frobenius-family-test.md`. Their Galbraith
classification leads remain unread and unnecessary: the proposed audit
checks the existing elementary count, without importing a classification.

Directly reread [Milne](https://www.jmilne.org/math/Books/EC2.pdf),
II.6 Corollary 6.2 and its complete proof (printed p.70), IV.9
Theorem 9.4's proof (p.150), and V.8 Propositions 8.1/8.3 with
their reduction arguments (pp.220–221). The relevant hypotheses are
an elliptic curve over Q, good reduction at p, and Tate prime unequal
to p. The preceding Frobenius definition uses the residue p-power
automorphism. Proposition 8.3's proof identifies the Tate-module
actions by reduction; Corollary 6.2 supplies an endomorphism identity,
whose coefficients are identified in IV.9.4's proof. The audit must
check all finite-level parts and one actual lift, rather than trace
and determinant alone. These are imported theorems, not new reproofs.

Directly reread [Zywina](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
author-hosted 15-page version: section 1.1's coefficient-box definition,
Definition 5.1 (p.6), Proposition 5.7 with its entire proof (p.8),
Lemma 2.4's opening proof assertion (p.5), and section 5.1's
cyclotomic-determinant statement (p.6). The bound allows k=Q,
fixed level and fixed norm; it concerns failure of SL_2 containment
among nonsingular integral short models. Its proof uses the finite
conjugacy-class union and Proposition 5.5, whose deeper sieve inputs
remain covered by L046's existing assessment. No theorem there
asserts the refined family's positive count. That count, fixed-modulus
domination, and transfer through the actual pointed map remain audit
obligations. Theorem 1.3's restriction on Q is not used.

For retention, reuse L044's already audited Bisatt–Dokchitser,
*Tame torsion and the tame inverse Galois problem*, Theorem 2.2,
p.1441 ([primary repository PDF](https://d-nb.info/1235382842/34), p.3),
including genus one, arbitrary m and a squarefree same-degree
neighborhood. L045's Hypotheses/Conclusion and L048's Hypotheses,
Conclusion and “One fixed precision and one curve” audit passage
were read. Their existing coverage applies to any member in the
fixed original neighborhood; the new audit must verify that L073
actually retains it and applies the local/global constructions to
one witness. This source turn does not re-audit those mathematical
inferences or assert their success for L073.

Duplicate/failure comparison: L046 covers the unrefined family,
L048 the fixed neighborhood's reduction, and L072 only a conditional
downstream consequence. ATTEMPTS/027 excludes the exact old Tate
curve, 028 treats a broad model predicate, 031 parks unverified
marked coordinates, and 032 records a surviving native enclosure.
None certifies L073 or prohibits this distinct audit. Old and auxiliary
curves, global fields, places and parameters must remain distinct.

Continue with the exact audit only if these hypotheses suffice at
each use; pass L073 only after every count, action, fixing and
retention check succeeds, otherwise report the precise failed
inference. Its possible downstream use remains an auxiliary joint
scalar test. Native T/model, exact generation, independent initial
data, marked all-image factorization, pilot transport, essentiality
and original finite B>=A are unresolved. Mathlib coverage remains
unchecked. No lemma, script, argument overview or DAG was changed.
