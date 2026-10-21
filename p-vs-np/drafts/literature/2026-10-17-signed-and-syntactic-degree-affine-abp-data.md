# Exact signed-AND data from syntactic degree — completed source comparison

TARGET: Determine whether every exact signed-AND ER value DAG of maximum syntactic degree D admits L037 data of full bit length and construction time polynomial in T+D+2, retaining constants and both signs.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded discovery for signed-AND/formal-degree unfolding, constant-addition circuits, parse trees and noncommutative circuit/formula/ABP comparisons; inspected the precise primary passages below and the relevant L019/L033, Attempts 016/020, L031/L032/L075 conventions and L037 interface. No inspected full-statement match; no novelty inference.
SOURCE_EVIDENCE: Reused and successfully retrieved Raz–Shpilka's undated author-hosted 16-page manuscript, section 2.1 and Lemma 2 Step 1, PDF pp.4–5; retrieved Nisan's STOC 1991 primary-paper mirror, Theorem 1 in section 3 and Theorem 4 with its recurrence in section 4.2, PDF pp.5–6. Exact passages and limitations are recorded below.
COMPARISON: Formula-to-graph conversion is covered, but the all-root presentation bound in T+D is not. L033's displayed small circuit uses a sum of two nonconstant sandwiches, outside the proposed gate syntax; no bounded-D realization in that syntax was inspected. L019 obstructs a bound in T alone, not the charged T+D statement. L075 remains family-specific.
GAP: Prove or refute one fixed polynomial full-bit/time bound for the exact signed-AND data, paying constant subgraphs, signed chains, independent copies of every root, repeated operands and complete dictionaries in actual T+D+2. Neither a generalized bound nor a qualifying obstruction is established by this review.
REASON: Essential conversion and receiving-model coverage is adequate for one later bounded attempt on the unchanged target; the unproved presentation/encoding specialization is explicitly isolated. EXPLORE approves investigation, not the proposed conclusion or its originality.
LITERATURE_REASON: The startup REVIEW_REQUIRED target generalizes L075's family hypotheses; this turn supplies the missing separate theorem comparison without repeating its completed audit or doing mathematics.
SCOPE: Only the canonical exact signed-AND DAG and degree convention below; no arbitrary nonconstant addition, semantic-degree replacement, Boolean simplification or uncharged abstract graph.

## Intermediate target and relevance

The main gap is still unrestricted SAT decision/separation, and the immediate
representation gap is arbitrary ER-to-affine-ABP data. The proposed target
would isolate a sufficient condition stated directly on the exact signed
value DAG, extending the restricted-family role of L075. Its intended
downstream use is L037 when D is polynomially bounded in actual T. No such
bound on D is assumed for arbitrary ER proofs, and no general representation
or SAT consequence is claimed. This is a proposed target, not a lemma.

Use L037's width-at-most-three original CNF and signed-AND ER convention,
T=2+|F|+|pi|, and its original-axiom dictionary. Exact originals and constants
are retained. Use the canonical abstract DAG with one positive and one
signed node per proof variable, plus the two constants, and no extraneous
abstract nodes; nonextension proof variables absent from F have value zero
as in L037. A signed node is 1+P and an AND node is the ordered product
of its designated operands. Set syntactic degree to zero on constants,
one on original variables, the maximum at addition of 1 and the sum at
AND, without cancellation. D is the maximum over the supplied exact
value DAG. Both signs and every unused extension value must be supplied;
H_i=0 is intended only because the requested values are exact. Any
constant simplification must preserve formal polynomials. Do not replace
syntactic degree by degree after cancellation or by Boolean degree.

## Discovery and precise primary coverage

On 2026-10-17 the bounded web search included the queries
`"signed-AND" "syntactic degree" ABP`,
`"AND" "NOT" "formal degree" circuit formula`,
`"arithmetic circuits" "addition by constants" formula`,
`"arithmetic circuit" "only" "constant" "addition gates" formula degree`,
`"arithmetic circuits" "parse trees" "formal degree" formula`,
`"noncommutative" "syntactic degree" "unfolding"`, and
`"noncommutative" "multiplicatively disjoint" "degree" formula`.
Related results returned general circuit/formula surveys, formula depth
reduction and standard degree conventions. These search hits do not
establish a theorem for this target. No full matching statement or
qualifying counterexample was found in the inspected sources. This is
bounded discovery, not a claim of exhaustive coverage or novelty.

**Conversion input.** Ran Raz and Amir Shpilka, *Deterministic Polynomial
Identity Testing in Non Commutative Models*, undated author-hosted 16-page
manuscript, [section 2.1 and Lemma 2 Step 1, PDF pp.4–5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Read the formula and ABP definitions, lemma hypotheses and complete Step 1:
scalar/variable leaves, parallel sums and ordered serial products yield
a constant-edge, possibly nonleveled graph of linear record size/time in
the supplied tree. The field is arbitrary, including F₂. The full lemma
instead assumes zero free term and constructs homogeneous components;
that later conclusion is unnecessary here. Step 1 retains constants
and mixed degrees. Reuse it without reproof once a presentation is paid.
The input is a tree, so this theorem supplies no unfolding bound for a DAG.
This confirms the component coverage already recorded in
`2026-10-10-frege-abp-er-one-way-bound-application.md` and
`2026-10-07-alternative-affine-abp-certificate-assembly.md` in this directory;
no source-access blocker remains for this component.

**General obstruction.** Noam Nisan, *Lower Bounds for Non-Commutative
Computation (Extended Abstract)*, STOC 1991, pp.410–418,
[DOI](https://doi.org/10.1145/103418.103462),
[primary-paper mirror, Theorem 1, section 3, PDF p.5; Theorem 4 and proof, section 4.2, PDF p.6](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf).
Read the real-field rank characterization and the palindrome theorem's
linear-circuit/exponential-ABP conclusions and displayed recurrence. Its
addition joins two nonconstant sandwiches. L033 already supplies the F₂
and affine-DAG specialization; it is not reproved here. The displayed
source circuit is outside the present gate syntax. Neither the source
nor L033 supplies a polynomial-D signed-AND encoding of it. Consequently
this inspected obstruction cannot simply be asserted for the target.

## Local comparison, unresolved specialization and test

L019's Hypotheses and used-extension proof give literal tree substitution
with cost parameter U and a used Fibonacci family with exponential U in
T. That result does not lower-bound representation size by every
polynomial in T+D. This review does not infer a new degree bound or a
polynomial occurrence bound from it. Attempt 016 concerns the identical
assembled certificate's surviving degree, not the representative-only
target. Attempt 020/L033 stops arbitrary arithmetic circuits; its broader
addition syntax remains essential to the recorded comparison. Both
stops and their original evidence remain intact.

L031/L032 fix ordered exact values on every original assignment and retain
the repeated square and every accumulator. L075's existing construction
and audit pay a particular family's separately copied trees. Those facts
are useful conventions and a restricted precedent, not a proof of the
general presentation claim. L037's Hypotheses receive every root, exact
signed nodes, originals/constants and one formal H per AND; E charges
graphs, associations and complete original-axiom dictionaries. It admits
constant edges and unequal path lengths, so no homogeneous-component
normalization is required. Its conclusion is conditional on supplied
data and cannot itself furnish those data.

The uncovered mathematical work is a constant-aware all-root presentation
or direct-graph bound for products and unary complements. A later attempt
must explicitly handle degree-zero constant subgraphs, long signed chains,
shared/repeated operands, D=0, independent outputs and actual T. It may
simplify constants only through justified formal F₂ identities. Neither
Boolean idempotence nor cancellation-based semantic degree may substitute
for the saved syntactic degree. No occurrence estimate, general data
construction or new lemma is derived in this literature turn.

Continue only on a proof of one fixed polynomial in T+D+2 paying all
separate graphs, complete repeated dictionaries, associations and bit time,
with both zero-H identities and every L037 promise; a partial result must
name its remaining case. Abandon this criterion on a qualifying obstruction
within the exact saved syntax and degree convention. An arbitrary
arithmetic circuit or exponentially large D does not suffice. Repeated
failure without new evidence calls for a different independently testable
target under the shared bounded-exploration rules.

Essential prospective inputs remain L031/L032/L075's exact-value/encoding
conventions, L037's complete receiver and the cited conversion; L019/L033
and Attempts 016/020 are comparisons. No cross-notebook input is used.
Polynomial D for arbitrary ER, alternative reduced-value witnesses,
formula-only bounds, W/V/U, every-certificate hardness and unrestricted
SAT transfer remain unproved. Mathlib coverage is not checked; this does
not assert absence. The newly completed EXPLORE assessment receives the
supervisor's separate next-turn approval before mathematical invocation.
