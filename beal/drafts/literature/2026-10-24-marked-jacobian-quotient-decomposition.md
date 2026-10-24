# Marked Jacobian quotient decomposition — review required

TARGET: Determine whether the existing L110 and L111 quotient maps give a Q-isogeny decomposition of L113's Jacobian, and certify the exact rank relation if they do.
CHECKED: 2026-10-24
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Narrow local checks of L111/L112, the L113 model assessments and ATTEMPTS/050–052 found the existing quotient constructions and rank/backend stops; external theorem-level comparison for the Jacobian decomposition has not been performed.
SOURCE_EVIDENCE: L111 cites Bruin Section 2.2/Proposition 2.2 and Docking Section 2/Table 1 Case II for split covers; these are reusable source leads, but their exact isogeny, twist and rank scope has not been assessed for this target.
COMPARISON: Existing curve maps and the elliptic positive-rank input do not by themselves document the requested Jacobian isogeny and exact rank relation; a matching theorem may supply most or all of it.
GAP: Inspect the primary decomposition theorem and its relevant proof cases, compare the actual marked twist and both existing quotient maps, and determine whether a citation suffices or an exact specialization is needed.
REASON: This is a new intermediate target beyond the ready L126 torsion audit; its essential theorem coverage must be approved in a separate literature-only turn before mathematical work.

## Proposed scope and discriminating test

The main gap remains primitive positive integer nonexistence. A verified
Jacobian decomposition could reduce the missing genus-three rank problem
to the smaller quotient Jacobians, making a later descent or point method
more concrete. This is a proposed structural step, not a claimed rank
bound or a claim that the smaller rank problems are already tractable.

Essential inputs are the actual smooth models and maps in L110, L111
and L113. L112 records positive rank of the elliptic quotient; audited
L126 records the marked Jacobian's rational two-torsion and must not be
mistaken for a rank computation. Retain all constants and the marked
quadratic twist. Check for a duplicate exact statement in the relevant
split-cover source assessment before proposing a new lemma. Reuse its
inspected source material where adequate, and retrieve primary theorem
hypotheses and essential proof cases before larger passages.

The proposed acceptance test is an explicit Q-defined isogeny through
the two existing quotient Jacobians, with finite kernel justified by a
precisely applicable theorem or approved pullback/norm comparison, and
an exact rank relation. Reject or narrow the mechanism if the stated
quotients have the wrong twists, the comparison fails to have finite
kernel, or the result only repeats already recorded conclusions without
providing a usable rank interface. Do not infer rank from dimensions.
No isogeny identity or rank relation is proved in this assessment.

ATTEMPTS/050 concerns an exhausted bounded genus-two detector;
ATTEMPTS/051 excludes rank zero for the elliptic quotient;
ATTEMPTS/052 records a persistent class-backend blocker. This target
repeats none of those searches or probes. Upper ranks, supported units
and S-class two-torsion, full descent/Kummer comparison, rational points,
degree-nine recovery, remaining factors, both L095 integer systems and
the minus-eleven alternative remain unresolved. If existing theorems
already imply the structural statement, import them with the necessary
applicability justification instead of reproving them.

Mathlib coverage of the exact decomposition is not checked. No absence
or novelty is claimed. The next invocation is literature-only, and this
new target has not been approved by the completed torsion audit.
