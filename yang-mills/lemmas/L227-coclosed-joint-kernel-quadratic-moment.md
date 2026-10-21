# L227 — A uniform quadratic moment for the frozen co-closed resolvent product

## Hypotheses

Use L088 and L090's complete frozen transverse alternating stencil on
the infinite four-dimensional grid, with real normalized exterior vector
v=(v_2,v_3,v_4). The corresponding stored exterior is av. This is a
bulk comparison operator, not a replacement of the finite relative box.
The intended finite application is L226's exact T_(epsilon,delta), for
SU(2), the lower-rooted direction-1 forest, a=8/N, admitted even N,
tau=1/16 and actual probes i=3,6. The bare expansion remains fixed-mesh
first. No finite boundary comparison is assumed in this lemma.

On theta in [-pi,pi]^4 write

    d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2),
    h=sum_(j=1)^4 d_j^2, lambda=sum_(j=2)^4 d_j^2,
    r=sqrt(lambda), w_j=v_j eta_j,
    Q_delta^c=I-d_T d_T^T/(lambda+delta),
    Omega_v^c=2i[2(w dot d_T)I-d_T w^T-w d_T^T].        (1)

Here 0<epsilon,delta<=1. Superscript c denotes component-center
phases. Omega_v^c is the complete normalized frozen stencil of
L088(11)--(13), with the sum over planes evaluated in L109(4).
It contains both original two-edge paths. The actual frozen exterior
circulation is zero; the nonconstant exterior-circulation terms of the
finite trace remain accounted for by L089, not by (1).

For integer-index Fourier phases let U=diag(exp(i theta_j/2))_(j=2)^4
and set Q_delta=U Q_delta^c U*, Omega_v=U Omega_v^c U*. Define

    J_(v,epsilon,delta)(theta)
        =Q_delta Omega_v Q_delta^2/(h+epsilon).         (2)

Thus a J is exactly the frozen product H_v^delta K_(epsilon,delta)
from L090(14); its adjoint represents the reversed transposed product.
Let j(z), z in Z^4, be the inverse Fourier coefficients of (2), with
normalized torus measure and convention exp(i z dot theta).
All matrix norms below are Frobenius norms unless marked otherwise.

For the commutator statement let b:R^4->R be bounded and globally
Lipschitz with constant L, and let M_b multiply all three integer-index
components at x by b(ax). Let Lambda be any finite set of integer
output cells, and R_Lambda restrict outputs to those cells. This is
a common-index scalar multiplier; it is not an identification of the
different actual staggered coefficient placements.

## Conclusion

With a universal constant independent of epsilon, delta and v,

    sum_z ||j(z)||_F^2 <= C |v|^2,
    sum_z |z|^2 ||j(z)||_F^2
                         <= C |v|^2 log(e/epsilon).     (3)

Both bounds also hold for the adjoint convolution kernel. In particular,

    ||R_Lambda [M_b,J]||_HS
        <= C a L |v| sqrt(|Lambda| log(e/epsilon)),     (4)

and, for R>0, the kernel restricted to |x-y|>R obeys

    ||R_Lambda J_(>R)||_HS
        <= C |v| sqrt(|Lambda| log(e/epsilon))/R.       (5)

If |Lambda|<=C_0 N^4, a=8/N, epsilon=N^-1 and
delta=N^(-4/3), then

    ||R_Lambda [M_b,aJ]||_HS
                   <= C sqrt(C_0) L |v| sqrt(log(eN)). (6)

The same estimate holds for the adjoint. The absence of an inverse
power of delta in (3)--(6) is the relevant partial advance. Coupling
a commutator of exactly this form to factors of Hilbert--Schmidt norm
O(p(l)N) and operator norm O(N) would give O(N^2 sqrt(log(eN)))
by the trace inequality. Those are the sizes in L090/L226, but this
lemma does not express every error of their actual trace in that form.

In particular it supplies neither the requested complete-sector
O(N^(5/2)log(eN)^2) bound nor a finite relative-boundary comparison.
The separate critical audit in proof section 5 accepts these kernel
and localized consequences relative to the imported complete stencil.
The variable-coefficient factorization, intervening projections, both
generator orientations and all actual staggered placements remain
obligations. Independent response rates, interacting reflected error
<=c_box/2, continuum axioms and finite positive mass stay open.

## Proof

### 1. Retain periodic phases and the transverse derivative

Formula (1) is imported from the complete path calculation L088 and
its plane sum L109, rather than inferred from an individual generator
filter. In center phases Q_delta^c is a positive contraction: it is
one on the orthogonal complement of d_T and delta/(lambda+delta)
on its span. Thus the same holds for Q_delta.

The unshifted symbols are periodic, even though U alone is not.
Indeed, for t_j=exp(i theta_j)-1,

    U d_T=-i t,  Q_delta=I-t t*/(lambda+delta).

For Omega, its diagonal entries are sums of v_j sin(theta_j).
Every off-diagonal entry is a linear combination of products

    (exp(i theta_j/2)d_j)(exp(-i theta_k/2)eta_k),
    (exp(i theta_j/2)eta_j)(exp(-i theta_k/2)d_k).

Their four factors are respectively (exp(i theta_j)-1)/i,
(1+exp(-i theta_k))/2, (1+exp(i theta_j))/2 and
(1-exp(-i theta_k))/i. Hence they are periodic trigonometric
polynomials. This also verifies that no phase jump is introduced
when taking a torus derivative. The scalar h is periodic.

For each transverse coordinate, differentiating d_T d_T^T and
lambda gives, in center phases,

    ||partial Q_delta^c||_op
       <= C[r/(r^2+delta)+r^3/(r^2+delta)^2]
       <= C r/(r^2+delta),
    r ||partial Q_delta^c||_op <= C.                   (7)

For the axial coordinate its derivative is zero. The finite formula
for Omega in (1) gives

    ||Omega_v^c||_F<=C|v|r,
    ||partial Omega_v^c||_F<=C|v|.                     (8)

These estimates include r=0 by continuity at positive delta.
When differentiating the unshifted conjugation, derivatives of U
and U* have bounded norm. Their additional terms are bounded by
C||Omega_v^c||_F for the entire projected numerator. In particular,
if B=Q_delta Omega_v Q_delta^2, (7)--(8) and the product rule give

    ||B||_F<=C|v|r,
    ||partial B||_F<=C|v|.                            (9)

For clarity, a derivative on any of the three projection factors
costs at most C r/(r^2+delta) before multiplication by Omega's
O(|v|r). Their product is O(|v|r^2/(r^2+delta)), hence uniformly
O(|v|). All other projections are contractions. This is the precise
place where keeping the alternating stencil with the resolvent and
projections avoids an inverse delta power. It is not a bound for
an isolated projection derivative in operator norm.

### 2. Integrate the full four-dimensional derivative bound

Since |partial h|<=2 sqrt(h), (2) and (9) imply

    ||J||_F<=C|v|sqrt(h)/(h+epsilon),
    ||partial J||_F
       <=C|v|[1/(h+epsilon)+r sqrt(h)/(h+epsilon)^2]
       <=C'|v|/(h+epsilon).                           (10)

The last step uses r<=sqrt(h) and h/(h+epsilon)<=1. It is uniform
in both masses, including delta much smaller than epsilon. In the
fundamental cube, with rho=|theta|,

    (4/pi^2)rho^2<=h<=rho^2.

Integration over an enclosing four-dimensional ball now gives

    integral ||J||_F^2 <= C|v|^2 integral_0^(2pi) rho d rho
                       <= C'|v|^2,
    integral sum_j ||partial_j J||_F^2
       <= C|v|^2 integral_0^(2pi) rho^3/(c rho^2+epsilon)^2 d rho
       <= C'|v|^2 log(e/epsilon).                     (11)

All integrals here use normalized torus measure, absorbed in C.
For the first bound use h/(h+epsilon)^2<=1/h away from the single
point h=0. For the second split at rho=sqrt(epsilon). Below that
point the integral is bounded by epsilon^-2 times its fourth power,
hence by a constant. Above it the majorant is C/rho, giving
C[1+log(1/epsilon)]. No transverse or axial mode is removed from
the integral, and the set lambda=0 causes no singular term at
positive delta. This is a bulk Fourier estimate, not a claim about
the finite relative component zero modes.

For positive masses the periodic symbol is smooth. The standard
Fourier-series Plancherel theorem applied to each entry and each
derivative identifies the two integrals in (11) respectively with
sum_z ||j(z)||_F^2 and sum_z |z|^2||j(z)||_F^2. This proves (3).
The adjoint kernel is j(-z)*, so its two sums are identical.
If distances between physical component centers are used instead,
their index displacements differ from z by a vector of uniformly
bounded length. The bound |z+s|^2<=2|z|^2+2|s|^2 and both parts
of (3) give the same logarithmic bound. Midpoint offsets are thus
retained rather than silently set to zero.

### 3. State exactly the localized operator consequences

The commutator kernel is

    (M_b J-J M_b)_(x,y)=[b(ax)-b(ay)]j(x-y).

Consequently its restricted squared Hilbert--Schmidt norm is bounded by

    sum_(x in Lambda) sum_y a^2 L^2 |x-y|^2 ||j(x-y)||_F^2
       <= C a^2 L^2 |Lambda| |v|^2 log(e/epsilon).

All input rows y remain in this sum. This proves (4). Similarly,
sum_(|z|>R)||j(z)||_F^2<=R^-2 sum_z |z|^2||j(z)||_F^2 proves
(5). Multiplying (4) by a and using a^2 N^2=64 proves (6).
Only uniform inequalities receive the varying mass schedule.
No fixed-parameter limit is evaluated at varying mass.

The conditional trace estimate after (6) is just
|Tr(X G Y)|<=||X||_HS||G||_op||Y||_HS, when a finite-trace
error has these compatible factors and X is the restricted actual
aJ commutator. Polynomial exterior amplitudes can be summed by
L088/L090's complete heat envelope when such a representation is
established for every mode pair. That representation has not been
proved here. In particular (5) bounds omitted infinite-grid rows;
it does not compare a finite relative Green function with a compressed
infinite-grid Green function. Nor does (4) permit commuting a scalar
past an intervening component stencil or replacing different
staggered multipliers by one common multiplier without an error bound.

### 4. Scope, comparison and standard inputs

This is a REPRODUCTION within the unchanged quantitative-sector
EXPLORE assessment. The standard named input is Fourier-series
Plancherel, with smooth periodic symbols checked above; the remaining
steps are finite product differentiation and integrable radial bounds.
No general matrix-decay theorem is reproved. The necessary local
specialization is the full one-alternating-stencil, one-resolvent
product (2), including all three projection factors and the original
edge phases. No originality beyond the sources checked is claimed.

L110's existing quadratic moment concerns a different product with
two circulations and an offset-by-offset axial sum. It does not
provide (3) for this one-resolvent product. L109/ATTEMPTS/032's
failure of separate first absolute moments is compatible with the
squared moment here. ATTEMPTS/030's warning about fixed-mass limits
also remains intact. This result does not settle the actual signed
trace, its physical boundary rows or complete freezing error. The
separate audit below concerns this input, not those applications.

### 5. Separate critical audit of the joint moment and its consequences

The 2026-10-18 audit accepts (3)--(6) relative to L088's complete
two-path stencil, L109(4)'s plane sum and L090(14)'s ordered product.
Those upstream results are imported rather than recursively audited.
No new rate or mathematical novelty is claimed. The checks are:

1. **Normalization, order and periodicity.** The frozen stored
   exterior is av, so H_v^delta=a Q_delta Omega_v Q_delta and
   K=R_epsilon Q_delta give H_v^delta K=aJ exactly, using only
   the scalar resolvent's commutation with Q_delta. There are three
   projection factors, not an idempotent simplification of Q_delta.
   L088(11)--(13) retains both paths before L109(4)'s full plane sum.
   For j!=k, the integer-index off-diagonal entries of Omega are
   -2i[v_k (U_j d_j)(conj(U_k) eta_k)
       +v_j (U_j eta_j)(conj(U_k) d_k)]. Each product is a periodic
   polynomial by the four identities in section 1. The diagonal
   entry is 4i sum_(l!=j) v_l sin(theta_l), also periodic.
   Q_delta=I-t t*/(lambda+delta) is periodic and smooth, including
   at lambda=0 because delta>0. Thus the conjugation by U introduces
   no seam term in Fourier differentiation, despite U itself not
   being periodic. All axial dependence is in the scalar resolvent.

2. **Every derivative placement.** For a transverse derivative,
   put d=d_T and d'=partial d, so |d'|<=1 and
   |partial lambda|=|2d dot d'|<=2r. The exact derivative is

       partial Q_delta^c
         =-(d'd^T+d(d')^T)/(r^2+delta)
            +d d^T (partial lambda)/(r^2+delta)^2.

   Its norm is at most 2r/(r^2+delta)
   +2r^3/(r^2+delta)^2 <=4r/(r^2+delta).
   In the derivative of B^c=Q_delta^c Omega_v^c (Q_delta^c)^2,
   each of the three projection placements therefore contributes
   at most C|v|r^2/(r^2+delta)<=C|v|. A derivative of Omega
   contributes at most C|v| with the other projections contractions.
   Conjugating the complete B^c adds the two phase derivative terms;
   each is bounded by C||B^c||<=C|v|r<=C'|v| on the whole torus.
   These bounds hold also on r=0 by the smooth positive-mass formulas.
   The axial derivative of B is zero. For any coordinate the quotient
   derivative then has the two terms in (10); the denominator term
   obeys r sqrt(h)/(h+epsilon)^2<=1/(h+epsilon).
   No inverse delta constant or relation between masses is used.

3. **Complete singular integrals and Fourier weights.** On the
   entire fundamental cube, h>=c|theta|^2 with c=4/pi^2.
   The unweighted norm is controlled by integral h^(-1), whose
   four-dimensional radial integrand is C rho and is integrable.
   For the derivative norm, the integral below sqrt(epsilon) is
   at most C epsilon^(-2) integral_0^sqrt(epsilon) rho^3 d rho
   =C/4. Above it the integrand is at most C/rho, giving precisely
   C[1+log(1/epsilon)]. This checks all four derivatives and retains
   the transverse line lambda=0 and every axial frequency; there
   is no omitted spectral sector or lower-dimensional replacement.
   Smooth periodic entrywise Plancherel identifies the sum of the
   four derivative norms with the full |z|^2 weight. Bounded component
   center offsets are handled using both parts of (3), as stated.

4. **Adjoint, localization and finite schedule.** The adjoint kernel
   j(-z)* has exactly the same unweighted and weighted squared sums.
   The common-scalar commutator kernel uses b(ax)-b(ay) and keeps
   all y for each restricted output x. Its Lipschitz bound therefore
   gives (4) without any support restriction on b or on the inputs.
   Markov's inequality for the weighted squared sum gives (5).
   Multiplying (4) by a gives a^2 sqrt(|Lambda|)<=64 sqrt(C_0)
   when |Lambda|<=C_0 N^4 and a=8/N, yielding (6). The same argument
   applies directly to the adjoint, without treating output restriction
   as invariant under adjunction. Only these uniform inequalities
   receive epsilon=N^-1; delta's schedule has no role in their constants.

The restricted scalar consequence is not an estimate for an arbitrary
intervening staggered multiplier or a relative Green boundary defect.
It also does not imply an absolute first kernel moment: the distinct
L109/ATTEMPTS/032 obstruction remains valid. No fixed-mass limit is
evaluated at varying mass, and no complete-sector, complete-response
or interacting estimate is established by this audit. L225--L226's
finite spectral comparisons remain separate unaudited inputs.

## Mathlib

Full matching result: **not checked**. Supporting Fourier-series
Plancherel, matrix product differentiation and Hilbert--Schmidt
commutator coverage: **not checked**. Unknown availability is not
evidence of absence.
