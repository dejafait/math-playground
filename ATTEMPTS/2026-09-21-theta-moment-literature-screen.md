# Actual-theta moment literature screen — 2026-09-21

Outcome: the screened adjacent-moment and shifted-Jensen results do not supply all-degree mixed positivity. This bounded review does not claim to exhaust the literature, and imports no new lemma into the main proof.

**Hypotheses.** Use the actual moments of L021, γ_n=n!M_{2n}/(2n)! as in L028, and H_d of L030. The target is H_d positive semidefinite for every d; C032a would then prove RH. Reviewed the existing changes, whole overview and DAG, and reused the theta-transfer and finite-test obstructions. Searched primary sources for theta-moment inequalities and Jensen hyperbolicity; screened the following exact ranges.

**Conclusion.** No reopening of technical work is justified by these ranges alone. There is a stronger external supply of adjacent-moment inequalities than the notebook’s finite tests, but no established transfer to the signed Newton forms. Large-shift hyperbolicity leaves an infinite uncovered range as degree grows. No RH candidate or certified off-line zero results.

**Proof / source assessment.**

1. G. Csordas and R. S. Varga, *Moment Inequalities and the Riemann Hypothesis*, Constructive Approximation **4** (1988), 175–198, Theorem 2.4, special case f=1 (also explicitly stated in the abstract), [author-hosted paper](https://www.math.kent.edu/~varga/pub/paper_161.pdf), DOI 10.1007/BF02075457. For b_m(λ)=∫₀∞t^{2m}e^{λt²}Φ(t)dt, it gives b_m(λ)²>((2m−1)/(2m+1))b_{m−1}(λ)b_{m+1}(λ), m≥1, λ real, without RH. Only this special case is screened here; the full universal-factor family is not assessed.

The kernel normalization in L019 is K(u)=4Φ(u/2), hence M_{2m}=8·2^{2m}b_m(0). The common scaling cancels in the inequality. The factorial ratio then gives γ_m²>γ_{m−1}γ_{m+1}, so every quadratic J^{2,n}(X)=γ_n+2γ_{n+1}X+γ_{n+2}X² has positive discriminant. At m=1 this recovers M_0M_4<3M_2², already proved in L027. Varying m is varying the coefficient index, not the polynomial degree or the size of H_d. No signed-Newton mixed-form inequality follows from this calculation. The heated inequalities similarly concern different coefficient sequences; no reverse heat implication to RH is being assumed.

2. M. J. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp and I. Wagner, *Jensen polynomials for the Riemann xi-function*, Advances in Mathematics **397** (2022), 108186; [arXiv:1910.01227v3](https://arxiv.org/pdf/1910.01227), equations (1.1)–(1.2), Theorems 1.1–1.2. Their γ is exactly the sequence above. Theorem 1.1 gives hyperbolicity of J^{d,n}=Σ binom(d,j)γ_{n+j}X^j for n≥c exp(d/2), with an absolute c>0. Theorem 1.2 instead assumes RH_m(T) and restricts d≤floor(T)²; it cannot be used as unconditional information at arbitrary height. Its finite-height corollary remains finite in degree.

The first range is not all pairs (d,n): it supplies no n=0 case for d≥1. Adding any fixed degree cutoff D leaves the infinite set n=0, d>D uncovered. In particular “finitely many exceptions for each degree” does not make the union over degrees finite. No reverse implication from high shifts to the missing small shifts is proved by these statements.

3. A recent primary-source search hit, J. Holland, *A new hyperbolicity wedge and a joint semicircle limit for Jensen polynomials of Riemann’s ξ-function*, [arXiv:2608.08682v1](https://arxiv.org/abs/2608.08682v1), submitted 9 August 2026, claims in its abstract a sufficient range n³log²(n+2)≥Kd⁵, K>0. This preprint’s proof was not reviewed or adopted. Even accepting that claimed range would leave every pair n=0,d≥1 outside it. Thus its improved simultaneous range would not itself close this notebook’s gap.

**WHY IT FAILS.** Adjacent-coefficient control, a growing-shift region, and a finite-degree region are each weaker than control of every mixed form. Combining the screened ranges still leaves infinitely many missing cases. This rejects that proposed combination as a completion mechanism, not the theorems or every possible use of their methods. The remaining specific source feature worth screening is the universal-factor quantifier in the 1988 theorem: only an exact conversion of that family into arbitrary mixed forms could change the decision. Another scalar inequality or another Jensen cutoff would not do so.

## Universal-factor review — 2026-09-21

**Hypotheses.** The target remains the original-node form Q(q) of L030 for every real polynomial q. This reviews the previously unassessed quantifier in the same source, without importing a new lemma.

**Conclusion.** The full family supplies no established conversion to that target. Park this source as a completion mechanism; this is not a theorem that no further consequence of the family could prove RH.

**Proof / precise source and conversion check.** Csordas–Varga, cited above, p. 179, equations (2.11)–(2.16), and p. 181, Theorem 2.4, allow

f(z)=Cz^{2r}∏_j(1−z²/a_j²), with r≥0 integral, a_j>0, Σ_j a_j⁻²<∞ and (−1)^r C>0.

The product can be finite, empty, or infinite. For B_m=∫₀∞t^{2m}e^{λt²}f(it)Φ(t)dt, the conclusion is B_m²>((2m−1)/(2m+1))B_{m−1}B_{m+1} for every m≥1 and real λ. The zero-preservation discussion on p. 177, equations (2.1)–(2.4), requires a transform already having only real zeros and λ≥0. It does not assert unconditional real zeros for these weighted theta transforms. The first proof on p. 181 uses strict concavity of log Φ(√u); the factor contributes nonpositive logarithmic curvature. A constant factor contributes zero, so strictness comes from Φ.

Here is the direct algebraic comparison, rather than identifying the two positivity problems by terminology. For a finite product write

f(it)=A t^{2r}P(t²),  P(u)=∏_{j=1}^k(1+u/a_j²)=Σ_{j=0}^k p_j u^j,  A>0.

All p_j are nonnegative. With b_ℓ(λ)=∫₀∞t^{2ℓ}e^{λt²}Φ(t)dt, finite expansion gives B_m=AΣ_j p_j b_{m+r+j}(λ). Consequently the theorem gives positivity of

A²Σ_{j,k}p_jp_k [b_{m+r+j}(λ)b_{m+r+k}(λ)−κ_m b_{m+r+j−1}(λ)b_{m+r+k+1}(λ)],  κ_m=(2m−1)/(2m+1),

on this restricted product family. This is a quadratic expression in coefficients of positive-root-parameter weights and in ordinary moments. It is not Σ c_jc_k S_{j+k+2}. The latter involves the logarithmic coefficients of the original transform, including the subtractions in L025/L040. No identity equating the displayed expression, or a proved sign-preserving combination of these expressions, to every Q(q) has been supplied.

Two tempting conversions fail at their hypotheses. First, substituting an arbitrary squared polynomial weight is not allowed: P(u)=(1−u)² has a positive root and a negative coefficient, whereas every admissible finite P has negative roots and nonnegative coefficients. The desired q(β)² is in any case evaluated on reciprocal zeros, not on the real integration variable. Second, subtracting inequalities for different admissible factors does not preserve their sign, so polarization cannot simply recover arbitrary signed vectors. Neither observation claims to exclude all possible indirect uses of the family.

Infinite products do not remove this immediate obstruction. Their finite partial products converge locally uniformly since Σ a_j⁻²<∞; all Taylor coefficients of their limit in u remain nonnegative, by coefficient convergence. They also have no positive real zero: for u>0 the convergent product ∏(1+u/a_j²) is positive. Thus this limit operation does not license the missing arbitrary polynomial substitution. For λ<0 the exponential has alternating coefficients, but its coefficients are linked by one parameter; the theorem still supplies only the displayed weighted moments, not an arbitrary signed test or a logarithmic transfer. No closure or differentiation argument giving the required forms is established.

**WHY IT FAILS (full family).** Uniformity over m, λ and admissible factors is not the required uniformity over all q for the original nodes. The achieved statement is an unconditional family of weighted adjacent inequalities; the required statement is Q(q)≥0 without any degree restriction. The universal-factor name describes conditional preservation, not creation, of real zeros. There is no new lower bound for the target forms, no candidate, and no rigorous off-line zero. This closes the specific source lead left open by the first screen, while preserving its theorems and all prior counterexamples. Existing generic counterexamples must not be claimed to satisfy this full weighted family without checking the stronger square-root log-concavity input.

## Existing-counterexample hypothesis audit — 2026-09-21

**Hypotheses.** Compare L044 and L055/L057 with strict concavity of ψ(u)=log K(√u), u>0. A counterexample satisfying this stronger input could obstruct deriving all-degree mixed positivity from it. This is a hypothesis audit, not a new kernel construction.

**Conclusion.** L044 fails this hypothesis. L057's recorded curvature bound does not establish it; its status under the stronger hypothesis remains unresolved. Neither existing proof therefore certifies the stronger obstruction. No conversion to the RH criterion follows.

**Proof.** For exactly L044's h, the three positive weights sum to one. At t=√32, 5<t<6, so each of |t|, |t−8|, |t+8| exceeds 2. Hence h(√32)<exp(−cosh 4)<exp(−10), since cosh 4≥1+4²/2+4⁴/24>10. But h(0)≥(9/10)e⁻¹>e⁻¹/20 and h(8)≥e⁻¹/20. Thus ψ(0),ψ(64)≥−1−log 20>−5, using e⁴>20 from its Taylor series. This contradicts the midpoint inequality ψ(32)≥[ψ(0)+ψ(64)]/2. Concavity on the open positive axis would imply this endpoint inequality by continuity at zero, so the endpoint causes no loophole.

For L055 write ℓ(t)=log h_a(t). Direct differentiation gives

ψ''(u)=[tℓ''(t)−ℓ'(t)]/(4t³),  t=√u>0.

The explicit sufficient strict sign is therefore tℓ''(t)−ℓ'(t)<0 for every t>0. L055 bounds only ℓ''(t)<−cosh(2t)/4. Since ℓ is even and strictly concave, ℓ'(t)<0 for t>0, and the subtracted slope contributes positively; it cannot be dropped. Ordinary strict log-concavity does not imply the stronger property: ℓ(t)=−√(1+t²) has ℓ''(t)=−(1+t²)⁻³ᐟ²<0, but d²[ℓ(√u)]/du²=(1/4)(1+u)⁻³ᐟ²>0. This elementary distinction is not proposed as a new RH counterexample.

For the exact existing family, put V_s(t)=cosh(2(t+s)), s∈{−a,0,a}, p_0=cosh(a/10), p_{−a}=p_a=1/2, and w_s=p_s exp(−V_s)/Σ_r p_r exp(−V_r). Differentiating the finite sum gives ℓ'=−Σ_s w_s V_s' and ℓ''=−Σ_s w_s V_s''+Var_w(V_s'). The sufficient strict sign becomes

Σ_s w_s[2sinh(2(t+s))−4t cosh(2(t+s))]+t Var_w(2sinh(2(t+s)))<0.

The existing curvature proof does not bound this combined expression. Pointwise continuity as a→0 does not provide a single nonzero a uniformly on t>0. Near zero, evenness gives tℓ''−ℓ'=ℓ''''(0)t³/3+O(t⁵); thus an absolute perturbation bound alone would not settle that endpoint. These are missing estimates, not a demonstrated sign failure for L055.

**WHY THE EXISTING OBSTRUCTION DOES NOT YET APPLY.** L044 is excluded from the stronger hypothesis, and L057 has an unresolved stronger sign. To obtain the proposed obstruction one must prove square-root concavity for an existing nonzero parameter and check applicability of the source's weighted-moment argument to that kernel. No all-degree bound or RH candidate has been obtained. A bounded uniform-sign check of this existing family has a precise use; further finite Hankel tests do not.

## Uniform curvature resolution — 2026-09-21

The unresolved sign in the preceding historical audit is now settled in the strengthened [L055](../lemmas/L055-the-combined-generic-conditions-admit-nonreal-zeros.md): all sufficiently small positive parameters satisfy strict square-root log-concavity. The full proof is in that lemma; it uses fourth-derivative continuity on [0,17] and the existing global curvature bound on the tail. L057 inherits the stronger condition while retaining every fixed finite collection of positive Hankel tests and explicit nonreal zeros. The parameter still depends on the number of tests.

**WHY THE STRONGER SHAPE ROUTE FAILS.** This closes the hypothesis gap for the existing family without constructing another example. Square-root log-concavity, even combined with the retained generic conditions and finitely many tests, cannot imply real-rootedness. It gives no improved bound for actual-theta Q(q); that target still requires every degree. The complete source-weighted family has not yet been transferred to this kernel, so this result must not be stated as a counterexample satisfying that whole family. That source-applicability question is distinct from the now-proved uniform curvature sign.

## Full weighted-family resolution — 2026-09-21

The preceding applicability qualification is now resolved for exactly the admissible family recorded above. L055 contains a direct proof for every factor (including infinite products), real λ and m≥1. It proves strict increase of the negative logarithmic derivative after u=t², checks both integration-by-parts boundaries and absolute integrability, and uses a strictly positive covariance. Thus it does not require treating a theorem stated for Φ as automatically valid for another kernel, or passing strictness through a limit. The author-hosted PDF was reopened but its image-only pages were not readable in this session; the proof here independently establishes the precise family already transcribed in the earlier review.

L057 consequently supplies, for each fixed N, one nonreal-zero transform satisfying the whole weighted family and H_d positive definite for d≤N. No new kernel or lemma identifier is introduced. All these inequalities together therefore fail to imply real-rootedness in this comparison class. This is stronger than the earlier absence of a known conversion; it still does not exclude a proof using additional theta arithmetic.

**WHY THIS COMPLETION ROUTE FAILS.** The achieved threshold is the complete weighted adjacent family, with all its quantifiers, and any prescribed finite number of Hankel tests, for the same example. The required RH threshold is every mixed form for the actual theta nodes. The comparison transform still has explicit nonreal zeros, so the proposed generic implication cannot supply that threshold. Close this source/comparison route; no further shape refinement or finite test is justified by this lead.

## Shifted-Jensen proof mechanism audit — 2026-09-21

**Hypotheses.** The target remains every actual-theta mixed form nonnegative. An alternative sufficient endpoint is hyperbolicity of J^{d,0} for every d. This review tests the already-screened source, not another finite-degree calculation.

**Conclusion.** Park this source as a completion mechanism. Its proof supplies more than square-root concavity, but no unshifted all-degree estimate. No new lemma is imported.

**Proof / precise citation.** Griffin–Ono–Rolen–Thorner–Tripp–Wagner, cited above, §§2–4: the theta-integral coefficient asymptotics in (3.1)–(3.2) yield uniform logarithmic-ratio estimates (Theorem 2.1). Theorem 2.3 requires M=n+d>max{10k³,M_C}. Lemma 2.4 requires

E_{d,n}=Σ_{j=3}^d 2^(−j)(d−j)!/(d−1)! · c_{d,n,j}²<1,

where c are the Hermite expansion coefficients in (2.8). Equations (2.14)–(2.15) bound its even and odd parts by O_C(d¹³ A_C^d Δ(M)^8) and O_C(d⁹ A_C^d Δ(M)^6), respectively, with A_C=1+√(1+16C²), 1<C<2, and Δ(M)∼(2M)^(−1/2). These are theta-specific asymptotic inputs, not consequences of the comparison kernel’s shape assumptions.

Our endpoint check: taking n=0 and k=d would require d>10d³, impossible for d≥1. Thus the coefficient theorem cannot be applied across the needed range. Even a purely formal substitution M=d into the displayed error envelopes gives exponential factors times d⁹ and d⁶, rather than a bound below one. This substitution is outside the theorem’s domain and is not a valid bound on E_{d,0}; it only diagnoses why extrapolating the error formula would not rescue the argument. Failure of a sufficient error test does not prove nonhyperbolicity.

**WHY IT FAILS.** The required threshold is every unshifted degree. The achieved mechanism controls a high-index coefficient window whose length must be small relative to its location. Increasing d at n=0 moves both endpoints and does not create that regime. The proof therefore adds no bound for the missing mixed forms. This rejects reuse of the recorded estimates at shift zero, not every possible refinement of the method. Further shift-cutoff improvements alone do not justify reopening. No RH candidate or certified off-line zero results.

## Nonasymptotic sign-input screen — 2026-09-21

**Hypotheses.** The required input is unconditional positivity of every actual H_d, for every real vector, or an independent all-zero exclusion theorem. This bounded search used “Riemann xi theta kernel generalized Laguerre inequalities positive definite Csordas” and “Riemann xi logarithmic derivative Hankel positivity theorem theta moments”. The following primary sources were opened; no search snippet is adopted as a theorem. Existing weighted-family and shifted-Jensen screens are retained rather than repeated.

**Conclusion.** No qualifying input was found in this screen. This is neither a literature-exhaustiveness claim nor evidence against RH. No new lemma, candidate, or certified off-line zero is obtained.

**Proof / precise source assessment.**

1. George Csordas, *Fourier transforms of positive definite kernels and the Riemann ξ-Function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055), Theorems 4.5–4.6 and Open Problem 4.7, pp. 11–12. The associated kernels are K_n(t)=∫_R Φ(s+t)Φ(s−t)s^(2n)ds. Theorem 4.5 establishes admissibility; Theorem 4.6 characterizes real zeros by positive definiteness of every K_n. It does not prove that premise. Open Problem 4.7 explicitly asks for the first Laguerre inequality at every real argument. This is an alternate sign interface, not a supplied unconditional sign theorem. Our inference: pointwise positivity of this integrand cannot be substituted for positive definiteness, which quantifies over arbitrary signed/complex test coefficients. Accordingly this source does not justify reopening the associated-kernel route merely by renaming the positivity target. Its normalization is H(x)=Ξ(x/2)/8, so its real-zero target is the same one; no new quantitative estimate for H_d is obtained.

2. Larry X. W. Wang and Neil N. Y. Yang, *Laguerre inequalities and complete monotonicity for the Riemann Xi-function and the partition function*, [institution-hosted manuscript](https://cfc.nankai.edu.cn/_upload/article/files/81/18/f83d37e449ebaf1b2f4141fa59be/9323c2fc-4d6a-4610-a747-1bd985a7be41.pdf), Theorems 1.3, 1.8–1.9, pp. 4–6. Theorem 1.3 states an order-r coefficient inequality for n>cr³, with the quantifiers “for every r, there exists a constant c”; no order-independent constant is inferred here. The other two statements concern finite differences at sufficiently large coefficient indices. Our range check: none supplies n=0 for all r, all real arguments for the entire-function Laguerre expressions, or all mixed reciprocal-zero forms. These are distinct inequalities, so no implication between them is silently imported. This is another asymptotic range, excluded by the screen's threshold rather than a reason to refine its cutoff.

3. Michel Planat and Patrick Solé, *Second-Level Concavity of the Riemann Ξ Kernel*, [arXiv:2608.19160](https://arxiv.org/abs/2608.19160), abstract, submitted 19 August 2026. The authors claim concavity of the logarithm of the first Laguerre expression of Φ(√t), and resulting double Turán inequalities; they expressly make no RH assertion. Only the abstract's scope was screened, not its proof or certificates. Our decision: even accepting that claim supplies no stated arbitrary-order mixed-form theorem. Do not reopen the parked shape route solely to add this fixed level; an explicit passage to every required form would first be necessary.

4. Zhiliang Deng, Xiaomei Yang and Huazhong Lü, *Contour Hankel dynamics and indicator fields for the Riemann Ξ-function*, [arXiv:2608.11520](https://arxiv.org/abs/2608.11520), abstract, submitted 12 August 2026. The proposed contour-Hankel formulation explicitly leaves independent positivity unresolved. Only that scope was screened; no proof is adopted. Our decision: a local reformulation and numerical validation do not supply C032a's missing sign, and importing another equivalent criterion would duplicate the retained reduction's role.

**WHY IT FAILS.** The strongest all-order statement screened is conditional on the very positivity it would need to establish. The unconditional statements or claims concern large coefficient indices or a fixed level of kernel curvature. The achieved bound for the actual target is unchanged: the recorded finite tests, versus all d and all c. Stop this source-screening cycle as a technical reopening strategy; another keyword search, equivalent criterion, or fixed-order estimate has no demonstrated downstream use. A subsequent strategic stop/go review should require a specific new mechanism before further technical work. No universal impossibility claim is intended.

**Mathlib.** Not checked; this is a source and quantifier review, not a new library theorem.

**Lean proof status.** Paused; not required in the current research phase.

**Lean proof command.** Not available.

**Lean proof code.** Not available.
