# Joint endpoint conditioning: saved attempt276

10 November2026. RESEARCH under the pre-existing SPECIALIZE assessment
`literature/2026-11-10-joint-endpoint-polynomial-test-review-275.md`.
Exactly its target is being attempted; no source refresh or new scope.

Main gap: actual-Xi positivity L030-L032/C032a and signed forcing
L966/L968. Intermediate target: an all-index polynomial lower singular
value for the exact three-row J_n. Downstream use would require
independent bounds on all three actual B outputs, still unavailable.
Continue with a rigorous C*n^(-A) bound for some finite A, or an
informative obstruction; finite sampling does not decide this target.

Read L990's exact rows, row scales and recurrence, C990a's full proof,
and review274's completed source comparison. Preserve stops270/272/274
and working271; none supplies or refutes joint conditioning. Reuse the
audited GST/Bessel contracts and finite-dimensional SVD coverage.

## Saved reasoning before completing the proof

Write U=a/||a||_2, V=b/||b||_2, choose s in {+1,-1} minimizing
epsilon=||V-sU||_2, and set lambda=s*||b||_2/||a||_2,
r=b-lambda*a. Then ||r||_2=||b||_2*epsilon. L990's individual
row scales keep lambda away from zero at its exponential scale.

The exact corrected recurrence R(u) dot K(u)=-u gives

    p_n(n)=2-2/lambda-(R(2n) dot r)/(lambda*n),
    p_n(2n)=lambda-1-(R(2n) dot r)/n+n*r_1.

Provisional estimate to verify uniformly: each expression divided by
C990a's corresponding amplitude is O(epsilon+sqrt(n)*exp(-n/2)).
This would yield phase errors O(epsilon+n^-2). Reusing the integer
combinations A=12k+15-4n, B=2l+2-n should then give

    |A^2-27B^2-169/pi^2| <= K*(n*epsilon+1/n).

Its right side must be at least dist(169/pi^2,Z)>0, suggesting
epsilon>=c/n. Check all error products, the antiparallel case,
constant subtractions, and the third row's l1 normalization before
asserting a bound. No small cross product or pivot may be divided out.
If valid, use the exact Gram matrix to pass to sigma_min(J_n).

This draft is unfinished reasoning, not a lemma or verified result.
All arithmetic outputs, interval identification, prime powers, other
zeros, complements and L984(H) transfer remain open. No cross-notebook
input. Full matching Mathlib coverage is unchecked.

## Completion

The saved provisional estimates above have now been proved in
`lemmas/L993-joint-endpoint-polynomial-conditioning.md`. The exact
residual identities give uniform O(epsilon) normalized small values;
the integer error is bounded by K*(n*epsilon+1/n). This establishes
sigma_min(J_n)>=C/n at every sufficiently large integer. No numerical
calculation, asymptotic reproof, or new source was required. The full
argument and its qualifications are canonical in L993; a separate
critical audit remains pending. The original saved reasoning is kept.
