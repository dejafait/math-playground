# Fixed actual-Jensen pair — squared-mass coverage1402

TARGET: Test the O(B) squared-mass bound for C019r's fixed actual-Jensen weighted pair, including every moving-heat channel and the actual-P transfer.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused review1394/source-notes1394 and ready1377; six additional exact fractional/fourth/eighth-power searches are recorded in source-notes1402. No matching theorem was located in this bounded search; this is not a novelty conclusion.
SOURCE_EVIDENCE: Reopened BBLR arXiv1609.02539v1 Theorems1.1-1.2 pp2-4, six-term and holomorphy remarks p3, Section2.4 pp8-12; Bui-Hall2304.05178v1 Proposition2 and proof (10)-(14); Gonek-Ivic1604.00517v1 (2.8)-(2.9). Inspected Baluyot's author-hosted 52-page criticalline.pdf definition(1.4), Theorem1.3 p4 and following taper discussion p5. Direct URLs and scope below; ready1377's inspected classical tools are reused.
COMPARISON: Ordinary shifted fourth-moment formulas do not evaluate this moving-heat moment. Their arbitrary short twists accommodate an ordinary finite-polynomial comparison, but heat/floors and the fractional linear-taper arithmetic remain unproved specializations. Mu-mollifier formulas cannot replace them.
GAP: Establish or refute the exact O(B) bound below; all quartic heat channels, resonant/stationary arithmetic, endpoints and squared-mass actual-P transfer are unpaid. C019r's W-weighted single squares are a different moment.
REASON: The sources and elementary finite-sum tools support a bounded direct attempt without the parked historical Selberg import. No theorem matching the full observable was found, and no required inaccessible source is used as a premise. This assessment permits testing, not assuming, the bound; separate next-turn approval is required before research.
SCOPE: Exactly C019r/C019m P,T,d,X,q,B,h,D,V,M,W; every sufficiently large integer d; L=floor(X^(1/1000)), unchanged alpha and linear taper, own heat times and true floors; no RH/random-law/nonvanishing assumption.
LITERATURE_REASON: This is the independent squared pair moment excluded by ready1398 and narrowed review1394. The additional searches check stronger single/fractional fourth-moment coverage and a newly surfaced taper warning, rather than reopening the retained mean.

## Exact target, existing inputs and downstream gap

Keep nomination1401's proposed inequality, with no change of observable:

\[
 Q_d(Y)=P(Y)P(Y+h)W(Y),\qquad
 \int_D Q_d(Y)^2\,dY
 =\int_D P(Y)^2P(Y+h)^2|M(Y)M(Y+h)|^4\,dY\le C B
 \quad(d\ge d_0),
\]

where C and the integer onset d_0 are absolute. The definitions and
positive gamma normalization are canonical in C019m/r; the finite
reference V is C019m (7), also C019p (1). In particular h=3*pi/q,
q=log X, D=[X,sqrt(2)X-h], and B=(sqrt(2)-1)X. Alpha is defined by
the Euler-product branch of zeta(s)^(-1/2) on Re(s)>1 only. It is
not a reciprocal evaluated on the critical line.

The retained C019r mean <=-B/2 makes this moment relevant to quantitative
opposite-sign density. That use, disjoint ordered intervals, reciprocal
root mapping and separation from existing bulk roots remain later
obligations toward the unbounded Jensen deficit and actual-Xi
all-degree positivity L030-L032/C032a. No density implication or new
bound is derived during this literature step.

Local input scope: C019r and C019l/p/q, with C019m and inherited
C019j/k,L018/L021. Existing mean reductions are not quartic formulas.
C019m (19) with (8) supplies sup_J|P+V|=O(1/q); C019r (2) bounds
integrals V(Y+j)^2 W(Y), not V(Y)^2 V(Y+h)^2 W(Y)^2. Its relative
mean transfer o(BqA) likewise is not a squared-mass transfer. Neither
an O(B) quartic error nor sufficient higher weighted error norms are
available merely from that uniform comparison.

## Primary comparison and exact boundary

**BBLR**, [*A quadratic divisor problem and moments of the Riemann
zeta-function*, arXiv:1609.02539v1](https://arxiv.org/pdf/1609.02539),
8 September 2016, Theorems1.1-1.2 pp2-4: four ordinary zeta factors,
shifts O(1/log S), twists of length S^vartheta with coefficients
O_epsilon(n^epsilon), smooth Phi supported in [1,2] with
Phi^(j)<<_j S^epsilon. Error:
O_epsilon(S^(1/2+2vartheta+epsilon)+S^(3/4+vartheta+epsilon));
vartheta<1/4 gives a power saving. All six terms matter: original,
full dual, and the four one-pair exchanges. Only their sum extends
holomorphically across colliding shifts. Section2.4 pp8-12 retains
near-diagonal unequal products and pairs dual contour contributions;
discarding them is unjustified. These hypotheses do not contain
moving heat or hard source floors. Source height S would be comparable
to X, not the notebook's T. The prospective ordinary twist is
(M(Y)M(Y+h))^2 of length L^4, so length alone is not the issue;
its main terms still need evaluation. No application is imported.

**Bui--Hall**, [*On the derivatives of Hardy's function Z(t)*,
arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1),
11 April 2023, Proposition2 and proof (10)-(14): coefficients mu,
polynomial taper p(0)=p'(0)=0 (normalized p(1)=1 in the definition),
vartheta<1/8, shifts O(1/log S),
error O_epsilon(S(log S)^(-1+epsilon)). The proof starts at taper
degree two and uses a mu-specific arithmetic factorization. Our
linear alpha taper meets neither restriction. Squaring its finite
truncation is not an identification with the source's prescribed
mu mollifier. This excludes a direct citation, not the proposed bound.

**Baluyot**, [*On the zeros of Riemann's zeta-function on the critical
line*, author-hosted PDF](https://sieg-baluyot.github.io/criticalline.pdf),
52 pages, accessed 17 November 2026; no version date identified.
Definition(1.4) uses mu and a squared logarithmic taper. Theorem1.3
p4 has 0<theta<1/22, fixed real a, rho=2a/log(S/(2*pi)), smooth
nonnegative w supported in [S/2,4S], w^(j)<<_j S_0^(-j),
S^(1/2+epsilon)<<S_0<<S. It gives the ordinary shifted fourth
moment with |M|^4 and errors O(W/log S) and
O(y^(11/2)S^(3/4+epsilon)(S/S_0)^(9/4)), W=integral w.
The p5 discussion reports a W log S main term with a linear taper;
that variant's proof was not inspected. This warning is not a
counterexample for our fractional coefficients, eighth total
mollifier power, moving heat and prescribed pair. No theorem or
growth obstruction for our target is imported from it.

**Gonek--Ivic**, [arXiv:1604.00517v1](https://arxiv.org/html/1604.00517v1),
Lemma3 proof (2.8)-(2.9), is reused from review1394: an ordinary
paired second moment with fractional coefficients. It gives no
squared-pair theorem. The underlying unread Selberg Lemma15 remains
parked and is not an essential premise of the direct test. The prior
positive-amplifier comparison in review1394 is also unchanged.

## Bounded permitted attempt and stopping test

A later attempt may start with the exact finite V and weight, retaining
every conjugate/nonconjugate quartic channel and its actual entry
domain. It may use ready1377's inspected classical estimates:
H. Koesters, [arXiv:0803.1141v2, Appendix A](https://arxiv.org/html/0803.1141v2#A),
5 September 2008, A.1-A.3 (=Titchmarsh, second edition,
Lemmas4.2,4.4,7.2). A.1 requires monotone real F' separated from
zero and gives 4/epsilon; A.2 requires real F'' of one sign with
|F''|>=epsilon and gives 8/sqrt(epsilon); A.3 is the ordinary
integer sum of 1/(sqrt(mn)log(n/m)), m<n<=R, bounded by O(R log R).
Variable amplitudes need paid variation. Quartic near-resonances,
stationary points and rational twists do not automatically meet
these hypotheses or inherit C019p's pair error exponent.

This is EXPLORE for a direct finite-sum development. No automatic
ordinary-to-heat transplant, Gaussian averaging theorem, infinite
coefficient identity at the critical line, factorization of correlated
moments, arbitrary-twist A.3, or uniform effective onset is approved.
If an ordinary-source approach is used, it must pay smoothing,
coefficient and heat comparisons rather than citing the final formula
for the wrong integrand. A stronger single-factor moment may be tested
as an upper-bound method, but it must not replace the saved target or
make failure of that stronger method a refutation of the target.

The discriminating evidence is a proved O(B) bound with all reference
and actual-P costs paid, or a rigorous incompatible growth lower bound
for this exact observable. A logarithmic loss in an upper estimate,
an unevaluated six-term formula, the taper warning for another
mollifier, or failure to pay a transfer is not a disproof. Preserve
the first unpaid term if inconclusive; repeating an unsuccessful
attempt requires materially new input or a refined test. No mathematical
attempt on this M2 target has been performed in this review.

Stops1345/1355/559/1387/1391 and parked(A) retain their original scopes.
None proves that this different full arithmetic squared moment fails.
No cross-notebook input is used. Full matching Mathlib coverage remains
unchecked; supporting inequalities are not a formalization of M2.

Separate approval of this newly written assessment is the next turn.
After that, the supported route is proof_attempt/development: a
difficult quartic extension of the established finite-sum route, not
an already established specialization or a distinct creative mechanism.
The prescribed review has identified no separate source-supported
creative mechanism to nominate; source and quartic-transfer differences
must be tested rather than inventing one for scheduling. No lemma,
mathematical script, argument assembly or DAG changes occur here.
