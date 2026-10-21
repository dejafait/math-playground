# Redistributed-H t=0 real-feasibility source assessment

TARGET: Determine whether the redistributed-H t=0 affine cyclic root satisfies every constraint of L051 (1)–(4).
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the recorded prescribed-parity, rational-cycle, even-allocation and exact-count discovery searches in 2026-10-11-twenty-five-fixed-count-tail-budget.md and the 2026-10-13-single-tail-survivor-remaining-real-guards.md comparison; searched the specific redistributed-H assessments and histories 310–317 for a feasibility verdict, and read Attempts 026–031. No duplicate verdict was found in that scope; no novelty is asserted.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemmas 1/2 and printed essential proof cases, pp. 228–229; rechecked NIST DLMF 4.6.4 and 4.5.1, 4.5.8–4.5.11, version 1.2.8 (2026-09-15); rechecked the MathPrize statement. Read complete L051 (1)–(4), L055 table/root/remainder passages, L065 guard/remainder method, L079 changed-table statement/analytic conventions and L078/L080 coordinate passages.
COMPARISON: The sources cover formal affine fixed points and rigorous analytic enclosures, while L055/L065 witness other parameter choices; none of the inspected results decides every changed-table t=0 guard. L079 supplies table tests and positive Lambda, and L080 supplies nonintegrality, neither survivor feasibility nor real infeasibility.
GAP: Fresh bounds must establish the changed root's domain, designated minimum, every own-input J/H guard, seed and aggregate/scaling conditions, or certify one violated necessary constraint. Unchanged totals do not transfer prefix or guard bounds.
REASON: Approve one separate RESEARCH/REPRODUCTION calculation using the inspected affine and analytic machinery; no general coding reproof, new source theorem, stronger integer-cycle threshold or wider allocation search is needed.
SCOPE: Exactly L051 (1)–(4) at r=25, B=9250245, literal L055 indexed pairs except H_0=39 and H_24=32670622, t=0 with a_i=2 for i<24 and a_24=166504412; test the unique formal cyclic root normalized at indexed row 0.
LITERATURE_REASON: The newly proposed full-real-system target changes H and requires bounds outside the previous actual-word audit and original witness scopes; compare essential affine/analytic coverage once before calculation.

## Gap and useful bounded target

The main gap remains universal eventual descent. This intermediate test
would determine whether the already excluded integer allocation is a
survivor of the complete existing real relaxation. A pass would explain
why arithmetic is needed for this root; a failed necessary constraint
would identify an earlier obstruction. Neither outcome gives universal
entry, unrestricted cycle exclusion, divergence control or descent.

Essential inputs are L051's complete real-system requirements, L055's
explicit indexed pairs and witness method, L079's exact changed table and
positive Lambda, and L078/L080's formal unshifted root normalization.
C080b is the audited actual-word exclusion for comparison, not a premise
of real infeasibility. No H/seed, minimum, integer realization or guard
verdict is assumed. Both original witnesses and Attempts 026–031 persist.

## Primary coverage and specialization

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemmas 1/2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf)
was reopened. Read the pseudo-cycle definition, odd-denominator parity
argument, numerator recursion and concatenation identity, Lemma 2's
statement and its length-one and last-zero induction cases; the printed
last-one case is stated analogous. It gives the affine composition and
unique rational fixed point of a nonempty binary word. Here the existing
formal word has length N and K odd letters, with the positive denominator
certified in L079. L078/L080 match the normalized unshifted input to this
formula; the later calculation must match its factored representation at
the same cut and include the closing tail. Import the affine identity,
without redoing the coding theorem or asserting positive-integer
realization. It does not impose the additional L051 guards.

[NIST DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), version 1.2.8,
released 2026-09-15, gives the odd-power logarithm expansion for
Re(z)>=0, z!=0; all required positive-real arguments are included.
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1) gives
x/(1+x)<log(1+x)<x for x>-1, x!=0. The inspected
[4.5.8–4.5.11](https://dlmf.nist.gov/4.5) exponential bounds include
the positive small-argument regime used for root enclosures. Existing
L055/L065 finite remainder and rounding proofs, and L079's unrounded
rational variant, supply certification methods beyond the infinite
series statement. Reuse those methods with fresh changed-table operands;
retain all rounding/remainder errors and their amplification by large
exponents. No new analytic theorem or remainder derivation is proposed.

Reuse the fixed-count-tail assessment's comparison with Simons–de Weger,
Acta Arithmetica 117 (2005), sections 1.2, 2.1–2.2 and Lemmas 4/6/7,
pp. 52, 56–59. Its full local-minimum partition and integer-orbit bounds
cannot be imposed on these arbitrary real designated junctions by setting
m=25. No stronger cycle theorem is imported. The required K_0 guard is
an explicit real-system requirement to check, not a claim that the root
realizes a primitive integer orbit. Background computational/Rhin/Crandall
qualifications remain as previously recorded. Full matching Mathlib
coverage and external Lean builds remain unchecked, not known absent.

The [MathPrize page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07, was rechecked: its target is eventual arrival at 1 for
every positive integer under n/2 when even and 3n+1 when odd. This agrees
with GOAL.md and the recorded shortcut convention. Prize adjudication
remains separate from mathematical correctness.

## Comparison, failures and approved test

The existing discovery queries and inspected theorem comparisons are
adequate for this finite specialization; no repeat general web search is
needed. Prior snippet-only leads remain unread and unused. There is no
essential source blocker. A failed search does not establish originality.
L055's original full witness and L065's changed-tail witness establish
neither the present changed-H margins nor its minimum location. L079's
O/S/C tests classify necessary candidates without asserting existence;
L080's denominator obstruction is compatible with either real verdict.
The specific redistributed-H assessments and histories 310–317 supply
no completed full-system t=0 test.

Attempt 026 stops exclusion of the original real system, not testing this
different pair table. Attempts 027–030 stop particular modular diagnostics;
Attempt 031 rejects a different permuted candidate by an own-input guard.
No such permutation, diagnostic or unchanged-table exclusion is reopened.

SPECIALIZE approves only the exact TARGET for a later
RESEARCH/REPRODUCTION calculation. Check all integer parameter lower
bounds, tail congruences and defining sums K,L,N; give explicit positive
d,K_0,L_0 with the required scaling and threshold; check Lambda and the
strict length inequality. At the exact root, certify every endpoint,
including closure; all s_i>=540/11; s_0=min_i s_i; both seed inequalities;
every non-strict J guard and every strict H guard. A rigorously violated
necessary constraint suffices to stop without certifying the others.
Equality fails strict requirements; equality passes a non-strict guard
only if established exactly. An interval touching a boundary is unresolved.

Use complete exact operands and outward bounds in a disk certificate,
with actual/required thresholds and explicit failures. Do not substitute
floating-point previews for proof. Stop at this one allocation, with a
full certificate, one rigorously failed necessary constraint, or the
precise undecided comparison. Do not expand to t=1, other tables, orders
or stronger constraints. The unchanged Next action and matching assessment
remain ready for mathematics, subject to the supervisor's separate
approval routing for this newly completed assessment.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: essential
source-scope comparison is complete, but no feasibility verdict or new
mathematical result was obtained. No lemma or mathematical script was
modified or executed. Mathematical exploration usage remains zero.
