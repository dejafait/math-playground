# Finite Mellin saddle local-phase comparison: nominated audit

TARGET: Audit paper23 v1's local phase bound 1.1/Q on its finite descent diameter throughout (10), with L797, using the normalized truncated-Gaussian comparison specified in the assessment.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step511's completed remainder source review checked the exact paper23 claim, primary saddle hypotheses and relevant local/global proof cases, and the named local overlap/failure records. No matching completed local audit was located in that scope; no novelty inference.
SOURCE_EVIDENCE: paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23; O'Sullivan PJM298(2019), Assumptions1.1/Theorem1.2 pp159–160, Corollary5.1/proof pp175–176, https://msp.org/pjm/2019/298-1/pjm-v298-n1-p08-s.pdf; DLMF2.4(iii)–(iv), https://dlmf.nist.gov/2.4#iv; localization evidence reused from 2026-11-05-actual-mellin-remainder-source-scope.md.
COMPARISON: The source asserts a relative local phase cost <=1.1/Q using symmetric cubic cancellation, quartic and squared-cubic errors. The finite integral below makes the audit normalization explicit; general fixed-data saddle theorems do not verify its parameter-uniform constant. Reproduction is justified by the unverified numerical premise and inaccessible detailed derivation.
GAP: Prove or rigorously fail the specified finite-integral inequality on the whole closed complex domain. The source's derivative bounds and real decrement are audit obligations, not assumptions. No full Mellin estimate or global-contour assertion is approved.
REASON: A bounded independent local test uses only the explicit elementary phase and audited L797, without continued Mellin endpoints, theta evaluators or supplementary inputs. Success verifies one local error budget; failure isolates a precise source premise without claiming a disproof of RH.
SCOPE: Separately reviewed and approved in step512 for exactly the saved finite-integral audit; SPECIALIZE permits REPRODUCTION. Neither source review evaluates or proves the inequality. No global estimate or central creative-sign claim is covered.

## Explicit test specification

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
verify one local remainder cost behind paper23's proposed actual Mellin
quotient. Downstream use is one component of (11), then separately
assessed quotient/inversion control. Amplitude, full-contour errors,
certificates and a sufficient sign mechanism remain independent gaps.

For every s in

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},

use L797's x(s)=u+ih and A=2F'(x)/x, where

    F(z)=z(pi exp(2z)-9/4),
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z),
    Q=pi exp(2u), d=3/(16u), theta=Arg A,
    a=exp(-i theta/2).

All logarithms and square roots are principal. The proposed audit is
the following explicit reading of the source's relative local-phase
budget, with the omitted Gaussian tail kept separate:

    J(s)=a integral[-d,d] exp(S_s(x+av)-S_s(x)) dv,
    G(s)=a integral[-d,d] exp(-|A|v^2/2) dv,
    |J(s)-G(s)| / |sqrt(2pi/A)| <= 1.1/Q.             (local test)

These definitions and the inequality are a test nomination, not a
derived lemma or an assertion that the source explicitly printed this
integral formula. It operationalizes the printed local-phase term;
any discrepancy in the interpretation must be reported before calling
the source claim verified. Do not silently include amplitude errors
or replace the finite Gaussian with its full integral in the numerator.
The source budgets the omitted Gaussian separately in (14).

## Hypotheses, review scope and decisive evidence

Essential mathematical input is L797's audited inverse, branch,
curvature and full-domain coverage; the phase and constants above are
definitions. The source claims |S_s'''|<=10Q and |S_s''''|<=19Q on
the closed radius-d saddle disc, and real quadratic decrement at least
1.54Qv^2. A later audit must justify every auxiliary bound it uses, or
replace it with a proved usable estimate; it must not assume these
unreviewed source claims and then call their conclusion unconditional.
Prove analytic admissibility and all denominator/branch cases needed
for the test, and retain |s|=6000, curved-boundary and conjugate cases.
Do not infer global contour validity from an admissible local disc.

The reviewed primary method coverage is the opposite-sector cancellation
and explicit local remainder control in O'Sullivan Corollary5.1 and
its localization/Cauchy proof, and DLMF2.4(iii)–(iv)'s branch/geometric
hypotheses. This authorizes reproducing and bounding a source claim,
not importing an unproved uniform error constant. Full precise citations,
read proof cases and unread leads remain in the completed source review.
No new asymptotic theorem is needed merely to formulate this finite
integral. Standard Taylor remainder and Gaussian moment facts used in
a later proof must be stated with their actual hypotheses.

Continue with an analytic proof or a rigorous counterexample on D.
A weaker constant must be compared explicitly with 1.1 and the full
4.5 budget; it does not verify the nominated claim. If one turn leaves
a bound unpaid, save the exact missing inequality and partial reasoning;
do not repeat without a refined mechanism or new input. A finite
numerical grid is only a diagnostic and no script is required. The
global endpoint/tail route is parked and not an input to this test.

L019/L021 establish actual-kernel relevance/normalization only. L795/L796
and the step507/508 representation stops are context, not dependencies.
No cross-notebook theorem, finite enclosure data, Mathlib matching
theorem or sufficient Xi sign result is assumed. Full Mathlib coverage
remains unchecked. This established-route local audit cannot be
reclassified as creative to meet a scheduling preference.

## Separate approval and direct-source repair — step512

On 5 November 2026, reopened the direct primary URLs above to repair
source provenance, not to seek another saddle theorem. Reused step511's
search, overlap/failure comparison and localization proof-case assessment.
The research target, domain, normalization and unpaid bounds are unchanged.

[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
Section3 Lemma2, paragraph between (13) and (14), confirms the finite
diameter and the asserted local cost. It separately assigns an omitted
Gaussian term in (14). The source does not print J and G in this
assessment's form: this is an explicit operational audit, not a quotation
of a theorem. A successful test would verify this reading only.

[O'Sullivan's published text](https://msp.org/pjm/2019/298-1/pjm-v298-n1-p08-s.pdf),
Assumptions1.1/Theorem1.2 pp159–160 and Corollary5.1/proof pp175–176,
were directly checked. The hypotheses fix phase and geometry independently
of N, require holomorphy and strict real-phase domination, and use even
saddle order and opposite sectors for cancellation. The error constant is
independent of N and amplitude, with no claimed independence from phase
or geometry. The proof cancels odd indices; it does not supply 1.1 here.
[DLMF2.4(iv)](https://dlmf.nist.gov/2.4#iv), (2.4.14)–(2.4.15),
likewise treats branches and an asymptotic expansion, not this effective
uniform bound. No theorem is imported to discharge the audit obligation.

Approval: SPECIALIZE is adequate for a direct reproduction audit with
all auxiliary bounds proved independently. No essential source blocker
remains for this finite test. Missing global supplements remain outside
scope. Matching Mathlib coverage is unchecked. This is a provenance and
gate repair, not new mathematical evidence or a renewed exploration budget.
