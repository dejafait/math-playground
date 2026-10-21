# L147 — Complete other/other coefficients and two-probe noncompensation

## Hypotheses

Use L124's SU(2) setup: the actual L010 probes i=3,6 at flow time
1/16, the actual residual, straight lower-rooted direction-1 forest,
all-face relative fixed-link box (-4,4)^4, and a=8/N through admitted
even meshes. Take the bare small-coupling coefficient at each fixed
mesh before refinement. Put C=S3_top, Y=S3-C,
O_i=(1/2) kappa(f_(i,0),r0,Y,Y), and M_i=kappa(f_(i,0),r0,C,Y).
Import L124(1)--(3) and L084(1), including gamma>0 and its actual
continuum D_i. Retain ordered coincident pairs, both connected classes,
all residual orientations, pinned rows, axial levels and exterior modes.

Import L133(1)'s complete transverse-H interval, L137(1)'s E intervals,
L138(2)'s Q intervals, L139(3)'s axial intervals and the complete G/R
coefficient intervals in L144/L146's conclusions. By L132(2) and L124's
proof section 2, K_(i,tr)=K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en).
These inputs all use the same probes, prefix fields, box and limits;
none includes L124's outside factor 3.

For the audited shear comparison, import L070(3), proof section 4:
its full normalized torus integrand V is nonnegative and bounded by 1,
and its integral is strictly positive. L084 uses exactly this gamma.
This input gives 0<gamma<=1/3 by monotonicity of integration. No
frozen-symbol substitution into the actual trace is made: L084 already
establishes that the actual mixed limit uses the same constant.

Keep every imported numerical qualification: the specified certified
moment, node, weight and saved hexadecimal inputs, complete spectral
omission bounds, and L039's IEEE binary64 addition/multiplication/FMA
model, arbitrary summation order, no overflow and local underflow
allowance 10^-290. L084's strict D_i signs retain L082's qualifications.
This is conditional informal computer-assisted inclusion, not independent
processor or BLAS verification. Exact endpoint arithmetic below needs
no additional floating-point assumption. No numerical gamma value is assumed.

## Conclusion

The complete L124 coefficients satisfy the strict intervals

    -28804.836 < K_(3,oo) < -15576.369,
      4086.795 < K_(6,oo) <  11112.074.                    (1)

Consequently

    -86414.508 < lim a^3 O_3(a) < -46729.107,
     12260.385 < lim a^3 O_6(a) <  33336.222.              (2)

The triplet cannot compensate L084's mixed contribution:

    K_(3,oo) != -4 gamma D_3,
    lim a^3[O_3(a)+M_3(a)] < -46729.107 < 0.             (3)

Thus this two-group triplet sum has a nonzero negative cubic coefficient
and is not O(a^-2). The two corresponding shear coefficients have
opposite signs, so signs alone do not settle compensation. A necessary
condition for shear compensation is

    102169875/9887743 < gamma < 2778018500/98877429,        (4)

approximately (10.332982,28.095578); these rounded displays are not
the exact endpoints. L070's imported bound gamma<=1/3 excludes this
interval. The complete shear comparison therefore satisfies

    11864.87528 < lim a^3[O_6(a)+M_6(a)] < 33336.222.    (5)

Thus these two groups do not compensate for either actual probe; their
shear sum also is not O(a^-2). This shear conclusion was added by the
separate critical audit YM-20261012-174-complete-cubic-comparison-audit,
using a bound already established in L070 rather than new integration.

This is local REPRODUCTION through finite interval assembly, not a new
general theorem beyond the checked sources. Other response jets can
still compensate (3). Finer powers/logarithm, finite matching, interacting
error <=c_box/2, continuum axioms, reflection positivity, infrared control
and finite positive mass remain open. There is no Yang--Mills candidate.

## Proof

### 1. Add the complete signed coefficient intervals

L124(1), with the exact full transverse-H identification above, reads

    K_(i,oo)=K_(i,E)+K_(i,ax)-K_(i,Q)+K_(i,G)+K_(i,R)+K_(i,tr).

Use the following full intervals. Q is already negated in this table.

| i | E | ax | -Q | G | R | tr |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | (-5184,-4342) | (786,1770) | (-20768,-13590) | (-146.92,-103.56) | (-74.916,-52.809) | (-3417,742) |
| 6 | (471,702) | (234,528) | (-4137,-2971) | (-315.66,-222.51) | (-27.545,-19.416) | (7862,13095) |

The entries are respectively the six imported results in the hypotheses.
Each interval contains the full continuum functional, including its
omitted spectrum; retained diagnostic values are not used. Shared
inputs or correlations between coefficients do not invalidate interval
addition: each inequality holds simultaneously under the common
hypotheses, and summing inequalities requires no independence.

Exact terminating-decimal arithmetic gives the triplet endpoints

    -5184+786-20768-146.92-74.916-3417 = -28804.836,
    -4342+1770-13590-103.56-52.809+742 = -15576.369.

The shear endpoints are

    471+234-4137-315.66-27.545+7862 = 4086.795,
    702+528-2971-222.51-19.416+13095 = 11112.074.

This proves (1). L124(2) multiplies this coefficient by exactly 3,
giving (2). No connected-class, triangular-half-weight or color factor
is applied again. No new limit interchange is needed. In particular
the triplet transverse-H sign remains unresolved individually, but its
full upper bound 742 is included in the negative complete upper bound.

### 2. Compare to the required compensation value

L084 gives D_3<0, D_6<0 and gamma>0 under the retained qualifications.
Thus -4 gamma D_3>0, whereas (1) makes K_(3,oo)<0. They cannot be
equal. Moreover 4 gamma D_3<0, and L124(3) gives

    lim a^3[O_3+M_3]=3[K_(3,oo)+4 gamma D_3]
                      <3 K_(3,oo)<-46729.107.

This proves (3) without evaluating gamma. An O(a^-2) sequence would
have a^3-scaled limit zero, contradicting (3). This reasoning concerns
exactly these two groups, not the full response.

For shear, put d=-D_6. L084's bounds give
98.877429<d<98.877430. If cancellation holds, then
gamma=K_(6,oo)/(4d). Both numerator and denominator are positive.
Monotonicity of division and (1) therefore require

    4086.795/(4*98.877430) < gamma
                              < 11112.074/(4*98.877429).

Reducing these exact rational fractions gives (4). It is only a
necessary condition. Interval compatibility establishes no equality.
The triplet exclusion already rules out simultaneous compensation
for both probes by this other/other group.

The separate critical audit found that L070(3), proof section 4
already supplies a sufficient upper bound. With normalized full-torus
measure of total mass 1 and its established 0<=V<=1,

    0<gamma=(1/3) integral V<=1/3.

The lower endpoint in (4) exceeds 1/3: in exact integer arithmetic,
3*102169875>9887743. Hence the necessary shear interval cannot be met.
More quantitatively, because D_6<0 and gamma<=1/3,

    12 gamma D_6 >= 4 D_6 > -4*98.877430=-395.50972.

Combining this with (2)'s strict shear lower bound gives

    lim a^3[O_6+M_6] >12260.385-395.50972=11864.87528.

Its upper bound is <33336.222 since 12 gamma D_6<0. This proves (5).
Its nonzero limit excludes O(a^-2) exactly as in the triplet case.
Only integral monotonicity and finite inequality arithmetic have been
added; the known variance bound and all actual-trace limits are imported.

### 3. Reproduction and evidence

Run from the active notebook:

    python3 scripts/combined-ward-response/assemble_cubic_comparison.py

The script converts every decimal endpoint to an exact Fraction,
negates Q by swapping endpoints, sums all six signed intervals,
multiplies by 3 once, and computes (4) as rational divisions. The full
certificate is scripts/combined-ward-response/complete-cubic-comparison-certificate.json.
It records all source intervals, signed terms, exact output fractions
and failures. The run has zero failures; the complete selected results
and gamma interval were inspected. Printed decimal summaries are only
displays; the proof uses the exact values above. This check validates
endpoint assembly and thresholds, not the imported source certificates
or their underlying analytic reductions independently.

The separate audit command is

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_complete_cubic_comparison.py

It extracts the six full intervals directly from the canonical
Conclusion sections, checks every signed term and exact output against
the original certificate, identifies L070's bound as the same constant
in L084, and saves exact shear comparisons in
scripts/combined-ward-response/complete-cubic-comparison-audit.json.
All 49 checks pass with zero failures; all complete check records,
gamma bounds and shear endpoints were inspected. Text matching only
identifies the cited inputs; the proof above establishes applicability.
The first parser searched entire proofs and incorrectly selected
numerators/denominators from finer rational inequalities, causing 14
failures. That invalid replay is preserved in
scripts/combined-ward-response/complete-cubic-comparison-audit-first-parser-failure.json.
Restricting extraction to the canonical Conclusion sections repairs
the parser. The failed run certifies no mathematical result. The
successful audit neither reevaluates source tensors nor independently
verifies a processor or BLAS implementation.

## Mathlib

Full matching specialized comparison: **not checked**. Supporting finite
addition of strict inequalities, monotonicity of integration, positivity of division and linearity
of limits: **not checked**. Unknown availability is not absence. All
load-bearing specialized coefficients and limits are imported by their
canonical equation/conclusion citations above; no new external theorem
or reproof of their numerical integrations is needed.
