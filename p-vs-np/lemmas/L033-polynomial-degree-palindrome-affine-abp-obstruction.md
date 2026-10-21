# L033 — Polynomial-degree palindrome circuits obstruct affine-ABP conversion

## Hypotheses

Work in the free noncommutative polynomial ring F₂<x_0,x_1>, with distinct generators and formal polynomial equality. For integers k>=0 set

    P_0=1,
    P_(k+1)=x_0 P_k x_0+x_1 P_k x_1.

Arithmetic circuits are division-free, fan-in two, with ordered multiplication and shared gate references. Syntactic degree is zero at constants, one at generators, the maximum at addition and the sum at multiplication; every internal gate is charged.

An affine-edge ABP is an explicitly encoded finite acyclic directed graph with N>=1 vertices, designated source s and sink t, and edge labels c+a_0 x_0+a_1 x_1 with coefficients in F₂. Its output is the sum of source-to-sink path products in traversal order. Include the empty path when s=t. Parallel edges are allowed. All vertices, edges, labels and identifiers count toward its full binary length B; graphs or edge labels given implicitly by circuits are excluded. Dense numbering and a conventional encoding using O(log(N+2)) bits per vertex reference are permitted. Requiring a unique graph source and sink only narrows this receiving model.

## Conclusion

There is a shared circuit for P_k with at most 5k+3 nodes, all gate syntactic degrees at most 2k, and full binary length

    T_k=O((k+1) log(k+2)).

For k>=1 its output has formal degree exactly 2k. Every affine-edge ABP computing the identical formal polynomial has

    N>=2^k,     B>=c N

for a fixed positive encoding constant c. Consequently its full binary length exceeds every fixed polynomial in T_k asymptotically. No conversion of arbitrary polynomial-size, polynomial-syntactic-degree shared circuits into explicit affine-edge ABPs computing the identical polynomial can have a polynomial bound in full input length.

For completeness, the degree-d component, d>=1, of any such N-vertex ABP has a homogeneous consecutive-layer linear-edge ABP with at most 1+dN vertices, at most N+(d-1)N² edges, and full binary length

    O(d N² log(dN+2)).

It is constructible in polynomial time in B+N+d; if its component is nonzero, pruning makes every retained vertex lie on a source-to-sink path. In particular this normalization is polynomial in B+k when d=2k. The lower bound N>=2^k is on the original affine graph, not only its normalized graph. At k=0, P_0=1 has a constant-size ABP, and no asymptotic obstruction is asserted.

This is a REPRODUCTION and field/model specialization of the established palindrome separation, not a newly discovered lower-bound mechanism. It concerns neither Boolean equality nor IPS certificates. No realization as an unavoidable L025 output, hardness of every certificate, ER lower bound, arbitrary-circuit identity checker or SAT decision lower bound follows.

## Proof

**Precise imported results and reason for the specialization.** Noam Nisan, *Lower Bounds for Non-Commutative Computation (Extended Abstract)*, STOC 1991, pp.410–418, [DOI](https://doi.org/10.1145/103418.103462), [primary-paper mirror](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf), §§2–3 and §4.2, PDF pp.4–6: Theorem 1 gives the coefficient-matrix rank characterization of homogeneous linear-edge ABPs; its lower-bound proof factors each cut matrix through the vertices of its layer. Theorem 4 gives the exact palindrome family above, a linear-size shared circuit, and an exponential ABP/formula lower bound. The source works over the reals. We use its named cut-factorization mechanism and exact family, checking below the F₂ case and the broader affine-DAG receiving model; the real-field theorem is not simply restated over F₂. We do not need its upper-bound characterization or circuit-depth conclusion.

Ran Raz and Amir Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative Models*, [author-hosted 16-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf), Definition 1 and Lemma 2, printed pp.4–6, Steps 2–5, provide degree copies and scalar-edge elimination over a field without a characteristic restriction. Its stated input is a formula with zero free term. We specialize those normalization operations to an explicit DAG using finite constant-path matrices below, without unfolding it to a formula or importing the formula-specific runtime. The construction also isolates positive-degree components when the input has a nonzero constant term. The source versions and inspected proof cases are recorded in the existing literature assessment. The details here are needed for changed hypotheses and binary cost, rather than a reproof claimed as new mathematics.

**The polynomial and its small circuit.** Write rev(w) for word reversal. Induction gives

    P_k=sum_(w in {x_0,x_1}^k) w rev(w).                 (1)

The base case is the empty word. A term x_a w rev(w) x_a at the next stage is (x_a w) rev(x_a w). The two choices of first letter are disjoint and give every length-(k+1) word once. Moreover different w give different full words, since their first k letters differ. Thus no characteristic-two cancellation occurs in (1), and for k>=1 all nonzero terms have degree 2k.

At each recurrence step use two multiplication gates to form each ordered sandwich, then one addition gate. Both sandwiches refer to the same prior root. For k>=1 this adds five gates per stage, starting with the constant and two generator input nodes, giving 5k+3 nodes. The intermediate products at stage j have degrees 2(j-1)+1 and 2j; the addition has degree 2j. All inputs and internal gates satisfy the 2k bound. For k=0 use just the constant node, of degree zero. Number the nodes topologically and write each gate's opcode and at most two references with O(log(k+2)) bits; include all input labels and the output reference. This is the stated full T_k bound, without monomial expansion or tree unfolding.

**Constant-path closure for the affine receiving model.** Topologically number its N vertices. Let C,A_0,A_1 be N by N scalar matrices: for each ordered pair of vertices sum, modulo two, respectively the constant, x_0 and x_1 coefficients of all parallel edges. Each matrix is strictly upper triangular. Combining parallel edges preserves the formal path polynomial by distributivity. The combined edge's constant and variable terms may likewise be viewed as separate parallel choices; this step involves at most three choices per original edge and does not unfold paths.

Set

    K=I+C+...+C^(N-1),        G_a=A_a K  (a=0,1).

C^N=0. The (u,v) entry of K is the sum of constant-only paths from u to v, including the empty path. This identity counts contributions in F₂ and remains valid when paths cancel. Every expanded path with selected variable letters a_1,...,a_r decomposes uniquely into a constant-only prefix, the first variable edge, a constant-only block, and so on through the constant-only suffix. Conversely, concatenating such pieces gives a directed path: every nonempty piece strictly advances in topological order, so it cannot revisit a vertex. Therefore its word coefficient is exactly

    [x_(a_1)...x_(a_r)] f_B
       =e_s K A_(a_1) K ... A_(a_r) K e_t
       =e_s K G_(a_1)...G_(a_r)e_t.                    (2)

For r=0 this reads e_s K e_t. There is no infinite sum, division, positivity assumption or use of Boolean relations in (2). Each G_a is strictly upper triangular, so words longer than N-1 have zero coefficient, as also follows from acyclicity.

**Charged homogeneous normalization.** For d>=1 create a new source in layer zero and copies of the N vertices in layers 1,...,d. From the source to coordinate v in layer one, use the homogeneous linear label whose x_a coefficient is (e_s K G_a)_v. Between coordinates u,v in consecutive later layers use the label whose x_a coefficient is (G_a)_(u,v). Designate coordinate t in layer d as the sink. Formula (2) shows that the output is precisely the degree-d homogeneous component, including when other degree components of f_B are nonzero. There are at most 1+dN vertices and N+(d-1)N² nonzero edges after the two variable coefficients of each pair are combined into one label. If a unique source/sink is required and this component is nonzero, remove all vertices and edges not on source-to-designated-sink paths; this preserves the output and the bounds, and leaves consecutive layers. In particular other terminal coordinates are removed.

All coefficients are bits: there is no coefficient-length growth. The normalized labels have at most two fixed generator names and two coefficient bits. Charging vertex/layer records, all edge references, source/sink designations and framing gives O(dN² log(dN+2)) bits. Topological sorting and coefficient assembly are polynomial in B. Naively summing the N powers of C takes O(N⁴) field-bit operations and computing G_a takes O(N³) field-bit operations; address handling on a bit-machine adds polynomial overhead. Writing the layers takes O(dN² log(dN+2)) output bits and polynomial time in that length. These give a polynomial bound in B+N+d, rather than the formula-specific complexity in Raz–Shpilka. For the application d=2k>=2, the normalized middle layer has at most N vertices. No formula unfolding, implicit layer or circuit-valued edge is used.

**Nisan's cut-rank bound over F₂, on the original graph.** Let M_k have rows indexed by words u of length k and columns indexed by words v of length k, with entry [uv]f_B. For a word u=a_1...a_k write G_u=G_(a_1)...G_(a_k). Equation (2) factors M_k=R S, where

    R_(u,*)=e_s K G_u,       S_(*,v)=G_v e_t.

R has N columns and S has N rows. Thus rank_(F₂)(M_k)<=N. This is precisely the cut-factorization lower-bound direction of Nisan's Theorem 1, applied after finite constant closure; alternatively the normalized homogeneous graph has that width at layer k. The argument is elementary field linear algebra and uses no characteristic-zero step. Exponential matrices are used only in the proof of the bound, not constructed as part of the polynomial normalization.

For f_B=P_k, (1) says

    (M_k)_(u,v)=1 if v=rev(u), and 0 otherwise.

Reversal is a bijection of the 2^k length-k words, so M_k is a permutation matrix. Permuting its columns yields the identity; its rank over F₂ is exactly 2^k. In particular cancellation or the vanishing of minus signs in F₂ cannot change this rank. The factorization proves N>=2^k for the original affine graph. The original path-length observation additionally gives N>=2k+1, though that is not needed asymptotically. At k=0 the sole coefficient matrix is [1], and a one-vertex s=t graph represents 1 by its empty path; if distinct terminals are required, use a single constant-1 edge instead.

**Required threshold and route limit.** Explicit vertex encoding gives B>=cN. For any fixed exponent q>=0 and positive constant H, the constructed circuit encoding satisfies

    B/(T_k+2)^q >= c 2^k / (C (k+1)log(k+2)+2)^q -> infinity.

Hence B>H(T_k+2)^q for all sufficiently large k. The input syntactic degree 2k is polynomial in its full encoding length, since this encoding explicitly contains 5k+3 nodes. Degree control alone therefore cannot justify a universal polynomial-size same-output circuit-to-affine-ABP conversion. The threshold is superpolynomial in the full written circuit length, not just in degree or in a count of variables.

This disposes of that general representation step while preserving circuit upper bounds and promised ABP simulations. L017/L018 are only receiving-model context and L032 only motivates the polynomial-degree question; none is a mathematical premise here. The family need not occur in any IPS output. Changing the polynomial, choosing another refutation, supplying another certificate representation or using extra structure remains open. In particular this known representation separation supplies no all-certificate or unrestricted computation lower bound.

**Separate critical audit, 2026-10-07.** The preapproved audit checks the entire proof above against the unchanged field/model hypotheses and the inspected Nisan Theorems 1/4 and Raz–Shpilka Lemma 2 proof cases. It finds no substantive mathematical error and changes no conclusion, bound or mathematical input. The operation-count wording above now distinguishes field-bit arithmetic from address handling; the claimed construction time remains polynomial. The checks are as follows.

1. The expansion (1) is injective by its first k letters. Its terms therefore have coefficient one even in characteristic two. With lexicographic column order the middle matrix need not be diagonal, but reversal permutes its columns to the identity. Full rank follows over F₂ without a real-field rank comparison, signs, positivity or evaluation on Boolean assignments.

2. Equation (2) counts labeled path choices before reducing their multiplicities modulo two. Aggregating parallel edges uses distributivity; each chosen variable edge determines its adjacent constant runs. A nonzero-length constant run strictly increases the topological index, and an empty run fixes it. Every variable edge strictly increases it. Thus concatenated pieces are actual paths and cannot repeat vertices. Summing equal path words can cancel on either side of (2), with the same parity. In the factorization R S the entire constant run after the kth variable lies in the final K of the left factor. The right factor begins with A for the next variable, not another initial K. Consequently the cut has a unique placement for each expanded path and does not count every vertex of a constant run as an alternative split. This is the load-bearing constant-edge check.

3. For d=1 the new source-to-v label has coefficient (e_s K A_a K)_v; selecting the sink t extracts exactly [x_a]f_B. For any d>1 the successive labels give e_s K G_(a_1)...G_(a_d)e_t, with exactly d variable letters. A nonzero free term contributes only to degree zero and is never inserted into these positive-degree paths. If d>N-1, every such matrix product vanishes by strict topological progress, consistently with the zero homogeneous component. If s=t, acyclicity leaves only the empty original path, so the output is 1 and every positive component is zero. This includes N=1. The construction still represents those zero components by its unpruned layered graph; it does not claim successful nonempty-path pruning for them.

4. Pruning uses graph reachability from the new source and to the designated layer-d vertex t after zero labels are omitted. Every surviving edge on a source-to-t path has a nonzero homogeneous label; edges and vertices discarded by this rule occur on no such path at all. Therefore deletion preserves the polynomial even when surviving path contributions cancel. A nonzero component guarantees at least one such path. Every retained interior vertex then has a preceding and succeeding path edge, so the new source and designated t are the unique graph source and sink. Other layer-d coordinates cannot reach t and are removed. No layer is skipped or merged. This verifies precisely the nonzero-component qualification in the conclusion, not a stronger pruning assertion for zero polynomials.

5. Before pruning there are exactly one new source and d copies of at most N coordinates. Layer zero has at most N edges; each of the remaining d-1 transitions has at most N², each with two fixed-generator coefficient bits. With binary references to at most 1+dN vertices, vertex records and framing are bounded by the same O(dN² log(dN+2)) allowance for all N,d>=1, including N=d=1. Coefficients never grow beyond bits. Parallel-edge input size is charged in B before aggregation; no bound on its multiplicity in terms of N is assumed. Polynomial construction time is in B+N+d, not in log d or in an uncharged implicit graph description.

6. For k>=1 the circuit uses three input nodes and five new gates per stage, each gate having syntactic degree at most 2k. At k=0 the two generator inputs are omitted, so the claimed degree-zero bound really holds for every included gate. Full encoding has an upper bound C(k+1)log(k+2), and its explicit gate records also give an Omega(k) lower bound. Thus syntactic degree is polynomial in full input length. Conversely the receiving graph has B>=cN by its explicitly charged vertex records. Combining the original-graph rank bound with the upper bound on T_k proves the displayed divergence for every fixed polynomial exponent and constant. A lower bound only on the normalized graph would not suffice for that conclusion; the N-column factorization provides the required original-graph bound directly.

The audit confirms an existing local specialization of a known separation. It is neither a new lower-bound theorem nor formal verification. L017/L018/L032 are context and do not enter this proof; the empty local DAG input row remains correct. The result stops only the blanket degree-only identical-output conversion. It establishes no IPS realization, forced L025 output, lower bound for all alternative certificates, unrestricted ER bound or SAT decision lower bound.

## Mathlib

Coverage **not checked** for the full noncommutative palindrome separation, affine-DAG normalization or Nisan cut-rank characterization. No matching Mathlib theorem or absence claim is asserted. The named primary papers above provide the standard inputs; the characteristic-two and explicit-encoding applicability checks are written out here. The separate critical audit above is complete; neither the proof nor the audit is formally verified.
