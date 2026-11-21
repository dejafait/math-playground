# Actual-G real closed dual forms: domination and period test

TARGET: Test whether every real C1 closed two-form dominated by L847's absolute form on all radial-graph tangent planes has |integral_T alpha|<=|integral_T omega|, retaining every F and J zero.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the bounded exact/stronger closed-form-domination, real-two-form rigidity and calibration search in 2026-11-06-post-census-global-mechanism-discovery.md; scoped named contour assessments and failures contain no matching classification. No novelty inference.
SOURCE_EVIDENCE: Lawrence-Yamauchi arXiv:2311.13002v2 https://arxiv.org/html/2311.13002v2 Section III (18)-(20), rechecked directly; Lebl SCV v4.4 https://www.jirka.org/scv/scv.pdf Definition1.1.2/CR pp14-15 and Theorem1.6.1/proof pp40-41; Lebl CA v1.10 https://www.jirka.org/ca/ca.pdf Theorems3.3.10 and5.2.2/proofs pp80/125, all rechecked. Other previously inspected cases remain in the parent comparison.
COMPARISON: The cited sufficient bound applies once closedness and domination hold; it supplies no real-two-form classification for the coupled actual-G graph. One-variable examples, the holomorphic-subclass remark and generalized-chain duality do not decide this target.
GAP: Classify or adequately constrain the real two-form coefficients under the all-plane inequality, then combine C1 closedness with justified analytic continuation and torus periods. No rigidity, strict-gain certificate or graph is established.
REASON: A distinct global weighted obstruction can be tested without unknown contact data or a singular real-flux lift. This prepares one bounded research attempt after separate approval; no new mathematics is performed or approved as proved here.
SCOPE: Actual G,R,C,F,omega and graph orientation of L847; X=(C*)^2; real C1 ambient two-form alpha with d alpha=0 on all X, uniformly dominated as defined below for every zero-jet and every real derivative matrix A. Only this sufficient real smooth certificate class is tested. No bound on u or Du, finite census, nonzero J, zero simplicity or RH is assumed.

## Exact proposed test

Let T be L847's coordinate torus of radius R, with its original
orientation. At z in X and A in M_2(R), use the tangent vectors of
L847's graph with that zero-jet and derivative:

\[
 E_j(z,A)_k=z_k(A_{kj}+i\delta_{kj}),\qquad j,k=1,2.
\]

This is the already stated graph differential in L847, not a new
identity proved by this assessment. The proposed hypothesis is

\[
 |\alpha_z(E_1(z,A),E_2(z,A))|
 \leq |\omega_z(E_1(z,A),E_2(z,A))|
 \quad\hbox{for every }z\in X,\ A\in M_2(\mathbb R).
\]

No plane with J=det(I-iA)=0 is excluded. No point with F(z)=0 is
excluded. Domination is a bound on evaluations, not a coefficient
norm and not a Riemannian comass bound. The quantifier over all A
is part of this sufficient-certificate hypothesis; no claim is made
that each such jet belongs to an exchange-symmetric positive global
graph. This deliberately smaller certificate class must not be
silently identified with all possible obstructions to those graphs.

The sought conclusion is the period inequality in TARGET. Try a
pointwise classification of the six real two-form coefficients, then
use closedness and the cited analytic results only after verifying
their hypotheses. A possible stronger rigidity statement may be
investigated, but no representation of alpha as a real part of a
holomorphic form, no removability, and no global scalar bound is
assumed here. The problem is a bounded classification/period attempt,
not a search over successively larger numerical ansatz families.

## Required threshold, use and stopping decision

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
Essential local input is L847's full form, graph differential and
homotopy/Stokes interface; G,R,C are exactly its actual inputs from
L775. L864/L866's finite-census conclusions are not needed here.
No cross-notebook theorem is proposed.

The source's obstruction threshold is
|integral_T alpha|>|integral_T omega|. A certificate meeting it would
need a full global domination and period proof. Import the sufficient
closed-form bound by its precise citation and justify compact swept
chains in X using L847; do not reprove it, use strong duality, or
infer a graph from equality. Conversely, a proved no-gain inequality
for all alpha in this class stops that certificate mechanism at this
scope. It neither constructs a graph nor excludes less regular,
sign-cone-dependent or more narrowly dominated certificates.

Continue only with a valid strict-gain certificate or an informative
rigidity/range result. If the one attempt is inconclusive, preserve
the exact unsolved coefficient/closure case and require a materially
new input before repetition. No actual-G zero census, global graph,
higher-order sign, other-shift transfer or RH conclusion follows from
source coverage. Those independent gaps remain unresolved.

This is development of a cited global dual-bound mechanism with a
newly isolated applicability difference, not an automatic import or a
certified novel theorem. EXPLORE permits REPRODUCTION or
POTENTIALLY_NEW in the subsequent research report, according to what
is actually established. Full Mathlib matching coverage is unchecked.
This assessment was written during literature discovery. Its separate
literature approval and direct-URL repair were completed on 6 November
2026 below; no mathematics was performed in that approval turn.


## Separate source approval and URL repair, 6 November 2026

The exact TARGET and SCOPE are unchanged. This is the separate approval
of the previously nominated research target, not an approval of its
conclusion. DECISION remains EXPLORE. No missing essential source was
found; the direct URLs are now in this assessment itself.

Reopened [Lawrence-Yamauchi, Section III, equations (18)-(20)](https://arxiv.org/html/2311.13002v2#S3).
The bound requires closedness, domination of absolute evaluations and
homologous contours. The text uses strict domination in prose but
non-strict inequalities in (19); no strict margin is needed to use that
bound. The real C1 graph-plane class here is our stated sufficient
certificate class, not a classification claimed by the paper. Its
holomorphic remark is not a theorem for arbitrary real forms on X.
Reuse the parent assessment for the one-variable examples and duality
limitations; no strong-duality or attainment theorem is imported.

Reopened [Lebl, SCV v4.4, pp14-15 and 40-41](https://www.jirka.org/scv/scv.pdf#page=40),
including the complete extension proof. The CR characterization requires
C1 coefficient functions on an open set. The extension theorem requires
a domain U, nonidentically-zero holomorphic g, holomorphic data off its
zero set, and local boundedness throughout U. Its transverse-line and
Cauchy-integral proof includes singular divisor points; simplicity is
not a hypothesis. None of these analytic hypotheses for a quotient of
form coefficients is established by this review.

Reopened [Lebl, CA v1.10, Theorem3.3.10 p80 and Theorem5.2.2 p125](https://www.jirka.org/ca/ca.pdf#page=80)
and their full proofs. Liouville needs bounded entire one-variable data;
removal needs bounded holomorphic data near an isolated puncture.
Applying either on slices requires proving the scalar reduction and
bounds first. No global control on the noncompact X is supplied by a
compact-torus period alone. These are citation inputs if applicable,
not a request to reprove standard theorems.

Local overlap was rechecked against L847's hypotheses, full graph
pullback and compact-cylinder Stokes proof, the parent three-mechanism
comparison, and the open-ample and averaged-extension ATTEMPTS records.
Those stops concern different construction mechanisms and neither
settle nor prohibit this dual classification. No additional search for
novelty was undertaken; the bounded discovery coverage is reused.
Mathlib matching coverage remains unchecked.

Approval: the next invocation may perform exactly the stated bounded
classification/period attempt under EXPLORE. Its decisive alternatives
remain a global strict-gain certificate, a no-gain theorem for the whole
stated class, or an exact unresolved coefficient/closure case saved
without repeating the attempt absent new input. This process repair
is STALLED mathematically; it supplies no new RH input or budget reset.
