# One small-support operand — completed source comparison

TARGET: Construct polynomial-full-bit L037 data when every AND definition has at least one operand with syntactic original-variable support size at most floor(log₂(T+2)).
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 299 completed bounded exact/support, Boolean skew, weakly-skew, noncommutative mixed-side and formula/ABP discovery, plus targeted L026/L037/L071/L076/L077 and Attempts 019–020 comparison. No inspected full-statement match; unsuccessful queries do not establish novelty.
SOURCE_EVIDENCE: Read Bryant (1986), author-restored §1 equation (1) and §2 Definitions 1–2, PDF pp.3–4; Raz–Shpilka, undated author manuscript §2.1 and Lemma 2 Step 1, PDF pp.4–5; Limaye–Malod–Srinivasan (2016), §1.2 printed p.3; Arvind–Raja ECCC TR14-028 (2014), §3/Remark 11 p.10. Reuse the assessed L026 formal correction and audited L071 post-compilation graph component.
COMPARISON: Small-cone Boolean representations and paid formula-to-graph conversion are covered components, but L077 needs every whole root small and L076 charges exact D. Mixed-side noncommutative skew circuits do not inherit the commutative skew-to-ABP equivalence; neither that equivalence nor a global support/degree bound covers this target.
GAP: Test polynomial all-root presentation after small-cone replacement, exact signed/ordered local H reception, and one aggregate full-bit/time ledger under the operand-only promise; none is proved for this changed promise in this review.
REASON: Essential component sources are accessible and reusable; a bounded construction test is justified, while no precise citation supplies the whole data package. EXPLORE authorizes that test, not its conclusion or certified novelty.
SCOPE: L037's width-at-most-three signed-AND ER conventions, actual binary T, all definitions including unused ones, both signs, syntactic reachable originals with absent nonextension variables set to zero, and complete original-axiom framing. No semantic-support oracle or whole-graph treewidth promise.

The immediate gap is polynomial-in-T L037 data for general supplied ER;
unrestricted SAT decision/separation remains the main gap. This proposed
intermediate target tests an operand restriction in place of L077's
whole-root restriction. A successful construction would widen the class
received by L037. It would not establish that arbitrary ER admits the
restriction, a formula-only bound, W/V/U, every-certificate hardness or
SAT transfer. No representative, relation, recurrence or new bound for
this promise is derived in step 298.

The next comparison should search the exact statement and standard
skew/weakly-skew circuit and branching-program terminology, distinguishing
Boolean support from formal arithmetic dependence. Reuse existing graph
composition and formal-witness coverage wherever its hypotheses apply.
Inspect any relevant primary theorem's hypotheses and essential cases,
then determine whether it fully covers this data package or only a
component. L026, L071's post-compilation component, L037 and audited L077
are candidate inputs. L076 is a possible comparison or component only
after its exact scope is checked; it is not silently imported here.
No cross-notebook input is proposed. Mathlib coverage is not checked.

Compare Attempts 019–020: unrestricted common-order-width and arbitrary
same-output arithmetic-circuit conversion remain stopped. Merely renaming
either failed premise is not a new mechanism. Check duplicates in the
specific small-support/degree work before proposing any additional lemma.

The discriminating threshold is one fixed polynomial in actual T for
all separately written representatives and formal local witnesses,
including repeated/sign/unused cases, dictionaries and construction time.
Proceed to mathematics only after coverage identifies a concrete way to
test this package. If it requires an unproved general support bound,
Boolean-only equality of arbitrary free polynomials, or an unsupported
conversion, record the precise missing interface and choose or narrow the
target accordingly. An established full match calls for import. This
continuation is a question for a separate review, not self-approved work.

## Completed separate review — step 299, 2026-10-17

The proposal above is retained as its pre-review record. This section and
the updated fields record the separate literature-only assessment. No
representative construction, new identity, copying bound, lemma or
mathematical script was derived or verified in this step.

**Exact main gap.** There is no SAT algorithm or argument excluding all
polynomial-time SAT algorithms here. The nearer representation gap is
polynomial-in-T L037 data for arbitrary supplied ER. The exact TARGET
tests a restricted sufficient condition, not a reduction of arbitrary ER
to that condition. Success would widen L037's input class; formula-only
bounds, W/V/U, every-certificate hardness and SAT transfer remain separate.

**Official target reconfirmed.** On 2026-10-17, retrieved the
[Clay problem page](https://www.claymath.org/millennium/p-vs-np/)
and Stephen Cook's linked
[official description, §1, pp.1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf).
The version is the currently linked 12-page PDF (no revision date asserted).
It defines P by a fixed polynomial worst-case Turing-machine time bound
and NP by a polynomial-time checking relation with a fixed polynomial
witness bound, then asks whether P=NP. This matches the notebook's
foundation; no changed target or prize-adjudication premise is introduced.

**Queries and discovery scope.** Queries actually submitted included
`"arithmetic circuits" "small support" "skew"`,
`"weakly skew" "branching programs" noncommutative circuits theorem`,
`"Boolean circuits" "one input" "logarithmic" "branching programs"`,
`"noncommutative" "skew circuits" "left"`,
`"noncommutative" "skew" "palindrome"`,
`"small support" "branching programs" circuit`,
`"Boolean circuits" "small support" "formula"`,
`"circuits" "one operand" "support" "branching"`,
`"skew" "circuits" "AND" "NOT" "formulas"`, and
`"noncommutative" "small-support" circuit`.
Many hits concern pseudorandom-distribution support, commutative circuits,
or rational functions, rather than this syntactic-support data package.
Only the primary passages specified here are theorem-level evidence.
Uninspected discovery leads include Jansen–Rao's *Simulation of
Arithmetical Circuits by Branching Programs with Preservation of Constant
Width and Syntactic Multilinearity* and Arvind–Joglekar–Raja's
*Noncommutative Valiant's Classes: Structure and Complete Problems*
(arXiv:1508.00395). Neither abstract is used as a theorem; neither is an
essential source for the bounded paid-formula test selected here.

**Inspected representation component.** Bryant,
[*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE TC
35(8), 677–691 (1986)](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
author-restored 28-page file, §1 equation (1) and §2 Definitions 1–2,
PDF pp.3–4, gives ordered Shannon decomposition, terminal constants and
assignment-path semantics in a shared input order. This is Boolean
representation coverage. It supplies neither a formal equality between
arbitrary free polynomials nor the H witnesses. Reuse L077's audited
small-cone table coverage; application to selected cones and consistency
with every actual signed operand still require an applicability argument.

**Inspected ordered graph component.** Raz–Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
undated 16-page author manuscript, §2.1 and Lemma 2 Step 1, PDF pp.4–5:
the inspected leaf, parallel-sum and ordered-serial-product cases convert
an already written formula to a nonlayered graph with constants and at
most s+1 vertices. They preserve the left/right order over any field,
including F₂. The complete lemma's later homogeneous-component conclusion
assumes zero free term; that restriction is not needed for Step 1 alone.
This is an import, not a result to reprove. It does not pay an unprovided
formula unfolding of a DAG; any such presentation bound is the remaining
local question.

**Inspected skew obstruction and stronger-model comparison.**
Limaye–Malod–Srinivasan,
[*Lower Bounds for Non-Commutative Skew Circuits*, Theory of Computing
12(12), 2016](https://theoryofcomputing.org/articles/v012a012/v012a012.pdf),
§1.2 printed p.3, defines skew multiplication by a scalar/variable operand
and distinguishes its noncommutative power from ABPs. Its cancellation
warning explains why switching multiplication sides can change the
polynomial. The adjacent δ-unbalanced model restricts formal degree,
rather than Boolean support; its stated lower bounds are not imported
as an obstruction for the present gate syntax.
Arvind–Raja,
[*The Complexity of Two Register and Skew Arithmetic Computation*, ECCC
TR14-028, 27 February 2014](https://eccc.weizmann.ac.il/report/2014/028/download/),
§3 and Remark 11, printed p.10, explicitly uses both multiplication sides
in the palindrome example and explains the failed reorientation argument.
These passages confirm the terminology and mismatch already recorded in
the L037 assessment; this is not fresh negative evidence or a new
lower-bound proof. The more general addition gates in those models must
not be silently added to the complement/AND source syntax.

**Exact local comparison.** L076's Hypotheses and initial proof show exact
unreduced values with cost polynomial in T+D; no polynomial D in T is
available under the changed promise. L077's Hypotheses, formal-reception
section and step-298 audit receive whole-root support bounds. The changed
target therefore cannot be called an application of either whole theorem.
L026's ordered representative, signed complement, corrected product and
increasing-multilinear identification are available conditional interfaces.
L071's explicit value/K/W/P graph construction and audited degree cases
realize those particular recurrences after diagrams are supplied. Reusing
that component does not delete treewidth from L071's whole theorem.
L037's Hypotheses require every representative and both H identities,
with degree and complete aggregate encoding charged; its receiver does
not construct missing data.

The prior small-support assessment records the older logarithmic-support
lead and the inspected completion proposition. The present bounded local
search found no completed one-small-operand theorem in those assessments,
L076/L077 or their recent histories. This is a duplicate check, not an
originality certificate. Attempt 019/L027 stops a universal common-order
width claim. Attempt 020/L033 stops arbitrary same-output circuit-to-ABP
conversion, with broader addition syntax. Neither stop is removed or
treated as a counterexample to this exact promise. No other notebook was
read or imported. Mathlib coverage remains **not checked**.

**Bounded mathematical test now covered.** Test replacing selected
small-support source cones by explicitly paid ordered table formulas,
then controlling the remaining copying using the actual complement/AND
syntax. This is a proposed proof strategy, not a proved decomposition or
size bound. It must justify that each required local diagram/witness
application has all its operand and output promises; the large roots
must not be assumed to have small common-order diagrams. Preserve actual
left/right factors rather than invoking a mixed-side skew equivalence.
Use L026, L071's audited post-compilation component, L037 and audited L077
as conditional inputs; use L076 only for its checked conventions and as
a comparison unless a precise subcase application is justified.

Continue if one fixed polynomial in actual T pays every independently
written representative and H, pre-substitution degrees, restored names,
unused definitions, exact signed roots, repeated/complementary operands,
empty supports, complete repeated dictionaries and deterministic bit
time, with H(x,0)=0 and H(x,A)=r_i+r_a r_b formally. Do not spend the
attempt reproving standard graph composition. An informative partial
result may isolate a remaining interface without claiming the package.
Abandon this particular mechanism if its presentation or witnesses need
unbounded recursive copying, general circuit-to-ABP conversion, an
unproved global degree/support/width bound, a semantic oracle, or Boolean
agreement outside the ordered multilinear subspace. A new obstruction
must meet the actual source syntax; the existing palindrome warning
alone does not refute the target.

Decision EXPLORE permits one subsequent mathematical attempt on the
unchanged exact TARGET, under the supervisor's approval routing. The
literature outcome is EXPLORATION / NOVELTY_UNCHECKED: coverage was
completed, but no new mathematical result or certified novelty was
established. No mathematical exploration allowance was spent.
