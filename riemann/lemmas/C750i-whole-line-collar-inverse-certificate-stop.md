# C750i: The whole-line collar-mass inverse certificate cannot pay prime97/8

## Hypotheses

Set a=9/4, b=log(101)/2, r=(a/b)log97, w=2a-r and
k=2log97/sqrt97. Let I_L=(-a,-a+w), I_R=(a-w,a), E=I_L union I_R.
Use complex Lebesgue L2 spaces, zero extensions, and

    F_f(t)=integral f(x)exp(-itx)dx,
    J[f]=(1/(2pi))integral log(2+|t|)|F_f(t)|²dt,
    D={f in L2(R): J[f]<infinity},
    D_a={f in D: f=0 almost everywhere outside (-a,a)},
    C_f(s)=integral f(x+s)conj(f(x))dx,
    (U_b f)(x)=sqrt(a/b)f(ax/b).

These are the unchanged conventions of assessment1140 and C750h;
neither C750h's pulse bound nor C750f/C750g's sign conclusions are
mathematical premises. No parity, neutrality or nullvector is imposed.
Put ell(t)=log(2+|t|), mu(t)=1/ell(t). On L2(R), let M be the
self-adjoint Fourier multiplier ell, using the unitary transform
F/sqrt(2pi). Let R_E be restriction to E, R_E* zero extension, and

    B=R_E M^(-1) R_E* : L2(E) -> L2(E).

Computer-assisted bounds assume installed MPFR4.2.2, Python integers
and ctypes implement their documented arithmetic/ABI semantics.
Directed rounding is as in the [MPFR manual, Section4.4](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Rounding).
Correctness audit1146 below reviews the analytic reduction, arithmetic
implementation and fixed-grid replay. This is an informal
computer-assisted certificate, conditional on the stated platform
semantics, not a formal verification of MPFR or Python.

## Conclusion

For every f in D_a, a sufficient bound for the proposed allocation is

    k|C_(U_b f)(log97)| <= (k/2)||B|| J[f].              (1)

The fixed certificate criterion is therefore ||B||<=1/(4k). However,
rigorous complete-frequency bounds give

    1/(4k) < 0.269112,
    0.29256024 < ||B|| < 1.014420,
    ||B||-1/(4k) > 0.02344876.                         (2)

In particular this sufficient whole-line collar-mass criterion fails.
Its best possible right-side coefficient k||B||/2 exceeds0.13589175,
whereas the required coefficient is0.125. Refining quadrature or a
kernel approximation cannot make this particular criterion pass.

This does not refute the original inequality k|C_(U_b f)(log97)|<=J[f]/8
on D_a. No violating original-domain witness is produced. Restricting
the numerator to total collar mass and relaxing the support in the
inverse are substantive losses. This is a local negative computation
under an EXPLORE assessment, not certified originality or RH progress.

## Proof

### Closed forms, complex scope and the sufficient relaxation

Use the spectral/functional calculus in Gerald Teschl, *Mathematical
Methods in Quantum Mechanics*, online GSM99 edition,
[Theorem2.13 and Theorems3.1-3.2, domain(3.25)](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
pp71-72 and90-92. These are standard imported inputs; the following
identifies their domain here, rather than claiming a new abstract
operator theorem. Multiplication by positive real ell on its maximal
weighted domain is self-adjoint, and M^(-1), M^(-1/2) are bounded since
ell>=log2>0. Its form domain is exactly D, with J[f]=||M^(1/2)f||².

For clarity the form is closed directly: a J-Cauchy sequence has
Fourier transforms Cauchy in L2(ell(t)dt); its limit is also its
unweighted L2 limit because ell>=log2. Thus the sequence converges
in D. Support in (-a,a) is closed under L2 convergence, hence D_a is
closed in this form norm. Zero-extended C_c^infinity(-a,a) lies in D_a
and is dense in L2(-a,a). No unproved identification of the supported
operator's inverse is needed or asserted.

For f in D, set v=M^(1/2)f. Then f=M^(-1/2)v and

    ||R_E f||² <= ||R_E M^(-1/2)||² ||v||² = ||B|| J[f]. (3)

The last equality is the Hilbert-space identity ||A||²=||AA*||.
It applies to bounded operators between complex Hilbert spaces.
B is bounded, positive and self-adjoint. In fact ||B|| is the best
constant in(3) when f ranges over the whole-line domain D, since
M^(1/2):D -> L2(R) is onto. We do not assert it is the best constant
when f is restricted to D_a.

The directed geometry checks below give 0<w<a and r>w. For supported
f, C_f(r) is exactly the pairing from I_L to I_R. Cauchy-Schwarz
and 2uv<=u²+v² therefore give

    |C_f(r)| <= (1/2)integral_E |f|².

Changing variables y=ax/b proves C_(U_b f)(log97)=C_f(r), with no
extra normalization factor. Combining this identity with(3) gives(1)
for arbitrary complex f. No compression/inversion commutation,
Birman-Schwinger eigenvalue argument or unknown complete-Weil floor
has entered.

### One fixed cutoff and finite kernel with all operator errors

The working checkpoint fixed T=256 and h=1/64 before evaluation.
There are N=T/h=16384 frequency cells, with t_j=(j+1/2)h,
0<=j<N. Write

    K_T(z)=(1/pi)integral_0^T mu(t)cos(tz)dt,
    K_N(z)=(h/pi)sum_(j=0)^(N-1) mu(t_j)cos(t_j z),
    S=h sum_j mu(t_j),
    epsilon_K=(h/pi)[mu(0)-mu(T)+a*S].                  (4)

On each frequency cell, use the monotonicity of mu to bound the
integral of |mu(t)-mu(t_j)| by h times that cell's total variation.
For its cosine factor, |cos(tz)-cos(t_j z)|<=|z|h/2.
Summing the cells and using |z|<=2a yields

    |K_T(z)-K_N(z)| <= epsilon_K.                       (5)

This is a uniform absolute error, not a pointwise sample assertion.
On L2(E), the kernel error operator has norm <=2w*epsilon_K by
Schur's criterion (Teschl, same book, Lemma0.32/proof, pp28-29).
The hypotheses are satisfied because the bounded kernels are on a
finite-measure set and both absolute row and column integrals have
this bound. Finite-frequency convolution represents the restricted
multiplier by Fubini, since supported L2 inputs are L1.

The omitted whole-line frequency multiplier mu(t)1_(|t|>T) has norm
mu(T) by functional calculus. Restriction/extension are contractions,
so its compression has norm at most mu(T), including every discarded
frequency. This is an operator-norm tail, not a Fourier cutoff used
as the full inverse.

For all z, |K_N(z)|<=S/pi. For z!=0, integration by parts, using
mu'<=0, gives

    |K_T(z)| <= [mu(T)+integral_0^T |mu'(t)|dt]/(pi|z|)
               =mu(0)/(pi|z|).

The two collars' cross distances are at least d=r-w>0. Thus K_N
has cross-block bound mu(0)/(pi*d)+epsilon_K. Each collar has length
w. Schur's criterion consequently gives the complete upper bound

    ||B|| <= mu(T)
              + w[S/pi+mu(0)/(pi*d)+epsilon_K]
              + 2w*epsilon_K =: U.                    (6)

Both collar blocks and their off-diagonal interaction are retained;
no cross block is set to zero. This estimate allows arbitrary complex
inputs and all phases. The large absolute kernel error makes(6)
loose, but it is an upper certificate on the required full domain.

### Discriminating lower information for the same inverse compression

Let g=1_(I_L)/sqrt(w) in L2(E), so ||g||=1. Positivity implies
||B||>=<Bg,g>. Translation contributes only a Fourier phase; hence

    <Bg,g>=(4/(pi*w))integral_0^infinity
              sin²(wt/2)/(t² log(2+t))dt.              (7)

This is a test of B, not a trial eigenvalue used as an upper bound.
Its use of only I_L is legitimate lower information about the full
B; no off-diagonal block is omitted from the upper proof.

Evaluate(7) on the same [0,T] using composite Simpson quadrature,
mesh h=1/64, with its removable value w/(pi log2) at zero. To justify
the error use NIST DLMF, [Section3.5(ii), equations3.5.6-3.5.8](https://dlmf.nist.gov/3.5.ii):
for a C^4 integrand and an even number of mesh intervals the absolute
error is at most T*h^4*sup|V''''|/180. Here put A_0=1/log2 and,
for1<=n<=4, define

    A_n=(1/log2)sum_(j=1)^n binom(n,j)(j-1)! A_(n-j)/2^j.

Differentiating mu(t)log(2+t)=1 inductively proves |mu^(n)(t)|<=A_n
for all t>=0. The normalized single-interval Fourier square Q obeys
|Q^(n)(t)|<=w^(n+1): differentiate its double integral over I_L²,
where |x-y|<=w. Thus the density V in(7) satisfies

    |V''''(t)| <= (w/pi)sum_(j=0)^4 binom(4,j)A_j*w^(4-j)=:M_4.

All differentiated integrals are over bounded intervals, so domination
is immediate. The composite Simpson error is at most T*h^4*M_4/180.
The nonnegative omitted tail in(7) is at most

    4/(pi*w*T*log(2+T)),                                (8)

by sin²<=1 and mu(t)<=mu(T) for t>=T. For the lower bound it is
simply discarded in the favorable direction; it is added in full
for the upper endpoint of the Rayleigh enclosure. No unknown sign
or missing oscillation is used.

### Directed computation and the failed tests

Run from this notebook:

    python3 scripts/prime-collar/certify_1144.py

The full reproducible evidence is
[scripts/prime-collar/certificate-1144.json](../scripts/prime-collar/certificate-1144.json).
The implementation uses the previously audited interval backend in
scripts/pivot-area/certify_1136.py, without modifying it. Both source
hashes, MPFR version and precision384 are recorded. Every arithmetic
endpoint is directed; products take four endpoint extrema, squares
use absolute endpoints, and trig values are widened by the entire
argument interval width using the derivative bound1. Decimal output
is rounded outward again. Binary64 appears only in console display.
The certificate retains cumulative outward sums every1024 cells,
all derivative bounds and every frequency/kernel remainder.

Outward weakenings of the complete endpoints, inspected in full, are

    Simpson error < 2.657925e-8,
    0.2925602441470644 < <Bg,g> < 0.3152920166028328,
    epsilon_K < 0.675793334,
    mu(T) < 0.180084149,
    U < 1.014419622,
    1/(4k) < 0.2691114763335869,
    lower_bound - 1/(4k) > 0.0234487678134775,
    (k/2)*lower_bound > 0.1358917539178126.

These imply(2). The code verifies the weaker robust comparisons
lower_bound>0.29, threshold<0.27, miss>0.023, U<1.02 and Simpson
error<10^(-6), as well as the exact interval threshold comparison.
All verification assertions pass. The mathematical allocation test
fails, as explicitly recorded in `failed_tests`; this is the outcome,
not a verification success for the allocation.

The initial extra expectation U<1 also failed. Its complete first
certificate is preserved in scripts/prime-collar/certificate-1144-initial.json;
no mesh, cutoff or mathematical estimate was tuned. The final code
labels that nonessential failure explicitly and checks the valid
weaker display bound U<1.02. The decisive lower obstruction is
unchanged. A smaller approximation error cannot overcome that lower
bound, so this certificate is parked without a refinement search.

The exact supported allocation, all-support/sector budgets,
J-to-baseline comparison, old-shift and pole/digamma costs, and
actual-Xi realization at L030-L032/C032a remain unresolved.

### Correctness audit1146 — 16 November2026

The separate audit used the approved source comparison1145. It confirms
the stated obstruction, with no change of domain, cutoff, mesh or
threshold. It reproduces and verifies1144; no new norm inequality or
progress beyond the checked mathematics is claimed.

For the domain check, ell>=log2 makes the form norm equivalent to the
usual graph-form norm. Supported L2 convergence preserves zero
extension almost everywhere; endpoints have measure zero. The complex
form is closed and densely defined on the supported L2 space, while
the actual estimate uses only the explicitly defined whole-line M.
The range of M^(-1/2) is D, and M^(1/2):D->L2 is onto, so the sharp
whole-line mass constant is indeed ||B||. Cauchy-Schwarz pairs the
two disjoint collars, and the dilation cancels its Jacobian against
the squared normalization factor. The resulting factor is1/2, not1.
This justifies the threshold1/(4k) without assuming the desired
supported allocation or a spectral floor for the complete Weil form.

For the upper estimate, the cutoff convolution is justified for
zero-extended L2(E) inputs by finite measure and finite frequency
range. The midpoint variation error telescopes over all16384 cells;
the cosine error uses the full separation2a. Each row and each column
has one self-collar contribution and one cross-collar contribution.
Their cross separation is r-w>0. Integration by parts has a zero
lower boundary term because sin0=0 and total variation mu(0)-mu(T).
Adding2w*epsilon_K and the compressed high-frequency multiplier norm
mu(T) accounts for the entire operator remainder. Both blocks and
arbitrary complex phases are covered.

For the lower estimate, ||g||=1, and Plancherel supplies exactly the
density in(7). In detail, write

    Q(t)=|F_g(t)|²=(1/w) integral_(I_L²) exp(-it(x-y)) dx dy.

For real t, differentiation of this double integral gives
|Q^(n)(t)|<=w^(n+1). Thus
V(t)=mu(t)Q(t)/pi is C^4 on[0,T], including its removable zero.
Differentiating mu(t)log(2+t)=1 gives, for n>=1,

    |mu^(n)(t)| <= (1/log2) sum_(j=1)^n
        binom(n,j)(j-1)! A_(n-j)/2^j = A_n.

The product rule proves the displayed M_4. The16384 Simpson intervals
are even; the error and tail signs in(7)-(8) are correct. Positivity
permits discarding the omitted tail for the lower bound, without
assuming a supported original-domain witness.

The complete backend functions used here were reviewed: decimal
inputs are rounded in both directions; addition and negation use the
appropriate endpoints; multiplication takes all four endpoint extrema;
division rejects a zero-crossing denominator before taking its
reciprocal; powers use outward products. The only monotone unary
functions used are log and sqrt on positive intervals. Trig evaluation
at the exact binary lower endpoint is widened by the full argument
width, using the global derivative bound1; absolute value followed by
endpoint squaring encloses sin² even across zero. All numerical inputs
in this invocation are integers or MPFR intervals, not binary64
constants. mpfr_get_str's directed105-significant-digit conversion
and the decimal exponent assembly preserve outward containment; see
[MPFR4.2.2 Sections4.4 and5.4](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Conversion-Functions).
Binary64 is confined to the original script's console rendering.

Reproduction command:

    python3 scripts/prime-collar/audit_1146.py

This executes unchanged certify_1144.py while redirecting its single
certificate write to scripts/prime-collar/certificate-1144-replay-1146.json.
Every JSON field, including all cumulative sums, matches the retained
original. All numeric enclosures and cumulative blocks also match the
initial certificate. Both original files remain byte-for-byte unchanged.
The explicit header/library probe in scripts/prime-collar/abi_1146.c
checks the installed MPFR ABI against ctypes: struct size32, field
offsets0,8,16,24, component sizes8,4,8,8, rounding RNDD=3/RNDU=2,
precision384, and matching header/runtime version4.2.2. The source hashes
match the retained certificate. This is a platform/implementation
check under the stated semantics, not a proof of those semantics.

All36 audit checks pass. The complete audit record is
[scripts/prime-collar/certificate-audit-1146.json](../scripts/prime-collar/certificate-audit-1146.json).
It verifies every displayed numerical weakening above by exact rational
comparison of the complete outward decimal endpoints, including
lower_bound>threshold, the miss>0.02344876 and the allocation
coefficient>0.13589175. Selected complete derivative, geometry, kernel,
tail and decisive endpoint values were inspected in addition to replay;
no preview or rounded eigenvalue is used as proof. The failed allocation
and initial nonessential U<1 test are preserved. The fixed sufficient
certificate is therefore stopped reliably. The original supported
correlation inequality and all actual-Xi obligations remain undecided.

## Mathlib

Full matching coverage was not checked. Plancherel, positive Fourier
multipliers, complex Hilbert adjoints, Schur's kernel test, elementary
interval geometry and Simpson's error estimate are supporting inputs.
No matching theorem name, Lean verification, or absence from Mathlib
is asserted. Abstract functional calculus and Schur bounds are imported
by the precise primary citations above; only their stated-domain
specialization and the fixed numerical obstruction are supplied here.
