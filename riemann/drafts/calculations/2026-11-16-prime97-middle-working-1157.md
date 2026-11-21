# Fixed middle-response calculation1157 — working checkpoint

Approved target: assessment1155, separately approved1156. Only the saved
family 1_E+t1_M, t real, and original prime97/8 allocation are in scope.
Main gap: L030–L032/C032a actual-Xi mixed positivity, not this allocation.

Inputs read: C750h (pulse/domain and old wide enclosure), C750i
(geometry/pairing), C750j (capped contrast), audited C750k (full kernel).
No duplicate middle-response calculation was found in the targeted local
records. Preserve all earlier stops. No essential new literature needed.

Plan saved before computation: use C750k's exact whole-line kernel,
not the old pulse quadrature. Let m=2a-2w, A(L)=J[1_(0,L)], and
K_g(u,v)=integral_0^u integral_0^v j(g+x+y)dy dx. Then the matrix
should be (2A(w)-2K_m(w,w), -2K_0(w,m); -2K_0(w,m), A(m)).
Derive/check factors and all overlaps before minimization. Membership
follows from each finite interval transform being O(1/|frequency|).

For each nonnegative decreasing Laplace-s integrand, use endpoint
rectangle enclosures on a fixed dyadic mesh from delta=2^-24 to S=16,
2048 equal panels per octave. Bound both omitted s ranges analytically;
all arithmetic uses the existing MPFR384 backend without changes.
Save every endpoint term, cumulative sums, errors and full matrix in
scripts/prime-collar/certificate-1157.json. Fixed endpoints and mesh
will not be tuned after a straddling sign. Compare exact scalar
minimum EE-EM^2/MM-8kw to zero only after MM>0. A strict negative
interval is an unaudited allocation counterexample; a positive interval
closes only this family; a straddling interval ends inconclusively.

## Analytic reduction saved while the fixed certificate runs

Every supported overlap at shift r is accounted for by
I intersect (I-r)=I_L and I_L+r=I_R. Thus on this family the
correlation is w for every real t, regardless of the middle value.
Each interval indicator has Fourier transform bounded by its length
and by 2/|frequency|, so all family members belong to D_a.

C750k's exact real polarized form gives J(e,h)=-integral_(E x M)
j(x-y)dxdy=-2K_0(w,m), since E and M are disjoint. Likewise the
collar cross term is -K_m(w,w), so J(e)=2A(w)-2K_m(w,w).
The diagonal response is A(m). No off-diagonal interaction is dropped.

From C750k's nonnegative whole-line form, for a single interval,
A(L)=L log2+(1/pi)integral_0^infinity e^(-2s)G_L(s)ds,
G_L(s)=log(1+(L/s)^2)+(2L/s)atan(s/L).
Indeed the real difference form is twice the integral across each
end, yielding 2[integral_0^L z j(z)dz+L integral_L^infinity j(z)dz].
Tonelli justifies the displayed s integral.

For s>0 and z>=0 put Phi_s(z)=-(z/s)atan(s/z)-log(s²+z²)/2
with the continuous value Phi_s(0)=-log s. For z>0,
Phi_s'(z)=-(1/s)atan(s/z), Phi_s''(z)=1/(s²+z²).
Consequently the Laplace integrand for K_g(u,v) is
Phi_s(g+u+v)-Phi_s(g+u)-Phi_s(g+v)+Phi_s(g).
At g=0 its value follows by continuity, not differentiation at0.
These expressions keep the cancellation of pi*z/(2s) analytic.

All four s integrands including e^(-2s) are positive and decreasing:
for K this follows under its positive spatial integral; for G_L use
G_L=2[integral_0^L z/(s²+z²)dz+L integral_L^infinity
1/(s²+z²)dz]. Thus the complete rectangles need no sampled derivative
or quadrature remainder assertion.

For delta<L the omitted G_L integral below delta is bounded by
2delta[log(2L/delta)+2], since G_L<=2log(2L/s)+2 there.
For adjacent K_0(w,m), enlarge m to infinity, split x at s,
and use atan(s/x)<=min(pi/2,s/x): its integrand is at most
pi/2+log(w/s) for s<w, giving the small bound
delta[pi/2+log(w/delta)+1]. For the far pair use w²/m²,
giving delta*w²/m². All lower omitted bounds are zero.

Above S the respective integral upper bounds are e^(-2S)/2 times
L²/S²+pi L/S (single interval), wm/S² (adjacent), and w²/S² (far).
They follow from log(1+x)<=x, atan<=pi/2, and denominator>=s².
Restore 1/pi for all integrals and L log2 for single intervals.

After MM>0 the exact scalar completion gives
J[e+t h]-8kw=MM(t+EM/MM)^2+EE-EM²/MM-8kw.
The bounded finite span is the entire scope; no arbitrary trace,
unbounded inverse, neutrality or Xi realization is inferred.

## Completed disposition

The fixed certificate gives a positive minimized margin in
(0.00083852,0.00092782), so the no-counterexample family test closes.
The full argument is now canonical in C750l. No parameters changed.
The initial decimal-output containment check failed and is preserved;
its replacement directly reconstructs all integrals and the minimum
from all57345 saved nodes using exact rational arithmetic. All27 final
verification checks pass. Independent critical audit is still pending;
its new source gate is REVIEW_REQUIRED in assessment1157. The main
argument and PROOF.md are unchanged. See history1157 for validation.
