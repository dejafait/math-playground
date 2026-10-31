# Lemma 561: partial certificate for the fixed high-rank reciprocal model

## Hypotheses

Fix A=2^20, b=1/4, a=A+ib and m=270. Put

    Q(z)=(1-z^2/a^2)(1-z^2/conjugate(a)^2),
    P_*(z)=(1-z^2)^270 Q(z),
    p_*(x)=(1/(2*pi)) integral_R exp(iux)/P_*(iu) du,
    H_k(x)=(-1)^(k(k-1)/2) det[p_*^(i+j)(x)]_(i,j=0)^(k-1).

The bilateral Laplace convention is integral exp(-zx)p_*(x) dx.
This is the single fixed model in the preexisting EXPLORE assessment
`drafts/literature/2026-10-31-high-rank-pf256-fixed-model.md`.
No Xi realization, PF256 premise or source probability certificate is used.

## Conclusion

The Fourier integral is absolutely convergent and defines a real even,
strictly positive C^542 probability density. With ell(x)=exp(-|x|)/2,

    p_*(x) > (1/2) ell^{*270}(x) > 0                 (x in R).

It has absolute exponential moments of every order sigma<1, sigma>=0,
and its bilateral transform is 1/P_*(z) on |Re z|<1. Moreover

    (P_*'(A)^2-P_*(A)P_*''(A))/P_*(A)^2
      = -170277282315511414008713060143186594067936298338644
         /5321165072441475074137145028169664078494042230125
      < -31.

For all integers 1<=k<=256, H_k(0)>0. There exist common constants
eta>0 and X>eta such that H_k(x)>0 for all these k whenever
|x|<=eta or |x|>=X. The tail proof gives, for x tending to +infinity,

    H_k(x) ~ exp(-kx) alpha^k
                   (prod_(j=0)^(k-1) j! (269)_j) x^(k(270-k)),
    alpha=1/(2^270 * 269! * Q(1)) > 0,

where (269)_j=269*268*...*(270-j) and (269)_0=1.
The constants eta and X are not made effective here.

**Scope of this partial certificate:** the arguments here leave H_k
on the intervening range for 2<=k<=256 unresolved and do not establish
strict PF256. L562 subsequently supplies and independently audits the
global certificate. The retained-input audit below verifies this lemma's
density, transform, regularity and negative first sign, without relying
on its optional origin/tail estimates. Neither result gives an actual-Xi
sign, RH conclusion, or originality certification.

## Proof

### Density and transform, including the signed convolution factor

Let f=ell^{*270}. It is an even, continuous, strictly positive
probability density. Writing f=ell*ell^{*269} and using the triangle
inequality inside this convolution gives the pointwise bounds

    exp(-|y|) f(x) <= f(x-y) <= exp(|y|) f(x).          (1)

Define a real even, generally signed function h by, with r=|x|,

    c0=(A^2+b^2)/(4A),
    h(x)=c0 exp(-Ar) (cos(br)+(A/b)sin(br)).             (2)

It is integrable, with absolute exponential moments below A.
For any complex lambda with Re lambda>|Re z|, direct integration gives

    integral_R exp(-zx) exp(-lambda|x|)/(2lambda) dx
        =1/(lambda^2-z^2).

The elementary partial fraction identity

    1/Q(z)=|a|^4/(conjugate(a)^2-a^2)
               (1/(a^2-z^2)-1/(conjugate(a)^2-z^2))

therefore proves that (2) has bilateral transform 1/Q(z) throughout
|Re z|<A. Indeed conjugate(a)^2-a^2=-4iAb, and the inverse expression
is exactly c0 exp(-Ar)(cos(br)+(A/b)sin(br)), with the positive sine
coefficient shown. In particular integral h=1; h itself is not
assumed nonnegative.

For 0<=sigma<1, the triangle inequality in a convolution gives

    integral exp(sigma|x|) f(x) dx
        <= (integral exp(sigma|x|) ell(x) dx)^270 < infinity.

The analogous absolute bound for h permits Fubini for f*h, both with
this weight and with exp(-zx) for |Re z|<1. Thus f*h is integrable,
continuous, real and even, has the required absolute moments, and has
transform (1-z^2)^(-270)/Q(z)=1/P_*(z). Its integral is 1.

Here is a quantitative positivity argument that does not discard the
signed part of h. Define

    h0(x)=(A/4)(1+A|x|)exp(-A|x|),
    epsilon=b^2/A^2,       E=h-(1+epsilon)h0.

The inequalities |cos v-1|<=v^2/2 and |sin v-v|<=|v|^3/6 hold for
all real v, by Taylor's theorem with bounded derivatives. Consequently

    |E(x)| <= c0 b^2 exp(-Ar)(r^2/2+Ar^3/6),
    integral exp(|y|)|E(y)| dy <= delta,
    delta=(A^2+b^2)b^2(2A-1)/(2A(A-1)^4).               (3)

The last formula follows by integrating r^2 and r^3 on [0,infinity).
Also

    M=integral exp(-|y|)h0(y) dy=A(2A+1)/(2(A+1)^2).

Using (1), h0>=0, and the absolute bound (3) yields

    (f*h)(x) >= ((1+epsilon)M-delta) f(x).              (4)

All constants are fixed rationals. For a transparent strict bound,
A>=8 implies M>=(A/(A+1))^2>=64/81. Since A^2+b^2<=2A^2,
A-1>=A/2 and 2A-1<=2A,

    delta <=32b^2/A^2=2/A^2<=1/32.

Hence the coefficient in (4) is at least
64/81-1/32=1967/2592>1/2. This proves strict positivity on all R.
The certificate also stores its sharper exact value

    (1+epsilon)M-delta
      =41977733198765155386868679947546458503249921
         /41977793248403718949638339179210342400000000.

To identify this function with the specified inverse Fourier integral,
observe that

    phi(u)=1/P_*(iu)=1/((1+u^2)^270 |1+u^2/a^2|^2)>0.

There are no real u singularities, and phi(u)=O(|u|^(-544)) at infinity.
The standard Fourier inversion theorem for an L1 function with L1
Fourier transform, applied to the continuous function f*h, gives the
displayed defining integral for p_* at every real x. This is a named
standard inversion input, not an inference from point samples.
For every integer 0<=j<=542, |u|^j phi(u) is integrable. Dominated
differentiation then gives

    p_*^(j)(x)=(1/(2*pi)) integral (iu)^j exp(iux)phi(u) du,

with continuous derivatives. Thus p_* is C^542, in particular C^510.

### The first polynomial sign at the frozen real point

For a polynomial P with roots r of multiplicities n_r, at a point
where P is nonzero, differentiation of P'/P gives the algebraic identity

    (P'^2-PP'')/P^2=sum_r n_r/(t-r)^2.

No branch of a logarithm or transform evaluation at t is needed.
Here P_*(A)>0: (1-A^2)^270>0 and Q(A)=|1-A^2/a^2|^2>0.
The exact root sum at t=A is

    S=270/(A-1)^2+270/(A+1)^2 - 2/b^2
         +2(4A^2-b^2)/(4A^2+b^2)^2.                   (5)

Since b=1/4 and A>2, it satisfies

    S < -32+(1350+1/2)/A^2 < -31.

The first inequality uses (A-1)^(-2)<4/A^2,
(A+1)^(-2)<1/A^2 and the last summand of (5)<1/(2A^2).
Exact rational evaluation gives the fraction in the conclusion.
The script separately uses

    Q(z)=1-2(A^2-b^2)z^2/(A^2+b^2)^2+z^4/(A^2+b^2)^2

to evaluate Q,Q',Q'' at A, and obtains the identical normalized sign
from the quartic jet and the real-pole contribution. The real point A
is outside the transform strip; no divergent bilateral integral at A
is used.

### Origin and a common neighborhood

For k<=256, put

    M_ij=(1/(2*pi)) integral_R u^(i+j) phi(u) du,
    D=diag(1,i,i^2,...,i^(k-1)).

All needed moments exist. For any nonzero real polynomial v of degree
less than k, integral v(u)^2 phi(u) du>0, since phi is strictly positive
on R. Hence the real moment matrix M is positive definite and det M>0.
The derivative formula at zero is [p_*^(i+j)(0)]=D M D, so

    det[p_*^(i+j)(0)]=(-1)^(k(k-1)/2)det M,
    H_k(0)=det M>0.

Each H_k is continuous, and there are only 256 indices. Taking a
smaller common neighborhood proves their positivity for |x|<=eta
for some eta>0. No numerical value of eta is asserted. This moment
proof is confined to the origin; exp(iux) for nonzero x does not give
a positive moment measure by the same argument.

### Exact tail reduction and its limit

The proper rational function 1/P_*(z) has poles at +/-1 of order 270
and at +/-a, +/-conjugate(a) of order one. Its evenness pairs its partial
fraction terms. For Re lambda>0 the even extension of
x^(j-1)exp(-lambda x)/(j-1)! on x>=0 has bilateral transform

    1/(z+lambda)^j+1/(lambda-z)^j.

Partial fractions and uniqueness of the Fourier transform on L1
therefore give, for x>0, the exact finite representation

    p_*(x)=exp(-x)R(x)+c exp(-ax)+conjugate(c)exp(-conjugate(a)x),  (6)

where R is a real polynomial of degree 269. The highest pole coefficient
at -1 is

    lim_(z->-1) (z+1)^270/P_*(z)=1/(2^270 Q(1)).

It follows that R(x)=alpha x^269+O(x^268), with the positive alpha
given above. All functions used for this partial-fraction inversion
are integrable and continuous; equality a.e. upgrades to equality
on x>0, where they are analytic. Thus all derivatives in (6) can be
taken there. No contour displacement or unproved remainder is used.

For g(x)=exp(-x)R(x), binomial expansion of (D-1)^(i+j) and the
lower triangular binomial matrix with diagonal 1 imply

    det[g^(i+j)(x)]=exp(-kx) det[R^(i+j)(x)].           (7)

For an integer d>=k-1,

    det[(d)_(i+j)]_(i,j=0)^(k-1)
       =(-1)^(k(k-1)/2) prod_(j=0)^(k-1) j! (d)_j.    (8)

Indeed factor (d)_i from row i. The remaining entry (d-i)_j is a
polynomial in i of degree j and leading coefficient (-1)^j; its
evaluation determinant is that sign product times the Vandermonde
of 0,1,...,k-1, namely prod j!. This argument includes entries equal
to zero when i+j>d, with the usual falling-factorial convention.

Factoring the powers x^(269-i-j) out of the normalized derivative
matrix and using (8) shows that its determinant has leading term

    (-1)^(k(k-1)/2) alpha^k
       (prod_(j=0)^(k-1) j! (269)_j) x^(k(270-k)).      (9)

For k<=256 its coefficient is nonzero with the stated sign; every
falling-factorial factor is positive. The remaining polynomial terms
are lower degree. By multilinearity of the determinant, the difference
between the derivative determinants of p_* and g in (6) is, for each
fixed k and x>=1,

    O(exp(-(k-1+A)x)(1+x)^(269(k-1))).                 (10)

Every term of that difference contains at least one fast exponential
column; fixed derivative factors a^j only change the constant. Relative
to (7)--(9), (10) tends to zero because A>1, irrespective of its
polynomial factor. This proves the tail asymptotic and eventual positive
H_k for each k<=256. A maximum of the finitely many cutoffs gives one X.
Evenness gives H_k(-x)=H_k(x), so both tails are included. Enlarging X
and shrinking eta if needed ensures X>eta.

These are existential endpoint bounds only. Neither (9) nor (10)
supplies a certified sign on the intervening compact range. There is
no monotonicity or no-zero theorem for H_k in this argument that would
join the positive regions. Global positivity of H_1 follows separately
from (4); the unsettled indices are 2 through 256.

### Source scope and verification

The approved source is S. Sra, *On some positivity properties of the
Riemann Xi function*, v2 (29 October 2026), Appendix C.4, Lemma C.6,
printed p.21, with the two Wronskian transfers supplied by Lemma C.1,
printed p.18: https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf.
Its hypothesis is p in C^(2m-2)(R) with H_k(x)>0 for every real x and
all 1<=k<=m; its conclusion is strict ordered minors through m. For
m=256 the regularity hypothesis is met here, but the global sign
hypothesis is not established by this partial argument. C.6 is therefore
not applied here to claim PF256; L562 supplies that later application.
No reproof of C.6 or use of C.7 is made.

The elementary computations above are needed to verify this fixed
model; the inspected literature did not supply these model properties.
L560 is a contrasting lower-order example, not a mathematical premise.
The retained inputs received the separate audit below. The optional
origin/tail proof is not certified by that narrower audit.

Reproduce the exact scalar checks with
`python3 scripts/reciprocal-pf256/fixed_model.py`.
The complete output is
`scripts/reciprocal-pf256/fixed-model-partial-certificate.json`.
All 13 scalar checks passed, including independent root-sum/quartic-jet
agreement and the global density lower bound. The exact first-sign and
density fields and empty failure list were inspected in full. The
origin/tail determinant assertions rest on the analytic proofs above,
not these scalar checks. No sampled H_k, compact-range certificate or
effective tail cutoff was produced.

### Independent audit of the retained inputs — 31 October 2026

The separately gated L561--L562 audit checked the density/transform,
regularity and first-sign sections in full. No failure was found in
these inputs. The origin and existential tail estimates are unnecessary
for L562's global proof and remain outside this audit's acceptance.

For the signed factor (2), integrating exp(-lambda|x|)/(2lambda)
on its two half-lines gives 1/(lambda^2-z^2) whenever
Re lambda>|Re z|. Subtract the terms for lambda=a,conjugate(a):
the denominator difference is -4iAb and the exponential difference
has imaginary part proportional to -(A sin(br)+b cos(br)). These
two signs cancel, giving exactly the positive sine coefficient in
(2). This verifies the normalization and avoids treating h as a
probability density. At z=0 its integral is 1. Absolute exponential
moments of h below A, and of f below 1, justify Fubini for their
convolution throughout |Re z|<1. Its continuity follows, for example,
from bounded uniform continuity of f and h in L1. Hence the Fourier
uniqueness and inversion use a continuous L1 representative.

The pointwise translation inequalities (1) follow from those of ell
inside its convolution with the nonnegative ell^{*269}. Since
c0=(1+epsilon)A/4, the Taylor error used for E is exactly the error
after subtracting (1+epsilon)h0. Its weighted integral is bounded by

    2 c0 b^2 [1/(A-1)^3+A/(A-1)^4]
       =(A^2+b^2)b^2(2A-1)/(2A(A-1)^4)=delta.

The lower bound for the h0 part and the upper bound for the absolute
E part use opposite sides of (1), as required for a signed convolution.
Their difference gives (4) with the stated coefficient. Independently,
M>=64/81, delta<=1/32, and 64/81-1/32=1967/2592>1/2. Thus the
positivity claim holds at every real x without discarding a negative
tail. Its integral is one by the already justified transform at zero.

For real u, the complex-pole factors of P_*(iu) are conjugates and
cannot vanish because a^2 has nonzero imaginary part. Consequently
phi is strictly positive, continuous, and O(|u|^-544). Every
|u|^j phi(u) for j<=542 is integrable, including at u=0. Dominated
Fourier differentiation therefore proves C^542 on the whole real
line, including the origin. This verifies the regularity needed to
identify L562's continuous weak derivatives with classical ones.

The root sum (5) includes both roots +/-1 with multiplicity 270 and
all four nonreal roots, each simple. The two roots at A+/-ib
contribute -2/b^2=-32; those at -A+/-ib contribute the last positive
summand in (5). The displayed upper estimate is strictly less than
-31 for the fixed A. Moreover Q(A)>0 and (1-A^2)^270>0, so the
normalized sign really determines the sign of P_*'^2-P_*P_*''.
The alternative quartic-jet calculation agrees exactly with this
root sum, without invoking a transform outside its convergence strip.

`python3 scripts/reciprocal-pf256/fixed_model.py` was replayed with all
13 scalar checks passing and no failures. The complete first-sign
and density fields, including the exact fractions in the conclusion
and (4), were inspected with the shared JSON inspector. The script's
global-sign status remains a description of this partial certificate;
L562, not a change to that scalar status, supplies the global proof.
This is verification of retained local inputs, not a new construction
or an independent audit of the external Xi manuscript.

## Mathlib

The full fixed-model result, finite-order differential criterion, and
supporting Fourier/Gram/asymptotic coverage have not been checked in
Mathlib. Availability is unknown; no absence or formal verification is
claimed. Reference: https://leanprover-community.github.io/mathlib4_docs/.
