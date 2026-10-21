# Actual right axial-prefix trace test

STEP_ID: YM-20261008-086-mixed-axial-prefix-trace

Reuse `literature/2026-09-26-current-target.md` (SPECIALIZE) for the
unchanged full-response target. The bounded intermediate target is
L064(16)'s actual right axial-path summand, with O(N²) sought and
a²-scale removal requiring o(N²). Such a bound would exclude stronger
powers from this one summand, without completing the mixed response.
Continue if its exact prefix composition meets that threshold;
otherwise park this estimate rather than assume source smoothness.

Specific duplicate/failure checks: L064 sections 3–5, L065, L067,
ATTEMPTS/019–021 and history/085. L065 supplies a scalar residual
bound, not a trace estimate; L067 supplies only the direct summand.
The supplied primary-source assessment is reused. No general flow or
stress-renormalization result is reproved; Mathlib coverage is unchecked.

Unfinished reasoning saved before completing the bound: let J take
every lower axial prefix and let T_ax be its actual signed transverse
incidence, so the axial forest lift is J T_ax. Its adjoint source at
axial edge r is the sum over s>r of Q_(l,s)^T K_(1,s)^T. Do not infer
interior smoothness from L067, because this sum includes near-top levels.
Instead use the full spectral bound
||K_(1,N-d)||_HS <= C N^(3/2) d^(-5/2), 1<=d<N.
If proved, the summable d tail and ||Q_(l,s)||<=C a p(l) give
||J^T Q_l^T K_1^T||_HS<=C a N² p(l). The scalar relative inequality
||T_ax Sigma_1^(1/2)||<=1 and L065's ||R_01||<=C should then bound
the ordered trace by sqrt(N) times this norm times
||G^(1/2) E_+^T M_(g_k)||_HS<=C a N^(3/2) p(k), yielding O(N²).
The shell sum, operator order, endpoints and heat sum remain to be
verified. No o(N²) estimate, limit, sign or logarithm is assumed.

Essential inputs: L018, L026, L041, L062, L064 and L065. The actual
paths and multipliers are retained. L067's direct result is used only
when assembling the two right-lift summands. The first pair and other
endpoint monomials, all nine logarithmic placements, other/other
cubics, measure, insertion/flow jets and L011/L019's nonlinear forest
compensation remain open. No axial-source regularity or cancellation
is assumed. Finite matching, reflected error <=c_box/2, continuum
fields, full reflection positivity, infrared control and finite
positive mass also remain open.

Completed: L068 proves the exact spectral shell bound (8), summable
level estimate (9), adjoint prefix estimate (12), and ordered trace
bound (16), giving O(N²) for both probes after the full heat sum.
The scalar residual input is used only in its proved component-1
scope. No interior regularity of this prefix source was needed.
This is ADVANCE / RESEARCH / REPRODUCTION: a new local bound within
the approved specialization, not progress beyond the checked sources
or a solution of the full logarithmic problem. The independent audit
of this bound is the next bounded test within the same assessed target.
