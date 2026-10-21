# L090 — Exact OBDD-product witnesses after a small order-deletion set

## Hypotheses

Work in F₂⟨y₁,…,y_q⟩. Supply two explicit deterministic dense OBDDs U,V
on the same named alphabet, of nonterminal width at most three, in orders
π,ρ. Each state has a bit-0 and a bit-1 successor at the next level;
only the final level has scalar terminals 0 or 1. Repeated successors,
redundant tests, unreachable states and multiple terminals are allowed.
For q=0 the designated root is a terminal. All records are explicit.
The representatives are the exact ordered free polynomials defined by
L026 (4), separately in each order:

    r_u=(1+z)r_(u,0)+z r_(u,1).

Write f=r_U and g=r_V, and assume fg(a)=0 for every Boolean assignment a.
Supply a set D of k distinct alphabet variables such that deleting them
from π and ρ leaves the same order. Assume k≤floor(log₂ M), where M is
exactly L087's original pre-witness size: 2 plus the complete bit lengths
of the two diagrams, orders, original-name dictionary and full Boolean/
commutator axiom and placeholder dictionaries. Neither H nor a degree
parameter contributes to M. Write

    B=(y_i²+y_i, y_i y_j+y_j y_i : i<j),

at its original listed positions, with placeholders σ_i,τ_ij. The extra
set D is a list of distinct original names; its full length is bounded
by O(M²), without redefining M. Output graphs are explicit acyclic
affine-F₂ ABPs with full dictionaries and references.

## Conclusion

There is a deterministic polynomial-bit-time construction on these
promised inputs of an affine ABP H with formal identities

    H(y,0)=0,                       H(y,B(y))=fg.             (1)

For one absolute K its full encoding has at most K(M+2)^14 bits. More
generally the proof pays K(2^k+1)²(M+2)^12 bits before using the logarithmic
cutoff. Its pre-substitution path degree is bounded by the same polynomial.
The construction does not test the Boolean-zero promise.

This is an all-size informal specialization. The separate step-351
critical audit below found no substantive defect in the stated identities,
endpoint cases or bound; no implementation or finite certificate execution
is claimed.
The checked literature supplies its components, but no full matching
theorem was found in that comparison; originality is not certified.
Arbitrary-order W₂, general ER data availability and unrestricted SAT
decision/separation remain open. Attempt 030's independent universal
value-representation obstruction is unchanged.

## Proof

**Coverage and imports.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-19-small-deletion-set-order-pair-witness.md`.
Import Boolean restriction from Randal E. Bryant, *Graph-Based Algorithms
for Boolean Function Manipulation*, IEEE TC 35(8), 677–691 (1986),
[annotated author copy](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
§1.1 equation (1), printed p.3, and §4.4, printed p.15. Its successor
redirection is specialized below to dense graphs and exact scalar
substitution. Boolean Shannon expansion alone is not the formal lift.
Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, [arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4),
Lemmas 3.6–3.7, pp.17–18, provides the formula-input contextual commutator
comparison. We need graph-sized corrections and use L035's audited
explicit x-only ABP theorem, not an unproved short formula unfolding.
Separate graph sum/product composition is the construction in
Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative
Models*, [author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Lemma 2 Step 1, p.5; no PIT theorem is needed here.

Import L026 (4)–(12) and its ordered-multilinear injectivity, and only
L071's post-compilation value/K/W graph realization. Import L072's
indicator corrections (3) and ordered recombination (5)–(7), specialized
below to supplied cofactor diagrams. No treewidth or ER hypothesis is
dropped from either whole theorem: their diagram-only components use
neither compilation nor an ER derivation. L088/L089 are narrower scope
comparisons, not mathematical inputs. The additional work is the exact
original-polynomial lift and its complete copying ledger; it is not a
reproof of Boolean restriction or of the imported commutator theorem.

**Restriction preserves the exact substituted polynomial.** Fix any
partial assignment α to variables in D. Replace their edge labels by
the corresponding field scalars in the original value graph. At an
assigned test exactly one outgoing label is 1 and the other is 0.
Redirect every incoming reference, and the root if necessary, through
the selected successors until the next unassigned level or a terminal.
Keep every original state on unassigned levels, including unreachable
ones, and all terminal records. Each retained state still has its two
successors at the next retained level. Thus the resulting dense diagram
has at most the original number of states, with width at most three.
Backward substitution in the displayed suffix recurrence proves that
its free polynomial h_α is exactly h|α, for h=f or g. There is no
commutation in this argument: substituted bits are scalars and the zero
branch vanishes. This justifies Bryant's Boolean restriction operation
at the stronger formal-polynomial interface actually used here.

Represent a diagram or any suffix by its affine edge graph, with a fresh
sink receiving a 1-edge from every terminal of value 1 and no edge from
terminals of value 0. This is L071's value graph. Scalar and zero cases
use fresh outer endpoints, retaining empty-path conventions internally.

**An exact one-variable lift.** In one partially restricted diagram,
let z be a still unassigned variable, and cut just before its level.
For each state u of that level let p_u be the root-to-u prefix path sum,
and let a_u,b_u be the value polynomials of its two successor suffixes.
These are explicit x-only affine graphs of at most the original size:
use the prefix subgraph through that level, with endpoints root,u, and
the suffix value graphs just described. A root-level prefix can have
coincident endpoints, hence value 1; an unreachable state has value 0.
By partitioning the finite paths at their unique state on this level,

    h_α=Σ_u p_u((1+z)a_u+z b_u),
    h_(α,0)=Σ_u p_u a_u,       h_(α,1)=Σ_u p_u b_u.          (2)

This is a proof by finite distributivity, not a path enumeration in the
construction. Each prefix and suffix remains a graph.

Apply L035 to p_u and the one-edge graph z. It supplies C_u with

    C_u(y,0)=0,               C_u(y,B)=p_u z+z p_u.

Only original commutator placeholders occur. Put

    J_α=Σ_u C_u(a_u+b_u).                                  (3)

Every occurrence is a disjoint graph copy in the indicated order. Then
J_α(y,0)=0. Expanding (2), the substituted value of (3) is

    Σ_u (p_u z a_u+z p_u a_u+p_u z b_u+z p_u b_u)
      =h_α+(1+z)h_(α,0)+z h_(α,1).                         (4)

Indeed the two extra Σ_u p_u a_u terms on the right cancel. No Boolean
axiom or movement of a placeholder factor is hidden in (4). L035 receives
only the x-only prefix p_u and variable z, never J or an interpolant
correction. This identity is valid even when a_u=b_u or p_u=0.

**Telescoping over the supplied set.** Fix one order D=(z₁,…,z_k), for
example the original alphabet order. For a bit string α of length j set

    e_α=∏_(i=1)^j l_(i,α_i),   l_(i,0)=1+z_i, l_(i,1)=z_i,

with the product in that order and e_empty=1. At every node α of length
j<k form J_α by (3) in the restriction of the original diagram by α,
using z_(j+1). Define, independently for h=f,g,

    L_h=Σ_(j=0)^(k−1) Σ_(α∈{0,1}^j) e_α J_α,
    I_h=Σ_(α∈{0,1}^k) e_α h_α.                            (5)

All J_α vanish at zero placeholders. After B substitution, (4) makes
each summand equal e_α h_α+Σ_b e_(αb)h_(αb). Every interior term occurs
twice, in identical factor order, once as a child and once as a parent.
It cancels in F₂. The root and full-depth terms remain, so formally

    L_h(y,0)=0,                L_h(y,B)=h+I_h.              (6)

At k=0 use the zero graph for L_h and I_h=h; (6) still holds. This
uses 2^k−1 internal nodes, not a multiplicative M^k recurrence. Every
node refers to a separately restricted original graph.

**Common-order branch witnesses.** Write a_α=f_α and b_α=g_α for full
assignments to D, and F=I_f, G=I_g. The two restricted diagrams now have
the same induced order on the complement of D. Their Boolean product
is zero: extend any assignment on the complement by α and apply the
original fg promise. L026's paired representative P_α is increasing
multilinear in precisely this common order and evaluates to zero.
Its injectivity result therefore gives P_α=0 formally. L026 (9), with
L071's explicit post-compilation graph, yields V_α satisfying

    V_α(y,0)=0,                V_α(y,B)=a_α b_α.            (7)

The subset alphabet maps injectively into the original alphabet; its
Boolean and pair-once commutator placeholders map to their unchanged B
positions. Thus both substitutions are preserved. This construction
has no original-clause or ER input. If the complement is empty, the
cofactors are scalars, their product is zero by the promise, and take
V_α=0 directly. This uses injectivity only for P_α, never for original fg.

**Paid recombination and original-product recovery.** On the fixed
z order, L072's indicator correction, itself the L026/L071 construction
on width-two matching/dead diagrams, supplies Q_(α,β) with

    Q_(α,β)(y,0)=0,
    Q_(α,β)(y,B)=e_α e_β+δ_(α,β)e_α.                       (8)

The associated paired representative equals δ_(α,β)e_α by ordered
injectivity. The raw product e_α e_β is not identified with it without
Q. For k=0, e=1 and Q=0. The same subset-placeholder inclusion applies.
L035 applied to the x-only graphs a_α,e_β supplies C_(α,β) substituting
to a_α e_β+e_β a_α and vanishing at zero placeholders. Set

    W=Σ_α e_α V_α
        +Σ_(α,β) (e_α C_(α,β) b_β+Q_(α,β) a_α b_β).       (9)

This is exactly L072's ordered recombination component with zero branch
output. To check its reception explicitly, the two terms for α,β give

    e_α a_α e_β b_β+e_α e_β a_α b_β
      +e_α e_β a_α b_β+δ_(α,β)e_α a_α b_β.

The middle words cancel literally. The double sum is FG+Σ_α e_α a_α b_α;
the first sum in (9), by (7), cancels the latter. Hence W(y,B)=FG and
W(y,0)=0. Finally use fresh graph copies to form

    H=W+L_f g+F L_g.                                      (10)

All three summands vanish at zero placeholders. Equations (6) and (9)
give H(y,B)=FG+(f+F)g+F(g+G)=fg. In particular the original g remains
on the right of L_f, and F remains on the left of L_g. The conclusion
concerns the unchanged original fg, not merely its interpolants.

Every sum is a parallel composition and every product a serial composition
of independent graphs with unit connectors and fresh outer endpoints.
An internal designated exit with outgoing edges cannot be left and
revisited in a DAG; those edges create no extra route to a later factor.
All cross-copy edges move forward in the displayed factor order.
Consequently these are acyclic affine ABPs, including constant factors,
zero components, parallel edges and coincident prefix endpoints.

**One full-bit ledger.** Put R=M+2 and t=2^k. Original state, edge and
alphabet counts are O(R); every written original name has at most R
bits. We may copy all original states and terminal records even when
unreachable. Each restricted diagram, prefix, suffix, suffix sum or
indicator has O(R) records and at most O(R²) full bits with complete B
framing and original names. Root redirection and restrictions for all
nodes take polynomial bit time in R,t; for example following at most q
successors for each of O(R) references per node suffices. The full
set-name list is also within O(R²).

Every L035 call in (3) or (9) has complete input E≤C R², including its
full commutator dictionary. Its output therefore costs at most C'R^8
full bits by L035's O(E^4) bound. Repeated Boolean dictionary framing,
when not used in a call, adds only O(R²). There are at most 2(t−1)O(R)
calls of type (3) for the two inputs, and t² of type (9). The cut-state
bound O(R) deliberately avoids relying on width at that cut. Each
occurrence of C_u has its own suffix sum and prefix indicator in (5),
costing O(R²) more. Thus independently written lift blocks and all
their local dictionaries cost O(tR^9) before global reference rewriting.
There is no recursively copied L_h in this bound.

For each V_α there are at most O(R²) same-level state pairs, even when
all terminal records are retained. L071 gives two recursive affine
edges per nonterminal pair and a constant number of local exit blocks,
each containing O(R)-record value/K graphs. The copies cost O(R³)
records and O(R^4) full bits, including names and dictionary. The
recursive pair region only moves forward and never receives a return
from a local block. This counts actual W graphs rather than unfolded
recurrences. The same generous O(R^4) bound covers each Q_(α,β).
All t copies of V_α, t² copies of Q_(α,β), and every branch/value/
indicator occurrence in (9) are charged separately. Their total is
O(tR^4+t²R^8), dominated by the L035 allowance for (9).

The explicit interpolants F,G have O(tR) records and O(tR²) local full
bits. The factors L_f,g,F,L_g in (10) are independently copied once
each, not once per path. Retaining the previously constructed auxiliary
outputs as well increases all these bounds by only a constant factor;
all per-call input copies cost O((tR+t²)R²), already smaller. The
aggregate local bit and record allowance is therefore

    A≤C(tR^9+t²R^8+tR²+R²)≤C'(t+1)²R^9.

All connectors, source/sink records, root references and tuple indices
fit this allowance. Rewriting any global record reference costs at most
O(log(A+2))=O(log(t+1)+log R). Since k≤q≤O(R), this is O(R), even
before using k≤log₂ M. Charging a full O(R) factor to every local bit
and record, plus fresh full dictionary copies and the original input,
gives O((t+1)²R^10). The stated K(t+1)²R^12 is a uniform slack bound.
There are no implicit edges, uncharged dictionaries, unbounded names or
free sharing across outputs. With t≤M it is at most K'R^14.

Each call has the deterministic polynomial bit time of L035; all other
work consists of the stated finite loops, graph copies, reference
redirection and renumbering. Hence there is one fixed polynomial bit-time
bound in R,t, and in M under the cutoff. This need not equal the output
exponent. Every accepting path in an acyclic affine graph uses fewer
edges than its vertex count, so the same full-size bound also bounds
pre-substitution path degree. No semantic-degree assumption is used.

Empty D, q=0, D equal to the whole alphabet, constants, repeated
successors, multiple terminals and unreachable states were included
above. The semantic promise is used only in (7), not as an algorithmic
oracle. No global intermediate reordering-width theorem, general W₂,
faithful-value availability claim or SAT transfer is obtained.

**Separate critical audit — step 351, 2026-10-19.** This audits the same
statement under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-19-small-deletion-set-order-pair-audit.md`.
It does not extend the width, deletion-set or Boolean-zero promises.
The source comparison and precise primary citations above are reused.
In particular Bryant supplies restriction, not the free-ring lift;
LTW supplies formula corrections, not an ABP-size estimate. L035 supplies
the latter, and only the diagram components of L026/L071/L072 are used.

For exact restriction, induct from the final terminals backward in the
original diagram. A substituted test becomes 1 times its selected child
plus 0 times its other child. An unassigned test retains its two ordered
left factors. Redirecting through a chain of assigned tests therefore
preserves precisely the scalar-substituted free polynomial at every
retained state and at the root. It does not require any factor swap.
After redirection the retained levels are exactly the unassigned levels;
no new state is introduced and terminal labels remain scalar bits.
Unreachable states can stay without changing any designated root value.

At the next queried variable z, a path to the fresh value sink visits
exactly one state u on its dense cut level and exactly one of that state's
two outgoing edges. Its before-cut factors are exactly those counted by
p_u; its remaining factors are exactly those counted by a_u or b_u.
Conversely each such prefix/edge/suffix concatenation is a path, since
levels increase. Thus (2) holds with all multiplicities, including
parallel edges and several 1-terminals, without constructing path lists.
The prefix ends at u, before the z-edge; it contains no z and no witness
placeholder. L035 nevertheless needs only its x-only graph property,
not syntactic nonzeroness or a formula representation. Its empty-path
and disconnected-input conventions admit p_u=1 and p_u=0.

The noncommutative expansion of the right side of (4) has two copies
of each p_u a_u, which cancel, and exactly
p_u z a_u+p_u z b_u+z p_u a_u+z p_u b_u remaining.
These are precisely (p_u z+z p_u)(a_u+b_u), in that order.
This verifies the lift without commuting a suffix or using a Boolean
quotient. If a_u=b_u, its correction is formally zero; equal successor
edges are still retained by the construction. If p_u is a scalar, the
commutator vanishes formally, including scalar values obtained by path
cancellation. No such cancellation is used to delete a non-scalar graph.

For telescoping, let T_j=Σ_{|α|=j} e_α h_α. The sum of the depth-j
terms of L_h after substitution is exactly T_j+T_(j+1): multiplying
(4) on the left gives e_α l_(j+1,b)=e_(αb), with the next literal
appended on the right of the existing indicator. Hence summing depths
leaves T_0+T_k=h+I_h. This also checks arbitrary relative positions of
z_(j+1) in the two original orders. Every h_α is independently obtained
from the original diagram; no correction is nested inside another
L035 input. At zero substitution every depth term is zero separately.

At full depth the complement orders agree. In L026, the paired P is
increasing multilinear in that one order, and its evaluation is the
product of the two cofactor values. The Boolean-zero promise makes
those evaluations zero. The induction following L026 (4) then makes
P formally zero. L071's pair-to-pair edges and three one-way local
exit blocks compute the identical W recurrence, so (7) is a formal
consequence of L026 (9), without a new semantic test. For indicators,
their matching/dead diagrams compute their exact ordered literal products.
The same injectivity argument identifies their paired P with
δ_(α,β)e_α, which is in that increasing-multilinear space, giving (8).
It is never applied to the raw products a_α b_α or e_α e_β.
Subset Boolean symbols and unordered distinct-variable pairs map to
their original B positions; in F₂ reversing a pair's listing changes
neither its commutator nor its substitution. Both substitution maps are
therefore respected even when the common order differs from name order.

In (9), the cross term from the commutator block and that from Q have
the identical word e_α e_β a_α b_β; their cancellation leaves
e_α a_α e_β b_β+δ_(α,β)e_α a_α b_β.
The double sum is FG plus the diagonal branch sum. Equation (7) cancels
that diagonal sum, and (6) in (10) leaves
FG+fg+Fg+Fg+FG=fg. This checks the original-product orientation:
the lift of f is followed by original g, while the lift of g is preceded
by F. Every summand of H independently has a zero-at-zero witness
factor. No claim of literal indicator orthogonality in the free ring
or of commutation of witnesses enters either identity.

The endpoint convention was also checked directly. A prefix graph with
root=u has only the empty root-to-u path. A copy with a designated exit
having outgoing edges can contribute to the next factor only through
that exit's connector; following an internal outgoing edge cannot reach
the connector again in a DAG. Fresh outer endpoints distinguish zero
graphs from empty-product graphs. Multiple terminal-1 records each get
one exit edge; terminal-0 records get none. All cross-copy edges advance
in factor/branch order. Thus no accepting path bypasses a required
witness factor, including scalar factors or dead components. With k=0,
L_f=L_g=0 and F=f,G=g; Q=0 and commutation with e=1 is zero, leaving
the common-order branch witness. With empty complement all a_α,b_α
are scalar bits and a_α b_α=0, so the chosen zero V_α is correct.
With q=0 both statements apply and the scalar fg is zero by the promise.

For an independent bound, retain R=M+2 and t=2^k from the proof.
Each restricted diagram, prefix, suffix sum or indicator has O(R)
records. A record needs O(R) original-name payload and O(log R) local
references; the complete original dictionary is already in M. Thus
O(R²) full bits per input copy is valid even with repeated full framing.
L035 receives two such graphs plus its complete pair dictionary,
so E=O(R²) and its proved O(E⁴) bound gives O(R⁸) per output.
There are at most O(tR) lift calls and exactly t² recombination calls.
Adding the separate suffix/indicator factors costs O(R²) per lift call,
giving O(tR⁹) total for both lifts and O(t²R⁸) for these pair blocks.

For one V_α the number of same-level pairs is at most the product of
the two total state counts, O(R²), including every terminal pair.
Each nonterminal pair has two recursive edges and constantly many local
blocks, whose value/K factors have O(R) records each. This gives
O(R³) records and O(R⁴) bits. Repeating a full O(R)-bit dictionary for
every local block would cost only O(R³) more and is covered. The same
bound covers Q, whose indicator diagrams have O(R) records; all t branch
and t² indicator-pair copies are charged. Optional P graphs and K
templates used to realize these components fit this allowance as well.
The interpolants and their separately retained copies cost O(tR²).
The final products in (10) copy each complete factor once; they do not
distribute a lift across the paths of the other factor. All these local
costs are bounded by A=O((t+1)²R⁹), including connector records.

Global endpoint/root/tuple references require O(log(A+2)) bits each.
Here log t=k≤q≤O(R), independently of the logarithmic cutoff, so
charging an extra O(R) factor to every local bit/record suffices.
This gives O((t+1)²R^10), within the claimed K(t+1)²R^12.
All original dictionaries and the D-name list were included before
this renumbering; M has not been enlarged by any output. Finally t≤M
gives the stated O(R^14). Finite restriction/redirection loops and the
O(tR+t²) polynomial-time L035 calls give one fixed polynomial bit time
in R,t. The affine DAG vertex count bounds every path's number of
nonconstant edges, so it also bounds pre-substitution path degree.

The audit found no substantive identity, endpoint, hypothesis or copying
defect and required no change to the construction or its bound. This is
new informal checking evidence, not a new theorem, a finite execution,
a machine-checked proof, or certified originality. The arbitrary-order
witness, general ER availability and unrestricted SAT gaps remain open.

## Mathlib

Full matching coverage was not checked. No absence claim is made. The
argument uses finite distributivity in the free associative F₂ algebra,
explicit finite DAG sums/products, and the cited local constructions.
No Mathlib formalization or machine-checked all-size proof is claimed.
