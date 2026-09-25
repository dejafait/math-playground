# L002 — Validating a supplied succinct computation trace is coNP-complete

## Hypotheses

Use the explicit Boolean-circuit and language conventions in [the model note](../foundations/01-model-and-target.md). A circuit with several output bits lists every output wire explicitly; its input ports are also explicit. Constants may be implemented with a constant number of AND/OR/NOT gates if necessary. All reductions are deterministic polynomial-time many-one reductions, measured in full binary description length. Define coNP = {L : the complement of L belongs to NP}.

Fix the following deterministic Turing machine M₀. On a one-symbol input b ∈ {0,1}, it starts with its head at cell 0 in state q_start, leaves b unchanged, moves right once, and enters q_accept. As in the standard simulation convention, extend the transition function at a halting configuration by a stationary self-loop. This extension only pads an already terminated computation; it does not change the accepted language or its running time. Complete unused transitions in any fixed deterministic way.

Let s₀ be the initial configuration on input 0. For b ∈ {0,1}, let h_b have tape symbol b in cell 0, a blank in cell 1, the head at cell 1, and state q_accept. Thus

Next(s₀) = h₀,    Next(h₀) = h₀,    Next(h₁) = h₁.

Encode configurations whose head and nonblank cells lie in the fixed window {0,1}, with blank tape outside it, using a fixed number w of bits. Legal encodings, the transition relation within this window, and the distinct encodings s₀,h₀,h₁ are fixed independently of every instance. Leaving the window is not a transition to a window configuration. The actual computation from s₀ stays in the window.

An instance of VALID₀ consists of an explicitly listed circuit G with ℓ ≥ 3 input bits and w output bits, and an integer T in binary with 1 ≤ T < 2^ℓ. An integer t is supplied to G in exactly ℓ bits, most significant bit first. Let N denote the full instance length, so ℓ ≤ N. The instance belongs to VALID₀ precisely when:

1. G(0) = s₀ and G(T) = h₀;
2. G(t) is a legal configuration encoding for every 0 ≤ t ≤ T;
3. G(t+1) = Next(G(t)) for every 0 ≤ t < T.

Malformed instances are rejected. There is no promise that a supplied circuit describes a genuine run.

## Conclusion

VALID₀ is coNP-complete. Hardness already holds for the subfamily with T = 2^ℓ−1, correct endpoints, and legal configuration encodings at every address. The machine, its input, and configuration width are all fixed, and its actual computation accepts after one step.

Consequently, VALID₀ has a deterministic polynomial-time decider if and only if P = NP. VALID₀ has polynomial-length NP certificates checked in deterministic polynomial time if and only if NP = coNP. These are conditional equivalences, not separations.

The reduction can also produce an invalid trace with exactly two illegal adjacent transitions among T transitions. Accordingly, a test that only samples r independent uniform transition positions detects such an instance with probability at most 2r/T. This last statement concerns uniform local sampling alone, not every possible analysis of the supplied circuit.

## Proof

**Membership in coNP.** The complement of VALID₀ has polynomial-size certificates. Malformed descriptions, invalid parameter ranges, or incorrect endpoints can be checked directly in polynomial time. Otherwise a certificate is either an ℓ-bit address t ≤ T whose output is not a legal encoding, or an ℓ-bit address t < T with G(t+1) ≠ Next(G(t)). Circuit evaluation, binary comparison and addition, and the fixed transition test take polynomial time in N. If none of these failures occurs, all three defining conditions hold. Thus these certificates are sound and complete for the complement, proving VALID₀ ∈ coNP.

**The tautology input.** Let CIRCUIT-TAUT be the language of well-formed circuits F on m ≥ 1 explicitly listed input bits satisfying F(a)=1 for every a ∈ {0,1}^m. Malformed descriptions are rejected. A dummy input makes the restriction m ≥ 1 harmless. CIRCUIT-TAUT belongs to coNP because a falsifying assignment certifies failure, and malformed descriptions are recognizable in polynomial time.

For completeness, take any language A ∈ coNP. Its complement belongs to NP, so the Cook–Levin theorem, recorded in [the standard inputs](../foundations/02-standard-results.md), supplies a polynomial-time map x ↦ φ_x to well-formed CNF formulas such that x is outside A iff φ_x is satisfiable. View φ_x as a polynomial-size circuit and negate its output to obtain F_x. Then x ∈ A iff F_x is a tautology. Relabel the occurring variables consecutively and add a dummy variable if needed; the number of explicitly listed inputs is polynomial in |x|. This proves coNP-hardness of CIRCUIT-TAUT. The use of Cook–Levin is the only external complexity-completeness input here; the full trace reduction follows below. Stephen Cook's [official description, §2, p. 5](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) also states the formula-TAUT counterpart, supporting this input rather than supplying the full result of this lemma.

**A reduction with genuine initial and final configurations.** Given F on m ≥ 1 bits, put ℓ=m+2 and T=2^(m+2)−1. Write a time address as (u,v,a), where u,v are the first two bits and a is the remaining m-bit string. Define

b_F(u,v,a) = (¬u) ∧ v ∧ (¬F(a)),

and let the circuit G_F output

G_F(t) = s₀                 if t=0,
G_F(t) = h_{b_F(t)}         if t>0.

This is an ordinary Boolean circuit. Use one copy of F, a constant number of gates to compute b_F, O(ℓ) gates to recognize the zero address, and a constant number of gates per output bit to select the fixed configuration encoding. Its gate count is size(F)+O(m); listing ports, gates, and binary wire indices gives a description length polynomial in the full description of F. The binary representation of T is ℓ ones, generated without enumerating the T+1 times. Thus F ↦ (G_F,T) is a polynomial-time transformation. An invalid CIRCUIT-TAUT description can be sent to the fixed instance with ℓ=3, T=7, G(0)=s₀, G(2)=G(3)=h₁, and G(t)=h₀ at the other positive addresses. A fixed circuit implements this finite lookup. Its endpoints and encodings are correct but its edge from time 1 to time 2 is illegal. Thus the reduction is total on binary strings and its malformed-input fallback also preserves the stated extra guarantees.

Every G_F(t) is one of s₀,h₀,h₁, hence is a legal encoding. At time 0 the initial override gives s₀, and at time T the prefix is 11, so the final configuration is h₀. The only possible h₁ outputs occur in the interior interval

2^m ≤ t ≤ 2^(m+1)−1,

which is exactly the block of addresses with prefix 01. Since m ≥ 1, this interval starts at least at time 2 and ends before T. Also G_F(1)=h₀, so even the first transition is correct for every F.

If F is a tautology, b_F is identically zero. The trace is s₀ followed by h₀ at every positive time, so every adjacent transition is legal. Hence (G_F,T) ∈ VALID₀.

Conversely, if F(a)=0 for some a, the time t=2^m+value(a) has G_F(t)=h₁. Choose the least time t_* with that output. It satisfies t_* ≥ 2, and G_F(t_*−1)=h₀ by minimality and the form of all positive-time outputs. The edge at t_*−1 is illegal, because Next(h₀)=h₀ ≠ h₁. Hence (G_F,T) is outside VALID₀. We have proved

F ∈ CIRCUIT-TAUT iff (G_F,T) ∈ VALID₀.

Together with coNP membership and the preceding completeness input, this proves coNP-completeness. All outputs of this reduction have correct endpoints and legal configurations, so those additional guarantees do not remove the hardness. No change of machine, growing workspace, or difficult underlying computation is involved.

**The two conditional consequences.** If VALID₀ ∈ P, decide SAT on a well-formed formula φ by constructing the circuit F=¬φ, reducing F to VALID₀, and reversing the answer. Handle malformed SAT inputs by rejecting them directly. The construction has polynomial length, so SAT ∈ P and the standard completeness theorem gives P=NP. Conversely, if P=NP, closure of deterministic polynomial time under complement gives coNP=P, so VALID₀ ∈ P.

If VALID₀ ∈ NP, coNP-hardness and closure of NP under polynomial-time many-one reductions give coNP ⊆ NP. This closure follows by first computing the reduction and then using the target verifier; the target input and certificate lengths stay polynomial in the original length. Complementing the inclusion gives NP ⊆ coNP, so NP=coNP. Conversely, equality puts VALID₀ ∈ coNP inside NP. Equivalently, a sound and complete polynomial-time checker V(G,T,z) with a polynomial bound on |z| for every valid supplied instance would prove NP=coNP. This additional existential certificate z must not be confused with a certificate for an invalid transition.

**Sparse defects and the achieved bound.** Fix a ∈ {0,1}^m and let F_a(x) be the disjunction of the m literals expressing x_i ≠ a_i. This circuit has O(m) gates and is false only at x=a. The resulting trace has h₁ at just t_a=2^m+value(a), with h₀ immediately before and after it. Exactly the transitions at t_a−1 and t_a are illegal; all other transitions, including the initial edge, are legal. Both indices lie in {0,…,T−1} by the strict interior bounds above. A uniform transition sample therefore detects a violation with probability 2/T. For r independent samples the detection probability is 1−(1−2/T)^r ≤ 2r/T, by the union bound. The formula for the upper bound also holds without independence when every sample is individually uniform. For this family the full description length is N=O(m log(m+2)), whereas T=2^(m+2)−1. For every fixed d, N^d/T tends to zero, so polynomially many such samples have vanishing detection probability. This is a bound on this sampling rule, not a circuit lower bound.

The desired general deterministic validator would run in N^d for one fixed exponent d, not in a polynomial in the numeric horizon T. Directly evaluating every transition gives a bound O(T·poly(N)), which is exponential in m on these instances. That enumeration cost alone proves no time lower bound; the rigorous obstruction is the reduction and its conditional complexity consequences.

**Scope of the negative result.** This lemma concerns the semantic validity of an arbitrary *supplied* circuit. It does not prove that a short trace description exists for an arbitrary long computation, or that verifying all such descriptions is outside P or NP. Those latter separation statements are not known here. In this very example the valid padded run has the simple canonical descriptor “output s₀ at zero and h₀ otherwise,” regardless of F. A proposed NP verifier for a different language could restrict itself to a structured certificate family and reject other descriptions of the same computation. Therefore the lemma stops the unsupported generic-validator shortcut, not every possible succinct-certificate construction, and it does not establish hardness for the existential question of whether the fixed machine has some valid descriptor. A route using a restricted family still needs its own soundness, polynomial verification bound, and completeness for the computations required by the diagonal construction.

Mathematical review: both directions of the reduction, the nonhalting initial state, the strict interior address bounds, full description lengths, malformed strings, and the distinction between descriptor validation and descriptor existence are accounted for above. No finite experiment is used as evidence for a complexity separation.

## Mathlib

Coverage: **not checked** for the full succinct-trace statement or its supporting circuit, coNP, reduction, and probability facts. No matching Mathlib theorem, absence claim, or unverified identifier is asserted. Cook–Levin is a named supporting input in the linked standard-results note; the official formula-tautology statement supports the completeness background, not a match for this entire lemma. The trace construction and its correctness are proved explicitly above.
