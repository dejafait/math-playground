# Lemma 123: nonexplosion for arbitrary summable coordinates

**Hypotheses.** Let 0<x_1<x_2<⋯ with Σ_i x_i^(-2)<∞. Use the
forward-jump process of Lemma 107: q_ij=(x_j−x_i)^(-2) for j>i,
K_i=Σ_(j>i)q_ij, embedded chain Y_m, independent mean-one exponential
variables Z_m, and lifetime T=Σ_(m≥0)Z_m/K_(Y_m).

**Conclusion.** For every starting index n, P_n(T=∞)=1. For every
strictly increasing positive bounded height sequence b_i, the full
upward contributions E_i of the paired product defined in Lemma 107
satisfy liminf_i E_i=0. Thus there are increasing indices i_r with
E_(i_r)→0. These indices may depend on the heights.

## Proof

Summability and monotonicity imply x_i→∞. For each fixed i, there
are only finitely many j with x_j<2x_i, each having positive distance
from x_i; all other q_ij are at most 4/x_j². Hence 0<K_i<∞,
without a uniform bound or a minimum-gap assumption. Lemma 107's
holding-time construction is therefore defined from every index.

Lemma 122 gives a positive strictly increasing unbounded payoff f on
the indices with

Σ_(j>i)q_ij(f(j)−f(i))≤B<∞ for every i.                 (1)

Fix n and an integer R>n. On the original holding-time probability
space set

M_R=min{m≥0:Y_m≥R},
τ_R=Σ_(m=0)^(M_R−1) Z_m/K_(Y_m).

Since Y_0=n and Y_(m+1)>Y_m, 1≤M_R≤R−n. Thus τ_R is finite
almost surely. Collapse every destination j≥R into one absorbing
state ∂, obtaining a finite-state chain on {n,…,R−1,∂}. Its rates
from i<R to j<R are q_ij for j>i, and its rate to ∂ is the full
sum Σ_(j≥R)q_ij. These are finite, and their sum is exactly K_i.
The holding times and the probabilities of all transient destinations
and of exit therefore agree with the original process until τ_R.
This construction uses only finitely many jumps before exit and makes
no prior assumption of nonexplosion for the original process.

Give this finite chain payoff g_R(i)=f(i) on transient states and
g_R(∂)=f(R). Since f is increasing, f(R)≤f(j) for every exit
destination. Its generator consequently satisfies

Q_R g_R(i)
 =Σ_(i<j<R)q_ij(f(j)−f(i))
  +Σ_(j≥R)q_ij(f(R)−f(i))≤B,                         (2)

and Q_R g_R(∂)=0. The inequality compares nonnegative series with
(1); it does not omit any exit rates. All values of g_R are finite.

Apply the finite-state expectation identity justified in Lemma 108
(the identity itself requires only a finite rate matrix, not that
lemma's power-gap hypotheses). For every finite t≥0,

E_n[g_R(X_t)]=f(n)+∫_0^t E_n[Q_R g_R(X_s)] ds
             ≤f(n)+Bt.

The integrand is bounded for this fixed finite matrix; neither a
uniform bound on K_i as R varies nor an infinite-state expectation
identity is used. Positivity of g_R and absorption at exit yield

P_n(τ_R≤t)≤(f(n)+Bt)/f(R).                            (3)

On the original probability space M_R is nondecreasing in R and tends
to infinity: for each fixed m, the finitely many visited indices
Y_0,…,Y_m are finite, so R above their maximum has M_R>m.
Thus τ_R increases to exactly the nonnegative series T. This is a
pathwise statement, valid also when that series is finite. In particular
{T≤t}⊆{τ_R≤t}. Since f(R)→∞, (3) proves P_n(T≤t)=0.
Taking the union over positive integer t gives P_n(T<∞)=0. The
starting index n was arbitrary.

For any fixed permitted heights, apply the final implication of Lemma
107. Its coordinate condition now holds at every starting index. To
make the tail argument explicit, if E_i had no vanishing subsequence,
its nonnegativity would give E_i≥ε>0 eventually. The reflected part
is bounded by 2HΣ_(j>i)x_j^(-2)→0, with H=lim b_i. Lemma 107 then
bounds the expected lifetime from every sufficiently large n by
4(H−b_n)/ε<∞, contradicting the almost-sure infinite lifetime just
proved. Thus liminf E_i=0, and successive indices with E_(i_r)<1/r
supply the conclusion. All contribution sums and the reflected-tail
bound here are those already justified in Lemma 107. ∎

## Qualifications and verification

This proves the arbitrary-coordinate stochastic and height-dependent
selection statements under reciprocal-square summability. It gives
neither a subsequence common to all heights nor a quantitative rate.
The heights must increase with the coordinates as stated; arbitrary
bounded assignments of heights to zeros are not covered. No uniform
heat-parameter control, whole-plane zero continuation, or RH conclusion
is asserted.

The proof is analytic and requires no numerical certificate. The audit
checks fixed-row tail finiteness, complete exit-rate retention, finite
cutoff coupling, the direction of payoff capping, and pathwise stopped
sum convergence before taking probabilities. The only earlier proof
inputs are the payoff from Lemma 122, the finite-state expectation
identity from Lemma 108, and the process and selection implication from
Lemma 107. Formalization would require those statements, finite-state
absorption coupling, nonnegative series limits, and countable unions of
null events. No stopping identity at an unknown explosion time is used.
