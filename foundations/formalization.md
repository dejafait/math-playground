# What a Lean check would need

This is a future statement inventory only; no Lean is used or written.

1. The defining Dirichlet series, meromorphic continuation theorem, and functional equation for ζ with their precise domains.
2. For real σ>1, convergence of Σ n^{-σ}; |μ(n)|≤1; and Σ_{d|n}μ(d)=1 for n=1 and 0 otherwise.
3. Absolute summability of the double product and its regrouping by mn=k, giving ζ(s)M(s)=1 for Re(s)>1.
4. Meromorphicity of conjugate-reflected functions and the meromorphic identity theorem, yielding the conjugation identity and preservation of zero order.
5. Nonvanishing of the functional-equation prefactor on 0<Re(s)<1 and preservation of zero order under s↦1-s.
6. The polynomial's factorization, two symmetry identities, two positivity identities, and four off-line roots.

7. Uniform absolute convergence of the Euler-product logarithm on Re(s)≥1+δ, δ>0, and the finite-prime-product tail estimate proving exp L=ζ.
8. The identity 3+4cos θ+cos 2θ=2(1+cos θ)², its summed logarithmic inequality for σ>1, and exponentiation.
9. Local bounds at a simple pole, a zero of order m, and a regular point, giving the contradiction 1≤C h^{4m-3} as h decreases to zero for t≠0.

10. Integral comparison giving residue 1, the local functional-equation expansion giving ζ(0)=-1/2, and the classification and simplicity of zeros outside the open strip.

11. Divergence of reciprocal-prime sums via finite products and harmonic sums; the k=1 comparison; and the continuity counterexample F(0,0)=1/256 to the proposed continued inequality.

12. The alternating-series compact tail bound, removable product identity for η, paired positivity for real 0<σ<1, and the absolutely convergent indicator-kernel integral.
13. The elementary cubic root count and Vieta modulus bound in Lemma 15, the compact-support Laplace transform, and its zero obtained from an individual complex logarithm.

14. Poisson summation with the stated Fourier convention and Gaussian transform; theta transformation and its derivative tail bounds.
15. Absolute Fubini for the Mellin integral, the split identity, and the compact derivative majorants proving I entire.
16. Entirety, two symmetries, endpoint values, continued product formula, and exact zero/multiplicity correspondence for ξ and Ξ.

17. The differentiated theta identity, exact A and K derivative formulas, termwise K positivity, and superexponential majorants.
18. The change x=e^{2u}, both integration-by-parts boundary terms, and local uniform convergence of every complex derivative of the cosine integral.

19. Absolute cosine-series domination and moment Cauchy–Schwarz; the shifted superexponential counterexample, its Fourier factorization, and the exact off-real zero (π+i log(2+√3))/4.

20. The explicit entire-growth bound, the order-at-most-one Hadamard theorem, reciprocal-square summability, justified ± pairing, and local logarithm coefficient identities.
21. The analytic rectangle bound |J|<1/72, infinitude of zeros, positivity of S_1,…,S_6, strict moment inequalities, and the degree-two Jensen root calculation.
22. The scalar-sign counterexample including its cosine multiplier, convergent mixed forms, finite interpolation witness, and infinite interpolation witness with the C²4^{-N} tail bound.
23. Corollary 32a as an equivalence only, the moment determinant formulas, and the exact negative determinant for the conjugate-node example. Proving all actual Hankel matrices positive semidefinite would remain a separate missing theorem.
24. The explicit E and E_m truncation estimates, eighth-derivative Taylor panel bound, and normalized derivative recurrences.
25. Rational Machin bounds, verified interval-operation contracts (or an independent rational interval implementation), and rechecking the saved certificates' full rational endpoints against every intermediate enclosure. This would replace the current reliance on the documented Decimal implementation.
26. Newton's recurrence and the positive-principal-minor implication, yielding the finite conclusions H_1>0 and H_2>0 from their respective interval certificates.

Even checking every item would certify only the partial results and the stated equivalence, not the missing all-degree positivity or RH.

## Coverage beyond the original inventory

The numbered inventory above was recorded through Lemma 41. For Lemmas 42–57, formalize each exact hypothesis and conclusion in its lemma file, including the convergence bounds, curvature estimates, comparison-transform energy identity, and the dependence of the small shift on the fixed finite degree. This is an inventory extension, not a claim of formal verification. Future lemma-specific obligations belong beside their proofs.
