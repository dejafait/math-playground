# Centered complete-source residual — completed review1139

TARGET: Assess whether C750g's centered residual r_u-(G_uv/G_vv)r_v admits a cancellation-preserving signed-kernel representation that can support a uniform pivot-area bound for prime P>=101 and 2<=j<P under M_(j+1)>0.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1139 searched centered/source-Gram/signed-kernel and projection/power-function terms; checked C750g, C750c(1)-(8), assessments1134/1135 and the separate-channel stop. No applicable uniform signed-kernel estimate was located; this establishes neither novelty nor impossibility.
SOURCE_EVIDENCE: Reused paper162/v1 Section2(8)-(12), Lemma1/Section7 and Gallier24August2019 Section1 p2/Proposition2.2 p4; directly checked paper162 Sections2/3/7, Santin-Karvonen-Haasdonk DOI10.1007/s10543-021-00870-3 Propositions2.1-2.3/Theorems3.1-3.2 and relevant proofs, Sloan-Kaarnioja arXiv:2308.06052v3 Theorem1/proof and Theorem2, and DLMF5.9.16 with Re(z)>0.
COMPARISON: Projection identities require a specified positive kernel and bounded functional; quantitative rates require additional approximation estimates. No checked source identifies these inputs uniformly for the complete arithmetic cores. Scalar digamma integrals and exact Schur elimination do not supply a joint residual bound.
GAP: No independently boundable signed kernel or estimate for the centered complete residual was obtained. Finite core positivity supplies no established all-mode positive kernel; the original area budget, second contribution, growing cores and Xi realization remain unpaid.
REASON: Complete the source comparison and park this continuation because its admission test was not met. EXPLORE records an unanswered bounded search, not a mathematical obstruction or permission to repeat the pilot. A different support-perturbation target is nominated separately as REVIEW_REQUIRED.
SCOPE: Literature-only comparison of the exact TARGET; no new identity, proof, sample, replay, lemma or mathematical script. This assessment does not cover the different next mechanism.
LITERATURE_REASON: Turn-start REVIEW_REQUIRED lacked essential coverage of centered signed functionals and RKHS/Green-response terminology; the previous Schur and finite-pilot coverage did not assess it.

## Completed comparison1139

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
The intermediate target was a joint representation of the stated
centered residual, potentially pricing one pivot-area contribution.
The test required an applicable estimate or independently boundable
kernel, beyond rewriting the inverse solve. Neither was found.
This does not disprove the representation or the trial inequality.

### Primary statements and comparison

[bramble_trace, paper162](https://rstation.ai/problems/riemann_hypothesis/papers/162),
displayed v1, 15 November2026, Sections2-3/7: the complete sources,
positive-core resolvent lemma, exact elimination and generic
unbounded-area example were checked. Reuse1134/1135 for the earlier
comparison and Gallier's block-inverse input. None estimates the
centered residual at variable P,j or identifies its Fourier sources
with physical boundary evaluations. The fixed-window certificate
supplies no uniform support estimate.

[G. Santin, T. Karvonen and B. Haasdonk, *Sampling based approximation
of linear functionals in Reproducing Kernel Hilbert Spaces*](https://tskarvone.github.io/pdf/BIT2021.pdf),
author PDF, DOI10.1007/s10543-021-00870-3, Propositions2.1-2.3,
pp5-6, give representers, interpolation and optimal-quadrature
projection errors for a continuous strictly positive-definite kernel
on bounded measurable Omega and a bounded linear functional.
The projection proof was read. Theorem3.2, p10, uses a
translation-invariant kernel Fourier upper decay of order tau>d/2,
the bounded interior-cone domain of Theorem3.1, small fill distance,
and |L(f)|<=c_L||f||_(Lq). Its proof uses the sampling inequality,
Sobolev embedding constant and native-norm projection contraction.
No matching kernel, functional bound, node identification or uniform
constants are available here. Thus its rate is not an arithmetic
bound. Proposition2.4 is not used; no Lq contraction for the proposed
centering is assumed.

[I. H. Sloan and V. Kaarnioja, *Doubling the rate — improved error
bounds for orthogonal projection with application to interpolation*](https://arxiv.org/pdf/2308.06052v3),
v3, 30 September2024, Theorem1/proof PDF p6 and Theorem2 p8:
H must embed continuously in L2, B in H, with
|<f,g>_H|<=||f||_2||g||_B and an existing approximation bound M.
The conclusion improves errors using M and ||g||_B; its
orthogonality proof was inspected. Neither quantitative input has
been paid for the arithmetic source. Centering alone does not
provide the required estimate.

[DLMF5.9.16](https://dlmf.nist.gov/5.9.E16), Section5.9(ii),
requires Re(z)>0; C750g's z_x has real part1/4. This scalar input is
applicable to its digamma component. It supplies no bound for the
joint eliminated source or its inverse-dependent coefficients.
No combined representation or integral exchange is derived here.

The source gap is quantitative. M_(j+1)>0 permits the finite inverse
at the nominated index, but supplies no established positive
arithmetic kernel on all modes and supports. A finite native-space
reinterpretation could retain the unknown inverse costs and would
still have to meet P^2(j+1)^5*p_j. No RKHS specialization is approved
by this review. The other area contribution, base area, growing
cores, individual Gram entries, complete middle/residual costs,
odd sector and actual-Xi realization remain independent gaps.

### Duplicate/failure checks and decision

C750g(1)-(7)/Section5 are canonical finite evidence. Its stop1136
concerns separate absolute payments, whereas the signed pilot passes.
C750c(1)-(8) rejects its scalar-floor certificate, not exact inverse
geometry. Paper162's generic example does not refute an actual
arithmetic bound. These stops are not global bans on signed methods.
Assessments1134/1135 already cover paper143/144's inverse-core
mismatch; their long proofs were not reopened. No matching centered
result appeared in the targeted local searches.

External queries included `"Weil" "centered" "source" "Schur" kernel`,
`"Weil" "source-Gram" residual kernel`,
`"Weil" "signed kernel" "source" residual`,
`"displacement" "Schur complement" "reproducing kernel" projection`,
and `reproducing kernel orthogonal projection power function
interpolation error theorem pdf author`. Only primary statements
above count as theorem evidence. Repository import manifests,
aggregator copies and snippets were discovery leads only, not
inspected theorems or cross-notebook inputs. No essential source
access blocker persists; the sought estimate was not found.
Full matching Mathlib coverage is unchecked, not asserted absent.

Park the centered representation route under its admission test.
No larger sample, retuned budget or separate payment is justified.
A different complete-operator energy-relative support comparison is
nominated in assessment1139 as REVIEW_REQUIRED. It retains older
flux/nodal stops; no mathematics for that target is performed or
approved here. Outcome: EXPLORATION; LITERATURE/NOVELTY_UNCHECKED.
This is source coverage and a route decision, not a new bound or
progress beyond checked mathematics. No mathematical exploration
budget is reset. PROOF, DAG, lemmas and scripts are unchanged.

## Original nomination1138 (historical; reviewed above)

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
Use exactly C750g's complete even sources, M_j, G_j, r_j and p_j,
now with variable prime P and the corresponding a=log(P)/2. Core
positivity remains a hypothesis. Require G_vv>0 wherever the displayed
quotient is used. This note defines a proposed observable, not an
identity or estimate proved during the audit.

Plausible downstream use: controlling the centered joint residual
could help price one part of the two-source area while preserving
prime/digamma/exponential/pole cancellation. The remaining area
contribution, growing positive cores, initial area, individual Gram
entries, all middle/residual costs, odd sector and actual-Xi realization
would still be open. No bound for that other area contribution is
silently assumed. Keep the original trial budget P^2(j+1)^5*p_j;
no replacement coefficient, exponent or larger finite sample is proposed.

The next review should search the exact centered complete-source
functional, its possible signed integral/Green-response representation,
known orthogonal-projection/reproducing-kernel terminology, and local
recorded failures. Reuse adequate inspected sources instead of broadly
reopening paper143/144. The generic displacement counterexample,
C750c scalar stop and C750g absolute-channel stop must remain visible.
No cross-notebook theorem is proposed; Mathlib matching is unchecked.

Discriminating source test: retain this direction only if the review
finds either an applicable known estimate or an explicit, independently
boundable joint signed kernel at this support/core scope. A gauge
change, tautological reformulation of the unknown area, standard Schur
update or four separate absolute payments is insufficient. If those
are all that survives, keep the route parked and choose a different
independently testable mechanism. Do not perform a new proof or test
while covering the changed target. A newly prepared ready continuation
will receive separate approval in a later turn.

No mathematical claim, literature approval or originality claim is
made by this nomination. Audit1138 is completed independently of the
success or failure of this future source search.
