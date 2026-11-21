# Corollary C033u: logarithmic ellipse majorant and uniform prime-cost stop

## Hypotheses

Retain C033s/t's exact finite approximants, order128, cuts a=2^-256,
b=2^256, n=1, delta=1/16, and real signed width measures of mass one
and TV at most2 on [1,2]. Retain the full actual positive-ordinate
divisor with conjugation and multiplicity, excluded ordinate zero,
strict strip, gamma>14, explicit counting, real zeros through100,
retained real zero in(14,15), reciprocal-square tail, heat positivity,
separate fixed-j heat errors through j=2, Gaussian half-variance and
both fixed-v1 preprint qualifications. Neither those sources nor zero
data are independently certified here. C033s/t remain unaudited inputs.

Use C032w's unconditional complex-divisor explicit formula. Write
F(w)=p_w(0), initially for real w>0, and use its continuation specified
below. For real sigma in[1,2], complex y, and s>=0 set

    w_sigma(y)=sigma+exp(-y)/4,
    d_sigma(y)=sqrt(pi)*exp(-y/2)*(F(w_sigma(y))-F(w_1(y))),
    d_sigma,s(y)=exp(-s*exp(y))*d_sigma(y).

The mass Mc_sigma and the four q_sigma(s_i) in C033t are the integrals
of these functions on [-256*log(2),256*log(2)], with s=0 or its four
positive nodes. The P integrands for m and p(s_i) are

    f_s(y)=sqrt(pi)*exp(-y/2)*F(1+exp(-y)/4)*exp(-s*exp(y))

on [0,log(3/2)]. These identities retain the finite polynomial,
normalizations, signs and zero atoms from C033t. No positivity of
Qc_sigma, eta, or the paired observable is assumed.

For the cost statement specify THIS branch:128 equal logarithmic
panels for Mc and q, a Bernstein ellipse with parameter rho=2 on each
panel, and a common Gauss degree selected by the allowance below.
At every real node, evaluate the combined width-difference prime sum
directly with every prime power up to a common dyadic cutoff N=2^k,
k>=2. Use the uniform pointwise prime-tail allowance below and the
positive Gauss weights. No node-dependent omission or rearrangement
of the prime sum across outer quadrature is part of this branch.
Share a node's d_sigma value among all five scalar integrals; the stop
counts only Mc at one nontrivial width, such as sigma=2.

## Conclusion

F has a holomorphic continuation to Re(w)>0. For v=Re(w)>=1,

    |F'(w)|<17/v.                                      (1)

The functions d_sigma,s are holomorphic on |Im(y)|<pi/2 and satisfy,
uniformly for all real Re(y), sigma in[1,2] and s>=0,

    |d_sigma,s(y)|<64,  |Im(y)|<=11/10.                 (2)

In particular this pays the complex-domain callback majorant over
the enlarged widths, without losing small-time cancellation. The same
bound64 holds for f_s on the rho=2 ellipse of [0,log(3/2)].

Allocate each scalar error2^-112 from C033t in four parts2^-114:
outer quadrature, prime truncation, archimedean integration, and all
node/weight/elementary arithmetic. The real exact-node outer Gauss
allowance for Mc or q is

    E_quad(n)=819200*4^(-n).

Its least accepted degree is67, giving128*67=8576 outer nodes. A valid
allowance for the entire weighted prime-truncation error is

    E_prime(N)=256*exp(-(log N)^2+log(N)/2).             (3)

For N=2^k its acceptance at2^-114 is exactly

    k^2*log(2)>=122+k/2.

The least accepted dyadic exponent is14. There are1961 prime powers
up to16384, including1900 primes. Consequently the specified branch
requires, for Mc at one nontrivial width alone,

    8576*1961=16817536 > 10000000                       (4)

elementary node/prime-power terms. This generously counts one combined
term for the two widths, and grants every other cost for free. The
aggregate preflight therefore fails before numerical evaluation.
Neither an archimedean implementation nor a512-bit arithmetic guarantee
is claimed. C033t's conditional final-error allocation remains unchanged.

This is a failed sufficient certificate for the stated nested rule,
not a lower bound on actual error, necessary scalar precision, adaptive
quadrature, separated prime integration, or all analytic evaluators.
It is a local specialization of the assessed sources, checked in
critical audit1784 below, not progress beyond their general theorems
or a result about RH. C033s/t remain conditional and unaudited.

## Proof

### Sources and applicability

Use the prior SPECIALIZE assessment1780. Import the explicit formula
from A. Connes, *Heat Expansion and Zeta*,
[arXiv:2402.13082v1, Section2/(4)-(9), p4](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf),
in C032w's Gaussian normalization. The even-test hypotheses are also
stated in A. Chirre and F. Goncalves, *Bounding the log-derivative of
the zeta-function*,
[arXiv:2103.06237v2, Proposition5, pp3-4](https://arxiv.org/pdf/2103.06237v2).
No RH-dependent spectral rewriting is used. C033t already supplies
the finite signed-transform product and scalar error propagation; no
convolution theorem is reproved here.

For analytic Gauss quadrature import F. Johansson, *Numerical
integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1, Section2, p2, and Section2.1, p3](https://arxiv.org/pdf/1802.07942v1).
On [-1,1], an analytic function bounded by M on the closed Bernstein
ellipse has n-point Gauss error at most M*C_rho*rho^(-2n), with
C_rho<50 for rho>1.1. Rescaling multiplies this by half the interval
length. The statement does not supply application majorants or
certified callback cost. Those are precisely the work here. Positive
Gauss weights sum to the interval length; this is the standard
Gauss-Legendre rule used by the cited algorithm. Precision settings
alone are not certified error bounds, as its Section2.1 emphasizes.

### Enlarged complex widths

Put B(t)=exp(t/2)/(exp(t)-exp(-t)), c=log(4*pi)+gamma_E and
A(w)=exp(1/(16*w))/sqrt(4*pi*w), using the principal square root.
C032w(1), at spatial argument zero, becomes

    F(w)=A(w)-c/(4*pi)
      -(1/(2*pi))*integral_0^infinity
                  (exp(-w*t^2)-exp(-t/2))*B(t)dt
      -(1/(2*pi))*sum_(n>=2) Lambda(n)/sqrt(n)
                                      *exp(-w*(log n)^2).       (5)

For any compact subset of Re(w)>0 let v0 be its positive minimum
real part and W0 its maximum modulus. Near zero, the combined
integrand has magnitude at most (W0*t^2+t/2)*B(t); C032w gives
B(t)<=1/t for t<=1. For t>=1 use B(t)<=2*exp(-t/2) and
exp(-v0*t^2). These are integrable bounds. The prime series and its
width derivatives converge normally: factors polynomial in log(n)
times exp(-v0*(log n)^2) beat any fixed power of n. Thus (5) is
holomorphic, with differentiation under the combined integral and
series justified by compact domination. The archimedean subtraction
is never split into two divergent integrals at zero.

For real w>0, the source's Mellin test exp(-w*(log v)^2)/(2*pi),
times v^-1/2, satisfies the endpoint decay and smoothness hypotheses
by Gaussian domination. The same Gaussian transform and divisor
pairing as C032w therefore identify (5) with the actual profile at
every such width, not only [1,2]. This checks the changed width range;
it does not reprove the explicit formula. It also justifies the real
logarithmic integrands in the hypotheses by substituting
u=1/(4*w_sigma). The source's full divisor and half-variance remain.

Differentiating (5) gives

    F'(w)=A'(w)+(1/(2*pi))*integral t^2*exp(-w*t^2)*B(t)dt
             +(1/(2*pi))*sum Lambda(n)/sqrt(n)*(log n)^2
                                                *exp(-w*(log n)^2).

Let v=Re(w)>=1. Since |w|>=v,
|A'(w)|<=exp(1/16)/(2*sqrt(pi*v))*(1/(2*v)+1/(16*v^2))<1/v.
The integral without its prefactor is at most

    integral_0^1 t*exp(-v*t^2)dt
      +2*integral_1^infinity t^2*exp(-v*t^2)dt
    <=1/(2*v)+sqrt(pi)/(2*v^(3/2))<3/(2*v).

In particular the archimedean derivative is less than2/v.
For l=log(n), the inequality x*exp(-x/2)<=2/e<1 gives

    l^2*exp(-v*l^2) <= v^-1*exp(-l^2/2).

Using Lambda(n)<=n and sum_(n>=2)n^-2<1,

    sum Lambda(n)/sqrt(n)*exp(-l^2/2)
      <=sum n^-2*exp(-l^2/2+(5/2)*l)
      <exp(25/8)<81.

Since2*pi>6, the prime derivative is less than(27/2)/v.
The sum of the three allowances is less than(33/2)/v<17/v,
proving(1). None of these bounds requires a sign of the heat profile.

### Cancellation on the logarithmic ellipse

Write y=x+i*z and r=exp(-x/2). On |z|<=11/10,
cos(z)>=1-z^2/2>=79/200. Along the real width segment from1 to sigma,

    Re(w_tau(y))>=1+(79/800)*r^2.

Integrate F' along this segment, whose length is at most1. Equation(1)
and sqrt(pi)<2 give

    |d_sigma(y)| < 34*r/(1+(79/800)*r^2)
                <=34*sqrt(200/79)<64.

The last inequality is equivalent after squaring to231200<323584.
This difference estimate, rather than two separate F bounds, pays
the small-time cancellation. Also
|exp(-s*exp(y))|=exp(-s*exp(x)*cos(z))<=1. All compositions are
holomorphic on |Im(y)|<pi/2 because Re(w_sigma)>0 there. This proves(2).

For the P interval let L=log(3/2)<1/2. Its rho=2 ellipse has
real coordinates in[-L/8,9*L/8] and imaginary coordinates at most
3*L/8. Hence Re(w_1)>1 and |w_1|<2 on that ellipse.
In (5), the pole and constant each have modulus below1 (the latter
constant is bounded in C032w). The archimedean integral before its
prefactor is bounded by3/2 on(0,1) and by4 on(1,infinity).
The prime sum is at most exp(25/16)<9, by completing the square
in -l^2+(5/2)*l; its prefactor is below1/6. Thus |F(w_1)|<12.
Moreover sqrt(pi)*exp(-x/2)<2*exp(1/32)<4 and the Laplace factor
has modulus at most1. Consequently |f_s|<48<64 on this ellipse.

### High-order outer allowance

Each of the128 panels has length4*log(2). Its rho=2 ellipse has
imaginary semiaxis(3/8)*4*log(2)=(3/2)*log(2)<11/10.
Thus(2) is a valid uniform majorant including panel endpoints.
Summing the imported Gauss errors over the panels gives

    error <(512*log(2)/2)*50*64*4^(-n)
          <819200*4^(-n)=E_quad(n).

The entire P interval would use a smaller allowance with the same
degree. No quadrature nodes need to be generated to check this bound.
At degree67, E_quad<2^-114; degree66 fails this displayed allowance.
This justifies the selected degree, not a lower bound on actual error.

### Every omitted prime power and the weighted callback error

At a real node y, with r=exp(-y/2), the prime part of d_sigma is

    -(r/(2*sqrt(pi)))*sum_(n>=2) Lambda(n)/sqrt(n)
      *exp(-(1+r^2/4)*(log n)^2)*(exp(-(sigma-1)*(log n)^2)-1).

The factor in parentheses has modulus at most1 for sigma in[1,2].
For l>0, r*exp(-r^2*l^2/4)<=sqrt(2/e)/l<1/l. Since
Lambda(n)<=log(n), the omitted terms above N>=4 are bounded uniformly
at every real node by

    (1/(2*sqrt(pi)))*sum_(n>N) n^-1/2*exp(-(log n)^2)
    <=(1/(2*sqrt(pi)))*exp(-(log N)^2+log(N)/2).        (6)

Indeed rewrite the summand as n^-2*exp(-l^2+3*l/2);
the exponential factor decreases for l>=log(N)>3/4, and
sum_(n>N)n^-2<=1/N. This includes all omitted prime powers by
dominating with all integers. It uses neither a prime-density
asymptotic nor numerical zero coordinates. The bound remains valid
after multiplying by any of the real Laplace factors, which lie in[0,1].

All real Gauss weights are positive and sum over the panels to
512*log(2). Therefore the difference between the exact Gauss sum
and the sum with truncated prime callbacks is at most this length
times(6). Since log(2)<sqrt(pi), (3) is a valid larger allowance.
This argument concerns the finite weighted callbacks, not an
unjustified exchange between quadrature error and integrated tails.

For N=2^k take logarithms of E_prime(N)<=2^-114 and divide by
log(2)>0 to obtain the stated acceptance test. The elementary bounds

    56/81 < log(2) < 25/36

follow from log(2)=2*sum_(j>=0)3^(-2*j-1)/(2*j+1): retain the
first two terms for the lower bound, and replace denominators for
j>=1 by3 for the upper bound. That convergent positive expansion
also follows by integrating the geometric series for1/(1-x^2)
on[0,1/3]. These rational bounds accept k=14 and reject k=13
and every k=2,...,12. Thus the declared uniform dyadic rule uses16384.

### Exact cost check and scope of the failure

The finite calculation

    python3 scripts/smoothed-law/paired_ellipse_preflight_1782.py

writes scripts/smoothed-law/paired_ellipse_preflight_1782.json.
It enumerates every prime power by a sieve and independently by
trial division, checking equality of the complete lists. The certificate
contains the complete prime-power list with base and exponent, exact
rational comparisons, and the resulting1961-term count. It proves(4)
for the specified term count without running any quadrature. Even the
1900 primes alone would exceed the total budget at these8576 nodes.

The chosen error allocation could imply the final2^-20 bound through
C033t if all four scalar parts and its final-expression allowance were
paid. Here the two analytic allowances are paid, but total cost already
fails. Archimedean quadrature, continuum-width representation, node
generation and512-bit arithmetic are consequently left unimplemented
and uncertified. This is a legitimate early preflight stop, not a
successful full evaluator or an observed error of the observable.

Adaptive prime cutoffs, integrating separated terms first, stronger
integrated-tail estimates, correlated scalar errors or a different
width representation could change the count. No impossibility for
those methods follows. After the distinct midpoint1781 and this
uniform nested-ellipse certificate have failed, park the present
numerical interface without erasing either obstruction. A reopening
needs a materially different, separately assessed cost mechanism.

### Critical audit1784, 19 November 2026

Audit target and coverage are exactly assessment1783's SPECIALIZE scope.
The analytic checks below use its inspected Haslinger,
[*Complex Analysis*, Theorem2.39, pp67-68](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
Johansson Sections2/2.1 cited above, and
[DLMF3.5(v), equations3.5.18,3.5.20_1,3.5.21](https://dlmf.nist.gov/3.5#v),
together with C032w's audited normalization. C033s/t and every inherited
actual-divisor qualification remain conditional. No failed hypothesis,
inequality or count was found in this scope. This is local verification
of existing claims, not a new estimate beyond the checked sources.
This audit does not reopen numerical evaluation.

The compact domination in(5) is valid: for Re(w)>0,
|exp(-w*t^2)-1|<=|w|*t^2 follows by integrating the exponential
on the segment from0 to w. The combined integrand on(0,1) is therefore
bounded by W0*t+1/2. At infinity, use
2*exp(-v0*t^2-t/2)+2*exp(-t). Width derivatives of order j>=1
are dominated near zero by t^(2*j-1), and at infinity by the same
Gaussian times t^(2*j). Counting measure supplies the corresponding
prime-series application of Haslinger: on a compact width set every
logarithmic derivative factor times exp(-v0*(log n)^2) is summable.
The principal square root is holomorphic on the right half-plane.
The Mellin Gaussian at each real w>0 satisfies the source hypotheses;
the paired divisor normalization is unchanged. Thus(5) identifies
the claimed extension, not merely an unrelated analytic function.

For(1), setting x=v*(log n)^2 gives
(log n)^2*exp(-v*(log n)^2)
 <=v^-1*(2/e)*exp(-v*(log n)^2/2)
 <v^-1*exp(-(log n)^2/2).
The three bounds1/v,2/v and(27/2)/v sum to(33/2)/v<17/v.
They are deliberately loose; no heat sign or differentiation of an
asymptotic remainder enters. Integration along tau in[1,sigma] is
inside Re(w)>=1+(79/800)*r^2. The maximum of
r/(1+(79/800)*r^2) is sqrt(200/79), and
34^2*200<64^2*79. The damping factor has modulus at most one
because cos(Im(y))>0. This verifies(2) and strip holomorphy.

The P ellipse has the stated axes. There Re(w_1)>1 and
|w_1|<=1+exp(L/8)/4<2. The absolute integral on(0,1) is
at most integral_0^1(2*t+1/2)dt=3/2; on[1,infinity) it is
at most(4/3)*exp(-3/2)+2/e<4. Thus the stated |F|<12 and
|f_s|<48 are valid. The conversion K(u)=sqrt(pi)*F(1/(4*u))
follows from the Gaussian normalization, so the d and P integrands
retain C033s/t's log-time Jacobian and half-variance.

Each panel's affine map has Jacobian2*log(2) and imaginary semiaxis
(3/2)*log(2)<11/10; its whole closed ellipse is inside the open
holomorphy strip. Johansson's M=64,C_2<50 bound therefore sums to
819200*log(2)*4^(-n)<E_quad(n). The same argument on the P
interval gives a smaller bound. For the displayed allowance,
E_quad(67)/2^-114=25/32<1, whereas
E_quad(66)/2^-114=25/8>1; monotonicity excludes every smaller degree.
These are sufficient-error tests, not measured errors or necessary
quadrature orders.

In(6), maximization over all r>0 gives
r*exp(-r^2*l^2/4)<=sqrt(2/e)/l<1/l. The real width-difference
factor is at most one, including sigma=1. The all-integer majorant
then follows because -l^2+3*l/2 decreases for l>3/4 and
sum_(n>N)n^-2<=1/N. No prime powers are excluded by this replacement.
The Gauss weights are positive and integrate constants exactly by
the cited DLMF statements; affine weights sum to512*log(2).
Multiplying(6) by that sum gives a bound smaller than E_prime(N).
This controls the difference between two finite Gauss sums. It need
not bound a prime tail on the complex ellipse, and makes no such
claim: the analytic Gauss error applies to the full exact integrand
first, then this separate real-node callback error is added.
For m and p(s), the identical pointwise tail estimate holds without
the width-difference factor; their weights sum to the smaller length
log(3/2). Thus the two analytic allocations also cover those scalars.
The unimplemented archimedean and arithmetic allocations are separate.

Taking logarithms in(3) gives exactly
k^2*log(2)>=122+k/2. The positive geometric-integral expansion
in the proof gives strict bounds56/81<log(2)<25/36. At k=14
the lower bound minus the required right side is527/81>0;
at k=13 the corresponding upper difference is-401/36<0.
Every k=2,...,12 is also rejected by exact rational comparison.
No precision-dependent floating-point logarithm was used.

The independent complete certificate audit is reproduced by

    python3 scripts/smoothed-law/paired_ellipse_audit_1784.py

It reads the entire existing1782 certificate, factors every integer
from2 through16384 by full trial division without its generator's
prime sieve, and constructs the full expected(n,p,a) list. It checks
equality of every stored tuple, strict ordering and uniqueness, every
base's primality and p^a=n, and the full exponent histogram. For
a=1,...,14 that histogram is

    1900,31,9,5,3,3,2,2,1,1,1,1,1,1.

The counts sum to1961. Exact verification also checks every lower
degree and every dyadic candidate k=2,...,14, all stored rational
thresholds, the panel/degree/cutoff settings, cost and excess. All20
checks pass with no discrepancies. The full expected list, input hash,
rational comparisons and outcomes are saved in
scripts/smoothed-law/paired_ellipse_audit_1784.json; no preview is used
as enumeration evidence. Both this audit and inspection of the original
sieve/trial-division generator support the count.

The stipulated branch uses all1961 terms at each of8576 exact real
nodes for one nontrivial width. Hence its cost16817536 exceeds10^7
by6817536; even the1900 primes alone give16294400. This verifies
the stated sufficient-certificate stop. It proves no algorithmic lower
bound and does not certify actual quadrature error, width integration,
the remaining scalar allowances,512-bit arithmetic or any observable.
Those distinctions and C033s/t's unaudited hypotheses are essential.

## Mathlib

Full matching coverage for this qualified actual-divisor ellipse bound
and preflight is unchecked/unknown. Standard holomorphic integration,
Gaussian integrals, finite sums and quadrature support portions of it;
no matching theorem or Lean proof is claimed. The local independent
audit1784 above checks this application under its retained inputs.
The exact certificate verifies finite arithmetic and enumeration,
not source correctness, analytic hypotheses or RH.
