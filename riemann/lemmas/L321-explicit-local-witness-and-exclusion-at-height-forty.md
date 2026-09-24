# Lemma 321: an explicit local witness bound and exclusion through height forty

**Hypotheses.** Let Ξ(z)=ξ(1/2+iz) be the actual completion of L018. For real a put

H_a(y)=Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0)D_n(Ξ;a)y^(2n).

Use the anchor lower bound A(a) of L266, with η=3/2. Set R=7/2, p=η²/R²=9/49, and, for a>0,

M(a)=72a(a+4)^6(a+2)^2 exp(−πa/2).

The analytic witness bound below requires no interval-arithmetic contract. For the exclusion conclusion, assume L037's arithmetic contracts as inherited by L314 and L315. These do not include an independently verified implementation. Euler's gamma integral, reflection formula and recurrence are the standard inputs recorded in foundations.

**Conclusion.** For 20≤|a|≤40,

max_(|y|=7/2)|H_a(y)|≤M(|a|),
M(|a|)/A(a)<43·10^9,
K_loc(a):=ceil(log(2M(|a|)/(A(a)(1−p)))/log(1/p))≤15.       (1)

Every hypothetical nonreal zero of Ξ with such a real center therefore forces D_n(Ξ;a)<0 for some 1≤n≤15, including when Ξ(a)=0. L315's established signs through seventeen contradict this. Together with L314, Ξ has no nonreal zero with |Re z|≤40 under the stated arithmetic contracts. Equivalently, every nontrivial zeta zero with |Im s|≤40 has Re s=1/2 under those contracts.

This extends the bounded exclusion interval, without proving any new coefficient sign, all-level positivity beyond height ten, or the signs required at unbounded heights. It is not an RH candidate.

**Proof.** We give all constants in the local circle estimate. This uses the common gamma decay identified in L320, but does not use its unspecified strip constants.

First, for 1/4≤x≤2 and t real,

|Γ(x+it/2)|≤4|Γ(2+it/2)|.                                (2)

For x<2, the beta integral identity gives

Γ(x+it/2)Γ(2−x)/Γ(2+it/2)
  =∫_0^1 u^(x+it/2−1)(1−u)^(1−x)du.

For completeness, this identity follows by multiplying the two absolutely convergent Euler integrals and making the change of variables (v,w)=(ru,r(1−u)), with Jacobian r. Absolute convergence follows from x>0 and 2−x>0, so Fubini and the change of variables are valid. The radial integral is Γ(2+it/2); the same calculation with t=0 gives the positive beta integral. Taking absolute values and cancelling Γ(2−x)>0 thus yields

|Γ(x+it/2)|≤Γ(x)|Γ(2+it/2)|/Γ(2).

Here Γ(2)=1. Hölder applied to Euler's integral gives Γ(x)≤1 on [1,2], by interpolation between Γ(1)=Γ(2)=1. For 1/4≤x<1, recurrence gives Γ(x)=Γ(x+1)/x≤1/x≤4. This proves (2), including x=2 directly. No assertion of complex log-convexity is needed.

For t≥1, exact reflection and recurrence give

|Γ(1+it/2)|²=(πt/2)/sinh(πt/2)
             =πt exp(−πt/2)/(1−exp(−πt))
             <8t exp(−πt/2).                              (3)

Indeed 1<π<4 and e>2 imply exp(−πt)<1/2. The elementary π bounds follow, for example, from π/4=∫_0^1(1+u²)^(−1)du; e>2 follows from its positive series. Therefore (2), (3) and |1+it/2|≤(t+2)/2 imply

|Γ(x+it/2)|≤2(t+2)sqrt(8t) exp(−πt/4),
                         1/4≤x≤2, t≥1.                  (4)

Next, for s=σ+it with 1/2≤σ≤4 and t≥1, Euler summation gives

ζ(s)=s/(s−1)−s∫_1^∞{v}v^(−s−1)dv,
|ζ(s)|≤|s|/|s−1|+|s|/σ≤3(t+4).                           (5)

To justify the identity without an estimate in the critical strip as a premise, start with ζ(s)=s∫_1^∞floor(v)v^(−s−1)dv on Re s>1, where termwise integration is absolutely convergent. Split floor(v)=v−{v}. The fractional-part integral converges locally uniformly for Re s>0, since 0≤{v}<1, so meromorphic continuation proves the displayed identity there. In the specified rectangle |s−1|≥t≥1, 1/σ≤2, and |s|≤t+4; these prove the inequality in (5). The pole at s=1 is outside this range.

L018's completed-zeta formula, |s(s−1)|≤(t+4)², π^(−σ/2)≤1, (4) at x=σ/2, and (5) now give

|ξ(σ+it)|≤3(t+4)^3(t+2)sqrt(8t) exp(−πt/4),
                         1/2≤σ≤4, t≥1.                  (6)

Let 20≤a≤40 and y=u+iv with |y|=7/2. The two factors of H_a are

ξ(1/2−u+i(a−v)),             ξ(1/2+u+i(a+v)).

Apply ξ(s)=ξ(1−s) to whichever real part is below 1/2, and then conjugate when necessary to make the imaginary part positive. Both factors in modulus have real part 1/2+|u|∈[1/2,4], with heights t_−=a−v and t_+=a+v, respectively. Since |v|≤7/2, both heights are at least 33/2>1. Thus (6) applies to both factors. Their exponential moduli multiply to exp(−πa/2). Moreover

(t_−+4)(t_++4)=(a+4)²−v²≤(a+4)²,
(t_−+2)(t_++2)=(a+2)²−v²≤(a+2)²,
sqrt(t_−t_+)=sqrt(a²−v²)≤a.

Multiplying (6) proves |H_a(y)|≤M(a). Evenness of Ξ gives H_(−a)(y)=H_a(y), so this circle bound also holds for negative a in the stated band.

At η=3/2, L266 supplies H_a(η)≥A(a)>0, where

A(a)=((a²+4)(a²+1)/(4π²ζ(2)²))|Γ(1−ia/2)|².

This lower bound uses the absolutely convergent reciprocal zeta series on Re s=2, and does not require any central value or derivative to be nonzero. For a>0, (3)'s exact identity, sinh x<exp(x)/2, and the decreasing-series estimate ζ(2)<1+∫_1^∞v^(−2)dv=2 yield

A(a)=a(a²+4)(a²+1)/(8πζ(2)² sinh(πa/2))
     >a^5 exp(−πa/2)/(4πζ(2)²)
     >a^5 exp(−πa/2)/64.                                 (7)

The exponential factors cancel in the ratio. For 20≤a≤40,

M(a)/A(a)<4608(a+4)^6(a+2)^2/a^4
         =4608a^4(1+4/a)^6(1+2/a)^2
         ≤4608·40^4·(6/5)^6·(11/10)^2
         =26638226030592/625<43·10^9.                     (8)

Finally, since 2/(1−p)=49/20,

[2M(a)/(A(a)(1−p))]p^15
 <(49/20)(43·10^9)(9/49)^15
 =43000000000·9^15/(20·49^14)<1.                          (9)

The last comparison is an exact integer inequality: 43000000000·9^15<20·49^14. Equations (8) and (9) prove K_loc(a)≤15. They need no decimal approximation or computed value of Ξ. All hypotheses of the general comparison in L266 hold: H_a is even entire with real coefficients, the anchor has a positive lower bound, the complex circle has the stated majorant, and a nonreal zero may be conjugated to have 0<b<1/2<η<R by L018. Its negative-witness conclusion therefore applies even if a is itself a zero.

L315 proves D_n(Ξ;a)>0 for every 1≤n≤17 throughout 20≤|a|≤40 under the inherited arithmetic contracts. It covers all fifteen required indices, giving the contradiction on this band. L314 excludes nonreal centers for |a|≤20 under the same contracts, so their union proves the exclusion through forty. L018's exact change of variables z=(s−1/2)/i identifies Re z=Im s and Im z=1/2−Re s; this proves the final zeta formulation. ∎

The comparison sought was a cutoff at most seventeen; the achieved cutoff is at most fifteen. This deliberately coarse explicit estimate suffices on the bounded band; it does not improve L320's asymptotic leading coefficient. No extrapolation of the finite certificates is used. In particular their all-level conclusion still stops at ten, and the low logarithmic and sublogarithmic indices in the unbounded-height witness target, together with the endpoint arithmetic margin, remain unresolved. Reproduction of the exact arithmetic checks is `python3 scripts/laguerre/check_local_witness_bound.py`; its inspection of the inherited sign certificate checks saved source digests, interval coverage and rational margins, not the Fourier quadrature or the Decimal implementation.

**Mathlib.** Full statement: not checked. Coverage of the beta-integral bound, reflection/recurrence estimates, local circle majorant and finite exclusion assembly is not checked; no full match is claimed. L266 retains L001's supporting reciprocal-series results, recorded there as present and not rechecked here: [`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius) and [`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff). These support the anchor, not the full statement. The exact gamma modulus is the consequence of the standard [Euler reflection formula, DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3) and recurrence already recorded in foundations; [DLMF 5.4.3](https://dlmf.nist.gov/5.4.E3) gives the equivalent modulus at real part zero. These classical supporting references are not Mathlib coverage claims and were not rechecked in this step. The beta identity and all quantitative bounds needed here are proved above.
