# Source review: one extra label after a square-support obstruction

TARGET: Test whether adding one common unused label from the existing129-index grid to C998w's35 labels permits nonnegative degree34 rules for all k=11,...,71, without per-block NNLS or inverse recomputation, at original-measure residual<=5e-19, B^2 uniform error<=1e-7 and complete preparation/validation work<=10^8.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison737 searched signed-weight node addition, prescribed nodes and fixed-degree nullspace feasibility; inspected van den Bos--Sanderse1902.07477v2 and Boyd--Vandenberghe2004 primary text. Narrow local support/extension searches found736 nomination but no prior ready36-node certificate. Reuse732/comparison733 and729/comparison730 for unchanged verified-system/residual coverage; no novelty inference.
SOURCE_EVIDENCE: Read van den Bos--Sanderse arXiv:1902.07477v2 Sections2.1/2.3/2.4,3.1 Theorem2/(3.3)-(3.14) and both proof directions,3.2.1 and Lemma3 hypothesis; Boyd--Vandenberghe Convex Optimization(CUP2004),Sections4.1.3 p132 and4.2.4 pp142-143,equality-elimination statement and equivalence argument. Reuse Rump2010 Theorems10.2/10.6/10.8 and original discrete residual/analytic-approximation sources inspected733/730.
COMPARISON: The quadrature extension increases degree and its positive-base geometry is insufficient for this fixed-degree signed-start problem. General equality elimination instead accepts any particular solution and a certified nullspace basis; it supports a finite nonnegative-feasibility test without a positive starting rule. It guarantees neither feasibility nor residual/cost success. C998w Section7 remains an obstruction only on the unchanged35 nodes.
GAP: Derive and validate only the instance-specific fixed-degree parametrization, signs and rounded residuals;test at most94 unused labels with one label common to all61 blocks. Reuse of734 preconditioners and735 contraction must be justified for the retained square systems;all original moments,Gram inclusion,error,complete production/validation work and byte storage remain unpaid.
REASON: The newly inspected equality-elimination result closes the signed-start source gap for a bounded known-method specialization. No extension formula,label,feasibility,original residual or affordable construction is derived737. This changed ready continuation receives separate approval next turn;it does not reopen the exhausted35-support family.
LITERATURE_REASON: Changed essential hypotheses:36 instead of35 prescribed nodes,fixed degree34,one free weight and a signed starting solution required fresh primary comparison;737 supplies general equality-elimination coverage rather than importing positive-base geometry.

The following nomination is preserved as the invocation-start proposal.
Its pending-coverage statements are superseded only by comparison737 below.

This is a nomination, NOT a ready assessment or mathematical result.
Do not derive an extension formula or test candidates during its review.
Read the exact primary hypotheses and relevant proof cases first; check
duplicates and the736 separating polynomial before judging applicability.
The proposed finite search would allow at most94 unused grid labels,
one common added label for all61 actual dyadic blocks, the original
measures and residual, and734's preconditioners where justified. It
must not silently replace the original measure by a density, rerun
per-block NNLS/inverses or treat old production as free. Stop on a
source mismatch without a covered finite test, or on a later bounded
feasibility/residual/cost failure. No new support label is selected here.

Essential inputs for the separate review: C998w Sections5-7, exact736
separator and735 contraction, assessment732/comparison733, unchanged
residual assessment729/comparison730, C998v Sections1-3/5. Retain
C998u Section2,C998t/C998s,C744z(1),C999l(1),C998r witness and all
analytic-response/neutral-core/IEEE754/Decimal/unreplayed c_* contracts.
The exact736 obstruction itself does not assume Decimal correctness.
Main actual-Xi positivity/signed S3, H2, density, mixed interactions,
other entries/endpoints, remaining9e-7 and global assembly remain open.
No cross-notebook input or original-operator inverse. Full matching
Mathlib coverage for this changed target has not been checked.


## Completed primary-source comparison737 — 13 November2026

### Exact source distinction

L.M.M. van den Bos and B. Sanderse, *A geometrical interpretation of
the addition of nodes to an interpolatory quadrature rule while
preserving positive weights*, [arXiv1902.07477v2](https://arxiv.org/html/1902.07477v2),
23January2021; published J.Comput.Appl.Math.391(2021),113430,
DOI10.1016/j.cam.2021.113430. Inspected Sections2.1/2.3/2.4,
3.1/Theorem2 and both proof directions,3.2.1 and Lemma3's hypothesis.
Distinct nodes and exact finite moments underpin(2.4)-(2.6).
Theorem2 characterizes nonnegative weights after extending degree N
to N+1; its proof solves the next-moment correction(3.3)-(3.13).
Display(3.14)'s equality is valid only at the boundary, not under every
nonstrict inequality. Section2.4 and Lemma3 use positive starting rules;
Theorem1's removal argument also starts with nonnegative coefficients.
The printed Theorem2 statement says interpolatory, but this does not
supply our degree34 free-weight test on36 nodes. No signed-start
geometric corollary or discrete-density extension is imported.

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*,
Cambridge University Press2004, Section4.1.3,p132, “Eliminating linear
equality constraints,” and Section4.2.4,pp142-143,
[author book PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Read the complete relevant paragraphs and the two-direction equivalence
argument; PDF zero-based pages145 and155-156 were inspected.
For a consistent real system Ax=b, any particular solution x0 and
matrix F with range equal to ker(A) parametrize ALL solutions by
x=Fz+x0. A full-column-rank F has n-rank(A) columns. Substitution
into the inequalities gives an equivalent feasible problem. The
particular solution need not satisfy those inequalities. The text
separately handles inconsistent equalities as infeasible and warns
that elimination can harm computational efficiency. These are the
imported general statements, not new local mathematics. The copy's
revision date is unverified; the book edition and printed pages identify
the source. No algorithmic complexity or numerical enclosure is imported.

### Applicability and bounded later test

The unchanged target is a finite real equality/nonnegativity problem:
original nu_J moments through degree34, evaluation at the35 retained
nodes plus one candidate original node, and36 nonnegative weights.
This falls within the imported general feasibility framework without
requiring a density, positive base weights, or any smooth dependence
on J. Use the existing square interpolation system of C998w Section5
as the source of rank/consistency information. Verify the extra column,
nullspace parametrization and its completeness explicitly in the later
research step; no local parametrization or one-node formula is derived
here. The Chebyshev basis does not alter the polynomial space. No
next-moment degree35 equation is part of this target.

A covered prescription may eliminate the exact moment equalities and
intersect the resulting scalar nonnegativity constraints, with outward
certification or exact rational comparisons. Alternatively it may
choose an exact finite-decimal free weight and validate the retained
square solve. All36 signs must then be proved. A signed particular
solution is merely algebraic input, never a positive quadrature rule.
No new label or scalar is selected in this literature step. The
necessary finite algebra is a specialization of the cited general
method, not a reproof of a quadrature existence theorem.

Bound the later attempt in advance: at most94 unused labels, tested
in increasing label order with rejection at the first certified failing
block, k increasing from11 through71. ONE label must survive every
block; the free scalar/weights may differ between blocks. Preserve
all failed cases; fix precision, iteration limits and a paid work-stop
rule before calculating. No per-block NNLS, inverse regeneration,
new support family or repeated precision/anchor sweep is covered.
Use734's exact R_A/R_H and735's FINAL d,M where applicable. Their
existing certificate covers only the original square A systems;
it is not an inverse or inclusion for a rectangular36-column matrix.
Every new right side, null direction or moment enclosure needs its
own validation. Reuse Rump10.2/10.6/(10.14)/10.8 precisely as assessed733;
a shared preconditioner is allowed but inclusion is not guaranteed.
Zero-containing weight intervals are inconclusive unless exact
nonnegativity is otherwise proved. Do not clamp negative weights
without validating the changed rule against the original moments.

Even certified infeasibility of EXACT degree34 matching on a given
36-node support does not alone exclude an approximate positive rule
at residual5e-19. It can stop this exact-matching construction; an
impossibility claim at the allowed tolerance requires a certified
original-measure residual lower bound. C998w Section7's35-node
separator cannot be transferred without checking the added node.
A failed sufficient interval criterion likewise rejects only that
certificate. These distinctions preserve the exact target and prevent
inflating a diagnostic into a36-node impossibility result.

### Reused residual, error and full-accounting gates

Reuse assessment729/comparison730: Piazzon--Sommariva--Vianello2017,
Proposition1.2/(7)-(15), for nonnegative weights on ORIGINAL discrete
support and residual in the ORIGINAL-measure orthonormal norm;
Trefethen ATAP Theorems8.1-8.2 for the unchanged analytic approximation.
C998w Sections1-3 identify the Gram norm and conditional zero-inclusive
transfer. Adding an original support point does not replace those
hypotheses. Rounded output weights require their own certified residual
<=5e-19 on all61 blocks, not just existence of exact weights or a tiny
raw Chebyshev residual. The B^2 uniform bound<=1e-7 is still conditional.
No reproof or refreshed literature search for this unchanged part.

Price the ENTIRE prescribed construction/validation before expensive
work, using C998v Section5's source-operation convention and explicitly
resolving its omissions for any upper-bound claim. Count94-candidate
search work actually required, original moments through68, all retained
rules/atoms, anchor and radius production, preconditioned solves,
sign/residual checks, exact replay, directed arithmetic, bindings,
control/output and integer/Fraction internal work. Record peak entries
AND bytes at the fixed precision, including candidate-search data and
certificates. Existing verified artifacts can be incremental mathematical
inputs; their production is not free for a complete preparation claim.
The old33,326,300 and62,769,000 figures remain LOWER bounds, not budget
passes. No new work/storage estimate is derived here.

Continue only on a rigorously surviving common label, validated
nonnegative output and original residual on all61 blocks, the uniform
error threshold, and complete work<=10^8 with explicit storage. Stop
this prescription on exhausted certified scalar-feasibility tests,
bounded validation failure or an above-cap complete ledger; distinguish
inconclusive arithmetic and exact-matching-only failures as above.
Passing pays kernel preparation only, not the scalar or signed S3.
Preserve736 and729/732/734 stops and735's useful contraction input.

Queries: `quadrature negative weights addition van den Bos`,
`prescribed quadrature nodes one additional node degree fixed signed
weights positivity null space`, and `Boyd Vandenberghe convex
optimization eliminating equality constraints x x0 Fz 4.2.4 pdf`.
Only the primary texts above supply the changed coverage. Other
quadrature search hits, the author's dissertation and general prescribed
Gauss-type leads were not inspected as essential theorem evidence.
Local checks were confined to support/extension assessments and stops;
no cross-notebook theorem input or global novelty claim is made.

Mathlib: full matching coverage for this fixed36-node family and its
validated numerical/cost certificate has not been checked. Supporting
linear algebra is not claimed to constitute such a full theorem.
Main actual-Xi positivity, signed remote-plus-induced S3, density,
mixed interactions,other entries/endpoints,remaining9e-7,C744q/H2 and
global assembly remain open. No source-qualified new central sign
mechanism emerges from this preparation review; the creative-target
blocker persists. Local progress is a known-method source gate, with
no progress beyond the inspected general results or new sign theorem.

SCOPE: Only the unchanged TARGET,at most94 added original-grid labels,one common label for61 blocks,degree34,734 preconditioners and735 final contraction;no per-block NNLS/inverse,no degree35 requirement,no central sign claim. Ready coverage written737 requires separate next-turn approval before research.
