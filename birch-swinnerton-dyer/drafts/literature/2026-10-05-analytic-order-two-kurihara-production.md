# Analytic order two to the two-prime premise: pending source scope

TARGET: Assess whether primary Kurihara nonvanishing and modular-symbol theorems produce a minimal nonzero mod-p two-prime index with primes in P_(2,0) from analytic order two under L018's ordinary residual hypotheses, without finite Sha or an assumed Selmer corank.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Two targeted searches for Kurihara mod-p nonvanishing, analytic rank two and modular-symbol Selmer dimension located primary Kim and Sakamoto statements; reused the saved Castella--Sano and BCGS assessments and inspected the changed comparison in Castella--Sano v1.
SOURCE_EVIDENCE: Kim publisher-hosted author PDF dated 2025-05-12, Sections 1.2.2/1.4/1.5, Corollary 1.6, Theorems 1.8/1.10 and Corollaries 1.11/1.12; Sakamoto 2022, Section 1.1, Definition 1.4, Theorems 1.2/1.5/4.8, Corollary 1.9 and proof of Theorem 4.8; Castella--Sano arXiv:2601.14504v1, Sections 1.1.1/1.1.4/1.3.1, Theorem A, Corollary A and Proposition 2.2.3.
COMPARISON: Known results cover integral nonvanishing at ordinary p and conditional residual nonvanishing, but measure Selmer corank or residual Selmer dimension rather than exact complex order; their stated prime sets do not certify the fixed P_(2,0) threshold.
GAP: No inspected theorem produces residual dimension two or a minimal two-prime P_(2,0) witness from analytic order two on the retained hypotheses; full integral main-conjecture applicability and restricted-prime nonvanishing are not established here.
REASON: Park direct analytic-order-to-two-prime import; specialize the known structural comparison only to isolate the finite residual defect in a separate approved attempt, without claiming analytic equality or arithmetic realization.
LITERATURE_REASON: The target removes the assumed two-prime witness and adds exact analytic order two; existing ready assessments cover applications after nonvanishing, not this changed hypothesis.
SCOPE: Non-CM E/Q; p >= 5 good ordinary and non-anomalous; surjective E[p]; Manin and Tamagawa factors prime to p; E(Q_p)[p] = 0; ord_(s=1) L(E,s) = 2. Do not assume finite Sha, positive rational rank, Selmer corank two or the nonzero two-prime premise.

## Essential inputs and test

Use L015's fixed-prime notation, C016a's hypothesis matching and L018's
conditional conclusion as the intended downstream application. Their
conclusions are not premises for producing the missing witness. Reuse
the saved primary source assessments for normalizations and P_(m,0).
Search exact residual nonvanishing statements and analytic-rank
comparisons, then read primary hypotheses and the essential cases.

The intermediate threshold is a nonzero mod-p scalar at a two-prime
index eligible at depth p^2, together with minimality in the same
residual convention. Mere nonzero integral collections or an unspecified
number of primes do not meet it. A result assuming finite Sha or already
assuming Selmer corank two must be recorded as conditional, rather than
silently used to infer it from analytic order two.

Continue if an inspected theorem supplies the threshold on these
hypotheses, or a concrete weaker input with a plausible independent
use and a separately reviewable test. Otherwise record the exact
hypothesis/index mismatch and choose a materially different target.
Rational membership, the r >= 2 lower bound, analytic comparison and
higher ranks remain open even if this production question succeeds.
The pending discovery has now been completed by the source comparison below.
This turn supplies source evidence only; no new mathematical result is claimed.

## Mathlib

Full matching production theorem: not checked. No absence inference.

## Completed source comparison (2026-10-05)

The exact TARGET remains unchanged. Searches used:
`Kurihara numbers mod p nonvanishing analytic rank two Kim conjecture`
and `Kurihara nonvanishing modular symbols two primes analytic rank Selmer dimension Sakamoto`.
Search summaries were locators only. No claim of exhaustive coverage or novelty is made.

**Kim**, *The structure of Selmer groups and the Iwasawa main conjecture
for elliptic curves*, [author PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf),
2025-05-12, printed pp. 3, 5--8: Corollary 1.6 supplies integral-family
nonvanishing at ordinary primes. Theorem 1.8 equates its integral
index with Selmer corank and retains paired finite factors; rational
rank requires finite p-primary Sha. Theorem 1.10 assumes p >= 5,
surjective residual representation, prime-to-p Manin/Tamagawa factors
and E(Q_p)[p] = 0. It equates mod-p family nonvanishing with the full
main conjecture, with residual localization isomorphism at a first
nonzero index. Corollary 1.12 supplies analytic parity, not order equality.
Section 1.2.2 defines P_k by congruences, not Sakamoto's cyclicity test.
These match the retained arithmetic assumptions but do not assert
analytic order two gives a two-prime residual index. Integral
nonvanishing alone is insufficient for that import. Full main-conjecture
hypotheses were not audited in this step and are not silently imported.

**Sakamoto**, *p-Selmer group and modular symbols*, Doc. Math. 27
(2022), 1891--1922, [primary PDF](https://ems.press/content/serial-article-files/29299?nt=1),
pp. 1892--1894, 1919: hypotheses (a)--(c) are ordinary p > 3,
surjective E[p], and p prime to #E(F_p) and the Tamagawa product.
Definition 1.4 uses divisor-minimality. Theorem 1.2 equates existence
of a residual witness with the main conjecture. Theorem 1.5/4.8
identifies each minimal witness's prime count with dim Sel_p.
Its proof uses Lemma 4.4's zero transverse Selmer space and
Proposition 4.7's divisor of size lambda(1); minimality forces that
divisor to be the original index. Corollary 1.9 gives only analytic
parity. The theorem uses P_(1,0). The saved depth-two assessment
retains the additional cyclic p^2 and congruence conditions for P_(2,0).
No read statement promotes this existence to P_(2,0) or makes its
prime count two from complex order two.

**Castella--Sano**, *On refined nonvanishing conjectures by Kurihara
and Kolyvagin*, [arXiv:2601.14504v1](https://arxiv.org/html/2601.14504v1),
2026-01-20, Theorem A/Corollary A: under non-CM, p > 3, surjectivity
and prime-to-p Manin constant, refined divisibility equals the Tamagawa
valuation iff the main conjecture holds. When Tamagawa factors are
units, this yields equivalence with residual nonvanishing at some index.
Section 1.3.1 identifies the ordinary non-anomalous overlap with Kim
and Sakamoto. Section 1.1.1 uses congruence primes; neither two factors
nor P_(2,0) is stipulated. Proposition 2.2.3 identifies its determinant
main conjecture with characteristic-ideal equality, so the equivalence
cannot be read as an unconditional analytic-rank comparison.

The earlier BCGS assessment is reused only for its integral Kato-family
nonvanishing/fine-Selmer-index scope; no unread stronger theorem is
claimed. The newly located Kim--Pollack arXiv:2505.09121 and the
Kriz--Nordentoft search hit are unread leads, not imported inputs.

## Route test and continuation

The required threshold was exact two-prime residual nonvanishing with
P_(2,0) eligibility. Inspected results leave residual dimension and
restricted-prime existence open, even if ordinary family nonvanishing
is available. This is a negative source comparison, not a counterexample
to BSD or to witness existence. L015, C016a and L018 remain conditional;
no proof overview or dependency has changed.

A separate continuation will audit the integral-versus-residual defect
under the deliberately stronger Selmer-corank-two assumption. Its use
is to identify the additional input needed before any analytic-to-corank
argument could feed the existing basis route. The newly saved assessment
requires separate supervisor approval next turn; no derivation occurs here.
Rational membership, r >= 2, analytic equality and higher ranks remain open.
