# L073 — Affine-ABP data after logarithmic internal extension deletion

## Hypotheses

Use L037's original width-at-most-three CNF F, supplied valid signed-AND ER
refutation π, full binary length T=2+|F|+|π|, and unchanged ordered original
axiom list A(x). Work over the free associative F₂ algebra, with original
variables x and independent placeholders for A. Retain every original name,
signed operand, unused extension and root association. Nonextension proof
variables absent from F have value zero. There are n≤T original variables.

Let G be L071's full signed Boolean value DAG: shared original inputs,
constants, positive extension AND vertices and required NOT vertices,
including unused roots. Treewidth refers to its underlying simple
undirected graph; operand occurrences are retained separately. Supply a
named set D of k positive extension AND vertices such that

    k≤floor(log₂(T+2)),             tw(G−D)≤2.

Original-input and NOT vertices are not deleted. No common order between
different conditioned compilations or restricted ER refutation is supplied.

## Conclusion

There is a deterministic polynomial-bit-time construction of complete L037
data for this unchanged F, π and A, with S=O(T), faithful x-only affine-ABP
representatives, exact original/constant roots and exact signed complements.
For every actual extension definition i with signed operands a,b it supplies
an explicit affine ABP H_i using only original Boolean and commutator
placeholders, satisfying the formal identities

    H_i(x,0)=0,             H_i(x,A)=r_i+r_a r_b.             (1)

One fixed polynomial bounds aggregate encoding and construction time in
T and M=2^k, independently of k and extension depth. More explicitly there
is a fixed p(T)=C(T+2)^c and constants K,b, with b≥6, such that, putting
Q=2+T+M+p(T), the full output length is at most KQ⁶ and bit time at most
KQ^b. Valid pre-substitution degree parameters are

    d=max(1,(2k+1)n),
    h=max(1,max_i |edges(H_i)|)≤KQ⁶.

All separate graph copies, identifiers, root associations and original
axiom dictionaries are included. Thus M≤T+2 gives polynomial bounds in T,
and the existing conditional L037 assembly supplies a polynomial-full-bit
original-axiom affine-ABP certificate on this restricted class.

This is an informal sufficiency result. The separate step-282 critical
audit below found no substantive defect within the stated hypotheses;
it changes neither the theorem nor its bounds and verifies no implementation.
Its POTENTIALLY_NEW classification under the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-internal-extension-deletion-data.md` means only
that the checked sources did not supply the full matching theorem; it does
not certify originality. Arbitrary ER representation, formula-only bounds,
W/V/U and unrestricted SAT decision or separation remain unresolved. This
is not a main-problem candidate.

## Proof

**Imported inputs and scope of the specialization.** Reuse L071's all-root
compiler and explicit affine graphs realizing L026's value and local
relation recurrences. The primary compilation input is Amarilli–Bourhis–
Senellart, *Tractable Lineages on Treelike Instances: Limits and Extensions*,
arXiv:1604.02761v1, Definition 6.4/Lemma 6.6, pp.15–16 and Appendix A,
pp.28–29 ([inspected long version](https://pierre.senellart.com/publications/amarilli2016tractable_long.pdf)).
The supporting order bound is Jha–Suciu, *On the Tractability of Query
Compilation and Bounded Treewidth*, ICDT 2012, Corollary 2.14 and section 4,
PDF pp.6–7,9 ([author PDF](https://homes.cs.washington.edu/~suciu/file38_paper.pdf)).
Same-order completion uses de Colnet–Ordyniak–Szeider, *OBDDs, SDDs, and
circuits of bounded width: Completeness matters*, AI 351 (2026), 104458,
Proposition 2, pp.3–4 ([published PDF](https://eprints.whiterose.ac.uk/id/eprint/234745/9/1-s2.0-S0004370225001778-main.pdf)).
Only fixed-width polynomial compilation is used; the width is never k+2.

Separate affine graphs are summed and multiplied by disjoint parallel and
serial composition, as in Raz–Shpilka, *Deterministic Polynomial Identity
Testing in Non Commutative Models*, author manuscript, Lemma 2 Step 1, p.5
([PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)).
For arbitrary explicit x-only graphs use the audited local L035 commutator
witness C(f,g) and L036 Booleanity witness B(f):

    C(f,g)(0)=B(f)(0)=0,
    C(f,g)(A)=fg+gf,          B(f)(A)=f²+f.                 (2)

These have polynomial full-bit bounds in their graph inputs. The
formula-input comparison is Li–Tzameret–Wang, *Characterizing Propositional
Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, Lemma 3.7, p.18
([PDF](https://arxiv.org/pdf/1412.8746v4)); it is not promoted to an arbitrary
graph-input theorem. The prior assessment covers these inputs. The new
work is compatible internal branching, a formal comparison of two local
data collections and the guarded reconstruction. None of the cited Boolean
compilation theorems alone supplies these original-axiom identities.

**Full branches and small prefix tests.** Order D as d₁,...,d_k in an
original topological gate order. For α∈{0,1}^k form C_α by removing the
vertices D and their incident wires, replacing each outgoing operand
occurrence of d_j by its own fresh constant leaf α_j. Keep all remaining
vertices, including NOT vertices, and all operand positions. Give each
deleted positive root an isolated constant with value α_j. A constant
root is never identified with its outgoing replacement leaves.

Each added nonisolated leaf has just one neighbor, so the two-vertex bag
containing that leaf and its neighbor attaches to a bag of G−D without
increasing width above two. Isolated roots use singleton bags. There are
O(T) occurrences, vertices and edges. L071's explicit degree-two
elimination/decomposition procedure and its width-at-most-16 all-root
selector construction apply. Original inputs with no remaining use may
be retained as isolated roots. Compile all values within this one branch
in a common order on the original x, removing selectors before arithmetic
compilation. Different branches may have different orders.

Write f_(v,α) for the resulting x-only representative of a positive
nondeleted extension. Originals/constants are exact; deleted positive
roots have f_(d_j,α)=α_j; every sign is exactly 1 plus its unsigned root.
The constant leaves and their root associations have these same scalar
values. For every nondeleted positive extension i, L026 and L071 supply
J_(i,α) with

    J_(i,α)(0)=0,
    J_(i,α)(A)=f_(i,α)+f_(a,α) f_(b,α).                   (3)

The construction uses only the circuit/diagram part of L071, as justified
in L072: the suffix recurrences need the branch's correct Boolean AND
relations and common-order diagrams, not an ER derivation. Map Boolean
and commutator positions into the unchanged A. All f degrees are at most
n; each branch's total graph encoding and construction time have one fixed
polynomial bound in T. No (3) is claimed for a deleted definition.

For j and a prefix γ∈{0,1}^{j−1}, take the ancestor subcircuit of the two
signed operands of d_j. Retain the gates needed for both operand values,
stopping at earlier deleted vertices and treating them as fixed constants
γ. No d_l with l≥j can be an ancestor, by topological ordering. Equivalently
take the ancestor graph before deletion, remove its earlier D vertices,
and replace each remaining outgoing occurrence by its own constant leaf;
discard ancestors whose outputs are no longer needed if desired. The
retained nondeleted graph is a subgraph of G−D. Retaining extra unused
original inputs as isolated vertices is harmless. The same leaf-bag proof
gives width at most two and O(T) encoding.

Compile this prefix ancestor circuit by the same L071/L026 interface. Let
u_a,u_b be the exact signed operand representatives it supplies, and set

    q_(j,γ)=u_a u_b.                                      (4)

Use a disjoint serial graph, not a circuit-valued edge. Each q has degree
at most 2n and polynomial full encoding in T. It computes the value of
d_j with earlier cut values γ, on every original Boolean assignment. Keep
its complete prefix collection of local relations for later comparison.
There are at most M−1 such tests and M full branches; no recursive
substitution of tests into tests occurs.

**Formal comparison on a common ancestor circuit.** We require more than
Boolean agreement between (4) and its full-branch operands. Here is an
explicit comparison using only already constructed local data. Consider
two collections u_v,v_v for the same acyclic AND circuit, with identical
exact original and constant inputs, identical fixed values at cut roots,
exact signs, and local witnesses J^u_i,J^v_i for every remaining AND. Their
polynomials and compilation orders need not agree. Put Δ_v=u_v+v_v.
Original/constant/cut roots have Δ=0; signed nodes have the same Δ as
their underlying unsigned roots.

Define witness outputs D_v with D_v(0)=0 and D_v(A)=Δ_v. The zero input
outputs start the induction. For an AND i with operands a,b set

    Z_i=J^u_i+J^v_i+C(v_a,u_b+v_b),
    D_i=Z_i+D_a u_b+D_b v_a.                              (5)

All C inputs are explicit x-only graphs. After A substitution, (5) is

    u_i+v_i+u_a u_b+v_a v_b
      +v_a(u_b+v_b)+(u_b+v_b)v_a
      +(u_a+v_a)u_b+(u_b+v_b)v_a
      =u_i+v_i.

The cancellation is literal, in the displayed order. Every summand in
(5) vanishes at zero substitution. Exact signed wrappers make the same
recurrence valid for signed or repeated operands, with sign aliases for
D. Constants and zero local defects present no exception.

Realize (5) without recursively copying D. Use one node η_i for each
unsigned circuit gate and one common source σ. A disjoint copy of Z_i
goes from σ to η_i. From η_a to η_i attach a fresh u_b graph, and from
η_b to η_i attach a fresh v_a graph, using sign aliases for η and retaining
parallel edges for repeated operands. Input η nodes have no source block,
so their source path-sums are zero. Each gadget has private internal
vertices and unit connectors. Gate order is strict along these transitions,
and each local block is acyclic. The σ-to-η_i path-sum is precisely (5).
Writing a separate copy with sink η_i for each requested output costs
only another O(T) factor. Paths that leave a designated internal exit
cannot return to it in an acyclic graph, so arbitrary factor endpoints
do not introduce extra accepting paths. The entire comparison has a fixed
polynomial encoding/time bound in the two supplied collections, with no
dependence on the number of circuit ancestry paths.

Apply this comparison to the prefix ancestor collection for (j,γ) and
the full-branch collection for every α extending γ, restricted to the
same ancestor circuit. Their fixed earlier cut values agree. Every
nondeleted ancestor's J is available in both collections, and every
signed or constant operand is retained. Thus the hypotheses of (5) hold
without a common variable order. Take u as the prefix collection and v
as the branch collection, and form

    K_(j,α)=D_a u_b+f_(a,α) D_b.

It satisfies

    K_(j,α)(0)=0,
    K_(j,α)(A)=q_(j,α_<j)+f_(a,α)f_(b,α).                 (6)

Indeed its substituted value is
(u_a+f_a)u_b+f_a(u_b+f_b)=u_a u_b+f_a f_b.
Every comparison uses two collections of polynomial size in T. There are
at most kM comparisons; they are independent, rather than stages of a
recursively growing comparison. This is the essential control on copying.

**Adaptive path weights and exact roots.** For a full branch α put

    l_(j,α)=1+α_j+q_(j,α_<j),
    e_α=l_(1,α) l_(2,α) ... l_(k,α),                     (7)

in this order, with empty product 1. Each weight is a disjoint product of
at most k small x-only graphs. Two siblings at a fixed prefix have factors
1+q and q, whose sum is formally 1. Backward induction on the finite
binary decision tree therefore gives the free-ring identity

    sum_α e_α=1.                                         (8)

More explicitly, the sum of suffix products below a leaf is 1, and below
a node is (1+q)·1+q·1=1 after the two child suffix sums are substituted.
No factor reordering or Boolean quotient is used in this induction.

For each positive extension write

    r_v=sum_α e_α f_(v,α),                                (9)

with separate product and sum graphs. Write originals/constants exactly,
and signs as the exact wrapper 1+r_v. These roots equal their interpolants
formally: originals and constants are the same in every branch, so (8)
factors on their left; signed interpolation is
sum e_α(1+f_(v,α))=1+r_v. This also treats signs of deleted roots. Unlike
the independent-input case, no identity sum α_j e_α=x_j is asserted for
an internal gate: its actual representative is (9).

On any original Boolean assignment, each q test is a bit and exactly one
path of (7) has value 1. Inductively its first j−1 choices are the actual
values of d₁,...,d_(j−1), so the prefix ancestor circuit computes the true
next gate value at stage j. That next choice is therefore also correct.
The selected full branch agrees with the original value circuit at every
deleted gate and hence at every remaining vertex by topological evaluation.
Thus every r_v is faithful on all original assignments, irrespective of F.
Its degree is at most 2nk+n; exact roots and signs give the stated d.

**Explicit weight-product corrections.** Construct Q_(α,β) with

    Q_(α,β)(0)=0,
    Q_(α,β)(A)=e_α e_β+δ_(α,β)e_α.                       (10)

For α=β use B(e_α) from (2). For α≠β let j be their first disagreement.
The preceding factors coincide as formal polynomials, since their entire
prefixes coincide. Write

    e_α=P l R,          e_β=P m S,

where l,m are the complementary factors 1+q,q for the same test
q=q_(j,α_<j). The suffixes R,S may differ arbitrarily. In either order
lm=q²+q formally. Set

    Q_(α,β)=P l C(RP,m) S + P B(q) R P S.                 (11)

After substitution its value is
P l(RP m+m RP)S+P(q²+q)RP S=P l RP m S=e_αe_β.
The two terms containing P l m RP S cancel literally. At zero substitution
both displayed summands vanish by (2). All C and B inputs are x-only
products of at most O(k) small prefix-test factors. Empty P,R,S are 1;
no formal independence of the internal tests is assumed. In particular
(10) is a witnessed free-ring correction, not a claim that the weights
are formally orthogonal without correction.

**Guarding every deleted definition.** For i=d_j and α, use q as in (6),
write e_α=P l R with l=1+α_j+q, and put t=α_j+q. Here t is an x-only
polynomial, not an axiom placeholder. Since lt=q²+q, the witness

    U_(j,α)=P B(q) R+P l C(R,t)

has value P l t R+P l(Rt+tR)=P l R t=e_α(α_j+q) after
substitution, and value zero at zero substitution. Define

    I_(i,α)=U_(j,α)+e_α K_(j,α)          if i=d_j,
    I_(i,α)=e_α J_(i,α)                  if i∉D.

Using (3) or (6), respectively, gives in all cases

    I_(i,α)(0)=0,
    I_(i,α)(A)=e_α(f_(i,α)+f_(a,α)f_(b,α)).              (12)

For a deleted root f_(i,α)=α_j, so the two q terms cancel. This is where
its retained defining equation is restored; no free extension axiom is
introduced. There is no claim of a small unguarded witness for the false
equation α_j=f_(a,α)f_(b,α) on an incompatible branch.

**Flat recombination.** Use L072's ordered recombination with the weighted
local witnesses (12). For a fixed i abbreviate a_α=f_(a,α), b_β=f_(b,β),
and set C_(α,β)=C(a_α,e_β). Define the single explicit affine graph

    H_i=sum_α I_(i,α)
       +sum_(α,β) [ e_α C_(α,β) b_β
                    +Q_(α,β) a_α b_β ].                 (13)

All products and sums use independent factor occurrences in the indicated
order. Every term contains a zero-at-zero witness, so H_i(0)=0. Substituting
(2) and (10) into the double sum gives

    sum_(α,β) [e_α a_α e_β b_β
       +e_α e_β a_α b_β+e_α e_β a_α b_β
       +δ_(α,β)e_α a_α b_β]
       =r_a r_b+sum_α e_α a_α b_α.

The first equality to r_a r_b uses the exact interpolation identities for
every signed operand, original and constant. By (12) the other part of
(13) has value r_i+sum_α e_α a_α b_α. Cancellation proves (1) formally.
All original clauses and the original refutation are unchanged. Only
Boolean and commutator positions of A occur in any local witness.

**One aggregate ledger.** First choose a fixed p₀(T)=C₀(T+2)^c₀ bounding
the complete data, names, dictionary and bit time for any one full branch
or prefix ancestor compilation, and the two-operand q product. Such a
fixed polynomial exists by L071's fixed-width compiler and recurrences.
Each comparison (5) uses O(T) calls of L035 on inputs of length O(p₀),
O(T) independent multiplier graphs and O(T) separate output copies if all
are retained. The L035 output bound O(E⁴), polynomial bit time and graph
framing make its entire encoding/time bounded by another fixed polynomial
in T. The K outputs in (6) have that same type of bound. There is no call
of L035 on a D or other witness, and no nested comparison of comparisons.

Each P,l,R,S,e and RP in (7), (11) and (12) contains at most O(k) factors
of size O(p₀), and k≤T. Their full independent graph encodings, including
new references, are bounded by a fixed polynomial in T. L035 and L036
on these x-only inputs have fixed polynomial output/time bounds; L036's
O(E⁶) bound is sufficient for B(e). Products with K in (12) are disjoint
serial composition, not substitution at its edges. Consequently choose
one larger fixed p(T)=C(T+2)^c, at least (T+2)^4, covering the full size
and construction time of each of the following complete objects: one
branch or prefix compilation, one comparison and K, any path factor or
weight, one Q, one I, and one correction summand in (13). Include a full
copy of A and its dictionary in each allowance. This choice is legitimate
because the construction just described has a fixed number of nested
polynomial operations, independent of k; the only k-length operation is
concatenating at most T independently bounded graphs.

There are M branches, M−1 prefix tests, at most kM comparisons, M² weight
corrections, O(TM) local I graphs, and O(TM²) correction occurrences in
the final H graphs. The representatives and their separately copied signs
cost O(TMp). Keeping all auxiliary graphs as well costs at most O(TM²p),
since k≤T and M≥1. No sharing between exported roots is credited.
Before final global renumbering the records and existing labels therefore
have total length O(TM²p). Names, root associations and full dictionaries
are already included. Allowing a further factor
O(T+log(M+2)+log(p+2)) for every reference and name occurrence gives a
bound KQ⁵, hence the stated slack bound KQ⁶. All original names have at
most T bits, and dense graph identifiers need O(log(Q+2)) bits after
renumbering. Extra copies retained in the comparison are already in p.

Enumerating branches and prefixes, constructing these independent local
objects, writing all occurrences and renumbering are bounded by one fixed
polynomial KQ^b in bit time. A larger fixed b≥6 covers even naive polynomial
string operations; it does not depend on k or the extension depth. No
step enumerates the paths of an ABP or unfolds circuit ancestry.

Every final edge label is affine in x and the original placeholders.
An acyclic accepting path uses at most the graph's total number of edges,
so this number bounds its full formal degree before substitution, giving
the asserted h. This bound also pays syntactic degree without relying on
cancellation. All value roots satisfy the separately proved d bound.
The abstract S-node value DAG remains the original O(T) gate/sign DAG;
private arithmetic vertices are not additional extension definitions.

For k=0 there is one weight 1, no deleted definition, and the construction
reduces to the branch data and the same valid recombination (zero correction
polynomials are allowed). If n=0 one can instead directly evaluate the
entire original acyclic value circuit as scalars, write exact constants
and signs, and use zero H graphs; all bounds hold with d=h=1. Empty clauses,
unused roots, repeated or complementary operands, disconnected graphs,
zero factors, parallel edges and empty products require no additional
assumption. Fresh outer endpoints and private composition blocks implement
all zero/constant cases without spurious accepting paths.

All L037 data hypotheses are now supplied for the unchanged proof, so its
conditional assembly gives the claimed certificate. Attempts 019–021
remain valid: no unrestricted OBDD premise, same-output degree-only
conversion or prescribed pair-table conversion is used. The structural
promise is explicit and the witnesses are alternatives. Neither small
internal deletion sets for arbitrary ER proofs nor any formula-length or
unrestricted SAT consequence is established. No implementation or separate
critical audit is asserted by the original construction step. The separate
audit follows.

**Separate critical audit, 2026-10-17 (step 282).** This reviews exactly
the existing statement under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-17-internal-extension-deletion-critical-audit.md`.
It reuses the inspected primary compilation/completion/composition inputs
above and the audited L026/L035/L036/L037/L071/L072 interfaces. The task is
to validate this restricted input to L037; arbitrary ER representation and
unrestricted SAT decision/separation remain independent gaps. The tests
are the common ancestor interface, both formal identities, and a fixed
polynomial in T and M=2^k, with no uncharged recursive copying.

First check which circuit each collection describes. In a full branch,
every edge whose tail was a deleted gate and whose head remains is replaced
by its own constant leaf; edges into deleted gates disappear. A repeated
operand still has two occurrence leaves, even if its underlying adjacency
was single. Each new leaf has one neighbor and attaches by a two-vertex
bag. Deleted-root association constants remain separate isolated vertices.
NOT vertices remain and receive their actual input leaf. Thus all retained
edges belong to G−D, all new nonisolated edges are leaf edges, and width
at most two is preserved. O(T) counts occurrences as well as roots. The
fixed-width selector construction of L071 therefore applies, including
unused vertices and disconnected original inputs. Only its circuit part
is used, not a purported valid refutation after deleting definitions.

For the prefix of d_j, start with the cones of its two signed operands
and stop at the first earlier deleted gates encountered on each backwards
path. Topological order excludes d_j and every later deleted gate from
these cones. On cutting the earlier deleted vertices, the remaining graph
is a subgraph of G−D with the same leaf additions. One may keep all n
originals as isolated vertices when absent from the cones; this keeps the
alphabet and complete original dictionary literally identical. Exact
constant representatives and sign wrappers handle absent proof variables.

For alpha extending the prefix, identify every retained unsigned ancestor
with the same original gate in the full branch. Identify each cut operand
occurrence with its own constant input in the ancestor circuit, of value
alpha_l=gamma_l. When a target operand itself is a cut gate, use its scalar
root directly. Different occurrence leaves need not be the same vertex:
their supplied representatives are the identical scalar in both data
collections. Each retained AND has exactly the original ordered signed
operands, interpreted with these cut constants. The prefix J and the
full-branch J for that gate satisfy (3) on this same circuit. The latter
may involve variables outside the ancestor cone formally; (5) does not
require support equality or common compilation order. It requires only
the exact base roots, signs and local identities, all of which hold.
Completion and L026's increasing-multilinear identification are used
within each compilation separately, never across their two orders.

For (5), the substituted value of Z_i is

    u_i+v_i+u_a u_b+v_a v_b+v_a Delta_b+Delta_b v_a.

Adding Delta_a u_b+Delta_b v_a cancels the two copies of Delta_b v_a.
Expanding the two remaining Deltas cancels u_a u_b and v_a v_b and
leaves two identical copies of v_a u_b, which cancel as well. The result
is u_i+v_i, with no commutation. At zero placeholders both local J's and
C vanish, as do the earlier D's. Signed operands have Delta equal to
their unsigned Delta, since the two scalar 1's cancel. This also verifies
repeated operands, including opposite signs, without identifying their
two multiplier occurrences.

In the comparison graph, a source-to-eta_i path either enters its private
Z_i block or reaches an earlier eta_a or eta_b and then follows the
corresponding multiplier to eta_i. This last-step partition yields
exactly Z_i+D_a u_b+D_b v_a. Source blocks have no edges back to sigma;
transitions between eta vertices strictly increase the original gate
order. Private blocks have no other external entrances/exits. Thus a
cycle would either lie within an acyclic block or induce a cycle in the
gate order, both impossible. A designated factor exit with outgoing
internal edges is safe: a path taking such an edge cannot return to that
exit, and no other internal vertex connects externally. Coincident factor
endpoints give exactly their empty path. Fresh unit connectors avoid
identifying these endpoints with eta vertices. Base eta nodes have no
incoming source block or predecessor transitions, so their path sums are
zero. Keeping outgoing transitions at the designated output eta_i adds
no accepting return path. All separately requested D outputs can therefore
be copied from this one finite graph, with an O(T) output-copy factor.

In (6), K is a disjoint sum of two products of already completed D graphs,
not a new recursive rule with two-sided multiplication. Substitution gives
Delta_a u_b+f_a Delta_b=u_a u_b+f_a f_b by literal cancellation of
f_a u_b. Both terms vanish at zero placeholders. Each comparison is made
anew from a prefix compilation and a full-branch compilation; no earlier
comparison or K is an input to a later comparison. In particular L035
in (5) receives v_a and u_b+v_b, both explicit x-only graphs.

For (8), at any decision-tree node let the two sums of all descendant
suffix products be S_0 and S_1. Induction from leaves gives S_0=S_1=1,
even though the two descendant tests differ. Its suffix sum is therefore
(1+q)S_0+qS_1=1. This proves the ordered free-ring partition, without
assuming that the tests are independent or moving a factor through a
prefix. On a Boolean assignment each test is a scalar bit and selects
one child. Induction over the topologically ordered deleted gates then
shows that the selected prefix gives their true values. The full selected
branch computes every remaining gate correctly. This establishes fidelity
on all original assignments, including those not satisfying F. Formal
interpolation of an original x is (sum e_alpha)x=x, and that of a sign
is sum e_alpha+sum e_alpha f=1+r. No x is moved past a weight.

Audit the off-diagonal weight correction at the first disagreement.
There the two earlier prefixes are literally the same factor list P,
and the split factors l,m are complementary polynomials in the same q.
After substitution the first summand of (11) expands to

    P l R P m S + P l m R P S.

The second becomes P(q^2+q)R P S=P l m R P S, in that same order.
Their sum is e_alpha e_beta. Empty P, R or S is the scalar 1, so the
calculation covers first/last disagreements. The diagonal L036 call has
value e_alpha^2+e_alpha as required. Its inputs, and the inputs RP,m and
q of the off-diagonal calls, are x-only disjoint products of tests; they
are not recursively constructed corrections or placeholder-bearing data.

For the deleted-definition guard, l=1+alpha_j+q and t=alpha_j+q have
lt=q^2+q in either bit case. The two U terms substitute to

    P l t R + P l R t + P l t R = P l R t.

Thus U gives e_alpha(alpha_j+q). Adding e_alpha K cancels the two
e_alpha q terms and gives e_alpha(alpha_j+f_a f_b), exactly (12).
For an undeleted gate the same identity follows directly from (3).
All displayed U, K, J and I terms vanish formally at zero placeholders.
Incompatible branches never require a witness for their false unguarded
definition. Only original Boolean and commutator placeholders are used.

Finally the two correction terms of (13), after substitution, contain
the identical middle word e_alpha e_beta a_alpha b_beta twice. Their
uncancelled sum over ordered pairs is r_a r_b plus the diagonal sum
sum_alpha e_alpha a_alpha b_alpha. By (12), the local I sum is r_i
plus that identical diagonal sum. This proves H_i(A)=r_i+r_a r_b.
Every summand of H_i has a witness factor zero at zero placeholders,
proving H_i(0)=0 independently of pathwise cancellation. This applies to
every actual signed/original/constant operand by the formal interpolation
checks above; Boolean agreement is not substituted for a free identity.

Independently check the order of polynomial bounds. A fixed p_0 covers
one complete full-branch or prefix compilation and its time, including
the O(T) roots and the original dictionary. Fixed circuit width 16 fixes
its exponent. Each comparison uses O(T) L035 calls on O(p_0)-length
inputs, O(T) multiplier occurrences, and at most O(T) separately exported
copies. L035 costs O(p_0^4) output bits and a fixed polynomial time per
call. Thus one comparison and K have a fixed polynomial bound in T.
This operation is performed independently at most kM times.

Every weight, prefix/suffix factor and RP has O(k) test occurrences, not
a number of occurrences exponential in prefix depth. As k<=T, their
full encodings and construction time have a fixed polynomial bound in T.
The calls of L035 and L036 on these graphs then have fixed polynomial
bounds as well; L036's O(E^6) allowance includes its internal L035 work.
No Q, I or D feeds back as an x-only correction input. Multiplying K by
e_alpha, and placing Q in a final summand, only copies/concatenates the
already bounded graphs. Hence a single larger fixed p(T) can cover every
complete local object and every summand of (13), with its dictionary,
source associations and time. There is no iteration of a size-polynomial
k times; the polynomial-composition depth is fixed.

The counts are M full branches, M−1 prefix compilations, at most kM
comparisons, M^2 separate Q graphs, O(TM) I graphs, O(TM^2) final correction
occurrences, and O(T) separately exported value/sign roots each using
O(M) branch products. These counts include templates retained in addition
to their uses. They give O(TM^2 p) total pre-renumbering records and label
payload, without sharing between outputs. A further name/reference factor
O(T+log(M+2)+log(p+2)) is O(Q), for Q=2+T+M+p. Since TM^2p<=Q^4, total
full bits are O(Q^5), below the stated KQ^6 after adjusting an absolute
constant. Dense graph identifiers have O(log Q) bits even though the
graph count is polynomial in Q. Separate original dictionary copies were
already charged to p; none is an external free input. Enumeration, all
local algorithms, copying and renumbering have one fixed polynomial bit
time KQ^b. Neither exponent depends on k, ancestry depth or branch order.

For degree, each test has degree at most 2n, each weight at most 2kn,
and each branch representative at most n; sums and exact signs do not
increase their maximum. Thus d=max(1,(2k+1)n) holds. Every final H is
an explicit affine-edge DAG, so its total edge count bounds every
pre-substitution accepting-word degree, even for cancelled paths. This
proves h<=KQ^6. The abstract gate/sign DAG remains the original O(T)
structure, independently of private graph vertices. When k=0 the only
weight is 1, no comparison or deleted guard is needed, and all equations
remain valid (correction graphs may compute zero). When n=0, direct
scalar evaluation gives exact roots and zero H, with d=h=1. Empty clauses,
unused gates, parallel edges, zero polynomials and arbitrary endpoints
create no extra input promise.

The two formal identities, all-assignment fidelity and the aggregate
fixed polynomial therefore pass this separate informal audit. All L037
receiving data are supplied on precisely the stated structural class;
M<=T+2 makes their bounds polynomial in T. No substantive defect or
theorem/bound repair was found. This is verification of an existing local
input, not a new theorem, certified originality, implementation, general
ER-data existence or a solution to P versus NP. Attempts 019–021 retain
their original scope. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching theorem, adaptive compatibility witnesses, comparison graph
and aggregate binary ledger: **not checked**, not claimed absent. Supporting
primary compilation, completion and graph-composition citations are given
above; none is claimed to contain the complete formal-data conclusion.
The L035/L036 graph corrections and L026/L071 compiler interface are reused
with their stated hypotheses. The comparison and ordered identities are
written out because they are the uncovered specialization being tested,
not a reproof of an already imported full theorem.
