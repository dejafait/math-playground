# L006 — Circuit counting and an easy MCSP threshold range

## Hypotheses

Use the AND/OR/NOT circuit basis from the [model conventions](../foundations/01-model-and-target.md), with no free constant gates. Output may be an input wire; unused gates are allowed. Let r>=1, N=2^r, and let T in {0,1}^N be the lexicographically ordered truth table of a function f_T on r bits. Write C(T) for its minimum number of non-input gates.

For an integer s>=0, encode an instance as the binary string 1^r 0 T 1^s. The unary header fixes the table length, so the suffix unambiguously encodes s. The full input length is M=N+r+1+s. Define MCSP_u to accept exactly the well-formed instances with C(T)<=s, rejecting malformed strings. This is the unary-threshold version of the minimum circuit size problem.

All logarithms below have base two. Put

B(r,s)=(s+1)(r+s)[3(r+s)^2]^s,

ell(r)=ceil(log_2(r+2)),    b(r)=floor(r/(16 ell(r))).

## Conclusion

MCSP_u belongs to NP, and every table satisfies C(T)<=2rN. At most B(r,s) of the 2^N tables satisfy C(T)<=s.

In particular, for r>=8 and s_H=floor(N/(32r)), at least a fraction 1-2^(-3N/4) of tables satisfy

C(T)>s_H, hence C(T)>N/(32r).

Nevertheless, the fixed language consisting of MCSP_u instances with s<=b(r) belongs to P, rejecting instances outside that range. For each fixed r and s<=b(r), its YES fraction among the 2^N tables is at most N^3/2^N. The permitted threshold b(r) tends to infinity and has order log N/log log N.

Thus almost universal rejection and the presence of functions requiring Omega(N/log N) gates are compatible with exact polynomial-time MCSP recognition on an unbounded threshold range. These conclusions do not decide MCSP_u at all thresholds and do not establish a lower bound for its decision predicate.

## Proof

**Parsing and NP certificates.** Read the input length and unary header first. If the stated table length 2^r exceeds the remaining input length, reject before enumerating any assignments; the comparison can use the r+1-bit binary representation of 2^r. Otherwise read exactly N table bits and check that every remaining bit is 1. This takes polynomial time even on malformed inputs.

For a well-formed input, a certificate lists t<=s gates in topological order, gate types and predecessor indices, and one output index. Each gate's predecessors must be among the r inputs and earlier gates. A NOT gate has one meaningful predecessor; when using a two-slot description, ignore its second slot. The description length is O((s+1)log(r+s+1)), hence polynomial in M. For each of the N assignments, evaluate the gates in order and compare the output with its bit of T. There are at most M assignments and M gates, and all stored indices and values have polynomial total length; even naive tape scans for each lookup give a fixed polynomial running time. A correct circuit certifies acceptance, and agreement on all assignments implies that any accepted certificate computes f_T. This proves both completeness and soundness of one polynomially bounded verifier for the whole language.

**A universal upper bound for the represented function.** Suppose T has k>=1 one-entries. Compute the r negated input bits once. For each one-entry form the conjunction of its r matching literals, using r-1 AND gates; then OR the k conjunctions with k-1 gates. The total is at most

r+k(r-1)+(k-1)=r+rk-1<=r+rN-1<=2rN.

For r=1 a conjunction has no gates, as required. If k=0, compute the constant zero using NOT(x_1) and AND(x_1,NOT(x_1)), using two gates, also at most 2rN. This argument uses no free constants. It also covers the constant-one function via the nonempty disjunction construction.

**Counting descriptions.** Fix t<=s. At gate j, for 1<=j<=t, there are r+j-1 preceding wires. Allow three gate types and two predecessor slots even for NOT. There are at most 3(r+j-1)^2 choices for that gate. The output has r+t choices. Thus the number of topologically labeled descriptions with t gates is at most

(r+t) product_{j=1}^t 3(r+j-1)^2 <= (r+s)[3(r+s)^2]^t.

This also holds at t=0, when there are r choices of output input. Every circuit has such a topological description. Summing over t=0,...,s gives at most B(r,s) descriptions. Different descriptions may compute the same table, so the number of YES tables is no larger. This is an upper bound on descriptions and tables, not a time lower bound for recognizing them.

**The counting threshold.** For r>=8 and s=s_H, both r+s<=N and s+1<=N. For example, r<=N/2 and s<=N/256 imply the first inequality, and the second follows directly from s<=N/256. Therefore

log_2 B(r,s) <= 2r+s(2+2r)
             <= 2r+N/16+N/(16r)
             <= N/16+N/16+N/128
             = 17N/128 < N/4.

Here 2r<=N/16 holds at r=8 and persists by induction, and log_2 3<2 was used in the first line. Dividing the table count B<=2^(N/4) by 2^N bounds the YES fraction by 2^(-3N/4). An integer circuit size greater than floor(N/(32r)) is greater than N/(32r), giving the claimed lower bound for the represented functions. At this fixed threshold, the constant answer NO has distributional error at most 2^(-3N/4) under the uniform table distribution. It is not an exact decider: YES tables still exist.

**An exact polynomial-time threshold range.** First let r>=2 and ell=ell(r). Then ell>=2 and ell<=r: the latter follows from r+2<=2^r, true at r=2 and preserved by induction. For s<=b(r), we have s<=r, s+1<=r+1<=2^ell, and r+s<=2r<=2^(ell+1). Consequently

log_2 B(r,s) <= 2ell+1+s(2ell+4)
             <= 2ell+1+4ell s
             <= 2ell+1+r/4
             <= 2r+1+r/4 <= 3r.

Hence B(r,s)<=2^(3r)=N^3. For r=1, b(r)=0 and B(1,0)=1, so the same bound holds.

An exact algorithm parses the instance and rejects if s>b(r). Otherwise, for every t<=s it enumerates the gate descriptions just counted and compares each circuit with every bit of T. The descriptions can be generated by nested counters over the gate types, permitted predecessor indices and output indices; this lists every allowed circuit, with possible harmless repetitions. There are at most N^3 descriptions and each comparison has polynomial cost in M. Testing the range and enumeration also take polynomial time, so one fixed polynomial bound works for the entire restricted language. For fixed r and s in this range, counting again gives YES fraction at most N^3/2^N. Since ell(r)=Theta(log r), b(r)=Theta(r/log r) as r tends to infinity; the range is not a collection of fixed finite cases.

**Comparison with the required threshold.** At s=s_H and throughout the efficient range, M=Theta(N). Counting supplies Omega(2^r/r)=Omega(M/log M) gates for individual represented functions, whereas the direct DNF construction bounds every such function by O(M log M). Neither is a superpolynomial bound in the MCSP input length. More fundamentally, C(T) measures the r-input function f_T, while a decider for MCSP_u receives the whole table and threshold. They are different functions. For all sufficiently large r, b(r)<s_H, so the same overwhelming set of Shannon-hard represented functions consists of NO instances of the exactly decidable low-threshold language. Their individual circuit complexity does not force that language outside P.

To separate P from NP through MCSP_u, one would still need to exclude every deterministic polynomial-time decider on all its inputs. Alternatively, a superpolynomial unrestricted circuit lower bound for the MCSP_u predicate would be a stronger sufficient target, using P contained in P/poly. Nothing above proves either assertion. In particular, the polynomial enumeration at s<=b(r) is not extended to thresholds near s_H, and a large enumeration cost there is not a lower bound on other algorithms. No efficient uniform construction of the high-complexity tables is supplied by counting alone.

The standard truth-table formulation is supported by Valentine Kabanets and Jin-Yi Cai, [*Circuit Minimization Problem*, STOC 2000, pp. 73–79, author's abstract and paper page](https://www.cs.sfu.ca/~kabanets/Research/circuit.html), checked 2026-09-25. The page was consulted for the definition; no theorem about NP-hardness or pseudorandomness is imported. The unary encoding and quantitative bounds above are proved here, not attributed to that abstract.

Supplementary verification: `python3 scripts/mcsp-counting/check_bounds.py` checks 400 low-threshold integer bounds for r=1,...,256 and 249 high-threshold rounding bounds for r=8,...,256. The general bounds and algorithms rest on the proofs above, not these finite checks.

## Mathlib

Coverage: **not checked** for this full statement or the supporting circuit-enumeration, NP-verification, and uniform recognition facts. No matching Mathlib theorem, supporting Mathlib identifier, or absence claim is asserted. The external source above supports the problem definition, not a match for this complete quantitative statement.
