# Repeated self-AND family — structural obstruction source review

TARGET: Test whether a polynomial-bit genuinely used ER family built from an n-input conjunction followed by repeated self-ANDs forces |D|>=n-k for L080's promise and M>=2^(n-k) for L081's trees at its actual original T/k.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 319 searched exact syntactic-support/backdoor, repeated-squaring/ER, backdoor-tree/conjunction and non-skew-depth terminology; compared L080–L082, L019/L023/L027/L076, Attempts 016–017/019–020 and targeted proposal/history matches. No inspected full-statement match; search failure does not establish novelty.
SOURCE_EVIDENCE: Read Ordyniak–Schidler–Szeider (2024), Theorem 2 and its complete Horn proof, PDF pp.6–7; reused the assessed restriction/tree definitions and Observations 1–2. Inspected Limaye–Malod–Srinivasan (2016), §1.2 pp.3–4 and precise Theorem 1.2 statement/final proof paragraph pp.29–30, as comparison only. Reconfirmed Cook's currently linked Clay statement, §1 p.1.
COMPARISON: The inspected exponential CNF backdoor bound restricts the variables available to the expensive trees and uses simplification; it is not a bound for every L081 tree. Arithmetic non-skew depth uses a different gate predicate. L082 supplies conditional replacement, while existing repeated-square examples do not establish this genuinely used-family structural bound.
GAP: Construct or refute the proposed genuinely used ER family with every input occurring originally, charge actual full-bit T, choose a polynomial chain exceeding the resulting k, and prove or refute both unchanged-cutoff thresholds without simplification.
REASON: Essential coverage is sufficient for one separate bounded proof/counterexample attempt on the unchanged TARGET; no known theorem import or new family bound is asserted in this literature-only step.
SCOPE: Original T=2+|F|+|pi| and k=floor(log₂(T+2)); all roots, both signs, ordered/repeated operands and zero products retained. Explicit full binary read-once-per-path trees only; no simplified restriction, compressed DAG, alternative-certificate bound or SAT transfer.
LITERATURE_REASON: This newly proposed genuinely used family and its n-k thresholds were outside the ready replacement assessment; step 318 explicitly left this target REVIEW_REQUIRED. This review supplies that essential comparison without repeating the completed audit.

The main gap remains unrestricted SAT decision/separation. The nearer
route has no suitable fixed sets or polynomial explicit trees for
arbitrary ER. A rigorous obstruction on a short genuinely used family
would test whether the present structural supplier can be universal,
and guide a change of representation if it fails. An easy alternative
refutation or certificate would not invalidate a supplied-proof
structural obstruction; it would limit its consequences.

Essential intended inputs are L080's residual definition, L081's full
explicit query-tree hypothesis and audited L082's fixed-set replacement.
Their hypotheses and relevant residual/source-comparison passages were
read. L080's whole theorem additionally requires |D|≤k; L082 applies
also for M>T+2 without making that cardinality inference. A valid family,
its ancestry and its ledger remain unproved. No cross-notebook input is
used. Full matching Mathlib coverage is not checked; no absence is claimed.

### Primary comparison and literature reuse

Ordyniak, Schidler and Szeider, *Backdoor DNFs*, JCSS 144 (2024), 103547,
[published PDF](https://eprints.whiterose.ac.uk/id/eprint/213187/7/1-s2.0-S0022000024000424-main%20%281%29.pdf),
Theorem 2, PDF pp.6–7: its Horn case has an s+2-leaf tree, whereas trees
whose query variables form a subset-minimal strong backdoor set require
at least 2^s leaves. The displayed family has exponential size in s. The
inspected Horn proof classifies the minimal sets, forces their relevant
variables to be assigned at leaves, and supplies a small unrestricted
tree by querying p first. Thus this is not an all-tree exponential bound.
Reuse sections 2.2–2.5 and Observations 1–2 through the ready assessment
`drafts/literature/2026-10-18-adaptive-tree-fixed-set-premise-comparison.md`.
Their restriction removes clauses and literals. No result from this
paper is imported as a proof of TARGET; its other base-class proof cases
are not needed here.

Limaye, Malod and Srinivasan, *Lower Bounds for Non-Commutative Skew
Circuits*, Theory of Computing 12(12) (2016), 1–38,
[published PDF](https://toc.cs.uchicago.edu/articles/v012a012/v012a012.pdf),
§1.2 pp.3–4: non-skew depth counts multiplication gates with neither
operand a scalar/input variable. Theorem 1.2 compares circuits computing
the same polynomial under different non-skew-depth budgets. The precise
version on pp.29–30 imposes 64(8+12k)|d; its final proof invokes earlier
rank lemmas, whose proofs were not reviewed or imported. Neither this
gate predicate nor its lower bounds establish the support/deletion
claim here. Reuse the terminology comparison in
`drafts/literature/2026-10-17-logarithmic-large-branch-depth-data.md`.
The new extracts check the stronger-result lead; no arithmetic bound is
specialized or reproved.

The [current Clay page](https://www.claymath.org/millennium/p-vs-np/)
still links Stephen Cook, *The P versus NP Problem*,
[official PDF](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf),
§1 p.1: deterministic versus nondeterministic polynomial-time language
recognition remains the exact target. No revision date is printed in
the inspected opening; the served linked version was checked on
2026-10-18 and agrees with `foundations/01-model-and-target.md`.

### Search, duplicates and recorded failures

Queries on 2026-10-18 included `"backdoor trees" "backdoor sets" SAT leaf`,
`"syntactic support" circuit repeated squaring backdoor`, `"non-skew"
"depth" arithmetic circuits repeated squaring`, `"circuit" "syntactic
support" "backdoor"`, `"repeated squaring" "extended resolution"`,
`"backdoor trees" "conjunction"`, and `"support" "non-skew depth" circuits`.
Primary inspection was confined to the comparisons above. Search leads
on probabilistic backdoors, backdoor-decomposable monotone circuits and
recursive backdoors remain uninspected, not theorem evidence. No
exhaustiveness or originality is asserted.

Targeted searches in local literature/history/attempt paths found the
step-318 proposal but no completed n-k structural obstruction there.
L019's used Fibonacci family concerns literal unfolding on two originals;
its proof and constant alternative certificate were read. L023's stated
exact-correction obstruction and repeated-square discussion concern
formal degree. L076's repeated-self-AND boundary example expressly has
unused definitions and one original. None establishes the present bound.

L027's existing signed-unit, repeated-operand, ancestry-device and
full-bit construction passages were read as a reusable host template.
Its HWB lower bound is not transferred. The local ER convention in
`foundations/05-refutation-systems-and-simulation.md` allows earlier
signed operands without requiring them to be distinct. A new
conjunction/square instance still needs its own legality, ancestry and
encoding proof; no specialization is derived during this review.

Attempts 016–017 stop identical-output tree conversion and independently
bounded exact corrections. Attempts 019–020 stop universal common-order
OBDD width and degree-only identical-output ABP conversion. Their failure
records were read and remain intact. This target tests a later structural
promise and assumes none of those stopped conclusions. The possible
existence of an easy alternative proof remains a limitation, not an
objection to testing the supplied proof.

### Separately approved bounded attempt

The candidate family is only a proposal: an n-input conjunction with
a following chain of repeated self-AND definitions. Its length must be
chosen and charged using actual original T, rather than an externally
chosen cutoff or padding alone. All claimed used definitions must have
genuine final inference ancestry; all n inputs must be originals of
the actual CNF. Both signs, repeated operand occurrences, scalar roots,
unused-root conventions and products by zero remain as in L080/L081.
Do not change to semantic support or simplified restrictions.

Prove the deletion threshold for every queried set meeting the residual
promise, without first assuming |D|≤k, if it is to feed L082 for arbitrary
M. Choose and verify a polynomial chain length exceeding the resulting k.
These are obligations for the next attempt, not results of this review.

The discriminating test is |D|≥n-k and the proposed M≥2^(n-k), with n-k
large enough relative to actual T. Check n>2k to exclude L080's allowed
sets, and require (n-k)/log₂(T+2) to be unbounded to exclude every fixed
polynomial leaf budget. These are required thresholds, not achieved
estimates. Continue only with a valid family, genuine use, complete
full-bit ledger and unchanged-cutoff proofs. If a threshold fails,
preserve a counterexample or exact failed assumption and abandon that
claimed bound; this does not prove universal structural sufficiency.
No new mathematical construction, lemma or script was executed here.

Even a successful obstruction would concern these supplied-proof
structural promises only. It would not rule out alternative ABP data,
other proofs or certificates, establish formula-only lower bounds, or
resolve P versus NP. This assessment approves only a separate bounded
mathematical attempt, not the family or its bounds. Arbitrary-ER data,
formula-only bounds and unrestricted SAT remain independent open gaps.
