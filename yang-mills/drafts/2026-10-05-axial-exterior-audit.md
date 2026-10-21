# Independent audit of the interior axial exterior estimate

STEP_ID: YM-20261005-039-axial-exterior-audit

The approved combined-response target and its unchanged SPECIALIZE
assessment remain in force. The main unresolved comparison is the
interacting reflected error <= c_box/2; computing the complete fixed-mesh
coefficient and its cutoff asymptotics is an intermediate diagnostic.
This bounded step audits only L028's selected interior axial
one-internal-action-pair bound for both original probes.

Intermediate target: verify L028's second-order adjoint consistency,
all-mode relative inverse estimate, stored-coordinate conversion and
restriction excluding the upper pinned face. Its downstream use is to
exclude this selected class as an unsuppressed logarithmic source.
Continue using the bound if those estimates follow from the actual
operators; withdraw or repair the affected rate if a stencil, covariance
order or boundary mismatch appears. An audit does not compute the full
coefficient or certify a finite matching constant.

The supplied literature assessment is reused, including its primary
flow-finiteness, bulk stress protection and lattice-matching citations
and their restrictions. This step does not reprove those theorems or
extend their scope. Relevant local inputs are L008, L009, L018, L023,
L025, L026 and L027. ATTEMPTS/011–012 continue to rule out raw-loop and
tensor-only uniform bounds; the prior finite-mesh samples are not
asymptotic premises. L019's complete cancellation obligations persist.

The audit is complete. The canonical proof in
[L028](../lemmas/L028-axial-action-loop-exterior-bound.md) now spells out
the exact generator adjoint and telescoping consistency argument, and
the stored-coordinate covariance product. Its statement is unchanged.
The four checks were:

- The clover, endpoint and incidence maps are centered between their
  actual component grids. Reversing their order differentiates the
  coefficient products. Uniform integral difference bounds justify the
  O(a^2) rate with five input derivatives beyond the requested output
  norm. Only the limiting u is required to be continuum divergence-free.
- Applying three relative Laplacians to the compactly supported
  residual uses six further differences. The inverse-mode C^1 majorant
  has summand O(|ell|^(-7)) in four dimensions, with a positive spectral
  gap. It includes all components, the zero own-direction cosine mode
  and all allowed high modes. There is no infinite-lattice substitution.
- The physical/stored conversion gives covariance a^(-2)Delta^(-1)
  in x=a A, insertions a^2 Q_i and a^2 N, and the nonsymmetric exterior
  order U E B_i E R U^T. Symmetry of R justifies the residual mode row;
  neither Q_i nor N is commuted through a heat factor.
- Both active transverse edges have interior endpoints and levels
  j,j+1 <= N-1. Their lower-root path sums differ by one level, not by
  a pinned upper-face potential. The restriction excludes the axial
  omitted link at level N-1 and every face-crossing plaquette. L027's
  transformed contraction retains all three colors and both mixed
  entries; its coefficient bounds give the stated absolute sums.

No counterexample or mathematical error was found within the stated
scope. This is EXPLORATION / REPRODUCTION: an independent bounded audit
of existing local mathematics, not a new theorem, improved rate or
advance beyond the inspected literature. It resolves the requested
review of that proof but leaves every excluded class and the complete
coefficient unevaluated. No mathematical script or numerical run was
needed. The argument assembly and DAG are unchanged.

Continuation within the same approved target: test a uniform O(1)
bound for the excluded upper-face axial one-internal-action-pair class
using its actual ordered quartic and lifted exterior product. Inputs
are L003, L008–L011, L018, L023 and L025–L028; L019 remains the required
cross-group cancellation framework if an isolated bound fails. The
upper-face potential is pinned to zero, not assigned the lower-root
sum; the omitted axial edge is a variable coordinate. Neither L028's
two-active-edge polynomial nor its neighbor-difference rates may be
assumed on this class. A bound must retain every surviving edge and
all modes. Continue if that full class can be bounded; if the exact
upper-face lift defeats the estimate, record the obstruction and test
a different cancellation mechanism. Transverse plaquettes, the
no-internal-pair class, other jets, finite matching, the reflected error
<= c_box/2 and the continuum/infrared gaps remain independent.
