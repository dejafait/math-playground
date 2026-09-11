# Lemma 77: full upward subsequence with growing local counts

**Hypotheses.** Assume the monotone quartet hypotheses and paired product f of Lemma 74: positive coordinates x_n increase strictly to infinity, positive heights b_n increase strictly to a finite H, and Σ_n x_n^{-2}<∞. Set w_n=x_n+i b_n and h_n=H−b_n. Suppose there are constants C≥1 and 0≤α<1 such that every half-open interval [t,t+1), t≥0, contains at most C(1+t)^α coordinates. Assume also

h_n(1+x_n)^{3α} → 0.

**Conclusion.** With c=[2C(α+1)2^α]^{-1}, the set

S={n:x_{n+1}−x_n≥c(1+x_n)^{-α}}

is infinite. The full upward contribution

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²

tends to zero as n tends to infinity in S. In particular liminf_n E_f(w_n)=0. The sum ranges over the zeros of f, with multiplicity.

## Proof

Lemma 74 gives the exact simple zero set, and thus E_f(w_n)=U_n+V_n, where

U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²]

and V_n is the reflected sum of that lemma. It also gives V_n≤2HΣ_{j>n}x_j^{-2}→0. For fixed n the U_n series converges: the finitely many terms with x_j<2x_n have positive denominators and all remaining terms are bounded by 8H/x_j².

### Infinitely many adequately sized gaps

Counting the coordinates up through x_n in integer unit intervals gives

n≤Σ_{k=0}^{floor(x_n)} C(1+k)^α
 ≤C(floor(x_n)+1)(1+x_n)^α
 ≤C(1+x_n)^{α+1}.                                      (1)

Suppose S were finite. Then for all n≥N, the gap d_n=x_{n+1}−x_n would satisfy d_n<c(1+x_n)^{-α}. Since c≤1/2, this implies 1+x_{n+1}≤2(1+x_n). Applying the mean value theorem to F(x)=(1+x)^{α+1}, whose derivative is increasing, gives

F(x_{n+1})−F(x_n)
 ≤(α+1)(1+x_{n+1})^α d_n
 ≤(α+1)2^α(1+x_n)^α d_n
 <(α+1)2^α c=1/(2C).

Therefore F(x_n)≤F(x_N)+(n−N)/(2C) for n≥N. But (1) requires F(x_n)≥n/C, a contradiction for large n. Thus S is infinite.

### The entire right-hand sum

Fix n∈S, write X=1+x_n≥1 and g=cX^{-α}≤1, and partition the future coordinates into bins

I_k=[x_n+g+k,x_n+g+k+1),  k≥0.

There are at most C(X+g+k)^α coordinates in I_k. Each has horizontal distance at least g+k and height difference at most h_n. The bin estimate, first on finitely many bins and then by monotone limits, is

U_n≤2Ch_n Σ_{k≥0}(X+g+k)^α/(g+k)².                     (2)

For k=0, X+g≤2X, so the term is at most 2^α c^{-2}X^{3α}. For k≥1, X+g+k≤X(k+2), g+k≥k, and k+2≤3k. Consequently

Σ_{k≥1}(X+g+k)^α/(g+k)²
 ≤3^α X^α Σ_{k≥1}k^{α−2}
 ≤3^α X^α [1+1/(1−α)].                                (3)

The final inequality follows by integrating t^{α−2} on [1,∞), after separating its first term. This is where α<1 is needed. Since X^α≤X^{3α}, (2) and (3) yield

U_n≤2C{2^α c^{-2}+3^α[1+1/(1−α)]} h_n X^{3α}.          (4)

The assumed height-tail rate makes (4) tend to zero on S. The reflected contribution tends to zero along all indices, proving the conclusions. ∎

## Strict enlargement and limitations

Take x_n=n^{2/3}, b_n=2−n^{-2}, n≥1. These satisfy the monotonicity hypotheses with H=2, and Σ x_n^{-2}=Σ n^{-4/3}<∞. The number of coordinates in [t,t+1) is at most

(t+1)^{3/2}−t^{3/2}+1≤(3/2)(t+1)^{1/2}+1≤(5/2)(1+t)^{1/2}.

Thus C=5/2 and α=1/2 work. Moreover

h_n(1+x_n)^{3α}=n^{-2}(1+n^{2/3})^{3/2}≤2^{3/2}/n→0.

The unit counts are unbounded: the number in [m,m+1) is at least (m+1)^{3/2}−m^{3/2}−1, which tends to infinity. Hence this example is covered here but not by the bounded-count hypothesis of Lemma 76. At α=0 the height-tail assumption is automatic; the present proof then also covers that bounded-count case.

This is a sufficient condition, not a resolution of unrestricted monotone quartets. Neither polynomial local counts nor the height-tail rate is implied by reciprocal-square summability. For instance the same coordinates with b_n=2−n^{-1/2} still meet Lemma 74's hypotheses but violate the displayed rate condition. That is a limitation of this estimate, not a counterexample to vanishing lower limit. No penalty-maximizer selection, theta-specific hypothesis, signed-motion estimate, or RH conclusion is established.

## Verification and formalization obligations

The proof is analytic and needs no computational certificate. Required checks are the integer-bin count (1), mean value bound with its explicit constant, finite-bin bounds followed by monotone limits, convergence of the power tail in (3), and the rate implication in (4). The example uses elementary integer counting, the mean value theorem, and the convergent p-series test. Formalization would also require Lemma 74's product zero set and reflected tail bound and an enumeration of S. There is no exchange of a varying-index limit with an uncontrolled infinite sum.
