# Corollary 997d: a paid Hardy point certificate retains exponential amplification

## Hypotheses

Use C997c(1),(4)-(6) exactly: n>=2 is an integer, I=[7/4,9/4],
mu is any finite complex Borel measure on I, V=||mu||_TV, and

    g_n(t)=K_(n+2)(t)*exp(-t/2)*cosh(3t/8),
    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    h_U(t)=-2*g_n(t)*integral_I exp(-cn/4)
                                  *1_{cn<=t<=c(n+2)}dmu(c),
    h_L(t)= 2*g_n(t)*1_{n<=t<=n+2}*integral_I exp(-cn/4)dmu(c),
    H_j(z)=integral_R exp(izt)*h_j(t)dt, j=U,L,
    H(z)=H_U(z)+H_L(z)=H_n^+(z;mu).

Set E=[15/8,17/8], z_star=1+i/8, D=sup_E|H| and D_U=sup_E|H_U|.
Both short intervals, both terms in cosh and K's constant subtraction
are retained. No positivity, density assumption on mu, actual-zero
realization, selected-response identity or RH hypothesis is made.

## Conclusion

Write

    theta=arctan(1/32)/pi, 0<theta<1/96,
    rho=3/sqrt(pi*theta), B_theta=2^(5/2-2*theta)*rho,
    m_U=12*sqrt(pi)*exp(27/16), m_L=8*sqrt(pi)*exp(3/4),
    m=m_U+m_L, A=9/32,
    ell_n=8*exp(3/4)*(n+2)*exp(-n/16).

The exact densities above belong to L1(R) intersect L2(R). The carrier
functions F(z)=exp(-inz)H(z) and F_U(z)=exp(-7inz/4)H_U(z) belong
to H2 of the upper half-plane, with the convention
||f||_H2=sup_(y>0)||f(.+iy)||_L2(R), and satisfy

    ||F||_H2 <= m*(n+2)*exp(A*n)*V,
    ||F_U||_H2 <= m_U*(n+2)*exp(A*n)*V.                       (1)

The imported boundary-continuation theorem gives

    |H(z_star)| <= P_F(n)*exp(b_F*n)*V^(1-theta)*D^theta,
    P_F(n)=B_theta*[m*(n+2)]^(1-theta),
    b_F=(5-9*theta)/32>0,                                   (2)

and the more favorable upper-band estimate

    |H_U(z_star)| <= P_U(n)*exp(b_U*n)*V^(1-theta)*D_U^theta,
    P_U(n)=B_theta*[m_U*(n+2)]^(1-theta),
    b_U=(2-9*theta)/32>0.                                   (3)

The complete response, rather than an upper-only surrogate, obeys

    |H(z_star)| <= exp(-n/8)*ell_n*V
       +P_U(n)*exp(b_U*n)*V^(1-theta)*(D+ell_n*V)^theta.      (4)

For b=b_F or b_U and P=P_F or P_U, converting the corresponding
scalar bound P(n)exp(bn)V^(1-theta)D_0^theta to

    C*exp(-kappa*n)*V+B_n*D_0

uniformly over all nonnegative scalar ratios D_0/V, with fixed C>0
and kappa>0, requires and is achieved by B_n at least

    theta*(1-theta)^((1-theta)/theta)
       *P(n)^(1/theta)*C^(-(1-theta)/theta)
       *exp(r_b(kappa)*n),
    r_b(kappa)=[b+kappa*(1-theta)]/theta.                   (5)

Even the upper-only scalar conversion has

    r_(b_U)(kappa)>183/32,
    r_(b_F)(kappa)>471/32.                                 (6)

Thus this certificate does not give subexponential amplification for
every epsilon>0 at any fixed positive TV-error exponent. Equations
(5)-(6) concern domination of the displayed scalar upper envelopes,
not the best inequality on the actual response range. No admissible
slope-measure counterexample to the desired point inequality is proved.

Step325, 10 November 2026: RESEARCH / REPRODUCTION under the unchanged
pre-invocation EXPLORE assessment323, approved in step324. This is an
inconclusive mathematical EXPLORATION and a stop of this certificate,
not a new discovery, an all-range obstruction or an RH candidate.
Independent audit of this specialization remains pending.

## Proof

### Imported theorem and why specialization is necessary

Import Y. Grabovsky and N. Hovsepyan, *Optimal error estimates for
analytic continuation in the upper half-plane*, Communications on Pure
and Applied Mathematics 74 (2021), 140-170,
[published author copy](https://sites.temple.edu/yury/files/2023/06/general_curve.pdf),
Theorem 2.7, equations (2.20)-(2.22), pp149-150; its boundary case and
proof are in Section 5, pp162-168. The exact contract and essential proof
cases were inspected in review322 and reused in assessment323/step324.
For f in H2 of the upper half-plane with ||f||_H2<=1 and
||f||_L2(-1,1)<=delta, 0<delta<1, the theorem states

    |f(w)|<=rho(w)*delta^gamma(w), w=x+iy, y>0,
    gamma(w)=-arg((w+1)/(w-1))/pi,
    rho(w)^(-2)=(y/9)*[arctan((x+1)/y)-arctan((x-1)/y)].

This general theorem is not reproved. Its unrestricted-class sharpness
is not an obstruction for our slope measures. Named Plancherel and
finite-complex-measure Fubini are also imported. What requires proof
here is the density and original-V norm cost, carrier legality, affine
rescaling, lower-band error and both exponential quantifiers. C997c's
audited proof supplies the measure-theoretic premises and L997(4)'s
bound on the original K; no Laguerre asymptotic is assumed.

### Densities, paid norms and legal carriers

For each fixed n, the integrands are measurable and absolutely
integrable on the compact rectangle I times [0,9(n+2)/4] against
d|mu|(c)dt. Fubini gives the displayed densities, including for atomic
mu. Endpoints have zero dt measure for each c. Compact support and
bounded densities imply L1 and L2 membership and entire Fourier
transforms. All subsequent finite-integral identities hold for complex
mu by the same domination; no interchange over actual zeros occurs.

By L997(4), already used in C997c,

    |g_n(t)|<=2*(n+2)*exp(3t/8), t>=0.

For the individual upper density h_(U,c), its support has length 2c,
and throughout that support

    |h_(U,c)(t)|<=4*(n+2)*exp(cn/8+3c/4).

Consequently

    ||h_(U,c)||_2 <=4*sqrt(2c)*(n+2)*exp(cn/8+3c/4)
                  <=6*sqrt(2)*exp(27/16)*(n+2)*exp(9n/32).

The corresponding lower density has support length 2 and satisfies

    ||h_(L,c)||_2 <=4*sqrt(2)*(n+2)
                                      *exp((3/8-c/4)n+3/4)
                  <=4*sqrt(2)*exp(3/4)*(n+2)*exp(-n/16).

These estimates pass to the integrated densities with factor V. To
check this without assuming an L2 density for mu, write dmu=u d|mu|,
|u|=1 almost everywhere. Cauchy-Schwarz gives, for j=U,L,

    |integral h_(j,c)(t)dmu(c)|^2
                   <=V*integral |h_(j,c)(t)|^2 d|mu|(c).

Integrate in t by nonnegative Fubini and take square roots. This proves
||h_j||_2<=V*sup_c||h_(j,c)||_2. The V=0 case is identically zero.

With our Fourier normalization, Plancherel gives
||integral exp(ixt)a(t)dt||_2=sqrt(2pi)||a||_2. If a is supported
in [0,infinity), the same identity applied to exp(-yt)a(t) gives
H2 membership and its norm, by dominated convergence as y decreases
to zero. C997c supplies supp h_L subset [n,n+2] and
supp h_U subset [7n/4,9(n+2)/4]. Multiplication by exp(-ianz)
translates the density from t to t-an. Thus the carriers in (1) are
exact, preserve every real-boundary modulus and the boundary L2 norm,
and leave nonnegative spectral support. The triangle inequality gives
(1) with the stated m_U,m_L and exp(-n/16)<=exp(9n/32).

For this uniform nonnegative-support carrier construction, the shifts
a=1 and a=7/4 are maximal for H and H_U respectively. Indeed, take
the admissible mu=delta_(7/4). Its upper density is nonzero almost
everywhere in the interior of [7n/4,7(n+2)/4]: the nonzero polynomial
K has only finitely many real zeros and the other factors never vanish.
Its lower density is likewise nonzero on an interval immediately to
the right of n, where the upper density is absent. A larger respective
shift produces a nonzero negative-frequency interval. Plancherel on
horizontal lines then shows exponential growth of the squared L2 norm
as y tends to infinity, so that carrier function is not in H2.
This only bounds this pure-carrier construction; other analytic weights
are neither tested nor excluded.

### Interval rescaling and the exact harmonic exponent

Suppose a nonzero entire G is in H2 with ||G||_H2<=M, M>0, and
D_0=sup_E|G|. Define

    f(w)=G(2+w/8)/(2*sqrt(8)*M).

Changing variables on each horizontal line gives ||f||_H2<=1/2.
Its boundary data norm delta=||f||_L2(-1,1) is in (0,1/2], and
delta<=D_0/(4M). Positivity follows from the identity theorem if G
is nonzero. The hypotheses of the imported theorem therefore hold.
For G identically zero the desired bound is immediate. The rescaled
target is w_star=8*(z_star-2)=-8+i. At this point

    (w_star+1)/(w_star-1)=(64-2i)/82,
    gamma(w_star)=arctan(1/32)/pi=theta,
    rho(w_star)^(-2)=[arctan(9)-arctan(7)]/9=pi*theta/9.

The arctangent difference lies in (0,pi/2) and its tangent is
(9-7)/(1+63)=1/32, which verifies the branch choice. Undoing the
normalization yields

    |G(z_star)|<=B_theta*M^(1-theta)*D_0^theta.              (7)

No extra restriction such as D_0<4M is necessary: the theorem uses
the actual delta<=1/2, and only then its upper bound D_0/(4M).

Apply (7) to F in (1). On E its modulus equals |H|, while at
z_star the identity is |H(z_star)|=exp(-n/8)|F(z_star)|.
This gives (2), including its polynomial prefactor and exponent.
Apply it to F_U: now the point factor is exp(-7n/32), giving (3).
For a smaller legal carrier a the exponent would be
A*(1-theta)-a/8, so these choices minimize that exponent within
the just-verified pure-carrier class with the same paid norm.

C997c(5) gives ||h_L||_1<=ell_n*V. Its support is in [n,n+2],
so sup_E|H_L|<=ell_n*V and
|H_L(z_star)|<=exp(-n/8)*ell_n*V. Hence D_U<=D+ell_n*V,
and (3) plus the triangle inequality proves (4). The lower band was
not silently dropped. For example, separating its noise in (4) by
(x+y)^theta<=x^theta+y^theta gives an upper-error term proportional to

    (n+2)*exp((b_U-theta/16)*n)*V,
    b_U-theta/16=(2-11*theta)/32>0.                         (8)

This particular propagated upper error grows. It is not evidence
that the actual lower-interval contribution grows; its point value
already has the exponentially decaying direct bound above.

### The scalar conversion and its limited meaning

Fix 0<theta<1, A_0>0 and tau>0. An inequality

    A_0*x^theta<=tau+B*x for every x>=0

holds if and only if B is at least the supremum over x>0 of
A_0*x^(theta-1)-tau/x. Differentiation gives its unique maximum at

    x^theta=tau/[A_0*(1-theta)],
    B_min=theta*(1-theta)^((1-theta)/theta)
                         *A_0^(1/theta)*tau^(-(1-theta)/theta).

The expression tends to minus infinity at zero and to zero at
infinity, and its derivative changes from positive to negative at
that point, so this is a global maximum. This elementary optimization
is the required additive specialization, not a reproof of analytic
continuation. Put x=D_0/V, A_0=P(n)exp(bn), tau=C exp(-kappa n)
to obtain (5). Its non-exponential factors are fixed constants and
powers of n+2. Thus log(B_min)/n tends to r_b(kappa).

Since arctan(u)<u for u>0 and pi>3, theta<1/96. Therefore

    b_U/theta=(2/theta-9)/32>183/32,
    b_F/theta=(5/theta-9)/32>471/32,

and adding kappa*(1-theta)/theta proves (6). Similarly (8)'s exponent
is greater than 181/3072. These strict rational comparisons suffice.
The exact endpoint arithmetic was checked by
`python3 scripts/adaptive-slope/paid-hardy-point-arithmetic-325.py`;
the certificate is
`scripts/adaptive-slope/paid-hardy-point-arithmetic-325.json`.
Its complete `/checks` object was inspected with
`python3 ../scripts/loop/inspect_json.py scripts/adaptive-slope/paid-hardy-point-arithmetic-325.json --pointer /checks --full`.
This checks rational arithmetic only, not the analytic proof, realization
of scalar extremizers, or the truth of the desired point inequality.

The desired conclusion requires a SINGLE kappa>0 and C independent
of epsilon, with data coefficient at most C_epsilon exp(epsilon n)
for EVERY epsilon>0, eventually uniformly over mu. For any kappa>0,
the above scalar conversion fails that requirement whenever
epsilon<r_b(kappa). Even removing the lower-band data error would
not repair its rate. Crucially, x in the optimization is a free scalar:
no assertion has been made that its maximizing values and the Hardy
upper envelope are attained together by actual slope measures. The
result is a precisely paid failure of this certificate. It neither
settles the nominated point inequality nor reopens old subclass stops.

The original selected normalization, both-sign transfer, slope-assay
feasibility, actual reconstruction, signed forcing, infinite-zero
complements, regulator uniformity, L993 and L984(H) remain unpaid.

## Mathlib

Matching coverage for this quantitative Hardy theorem and its exact
slope-measure specialization has not been checked and is unknown.
Plancherel, finite-complex-measure Fubini and the identity theorem are
standard named informal inputs; no claim of matching Mathlib names or
absence is made. The imported continuation theorem is precisely cited
above. L997 and C997c retain their existing coverage qualifications.
