# L096 — Small source cores give exact occurrence-product witnesses

## Hypotheses

Work over F₂ in exactly L087's occurrence construction for a width-at-most-
three source CNF F. Append its two u/v clauses, retain each distinct
occurrence name y_(j,k), its clause/literal position and the original
dictionary, and use its two dense width-at-most-three testers D,E.
D tests split clauses in clause order; E tests equality of raw occurrence
bits within each old-variable group in group order. Let f,g be their exact
ordered free-ring representatives, in their respective supplied orders.
Keep all original records, including dead states and the appended gadget.
The full original Boolean/commutator list B and pre-witness parameter M
are unchanged from L087. No source-clause placeholder or unsplit source
variable may occur in the output witness.

Supply a canonical binary list I of c distinct source-clause indices
whose conjunction is unsatisfiable, with c≤floor(log₂ M). Indices refer
to F, excluding the appended two clauses. Distinct source positions may
contain equal clauses. Repeated literals, complementary literals, empty
clauses and unused diagram records retain L087's meanings.

F specifies the provenance of the supplied occurrence pair; a second,
separately serialized copy of F is not included in M or required by the
constructor. The constructor below receives the pair and I, extracts
occurrences using their actual clause-position names, and verifies the
branch condition it uses. It does not promise to recompute the pair from,
or scan, an arbitrarily larger separate source file in time polynomial
in M. This distinction matters when F has many empty clauses.

## Conclusion

There is a deterministic polynomial-bit-time constructor, on these
promised inputs, of an explicit acyclic affine-F₂ ABP H using only the
unchanged occurrence originals and B placeholders, such that formally

    H(y,0)=0,                     H(y,B(y))=fg.              (1)

For an absolute K its full binary encoding is at most K(M+2)^18 bits.
The same bound can pay for all auxiliary outputs, complete repeated
dictionaries, the annotation and original pair retained with the output.
It also bounds pre-substitution path degree. The constructor checks a
sufficient branch condition without relying on an UNSAT oracle; all
promised inputs pass. It does not find I or certify source-to-pair
provenance from an uncharged external file.

This is local informal progress under an additional source-core promise,
with no certified originality. The separate step-376 critical audit below
found no substantive defect in the identities, reception or stated bound.
There is no implementation or finite graph-certificate execution here.
It supplies neither small cores for arbitrary UNSAT formulas nor
arbitrary-order W₂, general ER data, or a SAT decision/separation theorem.
L095's partition obstruction and Attempts 018/030/031 remain intact.

## Proof

**Coverage and precise imports.** The pre-invocation SPECIALIZE assessment
is `drafts/literature/2026-10-20-small-unsatisfiable-core-occurrence-witness.md`.
Reuse L087's explicit specialization of the occurrence-splitting mechanism
in Meinel–Theobald, *Algorithms and Data Structures in VLSI Design: OBDD —
Foundations and Applications* (Springer, 1998), Theorem 4.32 proof and
Lemma 4.35, inspected pp.72–74
([inspected copy](https://www.slideshare.net/slideshow/algorithms-and-data-structures-in-vlsi-design-259675197/259675197)).
The actual small testers, literal signs and exceptional clauses needed
here are L087's proved transition systems, not an unstated stronger
theorem about the book's different SAT syntax.

Bryant, *Graph-Based Algorithms for Boolean Function Manipulation*,
IEEE TC 35(8), 677–691 (1986),
[annotated author copy](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
§4.4 printed p.15, supplies Boolean restriction. L090's audited restriction
paragraph and equations (2)–(6) supply exact scalar restriction and the
stronger free-ring lift; its equations (8)–(10) supply paid indicator
recombination and original-product recovery. We do not invoke L090's
whole theorem or its common-residual-order branch construction (7).

L035 supplies graph-sized original-only commutator witnesses, including
arbitrary endpoints and zero inputs. Its source comparison with
Li–Tzameret–Wang, [arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4),
Lemmas 3.6–3.7, printed pp.17–18, retains that source's formula-input
qualification. Separate-graph sum/product composition is the inspected
Raz–Shpilka [author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Lemma 2 Step 1, printed p.5, received with L090's endpoint conventions.
L026's injectivity paragraph after (4) is used only for an individual
ordered-multilinear factor. No general Boolean-to-free-ring implication,
core-finding theorem, formula unfolding or new PIT theorem is used.

These inputs do not prove the target outright. The additional argument
is the following factor-zero branch ending, its reception without
residual-order agreement, and its changed cutoff/annotation accounting.

**Select occurrence names, not unsplit variables.** Let S contain every
occurrence y_(j,k) with j in I, in fixed original dictionary order.
Its names are distinct even for repeated literals. Put s=|S| and t=2^s.
Width at most three gives

    s≤3c≤3 floor(log₂ M),             t≤M³.                (2)

No appended gadget occurrence belongs to S. Restrict each original tester
by a complete bit assignment α to S. As in L090, scalar substitution and
successor redirection yield dense diagrams on the unassigned variables
with their respective induced orders. Retain every state on each
unassigned level and all terminal records. Write

    a_α=f|α,                         b_α=g|α.

These are exact free polynomials of the restricted diagrams, rather than
merely Boolean-equivalent replacements.

**Every branch has a formally zero factor.** First suppose α assigns
different raw bits to two selected occurrences of the same old variable.
Every extension of α to all occurrence names fails E's equality test,
irrespective of the signs of those literal occurrences. Thus b_α evaluates
to zero on every Boolean assignment of the unassigned occurrences.

Otherwise all selected occurrences of each old variable have the same
raw bit. They define an assignment v to every old variable appearing in
the selected clauses. Unsatisfiability of that selected conjunction implies
that at least one selected clause C_j is false under v. All of C_j's
occurrence variables lie in S; their signed evaluations under α are its
literal evaluations under v. Hence the corresponding split clause is
false on every completion of α. Every such completion fails D, so a_α
evaluates to zero on every remaining Boolean assignment.

This includes an empty selected clause: it is false under every v, and
L087 starts D at its dense failure state. Complementary literals cannot
form a false clause under consistent raw bits, but they cause no problem:
unsatisfiability supplies some false clause. Literal/clause repetitions
do not identify their distinct occurrence positions.

Each restricted factor separately lies in the span of increasing
multilinear words in its own induced order: this is L026's suffix
invariant, preserved by scalar restriction. Apply L026's injectivity
separately to the factor whose Boolean function is identically zero.
It is therefore zero as a free polynomial. Consequently, on every branch,

    a_α=0 or b_α=0 formally; hence a_α b_α=0.              (3)

The two orders need not agree, and no injectivity is asserted for their
raw product. Set the branch witness V_α to the zero graph, with distinct
endpoints and no accepting path. It has both identities required at
L090 (7), because of (3).

**Reception by the already proved ordered components.** For S ordered
as z₁,…,z_s define e_α=∏_i l_(i,α_i), with l_(i,0)=1+z_i and
l_(i,1)=z_i, in this fixed order. For s=0 the sole indicator is 1.
Use L090 (2)–(6) independently on D and E to construct L_f,L_g and
the original-only interpolants

    P=Σ_α e_α a_α,                   Q=Σ_α e_α b_α,
    L_f(y,0)=L_g(y,0)=0,
    L_f(y,B)=f+P,                    L_g(y,B)=g+Q.          (4)

The lift uses independently restricted original diagrams at each node,
with original-only prefixes in every L035 call. It uses neither residual
order agreement nor the old cutoff s≤log₂ M. We retain its finite
assignment-tree construction before the final resource specialization.

Let T_(α,β) be L090 (8)'s indicator correction, so

    T_(α,β)(y,0)=0,
    T_(α,β)(y,B)=e_α e_β+δ_(α,β)e_α.                    (5)

This component only needs the common fixed order on the indicators.
Its subset Boolean/commutator symbols map to their original positions
in B. Apply L035 to the original-only graphs a_α,e_β to obtain C_(α,β)
vanishing at zero placeholders and substituting to a_α e_β+e_β a_α.
No placeholder-bearing lift or witness is an L035 operand. Define

    W=Σ_(α,β) [e_α C_(α,β) b_β+T_(α,β) a_α b_β],
    H=W+L_f g+P L_g.                                       (6)

All products have exactly the written order. After B substitution the
α,β summand of W is

    e_α a_α e_β b_β+e_α e_β a_α b_β
       +e_α e_β a_α b_β+δ_(α,β)e_α a_α b_β.

The middle terms cancel literally. Summing leaves
PQ+Σ_α e_α a_α b_α=PQ by (3). Equation (4) then gives

    H(y,B)=PQ+(f+P)g+P(g+Q)=fg.

Every summand in (6) has a zero-at-zero witness factor, proving H(y,0)=0.
This is L090's recombination with zero branch witnesses; its missing
common-order premise is replaced precisely by (3), and nowhere else.
In particular the right factor in L_f g remains the original g.

Use independent affine-graph copies, serial unit connectors and fresh
outer endpoints for every displayed sum and product. The proof of
L090 (9)–(10) includes scalars, zero polynomials, parallel edges and
coincident internal prefix endpoints. Cross-copy edges move forward in
factor order, and a designated exit cannot be left and revisited in a DAG.
Thus no path bypasses a required factor; all graphs remain explicit
acyclic affine ABPs with the stated formal polynomials.

**Annotation and constructive branch checks.** Use the actual clause/
position occurrence names of L087, not aliases that erase those positions.
The two appended clauses have indices m+1,m+2, where m is F's clause
count. Their names already occur in the input dictionary. Canonical
binary writing of any source index j≤m therefore takes O(M+2) bits.
With c≤log₂ M, the whole annotation, including count/framing and index
separators, costs O((M+2)²), without altering M. Reject noncanonical
index encodings, duplicates, indices outside 1,…,m and a failed cutoff.
Repeated clauses at distinct valid indices are allowed.

Extract S by scanning the full occurrence dictionary for these indices.
A valid source position with no occurrence is an empty clause, not an
unrepresented witness variable. Check s≤3c. This scan and all equality/
range comparisons have polynomial bit cost in M. Original unsplit names
never become witness variables. The source-to-pair construction remains
a hypothesis; no uncharged source file is consulted to establish it.

The constructor can additionally verify exactly the branch fact needed
by (6): for each of the t assignments, restrict the two testers and test
whether either has no root-to-terminal-1 path. Use ordinary directed
reachability with each bit transition available at each unassigned test.
A deterministic ordered diagram queries each remaining variable once,
so every such directed path is realized by a Boolean assignment, and
every assignment induces such a path. Thus absence of an accepting path
is equivalent to identically zero Boolean value of that single tester.
L026 then gives formal zero as above. This is not reachability in the
arithmetic graph, where edges 1+y and y can cancel.

Reject if a branch has accepting paths in both testers. Under the
supplied unsatisfiable-core promise, (3)'s stronger single-factor
reasoning makes every branch pass. For malformed or unpromised data that
pass the syntax and branch checks, the subsequent formal assembly is
still sound. The check certifies sufficiency of the queried occurrences;
it need not decide whether precisely the named source subformula is
UNSAT. A contradiction elsewhere in F can also make branches pass.
No stronger annotation-recognition claim is required or made.

**Complete original-M ledger.** Put R=M+2. Apply L090's audited
pre-cutoff ledger with s queried variables and t=2^s. Its mathematical
construction and counts before the last cutoff do not require agreement
of residual orders except for V_α, which here is zero. More explicitly:
each restricted diagram, prefix, suffix sum or indicator has O(R) records
and O(R²) full bits including the complete original B and name framing.
Each L035 call has E=O(R²), and output O(E⁴)=O(R⁸) bits. There are
O(tR) lift calls and t² recombination calls; all independent contexts
and retained copies cost O(tR⁹+t²R⁸). Each indicator correction costs
O(R⁴), as in L090; all t² copies and their complete dictionaries fit
the latter allowance. All t branch witnesses are constant-size zero
graphs, or O(R²) each if their full dictionaries are repeated.

P,Q have O(tR²) local full bits. Each final factor in (6) is copied
once per written occurrence, without distributing products into paths.
Retaining the original pair, I, all restrictions, call inputs, auxiliary
outputs and dead original records adds O(tR²+R²), already covered.
Connector records, tuple indices and local roots are included, giving

    A≤C(t+1)²R⁹

for all local bits/records. Global renumbering costs O(log(A+2)) bits
per reference. Since s≤q≤O(R), even before (2) an extra O(R) factor
suffices. Repeated dictionaries and framing fit the same allowance.
The conservative audited bound K(t+1)²R^12 therefore remains valid.
Now (2), rather than L090's t≤M cutoff, gives

    K(t+1)²R^12 ≤ K'R^18.                                  (7)

This charges occurrence assignments and all ordered pairs, not merely
clause assignments. M was fixed before the annotation, branch graphs,
witness or degree. No supplied length was enlarged to absorb the output.

Syntax checking, annotation extraction and all t branch reachability
checks cost a fixed polynomial in R,t. Restrictions follow at most q
selected successors per reference; graph-building uses O(tR+t²) L035
calls of polynomial bit cost on E=O(R²), the indicator constructions
already paid in L090, and explicit copying/renumbering loops bounded
by the displayed output ledger. Their composition has one fixed
polynomial bit-time bound in R,t, hence in M by (2). It does not
enumerate accepting paths or noncommutative monomials. The vertex count
of an acyclic affine graph bounds its accepting-path length and thus
its pre-substitution degree, including paths whose contributions cancel;
(7) is also a valid degree bound.

If s=0, the only possible promised core contains an empty clause and
f=0; the same formulas work with indicators 1 and zero branch product.
The empty list of selected clauses is satisfiable and is not a promised
core. An empty source conjunction has no promised core either. Whole-
alphabet restrictions and scalar cofactors are already covered by (3)
and L090's endpoint conventions. Tautologies, repeated signs/clauses and
unreachable states require no altered product or reduced input package.

The branch condition and the ledger meet the proposed continuation
test. This establishes only the stated restricted supplier. In particular
no small-core theorem for general UNSAT is inferred from it, and a
short witness for this easy-to-verify annotation class does not settle
L087's universal premise or P versus NP.

**Separate critical audit — step 376, 2026-10-20.** This reviews the
unchanged statement under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-20-small-core-occurrence-witness-audit.md`.
The precise source comparisons above and in step 373 are reused. The
audit uses L090's already audited components, not its whole theorem:
its branch construction (7) is not available here. The new branch
ending, its Boolean check and changed original-input ledger are checked
below. No implementation or finite certificate test is claimed.

For any fixed assignment α to S there are two exhaustive cases. If two
selected occurrences of one old variable have different raw values,
E rejects every completion: its single group memory must either already
be in failure or encounter both conflicting bits and enter failure.
Selected occurrences need not be consecutive in that group. Signs play
no part in E. If no such pair exists, define v on each old variable
appearing in a selected clause by its selected raw value. Every literal
of every selected clause has an occurrence in S, so v evaluates the
entire selected conjunction. Its UNSAT promise supplies a false clause.
All that clause's signed occurrence evaluations are already fixed false;
D therefore rejects every completion. An empty clause instead puts the
original root in failure before any query. Repeated source clauses
remain different clause positions, and repeated literals remain distinct
queried occurrences. Complementary literals do not invalidate the
argument: they make their clause true in the consistent case, so another
clause must furnish the contradiction. No source assignment or core is
found by the constructor.

In either case exact scalar restriction preserves the selected tester's
ordered suffix polynomial, by L090's backward-substitution argument.
It remains a linear combination of increasing multilinear words in
that tester's remaining order. L026's injectivity, including its scalar
base case, makes this polynomial formally zero. The argument does not
require the other factor to have the same order. In particular it does
not use Boolean vanishing of a product as evidence of formal vanishing
of that product. This proves the precise replacement of (7) in L090:
the zero graph is a valid branch witness because a whole factor is zero.

For reception, first validate the ordinary L087 diagram syntax used by
the construction: explicit distinct occurrence names; two permutations
of that same alphabet; legal designated roots; at most three states per
nonterminal level; exactly one successor for each bit at the next
level; and only final Boolean terminals. Validate the full listed B and
its placeholder positions against that alphabet. These are finite
string, reference and level checks in polynomial time in M; they do not
validate source provenance. The actual y_(j,k) coordinates must be
available in the name dictionary, as the hypotheses require.

On promised inputs the final four names in π are precisely
y_(m+1,1), y_(m+1,2), y_(m+2,1), y_(m+2,2). Thus the constructor can
recover m from these already written indices, using binary subtraction
and comparisons, without scanning or listing the m source clauses.
Their presence is guaranteed even when F is empty or has many empty
clauses. Check this suffix pattern as part of the pair-and-index syntax;
the pattern is not asserted to prove that the rest of the pair arose
from F. Canonical writing of a valid j≤m has length no greater than
that of m+2, up to fixed framing. That length is at most O(M).
Consequently c≤floor(log₂ M) valid indices occupy O(M log(M+2)),
within the claimed O((M+2)²) allowance. Canonical zero, negative,
duplicate and out-of-range indices are rejected. Count/framing and
separators satisfy the same bound. If a total bounded-time parser is
desired on arbitrary annotation strings, reject once that generous
allowance is exceeded; every promised annotation remains readable.
No polynomial-M bound on reading an arbitrarily long malformed string
or external source file is needed.

Scan the actual dictionary and select all names with first coordinate
in I. Distinct names are counted separately, and check s≤3c. Absence of
any occurrence for a valid selected position means an empty clause
only under the provenance promise. The algorithm does not need to trust
that interpretation for soundness: it checks the resulting S directly.
For each α, scalar-successor redirection yields dense deterministic
testers on their remaining variables. A root-to-1 path specifies one
bit per tested remaining variable, with no repetition, so it extends
to a complete assignment inducing that path. Conversely each assignment
induces exactly one path. Thus accepting-path reachability is equivalent
to existence of a satisfying assignment for that single restricted
tester. This is a Boolean transition-graph test, not a path test on the
affine graph with labels 1+y and y.

The check accepts a branch exactly when at least one tester has no
accepting path. By the preceding injectivity argument it then has a
formally zero factor. Requiring this on every branch is sufficient for
the formal assembly even on a syntactically valid pair not having the
promised source provenance. It does not recognize precisely the claimed
UNSAT subformula. For example, failure of D caused by an unselected
empty clause can make the check pass. Conversely, both testers might
have some accepting assignment while having no common accepting
assignment; the check rejects that branch, correctly declining this
sufficient method rather than asserting satisfiability of their product.
On all promised inputs the exhaustive dichotomy above proves acceptance.

The two lifts satisfy L_f(B)=f+P and L_g(B)=g+Q for this arbitrary S:
their internal cut-prefix commutators and additive telescoping make no
use of a common residual order or of the cutoff on s. At each assignment
tree node the diagram is a fresh restriction of the original input.
Each L035 operand is therefore an explicit original-only graph, either
a cut prefix and a variable, or a_α and e_β. Original-only indicators
have affine literal edges; scalars, no-path inputs and coincident prefix
endpoints are admitted by L035. No lift or previously constructed
placeholder witness is used as an operand.

The indicator correction uses only their fixed common order. Its subset
Boolean symbols and unordered commutator pairs are mapped to exactly
their original B positions. The ordering of a pair's indices does not
change its axiom over F₂. Hence the imported correction respects both
substitution maps even when dictionary order differs from indicator
order. It corrects e_α e_β to δ_(α,β)e_α; it does not assume literal
orthogonality of free indicator products.

Independently expanding the two terms for α,β in W(B), the commutator
term is e_α a_α e_β b_β+e_α e_β a_α b_β and the indicator term is
e_α e_β a_α b_β+δ_(α,β)e_α a_α b_β. The identical middle products
cancel without moving any factor. Summing the remaining terms gives
PQ+Σ_α e_α a_α b_α=PQ, by factor-zero closure. Therefore

    H(B)=PQ+fg+Pg+Pg+PQ=fg.

At zero placeholders each displayed summand of H separately contains
a vanishing witness factor, giving H(0)=0 independently of cancellation.
This checks the exact original product: original g, not Q, follows L_f;
P precedes L_g. Serial composition uses fresh disjoint copies in this
factor order. Inside a copy, leaving its designated exit cannot lead
back to that exit in a DAG; it therefore creates no additional route
to the next factor. Parallel branches share only their fresh outer
endpoints. Zero graphs have distinct endpoints and no path, whereas
an empty product is 1. These facts cover dead records, repeated
successors, internal coincident endpoints and scalar cofactors.

For an independent ledger let R=M+2 and t=2^s. The original alphabet,
state and edge counts are O(R), and the full original dictionaries
already contribute to M. A restricted diagram, prefix, suffix sum or
indicator has O(R) records and O(R²) bits even if original names and
full dictionaries are copied afresh. The s-entry selected-name list and
the c-entry index list also fit O(R²). L035 thus receives E=O(R²) bits
per call, giving O(R⁸) output bits by its proved O(E⁴) slack bound.
The two complete binary assignment trees contain 2(t−1) internal
nodes. At each node there are at most O(R) cut states, giving O(tR)
lift calls. Each correction has its own suffix sum and partial-indicator
copy; these add O(R²) per call and do not multiply the number of calls.
The lifts, including their local framing, cost O(tR⁹).

There are exactly t² ordered recombination pairs, including diagonal
pairs and pairs with zero cofactors. Each uses one independent
commutator graph and O(R²)-bit original-only contexts. Each indicator
correction has O(R⁴) bits by L090's audited matching-diagram component,
including its local blocks. Therefore all pair blocks fit O(t²R⁸).
The zero branch witnesses, their dictionaries if retained, the two
interpolants and all full-depth restrictions fit O(tR²). Restrictions
at internal nodes fit the same allowance because there are O(t) nodes.
All separately retained inputs to calls cost O((tR+t²)R²), already
dominated. The whole lifts and interpolants are copied only a constant
number of times in H and the auxiliary archive; no product is expanded
over paths. Original dead states and records are retained in these
explicit copies. Connector and local-root records yield the aggregate
local bound A=O((t+1)²R⁹).

Renumbered references cost O(log(A+2)) per occurrence. Since s≤q=O(R),
this logarithm is O(R) even before using the clause cutoff. Charging
an extra R factor everywhere yields O((t+1)²R^10), below the stated
K(t+1)²R^12 allowance. Repeated complete dictionaries, retained original
input and annotation are included. Finally

    t≤2^(3 floor(log₂ M))≤M³,
    (t+1)²R^12≤4R^18.

Thus an absolute change of K absorbs the complete output in the stated
R^18 bound. In particular t² can be as large as M⁶; replacing it by
M² or measuring assignments by clause count would be unjustified.
Binary index arithmetic never iterates to m, which can be exponentially
larger than its written length when most clauses are empty. Restriction,
reachability, dictionary mapping and copying use polynomially many bit
operations in R,t, as do the O(tR+t²) calls with E=O(R²). This yields
one fixed polynomial construction time in M; equality of its exponent
with the output exponent is not asserted. Every accepting path has
length bounded by its explicit DAG's vertices, so R^18 also pays the
pre-substitution path degree, including paths with cancelling values.

For s=0 a promised nonempty index list can select only empty clauses,
and D is zero. The single indicator is 1, both lifts can be zero, and
the identity still yields fg=0. An empty selected list or an empty source
conjunction has no promised UNSAT core. Whole-alphabet restrictions and
scalar cofactors are admitted by the component identities, although the
appended gadget ensures S is a proper subset on actual promised inputs.
No exceptional case needs new original symbols or a changed B or M.

The audit finds no substantive defect or required repair. It establishes
new informal checking evidence for the existing restricted supplier,
not a new theorem, improved bound, certified originality or a resolution
of any general witness-availability premise. The construction and its
direct mathematical inputs are unchanged.

## Mathlib

Full matching theorem coverage is **not checked**; no absence claim is
made. The proof uses finite free-algebra identities, single-order
multilinear injectivity, explicit graph composition and the cited local
constructions. No Lean formalization or machine-checked all-size proof
is claimed. The separate step-376 audit checks its branch-ending/encoding
interface informally and makes no additional Mathlib coverage claim.
