# Paired states and suffix minima: literature assessment

TARGET: Test whether a linear invariant in the two paired states and their suffix minima can exclude simultaneous non-descent for the four-block alphabet while preserving the one-block depth offset.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the adequate 2026-09-27 exact-target screen; recovery searches on 2026-10-03 compared modular sufficient sets and Diophantine cycle exclusions with the exhausted paired route; exact queries and inspected sources appear below.
SOURCE_EVIDENCE: Reused the inspected Colón–Sankaranarayanan–Sipma Theorems 1–2, https://theory.stanford.edu/~sipma/papers/cav03.pdf; Bradley–Manna–Sipma Theorem 2, https://theory.stanford.edu/~arbrad/papers/z.pdf; Shoham Theorem 1, https://arxiv.org/pdf/1812.01069v2; additionally read Monks et al., arXiv:1204.3904v2, section 6, Theorem 6.4 and Proposition 6.5, https://arxiv.org/pdf/1204.3904v2; Hercher, arXiv:2201.00406v3, Definitions 4–5 and Theorem 23, https://arxiv.org/pdf/2201.00406v3.
COMPARISON: Known methods cover checking and searching specified linear inductive certificates; no inspected theorem supplies the requested certificate for the paired histories, and real-variable completeness does not establish completeness for their exact integer guards.
GAP: Find or obstruct a linear certificate preserving both suffix minima and the one-block offset and excluding every terminal pair whose starts each meet their own non-descent threshold.
REASON: The exact certificate remains a justified specialization but has not been found or refuted; the exhausted three-turn batch is parked, and recovery selects a distinct forward modular-graph target with its own REVIEW_REQUIRED assessment.

The body below records the September 27 assessment and its bounded test.
The October 3 recovery comparison is appended at the end. SPECIALIZE is
a literature-coverage decision, not permission to repeat the exhausted
exploration batch; the current route and sole action are in PROGRESS.md.

## Hypotheses

The alphabet is {(1,1),(2,1),(3,1),(1,2)} and the histories are positive
odd maximal-block histories starting above 1. At each backward stage,
retain the two current states and the minimum already seen in each
suffix. The paired coordinates have indices one apart, and the
companion side needs one extra inverse before testing equal-depth
histories. Each final start must be compared with its own suffix minimum.

The proposed mechanism seeks a linear inequality preserved under the
admissible paired transitions and incompatible with both starts meeting
those inequalities. This is a candidate certificate class to assess,
not an asserted invariant. The assessment must also compare the old
finite-residue and valuation-potential obstructions without treating
them as a prohibition on every use of paired histories.

The saved target text is unchanged. The main gap is universal eventual
descent. A certificate for these paired histories could establish
restricted suffix rigidity at arbitrary depth. It would still leave a
bound on non-descent depth for each fixed start and the treatment of
other block types unresolved. No passage from rigidity to those further
claims is assumed.

## Conclusion

The assessment is complete under SPECIALIZE. Standard inverse arithmetic
and invariant verification methods are available by citation. Their
application does not supply the required invariant. No new inequality,
transition calculation, impossibility result, or mathematical lemma is
claimed in this review; the full target's coverage was not established
by the bounded search. Completed-step classification: NOVELTY_UNCHECKED.

The achieved bounds remain analytical rigidity through three blocks and
the saved exact paired screen through depth 11. The required assertion
concerns every depth. General synthesis theorems add a way to test
certificates, but do not extend either local bound.

The assessment supports a specified certificate test as a possible
continuation; it does not support more depth enumeration or unbounded
coefficient searches. This is the third consecutive EXPLORATION turn.
The current exploration batch stops here with its assessment finished;
the screened target is retained for resumption under the shared stopping
policy. No budget or runner state is reset. PROGRESS.md remains the sole
current checkpoint and action record.

## Proof

This section gives inspected citations and applicability comparisons,
not a proof of the proposed invariant.

### Reused Collatz arithmetic and inverse-tree assessment

The [previous assessment](2026-09-26-current-target.md) already records
the primary statements and their versions. Its unchanged arithmetic
comparisons are reused:

- Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers and
  Euclidean Embedding*, INTEGERS 19 (2019), A8,
  [Lemma 1 and Theorem 1, pp. 2–4](https://math.colgate.edu/~integers/t8/t8.pdf#page=2),
  supply the finite parity-word congruences and affine formulas.
- Andaloro, *On Total Stopping Times Under 3x+1 Iteration* (2000),
  [Lemma 2 and the remark after Theorem 1, pp. 74–75](https://www.mathstat.dal.ca/FQ/Scanned/38-1/andaloro.pdf#page=2),
  cover the odd-only coalescence of x and 4x+1, with the time convention
  qualifications recorded in that assessment.
- Monks et al., *Strongly Sufficient Sets and the Distribution of
  Arithmetic Sequences in the 3x+1 Graph*,
  [arXiv:1204.3904v2, sections 4–5](https://arxiv.org/pdf/1204.3904v2),
  give inverse admissibility, Theorem 5.1's endpoint uniqueness for a
  fixed infinite reverse word, Lemma 5.4's asymptotic parity restriction,
  and Theorem 5.7's residue visitation result.

None of those inspected statements retains the two original thresholds
and the block offset. They support L012's existing arithmetic, so
reproving that arithmetic or the coalescence identity is unnecessary.
The earlier LaDue finite coalescence comparison is also retained without
claiming that it addresses suffix minima. The Tao comparison in
foundations still allows exceptions and a diverging orbit-minimum bound;
it cannot supply this universal exclusion.

### Linear inductive assertions over real variables

Michael A. Colón, Sriram Sankaranarayanan, and Henny B. Sipma,
*Linear Invariant Generation Using Non-Linear Constraint Solving*,
CAV 2003, LNCS 2725, pp. 420–433. Read the
[author manuscript, sections 2–3, PDF pp. 3–7](https://theory.stanford.edu/~sipma/papers/cav03.pdf#page=3),
including Definition 2, Theorem 1 (Farkas' Lemma), Theorem 2, and its
following qualification. For a fixed number of conjuncts, Theorem 2
characterizes inductive linear assertion maps through coefficient
constraints. Theorem 1 concerns real variables. The text distinguishes
this completeness from proving every true invariant: stronger assertions
outside the chosen convex class may be needed.

This is a supporting synthesis method, not a Collatz theorem. Using it
here would require a justified model of the integer guards, minima,
initial tails, and terminal test. No such model is constructed this turn.
A sound relaxation could certify a positive result; failure in that
relaxation would not exclude a certificate for the original integer
system. The method's coefficient constraints can be nonlinear even
though the desired assertion is linear.

### Integer guards and bounded certificate searches

Aaron R. Bradley, Zohar Manna, and Henny B. Sipma,
*Termination Analysis of Integer Linear Loops*, CONCUR 2005.
Read the [author manuscript](https://theory.stanford.edu/~arbrad/papers/z.pdf),
Definitions 2–6 (PDF pp. 3–4), Theorem 1 and its limitation (p. 8),
and section 4, especially Definition 15 and Theorem 2 (pp. 9–11).
The input language retains constant division, modulo, and Boolean
guards. Theorem 2 covers a fixed conjunction size and integer
coefficients in [-2^(D-1),2^(D-1)), under its specified bisection and
corner-selection rules. Increasing D indefinitely need not terminate.

This is the closer method for L012's congruences. Its relevance is
conditional on an exact encoding of the augmented state. It supplies
verification and a bounded synthesis guarantee, not an assertion that a
separator exists. A failed coefficient box is only a result about that
box; it cannot justify an unrestricted impossibility claim. The needed
property excludes terminal pairs; proving termination of all backward
paths would impose an additional, unnecessary demand.

### Limits of automatic integer invariant inference

Sharon Shoham, *Undecidability of Inferring Linear Integer Invariants*,
[arXiv:1812.01069v2, 2018-12-06](https://arxiv.org/pdf/1812.01069v2).
Read section 2 and Definition 1 (pp. 1–2), the example and proof in
section 3.1 (pp. 2–4), and Theorem 1 (p. 7). The theorem concerns
existence of a safety invariant in quantifier-free linear integer
arithmetic for arbitrary systems and properties in that language. The
example is safe but has no invariant in that language.

This is a limitation of a general inference problem, not an obstruction
proved for the present Collatz system or a fixed template. It prevents
using safety or an ever-growing automatic search as a guarantee that
this certificate will eventually appear. Neither the example nor the
undecidability reduction is transferred to L012.

### Related Collatz invariant and termination claims

Sebastian Angermund, *A Two-Operator Calculus for Arithmetic-Progression
Paths in the Collatz Graph*,
[arXiv:2506.19115v1, submitted 2025-06-23](https://arxiv.org/pdf/2506.19115v1).
The PDF title page is dated June 25. Read Definition 5.1 (p. 4),
Proposition 6.1 (p. 5), and Theorem 7.1 with Lemma 7.1 and proof
(pp. 7–8). The latter treats indefinitely consecutive odd shortcut
steps, using an affine relation between progression parameters. It
does not address mixed maximal blocks or paired suffix minima. Its
scope is already within the local odd-run analysis. It is a scope
comparison only; no broader claims from the manuscript are imported.

Mishel Carelli, *Loop Termination and Generalized Collatz Sequences*,
[ICALP 2026, LIPIcs 374, article 175](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.175/LIPIcs.ICALP.2026.175.html).
Read the published HTML, sections 1–2, Theorem 14, section 4's
Conjectures 15–16 and Propositions 17–18, and Theorem 20's statement.
Theorem 14 concerns cycles in a one-variable single-path
linear-constraint loop; Theorem 20's termination algorithm is conditional
on the stated Reachability Conjecture. Proposition 17 forces an unbounded
generalized Collatz sequence to visit at least two residue classes.
These results do not match the paired, branching system with two
thresholds. In particular, they do not give an unconditional all-depth
certificate here. The full-version link was identified, but no claim
depends on material beyond the published statements inspected.

## Mathlib

Full invariant target: **not checked**. Supporting library coverage for
linear arithmetic, Presburger reasoning, Farkas' Lemma, and invariant
verification: **not checked**. No verified Mathlib theorem name or
library link is recorded, and no absence from Mathlib is asserted.
The direct links above document mathematical sources only.

## Search record and source limits

Queries actually used on 2026-09-27 included:

- `Collatz "linear invariant" "minimum"`
- `Collatz "inductive invariant" linear`
- `linear invariant generation nonlinear constraint solving Colon Sankaranarayanan Sipma 2003 polyhedra`
- `Collatz inverse tree "minimum" "stopping"`
- `Collatz "linear invariants" -site:reddit.com`
- `Collatz nondecreasing trajectories merging suffix minima`
- `Collatz "polyhedral" invariant`
- `Collatz "paired" "invariant" -site:reddit.com -site:preprints.org`
- `Collatz "suffix minima"`
- `"Termination Analysis of Integer Linear Loops" 2005 CONCUR`

The synthesis searches were followed to the authors' full manuscripts;
Bradley–Manna–Sipma's reference to the CAV 2003 method was checked
against that manuscript. The general-inference search was followed to
Shoham's versioned paper. The Collatz/polyhedral search was followed
to Carelli's published theorem statements. A secondary hit advertising
an affine invariant was followed to Angermund's primary manuscript and
its actual consecutive-odd-step theorem. Search snippets and purported
full solutions were not used as mathematical evidence.

An additional lead, Tee Hui Teo,
[*Binary Suffix Reductions for Collatz Descent: Trailing-One Classification
and Parameterized Certificates*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7494358),
appeared with a September 22, 2026 posting date. Only search-indexed
metadata and the abstract were available; opening the page failed.
Its theorem statements remain unread and no coverage conclusion is
drawn from it. It is not an essential premise for the imported synthesis
methods. The earlier assessment's unread Wirsching and Garner leads
remain unread; no theorem from them is assumed. These limits preclude
any exhaustive novelty claim, but leave no inaccessible essential input
for the proposed certificate test.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
page dated July 7, 2021, was rechecked on September 27, 2026. It still
requires reaching 1 for every positive integer under the unshortened
map. No change to the local target or time conventions is needed.

## Relevance, previous failures, and discriminating test

The shared and local instructions, complete overview, DAG, L011/L012,
Attempt 008, and the previous paired test and histories were inspected.
L001/L003's bounded-window obstructions and L004/L006's valuation
correction obstructions, as recorded in the overview, concern different
certificate classes. They neither supply this invariant nor refute it.
L010 already refutes unrestricted inverse uniqueness. L011/L012 retain
two independent starting thresholds precisely because unrestricted
merging or forced local contractions cannot decide compensation.

The proposed specialization must use the existing transitions and check
three obligations: initialization on both L012 tail families,
preservation on every admissible paired inverse with both suffix minima
retained, and exclusion of simultaneous non-descent after the companion
side's additional inverse. The block offset and original starts remain
part of the specification. A fixed number of affine inequalities and
any coefficient bounds must be stated before a bounded search. This is
a test specification; the augmented encoding and any coefficients have
not been derived or checked here.

Continuing would be justified by an exact certificate satisfying all
three obligations, or by a rigorously informative obstruction to a
specified certificate class. An admissible pair of original histories
meeting both thresholds would refute the rigidity repair. In contrast,
a real relaxation witness must first be checked for integer
admissibility, and an empty bounded coefficient search excludes only
its declared range. A timeout or more finite-depth agreement would not
justify another enumeration turn. Any changed certificate class needs
its own assessment rather than silently extending this one.

The present review supplies new source comparisons and a precise
method limitation, but no mathematical advance or Collatz-specific
negative result. It is therefore EXPLORATION, not ADVANCE or NEGATIVE.
The third-turn assessment and continuation/stop decision are complete:
retain the screened invariant test for possible resumption, and stop
this exploration batch. No candidate proof or disproof appeared.

## 2026-10-03 supervisor recovery

The saved target above is unchanged for this completed review. Its prior
assessment is sufficient and is reused without mechanically repeating
the paired-invariant searches or source retrievals. No essential input
to that method is inaccessible. The unread leads remain unassumed.
The recovery request requires a different future target, so retaining
this action as the current continuation would not repair the exhaustion.

The gap is still earlier growth compensating the forced contractions.
The proposed paired invariant would address restricted all-depth suffix
rigidity, with fixed-start depth control and other block types left open.
The achieved analytical depth is three; the saved screen reaches eleven.
Neither meets the all-depth requirement. The prior initialization,
preservation, and terminal-separation test remains the correct test of
this certificate class; no coefficients have been searched this turn.

### Three mechanisms compared

| Mechanism | Inspected evidence and relation to previous work | Recovery decision |
| --- | --- | --- |
| Paired linear invariant with suffix minima | Reuse the complete screen above. General certificate synthesis supplies no local certificate, and the finite paired screen leaves compensation unresolved. | Park the exhausted batch; preserve L011/L012 and their tests. |
| Diophantine exclusion of periodic orbits | Hercher, arXiv:2201.00406v3 (2023-04-04), Definitions 4–5, pp. 2–3, and Theorem 23 with its proof, pp. 15–16, exclude nontrivial cycles with at most 91 local minima, using the paper's stated verification input. | Covered finite-cycle exclusions should be cited, not reproved. No argument for all cycle sizes or divergent orbits was supplied by this comparison; do not activate this route. |
| Forward modular graph and parity imbalance | Monks et al., arXiv:1204.3904v2, section 6 definitions, pp. 16–17, Theorem 6.4, pp. 22–23, and Proposition 6.5, pp. 23–25, give qualitative visitation and graph criteria. | Select effective hitting-time control as a different intermediate gap; its exact quantitative statement still needs review. |

The graph mechanism controls one forward path across unrestricted
shortcut steps. It uses no paired merge, suffix minima, decoder
uniqueness, or endpoint-density count. The proposed time bound depends
on the starting size; Attempts 001 and 003 refute common bounded
windows, not this specification. This distinction does not establish
the proposed bound.

The modular theorem requires neither reproof nor a new local lemma in
this recovery. It does not give the paired separator. A quantitative
avoidance bound could support a later induced-return analysis on a
residue class and a finite base set; descent after visitation remains
an independent unresolved step. There is no claim of progress beyond
the inspected literature.

### Search and reading record

Queries executed on October 3:

- `Collatz strongly sufficient sets arithmetic sequences Monks 1204.3904 theorem`
- `Collatz nontrivial cycles m cycles Simons de Weger 2005 pdf`
- `Collatz sufficient set residue classes minimal counterexample descent Andaloro 2000`

The Monks manuscript's graph definitions, Proposition 6.2 and its proof,
Proposition 6.3, the complete proof of Theorem 6.4, and the statement
and forward-path argument of Proposition 6.5 were inspected. The PDF
margin identifies v2, 2012-04-20, while its retrieved title page reads
November 27, 2024; retain the exact versioned URL rather than infer a
different revision. The newly inspected section 6 extends the previous
assessment's section 4–5 reading.

Hercher's version is identified by its PDF margin as v3, 2023-04-04.
Read its cycle definitions, numerical input convention, and Theorem 23
with its proof. Its computational verification and all cited inputs
were not independently audited, and it is not an essential premise of
the selected graph direction. The author-hosted Simons–de Weger
[2005 PDF](https://math.deweger.net/papers/%5B35%5DSidW-3n%2B1-ActaArith%5B2005%5D.pdf)
opened but produced no extracted text. Its theorem statements were not
read, no result is imported from that file, and dependent work is parked
without repeating access attempts. New search hits claiming stronger
cycle bounds were not read or relied on; no latest-bound claim is made.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
page dated July 7, 2021, was read again: every positive integer must reach
1 under the unshortened map. The target and local conventions are
unchanged. Prize rules are outside this mathematical review.

The different target has a
[REVIEW_REQUIRED assessment](2026-10-03-mod27-effective-hitting.md).
Its quantitative source search and comparison have not been performed.
The present recovery is EXPLORATION, not a mathematical advance or
informative negative result. It adds primary-source comparisons and a
concrete different test; it does not merely repeat the previous stop.
The exhausted batch's three turns are preserved, with this recovery
recorded separately. No scheduler state or counter is edited. Full
Mathlib coverage for either the paired certificate or the graph-bound
target remains **not checked**. No complete candidate appeared.
