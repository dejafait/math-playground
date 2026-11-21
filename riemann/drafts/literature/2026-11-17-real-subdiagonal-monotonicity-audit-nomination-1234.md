# Real subdiagonal monotonicity: independent audit nomination1234

TARGET: Audit C030u's fixed-real-rate subdiagonal monotonicity proof, including the signed Toda equation, positive-part convexity, and repeated-rate endpoint limits, under its full stated hypotheses.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1235 reuses the completed exact/stronger-result and obstruction searches in assessment1232/review1233 and assessment1228/review1229; targeted local searches in C030q-u and working1232/1234 found no independent completed monotonicity audit. No new general web search or novelty claim.
SOURCE_EVIDENCE: Read C030r and C030u in full; reused inspected primary coverage1232/1233 and1228/1229; refreshed Sra arXiv2611.02944v1 Lemma C.6/(C.10), pp23-24, including full-rank endpoints and coalescing rates, and C.9/(C.18)/(C.22), pp27-28. Exact audit scope below.
COMPARISON: The imported determinant interface covers the audit family; the inspected pointwise coefficient bound does not prove time monotonicity. C030u supplies explicit arguments for its signed evolution, convexity and endpoint limits, which require mathematical audit rather than an unproved external monotonicity import.
GAP: Source scope is ready for the exact saved audit; validity of C030u(3)-(9), full rank boundaries, zero crossings and repeated-rate limits remains unresolved. C030t and actual-Xi transfer are outside this audit.
REASON: Separate literature-only review1235 found no essential missing source premise for one conceptual audit; EXPLORE authorizes scrutiny of the written proof, not acceptance of monotonicity or a novelty finding.
SCOPE: C030u's exact positive fixed real-rate list, n>=max(4,2m), every required rank 1<=i<d<=floor(n/2), repeated rates, n=2m, all contrasts and both interval endpoints; auxiliary determinant ranks run from 0 to n.

## Main-gap relevance and discriminating audit

The main RH gap remains L030-L032/C032a actual-Xi positivity in every
degree. C030u claims beta_(i,0)(t)>=beta_(i,0)(x) for 0<t<=x, supplying
C030t's additional real-scale premise. C030t's conditional reduction is
a separate unaudited result and must not be treated as audited by this
continuation. Finite evolution, actual-Xi supply, degree/time, complement,
theta signing and graph realization remain independent.

The precise canonical proof is
[C030u](../../lemmas/C030u-real-subdiagonal-monotonicity.md).
Its essential established input is C030r, with the source qualifications
recorded there. Desnanot--Jacobi supplies the algebraic determinant
identity; the new argument uses the signed finite evolution and elementary
compact-orbit concentration, not positive-functional recurrence theory.
The numerical diagnostic is not a proof dependency.

The separate review should reuse the existing inspected theorem coverage
where it applies and decide whether any essential source hypothesis or
proof technique falls outside it. It must not repeat the source screen
merely because the proof is new. At nomination1234 this file was not ready; separate review1235 below completes its source scope.

After source approval, test every coefficient and boundary term in
C030u(3)-(6), the rank collection in (9), analyticity through repeated
rates, and the one-sided derivatives at zero crossings. Verify that
G_k tends to the minimum rank-k energy without a spectral-gap hypothesis,
that the near-zero signs hold simultaneously for the fixed finite family,
and that the final chord limit needs no uniform onset across families.
Continue only if the full proof survives; otherwise record the precise
logical failure and retain the original claim as unverified.

## Retained limits and routing

No change is made to parked joint-moment route1232 or the scoped prior
stops1117/1181/1193/1200/1107. No cross-notebook input is used. Mathlib
matching remains unchecked, not absent. This nomination makes no
additional mathematical claim beyond the pending C030u proof.

The eventual work is proof_audit/conceptual_audit, deep_research/xhigh:
the global sign comes from a nonsmooth convexity argument for a coupled
signed system, with degenerate spectral endpoint limits. It is not a
routine numerical replay or a possible complete RH solution. The required
separate source approval comes first. No justified new central creative
target is prepared; the actual-Xi signed input and its coverage remain
missing, and this essential audit should not be skipped.

## Completed literature-only source-scope review1235

17 November 2026. This is an EXPLORATION outcome: new comparison of the
written audit object's scope with existing coverage, without a new
mathematical result or a correctness verdict. No lemmas or mathematical
scripts were changed. The target above is unchanged.

LITERATURE_REASON: The supervisor requires separate approval of the new
C030u audit nomination; review1235 checks its precise proof techniques and
hypotheses against ready coverage, without repeating the earlier broad search.

### Primary input and specialization boundary

S. Sra, *On some positivity properties of the Riemann Xi function*,
[arXiv2611.02944v1, 2 November 2026](https://arxiv.org/pdf/2611.02944v1),
Lemma C.6/(C.10), pp23-24: refreshed the statement and proof through the
coalescing-rate case. It covers positive rates, repeats, probability Haar
normalization and every rank 0<=k<=n. C030u uses exactly C030r's zero-phase
case; no complex extension is needed. The finite rate list has a finite
upper bound, without a uniform bound across families.

Refreshed Theorem C.9/(C.18) and proof (C.22), pp27-28. Its smoothing
conclusion requires the extra degree inequality; C030u does not import
that conclusion. The coefficient identity and upper bound in (C.22)
are not the proposed two-time comparison. The unchanged prior assessment
already documents this difference. No reproof of the orbital formula
or a monotonicity theorem is authorized as a new source import.

### New proof scope versus existing coverage

Read C030u fully to identify its proof obligations, without deciding
them. Its additional tools are the standard named Desnanot--Jacobi
identity, finite differentiation, compact Haar integration and elementary
convexity. The manuscript includes the determinant-minor calculation,
full rank boundary treatment, concentration argument and one-sided
crossing argument explicitly. These are proof-audit objects, not
external claims left on an unread citation. No general signed-Toda
comparison theorem or positive-functional recurrence theorem is assumed.
No additional essential unread source was identified. This observation
does not validate any displayed identity or inequality in that proof.

Reused the Hirschman-Widder comparison in review1233 and the signed
recurrence/Toda and positive-measure scope comparisons in review1229.
They do not supply the desired monotonicity. The prior exact and stronger
result searches remain adequate for this unchanged fixed-real-rate
statement. No external broad search was repeated simply because a new
proof now exists. Unread spline and recurrence leads remain unread;
this assessment does not exclude their containing stronger results.

Targeted local searches covered C030q-u and working1232/1234 for
monotonicity, positive parts, Toda and the half-value premise. The proof
under review is C030u, not an independently audited duplicate. Read
stop records1117/1181/1193/1200/1107; their distinct unpaid transfers
neither refute this finite statement nor disappear if it survives.
The joint route remains parked and unfinished1218 is preserved.

### Bounded audit and route

Proceed on the exact TARGET only after the separate approval mechanism.
Essential established input: C030r. Audit object: C030u. C030q/C030t are
motivation or downstream context, not additional established premises
for monotonicity. Check C030u(3)-(9), every auxiliary rank 0..n,
coefficient signs, positivity needed for logarithms, local analyticity,
zero crossings, and both endpoint arguments with repeated rates. Keep
n=2m, all contrasts and each fixed rate family. A proof may use
family-dependent onsets only if its final universal comparison needs
no uniform onset. The rounded diagnostic is not proof evidence.

Continue downstream only if the full stated monotonicity survives;
otherwise record the exact failure and block its use. Do not silently
restrict rank, rate separation or degree. This audit does not include
C030t's phase reduction, finite evolution bounds, actual-Xi supply,
signing, complement payment, degree/time or graph realization. Those
remain independent. Main gap: L030-L032/C032a actual-Xi all-degree Q>=0.
Mathlib matching remains unchecked, not absent. No cross-notebook input.

Recommend proof_audit/conceptual_audit, deep_research/xhigh. The coupled
signed-system and nonsmooth global-sign argument need conceptual
scrutiny. No justified central creative target is prepared: the signed
actual-Xi input and its source coverage are missing. The essential
pending audit takes precedence over inventing a creative target.
