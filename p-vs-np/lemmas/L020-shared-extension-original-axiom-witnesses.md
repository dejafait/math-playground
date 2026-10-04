# L020 — Shared original-axiom witnesses for ER extensions

## Hypotheses

Let F be an explicitly encoded CNF of width at most three, and let pi use the fresh acyclic AND-extension convention of [the ER foundation](../foundations/05-refutation-systems-and-simulation.md). Write T=2+|F|+|pi|, charging all literal identifiers, definitions, clauses and references. No assumption about a polynomial bound on the length of pi is made. The witness construction below uses its extension definitions; it does not use or simulate its resolution inferences.

Over F₂, fix the original axiom list A(x): the ordered falsity product for each original clause of F, the Boolean polynomials x_i²+x_i for each distinct variable of F, and the pair-once commutators x_i x_j+x_j x_i for i<j. A positive literal has falsity factor 1+x_i and a negative literal has factor x_i. Each clause has a fixed explicit literal order. Let t be placeholders for exactly this list, with b_i denoting its Boolean placeholders and c_ij its commutator placeholders. Original identifiers can first be densely relabeled, with restoration costs charged to T.

For each original variable put P_(x_i)=x_i. In extension order, a definition z iff (a AND b), with previously available literals a,b, gives the shared circuit

P_z=L_a L_b,             L_v=P_v,             L_(NOT v)=1+P_v.       (1)

Retain every value as a rooted arithmetic DAG, with ordered multiplication. Include the negative value 1+P_v for each available variable and the constants 0,1. If a nonextension proof variable does not occur in F, send it to 0 under this substitution; it is not an additional original input. This also accommodates such variables introduced by weakening. Let sigma denote the resulting substitution, and S the number of distinct nodes in the common x-only evaluation DAG. Then S=O(T).

Let A⁺ consist of the original clause polynomials, the three defining-clause falsity polynomials for every extension, and Boolean/pair-once commutator polynomials for all variables appearing in F or pi. Defining clauses may use any literal permutation and deletion of repeated identical literals, as in a sorted-set clause encoding. Opposite literals are retained if the clause is retained. Original clause order in A⁺ agrees with A. All identities below are in free noncommutative polynomial rings, not merely identities on Boolean assignments.

## Conclusion

One can construct a circuit W_j(x,t) for each axiom A⁺_j such that

W_j(x,0)=0,                 W_j(x,A(x))=sigma(A⁺_j).                 (2)

There is no extension variable, extension-axiom placeholder or additional free input in any W_j. The substituted extension values occur only as shared internal circuits over x. Each monomial in W_j contains at most one original-axiom placeholder.

For fixed constants K, independent of the proof, syntactic degree and unfolded sizes, the union of the witness circuits has at most K T² nodes. Even if every rooted witness is written separately without sharing between outputs, its aggregate full binary length, together with the explicit original axiom list, is at most K T⁵. The construction is polynomial-time in T, including writing those separate outputs.

This closes the shared original-axiom **witness** obligation at the required polynomial threshold in T. It does not yet construct the certificate body from pi or prove both identities of an assembled ER-to-circuit-IPS translation. Those remain the next mathematical applicability/composition check. It supplies no tree-size bound, certificate lower bound, proof lower bound or SAT decision conclusion. It specializes the inspected formula-commutation and commutative Booleanity mechanisms to this noncommutative shared representation; the exact shared statement has no full match in the checked assessment, and originality is not certified.

## Proof

**A polynomial table of formal commutation witnesses.** Number the x-only DAG nodes in topological order. P_g denotes the polynomial at node g. Construct one output K_(g,h)(x,t) for each ordered pair of nodes. Its invariant is

K_(g,h)(x,0)=0,        K_(g,h)(x,A(x))=P_g P_h+P_h P_g.               (3)

For g=h, or when either node is a constant, use the zero circuit. For two distinct original-variable nodes x_i,x_j, use c_(min(i,j),max(i,j)). Over F₂ that placeholder supplies either ordering of the same commutator. Every auxiliary variable sent to 0 is already a constant node.

For other pairs, split the first noninput node if possible. Use the following recurrences, with all value nodes and all earlier witness outputs shared:

K_(a+b,h)=K_(a,h)+K_(b,h),
K_(ab,h)=P_a K_(b,h)+K_(a,h) P_b.                                   (4)

If the first node is an original input, split the second node:

K_(g,a+b)=K_(g,a)+K_(g,b),
K_(g,ab)=K_(g,a) P_b+P_a K_(g,b).                                   (5)

Each referenced pair has a strictly smaller sum of topological indices, so the table is acyclic and can be constructed in increasing order of that sum. The algebra behind the product cases is, formally,

a(bh+hb)+(ah+ha)b = abh+hab,
(ga+ag)b+a(gb+bg) = gab+abg.                                        (6)

The middle terms cancel in characteristic two; no permutation of noncommutative factors is assumed. Addition cases follow from distributivity. The diagonal and constant cases are exact formal zero commutators. Induction proves (3), including zero when all placeholders are zero. Each pair creates at most three new arithmetic gates, so the table has at most 3S² new gates. The inspection of an unfolded formula, or enumeration of its words, is unnecessary for the construction.

**Booleanity with the missing commutator correction retained.** For each evaluation node construct B_g(x,t) satisfying

B_g(x,0)=0,                  B_g(x,A(x))=P_g²+P_g.                   (7)

At constants use zero; at x_i use b_i. At an addition gate use

B_(a+b)=B_a+B_b+K_(a,b).                                            (8)

After axiom substitution its value is a²+a+b²+b+ab+ba, which is exactly (a+b)²+(a+b). In particular, the negative-literal node 1+a has the same Booleanity polynomial as a.

At a product gate use

B_(ab)=P_a K_(b,a) P_b+B_a P_b²+P_a B_b.                             (9)

After substitution, its three terms are

a(ba+ab)b,              (a²+a)b²,              a(b²+b).

Their sum is abab+ab: the two a²b² terms and the two ab² terms cancel. This is (ab)²+ab in the free ring. Omitting the first term would leave a²b²+ab, which is generally a different formal polynomial. Every right-hand-side witness is already constructed, and at most a fixed number of new gates is required per node. Induction proves both parts of (7). These witnesses have O(S) additional gates once the commutator table is available, even for circuits of exponential syntactic degree.

**Substituted defining clauses.** Fix z iff (a AND b), and abbreviate A=L_a, B=L_b, Z=P_z=AB. For the definition-order clauses

(NOT z OR a),             (NOT z OR b),             (z OR NOT a OR NOT b),

their falsity products after sigma are

Z(1+A),                   Z(1+B),                  (1+Z)AB.         (10)

The equalities between literal factors and 1+A or A remain formal even for negative literals, because 1+(1+P_v)=P_v. Use the witnesses

D_1=B_A P_B+P_A K_(B,A),       D_2=P_A B_B,       D_3=B_Z.           (11)

Here subscripts A,B,Z designate their evaluation-DAG nodes, not new variables. The first evaluates to

(A²+A)B+A(BA+AB)=AB+ABA=AB(1+A),

the second to A(B²+B)=AB(1+B), and the third to (AB)²+AB=(1+Z)AB. Each is zero when the original placeholders are zero. Thus (11) supplies the defining-clause instances of (2) in definition order.

**Literal ordering and duplicate removal.** It is insufficient to identify a sorted-set clause polynomial with (10) only on Boolean assignments. Let L and R be the x-only products of the factors before and after a local change, with empty products equal to 1. For an adjacent swap of evaluation factors u,v, the formal difference is

LuvR+LvuR=L(uv+vu)R.

Add L K_(u,v) R to the current witness. Its axiom-substituted value is this difference, so characteristic two changes the represented polynomial from the old product to the new one. Its zero-placeholder identity is preserved. The signed falsity factors are nodes already present in the evaluation DAG.

After sorting, identical repeated literals have adjacent equal factors q. Removing one of them has formal difference

LqqR+LqR=L(q²+q)R.

Add L B_q R to the witness. Again both identities are preserved. Since a defining clause has width at most three, there are at most three adjacent sorting swaps and two duplicate deletions. Prefixes, suffixes and corrections each need only constantly many gates referencing the shared table. The normalized defining-clause witness therefore retains the constant additional cost per clause. A retained tautological clause is treated by the same calculation; no semantic tautology test replaces its witness.

**All remaining augmented axioms.** For an original clause use its original placeholder. No original variable or clause factor is changed by sigma. For a Boolean axiom of an original, extension or auxiliary variable v, use B_(P_v). For a commutator of any two such variables v,w, use K_(P_v,P_w). A variable mapped to zero is handled by the constant cases. Equations (3), (7), (10)–(11) and the normalization calculation now prove (2) for every entry of A⁺.

All coefficient circuits in these recurrences contain only x. The initial witnesses are zero or individual original placeholders. Addition and multiplication on either side by x-only coefficients preserve the property that a monomial contains at most one placeholder. This proves the stated two-sided linearity without asserting that placeholders commute with coefficients.

**Binary cost in the original parameter.** The number of distinct written variables, clauses and extensions is O(T). Original values and their negative values need O(T) evaluation nodes; auxiliary values are constants. Thus S=O(T), not a bound in their occurrence-tree sizes. The commutator table adds O(S²) nodes, Booleanity adds O(S), and each defining-clause normalization adds O(1). Original clause placeholders and the list A add only O(T²) entries. There are O(T²) outputs in A⁺, dominated by its pair-once commutators. Counting input nodes and unused table states as well gives a common witness network of H=O(T²) nodes.

To avoid assuming free sharing between separately written certificates, write each output as its entire rooted DAG. Each such DAG has at most H nodes, so all outputs together have O(T⁴) node occurrences. Constants have one-bit coefficients. Dense gate/placeholder references require O(log(T+2)) bits; any restored original identifier requires at most T bits. Charging even T+O(log(T+2)) bits to every occurrence gives O(T⁵) total binary length. The explicit original axiom list contains O(T²) constant-width expressions and costs O(T³) bits under the same conservative identifier bound. Its cost is absorbed by K T⁵.

The table is constructed by polynomially many fixed arithmetic operations and reference writes. Extracting each rooted DAG, densely renaming it and restoring identifiers has polynomial bit cost bounded by the same output estimate. No identity test, degree enumeration or materialization of an extension occurrence tree is part of the construction. This proves the fixed polynomial threshold in T. L019's exponential literal-substitution parameter remains a valid obstruction for its own tree construction; it is not used as a witness parameter here.

**Finite verification and limits.** Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/shared-extension/check_witnesses.py`. Independent exact expansion into noncommutative words checks 67 small cases: 11,181 gate-pair witnesses, 853 Booleanity witnesses, 537 defining clauses, 802 sorting swaps and 25 duplicate deletions. It checks both identities, ordered multiplication and syntactic placeholder degree at most one. Four corrupted constructions are detected: omission of the product commutator correction, reversed coefficient order in a commutator, omission of a sorting correction and omission of a duplicate-deletion correction.

Six separate structural cases preserve repeated-squaring DAGs without word expansion. With 128 extensions, the value degree is 2^128 and its unfolded root has 2^129−1 nodes, while the shared witness construction has 67,600 gate-pair states and 133,254 total nodes. Its gate-record and output-reference payload, charging a sparse original identifier, has 8,539,510 bits. This diagnostic count excludes framing and the explicit axiom list; the asymptotic argument above separately charges the full aggregate rooted outputs and original axioms. It is not the length of a complete ER/IPS translation. Results are in `scripts/shared-extension/witness-results.json`.

These finite tests check the new witness identities and indexing. They do not verify ER proof strings or the two IPS identities of an assembled certificate. The formal inductions and cost argument above establish the claimed asymptotic intermediate result. The ready assembly subtarget can next test whether composing these witnesses with a screened certificate construction has polynomial full binary cost and removes every auxiliary placeholder.

## Mathlib

Coverage: **not checked** for the shared witness statement, its normalization or binary cost. Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Lemmas 3.6–3.7, printed pp. 17–18](https://arxiv.org/pdf/1412.8746v4), and Tzameret, [*Algebraic Proofs over Noncommutative Formulas*, July 2011 author manuscript, Lemma 3.7 / Claim 3.8, pp. 10–11](https://www.doc.ic.ac.uk/~itzamere/nonComm.pdf), supply supporting formula-commutation comparisons. Grochow–Pitassi, [*Circuit complexity, proof complexity, and polynomial identity testing*, author-hosted manuscript, §3.5 Lemma 3.6, printed 1:19–22](https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf), supplies a supporting commutative Booleanity construction. Those sources do not supply an inspected full match for this shared noncommutative original-axiom result. The recurrences, correction terms, clause witnesses and binary accounting are proved above; no Mathlib identifier, absence claim or certified originality is inferred.
