# Corollary 40c: fixed order-one qualitative bridge countermodel

## Hypotheses

Write (a)_n=Gamma(a+n)/Gamma(a). Set

F(t)=1F2(3/2;1,100;-t^2/4),
G(w)=1F2(3/2;1,100;-w/4),
F(t)=sum_(n>=0)(-1)^n gamma_n t^(2n)/n!.

For real sequences let Delta f(n)=f(n+1)-f(n). Define the logarithmic
germ by log G(0)=0, S_k=-k[w^k]log G(w), and
H_1=((S_2,S_3),(S_3,S_4)). A normalized Stieltjes moment sequence
means the nonnegative integer moments of a probability measure on
[0,infinity); uniqueness of that measure is not required.

## Conclusion

The fixed F has all the following properties simultaneously:

1. F is even, real entire of exact order one, F(0)=1, and gamma_n>0.
2. For all integers n>=0 and r>=2,
   (-1)^(r-1) Delta^r log(gamma_n)>0.
3. For every real c>0, (gamma_n^(-c))_(n>=0) is a normalized
   Stieltjes moment sequence.
4. There is an actual nonnegative L1 density m on [0,infinity),
   of mass one and with every nonnegative real moment finite, such that
   F(t)=integral m(u)cos(tu)du for all real t.
5. det(H_1)=-6279691/23154296938026762240000000<0.

Thus these qualitative premises, even including exact order one, do
not imply positivity of every logarithmic Hankel matrix. This only
refutes that generic implication. There is no actual-Xi realization,
quantitative coefficient bound, full continuous Mellin-ratio premise,
or conclusion about zeta zeros. This is a source-guided specialization
of known methods, not a claim of a new hypergeometric family.

## Proof

### Normalization and every-real-c inverse moments

The defining hypergeometric series gives

gamma_n=4^(-n)(3/2)_n/((1)_n(100)_n),
b_n=gamma_n^(-1)=4^n(100)_n(1)_n/(3/2)_n.                 (1)

All parameters are positive; hence gamma_0=1 and every gamma_n>0.
In particular the (1)_n=n! factor in (1) is retained even though the
series for F has its own n! denominator.

Import C. Berg, *On powers of Stieltjes moment sequences, II*,
[arXiv:math/0412340v1](https://arxiv.org/pdf/math/0412340v1),
Theorems 5.1-5.2, printed pp.14-15 (arXiv v1 dated17December2004,
PDF internal date27August2018). For a>0 and each real c>0 the gamma
moment law has Mellin transform [Gamma(a+z)/Gamma(a)]^c on Re(z)>-a.
For 0<a<b the beta moment law has Mellin transform
[Gamma(a+z)Gamma(b)/(Gamma(a)Gamma(b+z))]^c on Re(z)>-a.
Only real z>=0 is needed, so the powers here are positive real powers.
We import existence, not moment determinacy or arbitrary quotient closure.

For fixed c>0 take independent variables U_c,V_c from these laws,
with gamma parameter a=100 and beta parameters a=1,b=3/2. The latter
are the ordered parameters in Berg's theorem; the ordinary c=1 beta
distribution has shape parameters1,1/2. All integers n>=0 lie in
both Mellin domains. For X_c=4^c U_c V_c, Tonelli on the product
probability space, with finite individual moments, yields

E(X_c^n)=4^(cn)(100)_n^c [(1)_n/(3/2)_n]^c=b_n^c.

The zeroth moment is one. This proves claim3 for every real c>0,
including those for which gamma moments can be indeterminate.

### Strict differences at every n and order

Extend f(n)=log b_n to x>=0 by

f(x)=x log4+log Gamma(100+x)-log Gamma(100)
     +log Gamma(1+x)-log Gamma(1)
     -log Gamma(3/2+x)+log Gamma(3/2).

Differentiating the digamma integral
[NIST DLMF5.9.16](https://dlmf.nist.gov/5.9#E16), valid at positive
arguments, gives

f''(x)=integral_0^infinity t exp(-xt) A(t)/(1-exp(-t)) dt,
A(t)=exp(-100t)+exp(-t)-exp(-3t/2)>0 for t>0.             (2)

Indeed exp(-t)>exp(-3t/2), and the remaining term is positive.
For any compact interval of x>=0, the integrand in (2) is bounded
near0; each further x derivative contributes a power of t. At infinity
all these derivatives are dominated by a polynomial times exp(-t).
The same domination permits differentiating the source digamma
integral at arguments100+x,1+x,3/2+x, including x=0. Thus f is
smooth on a neighborhood of [0,infinity) and, for integer r>=2,

f^(r)(x)=(-1)^(r-2) integral_0^infinity
             t^(r-1) exp(-xt) A(t)/(1-exp(-t)) dt.

Repeated application of the fundamental theorem of calculus gives
Delta^r f(n)=integral_[0,1]^r f^(r)(n+u_1+...+u_r)du.
Apply Tonelli to the sign-adjusted nonnegative integrand and evaluate
each integral of exp(-tu_j). The result is

(-1)^r Delta^r f(n)=integral_0^infinity
 exp(-nt)(1-exp(-t))^r A(t)/[t(1-exp(-t))] dt>0.          (3)

Near0 this is O(t^(r-2)), and at infinity it is O(exp(-t)/t),
uniformly for n>=0. It is therefore finite even at n=0, and is
strictly positive since its integrand is positive for every t>0.
As log gamma_n=-f(n), (3) is exactly claim2. The affine geometric
normalization is annihilated by every difference of order at least2.

### An integrable cosine density and all interchanges

Let B=B(3/2,197/2), and let
p(s)=s^(1/2)(1-s)^(195/2)/B for 0<s<1.
This is a normalized beta density; its parameters sum to100.
Import the beta transform
[DLMF16.5.2](https://dlmf.nist.gov/16.5#E2), with
p=0,q=1,a0=3/2,b0=100 and remaining denominator1:

F(t)=integral_0^1 p(s) 0F1(;1;-t^2 s/4) ds
    =integral_0^1 p(s) J_0(t sqrt(s)) ds.                 (4)

The condition Re(b0)>Re(a0)>0 holds. The second identity is
[DLMF10.16.9](https://dlmf.nist.gov/10.16#E9) at nu=0.
There is no branch power at this integer parameter. The hypergeometric
series is uniformly absolutely convergent for s in[0,1] and t in any
compact set: it is bounded termwise by
sum_(n>=0)(R^2/4)^n/(n!)^2 for |t|<=R. Thus (4) involves no
unjustified sum-integral interchange.

The Poisson cosine integral
[DLMF10.9.4](https://dlmf.nist.gov/10.9#E4), admissible because
nu=0>-1/2, gives, for real t and s>0,

J_0(t sqrt(s))=(2/pi) integral_0^(sqrt(s))
                     cos(tu)/sqrt(s-u^2) du.             (5)

The conditional density in (5) has mass one, since substituting
u=sqrt(s)v gives (2/pi) integral_0^1(1-v^2)^(-1/2)dv=1.
Define for 0<=u<1

m(u)=(2/pi) integral_(u^2)^1 p(s)/sqrt(s-u^2) ds,

and set m(u)=0 for u>=1. It is measurable and nonnegative.
Since p(s)<=1/B,

0<=m(u)<=4 sqrt(1-u^2)/(pi B) for 0<=u<1.               (6)

In particular this is a finite actual density, including at0; there
is no endpoint atom. Tonelli and the conditional mass calculation give
integral_0^infinity m(u)du=integral_0^1 p(s)ds=1.
For real t the absolute double integral in (4)-(5) is at most1,
so Fubini yields F(t)=integral_0^1 m(u)cos(tu)du.
Every real q>=0 moment is finite because u^q<=1 on[0,1].
Even for complex t the double integrand is dominated in absolute value
by exp(|Im(t)|) times the joint density, uniformly on compact sets.
Thus the representation defines an entire function, with all its
derivatives justified by compact support. This proves claim4 and
also confirms the evenness, reality and F(0)=1 in claim1.

### Exact entire order, rather than just a growth upper bound

Import A. D. Sokal, *When does a hypergeometric function pFq belong
to the Laguerre-Polya class LP+?*, J. Math. Anal. Appl.515(2022),126432,
[published author PDF](https://discovery.ucl.ac.uk/id/eprint/10150527/1/Sokal_1-s2.0-S0022247X22004462-main.pdf),
p.1, the nonterminating p<=q order formula1/(q-p+1).
The numerator3/2 does not terminate, and denominators1,100 avoid
nonpositive integers. With p=1,q=2 it says that G has exact order1/2;
the nonzero scale -1/4 in its argument does not change order.
For M_h(r)=max_(|z|=r)|h(z)|, the map t->t^2 maps the circle
|t|=r onto |w|=r^2. Hence M_F(r)=M_G(r^2). In the definition
rho_h=limsup_(r->infinity)log log M_h(r)/log r, substitution R=r^2
gives rho_F=2rho_G=1. The upper bound exp(|Im(t)|) alone would not
have proved equality. This completes claim1.

### Exact H_1 and its negative direction

Put e_n=gamma_n/n!, so G(w)=sum(-1)^n e_n w^n. Its first terms are

e_0=1, e_1=3/800, e_2=3/517120,
e_3=7/1265909760, e_4=7/1854417141760.

Since G(0)=1, its logarithmic germ exists on a neighborhood of0.
Writing a_n=(-1)^n e_n, differentiate the germ and compare coefficients:

S_k=-k a_k-sum_(j=1)^(k-1) a_j S_(k-j), k=1,2,3,4.       (7)

This uses no zero-location or product representation. Exact substitution
in (7) gives

S_1=3/800,
S_2=159/64640000,
S_3=5351/1318656000000,
S_4=144513593/21948765388800000000.

Consequently

det(H_1)=S_2 S_4-S_3^2
        =-6279691/23154296938026762240000000<0.            (8)

For an explicit real negative direction take v=(S_3,-S_2). Since
S_2>0, direct multiplication gives

v^T H_1 v=S_2 det(H_1)
 =-332823623/498897918024683303731200000000000<0.

The full exact certificate is `scripts/beta-bessel/fixed-h1-782.json`;
reproduce it with `python3 scripts/beta-bessel/fixed-h1-782.py`.
It uses Python integer fractions throughout. In addition to (7), it
independently expands log(1+x)=x-x^2/2+x^3/3-x^4/4 through degree4
with x=G-1, checking all four coefficients. All eight checks pass,
including factorial normalization, both logarithm calculations and the
witness identity. No floating-point input, zero approximation, parameter
sweep, other matrix degree or adjacent minor is involved.

Sokal's AppendixA, pp.5-6, Propositions6-7/(12)-(14), motivates the
fixed parameters but its decimal threshold and continued-fraction
conventions are not inputs to (8). The general source moment theory
and entire-function order theorem have been imported rather than
reproved; the density, normalization, strict difference quantifiers
and fixed finite determinant are the necessary local specializations.
Assessment780 licenses exactly this test. The generic implication
fails already at its prescribed H_1; no claim that any stronger
actual-theta hypothesis holds for this model is made.

### Critical audit and independent exact verification — step784

The unchanged joint claims were critically reviewed under the approved
audit assessment782, reusing its precise primary-source domains. No
defect was found. In the moment argument, independence is required only
between U_c and V_c for each fixed c; no simultaneous coupling across
uncountably many c is asserted. The gamma law has parameter100, the
power-moment beta law has ordered parameters1,3/2 (ordinary beta
shapes1,1/2 at c=1), and the cosine mixture instead has beta shapes
3/2,197/2. Their distinct uses and the two factorials are essential.

For explicit endpoint domination in (2)-(3), A(t)<=2 for0<t<=1
and A(t)<=2exp(-t) for t>=1, while
1-exp(-t)>=t/e for0<t<=1. Thus the absolute r-th derivative
integrand is at most2e t^(r-2) near0 and at most
2t^(r-1)exp(-t)/(1-exp(-1)) at infinity, uniformly for x>=0,
for every fixed integer r>=2. The difference integrand is bounded
by2e t^(r-2) near0 and2exp(-t)/(t(1-exp(-1))) at infinity,
uniformly for n>=0. These are integrable bounds including n=0;
no uniformity as r tends to infinity is needed or claimed. Strictness
comes from A(t)>0 on every t>0, with the sign conversion
(-1)^(r-1)Delta^r log gamma=(-1)^r Delta^r f.
The finite bound (6), conditional mass1 and absolute Fubini bound
establish an actual density. Compact support is allowed by the stated
premises. The exact-order equality uses the full circle surjection
under squaring, so it does not infer equality from an upper bound.

The entire original arithmetic certificate was inspected at each
load-bearing field: e, gamma, S, log coefficients, H_1, determinant,
threshold, vector, quadratic form and both residual lists. An independent
check forms the Pochhammer symbols by finite products and uses the
following explicit polynomial identities, obtained by collecting the
degree1-4 terms of log(1-e_1 w+e_2 w^2-e_3 w^3+e_4 w^4):

S_1=e_1,
S_2=e_1^2-2e_2,
S_3=e_1^3-3e_1 e_2+3e_3,
S_4=e_1^4-4e_1^2 e_2+2e_2^2+4e_1 e_3-4e_4.

These give exactly the displayed four S values and (8). The scalar
expansion S_2 v_0^2+2S_3 v_0 v_1+S_4 v_1^2 reproduces the
displayed negative quadratic form. This check shares neither the
producer's coefficient recurrence nor its formal-power multiplication
loop. All19 exact checks pass, with no failures. Reproduce with
`python3 scripts/beta-bessel/fixed-h1-audit-784.py`; the complete
certificate is `scripts/beta-bessel/fixed-h1-audit-784.json`, which
records the original certificate's SHA256 and every recomputed value.
No original artifact was overwritten. Analytical claims are justified
above, not certified by arithmetic Boolean flags.

This verifies only the failure of the precise generic implication in
the conclusion. Neither this audit nor the original construction
establishes an actual-Xi sign, a stronger continuous Mellin condition,
or an RH counterexample. No further parameter or minor test follows.

## Mathlib

Full matching coverage has not been checked; availability is unknown.
No formal Lean proof is supplied, and unknown coverage is not absence.
Supporting matrix notion is
[Matrix.PosSemidef](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/PosDef.html#Matrix.PosSemidef).
The general moment laws and exact entire order are imported above by
precise primary citations; the joint specialization and certificate
are proved here, not attributed to a matching Mathlib theorem.
