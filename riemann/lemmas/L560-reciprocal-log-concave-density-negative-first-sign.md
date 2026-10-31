# Lemma 560: a reciprocal log-concave density with a negative first polynomial sign

## Hypotheses

Set a=10+i/4 and

    P(z)=(1-z^2)(1-z^2/4)(1-z^2/a^2)(1-z^2/conjugate(a)^2).

The bilateral Laplace convention is integral_R exp(-zx)p(x) dx.
This is a fixed finite polynomial diagnostic; no Xi, theta, PF256,
self-decomposability or infinite-product hypothesis is assumed.

## Conclusion

There is an even, strictly positive, integrable C2 probability density p
on R such that, throughout |Re z|<1,

    integral_R exp(-zx)p(x) dx = 1/P(z),
    p'(x)^2-p(x)p''(x)>0          (all real x).

Nevertheless

    P'(10)^2-P(10)P''(10)=-7390676030193099/6569999366401<0.

Thus ordinary log-concavity of the reciprocal-transform density, even
with evenness and C2 regularity, does not imply the first Laguerre sign
of its reciprocal polynomial at every real point. This tests the
log-concavity/PF2-only inference, not any stronger finite-order total
positivity hypothesis. In particular it proves no claim about PF256,
actual-Xi signs, the complete theta residual, or RH. No originality
beyond the sources assessed is claimed.

## Proof

All constants below are rational. Define

    A=5126402/7536867,                 B=-2563201/7087875,
    C=31766670568/5935596798625,        D=247683050816/5935596798625,
    c=(C+iD)/2.

For x>=0 put

    f(x)=A exp(-x)+B exp(-2x)
          +exp(-10x)(C cos(x/4)+D sin(x/4)),
    p(x)=f(|x|).

Equivalently f=A exp(-x)+B exp(-2x)+c exp(-ax)
+conjugate(c)exp(-conjugate(a)x). The conjugate terms include both
nonreal poles; their sine coefficient has the displayed positive sign.

**Transform and normalization.** Every term is absolutely integrable,
and has absolute exponential moments for |Re z|<1. Direct integration
on the two half-lines gives, for Re lambda>|Re z|,

    integral_R exp(-zx)exp(-lambda|x|) dx
      =1/(lambda+z)+1/(lambda-z)=2lambda/(lambda^2-z^2).

This applies also to lambda=a and conjugate(a). Consequently the
transform of p is

    2A/(1-z^2)+4B/(4-z^2)
       +2ac/(a^2-z^2)+2conjugate(ac)/(conjugate(a)^2-z^2).     (1)

Here a^2=(1599+80i)/16 and |a^2|^2=2563201/256. For an explicit
polynomial check let

    d1=1-z^2, d2=4-z^2,
    dc=z^4-(1599/8)z^2+2563201/256,
    nc=4 Re(ac conjugate(a)^2)-4 Re(ac)z^2.

The numerator of (1), over d1*d2*dc, is

    2A*d2*dc+4B*d1*dc+nc*d1*d2=2563201/64.

Also P=64*d1*d2*dc/2563201. These exact coefficient identities
prove (1)=1/P throughout the stated strip; no residue orientation,
contour limit or Fourier-normalization input is needed. At z=0 this
identity gives integral p=1. There are no poles in the open strip.

**Zero matching, positivity and decay.** Direct differentiation gives

    f(0)=21691949/66971775,
    f'(0)=0,
    f''(0)=-58953623/133943550,
    f'''(0)=0.

In particular the even extension is C2 at zero: the one-sided first
derivatives agree at zero, and the second derivatives both tend to
f''(0). More explicitly, p'(0)=0, and for h!=0,
p'(h)/h=f'(|h|)/|h| tends to f''(0), so the second derivative at
zero exists and equals the same limit. Away from zero the formula is
analytic. Since A>0, B<0 and
C,D>0, for x>=0,

    f(x)>=(A+B-C-D)exp(-x),
    A+B-C-D=4833914684009/17806790395875>0.

Indeed B exp(-2x)>=B exp(-x), the oscillatory bracket is at least
-C-D, and exp(-10x)<=exp(-x). This proves strict positivity.
Also |f(x)|<=(A+|B|+C+D)exp(-x), proving integrability and the
absolute exponential moments used above.

**Global curvature.** For a sum sum_j c_j exp(-lambda_j x), direct
multiplication gives

    f'^2-ff''=-sum_(j<k) c_j c_k (lambda_j-lambda_k)^2
                                  exp(-(lambda_j+lambda_k)x).

Use the four terms with lambda=1,2,a,conjugate(a). Define

    b=-AB=13139998732802/53420371187625,
    u=-2Ac(a-1)^2=u_r+i u_i,
    v=-2Bc(a-2)^2=v_r+i v_i,
    k=|c|^2/4=16414739204/148389919965625.

Their real and imaginary parts are

    u_r=-5756989644681283/34491752996809875,
    u_i=-79800320299202816/34491752996809875,
    v_r=26015847378648431/410446518624918750,
    v_i=199595858502737404/205223259312459375.

The pair a,conjugate(a) contributes +k exp(-20x), since
(a-conjugate(a))^2=-1/4. Thus, exactly,

    exp(3x)(f'^2-ff'')
       =b+exp(-8x)(u_r cos(x/4)+u_i sin(x/4))
          +exp(-9x)(v_r cos(x/4)+v_i sin(x/4))+k exp(-17x).    (2)

We certify (2)>0 globally, without a sampling argument. On 0<=x<=1
both sine and cosine are nonnegative, so the v and k terms are
nonnegative. Put e=-u_r>0 and h=-u_i>0. Since cos(x/4)<=1 and
sin(x/4)<=x/4, the u term is at least -exp(-8x)(e+hx/4).
The derivative of exp(-8x)(e+hx/4) is
exp(-8x)(h/4-8e-2hx), which is nonpositive because

    8e-h/4=42448515581544/56084151214325>0.

It follows that (2) is at least

    b-e=b+u_r=1596333387589/20190294437157>0.              (3)

For x>=1 use |sin|,|cos|<=1 and discard k. Since exp(1)>2,
exp(-8x)<1/256 and exp(-9x)<1/512. Therefore (2) is greater than

    b-(e+h)/256-(v_r+v_i)/512
       =286072961398359582124871/1221173616501454262400000>0. (4)

Equations (3)--(4) cover all nonnegative x, including zero and the
joining endpoint. Evenness and C2 matching extend the curvature sign
to negative x as well. As p>0, the identity
(log p)''=(pp''-p'^2)/p^2 proves strict log-concavity everywhere.

**Polynomial jet.** Expand the conjugate factors as

    (1-z^2/a^2)(1-z^2/conjugate(a)^2)
      =1-(51168/2563201)z^2+(256/2563201)z^4.

Exact differentiation of this polynomial times (1-z^2)(1-z^2/4)
gives

    P(10)=15208776/2563201,
    P'(10)=7761615/2563201,
    P''(10)=979818323/5126402.

Their substitution proves the negative value in the conclusion.
The real evaluation 10 lies outside the transform's open strip;
the claimed inference being tested asks for all real polynomial
arguments. No divergent transform integral is evaluated at z=10.

**Reproduction and source scope.** Run
`python3 scripts/reciprocal-pf2/fixed_model.py`.
It verifies the full rational transform numerator identity, derivative
matching, all rational bounds (3)--(4), and the exact jet. Its complete
certificate is `scripts/reciprocal-pf2/fixed-model-certificate.json`.
All listed checks passed with no failures. Decimal output is only a
summary; the proof uses exact rational values. The calculus and direct
finite integration above are elementary model-specific checks, not a
reproof of a known inversion theorem. The assessed DLMF 1.14.1--4
inversion alternative is unnecessary. Literature scope and prior
comparisons are retained in
`drafts/literature/2026-10-31-reciprocal-pf2-first-sign-model.md`.

**Independent audit, 31 October 2026.** The complete analytic argument
above was checked against the saved audit assessment. In particular,
Re(lambda)>|Re z| justifies each half-line integral absolutely; the
conjugate pair gives +D sin(x/4); the even extension has the stated
second derivative at zero; and (3)--(4) cover every x>=0 including both
endpoints. No inversion theorem, numerical sampling or transform value
at 10 enters the proof. There was no mathematical defect to repair.
The regularity explanation above makes the origin limit explicit.

Run `python3 scripts/reciprocal-pf2/audit_fixed_model.py` for the
independent exact replay. It uses the four defining polynomial factors
and directly multiplies the ordered exponential sums for f'^2-ff'',
without importing the original script. All 27 exact checks passed;
every numeric field of the original certificate agrees, including the
entire rational numerator, all origin jets, the six curvature terms,
the global bounds and the polynomial jet. Complete actual/required
values and the empty failures list are retained in
`scripts/reciprocal-pf2/independent-audit-certificate.json`.
This first audit validates the existing qualified countermodel; it
establishes no stronger conclusion or originality claim. Finite-order
determinants, including strict PF256, are not certified by this audit.

## Mathlib

The full matching countermodel, rational-transform calculation and
supporting calculus coverage have not been checked in Mathlib.
Availability is unknown; no absence or formal verification is claimed.
Documentation: https://leanprover-community.github.io/mathlib4_docs/
