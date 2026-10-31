# Approved Haar support diagnostic: working record

Target and source gate: the exact TARGET in
`literature/2026-10-30-euler-phase-haar-support-obstruction.md`, whose
saved SPECIALIZE assessment was supplied at invocation start.
No actual-height replacement is used. Existing uncommitted work is
preserved.

Main gap: actual-Xi all-degree mixed positivity. The intermediate
test concerns only nonvanishing Haar L2 error for the specified
rational-frequency rectangle; a positive result could stop this
particular globally accurate truncation implementation. Continue if
a uniform positive limiting distance or a contrary asymptotic is
proved; otherwise preserve the computation and park it.

Working mechanism, saved before full write-up: for r=p^(-1/2),
the factor (1-rz)/(1-r conjugate(z)) has Fourier coefficients
a(1)=-r, a(-j)=(1-r^2)r^j (j>=0), and a(k)=0 (k>=2).
The geometric expansion converges absolutely uniformly for each p;
finite tensoring and Parseval are covered by the saved assessment.
For the real part the coefficient at k is (c(k)+c(-k))/2.

Use k_2=-2 to force c(-k)=0. In the prime block
y^(10/11)<p<=y require exactly eleven coordinates k_p=1.
Then the reduced numerator exceeds y^10=T^(1/100), so these
characters lie outside V_T. Under the squared c(k) law, k_2=-2
has mass 1/16 and the block indicators are independent Bernoulli(1/p).
Strong Mertens and a fixed-order elementary-symmetric calculation
should give block probability tending to
(10/11)(log(11/10))^11/11!, hence a squared-distance lower bound
with an additional factor 1/64. Check that complement coordinates
are summed without restrictions and that finite-T coefficient laws,
real-part cancellation and growing-prime limits are fully justified.

Completion: the full proof and qualifications are now canonical in
L484. The stated positive bound is obtained there, with a separate
critical audit still pending. This saved working record is not the
certificate. No script or numeric experiment was used.
