# Leading-minor attempt2039 — work checkpoint

Approved target: assessment `literature/2026-11-20-tilted-hurwitz-leading-sign-test-2037.md`.
Reuse comparison2037 and recovery2038; this is the nominated mathematical
attempt, not another literature review. Main gap: L030-L032/C032a.

Exact finite reduction obtained from C029m's recurrence and weights:
for even N with beta_N nonzero, the monic reflection has first Hurwitz
minor -N^2 beta_(N-1)/beta_N. Necessary strict positivity is equivalent
to opposite adjacent beta signs. Degree drops must not be ignored.

Work in progress, not a proved asymptotic: combine Kuznetsov (11) inside
the rotated integral before estimating. Put q=2 sqrt(pi)(1+i),
K_n=sqrt(pi)/(2 Gamma(n+3/2)), c_n=i(-i)^n exp(i pi/8). Then
a_n=Im[c_n K_n integral_0^infinity exp(-x)x^n/(1+exp(q sqrt(x))) dx].
The transformed integrand multiplier is

    P_n(x)=8n^2+12n+7-4x^2-4n(n-1)(n^2-1/4)/x^2.

At x=n+sqrt(n)u, P_n/n tends to 16(1-u^2). The Gaussian saddle
weight tends to exp(-u^2/2-q u/2). Its weighted integral should be
32 pi i sqrt(2pi); the resulting proposed beta leading term is

    16 pi^(3/2) sqrt(n) exp(-2sqrt(pi n))
      sin(n pi/2+2sqrt(pi n)-pi/8).

Still unpaid at this checkpoint: absolute O(n^(-1/2)) integrated error
after division by n, global tails including x near zero, all prefactors
and phase signs. Planned test: even N with reduced phase in
[3pi/4,5pi/6]; if the error is paid, adjacent beta values have the same
strict sign along an infinite subsequence. No numerical scan.

Analytic representation retains Kuznetsov's unaudited upstream[9]
qualification. No new independent derivation from finite Bernoulli
formulas is claimed. Higher minors, bare one-sided exclusion and the
qualified limit/symmetry bridge remain separate. If tails/error cannot
be paid in this attempt, retain this draft and stop inconclusively.

Completed disposition: the combined integral and all three tail regions
are now handled in canonical C029u,
`lemmas/C029u-even-reflected-hurwitz-leading-sign-obstruction.md`.
Its exact positive scale B_n has absolute beta error O(B_n/sqrt(n));
the even phase subsequence proves strict violations with actual degree.
The earlier unpaid items above record the work checkpoint, not current
assertions of missing bounds. The full proof still needs an independent
conceptual audit and retains the named analytic-input qualification.
