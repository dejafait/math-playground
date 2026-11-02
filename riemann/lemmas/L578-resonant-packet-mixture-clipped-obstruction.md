# Lemma 578: a uniform resonant packet with positive spectral completion misses the clipped threshold

## Hypotheses

Let A,C,D be deterministic in [0,4], p in [0,1], and phi real.
Let U be uniform on [-1/4,1/4], B uniform modulo 2pi, independent.
A selector constant along each path chooses, with probability p, the packet

    P(x)=A cos(Ux+B)+C cos(2Ux+2B+phi),

and otherwise chooses R(x)=D cos(Vx+E). Here V has an even positive
probability measure nu on [-1/2,1/2], and E is uniform modulo 2pi,
independent of V. The selector is independent of the entire tuple
(U,B,V,E). No independence between the packet and remainder tuples
is needed. Denote the selected process by S.
All derivatives are ordinary x derivatives. Put

    J=(S(0),S'(0),S''(0),S(1),S'(1),S''(1)),
    Q(J)=(S(0)S''(0)-S'(0)^2)_+.

Require **spectral completion**: the covariance spectral measure of S
is Lebesgue measure of density one on [-1/2,1/2]. In particular the
remainder is a nonnegative measure, not a signed repair. The covariance
convention is E S(x)S(y)=integral exp(i(x-y)w) dmu(w).
This is the explicit completion condition of the approved test; it is
stronger than merely matching the finitely many entries of K.
Only the definition of K in L473 (6) is a mathematical input:

    K_((r,j),(s,k))
      =integral_(-1/2)^(1/2) (iw)^j(-iw)^k exp(i(r-s)w) dw,
      r,s in {0,1}, j,k in {0,1,2}.

No arithmetic moment theorem, actual-Hardy law, fourth-tensor realization,
Xi transfer, real-zero hypothesis or RH assumption is used.

## Conclusion

Every such spectrally completed mixture is centered, has real analytic
paths and a joint derivative process stationary under every real shift.
It satisfies all entries E JJ^T=K, including the four exactly zero
same-height odd entries, and

    |J|^2<=1193/8,
    0<=E Q(J)<=1/(216 sqrt(2))<5/1512<1/288.                    (1)

The last two rational thresholds have gap 1/6048. If ell=log H>0,
sqrt(ell) S has paired norm at most ell^2 for ell^3>=1193/8,
covariance ell K, and clipped mean strictly below ell/288.
Thus no member of this entire completed subfamily passes the approved
test. This does not exclude other frequency laws, more harmonics,
other stationary processes, or a finite-K match without the stated
spectral completion. It proves no actual-Hardy or RH assertion.
The result is a bounded analytic obstruction under previously reviewed
EXPLORE coverage, not a certified originality claim.

## Proof

### Spectral measure and all completion cases

For harmonic number m=1,2 the j-th derivative is
Re((imU)^j exp(i(mUx+mB+phi_m))), with phi_1=0, phi_2=phi.
Uniform integration in B centers each derivative. Products with distinct
harmonic numbers vanish, since all their B exponents are nonzero
integers (of absolute value 1 or 3). For a fixed harmonic, its paired
phase average is

    (1/2) Re((imU)^j(-imU)^k exp(im(r-s)U)).                   (2)

This follows by expanding the two real parts; the terms with exponent
2imB vanish. Thus relative phase coherence changes the nonlinear law
but creates no second-order cross-harmonic term, even for derivatives.
The density of U is 2 on I=[-1/4,1/4], while 2U has density 1 on
F=[-1/2,1/2]. The packet spectral density therefore is

    a(w)=A^2 1_I(w)+(C^2/2)1_F(w).                            (3)

Endpoint conventions have no effect on these absolutely continuous
measures. The single-wave remainder spectral measure is (D^2/2)nu,
because nu is even and E is an independent uniform phase. The selector
forms a mixture, so its weights enter linearly, not quadratically:

    mu=p a(w)dw+(1-p)(D^2/2)nu.

Set h=1_F-p a and M=integral h=1-p(A^2+C^2)/2. Completion is exactly

    (1-p)(D^2/2)nu=h(w)dw.                                   (4)

In particular nonnegativity requires

    p(A^2+C^2/2)<=1.                                         (5)

This condition also implies h>=0 on F outside I. If M>0, (4) holds
if and only if (1-p)D^2/2=M and nu has density h/M; this is an even
probability density. In this case necessarily p<1 and D>0. If M=0,
nonnegative h has zero integral and is zero almost everywhere; then
(4) holds if and only if (1-p)D^2=0, with arbitrary nu. This includes
the zero-remainder case without division by M. If p=1, completion
forces C^2/2=1 from F outside I and A=0 from I; the remainder is
unused. If p=0, it forces D^2=2 and nu uniform on F; the packet is
unused. If p<1 and D=0, only the M=0 case is possible. These statements
also cover zero packet amplitudes. Any proposed amplitude outside
[0,4] is simply outside this lemma; no reduction from arbitrary
amplitudes is claimed. The family is nonempty, for example p=0,
D=sqrt(2), nu uniform on F.

### Exact covariance, stationary derivatives and support

Apply (2) and its single-wave counterpart for every j,k<=2 and every
r,s in {0,1}. All frequencies are bounded, and the sums are finite,
so the computations are integrable and differentiating the individual
paths and phase formulas is legitimate. Combining with (4) gives

    E S^(j)(r)S^(k)(s)
      =Re integral_F (iw)^j(-iw)^k exp(i(r-s)w) dw=K_((r,j),(s,k)).

The last integral is real by w -> -w and conjugation. At equal heights,
odd j+k gives zero by oddness; this verifies the four tight odd entries
without an O(1) error. Every cross-height entry is included in the same
identity; the jets at the two heights are not assumed independent.

For a real shift t, conditional on U, the transformation B -> B+Ut
modulo 2pi preserves its uniform law and independence from U. It changes
the second harmonic phase to 2B+2Ut+phi, precisely as translation
requires. This proves stationarity of all finite joint derivative laws
of P, including U=0. For R, conditional on V the same argument uses
E -> E+Vt. The independent time-independent selector preserves the
mixture law. No ergodic or time-average assertion is needed.

Each path is a finite cosine sum. For j=0,1,2 the packet has the uniform
bound A/4^j+C/2^j, and the remainder has bound D/2^j. The common bounds
under the amplitude caps are respectively 8,3,5/4. Hence

    |J|^2<=2(8^2+3^2+(5/4)^2)=1193/8.

All observables here are integrable. The asserted scaled norm follows
from (1193/8)ell<=ell^4. Quadratic homogeneity gives the scaled covariance
and clipped mean. This does not construct any of the required fourth
moments or a derivative-preserving rare correction.

### A phase-arc obstruction, uniform in every parameter

The single-wave remainder satisfies, pathwise,

    RR''-(R')^2=-D^2 V^2<=0.

For the packet at x=0 put theta=B and psi=2theta+phi. Direct expansion
using cos^2+sin^2=1 gives

    PP''-(P')^2=U^2 W(theta),
    W=-A^2-4C^2-AC(5 cos(theta)cos(psi)+4 sin(theta)sin(psi))
     =-A^2-4C^2-(AC/2)(9 cos(theta+phi)+cos(3theta+phi)).         (6)

The factors of U in the first and second derivatives give U^2,
also when U=0. The last equality follows from the sum/difference
identities: 5 cos(theta)cos(psi)+4 sin(theta)sin(psi)
=(9/2)cos(theta-psi)+(1/2)cos(theta+psi).

As (A-2C)^2>=0, A^2+4C^2>=4AC. Also cos(3theta+phi)>=-1.
Consequently, for every theta and phi,

    W<=AC[-7/2-(9/2)cos(theta+phi)],
    W_+<=AC 1_{cos(theta+phi)<-7/9}.                           (7)

Indeed the bracket can be positive only on that arc, and is everywhere
at most 1. This remains valid when AC=0, in which case W_+=0.

For completeness the normalized length of that arc is strictly less
than 2/9, without numerical trigonometry. Let x=cos(2pi/9), so
1/2<x<1 and 4x^3-3x=cos(2pi/3)=-1/2. The polynomial f(z)=4z^3-3z
is strictly increasing on [1/2,1], and

    f(7/9)=-329/729>-1/2=f(x).

Hence x<7/9 and arccos(7/9)<2pi/9. For uniform theta modulo 2pi,

    Pr(cos(theta+phi)<-7/9)=arccos(7/9)/pi<2/9.                (8)

Independence of U and B gives E U^2=1/48 and, by (7)--(8),

    E Q(J)=p E U^2 E W_+<=pAC/216.                            (9)

The unused remainder and all selector weights have been retained.
Finally, (A-C/sqrt(2))^2>=0 and (5) imply

    sqrt(2) pAC<=p(A^2+C^2/2)<=1.

Substitution in (9) proves the first upper bound in (1). Since
sqrt(2)>7/5, it is strictly less than 5/1512; exact subtraction gives

    1/288-5/1512=1/6048>0.

The upper bound therefore excludes the entire covered family, including
all zero amplitudes and endpoint selectors. No optimization, quadrature,
sample estimate or unproved exchange of infinite limits is used.

### Source specialization and qualifications

The prior assessment is
`drafts/literature/2026-10-31-resonant-stationary-packet-review.md`,
DECISION EXPLORE, at its exact uniform-frequency COVERED_TARGET.
It reuses Ali Rahimi and Benjamin Recht, *Random Features for Large-Scale
Kernel Machines*, Advances in NIPS 20 (2007), Section 3, Theorem 1,
equation (2), and the subsequent real random-phase formula, PDF pp. 2--4,
[author PDF](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf).
That result supplies the standard independent-phase spectral construction
for the single-wave remainder. Here the elementary phase integrals and
explicit residual are given to justify the normalization and specialization
to all derivative entries; the independent-phase theorem is not used
to infer the coherent packet's nonlinear law. The reviewed phase-coupling
sources are contextual comparisons, not mathematical premises of (6)--(9).
The nonlinear phase-arc bound is the covered test not supplied by an
inspected theorem. No novelty conclusion is inferred from that comparison.

L576 and L577 are contrasts only; neither is an input to this proof.
Their independent-model failures remain unchanged. The present obstruction
uses the uniform base-frequency law, the two specified harmonics, a
mixture rather than a sum, and full nonnegative spectral completion.
Removing any of those restrictions requires a new assessment. Full
fourth-tensor realization, actual-Hardy transfer and actual-Xi positivity
remain unresolved, independently of this negative test.

### Independent application audit, 2026-10-31

The separate audit uses the prior ready assessment
`drafts/literature/2026-10-31-l578-independent-audit.md`. It replays the
elementary application, not the proofs of external spectral or arithmetic
theorems. Only L473 (6) is a local mathematical input.

**Hypothesis repair.** The initial wording said the selector was independent
of "these variables" immediately after defining U and B; it did not
explicitly include V and E. Equations (3)--(4) use their unconditional
remainder law after selection. The hypotheses now explicitly require
independence of the selector from the whole tuple (U,B,V,E), exactly as
in the approved family. Pairwise independence would not justify that
conditioning step. No conclusion is asserted for the weaker wording.
Dependence between the two unselected path tuples is harmless because
the selector forms a mixture, without products between those paths.

**Completion cases.** Independent phase averaging gives one half of the
frequency law times amplitude squared. Thus U's density 2 and 2U's
density 1 give (3), and independence of the selector gives (4) with
linear weights. The residual density on I is
1-p(A^2+C^2/2), and on F outside I is 1-pC^2/2. The former being
nonnegative implies the latter is too. Integrating gives exactly M.
For M>0, equality of positive measures forces the stated total mass and
normalized density h/M. For M=0, a nonnegative density with zero integral
vanishes almost everywhere, so no normalization or hidden division is
needed. For p=1 the two density equations force C^2=2 and A=0;
for p=0 total mass and normalization force D^2=2 and nu=dw on F.
If p<1 and D=0 the residual must vanish. These arguments exhaust the
zero-amplitude and endpoint cases; they do not assert feasibility for
arbitrary prescribed D in the positive-mass case.

**All 21 covariance entries.** Put G(d)=integral_F exp(idw) dw,
so G(d)=2 sin(d/2)/d with its continuous value at zero. Bounded
frequencies justify its derivatives through order four under the
integral. The entry in (6) of L473 is
(-1)^k G^(j+k)(r-s). At either equal height the six unordered entries
form exactly

    K_0=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]].

For r=0 and s=1, writing g_n=G^(n)(1), the remaining nine entries are

    K_01=[[g_0,g_1,g_2],[-g_1,-g_2,-g_3],[g_2,g_3,g_4]].

Indeed G is even, so G^(n)(-1)=(-1)^n G^(n)(1); this checks every
cross-height derivative sign. If s=sin(1/2) and c=cos(1/2), direct
differentiation gives

    g_0=2s, g_1=c-2s, g_2=(7/2)s-2c,
    g_3=(23/4)c-(21/2)s, g_4=(337/8)s-23c.

The other block is K_01 transposed. The two diagonal blocks account
for twelve unordered entries, including the four exact odd zeros;
the displayed cross block accounts for nine. Formula (2) and exact
completion give each of them, without independence of the two heights.

**Stationarity and support.** Conditional on U, translation sends
B to B+Ut and the doubled phase to 2(B+Ut)+phi. Uniform phase is
preserved at every real t, jointly for every finite list of ordinary
derivatives. The identical argument conditional on V applies to E.
The independent, path-constant selector therefore preserves the full
stationary derivative law. No time-average assertion is involved.
The componentwise bounds 8,3,5/4 hold for both selected path types;
their squared sum at both heights is 1193/8. Multiplication by
sqrt(ell) gives support within ell^2 exactly under the stated sufficient
condition ell^3>=1193/8. The clipped form is homogeneous of degree two.

**Nonlinear bound and exact margin.** Expanding PP''-(P')^2
gives cross terms -5AC cos(theta)cos(psi) and
-4AC sin(theta)sin(psi), and diagonal terms -A^2-4C^2.
The sum/difference identities give
the 9:1 cosine coefficients in (6). The inequalities
A^2+4C^2>=4AC and cos(3theta+phi)>=-1 give (7); its bracket is at
most one and positive only on the stated arc. If AC=0 the clipped
form vanishes. For AC>0 the normalized arc length is less than 2/9:
f(7/9)+1/2=71/1458>0, f is strictly increasing above 1/2, and
cos(2pi/9) lies in that interval with f=-1/2. The frequency factor
is E U^2=1/48. The single-wave branch has exactly zero clipped form,
so the expectation is at most pAC/216, including both selector
endpoints. Completing the square gives pAC<=1/sqrt(2).
Finally 2>49/25 proves sqrt(2)>7/5, and exact subtraction gives
1/288-5/1512=1/6048. No trigonometric sampling, optimization or
numerical evidence is used in any of these checks.

**Verdict.** With the selector independence made explicit, the entire
approved obstruction passes this application audit. The bound remains
E Q<=1/(216 sqrt(2))<5/1512<1/288. This validates local route evidence,
not progress beyond the checked sources on RH. Full spectral completion
is used essentially at (5); finite-K-only matching, full fourth moments,
other frequency laws and actual-Hardy/Xi transfer remain unresolved.
The existing DAG row L578: L473 accounts for the sole direct input.

## Mathlib

Full matching coverage for this coherent two-harmonic mixture and clipped
phase-arc obstruction has not been checked. No absence claim is made.
The phase integration, trigonometric identities and finite algebra above
are explicit; no Mathlib theorem is an essential input.
