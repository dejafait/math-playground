# L087 — Two-order OBDD product witness bounds would imply NP=coNP

## Hypotheses

Work over the free associative algebra F₂⟨y₁,…,y_q⟩. Supply exactly two
explicit deterministic dense OBDDs D,E on this same explicitly listed
alphabet. Each has its own supplied permutation of all q variables; the
two permutations are strictly different. A level-k state queries the kth
variable in its order, has one successor for each bit, and both successors
are at level k+1. Only the final level has Boolean terminals. Redundant
tests, unreduced states and unreachable states are permitted. All orders,
states, transitions, roots, terminal values, names and framing are written.

The ordered representative of either diagram is defined by L026's suffix
rule, separately in its own order z₁,…,z_q:

    r_0=0, r_1=1,
    r_a=(1+z_k)r_(a,0)+z_k r_(a,1).                 (1)

Put f=r_D, g=r_E, retaining the ordered free-ring product fg. For the
fixed listed alphabet order y₁,…,y_q, let B consist only of

    b_i=y_i²+y_i,           b_ij=y_i y_j+y_j y_i  (i<j),

with distinct placeholders σ_i,τ_ij. Define M as 2 plus the full bit
length of the two diagrams, both orders, their complete original-name
dictionary and the full B/placeholder dictionaries, including all axiom
words and framing. No witness or witness-degree parameter contributes
to M. Unused permitted symbols in a witness must still have their full
dictionary entries. Implicit graphs and circuit-valued labels are excluded.

Assume the following **unproved restricted universal premise W₂**: one
fixed polynomial p, independent of q, the pair and its orders, bounds
the full encoding of some explicit acyclic affine-F₂ ABP H whenever
fg(a)=0 for every a∈{0,1}^q, with the formal identities

    H(y,0)=0,                  H(y,B(y))=fg.        (2)

H uses only y,σ,τ. It may have nonlinear placeholder dependence,
cancellation, arbitrary designated endpoints and dead records, with the
empty-path convention of L041. There is no constructor or semantic-promise
tester. In fact it suffices that this premise cover the particular pairs
below, whose nonterminal widths are at most three in both orders.

Use the inspected occurrence-splitting mechanism of Meinel–Theobald and
the named Cook–Levin and Raz–Shpilka inputs specified in the proof.
L041's audited zero-testing component receives explicit arbitrary affine
graphs; its formula-specific verifier is not invoked unchanged.

## Conclusion

    W₂ implies NP=coNP.

The implication already holds with W₂ restricted to the constructed
width-at-most-three pairs, dense in two strictly distinct orders. This
is a conditional burden on the alternative-witness bound, without a
proof or refutation of that bound, a witness finder or a converse. It
does not imply either answer to P versus NP. It reproduces the known
two-program consistency/identity-checking mechanism with local free-ring
and full-bit specialization; certified originality is not claimed.
The separate critical audit on 2026-10-18, recorded below, finds no
substantive defect. This remains an informal conditional result, without
a verified implementation or a proof of W₂.

## Proof

**Coverage and precise imports.** The pre-invocation SPECIALIZE assessment
is `drafts/literature/2026-10-18-two-order-obdd-product-witness-burden.md`.
Christoph Meinel and Thorsten Theobald, *Algorithms and Data Structures
in VLSI Design: OBDD — Foundations and Applications* (Springer, 1998),
Theorem 4.32 proof and Lemma 4.35, displayed pp.72–74 in the inspected
[English copy](https://www.slideshare.net/slideshow/algorithms-and-data-structures-in-vlsi-design-259675197/259675197),
split query occurrences and use two oblivious read-once programs for
clause testing and copy consistency. Definitions 4.28 and 6.1–6.2,
pp.69,89–90, specify the relevant programs/diagrams. We specialize that
mechanism to ordinary width-at-most-three SAT below, explicitly providing
the small transition systems. This applicability argument is needed
because Problem 4.29's exactly-three-literal wording and Lemma 4.30's
binary-clause transformation do not match. No bounded-occurrence
completeness premise or claim from the unread Lemma 8.14 is imported.

Adnan Darwiche and Pierre Marquis, [*A Knowledge Compilation Map*, JAIR
17 (2002), 229–264](https://www.cril.univ-artois.fr/~marquis/darwiche-marquis-jair02.pdf),
Appendix A, pp.253,260–261, corroborate hardness of consistency of two
differently ordered OBDDs, citing that Lemma 8.14. This corroboration is
not a substitute for the explicit receiving specialization below.

Import the standard named **Cook–Levin theorem**, including 3-SAT
completeness; see Stephen Cook, [*The P versus NP Problem*, §2,
pp.4–5](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf).
The only PIT input is Ran Raz and Amir Shpilka, [*Deterministic Polynomial
Identity Testing in Non Commutative Models*, author manuscript,
Definition 1 p.4 and Theorem 4 p.9](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf):
deterministic O(s⁵+s n⁴) field operations for homogeneous adjacent-layer
linear-edge noncommutative ABPs with unique terminals and singleton
first/final layers. Its actual receiving hypotheses are met through
L041's finite constant closure, output restriction and support-path
pruning, including direct degree-zero/no-path cases. F₂ operations have
constant bit cost. We reuse that audited component, not a new PIT proof
or a theorem about arbitrary arithmetic circuits.

**A pair from ordinary 3-SAT, with distinct orders even in small cases.**
Let F be a well-formed explicitly written width-at-most-three CNF with
m clauses, N=|F| and L=N+2. Literal repetitions, tautological clauses, clause
repetitions, empty clauses and the empty conjunction are permitted.
Choose two fresh variable names u,v and append, in this order,

    (u OR v),                 (NOT u OR NOT v).           (3)

Call the result F⁺. These two clauses have a satisfying assignment
u=1,v=0 independently of F. Thus F⁺ is satisfiable iff F is.
Fresh identifiers and the retained old-name map have polynomial length;
for example two tagged names longer than every old name have O(L) bits.

Replace each literal occurrence in F⁺ by a fresh variable y_(j,k),
retaining its sign, where j is the clause position and k its literal
position. There are q≤3m+4=O(L) such variables, with q≥4. They, rather
than the old unsplit variables, are exactly the originals of the two
diagrams and their B dictionary. Every one is queried in both diagrams.
No separate unsplit original or anchor symbol is permitted in H.

For D, use the order π that lists these occurrences by clause and then
literal position. D tests the conjunction of the split clauses. It can
be written with at most three states at every nonterminal level:
a failure state ⊥ and the two bits t=0,1 recording whether the current
clause has already been satisfied. At the first occurrence of a clause
the live state is 0. On a queried bit b, update t to t OR ℓ(b), where
ℓ(b)=b for a positive literal and ℓ(b)=1−b for a negative one. Failure
stays failure. At a clause's last occurrence, a false updated bit sends
the state to ⊥; a true updated bit sends it to live state 0 for the next
clause. At the last occurrence overall, send success directly to terminal
1 and failure to terminal 0. All intermediate failure transitions proceed
to the next variable level, so no early terminal is used. If F contains
an empty clause, take the root to be ⊥, which propagates to terminal 0;
the remaining nonempty-clause schedule is still written. Empty clauses
otherwise require no queried variable. The appended clauses ensure a
last occurrence always exists. Unreachable live states may be retained.
Induction over each clause's literal positions verifies exactly this
clause tester, without enumerating assignments.

For E, group the occurrences by their unsplit variable, listing old
variables in a deterministic order followed by u then v. Within a group
use their π order. Call this permutation ρ. E tests equality of every
group's bits. Again use states ⊥,0,1, initially live 0. At the first
occurrence of a group, replace any live state by its input bit b. At each
later occurrence, retain the remembered bit if it equals b and otherwise
go to ⊥. Failure always propagates. The first occurrence of the next
group overwrites the old remembered bit. After the last query any live
state goes to terminal 1 and failure to terminal 0. A singleton group
places no constraint. Positions of group starts are part of the written
level schedule, not additional memory. This gives width at most three
with dense levels and exactly the required equality test.

At the four appended occurrences, π ends with

    u₁, v₁, u₂, v₂,

whereas ρ ends with u₁,u₂,v₁,v₂. These four names are distinct. Their
relative order proves π≠ρ regardless of F, including the empty conjunction
or an empty clause. No ignored padding variable or semantic change of
an already chosen free-ring representative is used. Every level queries
its scheduled variable even if both successors coincide.

There are exactly two diagrams, each with at most 3q+2 vertices and
6q transitions. Both have the same q-variable alphabet and final Boolean
terminals. Their joint acceptance has the exact scalar characterization

    ∃a [D(a)=E(a)=1]    iff    F is satisfiable.           (4)

Indeed a satisfying assignment to F extends by u=1,v=0 and copying
each unsplit value to all its occurrences; it satisfies both testers.
Conversely E's accepted bits define one value for each occurring unsplit
variable, and D's acceptance makes every clause of F⁺ true under those
values. Restrict to F. An empty clause prevents D's acceptance, as it
should; repetitions and both literal signs use the same raw group bit.

**Exact path polynomials, without changing variable orders.** Apply
L026's rule (1) to D in order π and E in order ρ separately. Its suffix
evaluation argument shows f(a)=D(a), g(a)=E(a) for scalar assignments.
We do not invoke L026's common-order product construction or infer
formal equality from Boolean equality across these different orders.
Scalar multiplication in F₂ and (4) give

    fg is Boolean-zero    iff    F is unsatisfiable.      (5)

For each diagram make an explicit affine ABP using its states, replacing
the bit-0 transition at variable y by an edge labelled 1+y and the bit-1
transition by an edge labelled y. Keep parallel edges, even for equal
successors. Attach a fresh exit by a 1-edge from terminal 1; terminal 0
has no such edge. Attach a fresh entrance by a 1-edge to the diagram root.
The suffix path recurrence is exactly (1), including terminal values.
Backward induction in the finite DAG therefore identifies its formal
path polynomial with the prescribed representative, not just its Boolean
function. Repeated equal-successor transitions cancel only as dictated
by F₂ addition; they are never silently identified as a single edge.

Take disjoint copies of the two graphs and connect the first exit to the
second entrance by a 1-edge, with fresh exterior endpoints if necessary.
Every accepting path decomposes uniquely into a first-graph path, that
connector and a second-graph path. Finite distributivity proves its exact
ordered polynomial is fg. Denote this graph by G. Its variable-word
degree is at most 2q, but no degree promise on a sought H is used.
This construction makes no diagram for the intersection and does not
unfold the exponentially many accepting paths.

**A fixed full-bit input bound before H exists.** There are O(L) diagram
and graph records and two O(L)-entry permutations. Occurrence identifiers
can be tagged dense pairs of O(log(L+2)) bits; retaining the old identifier
map still costs O(L²) bits under the conservative O(L)-bit-name bound.
Choose an explicit fixed dictionary order for the q occurrence variables.
B then has q+q(q−1)/2 entries, each with at most four original-symbol
occurrences. Its independent placeholders can be tagged by their dense
indices with O(log(L+2)) bits. Even repeating O(L)-bit original names
at every word occurrence gives O(L³) bits for all B and placeholder
framing. Root associations, terminal records, both orders and all graph
labels fit this same loose bound. Consequently there are absolute fixed
constants C,C' for this encoding such that

    M≤C L³,                 |G|≤C' L³.                    (6)

These lengths include all input dictionaries before H is sought; no H,
H degree or putative bound p(M) enters their construction. All records
are produced in deterministic polynomial bit time in N. These counts
also prove that dense completion and strict order distinction have not
incurred an exponential cost.

**One promise-free verifier.** On (F,H), reject malformed F and recompute
D,E, their permutations, B and G exactly as above. Parse H as an explicit
acyclic affine graph in L041's model. Check actual vertex/edge/label lists,
unique record identifiers, endpoint references, acyclicity and exact
permitted symbol/axiom dictionaries; reject any foreign variable or
placeholder, including all original-clause placeholders. Counts must
match actual written records before allocation. Extra unreachable records,
zero labels, repeated label entries, nonlinear placeholder paths and
arbitrary endpoints remain permitted. All such syntax checks have a
fixed polynomial bound in N+|H|. The verifier does not need to know p.

Accept precisely when the following free-ring identities pass:

    H(y,0)=0,                H(y,B(y))+f g=0.              (7)

Use L041's audited graph zero-testing component for both tests. To check
its application, split affine entries into parallel constant or singleton
symbol edges. For the first test delete placeholder entries. For the
second replace each σ_i edge by the two paths y_i y_i and y_i, and
each τ_ij edge by the two paths y_i y_j and y_j y_i, with fresh gadget
interiors. Each edge occurrence has its own bounded gadget. Thus full
simultaneous substitution is exact even on nonlinear placeholder paths.
Add a disjoint G branch for the second test. The graph operations are
ordered and endpoint-safe as proved in L041; wrapping nonextremal or
coincident designated endpoints retains its empty-path convention.
No path unfolding or Boolean-identity test is involved.

The resulting graphs have polynomial full length in
R=2+N+M+|G|+|H|. They are exactly L041's finite acyclic constant/singleton
edge inputs. Its finite constant-path matrices retain leading/trailing
constant stretches; each positive word-length component is formed up to
the graph's vertex bound. Restriction of the last layer to the designated
exit, combination of zero linear labels and pruning to support paths
gives the actual Raz–Shpilka terminal model. No-path components are zero
directly, and the constant component is tested separately. Cancellation
among support paths is left to PIT. These audited operations apply to G
regardless of its two orders: the imported PIT theorem has no common-order
hypothesis. L041 establishes polynomial bit cost on all such inputs,
including false identities and no-path/coincident-endpoint graphs. Since
(6) bounds R by a fixed polynomial in N+|H|, this is a single deterministic
polynomial-time verifier for every submission. This reuses the graph
component, replacing L041's clause-product branch by G; it does not assert
that L041's F-specific verifier already computes this different polynomial.

For soundness, suppose the verifier accepts and F has a satisfying
assignment. By (4) there is an occurrence assignment a with f(a)g(a)=1.
Scalar evaluation is a homomorphism from the free algebra to F₂, and
B(a)=0. Evaluating both accepted identities gives

    1=f(a)g(a)=H(a,B(a))=H(a,0)=0,

a contradiction. Thus every accepted F is unsatisfiable for every H,
without W₂ or a Boolean-zero-promise test. This remains valid for
cancellation-based and nonlinear witnesses.

For completeness, if F is unsatisfiable, (5) places the computed pair in
W₂'s domain. Both orders are strictly distinct and all promised input
conditions have been checked. Some H satisfying (2) has length at most
p(M) and is accepted by (7). Choose a single increasing polynomial
majorant for p on nonnegative integers and compose with (6). There exist
fixed A,d, independent of F and H, with |H|≤A(N+2)^d for every such F.
An NP machine fixes that bound in its code, guesses an H up to it and
runs the verifier. No algorithm for discovering the constants or H is
needed for this existential class inclusion. Hence UNSAT 3-CNF is in NP.
Cook–Levin then implies that the complement of every NP language is in
NP: reduce its instances to well-formed 3-CNFs and use these certificates
on the unsatisfiable images. This gives NP=coNP. Malformed encodings are
polynomially recognizable and do not enter that reduction.

**Separate critical audit — 2026-10-18, step 338.** The audit reuses the
unchanged SPECIALIZE assessment and checks this complete proof against
L026's suffix interface and L041's complete repaired graph zero tester.
It imports no further theorem and finds no substantive error. The
following are the load-bearing checks, including the degenerate cases.

For D, immediately before a noninitial literal in a clause, a reachable
live state records the OR of exactly the preceding literals of that
clause, and every previous clause is true. At a clause's first literal
the reachable live state is 0. Updating that bit and then either failing
or resetting at the boundary preserves these assertions. A singleton
clause performs the update and boundary test on the same query; the last
clause sends its successful update directly to terminal 1. Failure never
leaves ⊥. An empty clause selects ⊥ at the root regardless of its written
position. Thus retaining live states which are unreachable at some levels
does not create an accepting run. For E, a live state within a group is
its first raw bit, all preceding bits of that group agree with it, and
all preceding groups have passed. A group-start query overwrites only
live states; ⊥ remains absorbing. A singleton imposes no comparison and
the final query performs its comparison before the terminal decision.
Literal signs belong only to D, so negative occurrences do not reverse
E's equality test. These invariants cover repetitions, tautologies, the
empty conjunction and empty clauses with the same three states per level.

The appended clauses use fresh unsplit u,v, so the four appended
occurrence names are distinct even when F has no occurrences. They are
last in π; placing u,v after all old-variable groups makes them last in
ρ as well. Their displayed relative orders differ. The assignment
u=1,v=0 satisfies both appended clauses independently of all old bits.
The gadget therefore changes neither direction of (4), while q≥4 avoids
any exceptional zero- or one-variable permutation case. The premise
allows redundant and unreachable states, so no reduction or canonical
diagram requirement is silently added.

The path graph checks formal equality by the same left-labelled suffix
recurrence as (1). Parallel transitions with a common successor remain
separate summands; the terminal-1 exit implements scalar 1 and terminal 0
has zero suffix. Disjoint composition permits exactly a D path followed
by an E path, giving fg, never gf. No identity replaces either diagram
by a Boolean-equivalent representative in the other order. Only the
scalar statement (5) uses joint satisfiability. Consequently the audit
does not rely on extending L026's common-order injectivity argument to
different orders or on a small OBDD for the intersection.

The input ledger counts q=O(L) explicit occurrences, O(q) records in
each diagram and G, both permutations, the retained old-name map and
q(q+1)/2 explicitly written axioms/placeholders. Every axiom has at most
four original-symbol occurrences. Even the conservative O(L)-bit name
allowance yields O(L³) bits, including framing and endpoints. All maps
and schedules are computed before seeking H. Polynomial construction
uses only parsing, grouping and writing these lists. The certificate
bound is one polynomial in M, not a separate polynomial for each pair,
and no certificate-dependent size or degree parameter enters (6).

Finally, the verifier checks every submitted graph's actual records and
dictionaries before allocating derived graphs. Bounded edge replacement
preserves arbitrary nonlinear placeholder paths and cancellations. Fresh
outer endpoints retain the designated empty path when the endpoints
coincide; that case fails H(y,0)=0 rather than escaping the test. In
L041's component, finite constant closure includes both leading and
trailing constant stretches, degree zero is tested separately, and no
word length exceeds the vertex bound. Restricting the final layer and
pruning support paths supplies singleton terminal layers and unique
terminals to the imported PIT theorem; no-path components are handled
directly and cancellation is left to PIT. None of these operations
requires a variable order. Replacing L041's clause-product branch by G
therefore retains a fixed polynomial cost in N+|H|, including on false
identities and dead-record submissions. Scalar evaluation proves
soundness for every accepted H without W₂. Only completeness invokes
W₂, after (5), and the increasing majorant of p composed with (6) gives
one certificate polynomial. Thus the existential NP machine and the
Cook–Levin complement inference do not require a witness finder or a
promise-recognition algorithm.

This audit makes the existing conditional implication available for
downstream informal use; it adds no stronger theorem and no new witness
bound. Its only direct local inputs remain L026 and L041. The more
general W, faithful-collection premises and common-order availability
stops are comparisons, not additional hypotheses of this implication.

**Limits and continuation test.** This proves the approved conditional
specialization using known mechanisms, not W₂. L041's more general W
would imply W₂ by the small graph construction, but its implication alone
did not establish the burden for this weaker hypothesis. L042's universal
faithful collections and contradictory host are not used. L085/L086 and
Attempt 030 concern common-order value availability, which remains a
different obstruction. The present result supplies neither such values
nor formal witnesses, arbitrary ER representation, short certificates
for all UNSAT, an unconditional lower bound or a SAT algorithm. The
separate audit above checks the width-three transition schedules, strict
order distinction, exact ordered graph identity, pre-witness bound and
promise-free PIT interface. Any future application outside these
hypotheses needs its own coverage and applicability argument. No complete
main-problem candidate has been proposed.

## Mathlib

Coverage is **not checked** for the full two-order conditional, two-OBDD
consistency hardness, Cook–Levin or Raz–Shpilka. No matching theorem or
absence claim is asserted. The known primary Boolean mechanism and PIT
theorem are imported with their receiving hypotheses justified above;
L026 supplies only the separate ordered-suffix interface and L041 only
its audited arbitrary-affine-graph verifier component. No mathematical
script, finite example or proof-assistant verification is claimed, and
none substitutes for the all-size transition and bit-count arguments.
