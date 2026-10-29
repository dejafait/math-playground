# Corollary 464a: explicit quadratic-order Xi tail

## Hypotheses

Let Ξ be the actual Xi function, with normalization and multiplicities
as in L464, and define D_p by

    Ξ(t+iy)Ξ(t−iy)=Σ_(p≥0) D_p(Ξ;t)y^(2p).

Use L464's product comparison and L467's unconditional closed-unit-shell
bound A=18. Logarithms are natural. No RH, simplicity or external
fixed-half-plane hypothesis is assumed.

## Conclusion

For every real t≥2 and every integer p≥154369 log²(t+2),

    D_p(Ξ;t)>0.

This includes equality in the order threshold and centers t that are
zeros, with any multiplicity. It is a conservative quantitative
specialization of the known product tail. It leaves an initial segment
unchecked and proves neither RH nor an effective logarithmic-order or
common-height onset.

## Proof

The complete sums from L464 admit elementary integral majorants.
Since x↦x⁻² is positive and decreasing,

    S_0=Σ_(k≥2) k⁻²≤1/4+∫_2^∞ x⁻² dx=3/4.

For f(x)=log(x+3)/x² and x≥2,

    f'(x)=x⁻³[x/(x+3)−2log(x+3)]<0.

Indeed x/(x+3)<1 and log(x+3)≥log 5>log 2>1/2,
where the last bound follows by integrating 1/u>1/2 on 1≤u<2.
The decreasing-function integral comparison therefore gives

    S_1=Σ_(k≥2) f(k)≤log 5/4+∫_2^∞ log(x+3)/x² dx
        =(3/4)log 5+(1/3)log(5/2).

For the equality, integration by parts gives the integral as
log 5/2+∫_2^∞ 1/[x(x+3)] dx. The remaining primitive is
(log x−log(x+3))/3, with limit zero at infinity, giving
(1/3)log(5/2). The integration-by-parts boundary term vanishes:
for u≥1, log u≤∫_1^u dv/√v=2(√u−1), whence
log(x+3)/x→0. Thus the full infinite tails are included.

The positive exponential series gives exp(2)>1+2+2=5 and
exp(1)>1+1+1/2=5/2. Consequently log 5<2,
log(5/2)<1, and S_1<3/2+1/3=11/6. Also
log 4=2log 2>1. No floating-point logarithms are used.

Substitute A=18 from L467 in L464's displayed constants. Then

    a=8A=144,
    b=A(2S_0+3S_1/log 4)<18(3/2+3·11/6)=126,
    C_* = a/log 4+2(17/4)ab+1
        <144+(17/2)·144·126+1
        =144+154224+1=154369.

All these bounds are independent of t and p. To check the sufficient
order explicitly, set L=log(t+2)≥log 4. L464 gives M≤aL and
U_t≤bL. Therefore

    C_*L²=aL²/log 4+2(17/4)abL²+L²
           ≥M+2(17/4)M U_t+L².

Thus p≥154369L² implies p≥M and
p−M+1≥2(17/4)M U_t. If M≥1, L464's strict comparison
applies, even at equality in the stated numerical threshold. If M=0,
its infinite positive product has every coefficient strictly positive
without a threshold. Multiplication by L464's positive scalar C_t gives
the conclusion. That scalar does not divide by Ξ(t); central zeros and
all multiplicities are included. The index is p and the exponent is
2p throughout; no conversion from p to 2p occurs. ∎

The source product theorem is bramble_trace, *Generalized Laguerre
positivity at growing orders*, paper 41 v4 (24 October 2026, 07:18 UTC),
Section 4.3 (18c)–(18h),
[primary source](https://rstation.ai/problems/riemann_hypothesis/papers/41),
reproduced in L464. The explicit count input is Bellotti–Wong,
*Improved estimates for the argument and zero-counting function of the
Riemann zeta-function*, arXiv:2412.15470v2 (7 July 2025), Theorem 1.1,
p. 1 and Section 5, pp. 23–24,
[versioned source](https://arxiv.org/pdf/2412.15470v2), specialized and
locally audited in L467. Source computations remain cited inputs;
no independent full-manuscript audit is claimed. The sum majorants and
numerical substitution above supply the quantitative difference; the
product theorem and shell estimate are reused without reproof.

### Critical audit — 2026-10-26

The bounded audit passes under the invocation-start SPECIALIZE scope.
It confirms the existing numerical specialization; it changes neither
the bound nor its mathematical inputs. The cited product and shell
results are reused, without a full-manuscript audit.

For each positive decreasing f used above, the comparison is of the
entire remainder: Σ_(k≥3) f(k)≤∫_2^∞ f(x) dx. The derivative of
log(x+3)/x² has the displayed negative sign on the full domain x≥2,
not just at integer points. Integration by parts on [2,R] gives

    ∫_2^R log(x+3)/x² dx
      =log 5/2−log(R+3)/R
        +(1/3)[log R−log(R+3)−log 2+log 5].

The bound log(R+3)≤2(√(R+3)−1) makes the first infinite boundary
zero; log R−log(R+3)=−log(1+3/R) also tends to zero. This proves
the asserted full S_1 majorant with no truncated tail. All subsequent
upper bounds have the required direction: S_0≤3/4, S_1<11/6 and
log 4>1 imply b<126, while a/log 4<144. Exact arithmetic gives
(17/2)·144·126=154224 and 144+154224+1=154369.
The rational identities are independently checked in
drafts/audits/2026-10-26-c464a-exact-arithmetic.json; that certificate
does not certify the analytic inequalities or replace their proofs.

For every t≥2, L≥log 4>0 implies aL²/log 4≥aL≥M;
also abL²≥M U_t because both factors are nonnegative. Consequently
p≥154369L²>C_*L²≥M+2(17/4)M U_t+L². This verifies both sufficient
conditions in L464 for every real t≥2, including t=2 and equality
p=154369L² when that value is an integer. L464's relative remainder
is at most exp(1/2)−1<1, so strict positivity is retained, rather than
merely nonnegativity. The same log 2>1/2 bound above proves
exp(1/2)<2. No sampling in t or p is used.

For M=0, L464 has infinitely many positive linear factor coefficients,
so its finite-product argument gives g_p>0 at every nonnegative
integer p. For M≥1, repeated and zero roots are expressly allowed.
A central zero of multiplicity m contributes x^m to B_t, hence
m≤M≤p; the threshold does not mistakenly claim positivity below
that forced zero order. The positive C_t is constructed using only
far constant terms and the original paired-product denominators,
not Ξ(t) or a near constant term. Thus central multiplicities do
not invalidate normalization. Finally D_p is the coefficient of
x^p=y^(2p), so the numerical bound is on p itself. No extra factor
of two, height restriction, RH or simplicity premise is required.

No defect was found in this local claim. Initial signs at unbounded
heights, effective logarithmic-tail onset and global mixed positivity
remain unresolved. Mathlib coverage remains unchecked.

## Mathlib

Full matching and supporting coverage have not been checked. Unknown
coverage is not absence. No Lean verification is claimed. The rational
certificate checks only the displayed arithmetic; the bounds and
all-height conclusion rely on the exact analytic proof above.
