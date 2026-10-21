# Fixed-regulator negative-sign audit — 2026-10-04

The completed target is the saved covered action: Test the large-frequency sign of F_ε′²−F_εF_ε″ for L357's Gaussian-regulated family at fixed ε>0, tracking whether any negative values occur for arbitrarily small ε.

The prior SPECIALIZE assessment is [the spectral review](literature/2026-10-03-gaussian-regulated-first-spectrum.md), whose COVERED_TARGET matches that action exactly. The separate [arithmetic assessment](literature/2026-10-04-gaussian-logarithmic-form-return-assessment.md) supplies the already read Matveev statement. Neither needs another search for this audit. Read the shared and local instructions, complete overview, DAG, existing working changes and pertinent proofs; preserve the existing L365 and all inactive branches.

## Gap and discriminating test

The main gap is actual-theta mixed positivity, including its low-index signs at unbounded heights. The proposed intermediate certificate was global first-sign nonnegativity for every sufficiently small regulator, which could have passed to theta through L357. L365 instead claims negative actual regulated signs for each sufficiently small fixed regulator. Check its arithmetic applicability, the full-series template, both return inequalities, the same-frequency sign transfer and the order of quantifiers. An invalid implication would require repairing or withdrawing that conclusion; an intact chain retains the stop of this global certificate. Even an intact chain leaves actual-theta first signs, higher low-index signs and the endpoint arithmetic margin unresolved.

This is a critical proof audit of an existing result, not a new source assessment or a new theorem. The full mathematical statements and proofs remain in L358–L365. No numerical scan can decide their eventual quantifiers, so none is used.

## Arithmetic applicability and asymptotic scales

L365 uses the additive form in Matveev, Corollary 2.3, as restated in Sha, §2.4, (2.19), rather than substituting a bound for a product minus one. The precise references and links remain in L365 and the saved arithmetic assessment. For each nonzero prime coefficient, D=1, h(p)=log p, the principal logarithm is real, and A_j=log p exceeds 0.16. Unique factorization proves nonvanishing, including with mixed positive and negative coefficients. The coefficient norm is 1≤B≤K. The one-term case is handled separately by |k log p|≥log 2, so it does not silently invoke the n≥2 source statement.

Rechecked the constant absorption in L365 (4)–(5): log(eB)≤2log(2+K); the residual multiplier is at most 2^(6n+21) max(1,log N)^N. Its logarithm is bounded by 17N+Nlog(N+2)≤18Nlog(N+2), for every real N≥2. Thus C=20 has slack; a factor log 2 below one is never used as a lower bound for the height product.

For R fixed and y=log log H, L364 has N_H=O_R(sqrt(y)), log K_H=2y+O_R(log(y+2)), and -log β_H=O_R(y^(3/2)). The logarithm of the ratio of the Matveev exponent Q_H to log H=e^y is bounded above by

\[
 -y+O_R(\sqrt y\log(y+2))+O_R(\log(y+2))\longrightarrow-\infty.
\]

Hence Q_H=o_R(log H), as is -log β_H. It follows that HΔ_Hβ_H tends to infinity, and so does sqrt(H)β_H. This comparison fixes R before letting H grow; it supplies no uniformity in R. The growing number of primes is included in Q_H, not frozen before applying Matveev. Finite minima over the Fourier support preserve its uniform vector bound.

## Template and infinite-tail audit

L362's construction changes the growing background as well as the three selected prime groups. The restricted-background obstructions in L360–L361 therefore do not apply. Its elementary prime supply gives positive group mass M≥c_a sqrt(R)/log R, with a fixed before R grows. Although c_a can be extremely small, sqrt(R)/log R eventually dominates both sqrt(log N_R) and (log R)sqrt(log N_R). Thus the background and centered-derivative errors divided by M do tend to zero.

For fixed a and large R, N_R<R², whereas every selected prime exceeds aR≥R. No retained integer has two selected prime factors, including a repeated prime. This justifies the finite affine polynomial; it is not asserted for the full series. The latter's C² tail is handled separately by the Gaussian majorant and is o(M). The contraction therefore addresses the full infinite series and retains its nonsingular two-variable Jacobian and nonzero W_R.

L363 allows the third group angle to vary. Its C² bound extends to all three variables because their total multiplicity in n is at most log n/log R. The μ_j lie in fixed compact intervals independent of a and R after centering by log(aR). The perturbed triangle zero and centered derivative therefore have uniform tolerances. At λ=0 its W curve stays close to M e^(iθ)z_R, with |z_R| bounded below. For fixed R, the perturbation λW is uniformly small as λ→0. The resulting continuous argument increases by 2π across a period, so it reaches the required argument without requiring monotonicity or an exact rotational symmetry of the background.

For L364, the template is chosen at λ=1/ω(H), gamma angle zero, before a visit is selected. Its support remains within N_R. The larger N_H tends to infinity and eventually contains this support. The discarded logarithmically weighted tails through order two are O_R((log H)^(-4π))=o_R(ω(H)^(-2)), uniformly in all phase assignments. This covers the full series, including primes between N_R and N_H assigned +1 in the template. No derivative of the H-dependent template is taken.

## Joint visit and same-frequency sign

Rechecked the finite cosine-power bump inherited from L336: translation changes coefficient phases but not their absolute sum one, constant coefficient b_H≥β_H, or support. Outside the open δ_H box it is at most β_H/4. There are finitely many harmonics even though their support grows with H.

For a harmonic -ν_k t+lφ(t), l=0 and k≠0 gives normalized integral at most 2/(HΔ_H). For l≠0, φ″=ω′ lies between 1/(8H) and 1/H eventually throughout [H,2H]. Thus its phase derivative is monotone, with second derivative magnitude at least η=|l|/(8H), even when ν_k causes a stationary point. The region |f′|≤sqrt(η) has length at most 2/sqrt(η); integration by parts over the at most two complementary intervals contributes at most 6/sqrt(η). Dividing by H yields at most 24/sqrt(H). The conditions HΔ_Hβ_H≥8 and sqrt(H)β_H≥96 consequently make the total discrepancy at most β_H/2. Its average then exceeds the outside-box bound, proving an actual visit. The changing target center requires no uniform center estimate beyond the coefficient absolute-sum bound already used.

At that same actual t, write w=ω(H) and W_a=iS_ε′(t). The head and tail estimates give |S_ε(t)-W/w|≤m_R/(64w) and |W_a-W|≤m_R/(64w), with m_R≤W≤M_1 real. Since ω(t)/w≤2 and ω(t)-w=O(1), they imply |S_ε′+iω(t)S_ε|≤m_R/8 eventually. The gamma window gives |Re(e^(iφ(t))W_a)|>15m_R/16. These are compatible conditions at one visit, not separate arithmetic and gamma recurrences.

Rechecked L359's exact projected identity: its negative term is -(Im(e^(iφ)S′))²; the completed positive square is |S′+iωS|². Thus those two terms contribute at most

\[
 ((1/8)^2-(15/16)^2)m_R^2=-221m_R^2/256.
\]

The remaining terms are |S||S″|≤O_R(1/w)M_2, γ|S|²=o_R(1), and the fully retained beta subtraction error O_R((1+ω²)β)=o_R(1). No second-derivative phase approximation is needed. Taking their sum at most 93m_R²/256 gives precisely the asserted upper bound -m_R²/2. The real projection, amplitude curvature and subtraction are retained; replacing this by a modulus-square spectrum would invalidate the calculation.

## Quantifiers, decision and limits of the audit

The checked chain has the order ∃ε_*>0, ∀ fixed ε∈(0,ε_*], ∃H_ε, ∀H≥H_ε, ∃t∈[H,2H] with the regulated first sign negative. This suffices to contradict any common global-first-sign threshold: choose one ε below both proposed thresholds and then a sufficiently large H. It does not require a bound on H_ε uniform in ε.

No defect was found in the local argument under the precisely cited standard arithmetic and gamma inputs. This audit does not reprove Matveev's theorem or certify the finite interval programs, neither of which is required to recheck the analytic conclusion. It does not establish an RH candidate. The actual negative margin is on the scale A(t)²m_R², while L357 supplies only an O(ε) absolute difference. No inequality comparing that difference to the margin, or controlling the escape of t as ε decreases, is in the proof. Passing these signs to F_0 remains unjustified.

Retain the existing stop result and park the common global-sign certificate. This repeated stop confirmation has STEP_OUTCOME STALLED: no mathematical repair, new bound or new counterexample was obtained. The audit reproduces the already screened supporting tools and checks their composition; no originality beyond the checked literature is claimed. Mathematical exploration usage remains zero after the preceding informative negative result.

A different unresolved gap is the *frequency-dependent approximation error* near ε=0, rather than positivity of every fixed-regulator spectrum at every frequency. A future target may test a regulator derivative expressed by shifted completed-zeta values and a two-frequency-derivative remainder in a coupled small-ε range. Its first test is a source comparison, not another phase-return calculation. A useful controlled response could quantify actual-theta arithmetic structure lost by the absolute envelope; any signing mechanism and the higher levels would still be missing. No such expansion or remainder is derived in this audit.

## Mathlib

Full fixed-regulator sign theorem and the audited parameter composition: **not checked**. Supporting gamma, logarithmic-form, contraction and finite Fourier library coverage: **not checked** in this step. Matveev, Corollary 2.3, [journal record](https://www.mathnet.ru/eng/im314), and Sha, [§2.4 (2.19)](https://arxiv.org/pdf/1505.07147v6), are supporting arithmetic citations, not full matches for the regulated sign statement. [DLMF 5.11](https://dlmf.nist.gov/5.11) and [5.15.8–9](https://dlmf.nist.gov/5.15#E8) support the gamma estimates. Preserve L357's previously recorded supporting Mathlib theorem names and direct links; they were not rechecked. No full matching library theorem or library absence is asserted.
