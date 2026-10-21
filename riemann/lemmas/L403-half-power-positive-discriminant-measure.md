# Lemma 403: a half-power lower bound for the positive physical discriminant set

## Hypotheses

Use the fixed actual functions of L389/L390/L391/L401, for real t>=40:

    T=1+t, L=log(2+t), f=F_0/A,
    R=exp(i phi), Z=zeta(5/2+it), a=Re(RZ), W=a f,
    X=(x,y,z)=(f,f'/L,f''/L^2), U=x^2+y^2+z^2,
    D=(2F_0'G'-F_0 G''-F_0''G)^2
          -4(F_0'^2-F_0 F_0'')(G'^2-GG''),
    Delta=D/(A^4 T^4 L^4).

A is the positive real gamma envelope, and primes on f,F_0,G are
ordinary height derivatives. All functions, phases and the complete
right-line zeta value are the actual ones. H tends to infinity through
all real values. There is no RH, conjectural higher moment, independent
phase, response truncation, growing order, weight lower bound, simplicity,
disjointness, common-zero bound or favorable total pencil-margin premise.

## Conclusion

There exist fixed constants C,c>0 and H_0>=40 such that for every real
H>=H_0, writing ell=log H,

    integral_[H,2H] |f^(j)(t)/L(t)^j|^12 dt
        <= C H^2 ell^17,                  j=0,1,2,       (1)
    integral_[H,2H] U(t)^6 dt <= C H^2 ell^17,            (2)
    meas{t in [H,2H]:D(t)>0}
        >= c H^(1/2) ell^(-5/2).                         (3)

Constants and onset are existential, not numerically evaluated. This
improves L402's H^(1/3)ell^4 lower bound eventually, since the ratio is
H^(1/6)ell^(-13/2) times a fixed positive constant. It remains sublinear
and asserts neither positive density nor an RH consequence. The separate
step 94 critical audit below validates (1)-(3); this is a local REPRODUCTION of known-source
tools, not a new higher-moment theorem or a complete RH candidate.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-positive-discriminant-higher-moment-concentration.md`.
The needed specialization is not stated directly in the sources: we
must localize their scalar bound, verify the strip-convexity hypotheses,
retain the ordinary phase derivatives and apply the exact physical weight.
No reproof of the scalar moment theorem or strip-convexity theorem is
needed. A Gaussian entire window suffices here because we require no
Fourier-support restriction; we verify its complete tails directly rather
than needing the more general AOR Lemma 3.5 window construction.

### Imported analytic inputs

D. R. Heath-Brown, *The twelfth power moment of the Riemann zeta-function*,
Q. J. Math. Oxford (2) 29 (1978), 443–462,
[Theorem 1, p. 444](https://wiki.math.ntnu.no/_media/ma3001/2025h/analyticnumbertheory/heathbrowntwelfthmoment.pdf#page=2),
DOI [10.1093/qmath/29.4.443](https://doi.org/10.1093/qmath/29.4.443),
gives the unconditional bound

    integral_0^V |zeta(1/2+it)|^12 dt
        <= C_0 V^2 (log V)^17,                  V>=V_0. (4)

The displayed formula in the original scan was not readable in the
retrieval used for the assessment. Its exact finite-log statement and
attribution were inspected in A. Ivic, *On some mean value results for
the zeta-function and a divisor problem*,
[arXiv:1406.0604v1, Lemma 10 and proof, p. 7](https://arxiv.org/pdf/1406.0604v1#page=7).
We import this named scalar theorem only, not a derivative theorem or an
RH-dependent sharp k=6 bound.

L.-P. Arguin, F. Ouimet and M. Radziwill, *Moments of the Riemann zeta
function on short intervals of the critical line*, Ann. Probab. 49
(2021), 3106–3141,
[arXiv:1901.04061v4, Proposition 3.3, p. 22](https://arxiv.org/pdf/1901.04061v4#page=22),
states the integral strip-convexity theorem: for p>0 and a function F
analytic on the closed vertical strip and tending uniformly to zero at
imaginary infinity, the finite integrals
I(sigma)=integral_R |F(sigma+it)|^p dt are log-convex in sigma. In
particular each is at most the maximum of the two boundary integrals.
We apply it with p=12 and strip [1/2,2].

The fixed-order Cauchy/Holder transfer is the calculation in
M. J. Curran and A. Heycock, *Sharp bounds for joint moments of the
Riemann zeta function*,
[arXiv:2403.00902v1, Section 4, p. 8](https://arxiv.org/pdf/2403.00902v1#page=8).
We write that calculation below with the standard j! Cauchy prefactor;
the reciprocal-factorial typo in that source is not used. Its subsequent
sharp moment for k>2 assumes RH and is not imported. The zeta functional
equation, conjugation and sector-qualified Stirling formula are the
standard named inputs already used in L391.

### Pole cancellation, uniform decay and complete localization tails

Fix H sufficiently large, put b=3H/2 and define the entire function

    F_H(s)=[(s-1)/H] zeta(s) exp((s-i b)^2/H^2).       (5)

Zeta's only pole is the simple pole at s=1, so (s-1)zeta(s) has a
removable singularity there and is entire. To check all strip-growth
hypotheses explicitly, the first Euler summation formula is

    zeta(s)=s/(s-1)-s integral_1^infinity {v} v^(-s-1) dv,
                                                        Re s>0, s!=1.

For Re s>1 this follows by integrating floor(v) term by term and
splitting floor(v)=v-{v}; the remainder integral is absolutely and
locally uniformly convergent on Re s>0 and continues the identity
there. Its absolute value is at most 1/Re s. Thus on [1/2,2],
|(s-1)zeta(s)|<=|s|+2|s||s-1|, also at s=1 by continuity.
The elementary formula is used only to verify the localization
hypotheses, not to replace the twelfth-moment theorem.

Since for s=sigma+it

    |exp((s-i b)^2/H^2)|
        =exp((sigma^2-(t-b)^2)/H^2),                  (6)

F_H tends uniformly to zero as |t| tends to infinity on the closed
strip, and all its twelfth integrals there are finite. The uniform
polynomial bound above times this Gaussian proves both assertions
for each fixed H. No compact analytic support is asserted.

We now prove boundary bounds with constants independent of H.
At sigma=2, absolute convergence gives |zeta(2+it)|<=zeta(2).
Substituting v=(t-b)/H into (6) gives

    I_H(2):=integral_R |F_H(2+it)|^12 dt
       <= C H integral_R (1+|v|)^12 exp(-12v^2) dv
       <= C H.                                      (7)

Here |1+it|/H<=H^(-1)+|v+3/2|<=C(1+|v|), and
exp(48/H^2) is bounded. At sigma=1/2, split the complete real line
into |t|<=4H and shells 2^j H<|t|<=2^(j+1)H for j>=2.
On the first piece the twelfth power of the multiplier in (5) is
bounded, and conjugation plus (4) bounds its integral by
C H^2 ell^17. On the j-th shell,

    |t-b| >= |t|-3H/2 >= (5/8)|t|,
    |(s-1)/H|^12 <= C 2^(12j),
    |exp((s-i b)^2/H^2)|^12 <= C exp(-4*4^j).

Restriction of the nonnegative scalar integral (4), together with
|zeta(1/2-it)|=|zeta(1/2+it)|, bounds the shell contribution by

    C H^2 ell^17 2^(14j)(1+j)^17 exp(-4*4^j).

The displayed series over j>=2 converges to a fixed finite constant:
the double-exponential factor dominates its polynomial and exponential
factors. This controls both full tails, without discarding distant or
negative heights. Consequently

    I_H(1/2)<=C H^2 ell^17.                           (8)

Proposition 3.3, with every hypothesis checked above, now gives

    I_H(sigma)<=C H^2 ell^17,                 1/2<=sigma<=2. (9)

Only the maximum-boundary consequence of log-convexity is needed; no
height-dependent convexity loss is introduced.

### Every small shift, sharp endpoints and complex derivatives

Let J_H=[H-1,2H+1], r=1/ell and H>=10, enlarged further if needed
so 1/2+r<=2. For t in J_H and 1/2<=sigma<=1/2+r,
|(s-1)/H|>=t/H>=1/2 and |t-b|/H<=1/2+1/H<=1.
Thus (6) implies that the modulus of the multiplier in (5) is at
least 1/(2e), uniformly in H,t,sigma. Restricting (9) therefore yields

    integral_J_H |zeta(sigma+it)|^12 dt
        <= C H^2 ell^17,               1/2<=sigma<=1/2+r. (10)

For sigma=1/2-u, 0<=u<=r, the functional equation gives

    zeta(sigma+it)=chi(sigma+it)zeta(1-sigma-it).

Uniform Stirling on this fixed near-critical strip at t in J_H gives
|chi(sigma+it)|<=C t^u. Since t<=3H, u<=1/ell and H is large,
t^u<=exp(log(3H)/ell)<=C. Conjugation changes the remaining zeta
modulus to |zeta(1/2+u+it)|. Hence (10) also holds throughout
1/2-r<=sigma<=1/2. In particular for every complex w with |w|<=r,
the substitution tau=t+Im w maps [H,2H] into J_H and gives

    integral_[H,2H] |zeta(1/2+it+w)|^12 dt
        <= C H^2 ell^17,                    uniformly in w. (11)

These restrictions of nonnegative integrals work for every sufficiently
large real H; neither moving-endpoint subtraction nor an exceptional
height set is used.

Cauchy's formula on the radius-r circle around 1/2+it, followed by
Holder on its normalized angular measure, gives for j=0,1,2

    |zeta^(j)(1/2+it)|^12
       <= (j!)^12 r^(-12j) (1/(2pi))
              integral_0^(2pi) |zeta(1/2+it+r exp(i theta))|^12 dtheta.

No circle meets the pole for these heights. Integrating and applying
Tonelli and (11) gives

    integral_[H,2H] |zeta^(j)(1/2+it)|^12 dt
        <= C_j H^2 ell^(17+12j).                     (12)

### Ordinary Hardy jets with the complete phase derivatives

L389 identifies f as one constant sign times the ordinary Hardy
function on this connected ray, including at its zeros. More
explicitly the zero-safe real-ray specialization of L391 (3) is,
with h_j=zeta^(j)(1/2+it),

    x=-R h_0,
    y=-R i(h_1+Omega h_0)/L,
    z=-R(-h_2-2Omega h_1-Omega^2 h_0+i Omega' h_0)/L^2.

Here |R|=1, Omega=O(ell), Omega'=O(1/H) uniformly on [H,2H],
and ell<=L<=2ell for large H. Thus all three jet moduli are bounded
by a fixed constant times

    |h_0|+|h_1|/ell+|h_2|/ell^2.

This retains Omega' and both powers of i; L^j is a divisor after
ordinary differentiation, not inside it. The elementary inequality
|b_1+...+b_m|^12<=m^11 sum |b_k|^12 and (12) prove (1).
Finally U^6<=(3^5)(|x|^12+|y|^12+|z|^12) proves (2).
No division by a Hardy value occurs at any zero.

### Exact weight and the concentration threshold

L390's full physical bound is |Delta|<=C U uniformly on the
eventual ray. It follows directly from its exact formula (5): the
complete response jets v_0,v_1,v_2 are bounded, its polynomial is
quadratic in X, and the retained envelope-curvature correction is
bounded by C U/(T^2 L^2). Thus this is a bound for Delta itself,
not just its leading replacement d. Absolute convergence gives
|a|<=zeta(5/2), with the entire response retained. Since f^2<=U,
for Y=Delta W^2 we have

    |Y|<=C U^2,
    integral_[H,2H] |Y|^3 dt <= C_1 H^2 ell^17.       (13)

L401 (1), (3), with precisely u=(1,0,0), v=0, gives

    integral_[H,2H] Y dt
       = gamma H ell^4+o(H ell^4),
    gamma=Psi/(71680 pi^2 zeta(2))>0.                 (14)

The complete arithmetic constant is fixed and finite. Absorb the
little-o at one fixed onset for all real H to obtain a lower bound
(gamma/2)H ell^4 in (14). The positive divisor A^4 T^4 L^4 implies
E_H={D>0}={Delta>0}; this set is measurable by continuity. On its
complement Y<=0 because W^2>=0. Restricting there and applying
Holder with exponent 3 on E_H yields

    (gamma/2)H ell^4
       <= integral_E_H Y dt
       <= meas(E_H)^(2/3) (integral_E_H |Y|^3 dt)^(1/3)
       <= meas(E_H)^(2/3) (C_1 H^2 ell^17)^(1/3).

All integrals are finite on the compact interval. Cubing gives
(gamma/2)^3 H^3 ell^12<=meas(E_H)^2 C_1 H^2 ell^17.
Division by positive quantities and taking the nonnegative square root
prove (3), with c=(gamma/2)^(3/2)/sqrt(C_1). A single maximum of
all the fixed onsets supplies H_0. The exact approved threshold is
met with K=5/2; an H^(2+epsilon) moment was never substituted for (4).

This proves only the intermediate concentration statement. The ratio
of its bound to H tends to zero. Global mixed positivity, a total
L367 signed margin and actual common-zero upper counts remain open.
L394/L399/L400's negative-weight results are neither changed nor
contradicted. The separate critical audit below checks this specialization.

### Separate critical audit — 2026-10-12, step 94

This independent REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-12-half-power-positive-discriminant-critical-audit.md`.
It checks (1)-(3) with unchanged hypotheses and constants uniform in real
H, using the inspected primary statements recorded above. It imports the
scalar twelfth moment and bounded-strip convexity, not an RH-dependent
sharp higher moment or the half-plane corollary. The specializations,
rather than those named theorems, are the obligations checked here.

**Analytic domain and boundary integrals.** The pole at 1 is canceled
exactly: the residue-one pole makes (s-1)zeta(s) tend to 1 there.
The Euler-summation integral converges locally uniformly for Re s>0
and is bounded by 1/Re s. Its identity therefore gives the stated
polynomial bound uniformly for 1/2<=Re s<=2, including s=1 by
continuity. For fixed H this polynomial times
exp(-(t-3H/2)^2/H^2) tends to zero uniformly across that closed strip.
The same bound makes every twelfth integral finite. This checks the
actual domain of AOR Proposition 3.3; decay as Re s tends to infinity
is neither needed nor claimed.

On the right boundary, t=H(v+3/2) leaves the integrable majorant
C H(1+|v|)^12 exp(-12v^2). On the left boundary, |t|<=4H
costs C times the scalar integral over that whole interval, hence
C H^2 ell^17 by conjugation and (4). For j>=2, the two shells
2^j H<|t|<=2^(j+1)H obey |t-3H/2|>=(5/8)|t|;
the exponential in the twelfth power is at most
C exp(-(75/16)4^j), which is bounded by C exp(-4*4^j).
The pole-removal factor costs at most C 2^(12j), and (4) on the
larger symmetric interval costs C 2^(2j)H^2(ell+j)^17.
Since ell>=1, their product is bounded by the displayed summable
shell majorant in the construction. Thus neither negative heights nor
either infinite tail is omitted, and its sum has an H-independent
constant. Boundary log-convexity, with interpolation constant one,
proves (9) without an extra power of H or log H.

**Shifts and ordinary derivatives.** On J_H, t/H>=1/2 and
|t-3H/2|/H<=1 for all sufficiently large H. The multiplier modulus
is consequently at least 1/(2e); removal after restriction costs
only (2e)^12. The functional-equation factor on sigma=1/2-u,
0<=u<=1/ell, is bounded uniformly by C t^u<=C exp(log(3H)/ell).
Conjugation places the reflected value on the already controlled
right-hand strip. Every vertical shift on the radius-1/ell disk
maps [H,2H] into J_H. These are nonnegative integral restrictions,
valid for every real H above a single onset, not differences of
asymptotics at shifted endpoints.

The exact normalized-angular Cauchy formula has prefactor j! r^(-j).
Jensen/Hölder for the twelfth power and Tonelli therefore give precisely
(12), with (j!)^12 and ell^(12j). The entire circle is far from s=1.
L389's phase comparison is made between nonzero gamma phase factors,
not by dividing by zeta; hence the constant-sign Hardy identity survives
all its zeros. Direct differentiation of f=-R h_0, R'=i Omega R,
and h_j'=i h_(j+1) gives exactly the displayed x,y,z formulas,
including +i Omega' h_0 within the second derivative bracket.
The separate bounds |Omega|<=C ell and |Omega'|<=C/H from L391
bound every coefficient after division by L or L^2, with L comparable
to ell. No derivative of the divisor is part of these ordinary jets.
The finite-sum inequalities then prove (1) and (2), zero-safely.

**Complete physical statistic and Hölder threshold.** To check that the
full physical bound is sufficient, let V bound all three complete
response jets v_j in L390 (5). Each of its three minors has modulus
at most sqrt(2)V sqrt(U). Consequently |Q_0|<=10 V^2 U, while
the curvature term is at most 8|q|V^2 U/L^2. The audited q=O(T^(-2))
therefore gives |Delta|<=C U for the complete discriminant, not merely
its leading polynomial. Since |a|<=zeta(5/2) and f^2<=U, this proves
(13) without a response cutoff or a lower bound for W.

The exact L401 direction is W=a f and its coefficient is
c^2 Psi/(4480 zeta(2))=Psi/(71680 pi^2 zeta(2)), strictly positive
and finite by its audited complete arithmetic sum. Its sharp asymptotic
holds for all real H, after taking fixed-head and smoothing limits in
the audited order. Choosing one onset absorbs its little-o and gives
(14)'s positive lower bound. E_H is measurable; its complement has
Y<=0, even where W vanishes. Thus the positive total mass is bounded
above by integral_E_H Y. Hölder with p=3 gives exactly

    meas(E_H)^2 >= ((gamma/2)^3/C_1) H ell^(-5).

The positive normalizing divisor identifies E_H with {D>0}; taking
the square root yields (3) with the stated constant. All fixed onsets
can be maximized; no exceptional-height or integer-H restriction remains.

**Verdict and limitations.** All three conclusions pass unchanged. There
is no repaired mathematical error, new exponent, new source theorem or
new DAG input. The ratio to L402's lower-bound scale tends to infinity,
but the ratio to H tends to zero. This validates a local known-tool
concentration result, not positive density or a complete RH candidate.
It supplies no total L367 signed margin, common-zero upper count,
global mixed positivity or new zero-exclusion range. The narrower
L394/L399/L400 failures are untouched. Full matching Mathlib coverage
remains unchecked as described below.

## Mathlib

The full matching scalar twelfth-moment, shifted derivative-moment and
physical discriminant measure results have not been checked in Mathlib;
availability is unknown, not claimed absent. Cauchy's formula, Holder,
the zeta functional equation and Stirling are supporting named inputs,
not full matching formalizations of this result. The precise imported
analytic sources and the ordinary-jet applicability argument appear
above; no Mathlib completion claim is made.
