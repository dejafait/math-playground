# L080 — Original-input deletion with counted-path residuals supplies affine-ABP data

## Hypotheses

Use L037's width-at-most-three original CNF F, valid supplied signed-AND
ER refutation pi, and actual full binary length T=2+|F|+|pi|. Definitions
are fresh and acyclic, with actual ordered signed earlier operands;
clauses and inference rules retain L037's conventions. Work in the free
associative F₂ algebra. Keep the unchanged ordered original-clause,
Boolean and pair-once commutator axiom list A(x), with independent
placeholders t. There are n≤T originals occurring in F. Nonextension
proof variables absent from F have positive value zero. Keep the entire
canonical signed value DAG G, including both signs and unused definitions.

Put k=floor(log₂(T+2)). Supply an explicitly named set D of ell original
inputs, where 0≤ell≤k. For each assignment alpha:D→{0,1}, replace each
operand occurrence from D by its assigned scalar leaf, retain every
other gate and operand position, and associate each deleted original's
own root with that scalar. No Boolean simplification is performed. Call
this circuit G_alpha. Distinct replacement occurrences may use distinct
scalar leaves; their values and empty syntactic supports are unchanged.

Compute supports in G_alpha by singleton remaining originals, empty
scalar/absent bases, inheritance at signs, and union at ANDs. An AND is
counted when BOTH actual operand supports have size greater than k.
Assume every source-ancestry path from any root of G_alpha encounters at
most k counted ANDs, for every alpha. This uses the original T and k,
not the size of a restricted proof or a simplified circuit. Operand
multiplicities, signs and unused roots are retained. No restricted ER
proof, branch treewidth bound or common order on large roots is assumed.

## Conclusion

There is a deterministic polynomial-bit-time construction of all L037
data for the unchanged F and pi: an abstract value DAG of size S=O(T),
exact originals/constants and signed wrappers, Boolean-faithful x-only
affine-edge ABPs r_v, and an affine-edge ABP H_i for every definition
i iff a AND b, satisfying the formal identities

    H_i(x,0)=0,           H_i(x,A(x))=r_i+r_a r_b.          (1)

Only original Boolean/commutator placeholders occur in H_i. Put
M=2^ell and S_*=max_alpha |V(G_alpha)|, so S_*=O(T). Valid
pre-substitution degree parameters are

    d=ell+(S_*·2^k+1)(k+1),
    h=max(1, max_i |E(H_i)|),                            (2)

where the empty maximum is zero and edges mean the actual written
affine graph edges. For fixed constants C,K,b, with b≥8, put

    p(T)=C(T+2)^16,        Q=2+T+M+p(T).

C can be chosen uniformly so that the complete aggregate output has
E_ABP≤KQ^8, h≤KQ^8, and construction time at most KQ^b. Since M≤T+2,
these and d are fixed polynomials in the original T. All separately
written graphs, signs, unused roots, operand/root associations, original
names and complete repeated axiom dictionaries are charged. L037 then
supplies a polynomial-full-bit original-axiom affine-ABP certificate.

This is an informal restricted sufficiency result. The separate step-310
critical audit below finds no substantive defect and changes no hypothesis
or bound. POTENTIALLY_NEW under the prior SPECIALIZE assessment
means only that no inspected full-statement match was established; it
does not certify originality. No small set D for arbitrary ER is supplied.
Formula-only bounds, W/V/U, every-certificate hardness and unrestricted
SAT decision/separation remain open. This is not a main-problem candidate.

## Proof

**Source use and scope.** The pre-invocation assessment is
`drafts/literature/2026-10-18-input-deletion-large-branch-depth-data.md`.
Reuse L079's audited value-DAG/table/unfolding and local-relation
components, L072's audited indicator and ordered recombination
component, L026's ordered-multilinear identities, L071's post-compilation
affine graphs and L035's arbitrary-affine-graph commutator witnesses.
Neither the whole L079 theorem with a new proof-length cutoff nor the
whole residual-treewidth-two theorem L072 is invoked here. Their precise
component reception is justified below. L037 is used only after all its
supplied-data hypotheses have been established.

The small-table representation input is Randal E. Bryant,
*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE TC
C-35(8) (1986), 677–691, author-restored §1 equation (1), §2 Definitions
1–2, PDF pp.3–4
([manuscript](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf)).
For paid trees and disjoint graph composition use Ran Raz and Amir
Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative
Models*, undated 16-page author manuscript, §2.1 and Lemma 2 Step 1,
PDF pp.4–5
([manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)).
Only its leaf, parallel-sum and ordered-serial-product construction is
used; the later homogeneous conversion's zero-free-term hypothesis is
not being applied. The formal commutator interface is the audited L035,
not an extension of the formula-input hypotheses of Li–Tzameret–Wang,
arXiv:1412.8746v4, Lemma 3.7, p.18
([paper](https://arxiv.org/pdf/1412.8746v4)). These source operations are
imported, not reproved. Boolean conditioning alone would not prove (1).

**Circuit-only reception at the original cutoff.** Fix alpha. Replace
each occurrence of a deleted input by a fresh scalar leaf with that
bit, and give its own root association an isolated scalar leaf. Keep
all other original, absent-variable, constant, sign and extension nodes.
There are O(T) operand occurrences, so G_alpha has O(T) nodes and wires,
uniformly in alpha. Its source order is acyclic. Induction in that order
shows that every associated root has exactly the original Boolean value
under the restriction alpha. No inference of pi is restricted or used
to establish this fact. Its only variable inputs are the n'=n−ell
undeleted originals. Replacement leaves have empty support even when
their scalar is zero; products by zero are not simplified away.

L079's component proof uses only this signed Boolean DAG, the local
AND equations, syntactic supports, an upper bound on its node count,
and a fixed cutoff/branch budget. Its dependence induction, occurrence
count and local diagram identities use no ER inference and no original
clause polynomial. In particular the use of T in those components is
only to bound node/name counts and 2^k; the recurrences do not define a
new cutoff from a new encoding. Here |V(G_alpha)|≤S_*=O(T), n'≤T and
2^k≤T+2 meet those same numerical requirements. We check the remaining
component hypotheses explicitly.

Supports are ancestor-monotone. Thus every predecessor of a small node
(support size at most k) is small. Computing maximum counted-path depth
uses zero at bases, inheritance at signs and, at each AND,

    b(i)=1_{|U_a|>k and |U_b|>k}+max(b(a),b(b)).          (3)

The supplied promise is exactly max b≤k, including unused roots.
Every remaining original is small. Choose the order on the undeleted
originals inherited from one fixed order of all originals. For each
small positive extension evaluate its support table on at most 2^k
assignments. Agreement on a syntactic support implies agreement of that
root by topological dependence induction, so zero-filling the other
remaining inputs gives its correct table under all completions. Keep
alpha fixed throughout this evaluation. The paid complete Shannon tree
from L079 has size 8·2^m−7 and degree at most m for support size m≤k;
empty support gives a scalar. Exact originals/scalars and exact sign
wrappers are retained. Each small root therefore has a paid tree of
size at most 10·2^k and degree at most k.

At every large positive extension choose its exact ordered product of
the already chosen operand representatives. At signs use 1 plus the
underlying representative. Unfold a root only until reaching small
nodes, copying every occurrence separately. In its large-node tree a
two-child vertex is exactly a counted AND. L079's occurrence argument
applies: suppress unary vertices to bound leaves by 2^k, and use at most
S_* source vertices per root-to-leaf path to bound large occurrences by
S_*·2^k. With a AND occurrences and z sign occurrences, the tree has
a+z vertices, 2a+z slots and a+z−1 internal edges. Hence it has a+1
small attachments, at most S_*·2^k+1. The resulting tree has at most
12(S_*+1)2^(2k) nodes and degree at most

    d_0=(S_*·2^k+1)(k+1).                              (4)

The harmless factor k+1 covers all bases and scalar/sign cases too.
Repeated large operands are distinct child occurrences and consume a
counted vertex; reconvergence never identifies expanded occurrences.
The paid aggregate for O(T) roots is O((T+2)^4) records. Import the
tree-to-graph operation separately for each tree. It preserves its
free polynomial and path-degree bound, with scalar/variable edges and
degree-zero connectors. Denote the resulting branch polynomials by
f_(v,alpha). Signed roots are the actual 1+f_(v,alpha). Their Boolean
faithfulness follows by induction through the tables and ordered ANDs.

At a large-output definition set J_(i,alpha)=0, represented by distinct
endpoints with no accepting path. Its defect is zero formally by the
chosen ordered product, even for repeated/complementary operands.
At a small-output definition both operands are small. Receive exactly
L079's small-root component: complete prefix-state diagrams of width
v≤2^k+2 on the n' undeleted variables, with equal-successor tests filling
every irrelevant level; auxiliary signed diagrams complement terminals.
The table trees, exact bases and these diagram roots lie in the same
increasing-multilinear subspace and have identical Boolean evaluations.
L026's injectivity in that subspace identifies their free polynomials;
its sign identity gives the exact wrappers. L026's paired P is in the
same subspace and computes the operand product on Boolean inputs, so
P=f_(i,alpha) formally. Its W therefore has precisely this defect.
Use L071's post-compilation graph for that identical W: increasing-level
pair states have only left recursive multipliers; a path exits once
into disjoint K/value/Boolean correction factors and never returns.
It has O((n'+1)^2 v^3) records per definition and pre-substitution degree
at most max(1,2n'−1). No treewidth/compiler input is used by this graph
component, and no diagram of a large root is needed.

Map each undeleted original to its unchanged original name, its Boolean
placeholder to that Boolean position of A, and its pair placeholder to
the corresponding pair-once position of A (either orientation has the
same axiom over F₂). This injective alphabet map commutes both with
zero substitution and with substitution of A. It proves, in the
unchanged full alphabet, exactly

    J_(i,alpha)(x,0)=0,
    J_(i,alpha)(x,A)=f_(i,alpha)+f_(a,alpha)f_(b,alpha).  (5)

No clause or deleted-input placeholder occurs in J. If n'=0 evaluate
every branch node as a scalar and take every J zero: each defect is a
scalar zero, with exact signed wrappers. This also covers all-input
deletion and constant branches. The original proof and full A remain
unchanged, and (5) is not a claim about a restricted ER refutation.

**Indicator reception and exact roots.** Order D as z_1,...,z_ell and put

    e_alpha=product_{j=1}^ell l_(j,alpha_j),
    l_(j,0)=1+z_j,       l_(j,1)=z_j,

with factors in the displayed order and empty product 1. L072's audited
component gives the formal finite-distributivity identities

    sum_alpha e_alpha=1,
    sum_alpha alpha_j e_alpha=z_j.                     (6)

It also supplies explicit affine graphs Q_(alpha,beta), using only the
D Boolean/commutator positions, with

    Q_(alpha,beta)(x,0)=0,
    Q_(alpha,beta)(x,A)=e_alpha e_beta
                              +delta_(alpha,beta)e_alpha. (7)

Here its only inputs are complete constant-width indicator diagrams in
the fixed D order. L026's P is increasing multilinear and has the Boolean
values delta_(alpha,beta)e_alpha, so injectivity identifies this P
formally; it does not identify the raw product e_alpha e_beta with that
diagonal polynomial. L071's graph component supplies (7) in
O((ell+1)^2) records. The subset-placeholder inclusion into A works as
above. For ell=0 take the unique e=1 and Q=0. These indicator identities
have no branch treewidth, branch order or branch multilinearity premise.

For each positive extension write, using independent serial/parallel
copies,

    r_v=sum_alpha e_alpha f_(v,alpha).                  (8)

For originals and constants write their exact prescribed roots, and
for signs write their actual wrapper 1+r_v. These also equal (8)
formally: an undeleted x_j uses (sum e_alpha)x_j=x_j, a deleted z_j uses
the second identity (6), and a scalar uses the first. The interpolant
of a signed root is sum e_alpha(1+f)=1+sum e_alpha f. This proves the
interpolant identity for every actual signed operand without commuting
any factor or identifying branch orders. On each Boolean assignment
exactly one e_alpha is 1; hence r_v is faithful on every assignment.
Each summand path has degree at most ell+d_0, which proves (2)'s d.
The degree need not be n: large branch polynomials can be nonmultilinear.

**Ordered formal recombination.** We can now receive L072's component
with the explicit branch graphs and (5), retaining its factor order.
For a fixed definition abbreviate a_alpha=f_(a,alpha) and
b_beta=f_(b,beta). Apply L035 only to the two x-only graphs a_alpha
and e_beta, with the full original commutator framing. It supplies

    C_(alpha,beta)(x,0)=0,
    C_(alpha,beta)(x,A)=a_alpha e_beta+e_beta a_alpha.    (9)

No J, Q, previously glued representative or recursive witness is an
operand of that call. Define the independently copied ordered graph sum

    H_i=sum_alpha e_alpha J_(i,alpha)
        +sum_(alpha,beta) [e_alpha C_(alpha,beta)b_beta
                              +Q_(alpha,beta)a_alpha b_beta]. (10)

At t=0 every summand has a zero J, C or Q factor, proving the first
identity (1). At A, the two double-sum contributions expand respectively
to

    e_alpha a_alpha e_beta b_beta
                       +e_alpha e_beta a_alpha b_beta,
    e_alpha e_beta a_alpha b_beta
                       +delta_(alpha,beta)e_alpha a_alpha b_beta.

The middle words are literally identical and cancel in F₂. Summing the
first words gives r_a r_b by (8); the diagonal words sum to
sum_alpha e_alpha a_alpha b_alpha. By (5), the first sum of (10)
substitutes to r_i plus that same diagonal sum. It cancels, proving
the second identity (1) as an equality in the free algebra. No factor
order is changed. This is exactly L072's proved recombination with a
different branch supplier, rather than an inference from Boolean
agreement of arbitrary free polynomials.

Serial/parallel construction uses disjoint factor occurrences and fresh
outer endpoints, with unit connectors. All graphs are acyclic and all
edges affine. For nonextremal factor endpoints, leaving a chosen exit
internally cannot return to it to take an exterior connector without
a cycle. Thus only the intended ordered factor path products accept;
parallel edges, zero factors and constant/empty products cause no extra
terms. Repeated/complementary operands are retained in (5) and (10).
When ell=0, (9) witnesses a_alpha·1+1·a_alpha=0 and Q=0; the same proof
works. When n=0 all branches and indicators are scalar. Empty original
clauses affect neither these identities nor the dictionary requirement.

**Complete copying, degree and bit-time ledger.** Put U=T+2. For one
branch S_*=O(U), n'+1=O(U), 2^k≤U and v=O(U). The component counts above
give O(U^4) paid value-tree/graph records. All small-output J together
cost O(T(n'+1)^2v^3)=O(U^6) records, with zero J at every other AND.
Complete small diagrams cost O(U^3), optional K and auxiliary P templates
O(U^4), and copied K/value blocks within J are already in O(U^6).
Supports, (3), scalar replacements and small tables fit these bounds.
Each record, original name, source annotation and dense reference costs
at most O(U) bits, so the branch storage/export is O(U^7) full bits.
The full original dictionary is O(T^3); repeating it for each of O(U)
branch output graphs adds O(U^4), including unused clauses and pairs.

The O(U^2) table evaluations visit O(U) source nodes each; tree visits
take O(U^4) operations and all diagram/pair/correction copies O(U^6)
indexed record operations. Working storage is O(U^7) bits. As in L079's
audited ledger, replacing every indexed access by a storage scan and
allowing another O(U^2) per operation for arithmetic, names and writing
costs O(U^15), covered by p(T)=CU^16. Checking all supports and (3) is
included. This is uniform in alpha and uses original T, with constants
absorbing S_*=O(T); no exponent depends on ell or extension depth.
The same p covers one indicator or Q graph with complete framing and
bit construction time: their constant-width component has O((ell+1)^2)
records, ell≤T, and the same explicit-copy/scan estimate is smaller.
It also covers parsing D's names, which cost at most O(T^2) bits.

Retaining M complete branches costs at most Mp; retaining all M^2
separate Q templates costs at most M^2p. Each L035 call has full input
O(p), including its alphabet/commutator dictionary, so its full output
is O(p^4), and its time is O(p^a) for one fixed a. Each definition has
M first summands and 2M^2 correction summands in (10); a constant number
of whole independent factors per summand costs O(Mp+M^2p^4).
There are O(T) definitions. All final base/value/signed graphs cost
O(TMp); each signed root receives a full copy of its unsigned graph.
Repeated dictionaries per final output and root/operand associations
are covered by these charges, with no sharing discount across outputs.

Thus all pre-renumbering graph records and existing label payload are
O(TM^2p^4). A further factor O(T+log(M+2)+log(p+2)) covers fresh dense
references and even verbatim restoration of every original name. The
extra O(T^3) full A is smaller. Since T,M,p≤Q, the total is at most
KQ^8. This includes retained branch/template exports if requested,
independent dictionaries and zero-graph endpoints. It is a deliberately
loose bound; it neither assumes implicit graphs nor counts a complete
graph copy as one operation.

All M branches can be enumerated explicitly. Branch/table/indicator
work takes polynomial time in T,M,p, while O(TM^2) L035 calls take
O(TM^2p^a). The remaining graph copies, dictionary lookups, source
associations, renumbering and binary writes admit a fixed polynomial
time bound in Q even with naive string scans. Choose fixed b≥8 large
enough to dominate these operations. This proves the claimed time
bound. There is no T^ell loop or exponent depending on M.

Every written H_i edge is affine in the independent x,t. Each accepting
path uses at most |E(H_i)| edges, so its word degree before substitution
is at most that count. Cancellation cannot increase degree. This proves
h in (2) and h≤KQ^8, replacing L072's unavailable multilinear degree
ledger. Equation (4) gives d_0=O(U^2 log U), so d is polynomial as well.
No semantic cancellation bound is substituted for a path-degree bound.

Finally the abstract value DAG remains the original O(T) acyclic
associations; replacement/indicator/arithmetic vertices are internal to
supplied graphs, not new extensions. Exact bases/signs, every relation
(1), complete E_ABP and d,h≥1 meet all L037 promises for the unchanged
F, pi and A. M≤U makes its conditional certificate bound polynomial in
T. Neither a restricted refutation nor a new ER proof has been assumed.

The continuation threshold was a fixed polynomial in original T with
both formal identities. The displayed construction meets that threshold
under the supplied residual promise. Attempts 019–020 retain their force
against unrestricted common-order width and general degree-only
same-output conversion. No large-root OBDD, general circuit-to-ABP
theorem or universal Boolean-zero witness is used here. A separate
critical audit remains necessary, especially for original-cutoff branch
reception, alphabet inclusion and the independent-copy ledger. No finite
test, script certificate or formal verification is claimed.

**Separate critical audit — step 310, 2026-10-18.** This audit uses the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-18-input-deletion-counted-path-critical-audit.md`.
It checks the complete construction under its unchanged hypotheses.
Reuse the precise Bryant and Raz–Shpilka components cited above, L079's
step-306 audited circuit construction and L072's step-278 audited
recombination. Neither whole structural theorem is applied with a
weakened hypothesis. Earlier pending-audit language describes the
construction step and is superseded by this section. This is an all-size
informal audit, not a new theorem, executable test or formal verification.

First keep the two parameters distinct: k comes from original T and
ell=|D| only counts deleted original inputs. Each deleted positive input
is replaced at its actual outgoing operand occurrences; retained sign
nodes still complement their new scalar predecessor. Thus a negative
literal receives 1+alpha_j, not alpha_j. Repeated operand positions get
separate leaves, and each deleted original's own association gets its
scalar root. There are O(T) such occurrences even with arbitrary fan-out,
because every target gate has bounded fan-in and there are O(T) gates.
The resulting S_*=O(T) bound includes isolated roots and both signs.
Topological induction proves the restricted Boolean values without using
any restricted inference of pi. Scalar zero leaves have empty support,
but a product by zero retains the union of its operand supports.

Support containment makes the small nodes ancestor-closed. Equation (3)
computes the maximum count along an actual source path, not the total
number of counted nodes in a DAG. Its original cutoff stays k in every
branch. Small table evaluations visit the original source order with
alpha fixed; dependence only on syntactic support justifies zero-filling
the other undeleted inputs. At most O(T) tables each have at most 2^k
entries. Their paid Shannon trees, exact bases and signed wrappers satisfy
the stated 10·2^k size and k degree bounds. Their use requires neither
large-root diagrams nor an ER derivation on the remaining variables.

For a large root, count occurrences after stopping at small roots.
Signs and ANDs with one large operand have one large child; ANDs with
two large operands are exactly the counted binary vertices. A large
base cannot occur. Suppressing unary vertices and inducting on the
remaining split budget gives at most 2^k leaves. Each root-to-leaf path
follows distinct source vertices, hence has length at most S_*; the union
of these paths has at most S_*2^k vertices. This includes reconvergence
and repeated large operands because occurrences remain distinct. With
a ANDs and z signs, the 2a+z slots minus a+z−1 internal edges leave
exactly a+1 small attachments. Scalar summands at signs cost two added
formula nodes each. Consequently the independent tree cost is at most
10·2^k(S_*2^k+1)+2S_*2^k≤12(S_*+1)2^(2k). Summing attachment degrees
bounds every accepting path by d_0 in (4); scalar edges and graph
connectors add no degree. This also bounds already-small roots. No
semantic cancellation or uncharged unfolding is used.

Next check the formal small-output interface. The complete prefix-state
diagrams retain all n' undeleted levels, including redundant tests and
terminal gaps, with width at most 2^k+2. The support table trees and the
diagram roots are increasing multilinear in the same order and agree on
all Boolean assignments. Precisely L026's injectivity therefore identifies
them as free polynomials. Its terminal-complement identity identifies the
auxiliary signed diagrams with the actual signed wrappers. At a small
output both operands are small, so the same argument identifies the
paired P with its chosen output f_i. L026's W then has the exact defect
in (5), together with its independently proved zero-at-zero identity.

L071's graph realizes that same W before substitution: pair vertices
have only left-multiplied recursive successors; an accepting path exits
once into a disjoint K/value/Boolean block and cannot return. There are
O((n'+1)v²) pair vertices and O((n'+1)v) records in the constant number
of copied factors per exit. Thus O((n'+1)²v³) records suffice per J.
At a large output f_i is exactly the ordered product of the globally
chosen branch operands, so the distinct-endpoint zero J is valid. The
small-output bridge is never applied to a nonmultilinear large root.

The alphabet map is defined on generators: each undeleted x retains its
original name, each Boolean placeholder goes to that variable's full-A
position, and each pair placeholder goes to its unordered pair's full-A
position. Distinct subset generators stay distinct; both possible pair
orientations have the same F₂ axiom. On each generator the map commutes
with zero substitution and with axiom substitution, hence it does so on
every free polynomial. Unused full-A generators, including every clause
placeholder, can be adjoined without changing an identity. This verifies
(5) in the original alphabet. For n'=0 all branch roots are scalars,
exact signs remain scalar, and every AND defect is identically zero.

For (6), distribute the ordered product of the sums (1+z_j)+z_j=1.
Fixing the jth bit to 1 leaves z_j in its original factor position and
all other sums equal to 1. No factors commute. The indicator diagrams
have constant width in the D order. Their paired P, and only that P,
is identified with delta_(alpha,beta)e_alpha by L026's injectivity;
L071's O((ell+1)²)-record W supplies (7) through the same alphabet map.
The raw product e_alpha e_beta is not replaced by its Boolean reduction.
For ell=0 there is one indicator 1 and the required Q is zero.

Every exact original, scalar and signed root equals its interpolant:
undeleted originals factor on the right of sum e_alpha, deleted originals
use the fixed-bit identity, and signed interpolation adds sum e_alpha=1.
These statements cover signed originals and constants as well as signed
extensions. They require no order or multilinearity of branch values.
Faithfulness separately follows by evaluation at the unique selected
branch. An interpolant path has at most ell indicator degree plus d_0
branch degree; exact bases and signed wrappers satisfy the same d.

Each L035 input in (9) is an explicit x-only branch-value graph and an
indicator graph, with the full original commutator framing. In particular
no J, Q or recursive witness is used as an operand. On A substitution,
the two correction terms of (10) contain the identical middle word
e_alpha e_beta a_alpha b_beta twice. Cancelling those words leaves
e_alpha a_alpha e_beta b_beta and the diagonal term
 delta_(alpha,beta)e_alpha a_alpha b_beta. The first terms sum to r_a r_b;
the diagonal terms cancel the identical sum from the J part of (10),
leaving r_i+r_a r_b. At zero substitution every whole summand has a zero
J, C or Q factor. This reasoning preserves cancellation within those
factors and proves both identities independently of pathwise vanishing.

Fresh disjoint serial factors and parallel branches have only their
specified forward connectors. Within a factor, leaving a designated
exit internally cannot return to that exit in a DAG; no later factor
returns to an earlier one. Thus nonextremal or coincident endpoints,
parallel edges, no-path factors and empty products add no unwanted
accepting paths. Repeated/complementary operands do not change any
identity. Empty deletion gives e=1 and zero-valued C and Q; all-input
deletion gives scalar branch data; n=0 combines these cases. Constant
branches and redundant tests are already covered by the small-root
recurrences. Empty original clauses leave the data construction unchanged
and remain in the complete dictionary. Every unused definition is still
processed and every sign is still written.

Independently recount with U=T+2. One branch has O(U^4) paid value
records. Its at most O(U) small-output witnesses each use O(U^5)
records, giving O(U^6). Small diagrams, auxiliary P and optional K
templates contribute O(U^3), O(U^4) and O(U^4); copies inside J are
already charged. O(U) bits per record safely pays original names,
annotations and dense references, giving O(U^7) storage. The complete
O(T³)-bit original dictionary, even repeated in O(U) branch exports,
adds only O(U^4). O(U²) table evaluations visiting O(U) nodes, O(U^4)
tree visits and O(U^6) graph-record operations suffice. Replacing each
indexed access by an O(U^7)-bit scan and paying another O(U²) per
operation gives O(U^15), within the fixed p(T)=CU^16. This includes
source parsing, support/promise checks and independent copies. Indicator
and Q construction with full dictionaries fits the same p, uniformly.

Retaining branches costs Mp and retaining all Q templates costs M²p.
L035 receives O(p) full input bits per call, so its output costs O(p^4)
and its time O(p^a) for a fixed a. Each definition has M first summands
and 2M² correction summands, each copying a constant number of complete
factors. All definitions therefore cost O(TM²p^4); final values/signs
cost O(TMp), with full unsigned graphs copied into signed outputs.
Associations, zero endpoints, retained templates and repeated dictionaries
fit these charges. Fresh references and verbatim names multiply the
pre-renumbering payload by at most O(T+log(M+2)+log(p+2))=O(Q).
The exponents 1+2+4+1 give the stated KQ^8, with the extra O(T³)
dictionary smaller. There is no sharing discount or unit-cost graph copy.

The O(TM²) commutator calls cost O(TM²p^a). Branch/indicator enumeration,
all individual record copies, dictionary scans and renumbering have
fixed polynomial bit costs in Q; one fixed b≥8 dominates them. Since
M≤U and p=CU^16, this is one polynomial in original T. Each written
H edge is affine in independent x,t and each DAG path uses at most its
edge count, proving h as stated before substitution and h≤KQ^8.
The path calculation above gives d=O(U² log U), without assuming large
roots multilinear. Internal graph vertices are not new abstract
extensions, so S=O(T) and the original pi, exact roots, every local
identity and complete E_ABP meet L037's unchanged receiving hypotheses.

The audit finds no substantive defect and needs no hypothesis, bound or
argument repair. Direct mathematical inputs and the DAG are unchanged.
This establishes new local verification of the restricted supplier, not
mathematics beyond the checked sources or certified originality. Attempts
019–020, arbitrary-ER data, formula-only bounds, W/V/U, every-certificate
hardness and unrestricted SAT decision/separation remain unresolved.
No mathematical script, finite certificate or proof-string verification
is claimed. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching conditioned counted-path theorem and binary accounting:
**not checked**; no absence claim. Supporting mathematics consists of
the precise Bryant and Raz–Shpilka source components cited above and
the audited local interfaces stated in the proof. The prior assessment
found no inspected full-statement match; that does not certify novelty.
