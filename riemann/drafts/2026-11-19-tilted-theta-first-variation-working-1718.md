# Finite tilted-theta response working checkpoint1718

Approved target: assessment1716, SPECIALIZE, separately approved1717.
One calculation only; no tilt sweep or higher derivatives. Main gap:
actual-Xi all-degree positivity, equivalently the unpaid C028b height
condition. Existing stops1695/1713 and parks1534/1708/1716 are preserved.

Write b_n=B_n(0), T=sum_(1<=n<d)b_n and V=2T/d. Imported Toda
gives A_n'(0)=b_(n+1)-b_n and B_n'(0)=0. Thus the empirical
mean derivative is b_d/d. The centered cubic trace derivative reduces
to 3*b_d*(b_(d-1)-2T/d), before division by d; the interior square
terms telescope. Proposed final identity:

    g_d'(0)=3*b_d*(b_(d-1)-V)/(d*V^(3/2)).

At d=3, the sign is that of b_2-2*b_1. Existing L021/L025/L027
give probability moments mu_2=M_2/M_0, mu_4=M_4/M_0 and
mu_4-3*mu_2^2=-12*S_2<0. Orthogonality yields b_1=mu_2,
b_2=mu_4/mu_2-mu_2, so this existing strict moment inequality
appears to settle nonvanishing negatively in degree3, without any new
recurrence estimate. This is part of the approved first-response test.

Completion: the full proof and citations are now canonical in
[C028q](../lemmas/C028q-tilted-theta-finite-spectral-skewness-first-variation.md).
An independent d=3 determinant expansion confirms the trace derivative
and empirical divisor. L025/L027's existing strict fourth-moment input
proves the negative degree-three sign. The actual standardized cubic
and both real affine signs are retained. General-degree nonvanishing,
actual-magnitude attainability, full residual payment and uniform tilt
control remain open. Independent audit is pending.

Verification method: exact algebra in the canonical proof. A preliminary
optional SymPy availability check failed (module not installed); no
symbolic computation or numerical certificate is claimed, and no package
was installed. The independent determinant check is written out in full.
