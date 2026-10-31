# Finite vertical-side measures: bounded norm test

TARGET: Test whether finite nonnegative measures on L504's paired vertical sides can give a full-space M norm O_R(a) for Q_a plus the side integral, uniformly at all large T.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-family queries, scoped common-witness duplicate check and failure comparison in drafts/literature/2026-10-30-vertical-side-finite-measure-certificate.md; no matching theorem or recorded obstruction for every vertical measure was identified. No originality is inferred.
SOURCE_EVIDENCE: Brevig et al., arXiv:2210.13922v2, Corollary 3.9/Theorem 3.10 and endpoint proof, pp. 14--15, https://arxiv.org/pdf/2210.13922v2#page=15 ; Goberna--Volle, arXiv:2106.14573v1, Proposition 3.2/proof, pp. 7--8, https://arxiv.org/pdf/2106.14573v1#page=8 ; Instanes, Section 1/Theorems 1.1--1.3, https://link.springer.com/article/10.1007/s00365-026-09777-0 . Direct primary sources retrieved again on 2026-10-30; these are scope comparisons, not imported premises.
COMPARISON: Existing horizontal-density and global-majorant stops do not state the proposed every-vertical-measure norm result. General evaluation/duality theorems provide no threshold here. The test requires only elementary Fourier and finite-measure calculations; no strong duality, optimizer, mass bound or total-positivity theorem is presumed.
GAP: Decide the displayed infimum at the O_R(a) threshold, or establish a lower bound divergent relative to a uniformly over all finite nonnegative measures, using genuine V_R tests and all large real T. Neither conclusion has been derived.
REASON: Separate literature-only recovery has checked the unchanged target against the recorded comparison and retrieved direct primary URLs. EXPLORE remains ready for one bounded elementary test; this approves source coverage only, not a mathematical result or audit pass.
SCOPE: Only J_{a,nu} below and its applicability as a possible one-sided Q certificate. No arbitrary rectangle-supported measures, H_a construction, L503 audit, actual-Xi transfer or RH claim. Matching Mathlib coverage is unchecked.

## Exact question and inputs

Retain L504's fixed R>0, L=log T, a=log L/pi, b=a/4,
B=L/(4pi), lambda=pi/(2a), K, V_R, u=Re f, M and Q_a.
In particular V_R consists of even entire functions real on R with
smooth compact Fourier data supported in [-R,R] in the 2pi convention;
M(f)=integral_R |f(x)|K(x)dx and K(0)=0. There is no uniform
Fourier-derivative bound. For a finite nonnegative Borel measure nu on
[b,B], independent of f and allowed to depend arbitrarily on R,T, set

    J_{a,nu}(f)=Q_a(f)
       +integral_[b,B] [u(a,y)+u(-a,y)] dnu(y),
    ||J_{a,nu}||_M=sup_{0!=f in V_R} |J_{a,nu}(f)|/M(f).

The threshold sought is

    inf_{finite nu>=0 on [b,B]} ||J_{a,nu}||_M <= C_R a

for all sufficiently large real T. The constant and onset may depend
on fixed R but not T, f or nu. Atomic/singular measures and endpoint
atoms are included. No uniform mass bound, minimizing measure,
finite-norm assertion or strong duality is assumed. L504 supplies the
definitions and basic Fourier facts; L505 and L507 are scope contrasts,
not theorem inputs for a new conclusion. No cross-notebook input.

## One bounded attempt and decision

Attempt a finite-frequency separation test for this positive-measure
family, using smooth compact-frequency packets or their finite linear
combinations. First establish the actual functional formula and
well-definedness; do not treat a formal cosine as an element of V_R.
Any proposed lower obstruction must be uniform over every nu, either
by a common witness or by explicitly controlled nu-dependent tests.
The elementary positivity/support constraints on nu may be used, but
no unexplained finite-atomic reduction or moment-duality theorem may
be introduced. This is a proposed test, not a claimed separating
combination, transform identity or estimate.

Track the full signed functional and M, not one large term or sampled
Fourier values. L504's M<=N may support a lower bound. For an upper
bound any reverse norm conversion must be justified at K's zero.
Approximation on the gap alone is insufficient: the side interval
extends to B and errors are integrated against unrestricted mass.
Check evenness, reality, bandwidth, endpoint atoms and uniformity at
every sufficiently large real T, including frequency-choice jumps.

Continue only with the stated upper certificate or an explicit lower
bound whose ratio to a diverges for every allowed measure. Otherwise
save partial reasoning and the failed discriminating test, and stop
this bounded attempt rather than try more measures without new input.
One failed nu, a failed common-witness ansatz or an unbounded formal
multiplier does not refute the whole family or the H_a inequality.

The prospective use is a one-sided Q bound on H_a using rectangle
positivity. Its sign and endpoint applicability must be checked in the
research turn. Success would still leave actual-Xi realization,
T-uniform arithmetic errors, initial signs and all-degree positivity
unresolved. This is established-route development, not a newly
justified creative mechanism at the actual-Xi gap.

## Separate source-gate recovery, 30 October 2026

LITERATURE_REASON: The supervisor required direct source URLs in the ready assessment; target and assumptions are unchanged. Reuse the exact-family searches and duplicate/failure comparison in the certificate assessment; no repeat discovery search or new mathematical deduction is needed.

The [Brevig--Chirre--Ortega-Cerda--Seip v2 primary PDF](https://arxiv.org/pdf/2210.13922v2#page=15) is accessible. The retrieved Theorem 3.10 and its proof take a normalized function in PW^p, 1<=p<infinity, and use a Fourier-matching residual, Holder and density to bound origin evaluation. Reuse the previously inspected Corollary 3.9 and p=1 qualification from the parent comparison. Neither the weighted M norm nor positive vertical measures occur in the needed conclusion; no specialization is asserted.

The [Goberna--Volle v1 primary PDF](https://arxiv.org/pdf/2106.14573v1#page=8) is accessible. Rechecked Proposition 3.2's proof and finite-constraint discussion against the earlier statement extraction: its uniform strict-feasibility hypothesis is essential to the attained scalar sup-dual conclusion. The finite-index minimax argument does not certify an arbitrary Borel side measure or our norm threshold. No duality theorem is used as a premise.

The [Instanes publisher full text](https://link.springer.com/article/10.1007/s00365-026-09777-0) is accessible directly although the DOI redirect failed in this retrieval. Rechecked the Section 1 theorem statements: Theorem 1.1 gives origin-evaluation comparisons for p>=2; Theorems 1.2 and 1.3 optimize separated real sequences for 2<=p<=4 and 4<p<=5, respectively. They do not cover the p=1 weighted side-measure problem. Later proof cases remain unnecessary and are not newly claimed read.

This is a process repair and separate source approval, with no new overlap result, mathematical advance, or informative negative result. Preserve L504/L505/L507's recorded stops and the exact bounded test above. Essential coverage for that elementary attempt is ready; needing any unassessed non-elementary theorem would require a new literature gate. Matching Mathlib coverage remains unchecked.
