# Direct compact-support transform growth screen1535

TARGET: Test whether C032m's odd kernels K_sigma(w) satisfy a common bound |K_sigma(w)|<=C(1+|w|)^N exp(A|Im w|) for all complex w and sigma in [1,2], as a prerequisite for a uniformly bounded compact-support Fourier-Laplace representation.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Endpoint review1535 searched exact nonlinear-kernel, signed-support, Gaussian-mixture and entire-exponential growth terminology and checked C032j/k/l/m/n, ledger1532, stop1302 and transform comparison1266; no inspected matching growth theorem for K was found. See drafts/literature/2026-11-18-endpoint-support-source-notes-1535.md.
SOURCE_EVIDENCE: Hormander, Supports and singular supports of convolutions, Acta Math110 (1963), Theorem2.1/(2.4), pp281-282, primary scan https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5966-11511_2006_Article_BF02391861.pdf; statement and printed proof read in1535. C032m and ledger1532 supply covered Gaussian/entire-integration tools. Newman Proposition1.12 is context only for this screen.
COMPARISON: A compact-distribution family with common support, bounded order and common distribution estimate must obey this bound. C032m proves compact-disk bounds only. Neither a matching bound nor a violating lower-growth sequence for K has been established; a bad upper envelope proves neither.
GAP: Establish the stated global bound with finite C,A and integer N>=0, or rigorously show no common constants exist; retain the actual divisor and nonlinear terms. This screens a direct transform in w, not arbitrary reparameterizations or mass-one annihilators.
REASON: Signed endpoint sources are available, but the transform interface is missing. One necessary-growth test is independently falsifiable. This nomination derives no new mathematics and awaits separate next-turn approval.
SCOPE: Actual C032j divisor, multiplicities and fixed-v1 qualifications; C032k/m normalized primitives and K_sigma=exp(-E_sigma)*sinh(O_sigma), 1<=sigma<=2. Only direct Fourier-Laplace transforms in w from a uniformly bounded common compact distribution class are tested. No density, endpoint atom, one-sign support, zero width, positive mixture, moment or Xi realization is assumed.

## Bounded mathematical test after separate approval

Use exactly the displayed inequality, with C>0, A>=0 finite and
integer N>=0, independent of sigma,w. Keep both reflected exponentials
and the actual infinite Gaussian zero sum. Any exchanges, complex
directions or lower bounds beyond C032m require full justification.
C032n is not essential; its pending audit is not bypassed.

A positive result must give actual finite constants or a rigorous
existence proof on the whole plane and full width interval. A negative
result must contradict every common triple, for example through a
proved violating sequence at one fixed admitted width. Failing to
estimate K is inconclusive. Growth of E or O alone cannot stand in
for growth of their nonlinear combination. No finite surrogate or
grid fit proves the required assertion.

Stop after this growth decision or the first unpaid control issue.
Do not also attempt signed-mixture uniqueness. A violation parks this
direct uniform compact-distribution interface, not other coordinates,
individual nonuniform representations or endpoint methods generally.
A bound leaves transformed-input identification, nonvanishing for
mass-one eta and injectivity open. Its plausible use is to screen one
source bridge for compact signed cancellation; L030-L032/C032a
actual-Xi positivity and unsmoothed realization stay unpaid.

This is auxiliary established-route development, not a new creative
mechanism at the main sign gap. Full matching Mathlib is unknown.
