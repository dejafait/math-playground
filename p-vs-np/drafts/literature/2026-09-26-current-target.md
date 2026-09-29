# L011 soundness specialization: literature assessment

TARGET: Construct the specialization from an ER refutation of L011's H_(A,N) to an ER refutation of each length-N CNF F rejected by A, and bound its overhead while retaining short soundness proofs as an explicit hypothesis.
CHECKED: 2026-09-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched reflection/simulation and ER substitution, followed the Pudlak reference to Jerabek and located Cook's original paper; queries and inspected sections are recorded below.
SOURCE_EVIDENCE: https://arxiv.org/pdf/2007.14835v1, Lemma 2.1 and Fact 1, pp. 5 and 9; https://www.karlin.mff.cuni.cz/~krajicek/cookpv.pdf, Definition 5.4 and ER Simulation Theorem 6.8 with simulation sketch, pp. 93 and 95; https://users.math.cas.cz/~jerabek/papers/wphp.pdf, Lemmas 2.4–2.5, pp. 12–14; https://www2.karlin.mff.cuni.cz/~krajicek/defc.pdf, Theorem 2.1, pp. 6–8. The named statements and indicated arguments were read, not just their abstracts.
COMPARISON: The general conditional reflection-to-simulation method is covered; applying it to L011 still requires the evaluator identification, gate-encoding correspondence, and binary proof accounting. This is a specialization of known machinery, not an identified new mechanism.
GAP: Establish the necessary syntactic correspondence for L011's Eval_N and ER convention, then the overhead for a supplied H_(A,N) refutation; polynomial-size refutations of H_(A,N) remain an additional hypothesis.
REASON: Import the standard machinery and restrict subsequent work to its concrete applicability; a semantic equivalence of circuits alone does not meet the source hypotheses, and a general proof compiler would duplicate established work.

## Scope and discriminating test

This completes the source review begun by the migration assessment, preserving its exact target. The turn is literature-only: no specialization, new bound, or mathematical script is produced. The standard inputs are recorded by citation in the [reflection source note](../../foundations/06-reflection-specialization.md), using the notebook's Hypotheses / Conclusion / Proof / Mathlib format.

The main gap is still exclusion of every polynomial-time SAT decider, or construction of one. For the proof-complexity route, the intermediate target is a conditional translation for one fixed polynomial-time A. L011 supplies H_(A,N), formed from the rejection circuit C_(A,N), the well-formedness/satisfaction circuit Eval_N, their gate clauses, and two asserted outputs. It supplies neither short ER refutations of H_(A,N) nor the proposed translation.

The continuation test is a uniform transformation, for fixed A and its fixed clock/encoding, taking a supplied ER refutation π_N of H_(A,N) and a rejected length-N well-formed F to an ER refutation of F, with time and full binary output length bounded by one polynomial in N+|H_(A,N)|+|π_N|. This is the sought threshold, not an achieved bound. Proving it would isolate the exact soundness-proof assumption needed by this route. It would still leave the short-proof premise and a relevant superpolynomial ER lower bound unresolved. Mere unsatisfiability of H_(A,N), or a separate polynomial chosen for each F, fails the test.

## Discovery and sources actually inspected

Queries used on 2026-09-26:

- `Pudlak "Reflection principles, propositional proof systems, and theories" simulation reflection extended Frege`
- `extended resolution reflection principle substitution proof simulation soundness polynomial`
- `Jerabek dual weak pigeonhole principle circuit Frege Lemma 2.2 2.6 extended resolution pdf`
- `Cook 1975 Feasibly constructive proofs propositional calculus extended resolution reflection theorem pdf`
- `"extended resolution" "SAT" "soundness" "reflection" decider`
- `"reflection principle" "evaluation" "encoding" "Frege"`

The exact structural comparison was to reflection formulas with a proof/acceptance predicate and an evaluation predicate; the local name H_(A,N) is not a literature identifier. The theorem numbers in a search query were leads, not accepted citations: the inspected 2003 Jeřábek manuscript's relevant results are Lemmas 2.4 and 2.5.

| Source version | Material read and use |
| --- | --- |
| Pudlák, arXiv:2007.14835v1, submitted 29 July 2020; PDF cover dated 30 July | §2.1–2.2, pp. 4–5, and §3.1, pp. 8–9: circuit representation, substitution, distinctions between proof existence and construction, and Fact 1. Closest specialization statement. |
| Cook, STOC 1975 preliminary version, pp. 83–97 | §5, pp. 91–93, and §6, pp. 94–95: definitional clauses, evaluator-dependent formal soundness, Theorem 6.8, and its following simulation sketch. Supporting ER treatment, with its stronger formal-provability premise retained. |
| Jeřábek, author manuscript dated 25 November 2003 | §2, pp. 12–14: CF definition and both conversion lemmas with proofs. Supporting representation result. |
| Krajíček, undated 13-page author manuscript, accessed 2026-09-26 | §2, pp. 5–8: clause-reduction definition, Theorem 2.1, its proof and interpretation. Concrete reflection reduction for different formulas; not an exact match. |

The existing [Cook–Reckhow assessment](../../foundations/05-refutation-systems-and-simulation.md) remains sufficient for the existential characterization of polynomially bounded systems; that result does not select ER. The [Clay problem page](https://www.claymath.org/millennium/p-vs-np/) and [Cook's official problem statement, §1, pp. 1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) were also read on this date: the ordinary uniform P-versus-NP target and the site's unsolved label are unchanged.

Unread leads are not inputs: Krajíček's cited book §9.3 was not inspected; later papers returned about TFNP and reflection encodings were search leads only. They are unnecessary for the conditional components selected above. No essential source needed for this assessment remains inaccessible. No absence or novelty inference is drawn from the searches.

## Exact applicability still to check

- L011's H_(A,N) concerns false rejection of CNFs. It is not literally the two-parameter reflection formula for arbitrary R_A certificates or the Γ family in Krajíček's theorem. A later application must respect this distinction and the polarity of satisfaction versus refutation.
- L011 describes Eval_N by parsing, sorting identifiers, dense assignment indexing, and evaluating clauses, then unrolling that algorithm. Its semantic description does not itself record a short ER identification with F on the corresponding assignment variables. The remaining work is to pin down that construction consistently and justify the identification required by the source. Replacing it by an arbitrary equivalent circuit, or silently switching to another H family, does not discharge the saved target.
- The source proof representations must be related to the notebook's fresh AND-extension variables, initial gate clauses, and final refutation of F. Preserve freshness under renaming and account for input/gate identifiers and proof references. Import standard conversions with an applicability argument; reprove only a necessary difference that the cited results do not cover.
- Polynomial time in a supplied π_N does not assert polynomial-time construction of π_N from N. Polynomial-length soundness proofs must remain an explicit premise. A proof of A's external correctness and a proof of its correctness in PV/ER are separate assertions in this notebook.

## Redundancy, decision, and limits

The [automatic-transfer failure](../../ATTEMPTS/010-automatic-decider-to-er-simulation.md) remains relevant: local transition checking did not establish global ER boundedness. L010's resolution lower bound and L012's O(N²) ER upper bound concern the already tested parity family; they are not additional evidence for this conditional target or an ER lower bound. The earlier assessment's warning against duplicating a known parity compiler is retained.

**SPECIALIZE, rather than a full-statement IMPORT:** the common reflection method is already known, while the concrete evaluator/encoding correspondence has not been checked here. Continue only with that application and its overhead. If it cannot meet the fixed-polynomial test without assuming the desired evaluator equivalence or changing the family, record the obstruction instead of claiming the target solved. No exact constant or optimal exponent is needed for the present downstream use.

The completed turn imports known literature inputs and makes no result beyond the checked literature. Any later implementation of the identified specialization should be classified as reproduction unless a separate, supported comparison establishes another difference. This is exploration turn 1 since the last mathematical advance or informative negative result; the review does not reset that count. The unchanged target is now assessed for a later research invocation, not for derivation during this turn.

## Mathlib

Coverage: **not checked** for the exact target or its supporting reflection/simulation results. Named source results and direct links are retained above and in the source note; no full Mathlib match or absence is claimed.
