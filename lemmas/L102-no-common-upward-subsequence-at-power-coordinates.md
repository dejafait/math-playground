# Lemma 102: no common upward subsequence at power coordinates

**Hypotheses.** Set P equal to the positive integers in Lemma 100,
so x_n=n^(3/4). Let S be any infinite subset of the positive integers.

**Conclusion.** There exist heights 0<b_1<b_2<⋯ tending to a finite
H≤7/3 such that, for the product and full upward contribution of
Lemma 100, infinitely many n∈S satisfy E_f(x_n+i b_n)≥32/73.
Consequently this prescribed set P admits no increasing subsequence
along which the full upward contribution tends to zero for every
permitted height sequence.

## Proof

Recursively choose n_l∈S, for l≥1, with n_l≥2^(4l) and
n_(l+1)>n_l+1. This is possible because an infinite subset of the
positive integers is unbounded. For r≥1 define

Δ_r=2^(−r)+Σ_{l≥1}1_{r=n_l}n_l^(−1/2),
b_n=1+Σ_{r=1}^{n−1}Δ_r.

The marked indices are distinct, so each defining sum for Δ_r has
at most one nonzero marked term. Every Δ_r is positive and

Σ_{r≥1}Δ_r=1+Σ_{l≥1}n_l^(−1/2)
           ≤1+Σ_{l≥1}2^(−2l)=4/3.

Thus b_1=1 and the heights increase strictly to
H=1+Σ_rΔ_r≤7/3. Lemma 100 supplies the nonzero entire product,
its exact simple zeros, and finiteness and nonnegativity of the full
upward sum for these coordinates and heights.

Fix a marked index n=n_l. The decreasing derivative of v^(3/4)
gives

a_n=x_(n+1)−x_n=∫_n^(n+1)(3/4)v^(−1/4)dv
                   ≤(3/4)n^(−1/4).

Also 2^(−n)≤n^(−1/2) for every positive integer n: for example,
4^n≥n follows by induction. Therefore

n^(−1/2)≤Δ_n≤2n^(−1/2),
a_n²+Δ_n²≤(9/16)n^(−1/2)+4n^(−1)
                  ≤(73/16)n^(−1/2).

The zero w_(n+1)=x_(n+1)+i b_(n+1) is higher than w_n. Its single
term in the nonnegative full upward sum proves

E_f(w_n)≥2Δ_n/(a_n²+Δ_n²)≥32/73.

This holds at every n_l, proving the conclusion. In particular, given
any proposed increasing subsequence, apply the construction to its
range S. Its contributions cannot tend to zero for the resulting
permitted heights. ∎

## Qualifications and verification

The quantifiers are essential: the heights may depend on the proposed
subsequence. This does not assert one height sequence obstructing every
subsequence. Lemma 101 still gives a vanishing subsequence for each
fixed height sequence. It disproves the universal common-subsequence
claim for prescribed sets by the single choice P equal to all positive
integers; it does not classify other P or address theta zeros or RH.

The proof is analytic and requires no numerical certificate. Checks
are the recursive sparse extraction, positive summable increments,
the common height bound, the derivative estimate, both directions of
the successor-term bound, and the order of the quantifiers.
Formalization would require these elementary estimates and extraction,
series convergence, and Lemma 100's product and full-sum conclusions.
