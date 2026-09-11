# Lemma 107: forward-jump obstruction to upward selection

**Hypotheses.** Let 0<x_1<x_2<⋯ and Σ_n x_n^(-2)<∞. Set

a_nj=(x_j−x_n)^(-2) for j>n, and K_n=Σ_{j>n}a_nj.

Define an integer-valued Markov chain Y_m, starting at Y_0=n, by

P(Y_(m+1)=j | Y_m=i)=a_ij/K_i, j>i.

Independently of this chain let Z_m be independent exponential random
variables of mean one. Define its lifetime by the nonnegative series

T=Σ_{m≥0} Z_m/K_(Y_m).

Here finite lifetime means infinitely many forward jumps occur in finite
time; this is the meaning of explosion in this lemma. For strictly
increasing positive bounded heights b_n, set H=lim b_n and let E_n be
the full upward contribution of the paired product in Lemma 106.

**Conclusion.** If E_n≥ε>0 for every sufficiently large n, then there
is N such that, for every starting index n≥N,

E_n[T]≤4(H−b_n)/ε<∞, and P_n(T<∞)=1.                 (1)

The subscripts on expectation and probability specify the starting
index and do not denote the upward contribution. Consequently, if
there are arbitrarily large starting indices n with P_n(T=∞)>0,
then every permitted height sequence admits an increasing subsequence
along which its full upward contribution tends to zero.

## Proof

Lemma 106 proves 0<K_n<∞ and provides the paired product, its exact
simple zero set, and the decomposition

E_n=U_n+V_n,
U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],
0≤V_n≤2HΣ_{j>n}x_j^(-2)→0.                         (2)

Thus the transition probabilities are well defined and sum to one.
One explicit construction uses successive independent uniform random
variables and the cumulative probabilities in each row. This defines
the entire discrete chain regardless of whether T is finite. Always
Y_(m+1)>Y_m, hence Y_m≥n+m and Y_m→∞.

Suppose E_i≥ε eventually. Increase N so that this holds and V_i≤ε/2
for every i≥N. Then U_i≥ε/2 on that tail. Define the finite linear
quantity

L b(i)=Σ_{j>i}a_ij(b_j−b_i).

It is at most (H−b_i)K_i<∞. Dropping the nonnegative vertical square
in the denominators of U_i gives

L b(i)≥U_i/2≥ε/4=:c, i≥N.                          (3)

Fix n≥N. At each step all visited indices are at least N. Conditional
on Y_m=i, the expected height increment equals L b(i)/K_i, since
it is a bounded nonnegative random variable with the displayed
countable distribution. Therefore, for every integer M≥1,

c E_n[Σ_{m=0}^{M−1}1/K_(Y_m)]
 ≤Σ_{m=0}^{M−1} E_n[b_(Y_(m+1))−b_(Y_m)]
 =E_n[b_(Y_M)]−b_n≤H−b_n.                          (4)

In particular all the expectations on the left are finite; no initial
integrability assumption on 1/K_(Y_m) is needed. Taking increasing
limits of the nonnegative partial sums proves

E_n[Σ_{m≥0}1/K_(Y_m)]≤(H−b_n)/c.                   (5)

Independence of the Z_m from the chain and their unit means give
E_n[Z_m/K_(Y_m)]=E_n[1/K_(Y_m)]. Applying the same nonnegative-limit
rule to the lifetime series and using (5) proves its expected bound
in (1). A nonnegative extended random variable with finite expectation
is finite almost surely: otherwise E[T]≥R P(T=∞) for every R>0
would force infinite expectation. This completes (1).

For the contrapositive conclusion, fix any permitted heights. If no
vanishing subsequence existed, the nonnegative finite sequence E_n
would have a strictly positive lower limit, possibly infinite. Thus
some ε>0 would be an eventual lower bound. Assertion (1) would give
P_n(T=∞)=0 at every sufficiently large starting index, contradicting
the stated coordinate-only condition. Hence liminf E_n=0. Recursively
choosing n_l>n_(l−1) with E_(n_l)<1/l gives the required subsequence.
The chosen indices may depend on the heights. ∎

## Qualifications

This is a scoped reduction, not a proof that the coordinate-only
condition always holds. Reciprocal-square summability ensures each
individual jump rate K_n is finite; that fact alone does not establish
infinite lifetime for a chain whose rates change after every jump.
No claim of nonexplosion under the present coordinate hypotheses is
made. Conversely, explosion does not itself construct increasing bounded
heights with an eventual positive *nonlinear* upward contribution:
(3) is a one-way inequality. Thus neither direction of the original
unrestricted height-dependent question is settled here. There is no
RH or theta-specific conclusion.

## Verification and formalization obligations

The proof is analytic; no numerical certificate is required. Audit
positivity and finiteness of the rates, normalization of every transition
row, strict index increase, the reflected-tail choice of N, the factor
c=ε/4, and the direction of the discarded-denominator inequality.
All infinite expectation operations use nonnegative increasing limits;
telescoping is performed only for finitely many bounded height increments.
Formalization would require countable transition sampling on a product
probability space, independent mean-one exponentials, the conditional
expectation identity, monotone convergence, and the subsequence criterion.
Lemma 106 is the sole earlier mathematical input.
