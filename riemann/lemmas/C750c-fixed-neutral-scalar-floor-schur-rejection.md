# C750c: The fixed neutral six-mode scalar-floor certificate fails

## Hypotheses

Let T=4log3 and I=(0,T). Use C750a's exact smooth cutoff chi,
delta=T/40, and phi_k(x)=chi(x)sin(k*pi*x/T), extended by zero.
Use the complete Hermitian form Q whose quadratic form E is L744(6):

    E(f)=integral_R m(t)|F_f(t)|^2 dt/(2pi)
         +2Re(M_+(f)conj(M_-(f)))
         -2 sum_(2<=n<81) Lambda(n)/sqrt(n) Re R_f(log n),
    m(t)=Re psi(1/4+it/2)-log pi,
    F_f(t)=integral f(x)exp(-itx)dx,
    M_sigma(f)=integral_I exp(sigma*x/2)f(x)dx,
    R_f(u)=integral f(x+u)conj(f(x))dx.                    (1)

The inner product and Q are linear in their first argument. All31
prime powers below81 are retained. The delay at81 has zero overlap.
Let H be the closed common L2 kernel of M_+,M_- on I, and set

    U_j=span_C{phi_1,...,phi_j} intersect H (j=6,12),
    V=U_6, W=H intersect V-perp, Z=U_12 intersect V-perp. (2)

The form domain on H consists of supported zero extensions with
integral log(2+|t|)|F_f(t)|^2 dt finite. Formula(1) defines it without
assuming positivity or extending L741's smaller-window theorem.
The form is well-defined: L744(8) bounds |m| by a logarithmic weight,
the moments are bounded L2 functionals, and all shifts are bounded.

The scalar-floor certificate under test requires a d>0 such that
E(w)>=d||w||^2 on the entire complementary form domain, and then
nonnegativity of E(v)-K(v)/d on every v in V. Here K(v) is the squared
L2 norm of the COMPLETE W cross representer proved below. Paying an
upper covariance bound in place of K can only lower that certificate.
This is the scalar-floor sufficient comparison, not the exact
Schur complement with the complementary operator inverse.

Import the conditional comparison from Andrews--Connes--La Gatta,
*The uncertainty operator, the Weil ground state and the zeros of zeta*,
[2611.13129v1](https://arxiv.org/html/2611.13129v1#S8.SS6), Lemma8.16,
and Hongmin Li, *Cutoff-free positivity of localized Weil forms through
the (log11)/2 threshold*, [paper45/v2](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Sections4-5, (4.7)-(5.5). Complex finite-block order is covered by
Gallier,24August2019, [Propositions2.1-2.2, pp3-4](https://www.cis.upenn.edu/~jean/schur-comp.pdf),
and Dritschel--Rovnyak, [0903.3639v1](https://arxiv.org/pdf/0903.3639v1),
AppendixA LemmaA.1, pp28-29. These are method inputs, not positive-floor
or sign inputs. Assessment870, approved before this attempt, covers
the exact scope. The rejection implication is specialized below.

Numerics assume IEEE binary64, outward nextafter arithmetic, no
fast-math and no floating contraction. Reuse L750 Proof3-4's audited
elementary enclosures, real Simpson bounds, interpolation and complete
periodization estimates. Scalar identities are
[DLMF5.5.2](https://dlmf.nist.gov/5.5.E2),
[5.11.2](https://dlmf.nist.gov/5.11.E2), and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii);
the smooth difference representation is L750(8), from
[DLMF5.9.16](https://dlmf.nist.gov/5.9.E16), Re(z)>0.
No external numerical certificate is imported.

## Conclusion

There exist exact real v in V and nonzero real y,z in Z with

    E(v)<7/500, ||y||^2<1, Q(v,y)>9/250,
    ||z||^2>99/100, E(z)/||z||^2<1/1000.                 (3)

Consequently, for every possible strictly positive complementary floor d,

    E(v)-K(v)/d < -641/500 < -32/25 <0.                 (4)

Thus no scalar-floor Schur certificate of the stated family can work
for V. The finite compression alone rejects it: K may be replaced in
(4) by the finite covariance ||P_Z h_v||^2, where h_v is the complete
cross representer. Neither a complete covariance upper computation
nor an infinite complementary floor is needed for this rejection.

This is a REPRODUCTION/known-method specialization and a local route
stop, not a discovery beyond the assessed sources. The separate
conceptual audit873 below accepts (3)-(4) under the stated arithmetic
model. No negative E(z),
negative complete finite form, failure of exact inverse Schur theory,
full Weil positivity, Xi realization or RH conclusion is asserted.

## Proof

### 1. Exact dimensions, moments and L2 projections

All phi_k are real, smooth and compactly supported inside I. Their
sines are independent on the open plateau where chi=1, hence the
first j functions have dimension j. Reflection gives

    phi_k(T-x)=(-1)^(k+1)phi_k(x),
    M_-(phi_k)=(-1)^(k+1)exp(-T/2)M_+(phi_k).            (5)

M_+(phi_1)>0. Also M_+(phi_2)<0: on(0,T/2), phi_2>=0 and is
positive on an interval, whereas exp(x/2)-exp((T-x)/2)<0. Pairing
reflected points proves the strict inequality. Thus the two moment
rows have rank two on both spans, so dim V=4, dim U_12=10 and dim Z=6.
These are complex dimensions; both moment constraints are complex linear.

Write mu_k=M_+(phi_k), and, for even k=4,6,8,10,12, put

    b_k=phi_k-(mu_k/mu_2)phi_2.                          (6)

They have both moments zero EXACTLY by(5), and are antisymmetric
about T/2. The antisymmetric part of V is span{b_4,b_6}; its symmetric
part is spanned by phi_k-(mu_k/mu_1)phi_1, k=3,5. These parts are
L2 orthogonal, including for complex coefficients.

Define exact real trials

    v=(23 b_4+58 b_6)/100,
    r_z=(38 b_8-52 b_10+19 b_12)/100,
    r_y=(32 b_8+42 b_10+50 b_12)/100,
    z=r_z-P_V r_z, y=r_y-P_V r_y.                        (7)

These rational coefficients were selected from a floating preview;
that preview supplies no bound. Let H_ab=<b_a,b_b>, a,b in{4,6}.
Its determinant is positive because b_4,b_6 are independent. For
either real r in(7), write p=(<r,b_4>,<r,b_6>)^t. Its exact
projection has coefficients H^(-1)p. Orthogonality to the symmetric
part is automatic by reflection. Therefore z,y belong to Z, without
defining an approximate nullspace or approximate projection. Their
nonzero norms follow also from(3). v is nonzero by independence.
All three trials and v+y remain smooth compactly supported and neutral.

### 2. Complete representability and direction of the rejection

For every v_0 in V, its full-line Fourier transform is Schwartz.
The logarithmic bound L744(8) therefore gives m F_(v_0) in L2, an
operator-domain fact stronger than finite form norm. Let r_(v_0) be
the restriction to I of its inverse Fourier transform, minus

    B v_0=sum_(2<=n<81) Lambda(n)/sqrt(n)
                   [v_0(.+log n)+v_0(.-log n)].

Zero extension is used in both shifts. This is L2: restriction and
shifts are contractions and the sum is finite. For every neutral w
in the form domain, Plancherel and the finite shift identities give
Q(v_0,w)=<r_(v_0),w>. The Fourier pairing is absolutely convergent
by Cauchy--Schwarz on m F_(v_0) and F_w; the pole cross terms vanish
by the EXACT moments of v_0. This proves the identity on the entire
specified form domain, not only on the numerical span.

H and W are closed L2 spaces because the moments and finite projection
are continuous. Put h_(v_0)=P_W r_(v_0), K(v_0)=||h_(v_0)||^2.
Then Q(v_0,w)=<h_(v_0),w> on the W form domain, with the stipulated
complex conjugations. Bessel/Cauchy--Schwarz, using y in Z subset W,
give

    K(v)>=||P_Z h_v||^2>=|Q(v,y)|^2/||y||^2.             (8)

This is a LOWER covariance bound. No omitted covariance is treated
as an upper bound, and no L2 representability follows merely from
form-dual continuity.

Any valid floor d>0 must satisfy, using the nonzero z in Z subset W,

    0<d<=E(z)/||z||^2<1/1000.                           (9)

This conditional restriction is valid even though the enclosure of
E(z) below straddles zero: if E(z)<=0, no positive d exists at all.
If a d does exist, (3),(8),(9), positivity of d and monotonicity of
1/d yield

    E(v)-K(v)/d
      <=E(v)-|Q(v,y)|^2/(||y||^2 d)
      <7/500-(9/250)^2/(1/1000)
      =-641/500<-32/25.                                 (10)

The same inequality holds for the finite covariance in(8).
A real v suffices to refute positive semidefiniteness on the complex
retained space. No exact complementary inverse is identified with dI.

### 3. Full numerical enclosures and all error budgets

Reproduce from the notebook directory:

```sh
clang++ -O2 -std=c++17 -ffp-contract=off scripts/neutral-scalar-preflight/certificate-872.cpp -o /private/tmp/riemann-neutral-scalar-872
/private/tmp/riemann-neutral-scalar-872 > scripts/neutral-scalar-preflight/certificate-872.json
python3 scripts/neutral-scalar-preflight/check-872.py
```

The program includes the elementary outward implementation in
`scripts/corrected-ims/certificate-315.cpp`, renaming its old main,
which is never called. No old moment, norm, energy, or sign is used.
Its exp/log/trigonometric remainders are L750(9); all reduced sine/cosine
arguments here lie in[-4,4]. For the largest k=12 and derivative
panels, the phase width is less than .002; nearest-period reduction
leaves magnitude below pi+.002<4, including outward rounding.
Other phases are in[-pi,pi] or[0,pi/2].

First compute mu_(2j) and the6-by6 Gram of phi_2,...,phi_12 by
composite Simpson with65536 subintervals on[0,T]. The node values are
outward intervals; the C4 remainder is T h^4 D4/180, h=T/65536.
L750(11) gives theta derivative bounds(1,5,352,26000,3000000).
The two cutoff transitions are disjoint, so chi derivatives are
bounded by these numbers divided by delta^j (and chi itself by1).
The product rule with |(sin(k*pi*x/T))^(j)|<=(k*pi/T)^j supplies
phi derivative bounds. Product-rule bounds are applied to every
Gram entry and to exp(x/2)phi_k; the exponential derivatives are
bounded by9/2^j because exp(T/2)=9 exactly. Flat joins are C-infinity,
so the real Simpson theorem applies across them; complex analyticity
is not assumed. The exact integrals define(6)-(7); interval inverses
enclose them. In particular mu_2 lies in

    [-4.839816942482802,-4.8398167581194125].

The retained Gram determinant is checked positive by interval
arithmetic; the independent exact-dyadic checker also verifies it
from the complete saved moments and Gram. These computations enclose
the original L2 projection, not a coefficient-space Euclidean one.

For each of v,z,y,v+y let q be the linear interpolant of its EXACT
grid values on period P=64 with N=262144, step s=1/4096. Its support
has diameter<9 and is separated from the period endpoints after
periodic identification. The interval radix-two FFT encloses every
nodal DFT S_k, with outward roots of unity. Integrating the linear
hat gives F_q(2pi k/P)=s sinc(pi k/N)^2 S_k. The archimedean head
retains k=0 and both signs through N/2, including both Nyquist terms.
The digamma recurrence shifts by256 for frequency<512, then uses
the sector error <1/(4|z|^2), Re(z)>0; above512 it uses that bound
without a shift. Thus low frequencies and the full symbol are retained.

Write A0=2+8sqrt2/3+log(4pi), W0(t)=A0+log(2+|t|), R0=pi/s.
L750 Proof4, with these new functions and unchanged P, gives

    Fourier tail <= W0(R0)||q'||^2/R0^2,
    periodic images <=27||q||^2 exp(-55/2)/(1-exp(-32)).  (11)

The first follows from periodic derivative Parseval and decrease of
W0(t)/t^2; the second bounds every correlation image using support
diameter<9. It compares the periodic archimedean sum to the full-line
form, rather than assuming they agree.

The inverse FFT of |S_k|^2 encloses cyclic nodal correlations C_j.
Each prime delay uses the EXACT hat correlation

    R_q(u)=s sum_j C_j B3(u/s-j),
    B3(a)=2/3-a^2+|a|^3/2 (|a|<=1),
          (2-|a|)^3/6 (1<=|a|<=2), 0 otherwise.          (12)

Only the adjacent terms contribute; using five indices includes any
endpoint zeros. P>18 excludes image overlap for our delays. The
prime-power enumeration is exactly

    2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,
    31,32,37,41,43,47,49,53,59,61,64,67,71,73,79.

Every coefficient is log(p)/sqrt(n), n a power of p. There is no
infinite arithmetic remainder for supported trials.

Second-derivative interval jets on32768 entire panels of[0,T] give
B2>=||f''||^2, including flat joins and endpoints. The eta endpoint
jet bounds are those justified in L750 Proof3-4, with reciprocal
powers bounded by sup_(u>=1/a) u^j exp(-u); no division at zero
occurs. L750(19)-(21) then specialize to

    epsilon=s^4 B2, C0=A0+log3,
    EW=epsilon[C0+.5log(1+s^(-2))],
    QW=||q||^2[C0+.5log(1+||q'||^2/||q||^2)],
    interpolation error <=2sqrt(QW*EW)+EW
       +Cprime[2sqrt(||q||^2 epsilon)+epsilon],
    Cprime=2sum_(2<=n<81) Lambda(n)/sqrt(n)<30.698.        (13)

The interpolant norms and derivative norms are integrated exactly
on each segment. The estimates use the fundamental theorem of
calculus for interpolation, Jensen for the logarithmic weight, and
Cauchy--Schwarz for the energy difference. The auxiliary q need not
be neutral: only A(q)-B(q) is evaluated. Its pole product is never
declared zero. The assigned E(f) is for the EXACT neutral smooth f.

All head, prime, projection-coefficient and rounding uncertainties
are retained in intervals, then (11),(13) are added. Some rounded-UP
error budgets (not replacements for the signed heads) are:

| Trial | B2 upper | Fourier tail | Images | Interpolation error |
| --- | ---: | ---: | ---: | ---: |
| v | 9596 | .000002103 | 3.110e-11 | .000523438 |
| z | 2515 | .000005000 | 3.053e-11 | .000267124 |
| y | 70435 | .000009915 | 3.043e-11 | .001417977 |
| v+y | 129215 | .000014447 | 6.152e-11 | .002724890 |

Outward enlargements of the COMPLETE final enclosures are

    ||z||^2 in [.99167413,.99167425],
    ||y||^2 in [.98842939,.98842962],
    E(v) in [.01245010,.01363192],
    E(z) in [-.00050104,.00050574],
    E(y) in [.11960254,.12365196],
    E(v+y) in [.21007741,.21753302],
    Q(v,y) in [.03639676,.04274019].                     (14)

The last uses real polarization (E(v+y)-E(v)-E(y))/2, justified
because all functions and the kernels are real. Dividing the full
E(z) interval by the strictly positive norm interval yields upper
.000509983, below1/1000. Bounds(14) prove(3), with strict margins.
The implementation also uses its tighter positive Rayleigh upper
and norm bounds directly, giving scalar-comparison upper<-2.61436.
The simpler rational comparison(10) suffices.

The full certificate is `scripts/neutral-scalar-preflight/certificate-872.json`.
The independent rational checker reads all its endpoints as exact
binary64 dyadics, verifies energy-error accounting, polarization,
Rayleigh division, positive retained Gram determinant, exhaustive31
prime powers and the strict rational inequalities. Its19 checks pass;
full output is `scripts/neutral-scalar-preflight/check-872.json`.
This checker is not an independent FFT or elementary-function replay,
and does not replace a later conceptual audit. The preserved
`preview-872.py`/`preview-872.json` are explicitly UNVALIDATED and
are not mathematical evidence. No enclosure determines E(z)'s sign.

### 4. Independent conceptual audit, 14 November 2026, step873

This audit reuses the invocation-start SPECIALIZE assessment870 and
its exact scope. It accepts the existing rejection, not an unrestricted
positivity claim or a new result beyond the assessed literature. The
proof inputs remain L744(6)-(8), C750a's cutoff and L750 Proof3-4.

**Exact spaces and full-domain pairing.** Reflection multiplies the
two moment rows by the factors in (5). The strictly signed first and
second moments give two independent columns, including over C. Sine
independence on the plateau proves the dimensions, without inferring
rank from floating data. For each even neutral b_k the second moment
vanishes as a consequence of its first, because its reflection sign
is -1. Symmetric and antisymmetric functions are L2 orthogonal also
for complex coefficients. Thus the real two-by-two Gram projection
in (7) is the full V projection, with the original L2 metric.

The finite smooth space V lies in the multiplier's operator domain:
|m(t)|<=A0+log(2+|t|) and the Schwartz decay give m F_v in L2.
For any w in the specified logarithmic form domain, its pairing with
that function is absolutely integrable by Cauchy--Schwarz. The finite
shifts are bounded and have the adjoints used in B. Both pole cross
terms vanish from v's exact two moments. Consequently the represented
pairing is the complete Q(v,w), with the inner product linear in v;
there is no unsupported upgrade from form-dual to L2 continuity.
Projection to the closed space W preserves that pairing. The Riesz
representer need not itself belong to the form domain. The finite
projection onto Z and the test y give lower covariance bounds in (8).

Any asserted positive full floor can be tested on the exact z, forcing
(9). If E(z)<=0, no such floor exists; otherwise its value is still
less than .001. The strictly positive cross lower bound and ||y||²<1
then give (10). This conditional case split does not assign a sign to
E(z). A covariance upper bound would make the sufficient certificate
smaller, so cannot rescue it. No inverse complementary operator or
sign of the complete finite matrix is inferred from this calculation.

**Analytic error coverage.** Simpson is applied to real C4 functions
with an even number of subintervals. The disjoint cutoff transitions
justify the derivative bounds; exp(x/2)<=9 on the exact interval.
Uncertain nodes, T, moments and projection coefficients are enclosed
throughout. The second-derivative jets cover entire panels of [0,T],
including flat joins; the smooth trials vanish outside it. Only the
upper endpoint of each B2 field is an asserted bound for ||f''||².

Integrating the linear hats gives the continuous Fourier coefficients
at every integer frequency, including aliases. Real symmetry justifies
doubling the nonzero head, including the two distinct Nyquist terms.
Periodic derivative Parseval pays every omitted frequency by (11).
The digamma recurrence and right-half-plane sector remainder retain
all low frequencies. For the H1 interpolant, the nonnegative multiplier
difference formula L750(8) holds by Tonelli, on the line and on the
circle, with the derivative norm controlling u near zero. Their
correlation difference consists of images centered at jP, j>=1 for
u>0. The support diameter bound, k(u)<=3exp(-u/2) there, and
integral |R_q|<=9||q||² give the entire geometric image bound (11).
No extra negative-u factor is needed for this positive-u representation.

The interpolant support stays inside I: its enlargement beyond the
smooth support is at most s<delta. Thus the same31-delay bounded
operator applies to f and q. Inverse DFT normalization is 1/N; the
cubic hat correlation and all coefficients log(p)/sqrt(p^a) have
the factors in (12). Delay intervals remain in single grid cells, so
the five indices include every possible nonzero hat term. With P=64,
diameter<9 and delays<T<9, no arithmetic image overlaps.

On each grid cell, q' is the mean of f', giving both interpolation
bounds in L750(19) with constant one. Jensen applies to the full-line
Fourier probability measure; x[C0+.5log(1+y/x)] is increasing in
x,y>=0. The resulting weighted Cauchy--Schwarz and finite-delay
operator estimates are exactly (13). They compare A-B for q and f;
only the exact smooth neutral f is assigned E(f). No pole product of
q is declared zero. Polarization is real because the multiplier is
even and real and the shift operator preserves real functions.

**Implementation and exact accounting.** The audit driver
`scripts/neutral-scalar-preflight/audit-873.py` instruments a copy of
the current implementation; originals and previous outputs remain
unchanged. It checks finite ordered intervals, binary64 round-to-nearest
with subnormals, every elementary-function domain, the grid counts,
interpolant support, endpoint jet domains and all124 delay evaluations.
The inherited named-main return warning concerns an uncalled function;
its body contributes no result. The complete domain evidence is
`scripts/neutral-scalar-preflight/domains-873.json`:

    max reduced trigonometric modulus = 3.141976148788587 < 4,
    max arctangent modulus = .20000000000000007 < 1/4,
    max exponential base modulus = 1/8; log bases in [1,2],
    max delay interval width = 4.365574568510056e-10,
    min delay cell margin = .015691554055592857 > 0.

All14 inherited derivative/series checks replay identically. The
instrumented and unmodified numerical replays are identical to the
complete certificate872, not merely its previews. Exact rational
interval arithmetic independently reconstructs the moment-ratio
coordinates, the two-by-two original-metric projections and all three
norm enclosures from the saved moment and Gram endpoints. It checks
the interpolation upper bounds using rational square-root upper
enclosures, all four complete signed energy budgets, polarization,
Rayleigh division, exhaustive prime powers and the strict comparisons.
All37 checks pass in `scripts/neutral-scalar-preflight/audit-873.json`.
The tighter certificate comparison has upper -2.61436312224493<0;
the deliberately weaker rational bound -641/500<-32/25 suffices.

To reproduce while preserving earlier certificates:

```sh
clang++ -O2 -std=c++17 -ffp-contract=off scripts/neutral-scalar-preflight/certificate-872.cpp -o /private/tmp/riemann-neutral-scalar-audit-873
/private/tmp/riemann-neutral-scalar-audit-873 > scripts/neutral-scalar-preflight/replay-873.json 2> scripts/neutral-scalar-preflight/replay-873.log
python3 scripts/neutral-scalar-preflight/audit-873.py
```

The driver writes full instrumented, constants, domain and rational
audit certificates beside those files and prints the actual/required
bounds and failures. This is an instrumented replay plus independent
coordinate/accounting verification, not a second independent FFT
library or a formal proof of the compiler. Under the stated arithmetic
model, (3)-(4) and the stop for this scalar-floor family survive audit.
The E(z) enclosure still contains zero. The exact inverse Schur route,
other supports, non-neutral terms and actual-Xi assembly remain open.

### 5. Unfinished exact energy-block diagnostic, 14 November2026, step875

This bounded REPRODUCTION calculation uses the unchanged SPECIALIZE
assessment874, `drafts/literature/2026-11-14-neutral-exact-schur-compression-874.md`.
It records an inconclusive test of the exact U12 compression, not an
additional conclusion to (3)-(4). No complete positivity or negativity
claim is made. The scalar-floor rejection above remains audited;
this calculation has not received an independent conceptual audit.

Use the same exact chi, moments and spaces (1)-(2). For p=1,2 put

    b_(p,j)=phi_(p+2j)-[mu_(p+2j)/mu_p]phi_p, j=1,...,5,
    e_(p,1)=b_(p,1), e_(p,2)=b_(p,2),
    e_(p,j)=b_(p,j)-P_V b_(p,j), j=3,4,5.               (15)

The mu are exact integrals, not midpoint values. Proof1's reflection
identity applies to all twelve modes. The same strictly signed mu_1
and mu_2 justify each ratio. Each b has both complex moments exactly
zero. The first two b in each sector span that part of V; all five
span that part of U12 by sine independence on the plateau. Projecting
only onto the first two b in the SAME sector equals P_V: the other
sector is L2 orthogonal. Use exactly the two-by-two original L2 Gram
inverse from Proof1. It has strictly positive determinant by independence;
the new computation also encloses it positively in both sectors.
Projection preserves parity, so the last three e in each sector lie
in Z. The ten e are a basis: projecting the last six by subtracting
vectors in the first four is an invertible triangular basis change.
These statements remain true over C; they do not require numerical
rank or Euclidean coefficient-space orthogonality.

Here is the exact zero pattern needed to represent the FULL matrix.
Let Jf(x)=f(T-x), with zero extension. Its Fourier transform is
exp(-itT)F_f(-t). Since m is real and even, substitution t -> -t
proves Q_arch(Jf,Jg)=Q_arch(f,g). The finite symmetrized translation
operator B commutes with J, so Q_prime has the same invariance.
The two moments already vanish. Hence Q(Jf,Jg)=Q(f,g) on the neutral
space. Opposite reflection eigenvalues imply Q(f,g)=-Q(f,g)=0,
including for complex f,g. Real tests have real Q: the real even
Fourier multiplier and the real symmetrized shifts preserve real
functions, or conjugate their Fourier integrals under t -> -t.
Thus the complex Hermitian matrix is real symmetric and consists
of the two five-by-five sectors, with exact cross-sector zeros.
Within each sector set M_ij=Q(e_j,e_i), using the first-linear Q.
Then E(sum c_i e_i)=c* M c. For real basis vectors the recorded
polarization is M_ij=[E(e_i+e_j)-E(e_i)-E(e_j)]/2.

The first two coordinates in each sector belong to V, the last
three to Z. These are not asserted orthonormal. An invertible
basis change within V and Z is a block diagonal congruence, so the
finite Hermitian criterion applies directly to this coordinate
matrix, without replacing an energy block by an L2 Gram matrix.
Import the criterion, without reproof, from Takashi Sano,
*Moore-Penrose inverse, generalized Schur complement and inertia*,
2026, [Theorem2.6](https://link.springer.com/article/10.1007/s44146-026-00231-y#Sec2).
It requires G>=0, ker G subset ker B and A-B G^dagger B*>=0.
For a positive-definite G the kernel condition is vacuous and the
ordinary inverse suffices. The positive-definite elimination case is
also Gallier,24August2019,
[Propositions2.1-2.2, pp3-4](https://www.cis.upenn.edu/~jean/schur-comp.pdf).
These are the assessed abstract inputs, not sign inputs.

Reproduce the fixed calculation and its exact-rational accounting:

```sh
clang++ -O2 -std=c++17 -ffp-contract=off scripts/neutral-exact-schur/certificate-875.cpp -o /private/tmp/riemann-neutral-exact-schur-875
/private/tmp/riemann-neutral-exact-schur-875 > scripts/neutral-exact-schur/certificate-875.json 2> scripts/neutral-exact-schur/run-875.log
python3 scripts/neutral-exact-schur/check-875.py
```

`elementary-875.hpp` preserves the elementary interval methods of
L750 Proof3-4 with explicit finite/ordered-interval and elementary-domain
guards; no old numerical result or old main is used. The evaluator
specializes Proof3 above to all twelve phi_k, all moments and
same-parity Gram entries. Opposite-parity Gram entries are exactly
zero by reflection. Simpson uses65536 subintervals, with the same
T h^4 D4/180 remainder, derivative product rules and exp(x/2)<=9.
Exact ratio and projection coefficients are enclosed throughout.
All reduced trigonometric inputs are checked against4; logarithm,
exponential and arctangent base domains are checked as well. Binary64
round-to-nearest and preserved subnormals are required at runtime.

For each sector, five diagonal and ten sum energies are evaluated:
30 complete evaluations in total, without a mode/window/shift sweep.
The period64, N=262144,32768 entire derivative panels, exact hat
correlations, digamma recurrence with its sector remainder, all31
prime powers, head Nyquist convention and full tail/image/interpolation
bounds are precisely Proof3's (11)-(13), applied to the new exact
functions. Support enlargement is checked less than delta and the
support diameter less than9. Every delay interval is checked to stay
in one selected grid cell before the five hat terms are used. No
interpolant is assigned a zero pole product. Only the exact neutral
smooth functions are assigned E. Real polarization includes the
full errors from all three energies.

The complete matrix enclosures are in `certificate-875.json`,
`/sectors/0/energy_matrix` and `/sectors/1/energy_matrix`; both entire
matrices were inspected. Exact-rational checker `check-875.py` verifies
all original-metric coordinates, norms,30 energy budgets and20
polarizations, symmetry, diagonal assembly and exhaustive prime
powers:139 accounting checks pass. It also checks the interpolation
upper comparison with rational upper square roots. This is not an
independent FFT or elementary-function implementation. The arithmetic
model and inherited analytic methods remain qualifications.

The unshifted interval elimination order in each sector is Z first,
then V. The first complementary pivots are respectively enclosed in the
following outward enlarged decimal intervals:

    [.01708563, .02041716],
    [.04382693, .04776791].

After eliminating that positive pivot, the NEXT complementary pivots
have the following outward enlarged enclosures, respectively:

    [-.018280, .014250], [-.019919, .017703].             (16)

Full exact-rational pivot calculations and outward binary64 bounds
are in `check-875.json`, `/block_tests`. At the overlapping pivots
the checker stops WITHOUT division. Thus it certifies neither G>=0
nor a negative direction. It does not reach the Schur remainder,
identify an exact singular kernel or decide kernel-range compatibility.
An overlapping interval is not a singularity certificate. Midpoint
spectra, including the old expressly UNVALIDATED preview872, supply
no missing sign or rank. Accounting passes while both positivity
tests remain INCONCLUSIVE_G; these failures are explicitly recorded.

This is one mathematical EXPLORATION outcome: full entry coverage and
an identified numerical bottleneck, with no sign advance and no
new lemma claimed. It does not refute the exact-block route. A
passing finite compression would still leave positivity on the
infinite complement, non-neutral terms, other windows and actual-Xi
all-degree/global assembly unresolved. A negative finite direction,
if ever certified, would require separate critical review and would
not itself be the goal's certified off-line zeta zero.

## Mathlib

Full matching coverage for this supported logarithmic form, exact
projection and interval rejection certificate has not been checked.
Plancherel, Cauchy--Schwarz, orthogonal projections, finite Hermitian
order and Bessel are standard supporting inputs; no Mathlib theorem
matching the entire result is claimed. Numerical validity remains
qualified by the stated arithmetic model; the separate conceptual
audit above is informal verification, not a Lean-checked theorem.

The full fixed-U12 generalized-Schur diagnostic in Proof5 has no verified
matching Mathlib theorem here; coverage remains unchecked. The cited
finite Hermitian criteria are standard supporting inputs, not a formal
verification of the numerical enclosures or a positive compression.
