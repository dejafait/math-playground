# Corollary C032m: compact-width uniform entire lifts

## Hypotheses

Retain C032j's actual-zero normalization and all its fixed-v1 preprint
qualifications. Thus Z+ counts the nontrivial zeta zeros of positive
ordinate with multiplicity, z_rho=gamma_rho-i*delta_rho,
gamma_rho>14, |delta_rho|<1/2, and N(T)=O(T log(T+2)). For
1<=sigma<=2 use precisely

    G_sigma(z)=(4*pi*sigma)^(-1/2) exp(-z^2/(4*sigma)),
    p_sigma(z)=(1/2) sum_(rho in Z+)
                    [G_sigma(z-z_rho)+G_sigma(z+z_rho)].

Use C032k's individual entire functions R_sigma, E_sigma, O_sigma
and b_sigma, with the definitions restated below. Inherited heat
positivity, finite-zero, probability-law and counting inputs retain
their source qualifications. This is not an independent verification
of those preprints or their finite-zero data. Heat positivity is not
needed for the uniform estimates themselves. No p_sigma>=0 or RH
hypothesis is imposed.

Let eta be any real finite signed Borel measure on [1,2], and write
V=|eta|([1,2])<infinity. Its mass need not be one. Atoms, infinite
support and singular continuous parts are allowed. Width zero,
unbounded widths, distributional weights and weights depending on
the complex variable are outside the conclusion.

## Conclusion

The functions p_sigma(z), R_sigma(w), E_sigma(w), O_sigma(w) and
b_sigma(w) are jointly continuous in width and complex variable on
[1,2] times C. They are entire in the complex variable, with a bound
independent of sigma on each closed complex disk. The same is true
of each fixed-order complex derivative. Here

    R_sigma(w)=integral_0^infinity
                 (p_sigma(x)-p_sigma(i*w))/(x^2+w^2) dx,
    E_sigma(w)=4*integral_0^w t*R_sigma(t) dt,
    O_sigma(w)=2*pi*integral_0^w p_sigma(i*t) dt,
    b_sigma=E_sigma+O_sigma.

The integrand in R has its continuous removable values at w=+/-i*x,
including x=w=0. A single integrable spatial majorant for each disk,
uniform in sigma, is given explicitly in the proof. The primitives
are path independent; R and E are even, and O is odd.

Consequently the well-defined finite signed integrals

    F_eta(w)=integral_[1,2] exp(-b_sigma(w)) d eta(sigma),
    J_eta(w)=integral_[1,2]
               exp(-E_sigma(w))*sinh(O_sigma(w)) d eta(sigma)

are entire. They satisfy F_eta(0)=eta([1,2]), J_eta is odd, and

    F_eta(w)-F_eta(-w)=-2*J_eta(w).

For every integer k>=0, complex differentiation k times may be
passed through these width integrals. The proof gives finite
constants K_M, independent of eta, such that for |w|<=M,

    |F_eta(w)|, |J_eta(w)| <= V*exp(K_M).

This does not decide whether J_eta can vanish identically for mass-one
eta. It defines no mixture of probability measures, proves no
measurability of sigma -> nu_sigma(A), and asserts neither positivity
nor exponential moments of such a mixture. F_eta need not be
zero-free. No unsmoothed actual-Xi realization or all-degree sign
follows. C032l's finite-family obstruction is a contrast, not an
input to these estimates.

## Proof

### 1. Imported tools and the precise specialization

C032j supplies the displayed Gaussian and actual-zero conventions.
C032k supplies the individual lifts and their interpretation. The
underlying source is Suvrit Sra, *Some positivity properties of Riemann
Xi under smoothing*, fixed
[2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1),
Lemma A.4 and its proof, printed p.13; the Gaussian convention is
Section 3.1, printed p.5. Its individual-kernel regularity conclusion
does not itself verify a width-independent constant. The following
Gaussian bounds prove exactly that missing specialization. They
neither reprove the general admissible-kernel theorem nor import a
uniform constant from a pointwise assertion. In particular we will
use an integrable common envelope, without needing to strengthen the
individual logarithmic-growth assertion to a uniform one.

For integration of holomorphic functions use Friedrich Haslinger,
*Complex Analysis*, Section 2.7,
[Theorem 2.39 and proof, printed pp.67-68](https://www.mat.univie.ac.at/~has/scriptneu.pdf).
On a positive measure space the theorem requires measurable integrable
sections, holomorphy in the complex variable, and an integrable
dominator on each compact disk. It then gives holomorphy and
differentiation under the integral of every order. The source
statement and full proof were inspected in review1528; that coverage
is reused. Below all these hypotheses are checked, first for Lebesgue
spatial integration and then for each positive part of eta. There is
no reproof or extension of the general theorem.

### 2. Common Gaussian bounds and joint profile continuity

For Y>=0 set

    c_Y=exp((Y+1/2)^2/4)/sqrt(4*pi).

For z=u+i*v with |v|<=Y and 1<=sigma<=2, the exact Gaussian modulus
and |delta_rho|<1/2 give

    |G_sigma(z-z_rho)| <= c_Y*exp(-(u-gamma_rho)^2/8),
    |G_sigma(z+z_rho)| <= c_Y*exp(-(u+gamma_rho)^2/8).

Indeed the modulus is the prefactor times
exp(-(u-/+gamma)^2/(4*sigma)+(v+/-delta)^2/(4*sigma)).
The prefactor is at most 1/sqrt(4*pi), the negative exponent is at
most -(u-/+gamma)^2/8, and the positive exponent is at most
(Y+1/2)^2/4. All inequalities include both width endpoints.

Write a_+=max(a,0). For M>=0 define

    S_M=sum_rho exp(-(gamma_rho-M)_+^2/8),
    A_M=c_M*S_M.

These constants are finite. There are finitely many ordinates below
2M; beyond 2M the summand is bounded by exp(-gamma_rho^2/32).
The counting input makes this Gaussian sum finite. More explicitly,
on dyadic intervals [14*2^n,14*2^(n+1)) the number of terms, with
multiplicity, is O(2^n*(n+1)), while the Gaussian bound decays like
exp(-c*4^n). The same count proves

    S_G:=sum_rho exp(-gamma_rho^2/32)<infinity,
    S_2:=sum_rho gamma_rho^(-2)<infinity,

since the latter dyadic contributions are O((n+1)*2^(-n)). This
uses only the retained counting bound, not a local zero-density
estimate or a numerical truncation of the divisor.

If |z|<=M, then |u+/-gamma_rho|>=(gamma_rho-M)_+. Consequently

    sup_(1<=sigma<=2, |z|<=M) |p_sigma(z)| <= A_M.       (1)

The same summable majorant bounds the entire defining series
uniformly on [1,2] times this disk. Each summand is continuous jointly
in sigma,z and entire in z; uniform convergence makes the sum jointly
continuous and holomorphic in z. Symmetry of its definition makes it
even. Cauchy's integral formula on radius-one circles then gives, for
every k>=0,

    sup_(sigma, |z|<=M) |p_sigma^(k)(z)| <= k!*A_(M+1). (2)

The same Cauchy formula, with z+exp(i*t) as integration variable,
proves joint continuity of these derivatives. Thus derivative
control comes from the verified common larger-disk bound.

### 3. The uniform removable-part and spatial-tail bounds

For x>=0 define the nonnegative continuous envelope

    Q(x)=(c_0/2) sum_rho
                 [exp(-(x-gamma_rho)^2/8)
                    +exp(-(x+gamma_rho)^2/8)].

The preceding local convergence also applies to this real Gaussian
series. In particular |p_sigma(x)|<=Q(x), uniformly in sigma. We now
prove the weighted integrability required for R; pointwise finiteness
of Q alone would not suffice.

For any X>=1 and gamma>14, split the first translated Gaussian at
x=gamma/2. In the portion X<=x<gamma/2 (empty if X>=gamma/2), its
exponential is at most exp(-gamma^2/32), and integral_X^infinity
x^(-2) dx=1/X. In the other portion x>=max(X,gamma/2), x^(-2)
is at most 4/gamma^2; the Gaussian integral over the whole real line
is sqrt(8*pi). Hence

    integral_X^infinity exp(-(x-gamma)^2/8)/x^2 dx
       <= exp(-gamma^2/32)/X + 4*sqrt(8*pi)/gamma^2.

For the other translate, x>=X>0 gives (x+gamma)^2>=gamma^2, so

    integral_X^infinity exp(-(x+gamma)^2/8)/x^2 dx
       <= exp(-gamma^2/8)/X <= exp(-gamma^2/32)/X.

Tonelli's theorem applies to these nonnegative summands. The finite
sums just established therefore give the common bound

    integral_X^infinity Q(x)/x^2 dx
       <= c_0*[S_G/X+2*sqrt(8*pi)*S_2] < infinity.       (3)

For the compact removable portion write p_sigma(z)=h_sigma(z^2).
Evenness and the entire Taylor series define an entire h_sigma.
It is also jointly continuous in sigma and its variable. To verify
this without choosing a square-root branch, fix U>=0, put
r=sqrt(U+1), and use (1) and Cauchy's formula: the coefficients
a_(2n)(sigma) of p_sigma are continuous in sigma and satisfy
|a_(2n)(sigma)|<=A_r/r^(2n). The series
sum_n a_(2n)(sigma)*u^n then converges uniformly on [1,2] times
|u|<=U, since U/r^2<1. Pointwise, any square root of u gives

    |h_sigma(u)|<=A_sqrt(U)       (|u|<=U).

Cauchy's radius-one formula implies joint continuity of h_sigma'
and the bound

    |h_sigma'(u)|<=A_sqrt(U+1)   (|u|<=U).             (4)

Now fix M>=0 and put X=2M+1. The integrand defining R, with all
removable values, is exactly

    q_sigma(x,w)
      =integral_0^1 h_sigma'((1-v)*(-w^2)+v*x^2) dv.    (5)

For x^2+w^2!=0 this is the difference quotient. For x^2+w^2=0
it equals h_sigma'(x^2); in particular its value at (x,w)=(0,0)
is h_sigma'(0). Formula (5) is jointly continuous in sigma,x,w
and entire in w for each sigma,x. Holomorphy follows either from
the removable difference quotient or from the compact v-integral
of the entire integrand with its compact bound.

If 0<=x<=X and |w|<=M, the argument in (5) has modulus at most
max(x^2,|w|^2)<=X^2. By (4),

    |q_sigma(x,w)|<=A_sqrt(X^2+1).                    (6)

This includes w=+i*x, w=-i*x and their coincident origin. For x>=X,
|w|<=M, the denominator instead obeys
|x^2+w^2|>=x^2-M^2>=3*x^2/4. Equations (1) and (3) now give
the single measurable spatial majorant

    D_M(x)=A_sqrt(X^2+1),                  0<=x<X,
    D_M(x)=4*(Q(x)+A_M)/(3*x^2),           x>=X,
    |q_sigma(x,w)|<=D_M(x).

It is integrable, and an explicit finite upper bound for its
integral is

    B_M=X*A_sqrt(X^2+1)
          +(4/3)*[c_0*(S_G/X+2*sqrt(8*pi)*S_2)+A_M/X]. (7)

Thus sup_(sigma,|w|<=M)|R_sigma(w)|<=B_M. Uniform tail convergence
follows by integrating this same D_M beyond a cutoff. Joint
continuity follows by dominated convergence for any sequence of
widths and complex arguments approaching a given pair, choosing one
disk containing that sequence. For each fixed sigma, the x-sections
are measurable, the w-sections are entire, and D_M verifies every
compact-disk domination hypothesis of Haslinger Theorem 2.39 on
Lebesgue measure on [0,infinity). It makes R_sigma entire. The
removable expression is even in w, as is R. This is the same R as
in C032k, since the integrands and removable values agree.

### 4. Primitives and the signed width integrals

The entire primitives in C have no path ambiguity. Using straight
segments gives the jointly continuous representations

    E_sigma(w)=4*w^2*integral_0^1 v*R_sigma(v*w) dv,
    O_sigma(w)=2*pi*w*integral_0^1 p_sigma(i*v*w) dv.

Their common bounds on |w|<=M are

    |E_sigma(w)|<=2*M^2*B_M,
    |O_sigma(w)|<=2*pi*M*A_M,
    |b_sigma(w)|<=K_M:=2*M^2*B_M+2*pi*M*A_M.           (8)

Their derivatives and values at zero give E even, O odd and
E(0)=O(0)=b(0)=0. Joint continuity and common bounds for every
complex derivative of R,E,O,b follow again by Cauchy's radius-one
formula from the larger-disk bounds. These statements hold also
at the two width endpoints and at w=0.

Both kernels in F_eta and J_eta are jointly continuous, hence have
Borel measurable width sections. They are entire in w for each
sigma. For |w|<=M, (8) and the power series bound
|sinh(z)|<=sinh(|z|)<=exp(|z|) yield

    |exp(-b_sigma(w))|<=exp(K_M),
    |exp(-E_sigma(w))*sinh(O_sigma(w))|<=exp(K_M).       (9)

Use the Hahn-Jordan decomposition eta=eta^+-eta^-. Both positive
measures are finite, and eta^++eta^-=|eta|. The constant in (9)
is integrable against each. Apply Haslinger Theorem 2.39 separately
to each positive part for each kernel. All its hypotheses have
just been checked, so subtraction gives the two entire signed
integrals and differentiation under them of every order. In
particular this does not presume a theorem stated only for positive
measures applies directly to a signed measure. Absolute integrals
against |eta| give the stated bound V*exp(K_M).

At w=0 the first kernel is one and the second is zero. Evenness of
E and oddness of O make the J kernel odd and give, pointwise in
sigma,

    exp(-b_sigma(w))-exp(-b_sigma(-w))
       =-2*exp(-E_sigma(w))*sinh(O_sigma(w)).

Each term is absolutely integrable against |eta| for fixed w by
(9); integrating proves the claimed identity. No moment integral,
width-dependent probability kernel or infinite linear-independence
assertion is used. This completes the analytic specialization only.

### Critical audit1531, 18 November 2026

The compact-width analytic conclusion passes an independent conceptual
audit under the stated divisor and counting inputs. This checks (1)-(9)
and their measure-theorem interfaces; it is not an independent audit of
the external preprints, their finite-zero data, or C032k's probability
claims. The primary-source coverage for Haslinger Theorem 2.39 and Sra
Lemma A.4 cited above is reused. No stronger source statement is needed.

For the Gaussian modulus, all three estimates are simultaneous on the
closed interval: (4*pi*sigma)^(-1/2)<=1/sqrt(4*pi),
1/(4*sigma)>=1/8 in the negative exponent, and
1/(4*sigma)<=1/4 in the positive exponent. The two summands in p each
have the S_M majorant; their sum and the factor 1/2 give exactly A_M,
not 2*A_M. The same factor remains in Q. Dyadic zero counting includes
multiplicity. After finitely many initial ordinates, S_M is bounded
by the summable Gaussian series S_G; the inverse-square series has
dyadic bound O((n+1)*2^(-n)). Thus all three sums are finite for every
finite M, including M=0. Uniform convergence of continuous summands
proves joint continuity, and the common radius-one Cauchy bound
justifies (2) and continuity of every fixed derivative.

For (3), if X<gamma/2, the first part is bounded by
exp(-gamma^2/32)*integral_X^(gamma/2) x^(-2) dx, which is at most
exp(-gamma^2/32)/X. If X>=gamma/2, that part is empty. In both cases
the remaining domain has x^(-2)<=4/gamma^2; extending its Gaussian
integral to all of R gives 4*sqrt(8*pi)/gamma^2. The negative-centre
translate contributes at most exp(-gamma^2/32)/X. Summing these two
estimates and multiplying by c_0/2 gives precisely (3). Tonelli is
applied to nonnegative majorants, not to a possibly signed p_sigma.
The bound contains a constant S_2 term and is not asserted to tend to
zero as X increases. Its role is integrability at a fixed cutoff.

The construction of h_sigma uses continuous even Taylor coefficients
and a geometric majorant with ratio U/(U+1)<1, including U=0. It
therefore needs no continuous choice of square root. Choosing a square
root separately at each point only estimates the value of h_sigma.
For |u|<=U the radius-one circle lies in |u|<=U+1, giving exactly (4).
The segment in (5) has modulus at most max(x^2,|w|^2), so (6) follows.
At either w=+/-ix its value is h_sigma'(x^2); at the coincident origin
it is h_sigma'(0)=p_sigma''(0)/2. For x>0 the former is also
p_sigma'(x)/(2*x). These are the required continuous removable values;
no principal value or contour indentation is being used.

For x>=X=2M+1, x>=2M gives
|x^2+w^2|>=x^2-M^2>=3*x^2/4. Hence the tail part of D_M dominates
the full numerator by Q(x)+A_M. The compact part covers x<X, and the
tail formula also covers the joining point x=X. Its integral is at
most B_M in (7). This one measurable integrable D_M, fixed for the
whole disk and every width, gives

    sup_(sigma, |w|<=M) integral_T^infinity |q_sigma(x,w)| dx
      <= integral_T^infinity D_M(x) dx -> 0.

This last limit follows from integrability of D_M, not by taking a
limit in the coarse right side of (3). On bounded spatial intervals
(5) supplies joint continuity. Together they justify dominated
convergence for any convergent sequence of widths and complex points,
using one disk containing the sequence. For fixed x, the q-section
is entire in w; for fixed w it is continuous, hence measurable, in x.
These are precisely the section and domination premises of Haslinger's
positive-measure theorem for the Lebesgue integral defining R.

There is also a direct bound for the derivative interface: Cauchy's
formula on a radius-one circle about w, |w|<=M, gives

    |partial_w^k q_sigma(x,w)| <= k!*D_(M+1)(x),
    |R_sigma^(k)(w)| <= k!*B_(M+1).

The first majorant is integrable for every fixed k and M. Continuity
of the derivatives follows from the same larger-disk Cauchy formula
and domination. Thus no exchange of differentiation with the
noncompact spatial integral relies only on a bound for fixed width.

The straight-segment primitive formulas integrate |v| on [0,1] in E
and 1 on [0,1] in O, yielding exactly the factors 2*M^2 and 2*pi*M
in (8). They fix both primitives to zero at the origin. R is even,
so t*R(t) is odd and E is even; p(i*t) is even and O is odd. These
facts verify the sign and factor -2 in the F/J identity. Joint
continuity and the same Cauchy argument give the stated derivative
properties for E, O and b.

Finally, neither width kernel needs to be nonnegative. Each is jointly
continuous and entire in w; (9) follows from the exponential and sinh
power-series bounds. For a real finite signed Borel eta, its two
Jordan parts are positive finite measures, each dominated by |eta|.
The constant exp(K_M) is an integrable disk majorant for each part.
Haslinger's theorem therefore applies four times, once to each kernel
and each positive measure. Subtraction yields the signed integrals.
For every k>=0 their differentiated width integrands have the common
bound k!*exp(K_(M+1)), again by the radius-one Cauchy formula. Their
integrals against |eta| are at most k!*V*exp(K_(M+1)). This verifies
all derivative exchanges, including atomic and singular continuous
eta; no absolute continuity of eta or probability-kernel theorem is
needed. Evaluation at zero and integration of the pointwise parity
identity are legitimate absolute integrals.

No failed inequality or missing analytic premise was found within this
scope. The result is a checked specialization of known integration
tools, not a new general theorem. In particular this audit establishes
no mass-one annihilator, uniqueness, measurable family of probability
laws, positive mixture, moment implication or unsmoothed Xi transfer.
The qualified analytic input may be used for a later source-assessed
cancellation test; the independent main positivity gap is unchanged.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used. Gaussian, Cauchy, dominated-convergence, Tonelli and signed
measure APIs may support parts, but no coverage of this full uniform
lift or its qualified preprint inputs is asserted. This is a local
specialization of cited analytic tools, not a claim of a new general
integration theorem or a result beyond the literature checked.
