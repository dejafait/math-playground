# Lemma 674: a positive-real parameter disk exceeds the angular norm budget

## Hypotheses

Use L666's complete product. Put

    q>=1 integer, n=12q+3, J=n-1, tau=J/n,
    x=-d=-5/4, R=11/8, U=R^2=121/64, t_j=j/n,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a), |u|=1.

The ratio is interpreted by its exact rational formula, including
at removable singularities of this quotient. Let psi belong to
normalized complex L2(T), and define

    A(a)=mean_u conjugate(psi(u))*W_a(u), |a|>tau.

Set h=d-tau>0 and

    a_n(z)=-tau-h*(1+z)/(1-z),
    Omega_n={a_n(z): |z|<3/4}.

For the positive-real conclusion assume A(x)=1 and Re A(a)>=0
throughout Omega_n. This is an additional open-domain condition,
stronger than positivity only on x+i[-9/20,9/20]. No displacement
vector, coefficient mass bound, or Xi realization is assumed.

## Conclusion

The action A is holomorphic on |a|>tau. The disk Omega_n lies in
Re(a)<-tau and contains the entire closed target ordinate segment
as well as a_*=-R. Every angular representer, without a positivity
assumption, satisfies the full parameter-circle attenuation bound

    sup_(|a|=R) |A(a)|
       <=(10/11)*(66/67)^(n-1)*||psi||_2.               (1)

With the additional positive-real hypothesis,

    Re A(-R)>=11/19,
    ||psi||_2 >=(121/190)*(67/66)^(n-1).               (2)

In particular no absolute C and onset can make
||psi_n||_2<=exp(n/100)*n^C hold for such positive-real actions for
all sufficiently large n=12q+3. Positivity on the whole half-plane
Re(a)<-tau also implies this obstruction. Arbitrary Herglotz measures
on the displayed disk, including singular measures, are covered.

This stops that disk/half-plane representation, not every positive-real
extension on a smaller or differently shaped domain. It does not
exclude actions nonnegative only on the required segment, prove a
counterexample to the displacement-dependent cone lower bound, or
give an estimate for the original unit-residue H. Support, realization
and actual-Xi mixed signs remain open. This result has not received a
separate critical audit; no certified originality is claimed.

## Proof

### 1. Source scope and exact action

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-positive-real-angular-separator.md`
authorizes one exact family-specific representation/cost test or a
scoped obstruction. Its inspected disk Herglotz theorem is the only
non-elementary analytic input used below. Import the named Herglotz
representation as stated in J. Bal, R. T. W. Martin and F. Naderi,
*A reproducing kernel approach to Lebesgue decomposition*, Canadian
Journal of Mathematics 77(5) (2025), 1570--1610, Section 2.1, p.1574,
DOI 10.4153/S0008414X24000488,
[published version](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/D6C85487ABC9D29C3F79208BEED1F1B9/S0008414X24000488a.pdf/reproducing_kernel_approach_to_lebesgue_decomposition.pdf).
For holomorphic F on the unit disk with Re F>=0 it states

    F(z)=i*Im F(0)+integral_T (zeta+z)/(zeta-z) dmu(zeta),

where mu is a finite positive regular Borel measure of mass Re F(0).
No absolute continuity or L2 density is required. We apply this known
formula after an explicit parameter change; we do not reprove it or
identify its measure space with the angular L2 space. Douglas range
factorization is not needed for this necessary cost bound.

L666 Section 2 gives, with no dropped factors,

    W_a(u)=(x/a) product_(1<=j<n)
       [(x-t_j*u)/(a-t_j*u)] [(U*u-t_j*a)/(U*u-t_j*x)]. (3)

The possible parameter poles are a=0 and a=t_j*u. Thus they all
have modulus at most tau. The angular denominators U*u-t_j*x
have modulus at least U-tau*d>0. On each compact subset of |a|>tau,
(3) and its parameter derivatives are uniformly bounded in u.
Since normalized L2 embeds in L1 by Cauchy--Schwarz, differentiation
under the angular integral is justified by these compact bounds.
This proves holomorphy and also fixes the pairing convention: A is
conjugate-linear in psi and holomorphic in a. No angular mean-value
formula across interior angular poles has been used.

The parked C645p continued-angular-value cost, C645o negative Gram
entry, L668 spatial inverse cost, and finite polar fits are comparisons,
not inputs. Here a varies as the pole parameter while u remains on
its actual circle; (1) is not continued evaluation at u=0.

### 2. Uniform attenuation on the parameter circle

If |a|=R and |u|=1, each factor defining B_u(a) has modulus one:

    R^2*|a-t*u|^2 = |U-t*a/u|^2, 0<=t<=tau.

This follows by expanding both squares and using |a|^2=U=R^2.
Its denominator and numerator are nonzero, since t<R. Consequently

    |W_a(u)|=|B_u(x)|, |a|=R.                         (4)

At x=-d, the squared modulus of a single factor is

    R^2*(d^2+t^2+2*d*t*c)/(U^2+d^2*t^2+2*U*d*t*c),
    c=Re u, -1<=c<=1.

The derivative of the fraction without R^2 with respect to c is

    2*d*t*(U-d^2)*(U-t^2)
        /(U^2+d^2*t^2+2*U*d*t*c)^2 >=0.

All denominators are strictly positive: U>d*t. Also U>d^2 and
U>t^2. Thus the modulus is largest at u=1, with value

    R*(d+t)/(U+d*t).

This expression increases with t, because its derivative is
R*(U-d^2)/(U+d*t)^2>0. For j>=1, t_j<1, so it is at most

    R*(d+1)/(U+d)=66/67.

The j=0 factor is exactly d/R=10/11. Multiplying all n factors
therefore gives, uniformly in u,

    |B_u(x)| <=(10/11)*(66/67)^J.                     (5)

Cauchy--Schwarz in the normalized angular measure, followed by
(4)--(5), proves (1). Neither a positive Gram entry nor a sign of
any individual W_a is assumed. The full product and denominator
angle remain in the calculation.

### 3. The positivity domain and the paid evaluation

For |z|<1,

    Re [(1+z)/(1-z)]=(1-|z|^2)/|1-z|^2>0.

Hence a_n maps the unit disk into Re(a)<-tau, and a_n(0)=x.
The inverse coordinate is

    z_n(a)=(a-x)/(a+x+2*tau).

Completing squares in |z_n(a)|<3/4 also gives the explicit bounded disk

    Omega_n={a: |a+tau+(25/7)*h|<(24/7)*h}.

On the target segment a=x+i*y this gives

    |z_n(x+i*y)|^2=y^2/(4*h^2+y^2)
       <=81/181 <9/16, |y|<=9/20,                   (6)

because h=d-tau>=1/4. The strict comparison is 1296<1629.
Thus the closed segment, including its endpoints, lies inside Omega_n.
At a_*=-R the coordinate is real and positive:

    z_*=z_n(-R)=(R-d)/(R+d-2*tau)
                =1/(5+16/n)<=1/5.                  (7)

In particular a_* also lies strictly inside Omega_n. Define
F(w)=A(a_n(3*w/4)) on the unit disk. The earlier holomorphy,
the positive-real hypothesis and the anchor normalization give
F holomorphic, Re F>=0 and F(0)=1. In the imported Herglotz
formula, the imaginary constant is zero and mu has mass one.
For real 0<=s<1 the real part of its kernel is

    Re [(zeta+s)/(zeta-s)]=(1-s^2)/|zeta-s|^2
                          >=(1-s)/(1+s), |zeta|=1.

Integrating this pointwise inequality against that positive unit
measure is precisely the required specialization. At
s=4*z_*/3<=4/15, it yields

    Re A(-R)=Re F(s)>=(1-s)/(1+s)>=11/19.             (8)

There is no assumption about boundary values or a density of mu.
Equation (1) at a=-R and |A(-R)|>=Re A(-R) now give

    ||psi||_2 >=(11/19)*(11/10)*(67/66)^J,

which is (2). This lower bound holds for every angular preimage
of every action meeting the stated open-domain condition, whether
or not its exact inverse has been constructed.

### 4. Required rate and precise stopping scope

The elementary integral bound log(1+t)>=t/(1+t) for t>=0 gives

    log(67/66)>=1/67>1/100.

Therefore every such representer satisfies

    [log||psi||_2-n/100]/log n
      >=[(n-1)/67-n/100+log(121/190)]/log n
      ->+infinity along n=12q+3.                     (9)

This contradicts every fixed polynomial allowance n^C. The test is
asymptotic, with explicit constants and all n in the family; no sampled
signs, floating computation, unknown onset or numerical inference is
used. It applies already to the bounded disk Omega_n, not only to a
positive-real extension on an unbounded half-plane.

Conversely, segment positivity by itself gives no lower bound (8).
An action positive near that segment but not throughout Omega_n may
have a small or zero value at -R. Such actions are not ruled out.
The general necessary condition (1) says any norm-budget candidate
must be exponentially small on the entire circle |a|=R; it does not
assert existence of a candidate with that property. No upper bound
on the positive-cone distance or on the actual original-residue sum
follows from this obstruction.

## Mathlib

Full matching coverage for this product-specific parameter-circle
bound, domain specialization and quantitative norm obstruction has
not been checked. The Herglotz theorem is imported from the precise
primary citation above. Cauchy--Schwarz, finite rational-function
holomorphy and the displayed elementary algebra are supporting inputs;
no unverified Mathlib theorem name or absence claim is made.
