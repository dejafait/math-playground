# Occurrence-pair oriented-block availability — source assessment

TARGET: Test whether L087's occurrence-splitting pairs from unsatisfiable 3-CNFs always admit L094's oriented common contiguous partition with at most floor(log₂ M) blocks, or exhibit an explicit family exceeding that cutoff.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 368 searched reversed minimum common string partitions, unsigned permutation strips/breakpoints and clause/occurrence/OBDD overlap; primary passages and local duplicate/failure checks are recorded below.
SOURCE_EVIDENCE: Kolman–Waleń, EJC 14 (2007) R50, §1.1 pp.3–4 and §5 p.10 Theorem 3; Goldstein–Kolman–Zheng author manuscript pp.2–3; Alexandrino et al., JUCS 26(9) (2020), §2.1 pp.1080–1081 Definitions 8–13; L087 construction/ledger and L094 hypotheses inspected.
COMPARISON: The partition hypothesis matches reversed MCSP on unsigned distinct occurrence symbols; inspected approximation and breakpoint results do not supply a logarithmic optimum on the exact unsatisfiable occurrence images.
GAP: Specialize unsigned internal-adjacency/strip reasoning to L087's stable occurrence-group order and establish a uniform cutoff bound or an explicit unsatisfiable family above the cutoff with its full original encoding.
REASON: Primary coverage supports a separate mathematical availability test; realizability, orientation/endpoint conventions and the original-M comparison remain local obligations, with no novelty claim.
SCOPE: Only the unchanged TARGET with L087's exact construction and L094's audited partition promise; no new supplier or general permutation-hardness target is covered.

The main gap remains unrestricted SAT decision/separation. This target asks
whether the newly audited restricted interface reaches L087's particular
clause/equality-testing pairs. A positive coverage theorem could connect
that interface to L087's conditional burden; a negative family would
precisely limit this application and direct subsequent work to a different
mechanism. No conclusion in either direction is asserted here.

Essential inputs: L087's construction beginning with the two appended
clauses, its exact occurrence-name convention, clause order, variable-group
order and full original B/M ledger; L094's oriented contiguous partition
hypothesis and audited conditional conclusion. All inputs are local.
Do not substitute original unsplit names for distinct occurrence names,
change either supplied order, omit the appended gadget, or redefine M.
The cutoff must use the actual explicit encoding, not only a lower bound
on M or an arbitrary padding of it. State a concrete encoding for any
proposed growing family and pay its full dictionaries. An arbitrary
permutation example is insufficient unless realized by these exact
occurrence orders of unsatisfiable width-at-most-three CNFs. A negative
family must retain this unsatisfiability premise: a large partition count
on satisfiable inputs alone would not block the needed Boolean-zero use.

The step-368 primary comparison below completes the discovery review.
Reuse L094's component assessments and audit. No full matching theorem
for this exact occurrence-family cutoff was found in the inspected
sources; this is not evidence of novelty or nonexistence elsewhere.
Full matching Mathlib coverage is not checked.

Continue if coverage supports either a uniform logarithmic bound or an
explicit realizable family with a provable minimum count above the actual
cutoff. A demonstrated failure stops this partition-availability route
for these supplied pairs, not L094, alternative witnesses, other ER data
or research on P versus NP. Preserve Attempts 018/030. No partition lemma,
family analysis or new mechanism is derived in this literature turn.
The source verdict authorizes only the unchanged availability test after
the supervisor's separate approval of this changed assessment.

## Primary source comparison — step 368

The [Clay page](https://www.claymath.org/millennium/p-vs-np/) and Cook's
[official description, §1 pp.1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf)
were reconfirmed on 2026-10-20: the target remains deterministic versus
nondeterministic polynomial-time language classes, with the checking-relation
formulation. No notebook target convention changed.

[Kolman–Waleń, *Reversal Distance for Strings with Duplicates: Linear Time
Approximation using Hitting Set*, EJC 14 (2007), R50](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r50/pdf),
§1.1 pp.3–4, defines contiguous partitions of related strings and
congruence by equality or reversal. Unsigned congruence gives RMCSP;
signed congruence also flips signs. Theorem 3, §5 p.10, gives a linear-time
Θ(k)-approximation for its listed variants when symbol multiplicity is
at most k. The relevant §5 cases inspected count both substring
orientations, use Lemmas 3a/4a and cut both orientations of a duo.
L087 has multiplicity one in each order, irrespective of repeated unsplit
variables. A guarantee relative to the optimum is not an absolute
logarithmic bound on that optimum. The theorem does not state the exact
occurrence-family availability result.

[Goldstein–Kolman–Zheng, *Minimum Common String Partition Problem:
Hardness and Approximations*, author manuscript](https://kam.mff.cuni.cz/~kolman/papers/mcsphard.pdf),
pp.2–3, distinguishes signed/ordinary MCSP and identifies the unique-symbol
case with permutation breakpoint counting. Its letter-preserving mapping
formulation relates directed breaks and block counts, allowing unnecessary
cuts. These passages were read as supporting coverage, not a reversed-MCSP
optimum formula. Its repeated-symbol hardness does not establish hardness
for the present distinct-symbol orders. Its directed consecutive-position
condition cannot be used unchanged when block reversals are allowed.

[Alexandrino–Oliveira–Dias–Dias, *On the Complexity of Some Variations of
Sorting by Transpositions*, JUCS 26(9) (2020), 1076–1094](https://www.jucs.org/jucs_26_9/on_the_complexity_of/jucs_26_09_1076_1094_alexandrino.pdf),
§2.1 pp.1080–1081, Definitions 8–13, defines extended permutations,
unsigned reversal breakpoints using absolute successive difference unequal
to one, and strips as maximal sequences without the chosen breaks.
Signed/directed breakpoints use a different condition. This supplies
appropriate unsigned terminology for the pending test. The source has
fixed sentinel endpoints; L094 partitions only the actual alphabet, so
endpoint contributions require explicit treatment. No sorting-hardness
theorem from this paper is imported.

The primary RMCSP definition matches L094 when both orders are treated
as unsigned strings of distinct occurrence names. Literal signs belong
to D's Boolean test, not the permutation alphabet. This is a hypothesis
comparison, not an availability proof. Any exact optimum characterization,
realizable family and quantitative cutoff argument remain for a research
turn. A short local adjacency argument is justified by this application
and its endpoint convention; reproof of the approximation algorithm is
unnecessary.

## Search, duplicates and limits

Queries included “minimum common string partition reversal permutations
breakpoints strips unique symbols”, “Kolman Walen reversed minimum common
string partition breakpoints pdf”, “occurrence clause common string
partition unsatisfiable” and “reversed common partition OBDD”. Search
snippets were not accepted as theorem evidence. Genome-rearrangement book
and other algorithm hits remained discovery leads, not inspected inputs.
Initial journal/mirror retrievals failed; the journal PDF without its
trailing slash was subsequently read, resolving essential access.

Recent notebook order-pair assessments/history searches found only the
step-367 proposal for this availability question. L087's clause/group
orders, appended gadget, empty-clause reception and pre-witness ledger,
and L094's hypothesis were read. Attempt 018 stops repeated scope approval;
Attempt 030 stops universal faithful common-order value availability.
Neither supplies this partition conclusion. Both stops and unfinished
work are preserved; L094's audited supplier is reused. No cross-notebook
input was read. No inspected theorem covers the joint stable-order,
unsatisfiability and full-bit cutoff obligations. This bounded review
does not certify novelty. No lemma, mathematical script or DAG edge is
written this turn.
