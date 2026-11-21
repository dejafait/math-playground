# Independent finite-parity certificate audit — approved source scope

TARGET: Audit L759's finite simple-even certificate at lambda=sqrt(13), N=120, including the defining archimedean integral, all series and rounding bounds, and interval inertia counts.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step360 reused exact-cell and parent source/title/obstruction searches; narrowly checked L759, the finite-parity assessments and steps358-359, including the superseded first-pass failure. Read the primary numerical-method passages listed below; no fresh general-parity discovery or novelty claim.
SOURCE_EVIDENCE: CCM https://arxiv.org/html/2511.22755v1 Lemma2.3 with derivation, (3.13), (3.21), (4.1)-(4.4) with exterior-correction derivation, Lemmas5.1-5.2 with proofs and Definition5.3; https://dlmf.nist.gov/2.10.E1 and https://dlmf.nist.gov/24.8.E1 including hypotheses; Python3.15 Decimal Context/rounding/ln/exp/sqrt/next_minus/next_plus https://docs.python.org/3.15/library/decimal.html; Decimal Arithmetic Specification1.70 square-root/ln/exp https://speleotrove.com/decimal/daops.html; standard named finite-dimensional spectral theorem and Sylvester law of inertia.
COMPARISON: L759 is a computer-assisted finite specialization of the source matrix, with elementary series evaluation and interval Sylvester inertia; it is not a general simple-even theorem, a determinant convergence theorem or an RH sign result.
GAP: Sources supply matrix definitions and standard analytic/software tools, but do not verify L759's reductions, error expressions, implementation or saved pivots. These exact checks remain for the separately authorized audit.
REASON: Separate literature-only approval now completes the previously missing audit coverage; reproduction of the finite certificate may be critically checked next turn. No numerical replay, new derivation or proof approval is performed here.
SCOPE: Only L759 and scripts/spectral-triples/finite-parity-359.py/.json plus the consistency-check artifact; all original and corrected evidence retained. No new parameter cell or eigenfunction comparison is nominated.
LITERATURE_REASON: The exact audit continuation entered with REVIEW_REQUIRED coverage; essential numerical-method hypotheses and software-contract scope required separate inspection despite ready coverage of the original calculation.

## Separate approval — step360, 4 November 2026

Reuse the parent assessment for the determinant theorem and general
route comparison. The matrix source is Connes--Consani--Moscovici,
*Zeta Spectral Triples*, arXiv:2511.22755v1, 27 November 2025.
The inspected passages cover the signed finite matrix, regularized
archimedean integral and parity invariance, including the diagonal and
off-diagonal convolution cases. The hypotheses are lambda>1 and positive
integer N, met by the proposed cell. The simple-even property is a
separate hypothesis in Definition5.3. Existing numerical examples do
not replace this certificate's verification. Source formulas may be
imported; their scalar-series implementation must still be checked.

The precise analytic tools are NIST DLMF 2.10.1 and 24.8.1
(live pages inspected on the checked date). The former assumes integer
endpoints and m>0, with absolutely integrable derivative of order 2m;
it retains a periodic-Bernoulli remainder and sums corrections only
through m-1. The latter covers n>=1 and 0<=x<=1, including endpoints.
For the proposed use, the audit must justify passing the finite upper
endpoint to infinity and all derivative integrals, as well as comparing
the actual implemented two-term inflation with this remainder. No
favorable remainder sign is supplied by this approval.

The local interpreter identifies as Python3.15.0; the online versioned
3.15 reference currently identifies as 3.15.2. It documents context
precision/directed arithmetic, correctly rounded half-even ln/exp,
sqrt to full precision, exact copy_negate and adjacent representable
numbers. Context methods correspond to Decimal methods with an explicit
context. The linked General Decimal Arithmetic Specification1.70
(7 April 2009), square-root section, explicitly uses half-even rounding
independently of context rounding. Its generic ln/exp allowance is
weaker (up to one ulp); use Python's stronger documented contract for
those operations. This is a declared interpreter/library trust
assumption, not an implementation-conformance proof. The audit must
check all conversions, operator dispatch, exponent limits and
outward-enclosure operations; reading a contract does not verify them.

For finite real symmetric matrices, the standard named spectral theorem
and Sylvester law of inertia suffice as external algebraic inputs.
The remaining specialization is to verify the exact parity bases,
nonzero pivots and congruence/elimination bookkeeping for every shifted
matrix, with every entry uncertainty propagated. No generic software
theorem certifies this particular hand-written interval program.

Approved audit tasks, all within the exact TARGET:

1. Compare the source's defining integral with L759's canceled reduction;
   check zero-frequency and endpoint cases and the full prime-power list.
2. Check all series interchanges, four geometric/exponential tails,
   inverse-power Euler--Maclaurin and gamma bounds, and constant/trig
   evaluation. The earlier one-term inflation is not evidence.
3. Inspect the entire implementation and complete relevant certificate,
   then independently replay interval inertia. A same-program rerun alone
   is a reproducibility check, not independent correctness evidence.
4. Establish only the stated finite strict gap if every check succeeds;
   otherwise isolate the defect and the surviving conclusion. Overlap
   is inconclusive, not a degeneracy or an RH counterexample.

Downstream use remains one anchor for the arithmetic rank-one
construction. General parity, normalized limits, eigenfunction
comparison and Xi transfer remain independent gaps. No justified
quantitative eigenfunction mechanism is ready for a creative turn;
the essential certificate audit takes priority. Full matching Mathlib
coverage remains unchecked, not absent. This SPECIALIZE assessment
authorizes REPRODUCTION on the unchanged target next turn.

## Retained nomination qualifications (step359)

The preceding approved assessment remains unchanged. The successful run
uses two Euler--Maclaurin last-term losses and shifts 10^-55, 5*10^-56;
the preliminary first-pass file is not proof evidence. Audit must not
substitute a floating eigenpair or certificate preview for the complete
relevant entry/error and pivot evidence. A positive audit certifies only
this finite parity gap. A failed audit should identify the actual error
and surviving conclusion, not infer degeneracy or an RH counterexample.

Essential input IDs: L759 (no local lemma inputs), the cited source
matrix formulas and standard Euler--Maclaurin/Sylvester results.
Unresolved independent gaps remain general simplicity/parity, both
boundary-normalized limits, ground-eigenfunction approximation and Xi
transfer. No covered quantitative eigenfunction mechanism currently
justifies relabeling this reproduction or its audit as creative work.
Mathlib coverage remains unchecked.
