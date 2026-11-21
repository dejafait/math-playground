# Actual theta coefficients and a prescribed Jensen primitive — source review

TARGET: Test a theta-specific one-step Jensen primitive margin for J^{d+1,n} from J^{d,n+1}, retaining the prescribed constant gamma_n and the boundary n=0.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact primitive, real-rooted-antiderivative, inverse-Rolle, Jensen critical-value and integration-constant searches completed; queries and primary ranges below. Narrow local searches found no earlier exact primitive-margin assessment. Reuse the September21 shifted-Jensen screen and October31 O'Sullivan comparison; no novelty inference.
SOURCE_EVIDENCE: Pereira arXiv:1901.08156v2(17April2019), pp.1–2, introduction/Lemmas1.1–1.2/Corollary2.1/Theorem2.2; Dimitrov–Kostov JMAA376(2011)385–392, Theorem1, section2/(7)–(8)/Proposition1 and section4; O'Sullivan arXiv:2007.13582v2(9December2020), (1.2)–(1.4), (3.1), Corollaries3.2–3.3, Theorem3.5/proof, Theorem8.1/(8.2)–(8.5). Prior Griffin et al.v3 comparison reused.
COMPARISON: The inspected primitive theorem supplies the constant interval, not an actual-theta estimate placing gamma_n in it. Very-hyperbolic conclusions have an LP premise. Neither closes the prescribed margin; no mathematical subtarget of this transfer is approved.
GAP: Actual critical values at the prescribed constant, input hyperbolicity, repeated-root compatibility, uniform degree control and descent initialization remain unpaid, including n=0.
REASON: The bounded search found no adequate match or independently justified theta-margin mechanism. Park this transfer with the source-scope obstruction; EXPLORE records the search decision, not an all-degree result or readiness to assume the margin. A new theta estimate is required to reopen.
SCOPE: Source comparison for d>=2,n>=0 and actual gamma_j=j!M_(2j)/(2j)!. No new lemma, theta estimate, mathematical script, or primitive proof is produced. Downstream L030/C032a remain criteria only.
LITERATURE_REASON: The step378 nomination explicitly lacked essential prescribed-primitive and multiple-root source coverage; unchanged large-shift coverage was reused.

## Completed comparison — step379

The main gap is actual-Xi all-degree positivity. The selected intermediate
margin could support shift descent, but would not by itself supply its
input hyperbolicity or a complete descent chain. The threshold remains
zero at every signed critical value. The nomination's continuation test
fails in the sources checked: only a general criterion and conditional
closure are supplied. This is a source-scope negative, not a proof that
no such theta estimate exists.

**Hypotheses and prescribed constant.** Rajesh Pereira,
[*Which quartic polynomials have a hyperbolic antiderivative?*, v2](https://arxiv.org/pdf/1901.08156v2),
pp.1–2, gives the following criterion (introduction and Lemma1.1).
For monic p=product_(k=1)^d(x-w_k), real w_1>=...>=w_d counted
with multiplicity, and F'=p, the admissible constants for F-c are

    max_(k odd) F(w_k) <= c <= min_(k even) F(w_k).

Weak inequalities include repeated roots; the list must be the full
root multiset, not arbitrary repeated stationary points. At coincident
opposite-parity entries both signs must hold. For distinct roots and
strict inequalities, the interval argument uses the two exterior rays
as well as all interior intervals. Weak endpoints permit multiple roots.
The rightmost critical value is the lower-sign one for a positive leading
coefficient, independently of degree parity. Lemma1.2 removes automatic
adjacent comparisons only for existence of some c. It cannot remove the
requirement to test a fixed c. Corollary2.1 and Theorem2.2 are likewise
existence tests, not a prescribed theta-constant theorem. No reproof is
needed or attempted.

**Normalization.** L018/L021/L028 match O'Sullivan's (1.2)–(1.3):
local gamma is the factorial-scaled sequence, not the raw moments.
Dimitrov–Kostov (7), or O'Sullivan (3.1), supplies the derivative identity
with factor d+1 for the nomination's degree d+1 polynomial. Consequently
its stated integral normalization is the prescribed primitive interface;
there is no extra constant to choose. Positive leading-coefficient
normalization must scale the constant as well as the primitive.
No bounds on its signed values follow from this identification.
The earlier screen's assertion that Griffin et al.'s gamma is literally
the same should be understood up to their common factor8: O'Sullivan's
text following (1.8) explicitly notes that factor. It does not change
hyperbolicity or the fixed-constant question when consistently applied.

**Conditional closure is not the missing input.** D.K. Dimitrov and
V.P. Kostov, [*Sharp Turán inequalities via very hyperbolic polynomials*](https://repositorio.unesp.br/bitstreams/1d015e15-3edd-475d-9a47-4e31dfc1edf4/download),
JMAA376(2011)385–392, DOI10.1016/j.jmaa.2010.12.014, Theorem1
and Proposition1 assume a real entire function in LP, with nonzero
Maclaurin coefficients. Section2 distinguishes Appell primitives of
arbitrary order from Jensen primitives of order only up to the shift;
section4 explicitly retains LP in the proof. This assumption is unavailable
for actual Xi and cannot be imported as an unconditional theta estimate.
Their normalization also retains the factorial factor. No suspect theorem
is reproved; this is a hypothesis comparison.

**A separate source method, not a descent theorem.** C. O'Sullivan,
[*Zeros of Jensen polynomials and asymptotics for the Riemann xi function*, v2](https://arxiv.org/html/2007.13582v2),
Theorem3.5 and proof, uses a fixed LP multiplier and an all-degree
hyperbolicity criterion. Its Hermite-family application does not supply
inverse Rolle. Theorem8.1 and (8.2) give an explicit sufficient coefficient
budget; the proof (8.3)–(8.5) obtains it in a large-shift regime. This
comparison was already recorded in the October31 signed-Hermite review
and is reused. Testing that budget at shift zero is a different, finite-
coefficient method test; it does not presuppose input root signs.

## Searches and limitations

Queries were `hyperbolic antiderivative polynomial critical values
integration constant real rooted Rolle`, `Riemann xi Jensen polynomials
primitive integration constant hyperbolicity`, `polynomial "hyperbolic
antiderivative"`, `polynomial "real-rooted antiderivative" critical`,
`Jensen polynomials Riemann xi "critical values"`, `Jensen polynomials
"antiderivative" xi`, `Jensen polynomials "integration" "constant"
hyperbolicity`, and the exact Dimitrov–Kostov title. Local duplicate
searches used inverse-Rolle, primitive-margin, Jensen-descent and exact
source identifiers in drafts/literature, ATTEMPTS and foundations.
The existing September21 failure remains the controlling large-shift
comparison; its source was not downloaded again. The October31
`actual-hermite-signed-cross-term-review.md` source paragraph was reused.

Read the primary ranges named above, including the constant-selection
argument, weak root order, quartic comparison, LP premises and the
Hermite sufficient-budget application. The original Souroujon–Stoyanov
2016 paper was located in author-uploaded search text, but not inspected
as a full primary document; Pereira's explicit statement is the citation
used here. Original Turán1959 TheoremIII is not newly inspected; use its
precise restatement in O'Sullivan8.1 as the cited standard input, as the
prior local assessment does. Farmer arXiv:2008.07206v2, section3 and
opening section4, was checked as a caution about lost derivative data;
its title is not an impossibility theorem. The Holland lead remains
unadopted; another high-shift range alone would fail the saved test.

A Planat2026 hit, DOI10.3390/math14111884, appeared in searches.
Direct publisher/DOI retrieval returned429 twice; indexed text suggests
a coefficient-normalization problem but is not used to certify an error
or adopt any obstruction theorem. This inaccessible lead is nonessential
to the criterion comparison and does not justify retrying the parked
primitive transfer. Mathlib coverage for the full prescribed-margin
statement and the imported finite criteria is not checked.

## Route decision

Park prescribed-primitive descent: no independently justified actual-theta
margin was identified. Preserve the proposal below and its original
pass/fail test. Reopening requires a concrete new theta estimate, not
another approval of the general criterion. A creative attempt is not
justified solely by naming the missing signs. The separately nominated
fixed-Gaussian budget test is a known-method specialization with a clear
failure threshold; no result of that test is asserted this turn.

## Original nomination from step378 — preserved context

## Why this is a different question

The main gap is actual-Xi all-degree positivity, equivalently the
unresolved full criterion recorded in L030–L032/C032a. The suggested
intermediate input would control one prescribed primitive using actual
theta coefficient information. It might support a descent in shift if
its input hyperbolicity and its margins can independently be supplied.
Neither a descent chain nor an all-degree theorem is asserted. A fixed
finite-degree check would be diagnostic only, not a new RH milestone.

The prospective object to compare with J^{d+1,n} is

    P_(d,n)(X)=gamma_n+(d+1) int_0^X J^{d,n+1}(t)dt.

This is a definition for the proposed review, not an established sign
or transfer result. Check its exact coefficient normalization. The
specific question is whether actual theta data constrain the prescribed
constant relative to the primitive's extrema, rather than whether some
freely chosen constant could give a hyperbolic polynomial. The future
attempt must retain all signed extrema and any multiple-root equality
cases. A derivative with real roots by itself is not approved as a
hyperbolicity premise for its primitive.

## Three-way continuation comparison

1. Repeating L762's trace/source audit has no remaining discriminator:
   step378 checks the all-N claim, while C761a retains its fixed-cell
   miss. Tightening this trace alone supplies neither a ground comparison
   nor actual-Xi signs. Close that audit sequence without banning a
   future independently justified prolate mechanism.
2. Generic admissible-kernel critical-value signing is contradicted by
   audited L738. Its positive stationary minimum survives the recorded
   shape hypotheses. Another generic shape inference is not selected.
3. The prescribed actual-coefficient primitive asks for different data:
   an integration constant compared with signed critical values. It is
   selected for source review, with actual-theta information required.
   The old shifted-Jensen stop remains evidence against using high-shift
   estimates at n=0, not a ban on every different transfer mechanism.

The existing failure records are
[the CCM fixed-cell miss](../../ATTEMPTS/2026-11-04-ccm-fixed-boundary-observable-miss.md),
[the generic critical-point stop](../../ATTEMPTS/2026-11-04-admissible-critical-point-shape-sign-stop.md),
and [the shifted-Jensen screen](../../ATTEMPTS/2026-09-21-theta-moment-literature-screen.md).
None is discarded or contradicted by this nomination. The separate
L727 and L617 assessments inspected during continuation triage already
have mathematical-audit records; they are not nominated for another
unchanged audit on the strength of stale overview labels.

## Required next-turn source review and bounded test

Read primary prescribed-antiderivative/hyperbolicity or inverse-Rolle
statements and relevant proof cases, including degree parity, exact
constant, strict versus repeated roots, and normalization. Search the
exact actual-Xi Jensen assertion, stronger results and known obstructions.
Reuse the existing large-shift comparison while its hypotheses remain
unchanged; do not browse it merely for another approval. Its later
Holland preprint mention is an unread lead, not an adopted theorem.

The source review succeeds only if it identifies a matching import or
states ready hypotheses for an independently testable actual-theta
margin, with zero as the signed-margin threshold. The general primitive
criterion by itself is not the desired theta estimate. A renamed
all-degree sign assumption, an adjustable constant, a numerical finite
sample or another positive-shift cutoff does not meet the test. If only
those are available, record the precise scope obstruction and park this
proposed transfer rather than renewing it by changing degree labels.

Essential local inputs to check are L021/L028 for coefficients and their
moment convention; L030/C032a give the downstream all-degree gap, not a
positive premise. L738 is a contrast only. No cross-notebook result is
used. Unresolved assumptions include simple input roots if required,
their availability for the actual family, all primitive margins,
uniformity in degree and any finite initialization of a descent chain.

No lemma, derivative identity, theta estimate or mathematical script
for this target is produced in step378. After coverage is ready, a
genuinely new actual-theta margin attempt could warrant creative routing;
it is not approved now. Mathlib coverage is unchecked. The next turn is
literature-only because this target's essential source interface is new.
