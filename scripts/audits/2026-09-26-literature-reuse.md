# Literature reuse audit — 2026-09-26

Verdict: the project uses online research, but does not systematically prevent rediscovery. It does not currently meet a requirement to search for and reuse existing proofs before spending substantial effort on a new derivation. There is confirmed overlap with established results, as well as good examples of precise theorem imports. This is a research-process audit, not a mathematical verification or novelty certification of the portfolio.

## Scope and evidence

Inspected the shared GOAL.md and PROMPT.md, launcher/provider construction, research-outcome assessment, structural validator, all ten local goals and checkpoints, notebook source inventories, selected foundations, overviews, histories and mathematical statements. Examined all ten retained stdout logs and extracted their web actions. Spot-checked mathematical overlap against online primary sources.

The retained logs contain two completed turns per notebook: 20 completed turns total. They also contain failed/interrupted or ongoing sessions; these are not counted as completed research. This is a recent window, not the project's complete execution history. Logs rotate, and no claim about lifetime browsing frequency or percentage of wasted tokens can be inferred. No full proof-by-proof literature search of all 450 lemma/corollary files was performed. The inventory at inspection was 353 files in RH and 97 across the other nine notebooks.

Only this audit report was added. Research artifacts, launch settings, running processes and checkpoints were not changed.

## System-level findings

1. **Literature checking is requested but not operationally specified.** [GOAL.md](../../GOAL.md), relevance rules, says “Check existing theorems, duplicates, and failed approaches first.” It does not require online discovery, a source/version record for each new route, comparison with the strongest known result, or an explicit explanation of what remains beyond the literature. [PROMPT.md](../../PROMPT.md) emphasizes internal redundancy, relevance and full proofs or citations. It permits a fully self-contained derivation without an external overlap assessment.

2. **The loop does not enforce literature reuse.** [research.py](../loop/research.py) checks changed checkpoints, fresh step IDs, nonempty evidence and self-reported outcomes. ADVANCE and NEGATIVE reset exploration/stall counters. It does not distinguish importing a known theorem, independently deriving a known result, checking an implementation, or making a potentially new mathematical contribution. [runner.py](../loop/runner.py) applies that assessment after structural validation. A sequence of locally useful rediscoveries can keep the loop running indefinitely.

3. **The validator checks documents, not prior art.** [check_structure.py](../docs/check_structure.py) checks layout, identifiers, dependency acyclicity and local links. It does not retrieve external citations, validate theorem matches, check literature coverage or determine whether a proposed result is already known. Passing it is no evidence of efficient research.

4. **Search exists, but the repository does not pin its mode.** [codex.py](../loop/codex.py) launches Codex with workspace-write, no approval prompts, and max reasoning effort; it does not explicitly set web_search. The inspected user config had no explicit web_search setting. Actual web events establish that the tool was available. Current [official configuration documentation](https://learn.chatgpt.com/docs/config-file/config-reference) describes cached search as the default and live retrieval as an explicit option. The historical effective mode is not established by the retained events. Absence of a --search flag does not mean search was disabled. Availability alone does not ensure use.

5. **The current mandatory source work often targets the wrong question.** Nine local goals require checking the current official problem statement before selecting a route. That is useful for defining the target, but repeated prize-page checks do not discover theorems about the chosen intermediate problem. The recent logs show this distinction clearly.

6. **Mathlib entries are not literature reviews.** Lookup is explicitly optional, appropriately for informal research. But there is no separate required research-literature assessment. RH has 304 lemma files containing URLs, yet the generic Mathlib documentation homepage occurs 253 times. A URL count substantially overstates substantive source coverage. “Not checked” does not imply either novelty or absence from the mathematical literature.

7. **No required classification of progress relative to existing knowledge.** Some notes explicitly disclaim novelty, which is good practice, but recaps can still present a new local write-up as a constructive research gain. The project needs to distinguish what became known to the notebook from what was not already available in published research.

## Evidence across all ten notebooks

Web activity below describes the retained recent window. A paper already read earlier need not be reopened every turn; absence of new calls is a warning when there is also no documented comparison for the new target, not by itself proof of waste.

| Notebook | Existing research actually used | Recent web evidence | Assessment |
| --- | --- | --- | --- |
| Beal | FLT, Darmon–Merel, Freitas, Kraus, Bilu–Hanrot–Voutier, Bruin, Chen–Siksek, with theorem ranges and access qualifications | Technical searches and paper/code retrieval | Strong example of theorem reuse. The new exponent exclusions are largely imported knowledge, not new exclusions discovered by this project. Coverage remains route-specific. |
| BSD | Milne, Greenberg, Kato, Darmon–Rotger, Castella–Hsieh, with hypotheses and distinctions between analytic/algebraic ranks | Technical paper retrieval and theorem lookup, alongside Clay pages | Substantial source-led work. No systematic documented comparison of each new strict-lifting target against the wider literature. |
| Collatz | Tao's almost-all-orbits result as background; official target page | Only the same prize page opened once in each completed turn | Weakest source coverage: only two distinct external URLs in the notebook inventory. The parity/congruence route lacks comparison to classical parity-vector work. |
| Hodge | Buskin, Huybrechts, van Geemen–Schütt, Huybrechts–Thomas and Stacks references | Technical discovery queries, papers and Stacks pages | Good supporting-source practice and careful theorem scope. Still no exhaustive novelty check on the specialized deformation calculations. |
| IUT challenge | Exact IUT III passages, Scholze–Stix criticism, Mochizuki's response, Frobenioids definitions | Source documents and exact passage lookups, plus prize pages | Clearly engages prior research and both sides of the dispute. Simplified local models are expressly not identified with full IUT; their payoff remains uncertain. |
| P vs NP | Cook–Reckhow and Ben-Sasson–Wigderson, among other standard inputs | Technical searches in one turn; only Clay page in the later ER-construction turn | Mixed. Precise sources exist, but the key qualitative conclusion of the new Tseitin ER construction was already available. |
| RS list decoding | September 2026 ECCC results, chart/cover arguments, pinned ArkLib model | Only prize-page opens in both completed turns | Earlier serious literature engagement, followed by local Riccati work without a fresh documented overlap search. The ABF challenge-paper comparison remains incomplete. |
| RS MCA | Pinned ArkLib definitions and a WHIR definition excerpt | Only prize-page opens in both completed turns | Source model is explicit, but the main companion paper's bounds and definitions remain unaudited. Continued model-specific research risks missing existing bounds or target qualifications. |
| RH | Classical inputs, selected analytic estimates, Csordas–Varga and Jensen-polynomial literature screens | No web actions in the two completed turns | Historical literature use is real, but uneven. Confirmed weaker finite-height coverage and acknowledged earlier rediscovery of moment inequalities. No current search evidence for the Mellin-width route. |
| Yang–Mills | Magnen–Rivasseau–Sénéor, Giusti–Pepe, Del Debbio–Patella–Rago | Only official Clay statement/PDF opens | Relevant precedents are recorded, including regulator mismatches. New specialized calculations are not accompanied by a recorded comparison with the broader Ward-identity/gradient-flow literature. |

Five notebooks in this recent window had no substantive technical web retrieval: RH, Collatz, both RS notebooks and Yang–Mills. The other five did. This is not a claim that the former five never use research or that every turn must repeat a search.

## Concrete overlap and gaps

### RH: finite-height zero exclusions are already covered much more strongly

[PROOF.md](../../riemann/PROOF.md) reports exclusion of nonreal centers through height 40, with arithmetic contracts, and separately records finite Laguerre signs and normalization/order information. [Platt–Trudgian](https://arxiv.org/abs/2004.09765), published in 2021, rigorously verified RH by interval arithmetic through height 3 × 10^12. Their result already supplies the finite-height zero-location conclusion on the notebook's small band.

This does **not** mean their theorem supplies every local Laguerre inequality, coefficient bound, ordering result or a method extending to arbitrary heights. The duplication is the zero-exclusion coverage, not an assertion that every proof or intermediate object is identical. A new method may justify small-scale tests, but the project should identify the missing scalable property and why an existing theorem cannot serve as the needed input. No Platt/Trudgian citation was found in the RH markdown search.

There is also internal evidence of delayed discovery: [the September 21 literature screen](../../riemann/ATTEMPTS/2026-09-21-theta-moment-literature-screen.md) explicitly says known adjacent-moment inequalities are stronger than the notebook's finite tests, and explains how a source result recovers L027. That audit carefully identifies why the known theorem still does not prove RH. It is good corrective work, but illustrates why the literature comparison should precede the finite reproof.

### P vs NP: the decision made by L012 did not require a new proof construction

[L012](../../p-vs-np/lemmas/L012-tseitin-er-row-addition.md) develops a parity-row compiler, quantitative size/width bounds, and a checked proof generator. Its strategic conclusion is that the existing bounded-degree Tseitin family has polynomial-size extended-resolution refutations and cannot furnish superpolynomial ER lower bounds.

That qualitative conclusion follows from existing primary results: [Buss–Thapen](https://users.math.cas.cz/~thapen/DRAT.pdf), Theorem 4.10, gives polynomial-size SPR-minus refutations of Tseitin clauses; their Theorem 3.3 supplies the relevant simulation into DRAT. [Kiesl–Rebola-Pardo–Heule](https://www.cs.utexas.edu/~marijn/publications/ijcar18.pdf) proves polynomial simulation of DRAT by ER. Composing these is the audit's inference. It settles the polynomial/nonpolynomial route-selection question without rebuilding the local compiler.

The local explicit O(n² log n) bit bound, bounded-width implementation and proof records are extra deliverables; this audit does not establish whether those details are novel or dominated by other constructions. Their necessity for the stated research goal was not shown by the existing literature comparison. No Buss–Thapen citation was found in the notebook.

### Collatz: classical machinery is being developed without its literature map

[L002](../../collatz/lemmas/L002-maximal-odd-even-block-descent.md), [L003](../../collatz/lemmas/L003-consecutive-growing-blocks.md) and [L005](../../collatz/lemmas/L005-mixed-growing-word-congruences.md) derive prescribed block residues, affine iterate expressions and repeated-word formulas. The general parity-vector/congruence correspondence and inverse formulas are established machinery. [Rozier (2019), sections 1–2 and Lemma 1](https://math.colgate.edu/~integers/t8/t8.pdf), records the classical correspondence and inverse expression, with references to Terras, Everett and others, and gives a further inverse formula.

The notebook contains no Terras/Everett/Lagarias comparison in the inspected markdown. This confirms overlap at the machinery level and a material literature gap. It does not prove that the exact restricted-alphabet inverse branching or L011's first-merge statement already appears elsewhere. Those more specific claims require their own search and comparison before being treated as new research.

### Both RS notebooks: an acknowledged source gap has not blocked extended research

The [list-decoding source audit](../../reed-solomon-list-decoding/foundations/01-target-and-source-audit.md) and [MCA source audit](../../reed-solomon-mca/foundations/01-target-and-source-audit.md) explicitly record failure to obtain the July ABF26 companion PDF, including HTTP 403/DNS issues. Alternative pinned models and supporting sources were used transparently; no silent equivalence is claimed.

Nevertheless, the projects continue substantial calculations while current companion-paper definitions, bounds and target correspondence remain incomplete. This is not confirmed duplication of their latest Riccati or locator-incidence lemmas. It is an unresolved risk that directly conflicts with confidently avoiding already-solved or mis-scoped subproblems. The local goals explicitly requested freezing the exact source before research; the current alternative-model qualifications do not complete that task.

### Good reuse exists and should be preserved

[Beal's Chen–Siksek foundation](../../beal/foundations/07-chen-siksek-exponent-range.md) identifies the exact theorem, manuscript version, signed primitive scope, computational qualification and access limitation. It imports the result rather than rerunning its entire computation. [BSD's Castella–Hsieh foundation](../../birch-swinnerton-dyer/foundations/07-castella-hsieh-nonvanishing.md) carefully retains hypotheses and distinguishes supporting results from the missing rank implication. The Hodge and IUT source notes likewise distinguish theorem statements from notebook deductions. These practices are useful models, but are not universally required or enforced.

## Changes needed to meet the user's requirement

These are recommendations, not implemented changes.

1. Require a short, recorded literature assessment **before substantial work on each new route or intermediate target**. State the target, sources actually read, closest theorem with exact hypotheses, strength comparison, and the remaining difference. Reuse an adequate existing assessment when the target is unchanged; do not require pointless browsing every turn.
2. Search both the exact statement and the standard terminology/mechanism. Follow references from a credible survey or key paper. Checking only the prize page or the name of the notebook misses the useful literature.
3. Prefer a precise citation and minimal specialization over a full independent reproof. Permit rederivation when needed to change hypotheses, obtain missing effective constants, validate a suspect recent claim, or build an essential artifact; record that reason before spending a full turn.
4. Classify outcomes as imported known result, specialization/reproduction, potentially new result after a bounded search, or novelty unchecked. Keep these distinct in recaps and resource decisions. “ADVANCE” alone should not be read as new research.
5. Add a process check for the existence and relevance of that assessment before accepting a new-route research step. A validator cannot certify novelty, but it can flag absent evidence instead of rewarding any fresh lemma/checkpoint.
6. Make literature access failure visible as an unresolved prerequisite for source-dependent work. Seek another authoritative version when needed; if the exact target remains unread, prioritize resolving that gap or explicitly budget only provisional exploration.
7. Prioritize retrospective review of RH finite certificates, Collatz parity/inverse machinery, P vs NP proof-system examples and both RS target comparisons. Preserve useful artifacts, but stop allocating turns merely to reproduce already available conclusions.

The project is not devoid of research value. It is currently a mixture of source-based synthesis, independent reconstruction, method testing and unchecked novelty. That mixture is unsuitable for unattended resource spending under a strict “do not redo existing work” requirement until literature comparison becomes a concrete part of route selection and progress reporting.
