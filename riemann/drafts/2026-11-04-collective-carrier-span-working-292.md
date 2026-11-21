# Collective corrected carriers — working checkpoint, step 292

Approved target: establish or refute the cardinality-independent
complete-energy floor for finite separated-carrier spans of L744,
with K,w,chi,Delta fixed. The saved SPECIALIZE assessment is
`literature/2026-11-04-collective-corrected-carrier-span-specialization.md`.
This is one standard-mechanism mathematical attempt, not a source turn.

Main gap: unconditional actual-Xi mixed positivity. A successful floor
would pay this high-carrier trial space only; low-frequency signs,
moment complements, cross-block coupling and growing support remain open.
The generic-source and prime-only stops were checked and remain intact.

Unfinished argument saved before development:

- Use Montgomery--Vaughan Corollary 2 on one interval where |w| is
  bounded below, and on (0,L) for the upper norm bound. Choose a fixed
  separation large enough to pay the lower denominator.
- L744 (13) gives ||h_t||_H2 <= H |t|^-2. Separation on both half-lines
  should give sum |t_r|^-4 <= 2T^-4+2T^-3/(3Delta). Cauchy--Schwarz
  then pays the entire correction synthesis map, not each vector alone.
- For d_T(xi)=[log(T/(2pi))-m(xi)]_+, use L744 (8). Outside
  |xi|<T-sqrt(T), d_T should be <=2/sqrt(T)+8/T^2. Inside, it is
  O(log T), and every carrier is at least sqrt(T) away.
- Use |F_w(u)| <= C(1+|u|)^-2. A separated row sum and an integrated
  column tail, justified directly by weighted Cauchy--Schwarz, should
  bound the entire synthesis leakage by O(T^-1)||c||_ell2^2.
- Apply the triangle inequality in the nonnegative deficit seminorm
  to the original sum and its correction, then divide by the paid
  norm. L744 (6)/(7) removes both poles exactly; its full arithmetic
  bound costs Cprime. No RH-conditional L742 input is used.

Still to verify: explicit row/column constants, all-T thresholds,
complex coefficients, both carrier signs and finite-domain energy.
Continue only if the error vanishes independently of cardinality and
maximum carrier. Stop if any unpaid sign or growing-support assumption
enters. No inequality is yet claimed proved by this checkpoint.

Completion of the same attempt: the full proof is now canonical in
`../lemmas/L745-collective-corrected-carrier-energy-floor.md`. It gives
the exact requested floor with epsilon(T)=O(T^-1/2), uniformly in
carrier count and maximum frequency. The interval normalization,
collective inverse-fourth-power bound and row/column leakage constants
are written there; this draft is retained as the pre-proof checkpoint.
L745 remains unaudited. A separate conceptual audit is the continuation;
no new central-sign claim or RH candidate results.
