# Common-pole generic increment: bounded attempt

2026-10-30. Research under the pre-existing EXPLORE assessment
`literature/2026-10-30-common-pole-generic-increment-test.md`.
No new source gate or change of target is being made.

Main gap: actual-Xi all-degree positivity, with the conditional L522
upper sign still open. The intermediate target is the exact generic
compression increment Gamma_p from the assessment on L526's fixed
normalized two-packet family, common M=L+2 and actual P_-/P_+.
A coefficient at most -2 at scale rL could nominate a collective
comparison; a contrary coefficient, subleading bound or domain
obstruction stops this local absorption mechanism. No independent
overlap/remainder, missing-prime, nullvector, family or Xi-transfer
gap is assumed closed.

Inputs read: all of L526, its confirmed Sonin-only stop, and the
completed generic-increment source comparison. Reusing its literature
and duplicate/failure screen. Primary paper 2 v2 Lemma 4.1 and proof
(4.1)--(4.4) reopened for the exact Hardy application; this is input
retrieval in the approved research step, not a new literature turn.
Halmos's primary PDF retry returned 403; the saved assessment already
records its inspected full decomposition/Theorem 2, which is reused.
Source manuscripts remain unaudited; Mathlib matching coverage unchecked.

Working reduction (to be completed and checked): with E=P_- the
frequency Hardy projection and R reflection, J=M_(bar u)R and
J E J=M_(bar u)P_+M_u. Thus the physical positive compression is
A=E M_(bar u)P_+M_u E. Its intersection is exactly L526's K, with
projection S. Halmos gives A-S>=0 on the generic part and zero on
the four intersection parts. The smoothed full trace is the squared
HS norm of M_F E M_(bar u)P_+. Lemma 4.1 must therefore use bar u,
not u. Its fixed-p phase derivative and higher derivatives have
polynomial growth, and its second derivative is bounded. Finite
traces follow only after checking these hypotheses and the measures.

Remaining calculation: derive a correlated difference for the added
factor rather than subtract the separate O(sqrt(B)) errors. The
common pole phase remains fixed during the prime change. Preserve
the full prime-power series, reflected symbol and two-packet weight.
No signed increment estimate is established in this checkpoint.

## Direct difference under development

Reserve E=P_- for Hardy negative frequencies in the t variable,
Z=M_(exp(itL)), v=bar u_-, V=M_v P_+ M_v^*, and
R=M_v^* E M_v. The added conjugate Euler factor is
a=(1-r Z^*)/(1-r Z)=1+r(Z-Z^*)+O(r^2).
With B_L the t-Fourier projection onto (0,L),

    [Z-Z^*,P_+]=-(B_L Z+Z^* B_L).

The prospective full-compression increment is therefore

    -2r Re Tr(B_L Z R W R B_L)+O_h(r^2 L),
    W=|H|^2(2+Z+Z^*).

Trace-ideal remainder plan: expand a in its absolutely convergent
shift series; [Z^n,P_+] is a band of length |n|L followed by a
shift. For any bounded multiplier m and such a band B,
||M_F E M_v M_m B||_HS is at most
||m||_infinity[(|B| integral |F|^2 dm)^(1/2)
+||[M_F,E]||_HS]. The last squared norm is O_h(L).
This would give the displayed correlated O(r^2 L) error, uniformly
in the common background, after summing the geometric coefficients.

Move only the fixed multipliers H and bar H through R:
||[R,M_H]||_HS=||[E,M_H]||_HS=O_h(1). The resulting trace error
is O_h(sqrt(L)); do not commute the whole two-packet transform
with R at O(1) cost. The remaining diagonal band formula involves
R(H exp(i xi t)) for -L<=xi<=L.

Proposed uniform selector: let R0=sqrt(p), a_p=phi_-'/R0 and
b_p=1_(a_p>0). Show
sup_(|xi|<=2L)||R(H exp(i xi t))-b_p H exp(i xi t)||_2=o(1).
An elementary route conjugates D=-i d/dt: R is the negative
spectral projection of D/R0-a_p. Its unitary group is an exact
translated phase; Taylor's bound uses ||phi_-''||=O(R0 L),
whereas amplitudes have derivative O_h(L). Smooth spectral cutoffs
therefore approximate multiplication by the corresponding function
of -a_p. A separate small-turning-set bound is still needed for
the discontinuous projection.

On compact t intervals the approved PNT input gives
a_p(t)=4 Re(exp(itL) K(t))+o(1),
K(t)=(e exp(2it)-1)/(1+2it), which never vanishes. If the selector
and trace estimates hold, phase averaging predicts

    Gamma_p/(rL) -> -1-(4/pi) c_h,
    c_h=integral |H(t)|^2 Re(K(t)/|K(t)|) dm(t).

This is a target calculation, not yet a theorem. The required
threshold is c_h>=pi/4; deciding its relation requires a rigorous
bound as well as all preceding limit justifications. Sonin's
O_h(r L^(9/10)) difference would then be negligible by L526.

## Completed attempt

The preceding paragraphs preserve the intermediate reasoning. The
completed proof is canonical in
`lemmas/L527-common-pole-generic-prime-increment.md` (paths here
are notebook relative). It verifies the positive compression and
both separate traces, the trace-norm O(r^2 L) expansion, the uniform
moving Hardy selector, and the phase average. Its exact integer
interval certificate bounds c_h between 0.1511 and 0.2343, below
pi/4, so the generic increment's limiting coefficient is between
-1.299 and -1.192. The local -2 absorption threshold fails.

The result is informative NEGATIVE for this mechanism, not a claim
of an RH disproof or certified novelty. The proof and certificate
await an independent conceptual audit; upstream source proofs retain
their qualifications. The proposed audit is a new target and its
assessment is REVIEW_REQUIRED, not approved in this research turn.
No further mathematical mechanism was attempted here.
