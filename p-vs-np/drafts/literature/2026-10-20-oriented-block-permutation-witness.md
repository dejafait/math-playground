# Independently oriented block permutations — completed source comparison

TARGET: Test whether Boolean-zero products of two dense width-three OBDDs whose orders permute at most floor(log₂ M) common contiguous blocks, allowing independent reversal inside each block, admit polynomial-full-bit original-fg witnesses in the unchanged pre-witness M.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 364 searched OBDD block permutation/reversal conjunction, noncommutative IPS block witnesses and read-once block reversal; inspected the local nonzero component interfaces and reused the ready GKST/GKS comparison. Queries, inspected sources and unused leads are distinguished below; no full-target theorem was found.
SOURCE_EVIDENCE: Reused L092/L093 assessments; reread LTW arXiv:1412.8746v4 Lemmas 3.6–3.7 pp.17–18 and Raz–Shpilka author manuscript Definition 1 p.4/Lemma 2 Step 1 p.5. Inspected L092 boundary factors, L093 parts 1–3, L035 hypotheses, L085 weighted recurrence and L026 injectivity; these supply components, not the combined theorem.
COMPARISON: L092 fixes internal orders; L093 has opposite whole orders. Its reversal correction precedes and does not use Boolean vanishing; L085 retains a possibly nonzero paired residual. These are relevant nonzero interfaces, whereas neither whole zero-product theorem can be invoked separately on arbitrary blocks.
GAP: Test composition on independently oriented boundary factors, including singleton blocks and scalar endpoints; establish both original-fg identities, a common-order global residual and one polynomial full-bit/time/path-degree bound in unchanged pre-witness M, paying the supplied annotation.
REASON: The changed-hypothesis source comparison is now complete enough for one bounded proof attempt on unchanged TARGET; no essential inaccessible theorem is needed. The new composition and ledger are not derived or approved as correct here.

LITERATURE_REASON: Independent internal block reversals change L092’s hypotheses; the saved REVIEW_REQUIRED target required a separate comparison of nonzero reversal and boundary interfaces.
SCOPE: Exactly TARGET with the supplied common partition, distinct full orders, original B and pre-witness M; source readiness permits a proof attempt, not a theorem import.

## Retained proposal at turn start

The following proposal and its pending obligations are preserved as the starting record. Its requests for source review are discharged by the completed comparison below; they do not request another approval-only literature turn.

Main gap: unrestricted SAT decision/separation. The proposed intermediate
target would cover supplied order pairs beyond either unchanged internal
block order or complete reversal alone. Its potential downstream use is
an explicit restricted original-fg witness interface with a growing
number of blocks. This does not supply arbitrary-order W₂, general ER
data, formula-length-only bounds or a SAT transfer.

Retain L087's distinct supplied orders, dense width-at-most-three inputs
on the same complete named alphabet, q≥2, Boolean-zero fg promise,
original B/placeholders and pre-witness M. Require an explicitly supplied
partition into nonempty sets, each contiguous in both orders. Each block
retains or reverses its first-order internal sequence in the second
order; the sequence of blocks may be permuted. Keep M exactly as in
L087: the assessment must check the complete partition/orientation
annotation cost against this M, without redefining M or its cutoff.
Do not infer a polynomial encoding bound without checking it.
Keep all unreachable states, duplicate successors and scalar terminals.

Essential proposed inputs are L092's boundary-state and independent-copy
construction, L093's now-audited reversal correction and normalization,
L035's original-only commutator graph, L085's paired component, L026's
ordered injectivity and L087's original input convention. Read only
their needed ranges during review. No cross-notebook theorem is proposed.
The step-363 audit changed none of these mathematical statements.

The whole L093 theorem assumes a Boolean-zero product. Individual block
factors in a boundary expansion have no such premise supplied here, so
whole-theorem blockwise invocation is not licensed. The next review must
compare the exact nonzero-segment component interfaces and endpoint
hypotheses before approving a proof attempt. No composition identity,
resource estimate or correctness claim for the new target is established
in this proposal. The original cutoff must be evaluated before witnesses,
with all boundary choices, independent copies, dictionaries, time and
path degree charged if mathematics is later authorized.

Search exact and standard block-reversal/order-permutation witness terms
and inspect the relevant primary statements, reusing existing component
assessments where hypotheses agree. Attempts 018/030 remain unchanged:
this changed-hypothesis review is not another approval of L093, and it
does not assert universal common-order value availability. The optional
blocked automata scan is not an essential input. Full matching Mathlib
coverage remains not checked, with no absence or novelty claim.

Continue only after source comparison supports a concrete bounded test
of the original-fg interface with one polynomial in original M. Record
a precise mismatch if local components require an unavailable blockwise
vanishing premise, incompatible endpoints, unbounded enumeration or
placeholder-bearing commutator operands. A favorable source assessment
must be saved and separately approved before a mathematical attempt;
this proposal neither performs nor approves that attempt.

## Completed comparison — step 364, 2026-10-20

The exact main gap remains unrestricted SAT decision/separation. TARGET
is an intermediate restricted witness supplier. Its downstream use would
extend the supplied order-pair coverage, without providing arbitrary-order
W₂, general ER data or a SAT consequence. No mathematics is derived in
this literature step and no new lemma or mathematical script is written.

### Discovery and precise source scope

Queries actually issued: `OBDD block permutation reversal conjunction
noncommutative IPS witness`; `ordered branching programs block reversed
variable orders conjunction polynomial width`; `"noncommutative" "block"
"reversal" "witness"`; `"OBDD" "block" "commutator"`; `"OBDD"
"independent" "reversal" product`; `"blockwise branching programs"
"exchanging" variable orders blocks`; `"noncommutative IPS" "OBDD"
reversal`; and `"read once" "block reversal" branching program`.
These bounded searches found no inspected theorem matching TARGET;
this is not evidence of novelty or a claim that no such theorem exists.

Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, arXiv:1412.8746v4 (11 September 2015), Lemmas 3.6–3.7,
printed pp.17–18 ([primary PDF](https://arxiv.org/pdf/1412.8746v4)):
reread both statements and their context/product/sum proof cases.
Lemma 3.7 receives two noncommutative formulas P,Q and supplies a
commutator witness, zero at zero placeholders, for PQ−QP, with size
at most |P|²|Q|². F₂ is an allowed specialization and subtraction is
addition. Lemma 3.6 handles one commutative rewrite inside a formula.
Neither yields a bound in arbitrary supplied graph size by unfolding.
Use L035's existing graph result for that difference; no reproof of
the formula theorem is justified or proposed.

Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative
Models*, undated 16-page author manuscript, Definition 1 p.4 and
Lemma 2 Step 1 p.5 ([primary PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)):
reread ordered path semantics and the scalar/variable leaf, parallel-sum
and sequential-product cases. Definition 1 itself uses homogeneous linear
labels, single endpoint layers and a layered DAG. The intermediate model
in Step 1 permits constants and unlayered graphs. Lemma 2's full conversion
assumes a zero free term; that conversion and its PIT are not inputs to
this target. Only explicit disjoint composition is reused, with endpoint
handling still a local obligation.

Reuse the completed stronger-result comparison in
`drafts/literature/2026-10-19-logarithmic-block-permutation-witness.md`:
GKST CCC’15 Theorems 3.1–3.2 concern commutative sum-PIT, not formal
Boolean-ideal witnesses; GKS ToC 13(2) (2017) Theorem 3.6 has an
inapplicable characteristic restriction, and Theorem 4.9 requires
small representations in every order. Adding oriented blocks does not
remove those mismatches. Direct primary references and inspected cases
are retained there. Bryant §4.3 coverage is reused through the same
assessment for Boolean common-order Apply only.

Uninspected leads are not theorem inputs. Koseki–Takenaga, *The Relation
between Variable Order and Computational Power of Blockwise Branching
Programs*, IPSJ AL 2004(34), pp.89–94
([repository](https://ipsj.ixsq.nii.ac.jp/records/31869)), appeared in search;
only its repository metadata/abstract was available and a direct open
failed. No theorem statement or proof was read. The Buss-hosted
*Lower Bounds on OBDD Proofs with Several Orders* PDF opened but text
finds and the selected first-page screenshot failed; no mathematical
passage was inspected or used. Search also surfaced 2026 roABP closure
and roABP-IPS lower-bound leads without inspected relevant statements.
These remain optional, unused leads, not asserted matching results or
essential blockers. The previously parked automata lead remains parked.

### Local interfaces, duplicates and recorded stops

L092's all-boundary expansion receives segment roots at arbitrary chosen
boundary states, with indicator scalar endpoints at cuts and original
scalar endpoints on the last block. Its canonical proof explicitly
retains unreachable roots and no-accepting-path factors. It bounds the
boundary tuple pairs by 9^(b−1) and already pays the unchanged-order
partition annotation separately from M. The new orientation annotation
and its parsing/copying cost must still be bounded in the proposed proof;
no revised definition of M or cutoff is permitted.

L093 parts 1–2 define a reversed original-only graph for every suffix and
a correction J with J(0)=0 and J(B)=g+rev(g). These are existing written
identities, not results derived here. Their proof precedes use of the
Boolean-zero promise. Part 1's scalar-terminal absorption supplies a
weighted layered graph; determinism is not a receiving hypothesis.
Applying this component to normalized boundary factors, especially
length-one factors, is a specialization obligation, not an invocation
of L093's whole theorem or a new result of this review.

L085's weighted paired recurrence states W(0)=0 and W(B)=uv+P for its
same-order original-only operands. P may be nonzero. The fidelity-to-ER
conclusion of its whole theorem is unnecessary for that component.
L035 explicitly receives original-variable affine DAGs with constants,
no-path cases and arbitrary endpoints, and needs no semantic-zero
promise. It does not accept already constructed placeholder witnesses
as operands. L026 injectivity is restricted to a single increasing
multilinear order. These precise receiving scopes remove the need for
an *assumed* blockwise zero promise, but do not establish composition.

L088–L090's adjacent-swap, move and deletion promises do not cover the
new hypothesis in general. L091/L092 retain internal orders and L093
reverses the whole list. No duplicate full theorem was identified in
those canonical statements. Attempts 018/030 were read: ready coverage
must lead to mathematics, and universal faithful common-order graph
availability remains obstructed. The present target assumes the two
input diagrams and makes no availability claim. Both stops and all
unfinished work drafts are preserved; no cross-notebook input is used.

### Bounded continuation and abandonment test

Approve EXPLORE for exactly TARGET, not correctness of the proposed
combination. Essential inputs are L092, L093, L035, L085, L026 and
L087. A proof attempt must explain how nonzero oriented block corrections
are received, retain original fg and the original B dictionary, and use
Boolean vanishing only on a demonstrated single-order global residual.
It must pay every independent boundary choice, graph/context copy,
annotation, dictionary, bit operation and accepting-path degree against
original M. Singleton blocks, unreachable roots, duplicate successors,
zero scalar terminals and cancellations must remain covered.

Continue if those interfaces admit an explicit acyclic construction and
one fixed polynomial in M under b≤floor(log₂ M). Abandon this composition
if it needs an unavailable blockwise vanishing premise, unsupported
endpoints, placeholder-bearing commutator operands, path enumeration or
a superpolynomial independent-copy bound. Preserve any failing case
rather than adjusting M or claiming arbitrary-order coverage. No bound,
new identity, implementation or combined theorem is established today.
Full matching Mathlib coverage remains not checked, with no absence claim.
