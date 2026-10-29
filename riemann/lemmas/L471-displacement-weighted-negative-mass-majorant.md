# Lemma 471: a zero-safe displacement-weighted negative-mass majorant

## Hypotheses

Use the actual Xi function of L018 and its unconditional product in
L024. All derivatives at real heights are ordinary derivatives. For
real t>=2 and T>=2 set

    D_1(Xi;t)=Xi'(t)^2-Xi(t)Xi''(t),  x_+=max(x,0),
    A(t)=(t^2+1/4)/2 * pi^(-1/4)|Gamma(1/4+it/2)|,
    Z(t)=-Xi(t)/A(t),
    N(T)=integral_T^(2T) (-D_1(Xi;t))_+/A(t)^2 dt.

Thus A is precisely the modulus of the completion prefactor in the
approved target; it is positive. L465 Sections 1 and 5 identify Z
with Hardy's function and give (log A)''=O(t^(-2)). No RH, simplicity,
positive lower bound on displacement, zero-density estimate or
external fixed-half-plane premise is assumed.

Index distinct conjugate nonreal Xi pairs by j, writing their zeros
as gamma_j +/- i d_j, with gamma_j real, 0<d_j<1/2, and equal
multiplicity m_j>=1. Each conjugate pair occurs once, including
both signs of gamma when present. Put

    q_j(z)=(z-gamma_j)^2+d_j^2,
    F_j(z)=Xi(z)/q_j(z).

F_j is a real entire function: remove just one copy of each zero,
even when m_j>1. Let P_T be the set of these pairs with
[gamma_j-d_j,gamma_j+d_j] meeting [T,2T]. It is finite. Define

    J_j(T)=[-1,1] intersect [(T-gamma_j)/d_j,(2T-gamma_j)/d_j],
    B(T)=sum_(j in P_T) m_j d_j^3
         integral_(J_j(T)) (1-v^2)
           |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|^2 dv,
    H_j(T)=sup_(v in J_j(T))
           |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|.

An interval reduced to one point has integral zero. Empty sums are
zero. The gamma factor is evaluated only at heights in [T,2T].

## Conclusion

For every t in [T,2T], including real Xi zeros,

    (-D_1(Xi;t))_+/A(t)^2
      <= 2 sum_(j in P_T) m_j (d_j^2-(t-gamma_j)^2)_+
                                  |F_j(t)/A(t)|^2.             (1)

Consequently

    N(T) <= 2 B(T)
         <= (8/3) sum_(j in P_T) m_j d_j^3 H_j(T)^2.           (2)

For L=log T, put

    R_(j,T)(v)=F_j(gamma_j+d_j v)
                   /[A(gamma_j+d_j v) L^(5/2)],
    W(T)=(1/(T L)) sum_(j in P_T) m_j (d_j L)^3
             integral_(J_j(T)) (1-v^2)|R_(j,T)(v)|^2 dv.

Exactly B(T)=T L^3 W(T). The explicit additional estimate

    sum_(j in P_T) m_j (d_j L)^3
       integral_(J_j(T)) (1-v^2)|R_(j,T)(v)|^2 dv = o(T L)     (3)

would suffice for N(T)=o(T L^3). Estimate (3) is NOT proved.
It is a sufficient weighted pair-divided second moment, not a
necessary condition for small N(T), and not a zero-count assertion.

The covered ordinary moments give the weaker actual-Xi bound

    N(T) <= (1/(8 sqrt(5))-1/24+o(1)) T L^3.                 (4)

The leading constant is strictly positive. This is an upper bound,
not an asymptotic for N(T) or evidence that its normalized mass has
a positive limit. These ordinary-moment applications do not prove
(3). More precisely, applying Cauchy--Schwarz to one pair after
replacing F_j/A by -Z/q_j gives

    2 m_j integral_(I_j) (d_j^2-(t-gamma_j)^2)
                  |F_j(t)/A(t)|^2 dt
      <= 2 m_j sqrt(1/3+pi/8) d_j^(-3/2)
                  (integral_(I_j) |Z(t)|^4 dt)^(1/2),        (5)

where I_j=[T,2T] intersect [gamma_j-d_j,gamma_j+d_j].
Thus this particular use of the ordinary fourth moment loses,
rather than bounds, the retained positive displacement power.
No full-scale upper bound for B(T), let alone (3), follows here.

This is a local application of known identities and moment theorems,
with a quantified missing estimate. It is not a new pointwise sign
theorem, a proof that (3) is false, or a solution of RH. The separate
critical application audit below finds no repair necessary; it does
not independently audit the imported moment theorems.

## Proof

### 1. Known pair identity and its actual-Xi application

Import the logarithmic-derivative identity from George Csordas,
*Fourier transforms of positive definite kernels and the Riemann
xi-Function*, [arXiv:1309.0055v2, Definition 1.1 and the proof of
Proposition 2.2, (2.3), pp. 3--4](https://arxiv.org/html/1309.0055v2).
We use the identity in that proof, not the proposition's additional
zero-free vertical interval hypothesis. The following convergence
and real-zero checks justify precisely the specialization needed
here; the kernel itself is not a new result.

L024 gives reciprocal-square summability and a locally uniform
paired product, with no quadratic exponential. On a compact disk
avoiding Xi zeros, its finite products, their first two derivatives,
and hence their logarithmic derivatives and their derivatives
converge uniformly. Indeed derivatives converge by Cauchy's formula,
and Xi has a positive minimum modulus on a slightly smaller compact
disk, so the denominators are bounded away from zero eventually.
For large zeros rho, |z-rho|>=|rho|/2 uniformly on that disk.
Thus the series of (z-rho)^(-2) converges absolutely and locally
uniformly, counting multiplicity. The finite product identity passes
to the limit. No conditionally convergent first reciprocal sum is
split or rearranged.

At a real t with Xi(t)!=0, group this absolutely convergent series
into real zeros r of multiplicity nu_r and conjugate pairs. It gives

    D_1(Xi;t)/Xi(t)^2
       = sum_r nu_r/(t-r)^2
         + sum_j 2 m_j ((t-gamma_j)^2-d_j^2)/q_j(t)^2.        (6)

For a conjugate pair the sum of its two reciprocal squares is
exactly the displayed real term. This is Csordas (2.3) with zero
quadratic-exponential parameter. L018 supplies conjugation, the
equal multiplicities and the strict displacement bound d_j<1/2.

Every real-zero term is nonnegative. A pair contributes negatively
only in |t-gamma_j|<d_j; at equality it contributes zero. Only
finitely many pairs can have a negative contribution on [T,2T]:
their zeros lie in the compact rectangle with real part in
[T-1/2,2T+1/2] and imaginary part in [-1/2,1/2]. A nonzero entire
function has only finitely many zeros in this rectangle. Removing
the nonnegative terms from (6) therefore bounds its negative part
by the finite sum of the negative pair kernels. This operation is
legitimate even if there are infinitely many nonnegative terms,
since (6) is absolutely convergent at this t.

### 2. Cancel before estimating; real zeros and integration

Multiply that bound by Xi(t)^2/A(t)^2. Since q_j(t)>0 on the real
axis and Xi=q_j F_j as an entire identity, its j-th term becomes
the j-th term of (1), with no pole. The multiplicity coefficient is
m_j, while F_j removes only one pair. Removing all m_j copies
without restoring q_j^(2m_j-2) would be incorrect.

At a real zero r, D_1(Xi;r)=Xi'(r)^2>=0, for any multiplicity.
Also F_j(r)=0 because q_j(r)>0. Both sides of (1) are therefore
zero. Thus no singular logarithmic derivative is evaluated there;
equivalently, the same extension follows by continuity. A simple
real zero may give D_1>0, but its negative part is still zero.

Integrate the finite nonnegative sum (1). In the j-th term use
t=gamma_j+d_j v. The factor d_j^2-(t-gamma_j)^2 supplies d_j^2,
and dt supplies d_j. The truncated integration interval is exactly
J_j(T), so the first bound in (2) follows, including boundary
windows and equality endpoints. Since
integral_(-1)^1 (1-v^2) dv=4/3, the supremum bound in (2) follows.
There is no infinite-sum/integral interchange in this step.

Substitution of the definition of R_(j,T) gives
d_j^3 L^5=(d_j L)^3 L^2, proving B=T L^3 W exactly. This explains
the threshold (3), without asserting any bound on its summands.
For example, only as a scaling diagnostic, if d_j L and the
displayed normalized integrals are bounded above and the summed
multiplicity is O(T L), the conclusion is merely W=O(1).
Those bounds are not assumed or proved for actual Xi; even that
diagnostic lacks the factor tending to zero required by (3).

### 3. Gauge transfer and the actual versus required moment scale

Write a=log A. Differentiating Xi=-AZ directly, including at zeros,
gives the exact identity

    D_1(Xi;t)/A(t)^2=Z'(t)^2-Z(t)Z''(t)-a''(t)Z(t)^2.       (7)

By L465 Section 5, a''=O(t^(-2)), uniformly on [T,2T] for large T.
That result includes the polynomial prefactor in A and the
paired-gamma curvature cancellation. No derivative of |Xi| or
log Xi at its zeros is used.

For the moments import H. M. Bui and R. R. Hall, *On the derivatives
of Hardy's function Z(t)*, [arXiv:2304.05178v1, 11 April 2023,
(1)](https://arxiv.org/html/2304.05178v1). Its fixed derivative
orders are ordinary t derivatives of the same Hardy function.
Taking orders (j,j), j=0,1,2, and (0,2), and subtracting the source
formulas at 2T and T, gives, with L=log T,

    M_j(T):=integral_T^(2T) (Z^(j)(t))^2 dt
       = T L^(2j+1)/(4^j(2j+1)) + O(T L^(2j)),
    integral_T^(2T) Z(t)Z''(t) dt
       = -T L^3/12 + O(T L^2).                              (8)

The monic source polynomials have fixed coefficients. Replacing
log(T/(2pi)) by L and taking the dyadic difference changes only
the one-power-smaller terms. Its error
O(T^(3/4)(log T)^(2j+1/2)) is absorbed by the displayed errors.
This is a citation application, not a reproof of those moments.

The map x -> x_+ is 1-Lipschitz, so (7) and (8) imply

    |N(T)-integral_T^(2T) (Z Z''-Z'^2)_+ dt|
       <= integral_T^(2T) |a''| Z^2 dt = O(L/T).             (9)

Drop the nonnegative Z'^2 inside the negative-part estimate, and
use x_+=(|x|+x)/2. Cauchy--Schwarz and (8) give

    integral_T^(2T) (Z Z'')_+ dt
       <= (sqrt(M_0(T) M_2(T))
                    + integral_T^(2T) Z Z'' dt)/2
        = (1/(8 sqrt(5))-1/24) T L^3 + O(T L^2).

Together with (9), this proves (4). Its strictly positive constant
shows the scale delivered by this calculation, not an obstruction
to a stronger estimate using additional arithmetic information.

### 4. Why the ordinary fourth-moment substitution loses the weight

On I_j the entire cancellation is exactly
F_j(t)/A(t)=-Z(t)/q_j(t). Let u=t-gamma_j and d=d_j. The square
of the remaining scalar kernel has full-window integral

    integral_(-d)^d [(d^2-u^2)/(u^2+d^2)^2]^2 du
       = d^(-3) integral_(-1)^1 (1-v^2)^2/(1+v^2)^4 dv
       = d^(-3)(1/3+pi/8).                                 (10)

For the last equality set v=tan theta. The integrand times dv is
cos^2(2theta) cos^2(theta) dtheta on [-pi/4,pi/4]. It expands as
(1+(3/2)cos(2theta)+cos(4theta)+(1/2)cos(6theta))/4;
integration gives pi/8+3/8-1/24=pi/8+1/3.
Apply Cauchy--Schwarz on I_j and enlarge only the scalar-kernel
integral to the full window. This proves (5), including truncated
windows. No uniform bound as d tends to zero was inserted.

Bui--Hall v1 Theorem 3, at derivative orders (0,0,0,0), supplies
integral_T^(2T) |Z|^4 dt=O(T L^4). This imported ordinary moment
is uniform in height; it is not a zero-conditioned short-window
moment. Substitution in (5) leaves d_j^(-3/2) and a sum over the
pairs. The assessed sources supply no lower displacement bound
and no compensating pair-conditioned factor for this substitution.
This precise loss stops that implementation of the summation.
The source's Proposition 3 permits deterministic shifts
O(1/log T); it does not by itself supply the zero-indexed quotient
estimate (3). Its omitted proof is not independently audited here.

Nothing here proves that every nonreal pair creates a negative
value: positive contributions discarded in (6) may mask it, as
the existing L251 countermodel illustrates. Likewise a successful
bound on N(T) would not exclude a single negative height or prove
the higher signs and global mixed positivity.

### 5. Separate critical application audit, 27 October 2026

The approved audit scope is
`drafts/literature/2026-10-27-l471-majorant-critical-audit-coverage.md`.
This audit reread L018, the complete L024 proof and L465 Sections 1
and 5, and replayed every application in (1)--(10). The following
checks find no changed conclusion or new estimate.

For the product passage, take any compact disk disjoint from the zero
set and a slightly larger zero-free disk. Locally uniform convergence
in L024 gives convergence of both derivatives by Cauchy's formula;
the positive minimum of |Xi| makes the logarithmic-derivative limits
valid. Each finite factor contributes the inverse squares of its two
zeros, with multiplicity. The tail comparison
|t-rho|^(-2)<=4|rho|^(-2) proves absolute convergence, so regrouping
from opposite-zero pairs into conjugate pairs is legitimate. No first
reciprocal sum is used. Csordas v2 (2.3), directly checked in its
complete proof, is the same identity; its additional interval premise
is not needed for that algebraic identity. L024 excludes the quadratic
exponential that would otherwise add a constant term.

For enumeration, each nonreal zero has exactly one conjugate mate of
equal multiplicity. Taking d>0 counts each pair once; reflected pairs
at opposite nonzero gamma are different pairs. The finite rectangle
in Section 1 includes the closed endpoint windows. Dividing by q_j
removes one copy of each root and leaves an entire, real F_j even
when m_j>1. Thus the factor m_j in (6) and (1) is correct. At a real
zero q_j stays positive, F_j vanishes and the negative part of D_1
vanishes, so the extension does not assume simplicity.

For integration, J_j(T) is a nonempty compact interval, possibly a
singleton; F_j/A is continuous there. The substitution contributes
d_j^2 from the kernel and d_j from dt. The integral of 1-v^2 is at
most 4/3, including singleton windows. Hence both constants in (2)
are correct. Independently substituting |R|^2=|F_j/A|^2/L^5 gives
the sum on the left of (3) equal to B/L^2, and W=B/(T L^3).
This checks the exact normalization, not merely its logarithmic order.

For the gauge, L465's b agrees exactly with A, including the factor
(t^2+1/4)/2. Its formula (2) identifies the same Hardy branch used by
Bui--Hall; a constant sign choice would also leave every product used
here unchanged. Direct differentiation gives the minus sign before
a''Z^2 in (7). The paired-gamma calculation (14) in L465 gives the
uniform O(T^(-2)) curvature, hence (9), with no logarithm of Xi at
zeros. Bui--Hall v1 (1), checked against its ordinary-derivative
definition, gives the leading dyadic constants 1, 1/12 and 1/80
for M_0, M_1 and M_2, and -1/12 for the mixed (0,2) product.
The dyadic subtraction preserves these leading constants. Therefore
half the difference 1/sqrt(80)-1/12 is precisely
1/(8 sqrt(5))-1/24>0. The inequality discards Z'^2 only in the
direction of an upper bound; it supplies no lower bound on N.

Finally, replaying v=tan(theta) gives exactly pi/8+1/3 in (10).
Its square root is multiplied by d_j^(-3/2), as asserted in (5),
even for clipped windows. Bui--Hall v1 Theorem 3 and Section 7,
directly checked, give the ordinary fourth moment used here; Section
4.2 explicitly omits the proof of Proposition 3. This qualification
is retained. No cited statement is a zero-conditioned quotient moment.
The displacement loss and the absence of (3) are therefore unchanged.

This completes a local correctness audit of the existing known-tool
specialization, without independently checking the imported moment
proofs, improving a bound or producing a new mathematical input.
The ordinary-moment summation stop remains in force. Small first-sign
mass would still not exclude individual negative heights, nor would
first signs alone establish all-degree mixed positivity.

## Mathlib

Full matching coverage for the integrated pair-divided majorant
and its actual-Xi application has not been checked. Supporting
availability for the analytic product passage, clipping, integration
and moment theorems is also unchecked; no absence claim is made.
The cited primary identity and moment formulas are the imported
mathematical inputs. The necessary specializations and their
remaining arithmetic limitation are written out above.
