# Short-resonator correlation attempt — 29 October 2026

Invocation-start scope is the unchanged EXPLORE target in
`literature/2026-10-29-complete-residual-short-resonator-fourth-moment.md`.
This working note preserves unfinished reasoning; it is not a proved input.

Main gap: actual-Xi all-degree mixed positivity. The bounded intermediate
test is the complete L477 residual fourth-moment lower bound
I_4 >= c T(log T)^24. By audited L480 this would stop its particular
second/fourth-moment interpolation certificate, without deciding I_1,
negative mass or RH. Required correlation and norm scales are
S >= c T(log T)^18 and H <= C T(log T)^16.

Retained inputs: exact L477 R_T and actual theta; L479 Section 1's
Gonek Lemma 2 normalization only; audited L480's interpolation criterion;
the approved finite mean square, Holder and elementary geometric sums.
The coefficientwise, supremum and stationary-involution stops remain.
No new source or mathematical script is needed for the finite attempt.

Provisional calculation plan (not yet conclusions): N=floor(T^(1/24)),
d_a=d_3(a;N), Q=N^3. Group the nonchirped part using products of length
M Q. For the chirped term the scalar saddle is r=2 pi nm a/b,
with main coefficient 2 pi d_a d_b log(n/m)^2/b. Resonances b|ma
are nonnegative. Reduced denominators q<=b<=Q<<M might bound the
complete nonresonant sum by O(M Q (log T)^6). Both scalar endpoint
kernels must be summed over all tuples, including empty intervals and
coincidences; their middle-region coefficient is O(d_a d_b L^2/(b sqrt T)).
The weighted equal-product diagonal is the remaining delicate lower bound.
An elementary coprime factorization matrix is a candidate construction,
not an established estimate. Stop if no signed/error separation is proved.

Completed in this invocation: the provisional plan is now proved in
`../lemmas/L481-short-resonator-fourth-moment-obstruction.md`, including
the weighted diagonal, auxiliary norm, both endpoint kernels and complete
nonresonant sum. The earlier paragraphs preserve the reasoning before
completion, not remaining proof gaps. The result awaits a separate critical
audit; no independent audit is claimed in this proof-construction turn.
