# Direct transverse summand of the actual mixed trace

STEP_ID: YM-20261008-084-mixed-direct-trace-test

Reuse `literature/2026-09-26-current-target.md` (SPECIALIZE) for the
unchanged combined-response target. The bounded intermediate target is
the direct transverse summand of L064(16), exactly as saved after L066.
Seek O(N²), or a retained nonzero stronger-power coefficient, using the
actual paths, multipliers, covariance and complete signed heat sum.
It could remove this summand at a² scale; it cannot settle the first
pair, the axial-path summand, other endpoint monomials or the logarithm.

Checked L064–L066, L062's heat coefficients, L026's tensor spectrum,
L028's quantitative consistency, L041's separated-source argument,
and ATTEMPTS/019–021. General norm estimates are exhausted, and L066's
packet is not a lower bound on this trace. Ready primary-source coverage
is reused; no general flow or stress-matching theorem is reproved.

Unfinished reasoning saved before writing the proof: for each upper
edge e put x_e=Sigma_T Q_l^T K_1^T delta_e. The identity
K_1^T delta_e=-D g_s(Delta_T) delta_e deletes P algebraically.
On the compact coefficient neighborhood its smooth extension should be
O(a⁴), by the full transverse mode sum and the physical axial separation.
The actual Q_l has local coefficient derivatives O(a p_m(l)), so the
forcing Q_l^T K_1^T delta_e is locally O(a⁵). Globally the known operator
bounds give ||x_e||_2=O(a^-1 p(l)), hence ||x_e||_(L²_a)=O(a p(l)).
A proved interior discrete elliptic estimate, followed by a lattice
Fourier interpolation estimate, would give a local C⁵ extension
O(a p(l)). L028 would then give ||A_0 I_T x_e||_2=O(a³ p(l)).
The retained left column sqrt(N) g_k(e) E_0 G E_+^T delta_e has
norm O(p(k)), using (G²)(v,v)=O(N), including pinned endpoints.
Summing all O(N³) upper edges would bound the direct S_kl by O(p(k)p(l)).
The interior estimate and the higher derivative bounds on the actual
forest exterior paths must be justified before treating this as a result.

Essential inputs: L018, L026, L028, L041, L062 and L064.
L066 is stop evidence only; L065 controls a different input block.
L011/L019 remain necessary for the full response. No signed growth,
scaled mixed limit, logarithmic coefficient, finite matching or
reflected error <=c_box/2 is assumed. Continuum fields, full reflection
positivity, infrared control and finite positive mass remain open.

Completed: L067 supplies the missing interior estimate by an exact
cutoff energy identity, eight orders of physical differences and
lattice Fourier interpolation. The actual source has local C^m size
O(a⁵ p_m(l)); its covariance column has global L²_a size O(a p(l)),
and its local C⁵ extension has that same size. L028 then gives an
O(a³ p(l)) ordinary residual-column norm. All O(N³) upper-edge
columns and the full heat sum yield O(1) for the direct trace.
This clears O(N²) for exactly this summand and removes it at a² scale.
The proof retains the actual prefix paths and pins; no numerical
preview, unrestricted block bound or conditional sign is used.

Outcome: ADVANCE / RESEARCH / REPRODUCTION. This is relevant local
standard-method progress, without a beyond-source originality claim.
The large gain merits a separate critical audit of the source,
interior regularity and path-derivative arguments before extending the
mechanism. The right axial-path summand and all independent gaps above
remain open; no complete solution candidate or logarithm is claimed.
