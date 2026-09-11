# Lemma 83: close pairs obstruct unrestricted upward averaging

**Hypotheses.** For integers k≥1 set

x_{2k−1}=2^k,   x_{2k}=2^k+4^{−k},   b_n=1−2^{−n},

w_n=x_n+i b_n,   f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

**Conclusion.** The x_n are strictly increasing with Σ x_n^{−2}<∞,
and the b_n increase strictly to 1. The product is a nonzero even real
entire function with exactly the simple zeros ±w_n, ±conjugate(w_n).
The full upward contribution

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²

is finite at every n, but for every N≥2,

(1/N)Σ_{n=N}^{2N−1}E_f(w_n) ≥ 2^{N+1}/N → ∞.       (1)

Nevertheless E_f(w_{2k})≤(68/3)4^{−k}, so liminf_n E_f(w_n)=0.
Thus increasing coordinates and reciprocal-square summability alone do
not imply vanishing full upward block averages.

## Proof

Within each pair the horizontal gap is 4^{−k}>0; between pairs,
2^{k+1}−(2^k+4^{−k})=2^k−4^{−k}>0. The coordinates tend to infinity and

Σ_n x_n^{−2}≤2Σ_{k≥1}4^{−k}=2/3.

The assertions about heights are immediate from their formula. Lemma 74
therefore supplies the product and its exact simple zero set. The only
zeros higher than w_n are w_j and −conjugate(w_j) with j>n, giving

E_f(w_n)=U_n+V_n,

U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],

V_n=2Σ_{j>n}(b_j−b_n)/[(x_j+x_n)²+(b_j−b_n)²].

For fixed n, eventually x_j≥2x_n, and the corresponding U_n summands
are at most 8x_j^{−2}, since 0<b_j−b_n<1. The finitely many preceding
denominators are positive. Also V_n≤2Σ_{j>n}x_j^{−2}. Thus both full
series converge; all subsequent inequalities hold for their nonnegative
partial sums and then their limits.

For n=2k−1 the successor has

x_{2k}−x_{2k−1}=b_{2k}−b_{2k−1}=4^{−k}.

Its single contribution to U_{2k−1} equals

2·4^{−k}/[2·4^{−2k}]=4^k=2^{n+1}.

Every integer interval [N,2N−1] with N≥2 contains an odd n≥N.
Keeping just this contribution proves (1). Its lower bound tends to
infinity, for example because the ratio of consecutive bounds is
2N/(N+1)≥4/3 for N≥2.

For the even indices, x_{2k}≤(3/2)2^k, while x_j≥2^{k+1} for j>2k.
Consequently x_{2k}/x_j≤3/4 and x_j−x_{2k}≥x_j/4. Hence

U_{2k}≤32Σ_{j>2k}x_j^{−2},   V_{2k}≤2Σ_{j>2k}x_j^{−2}.

The remaining indices consist of entire pairs with pair index l≥k+1, so

Σ_{j>2k}x_j^{−2}≤2Σ_{l≥k+1}4^{−l}=(2/3)4^{−k}.

This proves the stated even-index upper bound and, by nonnegativity,
the zero lower limit. ∎

## Qualifications

The multiplier condition in Lemma 82 is absent here. Indeed
x_{2k}/x_{2k−1}=1+2^{−3k}<sqrt(2k/(2k−1)), so the multiplier decreases
within every pair. To verify this inequality, squaring reduces it to
2·2^{−3k}+2^{−6k}<1/(2k−1). The left side is at most
(17/8)2^{−3k}; multiplying by 2k−1 gives 17/64 at k=1 and decreases
thereafter, since the consecutive ratio is (2k+1)/(8(2k−1))<1.
The obstruction comes from very strong contributions at odd indices,
not from a positive lower bound at all sufficiently large indices.
The unrestricted favorable-subsequence question remains open in this
write-up. No theta-specific geometry, heat-flow statement, signed
velocity conclusion, or RH conclusion is asserted.

## Verification and formalization obligations

The proof uses exact inequalities and geometric sums; no numerical
certificate is required. Check coordinate ordering, the summability
bound, Lemma 74's product hypotheses, higher-zero enumeration, fixed-n
tail convergence, equality of the two successor gaps, block parity,
the even-index separation bound, and the geometric tail endpoints.
Formalization also requires passage from nonnegative finite partial sums
to full sums, divergence of the lower bound in (1), and the subsequence
argument for the lower limit.
