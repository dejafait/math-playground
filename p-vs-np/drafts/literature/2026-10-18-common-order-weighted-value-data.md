# Common-order weighted value graphs — source comparison

TARGET: Construct or obstruct polynomial-full-bit Boolean/commutator-only L037 data from supplied faithful common-order layered affine-F₂ value ABPs with one original variable per level.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 328 ran six target/stronger-result queries recorded below, inspected weighted-roABP correction and two recent obstruction leads, and checked the named local results/failures. No inspected full match or applicable obstruction was established; no novelty inference follows.
SOURCE_EVIDENCE: Read FSTW ToC 17(10) (2021), Lemma 3.6, Facts 3.8/3.12 and Propositions 4.5–4.6 with complete correction proofs, pp.19–21,30–32; inspected Andrews et al. ITCS 2026 article 9 Theorems 1–3 and HLT arXiv:2605.04544v1 Definition 3/model and Theorem 1 statements only. Reused assessed LTW/Raz–Shpilka component coverage; URLs and scopes below.
COMPARISON: Known commutative weighted-roABP corrections do not supply ordered free-ring ABP witnesses. L029 covers particular atom lists, not arbitrary transitions; L035/L036 supply commutators and Booleanity, not independent faithful AND defects. Recent obstructions have different output/model hypotheses.
GAP: Construct or obstruct ordered local-product corrections and explicit affine graphs with one aggregate polynomial in Q=2+T+E_val, retaining supplied unsigned roots, exact signs, both formal H identities and all copying/dictionaries. No weighted construction or bound is proved here.
REASON: Essential source comparison for the unchanged TARGET now supports one bounded mathematical attempt. EXPLORE approves testing the documented difference, not a positive result or certified originality; no lemma or mathematical script is written in this literature-only step.
SCOPE: Supplied valid ER proof and explicit faithful x-only layered value ABPs in one common original-variable order; affine labels a+b*y_k over F₂ only between consecutive levels, scalar terminal data, arbitrary finite width, exact original/constant/signed-root associations, complete input encodings. No availability promise for arbitrary ER or restriction of assignments to models of the original CNF.
LITERATURE_REASON: Step 327 changed deterministic diagrams to weighted ordered graphs; that changed hypothesis had no ready source comparison at invocation start.

The main gap is still unrestricted SAT decision/separation. The proposed
intermediate target asks whether the formal-witness component can receive
weighted ordered graphs directly. If it can, L037 could receive data
under this representation promise without first converting the supplied
graphs to small deterministic diagrams. This is only a proposed use,
not a claimed extension or a route to arbitrary ER data.

Measure resources in Q=2+T+E_val, where E_val pays the complete supplied
collection, all roots, states, edges, weights, original names, orders
and dictionaries. The desired output has one fixed polynomial bound in
Q for aggregate full bits, bit time and pre-substitution degrees. Both
formal H identities and the Boolean/commutator-only restriction are
essential. Supplied fidelity is a hypothesis; deciding it is not a
promised part of the construction. Exact complements and original/base
roots remain required. Width is charged through E_val, not presumed
bounded independently of the input. Do not infer a polynomial Q in T
for arbitrary ER proofs.

Prospective local inputs/comparisons are L026's exact suffix identities
and ordered-multilinear bridge, L071's audited graph component, L037's
full receiver, and L029's existing sums of atomic diagrams. L084 is the
completed deterministic family application, not a proof of the changed
scope. Check the exact L029 generality before creating any new lemma.
L030 and Attempt 019 are representation limitations to compare with the
proposed promise, not reasons to claim universality. Attempt 020 forbids
an unsupported arbitrary circuit-to-ABP conversion; Attempt 029's
unsimplified structural stop remains in force on its own stated target.
No cross-notebook input is proposed. Matching Mathlib coverage is not
checked.

The separate review must search standard weighted/read-once oblivious
ABP terminology, exact local-witness claims, stronger existing results
and known obstructions, then inspect primary hypotheses and essential
proof cases. Import a matching result, specialize only a documented
difference, or record a concrete obstruction. Do not infer novelty from
an unsuccessful search or use generic Boolean equivalence to identify
arbitrary free polynomials. Continue to research only with a ready
assessment identifying the exact remaining difference and paid input
model. Abandon or redirect this target if it duplicates an established
local statement or an essential failed premise prevents the desired
polynomial bound. No new mathematics is asserted in this proposal.

## Step 328 — completed source review

The preceding proposal's initial review requirement is discharged by this
literature-only comparison. The TARGET is unchanged. No weighted recurrence,
new identity, graph construction or mathematical bound is proved here.

**Main gap and exact statement.** On 2026-10-18 reopened the [Clay page](https://www.claymath.org/millennium/p-vs-np/)
and linked [Stephen Cook description, §1, pp.1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf).
The page says unsolved; the linked 12-page description asks equality of
deterministic and nondeterministic polynomial-time languages, equivalently
polynomially bounded witnesses checked by one polynomial-time relation.
The upload path is not a revision date. This agrees with the local target.
The intermediate supplier below leaves unrestricted SAT decision/separation open.

**Discovery queries actually run:**

- `read once oblivious algebraic branching program multilinearization Boolean axioms IPS Forbes Shpilka Tzameret Wigderson`
- `"noncommutative" "read-once" "Boolean" IPS witness`
- `"Hadamard product" "read once oblivious" ABP Boolean`
- `"noncommutative" "multilinearization" "branching" proof`
- `"read-once oblivious" "commutator"`
- `"algebraic branching" "Boolean axioms" "witness"`

Snippets located primary sources only. Unrelated PIT/set-multilinearization
hits are not inputs. A failed search establishes neither novelty nor impossibility.

**Closest weighted result.** [Forbes–Shpilka–Tzameret–Wigderson,
*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*,
Theory of Computing 17(10), 2021](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf),
Lemma 3.6/Fact 3.8, pp.19–20; Fact 3.12, p.21;
Propositions 4.5–4.6 with complete proofs, pp.30–32.
Proposition 4.5 assumes a supplied width-r common-order roABP of individual
degree d over any field. It gives explicit width-r multilinearization and
Boolean-ideal coefficients in polynomial resources in r,n,d. Its proof
divides univariate transition matrices by their Boolean polynomial and
telescopes; extracting that polynomial to the right uses commuting entries.
Proposition 4.6 additionally assumes unsatisfiable axioms and supplied
same-order coefficients whose axiom combination is one modulo the Boolean
ideal. Its proof multilinearizes coefficients, forms same-order products,
applies Proposition 4.5 and checks both IPS identities. F₂ is allowed
without a field-size assumption. This does not supply a free-ring witness.
Affine degree-one input labels do not authorize reordering operand products.
No reproof of this known commutative theorem is proposed.

**Component coverage reused.** The ready assessments
`drafts/literature/2026-10-05-obdd-reduced-data.md`,
`drafts/literature/2026-10-05-hwb-boolean-only-relations.md`,
`drafts/literature/2026-10-07-affine-abp-boolean-witnesses.md` and
`drafts/literature/2026-10-07-alternative-affine-abp-certificate-assembly.md`
already inspect [Li–Tzameret–Wang, arXiv:1412.8746v4,
11 September 2015, Lemmas 3.6–3.7, pp.17–18](https://arxiv.org/pdf/1412.8746v4)
including constant/variable, addition, product and context cases, and
[Raz–Shpilka, author-hosted 16-page manuscript, Lemma 2 Step 1,
p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
The former supplies ordered formula commutation with cost in written trees;
the latter supplies disjoint graph sums/products. Their scopes are unchanged
and are reused without refreshing those sources. Neither converts arbitrary
shared circuits to ABPs. Later applications must charge complete operands
and framing. Known operations need applicability arguments, not reproofs.

**Recent obstruction leads, statement-level comparison only.** [Andrews,
Armand, Dwivedi, Hansen, Limaye, Srinivasan and Tavenas,
*On Closure Properties of Read-Once Oblivious Algebraic Branching Programs*,
ITCS 2026, article 9](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.9/LIPIcs.ITCS.2026.9.html),
§1.1 Theorems 1–3, printed pp.3–4: factor non-closure is all-field;
the two symmetric-composition statements assume characteristic zero.
These operations/output restrictions differ from this target. Proofs and
full version arXiv:2509.10725 were not inspected or invoked. No factor
extraction, symmetric inversion or growing-power closure is a proposed premise.

[Hakoniemi–Limaye–Tzameret, *Hard CNF Instances for Ideal Proof Systems*,
arXiv:2605.04544v1, 6 May 2026](https://arxiv.org/html/2605.04544v1),
§§1.1,2.4: inspected Theorem 1's stated all-field/any-order roABP-IPS_LIN
lower bound and Definition 3 with its following coefficient model.
Its proof and formal Theorem 18 were not read; no lower bound is imported.
Requested H and L037 output are general affine free-ring ABPs, not
coefficients constrained to remain read-once oblivious. That receiving-model
hypothesis cannot be imposed silently. Requiring ordered output coefficients
would change the target and need another review.

**Local overlap and failures.** Read L026's complete suffix/product/sign/
injectivity proof, L029 through its fixed-root bridges and local-product
construction, L071's post-compilation graph component and L037's input
promises. L026/L071 use deterministic two-successor diagrams. L029's theorem
concerns fixed HWB roots and explicit polynomial atom lists; it does not
supply such a decomposition for arbitrary weighted graphs. No efficient
conversion to those atoms or deterministic diagrams is assumed.
L035/L036's hypotheses and conclusions already cover x-only graph
commutators and Booleanity; they do not identify an independent faithful
output with its operand product. L037 receives, rather than supplies,
the desired local identities. L084's reviewed deterministic specialization
is retained from the supplied overview; its proof was not reread.

Read Attempts 019/020/029 and L030's exact hypotheses/conclusion.
Attempt 019 stops universal small deterministic OBDD availability;
Attempt 020 stops generic degree-only same-output circuit-to-ABP conversion.
This promise starts with supplied graphs and asserts neither premise.
L030's stated model is a common-order sum of deterministic diagrams;
no extension of its lower bound is proved here. Attempt 029's structural
stop remains in force on its unsimplified promise. None of these records
establishes or refutes the present supplier statement.

**Bounded test and downstream use.** Attempt an ordered paired-state
local-product correction for arbitrary affine transitions and scalar
terminals. L026's identities/ordered-multilinear bridge and L071's
one-way correction regions are design leads, not already proved weighted
recurrences. A successful restricted supplier could feed L037 without
first converting the weighted inputs to deterministic diagrams.

Essential continuation inputs are L026, L029, L035, L036, L037 and L071's
graph component within its stated scope. Retain supplied unsigned
polynomials, actual original/scalar roots and exact signed wrappers 1+r;
terminal complementation for deterministic diagrams is not an imported
weighted-graph rule. Each original occurs at most once in the shared
level order. Higher-degree labels or repeated-variable levels are outside
SCOPE. Fidelity is supplied on all original assignments, not merely models
of the CNF; no promise-verification algorithm is required.

The required threshold is one fixed polynomial in Q=2+T+E_val for full
output bits, deterministic bit time and degrees before axiom substitution.
Prove H(x,0)=0 and H(x,A)=r_i+r_a r_b formally, using only original
Boolean/pair-commutator placeholders. Pay every root, local block, state/
edge pair, repeated dictionary, name and copy without path unfolding or
truth tables. Include cancellation, parallel/zero edges, absent paths,
constants, signs, repeated operands, scalar-only inputs and unused roots.
No weighted recurrence or exponent is asserted by this review.

Continue if a rigorous recurrence and acyclic graph realization meet that
threshold, or a partial component resolves a named independent obligation
with a concrete remaining test. Abandon this mechanism if an essential
step forces unbounded copying, a large deterministic conversion or an
uncorrected factor move. Search non-matches alone are not stop evidence.
Arbitrary ER value-graph availability, formula-length-only bounds and
unrestricted SAT decision/separation remain independent gaps.

All essential component coverage is available. Mathlib matching coverage
is **not checked**, not absent; no cross-notebook input is used. Screenshot
calls yielded no visible page content, so reading claims rely on primary
text and the reused assessments. This LITERATURE / literature_comparison /
NOVELTY_UNCHECKED step is EXPLORATION and uses no mathematical exploration
attempt. The unchanged TARGET is ready for one bounded research attempt
using this saved EXPLORE assessment, without certified originality.
