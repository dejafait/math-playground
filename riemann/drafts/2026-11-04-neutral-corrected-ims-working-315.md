# Corrected two-window defect: working record, step315

Invocation-start EXPLORE coverage is the unchanged
`drafts/literature/2026-11-04-neutral-corrected-ims-defect.md`, exact
COVERED_TARGET in PROGRESS at invocation. One bounded mathematical
attempt, not another source review; preserve all earlier work.

Main gap: unrestricted-support complete Weil positivity. Target: the
fixed six-mode exact-neutral corrected localization defect at T=8log3,
ell=6log3. A negative exact-neutral vector stops only the literal
nonnegative-defect rule. A finite nonnegative form leaves smaller-window
positivity, full-class control and uniform iteration unresolved. No
family enlargement is authorized. Reuse L744(6) and L749's smooth cutoff;
L743's different moment columns are comparison only; no L742 premise.

## Partial reasoning saved before implementation

Write B(t)=eta(1-(t/r)^2), r=ell/12, and
b=integral exp(t/2)B(t)dt>0. Evenness gives the same b for exp(-t/2).
For c_(j,k)=a_j+k ell/3, the nominated matrix has entries
H_j(sigma,k)=b exp(sigma c_(j,k)/2). Thus its determinant, with rows
(+,-) and columns (1,2), is -2b^2 sinh(ell/6)=-8b^2/3, nonzero.
This also explicitly accounts for the translated exponential weights.
All bumps lie strictly inside their nominated windows. The flat cutoff
and partition give smooth compact zero extensions. Exact correction
therefore kills both moments; the complete pole product vanishes only
after this identity, not as a numerical approximation.

The global cutoff is symmetric about T/2. With
M_k=integral exp(x/2)phi_k(x)dx, odd modes satisfy the negative moment
equal to exp(-T/2)M_k and even modes its negative. M_1>0. Pairing
x and T-x on the left half proves M_2<0. Hence the two-moment map has
rank two, and exact neutral basis candidates are phi_k-(M_k/M_1)phi_1
for k=3,5, and phi_k-(M_k/M_2)phi_2 for k=4,6.

For real compact smooth h, the DLMF5.9.16 representation in the ready
assessment suggests the exact physical-space evaluation
A(h)=m(0)||h||^2+integral_0^infinity k(u)(||h||^2-R_h(u))du,
k(u)=2exp(-u/2)/(1-exp(-2u)), R_h(u)=integral h(x+u)h(x)dx.
It must be justified by the nonnegative squared-difference expression
and Plancherel before certification. Every arithmetic term is
-2 Lambda(n)/sqrt(n) R_h(log n); equality at the window delay is zero.
No positivity of the full energy or numerical sign is presumed.

Pending: full signed defect formula, validated numerical or analytic
enclosures and sign. Diagnostic previews will not count as proof.

## Diagnostic and validation plan

`scripts/corrected-ims/screen-315.json` is explicitly NONRIGOROUS. It
suggests Delta(phi_3-(M_3/M_1)phi_1) about -0.0381, not a certificate.
Reflection interchanges the two nominated corrections, so their full
energies are equal. Both pole products vanish by exact algebra above.

For g_j=rho_j f, q_j=g_j-C_j g_j, let Q be the polarization of the
complete form. The exact expansion is
Delta=E(f)-sum E(g_j)+sum[2Re Q(g_j,q_j)-E(q_j)].
If K_u=Re integral f(x+u)conj(f(x))
              [1-sum rho_j(x+u)rho_j(x)]dx, the first difference is
-integral_0^infinity k(u)K_u du
-2sum_(n<6561) Lambda(n)/sqrt(n) K_(log n)
-2Re sum_j M_+(g_j)conj(M_-(g_j)). The last term is necessary before
correction; compact smooth domination justifies all integrals.

Prospective certificate: enclose samples with elementary directed
interval arithmetic, interpolate linearly on a uniform periodic grid
of period P=64, and evaluate its full periodic Fourier form plus exact
linear-interpolant delay correlations. Use a validated FFT, the
O(log R/R^2) Fourier tail controlled by the interpolant derivative,
and exponentially small real-line/periodic archimedean image error.
Control smooth-to-linear replacement by ||h-q||_2<=s^2||h''||_2 and
||h'-q'||_2<=s||h''||_2 and a logarithmic Fourier norm bound.
The prime form error retains its complete operator norm. Every error
must be recorded; if enclosures overlap zero the outcome is inconclusive.

The optional python-flint installation was unavailable because network
DNS failed; no source coverage changed. A self-contained interval
implementation, if completed, is the mathematical certificate route.

## Completed disposition

The corrected interval implementation succeeds; canonical full proof
and enclosures are in L750. `scripts/corrected-ims/certificate-315.json`
has Delta upper endpoint -0.03606073089581196. All constant checks pass.
The first full certificate used an insufficient eta derivative bound
270; it is marked invalid and preserved, and the entire calculation was
rerun with 280. The constant check's first equality enclosure is also
preserved; exact integer arithmetic verifies its value 352. Neither
failed output supports the conclusion. Do not use the diagnostic as
evidence. No family enlargement or independent audit was performed.
