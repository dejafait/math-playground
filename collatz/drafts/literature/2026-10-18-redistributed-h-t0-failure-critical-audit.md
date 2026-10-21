# Changed-H t=0 failed-H-guard audit — source scope approved

TARGET: Critically audit L081's changed-H t=0 H-guard exclusion against L051 (1)–(4).
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready 2026-10-18-redistributed-h-t0-real-feasibility.md discovery assessment and the 2026-10-13 remaining-real-guards comparison; searched the specific redistributed-H assessments/history 318–319 and read Attempts 026/031. The calculation exists as L081; no completed independent audit was found in this scope, and no novelty is asserted.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemmas 1/2 and essential proof cases, pp. 228–229; inspected NIST DLMF 4.6.4, 4.5.1, 4.5.8 and 4.2.19, version 1.2.8 (2026-09-15). Compared L051 (1)–(4), L055 table/root/remainder method, L079 changed-table/analytic conventions and L081's proof obligations.
COMPARISON: The known finite-word affine identity and existing certified analytic methods cover exactly this audit's machinery. They do not certify L081's changed operands, normalized root cap or negative own-input margin; the next research turn must check those independently. Integer-cycle and arithmetic exclusions are unnecessary premises.
GAP: Independently verify the exact t=0 endpoints and unique positive root, normalized all-input upper cap, changed C18 exponents, amplified analytic errors and row18 strict H-guard sign against L051 (1)–(4).
REASON: Approve one separate RESEARCH/REPRODUCTION critical audit of the existing finite specialization; no general coding reproof, new analytic lemma, wider parameter search or stronger cycle theorem is needed.
SCOPE: Exactly TARGET for L055's literal table with only H_0=39 and H_24=32670622, a_i=2 for i<24 and a_24=166504412; no t=1 test or new table.
LITERATURE_REASON: The new continuation requests an independent audit of a normalized upper bound and failed necessary guard; compare its exact source scope once, reusing the ready feasibility coverage without repeating general discovery.

Essential inputs: L051's complete real system; L055's complete original
indexed table and assessed affine/analytic method; L079's changed table;
L081's complete proof and certificate. L078/L080/C080b are comparison
context, not premises for real infeasibility. No cross-notebook input.

Unresolved assumptions: no correctness defect is known, but independent
critical audit remains outstanding. In particular check the exact t=0
closing tail, C_i>=1 only for input indices 0,...,24, positivity before
logs, the strict upper bound on s_i/C_i, all changed prefix exponents,
large-coefficient analytic errors and the own-input pairing at row18.
The other guards need not be classified once a necessary guard fails.
Preserve both original witnesses and Attempts 026–031; do not test t=1
or another table as part of this audit.

Continuation test: after separate source approval, accept the local
exclusion only if every load-bearing step survives independent checking;
otherwise record and repair the precise defect without expanding scope.
The initial proposal intentionally approved no mathematical work; the
separate source comparison below now approves this exact audit only.

## Separate source comparison — 2026-10-18

The main gap remains universal eventual descent. The intermediate target
is independent validation of L081's single-root obstruction. Its plausible
downstream use is to distinguish this real-system rejection from the
independent arithmetic exclusion, without importing either as a premise
of the other. No source supplies a universal termination mechanism.

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives the affine composition and rational fixed point for a finite
nonempty binary word. Read the pseudo-cycle and odd-denominator argument,
numerator recursion, concatenation identity, length-one and last-zero
proof cases; the printed last-one case is stated analogous. Here the
formal word has the stated positive integer length N and K odd letters;
the audit must verify the positive nonzero fixed-point denominator and
the exact shifted-coordinate match including the closing tail. Import
the identity; checking its local coordinate specialization is necessary,
whereas reproving the general coding theorem is not. This source does
not impose L051's logarithmic guards on arbitrary real junctions.

[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), version 1.2.8,
released 2026-09-15, applies for Re(z)>=0, z!=0, including positive
arguments 2 and 3. The existing L079 unrounded 100-term rational method
and L081's stated remainder use this series; source coverage does not
replace independent verification of all finite sums and amplified errors.
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1) has hypotheses x>-1,
x!=0; [4.5.8](https://dlmf.nist.gov/4.5.E8) has real x!=0.
The audit uses positive Lambda and must check positivity before the
strict exponential comparison. [DLMF 4.2.19](https://dlmf.nist.gov/4.2.E19)
supplies the exponential series for the existing exp(24) finite-sum test;
the exact partial sum is still a local certificate obligation. These
cover the required analytic steps without a new remainder derivation.
Direct TeX endpoints returned unsupported-content errors; the complete
equations and hypotheses were accessible in the HTML, so no essential
source remains blocked. Mathlib full matching coverage remains unchecked,
not known absent; no Lean verification is claimed.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07 and checked today, still asks for arrival at 1 for every
positive integer under the ordinary even/odd map. This is the local
target; prize adjudication is separate. The shortcut convention is
compatible with that target, not a restriction to the present language.

## Audit boundary and discriminating test

L051 (1)–(4) explicitly requires every own-input H margin to be positive.
L055 supplies the indexed table and method, not changed-table margins.
L079 specifies the two changed H entries; equal total H does not preserve
proper prefixes. L081 asserts a negative row18 margin at the unique
endpoint root. This comparison identifies the precise obligation to
audit; this literature turn neither recomputes that margin nor validates
the certificate or any new mathematical conclusion.

In the next research turn check all endpoints and uniqueness before using
the failed guard; retain a_24=166504412 in C_25. Check positivity of eta,
R, the denominator and all logarithm arguments. Check the claimed prefix
growth and C_i>=1 only for input indices 0,...,24, the bound on s_i/C_i,
the exp(24) comparison, C18's changed prefix and the own row18 J/H values.
Independently inspect the full load-bearing certificate fields and verify
the signs and large coefficients in the outward logarithm substitutions.
All 150 reported checks passing is a claim to audit, not current evidence
of correctness. A rerun alone would not be independent mathematical review.

Accept the exclusion only if the complete relevant proof and certificate
establish a strictly negative upper H margin; an interval touching zero
is unresolved. On a defect, record and repair that precise issue within
scope rather than extending to another allocation. No verdict on other
guards is required after one necessary failure. No assumed minimum,
seed, integrality, parity, primitive realization or integer-cycle bound
is permitted to supply an unproved premise of this real obstruction.

Attempt 026 rules out excluding the original real witness from the
unchanged subsystem; this different table is outside that stop.
Attempt 031 concerns another order and its own-input J failure, not
this literal root. Other recorded prime/order failures remain untouched.
The ready feasibility assessment already checked Attempts 027–030;
no new modular mechanism is proposed, so that comparison is reused.
No cross-notebook result, unread source lead or stronger source threshold
is required. Both original witnesses and every universal gap persist.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: the separate
scope comparison is complete and the unchanged target is ready for a
RESEARCH/REPRODUCTION audit. No new result, independent audit verdict,
lemma edit or mathematical script execution occurred. Mathematical
exploration usage remains zero; resume mathematics next.
