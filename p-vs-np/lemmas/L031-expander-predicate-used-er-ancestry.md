# L031 — Independent-set predicate in genuinely used short-ER ancestry

## Hypotheses

Fix an integer Delta>=3 and a real 0<epsilon<1. Supply a finite simple undirected graph G=(V,E), with V={1,...,n}, n>=2, maximum degree at most Delta and

|N_G(U) \\ U| >= epsilon |U| for every U subset V with |U|<=n/2.

Put m=|E|. Let f_G(x)=1 exactly when {i:x_i=1} is independent. This is the predicate and graph class of L030. Use the fresh acyclic signed-AND ER convention in [foundations/05](../foundations/05-refutation-systems-and-simulation.md): z iff (a AND b) introduces (NOT z OR a), (NOT z OR b), (z OR NOT a OR NOT b), with earlier signed operands, repeated operands permitted, and duplicate literals removed. Every resolution names its earlier premises and signed pivot. Binary length charges all clauses, literal identifiers and inference references. Set T=2+|F|+|pi| in bits.

For the standard extension mechanism, cite Matti Järvisalo and Tommi Junttila, *Limitations of restricted branching in clause learning*, Constraints **14** (2009), 325–356, DOI [10.1007/s10601-008-9062-z](https://doi.org/10.1007/s10601-008-9062-z), §5.4 Remark 5, printed p. 347, [author journal PDF](https://www.cs.helsinki.fi/u/mjarvisa/papers/jarvisalo-junttila.constraints09.pdf). Fresh-definition soundness is also the principle in Stephen A. Cook and Robert A. Reckhow, *The Relative Efficiency of Propositional Proof Systems*, JSL **44(1)** (1979), 36–50, Definition 4.1 and Proposition 4.2 with proof, printed p. 44, [author scan](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf). The latter is extended Frege, not an ER ancestry theorem. Neither source is used to assert this full embedding. L027 supplies the already established signed-unit/accumulator template; the edge circuit, both output signs, exact references and binary costs are specialized below. L030 supplies its existing common-order F₂-sum lower bound without a reproof.

An extension's value is always its recursively defined Boolean function on every assignment of the original variables, including assignments violating F. Final inference ancestry is the transitive closure of actual premise references from the empty clause. A defining block's mere presence does not establish ancestry.

## Conclusion

For each sigma in {0,1}, one can construct an original width-one CNF F_(G,sigma) on exactly x_1,...,x_n and an ER refutation pi_(G,sigma) containing a positive extension variable h with all-assignment value f_G. Every extension has at least one of its defining clauses and a derived signed unit in the final inference ancestry. In particular the unit for h is (h) for sigma=0 and (NOT h) for sigma=1, and this actual signed literal is an operand in that ancestry. There are exactly 4m introduced extensions, all proof clauses have width at most three, and

T=O((n+m) log(n+m+2))=O_Delta(n log(n+2)).

For any dense common-order F₂ sum of deterministic OBDDs representing h on every original-variable assignment, L030 gives total width

W >= 2^(c n),       c=epsilon/(16*Delta*(Delta+1)).

Along any supplied unbounded family with fixed epsilon and Delta, no fixed polynomial in T bounds this total width. This is a reproduction and local specialization, without a certified originality claim. It strengthens the supplied-proof obstruction from a single OBDD to these common-order sums. It does not establish optimal-proof or every-certificate hardness, general reduced-data impossibility, an unrestricted ER lower bound, or a P versus NP resolution. The separate informal critical audit below found no substantive defect; no proof string or formal verification is claimed.

## Proof

**Retain the original domain and fix a consistent evaluation assignment.** Singleton expansion applies because n>=2 and gives deg(i)>=epsilon>0. In particular m>=1, so the edge circuit below has a first edge. For sigma in {0,1}, put ell_i=x_i if sigma=1 and ell_i=NOT x_i if sigma=0. Define

F_(G,sigma)=(ell_1) AND ... AND (ell_n) AND (NOT ell_1).

These n+1 original unit clauses retain exactly all n graph vertices as original variables. Let s_sigma be the consistent assignment x_i=sigma for every i. It satisfies the first n units, although it does not satisfy their conjunction with the last unit. Use it only to determine gate values and to derive gate units from the first n units and extension clauses. The opposite unit is reserved for the negative accumulator chain. Original clauses do not restrict the domain on which the extension functions are defined, and no nonextension variable outside F is introduced.

**Enumerate the predicate circuit.** Enumerate the edges in a fixed supplied or lexicographic order as e_i={u_i,v_i}, i=1,...,m, orienting each by u_i<v_i. First introduce the m fresh gates

p_i iff (x_(u_i) AND x_(v_i)).

Set r_1=NOT p_1 as a signed-literal alias. For i=2,...,m introduce a fresh gate

q_i iff (r_(i-1) AND NOT p_i),       r_i=q_i.

Finally introduce the fresh positive root

h iff (r_m AND r_m).

Aliases introduce no variables or clauses. The m=1 case has no q_i and uses r_m=NOT p_1; the final repeated-operand definition is legal in this case as in every other case. Enumerate these K=m+(m-1)+1=2m positive gate variables as g_1,...,g_K in the displayed order, ending with h, using identifiers n+1,...,n+K. Each operand is an original literal or an earlier signed gate, proving freshness and acyclicity.

For every assignment x, p_i(x)=1 exactly when both endpoints of e_i are selected. Induction on i gives r_i(x)=AND_(j=1)^i NOT p_j(x): the base is the alias r_1, and the step is its stated conjunction. Since b AND b=b for Boolean b, h(x)=r_m(x). Thus h(x)=1 exactly when no graph edge has two selected endpoints, which is precisely f_G(x). This verifies the function on all 2^n assignments, without any original-unit substitution. At s_0 every p_i is false and h=1. At s_1 every p_i is true and, since m>=1, h=0. The positive root variable and the sign of its derived unit are distinct notions.

**Derive every circuit signed unit with actual references.** For each k let eta_k=g_k if g_k(s_sigma)=1 and eta_k=NOT g_k otherwise. Apply L027's gate-unit procedure in topological order, introducing each gate's three defining records before its unit derivation. To verify the specialization and the repeated-operand boundary, consider z iff (a AND b).

If a(s_sigma)=b(s_sigma)=1, the true signed units (a),(b) are already available. Resolve (z OR NOT a OR NOT b) against (a), then against (b), obtaining (z). If a=b, clause normalization removes the duplicate opposite operand and one resolution suffices. The case a=NOT b cannot be in this true branch. If at least one operand is false, choose one such operand, say a, whose true signed unit is (NOT a). Resolve it against (NOT z OR a), obtaining (NOT z); use the second projection if b was selected. Here a can itself be negative, and NOT a means its opposite signed literal. The child z is fresh and cannot equal either operand variable, so the stated pivots do not delete z. These cases exhaust both truth values and require at most two resolutions per gate, each with at least one defining clause of that same gate as an ancestor. Units for original operands are the first n original clauses; units for extension operands are earlier eta units. No appeal to the inconsistent last original unit occurs in these derivations.

In particular eta_K=h for sigma=0 and eta_K=NOT h for sigma=1. This proves both required output-unit cases by the actual ER rules, not only by evaluating the circuit.

**Make all the signed units ancestors of the final inference.** Apply L027's accumulator template with the signed anchor a_0=ell_1, rather than presuming the anchor is positive. For k=1,...,K introduce a fresh gate, with identifier n+K+k,

a_k iff (a_(k-1) AND eta_k).

The symbol a_0 is an alias for an original signed literal. For each k the two operands have distinct underlying variables: one is the original anchor or an earlier accumulator, and the other is a circuit gate. Derive (a_k) by resolving the third defining clause

(a_k OR NOT a_(k-1) OR NOT eta_k)

against the earlier (a_(k-1)) and (eta_k), using two resolutions. The positive anchor unit is (ell_1), an original clause even when ell_1=NOT x_1. Independently derive (NOT a_k) from the first projection

(NOT a_k OR a_(k-1))

and the earlier (NOT a_(k-1)), using one resolution; start this chain with the original opposite unit (NOT ell_1). Both chains can be produced in increasing k immediately after each defining block. Finally resolve (a_K) against (NOT a_K) to obtain the empty clause.

Following the positive a_K derivation backwards includes (eta_K), (a_(K-1)) and its third defining clause. Repeating includes every eta_k, every positive accumulator unit and every accumulator third defining clause. Following each eta_k backwards includes a defining clause of g_k by the checked gate-unit cases. The negative chain additionally includes every negative accumulator unit and every accumulator first projection. Therefore every one of the K circuit extensions and K accumulator extensions has a defining-clause ancestor and a derived signed-unit ancestor. The root's signed unit eta_K is a direct premise in deriving a_K and its signed literal is a defining operand of that gate, whether eta_K is h or NOT h. All references are to actually written earlier records. Not every individual clause in a three-clause definition must participate; the promised property concerns at least one clause for each extension.

**Full binary accounting.** There are 2K=4m extension variables and 6K=12m defining-clause records. The circuit units require at most 2K resolutions, the positive accumulator chain 2K, the negative chain K, and the final step one. Including n+1 original initial-clause records gives

R<=6K+2K+2K+K+1+(n+1)=11K+n+2=22m+n+2=:R_*.

Clause width is at most three throughout. Maximum variable identifier is n+2K=n+4m<=R_*, initial-clause indices are at most n+1<=R_*, and premise references are at most R_*. No circuit or proof tree is unfolded.

For an explicit encoding, use L027's Elias gamma convention: a nonnegative integer t is encoded by the gamma code of t+1 with length 2 floor(log₂(t+1))+1. Prefix every clause with its size and each literal with its sign bit and absolute variable identifier. Encode F by n, clause count and its clauses. Encode pi by its record count; each record has a two-bit kind, its clause and either an initial-clause index, an extension-variable identifier and two-bit definition slot, or two premise references and a signed pivot. Each three-clause extension block recovers both signed operands from its two projections and checks the normalized third clause. Duplicate projection clauses for repeated operands are still written as the two distinct definition slots. Thus no gate information is omitted from the encoding.

Put L=ceil(log₂(R_*+2)). All encoded integer values, including headers, are at most R_* for these graphs, so each has at most 2L+1 bits. A width-three clause and constant-sized inference metadata fit in 64L bits per proof record: for example a resolution record has at most seven encoded integers (clause size, three variable identifiers, two references and pivot identifier), four sign bits and two kind bits, totaling at most 7(2L+1)+6<=64L. The smaller initial and extension records satisfy the same bound. Headers and original unit clauses are also charged. The conservative full bound is

T<=128(R_*+n+3)L.

Hence T=O((n+m) log(n+m+2)). The degree bound gives 2m=sum_v deg(v)<=Delta*n, yielding O_Delta(n log(n+2)) for fixed Delta. Enumeration, topological value computation, clause normalization of width-three clauses and writing all records take polynomial time in n+m and their binary descriptions. This is a construction from a supplied graph, not an algorithm selecting an expander family.

**Apply the existing representation bound, with its scope unchanged.** A representation of h by dense deterministic OBDDs in one common permutation of the n original variables, with F₂ sum equality on every assignment, is a representation of f_G by the all-assignment identity already proved. All L030 hypotheses therefore hold for that graph and representation, and its conclusion is W>=2^(c n) for the stated fixed c. Both signs of the derived h unit lead to the same positive root function f_G; the representation claim concerns h, not its negation. The bound is imported from L030, which records its graph and disjointness-rank sources, not rederived here. For each fixed exponent e and any such unbounded supplied family, T<=C_Delta*n log(n+2) implies 2^(c n)/T^e tends to infinity. There is no assertion that arbitrary changing epsilon or Delta preserve a fixed exponential constant, or that a uniform graph-selection algorithm has been supplied.

**Limits and verification.** The all-assignment induction, explicit resolution cases, ancestry induction and full-bit bound verify the construction for every graph satisfying the hypotheses, including m=1 whenever it satisfies them. No numerical or finite-check evidence replaces these arguments, and no mathematical script is needed for this step. The original pair (ell_1),(NOT ell_1) has an immediate resolution refutation. Under the F₂ clause-polynomial convention its two falsity polynomials sum to (1+x_1)+x_1=1, regardless of their order, giving the three-node tree certificate t_(ell_1)+t_(NOT ell_1). Thus another proof can avoid every hard extension. Common-order dense atomic sums for this supplied proof are obstructed; different-order sums, arbitrary reduced circuits, general reduced-data existence, tree conversion, hardness of every certificate and decision transfer remain independent unresolved questions. This is neither an UNVERIFIED CANDIDATE for P versus NP nor a verified global lower bound.

**Separate critical audit, 2026-10-06.** The preexisting SPECIALIZE assessment `drafts/literature/2026-10-06-expander-predicate-er-ancestry-audit.md` covers this REPRODUCTION audit. The statement, argument, constants and direct mathematical inputs are unchanged. The checks below make the reference and encoding obligations explicit; they are not a new lower bound or a reproof of the imported graph/rank theorem.

Singleton expansion is applicable at n=2 as well as larger n, so every vertex has a neighbor and m>=1. Every x_i occurs as an original unit, irrespective of the edge enumeration. Circuit definitions contain no substitution of these units: their unique recursively extended values are defined on every assignment, including those falsifying F. The conjunction induction therefore identifies the positive variable h with f_G, while s_sigma selects only the sign of its derived unit. A negative eta_K never replaces the represented function by 1+f_G.

For a signed literal a, resolving (NOT z OR a) with (NOT a) leaves exactly (NOT z). In the true branch with distinct underlying operand variables, the first resolution of (z OR NOT a OR NOT b) with (a) leaves (z OR NOT b); the second leaves (z). Equal operands instead give the normalized clause (z OR NOT a) and one resolution. Complementary operands cannot both be true and are handled by the false branch. Freshness ensures z survives all these pivots. The two projection slots remain separate records when equal. In the accumulator, a_(k-1) and eta_k have distinct underlying variables, so both positive-chain resolutions are always valid. For sigma=0 the first third clause is (a_1 OR x_1 OR NOT eta_1), and its anchor premise is (NOT x_1); the first negative-chain projection is (NOT a_1 OR NOT x_1), with premise (x_1). Thus neither chain silently presumes a positive original anchor.

At m=1 there are just p_1 and h in the circuit. The h block is (NOT h OR NOT p_1), (NOT h OR NOT p_1), (h OR p_1). At s_0, a projection for p_1 with a negative endpoint unit gives (NOT p_1), which with (h OR p_1) gives (h). At s_1, the p_1 third clause and the two endpoint units give (p_1), which with either h projection gives (NOT h). Both use the stated normalized clauses. There are still K=2 accumulator steps and 4m=4 extensions. No empty conjunction or missing q gate is used.

For an explicit indexing check, first write the n+1 initial records in the displayed order. Let u_k in {1,2} be the number of resolutions used for the unit of g_k, and put

c_k=n+2+sum_(j<k)(3+u_j),       C=n+1+3K+sum_(j=1)^K u_j.

The three defining records of g_k have indices c_k,c_k+1,c_k+2. The following u_k records derive its unit, whose index is e_k=c_k+2+u_k. A first unit inference cites the relevant defining record and an original unit (index at most n) or an earlier gate unit e_j, j<k. If there is a second inference, it cites c_k+3 and the other already available operand unit. Topological gate enumeration ensures that every reference is strictly earlier. C is the final circuit record index.

The accumulator block k starts at b_k=C+6(k-1)+1. Its definitions occupy b_k,b_k+1,b_k+2. Record b_k+3 resolves b_k+2 with the preceding positive anchor unit (record 1 when k=1, otherwise b_k-2), leaving (a_k OR NOT eta_k). Record b_k+4 resolves that clause with e_k, obtaining (a_k). Record b_k+5 resolves projection b_k with the negative anchor unit (record n+1 when k=1, otherwise b_k-1), obtaining (NOT a_k). These references are all earlier, and their signed pivots are precisely the eliminated literals. The final record C+6K+1 resolves records C+6K-1 and C+6K. This order gives

R=C+6K+1=n+2+9K+sum_k u_k<=n+2+11K=R_*.

Starting at the final record and following these actual references reaches every b_k+4 and every e_k through the positive chain, every b_k+5 through the negative chain, and each corresponding defining clause used by those inferences. This establishes both promised ancestry properties for all 2K extensions. It does not merely place the definitions in an earlier, unused part of the proof. Unused individual projection slots are permitted.

For decoding a definition block, delete the literal NOT z from each of its first two projections. Freshness guarantees that the remaining singleton is exactly its signed operand, even if the two projections coincide. The recorded slots fix their order, and the third clause is checked against their normalized conjunction definition. Extension identifiers, slot bits and all actual proof references are therefore sufficient without an uncharged circuit description.

In the stated gamma encoding let L=ceil(log₂(R_*+2))>=1. Every integer field, including clause sizes and both formula headers, is at most R_*, so its length is at most 2L+1<=3L. A unit clause has two integer fields and one sign bit, hence at most 7L bits. The two F headers cost at most 6L and the proof-count header at most 3L. The earlier per-record bound of 64L includes a clause, kind bits and the appropriate inference metadata; a resolution record specifically costs at most 7(2L+1)+6<=27L. Thus a direct bound on all written data, including T's additive two bits, is

T<=2+6L+7(n+1)L+3L+64RL
 <=(64R_*+7n+18)L
 <=128(R_*+n+3)L.

This confirms the conservative advertised bound without omitting F, framing, signs, slots or references. There is no unfolding in either the record enumeration or the encoding. Finally 2m<=Delta*n gives the stated fixed-Delta asymptotics. Applying L030 uses exactly its finite simple graph, expansion, dense deterministic layering, one common order, F₂ sum and all-assignment equality hypotheses. Fixed epsilon and Delta keep c positive along an unbounded supplied family. The immediate opposing-unit refutation still prevents any conclusion about all proofs or all certificates. No mathematical script was needed for these all-size inference and accounting checks, and Mathlib coverage remains not checked.

## Mathlib

Coverage of the full ER embedding, signed-unit ancestry property and common-order sum specialization is **not checked**. No absence claim is inferred. Primary sources give the standard fresh signed-AND mechanism, L027 gives the local ancestry template, and L030 gives the restricted representation theorem with its precise citations. The local graph-specific implementation, both output signs and binary accounting require the applicability proof above; neither an inspected full-statement source match nor certified novelty is claimed.
