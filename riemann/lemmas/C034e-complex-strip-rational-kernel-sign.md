# Corollary C034e: negative real part of the rational kernel on a product strip

## Hypotheses

Let z,w be independent complex numbers satisfying

    Re z>=13, Re w>=13, |Im z|<=1/2, |Im w|<=1/2.

Use exactly the rational functions and symmetric kernel of C034d(29):

    Q_j(v)=4*j*(3*v^2+j)/(v^2*(v^2+j)^2), j=1,2,
    K(z,w)=[Q_1(z)Q_2''(w)+Q_1(w)Q_2''(z)
                      -Q_2(z)Q_1''(w)-Q_2(w)Q_1''(z)]/2.

Primes here are ordinary complex derivatives. This standalone rational
statement does not require any divisor, zeta estimate, Gaussian width,
probability interpretation, nonnegative profile, RH or conjugacy
relation between z and w. In particular w need not equal conjugate(z).

## Conclusion

Put T=z^2-1, U=w^2-1 and H(t)=t^2(t+1)^4(t+2)^4. All denominators
below are nonzero, and throughout the closed product strip,

    Re K(z,w)<-8040*|T|^7*|U|^7/(|H(z^2)|*|H(w^2)|)<0.       (36)

Both real coordinates are unbounded above. The estimate is strict at
every finite point; no uniform negative constant at infinity is claimed.
This local result of attempt1851 passes conceptual audit1853 below.

The possible downstream use is a sign for retained complex divisor cores
after a justified Gaussian contour deformation. No such deformation is
proved here. Its endpoint connectors, tails, origin subtractions, pole
checks and divisor exchanges remain obligations. C034d's R and the
comparison C034c(20) with S4^3/5 remain unpaid. This is neither the final
ECT prefix nor conditioning, exact weights, TV<=2, full observations,
signed-height cancellation or actual-Xi realization.

## Proof

### Scope and exact algebra

The pre-invocation EXPLORE assessment1850 covers precisely this kernel,
domain and whole-domain sign test. Its source comparison is recorded in
`drafts/literature/2026-11-20-laplace-complex-kernel-source-notes-1850.md`.
The inspected exact-enclosure reference is T. Hamadneh, H. Al-Zoubi,
M. Al-Qudah and A. Zraiqat, *Linear Optimization of Polynomials and
Rational Functions over Boxes*, arXiv:1906.03472v1, Section2(1)-(6),
pp2-3 and Section4(17)-(18), p8,
[primary source](https://arxiv.org/pdf/1906.03472v1).
It does not give this sign. Its Bernstein enclosure is not invoked:
the certificate below consists of an explicit polynomial identity,
coefficient inspection and elementary argument estimates. This is the
target-specific algebra missing from the assessment, not a reproof of
the general enclosure theorem. No contour theorem or Gaussian formula
is used. No originality claim follows from the recorded search.

For t=v^2, direct differentiation gives

    Q_j''(v)=24*j*(10*t^3+5*j*t^2+4*j^2*t+j^3)
                                    /(t^2*(t+j)^4).          (37)

This can also be checked by d_v^2=2*d_t+4t*d_t^2, starting from
Q_j(v)=4j(3t+j)/(t(t+j)^2). Define four real polynomials

    a1(t)=t*(3t+1)*(t+1)^2*(t+2)^4,
    a2(t)=t*(3t+2)*(t+2)^2*(t+1)^4,
    b1(t)=(10t^3+5t^2+4t+1)*(t+2)^4,
    b2(t)=(10t^3+10t^2+16t+8)*(t+1)^4.

Multiplication by H(t) gives Q_1 H=4a1, Q_2 H=8a2,
Q_1'' H=24b1 and Q_2'' H=48b2, where Q_j and Q_j'' are
evaluated at v and H at t=v^2. Consequently, for t=z^2,u=w^2,

    -K(z,w)=96*P(t,u)/(H(t)H(u)),
    P(t,u)=a2(t)b1(u)+b1(t)a2(u)
                          -a1(t)b2(u)-b2(t)a1(u).            (38)

Write P(T+1,U+1)=sum_(i,j=0)^8 c_ij T^i U^j. The entire coefficient
matrix is displayed below; row i and column j begin at zero. It follows
by expanding the four factored polynomials in (38) and using the
binomial theorem, so it is a finite exact identity rather than a
numerical sample or a rounded enclosure.

```text
508032 2179008 3953232 3946368 2392228 926936 233744 36520 2748
2179008 9089280 16045344 15550080 9112316 3404176 832384 128480 9780
3953232 16045344 27571536 25929720 14655039 5251994 1237568 188350 14577
3946368 15550080 25929720 23543040 12716570 4307902 962416 143870 11490
2392228 9112316 14655039 12716570 6442436 1994826 404367 58500 4998
926936 3404176 5251994 4307902 1994826 529352 85726 11170 1134
233744 832384 1237568 962416 404367 85726 7440 410 105
36520 128480 188350 143870 58500 11170 410 -100 0
2748 9780 14577 11490 4998 1134 105 0 0
```

The only negative coefficient is c_77=-100. Separate the block

    B(T,U)=105*T^8*U^6+105*T^6*U^8-100*T^7*U^7.              (39)

Every coefficient of P(T+1,U+1)-B(T,U) is nonnegative, and its
constant coefficient is 508032>0. It is not legitimate to discard
the negative coefficient; (39) will be bounded as a whole.

### Argument bounds on the full domain

Write z=x+iy, x>=13, |y|<=1/2. Then

    Re T=x^2-y^2-1>=671/4>0,
    |Im T|/Re T<=x/(x^2-5/4)<=52/671.                       (40)

For the last inequality, cross multiplication reduces to
(x-13)(13x+5/4)>=0. Thus T is nonzero and its principal argument
has magnitude theta<=arctan(52/671)<52/671. The same statements hold
for U, independently. Since z^2=T+1, the factors z^2,z^2+1,z^2+2
all have positive real part, as do their w counterparts. This proves
nonvanishing of every denominator in (37)-(38) on the entire domain.

For c=1,2,3, the argument of T+c has the same sign as that of T,
and its magnitude theta_c satisfies

    (4/5)*theta<=theta_c<=theta.                            (41)

To verify the lower bound, put a=Re T, b=|Im T|, r=b/a and
k=a/(a+c). Then k>=671/683>4/5, theta=arctan r and
theta_c=arctan(kr). For 0<k<=1,

    arctan(kr)=int_0^r k/(1+k^2 s^2) ds
                   >=k*int_0^r 1/(1+s^2) ds=k*arctan r.

This also covers b=0. The upper bound in (41) follows from k<=1.

Now H(T+1)=(T+1)^2(T+2)^4(T+3)^4. For Im T>=0, an argument
of T^i/H(T+1), 0<=i<=8, is

    psi_i=i*theta-2*theta_1-4*theta_2-4*theta_3.

By (41),

    -(10-i)*theta<=psi_i<=(i-8)*theta<=0.

For Im T<0 the arguments reverse sign and the same absolute bound
holds. Hence in all cases |psi_i|<=(10-i)*theta. This is an explicit
argument obtained by multiplication, so no choice of a principal
argument for a product is tacitly used. Applying the same reasoning
to U proves that each monomial divided by the common denominator has
an argument phi_ij satisfying

    |phi_ij|<=(10-i)*theta_T+(10-j)*theta_U
                    <=(20-i-j)*52/671<=1040/671<31/20.      (42)

An elementary exact cosine bound suffices, with no rounded value of
pi. For |s|<=v=31/20<2, the alternating cosine series gives

    cos s>=1-s^2/2+s^4/24-s^6/720.

The polynomial on the right decreases on [0,v]: its derivative is
-s+s^3/6-s^5/120<0 for s>0 because v^2<6. Therefore

    cos s>=1-v^2/2+v^4/24-v^6/720
                  =921148319/46080000000>0.                (43)

The alternating-series lower bound is valid since the omitted tail
starts with +s^8/8! and its absolute terms decrease for |s|<2.
Equations (42)-(43) show that every rational monomial with a positive
coefficient in P(T+1,U+1)-B(T,U) has strictly positive real part.
The constant coefficient is positive, so their finite sum has strictly
positive real part. This remains true for either sign of either
imaginary coordinate and when either is zero.

### Paying the one negative coefficient

For all three monomials in (39), i+j=14. Thus their angle bound in
(42) improves to312/671<1/2. The elementary bound
cos s>=1-s^2/2 then gives cos(phi)>7/8 for the two positive terms.
Write R_T=|T|>0, R_U=|U|>0 and D=|H(T+1)H(U+1)|>0. The negative
term is bounded below using Re(-v)>=-|v|. Consequently

    Re[B(T,U)/(H(T+1)H(U+1))]
      >( (735/8)*(R_T^8 R_U^6+R_T^6 R_U^8)
                                         -100 R_T^7 R_U^7 )/D
      >=(335/4)*R_T^7 R_U^7/D>0.                          (44)

The second inequality uses R_T^2+R_U^2>=2 R_T R_U, which follows
from (R_T-R_U)^2>=0. This retains independent moduli and does not
assume z=w or conjugacy. Adding the strictly positive remainder
from (43), then multiplying by96 in (38), proves (36), since
96*(335/4)=8040.

All estimates were made directly for arbitrary finite x>=13 and
arbitrary finite Re w>=13. There is no finite-box truncation, limiting
face, compactification, infinite sum, contour, or exchanged limit in
this proof. The signs at |Im z|=|Im w|=1/2 and Re z=Re w=13 are
covered by the non-strict hypotheses and strict scalar margins above.

### Reproduction and limits

Run `python3 scripts/smoothed-law/laplace_complex_kernel_1851.py`.
The full exact certificate is
`scripts/smoothed-law/laplace_complex_kernel_1851.json`.
It starts from Q_j, differentiates by the quotient rule, and checks
the six cleared identities by polynomial cross multiplication. It
also checks the shift by two constructions, the complete coefficient
matrix, exceptional block, rational angle/cosine margins and the
normalization K(1,1)=-784/27. All20 checks pass. The complete
load-bearing coefficient matrix, zero difference arrays and exact
scalar values were inspected, not merely previewed. The program
checks the finite algebra and bounds; the domain and complex-argument
proof is the argument above, verified separately in audit1853 below.

The raw numerator has twelve negative coefficients; merely shifting
leaves one. Those two simple coefficient tests are inconclusive, not
counterexamples. The combined block and sector bounds resolve this
specific sign test. They do not bound C034d's origin/cutoff R or any
contour connector. Preserve stops1847/1843/1839 and their cited older
evidence; the sign supplies no automatic closure of those gaps.

For a later actual-divisor use, retain C034d/c/b and C032n's actual
divisor, conjugation and multiplicities, excluded ordinate0, gamma>14,
strict strip, count, through100/retained real zero, reciprocal-square
tail, heat positivity/separate fixed-j errors, both fixed-v1 input
qualifications, zero drift/killing and Gaussian half-variance. C032m
and C033w through C033l/C032q supply the qualified probability context.
Source-wide/finite-zero validity and global Sobolev membership remain
unverified. None is asserted or silently used in this rational result.

### Conceptual audit1853 — 20 November 2026

**Verdict and scope.** The complete proof of (36) passes for the stated
independent closed product strip, including its finite edges and without
an upper cutoff. Assessment1851, separately approved1852, authorizes
exactly this audit; the unchanged source comparison1850 is reused.
This verifies a local mathematical input, without an originality claim
or an RH candidate. No contour conclusion is added.

**Independent algebra.** The replay
`python3 scripts/smoothed-law/laplace_complex_kernel_audit_1853.py`
starts with Q_j as a rational function of v, applies the ordinary
quotient rule twice in v, and clears H(v^2) by exact polynomial
division. Thus it does not assume (37) or differentiate in t as the
original program did. The two derivative differences and four division
remainders are identically zero; the derived factors are exactly
a1,a2,b1,b2 displayed above. Substitution in K gives coefficient
(4*48)/2=(8*24)/2=96 with the minus sign in (38). The independently
formed bivariate numerator is translated by successive Horner
composition in each variable. All81 entries agree both with the
displayed matrix and with certificate1851, including the exceptional
105,105,-100 block and every zero entry. The positive constant and
nonnegative remainder are verified after subtracting that entire block.
The original20 checks replay unchanged; all20 independent checks pass.
Full exact evidence is in
`scripts/smoothed-law/laplace_complex_kernel_audit_1853.json`.
Its complete factor, raw/shifted/remainder matrix, derivative/division,
scalar and check fields were inspected. Computation verifies this finite
algebra; the following argument checks establish its domain coverage.

**Selected arguments.** In (40), cross multiplication is valid because
x^2-5/4>0. The difference is
52*x^2-671*x-65=4*(x-13)*(13*x+5/4)>=0.
Consequently a=Re T>=671/4 and |arg T|<52/671 for every finite x>=13.
All denominator factors have positive real part. For c<=3,
a/(a+c)>=671/683>4/5; the integral in (41) uses
1+k^2*s^2<=1+s^2 and hence proves the claimed lower bound, including
zero imaginary coordinate. The weighted denominator argument lies
between8*theta and10*theta. Therefore for each 0<=i<=8 the explicitly
selected argument psi_i lies between -(10-i)*theta and0 when Im T>=0,
and is reflected when Im T<0. Multiplying the independent z and w
factors adds these selected arguments; it does not require either
product to have that principal argument. The triangle inequality gives
(42) for all four sign combinations and both zero-imaginary cases.

**Strict margins and finite edges.** The narrow comparison in (42) is
exact: 31/20-1040/671=1/13420>0. The alternating cosine remainder
and decreasing polynomial in (43) give the displayed strictly positive
bound without an assumed numerical value of pi. For the three terms of
B, 1/2-312/671=47/1342>0; thus each positive term has cosine strictly
greater than7/8, independently of its modulus. The negative term obeys
Re(-v)>=-|v| even when its phase differs from the positive terms.
Finally (|T|-|U|)^2>=0 proves (44) with the coefficient335/4, and
96*(335/4)=8040. T,U and the denominator are nonzero; the positive
constant term also gives a strictly positive remainder. None of these
strict steps requires x>13, |y|<1/2, equal moduli, equal phases or
conjugacy. The argument is pointwise for every finite real coordinate,
so an asymptotic face or uniform negative constant is not required.

**Qualification and mathematical inputs.** C034d is the sole direct
local input, supplying K's rational definition; the real ordering proof
and its divisor hypotheses are not used in this standalone complex
sign. The existing DAG entry therefore remains correct and unchanged.
The already stated actual-divisor qualifications, contour connectors,
tails, origin terms, R and C034c(20) remain unproved here. In particular
the audit does not replace a signed spatial profile by a nonnegative
weight. Stops1847/1843/1839 remain valid for their stated mechanisms.

## Mathlib

Full matching coverage is unchecked and unknown; no absence claim is
made. No Mathlib theorem is imported. Polynomial identities, complex
arguments, elementary cosine bounds and finite sums are the supporting
mathematics, but no complete matching theorem has been verified. The
exact Python certificate is not a formal Mathlib proof.
