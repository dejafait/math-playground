# Positive-diagonal Grunsky finite calculation — assessment1303

TARGET: Test whether c_mn=delta_mn/m-tau*d_m*d_n*S_(m+n) for m,n>=1 and m+n<=6 admits a real normalized formal jet through a_7 with tau>0, d_1=1 and d_2,...,d_5>0, using the covered Grunsky identities and existing rigorous L025/L027 inputs while retaining all exceptional branches.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed review1303 of nomination1302 checked the exact weighted scope against C030y, fixed assessments1250/1251/1253, local variable-coefficient/congruence/realization stops and bounded external prescribed-Grunsky/Hankel queries. No inspected theorem settles this finite weighted prescription; no originality inference.
SOURCE_EVIDENCE: Teo, Lett.Math.Phys.64(2003),75-92, arXiv:hep-th/0305005v2, Sections2.1-2.2(2.3)-(2.4),(2.8)-(2.12), pp2-6, https://arxiv.org/html/hep-th/0305005v2; formal hypotheses, coefficient-comparison proof and formal extension inspected and reused. C030y supplies the audited nine mixed entries including c_24, reciprocal-map convention and jet truncation; L025/L027 supply actual sums, reality, convergence and finite strict signs. Takhtajan-Teo arXiv:math/0406408v1 Section3.1 Theorem3.1/(3.2)/Remark3.3, pp11-13, https://www.math.stonybrook.edu/~leontak/Takhtajan-Teo-II.pdf, supplies only the conditional analytic contraction motivation.
COMPARISON: The general formal identities apply to the weighted real prescription, but C030y's fixed substitutions and contradiction do not cover independent d_m. Source tools cover the finite algebra; actual-Xi compatibility still needs a calculation, and passing it supplies no analytic realization or sign.
GAP: Derive and decide the finite necessary conditions, or preserve the exact undecided conditions and missing rigorous input. All strictly positive weights, tau branches and possible zero jet coefficients must be retained. Higher degrees, analytic extension, univalence and all-degree positivity remain independent.
REASON: One bounded formal specialization can reject this precise representation before global realization work. Essential literature is now covered; this new ready assessment requires separate next-turn approval before research. No weighted equations or feasibility results were derived in the source turn.
SCOPE: Exactly the stated real normalized degree-seven jet and mixed total degree at most six; use existing rigorous actual-Xi inputs only. No extra weights, scale parameters, oddness, univalence premise, independent zero-index data, higher degree, new quadrature/enclosure method or infinite realization construction.

## Known inputs and proposed work

Use the normalized logarithm with constant term zero,

    log((f(z)-f(w))/(z-w))=-sum_(m,n>=0) c_mn*z^m*w^n.

The zero-index coefficients are determined by f. The permitted jet is
f(z)=z+a_2*z^2+...+a_7*z^7+O(z^8), with all a_j real. It is not assumed
odd or univalent. The actual S_k are the reciprocal-zero sums of L025,
not raw theta moments. The strict signs in L027 are unconditional
finite inputs, not an all-degree positivity premise.

Import Teo's identities in the symmetric c_mn normalization. Reuse
only C030y's general nine-entry extraction, reciprocal-map identity,
free exterior constant and truncation proof. Do not reuse its fixed
first-row substitutions or fixed-weight residual equations as though
they applied to the changed prescription. No general Grunsky reproof
is justified. The new work is substitution, elimination and a decided
test for this precise weighted family.

Retain tau>0 and every d_j>0. The boundary tau=0 and zero weights
are excluded hypotheses, not legitimate witnesses. Any division by
other variables requires a separate zero branch. Sampling weights,
symbolic equation counts or floating residuals cannot prove existence
or impossibility. A proposed compatible jet needs exact identities
and rigorous positivity; an impossibility claim must cover every
permitted branch. If existing actual-Xi signs/bounds do not decide a
condition, save it as unfinished reasoning and name the missing input.
Do not introduce an unassessed enclosure algorithm to force a result.

Any mathematical program in the later research turn must write the
complete exact identities, branch conditions and verification residuals
under scripts/grunsky/, printing only the result, actual/required
thresholds, failures and paths. Existing certificates remain preserved;
no such program is written or run by this assessment.

## Use, stopping test and qualifications

A compatible finite jet would justify considering a further explicitly
reviewed realization question. An impossible necessary condition for
all positive weights stops this weighted prescription. An unresolved
condition is neither outcome. The intended downstream interface is
L030's actual Hankel form and the known real Grunsky contraction metric;
no finite test supplies its analytic premise or all-degree conclusion.
L032/C032a's initialization, singular blocks, identification and
realization remain open. C032l's smoothed-law stop and theta-Loewner
stop1200 are scoped contrasts, not inputs to this calculation.

No cross-notebook input. Full matching Mathlib coverage is unchecked.
Routing after separate approval: calculation, standard/high. This is a
finite classical-identity specialization, not proof_attempt/creative.
A decided result absent from the checked sources may be described as
POTENTIALLY_NEW only in that limited sense; pure identity replay is
REPRODUCTION. Neither classification certifies originality.
