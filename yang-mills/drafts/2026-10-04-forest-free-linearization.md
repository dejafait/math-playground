# Free linearization of the compensated forest generator

The completed-step target is the exact free-linearization COVERED_TARGET in
drafts/literature/2026-10-04-forest-compensated-ward-identity.md. Its saved
SPECIALIZE assessment is ready and is reused without browsing. Existing
work, identifiers and stopped branches are preserved.

The representation gap is an explicit linear operator on the forest
coordinates used by L011's Gaussian Hessian. The intended use is to take
Ward derivatives in those coordinates without dropping the tree-path
terms. The discriminating test is equality of the induced trace and
curvature action variation with L009, followed by equality of the two
leading Wilson-flow responses. A discrepancy would stop the proposed
operator. No interacting bound against c_box/2 is sought from this free
test; that bound and physical-boundary control remain open.

Working reasoning saved before matrix checks:

- For one real color, let H_F A(v) be a times the signed sum of A along
  the pinned root-to-v path, and set it to zero on the boundary. With d_0
  the relative vertex differential, H_F d_0 = identity. The linear
  retraction is R_F = identity - d_0 H_F. It sets every forest edge to
  zero and changes no curvature.
- Let E_F insert remaining-link coordinates, with zero forest entries,
  and let B_F extract them. Linearizing L016's compensator gives
  K_F = B_F R_F K_a E_F. Its path potential is H_F K_a E_F, rather than
  H_F E_F. The factor a comes from U = exp(g a A).
- Since K_a d_0 = 0, the decomposition into pinned gradients and the
  forest slice gives Tr K_F = Tr K_a = 0. Equality of traces does not
  require the diagonal entries of K_F to vanish individually.
- The forest action Hessian is positive. Its Gaussian Ward insertion is
  sum_c <d_1 E_F b^c, d_1 E_F K_F b^c>_a - 3 Tr K_F. Since
  d_1 R_F = d_1, it is L009's insertion on the slice. Gaussian curvature
  laws agree by the existing L003 quotient result.
- The linear Wilson flow is exp(-tau d_1* d_1) on the full initial
  configuration, whereas L008 uses Hodge heat flow. Their curvatures
  coincide because their difference lies in the gradient sector. This
  must be checked before identifying either flowed probe.

The saved reasoning is now completed in
[L017](../lemmas/L017-forest-free-generator-and-gaussian-ward-comparison.md).
It proves the retraction, the compensated linear operator, trace equality,
and the forest-Hessian Ward identity for both actual free Wilson-flow
probes. The latter agrees with the existing Hodge response because the
Wilson and Hodge heat operators have identical curvatures and L003's
normalized quotient law applies. No higher Taylor polynomial is assigned
the Hodge law. The existing free residual limit is reused, not reproved.

The check
`PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 scripts/forest-ward/check_free.py`
uses two N=4 rooted forests, including a reversed upper-face orientation.
Both have 81 forest edges. Independent exact plaquette contractions agree
with the compensated curvature map. Six reduced diagonal entries are
nonzero in each sample, but their total trace is exactly zero. Deleting
paths gives exact maximum curvature-map discrepancies 3/80 and 1/24.
Thus total trace alone is an inadequate check of the induced operator.

The numerical Hessian check agrees between forest and Hodge curvature
covariances within 1.8e-15, and both nonzero sample flowed responses and
their Ward covariances agree within 9e-17. The sample responses are about
0.1004700911 and 0.01858817482. These use one-site rational displacement
coefficients and the existing two quadratic construction rules; they are
not the original smooth displacement or interacting Wilson expectations.
The original all-mesh comparison is proved in L017.

Outcome: ADVANCE / RESEARCH / REPRODUCTION, limited to an explicit input
for the finite forest representation. No ultraviolet estimate, result
beyond the checked literature or improvement toward reflected error
<= c_box/2 is claimed. No inconclusive exploration turn is spent. The
nonlinear identity and free representation tests are now complete.

The next direction reuses the exact ready TARGET in
drafts/literature/2026-09-26-current-target.md for the complete remaining
one-loop coefficient. Its hypotheses are unchanged. The explicit
compensated operator and forest-Hessian contractions give a concrete
mechanism to test actual terms in L011, beginning with the connected M2
measure contraction against its two leading quadratics and a test of
forest dependence. Its cutoff behavior cannot determine the full
logarithm before the action, insertion and flow terms are combined.
Require an evaluated contraction or informative obstruction. This does not repeat
the stopped bulk-only locality import or license another unevaluated
expansion. All prior stopping evidence and the missing boundary,
interacting, continuum and mass-gap steps remain preserved.
