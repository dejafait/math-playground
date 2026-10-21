# Two six-coordinate lifts — completed bounded proof attempt

Approved target: Determine whether L043's recovery equations and triple gates allow at most eleven distinct nonuniversal candidate parameters for every tau=1 local pencil.

Reuse the unchanged EXPLORE assessment `drafts/literature/2026-10-08-nine-union-simultaneous-recovery-count.md`. Main gap: arbitrary sixteen-error equality. Intermediate test: couple the original six-coordinate lift B with the second lift supplied by two d-tag candidates, using L048–L049. A conditional exclusion of the all-overlap twelve profile or a forced additional recovery would narrow the uniform eleven problem. Continue for an all-label restriction; abandon isolated tag-degree sums and further fixed-label positive sampling.

Inputs inspected: L010's kernel/distance/locator identities; audited L041 local converse and L042–L043; audited L048–L049. L045 and L047 were read for duplication and scope comparison, not assumed wholesale. L044's two-equation solve is a duplicate, not a new result. ATTEMPTS/022 records why isolated degree sums fail. No changed source hypothesis or essential missing literature was found; use the ready assessment and L043's already specialized primary recurrence citation. No cross-notebook input.

Working argument, not yet a claimed result: assume at least twelve nonuniversal parameters, hence at least fifteen bad parameters; L010 excludes all lower-weight errors. Two d witnesses are {d,s}+P and {d,s}+P', with P,P',W minus {s} disjoint by L048–L049. Their union B' has six labels and intersects B only at d. Interpolate their actual errors in the original affine parameter to obtain the second lift. Away from those two parameters, its four singleton coefficients are nonzero, so any further four-support meeting B' twice must be exactly V=P union P'. The original lift gives the parallel restriction with exceptional K_*. Outside B union B' there are five labels T, with total locator capacity twenty. A_2 uses two of them. Unless V actually occurs at an eligible finite parameter, twelve nonuniversal candidates force at least twenty-two incidences in T. If V occurs, equality in this budget forces all nine other candidates to meet B and B' once and T twice. Verify all exclusions and finite-parameter distinctions before promoting this argument.

Unresolved: existence and compatibility of the forced V candidate, pencils with fewer than two d-tags, original universal lift, all other patterns, extraction and ABF26. No numerical certificate is needed for this capacity argument; no new mathematical script has been written.

## Completed result and decision

The working argument was completed as [L050](../lemmas/L050-two-six-lift-forced-disjoint-recovery.md).
It proves an all-label restriction, uniform over extension-field weights
and the original chart: twelve candidates with two d-tags force exactly
one additional finite candidate on V. The remaining nine use exactly
two labels of T_0, saturating the bound twenty with A_2. In particular
the all-overlap twelve profile is impossible in this branch. No script,
new enumeration or external browsing was needed. The full proof and
source qualifications are canonical in L050, not in this checkpoint.

Outcome: ADVANCE, a conditional input beyond the existing local results,
not a complete eleven bound or certified originality. The first-lift
argument is explicitly acknowledged as L045's argument and checked only
in the scope needed. L047 previously assumed the disjoint candidate;
L050 now forces it at twelve. The h equations' solve fixes p,q but is
already in L044; it is not promoted as new. The new mechanism uses the
second affine lift provided by the actual two-d recoveries.

Meaningful proof checks covered the lower-weight reduction before either
lift, nonzero singleton coefficients away from their two interpolation
parameters, both size-at-most-eight kernel arguments, the possible
constant d coefficient in the V uniqueness test, and exact parameter
eligibility via L043's full converse. These checks are part of writing
the proof, not a separate critical audit. The capacity equality gives
2+2*(12-2-1)=20 versus capacity twenty; without V the required incidence
count is twenty-two and fails. DAG edges record only actual inputs.

The unchanged gate approved this attempt; the separately proposed audit
has REVIEW_REQUIRED coverage in
`drafts/literature/2026-10-10-two-six-lift-critical-audit-scope.md`.
Preserve the fixed-Y/Z exploration and all old stops. The forced V
branch, fewer-than-two-d cases, extraction, other patterns and ABF26
remain unresolved. No global safety or complete candidate is claimed.
