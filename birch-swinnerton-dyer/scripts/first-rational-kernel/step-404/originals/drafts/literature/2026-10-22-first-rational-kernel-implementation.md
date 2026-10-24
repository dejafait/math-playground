# First complete rational kernel — implementation coverage approved

TARGET: Implement and independently replay L102's unchanged rational kernel scheme for n=1 at the midpoint of a certified enclosure of 2*pi/sqrt(389) of radius at most 2^-50, in one run capped at 180 seconds and 134217728 output bytes.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused drafts/source-notes/2026-10-21-rational-kernel-source-review.md and drafts/source-notes/2026-10-22-rational-kernel-audit-coverage.md; inspected L102's construction/replay contract and step-402 audit, L031's elementary parameter rules and L101's hypotheses/contract. Targeted local comparison found no completed first-kernel implementation; ATTEMPTS/043/045/046 preserve different comparison, adaptation and unavailable-library failures. New primary searches were site:dlmf.nist.gov Machin arctan 239 5 and site:dlmf.nist.gov 4.24 arctan series.
SOURCE_EVIDENCE: Reuse audited L102 and its precisely cited DLMF Taylor/integration inputs; L031 lines 174--198 supply exact outward endpoints, square-root inequalities and Machin adjacent-sum enclosure. Newly inspected DLMF 4.24.3 with |z|<=1, z!=+/-i, and Mathlib Real.four_mul_arctan_inv_5_sub_arctan_inv_239 (complete unconditional statement). Source/version and applicability details follow below.
COMPARISON: Known sources and audited L102 cover containment for this unchanged real-positive domain. They do not provide an implementation, narrow actual parameter, complete executed replay or a practical runtime/byte guarantee. The necessary specialization is finite implementation and complete replay under the fixed contract below, with actual acceptance inequalities rather than an inferred feasibility claim.
GAP: Essential source coverage for this exact one-kernel attempt is sufficient; parameter endpoints and kernel evidence remain uncomputed, and runtime/output feasibility remains an execution test. All other kernels, coefficients, derivative zero exclusion and arbitrary-curve rank comparison remain absent.
REASON: The changed narrow-parameter and implementation scope required this separate review; its endpoint cases and full replay/persistence obligations are now specified without deriving new mathematics or running a mathematical program.
SCOPE: Only n=1, certified midpoint in [3/10,1/2], all 1016 original panels, degrees 128+64+64 with all full product pairs, sixteen scalar squarings, outward grid 2^-256, actual kernel radius <=2^-50. One aggregate 180-second/134217728-byte execution includes parameter construction, production, independent replay, certificate writing and preservation; no retry or cap enlargement.
LITERATURE_REASON: Prior approval covered a proof audit only; the essential changed scope is actual narrow-parameter certification plus complete finite implementation/replay and one aggregate resource contract.

## Relevance, duplicates and exclusions

The main gap is rank E(Q)=ord_(s=1)L(E,s) for arbitrary curves of
analytic order at least two. This intermediate target tests a working
finite-kernel backend and its actual cost before any other kernels or
signed derivative sum. L035 already imports this fixed curve's complex
order, so success changes provenance only. No new BSD case is sought.

Reused the earlier inspected Taylor/integration source assessment rather
than repeating broad discovery. Read the complete L102 construction,
its replay obligations and relevant audit cases; L031's endpoint and
parameter passage; L101's hypotheses and finite-error contract. Searched
the specific rational-plan assessments, step-402 record and critical-audit
note for duplication. No executed first kernel is supplied there.
ATTEMPTS/043 concerns complex/p-adic comparison, /045 a nonunique table
adaptation marker, /046 an unavailable library. None disproves this
rational mechanism. Preserve their stops; no library installation or
optional unread Taylor-model theorem is a dependency.

## Inspected primary statements and specialization

[DLMF 4.24.3](https://dlmf.nist.gov/4.24.E3), online chapter inspected
2026-10-22 (the reused source record identifies DLMF v1.2.8), gives
the arctangent odd-power series for |z|<=1, z!=+/-i. Both real
arguments 1/5 and 1/239 lie strictly inside its domain. The finite
adjacent-partial-sum enclosure is already justified in L031, including
the sign and decreasing-term condition. Reuse that rule; the infinite
series identity alone is not treated as an error certificate.

The inspected current Mathlib documentation contains the complete
unconditional theorem
[Real.four_mul_arctan_inv_5_sub_arctan_inv_239](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Arctan.html#Real.four_mul_arctan_inv_5_sub_arctan_inv_239):
4 arctan(5^-1)-arctan(239^-1)=pi/4. This is supporting formal coverage
for L031's Machin identity; no branch selection or new reproof is needed.
The rolling documentation's commit was not pinned or compiled locally.
Full L102 algorithm/certificate coverage in Mathlib remains not checked.

L031's square-root enclosure uses nonnegative integer square inequalities;
for sqrt389 the denominator is strictly positive. Its instance's
2^-48 grid is not a restriction on the exact floor/ceiling rule.
The approved implementation may use the same 24-term adjacent sums
and square-root inequalities at grid 2^-256, with exact rational
Machin sums before conversion. This is an application of the existing
rules, not a claimed evaluated width: the actual resulting c endpoints
must pass the radius and range tests. Failure stops this attempt;
no extra terms, refinement loop or altered precision is approved.

Python's official math documentation was also inspected for integer
square-root support; it lists math.isqrt and distinguishes floating
math.pi/sqrt. No runtime version or executable support was tested.
The certificate must verify square inequalities directly, so an integer
root routine is only a witness producer, not a trusted transcendental
primitive. No floating pi, square root, exp or log enters containment.

The positive real panel domain, endpoint y=1, full product degree,
scalar reduction and all analytic enlargements are unchanged from
audited L102. No new smoothness, branch or Taylor-remainder case is
introduced. Reproof of those standard theorems would add no needed
coverage. Their audited specialization supplies the error justification;
execution must still verify every prescribed operation.

## Approved complete finite evidence and replay contract

Before the one capped execution, choose explicit producer and separately
written replay code. The same exact mathematical schedule must be used;
shared immutable constants are allowed, shared producer arithmetic or
coefficient/convolution functions are not an independent replay.
No preliminary kernel benchmark, hidden retry or resumed partial pass.
All setup that reads inputs, builds inventories or writes generated
execution sources must be inside the aggregate watchdog and byte cap.

Persist source bytes and hashes, fixed input inventory/hashes, a manifest
with exact integer/rational encodings and constants, a parameter witness,
one record for every panel, full replay report and final resource/status
report. The parameter witness includes every term of both adjacent
arctangent sums, exact Machin bounds, square-root integers and their
square inequalities, positive division bounds, c_l,c_u,c_* and delta.
Replay reconstructs them independently and checks
3/10<=c_l<=c_u<=1/2 and delta<=2^-50, in addition to containment
via the cited identities and exact endpoint operations.

Each panel record identifies its index and exact endpoints, binary log
reduction, scalar log and exponential intervals, integrated polynomial
interval and running sum. Store stage digests and operation counts as
provenance diagnostics; they are not substitutes for recomputation.
Full coefficient arrays and scalar traces may be recomputed rather
than persisted. This storage choice does not omit any replay operation.

Replay independently constructs every scalar-series term and tail,
every conversion, sign, rounded endpoint and containing clip; all
sixteen squares; all 129/65/65 factor slots; all 193 and 257 product
slots, with every 8385 and 12545 coefficient pair, including zeros;
all 257 integration divisors; scalar multiplication, dy=ds/8, every
panel and cumulative sum, and the exact final +/-2^-184 enlargement.
Use independent signed floor/ceiling checks and a distinct convolution
loop ordering. Check every reconstructed stage against recorded stage
outputs/digests, every panel integral and running sum by exact equality.
Hash equality alone does not validate arithmetic; the reconstructed
complete operations and containment proof do. Missing panels, fields,
terms or mismatches are failures, not warnings to bypass.

Record the full exact final endpoints, midpoint and actual radius,
and verify ordering and radius<=2^-50 with exact integer comparisons.
Also report comparison to L102's stronger <2^-183 prediction, preserving
any discrepancy as a failure of the unchanged scheme. The accepted
numerical integral is J_1(c_*), not J_1(c). All original inventories
must match at the end; hash preservation alone proves no mathematics.

A single watchdog covers production and full replay through final
writing/preservation. Account for generated sources, certificates,
logs and fixed copies in the 134217728-byte output budget. Reserve
space/time for a stop record; report actual values and conservative
inclusive bounds. Do not claim a pass after timeout, byte overflow,
arithmetic failure, missing replay or incomplete preservation. Preserve
partial artifacts and the first failure, then stop without a retry or
larger cap. A later materially different target needs its own review.

## Decision and continuation test

SPECIALIZE authorizes one REPRODUCTION implementation attempt under
this exact contract. There is no source claim of practical feasibility
and no new lemma or mathematical program in this review. Continue only
if the parameter, every panel, full replay, final radius and aggregate
resource checks all pass; otherwise preserve the negative evidence and
park this execution plan. Even success does not license the other 127
kernels or establish their aggregate runtime.

Essential direct inputs are audited L102, L031's elementary endpoint/
parameter rules and audited L101's kernel definition. Eventual analytic
use still needs L030, independent L031 coefficients/Fricke sign,
audited L099 and foundations/02. No L035/L100, published basis/Sha,
normalization or unavailable executable enters this integral certificate.
The derivative still requires all remaining kernels, coefficients and
L101's B=2^-43+200*delta+4*sum(|a_n|/n)e_n with eta=0, followed by
strict zero exclusion. Zero containment remains inconclusive. No
arbitrary-curve rank comparison, full Sha result or refined formula
follows. PROOF.md and DAG.md need no argument change.
