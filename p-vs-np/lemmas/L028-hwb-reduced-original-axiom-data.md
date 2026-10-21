# L028 — Reduced original-axiom data for the used HWB ER family

## Hypotheses

Take exactly the CNF F_n, signed-AND gate enumeration and ER refutation pi_n of L027, for n>=10 divisible by 10. In particular F_n consists of the positive units (x_1),...,(x_n) and the negative unit (NOT x_1). Put T=2+|F_n|+|pi_n| with its full binary conventions. There are G=(3n²+13n+2)/2 counter/selector gates g_k, including z_0 and h, followed by G accumulator gates a_k. Their operands and construction order are those of L027; changing their order is outside this statement.

Use L025's abstract value DAG, exact signed nodes, shared fan-in-two division-free arithmetic circuits and supplied-data parameters E,d,h. Work in the free noncommutative polynomial ring over F₂ on all original x_1,...,x_n and independent placeholders for L020's original clause, Boolean and pair-once commutator axioms A(x). Do not restrict witnesses to Boolean/commutator placeholders. All original variables retain their values on every Boolean assignment, including assignments violating F_n.

## Conclusion

One can construct faithful all-assignment representatives and exact signed nodes for **every** extension and operand of this supplied proof, together with every required local relation witness H_i, satisfying formally

H_i(x,0)=0,                 H_i(x,A(x))=r_i+r_a r_b.

With S the number of abstract nodes, the complete supplied data admit

S=2n+4G+2,                 d=n+1,                 h=2n+3,
E=O((n+2)^4 log(n+2)).

The E bound permits each representative and each witness to be written as a separate rooted DAG, with all root associations, abstract operands and the full original axiom list charged. Construction time is polynomial in n and T. These premises therefore instantiate L025 with polynomial complete size and degree in T, on this OBDD-hard supplied-proof family.

This is a family-specific reduced representation, using F_n's easy original-clause contradiction. It neither bounds Boolean-only relation witnesses nor supplies data for arbitrary ER proofs. It gives no tree conversion, all-certificate hardness, efficient identity verifier, ER lower bound or SAT decision transfer. It is local progress beyond the full matches established by the recorded source comparison, with no certified originality or P-versus-NP candidate claimed.

## Proof

**Counter representatives and characteristic two.** Set q_(0,0)=1 and every out-of-range q_(i,j)=0. For 1<=i<=n and 0<=j<=i, construct shared roots

U_(i,j)=q_(i-1,j)(1+x_i),
V_(i,j)=q_(i-1,j-1)x_i,
q_(i,j)=U_(i,j)+V_(i,j).

Products have precisely the displayed order. Assign the positive extension representatives r_z0=0, r_u=U, r_v=V and r_w=1+q_(i,j). The signed alias E_(i,j)=NOT w consequently has representative 1+r_w=q_(i,j) as a formal free-ring identity. The base E_(0,0)=NOT z_0 is exactly 1, and the missing aliases are exactly 0. These statements about signed values use 1+(1+q)=q in F₂, without swapping any factors.

On a Boolean assignment, induction shows that q_(i,j) is 1 exactly when the first i bits have weight j. For x_i=0, U equals q_(i-1,j) and V=0; for x_i=1, U=0 and V equals q_(i-1,j-1). Thus the sum is the disjunction of the two exclusive branches, with values only 0 or 1, also in characteristic two. Accordingly 1+q agrees with the actual AND (NOT u AND NOT v) on every assignment. The positive z_0 also agrees with x_1 AND NOT x_1. Degree induction gives deg q_(i,j), deg U_(i,j), deg V_(i,j)<=i. This is an ordered circuit construction, not generic multilinearization or an equality of r_w with its operand product in the free ring.

**Selectors and successive disjunctions.** Put

T_j=q_(n,j)x_j,             R_j=sum_(l=1)^j T_l.

Use r_tj=T_j, r_dj=1+R_j for 2<=j<=n, and r_h=R_n. The alias r_1 of L027 has value T_1, and the later signed aliases NOT d_j have exactly value R_j. On an assignment of weight k>0, only q_(n,k) is nonzero, so at most one T_j is nonzero. At weight zero every T_j is zero. Hence R_j equals the actual successive disjunction of t_1,...,t_j over F₂; d_j equals the actual AND of their two negative operands; h's repeated AND has Boolean value R_n. All these statements hold on every assignment. The formal degrees are at most n+1, even though T_j may repeat x_j in its words. No ordered-multilinear or reduced Boolean quotient promise is needed by L025.

The assessed Onaka–Nakamura–Nishino–Yasuda result (*Tensor Decomposition Meets Knowledge Compilation*, AAAI 39(14), 2025, Proposition 1/Lemma 5, pp. 15114–15115, [primary PDF](https://ojs.aaai.org/index.php/AAAI/article/download/33657/35812)) is a supporting alternative HWB tensor representation, not an input to this counter construction. No tensor-core reduction modulo two, tensor rank claim, sharper source size bound or long-product closure is imported. The justification for writing this family-specific specialization is that the source does not supply L027's individual counter gates, ancestry accumulator or free-ring relation witnesses. L027's explicit Boolean recurrence fixes those gates, and the exclusive-case argument above supplies the necessary F₂ arithmetic specialization directly.

**All-assignment accumulator invariant.** Write P_m=x_1 x_2 ... x_m in this fixed order. Let epsilon_k be the true-on-all-one sign of g_k as in L027. Assign each accumulator a_k a prefix representative according to the following rule. Start a_0 with P_1. Processing z_0 retains P_1. Every gate of row i=1 retains P_1. For a row i>=2, retain P_(i-1) through all gates before u_(i,i-1); at that u gate change the prefix to P_i, and retain P_i for the rest of the row. After row n, retain P_n through every t_j, d_j and h. These are aliases to shared prefix roots, not new formal products of all preceding epsilon values.

Here is a proof for all assignments. Multiplication by any Boolean literal leaves an accumulator that is zero at zero; thus, if its current value is the prefix conjunction P_m, it suffices to evaluate the next sign on assignments satisfying that prefix. For z_0 the sign is NOT z_0 and is always 1. During row 1 the prefix already fixes x_1=1, so every row-1 gate has its all-one value and its chosen sign is 1.

For row i>=2, on P_(i-1)=1 the preceding counter row is fixed: q_(i-1,j)=1 exactly for j=i-1. Therefore U_(i,j) is zero except for j=i-1, where it is 1+x_i, and V_(i,j) is zero except for j=i, where it is x_i. For j<i-1, the actual gate values are u=v=0 and w=1 regardless of x_i. Their all-one signs are NOT u, NOT v and w, each equal to 1, so the prefix stays P_(i-1).

At u_(i,i-1), the actual value on that prefix is 1+x_i and its all-one value is 0. Its sign NOT u is therefore x_i on the prefix. Multiplying the accumulator changes its Boolean value to P_i. The two remaining gates at j=i-1 and all three gates at j=i now have the first i bits fixed to 1. Thus they have their all-one values (later inputs are absent from this row), and their signs are 1. The prefix stays P_i. This exhausts the row, including its j=i boundary and every zero/out-of-range operand. Induction proves the stated prefixes for all counter gates. Afterwards P_n fixes every original input to 1, so every selector/disjunction/h sign is 1 on its support, and the accumulator stays P_n. Outside its current prefix it is zero and cannot become nonzero by a later multiplication. This proves equality on every assignment for every a_k, not merely agreement at the all-one assignment. Prefix degree is at most n and its shared construction costs n-1 multiplications.

**Abstract nodes and exact signs.** Take n original-variable nodes and two constant nodes, then, immediately after each base variable or each positive extension node, an exact signed node whose root is 1 plus that positive root. This is a topological abstract order: the n originals and their signs precede all extensions, and both signs of every earlier extension precede the next definition. Each positive extension is a reduced AND node with its actual two designated signed operands. A positive accumulator representative is the assigned P_m, not the product of the previously supplied roots. The q and R arithmetic gates internal to representatives need not be abstract nodes. There are n+2G positive nonconstant nodes, their n+2G sign nodes and two constants, giving S=2n+4G+2. Every abstract root has formal degree at most d=n+1. If two roots represent the same polynomial, they still have their distinct explicitly encoded abstract associations. No original variable is replaced by a constant.

**Exact local witnesses using original clauses.** Let tau_+ be the placeholder for (x_1) and tau_- the placeholder for (NOT x_1). In the original axiom convention, their substituted values are 1+x_1 and x_1. The existing L027 original-CNF certificate

J=tau_++tau_-

satisfies J(x,0)=0 and J(x,A(x))=(1+x_1)+x_1=1 **formally** in the free ring. For each reduced AND node, including z_0, all counter/selector/h nodes and all accumulator nodes, put

delta_i=r_i+r_a r_b,                 H_i=delta_i J.

This uses right multiplication in exactly the displayed order. At zero placeholders H_i=delta_i 0=0. After axiom substitution H_i=delta_i 1=r_i+r_a r_b. These are identities for unrestricted formal x, with no Boolean-cube inference, commutation, division or omitted correction. Sign nodes are exact formal complements and need no H. Since deg delta_i<=2d and deg J=1 in independent x,t, every H_i has full pre-substitution degree at most 2d+1=2n+3. Each local witness adds one product for r_a r_b, one sum and one product with J. Cancellation may lower this bound but is not needed. This is an application of the already recorded easy certificate to a bounded local relation, not an exact lift from any unreduced value and not a reproof of a general correction theorem.

**Full encoding and construction cost.** Let C=sum_(i=1)^n(i+1)=(n²+3n)/2. In one common arithmetic DAG, include n inputs, two constants, two original-clause placeholders and J. Original-input signs cost n sums. Each counter cell costs at most four arithmetic gates for U,V,q and 1+q. The selectors cost n products and n-1 prefix sums; their d roots cost n-1 sums. Prefix conjunctions cost n-1 products. Additional exact signed roots for all positive extensions cost at most 2G sums, even if already available complements are duplicated. All 2G local witnesses cost at most 6G gates. The positive z_0,h and accumulator roots are aliases already available. Thus the total N is bounded by

N<=4C+8G+6n+5<=100(n+2)².

The bound deliberately allows redundant gates; in particular no cancellation algorithm or exponentially unfolded expression is required. The axiom list has n+1 clauses, n Boolean entries and n(n-1)/2 pair entries, with expressions of degree at most two and constant size. Including it separately costs O((n+2)² log(n+2)) bits with the dense original identifiers of this family.

For explicit rooted encoding, take L=ceil(log_2(100(n+2)²+2)). Tag every arithmetic record with three bits and give up to two L-bit gate/input labels, or an L-bit original/placeholder label for leaves; a constant leaf includes its coefficient bit. Include gate count and root label. Even padding every record and header to 16L bits encodes any single rooted DAG in at most 16(N+1)L bits. There are B=S+2G=2n+6G+2 supplied representative/relation roots, and B<=20(n+2)². Writing every root separately, including all its reachable ancestors, therefore costs at most 16B(N+1)L bits. The abstract records give their kind, label, operand labels and corresponding root association, at O(SL) additional bits; the full axiom list and placeholder associations cost O((n+2)²L). Constants, original identifiers, signs, framing, root labels and operands are all included. Consequently E=O((n+2)^4 log(n+2)), even without sharing across separately supplied roots. This is a bound on actual complete encodings, not just on internal node counts or semantic degrees. Root extraction and dense renumbering take polynomial time within the same bound.

The supplied proof has n original inputs and O(n²) explicitly written gates. In particular n<=T, and all displayed S,d,h,E bounds are polynomial in T. L025 applies to the formally established local relations and these exact signs; it constructs a polynomial-degree, polynomial-full-size original-axiom circuit certificate. This consequence does not identify that circuit with L021's original high-degree output or make it a tree. F_n itself already has J as a constant-size tree certificate, so success says nothing about optimal certificate hardness.

**Verification.** The meaningful finite tests and full certificates are recorded by `PYTHONDONTWRITEBYTECODE=1 python3 scripts/hwb-reduced-data/check_data.py` in `scripts/hwb-reduced-data/data-results.json`. The checker compares every representative, including every accumulator, against L027's actual signed-AND definitions on all assignments for n=2,4,6; it checks complete local free-word witness identities for n=2, and structural size/degree/encoding bounds for n=10,20,40. Corrupting the accumulator cutoff and omitting one original-clause term from J are tested. These finite checks supplement the all-n case proof and explicit bounds above; they neither prove an asymptotic OBDD theorem nor verify a general research candidate.

The separate critical audit of 2026-10-05 found no substantive error. It checked row 1 under the initial P_1 condition, the empty early range at i=2, the cutoff before v and w at j=i-1, the last j=i cell, and the terminal t,d,h phase. If x_1=0 every accumulator is zero; a first zero at i>=2 is enforced by the indicated negative u sign. The signed aliases of w and d are formally q and R despite the extra complement gate. Exact complements of accumulator roots also retain their degree bounds. Witnesses use the actual signed operand roots; equality of alias polynomials suffices without equality of root identifiers. The alias a_0=x_1 adds no extension node.

The complete encoding ledger consists of n+5 input/constant/placeholder/J nodes, n original signs, 4C counter nodes, n selector products, n-1 selector prefix sums, n-1 d complements, n-1 conjunction prefixes, 2G extension complements and 6G witness nodes: 4C+8G+6n+2 in total, within the displayed allowance. Abstract labels and root-association labels are at most S<=B<=20(n+2)²<100(n+2)²; axiom indices are smaller too. Thus L also bounds these identifiers. A constant number of L-bit fields per abstract record and constant-size axiom expression fits the separately charged terms. This checks actual encoding capacity, not just semantic degree or shared node count.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/hwb-reduced-data/audit_data.py` for the audit supplement in `scripts/hwb-reduced-data/audit-results.json`. It regenerates and compares all six saved certificates in full, including all 40 free-word relations and both substitutions at n=2. At the first in-family value n=10 it checks all 1,024 assignments, both signs of all 432 extensions, a topological 886-node abstract table, every ordered relation/root association, and rejection of a late-cutoff corruption. At n=40 the replayed padded rooted count is 1,736,972,928 bits versus the conservative ceiling 815,301,528,768; representative and witness degrees are at most 41 and 83. Finite tests supplement the all-n proof and ledger, rather than verify them in a proof assistant. The audit adds verification evidence, not a new theorem or certified novelty.

## Mathlib

Coverage: **not checked** for this full HWB reduced-data, accumulator-invariant or complete encoding result. The cited Onaka et al. theorem is supporting representation coverage only and is not used as a premise. L027 supplies the explicit family and its recorded original-clause certificate; L020 supplies the axiom convention; L025 supplies the receiving hypotheses and conditional certificate construction. All new specializations and qualifications are written above. No Mathlib absence, certified originality or unconditional complexity separation is inferred.
