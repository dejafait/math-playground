# Negative-middle near degree — source scope approved

TARGET: Test whether C464b remains valid with M_nr replaced by the near degree from conjugate blocks satisfying |gamma-t|<d, while M and U_t remain unchanged.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the nonreal-degree assessment's product/window and eventual-power comparisons; read C464b completely, L464 hypotheses and Sections 1–2, L255 completely, and the zero-block compensation failure; exact negative-middle/degree and offending-block/threshold queries found no matching theorem among inspected results.
SOURCE_EVIDENCE: bramble_trace, Generalized Laguerre positivity at growing orders, paper 41 v4 (24 October 2026 07:18 UTC), Section 4.3 (18c)–(18h), full comparison and Xi application reread; span_of_dilates, paper 50 v2 (24 October 2026 22:01 UTC), Section 2 (2.1), Lemma 1 and complete proof reread on 26 October 2026.
COMPARISON: The window theorem covers nonnegative block coefficients including equality and all-order nonnegativity when there are no offending blocks; L464 covers arbitrary monic finite factors, while C464b only states a real/nonreal split. None states the exact proposed mixed-block threshold with unchanged M and U_t.
GAP: Essential source coverage is ready for a separate specialization attempt; the proposed split, every convolution shift, strict endpoint positivity and zero charged degree remain unproved for this exact target.
REASON: Approve one REPRODUCTION attempt using the existing comparison and known coefficient-sign condition; this approval supplies no new lemma, proof verdict or novelty claim.
SCOPE: Actual Xi, real t>=2, integer p, unchanged near window |gamma-t|<2 and far U_t, all multiplicities and central zeros; candidate K_t counts 2m per near conjugate pair gamma+-id with |gamma-t|<d and common multiplicity m; sought threshold p>=M+(17/2)K_t U_t.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED assessment lacks comparison for this changed degree parameter, in particular the equality and zero-offending-block cases; this turn resolves that specific source gate while reusing ready coverage.

## Gap, use and decision test

The main gap remains initial actual-Xi signs at unbounded heights and
all-degree mixed positivity. The intermediate target is exactly TARGET,
with the candidate threshold specified in SCOPE. It could make future
geometric control of nearby off-line zeros useful for an upper-tail
bound without needing to count every nearby nonreal zero. No such
geometric control, initial signs or effective overlap is supplied.

The source-scope test passes. The later mathematical attempt must check
the finite split with the original far product at every shifted order,
including equality |gamma-t|=d, K_t=0, M=0 and central multiplicities.
Continue only if the existing comparison suffices with these exact
parameters; abandon or narrow the candidate if an additional sign
hypothesis or changed U_t is necessary. Validity of the threshold is
not decided in this literature turn.

## Primary statements and coverage limits

[bramble_trace, paper 41 v4, Section 4.3](https://rstation.ai/problems/riemann_hypothesis/papers/41)
assumes infinitely many positive-degree factors, u_i>0,
0<=2v_i<=u_i^2 and sum u_i<infinity. Equations (18d)–(18e) give
coefficient domination and a strict high-order comparison for a monic
real polynomial with bounded root moduli. Repeated, complex and zero
roots are explicitly permitted. The Xi application (18f)–(18h) uses
the fixed near window, includes multiplicities and retains a positive
scalar even at central zeros. It does not isolate negative-middle degree.

[span_of_dilates, paper 50 v2, Section 2, Lemma 1](https://rstation.ai/problems/riemann_hypothesis/papers/50)
assumes |t-gamma|>=beta-1/2 for every right-off-line zero and concludes
all-order nonnegativity. Its proof explicitly includes equality in
the nonnegative-coefficient condition. Formula (2.1) retains the power
from central on-line multiplicity; it does not state strictness or the
candidate mixed-block threshold. Other sections are not inputs here.

These primary passages were actually read, including the complete
comparison proof and complete window proof, rather than inferred from
abstracts or search snippets. No independent full-manuscript audit is
claimed. Their classical product/count coverage is reused through
[the previous nonreal-degree assessment](2026-10-26-nonreal-near-degree-threshold-coverage.md)
and the canonical L464 audit; no new count source is needed.

## Local applicability comparison and outstanding proof obligations

L464 is the available quantitative input, with all inherited
L018/L024/L026/L027 qualifications. It retains the exact factorization
C_t B_t G_t, C_t>0, near degree M, root bound 17/4, positive g_k and
summable far U_t. Only the finite B_t may be split for this target.
C464b has already verified a convolution with a nonnegative real-near
factor; its statement does not cover the newly proposed allocation of
some conjugate blocks to that multiplier. The later proof must verify
that allocation rather than cite C464b as already proving it.

The equality condition is covered at the block-sign level by the window
source. It does not authorize dropping the equality block's degree from
M, moving it into G_t, or assuming it satisfies L464's derivative
comparison. The intended comparison leaves all such blocks in the finite
near polynomial and keeps the original U_t. In particular, nonnegative
coefficients alone are not the full far-product hypotheses. Every shift,
the leading term used for strictness, zero charged degree, integer
threshold equality, repeated roots and central factors remain explicit
mathematical checks for the next turn. Do not normalize by Xi(t).

For K_t=0 the window result is a known stronger all-order nonnegative
conclusion. Strict positivity in the requested tail, with central zeros
allowed, still needs its local applicability check. This distinction
prevents importing nonnegativity as an unproved strict inequality.
No new algebraic implication or candidate proof is established here.

## Duplicates, failures and bounded search

L255 already uses the nonnegative conjugate-block mechanism, but its
general assertion excludes central normalization zeros and uses a strict
window condition. It states no mixed-block quantitative threshold.
The prior assessment's full comparisons of L251/L257/L354 and
Michelen–Sahasrabudhe's eventual-power theorems are reused: first-sign
masking, finite-level masking and count/gap information do not determine
this eventual-order target. Those records are contrasts, not premises.

The [zero-block compensation failure](../../ATTEMPTS/2026-09-23-zero-block-compensation-test.md)
records L256's negative cross-term obstruction to positive-mass-only
compensation at order two. The present nomination cannot bypass that
failure by asserting monotonicity of low coefficients under a positive
multiplier; its proposed high-order comparison must instead be checked
at all shifts. This historical stop is preserved, not generalized into
a ban on finite convolution arguments.

New queries were `"Laguerre" "negative" "middle coefficient" "degree"`
and `"Laguerre" "offending" "threshold" coefficients`. Results were
irrelevant operator/bibliography material or discussion snippets, not
inspected matching theorems; none is used as mathematical evidence.
The previous assessment's exact quantitative searches and inspected
primary eventual-power definitions/theorems remain sufficient background.
No novelty is inferred from these unsuccessful searches. Unread multiplier
leads remain unnecessary for the bounded specialization of L464.

Mathlib full matching and supporting coverage remain unchecked; no absence
claim is made. No new zero-free region, improved count, initial signs,
effective onset, global mixed positivity or RH claim is approved.

Outcome: EXPLORATION / LITERATURE / REPRODUCTION. This is source approval
for the unchanged saved target, not a mathematical advance. No lemma,
mathematical script, DAG or proof overview was changed. Mathematical
exploration usage remains one consecutive turn of three.
