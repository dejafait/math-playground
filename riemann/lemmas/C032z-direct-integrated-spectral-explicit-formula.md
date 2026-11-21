# Corollary C032z: direct integrated spectral explicit formula

## Hypotheses

Use C032y's exact pair e_(sigma,a)(w), equations(3)/(8), and its
identity E_sigma(w)=sum_(rho in Z+) e_(sigma,a_rho)(w). The actual
positive-ordinate divisor has multiplicity, a_rho=(rho-1/2)/i,
|Im(a_rho)|<1/2, and no ordinate-zero members. Retain C032m/y's
strip, counting and zero-ordinate qualifications. No RH, individual
zero coordinates, heat positivity or real-valued test hypothesis is
imposed. Probability applications still require their additional
finite-zero, heat and fixed-v1 source qualifications, not audited here.
Throughout sigma is real in[1,2] and w is complex with |w|<=2.
All primitive paths are straight segments.

Import the unconditional explicit formula in Andres Chirre and Felipe
Goncalves, *Bounding the log-derivative of the zeta-function*, Math. Z.
300(2022), 1041-1053, Proposition5, printed p.1044,
[publisher PDF](https://link.springer.com/content/pdf/10.1007/s00209-021-02820-9.pdf).
For even h analytic on a neighborhood of the closed strip
|Im(a)|<=1/2+epsilon, epsilon>0, and decaying there as
O((1+|a|)^(-1-delta)), delta>0, its convention and formula are

    hat(h)(y)=integral_R h(r)*exp(-2*pi*i*r*y) dr,
    sum_(all nontrivial rho) h((rho-1/2)/i)
      =2*h(i/2)-log(pi)*hat(h)(0)/(2*pi)
       +integral_R h(r)*Re psi(1/4+i*r/2) dr/(2*pi)
       -sum_(n>=2) Lambda(n)*hat(h)(log(n)/(2*pi))/(pi*sqrt(n)). (1)

This proposition, rather than its neighboring RH-dependent lemma, is
the input. Its statement permits complex-valued h; do not silently
replace it by the upstream real-valued-test statement. Source coverage
is in notes1582/1572/1555. No reproof of(1) is intended.

## Conclusion

For v>=0 define

    q(v)=exp(-sigma*v^2)*(cosh(w*v)-1)/v (v>0), q(0)=0,
    C=8+704*exp(121/32).

The test h(a)=e_(sigma,a)(w) is even and entire in a and satisfies

    h(a)=-2*integral_0^infinity q(v)*cos(a*v) dv,             (2)
    |h(x+i*y)|<=C/(1+x^2), |y|<=3/4.                       (3)

Its ordinary, absolutely defined Fourier transform is

    hat(h)(y)=-exp(-4*pi^2*sigma*y^2)
                    *(cosh(2*pi*w*|y|)-1)/|y|, y!=0,
    hat(h)(0)=0.                                          (4)

The actual full-divisor positive-ordinate sum consequently equals

    E_sigma(w)=h(i/2)
      +integral_R h(r)*Re psi(1/4+i*r/2) dr/(4*pi)
      +sum_(n>=2) [Lambda(n)/(sqrt(n)*log(n))]
               *exp(-sigma*(log(n))^2)*(cosh(w*log(n))-1).  (5)

The pole value, with no singular or principal-value interpretation, is

    h(i/2)=h(-i/2)
      =-2*integral_0^infinity exp(-sigma*v^2)
             *(cosh(w*v)-1)*cosh(v/2)/v dv.                (6)

All prime powers occur in(5); trivial zeros are already accounted for
by the gamma term. For integer N>=4 the omitted terms n>N have total
absolute value at most

    T_P(N)=exp(-(log(N))^2+(5/2)*log(N))/(log(N)-5/4).       (7)

For real R>=1 the error on restricting the gamma integral in(5)
to[-R,R] is at most

    T_G(R)=C*[12+log(1+R)]/(2*pi*R).                        (8)

Both errors tend to zero uniformly on the closed parameter set.
Replacing psi on[-R,R] by its series through k=K-1 in(15) below,
K>=1, adds error at most

    T_psi(R,K)=C*sqrt(9/16+R^2/4)/(4*K).                    (9)

These are analytic identities and coarse effective errors. No finite
quadrature, implemented evaluator, feasible cost, O_sigma enclosure,
residual below1/2 or cone certificate is supplied. Full odd cancellation,
arbitrary variation exclusion, unsmoothed Xi realization and actual-Xi
all-degree positivity remain open. This is specialization/reproduction
of known tools under assessment1582, not a discovery beyond the sources
checked. Critical audit1585 below validates (2)-(9) under these exact
hypotheses; it supplies neither numerical evaluation nor a certificate.

## Proof

### 1. Exact representation and compact exchanges

Use NIST DLMF version1.2.8 (15 September2026),
[7.7.3](https://dlmf.nist.gov/7.7.E3), at its parameter A=1 and
opposite complex arguments z,-z. Subtract the identities and use
oddness of Dawson's F to obtain

    F(z)=integral_0^infinity exp(-u^2)*sin(2*z*u) du.

Subtraction, rather than taking an imaginary part, is valid for complex
z. DLMF [7.5.1](https://dlmf.nist.gov/7.5.E1) gives
D_F(z)=2*i*F(z)/sqrt(pi), in C032y's notation. Its B(t) is therefore

    B(t)=-4/sqrt(pi)*integral_0^infinity exp(-u^2)
                    *sinh(t*u/sqrt(sigma))*cos(a*u/sqrt(sigma)) du.

Substitute u=sqrt(sigma)*v into C032y's primitive
h(a)=sqrt(pi)/(2*sqrt(sigma))*integral_0^w B(t)dt.
Integrating sinh(t*v) over the straight path gives
(cosh(w*v)-1)/v, continuously0 at v=0, proving(2).

These operations precede any infinite-divisor exchange. On compact
a,w sets, all trigonometric factors are bounded by constants times
exp(M*v). At the origin q(v)=w^2*v/2+O(v^3). At infinity a Gaussian
exp(-v^2+M*v) times a fixed polynomial dominates, including the
compact t path and every fixed-order derivative in a. Fubini thus
applies to absolute integrals. Compact holomorphic integration
(Haslinger, *Complex Analysis*, Theorem2.39, pp.67-68,
[primary PDF](https://www.mat.univie.ac.at/~has/scriptneu.pdf), as
covered in C032m) proves entireness in a. Evenness follows from cos.
The same compact domination applies locally to w and throughout the
closed width interval. No nonintegrable Fourier terms are separated.

### 2. Common inverse-square strip bound

Taylor's integral remainder, also for complex arguments, gives

    q(v)=w^2*v*exp(-sigma*v^2)*L(v),
    L(v)=integral_0^1 (1-t)*cosh(t*w*v)dt.

For j=0,1,2 and v>=0,
|L^(j)(v)|<=(2^j/2)*exp(2*v): differentiate the compact t integral
and use |sinh z|,|cosh z|<=exp(|z|), |w|<=2 and
integral_0^1(1-t)dt=1/2. For A(v)=v*exp(-sigma*v^2),

    A'=(1-2*sigma*v^2)*exp(-sigma*v^2),
    A''=(-6*sigma*v+4*sigma^2*v^3)*exp(-sigma*v^2).

It follows, including continuous derivatives at0, that

    |q(v)|<=2*v*exp(-v^2+2*v), q'(0)=w^2/2,
    |q''(v)|<=(8+32*v+32*v^2+32*v^3)*exp(-v^2+2*v).       (10)

Indeed A''L contributes at most6*v+8*v^3 before multiplication by
|w|^2<=4; 2*A'*L' contributes2+8*v^2 and A*L'' contributes2*v.
These give exactly(10). The same formulas bound q' by a polynomial
times exp(-v^2+2*v). All boundary terms at infinity therefore vanish
after multiplication by sin(a*v) or cos(a*v), uniformly on the strip.

For |Im(a)|<=3/4, use
-v^2+(11/4)*v<=-v^2/2+121/32 and the elementary integrals

    integral_0^infinity exp(-v^2/2)dv=sqrt(pi/2)<2,
    integral_0^infinity v*exp(-v^2/2)dv=1,
    integral_0^infinity v^2*exp(-v^2/2)dv=sqrt(pi/2)<2,
    integral_0^infinity v^3*exp(-v^2/2)dv=2.

They imply

    |h(a)|<=4*exp(121/32),
    integral_0^infinity |q''(v)|*exp(3*v/4)dv
                       <=176*exp(121/32).                (11)

For a!=0 integrate(2) by parts twice on[0,L], then let L tend to
infinity. Bound(10) justifies both limits. The first origin term
is q(0)*sin(0)=0; the second is q'(0)*cos(0). The signs give

    h(a)=2/a^2*[q'(0)+integral_0^infinity q''(v)*cos(a*v)dv]. (12)

Thus |h(a)|<=[4+352*exp(121/32)]/|a|^2. For |x|>=1 use
|a|>=|x| and(1+x^2)/x^2<=2; for |x|<=1 use the first bound
in(11) and1+x^2<=2. This proves(3) with the displayed C, without
division by a at a=0. Since (1+|a|)^2/(1+x^2) is bounded on the
strip, (3) gives the decay hypothesis in(1) with delta=1 and
epsilon=1/4. Analyticity on a neighborhood follows from entireness.

### 3. Ordinary Fourier identification, including zero

Set H(y)=-2*pi*q(2*pi*|y|), including H(0)=0. Bound(10) makes H
absolutely integrable and continuous on R. Its derivative on each
side of0 has finite one-sided limits there; it is Lipschitz and
of bounded variation on every compact interval. Its even inverse
integral, on substituting v=2*pi*y, is

    integral_R H(y)*exp(2*pi*i*a*y)dy=h(a), a real.         (13)

This single integral is absolutely convergent. Apply DLMF
[1.14.1-3](https://dlmf.nist.gov/1.14), with its positive exponential
and1/sqrt(2*pi) convention, to H. Its normalized transform at u is
h(u/(2*pi))/sqrt(2*pi). The inversion statement, with u=2*pi*a,
therefore gives

    H(y)=lim_(L->infinity) integral_(-L)^L
                                 h(a)*exp(-2*pi*i*a*y) da.

The average of one-sided values equals H(y) by continuity. Bound(3)
makes this inverse integral absolutely convergent, so its
principal-value limit equals the ordinary integral. Substitution
gives(4) for both signs; H(0)=0 proves the zero-frequency value.
In particular integral_R h(r)dr=0. No uncontrolled double Fourier
integral or formal delta function is used.

### 4. Explicit formula, divisor normalization and prime tails

Apply(1) using the hypotheses established above. The map rho->1-rho
sends a_rho to -a_rho and pairs the positive and negative ordinate
divisors with multiplicity. With the retained exclusion of ordinate
zero, the all-zero sum is exactly twice C032y's positive-ordinate
sum. Its absolute convergence follows from(3) and the retained
counting bound, or from C032y's sum identity. Off-line members at
one positive ordinate remain separate; no extra division is applied.

Divide(1) by2. At y=log(n)/(2*pi)>0, (4) gives

    hat(h)(y)=-2*pi*exp(-sigma*(log(n))^2)
                                  *(cosh(w*log(n))-1)/log(n).

This proves the plus sign and all factors in(5). The two pole values
are equal; after division by2 their contribution is h(i/2), namely
(6). Its integrand is O(v) at0 and is dominated at infinity by a
polynomial times exp(-v^2+(5/2)*v), uniformly in sigma,w.
At w=0 all displayed terms vanish. The -log(pi) term vanishes by
hat(h)(0)=0 only after integrability has been established. The gamma
term accounts for trivial zeros, so no additional series is inserted.

For all n>=2, 0<=Lambda(n)/log(n)<=1, including prime powers,
where this ratio is1/k. Also |cosh(w*log(n))-1|<=2*n^2.
The absolute n-th prime contribution in(5) is at most
2*n^(3/2)*exp(-(log(n))^2). The function
f(x)=x^(3/2)*exp(-(log(x))^2) decreases for log(x)>=3/4.
For integer N>=4,

    sum_(n>N) 2*f(n)
      <=2*integral_N^infinity f(x)dx
      =2*integral_(log(N))^infinity exp(-u^2+(5/2)*u)du.

Complete the square and put b=log(N)-5/4>0. Replacing1 by t/b
under the positive integral gives
integral_b^infinity exp(-t^2)dt<=exp(-b^2)/(2*b).
This proves(7), tending uniformly to0. The estimate uses every
integer and never omits prime powers; no critical-line Dirichlet
series is expanded.

### 5. Gamma-integral and digamma-series errors

Put m(r)=Re psi(1/4+i*r/2). DLMF version1.2.8,
[5.7.6](https://dlmf.nist.gov/5.7.E6), gives

    psi(z)=-gamma_E+sum_(k>=0)[1/(k+1)-1/(k+z)],           (15)

for z outside the nonpositive integers. In particular it applies
at every z=1/4+i*r/2. Set a=1/4 and b=r/2. At b=0,

    |psi(a)|<=1+3+(3/4)*sum_(k>=1)1/[k*(k+1)]<5.

Here0<gamma_E<1, the k=0 reciprocal difference is3, and the
remaining difference is (3/4)/[(k+1/4)*(k+1)].
Take real parts in the convergent difference of(15) at a+i*b,a:

    m(r)=psi(a)+sum_(k>=0)
                    b^2/[(k+a)*((k+a)^2+b^2)].           (16)

For J=ceil(max(1,|b|)), the k=0 term is at most4; the terms
1<=k<=J sum to at most1+log(J). Terms k>J sum to at most
b^2*sum_(k>J)k^(-3)<=b^2/(2*J^2)<=1/2. Since J<=1+|b|,

    |m(r)|<=11+log(1+|r|).                                (17)

Every difference above converges absolutely; divergent reciprocal
sums have never been separated. Bounds(3)/(17) prove absolute
convergence of the gamma integral in(5). Both omitted spatial tails,
including the factor1/(4*pi), contribute at most

    C/(2*pi)*integral_R^infinity [11+log(1+r)]/r^2 dr
      =C/(2*pi)*{[11+log(1+R)]/R+log(1+1/R)}
      <=T_G(R).

This proves(8). For k>=K>=1 and Re(z)=1/4, the series remainder
has individual terms bounded by

    |1/(k+1)-1/(k+z)|
      =|z-1|/[(k+1)*|k+z|]<=|z-1|/[k*(k+1)].

Their sum is at most |z-1|/K. On |r|<=R this is at most
sqrt(9/16+R^2/4)/K. Multiplying by |h(r)|/(4*pi), integrating,
and using integral_R 1/(1+r^2)dr=pi proves(9).
For fixed R it tends to0 as K increases. For simultaneous limits,
one can take K>=R^2 and let R tend to infinity. Together with(7)/(8)
this gives explicitly vanishing uniform analytic truncation errors,
not a certified finite arithmetic or quadrature implementation.

### Critical audit1585 — 18 November2026

The full statement (2)-(9) passes a separate conceptual audit under
the prior SPECIALIZE assessment1583, approved in1584. No mathematical
correction is needed. This is local verification of the analytic input,
not mathematics beyond the cited sources, a finite evaluator or a
verification of the inherited source data. The following checks retain
complex w, both width endpoints, all multiplicities and the exclusion
of ordinate zero. Primary theorem coverage1582/1572/1555 and C032m's
Haslinger2.39 coverage were reused, without reproving the inputs.

**Pair normalization and entire parameters.** For k=2*sqrt(sigma),
the two Dawson integrands in C032y's B add as

    sin((i*t-a)*u/sqrt(sigma))
      +sin((i*t+a)*u/sqrt(sigma))
      =2*i*sinh(t*u/sqrt(sigma))*cos(a*u/sqrt(sigma)).

Multiplication by 2*i/sqrt(pi) gives exactly -4/sqrt(pi).
The substitution u=sqrt(sigma)*v then cancels the sqrt(sigma)
in the primitive prefactor, leaving -2 in (2). This is valid for
complex parameters: no imaginary-part operation is used. The compact
Gaussian dominator controls the entire straight path t=s*w and all
fixed a derivatives. At v=0, q=w^2*v/2+O(v^3) uniformly on the
closed parameter set. Thus the lower endpoint and w=0 are covered,
and Haslinger2.39 applies to absolutely integrable sections on every
compact a disk. Neither the zero sum nor a spectral integral is
exchanged in this calculation.

**Strip constants and boundary terms.** The three differentiated
product bounds in q'' give, before the factor |w|^2<=4,
(6*v+8*v^3)+(2+8*v^2)+2*v. Hence (10)'s bounding polynomial is
8+32*v+32*v^2+32*v^3. After the exponential absorption, its integral
is bounded by (16+32+64+64)*exp(121/32), which is the176 in (11).
The small-a estimate has factor4 from -2*q and integral v*exp(-v^2/2)=1.
For I=integral q*cos(a*v), the two integrations by parts give

    I=-a^(-1)*integral q'*sin(a*v)
     =-a^(-2)*[q'(0)+integral q''*cos(a*v)].

The origin contribution has the indicated plus sign inside the
brackets; all infinity terms vanish uniformly in the wider strip.
Since |q'(0)|<=2, multiplication by -2 gives (12) and the coefficient
4+352*exp(121/32). Doubling this for |Re(a)|>=1 yields precisely C.
For |Re(a)|<=1, including a=0, the undivided bound gives8*exp(121/32)
after multiplication by1+Re(a)^2, which is smaller than C. Thus the
closed strip has uniform inverse-square decay. Entireness supplies
the required neighborhood of that strip, so Proposition5 applies
with epsilon=1/4 and delta=1.

**Ordinary Fourier inversion at the cusp.** H(y)=-2*pi*q(2*pi*|y|)
is continuous, absolutely integrable, and has locally bounded
variation, including at zero. Indeed its two one-sided derivatives
there are finite and its derivative elsewhere has a Gaussian
integrable bound. The cusp is permitted by the imported inversion
theorem. In its positive-exponential normalization, the transform of
H at u is h(u/(2*pi))/sqrt(2*pi). Inversion and u=2*pi*a therefore
cancel both normalization factors and give exactly the ordinary
negative-exponential transform of h. Bound (3) makes its integral
absolutely convergent. The average at zero is H(0)=0, not an
uncomputed distributional term. Substituting q into H proves every
factor in (4), and integral h=0 is obtained only after inversion.

**Actual divisor and explicit-formula terms.** The functional-equation
map rho->1-rho preserves multiplicity and sends a_rho to -a_rho.
With no ordinate-zero members, it is a bijection from positive to
negative ordinates. Bound (3) and N(T)=O(T*log(T+2)) give absolute
summability, so pairing is legitimate. Distinct off-line members of
Z+ remain distinct. Evenness makes the all-zero sum exactly2*E,
and the two pole evaluations become h(i/2) after this division.
At y=log(n)/(2*pi), the transformed test is -2*pi times the
Gaussian/cosh factor divided by log(n); multiplication by the prime
coefficient -Lambda(n)/(2*pi*sqrt(n)) after division by2 gives exactly the
positive term in (5). The log(pi) term vanishes by the already proved
zero-frequency identity. No extra trivial-zero term is allowed.
The pole integral in (6) is ordinary: its origin is O(v), and the
uniform Gaussian bound at infinity includes cosh(v/2).

**All three error bounds.** For the prime tail, the envelope
2*n^(3/2)*exp(-(log(n))^2) includes every prime power, since
Lambda(n)/log(n)=1/k on n=p^k. The function f decreases already for
log(x)>=3/4, and N>=4 also ensures log(N)-5/4>0. Thus the integral
comparison and Gaussian tail inequality prove (7), including its
factor2 and denominator. No prime-density assertion is used.

In (15), |psi(1/4)| is bounded by1+3+3/4<5. The real-part
difference (16) is nonnegative termwise and absolutely convergent.
Its k=0 part is at most4; the next J terms total at most1+log(J);
the remaining terms total at most b^2/(2*J^2)<=1/2. This yields
10.5+log(1+|b|)<=11+log(1+|r|), so (17) is sufficient without
any hidden asymptotic constant. The two spatial tails and factor
1/(4*pi) give C/(2*pi), and the integration by parts leaves
log(1+1/R)<=1/R. This verifies exactly (8).

For (9), sum_(k>=K)1/[k*(k+1)]=1/K, valid for every integer K>=1.
The modulus of z-1 is sqrt(9/16+r^2/4). Taking real parts cannot
increase the error; integrating the bound against |h|/(4*pi)
and extending the remaining positive integral to all real r gives
C*sqrt(9/16+R^2/4)/(4*K). No rounding, approximation to gamma_E,
quadrature, or approximation to h is included in that allowance.
Choosing integers K>=R^2 makes it vanish as R increases; the prime
and gamma tails vanish independently. All statements are uniform
on sigma in[1,2], |w|<=2, including the boundary and w=0.

The bounded analytic audit is complete. Practical evaluation must
still pay finite special-function/integral arithmetic, quadrature,
the O enclosure and coefficient amplification. Stops1571/1576/1581
keep their original enclosure, expanding-disk and finite-coordinate
scopes; this audit neither repeats nor removes them. The direct test
is a materially different available analytic input for a subsequent
cost preflight, not proof that the prescribed residual is attainable.
No all-order cancellation, unrestricted variation exclusion, positive
output, unsmoothed realization or RH conclusion follows.

### Literal series cost preflight1586

On 18 November2026 the approved dictionary1570 calculation tested the
literal common uniform bounds (8)-(9) before numerical sampling. Retain
all hypotheses above, R>=1, integer K>=1, and the exact constant C.
Let A=T_G(R), B=T_psi(R,K). Suppose a proposed total uniform E-error
allowance includes A+B plus other nonnegative errors. For 0<epsilon<=1,
making that allowance strictly below epsilon necessarily requires

    R>45000/epsilon,
    K>1181250000/epsilon^2.                              (18)

These are necessary conditions for these displayed *allowances*, not
lower bounds on actual numerical errors or on any dictionary residual.
In particular the benchmark epsilon=1 is not asserted necessary for
a successful coefficient-weighted certificate.

Here is the complete arithmetic proof. Positivity of the exponential
Taylor coefficients gives

    C>8+704*sum_(j=0)^24 (121/32)^j/j! >30000.

The last strict comparison is an exact rational inequality, reproduced
in `scripts/smoothed-law/integrated_spectral_cost_1586.py` and saved in
its `.json` certificate; it uses no floating-point exponential value.
Since pi<4 and log(1+R)>=0, (8) gives A>3*C/(2*R)>45000/R.
Thus A+B<epsilon<=1 implies R>45000/epsilon>=45000. The elementary
bound e<3 gives e^9<3^9=19683<45000<1+R, hence log(1+R)>9.
Return to (8)-(9), retaining this improved numerator:

    A>21*C/(8*R),       B>=C*R/(8*K).

The second estimate follows from sqrt(9/16+R^2/4)>=R/2.
Because (A-B)^2>=0,

    (A+B)^2>=4*A*B>21*C^2/(16*K)>1181250000/K.

Together with A+B<epsilon this proves (18), for every allowed R,K;
no numerical minimization of the cutoffs is involved. In particular
epsilon=1 requires at least1181250001 terms in the literal digamma
partial sum, and epsilon=1/8 requires at least75600000001 terms.
This counts one common-bound partial sum, not repeated work across
widths or w: digamma evaluations can be cached and reused. Grouping,
asymptotic/recurrence evaluation, or bounding the integrated remainder
more sharply can avoid this particular literal implementation and
are not excluded by (18).

The bounded calculation imposed a ceiling of10000000 explicitly
enumerated digamma summands and stopped before quadrature or a solve.
Indeed, if R<=45000, A>45000/R>=1; if R>45000 and K<=10000000,
the displayed square bound is greater than118.125>100. Thus no R
within this literal procedure pays even the unit E-error benchmark
under that finite-work ceiling. The pole integral, h quadrature,
prime tail, numerical constants, O enclosure and coefficient
amplification would add obligations; none repairs this cost bound.
C032w's compact profile/O interface remains available analytically,
but was not run after this earlier E preflight failed. Its old
expanding-disk cost stop is not being reapplied to direct E.

Only the retained exact candidate q=0 is certified: all16 real odd
components and four nonnegative Laplace coefficients are zero, so
the residual is exactly1 on the entire closed width interval[1,2].
It uses one closed cell, no kernel arithmetic and zero propagated
rounding/tail error. No grid solve, nonzero candidate or lower bound
on the actual dictionary residual is supplied. For a nonzero q, all
kernel errors must still be propagated through exp/sinh and weighted
by the actual coefficient magnitudes; no coefficient lower bound or
unavoidable unit E accuracy is asserted here.

The interpretation of the requested threshold keeps its sign: for
an admissible eta, C032q makes integral q deta>=0, while eta(W)=1
gives integral(1+q)deta>=1. Its norm pairing bounds the latter by
|eta|(W)*||1+q||_infinity. A strict residual below1/2 would therefore
contradict |eta|(W)<=2. Residual1 supplies no contradiction. This is
only the existing cone interface applied to the test, not an exclusion
of arbitrary variation, a witness, or actual-Xi all-degree positivity.

Stop this literal error scheme inconclusively for dictionary1570.
This is a new evaluator-specific cost obstruction using known input
bounds and elementary arithmetic, not a mathematical discovery beyond
those sources, an obstruction to sharper methods, or an RH candidate.
Original stops1571/1576/1581 retain their distinct scopes. The full
certificate records every zero coefficient, exact comparisons, failed
obligations and work limits. Reproduce with
`python3 scripts/smoothed-law/integrated_spectral_cost_1586.py`.

### Independent cost audit1606

18 November2026. Under unchanged assessment1604, separately approved1605,
audit preflight1586 only for epsilon in{1,1/8}, retaining (8)-(9),
R>=1, integer K>=1, sigma in[1,2], |w|<=2 and the hypotheses above.
The complete restricted claim passes without repair. This verifies
the existing implementation stop, rather than adding a new result
beyond the assessed sources or resolving a dictionary constraint.

For an independent rational check set d=32^24*24! and
n=sum_(j=0)^24 121^j*32^(24-j)*(24!/j!). Then the Taylor lower
bound is (8*d+704*n)/d, agreeing exactly with certificate1586.
After reduction its excess over30000 is

    95110405479058826446089740115623260225786908369993005237603
    /106497596271155498924797840283600582127814121556541440000 >0.

The omitted exponential terms are strictly positive, so C>30000.
The elementary constants require no uninspected theorem: pi<4 follows
from pi/4=integral_0^1(1+x^2)^(-1)dx<1. Also
e=2+sum_(j>=2)1/j!<2+sum_(j>=2)2^(-(j-1))=3; factorial
comparison is strict from j=3 onward. These are only constant checks,
not a reproof of the cited explicit formula or digamma identity.

For every allowed R, the numerator12+log(1+R) is at least12 and
1/(2*pi)>1/8. Thus A>3*C/(2*R)>45000/R. Since B>0,
A+B<epsilon implies R>45000/epsilon. For epsilon<=1 this is
strictly greater than45000; 3^9=19683<45000<1+R proves
log(1+R)>9. Hence A>21*C/(8*R). Positivity of R,K,C and
sqrt(9/16+R^2/4)>=R/2 give B>=C*R/(8*K). Multiplication
is legitimate with these signs, and (A-B)^2>=0 gives

    (A+B)^2>=4*A*B>21*C^2/(16*K)>1181250000/K.

Comparing with epsilon^2 yields the strict thresholds in(18).
For epsilon=1 they are R>45000,K>1181250000; for epsilon=1/8
they are R>360000,K>75600000000. Integer K therefore is at least
1181250001 or75600000001 respectively. These are necessary counts,
not sufficient choices attaining the tolerance.

The work-ceiling argument does not assume the tolerance first.
If1<=R<=45000 then A>45000/R>=1, including R=45000. If R>45000,
the same logarithmic improvement holds without a tolerance assumption;
for K<=10000000 it gives (A+B)^2>1181250000/K>=945/8>100.
Because A+B>0 it follows that A+B>10. These two cases cover all
R>=1 and exclude A+B<1, hence also A+B<1/8, at that ceiling.
Caching psi across widths and w does not reduce K for the single
literal partial sum; no cost multiplier for repeated evaluations is
used. Grouped, asymptotic, recurrence or sharper integrated evaluation
remains outside this cost claim.

The independent integer-common-denominator replay is
`python3 scripts/smoothed-law/integrated_series_cost_audit_1606.py`.
Its `.json` contains17 passing checks and no failures; the complete
load-bearing rational values were inspected. The original1586 script
and certificate are preserved. The replay checks arithmetic; the
analytic implications and endpoint split are justified above.

The allowance hypothesis is essential: actual errors can be smaller,
and coefficient-weighted residual propagation need not require unit
primitive accuracy. No actual-error lower bound, nonzero q, residual
obstruction, cone infeasibility or RH candidate follows. C032m/y/z's
divisor, multiplicity, zero-ordinate and strip/counting hypotheses,
and the interpretation-specific finite-zero, heat and fixed-v1
qualifications, have not been discharged by this cost audit.

## Mathlib

Full matching coverage of this integrated test, its explicit-formula
specialization and effective constants is unchecked/unknown.
No Mathlib theorem is used. The external inputs cited above supply
the general transform, inversion, holomorphic integration, explicit
formula and digamma series; only their specialization is proved here.
No assertion of absence from Mathlib is made.
The exact-arithmetic cost consequence (18) has no separately checked
Mathlib coverage; the script is a reproducible rational check, not a
formal proof assistant verification.

