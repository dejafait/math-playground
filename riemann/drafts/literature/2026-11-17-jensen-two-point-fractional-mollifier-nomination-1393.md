# Two-point fractional mollifier — nomination1393, source review1394

TARGET: Assess primary-source coverage for the two-point reciprocal-square-root mollifier test (M2) for C019m's actual Jensen values.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1394 completed bounded exact/stronger-result searches and the narrow local duplicate/failure comparison listed in source-notes1394; no matching moving-heat (M2) theorem located, with no novelty inference. Reused1372/1376/1377/1381/1385/1389/1391 rather than repeat their broad discovery.
SOURCE_EVIDENCE: Inspected BBLR arXiv1609.02539v1 Theorems1.1-1.2 pp2-4 and Section2.1-2.4 pp6-10; Bui-Hall arXiv2304.05178v1 mollifier definition, Proposition2 and proof (10)-(14); Bui-Hall-Subira Jorge arXiv2511.14415v1 Theorem1.1 and amplifier hypotheses. Rechecked Gonek-Ivic1604.00517v1 Lemma3 proof (2.8)-(2.9); earlier scalar/HRS coverage reused. Direct URLs and qualifications below.
COMPARISON: Ordinary paired fractional-mollifier shape was already recorded in1372/1376; its bounded kernel does not establish the negative sign. New fourth-moment comparisons supply ordinary twisted formulas, not an evaluated moving-heat (M2). Narrow to the signed first mean before attempting squared mass; do not treat that narrowing as a theorem.
GAP: Both (M2) inequalities, both conjugate product channels with arithmetic twists, all moving floors/weights and weighted actual-P transfer remain unproved; squared mass is parked pending a discriminating mean test.
REASON: Available finite-sum oscillatory tools support a bounded direct mean attempt without importing unread historical proofs. No automatic ordinary-to-heat import is justified; the two-moment closure is not approved as an established input. Separate approval of the narrowed continuation is required.
SCOPE: C019m's exact P, X, q, B, h, J and D; fixed exponent1/1000 and finite polynomial below; all sufficiently large integer d with own times/floors; no RH, random law, nonvanishing or effective-onset premise. Completed work is literature-only; no new mathematical result.
LITERATURE_REASON: Coupled fractional-mollifier moments change the target beyond1391's first-absolute-moment audit; this turn inspects genuinely additional paired/twisted coverage. The former scalar assessments remain reused.

The original nomination below is retained verbatim after this note.
Its prospective instructions describe the state at1393; completed
review1394 and its narrower continuation at the end now govern routing.

## One bounded proposed test, not a result

Use exactly C019m's real P(Y) and positive normalization. Retain
X=T/sqrt(2d), q=log X, B=(sqrt(2)-1)X, h=3*pi/q and
D=[X,sqrt(2)X-h]. Let L=floor(X^(1/1000)), eventually at least 2.
Define the real arithmetic coefficients alpha(n) by the absolutely
convergent Dirichlet series

\[
 \zeta(s)^{-1/2}=\sum_{n\geq1}\alpha(n)n^{-s}
 \quad(\operatorname{Re}s>1),
\]

using the Euler-product branch positive for real s>1. Only these
coefficients, not an analytic reciprocal at a critical-line zero,
enter the finite polynomial

\[
 M_d(Y)=\sum_{n\leq L}\alpha(n)
       \frac{\log(L/n)}{\log L}\,n^{-1/2-iY},\qquad
 Q_d(Y)=P(Y)P(Y+h)|M_d(Y)M_d(Y+h)|^2.
\]

The single proposed discriminator asks for absolute c,C>0 and a common
integer onset such that, for every subsequent d,

\[
 \int_D Q_d(Y)\,dY\leq-cB,
 \qquad \int_D Q_d(Y)^2\,dY\leq CB.                 \tag{M2}
\]

The exponent is a fixed test parameter, not a value justified by a
two-point theorem. Even this short mollifier does not make (M2)
automatic. Neither inequality, an arithmetic constant, nor a transfer
bound is derived here. The intended use is to seek positive-measure
opposite-sign pairs and then disjoint intervals at the Xq root scale;
that implication, selection, reciprocal root map and separation from
bulk roots remain subsequent obligations. No full-degree conclusion
or RH candidate is proposed.

## Comparison, test and routing

This differs from parked (A) in assessment1372: (A) required a
signed-versus-absolute deficit on individual microscopic blocks with
a Mobius weight. Here the reciprocal-square-root coefficients match
the recorded scalar sign source, while the integrals are over the
whole band and the weight acts on both members of a prescribed pair.
The changed object is a question about two coupled global moments,
not an assertion that scalar sign density implies paired signs.
It also differs from1387/1391: no upper bound on their additive R
is proposed, and no endogenous denominator is differentiated.

Essential local inputs for an eventual attempt are C019m's exact P,
C019l's V/scales, corrected C019n, and audited C019o's real-kernel
representation. C019j/k and L018/L021 remain inherited normalization
inputs. The known unweighted error P+V=O(1/q) does not by itself pay
its error after multiplication by this arithmetic weight. Likewise
C019o's unweighted Tonelli argument supplies no coupled moment bound.
These costs, the two pair channels and the sign of the whole mean
must be assessed explicitly, not hidden in a diagonal premise.

The next turn is literature-only: search the exact paired fractional
mollifier, shifted Hardy signed moments and twisted second/fourth
moments; compare primary hypotheses, lengths, shifts and proof cases.
Reuse1372/1385 for scalar results and1390 for Fourier/first-moment
tools. The original Selberg shifted-moment proof recorded as unread
in1372 is a lead, not an input. Do not redo broad searches for (A)
or (N), and do not treat absence of a search match as novelty.

Continue only if that review identifies a concrete arithmetic/analytic
calculation capable of testing both inequalities, or narrows to one
load-bearing moment with a discriminating sign or growth threshold.
A conditional moment theorem, a nonnegative leading constant, an
unpaid transfer at the B scale or only scalar sign density requires
narrowing or abandoning this precise test. Do not repeat the same
unresolved search under a renamed route.

If subsequently covered, the intended proof route is creative,
deep_research/max. Its precise obstruction is rare-amplitude dominance
of the negative unweighted pair mean: it prevents the root density
needed to address the unbounded Jensen deficit. The bounded test is
(M2), with fixed negative B-scale mean and bounded B-scale squared
mass, or an informative incompatible asymptotic. This nomination
neither approves nor attempts that creative work. The immediate
source review is standard/high literature_comparison.

Retain stops1345/1355/559/1387/1391 and parked (A). No cross-notebook
input is used. Full matching Mathlib coverage for (M2) is unchecked.

## Completed source comparison1394 — 17 November 2026

### Primary statements and relevant proof cases

**Gonek--Ivic**, [arXiv:1604.00517v1](https://arxiv.org/html/1604.00517v1),
Lemma3 proof (2.8)--(2.9), was rechecked specifically for paired scope.
Using S for source height, their quoted Selberg formula concerns
X_0(t+u)X_0(t+v)|eta_u(t)eta_v(t)|^2 integrated over [S,S+U],
with xi=S^((2a-1)/20), 1/2<a<3/5,
S^a<=U<=S^(3/5), and 0<=u,v<=H<=1/sqrt(log xi).
It has main term sqrt(2*pi) U K(u-v) and error O(S^(1/2)xi^7).
Here X_0 is their gamma-normalized ordinary Hardy function. They
report K(w)=O(1) for 0<w<=1/log xi and discuss w=0 by continuity.
This is the already recorded ordinary paired shape, not newly found
mathematics. No negative constant, moving heat weights or squared-pair
bound is established there for our target. Their original Selberg
input, *Collected Papers I*, Lemma15, pp100/108/113, remains unread;
we neither certify its proof independently nor use it in the next
direct attempt. Its original length/interval restrictions must not be
silently replaced by the nomination's band.

**Bettin--Bui--Li--Radziwill**, *A quadratic divisor problem and moments
of the Riemann zeta-function*, [arXiv:1609.02539v1](https://arxiv.org/pdf/1609.02539),
8 September2016, Theorems1.1--1.2, pp2--4: four ordinary zeta factors,
two on each side, shifts O(1/log S); polynomial twists A,B of length
S^vartheta with coefficients O_epsilon(n^epsilon); smooth Phi supported
in [1,2], Phi^(j)<<_j S^epsilon. The error is
O_epsilon(S^(1/2+2*vartheta+epsilon)+S^(3/4+vartheta+epsilon)),
so the stated useful range is vartheta<1/4. All six main terms are
required, including their holomorphic continuation at colliding shifts.
Section2.1--2.4, pp6--10, was read through the production of the four
off-diagonal main terms: the twisted equality is arithmetic, and
unequal-index terms cannot all be declared negligible. The theorem
provides a possible ordinary comparison, not the value or boundedness
of our fractional-coefficient main sum. No heat parameter or moving
source floor occurs. Its quadratic-divisor proof is not independently
reproduced; no specialization is asserted here.

**Bui--Hall**, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1),
11 April2023: inspected the Section1 mollifier definition and
Section4/Proposition2, with proof (10)--(14). The mollifier uses mu(n),
not alpha(n). Proposition2 assumes a polynomial taper p with
p(0)=p'(0)=0, length S^vartheta with vartheta<1/8, and shifts
O(1/log S). Its error is O_epsilon(S(log S)^(-1+epsilon)). The proof
retains six terms, uses the double-zero taper in its Mellin
representation, and factors the mu-specific arithmetic series.
Nomination1393's linear taper and fractional coefficients do not
satisfy these exact premises. Squaring a truncated fractional
mollifier has not been identified with this prescribed mu mollifier;
the coefficient/truncation difference needs an estimate, not a formal
substitution. This does not prove (M2)'s squared-mass requirement.

**Bui--Hall--Subira Jorge**, [arXiv:2511.14415v1](https://arxiv.org/html/2511.14415v1),
18 November2025, Theorem1.1 and its preceding definitions were inspected
as a stronger-result lead. Its coefficients are d_r(n), r positive
integer (with a stated positive-real extension), not reciprocal
fractional coefficients. Its four-amplifier theorem is not a
negative-r substitution rule. It supplies no automatic (M2) import.

### Result of this review and precise boundary

The preserved target remains (M2); neither inequality is derived or
refuted. The first paired mean is sufficiently concrete to test
directly, using C019l's finite real sum and the classical estimates
already assessed in1377. The new twists and their possible resonances
must be analyzed in the future proof attempt. No new original theorem
is needed as a premise merely to formulate this finite-sum test.
Unread Selberg proof cases are parked with that import route; they
are not an essential source blocker for a direct attempt.

The assessed narrower question is exactly the first inequality of
(M2), including actual-P transfer at the B scale. It is recorded in
[continuation1394](2026-11-17-jensen-paired-mollifier-mean-test-1394.md)
and awaits separate approval next turn. The second inequality remains
independent and cannot be inferred from scalar sign density or an
unevaluated twisted-moment formula. Disjoint interval selection,
reciprocal root mapping, bulk separation, the unbounded root deficit
and all-degree positivity also remain open. There is no RH candidate.

This is EXPLORATION: a completed bounded source comparison and a
narrowed actionable test, without a new estimate, refutation or novelty
claim. Mathlib coverage of the full matching result remains unchecked.
No lemma, mathematical script, DAG edge or argument assembly changed.
