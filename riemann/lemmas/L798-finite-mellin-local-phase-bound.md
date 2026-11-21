# Lemma 798: a uniform finite Mellin local-phase bound

## Hypotheses

Let

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    c=9/4, F(z)=z(pi exp(2z)-c).

Use L797's inverse x=x(s)=u+ih for s in D. Define

    q=pi exp(2x), Q=|q|=pi exp(2u), d=3/(16u),
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z),
    A=2F'(x)/x, B=|A|, theta=Arg A, a=exp(-i theta/2),
    J(s)=a integral_{-d}^{d} exp(S_s(x+av)-S_s(x)) dv,
    G(s)=a integral_{-d}^{d} exp(-B v^2/2) dv.

Log, Arg and square roots are principal. The square root of a positive
real number is positive. L797 supplies existence, uniqueness and the
branch over all of D, including |s|=6000 and the curved left boundary,
as well as u>3, |h|<pi/4-1/(4u), Re A>0, Q>1000 and c/Q<1/400.
No phase derivative or decrement estimate from the source is assumed.

This is the exact finite-integral test nominated and separately approved
in `drafts/literature/2026-11-05-mellin-local-phase-remainder-audit.md`.
It operationalizes the local-phase cost asserted between (13) and (14)
in bramble_trace, *A continuum certificate for the decreasing Levy
factor associated with Riemann xi*,
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section 3, Lemma 2, (10)–(14). The source does not
print J and G in this form. Accordingly the result verifies this
specified reading; it does not verify an unspecified different split
of phase and amplitude errors.

## Conclusion

For every s in D,

    |J(s)-G(s)| / |sqrt(2pi/A)|
       < (58034/77175)/Q < (4/5)/Q < (11/10)/Q.          (1)

On the entire closed disc |z-x|<=d,

    |S_s'''(z)|<10Q,   |S_s''''(z)|<19Q.               (2)

For real |v|<=d the real phase satisfies

    Re(S_s(x+av)-S_s(x)) <= -(85/48)Q v^2,             (3)

with strict inequality when v!=0. In particular (3) pays the source's
weaker 1.54Q v^2 local decrement under this parameterization.

This is a reproduction of a selected effective local source bound,
with an explicit stronger constant for the nominated interpretation;
no novelty beyond the sources checked is asserted. The proof below
was completed in step513 and passed the independent conceptual audit
in step514, recorded below. It
does not prove the full Mellin estimate (11), amplitude control, the
omitted Gaussian or global contour tails, continued endpoint identity,
quotient differences, inversion, evaluator/certificates, Levy signs or
actual-Xi all-degree mixed positivity. There is no claim of RH progress
beyond establishing this local prerequisite.

## Proof

### Admissibility, normalization and curvature modulus

Since u>3, we have d<1/16. On the closed radius-d disc about x,

    Re z >= u-d > 47/16 > 0,
    |Im z| <= |h|+d < pi/4-1/(16u) < pi/4.

Thus the principal Log and S_s are holomorphic on a neighborhood of
the disc; in particular all Taylor segments used below are admissible.
Only phase analyticity is used, not any global theta-contour assertion.

From s=x(q-c), direct differentiation gives

    S_s'(x)=0,
    S_s''(x)=-2(q-c)/x-4q=-A,
    A=4q+2(q-c)/x=2q(2+1/x)-2c/x.                     (4)

Because Re(1/x)>0, |2+1/x|>2. The reverse triangle inequality and
|x|>=u>3 therefore imply

    B > 4Q-2c/|x| > 4Q-3/2 > (15/4)Q.                (5)

The last inequality needs only Q>6, already supplied by L797. Also

    B <= 4Q+2(Q+c)/|x|
      < [4+(2/3)(401/400)]Q = (2801/600)Q < 5Q.       (6)

Since Re A>0, theta lies in (-pi/2,pi/2), |a|=1 and Aa^2=B.
The principal-square-root convention consequently gives exactly

    sqrt(2pi/A)=a sqrt(2pi/B),
    |sqrt(2pi/A)|=sqrt(2pi/B)>0.                       (7)

This also establishes that every denominator in (1) is nonzero.

### Paying the two derivative bounds

For |z-x|<=d, the triangle inequality gives

    |z| > 47/16,   |x|/|z| <= 1+d/|z| < 48/47.

For 0<=t<=1/8, the exponential series and n!>=1 give
exp(t)<=sum_{n>=0}t^n=1/(1-t). Since 2d<1/8, it follows that

    |pi exp(2z)| <= Q exp(2d) < (8/7)Q.               (8)

Moreover |s|=|x||q-c|<(401/400)Q|x|, so

    |s|/|z|^3 < Q (401/400)(48/47)(16/47)^2 < Q/8,
    |s|/|z|^4 < Q (401/400)(48/47)(16/47)^3 < Q/24.    (9)

The last comparisons are exact rational inequalities. Their left
coefficients are respectively

    4927488/41529200,    78839808/1951872400.

Multiplying the first numerator by 8 gives 39419904<41529200;
multiplying the second by 24 gives 1892155392<1951872400.
No numerical sampling of D is involved.

Differentiate the explicit phase on the disc:

    S_s'''(z)=4s/z^3-8pi exp(2z),
    S_s''''(z)=-12s/z^4-16pi exp(2z).

Equations (8) and (9) give

    |S_s'''(z)| < (1/2+64/7)Q = (135/14)Q < 10Q,
    |S_s''''(z)| < (1/2+128/7)Q = (263/14)Q < 19Q.

This proves (2) uniformly on the closed disc rather than assuming the
source's claimed bounds.

### Symmetric cubic cancellation and exponential remainder

For real v in [-d,d], put

    f(v)=S_s(x+av)-S_s(x),
    R(v)=f(v)+B v^2/2,
    b=a^3 S_s'''(x)/6.

Taylor's formula along the straight segment from x to x+av, with its
integral remainder and (2), yields

    |R(v)| <= (5/3)Q |v|^3,
    |R(v)-b v^3| <= (19/24)Q v^4.                     (10)

These are the order-two and order-three Taylor estimates respectively;
the constants are the derivative suprema divided by 3! and 4!.
For negative v the segment is traversed in the opposite direction,
and its absolute-length remainder gives the same estimates. No
asymptotic limit or unproved uniform remainder is used.

From (5), (10) and d<1/16,

    Re f(v) <= -B v^2/2+(5/3)Q d v^2
             <= -(85/48)Q v^2,

strictly for v!=0. This proves (3), since
15/8-5/48=85/48>77/50=1.54.

For any complex w the exponential series proves

    |exp(w)-1-w| <= (|w|^2/2) exp(|w|),               (11)

because (m+2)!>=2m! for m>=0. Applying this to w=R(v) and using
both estimates in (10) gives

    |exp(R(v))-1-bv^3|
      <= (19/24)Q v^4
         +(25/18)Q^2 v^6 exp((5/3)Q |v|^3).           (12)

Crucially, the omitted term integrates to zero on the finite interval:

    integral_{-d}^{d} exp(-B v^2/2) b v^3 dv=0.

This uses only oddness, B real and positive, and the symmetric
endpoints. It does not require b real. Consequently

    J-G = a integral_{-d}^{d} exp(-B v^2/2)
                         [exp(R(v))-1-bv^3] dv.       (13)

Thus G in the numerator remains precisely the truncated Gaussian.
No missing Gaussian tail is silently absorbed into J-G.

### Complete Gaussian moments bound the error majorants

Define the positive real number

    T=B-(10/3)Qd > (85/24)Q > (7/2)Q.                 (14)

For |v|<=d we have

    exp(-B v^2/2+(5/3)Q |v|^3) <= exp(-T v^2/2).

Taking absolute values in (13), applying (12), dividing by (7), and
extending only the nonnegative error majorants to the entire real
line yields

    |J-G|/|sqrt(2pi/A)|
      <= sqrt(B/(2pi)) [
           (19Q/24) integral_R v^4 exp(-B v^2/2) dv
          +(25Q^2/18) integral_R v^6 exp(-T v^2/2) dv]. (15)

For any real t>0 the real Gaussian integral is
integral_R exp(-t v^2/2) dv=sqrt(2pi/t). Its even moments obey
I_{2k}(t)=(2k-1)I_{2k-2}(t)/t by integration by parts; the boundary
term vanishes because a fixed polynomial times exp(-t v^2/2) tends
to zero at both infinities. Thus all integrals here converge and

    integral_R v^4 exp(-t v^2/2) dv=3 sqrt(2pi) t^(-5/2),
    integral_R v^6 exp(-t v^2/2) dv=15 sqrt(2pi) t^(-7/2).

Using these identities in (15) gives the explicit bound

    |J-G|/|sqrt(2pi/A)|
      <= 19Q/(8B^2) + (125Q^2/6) sqrt(B)/T^(7/2).     (16)

By (5), the first summand is less than 38/(225Q). By (6) and (14),
the second is less than

    (1/Q)(125/6) sqrt(5)/(7/2)^(7/2)
      = (1/Q)(125/6)(8/343) sqrt(10/7)
      < 200/(343Q),                                  (17)

where sqrt(10/7)<6/5 follows from 250<252. Finally

    38/225+200/343=58034/77175
                   <61740/77175=4/5<11/10.

This proves (1). All estimates use L797's strict inequalities at
every point of the closed D; neither the radius-6000 case nor the
curved-boundary case was removed. They depend only on u, |x| and
absolute derivative bounds and therefore cover both half-planes
directly. Equivalently L797 gives x(conjugate(s))=conjugate(x(s));
Re A>0 then makes a, J and G respect conjugation with these branches.
No limiting argument at infinity, change in logarithm branch, integral
interchange, numerical certificate or zero-location assumption occurs.

The exact proof technique is a direct effective specialization of
the symmetric-saddle cancellation already assessed from C. O'Sullivan,
*Revisiting the saddle-point method of Perron*, Pacific J. Math.
298(1) (2019), 157–199, Corollary 5.1 and proof, pp.175–176,
[published text](https://msp.org/pjm/2019/298-1/pjm-v298-n1-p08-s.pdf).
That fixed-data asymptotic theorem is methodological context, not an
input furnishing any of the uniform constants above. The independent
reproduction is needed because neither that theorem nor the inspected
paper23 outline proves this nominated numerical inequality with its
parameter-dependent phase and normalization.

### Independent conceptual audit, 5 November 2026 — step514

The unchanged SPECIALIZE assessment named in the hypotheses covers
this exact test. Independently reconstructing the proof verifies (1)
on all of D; no mathematical correction or extra assumption is needed.
This removes the pending-review qualification for the nominated local
bound only. It is verification of a source reproduction, not a new
result beyond the sources checked or verification of source (11).

**Analytic domain and branches.** L797 supplies its inverse on an open
neighborhood of D, with strict u>3 and strip clearance even when
|s|=6000 or Re(s)=-|s|/(8 log|s|). Thus u-d>47/16 and
|h|+d<pi/4-1/(16u), so every closed Taylor segment is inside the
holomorphy domain of the principal logarithm. Directly differentiating
S_s and substituting s=x(q-c) gives S_s'(x)=0 and S_s''(x)=-A.
The modulus lower bound uses |2+1/x|>2, which follows from
Re(1/x)>0; it does not replace |A| by Re A. In detail,
B>4Q-3/2>(15/4)Q because Q>1000>6, and
B<(2801/600)Q<5Q. Separately Re A>0 places theta in
(-pi/2,pi/2), so Aa^2=B and the principal square root is exactly
a sqrt(2pi/B). There is no phase or factor-of-two loss in (7).

**Uniform derivative constants.** The disc estimates
|z|>47/16 and |x|/|z|<48/47 hold simultaneously at every z in
the disc. Together with |s|<(401/400)Q|x| they give the two
rational coefficients in (9). Recomputing their cross-products gives
39419904<41529200 and 1892155392<1951872400, respectively.
Also 2d<1/8 and the positive exponential series imply
|pi exp(2z)|<(8/7)Q. The independently differentiated third and
fourth derivatives are 4s/z^3-8pi exp(2z) and
-12s/z^4-16pi exp(2z). Hence their uniform majorants are
(135/14)Q<10Q and (263/14)Q<19Q, including the disc boundary.
None of these inequalities assumes a source derivative estimate.

**Complex Taylor remainder and cancellation.** With f and b as above,
the exact real-parameter Taylor formulas are

    R(v) = (v^3/2) integral_0^1 (1-t)^2 f'''(tv) dt,
    R(v)-b v^3 = (v^4/6) integral_0^1 (1-t)^3 f''''(tv) dt.

Here f^(k)(tv)=a^k S_s^(k)(x+atv); |a|=1, and the same
parameterization holds for negative v. Integrating the positive weights
gives precisely the factors 1/6 and 1/24 in (10). The exponential
remainder then has the quartic and squared-cubic majorants in (12).
The coefficient b may be complex: the integral of v^3 times the
real even Gaussian is still exactly zero on [-d,d]. Consequently
(13) subtracts the specified finite G, with no unaccounted Gaussian
tail. The real-phase coefficient is 15/8-5/48=85/48>77/50,
and the damped quadratic coefficient is
15/4-5/24=85/24>7/2. Thus both (3) and T>0 are paid uniformly.

**Integral normalization and final threshold.** The finite integrands
are continuous. Only their nonnegative error majorants are extended
to the real line. For each positive real t, integration by parts in
the convergent real Gaussian moments gives factors 3 and 15 for the
fourth and sixth moments; the boundary terms vanish. Multiplying by
sqrt(B/(2pi)) therefore yields exactly
19Q/(8B^2)+(125Q^2/6)sqrt(B)/T^(7/2). The first term is
<38/(225Q). In the second, the upper bound for B and lower bound
for T are used in the correct directions, giving

    (125/6)(8/343)sqrt(10/7)/Q < 200/(343Q),

since (6/5)^2-10/7=2/175>0. Their sum is
58034/(77175Q), strictly less than 4/(5Q) because
58034<61740, and hence strictly less than the required 11/(10Q).
These are analytic bounds for every s in D, not a finite sample.

All estimates also apply directly for h<0. Alternatively L797's
conjugation identity, the right-half-plane logarithm and Re A>0
make x, a, J and G respect conjugation, with no cut crossing.
No limiting step at the closed boundary of D is used. L797 remains
the sole direct notebook input, so the existing DAG edge is complete.
The omitted Gaussian, amplitude, global contour and continued endpoint,
Mellin quotient, inversion, certificates and sufficient Xi signs are
unresolved; this audit supplies none of those claims. No numerical
script or additional source import was required.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
Only elementary complex differentiation, Taylor's integral remainder,
the exponential series, odd-integrand cancellation and real Gaussian
moments are used after L797. No specific Mathlib declaration or formal
verification is asserted. The explicit proof above, not a Mathlib
availability assumption, supplies the bounds.
