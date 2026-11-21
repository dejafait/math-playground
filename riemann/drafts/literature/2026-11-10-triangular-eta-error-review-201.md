# Triangular common-terminal eta error — component nomination

TARGET: Test whether the full common-terminal-eta error in triangular Li-forcing accumulation is bounded in absolute value by 16 A n^2 for every n>=3, retaining both initial values.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step201's cumulative-forcing comparison searched Li recurrences, triangular/Fejer signed sums and discrete Taylor/summation-by-parts terminology. Reused step192/197 coverage; read L040/L044/L046 and L972/L973 stops. No matching complete aggregate eta-error result was identified; no novelty claim follows.
SOURCE_EVIDENCE: DLMF2.10.9-10 finite summation by parts, web edition accessed 2026-11-10; reused Cauchy/Taylor coverage in L964(9)-(12), L972(4)-(5) and L968(9)-(11), with actual L024/L026 node geometry. Primary real-frequency/Fejer comparisons are recorded in 2026-11-10-signed-cumulative-forcing-review-200.md and are not positive-sign inputs.
COMPARISON: Known finite summation and Cauchy estimates cover the tools, not this terminal-n aggregate. L972 bounds one parameter transition at fixed polynomial index, while this test retains the signed triangular accumulation of the complete difference from ordinary Li forcing at common eta_n. It requests a polynomial budget rather than summable sign-induction loss.
GAP: Verify one explicit absolute O_A(n^2) regularization budget including the exact first two errors. No lower bound on the remaining unregularized cumulative forcing is supplied; that independent central gap remains open.
REASON: A bounded component specialization is justified by the changed downstream tolerance for polynomial losses. This newly written assessment requires separate next-turn source/scope approval; it neither derives nor certifies the proposed estimate.
SCOPE: Only the quantity B_n below for n>=3, actual complex paired nodes, multiplicities and eta_n=1/(64*9^n) common at every inner index. No new convexity, real spectrum, full forcing lower bound, theta-integrand sign or RH claim.

## Exact test and input scope

Fix A>0 with sum_j |beta_j|<=A using L024, and retain L026's
complex-node geometry. Use L972(1)'s definition of Q_u(k), L964(5)'s
a_k and L964(7)'s ordinary Li normalization. For each terminal n>=3
put u=eta_n and define, solely to specify the proposed test,

    E_n(k)=Q_u(k)-lambda_k,             1<=k<=n,
    J_n=(n-1)E_n(2)-(n-2)E_n(1),
    T_n=sum_{k=2}^{n-1}(n-k)
            [E_n(k+1)-2E_n(k)+E_n(k-1)],
    B_n=|J_n|+|T_n|.

The requested threshold is B_n<=16 A n^2 for every n>=3. These
are definitions and a proposed inequality, not a derived Green formula
or a proved bound. Keep the two initial errors exactly in J_n; do not
replace them by positive margins or diagonal Q_{eta_k}(k) values. All
series include all nodes and multiplicities, with algebraic squares.

Start from L964(12)/L968(9)'s complete eta subtraction, independently
of L964's negative-margin hypothesis. The analytic estimates are valid
for each polynomial index k; their constants depend on k. Testing all
k<=n with the common terminal eta_n requires showing that the resulting
complete sums and aggregate bounds are valid, not silently substituting
eta_k or summing an uncontrolled exponential majorant. Import finite
summation by parts from [DLMF2.10.9-10](https://dlmf.nist.gov/2.10.ii).
Its specialization to signed second differences and the subsequent
aggregate estimate remain future mathematical work. A short finite-sum
verification is warranted to check endpoints and exact initialization;
there is no reason to reprove the general summation theorem.

## Relevance and decision test

A proved polynomial regularization budget would allow this error in a
later all-epsilon subexponential lower bound to be paid independently.
L968 supplies the downstream Li implication. The signed unregularized
triangular forcing is still uncontrolled: simply reexpressing lambda_n
or assuming its lower bound would not advance that gap. This test may
pay one component while leaving the principal problem untouched.

Continue only if the stated complete absolute bound is established
without RH, finite-head replacement or omitted initial/eta contributions.
A counterexample or an unavoidable exponential loss at this threshold
is a discriminating negative. If the only output reconstructs Q or Li
without paying B_n, stop without reporting a component advance. Do not
claim an independent central cancellation mechanism from a successful
parameter budget, and do not add a lemma merely for the finite identity.

This is a routine specialization/reproduction, not creative discovery;
after separate approval the appropriate task is calculation, standard/high.
L966/L968 are downstream context; L972/L973 provide conventions and scope
contrasts. Mathematical inputs are L024/L026 and L964's unconditional
identity/analytic bounds plus finite summation by parts. Full matching
Mathlib coverage is unchecked/unknown. No cross-notebook input.
