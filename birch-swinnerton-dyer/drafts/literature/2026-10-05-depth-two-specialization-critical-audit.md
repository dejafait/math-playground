# Source approval for the depth-two specialization audit

TARGET: Critically audit L022's depth-two unit detection, common-index scalar projection and support-preserving minimization against the cited theorem hypotheses.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready depth-two prime-restriction assessment and its Mazur--Rubin discovery/existence coverage; searched L021/L022, ATTEMPTS/021 and histories/039--040 for duplicates, prior failure and changed scope; reopened the published Sakamoto theorem statements and essential proof cases for this audit.
SOURCE_EVIDENCE: Sakamoto, p-Selmer Group and Modular Symbols, Doc. Math. 27 (2022), 1891--1922, DOI 10.4171/DM/X21, revised 2022-07-20: Section 1.1, Section 2 setup, Lemma 2.2, Definitions 2.3--2.4, Corollary 2.15, Sections 2.3--2.4, Theorem 2.20/Remark 2.21/Corollary 2.22, Lemmas 3.13--3.14/Definition 3.15, Theorem 3.17/Proposition 3.19 and proofs, Lemma 4.2 and proof, Proposition 4.7/Theorem 4.8 and proof.
COMPARISON: The published unit-detection and inverse-limit-family statements cover the imported inputs; Section 2.4 fixes quotient isomorphisms rather than canonically choosing bases. L022's exact common-index map and normalization argument therefore remain a bounded mathematical audit, not a consequence of rank-one freeness alone.
GAP: Audit the conditional specialization, especially compatibility of quotient trivializations and unchanged G_d under downward coefficient projection; do not treat source approval as a completed proof audit.
REASON: Adequate primary coverage is available for testing the completed conditional application without a new existence theorem or a reproof of system rigidity.
LITERATURE_REASON: The changed critical-audit target requires separate source approval; source comparison must distinguish coefficient projection from the inclusion in Lemma 2.2 and distinguish chosen quotient bases from canonical maps.
SCOPE: All L022 hypotheses, the constructed Kato-derived family, compatible normalizations and common indices at (2,0) and (1,0); L021 is the sole direct local input. No weakening of the zero finite quotient or residual nonvanishing assumptions is covered.

## Reused coverage and exact source cases

The ready [production assessment](2026-10-05-depth-two-prime-restriction.md)
already inspected Mazur--Rubin's core-vertex existence and p>=5
Chebotarev case. Its target and arithmetic assumptions are unchanged
inside this audit. Repeating discovery searches or reproving that
machinery would not improve coverage. L022 is the completed application
to audit, not a duplicate lemma to create. ATTEMPTS/021 and L021 retain
the finite-defect obstruction; the audit grants its extra finite condition.

The primary source is [Sakamoto's published text](https://ems.press/content/serial-article-files/29299?nt=1).
The reviewed version has received date 2022-05-13 and revised date
2022-07-20. Section 1.1, p. 1892, assumes p>3, good ordinary reduction,
surjective residual action and p prime to the local point count and
Tamagawa product. Section 2, p. 1896, specifies the induced representation
and group ring and records (H.0)--(H.3), with the p=3 caveat. L022 retains
p>=5 and the additional Manin/local-torsion hypotheses of L021.

On pp. 1897--1898, Lemma 2.2 is explicitly an inclusion-induced
identification with maximal-ideal torsion and a vanishing equivalence
for the dual propagated structure. Definitions 2.3--2.4 describe
transverse modification, its dual, and classical self-duality. These
cover the vanishing input, but Lemma 2.2 is not the downward scalar map.
Corollary 2.15, p. 1902, supplies Cartesian classical conditions.

Sections 2.3--2.4, pp. 1902--1904, specify P_(m,n), the fixed groups
G_d, the free local quotients and the chosen isomorphisms to R. Definition
2.18 and the following scalar evaluation use a common pair (d,q), with
q coprime to d; independence of q is stated. Theorem 2.20(2) is a
Fitting-ideal formula for a basis. Remark 2.21 applies to nonnegative
residual core rank, and Corollary 2.22's proof actually selects an index
with vanishing modified residual Selmer group and unit scalar. This is
stronger source evidence than injectivity alone. The next audit must
check these hypotheses in L022 and the supply of an evaluating prime.

Theorem 3.17, p. 1915, identifies the constructed scalar family with
D^0_(m,n) of the modular-symbol system. Proposition 3.19 and its proof,
pp. 1915--1916, explicitly place that family in an inverse limit and
state surjective canonical finite-level maps; residual scalar
nonvanishing is equivalent to basis status at every depth. This does
not state a unit at every index. Section 2.4's choices must be made
compatibly when using that statement in scalar coordinates.

An additional inspected cross-check is Lemma 3.13, pp. 1913--1914,
Lemma 3.14 and Definition 3.15, p. 1914. They describe the derivative
scalar using the norm element, fixed group generators, and discrete
logarithms modulo p^m, and define its tensor with g_d. These give a
primary scalar formula against which to audit a claimed projection;
no new reduction identity is proved here. The relevant proof case in
Lemma 3.13 was read, including its invariant-derivative premise. The
normalization bridge in Lemma 4.2, p. 1917, is a nonvanishing equivalence,
not an equality with an arbitrarily normalized Kurihara number.

Proposition 4.7 and Theorem 4.8 with proof, p. 1919, select a divisor of
the existing index and count primes for residual divisor-minimality.
Their argument uses self-duality; Remark 4.9 warns against the class-group
analogue. They do not assert that proper divisors have zero depth-two
scalar. L021's conditional residual count is the local input to inspect,
not a replacement for the zero finite quotient assumption.

## Approved test and limits

The main gap is rational rank equal to complex order at analytic order
at least two. The intermediate target is a critical audit of conditional
depth-two eligible-index production. Its downstream use is L015's prime
eligibility premise and the lifting route described in L018; neither is
an input to L022. Continue the application if the detection hypotheses,
common-index coefficient map and support-preserving minimization all
check. If a nonunit factor, incompatible normalization or unsupported
hypothesis appears, isolate the exact failing passage and repair or
withdraw only that application, preserving the original evidence.

This approval covers the exact TARGET above. The mathematical audit is
reserved for the next turn; no new lemma, implication or mathematical
script was written. Standard existence and rigidity theorems should be
imported by citation, with only the local applicability/map checks
justifying further proof work. Corank two, residual nonvanishing and
S/S_div=0 remain granted. Rational membership, finite Sha,
complex-to-corank comparison and higher ranks remain unresolved. No
essential source is blocked. Mathlib coverage is not checked and no
absence claim is made. This is local coverage progress, not a result
beyond the inspected literature or a completed correctness review.
