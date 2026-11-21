# Approved separate audit of the Riccati growth stop1956

TARGET: Independently audit C029d's Riccati spectral enclosure, complete Frobenius/trace bound, explicit onset and height-majorant qualification, repairing any failed claim.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment1954 and source-notes1954's exact Riccati/Jensen/companion, quantitative-bound and Frobenius/trace searches and recorded duplicate/failure comparisons. This continuation only audits the resulting C029d specialization; no new theorem search or novelty inference is claimed.
SOURCE_EVIDENCE: Reuse Wimmer1976 Theorems2-3 and full proofs pp459-461, equation/sign conventions pp457-459 https://doi.org/10.1017/S0004972700025387 ; Watrous2018 Section1.1 (1.165)-(1.181), pp32-34 https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf ; Schmeisser2002 Lemma1 pp211-212 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf . Inspection and precise applicability are recorded in source-notes1954/1523/1947 and reused unchanged, not represented as new source inspection in step1956.
COMPARISON: The standard inputs supply finite positive stabilizing existence, compatible Schatten inequalities and the eigenvalue-height majorant. C029d adds the scalar Riccati enclosure and actual complete-companion Frobenius/trace specialization; their signs, constants and logical direction still require an independent audit.
GAP: Audit the existing finite proof, especially eigenvectors of X rather than M, principal-block bounds, the squared similarity factor, both ordered trace contributions, positive part, onset and the fact that a growing upper majorant says nothing against RH. No new metric or bound is authorized.
REASON: Separate literature-only review1957 approves this exact audit under unchanged SPECIALIZE coverage after reading C029d and the reused source evidence. No essential source gap was found; the mathematical audit itself has not occurred.
SCOPE: Only audit and necessary repair/retraction of C029d for actual C029b matrices, all integer d>=3, exactly identity state cost and its upper-left principal block. New costs, parameter schedules, horizons and positive-payment mechanisms remain outside scope.

## Audit target and standard hypotheses

Read the complete canonical C029d proof. C029b supplies the actual
centered companion, finite entire coefficient bound and degree scale;
C028b supplies the relevance of H_d=o(d). Reuse their already recorded
source coverage without reopening the finite-horizon endpoint attempt.

Wimmer's coefficient signs, real symmetry and full-rank controllability
and observability follow from (A_0,B_0,C_0)=(I,M_d,-I); no root
premise or Hamiltonian diagonalization may be assumed. The enclosure
uses eigenvectors of the symmetric positive X, for which scalar
compression is legitimate even though M_d is nonnormal. Watrous's
p=2 ideal inequality must be applied to reconstruct C from B; the
resulting squared lower factor is a^2, with a*u=1. Schmeisser's bound
uses all roots with algebraic multiplicity and an unnormalized trace
norm, with division by d from the normalized companion.

The exact claimed cost bound is

    (k_d^R)^2 >= max{0,[a^2(d-1)+(1-1/d)(b_2-b_1^2)]/2},
    a=sqrt(1+A^2)-A, A=exp(b_1)F(1).

Check all d>=3, including possibly negative inner expressions at small
d. Check the explicit sufficient onset and lower-limit conclusion.
No numerical replay is needed for these exact finite identities. The
audit must repair or retract a failure, rather than merely repeat the
recorded stop. A successful audit verifies a local metric obstruction,
not a complete RH candidate or certified novelty. Full Mathlib coverage
is unchecked. Separate literature-only review1957 approves the assessment for the
exact saved audit target; completed step1956 remains a research
calculation under the preexisting assessment1954. Approval establishes
source readiness, not correctness of C029d.


## Separate source-scope approval1957

2026-11-20. Read the complete C029d solely to inventory its imported
inputs and proposed audit obligations, not to execute the proof audit.
Read assessment1954 and source-notes1954 completely, source-notes1523
through its Schmeisser/companion/Watrous coverage, source-notes1947's
reuse/comparison section, C029b's exact definitions and conclusions,
and the stop/history1956. The supplied overview and DAG were used
before these detailed reads. No new external retrieval or search is
represented as having occurred; adequate primary coverage and the
recorded exact-query/duplicate/failure assessment are reused.

Wimmer's equation convention and hypotheses are explicitly recorded
in source-notes1954: real symmetric state coefficient nonnegative,
quadratic coefficient nonpositive, controllability and observability.
C029d cites that unrestricted result with identity input/output rather
than importing the diagonalizable-Hamiltonian convention in Kucera.
The audit must check this substitution against the recorded source,
but needs no theorem about the actual companion spectrum. The
unread quantitative Riccati bounds listed in source-notes1954 are
not essential: the audit concerns an existing scalar argument, not
an import from those leads. No new quantitative theorem is approved.

Watrous's compatible finite-dimensional ideal inequality covers p=2
and complex matrices, as well as the trace/Frobenius comparison.
Schmeisser Lemma1 covers arbitrary complex square matrices with all
algebraic multiplicities and no normality or simplicity premise. Its
Gohberg--Krein proof reference remains not independently read; import
is through the inspected primary lemma, not a claimed book inspection.
The source does not assert decay of this particular metric cost.
C029b's normalization and C028b's criterion remain local inputs whose
precise use and direction are mathematical audit obligations.

The proposed audit therefore stays within already assessed techniques
and assumptions. The general existence and norm results should be
imported by citation; checking the actual coefficients, spectral
compression, similarity factor, square trace, positive part and onset
is necessary specialization verification, not reproof of those sources.
The earlier diagonal/shear, theta-metric and finite-horizon stops are
contrasts under assessment1954; they neither replace this audit nor
become additional mathematical premises. No broader claim of novelty
or exclusion of other metrics is supported by this source review.

Decision: SPECIALIZE, ready for the exact TARGET above. A successful
audit sustains this metric's decay stop; a failure requires repair or
retraction of the offending claim. Neither outcome by itself settles
actual root height or RH. New costs, horizons and alternative metrics
remain uncovered targets requiring REVIEW_REQUIRED before research.
Full Mathlib matching coverage is unchecked. This approval repeats
no mathematical calculation and adds no new source theorem or overlap
finding, so review1957 is honestly STALLED rather than a mathematical
advance. The required audit has priority over preparing an unsupported
creative mechanism; no independent positive-payment target has yet
been justified by this bounded approval step.
