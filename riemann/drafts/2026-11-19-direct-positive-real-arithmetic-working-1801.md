# Direct positive-real arithmetic preflight1801

One RESEARCH development attempt under unchanged ready SPECIALIZE1799;
the target remains the eight-scalar radius2^-8/full10^6-term preflight.
Main gap: L030-L032/C032a actual-Xi positivity. Possible use is C033w's
fixed-three-width interpolation; conditioning, TV, the full observation
interval, cancellation, signed height and realization remain unresolved.
No transform or callback has been evaluated. Preserve all prior work.

Reuse C033y analytic allowances and source-notes1799. C033u's enlarged
formula and C033m/C032w's elementary evaluator are the local inputs;
C033x and stops1781/1782 concern other evaluators. Initial notebook-only
git status was overlarge; no truncated listing is mathematical evidence.
No sibling notebook or shared runtime state was inspected or changed.

Unfinished mechanism: approximate the exact48-node Jhat(w) sum through
R(z)=(exp(z/2)-sinh(z)/z)/(2*z*sinh(z)/z). For small z, use its Taylor
polynomial and shared Gaussian moments; for the remaining arguments use
the factored quotient (E16(z)-T10(z))/(2*(1+z*T10(z))), with
E16=sum(k=1..16) z^(k-1)/(2^k*k!),
T10=z*sum(j=1..10) z^(2*j-2)/(2*j+1)!.
The denominator is at least2 on the positive real ray. No 1/z
subtraction remains. Exact rational arithmetic avoids operation rounding,
but input constants/nodes/weights still require certified generation.

Provisional bounds to verify: on |z|<=2, |R|<6, hence degree28 Taylor
tail <=6/2^28 on [0,1]. The first17 logarithmic panels give w>=16,
so x/sqrt(w)<=1, and shared scaled moments avoid663*48 callbacks.
The remaining117 profiles and J(1) use the quotient on [0,4]. Prove
its remainder <2^-28 and derivative <=35; then propagate absolute
2^-60 input errors. Count every rational operation in this core,
including coefficient and moment formation, without calling it the
aggregate cost. Constants, Gauss-node/weight and q generation, I(1),
prime/outer arithmetic and final exponentials remain outside this core.

Continuation/stop test: complete the core proof and exact bounds/count;
do not evaluate any scalar unless the full radius and all work pass.
An unfinished core or missing generation cost is not a full preflight.

## Completion and continuation

The finite core is now proved in canonical
[C033z](../lemmas/C033z-direct-positive-real-stable-inner-arithmetic.md).
Its exact rational certificate is
`scripts/smoothed-law/direct_positive_real_inner_core_1801.json`.
All21 rational checks pass. The conditional input requirement is
absolute2^-60 for the stated node/weight/exponential/q data. Subject
to that requirement, the Jhat differences have error<2^-24 and their
exact-outer-sum contribution is<2^-22. The core count374518 includes
coefficient/moment formation, clamping and final differences; it is
not the full evaluator's operation count or a bit-complexity estimate.

No input data, Gauss callback or scalar was evaluated. Input generation,
constants, I(1), the remaining profile/prime terms, outer and final
arithmetic still lack a full error/cost contract. The aggregate preflight
therefore remains INCOMPLETE; do not infer either complete2^-10 allowance.
Application audits of C033y and C033z remain pending.

Continue the exact unchanged ready1799 target using C033y/z. This is
an informative local arithmetic input, not a new central mechanism.
The independent signed-height estimate/representation blocker recorded
in comparison1796 persists; no creative target is invented to fill a
scheduling preference. Earlier C033x/1781/1782 stops are preserved and
do not prohibit the present distinct evaluator. PROOF.md is unchanged
because the main mathematical assembly and unresolved gap did not change.
