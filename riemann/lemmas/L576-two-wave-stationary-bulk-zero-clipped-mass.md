# Lemma 576: the equal-amplitude two-wave stationary bulk has zero clipped mass

## Hypotheses

Let U,V be independent uniform random variables on [-1/2,1/2], and
B,C independent uniform random variables on [0,2pi], all four mutually
independent. For real x define

    S(x)=cos(Ux+B)+cos(Vx+C),
    J=(S(0),S'(0),S''(0),S(1),S'(1),S''(1)),
    Q(J)=(S(0)S''(0)-S'(0)^2)_+.

Derivatives are ordinary x derivatives. Norms on R^6 are Euclidean.
Let K be the exact matrix in L473 (6), with indices (r,j), r=0,1,
j=0,1,2, in that order:

    K_((r,j),(s,k))
      =integral_(-1/2)^(1/2) (iw)^j(-iw)^k exp(i(r-s)w) dw.

This uses only L473's explicit matrix as the comparison target, not
its arithmetic moment asymptotics or its abstract law construction.
No assumption about actual Hardy sampling, Xi, RH or stationary
realization of the full fourth tensor is made.

## Conclusion

S has real analytic paths and is stationary in all joint
finite-dimensional distributions under every real shift. In fact the
joint derivative process through order two is stationary. Moreover

    E J=0, E JJ^T=K,
    sup_(x in R)|S^(j)(x)|<=2^(1-j), j=0,1,2,
    |J|^2<=21/2,
    S(x)S''(x)-S'(x)^2<=0 for every real x, for every outcome,
    E Q(J)=0<1/288.                                             (1)

For ell=log H>0 the scaled process F_H=sqrt(ell) S therefore has
paired covariance ell K and paired norm at most ell^2 whenever
ell^3>=21/2. All four tight same-height odd second entries of L473
are zero. Nevertheless its clipped mean is zero, so this bulk cannot
supply the nominated ell/288 lower bound. These statements do not
verify any of the 126 fourth constraints of L473. No other stationary
process or actual Hardy law is ruled out.

## Proof

### Covariance and bounded paths

For a fixed real w and uniform phase b, write

    d^j/dx^j cos(wx+b)=Re((iw)^j exp(i(wx+b))).

The uniform phase has E exp(ib)=E exp(2ib)=0. Multiplying two real
parts and integrating b therefore gives, for j,k=0,1,2,

    E_b [cos(wx+b)^(j) at x=r
                   * cos(wx+b)^(k) at x=s]
      =(1/2) Re((iw)^j(-iw)^k exp(i(r-s)w)).                     (2)

Here the superscripts in the bracket mean derivatives, not powers.
Each derivative is centered after phase averaging. Independence of
the two waves makes all cross-wave terms vanish. The two identical
diagonal-wave contributions in (2) add to

    E S^(j)(r)S^(k)(s)
      =Re integral_(-1/2)^(1/2)
                         (iw)^j(-iw)^k exp(i(r-s)w) dw
      =K_((r,j),(s,k)).                                        (3)

The integral is real: replacing w by -w conjugates its integrand.
Equation (3) covers every entry, including all nine lag-one cross
entries; it imposes no independence between the two height jets.
At r=s, j+k odd makes the integral zero. In particular the four
entries (j,k)=(0,1),(1,2), r=s=0,1, vanish exactly.

Every path is a finite sum of cosines, hence real analytic. The
frequency bound gives |S^(j)(x)|<=|U|^j+|V|^j<=2^(1-j), including
j=0 by bounding each cosine by one. Consequently

    |J|^2<=2*(2^2+1^2+(1/2)^2)=21/2.

Every polynomial in these six coordinates is integrable. Scaling by
sqrt(ell) gives squared norm at most (21/2)ell, which is at most
ell^4 precisely when ell^3>=21/2. This is a common sufficient onset
H>=exp((21/2)^(1/3)), not an onset for actual Hardy moment formulas.

### Exact stationarity

For any fixed shift h, condition on U=u,V=v. The translated phases
(B+uh mod 2pi,C+vh mod 2pi) remain independent uniform phases, with
conditional law independent of u,v. Thus
(U,V,B+Uh mod 2pi,C+Vh mod 2pi) has the same law as (U,V,B,C).
For every finite list of real positions, substituting these phases
represents the shifted S and all its derivatives at those positions.
Their joint laws are unchanged. This proves the stated stationarity;
no assertion about translation invariance of a finite Hardy interval
is involved.

### Exact clipped statistic and the decisive threshold

Fix any real frequencies u,v, phases b,c and position x. Put
A=ux+b, D=vx+c. Expansion without division by S gives

    S S''-(S')^2
      =-u^2-v^2-(u^2+v^2)cos A cos D-2uv sin A sin D
      =-((u+v)^2/2)(1+cos(A-D))
       -((u-v)^2/2)(1+cos(A+D)).                               (4)

The second equality follows from
cos A cos D=(cos(A-D)+cos(A+D))/2 and
sin A sin D=(cos(A-D)-cos(A+D))/2. Both squared coefficients
are nonnegative and both parentheses lie in [0,2]. Hence (4) is
nonpositive identically. It includes u=v, u=-v, zero frequencies,
zeros of S and multiple zeros, since no division or excluded case
occurred. Its positive part is zero pointwise, giving E Q=0.
For F_H the quadratic form is ell times (4), so its positive part
is again zero. The required 1/288 and ell/288 thresholds fail by
these exact amounts. No quadrature, limiting interchange, numerical
certificate or probabilistic exceptional-set argument is needed.

### Source relation and scope

The reusable assessment is
`drafts/literature/2026-10-31-stationary-hardy-path-feasibility.md`,
whose explicit COVERED_TARGET is exactly this test. Its known spectral
comparison is Ali Rahimi and Benjamin Recht, *Random Features for
Large-Scale Kernel Machines*, Advances in NIPS 20 (2007), Section 3,
Theorem 1, equation (2), subsequent real random-phase formula and
Algorithm 1, PDF pp. 2--4,
[author PDF](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf).
The source's continuous positive definite translation-invariant kernel
and probability spectral measure give the random-phase covariance
formula. Here the spectral probability measure is uniform on
[-1/2,1/2]. The factor two from two independent unit-amplitude waves
cancels the phase factor 1/2, as checked in (2)--(3). This direct
specialization is included to fix normalization and cover derivatives,
cross-height entries, support and stationarity under the exact local
hypotheses. No kernel approximation concentration theorem is needed.

The source assessment did not supply the nonlinear statistic. Formula
(4) is the approved bounded obstruction test, not a claim of a new
general theorem or a reproof of an arithmetic moment theorem. The
sum-to-product factorization of two equal-amplitude cosines explains
why this particular choice is too restrictive. Unequal amplitudes or
more waves are outside the result; neither their feasibility nor
their threshold is established here. Fourth moments, rare-path
components, derivative-preserving correction and actual-data boundary
and tail transfer remain unresolved.

## Mathlib

Full matching coverage for this stationary six-coordinate law and
clipped statistic was not checked. No absence claim is made. The
proof is an elementary phase integral and trigonometric identity;
no Mathlib theorem or computation is used as an essential input.
