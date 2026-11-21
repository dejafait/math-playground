# Compact signed convolution: attempt1244

17 November 2026. One mathematical specialization under the prior
SPECIALIZE assessment1242/review1243; no additional source search.

The intended assembly uses C030r's real triangular normalization at t
and C030v's bound between t and s=t-u. Conjugating the shifted Hankel
matrix gives R(u) J R(u)^T, so its norm is at most B_t(u)^2. Integration
against total variation should put the normalized signed perturbation
strictly within distance one of J. Every leading block must be treated
separately using triangularity; full-matrix inertia alone is insufficient.

Before completion check a common neighborhood of t with x-u>0,
domination of all required ordinary derivatives, the fixed signed
measure, every leading size including one, and atoms at both support
endpoints. Retain s_*=t, M=0, n=2m, repeats, arbitrary contrasts and
the closed phase boundary. No boundary extension or actual-Xi
representation is being attempted. Success means the exact strict
criterion; an unpaid additional premise is a gap, not a refutation.

Completed in [C030w](../../lemmas/C030w-compact-signed-convolution-determinant-criterion.md),
which contains the full proof, citations, boundary checks and limitations.
The complete strict criterion follows with no extra positivity premise.
The proof awaits independent audit. This checkpoint is retained as
working history; the main all-degree actual-Xi gap and scoped stops remain.
