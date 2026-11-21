# Lemma 723: the complete sampled response retains the signed bump edge

## Hypotheses

Fix the original actual L703 profile once before n varies, with the
full L666 family and the exact low-frequency prescription of L708.
Use the audited inverse density and signed bump K_n of L714, the
audited phase/support-edge result of L721, and the audited residue
rate bound of L722. In particular

    n=12q+3, q>=1, M=n/3, h=A/n,
    d=5/4, R=11/8, U=121/64, A=27/10, c_0=R-d=1/8,
    u=u_*=(3+4i)/10, Y=9/20, a(y)=-d+i*y,
    y_m=h*(m+1/2+e_m), |e_m|<=1/8, E=sum_m|e_m|<infinity,
    Z_n={-d} union {a(y_m): -2q<=m<2q},
    W_n(y)=product_(j=0)^(n-1) Q_(j/n)(y),
    Q_t(y)=(d+t*u)*(U*u+(d-i*y)*t)
                           /[(U*u+d*t)*(d+t*u-i*y)],
    G_n=R^(-1)*sum_(a in Z_n) W_a(u)
                              *sum_(k=0)^(M-1)(-a/R)^k.

Here W_(a(y))(u)=W_n(y), including Q_0(y)=d/(d-i*y), and
W_(-d)=1. All original masses, both endpoints, the anchor and all M
moments are retained. The angular argument is the rational continuation
specified in L666, not a change to its denominator convention.

On real frequencies put

    S_e(v)=sum_(m in Z)[exp(i*v*(m+1/2+e_m))-exp(i*v*(m+1/2))].

L708 gives |S_e(v)|<=E*|v|, and S_e(v)=-chi(v) for 0<v<3*pi/4.
The fixed positive bump has support in I=[omega-delta,omega+delta]
inside (0,9/4), equals one on the middle half of I, and
0<delta<1/3000. Its actual right support endpoint is b=sup supp chi.
No law of vanishing at b, complex continuation of chi, or n-dependent
selection is assumed. Write S for L721's holomorphic phase and
r(b)=Re S(b)>1/200. The density and signed integral are

    k_n(y)=W_n(y)/(c_0+i*y),
    k_n(y)=integral_R exp(i*y*v/h)*p_n(v)dv,
    K_n=integral_I chi(v)*p_n(v)dv.

## Conclusion

For this unchanged family there is a fixed C<infinity such that,
for all sufficiently large permitted n,

    G_n(u_*,-1)=8-K_n+epsilon_n,
    |epsilon_n|<=C*exp(-n/1000).                         (1)

Consequently

    limsup_(q->infinity) log|G_(12q+3)(u_*,-1)|/(12q+3)
                                  =r(b)>1/200.          (2)

The exact sampled power series

    F(z)=sum_(q>=1) (12q+3)^(-1/2)*G_(12q+3)(u_*,-1)*z^q

has radius exp(-12*r(b)) and retains L721's nonremovable singularity
at z_*=exp(-12*S(b)). The combined correction germ is holomorphic
on |z|<1 and is identified with the same germ from zero. Neither a
formal expansion nor a noncancellation assumption is used.

Status: derived in step 201; accepted by the separate step-203
conceptual audit in Section 7 below.
This is a local complete-response result within the prior EXPLORE
scope, not certified originality or an RH candidate. There is no
full rate limit, eventual nonvanishing or sign assertion. Angular
persistence, logarithmic-mean payment, complementary spatial Jensen
defect, amplitude/full charge, H/support, Xi realization and actual-Xi
all-degree mixed positivity remain open. All onsets are existential.

## Proof

### 1. Source scope and verification of the complete finite identity

Reuse the invocation-start assessment
`drafts/literature/2026-11-03-complete-response-support-germ-scope.md`
and its exact COVERED_TARGET. This proof does not repeat the stopped
comparison of R_n with the smaller residue P_n. Instead it bounds the
other terms after the exact cancellation P_n-R_n=-K_n from L714.
L713's proposed full identity is checked here; its unaudited contour
envelopes are not inputs.

The imported Fourier/convolution facts are those already justified
in L714 Section 2: J. Kallsen and P. Kruehner, *On uniqueness of
solutions to martingale problems — counterexamples and sufficient
criteria*, [arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1),
Appendix A, Lemma A.1(6),(9)--(11),(14), pp.29--30, and NIST DLMF
[1.14(i), (1.14.1), (1.14.3)](https://dlmf.nist.gov/1.14.i).
They concern finite complex measures, and inversion with the stated
integrability and bounded-variation hypotheses. L714 verifies these
for the present fixed-n density, including its value at zero. Poisson
summation below imports S. D. Miller, *Some notes on distributions*,
15 January 2006, [Theorem 4.1 and Section 6, pp.7--9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf).
Its Schwartz hypothesis is met by Gaussian regularization before the
limit. No general Fourier, support-transfer or Poisson theorem is
reproved. Only the new-center bounds and limiting hypotheses are paid.
For the final series operations use NIST DLMF
[1.9(v)--(vi), especially (1.9.48)--(1.9.50)](https://dlmf.nist.gov/1.9):
the M-test, power-series analyticity/radius and addition/subtraction on
a common convergence disk. These inputs were inspected in the separate
audit assessment; they do not supply any of the correction estimates.

By L714, p_n is continuous with finite first absolute moment, and
k_n is a rational function with no real pole and k_n(y)=O(|y|^-2).
Thus all integer physical sums below converge absolutely. Since

    sum_m |exp(i*v*(m+1/2+e_m))-exp(i*v*(m+1/2))|
                                                <=E*|v|,

absolute Fubini gives exactly

    sum_m k_n(y_m)=B_n+integral_R S_e(v)*p_n(v)dv,
    B_n=sum_m k_n(h*(m+1/2)).

Set

    V_n=integral_(v<0 or v>=9/4) S_e(v)*p_n(v)dv,
    L_n^-=sum_(m<=-2q-1) k_n(y_m),
    L_n^+=sum_(m>=2q) k_n(y_m),
    T_n=sum_(a in Z_n) W_a(u)*(-a/R)^M/(R+a).

The integral on 0<v<9/4 equals -K_n by the real-frequency
prescription and its support. Removing precisely the two displayed
tails and adding the anchor gives 8+B_n-K_n+V_n-L_n^--L_n^+.
The finite geometric identity, including its R^(-1) normalization,
is

    R^(-1)*sum_(k=0)^(M-1)(-a/R)^k
                               =[1-(-a/R)^M]/(R+a).

Every R+a has real part c_0>0. Consequently the exact full identity is

    G_n=8-K_n+B_n+V_n-L_n^--L_n^+-T_n.                (3)

This verifies L713 (4) with L714's P_n-R_n=-K_n. No estimate at
u=1/2, infinite complex-frequency prescription or omitted moment is
used. We now bound all terms in the correction in (3).

### 2. Two uniform real-physical product bounds

Use p=3/10 and beta=2/5 for the real and imaginary parts of u;
beta is unrelated to the support endpoint b. For 0<=t<=1 put

    L(t)=d^2+2*d*p*t+t^2/4,
    B(t)=U^2/4+2*U*p*d*t+d^2*t^2,
    C=d^2-U/4=279/256, H=2*beta*C=279/320,
    E_t=t^2/4+2*d*p*t+U/4.

These are positive, and U-t^2>0. For x>=0 direct expansion gives

    |Q_t(-x)|^2-1
       =(U-t^2)*x*(H*t-E_t*x)
                          /[B(t)*(L(t)+2*beta*t*x+x^2)].  (4)

Also |Q_t(x)|<=|Q_t(-x)|. To check this last assertion, cross
multiply their positive denominators. After removing the common
positive factor L/B, the difference of the two numerators is

    4*beta*t*x*[(B-U*L)+(t^2-U)*x^2]
       =-4*beta*t*x*(U-t^2)*(C+x^2)<=0.

For the right side of (4), the derivative of the variable part
x*(H*t-E_t*x)/(L+2*beta*t*x+x^2) has numerator

    H*t*L-2*E_t*L*x-(H*t+2*beta*t*E_t)*x^2.

The exact identity

    (3/5)*E_t-H*t
           =3/256+(1-t)*(87/320-3*t/20)>0

shows that this derivative is strictly negative for x>=3/10.
Therefore for all real |y|>=2/5,

    |Q_t(y)|<=|Q_t(-2/5)|.                             (5)

For a global bound complete the square in the numerator of (4).
If it is negative, |Q_t(-x)|^2-1<=0. If it is nonnegative, the
denominator is at least B*L and
x*(H*t-E_t*x)<=(H*t)^2/(4*E_t). In both cases, and by the
positive/negative comparison for every real y,

    |Q_t(y)|^2-1<=X(t):=(U-t^2)*(H*t)^2/[4*E_t*B*L],
    log|Q_t(y)|<=X(t)/2.                               (6)

All Q_t(y) are nonzero for real y: the real parts of U*u+d*t-i*t*y
and d+t*u-i*y are positive. Thus the elementary inequality
log a<=a-1 is applied to positive a=|Q_t(y)|^2.

The exact certificate in Section 4 proves

    integral_0^1 (|Q_t(-2/5)|^2-1)/2 dt < -1/400,
    integral_0^1 X(t)/2 dt < 1/125.                    (7)

The integrands are fixed continuous rational functions with positive
denominators. Left Riemann-sum convergence implies, for all sufficiently
large permitted n, respectively an upper average -1/500 and 1/120.
For the tail product retain the exact j=0 factor separately; removing
its finite contribution to the first sum costs only a fixed constant.
Equations (5)--(7) give

    |W_n(y)|<=C_1*exp(-n/500)/|y|,       |y|>=2/5,
    |W_n(y)|<=exp(n/120),                y real.     (8)

The first line uses |Q_0(y)|<=d/|y|. Both conclusions are uniform
in the indicated y ranges, not estimates at sampled physical points.

### 3. Positive-frequency tilt and negative-frequency pole

Write lambda_t=d+t*u and r_t=t*lambda_t/(U*u+d*t). The exact factor
measure used in L714 is

    mu_t=r_t*delta_0+(1-r_t)*(lambda_t/h)
                                    *exp(-lambda_t*v/h)1_(v>=0)dv.

At the exponential tilt exp(n*v/5), its total variation mass is

    z(t)=|r_t|+|1-r_t|*|lambda_t|/(Re lambda_t-A/5)
        =sqrt(L(t)/B(t))*[t+(U-t^2)/(2*(d+p*t-A/5))]. (9)

Here d-A/5=71/100>0 and 1-r_t=u*(U-t^2)/(U*u+d*t), so (9)
is exact. Section 4 proves integral_0^1 z(t)dt<3/2. Continuity
then gives n^(-1)sum_j z(j/n)<3/2 eventually. The finite AM--GM
inequality yields product_j z(j/n)<=(3/2)^n. In particular the
product with j=0 omitted is at most this, since z(0)=125/71>1.

The full convolution has density g_n from L714. Isolate the j=0
exponential of rate d/h. For v>=0, variation domination and its
explicit density show

    exp(n*v/5)*|g_n(v)|
      <=(d/h)*integral_[0,v] exp[-(d/h-n/5)*(v-s)]
                         exp(n*s/5)d|(*_(j>=1)mu_(j/n))|(s)
      <=(d/h)*(3/2)^n.

The isolated convolution gives this bound first for a density
representative, hence almost everywhere. L714's finite exponential
formula is continuous on (0,infinity) and has a right limit at zero,
so the same bound holds pointwise there and for that right-limit value
at zero. This is a bound on a complex density obtained from positive
variation, not a probability assertion about g_n. L714's exact
convolution with the negative-halfline resolvent gives for v>=0

    p_n(v)=exp(c_0*v/h)/h
                             *integral_v^infinity exp(-c_0*s/h)*g_n(s)ds.

Absolute integration therefore yields

    |p_n(v)|<=d/[h*(c_0+A/5)]*(3/2)^n*exp(-n*v/5)
             <=C_2*n*exp(41*n/100-n*v/5).             (10)

The inequality log(3/2)<41/100 follows because the first four
terms of exp(41/100) already exceed 3/2; the exact comparison is in
the certificate. All exponential moments used here converge since
Re lambda_t-A/5>0 uniformly. Thus (10) covers the entire half-line.

For v<=0 L714 supplies the exact formula, including v=0,

    p_n(v)=W_n(i*c_0)*exp(c_0*v/h)/h.                  (11)

We need the pole product before multiplying by the positive bump.
L722 gives p(b)=Phi_0+c_0*b/A<1/5000, where
Phi_0=integral_0^1 log|Q_t(i*c_0)|dt. Also b>=omega and

    omega/A=integral_0^1 (U-t^2)/[(d+t)*(U+d*t)]dt
                  >=(U-1)/[(d+1)*(U+d)].

The scalar certificate verifies
c_0*(U-1)/[(d+1)*(U+d)]-1/5000>1/100. Hence Phi_0<-1/100.
The four affine factors at i*c_0 have positive real parts and bounded
logarithmic derivatives on [0,1]. Their left Riemann sum has O(1)
error after multiplication by n, proving

    |W_n(i*c_0)|<=C_3*exp(-n/100).                    (12)

This uses the audited L722 residue bound, not L713's envelope or an
unjustified positivity estimate for K_n.

### 4. Full exact certificate for the auxiliary integral bounds

Run
`python3 scripts/one-sided-hankel/complete-response-correction-certificate-201.py`.
Its complete rational certificate is
`scripts/one-sided-hankel/complete-response-correction-certificate-201.json`.
It covers [0,1] with all 2048 closed cells [j/2048,(j+1)/2048].
Interval addition, subtraction and all four endpoint products give
exact rational enclosures. Division is performed only after checking
the denominator lower bound is positive. Squares are of nonnegative
intervals. For (9), the upper endpoint L/B is square-rooted upward
to denominator 2^50 by integer square root; exact squaring checks the
rounding. Every cell's final upper bound is rounded upward to the
same denominator before averaging. There is no quadrature error term:
these are pointwise upper bounds on each entire cell, integrated by
its exact length. Endpoints and the full interval are included.

The resulting integral upper bounds, with exact required thresholds, are

    tail:   -101065706568539/36028797018963968 < -1/400,
    global:  546067086027185/72057594037927936 < 1/125,
    tilt:   210875637913269195/144115188075855872 < 3/2. (13)

The same certificate checks the four scalar comparisons used here:

    67/6050-1/120=199/72600>1/400,
    c_0*(U-1)/[(d+1)*(U+d)]-1/5000
                                   =46897/3015000>1/100,
    1+41/100+(41/100)^2/2+(41/100)^3/6
                                   =9033221/6000000>3/2,
    Y-A/(8*15)=171/400>2/5.                           (14)

All seven comparisons pass, with no failures. The certificate retains
every cell upper bound and the full exact totals; the displayed decimal
previews in the JSON do not decide any inequality. The separate
`scripts/one-sided-hankel/complete-response-correction-diagnostic-201.json`
is only a floating-point screen and supplies no proof premise.

### 5. Pay every correction, with no unproved size-series interchange

For v>=9/4, equations (10) and |S_e(v)|<=E*v imply

    |V_n^+|<=C_2*E*n*exp(41*n/100)
                                  *integral_(9/4)^infinity v*exp(-n*v/5)dv
              <=C_4*exp(-n/25),                       (15)

since (9/4)/5-41/100=1/25 and the integrated prefactor is bounded.
On the negative half-line (11)--(12) give

    |V_n^-|<=E*|W_n(i*c_0)|*h/c_0^2
                                      <=C_5*exp(-n/100). (16)

For completeness the comb identity at this new center is

    B_n=2*pi*sum_(l in Z)(-1)^l*p_n(2*pi*l).           (17)

To justify it, apply the cited Schwartz Poisson theorem to
k_n(h*s)*exp(-epsilon*s^2), epsilon>0. For fixed n all derivatives
of the rational factor have polynomial bounds and it has no real
pole, so the product is Schwartz. Finite-variation Fubini identifies
its Fourier transform as 2*pi*(p_n*G_epsilon), where
G_epsilon(v)=(4*pi*epsilon)^(-1/2)exp(-v^2/(4*epsilon)).
For every fixed permitted n, L714's finite exponential formulas on the
positive half-line and exact negative pole formula give
|p_n(v)|<=C_n*exp(-a_n*|v|), with a_n>0. This also covers the finitely
many n before the common onset of (10)--(12). Hence for 0<epsilon<=1,

    |(p_n*G_epsilon)(w)|<=2*C_n*exp(a_n^2)*exp(-a_n*|w|).

This follows by |v|>=|w|-|w-v| and the Gaussian exponential moment.
The bound is summable at w=2*pi*l. Continuity of p_n and absolute
summability of k_n(h*(m+1/2)) justify both limits in Poisson, including
the zero sample. Thus (17) concerns the original unshifted comb.
It is not an application of a finite-measure theorem to the infinite
unit-mass counting measure.

In (17) the l<=0 terms, by (11)--(12), sum in modulus to at most
C*n*exp(-n/100)/(1-exp(-2*pi*c_0/h)). The l>=1 terms, by (10),
sum to at most C*n*exp(41*n/100-2*pi*n/5)/(1-exp(-2*pi*n/5)).
The denominators are bounded below for n>=15, and pi>3. Therefore

    |B_n|<=C_6*n*exp(-n/100)+C_7*n*exp(-79*n/100).    (18)

Both omitted physical tails satisfy |h*(m+1/2)|>=Y and
|y_m|>=Y-h/8>2/5 for n>=15, as (14) checks at the smallest n.
By (8) and |c_0+i*y|>=|y|,
|k_n(y_m)|<=C*exp(-n/500)/y_m^2. Also
|m+1/2+e_m|>=(3/4)|m+1/2|. Integral comparison gives

    sum_(m>=2q or m<=-2q-1) 1/y_m^2
           <=(32/9)*h^(-2)/(2q-1/2)<=320*n/(9*A^2),

where 2q-1/2>=n/10. Consequently

    |L_n^-|+|L_n^+|<=C_8*n*exp(-n/500).              (19)

For every retained atom |y_m|<Y (the outer index plus its maximal
shift has absolute value at most 2q-3/8). Hence
|a|^2<=d^2+Y^2=353/200 and |a|/R<=rho=sqrt(2824/3025)<1,
including the anchor. Using all M atoms, all M moments, (8), and
|R+a|>=c_0 gives

    |T_n|<=8*M*exp(n/120)*rho^(n/3).

Since log(rho)/3=log(2824/3025)/6<=-67/6050, the first comparison
in (14) proves

    |T_n|<=8*M*exp(-n/400).                           (20)

Combining (15)--(20), all terms in the correction in (3) are
O(n*exp(-n/500)). Absorbing the polynomial factor gives (1).
Constants may depend on the fixed profile through E; no uniformity
as its width shrinks is asserted. A common onset suffices, and changing
finitely many samples affects none of the conclusions.

### 6. The common germ and the rate conclusion

Define H(z)=sum_(q>=1) n^(-1/2)*(8+epsilon_n)*z^q, n=12q+3.
Equation (1) gives absolute locally uniform convergence on |z|<1;
the epsilon part even converges on |z|<exp(12/1000). Define
Kcal(z)=sum_(q>=1) n^(-1/2)*K_n*z^q. L721 proves its radius is
R_*=exp(-12*r(b)) and its germ from zero has a nonremovable
singularity at z_*. The missing q=0 term is a polynomial change and
does not affect that conclusion. L722 gives R_*<exp(-3/50)<1.

On the common disk |z|<R_*, the exact coefficient identity (3) and
the absolute convergence just established give

    F(z)=-Kcal(z)+H(z).                               (21)

No q-sum is interchanged with an uncontrolled frequency integral or
physical sum: their completed numerical coefficients were bounded
first. Every correction in (3) separately has the exponential bounds
above, so their combined generating germ is indeed H. It is holomorphic
across a neighborhood of z_* inside the unit disk. If F extended
holomorphically through z_*, then H-F would give such an extension
of the same Kcal germ from zero, contradicting L721. This proves the
claimed inherited singularity and excludes a nearer obstruction from
the correction. The convergence radius is exactly R_*.

Alternatively (2) follows directly without a transfer theorem. From
L721's limsup and (1), the upper limsup for G is at most r(b)>0.
For any 0<eta<r(b), infinitely many allowed n satisfy
|K_n|>=exp((r(b)-eta)*n). The correction 8+epsilon_n is bounded,
so along sufficiently large such n, |G_n|>=|K_n|/2. Let eta tend
to zero. This proves the lower limsup and (2), with log(0)=-infinity.
It supplies no angular or logarithmic-mean lower bound.

### 7. Separate conceptual audit — 3 November 2026, step 203

The prior SPECIALIZE assessment
`drafts/literature/2026-11-03-complete-response-support-edge-audit.md`+covers exactly this audit, with the original fixed profile and constants.
This section accepts (1)--(2) and the same-germ assertion. It verifies an
existing local specialization, not a new general theorem, a full rate
limit or an RH candidate. No input from the stopped contour envelopes,
common-phase argument or size interpolation has been added.

**Finite identity and domains.** Substituting the rational continuation
of L666 into W_a gives the displayed Q_t, with the exact t=0 factor.
For real y its two denominators have positive real parts. The real
parts of R+a all equal c_0; the anchor contributes 1/c_0=8. The Mth
geometric remainder is subtracted, not added. Since the infinite
physical sums are absolutely convergent and

    sum_m integral_R |exp(i*v*(m+1/2+e_m))
                       -exp(i*v*(m+1/2))|*|p_n(v)|dv
                            <=E*integral_R |v*p_n(v)|dv<infinity,

the shifted-minus-unshifted pairing is absolute. The supplied
real-frequency identity is used only on 0<v<9/4<3*pi/4. The other
two frequency ranges remain in V_n. Removing m<=-2q-1 and m>=2q
leaves exactly 4q nonanchor atoms, hence M=4q+1 atoms in all. This
independently verifies every sign and normalization in (3).

**Exact arithmetic and all-variable reductions.** Run
`python3 scripts/one-sided-hankel/complete-response-correction-audit-203.py`.
It replays the original certificate into
`scripts/one-sided-hankel/complete-response-correction-replay-203.json`
and preserves the step-201 file byte for byte. Its independent full
certificate is
`scripts/one-sided-hankel/complete-response-correction-audit-203.json`.
All 2048 cells are checked; the stored pass flags and decimal previews
are not premises.

The script checks five exact bivariate polynomial identities: (4), the
positive/negative-y comparison, the derivative numerator, the strict
monotonicity margin and the completed square. Positivity is justified
by d>0, U-1>0, L,B,E_t>0 and
87/320-3*t/20>=39/320>0 on [0,1]. Thus the derivative is strictly
negative for x>=3/10, and (5) covers both real tails. The square
completion covers all real y, including the case where the numerator
in (4) is negative. Every factor is nonzero, so log a<=a-1 applies.

Independently of the original interval operations, the audit clears
positive denominators in each stored cell inequality. Write
D(t)=d+p*t-A/5 and N(t)=2*t*D(t)+U-t^2. For the tail and global
bounds it checks respectively

    2*a_j*B*(L+2*beta*t*x+x^2)
                    -(U-t^2)*x*(H*t-E_t*x)>=0, x=2/5,
    8*b_j*E_t*B*L-(U-t^2)*(H*t)^2>=0.

For the stored nonnegative tilt upper bound c_j it checks

    4*c_j^2*D(t)^2*B-L*N(t)^2>=0.

Here a_j,b_j,c_j are exactly the stored dyadic bounds, not new
samples. Since D>0, B>0 and c_j>=0, the last inequality implies
z(t)<=c_j. On a cell t=l+s/2048, 0<=s<=1, the audit computes the
complete Bernstein coefficients of each cleared polynomial. If its
ordinary coefficients are A_k and its degree is m, those coefficients
are B_j=sum_(k<=j) A_k*binom(j,k)/binom(m,k). Expanding
(s+(1-s))^(m-k) verifies the identity with the basis
binom(m,j)*s^j*(1-s)^(m-j), whose entries are nonnegative on [0,1].
All 38,912 exact coefficients are nonnegative. Thus all 6,144
inequalities hold on their entire closed cells, not only at endpoints.
Every coefficient is retained in the audit certificate.

Integrating these bounds by the exact cell length reproduces the
three totals in (13). All four scalar comparisons in (14) also pass
independently. The audit has 17 passing summary checks and no failures.
It verifies the certificate's full rational domain; the analytic
uses are the arguments here, not consequences of the flags alone.

The three continuous integrands have fixed strict margins. Consequently
their left Riemann sums have the stated common eventual bounds after
taking the maximum of three onsets. Dropping the j=0 term from the
tail logarithmic sum changes its upper bound by the fixed number
-f(0), with f(t)=(|Q_t(-2/5)|^2-1)/2. Multiplication by
|Q_0(y)|<=d/|y| then proves the first bound in (8) uniformly; the
global estimate in (8) needs no factor removed.

**Density and pole normalization.** Each exponentially tilted factor
measure is finite because Re lambda_t-A/5>=71/100. The atom and
absolutely continuous part are mutually singular, so their variation
masses add and (9) is exact. Their finite convolution has variation
at most the product of these masses. AM--GM and the strict integral
margin give that product at most (3/2)^n eventually. Since z(0)=125/71>1,
omitting j=0 cannot increase this bound. Its explicitly isolated
exponential density supplies d/h; continuity completes the pointwise
argument as now written above (10). Integrating the negative resolvent
then supplies

    (d/h^2)/(c_0/h+n/5)=d/[h*(c_0+A/5)].

This confirms the required factor of n and (10), including v=0.
No density positivity has been used. For (12), the plateau implies
b>=omega. L722's accepted p(b)<1/5000 and the elementary lower bound
for omega/A give Phi_0<-1/100 by (14). The four affine factors at
i*c_0 stay in the right half-plane with bounded log derivatives.
Their Riemann-sum error is O(1), proving (12) with a fixed constant.

**Poisson and all correction sums.** With Miller's convention
hat f(l)=integral f(s)*exp(-2*pi*i*l*s)ds, the Gaussian-regularized
transform is exactly

    hat f_epsilon(l)=sqrt(pi/epsilon)*integral_R
       p_n(v)*exp(-(v-2*pi*l)^2/(4*epsilon))dv
                    =2*pi*(p_n*G_epsilon)(2*pi*l).

Its Fubini bound is ||p_n||_1*sqrt(pi/epsilon)<infinity. Translation
by 1/2 supplies (-1)^l. The fixed-n exponential bound, including the
finite preasymptotic sizes, provides the summable majorant displayed
before (18), uniformly for 0<epsilon<=1. Continuity of p_n includes
the zero sample. Absolute physical summability gives the other limit.
Thus (17) is justified first for each n; the later uniform estimates
use (10)--(12) only after their common onset.

For (15), n*integral_L^infinity v*exp(-n*v/5)dv equals
(5*L+25/n)*exp(-n*L/5), with L=9/4. Its bounded prefactor gives
the exact rate 1/25. On the negative half-line
integral_(-infinity)^0 |v|*exp(c_0*v/h)dv=h^2/c_0^2,
which confirms (16). Both signs of l, including l=0, are retained
in (18); pi>3 suffices for the displayed positive-alias rate.

The first omitted absolute unshifted position is exactly
h*(2q+1/2)=Y. The worst shift and n>=15 therefore give (14)'s
strict lower bound above 2/5. The comparison
|m+1/2+e_m|>=(3/4)|m+1/2| and the integral tail of x^(-2)
give (19) with its stated constant; 2q-1/2>=n/10 follows from q>=1.
Every retained nonanchor has |m+1/2+e_m|<=2q-3/8 and hence |y_m|<Y.
The anchor satisfies the same bound on |a|. Thus rho^2=2824/3025
controls all M atoms in T_n. Its full Mth power and the global (8)
bound give exponent at most
n*(1/120-67/6050)=-199*n/72600<-n/400.
This verifies (20) without discarding a moment or physical endpoint.
The largest remaining correction is O(n*exp(-n/500)); absorbing n
proves (1) with a common existential onset and profile-dependent C.

**Same sampled germ and conclusion.** The accepted L721 germ concerns
exactly n^(-1/2)K_n on n=12q+3. Its coefficient limsup gives radius
R_*=exp(-12*r(b)); multiplication by n^(-1/2) and finite omitted
samples do not change it. The epsilon coefficients have radius at
least exp(12/1000)>1; the anchor coefficients converge on |z|<1.
Since r(b)>1/200, z_* lies strictly inside that unit disk. Equality
(21) therefore holds on the original common disk and continues the
same germ. A continuation of F through z_* would continue Kcal=H-F
there, contradicting the accepted input. The correction introduces
no nearer obstruction. The direct subsequence argument after (21)
also proves the equal limsup when some coefficients vanish, with
log(0)=-infinity. No full rate limit or angular integral follows.

The audit has clarified the density representative and the fixed-n
Poisson argument before the uniform onset, and independently supplied
the complete interval check. No hypothesis, constant, conclusion or
direct mathematical input has changed. In particular L722's audited
subordination stop is preserved. The unresolved qualifications in
the Conclusion remain essential.

## Mathlib

Full matching coverage has not been checked. Coverage of the particular
complex-measure tilt, rational interval certificate and sampled endpoint
specialization is not established here. Standard Fourier, power-series
and dominated-convergence results are supporting tools, not a checked
formalization of this lemma. Unknown coverage is not evidence of absence.
