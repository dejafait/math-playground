# C744d: The coarse complete-compression enclosure admits a negative artificial member

## Hypotheses

Fix exactly C744b's ell=log(3)/2, a=5log(3)/4, penalty 256,
orthonormal even basis e_0^+,...,e_63^+, nine active prime powers
2,3,4,5,7,8,9,11,13, and ten physical moments. The complete form is
L744 (6)'s semibounded smooth form closure, with C744c's centering
and parity conventions; no generator-domain assertion is made.
Let V be this complex 64-dimensional span. Reuse the accepted step457
C744b individual diagonal intervals (harmonic cutoff 100000, digamma
prefix 8192), with their actual uncertainties. Evaluate responses
0<=j<2048 individually and retain every omitted response as below.

The imported arbitrary-a smooth identity is Hongmin Li,
*Cutoff-free positivity of localized Weil forms through the (log 11)/2
threshold*, [paper45 displayed v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma 3.1 and (2.1)-(2.5). The cutoff method is
[Suzuki, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3#S3),
Section 3.2, (3.2)-(3.4). C744c's accepted step461 audit verifies their
local normalizations, both cutoff limits and bounded complex response
map. Their numerical sign claims are not inputs. The numerical
contracts are directed basic arithmetic, correctly rounded exp/ln/sqrt
and adjacent-number widening in the
[Python Decimal documentation](https://docs.python.org/3/library/decimal.html),
and C744b's explicit Machin/Taylor remainders. This is REPRODUCTION
under the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-complete-compression-461.md`.
No conditional assertion of L742 or inaccessible artifact is used.

## Conclusion

The calculation constructs an interval enclosure of the complete
compression on V, retaining all moments and responses. Its physical
sign is **unresolved**. For the exact response-prefix matrix P and
the exact complete compression M, it proves

\[
 M=P+T,\qquad 0\le T\le\tau I,\qquad \tau<0.011294. \tag{1}
\]

An interval LDL attempt certifies ten pivots only; the next enclosure
contains zero. The independent entrywise interval box admits an exactly
specified rational symmetric matrix A_* and nonzero dyadic vector z with

\[
 -5.40072057\,10^{-10}<z^TA_*z<-5.40072056\,10^{-10}<0. \tag{2}
\]

A_* is an **artificial box member**, not the physical compression.
Thus universal positivity of all members of this coarse box is false.
This stops this coarse interval-only certificate, not the complete
penalty-256 comparison itself. No actual negative complete direction,
positive complete eigenvalue, neutral sign, complement sign, all-window
result or RH consequence follows. This numerical-method obstruction
has not received a separate later audit; it is not a new sign theorem
beyond the inspected sources.

## Proof

### Finite-span applicability and matrix normalization

C744c's cutoff argument applies to every fixed element of V, including
complex coefficients. A finite cosine sum and its derivative are bounded
and smooth, and its even full-interval extension is smooth at zero.
With the same real even interior cutoff chi_e, its removed collar has
L1 norm O_v(e) and zero-extended total variation O_v(1), including both
endpoint jumps. Its Fourier transform is O_v(min(e,1/|xi|)), giving
logarithmic Fourier norm squared O_v(e log(1/e)). The half-interval
removed cosine coefficients are O_v(min(e,1/q)), with constant
coefficient O_v(e), so the shifted diagonal form norm also tends to
zero by the same series split. Real and imaginary parts obey these
estimates separately. C744c's bounded response map is already on complex
L2; the finite delay, pole and moment maps are bounded. The smooth
identity therefore passes to the limit for each v in V. No assertion
of zero-extension H1 membership or equality of whole domains is needed.
Polarization identifies the finite Hermitian matrix.

Put k_q=q*pi/a, n_0=a^(-1/2), n_q=(2/a)^(1/2) for q>=1. C744b's
exact integration formulas (8)-(10), applied to basis pairs, give

\[
 M_{rs}=\delta_{rs}h(k_r)+(B_p)_{rs}+p_rp_s
  +256\sum_{j=0}^4\sum_{\sigma=\pm1}m_{j\sigma,r}m_{j\sigma,s}
  +\sum_{j\ge0}b_{jr}b_{js},\qquad
 b_{jq}=\frac{n_q(-1)^q c_j\sqrt{1-e^{-2ac_j}}}{c_j^2+k_q^2},
 \quad c_j=2j+\tfrac12.                              \tag{3}
\]

Here p_q=e^(a/2)sqrt(1-e^(-a))b_(0q). Physical moment rows m include
n_q/sqrt(2), because they integrate the full-interval even function.
For d=log(n), b=a-d/2, an arithmetic pair entry is -2log(p)/sqrt(n)
times n_rn_s/2 times

\[
 S_d(k_r-k_s)\cos((k_r+k_s)d/2)
 +S_d(k_r+k_s)\cos((k_r-k_s)d/2),
 \quad S_d(t)=\begin{cases}\sin(tb)/t&t\ne0,\\b&t=0.\end{cases}
\]

Use all nine n and base primes p in C744b's list. A moment row is
n_q/sqrt(2) times the endpoint difference of
e^(beta(x-t_j))(beta cos(k_q x)+k_q sin(k_q x))/(beta^2+k_q^2),
at t_j+-ell/2, beta=sigma/2. These formulas include r=s, r=s=0
and the constant moment, without a nonconstant-mode limiting shortcut.
All entries are real symmetric; for complex x+iy the value is
x^TMx+y^TMy. A real positive-definite certificate would suffice on V.

### Entire response remainder

For all q,j, |b_jq|<=n_q/c_j, without any c_j>k_q assumption.
For N=2048, c_N=4096.5, decreasing-function comparison yields
sum_(j>=N)c_j^(-2)<=U_2:=c_N^(-2)+(2c_N)^(-1).
Cauchy-Schwarz gives, for every complex z,
sum_(j>=N)|sum_q z_q b_jq|^2 <= ||z||^2 sum_q n_q^2 U_2.
The squared projections give the lower bound zero. Thus (1) holds
with tau=(127/a)U_2. This is a uniform matrix bound, not C744c's
witness-specific cancellation estimate. Each mixed tail entry has
sign (-1)^(r+s) and magnitude <=n_rn_s U_2. Use [0,n_rn_s U_2]
when r+s is even and [-n_rn_s U_2,0] otherwise. No omitted physical
response is asserted to vanish.

### Directed calculation and actual error threshold

Reproduction commands, relative to this notebook:

```sh
python3 scripts/five-cell-penalty/compression-463.py
python3 scripts/five-cell-penalty/check-compression-463.py
```

The first program checks the SHA256 hashes of the unchanged interval
source and accepted C744b certificate against step457, reads all 64
diagonal intervals, and assembles all nine arithmetic matrices, ten
moment rows, the pole and 2048 response rows. Full evidence is in
`scripts/five-cell-penalty/compression-463.json`: all component matrices,
each response row, P's enclosure, every complete entry enclosure,
remainder constants, partial LDL factors and pivots. Old artifacts
are preserved. It uses the assessed 70-digit outward arithmetic and
no floating special-function value or source sign certificate.

The LDL recurrences are d_j=P_jj-sum_(k<j)l_jk^2 d_k and
l_ij=(P_ij-sum_(k<j)l_ik l_jk d_k)/d_j, with l_jj=1.
Interval inclusion and positive pivot lower endpoints justify each
division: by induction every exact pivot and factor lies in its saved
interval. If all 64 succeeded, the recurrences would give
P=L diag(d_j)L^T with unit triangular, hence invertible, L and positive
d_j, proving P>0. Ten succeed. At
zero-based index 10, the exact saved interval straddles zero and lies
inside [-0.001478762,0.001421936]. No later division is made.
A failed interval pivot alone is no negative certificate.

Actual bounds are: maximum accepted diagonal width <9.460944e-9,
prefix entry half-width row-sum bound <4.730472e-9, and
tau<0.011293233. None supplies a positive sign margin. The required
threshold was 64 positive interval pivots, or a strictly negative
actual complete directional upper enclosure. Neither was obtained.
The accepted C744c positive scalar intersects the reconstructed full
enclosure, a consistency check that does not determine a matrix sign.

### Exact enclosure insufficiency and its qualification

Write [P^-_rs,P^+_rs] for the exact finite-decimal endpoints of the
saved prefix matrix. Define (A_*)_rr=P^-_rr and
(A_*)_rs=(P^-_rs+P^+_rs)/2 for r!=s. This is an exact rational
symmetric member of the independent prefix box, hence also of the
complete box whose tail intervals contain zero. It is admitted by
the relaxation 'prefix box plus 0<=T<=tau I', taking T=0.
This relaxation does not enforce shared analytic correlations:
A_* need not equal any physical matrix.

The checker's floating proposal is frozen as integers divided by 2^44;
all subsequent norm, energy, membership and recurrence tests are exact
Fraction arithmetic. The ordered integer coordinates are

```text
-3156075698, -48287561532, -235508472256, -14547060069,
-986260099505, -1450893252061, 386526990493, -2163977902649,
1303249645913, 266530787696, 1556569891230, -279347514227,
511380732571, 1377692155778, -991451984913, 81823494753,
-1343718007144, 745577557445, 280944533654, -591006184718,
-12549919044864, 227126844596, -3603861078258, -3051133700210,
9044181007530, -3576896162661, 326509630594, -2885919655041,
-2646679636477, 649710621980, -615799117123, 550217563032,
-552033836043, -46937872856, -66839304231, 95225601321,
44808356777, -3271802681, 10011128487, 7053206060,
13150426745, -3284846845, -641330598, -1539715569,
1235839011, -691545451, 103331532, 214911406,
446035532, 27534382, -8627545, 58953093,
-19045878, -9298255, -10089670, 59343703,
-20631553, 10750611, -18710500, 4358653,
-28647242, 14572169, -12674199, 10404470
```

Its norm squared is exactly
309485009821349642983316483/309485009821345068724781056>0.
Summing all 4096 rational products gives an energy strictly between
-540072057/10^18 and -540072056/10^18, proving (2). Every matrix
membership and every saved LDL recurrence, including each division's
outward containment, is checked. All 12889 checks pass, with no failures.
The exact energy, norm, integer vector, input hash and checks are in
`scripts/five-cell-penalty/compression-checks-463.json`.
No floating eigenvalue sign is used in this proof.

Thus an interval-only proof that all matrices in this enclosure are
positive is impossible. It does not imply M<0 in any direction;
z is not asserted neutral. This coarse implementation stops without
changing a, penalty, basis, moments or the form. Further work needs
sharper complete-response/diagonal data or preserved correlations;
another solver applied to the same box cannot prove universal positivity.

## Mathlib

Full matching coverage of this finite compression, smooth-closure
specialization and numerical insufficiency certificate has not been
checked. No absence claim or formal verification is made. The source
identity, cutoff method, interval arithmetic and finite-matrix criteria
are known methods; no new general positivity theorem is claimed.
