# L747: Odd-centered tests satisfy the first-prime half-remainder allocation

## Hypotheses

Put a=log2, b=2log3, L=2b=4log3 and c=sqrt(2)log2.
Let f belong to the complex space C_c^infinity(0,L), extend it by zero,
and set h(y)=f(y+b). Assume

    h(-y)=-h(y),
    integral_0^L exp(x/2)f(x)dx = integral_0^L exp(-x/2)f(x)dx = 0.

Use the actual first-prime coefficient fixed in L743 (1), and precisely
the entire resource of L746 (1):

    Q_2(f)=c Re integral_R h(y-a) conjugate(h(y))dy,
    R_B(f)=R(h)=(1/4) integral_(R x R)
       |sqrt(|y|)h(y)-sqrt(|z|)h(z)|^2 /
                           (|y-z|sqrt(|yz|)) dy dz.             (1)

Interpret the resource as a nonnegative Lebesgue integral; singular
coordinate sets are null. All exterior pairs are retained.

External imports, with their necessary scope, are:

- D. V. Gorbachev, V. I. Ivanov and S. Yu. Tikhonov, *Sharp Pitt
  inequality and logarithmic uncertainty principle for Dunkl transform
  in L2*, [arXiv:1505.02958v1](https://arxiv.org/pdf/1505.02958v1#page=6),
  Corollary 3.2, printed p.6, with c(beta,lambda) from Theorem 2.1,
  printed p.3. Transform/measure conventions are on pp.1-2, sector
  definitions/reduction on pp.4-6, especially (3.7)-(3.8). Its complex
  Schwartz scope and d=1, k=0, harmonic degree n=1 case were inspected
  in the prior assessment. The arXiv identifier is pinned to v1;
  the PDF's internal date is 19 May2018, as recorded in that assessment.
- William Beckner, *Pitt's inequality and the fractional Laplacian:
  sharp error estimates*, [arXiv:math/0701939v6](https://arxiv.org/pdf/math/0701939v6#page=5),
  31 July2009, Theorem 4, equation (12), printed p.5; convention p.2.
  Import its entire logarithmic-remainder identity on complex Schwartz
  functions, including dimension one, as also normalized in L746 (4).
- Digamma reflection, [NIST DLMF 5.5.4](https://dlmf.nist.gov/5.5.E4):
  psi(z)-psi(1-z)=-pi cot(pi z), for z not an integer. Here psi is
  Gamma'/Gamma. Use also the standard Plancherel theorem and dominated
  convergence theorem, with hypotheses verified below.

These are imports of the named theorems, not reproofs of sharp Pitt,
Beckner's identity or their source endpoint arguments. No RH, spectral
endpoint or positivity assumption is made. L744, L742 and L745 are
not premises.

## Conclusion

In fact every complex odd Schwartz function h satisfies

    R(h)>=pi ||h||_2^2.                                      (2)

Consequently every f in the stated class satisfies

    Q_2(f)<=sqrt(2)log2 ||h||_2^2
           <= (sqrt(2)log2/pi) R_B(f) < R_B(f)/2               (3)

when f is nonzero; for f=0 both sides are zero. In particular the
approved non-strict half-allocation holds on the entire stated class.
The positive margin obeys

    R_B(f)/2-Q_2(f)
       >= (pi/2-sqrt(2)log2)||h||_2^2.                        (4)

This is a REPRODUCTION/specialization of known uncertainty machinery,
not a claimed new uncertainty principle or certified original result.
The exact moments are respected but unnecessary for (2)-(4). This pays
only this parity sector's first-prime term. It does not control the
even sector, remaining primes, energy corrections, support propagation
or the full Weil form, and gives no RH candidate. L746's even-sector
counterexample is unchanged. The separate audit in step305 below accepts
(2)-(4) on precisely the stated complex smooth class.

## Proof

### 1. Specialize the known sector theorem

Use the unitary Fourier transform

    U h(xi)=(2pi)^(-1/2) integral_R h(y)exp(-i y xi)dy,
    N=||h||_2^2=||U h||_2^2.

In the sector theorem choose d=1, multiplicity k=0 and harmonic
degree n=1. Then lambda_k=d/2-1+|k|=-1/2, so lambda_k+n=1/2.
The degree-one spherical harmonic in one dimension is the sign
function on the two-point sphere. Its radial multiples are exactly
odd functions. In particular an odd Schwartz h belongs to this sector;
if expressed as y times a radial function, h(y)/y extends smoothly
and evenly across zero by the odd Taylor expansion, and is Schwartz.
Complex radial coefficients are allowed by the source theorem.

At k=0 the transform is U. The source measure on both sides is
(2pi)^(-1/2) times Lebesgue measure in dimension one, so its common
constant cancels upon squaring the source norm inequality. Corollary
3.2 and Theorem 2.1 therefore give, for 0<=beta<3/2,

    integral |xi|^(-2beta)|U h(xi)|^2 dxi
       <= C(beta)^2 integral |y|^(2beta)|h(y)|^2dy,
    C(beta)=2^(-beta) Gamma(3/4-beta/2)/Gamma(3/4+beta/2).       (5)

Only 0<=beta<=1/4 will be used. We import (5), including its constant
and complex scope; no sharpness proof is needed for this application.

### 2. Justified one-sided logarithmic differentiation

Write J_y=integral log|y| |h(y)|^2dy and
J_xi=integral log|xi| |U h(xi)|^2dxi. Both are absolutely convergent:
h and U h are bounded near zero and Schwartz at infinity. For
0<=beta<=1/4, the absolute beta-derivative of the spatial weight is
bounded by

    2 |log|y|| max(1,|y|^(1/2)).

After multiplication by |h(y)|^2 this is integrable, both at zero
and at infinity. The Fourier weight's derivative is bounded in absolute
value by

    2 |log|xi|| max(1,|xi|^(-1/2)).

Multiplied by |U h(xi)|^2 this is integrable: near zero use boundedness
and the finite integral of r^(-1/2)|log r| on (0,1); at infinity use
Schwartz decay. The mean value theorem gives these same majorants
for the weight difference quotients. Dominated convergence therefore
justifies the right derivatives at beta=0 of both integrals in (5).

The nonnegative difference between the right and left sides of (5)
vanishes at zero by Plancherel. Its right derivative is nonnegative.
Since C(0)=1 and

    (log C)'(0)=-log2-psi(3/4),

this derivative condition is

    2(-log2-psi(3/4))N+2J_y+2J_xi>=0.

Thus the direct specialization of the known family yields

    J_y+J_xi >= (log2+psi(3/4))N.                            (6)

The argument uses only the smooth class and an ordinary one-sided
parameter derivative. It assumes no singular extremizer, limit-domain
extension, or interchange involving the resource's double integral.

### 3. Match Beckner's entire identity

For clarity, retain Beckner's Fourier convention explicitly:

    B h(eta)=integral h(y)exp(+2pi i y eta)dy.

His Theorem 4, equation (12), with n=1 and
g(y)=sqrt(|y|)h(y), is

    R(h)=J_y+integral log|eta| |B h(eta)|^2deta
                    -(psi(1/4)-log pi)N.                     (7)

The coefficient on the right-hand resource is precisely
Gamma(1/2)/(4pi^(1/2))=1/4, as in (1); (7) is an imported identity,
not a newly proved endpoint formula. Since h is Schwartz it applies
without any assumption that g is smooth at the origin. It includes
every pair in R x R, and also proves finiteness of (1).

Substituting xi=-2pi eta gives

    B h(eta)=sqrt(2pi) U h(-2pi eta),
    integral log|eta| |B h(eta)|^2deta=J_xi-log(2pi)N.

These substitutions are justified by absolute integrability of the
logarithmic integrals. Hence (7) becomes, as in L746 (4),

    R(h)=J_y+J_xi-(psi(1/4)+log2)N.                          (8)

Subtracting (8)'s scalar from (6), and applying digamma reflection at
z=1/4, gives

    R(h)>=(psi(3/4)-psi(1/4))N=pi N.

This proves (2) on the entire odd complex Schwartz class, and therefore
on the target subclass without weakening either global moment.

### 4. Pay the actual delay

Translation on the whole real line is unitary on L2. Cauchy--Schwarz,
valid for complex h, gives

    Re integral h(y-a) conjugate(h(y))dy
       <= |integral h(y-a) conjugate(h(y))dy| <=N.

The target uses the whole-line zero extension, so no boundary term or
support correction is omitted. Multiplying by the positive coefficient
c from (1) gives Q_2<=cN. Combining with (2) proves (3)-(4).
Finally log2<1, sqrt(2)<3/2 and the elementary bound pi>3 imply
sqrt(2)log2<3/2<pi/2. For nonzero h, N>0 and R(h)>=pi N>0,
so the final comparison with R_B/2 in (3) is strict. Zero is handled
directly. This completes the approved comparison.

### Independent audit — step305, 4 November 2026

The audit accepts (2)-(4), without a mathematical correction, under
the pre-existing SPECIALIZE scope in
`drafts/literature/2026-11-04-odd-first-prime-allocation-audit.md`.
It reuses the inspected primary statements and scope evidence recorded
there and in the step302 assessment; it does not audit their sharpness
proofs anew. The following checks constitute the independent replay.

1. **Source class and measure.** In the cited Corollary3.2 take
   d=1, k=0, n=1. This is an allowed nonzero harmonic sector even in
   dimension one: its angular function is sign(y). Every odd Schwartz
   h is in it. Explicitly h(y)/y extends at zero as
   integral_0^1 h'(ty)dt; it is smooth and even, and division by y
   preserves Schwartz decay away from zero. This works componentwise
   for complex h, within the source's complex class. Here lambda_k=-1/2,
   lambda_k+n=1/2, and the admissible range is 0<=beta<3/2.
   The source transform at k=0 is U, and both squared norms have the
   same factor (2pi)^(-1/2) in their measure. Cancelling it gives (5)
   with C(beta)^2, not C(beta). Only beta<=1/4 is needed.

2. **One-sided derivative.** Let A(beta) and B(beta) denote the
   Fourier and spatial integrals in (5). The source gives
   F(beta)=C(beta)^2 B(beta)-A(beta)>=0 and F(0)=0.
   The displayed derivative majorants in Section2 dominate the
   difference quotients on [0,1/4]: at the Fourier origin the worst
   factor is r^(-1/2)|log r|, and at the spatial origin it is
   |log r|. Both are integrable; the Schwartz factors control
   infinity. Thus A'(0+)=-2J_xi and B'(0+)=2J_y.
   Since (C^2)'(0)=-2(log2+psi(3/4)), F'(0+)>=0 is exactly (6).
   No two-sided parameter assertion or singular limiting test is used.

3. **Entire identity and normalization.** The imported Beckner
   Theorem4/(12) is for Schwartz h, including complex h in dimension
   one; it does not require sqrt(|y|)h(y) to be Schwartz.
   Gamma(1/2)/(4sqrt(pi))=1/4 matches (1), on R x R with exterior
   pairs. Absolute integrability of the two logarithmic integrals
   follows from boundedness at zero and Schwartz decay. In particular
   B h(eta)=sqrt(2pi)U h(-2pi eta) and |dxi|=2pi |d eta|
   in the change of variables give Fourier logarithm J_xi-log(2pi)N.
   Subtracting Beckner's scalar psi(1/4)-log pi leaves
   psi(1/4)+log2 in (8). The imported identity also establishes
   finiteness of the literal nonnegative resource; no truncated
   resource or unproved double-integral differentiation is substituted.

4. **Subtraction and delay.** DLMF5.5.4 at z=1/4 says
   psi(1/4)-psi(3/4)=-pi. Thus (6) and (8) give R>=pi N
   with the stated sign. The p=2 term of L743 (1) has Hermitian
   coefficient 2Lambda(2)/sqrt(2)=sqrt(2)log2=c.
   Centering changes no Lebesgue measure or whole-line correlation.
   Whole-line translation is unitary, so the complex inner product
   has real part at most N. Hence Q_2<=cN<=c R/pi and
   R/2-Q_2>=(pi/2-c)N. The elementary bounds in Section4 give
   c<pi/2; strictness in (3) uses N>0, while zero has equality.

5. **Target constraints and limitations.** The zero extension of
   f in C_c^infinity(0,L), shifted by b, is Schwartz and supported
   in (-b,b). Substitution gives the exact original moments as
   exp(+-b/2) integral exp(+-y/2)h(y)dy; neither is replaced or
   approximated. The argument proves the stronger odd Schwartz
   assertion without using these constraints and hence applies to
   their full stated intersection. No implication for the even
   sector follows: L746's even witness is retained. No source sign
   for other primes, complete-energy corrections or support growth
   has been supplied. L742/L744/L745 are not mathematical inputs.

The direct local inputs remain L743 and L746, and the DAG row needs
no change. This is certification of a REPRODUCTION of known machinery,
not an original uncertainty theorem, a full-energy sign or an RH
candidate. Full matching Mathlib coverage remains unchecked as below.

## Mathlib

Full matching coverage for the sharp odd-sector Pitt inequality,
Beckner's weighted logarithmic-remainder identity and this allocation
has not been checked. The proof relies on the precise external
citations above, not a claimed Mathlib theorem. Supporting Plancherel,
dominated convergence and Cauchy--Schwarz are standard inputs; their
Mathlib theorem names were not checked in this step. No absence claim
or formal verification claim is made.
