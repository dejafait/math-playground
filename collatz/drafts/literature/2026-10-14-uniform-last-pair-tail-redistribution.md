# Uniform last-pair tail redistribution — proposed target

TARGET: Classify the lower-domain and J-guard feasibility of L055's literal-order cyclic endpoints with a_23=2+18t, a_24=166504412-18t and all other tails 2, for every integer 0<=t<=9250245.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Two focused prescribed-parity/redistributed-even-step searches; narrow duplicate and failure check of L051/L055/L064, the single-tail assessment, histories 187/189/209 and Attempts 026–031; no inspected result supplies the full parameter classification.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemmas 1/2 pp. 228–229 and Lemma 4 with its exchange proof p. 230; rechecked NIST DLMF 4.6.4 version 1.2.8 and L055's exact logarithm remainder method; reused prior global-minimum scope comparison.
COMPARISON: Prescribed-word affine composition covers each word in the finite parameter family; scalar numerator ordering does not decide all own-input guards. L055 and L064 supply only t=0 and t=1 evidence, not uniform growth, minimum location or guard thresholds.
GAP: Specialize the existing exact endpoint construction to parameter-dependent tails and certify the entire lower domain and own-input J-guard classification; no parameter dependence or new guard verdict is established in this review.
REASON: Essential sources are accessible and sufficient for a separate bounded RESEARCH/REPRODUCTION attempt at this exact target; import general affine machinery and justify only the changed parameter comparisons.

The main gap remains universal eventual descent. The intermediate target
would replace further isolated tail tests with one uniform necessary-guard
classification along this explicitly fixed family. A rejection could
remove part of that family from possible actual cycles; a survivor would
mark the limit of the J-only filter. Either outcome still leaves other
allocations, permutations, integer realization, entry and divergence open.

Keep every indexed J_i,H_i of L055 in its literal order. For each integer
t in the stated interval, impose all 25 exact endpoints of L051 (4),
including s_25=s_0, and test all s_i>=540/11 and
4J_i log2<=log s_i+log(11/4) at their own outgoing inputs.
Do not assume the literal cut is the minimum or transfer L064/L067's
prefix growth estimates to this whole interval. No H guard, seed,
integrality, parity, valuation realization or primitive condition belongs
to this proposed subsystem. Essential starting inputs are L051's formulas,
L055's complete table/counts and t=0 evidence, and L064's t=1 evidence.
C067b provides the downstream fixed-allocation precedent, not a theorem
about any t>=2. Full matching Mathlib coverage is unchecked.

The separate source comparison should reuse adequate affine/logarithm
coverage from `2026-10-12-single-tail-redistribution-j-guards.md`, checking
its precise scope against the uniform target. The cited primary source
is Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[primary PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its formal fixed-point machinery is a lead for the parameter dependence;
no theorem-level comparison of uniform guard thresholds has been made.
The ready fixed-tail assessments are not automatically extended here.

The later mathematical test, only after coverage approval, should either
certify all passing parameter values with every domain/guard condition,
or identify an explicit violated domain/guard for each rejected value.
An exact uniform argument or rigorous interval partition would be useful;
isolated samples or a straddling enclosure would be inconclusive. Stop
the bounded attempt with the precise unclassified interval or failed
uniform comparison if a complete classification is not justified.
Do not expand to other row pairs or orders in that attempt. Attempts
027–031 retain their old-allocation stops; their prime cancellations
are neither inputs nor obstructions to this independent guard question.

The original proposal supplied a future target only. No cyclic-root dependence,
monotonicity, new guard verdict, script or additional theorem has been
derived during C067b's audit. Next turn is literature-only for this
then-REVIEW_REQUIRED scope. The separate review below completes coverage.

## Separate source comparison — 2026-10-14

LITERATURE_REASON: Essential coverage for the saved uniform parameter interval was incomplete; fixed t=0,1 approvals do not cover changed prefix growth or all indexed guard comparisons.
SCOPE: Exactly the TARGET and its stated necessary subsystem; literal J,H order, the two parameterized tails, all 25 endpoints and all own-input J guards. No permutations, H guards, seed or integer realization.

### Inspected primary inputs

The published 1997 paper was read at pp. 228–230, including the
odd-denominator parity argument, length-one and last-zero induction
cases, the stated analogous last-one case, and the finite exchange proof.
Lemma 2 gives affine composition and the fixed-point formula for a
prescribed binary word. Import only that formal identity for a nonempty
word with nonzero denominator. Lemma 4 requires equal length/one count
and domination at every prefix; it orders scalar numerators, rather than
all designated junction guards. Reuse the existing Lemma 5/Corollary 1
comparison concerning minima over all parity-phase rotations.

For applicability, the unchanged table and total tail budget retain
the same N,K; the allowed integer interval keeps both tails at least 2
and congruent to 2 modulo 18. L055's count-dependent positive Lambda
enclosure is therefore reusable to check the nonzero denominator.
L051 (4) provides the coordinate specialization template. These are
source-hypothesis checks, not a derivation of uniform root dependence,
ordering, domain or feasibility. No general parity-coding reproof is
needed; changed endpoint and guard comparisons are the remaining work.

[NIST DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), version 1.2.8,
release 2026-09-15, states the odd-power logarithm expansion for
Re(z)>=0, z!=0. Positive real arguments satisfy its domain.
L055's proof gives the exact integrated remainder, binary reduction,
outward term rounding and large-cancellation error accounting. Reuse
that certification method; it does not certify any new parameter value.
No full matching Mathlib coverage was checked, and absence is not claimed.

### Discovery, overlap and failures

Queries actually run:

- `Collatz rational cycle prescribed parity sequence redistribution even steps cyclic fixed point Halbeisen Hungerbuhler`
- `Collatz cycle tail exponents parameter affine fixed point guard inequalities`

The primary paper and its publisher record were returned. Other hits
included *Collatz Cycles and 3n+c Cycles* (arXiv:2101.04067), general
repositories, informal discussions and speculative preprints. These
are unread leads, not theorem evidence or essential dependencies.
The finite search establishes neither novelty nor absence of a stronger
result. No essential source is blocked. Reuse the single-tail assessment's
Simons–de Weger comparison: integer-orbit/global-minimum hypotheses do
not supply a theorem about arbitrary real designated junctions.

L055 already settles t=0 and L064's j=23 case settles t=1.
The narrow search found only the current proposal for the whole interval.
L064's first-24 multiplier bound assumes tails at most 20. L063/L067
rigidity concerns intact fixed triples. None can be transferred to
unrestricted t. C067b is a downstream fixed-allocation precedent only.
Attempt 026 stops exclusion of the unchanged full real branch;
Attempts 027–030 stop specific prime diagnostics; Attempt 031 rejects
one permuted tuple. Their evidence remains valid, but none bans or
answers this independent literal-order uniform guard question.

### Approved bounded continuation

SPECIALIZE now approves precisely TARGET for a later mathematical turn,
classified REPRODUCTION. Essential inputs are L051's endpoint and J
formulas, L055's complete table/counts, affine construction and positive
Lambda enclosure, and L064's t=1 evidence. Use known affine composition
by citation; establish parameter dependence and every required comparison
locally. Do not assume monotonicity, prefix growth or the minimum's location.
Include closure, every domain inequality and each outgoing row's own input.

The continuation test is a complete exact classification, or a rigorous
interval partition covering all permitted integers with a named violated
domain/guard for each rejected part and all guards for each passing part.
If a uniform comparison fails, record the precise unclassified interval
or boundary and stop this attempt; isolated samples are insufficient.
No wider row-pair/order search is approved. Survivors leave H/seed,
integrality, parity, exact valuations, primitive realization, other
allocations and universal eventual descent unresolved.

This completes LITERATURE/NOVELTY_UNCHECKED with outcome EXPLORATION.
No new mathematical result, script, parameter verdict or lemma was derived.
Mathematical exploration usage is unchanged. The approved target is the
saved target reviewed in this turn, not a newly proposed continuation.
