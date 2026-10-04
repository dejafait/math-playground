# Assessment of the depth-p^3 initial-Fitting test

TARGET: Test whether the initial rank-zero Fitting identity at depth p^3, together with L(E,1)=0, forces tau=0 for the fixed-prime p^2 lifting problem under the same non-anomalous ordinary hypotheses and minimal nonzero two-prime Kurihara premise.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Eight bounded queries listed below located the initial-Fitting inputs and Kim's stronger rank-zero p-converse; read primary statements and their coefficient/normalization conventions. Reused the adequate official-scope, p^2, determinant and Angurel assessments.
SOURCE_EVIDENCE: Sakamoto 2022, https://ems.press/content/serial-article-files/29299?nt=1, Section 2.3, Theorem 2.20(2), Remark 3.1, Definition 3.15, Theorem 3.17, Proposition 3.19 and Lemma 4.2; Sakamoto 2021, https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf, Theorem 5.8(i), Remark 5.9 and Theorems 6.3/6.4; Kim, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf, author text dated 2025-05-12, Sections 1.2.2/1.4, Theorem 1.8, Corollary 1.11 and Section 5.3.1.
COMPARISON: The primitive initial Fitting identity and all-depth primitivity are published inputs; Kim's Corollary 1.11 already supplies the stronger finite-Selmer/central-value comparison under the retained nonvanishing premise. The tau question is a local applicability specialization, not a prospect of new arithmetic beyond these sources.
GAP: Apply the known finite-Selmer comparison to L016's nonzero-tau alternative; no such application or depth-p^3 Fitting calculation is completed in this review. Rational membership, r >= 2, analytic production of the two-prime index, the determinant comparison and higher ranks remain missing.
REASON: Approve the original depth-three target but use the stronger known converse by citation first; a reproof of that theorem is redundant. The initial identity is available at index 1 without promoting the old primes from P_(2,0) to P_(3,0).
LITERATURE_REASON: The saved target changed coefficient depth and added L(E,1)=0; the initial normalization and the previously unassessed Corollary 1.11 were concrete source needs. No further review is required for the covered application.
SCOPE: Retain non-CM E/Q, ordinary p >= 5, surjective E[p], p prime to #E(F_p), the Manin constant and every Tamagawa factor, E(Q_p)[p] = 0, and fixed distinct primes in P_(2,0) with a minimal nonzero mod-p two-prime Kurihara index. Add L(E,1)=0 explicitly. Assume neither finite Sha nor positive rational rank, and do not assume the fixed primes lie in P_(3,0).
COVERED_TARGET: Apply Kim's Corollary 1.11 to test whether L(E,1)=0 excludes L016's nonzero-tau alternative under the retained non-anomalous ordinary and minimal nonzero two-prime Kurihara hypotheses.

The original TARGET is preserved exactly from the pending assessment.
This turn completes its source review only. No implication about tau is
proved, no Fitting ideal of a notebook model is calculated, and no lemma
or mathematical script is changed. The next application is approved by
the exact COVERED_TARGET above.

## Main gap and relevance

The exact main gap is rank E(Q) = m(E) for arbitrary m(E) >= 2.
The conditional branch has the upper bound r <= 2; the required lower
bound remains r >= 2. A classical mod-p or p^2 Selmer basis does not
reach that threshold. The proposed intermediate target addresses the
first Sha descent defect that obstructs classical lifting, and could
support a subsequent compatible-lifting and rationality investigation.

L016 already records the nonzero-tau alternative as rational rank zero
with finite p-primary Sha killed by p. Those are the stored consequences
to compare with the new analytic premise. Their application to a known
converse is left to the research turn. The formal subsystem in L017 is
not a full arithmetic family and has no imposed analytic initial value.
Its negative result is retained; the additional hypothesis changes the
test. Even a successful exclusion would not identify rational directions.

## Primary statements and scope

**Sakamoto 2022.** *p-Selmer group and modular symbols*, Documenta Math.
27 (2022), 1891--1922, DOI 10.4171/DM/X21; received 2022-05-13,
revised 2022-07-20. Read the publisher's text at these locations:

- [Section 2.3, p. 1902](https://ems.press/content/serial-article-files/29299?nt=1#page=12): the depth-dependent prime sets P_(m,n).
- [Theorem 2.20(2), p. 1904](https://ems.press/content/serial-article-files/29299?nt=1#page=14): for a basis kappa and d in N_(m,n), R delta(kappa)_d = Fitt^0_R(H^1_(F_cl(d))(Q,T)^vee).
- [Remark 3.1 and the modified modular elements, p. 1908](https://ems.press/content/serial-article-files/29299?nt=1#page=18): the two ordinary unit-root factors are units under the non-anomalous hypothesis.
- [Definition 3.15 and Theorem 3.17, pp. 1914--1915](https://ems.press/content/serial-article-files/29299?nt=1#page=24): the scalar family and its Kato-derived construction.
- [Proposition 3.19 and its proof, pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25): a nonzero residual scalar is equivalent to basis status at every m >= 1, n >= 0; the initial scalar family is the modified cyclotomic element.
- [Lemma 4.2, p. 1917](https://ems.press/content/serial-article-files/29299?nt=1#page=27): residual modular-symbol nonvanishing agrees with residual scalar nonvanishing.

These are precise imported inputs, not a calculation of their consequence
for tau. Index 1 is included at every depth; using an initial identity
does not require a depth-three component at the old two-prime index.
Such a component would require P_(3,0) eligibility, which is not assumed.

**Sakamoto 2021.** *On the theory of Kolyvagin systems of rank 0*,
JTNB 33 (2021), 1077--1102, published 2022-01-26. Rechecked
[Theorem 5.8(i) and Remark 5.9, pp. 1093--1094](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=18),
and [Theorems 6.3/6.4, pp. 1097--1098](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=22).
The initial equality requires a basis; a general system gives only an
inclusion. Base change preserves the free rank-one system module under
the stated Cartesian/core-rank-zero and Galois hypotheses. No equality
for every higher Fitting ideal is imported from Remark 5.9.
The elliptic arithmetic application comes from the 2022 paper, not an
unverified application of the abstract prerequisites.

**Kim.** *The structure of Selmer groups and the Iwasawa main conjecture
for elliptic curves*. The inspected publisher-hosted author PDF is dated
2025-05-12. The [arXiv record](https://arxiv.org/abs/2203.12159)
lists v6, 2025-05-14; file identity is not presumed. Read
[Sections 1.2.2 and 1.4, pp. 4--6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=4),
[Theorem 1.8, p. 7](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7),
[Corollary 1.11 and its proof, pp. 8--9](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8),
and [Section 5.3.1, p. 28](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28).

Corollary 1.11 assumes p >= 5, surjective E[p], Manin constant prime
to p and ord(tilde-delta) < infinity. It states that
Sel(Q,E[p^infinity]) is finite exactly when L(E,1) != 0.
Section 1.4 explicitly identifies tilde-delta_1 with L(E,1)/Omega_E^+.
Theorem 1.8 identifies Selmer corank with ord(tilde-delta); its separate
rational-rank clause retains finite p-primary Sha. The fixed-prime
nonzero mod-p premise is a nonvanishing witness, not a claim that the
global minimum in Kim's integral collection is two. The prime and
modular-symbol definitions were read for the follow-up applicability
check. No positivity of rational rank is assumed by the converse.

This stronger comparison makes a new proof of the arithmetic converse
unnecessary. The remaining notebook-specific application concerns the
recorded tau alternative, not a new rank-zero converse theorem.

## Approved application and continuation test

Use Kim's Corollary 1.11 by citation. Match the retained modular-symbol
nonvanishing witness to his convention, and use the already recorded
Kummer description of the nonzero-tau branch to test its compatibility
with L(E,1)=0. Do not substitute finiteness of all Sha for finiteness
of the p-primary Selmer group, and do not equate the minimal mod-p
two-prime index with analytic order two or the first integral index.

The original depth-p^3 target is also screened: cite Sakamoto's initial
identity at index 1 and all-depth primitivity, then check the classical
coefficient group and initial normalization before computing its Fitting
ideal. Reproving the converse or manufacturing a depth-three component
at ineligible fixed primes is unnecessary. A coefficient calculation is
justified only if needed to verify the specific finite-depth connection;
it is a reproduction/application, not a claim beyond the literature.

Continue the lifting route if the cited comparison excludes the stored
nonzero-tau branch under the extra analytic premise. Stop that inference
if a hypothesis or normalization cannot be matched, recording the exact
failure. Success leaves higher compatible classical lifting, rational
Kummer membership and the r >= 2 lower bound as separate questions.
No test or outcome of this application is claimed in this review.

## Searches, redundancy and access

Queries actually issued on 2026-10-04:

- `Sakamoto "p-Selmer group and modular symbols" Fitting initial`
- `Sakamoto "On the theory of Kolyvagin systems of rank 0" "Fitting"`
- `"Kurihara" "L(E,1)" "Fitting" Selmer`
- `"Selmer" "L(E,1)" "converse" "rank zero" ordinary`
- `"Sakamoto" "initial Fitting" "L" elliptic`
- `"prime-deletion" "Kolyvagin" Fitting`
- `"The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves" Kim arxiv`
- `"Corollary 1.11" "rank zero" Kim Selmer`

Primary PDFs, not the returned abstracts, secondary summaries or seminar
notes, support the comparison. A mistaken arXiv address 2203.12161 was
opened and identified as a different paper; it supplies no evidence here.
The title search resolved the correct record 2203.12159. No essential
source remains unread or inaccessible for the covered application.
Other search hits, including the p = 3 extension and general Stark-system
papers, were discovery leads only and are not imported inputs.

Reuse the adequate previous assessments for the unchanged Clay scope,
p^2 local framework, determinant route and Angurel comparison. Do not
repeat ATTEMPTS/017--018 or reopen the parked Eisenstein source blocker.
The two unsuccessful automatic-promotion mechanisms are preserved; the
new analytic comparison changes the mechanism and hypotheses. This step
adds usable known source coverage, not a mathematical result about tau,
a rank improvement, an arithmetic counterexample or evidence of novelty.

## Mathlib

Full library coverage of the depth-three/tau implication: **not checked**.
Supporting initial Fitting identities, coefficient-level primitivity,
Kummer sequences and analytic normalization: **not checked**.
Sakamoto's Theorem 2.20 and Proposition 3.19 match the Fitting/primitivity
inputs; Kim's Corollary 1.11 matches the stronger arithmetic comparison.
None is a claimed Mathlib theorem or a verbatim full tau-statement match.
No library absence or originality inference is made.
