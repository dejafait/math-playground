# L111 — Copy-ancestry simulations with total support at most 2S

## Hypotheses

Work over F₂ with the exact ordered, finite acyclic graph semantics of
L035 and L038. Fix L110 §§2–3's job-7 recipe: the original-only operands
F,G are specified independently of W from source record 78, events
2642–2643 and `scripts/four-rule-extraction/output-493/restricted-boolean.json`,
`jobs[7]`. L036 (5)–(9) fixes that job's operands and outer context.
This is a symbolic statement conditional on the following graph hypotheses,
not a fresh reception of those files or their byte binding.

For each edge pair of F,G recompute L035 (2)'s ordered central list from
their original labels. Retain every pair with a literally nonempty list,
with multiplicities; omission is not based on a vanishing polynomial.
R is the independent L035 (4) graph with four fresh whole-operand copies
per retained pair, designated roots in F-prefix/G-prefix/G-suffix/F-suffix
order, central edges, four constant connectors and fresh common roots.
R is constructed from F,G's original lists, never W's restrictions.
W uses the same branches, central occurrences, connectors and common roots,
replacing each of the four copies by L097 §22's designated-path restriction.
If distinct designated roots have no path, that restriction retains both
roots and no edges; if they coincide, it retains the one root and no edges.
All ancestry maps are literal vertex/edge occurrence maps, with no shared
copy interiors. Hypotheses include the exact labels, roots and ordered lists.

For m in {free, zero, axiom}, let W_m,R_m be the six explicit local-mode
graphs of L110 §3, before constant closure. Split affine labels per edge
into singleton coefficients over F₂. Original/constant edges remain;
placeholders remain in free mode, are deleted in zero mode, and are replaced
in axiom mode by the complete ordered dictionary word gadgets of L038.
Word interiors are fresh for each occurrence and have no other incidence;
an empty word uses one constant-one edge, and an empty list adds no edge.
The fixed job's labels are already singletons and its dictionary is the
complete six-original/21-placeholder dictionary, including unused entries.
Original labels with zero coefficient contribute no normalized edge.
Scalar one, original letters and placeholders have disjoint types.

In each normalized graph, parallel occurrences are retained; reachability
below ignores their labels and does not cancel parallel edges. Scalar
adjacency subsequently sums their coefficient bits modulo two. This graph
normalization is not deletion of occurrences from the original structural
receiver. In particular original zero-labelled occurrences, if allowed in
a generalized input, still need their separate structural checks.

Write n_H,e_H,l_H for a mode graph's vertex, edge and written singleton
label-entry counts, and g(H)=n_H+e_H+l_H. Set

    V = sum_m (n_(W_m)+n_(R_m)),
    S = sum_m (g(W_m)+g(R_m)).                            (1)

All six endpoints are explicit rooted graphs with at least one vertex;
all substituted gadget vertices, edges and label entries are included.
S is not the size of the original proof, source trees, operand enumeration,
full dictionary encoding, a proposed wire format or a historical invocation.

## Conclusion

There are, for each mode, explicit acyclic intermediate linear
representations Q_W,Q_R,T and four simulation arrows

    W_m <- Q_W -> T <- Q_R -> R_m.                        (2)

An arrow A -> B uses the source convention X with rows indexed by A and
columns by B. For the finite right-closed representations

    alpha_H = eta_H K_H,  M_(H,a) = E_(H,a) K_H,
    beta_H = theta_H,     K_H = sum_(k=0)^(n_H-1) E_(H,0)^k,

every arrow satisfies exactly

    alpha_A X = alpha_B,
    M_(A,a) X = X M_(B,a) for every alphabet letter a,
    beta_A = X beta_B.                                   (3)

All X are partial permutation matrices, including the all-zero matrix.
Across all twelve arrows their total number of nonzero entries is at most
**2S**, uniformly in operand size. The nine intermediate graphs have total
vertex/edge/label size at most 3S/2; endpoints and intermediates together
have size at most 5S/2. These counts are before constant closure.

Thus the three equalities W_m=R_m have explicit sparse simulation chains.
Their semantic equality was already proved by L097 §22; the added local
input is the oriented chain, closure compatibility and support ledger.
This is REPRODUCTION under the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-26-copy-ancestry-sparse-construction.md`, not a new
PIT theorem or a certified originality claim. The separate conceptual audit
in §7 finds no substantive defect under these hypotheses. It is not a finite
received certificate, an implementation, a cap pass or a solution of P versus NP.

## Proof

### 1. Imported results and the specialization

Import Zoltán Ésik and Andreas Maletti, *Simulation vs. Equivalence*,
[2010 author manuscript, Definition 3.1 and soundness, p.2; Theorem 4.2
and Corollaries 4.4–4.5, p.3](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
The simulation convention is precisely (3), and each arrow implies equality
of recognized series. F₂ is a finite semiring; no positivity or
characteristic-zero hypothesis is needed. The qualitative existence
theorems do not supply the bound in (1); no such bound is imported and no
existence theorem is reproved. Jacques Sakarovitch's
[*Rational and recognisable power series*, draft 19-Sep-2008, Definition 11,
Proposition 12 and Definitions 12–13, pp.26–27; Theorem 24, pp.58–59](https://perso.telecom-paristech.fr/jsaka/ENSG/MPRI/Files/References/JS-HWA.pdf)
corroborates the oriented field convention; no arrow is reversed by
transposing its matrix without checking its equations.

Reuse the assessed pruning precedent of Raz–Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author manuscript, Lemma 2 Steps 1,3,5, pp.5–6](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
only for separate graph composition and pruning, with L097 §22 supplying
the exact arbitrary-root occurrence restriction. Do not import its
formula-input/homogeneous size bounds for these graphs.

L038 and L110 §4 provide the finite right-closure coefficient semantics.
Their primary inputs are Kiefer,
[*Notes on Equivalence and Minimization of Weighted Automata*,
arXiv:2009.01217v1, §§1–3, pp.1–5](https://arxiv.org/pdf/2009.01217v1),
and Mohri,
[*Generic Epsilon-Removal and Input Epsilon-Normalization Algorithms for
Weighted Transducers*, IJFCS 13(1):129–143 (2002), author manuscript,
Definitions 4–5/Theorem 1, pp.4–6; acyclic case, pp.10–11](https://cs.nyu.edu/~mohri/pub/ijfcs.pdf).
Only finite constant segments are used. An infinite F₂ closure is neither
defined nor needed. Below we check the additional intertwining equations,
which do not follow just by citing equality-preserving epsilon removal.

### 2. Ancestry identifies the entire accepting core

Map W's common roots to R's common roots. Map a vertex in a retained copy
to its original vertex in R's corresponding whole copy, using the branch
index and one of the four copy positions. Map each retained edge occurrence
to its original occurrence; map connectors and central occurrences by their
same branch and list positions. Call the resulting vertex injection iota.
It is injective because copy interiors are disjoint and each restriction
map is injective. It preserves both roots. The edge map is also injective
and preserves incidence and the full written label. These are consequences
of the two independently specified recipes, not definitions of R from W.

Every accepting R path chooses one branch and traverses its four copies
between their designated roots. L035's construction excludes other
cross-copy edges; leaving an exit internally cannot return to that exit in
a DAG. L097 §22's occurrence restriction therefore retains every edge and
vertex on that path. Conversely, every W path maps edge by edge into R.
These are inverse occurrence maps on accepting paths, including empty
subpaths within any copy. This reuses that existing path-bijection result;
we need the additional injective ancestry, not only polynomial equality.

Extend iota separately to each mode. Matched old edges have identical
per-edge normalizations. For each retained placeholder occurrence, each
dictionary word occurrence and each internal position, map its W gadget
vertex to the corresponding R gadget vertex. Different occurrences and
positions remain distinct. This gives an injection iota_m on all mode
vertices and a compatible edge-occurrence injection. Zero-mode deletion
and empty word lists delete the same matched edges; an empty word has its
matched constant edge, without an internal vertex.

Every accepting R_m path contracts to an accepting base-R path: each gadget
interior has only its prescribed word-path incidence, so an accepting path
cannot enter or leave a word at an internal point. Contraction preserves
the order of old edges; normalized singleton choices remember their
original edge and token. The base path lifts to W by the preceding result.
Keeping the same token and word occurrences then lifts the original mode
path to W_m. Conversely iota_m maps any W_m accepting path into R_m.
This argument also covers a constant-only word, per-edge zero normalization
and cancellation between parallel occurrences: reachability is structural,
before scalar parity is taken.

For any mode graph H with roots s,t, let U_H be its vertices reachable from
s, including s. Let C_H be the vertices in U_H from which t is reachable;
if t is not in U_H, C_H is empty. A vertex is in C_H exactly when it lies
on an accepting path. Moreover, every edge occurrence with both endpoints
in C_H lies on an accepting path: concatenate an s-to-tail path, that edge
and a head-to-t path. A repeated vertex would be a directed cycle, so this
is a path in the DAG. These statements concern paths, not nonzero values.

The mode path maps thus identify every vertex and every edge occurrence of
H[C_H] on W's side with those on R's side, including their labels. The
restriction of iota_m is a graph isomorphism of these induced accepting
cores and preserves their initial/final root positions. It is surjective
on vertices and edges because each core item lies on an accepting path
which lifts. It is injective because the full ancestry map is injective.
No equality of scalar adjacency matrices is being substituted for this
occurrence-level statement. Retained occurrence order is checked via its
ancestry indices even when the two global numberings differ.

### 3. Two different deletion directions

Fix H=W_m or R_m. For its preclosure matrices use rows as edge tails and
columns as heads. Let E_(H,0) be the constant adjacency and E_(H,a) each
letter adjacency, each obtained by parity of all relevant edge occurrences.
The endpoint boundaries are eta_H=e_s (row) and theta_H=e_t (column).

Let Q_H=H[U_H], keeping all occurrences induced on U_H. Its boundaries are
eta_Q=e_s and theta_Q equal to e_t if t belongs to U_H and zero otherwise.
A zero final column is allowed for an intermediate linear representation;
it is not a rooted graph with a fictitious exit. Define the inclusion

    J_H(u,v) = 1 if v is the original vertex u, else 0,
    J_H has dimensions |U_H| by n_H.                     (4)

There is no edge from U_H to its complement: following that edge would
make its head reachable. For every b in {0} union the alphabet, this gives

    eta_Q J_H = eta_H,
    E_(Q,b) J_H = J_H E_(H,b),
    theta_Q = J_H theta_H.                               (5)

For clarity, the transition equality's entry (u,v) is the same adjacency
bit on both sides if v is in U_H; otherwise its left side is zero and its
right side is zero by the no-edge property. The initial equality uses
s in U_H. The final equality holds whether or not t is reachable.
Thus this deletion gives the arrow Q_H -> H, not H -> Q_H.

Number the common nonempty core C by R_m's old vertex order, using the
isomorphism above to give W's core the same numbering. Let T be that
labelled graph with its s,t unit boundaries. If C is empty, instead let T
be the one-state, edgeless representation with both boundary vectors zero.
This conventional zero representation avoids an empty-root convention.
The same T is independently obtained from either endpoint; it need not
be recovered from the polynomial of either endpoint.

For nonempty C define P_H with rows indexed by U_H and columns by T:

    P_H(u,c) = 1 if u represents common-core vertex c,
               and 0 otherwise.                         (6)

For empty C take the |U_H|-by-1 zero matrix. If C is nonempty there is no
edge in Q_H from U_H minus C_H into C_H, since its tail would then reach
t. All edges inside the core agree with T, occurrence by occurrence, so

    eta_Q P_H = eta_T,
    E_(Q,b) P_H = P_H E_(T,b) for every b,
    theta_Q = P_H theta_T.                               (7)

Indeed for a row u in C_H the transition entries are its reindexed core
adjacency; for a row outside C_H they are zero by the no-incoming-edge
property. Nonempty C_H implies an s-to-t path, hence contains both s,t,
which checks the two boundaries. If C_H is empty, t is not in U_H:
otherwise its empty t-to-t path would put t in C_H. Consequently theta_Q
is zero and all three equations hold with P_H=0 and eta_T=theta_T=0.
Thus this deletion gives Q_H -> T. It is distinct from (5).

Equations (5) and (7) prove the four raw constant/letter arrows in (2).
They also explicitly cover vertices dead on either side of a designated
subpath. An arbitrary one-step projection deleting all dead vertices
need not have both no-crossing properties and is not used here.

### 4. The same maps survive finite right closure

For any of these arrows A -> B, let X be J_H or P_H. We have established
eta_A X=eta_B, E_(A,b)X=XE_(B,b) for every b including 0, and
theta_A=X theta_B. All intermediate graphs are acyclic. By induction on k,

    E_(A,0)^k X = X E_(B,0)^k     for every k >= 0.       (8)

Take d=max(n_A,n_B). Each constant matrix has its nth power zero. Summing
(8) for k=0,...,d-1, with terms beyond each nilpotence bound equal to zero,
therefore gives K_A X=X K_B. This also applies to the one-state zero
representation, whose E0=0 and K=I. Thus

    alpha_A X = eta_A K_A X = eta_A X K_B = alpha_B,
    E_(A,a) K_A X = E_(A,a) X K_B
                  = X E_(B,a) K_B = X M_(B,a),
    beta_A = theta_A = X theta_B = X beta_B.              (9)

These are exactly (3). No dense matrix K is included as unchecked evidence;
the finite sum here is mathematical notation. There is a K before the
first letter and after every letter, including the last. In particular
the empty-word coefficient is eta K theta. It is covered by (9), not by
replacing it with eta theta. Imported simulation soundness gives equality
along every arrow; equality is symmetric, so the zigzag gives W_m=R_m.
We never assert that reversing an arrow transposes a valid simulation.

### 5. Support, intermediate sizes, vectors and checking work

For one mode put u_W=|U_(W_m)|, u_R=|U_(R_m)| and
t_m=|C_(W_m)|=|C_(R_m)|. Equations (4) and (6) give the exact total support

    nnz(J_W)+nnz(P_W)+nnz(P_R)+nnz(J_R)
      = u_W + u_R + 2t_m
      <= 2(n_(W_m)+n_(R_m)).                            (10)

Here 2t_m<=n_(W_m)+n_(R_m); in the empty-core case both P supports are
zero, even though T has one dummy state. Summing (10) proves total support
<=2V<=2S. Hence the requested uniform constant is C=2. These are four
separate factors per mode. No bound on a multiplied endpoint transfer
matrix is assumed or needed.

Q_W,Q_R are induced subgraphs, so their total size in one mode is at most
g(W_m)+g(R_m). Nonempty T is occurrence-isomorphic to an induced subgraph
of each endpoint; hence g(T)<=min(g(W_m),g(R_m)). If T is the dummy zero
representation, g(T)=1 and the same bound holds because both endpoints
have at least one vertex. Thus intermediate size is at most 3S/2 summed
over modes, and all fifteen graph instances together have size at most
5S/2. This includes isolated vertices and label occurrences, with no
discount for sharing graph records between endpoints or intermediates.

All twelve matrices have at most one 1 per row and column. If local vertex
indices use b=ceil(log2(3S+1)) bits, listing both indices and the coefficient
of every nonzero requires at most 2S(2b+1) bits, before framing. Twelve
dimension pairs need at most 24b additional index bits; directions, mode
names and list framing must also be encoded. This is an index ledger,
not a specified or measured wire format. Literal original names and the
complete dictionary are outside this index count and remain required.

Before closure each of the fifteen eta/theta pairs has at most one nonzero
in either vector, hence at most 30 nonzero positions total. Dense vectors
before or after closure require at most twice the total number of states,
which is at most 5V<=5S field bits. Alpha may be dense. K and M_a may be
dense, and the argument provides no linear bound for storing them. They
are not intermediate graphs and are not charged as if sparse matrices.
If desired, alpha can be computed by L110 §4's constant-edge sweep, with
one XOR per constant occurrence and initialization of every coordinate.

There is a finite graph-only way to check the arrow premises without
forming K or M_a. From explicit topological orders, compute U and C by
forward/backward reachability sweeps, visiting every occurrence. Check
each induced graph, both boundary vectors and the lists (4)/(6). Check
the two no-crossing conditions used in (5)/(7), and the full common-core
vertex/edge/label bijection. Inspect every normalized letter, including
matched parallel occurrences; unused alphabet letters have zero matrices
on both sides. These stronger occurrence checks imply every raw adjacency
equation, then (8)–(9) imply the closed equations. They do not require
materializing a transition table for each absent letter.

For an elementary conservative cost, retain explicit arrays for all graphs,
maps, reachability marks and topological ranks. Verify rank permutations,
map injectivity and matched occurrence lists by nested scans if necessary;
there are O(S) entries of bounded arity, so O(S^2+q+1) bounded index/letter
operations suffice for these graph-only checks, where q is the sum of
the three alphabet sizes (39 for this job). All vertex/edge identifiers
can be dense. An individual index comparison or addition uses
O(log(S+q+2)) bit operations. To avoid unit-cost random access, realize
each array lookup/update by a sequential scan of at most O(S+q+1) records.
This gives the conservative bound O((S+q+1)^3 log(S+q+2)) bit work and
O((S+q+1)log(S+q+2)) retained bits for these additional tables. The
reachability and optional alpha sweeps are over explicit adjacency lists;
their lookups are charged by the same sequential-scan allowance. These
are algorithmic bounds for these graph checks with dense identifiers,
not measurements of Python, parsing, allocation or old code.

In particular this ledger starts with six explicit graphs and their
specified ancestry, after independent recipe/binding checks. It cannot
bound those earlier checks solely in S: enumerating all edge pairs of
F,G can involve many literally empty central lists absent from both W
and R. The original proof, operands, complete dictionary, source trees,
input decoding, ancestry verification against those inputs and evidence
serialization must be charged separately by any eventual receiver. No
linear total receiver cost or numerical cap fit follows from (10).

### 6. Boundary cases and scope of the result

The proof did not require extremal roots. Incoming entry edges and outgoing
exit edges are handled by their respective reachability conditions; arrows
keep the full raw transition equation, not just accepting path values.
Distinct roots with no path give the dummy zero T and zero P maps.
Coincident roots in a DAG have exactly the empty path and no nonempty
cycle; their core is one vertex, and the initial/final equations and K
include that empty contribution. Within a branch these cases apply to
each independent copy as well as to the common-core construction.

Constants and empty-word substitutions are genuine constant edges. An empty
central list creates no branch in either endpoint. Zero-mode deletion can
leave reachable vertices but no accepting path; theta_Q=0, rather than a
false claim that eta_Q or alpha_Q is zero, makes (7) valid. In the fixed
L035 branch every accepting base path has one central placeholder, so the
zero mode indeed has empty accepting core. A nonzero free or axiom graph
whose entire polynomial cancels can still have a nonempty structural core;
the construction retains it and all parallel multiplicities. It never
uses a semantic zero test to choose a state set.

Fresh gadget interiors, exact token/word occurrence indices and four-copy
factor order are essential to §2. Arbitrary equal polynomials need not
have occurrence-isomorphic cores and are not covered by that argument.
L110 §21's constructor theorem remains conditional on its exact input and
comparison hypotheses; it is not a substitute for a strict arbitrary-input
decoder. L108 §§11,13's caller/byte assumptions are unchanged when those
interfaces are used. Scalar simulations cannot certify structural occurrence
reception, source-tree identity or a literal propositional inference.

The three W=R chains do not supply L110's separate Dcomm receipt for
R(x,A)=fg+gf, even though L035 proves that semantic identity. Nor do they
produce the coordinate arrays required by L110's old contract. Attempts
044–046, their failed receipts and historical administrative stop remain
intact. Wire/work/live fit, strict reception, later jobs, complete Boolean
and K/H/nonzero-fJ reception, certificate availability, L087 W₂ and
unrestricted ER/Frege/SAT consequences remain unresolved. No finite
mathematical script, file replay or numerical experiment was used for
this all-size symbolic construction.

### 7. Separate conceptual audit — step 523, 2026-10-26

**Scope and verdict.** This is one RESEARCH / REPRODUCTION / proof_audit
under the prior SPECIALIZE assessment
`drafts/literature/2026-10-26-copy-ancestry-sparse-critical-audit.md`.
The entire statement and proof above were audited, with the relevant full
passages of L035 (2)/(4), L036 (5)–(9), L038's local transports, L097 §22,
L110 §§2–4,21 and the input/administrative qualifications in L108 §§11,13
and L110 §24. Reuse the precise primary statements cited in §1 and the
completed steps 519/520 source comparison; no source theorem is newly
retrieved or reproved. No substantive defect was found in the conditional
occurrence-core construction, any of the twelve raw/right-closed arrows,
or the stated quantitative ledger. The following are independent checks
of those claims, not additional existence or complexity theorems.

**Occurrence ancestry and all three modes.** L036 (5)'s operands are
original-only graphs formed from the normalized input suffixes and their
selected prefix edges, not previously constructed Boolean witnesses.
L110 fixes their independent whole-operand restrictions before constructing
either W or R. The hypotheses here further require complete equality to
those recipes; a file name or old successful status is not that equality.

For each retained edge pair, L035 (4) fixes the four copy roots and their
order. L097 §22 retains exactly the designated-path occurrences within
each copy, except for the specified edgeless root retention in the no-path
case. Distinct copy positions and branch indices distinguish all vertices
and edges even when they have the same original operand index. Accordingly
the ancestry map is injective on the whole of W, including dead retained
roots, not just on accepting paths. No branch can be entered twice or
switched: the only inter-copy edges are its four prescribed connectors
and central edge occurrences. An internal departure from an exit cannot
return to that exit in a DAG. These facts give the exact accepting-path
bijection required by §2, for nonextremal and coincident copy roots too.

The mode lifting needs the occurrence bijection, not just the known
free-polynomial equality. In free mode each singleton edge retains its
old edge/token indices. Zero mode removes the same placeholder singleton
occurrences on the two sides. In axiom mode each word path retains old
edge, token, dictionary-word occurrence and position indices. A fresh
internal word vertex has only its own prescribed predecessor/successor
incidence and is never a root. Hence an accepting normalized R path
contracts to an old accepting path with specified singleton/word choices;
the old path lifts to W, and the same choices recover the entire mode
path. An empty dictionary word contracts its constant edge; an empty list
has no path to contract. Deleted zero coefficients supply no normalized
path, and any surviving choice still lifts. Constants retain their scalar
type. Parallel edges and repeated words remain distinct in this argument
even if their final contributions cancel in F₂.

For a DAG, a vertex is in C exactly when it lies on an accepting path.
For any edge with both endpoints in C, concatenating the reachable prefix,
the edge and a suffix is an accepting path: a repeated vertex would give
a directed cycle. Thus lifting all accepting paths is surjective on the
entire induced core's vertices and edges. Together with injective ancestry
this proves the claimed whole-core isomorphism, with roots, singleton
labels and occurrence indices preserved. There is no inference from equal
scalar series to isomorphic graphs. In particular a zero-valued series
can have a nonempty core, which this construction does not delete.

**Independent matrix and boundary check.** For a nonempty core, reorder
H's indices as (C,D,Z), where D=U minus C and Z is the unreachable set;
on C use the common T numbering. For every constant or letter b, its
adjacency has the block pattern

    E_(H,b) = [ E_CC  E_CD    0  ]
              [   0  E_DD    0  ]
              [ E_ZC E_ZD E_ZZ ].

The right zero block in the first two rows follows from reachability.
The D-to-C zero block follows because such an edge would make its tail
coaccessible. No claim sets E_CD, E_ZC or E_ZD to zero. Q is the upper-left
two-by-two block, T is E_CC, J embeds (C,D), and P retains just C, with
the stated ancestry permutation. Block multiplication therefore gives
E_Q J=J E_H and E_Q P=P E_T separately. Both boundaries s,t belong to C,
so eta_Q J=eta_H, theta_Q=J theta_H, eta_Q P=eta_T and
theta_Q=P theta_T, with exactly the dimensions in (4)/(6). This checks
incoming edges at s, outgoing edges at t and other dead transitions,
which mere equality of accepting values would not check.

When C is empty, t is not reachable (its empty t-to-t path would otherwise
put it in C). Q has eta_Q=e_s but theta_Q=0. J still has the same reachable
inclusion equations; P is a |U|-by-1 zero matrix and T has zero eta, theta
and adjacency. All three P equations are then literally zero equalities.
The nonzero eta_Q must not be replaced by zero. The dummy's dimension is
one, but its contribution is zero, not the unit empty word of a rooted
one-state graph. If the roots of a graph coincide, C instead consists of
that one vertex, its adjacency is zero, and both unit boundaries preserve
the empty-word contribution. For a designated no-path factor inside a
branch, its retained roots cannot produce a complete accepting path.

**Closure and equality.** The raw constant equation implies
E_A0^k X=X E_B0^k for every k, including k=0 for rectangular X. For
d=max(n_A,n_B), both constant matrices have vanished in powers at least
d. Summing k=0 through d-1 is therefore precisely K_A X=X K_B, regardless
of the different truncation lengths in their original definitions. This
also holds for the dummy, where K=I and the associated P=0. Multiplication
on the left by eta_A or E_(A,a), followed by the respective raw equations,
gives alpha_A X=alpha_B and M_(A,a)X=X M_(B,a); beta is unchanged.
This confirms right closure, including the trailing K, rather than a
left-closure or no-trailing-closure variant.

To check the consequence directly under the imported source convention,
the transition equations give M_A(w)X=X M_B(w). Thus
alpha_A M_A(w) beta_A=alpha_A M_A(w)X beta_B
=alpha_B M_B(w) beta_B for every word. At the empty word this uses the
closed alpha=eta K and therefore includes all constant paths. Applying
equality along the four arrows gives each W_m=R_m without reversing a
simulation. Free, zero and axiom alphabets have respectively 27, 6 and 6
letters; scalar one is excluded, and unused letters have zero adjacency
on both sides. In zero mode every base accepting branch would need its
deleted central placeholder, so the core is empty. Free/axiom cancellation
does not alter the structural argument. No finite word enumeration is used.

**Independent ledger check.** For each mode the exact support is
u_W+u_R+2t. Since u_H<=n_H and t<=min(n_W,n_R), this is at most
2(n_W+n_R). For an empty core the two P supports are zero. Summing gives
at most 2V<=2S across twelve separate matrices; every J and P has at most
one nonzero per row and column. No product of factors is charged as sparse.

For each mode, Q_W and Q_R are induced subgraphs and their summed g is
at most the summed endpoint g. If t>0, T is an induced occurrence graph
of either endpoint; if t=0, g(T)=1<=min(g(W),g(R)). Hence the nine
intermediates have summed g<=3S/2 and all fifteen graphs have g<=5S/2.
The same argument applied to vertex counts alone gives at most 3V/2
intermediate states and 5V/2 total states, including all dummy states.
All word interiors, isolated vertices, parallel edges and singleton-label
entries are counted before closure; shared data receives no discount.

Each preclosure boundary is zero or a unit vector. Fifteen representations
therefore use at most 30 nonzero boundary positions, while two dense vectors
per state use at most 5V field bits. Closure can densify alpha, K and M_a;
only the boundary-vector bit bound survives as stated, not a sparse bound
on K or M_a. With b=ceil(log2(3S+1)), every local dimension and index fits:
even the sum of all state counts is at most 5S/2<3S+1. At most 2S support
entries with two indices and one coefficient use at most 2S(2b+1) bits;
the twelve ordered dimension pairs use at most 24b more. This is exactly
the claimed incomplete index ledger, with framing, source names and full
dictionary still outside it. It establishes no numerical wire cap.

For the graph-only work assertion, explicit graphs, maps, ranks, marks
and occurrence lists contain O(S) bounded-arity records. Nested scans
check rank permutations, injectivity, induced edges, the two crossing
conditions and the core bijection with O(S²) index/letter operations.
Reachability takes forward/reverse topological sweeps; scanning the whole
edge list per vertex is already within that bound. Comparing all matched
occurrences handles label multiplicity without enumerating alphabet-sized
transition tables. Scanning alphabet declarations adds O(q+1), with q=39
here. These operations use dense indices/letters of O(log(S+q+2)) bits;
raw long names have not been made unit-cost inputs. Sequentially scanning
O(S+q+1) records for each access gives the claimed conservative
O((S+q+1)³ log(S+q+2)) bit-work bound and
O((S+q+1)log(S+q+2)) retained bits for these tables. No nested scan
materializes O(S²) pairs. Optional alpha sweeps fit the same allowance.
These are mathematical bounds for the stated graph checks after input
preparation, not bounds on the entire source/recipe/decoder computation.

**Audit boundary and downstream use.** In particular S need not pay for
operand edge pairs whose central lists are empty, complete source trees,
dictionary payload, binding, original occurrence reception or serialization.
The full input and recipe hypotheses are essential. L110 §21 remains a
conditional static constructor proof; L108's actual-byte/caller assumptions
are unchanged. This audit reads no archived graph certificate and receives
no fixed-job data or finite resource measurement. Attempts 044–046 retain
their precise word/evidence/historical-administrative obstructions.

The result closes the pending conceptual audit of this local structural
input, making it eligible for separately assessed downstream work. It is
new local verification evidence, not a new pruning theorem, an extension
of the support bound, or progress beyond the primary mathematics checked.
It does not supply Dcomm, coordinate evidence for the old contract, strict
reception, wire/work/live fit, later jobs, Boolean/K/H/nonzero-fJ reception,
general certificate availability, L087 W₂ or unrestricted ER/Frege/SAT.
Full matching Mathlib coverage is still not checked. No new mathematical
DAG input, production change, finite experiment or mathematical script is used.

## Mathlib

Full matching coverage for the copy-ancestry chain, its arbitrary-root
cases, right-closure transport and this support/index ledger is **not
checked**. No absence claim is made. The precise primary simulations and
finite-closure sources are cited in §1; the source assessment did not
establish a matching quantitative theorem in S. This is local progress
in a known pruning/simulation specialization, with no claim of progress
beyond all literature or of a resolution of the main target.
