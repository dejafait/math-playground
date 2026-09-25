# L008 — Fixed-exponent lower bounds and the missing uniform join

## Hypotheses

Use c_L(n), SIZE(n^k), and Sigma_2^P from the [fixed-exponent theorem note](../foundations/03-kannan-fixed-exponent-theorem.md), and the no-free-constants circuit convention of L006. All circuit claims concern positive input lengths. Logarithms have base two.

For each integer r>=8, let T_r be the lexicographically first r-variable truth table with minimum circuit size greater than 2^r/(32r). L006 ensures that such a table exists. For k>=1 and n>=1 put

    r(k,n) = (k+1) ceil(log_2 n).

Define H_k on n-bit strings as follows. If 8<=r(k,n)<=n, apply the function represented by T_{r(k,n)} to the first r(k,n) input bits, ignoring the others. At every other length, and on the empty string, reject.

For any sequence of languages (A_k)_{k>=1}, define its unary-tagged join

    J_A = {1^k 0 x : k>=1 and x in A_k}.

The first zero terminates the tag; strings without such a tag are rejected. No effective selection of a general sequence (A_k) is assumed.

## Conclusion

1. Under the temporary assumption P=NP, Kannan's theorem implies that for every k there is K_k in P but outside SIZE(n^k). Each such K_k still belongs to P/poly, with a polynomial bound depending on k. This gives no single fixed NP language outside P/poly.
2. There is an actual decidable witness family for the quantifier distinction: each H_k is in SIZE(n^(k+2)), yet

       c_H_k(n) / n^k -> infinity as n -> infinity.

   Thus the class {H_k : k>=1} is contained in P/poly but is not contained in SIZE(n^d) for any fixed d. No NP membership of H_k is asserted.
3. If A_k is outside SIZE(n^k) for every k, then J_A is outside P/poly. Consequently a uniform NP verifier for the joined Kannan witnesses would suffice for P!=NP. Such a verifier is not supplied by the individual Sigma_2^P memberships, or by their conditional P memberships under P=NP.

The second assertion is a concrete counterexample to interchanging the language and exponent quantifiers. It is not a claim about formal independence of P=NP from other complexity theorems. The third assertion isolates a missing membership input, rather than establishing it.

## Proof

**Eliminating the two quantifiers under P=NP.** P is closed under complement, by exchanging the accepting and rejecting states of a total deterministic decider. Hence P=NP implies coNP=P. Fix any L in Sigma_2^P and its predicate R and polynomial p. The language of well-formed pairs (x,y) with |y|=p(|x|) for which

    for every z in {0,1}^{p(|x|)}, R(x,y,z)=1

belongs to coNP: a failing z certifies its complement, and malformed pairs can be checked deterministically. Under the temporary assumption, that pair language has a polynomial-time decider. Existentially guessing y and running that decider places L in NP, hence in P. Every bound here is fixed once L is fixed, but may depend on L. This proves Sigma_2^P=P under P=NP without any quantitative uniform bound over languages.

Apply the standard Kannan theorem separately at each k. The resulting K_k lies in P under the assumption, but remains outside SIZE(n^k). The computation-to-circuit simulation in the [standard-results note](../foundations/02-standard-results.md) gives K_k in SIZE(n^{d_k}) for some integer d_k. Necessarily d_k>k, since SIZE(n^d) is contained in SIZE(n^k) when d<=k. There is no contradiction in these exponent-dependent conclusions. In quantifier order, the available statement is

    for every k there is K_k in P with K_k not in SIZE(n^k),

whereas the sufficient circuit target is

    there is one L in NP such that for every k, L not in SIZE(n^k).

The common language in the latter is not provided by the former. The next construction verifies that the distinction is substantive even for actual decidable languages and ordinary Boolean circuits.

**A fixed-exponent family inside P/poly.** For fixed k and all sufficiently large n, r=r(k,n) satisfies 8<=r<=n, because log n tends to infinity but log n/n tends to zero. Put N=2^r. The integer rounding gives

    n^(k+1) <= N <= 2^(k+1) n^(k+1),
    r <= (k+1)(log_2 n+1).

L006 supplies T_r with c(T_r)>N/(32r) and the universal upper bound c(T_r)<=2rN. Its existence does not require an efficient table-construction algorithm.

An r-input circuit for T_r can be used on n inputs by ignoring the last n-r bits. Therefore

    c_H_k(n) <= 2rN
              <= 2^(k+2)(k+1)(log_2 n+1)n^(k+1)
              = O_k(n^(k+2)).

The finitely many exceptional lengths use the constant-zero function, which requires at most two gates when there is at least one input bit. They can be absorbed in the constant, proving H_k in SIZE(n^(k+2)).

Conversely, given any n-input circuit for H_k, fix its last n-r inputs to zero. This produces an r-input circuit for T_r. To respect the absence of free constants, create NOT(x_1), x_1 AND NOT(x_1), and x_1 OR NOT(x_1) as needed; three gates suffice for both constant values. The remaining free input x_1 exists since r>=8. The restricted circuit has at most c_H_k(n)+3 gates, so

    c_H_k(n) > N/(32r)-3,
    c_H_k(n)/n^k > n/[32(k+1)(log_2 n+1)] - 3/n^k -> infinity.

This excludes every constant multiple of n^k, not merely the unit coefficient. Replacing n^k by (n+1)^k changes the ratio by a factor tending to one, so H_k is outside SIZE(n^k) under the precise convention used here. For any fixed d, choosing k=d shows that the class of all H_k is not contained in SIZE(n^d), although each member has a polynomial circuit family.

The languages are decidable: when the length test succeeds, enumerate the finitely many r-variable truth tables in lexicographic order, enumerate every circuit with at most floor(2^r/(32r)) gates, and test each candidate table against their full truth tables. The first table not realized is T_r, and L006 guarantees termination. This describes a finite uniform computation even when k is supplied as a parameter. It does not give a polynomial-time algorithm or an NP verifier; nor is its enumeration cost a lower bound on other algorithms. Decidability is included to avoid relying on arbitrary noncomputable choices for this example.

**A short tag preserves all the lower bounds.** Suppose every A_k is outside SIZE(n^k), but J_A has circuits of at most B(m+1)^d gates at input length m, for fixed B>=1 and a positive integer d. Choose a fixed integer k>=d. For an n-bit input to A_k, use the circuit for J_A at length m=n+k+1 and hardwire the first k+1 bits to 1^k 0. The circuit is allowed to depend on k and n. Adding at most three gates to supply both constants gives

    c_A_k(n) <= B(n+k+2)^d+3
             <= (B(k+2)^d+3) (n+1)^d,

for every n>=1. With k fixed the coefficient is a constant. Hence A_k is in SIZE(n^d), and therefore in SIZE(n^k), contradicting the hypothesis. This proves J_A is outside P/poly. It applies both to the H_k example and to any choice of Kannan witnesses.

For the latter join, one would still have to exhibit a single verifier V and a single polynomial p in the full length m=k+1+|x|, with witnesses of length at most p(m), working uniformly over every k and x. Separate verifiers or deciders for fixed k, whose exponents depend on k, do not establish that assertion. Even an effective way to obtain their descriptions supplies no common time bound. In fact, under P=NP the joined Kannan language cannot be in NP: otherwise it would be in P and thus in P/poly, contrary to the proved join lower bound. This conditional exclusion is not an unconditional separation or a proof that the join lies outside NP in the actual unrelativized setting.

**Required versus achieved bound and route decision.** The imported theorem defeats each fixed circuit exponent with a possibly different Sigma_2^P language. The join defeats all polynomial circuit bounds, but lacks NP membership. Under P=NP, each separate witness has both a fixed-exponent lower bound and an exponent-dependent polynomial upper bound; the explicit H_k family demonstrates that this bound pattern alone is entirely compatible with P/poly containment. Stop the direct inference from Kannan plus collapse to a contradiction. A repair must supply new control of a combined language's membership and full input length, not interchange quantifiers. No complete P-versus-NP candidate has been obtained.

## Mathlib

Coverage: **not checked** for the full statement or supporting circuit restriction, class collapse, tagged join, and asymptotic results. No matching Mathlib theorem, supporting Mathlib identifier, or absence claim is asserted. The external Kannan reference in the foundation note matches the fixed-exponent input only. The family construction, restriction estimates, collapse argument, and join proof are supplied above.
