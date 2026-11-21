# Uniform near-zero source-proof coverage — nomination1182

TARGET: Assess Polson v24 Lemma 7.7's uniform near-zero block bound for 0<t<=(4000000N)^(-1), and nominate one precise source-proof audit with its required constants and hypotheses.
CHECKED: 2026-11-16
DECISION: IMPORT
SEARCH_EVIDENCE: Comparison1183 reused comparisons1108/1113 and audit1116, searched Polson/Lemma7.7 records and recent Mehler/Gaussian-bound records in this notebook, and searched exact source phrases externally; no independent audit of these estimates was located. Search limits and queries are recorded below; no novelty inference follows.
SOURCE_EVIDENCE: Directly inspected Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24, https://arxiv.org/pdf/1708.02653v24, Section7.3/(21)-(26), Lemma7.6/full proof p19 and Lemma7.7/full proof pp19-20; Lemma6.1/full proof pp11-12 and Section4.3 explicit-formula hypotheses p8. Also inspected NIST DLMF18.18.28 https://dlmf.nist.gov/18.18.E28 and Hermite normalization in18.39(i) https://dlmf.nist.gov/18.39#i. Reading does not certify the estimates.
COMPARISON: C030b's finite application is already audited; comparisons1108/1113 read the source cases without independently validating them. The exact Gaussian estimates in Lemma7.6 are known preprint claims with a short Mehler/contour proof and support all three near-zero error bounds. Rechecking them is reproduction for reliability, not a new sign mechanism.
GAP: No essential source-access gap remains for the selected Lemma7.6 audit. Its complex Mehler specialization, coefficient-uniform norm estimates and contour constants remain mathematically unaudited; the explicit formula, Lemma6.1 and complete Lemma7.7 assembly are separate imported inputs.
REASON: Lemma7.7 already states the requested bound with exact hypotheses, so its statement is available by precise citation. Coverage1183 separately nominates reproduction of one supporting source proof, equations(23)-(25); no validation is performed here and the new continuation receives separate approval next turn.
LITERATURE_REASON: Changed scope from local application to independent source-proof validation; essential detailed estimate and overlap comparison are not supplied by the ready application assessment.
SCOPE: Literature-only extraction/comparison of the near-zero estimate and its directly necessary proof inputs; select at most one concrete audit. No lemma/script writes, fresh sign derivation, full-paper audit, verification-computation replay, cap optimization or all-degree inference.

The main gap remains actual-Xi Q(q)>=0 in every polynomial degree,
L030-L032/C032a. The plausible downstream use here is reliability of
the finite source input in C030b, not closure of that main gap. C030a,
C030b and L030 are the essential local inputs; do not reopen C030a's
audited analytic transfer unless an identified discrepancy requires it.
Source-proof correctness is presently imported; no new doubt or error
has been established. Actual-theta signing, all degrees and graph
realization remain independent unresolved requirements.

First search specific local Polson/Lemma7.7/near-zero records for an
existing independent audit, distinct from reading/applicability notes.
Then extract the primary lemma statement and relevant proof cases,
including its N/time domain, polynomial normalization and all constants.
Compare its actual tools with known results and recorded failures.
Reuse adequate prior source reading; additional reading is justified
only to cover the changed independent proof-audit scope.

Continue only if one load-bearing estimate admits a bounded independent
check under its exact hypotheses. Record that precise threshold and
its sources in the resulting assessment for separate approval. If the
task merely duplicates an already completed independent audit, or needs
unbounded source revalidation, stop this proposed check and record the
specific overlap or blocker; do not repeat C030b audit1116/1182.
No mathematical conclusion about the near-zero estimate is made here.

A genuinely new central sign mechanism remains unspecified. This
nomination is source comparison, not creative work manufactured from a
routine specialization. Discovery1117 and the stopped all-a automatic
bridge1181 retain their scopes and are not restarted. Full matching
Mathlib coverage is unchecked. No cross-notebook input is proposed.

## Completed comparison1183 — 16 November 2026

The preceding paragraphs preserve the nomination and its historical
instructions. This section records the completed source review; no
mathematical estimate was independently proved or tested.

### Exact near-zero source statement and required threshold

In [Polson v24](https://arxiv.org/pdf/1708.02653v24), printed p19,
equation(22), N is any positive integer, epsilon is 0 or 1, p is a real
polynomial of degree at most N-1, and q(x)=x^epsilon p(x^2). Thus
deg(q)<=2N-1. The norm uses unnormalized Lebesgue Gaussian weight:

    ||q||_G^2 = integral_R exp(-x^2)|q(x)|^2 dx.
    c_j(t)=(-1)^j W^(j)(t),
    Q_N,t^epsilon(p)=4*pi*t^(epsilon+1/2)
                    sum_(i,j=0)^(N-1) v_i*v_j*t^(i+j)*c_(i+j+epsilon)(t).

This is a scaled algebraic-square form over all squared zero exponents;
it is not the local Q(q) of L030 and is not a modulus-square spectrum.
Equation(22) includes one exponent per reflection pair and multiplicities.
No simplicity or critical-line assumption enters the near-zero estimate.

Lemma7.7/(26), printed pp19-20, states for 0<t<=log(2)/180:

    Q_N,t^epsilon(p) >= eta_N(t)||q||_G^2,
    eta_N(t) = 1 - 280*C_N*sqrt(t)
                 - 4*pi*C_N*sqrt(t)*exp((4N-1)*t/4)
                 - (4^N/48)*exp(-(log(2))^2/(24*t)),
    r_N=1-1/(2N),
    C_N=r_N^(-(2N-1))/(sqrt(pi)*sqrt(1-r_N^2)) < 2*sqrt(N).

It additionally claims eta_N is decreasing and eta_N(tau_N)>0.7
for every N>=1, tau_N=1/(4000000N). The exceptional join uses
eta_3(10^(-6))>1/4. These are extracted source claims, not conclusions
of this review. Required positivity is a coefficient-uniform lower bound;
checking selected vectors or individual diagonal entries is insufficient.

The full proof was read: the explicit formula is applied to
h(r)=q(sqrt(t)*r)^2 exp(-t*r^2); the archimedean term loses at most
280*C_N*sqrt(t), the polar term at most
4*pi*C_N*sqrt(t)*exp((4N-1)*t/4), and the prime term at most the last
displayed term. The source's endpoint error thresholds are respectively
0.28, 0.013 and 0.001; its N=3 thresholds are 0.7112, 0.032 and 0.001.
No endpoint arithmetic was independently checked here. Appendix A's
verification/higher_hankel.py is an unread/unreplayed implementation
lead, not evidence of successful local verification.

### Supporting inputs and why the selected audit is bounded

Lemma6.1, pp11-12, supplies m(r)>=-6 everywhere and m(r)>1 for |r|>=20,
where m(r)=Re(psi(1/4+ir/2))-log(pi). Its full series/Binet proof was
read to identify the import boundary, not independently validated.
Section4.3, p8, states the explicit formula for even h holomorphic in
a closed strip |Im(r)|<=1/2+delta, delta>0, with decay
O((1+|r|)^(-2-delta)) there, and Fourier convention
g(x)=(2*pi)^(-1) integral_R h(r)exp(-irx)dr. These hypotheses and
normalizations would require checking in a full Lemma7.7 audit.
They are not needed for the selected Gaussian-polynomial audit.

Lemma7.6/(23)-(25), p19, has no zeta or zero-verification hypotheses.
It supplies the real-axis and imaginary-axis evaluation estimates and
the Fourier estimate used in all three error terms. Its proof uses
Hermite orthogonality, Cauchy-Schwarz, Mehler's formula and one Gaussian
contour displacement. Read every proof case, including negative Fourier
frequency and the N=1 range. The independent audit remains to be done.

[DLMF18.18.28](https://dlmf.nist.gov/18.18.E28) gives Mehler's sum with
parameter of modulus less than one. [DLMF18.39(i)](https://dlmf.nist.gov/18.39#i),
equation18.39.14 and its normalization paragraph, specifies the physicists'
Hermite weight exp(-x^2) and squared norm 2^j*j!*sqrt(pi). These are
standard inputs to cite, not reprove. DLMF labels the displayed spatial
variables real; use at a conjugate complex pair requires the audit to
justify complex continuation/convergence, rather than importing the
real-variable positivity sentence as complex positivity.

The exact selected audit is in
[coverage1183](2026-11-16-gaussian-polynomial-source-audit-1183.md).
It checks known estimates rather than enlarging N or claiming novelty.
Reproof is justified only as independent validation of this load-bearing
preprint input; reading the theorem alone would leave that question open.

### Search, overlap and decision

Notebook searches selected Polson/Lemma7.7 records in drafts/literature,
history and ATTEMPTS; then Mehler, Gaussian-polynomial and equation-number
records from 14-16 November. Comparison1108 supplies prior full case
reading; coverage1114 and C030b/audit1116 explicitly exclude independent
source-proof validation. Discovery1117 reads the perturbation application
of the near-zero bound, and prime-gap audit1120 concerns a different
Fourier probe. Neither certifies Lemma7.6. The scoped searches located
no independent audit; this is not an exhaustive claim about all history.

External queries included `"Polson" "7.7" "heat"`,
`"Gaussian polynomial" "Hankel" "near zero" zeta`,
`"Xi heat trace" "Mehler" polynomial`,
`"Gaussian polynomial bounds" Hermite Fourier`,
`"1708.02653" "7.7"`, `"1708.02653" "Mehler"`, and
`"heat trace" "uniformly in the polynomial"`. Results supplied no
independent matching audit or stronger directly usable coefficient bound;
unrelated search hits were not mathematical evidence. Primary-source
reading, not snippets, establishes the comparison with the known claim.
No originality is asserted. DLMF's optional TeX endpoint was inaccessible
to the reader, but the complete HTML Mehler formula and parameter range
were accessible; there is no resulting source blocker.

Continue with exactly the Gaussian estimate audit if separately approved.
Success means all constants (23)-(25) hold for every allowed polynomial,
including N=1 and all real frequencies; failure means an explicit failed
inequality, inadmissible specialization or counterexample is isolated.
A pass validates only this source component. The full near-zero assembly,
archimedean input, far-time estimates, all-degree signs and graph
realization remain independent. Do not repeat the finite application or
revive the stopped automatic-extension route. No justified creative
central sign mechanism was identified in this review. Full matching
Mathlib coverage remains unchecked.
