# Approved slow-dilation calculation

Target and prior coverage: `drafts/literature/2026-10-30-slow-dilation-weighted-gap-cost.md` (SPECIALIZE, saved before this turn).

The exact main gap remains actual-Xi all-degree positivity. The bounded
intermediate test is the uniform absolute Q_a bound for p(z)e(z/D),
D>=max(1,B), without H_a. Success stops only this family as a route to
an unbounded positive ratio; failure would require a rigorous weighted
norm witness and would not establish H_a membership or Xi transfer.

Saved calculation before documentation: if phi is the smooth compact
spectrum of e, the spectrum of e(z/D) is phi_D(v)=D phi(Dv).
Multiplication by z^j replaces it by (-2pi i)^(-j) phi_D^(j),
without increasing support. Thus f has bandwidth r=R/D, even with
unbounded finite polynomial degree. Fourier inversion gives
|phi_f|<=N and |f(x+iy)|<=2r exp(2pi r b)N for 0<=y<=b.
Replay the isolated-zero argument with ambient R to obtain N<=A_R M.
Then |Q_a(f)|<=4rb exp(2pi r b)A_R M
=R A_R a exp(2pi R b/D)M/D. Since b/B=log L/L<=1,
this implies the target with C_R=R A_R exp(2pi R), for T>exp(1).

Finalized: the full proof, source qualifications and Mathlib status are
in supplementary (19) of canonical L504, without a new lemma ID or use
of L503's unaudited theorem. The old L504 audit remains explicitly
confined to its original conclusion. The saved sketch above is the
pre-documentation reasoning; canonical L504 controls the exact statement.
No numerical script was needed. A separate REVIEW_REQUIRED assessment
nominates an independent audit; that audit was not performed this turn.
