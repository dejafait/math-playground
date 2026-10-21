# L076 — Exact signed-AND data with cost polynomial in T+D

## Hypotheses

Work over the free associative algebra F₂<x>. Let F and pi satisfy L037's
original width-at-most-three CNF and valid signed-AND ER conventions, with
actual binary length T=2+|F|+|pi|. In particular, definitions are fresh and
acyclic, have ordered earlier signed operands, and repeated operands are
allowed. All written variable names, clauses and references are charged.
Use exactly L037's ordered original-clause, Boolean and pair-once
commutator axiom list A, with independent placeholders and no extension
axiom placeholders.

Form the canonical abstract value DAG: one positive node and its signed
node for every distinct proof/formula variable, together with constants
0,1, and no extraneous nodes. Original variables occurring in F retain
their distinct free generators. A nonextension variable absent from F
has positive value zero. A signed node has exact value 1+P; an extension
node has exact ordered value P_a P_b for its designated signed operands.
Include both signs and every unused extension. Topologically number this
DAG, with S nodes. Aliases designate existing nodes and introduce no
extra arithmetic operation.

Assign syntactic degree delta=0 to scalar base nodes, delta=1 to original
generators, delta=delta_a to a signed node and delta=delta_a+delta_b to
an AND node. The absent nonextension variables mapped to zero have
delta=0. Let D be the maximum delta over all these nodes, before any
cancellation or Boolean simplification. Put Q=T+D+2.

Graphs have L037's explicit acyclic affine-edge model, including constant
labels and empty paths when endpoints coincide. Charge separate graph
copies, every signed/root association, original names, and the complete
original-axiom/alphabet dictionary, even if repeated for each graph.

## Conclusion

All representatives and AND relations required by L037 can be constructed
with their exact formal values. Every relation H_i is zero. There are
absolute constants K,K' for a fixed explicit encoding such that their
aggregate full-bit length and deterministic bit construction time obey

    E_ABP <= K Q^4,                 time <= K' Q^12.          (1)

One may take d=max(1,D), h=1. More specifically, all S representatives
have independent formula trees of total node count

    L <= 2 S^2 max(1,D).                                    (2)

The graphs for these representatives and all zero H_i have aggregate
O(S^2(D+1)+T) vertices plus edges. Applying L037 gives an original-axiom
affine ABP C with C(x,0)=0, C(x,A)=1, full binary length
O(Q^32 log(Q+2)), complete pre-substitution degree O(Q^32), and
deterministic construction time polynomial in Q.

This is a syntax-specific sufficient condition: a polynomial bound on D
in actual T gives polynomial L037 data for that promised class.
Exact repeated squaring can have exponential D, as checked below; no
unrestricted degree promise is available from this criterion. This is local progress
under an EXPLORE assessment, classified POTENTIALLY_NEW only in the sense
that the checked comparison supplied no matching theorem. Originality
is not certified. The separate all-size critical audit on 2026-10-17
found no substantive defect; its checks are recorded below. No arbitrary
polynomial-in-T ER data construction, formula-length-only bound, W/V/U premise,
every-certificate hardness or unrestricted SAT conclusion follows.

## Proof

**Scope and imported conversion.** The prior EXPLORE assessment is
`drafts/literature/2026-10-17-signed-and-syntactic-degree-affine-abp-data.md`.
It compares L019's literal-unfolding obstruction and L033/Attempt 020's
general arithmetic-circuit obstruction. The latter uses addition of two
nonconstant polynomials, absent here. Neither is a refutation of the
present T+D-charged syntax. L075 is a family-specific precedent, not a
mathematical premise for the bound below.

Use Ran Raz and Amir Shpilka, *Deterministic Polynomial Identity Testing
in Non Commutative Models*, undated author-hosted 16-page manuscript,
[section 2.1 and Lemma 2 Step 1, PDF pp.4–5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
The inspected scalar/variable, parallel-sum and ordered-serial-product
cases convert a supplied formula tree to a linear-record graph. Only
this pre-homogenization construction is used: it retains constants and
mixed degrees over an arbitrary field, including F₂. We do not invoke
the full lemma's zero-free-term hypothesis or its homogeneous-component
conclusion. Its input must already be a paid tree. The new issue proved
here is that presentation cost and the complete all-root encoding;
the imported conversion is not reproved.

**Degree-zero subgraphs.** Compute all deltas in topological order.
Every ancestor of a degree-zero node also has degree zero: a complement
preserves degree, and a sum of nonnegative operand degrees at a product
is zero only if both are zero. Such an ancestor cannot be an original
generator. Inductively its polynomial is a scalar in F₂. Evaluate these
nodes topologically by scalar complement and scalar multiplication,
obtaining a bit c_i for each degree-zero node i. This evaluation is exact
in the free algebra. It does not test whether a positive-degree node
cancels to a scalar or has a constant Boolean function.

Define a tree P_i for each root independently. If delta_i=0, use the
single scalar leaf c_i. An original generator is its single variable
leaf. At a positive-degree signed node use the binary tree 1+P_a. At a
positive-degree AND use the ordered binary product P_a P_b, making a
separate child occurrence even when a=b. Any degree-zero child is the
single precomputed scalar leaf. Acyclicity makes the recursion finite.
Induction on the abstract order proves that each P_i is the identical
formal value at i. We retain a product by scalar zero or one, and retain
all positive-degree complements, even where further simplification is
possible. No commutation, distributive word expansion, Boolean
idempotence, or semantic-degree estimate occurs.

**Positive-occurrence bound.** Fix a root of positive degree d. In its
tree delete the newly inserted scalar leaves, leaving the skeleton of
occurrences of positive-degree abstract nodes. A signed occurrence has
one child. A product occurrence has one or two children according as
one or both original operands have positive degree. There is always at
least one such child. The leaves are exactly original-variable
occurrences. Labels keep the original deltas: at a unary node the child
has the same delta, at a binary node the two child deltas add, and a
leaf has delta one. Induction on this finite tree therefore gives
exactly d leaves. This counts occurrences, including repeated operands
and shared ancestors copied in different branches.

Every skeleton root-to-leaf path follows strictly decreasing abstract
indices, so contains at most S nodes. Count pairs (v,l) where v is a
skeleton occurrence and l is a descendant leaf. Every occurrence has
at least one descendant leaf. Consequently, writing A_i for the number
of skeleton occurrences,

    A_i <= sum_leaves l (# ancestors of l, including l)
        <= S d.                                             (3)

Restore the scalar leaves. Each signed node restores one constant-one
leaf; each product with just one positive operand restores one scalar
leaf; a product with two positive operands restores none. Original
leaves restore none. Thus there is at most one restored scalar leaf
per positive occurrence, and |P_i|<=2A_i<=2S d. A degree-zero root has
size one. Summing the bound 2S max(1,delta_i) over every one of the S
roots proves (2). In particular, D=0 gives S scalar trees and is covered.
Long complement chains spend their actual S nodes in (3); repeated
products spend their two degrees. Nothing is bounded in terms of
post-cancellation degree.

**Graphs and all receiving identities.** Apply the cited conversion to
each P_i separately, with disjoint occurrences and distinct terminals.
Its distinct-terminal implementation uses at most 2L vertices and 4L
edges in total: scalar/variable leaves have two vertices and at most
one edge, sums add two terminals and four constant-one connectors,
and ordered products use one serial connector. This is record
accounting for the imported construction. No path homogenization or
unfolding of accepting paths is needed. Zero leaves may have no edge;
all labels are scalar or a single original symbol, hence affine.

For each AND node supply a separate graph with two distinct isolated
vertices as H_i. It has no accepting path and polynomial zero, rather
than a spurious empty-path one. If q is the number of AND nodes, this
adds 2q vertices and the complete endpoint/root records. Exact formal
values give

    H_i(x,0)=0,
    H_i(x,A)=0=r_i+r_a r_b.

Both signs, unused roots, constants and absent nonextension variables
have all been supplied. Copying and collapsing scalar subgraphs cannot
increase internal syntactic degree: each P_i has precisely delta_i by
the same recursive degree rule. Thus all representative polynomials
have degree at most d=max(1,D); the zero relations meet h=1. The original
axiom list and independent placeholders are unchanged, including unused
clause placeholders. No optional prescribed pair, Boolean or
defining-clause witness output is claimed. These are every supplied-data
promise in L037.

**Actual input and full-bit ledger.** The number v of distinct variables
in F and pi, the number n of original variables occurring in F, the
number q of definitions and the number of original clauses are all at
most T: each has an actual written nonempty occurrence. This assertion
uses distinct occurring names, not the numeric value of the largest
name. Hence S=2v+2<=2T+2. Dense topological node indices and root
associations have O(T log(T+2)) bits apart from names. Each original
name is at most T bits, and retaining every name in every association
would still cost O(T^2). No assumption of small original numeric names
is made.

By (2), representative-plus-H graph records number

    R=O(S^2(D+1)+T)=O(Q^3).                                 (4)

Dense local vertex indices, symbol positions, endpoints, edge counts
and list framing have O(log(Q+2)) bits per record. Edges use dictionary
positions; actual original names are retained in the copied dictionary.
The axiom list has at most T original-clause entries, n Boolean entries
and n(n-1)/2 commutator entries. Each polynomial has a constant-size
tree because F has width at most three. With actual original names of
at most T bits, even direct repeated spelling costs O((T+2)^3) bits
for one entire axiom/alphabet dictionary. Placeholders can be named by
their actual axiom-list position, with O(log(T+2))-bit indices. The
original name map, ordered clause factors, all constants, empty clauses
and unused placeholder entries are included in this bound.

Repeat this complete framing for every one of S+q=O(T+2) separately
written graphs. Its total cost is O((T+2)^4). Graph records and all
associations therefore give

    E_ABP=O(Q^3 log(Q+2)+(T+2)^4)=O(Q^4),                    (5)

since Q>=4. Reusing a dictionary or an identical root is unnecessary
for this upper bound. Independently copied formulas, both signs,
repeated operands and every zero graph have already been charged.

**Bit construction time.** Topological degree computation uses integers
of at most S+1 bits: the running maximum delta at most doubles at each
new node, starting at most one, so D<=2^S. Scalar evaluation uses one
bit per degree-zero node. These tables are polynomial in actual T,
even when D is large. An explicit stack traversal writes each paid
formula occurrence once, with depth at most S and an abstract index
per stack entry. Across roots it visits O(L) occurrences. The cited
conversion, root/endpoint renumbering and dictionary copying enumerate
only the records already bounded in (4)–(5). They require no polynomial
identity testing, word/path enumeration, assignment enumeration or
search for witnesses.

For a deliberately loose sequential bit-machine bound, there are
O(Q^4) elementary list/stack/record actions including copying dictionary
bits. All stored trees, graphs, tables, stacks and framing occupy
O(Q^4) bits; counters and degrees fit O(Q) bits. Implementing each action
by a full scan of this storage and ordinary quadratic-time integer
arithmetic costs at most O(Q^8) bit operations per action. Thus
O(Q^12) bit time suffices for the entire data construction. This generous
bound avoids a unit-cost random-access or long-integer assumption.
The parameter is numeric D, not its binary length; no polynomial-time
claim in T+log(D+2) is made.

**Receiver, tests and limitations.** All L037 hypotheses now hold with
S=O(T), E_ABP=O(Q^4), d=max(1,D), h=1. In its notation
N=2+T+S+E_ABP=O(Q^4). Its conclusion gives the asserted size, degree,
construction time and both formal IPS identities. Only L037 is used
as a local mathematical input to this final application.

The proof treats D=0, empty original-variable lists, constants zero and
one, arbitrary signs, long unary chains, shared/repeated operands and
all unused roots uniformly. The relevant all-size check is the exact
leaf conservation and ancestor-incidence count (3), together with the
complete ledger (5); no finite diagnostic or mathematical script is
offered as proof. In particular a product with a degree-zero zero
operand can still have large syntactic degree, which is retained here.
Allowing arbitrary nonconstant addition would break leaf conservation
and is outside the hypotheses, as in L033. Attempts 016/020 and the
family-specific result L075 remain intact. Arbitrary ER still lacks an
alternative general polynomial-in-T data construction; independent
certificate-existence, formula-only and SAT gaps remain.

As a boundary check on the required threshold, start with original
opposing units (x),(NOT x), insert definitions z_1 iff x AND x and
z_i iff z_(i-1) AND z_(i-1) for 2<=i<=m, then resolve the original units.
This is a valid ER refutation; its unused definitions are explicitly
included as required here. With dense names and references its full
binary length is O((m+2)log(m+2)). The exact value of z_i is the formal
word x^(2^i), and its syntactic degree is 2^i by the defining sum rule.
Thus D=2^m (also for the complements), exceeding every fixed polynomial
in this T. Our bound charges this D and does not imply a polynomial-in-T
conclusion on this boundary family. This test neither lower-bounds
alternative reduced data nor its easy original-clause certificate.

**Independent critical audit, 2026-10-17: scalar collapse and occurrences.**
The audit uses the prior EXPLORE assessment
`drafts/literature/2026-10-17-signed-and-degree-data-audit.md` and reuses
the inspected conversion above. Its verdict is confined to this exact
syntax and to numeric D. A degree-zero product has two degree-zero
operands, and a degree-zero signed node has a degree-zero operand.
Following dependency edges therefore never reaches a free generator.
Topological scalar evaluation is a formal induction, including absent
nonextension variables assigned zero; it assumes no Boolean identities.
Replacing each such occurrence by its scalar leaves the root polynomial
unchanged. A positive-degree product with a scalar-zero operand is not
collapsed: its other operand still contributes its full syntactic degree
and its full occurrence tree. A positive-degree polynomial cancelling to
zero receives the same treatment. Thus no semantic test is hidden here.

In the resulting positive skeleton, the only possible terminal is an
original-generator occurrence. A positive signed node has a positive
child; a positive product has at least one positive child, and cannot be
a terminal. If a product has one positive child, its degree equals that
child's degree; if it has two, their degrees add. Induction, with value
one at each leaf, proves exactly delta_i leaves for root i, even when
two child occurrences have the same abstract index. Each skeleton
occurrence has a descendant leaf. Counting its incidences with all such
leaves bounds the number of occurrences by the sum of the lengths of
the root-to-leaf paths. Every individual path strictly decreases the
abstract index, so its node count is at most S; repetition across
different paths is paid separately. This establishes (3), without a
fan-out bound or a bound on the number of abstract paths. Restoring
scalar children adds at most one leaf per positive occurrence. Summing
over all S independently written roots gives (2), including the S
one-leaf trees when D=0. No sign or unused root is removed from this sum.

**Independent audit: graph and receiver promises.** The imported
scalar/variable and serial/parallel conversion receives precisely the
paid trees, including mixed degrees and constants. For its stated
distinct-terminal implementation, a leaf introduces two vertices and
at most one edge, a sum introduces two vertices and four connectors,
and a product introduces one connector and no additional vertex.
Charging these contributions to their respective formula occurrences
gives at most 2L vertices and 4L edges. The disjoint child copies retain
both occurrences of repeated operands. No homogeneous-component theorem
or zero-free-term premise is used. Every label is scalar or an original
symbol. A zero representative and each zero H use distinct endpoints
with no connecting path, so the empty-path convention cannot create 1.

The original generators and constants are exact; each signed root is
formally 1 plus its positive root; each ordered extension root is
formally the product of its designated signed operands. Consequently
each separately supplied H has both required identities, with
r_i+r_a r_b=0 in characteristic two before any axiom substitution.
Unused definitions satisfy the same identities. All representatives
are x-only, and the complete original axiom list supplies precisely
L037's independent placeholders, with no extension placeholders. The
syntactic-degree induction bounds the formal polynomial degrees needed
in L025/L037, including cancellation and zero polynomials; d=max(1,D)
and h=1 also meet the receiver's lower bounds when D=0. The explicit
canonical numbering supplies S=2v+2 nodes without adding internal
formula or graph vertices to that abstract node count. These checks
discharge the inherited promises; the previously audited L037 assembly
is applied, not assumed to construct its own input data.

**Independent audit: full bits, time and specialization.** Each distinct
variable or definition is explicitly written somewhere in F or pi, so
v,q,n<=T even for unused definitions and very long names. Equation (2)
and the independent H endpoints give O(T²(D+1)+T)=O(Q³) graph records.
References into these finite graphs have O(log(Q+2)) bits. Actual names
are not substituted by their numeric magnitudes: their written strings
are retained, with length at most T each. One complete original axiom
dictionary has O(T²) constant-size polynomial entries, each costing
O(T+log(T+2)) bits even with direct name repetition. Repeating that
O((T+2)³)-bit dictionary for all S+q=O(T+2) graphs gives O((T+2)^4)
bits. Abstract associations, signs, endpoints, unused placeholders and
counts fit the same allowance. Since log(Q+2)=O(Q), this verifies (5)
with its displayed exponent four, rather than merely some polynomial.

For time, the degree recurrence starts at zero or one and at most
doubles its current maximum per abstract node, so each stored degree
uses at most S+1 bits. Scalar evaluation visits only the degree-zero
nodes after these tables are known. Stack traversal stops immediately
at every collapsed scalar occurrence and otherwise visits only the
paid formula nodes; its depth is at most S. The conversion and reference
backpatching use a bounded number of list operations per output record.
Input parsing, name comparison/dense indexing and topological ordering
can be implemented with polynomially many naive scans in T, within
O(Q^4) outer operations; writing the repeated dictionary bits also fits
that operation count. Trees, stacks, degree tables, reference tables and
the complete output fit O(Q^4) bits: even spelling a T-bit name at every
formula leaf fits this bound. Each operation can scan that storage and
perform ordinary integer arithmetic; O(Q^8) bit operations per outer
operation is a conservative allowance. Thus the stated O(Q^12) time
bound is valid on a sequential bit machine and uses no unit-cost large
integer or random-access assumption. It is not polynomial in log D.

Finally N=2+T+S+E_ABP=O(Q^4) in L037. Its O(N^8 log(N+2)) full bits
become O(Q^32 log(Q+2)); its O(N^8) complete pre-substitution degree
becomes O(Q^32), and its polynomial bit time remains polynomial in Q.
This application imports both final identities, not just their Boolean
evaluations. No hidden d or h factor is required by L037's conclusion.
The repeated-squaring boundary example retains D=2^m while T is
O((m+2)log(m+2)); unused definitions are explicitly allowed here. It
therefore continues to defeat any inference of a polynomial-in-T bound
from this criterion alone. The audit establishes reliability of this
local sufficient condition, not new data for arbitrary ER, a stronger
representation theorem, certified originality or a SAT consequence.
No mathematical script or finite experiment is needed for these
all-size checks. No substantive defect or changed exponent was found.

## Mathlib

Full matching theorem and supporting coverage not checked. No assertion
of absence is made. The external conversion is imported by the precise
primary citation above; the occurrence and full-bit specialization is
proved informally here. The separate informal audit above is complete;
no Lean formalization has been completed.
