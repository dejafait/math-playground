# Rounded arithmetic source comparison1809

19 November2026. LITERATURE / literature_comparison;
EXPLORATION / NOVELTY_UNCHECKED. No mathematical derivation, lemma,
mathematical script, new numerical experiment or scalar enclosure.

LITERATURE_REASON:1806 explicitly excludes changed arithmetic. The saved
1808 nomination requires new primary coverage for rounded intermediates
and their cost under the unchanged rational-operation contract.

## Gap, target and bounded test

The main gap is L030-L032/C032a actual-Xi all-degree positivity;
C028b signed height, cancellation and realization remain unpaid.
The reviewed intermediate target is the exact TARGET in review1808:
whether rounding C033z's intermediates can retain both2^-10 allowances
and the10^6 cap for the eight C033w scalars, at radius<2^-8.
Those scalars could make fixed-three-width interpolation concrete;
conditioning, exact weights, TV and the full observation interval remain
independent gaps. The source test is whether a matching theorem pays
both rounding propagation and the original operation model. General
enclosure semantics alone cannot pass that test.

## Local comparison and duplication check

Used the supplied overview/DAG before detailed reads. Read C033z's
hypotheses, original core through(10), input construction and remaining
arithmetic(18)-(32)/ledger, plus the relevant C033y bounds/audit;
C033w's law/minimax definitions and C033u's specified-rule stop.
Reused1806/1807 execution coverage,1799/1804 source coverage,1805 repair,
and1808 execution notes/history. The direct-positive-real assessment/
history search found the explicit exclusion of alternative arithmetic,
not an earlier rounded-evaluator contract. This is a scoped duplicate
check, not a claim that no similar algorithm exists elsewhere.

C033z counts rational +,-,*,/, comparisons and clamping, including
operations by small integers. Assignments/indexing/storage are excluded;
floor, arbitrary-precision bit operations and fused multiply-add are not
granted free. Its989767 ledger leaves10233 operations, as already recorded.
The stable moment rearrangement is justified for exact rational inputs;
its current proof has no intermediate-rounding term. Likewise(19)-(21)
evaluate and sum224 Ihat samples exactly, and(23),(28),(31),(32) propagate
that existing error. Changing the accumulation requires a new charge
through these formulas; the quoted bounds cannot simply be reused unchanged.

Execution1808 completed inputs/moments and21 Ihat weighted terms, with
a4063129-bit partial denominator, before its operational time limit.
These are reused saved-execution observations, not newly verified bounds.
No scalar or completed execution count was obtained. Preserve all exact
values, including the unused22nd sample, and the recorded431-check replay.
No certificate replay was needed for this source-scope comparison.

Preserve C033x and1781/1782 stops, which concern different specified
rules/representations. They neither establish a rounding obstruction nor
ban a changed mechanism. No existing failure was removed or reopened as
a universal claim. Unfinished C033v/audit1791 remain untouched.

## Bounded external search and inspected primary cases

Queries used: `Johansson Arb efficient arbitrary precision midpoint radius
interval arithmetic 2017 rounding error rational operations`;
`"rational arithmetic" "rounding" "operation count" interval arithmetic`;
`"Numerical integration in arbitrary-precision ball arithmetic" error
propagation precision`; `site.fredrikj.net "Arb: efficient" pdf`;
`site.arxiv.org "Arb: efficient arbitrary-precision midpoint-radius interval
arithmetic"`; `site.mpfr.org rounding exact result correctly rounded
operations precision`. Read primary statements/cases below rather than
using search snippets as evidence. Search failure is not evidence of novelty.

1. Fredrik Johansson, *Arb: Efficient Arbitrary-Precision Midpoint-Radius
   Interval Arithmetic*, [arXiv1611.02831v1,9 November2016](https://arxiv.org/pdf/1611.02831v1).
   Inspected Sections3.1.1-3.2 pp5-6, Section4 pp6-7 and
   Sections5-5.1 pp7-8. The paper gives rounded-addition radii,
   product-radius propagation, and derivative bounds requiring a valid
   derivative supremum on the full input interval. Its implementations
   use mantissa limbs and directed magnitude arithmetic; benchmarks are
   timings. Compiler and correctly-rounded-operation assumptions in
   Section3.2 concern software correctness. These are general tools,
   not the local evaluator's rational-operation or precision certificate.
   No reproof is needed. No asymptotic convergence statement there is
   used as a fixed-precision bound.

2. [Arb2.23.0 arb.h](https://arblib.org/arb.html), introduction,
   `arb_set_round`, `arb_div` and dot-product section. Inspected enclosure
   semantics and the full quotient-error identity/triangle-inequality
   explanation. For midpoint denominator y and radius b it requires
   |y|>b; a denominator ball containing zero yields an infinite enclosure.
   It bounds numerator/denominator perturbation, separately from midpoint
   rounding. The precise dot routine rounds only at the end and may be
   slow; the default uses mpn arithmetic. Neither routine supplies the
   notebook operation count. Frozen2.23.0 documentation is used as a
   specified contract, not a claim about an installed/current library.

3. [Arb2.23.0 arf.h](https://arblib.org/arf.html), opening semantics and
   assignment/rounding/conversion functions. Inspected exact-input
   correctly-rounded semantics, precision and direction, unbounded
   exponent representation, integer/fixed-exponent conversion and their
   exceptional-value/memory qualifications. These are separate operations
   on an integer/limb representation, not rational field primitives.
   No software version or execution environment was installed/validated.

4. [GNU MPFR4.2.2 manual](https://www.mpfr.org/mpfr-4.2.2/mpfr.html),
   Sections4.4 Rounding,4.6 Exceptions and5.2 Assignment Functions,
   including `mpfr_set_q`. Inputs are exact for each individual rounding;
   directed modes and round-to-nearest have local ulp guarantees subject
   to the documented exponent/special-value cases. Rational conversion
   can fail if numerator/denominator cannot be represented. These are
   stronger individual conversion guarantees than an unspecified
   precision request, but do not track earlier input errors or count
   their implementation as one rational operation. No MPFR dependency
   is imported into the evaluator.

Johansson1802.07942v1 quadrature coverage is reused from1799/1804/1805;
no fresh integration theorem or changed analytic error is claimed.
The dot-product paper1901.04289 and midpoint-analysis DOI10.1145/2493882
appeared as leads; neither was inspected or used. They are not essential
to a rational-comparison specialization of the already fixed finite sum.
Third-party summaries and current FLINT documentation were not used as
theorem evidence. No essential source remains inaccessible for this scope.

## Decision and specialization boundary

SPECIALIZE for ingredients: import known enclosure principles with their
hypotheses. No matching inspected theorem supplies both the original cap
and the eight radii. The remaining difference is an instance-specific
cost/error contract, not an unproved general interval-arithmetic theorem.
In particular, treating an Arb/MPFR call as one rational operation is
unsupported. This comparison does not prove that the cap is impossible.
Replacing every exact operation by a ball operation is not costed here.

Nominate only rounding selected Ihat(1) accumulation checkpoints while
retaining exact samples and the other C033z constructors. A later bounded
calculation must specify each rounding using rational arithmetic and
comparisons, count it, bound all new errors and propagate them through
the existing K/profile/exponent/final-scalar formulas. No precision,
checkpoint spacing, rounding algorithm, successful bound or execution
has been chosen or derived today. This is an ordinary specialization;
a proof of general enclosure principles would duplicate known results.

Continue only with a fully specified Ihat contract preserving both
arithmetic allowances and the full cap, including any error-tracking
work. Otherwise save the first failed budget/uncertified amplification
and abandon that schedule, without declaring every rounding schedule
or the exact route impossible. Success would address this accumulation
bottleneck only: denominator growth elsewhere, practical runtime and
completed eight-scalar execution would still need separate work.

## Qualifications and handoff

Essential inputs: C033y/z/u/w, C032s/q/w and C032j conventions;
execution1808 saved data/index and replay. Retain actual divisor,
conjugation/multiplicity, excluded ordinate0, strict strip/gamma>14,
counting, real zeros through100 and one in(14,15), reciprocal-square tail,
heat positivity/separate fixed-j errors, both fixed-v1 qualifications,
zero drift/killing and Gaussian half-variance. Source-wide/zero-data
correctness remains unverified. Full matching Mathlib coverage is
unchecked/unknown; this review does not establish absence.

No PROOF/DAG change: no new mathematical input or argument has been
established. The new Ihat assessment1809 is a ready source-scope nomination
for separate next-turn approval, not completed mathematics. Outcome
EXPLORATION records new source comparison, not an advance beyond sources
or a new mathematical negative. Literature uses no mathematical
exploration turn and claims no reset. Central creative blocker1796
persists: this arithmetic supplies no independent signed-height input
or representation; no creative mechanism is justified by these sources.
