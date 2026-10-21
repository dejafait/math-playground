# L081 — Finite continuum tensor reduction and an explicit exterior tail

## Hypotheses

Use exactly L080's continuum diagnostic D_i, i=3,6, with L008's
orthonormal relative one-form modes f_k, lambda_k=(pi/8)^2|k|^2,
tau=1/16, the full displacement and actual physical weight
(x_1+4)u_1. Keep positive upper curvature and the lower-rooted prefix,
including the constant component-1 edge mode. No random boundary
trace is invoked. Let K>=1 be an integer and retain every mode with
each index at most K: indices 0,...,K in its component coordinate,
and 1,...,K in its other coordinates. Both exterior indices in the
double sum are restricted this way. D_i^[K] denotes that exact finite
sum, before spatial quadrature, time quadrature or machine arithmetic.

## Conclusion

Both finite continuum sums have the exact representation

    D_i^[K] = Tr(M_K F_K Q_(i,K)^A F_K),
    F_K = Delta_K^-1 exp(-tau Delta_K),                    (1)

where Q_(i,K)^A has entries q_i(f_k,f_l;Psi_13) and M_K has entries
P(f_k,f_l): the formula for P is L080(1), with f in place of A.
The superscript A changes only the probe's strain; u_1 stays actual.
There is an explicit finite tensor expansion of (1), with 12 M terms,
24 triplet Q terms and 96 shear Q terms, and respectively 28 and 72
opposing-component trace products. Its double Laplace integrals
converge absolutely and retain both inverse factors and every mode
below the cutoff, including the constant edge mode.

Define C_P=1296*1155*3/32, C_3=3025 and C_6=820368. Then

    |D_i-D_i^[K]| <= C_P C_i * 2(4*12^4)(16*12^3)
                          *512/(9K) * exp(-9K^2/1024).     (2)

In particular, at K=96 the error is strictly below 4*10^-15 for
both probes. This bounds the omitted full continuum spectrum,
not the error in evaluating the retained tensor. No numerical
continuum sign, nonvanishing, complete response/logarithm or improved
L079 remainder is claimed. L080's conditional transfer of a certified
nonzero value to the selected a^-3 coefficient remains available.
This is a local REPRODUCTION of tensor/Laplace and heat-tail methods
for the actual boundary/prefix specialization, not an originality claim.

## Proof

### 1. Exact finite-mode trace and tensor factors

Put r=rho and f(x)=x rho(x). The Psi_13 displacement is

    u_1=f tensor r tensor f' tensor r,
    u_3=-f' tensor r tensor f tensor r,
    u_2=u_4=0.                                           (3)

Derivatives in the corresponding coordinate give w_mu=partial_mu u_mu
and s_mu nu=partial_mu u_nu+partial_nu u_mu. Every coefficient is a
signed sum of products of r,r',f,f',f''. These are the actual analytic
continuum derivatives, not mesh differences. L071 and L080 remove
the Psi_24 sector from the full diagnostic. The same cancellation
holds at this rectangular cutoff: the swap of coordinates 2 and 4
preserves its mode set, heat eigenvalues, physical weight and prefix,
and negates only that probe sector. Thus it is valid to use Q^A here
without changing either D_i or its rectangular truncation.

Let b_(alpha,j,n) be e_n in coordinate j=alpha and v_n otherwise,
with exactly L080's normalization. To describe all tensors explicitly,
represent a curvature row F_mu nu on input component nu by the product
of b's with b_mu replaced by b'_mu, with sign +1; on input component
mu replace b_nu by b'_nu, with sign -1. No other component contributes.
For reversed orientation negate this row. These are precisely the
two terms of partial_mu A_nu-partial_nu A_mu.

For any signed product coefficient c(x)=sigma product_j c_j(x_j)
and two such row products L_k(x)=product_j l_(j,k_j)(x_j),
R_l(x)=product_j r_(j,l_j)(x_j), define their matrix contribution by

    sigma product_j I_j,   (I_j)_(mn)=
                 integral_(-4)^4 c_j(x) l_(j,m)(x) r_(j,n)(x) dx. (4)

This specifies ordinary tensor matrices on component blocks; derivative
frequencies and all one-dimensional normalizations are inside l and r.
For Q_3 apply (4) to every curvature row paired with itself and the
coefficient terms w_mu+w_nu, over mu<nu. For Q_6 apply it to rows
F_mu alpha and F_nu alpha, alpha outside {mu,nu}, with coefficient
s_mu nu and factor 1/2, then include the transposed pairing with
the same factor. This is exactly the symmetric polarization of
L008(1),(6). In the continuum the plaquette average and clover have
the common stated differential limit already proved in L008/L080.
They are not replaced at finite lattice spacing.

For M use the upper and lifted rows of L080, now applied to f:
on input component mu, the upper row's axial factor is
v'_n(4) replicated constantly in x_1 and its other factors are
b_(mu,j,n); on input component 1 it is -e_n(4) replicated axially,
with transverse factor v'_n in coordinate mu and v in the other two.
The lifted row on input mu is just its ordinary product mode.
On input 1 it is the negative product with axial factor

    p_0(x_1)=(x_1+4)/sqrt(8),
    p_n(x_1)=sin(n pi(x_1+4)/8)/(2 n pi/8), n>=1,        (5)

and transverse factor v'_n in coordinate mu. These are the exact
integrals of the e_n modes from -4, not a bulk-profile approximation
or an imposed upper value of the pinned potential. Pair all four
upper/lifted component combinations for each mu=2,3,4 by (4), with
coefficient product ((x_1+4)f, r, f', r). This gives exactly P(f_k,f_l).
In particular v'_n(4)=(n pi/16)(-1)^n has its positive upper derivative
sign, and e_0(4)=1/sqrt(8) and (5) keep the constant axial mode.

Distributing these instructions gives 12 M terms. The two nonzero w's
each occur in three unordered planes, with four row pairings each,
giving 24 Q_3 terms; the two contributions that cancel in plane 13
are retained as distinct terms. There are six signed coefficient
summands among the five nonzero shears (two in s_13); each has two
alpha choices, two polarization orders and four component row pairs,
giving 96 Q_6 terms. Matching reversed component blocks with M gives
28 and 72 products respectively. These counts are descriptions of
the displayed expansion, not hypotheses about nonzero floating values.

Because Q_(kl)=sqrt(lambda_k lambda_l)(B_i)_(kl) and
M_(kl)=sqrt(lambda_k lambda_l)P_(kl), the diagonal F entries
exp(-tau lambda_k)/lambda_k give (1); symmetry of Q permits the
unsymmetrized M. No color factor or torus constant gamma enters.
For each positive lambda,

    exp(-tau lambda)/lambda=integral_tau^infinity exp(-t lambda) dt.

The least full eigenvalue is at least 3 pi^2/64>0. At finite K all
matrix products and integrals converge absolutely; therefore this
scalar Laplace identity may be inserted on both sides of Q. The
component heat is the tensor product of four diagonal one-dimensional
heats, with entries exp[-t(n pi/8)^2]. Thus a matched M_(alpha,beta)
and Q_(beta,alpha) product contributes exactly

    coefficient * integral_tau^infinity integral_tau^infinity
      product_(j=1)^4 Tr[M_j E_(beta,j)(t) Q_j E_(alpha,j)(s)] dt ds. (6)

The elementary identities for products and traces of tensor matrices
prove (6) directly by expanding their diagonals. This is the continuum
specialization of L072's finite construction; its continuous derivative,
boundary and prefix factors have been explicitly justified above.
No general flow-renormalization theorem is reproved or used to assign
a value to this trace.

### 2. Explicit coefficient bounds

Here are coarse global bounds sufficient to make the exterior tail
effective. On a transition interval set a(x)=b(9-x^2),
c(x)=b(x^2-25/4), S=a+c and r=a/S. The two positive b arguments
sum to 11/4. One is at least 11/8, so S>=exp(-8/11)>1/3,
using e<3. For t>0, write z=1/t. Then

    |b'(t)|=z^2 exp(-z)<=4/e^2<1,
    |b''(t)|<=z^4 exp(-z)+2z^3 exp(-z)
                  <=256/e^4+54/e^3<23,

using e>2 and the maximum of z^m exp(-z) at z=m. The same
derivatives extend by zero at t=0. Since |x|<=3 wherever these
transition derivatives are used, |a'|,|c'|<=6 and
|a''|,|c''|<=36*23+2=830. Differentiating r=a/S gives

    |r'|=|(1-r)a'-r c'|/S<=18,
    r''=((1-r)a''-r c''-2r'S')/S,
    |r''|<=3(830+2*18*12)=3786.                         (7)

Outside the transitions r is constant, so these are global bounds.
Consequently |f|<=3, |f'|<=55 and |f''|<=11394. Equation (3) gives
|u_1|<=165. On its support x_1+4<=7, hence |(x_1+4)u_1|<=1155.

The only nonzero diagonal strains in the A sector are
w_1=f' tensor r tensor f' tensor r and w_3=-w_1. Thus
max_(mu<nu)|w_mu+w_nu|<=3025. The 13 shear is bounded by
2*3*11394=68364; the other nonzero shears are bounded by
3*18*55=2970. For q_6 there are twelve curvature products in total;
bounding each |XY| by (X^2+Y^2)/2 and then by the full two-form
norm squared yields ||M_6^A||<=12*68364=820368. Also
||M_3^A||<=3025. L008's ||d Delta_1^-1/2||<=1 therefore gives
||B_i^A||<=C_i. These are bounds for the actual retained A sector,
not an assertion that the full two-sector coefficient has the same
operator norm; its diagnostic equality was justified separately.

### 3. Bound every normalized diagnostic factor

The product amplitude of any f_k is at most 1/16, including its
constant edge factor 1/sqrt(8)<1/2. Each first derivative of
A_k=f_k/sqrt(lambda_k) has amplitude at most 1/16 because its
frequency numerator is at most sqrt(lambda_k). As |k|>=sqrt(3),
|A_k|<=1/(2 pi sqrt(3))<1/8. For each k and mu, only one of
the two curvature derivatives can be nonzero (a mode has a single
component), so |U_(k,mu)|<=1/16. For a component-1 mode the
prefix derivative has absolute value at most 8/16=1/2. For a
transverse component the direct mode value is at most 1/8.
Thus |V_(l,mu)|<=1/2 for every mode and direction. The support
has volume at most 6^4=1296, so the actual signed integral satisfies

    |P_(kl)|<=1296*1155*3*(1/16)*(1/2)=C_P.             (8)

This uses the exact length-8 prefix, including n=0, and an ordinary
smooth-mode boundary evaluation. It does not assume localization of
the internal forest covariance or replace an upper potential jump.

### 4. Sum the complete omitted spectrum

Set beta=pi^2/1024>9/1024. Write
theta=sum_(n>=0) exp(-beta n^2). Since this Gaussian is decreasing,

    theta<=1+integral_0^infinity exp(-beta x^2) dx
          <=1+(16/3)sqrt(pi)<12,                        (9)

using pi<4. Allowing zero in every coordinate only enlarges the
true one-form mode sum, which is consequently at most 4*12^4.
For each coordinate omitted at n>K, its sum is bounded by

    sum_(n>K) exp(-beta n^2)
        <=integral_K^infinity exp(-beta x^2) dx
        <=exp(-beta K^2)/(2 beta K)
        <=512/(9K) exp(-9K^2/1024).                     (10)

The middle inequality follows by bounding 1<=x/K before integrating
x exp(-beta x^2). A union bound over four component choices and
four omitted-coordinate choices bounds the single-label complement
by 16*12^3 times (10). The double-label complement is contained in
the union where either label is omitted, so its heat sum is at most
twice the full single-label sum times this complement sum. Equations
(8), ||B_i^A||<=C_i and absolute convergence from L080 prove (2).
Every corner and all higher omitted indices are included.

At K=96 the exponent is exactly -81, and the prefactor excluding
C_P C_i is 2,717,908,992. The larger full prefactor is less than
3.2*10^20. To certify the decimal threshold without a machine
exponential, the positive Taylor series through degree 8 shows
e^3>20. Thus e^81>20^27=134217728*10^27>10^35,
so exp(-81)<10^-35. Hence the error is below 3.2*10^-15,
and in particular below the stated 4*10^-15 for either probe.

### 5. Retained numerical evidence and its limits

`scripts/combined-ward-response/check_continuum_first_pair.py` implements
(3)–(6), stores all component factors, rule nodes/weights and signed
trace summands, and prints previews of (2). Its stored floating
coefficients, Legendre rules and traces are not interval enclosures.
Its refinement and normalization checks are diagnostics only. The
complete retained spatial quadrature, time quadrature and arithmetic
errors must be bounded separately before assigning a sign to D_i.
The analytical threshold above requires none of those numerical values.
The retained evaluations at K=96 are approximately
(-237.28964248298,-98.87742937270). Raising the spatial rule degree
from 160 to 240 at time degree 20 changes them by about
(4.8e-12,2.5e-11); raising time degree from 20 to 28 at spatial degree
240 changes them by less than 1e-13 each. These differences are not
error bounds. At K=2 the direct complete modal formula and the double
time rule differ by at most 1.4e-15, against the declared diagnostic
tolerance 2e-10*max(1,abs(value)). All five normalization/parity
checks pass at each recorded cutoff; they do not validate the physical
sign. Full numerical evidence is in
`scripts/combined-ward-response/continuum-first-pair-K96-s240-t28-certificate.json`
and its named factor archive; the other recorded rules have separate
certificates under that directory. Reproduction commands are:

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_first_pair.py --cutoff 96 --space-degree 160 --time-degree 20 --label K96-s160-t20
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_first_pair.py --cutoff 96 --space-degree 240 --time-degree 20 --label K96-s240-t20
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_first_pair.py --cutoff 96 --space-degree 240 --time-degree 28 --label K96-s240-t28
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_first_pair.py --cutoff 2 --space-degree 160 --time-degree 20 --label K2-modal-check
```

L079's qualitative error, other placements and response jets, matching,
reflection positivity and the Yang–Mills mass gap remain unresolved.

## Mathlib

Coverage of the full forest-lifted continuum tensor and effective tail:
not checked. The scalar Laplace integral, Gaussian integral and tensor
trace identities are standard supporting facts proved or specified above;
no matching Mathlib declaration was inspected. L008, L071 and L080
supply the existing mathematical inputs. No numerical preview is
attributed to a formal verification theorem.
