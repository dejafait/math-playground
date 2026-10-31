# Lemma 504: clipped strip-Poisson dual residual obstruction

## Hypotheses

Fix R>0. For sufficiently large real T put

    L=log T, a=log L/pi, b=a/4, B=L/(4pi),
    lambda=pi/(2a), beta=lambda*b=pi/8,
    K(x)=1-(sin(pi x)/(pi x))^2, K(0)=0.

Let V_R be the real vector space of even entire functions, real on R,
of the form

    f(z)=integral phi(v)exp(2pi i v z)dv,
    phi in C_c^infinity(R), supp phi subset [-R,R].

Write u(x,y)=Re f(x+iy), N(f)=integral_R |f(x)|dx and
M(f)=integral_R |f(x)|K(x)dx. Define the linear functional

    Q_a(f)=-integral_0^b exp(-lambda y)[u(a,y)+u(-a,y)]dy.

The subset H_a of interest additionally satisfies

    u(x,y)>=1 for |x|<=a and b<|y|<B.                 (H)

No sign restriction is imposed on V_R itself. There is no uniform
Fourier-derivative bound. Introduce, for 0<=y<b,

    p_b(t,y)=(1/(2b)) Re sech(pi(t+iy)/(2b)),
    w_b(t)=integral_0^b exp(-lambda y)p_b(t,y)dy,
    W_a(x)=w_b(x-a)+w_b(x+a).

The nonnegative integrable density w_b is defined almost everywhere;
its possible infinite value at t=0 is immaterial. Define a finite
positive measure mu_a on the horizontal segment y=b, |x|<=a by
dmu_a=W_a(x)dx, and set

    E_a(f)=Q_a(f)+integral_{-a}^a W_a(x)u(x,b)dx.      (1)

The standard inputs are Fourier inversion for Schwartz functions and
Cauchy's residue theorem. The strip Poisson kernel is classical. Its
short transform calculation is included to fix the normalization and
justify this particular clipped measure, not as a new kernel theorem.
No conclusion of L503 is a mathematical input; only its target and
geometry motivate these definitions.

For the supplementary slow-dilation calculation only, take T>exp(1)
and an even entire envelope e, real on R, with e(0)=1 and representation
e(z)=integral psi(v)exp(2pi i v z)dv, where psi is globally C_c^infinity
and supported in [-R,R]. Let p be any even real polynomial of finite
degree and f(z)=p(z)e(z/D), D>=max(1,B). There are no uniform bounds on
the degree, coefficients or derivatives of psi. The source construction
is I. Chremmos and G. Fikioris, *Superoscillations with arbitrary
polynomial shape*, [arXiv:1504.04822v1](https://arxiv.org/pdf/1504.04822v1),
Section II (2)--(4), printed pp. 4--5, and Section V, printed p. 8.
The arXiv footer is v1, 19 April 2015; the retrieved title page says
6 July 2021. The source uses angular frequency. Smooth compact spectra
meet its degree-dependent regularity hypotheses for every finite p.
The proof below fixes the 2pi convention and independently checks the
support and weighted-norm specialization. No source approximation or
L2 estimate is being used to assert complex positivity or control M.

## Conclusion

For every f in V_R,

    Q_a(f)=-integral_R W_a(x)u(x,b)dx,
    E_a(f)=-integral_{|x|>a} W_a(x)u(x,b)dx.          (2)

All integrals are absolutely convergent. For f in H_a, continuity gives
u(x,b)>=1 on [-a,a], so

    Q_a(f)<=E_a(f)-mu_a(R^2)<=E_a(f).                (3)

For each a the real linear functional E_a is bounded in N on V_R.
Nevertheless, there are constants c_R>0 and T_R, independent of f,
such that for every T>=T_R,

    sup_{0!=f in V_R} |E_a(f)|/N(f)
        >=c_R L^(R/4)/a^2.                          (4)

Thus the ratio of this lower bound to the required O_R(a) norm tends
to infinity, at least as a constant times L^(R/4)/a^3. In particular,
no bounded real-axis representative of this particular E_a can have
L-infinity norm O_R(a), even if representatives are allowed to vary
with a. Since M<=N, the same obstruction holds for its full-space
operator norm with denominator M.

This stops the specific clipped strip-Poisson certificate (1). The
norm tests used below need not belong to H_a. Consequently (4) does
not refute Q_a(f)<=C_R a M(f) on H_a, prove a detector cost bound or
rule out other positive measures supported on the rectangle. It also
does not preclude a bound for E_a restricted to H_a that uses further
positivity information. No actual-Xi signs or RH conclusion follows.
The first independent critical audit of 2026-10-30 passes for (1)--(4) and
their qualifications. It found no mathematical defect or stronger norm
estimate; originality is not certified. It does not cover the following
later supplementary calculation.

For the slow-dilation family specified above, set

    eta_R=1/(8R+2), k_R=inf_{|x|>=eta_R} K(x),
    A_R=2/k_R, C_R=R A_R exp(2pi R).

Then 0<k_R<=1, f belongs to V_R, N(f)<=A_R M(f), and

    |Q_a(f)|<=R A_R (a/D)exp(2pi R b/D)M(f)
             <=C_R a M(f)/B.                       (19)

The constant is independent of T, D, p and the chosen envelope.
For nonzero f this gives |Q_a(f)|/[a M(f)]<=C_R/B, tending to zero
uniformly as T tends to infinity. Hence this restricted construction
cannot provide an unbounded positive ratio, even if some members lie
in H_a. No statement about other dilation regimes, unrestricted H_a,
existence in H_a, detector realization or Xi signs follows. Equation
(19) passes the separate slow-dilation critical audit of 2026-10-30
recorded below. It remains a known-method specialization, not a claim
of progress beyond the checked source methods.

## Proof

### Positive kernel and its exact transform

For r=pi t/(2b) and theta=pi y/(2b), direct algebra gives

    p_b(t,y)=cosh(r)cos(theta)
              /[2b(sinh(r)^2+cos(theta)^2)].          (5)

For 0<=y<b this is even in t, strictly positive and integrable in t.
We use angular frequency s temporarily: the Fourier integral below
has exp(i s t), so s=2pi v in the defining convention for V_R.

Let h_b(z)=(2b)^(-1)sech(pi z/(2b)). For s>=0 integrate
h_b(z)exp(i s z) around the rectangle with horizontal sides at
Im z=0 and Im z=2b and vertical sides tending to infinity.
The vertical integrals vanish by exponential decay in |Re z|.
The single enclosed pole is ib, with residue
exp(-s b)/(pi i). Also h_b(z+2ib)=-h_b(z). Accounting for the
reversed orientation of the top side gives

    (1+exp(-2s b)) integral_R h_b(t)exp(i s t)dt
       =2exp(-s b).

Evenness extends the result to real s. Shifting the integration line
to Im z=+y or -y crosses no poles for y<b; vertical integrals again
vanish. Since p_b(t,y)=[h_b(t+iy)+h_b(t-iy)]/2, it follows that

    integral_R p_b(t,y)exp(i s t)dt
        =cosh(s y)/cosh(s b).                       (6)

In particular p_b has integral 1. Tonelli's theorem and positivity give

    integral_R w_b(t)dt
       =integral_0^b exp(-lambda y)dy<=b.            (7)

This proves the asserted integrability, including at its possible
point singularity. Fubini is valid in (6) integrated over y, so with

    I_b(s)=integral_0^b exp(-lambda y)cosh(sy)dy

we have

    integral_R w_b(t)cos(st)dt=I_b(s)/cosh(s b).      (8)

The zero-height real trace of f is Schwartz by integration by parts
in its smooth compact Fourier integral. Fourier inversion implies
that phi is real and even. Thus

    u(x,y)=integral_{-R}^R phi(v)cos(2pi v x)
                                     cosh(2pi v y)dv.

Using (6) in this representation proves, for 0<=y<b,

    u(x,y)=integral_R p_b(x-t,y)u(t,b)dt.            (9)

For each fixed b the function u(t,b) is bounded (and Schwartz), and
p_b has mass 1. These facts justify all interchanges in (9), and
its integration over 0<=y<b. Integrating (9) at x=a and x=-a
gives the first equality in (2); subtracting the integral on [-a,a]
gives the second. Equation (7) shows mu_a has mass at most 2b.
For sufficiently large T, B>b. For each fixed x in the closed interval
[-a,a], take y down to b within (b,B). Continuity from (H) proves (3),
including x=+-a, without extending positivity into 0<=y<b or outside
|x|<=a. The infinite density values possibly occurring at x=+-a do
not create atoms: mu_a is the finite measure with integrable density
W_a relative to dx.

To check actual boundedness for each a, Fourier inversion yields
|phi(v)|<=N(f). Therefore, with the continuous value at y=0,

    |u(x,y)|<=N(f) S_R(y),
    S_R(y)=sinh(2pi R y)/(pi y), S_R(0)=2R.

Consequently

    |E_a(f)|<=N(f)[2 integral_0^b exp(-lambda y)S_R(y)dy
                               +2b S_R(b)]<infinity. (10)

This finite bound is only a boundedness check, not the desired
uniform O_R(a) certificate.

### The uncancelled half on a resonant cosine

First evaluate the compact expression (1) on g(z)=cos(s z), for s>0
with s a=2pi n, n an integer. This preliminary computation does not
assert that g is in V_R. It gives Q_a(g)=-2I_b(s). Evenness of w_b
and the resonance yield

    integral_{-a}^a W_a(x)cos(sx)dx
        =2 integral_0^{2a} w_b(t)cos(st)dt.

Put J_b(s)=integral_{2a}^infinity w_b(t)cos(st)dt. By (8),

    E_a(g)=-I_b(s)-2cosh(s b)J_b(s).                (11)

We bound J_b without a sampled Fourier approximation. Since beta is
fixed, scaling t=b r, y=b v gives

    w_b(t)=W(t/b),
    W(r)=(1/2) integral_0^1 exp(-beta v)
                              Re sech(pi(r+iv)/2)dv.

For r>=8, the geometric series

    (1/2)sech(pi(r+iv)/2)
       =sum_{k>=0} (-1)^k exp(-(2k+1)pi(r+iv)/2)

converges absolutely and uniformly, together with its first two
r-derivatives, for 0<=v<=1. Indeed the j-th derivative has absolute
sum at most

    exp(-pi r/2) sum_{k>=0} ((2k+1)pi/2)^j exp(-8pi k)

for j=0,1,2. It follows that the absolute constant

    D=|W'(8)|+integral_8^infinity |W''(r)|dr

is finite, and W and W' vanish at infinity. Because 2a=8b,
sin(2as)=0 and cos(2as)=1, two integrations by parts give

    J_b(s)=-w_b'(2a)/s^2
            -(1/s^2)integral_{2a}^infinity w_b''(t)cos(st)dt,
    |J_b(s)|<=D/(b s^2).                            (12)

Set d_0=exp(-beta)(1-exp(-1))/2>0. If sb>=1, integrating only
b-1/s<=y<=b gives

    I_b(s)>=exp(-beta) integral_{b-1/s}^b exp(sy)/2 dy
            =d_0 exp(s b)/s.                        (13)

As cosh(sb)<=exp(sb), (11)--(13) imply, whenever
bs>=max(1,4D/d_0),

    E_a(g)<=-(d_0/(2s))exp(s b).                   (14)

The full signed residual, rather than one individual boundary
evaluation, has retained an exponentially large component.

### Genuine tests in the smooth Fourier class

Fix an even nonnegative chi in C_c^infinity((-1,1)) with integral 1,
and define

    h(z)=integral chi(v)exp(2pi i v z)dv,
    H=integral_R |h(x)|dx<infinity.

This fixed h is even, real on R, entire, Schwartz on R, and h(0)=1,
so H>0. For each sufficiently large a choose

    n=floor(R a/2), s=2pi n/a, A=a^2,
    f_a(z)=h(z/A)cos(s z).                           (15)

For a>=4/R, pi R/2<=s<=pi R. The Fourier transform of f_a is

    (A/2)[chi(A(v-s/(2pi)))+chi(A(v+s/(2pi)))].

Its support is contained in [-R,R] once 1/A<=R/2. Thus f_a belongs
to V_R, without any uniform bound on derivatives of its transform.
On the real axis,

    0<N(f_a)<=A H=a^2 H.                            (16)

The strict positivity follows from f_a(0)=1. This construction does
not impose (H).

The approximation on the compact support of (1) is quantitative.
Evenness of chi and the integral remainder for cosine give, for any
complex w,

    |h(w)-1|<=2pi^2 |w|^2 exp(2pi |Im w|).

For |x|<=a, 0<=y<=b, a>=1 and w=(x+iy)/a^2, this is at most

    epsilon_a=C_h/a^2,
    C_h=(17pi^2/8)exp(pi/2).

Since |cos(s(x+iy))|<=exp(s y), the gap integral in (1) changes by
at most 2epsilon_a exp(sb)/s. The measure term changes by at most
2b epsilon_a exp(sb), by (7). Hence

    |E_a(f_a)-E_a(g)|
       <=2epsilon_a(b+1/s)exp(s b).                 (17)

For fixed R this is O_R(a^(-1)exp(sb)), uniformly for the frequencies
in (15). In particular, for all sufficiently large a it is at most
(d_0/(4s))exp(sb). Conditions for (14) also hold for all such a.
Here is a sufficient simultaneous onset, making that uniformity explicit.
Put kappa=max(1,4D/d_0) and choose

    a_R=max(1, 4/R, sqrt(2/R), 8kappa/(pi R),
            4C_h pi R/d_0, sqrt(16C_h/d_0)).

If a>=a_R, the frequency and support conditions in (15) hold,
bs>=a pi R/8>=kappa, and

    2epsilon_a s(b+1/s)
       <=C_h pi R/(2a)+2C_h/a^2<=d_0/4.

Thus (17) has the required error for every such a, including the
values where floor(Ra/2) jumps. Taking T_R=exp(exp(pi a_R)) ensures
these conditions and B>b at every real T>=T_R. This is a symbolic
sufficient onset in terms of the finite constants D,C_h, not a
numerically evaluated height.

Combining (14), (16) and (17),

    E_a(f_a)<=-(d_0/(4s))exp(s b),
    |E_a(f_a)|/N(f_a)
       >=[d_0/(4pi R H)] exp(s b)/a^2.              (18)

Finally s>=pi R-2pi/a and b=a/4, so

    exp(s b)>=exp(-pi/2)exp(pi R a/4)
              =exp(-pi/2)L^(R/4).

Equation (4) follows with c_R=d_0 exp(-pi/2)/(4pi R H).
The onset may depend on the fixed R, while c_R is independent of T
and f. This argument works for every sufficiently large real T,
not only a subsequence of resonant widths.

If E_a(f)=integral f(x)r_a(x)dx for all f in V_R with a bounded
measurable representative r_a, Holder's inequality forces
||r_a||_infinity>=sup |E_a(f)|/N(f). The same necessary bound
applies to any full-space N-bounded real-axis functional, regardless
of the chosen representation. Since V_R is closed under f->-f,
a one-sided full-space residual bound would also imply the absolute
bound refuted above. This does not make the tests members of H_a.
Finally 0<=K<=1 gives M(f)<=N(f), which proves the stated weighted
norm obstruction without invoking a weighted norm conversion.
For nonzero f in V_R, M(f)>0: K(x)>0 for x!=0, so M(f)=0 would
force f=0 almost everywhere on R and hence everywhere by continuity
and the identity theorem. Thus the ratios with denominator M are
well defined on precisely the nonzero tests used above.

### Independent critical audit, 2026-10-30

The audit replayed the residue and both contour shifts in (6) with
s=2pi v; the positivity/mass and absolutely convergent Fourier
interchanges in (7)--(9); the plus sign of mu_a in (1); and the
endpoint limit from (H). No positivity in the gap was used. Evenness
expresses each clipped cosine transform as half the complete transform
minus the tail J_b, giving (11) and leaving the I_b contribution.
The two integrations by parts in (12) occur only at t>=2a=8b,
away from the integrable singularity, and scaling gives the factor
1/b with an absolute D. The smooth tests have the stated compact
Fourier support, N<=a^2 H and the complex approximation error (17).
The common onset displayed above verifies all error and resonance
conditions simultaneously for fixed R at every large real T.

These checks validate the existing lower bound, not an improvement
of it or a new kernel theorem. The ratio to a diverges since
exp(pi R a/4)/a^3 tends to infinity. The norm argument uses the
whole real vector space V_R (including its sign reversal), whereas
H_a imposes the additional lower bound 1 and is not closed under
sign reversal. Therefore no conditional positive-class inequality
is refuted. No L503 theorem, source manuscript, actual-Xi sign,
detector realization or RH assertion is certified by this audit.

### Supplementary slow-dilation calculation, 2026-10-30

This subsection proves only (19) under its separate family hypotheses.
It uses Fourier inversion and the cited polynomial-envelope mechanism,
not the clipped-measure conclusion or any theorem of L503. Write
p(z)=sum_{j=0}^m c_j z^j, allowing zero coefficients. With

    psi_D(v)=D psi(Dv),
    phi_f(v)=sum_{j=0}^m c_j (-2pi i)^(-j) psi_D^(j)(v),

the change of variable v=w/D gives e(z/D)'s Fourier representation.
Integrating by parts j times gives

    integral psi_D^(j)(v)exp(2pi i v z)dv
       =(-2pi i z)^j e(z/D).

Every boundary term vanishes because psi_D is globally smooth and
compactly supported. These identities hold for every complex z;
all the integrals have compact support. Thus phi_f is smooth, supported
in [-r,r] with r=R/D, and represents f in the 2pi convention. Polynomial
multiplication has not increased the bandwidth. D>=1 gives r<=R,
and p and e give the required evenness and reality, so f belongs to V_R.
Repeated integration by parts on the real axis shows f is Schwartz.
In particular N=N(f) and M=M(f) are finite. Fourier inversion now yields

    phi_f(v)=integral f(x)exp(-2pi i v x)dx,
    |phi_f(v)|<=N,
    |f(x+iy)|<=2r exp(2pi r|y|)N.                 (20)

The inverse-transform coefficient bound uses N itself; no norm of
psi_D's derivatives or of the polynomial coefficients enters (20).

Here is the weight conversion in full, independently of L503's
unaudited theorem. For x!=0, |sin(pi x)|<pi|x| gives K(x)>0.
Also K is continuous, 0<=K<=1, and K(x)>=1-1/pi^2 for |x|>=1.
Compactness on eta_R<=|x|<=1 proves k_R>0. At y=0, (20) and
r<=R give sup_R |f|<=2R N. Consequently

    integral_{|x|<eta_R}|f(x)|dx
        <=4R eta_R N<=N/2,
    M>=k_R integral_{|x|>=eta_R}|f(x)|dx>=k_R N/2.

Thus N<=A_R M with an ambient-R constant uniform in all the allowed
parameters. This handles the isolated zero K(0)=0 without dividing
pointwise by K or assuming a uniform envelope bound.

For 0<=y<=b, lambda>0, and (20) gives

    |Q_a(f)|
      <=integral_0^b exp(-lambda y)
                       [|f(a+iy)|+|f(-a+iy)|]dy
      <=4r b exp(2pi r b)N
      <=R A_R (a/D)exp(2pi R b/D)M.

This integral is over a finite interval of continuous functions, so
there is no infinite interchange or endpoint problem. For L>1,
b/B=log L/L<=1. Since D>=B, b/D<=1 and D^(-1)<=B^(-1), proving
(19) with the displayed C_R for every T>exp(1). The case p=0 gives
both sides zero. Otherwise f is nonzero (e(0)=1), so N>0 and the
weight conversion implies M>0; division to obtain the ratio is valid.
Since B=log T/(4pi), its uniform upper bound tends to zero.

The calculation is an elementary specialization of the inspected
source's spectral-support facts. It does not strengthen the source's
approximation theorem and imports none of its approximation conclusions.
The earlier audit of (1)--(4) does not certify this later subsection.

### Independent critical audit of supplementary (19), 2026-10-30

The separate audit verifies exactly the supplementary family and (19),
using the saved SPECIALIZE assessment
`drafts/literature/2026-10-30-slow-dilation-bound-audit.md`.
The scaled spectrum is D psi(Dv); j integrations by parts give
(-2pi i z)^j, confirming both sign and normalization of phi_f.
Global smooth compact support removes all endpoint terms and is
preserved by every finite derivative. The resulting support [-R/D,R/D]
is independent of polynomial degree. These are exact identities, not
an approximation uniform in an unbounded number of derivatives.

For each admissible f, its real trace is Schwartz. Fourier inversion
therefore gives |phi_f|<=N without a constant depending on derivatives,
degree, coefficients or the envelope. Integration over the support of
length 2r gives (20). Since D>=1, the same estimate at y=0 gives
sup |f|<=2R N. Here 4R eta_R=4R/(8R+2)<1/2. Positivity and continuity
of K away from zero, together with its stated uniform tail lower bound,
give k_R>0; hence M>=k_R N/2. No pointwise division by K(0) is used.

There are two gap sides, so integrating their bounds over length b
gives 4rb=Ra/D. For all T>exp(1), a,b,lambda,B are positive and
b/B=log L/L<=1; D>=B implies b/D<=1 and 1/D<=1/B. These checks give
exactly C_R=R A_R exp(2pi R), with a common onset T>exp(1) for every
degree, envelope and allowed D. The case p=0 is identically zero.
If p is nonzero, e(0)=1 ensures that p e(z/D) is not identically zero,
so N>0 and the conversion ensures M>0 before division. Constant p is
included. Every integration is absolutely convergent or over a compact
interval; no uniform derivative norm or interchange over degrees is
required.

No mathematical error or stronger estimate was found. This independent
replay validates only the restricted-family stop: its upper ratio tends
to zero as B tends to infinity. It does not certify H_a membership,
unrestricted H_a bounds, other dilation regimes, the source manuscripts,
L503, actual-Xi transfer, RH or a matching Mathlib theorem. The original
audit's scope remains (1)--(4); this separate audit supplies the new
coverage of (19).

## Mathlib

Full coverage of the clipped-measure norm obstruction has not been
checked. Fourier inversion, Holder's inequality and residue calculus
are standard supporting results; no matching Mathlib theorem name is
asserted. Unknown availability is not evidence of absence.

Full Mathlib coverage of supplementary (19), including the isolated-zero
weighted norm conversion and its uniform family quantifiers, is not
checked. Fourier inversion and compact-support differentiation are
supporting standard inputs, not a claim of a matching formal theorem.

The source assessment for the original clipped-residual attempt is
`drafts/literature/2026-10-30-signed-gap-flux-dual-test.md`. It compares
Brevig--Chirre--Ortega-Cerda--Seip, *Point evaluation in Paley--Wiener
spaces*, [v2](https://arxiv.org/pdf/2210.13922v2), Theorem 3.10,
printed pp. 12--15: a formal endpoint residual need not have a finite
norm. That theorem is context, not a premise of this proof. Here
boundedness for each geometry and failure of the required uniform
bound are both established on the full smooth Fourier class. The
classical kernel identities are reproduction; the exact clipped
residual obstruction was not identified in the checked sources,
which does not establish originality.

Supplementary (19) uses the separately approved source assessment
`drafts/literature/2026-10-30-slow-dilation-weighted-gap-cost.md`.
The primary construction citation and the exact specialization are
recorded in its hypotheses and proof above.
