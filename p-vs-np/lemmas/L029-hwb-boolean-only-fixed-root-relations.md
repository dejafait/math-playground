# L029 — Boolean-only relations for the fixed HWB representatives

## Hypotheses

Use exactly L028's representatives, abstract signed nodes and designated ordered operands for L027's family, with n>=10 divisible by 10. Write G=(3n²+13n+2)/2, S=2n+4G+2 and T=2+|F_n|+|pi_n| as there. In particular the selector roots are the unchanged products T_j=q_(n,j)x_j, the disjunction roots use R_j=sum_(l<=j)T_l, and the accumulator roots are the unchanged prefixes P_m=x_1...x_m with L028's cutoff rule. All original inputs remain free.

Work over the free noncommutative F₂ ring with independent variables x_1,...,x_n and placeholders b_i,c_ij (i<j), substituted respectively by x_i²+x_i and x_i x_j+x_j x_i. Denote this substitution by A_B. No original-clause placeholder is allowed in the witnesses. Circuits are division-free fan-in-two DAGs; degree is measured before substitution, counting each independent placeholder as degree one. Full supplied-data length E has L025's separately rooted encoding convention.

## Conclusion

For every positive reduced AND node i with its actual signed operands a,b, one can construct H_i using only these Boolean and pair-once commutator placeholders such that, as formal identities,

H_i(x,0)=0,                 H_i(x,A_B)=r_i+r_a r_b.

The supplied roots r_v are unchanged. They and these witnesses satisfy

d=n+1,                 h=3n,                 E=O((n+2)^9 log(n+2)).

A common arithmetic DAG has O((n+2)^7) gates. All data are constructible in polynomial time in n and hence in T. The degree bounds also bound the written circuits syntactically. Adding unused original-clause axiom entries to the framing gives precisely the data required by L025, with no use of those clauses in H_i.

This strengthens only the local relation input for this particular supplied-proof family. It neither supplies general reduced ER data nor converts circuit certificates to trees, excludes every certificate, or transfers proof hardness to SAT decision time. It is not a P-versus-NP candidate. The source assessment established no full matching result, which does not certify originality.

## Proof

**Previously proved local correction, with its scope retained.** Use only the local paired-suffix construction in L026, Proof equations (4)–(9), and its increasing-multilinear injectivity argument. For two explicitly layered Boolean diagrams D,E in order x_1,...,x_n with width at most w, let f_D,f_E be their ordered suffix representatives. Its local construction gives an increasing multilinear product representative p_DE and a witness W_DE such that

W_DE(x,0)=0,                 W_DE(x,A_B)=f_D f_E+p_DE.       (1)

The polynomial p_DE computes the pointwise product on the Boolean cube. Its syntactic degree is at most n; W_DE has syntactic degree at most 2n-1. These local identities are proved before L026 identifies a diagram for an extension output, and do not require an OBDD for that output or for any sum of functions. This is an application of those local identities, not L026's global promised-class conclusion.

For precision, with e_0=1+x_k,e_1=x_k, child representatives u_0,u_1,v_0,v_1, earlier-variable commutator witnesses K_(u_a,k), and children W_00,W_11, the correction used is

(e_0 K_(u_0,k)+e_1 K_(u_1,k))(v_0+v_1)
 +b_k(u_0+u_1)(v_0+v_1)+e_0 W_00+e_1 W_11.

The Boolean factor stays in its displayed position. The terminal correction is zero and the terminal product is the product of the two scalar labels. The K recurrence is L026 (6), with only original pair placeholders, including its suffix/earlier-variable restriction. Thus (1) includes repeated or constant operands, and uses no quotient simplification or new axiom. For A diagrams, all their K tables cost O(A(n+1)²w), and all ordered diagram-pair tables cost O(A²(n+1)w²), with constant gates per entry. Distinct pairs share only previously constructed suffix values and K roots; there is no product of state spaces across successive extensions.

The inspected primary supporting sources are Forbes–Shpilka–Tzameret–Wigderson, *Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10) (2021), Propositions 4.5–4.6, pp. 30–32, https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf, and Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, Lemmas 3.6–3.7, pp. 17–18, https://arxiv.org/pdf/1412.8746v4. The former is commutative roABP correction; the latter is ordered formula commutation. Neither is invoked as a full match for this shared fixed-root construction. L026 supplies the already justified local specialization; no source theorem is reproved here. The new applicability work is the atomic decomposition, bridges to the fixed roots, and full accounting below.

**A polynomial list of small atomic diagrams.** Use the following atoms, all in the single order x_1,...,x_n:

- constants 0,1 and original variables x_l;
- q_(i,j) for 0<=i<=n, 0<=j<=i, and one zero atom for out-of-range indices;
- U_(i,j)=q_(i-1,j)(1+x_i) and V_(i,j)=q_(i-1,j-1)x_i for each counter cell;
- the Boolean function s_j=[the full weight is j AND x_j=1], for 1<=j<=n.

The notation for an atom below denotes its ordered diagram polynomial f_D. The counter polynomials q,U,V are already increasing multilinear: their defining recurrence appends a variable strictly later than every preceding variable. They compute the displayed weight/literal predicates by L028. Hence their diagram polynomials equal the fixed arithmetic polynomials formally, by L026's injectivity on increasing multilinear words. This use of injectivity does not apply to T_j itself. Prefix P_m is formally q_(m,m) by the boundary recurrence; original variables and constants agree with their diagram polynomials by the same injectivity (or direct cancellation).

Here are explicit diagrams and width bounds, so no small-diagram premise is assumed. For a weight condition on the first t inputs, retain the partial count until x_t and freeze it thereafter. If there is an additional literal x_l=epsilon, send a mismatching branch at its query to a rejecting state. All other states keep the count; an already mismatching branch stays rejecting. At the final level accept just the requested count and nonrejection. This gives at most n+2 states per nonterminal level. It covers q_(i,j), U,V (weight t=i-1 and the literal at i), and s_j (weight t=n and literal at j). An impossible weight condition uses the constant-zero diagram. Constants have width one; a single literal uses two states, with redundant queries filling every level. Every diagram has n explicit nonterminal levels and terminals 0,1; count and rejection determine the successors uniformly in polynomial time. There are A=O((n+2)²) atoms, each of width w<=n+2. Their full description costs O(A(n+1)w log(n+2)). No diagram for R_n or HWB_n is built or presumed small.

**Bridges for the appended selectors.** Apply (1) to the q_(n,j) atom and the x_j atom. Its p has exactly the Boolean function s_j. Both p and the s_j atom polynomial are increasing multilinear, so p=s_j formally. Put D_j=W_(q_(n,j),x_j). Then

D_j(x,0)=0,                 D_j(x,A_B)=T_j+s_j,           (2)

deg D_j<=2n-1. In particular the originally appended x_j keeps its position in T_j. The commutator and Boolean terms in (1), rather than Boolean agreement alone, supply its correction.

For every supplied positive or signed root r_v, define an auxiliary increasing multilinear sum s_v of atoms and a bridge D_v as follows. These auxiliary roots do not replace r_v.

- Constants, original variables, z_0, and positive counter u,v: take their identical atom (zero for z_0), and D_v=0.
- Positive w_(i,j): take s_v=1+q_(i,j), D_v=0.
- Positive t_j: take s_v=s_j and D_v=D_j from (2).
- Positive d_j: take s_v=1+sum_(l<=j)s_l and D_v=sum_(l<=j)D_l.
- Positive h: take s_v=sum_(l<=n)s_l and D_v=sum_(l<=n)D_l.
- Every positive accumulator assigned P_m: take s_v=q_(m,m), D_v=0. The alias a_0=x_1 follows the original-variable case.
- For every exact negative signed node, take s_(-v)=1+s_v and D_(-v)=D_v.

These cases give, formally and independently of Boolean evaluations,

D_v(x,0)=0,                 D_v(x,A_B)=r_v+s_v.           (3)

For sums this is distributivity over F₂ and (2); for negative nodes the two constant ones cancel. Represent the sums as lists with F₂ coefficients, cancelling repeated constant entries. Each list has at most n+1 atoms. The list for zero can be empty. All s_v are increasing multilinear of syntactic degree <=n, and all D_v have syntactic degree <=2n-1. Root identities used for q,U,V and prefixes hold as polynomials even when their arithmetic DAG identifiers differ. No witness for an arbitrary Boolean-equivalent circuit is assumed.

**Correct each actual local product.** For an actual reduced AND node i, expand the two atom lists for its designated signed operands a,b by distributivity. Sum the pair witnesses (1), with their F₂ coefficients, in that order of operands. Call this sum W_ab, and call the corresponding sum of p_DE outputs p_ab. Then formally

W_ab(x,0)=0,                 W_ab(x,A_B)=s_a s_b+p_ab.     (4)

The polynomial p_ab is increasing multilinear and evaluates to the pointwise product of s_a and s_b. Equation (3) implies equality of their Boolean evaluations with r_a,r_b, since every substituted Boolean/commutator axiom vanishes there. L028's all-assignment invariant for the actual designated AND node gives r_i=r_a r_b on that cube. The same argument with (3) gives s_i=r_i there. Consequently p_ab and s_i agree on every assignment. Both are increasing multilinear, so L026's injectivity proves the **formal** identity

p_ab=s_i.                                                    (5)

This argument does not expand the atoms into monomials or compute an OBDD for their sum. Injectivity proves an identity between explicitly constructed circuits; it is not an algorithm for general identity testing.

Define the required witness with the following ordered coefficients:

H_i=D_i+D_a s_b+r_a D_b+W_ab.                                (6)

Every summand vanishes at zero placeholders. Substituting A_B and using (3)–(5) gives

(r_i+s_i)+(r_a+s_a)s_b+r_a(r_b+s_b)+(s_a s_b+s_i)
 =r_i+r_a r_b.

All cancellations are of identical words in the indicated positions. In particular there is no unrecorded swap of D_b or s_b and no dropped nonlinear correction. The use of r_a, rather than s_a, in the third term accounts for the entire bridge product exactly; no D_a D_b term is omitted.

**All signed gates and boundary cases.** Construction (6) is applied to all 2G positive extensions, with L027's actual operands, including z_0; every u,v,w cell; each t_j and d_j; the repeated-operand h; and every accumulator. All required signed nodes appear in (3). Out-of-range counter aliases use zero and E_(0,0) uses one; E_(i,j)=NOT w has normalized value q_(i,j). The repeated h operands both have list sum_j s_j and the same bridge, which (4) permits without alteration.

For the use of L028 in (5), its prefix invariant retains P_1 through z_0 and row 1. In row i>=2 it retains P_(i-1) until the negative sign of u_(i,i-1), then changes to P_i before v and w of that cell, and stays there through j=i. On the support of P_(i-1), earlier cells have all-one signs identically one, while that negative u sign equals x_i. After the transition the whole row is fixed to its all-one values. In the terminal t,d,h phase P_n fixes every input. Off the prefix support the product is zero. Thus every accumulator relation used in (5), including the cutoff and final phase, is exactly L028's proved all-assignment equality. This is not replacement of the original variables by unit-clause values: those values are used only under the indicated prefix support in that all-assignment proof. No clause axiom appears in (1)–(6).

**Degree and complete encoding.** Fixed r_v have syntactic degree <=n+1 by L028; s_v and p_ab have degree <=n. Every D_v and W_ab is a sum of degree-at-most-2n-1 witnesses. The four terms in (6) have degrees at most 2n-1, 3n-1, 3n, and 2n-1. Thus h=3n is a bound before substitution, without relying on cancellation. Fixed roots still have d=n+1.

With A=O((n+2)²), w<=n+2, construct all ordered atom pairs, even unused ones. The suffix values cost O(A(n+1)w), the K tables O(A(n+1)²w), and all pair-product/correction tables O(A²(n+1)w²). These are respectively O((n+2)^4), O((n+2)^5), and O((n+2)^7). All entries have constant fan-in cost and are acyclic in decreasing remaining suffix length. The original roots add O((n+2)²) gates. Bridges and normalized lists add at most O(S(n+1)) gates without exploiting prefix reuse. Each of 2G relations sums at most (n+1)² pair roots and adds the constant number of gates in (6), so this costs O((n+2)^4) more. Include the O(n²) placeholder leaves and every exact signed root. The entire common DAG therefore has N=O((n+2)^7) gates, with an absolute constant independent of n and extension depth.

There are B=S+2G=O((n+2)²) supplied representative/relation roots. Write each separately as its reachable DAG, with dense local gate numbers, gate tags, ordered operand labels, coefficient bits, original-variable/placeholder indices and a root header. Each costs O((N+1)log(N+n+S+2)) bits; this deliberately charges the whole common DAG per root. Include the topological S-node abstract table with actual signed operands and root associations, the original n-variable labels, the Boolean/pair-once axiom expressions, and (if framing L025's full axiom list) the unused n+1 original unit-clause entries. Those data have O((n+2)² log(n+2)) bits. The explicitly generated atom diagrams cost O((n+2)^4 log(n+2)), even if retained as extra construction evidence. Together these give

E=O(B(N+1)log(N+n+S+2)+(n+2)^4 log(n+2))
 =O((n+2)^9 log(n+2)).

All identifiers in this family are dense with polynomial range; none of the restored labels has uncharged length. The finite loops for diagrams, suffix tables, ordered pairs, lists and rooted outputs are polynomial. Ordered multilinear injectivity justifies the selected roots algebraically; the construction requires no expensive equivalence test. Since n<=T, these are polynomial supplied-data bounds for L025. L025 is used only for this final receiving conclusion, not to establish the local identities.

**Verification status.** The proof is the all-n construction above, using the already established local identities of L026 and all-assignment invariant of L028. The separate critical audit below found no substantive defect in this restricted statement; this is not a verified solution of the main problem. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/hwb-boolean-only/check_relations.py`. Its complete circuits, atomic diagrams, fixed and auxiliary root associations, atom lists, bridges, and all substituted relation/output word polynomials are saved in `scripts/hwb-boolean-only/relations-results.json`. The checker copies only the reachable x-only roots from L028's existing builder (rejecting any reached clause placeholder), builds the new diagram/pair/bridge witnesses, and compares exact noncommutative word sets without Boolean quotient reduction. It checks all 40 local relations and 84 signed bridges for n=2, and all 68 relations and 142 bridges for n=3. Both zero-placeholder identities, all ordered-output bridges and every full relation identity pass. The syntactic maxima are d=3,h=6 and d=4,h=9, meeting n+1 and 3n. Deleting the r_a D_b summand is rejected at 6 and 9 relations respectively.

The finite separately rooted padded encodings, including abstract/framing allowances, are 128,896 and 431,040 bits, below their full-common-DAG-copy ceilings 2,462,464 and 15,352,640 bits. These finite ceilings use each constructed DAG's actual node count; the asymptotic n^9 bound is the preceding all-n count, not a fitted estimate. The tests construct only needed pair states, which is a subset of the conservatively counted all-pair construction. Both test values lie outside the theorem's stipulated family; they test the same algebraic recurrences and boundary rules, not the every-order OBDD theorem. No large-n formal expansion, arbitrary identity verifier, or proof-assistant verification is claimed. The full all-n proof and its separate critical audit are distinct from these diagnostics.

**Separate critical audit, 2026-10-06.** The audit used the previously approved scope `drafts/literature/2026-10-06-hwb-boolean-only-critical-audit.md`. It found no substantive error and made no change to the construction or bounds. Here are the load-bearing checks, with L025's complete supplied-data convention retained.

For each atomic diagram, before the counted prefix ends the retained count has at most n+1 possible values; afterwards it is frozen. One extra rejecting state suffices for the literal mismatch, including when the literal lies inside the counted prefix. Thus the bound n+2 applies at every level, including redundant later queries and impossible weights. There are O(n²) counter atoms and O(n) selector/input atoms, independently of the number of assignments. U,V and q have increasing multilinear words by their appended-variable recurrence. The identity q_(m,m)=P_m follows from its zero boundary term and q_(0,0)=1. Neither this identity nor Boolean injectivity identifies T_j with its ordered atom without the explicit D_j bridge.

The pair recurrence uses K only for a child suffix and its strictly earlier queried variable; terminals use scalar products and zero corrections. In its four ordered branch cases, e_a e_b=delta_(a,b)e_a+(x_k²+x_k), with the Boolean factor remaining left of both suffix sums. This verifies the precise local applicability of L026, including equal, constant and complemented operand values. Sums of atoms use ordered pairs without requiring a diagram for the sum. F₂ cancellation of duplicate constant-list entries preserves both the represented polynomial and the bridge equation. Complementing a fixed root adds one to its auxiliary polynomial and leaves its bridge unchanged. Consequently both p_ab and s_i belong to the increasing multilinear subspace required for (5); the unnormalized r_i is never submitted to that injectivity claim.

The gate comparison covers z_0=(x_1 AND NOT x_1); the actual u,v,w operands with zero/one aliases at every boundary; t_j with its appended x_j; d_j with the negative preceding-disjunction and negative t_j operands; h with its repeated r_n operand; and every accumulator with its actual all-one signed gate literal. In the accumulator induction, x_1=0 makes the initial prefix zero permanently. If P_(i-1)=1, every j<i-1 cell has u=v=0,w=1; the sign of u_(i,i-1) is its negative and equals x_i on this support. The cutoff therefore precedes that cell's v,w, including the last j=i cell. For i=2 the earlier range consists just of j=0 and satisfies the same check. Row 1 already has x_1 fixed by P_1, and the terminal selector phase has every input fixed by P_n. These are restrictions inside an all-assignment case proof, not applications of original-clause axioms. The support-zero case completes each multiplication identity on the rest of the cube.

In (6), substitution yields two identical copies each of s_i, r_a s_b and s_a s_b, in exactly those orders, leaving r_i+r_a r_b. In particular r_a D_b includes the whole second bridge contribution; replacing it with s_a D_b would not justify the displayed cancellation. Each term separately has a zero-placeholder factor. The syntactic degree maxima are still n+1 for fixed roots, n for auxiliary values, 2n-1 for bridges and pair witnesses, and 3n for H. Padded diagrams may have larger syntactic degree than their simplified constant polynomials, but the already charged n-level bound covers that difference.

All K entries are indexed by one diagram state and an earlier input, and pair entries by two states at one level. Their dependency arrows go to strictly shorter suffixes, so bottom-up construction terminates; the pair tables are never fed back as new atomic diagrams. Thus A=O(n²) and w<=n+2 give O(n^7) common gates with a constant amount of work per entry. Lists of length at most n+1 and the O(n²) actual definitions add only O(n^4) gates. The O(n²) representative/relation outputs are separately charged at the entire common DAG size, with O(log(n+2)) bits per dense label. Abstract signs, operand/root associations, Boolean/commutator and unused clause framing, and even retained atomic diagrams fit the separately stated allowances. This verifies E=O((n+2)^9 log(n+2)) as a full encoding bound. L025 is used only after these premises are established. The direct mathematical inputs in DAG.md remain unchanged.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/hwb-boolean-only/audit_relations.py` to reproduce the finite audit supplement. It regenerates both complete cases, compares every circuit, diagram, root, bridge, atom list and expanded word polynomial with the entire existing certificate, and preserves that original file. The complete regenerated cases and individual audit checks are saved in `scripts/hwb-boolean-only/audit-results.json`, with the source certificate hash. All 108 relations, 226 signed bridges, ordered-output identities, degree/width/encoding checks and 15 bridge-deletion rejections agree; no failures occurred. This replay does not independently validate the common builder or establish the all-n theorem. The preceding informal audit supplies the all-n check. The outcome is reproduction/verification evidence for this local input, not a new theorem, certified novelty or a main-problem candidate. General reduced ER data and all downstream gaps in the Conclusion remain open.

## Mathlib

Coverage of this full fixed-root Boolean-only construction is **not checked**. This is not evidence of absence. L026 is the canonical local paired-suffix/injectivity input; L028 supplies the unchanged representatives and signed all-assignment invariant; L025 supplies the receiving data conventions and conditional propagation. The primary supporting citations above have the restricted scopes recorded in the preexisting EXPLORE assessment `drafts/literature/2026-10-05-hwb-boolean-only-relations.md`. No new full theorem import, general efficient multilinearization assertion, or certified novelty is claimed.
