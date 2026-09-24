# Lemma 229: large-divisor tail for the paired cell discrepancy

**Hypotheses.** Use L228's interior box, scales, wholly contained cells,
weights and discrepancy P. For a real cutoff 1<=D<=6N/5 define

P_{>D}=sum_(a,c,d) (phi(a)/a) sum_(b in D(a,c,d))
                         sum_(e|a, e>D) mu(e) r_e(b).

Here D(a,c,d) denotes L228's interval of b, distinct from the scalar
cutoff D. All assertions are for sufficiently large N with fixed scale
constants, h comparable to N^(3/2), and R comparable to h.

**Conclusion.** For every epsilon>0,

|P_{>D}| <= C_epsilon [N^(2+epsilon) h/D
                              +N^(2+epsilon) log(2N)].             (1)

In particular, for any fixed 0<delta<1, the choice D=N^delta gives
P_{>D}=o(B_0). Thus, with this cutoff, P=o(B_0) is equivalent to
P_{<=D}=o(B_0). The latter estimate is not proved.

**Proof.**

Let n_e(b) count multiples of e strictly between alpha(b) and beta(b),
and put ell(b)=beta(b)-alpha(b). The exact endpoint identity in L228 is

r_e(b)=n_e(b)-ell(b)/e.                                  (2)

This retains the signed difference and the strict upper-endpoint atom.
As ell>0 and the weight phi(a)/a is at most one, finite triangle
inequalities applied after (2) give |P_{>D}|<=U+V, where

U=sum_(a,c,d,b) sum_(e|a,e>D) n_e(b),
V=sum_(a,c,d,b) ell(b) sum_(e|a,e>D) 1/e.

Dropping |mu(e)| only enlarges these nonnegative quantities.

We first bound U by reversing its finite sums. Any counted multiple m
lies in J and satisfies e|a and e|m. The strict cell inequalities imply

(m²-R+1)/a-b < bcd < (m²+R)/a.

Since N<=b<=2N, every such positive integer product t=bcd lies in

((m²-R+1)/a-2N, (m²+R)/a),                              (3)

an interval of length 2N+(2R-1)/a=O(N). Also t=O(N³) from the
factor box. For fixed a,m each t has at most tau_3(t) ordered positive
factorizations into b,c,d; box restrictions can only reduce this count.

For completeness, for any eta>0 one has tau_3(t)<=C_eta t^eta.
Unique prime factorization gives

tau_3(t)=product_(p^k || t) (k+1)(k+2)/2.

The local factor is at most 3^k for k>=0, by induction (successive
ratios are (k+3)/(k+1)<=3). For p>=3^(1/eta) it is therefore at most
p^(eta k). For each of the finitely many smaller primes the supremum
of (k+1)(k+2)/(2p^(eta k)) over k>=0 is finite, since exponential
growth dominates a quadratic. Multiplying these finitely many suprema
proves the claim. Taking eta=epsilon/3, (3) consequently allows at
most C_epsilon N^(1+epsilon) ordered triples for each a,m.

For fixed e<=6N/5, the number of a in A divisible by e is O(N/e):
the interval count is O(N/e+1), and N/e>=5/6. The number of m in
J divisible by e is O(h/e+1). Hence the number of (e,a,m) at issue is
at most

C sum_(D<e<=6N/5) (N/e)(h/e+1)
 <= C [Nh/D+N log(2N)].                                 (4)

Here the integer reciprocal-square tail is O(1/D) for all real D>=1,
and the harmonic sum is O(log(2N)). Multiple counting of a pair a,m
by different e is intentional: U contains exactly that multiplicity.
Combining the product bound and (4) proves

U<=C_epsilon [N^(2+epsilon)h/D+N^(2+epsilon)log(2N)].

For V, L228 supplies ell<3/4 and O(h/N+1)=O(h/N) integers b per
triple. There are O(N²) pairs c,d, so

V<=C Nh sum_(a in A) sum_(e|a,e>D) 1/e
 <=C Nh sum_(D<e<=6N/5) N/e²
 <=C N²h/D.

This is absorbed in (1). No fractional-part distribution estimate or
cancellation among the Möbius coefficients was used.

Finally L227 gives B_0>=cN²h/log N. With D=N^delta choose
0<epsilon<min(delta,3/2). Dividing (1) by this lower bound gives

|P_{>D}|/B_0 <= C_epsilon [N^(epsilon-delta)log N
                                  +N^(epsilon-3/2)(log(2N))²],

which tends to zero. The finite identity P=P_{<=D}+P_{>D} proves
the equivalence claimed. A cutoff above 6N/5 has empty tail trivially.

## Qualifications, verification

This proves a growing divisor cutoff is permitted; it does not estimate
the remaining small-divisor phases. It gives no fixed-cutoff limiting
assertion. Other progression estimates, the signed comparison and RH
remain unresolved. The product count is deliberately an upper bound;
it does not assert uniform distribution of products or coprime integers.

Analytic verification covers strict endpoint algebra, finite reindexing,
the elementary divisor estimate and the two tail sums. The exact finite
checks in `scripts/heat/check_large_divisor_cell_tail.py` verify the
product-interval enlargement and counting multiplicities, including
strict endpoint exclusions. They do not prove an asymptotic estimate.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
