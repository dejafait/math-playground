# L761 — effective infinite-prolate and full CCM trial projection certificate

## Hypotheses

Fix lambda=sqrt(13), c=2pi lambda^2=26pi, L=log(13), N=120.
Use the translated orthonormal basis of L759,

    V_j(u)=L^(-1/2) exp(2pi i j log(lambda u)/L),  -120<=j<=120,

on [lambda^-1,lambda] with measure du/u. Inner products are conjugate
linear in the first argument. P_120 denotes this orthogonal projection.
No ground vector or sign of the Weil matrix is used in this lemma.

Import the angular prolate modes and their exact Legendre representation
from Osipov--Rokhlin, *On the evaluation of prolate spheroidal wave
functions and associated quadrature rules*,
[arXiv:1301.1707v1](https://arxiv.org/html/1301.1707v1#S3.SS2),
Theorems1,3,10 and equations(53)-(67). In particular, the positive
operator

    H_c=-d/dx ((1-x^2)d/dx)+c^2 x^2

has simple ordered eigenvalues chi_n, real unit L2(-1,1) eigenfunctions
psi_n of parity (-1)^n, and the stated normalized Legendre matrix.
The continuous-endpoint/Legendre self-adjoint realization is intended;
no alternative endpoint extension is allowed. This is the source's
differential eigenvalue chi_n, without a DLMF constant shift.

Set phi_n(t)=lambda^(-1/2)psi_n(t/lambda) on [-lambda,lambda],
extended by zero, for n=0,4. Let I_n=int phi_n(t)dt and choose

    h(t)=I_4 phi_0(t)-I_0 phi_4(t),
    k(u)=sqrt(u) sum_(r>=1) h(ru),  lambda^-1<=u<=lambda.

This is a common-scalar convention for the exact zero-additive-integral
trial of Connes--Consani--Moscovici, *Zeta Spectral Triples*,
[arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1#S7),
(7.2),(7.5)-(7.6), with the compact angular extension and finite sum
specified in Connes,
[arXiv:2602.04022v1](https://arxiv.org/html/2602.04022v1#S6.SS3),
sections6.3-6.4/(20) and footnote20. The proof below verifies I_0!=0.
Independently rescaling phi_0,phi_4 by nonzero a,b multiplies h by ab,
so this normalization preserves the source's projective trial. It is
not the older vanishing-at-zero, approximate-parity construction.

This is a computer-assisted specialization, not a new prolate spectral
theorem. It assumes the usual exact integer/rational semantics of Python
and correctly rounded Decimal arithmetic with the directed rounding
behavior specified below, as in the L759 arithmetic implementation.
Directed interval arithmetic encloses every numerical input. Point
inverse iterations are only candidate generators. Step371 independently
audited the operator realization, infinite isolation, normalization and
transport, and reconstructed every saved enclosure with a separate
interval implementation; section6 records the complete evidence. The
software arithmetic semantics remain trust assumptions.

## Conclusion

The certificate gives explicit unit polynomial approximants q_0,q_4 of
degree at most222, with signs of psi_0,psi_4 chosen by positive overlap,
such that

    ||psi_0-q_0||_L2(-1,1) < 2.645*10^-97,
    ||psi_4-q_4||_L2(-1,1) < 4.034*10^-93.

Their eigenvalues are in (80,82) and (723,726), respectively; their
mode labels are certified in the infinite problem. Omitted Legendre
coefficients are included in the errors above.

With Q_n(t)=lambda^(-1/2)q_n(t/lambda), J_n=int Q_n, and
H=J_4 Q_0-J_0 Q_4, put K=E(H) on this same interval. Then

    ||P_120(k-K)||_L2(du/u) < 1.276*10^-91.

For every j=-120,...,120, the real and imaginary parts of
a_j=<V_j,k> lie in the explicit closed intervals in
`scripts/spectral-triples/ccm-trial-certificate-369.json`, at
`/projection/exact_trial_coefficients/<j>`. Each component interval has
radius less than 1.276*10^-91, exceeding the selected accuracy
requirement (radius<10^-65). All 241 directions are retained.
The exact algebraic polynomial candidates are determined by the saved
decimal rational vectors divided by their exact Euclidean norms; no
displayed decimal midpoint is substituted for an exact eigenfunction.

These coefficient bounds are in the stated common-scalar convention.
They do not enclose b(P_120 k) away from zero, test L760's normalized
observable, compare full ground/trial vectors, prove a family estimate,
take either limit, or imply any Xi sign or RH. Reality gives
a_-j=conj(a_j); inversion parity a_-j=a_j is not assumed.

## Proof

### 1. Exact operator, domain and finite-to-infinite count

Let p_j=sqrt(j+1/2)P_j be the unit Legendre basis. Under this unitary
coefficient map, define D p_j=j(j+1)p_j with

    Dom(D)={v: sum_j j^2(j+1)^2 |v_j|^2 < infinity}.

Multiplication V by c^2 x^2 is bounded self-adjoint and 0<=V<=c^2 I.
Thus D+V is self-adjoint on Dom(D), lower bounded, with compact
resolvent (bounded perturbation of D). Here is the domain bridge to the
cited source, rather than an assumption about a formal infinite matrix.
For each source mode let a be its square-summable Legendre coefficient
vector. Theorem10 gives, coordinate by coordinate,

    j(j+1)a_j = chi_n a_j-(Va)_j.

The right side is a vector in l2 because V is bounded. Consequently
sum j^2(j+1)^2|a_j|^2 is finite, so a belongs to Dom(D) and is a genuine
eigenvector of D+V. Theorem1 supplies completeness of these source modes,
and Theorem3 supplies their simple ordered differential eigenvalues.
There is therefore no extra spectral subspace or endpoint extension in
this realization: the complete source eigenbasis diagonalizes D+V.
Parity identifies the even eigenvalues as chi_0,chi_2,chi_4,... . This
argument uses neither a truncation assertion nor a DLMF parameter shift.
No odd-sector gap is
needed because the candidates and residuals lie in this invariant
subspace. We use the standard self-adjoint spectral theorem and min-max
principle on this domain, not a heuristic finite-matrix approximation.

The cited matrix has, for j>=0,

    M_jj=j(j+1)+c^2[2j(j+1)-1]/[(2j+3)(2j-1)],
    M_(j,j+2)=c^2(j+1)(j+2)/[(2j+3)sqrt((2j+1)(2j+5))].

Keep the first m=112 even coordinates, degrees0,...,222, with finite
matrix A. The omitted compression is C=D_tail+Q V Q on Dom(D_tail),
where Q removes the retained coordinates. It is self-adjoint by bounded
perturbation, with form domain Dom(D_tail^(1/2)); it has C>=dI,
d=224*225=50400, since the compressed potential is nonnegative.
The only coupling B is
beta=M_(222,224) between the last retained and first omitted coordinate.
This includes all couplings; the remaining matrix is tridiagonal in
the even index. For each tested real t<d, C-t has positive bounded
inverse. Completing the quadratic-form square gives the finite Schur
complement

    S(t)=A-t-B(C-t)^(-1)B*,
    A-t-rho(t)e e* <= S(t) <= A-t,
    rho(t)=beta^2/(d-t),

where e is the last finite coordinate. The completion maps the form
domain to itself: (C-t)^(-1)B* maps a finite vector into Dom(C), and
the other component has the positive form of C-t. Therefore the
negative index of H_c-t on the even subspace equals that of S(t).
More explicitly, for finite x and tail form vector y the form equals

    <x,S(t)x> + ||(C-t)^(1/2)(y+(C-t)^(-1)B*x)||^2.

The triangular change of variables and its inverse preserve the form
domain, so they preserve its maximal negative-subspace dimension. The
positive tail contributes no negative direction. This proves the index
identity by the min-max principle, with no infinite determinant.

At t=80,82,723,726, respectively, interval tridiagonal LDL proves that
both bounding finite matrices have negative indices 0,1,2,3 and no
zero pivot. The complete 896 pivot intervals (four thresholds, two
matrices, 112 pivots each), correction intervals and off-diagonal
entries are saved at `/infinite_counts` and `/operator`.
For example the recurrence is

    d_0=a_0-t,
    d_k=a_k-t-b_(k-1)^2/d_(k-1),

with rho subtracted at the last diagonal for the lower matrix.
Every division excludes zero. Equal indices and nonsingularity of
both bounds imply, by ordered finite eigenvalue monotonicity, that
S(t) has that same index and no zero eigenvalue: its first k eigenvalues
are strictly negative by the upper bound, and all remaining ones are
strictly positive by the lower bound, where k is the common index.
A zero vector for H_c-t would, by its tail equation, give a zero vector
for S(t), so there is no omitted endpoint eigenvalue either. Compact
resolvent then makes the negative index exactly the count below t.
The infinite operator
therefore has exactly one even eigenvalue in each stated interval,
with labels0 and4. Finite Ritz gaps alone would not prove this step.

### 2. Full residual and eigenfunction error

For each selected mode, take the saved rational vector v and the exact
unit vector q=v/||v||, extended by zero. It is a polynomial and belongs
to Dom(D). A saved decimal rational mu is only a residual center.
The full residual consists of the 112 coordinates (A-mu)q and the
one omitted coordinate beta q_last; all other coordinates vanish.
Directed intervals give

    r_0=||(H_c-mu_0)q_0|| < 1.229*10^-97,
    r_4=||(H_c-mu_4)q_4|| < 2.456*10^-93.

The exact, tighter enclosures, rational centers and every residual
coordinate are stored at `/modes/0` and `/modes/4`. Their centers are
near 80.9290775234758 and 724.2175529925164. If (l,u) is the relevant
isolator, set s=min(mu-l,u-mu)>0. The certificate checks r<s. The
spectral theorem first places some eigenvalue within r of mu; the
count just proved identifies it as chi_n. Every other even eigenvalue
is at distance at least s from mu. Thus the squared norm of q's
component orthogonal to psi_n is at most (r/s)^2. With the real sign
chosen for nonnegative overlap,

    ||q-psi_n||^2=2(1-sqrt(1-delta^2)) <= 2delta^2,
    delta<=r/s<1,
    ||q-psi_n||<=2r/s=:epsilon_n.

The stored epsilon_0<2.645*10^-97 and epsilon_4<4.034*10^-93 prove
the stated bounds. In particular the norm of the exact omitted tail
is at most epsilon_n. This uses the infinite separation from section1,
not the tiny and unrelated Weil-matrix gap of L759/L760.

### 3. Integral normalization and bounded coefficient transport

The scaling to [-lambda,lambda] is unitary; substituting t=lambda*x
in the source's PW_lambda gives H_c with c=2pi lambda^2. Since
int_(-1)^1 p_j=0 for j>0 and int p_0=sqrt(2),

    J_n=sqrt(2lambda)q_(n,0),
    |I_n-J_n|<=sqrt(2lambda)epsilon_n.

The exact normalized q_0 constant coefficient minus epsilon_0 is
enclosed strictly above zero. In this convention J_0 is between1.187
and1.189, and J_4 between0.720 and0.721. Hence I_0!=0; independence
of phi_0 and phi_4 makes h nonzero. Its additive integral is exactly
zero by its definition. Sign choices or independent nonzero scalings
only change its common scalar, as specified in the hypotheses.

Both Q_n and phi_n have unit additive L2 norm. Cauchy--Schwarz gives
|J_n|<=sqrt(2lambda). Expanding h-H as

    J_4(phi_0-Q_0)-J_0(phi_4-Q_4)
       +(I_4-J_4)phi_0-(I_0-J_0)phi_4

therefore gives

    ||h-H||_L2(dt) <= 2sqrt(2lambda)(epsilon_0+epsilon_4)=:e_h.

Every function involved is compactly supported. On the chosen interval,
only 1<=r<=13 can contribute to E; the r=13 term is supported at a
single endpoint and has zero L2 class. For any additive L2 error f,

    ||sqrt(u)f(ru) 1_(lambda^-1<=u<=lambda/r)||^2_L2(du/u)
       = (1/r) int_(r/lambda)^lambda |f(t)|^2 dt
       <= (1/r)||f||^2_L2(dt).

The triangle inequality, even without using positive-half support,
gives ||E(f)||<=S||f||, S=sum_(r=1)^13 r^(-1/2). Bessel's inequality
for the exact L759 basis gives

    (sum_(j=-120)^120 |<V_j,k-K>|^2)^(1/2) <= S e_h.

The certificate encloses S e_h below 1.275818*10^-91. This is one
normwise error for the whole projected vector and bounds each complex
coefficient, hence each real/imaginary part. There is no factor sqrt(241)
needed here and no unproved point-evaluation estimate on an L2 error.

### 4. Exact finite integrations and rounding

Write H(lambda*x)=sum_(m=0)^222 d_m x^m. The exact polynomials obey

    H(lambda*x)=sqrt(2)[q_(4,0)q_0(x)-q_(0,0)q_4(x)].

The code expands p_j using the rational Legendre recurrence
(n+1)P_(n+1)=(2n+1)xP_n-nP_(n-1), then encloses every d_m.
Odd powers vanish by additive evenness; this does not impose inversion
symmetry in u. The p_0 amplitude cancels identically before expansion.
The full coefficient list is stored under `/trial`.

For omega=2pi j/L, direct integration on each support interval gives

    <V_j,K> = L^(-1/2) sum_(r=1)^12 sum_(m=0)^222
       d_m [sqrt(lambda/r) exp(-i omega log(13/r))
                -lambda^(-1/2)(r/13)^m] / (m+1/2-i omega).

Indeed the integrand is
L^(-1/2)u^(-1/2)exp(-i omega log(lambda*u))H(ru), and its mth
antiderivative has denominator m+1/2-i omega. At the upper endpoint
u=lambda/r the phase is exp(-i omega log(13/r)); at the lower endpoint
u=1/lambda it is1. For r=13 the endpoints coincide, so its integral
is exactly zero. All denominators have positive real part, including
j=0. Since j is an integer, the upper phase is also
exp(2pi i j log(r)/L); r=1 has exact phase1.

This finite power formula has no quadrature or omitted-series error.
The code groups the r sums first, divides by the complex denominator
using its positive modulus squared, and encloses every real and
imaginary part. The complete polynomial projection is saved at
`/projection/polynomial_coefficients`. The real function K has conjugate
negative coefficients; these are saved as well, with no even-part
replacement. The exact k intervals inflate each component by S e_h.
The exact j=0 imaginary part is0. The maximum stored component radius
is below1.275818*10^-91, including polynomial coefficient uncertainties,
transcendental rounding and mode errors.

Arithmetic details are part of the certificate. The script reuses only
the named interval class and elementary constant routines from
`scripts/spectral-triples/finite-parity-359.py` by AST extraction; it
does not rerun or assume that script's Weil computation. Decimal
addition, multiplication and division use floor/ceiling contexts of
260 digits. Correctly rounded sqrt/ln/exp endpoints are expanded by
one adjacent representable number. pi uses Machin's identity with
400 terms of each alternating arctangent series and the next-term
bound. Phase reduction subtracts an integer exactly and checks the
resulting angle has magnitude<4. Sine/cosine use260 Taylor terms and
twice the next absolute term, because all subsequent term ratios are
less than1/2. Their input intervals include all logarithm/pi error.
No binary floating-point eigenvalue is a certificate input.

### 5. Evidence, failed cutoff and reproduction

Run, from the notebook:

    python3 scripts/spectral-triples/ccm-trial-certificate-369.py
    python3 scripts/spectral-triples/ccm-trial-evidence-check-369.py

The first command writes all constants, operator entries, normalized
candidate coordinates, residuals, inertia pivots and coefficient
enclosures to the matching `.json`. It checks the selected mode bound
10^-70 and coefficient radius bound10^-65 and reports failures openly.
The successful file has outcome CERTIFIED_TRIAL_PROJECTION and no
failed assertion. SHA256 fields bind the script and reused interval
implementation. Software/runtime arithmetic correctness remains a trust
assumption; this is not a formal proof. The later independent audit is
recorded in section6.

The second command reads all 896 saved pivots, 226 residual coordinates
and 241 complex rectangles. It checks the full residual-error inequalities
and component inflations, verifies the same eight inertias by a
division-free leading-determinant recurrence, and checks the integration
formula at j=0,1,120 by summing the support intervals separately. Its
complete evidence file has outcome CONSISTENCY_CHECKS_PASSED, no failures.
Overlap of two computed enclosures is a consistency check, not a new
mathematical accuracy estimate. These checks do not replace the separate
conceptual audit of the infinite Schur argument and transport.

The initial m=96 truncation passed the infinite counts but gave
epsilon_4=3.83137...*10^-70, missing the chosen10^-70 mode threshold.
The initial failed script/JSON are retained with suffix`-first-pass`;
the same cutoff with improved failure reporting is retained with
suffix`-m96`, including the full failed residual. Increasing to112
changed the actual omitted-coupling error; it was not a relaxation of
the success threshold. The failed cutoff does not disprove the trial
or the certificate mechanism. No failed evidence was discarded.

This completes only the gate-approved fixed-cell prerequisite. Before
using L760's boundary-normalized ratio one must still enclose the
projected boundary denominator away from zero, then pay its error and
the ground observable error. Full-vector/family/limit/Xi gaps remain.

### 6. Independent conceptual and complete-arithmetic audit — step371

The separate audit verified the domain bridge and form-domain completion
in section1, infinite even-sector separation in section2, and the
normalization and bounded transport in section3. In particular, the
source coefficient identity is used to prove domain membership; it is
not silently promoted from a formal matrix equation. The exact omitted
compression retains the nonnegative potential. The spectral-theorem
error uses the whole even spectrum, including all omitted modes.

For the normalization, each sign is chosen by overlap with its own
candidate. The positive constant coordinate minus epsilon_0 ensures
I_0!=0 in that convention. A simultaneous change of the two independent
mode normalizations changes h by their product, as required. Zero
additive integral does not imply inversion parity. The map E is applied
only on [lambda^-1,lambda], where its finite L2 bound is valid; the r=13
endpoint makes no L2 or coefficient contribution. Bessel's inequality
controls the full projected error before any componentwise enclosure.
The finite integral in section4 retains both its endpoint terms and
the conjugation from the inner product. No boundary trace of an L2
remainder, Fourier invariance, ground vector or sign assumption enters.

Run the independent arithmetic audit from the notebook:

    python3 scripts/spectral-triples/ccm-trial-audit-371.py

It reads the complete original certificate without changing it and writes
`scripts/spectral-triples/ccm-trial-audit-371.json`. It imports no code
from the original interval implementation or candidate generator. It
uses 320-digit floor/ceiling Decimal contexts, all four endpoint quotients
for interval division, and sign-aware squaring. Sqrt and log are padded
by adjacent representable endpoints as in the stated arithmetic trust
assumption. The saved raw decimal vectors and residual centers are
interpreted as exact rationals, independently of how they were generated.

For an independent pi enclosure it uses
pi=4(atan(1/2)+atan(1/3)); the tangent addition formula gives tangent1,
and both angles have sum in (0,pi/2), fixing the branch. Each alternating
series keeps620 terms with the next term as remainder bound. For phases
it uses the original upper-endpoint turns -j(log(13)-log(r))/log(13),
subtracts an exact integer, checks |angle|<7, and keeps320 sine/cosine
terms. Twice the next absolute term bounds each tail because subsequent
ratios are at most49/(639*640)<1/2. All inputs to these computations are
intervals. Thus these are rigorous enclosures under the stated software
assumptions, not high-precision point comparisons.

Every original operator entry, Schur correction and LDL pivot contains
its independent reconstruction. The audit obtains the pivots as ratios
of consecutive leading determinants, checking all determinant signs.
All eight finite counts agree with the required0,1,2,3. It independently
normalizes both rational candidate vectors, recomputes every full residual
coordinate including the omitted coordinate, checks the residual norms,
isolating separations and eigenvalue intervals, and verifies the reported
unit-mode and integral/transport error bounds. The I_0 lower test passes.

The polynomial expansion is independently reconstructed using the exact
closed Legendre formula

    P_n(x)=2^(-n) sum_(l=0)^floor(n/2)
                (-1)^l binom(n,l) binom(2n-2l,n) x^(n-2l).

This is the coefficient form of Rodrigues' formula for the same Legendre
polynomials (equivalently it satisfies P_0=1, P_1=x and their three-term
recurrence). The constant Legendre amplitude cancels algebraically, as
in section4. All223 saved monomial intervals contain this reconstruction.
Every projected coefficient is then independently integrated by summing
each support interval separately, rather than first grouping its endpoint
sum as in the generator. All241 saved polynomial complex rectangles
contain these new enclosures; conjugate directions are all checked.
The same inclusion holds after the independently bounded mode/transport
error is added, for every exact-trial rectangle. Saved inflation amounts
and component widths are also checked with exact rational arithmetic.
This inclusion is stronger than overlapping enclosures. Its force comes
from the proved interval constructions and analytic error bounds, not
from numerical agreement alone.

The complete audit records224 operator entries,896 pivots,224 normalized
coordinates,226 residual coordinates,223 polynomial coefficients and241
complex projected coefficients. The maximum stored component radius is
less than1.275818e-91<1.276e-91<1e-65. All checks pass; no failure is hidden
or tolerance weakened. The JSON binds the input certificate and audit
script by SHA256 and checks the original generator/interval-source hashes.
Full reconstructed intervals and all decisions are retained there.

This establishes local verification of the existing specialization and
its advertised bounds; it adds no stronger prolate estimate or theorem
beyond the inspected source methods. The original96-mode failures remain
unchanged. No boundary division or relative1/10 observable test was made
in this audit. The independent gaps listed in the conclusion remain.

## Mathlib

Full matching coverage and supporting spectral/Legendre/interval results
were not checked. Unknown coverage is not absence. No Mathlib theorem
or numerical verification of zeta zeros is an input to this certificate.
