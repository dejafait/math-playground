# Actual twisted central pairing — step 478 working record

Approved target: Test uniform boundedness of the Chern curvature of L148's actual twisted harmonic L2 metric near each split parameter.
Reuse the unchanged SPECIALIZE assessment `literature/2026-10-23-twisted-harmonic-metric-curvature.md`.

Main gap: universal primitive rational Hodge realization. Intermediate
threshold: evaluate L149 (4) for the given line metric. Vanishing would
supply bounded curvature, potentially useful for a later extension test;
an actual nonzero pairing would stop this bound. F, nonempty Z, extension,
positivity and transport remain independent unresolved assumptions.

The existing local changes, L149, the relevant L146/L148 passages and
L094/L113 coefficient identities were inspected. The prior source review
and ATTEMPTS/060/063/066/067 are reused. No external theorem search is
needed for the unchanged approved calculation. No sibling notebook is used.

Work saved before continuing the comparison: at an actual split point,
let h_0 be the metric on L induced by the split compatible connection,
with a parallel determinant trivialization. This is an auxiliary reference,
not a replacement for the fixed metric on the twisting L^{-1}. The actual
metric on the negative coefficient L^{-2} is w times its connection metric,
where w is one fixed smooth positive function on S_1. The holomorphic
Dolbeault operator D is unchanged. Raw negative KS forms are harmonic for
the reference metric, but generally require an exact correction for w.
A prospective exact expression is obtained by solving
D_0^*(w D u_a)=D_0^*(w a) and using a-Du_a. The relevant coefficient has
H^0(L^{-2})=0, so this scalar-section equation has no kernel.

Remaining task in this attempt: retain that exact correction in both
arguments of the actual harmonic product and determine whether the actual
quaternionic KS relations annihilate the result. Do not discard the
correction, treat harmonic projection as multiplicative, or replace w by 1.
The central constant cannot be decided by quotient differentiation again.

Completed bounded attempt: the exact weighted harmonic expression and
its full justification are preserved in L149's step-478 subsection.
The central value was not evaluated; outcome EXPLORATION. These initial
notes remain a working record, not a separate canonical proof or current
next-action record. PROGRESS.md gives the reassessed continuation.
