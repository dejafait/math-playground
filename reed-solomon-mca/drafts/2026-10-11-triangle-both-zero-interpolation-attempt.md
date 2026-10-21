# Triangle both-zero interpolation — completed bounded proof attempt

Ready target: the unchanged twelve-additional-recovery question in
`drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md`.
Main gap: exclude thirteen additional recoveries uniformly over labels.
Intermediate target: classify both-zero projected support quartics using
the six singleton evaluations. Downstream use: restrict seven-scalar
fibers without assuming a sampled maximum or an audited L064.
Continue on a uniform support restriction or exact exceptional family;
abandon if interpolation only rewrites the projected equations.

Unfinished reasoning saved before the full proof: write Y,Z,W for the
three monic singleton-pair quadratics and S=YZW. For singleton x,
c_x*x*G_P(x)=16/S'(x), since H is the zero set of X^16-1.
Both-zero therefore forces each pair sum of f_K(x)/S'(x) to vanish.
Lagrange interpolation suggests exactly f_K in span{ZW,YW,YZ}, so
singletons occur in complete pairs. Independent Y,Z,W give an injective
projective evaluation map outside the six roots; dependent quadratics
give a degree-two fiber partition. Need prove both cases completely,
reject two original singleton pairs using restored equations, and bound
simultaneous pair-containing rows without relying on unaudited L064.

Inputs read: audited L041's shortening/kernel specialization; L057's
full statement and relevant recurrence, quotient and original-chart
proof; L059's exact table statement. L064 is comparison only: its
common-pair proof and constant-coordinate observations motivated a
check but its theorem is not assumed. ATTEMPTS/025 stops sampling and
formal common-root repetition, not this interpolation mechanism.
No new source review is needed: unchanged EXPLORE coverage includes
the full triangle and all both-zero lifts. No known bound or novelty
claim is inferred from that assessment.

Completed result: [L065](../lemmas/L065-triangle-both-zero-support-classification.md)
contains the full classification and proof. Independent pair quadratics
give at most five simultaneous both-zero additional parameters;
dependent pair quadratics give at most six, with an exact finite
two-element-fiber description. The proof covers all labels and extension
weights and rechecks the common-pair kernel argument rather than assuming
unaudited L064. Thus the continuation test succeeds: interpolation gives
a uniform restriction and an explicit exceptional family, not merely a
restatement of projected vanishing. Seven-scalar D fibers must have an
isolated row. No bound on those rows or their coupled fibers is supplied.

Supplementary exact check:
`python3 scripts/triangle-recovery/check_both_zero_interpolation.py`.
The complete selected certificate is
`scripts/triangle-recovery/both-zero-interpolation-check.json`.
It tests all 715 disjoint-P supports for each of two assignments, one
with quadratic rank three and one with rank two. All 1,430 direct
projected/net-membership comparisons pass. The independent assignment
has one candidate for each singleton pair and zero entirely-V candidates;
the dependent assignment has two for each singleton pair and one
entirely-V candidate, exactly the two-fiber classification. Each also
has three two-original-pair supports, which the written lift argument
rejects. This regression supplies no computational uniform bound and
does not evaluate actual recovery counts or original charts.

Outcome: ADVANCE as a local mathematical restriction, POTENTIALLY_NEW
only in the assessment's limited sense; no certified originality or
progress beyond unread sources is claimed. L065 still requires its own
critical audit. L060–L064's audit obligations, the full uniform twelve
bound, other patterns, extraction and challenge-definition gaps remain.
Next route: separately approve and audit L065 before using its count as
an established new input in further coupled-row arguments.

Scoped documentation validation passes: 67 nodes, 135 unique edges,
acyclic DAG, complete canonical-file coverage, valid local links and
compact overviews. L065's direct inputs were checked mathematically as
L010/L041/L057; neither L064 nor the sampled table counts are premises.
