# Archimedean pointwise source audit — nomination1186

TARGET: Audit Polson v24 Lemma 6.1's bounds m(r)>=-6 for all real r and m(r)>1 for |r|>=20, including the series and Binet constants used by C030e.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Approval1187 reused comparisons1183/1185 and searched active-notebook lemmas/assessments/attempts/history for the exact bounds, Binet and digamma; inspected L744(8)'s stronger tail estimate and the distinct L516/step310 uses. External queries were "1708.02653" "m(r)" "6.1" and "digamma" "1/4" "Binet" lower bound. No exact independent source-proof audit was found; no novelty inferred.
SOURCE_EVIDENCE: Rechecked Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24, 11 September2026, https://arxiv.org/pdf/1708.02653v24#page=11, complete Lemma6.1 statement/proof printed pp11-12; directly inspected NIST DLMF5.7.6,5.9.15 with Re(z)>0,5.4.19,25.5.1 with Re(s)>1,25.6.1 and5.11(ii)'s complex remainder paragraph on2026-11-16. Exact links and obligations below.
COMPARISON: Both desired conclusions are already Polson Lemma6.1; L744(8) also records a stronger asymptotic error, but not the source's exact Binet constants or global lower bound audit. C030d/e leave this input imported. A reliability reproduction is justified for this load-bearing import; importing the statement alone would not complete the requested proof audit.
GAP: Essential source coverage is ready; series real-part subtraction/convergence, evenness, the value at zero, uniform Binet split and strict scalar margins remain mathematical audit obligations. No bound is independently certified by this approval; the explicit formula and heat-series inputs remain imports.
REASON: Separate literature approval1187 covers the unchanged saved target and all necessary proof cases, permitting one REPRODUCTION audit next. Reuse existing stronger tail coverage where relevant; no full-paper review, unrelated head-integral audit, novel estimate or RH inference is authorized.
LITERATURE_REASON: Changed scope from assembly with Lemma6.1 imported to independent certification of its two pointwise estimates and the constants needed for them; prior ready coverage excludes this work.
SCOPE: Only m(r)=Re psi(1/4+ir/2)-log(pi), the bounds m>=-6 on R and m>1 for |r|>=20, and their necessary series/Binet steps. No full-paper audit, far-time estimates, source-program replay, heat transfer or all-degree sign inference.

This nomination follows the completed mathematical audit1186 and does
not approve or derive new mathematics. Read the complete relevant
primary proof cases and any essential supporting theorem hypotheses;
reuse accessible statements from comparisons1183/1185. Verify that no
earlier independent audit already covers these exact pointwise bounds.
The remaining two imports in C030e, the Section4.3 explicit formula
and the convergence/differentiation portion of Lemma5.2, stay external.

The bounded mathematical exit test, only after approval, is a complete
check of the all-real lower bound and the strict tail threshold at20,
including negative r and boundary points, or one isolated failed
constant or missing hypothesis. Necessary intermediate estimates may
be audited only within the separately approved scope. A successful
audit would remove one local source-proof qualification; it would
not supply an actual-Xi all-degree sign or a new result beyond the
source. C030e motivates its use and is not a premise proving m's signs.

There is no newly justified creative mechanism. The norm bounds in
C030d/C030e do not identify an arithmetic sign/coercivity estimate;
completed discovery1121 already found the arithmetic-to-square bridge
unpaid. Do not repeat that generic three-route discovery or the
completed C030c finite-surgery calibration merely to fill a scheduling
target. Stops1117/1181 retain their scopes. A creative continuation
needs a materially new signed input and a discriminating bounded test.
Full matching Mathlib coverage remains unchecked. No cross-notebook
input is proposed.

## Separate coverage approval1187 — 16 November 2026

The nomination above is retained as the record of why a separate gate
was required. This section completes coverage for its unchanged TARGET;
it gives no independent pass verdict on the estimates.

### Relevance and duplicate comparison

The main gap remains L030-L032/C032a actual-Xi all-polynomial
positivity. C030e uses precisely the two proposed pointwise bounds in
its near-zero assembly; C030d concerns Gaussian polynomials only.
Assessments1182/1184 and history1186 explicitly excluded this proof
audit. The downstream use is removing one source-proof qualification
from C030e, with the explicit formula, heat convergence, far-time,
all-degree, theta-sign and realization gaps still independent.

The targeted local search found L744, proof section2/(8), which already
records |m(xi)-log(|xi|/(2pi))|<=2/xi^2 for |xi|>=1 using the complex
DLMF remainder. Reuse this stronger tail control as an existing input
or cross-check, rather than present another asymptotic estimate as new.
It does not check the exact Binet proof requested here. L516 gives a
complete-form identity; step310's archimedean-payment assessment asks
a different operator inequality. The older history search hit L245's
unrelated tilted completed-zeta quantity, not these scalar bounds.
The checked near-zero histories and assessments contain no earlier
independent audit of the exact constants. Stops1117/1181 concern
finite-extension/class bridges, not this independently testable input;
they remain preserved. No failed mathematical audit is alleged.

### Inspected primary inputs and permitted specialization

- [DLMF5.7.6](https://dlmf.nist.gov/5.7.E6) gives the digamma
  partial-fraction series away from nonpositive integer poles.
  It covers z=1/4+ir/2 and z=1/4. Subtracting the paired series,
  taking real parts, convergence, and the resulting monotonicity
  are obligations for the audit, not conclusions of this review.
- [DLMF5.4.19](https://dlmf.nist.gov/5.4.E19), Gauss's digamma
  theorem, assumes integers 0<p<q. The source's value at1/4 is
  covered by p=1,q=4; retain the -log(pi) in m(0). Simplification
  and its numerical lower margin must be checked next turn.
- [DLMF5.9.15](https://dlmf.nist.gov/5.9.E15) supplies the exact
  differentiated Binet integral for Re(z)>0 with principal log.
  The entire proposed vertical line satisfies this domain. Its
  denominator can approach its smallest modulus near u=|r|/2;
  a real-positive-z denominator bound cannot be imported there.
  Check both pieces of the source split explicitly.
- [DLMF25.5.1](https://dlmf.nist.gov/25.5.E1) assumes Re(s)>1;
  [DLMF25.6.1](https://dlmf.nist.gov/25.6.E1) supplies zeta(2).
  These cover the Bose integral normalization used in the small-u
  Binet estimate, with s=2 and the source's rescaling. The value
  1/24 and that rescaling are still audit obligations.
- [DLMF5.11.2/5.11(ii)](https://dlmf.nist.gov/5.11#ii) gives the
  finite complex remainder bound, not merely an asymptotic series:
  the first omitted term is multiplied by sec(arg(z)/2)^(2n+1).
  This is the known input used by L744(8), not a new derivation here.

These DLMF pages were directly inspected on2026-11-16; the reused
version identification is1.2.8,15September2026 (assessment1136).
The TeX endpoints rejected the web reader; the accessible HTML formula
pages and their hypothesis paragraphs supplied the required evidence,
so this is not a source blocker. No numerical source program was run.

### Complete source cases and bounded exit test

[Polson v24 Lemma6.1, printed pp11-12](https://arxiv.org/pdf/1708.02653v24#page=11)
states the two requested bounds and gives a series/Binet proof.
Its proof uses monotonicity and m(0)=-gamma-pi/2-3log(2)-log(pi).
For r>=20 it compares m(r) with log(r/(2pi)). The displayed correction
budgets are1/3200 and2/1601. The Binet split is at u=r/4: the
first denominator bound is(3r^2-1)/16>=74, yielding1/888; the second
uses Im(u^2+z^2)=r/4 and an exponential tail bounded by

    (2/5)*exp(-10pi)/(1-exp(-10pi))*(5/(2pi)+1/(4pi^2)) < 10^-11.

The source totals these with error<0.003 and obtains1<m(20)<2.
The later head-integral bound136 is unnecessary for the saved target
and is outside this audit. All these are reported source obligations,
not independently reproduced inequalities in this literature turn.

The next audit must check every needed constant uniformly, justify
evenness/negative r and include r=0 and |r|=20. Continue only upon a
complete proof of the saved two bounds; otherwise isolate the precise
failed estimate or missing hypothesis and its effect on C030e. Do not
silently substitute a passing floating-point sample or a successful
L744 cross-check for validation of the requested source argument.

The external exact-statement query returned no adequate independent
audit. The broader query also surfaced Cryptids' DigammaBinet formal
development and a2022 Binet paper; these are unread leads, not imported
theorems or Mathlib coverage evidence. DLMF and the complete primary
proof already cover the needed scope. Full matching Mathlib coverage
is unchecked; supporting analytic formulas are not such a match.

Decision: SPECIALIZE, ready for one subsequent REPRODUCTION audit of
the exact TARGET. Outcome of this source review: EXPLORATION,
LITERATURE/NOVELTY_UNCHECKED. No lemma, mathematical script, new
estimate, or source-program replay was produced. No creative central
sign mechanism is justified by these scalar norms; discovery1121's
unpaid arithmetic-to-square bridge remains the blocker to that route.
