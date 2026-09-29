# Paired states and suffix minima: literature assessment

TARGET: Test whether a linear invariant in the two paired states and their suffix minima can exclude simultaneous non-descent for the four-block alphabet while preserving the one-block depth offset.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searches on 2026-09-27 covered Collatz paired and linear invariants, suffix minima, inverse-tree stopping conditions, polyhedral invariants, and integer invariant synthesis; exact queries and inspected sources appear below.
SOURCE_EVIDENCE: Read Colón–Sankaranarayanan–Sipma (CAV 2003), Theorems 1–2, https://theory.stanford.edu/~sipma/papers/cav03.pdf; Bradley–Manna–Sipma (CONCUR 2005), Definitions 2–6 and Theorem 2, https://theory.stanford.edu/~arbrad/papers/z.pdf; Shoham, arXiv:1812.01069v2, Definition 1, section 3.1 and Theorem 1, https://arxiv.org/pdf/1812.01069v2; additional Collatz comparisons and reused citations are identified below.
COMPARISON: Known methods cover checking and searching specified linear inductive certificates; no inspected theorem supplies the requested certificate for the paired histories, and real-variable completeness does not establish completeness for their exact integer guards.
GAP: Find or obstruct a linear certificate preserving both suffix minima and the one-block offset and excluding every terminal pair whose starts each meet their own non-descent threshold.
REASON: Reuse established invariant verification and synthesis methods; the remaining specialization is the exact paired integer system and its safety separator, whose existence is unresolved. The third exploration turn completes this assessment without resetting the budget.

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
