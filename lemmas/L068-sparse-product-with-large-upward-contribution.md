# Lemma 68: sparse product with large upward contribution

**Hypotheses and construction.** For integers n≥1 set x_n=2^n, b_n=1-2^{-n}, and c_n=1-2^{-n-1}. Define

f(z)=Π_{n≥1} Π_{h∈{b_n,c_n}} [(1-z²/(x_n+ih)²)(1-z²/(x_n-ih)²)].

**Conclusion.** This is an even real entire function with f(0)=1, positive on the imaginary axis, and growth log M_f(r)=O((log(2+r))²). In particular its order is zero, hence at most one. Its zeros are precisely the simple zeros ±(x_n±ib_n) and ±(x_n±ic_n). Their imaginary parts have finite, nonattained supremum H=1, and their reciprocal squares are absolutely summable.

For every zero w=a+ib with b>0 define the upward contribution, as in Lemma 67, by

E_f(w)=2Σ_{ρ: Im ρ>b}(Im ρ-b)/|w-ρ|².

This sum is finite. Nevertheless the simple zeros w_n=x_n+ib_n satisfy Im w_n→1 and

E_f(w_n)≥2^{n+2}→∞.

Thus finite strip height, symmetry, and order-at-most-one paired-product growth do not imply vanishing upward contribution along every sequence of simple zeros approaching a nonattained height supremum.

## Proof

There are four paired factors for each n. Their representatives α have |α|≥2^n, so Σ_α |α|^{-2}≤4Σ_{n≥1}4^{-n}<∞. On each disc |z|≤R the sum of |z²/α²| converges uniformly. In the tail it is at most 1/2 termwise, so the power-series logarithms log(1-z²/α²) converge absolutely uniformly there, using |log(1-u)|≤2|u| for |u|≤1/2. The tail product is the exponential of that sum, hence holomorphic and nonzero. The finite initial factors show that the full product is entire, and that there are no zeros besides their listed roots.

All listed roots are distinct: different n have different absolute real parts, and for fixed n the two strictly positive heights b_n<c_n are distinct. Each root occurs in one quadratic factor and is a simple root of that factor; the residual product is nonzero there. Every zero is therefore simple. The product is even. Conjugation swaps the two factors at each height, proving f(conjugate(z))=conjugate(f(z)). At z=iy each such factor pair equals |1+y²/(x_n+ih)²|²>0. Its finite products are positive, and the limit is nonzero by the preceding logarithmic argument, so f(iy)>0. Also f(0)=1.

For |z|≤r, taking absolute values of the factors gives

log M_f(r)≤4Σ_{n≥1} log(1+r²/4^n).

For r≥2 put N=floor(log₂ r). The terms n≤N contribute at most 4N log(1+r²). The tail, using log(1+t)≤t, contributes at most

4r²Σ_{n>N}4^{-n}=(4/3)r²4^{-N}<16/3.

This proves the asserted growth bound. The function is nonconstant (it has zeros); the definition of order limsup_{r→∞} log log M_f(r)/log r therefore gives order zero. The full zero multiset has eight elements per n, yielding Σ_ρ |ρ|^{-2}≤8Σ_{n≥1}4^{-n}<∞. All heights have absolute value below 1, while b_n→1, so H=1 is not attained.

The convergence argument for imaginary sums in Lemma 67 applies directly: for fixed w, the sum of |w-ρ|^{-2} over zeros other than w is finite, by |w-ρ|≥|ρ|/2 in the tail and discreteness in the finite part. The numerator 2(Im ρ-b) of each upward term lies between 0 and 4. Thus E_f(w) is finite and is a sum of nonnegative terms.

At w_n the higher zero ρ_n=x_n+ic_n alone contributes

2(c_n-b_n)/|w_n-ρ_n|²=2/(c_n-b_n)=2^{n+2}.

Dropping the remaining nonnegative terms proves the lower bound and divergence. ∎

## Qualifications

This is a counterexample to a generic sufficient estimate, not a theta zero configuration and not a counterexample to RH. No positive Fourier kernel or jointly entire heat evolution for f is asserted. Order zero satisfies the stated order-at-most-one assumption and the usual weaker upper growth bound O(r log(2+r)).

The statement disproves a universal sequential vanishing assertion. It does not exclude the existence of another sequence approaching H along which E_f tends to zero. It also does not establish the sign of the full imaginary interaction: negative contributions were omitted, and their effect has not been estimated here. A height-envelope derivative still requires additional arguments even if individual branch velocities are controlled.

## Verification and formalization obligations

The proof needs no numerical certificate. Check normal convergence and nonvanishing of the logarithmic tail, distinctness of all eight zeros per n, the four-factor growth estimate, and the single-term lower bound. The exact height and contribution arithmetic can be reproduced with `python3 scripts/heat/check_sparse_product.py`; this finite check supplements, and does not replace, the infinite-product proof. Formalization would require the normal-product theorem via logarithmic series, the order definition and growth estimate, and convergence and monotonicity of the nonnegative upward sum.
