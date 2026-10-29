# Seminvariant-first enumeration — source assessment

TARGET: Assess whether enumerating syzygy-admissible (a,p,r) and solving 3b² ≡ p (mod 8a) can replace L128's over-cap coefficient loops without increasing the saved caps.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the explicit-descent assessment and L128/ATTEMPTS/053; searched “Cremona binary quartic enumeration seminvariants p r syzygy algorithm” and “3b 8a syzygy quartic”; inspected the corrected book algorithm and the author quartic-equivalence manuscript, rather than inferring performance from search hits.
SOURCE_EVIDENCE: Cremona, Algorithms for Modular Elliptic Curves, second edition (1997), corrected online Chapter III, Section 3.6 Step 2 pp.93–95, especially the paragraph identifying c-bounds as seminvariant bounds, equation (3.6.7), the syzygy sieve and reconstruction; errata dated 26 September 2003 p.1; Cremona–Fisher (2009), 3 December 2008 author manuscript Section 1 pp.1–2.
COMPARISON: The sources supply complete coefficient regions, the seminvariant identity, modular square sieving and exact reconstruction. They do not implement the proposed ordering or establish its instance workload; L128 counts raw coefficient loops only. Approve a bounded specialization test, not a performance or rank conclusion.
GAP: Translate every signed real-type region exactly, prove the reordered traversal retains all source representatives, certify all congruence roots and reconstruction, and measure actual work under the unchanged numerical caps. No such derivation or calculation was performed in this literature turn.
REASON: Essential algebraic coverage is now inspected; only the explicitly identified elementary traversal specialization and bounded workload test remain. Reproving descent or assuming a fast traversal is unnecessary and unapproved.
LITERATURE_REASON: L128 gives a new over-cap obstruction; the changed ordering and its workload unit were outside prior assessed execution scope.
SCOPE: Exactly TARGET for L128's invariant pair and L112's elliptic model; a feasibility/completeness test of seminvariant-first ordering, without local Selmer processing, equivalence merging, backend probes, cap increases or higher descent.

## Relevance and continuation threshold

The main gap remains exclusion of residual primitive Beal solutions. The
intermediate target is a complete feasible quartic traversal, potentially
supporting upper rank one for L112 and the elliptic summand of L127.
Genus-two rank, marked lifts and integer recovery are independent gaps.
This review supplies coverage, not a new mathematical result or rank bound.

Continue only if the future specialization gives complete regions and
reconstruction and a certified workload within both saved caps. Otherwise
stop this traversal, preserve the evidence, and select a different mechanism;
no truncated enumeration may be called complete. A failed performance test
would not refute two-descent or the rank-one possibility.

## Inspected primary inputs and their limits

[Cremona, corrected Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf),
printed pp.93–95, is the primary algorithm. Its fixed-invariant search
assumes nonzero discriminant; L128 supplies this hypothesis and the applicable
real types. The p.94 paragraph expressly interprets c-bounds through the
seminvariant. Page 95 supplies modular filtering and reconstruction. These
are citations to known algorithms, not proposed reproofs. L128 already
supplies the invariant selection and certified root enclosures.

[Cremona–Fisher, author manuscript](https://johncremona.github.io/papers/quartequiv.pdf),
Section 1 pp.1–2, defines p=3b²−8ac and r=b³+8a²d−4abc and states
27r²=p³−48Ia²p−64Ja³. The same section defines I=12ae−3bd+c²
and J=72ace+9bcd−27ad²−27eb²−2c³. The field has characteristic
different from 2 and 3; Q qualifies. Its nonzero-discriminant convention
matches L128. This independently confirms the normalization used here.
The corrected equivalence results remain covered by the prior assessment;
this test requires no class merges.

The [book errata](https://johncremona.github.io/book/errata.pdf), p.1,
corrects the p.95 denominator for d to 8a². Use that corrected formula
and the cited formula for e, with exact integrality and invariant checks.
The book's sign simplification uses a reflection; the proposed test will
instead retain both r signs and zero, avoiding an extra covering-equivalence
argument. Do not omit zero by copying the prose instruction r>0.

The source sieve is a necessary test, followed by an exact square test;
passing residues is never sufficient. Its brief modulus-9 discussion must
not be implemented as though divisibility by 9 meant divisibility by 27:
require exact divisibility by 27 and integer squareness of the quotient,
including zero. Residue-table definitions must directly express the stated
congruence, with all possible residues checked.

## Covered future specialization; no derivation this turn

The next mathematical attempt must first write the elementary coverage
argument for the proposed reordering. It must translate p.94 into closed
p-intervals separately for type 1 and both type-2 signs, using L128's exact
root intervals and outward rounding. In particular negative-a inequalities
and the source's reversed root ordering cannot be copied from positive a.
No p-interval formula or specialized bound is asserted in this review.

It must then justify recovery of every reduced b from the saved congruence
3b² ≡ p (mod 8a), in the original half-open b interval, before using the
source reconstruction and integrality checks. A single modular root, division
by 3 when it is not invertible, or assumed unique lifting is insufficient.
Use positive moduli for signed a. Keep both source real-type regions even
if they overlap, unless overlap handling is rigorously justified. Source
representatives with nonzero a are the search scope; keep the identity class
separately and do not use formulas dividing by a for a=0.

The coverage proof, translated intervals and arithmetic certificates belong
in canonical lemma documentation only in that later RESEARCH turn. Their
absence here is an explicit specialization obligation, not an uncovered
appeal to a new descent theorem. The imported descent algorithm is not to
be reproved. Mathlib coverage of this traversal was not checked; no absence
or formal verification is claimed.

## Work units and bounded discriminating test

Do not redefine the old row cap to count only survivors while hiding an
unbounded preliminary scan. The unchanged numerical caps are 200000
workload-counting rows and 2000000 enumeration triples. Before execution,
fix the sieve moduli and a ledger: count each scalar residue-table cell,
CRT-combination trial, explicit candidate (a,p) inspection and congruence-root
trial against the 200000 cap during feasibility counting. Count all expanded
(type,a,p,r,b) candidates against the 2000000 cap during enumeration;
record the corresponding (a,b,c) triples as well. Duplicate/type/sign work
counts whenever executed. Arithmetic interval-counting may aggregate an
entire progression only with a proved floor-count formula and saved inputs;
record all such aggregate operations too. Table construction, CRT work and
b-root search must not be hidden behind a survivor count. These are stricter
accounting obligations for a changed traversal, not an increased budget.

A modular progression sieve with certified interval counts is an eligible
implementation proposal. The sources justify its rejection predicate, not
its speed or a particular choice of moduli. Fix and justify that choice
before arithmetic; if table/combination work itself cannot fit, stop rather
than retrying many choices in this one test. A bounded prefix may diagnose
an over-cap obstruction but cannot certify the unvisited remainder.

The full saved certificate must give complete or explicitly incomplete
coverage, every work subtotal, actual versus required bounds, exact rejected
residues/square checks, reconstruction failures and paths. First establish
counting feasibility; enumerate only if the complete bounds fit. No local
solubility or Selmer claim is approved merely because this succeeds. If the
count cannot be completed within budget, report that honest obstruction
rather than claiming a lower bound not proved.

## Duplicate/failure comparison and decision

The existing explicit-descent review already covers the general method,
local tests and corrected class comparison. It did not cover this ordering;
no duplicate instance certificate was located. Search results included
Cremona's reduction paper and a secondary discussion of recent average-rank
work; neither supplies an inspected exact-instance workload certificate and
neither is an input here. Failed searches do not establish novelty.

ATTEMPTS/053 stops raw loops, while ATTEMPTS/050–052 retain their separate
search, rank-zero and execution obstructions. None is erased or reopened.
L108 remains unfinished. This proposal changes the traversal and has an
independent pass/fail test; it is not a larger raw box. No new source blocker
remains for that test. The review approves its source scope only; a separate
next-turn approval precedes mathematical execution under supervisor policy.

Essential continuation inputs: L128, L112, L127, ATTEMPTS/050–053 and
`drafts/literature/2026-10-25-marked-elliptic-explicit-two-descent.md`.
Unresolved assumptions: traversal completeness and workload, complete local
and class certificates, sharp upper rank, genus-two rank, marked lifts,
degree-nine recovery, both L095 systems, minus-eleven and other signatures.
PROOF.md and DAG.md do not change: the mathematical argument is unchanged.
