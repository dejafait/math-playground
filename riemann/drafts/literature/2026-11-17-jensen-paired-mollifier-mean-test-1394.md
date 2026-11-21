# Paired fractional mollifier — narrowed signed-mean test1394

TARGET: Test the first (M2) inequality for C019m's actual Jensen pair with the fixed reciprocal-square-root mollifier, retaining both twisted product channels and paying the weighted transfer at scale B.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse completed review1394 in nomination1393 and its source-notes1394; the first (M2) inequality is a named subtarget of that exact search. Review1395 directly reopened https://arxiv.org/html/0803.1141v2 and https://arxiv.org/html/1604.00517v1 at the named proof cases; no new discovery search or novelty inference.
SOURCE_EVIDENCE: https://arxiv.org/html/0803.1141v2#A Appendix A.1-A.3 and Section2/(2.4)-(2.5), and https://arxiv.org/html/1604.00517v1 Lemma3 proof (2.8)-(2.9), directly inspected in review1395; other paired/twisted comparisons reuse review1394. Ready1381 and canonical C019l/m retain the local reduction/normalization, not a weighted theorem.
COMPARISON: Ordinary mollified pair formulas and fourth-moment results do not determine this signed moving-heat mean. Available standard finite-sum tools justify a bounded direct attempt; they do not guarantee the needed arithmetic sign or error saving.
GAP: Determine whether the whole actual-P weighted mean is eventually <=-cB for an absolute c>0; both twisted channels, all resonances and the weighted transfer remain unpaid. Squared mass and root counting are outside this narrowed attempt.
REASON: Review1394 narrowed the two-moment proposal to one load-bearing sign test, changing the full observable from the stopped small-R mechanism and avoiding the unread Selberg proof as a premise. Separate literature approval1395 repairs the missing direct source URLs and confirms unchanged scope; no calculation has been performed.
SCOPE: All sufficiently large positive integer d; exactly C019m P,T,X,q,B,h,J,D and C019l V; L=floor(X^(1/1000)); alpha(n) and taper below; own heat time/floor in each factor; no RH, random law, simplicity, nonvanishing or effective-onset premise.

## Exact proposed discriminator

Retain C019m (1)'s actual real P and positive normalization. In
particular X=T/sqrt(2d), q=log X, B=(sqrt(2)-1)X,
h=3*pi/q and D=[X,sqrt(2)X-h], with T and d related exactly as there.
Let L=floor(X^(1/1000)), eventually at least2, and define

\[
 \zeta(s)^{-1/2}=\sum_{n\geq1}\alpha(n)n^{-s}
 \quad(\operatorname{Re}s>1),\qquad
 M_d(Y)=\sum_{n\leq L}\alpha(n)
       \frac{\log(L/n)}{\log L}\,n^{-1/2-iY}.
\]

The branch is the Euler-product branch positive on real s>1. Only the
real coefficients enter a finite polynomial; no reciprocal at a zero
is taken. Set W_d(Y)=|M_d(Y)M_d(Y+h)|^2. The question is whether
there exist an absolute c>0 and common integer onset such that

\[
 \int_D P(Y)P(Y+h) W_d(Y)\,dY\leq-cB.                 \tag{M1}
\]

This is unchanged (M2)'s first inequality, not a weakening obtained
by changing shift, taper or degree subsequence. A successful finite-
reference computation must also pay

\[
 \left|\int_D\{P(Y)P(Y+h)-V(Y)V(Y+h)\}W_d(Y)\,dY\right|
       =o(B),
\]

or another explicit error smaller than its proved negative margin.
This proposed transfer is unproved. C019m's unweighted error and
P+V=O(1/q) alone do not establish it. Failure of a crude absolute
bound is only failure of that bound, not a refutation of (M1).

## Bounded attempt and decisive evidence

Start from C019l's actual finite V and retain the entire arithmetic
weight. Investigate both the conjugated and unconjugated product
channels; each twist, entry domain, stationary region and nonstationary
remainder must be paid. No diagonal dominance, shift cancellation or
sign of an arithmetic main term is assumed here. Preserve any partial
formula and explicit missing bound before lengthy work.

The sought evidence is a signed asymptotic or rigorous bound at scale
B with all errors compared to its margin. Continue the paired mechanism
if this establishes a fixed negative actual-P margin. A proved
incompatible sign/asymptotic abandons this fixed test; an unpayable
transfer or unresolved resonance records an informative obstruction
only if a rigorous lower bound or other discriminating evidence is
obtained. Otherwise report an inconclusive bounded attempt honestly,
preserve the gap and reassess before repeating. Do not optimize the
mollifier or change the target during the attempt without coverage.

Even success leaves (M2)'s O(B) squared mass, interval selection, root
map, bulk separation and the all-degree deficit unresolved. Its plausible
use is to remove rare-amplitude dominance from the negative pair mean
once squared mass is separately controlled. It is not an RH proof.

## Standard inputs and qualifications

Reuse1377's precise Koesters AppendixA.1 bound for monotone F' of fixed
sign bounded away from zero, A.2 bound for real F'' of one sign bounded
away from zero, and A.3 logarithmic index sum. These hypotheses must be
checked anew for every arithmetic twist; A.3 for plain log(n/m) is not
an estimate for an arbitrary rational twist. Variable amplitudes require
an explicit integration-by-parts/variation argument. C019l/m's existing
coefficient bounds and own-floor identities remain canonical local
inputs, not weighted theorems. No reproof of a known theorem is proposed;
the difference is this concrete full arithmetic weighting.

Essential inputs are C019m and C019l, with inherited C019j/k and L018/L021.
Corrected C019n and audited C019o supply comparison/stop evidence only;
their diagonal-small-remainder closure is not assumed. Review1394's
ordinary paired sources are comparisons, not essential premises. Full
matching Mathlib coverage is unchecked. No cross-notebook input is used.

After separate approval1395 the recommended route is proof_attempt/creative,
deep_research/max: the new arithmetic weighting tests rare-amplitude
dominance at the exceptional-root-density gap. The bounded critical
claim is (M1) with its paid actual-P transfer, not the full RH target.

## Separate source approval1395 — 17 November 2026

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; this approval checks access and the existing source scope, without repeating discovery or deriving mathematics.

Directly accessed Kösters v2, 5 September 2008, Appendix A.1-A.3
and Section 2, (2.4)-(2.5), including both channel estimates.
The derivative lemmas impose the stated separation conditions; the
logarithmic sum has ordinary integer indices. Neither gives arbitrary
twist summation or weighted transfer automatically. Its proof handles
entry times and a varying phase explicitly. These cases support a
direct attempt, not transplantation of its final error bound.

Directly accessed Gonek--Ivić v1, April 2016, Lemma 3 proof,
(2.8)-(2.9): ordinary gamma-normalized Hardy factors, fractional
mollifier, restricted short intervals and shifts. The reported kernel
bound does not give the signed margin needed here. The underlying
Selberg proof remains unread and parked; its reported formula is a
comparison, not a premise for the direct attempt.

Approval is EXPLORE for exactly TARGET and SCOPE above. Earlier
reviews1377/1381/1394 cover the remaining comparisons; no changed
hypothesis or essential unread input has been added. This is a process
repair, with no new mathematical evidence and no claim of novelty.
The next turn may attempt the saved target; this approval does not
approve its unproved sign, resonance estimates or actual-P transfer.
