# Fixed shifted sinc model: source-covered specialization2244

TARGET: Test whether the fixed G(z)=(2+cos z)/3 times product_{j>=1}sinc(z/(j+sqrt(2))) and every finite increasing real-zero-prefix quotient have smooth strictly positive probability inverses, all exponential derivative tails, a prefix-uniform finite second moment, simple real zeros, a retained nonreal zero and exact order one.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches and selected local duplicate/failure checks completed in review2244; exact queries and outcomes are recorded in drafts/literature/2026-11-21-shifted-sinc-source-notes-2244.md. No full matching shifted-prefix theorem was located; no claim of novelty or nonexistence.
SOURCE_EVIDENCE: Durrett PTE version5 Theorems2.5.6 and3.3.14 with proofs https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf ; Schmuland2003 sections2,4-5 https://web.williams.edu/Mathematics/sjmiller/public_html/105Sp11/addcomments/Schmuland_RandomHarmonicSeries.pdf ; Hoeffding UNC Mimeo326 (May1962) Theorem2 and (3.11)-(3.17) https://repository.lib.ncsu.edu/bitstreams/d0e6ed15-3e1c-432f-8419-e55ffb6f3171/download ; DLMF1.10(ix) M-test/nonvanishing https://dlmf.nist.gov/1.10.ix ; Eremenko2015 p2 order definition https://www.math.purdue.edu/~eremenko/dvi/legendre2new.pdf ; C919p finite identities (8)-(10) and unchanged source notes2239. Precise citations and hypotheses are in source notes2244; URL/access repair2245 below.
COMPARISON: Infinite-uniform smoothing and finite cosine-power removal are standard source-covered tools. Neither the different-width Schmuland law nor C919p's Gaussian model supplies this fixed G's every-prefix statement, strictness, all derivative tails, moment bound and exact order. Csordas's correlation-kernel criterion remains a different assertion.
GAP: Verify all model-specific convergence, support, derivative and growth estimates, ordered within-factor grouping and removable values; give one explicit moment bound uniform in the prefix and retain the nominated nonreal zero. No conclusion about G has been established by the source review.
REASON: A single coherent known-method specialization can test whether order one repairs the generic bridge left open by C919p; the ordinary tools are covered and need not be reproved. Actual-Xi mixed positivity remains independent.
SCOPE: One fixed G, sinc(w)=sin(w)/w with value1 at0, angular Fourier convention T(f)(z)=integral f(u)exp(izu)du, every integer prefix N>=0 of the candidate positive real roots {pi*k*(j+sqrt(2)):j,k>=1}, all integers m,p>=0 and B>=0; no parameter changes, finite-type requirement, Xi transfer or central creative claim.

## Exact obligations for the later attempt

Use R_N and the candidate root enumeration of nomination2243. First
justify that the product and enumeration exist and have the stated
exhaustive simple roots. For every finite N require removable G/R_N
and a smooth even probability inverse f_N strictly positive everywhere.
The tails sought are, for every m,p>=0 and B>=0,

    integral (1+|u|)^p exp(B|u|)|f_N^(m)(u)|du < infinity,
    exp(B|u|)f_N^(m)(u) -> 0 as u -> +/-infinity.

Require a single explicit finite upper bound for all second moments,
the retained simple zero `pi+i log(2+sqrt(3))`, and order exactly one
for every quotient, with both upper and lower growth bounds. The
constants in derivative estimates may depend on N,m,p,B. The moment
bound alone must be independent of N. No positive-density limit,
derivative-tail estimate or growth estimate is proved here.

Import Durrett's convergence/inversion, Hoeffding's bounded-variable
input and the analytic-product theorem. Reuse C919p's normalized compact
identity after proving its scaled applicability. Schmuland's finite-head
method is a reproduction guide; its distinct widths prevent verbatim
import of the full conclusion. Justify every interchange at the
infinite limit and the global ordered prefix's finite regrouping.
Full matching Mathlib coverage remains unchecked.

Continue only if all obligations hold for this single fixed function
and every finite prefix. A contradicted requirement abandons this
candidate, while a failed bound alone is inconclusive and must be saved.
If the assembled proof is incomplete, preserve it without inventing
a lemma conclusion or changing the model. Success would delimit a
generic order-one sufficiency assertion, not prove RH. Classify the
attempt as REPRODUCTION, without a novelty claim.

This continuation is newly written in literature turn2244 and requires
the supervisor's separate next-turn approval before mathematical work.

## Source URL recovery2245

21 November2026: supplied recovery gate required a direct source URL in
the ready assessment itself. Added the existing primary URLs to the
single-line SOURCE_EVIDENCE field; TARGET, scope and SPECIALIZE decision
are unchanged. This separate literature turn approves reuse of the2244
coverage for the exact saved target, subject to supervisor validation.
No new model mathematics or theorem-level coverage is claimed.

Reopened the linked Duke version5 PDF, DLMF infinite-product section,
Schmuland manuscript and Eremenko manuscript; their identities resolve.
Located Durrett's cited theorem numbers and DLMF's M-test conclusion.
The NCSU URL currently returns a bot-detection page, not the manuscript.
Reuse the previously inspected Theorem2/proof extraction in source
notes2244, including its transcription qualification; do not describe
the current response as a fresh proof inspection. No changed hypothesis
requires replacing that prior coverage. A future need for additional
Hoeffding text would require fresh access, but none is introduced here.

The source notes' duplicate/failure comparison remains applicable:
different widths in Schmuland and the order-two stop2241 do not settle
this fixed order-one target. All strictness, derivative, moment, root
and growth obligations above remain unproved. This is a process repair,
not a mathematical advance or an informative negative result.
