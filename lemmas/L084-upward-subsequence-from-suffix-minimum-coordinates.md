# Lemma 84: upward subsequence from suffix-minimum coordinates

**Hypotheses.** Let 0<x_1<x_2<⋯ with Σ_n x_n^{-2}<∞, and let
0<b_1<b_2<⋯ tend to H<∞. Put h_n=H−b_n, w_n=x_n+i b_n, and

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

Define S={n≥1: x_j/sqrt(j)≥x_n/sqrt(n) for every j≥n} and

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²,

where ρ ranges over the zeros of f.

**Conclusion.** The set S is unbounded. The product has the properties
and simple zero set stated in Lemma 74, and E_f(w_n) is finite for every n.
For every n∈S,

0≤E_f(w_n)≤36 h_n n²/x_n²
             +32H Σ_{j>2n}x_j^{-2}+2H Σ_{j>n}x_j^{-2}.       (1)

Consequently, if h_n n²/x_n²→0 as n→∞ through S, then
E_f(w_n)→0 through S and liminf_n E_f(w_n)=0. In particular the latter
conclusion holds for every coordinate sequence in the hypotheses if
h_n=O(1/n). No monotonicity of x_n/sqrt(n) is required.

## Proof

First, x_n→∞: otherwise the increasing positive coordinates would be
bounded and their reciprocal-square series would diverge. For n≥2,
the block from ceil(n/2) to n contains at least n/2 terms, each at least
x_n^{-2}. Thus

n/(2x_n²)≤Σ_{j=ceil(n/2)}^n x_j^{-2}
          ≤Σ_{j≥ceil(n/2)}x_j^{-2}→0.                       (2)

It follows that a_n=x_n/sqrt(n)→∞. For every N the sequence (a_j)_{j≥N}
attains a minimum: choose M>N so that a_j>a_N for all j≥M, and minimize
on the finite set N≤j<M. Any minimizing index n belongs to S and is at
least N. This proves that S is unbounded, including when minima tie.

Lemma 74 now applies and supplies the paired product and exact simple
zero set. Since all b_n are positive and strictly increasing, the zeros
higher than w_n are precisely w_j and −conjugate(w_j) with j>n. Therefore

E_f(w_n)=U_n+V_n,

U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],

V_n=2Σ_{j>n}(b_j−b_n)/[(x_j+x_n)²+(b_j−b_n)²].

For fixed n, eventually x_j≥2x_n, and each corresponding term of U_n
is at most 8H x_j^{-2}. All earlier terms are finite since x_j>x_n.
Lemma 74 gives convergence of V_n and the bound

V_n≤2H Σ_{j>n}x_j^{-2}.                                  (3)

Fix n∈S. For 1≤k≤n the defining inequality for S gives

x_{n+k}−x_n ≥ x_n(sqrt(1+k/n)−1)
            = x_n k/[n(sqrt(1+k/n)+1)]
            ≥ x_n k/(3n).

Here sqrt(1+k/n)+1≤sqrt(2)+1<3. Dropping the nonnegative squared
height difference in the denominator, using b_{n+k}−b_n≤h_n, and
using Σ_{k≥1}k^{-2}≤2, we obtain

2Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²]
≤18 h_n n²/x_n² Σ_{k=1}^n k^{-2}
≤36 h_n n²/x_n².                                         (4)

The reciprocal-square bound follows, for example, by comparing the
terms k≥2 with the integral of t^{-2} on [1,∞).

For j>2n the same defining inequality implies x_n/x_j≤sqrt(n/j)
<1/sqrt(2)<3/4, so x_j−x_n≥x_j/4. Consequently

2Σ_{j>2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²]
≤32H Σ_{j>2n}x_j^{-2}.                                   (5)

Apply the termwise bound first to finite partial sums and then take
their nonnegative increasing limits. Combining (3)–(5) proves (1).
Both tails in (1) tend to zero independently of the selected indices.
The stated sufficient condition therefore proves convergence through
the unbounded set S and the zero lower limit by nonnegativity.

Finally, if h_n≤C/n for all sufficiently large n, then

0≤h_n n²/x_n²≤C n/x_n²→0

by (2), even without restriction to S. This proves the particular case. ∎

## Qualifications

The condition on the height deficit is additional. Strictly increasing
heights with a finite limit do not imply h_n=O(1/n); for example,
b_n=1−1/log(n+2) are positive and strictly increase to 1 but n h_n
is unbounded. Indeed, with these heights and x_n=sqrt(n) log(n+2),
the reciprocal-square series converges by comparison for n≥2 with
Σ 1/[n(log n)²], whose integral converges after the substitution u=log t.
Every index belongs to S, but h_n n²/x_n²=n/[log(n+2)]³→∞. Thus the
sufficient condition itself is not automatic; this example is an
obstruction to using bound (4) alone, not a counterexample to liminf zero.
No bound for the near contribution in (4) tending to zero for every
permitted pair of sequences is proved here. Minima over tails
of x_n/sqrt(n) only control future coordinate separation; they do not
make the multiplier globally monotone or justify block averaging.
The unrestricted liminf assertion remains unresolved. This is a generic
paired-product result, with no theta-specific or RH implication.

## Verification and formalization obligations

This proof is analytic and requires no numerical certificate. Check the
finite-block proof of (2), attainment and unboundedness of suffix minima,
the product hypotheses and enumeration of higher zeros, fixed-index
series convergence, both separation estimates, and the nonnegative tail
passages. Formalization also needs enumeration of an unbounded subset of
the natural numbers and the resulting subsequence limit. Lemma 74 is used
for product properties and the reflected-sum estimate; all other bounds
are proved here.
