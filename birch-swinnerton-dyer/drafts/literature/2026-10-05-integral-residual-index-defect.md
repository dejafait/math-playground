# Integral versus residual index: proposed structural audit

TARGET: Quantify the finite paired Selmer contribution to the minimal mod-p Kurihara prime count under Selmer corank two, and test whether residual primitivity alone removes it, using Kim and Sakamoto without assuming finite Sha.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed analytic-order-two comparison and existing all-depth structure assessment; no separate discovery or new theorem is proposed.
SOURCE_EVIDENCE: Kim, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf, dated 2025-05-12, Theorems 1.8/1.10 (printed pp. 6--7), Section 5.3.1 (p. 27); Sakamoto, https://ems.press/content/serial-article-files/29299?nt=1, Doc. Math. 27 (2022), Definition 1.4/Theorem 1.5 (p. 1893), Proposition 3.19 (pp. 1915--1916), Lemma 4.2 (p. 1917), Theorem 4.8 and proof (p. 1919).
COMPARISON: The paired finite decomposition and residual index theorem cover the inputs; the proposed work isolates their exact discrepancy under a granted corank-two hypothesis rather than claiming complex-order equality.
GAP: Determine the extra finite-quotient condition required for residual prime count two, separately from unrestricted nonvanishing and P_(2,0) eligibility.
REASON: A bounded applicability audit can expose whether improving analytic-to-corank coverage would actually produce L018's stronger residual premise; no reproof of either theorem is needed.
LITERATURE_REASON: Supervisor recovery requires direct primary URLs in the ready assessment; inspect the load-bearing statements and primitivity proof to complete the saved target's separate approval, retaining its hypotheses.
SCOPE: Non-CM E/Q, ordinary non-anomalous p >= 5, surjective E[p], prime-to-p Manin/Tamagawa factors and E(Q_p)[p] = 0; grant Selmer corank two and residual-family nonvanishing explicitly. Do not assume finite Sha, rational rank two, residual dimension two or P_(2,0) nonvanishing.

## Inputs, intended use and bounded test

Use the precise primary citations and qualifications in
[the completed comparison](2026-10-05-analytic-order-two-kurihara-production.md)
and [the coefficient assessment](2026-10-04-central-vanishing-all-depth-classical-lifting.md).
Import known structure and residual localization by citation. The only
proposed specialization is the finite paired contribution to residual
size. No derivation or countermodel has been performed in this turn.

Local inputs L015 and L018 identify the desired downstream two-prime
threshold, but their conclusions must not be used as premises: their
hypotheses already eliminate the very discrepancy under examination.
C016a also assumes the two-prime witness. This audit starts before it.
No actual curve or modular-symbol collection need be constructed.

Continue if the audit yields an exact missing finite-quotient condition
or an informative obstruction to the proposed primitivity implication.
Abandon attempts to infer a two-prime witness from corank alone if a
paired finite contribution survives the imported constraints. Any formal
compatibility example must be labeled non-arithmetic. P_(2,0) eligibility,
production of Selmer corank two from complex order two, rational membership
and higher ranks remain independent unresolved assumptions.

The separate literature approval was completed on 2026-10-05 in step
BSD-2026-10-05-037-residual-defect-source-approval. The exact TARGET is
approved for the next mathematical turn; no specialization was performed
in this approval.

## Primary statements inspected for approval

**Kim**, *The structure of Selmer groups and the Iwasawa main conjecture
for elliptic curves*, author text dated 2025-05-12:
[Theorem 1.8, printed p. 6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7)
assumes p >= 5, surjective residual representation, prime-to-p Manin
constant and nonzero integral Kurihara collection. It gives Selmer corank,
paired finite cyclic factors, and finite-quotient length
partial^(ord)(delta) - partial^(infinity)(delta). The rational-rank
clauses add finite p-primary Sha.
[Theorem 1.10, p. 7](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8)
adds E(Q_p)[p] = 0 and prime-to-p Tamagawa factors; residual nonvanishing
implies partial^(infinity)(delta) = 0. It supplies residual localization
at the first residual index, with a separate Sha[p] = 0 hypothesis for
its rational-rank formula.
[Section 5.3.1, p. 27](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28)
uses Sel(E[p^k]) = Sel(E[p^infinity])[p^k], citing Mazur--Rubin
Lemma 3.5.3. These inputs match the saved scope. Import them; no reproof
is needed. Do not identify the two indices in advance.

**Sakamoto**, *p-Selmer group and modular symbols*, Doc. Math. 27
(2022), 1891--1922:
[Section 1.1, pp. 1891--1893](https://ems.press/content/serial-article-files/29299?nt=1#page=2)
assumes ordinary p > 3, surjective E[p], and p prime to #E(F_p) and all
Tamagawa factors. P_(1,0) requires ell congruent to 1 mod p and
E(F_ell)[p] cyclic of order p. Definition 1.4 uses divisor-minimality;
Theorem 1.5 identifies its prime count with dim Sel(E[p]).
[Proposition 3.19 and proof, pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25)
equates residual scalar nonvanishing with basis status of the rank-zero
Kolyvagin system at every coefficient depth. The proof uses a free
rank-one system module and a unit multiplier; this is system primitivity,
not primitivity of the scalar at the empty index.
[Lemma 4.2, p. 1917](https://ems.press/content/serial-article-files/29299?nt=1#page=27)
identifies scalar and modular-symbol nonvanishing.
[Theorem 4.8 proof, p. 1919](https://ems.press/content/serial-article-files/29299?nt=1#page=29)
uses Lemma 4.4 and Proposition 4.7 to find a divisor with prime count
lambda(1); minimality identifies that divisor with the original index.
These statements cover the proposed residual comparison, without a
P_(2,0) existence assertion.

## Reuse, duplicates and qualifications

The completed analytic-order comparison already reviewed these theorem
families; this turn checked their precise statements at the direct URLs,
rather than repeating discovery. ATTEMPTS/015 records the failure of
primitivity-to-rational-determinant import. The depth-three initial-Fitting
assessment already covers all-depth system primitivity. Neither is a
completed audit of the saved corank-two finite residual contribution.
Do not repeat L018's lifting result or use its stronger premises here.

The approved specialization is confined to taking p-torsion of the
imported decomposition and comparing the cited residual count. Its
discriminating test remains whether system primitivity removes the
finite quotient. No new lemma, compatibility model, arithmetic example
or implication about actual elliptic curves was established in this
source approval. No unread external lead is needed for this bounded test.

## Mathlib

Full matching theorem: not checked. Supporting finite-module reasoning
may be elementary; unknown coverage is not absence. No formalization
claim is made.
