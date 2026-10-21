# Fixed-shift response-cell correlation proposal

TARGET: Test the fixed-shift interior-response-cell correlation C_H for a negative log H-scale liminf, retaining the full actual projection and localization errors.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed bounded exact-Wronskian, microscopic shifted-moment and Gram-phase search in drafts/literature/2026-10-08-wronskian-response-cell-signs.md; no matching cell-local theorem was established in those inspected sources, and no novelty is inferred.
SOURCE_EVIDENCE: Kösters arXiv:0803.1141v1 Theorem 1.1/Section 2 https://arxiv.org/pdf/0803.1141v1; Christ–Kalpokas DOI 10.5802/jtnb.836 Proposition 4.1/full proof and Proposition 3.1/contour opening https://jtnb.centre-mersenne.org/item/10.5802/jtnb.836.pdf; Young Lemmas 4–5, (2.1)–(2.3) https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf; reuse audited L381 projection/tail specialization only within its hypotheses.
COMPARISON: Small opposite-height shifts and finite rational twists are known inputs; the fixed nonnegative response-phase cutoff, actual same-cell indicator and complete two-height projection are the identified uncovered difference. Neither a full-dyadic sine kernel nor fixed-angle Gram uniformity evaluates C_H.
GAP: The sign and scale of C_H, every cutoff harmonic contribution, same-cell/endpoint treatment, uniform infinite-tail passage and any implication to J_H remain unproved; no coefficient is guessed.
REASON: One bounded proof attempt can test a localized signed statistic after the global-mass limitation; derive only the stated family-specific difference, cite the known moment inputs, and stop if the full error cannot be separated from the sought signed scale.
SCOPE: Fixed actual F_0,G,A,Wcal from L366/L380; eventual positive simple response zeros and full phase from L372; ordinary real derivatives and H tending to infinity; no RH, F_0 simplicity, noncoincidence, discriminant sign, fourth moment or common-zero-count bound.

The separate literature approval on 2026-10-08 repairs direct source URLs
and approves EXPLORE coverage for this unchanged single test. It does not
approve a correlation value or a localization implication. No mathematical
application has been performed in either literature step.

## Exact single test

Let Φ be the full smooth response phase in L372 (6), so that
G(t)=D(t)cos Φ(t), D(t)>0, and the eventual consecutive positive
response zeros are g_j. Use the exact normalized Wcal of L380.
Set h_H=π/log H, with H>1 sufficiently large for L372's eventual ray.

Fix the following π-periodic nonnegative smooth cutoff. For the
representative x∈[−π/2,π/2) of its argument, put
y=8(x+π/4)/π and define

    χ(x) = exp(1−1/(1−y²))  when |y|<1,
           0                otherwise.

Thus the specified cutoff is supported in [−3π/8,−π/8] modulo π.
This is a definition of the proposed statistic, not an estimated phase
window or a claim about its correlation. Define

\[
C_H=\frac1H\sum_{[g_j,g_{j+1}]\subset[H,2H]}
\int_{g_j}^{g_{j+1}}
\mathbf 1_{\{t+h_H<g_{j+1}\}}
\chi(\Phi(t))\,\mathcal W(t)\mathcal W(t+h_H)\,dt.
\]

The indicator retains the exact same open response cell; endpoints of
the integration have measure zero. Do not substitute a Gram cell or
include opposite signs separated by a response zero. The proposed
threshold is

    liminf as H→∞ of C_H/log H < 0.

No threshold value or existence claim is made. A later proof must
justify the passage from a negative C_H to opposite signs inside one
open cell and to the J_H diagnostic in the preceding assessment.
A rigorous smaller-scale negative value at unbounded heights would
also be relevant, provided its complete error is smaller still.

## Permitted inputs and bounded stopping rule

Essential input IDs: L366, L368, L372, L380, L381, L382.
L373 is an obstruction comparison. Reuse L381's finite-head
complex-shift jet input by the precise Young citation, its holomorphy
qualifications, and complete right-line norm bounds where applicable.
Reprove neither Young nor the global signed-mass result. Read the
remaining relevant L381 proof ranges before applying those inputs.

The one attempt may separate a finite Fourier approximation to χ
from its remainder, keep the full two-height real projection and exact
response Euler phase, and test the resulting signed leading term.
Every Fourier remainder, rational-frequency collision, critical-line
jet error, response-phase approximation, endpoint contribution and
infinite-tail limit needs a bound at the actual claimed scale. A fast
harmonic is not a Young weight. L381's unweighted contour argument
does not license discarding new carrier harmonics; their stationary
and boundary cases must be retained or shown to block this test.
Replacing the indicator by one is also a separate applicability
obligation, not a convention.

Continue only if the complete signed statistic is negative with a
dominated error at unbounded heights, or a rigorous obstruction changes
the decision for this fixed test. Stop this implementation if it is
nonnegative, a leading harmonic or tail stays uncontrolled, the error
reaches the claimed negative margin, or successful application requires
RH/common-zero assumptions. Save that failure without expanding the
shift/cutoff search in the same attempt. This is one fixed diagnostic,
not approval for arbitrary phase windows, higher moments or a new
common-zero count mechanism.

Main gap: global actual-theta mixed positivity and the total L367
margin. Plausible downstream use: a sign-changing Wronskian zero in a
common-free response cell. This would still leave discriminant sign,
common-zero counts, global positivity, low indices, heights above forty
and endpoint margin unresolved. Matching Mathlib coverage is **not
checked**. A later specialization is intended as REPRODUCTION; this is
not a claim of mathematical novelty or an RH candidate.

## Separate direct-source recovery and approval — 2026-10-08

All three URLs above were opened successfully. Reused the bounded search
and proof-case comparison in the preceding assessment; no broader search
was needed because the target and hypotheses are unchanged.

Rechecked [Young](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
printed pp. 540–543: (2.1)–(2.3) require a nonnegative bounded smooth
weight supported in [T/4,2T], with derivative scale T/log T. Lemma 5
requires positive integer h,k with hk≤T^(2θ), θ<1/2, and complex
shifts O(1/log T). Its proof retains both functional-equation sums;
off-diagonals use repeated integration by parts and both frequency
orderings. L381 uses scale T=2H for fixed heads. The new microscopic
cutoff is outside the cited weight conditions. This review grants no
new uniform jet, Fourier-harmonic or indicator estimate. Singular
auxiliary shift denominators still require L381's holomorphic treatment.

Rechecked [Kösters](https://arxiv.org/pdf/0803.1141v1),
v1, Theorem 1.1, printed p. 3: real fixed shift parameters, opposite
critical-line heights, full dyadic averaging, continuous coincident-shift
value. Reuse the already inspected Section 2 proof cases; no derivative
or response-cell version is imported.

Rechecked [Christ–Kalpokas](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.836.pdf),
published version, Proposition 4.1 and complete proof, printed pp. 301–302:
nonnegative real k, nonnegative integer l, sufficiently large T and
monotone ordinary theta. The phase-averaged identity includes incomplete
endpoint intervals by the same change of variables. It supplies no
signed two-height estimate. Proposition 3.1's constant-phase comparison
remains reused from the preceding review; no further part is imported.

Decision: approve precisely the saved EXPLORE target for a later bounded
mathematical attempt, with the original continuation/abandonment test
unchanged. The local duplicate/failure check reuses the preceding
assessment and its history entry; the first-mean stop is also confirmed
in ATTEMPTS/2026-10-08-wronskian-first-mean-signing.md. This source repair
adds no mathematical evidence and is reported STALLED, rather than an
advance or informative negative result. Mathlib matching coverage remains
not checked. All listed unresolved assumptions and independent gaps remain.
