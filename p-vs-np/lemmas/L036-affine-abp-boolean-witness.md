# L036 — Booleanity witnesses for supplied affine ABPs

## Hypotheses

Work in F₂⟨x_1,...,x_n⟩. Supply an explicit finite acyclic affine-edge ABP G with designated source s and sink t, computing f by the sum of ordered source-to-sink path products. Edges carry explicitly listed affine forms over F₂ in the original x variables. Empty paths contribute 1. Constants, parallel edges, disconnected vertices, zero labels/polynomials, unequal path lengths, nonextremal designated roots and s=t are allowed. No formula-size promise, circuit-valued edges or implicit graph is allowed.

Supply the complete original Boolean and pair-once commutator framing, with independent free placeholders

    sigma_i → x_i²+x_i                 (1≤i≤n),
    tau_(i,j) → x_i x_j+x_j x_i         (1≤i<j≤n).

Write A for this simultaneous substitution. Let E≥2 be the full binary input length, including explicit vertex/edge records, affine-label entries, root references, original alphabet, axiom list and placeholder dictionary. Use an ordinary explicit binary encoding as in L035. There are no original-clause placeholders, additional variables or quotient-ring identifications.

## Conclusion

There is a deterministic polynomial-time construction of an explicit acyclic affine-edge ABP B over x,sigma,tau satisfying the formal identities

    B(x,0,0)=0,                   B(x,A)=f²+f.                 (1)

Its full binary encoding, including alphabet, axiom and placeholder framing, has size O(E⁵ log(E+2)), hence O(E⁶). Every accepting path contains exactly one placeholder edge. The output is an alternative Booleanity witness, not a conversion preserving a previously prescribed witness polynomial.

This supplies a Boolean-root identity of the kind required in L025 when the representative is supplied as an affine ABP. General small representative/relation data, defining-clause and final ABP assembly, every-certificate hardness and unrestricted SAT decision transfer remain unresolved. A separate critical audit on 2026-10-07 found no substantive error within these hypotheses; its checks are recorded below. The approved source comparison did not establish an arbitrary-ABP full-statement match; no certified originality or P-versus-NP candidate is claimed.

## Proof

**Known inputs and the representation difference.** Use the audited L035 construction for two x-only affine ABPs p,q: its explicit graph W(p,q) has W(x,0)=0, W(x,A)=pq+qp, and exactly one commutator-placeholder edge on each accepting path. L035's exact four-copy graph and record counts, not a formula unfolding, will be used below. Its source comparisons include Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4), Lemma 3.7, printed p.18, and Raz–Shpilka, [*Deterministic Polynomial Identity Testing in Non Commutative Models*, author-hosted 16-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf), Lemma 2 Step 1, p.5. The former gives formula-input commutator witnesses; the latter supplies separate-graph serial/parallel operations. F₂ and explicit affine graphs fit L035's hypotheses directly.

Grochow–Pitassi, [*Circuit complexity, proof complexity, and polynomial identity testing: The ideal proof system*, author-hosted 59-page manuscript](https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf), §3.5 Lemma 3.6, printed pp.1:21–22, supplies a commutative Booleanity comparison with formula-size parameters. LTW v4 §3.1 Lemmas 3.5–3.7, pp.16–18, and local L020 also explain the existing formula/circuit mechanisms. Those are comparisons, not an import of the present arbitrary-graph bound. The necessary extra step is realizing suffix Booleanity by one graph with only left multiplication of recursive witnesses. The elementary product identity is verified below because its exact factor order determines whether this representation works; no known formula theorem is reproved.

**Normalize the graph without unfolding paths.** Collect coefficients within each affine label over F₂, and replace it by parallel edges labelled 1 or a single x_i, one for each nonzero coefficient. A zero label contributes no edge. This preserves every path sum by distributivity, leaves the vertex set unchanged, and creates only as many edges as the total number of supplied label entries. Distinct original edges remain distinct; cancellations between their paths need not be detected. Densely relabel variables while retaining the original-name dictionary.

Delete every edge leaving t. Such an edge cannot lie on any path ending at t: a subsequent return to t would give a directed cycle. Thus this deletion preserves every u-to-t path sum, including the empty t-to-t path. Denote the resulting graph by H, its vertex count by V and its edge count by M. For each vertex u let f_u be its path sum to t, so f_s=f. We have f_t=1, and for every u≠t,

    f_u = sum_(e:u→v) a_e f_v,          a_e∈{1,x_1,...,x_n}.   (2)

Vertices with no path to t have f_u=0. Outgoing edges are listed in any fixed order, with parallel edges treated as distinct records. The graph may retain incoming edges at a designated source and dead components; no root-extremality assumption is imposed.

**The ordered local identity.** Put b(z)=z²+z and [p,q]=pq+qp. In the free F₂ ring,

    b(ab) = a[a,b]b + b(a)b² + a b(b).                       (3)

Indeed the three summands expand in their displayed order as

    a²b²+abab,          a²b²+ab²,          ab²+ab.

The repeated words cancel, leaving abab+ab. For any finite ordered list z_1,...,z_r, direct distributive expansion also gives

    b(sum_i z_i) = sum_i b(z_i)+sum_(i<j)[z_i,z_j].          (4)

Each off-diagonal ordered product occurs in exactly one pair bracket, while the diagonal and linear terms are exactly the first sum. The formula includes r=0,1. These are formal identities without commuting variables.

For an edge e:u→v, let beta_e be sigma_i if a_e=x_i and zero if a_e=1. Then beta_e(A)=b(a_e), and beta_e vanishes at zero placeholders. Let

    W_e = W(a_e,f_v),
    W_(e,d) = W(a_e f_v,a_d f_w)  for e:u→v, d:u→w, e<d.   (5)

The arguments in (5) are supplied x-only graphs: a_e is a two-vertex one-edge graph; f_v is a copy of H rooted at v,t; and a_e f_v is a copy of H with one fresh source and an a_e-edge to v. These graphs have at most V+1 vertices and M+1 edges, apart from the two-vertex atom, and all have single-symbol labels. L035 therefore applies even to zero/constant suffixes and coinciding suffix endpoints. Each W in (5) is constructed independently from these x-only inputs, never from a recursively constructed Boolean witness.

For u≠t define the following polynomial over the free enlarged alphabet:

    R_u = sum_(e:u→v) (beta_e f_v f_v + a_e W_e f_v)
          + sum_(e<d outgoing from u) W_(e,d),
    R_t = 0.                                               (6)

Zero beta terms may be omitted. Products retain precisely the displayed order. The two occurrences of f_v in the first term will be two disjoint graph copies, not squaring the edge labels or identifying path choices. Every summand vanishes at zero placeholders and has exactly one placeholder along any accepting path in its graph realization. After substitution, (3) and (4) imply

    b(f_u) = sum_(e:u→v) a_e b(f_v)+R_u(A)   (u≠t).         (7)

To see this explicitly, apply (4) to z_e=a_e f_v in (2). For each diagonal term apply (3), using beta_e(A)=b(a_e) and W_e(A)=[a_e,f_v]; the off-diagonal terms are exactly W_(e,d)(A). The only remaining terms are a_e b(f_v). At t, b(f_t)=b(1)=0, agreeing with the empty outgoing list and R_t=0.

Define recursively in reverse topological order

    B_t=0,       B_u=R_u+sum_(e:u→v) a_e B_v   (u≠t).       (8)

This temporarily defines polynomials, not a proposal to copy recursively expanded expressions. Induction in reverse topological order using (7) proves B_u(A)=b(f_u) for every vertex. The same induction gives B_u(x,0)=0. Thus B_s satisfies (1). The critical representation feature is that every recursive B_v occurs only on the right of its single x-only edge label. All right contexts and both suffix copies stay inside R_u.

**One actual affine graph for (8).** Retain one copy of H as a propagation graph, with source s, and add a fresh final sink omega. Do not connect t directly to omega. For every nonzero formal summand of (6) that we chose to retain (including ones whose path polynomial might vanish), construct a disjoint branch graph:

- beta_e f_v f_v: a single sigma_i edge followed in series by two disjoint copies of H with endpoints v,t;
- a_e W_e f_v: a single a_e edge, a copy of L035's W_e, and one copy of H with endpoints v,t, in series;
- W_(e,d): a copy of L035's pair graph.

Use fresh source/sink vertices for each serial product and constant-1 connectors between its factors. From the corresponding propagation vertex u add a 1-edge to the branch entry, and from its exit a 1-edge to omega. All branches are pairwise disjoint and have no edges back to the propagation graph or to other branches. There are no branches at t. Even if a branch computes zero, it may be kept: no identity test is used. All labels in this graph are 1, x_i, sigma_i or tau_(i,j), so in particular are affine.

The whole graph is acyclic. First place a topological order of H, then the branch graphs in any order, each internally topological, then omega. Each branch is acyclic by the serial composition of disjoint DAG copies and L035; every connector points forward between these pieces. In an internal graph copy, using a designated exit's outgoing original edge cannot create an unintended way to leave that copy: reaching the connector would require returning to the designated exit, contrary to acyclicity. This also justifies composition with nonextremal roots or coinciding entry/exit.

Every accepting path follows H to one chosen vertex u, exits into precisely one local branch, and then reaches omega. Therefore its sum is exactly

    sum_u H[s,u] R_u.                                      (9)

There is no additional accepting path staying in H. Equivalently the path polynomial from a propagation vertex u to omega obeys (8), with the same terminal value zero at t. Reverse topological induction identifies it with B_u, proving that the actual graph computes B_s without unfolding (8). Branching and reconvergence within H automatically sum all prefix choices, without storing their histories. Each accepting path takes one placeholder edge in its chosen local branch, by construction and L035; the rest of the path uses x-only labels. This proves the stated stronger placeholder property, even for contributions that cancel in F₂.

If s=t, deletion of outgoing edges and absence of branches there leave no path to omega, so B=0, as required for f=1. Empty alphabets, edgeless graphs and constant paths are included: beta terms disappear and commutator graphs have no accepting placeholder paths when their inputs are constant. Disconnected vertices and paths not reaching the original sink merely produce zero suffix polynomials; the inductive identities still apply without deleting these vertices. No path-length uniformity or nonzero promise entered the argument.

**Polynomial record and full binary bounds.** Put Q=V+M+n+2, so Q≥2 and Q=O(E). Let r_u be the outdegree in H. The number K of branch terms used above is at most

    M + M + sum_u binomial(r_u,2)
       ≤ 2M+M(M−1)/2 ≤ (M+1)² ≤ Q².                        (10)

The first M allows beta terms and the second M allows W_e terms, including constant labels. There is no summation over complete paths. Every input graph to a W block has at most Q vertices and Q edges, with at most Q nonconstant label occurrences. In L035's exact ledger, p is the product of the two edge counts, so p≤Q², and its central-placeholder count q≤Q². Consequently that block has

    N_W ≤ 2+4Q³,
    M_W ≤ 4Q³+5Q²,
    N_W+M_W ≤ 12Q³.                                        (11)

These estimates hold for a one-edge operand as well as the larger prefixed suffix graphs. Each beta branch adds one atom and two suffix copies; each edge-commutator branch adds one atom and one suffix copy to a W block. With a fresh two-vertex serial-product wrapper and its four connectors, the latter's vertex-plus-edge count is at most 12Q³+Q+9≤15Q³ for Q≥2. The beta branch is at most 2Q+9≤15Q³; a pair branch already fits (11). Adding the two attachment edges gives at most 16Q³ records per branch. The single propagation graph and omega use V+M+1≤Q records. Thus, conservatively,

    N_B+M_B ≤ Q+16KQ³ ≤ 50Q⁵.                              (12)

Isolated vertex records, all copied edges and every connector are included. The important threshold is a fixed polynomial, not the particular exponent or constant.

Give output vertices and x/sigma/tau symbols dense identifiers, keeping the original-name and full axiom dictionaries, whose total initial encoding is O(E). Every new edge has only one symbol, with O(log(E+Q+2)) identifier bits. Each endpoint and root identifier has O(log(E+Q+2)) bits by (12), with the constant factor 5 absorbed; framing each vertex/edge record costs the same order. Hence the entire output costs

    O(E+(N_B+M_B+1)log(E+Q+2)) = O(E⁵ log(E+2)).             (13)

No repeated long original name is treated as unit cost: it is stored in the charged dictionary and referenced densely. The complete Boolean and pair-once axiom framing is retained even for unused variables or placeholders.

For deterministic construction, parse and topologically validate the input, normalize finite affine lists, remove outgoing t-edges, enumerate vertices/outgoing edges and unordered outgoing edge pairs, and build the stated copied suffix and L035 graphs. L035 constructs its graph by edge-pair and label-entry loops; here all its inputs have O(Q) records with one-symbol labels. The number and total size of all blocks are bounded by (10)–(12). Renumbering vertices, copying labels and dictionaries, writing connectors and output framing use polynomial bit time in E. No step enumerates source-to-sink paths, expands polynomial words, performs PIT, or searches for a witness. The recurrence (8) is used for proof only, not recursive witness copying.

**Finite diagnostic.** Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/affine-abp-boolean/check_suffix_graph.py`. The script constructs the actual graph, reusing L035's graph constructor, and evaluates paths with exact free-word F₂ arithmetic in free, zero and axiom-substituted modes. It checks normalization, both identities, the one-placeholder property of all accepting paths, exact copy-ledger counts and (10)/(12). Its 35 cases include shared diamonds, constants and an empty alphabet, parallel cancellation, duplicate affine-label entries, unequal path lengths, unreachable roots, incoming/outgoing root edges, nonnumeric topological order and coinciding endpoints. All pass, with at most 3,002 vertices and 4,597 edges. Omitting the product commutator is detected in five cases and omitting sum commutators in seven. Complete input/output graphs, axiom dictionaries, polynomials, local block counts, actual/required bounds and mutation values are saved in `scripts/affine-abp-boolean/suffix-graph-results.json`. These finite checks are diagnostic, not a substitute for (2)–(13) or the separate audit recorded below.

**Critical audit, 2026-10-07.** The ordered calculation (3) was checked term by term: its first term is a²b²+abab, its second a²b²+ab², and its third ab²+ab. Neither cancellation moves a factor. In (4), each ordered pair i≠j occurs once among the two terms of the unique bracket with smaller index first. Thus the exact local correction (6) leaves only the left-multiplied suffix Booleanities in (7). At t the empty path gives f_t=1 and b(f_t)=0. Reverse topological induction therefore proves both formal identities simultaneously at every vertex, including dead vertices; cancellation of a suffix polynomial does not require pruning its graph.

Normalization preserves each suffix separately by finite distributivity. An edge leaving t cannot occur on a path ending there, even for a path starting at another vertex, because that path would return to t. Deleting all such edges is therefore valid before forming any suffix input. At each use of L035, the operand graphs are still x-only copies of H, one-edge atoms, or copies with one fresh entry edge. All fit L035's explicit affine-DAG hypotheses, including a suffix rooted at t. No Boolean or commutator witness becomes an operand of a later L035 call. This avoids silently applying its input-size bound to recursively enlarged graphs.

Serial composition remains correct for internal or coinciding designated roots: an accepting path must enter and exit a copy at its designated endpoints, and a path leaving its exit along an internal edge cannot return to take the connector. Internal incoming edges likewise create no additional entry from outside the copy. Every inter-copy edge goes forward in the fixed sequence, and the local branches only leave the propagation graph. The fresh final sink forces an accepting path to choose exactly one branch, which itself has exactly one placeholder edge. In particular, an original s-to-t path supplies no unwanted placeholder-free accepting path. When s=t there is no branch or outgoing propagation edge there, so the output is zero. Empty alphabets may leave many constant paths in H but no accepting local correction path: each beta term is absent and every L035 central placeholder sum is empty. These arguments concern graph paths even when contributions cancel over F₂.

For an independent copy ledger, a beta branch has exactly 2V+4 vertices and 2M+5 edges with the stated wrapper convention. A product-commutator branch whose W has N_W vertices and M_W edges has N_W+V+4 vertices and M_W+M+5 edges. A pair branch consists of its W graph alone. The propagation graph contributes V+1 vertices and M edges; each branch then adds two attachment edges. L035 gives N_W=2+2p(v_F+v_G) and M_W=2p(m_F+m_G)+4p+q. Since each operand has at most Q vertices and Q edges and singleton labels, p,q≤Q². Thus N_W+M_W≤2+8Q³+5Q²≤12Q³ for Q≥2. Also V+M≤Q, so the serial wrapper and suffix additions fit 15Q³, and two attachments fit 16Q³. Summing over K≤Q² gives Q+16Q⁵≤50Q⁵. Parallel edges and isolated copied vertices are included in these exact formulas; no count assumes a nonzero path polynomial.

To check full binary size separately, let b be the maximum bit length of a dense output vertex or symbol identifier, including list lengths and root references. There are O(Q⁵) vertex/edge records and O(n²+n+1) symbols; n=O(E), Q=O(E), hence b=O(log(E+2)). Every output edge label is one symbol. The copied original-name, axiom and placeholder framing costs O(E), and the new records cost O((N_B+M_B+1)b). This proves (13), including unused symbols, endpoints, roots and dictionary references; no long name is replicated at unit cost. Normalizing explicit labels, topologically ordering the graphs, enumerating outgoing edge pairs and copying the bounded L035 blocks take polynomial bit time. The finite-word evaluator below is only a diagnostic and is not part of that polynomial-time construction.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/affine-abp-boolean/audit_suffix_graph.py` for the independent finite audit. It reads the complete original certificate and preserves it byte-for-byte, reconstructs each graph, and uses backward topological evaluation with integer coefficient counts reduced modulo two, independently of the constructor's forward evaluator. All 35 saved cases pass. In addition to every saved free/zero/substituted/target polynomial, dictionary, graph, mutation and bound, it checks normalization of every vertex-to-t suffix, both identities from every propagation vertex, and structural placeholder counts on all accepting paths, including canceled paths. The independently recomputed block ledger agrees exactly; each attached block has at most 16Q³ records and the entire graph at most 50Q⁵. The largest tested graph has 7,238 vertex-plus-edge records. The omitted product/sum commutators are still detected in five/seven cases. Complete finite audit graphs, polynomials, failures and actual/required bounds are saved in `scripts/affine-abp-boolean/suffix-graph-audit-results.json`. These checks provide new verification evidence for the existing claim, not a stronger theorem, asymptotic proof or certified novelty.

**Scope.** This result changes the witness polynomial freely while retaining its formal substitution identities. It therefore does not reopen the same-output stops in L033/L034 or Attempts 020/021. Given separately supplied ABPs for several representatives, it can be applied separately, charging all outputs to their full aggregate input length, but no assertion here supplies those representatives or carries every later proof-assembly operation into the ABP model. It proves a local representation closure property, not certificate hardness, a general deterministic circuit-identity verifier, or a consequence for unrestricted SAT decision time.

## Mathlib

Full matching coverage, the explicit ABP construction and binary bounds: **not checked**. No absence claim is made. The primary theorem references and their narrower roles are stated above; L035 is the direct local theorem input. The comparison sources cover formula commutators, graph composition and commutative Booleanity, while the suffix propagation and graph/binary accounting are proved here. POTENTIALLY_NEW describes only the absence of an established full match in the reused assessment, not certified mathematical novelty.
