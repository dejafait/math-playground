# E diagonal: full-prefix scalar reduction

The unchanged EXPLORE-approved target is the complete other/other cubic
limit in `literature/2026-10-10-other-other-cubic-leading-scale.md`.
This bounded subtest addresses L092's R_E. The main gap remains the
interacting ultraviolet construction; removing an unknown leading-scale
term could help test compensation with L084, without controlling other
jets, finer scales, reflection positivity or the infrared/mass problem.

Unfinished reasoning saved before the proof: put U=T Delta_0^(-1/2),
B_(s,r)=1_(r<s), and F_11=H_T^(-1/2) A_11 H_T^(-1/2).
L092 gives V_g=U B F_11 B^T U^T and L065 gives ||F_11||<=C.
Factor the actual R_E through K_h^(1/2) Omega_k^T U B. Its leading
part is K_h^(1/2) Cc^T Zeta_k U B. The axial-energy bound from
L097 may allow replacement of K_h^(1/2) Cc^T by its static transverse
partial isometry with an o(N^(3/2)) Hilbert–Schmidt error, retaining
the upper prefix jump. Cycling the resulting trace should expose
the exact cumulative scalar residual B_s A_11 B_s^T rather than a
local strain times s. This is a proposal, not an established limit.

Continue if there is a controlled cubic-scale reduction, a finite limit
or a specific obstruction. Abandon any step that treats the residual
as level diagonal without proof, drops the upper jump, differentiates
a base-law projection zero, or uses the fixed-mass transverse H
shortcut stopped in ATTEMPTS/030. Known finite contractions, L065's
scalar bound and L097's source methods are imported, not rederived as
new general theorems. Searches in the relevant drafts/history found
the R_E limit unresolved; no duplicate scalar-prefix reduction was found.

Essential inputs: L008 L018 L026 L028 L065 L085 L088 L091 L092 L097.
L084 fixes the comparison with L079/L080/L082's qualifications. R_R,
R_H,tr and the gradient-base crossed limit remain open; the H axial
and curvature functionals remain unevaluated. No static replacement,
evaluated coefficient, joint compensation or candidate is assumed.

Further reasoning checkpoint: the square-root static comparison has
joint eigenvalue error squared at most mu/(mu+lambda). L097's full
prefix energy count therefore gives Hilbert–Schmidt error O(N^(6/5))
against factors O(N^(3/2)), hence trace error O(N^(27/10)) using
||F_11||<=C. The static trace contains A_<s=B_s A_11 B_s^T.
Its exact scalar form includes an axial endpoint term
(2a)^(-1) sum_mu T_mu^T M_(u_1(s)) T_mu. It cannot be omitted.
For fixed transverse mass the normalized finite stencil a A_<s
should converge after cumulative axial Riemann sums and the exact
transport commutators. Its symbol divided by lambda is bounded by
the scalar energy bound; inverse errors must be controlled uniformly
before identifying a limit. This remains unfinished here.

Completed: [L101](../lemmas/L101-other-other-e-diagonal-prefix-limit.md)
proves a finite real a^3 R_E limit for both probes. The controlled
O(N^(27/10)) static-trace error uses the full-prefix energy estimate
and the uniformly bounded scalar residual. Its exact cumulative
insertion A_<s retains the endpoint term at the moving prefix cut;
the normalized scalar stencil yields the explicit functional K_(i,E).
Transverse inverse errors are uniform at cubic scale before finite-range
coefficient freezing. This is local REPRODUCTION, with no evaluated
coefficient, sign or progress beyond the checked standard methods.

Continuation inside the same unchanged approved complete-group target:
test L091's independently cubic-bounded gradient-base crossed pair
using L092(10)'s exact off-diagonal residual representation in its
actual trace order. Require a controlled limit, a signed reduction
or a specific obstruction; scalar polarization is not available for
its transverse right input. Essential inputs: L009 L018 L026 L028
L065 L085 L087 L088 L091 L092 L097 L101. No cross-component form
bound, differentiated base-law zero, static replacement or compensation
is assumed. R_R and R_H,tr remain without cubic control; K_(i,E),
K_(i,ax) and K_(i,Q) remain unevaluated, with K_(i,Q) subtracted in R_H.
L084/L079/L080/L082 fix the required comparison and IEEE qualifications.
Finer scales, other jets and interacting/continuum requirements remain
unresolved. Reuse the unchanged complete-group literature assessment.
