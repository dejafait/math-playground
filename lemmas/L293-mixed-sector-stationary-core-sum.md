# Lemma 293: summable mixed-sector stationary cores

**Hypotheses.** Use the exact reflected summands of L292 and the parameter identities of L269. Fix 5<h₀≤h₁<∞, let a tend to infinity with h∈[h₀,h₁], and write H=h−9/2=n/r. Set ε=r/sqrt(a). In the sector u,v>0, let T_jk(u,v) denote the exact summand displayed in L292 (before its Jacobian). Define

Q_jk={u,v>0: |u−(r−log j)|≤ε, |v−(r−log k)|≤ε}.

Empty squares have zero integral. This includes clipped squares whose centers lie just outside the sector.

**Conclusion.** With γ=2(h₀−9/2)log 2−1/2>0, uniformly in the stated range,

(1/2) Σ_(j,k≥1) ∫_(Q_jk) |T_jk(u,v)| du dv
 ≤ C exp(Φ_*) (r²/a) exp(−γr)
 = o(exp(Φ_*)/a).

The factor 1/2 is the coordinate Jacobian. This is a summand-wise core estimate, not an estimate of the whole kernel on the union of these squares. It gives no bound for the complementary parts of each summand or any new global Laguerre sign.

**Proof.** The parameter identities give r~(log a)/2, so ε→0. A nonempty Q_jk requires j,k<N:=exp(r+ε). Put

α=u−r+log j, β=v−r+log k, d=log(k/j).

Then |α|,|β|≤ε and u−v=d+α−β. Dividing the exact modulus in L292 by C₀ exp(Φ_*) gives

(jk)^(−1/2) |(d+α−β)/(2r)|^(2n)
 · exp(9(α+β)/2−(h/2)(exp(2α)+exp(2β)−2)) |E_j(u)E_k(v)|.   (1)

Indeed j⁴exp(9u/2)=exp(9r/2)j^(−1/2)exp(9α/2), and π cos(2τ)j²exp(2u)=(h/2)exp(2α). Also

E_j(u)=1−3exp(−2α)/(h+ia),

so both E factors are uniformly bounded on all these squares. The exponential in (1) is uniformly bounded as well, independently of j,k.

By symmetry it suffices to sum over j≤k and multiply by two. Here d≥0, and the polynomial is at most ((d+2ε)/(2r))^(2n). For every positive t, log t≤t−1. Applying this with t=(d+2ε)/r yields

((d+2ε)/(2r))^(2n)
 ≤ 2^(−2n) exp(2H(d+2ε−r)).                 (2)

This remains a valid upper bound when the actual polynomial vanishes. Equations (1)–(2), and the area bound |Q_jk|≤4ε², show that the total in the conclusion is at most

C exp(Φ_*) ε² 2^(−2n) exp(−2Hr+4Hε)
 · Σ_(k<N) k^(2H−1/2) Σ_(j≤k) j^(−2H−1/2).    (3)

Since H≥h₀−9/2>1/2, the inner series is bounded by a constant uniformly in H. Since H ranges over a fixed compact interval and 2H−1/2>0, elementary integral comparison bounds the outer sum by C N^(2H+1/2). Inserting N=exp(r+ε) into (3), and absorbing exp((6H+1/2)ε) into a uniform constant, gives

C exp(Φ_*) ε² exp((1/2−2H log 2)r).

Now ε²=r²/a and H≥h₀−9/2. In particular γ>log 2−1/2>0, and r²exp(−γr)→0. This proves the claim. Only finitely many Q_jk are nonempty for each a; no exchange of an infinite signed integral and a series is used. ∎

The squares have radius r in units of the stationary phase scale a^(−1/2), so they include a growing central Fresnel region. Their complements still need signed estimates uniform in indices, including boundary-adjacent centers. An estimate for those complements does not follow from the present absolute bound.

**Mathlib.** Full statement: not checked. Supporting logarithmic inequalities, finite power-sum estimates, and exponential domination of polynomials: not checked. No full or supporting library match is claimed. The exact summands and their coordinate Jacobian are supplied by L292; the normalization and parameter identities are from L269.
