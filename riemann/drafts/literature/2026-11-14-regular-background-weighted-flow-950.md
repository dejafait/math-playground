# Regular-background weighted-flow source assessment951

TARGET: Assess source coverage for uniform integrability of stopped weighted densities for S(q)=-2 log q+H(q), q(0,r)=ir, with H holomorphic and H',H'' bounded on a fixed disk, up to first zero hit or escape.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step951 searched exact uniform-integrability, bounded weighted-Jacobian, logarithmic-zero and regular-term formulations; inspected TNV's relevant cases and followed references19–20; no matching arbitrary-H stopped-density theorem was found in those passages. Queries, scope and unread leads are below; no novelty inference.
SOURCE_EVIDENCE: TNV arXiv1706.03822v2 https://arxiv.org/pdf/1706.03822v2 Section2.2(2.19)–(2.21), footnotes1–2 p6, Sections3.1–3.2 pp7–9, AppendixB(B.1)–(B.5) p22; Kanazawa–Tanizaki arXiv1412.2802v2 https://arxiv.org/pdf/1412.2802v2 Section2 pp3–6; Tanizaki arXiv1412.1891v3 https://arxiv.org/html/1412.1891v3 SectionIV(32)–(35). Reused review948's LY coverage.
COMPARISON: Known raw-flow and real-parameter variational equations apply before singularity; the inspected collision example drops regular terms. Logarithmic-zero thimble existence and modified-metric no-blow-up results do not supply the requested fixed-time measurable-set estimate. C466q covers only H=0.
GAP: Uniform control of the full stopped weighted density for nonzero H remains unproved; no exact matching theorem was identified in the bounded comparison. This is an estimate to investigate, not an inaccessible essential source or an established obstruction.
REASON: Source scope now supports nominating one bounded perturbation attempt, with every singular boundary and arbitrary measurable initial set retained. No new mathematics was derived in this literature turn; the distinct continuation assessment951 is subject to separate next-turn approval.
SCOPE: Literature comparison for the stated one-normal-variable flat raw flow, analytic H with the prescribed disk bounds, stopped density and fixed physical time; no global contour, tangential-variable or actual-h theorem is imported.

## Preserved target scope, not an established result

Take a fixed disk D_R={|q|<R}, real 0<a<R, and r in (-a,a)
minus {0}. Require H holomorphic on the disk with finite uniform
bounds M_1 for |H'| and M_2 for |H''|. H(0) is finite and must be
retained in any constants. Use the unit flat metric and the same raw
upward conjugated-gradient convention as C466q. On nonsingular
trajectories the signed density to study is
-q(T,r)^2 exp(-H(q(T,r))) partial_r q(T,r)/i, with the derivative
taken at fixed T. Stipulate density zero once the trajectory first
hits zero or exits the disk. This stipulation makes no homology or
classical continuation assertion.

The proposed intermediate question is whether the known sources give,
or justify seeking, some T_0>0 and a modulus omega(s) tending to zero
as s decreases to zero, with integral_E |W_T|<=omega(|E|) for every
measurable initial set E and all 0<=T<=T_0. The dependence on
R,a,H(0),M_1,M_2 and the escape convention must be explicit. The
review may find stronger necessary hypotheses or an obstruction;
neither outcome is assumed. No proposed bound is derived here.

Input for comparison: C466q, with exact H=0, no lemma dependency
on the actual h law. Review948's convention and LY phase qualifications
are reused. Step951 inspected the changed regular-term proof case and
the references below. Their scope supports EXPLORE, not import of a
perturbation result. No novelty is inferred.

Plausible use: a local analytic factor is required before the frozen
collision audit could inform an actual-weight deformation. Even a
positive perturbation result would leave tangential coupling, metric
normalization, noncompact homology, endpoints, signed integration,
all orders and Xi transfer unresolved. Stops927/932/941/947/948 stand.
If sources cannot supply a precise, testable local claim, park it;
do not repeat the completed H=0 calculation or a phase-only test.

This nomination is not a creative central sign mechanism: a global
condition connecting local flow control to a signed determinant has
not been formulated or justified. Its source gate cannot be skipped
to meet a discovery cadence. No cross-notebook input is involved.
Full matching Mathlib coverage has not been checked.

## Primary source comparison completed 14 November 2026

The exact target above was preserved. No lemma, ODE calculation,
counterexample or mathematical script was written in this source step.

TNV: Tanizaki, Nishimura and Verbaarschot, *Gradient flows without
blow-up for Lefschetz thimbles*, JHEP10(2017)100, v2 dated
27 September 2017, [PDF](https://arxiv.org/pdf/1706.03822v2),
[HTML](https://arxiv.org/html/1706.03822v2). Inspected the entire
local zero case, both footnotes, the changed-metric hypotheses and
the variational derivation through the flat-metric case at the
locators in SOURCE_EVIDENCE. The raw-flow Jacobian law (B.5) is
\(\dot J=\overline{S''(q)J}\), at fixed time with real initial
variation. The simple-zero asymptotic omits regular terms. Footnote2
requires bounded full weighted Jacobian in its shrinking-region
discussion; it does not prove that bound for arbitrary H. Section3
uses polynomial bosonic action and determinant, with a decelerating
metric. Its completeness conclusion concerns that altered dynamics.
The present target fixes the raw metric, physical time and stopping
rule, so that conclusion cannot be substituted for the target.

Following TNV reference20: Kanazawa and Tanizaki, *Structure of
Lefschetz thimbles in simple fermionic systems*, JHEP03(2015)044,
v2 dated 18 February 2015,
[Section2 PDF pp3–6](https://arxiv.org/pdf/1412.2802v2),
[HTML](https://arxiv.org/html/1412.2802v2). Read the general
flow/homology hypotheses and the holomorphic-zero case, including
the example after (2.4) and the branch-phase qualification; also
compared Section3.1.1(3.4)–(3.5)'s nonzero analytic background.
The framework requires nondegenerate critical points and a suitable
relative integration cycle; logarithmic zeros modify its good-end
regions. Its simple-zero Gaussian example illustrates cycle
decomposition. This is not a theorem about the fixed-time Jacobian
of a family starting on our finite imaginary segment. The disk-only
H hypotheses do not supply its global cycle assumptions or critical
point conditions. Neither those extra assumptions nor homological
integral identities establish the requested absolute-mass modulus.
No global specialization is imported. The absence of a Jacobian
keyword in an HTML search was only a navigation aid; the relevant
zero-case discussion itself was read.

Following reference19: Tanizaki, *Lefschetz-thimble techniques for
path integral of zero-dimensional O(n) sigma models*,
Phys.Rev.D91(2015)036002, arXiv1412.1891v3 dated 11 February 2015,
[SectionIV(32)–(35)](https://arxiv.org/html/1412.1891v3).
Read its branch-independent derivative discussion and explicit
fermionic flow with regular and symmetry-breaking terms. Those
model-specific trajectories and cycle constructions do not state a
uniform stopped weighted-Jacobian estimate for the present H class.
This is an inspected comparison, not an imported perturbation theorem.

Reused, without new browsing, review948's direct LY2021
IV.A–IV.B(12)–(21) extraction: residual Jacobian phase and collision
contour qualifications remain relevant, with no mass bound supplied.
No reproof of a cited theorem is proposed; any subsequent proof must
establish the stated missing weighted estimate itself.

## Bounded discovery and local duplicate/failure checks

Exact queries included:

- `"holomorphic gradient flow" "uniform integrability" Jacobian`
- `"holomorphic gradient flow" "logarithmic" Jacobian singularities`
- `"Lefschetz" "regular terms" "Jacobian"`
- `"holomorphic gradient flow" "bounded" "weight"`
- `"holomorphic gradient flow" "regular" "Jacobian" singularities bounded density`
- `"stopped" "gradient flow" "logarithmic" Jacobian`

Search results did not identify a precise matching theorem.
Irrelevant transport/PDE gradient-flow results and secondary summaries
were not used as evidence of applicability. TNV's references19–20 were
followed as the most direct stronger-result leads. The broader
Rev.Mod.Phys.94(2022)015006 review and later model-specific numerical
contour papers remain unread leads, not mathematical inputs. There
is no claim of exhaustive absence or originality, and no persistent
source-access blocker has been established.

Narrow searches covered review947, review948, working950, histories948/950
and the collision attempt records. C466q was read in full. No local
nonzero-H weighted estimate was identified there. Stops927/932/941
concern common-product phases, conditional independence and pointwise
marginal signs; stop947 concerns generic finite contour jets;
stop948 rejects unsupported smooth-divided-phase necessity. None
settles the present mass estimate, and none is reopened. The exact
frozen calculation is complete and is not nominated for repetition.

## Decision and single continuation

EXPLORE records completed bounded source discovery with an unresolved
analytic estimate. It is not SOURCE_BLOCKED: the relevant primary
machinery and its essential cases were accessible. It is not IMPORT:
no matching bound was read. Global thimble assertions cannot pay it.

The mathematical continuation, formulated but not attempted, is in
[assessment951](2026-11-14-regular-background-weighted-flow-attempt-951.md).
It retains the original target assumptions and asks for the full
measurable-set modulus. An integrable envelope would suffice, but is
not presumed. A failure must distinguish a missing method from an
admissible counterexample; a failure of a stronger auxiliary estimate
would not by itself refute uniform integrability. The canonical
assessment is new and requires separate approval before invocation.

The plausible downstream use remains one local analytic-factor
condition for a future deformation. Tangential coupling, global
homology, endpoint payment, signed integration, all orders and Xi
realization stay open. No justified central creative mechanism has
emerged: the global signed-contour condition linking this estimate
to determinant signs is still absent. This blocks a creative
nomination, not this bounded established-route development target.
Mathlib matching coverage remains not checked; no absence is claimed.
