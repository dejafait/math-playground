# L007 — MCSP distinguishes restricted keyed functions, conditional on security

## Hypotheses

Use the circuit conventions in [the model note](../foundations/01-model-and-target.md) and the MCSP_u encoding of L006: an r-variable truth table T of length N=2^r and unary threshold s form the input 1^r 0 T 1^s, of length M=N+r+1+s. There are no free constant gates.

For each integer k>=2 and key K in {0,1}^k, let F_{k,K}:{0,1}^k -> {0,1}. Assume one deterministic evaluator computes F_{k,K}(x) from (1^k,K,x) in time polynomial in k, with one fixed polynomial for all k, K, and x. No security is required for the unconditional implications below.

The optional **pseudorandom-function security premise** is the following. For every uniform probabilistic polynomial-time oracle algorithm D, the advantage

delta_D(k) = |Pr_{K,coins}[D^{F_{k,K}}(1^k)=1] - Pr_{R_k,coins}[D^{R_k}(1^k)=1]|

is negligible in k. Here K is uniform in {0,1}^k, R_k is a uniformly random function from {0,1}^k to {0,1}, and the oracle answers k-bit queries. Query writing is charged to running time. Negligible means that for every positive integer b, delta_D(k)<=k^(-b) for all sufficiently large k. Security quantifies over every fixed polynomial running-time bound, not just one prescribed degree.

## Conclusion

There are fixed positive integers c,d such that every restriction obtained by fixing input bits and the key has a circuit of at most c k^d gates, provided at least one input bit remains free. Put a=d+2 and, for k>=2, define

r(k)=min(k, a ceil(log_2 k)),    N(k)=2^{r(k)},

q_k(z)=z 0^{k-r(k)},    s(k)=floor(N(k)/(32r(k))).

Then N(k)=Theta(k^a), and a deterministic polynomial-time decider for MCSP_u would give a uniform polynomial-time oracle distinguisher D with

delta_D(k) >= 1-2^(-3N(k)/4)

for every sufficiently large k. Thus the security premise implies MCSP_u is not in P; by L006 it is in NP.

The same security premise already implies P!=NP without a lower bound for MCSP. In fact, the fixed language

R_F = {1^k 0 T : k>=2, |T|=N(k), and there exists K in {0,1}^k such that T_z=F_{k,K}(q_k(z)) for every z in {0,1}^{r(k)}}

belongs to NP. A polynomial-time decider for R_F would give a uniform polynomial-time oracle distinguisher with advantage at least 1-2^{k-N(k)}. Consequently security implies R_F is in NP but outside P. These are conditional implications: neither a secure family nor an unconditional separation is established.

## Proof

**Uniform evaluation supplies the circuit upper bound.** Apply the computation-to-circuit simulation proved in [the standard-results note](../foundations/02-standard-results.md) to the fixed evaluator on inputs of total length O(k). Fix its parameter and key inputs, and any chosen function-input bits. The resulting circuits have polynomially many gates in k, uniformly bounded over the values fixed. Their descriptions need not be recovered by the distinguisher; only their existence is used for MCSP acceptance.

To obey the no-free-constants convention, use a remaining free input z_1 to construct NOT(z_1), z_1 AND NOT(z_1), and z_1 OR NOT(z_1). These three gates supply the values zero and one to every fixed wire, using unrestricted fan-out. Substitution adds at most three gates to the circuit before hardwiring. Increasing a fixed integer coefficient and exponent gives a bound c k^d for all k>=2 and all the indicated restrictions, with d>=1. The constants do not depend on the key or on k.

**The table fits a polynomial budget and the threshold covers it.** The formula for r(k) is a uniform integer calculation; the minimum ensures r(k)<=k even at small k, so every query q_k(z) is defined and distinct. For all k>=2,

N(k)<=2^{a ceil(log_2 k)}<=2^a k^a.

Since log_2 k grows more slowly than k, eventually r(k)=a ceil(log_2 k). For these k,

k^a<=N(k)<=2^a k^a,    r(k)<=a(log_2 k+1).

In particular, eventually r(k)>=8 and

[N(k)/(32r(k))]/[c k^d] >= k^2/[32ac(log_2 k+1)] -> infinity.

It follows that s(k)>=c k^d for all sufficiently large k, including the floor in s(k). Thus every restricted keyed table has circuit size at most s(k). The finitely many smaller k need no advantage guarantee.

**The oracle reduction.** Given 1^k and oracle O, query O(q_k(z)) for every z in lexicographic order and concatenate the answers into T. Run the proposed exact MCSP_u decider A on 1^{r(k)} 0 T 1^{s(k)}, and output its acceptance bit. This specifies one deterministic oracle algorithm once the evaluator and A are fixed. The integer a is fixed in its code; there is no advice depending on k or K.

Writing the N(k) oracle queries costs O(kN(k)). The MCSP instance has M=Theta(N(k)), because r(k)<=N(k) and s(k)<=N(k)/32. If A takes time O((M+1)^t) for a fixed t, the construction and its call to A take polynomial time in k; for example the query and decider terms are O(k^{a+1}+k^{at}). Computing the parameters, writing the unary threshold, and storing the table also have polynomial cost. On malformed security-parameter inputs the algorithm can immediately reject. Its behavior for the finitely many smaller k does not affect security's asymptotic quantifiers.

When O=F_{k,K}, the preceding size bound makes A accept for every K, for all sufficiently large k. When O=R_k, the queries are distinct and chosen independently of their answers, so the N(k) answer bits are independent uniform bits. Hence T is exactly uniform in {0,1}^{N(k)}; no approximation or assumption of independence about keyed outputs is used. At r(k)>=8, L006 bounds the fraction of tables of circuit size at most s(k) by 2^(-3N(k)/4). Therefore the difference of the two acceptance probabilities is at least 1-2^(-3N(k)/4), as claimed. It tends to one and so is not negligible. Since the security premise forbids every fixed polynomial-time oracle algorithm, the possibly large but fixed exponents a and at are allowed in this contradiction. Thus a secure family precludes A.

**The security premise already supplies a separation.** Consider R_F as defined in the conclusion, with the evaluator and a fixed once and for all. Parse the unary header and require exactly N(k) remaining table bits. The length and exponent calculation has polynomial cost in the header length, even on malformed inputs; an incorrect table length is rejected before recomputation. Guess a k-bit key K, evaluate F_{k,K}(q_k(z)) on all N(k) points, and compare with T. This verifier has certificate length k and running time polynomial in k+N(k), with one fixed degree. Agreement at every table position proves soundness, and a generating key proves completeness. Thus R_F belongs to NP with no security assumption.

For a fixed k, there are only 2^k keys, so the set of generated tables has size at most 2^k; distinct keys are allowed to generate the same table. A uniform table of length N(k) consequently belongs to this set with probability at most 2^{k-N(k)}. Every table obtained from a keyed oracle belongs to it with probability one.

If R_F were in P, query the same N(k) points and run its decider on 1^k 0 T. This is another uniform polynomial-time oracle algorithm, since k+N(k) is polynomial in k. Its advantage is at least 1-2^{k-N(k)}. The latter tends to one, since N(k)>=k^a eventually and a>=3. This contradicts the security premise. In particular, assuming P=NP would put the NP language R_F in P and cause this contradiction directly. No MCSP algorithm, circuit-counting estimate, or security-to-one-way-function theorem is needed for this paragraph.

**Scope, redundancy, and the required bound.** The first reduction achieves the intended intermediate threshold: the keyed functions fit below s(k), the random false-acceptance probability is exponentially small in the polynomial-length table, and the oracle query cost is polynomial in key length. This is a genuine conditional connection between recognition and pseudorandomness, distinct from a density-only lower-bound inference. It gives no unconditional lower bound for the MCSP predicate: no secure family has been established here. Proving security against all polynomial-time distinguishers would already exclude every polynomial-time decider for the separate NP language R_F. It is not a weaker premise that this argument upgrades to P!=NP, and no converse from P!=NP to security is asserted. In particular, a family proved secure only against a restricted circuit model or a fixed resource exponent would not justify the unrestricted security premise used above.

The qualitative relation between circuit minimization and pseudorandomness is standard; see Kabanets–Cai, [*Circuit Minimization Problem*, technical report dated November 15, 1999, §2.1, “Natural Properties”](https://www2.cs.sfu.ca/~kabanets/papers/mincircuit.pdf). That section's nonuniform strong-generator consequence is related context, not a match for the present uniform security hypothesis and explicit parameters. The oracle-security convention is supported by Goldreich–Goldwasser–Micali, [*How to Construct Random Functions*, JACM 33(4), 792–807 (1986), author's explanatory page](https://www.wisdom.weizmann.ac.il/~/oded/ggm.html). These primary sources were checked 2026-09-25. No generator-existence theorem, factoring assumption, or unrestricted natural-proofs impossibility is imported. The complete implications above are proved directly.

## Mathlib

Coverage: **not checked** for the full statement or for supporting oracle-security, circuit-restriction, range-verification, and asymptotic bounds. No matching Mathlib theorem, supporting Mathlib identifier, or absence claim is asserted. The external references supply context and the security convention, not a full match for this quantitative statement.
