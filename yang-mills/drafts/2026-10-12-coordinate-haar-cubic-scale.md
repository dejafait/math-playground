# Coordinate-Haar cubic-scale attempt

Approved target: determine whether L018's complete coordinate-Haar response
has a vanishing a^3-scaled limit for both actual L010 probes in the straight
lower-rooted forest. The prior EXPLORE assessment is
`literature/2026-10-12-coordinate-haar-cubic-scale.md`.

The main construction gap remains the ultraviolet-uniform interacting
comparison and continuum/infrared construction. This intermediate test
asks whether one same-forest response term can compensate L147 at cubic
scale. It leaves all other response jets and construction gaps unresolved.

Working calculation saved before final verification: use physical Delta,
the symmetric whitened residual R, bounded whitened probe B_i and
E=exp(-tau Delta). L018 becomes -2 Tr(E B_i E R U*U), where
U=a^-1 R_F Delta^-1/2. L028(5), with r=0, gives
||N_a f_k||_a <= C a^2(1+|k|)^5, so L023's rank-one heat expansion
should strengthen to ||R E||_1 <= C a^2. No heat is put on U*U.
The full pinned prefix has norm at most N, unscaled D0 has norm at
most 4, and ||R_F|| <= 1+4N. Thus ||U||^2 <= C a^-4.
Trace-ideal multiplication in the displayed order would give O(a^-2),
which suffices for a^3 Gamma^M -> 0. Retain upper pinned rows through
the full D0; do not apply L028's interior-only lift estimate there.

Continuation test: verify normalization, the one-sided heat rate and full
prefix bound. Abandon this mechanism if any fails at the required powers;
a generic O(a^-3) bound would not establish the zero threshold.
ATTEMPTS/009 and /011 remain valid: no forest independence or bounded raw
link covariance is assumed. L019's other nonlinear jets remain essential.

Completed result: [L148](../lemmas/L148-coordinate-haar-vanishing-cubic-scale.md)
verifies the normalization and each estimate above. It proves
|Gamma^M_(i,F)| <= C_i a^-2 and hence a^3 Gamma^M_(i,F) -> 0 for both
actual probes. The exact trace, full pinned prefix and all heat modes
are retained. No script or numerical evidence is needed. This is a local
advance under the prior EXPLORE assessment, without certified novelty.
The same target and unchanged assessment are retained for a separate
critical proof audit; the proof is not a candidate solution of Yang--Mills.
