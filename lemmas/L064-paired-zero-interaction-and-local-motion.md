# Lemma 64: paired-zero interaction and local motion

**Hypotheses.** Let F be the theta heat deformation of Lemma 58, fix a real parameter λ₀, and set f(z)=F(λ₀,z). Let x be any simple zero of f. In the paired product of Lemma 63 choose x as the representative of its pair, and write α_j for the representatives of all remaining pairs, repeated according to multiplicity.

**Conclusion.** The zero x is nonzero, and

f''(x)/f'(x) = 1/x + 4x Σ_j 1/(x²-α_j²).                    (1)

The displayed series is absolutely convergent, independent of pair ordering and of representative signs. Equivalently its summand is twice the paired expression

1/(x-α_j)+1/(x+α_j)=2x/(x²-α_j²).

There is a local holomorphic simple-zero branch z(λ) with z(λ₀)=x. For every real λ sufficiently near λ₀, using the remaining zero pairs of that slice,

z'(λ)=1/z(λ)+4z(λ) Σ_j 1/(z(λ)²-α_j(λ)²).                 (2)

This is a slice-wise identity; it requires no continuous labeling of the other zeros. If x is real, the branch is real for nearby real λ. No global reality hypothesis is needed for either identity.

## Proof

Lemma 63 gives f(0)>0, so x≠0. Evenness makes -x a simple zero as well. Remove precisely this pair from the product and put

H(z)=f(0) Π_j(1-z²/α_j²),
f(z)=(1-z²/x²)H(z).

The residual product converges locally uniformly. Also H(x)≠0, since the removed zero is simple. We justify its logarithmic derivative rather than differentiating an unevaluated infinite product.

Fix M>|x| and separate the finitely many factors with |α_j|≤2M. For the rest and |z|≤M, |z²/α_j²|≤1/4, and the power-series logarithm satisfies

|log(1-z²/α_j²)|≤2M²/|α_j|²,
|2z/(z²-α_j²)|≤(8M/3)/|α_j|².

Reciprocal-square summability from Lemma 63 gives absolute uniform convergence of both these logarithms and their derivative series. The standard theorem on differentiation of uniformly convergent holomorphic series (or Cauchy's integral formula on slightly larger discs) therefore permits termwise differentiation. Choose a small disc about x avoiding every zero of the finite factors and contained in |z|<M. The tail is the exponential of its convergent logarithmic series; on this disc H is nonzero and

H'(z)/H(z)=Σ_j 2z/(z²-α_j²).

The finitely many separated terms have no poles there. In particular evaluation at x is legitimate and the series is absolutely convergent. With p(z)=1-z²/x², the elementary product rule gives

f'(x)=p'(x)H(x),
f''(x)=p''(x)H(x)+2p'(x)H'(x).

Since p'(x)=-2/x and p''(x)=-2/x², their ratio yields (1). The finite case, including an empty residual product, is covered by the same calculation.

For the branch assertion, joint entirety and F_λ=-F_zz are established in Lemma 58. The holomorphic implicit function theorem applies at any complex simple zero, just as in that lemma's real-zero proof. Shrinking its parameter neighborhood keeps F_z nonzero. Differentiating F(λ,z(λ))=0 gives z'=F_zz/F_z. For real λ in this neighborhood Lemma 63 applies afresh to that slice, so (1) gives (2). For real x, the conjugation and uniqueness argument in Lemma 58 proves the branch is real. No parameter differentiation of the zero series has been taken. ∎

## Qualifications

Absolute convergence means Σ_j |1/(x²-α_j²)|<∞. It does not assert absolute convergence of the individual terms 1/(x-ρ) over all other zeros ρ. The contribution of the remaining member -x of the distinguished pair is 2/(x-(-x))=1/x. Omitting it or forgetting the factor two in f''/f' gives an incorrect velocity.

Nonreal pairs and multiple zeros elsewhere are allowed. For real x the total in (1) is real, also directly because f is real entire, but individual pair contributions need not be real or have a prescribed sign. Even assuming other zeros real would give terms of both signs depending on their positions. Thus the identity alone supplies neither initial global reality, a global continuation bound, nor RH. It makes no assertion at a multiple distinguished zero.

## Verification and formalization obligations

The proof is analytic and needs no numerical certificate. The checks are the uniform logarithm and derivative bounds, removal of exactly one simple pair, the product-rule factor two, and the heat-equation sign. As a finite algebraic check, f(z)=(1-z²/x²)(1-z²/a²) gives f''(x)/f'(x)=1/x+4x/(x²-a²) whenever x,a≠0 and a²≠x². Formalization would require normal convergence of the residual product and its logarithmic derivative, the nonvanishing neighborhood, the displayed product-rule calculation, and the complex holomorphic implicit function theorem. No uniform-in-parameter convergence of the zero series is claimed or required.
