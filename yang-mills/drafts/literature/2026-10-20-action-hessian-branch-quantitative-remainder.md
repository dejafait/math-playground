# Action-Hessian branch — quantitative source comparison

TARGET: Assess source coverage for the action-Hessian branch remainder |T_i-a^(-3)K_(i,T)|<=C_i N^(5/2) log(eN)^2 against exactly L173(8), for both actual probes.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read all of L173, the covariance/collapse/parity cases of L158, L156/L157's conventions, L254 sections 1--2 and its separate exterior audit; screened local assessment matches, history/205 and history/378, ATTEMPTS/011,036 and the existing rate inventory. New bounded external queries and inspected primary passages are recorded below; no exact branch-rate theorem was established.
SOURCE_EVIDENCE: Reused the inspected Ward/flow/Symanzik and Adams--Lee comparisons in the 2026-10-12 cubic-residual/action and 2026-10-17 complete-rate assessments, and the Lawler--Limic comparison in the 2026-10-20 quartic-rate assessment. Additionally read Lawler--Limic's author-posted 289-page PDF, section 1.2, Propositions 1.2.1--1.2.2, pp. 12--13, and section 8.2's complete rectangle eigenbasis calculation, p. 191. Rechecked Theorem 2.5.6's restricted statement, pp. 58--59.
COMPARISON: L254(18) covers the same normalized two-point exterior used explicitly in L173(6), including separate derivatives through total order two and the complete heat sum. Its projected covariance estimate (3) concerns a different integral and cannot bound L173's scalar prefix correction. L173(9),(18) already quantify the scalar Green boundary and displacement terms; (15)'s local double-heat difference remains qualitative.
GAP: Quantify L173(15) uniformly over its supported endpoint stencils, then assemble the signed remainder against exactly (8), retaining the logarithmic scalar cancellation, inversion-even part, axial slope, both subtractions and original -6. The prospective local-error threshold is O(N^(-1/2)log(eN)^2); neither that estimate nor the branch remainder is established here.
REASON: Existing quantitative exterior coverage and standard scalar heat/spectral inputs support one bounded specialization of L173's signed limit argument. The remaining difference is an explicit finite-to-infinite subtracted double-heat comparison, not a missing general Ward theorem. No essential inaccessible source remains; this decision approves an attempt, not a rate or novelty claim.
LITERATURE_REASON: The changed target is a remainder for L173's action-Hessian branch, outside the old cubic-limit scope and the ready L254 audit; essential quantitative source comparison is missing.
SCOPE: Same relative SU(2) cube, lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, stored coordinates, bare-first expansion and actual probes 3,6. Only L173's action-Hessian branch remainder; all endpoint sums, source/end rows, constant modes, upper jumps and full heat sums remain.
COVERED_TARGET: Prove the action-Hessian branch remainder |T_i-a^(-3)K_(i,T)|<=C_i N^(5/2) log(eN)^2 against exactly L173(8), for both actual probes.

## Completed source review, 2026-10-20

This is a literature-only EXPLORATION, classified NOVELTY_UNCHECKED.
No new mathematical estimate, proof audit, lemma or script is produced.
The registered target is preserved. The ready continuation above is
proposed for the supervisor's separate approval in another invocation.

The main gap remains an ultraviolet-uniform interacting reflected error
<=c_box/2, continuum axioms and finite positive infrared mass. The
intermediate target is this branch's remainder, with plausible downstream
use in the complete cubic residual/action rate and later L011 quantitative
assembly. The smooth-action and E,E rates, cubic-probe and transverse-H
rates, and all interacting/construction requirements remain independent.

### Exact local comparison and reusable coverage

Read the supplied whole overview and local DAG before the detailed
proofs. L156(1), L157(1)--(6), L158(1)--(2),(5)--(16) and L173(1)
fix the signed contraction after the full-link gauge identities. This
review does not reprove their collapse or audit upstream inputs.

| Existing statement | Applicable coverage | Remaining difference |
| --- | --- | --- |
| L173(9)--(11) | Scalar transverse Green boundary correction and bounded-offset differences are already quantitative. The local scalar is retained. | Use these estimates in the complete remainder; no new scalar Green theorem is needed. |
| L173(12)--(15) | Exact double-heat representation of F_N, uniform one-difference majorants and convergent subtracted infinite potential f. | Its finite-time polynomial argument followed by dominated convergence gives no modulus in (15). This is the first missing estimate. |
| L173(16)--(17), proof section 4 | Four endpoint pairs, logarithmic local scalar, exact smooth-residual cancellation and inversion parity for the complete frozen row. The slope remains. | Preserve these operations when inserting a quantitative covariance comparison; the scalar cannot be deleted termwise. |
| L254(11)--(18), separate audit paragraphs on raw derivatives and the complete exterior | The same covariance-normalized raw columns, lower primitive and full triplet/shear coefficient matrices as L173(6), through its explicit reference to L152(5)--(6). In particular (18) already states C^2 error O(a) on compact two-point sets. | Apply that existing exterior estimate with L173's first-argument offsets (7). Do not import L254's response normalization, covariance conclusion or factor twelve. |
| L173(18)--(21) and L028 coefficient estimates as used there | Complete displacement/adjoint Taylor rows, both frozen insertion stencils, exact cancellation at finite mesh and compact Riemann-sum setup. | Quantitative assembly against the original three densities (8) is still required. No branch rate follows just from the limiting coefficient identity in L174. |

L254's covariance section uses a co-closed transverse heat entry and a
two-incidence projection sandwich with its stated inner tail. L173's
F_N is instead the scalar product R_st(Delta_0)G_N in a double heat
integral. Its undifferenced infinite integral diverges logarithmically;
only the displayed differences in (14) are assigned finite integrals.
Thus L254(3) is not a duplicate or direct estimate for (15). The reusable
part is its bounded-Laplacian polynomial comparison method, with the
scalar difference tails in L173(13) still to be treated in their own
order. No new tail integration or growing-time estimate is performed
in this literature turn.

Scoped searches of literature target fields for L173/action-Hessian/
logarithmic prefix matches found the registration and rate inventory,
not a completed branch-rate assessment. History/205 records the original
qualitative limit; history/378 deliberately leaves the different prefix
covariance uncovered. ATTEMPTS/011 stops a uniformly bounded raw loop,
and ATTEMPTS/036 stops an insufficient unsigned local count. Neither
forbids this signed refinement, nor proves signed growth. Preserve both.

### Primary sources and their limits

New bounded queries were `"lattice" "prefix covariance" "remainder"`,
`"axial gauge" "lattice" "Ward" power divergences`, and
`discrete Dirichlet heat kernel finite box interior difference estimates
resolvent product logarithmic potential`. The results did not establish
an exact branch-rate theorem. General continuum Dirichlet-kernel papers,
noncompact Abelian gauge correlations and a Cornell discrete-domain
heat-kernel thesis remain screened or unread leads, not imported theorems
or essential prerequisites. No novelty is inferred from search failure.

**Lawler and Limic, Random Walk: A Modern Introduction, Cambridge
University Press (2010), [author PDF](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
289 pages, accessed 2026-10-20.** Read section 1.2, Propositions
1.2.1--1.2.2, pp. 12--13: Poissonization and independent coordinate
walks, with their jump-rate convention. Section 8.2, p. 191, treats
simple nearest-neighbor walks killed at rectangle faces; its complete
sine-product basis and eigenvalue calculation cover precisely the
scalar interval/cube geometry, after matching generator normalization.
These are supporting spectral inputs, not a subtracted resolvent-product
rate. Theorem 2.5.6, pp. 58--59, restricts its one-dimensional local
central limit estimate to |x|<=t/2; it is not an all-image derivative
bound. Reuse the earlier assessment's inspected transient Green/exit
and difference results (Theorem 4.3.1, Proposition 4.6.2(a), Lemma
6.3.3) within their stated domains. None evaluates F_N differences or
the signed branch. No general scalar theorem needs reproof here.

Reuse the precise primary comparisons in
`2026-10-12-cubic-residual-action-cubic-scale.md`, sections on bounded
search and inspected primary cases, and
`2026-10-17-complete-coefficient-quantitative-remainder.md`, primary
theorem comparison. In particular Del Debbio--Patella--Rago,
[1306.1173v1](https://arxiv.org/pdf/1306.1173v1), section 6,
(6.1)--(6.16), pp. 13--16, concerns complete matched Ward responses;
Luescher--Weisz, [1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
sections 7.1--7.4, 8.2/8.4, pp. 20--25, concerns renormalized flow
correlations and their zero-flow-time boundary. Neither supplies this
isolated bare, physical-boundary forest estimate. The inspected
Adams--Lee [0709.0781v3](https://arxiv.org/pdf/0709.0781v3), section
II (7)--(15), pp. 5--7, Appendix A (A1),(A11)--(A18), pp. 19--23,
requires its specified momentum-integral scaling, denominator growth,
sole zero and infrared convergence, with external-parameter dependent
constants. No matching representation and heat-uniform constants for
this variable-coefficient pinned branch are established. Reuse these
scope exclusions; no further Ward/source access is essential.

The official Jaffe--Witten version remains the one recorded in the
saved rate inventory; no global target hypothesis has changed.
Full matching Mathlib coverage for this branch remainder and supporting
discrete heat comparisons is not checked. Unknown is not absence.

### Bounded continuation and abandonment test

Attempt only the COVERED_TARGET. Essential IDs: L173 L158 L156 L157
L018 L028 L152; supporting quantitative exterior input L254, with
L222/L248 qualifications retained. L151 is a method comparison;
L174/L180 identify downstream coefficients but give no remainder.
All imported analytic assumptions remain premises, not newly verified
facts. No numerical heat-sign assumptions are needed to state the rate.

First test a uniform quantitative replacement for L173(15) on its
bounded endpoint stencils, seeking the stated normalized error budget.
Use its exact subtracted double-heat representation and original
one-difference majorants; a growing finite-time polynomial comparison
requires a bound for the full complementary two-time region. A preview,
fixed-time convergence or the quartic covariance tail is insufficient.
An adequate local comparison is useful even before the complete branch
assembly is finished. The assembly must retain L173's separate first
argument derivative, adjoint coefficient jet, both subtractions, slope,
all four endpoints and its one-color -6 once.

Continue upon an adequate rigorous local comparison or complete remainder;
otherwise record the actual bound and first unresolved term. Abandon
shortcuts based on a globally bounded raw loop, deletion of the scalar
logarithm, an unsubtracted infinite double integral, or internal final-time
heat damping. An above-budget upper bound is not signed growth. Newly
essential uncovered hypotheses require REVIEW_REQUIRED; persistent
essential source blockage would require parking dependent work. None
was found in this review. The new ready continuation still receives
separate supervisor approval before mathematical invocation.

## Original registration (historical; superseded above)

The main gap remains an interacting reflected error <=c_box/2, continuum
axioms and finite positive infrared mass. The intermediate proposed target
is the stated remainder for T_i, one branch of the complete cubic
residual/action group I_i^(3). Its plausible use is later quantitative
assembly with the separate smooth-action and E,E remainders. Those
remainders, the complete cubic probe and transverse-H rates, and all
construction requirements remain independent.

Use exactly L173(1)'s T_i=-6 sum A_ef U_(i,fe) K^+_fe, with
K_(i,T) specified by L173(8). This is a one-color exterior with its
original -6 already included, not a new color-extended quartic tensor.
Keep the relative SU(2) cube, lower-rooted direction-1 forest, admitted
even N, a=8/N, tau=1/16, stored coordinates, bare-first order and
actual probes 3,6. Retain both insertion subtractions, every endpoint
sum, source/end row, constant mode, upper jump and full heat series.

Essential starting IDs are L173 L158 L156 L157 L018 L028 L152.
L174 identifies the coefficient but does not quantify its remainder;
L180 places the branch in the complete group. L151 and audited L254
are potential quantitative comparisons only. In particular the scalar
prefix covariance in T_i is not the projected local forest covariance
of L254. The logarithmic scalar correction, its bounded-offset
differences and the actual residual cancellation must be read in
L173/L158 before deciding applicability. Do not assume a rate from
their qualitative local limit or transfer L254's final conclusion.
All imported qualifications remain premises, not newly verified facts.

Reuse the existing primary Ward/flow/momentum-integral comparisons
where their hypotheses still match. Inspect precise theorem hypotheses
and relevant cases only for genuinely missing quantitative coverage.
Check local duplicates and the existing covariance/absolute-count
failures before proposing a proof. This registration does not claim
that another external theorem is essential or inaccessible.

Continue if source comparison identifies adequate coverage for this
exact rate or a bounded intermediate estimate with a demonstrably
adequate error threshold. Otherwise name the first missing estimate
and register its own coverage needs. Abandon shortcuts based on a
qualitative limit, a globally bounded raw covariance, termwise deletion
of the logarithmic correction, or internal final-time heat damping.
An above-budget upper bound is not a signed lower bound. Persistent
source blockage requires an independently testable target.

No theorem is imported and no new mathematics is derived in this
registration. Matching Mathlib coverage remains not checked. A separate
source turn must decide scope before mathematical work on this target.
