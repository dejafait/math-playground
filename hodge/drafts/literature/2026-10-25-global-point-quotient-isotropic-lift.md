# Actual Serre-isotropic lifts to the point quotient — proposed specialization

TARGET: Test whether every vector of H^0(B,W) has a Q-isotropic lift in H^2(X,End_0(F)) using L116's actual trace-duality retraction.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 545's global-obstruction assessment searched isotropic-cone projections, CY4 isotropic Kuranishi terminology and stronger relevant results; compared actual L116/L164 with ATTEMPTS/068,/092. No inspected result states this actual-map lift test. This is not a novelty claim.
SOURCE_EVIDENCE: Direct primary sources: https://stacks.math.columbia.edu/tag/0BRT (Lemma 48.15.7), https://stacks.math.columbia.edu/tag/0G81 (Remark 48.12.6), https://stacks.math.columbia.edu/tag/0FVU (Lemma 48.27.1 and Remark 48.27.2); EKM I.1.6/I.1.9 https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=23; supporting Mathlib https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.html. Reuse step 545 for EKM; step 546 reread the Stacks statements/proofs and Mathlib declaration. L116 supplies the actual retraction, not the future Q-restriction comparison.
COMPARISON: Known duality and quadratic-form theorems supply the framework. The remaining specialization is to verify the actual restriction on H^1(B,M), compare its orthogonal complement through a and r, and decide surjectivity of the null cone onto H^0(B,W). No sign, orthogonality, lift or answer is proved in step 545.
GAP: The actual Serre-form comparison and pointwise lift test remain undone. Even surjectivity would not construct the actual bracket, a polynomial Kuranishi map, compatible kernel or algebraic cycle.
REASON: Step 546 separately approves the unchanged bounded target after repairing its missing direct source URLs and checking source hypotheses against its scope. General tools are covered; the actual-map specialization is reserved for the next research turn. No new mathematical claim is approved as proved.
SCOPE: Conditional L071/L116/L164 family on identical marked K3 factors; fixed original metric/triple and real product class; actual trace-free coefficient and j,a,r; arbitrary unknown t and possibly empty Z; finite-dimensional pointwise complex linear algebra only.

## Mathematical purpose and boundary

The main gap is primitive Hodge realization; existence of the equality
kernel F is still unproved. This test addresses the narrower question
whether a full scalar isotropy condition could by itself constrain
L164's point bracket when the complementary component is unrestricted.
It uses the actual global form Q, not arbitrarily assigned matrices.

Essential inputs are L071,L116,L164; L108,L109,L111,L115 remain as
used in L116. No cross-notebook input. Retain locally free rank-two F,
integral c_1=0, ch(F)=2-14e_1-21e_2-tau_D+62P and L071's actual
connection. Put V=End_0(F), C=Rp_*V, M=R^1p_*V and W=R^2p_*V.
Use the exact sequence with kernel H^1(B,M) and quotient H^0(B,W),
and the retraction r constructed from the actual trace adjoint in L116.
The question is whether the Q-null cone in H^2(X,V) maps surjectively
under H^2(a). Keep M=T_B direct sum N and its actual alternating
form, unknown t, and possible Z empty. Orthogonality must be checked;
an arbitrary splitting is insufficient. If a dimension claim is used,
justify it from these inputs, including the tangent-bundle summand,
rather than a numerically guessed positive dimension.

Import the precise general theorems cited in the completed global
assessment without reproof. Their specialization still has to verify
the coefficient, shifts, symmetric global sign, normalization and
restriction to the included kernel. EKM's nondegenerate-subspace
theorem is conditional on that restriction; it does not supply it.
The scalar normal-form theorem does not compare the actual arrows.

This test does not need a Kuranishi map. It treats isotropy as a
condition on an otherwise unspecified element of the actual obstruction
space. Thus no extension of Cao--Leung's SU(4) theorem, derived
moduli scheme construction, trace-free formality or identification of
analytic charts is a hidden prerequisite. If a proof attempts to use
one of those stronger statements, stop and request separate coverage.

Continuation/abandonment test: prove null-cone surjectivity using the
actual pairing, or exhibit an actual quotient vector with no isotropic
lift. The former parks scalar-isotropy-only projection exclusion; it
does not rule out stronger polarized, polynomial or geometric constraints.
The latter supplies a necessary condition whose comparison with the
actual beta would remain separate. Failure to control the actual
restriction must be recorded, not replaced by a chosen orthogonal model.
No value of t, beta or either actual obstruction component, integrability,
existence of F, transport or primitive realization is assumed or concluded.

Mathlib: only the supporting algebraically closed quadratic-form normal
form in the completed assessment was inspected. Full matching coverage
for this actual-map test is not checked. No numerical experiment or
mathematical script is needed for the proposed proof attempt.

## Step 546 — separate source approval and URL repair

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs
in this ready assessment. This review repairs that evidence field for the
unchanged target; it does not repeat the broader Kuranishi-source search.

On 2026-10-25 the direct Stacks pages above were retrieved and their
statements and proofs read. Lemma 48.15.7 requires a smooth proper morphism
of relative dimension d over a Noetherian base and identifies its relative
dualizing complex with the top relative differential sheaf shifted by d.
Remark 48.12.6 requires a pseudo-coherent second input and a pairing
inducing the displayed derived-dual isomorphism; its pushforward pairing
is specifically cup product followed by trace. This is a conditional
perfectness theorem, not a guarantee about an arbitrary subspace.
Lemma 48.27.1(5),(7) gives duality compatible with shifts and triangles
and the smooth dualizing complex. Remark 48.27.2 identifies evaluation
followed by trace and requires bounded coherent input for a perfect
pairing on both sides. These are imported general results, with no reproof.

For applicability, L116's hypotheses give smooth projective K3 factors,
a smooth proper projection, locally free V, perfect bounded coherent C,
and fixed canonical trivializations. Its proof, equations (5) and the
following definition of r, uses the actual trace adjoint and b. This
supports the proposed comparison. It does not itself assert the global
Q-restriction, its sign, its nonzero dimension or an orthogonal splitting
on middle cohomology; those remain precisely the proposed specialization.
W retains finite support and is not assumed locally free. Unknown t and
empty Z remain allowed. No analytic isotropic Kuranishi theorem is needed.

Reuse step 545's inspected EKM Chapter I Proposition 1.6 and Corollary
1.9, printed pp. 13–15, for orthogonal splitting of a nondegenerate
subspace and diagonalization of symmetric bilinear forms in characteristic
not two. The direct author PDF was opened this turn, but targeted text
finds did not resolve the proposition labels and the screenshot wrapper
returned no inspectable image. No fresh PDF theorem inspection is claimed;
the adequate prior recorded inspection is reused as instructed. These
statements do not determine whether the actual kernel restriction is
nondegenerate. Their hypotheses must be verified in the research step.

The current Mathlib declaration was inspected directly: finite dimension,
algebraically closed field, invertible 2, and a separating associated
form are required by
`QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed`.
This is supporting scalar normal form only; full matching actual-map
coverage remains unchecked. Do not use this normal form before verifying
its nondegeneracy hypothesis for the form to which it is applied.

Scoped duplicate/failure comparison reuses step 545 and reads
ATTEMPTS/068,/077,/080,/092. The lift test is distinct from repeating
zero Leray transgression, positivity/index imports or full-section bracket
vanishing: it asks about the information in scalar isotropy when the
complementary component is unrestricted. It neither determines the
actual bracket nor constructs F. The main gap, intermediate target,
downstream use and discriminating test above are unchanged. Assessment
approved as SPECIALIZE for that exact target only; no new lemma or
mathematical script, lift, orthogonality assertion or null-cone conclusion
has been produced in this literature-only turn.
