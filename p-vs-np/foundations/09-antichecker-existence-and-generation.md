# Antichecker existence and the required feasible generator

## Hypotheses

This note compares Lipton–Young's small-support theorem with Pich–Santhanam, arXiv:2312.08163v1, Theorem 7. It imports statements and records their applicability; it constructs no generator and proves no new transfer.

Keep the source conventions separate. Lipton–Young's C_L(n) and circuit size count **binary description length**. Pich–Santhanam's Circuit[s] counts gates in fan-in-two Boolean circuits (§2.1, p. 11). Their SAT_n(x,y) is the assignment-checking relation, whereas SAT_n(x) is the decision function. These conventions have not been substituted into L011's CNF evaluator.

## Conclusion

**Small support.** For an r-by-c payoff matrix M, Lipton–Young Theorem 2 gives a k-uniform strategy for Min within ε(M_max−M_min) of the game value when k≥ln(c)/(2ε²); there is a symmetric statement for Max. Their Theorem 6 gives, for sufficiently large n and s≤C_L(n)ε²/(3n), a multiset of s/ε² n-bit inputs on which each size-s circuit has error at least 1/2−ε. These are existence statements under the displayed conditions. The source's own example uses ε=1/3, s≤C_L(n)/(27n), 9s inputs and error at least 1/6.

**Construction scope.** Theorem 9 uses a payoff oracle and a Σ₂ computation. Theorem 10 uses Σ₂^P procedures for its circuit-complexity tests. Corollary 8's small sampling circuit is existential. None is the deterministic polynomial-time map from 1^n required below.

**Required transfer premise.** For fixed k≥3, Pich–Santhanam Theorem 7 assumes a polynomial-time f and an S^1_2 proof that, for every unary length n, its output satisfies one of these alternatives, with size poly(n^k):

- A circuit B satisfies ∀x,y∈{0,1}^n, SAT_n(x,y) → SAT_n(x,B(x)).
- Sets A,A′ and a relation D⊆A×A′ specify exactly one y_x per x∈A; ∀x∈A ∀y∈{0,1}^n, SAT_n(x,y) → SAT_n(x,y_x); and every circuit C with at most n^k gates disagrees with SAT_n(x,y_x) on some x∈A.

Under that premise, EF not being polynomially bounded implies SAT_n∉Circuit[n^k] for infinitely many n. This is a fixed-exponent conclusion. The full generator premise and the EF lower bound are both absent here.

**Comparison.** The existence theorem does not supply f, its assignment data, or the formal proof. No unprovability or impossibility claim follows. The pairing D is part of the formal statement, although informal Theorem 3 suppresses it. An unsatisfied chosen assignment does not certify unsatisfiability: the universally quantified implication is what justifies its decision label. No separate UNSAT proof for each member of A is demanded by the theorem.

## Proof

Imports by named statements; the comparison concerns their explicit hypotheses and conclusions.

- Richard J. Lipton and Neal E. Young, [*Simple Strategies for Large Zero-Sum Games with Applications to Complexity Theory*, STOC 1994](https://www.cs.ucr.edu/~neal/Lipton94Simple.pdf), pp. 734–740: Theorem 2 and proof, p. 736; Definition 4, Theorem 6 and proof, pp. 737–738; Corollary 8, pp. 738–739; Theorems 9–10 and their arguments, p. 739. The [arXiv:cs/0205035v1 transcription](https://arxiv.org/pdf/cs/0205035v1), posted 18 May 2002, PDF pp. 3–6, was used to read the formulas clearly. Proposition 11, p. 740, has an additional noncollapse hypothesis and only a stated result here; its omitted full proof is not used.
- Ján Pich and Rahul Santhanam, [*Towards P≠NP from Extended Frege lower bounds*, arXiv:2312.08163v1](https://arxiv.org/pdf/2312.08163v1), submitted 13 December 2023: nonuniform comparison and Theorem 3, pp. 5–6; feasible-minmax discussion, p. 9; circuit-size convention, p. 11; Theorem 7, its proof, and the subsequent existential-witnessing discussion, pp. 19–20. The proof retains the formal-provability premise. The following discussion identifies dependence of later KPT outputs on earlier satisfying assignments as an obstacle to replacing f by existential quantifiers. That discussion is not an impossibility theorem.

Further construction and formalization checks are recorded in the [assessment](../drafts/literature/2026-09-27-feasible-antichecker-generator.md). They do not provide a full matching theorem. No reproof of minmax, parameter specialization, new algorithm or EF bound is asserted.

## Mathlib

Coverage: **not checked** for the exact generator or the supporting minmax, antichecker and transfer results. Theorem 2 and Theorem 6 support existence; Theorem 7 is a conditional transfer. None is identified as a full library match for the missing premise.
