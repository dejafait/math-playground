# Corollary 997a: exact real-measure and dual forms of the adaptive slope assay

## Hypotheses

Use L997's exact K_(n+2), a_n(c;eta), z_0(c) and phi(c), with

    n>=2, I=[7/4,9/4], Gamma=[7/4,9/4], eta_0=3/4+i.

I is the slope interval and Gamma the competing ordinate interval.
All quartets have multiplicity one and are hypothetical finite inputs.
Keep both short intervals in L997(5) and the -1 in K_(n+2).
For real d and complex z define the finite integral

    q_n(c;d,z)=-4*exp(-cn/4)*[
       integral_(cn)^(c*(n+2)) K_(n+2)(t)*exp(-t/2)
                                      *cosh(d*t)*cos(z*t)dt
       -integral_n^(n+2) K_(n+2)(t)*exp(-t/2)
                                      *cosh(d*t)*cos(z*t)dt].       (1)

The values d=1/2 used below are only auxiliary finite integrals;
they assert nothing about actual zeros or an enlarged spectral family.
Set

    f_n(c)=q_n(c;1/4,1), k_n(c,gamma)=q_n(c;3/8,gamma),
    (T_n mu)(gamma)=integral_I k_n(c,gamma)dmu(c),
    (S_n lambda)(c)=integral_Gamma k_n(c,gamma)dlambda(gamma).       (2)

mu and lambda are finite real signed Borel measures on their respective
closed intervals, with total variation norm. Fix M>0 and epsilon>0.
For h in the real Banach space C(I) define

    p_(n,M,epsilon)(h)=inf_lambda [
       M*||h-S_n lambda||_(C(I))+epsilon*||lambda||_TV].            (3)

No bound for (3), positive limiting rate, RH, actual-zero reconstruction,
signed arithmetic forcing, or infinite-zero interchange is assumed.

## Conclusion

The original complex-measure assay at fixed n, TV allowance M and
competing error epsilon is feasible if and only if

    p_(n,M,epsilon)(f_n)>=1.                                    (4)

More precisely, the exact dual identity is

    p_(n,M,epsilon)(h)
      =max {integral_I h dmu : ||mu||_TV<=M,
                                  ||T_n mu||_(C(Gamma))<=epsilon}. (5)

The maximum is attained; no minimizer in (3) is asserted. Equivalence
(4) covers every finite complex Borel measure allowed by review312,
not just atomic measures or measures with densities.

In particular, for any such normalized filter and any real lambda,

    1<=||nu||_TV*||f_n-S_n lambda||_infinity
                         +epsilon*||lambda||_TV.                 (6)

If along an unbounded sequence of integers there were lambda_n with

    ||f_n-S_n lambda_n||_infinity<=C*exp(-kappa*n), kappa>0,
    ||lambda_n||_TV<=C_xi*exp(xi*n) for every xi>0,                (7)

then no filters meeting review312's three simultaneous requirements
could exist. The constants in (7) must be independent of n along that
sequence. Neither estimate (7) is proved here.

There is also an exact warning for the proposed analytic obstruction.
For fixed mu let R_n(z)=integral_I q_n(c;3/8,z)dmu(c), an entire
function. Its two natural shifted evaluations satisfy

    R_n(1+i/8)+R_n(1-i/8)
      =integral_I f_n dmu+integral_I q_n(c;1/2,1)dmu(c).           (8)

Thus the selected normalization is not the normalization of this sum
without estimating the additional finite integral. Equation (8) does
not rule out other analytic continuation arguments.

Step314, 10 November2026: a standard duality specialization and exact
kernel reductions during one proof attempt under the pre-invocation
EXPLORE review312. These statements are not independently audited.
The completed target-level outcome is EXPLORATION / REPRODUCTION:
no construction, universal impossibility theorem, or paid asymptotic
rate was obtained. No progress beyond the known general duality tools,
certified originality, actual-Xi bound or RH candidate is claimed.

Step315 adds the exact residual-transfer estimate and the unsuccessful
interpolation certificate (10)-(17) below. They do not establish (7),
exclude other interpolation estimates, or decide the assay. This second
attempt is EXPLORATION / REPRODUCTION and is not independently audited.

Step318 adds the full-quartet strip-transfer trial (18)-(27) below.
It eliminates (8)'s extra term by using the entire real-ordinate boundary,
then pays an exponentially small TV remainder at the cost of a displayed
competing-response multiplier whose logarithm is of order n^2 log n.
This does not meet (7)'s subexponential amplification threshold or decide
the assay. It is EXPLORATION / REPRODUCTION, not independently audited.

## Proof

### Exact quartet and phase reduction

For eta=beta+i*gamma with real beta,gamma as in the assay, summing
all four points gives the identity

    sum_(omega in Q(eta)) exp((omega-1)*t)
          =4*exp(-t/2)*cosh((beta-1/2)*t)*cos(gamma*t).

Insert this in L997(5), including its outer minus sign. It yields

    exp(-cn/4)*a_n(c;beta+i*gamma)=q_n(c;beta-1/2,gamma).

The polynomial K_(n+2) is real on the real axis, so this response is
real. No Laguerre branch, reflected quartet point, endpoint or constant
subtraction has been omitted. The integrands are continuous on compact
sets; changing variables to fixed integration intervals proves that
f_n is continuous and k_n is jointly continuous on I times Gamma.

L997(7) gives

    z_0(c)^n=exp(-cn/4)*vartheta_n(c),
    vartheta_n(c)=exp(i*n*(phi(c)-c)), |vartheta_n(c)|=1.

Given an admissible complex nu, form the complex measure
lambda_0=vartheta_n*nu and then the real signed measure mu=Re(lambda_0).
Multiplication by vartheta_n preserves TV, and taking the real part
contracts TV: for every finite Borel partition, the sum of absolute
real parts is bounded by the sum of absolute complex values. Taking
the supremum over partitions proves ||mu||_TV<=||nu||_TV.
For any real continuous g,

    integral g dmu=Re(integral g*vartheta_n dnu).

Consequently the selected value remains one, while every competing
modulus is no larger. Conversely, from a real mu with the required
constraints take nu=conjugate(vartheta_n)*mu. It has the same TV,
selected value one, and precisely the real competing values T_n mu.
This proves equality of the two feasibility questions. It is a change
of filter measure, not a claim that an original complex filter is real.

### Standard functional-analytic inputs and their specialization

Import the standard named real Hahn–Banach dominated-extension theorem
and the Riesz–Markov–Kakutani representation theorem for bounded linear
functionals on C(I,R), with representing signed measure norm equal to
the functional's sup-norm operator norm. These are the real forms of
the extension/representation tools recorded in review312. Their general
theorems are not reproved. The following argument checks the norm,
kernel and constraint hypotheses needed for this particular operator.

Write D_n=max_(I times Gamma)|k_n|<infinity. Then
||S_n lambda||_infinity<=D_n*||lambda||_TV, and S_n lambda is continuous
by uniform continuity of k_n. For fixed n,M,epsilon, the functional p
in (3) is a norm on C(I). Homogeneity follows by scaling lambda;
the triangle inequality follows by adding two approximating measures
and letting their two approximation errors tend to zero. For every
lambda,

    ||h||_infinity<=||h-S_n lambda||_infinity+D_n*||lambda||_TV
      <=(1/M+D_n/epsilon)*[
                    M*||h-S_n lambda||_infinity+epsilon*||lambda||_TV].

Taking the infimum, and using lambda=0 for the upper bound, gives

    (1/M+D_n/epsilon)^(-1)*||h||_infinity<=p(h)<=M*||h||_infinity. (9)

This proves definiteness and equivalence with the usual norm, without
an unproved closed-range assertion or attainment of the infimum.

For h nonzero, the linear functional on its real span taking h to p(h)
is bounded in absolute value by p. Hahn–Banach extends it to a real
linear functional ell on C(I) with |ell(g)|<=p(g). By (9), ell is
sup-norm continuous with norm at most M. Riesz–Markov–Kakutani gives
a finite regular real signed Borel measure mu with ||mu||_TV<=M
representing ell. Such a measure belongs to the allowed class.
For each gamma in the closed Gamma interval,

    |(T_n mu)(gamma)|=|ell(S_n delta_gamma)|
        <=p(S_n delta_gamma)<=epsilon,

where the last inequality uses lambda=delta_gamma in (3). Thus mu is
admissible and integral h dmu=ell(h)=p(h). If h=0, the zero measure
gives the same conclusion.

For the reverse bound take any admissible mu and any lambda. The
kernel is bounded and both measures have finite variation, so its
absolute integral against the product variation measure is at most
D_n*||mu||_TV*||lambda||_TV. Fubini therefore gives

    integral_I (S_n lambda)dmu=integral_Gamma (T_n mu)dlambda.

It follows that

    integral_I h dmu
       <=M*||h-S_n lambda||_infinity+epsilon*||lambda||_TV.

Take the infimum over lambda. Together with the attained forward
inequality this proves (5). The upper bound applies to arbitrary
finite signed Borel measures; no regularity assumption on them is
needed. Representation supplies a regular maximizer, so this proof
also avoids any need to restrict the original admissible class.

If a normalized mu is feasible, (5) gives p(f_n)>=1. If p(f_n)>=1,
take the maximizing mu from (5) and divide it by p(f_n). Its selected
value is one, TV is at most M, and competing norm at most epsilon.
The phase reduction then gives an admissible complex nu. This proves
(4), including equality at the threshold. Applying the reverse bound
with the actual norm of nu proves (6).

### The asymptotic test and the extra analytic term

Suppose (7) held and a putative filter sequence had TV bounded by
every positive exponential allowance and competing norm at most
C_0*exp(-delta*n), delta>0. Choose xi smaller than both kappa and
delta. On the unbounded integer sequence in (7), inequality (6)
would bound one by

    C*C'_xi*exp(-(kappa-xi)*n)
                  +C_0*C_xi*exp(-(delta-xi)*n),

which tends to zero. This proves the conditional obstruction.
Equivalently, for any individual lambda with residual R>0, (6) gives
the exact lower bound

    ||nu||_TV>=[1-epsilon*||lambda||_TV]_+/R.

For R=0 and positive numerator, no such normalized filter exists.
These are certificate tests; this proof provides no lambda_n paying
their residual and norm requirements.

For fixed n, the t ranges in (1) are compact. On every compact set of
z, the integrands and all their z derivatives are uniformly bounded
in c and t. Finite TV then permits differentiation under the two
integrals, proving that R_n is entire. Finally,

    cos((1+i/8)*t)+cos((1-i/8)*t)=2*cos(t)*cosh(t/8),
    2*cosh(3*t/8)*cosh(t/8)=cosh(t/2)+cosh(t/4).

Substitution into the same complete finite integrals proves (8).
The term with cosh(t/2) is present, not controlled by the selected
normalization or the competing real-ordinate constraints. This explains
why that simple analytic identification does not yet pay an obstruction.

### Scope and diagnostic separation

The proof above uses no numerical evidence. The separate
scripts/adaptive-slope/dual-diagnostic-314.py and its same-stem JSON
test atomic choices of lambda by floating-point quadrature and truncated
SVD at n=8,16,24,32,48,64. They supply neither (7), a continuum bound,
nor a primal construction. The explicit status is UNCERTIFIED_DIAGNOSTIC;
quadrature comparison is only a numerical comparison, not an error
certificate. No finite-grid result is used in (1)-(9).

The main positivity gap, actual signed recovery, L993, infinite-zero
complements, regulator uniformity and L984(H) remain unresolved. This
reformulation does not replace any of them by an established premise.

### Quantitative interpolation trial — step315, 10 November 2026

This is a bounded test of a particular dual construction and its stated
upper estimates. It is not a lower bound on the optimal dual residual,
an impossibility theorem, or a replacement of the complete quartet by
a Fourier model. All estimates in this section are for the original
operator (1)-(2). The only additional general tool is Cauchy's residue
theorem, in the standard form already imported by L997's source chain
from [DLMF1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.E8).
Its application to the interpolation remainder is given explicitly;
the general theorem is not reproved. No bulk asymptotic is used.

Put

    U_n=[A*n,B*(n+2)], V_n=[n,n+2],
    h(t)=cosh(t/4)*cos(t)/cosh(3*t/8),
    H_lambda(t)=integral_Gamma cos(gamma*t)dlambda(gamma).

For every finite real signed lambda, boundedness on these compact
sets and finite variation justify Fubini in (1). Thus f_n-S_n lambda
is exactly the expression (1) with cosh(d*t)*cos(z*t) replaced by

    cosh(3*t/8)*[h(t)-H_lambda(t)].                            (10)

In particular, if E_U and E_V are the sup norms of h-H_lambda on U_n
and V_n respectively, L997(4) gives the complete operator bound

    ||f_n-S_n lambda||_infinity
      <=36*exp(27/16)*(n+2)*exp(9*n/32)*E_U
        +16*exp(3/4)*(n+2)*exp(-n/16)*E_V.                    (11)

Indeed the upper interval has length 2c, and its integrand in absolute
value, including the factor 4 in (1), is at most
8*(n+2)*exp(-cn/4)*exp(3c(n+2)/8)*E_U. Maximize over A<=c<=B.
The lower interval has length two and its corresponding bound is
8*(n+2)*exp(-cn/4)*exp(3(n+2)/8)*E_V. Here
3/8-A/4=-1/16. This proves (11), including the lower interval and
all endpoints. The bound for K includes its -1. Neither a Laguerre
branch nor a quartet entry is removed.

For t>=0, |h(t)|<=1. Hence E_V<=1+||lambda||_TV; a subexponential
TV bound would pay the lower interval. A sufficient upper-interval
condition is E_U=O(exp(-(9/32+kappa)*n)) for some kappa>0,
since the polynomial n+2 can be absorbed by any smaller positive
residual exponent. This is a sufficient condition for this method,
not a necessary condition on all successful dual approximations:
(11) can lose cancellations in the t integrals.

Here is the trial, including its reflected cosine term. For integer
m>=1 (an interpolation order, NOT the earlier Laguerre index n+2), put

    zeta=1+i/8, t_0=2n, gamma_j=A+j/(2m), 0<=j<=m,
    ell_j(z)=product_(0<=k<=m,k!=j) (z-gamma_k)/(gamma_j-gamma_k),
    P_m(u)=sum_(j=0)^m ell_j(zeta)*exp(i*gamma_j*u),
    lambda_(n,m)=2*sum_(j=0)^m
       Re(exp(i*zeta*t_0)*ell_j(zeta)*exp(-i*gamma_j*t_0))
                                                        *delta_(gamma_j).
                                                                    (12)

This is an admissible finite real dual measure on the CLOSED Gamma
interval, including both endpoints. Expanding the cosine exactly gives

    H_lambda(t)=Re(exp(i*zeta*t_0)*[
                               P_m(t-t_0)+P_m(-t-t_0)]).       (13)

The first term is intended to approximate exp(-t/8)*cos(t). The
second term is present and requires its own bound; it is not licensed
to vanish by a positive-frequency convention. Also, exactly,

    0<=cosh(t/4)/cosh(3*t/8)-exp(-t/8)
      =exp(-t/8)*(exp(-t/2)-exp(-3*t/4))/(1+exp(-3*t/4))
      <=exp(-5*t/8), t>=0.                                  (14)

Thus (13)-(14) retain the reflected entries responsible for (8),
instead of identifying one shifted analytic value with f_n.

Set D=sqrt(101)/8=max_(gamma in Gamma)|zeta-gamma|,
r_*=sqrt(65)/8=|zeta-2| and W=4eD. The equally spaced node denominators give

    L_m:=sum_j |ell_j(zeta)|
      <=(2mD)^m*sum_j 1/(j!*(m-j)!)
      =(4mD)^m/m! <=W^m <16^m,
    ||lambda_(n,m)||_TV <=2*exp(-n/4)*L_m
                          <=2*exp(-n/4)*W^m.                 (15)

Here m!>=(m/e)^m, D<4/3 and e<3 suffice for the last bounds.
The estimates are upper bounds; no comparable lower bound on actual
TV is asserted. In particular, for m=floor(alpha*n), alpha>0, (15)
certifies subexponential TV through its final W bound when
alpha*log(W)<=1/4. If this inequality fails, that final bound supplies
no such certificate; the actual L_m or TV could be smaller.

For completeness the main interpolation error is bounded by a
continuum contour estimate, not a grid test. For any fixed R>r_*,
apply the residue theorem on |w-2|=R to

    exp(i*w*u)/(w-zeta)
                      *product_(j=0)^m (zeta-gamma_j)/(w-gamma_j).

The residue at zeta is exp(i*zeta*u); that at gamma_j is
-ell_j(zeta)*exp(i*gamma_j*u). Distances on the circle are
|w-zeta|>=R-r_* and |w-gamma_j|>=R-1/4, while
|exp(i*w*u)|<=exp(R*|u|) for real u. Consequently

    |exp(i*zeta*u)-P_m(u)|
      <=R/(R-r_*)*exp(R*|u|)*(D/(R-1/4))^(m+1).              (16)

For t in U_n, |t-t_0|<=n/4+9/2. The reflected term in (13)
has the valid bound exp(-n/4)*L_m for every real t. Combining
(13)-(16) proves the full sufficient estimate

    E_U <= exp(-35*n/32)
      +exp(-n/4)*R/(R-r_*)*exp(R*(n/4+9/2))
                                      *(D/(R-1/4))^(m+1)
      +exp(-n/4)*W^m.                                       (17)

Every bound in (17) is on the closed continuum interval. The first
term is harmless in (11): its resulting rate is exp(-13*n/16).
The last term, however, leaves the positive upper-envelope exponent
1/32+alpha*log(W) after multiplication by exp(9*n/32).
This does not prove the reflected response is large; it proves only
that its displayed absolute bound cannot certify its smallness.

Even the main term's contour estimate has no usable parameter choice
in the region where (15)'s final W bound certifies the required TV.
For fixed R>r_*
and m=floor(alpha*n), its upper-envelope exponent in (11) is

    F(alpha,R)=1/32+R/4+alpha*log(D/(R-1/4)).

The certified norm range has alpha<=1/(4*log(W))<1/8:
indeed 4D>5>e implies W>e^2. Since r_*>1, differentiation gives

    partial_R F=1/4-alpha/(R-1/4)>1/4-(1/8)/(3/4)=1/12.

Also r_*-1/4<D: equivalently sqrt(65)-2<sqrt(101).
Hence F(alpha,R)>1/32+r_*/4>9/32 for all these R and alpha.
The contour bound therefore grows exponentially throughout this
parameter region. Optimizing the fixed contour radius cannot turn
it into a decaying certificate. This is a comparison of explicit
upper bounds, not a positive lower bound on the true residual. No
claim is made about sharper interpolation estimates, nonuniform
nodes, cancellation between the two terms in (13), or other measures.

The completed trial supplies no lambda_n satisfying (7), no filters
satisfying review312, and no all-measure obstruction. The two
quantitative defects are the unpaid reflected term and incompatible
norm/error certificates for this equidistant interpolation estimate.
The original operator remains undecided. This is the second
mathematical EXPLORATION on the adaptive assay, with no budget reset;
the dual-interpolation route is reassessed before another attempt.

### Full-quartet strip propagation trial — step318, 10 November 2026

This tests the two-parameter analytic mechanism under unchanged review312.
No new existence claim, all-measure impossibility theorem or improvement
of the stopped interpolation or Chebyshev designs is asserted. In this
section mu may be a finite COMPLEX Borel measure on I. Put

    a=1/4, b=3/8, V=||mu||_TV,
    U_n(d,z)=integral_I q_n(c;d,z)dmu(c),
    R_n(z)=U_n(b,z), s_n=|U_n(a,1)|,
    epsilon_n=sup_(gamma in Gamma)|R_n(gamma)|,
    T_n=9*(n+2)/4,
    B_n=(n+2)*[36*exp(27/16)*exp(9*n/32)
                         +16*exp(3/4)*exp(-n/16)].             (18)

Here s_n is the scalar selected response. The symbol B_n is an envelope,
not a lower bound on any actual response. For an original complex filter
nu, take mu=vartheta_n*nu with the unit phase in the exact reduction above.
Then V=||nu||_TV, the selected integral equals U_n(a,1), and the original
competing integrals equal R_n(gamma), with no loss in their moduli.
Thus this trial covers the original complex-measure class directly.

The exact finite integrals give joint entire dependence on d,z and

    partial_d^2 U_n + partial_z^2 U_n=0,
    U_n(-d,z)=U_n(d,z), U_n(d,-z)=U_n(d,z),
    |R_n(x+i*y)|<=B_n*V*exp(T_n*|y|), x,y real.               (19)

For joint analyticity, expand cosh(d*t)*cos(z*t) into its four
exponentials. Their power series and differentiated series converge
uniformly on every compact parameter set, since all t intervals lie
in [n,T_n] and n is fixed. The other factors are continuous, the c
interval is compact and mu has finite TV. Integration therefore
preserves the series and their derivatives. The two second derivatives
cancel termwise. This proves (19)'s identities without an assumed
multivariable uniqueness theorem. For the bound, use L997(4),
|cos((x+i*y)*t)|<=exp(|y|*t), cosh(b*t)<=exp(b*t), and t<=T_n.
The upper short interval has length 2c and contributes at most

    16*c*(n+2)*exp(-c*n/4+b*c*(n+2))
        <=36*exp(27/16)*(n+2)*exp(9*n/32).

The lower interval has length two and contributes at most
16*exp(3/4)*(n+2)*exp(-n/16). This gives exactly B_n. All quartet
terms, both intervals, both closed slope endpoints and K's -1 remain.

**The exact strip transfer and its uncontrolled boundary complement.**
Set lambda=4*pi/3 and, for real x, define

    P(x)=(2/3)*cosh(lambda*x)/(cosh(lambda*x)^2-3/4).

Then P is positive and even, its integral over R is one, and

    integral_R P(x)*exp(i*t*x)dx=cosh(t/4)/cosh(3*t/8),
    U_n(a,y)=integral_R P(y-x)*R_n(x)dx, y real.              (20)

These are the familiar strip Poisson multiplier at the specific widths
a,b. We verify the normalization and poles by the following finite
residue specialization, since the proof needs the precise kernel and
its complementary mass. The general input is Cauchy's residue theorem
in [DLMF1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.E8), already
inspected through L997 and used above; no new general propagation
theorem is being proved or imported.

Let g(z)=(1/(2b))*sech(lambda*z), where lambda=pi/(2b).
For t>=0 integrate sech(lambda*z)*exp(i*t*z) around the rectangle
with vertices -H,H,H+2ib,-H+2ib. There is exactly one pole inside,
at ib, with residue exp(-b*t)/(i*lambda). The top integrand is
-exp(-2b*t) times the bottom one. Both vertical integrals tend to
zero as H tends to infinity: sech(lambda*(+-H+i*y)) is uniformly
O(exp(-lambda*H)) for 0<=y<=2b, while |exp(i*t*z)|<=1 there.
The bottom integral I_t therefore satisfies

    (1+exp(-2b*t))*I_t=(2*pi/lambda)*exp(-b*t).

It follows that integral_R g(x)*exp(i*t*x)dx=sech(b*t).
Evenness gives the same formula for t<0. Shifting the real contour
to imaginary height +a or -a crosses no pole, because a<b; the
vertical sides again tend to zero for each fixed real t. Hence
the transforms of g(x+ia) and g(x-ia) are respectively
exp(a*t)*sech(b*t) and exp(-a*t)*sech(b*t). Their average is

    [g(x+ia)+g(x-ia)]/2
      =(1/(2b))*cosh(lambda*x)*cos(lambda*a)
                       /(cosh(lambda*x)^2-sin(lambda*a)^2)=P(x),

since lambda*a=pi/3. This proves the first part of (20), including
integral P=1 at t=0 and positivity from its explicit denominator.
In the integrand (1), convolution against P replaces cos(x*t) by
cos(y*t)*cosh(a*t)/cosh(b*t). After multiplication by cosh(b*t)
this is exactly the selected cosh(a*t)*cos(y*t). P is integrable,
the t intervals are compact, and (19) bounds R_n on the real line.
Absolute integrability against P(x)dx and the product variation
measure justifies every interchange. This proves the full second
identity in (20), with the lower interval and the constant subtraction.

Thus (8)'s auxiliary response can be eliminated exactly, but doing so
uses the WHOLE real boundary, not just Gamma. Evenness makes the known
band Omega=Gamma union (-Gamma). Its kernel mass seen from y=1 is

    omega=integral_Omega P(1-x)dx, 0<omega<101/4000<1/32,
    s_n<=omega*epsilon_n+(1-omega)*B_n*V.                    (21)

For the numerical rational bound, when |x|>=3/4 we have
cosh(lambda*x)>=2, so

    P(x)<= (32/39)*sech(lambda*x)<=2*exp(-lambda*|x|).

The distances from 1 to the two observed intervals run respectively
over [3/4,5/4] and [11/4,13/4]. Consequently

    omega < (3/(2*pi))*(exp(-pi)+exp(-11*pi/3))
           < (1/2)*(1/20+1/2000)=101/4000.

Here pi>3, exp(3)>sum_(j=0)^8 3^j/j!=20+41/4480>20,
and exp(11)>2^11>2000 suffice. The strict positivity of P gives
omega>0. The bound in (21) controls neither cancellation nor the
actual complementary integral; its TV coefficient grows exponentially.
It does not establish leakage for any feasible filter.

**A complete quantitative continuation certificate.** To test whether
the available analytic propagation estimate repairs that complement,
import O. Kovrijkine, *Some results related to the Logvinenko-Sereda
theorem*, [math/0012186v1](https://arxiv.org/pdf/math/0012186v1),
Lemma1 with proof, pp4-6, as inspected in review312. If phi is analytic
on D(0,5), J is a length-one real interval containing zero, E is a
positive-measure subset of J, |phi(0)|>=1, and
M=max_(|z|<=4)|phi(z)|, the lemma gives

    sup_J |phi| <= (C_K/|E|)^(log(M)/log(2))*sup_E |phi|.

Enlarge the absolute constant to C_K>=1 if necessary. No atom count or
Fourier-model replacement is needed. We check the normalization below
instead of assuming that the selected value normalizes R_n.

For any real L>=5/4 put

    J_L=[1-L,1+L],
    A_L=log(4*C_K*L)/log(2), theta_L=1/(1+A_L),
    tau_L=integral_(|x|>L) P(x)dx
                         <=(3/pi)*exp(-lambda*L).             (22)

The last estimate integrates the preceding tail bound on both sides.
The following bound is valid for EVERY finite complex mu:

    s_n <= tau_L*B_n*V
       +(B_n*V)^(1-theta_L)*epsilon_n^theta_L
                            *exp(8*L*T_n*(1-theta_L)).         (23)

If R_n vanishes identically, this follows from (20). Otherwise
H=max_(x in J_L)|R_n(x)|>0 and it is attained at some x_* in J_L.
Set phi(z)=R_n(x_*+2L*z)/H. It is entire and |phi(0)|=1. The
rescaled interval (J_L-x_*)/(2L) has length one and contains zero.
Because L>=5/4, Gamma is contained in J_L; its rescaled image E
has measure 1/(4L). The entire growth estimate (19) gives

    1<=M<=B_n*V*exp(8*L*T_n)/H.

The left inequality follows from phi(0), so the logarithmic exponent
has the required sign. Kovrijkine's lemma and sup_J |phi|=1 yield

    H <= epsilon_n*(B_n*V*exp(8*L*T_n)/H)^A_L,
    H <= epsilon_n^theta_L
                    *(B_n*V*exp(8*L*T_n))^(1-theta_L).

If epsilon_n=0, the identity theorem already makes R_n identically
zero, a case treated above. Otherwise this rearrangement is valid.
Split (20) at |x-1|=L, bound the inner part by H using integral P=1,
and the outer part by tau_L*B_n*V. This proves (23). In particular,
no inaccessible normalization or uncontrolled d=1/2 term is left.

Now fix any kappa>0 and choose

    L_n=max{5/4, [log((3/pi)*B_n)+kappa*n]/lambda}.

Then tau_(L_n)*B_n<=exp(-kappa*n). Weighted arithmetic-geometric
mean applied to (23), with the auxiliary scale exp(-kappa*n), gives
the requested LINEAR form, but with an expensive coefficient:

    s_n <= (2-theta_(L_n))*exp(-kappa*n)*V
                                       +D_(n,kappa)*epsilon_n, (24)
    D_(n,kappa)=theta_(L_n)
       *exp(A_(L_n)*[log(B_n)+8*L_n*T_n+kappa*n]).              (25)

Indeed, with theta=theta_(L_n), the non-tail term of (23) equals
(exp(-kappa*n)*V)^(1-theta) times
([(B_n*exp(8*L_n*T_n+kappa*n))^((1-theta)/theta)
*epsilon_n])^theta. The weighted mean inequality bounds this by
(1-theta)*exp(-kappa*n)*V plus theta times the second bracket.
Together with the tail estimate this is (24)-(25), including V=0
by direct evaluation.

The rate comparison is explicit. For fixed kappa>0 and the fixed
constant C_K, let

    alpha_kappa=(3/(4*pi))*(9/32+kappa)>0.

From (18), (22) and the definition of L_n,

    log(B_n)=(9/32)*n+O(log n),
    L_n=alpha_kappa*n+O(log n),
    A_(L_n)=log(n)/log(2)+O(1),
    log D_(n,kappa)
       =(18*alpha_kappa/log(2))*n^2*log n+O(n^2).              (26)

For the last line, T_n=(9/4)*n+O(1), so
8*L_n*T_n=18*alpha_kappa*n^2+O(n*log n). Multiplying by A_(L_n)
gives the displayed leading term. The other terms in (25), and
log theta_(L_n)=O(log log n), are absorbed by O(n^2).
In particular this ACTUAL DISPLAYED coefficient satisfies

    log(D_(n,kappa))/n -> +infinity,                          (27)

whereas the sought certificate needs that ratio to tend to zero.
For any fixed delta>0, D_(n,kappa)*exp(-delta*n) tends to infinity.
Thus (24) pays the decaying TV term but cannot turn the assay's
allowed competing bound C*exp(-delta*n) into a contradiction. These
are rates of the proved upper certificate, not lower bounds on the
optimal amplification, the actual leakage, or the minimum filter TV.

The full-quartet analytic relation and its auxiliary term are now
accounted for within this particular test. The remaining failure is
quantitative: this positive strip transfer plus the available disk
propagation estimate uses a boundary interval of length proportional
to n to pay its tail, and its resulting amplification is far above
subexponential. Sharper propagation, a different realization or a
successful filter is not excluded. The exact assay remains undecided.
This is the third mathematical EXPLORATION among trials314/315/318;
step316's audited subclass NEGATIVE is preserved, with no supervisor
counter reset asserted. Park this tested propagation certificate and
reassess the general mechanism before another attempt. No actual-Xi
positivity, signed forcing, reconstruction or RH conclusion follows.

## Mathlib

Full matching coverage of this exact quartet feasibility problem and
its weighted dual norm is unchecked and unknown. Hahn–Banach and
Riesz–Markov–Kakutani are supporting named results, not matching theorems
for this kernel. Their precise Mathlib names were not checked here.
No claim of absence or formal verification is made.
The step315 interpolation and residual-transfer specialization is
also unchecked in Mathlib; no matching-coverage or absence claim is made.
The step318 strip-transfer and Kovrijkine specialization is also
unchecked in Mathlib; no formal verification or full matching theorem
is claimed. Its supporting input is the cited analytic propagation
lemma and the residue theorem, not a theorem deciding this assay.
