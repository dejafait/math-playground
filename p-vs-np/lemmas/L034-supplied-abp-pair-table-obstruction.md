# L034 — Supplied affine ABPs do not bound the prescribed pair table

## Hypotheses

Use exactly L025's hypotheses and ordered pair construction, including its rule to split the first nonbase node whenever possible, diagonal and constant exceptions, and equations (5)–(6). Strengthen the supplied representation format: every representative r_i and relation H_i is given by an explicit finite acyclic affine-edge ABP over the free F₂ algebra on the original variables and independent original-axiom placeholders. Each edge label is an affine linear form, and the output is the sum of ordered source-to-sink path products. All graphs, labels, root associations, abstract nodes and original axioms are charged in E_ABP. Inputs satisfy both formal H identities and the semantic degree bounds d,h before axiom substitution. Only representation format changes; in particular no all-assignment extension-value promise is added to L025.

The receiving ABPs have the same explicit affine-edge model, including constants and parallel edges. Equality to a prescribed table output means formal equality, before substituting axioms or passing to a Boolean quotient. Let T be L025's full binary CNF/proof parameter and S its abstract-node count.

## Conclusion

For every k>=2 there is such an input with a valid ER refutation, every extension used in the final inference ancestry, and

    T=O(k log(k+2)),    S=4k+8,    d=1,    h=3,
    E_ABP=O(k² log(k+2)).                                      (1)

One prescribed ordered pair output requires at least

    binomial(k,floor(k/2)) >= 2^k/(k+1)                        (2)

vertices in every identical-output affine ABP. Consequently no polynomial in T+S+E_ABP+d+h bounds the aggregate full binary size of affine ABPs computing all prescribed pair roots. The obstruction already holds for one root.

This is a negative answer to the supplied-ABP fixed-pair-table question, obtained with the established noncommutative cut-rank method. It is not a lower bound for alternative witnesses, the final certificate after assembly, all certificates, ER proofs or SAT decision. The original CNF has an immediate refutation. The separate informal critical audit below found no substantive error; no P-versus-NP candidate or certified originality is claimed.

## Proof

**The original instance and a used ER proof.** Take distinct original variables q,w,x_0,...,x_k and let F_k consist of the units

    (q), (NOT q), (w), (x_0), ..., (x_k).

Thus every displayed variable really occurs in the original width-one CNF. Set e_0=x_0 as a notation, not a new variable. For i=1,...,k introduce the fresh extension

    e_i iff (e_(i-1) AND e_(i-1)).

In the sorted-set convention its three defining clauses are two copies of (NOT e_i OR e_(i-1)) and the clause (e_i OR NOT e_(i-1)). These are the usual three AND clauses with repeated literals removed; repeated operand literals are allowed by the ER convention. Both copies may be written with distinct record references. From the earlier unit (e_(i-1)) and the third defining clause, resolve to obtain (e_i). Start with the original (x_0). After all definitions, weaken (NOT q) to (NOT q OR NOT e_k); resolve it with (e_k) to obtain (NOT q), and resolve this with the original (q) to obtain the empty clause. This is a valid ER refutation. Every extension's derived unit and third defining clause belong to the final inference ancestry through the unit chain. No assertion that all three defining clauses are used is needed. There are O(k) constant-width records, with O(log(k+2))-bit identifiers/references, giving the stated T bound.

Use L025's original axiom list: the ordered clause falsity polynomials, the Boolean polynomials for every original variable, and one commutator per distinct original pair. Let a,b be the placeholders for (q),(NOT q), respectively. Their substituted values are 1+q and q. Hence the affine polynomial

    U=a+b

satisfies U(x,0)=0 and U(x,A(x))=(1+q)+q=1 formally in the free algebra. Let c denote the original pair placeholder for x_0 and w (with the pair ordered according to the fixed original variable order). It is distinct from a,b, and its substituted value is x_0 w+w x_0.

**All supplied abstract data and ABPs.** Include the k+3 original-variable base nodes, two constant nodes 0,1, the k extension nodes e_i, and one exact negative signed node for each of the 2k+3 original or extension variables. Number bases first, then extensions in increasing i, then signed nodes. All edges point to earlier nodes. This gives S=(k+3)+2+k+(2k+3)=4k+8. There is a value for every signed literal needed in the proof, including the last weakening. No nonextension variable absent from F is used.

Original-variable and constant representatives retain their specified values. For extension nodes supply

    r_(e_i)=x_i,

and for every negative signed node supply 1 plus its positive representative. These polynomials all have degree at most d=1. Each has a two-vertex, single-affine-edge ABP (the zero label is allowed, or an edgeless source/sink pair represents zero). In particular x_i remains a separate original base node; equality of representative polynomials does not identify distinct abstract nodes.

For every reduced AND node e_i, supply exactly

    H_i=(x_i+x_(i-1)x_(i-1))(a+b).                              (3)

This has an explicit four-vertex ABP: use vertices s,u,v,t and edges s->v labeled x_i, s->u labeled x_(i-1), u->v labeled x_(i-1), and v->t labeled a+b. Its two path products sum to (3), in the required order. Its degree is three, so h=3 suffices. There are no other reduced AND nodes. Both required identities hold formally:

    H_i(x,0)=0,
    H_i(x,A(x))=(x_i+x_(i-1)^2)*1
              =r_(e_i)+r_(e_(i-1))r_(e_(i-1)).                 (4)

For i=1 the operand representative is r_(e_0)=x_0, as required. Signed-node identities are exact by definition. These checks supply every relation, rather than only the one later used in the lower bound.

There are O(k) constant-size supplied ABPs and abstract records; their labels, references and root associations cost O(k log(k+2)) bits in total. The original axiom list has O(k²) entries of constant arithmetic size and O(log(k+2))-bit variable identifiers. Including its framing yields the conservative E_ABP bound in (1). Degrees are measured in independent x,t and are genuinely bounded before substitution. These ABPs also yield representative circuits of the type required by L025 by ordinary addition of their displayed paths, with constant cost per supplied graph.

The actual extension e_i evaluates as x_0 on arbitrary Boolean assignments, whereas its supplied representative is x_i. This is permitted: L025 requires (4), not equality on every original assignment. On satisfying assignments the relation would enforce agreement, but F_k has none. The formal identities (4), not vacuity alone, certify the promise. This example therefore does not address a strengthened problem demanding faithful extension representatives on every assignment or forbidding original-clause placeholders in H_i.

**Isolating the prescribed output without altering its construction.** Let K_i be L025's ordered table output for the abstract pair (e_i,w), using the base node x_0 when i=0. Apply the algebra homomorphism rho that fixes every original variable and c and sends every other placeholder to zero. Thus rho(H_i)=0, while K_0=c. The first node of (e_i,w), for i>=1, is a reduced AND node with both operands e_(i-1); it is neither constant nor the same abstract node as w. The fixed split-first rule therefore uses precisely L025 (5). It gives

    Q_0:=rho(K_0)=c,
    Q_i:=rho(K_i)=x_(i-1) Q_(i-1)+Q_(i-1) x_(i-1).             (5)

The two H_i w+w H_i terms disappear under rho. No relation substitution, commutation or cancellation across uninspected placeholder sectors is used. If an N-vertex affine ABP computes K_k, setting its placeholder coefficients according to rho gives an affine ABP with the same vertices computing Q_k. Pruning, if desired, can only decrease its size. Thus a lower bound for Q_k is also one for the exact prescribed K_k.

For a subset L of {0,...,k-1}, write x_(L decreasing) for its letters in strictly decreasing index order and x_(L increasing) for increasing order; an empty product is 1. Induction on (5) yields

    Q_k = sum_(L subset {0,...,k-1})
                  x_(L decreasing) c x_(L-complement increasing). (6)

Indeed, at step i the new largest index i-1 is placed either at the far left or at the far right. These are exactly the cases where i-1 belongs to L or its complement. Different subsets give distinct words, because the letters preceding the unique c identify L. Every coefficient in (6) is therefore one over F₂, with no hidden characteristic-two cancellation. Every word has length k+1.

**The coefficient rank and the receiving model.** The standard input is the lower-bound direction of Nisan, *Lower Bounds for Non-Commutative Computation (Extended Abstract)*, STOC 1991, pp.410–418, Theorem 1, §§2–3 ([DOI](https://doi.org/10.1145/103418.103462), [primary-paper mirror](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf), PDF pp.4–5): a homogeneous ABP's coefficient matrix at a word-length cut factors through its cut layer. We reuse this rank mechanism, not a claim that arbitrary two-sided skew circuits are ABPs. L033 supplies the finite constant-path argument for affine-edge DAGs. For completeness the necessary extension of that argument from two letters to the present finite alphabet is as follows; this is receiving-model applicability, not a reproof of the general characterization.

Topologically number the N vertices. Let C be the matrix of constant edge coefficients and A_z the matrix of coefficients of a generator z, summing parallel edges. All are strictly upper triangular. Put D=I+C+...+C^(N-1) and G_z=A_z D. For a word v=z_1...z_r, write G_v=G_(z_1)...G_(z_r). The unique decomposition of a path into a constant prefix and variable edges each followed by a constant run gives

    [v]f=e_s D G_v e_t.

Strict topological progress ensures these concatenations are paths, and the final constant run before a cut is included only in its left factor. This is exactly L033's finite factorization, one scalar matrix per generator; it does not require two generators, characteristic zero, homogeneous input edges, or a bound on the number of monomials. For any fixed left and right word lengths, the matrix with entry [uv]f factors as the row e_s D G_u times the column G_v e_t, and consequently has rank at most N over F₂. Extra unused generators cause no change.

Set m=floor(k/2). For every m-element subset L of {0,...,k-1}, select the row word u_L=x_(L decreasing), of length m. For every m-element subset L', select the column word v_(L')=c x_(L'-complement increasing), of length k+1-m. Formula (6) implies

    [u_L v_(L')] Q_k = 1 if L=L', and 0 otherwise.

To see the off-diagonal assertion, a word with c after exactly m letters must have precisely those left letters as its subset in (6), and its right letters must then be that subset's complement in increasing order. Distinct subsets cannot produce the selected same word. The selected matrix is the identity of order binomial(k,m). Its F₂ rank is that order, so the full coefficient matrix and any affine ABP for Q_k have at least that rank and that many vertices. Among the k+1 binomial coefficients, the central coefficient is largest (as follows from the consecutive-coefficient ratio (k-j)/(j+1)); their sum is 2^k. This proves (2).

**Comparison with the required threshold.** Let P_k=T+S+E_ABP+d+h. Equation (1) gives P_k<=C(k+2)² log(k+2) for one constant C. Explicit vertex records cost at least a fixed positive number of bits per vertex, so for any fixed exponent b>=0 the receiving binary length divided by (P_k+2)^b is bounded below by a positive constant times

    2^k / ((k+1)(C(k+2)² log(k+2)+2)^b),

which tends to infinity. One hard root already excludes an aggregate polynomial bound, even if a common receiving graph is permitted to share vertices across multiple designated outputs: selecting its hard root still gives an ABP with no more vertices. This proof uses all-k identities and a symbolic identity submatrix; no finite experiment is its evidence.

The family satisfies the stated input format and all formal relations despite polynomial input degree and tiny individual graphs. The negative conclusion stops this prescribed pair-table conversion only. The fixed easy contradiction and the freedom to change the representatives, witnesses, refutation or eventual certificate prevent promotion to any optimal-proof or SAT lower bound.

**Separate critical audit, 2026-10-07.** This audit uses the previously approved exact scope and the cited sources through L033's completed affine-model specialization. It checks L025's written promises without adding all-assignment faithfulness or a restriction on the kinds of original placeholders in H. No substantive mathematical error, changed bound or new mathematical input was found. The following checks justify retaining the restricted stop; they are an audit of the existing argument, not a new lower-bound theorem or formal verification.

1. **Every proof record and used extension.** There are k+3 distinct original variables and k+4 unit clauses, all of width one. Each e_i is fresh and uses only the already available e_(i-1). Substituting equal operands into the three permitted AND clauses and removing repeated literals within each clause gives exactly the two identical first clauses and the third displayed clause. Repeated clauses may occupy distinct proof records; sorted-set normalization concerns literals within a clause. Resolving (e_(i-1)) with (e_i OR NOT e_(i-1)) on the selected pivot produces (e_i), with no other literal remaining. The final weakening adds NOT e_k to the original (NOT q); its resolution with (e_k) produces a new record (NOT q), and resolution with the original (q) produces the empty clause. These references are acyclic even though the new unit equals an earlier clause. Tracing backwards from the empty clause reaches (e_k), every earlier derived unit and each third defining clause. The two unused defining-clause copies do not undermine the stated used-extension property. The k+4 initial clauses, 3k extension clauses, k unit inferences and three terminal inferences give O(k) records and O(k log(k+2)) binary bits. A short alternative refutation does not invalidate this particular supplied refutation or create a lower bound for optimal refutations.

2. **All supplied nodes and identities.** The S count includes k+3 original bases, two constants, k positive extensions and 2k+3 negative signed nodes, hence 4k+8. Bases and constants come first, extensions reference earlier positive nodes, and the later negative nodes reference their positive nodes. No signed operand needed by this proof is omitted. Each r_i is x-only and either a constant, an original variable or one plus an original variable, with a two-vertex affine ABP. In particular a reduced node labeled e_i is distinct from the original base x_i even though their representative polynomials agree. The four-vertex H graph has precisely the two source-to-sink paths stated in (3); there is no extra path, constant term or reversed multiplication. Its degree-three terms do not cancel because a,b and the original variables are independent generators. Thus d=1 and h=3 bound every supplied root before substitution. Setting placeholders to zero kills the last edge. Substitution gives, in the actual multiplication order,

       (x_i+x_(i-1)^2)((1+q)+q)=x_i+x_(i-1)^2.

   This uses only F₂ addition and multiplication by 1, with no commutation or Boolean reduction. It holds also at i=1 with base operand x_0. Every reduced AND node has such an H; constants and signed nodes require no extra H. All original clause, Boolean and pair-once commutator axioms are explicitly available. They number O(k²), have constant arithmetic size, and use O(log(k+2))-bit identifiers, including placeholder identifiers. The supplied graphs and root associations have O(k log(k+2)) bits; with the complete axiom framing this verifies E_ABP=O(k² log(k+2)). Expanding each constant-size supplied graph into its at most two paths gives a constant-size circuit for L025's input format. No uncharged general ABP-to-formula conversion is used. The fact that the true Boolean e_i equals x_0 while r_(e_i)=x_i is not hidden: it violates a possible stronger faithfulness promise but no written L025 hypothesis.

3. **The prescribed recurrence and projection.** The base pair (x_0,w) is a pair of distinct original variables, so its output is exactly c. Pair-once storage causes no sign ambiguity over F₂. For i>=1, e_i and w are distinct abstract nodes; neither is constant, and e_i is a reduced AND node. The diagonal, constant and duplicate-base-label exceptions therefore never apply. The first-node split uses the two identical abstract operands e_(i-1), giving exactly the two differently ordered products in (5), plus H_i w+w H_i. Although both products reuse K_(i-1), they are not duplicate polynomials that may simply be cancelled. The homomorphism rho fixes every original generator and c, and kills a,b and all other placeholders, so it kills every H_i. Its action on every affine edge preserves affinity and acyclicity and uses no extra vertices. This compares formal polynomials before axiom substitution; substituting c by its commutator instead would be a different operation and is not used.

4. **Every selected coefficient.** At stage i the generator x_(i-1) is absent from Q_(i-1). Prefixing or suffixing it creates respectively the subsets that contain or omit i-1 in (6). The unique c separates the chosen left subset from its complement, so this enumeration is injective at every k. All 2^k words therefore have coefficient one over F₂ and degree k+1. For fixed m=floor(k/2), the row words are distinct, as are the column words. The selected diagonal word has the required decreasing left subset and increasing right complement, hence coefficient one. If L differs from L', equality of their cardinalities gives an index in L minus L'. That generator occurs both in u_L and in the complement part of v_(L'); the concatenated word repeats it. Every word of (6) uses each x_0,...,x_(k-1) exactly once. Consequently each selected off-diagonal entry is zero. This checks all entries, including when k is odd; for k>=2 both selected word lengths are positive. It does not assume that the rest of the cut matrix is zero.

5. **Constants, growing alphabet and original graph size.** For any receiving N-vertex graph, expand each affine edge into its scalar and generator choices for the coefficient argument. All matrices C,A_z are strictly upper triangular, including after parallel-edge aggregation. D counts constant-only paths with their F₂ multiplicities. An expanded path has a unique decomposition into its constant prefix and its generator edges followed by whole constant runs. Conversely these pieces concatenate into a path since every nonempty edge advances the topological index. Cancellations give the same parity in the path sum and the matrix expression. At the cut after u, the entire constant run after its last generator is in the last D of e_s D G_u; the right factor G_v starts with its first generator matrix, not another D. Hence a constant run is not counted once for each possible internal cut vertex. The product factors through exactly N scalar coordinates, so rank is at most the vertex count of the original graph. The alphabet is finite for every k and may grow with k: there is simply one A_z for each generator, and this does not enlarge the N-coordinate factorization. Constants, unused generators, parallel edges and cancellations are all accommodated by the same coefficient identity; a possible empty source-to-sink path contributes only to degree zero. No real-field comparison, implicit graph, circuit edge label or normalization-size lower bound is substituted for this original-graph bound.

6. **Threshold and scope.** The identity submatrix has rank binomial(k,m) over F₂. The central binomial coefficient is maximal, and the sum of the k+1 coefficients is 2^k, giving the stated 2^k/(k+1) bound. Full input P_k is at most C(k+2)^2 log(k+2), whereas an explicit output graph has at least a constant number of bits per vertex. Their ratio exceeds every fixed polynomial threshold by the displayed limit. Selecting one designated output in a shared multi-output graph leaves no more than its total vertices, so aggregate sharing cannot evade the lower bound. L025's degree allowance (7) is only linear in S here for the pair table; it makes no ABP-size promise contradicted by this example. The result concerns its prescribed output and no claim about a different witness satisfying the same two formal identities. General data, later assembly, optimal-certificate hardness and decision transfer remain unresolved.

Direct local mathematical inputs remain L025 and L033. L021 and foundation 05 delimit the inherited proof/axiom conventions rather than supply an additional theorem used in the lower bound. No script or finite test is needed for the exhaustive symbolic checks above. The audit completes a local reliability check without extending the conclusion beyond the sources and proof already recorded.

## Mathlib

Full matching coverage **not checked**. No absence claim or Mathlib theorem identifier is inferred. The established coefficient-rank lower bound is cited above, and the precise affine-model, growing-alphabet and F₂ applicability is justified in the proof using L033. The local content is the explicit instance meeting L025's supplied-data promises and the selected output-sector calculation; the saved EXPLORE assessment found no full statement match, which is not certified novelty. The separate informal audit is complete; neither proof nor audit has been formally verified.
