# Bounded Jensen Laplace reduction — nomination1387, source approval1388

TARGET: Audit C019n's bounded Jensen transfer, full Laplace tails, negative diagonal and origin-window bound, checking all cutoff jumps and the scope of the unpaid weighted remainder.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1388 reused ready1386 and review1386 in assessment1385, checked named step1387 history/attempt/working records and canonical C019n against C019l (8)-(27) and C019m (7)/(19); no completed audit duplicate found in these records. A displayed phase mismatch now takes priority; no new discovery search or novelty inference.
SOURCE_EVIDENCE: Review1388 directly rechecked DLMF1.14.17/Table1.14.4 first row and Koesters0803.1141v2 AppendixA.2-A.3 plus Section2 (2.4) and its sum/difference proof cases. Ready1377/1381/1386 cover the unchanged inherited inputs; ordinary Fubini/Tonelli, integral Cauchy-Schwarz and finite-piece integration by parts suffice for the proposed audit, subject to their hypotheses.
COMPARISON: Standard sources cover the scalar Laplace kernel and unweighted phase tests, not C019n's nonlinear weighted sign. Its hypotheses print a phase different from C019l (8)/C019m (7); reconcile that transcription before relying on inherited comparisons. SPECIALIZE approves checking and any justified in-scope correction, not accepting (1)-(5).
GAP: Audit the phase mismatch first, then retain or correct C019n (1)-(5) and delimit (15)-(17). No verdict on the intended corrected calculation or unpaid signed remainder is given here; (N), ordered samples, root separation and every-degree positivity remain open.
REASON: Separate literature approval1388 is complete for the unchanged saved audit target. Essential source coverage is accessible and adequate; proceed to conceptual mathematical audit next, with no further generic browsing. This review records a documentary discrepancy, not its repair or a new mathematical result.
SCOPE: Exactly C019n's hypotheses inherited from C019m/C019l, actual P and S_d, elementary V, integer d tending to infinity, h=3*pi/q, D, both moving times and floors, and one existential onset; no RH, nonvanishing, simplicity, independence, Gaussian law, effective onset or new target inequality.

## Reused source scope

The existing [assessment1386](2026-11-17-jensen-laplace-damped-product-attempt-1386.md)
approved the actual deterministic damping attempt. Its kernel reference is
NIST [DLMF Table1.14.4, first row](https://dlmf.nist.gov/1.14.T4), with
Re(s)>0; here the exact substituted denominator is strictly positive.
The full absolute double integral, rather than separate integrability at
each parameter, must justify Fubini. The stronger parameter-L1 transfer
in C019n must also be checked before truncating.

The existing [coverage1377](2026-11-17-jensen-heat-correlation-attempt-1377.md)
records the primary hypotheses of Koesters,
[arXiv:0803.1141v2, AppendixA](https://arxiv.org/html/0803.1141v2#A),
5 September2008, LemmasA.2-A.3 (Titchmarsh second edition Lemmas4.4/7.2).
The source's unweighted primitive estimate is not a theorem for an
arbitrary endogenous amplitude. C019n's finite piecewise integration
by parts and jump terms are precisely the specialization to audit.
No unread optional higher-moment, value-law or ratio source is an input.

## Exact audit scope and decision test

Read canonical C019n in full and the relevant C019l (8)-(27) and C019m
(2)/(19) ranges. Inherited L018/L021 and C019j/k conventions are unchanged.
Check the global coordinate-derivative bounds, parameter-L1 integral,
both tail budgets, common constants and the short negative window's
actual contribution. Verify that C019l's estimates used for the diagonal
are pointwise uniform before outer integration and that Cauchy-Schwarz
has the right inequality direction after multiplication by a negative
coefficient. Preserve all own-time and own-floor conventions.

Check integration by parts on the partition of every entry of either
whole sum, not just the selected pair's interval. Retain both product
channels and all indices. Distinguish a weak proved upper bound from a
lower bound on the actual remainder, and distinguish a sufficient
unproved condition from a consequence. No mathematical script is
needed unless a real uncertainty requires a meaningful certificate.

Retain the partial result only if these steps are valid uniformly at
one onset; otherwise identify and repair the first mathematical defect
within this scope. The audit must not claim that (N) or the main RH gap
is closed. Full matching Mathlib coverage is unchecked. The nomination
adds no new theorem and does not independently verify C019n.

Recommend proof_audit/conceptual_audit, deep_research/xhigh: the main
risks are the signed weighted comparison and the finite-jump/Fubini
bookkeeping. This is scrutiny of a partial established mechanism, not
a creative attempt or a possible complete-solution audit. Source
approval1388 below completes the nomination stage.

## Completed source approval1388 — 17 November 2026

This is the separate literature approval requested by step1387, for
exactly the TARGET above. DECISION remains SPECIALIZE. Read C019n in
full to delimit the claimed inputs and audit cases, not to issue an
independent mathematical verdict. No lemma or mathematical script was
changed, and no new estimate was derived. No essential source blocker
remains. Full matching Mathlib coverage is still unchecked.

### Primary sources and applicability

Reopened NIST [definition1.14.17](https://dlmf.nist.gov/1.14.E17)
and [Table1.14.4](https://dlmf.nist.gov/1.14.T4), first row, on
2026-11-17. The table gives the transform of 1 as 1/s for Re(s)>0.
C019n proposes s=1+a^2+b^2 for real a,b, within that domain. This
covers only the scalar identity; full double-integral absolute
integrability and parameter-L1 transfer remain audit obligations.
No claim that the table supplies a signed correlation estimate is valid.

Reopened H. Koesters, *On the Occurrence of the Sine Kernel in
Connection with the Shifted Moments of the Riemann zeta function*,
[arXiv:0803.1141v2](https://arxiv.org/html/0803.1141v2#A),
5 September2008, AppendixA.2-A.3. A.2 assumes a real twice
differentiable phase with second derivative of one sign, magnitude
at least epsilon throughout the interval, and gives 8/sqrt(epsilon).
A.3 bounds the reciprocal-log sum over 1<=m<n<=T by O(T log T).
These reproduce Titchmarsh second edition Lemmas4.4/7.2. Section2
(2.4) and its following proof retain both real-product channels,
true entry endpoints, separate equal indices, and first/second
phase estimates. They do not cover an endogenous discontinuous
weight automatically. No reproof of these source theorems is needed;
the local phase hypotheses, finite-piece amplitudes and all jumps
are the necessary specialization to check.

Ready1377/1381/1386 and assessment1385/review1386 remain adequate
for the unchanged heat/Jensen comparisons and exclusions of generic
joint-value imports. The source cases were inspected before the larger
Section2 passage. Unread optional higher-moment or random-matrix leads
are not essential inputs. Ordinary named Fubini/Tonelli and integral
Cauchy-Schwarz require, respectively, absolute integrability,
nonnegativity, and finite square integrals. Their verification belongs
to the audit; citing them does not verify C019n's bounds.

### Source-to-local definition discrepancy: first audit item

C019n's Hypotheses print
`f_n(Y)=Y*ell(Y)/2-Y/2-pi/8+pi*t(Y)*v_n(Y)/8`.
C019l (8) and C019m (7), which it explicitly claims to reuse, print
`f_n(Y)=vartheta(Y)-Y*log(n)+pi*t(Y)*v_n(Y)/8`, with
`vartheta(Y)=Y*ell(Y)/2-Y/2-pi/8`.
Thus the displayed definitions disagree by the term `-Y*log(n)`.
This is a direct textual comparison, not a derived counterexample
or an audit of the intended corrected lemma. The next audit must
resolve which definition is used and document any justified correction
before carrying over (6), the pointwise diagonal, or the phase tests.
Do not silently read the omitted term into the current canonical file.
Preserve step1387's completed work and stop evidence while checking it.

This new discrepancy changes the priority within the existing audit
and supports NEGATIVE as documentary evidence, not a mathematical
refutation of (N) or proof that the intended reduction fails. The rest
of the original audit scope above is unchanged: global derivative/L1
bounds, both tails, pointwise rather than integrated diagonal estimates,
inequality direction, every whole-sum entry and one common onset.
Retain only claims that survive those checks. An unpaid sufficient
bound R<=c_D B/2 must remain explicitly unpaid; a weak absolute upper
bound is not evidence that R is large or positive.

The origin-continuity/direct-variation closure stop in attempt1387
remains recorded. This review does not reopen that closure or parked
(A), nor treat historical stops as bans on independently tested methods.
The plausible use of a retained reduction is a later signed-remainder
test toward quantitative opposite-sign samples; reciprocal root mapping,
bulk separation and the main positivity gap remain independent.
Proceed next with the same TARGET under proof_audit/conceptual_audit,
deep_research/xhigh. Approval of source sufficiency is complete;
mathematical retention or correction is the next turn's work.
