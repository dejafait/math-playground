# Exact target and conventions

Source audit: 2026-09-24; statement reconfirmed 2026-09-25. The [Clay Mathematics Institute problem page](https://www.claymath.org/millennium/p-vs-np/) currently labels the problem unsolved and links Stephen Cook's [official description, §1, pp. 1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf). Its target is equality of deterministic and nondeterministic polynomial-time language classes. The notebook uses the equivalent certificate definition below. Historical algorithmic records in that older description are not treated as current records.

All languages are subsets of {0,1}*. Input length means the full binary description length, including indices, clocks, and padding. Deterministic machines must halt on every input. Changing between standard finite-tape Turing-machine conventions only changes polynomial overhead.

- P consists of languages decided by one deterministic machine in time at most C(n+1)^k for fixed constants C and k.
- NP consists of languages L for which one deterministic polynomial-time verifier V and one polynomial p satisfy x ∈ L iff there exists y with |y| ≤ p(|x|) and V(x,y) = 1. The bounds and verifier are fixed for the entire language.
- EXPTIME (also written EXP) consists of languages decided deterministically in time at most 2^p(n) for some fixed polynomial p. Multiplicative constants and polynomial tape-simulation overhead can be absorbed by enlarging p. A polynomial-time many-one reduction from A to B is a total polynomial-time function f with x ∈ A iff f(x) ∈ B; in particular, |f(x)| is bounded by one polynomial in |x|. Completeness for EXPTIME means membership in EXPTIME and such a reduction from every language in EXPTIME.
- SAT is the language of well-formed satisfiable Boolean CNF formulas under an ordinary explicit binary encoding; malformed strings are rejected. Width at most three defines 3-CNF here. Repeated literals can pad shorter clauses if a three-literal convention is needed.
- A circuit has fan-in-two AND/OR gates, fan-in-one NOT gates, unrestricted fan-out and depth, and one output. Size is the number of non-input gates. P/poly means existence of polynomial-size circuits for each input length, without an algorithm required to construct them.

The exact goal is to decide P = NP. A separation requires one fixed language in NP with no deterministic polynomial-time decider. For a negative answer it suffices to show SAT ∉ P; for a positive answer it suffices to show SAT ∈ P. A general-circuit lower bound showing SAT ∉ P/poly would be a stronger sufficient result, not an equivalent target asserted here.

For that circuit route the required quantifiers are: for every constants C,k, some length N has minimum SAT circuit size greater than C(N+1)^k. A bound for one fixed exponent, one input size, one algorithm, one variable order, or a restricted circuit basis with additional restrictions does not suffice. Circuit lower bounds on arbitrary Boolean functions do not by themselves produce a fixed NP language.

## Mathlib

Coverage: **not checked** for these complexity-class definitions or the exact target. No matching theorem or absence claim is asserted.
