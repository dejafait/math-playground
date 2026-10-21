# Full-grid diagonal cubic-bound attempt

Ready assessment reused: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
Main gap: interacting ultraviolet control. Intermediate target: bound
L116's exact signed full-grid diagonal by O(N^3), retaining distinct
levels s,t, every path/component filter and the complete exterior heat sum.
This could close cubic boundedness of transverse H; it would not establish
its limit or the joint compensation coefficient.

Essential inputs: L028 L088 L099 L110 L111 L112 L113 L114 L115 L116;
L091 supplies assembly. Checked overlap and ATTEMPTS/029--032: the
proposed test uses a complete closed-trace symbol and a local finite-path
coefficient error, rather than their stopped operator/mass shortcuts.

Working test: at each spatial input x freeze the actual normalized
transverse exterior edges separately at levels s and t to real vectors
v_s(x),v_t(x). The two path coefficients should equal v_mu+v_nu and
v_nu-v_mu up to O(a p(k)). L088's exact path phases then give
P F_v=2 P r_v^T in component-center phases. The complete generator
H_u has real even coefficients in those phases, D is imaginary odd,
and E_j is real even. Thus the complete diagonal Fourier integral
should vanish for arbitrary independent real v_s,v_t,u and each j.
Need verify the phase conversion and local coefficient comparison.

For the remaining error, bounded fixed stencils and
integral ||E_j|| <= C(1+|j|)^(-4) would give trace-diagonal error
C a p(k)p(l)(1+|j|)^(-4). Spatial count N^3, weighted level count
N^2 and outside a then give O(a^2 N^5)=O(N^3).

Continue if these identities and estimates hold with the original
filters. Stop if the cancellation needs s=t, omitted path phases,
component filters moved through P, or smoothness across pinned jumps.
No negligible earlier cubic error, finite transverse-H limit, evaluated
compensation, or complete Yang--Mills construction is assumed.

Completed: L117 verifies the exact integrated odd-symbol cancellation
for arbitrary independent vectors at s,t, without requiring exterior
label symmetrization or a pointwise-zero integrand. The O(a) local path
comparison and the complete offset bound C(1+|j|)^(-4) give R_inf=O(N^3).
All existing comparison errors are at most cubic, so R_H,tr=O(N^3);
L095 then gives the same bound for R_H with Q subtracted. No earlier
cubic error is removed from the coefficient. Outcome ADVANCE,
RESEARCH / REPRODUCTION, local standard-method progress only.

Continuation within the unchanged ready complete-group target: determine
the a^3 limit of R_inf by retaining the first-order local coefficient
correction in L117(4), using the exact kappa integrals and distinct s,t.
Essential inputs: L028 L088 L080 L111 L113 L116 L117; L091 and L095
fix assembly, L097 L098 L100 L101 L104 L107 retain other limits,
and L084 L079 L080 L082 fix the reference with its numerical qualifications.
The complete offset majorant has a finite first offset moment; this is
an input bound, not a proved Taylor-limit theorem. Continue only if the
first-order path correction has a justified uniform mode majorant and
its actual level/spatial sums converge before removing the heat tail.
Stop if identifying its limit requires a pinned-jump extension, equating
levels, or discarding a merely cubic error. L110/L111/L113/L115's
remaining cubic errors, the transverse-H limit, the values of the other
functionals and the required joint coefficient -4 gamma D_i before
factor 3 remain unresolved. No compensation or negligible cubic error
is assumed. Preserve ATTEMPTS/028--032 and all independent construction,
finer-scale, interacting, reflection-positivity and infrared/mass gaps.
