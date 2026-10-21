# Remaining cyclic shared gates — step 228

2026-10-15. RESEARCH / proof_attempt under the unchanged EXPLORE
assessment `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
Approved target: Determine whether L087's full alternating moment system
has zero kernel for every bijective H-labeling.

Saved before the extended calculation. The main gap is exclusion of
sixteen actual errors; this step addresses only the residual cyclic-family
kernel. The intermediate target is a further necessary restriction from
L089's first and second shared-coordinate gates, coupled with L090's
third gates. A useful restriction could reduce the eight-label seed
problem toward uniform rank R>=3. Essential inputs: audited L089, its
L010/L087/L088 conventions, and L090's new identities checked where used.
No actual errors, rational original chart, or cyclic symmetry of h is
assumed. Arbitrary families and challenge qualifications remain open.

The existing literature assessment is reused; no theorem import, source
refresh, cross-notebook input, positive rank sampling or labeling census
is proposed. ATTEMPTS/020,029,031 remain preserved. The prior attempt
simplified only the third gates. Continue for a uniform contradiction or
a useful proved residual restriction; if neither is obtained, save the
equations and reassess. A deficient labeling would require independent
full-kernel verification before abandoning uniform zero kernel.

For an initial first-gate calculation, put
u=h(t-2), a=h(t-1), b=h(t), x=h(t+1), c=h(t+4),
y=h(t+5), d=h(t+6), z=h(t+7), e=h(t+8), f=h(t+9).
Sliding the circuit window twice suggests the first gate is

    (c-a)(x-z)(x-e)(d-u)/((c-e)(x-u)(x-a)(d-z))
      +(x-b)(y-f)/((x-f)(y-b))=1.

This formula is unfinished until its exact derivation and possible
coupling to the translated third gates have been checked.

The second gate has a shorter prospective form. Put additionally
q=h(t+2), k=h(t+10). The formula to verify is

    (q-e)(z-a)/((q-a)(z-e))
      +(q-b)(q-x)(d-k)(e-f)/((q-f)(q-k)(d-x)(e-b))=1.

Each of its labels except q,e occurs in just one nonconstant fractional
linear factor. Thus eight labels, if they form a valid bijective partial
assignment, should determine the ninth in any of those seven positions.
The first gate similarly determines any one of its ten labels except x
from the other nine. These are prospective algebraic deductions, not
assumed sufficiency for a kernel. One exact abstract-index diagnostic may
look for a seven-seed reconstruction using these rules and L090's
five-known-label rule. It assigns no H values, tests no rank, and examines
no other support family. A successful tree must be verified analytically;
a failure will be saved and will not exclude other analytic mechanisms.

## Completed bounded pass

The full gate reductions, exact single-unknown rules and computational
qualification are canonical in
[L091](../lemmas/L091-cyclic-remaining-gates-reconstruction-limit.md).
Both displayed formulas above were verified by cancellation of the exact
circuit-window products. The part of L090 needed for its single-label
deduction was checked; neither L090 nor L091 receives a separate full
critical audit in this attempt.

The diagnostic tested only abstract index propagation, assigning no H
values and performing no rank tests. All 11,440 seven-index seed sets
have closure size at most nine, versus sixteen required for a complete
reconstruction. A separate whole-gate bit-mask implementation replayed
every complete closure, including all failed sets, with zero failures.
The complete evidence is in
`scripts/cyclic-shared-gates/seed-reconstruction-result.json` and
`scripts/cyclic-shared-gates/seed-reconstruction-audit.json`.
The selected maximal case was inspected in full using the prescribed
JSON inspector. The evidence is the complete replay, not that selected
case or a bounded preview. This negative finding changes the route:
stop trying to obtain seven-seed reconstruction by these single-label
rules. It supplies no uniform kernel obstruction or deficient labeling.
The classification POTENTIALLY_NEW does not certify originality, and
this is not reported as a new mathematical discovery beyond the sources.

A concrete alternative inside the unchanged approved target is
simultaneous elimination. The attaining seeds {0,1,2,3,5,7,9} acquire
indices 10 and 14 by D_1 and D_10. At that partial assignment, D_15
and S_8 each involve exactly two still unknown labels h(8),h(15):
D_15 uses pairs (14,15),(3,8),(5,7), and S_8 uses indices
{7,8,9,10,14,15,0,1,2}. These facts follow directly from the canonical
gate templates, with no field assignment or symmetry assumption.
Whether these two equations give a nontrivial eliminant or coincide
has not been determined. This is the proposed discriminating test;
no finite bound on solutions or new continuation assessment is asserted.
Any proposed continuation must retain poles, repeated labels, H
membership, degenerate equations, all unused gates and the full rank
test. Actual-error applicability and arbitrary families remain separate.

Outcome: NEGATIVE, limited to the single-label propagation mechanism.
Zero mathematical EXPLORATION turns were spent; zero consecutive
mathematical EXPLORATION turns carry forward. Existing unfinished work
and ATTEMPTS/020,029,031 are preserved. No source refresh, external
theorem import, cross-notebook input, H-label sweep, positive rank sample
or support-family census occurred.
