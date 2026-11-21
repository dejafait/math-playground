# Theta-dependent differential pair: completed source comparison

TARGET: Assess Hedenmalm arXiv:2606.17494v1's theta-dependent pair (LD,L), identifying its exact domain and boundary-form condition and whether it yields an independent bounded sign test rather than an assumed real spectrum.
CHECKED: 2026-11-08
DECISION: IMPORT
SEARCH_EVIDENCE: Step141 searched exact title/identifier, Hedenmalm operator-pair inner product/domain/positivity terminology and narrowly relevant local realization stops; no inspected stronger construction supplies the missing form. Exact queries and reading limits below; no exhaustive-search or novelty claim.
SOURCE_EVIDENCE: Hedenmalm, Spectral interpretation of Riemann zeta zeros, arXiv:2606.17494v1, submitted 16June2026: primary PDF pp2-8, especially (3.2.1)-(3.2.2), Theorem3.3.1/full proof pp4-6, Remark3.3.2(b)/(3.3.9), Theorem3.3.3/Remark3.3.4 p7, Definition4.2.1 p7, Theorem4.2.2/both proof cases and Corollary4.2.3/proof p8; PDF reference list p9 and primary HTML cross-check. Girouard-Polterovich arXiv:1411.6567v1 Section1.1-1.2 read for the cited Steklov analogy only.
COMPARISON: The source characterizes zeros by an ODE and assumes symmetry on their finite eigenfunction span; it constructs neither a Hilbert form nor a Green boundary identity. The earlier actual-pair construction stop therefore remains applicable to importing positivity, although this differential pair is a distinct object.
GAP: A positive definite form on the L-images, its symmetry for all included complex-zero eigenfunctions, and a defined inverse/domain remain unpaid. Closed realization, completeness, multiplicities and mixed-form transfer are not supplied by the inspected conditional criterion.
REASON: Retire automatic positive-realization import: the independent-sign continuation test fails. Preserve a separate, bounded formal-inverse diagnostic for later approval; do not infer nonexistence of a positive realization or an actual off-line zero.
LITERATURE_REASON: The startup REVIEW_REQUIRED target lacked primary theorem/domain and essential proof-case coverage; the ready heat-contact assessment could not cover this distinct pair. That missing comparison is completed once here.
SCOPE: Literature-only source and applicability comparison; IMPORT covers the conditional source statements and their limitations, not a new operator, proof of RH, lemma or mathematical script. The newly nominated domain diagnostic has its own assessment and was not attempted.

## Gap and review test

The gap is L030-L032/C032a all-degree actual-Xi mixed positivity.
The intermediate target was independent domain/boundary data making
the actual theta pair symmetric in a positive form. Such data could
support a real-spectrum route, while still requiring a justified link
to the mixed forms. Continue only with specified independent data and
a bounded discriminating test; retire automatic import if symmetry
remains the missing positivity assumption. The retirement case applies.

## Primary theorem and proof-case record

Use the [versioned PDF](https://arxiv.org/pdf/2606.17494v1), pp4-8.
Put w(t)=Theta_00(i t^2), phi=-log(w), D=(t/i)d/dt and
L=D+(D phi). Theorem3.3.1 treats real alpha with u(0+)=u(infinity)=0;
Theorem3.3.3 treats complex alpha with t^(-Im alpha)u tending to zero
at both ends. Nonzero solutions occur precisely at Xi zeros, with

    u_alpha(t)=t^(-i alpha) integral_(0,t) y^(i alpha) w(y) dy/y.

The real-case proof reduces Lv=0 to v=Cw and uses both endpoints.
The complex proof is omitted by the author. Remark3.3.4 replaces the
weighted endpoints by t^(-N)u(0+)=t^N u(infinity)=0 for every N>0.
Section4 uses H_finite=span{u_alpha: Xi(alpha)=0}, including nonreal
zeros, and

    <u,v>_1=<Lu,Lv>_2,
    <LDu,Lv>_2=<Lu,LDv>_2  for every u,v in H_finite.

Theorem4.2.2 gives zero norm for nonreal-alpha eigenfunctions and
orthogonality at distinct real alpha. Its two proof cases substitute
LDu_alpha=-alpha Lu_alpha. Corollary4.2.3 requires a Hilbert inner
product on the images and excludes Lu_alpha=0. No such form is built.

These are cited statements, not a local reproof or a verified RH input.

## Applicability and qualifications

Definition4.2.1's use of “self-adjoint” is the displayed symmetry
requirement. It does not specify an ambient measure, a closed operator
domain, an adjoint domain, a Green boundary form or endpoint fluxes.
Fast decay of each eigenfunction alone does not settle symmetry of the
pair in an unspecified inner product. In particular, the ordinary
positive scalar theta weight is not the required two-variable form.

Keep the differential nullspace and the spectral domain separate:
the paper's proof identifies ker L on smooth functions as multiples
of w, but does not establish that w belongs to H_finite. Its seminorm
comment cannot license taking an inverse of L on every decaying
function. Nor may a quotient silently identify a nonzero L-image
with zero to evade Corollary4.2.3's definiteness requirement. No
conclusion about injectivity on H_finite is derived in this turn.

One-dimensional solution spaces are geometric statements, not a proof
that Xi zeros are simple. The source supplies no generalized-eigenvector
theorem, completeness result or closed realization. All complex zeros
must remain in the criterion; restricting to known real ordinates
would remove the critical obligation. The complex endpoint proof and
the corollary's final incompatibility are not independently audited.

No exact numerical Mellin normalization or local K-to-w identification
is imported. The printed coefficients in (1.2.3)/(2.2.1) warrant a
separate normalization check against L019/L020 before any norm or
mixed-form transfer; that check was not performed here. This restriction
does not convert the source's zero criterion into a positivity result.
The printed small-t bounds (1.2.5) are likewise not imported as verified
estimates; any later endpoint check must use the defining series and
inversion identity with its own complete justification.

## Duplicate and reference comparison

Read canonical L019/L020, L030 and C032a, and the relevant step140
comparison. These distinguish positive theta integrals from algebraic
reciprocal-zero squares. No new normalization bridge is needed for
this source-scope decision. The supplied DAG located the sign goal
before those detailed reads. No cross-notebook input was used.

Read the October31 actual-pair construction stop and its completed
assessment. Their Suzuki and Conrey-Li comparisons are reused, not
rebrowsed: RH-conditional realization, another shifted pair and an
extra translation sign cannot furnish this pair's missing metric.
This comparison is conceptual; the source does not identify its pair
with those de Branges pairs. No input from parked L872/L873 is used.

Followed Hedenmalm's Steklov reference to Girouard-Polterovich,
[arXiv:1411.6567v1](https://arxiv.org/html/1411.6567v1), Sections1.1-1.2:
their compact-manifold boundary problem and Dirichlet-to-Neumann
interpretation have actual trace/extension hypotheses. This analogy
does not furnish the half-line pair's missing domain or metric.
No Steklov theorem is imported or reproved. The PDF's other references
to Berry-Keating, Connes and Pólya motivate spectral/theta formulations;
their full texts were not inspected and are not positive-form inputs.

Queries submitted included exact title plus self-adjoint inner product;
`2606.17494 boundary inner product`; `L_phi Riemann self-adjoint`;
`Hedenmalm 2606.17494 inner`; `Hedenmalm operator pair positive`;
and exact title plus domain. Secondary summaries, a toolkit repository,
other spectral proposals and claimed RH solutions were search leads
only, not inspected theorem evidence. No novelty inference follows.
Primary PDF pp4-8 resolved the load-bearing formulas. Its eight-item
reference list on p9 differs from the HTML's long reference rendering;
the PDF numbering governs this assessment. Screenshot calls returned
no displayed image here; textual PDF/HTML evidence, not a claimed
visual inspection, supports this comparison. Initial oversized local
search output was replaced with exact-path reads; no conclusion rests
on a truncated search preview.

## Decision and bounded continuation

NEGATIVE is new source-scope evidence: the specified independent-sign
test fails because the missing positive symmetric form is assumed,
not furnished. It is not a new theorem, a no-go theorem for all forms,
an off-line zero or progress beyond the inspected literature. Park
positive-realization import; reopening needs explicit metric/domain
data with a paid symmetry identity and a nondegenerate L-image norm.

The separate nomination tests the formal inverse on only
V=span{w,Dw}, using the prescription T(Lu)=-LDu and a one-point
theta-series test. It asks a well-definedness question, not a sign
theorem. Its outcome is deliberately not derived here; it cannot
refute H_finite symmetry unless an additional domain connection is
proved. The source's commutator and kernel formulas make this a
specific prerequisite to test rather than another positivity search.
See `2026-11-08-hedenmalm-formal-inverse-domain-test.md` for separate
approval and all limitations. This is routine source specialization,
not a protected creative central mechanism. No justified creative
metric construction is available: the independent metric is still
the mathematical blocker. Full and supporting Mathlib coverage for
the pair, inverse and positivity claims is unchecked.

