# Reciprocal-density Volterra propagation: comparison completed884

TARGET: Assess whether the reciprocal-density Volterra equation can propagate C466a's fixed-order boundary PF signs to a prescribed compact positive interval, comparing known PF preservation hypotheses and nominating one bounded first-contact test or a precise obstruction.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step884 checked the named local failures and exact Volterra/PF/self-decomposable/cofactor queries below. Located the classical scalar equation and a stronger version-specific finite PF theorem; no inspected theorem supplies the requested spatial determinant propagation. No novelty inference.
SOURCE_EVIDENCE: Steutel--van Harn (2004), V.2.11/V.2.16 equation(2.23), III.4.16/III.10.4 including the singular-kernel continuity proof; Sra author PDF riem-xi-v3 (2November2026), Theorems1.2/3.4/C.9 statements, SectionC.8 convolution proof, PropositionA.1 statement/relevant proof; official Mathlib convolution differentiation hypotheses. Reuse882/C466a for density and local Wronskian coverage. Precise links and qualifications below.
COMPARISON: The scalar equation has matching self-decomposable-law hypotheses. Convolution preservation requires signed minors of both factors; positivity and monotonicity of H are weaker premises. Sra v3 already states global PF through k*=1810540931075, so a low-order actual-density sign target would duplicate literature. Its finite-factor budget does not propagate arbitrary orders from C466a.
GAP: No independent first-contact forcing sign or global continuation is supplied. Complete monotonicity of actual H is an RH-equivalent premise, not an available repair. Analytic differentiation has standard coverage; its compact localization and the signed cofactor/tail bound remain future proof obligations.
REASON: New source overlap changes the proposed low-order test and parks the direct preservation inference. A symbolic arbitrary-order actual-H cofactor test is separately specified in assessment884; no contact identity or new sign is derived here.
SCOPE: Completed step884 is literature-only. No lemma or mathematical script was written. The nomination below is retained as provenance; current coverage and the distinct bounded mathematical continuation are recorded in the completion section and assessment884.
LITERATURE_REASON: C466a coverage ends at the boundary; the proposed spatial Volterra-to-minor propagation interface is a changed target with essential uninspected source hypotheses.

The main gap remains L030-L032/C032a. Essential local inputs are
C466a for the fixed-order boundary statement and L018/L024 for actual-Xi
normalization; source Theorem1.1 supplies the positive decreasing
function H and its Bernstein representation. The proposed identity to
locate and assess in primary sources is

    x theta_1(x) = integral_0^x H(t) theta_1(x-t) dt.

This line specifies a review target, not a newly established result in
step883. In particular, singular behavior of H at zero, endpoint terms,
derivative integrability and signed determinant combinations require
their exact source hypotheses. Generic convolution positivity or
log-concavity does not establish PF of higher order. If a preservation
theorem requires complete monotonicity of H, all-degree Hankel signs,
or another RH-equivalent input, record the unmet premise explicitly.

Plausible use: an independently proved finite-order propagation law,
iterated for each fixed order and arbitrary compact positive interval,
could turn the boundary input into global PF information. That is only
a proposed downstream route; neither the propagation law nor its final
Schoenberg/L030 interface is paid here. No order-uniform boundary
neighborhood is assumed. The cited density inputs and their finite
zero/counting premises remain external and are not discarded.

Bounded decision test: determine whether an inspected theorem gives a
first-contact sign under hypotheses known for actual H, or identifies
a specific extra signed term whose control can be tested independently.
Prefer the first nontrivial order beyond known global log-concavity,
but select its exact statement only after source and duplicate checks.
If the route only restates missing PF or an already recorded sign gap,
park that inference rather than repeat formal determinant manipulations.

Preserve ATTEMPTS/2026-11-06-reciprocal-hankel-contact-sign-unpaid.md
(canonical L874), ATTEMPTS/2026-11-01-reciprocal-double-zero-sign-input-stop.md
(canonical L611), the fixed-U12 stops, and the prior source-access limits.
They are scoped evidence, not a ban on the new spatial mechanism.
No cross-notebook input is proposed. Mathlib matching is unchecked.

A creative central-gap attempt is the desired eventual routing if this
comparison exposes a genuine independent sign mechanism. It is not yet
ready: essential propagation coverage is missing, so the immediate
recommendation is literature_comparison, standard/high. Do not relabel
the completed source reproduction or approve new mathematics here.

## Completion884: sources and applicability

The paragraphs above preserve the original nomination, not the current
coverage decision. Essential local inputs are C466a and L018/L024;
L030-L032/C032a remain the destination. Read the C466a hypotheses and
conclusion,882's full assessment, the named ATTEMPTS and L874's contact
reduction. This is spatial evolution of a density determinant, whereas
L874 concerns heat evolution of reciprocal-zero logarithmic moments.
Neither that distinction nor the source comparison proves a sign.

**Scalar equation.** F. W. Steutel and K. van Harn, *Infinite Divisibility
of Probability Distributions on the Real Line*, Marcel Dekker,2004,
Chapter V Theorems2.11 and2.16, equation(2.23),
[book text](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf).
For a nondegenerate positive self-decomposable law with left endpoint
zero and canonical density k, V.2.16 gives its continuous positive
density f and x f(x)=integral_0^x f(x-u)k(u)du, x>0.
Inspected its hypotheses, the preceding canonical representation,
III.4.16 and III.10.4's continuity argument, including k(0+)=infinity.
C466a's cited law has the required support; Sra's Bernstein
representation identifies k=H. Thus this is a known input ready for
citation, not an equation to rediscover. No determinant sign follows
from the cited theorem. The version's text extraction does not expose
reliable printed page numbers; chapter/theorem/equation locators are
used instead.

**Higher-order overlap and preservation.** S. Sra, *On some positivity
properties of the Riemann Xi function*, author version v3,2November2026,
[primary PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Theorem1.2 pp2-3 states Theta,Lambda in PF_k* for
k*=1,810,540,931,075, using verified zeros through3,000,175,332,800.
Theorem3.4 p10 requires n>=2m,
(n-2m+1)/2>=sqrt((m-1)(n-m+1)),100<=T<=U<=U_PT,
C(T)>=n,Q=T^2<U^2-1/4 and epsilon_U(Q)<1; n>=8m suffices
for its integer constraints. C(T) and epsilon_U are defined immediately
before it. Theorem C.9 pp27-28 additionally specifies positive
exponential rates<=Q and signed perturbation weighted variation<1.
Section C.8 p29 composes factors whose required minors have already
been signed. Proposition A.1 pp16-17 identifies complete monotonicity
of H with RH. Its slit-plane zero exclusion and PF proof cases were
read. These are inspected source claims, not a complete independent
audit of the enormous finite-order certificate. The Hub v1 used in882
is different; do not silently replace its theorem numbers or claim
C466a audited v3. The source itself, not its abstract, establishes the
overlap comparison; no new global PF input is inserted into PROOF.

The inspected composition argument gives no implication from merely
H>0,H'<0 to the missing signed minors of a Volterra solution. Using
already-global PF of the solution in that argument is circular for
this task. The finite factor hypothesis also prevents treating that
theorem as an order-independent propagation result. These are exact
hypothesis mismatches, not a proof that no other preservation theorem
exists. No claim is made that actual H fails a finite PF condition.

**Differentiation and Mathlib.** The official
[Mathlib.Analysis.Calculus.ContDiff.Convolution](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ContDiff/Convolution.html)
contains HasCompactSupport.hasDerivAt_convolution_right and
HasCompactSupport.contDiff_convolution_right. The inspected statements
require a compactly supported smooth right factor, locally integrable
left factor, and the stated invariant measure hypotheses; real
Lebesgue measure is the intended specialization. Source link commit
26573066084e6e2aa8526ea358bc43b66d96f970 fixes the inspected version.
These support a compact localization of the smooth density factor;
they do not justify differentiating a singular H at zero. Establishing
the localization and all endpoint terms belongs to the mathematical
attempt. Full matching Volterra/PF preservation coverage was not
checked in Mathlib; its absence is not claimed.

## Search scope and access qualifications

Queries: `self decomposable density Volterra equation total positivity
Polya frequency log concavity kernel Yamazato`; `Suvrit Sra Xi Volterra
theta H Polya frequency`; `self-decomposable density integral equation
Steutel 2.16`; `Volterra determinant Polya frequency`;
`self-decomposable first contact positivity`; `reciprocal xi Volterra
determinant`; and convolution differentiation/local integrability
follow-ups. Narrow local searches covered reciprocal assessments,
the named failures and November12-14 source notes, not sibling notebooks.
No matching ready spatial-contact assessment was found in those paths.

Watanabe's Euclid PDF opened only an iframe/service notice; MDPI
returned429, the Lancaster mirror failed, and direct shell retrieval
had no DNS. These are unread leads, not theorem evidence. The scalar
equation was instead read in the book; the author's v3 PDF was readable
through web extraction. Simon's stable-density introduction was seen
in search/extraction but its follow-up timed out: no stable countermodel
is imported or proved. Salamon/Folland mirrors failed; official Mathlib
statements suffice for the differentiation toolkit. No essential source
blocker remains for the bounded test884, and none of these failures
authorizes a mathematical repair in this literature turn.

## Decision and one proposed test

Park the inference that positive decreasing H automatically propagates
all boundary PF orders. Park a new actual-density PF3 proof as overlapped
by v3. Preserve L874, L611 and the fixed-U12 stops within their scopes.
No source found here refutes spatial propagation for the actual density.

Assessment884 nominates only the cofactor-weighted retained-zero test
at an arbitrary symbolic order beyond the cited finite range. It must
retain actual H, handle its singular endpoint through the smooth factor,
and seek a strict inward first-contact sign or a suitable local barrier.
A weak derivative sign at an isolated contact is insufficient. An
unpaid higher-order sign, complete monotonicity or a freely substituted
model cannot be reported as an actual-Xi obstruction. This is a bounded
creative attempt after separate approval, not a result of step884.
