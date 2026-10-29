# Actual ordinary-middle bracket radical — source-covered target

TARGET: Determine the radical of L164's symmetric bracket form on the ordinary middle-fibre image using L111's actual incoming KS plane.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 564 searched symmetric-form radical/double-orthogonal statements and K3 polystable KS/moment-map comparisons; inspected the primary passages below and searched active-notebook lemmas and relevant assessments for duplicates. L111/L164 and ATTEMPTS/092–094 leave this exact restricted radical unidentified.
SOURCE_EVIDENCE: Inspected Conrad, Bilinear Forms, 63-page author-hosted version, Theorem 3.12 and proof, pp. 18–19; Munemasa, The geometry of orthogonal groups over finite fields, initial definitions and Proposition 1.1 with proof, pp. 3–4; Arbarello–Sacca (2018), Proposition 6.1 and proof, pp. 680–681; live Stacks 0B91,0FP6,0H99. Reuse the inspected real-Kahler coverage and actual-map framework recorded below.
COMPARISON: Standard radical and double-orthogonal identities cover the finite-dimensional operation, and existing sources cover the necessary actual-family obstruction and derived cup comparison. They do not identify L164's ordinary image with the relevant annihilator for these actual incoming KS vectors; L164 currently gives only rank>=48 and the full-derived-space t>26 test.
GAP: One separate mathematical attempt must match L111's reduced ordinary-image inclusion, incoming KS vectors and L164's stabilizer/trace form, using integrability only on the actual base tangent plane. Neither the radical, its rank nor any new section threshold is calculated here; no essential unread source blocks this specialization.
REASON: Approve exactly TARGET for one bounded RESEARCH / REPRODUCTION specialization of the inspected linear algebra and established conditional family. Import the general identities without reproof; justify the actual-map specialization. No radical identification or exclusion is approved as a result by this literature turn.
SCOPE: Exactly the conditional family and split-point question retained below; general s,t, actual maps and real h. No ordinary middle-base-change isomorphism, arbitrary section integrability, endpoint, genericity or F existence is assumed.

LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changed from trace normalization to the restricted ordinary-middle radical. This turn supplies its missing bilinear-form/theorem comparison while reusing adequate real-Kahler and derived-map assessments; it does not repeat the normalization audit.

Main gap: primitive Hodge realization and existence of F remain open.
This is one proposed intermediate target, not a calculation performed
or approved in step 563. Under the entire L111/L164 conditional family,
write Q_z=e_z(M(z)) inside E_z=H^1(S_1,V_z). Determine
rad(B_z restricted to Q_z), using the actual incoming vectors
v_i=-ad_{h_0} KS(u_i), not an arbitrary codimension-two subspace.

Plausible downstream use: an identified radical and induced quotient
would specify which ordinary-fibre directions contribute to L169's
actual point quadrics. It might sharpen a section-image test, or show
that the existing threshold cannot improve by this local mechanism.
Neither conclusion alone determines actual global section values or
quartic square length, and no improvement is presumed.

Essential inputs to assess: L111, L164, the actual base-tangent
integrability input of L094 and the section evaluation framework of
L116. L169 motivates the downstream quartic; it adds no hypothesis
about these section values. Retain L071 and L108/L109/L115 through
the stated conditional family. No cross-notebook theorem is used.

Retain identical marked K3 factors, the fixed common metric/triple/forms
and actual connection, hypothetical locally free rank-two
product-polystable F with integral c_1=0 and full character
2-14e_1-21e_2-tau_D+62P, actual j,e_z,theta_z and h_0.
No ordinary middle-base-change isomorphism, section integrability,
semistability beyond established inputs, genericity, F existence,
endpoint s=800,t=48 or numerical trace convention is assumed.
The local question is at a split point; if Z is empty it is vacuous.

Continuation test for a later approved attempt: identify the actual
restricted radical (or exhibit the precise missing compatibility) and
compare its dimension/rank with L164's already established rank>=48
and t>26 test. If this only reproduces an existing bound, record that
limit and do not infer section vanishing or nonexistence. A failed
actual-image comparison requires preserving L164's weaker statement.
ATTEMPTS/092–094 stay parked: an additive splitting, scalar-isotropic
lift or cyclicity alone cannot evaluate the bracket. Do not carry out
this calculation in the source-approval turn.

Full matching Mathlib coverage is unchecked. This record neither
certifies novelty nor proves a new lemma. The completed comparison
below supersedes the proposal's source gate, not its mathematical limits.

## Completed source comparison — step 564

2026-10-26. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. The proposal above was saved in step 563 and
was not then approved. This separate source turn makes its unchanged
target ready for a later mathematical attempt. No new radical identity,
rank calculation, section bound or mathematical script is produced.

### Primary statements and essential cases

Keith Conrad, *Bilinear Forms*, author-hosted 63-page version accessed
2026-10-26, [Theorem 3.12 and proof, pp. 18–19](https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf#page=18).
For a finite-dimensional symmetric or alternating bilinear space,
the theorem characterizes nondegenerate subspaces by zero intersection
with their orthogonal complement and by an orthogonal direct sum.
If the ambient form is nondegenerate, it gives the complementary
dimension formula and double-orthogonal identity. Read the proof's
restriction-to-the-dual argument and its dimension/containment step.
Both symmetric and alternating cases are explicitly included, so
the statement applies separately to the two forms already retained
in L111/L164 over C. Do not transfer an orthogonal complement from
one form to the other without checking the actual stabilizer action.
The general theorem needs no reproof; that comparison is the local task.

Akihiro Munemasa, *The geometry of orthogonal groups over finite
fields*, lecture notes based on 1994/1995 lectures, author-hosted
40-page version accessed 2026-10-26,
[Section 1 definitions and Proposition 1.1, pp. 3–4](https://www.math.is.tohoku.ac.jp/~munemasa/documents/polar.pdf#page=4).
The opening section explicitly takes finite-dimensional spaces over
an arbitrary field K. It defines the restricted radical as
U intersect U-perpendicular and gives dimension and double-orthogonal
formulas allowing a degenerate ambient form. Read all three assertions
and their proofs. Only these opening arbitrary-field statements are
relevant over C; later finite-field orthogonal-group results are not
imported. This is corroborating standard coverage, not a stronger
result identifying our geometric subspace.

E. Arbarello and G. Sacca, *Singularities of moduli spaces of sheaves
on K3 surfaces and Nakajima quiver varieties*, Advances in Mathematics
329 (2018), 649–703, DOI 10.1016/j.aim.2018.02.003,
[Proposition 6.1 and complete proof, pp. 680–681](https://www.math.columbia.edu/~giulia/Quiver.pdf#page=32).
Its hypotheses are a polarized K3, distinct stable factors and their
polystable sum with multiplicities. Equivariant Ext identifications
carry the quadratic Kuranishi term to the quiver moment map. The proof
separates self and opposite Ext blocks and refers the final moment-map
comparison to Kaledin–Lehn–Sorger Section 3.4. Reuse the previously
inspected (5.5), p. 675, and opposite-block composition coverage in
`2026-10-25-adjoint-point-obstruction-projection.md`.
This related theorem neither identifies an ordinary direct-image
subspace nor evaluates its restricted radical. It is not imported
as a real-h moduli chart, formality assertion or section-integrability
theorem; the analytic coverage below handles the actual Kähler form.

Re-inspected live Stacks [36.30.4, 0B91](https://stacks.math.columbia.edu/tag/0B91),
including both alternatives and its reduction proof: a proper finitely
presented flat morphism with perfect coefficient has perfect derived
pushforward commuting with arbitrary base change. The smooth projective
product projection and locally free V satisfy these hypotheses.
This does not imply ordinary R^1 base change. Also re-inspected
[20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6), its full
composition diagram and counit proof, and
[20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99), its full
commutative-square statement (proof omitted in the source).
These cover the relative cup's functoriality used by the existing
actual-map comparison; they do not make a chosen additive splitting
multiplicative. The latter page has a reported parenthesis typo in
the displayed diagram; its stated objects and base-change maps are
unambiguous. No changed mathematical hypothesis is inferred from it.

Reuse the inspected analytic statements and relevant proof cases in
`2026-10-12-split-equality-tangent-critical-audit.md`, pp. 81–84,92–93,
and their exact-scope use in the projection and L164 audit assessments.
The primary citation is Buchdahl–Schumacher, *Polystable bundles and
representations of their automorphisms*, Complex Manifolds 9 (2022),
78–113, DOI 10.1515/coma-2021-0131,
[Lemma 2.5, Proposition 2.6/(2.4), Corollary 5.3/(5.1)](https://d-nb.info/1262812674/34).
The compact Kähler central bundle may be polystable at a real form;
the estimates require Sobolev p>2 dim_C X. Gauge fixing is complex
gauge fixing, and the harmonic unitary moment map is in one complex
structure. L094 supplies the actual ASD-family comparison and the
necessary tangent obstruction, not integrability of arbitrary sections.
A fresh fetch returned HTTP 429; the unchanged previously inspected
coverage is adequate and is reused, so this is not an essential source
block. No new analytic claim depends on that failed fetch.

### Local comparison, duplicates and remaining work

The narrow proof reads were L111's hypotheses and actual paired
complex through (12), L164's ordinary-to-derived map construction,
(4)–(5), rank argument and separate audit, and L094's necessary
quadratic term and actual-family bridge (5)–(6). L116's retained
truncation and full trivial section summand fix the downstream meaning.
The relevant existing local facts are L111's v_i=-ad(h_0)KS(u_i),
its nonzero alternating KS pairing and its orthogonal Koszul splitting;
L164 retains the reduction of that splitting for the actual inclusion
and the relation between its symmetric bracket form and alternating
trace form. These are existing inputs, not new results of this review.

The calculation still has to check that these are the same vectors,
maps and normalizations after reduction; that the quadratic obstruction
used is the one vanishing on the actual base tangent directions; and
that the resulting orthogonality statements identify the restricted
radical. No result of that calculation is asserted here. A separate
attempt may import the elementary linear identities and establish
only this specific applicability comparison; rederiving general
duality, slice or Kuranishi theorems would add no needed coverage.

The notebook search for radical, restricted symmetric form, ordinary
middle bracket and KS isotropy found L164's rank>=48 argument but no
existing identification for this actual subspace. L163's Hermitian
factor radicals concern a different form and do not settle this one.
ATTEMPTS/092 leaves section-image values undetermined; /093 concerns
scalar isotropic lifts with an uncontrolled complement; /094 concerns
the global complementary operation. These obstructions survive.
This is a testable domain comparison, not a reopening of bracket
vanishing by an additive splitting or cyclicity.

External discovery queries included `symmetric bilinear form isotropic
subspace radical orthogonal complement quotient nondegenerate`,
`K3 polystable sheaves Kodaira Spencer tangent moment map quadratic
obstruction orthogonal complement radical`, author-scoped bilinear-form
queries, and `"middle" "radical" "Kodaira-Spencer" bundle`.
Primary passages above were read rather than relying on snippets.
The exact-phrase searches gave no matching geometric theorem; that
does not establish novelty. No unread lead is essential to the bounded
linear comparison. Full Mathlib matching remains unchecked.

### One bounded mathematical continuation

Use exactly TARGET, with L111/L164/L094 and L116's framework, retaining
L071/L108/L109/L115 as conditional family inputs. L169 remains only
downstream motivation. No cross-notebook theorem is used. Continue if
the actual-map checks identify the radical or isolate a precise missing
compatibility. Compare the achieved rank and section consequence with
the already recorded rank>=48 and t>26 thresholds; a reproduction
without a sharper consequence must be reported as such. If the image
comparison fails, retain L164's weaker statement. If only unknown
section values remain, park this local mechanism instead of inferring
vanishing or nonexistence. Empty Z is vacuous. F existence, global
section values, the complementary operation, minimum quartic square
length, transport and primitive Hodge realization remain unresolved.
