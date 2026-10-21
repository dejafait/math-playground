# L172 — Exact IBP evaluates the third trace and the complete E,E sector

## Hypotheses

Keep L171's hypotheses and established limit for the third ordered
trace Z_i, for SU(2), D=(-4,4)^4 with all-face relative fixed links,
a=8/N through admitted even meshes, straight direction-1 lower-rooted
forest, L008's complete compact displacement, both actual L010 probes
i=3,6 at tau=1/16, and bare expansion at fixed mesh before refinement.
Import L171(1)--(2)'s complete scalar and physical reduction, and
L145's identity K_(i,R)=g_G B_(i,R). No new mesh limit is taken for Z_i.
All rough directions, colors, the projection and actual-prefix
half-weight are already retained in L171; none is changed here.

For the E,E assembly use exactly L161(3)'s six signed traces,
L161/L162's two subcubic double-gradient groups, L164's first-trace
zero limit and L168/L169's fourth/second limits. F=Phi Sigma remains
a cross matrix and E signed/correlated. Both insertion subtractions,
action faces, pinned end links, upper jump, constant modes and complete
heat spectrum retain the qualifications of those inputs.

The analytic identities below have no numerical premise. Quantitative
actual-probe intervals import L141's exact g_G enclosure and L146's
complete R intervals, with the latter's stated IEEE binary64/FMA,
no-overflow, underflow, moment/time and informal computer-assisted
qualifications. No independent processor/BLAS verification is claimed.

## Conclusion

The universal scalar is exactly

    z_Z=-(9/2)g_G,             387/2000<z_Z<549/2000.       (1)

Consequently the complete third ordered trace has cubic limit

    lim a^3 Z_i=K_(i,Z)=-(9/2)K_(i,R),                    (2)

and the entire E,E sector has limit

    lim a^3 H_i^EE=-6 K_(i,R),                    i=3,6. (3)

Under the imported heat arithmetic qualifications, the strict bounds are

| Probe | Third trace lower | Third trace upper | E,E lower | E,E upper |
| --- | ---: | ---: | ---: | ---: |
| 3 | 237.6405 | 337.122 | 316.854 | 449.496 |
| 6 | 87.372 | 123.9525 | 116.496 | 165.27 |

Thus this entire E,E sector is positive at cubic scale for both actual
probes under those qualifications. This does not determine the complete
cubic residual/action response: L158/L159's mixed branches T_i,V_i
still lack scaled limits/coefficients. If those limits exist, vanishing
of the complete response requires their sum to equal 6 K_(i,R).
The remaining response jets, full compensation, finer powers/logarithm,
finite matching, interacting reflected error <=c_box/2 and continuum/
infrared finite positive mass requirements remain unresolved. No
candidate Yang--Mills solution exists. This is local standard-method
REPRODUCTION under the unchanged ready EXPLORE assessment, with no
claim of progress beyond the sources checked.

## Proof

### 1. A complete rational numerator identity

All torus integrals use normalized measure. Put X_j=2-2cos(theta_j)
for j=2,3,4, lambda=sum X_j, S_m=sum X_j^m and p=X_2 X_3 X_4.
Let n be exactly L171(1)'s numerator. Define

    A=sum_(j<k) X_j X_k (X_j-X_k)^2=lambda S_3-S_2^2,
    D=(10lambda-lambda^2)S_2-2lambda S_3+S_2^2.

Then the following is an exact polynomial identity:

    18n=lambda^2(S_2/2-3lambda/2)+(3/8)A+(1/4)D.         (4)

To check it without any numerical evaluation, substitute L171's n.
Its degree-three part is (5/2)lambda S_2-(3/2)lambda^3,
which equals the degree-three part of the right side. The latter's
degree-four part is lambda^2 S_2/4-lambda S_3/8-S_2^2/8.
Subtract the degree-four part of 18n: the result is one quarter of

    lambda^2 S_2-2lambda S_3-S_2^2+2S_4-2lambda p=0.     (5)

Identity (5) follows by expanding in the three X variables. The
X_j^4 coefficient is 1-2-1+2=0; each ordered X_j^3 X_k
coefficient is 2-2=0; each X_j^2 X_k^2 coefficient is
2-2=0; and each X_j^2 X_k X_l with distinct indices has
coefficient 2-2=0. These exhaust degree four. Likewise expansion
over unordered pairs proves the displayed formula for A. Thus (4)
uses the whole signed numerator, not a pointwise sign estimate.

### 2. Justify periodic integration by parts at the origin

For lambda>0 set f=S_2/lambda, and extend it by zero at the origin.
Since 0<=S_2<=lambda^2, f<=lambda=O(|theta|^2) there. Also

    partial f/partial X_j=(2X_j lambda-S_2)/lambda^2,
    |partial f/partial X_j|<=3.

Hence partial_(theta_j) f=2sin(theta_j) partial_(X_j) f tends
to zero at the origin. The bound f=O(|theta|^2) proves differentiability
there with derivative zero; the derivative bounds prove continuity.
Thus f is a C^1 periodic function on T^3, smooth away from the sole
torus point lambda=0. In particular the periodic C^1 vector components
2sin(theta_j)f can be integrated by parts over the whole torus.

Using 2cos(theta_j)=2-X_j and
4sin^2(theta_j)=X_j(4-X_j), calculate

    sum_j partial_(theta_j)[2sin(theta_j)f]
      =sum_j [(2-X_j)S_2/lambda
               +X_j(4-X_j)(2X_j lambda-S_2)/lambda^2]
      =D/lambda^2.                                    (6)

The derivative is continuous, including at the origin, and its torus
integral is zero. No small ball, singular boundary flux or origin cell
is omitted. Every other quotient in (4) is also integrable:
A<=lambda^4, so A/lambda^2<=lambda^2, and the polynomial part is
bounded. Divide (4) by lambda^2 and integrate.

The exact one-angle moments are integral X_j=2 and integral X_j^2=6,
using integral cos(theta)=0 and integral cos^2(theta)=1/2. Therefore
integral lambda=6, integral S_2=18, and the polynomial part has mean
18/2-3*6/2=0. Equation (6) removes only the divergence part. Transverse
permutation symmetry makes the three unordered-pair integrals in A
equal. L145's precise scalar definition consequently gives

    integral A/lambda^2
       =3 integral X_2 X_3(X_2-X_3)^2/lambda^2=-12g_G.

By L171, z_Z=18 integral n/lambda^2. Equation (4) now yields
z_Z=(3/8)(-12g_G)=-(9/2)g_G. This is an integral identity; the
integrands are not asserted pointwise proportional. L141's strict
-61/1000<g_G<-43/1000 proves the strict scalar bounds in (1).
L171 and L145 give (2) without any new physical tensor or heat sum.

### 3. Restore all six E,E trace coefficients once

The first four terms in L161(3) are, in their original order, W_i,Y_i,
Z_i,X_i, with coefficients -36,-12,-6,-1 already included. L164
proves a^3 W_i->0. L169 gives a^3 Y_i->-3K_(i,R), (2) evaluates
the third, and L168 gives a^3 X_i->(3/2)K_(i,R). L161's fifth
term is O(N) and L162 bounds the sixth by O(N^(5/2)); since a=8/N,
both cubic-scaled limits are zero. Their finite signed sum thus has
limit

    [0-3-9/2+3/2+0+0]K_(i,R)=-6K_(i,R).

This proves (3) with no additional outside factor 3. Multiplication
of L146's strict intervals (-74.916,-52.809), (-27.545,-19.416)
by -9/2 and by -6, reversing endpoints, gives the table. No stronger
arithmetic premise is introduced by the rational multiplications.

The conditional statement about the full response follows from the
existing L159(3) assembly H_i=T_i+V_i+H_i^EE+O_i(N). Multiplication
by a^3 removes its O(N) error; if both mixed limits exist, the complete
limit is lim a^3 T_i+lim a^3 V_i-6K_(i,R). This states the remaining
condition, without assuming those limits or their value.

### 4. Exact verification evidence

Reproduction command from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_third_trace_scalar_ibp.py

The full certificate is
scripts/combined-ward-response/third-trace-scalar-ibp-certificate.json.
It records the entire target numerator, all tested polynomial columns,
rational elimination, actual polynomial and zero residual. A separate
direct construction checks (4) over all monomials, without using the
elimination coefficients. It also computes the one-angle moments as
exact constant Laurent coefficients, checks scalar endpoints, all
third/E,E endpoint multiplications and direct products with L146's
B_R intervals. All failures are empty. Complete load-bearing compact
identity, moments, results and failure fields were inspected. No
floating arithmetic, quadrature or sampled-angle evidence enters
these new checks. The analytic C^1/IBP argument above, not the finite
coefficient certificate alone, justifies the integral identity.

## Mathlib

Full matching third-scalar and E,E evaluation: **not checked**.
Supporting periodic C^1 integration by parts, trigonometric moments,
polynomial algebra and rational interval multiplication: **not checked**;
unknown availability is not absence. No new external theorem is imported
or general Ward/flow theorem reproved. The unchanged ready assessment
`drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md` covers
the complete target. This specialization evaluates its already-derived
scalar by explicit calculus; L141/L145/L146 and the established trace
limits are imported only within their recorded hypotheses.
