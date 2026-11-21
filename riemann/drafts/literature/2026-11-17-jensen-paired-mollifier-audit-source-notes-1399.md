# Paired-mollifier audit source notes1399

This is a literature-only scope review for the exact TARGET in
[assessment1398](2026-11-17-jensen-paired-mollifier-negative-mean-audit-1398.md).
It neither establishes nor audits a new estimate. The main gap is
actual-Xi all-degree positivity and the unbounded Jensen-root deficit.
The one intermediate target is critical review of provisional M1;
its downstream use and decisive test remain those in that assessment.

## Reused coverage and local failures

Read ready1394, its separate approval1395, source-notes1394 and
nomination1393's completed source comparison. These already inspect
[Kösters0803.1141v2](https://arxiv.org/html/0803.1141v2#A), Appendix
A.1-A.3 and Section2/(2.4)-(2.5): respectively separated monotone first
derivative, separated one-sign second derivative, and ordinary integer
logarithmic-index sum. Their hypotheses remain obligations for every
twist, variation and entry interval. Ready1394 contains the precise
Titchmarsh lemma locators and direct-access record; no reproof or new
source extraction of these unchanged inputs is needed.

Also reuse the inspected Gonek--Ivić1604.00517v1 Lemma3/(2.8)-(2.9),
BBLR1609.02539v1 Theorems1.1-1.2, Bui--Hall2304.05178v1 Proposition2
and Bui--Hall--Subira Jorge2511.14415v1 Theorem1.1 comparisons in1393/1394.
They concern ordinary Hardy/zeta moments with their own coefficient,
taper, length and interval restrictions. They do not supply this
moving-heat negative mean or complex square formula. Selberg's original
Lemma15 proof is still unread and is not an essential premise for
auditing the explicit local finite-sum argument.

For local scope, read C019p/q hypotheses, conclusions and classical-input
sections; C019r hypotheses, conclusions, norm/endpoint and square/transfer
sections; working1398's account of its changed mechanism; and history1398.
This was not a complete proof read or independent check. Exact counts,
phase identities and constants are not certified by this source review.
The inherited C019l/m,j/k and L018/L021 inputs remain subject to their
canonical qualifications and prior audit status.

Read ATTEMPTS/2026-11-17-jensen-small-remainder-budget-obstruction-1391.md
and ATTEMPTS/2026-11-17-jensen-laplace-origin-variation-closure-unpaid-1387.md.
The audited small-R contradiction concerns diagonal-plus-small-remainder
closure; the origin/variation stop concerns inadequate absolute control.
C019r explicitly retains the whole weighted arithmetic pair instead.
Neither historical result licenses dropping its stationary contribution,
and neither is a global prohibition of this different test. Older
stops1345/1355/559 and parked(A) are retained through the reused assessment;
no repeat broad archival search was made.

## Additional bounded searches

Queries actually issued:

- `gcd matrix Jordan totient factorization logarithmic weighted gcd sums operator norm Hilberdink`
- `"gcd sums" "logarithmic" weights matrix`
- `"Schur test" weighted row column operator norm lecture notes`
- `Dym Katsnelson Contributions of Issai Schur to analysis arxiv weighted Schur test`
- `gcd matrix "logarithmic weights" norm`
- `"GCD sums from Poisson integrals" arxiv`

These identify standard matrix tools and spectral bounds, without an
exact covering moving-heat or logarithmic-multiplier theorem. Search
absence is not a novelty claim. No repeated search for the stopped
small-R bound, no zero-free-region proposal and no cross-notebook read.

## Inspected primary comparison: gcd quadratic forms

Aistleitner--Berkes--Seip, *GCD sums from Poisson integrals and systems
of dilated functions*, [arXiv:1210.0741v3](https://arxiv.org/html/1210.0741v3),
28 March2013: read Lemma1/(23), its preceding Poisson identity, and
Section4 Theorem5 with its entire proof (25). For positive coordinates
0<t_j<1, Lemma1 represents the generalized gcd form for finitely many
multi-indices and arbitrary complex coefficients as a Poisson integral
of a squared polynomial modulus. Theorem5 assumes decreasing positive
t in the infinite polydisc and gives

\[
 \Lambda_t(N)\le(e^2+1)(\lfloor\log N\rfloor+2)
                    \max_{1\le n\le N}\Gamma_t(n).
\]

Here Lambda is the supremum of spectral norms relative to coefficient
ell2 norm over distinct multi-indices, and Gamma is the supremum of
normalized unweighted sums. The proof groups coefficient magnitudes
and uses positivity. These results do not state C019r's relative bound
for a logarithmic multiplier in its own gcd norm, its Jordan-coefficient
majorants, or the signed heat kernel. No specialization was derived.

## Inspected primary supporting tool: weighted Schur bounds

Grohs--Vigogna, *Intrinsic Localization of Anisotropic Frames II:
alpha-Molecules*, ETH Research Report2014-10, March2014,
[Section2.2 Lemma(2.8), (2.9) and proof, printed pp4-5](https://www.sam.math.ethz.ch/sam_reports/counter/ct.php?file=/sam_reports/reports_final/reports2014/2014-10_fp.pdf).
The matrix is complex on a discrete index set; weights w1,w2 are
strictly positive and 0<p0<=1. Its two assumptions are

\[
 \sum_\lambda w_2(\lambda)^{p_0}|A_{\lambda\lambda'}|^{p_0}
       \le C_1^{p_0}w_1(\lambda')^{p_0},\qquad
 \sum_{\lambda'}|A_{\lambda\lambda'}|w_1(\lambda')^{-1}
       \le C_2w_2(\lambda)^{-1}.
\]

Under both it gives weighted ellp boundedness; for p>=1 the norm
bound is C1^(1/p) C2^(1/p'), with 1/p+1/p'=1. Read the proof's
endpoint bounds and final Hölder step. This supports the classical
row/column method only: C019r's particular transformed matrix,
Schur weights, row/column constants and passage to its gcd norm
still require independent checking. No reproof is proposed.

## Locators and unread leads

Dym--Katsnelson0706.1868v1 Section3/(3.14)-(3.16) was read as a
locator for the classical weighted Schur test; its historical survey
is not relied on for a new mathematical premise. Original Schur1911
was not read. The Hilberdink--Pushnitski spectral paper, Hilberdink's
Acta Arith.139 (2009), pp362-363, and logarithmic gcd-average hits
remain unread leads. No theorem from them is imported. Search hits
from RH-claim pages and secondary aggregators were not used as evidence.
None is essential to audit this explicitly proved finite argument.

## Coverage decision

EXPLORE for the unchanged audit target. The standard finite-sum and
matrix tools are adequately covered; no source theorem inspected
replaces the actual claimed sign argument. Its exact norm constants,
integer harmonic endpoint convention, stationary lower-limit
cancellation, complex square symmetrization and paid transfer are
the mathematical audit, which is deferred. Full matching Mathlib
coverage is unchecked, with no absence or formalization claim.

No lemma, mathematical script, DAG or PROOF change is authorized or
made in this literature step. No mathematical exploration budget is
spent or reset; source approval is not mathematical progress beyond
the inspected sources.
