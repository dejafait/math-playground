# Low-time H2: finite real-zero contribution and complete remainder

TARGET: Review source coverage for finite-real-zero domination of H2(lambda) on 0<=lambda<=1/20, including a deformed paired product, uniform zero tracking and a complete complex-zero tail, without assuming RH or repeating the stopped moment-box calculation.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step200 reused the step194 cutoff/Hankel comparison and the 6 November reciprocal-Hankel heat assessment; inspected Polymath Proposition3.1 and its complete proof, Theorem1.5, Tao's Jensen theorem/counting proof, and a new compact-propagation lead. Exact queries and limits follow. No matching uniform H2 domination certificate was inspected; no novelty inference is made.
SOURCE_EVIDENCE: Polymath arXiv:1904.12438v2 Section3, Proposition3.1(i)-(ii), (28)-(33), paired product in the proof, Theorem3.2 and Theorem1.5; Tao 246B Notes1 (23 December2020), Theorem2/(3)-(6), Proposition8 and its proof; Planat-Raymond arXiv:2611.06245v1 Lemma7.1/Theorem7.2 and complete proofs; precise links, hypotheses and limits below.
COMPARISON: The deformed paired product permits complex zeros, and Jensen counting can bound all omitted zeros without tracking them. Local zero motion does not supply uniform finite-head enclosures; compact propagation requires a boundary nonvanishing certificate. The known positive-time real/simple tail is not uniform down to zero. No inspected theorem pays a strict H2 matrix margin.
GAP: A uniform explicit complete complex-zero tail bound is a covered quantitative specialization to attempt separately; real-head isolation, multiplicities, boundary control and a strictly larger certified head margin remain independent unpaid obligations.
REASON: Source comparison removes the need to seek a new product theorem or assume RH. It supports a tail-first intermediate test while leaving full domination unresolved. Explicit constants, a closed parameter interval and fixed matrix scaling justify specialization rather than reproof of the general theorems.
LITERATURE_REASON: The changed finite-zero mechanism required the product, uniform tracking and complete remainder comparison missing from step199; this is that one source-only review, not another review of the stopped density or moment-box targets.
SCOPE: Source review only. The proposed quantitative tail subtarget is specified in 2026-11-09-low-time-h2-complete-zero-tail-budget.md and awaits separate supervisor approval. No lemma, mathematical script, tail constant, zero location, positivity sign or new mathematical derivation was produced here.

## Purpose, duplicates and preserved failures

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The larger intermediate goal is strict H2 positivity on
the closed low-time band, excluding d=2 contacts there. A complete
remainder estimate could make a finite real-zero margin usable;
neither that margin nor the head certificate is assumed. Higher
degrees, initialization, global continuation and RH remain open.

Read L019, L058 and L874's definitions/flux statement, the complete
step194 source comparison and step195 failure. L917's independent
moment boxes straddle zero and are exhausted at their fixed budget;
that is not a negative determinant. L918's origin/compact sign is
unpaid. Neither failure is reopened. L058's local continuation and
audited L914's first-block positivity do not prove H2 positivity.
L488's positive-time tail was read narrowly: its conclusion expressly
excludes a uniform limit as the lower time endpoint decreases to zero.
No cross-notebook input or existing certificate was used.

## Primary product and motion input

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant*, Research in the Mathematical Sciences 6 (2019), article31,
[arXiv:1904.12438v2, 4 August2019](https://arxiv.org/html/1904.12438v2#S3).
Inspected Proposition3.1's full simple and repeated-zero proof, including
the paired Hadamard product and final Rouche count. Its H_t is even,
order one and nonzero at zero; complex zeros are allowed, counted with
multiplicity and opposite signs paired. The product converges locally
uniformly. This supplies a product without RH, but no effective uniform
remainder constant for this compact time interval.

Reuse L488's normalization F(lambda,z)=8H_(4lambda)(2z): L019's kernel
is 4Phi(u/2). Source time is [0,1/5] and the spatial cutoff corresponding
to |z|=100 is 200. This is the recorded normalization comparison;
product ratios cancel the scalar. Coefficient extraction, multiplicity
conventions and uniform interchanges remain to justify in research.
No reciprocal-power identity is derived in this review.

Proposition3.1's simple case is local and excludes multiple zeros;
the repeated case retains Hermite splitting, zero-dependent error and
a local Rouche count. Neither gives closed-band separation radii or
numerical zero enclosures. Do not integrate a real-zero ODE while
omitting complex zeros. The earlier Rodgers-Tao comparison remains
adequate: its real/simple contradiction regime is not this premise.

Theorem1.5(i)-(iv) was inspected: 0<t<=1/2, real/simple localization
above exp(C/t), and absolute but unspecified counting constants.
That localization cutoff diverges at zero; neither it nor an unspecified
O(log X) count is a paid numerical remainder on this closed band.
Theorem3.2's strip theorem is a cited input, not reproved here. A strip
alone supplies no zero count or H2 margin.

## Finite-head tracking: conditional coverage, unpaid certificates

The new primary lead is M. Planat and D. J. Raymond, *Certified Collision
Exclusion and an Unconditional Upper Bound Lambda<0.156821 for the
de Bruijn-Newman Constant*,
[arXiv:2611.06245v1, 4 November2026](https://arxiv.org/html/2611.06245v1#S7).
Read Lemma7.1/Theorem7.2 and complete proofs only. The theorem requires
joint holomorphy near a closed time-rectangle, the backwards heat PDE,
real type, no boundary zeros at every time, and all initial interior
zeros real. It concludes interior reality and simplicity at positive
times, allowing initial multiplicities. Its proof retains the compact
complement and backward multiple-root case. L058 supplies the analytic
hypotheses; boundary nonvanishing and a finite initial census remain
unpaid. It supplies no numerical zero brackets or matrix margin.
This is an unreviewed recent lead; the paper's global bound, remaining
sections and computational artifacts were not audited or imported.
Even its announced bound would leave a positive low-time interval.
The known Platt-Trudgian cutoff comparison is not replaced.

Inspected the author textbook [Complex Analysis, Section8.7](https://complexanalysis.org/web/sec_argument-rouche.html),
Corollary8.7.3, Theorem8.7.11 with proof and Corollary8.7.12. The
argument principle and Rouche methods require full-contour strict
comparison, not sampled signs. They are not an accomplished census.
Any unisolated interior zeros require their own paid contribution;
a selected list alone cannot exhaust the head.

## Complete-remainder method and quantitative difference

T. Tao, [246B Notes1, 23 December2020](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/),
Theorem2, (3)-(6), and Proposition8: read statements and full proofs,
including boundary-radius limiting and the nonzero-centre counting
case. Jensen counts all zeros with multiplicity from a function
holomorphic near a closed disk and nonzero at its centre. Proposition8's
proof compares the count to growth on a larger disk; its existential
constant is not the requested explicit budget. L058 supplies entirety,
a nonzero centre and an explicit compact majorant, L019 the actual
super-exponential kernel. Turning these into effective uniform growth
and count bounds is the identified later specialization. Summing the
entire count and bounding the scaled matrix are still work; no such
estimate is derived here. All-zero counts and opposite-pair counts
must be distinguished.

Reuse audited L914's uniform normalizer lower bound only under its
stated L037 contracts. L036/L037 support later finite real enclosures;
they do not already validate a complex-contour implementation. No new
complex arithmetic or trigonometric implementation is certified here.

The proposed subtarget fixes |z|>100 and D=diag(1,200,40000). It asks
for an explicit operator-norm budget and a conditional head threshold,
not proof of that threshold. Its plausible use is comparison with a
later independently certified head. A finite budget alone does not
warrant a head search or prove feasibility. Failure to obtain a complete
effective budget stops this envelope; no radius/scaling/time sweep or
moment-box refinement is part of this first test.

## Search limits and Mathlib

Queries: `de Bruijn Newman Ht finite zeros Hadamard product zeros
complex tail 0.22 Polymath theorem`; `deformed Riemann xi heat flow
zeros local motion finite zeros tail Rodgers Tao product`; `"Hankel"
"finite" "zeros" "heat" "Riemann" positive definite tail`; `"Riemann"
"Jensen" "H_t" zero count uniform Polymath`; targeted primary
Jensen/Rouche searches. Choi's all-real-zero and the fixed-Xi moving
contour results are already compared in step194; that coverage was
reused. Secondary moment/trace abstracts, generic RH claims and
Ki-Kim-Lee references remain unread leads, not theorem coverage.
The guessed 2011 Tao URL failed; the actual 2020 notes were accessible,
so no essential source blocker persists. DLMF1.10 was inspected but
is not a Jensen/Rouche theorem source for this assessment.

Inspected official [Mathlib JensenFormula documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/JensenFormula.html):
AnalyticOnNhd.circleAverage_log_norm and AnalyticOnNhd.sum_divisor_le
are supporting Jensen/counting results. The latter requires a positive
inner radius, larger outer radius, M>=1, analyticity near the closed
outer ball, nonzero centre and the outer-sphere bound. Full theta
heat/product/scaled-tail coverage was not checked. Supporting coverage
is not a formalization of the proposed quantitative result.

One source comparison is complete, without an H2 sign or advance beyond
the inspected sources. The only nominated continuation is the fixed
complete-tail specialization, whose newly written ready assessment
requires separate approval before a mathematical invocation.
