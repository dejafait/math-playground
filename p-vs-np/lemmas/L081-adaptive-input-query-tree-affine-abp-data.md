# L081 — Supplied adaptive input-query trees give affine-ABP data

## Hypotheses

Work over the free associative F₂ algebra, with L037's valid supplied
signed-AND ER refutation pi of the width-at-most-three original CNF F.
Put T=2+|F|+|pi|, including all binary names and references. Keep the
ordered original axiom list A: clause falsity products, Boolean axioms
x_j²+x_j, and pair-once commutators x_j x_q+x_q x_j. Their placeholders
are independent. The n≤T originals occur in F; nonextension proof
variables absent from F have positive value zero. Keep the full canonical
acyclic signed value DAG G, including constants, both signs, ordered and
repeated operand occurrences, and unused definitions.

Supply an explicitly encoded finite rooted binary tree of full bit length
B. Each internal node queries an original input and has both children,
labeled 0 and 1. No input is queried twice on a root-to-leaf path. There
is no global query-order or logarithmic-depth assumption. Let Lambda be
its leaves, M=|Lambda|, and D its maximum query depth. Thus M≤B+1 and
D≤n. The input is a tree, not a compressed DAG with implicit paths.

For each leaf lambda let alpha_lambda be its path assignment. Replace
each occurrence of a queried original input in G by its assigned scalar
leaf, retain its own scalar root association, and retain every other
node and operand position. In particular signs are still complemented
and products by zero are not simplified. Call this G_lambda. Compute
syntactic supports by singleton remaining originals, empty scalar/absent
bases, inheritance at signs and union at ANDs. With the unchanged
k=floor(log₂(T+2)), assume that every ancestry path from every root of
every G_lambda contains at most k ANDs whose two actual operand supports
both have size greater than k. No restricted ER refutation is supplied
or assumed. The residuals can be reconstructed from G and the tree;
their separate descriptions need not be part of B.

## Conclusion

There is a deterministic construction of all L037 data for the unchanged
F, pi and A: S=O(T), exact originals/constants, exact signed wrappers,
Boolean-faithful x-only affine ABPs r_v, and one affine ABP H_i for every
definition i iff a AND b, with the formal identities

    H_i(x,0)=0,       H_i(x,A(x))=r_i+r_a r_b.              (1)

Only original Boolean and commutator placeholders occur in H_i. Let
S_*=max_lambda |V(G_lambda)|=O(T), and set

    d=max(1, D+(S_* 2^k+1)(k+1)),
    h=max(1, max_i |E(H_i)|),                            (2)

where the empty maximum is zero. These bound pre-substitution degrees.
For absolute fixed constants C,K,b with b≥8, put

    p(T)=C(T+2)^16,       R=2+T+B+p(T).

Complete aggregate data length E_ABP and h are at most KR^8; construction
bit time is at most KR^b. In particular one fixed polynomial in T+B,
after increasing its constant, bounds E_ABP, d, h and construction time
simultaneously. All independent copies, signs, unused roots, source
associations, names and complete repeated original dictionaries are paid.
L037 then gives an original-axiom affine-ABP certificate polynomial in
T+B. A bound solely in T additionally requires B polynomial in T.

This is an informal restricted sufficiency result, not a main-problem
candidate. The separate step-314 critical audit below finds no substantive
defect and changes no hypothesis or bound. POTENTIALLY_NEW means that
the prior comparison found no inspected full-statement match; originality
is not certified. No small adaptive tree or finder for arbitrary ER,
formula-only certificate bound, W/V/U, or unrestricted SAT consequence
is established.

## Proof

**Coverage and imported components.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-adaptive-input-query-tree-data.md`.
Adaptive Boolean query trees are established representations: Darwiche
and Marquis, *A Knowledge Compilation Map*, JAIR 17 (2002), Definitions
2.6–2.10, pp.232–233 and Proposition 5.1's conditioning case, p.256
([published paper](https://www.cs.cmu.edu/afs/cs.cmu.edu/project/jair/pub/volume17/darwiche02a.pdf));
Ordyniak, Schidler and Szeider, *Backdoor DNFs*, JCSS 144 (2024), 103547,
sections 2.3–3, pp.3–4
([published paper](https://eprints.whiterose.ac.uk/id/eprint/213187/7/1-s2.0-S0022000024000424-main%20%281%29.pdf)).
Their Boolean definitions/conditioning do not supply (1).

Import the already audited circuit-only leaf component of L080 and the
formal ordered recombination component of L072 after proving its input
identities below. Use L035 for arbitrary x-only graph commutators.
Its edge-label specialization supplies the adjacent-literal exchange
used below. This is also the constant-size literal case of Li, Tzameret
and Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, arXiv:1412.8746v4, 11 September 2015, Lemmas 3.6–3.7,
pp.17–18 ([paper](https://arxiv.org/pdf/1412.8746v4)). No reproof or
generalization of that formula theorem is needed. Writing the specialized
literal seed makes its exact placeholder position and copying cost
explicit. Already paid formula trees and disjoint graph sums/products
use Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non
Commutative Models*, 16-page author manuscript, Definition 1 and Lemma 2
Step 1, pp.4–5
([manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)).
Only that component, including constants and mixed degree, is imported;
its later homogeneous conversion is not used.

The additional argument is the adaptive exact interpolation, the paid
sequence of literal corrections, and its reception by the existing
components. Attempts 019–020 stop universal common-order width and
degree-only identical-output conversion, respectively; neither premise
is used. No arbitrary FBDD conjunction, Boolean-zero witness theorem or
enumeration of assignments to the union of queried inputs is assumed.

**Leaf reception at the original cutoff.** For a fixed lambda, its
queried set can have any size up to n, rather than L080's logarithmic
deletion-set bound. Apply only L080's proof component “Circuit-only
reception at the original cutoff”, not its whole fixed-set theorem.
Here is why this change is allowed for that component. There are O(T)
operand occurrences, so replacing them by scalar leaves and retaining
all root associations gives O(T) nodes even with n queried inputs.
The source order is still acyclic; all signs retain their actual scalar
predecessors. There are n'≤n≤T unqueried originals. The counted-path
promise uses the same k, and 2^k≤T+2 still holds. These are exactly the
node, variable, table-size and occurrence-budget bounds used by that
component. Its per-leaf construction does not enumerate assignments
to the queried set or use its cardinality bound. That bound was used
only to enumerate all fixed-set branches later in L080.

Specifically, the component's small-support tables use at most 2^k
assignments each, while its large-root occurrence trees have at most
S_* 2^k occurrences before small attachments. The resulting paid
value trees have path degree at most

    d_0=(S_* 2^k+1)(k+1).

Its formal small-output witnesses use complete diagrams in an order on
the unqueried variables of this leaf, with the identical ordered roots;
large-output definitions retain their exact product and have zero
defect. This description identifies the imported component, not a new
claim that arbitrary Boolean-equivalent roots are formally identical.
For n'=0 all branch roots are scalars and all local witnesses are zero.
The alphabet inclusion retains original names and maps each remaining
Boolean/pair placeholder to its unchanged full-A position. No clause
placeholder is needed. It commutes with both zero and A substitution.

Consequently that component supplies, for every root including signs
and unused definitions, explicit branch graphs f_(v,lambda), J_(i,lambda)
such that

    J_(i,lambda)(x,0)=0,
    J_(i,lambda)(x,A)=f_(i,lambda)
                        +f_(a,lambda) f_(b,lambda).       (3)

An original x_j has branch root alpha_lambda(j) if queried and x_j
otherwise; constants/absent bases are their prescribed scalars and
signed roots are exactly 1+f. Each root is faithful on every completion
of the leaf assignment. L080's per-leaf ledger bounds all these graphs,
repeated full dictionaries, construction and promise checking by
p(T)=C(T+2)^16, uniformly in lambda. The cost of extracting a path from
the supplied tree is accounted for separately below. This receives
circuit data, never a putative restricted refutation.

**Path-ordered partition and exact interpolation.** Write
l_(j,0)=1+x_j and l_(j,1)=x_j. Define e_lambda as the product of the
path literals in their actual root-to-leaf query order; the empty
product is 1. They have path graphs of at most D affine edges.

For any tree node u, let e_(u,lambda) be the product from u down to a
descendant leaf, excluding the prefix above u. Let Z_u be their sum.
At a leaf Z_u=1. If u queries j, induction gives

    Z_u=(1+x_j)Z_(u,0)+x_j Z_(u,1)=1.

This is a formal identity by distributivity; no commutation is involved.
In particular sum_lambda e_lambda=1.

Fix an original x_q. In a subtree with prefix assignment sigma, form
the analogous sum of e_(u,lambda) times the branch root for x_q on the
right. It is sigma(q) if q is fixed in sigma, and x_q otherwise.
Prove this by induction. At a leaf the assertion is exactly the branch
root definition. If q is already fixed above u, the no-repeat promise
prevents querying it again, and both child sums are the same scalar c;
(1+x_j)c+x_j c=c. If q is not fixed and j≠q, both child sums are x_q,
so (1+x_j)x_q+x_j x_q=x_q without interchanging letters. If j=q, the
two child sums are the scalars 0 and 1, giving (1+x_q)0+x_q 1=x_q.
These exhaust all cases, including subtrees that never query q.
At the root we therefore have the exact identities

    sum_lambda e_lambda=1,
    sum_lambda e_lambda f_(q,lambda)=x_q.               (4)

Constants follow by multiplying the first identity on the right.
For positive extensions define r_v=sum_lambda e_lambda f_(v,lambda)
using independent graph copies. Write originals/constants with their
exact required roots and signed nodes as the actual wrapper 1+r_v.
Equation (4) and

    sum_lambda e_lambda(1+f_(v,lambda))
       =1+sum_lambda e_lambda f_(v,lambda)

show that every written root, including signed operands, equals its
interpolant formally. On every Boolean assignment exactly one tree
path is selected, so the representatives are faithful. Every accepting
path in an interpolant has degree at most D+d_0; constants/sign wrappers
preserve (2). Branch values need not be multilinear or in a common order.

**Explicit pair corrections in path order.** Denote the Boolean
placeholder for x_j by beta_j and its pair-once commutator placeholder
by tau_(j,q)=tau_(q,j), for j≠q. The imported literal exchange has seed
tau_(j,q) for either signs of the two literals: at A it equals
l_(j,a)l_(q,b)+l_(q,b)l_(j,a), and at zero it vanishes.
This is precisely L035's edge-label specialization (constant terms
cancel). Thus a swap of adjacent distinct-variable literals in a word
P l_(j,a) l_(q,b) R has correction P tau_(j,q) R, with the actual
prefix/suffix retained. No prefix or suffix is commuted.

The necessary Boolean specializations are, for both signs,

    l_(j,a)^2+l_(j,a)=x_j²+x_j,
    l_(j,0)l_(j,1)=l_(j,1)l_(j,0)=x_j²+x_j.           (5)

They follow by expanding the one affine literal, so beta_j corrects
either a square contraction to that literal or an opposite pair to zero.
Inside a word the correction is P beta_j R. These explicit seeds are
needed for the exact signs and target words, not for a general
Boolean-zero inference.

For lambda≠mu take their first branching node, querying j. Their words
are P l_(j,a) U and P l_(j,1-a) V. Move the second j-literal left across
U P, one adjacent exchange at a time. Every crossed literal has an
index different from j, since neither path repeats j. The final word is

    P l_(j,a) l_(j,1-a) U P V.

Correct its opposite pair to zero using P beta_j U P V. Sum this
correction and all the swap corrections, each with its own actual
intermediate prefix/suffix. The substituted sums telescope: each
intermediate word occurs exactly twice, leaving e_lambda e_mu. At
zero placeholders every summand vanishes. There are at most 2n swaps,
and no factor lists are expanded into monomials.

For lambda=mu write e=l_1...l_s in its own path order. Start with e e.
For q=1,...,s maintain the word

    l_1...l_(q-1) (l_q...l_s)(l_q...l_s).

Move the second l_q left across l_(q+1)...l_s, paying s-q swaps,
then contract the now adjacent l_q² to l_q using (5) in its current
context. This gives the invariant for q+1. All swaps have distinct
indices. After s(s-1)/2 swaps and s contractions the word is the
original path-ordered e, not a canonically reordered substitute.
The sum of corrections therefore specializes to e²+e and vanishes
at zero. For s=0 set Q=0, since 1²+1=0.

In both cases call the resulting graph Q_(lambda,mu). We have proved

    Q_(lambda,mu)(x,0)=0,
    Q_(lambda,mu)(x,A)=e_lambda e_mu
                                  +delta_(lambda,mu)e_lambda. (6)

Each summand has one placeholder and at most 2n-2 literal factors.
There are O((n+1)^2) summands, each a paid path of O(n+1) records.
Fresh endpoints and unit connectors give O((n+1)^3) records per Q,
and pre-substitution degree at most max(1,2n-1). Sum/product graph
composition preserves the exact contextual products. Keeping full
copies and the full A dictionary costs O((T+2)^4) bits per Q. Explicit
list updates and copying are polynomial (even naive scans fit p(T));
no path enumeration of an arithmetic graph or truth-table test occurs.

**Reception by ordered recombination.** For a definition i iff a AND b,
put a_lambda=f_(a,lambda), b_mu=f_(b,mu). L035, applied only to the
x-only graphs a_lambda and e_mu, constructs C_(lambda,mu) with zero
at zero and substituted value a_lambda e_mu+e_mu a_lambda. Use the
unchanged L072 ordered recombination:

    H_i=sum_lambda e_lambda J_(i,lambda)
        +sum_(lambda,mu) [e_lambda C_(lambda,mu)b_mu
                             +Q_(lambda,mu)a_lambda b_mu]. (7)

All factors are independently copied in the displayed order. Every
summand contains a zero-at-zero J, C or Q, proving the first part of
(1). For completeness the exact reception calculation is as follows.
At A the two double-sum contributions are

    e_lambda a_lambda e_mu b_mu
                       +e_lambda e_mu a_lambda b_mu,
    e_lambda e_mu a_lambda b_mu
                       +delta_(lambda,mu)e_lambda a_lambda b_mu.

The middle ordered terms cancel literally. The remaining sum is
r_a r_b+sum_lambda e_lambda a_lambda b_lambda, by the exact
interpolants. Equation (3) makes the first sum in (7) equal to r_i
plus this same diagonal sum. Thus it cancels and leaves r_i+r_a r_b,
as required. This matches all premises of the imported component;
no indicator-product quotient identity has been used as a free identity.
No witness J, C or Q is an input to L035. Graph factors have disjoint
vertices; serial connectors enter/exit their designated endpoints.
A path cannot leave an exit internally and then return to use a
connector in an acyclic graph. Hence even nonextremal endpoints add no
unintended accepting paths. Zero/scalar graphs and unit products use
fresh outer endpoints. Both signs, repeated operands and unused roots
are covered by the same formulas.

**Complete independent-copy ledger.** Reading the explicit tree,
checking both outcomes/no repeats and extracting all path assignments
is polynomial in T+B. There are M≤B+1 leaves and at most MD≤(B+1)T
written path literals; traversing source names and retaining every
path copy costs polynomially many bits. For each leaf, p(T) covers all
residual, support, value and J records, every original dictionary and
their construction. It also covers one framed indicator or Q, including
its literal-copy algorithm. Retaining all branches and Q templates
costs O(Mp+M²p). Scalar/empty cases are included in p.

Each L035 input pair has full length O(p), including the original
commutator framing. Its output has O(p^4) full bits, and bit time
O(p^a) for one fixed exponent a from that constructor. There are at
most O(TM²) calls, one for each definition and ordered leaf pair.
The M first summands and 2M² correction summands of (7), with every
factor copied, cost O(Mp+M²p^4) per definition. All separately written
unsigned, base and signed representatives cost O(TMp); a signed
root receives a full independent copy of its unsigned representative.
These charges include complete branch operand graphs on every use,
not merely their references. Retaining the whole template collection
does not exceed the same aggregate order O((T+1)M²p^4).

Fresh global references, even with verbatim restoration of original
names, add at most a factor O(T+log(M+2)+log(p+2)) to this bit/record
bound. Complete A costs O(T³); repeating A for all final graphs,
templates and source associations is included in the p-per-copy
charges. As T,M,p≤O(R), the total is at most KR^8 after enlarging K.
No independent output shares storage to earn a size discount. Dense
renumbering and all dictionary writes can be done with naive string
scans in polynomial time in R. The explicit O(TM²) calls cost
O(TM²p^a); choosing a fixed b≥8 sufficiently large for this and the
copy/scan operations gives total bit time KR^b. There is no loop over
2^n or T^D assignments. The only table exponential is 2^k≤T+2 in
the imported per-leaf component.

Every H_i is a finite affine DAG, so a word before substitution has
degree at most the number of edges on its path, bounded by |E(H_i)|.
Thus h in (2) is valid and at most KR^8. The value path bound d is
polynomial in T. Since R≤C'(T+B+2)^16, one fixed polynomial
K'(T+B+2)^(16b), with b enlarged if needed, bounds all four quantities
E_ABP,d,h and bit time. The unchanged abstract DAG has S=O(T), with
no auxiliary arithmetic vertices promoted to extension variables.
All L037 supplied-data hypotheses now hold, proving the conclusion.

**Discriminating cases and limitations.** A singleton unqueried leaf
has e=1, exact bases, Q=0 and the original counted-path leaf supplier.
For an unequal-depth tree querying x, stopping on 0 and querying y on
1, the indicators are 1+x, x(1+y), xy. Their sum is 1 formally; the
y interpolant is (1+x)y+xy=y, while the x interpolant is
x(1+y)+xy=x. An input z queried nowhere has interpolant (sum e)z=z.
Thus a variable queried only in one subtree does not lose its exact root.

For opposite subtree orders, query x first, then y,z on its 0 branch
and z,y on its 1 branch, with both outcomes at every node. Within
either subtree the original y and z interpolants follow (4) in that
subtree's actual order; for example on the latter subtree the y
interpolant reduces to (1+z)y+zy=y. Combining gives exact global roots.
An explicit cross pair e_lambda=(1+x)y(1+z), e_mu=x(1+z)y has correction

    (1+x)y tau_(x,z)(1+z)y
      +(1+x)tau_(x,y)(1+z)(1+z)y
      +beta_x y(1+z)(1+z)y.

The two adjacent swaps and then the opposite-x contraction prove its
substitution is exactly e_lambda e_mu, and every summand vanishes at
zero. A two-factor diagonal e=u v with different indices has correction
u tau_(u,v) v+beta_u v v+u beta_v; here beta/tau denote the placeholders
for the underlying indices regardless of literal signs. Its three
steps leave the original u v. These are symbolic proof cases, not
numerical certificates. The general induction/telescoping arguments
above cover every depth and pair. Scalar-only residuals and unused
definitions are included in (3) and the per-root ledger.

The continuation threshold—both formal identities and one polynomial
in actual T+B—is met by this informal construction. A separate audit
must check the leaf-component specialization, adaptive identities,
complete copying and degree bounds. The tree's existence and size for
arbitrary ER, formula-only bounds and SAT transfer remain independent
gaps. No claim is made that this tree premise evades the old obstructions
on arbitrary proofs. No executable construction or proof strings have
been verified in this step.

**Separate critical audit — step 314, 2026-10-18.** This uses the
pre-existing SPECIALIZE scope in
`drafts/literature/2026-10-18-adaptive-input-query-tree-critical-audit.md`.
The earlier pending-audit statements describe the construction step;
this section supersedes that qualification. Reuse the precise primary
components cited above and the already audited local components. This
is independent informal verification of the restricted construction,
not a new source theorem, certified originality, executable verification
or a resolution candidate.

**Leaf-component audit.** Distinguish the number of queried inputs from
the counted-AND budget k. Replacing up to n originals costs one scalar
leaf per actual outgoing operand occurrence and one per retained original
root association. Bounded fan-in and O(T) source nodes give O(T) such
occurrences even with arbitrary fan-out. Signs retain their predecessor
and therefore complement the assigned scalar correctly. Repeated operands,
isolated roots and unused definitions stay present. Support unions are
not simplified when a product has a zero operand.

The audited circuit-only part of L080 depends on S_*=O(T), n'≤T and
2^k≤T+2, all still valid for every leaf. In that component the support
recurrence is ancestor-monotone, and its maximum-count recurrence is
the indicator of two large operands plus the maximum predecessor count.
The promise here is exactly that recurrence bounded by k at every root.
Small tables have at most 2^k assignments each. The large-node unfolding
has at most 2^k terminal occurrences after suppressing unary nodes and
at most S_*2^k total large occurrences. Its small attachments number
at most S_*2^k+1. Thus the paid value-tree size and d_0 apply unchanged.
No step enumerates assignments to the set queried on this leaf.

For small outputs, the table trees, exact bases and completed diagrams
are increasing multilinear in the same order of the remaining originals.
L080's received L026 injectivity identifies their free polynomials, not
just their Boolean values. Both operands of a small output are small;
the paired P consequently equals that chosen output. The received L071
graph realizes the identical W, with O((n'+1)^2(2^k+2)^3) records per
definition. Large outputs retain the exact ordered product and use zero
J. The letter inclusion into full A preserves names and pair-once
positions and commutes with both substitutions on each generator, hence
on the free algebra. With no remaining variables every node has a scalar
value and zero defect. These checks establish precisely (3), including
signed operands, without a restricted refutation or a whole-theorem
application of L080 with its deleted-set hypothesis removed.

**Exact interpolation audit.** The induction is on actual subtrees,
not on a union of query sets. A leaf contributes 1 to Z_u. At an internal
node, both child partition sums are 1; the literal coefficients sum to
1 in their written left positions. For a fixed original q, if the prefix
has assigned q then both child sums are the same scalar. Otherwise a
query different from q leaves both child sums x_q, including when q is
queried only in one child subtree. Distributivity on the right yields
((1+x_j)+x_j)x_q=x_q. A query of q itself has child sums 0 and 1.
The no-repeat hypothesis is essential to the first case. This proves
the exact original interpolation on all trees, with constants and
signed wrappers following from the exact partition sum. It does not
claim that arbitrary extension interpolants are ordered multilinear.

Faithfulness is a separate scalar-evaluation statement: the unique
consistent root-to-leaf path has indicator 1 and all other leaves have
indicator 0. Its branch value is faithful on that completion. A value
graph path has at most D literal degree plus d_0 branch degree; zero,
constant and sign branches add no larger degree. This checks d in (2).

**All-context pair audit.** Here is an indexed check of the actual
contexts, to exclude a hidden reordering in (6). For distinct leaves
write their product as P a W b V, where a and b are the opposite
j-literals at first divergence and W=UP=w_1...w_r. Every w_h has an
index different from j: the prefix has not queried j and the suffix of
the first path cannot repeat it. Moving b left proceeds with h=r,...,1.
The hth correction is exactly

    P a (w_1...w_(h-1)) tau_(index(w_h),j)
                            (w_(h+1)...w_r) V.

At that stage the two replaced adjacent factors are w_h b. Its
substitution is the current word plus the next word, because the affine
literal signs cancel in their commutator. After all swaps the word is
P a b W V. The final P beta_j W V substitutes to this word, since ab
is x_j²+x_j for either opposite-sign order. Adding the differences
cancels every intermediate word twice and leaves the original product.
No j-containing factor is crossed; other repeated indices in W need
not be distinct from one another. This covers shared nonempty prefixes
and unequal depths. Also r≤2n and the initial total length is at most 2n.

For the diagonal, put L=l_1...l_(q-1) and V=l_(q+1)...l_s at stage q.
The current word is L l_q V l_q V. Moving the second l_q left across V
uses the same contextual rule, with prefix L l_q and trailing suffix V.
All crossed variables differ from that of l_q by pathwise nonrepetition.
The resulting word is L l_q² V V. The contraction L beta_(index(l_q))
V V replaces it by L l_q V V, which is exactly the next invariant.
The final word is the original l_1...l_s. Each swap/contraction therefore
has its actual prefix and suffix, vanishes at zero placeholders, and
telescopes to e²+e at A. The empty word needs zero Q.

At all stages a summand replaces two literals by one placeholder and
has at most 2n−2 other literals. Thus its degree is at most 2n−1 for
nonempty corrections. Off-diagonal pairs need at most 2n+1 summands;
diagonal pairs need s(s−1)/2+s. Independent paths and sum connectors
therefore use O((n+1)^3) records per Q, not exponentially many words.
Each literal name costs at most O(T) bits and the full A dictionary
costs O(T³), giving the claimed O((T+2)^4) bits per framed Q. Direct
word-list scans construct these paths in polynomial time covered by p.

The displayed opposite-order example also checks directly: its two
swaps give in succession
(1+x)y x(1+z)(1+z)y and
(1+x)x y(1+z)(1+z)y, followed by the Boolean contraction. Their three
corrections are exactly those displayed above. For e=u v, the swap,
first-square contraction and second-square contraction give respectively
u tau_(u,v)v, beta_u v v and u beta_v. These are sign-independent
specializations of the all-context proof, not finite evidence in place
of it.

**Receiver audit.** For every call to L035 the two arguments are the
x-only graphs a_lambda and e_mu. Its alphabet and complete commutator
framing are contained in the unchanged original A; adjoining unused
Boolean/clause generators does not change its identities. No J, Q,
recursive H or extension placeholder enters either argument. At zero
substitution every summand of (7) has a whole zero factor. At A the two
middle products are literally the same ordered expression
e_lambda e_mu a_lambda b_mu. Their cancellation leaves the sum for
r_a r_b and the diagonal sum. The latter cancels the identical diagonal
sum from (3), leaving r_i+r_a r_b. The exact base/sign interpolation
just audited licenses each replacement by r, including signed originals
and constants. This verifies both identities separately; Boolean
orthogonality alone would not have sufficed.

Serial copies have disjoint vertices and only forward exterior
connectors. A path that leaves a designated exit within a factor cannot
return there in a DAG; only that exit can reach the next factor.
Coincident endpoints contribute the allowed empty path, and distinct
endpoints with no path contribute zero. Parallel copies, scalar factors,
repeated/complementary operands, empty original clauses and all unused
roots are consequently admitted. A singleton tree has e=1, Q=0 and
the original leaf supplier; its C has zero substituted commutator, as
required. These checks receive L072's recombination only, not its
fixed-set indicator construction or its multilinear degree bound.

**Independent complete ledger audit.** Set U=T+2. Per leaf the audited
component has O(U^4) value records and O(U^6) aggregate J records. Complete
diagrams/templates and source associations fit these counts. O(U) bits
per record and O(U³) dictionaries repeated O(U) times give O(U^7) bits.
O(U^6) indexed operations, each replaced conservatively by an O(U^7)-bit
scan and O(U²) further bit work, give O(U^15) time. Hence the same fixed
p=CU^16 covers the leaf construction even when its path has n queries.

Parsing and checking an explicit B-bit tree and listing each path need
only polynomial work in T+B. There are at most MD≤(B+1)T literal
occurrences in these lists, with O(T) bits per retained source name.
Even naive repeated scans are polynomial and are separate from the
per-leaf bound. All leaf exports cost Mp. All separately constructed Q
templates cost M²p. For each of O(T) definitions and M² ordered pairs,
L035 receives O(p) full bits and returns O(p^4) bits; its polynomial-time
constructor has one fixed exponent a. The independently copied final
relations cost O(TM²p^4), including every C, Q, operand and indicator
occurrence. Separately written unsigned and signed values cost O(TMp);
signed outputs copy their whole unsigned graph. Retaining templates,
source associations and complete dictionaries fits
O((T+1)M²p^4). There is no uncharged recursive use of a generated H.

Renumbering the aggregate needs at most
O(T+log(M+2)+log(p+2)) additional bits per previous record: the total
record count is polynomial in T,M,p, and original names have at most
T bits. This factor is O(R), while T+1, M and p are each O(R).
The exponent sum is 1+2+4+1=8, proving KR^8 for the complete output.
All dictionary writes, dense renumbering and path-list updates can be
implemented using O(R^8) record operations outside the constructors,
each with an O(R^8)-bit storage scan and at most O(R²) further name/index
bit work. Parsing/checking the tree and extracting paths fits this
O(R^18) allowance. The O(TM²) calls cost O(TM²p^a); choosing one fixed
b≥max(18,a+3) therefore gives KR^b time.
Nothing enumerates assignments to the union of queried inputs.

An affine edge contributes degree at most one before substitution;
every path in each H is acyclic. Thus h as its maximum edge count is
valid and bounded by the complete output length. Independently,
d≤D+(S_*2^k+1)(k+1), with a minimum of 1, is polynomial in T.
Since R≤C'(T+B+2)^16, a single enlarged fixed polynomial bounds time,
full bits and both degrees. The exact abstract nodes, all roots, full
framing and both relation identities now meet every L037 hypothesis.
Its final assembly is polynomial in this supplied size, as claimed;
no formula-length-only bound follows.

The audit finds no substantive defect, missing direct mathematical input
or bound repair. The argument and its DAG inputs are unchanged. It
verifies only the restricted supplier with an explicitly paid tree;
tree existence/size or a finder for arbitrary ER, formula-only bounds
and unrestricted SAT decision/separation remain open. No new source
coverage, executable construction or Lean verification is claimed.

## Mathlib

Full matching adaptive-tree data theorem and full-bit graph construction:
**not checked**; no absence claim. Supporting mathematical sources and
their precise component scopes are cited above. The local component
specializations and explicit free-algebra argument constitute the
informal result; they are not a Lean formalization or certified novelty.
