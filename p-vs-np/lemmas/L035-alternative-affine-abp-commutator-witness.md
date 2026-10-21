# L035 — Alternative commutator witnesses for two affine ABPs

## Hypotheses

Work in the free associative algebra F₂⟨x_1,...,x_n⟩. Supply two explicit finite directed acyclic graphs F,G with distinguished source and sink vertices. An edge label is an explicitly written affine linear form in the original x variables. The polynomial of a graph is the sum of the ordered label products of all source-to-sink paths; an empty path has value 1. Constants, parallel edges, disconnected vertices, unequal path lengths, zero polynomials and coinciding source/sink vertices are allowed. Denote the two polynomials by f,g. No circuits as labels, implicit graphs or Boolean quotient are allowed.

For i<j introduce a distinct free placeholder tau_(i,j), with substitution

    A_(i,j)=x_i x_j+x_j x_i.

Let E>=2 be the full binary length of the supplied graph encodings, their root references, the explicit original alphabet and the complete pair-once commutator axiom framing. Use a fixed ordinary explicit encoding: vertex/edge records and affine-label entries are listed, with binary identifiers and field coefficients. There is no assumption of polynomial-size formulas for f or g, or of a relation between their values and any ER extension.

## Conclusion

There is a deterministically constructible explicit acyclic affine-edge ABP W over the free alphabet x,tau such that, as formal polynomial identities,

    W(x,0)=0,                 W(x,A(x))=fg+gf.                 (1)

W is linear in the placeholders in the stronger sense that every source-to-sink path contains exactly one placeholder edge. Its full encoding, including alphabet, axiom list, labels and root references, has size O(E³ log(E+2)), hence O(E⁴). Construction takes polynomial time in E without expanding path sets or testing polynomial identities. The existence/size claim follows from the graph below; the algorithmic claim is separately justified by its explicit loops.

The output is an alternative witness, not L025's prescribed pair root. This supplies the commutator identity needed in that pair stage when the representatives have supplied affine ABPs. It does not construct general representative data, Boolean witnesses, defining-clause or proof-line ABPs, or a final certificate. It does not resolve every-certificate hardness or SAT decision. A separate critical audit on 2026-10-07 found no substantive error within these hypotheses; the audit and its finite evidence are recorded below. The source comparison did not establish a full arbitrary-ABP statement match; certified originality is not claimed.

## Proof

**Source use and the precise extra step.** Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4 (11 September 2015), Lemma 3.7, printed p.18, proves (1) for formula inputs P,Q with formula-witness size at most |P|²|Q|². Import that theorem on its formula-input subcase: F₂ is allowed, minus equals plus, and its pair-once commutator placeholders have exactly the present substitution. Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative Models*, author-hosted 16-page manuscript, Lemma 2 Step 1, printed p.5, supplies separate-graph serial/parallel composition for converting those formulas to explicit constant/linear-edge ABPs. Neither bound is measured in arbitrary supplied ABP input size. The additional argument here sums by marked edges, and proves directly that independent graph copies suffice. The short algebraic telescoping check below verifies the essential factor order for this graph specialization; it is not a claim of a new product-commutator identity or a reproof of the formula-size theorem.

**Edge-label witness.** Write the labels of e in F and d in G as

    ell_e=c_e+sum_i a_(e,i)x_i,
    ell_d=c_d+sum_j b_(d,j)x_j.

Put

    T_(e,d)=sum_(i!=j) a_(e,i)b_(d,j) tau_(min(i,j),max(i,j)).   (2)

This is an affine label (with zero constant term), or equivalently a list of parallel single-placeholder edges. Repeated terms may be retained as parallel edges. Since constants are central and characteristic is two,

    T_(e,d)(x,0)=0,
    T_(e,d)(x,A)=ell_e ell_d+ell_d ell_e.                     (3)

Indeed, expansion of the latter commutator cancels the constant/linear terms; diagonal x_i² terms occur twice; the remaining ordered i,j terms are precisely the substitution in (2). This also handles n=0, n=1 and constant-only labels, for which the appropriate sum is empty.

**Marked-path identity.** For vertices u,v of F let F[u,v] be the sum of all u-to-v path products, with F[u,u]=1, and likewise for G. If there is no such path the sum is zero. For e:u→v of F and d:a→b of G, define

    W = sum_(e,d) F[s_F,u] G[s_G,a] T_(e,d)
                         G[b,t_G] F[v,t_F].                 (4)

All products have exactly the displayed order. These subpath polynomials are represented by graph copies below, not expanded as formulas.

To check substitution, write [p,q]=pq+qp. For any finite sequence h_1,...,h_r, distributive expansion and adjacent cancellation give

    [h_1...h_r,q]
      =sum_i h_1...h_(i-1) [h_i,q] h_(i+1)...h_r.            (5)

For example the two middle terms of [ab,q]=a[b,q]+[a,q]b are both aqb and cancel. Induction on r proves (5), including r=0 because [1,q]=0. Similarly

    [h,k_1...k_l]
      =sum_j k_1...k_(j-1) [h,k_j] k_(j+1)...k_l.            (6)

Apply (5), then (6), to the label products of a path P in F and a path Q in G. The summand marked at edges e in P and d in Q is

    (P before e) (Q before d) [ell_e,ell_d]
                             (Q after d) (P after e).       (7)

The sum over all P,Q equals [f,g] by bilinearity. For fixed e:u→v, the possible paths P containing e correspond bijectively to a u-ending prefix from s_F and a v-starting suffix to t_F. Every such concatenation is a valid path: if the prefix and suffix shared a vertex, that concatenation would contain a directed cycle, impossible in a DAG. The edge cannot occur twice for the same reason. This argument treats parallel edges as distinct edges, retaining their correct multiplicities. The analogous statement holds for d in G, independently. Thus summing (7) over paths with those marked edges factors into the four subpath sums in (4), with (3) at the center. All sums are finite, so distributivity justifies this regrouping without a limiting operation. Consequently W(x,A)=fg+gf. Each summand of (4) has a central T factor, proving W(x,0)=0.

When a source equals its sink, the only source-to-sink path in an acyclic graph is empty. Its commutator contribution in (5) or (6) is zero; no edge lies on such a path. Formula (4) therefore remains valid. Constant labels and unequal path lengths were never removed or homogenized. Cancellation between distinct paths is retained in F₂; no semantic nonzero promise is used.

**One explicit affine ABP.** For each edge pair e:u→v, d:a→b make four disjoint copies of the original graphs, in this order:

1. a copy of F with designated endpoints s_F,u;
2. a copy of G with designated endpoints s_G,a;
3. a copy of G with designated endpoints b,t_G;
4. a copy of F with designated endpoints v,t_F.

Keep every original edge and affine label in each copy; pruning is unnecessary. Add a constant-1 connector from the first copy's exit to the second copy's entrance, and one from the third copy's exit to the fourth copy's entrance. Between the second copy's exit and the third copy's entrance, add the parallel tau edges specified by (2). Finally add a common new source with a 1-edge into the first copy and a 1-edge from the fourth copy to a common new sink, for each pair. No other cross-copy edges exist. If there are no edge pairs use the two new vertices with no edges.

Each copy is acyclic, and all connectors go forward in copy order, so the full graph is acyclic. This remains true if a designated entry and exit within a copy coincide. A source-to-sink path selects one pair branch, follows its four designated subpaths in order, and uses one central placeholder edge. Leaving a designated exit along an original edge cannot create an additional route back to that exit, since the original graph has no cycle; the only exit to the next copy is the prescribed connector. Accordingly this graph computes exactly (4), even when some designated subpath has value zero. Every edge is affine over x,tau. There is no shared two-sided recursion or path-history state in the output graph.

**Full size and construction time.** Let v_F,v_G be the vertex counts, m_F,m_G the edge counts, p=m_F m_G, and let a_F,a_G be the total numbers of nonconstant label entries after collecting coefficients separately within each input edge. Put

    q=sum_(e,d) |{(i,j): a_(e,i)=b_(d,j)=1 and i!=j}|.

Retaining duplicate central tau edges gives q<=a_F a_G. The explicit graph above has exactly

    N=2+2p(v_F+v_G) vertices,
    M=2p(m_F+m_G)+4p+q edges.                               (8)

These formulas also apply at p=0. For a fixed explicit encoding, every input record count and label-entry count is O(E); thus p=O(E²), q=O(E²), and N,M=O(E³). Each original label is copied at most 2p times, so the aggregate copied label payload is O(pE)=O(E³) bits before endpoint renumbering. The central edges have O(E²) placeholder occurrences. Give placeholders dense pair identifiers and retain the original alphabet dictionary and axiom list, at cost O(E). Binary endpoints and graph/root framing cost O((N+M)log(E+2)). Central labels cost O(E² log(E+2)); even copying original written pair names with length O(E) would cost only O(E³). This proves the stated O(E³ log(E+2)) full bound, without unit-cost unbounded identifiers or uncharged original axioms.

There is also a polynomial-time construction: parse and topologically check the supplied explicit graphs, normalize each finite affine label over F₂, enumerate their m_F m_G edge pairs, copy the four graphs per pair, and enumerate the at most a_F a_G contributing label-entry pairs to write the central edges. Number output vertices and write the connectors and framing. Every loop is polynomially bounded in E and all identifiers have polynomially bounded bit length; ordinary deterministic string handling therefore gives polynomial bit running time. No source-to-sink path enumeration, ABP-to-formula conversion, division, identity test or search for a certificate occurs. The output-size estimate is proved independently of the implementation's choice of string-handling algorithm.

**Downstream scope and stopping comparison.** In L025, a pair witness is required to vanish at zero placeholders and to substitute to r_i r_j+r_j r_i. If x-only affine ABPs for r_i,r_j are supplied, (1) supplies that identity with only original commutator placeholders, even if defining relations use other placeholders. This observation identifies the intended use, not a proof that the rest of L025 admits small ABPs: its Boolean recursion and subsequent proof assembly can still reuse two-sided contexts, and its general supplied-data premises remain open. L034 lower-bounds one prescribed output polynomial; (4) is free to differ from that polynomial before substitution. Neither L033 nor L034 is used as a mathematical premise of this construction, and both stopped conversion mechanisms remain stopped.

**Finite diagnostic.** Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/alternative-abp-commutator/check_marked_edges.py`. The script constructs the actual graphs above and evaluates their path sums by a topological traversal with explicit free-word F₂ arithmetic. On 83 input pairs it checks both identities, placeholder linearity, acyclicity, the exact vertex/edge counts (8) and q<=a_F a_G. Cases include a shared diamond, unequal lengths, affine constants, parallel-edge cancellation, zero labels, edgeless graphs, an interior coinciding source/sink, an empty alphabet and a one-variable alphabet. All checks passed, with at most 722 vertices and 1,034 edges; reversing the two suffix blocks is detected on 18 pairs. The complete input/output graphs, framing, polynomials, bounds and mutation results are in `scripts/alternative-abp-commutator/marked-edge-results.json`. For f=x_1x_2 and g=x_3x_4 the recorded witness is tau_(1,3)x_4x_2+x_1 tau_(2,3)x_4+x_1x_3 tau_(2,4)+x_3 tau_(1,4)x_2; its substituted polynomial has exactly the two required words. These finite checks diagnose implementation/order errors; the all-input identities and asymptotic binary bound are proved above, not inferred from the tests.

**Critical audit, 2026-10-07.** The following checks concern this same construction, not an additional theorem. In (5), consecutive cut terms cancel because both have the ordered word h_1...h_i q h_(i+1)...h_r; only the two end terms remain. In (6) the shared cut word is k_1...k_j h k_(j+1)...k_l. Substitution therefore gives exactly the F-prefix, G-prefix, central commutator, G-suffix, F-suffix order of (7). The four surrounding factors are independent only after fixing e,d: any forbidden overlap of a prefix with its own suffix would yield a directed cycle through the marked edge. Parallel edges remain distinct marked choices. Regrouping uses distributivity on finite sums, without commuting factors. Pairwise cancellations of the two orientations of a central tau label agree with the expansion of (3), including diagonal and constant terms.

The four-copy construction was checked with entry or exit equal, with incoming edges at an entry, outgoing edges at an exit, dead components and no designated path. A path that leaves an exit internally cannot later reach its connector without returning to that exit and forming a cycle. Thus unused original edges add no extra source-to-sink paths. All inter-copy edges follow the prescribed copy order; each accepting path takes one pair branch and exactly one central single-placeholder edge, even if its contribution has zero label value or cancels against another path. If the central sum is empty the branch has no accepting path. Source=sink inputs contribute only the empty path, whose commutator is zero. These observations validate the graph claims without a nonzero-polynomial promise, root-extremality convention or numerical vertex ordering.

For a separate binary ledger, let L be the aggregate normalized input-label payload in bits, and let b=max(1,ceil(log₂(N+M+n(n-1)/2+n+2))). Normalization can retain the original alphabet references while removing duplicate F₂ coefficients, so L=O(E). There are 2p copies of each input graph, hence at most 2pL copied label bits. Explicit output vertex/edge records, rewritten endpoints, list framing, dense central-symbol identifiers and roots together cost O((N+M+q+1)b); copying the original alphabet and complete axiom framing costs O(E). Thus a full encoding costs O(E+2pL+(N+M+q+1)b). The exact (8), p,q=O(E²), N,M=O(E³), and n=O(E) give b=O(log(E+2)) and the claimed O(E³ log(E+2)) bound. Isolated vertex records and all connector records are included. A dictionary mapping dense tau identifiers to the explicitly supplied pairs costs O(E) because the complete pair list is already part of E. Enumeration performs p graph-copy operations and at most a_F a_G central-entry iterations; normalization, dictionary lookup, topological validation and string writing have polynomial bit cost. This is a bound on construction as well as output size; it uses no path or monomial enumeration. The diagnostic's free-word expansion is unnecessary to, and need not be efficient as part of, this construction algorithm.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/alternative-abp-commutator/audit_marked_edges.py` for the independent finite audit. It reads the entire original certificate, regenerates and compares each graph, and evaluates from sinks backward using integer coefficient counts reduced modulo two, independently of the original forward free-word evaluator. It compares every saved free/substituted/zero/target polynomial, exact bound, axiom dictionary and wrong-order mutation result. A separate structural path calculation checks every accepting graph path, including paths with cancelling or zero contributions, rather than just the surviving free monomials. All 83 saved cases and 16 extra cases pass. The extra cases cover nonnumeric topological order, duplicate-label normalization, incoming source/outgoing sink edges and unreachable designated roots; all 18 recorded wrong-suffix mutations remain detected. The original certificate is preserved byte-for-byte. Complete audit results, including all newly tested graphs and polynomials, are in `scripts/alternative-abp-commutator/marked-edge-audit-results.json`. These tests provide new verification evidence only. The formal identities and encoding bound remain the all-input arguments above; the audit establishes no stronger representation theorem or certified originality.

## Mathlib

Full matching coverage and the explicit binary-encoding specialization: **not checked**. No absence claim is made. The primary mathematical references reused from the ready assessment are [Li–Tzameret–Wang, arXiv:1412.8746v4, Lemma 3.7, p.18](https://arxiv.org/pdf/1412.8746v4) and [Raz–Shpilka, Lemma 2 Step 1, p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf). They cover the formula subcase and separate-graph operations, respectively; the four-subpath factorization, graph construction and arbitrary-ABP input cost are justified above. This is local progress beyond the statement scope established in the inspected comparison, not a certified new theorem in the literature and not a resolution of P versus NP.
