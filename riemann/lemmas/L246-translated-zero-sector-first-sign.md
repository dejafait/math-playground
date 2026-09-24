# Lemma 246: six logarithmic-derivative signs on the whole positive axis

**Hypotheses.** Let F(x)=Ξ(i√x) and G(x)=F′(x)/F(x) as in L242, for real x≥0. Let α_j be the paired zero representatives of L024, chosen with positive real part.

**Conclusion.** For every x≥0 and integer 1≤k≤6,

T_k(x):=Σ_j(x+α_j²)^(−k)=(-1)^(k−1)G^(k−1)(x)/(k−1)! >0.

All displayed series converge absolutely and locally uniformly. In particular G′(x)<0 on the entire interval [0,∞), including the previously unresolved compact range. These six derivative signs do not assert complete monotonicity, a positive Stieltjes representation, or all-degree mixed positivity.

**Proof.** L026 gives α_j=a_j+ib_j with a_j>4 and |b_j|<1/2. Therefore |arg α_j|<1/8, as in L027, and Re(α_j²)=a_j²−b_j²>0. Adding any real x≥0 preserves the sign of the imaginary part and increases the positive real part. Thus

|arg(x+α_j²)|≤|arg α_j²|=2|arg α_j|<1/4.

Also b_j²/a_j²<1/64 implies

|x+α_j²|≥x+a_j²−b_j²≥(63/65)|α_j|².

L024 supplies Σ_j|α_j|^(−2)<∞; since |α_j|>4, every higher reciprocal even-power series also converges. The last bound consequently proves absolute convergence of each T_k uniformly for real x≥0.

Here we justify the logarithmic-derivative identities beyond the small Taylor disk used in L242. The even power series of Ξ makes F an entire function of x, and the product in L024 gives

F(x)=F(0)Π_j(1+x/α_j²).

The identity follows either by substituting a square root in the even product, or by the identity theorem from its validity on the positive axis. On any bounded complex x set, the tail has |x/α_j²|≤1/2; its normalized logarithms converge absolutely locally uniformly by Σ|α_j|^(−2)<∞. Every differentiated tail series converges locally uniformly as well, since the k-th derivative is a constant times (x+α_j²)^(−k), bounded in that tail by a constant times |α_j|^(−2k). Near any fixed x≥0 the finitely many head factors are nonzero, and F(x)>0 by L242. We may therefore logarithmically differentiate locally, obtaining G=T_1 and, by repeated differentiation, the formula for T_k. This also establishes all derivatives at zero without division by √x.

The quantities T_k are real because G and its derivatives are real on the positive axis. Absolute convergence permits taking real parts termwise. For 1≤k≤6,

Re((x+α_j²)^(−k))=|x+α_j²|^(−k) cos(k arg(x+α_j²))>0,

because |k arg(x+α_j²)|<k/4≤3/2<π/2. L027 supplies infinitely many zeros, so the sum is nonempty and strictly positive. For k=2 this proves the requested strict first sign on every x≥0. ∎

The attained threshold is the exact sign G′<0, not a uniform positive lower bound for −G′. L245's quantitative large-parameter estimate remains a separate stronger bound there. This argument extends the six signs at x=0 from L027 to all nonnegative translations; it does not allow k→∞ in the angular inequality. At k=7 the bound 7/4 already exceeds π/2. Nor do positive scalar sums imply positive mixed forms. The proof uses only established zero geometry and the unconditional product, so it supplies no additional actual-theta mechanism to remove these limitations.

**Mathlib.** Not checked: coverage of the full translated-sector statement and supporting locally uniform product differentiation and complex argument results was not checked. No matching theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
