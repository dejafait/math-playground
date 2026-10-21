# L093 — Opposite-order OBDD product witnesses

## Hypotheses

Use L087's explicit dense deterministic OBDD inputs D,E, each of
nonterminal width at most three, on the same complete named alphabet
of q≥2 original variables. Their supplied variable orders are exactly
opposite. Write D's order as z₁,…,z_q and E's as z_q,…,z₁; this is a
positional notation, not a change to the original names or dictionaries.
Redundant tests, duplicate successors, unreachable states and all
scalar terminal records are retained. Let f,g be their exact ordered
free-F₂ representatives, with edge labels 1+z for bit 0 and z for bit 1,
and terminal values in F₂. Assume fg(a)=0 on every Boolean assignment.

Retain L087's complete original Boolean/commutator list B and independent
placeholders σ,τ, indexed by the original listed alphabet, and its
pre-witness M: 2 plus the full bit length of both diagrams, both orders,
names, B, placeholders and framing. M includes neither the sought
witness nor its degree. A pair placeholder is looked up by the two
original names, independently of their positions in either order.
Only explicitly written acyclic graphs with affine edge labels are
admitted. The Boolean-zero hypothesis is a promise.

## Conclusion

There is a deterministic construction of an explicit affine-F₂ ABP H,
using only the original variables and B's placeholders, such that

    H(z,0)=0,                    H(z,B)=fg

as identities in the free associative algebra. For constants K
depending only on the fixed explicit encoding, its complete output
length is at most K(M+2)⁵, and deterministic bit time is at most
K(M+2)¹⁶. Every accepting path has at most 2q−1 nonconstant edge
factors before substitution, including paths whose contributions
cancel or have a zero factor. Every accepting path contains exactly
one placeholder edge. No promise test, path expansion or identity-test
oracle is part of the construction.

This is a restricted supplier for L087's witness interface, not its
arbitrary-order premise W₂. It supplies no general ER data, formula-only
bound or SAT decision/separation. The separate all-size critical audit
on 2026-10-20 (step 363), recorded below, finds no substantive defect.
This remains an informal result; no implementation or certified
originality is claimed.

## Proof

**Coverage and source use.** The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-20-opposite-order-obdd-product-witness.md`.
Reuse L035's audited original-only marked-edge commutator construction,
L085's audited weighted paired recurrence and first-exit graph component,
and L026's ordered-multilinear injectivity. Only the indicated component
of L085 is used: no ER proof, extension fidelity or whole ER-data theorem
is assumed for these two graphs. Its graph and algebraic hypotheses
are checked below.

The inspected primary supporting inputs are Li–Tzameret–Wang,
[*Characterizing Propositional Proofs as Non-Commutative Formulas*,
arXiv:1412.8746v4, Lemma 3.7, printed p.18](https://arxiv.org/pdf/1412.8746v4),
on formula commutator witnesses, and Raz–Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author manuscript, Definition 1 p.4 and Lemma 2 Step 1 p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
on ordered path semantics and disjoint serial/parallel graph composition.
Their formula bounds are not asserted for arbitrary graph inputs;
L035 supplies that local specialization. The present new obligation is
the reversal correction and its original-M reception. No primary
theorem asserting that full conclusion was found in the assessment.
The optional unread automata-reversal lead is unused. The following
identities justify the necessary specialization, not a reproof of PIT,
formula conversion or deterministic OBDD reordering.

**1. Exact reversed path polynomials.** Define rev on free words by
reversing the letter sequence, fix scalars, and extend F₂-linearly.
Concatenation directly gives rev(ab)=rev(b)rev(a); affine original-only
labels are fixed by rev. For each E state u let g_u be its original
suffix polynomial, including its terminal scalar, and put R_u=rev(g_u).
If e:u→v has label l_e then

    g_u=Σ_e l_e g_v,          R_u=Σ_e R_v l_e.               (1)

These are finite polynomial equalities, allowing cancellations and
parallel occurrences. At a terminal both polynomials equal its scalar.

Here is an explicit x-only graph for every R_u. Reverse every E edge
without changing its affine label. Add a new source r with an edge
labelled s_t to every original terminal t of value s_t. Use u as the
designated output and retain the entire reversed graph. A path from r
to u chooses t and then the reverse of precisely one original path
from u to t. Its scalar s_t is central, so its value is the reversal of
that original path's product times s_t. This bijection proves its
polynomial is R_u. Parallel edges, zero terminal edges and cancelling
paths remain distinct. The graph is acyclic: reversed edges decrease
the old level, and only r has the added outgoing connectors. Edges
leaving the designated output cannot return to it. Thus keeping all
other vertices/edges introduces no additional designated paths. This
construction includes unreachable states and terminal u, for which the
only designated path has the scalar label s_u.

For use specifically in L085, construct a layered graph V for R_root
in D's order. Give an old E vertex at level i its new level q+2−i.
Make a new level-1 root v*. For every original last-variable edge
e:a→t, add v*→a with label s_t l_e. Keep all reversed original edges
and all old vertices; the old terminals are now unreachable level-1
vertices. Give each old level-1 vertex, now at final level q+1, scalar
1 if it is E's root and scalar 0 otherwise. The other levels need no
scalar outputs. Every edge now goes one level forward with label
a+b z_k at level k. In particular s_t l_e is still affine, even when
s_t=0, and the first variable is z₁. A path from v* to a nonzero final
scalar chooses exactly the last original edge, then the remaining
original path backwards to E's root. This is the same path bijection
as above, with the first scalar connector absorbed into that edge.
Consequently V computes R_root formally, not just on Boolean points.
No determinism of V is claimed or needed. The construction adds only
a linear number of records and retains all original records.

**2. A commutator-only correction to reversal.** For each nonterminal
edge e:u→v of E, let C_e be the L035 witness with its first x-only
operand the one-edge graph l_e and its second operand the graph R_v
from part 1. Thus

    C_e(0)=0,       C_e(B)=l_e R_v+R_v l_e.                 (2)

L035 uses only commutators. Its pair-once placeholders are identified
with the corresponding τ in the unchanged B dictionary; no Boolean
or additional placeholder is required here. In particular neither a
recursive correction nor a placeholder-bearing graph is an operand.

Set J_t=0 at every scalar terminal, and define backwards

    J_u=Σ_(e:u→v) (l_e J_v+C_e).                            (3)

This formula specifies a graph recurrence, not an unfolded expression.
Make one recurrence vertex per E state, with the original l_e edge
from u to v, and one fresh sink Ω. Terminal recurrence vertices have
no exit to Ω. At u attach a disjoint complete copy of C_e for each
outgoing occurrence e, with unit entry/exit connectors, its exit going
only to Ω. Different local copies share neither vertices nor exits
except Ω; no local block returns to the recurrence region. Each path
to Ω first follows original edges, then exits once into a C_e. This
proves exactly (3), with no accepting empty path and no recursive
copying. The level increase in the recurrence region, internal
acyclicity and the one-way block connectors prove acyclicity globally.

Induction from scalar terminals gives J_u(0)=0. At substitution, using
(1)–(2) and the induction hypothesis, each edge summand is

    l_e(g_v+R_v)+(l_e R_v+R_v l_e)
       =l_e g_v+R_v l_e.

Summing gives J_u(B)=g_u+R_u. Terminals satisfy this because a scalar
plus its own reversal is zero in F₂. Hence for J=J_root,

    J(0)=0,                    J(B)=g+R_root.              (4)

This induction does not commute a witness past any factor and does
not discard semantic-zero suffixes. L035's marked-edge graph is used
even when R_v happens to be constant by cancellation. If v is an
actual terminal, it has only the scalar designated path and the
commutator graph has no accepting path; it may be represented by a
distinct-endpoint zero graph instead. Either convention has the same
bounds, without a semantic constant test.

**3. Reception by the existing common-order component.** Let U be D's
own layered weighted graph with its original labels and terminal
scalars, so U computes exactly f. Part 1 supplies V computing exactly
R_root. These are explicitly layered in the same order z₁,…,z_q;
each variable occurs at most once on a path, edges are a+b z_k,
terminals are scalars, and missing paths/parallel edges are allowed.
They therefore meet precisely the graph hypotheses used in L085's
weighted paired recurrence, irrespective of extension/ER hypotheses
irrelevant to that component.

For clarity, its actual output interface is as follows. For outgoing
edge pairs with l=a+bz_k, m=c+dz_k set

    h=ac+(ad+bc+bd)z_k.

The paired P graph has transition h and terminal scalar products.
The paired W graph has h transitions between pair states, with
terminal pair states nonaccepting, and the two first-exit blocks

    d l K(u′,k) G_(v′),       bd σ_(z_k) F_(u′) G_(v′).

Here F,G denote the original-only suffixes of U,V, and the L035
component K satisfies K(B)=F_(u′)z_k+z_k F_(u′), K(0)=0.
The placeholder σ_(z_k) is the original dictionary entry for z_k.
L085's equations (2)–(5) and its audited first-exit construction give

    W(0)=0,                   W(B)=f R_root+P.             (5)

Its algebraic check is local: lm=h+bd(z_k²+z_k) and
F m=m F+d K(B). Thus l F m G=h F G+bd(z_k²+z_k)F G+
d l K(B)G, with exactly the displayed factor order. This identifies
the imported component's two operands and axiom positions; no whole
L085 theorem or renewed derivation of its construction is required.
Every suffix passed to K remains original-only, including those with
zero polynomial and cancelling paths. The audit's path-free shortcut
is used only for scalar terminals.

The polynomial P is increasing multilinear in D's order and agrees
on Boolean assignments with the pointwise product of U and V, as
proved in L085. At a scalar assignment reversing a word preserves its
value; finite linear extension gives R_root(a)=g(a). Thus the Boolean-
zero promise implies P(a)=f(a)g(a)=0. L026's injectivity on this exact
increasing-multilinear subspace gives P=0 formally. Injectivity has
not been applied to g+R_root, fg, J or W.

Use disjoint serial/parallel graph copies to set

    H=W+f J.                                                   (6)

Equations (4)–(5) give H(0)=0 and
H(B)=f R_root+f(g+R_root)=fg. Both identities retain the original
free-ring f and g, in that order. The cancellation requires no factor
movement. If the Boolean-zero promise fails the same constructor
instead gives H(B)=fg+P; no correctness or promise test is concealed.

**4. Independent-copy and original-input ledger.** Let N be 2 plus
the aggregate number of vertices, edges and affine label entries in
U, V, E and the scalar-source reversed-E graph of part 1. Scalar
terminal absorption, the added root and the duplicated last-level
edge occurrences cost a linear number of records. Therefore
N≤cM, also q≤cM, for an encoding-dependent absolute c. Original
names, terminal records, unused states and zero edges are included.
All relevant edge labels have at most two entries. No witness size
has entered N or M.

One complete R_v graph costs O(N) records; it is copied afresh wherever
required. For C_e, L035's first operand has one edge and O(1) vertices.
Its marked choices number at most O(N), one for each edge of R_v;
each choice has O(N) records in its separately copied subpath graphs
and O(1) central label entries. Thus one C_e has O(N²) records,
including all dead copies. There are O(N) original e occurrences.
The whole J graph, with all independently written C_e, recurrence
vertices, connectors and sink, consequently has O(N³) records.
There is no product over the number of root-to-edge paths.

For W, use L085's component ledger directly at the present N. There
are at most O(N²) same-level state pairs and O(N²) outgoing edge-pair
occurrences in total. Each K block is a single-variable L035
specialization with O(N²) records; its other suffix factors cost
O(N). Independent local copies and connectors give O(N⁴) records
for W; its auxiliary P has O(N²). Scalar exits to turn suffixes into
ordinary designated-output graphs add O(N) per suffix, already paid.
The disjoint f J branch and parallel combination with W in (6) add
O(N³+N) records, not a copy for each W path. Retaining all auxiliary
graphs, all separately generated C_e and R_v, and P if desired does
not increase the O(N⁴) aggregate bound.

With dense graph identifiers the endpoint lengths are O(log(M+2)).
Each restored original name has at most M bits; every edge has a
bounded number of label entries. Charging O(M+log(M+2)) per record
therefore pays full labels, names, references, lengths, coefficients
and root/output framing. The unchanged B/placeholder/name package
has at most M bits. Even repeating that entire package with each
primitive graph copy costs O(N⁴ M), since there are no more copies
than records under the counts above. Hence full output and retained
intermediates fit K(M+2)⁵ bits. In particular the original B is never
replaced by axioms in a newly generated alphabet.

A deterministic constructor uses only topological checks, source
record scans, reversal/renumbering, pair and marked-edge enumeration,
F₂ scalar arithmetic and record copying. The preceding counts bound
all graph-generation loop iterations by O((M+2)⁴). Their source and
dictionary lookup data, counters and output buffers have length at
most L=K(M+2)⁵. Even allowing a full quadratic scan/copy of such
buffers per iteration gives O((M+2)⁴ L²), bounded by
K′(M+2)¹⁶ after including parsing, finite name comparisons and
framing. This deliberately loose bit-time bound does not enumerate
paths, assignments, monomials or candidate witnesses. The proof of
the promise-dependent equality P=0 is mathematical, not an algorithm
subroutine. Output existence and construction do not rely on PIT.

**5. Complete path-degree check.** If u in E has s remaining query
levels, a designated R_v path after one outgoing e has s−1 affine
variable-level factors, plus scalar connectors. In L035's C_e every
accepting path marks one variable-bearing edge of that R_v path and
the single l_e edge. The two marked labels are replaced by one
placeholder. The unmarked reversed path has at most s−2 nonconstant
factors, so C_e has pre-substitution path degree at most s−1.
Scalar marked edges produce no central placeholder. For s=1 there
is no variable-bearing R_v path, so C_e has no accepting path.
Keeping the entire reversed graph does not alter this count: an
accepting marked prefix/suffix combination is a genuine designated
R_v path, by L035's acyclic path factorization.

An accepting J path takes j original recurrence edges and then a
C_e at a state with q−j remaining levels. Its nonconstant-factor
count is at most j+(q−j−1)=q−1. This holds for all accepting paths,
including cancelling paths, not merely surviving monomials. Every
such path has exactly one placeholder edge. The W component's
audited bound is 2q−1: at s remaining levels each local exit block
has at most 2s−1 factors, and a recurrence prefix adds at most one
per preceding level. Its terminal pair region has no accepting path.
The f J branch adds at most q+(q−1)=2q−1. Constant connectors and
fresh source/sink edges add zero degree and no placeholders. The
parallel union thus has the stated path bound and exactly one
placeholder on every accepting path, even if the complete output
polynomial is zero by cancellation.

**Scope and continuation test.** This meets the approved threshold:
both formal identities, the exact original fg, unchanged B/M and one
fixed polynomial for all independent graphs and bit time. It uses
weighted reversal, not a promised small deterministic reordering.
L092's boundary-state enumeration is not used; full reversal need not
meet its logarithmic block cutoff. Attempt 030's common-order value
availability obstruction remains separate, and L087's constructed
arbitrary-order hard pairs have no proved reversal promise. No
NP=coNP conclusion is inferred. The separate audit below checks the
reversal source/terminal absorption, recurrence block semantics,
L085 reception, original-name mapping and complete ledger within
exactly these hypotheses.

**Separate critical audit, 2026-10-20 (step 363).** This audit uses the
unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-20-opposite-order-witness-critical-audit.md`.
It independently checks the existing construction, using L035's full
marked-edge proof and audit, L085's paired component and step-331
scalar-terminal qualification, L026's ordered injectivity and L087's
input convention. The primary component citations above are reused;
no full opposite-order theorem, automata reversal theorem, whole L085
ER theorem or additional source result is assumed. This is verification
of a local input, not a new theorem or originality claim.

For the reversal graph, fix a designated output u before counting
paths. Its incoming source edge r→t selects an original terminal,
including terminals with scalar zero. Every subsequent reversed edge
corresponds to exactly one original edge occurrence, in reverse order.
The old levels strictly decrease, so the path cannot pass u and later
return to it. Hence the path correspondence includes all and only
original u-to-terminal paths, even with parallel edges or dead vertices.
The new source is distinct from every old vertex. If u is terminal,
the sole possible designated path is its own scalar connector; no
nonempty reversed-original path can end at that terminal. Thus the
scalar, zero and arbitrary-output cases in (1) are covered without
deleting paths by their polynomial values.

In the normalized graph V, an original level-i edge becomes an edge
from new level q+1−i to new level q+2−i. Its original query is
z_(q+1−i), exactly the new level's query. An old terminal is at new
level 1, whereas the added root v* has edges only into new level 2.
Thus no old terminal can be reached from v*. Each new first edge is
indexed by a separate original last-edge occurrence and has label
s_t l_e, accounting for the absorbed source connector exactly once.
At the final level only the old E root has scalar 1; other old level-1
states have scalar 0. The remaining path therefore reverses precisely
an original root-to-terminal path when its final scalar is nonzero.
Additional paths to zero-valued final states contribute zero and still
have exactly q variable-level edges. This proves the formal output
identity while retaining zero edges and irrelevant states. L085's
component permits multiple initial-level vertices, missing paths,
parallel edges, affine weights and scalar terminals; it does not require
V to be deterministic or to have a width-three reversed root layer.

For C_e, instantiate L035's factor order with first operand the single
l_e edge. The first operand's marked prefix and suffix are empty, so
each nonempty contribution is the R_v prefix, one original-pair τ,
and the R_v suffix, in that order. All four copied operand subgraphs
remain original-only. Different variable positions use the same τ
indexed by the unordered pair of original names; over F₂ its substituted
commutator is independent of which name is written first. Scalar edges
have no marked nonconstant coefficient. Even if R_v is zero through
cancellation, its marked paths remain present. If v is terminal, no
variable-bearing marked edge can lie on a designated R_v path, so
the distinct-endpoint zero shortcut is justified structurally.

An accepting J path has a unique first edge leaving the recurrence
region. The attached C_e has only its specified entry and exit, and
its exit goes to the fresh sink. An internal walk leaving a copied
designated exit cannot reach that exit again in a DAG. There is no
other cross-copy connector. Thus the first-exit partition implements
(3) without either extra accepting paths or copies of recursive J_v.
At substitution its edge contribution is exactly
l_e g_v+l_e R_v+l_e R_v+R_v l_e=l_e g_v+R_v l_e.
The middle terms have identical word order and cancel in F₂. Scalar
terminal bases and induction prove (4), and setting placeholders to
zero proves the first identity separately. No correction is moved
through a suffix or used as an L035 operand.

For W, the receiver's suffixes F_(u′),G_(v′) are copies of U,V with
fresh scalar exits; they contain originals only. L085 needs no fidelity
or ER hypothesis for its displayed paired recurrence. Directly,
F m+m F=d(F z_k+z_k F), and
l m+h=bd(z_k²+z_k). Multiplication on the stated left and right gives
the local identity in part 3 with its two corrections in exactly the
written order. Summing over all edge-pair occurrences gives the parent
identity, and terminal scalar products cancel against P's terminal
value. The common first-exit graph gives W(0)=0 because terminal pair
states cannot accept and each local exit contains one placeholder.
The same argument covers zero coefficients, absent edges and cancelling
suffixes; the path-free K shortcut is confined to scalar terminals.

P uses at most one affine factor from each successive level, so each
word lies in the increasing-multilinear subspace of D's order. Its
Boolean values are the product of the two graph values by the local
identity h(a)=l(a)m(a) and backwards induction. Reversal preserves
scalar evaluation, giving P(a)=f(a)g(a)=0 under the stated promise.
L026's injectivity therefore proves P=0 in precisely its admitted
subspace. Equation (6) then substitutes to
f R_root+f g+f R_root=fg; at zero placeholders both branches vanish.
Only disjoint graph composition is used. There is no commutation of
f with J and no assertion that g equals its reversal formally.

The independent resource check counts records before charging bit
lengths. Normalization adds one root, O(number of terminals) scalar
connectors and at most one new edge per original last-edge occurrence,
so N≤cM independently of semantic cancellation. One C_e enumerates
O(N) marked choices against the single-edge operand, with O(N) copied
records per choice, giving O(N²). All O(N) C_e and the recurrence
region give O(N³) for J. For W, the sum over same-level pairs of
outdegree products is at most m_U m_V≤N². Each occurrence has an
independently copied O(N²) K block, O(N) suffix factors and constant
connectors. Pair states, P and scalar exits are included in O(N⁴).
The extra fJ branch adds O(N³+N), not a multiplication of these
record counts. Retaining constructed R_v, C_e, K and P as separate
intermediates as well as their incorporated copies changes only the
constant allowance: their complete generation has the same counts.

There are O(N⁴) primitive copies and records in total. Each copied
complete original B/name package costs at most M bits. Each affine
label has boundedly many entries, with original or placeholder names
of at most M bits; dense endpoints require O(log(M+2)) bits. Lengths,
root associations, coefficients and framing have no larger cost.
Consequently O(N⁴(M+log(M+2)))≤K(M+2)⁵ pays the entire output and
retained intermediates in the original pre-witness M. A straightforward
constructor enumerates those O((M+2)⁴) record/copy operations. Even
allowing O(L²) bit operations per operation for complete-buffer scans,
name lookup, copying and renumbering, where L=K(M+2)⁵, gives
O((M+2)¹⁴). Parsing and topological checks are smaller; the stated
K′(M+2)¹⁶ bound has slack. No witness-dependent length, semantic-zero
test, monomial enumeration or unit-cost long-name operation is needed.

Finally fix an actual accepting path, including one with a zero factor.
If it exits J after j original edges, it enters C_e with s=q−j query
levels remaining. A marked R_v path uses s−1 variable levels; replacing
one of them and the single l_e factor by one τ leaves at most s−1
nonconstant factors. For s=1 no such marked path exists. Thus J paths
have at most j+s−1=q−1 factors. For W, after j pair transitions the
two exit types have at most 1+(s−1)+(s−1)=2s−1 factors, giving
j+2s−1=2q−j−1≤2q−1. The scalar-terminal K case adds no accepting
paths. The fJ branch has at most q+(q−1) factors. Every accepted path
uses exactly one placeholder, since original/pair prefixes and suffix
factors are original-only and all exits are one-way. These bounds
count structural paths before cancellation and hence verify the
stronger path statement, not just a bound on surviving word degree.

No substantive defect or change to the theorem, construction, bounds
or direct mathematical inputs was found. The audit supplies no executed
implementation, finite graph certificate, arbitrary-order W₂ result,
general ER data, formula-length-only bound or SAT consequence. Full
matching Mathlib coverage remains not checked. Attempts 018/030 retain
their stated scopes; neither supplies an obstruction to this conditional
opposite-order reception. The informal restricted result now has its
separate critical audit, while the independent main gaps remain open.

## Mathlib

Full matching coverage for the opposite-order witness and its explicit
encoding/time bounds is **not checked**, not asserted absent. Local
inputs L026, L035, L085 and L087 have the scopes specified above.
The direct primary citations cover formula commutators and graph
composition, not a full matching opposite-order witness theorem.
The result is local progress beyond the full-statement coverage found
in the assessment, without certified originality or a P-versus-NP claim.
