# L111 equality and descent — completed source comparison

TARGET: Assess whether Simons–deWeger Theorem3(b) covers L111's equality case and supports descent by j+1, retaining repetitions and a potentially partial final run.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected L110 equality assessment and the double-gap source comparison; searched L111's canonical statement, working/audit records and C110a for equality/descent coverage, and checked Attempts036–037. Retrieved the published primary PDF directly and located Theorem3(b), cycle definitions and Lemma15; no broad repeat search was needed.
SOURCE_EVIDENCE: Simons–deWeger, Acta Arithmetica117(2005),51–70, DOI10.4064/aa117-1-3: freshly inspected section1.1/p.51, section1.2/p.52, section1.3/pp.52–53, Theorem3(b)/p.55 and Lemma15 with complete proof/p.62; also inspected the referenced Corollary11/p.60 and Lemma14/p.61.
COMPARISON: The published closed-cycle exclusion allows arbitrary positive even-run lengths, nonminimal displayed periods and positional minima, so changing the middle length from1 to2 does not leave its scope. It supplies no open-endpoint bound; audited L111 supplies that separate cap. C110a is a method comparison only.
GAP: The canonical equality specialization and elementary combination with L111 remain unwritten and unproved here. The separate research turn must check closure, all extrema, the trivial-cycle exception and the unit-growth alternative without assuming terminal maximality for an open endpoint.
REASON: Essential source coverage is now adequate for a routine specialization of known cycle exclusion, followed by an elementary restricted descent consequence; no new cycle theorem or nondivisibility argument is needed.
SCOPE: Only L111's exact hypotheses and their equality/non-equality cases; no longer middle run, more peaks, divisor census, primitive-period restriction or universal first-drop assertion.
LITERATURE_REASON: The proposed next target changes from a finite open-word cap audit to a closed-cycle import and its restricted descent consequence; L110's existing approval explicitly covers length1 only.
COVERED_TARGET: Apply Simons–deWeger Theorem3(b) to L111's equality case and combine it with L111 to prove descent by j+1, retaining repetitions and a potentially partial final run.

## Exact scope and source evidence

Essential local input: audited L111, for actual words
1^a0^2 1^c0^d, n>1, a,c,d>=1, j=a+2+c+d,
all 3^{q_k}>=2^k for k<j and 3^{a+c}<2^j. Both odd runs and
the middle even run are exact; the final run is potentially partial.
The cap is proved and audited; equality exclusion and the requested
descent consequence are not established by this literature turn.
No hypothesis is asserted for every positive start.

Reuse the primary-source record and qualifications from
`2026-10-28-l110-equality-cycle-exclusion.md`:
[Simons and de Weger, *Theoretical and computational bounds for m-cycles
of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
Theorem 3(b), printed p.55](https://www.impan.pl/shop/en/publication/transaction/download/product/82263#page=5).
The published version was retrieved again on 2026-10-29. It uses the
same shortcut map (p.51). Section1.2 permits nonminimal periods and a
local starting minimum; minima are indexed by positions. Its trivial
m-cycle is the m-fold repetition of {1,2}. Nontrivial means containing
a value greater than2 (p.51). Theorem3(b) excludes nontrivial m-cycles
for 1<=m<=68. Its definitions impose no length-one middle even run.
Lemma15 and its full proof (p.62) already cover m=2: the upper bound
K<2.8037*10^14 conflicts with K>4.3116*10^14. Section1.3 records the
external computational bound X0=301*2^50 behind the estimates. Importing
the published theorem retains that computational basis; no independent
replay or reproof is claimed. No additional unproved conditional
hypothesis is attached to the theorem.

## Approved specialization obligations, deferred to research

Only the following routine application is covered. Under hypothetical
equality y=n, check an actual displayed period j against the source's
chronological parameters (k0,l0,k1,l1)=(a,2,c,d), K=a+c,
L=2+d. Check the proposed minima at positions0,a+2 and maxima at
a,a+2+c using the actual run statements. Closure must make the final
observed even segment exact in this equality case. Do not impose that
extra condition in an open-endpoint case. No numerical distinctness,
least-period or global-minimum requirement may be added.

Address the repeated trivial-cycle exception using the original odd
start n>1, rather than n>1 at an arbitrary even state. Apply the
published theorem only after actual closure; formal endpoint equations
or divisibility alone are insufficient. This application must be written
in a canonical corollary, with precise citation and qualifications.

For the separate open-endpoint combination, retain all L111 guards and
its audited integer cap. The only further work proposed is the elementary
integer/parity case split at y=n+1 and the next shortcut step, under
n>1 and the odd starting bit. C110a illustrates this argument but is not
a premise. No unit-growth exclusion or new theorem on divisibility is
needed. No such specialization or case-split proof is carried out here.

Continue only if the canonical application verifies all these matches.
A mismatch in closure, positional run count or exception treatment
stops the import; a mere cap without the final case split does not prove
descent by j+1. No source-scope mismatch was found in this comparison.
The plausible use is closure of this one family's remaining descent gap;
other shapes and universal finite-drop existence remain open. Matching
Mathlib coverage remains **not checked**, including supporting parity
and iteration facts; unknown coverage is not evidence of absence.

## Reuse, failures and decision

No existing L111 equality/descent corollary was found in the targeted
records; L111 explicitly leaves both cases open, while C110a has middle
length1. This is local bookkeeping, not a claim of mathematical novelty.
The double-gap source assessment already distinguishes open endpoints
from cycles, and that obstruction remains intact. Attempt036's failed
sorting inequality is not reused; Attempt037's repeated cap-source
approval loop is not reopened. Unfinished work is preserved.

The changed target is SPECIALIZE, with the exact COVERED_TARGET above
ready for the supervisor's separate next-turn approval. The completed
step is literature comparison only: no lemma, mathematical script or
new mathematical result was written. A canonical application should be
classified REPRODUCTION, not a creative mechanism. No justified bounded
new central mechanism is available from the saved coverage; missing
such a test is the blocker to a creative nomination, not a global stop.
