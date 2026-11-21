# Prescribed regularization and negative Li detection — source comparison

TARGET: Determine whether nonnegativity of L966's Q_eta(n) for every n>=1 at eta(n)=1/(64*9^n) implies RH, by testing L964's regularization error against a precisely sourced off-RH negative-Li subsequence.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step171 searched prescribed/regularized Li signs, negative Li subsequences and one-sided tempered growth; compared scoped step158/159/164/167 assessments and step158/168 stops. No inspected exact Q_eta theorem was found; bounded coverage does not establish novelty.
SOURCE_EVIDENCE: Lagarias AIF57(5)(2007), Theorem2.4(2)/(2.21), pp.1702-1703, normalization pp.1690,1697; cross-checked arXiv:math/0404394v4 Theorem2.2(2)/(2.39). Voros arXiv:math/0506326v2, Section1/(1)-(3) and Section3 RH-false case/(14), pp.2,4-5. L964(7),(9)-(13) and L966(1),(12),(16) inspected; prior analytic-tool coverage reused.
COMPARISON: The primary one-sided Li growth criterion supplies sign-sensitive coverage without an effective negative index or a new oscillation proof. The exact prescribed-eta error comparison remains a local specialization, not a cited result.
GAP: Verify that L964's pre-margin error applies for the prescribed eta at every index, compare its full n-dependence with the sourced criterion, and justify all quantifiers without assuming an actual negative coefficient or the all-n theta inequality.
REASON: Essential coverage now supports one bounded specialization of the unchanged target after separate approval. This literature turn does not prove the eta implication, simplify its error into a uniform bound, or reopen the retired payment profile.
SCOPE: Actual Xi, ordinary Li normalization, integer n>=1, eta(n)=1/(64*9^n), L964's a_n and all paired nodes with multiplicity. Only the detection implication and complete-sum/error checks; no new theta-sign mechanism, zero-free estimate or effective D(T,delta).

## Completed source comparison — step171

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. This intermediate target asks whether prescribed signs,
if established, would detect failure of RH. It does not establish
those signs; L966(16) remains unpaid.

### Precise primary input and applicability

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier 57(5) (2007), 1689-1740,
[Theorem 2.4(2), (2.21), pp.1702-1703](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=15),
equates RH for its completed L-function with

    for every epsilon>0 there exists C(epsilon)>0 such that
    Re(lambda_n)>=-C(epsilon)*exp(epsilon*n) for every n>=1.

The stated hypotheses are an irreducible cuspidal unitary automorphic
representation. Its trivial GL(1) case has completion 2*xi (p.1697).
Definitions (1.1)-(1.3), p.1690, use ordinary Li coefficients, retaining
multiplicity and star convergence. These agree with L964's existing
normalization, rather than Keiper coefficients divided by n.

The same statement and proof were read in
[arXiv:math/0404394v4](https://arxiv.org/html/math/0404394v4),
4 May 2005, Theorem 2.2(2)/(2.39). The proof explicitly imports
Bombieri-Lagarias, Theorem 1's corollary, for this one-sided criterion.
The published numbering above is canonical. No reproof is needed.

This is lower-side information, unlike an absolute-value exponential
limsup. A future attempt may use the criterion directly or its logical
contrapositive; an effective first negative index is unnecessary for
the present non-effective sufficiency question.

A. Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*,
[arXiv:math/0506326v2](https://arxiv.org/html/math/0506326v2),
25 January 2006 (PDF internal date: 25 September 2018), Section1/(1)-(3),
p.2, and Section3, RH-false case/(14), pp.4-5, were inspected in PDF
and HTML. The latter asserts exponentially large values of both signs,
retaining multiplicities and permitting infinitely many off-line zeros.
It distinguishes heuristic saddle analysis from a claimed rigorous
Darboux justification. It gives no effective first negative index.
Neither its saddle estimate nor its infinite asymptotic expression
is needed or imported here; do not interpret that expression as an
absolutely convergent zero sum at fixed n. The precise one-sided
criterion is the selected source input for the later comparison.

The original Bombieri-Lagarias paper, *Complements to Li's criterion
for the Riemann hypothesis*, JNT77(1999),274-287, was located at its
[author-copy PDF](https://websites.umich.edu/~lagarias/doc/bombieri.pdf).
Open-page text was garbled; search-index passages located its
maximal-modulus proof but are not treated as inspected proof evidence.
Screenshot calls returned text placeholders without visible images;
shell retrieval failed DNS. No complete direct reading is claimed.
This is nonessential: the accessible primary criterion above supplies
the needed precise theorem in the same zeta normalization.

### Existing error and exact remaining specialization

L964(9)-(13), before its final supplied-margin inequality, records

    Q_eta(n)-lambda_n <= eta*C_n*A,
    C_n=8*(3^n)^2,   A>=sum_j |beta_j|.

This is an existing estimate, not a result derived in this review.
Its proof uses Re(beta)>0, |beta|<1/16 and the complete summable
node mass, retaining the favorable real part of the n^2 term.
The final epsilon/8 bound uses its margin-dependent eta; it cannot
simply be copied for a different eta. The preceding inequality
instead needs checking under its own proof hypotheses. L966(1) sets

    eta_n=1/(64*9^n),
    Q_eta(n)=sum_j beta_j^2*a_n(beta_j)^2/(beta_j+eta_n).

Comparing these expressions with the sourced criterion is the future
test. No cancellation of n-dependence, uniform error, lower bound or
eta implication is established in this literature-only turn.

Use a single finite A independent of n, supplied existentially by
L024. The target needs no effective numerical A. Verify the admissible
eta range and analytic bounds, both separated absolute sums in
L964(12), conjugation reality and the direction of the one-sided
comparison. Preserve every-epsilon and every-index quantifiers in
the criterion. A fixed arbitrary exponential rate or an unsigned
growth assertion would not meet that requirement. If a negative-
subsequence formulation is used, explicitly justify its quantifiers
from the cited criterion rather than inventing an effective onset.

### Local duplicates, stops and bounded decision

Reused the ready identity/tool coverage in
`2026-11-10-li-negative-margin-mixed-transfer-review-158.md`
and representation coverage in
`2026-11-10-regularized-li-theta-representation-review-163.md`.
The finite-index comparison
`2026-11-10-height-deviation-witness-degree-review-157.md`
and its step158 stop concern effective windows, degree conversion
and unresolved printed constants. None of those constants is needed
here. Scoped searches found no completed local prescribed-eta
detection proof; this does not establish originality.

Read the step168 profile stop and step170 audit history. L967
excludes one pointwise payment rule, not this observable comparison.
Successful detection would neither repair that rule nor prove
R_n<=N_n. L964's polynomial construction is also distinct: the new
target neither chooses a margin-dependent eta nor requires a
polynomial truncation or mixed-degree bound. Prior stops remain intact.

Continue only if the complete pre-margin estimate applies to the
prescribed family and provides lower-side control meeting the cited
criterion, or a controlled sign-sensitive subsequence comparison.
Abandon this use of the estimate if it needs unknown n-dependent
mass, a discarded term or inadequate growth control. A success
would specialize a known criterion, not discover a Li theorem.

Essential local inputs are L964/L966 and L018/L024/L026 for actual
nodes and multiplicities; L030 explains downstream relevance. L967
is stop evidence only. All-n L966(16), actual signs and the main gap
remain open. Full matching Mathlib coverage is unchecked and unknown;
no Mathlib theorem or cross-notebook input is imported. No lemma,
mathematical script, DAG edge or PROOF argument changed. This newly
ready assessment receives separate next-turn approval; no mathematical
attempt is invoked here.

Queries included `Li coefficients if Riemann hypothesis false
exponentially growing oscillations Lagarias Theorem negative subsequence`,
`Li coefficients lambda n negative infinitely often exponential Bombieri
Lagarias Voros`, `Li regularized criterion eta coefficients positivity`,
`Li coefficients bounded below Bombieri Lagarias constant`, and exact
title/author-copy searches. Secondary summaries and unrelated hits
were not imported. No further retrieval of the blocked copy is needed.

## Original nomination — step170, retained as history

## Relevance and bounded next review

The main gap remains L030-L032/C032a actual-Xi mixed positivity.
Even if the still-open L966(16) were proved for every n, its restriction
to the prescribed eta(n) is not currently connected to L964's
margin-dependent negative-Li detector. The proposed intermediate
target tests that separate connection. Success could make an all-n
L966 inequality sufficient for RH; it would not prove that inequality.
Failure or inadequate source hypotheses would identify a genuine
limitation of the prescribed sequence without reopening L967's profile.

In the next literature-only turn, first inspect L964's canonical
statement and error estimate and compare the narrow local Li/theta
assessments and failure records. Reuse any adequate prior source
coverage. Then retrieve primary statements and essential proof cases
for relevant Li sign/oscillation results under failure of RH, if needed.
In particular, check whether any negative-subsequence assertion is
quantitative enough, in the same normalization, to pay the exact
regularization error. An abstract or informal assertion that signs
oscillate does not establish that comparison. No source is claimed
to supply such a theorem in this nomination.

The prospective bounded test is to obtain a sourced negative-margin
scale and an available uniform error scale for the same indices and
quantifiers. Continue to a separately approved mathematical attempt
only if their comparison is justified or a concrete remaining
comparison is adequately assessed. Otherwise record the precise
shortfall and park that proposed implication. Do not derive or approve
the new comparison during the source review. Do not repeat the
normalized-profile transfer, infer any integral sign from its negative
region, or undertake a new zero-free-region estimate.

Essential prospective inputs are L964 and L966; L024/L026 provide
their actual-node/multiplicity framework and L030 the Li/mixed-sign
connection. L967 is route-stop evidence, not a premise of a future
detection theorem. The exact quantitative negative-subsequence input,
uniform error bound, sufficient index range, all-n inequality and eta
implication remain unresolved here. No cross-notebook input is proposed.
Full matching Mathlib coverage is unknown. This file nominates a target;
it is not ready coverage or a mathematical result.
