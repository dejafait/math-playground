# Capacitated two-distance working record — step 407

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-22-two-distance-capacitated-triangle-test.md`.
Only its exact target is being attempted. Existing unfinished changes,
L108 and all stopped solves are preserved.

Main gap: arbitrary-center 68/67-agreement safety. Intermediate target:
the approved signed edge weights supported at half-distances 5 and 6.
A strict box-dual separator rejects L098's fixed pairs; exhaustive
nonseparation parks only this diagnostic. Full shared scalar feasibility,
Boolean lower rows, PSD, other pair prescriptions and RS realization
remain independent gaps. Stop after one original-orbit enumeration,
complete presentation/multiplicity check and exact two-weight evaluation.

## Saved before computation

For distinct supports the demand is d_i=(N-2)c_i: both endpoint
repetitions have coefficient one and value c_i. At i=0 they coincide,
so that row is only the objective. For a triangle T let b_T be the
minimum of its three c coordinates. A necessary box system is
Wz=d, 0<=z_T<=b_T. Eliminate b_T=0 coordinates before applying
Boyd–Vandenberghe Example 5.9. The necessary support inequality is

    F(lambda)=sum_T b_T max(sum_(e in T) lambda_e,0)
              -sum_e lambda_e d_e >=0.

This is the maximization sign of the cited coordinatewise box formula.
A negative F would separate. No converse source lift is assumed.

Take lambda_5=x,lambda_6=y, and zero elsewhere. If a triangle has
m_5,m_6 edges of these distances, its weight sum is m_5*x+m_6*y,
where m_5,m_6>=0 and m_5+m_6<=3. Hence all possible nontrivial
break lines are x=0,y=0,x+y=0,2x+y=0,x+2y=0. On the diamond
|x|+|y|=1, each piece is affine along a closed segment. Its minimum
is at an endpoint: the four axes and the six opposite-sign points
of ratios 1,2,1/2. Overpartition by unused lines is harmless.
The zero vector has F=0. Candidate completeness and every exact
margin still require checking in the computation and canonical proof.

For a common positive denominator q write P_i=q*c_i. For each actual
original (i,j,t,s), G=g_i*D is the source integer multiplicity per
anchor, h=i+j-t-s. Distinctness is i,j,h>0. Every unordered triangle
has six ordered presentations, including repeated distance keys.
Thus grouping only arithmetic coefficients gives

    F(x,y)=H/(6q) * [sum_(m5,m6) K_(m5,m6)
                    max(m5*x+m6*y,0)
                    -3(N-2)(g_5*P_5*x+g_6*P_6*y)],

where K sums G*min(P_i,P_j,P_h) over every distinct original entry.
This grouping must not identify distinct primal variables or discard
t-s. Planned certificate retains original ranges, source and D factor
arrays, all h descriptors, capacities, both repetitions, null edges,
all six presentations and exhaustive normalized candidates.

## Bounded attempt outcome — 2026-10-23

The single invocation was

    python3 scripts/finite-support/capacitated_two_distance_test.py

It completed the one original-orbit pass (1,500,625 entries), all six
presentation checks (9,003,750 visits), all row and unordered multiplicity
assertions, all ten normalized evaluations and the complete segment-sign
checks. It then failed its last output-size assertion, line 245, after
writing the full certificate. The exception handler preserves the data
with `stage=obstruction` and `failures=["AssertionError()"]` in
`scripts/finite-support/capacitated-two-distance-results.json`.

The saved certificate is 84,481,702 bytes; the declared script limit is
67,108,864 bytes (64 MiB). This limit was an implementation choice, not
a theorem hypothesis or a supplied numerical bound. It is nevertheless
a failed declared check, so the run is not reported as a passing
certificate. No rerun, compression, cap increase, second enumeration,
second weight evaluation or mathematical continuation followed.

The saved evaluation reports minimum normalized scaled margin divided
by the positive scale

    3(N-2)(g_5*P_5+g_6*P_6)

equal to **4/6521 > 0**, against the separator requirement <0. This
selected rational, the complete visit-count array, original count,
failure array and elapsed field were inspected in full with the shared
JSON inspector. The stored `NO_TWO_DISTANCE_SEPARATOR` verdict is
only a candidate until storage/validation is repaired and the relevant
evidence is critically checked. A field or bounded preview alone is
not verification of its mathematical claim. No canonical lemma, DAG
edge or PROOF.md conclusion is added on the basis of this failed run.

This is EXPLORATION: a new bounded mathematical test was attempted,
but no certified nonseparation verdict is claimed. The informative
saved arithmetic remains unfinished work, rather than an exclusion or
an accepted stop on the capacitated diagnostic. The mathematical route
is not exhausted. Existing L105–L108 stops and ATTEMPTS/081–082,088–091
remain unchanged, as does the 955–957 bracket.

The continuation under the unchanged prior assessment is storage-only:
preserve this failed artifact; determine a lossless representation of
its already computed evidence and validate that representation without
repeating the original-orbit pass or the weight evaluation. It must
retain every original coefficient, presentation rule, multiplicity,
both repetitions, null edges, t-s and the complete ten-candidate data.
Do not silently change the failed bound or advertise the current
candidate as a proved result. If packaging cannot be certified without
new mathematical passes, stop with the precise remaining obstruction.
## Storage-only continuation — 2026-10-23

Without rerunning the mathematical script, losslessly gzip the saved
84,481,702-byte JSON to
`scripts/finite-support/capacitated-two-distance-results.json.gz`.
Decompression reproduces the original byte-for-byte; both SHA-256 values
are `c26d6d8d9ab453874f0aba97c81cd99049ba5fd8c65b122b2aad032c61b0be44`.
The packed size is 26,035,289 bytes, below the recorded 67,108,864-byte
storage cap. A full JSON parse confirms the original `obstruction` stage
and `AssertionError()` remain recorded, 1,500,625 entries, 9,003,750
presentation visits, all ten stored candidates, and the selected ratio
4/6521. This validates packaging and selected stored fields only; it does
not independently verify the orbit math or certify nonseparation. The
original failed artifact and script are unchanged. The scoped structure
checker passes (114 nodes, 416 unique edges).

The storage blocker is removed. Next is the separate critical mathematical
review of this saved candidate, retaining all original orbit entries,
source multiplicities, six presentations, repetitions, null edges,
`t-s`, the box-dual sign, compact-domain candidate coverage, and exact
margins. Do not infer a theorem or change the boundary before that review.

## Critical audit in progress — 2026-10-23, step 409

The audit reuses the unchanged SPECIALIZE target. The original constructor,
failed JSON and lossless gzip remain immutable. Check the factored arrays
and every saved h aggregate independently, using coefficients of products
of two nonnegative integer polynomials, not a second original-orbit
enumeration. A power-of-two evaluation with base greater than the sum of
all product coefficients has no carries and recovers those coefficients
exactly. Derive all six presentations and their multiplicities symbolically
from the eight atoms. Then compare the complete saved ten-candidate
evaluation and segment coverage. This is verification of the saved attempt,
not an enlarged support, new solve or another mathematical search.

Continue only if the box sign, complete aggregate reconstruction and all
normalized margins agree. Otherwise save the exact defect and return
inconclusive or reject the candidate, as warranted. No full scalar lift,
PSD conclusion, other weight support or RS boundary change is in scope.

## Completed audit — step 409

The independent factored audit passes all 386,498 checks, with zero
failures, in `scripts/finite-support/capacitated-two-distance-critical-audit.json`.
It checks every source factor and every h aggregate without repeating
the original ordered-orbit enumeration; exact polynomial coefficient
reconstruction verifies all saved counts and weighted sums. All ten
candidate margins and complete segment coverage agree. The minimum
normalized margin is exactly 4/6521>0, while a separator requires <0.
L109 now contains the full canonical proof, including the symbolic six
presentations, t-s retention, unordered factor six and box-dual sign.
The two-distance diagnostic is parked; the earlier failure and original
artifacts are unchanged. No full scalar feasibility or boundary claim
follows. History/409 records the decision; current continuation is solely
in PROGRESS.md.
