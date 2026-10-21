# Lemma 404: a beyond-half-power positive-discriminant measure bound

## Hypotheses

Use the fixed actual functions and conventions of L390/L391/L401/L403,
for real t>=40:

    T=1+t, L=log(2+t), f=F_0/A,
    R=exp(i phi), Z=zeta(5/2+it), a=Re(RZ), W=a f,
    (x,y,z)=(f,f'/L,f''/L^2), U=x^2+y^2+z^2,
    D=(2F_0'G'-F_0 G''-F_0''G)^2
           -4(F_0'^2-F_0 F_0'')(G'^2-GG''),
    Delta=D/(A^4 T^4 L^4).

A is the positive real gamma envelope; all derivatives of f,F_0,G
are ordinary height derivatives, taken before division by L^j. R is
the actual gamma carrier, and Z is the complete right-line value.
H ranges over all sufficiently large real values. Import the
unconditional scalar preprint theorem cited below. No RH, conjectural
moment, independent phase, weight lower bound, response cutoff, growing
order/head, common-zero bound or favorable total pencil margin is assumed.

## Conclusion

Put d=520/445121, p=2-d/2=2-260/445121 and
delta=d/4=130/445121. There are fixed constants C,c>0 and H_0>=40
such that for every real H>=H_0, with ell=log H,

    integral_[H,2H] |f^(j)(t)/L(t)^j|^12 dt
        <= C H^p,                              j=0,1,2, (1)
    integral_[H,2H] U(t)^6 dt <= C H^p,                  (2)
    meas{t in [H,2H]:D(t)>0}
        >= c H^(1/2+delta) ell^6.                       (3)

In particular (3) meets the approved target with fixed delta>0 and
K=0. It improves L403's bound by a factor proportional to
H^delta ell^(17/2), tending to infinity, but remains sublinear.
Constants and onset are existential. This is a local REPRODUCTION
specialization of a cited stronger scalar bound and audited transfer
tools; no advance beyond the sources checked or originality is claimed.
The separate step 98 critical audit below validates this specialization.
The cited preprint's full proof is not independently audited here.

## Proof

The assessment saved before this step is
`drafts/literature/2026-10-12-beyond-half-power-positive-discriminant-large-values.md`
(SPECIALIZE). We reuse its inspected scalar coverage and the audited
L403 localization method. The new scalar budget requires checking its
complete tails, its comparison with the right boundary, and every
shift and ordinary-jet transfer; merely changing an exponent in L403's
conclusion would not establish these applications. No large-value theorem
is reproved. Only the family-specific specialization is derived here.

### Precise analytic imports and fixed slack

A. de Faveri and M. Pandey, *The sixth moment of the Riemann zeta
function*, [arXiv:2610.01035v1, 1 October 2026, Theorem 10.1,
p. 18](https://arxiv.org/pdf/2610.01035v1#page=18), states that for
every epsilon>0 and every real V>=1,

    integral_0^V |zeta(1/2+it)|^12 dt
        <<_epsilon V^(2-d+epsilon),  d=520/445121.       (4)

This is imported as an unconditional preprint theorem. The prior
assessment records reading its complete three-range proof and essential
supporting hypotheses; that source review is not an independent audit
of the preprint. We require no derivative version from this source.
Fix epsilon=d/2 once and for all. Thus (4) gives a fixed constant
C_d times V^p, with 1<p<2. No epsilon depends on H. Half the scalar
saving is deliberately reserved in this choice; the following transfer
introduces no additional height-power loss.

L.-P. Arguin, F. Ouimet and M. Radziwill, *Moments of the Riemann
zeta function on short intervals of the critical line*, Ann. Probab.
49 (2021), 3106–3141,
[arXiv:1901.04061v4, Proposition 3.3, p. 22](https://arxiv.org/pdf/1901.04061v4#page=22),
gives integral strip convexity: if F is analytic on a closed vertical
strip and tends uniformly to zero at imaginary infinity, its finite
integrals I(sigma)=integral_R |F(sigma+it)|^q dt, q>0, are log-convex
in sigma. We use only the maximum-boundary consequence with q=12
and strip [1/2,2]. Its hypotheses will be checked below.

The Cauchy/Hölder derivative transfer is the standard calculation in
M. J. Curran and A. Heycock, *Sharp bounds for joint moments of the
Riemann zeta function*,
[arXiv:2403.00902v1, Section 4, p. 8](https://arxiv.org/pdf/2403.00902v1#page=8).
We retain the correct j! Cauchy factor, as in audited L403; the
source's reciprocal-factorial typo is not used. No RH-dependent sharp
moment from that paper is imported. The zeta functional equation,
conjugation and sector-qualified Stirling formula are standard named
inputs already used in L391/L403.

### Entire localization and both full tails

For fixed H large and b=3H/2 put

    F_H(s)=[(s-1)/H] zeta(s) exp((s-i b)^2/H^2).       (5)

This is entire because the only pole of zeta is simple at s=1 and
is canceled by s-1. Audited L403 verifies the Euler-summation identity

    zeta(s)=s/(s-1)-s integral_1^infinity {v}v^(-s-1) dv,
                                             Re s>0, s!=1.

Its remainder integral is locally uniformly absolutely convergent and
has modulus at most 1/Re s. Consequently on 1/2<=Re s<=2,
including s=1 by continuity,

    |(s-1)zeta(s)|<=|s|+2|s||s-1|.

For s=sigma+it the exponential modulus in (5) equals
exp((sigma^2-(t-b)^2)/H^2). For each fixed H this Gaussian times
the displayed polynomial bound tends uniformly to zero at both
imaginary infinities on the closed strip. It also makes every twelfth
integral there finite. F_H is analytic on a neighborhood of the strip,
so these are the precise strip-convexity hypotheses.

We need boundary estimates uniform in H. At sigma=2, absolute
convergence gives |zeta(2+it)|<=zeta(2). With v=(t-b)/H,
|(1+it)/H|<=C(1+|v|), and hence

    I_H(2)=integral_R |F_H(2+it)|^12 dt
        <= C H integral_R (1+|v|)^12 exp(-12v^2) dv
        <= C H <= C H^p.                             (6)

The harmless factor exp(48/H^2) is uniformly bounded. On the left
boundary first take |t|<=4H. The multiplier in (5) has uniformly
bounded modulus there. By conjugation and (4) its integral costs
at most C_d(4H)^p<=C H^p. For each remaining shell
2^k H<|t|<=2^(k+1)H, k>=2,

    |t-b| >= (5/8)|t|,
    |(s-1)/H|^12 <= C 2^(12k),
    |exp((s-i b)^2/H^2)|^12 <= C exp(-4*4^k).

Conjugation and restriction of the nonnegative scalar integral (4)
bound its shell contribution by

    C H^p 2^((12+p)k) exp(-4*4^k).

The sum over k>=2 converges to a fixed finite constant, independent
of H, since its double-exponential decay dominates 2^((12+p)k).
This controls both complete infinite tails, including negative
heights, and proves

    I_H(1/2)<=C H^p.

Proposition 3.3 now yields

    I_H(sigma)<=C H^p,                         1/2<=sigma<=2. (7)

The right boundary's O(H) budget is smaller because p>1; no
interpolation height loss has been hidden in (7).

### Uniform shifts and complex zeta derivatives

Let r=1/ell and J_H=[H-1,2H+1]. Choose a fixed onset with r<=1/2.
For t in J_H and 1/2<=sigma<=1/2+r,
t/H>=1/2 and |t-b|/H<=1. The multiplier in (5) therefore has
modulus at least 1/(2e). Restricting (7) and removing this multiplier
gives

    integral_J_H |zeta(sigma+it)|^12 dt <= C H^p,
                                               1/2<=sigma<=1/2+r. (8)

For sigma=1/2-u with 0<=u<=r use
zeta(sigma+it)=chi(sigma+it)zeta(1-sigma-it).
Uniform Stirling on this fixed near-critical strip gives
|chi(sigma+it)|<=C t^u. Since t<=3H and u<=1/ell,
t^u<=exp(log(3H)/ell)<=C. Conjugation places the reflected
modulus at zeta(1/2+u+it), covered by (8). Thus (8) extends
to 1/2-r<=sigma<=1/2+r. For every complex w with |w|<=r,
substituting tau=t+Im w maps [H,2H] inside J_H, so

    integral_[H,2H] |zeta(1/2+it+w)|^12 dt <= C H^p,
                                                  uniformly in w. (9)

These are restrictions of nonnegative integrals with fixed constants,
valid for all sufficiently large real H. No exceptional-height set
or signed subtraction of moving endpoints is involved.

For j=0,1,2 Cauchy's formula on the radius-r circle, which cannot
meet the pole at these heights, and Hölder on its normalized angular
measure give

    |zeta^(j)(1/2+it)|^12
        <= (j!)^12 r^(-12j) (1/(2pi))
              integral_0^(2pi)|zeta(1/2+it+r exp(i theta))|^12 dtheta.

Here superscripts on zeta mean complex s derivatives. Tonelli and
(9) consequently prove

    integral_[H,2H]|zeta^(j)(1/2+it)|^12 dt
        <= C_j H^p ell^(12j),                         j=0,1,2. (10)

### Ordinary Hardy jets

L391 (3), including its audited real-ray phase bounds, gives the exact
zero-safe identities, writing h_j=zeta^(j)(1/2+it),

    x=-R h_0,
    y=-R i(h_1+Omega h_0)/L,
    z=-R(-h_2-2Omega h_1-Omega^2 h_0+i Omega' h_0)/L^2.

Here |R|=1, Omega=O(ell), Omega'=O(1/H) on [H,2H], and
ell<=L<=2ell for large H. These retain both i factors and Omega'.
No divisor has been differentiated and no Hardy value has been divided
out. Each of |x|,|y|,|z| is therefore at most

    C (|h_0|+|h_1|/ell+|h_2|/ell^2).

The finite-sum inequality |b_1+...+b_m|^12<=m^11 sum |b_k|^12,
together with (10), proves (1). The Cauchy logarithms are exactly
canceled by these normalized jet divisors. Since the real jets obey
U^6<=(3^5)(|x|^12+|y|^12+|z|^12), (2) follows with no extra
height or logarithmic loss.

### Complete physical weight and positive-set concentration

To verify the full physical estimate, use L390 (5), not just its
leading replacement:

    Delta=(xv_2-zv_0)^2-4(xv_1-yv_0)(yv_2-zv_1)
                  +4q/L^2 (xv_1-yv_0)^2,
    v_j=(G/A)^(j)/(T^2 L^j), q=(log A)''=O(T^(-2)).

L390 bounds the complete response triple by a fixed V. Each minor
has modulus at most sqrt(2)V sqrt(U), so

    |Delta| <= (10V^2+8|q|V^2/L^2)U <= C U.

This includes the entire envelope-curvature correction. Absolute
convergence of the complete right-line series gives
|a|<=|Z|<=zeta(5/2), and f^2=x^2<=U. For exactly Y=Delta W^2,
with W=a f, it follows that

    |Y|<=C U^2,
    integral_[H,2H]|Y|^3 dt <= C_Y H^p.               (11)

L401 (1), (3), in the fixed direction u=(1,0,0), v=0, gives

    integral_[H,2H]Y dt=gamma H ell^4+o(H ell^4),
    gamma=Psi/(71680 pi^2 zeta(2))>0.                 (12)

Its audited sequential-limit argument retains the complete response
and sharp endpoints, for all real H; Psi is fixed and finite. At one
fixed onset (12) is at least (gamma/2)H ell^4. Let
E_H={t in [H,2H]:D(t)>0}. By continuity this is measurable, and
A^4 T^4 L^4>0 makes it equal to {Delta>0}. On its complement
Y<=0 since W^2>=0, even at zeros of W. Hölder with exponent three
on E_H gives

    (gamma/2)H ell^4
        <= integral_E_H Y dt
        <= meas(E_H)^(2/3)(integral_E_H |Y|^3 dt)^(1/3)
        <= meas(E_H)^(2/3)(C_Y H^p)^(1/3).

All these integrals are finite. Cubing, dividing by positive quantities
and taking the nonnegative square root gives

    meas(E_H)>=((gamma/2)^(3/2)/sqrt(C_Y))
                           H^((3-p)/2) ell^6.

Since (3-p)/2=1/2+d/4, this is (3). Maximizing the finitely many
fixed onsets supplies a single H_0 valid for every real H>=H_0.
With ell>=1 it also implies the target with K=0. There is no lower
bound for W and no phase-independence premise anywhere in this step.

The ratio of (3)'s scale to H is H^(-1/2+delta)ell^6, tending to
zero. This result constrains positive discriminant exceptions but
gives neither positive density nor a total L367 signed margin, actual
common-zero upper count, global mixed positivity, extended Laguerre
sign/zero-exclusion range or RH conclusion. L394/L399/L400's narrower
weight failures remain unchanged. The separate specialization audit below
does not independently audit the new scalar source.

### Separate critical audit — 2026-10-13, step 98

This REPRODUCTION proof_audit uses the unchanged prior SPECIALIZE scope in
`drafts/literature/2026-10-12-beyond-half-power-critical-audit.md`.
It checks (1)-(3), with L390's complete physical identity, L391's
ordinary jets, L401's audited exact positive direction and L403's
audited transfer framework as inputs. The scalar preprint Theorem 10.1
is imported with the precise version and qualification given above;
this is not an independent audit of its proof. The existing source
assessment covers the theorem and all analytic tools used here.

**Fixed scalar saving and analytic hypotheses.** With d=520/445121,
epsilon=d/2 is a positive constant fixed before H, and 1<p=2-d/2<2.
Thus (4) provides one bound C_d V^p for every real V>=1. Conjugation
extends its integral bound to symmetric height intervals. The entire
function (5) cancels the sole zeta pole, including at s=1, where
(s-1)zeta(s) tends to 1. The Euler-summation remainder is locally
uniformly absolutely convergent for Re s>0. Multiplying its displayed
identity by s-1 gives exactly the claimed polynomial majorant on the
closed strip. For each fixed H that polynomial times the Gaussian
tends to zero uniformly across the strip at both imaginary infinities
and has an integrable twelfth power. These check the hypotheses of
AOR Proposition 3.3 on the bounded strip, without using its half-plane
corollary or requiring uniform-in-H decay at infinity.

On sigma=2 the substitution t=H(v+3/2) gives the integrable majorant
C H(1+|v|)^12 exp(-12v^2); this is O(H^p) since p>1.
On sigma=1/2 the region |t|<=4H costs O(H^p). For both remaining
shells 2^k H<|t|<=2^(k+1)H, k>=2, the reverse triangle inequality
gives |t-3H/2|>=(5/8)|t|. The twelfth-power exponential therefore
costs at most C exp(-(75/16)4^k), which is bounded by the displayed
C exp(-4*4^k). The polynomial multiplier costs C 2^(12k), while
the scalar theorem on [-2^(k+1)H,2^(k+1)H] costs C H^p 2^(pk).
The resulting full shell majorant is summable with an H-independent
constant. There is no omitted negative-height tail or residual log
factor. Strip log-convexity has constant one and gives (7) uniformly
in sigma and H; it consumes none of the fixed height saving.

**Every complex shift and ordinary derivative.** On J_H, for the stated
right-hand strip, |s-1|/H>=t/H>=1/2 and the Gaussian modulus is at
least exp(-1). Restriction and removal thus cost at most (2e)^12.
For the reflected left strip, uniform sector-qualified Stirling gives
|chi(1/2-u+it)|<=C t^u; on J_H and 0<=u<=1/ell this is bounded
by C exp(log(3H)/ell), uniformly for large real H. Conjugation puts
the reflected factor on the controlled right strip. Every imaginary
shift of modulus at most 1/ell maps [H,2H] inside J_H. These checks
prove (9) over the entire complex disk, not merely on real shifts.

The radius-1/ell Cauchy circle is disjoint from the pole. Cauchy's
formula on normalized angular measure has prefactor j! ell^j;
the twelfth-power convexity inequality and Tonelli give (10) with
(j!)^12 ell^(12j). Differentiating f=-R h_0, using R'=i Omega R
and h_j'=i h_(j+1), reproduces all three displayed Hardy jets,
including +i Omega' h_0 within the second derivative bracket.
L391's separate bounds Omega=O(ell), Omega'=O(1/H) apply on the
whole interval. Since ell<=L<=2ell, division after differentiation
bounds each normalized jet by the stated three-term sum. This remains
true at every Hardy zero. Its twelfth-power inequality and
(x^2+y^2+z^2)^6<=3^5(|x|^12+|y|^12+|z|^12) establish (1)-(2),
with neither a height-power loss nor an additional logarithm.

**Complete physical restriction and exponent.** In L390's exact
identity each minor is bounded by sqrt(2)V sqrt(U), because the full
response triple is uniformly bounded by V. Thus the first squared
minor costs at most 2V^2 U, the product term at most 8V^2 U and
the curvature term at most 8|q|V^2 U/L^2. This proves the full
|Delta|<=C U, including the envelope correction. Absolute convergence
on Re s=5/2 bounds |a| by zeta(5/2). The exact weight W=a f
therefore satisfies W^2<=zeta(5/2)^2 U. Consequently |Y|^3<=C U^6
and (11) has the same H^p budget, without a head cutoff.

L401's audited direction u=(1,0,0), v=0 has the complete positive
coefficient gamma=Psi/(71680 pi^2 zeta(2)). Its finite positive Psi
and fixed-head, sharp-endpoint and full-tail limits are taken in the
audited order and give (12) for all real H. Fixing one onset makes
the mean at least (gamma/2)H ell^4. Since Y<=0 off E_H, restriction
increases this lower bound even if W vanishes. Hölder with exponents
3 and 3/2 gives exactly

    meas(E_H)^2 >= ((gamma/2)^3/C_Y) H^(3-p) ell^12.

Taking its nonnegative square root proves (3), since
(3-p)/2=(1+d/2)/2=1/2+130/445121. The normalizing divisor is
strictly positive, so the set is indeed {D>0}. Maximizing the finitely
many onsets gives one H_0 for every sufficiently large real H.
No independent phase, lower bound for W, RH or exceptional-height
selection has entered the argument.

**Verdict.** Conclusions (1)-(3) pass unchanged. This audit establishes
their local applicability and exponent accounting; it supplies no new
bound, repaired mathematical error, independent scalar theorem or DAG
input. The ratio to H is H^(-1/2+130/445121)ell^6, tending to zero.
The global mixed-positivity gap, total L367 signed margin and actual
common-zero upper counts remain open. No RH candidate is asserted.
The cited scalar preprint remains an explicit unaudited source input;
full matching Mathlib coverage remains unknown.

## Mathlib

Full matching coverage for the new scalar twelfth moment, its uniform
ordinary-jet specialization and this physical-discriminant measure
bound has not been checked in Mathlib. Availability is unknown, not
claimed absent. Cauchy's formula, Hölder, the zeta functional equation
and Stirling are supporting named tools; no full formalization or
Mathlib completion claim is made. Precise analytic citations and all
needed family-specific applicability checks are given above.
