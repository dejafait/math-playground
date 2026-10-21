# Source comparison: inverse rigidity to a uniform starting-height bound

TARGET: Determine whether L023's unique extendible inverse can force a bound n>=F(K), with F(K) tending to infinity, for every actual K-word chain of W(J,H)=(OOEO)^J O^H E^2 from a positive odd residue-20 root, with J>=2,H>=3 and all tails exact, using L020–L023 without an assumed endpoint cutoff.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Changed-use inverse-tree, quantitative predecessor, exact-postspell and shifted-valuation queries on 2026-10-05; bounded search record below; prior finite coding and graph assessments reused.
SOURCE_EVIDENCE: Applegate–Lagarias, Density Bounds I, author manuscript 1993-12-15, section 2 equations (2.1)–(2.4), Theorem 2.1 and full proof including cyclic roots; Krasikov–Lagarias arXiv:math/0205002v1 (2002-04-30), section 2 definitions and Theorem 2.2, section 5 Theorem 5.1 and proof, proof of Theorem 2.2, section 6 Theorem 6.1 and proof; L020–L023 and previous assessments reused.
COMPARISON: Inspected inverse-tree bounds count unrestricted predecessors of a fixed endpoint or integers reaching it; they do not give a uniform least positive root for this variable-length language. L023 fixes an extendible predecessor, not an endpoint height. No inspected theorem settles the requested implication.
GAP: Obtain arithmetic control independent of unrestricted future endpoint size and parameter-dependent offsets; decoding uniqueness alone is not the missing estimate, and no uniform bound is established by this review.
REASON: Essential comparison for the changed use of L023 is complete enough for one bounded arithmetic attempt, without claiming exhaustive coverage or novelty; no essential inaccessible source remains.
SCOPE: Full J>=2,H>=3 alphabet, positive odd residue-20 word boundaries, actual input parities and exact E^2 tails; one symbolic test of shifted dyadic-valuation transport through whole words and its compatibility with L023, with a guarded counterexample allowed. No new finite-minima table or endpoint cutoff.

## Target, relevance and limits

The main gap remains universal eventual descent on the least-root domain
surviving L014–L021. The intermediate threshold is n>=F(K), uniformly
in all parameters, with F(K) tending to infinity. Its plausible use is
to exclude infinite chains in this alphabet. Entry into it, other tails
and compensation remain independent gaps. No least-root restrictions
are assumed for this target.

This is a LITERATURE / EXPLORATION step, classification NOVELTY_UNCHECKED.
It compares sources and approves a test; it derives no bound or lemma
and executes no mathematical script. The mathematical exploration
budget is unchanged. The local target statement was already checked
on 2026-10-05 in foundations/01-target-and-scope.md; reuse that record.

## Primary theorem comparison

Applegate–Lagarias, [*Density Bounds for the 3x+1 Problem I.
Tree-Search Method*](https://websites.umich.edu/~lagarias/doc/applegateI.pdf),
author manuscript dated 1993-12-15; published *Math. Comp.* 64 (1995),
411–426. Inspected section 2, printed pp. 4–9: equations (2.1)–(2.4),
Theorem 2.1 and its full proof. The shortcut map matches. Roots a are
integers not divisible by 3. The theorem bounds asymptotic predecessor
counts using minimum/maximum depth-k tree counts. Its proof handles
both cyclic and noncyclic roots. Equation (2.4) bounds a leaf l of
weight w by l<=2^k*3^(-w)*a. This is an upper bound retaining a;
it does not supply a least-root bound when a is unrestricted. The
counts include predecessors outside the postspell language, so their
lower bounds cannot be assigned to that subset. This is quantitative
inverse-tree coverage, not a match for the target. No numerical table
was reproduced. The conditional asymptotic statement (2.5) is not used.

Krasikov–Lagarias, [*Bounds for the 3x+1 Problem using Difference
Inequalities*, arXiv:math/0205002v1](https://arxiv.org/html/math/0205002v1),
2002-04-30; published *Acta Arith.* 109 (2003), 237–258. Read section 2's
counting definitions and Theorem 2.2, section 5's Theorem 5.1 and proof,
the proof of Theorem 2.2, and section 6's Theorem 6.1 and proof.
Theorem 6.1 says that for each positive a not divisible by 3,
pi_a(x)>=x^0.84 for x>=x_0(a), where pi_a counts positive integers
at most x whose shortcut orbit reaches a. Its proof uses the feasible
linear-program solution in Table 2. The auxiliary functions restrict
orbit height and exclude cyclic roots; their estimates require
positivity, monotonicity and the stated difference inequalities.
This counts predecessors over all times and retains a-dependent
thresholds. It provides neither an upper bound excluding small roots
at large postspell depth nor control of a moving endpoint. No
specialization to the target is imported; no linear-program certificate
was independently checked. No current-best-exponent claim is made.

The author-hosted September 2002 Krasikov PDF had corrupted extracted
text; the readable April 2002 arXiv v1 supplied the theorem evidence.
The failed direct local download and inaccessible EuDML landing page
are not persistent blockers: primary theorem text was accessible.
Screenshot calls yielded no inspectable image here and are not evidence.

## Reused coverage and local evidence

Reuse the [growing-chain assessment](2026-10-04-growing-postspell-initial-size.md)
and [inverse assessment](2026-10-05-postspell-extendible-inverse-rigidity.md).
Their inspected Bernstein–Lagarias conjugacy statements concern finite
parity coding and 2-adic symbolic realization; their Laarhoven–de Weger
Theorems 2.1/3.1 concern finite residue graphs and the 2-adic extension.
Neither changes a positive-integer height question into a finite graph
question. No rereading or refreshed coding proof is needed.

Reuse the same assessments' Sodelin postspell identities, sections 2–3,
node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, live main checked 2026-10-04,
with the recorded lack of an immutable revision or checked Lean build.
L020 already specializes the shifted B-spell and odd-run formulas;
L021 retains offsets and all parities under composition. These are
available mathematical inputs, not discoveries of this review.

Read L020's hypotheses and proof through guarded realizability, L021's
hypotheses and composition/coding proof, and the full L022/L023 proofs.
L023's endpoint valuation fixes H; its residue obstruction excludes
different extendible J values. It requires a preceding actual word.
It does not bound J,H forward from the original root or future endpoint
size. The first root of a K-word chain need not itself admit a preceding
word: any later argument must retain this boundary qualification.

L022 and [Attempt 012](../../ATTEMPTS/012-repeated-postspell-minimum-transfer.md)
refute transfer of the repeated-W(2,3) minimum, including a mixed witness
with every tail exact, and stop the negative affine positive-endpoint
estimate. Preserve both failures. Do not enlarge the nine-word screen.
L007/L008's supplied overview records the fixed-endpoint/fixed-start
quantifier gap and the density boundary error; no detailed reread of
those lemmas is necessary for this comparison. Attempts 009–011 remain
parked/stopped. The historical single-valuation failures in L004/L006
warn against assuming valuation decrease, but concern different
coordinates/alphabets and do not globally ban this test.

## One approved discriminating attempt

Keep the exact TARGET for the next research step. Its first concrete
test is symbolic transport of V(x)=v_2(11x+23) at actual W boundaries,
using L020's sourced shifted B formula, L021's actual concatenation,
and L023's extendibility obstruction. The shift is already in L020's
formula; no valuation identity or monotonicity is derived here.

Determine whether the dyadic loss during B^J can be renewed without
bound by the following O^H E^2 on a genuinely extendible chain.
Keep J,H unbounded. Any application of L023 must include the required
preceding actual word; control of the earliest boundary is a separate
obligation. A concrete proposed inequality must include that boundary,
all offsets, positivity, residue membership and every parity. A claimed
counterexample must be an actual chain, with an odd endpoint after each
tail, and must identify precisely which inequality it violates.

Continue this mechanism only if the calculation yields a depth budget
controlled by the original n, with constants uniform in J,H and no
unrestricted endpoint term, or another explicit arithmetic constraint
that can plausibly supply that budget. A proof of the requested bound
must give F and prove its divergence. A root-controlled bound for a
single fixed word or finitely many parameters does not meet the threshold.

Abandon the proposed valuation-budget mechanism if a fully guarded
chain violates its needed monotonicity/accumulation inequality, or if
its only estimate still contains uncontrolled endpoint height or
unbounded parameter-dependent replenishment. This would stop that
mechanism, not refute every possible F or the Collatz conjecture.
A finite collision-free decoder screen or increasing finite minima
alone does not justify continuation. With no discriminating constraint,
record EXPLORATION and reassess instead of repeating source browsing.
No sufficient valuation budget is being assumed or approved as true.

## Search record and evidence limits

Queries actually executed on 2026-10-05:

- Collatz inverse tree Krasikov Lagarias 0.84 counting predecessors theorem 2003 pdf
- Collatz unique predecessor inverse tree uniform starting height restricted parity words
- Collatz "postspell" "inverse" height
- site:websites.umich.edu/~lagarias "Bounds" "difference" Krasikov pdf
- site:arxiv.org Krasikov Lagarias difference inequalities 0.84
- site:arxiv.org Collatz inverse tree counting fixed endpoint Applegate Lagarias 1995
- Collatz "postspell" "valuation" "height"
- Collatz "11n+23" valuation
- Collatz "11x+23" inverse

No exact matching theorem was located in this bounded search. Search
results included word/tree papers, claimed complete inverse-tree
solutions and a forum claim of an improved counting exponent. These
are unread, nonessential leads, not verified mathematics or evidence
that the target is novel. The two primary quantitative comparisons
above and reusable coding coverage suffice for the proposed test.

## Mathlib

Full inverse-to-height implication, shifted-valuation budget and
supporting library coverage: **not checked**. No matching declaration,
library absence or formal verification is asserted. There is no
complete candidate argument; STATUS remains IN_PROGRESS.
