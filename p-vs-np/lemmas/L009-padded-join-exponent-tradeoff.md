# L009 — Resource normalization loses the fixed-exponent join bound

## Hypotheses

Use c_L(n), SIZE(n^d), and the circuit and machine conventions in the [fixed-exponent source note](../foundations/03-kannan-fixed-exponent-theorem.md). All core inputs have positive length, and all logarithms have base two. Set ell(n)=ceil(log_2(n+2)).

For each integer j>=2, take the constructive machine M_j and language A_j from Cai–Watanabe's Theorem 1 as recorded in that note. Thus M_j has one existential block followed by one universal block, branch time O_j(n^(j^2) ell(n)^(j+1)), and

    c_A_j(n) >= n^j/4

at an unbounded set of lengths. Let G be one deterministic algorithm producing a binary-branching description of M_j from 1^j. Binary branching can be arranged with fixed-j constant overhead; the interpreter below handles the machine's finite alphabet and tape count. No polynomial bound for G as j varies is assumed.

Define the clocked padded join J on strings

    1^j 0 1^n 0 x 1^t,     j>=2, n>=1, |x|=n, t>=1.

It first simulates G(1^j) for at most t steps. If G has not produced M_j, reject. Otherwise it simulates M_j on x for at most t target-machine steps on each branch, rejecting branches that time out. Accept according to the existential-then-universal semantics. Malformed strings are rejected. The unary n field determines where x ends and the final unary clock begins.

Choose a fixed integer D_j>=1 sufficiently large that

    B_j(n) = D_j (n+1)^(j^2) ell(n)^(j+1)

dominates G's running time, the description length of M_j, and every branch time of M_j on n-bit inputs, for every n>=1. The source bound and totality of G allow such a constant for each fixed j. These constants specify slices for a nonuniform restriction argument; the algorithm for J does not compute them.

## Conclusion

1. J belongs to Sigma_2^P with one fixed polynomial resource bound in its full input length. Its slice with t=B_j(n) agrees with A_j, and has length

       N_j(n) = j+2n+B_j(n)+2
              = Theta_j(n^(j^2) (log n)^(j+1)).

   Therefore c_J(N_j(n))+3 >= c_A_j(n). At the hard core lengths this yields, for some fixed-j positive constant delta_j and all sufficiently large such n,

       c_J(N_j(n)) >= delta_j N_j(n)^(1/j)
                     / (log N_j(n))^((j+1)/j).

   These inherited exponents are at most 1/2. This is a lower-bound guarantee from the particular slices, not an upper bound on c_J.

2. More generally, suppose a padding leaves the n original bits as free coordinates, fixes all other coordinates, and has length

       N_j(n) = Theta_j(n^(a_j) ell(n)^(v_j)),
       a_j>=1, v_j>=0.

   To pay for the displayed resource budget using one fixed exponent C>0, require B_j(n)=O_j(N_j(n)^C). Necessarily a_j C>=j^2; if equality holds, also v_j C>=j+1. The strict-exponent lower-bound transfer from the supplied n^j hard lengths excludes a proposed padded circuit exponent d when a_j d<j. Its threshold therefore satisfies

       j/a_j <= C/j <= C/2.

   It cannot become unbounded by increasing j. This stops the fixed-tag restriction argument based on these published resource and hardness bounds from proving a superpolynomial lower bound after normalization. It does not rule out stronger hardness, faster algorithms, or a different argument using additional information.

3. Padding has supplied a common Sigma_2^P bound, not an unconditional NP verifier. Under the temporary assumption P=NP, J is in P and hence P/poly; composing its hypothetical circuits with the padded slices gives bounds consistent with the supplied lower bounds for every A_j. This construction produces no P-versus-NP contradiction.

## Proof

**A common alternating bound with all setup costs charged.** Write N for the full input length. Parsing the unary fields and checking the clock suffix takes polynomial time. Both n and t are at most N. The fixed program G is simulated for at most t steps, so even unexpectedly expensive parameter-dependent machine construction cannot violate the common bound. Its output, if present, has length at most t up to a fixed encoding constant.

A universal interpreter can simulate t steps of a machine with description length O(N), on an input of length at most N, in time polynomial in N with an absolute exponent. Each simulated tape needs only O(n+t) cells. With explicitly described tapes, alphabet symbols, and transitions, both the number of tapes and the bit length of a cell symbol are bounded by O(N). Scanning these polynomially long configurations and the transition description at every one of the t<=N steps therefore incurs a fixed polynomial overhead. These bounds do not depend on j, and do not require a constant-overhead reduction to one tape.

For an explicit bounded-quantifier description, existentially supply N bits for choices before the phase switch and universally supply N bits for choices after it. A deterministic polynomial-time predicate runs the preceding setup and clocked simulation, consuming at most one corresponding choice bit per target-machine step. Unused choice bits are ignored. The constructed M_j never returns to the existential phase after entering the universal phase. Thus its accepting semantics is exactly one existential quantifier followed by one universal quantifier over polynomially long strings. Timeout and malformed-input rejection are deterministic parts of the same predicate. This proves J in Sigma_2^P uniformly, without asserting NP membership.

When t=B_j(n), the generator and every branch of M_j finish, so the slice accepts x exactly when x belongs to A_j. This proves the slice identity even though J also admits smaller or larger clock fields. The exact length is the sum of the two unary headers, the n-bit core, and the t-bit clock. For fixed j>=2, the clock dominates the linear terms and gives the displayed Theta estimate.

**Restriction and the logarithmic loss.** Use the constant-producing restriction construction in L008. From an N_j(n)-input circuit for J, hardwire the j and n fields and every clock bit, leaving exactly the n coordinates of x free. At most three additional gates produce both constants from the first free bit. The resulting circuit computes A_j. Hence

    c_A_j(n) <= c_J(N_j(n))+3.

At its unbounded hard lengths, c_J(N_j(n))>=n^j/4-3>=n^j/8 once n is sufficiently large. Since

    N_j(n)^(1/j) = Theta_j(n^j (log n)^((j+1)/j)),
    log N_j(n) = Theta_j(log n),

the asserted lower bound in N_j(n) follows. The j-dependent constants are fixed before taking the unbounded sequence of core lengths. This argument does not assert that every padded length is hard.

**The general exponent test.** Suppose a language B with the stated coordinate slices for A_j has circuits of at most K(N+1)^d gates for one fixed K and d>0. Fix j. Hardwiring gives

    c_A_j(n) <= K(N_j(n)+1)^d+3
             = O_j(n^(a_j d) ell(n)^(v_j d)).

If a_j d<j, dividing this inequality by n^j gives a quantity tending to zero, because every fixed power of log n is dominated by every positive power of n. That contradicts c_A_j(n)/n^j>=1/4 along the hard lengths. Thus unbounded values of j/a_j would suffice to exclude every fixed d by this strict-exponent test. Equality of exponents is not used: a unit-coefficient lower bound alone does not exclude all upper-bound coefficients, and logarithmic factors must also be charged.

Now the budget requirement B_j(n)=O_j(N_j(n)^C), for fixed j, implies

    n^(j^2-a_j C) ell(n)^(j+1-v_j C) = O_j(1).

A positive power of n cannot be bounded by any fixed negative power of log n. It follows that a_j C>=j^2. If the n exponent is zero, a positive logarithmic exponent is likewise unbounded, giving v_j C>=j+1. Rearranging proves j/a_j<=C/j<=C/2. Consequently the displayed data and this test do not contradict a proposed exponent d>C/2. No assertion is made that such a circuit family actually exists.

For the class convention requiring exclusion of O(n^k), take j=k+1 as in the source note. The weaker but coefficient-robust exponent ratio is then k/a_(k+1)<=C k/(k+1)^2<=C/4. Neither indexing convention gives the unbounded ratio required by this transfer. In the explicit clocked join, a_j=j^2 and v_j=j+1, so the budget is linear in the clock length before the fixed universal-simulation overhead; its inherited threshold is exactly 1/j.

The necessity a_j C>=j^2 concerns domination of the chosen upper-bound budget B_j. It is not a lower bound on the true running time of M_j or every algorithm for A_j. An improved independently justified resource bound would require a fresh comparison. Likewise, the failure of fixed-tag asymptotic comparisons does not exclude arguments involving additional uniform information across varying tags.

**The conditional collapse does not restore the lost exponent.** By L008's collapse argument, P=NP would place the single language J in P. The computation-to-circuit simulation from the [standard-results note](../foundations/02-standard-results.md) would then give constants K and an integer d>=1 with c_J(N)<=K(N+1)^d. Restricting to the explicit slices yields

    c_A_j(n) = O_j(n^(d j^2) (log n)^(d(j+1))).

For every j>=2, d j^2>j, so this upper bound is compatible with the supplied n^j/4 lower bound. Under that hypothesis there is one common algorithm for the padded language, but the cost of returning to core length depends quadratically on j. Unconditionally the universal stage is still present. The common NP membership and superpolynomial hardness required for the separation have not been obtained together.

## Mathlib

Coverage: **not checked** for the full padding statement or the supporting circuit restrictions, alternating universal simulation, asymptotic comparisons, and collapse results. No Mathlib identifier or absence claim is asserted. Cai–Watanabe's Theorem 1, linked and qualified in the source note, supplies only the per-parameter machine and lower bound. It is not a citation for the padding conclusion; the full informal proof of that conclusion is above. The previous restriction and collapse arguments are used in the indicated proof paragraphs.
