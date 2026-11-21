# C744w: A complete separation-seven Schur certificate

## Hypotheses

Use C744v's notation, complete response identity and operator extension.
Thus ell=log(3)/2; N is the complex C_c^infinity(0,ell) functions
whose two integrals against exp(x/2) and exp(-x/2) vanish exactly;
d(f)=H(f,f), q_7(f)=H(f,tau_(7ell)f). In the orthonormal cosine
basis, P retains indices 0 through511, Q=I-P, and

    A_theta=D+S+256 C*C+V_theta,
    V_theta=(exp(i theta)T+exp(-i theta)T*)/2.

C744v supplies ||T||<4.71, QA_theta Q>=tau Q for tau=143/100,
the equality with d-Re(exp(i theta)q_7) on N, and the sufficient
residual R_theta=PA_theta P-F_theta*F_theta/tau,
F_theta=Q(S+256C*C+V_theta)P. All sixteen prime powers and the
continuous response of that result are retained. None of its
previous finite-locator signs is an input.

The imported analytic input remains Hongmin Li, *Cutoff-free positivity
of localized Weil forms through the (log 11)/2 threshold*,
[paper45, displayed v2, 9 November2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma3.1, (2.1)-(3.4), specialized in C744v(4),(9); the complete
Schur precedent is (4.7)-(5.5). No numerical supplement or endpoint
sign is imported. The scalar remainder uses L744's sector-bound
argument for [DLMF5.11.2](https://dlmf.nist.gov/5.11.E2)
and [5.11(ii)](https://dlmf.nist.gov/5.11#ii), now at the shifted
argument specified below. These inputs and this
fixed comparison were covered before invocation by assessment529/530.

The computational contract is IEEE754 binary64 round-to-nearest for
basic operations, correctly rounded square root, and the usual
dot-product error bound gamma_r=ru/(1-ru), u=2^-53. A dot product
implemented with fused multiply-add has no larger error. There is no
overflow, and all quantities on which relative bounds are used are
normal. Zero and negligible underflowed values may instead be charged
absolute error 10^-300, much smaller than the allowances below.
Decimal operations use the directed contract specified in C744v.
No accuracy contract for a library sine, cosine, logarithm, digamma,
eigenvalue or Cholesky routine is presumed: elementary functions are
evaluated as described below, and proposed Cholesky factors are checked
by their full reconstruction residuals.

This is a new local fixed-separation comparison under the assessed
method, classified POTENTIALLY_NEW because no matching statement was
located in that assessment. This is not a claim of mathematical
originality. The separate step534 conceptual audit below upholds
C744v and this certificate under the stated arithmetic contract;
neither is a complete RH candidate.

## Conclusion

For every real theta, the complete residual satisfies

    R_theta >= (1/40) I on ran(P).                       (1)

Consequently, for every f in N,

    |q_7(f)| <= d(f).                                   (2)

This covers all complex exactly neutral smooth profiles, hence also
any of C744r's smaller admitted H2 families at this one separation.
It supplies no control at other separations, no C744q strict margin,
no non-neutral sign and no global actual-Xi positivity. It is not an
off-line-zero exclusion or a resolution of RH.

## Proof

### 1. Finite covariance and exact infinite remainder

Fix K=65536, and let Q_< retain indices 512,...,K-1 and Q_>= retain
indices n>=K. These are subdivisions of Q, not a change in the
512-mode Schur interface. Put

    W0=S+256C*C,  Wc=(T+T*)/2,  Wg=(T-T*)/2,
    B0=Q_< W0P,  Bc=Q_< WcP,  Bg=Q_< WgP,
    B_theta=B0+cos(theta)Bc+i sin(theta)Bg.

Their matrices are real, with Wg skew-adjoint. The finite residual is

    R_<,theta=PA_theta P-B_theta*B_theta/tau.             (3)

The products computed are B0^t B0, Bc^t Bc, Bg^t Bg, B0^t Bc,
B0^t Bg and Bc^t Bg. The last three contribute, respectively,

    c(B0^t Bc+Bc^t B0),
    i s(B0^t Bg-Bg^t B0),
    i cs(Bc^t Bg-Bg^t Bc),                              (4)

where c=cos(theta), s=sin(theta). The other three have coefficients
1,c^2,s^2. Thus all six covariance types, including their imaginary
mixed terms, are present. Orthogonality of the two output ranges gives

    F_theta*F_theta=B_theta*B_theta+G_theta*G_theta,
    G_theta=Q_>=(W0+V_theta)P.                           (5)

There is no omitted mixed product between these two orthogonal ranges.
We bound the whole G_theta, retaining all mixed products within it.

### 2. Entire covariance tail

Write k_n=n*pi/ell, nu_0=ell^-1/2 and nu_n=sqrt(2/ell) for n>0.
C744v(9) gives zero response entries between opposite parities. For
the same parity, n>=K and m<512, comparison of the decreasing sum
with its integral gives

    sum_(j>=0) 1/(c_j^2+k_n^2) <= 1/k_n^2+pi/(4k_n),
    c_j=2j+1/2.

Indeed the sum is at most its first term plus half the integral from
c_0 to infinity. Bound that integral by the one starting at zero.
The exponential addition for odd parity is at most

    sum_j exp(-ell c_j)/k_n^2
      =[3^(-1/4)/(1-1/3)]/k_n^2.

Since alpha_n alpha_m=2nu_n nu_m<=4/ell in C744v(9), this proves

    |S_nm| <= 1/n+b/n^2,
    b=4ell[1+(3/2)3^(-1/4)]/pi^2.

There are exactly256 retained indices of each parity. Using
sum_(n>=K)n^-2<=1/(K-1) yields the Hilbert--Schmidt bound

    ||Q_>=SP|| <= sqrt(256/(K-1)) (1+b/K).              (6)

For a single shift delta with |delta|<ell, its normalized entry is
nu_n nu_m times the integral of cos(k_n x)cos(k_m(x+delta)) over
the overlap. For n>m, an antiderivative is

 [k_n sin(k_n x)cos(k_m(x+delta))
       -k_m cos(k_n x)sin(k_m(x+delta))]/(k_n^2-k_m^2).

At one overlap endpoint sin(k_m(x+delta)) is zero, and at the other
sin(k_n x) is zero. Therefore its absolute entry is at most
2/[pi(n-m)]. This argument applies to delta and -delta, so it
controls both T and T* without a symmetry assumption about T.
If a=sum_(n in P7) Lambda(n)/sqrt(n), the complete prime part J obeys

    ||Q_>=JP||, ||Q_>=J*P||
       <= (2a/pi) sqrt(512/(K-512)).                     (7)

Here sum_(n>=K)(n-511)^-2<=1/(K-512). For the remaining continuous
operator, its entire norm kappa from C744v(2), rather than a truncated
tail, bounds both projected operators.

The exact moment entry with exponent c=+/-1/2 is

    C_cn=nu_n c[(-1)^n exp(c ell)-1]/(c^2+k_n^2).

For n>=K its absolute value is at most beta/n^2, where

    beta=sqrt(2/ell)(3^(1/4)+1)ell^2/(2pi^2).

Also ||C||<=||C||_HS=sqrt(sqrt(3)-1/sqrt(3)). Hence

    ||Q_>=256C*CP||
      <=256 sqrt(sqrt(3)-1/sqrt(3)) beta
                                     sqrt(2/[3(K-1)^3]). (8)

Equations (6)-(8), the triangle inequality and the two equal
coefficients in V_theta give, uniformly in theta,

    ||G_theta|| < 0.495202 < 1/2.                        (9)

The directed scalar calculation uses pi>3.14, which follows already
from Archimedes' lower bound 223/71. Thus it does not depend on the
floating pi used to assemble matrices. Its separate contributions
are less than 0.062501, 0.432594, 0.000106 and 0.000000906,
respectively. Their full intervals are in the certificate's
`scalar_tail_certificate`. In particular

    G_theta*G_theta/tau <= (25/143)I < .175 I.           (10)

This pays every omitted mode and all of its mixed covariance.

### 3. Finite entries and source-approximation errors

All retained matrices and the six covariance matrices are saved in
`scripts/separation-seven/complete-covariance-532.npz`. They are
assembled in blocks of512 rows; no finite block is discarded.

Here are the complete scalar formulas and analytic error bounds.
For the non-exponential part of a response entry put

    U(k)=sum_(j>=0)1/(c_j^2+k^2),
    b(k)=k Im psi(1/4+ik/2)/2=k^2 U(k).

The second equality follows from the exact recurrence for psi(z+J)
and then J->infinity: the cited asymptotic makes Im psi(z+J)->0,
while the imaginary parts of the recurrence summands converge
absolutely as O(j^-2). For unequal k,l,

    sum_j c_j^2/[(c_j^2+k^2)(c_j^2+l^2)]
      =[b(k)-b(l)]/(k^2-l^2).                           (11)

At k=0 set b(0)=0 exactly. Evaluate psi via the exact recurrence
psi(z)=psi(z+64)-sum_(j<64)1/(z+j), and approximate only
psi(z+64) by log(z+64)-1/[2(z+64)]. The cited remainder gives

    |psi(z+64)-log(z+64)+1/[2(z+64)]|
       <=r(k)=sqrt(2)/[6(64.25^2+k^2/4)].                (12)

Here z+64 has positive real part and |arg(z+64)|<pi/2, so the
same sector multiplier at most2sqrt(2) used in L744 applies.
The exact digamma recurrence follows by logarithmically
differentiating the gamma functional equation Gamma(z+1)=z Gamma(z)
on this pole-free right half-plane.

Thus b(k)'s analytic error is at most kr(k)/2. For an off-diagonal
response entry the exact error bound, before multiplication by
2nu_n nu_m and the parity indicator, is

    [k_n r(k_n)+k_m r(k_m)]/[2|k_n^2-k_m^2|].           (13)

On the response diagonal the sum in (11) is evaluated directly
through j=65535 and supplemented by 1/(2c_65536). Its error is at
most c_J^-2+2k_n^2[1/(6c_J^3)+c_J^-4], J=65536, by the integral
comparison in C744v(10). This avoids a divided difference at equal
arguments or any unassessed differentiated asymptotic formula.

The exponentially weighted response is summed through j=63. Since
exp(-ell c_j)=3^(-j-1/4), its omitted sum, after normalization, is
less than10^-30 even at n=m=0. The cross continuous operator is
summed for j=1,...,7; C744v(2)'s geometric argument starting at8
bounds its remaining operator norm by less than10^-24. These errors
are included in the elementary entry allowance below. Both complete
infinite terms are thus retained through an error bound.

For the diagonal D, (12) bounds the error by r(k_n); no approximate
eigenvalue of D is used. Moments use their exact preceding formula.
For shift entries the antiderivative in Section2 gives, with
sigma=(-1)^(n+m),

    I_nm(delta)=[-sigma k_n sin(k_n delta)+k_m sin(k_m delta)]
                   /(k_n^2-k_m^2), delta>0,
    I_nm(delta)=[k_n sin(k_n delta)-sigma k_m sin(k_m delta)]
                   /(k_n^2-k_m^2), delta<0.

When n=m>0 use instead

    I_nn(delta)=(ell-|delta|)cos(k_n delta)/2
                 -sign(delta)sin(k_n delta)/(2k_n),

and I_00=ell-|delta|. Multiply by nu_n nu_m and the exact prime
weight, and sum all sixteen terms. These formulas also verify the
adjoint block by replacing delta with -delta.

### 4. Elementary arithmetic ledger

The following deliberately coarse absolute allowances permit an
ordinary floating implementation to produce a checkable certificate.
They cover evaluation of the approximating formulas; the analytic
errors (12)-(13) are charged separately, not hidden in rounding.

Constants ell, 3^(1/4), prime weights, delays and log(pi) are formed
at80 Decimal digits and rounded once to binary64. The displayed pi
decimal can be bracketed by Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), using the alternating power series
through80 terms and the first omitted term. The analytic truncation
error is below10^-110; the saved directed60-digit enclosure verifies
the displayed decimal to10^-55 and the binary64 value to2*10^-16.
Each used constant's relative error is below2u (zero
constants are exact); delay absolute errors are below10^-16.

For sine and cosine, round x/(pi/2) to a nearest integer q and
evaluate the degree21/20 Taylor polynomials at x-q*pi/2. The reduced
argument has absolute value below.786; the Taylor remainder is less
2*10^-22. Changing reduction at a tie causes no problem because
both representations agree by the exact quadrant identities, and
the argument error is bounded in either representation. Here
|x|<207000. Direct propagation of at most40 operations with unit
roundoff u gives absolute sine/cosine error below

    10^-14(1+k_n) for x=k_n delta.                      (14)

In particular this is below4*10^-9 over all used rows and below
3.1*10^-11 on the head. For the phase arguments it is below10^-12.
To check (14), |k_n-true(k_n)|<=8u k_n, |delta error|<10^-16;
range reduction contributes at most 4u|x|+3u. Taylor arithmetic on
the reduced interval contributes less100u. Their sum is strictly
below (14), including n=0 (whose sine is exact).

The imaginary logarithm in (12) uses arctan. Reduce a nonnegative
argument using arctan(t)=pi/2-arctan(1/t) when t>1 and then apply
t -> t/(1+sqrt(1+t^2)) three times. The remaining t is at most
tan(pi/32)<.099. Ten alternating terms and multiplication by8
have truncation error below10^-21 and rounding error below10^-13.
The real logarithm needed for D is evaluated by80-digit Decimal.
The64 recurrence terms have total absolute size below130; the
resulting rounding error in either component is below3*10^-12.

For an off-diagonal entry, k_n^2-k_m^2 is never evaluated near zero
without an explicit lower bound: it equals (pi/ell)^2(n-m)(n+m),
with |n-m|>=1. For unequal indices in this rectangle,
(n^2+m^2)/|n^2-m^2|<1024. Thus subtraction and input errors in the
denominator amplify by at most1024, giving relative error below
10^-11. In a shift entry, (14) contributes at most

    10^-14 [k_n(1+k_n)+k_m(1+k_m)]/|k_n^2-k_m^2|

before normalization; the ratio in this expression is below1025.
Normalization is below4, and the complete prime weight sum is below
7.654. Including product, denominator and summation errors bounds
the complete prime-entry error by10^-8. The diagonal formulas are
bounded more directly and satisfy the same allowance.

For (11), the recurrence error contributes at most
1.5*10^-12(k_n+k_m)/|k_n^2-k_m^2| before normalization.
Its denominator roundoff and the64 exponential terms are below
10^-8 per normalized entry. The diagonal positive sum has value
below20 after normalization; even a sequential65536-term sum has
gamma_65536<8*10^-12, giving error below2*10^-10. The moment penalty
has entries below400, with evaluation error below10^-9. The
continuous entries and their arithmetic errors are smaller. Hence
the single allowance

    epsilon_entry=10^-7                                 (15)

for each assembled W0,Wc,Wg entry, and for the elementary part of
D, strictly dominates the errors just listed and the bounded tails.
The D allowance fits inside the W0/head allowance: their combined
elementary error is below10^-7, not two unexplained copies of it.

Let e_H be the Frobenius norm of the head response error matrix
(13) including its diagonal bound, plus max r(k_n) for n<512.
Let e_Q be the Frobenius norm of (13) over512<=n<K, m<512. Every
entry of these nonnegative error matrices is evaluated. They give

    e_H<.000184,                 e_Q<.000000181,
    ||B0_hat||_F<.586, ||Bc_hat||_F<1.485,
    ||Bg_hat||_F<1.091.                                  (16)

The subscript hat denotes the stored approximation. With

    e_F=e_Q+3 sqrt((K-512)*512)*10^-7,
    e_M=e_H+3*512*10^-7,

the exact finite factors differ by at most e_F uniformly in phase,
and the exact finite head by at most e_M. Symmetrizing the head
cannot enlarge these errors, since the true head has the stated
symmetry. Thus the norm error of (3) at a sampled phase is bounded by

    e_M+[ (2 sum_j||Bj_hat||_F+e_F)e_F+10^-6]/tau
      < .012.                                           (17)

The extra10^-6 covers all covariance dot products and subsequent
matrix arithmetic. For completeness, the basic bound used is
||fl(X^tY)-X^tY||_F<=gamma_(2b)||X||_F||Y||_F for real b-row
blocks (apply the entrywise dot bound, then Cauchy--Schwarz).
Sum this over the127 blocks and charge the127 accumulation steps.
Equation (16) gives total squared factor norms below5; with b=512,
the resulting error is below10^-9 even after all six products and
their phase coefficients are included. Formula/norm rounding in
(16)-(17) is below10^-8 of the .012 budget: the computed debt is
less .007991, leaving more .004 of slack. No displayed floating
last digit is used as an exact endpoint.

### 5. Verified finite phase checks and interpolation

For j=0,...,64, theta_j=j*pi/64, the script proposes a Cholesky
factor L_j for R_hat_<,theta_j-.24I. It saves every complex factor
in `scripts/separation-seven/phase-cholesky-factors-532.npz` and
checks the complete Frobenius reconstruction residual. Every residual
is below10^-7, every factor has squared Frobenius norm below10000
(the maximum is below2824), and all matrix entries have absolute
value below400. The complex dot-product bound, with gamma_(8*512),
therefore makes the exact reconstruction error less10^-6. Indeed
gamma_(4096)||L_j||_F^2<5*10^-9; addition, norm evaluation and
formation of the phase matrix fit inside the remaining allowance.
The approximated phase arguments differ from theta_j by less10^-14;
their arithmetic is also covered. Consequently, since L_j L_j*>=0,

    R_<,theta_j >= (.24-.000001-.012)I.                  (18)

The Cholesky routine is only a factor proposer; (18) follows from
its saved entries and checked multiplication, not a success flag.

The exact finite ||B0|| is below.7 by (15)-(16). Projection is
contractive, so ||B_theta'|| and ||B_theta''|| are at most4.71,
||B_theta||<=.7+4.71, and ||(PA_theta P)''||<=4.71.
Differentiating the finite covariance therefore gives

    ||R_<,theta''||
      <=4.71+2[4.71^2+(.7+4.71)4.71]/1.43 <72.           (19)

This bound is for the exact phase family, including all complex
mixed terms. On an interval of width h, the scalar second derivative
bound B implies that the function is at least its linear endpoint
interpolation minus Bh^2/8. Apply this elementary statement to
<R_<,theta v,v> for every unit v. One proof subtracts the endpoint
interpolant and compares with +/-B(t-a)(b-t)/2 using convexity.
Here h=pi/64 and the debt in (19) is less.022. Real coefficients
give R_<,-theta=conjugate(R_<,theta), and the family is2pi-periodic,
so the65 checks cover every real phase, not only[0,pi].

Finally combine (5),(10),(18),(19). The complete residual is at least

    [.24-.000001-.012-.022-.175]I
       =.030999 I > (1/40)I.                            (20)

This proves (1). C744v's full form-domain Schur completion proves
A_theta>=0. On an original exactly neutral compact smooth f it is
exactly d(f)-Re(exp(i theta)q_7(f)); the moment penalty vanishes.
Taking all phases gives (2). There is no smooth-density step from
the computed cosine vectors and no approximate neutrality argument.

### 6. Reproduction and limits

Run from this notebook:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/residual-certificate-532.py

The full scalar ledger and all65 phase checks are in
`scripts/separation-seven/complete-residual-certificate-532.json`;
the two binary artifacts named above contain every covariance matrix
and proposed factor. The script reports the actual bounds, rational
allowances, required threshold zero and failures. Its reported
uniform lower bound uses the rounded debts in (20), not unrounded
floating endpoints. The mathematical proof of the allowances is
Sections2-5; running a script alone is not their justification.

The earlier `scripts/separation-seven/residual-locator-532.json`
records the initial, explicitly uncertified4096-mode diagnostic and
is preserved. Its samples are not used in the proof. K=65536 pays
the covariance tail without changing the target or the frozen
N=512, penalty256, tau=1.43. This specialization imports the known
response and Schur tools; it does not reprove their source theorems.
Its independent arithmetic and analytic audit is recorded below.

### 7. Separate conceptual audit — 12 November 2026, step534

**Result.** The original fixed certificate is upheld under the
explicit IEEE754/Decimal execution contract in the Hypotheses.
The independently checked final lower bound is still .030999>1/40;
N=512, penalty256, tau=1.43, K=65536 and every phase are unchanged.
This is REPRODUCTION: validation of the existing local input, not a
new fixed-separation inequality or a claim beyond the sources checked.

C744v Section7 checks the imported response identity, both exact
moments, complex cross-pairing orientation and the closed-form Schur
domain. Here the covariance split (5) is orthogonal in its output
indices, so no mixed term connects Q_< to Q_>=. Within either range
all products remain. In the finite range, expanding
(B0+c Bc+i s Bg)^*(B0+c Bc+i s Bg) gives precisely (4) and the
three diagonal products. In the infinite range, the triangle bound
on G_theta bounds their complete combined quadratic form; no
individual mixed covariance is discarded.

The tail estimates were checked directly. The decreasing resolvent
sum in (6) is bounded by its first term plus half its integral;
the parity count is256, not512. For either sign of a shift, the two
overlap endpoints in the antiderivative leave a numerator of size
at most k_n+k_m. Multiplication by nu_n nu_m<=2/ell gives
2/[pi(n-m)], proving (7) for T and T* separately. In (8), the
Hilbert--Schmidt norm of C is exactly
sqrt(integral_0^ell(exp(x)+exp(-x))dx)
=sqrt(sqrt(3)-1/sqrt(3)). The tail of each moment is bounded by
beta/n^2. Integral comparison from K-1 pays the entire squared tail.
The complete directed replay gives

    response tail < .062500932,
    prime tail < .432593543,
    continuous tail < .000105742,
    moment-penalty tail < .000000906,
    ||G_theta|| < .495201122 < 1/2.

Thus (10) pays every omitted mode using the original tau. These
are operator bounds, not a comparison of sampled eigenvalues.

For (11), the absolutely convergent imaginary-part recurrence gives
b(k)=k^2 sum_j(c_j^2+k^2)^(-1), including b(0)=0. Subtracting two
such fractions gives the displayed divided difference. DLMF5.11(ii)
with n=1, at z+64=64.25+ik/2, bounds the remainder after log(z+64)
-1/[2(z+64)] by (1/12)|z+64|^-2 times at most2sqrt(2).
This is exactly (12), not an asymptotic assertion without remainder.
Equation (13), the direct equal-index sum and both exponential-tail
charges therefore cover the analytic approximation. There is no
differentiation of an unassessed remainder at equal indices.

The elementary error ledger has ample slack, but it is still needed.
For unequal indices in the used rectangle, the integer identity
n^2-m^2=(n-m)(n+m) gives the stated ratio bound<1024. The sine
input/reduction errors in (14), propagated through the shift formula,
contribute less than4*7.654*1025*10^-14<3.2*10^-10 per complete
prime entry before the separately charged product and denominator
errors. Those other errors fit within10^-8. The factor2nu_n nu_m
in response entries is at most8, and
(k_n+k_m)/|k_n^2-k_m^2|=1/|k_n-k_m|<=ell/pi<.175.
Consequently the recurrence rounding part of (13)'s evaluation is
less than8*(1.5*10^-12)*.175; denominator, exponential and diagonal
summation errors remain within the stated10^-8 entry charge. The
moment penalty and real diagonal evaluation fit in the single10^-7
assembled allowance, including their combined head contribution.
The positive error-matrix summations have no cancellation; their
roundoff is dominated by the slack in (16)-(17).

One implementation detail is checked without assuming an extra
transcendental contract: the generator uses float 3**(-j). The
audit converts each of its64 possible results to its exact dyadic
rational and proves |float(3**(-j))*3^j-1|<2^-52 by integer
arithmetic. This includes every exponent6j used by the continuous
part. Thus a library-power accuracy assumption is unnecessary.
Machin's directed enclosure validates the pi constant separately.

The complete covariance replay regenerated every row through65535
and all six products. All nine saved matrices (three head matrices
and six products) agree bit for bit with the originals. Their
Frobenius error ledger is

    e_H < .000184, e_Q < .000000181,
    factor norms < .586, 1.485, 1.091,
    finite Schur debt < .007991 < .012.

This replay validates the saved evidence, not the analytic entry
allowance by itself. That allowance is justified above and in
Section4. The blocking uses127 disjoint512-row pieces. Summing
the real dot-product bounds gamma_(1024)||X_b||_F||Y_b||_F and
using Cauchy--Schwarz across blocks proves the claimed total-product
bound; the127 accumulation errors and subsequent phase arithmetic
fit within10^-6. No statistical or independent-error assumption is
used. The dyadic encodings of1.43 and.24 introduce only elementary
rounding, already covered by this allowance and the reconstruction
allowance, respectively.

Every entry of all65 original factors was loaded. The audit forms
each full residual against the regenerated matrix, without proposing
new Cholesky factors. Its Frobenius norms and factor squared norms
are evaluated using separate real and imaginary squares, avoiding
any extra accuracy assumption for complex abs/hypot. Every observed
full reconstruction norm is less than6*10^-14<10^-7, and every
factor squared Frobenius norm is below10000. The complex product
error is bounded by gamma_(4096)*10000<5*10^-9; real-square norm
rounding and subtraction errors are far inside the10^-6 allowance.
Thus positive semidefiniteness follows from the stored LL*, even
without trusting the factorization routine or its success flags.

Finally the exact derivative bounds in (19) use
||V_theta'||,||V_theta''||<=||T||<4.71 and ||B0||<.7. Applying
the scalar second-derivative comparison to every unit vector gives
the operator bound between successive phases. Conjugation covers
negative phases and periodicity covers the rest. The exact rational
debt is .24-.000001-.012-.022-.175=.030999>.025, proving (1).
The penalty vanishes on the exact neutral class, so the full-domain
Schur comparison proves (2), including complex f and q_7(f)=0.

Reproduce from the notebook, preserving the original artifacts:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/certificate-audit-534.py
    python3 scripts/separation-seven/certificate-audit-534.py --contract-only

Full audit results, scalar data, all65 reconstruction checks, all
nine matrix comparisons and original artifact hashes are saved in
`scripts/separation-seven/certificate-audit-534.json`. Exact rational
power checks and runtime identification are in
`scripts/separation-seven/runtime-contract-534.json`. The regenerated
full covariance is in
`scripts/separation-seven/audit-replay-534/complete-covariance-532.npz`.
The runtime reports Python3.15.2, NumPy2.5.4, OpenBLAS0.3.34,
Darwin arm64 and fegetround=0. This records the execution setting;
it is not a formal verification of the interpreter, compiler or BLAS.
The standard execution contract remains an explicit computational
hypothesis, as it was in the original certificate. No interval
hardware or source numerical supplement is being claimed.

No mathematical failure was found in this fixed certificate. Other
separations, C744q's strict margin, non-neutral directions and global
assembly remain open. In particular a single separation supplies
no uniform-in-m premise for C744r and no RH candidate. Full matching
Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this localized response identity and
fixed-separation certificate has not been checked. No full Mathlib
theorem is asserted. Schur completion, Hilbert--Schmidt bounds,
finite-dimensional positive semidefiniteness and interpolation are
supporting mathematics; none by itself supplies (2) or RH positivity.
