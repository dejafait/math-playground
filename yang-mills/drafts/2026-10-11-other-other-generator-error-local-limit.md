# Generator-displacement error: compact derivative trace limit

Ready assessment: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
This is a bounded subtest of its unchanged complete other/other target.
Main gap: interacting ultraviolet control and a nonzero physical continuum
sector. Intermediate target: a finite cubic-scaled limit for L111's
Delta_V, using L119's derivative trace. Its downstream use is one retained
coefficient of transverse H; the other placement and exterior-circulation
errors and the joint compensation remain independent obligations.

Working reasoning, UNVERIFIED until checked in the canonical proof:
at fixed spatial range R and axial-offset cutoff J0, M_v B has compact
output and compact input, up to R lattice sites. In the cyclic trace
F_k M_v B F_l^T (P-P_bulk), the first factor's input edge rows lie
in a fixed physical interior set. L114's localized projection bound
therefore gives a subcubic error. No scalar crosses the projection.
Use F_k=a sum_alpha S_alpha M_phi(k,alpha). For compact plaquette
x,y the full-grid replacement then has entries
a^2 sum_alpha,beta phi(l,alpha,s)(y) phi(k,beta,t)(x)
Q_alpha,beta(y,x), where Q_alpha,beta=S_alpha^* P_inf S_beta.
With d=x-y fixed and s=t-j,
L080's exact lower prefix and fixed modes identify the limiting scalar
coefficients as V_mu+V_nu for b and -V_mu+V_nu for q. Only after
this fixed-offset argument may their limiting physical levels coincide.
The factor a min(s,t) tends to x_1+4. The normalized sum is an
a^4 four-dimensional Riemann sum with no extra box-length factor.

Candidate universal tensor: let q_alpha,beta(d) be the kernel of
S_alpha^* P_inf S_beta in the original lower-vertex convention; set
beta(r,j,m;alpha,beta)=sum_d tr(B(r,j,m)(d) q_alpha,beta(-d)).
Its absolute convergence follows from ell^2 Cauchy--Schwarz;
q_alpha,beta is ell^2 since P_inf is bounded and S has finite support.
The sum over j is absolutely convergent by L119(5). The resulting
functional is the heat sum of the integrals of
(x_1+4) partial_m u_rho phi(l,alpha) phi(k,beta), against this tensor.
L080's uniform B_i bound and physical eigenvalue lower bound supply
Gaussian heat tails multiplied by the existing polynomial p. L119(6)
then removes spatial and axial tails in the controlled order.

Essential inputs: L028 L080 L088 L111 L113 L114 L119. L110 supplies
the moments already imported by L119. No smooth upper-pin extension,
finite-mesh equal-level identity, negligible cubic placement error,
evaluation of a coefficient, or joint compensation is assumed.
Preserve ATTEMPTS/028--032. Continue if the compact projection error,
fixed-offset Riemann limit and uniform heat/kernel tails all close;
abandon this localization if it needs compact support of a nonlocal
output, an unproved boundary extension or absolute first kernel moments.

Continuation after a successful limit: select one still-retained cubic
placement error or the exterior-circulation remainder under the unchanged
assessment. A complete compensation test needs those limits plus values
of K_(i,E), K_(i,ax), K_(i,Q), K_(i,G), K_(i,R) and K_(i,V), with
L091/L095's assembly and L084/L079/L080/L082's reference retained.
The physical target, finer scales and the remaining response jets stay open.

Completed: L120 proves a^3 Delta_V -> K_(i,V) for both probes, with
an absolutely convergent real functional. The compact projection
comparison costs O_(J0,R)(N^(3/2)(log N)^(3/4)); the fixed-offset
normalization is exactly a^4 [a min(s,t)], and both uniform heat and
kernel tails close. The functional is unevaluated. Outcome ADVANCE,
RESEARCH / REPRODUCTION: local standard-method progress only.

Concrete continuation inside the unchanged approved complete other/other
target: test Delta_sc=R_bulk,moved-R_bulk,sc in L113(9). Use its exact
Z-Z^sc identity, retaining the two path-stencil differences and the scalar
finite-projection commutator, to seek a first-derivative reduction with
o(N^3) error or an independently testable obstruction. Do not assume such
a reduction, an available joint kernel moment, a small projection norm,
or a negligible cubic error. Continue if the full signed error has a
controlled derivative trace or a finite scaled limit; abandon this
reduction if its required moment or boundary transfer actually fails.
Essential inputs L028 L080 L088 L110 L111 L113 L114 L119 L120;
L115/L118 locate the still-retained comparison and energy error,
L091/L095 fix assembly, and L084/L079/L080/L082 fix the reference and
its arithmetic qualifications. All coefficient evaluations, the
exterior-circulation and energy errors, and the independent gaps remain.
The exact saved Next action and assessment are unchanged; no new source
assessment, coefficient evaluation or derivative claim is approved here.
