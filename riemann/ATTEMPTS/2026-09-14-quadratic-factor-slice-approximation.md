# Quadratic Taylor approximation on a full factor slice

Date: 2026-09-14. The attempted shortcut is to replace the phase on
an entire length-comparable-to-sqrt(N) integer b slice by its quadratic
Taylor polynomial with uniformly vanishing absolute error.

WHY IT FAILS: [L203](../lemmas/L203-factor-slice-quartic-phase-reduction.md)
proves that the omitted cubic contribution at the far endpoint is
comparable to sqrt(N), uniformly over the actual allowed triples.
The quartic Taylor polynomial does give vanishing error. This refutes
only the uniform quadratic approximation, not a possible distribution
estimate for quadratic phases, and not the desired phase population.
