# L750: A negative complete-energy corrected localization defect

## Hypotheses

Use the exact smooth Weil form in L744 (6), with zero extensions,
Fourier convention F_h(t)=integral h(x)exp(-itx)dx, and

    m(t)=Re psi(1/4+it/2)-log pi,
    M_sigma(h)=integral exp(sigma*x/2)h(x)dx,
    R_h(u)=integral h(x+u)conj(h(x))dx,
    E(h)=A(h)+2Re(M_+(h)conj(M_-(h)))-B(h),
    A(h)=integral m(t)|F_h(t)|^2dt/(2pi),
    B(h)=2sum_(2<=n<exp(length)) Lambda(n)/sqrt(n) Re R_h(log n). (1)

The length is that of the enclosing interval. A delay equal to its
length has zero overlap. Translations of the interval use the same
full-line form, not a different pole normalization.

Put T=8log3, ell=6log3, delta=T/40, r=ell/12. Take eta and theta
from L749: eta(s)=exp(-1/s) for s>0 and zero otherwise, and
theta(s)=eta(s)/(eta(s)+eta(1-s)). Define exactly the nominated data:

    chi(x)=theta((x-delta)/delta)*theta((T-delta-x)/delta),
    phi_k(x)=chi(x)sin(k*pi*x/T), k=1,...,6,
    alpha(x)=(pi/2)*theta((x-3log3)/(2log3)),
    rho_1=cos alpha, rho_2=sin alpha,
    I_1=(0,ell), I_2=(2log3,T), a_1=0, a_2=2log3,
    beta_(j,k)(x)=eta(1-((x-a_j-k*ell/3)/r)^2), k=1,2,
    H_j(sigma,k)=M_sigma(beta_(j,k)), sigma=+1,-1,
    C_j g=g-sum_k beta_(j,k)(H_j^(-1)(M_+(g),M_-(g))^t)_k.  (2)

The nominated trial space is the exact common kernel of M_+,M_-
on the complex span of phi_1,...,phi_6. No approximate nullspace is
used. For a member f of this space the defect is

    Delta(f)=E(f)-E(C_1(rho_1 f))-E(C_2(rho_2 f)).             (3)

External inputs are Plancherel and its derivative identity, Jensen's
inequality, the composite Simpson error theorem
([DLMF 3.5.7](https://dlmf.nist.gov/3.5.E7) and
[3.5.8](https://dlmf.nist.gov/3.5.E8), real C^4 integrand, even
subinterval count), and the following
already inspected scalar identities: [DLMF 5.9.16](https://dlmf.nist.gov/5.9.E16)
for Re z>0, [DLMF 5.5.2](https://dlmf.nist.gov/5.5.E2), and
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) with the complex
remainder in [5.11(ii)](https://dlmf.nist.gov/5.11#ii). Their
applicability and complete normalization are inherited from L744
and the invocation-start EXPLORE assessment. The numerical work below
is needed to enclose this particular signed defect, which those scalar
identities and the fractional IMS comparison do not sign. No
fractional IMS theorem, logarithmic-symbol approximation, L742
conditional statement, or smaller-window positivity is assumed.

## Conclusion

Let M_k=M_+(phi_k), for k=1,3, and define the exact function

    f=phi_3-(M_3/M_1)phi_1.                                  (4)

All inverses in (2) exist. The function f is nonzero, real, smooth,
compactly supported in (0,T), and has both exponential moments zero.
Each corrected localization is smooth, supported strictly inside its
specified window, and has both moments exactly zero. The full
outward-enclosure certificate gives the deliberately enlarged bounds

    E(f) in [0.0007555, 0.0020930],
    E(C_1(rho_1 f))=E(C_2(rho_2 f))
        in [0.0190768, 0.0204700],
    Delta(f) in [-0.040185,-0.036060] < 0.                    (5)

Thus the literal nonnegative-defect propagation rule fails even on
the approved six-mode neutral space. This does not refute positivity
of E: the same enclosures give positive energies for all three
functions. It is not a disproof of RH, a universal impossibility
result for localization, or a complete RH candidate. Smaller-window
positivity, another paid localization rule, and unrestricted-support
positivity remain unresolved.

The independent conceptual audit in step317 below accepts (5) without
changing the witness or numerical bounds. The step315 construction's
POTENTIALLY_NEW label has only the bounded-search meaning of its saved
assessment; the audit is REPRODUCTION/local verification, not a new
discovery or certification of originality beyond the sources compared.

## Proof

### 1. Smooth supports, right inverses and the exact kernel

L749 proves flatness, smoothness, theta(1-s)=1-theta(s), and
|theta'|<=5. With T substituted for its length, chi is supported in
[delta,T-delta], symmetric about T/2 and equal to one on
[2delta,T-2delta]. The product rho_1 f vanishes for x>=5log3;
rho_2 f vanishes for x<=3log3. Their zero extensions are smooth
and compactly supported strictly within I_1 and I_2. Each beta has
support [a_j+k ell/3-r,a_j+k ell/3+r], also strictly inside I_j.
Flatness at these support endpoints is retained.

Write B_0(t)=eta(1-(t/r)^2) and
b=integral_(-r)^r exp(t/2)B_0(t)dt. Evenness of B_0 gives the same
positive b with exp(-t/2). For c_(j,k)=a_j+k ell/3,

    H_j(sigma,k)=b exp(sigma*c_(j,k)/2),
    det H_j=-2b^2 sinh(ell/6)=-(8/3)b^2 != 0.               (6)

The factor exp(sigma*a_j/2) is included in its row; its determinant
contribution is one. Multiplying H_j by its exact inverse now proves
M_sigma(C_j g)=0 for both signs. This proves exact cancellation,
not just a small residual. In particular every pole product in (3)
is zero after these moment identities have been established.

For odd k, phi_k(T-x)=phi_k(x); for even k it is -phi_k(x).
Consequently M_-(phi_k)=(-1)^(k+1)exp(-T/2)M_k. Since phi_1 is
positive on an open subinterval, M_1>0. For phi_2, pairing x and
T-x on (0,T/2) gives M_2<0: phi_2 is nonnegative there and positive
on an open interval, while exp(x/2)-exp((T-x)/2)<0. The moment map
on the six-mode span therefore has rank two. Its exact kernel has
basis phi_k-(M_k/M_1)phi_1 for k=3,5 and
phi_k-(M_k/M_2)phi_2 for k=4,6. Independence follows from sine
independence on the interval where chi=1. In particular (4) is
nonzero and lies in that exact kernel, including its negative moment.

Reflection x -> T-x interchanges the two rho factors and interchanges
the two correction bumps in opposite order. It preserves simultaneous
vanishing of both moments. Uniqueness of the two-column correction
therefore shows C_2(rho_2 f)(x)=C_1(rho_1 f)(T-x). The complete
energy is reflection invariant for these real tests: m is even,
R_h is unchanged, and the pole product is unchanged. Translation
invariance likewise follows from the Fourier phase and the mutually
inverse moment translation factors. Thus both local energies in (5)
are equal without a numerical symmetry assumption.

### 2. The full signed localization and correction identity

This identity also applies to complex neutral f in the nominated
space. Let g_j=rho_j f, q_j=g_j-C_j g_j, and let Q be the
Hermitian polarization of the full E in (1), linear in its first
argument. Put

    k(u)=2exp(-u/2)/(1-exp(-2u)), u>0,
    K_f(u)=Re integral f(x+u)conj(f(x))
                    [1-sum_j rho_j(x+u)rho_j(x)]dx.

The exact identity is

    Delta(f)=-integral_0^infinity k(u)K_f(u)du
             -2sum_(2<=n<6561) Lambda(n)/sqrt(n) K_f(log n)
             -2Re sum_j M_+(g_j)conj(M_-(g_j))
             +sum_j [2Re Q(g_j,q_j)-E(q_j)].                (7)

To justify the continuous part, DLMF 5.9.16 at
z=1/4+it/2 and at 1/4 gives

    m(t)=m(0)+integral_0^infinity k(u)(1-cos(tu))du,
    A(h)=m(0)||h||^2
                  +integral_0^infinity k(u)(||h||^2-Re R_h(u))du. (8)

Tonelli applies to the nonnegative multiplier difference and
Plancherel gives ||h||^2-Re R_h(u)=||h(.+u)-h||^2/2.
Near zero this is bounded by u^2||h'||^2/2, while k(u)=O(1/u).
At infinity k decays exponentially. Thus the integral is finite;
subtracting the finitely many smooth identities is justified. Since
sum rho_j^2=1, their norm terms cancel, leaving -integral k K_f.
The arithmetic difference is the second term of (7); the pole
difference is its third term. Finally expand
E(g_j-q_j)=E(g_j)-2Re Q(g_j,q_j)+E(q_j).
This proves (7) with all signs. In particular correction energies and
the uncorrected pole products are not discarded. For small u the
factor 1-sum rho_j(x+u)rho_j(x) is half the squared distance of two
unit vectors and is O(u^2), giving direct domination of (7) too.

The certificate evaluates the algebraically identical expression
E(f)-2E(C_1(rho_1 f)) directly. It keeps the full digamma symbol
and every relevant arithmetic delay; no absolute estimate is used
to replace the signed central values in (7).

### 3. Exact coefficient enclosures and derivative controls

The reproducible certificate is
`scripts/corrected-ims/certificate-315.cpp` and its complete output
`scripts/corrected-ims/certificate-315.json`. All elementary operations
use binary64 outward intervals with nextafter; compilation disables
floating contraction and does not enable fast-math. Integer constants
are exact. Logarithms use the atanh series after binary range reduction;
exponentials use a degree-18 Taylor polynomial on [-1/8,1/8] followed
by squaring. For arguments below -100 the enclosure [0,4e-44] is
used. Pi uses Machin's identity and the alternating arctangent series.
Sine and cosine are reduced to [-4,4] and use degrees 65 and 64.
Square-root endpoints are checked by outward squaring; the library
square root is just the starting guess. These are interval evaluations
of real elementary functions, not ordinary unvalidated library values.

For clarity, the elementary remainder allowances are 2^(-100) for
the exponential base polynomial, 2^(-180) for the logarithm series,
2^(-300) for arctangent, and 2^(-160),2^(-150) for sine and cosine.
They exceed, respectively,

    2*(1/8)^19/19!,
    2*(1/3)^121/[121*(1-1/9)],
    (1/4)^181/181,
    4^67/67!, 4^66/66!.                                   (9)

The independent constant check and its complete evidence are
`scripts/corrected-ims/constants-315.cpp` and `constants-315.json`
in the same directory. All fourteen checks pass. Its first pass
failed only because an outward enclosure straddled the exact integer
352; that equality was then checked with exact integer arithmetic.
The retained `constants-315-first-pass.json` records that failure.

For derivative bounds on 0<=s<=1, direct differentiation of eta
and sup_(u>0) u^j exp(-u)=j^j exp(-j) give bounds

    |eta^(j)| <= 1,1,8,280,20000, j=0,...,4.                (10)

For example its third bound is the sum
6^6 e^(-6)+6*5^5 e^(-5)+6*4^4 e^(-4)<280; its fourth uses
8^8 e^(-8)+12*7^7 e^(-7)+36*6^6 e^(-6)+24*5^5 e^(-5)<20000.
These inequalities are included in the constant certificate. At
least one of s,1-s is >=1/2, so eta(s)+eta(1-s)>=e^(-2)>1/8.
Differentiate (eta(s)+eta(1-s))*theta(s)=eta(s), and use L749's
|theta'|<=5. The recursion gives valid bounds

    |theta^(j)| <= 1,5,352,26000,3000000, j=0,...,4.         (11)

For j=2 the bound is 8*(8+2*2*5+16)=352; for j=3 and j=4 the
same recursion gives 25536 and 2503936, below the displayed bounds.
Flatness extends them to the entire real line. On either transition
of chi its other factor is identically one. Consequently its j-th
derivative is bounded by (11)/delta^j, with no omitted overlap term.
Leibniz and chain rules give the displayed program's fourth derivative
bounds for phi_k, rho_1 phi_k, and exp(+-x/2) times these functions.
For beta use |z'|<=2/r, |z''|=2/r^2 for z=1-((x-c)/r)^2,
and (10); the fourth bound is
20000*(2/r)^4+1680*(2/r)^2*(2/r^2)+24*(2/r^2)^2.

Composite Simpson with n=262144 subintervals on [0,T] encloses M_1,
M_3 and d_+=M_+(rho_1 f), d_-=M_-(rho_1 f). Its error is
at most (b-a)*s^4*sup|F''''|/180 for panel spacing s; interval
nodes and arithmetic include the uncertainty in T and M_3/M_1.
For b in (6), use 65536 subintervals on [-r,r]. Both counts are even;
the program field `moment_panels` denotes subintervals, not pairs.
For positive moments
exp(x/2)<=81, for negative ones exp(-x/2)<=1; on the bump
exp(t/2)<2. The exact first correction matrix is

    H_1=b [[3,9],[1/3,1/9]],
    c_1=(9d_- - d_+/9)/((8/3)b),
    c_2=(d_+/3 - 3d_-)/((8/3)b),
    v=C_1(rho_1 f)=rho_1 f-c_1 beta_(1,1)-c_2 beta_(1,2).  (12)

Enlargements of the resulting intervals are

    76.14557024 < M_1 < 76.14557027,
    58.52241869 < M_3 < 58.52241872,
    .7685597270 < M_3/M_1 < .7685597274,
    .24534605110 < b < .24534605112,
    -15.46733825 < d_+ < -15.46733821,
    .1256992405 < d_- < .1256992412,
    4.355918335 < c_1 < 4.355918350,
    -8.456744741 < c_2 < -8.456744721.                       (13)

These enclose coefficients defined by exact integrals; replacing them
by their interval midpoints is never part of the proof.

### 4. Validated full-energy evaluation

Here are the analytic obligations behind the numerical certificate.
Let h be f or v, set P=64, N=524288 and s=P/N=1/8192, and let q
be the piecewise linear interpolant of the exact values h(js) on the
periodic grid. It vanishes near both period endpoints and its support
has diameter <9. In the local case it also remains strictly inside
I_1. Let a_j=h(js) and S_k=sum_j a_j exp(-2pi i jk/N). The
program encloses this finite sum by the radix-two FFT, whose butterfly
identity follows by separating even and odd indices; every butterfly
is evaluated with outward complex intervals. Thus the FFT is not a
floating-point sign heuristic.

For xi_k=2pi k/P, integrating the linear hat exactly gives

    F_q(xi_k)=s*sinc(pi k/N)^2*S_(k mod N),
    A_per(q)=P^(-1)sum_(k in Z) m(xi_k)|F_q(xi_k)|^2.       (14)

The head includes k=0 and both signs of 1<=k<=N/2, including both
Nyquist frequencies. The multiplier is enclosed by the recurrence
psi(z)=psi(z+J)-sum_(j=0)^(J-1)1/(z+j), with J=256 for xi<512
and J=0 otherwise. At w=z+J the cited remainder gives

    |psi(w)-log w+1/(2w)|
       <=sqrt(2)/(6|w|^2)<1/(4|w|^2), Re w>0.             (15)

This is the complete digamma multiplier, including low frequencies.
No asymptotic replacement is used without its remainder.

Write A_0=2+8sqrt(2)/3+log(4pi) and W(t)=A_0+log(2+|t|).
L744 (8) gives |m(t)|<=W(t). The function W(t)/t^2 decreases for
t>0, since t/(2+t)-2W(t)<0. With R_0=pi/s, periodic Parseval
therefore bounds the entire omitted head complement by

    tail <= W(R_0)||q'||^2/R_0^2.                          (16)

To compare (14) to the full-line A(q), use (8) on the periodic
circle. Its correlation is sum_(j in Z) R_q(u+jP). For u>0 only
images centered at jP, j>=1, contribute beyond the real-line
correlation. Since their supports have radius at most 9,
k(u)<=3exp(-u/2) there. Also integral |R_q(u)|du<=||q||_1^2
<=9||q||^2. Hence the full image error is at most

    images <=27||q||^2 exp(-55/2)/(1-exp(-32)).             (17)

No arithmetic Fourier tail is estimated. Instead compute the exact
nodal autocorrelation C_j=sum_i a_i a_(i+j), with cyclic indices,
by inverse FFT of |S_k|^2. The linear hat convolution is

    R_q(u)=s sum_j C_j B_3(u/s-j),
    B_3(z)=2/3-z^2+|z|^3/2, |z|<=1;
           (2-|z|)^3/6, 1<=|z|<=2; 0 otherwise.            (18)

Only the four adjacent terms (or harmless endpoint zeros) contribute.
For the required delays u<9, P>18 excludes periodic image overlap.
Thus (18) is the full-line correlation. The program generates every
prime power n<6561 (892 terms) for f and every n<729 for v, with
coefficient log(p)/sqrt(n) for n=p^a. A boundary delay has no overlap
and is excluded. There is no neglected infinite prime tail: these
finite cutoffs follow from the specified supports.

It remains to justify replacing the original smooth h by q. On each
cell, q' is the mean of h'; the fundamental theorem of calculus and
Cauchy--Schwarz, followed by h-q vanishing at the endpoints, give

    ||h-q||^2 <=s^4 B_2, ||h'-q'||^2<=s^2 B_2,
    B_2>=||h''||^2.                                       (19)

For B_2 the program evaluates second-derivative interval jets on
16384 entire panels covering [0,9], sums panel length times the
squared-derivative range, and uses its upper endpoint. These are
interval ranges over panels, not point samples with an unbounded
integration error. Near a flat endpoint, terms exp(-1/t)t^(-j)
are bounded by their maximum at 1/t=max(j,1/a), for 0<t<=a;
if 1/a>100, the larger endpoint value at 100 is used. This avoids
division by zero while retaining derivative bounds through flatness.

Set epsilon=s^4 B_2, C=A_0+log3 and e=h-q. The elementary inequality
2+|t|<=3sqrt(1+t^2) and Jensen give

    ||q||_W^2<=Q_W:=||q||^2[C+.5log(1+||q'||^2/||q||^2)],
    ||e||_W^2<=E_W:=epsilon[C+.5log(1+s^(-2))].             (20)

Here ||.||_W uses the full-line multiplier W. The expression
x log(1+y/x) increases in both nonnegative variables, so (19)
justifies the second inequality even if the actual L2 error is much
smaller or zero. The interpolant norms are integrated exactly on
each linear segment: s(a_j^2+a_j a_(j+1)+a_(j+1)^2)/3 and
(a_(j+1)-a_j)^2/s. Cauchy--Schwarz and the full finite-delay
operator bound C_prime=2sum Lambda(n)/sqrt(n) now give

    |[A(h)-B(h)]-[A(q)-B(q)]|
      <=2sqrt(Q_W E_W)+E_W
            +C_prime[2sqrt(||q||^2 epsilon)+epsilon].     (21)

Only h, whose moments vanish exactly, is assigned the energy E(h).
The interpolant q need not be neutral: (21) uses A(q)-B(q) as an
auxiliary quantity and makes no claim that its pole product vanishes.
This distinction is essential.

The entire error in (16), (17), and (21), together with all interval
rounding, is included in the final enclosures. Some outward rounded
upper budgets from the complete certificate are:

| Quantity | f | v |
| --- | ---: | ---: |
| ||q||^2 | 6.972271 | 4.941264 |
| ||q'||^2 | 6.339646 | 61.208387 |
| B_2 | 571.473 | 6832.225 |
| C_prime | 318.4530 | 102.4963 |
| Fourier tail | 0.000000177 | 0.000001706 |
| Periodic images | 0.000000000215 | 0.000000000153 |
| Interpolation energy error | 0.000624246 | 0.000638104 |

The signed central values are not these budgets: the head A(q) is
enclosed near -18.7932 and -5.38705, while the entire arithmetic
form B(q) is near -18.7946 and -5.40682. Subtracting their certified
intervals and adding all the above errors yields (5). The exact final
binary64 enclosure, printed with round-trip endpoint encoding, is

    [-0.04018430362622672, -0.03606073089581196].            (22)

The simpler rational bounds in (5) enlarge it outwards.

### 5. Reproduction, corrections and scope

From the active notebook, run:

```sh
clang++ -O2 -std=c++17 -ffp-contract=off scripts/corrected-ims/certificate-315.cpp -o /private/tmp/riemann-ims-315
/private/tmp/riemann-ims-315 > scripts/corrected-ims/certificate-315.json
clang++ -O2 -std=c++17 -ffp-contract=off scripts/corrected-ims/constants-315.cpp -o /private/tmp/riemann-ims-constants-315
/private/tmp/riemann-ims-constants-315 > scripts/corrected-ims/constants-315.json
python3 ../scripts/loop/inspect_json.py scripts/corrected-ims/certificate-315.json --pointer /Delta --full
```

The first full pass used the insufficient convenient bound 270 in
place of 280 for the third derivative of eta. It is retained as
`scripts/corrected-ims/certificate-315-first-pass.json`, explicitly
marked invalid. The coefficient 6*270 in the bump fourth-derivative
chain rule was corrected to 6*280=1680; the complete certificate was
then rerun. Only that corrected run and the passing constant checks
support (5). The separate `screen-315.py`/`.json` is a nonrigorous
four-dimensional diagnostic, not a dependency of the certificate.

The mathematical test stayed at its nominated lengths, partition,
bumps and six modes. One negative exact-neutral vector suffices;
there is no need to infer a sign from approximate eigenvalues or to
claim the entire restricted form was certified nonnegative. L749's
direct-payment stop and L743's different prime-only obstruction are
contrasts, not premises for this negative full-defect conclusion.
The separate conceptual audit below checks the interval implementation,
all analytic tails and exact neutrality on this unchanged witness.

### 6. Independent conceptual audit, 4 November 2026, step317

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-04-corrected-ims-negative-defect-audit.md`
covers exactly this audit. It reuses the inspected primary DLMF inputs,
L744 (6),(8) and L749's audited cutoff; no further source claim,
L742 hypothesis or source positivity computation is imported. The
following checks accept (5), (7) and the literal-rule stop. They do
not establish positivity on an unrestricted class.

**Exact functions and signed identity.** The columns of H_j are
b(exp(c_k/2),exp(-c_k/2))^t; their determinant is
b^2(exp(-ell/6)-exp(ell/6))=-8b^2/3. Translation multiplies rows
by exp(+-a_j/2) with product one. Solving H_1 c=(d_+,d_-)^t gives
exactly (12), without conjugation. Reflection changes
M_sigma(h) to exp(sigma*T/2)M_(-sigma)(h), so preserves neutrality
and exchanges the two bump columns. Uniqueness gives the reflected
corrected function, hence equality of its complete energy. Odd-mode
symmetry and M_1>0 justify both exact moments of (4); sine independence
on the plateau excludes the zero function. These conclusions use
exact integrals, not their interval midpoints. The pole products vanish
only for the resulting smooth h. In (7), subtracting (8) cancels the
norms and leaves -integral k K_f; the arithmetic and uncorrected-pole
signs then follow from (1). The Hermitian quadratic expansion supplies
the remaining correction terms. Tonelli for the nonnegative scalar
multiplier difference, followed by the H1 translation bound, justifies
the interchange before subtraction, including for complex tests.

**Quadrature and derivative constants.** Both counts in Section 3
are even subinterval counts in DLMF 3.5.7-8. The smooth integrands
meet its real C^4 hypothesis on the exact intervals. Each exact
endpoint, node, coefficient and mesh spacing lies in the program's
evaluation interval; endpoint uncertainty is not an extra uncharged
quadrature error. The exponential bounds 81, 1 and 2 apply on the
exact integration domains. Leibniz coefficients in `mulBounds` and
the chain-rule coefficients in `rhoBounds` and `bb` reproduce the
stated fourth-derivative bounds. In particular the beta term is
6*280*(2/r)^2*(2/r^2), not the invalid first pass's 6*270 term.
The theta recursion gives 352, 25536 and 2503936 as stated.
The replay of all fourteen constant checks is identical to the saved
passing output; the eta third-derivative majorant is greater than 270
and less than 280. Both failed first passes remain excluded.

**Outward arithmetic and actual domains.** The basic +,-,*,/ interval
operations enclose each binary64 rounding by nextafter, with division
only away from zero. Squaring retains zero when its interval crosses
zero. Square-root endpoints are verified by outward squaring, so
correctness does not depend on a library estimate alone. Binary
scalings in the elementary range reductions are exact; their finite
series and explicit remainder allowances were checked in (9).
The monotonic exponential/logarithm endpoint evaluations are valid.
For eta jets crossing zero, u^k exp(-u) increases up to u=k and
decreases thereafter. Choosing k when necessary, or replacing a lower
u>100 by 100 for k<=4, therefore gives an upper bound, including
the flat side. The differentiated product, inverse and composition
rules in the ordinary second-derivative jets are correct.

`scripts/corrected-ims/audit-317.py` instruments a preserved copy of
the original program as `instrumented-317.cpp`. It rejects nonfinite
or unordered intervals, wrong binary64/round-to-nearest settings,
flushed subnormals, out-of-domain elementary evaluations, invalid
Simpson counts and delay intervals crossing a grid-cell boundary.
This is an audit of the same interval implementation, not a second
independent numerical library. Its full-domain certificate is
`implementation-domains-317.json` in that directory. Maximum reduced
trigonometric modulus is 3.1417303168314623<4; maximum arctangent
modulus is 0.20000000000000007<1/4; exponential base modulus is at
most 1/8; logarithm base lies in [1,2]. Every interval remains finite
and ordered. These checks validate the domains of the proved series
bounds, rather than estimating accuracy from sampled comparisons.

**Continuous Fourier sum and images.** For a real linear interpolant,
integrating each hat gives (14) at every integer frequency, including
aliases. Real symmetry makes the negative head equal to the positive
head. The two Nyquist frequencies are distinct terms of the continuous
Fourier series, although their DFT coefficients coincide; doubling
that term is correct. The radix-two butterflies enclose the finite
DFT, and inverse transforming its squared moduli gives the cyclic
nodal correlations with normalization 1/N. All |k|>N/2 are paid
by periodic derivative Parseval and decreasing W(t)/t^2. This is an
entire alias-tail bound, not a finite-frequency truncation heuristic.
The digamma shift retains Re(w)>0; the complex remainder is at most
sqrt(2)/(6|w|^2)<1/(4|w|^2) for both shift choices.

Formula (8) also holds for q in H1: apply its nonnegative multiplier
difference to the Fourier integral, or to the periodic Fourier series,
and use the derivative norm to dominate u near zero. Periodization
replaces R_q(u) by sum_j R_q(u+jP); its norm term is unchanged.
The true interpolants have support diameter <9 and vanish near period
endpoints. For u>0 all extra images have u>=jP-9, j>=1, where
k(u)<=3 exp(-u/2). The L1 correlation bound and summing this geometric
series give exactly (17), with no missing negative-u factor.

**Arithmetic and replacement error.** Hat convolution gives (18).
For each used delay, the entire interval u/s stays inside one cell:
its width is at most 1.7462298274040224e-9 and its distance from the
nearest cell boundary is at least 4.334694676799699e-5. Therefore
the five retained integer indices contain every nonzero cubic-hat
term. Since u<9 and P>18, no cyclic image contributes to these
full-line correlations. Independent integer factorization in the
audit driver agrees with the full prime-power list without duplicates:
892 terms below 6561 and 151 below 729, for 1043 evaluated delays.
The generated coefficient for each n=p^a is log(p)/sqrt(n); the
external factor two matches (1). The excluded boundary delays have
zero overlap for both h and q; no infinite arithmetic remainder exists.

The second-derivative jets enclose whole panels covering [0,9], outside
which both smooth functions vanish. Summing panel length times the
squared range gives B_2's upper bound. On each cell q' is the mean
of h'; integrating the elementary mean-deviation bound, then using
the vanishing endpoint values of h-q, proves both inequalities (19)
with the displayed safe constants one. Jensen is applied with the
full-line Fourier probability measure. The function
x[C+.5log(1+y/x)] is increasing in x,y>=0, with its limiting value
at x=0, so substituting the separate L2/derivative bounds proves (20).
The archimedean Cauchy--Schwarz bound and the full finite-delay
operator norm prove (21). This compares A-B for the auxiliary q;
no assertion of neutral moments for q or removal of its pole term
is needed. Its support stays inside the corresponding original
window, so the same arithmetic operator is used in this comparison.

**Replays and conclusion.** On Apple clang 21.0.0, arm64, compiled
with -O2 -std=c++17 -ffp-contract=off, both the unmodified replay
`certificate-replay-317.json` and instrumented replay
`certificate-instrumented-317.json` are identical to the complete
step315 JSON, not merely to its displayed preview. The constants
replay is `constants-replay-317.json`; the full comparison and all
failure flags are `audit-summary-317.json`. All are under
`scripts/corrected-ims/`. Reproduce the unchanged-program and constant
builds from Section 5 with output redirected to those replay paths,
then run `python3 scripts/corrected-ims/audit-317.py`. The driver writes
complete evidence and prints bounds, requirements, failures and paths.
No mathematical script input or prior certificate was overwritten.

The complete final enclosure (22), and hence its outward rational
enlargement (5), survives the audit. The three individual energies
remain strictly positive. This completes local verification of the
existing counterexample to the literal rule; it adds no new sign
mechanism, RH candidate, global localization ban or originality claim.

## Mathlib

Full matching Mathlib coverage for this fixed corrected full-Weil
defect certificate was not checked. No absence claim is made.
The underlying matrix inversion, integration, Fourier/Parseval,
elementary-function and finite-sum facts do not by themselves sign
this defect. This is an informal proof with a reproducible interval
certificate, independently audited above but not a Lean-checked result.
