# Primitive-remainder source comparison2090

Literature-only review of assessment2089's unchanged TARGET. No estimate
is proved, no numerical test is run, and no canonical theorem is imported.
The purpose is to make the finite-scale reproduction independently
checkable before any energy assembly. The main gap remains actual-Xi
all-degree algebraic mixed positivity, L030-L032/C032a.

## Primary source and actual reading

Leonard van Hemert, *Exact Zero Detection and Compact Arithmetic
Realizations for the Riemann Xi Function*, v1.0.0, 11 October 2026,
DOI10.5281/zenodo.23295277,
[tagged primary TeX](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex).
Read `thm:log-primitive-remainder`, its complete proof, GC12-GC18,
lines11613-11717. Correct the earlier coverage locator: line11702
does not include the whole proof or GC18. Also read the preceding
gamma theorem/setup and proof, GC1-GC11, lines11382-11612; reuse
source-notes2080 and C034r for the fixed-band setup and actual kernel.
These are inspected manuscript assertions, not certifications.

The theorem concerns the **unprojected** source norm. Its sector uses
coprime reduced indices with maximum at most the primitive cutoff.
GC16 has a strict lower and inclusive upper divisor endpoint. GC17
states a squarefree coprime count for every positive real argument.
GC13 claims the saved error uniformly over inputs in E. GC18 additionally
uses GC6 and the GC14 cutoff/input growth conditions. It retains a
signed complementary sector and the completed gamma boundary cross term.
None of these statements supplies a primitive-sector upper bound.

The section's gamma setup starts at X>=q, whereas FB1 defines the
source for X>=1. The future audit must explicitly treat 1<=X<2
for the saved target; this review establishes no small-X extension.
The primitive cutoff in these paragraphs is K (the source calls it H),
not C034r's Fourier band. A projected arithmetic identity would need
its own correlation and is outside this approval.

## Named elementary arithmetic input

Giuseppe Molteni, *Analytic Number Theory*, Spring2026, revision9.0,
[author lecture notes](https://sites.unimi.it/molteni/didattica/matematica/analytic_number_theory/appunti-AnNTh.pdf),
Proposition3.2 (Eratosthenes-Legendre), printed pp68-69, PDF pp74-75.
Read the interval-count definition, statement and entire floor-sum proof.
For squarefree positive P the count of integers in (x,x+y] coprime
to P is (phi(P)/P)y+O(2^omega(P)). The proof keeps both floor
endpoints and an absolute error per squarefree divisor of P; it does
not require the error to be smaller than the main term.

This is a direct standard reference for the inner coprime count,
not for the full weighted two-index remainder. A future use with
general M must state the radical specialization, and square-divisor
expansion must retain the restriction on the square divisor. No such
specialization or new squarefree estimate is derived in this turn.

## GC18's additional analytic premise

Ethan Simpson Lee and Nicol Leong, *New explicit bounds for Mertens
function and the reciprocal of the Riemann zeta function*,
[arXiv2208.06141v5](https://arxiv.org/html/2208.06141v5),
9 September2026, Theorem2.2, equations(18)-(23), Table1 and its
row-matching qualification. Read the complete theorem, c3 in(20),
the admissible third table block, and(23). For fixed tabulated W
and its corresponding R3 and x3(W), (23) is the unconditional
Mertens estimate for x>=x3(W); its exponential scale is
(log x)^(3/5)(loglog x)^(-1/5), with the displayed prefactor.
For example, the row W=54 has R3=5223 and recorded
loglog x3(W)=10.01. Do not mix blocks or interpret rounded table
thresholds as an independently verified numerical certificate.
No proof or computational certificate of that paper was replayed.

Van Hemert explicitly cites this theorem at lines11570-11587 for
GC6. The future audit may cite Theorem2.2 as a named external input
with fixed admissible parameters; it must check its subsequent
constant reduction, threshold and vector Abel application if claiming
GC6. Merely reading that theorem does not certify GC5, the selected
integer gamma cap, or GC6. For GC18, distinguish the exact source
sector split plus the GC13 remainder from the separate gamma-energy
transfer. If the latter is not verified, write GC18 conditionally on
it; no unconditional completed-head or cumulative conclusion follows.
This permits the independently useful finite-scale remainder audit
without hiding an independent analytic gap.

## Bounded audit coverage and pass/fail criteria

The following are obligations for the next mathematical turn, not
results of this review:

| Case to check | Inspected source coverage | Required audit evidence |
| --- | --- | --- |
| Actual square and gcd grouping | GC15-GC16; C034r/C034s definitions | Check the translation factors, conjugation convention and coefficient outside the divisor sum; distinguish the full norm from a projection. |
| Squarefree coprime count | GC17 and its full square-divisor argument; Molteni Proposition3.2 | Retain coprimality of the square divisor, the exact Euler constant, uniform dependence on ab, and the real-argument case below one. |
| Nonempty/empty divisor interval | GC16 and proof immediately after GC17 | Write strict/inclusive endpoint conventions; treat an empty interval and its corresponding zero main weight without reversing an integral. |
| Stieltjes replacement | Source lines11681-11687 | Pay both endpoint discrepancy terms and the derivative integral with constants independent of a,b,K,X. |
| Summation over primitive slots | Source lines11688-11703 | Verify the support restriction before the block bound, the geometric sum, and its initial singleton; include K=1 and K near X. |
| Full saved X-range | FB1 and the gamma setup's X>=q qualification | Justify the bounded interval 1<=X<2 separately or report a restricted conclusion. |
| Energy interface | GC6, GC14, GC18; Lee-Leong Theorem2.2(23) | State the selected cap and input-family hypotheses when used; otherwise keep the gamma-energy error as an unproved conditional premise. No cumulative-energy claim. |

Continue if the audit establishes the saved finite-scale error with
one constant depending only on q=2 (and the stated factor C_h(0)),
with every listed endpoint and no primitive sign premise. A failure
must identify an exact inequality or hypothesis, record any surviving
restricted identity, and park only that failed specialization. Control
of this error alone is neither control of either signed sector nor RH.

## Duplicate/failure comparison and search boundaries

Reused source-notes2080's signed lcm/GCD/spectral comparisons; their
kernels and normalizations do not match this remainder. Read the exact
interface paragraphs of source-notes2082 and stop2089. C034s fixes the
kernel, not GC13; C034t's analytic-boundary/complement stop is not a
counterexample to the finite-scale claim. C034t is not a premise here.
Targeted searches in the November21 literature, histories and attempts,
and C034 lemma files found references to GC17 but no canonical local
remainder audit. This bounded duplicate check establishes no novelty
or claim about all earlier notebooks. No cross-notebook input.

Queries: `"log-primitive-remainder" "GC13"`;
`"squarefree" "coprime" "2^{\\omega" "sqrt"`;
`"squarefree" "coprime" "sqrt x" count`.
The first yielded no usable independent theorem. The arithmetic
search located Molteni's primary notes. Other snippets and forum
results are leads only and support no theorem import. Source access
worked; no blocked campaign was repeated.

Decision SPECIALIZE: the main finite-scale assertion is already
stated with a proof in the manuscript. Reproduction is justified by
its unaudited status, compressed endpoint estimates, the precise
fixed-input interface and the small-X qualification. It is not new
mathematics beyond those sources. The next audit is ready for this
scope; no creative mechanism or original upper bound is approved.
Full matching Mathlib coverage is unchecked; no inference of absence.
Literature work spends no mathematical exploration turn and resets
no counter. PROOF.md, DAG.md, lemmas/ and scripts/ are unchanged.
