# Vanishing-time heat reference: signed-block moment nomination1372

TARGET: Assess primary-source coverage for the proposed mollified signed-block inequality for C019j's variable-time heat reference on T/sqrt(2*d)<Y<T/sqrt(d), with margin 1/sqrt(log d) on at least c*sqrt(d) disjoint blocks as specified in nomination1372.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1373 searched Selberg sign-change mollifiers, Hardy signed/absolute short-interval moments and heat-flow mollifiers; inspected Gonek-Ivic1604.00517v1, Mawia2019, Pearce-Crump2609.15329v1/v2 and the relevant Polymath1904.12438v2 formulas. Exact queries, read ranges and local duplicates are recorded below. No matching theorem was located; no novelty inference.
SOURCE_EVIDENCE: https://arxiv.org/html/1604.00517v1 Sections1-3, Theorems1-2 and Lemmas1-3/(2.1)-(2.9); https://msp.org/cnt/2019/8-3/moscow-v8-n3-p03-s.pdf pp229-233, Theorem1 and mollifier definition; https://arxiv.org/html/2609.15329v2 Proposition4.3/(17), Proposition5.8/(33)-(36) and their proofs, with v1 Section4 read first; https://arxiv.org/html/1904.12438v2 (5)-(24), Theorem1.5, Corollaries6.4-6.5/(68)-(74), Proposition6.6 statement and its y=0-relevant estimates. C019j's statement and scale formulas were read; assessment1368's Gaussian-source coverage reused.
COMPARISON: Primary signed and absolute Hardy moments exist, and Selberg-type methods count odd zeros, but the inspected theorems do not supply (A) for the variable-time heat observable with this Mobius weight and quantitative block margin. Polymath supplies an explicit small-positive-time approximation, not these moments. Its real-zero threshold remains inapplicable automatically.
GAP: The signed/absolute moment controls for the deformed observable, correct mollifier coefficient choice, blockwise margin and disjoint-block count remain unproved. No mathematical counterexample to (A) or impossibility theorem is established.
REASON: Bounded source comparison is complete and rules out the proposed automatic imports. Park the direct (A) attempt until a concrete deformed-moment mechanism is paid; nominate the independently testable explicit Riemann-Siegel reduction in assessment1373. This is a route-changing source mismatch, not a new mathematical discovery.
SCOPE: Exact nomination1372 and C019j normalization, integer d tending to infinity, no RH/simplicity/nonvanishing/effective onset. EXPLORE records the completed bounded search, not established coverage of (A); no creative proof attempt is nominated without its missing moment mechanism. The new analytic subtarget requires separate approval.
LITERATURE_REASON: The target changes from an absolute circle/heat error to mollified signed oscillations along t=Y^2/(2*d); ready1368/1370 do not assess the essential short-interval moment inputs.

## One proposed bounded test, not a derived result

Use C019j's exact definitions and write
\[
 Y_-=T/\sqrt{2d},\qquad Y_+=T/\sqrt d,\qquad
 \mathcal R_d(Y)=\frac{8H_{Y^2/(2d)}(2Y)}{m(Y)}.
\]
For one fixed theta in (0,1/4), to be justified from sources, set
\[
 X=\lfloor Y_-^\theta\rfloor,\quad
 M_d(Y)=\sum_{n\leq X}\mu(n)
          \frac{\log(X/n)}{\log X}\,n^{-1/2-iY},\quad
 W_d(Y)=|M_d(Y)|^2.
\]
X is fixed throughout the band. Here mu is the usual Mobius function.
The proposed test seeks fixed constants K,c>0 and, for every sufficiently
large integer d, at least floor(c*sqrt(d)) disjoint closed intervals
I strictly inside (Y_-,Y_+), each of length K/log(Y_-), satisfying
\[
 \int_I|\mathcal R_d(Y)|W_d(Y)\,dY
 -\left|\int_I\mathcal R_d(Y)W_d(Y)\,dY\right|
 >\frac{2}{\sqrt{\log d}}\int_I W_d(Y)\,dY.                 \tag{A}
\]
No estimate in (A), choice of constants, or sign consequence is proved
in this nomination. It is a specified question for source comparison.
The proposed margin is intended to exceed C019j's O(1/log d) error.
Its intended use is to obtain robust opposite-sign witnesses in many
disjoint blocks and then transfer them to actual Jensen polynomials.
That transfer, sample ordering, the exact root map, and separation from
existing bulk counts would remain separate proof obligations. A growing
partial root count would still leave the all-degree hyperbolicity gap.

## Source comparison and decision test for the next turn

Locate primary versions of mollified Hardy/Selberg sign-change arguments;
read the exact interval, mollifier and error hypotheses before proof
extracts. Compare their real observable with the displayed heat reference and
positive W_d. Reuse the inspected Polymath formulas, but inspect any
additional Riemann-Siegel remainder cases needed when heat time varies
with Y at the stated scale. Do not replace this curve by fixed t or t=0
without a paid uniform comparison, and do not divide by a possible zero.

The decisive threshold is (A) on c*sqrt(d) disjoint blocks, not a global
nonzero second moment or an unsigned count. Continue toward a creative
attempt only if the source comparison identifies concrete signed and
absolute moment controls with that scale, or a precise bounded missing
estimate whose proposed proof mechanism could pay it. If essential
inputs apply only on much longer windows or give no sign margin, record
that failure of automatic transfer and select an independently testable
covered subtarget; do not treat absent coverage as a mathematical
counterexample or repeat the same source search indefinitely.

The planned creative obstruction is the lack of robust signed samples
for an entire reference that may vanish. The bounded discriminator is
(A), with its explicit margin and count; it concerns the still-unbounded
Jensen root deficit. No creative research is authorized before the
separate source gate. The exact next invocation is literature comparison.

## Recorded overlaps and limits

The November1 signed-short-interval Hardy screen addresses D_1(Xi)
and reports long-window derivative moments; its unsigned-to-signed
warning applies, but its target is not (A). The November9 Young-mollifier
assessment addresses a zero-displacement/endpoint budget, not local
heat-reference signs. The October11 short-mollifier stop concerns a
particular discriminant mean with P(u)=u^2 and length H^(1/100);
no such positivity is assumed here. These are scope comparisons, not
new audits of their canonical mathematics.

Stops1345/1355 and source-screen559 remain intact. Polymath's printed
real-zero threshold remains unavailable as an automatic import at this
shrinking time, as already recorded in assessment1367. No cross-notebook
input is proposed. Essential local input is C019j with L018/L021's
normalization; any further lemma use requires its exact hypotheses.
Full matching Mathlib coverage for (A) is unchecked.

## Completed source comparison1373 — 17 November 2026

The preceding proposed inequality and decision test are preserved verbatim.
Main gap: actual-Xi all-degree positivity and the unbounded Jensen root
deficit. The intermediate target remains (A); its intended use is robust
opposite-sign samples beyond C019j's absolute error. Independent root-map,
ordering and bulk-separation obligations remain even if (A) is proved.

### Discovery and duplicate checks

Queries included `Selberg positive proportion zeros critical line sign
changes mollifier intervals length log T Hardy function`, `Selberg 1942
zeros zeta function critical line pdf sign change integral mollifier I1
I2`, `"heat" "Selberg" "mollifier" H_t zeros`, `"heat flow" "mollified"
"Riemann"`, and the exact Gonek-Ivic title. A bounded search is not an
exhaustive bibliography or evidence of originality.

Read the ready November1 Hardy-derivative and November9 Young-endpoint
assessments and October11 positive-discriminant-mean failure. Those
observables differ from (A); no old failure was generalized. A subsequent
exact-source local search located the October13 clipped-joint-sign
assessment's Gonek-Ivic comparison and November9 totient-profile
assessment's Pearce-Crump comparison. Read those source-specific ranges;
reuse their scope exclusions. The new reads concern the actual signed
and absolute moment hypotheses and current source version, not a repeat
of their different mathematical targets. Stops1345/1355/559 are retained.

### Primary theorem comparison

**Gonek and Ivic**, *On the distribution of positive and negative values
of Hardy's Z-function*, JNT174 (2017), 189-201,
[arXiv:1604.00517v1](https://arxiv.org/html/1604.00517v1), 2 April2016:
read Theorems1-2, Lemmas1-3 and their proofs, and Section3's moment-to-sign
passage. Write S for their height to avoid confusing it with C019j's T.
Their positive weight uses coefficients of zeta^(-1/2), not mu.
On [S,2S], their signed mean is o(S) for X=S^theta, theta<1/4;
absolute mean is at least S+o(S) for theta<1/2; the squared detector has
integral O(S) for theta<1/100. Theorem1 gives both sign sets measure >>S.
Theorem2 assumes RH and pair correlation and is excluded.
Lemma3's quoted Selberg shifted-moment formula has short offsets but an
outer interval U with S^a<=U<=S^(3/5), 1/2<a<3/5; it is not (A) on
one interval of length K/log S. The original Selberg proof is an unread
lead, not independently certified here. No heat-time parameter occurs.

**Mawia**, *On the distribution of values of Hardy's Z-functions in
short intervals II: The q-aspect*, Moscow J.Combin.Number Theory8
(2019), 229-245,
[primary PDF](https://msp.org/cnt/2019/8-3/moscow-v8-n3-p03-s.pdf): read
pp229-233, Theorem1, the corrigendum and the coefficient definitions.
The theorem fixes primitive characters of conductor q>1, q<=S^eta,
H=S^vartheta, 1/2+eta/2<vartheta<=1. It controls positive/negative sign
measure with conductor factors. Its weight again uses reciprocal-square-
root coefficients. This is neither a printed q=1 specialization nor a
microscopic heat-reference block theorem. No q=1 extension is asserted.
The moving-cutoff corrigendum reinforces retaining the actual cutoff in
the new analytic test. Later lemmas and the earlier paper are leads only.

**Pearce-Crump**, *Optimising Selberg's method for critical zeros*,
[arXiv:2609.15329v2](https://arxiv.org/html/2609.15329v2), 23 October2026:
read v1 Section4 and Proposition5.8 first; the current-version check then
read v2 Proposition4.3 and Proposition5.8 with proofs. Proposition4.3
requires the exact real-part identity, o(S) horizontal errors, and a
dyadic analytic-half mean-square bound uniformly at
1-2delta comparable to 1/log S. Proposition5.8 further requires prime
U comparable to S^theta, theta<1/4, real bounded coefficients b_1=1,
b_U nonzero with log^+(1/|b_U|)=O(log S), and its specified quartic
arithmetic bound. It counts odd critical zeros; it supplies no amplitude
margin or (A). The nomination does not verify these arithmetic/terminal
conditions, and its heat observable has no supplied analytic-half
identity. v2 corrects v1's advertised proportion; use no numerical
proportion or profile claim from v1 as a current input. The v2 profile
optimisation proof/certificate is not needed or certified here.

**D.H.J. Polymath**, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant*, Research in the Mathematical Sciences6 (2019), article31,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), 4 August2019:
refreshed (5)-(24), Theorem1.5, and Section6.3/(68)-(74); inspected
Proposition6.6 and the estimates of its sum and remainder bounds relevant
at y=0. Theorem1.3 is pointwise with explicit errors throughout
0<t<=1/2, 0<=y<=1, x>=200, including the real axis and every cutoff
value N=floor(sqrt(x/(4pi)+t/16)). Thus a moving-time application need
not use a fixed-time limiting theorem. The normalized error is relative
to B_t, not m(Y); the conversion must be paid. The two sum errors and
the Riemann-Siegel remainder are all retained. The theorem notes the
finite sum's jumps when N increases. Theorem1.5's regular real zeros
require exp(C/t); its all-zero count does not supply real signs here.

### Decision, limitation and independently testable continuation

No inspected source proves the displayed (A), even at time zero with
the nominated mu weight and margin. This states the inspected scope,
not a theorem of absence. Long-window shifted moments can be ingredients
of a block argument; they do not automatically establish this one.
The gaps are the observable, coefficients, quantitative local deficit,
and distribution into disjoint blocks, rather than just a missing zero
count. No comparison with H_0 or frozen heat time is proved in this turn.

Park the direct (A) implementation. A materially narrower analytic test
is saved in [assessment1373](2026-11-17-jensen-heat-riemann-siegel-reduction-1373.md):
convert the effective source approximation to the explicit real deformed
sum on the entire C019j band, with error O(Y_-^(-1/4)). Its proof and rate
are unestablished here; only the cited uniform theorem and its domain
are available. This subtarget is independently testable without a signed
moment theorem. It could expose the exact phases and coefficient profile
for a later bounded new signed mechanism. It will not itself prove (A).

Continue that specialization only if all normalization and cutoff cases
yield the stated uniform rate; otherwise preserve the failed estimate.
Before a later creative block attempt, require a concrete signed-moment
mechanism for the resulting deformed sum. There is currently no covered
creative estimate to route honestly. No lemma, mathematical script,
canonical theorem import or new mathematical derivation was made.
Full matching Mathlib coverage is unchecked. Web primary texts were
accessible; an optional local download failed on DNS (and one extraction
attempt lacked bs4), so no local source archive is claimed. These failures
are not essential source blockers and no access-retry turn is needed.
