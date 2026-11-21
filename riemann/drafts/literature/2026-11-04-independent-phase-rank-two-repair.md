# Independent-phase Fourier extraction — completed source comparison

TARGET: At (3,2048), replace recursive Fourier powers by independently enclosed phases with L=2048 and N=512, reusing step435 data, and certify the full signed determinant and original-norm comparison.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step436 reused the signed-rank-two, fixed-pair and Decimal assessments; inspected L779's complete relevant extraction/error argument, L778's trig/audit ranges, signed_pair_435.py sincos/fourier and the recorded step435 failure. Targeted searches located NIST periodicity/De Moivre/Taylor statements and FLINT's independent rational-angle implementation; primary statements and the pinned implementation were read as detailed below. No novelty inference or new calculation.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), equations 4.14.3, 4.14.8–9, 4.19.1–2, 4.20.1–2, 4.21.2–3/34 and 1.4.35–37; FLINT v3.3.1 src/acb/unit_root.c complete 41-line file. Reuse assessed Duits AppendixA Lemmas66/69, Bornemann Sections2–4 and (4.1), Johansson 1802.07942v1 Sections2/2.1/4 and Python/mpdecimal contracts. Exact URLs and applicability below; no essential source is blocked.
COMPARISON: Integer-phase reduction and independent sine/cosine enclosure are standard and fit L778's already audited real-angle Taylor primitive. They may replace recursive rectangles without changing the exact Fourier factors or operator. Sources do not supply repaired coefficient errors or the actual sign/norm separation. Necessary remaining work is one known-method implementation/specialization, not new mathematics beyond these sources.
GAP: Coverage is ready for one fixed L=2048,N=512,precision75 repair. Uniform phase-table containment, complete Fourier intervals, both negative-mode exclusions, aliases, HS/trace-product errors, signed pairing and both Grams must be checked in the later calculation. Reuse of L779's evaluator/counts/grouping/residues retains its unaudited analytic qualifications. No repaired bound or actual determinant/norm conclusion was established here.
REASON: The changed phase mechanism addresses the recorded wrapping failure by a separately testable implementation change. Approve its one later fixed calculation with the original separation threshold; preserve all failed evidence and prohibit sweeps. The starting source-review action is completed below; TARGET records the concrete ready continuation.
LITERATURE_REASON: Step435 measured epsilon_512>4.017e6 versus infinite-tail HS bound<1.722e-17. Exact-index independent phases are a changed implementation lead outside the previous recursive implementation review. This turn checks only that missing scope, reusing the determinant/counting/Decimal coverage.
SCOPE: Actual G and original Hilbert norm, (r,R)=(3,2048), sigma=9/8, L=2048, N=512, precision75 and the existing trig degrees129/128. One later repair using step435's saved data; no numerical run, new lemma or mathematical-script edit in step436. A newly ready continuation remains subject to the supervisor's separate next-turn approval.

## Completed review — step436

The reviewed starting action was: Assess independent trigonometric-phase
Fourier extraction at (3,2048), reusing the saved evaluator, contours and
root brackets, to replace the failed recursive rectangular power certificate.
The mathematical target and its threshold are preserved; this review does
not execute that repair.

The main gap is actual-Xi all-degree mixed positivity. The intermediate
test asks whether the actual signed determinant stays positive when the
original operator norm is at least1. Its possible downstream use is deciding
whether signed interactions merit a growing-order estimate. Independently
paid interaction/reciprocal bounds, all orders and exceptional signs remain
open even if this finite diagnostic succeeds.

### Primary statements and their scope

NIST *Digital Library of Mathematical Functions*, v1.2.8, release
2026-09-15, accessed2026-11-04:

- [4.14.3 and 4.14.8–9](https://dlmf.nist.gov/4.14) give the exponential
  representation and integer-period identities for sine/cosine.
- [4.21.34](https://dlmf.nist.gov/4.21#E34) is De Moivre's theorem for
  integer n. The addition formulas4.21.2–3 supply quadrant rotations.
  Only integer exponents and real rational multiples of pi are used;
  the source's separate fractional/complex-exponent qualification is
  irrelevant and is not imported.
- [4.19.1–2](https://dlmf.nist.gov/4.19) give the entire sine/cosine series.
  [1.4.35–37](https://dlmf.nist.gov/1.4#vi) state Taylor's theorem for
  f in C^(n+1)[a,b], including the intermediate-point and integral
  remainder. [4.20.1–2](https://dlmf.nist.gov/4.20) give the derivatives.
  These cover the same real-angle primitive already audited in L778:
  true reduced angles in [0,pi/2], enclosing intervals in [0,2), enclosed
  pi, outward finite arithmetic and the retained common factorial error.
  They do not assert that a rounded polynomial alone is an enclosure.

The applicability is direct substitution of the integer indices j,n and
L=2048 in these identities. Required later implementation: compute the
phase index (-j*n) modulo L with exact integers, then use its independently
enclosed root-of-unity phase. The already saved table of2048 `z` rectangles
may be reused if its complete index coverage and original containment
proof are retained. Alternatively reproduce that same table at unchanged
precision/degrees. No recursive complex powers, interval-valued index,
floating remainder, or multiplication of an unreduced large angle is
needed. These are standard imported identities, not a newly proved lemma.

FLINT [v3.3.1 src/acb/unit_root.c](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/acb/unit_root.c),
complete file read: the generic case forms exact rational2/order and calls
`arb_sin_cos_pi_fmpq`; orders1,2,4 are exact special cases. This is primary
implementation overlap for rational-angle evaluation, not a substitute
software contract for the Decimal calculation. No FLINT dependency or
algorithm reproof is proposed. A current FLINT API leaf failed a repeat
access after its landing page was located; it supplies no essential input.
The NIST identities and reused audited primitive suffice.

### Reuse and retained obligations

The ready source assessments are
`2026-11-04-signed-rank-two-fredholm-diagnostic.md`,
`2026-11-04-actual-fredholm-fixed-pair-norm-test.md` and
`2026-11-04-actual-fixed-pair-certificate-audit.md` in this directory.
They supply the precise finite-rank, general trace-class perturbation,
compact analytic enclosure and Decimal contracts. No repeated Fredholm
discovery is needed. Bornemann's positive-selfadjoint small-norm lemma
remains excluded. L778's old radius1600 bounds are not substituted for
L779's enlarged evaluator. No full Mathlib match has been checked.

L779 remains canonical for the saved radius4096 evaluator, both count2
contours, strict simple grouping, complete residues/F bounds, signed
pairing and full-product trace-error transfer. Read its relevant proof
in full, not a certificate preview; no saved numerical evidence was
reverified in this source turn. Its analytic implementation is still
unaudited independently. All reuse must carry that qualification and
the trusted Decimal contracts, without silently promoting either.

In the later repair retain the original2048 sampled b enclosures, or
reproduce them at the same settings, keeping all node/evaluator/root
uncertainty. Each phase interval and sampled b interval must contain its
own exact value; statistical independence is not a hypothesis. Shared
pi uncertainty must stay enclosed rather than be cancelled. Save every
phase rectangle and the exact phase-index rule; check all indices and
the uniform component-error bound, not selected favorable entries.

Recompute every complete coefficient interval and all512 epsilon values,
including multiplication/summation rounding and the old alias allowance.
Do not reuse old hats as certified new coefficients or delete uncertain
imaginary components. Retain L779's exclusion of BOTH modes-2,-1, its
absolute-convergence justification, positive F lower bound and infinite
tail. Recompute the weighted Hilbert–Schmidt error, full trace-norm product
with cross term, finite signed determinant and both original-norm endpoints.
Retain both Gram matrices, adjoints/order/minus sign, possibly singular
Gram handling and the separate bounds needed by Bornemann(4.1).
Small phase errors alone do not certify any of these transfers.

### Duplicate/failure comparison and bounded decision

Local reads included step434/435 histories and
`ATTEMPTS/2026-11-04-signed-rank-two-recursive-power-certificate-failure.md`.
The previous recursive calculation is the relevant failed implementation,
not a duplicate successful repair. L778's scalar test and the distinct
shifted-boundary/q-Pascal stops retain their stated scopes. Low-order Xi
nonnegativity already overlaps the finite sign question, as assessed in
step434; repairing this certificate would not be a new low-order sign
theorem. No novelty is inferred from local or external search.

Continue only if the COMPLETE actual determinant lower endpoint>0 and
original norm lower endpoint>=1. If the norm upper endpoint<1, stop this
finite-pair escalation. Crossing either threshold is inconclusive; failed
admissibility or invalid reused data parks the repair. Preserve complete
failures, actual/required endpoints and all historical certificates. One
fixed run only: no precision, radius, degree or resolution sweep, and no
automatic refinement. A later successful certificate still needs its
own critical audit; this approval is method coverage only.

No creative central target is justified yet: no actual signed advantage
or independently paid growing-order budget has been certified. This
concrete repair is calculation/standard/high, not creative mathematics.
The mathematical exploration budget is unchanged by this literature step.
No cross-notebook input, new mathematical result or script was produced.

Searches: `site.flintlib.org doc acb unit_root exp_pi_i sin_pi exact rational
argument`; `site.dlmf.nist.gov 4.19 sine cosine Maclaurin series remainder`.
Search extracts were leads; the statements and pinned code above were
opened, including Taylor's hypotheses and both remainder forms. Reuse
of the inspected prior assessments supplies the unchanged theorem coverage.

## Original nomination — step435 (historical, superseded by review above)

This is an uncovered nomination, not an approval or another mathematical
attempt. The next turn is source comparison only. Full proofs and actual
certificate limitations stay in L779. Its finite approximant is not an
actual sign or norm lower bound.

Essential inputs are L017/L018/L021/L776/L777/L778/L779 and the existing
finite-rank, trace-ideal, counting and Decimal assessments. The saved
evaluator on |w|<=4096, both complete count2 contours, true grouping,
root brackets/residues and all independent analytic qualifications must
be reviewed for reuse, not silently treated as independently audited.
No zero list, RH, real/simple-zero premise, minor sign, cross-notebook
theorem or hidden reciprocal bound is allowed. Check compatibility with
the full-product trace error, not just small pointwise phase error.

If approved, nominate one fixed (3,2048), L=2048, N=512 repair using
independently bounded phases instead of recursively multiplied rectangles.
Do not execute it in the approval turn. The downstream test stays
determinant lower endpoint>0 and original norm lower endpoint>=1;
crossing intervals remain inconclusive, and norm upper endpoint<1 stops
finite-pair escalation. No new uniform/growing-order claim is proposed.

A protected creative central mechanism is not justified yet: the signed
advantage is still an uncertified finite-approximant observation, and no
independently paid growing-order interaction/reciprocal budget exists.
This specific implementation repair is routine development, not creative
mathematics. Full Mathlib matching remains unchecked.
