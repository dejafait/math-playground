STATUS: IN_PROGRESS

# Goal

Produce a complete, checkable informal proof of the Riemann hypothesis:

Every non-trivial zero of the Riemann zeta function ζ(s) has real part 1/2.

## Success criteria

STATUS in PROGRESS.md may become PROVED only if ALL of the following hold:

1. There is a single main argument in PROOF.md that starts from standard, named theorems (no original “well-known facts” that are actually RH-equivalent).
2. Every lemma is stated with hypotheses, conclusion, and a proof or a precise citation (book + theorem number, or a standard named theorem).
3. The argument does not assume the conclusion, does not hide an equivalent form of RH as a lemma, and does not rely on numerical evidence, “it is plausible”, or an unstated interchange of limits.
4. A dedicated section named “Known traps checked” lists the usual collapse points and explains why this write-up is not one of them.
5. A dedicated section named “What a Lean check would need” lists the exact statements to formalize later. Do not write Lean now.

If the argument only proves a weakening, STATUS stays IN_PROGRESS and the weakening is recorded under “Partial results”.

## Known traps (do not treat these as a proof of RH)

- Assuming the explicit formula plus “error too small” without a proved zero-free region stronger than what is already known.
- Weil / explicit-formula positivity arguments that smuggle RH-equivalent positivity.
- Interchanging sums, products, or contours without a dominated or compact estimate.
- “All computed zeros lie on the line, therefore all zeros do.”
- Claiming a proof of Li’s criterion, Robin’s inequality, Lagarias, or Nyman–Beurling without proving the criterion itself in full strength.
- Using the prime-number theorem with an error term that already encodes RH.
- A “new contour” that is the same as a standard contour plus an estimate equivalent to a zero-free strip.

## Working rules

- After every attempt, append a dated entry to PROGRESS.md and keep PROOF.md as the current best write-up.
- Prefer a lemma DAG: small claims, then a short assembly.
- If an attempt dies, write WHY IT FAILS in one paragraph. Do not delete failed attempts; move them to ATTEMPTS/.
- Do not claim PROVED to please the user. A wrong RH proof is worse than no proof.
- Do not use an API key. If rate-limited, stop cleanly.

## 2026-09-09 — Initial baseline and symmetry obstruction

- Initial state: PROGRESS.md duplicated GOAL.md; no “Next action” line existed, PROOF.md was absent, and ATTEMPTS contained only .gitkeep. Preserved the inherited text and started a baseline attempt.
- Tried: derive critical-line localization from the functional equation and complex conjugation. Proved the absolutely convergent Möbius reciprocal for Re(s)>1 and the zero-orbit/multiplicity lemmas in the open strip.
- Where it broke: set invariance does not imply pointwise fixedness. An exact degree-four polynomial has the same symmetries, positivity on the real axis and critical line, and four off-line roots.
- Archive: ATTEMPTS/2026-09-09-symmetry-only.md includes the failed inference and WHY IT FAILS. PROOF.md is the single current write-up of the surviving lemmas and obstruction.
- Validation: checked the series rearrangement by absolute double summability and the counterexample by explicit factorization and sum-of-squares identities. Verified the functional-equation reference against NIST DLMF 25.4.2. No Lean, API key, or numerical zero evidence used.
- Partial results: elementary nonvanishing for Re(s)>1 and zero symmetries; no RH proof and no claimed new zero-free region. STATUS remains IN_PROGRESS.
- Next lemma: the classical zero-free boundary Re(s)=1 away from its pole, with all convergence and local-order estimates supplied.

## 2026-09-09 — Lemma 5: Euler-product logarithm

- Tried and proved: absolute and locally uniform convergence of L(s)=Σ_pΣ_{k≥1}p^{-ks}/k on Re(s)>1, and exp L(s)=ζ(s).
- Validation: the uniform majorant is (1-2^{-(1+δ)})^{-1}Σ_{n≥2}n^{-(1+δ)} on Re(s)≥1+δ. The finite-product error is bounded by Σ_{n>X}n^{-(1+δ)}. Taking a real logarithm of the modulus introduces no branch assumption.
- Where it broke: no failure within the stated domain; no convergence on or left of Re(s)=1 was claimed.
- Next lemma: use 3+4cos θ+cos 2θ≥0 in this absolutely convergent prime sum.

## 2026-09-09 — Lemma 6: product inequality

- Tried and proved: ζ(σ)³|ζ(σ+it)|⁴|ζ(σ+2it)|≥1 for every σ>1 and real t.
- Validation: the logarithm of the left side is an absolutely convergent sum of p^{-kσ}·2(1+cos(kt log p))²/k, so every summand is nonnegative.
- Where it broke: no failure; the inequality has not been extended to σ<1.
- Next lemma: compare this lower bound with the local pole and hypothetical zero orders as σ decreases to 1.

## 2026-09-09 — Lemma 7: boundary nonvanishing completed

- Tried and proved: ζ(1+it)≠0 for all real t≠0. A hypothetical order-m zero gives 1≤C h^{4m-3}, impossible as h decreases to zero.
- Validation: the factor at 1 has a simple pole; the factor at 1+it has the hypothesized zero; the factor at 1+2it is bounded since t≠0. Constants may depend on fixed t, which is sufficient. No prime-sum limit on the boundary is required.
- Where it broke: no failure. This fully executes the original next action but proves only a classical boundary result, not RH. STATUS remains IN_PROGRESS.
- Next lemma: classify zeros in Re(s)≤0 using reflection, including the removable cancellation at s=0.

## 2026-09-09 — Lemma 8: residue and the origin

- Tried and proved: Res_{s=1}ζ=1 by integral comparison of the real Dirichlet series; ζ(0)=-1/2 by the functional equation and explicit cancellation.
- Validation: 1≤hζ(1+h)≤1+h identifies the assumed simple-pole residue. The sine zero cancels the pole of ζ(1-s) with sign -1/2.
- Where it broke: no failure; the separate check at s=0 prevents misclassifying it as a trivial zero.
- Next lemma: combine this value, Lemma 7, and the nonzero reflection prefactor to classify Re(s)≤0.

## 2026-09-09 — Lemma 9: all nontrivial zeros are in the open strip

- Tried and proved: outside 0<Re(s)<1, the only zeros are the simple negative-even-integer zeros.
- Validation: handled Re(s)>1, Re(s)=1, Re(s)<0, Re(s)=0 away from 0, and s=0 separately. In Re(s)<0 only the sine factor vanishes, with nonzero derivative.
- Where it broke: no failure; this is the classical strip localization, not critical-line localization.
- Next lemma: establish the genuine convergence obstruction to transporting the prime positivity proof left of 1.

## 2026-09-09 — Lemma 10: convergence barrier for prime positivity

- Tried and proved: Σ_p1/p diverges; the nonnegative prime-logarithm sum diverges for 0<σ≤1; absolute convergence fails throughout that portion of the strip.
- Validation: bounded reciprocal-prime sum would bound every finite Euler product, while each dominates the harmonic sum through X. The k=1 terms suffice for the remaining assertions.
- Where it broke: this exposes a failure of the proposed positivity extension, not a failure of the divergence lemma. Analytic continuation of ζ does not provide this divergent positive representation.
- Next lemma: check whether the inequality itself, even stripped of its divergent derivation, is false inside the strip.

## 2026-09-09 — Lemma 11 and failed continuation attempt

- Tried and proved: the proposed continuation of the product inequality is false, even after replacing the first factor by its modulus and restricting to t≠0.
- Validation: the repaired product is continuous at (0,0) with exact value 1/256, so it is <1 in an open neighborhood containing interior-strip points. ζ(σ)<0 near 0 also defeats the original signed form.
- Where it broke: inequalities and divergent positive representations do not analytically continue. Archived the route in ATTEMPTS/2026-09-09-continued-prime-positivity.md with WHY IT FAILS.
- Next lemma: the alternating Dirichlet series gives an actually convergent representation on Re(s)>0; prove its uniform tail bound before using it.

## 2026-09-09 — Lemma 12: alternating representation with compact estimates

- Tried and proved: η is holomorphic on Re(s)>0 and equals (1-2^{1-s})ζ(s), with the value log 2 at s=1.
- Validation: the finite tail is bounded by (1+R/δ)N^{-δ} on Re(s)≥δ>0, |s|≤R. The continuation uses equality of holomorphic functions after explicitly removing the pole at 1.
- Where it broke: no failure; no division at the zeros of 1-2^{1-s} is asserted.
- Next lemma: for real 0<σ<1, pair the alternating terms to obtain strict positivity of η and hence negativity of ζ.

## 2026-09-09 — Lemma 13: real-axis nonvanishing in the strip

- Tried and proved: η(σ)≥1-2^{-σ}>0 and ζ(σ)<0 for 0<σ<1, so all nontrivial zeros are nonreal.
- Validation: positivity is taken along the convergent subsequence of even partial sums. The factor 1-2^{1-σ} is strictly negative on the stated real interval.
- Where it broke: no failure for real σ; the positive summands become complex at nonreal s and cannot be ordered.
- Next lemma: write η(s)/s as an integral against a nonnegative bounded kernel, with absolute convergence, to isolate the exact positivity claim available.

## 2026-09-09 — Lemma 14: bounded nonnegative Laplace kernel

- Tried and proved: η(s)/s is the Laplace transform of the nonnegative bounded kernel w(e^u) on Re(s)>0.
- Validation: finite paired sums integrate exactly; the omitted x-integral is at most (2N+1)^{-σ}/σ. Compact convergence uses σ≥δ>0.
- Where it broke: no failure in the representation. Nonnegativity of the kernel does not yet control cancellation of e^{-itu}.
- Next lemma: test a compactly supported indicator kernel to determine whether nonnegativity alone can exclude complex zeros.

## 2026-09-09 — Lemma 15 and failed positive-kernel inference

- Tried and proved: the Laplace transform of 1_[0,1]∪[2,4] has a nonreal zero with 0<Re(s)<(log 2)/2<1 despite positivity on the whole real axis.
- Validation: exact integration factors the transform; derivative signs count the cubic's real roots, and Vieta gives the nonreal root modulus. No numerical roots were used.
- Where it broke: nonnegative kernels do not prevent complex phase cancellation. Archived ATTEMPTS/2026-09-09-positive-laplace-kernel.md with WHY IT FAILS.
- Next lemma: investigate the stronger reflection-symmetric completion using theta and Poisson summation; all representations must have compact convergence bounds.

## 2026-09-09 — Lemma 16: theta transformation

- Tried and proved: θ(x)=x^{-1/2}θ(1/x) by Poisson summation of a Gaussian; all fixed derivative orders of ψ have O(e^{-πx}) tails on x≥1.
- Validation: the Fourier convention and Gaussian transform are explicit, both lattice sums converge absolutely, and C_j=Σ(πn²)^j e^{-π(n²-1)} is a finite uniform derivative majorant.
- Where it broke: no failure. Poisson summation and the Gaussian integral are named standard inputs, not positivity or zero-location assumptions.
- Next lemma: split the Mellin integral at 1 using the transformation and prove the remaining integral is entire.

## 2026-09-09 — Lemma 17: entire Mellin remainder

- Tried and proved: the split Mellin identity π^{-s/2}Γ(s/2)ζ(s)=1/(s-1)-1/s+I(s) for Re(s)>1, with I entire and I(s)=I(1-s).
- Validation: Fubini is bounded by π^{-σ/2}Γ(σ/2)ζ(σ); after splitting, all compact s-sets and fixed derivatives are dominated by e^{-πx} times a fixed power of x and log x.
- Where it broke: no failure. The elementary pole terms were integrated only in their convergence domain before constructing the entire remainder.
- Next lemma: cancel the poles explicitly to form ξ, then identify its zero set and symmetries without asserting real-zero localization.

## 2026-09-09 — Lemma 18: entire completion and zero correspondence

- Tried and proved: entire ξ with reflection and conjugation symmetry, ξ(0)=ξ(1)=1/2, and exact nontrivial-zero correspondence; Ξ(z)=ξ(1/2+iz) is even and real on R.
- Validation: the product expression is continued only on Re(s)>0, where Γ(s/2) has no poles; s=1 is removed explicitly. Reflection handles Re(s)≤0. The linear variable change preserves zero orders.
- Where it broke: no failure. The statement “all Ξ zeros are real” is identified as equivalent to RH and is explicitly unproved, not inserted as a lemma.
- Next lemma: a controlled integration by parts of the theta integral yields the positive Fourier kernel; investigate the actual strength of its positivity.

## 2026-09-09 — Lemma 19: positive theta kernel and boundary derivative

- Tried and proved: A'(0)=-1/4 and K=2A''-A/2 is strictly positive on u≥0, with an explicit termwise formula.
- Validation: differentiated theta reflection gives the boundary derivative. Every K summand is 4v(2v-3)e^{u/2}e^{-v}>0 since v≥π. Lemma 16 bounds A and the needed derivatives by C e^{9u/2}e^{-πe^{2u}}.
- Where it broke: no failure. Positivity has been proved for the kernel, not for complex values of its transform or for zero locations.
- Next lemma: integrate twice by parts, retain the nonzero boundary term, and justify the resulting entire cosine transform.

## 2026-09-09 — Lemma 20: exact cosine representation

- Tried and proved: Ξ(z)=∫_0^∞K(u)cos(zu)du for every complex z, with every fixed derivative locally uniformly convergent.
- Validation: I(1/2+iz)=4J(z); two integrations by parts yield -A'(0)-z²J(z). The boundary value -2A'(0)=1/2 exactly supplies the constant term. Compact bounds use e^{R u} times the superexponential tail.
- Where it broke: no failure. No real-zero conclusion follows just from this representation.
- Next lemma: derive the valid imaginary-axis positivity and moment signs, then test whether they imply real zeros.

## 2026-09-09 — Lemma 21: positive moments and imaginary-axis nonvanishing

- Tried and proved: Ξ has alternating even Taylor coefficients from strictly positive moments, Ξ(iy)>0 for all real y, and the moments satisfy Cauchy–Schwarz log-convexity.
- Validation: the complete absolute cosine series is bounded by e^{R u} on |z|≤R, integrable against K; no unstated series/integral exchange occurs.
- Where it broke: no failure for these consequences. Positive moments and their log-convexity have not been shown to imply real zeros.
- Next lemma: construct a positive even superexponentially decaying kernel whose transform has an explicit off-real zero, to test these sufficient-condition guesses sharply.

## 2026-09-09 — Lemma 22 and failed positive Fourier-kernel inference

- Tried and proved: a smooth strictly positive even kernel with the same superexponential decay scale can have an entire transform with an off-real zero inside |Im(z)|<1/2.
- Validation: real shifts give the exact factor 2+cos(4z); z=(π+i log(2+√3))/4 is an exact zero. All complex transforms have compact majorants. The positive-moment and imaginary-axis properties survive.
- Where it broke: kernel positivity and decay do not imply real zeros. Archived ATTEMPTS/2026-09-09-positive-theta-kernel-inference.md with WHY IT FAILS and the limitation that global strip confinement was not proved for the counterexample.
- Next lemma: establish the actual Ξ growth bound and then its unconditional paired Hadamard product; do not assume any zero is real.

## 2026-09-09 — Lemma 23: order at most one

- Tried and proved: an explicit O(R log R) bound for log max_{|z|≤R}|Ξ(z)|, hence entire order at most 1.
- Validation: the kernel majorant becomes an incomplete gamma integral after x=e^{2u}; an integer factorial bound m!≤m^m supplies the growth estimate without any asymptotic zero formula.
- Where it broke: no failure. No real-zero property enters the growth estimate.
- Next lemma: invoke the named Hadamard factorization theorem in its finite-order form, then justify pairing zeros and removing the odd exponential factor.

## 2026-09-09 — Lemma 24: paired product without RH

- Tried and proved: Ξ(z)=M_0Π_j(1-z²/α_j²), with Σ|α_j|^{-2}<∞, selecting one representative per ± pair with multiplicity.
- Validation: applied the named Hadamard factorization theorem only after Lemma 23 and M_0>0; checked its order-at-most-one form against UCL notes, Theorem 7.7. Evenness sets the linear exponential factor to zero. Absolute convergence of the genus-one logarithmic tails justifies grouping.
- Where it broke: no failure; α_j are still allowed to be complex. Treating their even reciprocal powers as positive would assume missing zero information.
- Next lemma: compare the first two product coefficients with the moment expansion and isolate the unproved sign required by real zeros.

## 2026-09-09 — Lemma 25: exact reciprocal-zero/moment identities

- Tried and proved: absolute convergence and reality of all S_k=Σα_j^{-2k}, together with S_1=M_2/(2M_0) and S_2=(3M_2²-M_0M_4)/(12M_0²).
- Validation: a zero-free disk at 0 and Σ|α_j|^{-2}<∞ give an absolute double-series bound for the local logarithm. Coefficient comparison is local and justified.
- Where it broke: positive-kernel Cauchy–Schwarz supplies the opposite-direction bound M_0M_4≥M_2²; it does not establish the needed upper bound by itself. This is an identified insufficiency, not a claim that the upper bound is false for Ξ.
- Next lemma: use the much stronger theta tail and known horizontal strip for Ξ zeros to prove a concrete small-height zero-free rectangle, then see whether it certifies the first few S_k signs.

## 2026-09-09 — Lemma 26: a small-height zero-free rectangle

- Tried and proved: |J(z)|<1/72 for |Im(z)|≤1/2, hence Ξ(z)≠0 when additionally |Re(z)|≤4.
- Validation: ψ(X)≤e^{-πX}/(1-e^{-π}); the integral bound is 1/[2π(e^π-1)]<1/72 using only π>3 and e³>13. The resulting distance to 1/2 is <11/24.
- Where it broke: no failure. This is a coarse analytic low-height exclusion, not numerical evidence or an asymptotic zero-free strip.
- Next lemma: choose each ± representative with positive real part and use |arg α|<1/8 to prove finitely many reciprocal-power signs.

## 2026-09-09 — Lemma 27: finite sign certificate and infinitely many zeros

- Tried and proved: Ξ has infinitely many zeros; S_k>0 for 1≤k≤6; M_2²<M_0M_4<3M_2².
- Validation: finitely many zeros would make the paired Hadamard product a polynomial, contradicting all positive moments. Representatives in the right half-plane satisfy |arg α|<1/8, so their reciprocal powers have positive real parts for the six stated k. Absolute convergence makes the summation valid.
- Where it broke: the argument bound supplies only finitely many signs; for increasing k the angles 2k arg α need not stay below π/2. No all-k or real-zero assertion is inferred.
- Next lemma: turn the certified moment inequality into an explicit degree-two polynomial test, then test the stronger conjecture that all reciprocal-power sums being positive would suffice.

## 2026-09-09 — Lemma 28: degree-two Jensen test

- Tried and proved: J_2(X)=M_0+M_2X+(M_4/12)X² has two distinct negative real roots.
- Validation: its discriminant M_2²-M_0M_4/3 is positive by the independently proved Lemma 27; its root sum is negative and product positive.
- Where it broke: no failure for this polynomial. Higher degrees and shifted polynomials are untreated; this finite test is not a proof of a real-zero criterion or RH.
- Next lemma: test the sufficiency of all positive reciprocal-power sums by constructing an explicit off-real polynomial factor whose real zero contribution dominates every S_k.

## 2026-09-09 — Lemma 29 and failed scalar-power-sum criterion

- Tried and proved: an explicit even polynomial has nonreal zeros but all paired reciprocal-power sums positive; multiplying by cos(z/100) also supplies infinitely many zeros, order at most 1, alternating nonzero coefficients, and the same strip/rectangle zero confinement.
- Validation: |(10+i/4)^{-2}|<(1/25)/4 makes the real node dominate every power. The cosine adds only convergent positive real-zero contributions.
- Where it broke: all scalar signs still do not force real zeros. Archived ATTEMPTS/2026-09-09-positive-power-sums.md with WHY IT FAILS; the example is not claimed to have a positive Fourier kernel.
- Next lemma: mixed polynomial quadratic forms can cancel a dominant real node and detect a complex pair; derive them before considering any positivity claim for Ξ.

## 2026-09-09 — Lemma 30: mixed Hankel quadratic forms

- Tried and proved: Q(q)=Σβ_j²q(β_j)² converges absolutely, is real, and equals the finite Hankel form Σc_mc_nS_{m+n+2}. RH implies Q(q)≥0.
- Validation: Σ|β_j|<∞ gives bounded nodes and square-summable weights; fixed polynomials are bounded on their disk. The square is explicitly algebraic, not a modulus.
- Where it broke: unconditional positivity is not proved. Making each summand a modulus square would silently change the quantity.
- Next lemma: produce an explicit real polynomial q for which the finite counterexample has Q(q)<0, then extend the detection argument to a summable discrete zero set.

## 2026-09-09 — Lemma 31: explicit negative mixed test

- Tried and proved: a real degree-at-most-two interpolation polynomial makes the finite counterexample's Q equal exactly -2, despite every scalar T_k being positive.
- Validation: Lagrange basis polynomials at b,c,conj(c) have the stated values and conjugate coefficients. Each complex node contributes -1 and the real node contributes 0.
- Where it broke: no failure. This detects the artificial polynomial's nonreal zeros, not any zero of Ξ.
- Next lemma: suppress the tail of an infinite discrete node set with a high power, while preserving the same negative values at one conjugate pair.

## 2026-09-09 — Lemma 32: infinite-node detection with a controlled tail

- Tried and proved: any nonreal node in a conjugation-invariant absolutely summable node sequence is detected by a negative real-polynomial quadratic form.
- Validation: interpolate on the finite nodes |β|≥|w|/2; multiplying the target terms by (X/w)^N and its conjugate preserves the target values and bounds the tail by C²4^{-N}Σ|β|². The finite contribution is exactly -2μ.
- Where it broke: no failure in the detection lemma. It does not prove positivity of the actual Ξ forms.
- Next lemma: apply this equivalence to Ξ, then isolate the first genuinely mixed finite test for explicit analysis.

## 2026-09-09 — Corollary 32a: criterion identified, not established

- Tried and proved: RH is equivalent to positive semidefiniteness of every H_d=(S_{m+n+2}) for the actual Ξ nodes.
- Validation: negative real β would require a purely imaginary Ξ zero, already excluded; all other hypotheses are from the unconditional product and conjugation symmetry.
- Where it broke: the all-d positivity is precisely unproved and RH-equivalent. It is labeled openly as an unresolved condition, never used as an unconditional lemma.
- Next lemma: compute the smallest mixed determinant S_2S_4-S_3² in terms of moments, distinguishing positive moments from the needed mixed sign.

## 2026-09-09 — Lemma 33: first mixed determinant reduced to moments

- Tried and proved: explicit S_3 and S_4 formulas and D=S_2S_4-S_3²=a²b²-4b³-2a³c+10abc-9c²-4a²d+8bd in normalized moments through M_8.
- Validation: coefficient comparison uses the already justified local logarithm; completing the square shows H_1 is positive semidefinite exactly when D≥0 because S_2>0.
- Where it broke: the formula contains mixed positive and negative terms; positivity of individual moments and S_2,S_3,S_4 does not establish D≥0. No sign is claimed yet for the actual Ξ determinant.
- Next lemma: test the strength of the current zero-argument estimate on a conjugate pair, then seek an actual-theta-specific determinant bound if that generic estimate fails.

## 2026-09-09 — Lemma 34 and failed strip-to-mixed-positivity inference

- Tried and proved: the conjugate-node example has T_k>0 for k=1,…,6 but T_2T_4-T_3²=-4|c|⁴(Im c)²<0, while its zero pairs obey the same coarse strip/rectangle restriction.
- Validation: the determinant factors exactly; c is nonreal. No numerical approximation or inferred location is used.
- Where it broke: small arguments and individual positive sums do not imply mixed Hankel positivity. Archived ATTEMPTS/2026-09-09-strip-to-hankel-positivity.md with WHY IT FAILS.
- Next lemma: a genuine actual-theta estimate is needed for the finite determinant; the all-degree positivity remains openly RH-equivalent and unproved.

## 2026-09-09 — Lemma 35: certified moment truncation tails

- Tried and proved: a common explicit error E bounds M_k minus the n≤4, 0≤u≤2 truncated integral for k=0,2,4,6,8.
- Validation: positive K_n allow dropping omitted regions; n⁴ and n² comparisons sum the prime-free Gaussian tails geometrically. Repeated integration by parts gives the finite tail expression, and all constants use only 3<π<4 and elementary exponential-series lower bounds.
- Where it broke: no failure. The finite integrals still need validated quadrature; no floating-point sign has been accepted.
- Next lemma: derive a midpoint Taylor integration enclosure with an explicit eighth-derivative remainder and implement outward-rounded interval arithmetic for this finite certificate.

## 2026-09-09 — Lemma 36: validated Taylor quadrature

- Tried and proved: each symmetric panel has an explicit eighth-derivative error bound 2Bh⁹/9 after integrating the Taylor polynomial through degree seven.
- Validation: Taylor's remainder integrates absolutely; product and exponential normalized-derivative recurrences permit interval evaluation of the required coefficient and uniform remainder bounds.
- Where it broke: no failure. The planned code must still implement outward rounding and enclose π and exponentials; ordinary floating-point evaluations are insufficient.
- Next lemma: validate the arithmetic inputs, implement the finite certificate with standard-library Decimal and rational π bounds, then execute and inspect whether D is separated from zero.

## 2026-09-09 — Lemma 37: interval arithmetic inputs

- Tried and proved: enclosure propagation for the finite certificate under explicit directed-rounding and correctly-rounded-exp contracts, including exact rational Machin bounds for π.
- Validation: inspected endpoint signs, four-product multiplication, reciprocal division, exp neighbor widening, and normalized derivative recurrences. Standard-library Decimal contracts were checked against official Python documentation. The script rejects binary floats and exceptional exponent-range conditions.
- Where it broke: no failure. The certificate trusts the documented arithmetic implementation; it is not a formal verification of that library.
- Next lemma: record the executed finite determinant enclosure and its narrow conclusion; do not extrapolate to larger Hankel matrices.

## 2026-09-09 — Lemma 38: first mixed determinant certified positive

- Tried and proved with a computer-assisted interval certificate: 3.38·10^{-15}<D=S_2S_4-S_3²<4.34·10^{-15}; hence H_1 is positive definite.
- Validation: ran `python3 scripts/hankel/certify_hankel.py --panels 32 > scripts/hankel/hankel-certificate.json` under Python 3.14.7. Outward arithmetic, exact rational π bounds, every panel remainder, and both infinite-tail bounds are included. Exact rational self-checks pass. An alternative expanded expression encloses the result more loosely and is not used for the sign.
- Where it broke: no failure for H_1. This says nothing by itself about all H_d and does not satisfy the RH goal. STATUS remains IN_PROGRESS.
- Next lemma: extend the truncation bound to moments through M_12, derive a recurrence for S_k through S_6, and attempt a certified H_2 test.

## 2026-09-09 — Lemma 39: higher fixed moment tails

- Tried and proved: the common moment-tail formula extends to every fixed degree 2m with p=m+2. For M_12, p=8 and the second tail term is 3,225,600,000e^{-74}.
- Validation: replacing u^k≤e^{8u} by u^k≤e^{2mu} changes the post-substitution power to m+5/4, bounded by p=m+2; the same geometric n-tail proof applies.
- Where it broke: no failure. This family of estimates can become inefficient at high degree, so no uniform claim is inferred.
- Next lemma: derive Newton's recurrence from the local logarithm and use it to compute finite Hankel matrices from the certified moments.

## 2026-09-09 — Lemma 40: Newton recurrence and H_2 minors

- Tried and proved: a finite Newton recurrence computes each S_k from the normalized moments, and the explicit determinant formula D_2 tests H_2 together with its two previous leading minors.
- Validation: the recurrence comes from the convergent local identity F'=-FΣS_kt^{k-1}; the determinant expansion and positive Gaussian-elimination pivots give the matrix conclusion.
- Where it broke: no failure. Values and signs for the new determinant still require the interval execution.
- Next lemma: execute the generalized certificate through M_12 and S_6, increasing panel count only if its certified interval is inconclusive.

## 2026-09-09 — Lemma 41: H_2 certified positive definite

- Tried and proved with an interval certificate: the three leading principal minors of H_2 are positive and 3.10·10^{-31}<det H_2<3.14·10^{-31}.
- Validation: ran `python3 -B scripts/hankel/certify_hankel_next.py --panels 128 > scripts/hankel/hankel-h2-128.json`. The code retains every moment enclosure, quadrature remainder, higher tail, Newton sum, and principal-minor interval. The H_1 script/output were preserved. The 128-panel enclosure succeeded without refinement.
- Where it broke: no failure for H_2. Checking this matrix does not establish the infinite family in Corollary 32a; STATUS stays IN_PROGRESS.
- Next lemma: expose the structure of arbitrary finite determinants using a rigorously convergent Cauchy–Binet expansion, then use that structure to assess whether further finite tests can be connected analytically.

## 2026-09-09 — Lemma 42: convergent determinant expansion

- Tried and proved: the Cauchy–Binet/Vandermonde expansion for every fixed det H_d, with an absolute majorant (2R)^{d(d+1)}(Σ|β|²)^{d+1}/(d+1)!.
- Validation: finite truncations converge entrywise; determinant continuity and absolute convergence justify the limit. Indices preserve multiplicities, and repeated-node factors vanish correctly.
- Where it broke: the matrix is VVᵀ, not VV*, so the squares are algebraic and may be negative. Archived ATTEMPTS/2026-09-09-vandermonde-square-sign.md with WHY IT FAILS. No actual-theta identity supplying the missing sign has been found.
- Next lemma: positive K gives ordinary moment Hankel positivity; distinguish this from the nonlinear reciprocal-zero Hankel positivity and test the proposed transfer.

## 2026-09-09 — Lemma 43: ordinary moment positivity

- Tried and proved: every ordinary moment matrix G_d=(M_{2m+2n}) is strictly positive definite through the integral ∫K(u)q(u²)²du.
- Validation: fixed moment convergence permits the finite expansion, and a nonzero polynomial cannot vanish on an interval where K>0.
- Where it broke: G_d is not H_d; the latter uses coefficients of a logarithm and needs a separate positivity argument.
- Next lemma: build a positive smooth even superexponential kernel whose logarithmic fourth-order coefficient gives a negative reciprocal-power-type scalar, explicitly refuting automatic positivity transfer.

## 2026-09-09 — Lemma 44 and failed Gram-to-logarithm transfer

- Tried and proved: a positive smooth even superexponential kernel has all ordinary Gram matrices positive but a negative logarithmic T_2. The fourth cumulant is >27997/100 by an explicit Gaussian comparison and shifted-moment identities.
- Validation: moment shifts are integrated absolutely; ν_2<3/2 follows from elementary numerator/denominator bounds; the local logarithm gives T_2=(3μ_2²-μ_4)/12. No unverified decimal estimate is used.
- Where it broke: nonlinear logarithmic coefficients do not inherit ordinary moment positivity. Archived ATTEMPTS/2026-09-09-gram-logarithm-transfer.md with WHY IT FAILS.
- Next lemma: examine a stronger actual-kernel property, while first checking whether the proposed property would avoid the same generic counterexamples.

## 2026-09-09 — Lemma 45: individual theta summands are log-concave

- Tried and proved: exact logarithmic derivative formulas give (log K_n)''=-4v_n-24v_n/(2v_n-3)²<0 for u≥0.
- Validation: K_n=4v_n(2v_n-3)e^{u/2}e^{-v_n}, v_n'=2v_n, and v_n≥π>3 keep all factors and denominators positive.
- Where it broke: no failure for individual terms. A sum of log-concave functions need not remain log-concave; that transfer is not assumed.
- Next lemma: derive the weighted-curvature-plus-variance identity for log K and test the generic sum inference before bounding its variance for this specific theta series.

## 2026-09-09 — Lemma 46 and failed termwise-log-concavity inference

- Tried and proved: the exact weighted curvature plus variance identity, with compact summability checks for the theta summands.
- Validation: direct differentiation yields the identity; the explicit two-Gaussian sum has log curvature 14 at zero despite individual curvature -2.
- Where it broke: summing log-concave terms does not preserve log-concavity automatically. Archived ATTEMPTS/2026-09-09-termwise-log-concavity.md with WHY IT FAILS.
- Next lemma: the specific theta weights may make the variance small enough; estimate it rather than discard it.

## 2026-09-09 — Lemma 47: full theta kernel is strictly log-concave

- Tried and proved: (log K)''<-(68/125)πe^{2u}<0 on u≥0 for the actual theta kernel.
- Validation: bounded the variance by 9216v²e^{-3v}, while the mean curvature is <-4v. Exact geometric estimates and e³>20 give 2304v e^{-3v}<108/125, closing the strict inequality.
- Where it broke: no failure; this is an actual-kernel property beyond positivity, but no real-zero theorem has been deduced from it.
- Next lemma: verify the smooth even extension and boundary slope, then test whether strict log-concavity itself is sufficient for real transform zeros.

## 2026-09-09 — Lemma 48: even extension and monotone theta kernel

- Tried and proved: K extends smoothly and evenly to R, has K'(0)=0, is strictly decreasing on u>0, and is strictly log-concave globally with the quantitative curvature bound.
- Validation: A(-u)=A(u)+sinh(u/2) follows directly from theta reflection; the operator 2D²-1/2 annihilates the extra term. Compact theta estimates justify derivatives on the full real axis.
- Where it broke: no failure. These kernel properties are proved independently of any claim about transform zeros.
- Next lemma: test strict log-concavity as a proposed sufficient condition with a small-shift Gaussian mixture, preserving smoothness, positivity, and evenness.

## 2026-09-09 — Lemma 49 and failed log-concavity-alone inference

- Tried and proved: a smooth positive even kernel with (log h)''≤-1 has an explicit nonreal Fourier zero and logarithmic T_2=-7/19200.
- Validation: a three-slope variance bounds the log curvature; Gaussian shifts give the exact Fourier factor; the cumulant calculation is rational.
- Where it broke: strict log-concavity alone does not imply real zeros. Archived ATTEMPTS/2026-09-09-log-concavity-alone.md with WHY IT FAILS. Its Gaussian decay/order two are explicitly distinguished from the theta-scale properties.
- Next lemma: test log-concavity together with superexponential decay/order at most one using a controlled small-shift superexponential mixture.

## 2026-09-09 — Lemma 50: global log-concavity survives a small superexponential shift

- Tried and proved: for the explicit shift a=1/100, the positive superexponential mixture satisfies (log h_a)''<-cosh(2u)/4 on the entire real axis, yet has an explicit nonreal Fourier zero.
- Validation: a central range-variance bound handles cosh(2u)≤128; a pairwise likelihood-ratio bound handles the full tail. Both use exact constants and overlap, with no unproved uniform-in-u shift argument.
- Where it broke: log-concavity plus superexponential decay still does not force real zeros. Archived ATTEMPTS/2026-09-09-log-concavity-and-superexponential-decay.md with WHY IT FAILS; horizontal zero confinement remains an additional distinction.
- Next lemma: verify order at most one for this transform, then adjust the weights to bring the introduced zero into the actual strip without losing the curvature estimate.

## 2026-09-09 — Lemma 51: order bound for the comparison kernels

- Tried and proved: every Fourier transform of a kernel bounded by C exp(-c e^{2|u|}) has entire order at most 1, including the small-shift counterexample.
- Validation: dominated derivatives prove entirety; a gamma-integral/factorial estimate gives the explicit O(R log R) upper bound. Fixed shifts only change constants.
- Where it broke: no failure. The combined log-concavity/superexponential example now also meets the order bound; its zero confinement still needs separate analysis.
- Next lemma: tune the weight ratio to move the introduced nonreal zeros into the actual horizontal strip, and keep base-transform zeros explicitly unresolved until proved.

## 2026-09-09 — Lemma 52: introduced zeros satisfy the actual strip bounds

- Tried and proved: tuning the central ratio to cosh(1/1000) preserves the global log-concavity proof and places every introduced zero at (2k+1)100π±i/10.
- Validation: all weight ratios are <4, so the previous ratio-18 proof remains valid. Solving the exponential quadratic gives every prefactor zero exactly.
- Where it broke: no failure. All base-transform zeros must still be located before asserting that the full comparison function satisfies global confinement.
- Next lemma: derive a half-line differential equation for the base transform, with explicit decay and nontriviality, to locate those zeros through an energy identity.

## 2026-09-09 — Lemma 53: comparison transform differential equation

- Tried and proved: Y_z(0)=G(z), the half-line equation -Y_z''+e^{2x}Y_z=(z²/4)Y_z, superexponential decay, and a nonzero normalized limit at infinity.
- Validation: differentiated the explicit integral with compact domination; two integrations by parts have zero endpoint terms. A rescaled Gaussian majorant proves sqrt(r)e^rY_z→sqrt(π/2), ensuring nontriviality even for complex z.
- Where it broke: no failure. No spectral theorem or real-zero statement was assumed in deriving the equation.
- Next lemma: use the Dirichlet value at zero and the proved decay to derive the energy identity, then sharpen it enough to exclude |z|≤4.

## 2026-09-09 — Lemma 54: all comparison-base zeros are real and large enough

- Tried and proved: every G zero is real and has |z|>2sqrt(7)>4.
- Validation: the energy identity uses the proved decay and nonzero solution; completing the square with 1/x-2x gives the half-line oscillator bound. Y=O(x) explicitly removes the singular endpoint. The potential inequality is an elementary exponential-series estimate.
- Where it broke: no failure. This real-zero theorem is proved for the comparison base G, not for Ξ.
- Next lemma: assemble the tuned mixture to test the entire package of generic properties, now that its base zeros are also located.

## 2026-09-09 — Lemma 55: counterexample to the combined generic conditions

- Tried and proved: a family F_a simultaneously satisfies all listed generic kernel, order, coefficient, imaginary-axis, and full zero-geometry properties, but has nonreal zeros (2k+1)π/a±i/10.
- Validation: the curvature bound is uniform for 0<a≤1/100; the prefactor zeros are exact; the energy theorem locates every remaining G zero. No unlocated extra zeros remain in this comparison.
- Where it broke: the whole tested package still does not force real zeros. Archived ATTEMPTS/2026-09-09-combined-kernel-and-zero-geometry.md with WHY IT FAILS and the explicit distinction from arithmetic theta coefficients.
- Next lemma: prove every finite reciprocal-zero Hankel matrix of the base G is strictly positive, then use finite-dimensional continuity to test persistence under small shifts.

## 2026-09-09 — Lemma 56: all finite base Hankel tests are strictly positive

- Tried and proved: G has infinitely many distinct real zeros, a justified even Hadamard product with summable positive reciprocal nodes, and H_d(G)>0 for every fixed d.
- Validation: all even Taylor coefficients are nonzero by positive moments, ruling out the finite polynomial product. A nonzero polynomial cannot vanish at all the infinitely many distinct positive nodes, so every nonzero quadratic form is strictly positive.
- Where it broke: no failure. This all-degree result is for G, whose differential equation proved real zeros; it is not transferred to Ξ.
- Next lemma: preserve finitely many of these strict matrix inequalities under the small-shift family, while its introduced zeros remain nonreal.

## 2026-09-09 — Lemma 57 and failed finite-Hankel extrapolation

- Tried and proved: for every fixed N, a comparison function with nonreal zeros satisfies all H_d>0 for d≤N and every generic structural property in Lemma 55.
- Validation: normalized finite moment coefficients vary continuously with the shift; Newton recurrence gives continuity of each determinant; finitely many strict inequalities persist. The nonreal zeros retain imaginary parts ±1/10 and escape to large real parts.
- Where it broke: finite certificates cannot imply the infinite family. Archived ATTEMPTS/2026-09-09-finite-hankel-extrapolation.md with WHY IT FAILS and the explicit for-each-N/depends-on-N quantifier distinction.
- Next lemma: investigate the exact theta arithmetic structure through a deformation identity, rather than adding more finite checks as if they constituted an induction.

Next action: Define the heat-deformed transform Ξ_λ(z)=∫_0^∞e^{λu²}K(u)cos(zu)du for real λ. Prove entire z-dependence, smooth/analytic λ-dependence on compact parameter sets, and ∂_λΞ_λ=-∂_z²Ξ_λ with explicit domination. Then derive the local motion law for a simple real zero under λ variation and determine exactly what it can and cannot say about λ=0 without assuming a global real-zero theorem.
