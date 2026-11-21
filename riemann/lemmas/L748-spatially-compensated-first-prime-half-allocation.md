# L748: Spatial compensation pays the first-prime half allocation

## Hypotheses

Put a=log2, b=2log3, L=2b=4log3, c=sqrt(2)log2. Let f be
complex-valued in C_c^infinity(0,L), extend it by zero, and put
h(y)=f(y+b). Retain both exact global constraints

    integral_0^L exp(x/2)f(x)dx = integral_0^L exp(-x/2)f(x)dx = 0.

Use the actual coefficient of L743 (1) and the entire resource of
L746 (1), including every exterior pair:

    Q_2(f)=c Re integral_R h(y-a) conjugate(h(y))dy,
    R(h)=(1/4) integral_(R x R)
      |sqrt(|y|)h(y)-sqrt(|z|)h(z)|^2 /
                            (|y-z|sqrt(|yz|)) dy dz.

Define the proposed compensated resource, not a complete-energy identity,
by

    W_b(h)=R(h)+integral_(-b,b) log(b/|y|)|h(y)|^2dy.          (1)

Coordinate singularities in these integrals are interpreted in the
Lebesgue sense; they lie on null sets. No parity condition, cellwise
neutrality, singular limiting test or RH assumption is made.

External imports are:

- Ari Laptev and Tobias Weth, *Spectral properties of the logarithmic
  Laplacian*, [arXiv:2009.03395v2](https://arxiv.org/pdf/2009.03395v2#page=7),
  21 September2020, Theorem4.1/(4.1), printed p.7. For an open set
  Omega in R^d of finite measure it gives
  lambda_1(Omega)>=(1/d)log((2pi)^d/(e|Omega||B_d|)).
  Equations(1.1)-(1.3), pp.1-2, define the zero-extension form
  (2pi)^(-d) integral log|xi| |F_u(xi)|^2dxi, with
  F_u(xi)=integral exp(-ix.xi)u(x)dx, on the closure of
  C_c^infinity(Omega) in their logarithmic Fourier norm. The explicit
  dimension-one applicability of (4.3), the unit-ball instance of
  (4.1), is discussed on printed p.10. The d>=2 restriction belongs
  to the improved (4.4), not the imported bound. Use the standard
  Rayleigh--Ritz variational principle to pass to the form inequality.
- William Beckner, *Pitt's inequality and the fractional Laplacian:
  sharp error estimates*, [arXiv:math/0701939v6](https://arxiv.org/pdf/math/0701939v6#page=5),
  31 July2009, Theorem4/(12), printed p.5, convention p.2. Import its
  complex Schwartz logarithmic-remainder identity, including n=1,
  in exactly L746 (4)'s normalization. No endpoint or sharpness proof
  is repeated here.
- The rational digamma evaluation [NIST DLMF5.4.19](https://dlmf.nist.gov/5.4.E19),
  valid for integers 0<p<q, used only at p=1,q=4; standard
  Plancherel and Cauchy--Schwarz.

These primary statements and normalization were covered before the
attempt by the SPECIALIZE assessment. The source theorem and DLMF
constant were retrieved to check this specialization, without a new
source-discovery turn or reproof of either source theorem.

## Conclusion

With Euler's constant gamma, put

    C_*=log(pi/(4e))-psi(1/4)
       =gamma+pi/2+log(2pi)-1.

Then

    W_b(h)>=C_* ||h||_2^2,     C_*>2>2sqrt(2)log2,           (2)
    Q_2(f)<=c||h||_2^2<=W_b(h)/2,
    W_b(h)/2-Q_2(f)>=(C_*/2-c)||h||_2^2.                   (3)

The coefficient C_*/2-c is strictly positive. Thus the allocation is
strict for nonzero f, and zero gives equality. The source estimates
actually need neither global moment; hence they apply to the entire
stated exact-neutral class without restricting it further.

This is a REPRODUCTION of known-source machinery with the required
interval and arithmetic constants, not a new uncertainty principle
or certified original result. The independent proof audit in step309
below accepts (2)-(3), without changing their hypotheses or constants.
The spatial cost in (1) is added by definition: its
payment in the actual complete Weil energy remains unproved. Other
primes, signed corrections and support propagation remain open.
L746's R-only counterexample and L747's odd-only result are unchanged.
No complete-energy sign or RH candidate follows.

## Proof

### 1. Integrability and the entire identity

Use the unitary transform U h(xi)=(2pi)^(-1/2)F_h(xi), and write
N=||h||_2^2. Since h is smooth and compactly supported, h and U h
are Schwartz. The integrals

    J_y=integral log|y| |h(y)|^2dy,
    q(h)=integral log|xi| |U h(xi)|^2dxi

are absolutely convergent: near zero use boundedness and
integral_0^1 |log r|dr<infinity; at infinity use Schwartz decay.
The added spatial integral is also finite by this argument, and
nonnegative because |y|<b on the support. The imported whole-line
identity L746 (4) is precisely

    R(h)=J_y+q(h)-(psi(1/4)+log2)N.                           (4)

It applies directly to complex Schwartz h, including h not vanishing
at zero, and proves the finiteness of the full nonnegative double
integral. The Fourier constant in (4) already includes the change
from Beckner's exp(+2pi i y eta) convention to U; no second change
or factor of two is introduced. Adding (1)'s spatial term cancels
J_y exactly, with absolute integrability justifying the subtraction:

    W_b(h)=q(h)+(log b-psi(1/4)-log2)N.                       (5)

### 2. Apply the known support-volume bound on the complex core

Take Omega=(-b,b), d=1. It is an open bounded interval with measure
2b, and |B_1|=2. Its smooth core contains the zero extension of h.
The cited form is q exactly, not twice q and not the spectral
logarithm of the ordinary Dirichlet Laplacian. Theorem4.1 and
Rayleigh--Ritz give, first for real core functions,

    q(h)>=log((2pi)/(e(2b)2))N=log(pi/(2eb))N.                (6)

For completeness this form bound complexifies without changing the
constant. Write h=u+iv with u,v real smooth core functions. For real
u,v, F_u(-xi)=conjugate(F_u(xi)) and likewise for v. The cross
term in |F_u+iF_v|^2 is odd in xi. Its product with the even
log|xi| is absolutely integrable, since

    |log|xi|| |F_u(xi) F_v(xi)|
       <=(1/2)|log|xi|| (|F_u(xi)|^2+|F_v(xi)|^2).

The right side is integrable by Section1. The cross integral therefore
vanishes, giving q(h)=q(u)+q(v). Also N=||u||_2^2+||v||_2^2.
Adding the two real inequalities proves (6) for complex h. No
moment condition or parity was used in the source application.

Combining (5) and (6), the interval radius cancels:

    W_b(h)>=[log(pi/(2eb))+log b-psi(1/4)-log2]N
           =[log(pi/(4e))-psi(1/4)]N.                        (7)

### 3. Exact constant comparison and the actual delay

DLMF5.4.19 with p=1,q=4 has cot(pi/4)=1. In its finite cosine
sum, k=1,3 give zero and k=2 gives -(1/2)log4=-log2.
It follows that psi(1/4)=-gamma-pi/2-3log2, proving the stated
formula for C_*.

The strict comparison needs no floating-point calculation. Euler's
constant gamma>=0 follows from the harmonic-integral comparison.
The elementary bounds pi>3 and e<3 imply
e^(3/2)<3sqrt(3)<6<2pi, hence log(2pi)>3/2.
Thus C_*>0+3/2+3/2-1=2. On the other hand sqrt(2)<10/7, and
the positive exponential series gives

    exp(7/10)>sum_(k=0)^4 (7/10)^k/k!
             =482921/240000>2.

Consequently log2<7/10 and c=sqrt(2)log2<1. This proves the
strict threshold C_*>2>2c in (2).

Translation is unitary on the whole-line L2 zero extension, so
complex Cauchy--Schwarz gives

    Re integral h(y-a) conjugate(h(y))dy
       <= |integral h(y-a) conjugate(h(y))dy| <=N.

Multiplying by c>0 and combining with (7) proves (3), including the
displayed margin. There is no removed boundary or exterior term.
Both global exponential constraints are retained in the target;
their absence from this proof means the sufficient estimates hold
on a larger class, not that either constraint has been approximated.

### Independent proof audit, 4 November 2026, step309

The approved audit accepts the stated allocation as a known-source
REPRODUCTION. The following replay uses the pinned source scope in
the saved audit assessment, not a new proof of either imported theorem.

**Class and coefficient.** A compact subset of (0,2b) translates to a
compact subset of (-b,b), so the zero extension of h is smooth and
Schwartz, including at both endpoints. Its moments are exactly

    integral_R exp(y/2)h(y)dy
       =exp(-b/2) integral_0^(2b) exp(x/2)f(x)dx=0,
    integral_R exp(-y/2)h(y)dy
       =exp(b/2) integral_0^(2b) exp(-x/2)f(x)dx=0.

Translation preserves N. In L743 (1),
the n=2 term is (log2/sqrt2)(T_a+T_a^*); its quadratic form is
2log2/sqrt2 times the real delay correlation. Thus the coefficient
is precisely c=sqrt(2)log2, not half that value. Zero extension makes
the interval correlation equal to the whole-line correlation in the
hypotheses; no endpoint contribution is lost.

**Entire identity and normalization.** In Beckner's convention set
B_h(eta)=integral exp(2pi i y eta)h(y)dy. Then
B_h(eta)=F_h(-2pi eta), and absolute convergence gives

    integral log|eta| |B_h(eta)|^2deta
       =q(h)-log(2pi)N.

Theorem4/(12) subtracts D N with D=psi(1/4)-log pi.
Consequently its left side is J_y+q(h)-(psi(1/4)+log2)N.
The source coefficient Gamma(1/2)/(4pi^(1/2)) is 1/4, exactly
R(h)'s coefficient. The imported identity covers complex Schwartz
h; it does not require sqrt(|y|)h(y) to be smooth at zero.
Boundedness near zero and Schwartz decay make both logarithmic
integrals absolutely convergent. The identity therefore also makes
the nonnegative whole-plane remainder finite. Every exterior pair
is present. The added finite integral is log b N-J_y, so cancellation
gives (5) without subtracting divergent terms.

**Support and complex form.** Laptev--Weth Thm4.1 applies to the
zero-extension form of (1/2)log(-Delta), whose symbol is log|xi|.
The interval is open, has measure 2b, and its smooth core contains h;
the d=1 ball has measure 2. Rayleigh--Ritz gives exactly
log((2pi)/(4eb))=log(pi/(2eb)), not a bound for twice q.
For h=u+iv, the Fourier cross term is 2 Im(F_u conjugate(F_v)).
It is odd because u and v are real. Its product with log|xi| is
absolutely integrable by the displayed domination in Section2, so
its integral is zero. This proves q(h)=q(u)+q(v) and validates the
real-to-complex step. Applying the real bound separately needs no
moment hypothesis on u or v. Combining it with (5) gives (7), with
the b terms cancelling exactly.

**Strict comparison.** Directly checked DLMF5.4.19 with integers
p=1,q=4: its -log q term is -2log2 and its half cosine-log sum is
-log2, contributed only by k=2. Thus psi(1/4) is
-gamma-pi/2-3log2 and C_*=gamma+pi/2+log(2pi)-1.
Harmonic-integral comparison gives gamma>=0. The elementary bounds
pi>3 and e<3 imply e^(3/2)<3sqrt3<6<2pi; hence both pi/2 and
log(2pi) exceed 3/2, proving C_*>2. The exact fourth exponential
partial sum is 482921/240000>2, so log2<7/10. Since
2<100/49, sqrt2<10/7 and c<1. Thus C_*/2-c>0 with no numerical
rounding. Finally complex Cauchy--Schwarz and the unitary translation
give Re< h(.-a),h ><=N, yielding precisely (3). For nonzero h,
N>0 makes the margin strict; the zero function gives equality.

No correction to the statement, proof constants or direct inputs
was needed. This accepts only the compensated allocation. It does
not identify W_b with available complete energy, sign the remaining
prime powers or supply support propagation. L746's counterexample
for R alone and L747's odd-sector scope remain unchanged. No
Mathlib matching theorem or RH candidate is claimed.

## Mathlib

Full matching Mathlib coverage of the compensated allocation,
Laptev--Weth bound and Beckner identity was not checked. No absence
claim is made. The canonical evidence is the cited informal theorems
and the specialization above; no Lean proof is asserted.
