# C750j: The fixed T=256 supported capped certificate fails

## Hypotheses

Set a=9/4, b=log101/2, r=(a/b)log97, w=2a-r,
k=2log97/sqrt97 and I=(-a,a). Use complex H=L2(I), zero extension
to the real line, Lebesgue measure and inner product linear in its
second argument. Define

    F_f(t)=integral f(x)exp(-itx)dx,
    J[f]=(1/(2pi))integral log(2+|t|)|F_f(t)|^2dt,
    D_a={f in H: J[f]<infinity},
    C_f(s)=integral f(x+s)conj(f(x))dx,
    (U_b f)(x)=sqrt(a/b)f(ax/b).

These are the unchanged C750h/C750i conventions. Neither parity,
neutrality, a complete-Weil floor nor an inverse-compression identity
is assumed. C750h supplies only the fixed pulse's Fourier transform,
domain membership and correlation; its numerical J enclosure is not
a premise. C750i is historical motivation, not a theorem input.

Before evaluation, freeze T=256, alpha=log258, two-point Gauss-Legendre
quadrature on4096 panels of width h=1/16 on[0,T], and phase grid
theta_j=2pi*j/4096. The necessary test uses exactly C750h's unchanged
two-indicator pulse at theta=0. This scheme was recorded before
running the calculation. No pulse, cap, quadrature or phase search
was performed.

The computer-assisted bounds assume MPFR4.2.2's directed-rounding
semantics and Python/ctypes integer and ABI semantics, as in the
[MPFR manual, Section4.4](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Rounding).
The separate critical audit1150 below checks the analytic reduction,
the unchanged calculation, ABI and outward output. It remains
conditional on these library contracts, not formal verification of
the arithmetic libraries.

## Conclusion

Write J_T for J with multiplier min(log(2+|t|),log258). Then J_T<=J
on D_a, and the exact supported translation admits the bounded
finite-Gram sufficient test below. Its comparison base is coercive,
including the complete kernel and phase-error allowances.

Nevertheless, for f_0=1_(-a,-a+w)+1_(a-w,a), rigorous bounds give

    0.29186289 < J_T[f_0] < 0.29231410,
    0.29282701 < 8k|C_(U_b f_0)(log97)| < 0.29282702,
    -0.00096412 < J_T[f_0]-8k|C_(U_b f_0)(log97)|
                 < -0.00051291.                              (1)

The exact phase-zero finite Gram matrix without error subtraction
has norm >1.00510150; after subtracting the full positive-test error
from the base, it has norm >1.00823698. The required norm is <=1.
Thus this capped certificate fails even with exact quadrature. It
is parked; reducing numerical errors cannot repair its negative
capped form. No assertion is made about other caps.

This does not refute the original allocation k|C_(U_b f)(log97)|<=J[f]/8.
The removed high-frequency energy is nonnegative. No violating
original-domain witness or RH conclusion follows. This is a local
obstruction under an EXPLORE assessment, not certified originality
or an advance beyond the checked sources' abstract theorems.

## Proof

### The lower form and exact supported pairing

Use the unitary Fourier transform F/sqrt(2pi) and the bounded
functional calculus of Gerald Teschl, *Mathematical Methods in
Quantum Mechanics*, online GSM99 edition,
[Theorems3.1-3.2 and domain(3.25)](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
pp90-92, as inspected in review1143. These standard results are
imported. Their specialization here uses real bounded symbols and
zero extension, an isometry H->L2(R). The original J form is used
only on D_a; no bounded theorem is applied directly to its unbounded
operator. All supported L2 functions are L1, by finite measure.

Put ell(t)=log(2+|t|), alpha=log258 and

    q(t)=(alpha-ell(t))1_(|t|<=T),
    K(z)=(1/pi)integral_0^T [alpha-log(2+t)]cos(tz)dt.

Let K also denote convolution with this kernel restricted to I.
The symbol q is nonnegative, bounded and compactly supported.
Fubini is legitimate for supported L1 functions and a finite
frequency interval, so the kernel operator is exactly the compressed
Fourier multiplier. Plancherel therefore gives, for f in H,

    J_T[f]=alpha||f||^2-<f,Kf>.

For f in D_a the exact comparison remainder is

    J[f]-J_T[f]=(1/(2pi))integral_(|t|>T)
                     [ell(t)-alpha]|F_f(t)|^2dt >=0.          (2)

It is finite because J[f] is finite. This is a one-sided form
comparison, not an operator-norm approximation to J. No frequency
tail is omitted from a claim about J.

Let I_L=(-a,-a+w), I_R=(a-w,a), E=I_L union I_R. The directed
geometry check gives 0<w<a and r>a, hence r>w. Translation by r
maps I_L exactly onto I_R; a second translation has no supported
overlap. On H put

    (Sf)(x)=1_(I_L)(x)f(x+r),
    (S*f)(x)=1_(I_R)(x)f(x-r),
    P=1_E.

Both operators are contractions, ||S||=1, S^2=(S*)^2=0,
SS*=1_(I_L), and S*S=1_(I_R). The correlation is precisely
<f,Sf>, including for arbitrary complex f. Changing variables in
the dilated integral gives C_(U_b f)(log97)=C_f(r); the squared
normalization cancels the Jacobian.

Use the standard complex phase identity in Takeaki Yamazaki,
*On upper and lower bounds of the numerical radius and an equality
condition*, Studia Math.178(2007),83-89,
[equation(2.3) and proof, pp84-85](https://www.impan.pl/shop/publication/transaction/download/product/90571?download.pdf=),
DOI10.4064/sm178-1-5. It is applicable to bounded S on this complex
Hilbert space. In quadratic-form terms, the desired capped estimate
is equivalent to positivity for every real theta of

    J_T[f]-8k Re(exp(i theta)C_f(r))
       =<f,(B_theta-K)f>,
    U_theta=exp(i theta)S+exp(-i theta)S*,
    B_theta=alpha I-4k U_theta.                             (3)

This use of the phase identity is an import, not a new abstract
numerical-radius theorem. The support and the entire complex pairing
are retained in(3); no bound by total collar mass is used.

### Positive base, inverse and finite Gram criterion

The collar identities show U_theta is self-adjoint,
U_theta^2=P and U_theta(I-P)=0. On the collar pair it is the exact
two-by-two matrix with off-diagonal phases exp(+/-i theta), so its
eigenvalues there are +/-1; on the middle interval it is zero.
Consequently B_theta>= (alpha-4k)I. More generally, for beta>4k,
direct multiplication using U_theta^2=P gives

    (beta I-4k U_theta)^(-1)
      =(I-P)/beta+(beta P+4k U_theta)/(beta^2-16k^2).         (4)

Every term is a bounded supported operator. The computation certifies
alpha-4k>1.83702738. Formula(4) never replaces the supported inverse
by a whole-line inverse.

For p=0,...,4095, set t_(p,+/-)=(p+1/2)h+/-h/(2sqrt3).
Each two-point Gauss weight is h/2. Define

    K_N(z)=(h/(2pi))sum_(p,+/-) q(t_(p,+/-))cos(t_(p,+/-)z).

All nodes are in(0,T), hence all q values are positive. Index both
signed frequencies xi_l=+/-t_(p,+/-) and put
d_l=h*q(|xi_l|)/(4pi). There are16384 columns. With

    (Vz)(x)=sum_l sqrt(d_l)exp(i xi_l x)z_l, x in I,

the identity K_N=VV* is exact. In particular this finite-rank
operator is positive on the full complex H.

Let epsilon be the supported kernel error and nu the phase-cover
error proved below; put e=epsilon+nu and beta=alpha-e. The certificate
checks beta-4k>1.83131447>0. For each grid phase theta_j set

    D_j=B_(theta_j)-eI,
    G_j=V*D_j^(-1)V.                                      (5)

Use Zsigmond Tarcsay and Tamas Titkos, *Operators on anti-dual pairs:
Generalized Schur complement*, Linear Algebra Appl.(2020),
DOI10.1016/j.laa.2020.02.031,
[Theorem2.1, minimal completion and Corollary2.3, proof-PDF pp4-7](https://real.mtak.hu/112309/1/1-s2.0-S0024379520301038-main.pdf).
Apply it on Hilbert spaces H and C^16384 with positive invertible
A=D_j and bounded off-diagonal operator V*. Hilbert spaces satisfy
the weak sequential completeness requirements, and invertibility
makes the required range inclusion automatic. The minimal bottom
completion is V*D_j^(-1)V. Thus the block with bottom corner I is
positive exactly when G_j<=I, equivalently D_j-VV*>=0. This is the
bounded specialization of the cited result; no positivity of the
block being tested is assumed. Formula(4) verifies its inverse here.

For explicit matrix normalization, put I_0=I\E and
A_D(delta)=integral_D exp(i delta x)dx. With delta=xi_m-xi_l,
the exact(l,m) entry of G_j is sqrt(d_l*d_m) times

    A_(I_0)(delta)/beta
      + beta*A_E(delta)/(beta^2-16k^2)
      + (4k/(beta^2-16k^2))[
          exp(i(theta_j+xi_m*r))*A_(I_L)(delta)
          +exp(-i(theta_j+xi_m*r))*A_(I_R)(delta)].           (6)

For an interval(u,v), A(delta)=(exp(i delta v)-exp(i delta u))/(i delta)
when delta!=0 and A(0)=v-u. Formula(6) retains both collars, the
middle interval, exact translation and every complex phase. No matrix
entry is inferred from sampled functions. The failure test below
avoids assembling this large matrix by proving a lower bound on its
norm through an exact factorization identity.

If all grid matrices satisfy G_j<=I, then for any theta choose its
nearest grid phase, at circular distance <=pi/4096. The error bounds
give

    B_theta-K >= B_(theta_j)-K_N-(epsilon+nu)I
               =D_j-VV* >=0.                              (7)

This proves the sufficient all-complex-domain test. Positivity on
the complement of the finite-rank range follows from the coercive
base and the block criterion on all H; no Ritz convergence or
finite-section spectral assumption is needed.

### Full kernel and continuous-phase errors

Import the Gaussian quadrature remainder from NIST DLMF,
[Section3.5(v), equations(3.5.18)-(3.5.21)](https://dlmf.nist.gov/3.5.v),
as inspected in review1147. For two-point Gauss-Legendre quadrature
on a panel of length h the error is at most h^5 sup|g''''|/4320.
The weight is1, the nodes above are the scaled degree-two Legendre
zeros, and the positive weights are h/2. Apply this theorem to the
real smooth integrand g_z(t)=q(t)cos(tz) on each panel in[0,T].
There is no differentiation across the cusp at0 or across the cap;
only the smooth positive-frequency expression on this closed interval
is differentiated.

For0<=t<=T, q(t)<=q_0=log129 and
|q^(j)(t)|<=(j-1)!/2^j=:q_j for j=1,...,4. For every supported
spatial difference |z|<=2a, the product rule gives

    |g_z''''(t)|<=M4=sum_(j=0)^4 binom(4,j)q_j(2a)^(4-j).

Summing all4096 panel errors and dividing by pi proves the uniform
kernel and operator bounds

    sup_(|z|<=2a)|K(z)-K_N(z)| <= delta_K=T*h^4*M4/(4320*pi),
    ||K-K_N||<=epsilon=2a*delta_K.                         (8)

The last step is Schur's criterion: Teschl, same GSM99 edition,
Lemma0.32/proof, pp28-29. The finite-interval kernel is measurable,
and both absolute row and column integrals are <=2a*delta_K.
This controls every complex input, every spatial difference and
both off-diagonal collar interactions.

On the two collars the matrix U_theta-U_phi has norm
|exp(i theta)-exp(i phi)|, and it vanishes on I_0. Thus

    ||B_theta-B_phi||<=4k*dist_circle(theta,phi),
    nu=4k*pi/4096.                                       (9)

There is no uncovered phase interval in(7). In the negative test,
theta=0 is exact and already necessary, so its phase error is zero.
A failure at that phase obviates tests at the other4095 phases; it
does not prove signs at those phases.

### Decisive necessary test and directed calculation

For f_0 from C750h, ||f_0||^2=2w, C_f0(r)=w, and

    F_f0(t)=4sin(wt/2)cos(ct)/t, c=a-w/2,
    U_0 f_0=f_0,
    <f_0,B_0 f_0>=(alpha-4k)2w=:b_0.

Its finite J membership and exact Fourier formula are the C750h
inputs. The Gauss nodes are strictly positive, so no division by
zero occurs in their Fourier evaluation. Since this pulse is real
and even, both signed frequencies contribute the same Fourier square:

    A_N=<f_0,K_N f_0>
       =(h/(2pi))sum_(p,+/-)q(t_(p,+/-))|F_f0(t_(p,+/-))|^2.

Every one of the8192 positive-frequency nodes is included. Equation(8)
then proves

    <f_0,K f_0> in [A_N-epsilon*2w,A_N+epsilon*2w],
    <f_0,(B_0-K)f_0> in [b_0-A_N-epsilon*2w,
                          b_0-A_N+epsilon*2w].            (10)

All endpoint arithmetic in(10) is also enclosed. No infinite-frequency
contribution to K exists; equation(2) records the complete contribution
removed from J, whose sign prevents a disproof of the original bound.

The exact finite Gram G_(0,0)=V*B_0^(-1)V has norm at least A_N/b_0.
Indeed, put A=B_0^(-1/2)V. The Hilbert-space identity
||A*A||=||AA*|| identifies its norm with that of
B_0^(-1/2)K_N B_0^(-1/2); the latter's Rayleigh quotient at
B_0^(1/2)f_0 is A_N/b_0. Square roots exist by the cited bounded
positive functional calculus. The same reasoning with
D_0=B_0-eI gives the lower bound A_N/[(alpha-4k-e)2w] for(5).
These are lower bounds that disprove a proposed upper threshold;
no trial eigenvalue is presented as an upper bound.

Run from this notebook:

    python3 scripts/prime-collar/certify_1148.py

The full certificate is
[scripts/prime-collar/certificate-1148.json](../scripts/prime-collar/certificate-1148.json).
It contains every enclosed Gauss node, q value, Fourier square and
weighted contribution, cumulative sums every256 panels, geometry,
derivative majorants, kernel/phase allowances, final enclosures,
source hashes and all assertions and failed mathematical tests.
The script reuses only the interval backend in
scripts/pivot-area/certify_1136.py, without modifying it.

Precision is384 bits. Basic operations are directed, multiplication
takes four endpoint extrema, and nonnegative squares use absolute
endpoints. Monotone log/sqrt evaluations are directed; sin/cos
evaluations are enlarged by the entire argument width using their
global Lipschitz bound1. Hence node, weight, Fourier and summation
errors are included in A_N, rather than treated as exact printed
nodes. The final decimal endpoints are also rounded outward.
The interval width of A_N is <7.188e-113 before decimal output.
Binary64 is used only for console display. No approximate matrix is
assembled, so no unaccounted matrix-rounding error enters the exact
Gram lower bounds.

Outward weakenings of the certificate are

    M4 < 2210.326825,
    epsilon < 0.002862830,
    nu < 0.002850085,
    epsilon*2w < 0.000225600,
    alpha-4k-e > 1.83131447,
    1.00510150 < A_N/b_0 < 1.00510151,
    1.00823698 < A_N/[(alpha-4k-e)2w] < 1.00823700.

The complete load-bearing endpoints of(10), the Gram quotient and
quadratic error were inspected, not inferred from a JSON preview.
They give(1). All twelve verification assertions pass; the three
mathematical positivity tests fail and are explicitly retained.
The actual capped upper residual is below-0.00051291155, whereas
positivity requires residual >=0. The scalar quadrature allowance
0.000225599834 is already paid in that upper endpoint.

Thus the fixed cap's loss, not arithmetic or missing phase coverage,
stops this certificate. Exact evaluation of K or a finer mesh at
this same cap cannot make its universal form nonnegative. No claim
is made that a different cap cannot succeed; no such search is
performed. The original allocation, complete dilation budget,
J-to-baseline comparison, old-shift and pole/digamma costs, both
sectors, all supports and actual-Xi realization at L030-L032/C032a
remain unresolved.

### Separate correctness audit1150 — 16 November2026

Assessment1148, approved in source review1149, authorizes this exact
audit under SPECIALIZE. It reuses the primary results cited above;
none of their abstract conclusions is claimed as new mathematics.
The audit finds no error in the fixed obstruction. This is additional
verification of1148, not a stronger bound or an original-J counterexample.

The analytic checks are as follows. Zero extension is an isometry;
the bounded real symbol q gives the stated self-adjoint compressed
kernel by finite-interval Fubini. The lower comparison and entire
positive remainder in(2) hold on D_a, so their direction cannot be
reversed. C750h's explicit pulse is in D_a: its transform is bounded
at zero and O(1/|t|) at infinity. Only its transform, membership and
correlation are inputs; no numerical claim about its full J is used.

With the inner product linear in its second argument, <f,Sf> is
exactly integral conj(f(x))f(x+r)dx, and the adjoint is the displayed
left translation on I_R. Thus(3) has the correct conjugate phases and
factor4k. The collars are disjoint and translation takes I_L onto I_R,
so U_theta^2=P; multiplying(4) by beta I-4k U_theta gives I separately
on E and I_0. The certified beta-4k>1.83131447 makes the inverse
bounded and positive on the full complex H. This uses no inverse
compression identity or regularity of a whole-line resolvent.

The positive block in the cited Hilbert Schur theorem is precisely

    [ D_j   V ] on H direct-sum C^16384.
    [ V*    I ]

Its minimal lower-right completion is V*D_j^(-1)V; invertibility
of D_j supplies the range condition. Applying the inverse to the
column exp(i xi_m x) produces exp(i xi_m r) on I_L and
exp(-i xi_m r) on I_R, verifying both off-diagonal terms in(6).
The signed-frequency weight h*q/(4pi) doubles to the cosine weight
h*q/(2pi); consequently VV*=K_N with no missing Fourier factor.
The lower quotient uses B_0^(1/2)f_0 (or D_0^(1/2)f_0), not f_0
in a different norm. Equality ||A*A||=||AA*|| therefore gives a
lower bound for the exact Gram norm. Its direction cannot certify
an upper bound, and here correctly disproves one.

The two-point Gauss remainder applies to the smooth expression
alpha-log(2+t) on each positive-frequency panel, including the
endpoint panels. It does not differentiate the capped extension
across0 or T. The derivative bounds q_j cover the entire interval;
the spatial majorant covers all |x-y|<=2a. Both Schur integrals
are bounded by2a*delta_K, not a sampled collar width. The two-by-two
phase difference has norm |exp(i theta)-exp(i phi)|, yielding(9)
on all H and the circular grid radius pi/4096. The necessary
theta=0 countertest incurs no phase error. Equation(10) pays the
full kernel error times ||f_0||^2=2w in the unfavorable direction.

Reproduce the implementation audit from this notebook with

    python3 scripts/prime-collar/audit_1150.py

Its full records are scripts/prime-collar/certificate-audit-1150.json
and scripts/prime-collar/certificate-1148-replay-1150.json. The
original certificate and original script/backend remain unchanged.
The replay compares every JSON field, all8192 nodes and all16
cumulative blocks, not a bounded preview. A fresh compilation of
scripts/prime-collar/abi_1146.c checks the installed MPFR header and
runtime4.2.2, precision384, structure size32, scalar sizes8/4/8/8,
field offsets0/8/16/24 and RNDD/RNDU values3/2 against ctypes.

The backend source was checked independently in this audit. Addition
uses the ordered endpoints; multiplication takes all four endpoint
extrema; division rejects a zero-containing denominator before using
the decreasing reciprocal; squares use nonnegative absolute endpoints.
All log/sqrt arguments here are positive. Each trigonometric enclosure
evaluates at the exact binary lower endpoint with directed rounding
and widens by the whole argument width, using the global Lipschitz
constant1. Integer indices and all mesh constants are exact. Ignored
return values of MPFR void functions are not used in any computation;
pointer-returning conversion/version functions have explicit return
types. Basic operation return flags are not mistaken for numerical
results. This remains an informal ABI/code audit under the stated
Python/ctypes/MPFR contracts.

For output verification, every persisted interval endpoint was
compared as an exact rational with the exact384-bit MPFR significand
obtained in base2. All65630 endpoint checks confirm outward decimal
rounding; exponent assembly handles the sign and zero correctly.
The applicable conversion contract is the MPFR4.2.2 manual,
[Section5.4, mpfr_get_str](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Conversion-Functions),
already covered by review1145. Independently summing the8192 saved
decimal term intervals using Python Fraction checks each cumulative
block and, directly against the full saved error, gives

    base_pulse_upper - sum(term_lower) + quadratic_error_upper
        < -0.00051291155 < 0,
    sum(term_lower)/base_pulse_upper > 1.00510150 > 1,
    sum(term_lower)/(paid_coercivity_upper*norm_squared_upper)
        > 1.00823698 > 1.

All denominators are strictly positive. Every displayed numerical
weakening above is checked by exact rational comparison. All50 audit
checks pass; every original claim and all three failed mathematical
positivity tests are retained. Binary64 is not used for decisions.
This is a replay of the reviewed original interval backend with
independent exact-rational output/sum checks and a C ABI probe; it is
not an independently implemented second quadrature or formal proof
of MPFR. The analytic error estimates, not numerical agreement alone,
are what make the replay a certificate of the exact capped sign.

The only direct local mathematical input remains C750h. C750i is a
contrast, not a premise; no new DAG edge is needed. The fixed T=256
certificate is now an audited local stop. All other caps, the original
J allocation and the complete-form/actual-Xi gaps retain their scope.

## Mathlib

Full matching coverage was not checked. Supporting ingredients are
complex Hilbert-space adjoints, Fourier/Plancherel, bounded positive
functional calculus, Gaussian quadrature and Schur kernel bounds.
The cited theorems and this computer-assisted specialization are
informal inputs; no matching Mathlib theorem or formal verification
is claimed. Unknown coverage is not evidence of absence.
