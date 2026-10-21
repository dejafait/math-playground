# L072 — Affine-ABP data after logarithmic original-input deletion

## Hypotheses

Use L037's width-at-most-three original CNF F, valid supplied signed-AND ER
refutation π, and T=2+|F|+|π| in full binary bits. Retain its complete ordered
original clause, Boolean and pair-once commutator axiom list A(x), with
independent placeholders t over the free associative F₂ algebra. There are
n≤T original variables; nonextension proof variables absent from F have
value zero. All names, signed operands, unused extensions and root
associations are retained.

Let G be L071's full Boolean value DAG: shared original-variable vertices,
constants, every extension AND gate and required NOT vertices, including
unused roots. Multiple operand occurrences remain in the gate encoding;
treewidth refers to the underlying simple undirected graph. Supply a set
D of k original-variable vertices, with

    0≤k≤floor(log₂(T+2)),       tw(G−D)≤2.

The set is explicitly named. Its names cost at most O(T²) bits, since each
is an original name already in the input. No restricted ER refutation or
agreement of compilation orders across assignments to D is assumed.

## Conclusion

There is a deterministic polynomial-bit-time construction of complete
L037 data for the unchanged F and π: S=O(T), exact original/constant roots,
exact signed wrappers, faithful x-only affine-ABP representatives r_v,
and affine-ABP witnesses for every extension i with actual signed operands
a,b satisfying the formal identities

    H_i(x,0)=0,           H_i(x,A(x))=r_i+r_a r_b.

Only original Boolean and commutator placeholders occur in H_i. All
separate graph copies, names, roots, source associations and the full
original-axiom dictionary are charged. More generally, the construction
below has one fixed polynomial bound in T and M=2^k. For a fixed polynomial
p(T)=C(T+2)^c, chosen in the proof independently of k and π, put

    Q=2+T+M+p(T).

The aggregate full output length is at most KQ⁸, and construction time is
at most KQ^b for fixed K,b with b≥8. Representatives have formal degree
d=max(1,n). A valid pre-substitution witness-degree parameter is

    h=max(1, max_i(number of edges in the written H_i)),

with an empty maximum taken as zero; h≤KQ⁸ after increasing K. In particular
M≤T+2 gives polynomial bounds solely in T. L037 then supplies a
polynomial-full-bit original-axiom affine-ABP certificate on this class.

This is an informal restricted sufficiency result. The separate step-278
critical audit below finds no substantive defect within its stated promise
and changes neither the theorem nor its bounds. Classification
POTENTIALLY_NEW under the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-logarithmic-input-deletion-data.md`
means only that its comparison did not identify a full matching theorem.
It does not certify originality. Arbitrary ER data, formula-only bounds,
W/V/U and unrestricted SAT decision/separation remain unresolved. This is
not a main-problem candidate.

## Proof

**Imported inputs and specialization boundary.** Reuse L071's all-root
selector compilation and explicit affine graphs for L026's value/K/P/W
recurrences, and L035's audited arbitrary-affine-ABP commutator witness.
The Boolean compiler is Amarilli–Bourhis–Senellart, *Tractable Lineages on
Treelike Instances: Limits and Extensions*, arXiv:1604.02761v1,
Definition 6.4/Lemma 6.6, pp.15–16 and Appendix A pp.28–29
([inspected long version](https://pierre.senellart.com/publications/amarilli2016tractable_long.pdf)).
For each fixed circuit treewidth its running time and OBDD size are
polynomial; the exponent can depend on that fixed width. Its supporting
order bound is Jha–Suciu, *On the Tractability of Query Compilation and
Bounded Treewidth*, ICDT 2012, Corollary 2.14 and section 4
([author PDF](https://homes.cs.washington.edu/~suciu/file38_paper.pdf),
PDF pp.6–7,9). Same-order completion is de Colnet–Ordyniak–Szeider,
*OBDDs, SDDs, and circuits of bounded width: Completeness matters*,
Artificial Intelligence 351 (2026), 104458, Proposition 2, pp.3–4
([published PDF](https://eprints.whiterose.ac.uk/id/eprint/234745/9/1-s2.0-S0004370225001778-main.pdf)).

Separate-graph serial/parallel composition uses Raz–Shpilka,
*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author manuscript, Lemma 2 Step 1, p.5
([PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)).
Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, arXiv:1412.8746v4, Lemma 3.7, p.18
([PDF](https://arxiv.org/pdf/1412.8746v4)), gives a commutator witness for
formula inputs; the arbitrary graph-input bound used here is L035's local
result, not an enlargement of that primary theorem's hypotheses.

These sources and their essential proof cases have ready coverage in the
prior assessment. The additional work is the conditioned-circuit interface
and the ordered recombination below. Boolean Shannon equivalence alone
would not supply the free-ring identities. No compilation, OBDD Apply,
general Boolean-zero witness theorem or unrestricted circuit-to-ABP
conversion is reproved or presumed.

**Conditioned circuits without changing the ER proof.** Fix an assignment
α:D→{0,1}. Begin with G−D. For every operand occurrence whose source was a
deleted original vertex, attach a distinct fresh constant vertex, labeled
with its assigned bit, feeding that same operand position. This includes
operands of NOT gates and both positions of a repeated AND operand. Keep
every remaining vertex and wire, including constants, signs and unused
gates. For each deleted original's own root association add an isolated
constant vertex with its assigned bit. These isolated vertices do not
serve as shared hubs for the replacement wires. Thus this is a complete
Boolean circuit C_α, with inputs exactly the undeleted originals, and all
required original root associations. Induction in the original directed
gate order shows that its associated root values are precisely those of
G at α; replacing inputs by leaves cannot create directed cycles.

Each added nonisolated vertex has just one undirected neighbor. Given a
width-two decomposition of G−D, attach the bag {new leaf, neighbor} at a
bag containing that neighbor. Add isolated vertices in singleton bags,
joined arbitrarily to the decomposition. Coverage and connectedness are
preserved and bag size is at most three. If the graph is empty, start with
the first singleton bag. The number of replacements is bounded by the
number of operand occurrences, O(T), because gates have bounded fan-in.
Hence C_α has O(T) vertices/edges and treewidth at most two. L071's explicit
degree-two elimination algorithm can find its decomposition in polynomial
time, so a supplied decomposition is unnecessary.

Apply only the circuit part of L071: its owner/selector construction
compiles all vertices of C_α simultaneously through one width-at-most-16
single-output circuit. Each bag owns at most three vertices, and the
17-position bag bound is unaffected by fresh constant leaves or isolated
roots. Selectors are removed by restriction before any arithmetic graph
is built. Completion yields all root diagrams in a common order on the
undeleted originals within this branch. Orders for different α can differ.
The compiler's exponent is fixed by 16, never by k.

Write f_(v,α) for branch value representatives. For original variables
outside D these are exactly x_j, for deleted originals they are α_j, and
for constants they are their field values. Signed roots are exactly
1+f_(v,α). For each positive extension obtain an x-only graph from its
compiled diagram. Each extension's output and signed operand functions
obey the actual Boolean AND relation in C_α. L026's suffix proof, realized
by L071's explicit graphs, therefore supplies J_(i,α) with

    J_(i,α)(x,0)=0,
    J_(i,α)(x,A)=f_(i,α)+f_(a,α)f_(b,α).                 (1)

This is an application of the circuit/diagram construction, not of L071
to an invalid restricted ER proof. To justify the precise specialization:
L026's value, K and W inductions use only complete common-order diagrams,
field constants, the Boolean/commutator axiom positions for their input
variables, and the semantic AND equality for identifying the output in
the ordered-multilinear subspace. They never use ER inferences or original
clause axioms. Those hypotheses hold for C_α. Map its subset-variable
Boolean and pair-once commutator placeholders into the corresponding
positions of the unchanged full A. This is an injective alphabet inclusion
and preserves both free-ring identities. No restricted clause list is
needed or substituted into (1). All full original names and A are retained.

Put n'=n−k. Branch value degrees are at most n' (constants have degree
zero), and branch witness degrees are at most max(1,2n'−1). If n'=0,
evaluate all gates as constants and set every J to the distinct-endpoint
zero graph, exactly as in L071. Signed wrappers preserve the same bound.
One fixed polynomial in T bounds all graphs, orders, associations and
construction time for a single branch; the O(T²) set-name framing and full
O(T³) original axiom dictionary are included. No branch-specific exponent
or formula unfolding enters this bound.

**Small indicator products with formal correction graphs.** Choose one
fixed order z_1,...,z_k of D and put

    l_(j,0)=1+z_j,   l_(j,1)=z_j,
    e_α=l_(1,α_1)...l_(k,α_k).

The product is ordered as written; for k=0 it is 1. Each e_α is an affine
path graph with k edges. Finite distributivity, preserving that order,
gives the formal identities

    sum_α e_α=1,       sum_α α_j e_α=z_j.                (2)

For the second identity, expand the product of all earlier sums
l_(q,0)+l_(q,1), the single factor z_j, and all later such sums. Every sum
is 1, with no commutation. The scalars α_j are central.

For every ordered pair α,β construct Q_(α,β) using L026's paired-suffix
recurrence and L071's graph realization on the two complete indicator
diagrams in this same z order. Such a diagram has at most two states per
level: a still-matching state and a dead zero state; redundant tests fill
all later levels. Its free-ring value is exactly the displayed e_α, by
the recurrence with zero mismatching branches. The product representative
P is increasing multilinear in z, and on Boolean assignments equals the
product of the indicators. Hence L026's injectivity in that specific
subspace identifies P with δ_(α,β)e_α. This is a formal equality in that
subspace, not an identification of e_αe_β with a Boolean product.
Consequently

    Q_(α,β)(x,0)=0,
    Q_(α,β)(x,A)=e_αe_β+δ_(α,β)e_α.                    (3)

The diagrams have constant width. L071 gives O((k+1)²) graph records per
Q, with the full original names/dictionary separately charged, and degree
at most max(1,2k−1). Only Boolean/commutator placeholders for D occur.
For k=0 use Q=0: its claimed substituted value is 1+1=0. As with (1),
the recurrence is applicable to these diagrams without constructing an
artificial ER host. This reuses its proved diagram identities, rather
than claiming a new generic product correction theorem.

**Exact representatives and signs.** For every positive extension define

    r_v=sum_α e_α f_(v,α).                              (4)

Use disjoint serial graphs for each summand and a disjoint parallel sum.
For original variables, constants and signed values write the exact roots
required by L037 instead. They equal (4) formally as follows. An undeleted
original has sum_α e_α x_j=(sum_α e_α)x_j=x_j. A deleted original uses the
second identity (2). Constants use the first identity. Finally

    sum_α e_α(1+f_(v,α))=1+sum_α e_α f_(v,α),

so every exact signed wrapper is also its interpolant. These equalities
do not depend on branch orders. Thus (4) can be used for every actual
signed operand in calculations, while the written original and signed
roots have precisely L037's required syntax. For a Boolean assignment
exactly one e_α evaluates to 1, so the representatives are faithful to G
on every original assignment. Every summand has degree at most k+n'=n;
constants and exact wrappers give d=max(1,n).

**One ordered recombination, with both identities.** Fix a definition i
and abbreviate a_α=f_(a,α), b_β=f_(b,β). From the explicit x-only graphs
a_α and e_β, L035 constructs C_(α,β) with

    C_(α,β)(x,0)=0,
    C_(α,β)(x,A)=a_α e_β+e_β a_α.                       (5)

These graphs use only original commutator placeholders. Neither a witness
nor a glued representative is supplied recursively to L035. Define

    H_i = sum_α e_α J_(i,α)
        + sum_(α,β) [e_α C_(α,β) b_β
                         +Q_(α,β) a_α b_β].           (6)

Each product uses fresh disjoint copies of its displayed factors, in the
displayed order. Each summand has a factor J, C or Q vanishing when all
placeholders are zero; hence H_i(x,0)=0 as a free-ring identity.

For the other identity, substitute A in the double sum in (6), retaining
every order and expanding only its finitely many indexed summands:

    sum_(α,β) [e_α a_α e_β b_β + e_α e_β a_α b_β
                 + e_α e_β a_α b_β
                 + δ_(α,β)e_α a_α b_β]
      = r_a r_b + sum_α e_α a_α b_α.                   (7)

The two middle words cancel literally in F₂. The first term uses the
formal interpolant identities just proved, and the diagonal term retains
e_α on the left. The first sum in (6), by (1), substitutes to
r_i+sum_α e_α a_α b_α. Adding (7) cancels that last sum and gives
H_i(x,A)=r_i+r_a r_b. No cross-branch order is identified; no Boolean-only
equality is used to replace a free polynomial in this calculation.

The disjoint sum/product constructions give an acyclic affine ABP for
(6). Connectors have label 1. Within a factor, a path leaving its chosen
exit cannot return there without a cycle, so nonextremal designated
endpoints add no unintended accepting paths. Fresh outer endpoints also
handle zero graphs and empty products. Constants, repeated and
complementary operands, parallel edges and unused extensions are all
covered by (1)–(7). In particular no full accepting path set is enumerated.

**One full-bit and time ledger.** Choose p(T)=C(T+2)^c≥(T+2)^4 large
enough to cover, uniformly, all single-branch data and its compilation bit
time, each indicator and each Q graph with the full original alphabet and
axiom dictionary, their construction time, and all source-name framing.
Such fixed C,c exist by the fixed-width compiler and the polynomial
diagram recurrences above; k≤n≤T. All O(T) roots of a single branch are
already included. Exporting all M branches therefore costs at most Mp(T).
Writing all M² indicator correction graphs separately costs at most
M²p(T), including even a separate dictionary copy per graph if desired.

Every invocation of L035 receives graphs plus complete alphabet/commutator
framing of length O(p(T)); its full output costs O(p(T)^4). Its deterministic
bit time is O(p(T)^a) for one fixed a. Each extension has M J summands and
2M² correction summands in (6), each with a constant number of separately
copied factors of size O(p(T)^4). Thus its graph payload before global
renumbering is O(Mp(T)+M²p(T)^4). There are at most O(T) extensions.
All final value roots, exact signed copies and constant/original roots cost
O(TMp(T)); every signed root receives its own complete underlying graph.
No sharing across output graphs is credited. Retaining branch graphs,
orders and all Q templates adds only the charges already given above.

Total records and existing label payload are at most
O(T M² p(T)^4), after absorbing small cases into constants. Renumbering
vertices, references, source associations and root lists adds at most a
factor O(T+log(M+2)+log(p(T)+2)); this also covers original written names
at every occurrence, even where they were already counted. A further
O(T³) full original dictionary is included. Since T,M,p(T)≤Q, the total
is at most KQ⁸. This deliberately loose bound permits repeated dictionary
copies and retains every operand/sign and unused root. The graph
identifiers need only O(log(Q+2)) bits after dense renumbering.

Enumeration of all M assignments takes polynomial time in T,M. Branch
compilation takes at most Mp(T); indicator pairs take at most M²p(T).
The O(TM²) L035 calls take O(TM²p(T)^a). All remaining operations are
finite loops over these explicit records, graph copies, dictionary
lookups and binary writes. Even naive polynomial string handling bounds
them by KQ^b for a fixed b≥8. Thus output size and construction time both
have fixed polynomial exponents, independently of k, extension depth,
branch orders and the number of graph paths. There is no T^k cost or
exponent polynomial in M.

Every edge label in H_i is affine in x,t. An accepting path in an acyclic
graph uses at most its number of edges, and each edge contributes degree
at most one before axiom substitution. This proves the asserted h, with
no assumption that semantic cancellation bounds syntactic path length.
The output ledger bounds that edge count by KQ⁸. The sharper L071 witness
degree is not claimed after recombination. The abstract value DAG is
still the original acyclic extension/sign structure of size O(T);
internal arithmetic vertices are not additional abstract extensions.

Finally M≤T+2 makes Q and all output/time/degree parameters polynomial in
T. The original refutation was never restricted or replaced, and every
L037 data hypothesis has now been met for that refutation. Its conditional
assembly supplies the stated certificate. L036 is used inside that
existing assembly; no separate new Booleanity claim is needed here.

Attempts 019–021 retain their force for unrestricted OBDD width,
degree-only same-output conversion and the prescribed pair table. Here
branch orders may differ, the structural promise is explicit, and (6)
is an alternative witness. This proves neither small deletion sets for
arbitrary ER proofs nor bounds solely in |F|. No SAT decision consequence
or implementation is asserted by the construction step. Its separate
critical audit follows.

**Separate critical audit, 2026-10-17 (step 278).** This audits the existing
statement under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-17-logarithmic-input-deletion-critical-audit.md`.
It reuses the cited primary compilation/completion and graph-composition
inputs, and the proved L026/L035/L071 interfaces; no stronger source theorem
or new structural promise is imported. The original ER proof and ordered
axiom list are unchanged throughout.

For the conditioned graph, count operand occurrences rather than distinct
neighbors. If a deleted input supplies both positions of an AND, there
are two new leaf vertices, each with that gate as its only neighbor. If it
supplies a NOT or several different gates, each occurrence still has its
own leaf. No leaf is identified with the isolated constant for that input's
root. Thus every new edge is covered by its two-vertex leaf bag, whose
attachment to an existing neighbor bag preserves the occurrence subtree
of that neighbor. An isolated root constant has a singleton bag. Edges
between retained vertices already have their old bags. This proves width
at most two, including disconnected graphs, without a shared constant hub.
The original gate order verifies every conditioned root, including NOT
vertices and unused gates. There are only O(T) occurrences and roots.
The degree-two elimination and reverse-fill procedure in L071 therefore
applies to this explicit graph. Its selector construction has at most
three owned vertices and two child outputs per bag; the bound
3+6+2+6=17 includes the local constant and all five possible OR gates.
Child aggregate outputs occur in adjacent child/parent bags, so constant
leaves and isolated components create no connectedness exception.

Only this Boolean-circuit construction is used from L071. Restricting all
selectors in its one compiled OBDD gives a common induced order within
one branch, and completing that order retains constants and all omitted
original tests. No assertion relates orders from different branches.
L026 (4), (6) and (8) involve only these complete diagrams, their suffixes,
and the original Boolean/commutator positions. Their inductions never use
an ER inference or a clause polynomial. For a conditioned definition the
actual output and signed operands agree in the AND relation on all
assignments to the undeleted originals; their paired representative and
output are in the same increasing-multilinear subspace. Hence precisely
L026's proved injectivity gives (1). Inclusion of the subset alphabet in
the unchanged full alphabet maps each subset Boolean or unordered-pair
placeholder to its actual A position, preserving both substitutions.
Signed auxiliary diagrams equal their exact wrappers formally. No claim
about validity of a restricted ER derivation enters this argument.

For the indicators, the ordered product of the k sums
l_(j,0)+l_(j,1)=1 expands to the first identity (2). Fixing the jth bit
to 1 before expansion gives the second identity, with the scalar bit
central and z_j left at its actual position. Each indicator diagram has
only a matching and a dead state at any level. L026's paired P is in the
increasing-multilinear subspace in the fixed z order, and has the Boolean
values of the product of these two indicators. It therefore equals
delta_(alpha,beta)e_alpha in that subspace. Applying its W identity gives
(3). This does not assert that the raw free product e_alpha e_beta itself
is increasing multilinear or equals that diagonal term. These are exactly
the missing corrections supplied by Q. The O((k+1)^2) graph-record count
follows from L071's paired-state graph with constant width; dictionary
payload is separately retained in p(T).

For exact roots, distributivity in (2) gives the undeleted original x_j,
the deleted original z_j and both constants as written, without moving
x_j through any indicator. Similarly the interpolant of a signed root
equals 1 plus its unsigned interpolant. Consequently every actual operand
in (7), including a signed original or a signed constant, can be replaced
by that interpolant by formal equality. A branch value uses only the n'
undeleted variables and has degree at most n'; multiplication on its left
by an indicator gives degree at most k+n'=n. The exact roots and wrappers
satisfy d=max(1,n). Faithfulness uses the unique selected branch only for
Boolean evaluation, independently of these formal equalities.

Each L035 call receives just a_alpha and e_beta: two explicit x-only
graphs with the unchanged original alphabet and complete commutator
framing. It receives neither J nor any previously glued graph. After A
substitution, its contextual term is
e_alpha a_alpha e_beta b_beta+e_alpha e_beta a_alpha b_beta.
The other contextual term is
e_alpha e_beta a_alpha b_beta+delta_(alpha,beta)e_alpha a_alpha b_beta.
The repeated middle word has identical order in both expressions and
cancels in F₂. Summing the first terms gives r_a r_b by finite
distributivity and the formal interpolant equalities; summing the diagonal
terms gives sum_alpha e_alpha a_alpha b_alpha. By (1), the first sum in
(6) substitutes to r_i plus that same diagonal sum, proving the second H
identity. At zero substitution every complete term has a zero J, C or Q
factor, proving the first H identity even when individual paths cancel.
No commutation of branch representatives is used.

All products are disjoint serial graph copies, with connectors in factor
order; sums have fresh outer endpoints and disjoint branches. In a DAG,
leaving a designated exit internally cannot give another route to its
external connector, since that would require returning to the exit.
There is likewise no return from a later factor or another branch.
This verifies the path-sum identities for nonextremal or coincident factor
endpoints, parallel edges, no-path factors and empty products. For k=0,
there is one indicator 1, Q=0 and C witnesses a_alpha·1+1·a_alpha=0;
the displayed equations still hold. For n'=0 the branch relation is a
scalar equality and each J is a distinct-endpoint zero graph. For n=0
both cases apply. Repeated or complementary operands and an original
empty clause require no additional premise.

Independently recount the ledger with p=p(T), chosen once to dominate the
fixed-width compiler, complete single-branch data/time, indicator-pair
data/time, names and full dictionary. Its exponent is fixed by circuit
width 16, and k<=T lets the same p cover all indicator cases. Branches
cost Mp and the separately retained Q templates cost M^2p. A call to L035
has full input O(p), hence full output O(p^4) by its proved bound. For
each extension the M first summands and 2M^2 correction summands copy a
constant number of factors each, costing O(Mp+M^2p^4), including unit
connectors. All O(T) extensions therefore cost O(TM^2p^4). The O(T)
original/constant/signed/value roots cost O(TMp); each signed interpolant
is copied in full. Retained branches/templates, source associations,
zero-graph endpoints and even separately repeated dictionaries fit these
charges. There is no recursive gluing call or sharing discount.

Thus the pre-renumbering record/label payload is O(TM^2p^4). Its total
exponent in T,M,p is seven. Renumbering and restoring every original name
cost at most O(T+log(M+2)+log(p+2)) per record, bounded by O(Q). The extra
O(T^3) dictionary is smaller. Since T,M,p<=Q, the full output is at most
KQ^8, exactly the advertised threshold. In particular a logarithmic
identifier cost is not silently dropped at exponent eight. L035 has one
fixed polynomial bit-time exponent a, so all its calls cost
O(TM^2p^a). Assignment enumeration, the Mp compilation bound, M^2p
indicator-pair bound, record copying, parsing and renumbering all have
fixed polynomial costs in Q. A single fixed b>=8 can dominate them;
neither a nor b depends on k or the branch orders.

Finally, every written H edge is affine in the independent x,t. Every
accepting path in its finite DAG uses at most its total edge count, so
every resulting word before substitution has at most that degree.
Cancellation cannot increase it. Taking the maximum of these actual
edge counts and 1 proves the stated h<=KQ^8; it does not rely on a sharp
semantic degree surviving recombination. The original abstract value DAG
still has O(T) nodes, with internal graph vertices excluded. All of L037's
supplied-data hypotheses, including full aggregate E, exact roots and both
formal identities, now apply. M<=T+2 gives the claimed polynomial in T.
The separate audit finds no substantive defect or required theorem/bound
repair. It verifies this restricted local input, without a stronger
theorem, implementation, certified originality or main-problem result.

## Mathlib

Full matching coverage for this deletion promise, conditioned all-root
construction, ordered correction (6), and full-bit bound: **not checked**.
No absence claim is made. The precise supporting primary citations and
their roles are given above; the missing full-statement match is recorded
in the reused assessment. The new specialization is the explicit proof
above, not a claim that Boolean conditioning alone provides H witnesses.
