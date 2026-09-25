# Constrained exceptional-prime lifts — 2026-09-25

This records one focused test of the surviving repeated-cube factor system. It is not a candidate resolution of Beal.

## Starting state and relevance

The shared rules and prompt, local goal and checkpoint, whole overview, local DAG, existing changes, and relevant proofs and failed approaches were read. Existing work is preserved. Mauldin's [primary statement](https://sites.math.unt.edu/~mauldin/beal.html) again agrees with the positive-integer target; the nominated AMS page again returned HTTP 403. The existing source qualification remains applicable.

The addressed gap is emptiness of the constrained system II at primes p >= 19 congruent to 1 modulo 3. The intermediate target is to decide whether its equation and the restrictions from L005 admit nonzero primitive solutions over both Z_2 and Z_3, with compatible lifts to all precisions. An obstruction could support a constrained congruence exclusion; compatible lifts would stop this particular exceptional-prime mechanism. A global integer exclusion for this system, smaller exponents, and other residual signatures would remain unresolved.

The discriminating test uses the full discriminant equation, not just the isolated quadratic factor. For fixed odd u and v congruent to 1 modulo 12, put

\[
K=3^{2p-3},\quad s=3^{p-1}u^p,\quad
\Delta=4v^p-Ku^{2p}.
\]

Determine whether d^2=Delta has compatible roots at 2 and 3 and whether a=(s+d)/2, b=(s-d)/2, c=3uv satisfy local primitivity and the exact required valuations. A finite-precision survivor alone is not a completed test.

## Redundancy and initial reasoning saved

L001 and Attempt 001 cover unrestricted local solutions; their witnesses need not satisfy L005. L003 supplies the exact factor identity and reconstruction, and Attempt 002 shows why a single-factor test is insufficient. L005 supplies new global necessary restrictions but does not test their local sufficiency. No previous artifact supplies these constrained compatible lifts.

Initial calculations give Delta congruent to 1 modulo 8 and modulo 3. The derivative of d^2-Delta is not a unit at 2, so a simple-root invocation there would be invalid. A direct compatible binary-digit construction is needed. At 3 the roots reducing to +1 or -1 are simple. The identity

\[
s^2-\Delta=4(Ku^{2p}-v^p)
\]

suggests valuation exactly three at 2 because the parenthesis is 2 modulo 4. At this saved checkpoint the calculations were a lead, with the complete proof and scope assessment still pending. Real positivity and a single ordinary integer square are separate from local lifting.

## Completed assessment

[L006](../lemmas/L006-constrained-exceptional-prime-solubility.md) supplies the complete compatible binary and ternary digit constructions. At 2 the induction keeps a square congruence one power stronger than the root's compatibility precision, avoiding the nonunit derivative problem. Reconstruction gives v_2(ab)=1 and v_2(s^2-d^2)=3 exactly. At 3 the reconstructed cube bases and d are units, with v_3(c)=1+v_3(u); 3 dividing u is still allowed.

The auxiliary real-feasibility issue does not restore an obstruction: v=13^(2k) and a suitable u congruent to 1 modulo 26 provide infinitely many coprime parameter pairs with the required prime support and 0<Delta<s^2. Each pair has real, 2-adic, and 3-adic points, with no identification of their d coordinates. The explicit p=19,u=5,v=181 control satisfies the same side conditions but has a nonsquare integer discriminant.

The required local threshold was zero compatible primitive classes. The achieved result is at least one at each exceptional prime for every parameter pair under the congruence hypotheses, with simultaneous finite congruences by the Chinese remainder theorem. Hence increasing only these prime-power precisions cannot exclude the branch under the tested restrictions. This does not assert local solvability at other primes or an integer solution. The bounds remain relative size intervals, not upper height bounds.

The [exact-arithmetic output](../scripts/constrained-local-lifts/results.json) records 352 coprime parameter tests, including 224 with 3 dividing u, through equation precisions 2^64 and 3^40 and their product. It checks the exact valuations, local primitivity, both lifting recurrences, and the real-feasible nonsquare control. Reproduce with `python3 scripts/constrained-local-lifts/check_lifts.py`. These checks support the implementation of the general proof, not a numerical inference of that proof.

Outcome: NEGATIVE, because the new evidence stops the constrained exceptional-prime exclusion route. Exploration turns used without an advance or informative negative result: 0/3. A global factorization of the simultaneous power conditions is a materially different direction: L003 only allocated rational integer factors, and Attempt 002 rejected only a single-factor shortcut. The sole current action is recorded in PROGRESS.md. No complete candidate appeared.
