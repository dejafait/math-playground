# Kannan's fixed-exponent circuit lower bound

## Hypotheses

Use the language and bounded-fan-in AND/OR/NOT circuit conventions in [the model note](01-model-and-target.md). For a language L and n>=1, let c_L(n) be the minimum number of non-input gates computing membership in L on n-bit inputs. Define

    SIZE(n^k) = {L : there is C>=1 with c_L(n)<=C(n+1)^k for every n>=1}.

Allowing finitely many exceptional positive lengths gives the same class: enlarge C to cover their finite circuit complexities. Thus P/poly is the union of SIZE(n^k) over positive integers k, with the exponent depending on the language. The empty input has no effect on these asymptotic classes.

A language belongs to Sigma_2^P if there are a fixed polynomial p and a deterministic polynomial-time predicate R such that

    x in L iff exists y in {0,1}^{p(|x|)} for every z in {0,1}^{p(|x|)} R(x,y,z)=1.

Different polynomial bounds for the two strings can be equalized by padding. The polynomial and predicate may depend on L. Pi_2^P is the class of complements of Sigma_2^P languages.

## Conclusion

The following form of the standard **Kannan circuit lower-bound theorem** suffices here:

    For every fixed positive integer k,
    there is a language K_k in Sigma_2^P with K_k not in SIZE(n^k).

The theorem does not state that one K_k works for every k, or give a common polynomial resource bound for all witnesses.

## Proof

This is a named standard input, not a new lower-bound proof. The original reference is Ravi Kannan, [*Circuit-Size Lower Bounds and Non-Reducibility to Sparse Sets*, Information and Control 55 (1982), 40–56, DOI 10.1016/S0019-9958(82)90382-5](https://doi.org/10.1016/S0019-9958%2882%2990382-5). Its publisher page was not retrievable in this audit; no original theorem number or inspected original proof is claimed.

An inspected precise statement is Fortnow–Santhanam–Williams, [*Fixed-Polynomial Size Circuit Bounds*, CCC 2009, §II.A and §III, Theorem 8, PDF pp. 2–3](https://www.cs.cmu.edu/~ryanw/circuit.pdf). Their SIZE definition uses O bounds, and Theorem 8 attributes the displayed result to Kannan. Replacing n by n+1 does not change that definition for n>=1. Constant-factor changes of a fixed finite complete circuit basis likewise preserve SIZE classes; the theorem concerns unrestricted Boolean circuits, not a depth-restricted model.

For scope, Cai–Watanabe, [*On Proving Circuit Lower Bounds Against the Polynomial-time Hierarchy: Positive and Negative Results*, report C-256, §1, printed pp. 1–2](https://www.is.c.titech.ac.jp/report-c/C-256.pdf), describes Kannan's stronger intersection-class version and gives a constructive Sigma_2^P variant in Theorem 1. The displayed Kannan statement is sufficient for the original quantifier argument. The following quantitative input is also retained for the padding test. Sources checked 2026-09-25.

**Constructive quantitative input.** Cai–Watanabe, Theorem 1, printed p. 2, constructs, for each integer j>=2, an existential-then-universal machine M_j of branch time

    O_j(n^(j^2) (log_2 n)^(j+1))

whose language A_j has no n^j-size circuit family. Their size counts wires (Preliminaries, printed p. 3); the proof in §2, printed pp. 3–5, supplies arbitrarily large hard lengths. Only this infinitely-often lower-bound use is needed here. The construction gives an effective algorithm from j to M_j, without a common polynomial bound in j and n.

A circuit with s gates in the notebook's bounded-fan-in basis has at most 2s+1 wires, including a possible output wire. Consequently, at those hard lengths, c_A_j(n)>(n^j-1)/2, and hence c_A_j(n)>=n^j/4 for all sufficiently large such n. This conversion uses only circuits in the notebook's basis, regardless of whether the source allows additional fan-in. No exclusion of every constant multiple of n^j is inferred from a unit-coefficient statement. Instead, for each k>=1, choosing j=k+1 gives A_j outside SIZE(n^k), since n^j/(4(n+1)^k) tends to infinity along the hard lengths.

The displayed running-time bound is an upper bound for a particular alternating machine, not a lower bound for all algorithms or an NP verification bound. Replace log n by ceil(log_2(n+2)) and enlarge a fixed-j constant to cover small lengths when using a clock.

## Mathlib

Coverage: **not checked** for the full Kannan theorem, the constructive quantitative variant, or supporting polynomial-hierarchy and SIZE definitions. No Mathlib identifier or absence claim is asserted. The named external theorems match their respective fixed-exponent statements; neither matches a single-language superpolynomial lower bound or resolves P versus NP.
