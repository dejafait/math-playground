# Lemma 226: negligible transition weight loss

**Hypotheses.** Use L225's candidate set and strict occupancy indicator,
L220's rounded endpoints, and the interior box and scales of L221.
Use S,T from L223. All sums below run over the same a,c,d box and
b in Bset. Write m=k_b and let I_b be one when m is in J,
gcd(a,m)=1 and theta_b<ell_b, and zero otherwise. When I_b=1 set
H_m=(B_m-A_m)/R. Define

Z_full=sum_(a,c,d) (phi(a)/a) sum_(b: I_b=1) H_(k_b),
E_full=Z_full-T.

**Conclusion.** For every epsilon>0, the number of selected candidates
with W_b<H_(k_b) is O_epsilon(N^(3+epsilon)). Moreover

0 <= E_full-S <= O_epsilon(N^(3+epsilon)).                 (1)

In particular E_full-S=o(T), and S=o(T) if and only if
E_full=o(T). The full height retains the exact rounded endpoints
and the gcd selection. No estimate E_full=o(T) is asserted.

**Proof.**

Fix a selected candidate and put v=cd, m=k_b. L221 and L220 give
-R<=A_m<B_m<=R, hence 0<H_m<=2. By L225 the overlap weight is

W_b=R^(-1)[min(B_m,U)-max(A_m,L)]_+,
L=avb-m², U=a(v+1)b-m²-1.

Here U-L=ab-1>0. If L<=A_m and U>=B_m then W_b=H_m.
Consequently W_b<H_m implies L>A_m or U<B_m, including
cases of zero overlap. Strict occupancy gives

avb-R<m²<a(v+1)b+R-1.

If L>A_m, these inequalities imply -R<L<R, so
|abcd-m²|<=R+1. If U<B_m, they imply -R<U<R, so
|ab(cd+1)-m²|<=R+1. Every deficient selected candidate thus
belongs to at least one of these two near-square product families.
This deduction retains gcd(a,m)=1. We may discard that restriction
only to upper bound the cardinality of these nonnegative families.

We give the elementary divisor estimate used to count them. For each
eta>0, tau(n)<=C_eta n^eta for positive integers n. Indeed for
primes p>=2^(1/eta) and integers e>=1, e+1<=2^e<=p^(eta e).
For each of the finitely many smaller primes the supremum of
(e+1)/p^(eta e) over e>=0 is finite. Multiplying these bounds
in the prime factorization proves the assertion. In particular any
fixed product of divisor counts of integers O(N^4) is
O_epsilon(N^epsilon), by choosing eta sufficiently small.

There are O(h+1) possible integers m in J and O(R+1) possible
integers n with |n-m²|<=R+1. All these n are positive and O(N^4)
eventually. For fixed n the number of ordered positive solutions
abcd=n is at most tau(n)^3: choose a|n, b|(n/a), c|(n/(ab));
d is determined and divisor counts of divisors are at most tau(n).
For ab(cd+1)=n, choose a|n, b|(n/a), then t=n/(ab).
When t>=2 there are tau(t-1) possibilities for c,d; when t=1
there are none. The total is at most

tau(n)^2 max_(1<=u<=n) tau(u)=O_epsilon(N^epsilon).

These unrestricted counts bound the counts inside the box as well.
Thus the union of the two families has size
O_epsilon((h+1)(R+1)N^epsilon)=O_epsilon(N^(3+epsilon)).
Counting tuples (a,b,c,d,m) can only overcount the selected candidates.
Each loss H_m-W_b is between zero and two, and phi(a)/a<=1.
L225 identifies S with the aggregate selected overlap minus T,
so subtraction proves (1). Finally L223 gives
T>=cN²h/log N, with h comparable to N^(3/2). Taking, for
example, epsilon=1/4 bounds (E_full-S)/T by
O(N^(-1/4)log N), which tends to zero. The equivalence follows.

## Qualifications and verification

Only selected candidates are assigned full height. Candidates outside J,
with failed gcd, or with an unoccupied strict cell remain zero. Full
height can depend on m; neither equidistribution nor independence from
the gcd or candidate phase is used. The real benchmark remains T.
Other progression terms, the signed comparison and RH remain unresolved.

Analytic verification consists of the two endpoint implications, positive
integer factorization counting and the comparison to L223's lower bound.
`python3 scripts/heat/check_transition_weight_loss.py` checks the endpoint
implications and nonnegative replacement loss on exact finite fixtures;
it is not evidence for a distributional estimate. Formalization would
require those inequalities, the elementary divisor bound, finite counting
and the eventual power-versus-logarithm limit.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
