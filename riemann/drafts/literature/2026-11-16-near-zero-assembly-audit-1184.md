# Near-zero assembly audit — nomination1184

TARGET: Audit Polson v24 Lemma 7.7 equation (26), including eta_N(1/(4000000N))>0.7 for all N>=1 and eta_3(10^-6)>1/4, using C030d and explicitly importing Lemma 6.1 and the Section 4.3 explicit formula.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Approval1185 reuses comparison1183 in drafts/literature/2026-11-16-near-zero-source-proof-scope-1182.md and its exact-phrase/overlap searches; narrowly checked coverage1113/1114, histories1183/1184, C030d and stops1117/1181. No repeated external discovery search or originality claim.
SOURCE_EVIDENCE: Direct primary PDF text rechecked in approval1185: Nicholas G. Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24, 11 September2026, https://arxiv.org/pdf/1708.02653v24, Section4.3/(3) p8, Definition5.1/(4) p8 and Lemma5.2 convergence/differentiation p9, Lemma6.1 statement/full proof pp11-12, Section7.3/(21)-(22) pp18-19 and Lemma7.7/(26)/entire proof pp19-20. C030d independently audits only Lemma7.6/(23)-(25).
COMPARISON: The exact lower bound and both margins are already stated and proved in the cited preprint; prior finite application1116/1182 and Gaussian audit1184 do not independently check the assembly. Reproduction is justified by reliability of this load-bearing source input, not novelty or a larger finite/all-degree conclusion.
GAP: Coverage is complete for one bounded assembly audit; checking the test hypotheses, normalization, three error estimates, monotonicity and strict scalar margins remains mathematical work. Lemma6.1, equation(3) and the convergence/differentiation portion of Lemma5.2 remain explicit external imports; no source-access blocker remains.
REASON: Separate approval1185 confirms the unchanged saved target has accessible complete proof cases and precisely identified imports. Reuse this assessment for the next mathematical turn; this literature-only approval supplies no pass verdict or new mathematical result.
LITERATURE_REASON: The supervisor requires separate approval of nomination1184; its full assembly scope exceeds the prior Gaussian-only assessment. Reuse comparison1183 and inspect only the necessary source interfaces and margin cases.
SCOPE: Exactly one Lemma7.7/(26) assembly audit for N>=1, epsilon in{0,1}, real deg(p)<=N-1, q(x)=x^epsilon p(x^2), 0<t<=log(2)/180, including monotonicity and both stated margins; reuse C030d and explicitly import the source inputs identified below. No independent Lemma6.1/explicit-formula proof, full-paper certification, far-time audit, source-script replay, cap extension or all-degree sign claim.

The proposed mathematical domain is N an integer>=1, epsilon in{0,1},
p a real polynomial of degree<=N-1, q(x)=x^epsilon p(x^2), and
0<t<=log(2)/180. Retain the source's unnormalized Gaussian norm,
definition(22) of Q_N,t^epsilon and algebraic square convention.
The complete extracted eta_N formula and source cases are in completed
comparison1183 in the assessment cited above; do not infer them from a
numerical preview. C030d supplies(23)-(25) but no zeta identity.

Essential inputs for any subsequent proof are C030d, Polson Lemma6.1
(the pointwise lower bounds for m), and the Section4.3 explicit formula
with its Fourier normalization and analytic-strip/decay hypotheses.
The latter two remain named imports; verify their applicability, without
silently presenting them as independently audited. C030a/C030b and L030
motivate the downstream use and need no repeated application audit.

The bounded test, once approved, is to justify every term of(26) and
both strict scalar margins throughout the stated domain, or isolate a
specific failed estimate or missing hypothesis. A pass would validate
this source assembly relative to the named imports only. The actual-Xi
all-degree gap, far-time validation, theta signs and graph realization
remain unresolved. The finite-only stop1117 and class-bridge stop1181
retain their original scopes; neither is reopened here.

No justified creative central mechanism follows from the norm bounds
alone: an actual arithmetic sign/coercivity input is still unspecified.
This nomination is routine source validation planning, not a creative
attempt manufactured to satisfy a scheduling target. Mathlib coverage
for the full assembly is unchecked. There is no cross-notebook input.

## Separate coverage approval1185 — 16 November 2026

The preceding nomination records why a separate gate was needed. This
section completes that gate for the unchanged TARGET. It approves only
the ensuing proof audit, not the inequalities under audit. The exact
eta_N formula and source error thresholds remain in comparison1183;
they need not be copied or independently established in this source review.

### Imported hypotheses and normalization

The primary statement is [Polson v24, Section4.3, equation(3), printed
p8](https://arxiv.org/pdf/1708.02653v24#page=8). It assumes an even h,
holomorphic in the closed strip |Im(r)|<=1/2+delta for some delta>0,
with h(r)=O((1+|r|)^(-2-delta)) there. Use a neighborhood of the closed
strip to avoid a boundary interpretation issue. The proposed audit must
verify these conditions for its fixed polynomial and fixed positive t;
it must not assume a uniform decay constant over all coefficients, N,
or t down to0. The normalization read directly from the source is

    gamma_rho=-i(rho-1/2),
    g(x)=(2*pi)^(-1) integral_R h(r) exp(-irx) dr,
    m(r)=Re(psi(1/4+ir/2))-log(pi),
    sum_rho h(gamma_rho)
      =h(i/2)+h(-i/2)+(2*pi)^(-1) integral_R h(r)m(r)dr
       -2 sum_(n>=2) Lambda(n)n^(-1/2)g(log n).

The sum includes every nontrivial zero with multiplicity, including
off-line zeros. Its validity is retained as an import, not inferred from
positivity or a critical-line-only contour. The source identifies this
as its normalization of reference[12], Theorem5.12; that book theorem
was not separately inspected here and is not an additional audited input.

[Definition5.1 and Lemma5.2, printed pp8-9](https://arxiv.org/pdf/1708.02653v24#page=8)
specify the half-spectrum convention, absolute locally uniform heat-series
convergence and termwise differentiation. Import only these portions,
not Lemma5.2's separate large-time/first-zero assertion. In the future
audit compare equation(22) with this convention before applying(3);
the source proof divides the all-zero sum by two and scales by
4*pi*sqrt(t). No finite zero-verification height enters Lemma7.7.

[Lemma6.1, printed pp11-12](https://arxiv.org/pdf/1708.02653v24#page=11)
explicitly includes m(r)>=-6 for every real r and m(r)>1 for |r|>=20.
Both conclusions, with this exact definition of m, are named imports.
The full source proof cases were accessible; their numerical constants
and Binet estimates are not independently audited by this approval or
by the proposed assembly audit. C030d supplies the already audited
Gaussian estimates, with no zeta identity.

### Complete cases available for the bounded audit

[Lemma7.7 and full proof, printed pp19-20](https://arxiv.org/pdf/1708.02653v24#page=19)
apply(3) to h(r)=q(sqrt(t)*r)^2 exp(-t*r^2). Check evenness, reality,
the algebraic square, and admissibility before using the formula.
Track the polar evaluation q(i*sqrt(t)/2)^2 with its possible sign;
do not replace the original spectral or polar terms by modulus squares.
Taking an absolute value to bound an error is a separate operation.

All source proof cases needed after these imports were read, including
the core |x|<=20*sqrt(t), the complex evaluation in the polar term,
and the Fourier prime bound at frequency log(n)/sqrt(t). The source's
prime estimate uses b=log(n)>=log(2), its displayed quadratic comparison
in b, the domain t<=log(2)/180, Lambda(n)<=n, and the integral comparison
for sum_(n>=2)n^(-7). These are proof obligations for the mathematical
turn, not independently validated estimates here. No PNT error term,
zero simplicity or unverified-zero sign is among the source hypotheses.

The remaining scalar obligations are explicitly visible in the same
proof: eta_N monotonicity, membership of both tested times in the domain,
the errors <0.28, <0.013, <0.001 at tau_N=1/(4000000N), and the
N=3 errors <0.7112, <0.032, <0.001 using the stated C_3<2.54.
The target includes all N>=1, p=0, and both parities; sampled matrices
or floating point endpoint previews cannot certify it. Appendix A's
implementation is an unreplayed lead, not evidence for these strict
comparisons. The future audit may use analytic scalar bounds rather
than reproduce a source program, provided every strict inequality is
justified. No scalar estimate has been newly derived in this turn.

### Reuse, relevance, decision and exit test

Comparison1183's exact-statement/stronger-result searches remain adequate
for this unchanged source claim. Scoped local reads distinguish coverage
from audit: comparison1113 and approval1115 imported supporting estimates;
application1116/1182 checks their finite use; C030d/audit1184 checks only
the Gaussian component. No independent assembly audit was located in
these records. Stops1117 (finite-block extension) and1181 (all-a class
bridge) retain their scopes and do not prohibit this distinct check.
No claim about an exhaustive archive search or mathematical novelty follows.

SPECIALIZE licenses a subsequent REPRODUCTION audit of the identified
assembly difference. Merely citing Lemma7.7 would suffice to import its
conclusion, but would not answer the chosen question of independently
validating its proof relative to the retained imports. Do not reprove
C030d, C030a's transfer, the finite application, or the two imported
analytic theorems without a specific uncovered discrepancy and new gate.

Continue only if every term of(26), monotonicity and both strict margins
can be justified within these hypotheses; otherwise isolate the exact
failed inequality or missing applicability condition and preserve the
valid partial reasoning. A pass supports reliability of C030b's finite
source input only. All-degree actual-Xi positivity L030-L032/C032a,
far-time source validation, actual-theta signs and graph realization
remain unresolved. No new arithmetic sign/coercivity mechanism is
specified, so no justified creative continuation is nominated here.

This approval is process progress, reported STALLED mathematically;
it neither establishes a new mathematical input nor resets exploration.
Full matching Mathlib coverage is unchecked. No lemma, mathematical
script, PROOF or DAG changes, cross-notebook inputs, fresh mathematical
derivations or source-computation replay form part of this step. Screenshot
calls returned no visible images; only the accessible complete PDF text
and the recorded earlier primary reading are counted as source evidence.
