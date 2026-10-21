# Aggregate renaming-seed compression: source comparison

TARGET: Assess whether the B-substituted aggregate initial-seed contribution at K_n in L099 admits polynomial-size affine ABPs when arbitrary sharing, cancellation and refactoring are allowed.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped searches of L099/L033/L097/L087, renaming drafts and histories 385–388, and Attempts 020/032 found no completed aggregate bound; external searches for noncommutative ABP renaming, orbit sums, coefficient ranks and factorization located the primary results below, without an exact S_n match.
SOURCE_EVIDENCE: Read Nisan STOC 1991 Definition 1/Theorem 1 and both proof directions, plus Theorem 4; Raz–Shpilka author manuscript Definition 1/Lemma 2 with Steps 1–5; Arvind–Joglekar–Rattan arXiv:1501.00671v1 Theorem 2.7 and proof, printed pp.6–7. Reused L033's audited F₂ finite-constant-closure specialization.
COMPARISON: Nisan supplies a homogeneous coefficient-rank criterion, not this aggregate's ranks; L033 treats affine DAGs over F₂ with two generators, whose finite-alphabet specialization must be justified in an application. Factorization preserves the input representation type and does not imply circuit-to-ABP compression.
GAP: Establish a coefficient-rank obstruction or polynomial full explicit affine-ABP representation for exact S_n; this review establishes no aggregate coefficient/rank, ABP upper bound or full-certificate hardness.
REASON: Essential coverage is adequate for one bounded coefficient-cut attempt on the unchanged target; the literature supplies a cancellation-sensitive discriminator without deciding this instance. A failed search is not evidence of novelty.
SCOPE: The exact TARGET and recurrence below over the free F₂ algebra, explicit acyclic affine-edge ABPs, and original Q of L099; coefficient-cut testing and ordered refactoring of this same polynomial only.
LITERATURE_REASON: The changed model permits cancellation and arbitrary sharing excluded by literal-copy coverage; the essential new comparison is exact-output coefficient rank and representation-preserving factorization.

Step 389 completes the review proposed in step 388. This EXPLORE decision
is specific to this exact target; it does not broaden the literal-copy
audit assessment. No mathematical attempt on S_n was performed here.

The exact object is the initial-seed contribution defined by L099's
recurrence (1), with every later axiom seed Z_i set to zero, followed by
B substitution. Equivalently, as a definition of the review target, put

    a=x_1…x_n,  p=a+a²,  S_0=p,
    S_i=ρ_i(S_(i−1))p+S_(i−1)(1+ρ_i p)p  (1≤i≤n).

The requested output is S_n, before the final multiplier b. Maps ρ_i
are L099's disjoint swaps of x_i and x'_i. Work in the free F₂ algebra,
retaining exact ordered equality. The size measure is full explicit
acyclic affine-ABP encoding, including the alphabet and binary indices,
against L099's original Q≤C(n+2)³. Gates or implicit orbit descriptions
are not substitutes for explicit output graphs. No bound is conjectured
or established in this note.

Essential local inputs are L099's audited recurrence and input family,
and L097's original extraction convention. L087 supplies the original-Q
dictionary charge. L033's cut-rank/affine-ABP proof has now been inspected
as a method, not an aggregate bound. Its field, finite-alphabet, affine
constant and homogeneous-component qualifications are explicit below.

A source-supported polynomial representation would show how a shared
aggregate can evade this part of the copy diagnostic; a superpolynomial
exact-output bound would obstruct compression of this isolated contribution.
Either outcome still leaves cancellation with later seeds, changing the
witness, occurrence normalization, full fg transfer, short-proof
availability, universal W₂ and unrestricted SAT unresolved. In particular
an isolated-contribution lower bound is not hardness of the full extracted
certificate. The existing easy alternative source proof remains available.

## Inspected primary coverage

**Nisan.** Noam Nisan, *Lower Bounds for Non-Commutative Computation
(Extended Abstract)*, STOC 1991, pp.410–418,
[DOI](https://doi.org/10.1145/103418.103462),
[nine-page primary mirror](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf),
retrieved 2026-10-20. Read §2 Definition 1 (PDF p.4), §3 Theorem 1 and
both proof directions (PDF p.5), and §4.2 Theorem 4 (PDF p.6).
The setting is real coefficients, homogeneous polynomials, consecutive
layers, homogeneous linear labels and vertex size. Theorem 1 equates
minimum ABP size with the sum of prefix/suffix coefficient-matrix ranks.
The lower direction factors a matrix through its layer; the upper
direction eliminates dependent prefix or suffix vectors. These operate
on the polynomial after cancellation. Theorem 4 treats the palindrome,
not S_n. We use the named method with local field/model qualifications,
without silently importing a real-rank theorem over F₂.

**Raz–Shpilka.** Ran Raz and Amir Shpilka, *Deterministic Polynomial
Identity Testing in Non Commutative Models*,
[author-hosted 16-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
retrieved 2026-10-20, no revision date printed. Read Definition 1 and
Lemma 2, printed pp.4–6, all five steps and runtime discussion.
Over a field without a characteristic restriction, Lemma 2 starts from
a size-s formula with zero constant term, constructing positive-degree
component ABPs of O(s²) vertices in O(s³) total time. Degree copies,
pruning, acyclic scalar-edge removal and component selection support
normalization operations, not polynomial conversion from shared
circuits. Neither its formula-specific runtime nor a zero-free-term
premise for S_n is imported without verification.

**Factorization.** V. Arvind, Pushkar S Joglekar and Gaurav Rattan,
*On the Complexity of Noncommutative Polynomial Factorization*,
[arXiv:1501.00671v1, 4 January 2015](https://arxiv.org/pdf/1501.00671),
20-page version, retrieved 2026-10-20. Read §2.2 Theorem 2.7 and proof,
printed pp.6–7. It gives randomized poly(s,d)-time variable-disjoint
factorization for circuit input, deterministic polynomial time for ABP
input. Its partial-derivative/PIT algorithm outputs circuits from circuits
and ABPs from ABPs. This does not supply a circuit-to-ABP conversion
for S_n. Variable-disjointness and polynomial syntactic degree must be
checked before any use. No factorization of S_n is imported or derived.

L033's audited proof provides finite constant-path closure and
coefficient factorization through the original N vertices, including
affine labels and cancelling paths over F₂. Its statement has two
generators. A later application must justify the same construction for
the finite 2n-generator alphabet and charge every label; this review
writes no generalization lemma. Distinguish an original-N bound from
a lower bound only on a larger normalized graph. Reproof is warranted
only for changed hypotheses/encoding, not the established palindrome.

## Searches and prior failures

Queries issued on 2026-10-20 included:

- `noncommutative algebraic branching programs rank Nisan homogeneous components arbitrary field factors lower bound`
- `noncommutative polynomial renaming symmetrization branching program orbit sum rank lower bounds`
- `noncommutative ABP "renaming" "rank"`
- `noncommutative polynomial "S_i" "rho" "branching"`
- `noncommutative algebraic branching program coefficient matrix rank arbitrary field affine edge homogeneous component`
- `noncommutative polynomial symmetrization independent variable swaps algebraic branching programs exponential`

No inspected result decides the displayed S_n. Results on monotone
ABPs, commutative ABPs, border complexity and general symmetric
functions are unread leads, not mathematical inputs. No snippet is
theorem evidence. Shell retrieval failed DNS resolution; primary PDF
text was accessible and read through the web tool, so essential source
coverage is not blocked.

Attempt 032/L099 stop whole-seed literal copying only. Attempt 020/L033
stop a universal degree-only same-output conversion, not every structured
family. The renaming drafts/assessments and histories 385–388 contain
no completed cancellation-sensitive aggregate test. L097's ordinary
axiom/MP graph does not remove renaming contexts; L087's original
dictionary ledger is not a compression theorem. All stops and unfinished
work remain. No cross-notebook input was read.

## Covered bounded attempt and decision test

The main gap is still a polynomial SAT algorithm or an unrestricted
lower bound. This intermediate target is exact-output ABP complexity
of one aggregate. Its lower-bound discriminator is an explicit family
of nonsingular coefficient submatrices of superpolynomial size in
original Q; the opposite discriminator is a polynomial-full-bit explicit
ABP for the same S_n. Neither result is asserted by this review.

One bounded mathematical attempt may test homogeneous coefficient cuts.
For chosen d and 0≤k≤d, rows are words u of length k, columns words v
of length d−k, and entries are [uv]S_n over F₂. This defines the test,
not a rank claim. Start at cuts that are multiples of seed-word length
n and seek one uniformly described submatrix; coefficients must come
from the aggregate recurrence with all parity cancellations retained.
Finite samples may guide, but cannot replace, an all-size argument.
The 2^n context count supplies no row-independence evidence.

Continue with an explicit all-size rank witness and justified affine-model
specialization, or an explicit ordered graph and full dictionary/bit
ledger. A bound 2^(c n), fixed c>0, would suffice against original
Q≤C(n+2)³; a polynomial rank lower bound would not decide compression.
If proposed rows collapse or off-diagonal terms survive, abandon that
proposed submatrix and record its exact failure, leaving the aggregate
question unresolved. Do not renew literal counting or blanket circuit
conversion. Low rank at one cut is not an upper bound for all components.

Continuation inputs are L099 §3 and step-388 audit (later Z_i=0 before
B), L097's extraction convention, L087's original-Q ledger, and the
Nisan/L033 affine-graph comparison. End before multiplier b. Later-seed
cancellation, changed witnesses, general occurrence normalization,
exact fg transfer, short source proofs, M-only bounds, universal W₂
and SAT remain independent gaps. An isolated-contribution lower bound
is not full-certificate hardness. Mathlib coverage is **not checked**;
no absence or matching formal theorem is claimed. No new lemma,
mathematical script, coefficient calculation or S_n bound was produced.
