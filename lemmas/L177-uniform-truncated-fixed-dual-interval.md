# Lemma 177: uniform truncated fixed dual interval

**Hypotheses.** Use T, N, h, B, E_B and P_y from L174, and a and e
from L175. For each real N≤y≤2N define, with integer indices and closed
endpoints,

D_y(t)=Σ_(a/y≤k≤a/N) (sqrt(a)/k)e(−a log(k/N)),
Q_y(t)=Σ_(2N²/y≤k≤2N) (sqrt(a)/k)e(−a log(k/N)),
c(t)=e(a log(a/N²)−a−1/8).

**Conclusion.** Uniformly in y and t∈B,

P_y(t)=c(t)D_y(t)+O(log(2N)).                         (1)

Moreover, uniformly in y,

E_B|D_y−Q_y|²=O(sqrt(N)),
E_B|P_y−cQ_y|=O(N^(1/4)+log(2N))=o(sqrt(N)).          (2)

Consequently sup_y E_B|P_y|=o(sqrt(N)) if and only if
sup_y E_B|Q_y|=o(sqrt(N)). Neither decay assertion is proved here.
The supremum is outside the expectation; no estimate for an expectation
of a supremum, or for t-dependent choices of y, is asserted.

**Proof.**

For y>N, repeat L175's transform on [N,y]. The standard C^4 B-process
in foundations permits M≥y−N, so choose M=N and Q=a exactly as there.
On this entire interval the second derivative of −a log(x/N) is
comparable to a/N², and the next two derivatives are O(a/N³) and
O(a/N⁴). The derivative range has length a(1/N−1/y)≤a/(2N).
Thus the error is O(N/sqrt(a)+log(2+a/(2N)))=O(log(2N)),
with constants independent of y. Conjugation gives x_k=a/k and
phase a log(a/(kN))−a−1/8, proving (1). Any endpoint-convention
changes cost O(1): a primal term has modulus one, and a dual endpoint
amplitude is at most y/sqrt(a)=O(1). For y=N both sums have at most
one term of bounded modulus, so (1) also holds in that degenerate case.

Set δ=2N²−a and W=(h/(2π)+1/4)/N as in L176. Uniformly in B,
0<δ≤h/(2π)+1/4 and W=O(sqrt(N)). Write C_y=2N²/y, and define

S_y(t)=Σ_(a/y≤k<C_y) (sqrt(a)/k)e(−a log(k/N)),
S_+(t)=Σ_(a/N<k≤2N) (sqrt(a)/k)e(−a log(k/N)).

The exact identity D_y−Q_y=S_y−S_+ holds even when the strips
overlap. Indeed put A=a/y, B_0=a/N, C=C_y, D=2N. Then A≤B_0,
C≤D, A≤C and B_0≤D. On the real line,

1_[A,B_0]−1_[C,D]=1_[A,C)−1_(B_0,D].                (3)

To check all endpoint cases at once, express a closed interval indicator
as 1_(k≥A)−1_(k>B_0), and use the corresponding two differences for
the half-open strips. Subtraction gives (3), including A=B_0 or C=D.
In particular no lower bound on y−N is needed.

The first strip is contained in [C_y−W,C_y); the second in
(2N−W,2N]. Each has at most K=ceil(W)+2 possible integers, all
in [N/2,2N] for large N, since N≤C_y≤2N. Fix y before integrating.
For each possible index in S_y the moving condition is a(t)≤yk;
for S_+ it is a(t)<Nk. Both are thresholds in the increasing function
a(t). Each pair of indicators therefore restricts integration to an
interval J⊆B, possibly empty. Strict endpoints have measure zero.

The square-expansion argument of L176 now applies with the same
constants for every y. Explicitly the diagonal is at most CK after
normalization. Off the diagonal, a(t)/(kl) has supremum and total
variation O(1) on J. Integration by parts bounds the integral of

[a(t)/(kl)] exp(−i(t−π/2)log(k/l))

by C/|log(k/l)|≤CN/|k−l|. At each positive integer difference d
there are at most K pairs in a supporting interval, and d≤K.
For either strip S this proves

E_B|S|²≤C[K+NK log(2K)/h]=O(sqrt(N)),

because h is comparable to N^(3/2). The constants use only the stated
support widths, not C_y or y−N. Equation (3) and
|S_y−S_+|²≤2|S_y|²+2|S_+|² prove the first estimate in (2).
Cauchy–Schwarz gives E_B|D_y−Q_y|=O(N^(1/4)); (1) and |c|=1
then prove the second estimate. Finally

|E_B|P_y|−E_B|Q_y||≤E_B|P_y−cQ_y|

uniformly in y. Taking suprema outside the integrals and dividing by
sqrt(N) proves the equivalence. ∎

## Scope, verification, and formalization obligations

The result extends both operations to all fixed primal truncations,
including arbitrarily short intervals. It supplies the uniform error
needed to transfer the partial-sum first-moment question to fixed dual
intervals. It does not establish decay, uniform integrability, cutoff
covariance or RH; the overall argument is unchanged.

Analytic verification checks the transform's interval-length hypothesis,
uniform derivatives, degenerate interval, endpoint amplitudes, the signed
indicator identity in overlapping and disjoint cases, threshold pair
supports, coefficient variation and harmonic summation. No numerical
certificate is needed. Formalization would require this uniform version
of the C^4 input, (3), finite square integration and the supremum inequality.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
