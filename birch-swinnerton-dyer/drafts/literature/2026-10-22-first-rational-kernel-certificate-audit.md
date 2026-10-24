# First rational kernel certificate — critical-audit coverage approved

TARGET: Critically audit L103's step-404 n=1 rational-kernel certificate, including complete parameter and panel replay, independent signed rounding, and aggregate resource and preservation evidence, without producing another kernel.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready implementation assessment and drafts/source-notes/2026-10-22-rational-kernel-audit-coverage.md; searched the specific rational-kernel assessments, history/399--404 and ATTEMPTS/043/045/046, then read L103 in full, relevant L031/L101/L102 passages, step-402 audit and static runner/replay interfaces. No separate completed L103 audit was found in these records; no novelty inference follows.
SOURCE_EVIDENCE: Reused the previously inspected Taylor/series and Mathlib Machin coverage; reinspected NIST DLMF v1.2.8 (2026-09-15), 4.24.3, 1.4.26/28/29/35--37 and 4.8.16, including hypotheses and endpoint cases. Newly inspected official Python 3.15.1 time.monotonic, signal.setitimer and signal-handler execution contracts; fixed manifest reports Python 3.15.0. Details and audit obligations below.
COMPARISON: Known identities and audited L102 cover the unchanged positive-real scheme; they supply neither L103's executed arithmetic nor historical resource/preservation evidence. Separate complete fixed-evidence replay and critical comparison are required. Timer semantics do not establish a hard final-report deadline; measured bounds and reporting allowances must be assessed explicitly.
GAP: Source scope for this exact audit is sufficient; L103's numerical, independence, resource and preservation assertions remain unaudited. This is one finite midpoint kernel only; remaining kernels, derivative zero exclusion and arbitrary-curve rank comparison remain absent.
REASON: Changed validation scope is mapped to inspected source cases and a bounded audit contract; SPECIALIZE permits a separate REPRODUCTION audit, not import of an execution result or a new mathematical theorem.
LITERATURE_REASON: The new exact target audits newly executed parameter/panel and resource evidence in L103; prior coverage authorized construction rather than this separate critical audit.
SCOPE: Fixed step-404 evidence only; one complete independent audit replay under one aggregate 180-second/134217728-byte audit cap including setup and reporting. No producer or run_once.py execution, retry, new kernel, changed numerical caps or derivative computation. Original execution claims are checked as historical recorded evidence, separately from fresh audit measurements.

The main gap remains arbitrary-curve rank/complex-order comparison.
The intermediate target is independent critical validation of the one
actual n=1 backend certificate before any downstream use. This may
change fixed-case evidence provenance; L035 already imports this curve's
analytic order. No novelty or new BSD case is claimed.

Essential inputs are L031's parameter rules, audited L102, L101's
kernel definition, L103 and the exact static sources plus full finite
evidence in `scripts/first-rational-kernel/step-404/`. The audit must
compare all arctangent terms and squared inequalities, all 1016 panels,
every signed interval primitive, sixteen squares, all 129/65/65 factor
slots, both complete convolutions, all 257 integration divisors and
the final enlargement. Stage digests supplement exact complete
reconstruction; they are not substitutes for arithmetic checks.

The implementation pass reports actual radius
(2^72+2883372)/2^256 <2^-183<2^-50, complete replay of 21264880 pairs
per pass, and conservative inclusive bounds 28 seconds/1717513 bytes
against 180/134217728. Those are claims for the future audit to check,
not an already completed independent critical review. This assessment
approves the separate audit scope below; no replay occurs this turn.

Continue only if the complete evidence and all containment/resource
claims survive review; otherwise preserve the first counterexample or
failed obligation and park dependent use. Remaining kernels, exact
coefficient data, L101's parameter-weighted full error bound and zero
exclusion remain independent unresolved obligations. Eventual analytic
use still retains L030, independent L031 sign/coefficient data, audited
L099 and foundations/02; no published basis/Sha or L035/L100 is used
by this integral certificate. Full Mathlib algorithm coverage is not
checked. This literature review derives no estimate and executes no
mathematical program. The approved audit is a separate research turn.

## Source comparison and applicability

Step 405 (2026-10-22) reuses ready implementation coverage and the
step-400 source comparison rather than reopening broad discovery.
Read L103 for scope, not as independent verification of its own claims.
The step-402 audit is the existing validation of L102's mathematical
scheme. ATTEMPTS/043 concerns complex/p-adic comparison, /045 a different
source-adaptation stop, and /046 an unavailable library backend. Preserve
those stops; none supplies a duplicate L103 audit or a rational-method
obstruction. Optional unread Taylor-model results are not inputs.

Primary cases reinspected: NIST DLMF v1.2.8, released 2026-09-15,
online access 2026-10-22. The cited books were not separately read.

- [4.24.3](https://dlmf.nist.gov/4.24.E3) gives the arctangent
  series for |z|<=1, z!=+/-i. Real 1/5 and 1/239 satisfy this;
  L031 supplies the justified adjacent-sum error rule.
- [1.4.35--37](https://dlmf.nist.gov/1.4.vi) assume C^(d+1)
  regularity on [a,b]. The Lagrange case has a<c<x; at x=a use
  the finite identity. Positive log/reciprocal arguments and the
  entire exponential cover every original panel, including y=1.
- [1.4.26/28/29](https://dlmf.nist.gov/1.4.v) cover continuous
  primitive integration, continuous/piecewise-continuous derivative
  change of variable, and continuous integrand with nonnegative
  integrable weight. The unchanged affine panel map and polynomial
  integrals meet these cases.
- [4.8.16](https://dlmf.nist.gov/4.8.E16) gives exponential
  multiplication for complex arguments, covering real factorization
  and squaring; it does not certify their rounded execution.

Reuse the inspected 4.2.19, 4.6.1/4, 4.7.3/7/8/10, 4.8.2 and
1.2.11 cases recorded in the step-400 source note and L102.
Positive logarithm arguments retain the phase condition. No function,
branch or singular endpoint changes. Import these results without
reproof; L102 remains the quantitative specialization. The audit must
check that fixed evidence implements its entire scheme.

The official [time.monotonic contract](https://docs.python.org/3/library/time.html#time.monotonic)
uses clock differences unaffected by system-clock updates.
The official [setitimer contract](https://docs.python.org/3/library/signal.html#signal.setitimer)
specifies timer firing/clearing; that page's handler-execution section
explains delayed dispatch, including delays in C code. These rolling
pages identify Python 3.15.1; the complete selected manifest /python
field identifies the fixed run as Python 3.15.0. This is interface
coverage, not a pinned binary or verification of historical elapsed time.
The inspected runner clears the timer before preservation/reporting;
its final elapsed assertion and allowances are separate audit evidence.
No source guarantees six-second finalization. Distinguish successful-run
measurements from any stronger hard-watchdog interpretation.

Reuse supporting Mathlib coverage from the implementation assessment:
Real.four_mul_arctan_inv_5_sub_arctan_inv_239, directly linked in
L103. Its unconditional statement was inspected there; no compilation
or commit pin is claimed. Full certificate coverage remains not checked,
not absent. No imported theorem supplies this execution certificate.

## Approved separate audit and stopping contract

Before one replay, read the complete static producer/replayer/runner
and compare them with inventoried copies. Use a fresh audit directory;
preserve all step-404 evidence and eleven inventoried original/copy pairs.
The four post-run navigation bridges described in L103 are metadata,
not inventoried inputs. Record any changed input explicitly; no pathname
exemptions, original certificate edits or exclusive-directory reruns.

Reconstruct the complete parameter certificate: all arctangent terms,
exact sums, squared root inequalities, signed grid conversions and
positive interval divisions. Compare c_l,c_u,c_*,delta and all bounds.
Replay all 1016 panels, every scalar term/clip, sixteen squares, all
factor slots, both full convolutions including zeros, every integration
divisor/running sum and the final analytic enlargement. Exact endpoints,
midpoint and radius must agree. Test required radius <=2^-50 and the
stronger claimed <2^-183, preserving any failed stronger obligation.
These are future checks, not calculations performed by this review.

Review all signed floor/ceiling and multiplication branches independently
against integer inequalities/four-product extrema, retaining zeros and
zero crossings. A fresh audit wrapper may check every encountered
primitive by that separate rule during the single complete fixed replay.
Check full loop coverage and counters; stage digests and saved PASS
flags supplement arithmetic, never replace it. Compare the containment
interface with audited L102. Producer arithmetic is not an independent
correctness check. Recomputed traces are allowed by the original contract.

For historical resources inspect complete relevant status, manifest and
preservation fields; reconcile counting boundaries, original/fixed file
sizes, diagnostic/status reserves, reporting allowance and any retained
terminal record. A fresh measurement cannot reconstruct historical wall
time. If a claimed historical boundary lacks retained evidence, record
the qualification or failed obligation; do not supply it with a new run.
This turn's bounded JSON previews only located source paths/reported
resources and establish no verification; /python was read completely.

For the fresh audit start one aggregate clock/cap before inventories,
harness generation/imports or copying. Include all fresh sources, copies,
certificates/logs and final preservation/report writing in <=180 seconds
and <=134217728 output bytes; report actual inclusive bounds and reserve
reporting resources. Existing evidence is read-only input; copied bytes
count as new output. No retry, resumption, cap enlargement, run_once.py
execution or second kernel. Preserve the first failure and partial work.

Continue dependent use only if all load-bearing containment, complete
replay, required-radius and preservation obligations survive. Retain
resource/provenance qualifications separately; they cannot supply
mathematical containment. Failed load-bearing evidence parks dependent
use. All independent analytic and arbitrary-curve gaps above remain.
