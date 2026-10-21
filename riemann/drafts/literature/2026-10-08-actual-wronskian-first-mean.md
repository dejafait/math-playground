# Actual Wronskian first mean — bounded specialization coverage

TARGET: Compute the normalized dyadic first moment of (F_0'G−F_0G')/(A²T²L), retaining all carrier terms and testing its usefulness for a noncommon-zero witness.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact/stronger Wronskian and Hardy derivative-moment search in drafts/literature/2026-10-08-actual-wronskian-noncommon-zeros.md; specific L370 pointwise records contain no actual first-mean computation, and L369 treats a different bilinear expression.
SOURCE_EVIDENCE: Arias de Reyna arXiv:2406.16667v1, Theorem 6 and full proof pp. 5–6, https://arxiv.org/html/2406.16667v1 (rechecked); reused DLMF 25.2.1/11 https://dlmf.nist.gov/25.2 and gamma coverage https://dlmf.nist.gov/5.11#ii and https://dlmf.nist.gov/5.15#E8 through the October 5 assessments; inspected L366 (1), L368 (3)/(5)–(10), and L369 (4)–(9)/(12)–(18), including its complete weighted mixed-mean proof.
COMPARISON: Scalar truncation, right-line jets, critical-line reflection and bounded-variation mixed means are covered; neither the sources nor L369 compute the actual Wronskian mean or infer a noncommon zero from it.
GAP: Obtain a zero-safe expression for the physical Wronskian and verify the bounded-variation hypotheses of its weights, then determine the complete mean/error at the proposed normalization; noncommon localization is a separate unresolved gap.
REASON: One ordinary first-moment specialization can test the independent witness mechanism without the parked sharp-discriminant source or new high-moment hypotheses.
SCOPE: Actual F_0,G,A of L366, positive t, T=1+t and L=log(2+t), ordinary real derivatives with regulator zero; one dyadic first mean as H tends to infinity. No square/fourth moments, response-phase windows or noncommon-witness theorem are preapproved.

## Exact later test

Set W(t)=F_0'(t)G(t)−F_0(t)G'(t) and examine

    M_H = (1/H) integral_H^(2H) W(t)/(A(t)^2 T(t)^2 L(t)) dt.

The normalization is a proposed test scale, not an asserted asymptotic.
Seek a complete leading term and controlled error, or a rigorous bound
showing that this first-mean certificate cannot isolate useful sign
information. No value or sign of M_H has been derived or approved here.

L366 supplies the actual pair, with F_0=−A r and
G=A Re(exp(i phi)b zeta(5/2+it)) in L368/L369's notation.
The source hypotheses are critical-line reflection at 1/2+it,
absolute convergence on 5/2+it, and fixed gamma shifts in closed sectors
away from the negative real axis. These match this first-jet target.
Reuse L369's established weighted mean (16) for derivative total order
at most two, whenever sup|w|+integral|w'| is uniformly bounded.
Its complete proof retains the fixed cutoff, pole correction,
diagonal n=m including n=1, and every off-diagonal range.
Cite that result, rather than rerunning its proof or reproducing a
source theorem merely to add a lemma.

The missing specialization is the physical Wronskian's exact algebra
and the actual normalization weights. Retain both projections until an
exact critical-line identity handles them, the full polynomial b and b',
all carrier terms, and variation of T,L. Common-envelope cancellation
must be verified, not assumed. Do not divide by F_0,G or critical-line
zeta. At zeros use the same zero-safe identities; do not differentiate
an uncontrolled real-variable error or a moving cutoff.

## Relevance and decision threshold

The main gap is global actual-theta positivity and total L367 margin.
The first mean could determine whether a signed-mean route offers an
input for a later local sign test. It is not asserted sufficient for the
witness target: even both signs of W can arise only through common
zeros, as L373 proves. A later square/absolute moment, response-window
estimate or noncommon localization needs a separate exact assessment.

Continue if the complete statistic has sign/cancellation information
separated from its proved error and a concrete downstream local test.
If leading cancellation leaves no useful margin, report that limitation
and stop this first-mean signing certificate; do not infer W=0, eventual
disjointness or a noncommon witness. A first mean or independence alone
cannot settle the witness target. Physical D≤0, actual coincidence
control, all-degree positivity, low indices, exterior heights and
endpoint arithmetic margin remain unresolved.

Essential local inputs: L366's pair, L368's carrier and scalar bounds,
L369's reality identities and weighted means. L374/L378 explain possible
downstream use; L373 is obstruction context, not a premise of the mean.
Full matching Mathlib coverage is **not checked**. No mathematical
script is required. A completed mathematical specialization should be
classified REPRODUCTION, without claiming a new theorem beyond the
sources searched.

## Direct-source recovery review, 2026-10-08

The saved target and SPECIALIZE decision are unchanged. This separate
literature review repairs missing direct URLs, rather than proposing or
approving a new mathematical result. The October 5 assessments retain
the earlier search queries and source comparisons; the October 8
noncommon-zero assessment retains the stronger witness-theorem search.
No repeated broad search is needed for these unchanged hypotheses.

Reopened [Arias de Reyna v1, Theorem 6 and proof, pp. 5–6](https://arxiv.org/pdf/2406.16667v1#page=5)
in its [primary HTML](https://arxiv.org/html/2406.16667v1).
The scalar statement assumes fixed x>0, sigma>=0 and 0<t<=x,
retains x^(1-s)/(s-1), and bounds the remainder by (29/14)x^(-sigma).
Its proof treats sigma>0 using a weighted tail, the zero dual mode,
and t/x<=1, then handles sigma=0 by continuity. It assumes no RH.
This is an imported scalar result, not a Wronskian or derivative theorem.
L369 (12)–(14) already supplies the fixed x=3H disk applicability,
Cauchy jets and pole-correction estimates; no reproof is needed.

Reopened [DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii): the complex
log-gamma/digamma remainders carry the stated secant factors.
Reuse the earlier inspected DLMF version 1.2.8 coverage, including
[5.15.8](https://dlmf.nist.gov/5.15#E8) for controlled derivative
expansions and [25.2.1/11](https://dlmf.nist.gov/25.2) on Re s>1.
The fixed gamma arguments 1/4+it/2 and 5/4+it/2 stay in closed
sectors away from the negative real axis; 5/2+it lies in absolute
Dirichlet/Euler convergence. The critical-line factor is covered by
the scalar truncation, not by an absolutely convergent Euler series.

Read L369's complete (12)–(18) proof: its complex C1 weight condition
is sup|w|+integral|w'|<=C_w independent of H, derivative total order
at most two, and mean error O(C_w H^(-1/2)(log H)^2). It retains the
diagonal n=m, its tail, every off-diagonal range and analytic remainder.
This supports a later first-jet specialization only after its actual
weights meet that condition. The exact Wronskian algebra, weights,
mean and usefulness remain uncomputed. L370's pointwise decomposition
and its assessment do not duplicate this target or supply a first mean.

Coverage is ready for the exact saved calculation; no essential source
blocker remains. No lemma, script, new asymptotic or noncommon-witness
claim is produced in this literature-only review. Later higher moments
or localization still require separate coverage.
