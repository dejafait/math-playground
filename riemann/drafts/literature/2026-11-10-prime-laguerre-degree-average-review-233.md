# Degree averaging of the compensated prime head — completed source comparison

TARGET: Assess first-order Cesàro averaging across Laguerre degree as a mechanism for two-sided subexponential bounds on A_n(X_n), including exact recovery of P_n, common-cutoff tails and known zero-singularity obstructions.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step234 searched exact Li/Cesaro combinations, Laguerre degree sums, inverse Cesaro matrices and analytic Cesaro operators; compared the named local degree-recurrence, lobe-pair and Li-singularity records. No inspected theorem bounds the proposed actual-prime average; queries, inspected statements and unread leads are distinguished below.
SOURCE_EVIDENCE: Ross arXiv2210.08091v1, Prop3.4 p7, Prop4.2/Cor4.3 pp10-11 and proofs; Voros arXiv1403.4558v2, Sections3.1-3.2/(31)-(37), pp10-12 and Section3.4 radius statement; Lagarias AIF57(2007), Thm2.4/(2.20)-(2.23), pp1702-1703 and complete proof. Live DLMF1.15.4-7 and18.18.18 inspected. Exact source scope and a coordinate typo are recorded below.
COMPARISON: Standard Cesaro inversion and holomorphic isomorphism supply recovery tools, not arithmetic cancellation. Known Li radius/growth criteria warn against treating averaging as automatic singularity removal. The actual moving-cutoff specialization and its quantitative losses remain to be proved in a separate mathematical step; no bound for A_n is established.
GAP: Two-sided subexponential control of A_n(X_n) is unpaid. The specific remaining comparison is whether common-cutoff tails plus the cited inverse make that threshold equivalent to the individual-head threshold; no such equivalence is derived here. One-sided bounds, recovery from sampled averages, and an independent signed estimate remain separate.
REASON: Essential coverage is now available without the parked moment sources. Replace speculative automatic smoothing by one bounded cutoff/recovery obstruction test. The separately saved continuation receives approval next turn; this literature turn proves no new result.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and required exact Cesaro inverse/analytic contracts and Li singularity cases outside review231's degree-recurrence scope.
SCOPE: Literature comparison for actual Lambda, integers n>=2, P_k exactly as in L981/L982, X_n=exp(10000*(n+1)^4), A_n(X)=(n-1)^(-1)*sum_(k=2)^n P_k(X) at a common real X. No RH, simple zeros, signs, uniform fixed-index limit or n/X interchange is assumed.

## Original nomination, preserved

The following paragraphs were the uncovered step233 question. Their
pending-source language is historical; the completed comparison below
supersedes it without changing the proposed observable or threshold.

## Proposed mechanism and relevance

The main gap remains L030-L032/C032a and the signed Li forcing of
L966/L968. L981/L982 provide tail and normalization interfaces, while
the head has no n-uniform signed bound. L983's finite positive pair
rejects only a particular spatial-lobe sign proposal.

The prospective intermediate threshold is

    |A_n(X_n)|<=C_epsilon*exp(epsilon*n),
    for every epsilon>0 and all n>=2.

This is a question, not a claimed estimate. The source step should
check whether smoothing in degree supplies controlled cancellation
and permits recovery of the individual P_n with acceptable loss.
It must distinguish a two-sided bound from an upper bound alone,
and keep common cutoffs separate from the moving cutoffs X_n.
No new identity or inference is derived in this nomination.

The plausible downstream use is a full-head subexponential bound,
provided exact recovery and cutoff errors can actually be controlled.
That would still need its precise connection to L966/L968 checked;
this source proposal is not a new equivalence criterion or solution.

## Required comparison and discriminating decision

Search exact Cesàro/Riesz summability and Laguerre degree-sum
terminology for the compensated Li prime expression. Inspect relevant
primary theorem hypotheses, known Li coefficient/generating-function
growth results and essential zero-singularity cases. Reuse existing
source coverage only on its actual scope. In particular review231's
recurrence comparison did not establish a smoothing or recovery bound.
Do not reopen parked kenan/Coffey/original1999 extraction merely for
another route name. No inaccessible source is yet essential.

Continue toward a bounded mathematical attempt only if the comparison
identifies a concrete signed cancellation inequality or test with
loss-controlled recovery, whose premises do not already assume RH.
If the known singularity behavior defeats naive averaging, or recovery
demands the missing individual bound unchanged, record that obstruction
and abandon that precise mechanism. A formal averaging identity alone
is not an advance. No mathematical continuation is preapproved here.

This is a newly written assessment and requires separate approval.
The immediate task is literature_comparison/standard/high. A creative
proof attempt would require a precise new analytic mechanism, a bounded
test and its own ready coverage; none is claimed in step233. Full
matching Mathlib coverage of this proposed observable is unchecked.


## Completed comparison — step234, 10 November 2026

The main gap remains L030-L032/C032a actual-Xi positivity and
L966/L968 signed forcing. The intermediate question is still the
every-epsilon two-sided subexponential bound stated above. Its plausible
downstream use is recoverable individual-head control, provided the
recovery and cutoff losses are proved. No estimate is inferred merely
from the averaging operation.

### Reused notebook evidence and duplicate check

Read L981's exact cutoff definition, all-endpoint tail proof and audit,
and L982's entire fixed-index identification and audit. Read L980's
hypotheses, conclusion and imported arithmetic split, and L968's
ordinary-coefficient criterion and qualification. L981 pays only tails;
L982 fixes the limit convention. Their combination across degrees is
reserved for research. L968's symbol P_n(z) is a different polynomial:
only L981's P_n(X) is used in this assessment.

Reuse review231's completed degree-recurrence comparison and
review223's compensated-head source comparison. The step233 stop
records the actual positive lobe pair in L983; further lobe samples do
not repair its rejected universal sign rule. A narrow search of the
10 November Li/Laguerre literature and failure records located the
Pringsheim comparison review207. Its positive-coefficient correction
concerns another observable, not degree averaging. No cross-notebook
input, new zero-free region or reopening of the arithmetic envelope
routes is proposed. No new matching average theorem was located in
these scoped records; this is not a novelty claim.

### Summability terminology and exact source contracts

[NIST DLMF1.15.4-7](https://dlmf.nist.gov/1.15#i), live version
inspected 10 November2026, defines first-order Cesaro summability by
the convergence of arithmetic means of partial sums, and general
order alpha>-1 by normalized binomial weights. These definitions
do not assert growth bounds for arbitrary means. Here A_n averages
coefficient values; it must not be mistaken for the Cesaro partial
sums of the series having those values as its terms. No convergence
or regularity premise is available for that series.

William T. Ross, *The Cesaro Operator*,
[arXiv2210.08091v1, 14 October2022](https://arxiv.org/pdf/2210.08091v1),
Prop3.4 p7, states invertibility on all complex sequences, with inverse
diagonal 1,2,3,... and subdiagonal -1,-2,-3,... . Its proof solves the
triangular arithmetic-mean equations; no convergence, positivity or
normed-space hypothesis is required. Prop4.2 and Cor4.3, pp10-11,
with the complete injectivity/surjectivity proof, state that

    (Cf)(z)=z^(-1)*integral_0^z f(t)/(1-t) dt,
    (C^(-1)g)(z)=(1-z)*(z*g(z))',

are inverse maps on O(D), D the open unit disk. The coefficient-matrix
identification immediately following Cor4.3 was also inspected.
Only these stated results are imported; their reproof is unnecessary.
An actual-prime application still needs the correct degree indexing,
common versus moving cutoffs and explicit quantitative losses. In
particular holomorphy of a candidate germ is a hypothesis, not an
estimate supplied by the isomorphism.

As a primary algebraic cross-check, inspected H. Roopaei and M. Ilkhan,
*Fractional Cesaro Matrix and its Associated Sequence Space*,
Concr. Oper. **8** (2021), 24-39,
[DOI10.1515/conop-2020-0112](https://doi.org/10.1515/conop-2020-0112),
Section2 definition and Lemmas2.1-2.2 with proofs, pp26-27. The finite
binomial inverse includes order-one arithmetic means. Ross's direct
order-one statement suffices; no fractional-space estimate is needed.
Albanese-Bonet-Ricker2023 was checked as a lead: its Prop3.2 is stated
for t<1, so it is not used to import the endpoint t=1.

### Polynomial sums do not sign the arithmetic measure

The inspected live [DLMF18.18.18](https://dlmf.nist.gov/18.18.E18)
states the finite connection formula

    L_d^(beta)(x)=sum_(j=0)^d
       (beta-alpha)_(d-j)/(d-j)! * L_j^(alpha)(x).

The subscript is the rising factorial and d is a nonnegative integer.
Parameters alpha=1, beta=2 are permitted. This is the relevant known
degree-sum tool, not a prime-sum estimate. The omission of degree zero,
compensation starting at1 and division by n-1 must be retained in any
future specialization. No new averaged kernel, sign or inequality is
derived in this review. Prior DLMF18.5.12/18.9 coverage is reused only
for the existing polynomial definitions and recurrence warning.

### Li singularities: primary theorem hypotheses and essential cases

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
AIF **57**(5) (2007), 1689-1740,
[Thm2.4/(2.20)-(2.23), pp1702-1703](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=15),
gives the equivalence of RH, the every-epsilon lower exponential
bound and absolute subexponential growth for ordinary Li coefficients.
The complete proof was inspected: the one-sided implication imports
Bombieri-Lagarias; the absolute-growth case uses the logarithmic-
derivative germ, disk holomorphy and the functional equation. Reuse
L968's verified trivial-GL(1), multiplicity and normalization
specialization, and L980's cited arithmetic split and smooth trend.
Do not import a bound for S_f or A_n from these criteria.

There is a coordinate-description typo on p1703: the displayed map
-z/(1-z) has basepoint0, whereas the following sentence says basepoint1
and describes the right half-plane. Do not copy that sentence as an
applicability argument. The zeta specialization can instead use the
source's (1.5), conjugation symmetry, and the correct map in Voros
below. This flags a source-text issue, not a correction to a local lemma.
No stopped Section6 contour estimate or alternating (4.13) is used.

Andre Voros, *Zeta functions over zeros of Zeta functions and an
exponential-asymptotic view of the Riemann Hypothesis*,
[arXiv1403.4558v2, 26 July2014](https://arxiv.org/pdf/1403.4558v2),
Sections3.1-3.2/(31)-(37), pp10-12, and opening Section3.4, p12,
were inspected. Equation(32) uses the ordinary Li convention:

    log Xi(1/(1-z))=sum_(n>=1) (lambda_n/n)*z^n.

This is the completed function in the s variable, not the notebook's
real-height Xi(t). Section3.4 explicitly states radius1 under RH and
strictly smaller radius otherwise. Section3.2 treats competing real
and off-line saddle contributions; (36) describes exponential
oscillation in the false-RH case, while (37) gives the conditional
smooth trend. Those asymptotics concern the original Li sequence,
not this prime average. Their detailed infinite-saddle expansion is
not needed or imported. Use the radius statement and Lagarias's
criterion as the precise warning; do not claim an all-index lower
bound on oscillatory magnitudes or simple zeros.

The literature therefore supplies a concrete singularity/recovery
comparison, but no independent signed inequality for A_n. Whether
the actual common-cutoff average has the same subexponential threshold
is a specialization to test, not an established result of this turn.

### Search record, access limits and decision

Queries actually executed included `Li coefficients generating function
exponential growth Riemann hypothesis Voros Cesaro`, `Laguerre polynomials
Cesaro summation partial sums identity L n alpha DLMF`, `"Li coefficients"
"Cesaro"`, `"Li coefficients" "Cesàro"`, `"Keiper" "Cesaro" averaging`,
`Cesaro operator power series integral "radius" "convergence"`,
`Cesaro matrix inverse "n" "n-1" arithmetic means`, `Hardy divergent
series Cesaro means inverse sequence arithmetic means`,
`"Cesaro operator" "inverse" "holomorphic" derivative`, and
`"Cesaro matrix" "inverse" pdf`. Follow-up searches identified Ross
and Albanese-Bonet-Ricker by exact title. Search snippets are leads,
not theorem evidence. The inspected primary passages are specified above.

Hardy's *Divergent Series* PDF was rejected by the web fetcher as too
large; one shell retrieval failed DNS. Its chapter proof is UNREAD.
It is not essential: Ross's accessible exact inverse and full proof
supply the required contract. Stop that access path here. A DLMF TeX
endpoint was unsupported; the complete rendered equation was read.
The exact-Li searches also returned an unrelated generalized-Cesaro
root-identity lead, Laguerre-expansion divergence papers and recent
Cesaro spectral papers. Their theorem statements were not inspected
or imported; none supplies evidence about this actual prime observable.
The parked kenan/Coffey/original1999 sources were not reopened.

Decision: source coverage is sufficient for one routine specialization
of the cited inverse and existing tails. Save the exact target in
review234. Continue only if that test exhibits genuine loss-controlled
recovery and identifies what independent arithmetic input would still
be needed. If it simply preserves the original threshold, stop the
claim that first-order averaging automatically regularizes the problem;
do not infer a ban on all averaging methods or a proof of RH.
No mathematical exploration turn is spent here. No signed cancellation
inequality has emerged, so a creative proof nomination is unjustified.
Full matching Mathlib coverage is unchecked and unknown.
