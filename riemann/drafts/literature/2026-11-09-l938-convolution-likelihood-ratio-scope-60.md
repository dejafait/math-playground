# Integrated positive/negative convolution ratio — completed source review

TARGET: Assess convolution likelihood-ratio coverage for monotonicity of L938's positive-row sum divided by its negative-row sum on E>0.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step61 searched likelihood-ratio/convolution/log-concavity/TP2/mixture terminology and exact Riemann-theta variants; compared primary texts below with L938(5)-(10), its step50 audit and the recorded L940/L941 stops. No inspected theorem proves the actual mixture order; this is not a novelty claim.
SOURCE_EVIDENCE: Dümbgen–Mösching arXiv:2209.07868v3, Theorem1 and complete proof pp2–3,11–12, Theorem13/Remark16 pp6–7; Yu arXiv:0909.4570v1, Theorem1 and full proof pp2–3; Saumard–Wellner arXiv:1404.5886v1, Proposition2.3, Theorem6.1, and Theorem6.8 with proof pp32–34. Exact links and access limits below.
COMPARISON: General ratio/ordered-mass equivalence is available without endpoint smoothness, but convolution and conditional-monotonicity sources require extra shape/order hypotheses. Neither positivity of twelve factors nor arbitrary mixing supplies them. Existing zero-energy cancellation and the negative first-cell mass motivate a smaller compatibility test before global mixture analysis.
GAP: No actual V_plus/V_minus monotonicity, denominator theorem, ratio limit, relative log-concavity, ordered row family or mixing-weight order is established here. The proposed endpoint compatibility test remains unperformed; density crossing and RH gaps persist.
REASON: One bounded literature-only review found a directly usable order diagnostic and isolated a concrete endpoint test; automatic convolution/mixture import is unsupported. A separate ready continuation is nominated for next-turn approval, without deriving its outcome now.
LITERATURE_REASON: Startup target was REVIEW_REQUIRED and had no primary likelihood-ratio coverage; the ready step46 Laplace assessment covers only the downstream zero-count implication.
SCOPE: Source comparison only. No new mathematical conclusion, lemma, script, DAG edge or PROOF assembly. The original nomination below is historical; these completed fields supersede its pending-review language.

This continuation is newly written and requires its own next-turn
literature approval. It does not change acceptance of the completed
L941 audit. No new lemma, ratio identity, mathematical calculation or
source import is part of this nomination.

The proposed objects use exactly L938(6)-(9):

    V_plus(E) = sum_(c_alpha>0) c_alpha h_alpha(E),
    V_minus(E) = sum_(c_alpha<0) (-c_alpha) h_alpha(E).

The proposed sufficient property is increasing V_plus(E)/V_minus(E)
for E>0. It is a target, not an assumed theorem. Every row retains its
twelve labelled factors, zero exponents, factorials and M_0^12
normalization. The actual theta K is fixed. The review must check the
denominator, support and regularity before using a ratio or derivative.
It must not infer a convolution likelihood-ratio theorem from positivity,
apply a common-kernel theorem to unmatched factors, or assume closure
under arbitrary positive mixtures. The singular f_0 endpoint requires
explicit attention. No global balancing or pointwise Schur property
is a premise.

Plausible use: a justified actual-law monotonicity statement, with all
endpoint and nonvanishing qualifications, could supply the remaining
density crossing premise in the previously assessed Laplace zero-count
route. Parameter endpoint signs, contacts, other degrees, initialization,
realization and global continuation would still be independent gaps;
L030-L032/C032a actual-Xi mixed positivity remains the main goal.

The next source comparison should reuse
`drafts/literature/2026-11-09-actual-h2-signed-convolution-discovery-45.md`
only for its covered Laplace step. That record identifies generic
Stein/contact/derivative-sign failures; compare their exact scope before
proposing a technical test. L940/L941's canonical stops must remain
preserved. No matching full theorem or absence of one is claimed by
this nomination. Mathlib coverage is unchecked.

Continue only if inspected primary hypotheses cover the actual mixture
or isolate one concrete, independently falsifiable missing order
condition. Abandon an automatic convolution import if its common-kernel,
mixture or endpoint assumptions fail without a new justified mechanism.
Any proposed finite test must receive explicit scope coverage before
execution. Unread leads do not constitute approval; an essential source
blocker should be recorded rather than repeatedly revisiting balancing.

## Completed comparison — 9 November 2026, step61

### Primary order diagnostic

Lutz Dümbgen and Alexandre Mösching, *On Stochastic Orders and Total
Positivity*, ESAIM: Probability and Statistics27 (2023),461–481,
DOI10.1051/ps/2023005; inspected author version
[arXiv:2209.07868v3](https://arxiv.org/pdf/2209.07868v3), dated8 March2023.
Theorem1 (printed pp2–3) concerns arbitrary probability measures:
likelihood-ratio order is equivalent to ordered-set cross-product mass
inequalities. Read its complete proof, pp11–12, including zero-density
cases, integration and construction of density versions. Theorem13 and
Remark16 (pp6–7) connect conditional order with TP2; that condition
must already hold. They do not confer order on arbitrary mixtures.

For later application, each proposed positive measure must first have
finite nonzero total mass. Normalization constants and ratio orientation
must be retained. Theorem1 requires no endpoint derivative. It provides
a diagnostic, not the unproved actual order. This turn imports no
actual-law conclusion and gives no reproof.

### Stronger shape-based endpoint criterion

Yaming Yu, *Stochastic Ordering of Exponential Family Distributions and
Their Mixtures*, J.Appl.Prob.46 (2009),244–254,
DOI10.1239/jap/1238592127;
[arXiv:0909.4570v1](https://arxiv.org/pdf/0909.4570v1),24 September2009.
Read Theorem1 and its full proof, printed pp2–3. It assumes continuous
densities supported on (0,infinity) and a continuous concave log density
ratio l=log(f/g). Its likelihood-ratio/reversed-hazard equivalence and
left derivative criterion additionally require l continuously
differentiable. The proof uses concavity for the sign interval and
derivative monotonicity, treating both directions. It does not infer
concavity from positivity or convolution. This criterion is unavailable
for the actual two mixtures until its shape premise is proved.

### Convolution and conditional monotonicity

Adrien Saumard and Jon A.Wellner, *Log-concavity and strong log-concavity:
a review*, Statistics Surveys8 (2014),45–114,
DOI10.1214/14-SS107;
[arXiv:1404.5886v1](https://arxiv.org/pdf/1404.5886v1),24 April2014.
Read Proposition2.3 (pp4–5), Theorem6.1 (p27), and the authors' alternative
proof of Theorem6.8 in Section6.4 (pp32–34). PF2/translation-ratio
characterization requires log-concavity. Efron's theorem requires
independent log-concave variables and a coordinatewise nondecreasing
observable with defined expectation. The new proof smooths within the
log-concave class before differentiating and applying a covariance bound.
Neither independence alone nor a signed quotient observable meets these
hypotheses. Smooth approximations do not establish an omitted shape
premise for the original singular factors.

### Exact comparison with the notebook

Read L019's full kernel proof and L938's definitions, all34 rows,
equations(5)–(10), constant-kernel cancellation, first-cell enclosure,
arithmetic qualifications and complete step50 audit account. L938
already supplies continuous twelve-factor convolutions, no atom at zero,
absolute exponential moments and an integrable simplex majorant. It
does not state the strict denominator or the ratio's origin limit.
Those require an explicit applicability argument in the next attempt.

Every row retains twelve factors, including its zero indices, factorials
and M_0^12 normalization. Individual f_0 is singular at the origin;
continuity of the integrated density does not license differentiating
individual factors there. A common positive K does not supply a common
convolution kernel for two unequal row laws. A factor-level order, even
if checked later, would still require a valid convolution theorem and
an independently verified rule for the two finite mixtures. The
coefficient signs are not an ordered mixing parameter. None of these
missing premises is inserted here.

Reuse the step46 assessment only for the already-inspected Laplace
zero-count step. Read the step58 ATTEMPTS record: L941 refutes inward
closure of a pointwise sign set. L940's Schur obstruction is a separate
pointwise stop. Neither settles an integrated ratio. The old generic
Stein, derivative-sign and contact obstructions remain contrasts from
the reused assessment, not mathematical inputs. No sibling notebook
or cross-notebook result was used.

The exact existing cancellation and B_0<0 suggest checking endpoint
compatibility first. This is a nomination: no ratio limit or
incompatibility has been derived or accepted here. It is materially
different from another balancing ray and needs no larger grid.

### Search record, access limits and decision

Queries included `likelihood ratio order convolution log concave mixtures
preservation total positivity theorem`, `Dumbgen Mösching likelihood
ratio order total positivity convolution mixture conditional distributions`,
`Shaked Shanthikumar 1.C.9 logconcave convolution`, `likelihood ratio
order mixtures 1.C.17`, and `Riemann theta convolution likelihood ratio`.
The scoped local search covered the saved ratio nomination, step46
assessment, current L938 history and relevant H2 ATTEMPTS records;
no duplicate endpoint-ratio result was found in those inspected paths.
This bounded search establishes no claim of originality.

Shaked–Shanthikumar (2007), Theorems1.C.9/1.C.17, remains an unread
book lead: the indexed book mirrors timed out or were inaccessible;
shell retrieval failed at DNS resolution. Xu–Balakrishnan (2011),
J.Appl.Prob.48,877–884, DOI10.1239/jap/1316796922, quotes the
convolution theorem in its Bernoulli proof; that quotation is not a
substitute for inspecting the general theorem. Albabtain et al.,
Entropy22(8) (2020),843, DOI10.3390/e22080843, Theorem4, is an
additional mixture lead: introductory primary text and indexed theorem
extracts were accessible, but complete primary proof retrieval was
blocked by429/recaptcha/access errors. Its proof has not been inspected
and is not an input. Park both leads rather than repeat access work.
No essential source blocker remains for the independent endpoint test.

Decision EXPLORE: sufficient standard coverage for a bounded diagnostic,
no full theorem matching the actual mixture, and no mathematical
advance or informative actual-law negative result yet. Nominate
`2026-11-09-l938-ratio-endpoint-compatibility-scope-61.md` for separate
approval. Continue only if the exact endpoint/first-cell comparison
can be settled under retained hypotheses; a contradiction retires only
global nondecreasing-ratio sufficiency. No global crossing theorem
would follow from passing this test. Full/supporting Mathlib coverage
is unchecked, not asserted absent.
