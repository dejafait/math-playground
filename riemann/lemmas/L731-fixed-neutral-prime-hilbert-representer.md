# Lemma 731: the fixed neutral prime functional has a Hilbert representer

## Hypotheses

Let H=L²((1,∞),dy/y²), with ⟨v,w⟩=∫v conj(w)dy/y², linear in
the first entry. For every integer m≥2 put

    rho_m(y)=floor(y/m)-floor(y)/m,    a_m=(m-1)/(2m),
    f_m(y)=rho_m(y)+a_m,              K_m(x)=∫_x^∞ f_m(y)dy/y²,
    T_m(n)=sum_(j≥1)K_m(jn),          S_m=sum_(n≥1)Lambda(n)K_m(n).

Use the floor formula also for 0<y<1. The von Mangoldt function has
Lambda(1)=0. L729 establishes absolute convergence of these series,
bounded periodic primitives of f_m, and |K_m(x)|≤m/(8x²).
Let gamma be Euler's constant. Define the scalar

    C_m=T_m(1)-2 gamma a_m-S_m.

Take a fixed integer K≥2 and complex coefficients c_2,...,c_K, and put

    u=sum_(m=2)^K c_m rho_m,    K_u=sum_(m=2)^K c_m K_m,
    A(u)=sum c_m a_m,          B(u)=sum c_m T_m(1).

Assume A(u)=B(u)=0, and use L729's absolutely convergent functional
Q(u)=-sum_(n≥1)Lambda(n)conj(K_u(n)). No RH, zero simplicity, density
in the whole step-function space, or asymptotic uniform in u is assumed.

## Conclusion

For y>1 define the real-valued function

    q(y)=log(2pi)-{y}+(1/2)log(1-y^(-2)).

Then q∈H, and

    C_m=⟨q,rho_m⟩  for every fixed integer m≥2,
    Q(u)=⟨q,u⟩    for every fixed finite neutral complex u as above.

This reproduces the fixed-generator claim and its neutral specialization
in bramble_trace, *Fixed and growing neutral gradients of the anchored
Selberg–Möbius approximant*, [paper 18, displayed v3, 22 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/18),
fixed-probe theorem and “An elementary representer of the complete fixed
gradient,” (21)--(28), inspected 2026-11-03. The source is an unreviewed
manuscript. The replay below is warranted by the contour limits, pole
cancellations and complex pairing convention. It establishes no result
beyond that source. Here C_m is defined by the convergent arithmetic
expression; the manuscript's separate prime-discrepancy integral and
fixed-gradient asymptotic are not imported or audited.

## Proof

### Mellin transform and inversion

Fix m≥2, write a=a_m and ell=log m. L729 gives
K_m(1)=a-ell/m. Since f_m=a on (0,1), direct integration gives

    K_m(x)=a/x-ell/m,                    0<x<1.

Together with the bound at infinity this proves absolute convergence
of ∫₀^∞K_m(x)x^(s-1)dx when 1<Re(s)<2. K_m is locally absolutely
continuous on (0,∞), with K_m'=-f_m/x² almost everywhere. Integrating
by parts first on compact intervals and then taking endpoints gives

    Khat_m(s)=(1/s)∫₀^∞ f_m(x)x^(s-2)dx.                  (1)

Both boundary terms K_m(x)x^s vanish. The integral on the right is
ordinary improper at infinity: integration by parts with a bounded
primitive of f_m gives a convergent integral there for Re(s)<2. It
need not converge absolutely and is not used in an absolute Fubini step.

Set P_1(x)={x}-1/2. The standard centered fractional-part transform
is [DLMF 25.5.5](https://dlmf.nist.gov/25.5#E5), also Titchmarsh,
*The Theory of the Riemann Zeta-Function*, 2nd ed., (2.1.6), p. 15:
∫₀^∞P_1(x)x^(-z-1)dx=-zeta(z)/z for -1<Re(z)<0.
Here z=1-s is in that strip. Since f_m=P_1/m-P_1(·/m), substitution
in the two convergent improper integrals yields

    Khat_m(s)=zeta(1-s)(m^(s-1)-m^(-1))/(s(1-s)).          (2)

Fix 1<c<3/2. The reflected functional equation and the gamma
asymptotic give |zeta(1-c-it)|≪_c (1+|t|)^(c-1/2), since
zeta(c+it) is bounded by its absolutely convergent Dirichlet series.
Therefore

    |Khat_m(c+it)|≪_(m,c) (1+|t|)^(c-5/2),
    ∫_R |Khat_m(c+it)|dt<∞.                              (3)

The denominator has no zero on this line; bounded t is harmless.
K_m is continuous at every x>0, including integers. Thus the Mellin
inversion theorem [DLMF 1.14.35](https://dlmf.nist.gov/1.14#E35)
applies with absolute Mellin convergence and (3). Moreover

    sum_n Lambda(n)n^(-c) ∫_R |Khat_m(c+it)|dt<∞,

because 0≤Lambda(n)≤log n for n≥2. Inverting and summing is consequently
an absolute Fubini interchange. The standard Euler-product logarithmic
derivative, absolutely convergent for Re(s)>1, gives

    S_m=(1/(2pi i))∫_(c) I_m(s)ds,
    I_m(s)=-(zeta'/zeta)(s)
             zeta(1-s)(m^(s-1)-m^(-1))/(s(1-s)).          (4)

### Uniform horizontal bounds and cancellation

Use the functional equation

    zeta(s)=chi(s)zeta(1-s),
    chi(s)=2^s pi^(s-1) sin(pi s/2) Gamma(1-s).

These are [DLMF 25.4.1--2](https://dlmf.nist.gov/25.4).
Meromorphic continuation gives

    -(zeta'/zeta)(s)zeta(1-s)=-chi(1-s)zeta'(s).          (5)

At a zero of multiplicity r in the open critical strip, chi(1-s)
is analytic and nonzero, so the right side has order r-1≥0.
Thus there is no nontrivial-zero residue. More globally,
chi(1-s)=2^(1-s)pi^(-s)cos(pi s/2)Gamma(s) has possible poles only
at the nonpositive even integers; its gamma poles at negative odd
integers are canceled by the cosine. Zeta' has only the double pole
at 1. Along with the factors in (4), this accounts for all possible
poles: 1, 0, -2, -4,.... This argument needs no sequence of heights
avoiding zero ordinates, and no zero-free boundary-line assertion.

We justify the derivative estimate also at the adjoining strip edges.
Define the continuous, 1-Lipschitz exponent function

    p(sigma)=1/2-sigma     if sigma≤0,
             (1-sigma)/2 if 0≤sigma≤1,
             0           if sigma≥1.

For a fixed finite real strip and every delta>0, classical convexity
gives |zeta(sigma+it)|≪(1+|t|)^(p(sigma)+delta) uniformly there for
|t|≥2. The precise strip interpolation used here is Trudgian,
*A modest improvement on the function S(T)*,
[arXiv:1010.4596](https://arxiv.org/pdf/1010.4596), Section 4,
pp. 5--6, Lemma 1 and (8)--(9); the proof of Lemma 3 explicitly
removes the pole using (s-1)zeta(s). Only its polynomial interpolation
is used, not its subconvexity constants. Here is the applicability
and exponent calculation.

Choose 0<eta<min(1/2,delta). At Re(s)=1+eta the Dirichlet series
is bounded; at Re(s)=-eta the functional equation and Stirling give
O((1+|t|)^(1/2+eta)). Apply that interpolation to (s-1)zeta(s)
on [-eta,1+eta]; its two boundary exponents are 3/2+eta and 1,
so after division by s-1 the exponent is exactly
(1+eta-sigma)/2. On [0,1] this differs from p(sigma) by eta/2;
on [-eta,0] or [1,1+eta] it exceeds p(sigma) by at most eta/2.
Outside that strip, absolute convergence on the reflected right
side and the functional equation give the asserted p(sigma).

For completeness the interpolation's growth hypothesis is satisfied
without any zero estimate. Euler summation, followed by integration
by parts with the bounded primitive P(x)=∫₁^x P_1(v)dv, gives

    zeta(s)=1/(s-1)+1/2
             -s(s+1)∫₁^∞ P(x)x^(-s-2)dx,  Re(s)>-1.

Initially obtained for Re(s)>1 by summing floors, the integral
continues the identity and converges absolutely for Re(s)>-1.
It gives polynomial growth of (s-1)zeta(s) on [-eta,1+eta].
This is stronger than Lemma 1's double-exponential growth condition;
choose Q=2 in that lemma and any admissible positive k. The function
is analytic throughout the strip, and its left boundary exponent
is at least its right one. Hence all its hypotheses hold.

Now fix A≥3 and epsilon>0. Apply the just established bound with
delta=epsilon/2 on a slightly enlarged strip containing [-A,c].
Choose a fixed circle radius 0<r<min(1/4,epsilon/2). For |t|≥2 the
circle about sigma+it misses the pole at 1. Cauchy's derivative
estimate and |p(sigma')-p(sigma)|≤r give, uniformly on [-A,c],

    |zeta'(sigma+it)|≪_(A,c,epsilon)
                          |t|^(p(sigma)+epsilon).

Stirling's gamma bound, uniform on this fixed strip, gives
|chi(1-sigma-it)|≪_(A,c)|t|^(sigma-1/2). Thus

    |chi(1-s)zeta'(s)|≪
       |t|^epsilon                  if sigma≤0,
       |t|^(sigma/2+epsilon)        if 0≤sigma≤1,
       |t|^(sigma-1/2+epsilon)      if 1≤sigma≤c.         (6)

The same bound includes sigma=0,1; no invalid differentiation of
a boundary estimate has been used. The gamma input is Stirling's
formula with sector remainder and its vertical-line consequence,
[DLMF 5.11.9 and Section 5.11(ii)](https://dlmf.nist.gov/5.11).

On [-A,c], |m^(s-1)-m^(-1)|≤m^(c-1)+m^(-1), and at height
±T the denominator in (4) has modulus ≥T². Since c>1, all three
exponents in (6) are bounded above by c-1/2+epsilon. Choose
0<epsilon<3/2-c. Both horizontal integrals are consequently

    O_(A,c,m,epsilon)(T^(c-5/2+epsilon))→0,             (7)

and the exponent is strictly less than -1. The vertical integrals
on fixed lines not through a pole converge absolutely as well.

### Odd left boundaries and the ordered limits

Take an odd integer A≥3 and s=-A+it. Here zeta(1-s) and
(zeta'/zeta)(1-s) are bounded uniformly in A,t: their absolutely
convergent series are bounded already on Re(1-s)≥4. The functional
equation logarithmic derivative, evaluated on this line, is

    (zeta'/zeta)(s)=log(2pi)+(pi/2)cot(pi s/2)
                   -psi_Gamma(1-s)-(zeta'/zeta)(1-s).    (8)

There are no zeros or poles of zeta on the odd left line: this
also follows directly from its functional equation and the
nonvanishing Euler product on the reflected line. For odd A,
|cot(pi(-A+it)/2)|=|tanh(pi t/2)|≤1. On Re(1-s)≥4 the uniform
digamma estimate gives

    |psi_Gamma(1-s)|≤C log(A+|t|+2).

This is [DLMF 5.11.2 and its sector remainder](https://dlmf.nist.gov/5.11#E2):
1-s stays in |arg z|<pi/2, away from the excluded negative axis;
the bounded remaining range is compact. Also
|m^(s-1)-m^(-1)|≤2/m and |s(1-s)|≥A²+t². Therefore (4),(8) imply

    ∫_R |I_m(-A+it)|dt
      ≤(C/m)∫_R log(A+|t|+2)/(A²+t²)dt
      ≤C'(1+log A)/(m A)→0.                            (9)

For the second inequality substitute t=Av; the remaining integrals
of 1/(1+v²) and log(3+|v|)/(1+v²) are finite, uniformly for A≥3.
The residue theorem on the rectangle [-A,c]×[-T,T], oriented
counterclockwise, has its right edge traversed upwards. At each
fixed odd A, (7) permits T→∞, leaving the right integral minus
the upward left integral equal to the finite residue sum. Only
after that limit do we send odd A→∞ using (9). There is no joint
A,T limit or infinite sum over nontrivial zeros.

### Every residue and absolute summability

Write b=log(2pi). Standard values are zeta(0)=-1/2,
zeta'(0)=-b/2, and zeta(1+h)=1/h+gamma+O(h). References are
[DLMF 25.6.1](https://dlmf.nist.gov/25.6#E1),
[25.6.11](https://dlmf.nist.gov/25.6#E11), and
[25.2.4](https://dlmf.nist.gov/25.2#E4).

At s=1+h, expand the three factors in Khat_m:

    zeta(-h)=-1/2+bh/2+O(h²),
    m^h-m^(-1)=2a+ell h+O(h²),
    1/(s(1-s))=-1/h+1+O(h).

It follows that

    Khat_m(1+h)=a/h+ell/2-a(1+b)+O(h),
    -(zeta'/zeta)(1+h)=1/h-gamma+O(h).

The pole at 1 is double, with residue ell/2-a(1+b+gamma).
At s=0, zeta(1-s)=-1/s+gamma+O(s), while
m^(s-1)-m^(-1)=(ell/m)s+O(s²). Thus
Khat_m(s)=-ell/(m s)+O(1). Since -(zeta'/zeta)(0)=-b,
the residue at 0 is b ell/m. In particular the zero of the
m-factor does not remove the pole at 0.

For k≥1, the zero at -2k is simple: the sine in chi has a simple
zero and both Gamma(1+2k) and zeta(1+2k) are nonzero. Hence
the residue of -zeta'/zeta there is -1. Define, for Re(z)>0,

    R_m(z)=∫₁^∞rho_m(y)y^(-z-1)dy
          =(zeta(z)/z)(m^(-z)-m^(-1)).                 (10)

The floor integrals prove (10) first for Re(z)>1. Since rho_m
is bounded, its left side is analytic for Re(z)>0; the numerator
on the right cancels the apparent pole at z=1. Analytic continuation
proves the full stated domain. Substitution at -2k into (4) gives

    Res_(s=-2k) I_m(s)
      =zeta(1+2k)(m^(-1-2k)-m^(-1))/(2k(1+2k))
      =R_m(1+2k)/(2k).                                (11)

These residues are negative and their absolute values are at most
zeta(3)/(m(2k)(1+2k)), a summable bound. There are no other poles
by (5). The ordered contour limits therefore prove

    S_m=ell/2-a(1+b+gamma)+b ell/m
                +sum_(k≥1)R_m(1+2k)/(2k).              (12)

This also checks the orientation and sign of the trivial-zero sum.

### The conditional endpoint and the H pairing

L730 proves, by finite cell sums and Stirling rather than a contour,
the fixed-m identities

    ∫₁^∞ f_m(y)dy/y=ell/2-a b,
    T_m(1)=ell/2-a(1+b-gamma)-h_m,
    h_m=∫₁^∞{y}rho_m(y)dy/y².                          (13)

The first integral is only an ordinary improper integral. Its
convergence follows from the bounded primitive. The second uses
the finite summation endpoint with Y K_m(Y)→0 and the absolutely
convergent fractional-part integral. These precise endpoint facts
from L730 are reused; its density conclusion is not needed here.

Substituting (12),(13) into the definition of C_m cancels all
a-terms, including both gamma contributions, and gives

    C_m=-h_m-b ell/m-sum_(k≥1)R_m(1+2k)/(2k).            (14)

L729 proves ⟨1,rho_m⟩=-ell/m. To identify the remaining series,
use |rho_m|≤1 and, for y>1,

    sum_(k≥1)y^(-2k)/(2k)=-(1/2)log(1-y^(-2)).

Its integral against dy/y² is finite by Tonelli, since it equals
sum_(k≥1)1/(2k(2k+1)). Thus the logarithmic series may be integrated
term by term against rho_m, with an absolute majorant. It yields

    ⟨(1/2)log(1-y^(-2)),rho_m⟩
          =-sum_(k≥1)R_m(1+2k)/(2k).

Combining this with (14) proves C_m=⟨q,rho_m⟩.

We check q∈H separately, since the preceding L1 majorant is not
an L2 proof. For 1<y≤2,

    log(1-y^(-2))=log(y-1)+log((y+1)/y²),

and the second term is bounded. Consequently
|q(y)|²≤C(1+|log(y-1)|²), integrable at 1. For y≥2,
|log(1-y^(-2))|≤(4/3)y^(-2), and {y} is bounded. Hence q is
bounded there and ∫₂^∞|q|²dy/y²<∞. This proves q∈H.

Finally all coefficient sums below are finite. Because the inner
product is linear in the first entry and rho_m is real,

    ⟨q,u⟩=sum_m conj(c_m)C_m
          =conj(B(u))-2 gamma conj(A(u))-sum_m conj(c_m)S_m
          =-sum_(n≥1)Lambda(n)conj(K_u(n))=Q(u).

The last series rearrangement is absolute by L729, and the two
constraints remove exactly the displayed conjugated terms. This
proves the claimed identity for all finite neutral complex vectors. ∎

The audited result supplies an H-representer for the neutral arithmetic
functional. It does not identify q with the original prime discrepancy
as a function, assert q lies in the closed arithmetic span, prove a
projection saturation claim, enlarge the K^(5/2)/N range of L729,
or control the full or complementary approximation error. No RH
candidate or new Xi positivity statement is obtained.

## Mathlib

Full matching representer theorem: not checked; availability is unknown.
Supporting inversion is
[`mellinInv_mellin_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/MellinInversion.html#mellinInv_mellin_eq),
whose MellinConvergent, VerticalIntegrable and ContinuousAt hypotheses
were inspected in the completed step-235 coverage. They correspond
to (1)--(3) and continuity above. This supports only inversion, not
the strip estimates, residues, endpoint calculation or the full result.
Other exact Mathlib declarations were not checked in this step; no
absence claim is made.
