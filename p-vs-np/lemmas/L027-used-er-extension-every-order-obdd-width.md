# L027 — A genuinely used short-ER extension with every-order exponential OBDD width

## Hypotheses

Use the fresh acyclic signed-AND ER convention in [the refutation-system foundation](../foundations/05-refutation-systems-and-simulation.md): a fresh z iff (a AND b), for earlier signed literals a,b, introduces (NOT z OR a), (NOT z OR b), (z OR NOT a OR NOT b). Clauses are sets, retaining complementary literals and removing duplicates. Resolution has explicit earlier-premise references. Binary length charges every clause, literal, identifier and reference; put T=2+|F|+|pi|. Repeated gate operands are permitted by this convention.

The original variables of F are exactly x_1,...,x_n. An extension's Boolean value means its recursive definition on **every** assignment to these variables, not just satisfying assignments of F. Nonextension variables absent from F would be set to zero, as in L025/L026; our construction has none. A dense deterministic OBDD for an extension tests the original variables in a fixed permutation, with n nonterminal levels and two terminal values. Its width is the maximum number of states at a nonterminal level. Redundant tests are permitted and the diagram need not be reduced.

The imported primary input is Bollig–Löbbing–Sauerhoff–Wegener, *On the complexity of the hidden weighted bit function*, RAIRO Theoretical Informatics and Applications **33(2)** (1999), 103–115, DOI [10.1051/ita:1999108](https://doi.org/10.1051/ita:1999108), Definitions 1.1–1.2, Theorem 2.1(i) and Theorem 4.2, printed pp. 104–105 and 107–108; [primary journal scan](https://www.numdam.org/article/ITA_1999__33_2_103_0.pdf). For

HWB_n(x)=x_(sum_i x_i), with x_0=0,

Theorem 2.1(i) gives O(n)-size binary Boolean circuits, and Theorem 4.2 gives 2^(Omega(n)) deterministic OBDD node count in every variable order. Use only the qualitative lower bound: there are a>0 and n_0 such that every such diagram has at least 2^(a n) nodes for all sufficiently large n divisible by 10. Decreasing a absorbs any fixed leading constant. The source assessment read the relevant theorem and proof cases; its damaged numerical display is not reconstructed here. No exact finite threshold or optimal exponent is claimed.

## Conclusion

For every n>=10 divisible by 10 there is an explicitly constructible original width-one CNF F_n and a fresh-AND ER refutation pi_n, with

T_n=O(n² log(n+2)),

containing a positive extension h_n whose value on every original-variable assignment is HWB_n. Every introduced extension has a defining clause **and a derived signed unit value** in the actual inference ancestry of the final empty clause. In particular, h_n is an actual operand used in that ancestry. All hard-function inputs remain original variables under the outside-F-to-zero convention.

There is c>0 such that, for all sufficiently large members of this family, every dense OBDD for h_n in every original-variable order has width at least 2^(c n). Consequently no polynomial in T bounds L026's required common-order width on all supplied ER refutations, even under the stated ancestry restriction.

This is a reproduction and ER specialization of the known circuit/OBDD separation. The checked sources do not supply this exact ancestry construction, and no certified originality is asserted. It stops the universal small-OBDD premise for **supplied** proofs, not L026 on its promised class. It gives no hardness of alternative proofs, reduced data, trees, certificates or SAT decision. Indeed F_n has an immediate alternative refutation.

## Proof

**Retain all original inputs.** Set

F_n=(x_1) AND ... AND (x_n) AND (NOT x_1).

Thus F_n has n+1 width-one clauses and exactly n distinct original variables. The hard extension is evaluated on all assignments to these variables; original unit clauses do not replace their recursive values by constants. The unsatisfiability of F_n therefore does not make the all-assignment promise vacuous. Only original variables and introduced extensions occur anywhere in the proof.

**An explicit signed-AND implementation.** Although the cited Theorem 2.1(i) gives the stronger linear binary-circuit bound, its constant-basis implementation need not be recovered for this polynomial target. We use the following fully specified quadratic weight-counter implementation to fix every gate and sign. This is an encoding specialization; it neither reproves the source's linear bound nor its lower bound. Uniform gate enumeration and the ER references below require an actual local signed-AND description.

Introduce z_0 iff (x_1 AND NOT x_1), whose all-assignment value is zero. Represent zero by the literal z_0 and one by NOT z_0; no special constant gate or new original input is needed. Let E_(0,0)=NOT z_0, and let missing E_(i,j), including negative j and j>i, denote z_0. For i=1,...,n and j=0,...,i, introduce three fresh gates, in this order:

u_(i,j) iff (E_(i-1,j) AND NOT x_i),
v_(i,j) iff (E_(i-1,j-1) AND x_i),
w_(i,j) iff (NOT u_(i,j) AND NOT v_(i,j)),
E_(i,j) := NOT w_(i,j).

The E symbols are aliases for signed literals, not additional variables or definitions. Induction on i proves that E_(i,j) is true exactly when the first i inputs have weight j: the two branches describe x_i=0 and x_i=1, respectively, and NOT w is their disjunction by De Morgan's law. The base i=0 and out-of-range values are correct. Every operand is an original variable or a signed earlier gate, so freshness/topological legality is explicit.

For j=1,...,n introduce t_j iff (E_(n,j) AND x_j). Their disjunction is HWB_n: at weight zero every term is false, while at positive weight j only E_(n,j) can hold and its term has value x_j. Implement the disjunction successively: start with the alias r_1=t_1; for j=2,...,n introduce d_j iff (NOT r_(j-1) AND NOT t_j), and let r_j=NOT d_j. Finally introduce h iff (r_n AND r_n), so the hard value has a **positive extension-variable root**. It equals HWB_n on every Boolean assignment.

Enumerate all these positive gates as g_1,...,g_G in their construction order, including z_0 and h. The exact count is

G=1+3 sum_(i=1)^n(i+1)+n+(n-1)+1=(3n²+13n+2)/2.

There is no need to eliminate gates that are redundant on the all-one assignment: the next construction uses every one explicitly. On that assignment h=1, since the weight is n and x_n=1.

**Derive each gate's true signed unit.** Let epsilon_k be the signed literal g_k if its value on the all-one assignment is one, and NOT g_k otherwise. The original positive units supply the true sign of every original variable. Process circuit gates in topological order, introduce their three defining clauses, and derive epsilon_k as follows for z iff (a AND b).

If a and b both have value one, the previously derived units a,b resolve with (z OR NOT a OR NOT b) to give (z), using at most two resolutions. If a=b, remove its single opposite literal in one resolution; the second resolution is unnecessary. Previously derived units can be negative literals when the operand sign is negative.

If at least one operand has value zero, choose such an operand a (or b). Resolve (NOT z OR a) with the previously derived unit (NOT a), yielding (NOT z); use the second projection when b is chosen. This uses one resolution. Complementary operands cause no problem: they cannot both be true, and the selected projection is valid.

Each epsilon_k has thus been derived using a defining clause of its own gate, with at most two resolutions, and only earlier gate units or original positive units. All definitions and all proof clauses have width at most three.

**Force genuine ancestry for every definition and the hard output.** Introduce a second list of G fresh gates a_1,...,a_G, using the alias a_0=x_1:

a_k iff (a_(k-1) AND epsilon_k), for k=1,...,G.

Derive (a_k) by resolving its third defining clause against (a_(k-1)) and (epsilon_k), in two steps, starting with the original (x_1). These operands have distinct underlying variables. Also derive (NOT a_k) by resolving its first projection (NOT a_k OR a_(k-1)) against (NOT a_(k-1)), starting with the original (NOT x_1). Finish by resolving (a_G) against (NOT a_G).

The derivation of (a_G) has, recursively, every positive accumulator unit and every epsilon_k as ancestors. Each epsilon_k has a defining clause of g_k as an ancestor. Each accumulator third defining clause is itself an ancestor. The negative chain also uses the first projection of every accumulator definition. Hence every introduced extension has a defining clause and its derived signed unit in the final ancestry. Some other individual defining clauses are unused, as permitted by the three-clause extension convention; there are **no unused extension definitions**. The hard output's literal epsilon_G=h is an operand of a_G and its derived unit is a direct premise on that positive derivation. This is stronger than merely writing a hard circuit next to an unrelated refutation.

The accumulator is only an ancestry device; no claim that its function is HWB is needed. The hard extension h remains exactly HWB on all original assignments, including assignments violating F_n. Every accumulator definition is acyclic and fresh. This meets the stipulated syntactic/semantic participation test, even though the chosen CNF also has a much shorter proof.

**Full binary length.** There are 2G introduced extensions and 6G defining clauses. There are at most 2G circuit-unit resolutions, 2G positive accumulator resolutions, G negative accumulator resolutions, and one final resolution. Together with n+1 original initial records, the record count R satisfies

R<=11G+n+2=O(n²).

All clauses have at most three literals, variable identifiers are at most n+2G, and references are at most R. Dense enumeration therefore gives O(log(n+2)) bits per identifier/reference, constant records of metadata per inference, O(n log(n+2)) original CNF bits, and O(n² log(n+2)) proof bits. The algorithm enumerates polynomially many gates and records and computes their all-one values topologically, so has polynomial running time too.

For a concrete encoding used in the finite certificate, gamma-code every nonnegative integer k by the Elias gamma code of k+1, of length 2 floor(log₂(k+1))+1. Prefix each clause with its size, and each literal with one sign bit and its absolute variable identifier. Encode F by n, clause count and all clauses. Encode pi by record count and, per record, a two-bit kind, its clause, and either its initial-clause index; or extension variable and two-bit definition slot; or two premise references and signed pivot. The three extension clauses recover the operands without separate gate descriptions. With R_* =11G+n+2 and L=ceil(log₂(R_*+2)), all integer labels are <=R_*, each record costs at most 64L bits, and the headers and original clauses fit the conservative explicit bound

T<=128(R_*+n+3)L.

In particular this full-bit bound is polynomial in n, without unfolding circuits or suppressing identifiers and references.

**Import node hardness and specialize to dense width.** Fix **any** permutation of the n original variables and any dense diagram for h in that order. It computes HWB_n on all assignments. By the cited Theorem 4.2 its total node count is at least 2^(a n) for all sufficiently large members of our divisible-by-ten family. A dense diagram of width w has at most nw nonterminal states and two terminals. Consequently

nw+2>=2^(a n), so w>=(2^(a n)-2)/n.

For sufficiently large n this is at least 2^(a n/2): equivalently 2^(a n/2)-2^(1-a n/2)>=n, which holds because exponential growth dominates n. Set c=a/2. Skipped tests, if initially allowed, can be made redundant dense tests; the resulting diagram is still an OBDD to which the same node-count theorem applies. No reduced-diagram assumption, exact cut constant, or new OBDD lower-bound proof is used.

For any common order supplied for all extensions, its h diagram already requires this width. For each fixed polynomial exponent e, the upper bound T=O(n² log(n+2)) implies 2^(c n)/T^e tends to infinity along the family. Thus the required width is not bounded by any fixed polynomial in the full supplied ER length. This is exponential in n, rather than merely exponential in log T.

**Limits and finite verification.** Resolving original (x_1) and (NOT x_1) immediately refutes F_n. It therefore has other short proofs that contain no hard extension. Its original clause placeholders already give a three-node arithmetic tree certificate t_(x_1)+t_(NOT x_1): at the original clause axioms it is (1+x_1)+x_1=1 over F₂ and at zero placeholders it is zero. This observation needs no lemma input and explicitly separates supplied-proof hardness from optimal-certificate hardness. L025's arbitrary reduced representatives/witnesses are not lower-bounded by OBDD hardness; L026 is only one way to provide them. Tree conversion, every-certificate hardness, unrestricted ER lower bounds and decision transfer remain open.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/used-extension-obdd/check_embedding.py`. The independent checker validates fresh definition blocks, every resolution and reference, width-three bounds, original-variable retention, and defining-clause **and signed-unit** ancestry of every extension for n=2,4,6,10,20,40. It also exhaustively checks the HWB root on all assignments for n=2,4,6; the all-n induction above establishes general correctness. A corrupted final resolvent is rejected. Complete gates, clauses, inference references and small all-assignment evaluations are saved in `scripts/used-extension-obdd/embedding-results.json`. For n=40 there are 5,322 introduced extensions, all used, and 27,551 records, with actual T=2,557,576 bits versus the explicit bound 56,363,520 bits. These finite checks do not establish the asymptotic OBDD bound; that bound is the precisely cited primary theorem and dense-level counting specialization.

## Mathlib

Coverage: **not checked** for the full HWB circuit/OBDD theorems, ER ancestry embedding or dense-width specialization. The primary source supplies the binary-circuit upper bound and every-order OBDD node-count lower bound, not the exact ER construction. No Mathlib absence or certified novelty is inferred. The local signed-AND implementation, ER inferences, ancestry and full-bit accounting are written above; L025/L026 give receiving conventions and L019 is only an optimal-certificate/ancestry contrast, not a mathematical premise of this construction.
