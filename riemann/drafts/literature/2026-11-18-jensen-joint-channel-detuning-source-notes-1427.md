# Joint-channel detuning — source comparison1427

18 November 2026. Literature-only review of nomination1426's unchanged
TARGET. Decision: EXPLORE, subject to separate approval before research.
No cancellation, common-frequency identity, new bound or lemma is derived.

The main gap is L030--L032/C032a actual-Xi all-degree positivity. The
intermediate target is the joint unequal-product cancellation specified
in assessment1426. Its plausible use is to pay part of the full reference
numerator before the fixed-quotient cBq^2 versus O(B) test. Independent
denominator, UA, actual-P residual and actual-Xi transfer gaps remain.

Read C020e (1)--(7), C020f (1)--(6) and its inherited phase/tail check,
C019y (1),(3)--(5) with audit1421 of those finite identities only,
C019's scales/heat bounds and C020c's two exact translated domains.
Reuse source-notes1410/1418/1422/1425. Read stops1416/1426 and retain
their scoped conclusions. C019y's selected-slice estimates and C020a/b
are not premises. This source review is not an audit of C020f.

Targeted duplicate searches in the 17--18 November Jensen literature
assessments and ATTEMPTS found the joint nomination, but no completed
joint-channel assessment or comparison with arXiv:1811.01130. This is
a bounded local search, not a novelty conclusion. Existing work is
preserved; no cross-notebook input is used.

## Bounded searches and source scope

Queries actually used:

- `Riemann Siegel formula sharp cutoff complementary Dirichlet sums endpoint stationary phase Gabcke theorem`
- `twisted second moment approximate functional equation off diagonal cancellation dual sum sharp cutoff heat weights`
- `weighted approximate functional equation general Dirichlet polynomials Riemann Siegel moving weights complementary sums`
- `"Riemann" "heat" "mollified" "moment" cancellation`
- `"twisted" "second moment" "sharp" "complementary"`
- `"Riemann-Siegel" "weighted" "Poisson" cancellation partial sums`
- `"approximate functional equation" "Gaussian" "log" "weights" zeta`

These located the primary comparison below, but no matching theorem for
the coupled heat-weighted observable. Snippets, numerical descriptions,
secondary mirrors and unrelated moment papers are not mathematical
evidence. Recent fractional-summand and Gram-cloud papers were search
leads only: their theorem statements/proofs were not inspected or used.
The search is bounded; it establishes neither novelty nor impossibility.

**Cormac O'Sullivan**, *A generalization of the Riemann-Siegel formula*,
[arXiv:1811.01130v2](https://arxiv.org/html/1811.01130v2), 19 April 2019
(paper dated 18 April). Read Theorems 1.1--1.2, 1.5/(1.18)--(1.21),
Theorem 2.1, and Section 2.1 through Proposition 2.2's complete proof.
For s=sigma+it, sigma in a fixed finite real interval I, t>=2pi,
alpha,beta>=1 and t=2pi*alpha*beta, Theorem 1.1 gives

\[
 \zeta(s)=\sum_{j\le\alpha}j^{-s}
       +\chi(s)\sum_{j\le\beta}j^{s-1}
       +O_I(\alpha^{-\sigma}+t^{1/2-\sigma}\beta^{\sigma-1}).
\]

Theorem 1.5 gives the symmetric remainder's explicit Mordell expansion
(1.21), including both fractional cutoffs. For N>=0 its error is

\[
 O_{I,N}\left(t^{-N/2-1/4}\lambda^{1/2-\sigma}
                    (\lambda+\lambda^{-1})^{3N+1/2}\right),
 \qquad \lambda=\sqrt{\alpha/\beta}.
\]

Section 2.1/(2.8)--(2.10) retains the residue sum and contour correction;
integer beta requires a rightward contour displacement. Proposition 2.2
separately handles alpha>=10 and 1<=alpha<=10. These are ordinary
unweighted zeta sums; neither theorem states a weighted arithmetic
cancellation estimate.

**Local comparison, not a specialization:** N(Z) is the specified
heat-dependent floor, and E_j(Z) depends quadratically on log j.
No theorem above identifies the two heat-weighted channels with the
two ordinary partial sums. To use this source one would have to justify
the weights, the gamma phase versus the reference theta, and every
cutoff/boundary and outer-summation error. Conjugate symmetry of an
ordinary zeta formula supplies no negative relation between these
channels. Merely replacing E_j by 1 or replacing N(Z) by the ordinary
Riemann-Siegel cutoff is outside the target. The displayed source
correction must not be silently identified with C020e's lattice
endpoints or with its whole retained near layer.

**Bettin--Chandee--Radziwill**, *The mean square of the product of the
Riemann zeta function with Dirichlet Polynomials*,
[arXiv:1411.7764v1](https://arxiv.org/html/1411.7764v1), 28 November 2014;
the generated HTML's 2026 display date is not a source revision.
Reuse Theorem 1's hypotheses/error in source-notes1410. Rechecked
Lemma 1 and Section 3.1/(3.1), Section 3.2 from gcd extraction through
Case 1's final diagonal/zero-mode assembly, and the openings of Cases
2--3. Lemma 1 requires an entire even G, rapidly decaying on vertical
lines, G(0)=1, G(1/2)=0. For T<t<2T it writes ordinary |zeta|^2 as
twice a double sum with Mellin weight
W(x)=(2pi i)^(-1) integral_(2) x^(-w)G(w)dw/w, plus O(T^(-2/3)).
Its proof is referred to LR Lemma 3, not newly inspected here.
Case 1 combines the diagonal and progression-Poisson zero mode via
the zeta functional equation and even G, leaving a residue main term.
Large modes use smooth integration by parts; small nonzero modes use
Mellin separation and Kloosterman estimates. This is not automatic
vanishing of the complete off-diagonal sum.

**Local comparison, not a specialization:** the common Mellin weight,
fixed smooth height test, and ordinary zeta observable have not been
obtained for C020e plus C019y's U-conjugate(A) contribution. The target
has two own-time heat factors for each source pair, four prescribed
tapers, prime-window witness, and sharp shifted entries. BCR's
diagonal/zero-mode relation does not identify a counterpart to C020f
(6) inside the present full U-conjugate(A) channel. Polarization or
smoothing would require a separately justified identity and a paid
error. The source's ordinary error cannot simply be assigned to this
new observable. No source theorem or proof is imported into a lemma.

## Reused coverage and precise handoff

Source-notes1422's Evertse finite-Poisson theorem retains endpoint
corrections, with C020e providing its local finite tail calculation.
Source-notes1425's Kıral--Petrow--Young smooth interior theorem and
Vandehey finite-interval identities remain tools, with their original
smoothness/nonstationarity hypotheses. Source-notes1418's BCR and
Bettin--Chandee comparisons still require the correct inverse phase,
coprimality strata and separated weights. None pays a different
coupled sum merely because both channels occur in the same numerator.
No extra browsing of those ready assessments is needed.

**EXPLORE:** essential source access succeeded and the theorem-level
comparison is complete for one bounded common-frequency test. The
literature supplies transformation methods, not the target estimate.
The missing object is an exact local matching and signed arithmetic
payment; it is not an inaccessible theorem being assumed. No full
matching Mathlib theorem was checked; unknown coverage is not absence.

After separate approval, start from C020e (1)--(5), C020f (1)--(7)
with its phase/tail/bound uses checked, and C019y (1),(3)--(5) only.
C019's audited scales, coefficient/heat bounds and C020c (4)--(5)
fix the two translated domains. First identify, without deleting
tuples, the proposed counterpart in the full U-conjugate(A) channel,
its orientation, conjugation, exact weights and domains. C020f (6)
defines a mixed layer; it is not yet a common layer of the two
channels. A similarly named rational frequency is insufficient.
Grouping must retain unmatched terms, multiplicities and common
factors as well as equality terms separately. No such grouping is
proved in this review.

Continue only if this gives a valid complete coupled estimate at
o(Bq^2), with every localization error paid and both boundaries intact,
or a precisely identified mismatch/residual that discriminates this
implementation. If support or weight matching fails and its cost is
unpaid, stop this implementation and preserve the exact residual.
Do not promote a failed absolute bound to a signed lower bound, or
rename C020f (6) as a cancellation result. No uniform rapid decay
follows merely from lns!=vr; stop1426 already explains that point.

Retain positive/negative/zero dual modes, full lattice endpoints,
both shifted bands and n-entry indicators, each source's own heat
time, integer d, alpha, four tapers, floors and all common-factor
cases. No coprimality or nonvanishing assumption may be inserted.
Exact resonance evaluation and the rest of the mixed modes/endpoints,
UA, denominator and E_P remain independent unpaid obligations. Actual-P
use still retains C019t's C019j/k/l/s,L320,L018/L021 contracts.
C019y's selected-slice estimates and C020a/b remain uncertified and
are not inputs. No RH-equivalent sign premise or candidate is introduced.

This proposed next attempt develops standard complementary-sum and
finite-transform methods. No justified creative/max mechanism is yet
specified: the common-frequency map, its sign and its weight transfer
are unproved, and the inspected sources supply no new cancellation
principle beyond that development. This is the blocker to a creative
nomination within the unchanged gate-approved target, not a global ban.
Further inconclusive repetition requires materially new input or a
refined mechanism. The present literature EXPLORATION spends no
mathematical exploration turn and resets no recovery/exhaustion counter.
PROOF.md and DAG.md remain unchanged because the argument has not changed.
