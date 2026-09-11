# Lemma 86: increment-sensitive upward bound at suffix minima

**Hypotheses.** Let 0<x_1<x_2<⋯ satisfy Σ_n x_n^{-2}<∞, and let
0<b_1<b_2<⋯ tend to a finite H. Put Δ_r=b_{r+1}−b_r,
w_n=x_n+i b_n, and

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

Let S={n≥1: x_j/sqrt(j)≥x_n/sqrt(n) for every j≥n}. Define

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²,

where ρ runs over the zeros of f, and set

T_n=(n²/x_n²) Σ_{r=n}^{2n−1} Δ_r/(r−n+1).

**Conclusion.** The set S is unbounded, f has exactly the simple zeros
±w_n, ±conjugate(w_n), and E_f(w_n) is finite. For every n∈S,

0≤E_f(w_n)≤36 T_n+32H Σ_{j>2n}x_j^{-2}
                         +2H Σ_{j>n}x_j^{-2}.             (1)

In particular, if liminf_{n→∞, n∈S} T_n=0, there is an unbounded
subsequence of S on which the full upward contribution tends to zero.
If, for some C>0 and integer N, the additional increment condition

Δ_r≤C/[r log(r+1)]  for all r≥N                            (2)

holds, then E_f(w_n)→0 as n→∞ through all of S. This assertion imposes
no monotonicity on x_n/sqrt(n) and no separate height-deficit bound.

## Proof

Lemma 84 supplies unboundedness of S, the product and zero assertions,
fixed-index finiteness, and n/x_n²→0. Its enumeration of higher zeros
splits E_f(w_n) into a right-hand sum U_n and reflected sum V_n. For
n∈S, it proves

x_{n+k}−x_n≥x_n k/(3n)  (1≤k≤n),

2Σ_{j>2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²]
≤32H Σ_{j>2n}x_j^{-2},

V_n≤2H Σ_{j>n}x_j^{-2}.

For the remaining near part, retain the actual height difference and
drop only its nonnegative square in the denominator. This gives

2Σ_{k=1}^n (b_{n+k}−b_n)/[(x_{n+k}−x_n)²+(b_{n+k}−b_n)²]
≤(18n²/x_n²) Σ_{k=1}^n (b_{n+k}−b_n)/k².                  (3)

All sums in the following rearrangement are finite. Since
b_{n+k}−b_n=Σ_{r=n}^{n+k−1}Δ_r,

Σ_{k=1}^n (b_{n+k}−b_n)/k²
=Σ_{r=n}^{2n−1} Δ_r Σ_{k=r−n+1}^n k^{-2}
≤2Σ_{r=n}^{2n−1} Δ_r/(r−n+1).                            (4)

Indeed, for every integer l≥1 the decreasing-integrand comparison gives
Σ_{k=l}^∞ k^{-2}≤l^{-2}+∫_l^∞ t^{-2}dt=l^{-2}+l^{-1}≤2/l.
Combining (3), (4), and the two tails proves (1). Both tails vanish as
n→∞. If the nonnegative T_n has lower limit zero through S, recursively
choose increasing n_m∈S with T_{n_m}<1/m. Bound (1) proves the stated
subsequence conclusion.

Now assume (2). For n≥N and n≤r≤2n−1, both r≥n and
log(r+1)≥log(n+1), so

Σ_{r=n}^{2n−1} Δ_r/(r−n+1)
≤ C/[n log(n+1)] Σ_{l=1}^n 1/l
≤ C(1+log n)/[n log(n+1)].

The harmonic bound follows by integrating 1/t from 1 to n. Also
(1+log n)/log(n+1)≤1+1/log 2 for all n≥1. Consequently

0≤T_n≤C(1+1/log 2)n/x_n²→0.

This limit holds even before restriction to S; (1) proves convergence
of the full upward contribution through S. ∎

## Strict extension of the previous sufficient condition

Use the admissible sequences from Lemma 85:

x_n=sqrt(n) log(n+2),   b_n=1−1/log(n+2),   H=1.

That lemma proves (H−b_n)n²/x_n²→∞ along every unbounded index set,
so Lemma 84's height-deficit condition cannot apply. Here, however,
the fundamental theorem of calculus gives

Δ_r=∫_r^{r+1} dt/[(t+2)log²(t+2)]
≤1/[(r+2)log²(r+2)]≤1/[r log(r+1)].

The first inequality uses that the positive denominator increases;
the second follows from r+2≥r and
log²(r+2)≥log(r+2)>log(r+1), because log(r+2)≥log 3>1.
Thus (2) holds with C=1. In this example every index is in S since
x_n/sqrt(n)=log(n+2) increases. Full upward convergence follows.
The new general assertion applies to arbitrary admissible coordinates,
including ones for which this multiplier is not monotone.

## Qualifications

Condition (2) is additional, not a consequence of summability of Δ_r.
For example Δ_r=2^{-r}+1/m² when r=2^m (m≥1), and Δ_r=2^{-r}
otherwise, defines a strictly positive summable sequence; nevertheless
r log(r+1)Δ_r is unbounded at r=2^m. Taking b_1=1 and summing these
increments gives admissible increasing bounded heights. This example
only shows that (2) is not automatic; it does not refute the condition
on T_n or the desired full upward lower limit.

The step proves a scoped extension using actual increments. It does
not establish a rate-free subsequence for arbitrary bounded increasing
heights, nor assert that failure of its upper bound forces positive
upward motion. The general condition on T_n remains unproved without
extra assumptions. No theta-specific or RH conclusion follows.

## Verification and formalization obligations

The proof is analytic; no computational certificate is required. Verify
the inherited suffix-gap and tail bounds, finite rearrangement endpoints,
the reciprocal-square weight bound, harmonic bound, uniform logarithmic
ratio, and subsequence selection. Check the calculus estimate for the
slow-height example and summability of the sparse increments. Infinite
limits use only the already convergent tails from Lemma 84; there is no
interchange of an unbounded near sum with a subsequence limit.
