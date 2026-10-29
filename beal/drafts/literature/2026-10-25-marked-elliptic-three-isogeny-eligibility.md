# Marked elliptic quotient — rational-three-isogeny eligibility

TARGET: Determine whether L112's elliptic model admits a Q-rational 3-isogeny by a complete exact rational-root test of its 3-division polynomial.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed three-descent review's general and exact-coefficient searches, L112/L127, L128/L129 and ATTEMPTS/050–054; the scoped local terminology search found no existing exact three-isogeny eligibility certificate for this model.
SOURCE_EVIDENCE: Inspected Cremona, corrected second edition, III.3.8 p.99, including rational subgroup versus rational points, short-model three-division polynomial and isogenous coefficients; Schaefer–Stoll June 13, 2001 long version Section 9 pp.21–23 gives the smaller kernel-algebra branch and dual-direction qualifications.
COMPARISON: Criterion and formulas are known; only substitution, complete rational-root arithmetic and independent verification on L112 remain. Eligibility supplies no Selmer or rank bound; a rational kernel need not have rational nonzero points.
GAP: Determine all rational roots of the specialized polynomial within the stated bounds and certify yes/no eligibility; no root, absence, factorization or feasibility count is asserted in this literature-only step.
REASON: The finite structural test is independent of parked global arithmetic and stopped quartic enumeration, and discriminates whether the smaller-field branch is available. Ready coverage is proposed for separate next-turn approval.
SCOPE: Exactly TARGET on L112's actual Q-model; complete rational-root arithmetic and conditional isogenous-model check only. No class/unit computation, full Selmer algorithm, rank bound, Galois-surjectivity claim or new descent theory.

## Sources and applicability

J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second edition,
CUP 1997, corrected online edition,
[Chapter III Section 3.8](https://johncremona.github.io/book/fulltext/chapter3.pdf),
printed p.99: on y²=x³+ax+b, the rational-three-isogeny criterion is
the rational-root test of 3x⁴+6ax²+12bx−a². For a rational root xi the
isogenous short model has coefficients

    A=−3(3a+10xi²), B=−(70xi³+42a xi+27b).

These are cited formulas, not a new derivation. L112 supplies the
nonsingular integral short model with a=−2874960, b=1739350800.
No minimality or rational nonzero kernel point is needed. Preserve
the actual twist and model; do not rely on j-invariant matching.

E.F. Schaefer and M. Stoll, *How to do a p-descent on an elliptic
curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X), inspected
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 9, pp.21–23. Its rational-isogeny hypothesis makes eligibility
relevant; class/unit and dual-direction requirements are not discharged
by this test. Full comparison, queries and source-version distinctions:
`drafts/literature/2026-10-25-marked-elliptic-three-descent.md`.

## Bounded certificate plan for a later research turn

Use the standard rational root theorem without reproving it: for the
displayed integral polynomial, a reduced root m/n has m dividing the
nonzero constant −a² and positive n dividing 3. L112's a is nonzero.
Keep both signs, both allowed denominators and only reduced fractions;
duplicates are harmless if reported. Factor a by exact integer trial
division, verify primality of each factor and the full product, and
obtain the signed divisors of a². Substitution and this exhaustion
argument, not a black-box root list, certify completeness.

Before looping, bound required factor/divisor/candidate work. Caps
across the entire turn, including producer, verification, failures and
reruns: 10000 trial-divisibility tests and 200000 candidate inspections/
polynomial evaluations. No cap increase is approved. If planned complete
verification exceeds a cap, record unresolved bounded feasibility before
enumeration; a truncated list cannot prove no isogeny. Modular sieves
and backend probes are outside this single test. A separately organized
exhaustive replay must agree on every candidate and the complete zero
set within the same cumulative ledger.

If a root exists, verify its exact residual, the cited isogenous
coefficients and nonsingularity; report a rational kernel without
claiming its two nonzero points are rational. Full maps, quadratic
global arithmetic and Selmer computations are outside this target.
If there are no rational roots, stop the rational-three-isogeny branch;
do not infer general three-descent is impossible. Neither outcome
licenses another quartic traversal or backend probe. Save full
certificates under `scripts/pair-genus-two/`, print actual/required
bounds, failures and paths, and inspect complete load-bearing evidence.

## Relevance, remaining gaps and Mathlib

The main gap remains primitive positive integer exclusion in all
residual Beal signatures. Positive eligibility could permit a later
small-field rank-upper-bound plan; negative eligibility prevents work
on an inapplicable shortcut. L112 supplies lower rank one and L127
the downstream elliptic summand. L128/L129 and ATTEMPTS/050–054
constrain other mechanisms, not this test. No cross-notebook input.

Even positive eligibility leaves global data, local images, both descent
directions and sharp upper rank unresolved. Genus-two rank, marked
lifts, degree-nine recovery, both L095 systems, minus-eleven and other
signatures remain independent gaps. Mathlib coverage of the criterion
and instance was not checked; no absence or formal verification claim.
This newly written ready continuation awaits separate supervisor approval.
