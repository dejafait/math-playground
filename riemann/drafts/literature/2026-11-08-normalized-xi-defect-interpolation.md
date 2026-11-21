# Normalized Xi-defect measure interpolation — source comparison

TARGET: Assess primary coverage for an explicit degree-independent bound integral_R2 |W_y/A_0(y)-W_v/A_0(v)| <= M |y^2-v^2| for 0<=v,y<=1/2, with M finite and justified from the actual theta kernel.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact Xi/sinhc/total-variation and defect-kernel/Lipschitz searches found no matching Xi estimate; normalized-density stability searches located Sprungk's primary theorem, and scalar searches led to NIST DLMF. Scoped local checks found L898's fixed-endpoint stop and L309/L312's distinct ordering comparison, not this norm bound. No novelty is inferred.
SOURCE_EVIDENCE: Sprungk, arXiv:1906.07120v3 (22 January 2020), Sections2-3 Theorem8 and AppendixA equation(13); NIST DLMF version1.2.8, equations4.36.1/4.36.3, 4.33.1 and 25.6.1. Exact hypotheses and relevant normalization proof passages were inspected; details below.
COMPARISON: Quantitative normalization stability is known; the remaining work is a bounded actual-theta specialization of its potential hypotheses in the parameter y^2. The sources do not state the displayed Xi estimate. L898's parity-separated obstruction and L312's qualified oscillatory-ordering failure do not settle this full-density norm question.
GAP: Prove the scalar uniform difference estimate including zero, verify the chosen reference measure and every potential/normalization hypothesis, and obtain an explicit finite theta-integral M. No local Xi measure bound, numerical value, independent sign margin or all-height relative estimate is established in this review.
REASON: Primary coverage now identifies a precise bounded specialization with no essential source blocker. Import the general stability theorem; prove only its stated local applicability and scalar/constant calculation in a separate approved research turn.
LITERATURE_REASON: The changed normalized-measure dependence target lacked essential source coverage at invocation start; this turn completes that comparison rather than reopening the fixed-endpoint audit.
SCOPE: Actual Phi=K(|u|)/2 and W_y,A_0(y) of L898; full L1 distance, all 0<=v,y<=1/2, including both endpoints; finite explicit moment expression allowed. No RH, cosine-ordering sign, finite certificate or positive frequency margin is assumed. No new lemma or mathematical script was written.
COVERED_TARGET: Specialize Sprungk's total-variation stability theorem to prove the normalized Xi-defect measure bound in |y^2-v^2| on 0<=v,y<=1/2 with an explicit finite theta-integral constant M, including y=0 and the full-L1 normalization factor.

## Primary quantitative input

Björn Sprungk, *On the Local Lipschitz Stability of Bayesian Inverse
Problems*, Inverse Problems 36 (2020), 055015,
[arXiv:1906.07120v3](https://arxiv.org/pdf/1906.07120v3),
[Theorem 8](https://arxiv.org/pdf/1906.07120v3#page=10), printed
p.10. Read §2's setup (p.3), §3's convention (p.7), normalization splits
in Theorems5/7, and AppendixA's inequality preceding (13) (p.24).

For Polish E, probability mu, measurable f,g in L1(mu), essinf_mu f=0,
and positive finite Z_f,Z_g, write dmu_f=e^(-f)dmu/Z_f. Theorem8 gives

\[
 d_{TV}(\mu_f,\mu_g)\leq
 \frac{\exp(-[\operatorname{essinf}_\mu g]_-)}{Z_f}
 \|f-g\|_{L^1(\mu)},\qquad [a]_-:=\min(0,a).
\]

Here d_TV is **one half** of the full L1 density distance. Finite lower
bounds matter: an unbounded negative potential gives no finite factor.
The theorem's proof is referred to Theorems5/7's normalization argument;
AppendixA states the direct likelihood-difference version. Import this
known quantitative input; no reproof of it is needed.

## Scalar primary inputs and the zero endpoint

[NIST DLMF 4.36.1](https://dlmf.nist.gov/4.36.E1) states

\[
 \sinh z=z\prod_{n\geq1}(1+z^2/(n^2\pi^2)).
\]

[DLMF 4.36.3](https://dlmf.nist.gov/4.36.E3) states, away from
z=n*pi*i including zero,

\[
 \coth z=z^{-1}+2z\sum_{n\geq1}(z^2+n^2\pi^2)^{-1}.
\]

Its exclusion of zero must be respected. The entire sinh series in
[DLMF 4.33.1](https://dlmf.nist.gov/4.33.E1) is the inspected input
for the removable zero case; [25.6.1](https://dlmf.nist.gov/25.6.E1)
gives zeta(2)=pi²/6 for a possible explicit series bound. Version1.2.8,
release15 September2026, retrieved8 November2026. These formulas give
scalar tools, not a theorem about normalized theta measures. Their
specialization and any uniform limit/differentiation justification are
future proof obligations; none is silently treated as completed here.

## Bounded specialization nominated for the next research step

The main gap remains L030–L032/C032a actual-Xi all-degree mixed positivity.
Use L019/L020 and L898's definitions and already established positivity,
strict raw-mass monotonicity and polynomial-exponential domination.
The following is a proof plan with explicit obligations, not a derivation
of the requested bound.

Choose the proposed probability reference on R² with density
W_(1/2)/A_0(1/2), and potential

\[
 \Psi_y(u,v)=\log\frac{\operatorname{sinhc}((u+v)/2)}
                         {\operatorname{sinhc}(y(u+v))}.
\]

This choice is intended to avoid an unbounded negative likelihood
potential. A direct positive tilt relative to W_0 is not automatically
within the theorem's finite lower-bound hypothesis. No change of
variables in u,v or theta normalization is proposed.

The separately approved mathematical step must verify:

1. The reference probability, measurability, nonnegative potentials,
   their L1 integrability, and essential infimum zero. Since p=u+v=0
   is a null line where W vanishes, citing a zero there alone does not
   verify an **essential** infimum. Check positive-measure neighborhoods.
2. The exact normalized-density identification and a uniform positive
   normalization bound using L898's existing mass facts. Keep all factors
   A_0(0), A_0(1/2) and the full-L1 factor two visible.
3. A pointwise potential-difference bound in |y²-v²| with an explicit
   integrable coefficient. Test the DLMF product/partial fractions in
   t=y² and use the entire series at t=0; do not divide by y at zero.
   No interchange of a parameter derivative and an unbounded integral
   is licensed merely by quoting pointwise analyticity.
4. An explicit M in terms of rigorously finite theta integrals, for
   example by controlling the p² moment of the reference measure.
   The actual expression and its coefficient must be established then,
   with L898's domination justifying the moment. No numerical value,
   optimization or directed-rounding contract is required for this target.

This is SPECIALIZE rather than IMPORT of the Xi assertion: it identifies
exactly the hypotheses and finite scalar/moment calculation left to do.
The general normalization theorem is ready to cite; the displayed Xi
bound has not been proved or approved as a new theorem this turn.
The newly recorded covered target receives the supervisor's separate
approval next turn before dependent mathematical work.

## Relevance, failures and stopping test

The downstream use is control of the **same** normalized numerator and
denominator when moving y. Any later frequency signing application must
have the resulting error strictly below an independently proved positive
reference margin. No such margin is provided, and an absolute uniform
error need not suffice at large frequency where the transform is small.
No sign conclusion for C_0 or actual Xi, and no solution of the mixed-form
gap, follows from these source statements.

Further fixed-cross-endpoint degree scans meet the audited L898 stop
recorded in ATTEMPTS/2026-11-08-fixed-cross-endpoint-xi-extension-stop.md.
L309's variance ordering does not order an oscillatory cosine; L312
records the actual-theta conditional-ordering failure under its arithmetic
contracts. Those are contrasts, not premises for the proposed norm bound.
The selected full-density estimate is independently testable without
reopening those mechanisms or the parked FLINT/LMFDB source blockers.

Continue the bounded specialization only if it gives a finite explicit M
uniform through zero with no sign assumption. Abandon this specialization
if an essential hypothesis fails or its constant is unbounded; record the
failure rather than retreat to qualitative continuity. Even success only
supplies an error-control input. Do not continue into mesh/sign work
without separately covered, independently paid margins.

## Search record and qualifications

Queries included `normalized densities Lipschitz L1 parameter
differentiation`, `normalizing L1 densities Lipschitz stability`,
`Sprungk total variation Theorem Lipschitz Bayesian`, `sinhc derivative
integral representation`, `xi sinhc total variation`, and `Riemann defect
kernel Lipschitz`. Searches were for known results and overlap, not an
originality certification. The matching source-level result is generic
normalization stability, with the Xi applicability gap stated above.

The van Hemert raw manuscript's definitions/decay passage (lines131–160,
Sections2–3, title date20 July2026) was inspected at
[its primary source](https://raw.githubusercontent.com/LeonardSEO/certified-riemann-xi-positivity/main/paper/main.tex);
normalization and fixed-endpoint conclusions are reused from L898 rather
than audited again. Its finite certificates are not inputs. No immutable
repository version or peer-review status was verified.

Folland Theorem2.27 was located through search results, but its primary
statement was not obtained; the author-hosted errata is not that theorem.
It is **not imported**. Parameterized Banach-space differentiation and
later Bayesian stability papers remain unread leads, unnecessary for
the selected finite-potential comparison. No source blocker is inferred.
Full matching Mathlib coverage and supporting theorem names were not
checked; availability remains unknown. No cross-notebook input was used.
This literature step spends no mathematical exploration attempt and
resets no exhaustion counter. No progress beyond the checked sources is
claimed.
