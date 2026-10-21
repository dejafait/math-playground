# L030 — Expander independent sets require exponential common-order OBDD sum width

## Hypotheses

Fix an integer Delta>=3 and a real 0<epsilon<1. Let G=(V,E) be a finite simple undirected graph with n=|V|>=2, maximum degree at most Delta, and external vertex expansion

|N_G(U) \\ U| >= epsilon |U| for every U subset V with |U|<=n/2.

Let f_G:{0,1}^V -> F₂ be the independent-set indicator: f_G(x)=1 exactly when {v:x_v=1} contains no edge of G. Fix any permutation y_1,...,y_n of V. Supply a finite list D_1,...,D_m of deterministic OBDDs in this **one common order**, with

f_G(x)=sum_(j=1)^m f_(D_j)(x) over F₂ on every assignment.

Each diagram has n nonterminal levels: every level-i state queries y_i, both successors lie at level i+1, and level n+1 consists only of terminals labelled 0 or 1. Its root is at level 1. Redundant queries are allowed, and neither reduction nor minimality is assumed. Let w_j be its maximum nonterminal level size and W=sum_j w_j. Width counts all explicitly supplied states, including any unreachable ones. In particular no branch can terminate before the last query. This dense convention is essential to the width accounting below.

The imported graph input is Simone Bova and Friedrich Slivovsky, *On Compiling Structured CNFs to OBDDs*, Theory of Computing Systems **61** (2017), 637–655, [DOI](https://doi.org/10.1007/s00224-016-9715-z), [journal text](https://link.springer.com/content/pdf/10.1007/s00224-016-9715-z.pdf), Definition 16 and **the half-prefix claim in the proof of Lemma 18**, printed pp. 650, 652–653. For the expansion and degree hypotheses above, that claim gives, at the prefix of floor(n/2) vertices of any order, distinct crossing pairs (a_i,b_i), 1<=i<=q, with q>=epsilon*n/(16*Delta), such that the a_i are independent and a_i is adjacent to b_j among these suffix endpoints exactly when i=j. The b_i are not asserted independent. This is the specific graph witness used, not the deterministic OBDD conclusion of Theorem 19.

## Conclusion

For every such graph, common order and representation,

W >= 2^(c n),                 c=epsilon/(16*Delta*(Delta+1))>0.

In particular, for any supplied family satisfying these fixed graph hypotheses with unbounded n, polynomially many polynomial-width dense common-order OBDDs cannot represent f_G by an F₂ sum. The statement is conditional on the graph hypotheses; it neither constructs a uniform expander family nor assumes an uninspected existence theorem.

This is a specialization and reproduction of known graph and parity-rank mechanisms, not a certified new lower-bound theorem. It addresses the common-order sum representation motivated by L029. It does not cover sums with different orders, unrestricted arithmetic circuits, or reduced ER data in general. No ER ancestry embedding, optimal-proof or every-certificate hardness, or decision-time lower bound follows here.

## Proof

**Graph-source applicability and finite-size audit (2026-10-06).** Put k=floor(n/2), P={y_1,...,y_k}, and Q=V\\P. Singleton expansion gives deg(v)>=epsilon>0 for every vertex, since n>=2. Thus G has no isolated vertices, the positive graph CNF in the source has variable set exactly V, and its half-prefix is our cut. In the cited Lemma 18 proof, write R for the union of the solid neighborhoods of j chosen pairs. Each chosen pair is an edge ab; both a and b belong to N[a] intersect N[b]. Consequently |N[a] union N[b]|<=2(Delta+1)-2=2Delta and |R|<=2Delta*j. The source's count does not require the false bound |N[v]|<=Delta. With A=P\\R and B=(external neighborhood of A)\\R, its two stopping cases give j>=k/(2Delta) when A is empty, or j>=epsilon*k/(2Delta*(1+epsilon)) when B is empty. Here k>0 and k>=n/4 for n>=2. Since 0<epsilon<1, both bounds imply j>=epsilon*n/(16Delta). This checks equations (7)/(8) of the cited proof, without replacing its graph construction or using its OBDD conclusion.

**Thin the graph witness without changing the cut.** Apply the cited half-prefix claim to obtain (a_i,b_i) with a_i in P and b_i in Q. The source uses positive clauses (a OR b). Its claim is a graph-adjacency statement, independent of the clause sign; we use that graph statement for the independent-set indicator, whose clauses would instead be (NOT a OR NOT b). No source subfunction or sign-matrix conclusion is imported for this changed predicate.

Consider the subgraph induced by B={b_1,...,b_q}. It has maximum degree at most Delta. Repeatedly select an available vertex and delete it and all of its available neighbors. Each selection deletes at most Delta+1 vertices; the selected set B' is independent. When all q vertices have been deleted, its size r satisfies q<=r*(Delta+1). Thus

r >= q/(Delta+1) >= epsilon*n/(16*Delta*(Delta+1)) = c n.       (1)

Retain exactly the pairs whose suffix endpoint lies in B'. Write their endpoints as alpha_1,...,alpha_r in P and beta_1,...,beta_r in Q. The alpha endpoints remain independent, the beta endpoints are now independent, and the original diagonal-cross-adjacency property remains true after taking a subset. Consequently the graph induced by these 2r endpoints has **exactly** the r edges {alpha_i,beta_i}. No additional endpoint edge remains. The extra thinning, rather than the source's almost-induced condition alone, is what supplies this fully induced matching.

**Restrict the cut matrix exactly.** Let M have rows p in {0,1}^P and columns z in {0,1}^Q, with M[p,z]=f_G(p,z) in F₂. Restrict its rows to assignments that are zero on P\\{alpha_1,...,alpha_r}, and its columns to assignments zero on Q\\{beta_1,...,beta_r}. These are actual subsets of rows and columns, not an averaging operation. In particular all removed matching endpoints and all vertices outside the selected pairs are fixed to zero.

An edge incident to any fixed-zero vertex cannot violate independence. By the fully induced conclusion, the only remaining constraints are that alpha_i and beta_i are not both one, for 1<=i<=r. Label a restricted row by S={i:p_(alpha_i)=1} and a restricted column by T={i:z_(beta_i)=1}. Every subset of [r] occurs on each side, and the restricted entry is exactly

M'[S,T]=1 iff S intersect T is empty.                         (2)

Use Stasys Jukna, *Boolean Function Complexity: Advances and Frontiers*, author-hosted [bool-V7 draft](https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf), §4.3, **Lemma 4.11**, printed pp. 100–101 (PDF pp. 107–108). In that inspected draft, D_(r,t) has rows and columns all subsets of [r] of size at most t, and disjointness entries. For 1<=t<=r its rank over GF(2) is sum_(i=0)^t binom(r,i). Here r>=1 by (1), and (2) is precisely D_(r,r), up to row and column ordering. Therefore

rank_(F₂) M' = sum_(i=0)^r binom(r,i) = 2^r,
rank_(F₂) M >= 2^r.                                         (3)

The full rank is imported with its field and parameter range; no real-rank transfer or reproof of disjointness rank is needed. The second inequality holds because deleting rows and columns cannot increase matrix rank.

**Factor every diagram at this same dense cut.** Since n>=2, 1<=k<=n-1 and level k+1 is nonterminal. For D_j let S_j be its supplied state set at level k+1, of size s_j<=w_j. Determinism and dense layering ensure that every prefix assignment p reaches exactly one state rho_j(p) in S_j after its k queries. Define matrices over F₂ by

A_j[p,u]=1 iff rho_j(p)=u,         p in {0,1}^P, u in S_j;
B_j[u,z]=the terminal value reached from u on z, z in {0,1}^Q.

Each row of A_j has exactly one 1. Thus (A_j B_j)[p,z]=B_j[rho_j(p),z]=f_(D_j)(p,z). Unreachable supplied states cause no difficulty: their columns in A_j are zero. A constant function still has a state at this cut because early terminals are forbidden; redundant queries preserve its value.

The representation identity, interpreted in the same field as (3), gives

M=sum_j A_j B_j=[A_1 ... A_m] [B_1; ...; B_m].                (4)

The inner dimension of this horizontal/vertical concatenation is sum_j s_j, so

rank_(F₂) M <= sum_j s_j <= sum_j w_j = W.                   (5)

This explicit factorization specializes the residual-span mechanism in Henrik Brosenne, Matthias Homeister and Stephan Waack, *Characterizing the complexity of boolean functions represented by well-structured graph-driven parity-FBDDs*, RAIRO Theoretical Informatics and Applications **36(3)** (2002), 229–247, [primary scan](https://www.numdam.org/article/ITA_2002__36_3_229_0.pdf), equations (1)–(11) and **Lemma 1.5**, within printed pp. 235–239. It is written out because the source's subsequent quotient-space node characterization is not a raw dense-cut width equality. We do not reprove that characterization or use it to count sparse levels. Every factorization in (4) uses the same partition P,Q; different-order sums would not justify it with the individual diagram widths.

Combining (1), (3) and (5) yields W>=2^r>=2^(c n), as claimed. An empty list cannot satisfy the representation hypothesis: f_G(0)=1, whereas its F₂ sum would be zero. For fixed epsilon and Delta, c is positive and fixed, so 2^(c n) exceeds every fixed polynomial in n along an unbounded graph family. No asymptotic loss or uncharged number of summands is hidden in the bound.

**Verification and qualifications.** The argument consists of a greedy count, an exact row/column restriction, a cited F₂ rank theorem and the explicit matrix identity (4). These provide all-size evidence; a finite numerical rank calculation would not verify the graph hypotheses or the all-order bound and was not run. The canonical source assessment is `drafts/literature/2026-10-06-expander-parity-obdd-total-width.md`. Its prior searches found the supporting mechanisms without an inspected full-statement match; that does not establish originality. This is not a candidate resolution of P versus NP.

**Separate critical audit, 2026-10-06.** Under the preexisting SPECIALIZE scope in `drafts/literature/2026-10-06-expander-parity-obdd-audit.md`, the full informal argument was checked without finding a substantive defect. The statement, exponent and local dependencies are unchanged. The source applicability and rounding check is written above; the remaining load-bearing checks are as follows.

The greedy suffix selection deletes at most Delta+1 of the q distinct suffix vertices per choice, so its integer output satisfies r>=q/(Delta+1)>0 and hence r>=1. Distinctness of both endpoint lists and their separation into P and Q prevent vertex identifications. Prefix independence, suffix independence and diagonal cross adjacency exhaust every possible edge among retained endpoints. Edges incident to discarded endpoints also disappear from the independence constraint because those endpoints are fixed to zero. Thus (2) includes the empty subsets and every other row and column of D_(r,r), with no extra factor, sign change or omitted constraint. The reused Jukna theorem's field is F₂ and its permitted parameter r is positive; its conclusion gives full rank, not just distinct residuals.

For every summand, exactly k queries precede the same level k+1. For n=2 this is level 2 and remains nonterminal; for general n>=2 the same follows from k<n. Every prefix selects one supplied state, and all remaining queries are precisely Q in the common order. The factorization therefore computes the full matrix before its restriction. Zero columns handle unreachable states and dense constant diagrams still supply a cut state. Concatenation in (4) is valid for any finite nonempty list regardless of repeated summands or cancellations, since it represents addition over F₂ and has inner dimension sum_j s_j. The empty list is separately impossible at the zero assignment. Finally r>=c*n and W>=2^r yield the stated real-valued lower bound without rounding down its exponent. Fixed epsilon and Delta are essential for the family-level superpolynomial conclusion. These checks supply informal verification of this restricted input, not a new bound, proof-system lower bound or independently verified formal proof.

## Mathlib

Full matching coverage and the specific supporting graph/rank theorem names have not been checked in Mathlib. No absence claim is made. The named primary graph witness and disjointness-rank input above supply the mathematical references; the dense common-cut specialization is proved explicitly here.
