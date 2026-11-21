# C750i inverse-certificate audit — source approval1145

TARGET: Audit C750i's whole-line inverse-certificate obstruction, checking the complex supported-form relaxation, both collar blocks, complete frequency/kernel errors and directed numerical lower bound against the fixed one-eighth threshold.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused assessment1142/review1143 and assessment1140; targeted local prime97 literature/history/stop search found the recorded sufficient-test failure, not a supported counterexample. Opened NIST DLMF3.5(ii) and MPFR4.2.2 rounding/conversion documentation to close the numerical-input coverage gap.
SOURCE_EVIDENCE: Reuse inspected Teschl GSM99 Lemma0.32/proof pp28-29, Theorem2.13/proof pp71-72, Theorems3.1-3.2/proofs and domain(3.25) pp90-92; newly read DLMF3.5(ii), equations3.5.6-3.5.8 with hypotheses, and MPFR4.2.2 Sections4.4/5.4 rounding and mpfr_get_str semantics.
COMPARISON: Standard functional calculus, Schur and composite Simpson inputs cover the audit techniques; they do not certify the local form specialization, derivative majorant, code or numerical endpoints. No theorem proves the fixed obstruction or original supported inequality merely by citation.
GAP: Essential source coverage for the exact bounded audit is ready; independent verification of C750i and its complete directed certificate is still unfinished. The original supported allocation and all actual-Xi transfer gaps remain open.
REASON: Approve the saved correctness-audit scope after checking its new numerical source obligations; no new lemma, certificate replay or mathematical result is supplied in this literature turn.

The canonical result is lemmas/C750i-whole-line-collar-inverse-certificate-stop.md.
The exact constants and domain remain a=9/4, b=log101/2,
r=(a/b)log97, w=2a-r, k=2log97/sqrt97, complex D_a with finite J.
No cross-notebook theorem is needed. The complete evidence is
scripts/prime-collar/certificate-1144.json and certify_1144.py, using
unchanged scripts/pivot-area/certify_1136.py. The initial nonessential
upper<1 failure is preserved in certificate-1144-initial.json.

The proposed audit should test whether ||B||>1/(4k) was proved for
B=R_E M^(-1)R_E*, while keeping the original supported inequality
unresolved. Check the exact sufficient reduction, closed complex form,
Schur treatment of both blocks, full frequency tail, uniform kernel
quadrature error, normalized single-collar inverse test, removable zero,
Simpson derivative majorant and outward rounding. Review the complete
selected load-bearing certificate values and implementation, not a JSON
preview or rounded eigenvalue. Do not add a witness search, tune the mesh,
or derive a new inequality in the audit. A real gap requires preserving
the attempted negative result with its precise qualification.

Potential downstream use is reliable abandonment of this sufficient
relaxation and preservation of the original allocation for a materially
different test. The negative result does not reopen the completed pulse
search or establish actual-Xi positivity. No central creative mechanism
is nominated merely to fill a scheduling preference; the current evidence
concerns one auxiliary budget term. Discovery of a central mechanism
remains a later selection problem, not mathematics approved by this file.

## Source approval1145 — 16 November2026

LITERATURE_REASON: The gate was REVIEW_REQUIRED for a newly written
result. Its specific previously unread essential inputs were Simpson's
rigorous remainder and the MPFR arithmetic/output contract. The earlier
operator and domain assessments are adequate for this unchanged target
and are reused, rather than searched again.

SCOPE: Only the exact TARGET above, with the unchanged a,b,r,w,k and
complex finite-J domain in C750i. Permitted later work is correctness
review and replay of its existing fixed-grid certificate, including all
errors and retained failures. No mesh tuning, new supported witness,
stronger allocation or new operator inequality is covered.

### New primary source evidence

NIST, *Digital Library of Mathematical Functions*, Section3.5(ii),
[Simpson's rule](https://dlmf.nist.gov/3.5.ii), accessed16November2026,
equations3.5.6-3.5.8 and surrounding hypotheses: the integrand is in
C^4[a,b]; the composite rule has h=(b-a)/n with n even, and error
-(b-a)h^4 f^(4)(xi)/180 for an interior xi. The elementary rule's
remainder is also displayed in3.5.6. Thus the cited numerical theorem
matches the type of error formula used by C750i, provided its integrand
including the removable zero has the required regularity and its
claimed global fourth-derivative majorant is valid. Those are local
audit obligations, not established here. No reproof of Simpson's rule
is needed. This source supplies no evaluation of the inverse norm.

GNU MPFR, *MPFR4.2.2 Manual*,
[Section4.4 Rounding](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Rounding)
and [Section5.4 Conversion Functions](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Conversion-Functions),
accessed16November2026: RNDD/RNDU round toward negative/positive
infinity. The documented operations treat inputs as exact and return
correctly rounded results. The mpfr_get_str entry explicitly accepts a
rounding direction for conversion to significant digits. These contracts
support outward arithmetic and output; they do not verify ctypes ABI,
rounding-mode constants, interval formulas, trig enclosure, decimal
assembly or script hashes. Those remain implementation checks. No
machine-arithmetic proof or numerical replay was performed here.

### Reused inputs and theorem-scope comparison

Assessment1142/review1143 records the actual primary readings and
proof cases for Teschl's closed-form theorem, bounded and unbounded
functional calculus, and Schur's criterion. Their hypotheses remain
appropriate audit inputs: dense closed semibounded form; spectral
square-integrability domain; bounded measurable multiplier; measurable
kernel with both row and column integrability controls. The audit must
check each specialization rather than simply cite these abstract
statements. C750i uses the whole-line inverse, not an equality between
compression and inversion. The bounded Jensen and point-spectrum
Birman-Schwinger readings from review1143 remain contrasts, not
additional required premises. The unbounded complex form is not
covered by merely quoting the real bounded variational formula.

Read C750i in full to inventory its source needs, and read its stop note
and review1143 history. Targeted prime97 searches identify the existing
pulse test and inverse-certificate stop; neither is a proof of the
original supported allocation's failure. The displayed grid/derivative
code and backend symbol search were inspected only to identify which
source contracts the audit needs, not to certify implementation. No
certificate endpoint was accepted on the basis of a preview. Reuse
assessment1140's domain/normalization comparison; no new prime
activation, zero-free region or reciprocal-continuation target is
introduced, so the separate October quasi-RH baseline is not invoked.
No cross-notebook theorem is used. Full matching Mathlib coverage
remains unchecked, as in C750i; no absence or formal verification is
claimed.

### Bounded later audit and decision test

The exact TARGET is now source-covered under SPECIALIZE. The later
audit is REPRODUCTION, not a new mathematical discovery. Check the
complex form domain and support closure, normalization and factor1/2,
bounded restriction/adjoint maps, both collar blocks, full frequency
remainder, uniform kernel error, unit-test normalization, removable
zero and derivative majorant. Inspect every load-bearing directed
endpoint in full and replay the fixed certificate with hashes/backend
review. Retain both failed allocation and nonessential upper<1 tests.

Continue to treat the sufficient certificate as stopped only if the
verified lower endpoint exceeds the verified 1/(4k) upper endpoint;
C750i claims >0.29256024 versus <0.26911148. A failed essential
hypothesis, normalization or rounding check requires preserving and
qualifying the result, not calling it audited. This does not test an
admissible supported violating witness. Its downstream use is reliable
abandonment of this relaxation; J-to-baseline, other budget terms,
both sectors, all supports and actual-Xi positivity remain independent.

No new central creative mechanism follows from this auxiliary source
approval. Selecting one requires a separate justified central target;
the pending essential audit takes priority without relabeling it.
