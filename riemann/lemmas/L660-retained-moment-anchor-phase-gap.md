# Lemma 660: no retained monomial neutralizes the anchor phase

## Hypotheses

Retain L649's complete family: n>=5, x=-d=-5/4, R=11/8,
U=R^2=121/64, eta=1/100, t_j=j/n for 0<=j<n, distinct common
poles a with Re(a)=x, |a|<=R-eta and x among them. Their original
positive integer residues have total mass M<=n/3. For every |u|=1,

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_a r_a W_a(u)(a/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)zeta^k.

Keep the full grid and conjugated denominator angle. There is no
spacing, symmetry or coefficient-integrality assumption. For integer
0<=k<M, consider the normalized contribution of a variable pole near
the anchor:

    F_(k,u)(y)=W_(x+i*y)(u)*(1-i*y/d)^k,
    Lambda_n(u)=sum_(j<n) [1/(d+t_j*u)-t_j/(U*u+d*t_j)].

Thus the actual contribution to c_k is r_a/R times (x/R)^k F_(k,u)(y).
This normalization removes a constant phase, not any y-dependent
phase. The variable extension is used to differentiate at y=0;
the original pole set remains fixed as u varies. On |y|<=1/16 all
its poles x+i*y are within the permitted radius.

## Conclusion

There is a logarithm of F_(k,u) analytic near |y|<=1/16, with value
zero at y=0. Its exact anchor derivative and minimum over angles are

    (log F_(k,u))'(0)=i*(Lambda_n(u)-k/d),
    min_(|u|=1) Re Lambda_n(u)
        =Lambda_n(1)
        =sum_(j<n) [1/(d+t_j)-t_j/(U+d*t_j)]
        >n*lambda_+ > (2/5)*n,                         (1)

where

    lambda_+=log(9/5)-4/5+(121/100)log(201/121).

In particular the continuous phase, chosen to be zero at the anchor,
satisfies

    (arg F_(k,u))'(0)=Re Lambda_n(u)-k/d > (2/15)*n.    (2)

This holds for every angle and every retained monomial, even if their
selection depends on the entire pole family. Exact cancellation of
the linear anchor phase by the monomial a^k would require

    k=d Re Lambda_n(u)>n/2,                            (3)

whereas every retained k obeys k<n/3. For the whole small disk the
uniform, branch-specified expansion is

    |log F_(k,u)(y)-i*(Lambda_n(u)-k/d)*y|
                                             <=14*n*|y|^2. (4)

This excludes only an extension of L659's phase argument that tries
to replace its prescribed lattice resonance by one angle and one
phase-neutral retained monomial at the anchor. It does not exclude
resonance on discrete support, cancellation between moments, a
family-dependent polynomial combination, or a logarithmic lower bound.
Indeed, when M>=2, the degree-one polynomial

    p_u(a)=1-Lambda_n(u)*(a-x)

already makes the derivative of W_(x+i*y)(u)*p_u(x+i*y) vanish at
y=0. No uniform bound for its full-support response follows from this
local cancellation. Thus (3) is a monomial threshold, not a degree
lower bound for arbitrary polynomials.

No lower or upper estimate for H=max_u mean_zeta log|G| relative to
L649's squared-residue D is established. In particular this is not a
counterexample to the paid-arc criterion, L651's response inequality,
or RH. It is a route-specific obstruction, independently unaudited.

## Proof

### 1. Scope and prior comparisons

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
The approved target remains the paid logarithmic criterion for the
original integer family. The present calculation tests a possible
extension of the exact phase matching used in L659, addressing the
explicit continuation requirement to identify an arbitrary-support
amplitude mechanism or a quantitative obstruction to that extension.
It does not approve a new target or import an uninspected theorem.

The scoped duplicate check compared C645d's two-pole cancellation,
L647's constant-coercivity stop, the pure-power transfer in L649,
the narrow-cloud results L655/L656, and L659's resonant lattice.
Those statements do not supply (1)--(4). The elementary specialization
below is not claimed to be original beyond the sources checked.
It differentiates L649's exact product and uses a finite lower bound
for elementary real logarithms. Jensen, polynomial integrability and
the paid-arc localization are not reproved or used as premises here.
L658/L651 are downstream context, not inputs to (1)--(4).

### 2. Exact logarithm and its uniform remainder

For |u|=1 and 0<=t<1, direct division of the original factors gives

    W_(x+i*y)(u)
      =product_(j<n) [1-i*t_j*y/(U*u+d*t_j)]
                          /[1-i*y/(d+t_j*u)].         (5)

In particular t_0=0 contributes 1/(1-i*y/d); it has not been
discarded. The denominator angle in (5) is U*u+d*t_j, as obtained
by multiplying the original numerator and denominator by u.

Put A_j=1/(d+t_j*u), b_j=t_j/(U*u+d*t_j). Uniformly in u,j,

    |A_j|<=4,       |b_j|<=64/41<2,       1/d=4/5.

For |y|<=1/16 the arguments of each log(1-z) power series have
modulus at most 1/4. The analytic logarithm with value zero at y=0 is

    log F_(k,u)(y)
      =sum_(j<n) [log(1-i*b_j*y)-log(1-i*A_j*y)]
                              +k*log(1-i*y/d).        (6)

Its linear term is i*(Lambda_n(u)-k/d)*y. The convergent logarithm
series gives, for |z|<=1/4,

    |log(1-z)+z|
       <=sum_(ell>=2) |z|^ell/ell
       <=|z|^2/[2*(1-|z|)]<=(2/3)*|z|^2.

Applying this separately to all factors in (6), without replacing
their phases by moduli in the linear term, bounds the remainder by

    (2/3)*[n*(16+4)+k/d^2]*|y|^2
       <=(3032/225)*n*|y|^2 <14*n*|y|^2.

This proves (4) and the derivative in (1). For real y, the imaginary
part of this specific logarithm is a continuous phase, so its
derivative is Re Lambda_n(u)-k/d. There is no branch discontinuity.

### 3. Minimizing the exact phase slope over every angle

Write c=Re u in [-1,1]. For a fixed t=t_j,

    Re[1/(d+t*u)] = (d+t*c)/(d^2+t^2+2*d*t*c),
    Re[t/(U*u+d*t)] = t*(U*c+d*t)/(U^2+d^2*t^2+2*U*d*t*c).

All denominators are positive. Their respective derivatives in c are

    t*(t^2-d^2)/(d^2+t^2+2*d*t*c)^2 <=0,
    t*U*(U^2-d^2*t^2)/(U^2+d^2*t^2+2*U*d*t*c)^2 >=0.

For t>0 both signs are strict, since t<1<d and d*t<U.
Subtracting the second expression from the first shows that every
summand of Re Lambda_n(u) decreases with c; the t=0 term is constant.
Consequently the minimum is attained at c=1, that is u=1, proving
the exact angular minimization in (1). In particular angle selection
cannot make the phase derivative small by cancellation among grid
factors: their minima occur at this same angle.

Set f(t)=1/(d+t)-t/(U+d*t). Its derivative on [0,1] is

    f'(t)=-1/(d+t)^2-U/(U+d*t)^2<0.

The complete left Riemann sum is therefore strictly greater than its
integral, with no asymptotic error or omitted grid prefix:

    Lambda_n(1)>n*integral_0^1 f(t)dt=n*lambda_+.

Elementary integration gives the displayed value of lambda_+. To
verify its useful lower bound exactly, for 0<z<1 integrate the
geometric series for 2/(1-z^2), or use its convergent power series:

    log((1+z)/(1-z))
           >2*(z+z^3/3+z^5/5).

The omitted terms are strictly positive. With z=2/7 and z=40/161,
respectively, the two rational lower bounds are

    log(9/5)>148172/252105,
    log(201/121)>164696345840/324526850403.

Thus

    lambda_+ >651991305716/1622634252015
             =2/5+587520982/324526850403 >2/5.         (7)

Since k<M<=n/3 and 1/d=4/5, subtracting k/d from (1) proves
(2): the remaining slope is greater than (2/5-4/15)n=2n/15.
If the slope were zero for some monomial of any nonnegative degree,
its degree would have to satisfy (3). The strict gap above the
available cutoff exceeds n/6. This conclusion does not depend on
pole spacing or on the arrangement of the integer residues.

Finally, p_u(x+i*y)=1-i*Lambda_n(u)*y, so differentiating the
product W_(x+i*y)(u)*p_u(x+i*y) at zero gives
i*Lambda_n(u)-i*Lambda_n(u)=0. This verifies the stated limitation
on the monomial obstruction and prevents its extension to arbitrary
polynomial combinations. No full-support control is implicit.

### 4. Verification and effect on the approved target

The exact three-term logarithm bounds, every rational term, the slope
and degree gaps, and the remainder bound are stored in
`scripts/one-sided-hankel/retained-moment-phase-certificate.json`.
Reproduce them with

    python3 scripts/one-sided-hankel/retained-moment-phase-certificate.py

All these values and the empty failures list were inspected in full.
The arithmetic certificate does not replace the angular minimization
and branch argument above. No finite-family screen or numerical
quadrature is a premise.

The failed step is a proposed way to obtain an amplitude bound for
arbitrary support from an individually nonoscillating retained moment.
L659's prescribed discrete resonance remains valid on its hypotheses;
(2) does not contradict it. The original criterion concerns the full
spatial logarithmic mean and permits interference among all moments,
so its H-versus-D threshold and all spatial roots remain unresolved.
The next mechanism must use those data or an admissible all-angle
countersequence, rather than assert a stationary monomial at the anchor.

## Mathlib

Full matching coverage for this exact product, angle minimum and
retained-monomial phase gap has not been checked. The proof uses
elementary complex differentiation, the logarithm power series, real
monotonicity and rational arithmetic; supporting Mathlib declarations
were not inspected in this turn. This is not an absence claim, and
the rational certificate is not a Lean formalization.
