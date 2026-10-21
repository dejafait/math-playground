# Full initial height of growing postspell chains — source comparison

TARGET: Assess whether every positive residue-20 chain of K>=1 actual words W(J,H)=(OOEO)^J O^H E^2, with J>=2,H>=3 and exact two-step even tails at every word, must have initial root n0>=2^K, using exact parity constraints and extendible inverse rigidity.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-postspell, prescribed-parity and initial-height queries on 2026-10-06; inspected new lower-bound and endpoint-residue sources and reused the three prior postspell assessments; no exact matching theorem located, without a novelty claim.
SOURCE_EVIDENCE: L020/L021 coding and composition ranges and full L022–L024; Rozier arXiv:1510.01610v4 Hypotheses 2.2/2.3, Lemma 2.4, Theorem 2.6 and Lemma 6.1 with proofs; Sodelin F-BOUNDED-ALPHABET-ENDPOINT-GATE-001 sections 1–5; Wang arXiv:1809.02278v3 Propositions 2.3/2.8, Lemma 4.1 and Theorem 4.2 with proofs; Kramer arXiv:2607.10041v1 sections 3.2–3.4, Theorem 1 and proof; further scope comparisons below.
COMPARISON: No inspected result decides n0>=2^K; broad entropy-height coverage is conjectural or has incompatible hypotheses, and fixed-endpoint counts do not control moving endpoints. Finite endpoint representatives and their carry cost provide a distinct source-covered mechanism to test, rather than L022's vacuous affine minimum or L024's replenishable coordinate.
GAP: Whether the exact word language and L023's qualified rigidity force a sufficiently late positive endpoint carry, or another root-controlled constraint proving the exact threshold, remains unproved; finite compatibility, uniqueness and residue-rate necessity alone do not suffice.
REASON: The changed full-height threshold now has a bounded theorem comparison and a concrete discriminating carry test; approve one mathematical attempt at the unchanged TARGET. No essential source remains inaccessible and no new mathematical result is derived here.
SCOPE: Full J>=2,H>=3 alphabet with positive odd residue-20 boundaries and every exact E^2 tail; one symbolic endpoint-residue/carry test of n0>=2^K using L020–L024, with a guarded obstruction allowed. No enlargement of the nine-word minima screen or revival of the valuation-only budget.

## Exact scope, relevance and source statement

Use the shortcut map of L020–L024: O denotes its actual odd branch
and E its actual even branch. Each word begins at a positive integer
congruent to 20 modulo 27, and its endpoint is again positive and
congruent to 20 modulo 27. Exact two-step even tail means that the
two final input states are even and the endpoint is odd, at every
word including the last. All J,H are integers in the displayed
ranges and may vary from word to word. No least-root filters,
convergence, extra preceding word, or infinite-chain realization
is assumed. In particular L023's earliest-boundary exception must
be retained, rather than assuming every predecessor is extendible.

The main gap remains universal eventual descent. A bound by full
initial height could force a fixed positive start to leave this
restricted growing alphabet. Universal entry, other block types
and later compensation would remain unresolved. This is a proposed
intermediate target, not a new result or an assertion that the
threshold is true. It changes both the duration coordinate and
the mechanism from L028's CRT companion obstruction.

Rechecked [MathPrize](https://mathprize.net/posts/collatz-conjecture/)
on 2026-10-06: page dated 2021-07-07, “Collatz conjecture” statement
and displayed f. The exact claim is eventual arrival at 1 for every
positive integer under even x/2 and odd 3x+1. The notebook shortcut
compresses the obligatory halving after each odd step. This matches
the saved target; reward rules are separate.

## Local duplicates and preserved failures

Read L020 through its actual-word/CRT construction, L021 through its
joint guarded realizability argument, and all of L022, L023 and L024.
Read Attempts 012/013 and histories 033/037. Reuse the source inspections
in [growing-chain coverage](2026-10-04-growing-postspell-initial-size.md),
[inverse coverage](2026-10-05-postspell-extendible-inverse-rigidity.md)
and [inverse-to-height coverage](2026-10-05-postspell-inverse-to-height.md).

L022's exact-tail four-word witness refutes the repeated-W(2,3) minimum;
its root 11,553,444,320,785,499 is above the present threshold 16,
so it is not a counterexample here. Its two-word witness has an even
final endpoint and does not meet this target. The finite minima for
K<=5 concern nine labels and cannot settle unbounded parameters.
The negative positive-endpoint estimate remains stopped.

L023 permits at most one extendible predecessor of a fixed endpoint.
The first root has no assumed preceding word. L024's finite chains
with starting valuation 10 have roots varying with length; its
replenishment proof is not a violation of the full-height inequality.
The finite coding, offsets and qualifications are available inputs;
none of these lemmas supplies the missing root-height budget.

## Primary theorem comparisons

**Broad initial-height bounds.** Olivier Rozier,
[*The 3x+1 problem: a lower bound hypothesis*, arXiv:1510.01610v4](https://arxiv.org/html/1510.01610v4),
2016-11-17, published *Funct. Approx. Comment. Math.* 56 (2017), 7–23.
Read section 2.2 and section 6.1, including the displayed hypotheses
and proofs. Hypothesis 2.3 asserts
n>=j^(-C)2^((1-H(q/j))j); it is not a theorem.
Lemma 2.4 covers q/j<=1/2. Theorem 2.6 assumes distinct states and
q/j<=1/log_2(3), with its entropy refinement requiring q/j<=0.609089767….
Those ratio guards do not cover these growing words: L022 already
records their affine multiplier greater than one. Lemma 6.1 proves
an exponential minimum for exactly one even input, using both bounds
on its unique even position; our whole chains have multiple even
inputs. Applying it to a subword would retain a later input height.
None is an unconditional full match. The heuristic LBH must not be
inserted as a premise.

**Finite endpoint carries.** Sodelin,
[*Route F checkpoint — bounded-alphabet endpoint-residue gate*](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/routes/F_bounded_alphabet_endpoint_residue_gate.md),
claim F-BOUNDED-ALPHABET-ENDPOINT-GATE-001, live main read 2026-10-06,
sections 1–5; no immutable revision or checked Lean build obtained.
It uses exact accelerated valuations 1<=a_k<=A and representatives
1<=M_k<3^k satisfying 2^(q_k)M_k=C_k modulo 3^k.
Its carry equation (3) is
2^(a_k)M_(k+1)=3M_k+1+t_k 3^(k+1).
Read the proof of 0<=t_k<2^(a_k), both impossible-sign cases,
and (7)–(9): positive carry costs M_(k+1)/3^(k+1)>=2^(-a_k),
whereas a realizing root N gives M_k<=x_k<(N+1)(3/2)^k.
These arguments use only a finite prefix. Exact shortcut tails allow
compression into accelerated steps with valuations at most 3; the
factor two already included in O must be counted. No infinite
realization is needed to use these finite bounds. The source supplies
no forced late carry for this language. Its infinite equivalence is
not an escape theorem; no converse is used to manufacture a chain.

**Prior endpoint machinery.** The Route F references were followed.
[Wang, arXiv:1809.02278v3](https://arxiv.org/html/1809.02278v3),
2019-04-30, lists SanMin Wang and a periodicity title; this differs
from Route F's bibliographic author label. Read Propositions 2.3/2.8
and their reconstruction/stabilization proofs, Lemma 4.1 and
Theorem 4.2 with proof. Finite canonical starts are nondecreasing,
not exponentially increasing; the general nonperiodic escape claim
is Conjecture 1.2. Theorem 4.2 requires nonperiodicity and limsup
b_n/n>log_2(3), an additional drift hypothesis not supplied here.
Section 4's structured-code cases are not statements for arbitrary
J,H. No Wang result is imported as the desired bound.

[Oliver Kramer, arXiv:2607.10041v1](https://arxiv.org/html/2607.10041v1),
2026-07-10, sections 3.2–3.4, Theorem 1 and complete proof, gives
necessary vanishing of start/endpoint residue rates for a fixed
positive realizing root. Its endpoint comparison retains that root
and does not force this word language's representatives to be large.
It supports the diagnostic, not the sought uniform estimate.

**Other apparent matches.** Rozier–Terracol,
[arXiv:2502.00948v5](https://arxiv.org/html/2502.00948v5), 2026-05-17:
rechecked Definition 2.1, Lemma 2.3 and Theorem 2.4 with proofs,
including q=0. Their parity-order bounds control the affine remainder,
not the least positive initial CRT representative. Reuse the older
finite-coding assessment; there is no new general coding proof to write.

Fernández–Ibáñez,
[*Christoffel words as extremal structures in Collatz dynamics*, arXiv:2607.24844v1](https://arxiv.org/html/2607.24844v1),
2026-07-24: read sections 2–3's finite-word/cycle distinction,
Theorem 7.3 and Theorems 8.1/8.2 with their displayed proofs.
The arithmetic bound in 8.2 is an upper bound for a periodic orbit's
minimum and requires periodic closure. Our finite growing chains
have no such closure. It is not an initial-height lower bound.
No extremal theorem from this unrefereed version is a dependency.

The reused Applegate–Lagarias and Krasikov–Lagarias assessment
already compares quantitative inverse-tree counts with a moving
endpoint. Their endpoint-dependent counts do not resolve this target;
unchanged coverage was not browsed again.

## One approved discriminating attempt

Keep the exact TARGET. Test the finite endpoint-carry mechanism using
the sourced definitions and bounds (3), (7)–(9), L020/L021 actual
coding and L023's residue obstruction. Express indices in accelerated
odd steps and translate back to K complete words. The open obligation
is a language-forced carry sufficiently late to give the exact
n0>=2^K margin, uniformly in J,H. This is a proposed sufficient
mechanism, not an assertion that such a carry exists.

Account for the earliest-boundary exception, every offset, positivity,
residue guard and exact last tail. If diagnostics are needed, use
fully replayed actual chains to test the proposed carry condition;
a small guarded counterexample is enough to stop that condition.
Do not enlarge the nine-word minima table, assume all predecessors
extend, reuse boundary valuation nonincrease, or treat zero carry
as proof of convergence. No new screen is authorized merely for
increasing a finite minimum.

Continue only with an explicit constraint controlled by n0 whose
carry position and margin can be proved uniform over the full
alphabet. Abandon this sufficient mechanism if an actual chain
violates the needed carry condition or the estimate retains only
an uncontrolled endpoint/parameter term. A chain with n0<2^K
refutes the target itself; failure of an auxiliary carry condition
does not. With neither evidence nor a usable constraint, record
EXPLORATION and reassess; do not repeat the failed affine estimate.
Universal entry, other block types and later compensation remain open.

## Search record and limits

Queries executed on 2026-10-06:

- Collatz "(OOEO)" "height"
- Collatz "parity" "lower bound" "starting value" consecutive increasing
- Collatz "postspell" chain
- Collatz "postspell" "2^K"
- Collatz parity words uniform lower bound integer realization restricted language
- Collatz "initial value" "long" "growth" lower bound parity Rozier Terracol
- Rozier "3x+1 problem" "lower bound hypothesis" arxiv
- site:github.com/Sodelin/Collatz-Conjecture-Work "postspell" "height"

Search snippets and generic solution claims were not theorem evidence.
Density-descent, automata and regular-language leads outside the
exact hypotheses remain unread and nonessential to this bounded test.
No search establishes novelty. Source access succeeded; there is no
persistent source blocker and no cross-notebook input.

## Mathlib and completion

Full height target, endpoint-carry specialization and supporting
Mathlib coverage: **not checked**. No absence or formal verification
is asserted. This is LITERATURE / EXPLORATION / NOVELTY_UNCHECKED,
actual task type literature_comparison. It derives no new lemma,
runs no mathematical script and spends zero mathematical exploration
turns. The exact target is ready for one separate research invocation;
STATUS remains IN_PROGRESS and no complete candidate exists.
