# L084 — Faithful affine-ABP data for the unchanged repeated-square family

## Hypotheses

Use exactly L083's supplied family, indexed by n=2^r, r>=10, with
original CNF F_n=(x_1) AND ... AND (x_n) AND (NOT x_1) and its written
ER refutation pi_n. Its core consists of c_2,...,c_n and n² repeated
self-ANDs s_t, with s_0 the alias c_n. Write H=n²+n−1 and list those
core gates as g_1,...,g_H in their original order. Its other extensions
are a_i iff a_(i−1) AND g_i for i=1,...,H, with a_0 the alias x_1.
Retain all 2H definitions, their ordered operand occurrences, both signs
of every variable, all original-root associations and the unchanged
actual full binary length T=2+|F_n|+|pi_n|. No square or zero product is
removed from that supplied proof or its canonical value DAG.

Use L037's free associative F₂ algebra, affine-edge acyclic ABPs and
complete ordered original-axiom list A(x): clause falsity products,
x_j²+x_j, and x_i x_j+x_j x_i for i<j. Their independent placeholders
are, respectively, the clause placeholders, b_j and c_ij. An empty
accepting path has value one; a zero graph below has distinct endpoints
and no accepting path. Only the data representations may change.

## Conclusion

There is a polynomial-bit-time construction of the complete L037 data
for this unchanged proof, faithful on every original Boolean assignment.
It has an explicitly associated abstract value DAG with

    S=2n+4H+2=O(T),       d=n,       h=2n−1,
    E_ABP <= C(T+2)^4                                      (1)

for one absolute constant C under fixed explicit binary encodings.
The S nodes are the two constants and both signs of every original and
extension variable. Every representative is x-only; originals and
constants are exact, and each signed representative is exactly 1+r_a.
Every extension i, with its actual ordered operands a,b, has an affine
ABP H_i using only original Boolean/commutator placeholders and satisfying
the formal free-algebra identities

    H_i(x,0)=0,        H_i(x,A(x))=r_i+r_a r_b.              (2)

The d,h bounds are before axiom substitution and hold even for the path
degrees of the written graphs. E_ABP charges independently written
representative and relation graphs, every internal factor copy, explicit
diagrams, names, source/root associations, references and a full original
dictionary repeated in every exported graph package. Thus L037 receives
these data and supplies a polynomial-full-bit original-axiom certificate.

This is a reproduction/application of established local diagram and
graph machinery with a family-specific fidelity and encoding argument,
not certified originality. The separate step-327 informal critical audit
below finds no substantive defect in the stated specialization. L083's
structural stop remains valid: this result does not supply its missing
small sets/trees, data for arbitrary ER, formula-length-only bounds,
unavoidable certificate hardness or unrestricted SAT decision/separation.

## Proof

**Approved scope and imported components.** The pre-invocation SPECIALIZE
assessment is `drafts/literature/2026-10-18-repeated-square-alternative-diagram-data.md`.
It covers exactly this family and test. L083 supplies the valid proof,
retained gate list and actual-T ledger; no ER proof is being replaced.
L026 supplies its complete common-order suffix construction, exact-sign
bridge, equations (4)–(12), ordered-multilinear injectivity and formal
local identities. L071 supplies only the post-compilation component in
“Explicit value and earlier-variable graphs”, “Explicit paired-state W
graphs”, “Formal identities, signs and degrees” and its step-274 audited
ledger. Those graph constructions take supplied diagrams and the L026
recurrences as inputs; they use no tree decomposition or Boolean
compiler. Their applicability therefore follows from the diagrams below.
We do not apply L071's whole theorem or omit its treewidth hypothesis.
L037 is used only after verifying its complete receiving premises.

The primary supporting graph-composition construction is Raz–Shpilka,
*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author-hosted 16-page manuscript, Definition 1 and Lemma 2 Step 1,
printed pp.4–5,
[author PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Only its serial/parallel construction underlies the imported component;
the full lemma's zero-free-term/homogeneous conclusions are not invoked.
Bryant, *Graph-Based Algorithms for Boolean Function Manipulation*, IEEE
Trans. Computers 35(8), 677–691 (1986), DOI 10.1109/TC.1986.1676819,
Theorem 1 and sections 4.2–4.3 in the
[author-restored file](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
provide the assessed Boolean graph operations. Here diagrams are written
directly; no reduction/Apply theorem or general free-algebra correction
claim is reproved. The only additional mathematical work is the exact
root description and its reception/accounting on the supplied family.

**All root values, including every accumulator.** Let P_j be the Boolean
conjunction of x_1,...,x_j. All assertions in this paragraph hold on
every original assignment, without assuming any clause of F_n. L083's
core definitions give c_j=P_j and s_t=P_n for every t, since a Boolean
bit AND itself is that bit. Consequently

    g_i=P_(i+1) for 1<=i<=n−1,
    g_i=P_n     for n<=i<=H.                              (3)

We claim a_i=P_min(i+1,n), also for i=0. The base is a_0=x_1=P_1.
For 1<=i<=n−1, the induction hypothesis is a_(i−1)=P_i and (3)
gives g_i=P_(i+1). Their conjunction is P_(i+1), since P_(i+1)
already includes every factor of P_i. At i=n−1 this is P_n.
For every i>=n both the earlier accumulator and g_i equal P_n,
so their conjunction stays P_n. This proves the claim through i=H,
including all n² square operands in the accumulator chain. Negating
any retained root complements its Boolean function. Originals have their
own singleton functions, and constants their field values. These exhaust
the abstract roots; the proof has no nonextension variable absent from F_n.

This semantic description neither identifies vertices nor changes
L083's unsimplified support/path predicate. In particular every square
is still a definition for which (2) must be supplied. Boolean idempotence
does not make its formal defect zero.

**Complete common-order diagrams.** Fix the single order x_1,...,x_n.
For a set A of queried positions, construct levels 1,...,n+1, with
two states ell=0,1 at each level. Start at state 1 of level 1.
At level k<=n, the successor on bit b is the next-level state

    ell*b if k is in A, and ell otherwise.

Label terminal state ell by the bit ell. Induction over processed
positions shows that the current state is the conjunction of the
already read bits at positions in A. Thus this diagram computes
the conjunction on A. Tests outside A have identical successors, and
even unreachable states are explicitly retained. Every edge goes to
the next level, every nonterminal has both successors, and terminal
labels, the single root and dense identifiers are written. The width
is two, including terminal levels; no early termination is used.

Use A={1,...,j} for each root identified with P_j above, and A={j}
for original x_j. Supply a separately associated copy for each retained
root, even when its function equals many others. Constants use complete
width-one redundant-test diagrams with the corresponding terminal bit.
Each negative auxiliary diagram has the same states and transitions as
its positive diagram and complemented terminal labels. It therefore
computes the exact complementary function with unchanged width. All
these diagrams have O(n+1) records each. Writing both signs and both
constants costs O(S(n+1)) records; the common order, original labels,
terminal data and root associations are included in the bit ledger below.

By (3) and the accumulator induction, each output diagram agrees with
the AND of its actual two operand diagrams on every assignment. This
also covers repeated operands; they are still recorded twice in order.
No satisfying-assignment restriction, truth table or semantic promise
test is needed: the preceding explicit induction proves the promise.

**Formal representatives and relations by the existing interface.**
Apply L026's suffix recurrence to these diagrams. Its increasing-word
injectivity shows that a prefix root is formally the ordered word
p_j=x_1...x_j: both this word and the recurrence polynomial belong to
the increasing multilinear subspace and evaluate to P_j. Similarly the
singleton diagram has root x_j and the constant diagrams have their exact
scalars. The actual original/constant graphs are written directly with
these exact values. For each other positive root use the L071 value
graph; for its negative use a disjoint constant-one-plus-value wrapper.
L026's exact-sign bridge identifies this wrapper with the auxiliary
terminal-complemented diagram formally, not just on Boolean inputs.

For each of all 2H extension definitions, receive its two signed operand
diagrams and its independently associated output into the L071 W-graph
component. Its first-edge recurrences are precisely L026 (6)–(8), with
no change in factor order. L026 (9) gives zero at zero placeholders and
the substituted value r_a r_b+P at the operand-root pair. The synchronous
product polynomial P and the output-diagram representative are increasing
multilinear polynomials in the same fixed order. The all-assignment
agreement already proved therefore gives P=r_i by L026's injectivity.
This proves exactly (2). This is an application of the complete existing
suffix identities, not a fresh derivation of them from Boolean equality.

All W labels are originals, b_j or c_ij; no clause, extension or selector
placeholder is introduced. In particular no easy original-clause
certificate is used to fill (2). Coincident successors and repeated
operands retain separate edges as required by the component. Distinct
zero/sum endpoints exclude spurious empty paths. L026's degree bounds
and L071's audited path-degree check give d=n and h=2n−1 before
substitution. Exact originals, scalars and signed wrappers satisfy the
same d. These bounds are independent of the original square-chain
syntactic degree; they concern the newly supplied data only.

**All independent copies and full bits in actual T.** There are n
original and 2H extension variables, so two constants and both signs
give exactly S=2n+4H+2 abstract nodes. Place constants and originals
first, then the core and accumulator definitions in their given order,
with each negative immediately after its positive root. All operands
are earlier, and the original ordered operand/root associations are
retained. There are no extra abstract nodes for internal arithmetic
states. L083's explicit input contains the n originals and at least one
record per extension, so n<=T and 2H<=T. These are lower bounds from the
actual encoding, not an inference from L083's upper bound on T.
Thus S=O(T). Aliases s_0 and a_0 introduce no extra variable or definition.

Specialize the post-compilation ledger to w=2, v=w+2=4 and B=T+n+2:

    R=64(T+n+2)(n+1)^2+n²+1=O((T+2)^3).                  (4)

It bounds all independently copied graph records, not just shared circuit
gates. In detail, all signed/base/value graphs use O(B(n+1)v) records.
Each extension has O((n+1)v²) pair states. Each state's local corrections
use independently copied O((n+1)v)-record factors, so all H graphs use
O(2H(n+1)^2 v³) records. Every internal K or suffix-value factor occurrence
inside every local block is paid here. Pair-to-pair recursion uses edges,
never complete ancestry/path copying. Auxiliary paired-product graphs
add O(2H(n+1)v²), and temporary K templates add O(B(n+1)^2 v).
Together with O(S+n²) alphabet/association records and the explicit
diagrams, all terms fit O(R), since 2H<=T.
No sharing between distinct exported root graphs is credited.

Dense graph/level/state references cost O(log(R+2)) bits each. Each
affine edge has at most two terms, and restored original names, axiom
positions and source associations cost at most O(T) per occurrence.
The imported complete-collection bound is consequently

    O(R(T+log(R+2))+T³).                                  (5)

The full original clause/Boolean/commutator list and dictionary has
O(T³) bits under L037's receiving convention, including unused clause
placeholders. Its one-copy charge is the last term of (5). To pay for
redundant full dictionaries as well, export each of the S representative
graphs and 2H relation graphs with its own complete dictionary. There
are S+2H=O(T) such packages, so all these dictionaries cost O(T^4).
Names/references inside copied local blocks are already included in
O(R(T+log(R+2))); a block is part of its containing complete H graph,
not an implicit external graph or an additional uncharged file. Temporary
templates need no separately exported dictionary and are built from the
explicitly stored alphabet. Retaining the explicitly written diagram
collection and common-order names is covered by (5).

Combining (4)–(5) and the repeated-dictionary charge proves (1), since
log(R+2)=O(log(T+2))=O(T+2). Enumerating the O(T) roots, their O(n)
diagram records, the bounded pair tables, independent graph blocks and
binary dictionary writes takes polynomial bit time in unchanged T.
There is no enumeration of assignments, words, proof ancestry paths or
accepting graph paths. Every symbol of the resulting data is written.

All L037 premises are now met: the supplied proof is valid, abstract
nodes and operands are acyclic and explicitly associated, originals and
constants and complements are exact, (2) is formal with permitted
placeholders, and d,h,E_ABP are supplied polynomial bounds in actual T.
Its conditional assembly may therefore be invoked. This establishes
data on this one family; it says nothing about choosing data for an
arbitrary proof or checking arbitrary circuit identities.

**Relevance and limitations.** Attempts 019–020 concern unrestricted
common-order compilation and arbitrary same-output degree-controlled
conversion. Neither is used here. Attempt 029 and L083 retain the square
chain syntactically, so their support/path obstruction is unaffected by
these different semantic representatives. The present exact target's
continuation test succeeds: all root/sign/accumulator promises, formal
Boolean-only relation identities and paid polynomial full-bit/degree
bounds hold by the indicated inductions and imported components.
The original CNF still has an immediate alternative refutation; no
optimal-certificate lower bound or P-versus-NP claim results. A separate
critical review was pending at construction; the later audit follows.

**Separate critical audit — step 327, 2026-10-18.** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-repeated-square-data-critical-audit.md`.
This audit checks this specialization against L083's actual family and
encoding, L026 (4)–(12), L071's post-compilation graph component and its
step-274 qualifications, and L037's receiving hypotheses. It reuses the
precise supporting citations above, rather than applying Boolean
canonicity as a free-algebra theorem. No new lemma, source theorem or
finite diagnostic is used in place of the all-size checks below.

There are exactly n−1 conjunction gates followed by n² squares in the
core list, so g_(n−1)=c_n and g_n=s_1. For i=1,...,n−1 the accumulator
operands compute P_i and P_(i+1); at i=n the operands both compute P_n,
and this persists through H. Thus (3) and a_i=P_min(i+1,n) include the
boundary indices, the last square and every accumulator. The aliases
a_0 and s_0 contribute no additional definitions. Every assertion is
about arbitrary original assignments, with no use of F_n's contradictory
units. L083 supplies legal fresh definitions and the actual earlier
proof references; the alternative semantic values do not modify them.

For a conjunction on A, after positions 1,...,k the reached state is
the product of the bits in A intersect {1,...,k}. Induction uses exactly
the displayed transition, including the absorbing state 0 and redundant
tests outside A. Hence the terminal gives the required function.
Unreachable states are allowed by L026 and are paid. All roots use the
same n levels; the signed copy changes only terminal labels. L026's
formal sign induction therefore identifies it with the separately
written 1+r wrapper. Original singleton and constant diagrams agree
formally with the exact one-edge/zero representatives, so using those
smaller actual graphs introduces no extra relation premise. The two
constant nodes already give each other's complements. Together with
two signs of each of n+2H variables this verifies the exact S count.

At each definition, L026 receives complete diagrams of both actual
operands, including two occurrences when the operands coincide. Its
P polynomial is increasing multilinear, as is the output-diagram
polynomial. Their Boolean evaluations agree by the all-assignment
induction, so its injectivity bridge identifies these two polynomials.
The unreduced product r_a r_b need not be increasing multilinear and
is not identified with r_i by that bridge. Instead L026 (9) gives its
formal defect as the substituted W. This distinction is essential at
the square gates, whose formal defects need not vanish. The zero-at-zero
identity is independent of Boolean evaluation and follows from the same
imported recurrence. These arguments supply H for all 2H definitions,
with only b_j and c_ij placeholders; none uses a clause placeholder.

The graph component is applicable without its earlier treewidth-based
compiler: L071's value graph has the two transitions of L026 (4), its
K graph switches once from a K region to a value region, and its W graph
either advances a pair level or exits into one ordered local block.
There are no return edges from a block to a pair region. The first-edge
identities are consequently precisely (6) and (8), including parallel
edges for equal successors and zero terminal K/W regions. Disjoint
factor copies preserve the order e_a K_a(v_0+v_1) and
b(u_0+u_1)(v_0+v_1); no commutation is used to build them. The actual
signed wrappers equal the auxiliary signed values formally, so the same
identities receive the prescribed roots. Fresh sinks and the distinct
endpoints of zero graphs exclude an unintended empty accepting path.

Independently of cancellation, a value path over s levels has degree
at most s. An accepting K path uses an affine prefix, one commutator
placeholder and a value suffix, totaling at most s. A W path that
leaves its pair region after n−s levels has a local correction of degree
at most 1+2(s−1), so its full degree is at most n+s−1<=2n−1.
The s=1 K branches have no accepting path; the Boolean block still has
degree at most one. Unit connectors and scalar terminal edges add no
degree. The sign wrapper adds a constant branch. Since n>=2^10, the
exact base graphs and constants also satisfy d=n and h=2n−1 without
any exceptional zero-variable convention.

The actual input explicitly writes n+1 original unit clauses and 6H
definition records. In particular n<=T and 2H<=T hold by record lengths,
without using an upper estimate for T. With v=4, q=4(n+1), and at most
O((n+1)v²) pair states per definition, the constant number of complete
O(q)-record factors at each pair gives O((n+1)²v³) records per H.
Repeated equal factors are charged separately. Summing over all 2H
definitions pays every internal K and suffix occurrence. The other
charges are O(B(n+1)v) for values and diagrams, O(2H(n+1)v²) for P,
O(B(n+1)²v) for optional K templates, and O(B+n²) for framing.
Each is bounded by a constant times R in (4). Pair recursion shares
vertices within one graph; it does not copy a whole continuation per
path. There is no sharing credited between exported root graphs.

Every record contains boundedly many endpoints and affine terms. Dense
references have O(log(R+2)) bits and any restored input name has at most
T bits. Thus graph records cost O(R(T+log(R+2)))=O((T+2)^4).
The original dictionary has n+1 unit-clause entries, n Boolean entries
and n(n−1)/2 commutator entries, all of bounded arity. Its full names,
positions and framing fit the stated conservative O(T³) allowance.
There are exactly S+2H exported representative/relation packages, so
even independently writing this entire dictionary in every package
costs O((S+2H)T³)=O((T+2)^4). Auxiliary P and temporary K graphs are
already paid as records and may reference the explicitly stored common
dictionary; they are not additional promised independent exports.
The construction loops over these bounded records and copies, so its
bit time is polynomial as claimed. No assignment or path enumeration
is concealed in this bound.

Finally F_n has width one, L083's proof uses the allowed width-at-most-
three ER rules, all proof variables are covered, and the abstract order
places each operand before its output and each complement after its
unsigned root. The graphs, exact roots, formal H identities and complete
framing therefore meet all L037 premises. L037 permits this stronger
Boolean-only and faithful specialization but does not establish those
extra properties itself. Its conclusion is polynomial in the supplied
T,S,E, which are polynomial in this family's unchanged T.

No substantive defect, missing hypothesis or bound repair was found.
This verifies a family-specific informal input, not a result beyond the
checked source machinery, certified originality or a P-versus-NP
candidate. Attempts 019–020/029 remain unchanged. General ER data,
formula-length-only certificate bounds and unrestricted SAT transfer
remain open; no new graph dependency is introduced by the audit.

## Mathlib

Matching coverage for this full family-specific data construction is
not checked. No claim of absence, formalization or machine-verified
proof is made. The imported results and this applicability argument are
informal mathematics; no new mathematical script or finite diagnostic
is used as evidence for the all-size conclusion.
