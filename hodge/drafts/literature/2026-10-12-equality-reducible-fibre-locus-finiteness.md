# Equality kernel — reducible-locus finiteness source assessment

TARGET: Assess whether L095's nonzero harmonic derivative forces the reducible S_1-fibre locus of the hypothetical (14,21) kernel to be finite.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L071/L094/L095, 2026-10-12 slice/line-twist assessments, histories 240/242/244 and ATTEMPTS/061 contain no finiteness proof; bounded reducible-ASD and harmonic-family searches located the general slice and a differently hypothesized finite-gauge-class discussion, not this exact family theorem.
SOURCE_EVIDENCE: Diez--Rudolph (2022), Theorem 5.3 with full proof, Remark 5.5, Section 5.3 (5.14)--(5.23)/Theorem 5.8, Definition B.1 SL1--SL5, Proposition B.2, Appendix A Theorem A.1; Stacks 36.30.1 (0A1H), Noetherian case 36.27.2 (0DJQ), derived-base-change 36.26.4 (0A1D), and 36.31.1 (0BDI), statements and relevant complete proofs, inspected 2026-10-12.
COMPARISON: Primary coverage supplies orbit-intersection control, smooth local slice choices, finite-dimensional harmonic coordinates and upper semicontinuity of fibre cohomology; L071 and audited L094/L095 supply the exact-metric classification and derivative. No inspected theorem directly states finiteness of this parameter locus.
GAP: A separate attempt must match split fibres to one determinant-fixed unitary orbit, prove local isolation using the actual slice derivative, identify the reducible set by fibre endomorphism dimension, and justify closedness plus compactness. This assessment proves no assembled locus conclusion.
REASON: Essential source coverage permits one bounded known-tool specialization at the unchanged real metric; import the cited theorems and derive only the exact-family locus passage in a later research turn, without reproving slice or semicontinuity theory.
LITERATURE_REASON: Gate-required global-locus comparison; the ready derivative audit omitted essential SL2/SL3 orbit-return and fibre-locus closedness scope. Its harmonicity coverage is reused.
SCOPE: Identical marked K3 metrics, hypothetical locally free rank-two Omega-polystable F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D; S_2 parametrizes S_1 fibres. One bounded attempt may test set-theoretic finiteness, allowing an empty set. No generic stability, smooth quotient, multiplicities, reduced locus scheme, integrated germ, F existence or transport is assumed or concluded here.

Essential local inputs are L071's actual connection and exact-h
stable/split alternatives, audited L094's unitary slice at the split
connection, and separately audited L095's actual harmonic derivative
and positive norm. L093's equality boundary supplies context only;
it does not establish a global fibre-type statement. No cross-notebook
input is proposed.

Main gap: universal primitive rational Hodge realization. Nearer gap:
equality-kernel existence and realization of the prescribed full mixed
action. A finite reducible locus could isolate the exceptional points
before applying stable-moduli tools on their complement. It would not
construct a kernel, exclude it, or extend such tools across those points.
Integrated germs, higher-order constraints and transport remain open.

## Primary coverage and qualifications

Tobias Diez and Gerd Rudolph, *Normal form of equivariant maps in
infinite dimensions*, Ann. Global Anal. Geom. **61** (2022), 159--213,
version of record published 14 October 2021, DOI
[10.1007/s10455-021-09777-2](https://link.springer.com/article/10.1007/s10455-021-09777-2).
Fresh reads cover the locators above, including the full Theorem 5.3
proof and ASD specialization. Theorem 5.8 applies to compact semisimple
groups on compact oriented Riemannian four-manifolds. SU(2) at this K3
metric qualifies without irreducibility or a rational polarization.
It provides a finite-dimensional obstruction chart. Definition B.1
SL2 controls slice/orbit intersections; SL3 supplies smooth local gauge
choices; Proposition B.2 supplies the tube. Import these, retaining
the residual stabilizer. Neither smooth quotient nor exact quadratic
model is claimed. Appendix A.1 states the Banach inverse function
theorem, citing Lang, *Fundamentals of Differential Geometry*, Theorem
I.5.2; its finite-dimensional application still needs a justified
projection of the actual derivative.

The post-(5.23) finite-reducible-class discussion assumes instanton
number one and simply-connected positive-definite intersection form,
which fail here. It concerns gauge classes, not family preimages.
The adjacent discrete-stabilizer/flatness remark is not imported;
audited L094 remains the stabilizer input. General orbit-type
stratification is not an automatic conclusion there either.

The Stacks Project, live tagged statements inspected 12 October 2026:
[Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H),
[Lemma 36.26.4, 0A1D](https://stacks.math.columbia.edu/tag/0A1D),
[Lemma 36.27.2, 0DJQ](https://stacks.math.columbia.edu/tag/0DJQ), and
[Lemma 36.31.1, 0BDI](https://stacks.math.columbia.edu/tag/0BDI).
Read the statements, 0A1H's Noetherian reduction, the complete 0A1D
and 0DJQ proofs, and the complete semicontinuity proof. Prior line-twist
coverage already included 0A1H/0BDI; this comparison changes the
coefficient to End(F), not the metric or the connection theorem.

0A1H requires finite presentation of the morphism, a perfect first
object, and a bounded finitely presented base-flat coefficient complex
with proper support. It gives perfect pushforward and arbitrary
derived base change. Here p_2 is projective and flat, O is perfect,
and End(F) is locally free, hence base-flat. The Noetherian case applies
directly. 0A1D's proof specifies the derived base-change isomorphism
with ordinary pullback of the base-flat coefficient; 0DJQ verifies
coherence and finite Tor dimension in this case. 0BDI gives upper
semicontinuous dimensions of derived fibre cohomology for pseudo-coherent
objects; its proof uses finite-free representatives and matrix ranks.
The endomorphism-dimension characterization of reducibility must still
be justified in the next proof. Upper semicontinuity is not finiteness,
and ordinary pushforward rank is not fibre endomorphism dimension.

## Separate specialization and discriminating test

Reuse L071's all-fibre polystability, exact line lattice and Picard
qualifications, audited L094's determinant-fixed unitary slice bridge,
and audited L095's injective actual harmonic derivative at any specified
split fibre. Their hypotheses are unchanged. Do not repeat the norm
or second-order moment calculation. The new work is exact-family
assembly, not a reproof of the imported theorems. Full matching Mathlib
coverage is not checked.

The later attempt must explicitly check unordered line factors,
uniqueness of their connection orbit at fixed metric, residual gauge
choices, and the finite-dimensional coordinate derivative of the actual
family before quotienting. It must establish local isolation and
independently closedness before invoking compactness of S_2. Stable
simplicity versus split endomorphisms requires the retained polystability
and Picard hypotheses. Generic stability and quotient smoothness cannot
replace those checks. No such assembly is performed in this turn.

Continuation test: continue if slice control and the actual derivative
prove local isolation and the cohomological criterion proves closedness
under these hypotheses. Abandon this inference if an accumulating or
positive-dimensional split locus is consistent with all retained inputs,
or if the required actual-family coordinate comparison fails. Source
failure alone is not a counterexample. Neither alternative is proved here.

This changes the target from the exhausted second-order exclusion
(ATTEMPTS/061) to fibre-type control. It also does not reopen the
line-twisted IT or blocked index-curvature mechanism: finiteness is
weaker than absence of jumping and makes no index-effectivity claim.
The earlier historical stops and incomplete reasoning remain intact.

## Search and duplicate record

Queries included "Diez Rudolph normal form equivariant differential
operators anti self dual connections slice 2022 5.3 5.8", "reducible
anti self dual connections locus closed stabilizer slice K3 line bundle
isolated reducibles", "ASD connections K3 smooth family injective
harmonic derivative reducible locus isolated finite", and
"site.stacks.math.columbia.edu proper flat coherent cohomology upper
semicontinuous dimension fibre H0". Search snippets are discovery only.
No exact theorem was identified by this bounded search; no novelty is
inferred. Unrelated adiabatic K3 results and earlier inaccessible Itoh
leads are not essential and are not imported.

The proposal is superseded by this source assessment. The compatible-
line and line-twist stops are preserved. This readiness decision is for
a later bounded specialization after separate supervisor approval;
no finiteness lemma, counterexample, mathematical script or new proof
is written in this literature-only turn.
