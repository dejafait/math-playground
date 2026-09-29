# Feasible antichecker generation: completed source comparison

TARGET: Review whether Lipton–Young's small-support minmax theorem supplies the polynomial-time, S^1_2-provable solver-or-antichecker generator required by Pich–Santhanam's arXiv:2312.08163v1 Theorem 3, checking its formal Theorem 7.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched small-support minmax, feasible anticheckers, generation and bounded arithmetic; followed the original theorem, its algorithmic sequel and later formalization references. Queries, versions and inspected portions are listed below; no full matching generator theorem was found.
SOURCE_EVIDENCE: https://www.cs.ucr.edu/~neal/Lipton94Simple.pdf and https://arxiv.org/pdf/cs/0205035v1, Theorems 2, 6, 9–10 and Corollary 8; https://arxiv.org/pdf/2312.08163v1, Theorem 7 and proof, pp. 19–20, plus pp. 5–6, 9 and 11; https://arxiv.org/pdf/cs/0205036v1, oracle model and Table 1, p. 2, and §4/Figure 1, pp. 4–5. These portions were read, with further comparisons below.
COMPARISON: Lipton–Young supplies small anticheckers under a larger circuit lower bound, existential sampling circuits and constructions using Σ₂ resources; Young's greedy construction requires an optimization oracle and explicit weight updates. These do not supply Theorem 7's polynomial-time solver-or-antichecker function, assignment pairing and S^1_2 proof.
GAP: The missing objects are a single uniform generator for the disjunction at every length and the required arithmetic proof. Set size is not the missing bound. The transfer remains conditional on an EF lower bound and gives only a fixed circuit exponent per k.
REASON: Stop the direct minmax-to-generator import on newly read theorem-level evidence, while preserving the unresolved uniform P-versus-NP target. Any repair must address construction and formal certification; another existence proof would duplicate known mathematics.

## Scope and test

The exact saved target is preserved above. The main gap is a polynomial-time SAT algorithm or an unconditional exclusion of all such algorithms. The proposed intermediate input is the generator premise of the conditional EF transfer. Its circuit scope is stronger than the notebook's uniform target; no equivalence is asserted.

The continuation test was a known construction meeting the polynomial-time, output and S^1_2-provability requirements, or a specific residual obligation worth a bounded test. The direct import fails this test. The [source note](../../foundations/09-antichecker-existence-and-generation.md) gives the precise named statements and qualifications in the notebook's standard format. No mathematical construction or derivation is performed in this turn.

Even a full match would leave a superpolynomial EF/ER lower bound missing. L013 controls overhead in the length of a supplied soundness refutation; it still gives no bound on that length. One fixed k in Theorem 7 would not exclude all polynomial circuit sizes or resolve P versus NP.

## Discovery and sources inspected

Queries used on 2026-09-27 included:

- `Lipton Young Simple strategies for large zero-sum games applications complexity theory antichecker theorem pdf`
- `"antichecker" "generator" "provable"`
- `"Lipton" "Young" "anticheckers" "polynomial-time"`
- `"anticheckers" "S_2" minmax`
- `"anticheckers" "APC" "minmax"`
- `"Localizability of the approximation method" anticheckers pdf`
- `Neal Young Randomized rounding without solving linear program minmax games 1995 pdf`
- `"feasible anticheckers" "generator"`
- `"solver" "antichecker" "Pich"`

| Source/version | What was actually read |
| --- | --- |
| Lipton–Young, STOC 1994, pp. 734–740; author-hosted scan and arXiv:cs/0205035v1, 18 May 2002 | Theorem 2 and probabilistic proof; Definition 4, Theorem 6 and proof; Corollary 8; Theorems 9–10 and construction arguments; the statement and proof-omission notice for Proposition 11. The clean arXiv text resolved mathematical OCR gaps in the scan. |
| Pich–Santhanam, arXiv:2312.08163v1, 29 pages, submitted 13 December 2023 | The antichecker specialization and Theorems 2–3, pp. 5–6; feasible-minmax discussion, p. 9; gate-count convention, p. 11; all of §3, pp. 19–20, including Theorem 7, its proof and the KPT dependency warning. The arXiv record lists only v1. |
| Young, *Randomized Rounding without Solving the Linear Program*, arXiv:cs/0205036v1, posted 18 May 2002; SODA 1995 version | Problem/oracle model, game interpretation and Table 1, p. 2; §4, Lemmas 4.1–4.2, construction and Figure 1, pp. 4–5; approximate-oracle statement, Proposition 7.1, p. 8. This checks the constructive sequel, not merely the existence abstract. |
| Müller–Pich, [ECCC TR17-144 revision 1](https://eccc.weizmann.ac.il/report/2017/144/revision/1/download), 60 pages | §4.5, Definition 4.11, Theorem 4.12 and Proposition 4.14 with proof, pp. 45–46; theory-to-proof-system statements 4.1–4.2, p. 38. The exact revision is fixed by its URL; no date was identified in its PDF front matter. |
| Pich, [*Localizability of the approximation method*, author manuscript, June 2024](https://users.ox.ac.uk/~coml0742/papers/approxj.pdf), 30 pages | §4.1, Theorem 7 and the following feasibility discussion, pp. 25–26; reference [11], p. 30. This version's Theorem 7 concerns antichecker fusion and must not be confused with the transfer paper's Theorem 7. |

The [Clay statement](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf), §1, p. 1, was reconfirmed: the target is ordinary deterministic versus nondeterministic polynomial-time decision. No prize-status or search-ranking inference is a mathematical input.

## Size, construction and certification comparison

| Obligation | Available source result | Required difference |
| --- | --- | --- |
| Short list of tests | Lipton–Young Theorem 6 gives a small multiset with a constant error fraction under its displayed hardness condition. | Its bound concerns binary circuit-description size. Retain that convention; a gate-count specialization is not carried out here. |
| Appropriate disjunction | Pich–Santhanam already supplies the nonuniform existence formulation using hardness against size s³ and tests against size s, for s≥n³. | Efficiently choose and output a valid alternative. Antichecker existence is not asserted when an appropriate SAT solver exists. |
| Uniform construction | Lipton–Young's small sampler is existential; its uniform procedures use Σ₂ resources. | A deterministic polynomial-time f with input 1^n alone, for each fixed k. |
| Constructive minmax | Young uses weighted optimization plus updates across the opponent's strategies. | Neither an appropriate optimization oracle nor a compact implementation of all updates for the SAT/circuit game is supplied. Polynomially many rounds is insufficient without these costs. This is a limitation of the cited algorithm's guarantee, not a lower bound on all implementations. |
| Labels and witnesses | A truth-labelled multiset is an existence object. | Theorem 7's A′ and D must assign one y_x to each x, with a universal implication certifying that every satisfiable x has a satisfying chosen assignment. An arbitrary failed assignment cannot supply a sound negative label. |
| Formal certification | The minmax theorem and its algorithmic proofs give no S^1_2 proof of this generator statement. | An external correct function would still need the specified proof. An APC₁ or WF result cannot be silently substituted for an S^1_2 or EF result. |

The strongest existence bound is already adequate in scale: the transfer paper explicitly imports the polynomial-size antichecker consequence. The review obtains **no** new deterministic generation-time bound, formal proof or EF proof-length bound. It is therefore inappropriate to optimize support constants or reproduce the sampling proof as progress on the missing premise.

### Does formal existence eliminate the generator?

The transfer paper itself distinguishes the two. Its §3 says that replacing f by existential quantifiers produces a ∀Σ₂^b statement. Under an additional PV1 proof, KPT witnessing gives finitely many polynomial-time functions whose later outputs depend on prior counterexamples, including satisfying assignments. The text explicitly identifies this dependence as preventing its direct EF-boundedness argument. This is an inspected source warning, not our proof that every possible use of interactive witnesses fails.

The p. 9 minmax discussion likewise presents both feasible counting and removal of the explicit witnessing function as unresolved requirements. It does not report an APC₁ proof satisfying Theorem 7. Müller–Pich Theorem 4.12 restates an existential antichecker theorem for a Σ₀^b-defined predicate, and Proposition 4.14 transfers a conditional hardness statement between Frege formulations. Neither constructs the SAT generator or supplies its arithmetic proof. In particular, the latter is about Frege, not a new unrestricted EF lower bound.

The June 2024 Pich manuscript's feasibility paragraph reports a conditional generator using a one-way function secure against nonuniform polynomial-size circuits and subexponential circuit hardness in E. That paragraph was read, but its referenced cryptographic construction was not audited for the full generator target. It is an **unimported lead** with extra unproved assumptions, not an unconditional replacement. The general warning from L007 against using an assumed secure primitive to obtain an unconditional separation still applies. No theorem about the exact strength or equivalence of these assumptions is claimed here.

Other unread leads are the original KPT paper, the original 1994 technical-report version of Young's greedy algorithm, and proofs of the source's omitted Proposition 11. The later constructive algorithm was inspected directly. None of these unread items is needed to decide whether the named minmax theorem and the inspected construction statements satisfy Theorem 7. No essential source for this completed direct comparison remains inaccessible; the KPT original is required before working on a proposed repair.

## Redundancy and route decision

The prior dreambreaker comparison failed on length/description quantifiers. This review tests a different finite-set mechanism and now closes its direct-import proposal using the original bounds, computational model and full assignment interface. It is new evidence for this particular stop decision, rather than another generic reminder that soundness is missing. The [attempt record](../../ATTEMPTS/012-direct-minmax-to-antichecker-generator.md) preserves the failure.

Do not reprove the existence theorem, assume an efficient hardwired sampler was uniformly found, or assume a supplied SAT oracle is a polynomial-time implementation. The older automatic-transfer stop, L012's polynomial ER refutations and the missing soundness bounds after L013 remain in force. None of the sources supplies a main-goal separation.

**EXPLORE** records the completed search without a matching full generator theorem. The direct import is stopped, and this decision does not authorize a derivation in the same literature turn. The remaining existence-to-witness question has a specific candidate repair: use a hypothetical uniform SAT decider to choose canonical satisfying assignments in a two-round KPT strategy. Its feasibility and formal certification have not been assessed. Only a separate source review is queued in the [new assessment](2026-09-27-canonical-kpt-witness-substitution.md); no substitution or new implication is derived here.

The completed step is LITERATURE / NEGATIVE / NOVELTY_UNCHECKED. Its mathematical inputs are imported citations. The contribution is a documented applicability failure, with no result beyond the checked literature claimed. The exploration count stays at 0; no launcher or research-stop state is changed.

## Mathlib

Coverage: **not checked** for the full generator target or the supporting minmax, antichecker, arithmetic and simulation results. The named statements above support qualified components; no full matching theorem or absence claim is asserted.
