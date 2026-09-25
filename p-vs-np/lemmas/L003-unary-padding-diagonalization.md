# L003 — Unary padding does not repair explicit-trace diagonalization

## Hypotheses

Use the uniform language and full-input-length conventions in [the model note](../foundations/01-model-and-target.md). Fix a standard deterministic one-tape Turing-machine model with a fixed finite tape alphabet, explicit finite transition tables, and distinct accepting and rejecting halting states. Well-formed machine descriptions are recognizable in polynomial time. The usual polynomial simulations between standard tape models preserve P. A clock counts transitions of the described machine, not steps of a universal simulator.

For a nonempty well-formed machine description e of length s and an integer k ≥ 1, define the binary core

    z(e,k) = 1^s 0 e 1^k 0.

Thus the exponent is unary and the core is self-delimiting. A well-formed full input is x = z(e,k)1^r with r ≥ 0; put m = |z(e,k)| = 2s+k+2 and N = |x| = m+r. Parsing is unique: read s, then exactly s description bits, then the unary k terminated by 0; all remaining bits must be 1. Malformed strings are outside each language below. Write M_e for the described machine, and define

    T_full(x) = (N+1)^k,
    T_core(x) = (m+1)^k.

Let D_full contain exactly the well-formed x for which M_e(x) halts rejecting within T_full(x) transitions. Let D_core contain exactly the well-formed x satisfying T_core(x) ≤ N for which M_e(z(e,k)) halts rejecting within T_core(x) transitions. Acceptance by the simulated machine or failure to halt within the clock gives a no-instance in both definitions.

An explicit rejecting transcript lists the initial configuration, every following configuration, and the first rejecting halting configuration, without omitted steps or compressed intervals. Every listed configuration occupies a nonempty record in the binary certificate, so a run of t transitions requires at least t+1 certificate bits. Local transition checks and determinism force any valid such transcript to be the actual run.

## Conclusion

1. D_full is decidable and D_full ∉ P. This statement does not establish D_full ∈ NP.
2. For every C ≥ 1 and integer d ≥ 0 there is one fixed core z(e,k) such that, for all sufficiently large r, x = z(e,k)1^r belongs to D_full and every explicit rejecting transcript for x has length greater than C(N+1)^d. Thus this explicit-transcript certificate scheme has no fixed polynomial witness bound for D_full, even with arbitrary unary padding of the core.
3. D_core ∈ P, with one polynomial bound uniform over the descriptions e and exponents k. Complementing a machine's answer on the shorter core therefore does not, by itself, diagonalize against its answer on the full padded input.

These statements stop this padding repair of explicit-trace verification. They do not rule out a different verifier or a structured compressed certificate system, and they do not separate P from NP.

## Proof

**The full-input diagonal language.** On a well-formed x, compute the finite integer T_full(x), simulate M_e(x) for that many transitions or until it halts, and accept exactly if it halts rejecting within the clock. This terminates; no polynomial running-time claim is made for this algorithm.

Suppose a machine A decided D_full in time at most C(N+1)^a, for fixed C ≥ 1 and integer a ≥ 0. Use its description e_A and choose an integer k > a. The fixed core z(e_A,k) admits arbitrarily long padding, so choose r large enough that C ≤ (N+1)^(k−a). Then A(x) halts within (N+1)^k transitions on this very x = z(e_A,k)1^r. By the definition of D_full,

    x ∈ D_full  iff  A(x) rejects.

Since A is a correct decider, x ∈ D_full also holds iff A(x) accepts, a contradiction. Thus D_full ∉ P. The exponent k is allowed to depend on the candidate A; no fixed NP-verifier exponent has been obtained.

**Actual long runs, rather than merely large allowed clocks.** Fix C,d as in the second assertion and set q=d+1. Construct a deterministic machine R_q that, on every input of length N, obtains N, enumerates all q-tuples in {0,…,N}^q, executes at least one transition for every tuple, and then rejects. Here q is fixed in the machine description. Nested counters implement this enumeration. They store only q integers of O(log(N+2)) bits; initialization and each counter update can be implemented by polynomially many tape scans of a region of polynomial length in N. Consequently there are fixed constants B_q ≥ 1 and integer b_q ≥ 1 such that its actual running time t_q(N) satisfies

    (N+1)^q ≤ t_q(N) ≤ B_q(N+1)^b_q.

For clarity, the polynomial upper bound needs no speedup assumption: the machine can first count the input using repeated scans, then keep the q counters and N in delimited blocks next to the input. Updating and comparing these fixed many blocks costs a fixed polynomial in N per tuple. Multiplying this cost by the (N+1)^q tuples gives the asserted upper bound. The lower bound counts actual executed transitions, regardless of this overhead.

Choose a description e_q for R_q and k=b_q+1, keeping the core z(e_q,k) fixed while r increases. For all sufficiently large N, B_q ≤ N+1, so R_q(x) rejects within T_full(x) and x ∈ D_full. But every explicit transcript has length at least t_q(N), and

    t_q(N) / [C(N+1)^d] ≥ (N+1)^(q−d)/C = (N+1)/C.

This tends to infinity along the padded inputs. Hence all sufficiently large ones have no explicit transcript within the proposed witness bound. Every polynomial witness bound is bounded above by some C(N+1)^d, proving the assertion for every fixed polynomial.

The rejected proposal cannot be rescued just by increasing r: the running time in this family is measured on the same full input whose length is N. The elementary nominal comparison (N+1)^k/[C(N+1)^d] also grows with N when k>d, but that comparison alone would not have proved the claim; R_q supplies the necessary lower bound on actual runs. R_q decides a constant language, so its deliberate delay is not a lower bound on the intrinsic difficulty of that language or on other certificate formats.

**A polynomial algorithm for the shorter-core construction.** Parse x and determine m,N,k. Starting from 1, multiply by m+1 exactly k times, keeping a value capped at N+1. If it exceeds N, reject. This correctly checks (m+1)^k ≤ N, because m+1 ≥ 2 and further multiplication cannot restore the inequality. There are at most k ≤ N multiplications on O(log(N+2))-bit integers, so this test is polynomial in N even when the uncapped value is huge.

If the test passes, simulate M_e on the core z for at most T_core ≤ N transitions. A uniform interpreter has polynomial overhead here. In at most N transitions a one-tape machine on an input of length m ≤ N visits only O(N) tape cells. Its tape, head position, state and explicit transition table therefore have descriptions of polynomial length in N, since |e| ≤ N. Each simulated step can find the applicable table row by scanning the supplied table, comparing state and symbol descriptions, and updating the stored configuration. These are fixed polynomial-time operations on polynomial-size strings; at most N steps preserve one fixed polynomial bound, independent of e and k. Accept exactly when the simulated run halts rejecting within the clock. This is a deterministic polynomial-time decider for D_core.

**Where the putative contradiction is lost.** The defining complement for a sufficiently padded x concerns M_e(z), whereas a decider for D_core must answer membership on x. The following application to D_core's own decider makes the distinction explicit. Let A be the polynomial-time decider just constructed, with running time at most C(n+1)^a on length n. Choose an integer k > a with 2^(k−a) ≥ C, and let z=z(e_A,k), m=|z|. As an unpadded input z, its clock test fails because (m+1)^k > m. Hence A(z) rejects, and its running time is at most C(m+1)^a ≤ (m+1)^k. For every r with N=m+r ≥ (m+1)^k, the full input x=z1^r therefore belongs to D_core, and A(x) accepts. Thus

    A(z)=0,    D_core(x)=1−A(z)=1,    A(x)=1.

There is no disagreement on x. The same input requirement needed for the first diagonal contradiction is absent in this padded construction.

**Comparison with the target.** The first construction really defeats all polynomial-time deciders, but its explicit certificates fail the single fixed bound required for NP. The second has a uniform polynomial-time algorithm, despite allowing arbitrary encoded exponents, because its clock is paid for by the full input length while the simulated input stays short. Neither construction supplies a language proved to lie in NP outside P. The proof makes no assertion about all possible uses of padding or all possible verifiers.

## Mathlib

Coverage: **not checked** for these padded languages, the explicit-transcript obstruction, or the full statement. No matching Mathlib theorem or absence claim is asserted. The diagonal and padding arguments, including the elementary uniform-simulation justification, are supplied above.
