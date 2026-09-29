# Polynomial output covers for a two-round KPT strategy

TARGET: Review whether a polynomial list of complete second-round outputs with EF-provable coverage on first-round solver counterexamples can support the two-round KPT transfer without a canonical SAT selector.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched KPT finite-range and nonadaptive witnessing, polynomial candidate lists and EF antichecker transfers; followed the parallel-witnessing reference to Cook–Thapen and compared both Pich–Santhanam versions. Queries and inspected statements are recorded below.
SOURCE_EVIDENCE: https://arxiv.org/pdf/cs/0409015v1, Theorem 7 and proof, pp. 15–16 (author-manuscript Theorem 4.3, pp. 12–13); https://arxiv.org/pdf/2602.19934v1, Definition 1.2, Theorems 1.4 and 1.6–1.8, pp. 6–8, and Definition 4.7 / Theorem 4.11 with proof, pp. 23–24; https://arxiv.org/pdf/2312.08163v1, §3, pp. 19–20; https://eccc.weizmann.ac.il/report/2023/199/download/, §4, Theorem 10 and following discussion, pp. 25–26. Prior substitution/CF–EF sources are reused.
COMPARISON: Known parallel witnessing gives polynomially many candidates at a fixed interaction history, retaining earlier counterexamples; it supplies neither a complete range cover independent of the first free assignment nor EF proofs of such coverage. The closest EF transfer keeps a provable generator premise. No inspected theorem settles the proposed conditional cover transfer.
GAP: Test the sufficiency of supplied complete-output covers with uniformly polynomial EF coverage proofs; obtaining those covers and proofs, the existential arithmetic premise, and a superpolynomial EF lower bound remain separate gaps.
REASON: The bounded source search supports a focused conditional proof-obligation test, not a direct import or an impossibility claim. Import witnessing/substitution and investigate only the cover-specific difference in a later research turn; no derivation is performed here.

## Proposed scope for the source comparison

Keep a supplied two-round strategy, a fixed polynomial output-size bound, and the hypothetical SAT algorithm as conditional inputs. For each length and fixed first challenge formula, fix the earlier comparison and certification data. The proposed list contains complete possible second-round tuples, including the solver circuit, both lists, pairing relation and output-format data. Its total binary length must have one polynomial bound.

The proposed coverage proof would say that, whenever the first solver has a genuine satisfying-assignment counterexample, the second output equals a member of the supplied list. Ask whether known results give such lists and polynomial EF proofs of that implication, or provide a more useful equivalence notion with an equally explicit proof. Arbitrary polynomial-time output maps need not have polynomial range; no generic range bound is presumed. Counting only the solver outputs while discarding certification data is not an adequate match.

The plausible downstream use is polynomially many proof cases whose candidate descriptions no longer depend on the first free assignment. This is a proposed use, not a proved transfer. The screen must check proof length, all remaining universal variables, the theory strength and how the list is supplied. Merely asserting a list for every assignment or an exponential enumeration does not meet the threshold. The existential arithmetic premise and a superpolynomial EF/ER lower bound remain separate unresolved inputs.

The earlier direct-minmax and canonical-recovery obstructions remain relevant. Do not reprove the guard equivalence or count another description of that stop as new evidence. The source comparison should select an exact conditional statement worth testing or reject this cover mechanism on a specific bound or formalization mismatch.

## Completed source search, 2026-09-27

This review preserves the saved TARGET verbatim and completes its previously missing assessment. The [source note](../../foundations/11-kpt-output-covers.md) records named statements and version details in the standard format. No lemma, mathematical script, output cover, or new transfer proof is produced.

Queries included:

- `KPT witnessing nonadaptive finite list polynomial range extended Frege`
- `Pich Santhanam 2312.08163 antichecker existential witnessing assignments`
- `bounded arithmetic witnessing polynomially many witnesses Herbrand disjunction KPT`
- `"KPT" "nonadaptive" witnessing`
- `"Parallelism and Adaptivity in Student-Teacher Witnessing"`
- `"witnessing" "polynomial" "finite list" arithmetic`
- `Cook Thapen "strength of replacement" pdf`
- `"KPT" "range" "witnessing" Frege`
- `"Student Teacher" "non-adaptive" witnessing`
- `"KPT" "finite range"`
- `"KPT" "polynomial" "list" "Frege"`
- `"anticheckers" "existential" "witnessing"`

The exact-range searches returned no full matching theorem. That is a bounded-search report, not evidence of originality. Unrelated uses of “KPT” were discarded. Primary papers, rather than search snippets or secondary summaries, support the comparison.

| Source / material actually read | Role and limit |
| --- | --- |
| Cook–Thapen, arXiv:cs/0409015v1, §4 definition of BB and Theorem 7 with proof, pp. 13–16; corresponding author-manuscript Theorem 4.3, pp. 12–13 | Closest finite-list witnessing theorem. The later functions still take earlier counterexample sequences. The α(s)ʳ bound controls a list at a history, not the union over histories. |
| Ježil–Tsintsilidas v1, Definition 1.2 and Theorems 1.4, 1.6–1.8, pp. 6–8; §4.1, pp. 21–22; Definition 4.7 and Theorem 4.11 with proof, pp. 23–24 | Explicit parallel-query model and generalized witnessing. Read the separation statement to check its assumptions; its proof is not used. This is additional source coverage beyond the earlier canonical-selector assessment. |
| Pich–Santhanam arXiv v1, §3, Theorem 7 and discussion, pp. 19–20; ECCC 35-page version, §4, Theorem 10 and discussion, pp. 25–26 | Both give the same relevant generator/interactive distinction. The ECCC PDF has a 9 December 2023 cover date; its numbering must not be conflated with arXiv v1. |
| Pudlák Lemma 2.1 / Fact 1 and Jeřábek Lemmas 2.4–2.5 | Reused the sufficient [prior assessment](2026-09-26-current-target.md) and [source note](../../foundations/06-reflection-specialization.md). Substitution and formula-conclusion conversion need no new general compiler. |

The arXiv landing pages listed v1 for each of the two recent arXiv papers. The source record identifies the actual documents read, rather than assuming the ECCC file is a numbered revision of arXiv. The [Clay problem page](https://www.claymath.org/millennium/p-vs-np/) and [Cook's official statement, §1, pp. 1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) were reconfirmed: the target remains ordinary uniform P versus NP.

Cook–Thapen's author PDF had damaged extracted symbols; its readable arXiv counterpart resolved the needed theorem. Direct shell retrieval had a DNS failure, but web text supplied the needed statements and arguments. No essential source selected for this comparison remains unread. Search leads on range avoidance, witnessing flows, and quantified propositional calculus were not inspected as possible full matches and are not inputs. No exhaustive literature claim is made.

## Required bound and exact remaining test

For a fixed strategy and a comparison exponent compatible with the hypothetical SAT algorithm, use one polynomial p for all lengths n and fixed first formulas F. Write B₁ for the first solver, V for the chosen assignment verifier, and U₂(F,y,Cₙ,η₁) for the complete second output with the earlier comparison and certification challenges fixed. The proposed extra premise is a list U₁,…,Uₘ, independent of y and of the second-round universal variables, together with an EF/CF proof of

(V(F,y) ∧ ¬V(F,B₁(F))) → OR_{i≤m} [U₂(F,y,Cₙ,η₁)=Uᵢ].

This is the proposed obligation, not a proved formula family. All tuple bits, lengths, format flags, lists, pairing data and circuit descriptions count. The required bound is on the list's **total binary length plus its coverage-proof length**, at most p(n), uniformly over F and the chosen fixed prefixes. Lists may be supplied nonuniformly for this initial proof-size test; an algorithm producing them is a stronger, separate requirement. No representative-equivalence relaxation has been justified, so the test retains equality of complete tuples.

The inspected witnessing results achieve bounded rounds and per-history candidate counts. They do not achieve this p(n) bound on complete outputs and coverage proofs. A polynomial output length alone is not the required range bound, as already stated in the saved proposal. The source's theorem for one fixed circuit exponent must also not be promoted to a statement defeating all polynomial exponents.

The discriminating test is whether those supplied premises suffice for polynomial EF proofs of arbitrary tautologies through the two-round strategy, with a single polynomial overhead and the checked evaluator identification. Every second-round challenge must remain accounted for. In particular, coverage may be semantically vacuous on an unsatisfiable fixed F, but its short proof is still an input to be justified; external unsatisfiability is not permission to insert such a proof. Do not assume a formal proof of the hypothetical SAT algorithm's global correctness.

Continue only if this conditional test isolates a usable obligation without another uncharged proof assumption. If the case split still requires an unprovided universal recovery proof or superpolynomial total data, record that specific failure. Even a successful conditional transfer would leave cover construction/proofs, the existential arithmetic premise, extension beyond the supplied two rounds, and the required EF lower bound unresolved. It would not resolve P versus NP.

## Decision and relation to prior failures

**EXPLORE.** The proposed cover differs from ATTEMPTS/012's direct minmax import and ATTEMPTS/013's canonical universal recovery. Known list witnessing does not discharge it, and the checked conditional round separations do not forbid it. A bounded conditional applicability test is justified before attempting any construction of covers. The precise test has been screened in the [companion assessment](2026-09-27-kpt-output-cover-transfer.md); its execution is deferred to a later invocation.

This turn imports only known supporting statements by citation. It establishes no result beyond the checked literature and makes no claim of novelty for the unproved conditional target. Outcome: EXPLORATION, with exploration turns used increasing from 0 to 1. This is new theorem-level comparison and a concrete test, not another report of L014's stop decision and not an informative mathematical negative result.

## Mathlib

Coverage: **not checked** for the proposed cover condition, the conditional transfer, or supporting witnessing results. The named theorems above are supporting results, not a full statement match. No library absence or novelty claim is made.
