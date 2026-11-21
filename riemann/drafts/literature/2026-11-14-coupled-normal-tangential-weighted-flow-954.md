# Coupled normal–tangential stopped density — source review955

TARGET: Assess source coverage for a class-uniform measurable-set modulus of the stopped full weighted Jacobian for S(q,z)=-2 log q+H(q,z), initial (q,z)=(ir,s), with bounded first and second derivatives of H on a bounded bidisk.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Review955 searched coupled logarithmic-flow weighted Jacobians, singular volume and uniform integrability, then followed real additive-compound volume-growth terminology; inspected the primary cases below and reused review950/C466r. No matching stopped coupled modulus was identified; no novelty inference.
SOURCE_EVIDENCE: TNV arXiv1706.03822v2 AppendixB(B.1)–(B.5), printed p22, Section2.2(2.19)–(2.21)/footnotes1–2 p6 and Sections3.1–3.2 pp7–9 https://arxiv.org/pdf/1706.03822v2; Wu–Kanevskiy–Margaliot arXiv2008.10321v2 Sections2.2/2.4/2.5, Proposition5/full proof, printed pp5–9 https://arxiv.org/pdf/2008.10321v2; Nishimura–Sakai–Yosprakob JHEP09(2023)110 AppendixA.2(A.5)–(A.9), A.4(A.30)–(A.35), pp23/27, primary PDF linked below.
COMPARISON: TNV supplies the full conjugated matrix variational law on survivors; real compound-matrix growth is a possible volume tool. Neither source supplies the singular weighted determinant estimate, endpoint interpretation or class-uniform measurable-set modulus. C466r's scalar estimate and modified-metric completeness do not settle these differences.
GAP: Establish or refute the coupled stopped modulus with the original common data; complex determinant versus real tangent volume, weighted singular growth, finite lifetimes and Borel extension remain unproved. No numerical or analytic bound is asserted.
REASON: Completed essential multivariable source comparison supports one bounded established-route attempt, not import of the desired estimate. A separate continuation assessment955 records the mathematical target for next-turn approval; this literature step derives no extension.
LITERATURE_REASON: The new tangential variable and full two-parameter determinant lie outside the ready one-variable assessments950/952, requiring essential multivariable variational and volume-growth coverage.
SCOPE: Two complex variables, one double-zero divisor q=0, unit flat raw conjugated-gradient flow at fixed physical time, rectangular real initial parameters, bounded bidisk and stopped density; no intersections of divisors, changed metric, global homology or actual-Xi specialization.

## Exact proposed target, not a result

Fix 0<a<R<infinity and 0<b<L<infinity. Let H be holomorphic on
B={|q|<R, |z|<L}, with specified H(0,0) and finite bounds
||grad H||_2<=M_1 and ||D^2 H||_op<=M_2 throughout B. The
derivatives here are complex holomorphic derivatives and the norms
use the standard Hermitian vector norm. Use the unit flat raw flow
dot q=overline(partial_q S), dot z=overline(partial_z S), starting
at (q,z)=(ir,s), where (r,s) lies in
I=(-a,a) times (-b,b), with r!=0.

Let tau(r,s) be the maximal forward lifetime in B minus {q=0}.
At fixed physical time T<tau, let J_T be the full complex 2 by 2
matrix of derivatives of (q,z) with respect to the real parameters
(r,s). The nominated density is
W_T=-q(T,r,s)^2 exp(-H(q(T,r,s),z(T,r,s))) det(J_T)/i.
Set W_T=0 for T>=tau and on r=0. This stipulation claims neither
continuation through a zero nor signed-integral invariance.
Any interpretation of finite lifetime as first zero hit or escape,
and measurability of this extension, must be justified for the new
scope; they are not supplied by citing C466r unchanged.

The proposed question is a finite class-uniform modulus omega(u)->0
as u decreases to zero for every Lebesgue measurable E subset I:
sup_{H,0<=T<=T_0} integral_E |W_T| <= omega(|E|), for some T_0>0
depending only on the displayed common data. No envelope or growth
constant is conjectured as an established bound. The review must
distinguish fixed-time full determinant control from separate
directional bounds, action phase, and modified-metric completeness.

## Nomination954 source-review plan, preserved

Reuse review950's inspected collision examples and the completed
C466r audit without repeating their searches. Search exact and
stronger results for coupled weighted Jacobians/volume evolution
near a logarithmic divisor, then inspect primary hypotheses and
essential singular cases. Compare the multivariable TNV variational
law with the above matrix and norm conventions before considering
its applicability. Check local duplicates narrowly before approving
an attempt. At nomination954 no primary theorem for this target had
been read; the completed source comparison is recorded below.

Continue only with a precise imported theorem, adequate coverage
for one bounded estimate or obstruction test, or an identified
essential source blocker. A theorem for the modified metric or an
uncoupled H is not coverage of the stated claim. A method failure
does not refute the modulus. Do not derive an extension in the
source review or approve and attempt newly uncovered mathematics
in the same turn.

Essential local comparison input: C466r; C466q is the frozen control
only. No cross-notebook result is involved. Plausible downstream
use is control of a local holomorphic factor depending on the
collision coordinate and a tangential coordinate. Original-coordinate
metric normalization, multiple intersecting collisions, noncompact
ends, homology, signed integration, all-degree signs and actual-Xi
realization remain unproved. Stops927/932/941/947/948 retain their
recorded scopes; no pointwise-sign or finite-jet route is reopened.

There is still no justified central creative target: a global
signed-contour condition relating such absolute control to the
actual determinant signs is missing. This concrete local extension
is nominated because coupling is an independent unpaid hypothesis,
not to fill a creative quota. Full matching Mathlib coverage has
not been checked. This assessment required its own source review;
audit954 alone did not approve its mathematical target.

## Primary comparison completed at step955

This source-only step preserves the exact proposed target above.
It supplies coverage for a bounded attempt, without computing a
coupled solution, determinant, envelope or counterexample.

**TNV convention and singular case.** Tanizaki, Nishimura and
Verbaarschot, *Gradient flows without blow-up for Lefschetz
thimbles*, JHEP10(2017)100, arXiv:1706.03822v2, 27 September
2017, [Appendix B PDF](https://arxiv.org/pdf/1706.03822v2),
[equations rendered in HTML](https://arxiv.org/html/1706.03822v2#A2).
Read (B.1)–(B.5), including the complete derivation from real initial
variations. For unit flat metric the matrix equation is
\(\dot J=\overline{(D^2S)J}\), with conjugation on both factors.
Our initial real parameters prescribe J(0)=diag(i,1), rather than
the identity used for a real initial plane. The general real-variation
derivation permits this initialization. On the punctured bidisk the
logarithmic derivatives are holomorphic; local nonsingular use of
the law needs no global thimble theorem. This is applicability of a
known identity, not a new determinant estimate.

The inspected Section2.2 simple-zero case omits regular terms.
Footnote2 conditions its discarded-mass discussion on the full
weighted Jacobian being bounded. Sections3.1–3.2 instead use a
decelerating metric and polynomial action/determinant assumptions.
They do not give the stipulated fixed-physical-time raw-flow modulus
for arbitrary holomorphic H on a bidisk. Review950's other collision
sources are reused without repeating their searches.

**Volume-growth input.** Wu, Kanevskiy and Margaliot,
*k-Contraction: Theory and Applications*, arXiv:2008.10321v2,
27 September 2021, [primary PDF](https://arxiv.org/pdf/2008.10321v2),
Sections2.2/2.4/2.5, printed pp5–7, and Proposition5, p9.
Read Proposition2/(11)–(12), (15)–(20), the compound-equation
derivation, Section3.1's continuous-A hypothesis, Theorem4/full
proof and Proposition5/full proof. For real continuous A(t), the
transition matrix's k-th compound obeys the additive-compound
equation and has norm at most
\(\exp\int_0^T\mu(A^{[k]}(t))\,dt\). In Euclidean norm,
\(\mu_2(A^{[k]})=\sum_{j=1}^k\lambda_j((A+A^T)/2)\), with
decreasing eigenvalues. Rectangular tangent volume is the Euclidean
norm of its minors. The proof uses the compound equation and
Coppel's inequality; uniform negativity is not needed for the
growth bound. Only finite nonsingular intervals are proposed here.
The global nonlinear contraction conclusions require further
existence/state-space hypotheses and are not imported.

For the nominated flow these are tools to investigate real tangent
two-volume. They are not a theorem bounding the complex determinant
with its weight. That comparison and uniform control near q=0 must
be supplied in the mathematical attempt; no such calculation is made
in this review. Any use on a surviving interval must check continuity
of its actual real variational matrix and retain a bound independent
of its distance to the divisor. A finite-cutoff estimate alone would
not meet the target.

**Additional multivariable comparison.** Nishimura, Sakai and
Yosprakob, *A new picture of quantum tunneling in the real-time path
integral from Lefschetz thimble calculations*, JHEP09(2023)110,
18 September 2023,
[published primary PDF](https://scoap3-prod-backend.s3.cern.ch/media/files/80354/10.1007/JHEP09%282023%29110_a.pdf).
Inspected AppendixA.2(A.5)–(A.9), p23, and A.4(A.30)–(A.35),
p27: the full Jacobian is retained, individual tangent displacements
are analyzed using a Takagi decomposition, and a changed flow is
introduced for numerical conditioning. No arbitrary-H stopped
weighted determinant modulus is stated in those passages. Its
displacement discussion is not a singular-volume theorem. No new
result is imported from it.

## Search record, overlap and decision

Queries used in this bounded discovery included:

- `"holomorphic gradient flow" "Jacobian" "singular" volume`
- `"logarithmic" "gradient flow" "uniform integrability"`
- `"holomorphic gradient flow" determinant zeros weighted Jacobian bound`
- `"holomorphic gradient flow" "Lagrangian" "Jacobian" determinant`
- `"holomorphic gradient flow" "volume" "bound" singularities`
- `"compound" "matrix measure" "volume" "k-contraction" theorem`
- `"holomorphic gradient flow" "logarithmic" "volume"`
- `"complex determinant" "real volume" "Lagrangian" inequality`

Primary papers above were followed from these searches. Irrelevant
PDE flows, secondary summaries and search snippets were not used as
theorem evidence. Broader sign-problem reviews and the later
compound-free contraction paper arXiv:2209.01046 remain unread leads,
not dependencies. No exhaustive literature absence is claimed.
Screenshot calls for TNV p22 and WKM p9 returned reference-only text
in this tool interface; no visual verification is claimed. TNV's
conjugations were read in its rendered HTML, and WKM's stated
inequalities and proof in the extracted primary PDF text.

Read C466r in full and C466q's hypotheses/conclusion/source convention;
searched reviews947/948/950/951/952 and working954 for the coupled
target. No existing coupled modulus was identified in that checked
scope. Read the concise stop927/932/941/947/948 records: respectively
common-product phases, conditional iid factorization, pointwise
marginal signs, nondiscriminating finite jets, and unsupported
collision-phase smoothness. Their evidence is preserved; none is a
no-go theorem for this absolute-mass target. No cross-notebook input
is involved.

EXPLORE is appropriate: the relevant primary machinery is accessible,
so there is no essential source blocker; no matching bound was read,
so IMPORT would overstate coverage. The exact unresolved estimate is
isolated and one volume-based proof attempt is now source-assessed.
This is source progress only, with STEP_OUTCOME EXPLORATION rather
than a mathematical advance or an informative negative bound.

The single mathematical continuation is nominated in
[assessment955](2026-11-14-coupled-weighted-flow-attempt-955.md).
It is newly written and needs separate approval before invocation.
Continue with a common integrable bound or an admissible failure of
the requested modulus; if the volume method fails, record which
estimate fails without calling that a counterexample. Preserve any
partial reasoning before changing mechanisms.

The downstream use and independent gaps in the preserved nomination
are unchanged. A global signed-contour condition linking local
absolute control to all-degree determinant signs is still missing;
no justified central creative target has emerged from this review.
The proposed continuation develops a local established route, not a
creative sign mechanism. Full matching Mathlib coverage is not
checked, and no absence or formal verification is claimed.
