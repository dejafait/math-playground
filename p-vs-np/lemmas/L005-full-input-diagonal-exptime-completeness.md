# L005 — The full-input diagonal language is EXPTIME-complete

## Hypotheses

Use the uniform binary language, complexity-class, and reduction conventions in [the model note](../foundations/01-model-and-target.md). Use exactly the deterministic one-tape model and language D_full of L003: for a nonempty well-formed machine description e of length s, a unary integer k ≥ 1, and r ≥ 0, the input is

    x = 1^s 0 e 1^k 0 1^r,    N = |x| = 2s+k+2+r.

It belongs to D_full precisely when the described machine M_e halts rejecting on this same x within (N+1)^k transitions. Malformed strings are outside the language. The clock counts transitions of M_e, not transitions of a universal simulator. Descriptions are ordinary explicit transition tables with binary state indices; the fixed tape alphabet contains binary input symbols and a blank. The usual left-boundary convention, if present, is part of the machine model.

## Conclusion

D_full is EXPTIME-complete under deterministic polynomial-time many-one reductions. More precisely:

1. It has a deterministic decider taking time 2^(O(N log(N+1))).
2. Every language in EXPTIME reduces to D_full with r=0; no padding is needed for the hardness construction.
3. D_full ∈ NP if and only if NP = EXPTIME. If this holds, then P ≠ NP by L003, and NP = coNP.

The equivalence in part 3 neither supplies nor rules out an NP verifier. In particular, EXPTIME-completeness is not being used as a proved separation from NP.

## Proof

**Uniform exponential-time upper bound.** Parse the input, rejecting malformed strings in polynomial time. For a well-formed input, k ≤ N and |e| ≤ N. Its clock satisfies

    T = (N+1)^k ≤ (N+1)^N = 2^(N log₂(N+1)).

The integer T has O(N log(N+1)) bits. Repeated binary multiplication computes it in polynomial time in N, since there are at most N multiplications and all intermediate values have at most that many bits. The simulator keeps a binary transition counter of the same bit length.

During T transitions, a one-tape machine starting on N input cells visits at most N+2T+O(1) cells. A universal interpreter can store those cells, its head position, and its state, together with the supplied explicit transition table. Each state identifier has at most N bits. To perform a step, the interpreter scans the table to find the applicable row, compares the relevant state and symbol, and updates the stored configuration and counter. These operations take a fixed polynomial in N+T+1 time per step; the exponent is independent of e and k. There are at most T steps. A further polynomial simulation overhead, if needed to use the fixed one-tape model, keeps the total within (N+T+1)^a times a fixed constant, for a single fixed a. Thus the total is 2^(O(N log(N+1))). Check the initial configuration for a halting outcome as well as each subsequent configuration through transition T, and stop on either halting outcome. This decides the specified language and puts it in EXPTIME. No running-time lower bound is inferred from this upper bound.

**Compiling the source word into a machine.** Fix any language H ∈ EXPTIME. Fix a deterministic decider A for H in the same one-tape model and a nonnegative integer-valued polynomial p such that A halts on every n-bit input within 2^p(n) transitions. The choice of A and p depends only on H. If necessary enlarge p to absorb a constant factor and polynomial changes of machine model.

Given a source word y of length n, construct a machine R_y as follows. On any binary input w of length N, it clears that input, writes y in the standard initial input position, returns its head to that position, and runs A. It halts rejecting if A accepts and halts accepting if A rejects. A's finite transition table is included directly; simulating A therefore counts its actual transitions, with at most a fixed extra number of initialization and final transitions.

Clearing w costs O(N+1) transitions. For a two-way tape, scan right to the first blank without changing w, then scan left while erasing its nonblank input symbols. The first blank encountered to the left of the input identifies its former start; moving one cell right restores the standard starting position. For a tape with a left boundary, stop the return scan at that boundary instead. The empty-input case is handled separately in constant time. These routines use the same fixed alphabet. A chain of n writing states then writes y, and a return scan restores the head; this costs O(n+1). The n=0 case starts A directly on the cleared tape. Both routines leave an otherwise blank tape, so the run of A is exactly its run on y, independent of w.

Each writing state stores one specified bit of y in its transition. With binary state indices, the resulting description e_y has length

    n ≤ s_y = |e_y| ≤ C_H (n+1) log₂(n+2)

after enlarging the fixed constant C_H. For the lower bound, emit the n distinct writing states explicitly, without optimizing their transition tables. The fixed part is nonempty, including when n=0. The table can be generated in polynomial time by writing these states and relabeling the fixed states of A. Its generation does not run A. There is a constant C ≥ 1, independent of y and w, such that the actual transition count obeys

    t_R_y(w) ≤ C(N+n+1) + 2^p(n).

This bound includes clearing the full supplied input; ignoring its cost would not suffice for the intended reduction.

**Choosing a polynomial-length unary clock.** Let B=2C+1 and fix an integer c ≥ 1 with 2^c ≥ B. Set

    k_y = p(n)+c+1,
    f(y) = 1^s_y 0 e_y 1^k_y 0.

This is a well-formed core with r=0 and length N_y=2s_y+k_y+2 ≥ n. Both s_y and k_y are polynomially bounded in n; k_y is emitted in unary. The map f is therefore total and polynomial-time, including its whole output. The machine R_y was constructed independently of k_y and never needs to know its own description or the reduced input length in advance.

For w=f(y), the transition estimate and N_y ≥ n give

    t_R_y(f(y))
      ≤ C(2N_y+1) + 2^p(n)
      ≤ B(N_y+1) 2^p(n).

Since N_y+1 ≥ 2 and p(n) is a nonnegative integer,

    (N_y+1)^k_y
      = (N_y+1) (N_y+1)^(p(n)+c)
      ≥ (N_y+1) 2^p(n) 2^c
      ≥ B(N_y+1) 2^p(n).

Hence R_y always halts within the clock on f(y), with the correct comparison made in transitions of the described machine. Its output was reversed, so

    y ∈ H
      iff A(y) accepts
      iff R_y(f(y)) rejects within (N_y+1)^k_y transitions
      iff f(y) ∈ D_full.

This proves EXPTIME-hardness. Together with the upper bound, it proves completeness. The reduction is allowed a polynomial output degree depending on the fixed source language H. Consequently the 2^(O(N log(N+1))) target upper bound is fully compatible with completeness for the union of all deterministic exponential polynomial time bounds.

**What NP membership would imply.** First, NP ⊆ EXPTIME: for a fixed NP verifier and polynomial witness bound q(n), enumerate the fewer than 2^(q(n)+1) binary witnesses of length at most q(n), and run the verifier on each. A polynomial factor for verification is absorbed in an exponential of a fixed polynomial. This deterministic algorithm accepts exactly when some witness passes.

Suppose D_full ∈ NP. For any fixed H ∈ EXPTIME, first compute the reduction f above, then use the NP verifier for D_full on f(y). Polynomially bounded output length makes both the new witness bound and the verification time polynomial in |y|. Thus H ∈ NP. This proves EXPTIME ⊆ NP and hence NP = EXPTIME. Conversely, if NP = EXPTIME, the established EXPTIME membership puts D_full in NP.

Under this equality, the already proved D_full ∉ P from L003 supplies a language in NP outside P. Also EXPTIME is closed under complement: interchange the accepting and rejecting outputs of a total deterministic decider. If NP = EXPTIME, NP is therefore closed under complement, which gives NP = coNP by the definition of coNP. These are conditional conclusions, not new separations or collapses asserted unconditionally.

**Comparison with the missing bound.** The target NP verifier would require one fixed polynomial bound on certificate length and verification time for every input of D_full. The 2^(O(N log(N+1))) deterministic algorithm does not meet that requirement. Completeness shows that meeting it by any sound and complete certificate family would give NP verifiers for every EXPTIME language. This is a substantially stronger sufficient objective than finding some NP language outside P. The theorem does not refute an incomplete certificate family or rule out studying restrictions of D_full, but such a restriction must separately establish NP membership and preserve a separation from P; L003's diagonal argument cannot automatically be transferred to it.

## Mathlib

Coverage: **not checked** for this exact language, the EXPTIME-completeness theorem, or the conditional class equalities. No matching Mathlib theorem, supporting Mathlib identifier, or absence claim is asserted. The simulation, compiler, clock accounting, reduction, and class-containment arguments are proved above; the conditional separation uses the full-input diagonal contradiction in L003. The [official problem statement, §1](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) supports the uniform P/NP conventions, not a match for this completeness theorem.
