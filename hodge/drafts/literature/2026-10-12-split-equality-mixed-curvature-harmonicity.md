# Split equality fibre — actual mixed-curvature source coverage

TARGET: Assess whether the hypothetical (14,21) kernel's mixed curvature is fibrewise harmonic at its split fibre and has strictly positive L2 norm in every nonzero base direction.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact mixed-curvature/harmonicity and Hermite--Einstein family searches identified Biswas--Schumacher's harmonic representative theorem and Geiger--Schumacher's family formula; scoped comparison of L071, L070, audited L094, ATTEMPTS/061 and the existing curvature/slice assessments found no duplicate covering this exact raw reducible changed-sign target. Queries and inspected passages appear below.
SOURCE_EVIDENCE: Biswas--Schumacher math/0605589v1, Section 3 Lemmas 3.2/3.3, stability setup and Proposition 3.4 with complete proof, printed pp. 7--8; Buchdahl--Schumacher (2022), Section 1, printed p. 81 coefficient Kahler/Bianchi identities; Li 1908.05017v1, Section 2.2 metric/form/operator definitions and Section 2.3 through complete Proposition 2.13 proof, printed pp. 5--8; Verbitsky math/0107182v10 Definition 3.2/Proposition 3.7/Lemma 3.8/Theorem 3.9, printed pp. 11--14, and alg-geom/9307008v1 Section 4 operator proofs/Corollary 4.3, printed pp. 12--16; Bismut (1987), p. 492 equation (0.2); Geiger--Schumacher 1501.07070v1, Theorem 1 hypotheses and equation (1), printed pp. 2--3.
COMPARISON: Published family harmonicity assumes stable fibres in Biswas--Schumacher; Li's universal connection and Geiger--Schumacher's main curvature theorem retain irreducibility or simplicity. Their conclusions cannot be imported at the split fibre. Coefficient identities and actual invariant curvature have no such restriction; L070's audited raw pairing is usable only after checking the negative tensor, while L094 supplies the actual derivative comparison after projection.
GAP: The separate attempt must justify raw ASD/Dolbeault harmonicity from the actual fibrewise zero-contraction connection using coefficient Bianchi/Kahler identities, then specialize the complete raw Chern--Weil pairing to -tau_D and test strict positivity. Neither assertion is established in this review.
REASON: Essential coefficient and signed-pairing coverage is accessible; the remaining difference is a bounded reducible-family specialization and sign/application check, rather than an unread indispensable theorem. Reuse the published identities without reproving general moduli or existence results.
SCOPE: Exactly the hypothetical locally free rank-two Omega-polystable F with integral c_1=0, ch_2=-14e_1-21e_2-tau_D, identical marked metrics, and S_1-fibre L plus L^{-1} with c_1(L)=k, k^2=-14 and h.k=0; harmonic means the actual real mixed one-form lies in ker d_A^* intersect ker d_A^+, with the audited L094 Dolbeault comparison. No smooth quotient, nonzero derivative or generic stability is assumed.
LITERATURE_REASON: The newly proposed target adds raw harmonicity and strict norm detection to L094's projected derivative, with reducible fibres and the full negative mixed tensor outside the earlier positive-tensor curvature assessment.
COVERED_TARGET: Assess whether the hypothetical (14,21) kernel's mixed curvature is fibrewise harmonic at its split fibre and has strictly positive L2 norm in every nonzero base direction.

The main gap is universal primitive rational Hodge realization. The
nearer bottleneck is equality/positive-Euler kernel existence. This
proposed intermediate target asks about the actual differential of a
hypothetical kernel, not integration of an arbitrary compatible tangent.
Its potential use is to remove or retain the zero-derivative alternative
before a later local-geometric or global test. Even a positive answer
would not contradict L094's compatible W or construct a kernel.

Essential local inputs are L071's actual hyperholomorphic connection,
full negative tensor and exact real metric, audited L093's equality
boundary, and audited L094's real harmonic identification and family
bridge. L070 is a proposed comparison for the raw pairing only; its
positive-tensor exclusion must not be imported for the negative tensor.
No cross-notebook input is proposed.

Retain the hypothetical locally free rank-two Omega-polystable F with
integral c_1=0 and ch_2=-14e_1-21e_2-tau_D, identical marked K3
metrics, and split fibre L plus L^{-1}, c_1(L)=k, k^2=-14, h.k=0.
No nonzero derivative, immersion, generic stability, smooth quotient,
exact quadratic model, analytic germ or actual F is established.

The source-review test passes for one separate bounded attempt, not
for importing the target as a theorem. Continue only if the actual
mixed form satisfies both the ASD deformation equation and the
Coulomb equation without assuming irreducibility, and the signed raw
pairing forces a strictly positive norm for each nonzero parameter
direction. An uncontrolled covariant derivative term, an appeal to
an unavailable scalar-Laplacian inverse, or strict positivity of an
unprojected norm without established raw harmonicity stops the claimed
nonzero harmonic derivative conclusion. Nonnegative raw norm alone is below the
required strict-positive threshold. No value or sign of the
changed-tensor scale is concluded here.

Harmonicity here has L094's ASD deformation meaning, not the stronger
equation d_A r_u=0 for the full covariant exterior derivative. The
next proof must retain that distinction and the real skew-adjoint
coefficient structure. If both requested checks succeed, only the
zero-derivative alternative is removed; no contradiction follows
merely from an injective quaternionic tangent.

Preserve ATTEMPTS/061: all three quadratic equations already admit a
nonzero quaternionic line. Repeating that cancellation cannot answer
the actual-curvature question. Higher-order realization, global mixed
action, transport and the universal gap remain independent.

## Primary statements, hypotheses and essential proof cases

[Indranil Biswas and Georg Schumacher, *Geometry of moduli spaces of
Higgs bundles*, math/0605589v1, 22 May 2006](https://arxiv.org/pdf/math/0605589v1#page=7),
Section 3, printed pp. 7--8 (PDF pages 7--8), was read from Lemma 3.2
through the complete Proposition 3.4 proof, including the intervening
stability assumption. Lemma 3.3 identifies contraction of the actual
Chern curvature as the Kodaira--Spencer representative for a smooth
Hermitian family. Proposition 3.4 gives harmonicity for the stated
family of stable Higgs bundles. Its proof expresses the adjoint as a
covariant parameter derivative of the fibre Hermitian--Yang--Mills
equation. Setting the Higgs field to zero identifies the relevant
ordinary-bundle case. The split fibre fails the theorem's stability
assumption, so this is a comparison and proof-method input, not a
direct import of Proposition 3.4's conclusion. The next attempt must
justify its coefficient identity and differentiated equation for
the already supplied smooth metric and reducible connection; it
must not import uniqueness of the family metric modulo base scalars.

[Nicholas Buchdahl and Georg Schumacher, *Polystable bundles and
representations of their automorphisms*, Complex Manifolds **9**
(2022), 78--113, DOI 10.1515/coma-2021-0131](https://d-nb.info/1262812674/34#page=4),
Section 1, printed p. 81, supplies the coefficient Kähler adjoint
identities for a Hermitian connection and the Bianchi/Kähler
characterization of Yang--Mills curvature. This passage was inspected
directly, with its integrable-connection and closed-Kähler-form
hypotheses. It imposes no simplicity condition. Import these general
identities; showing that the actual mixed contraction satisfies the
required fibre equations remains an application, not a theorem
already proved here. The existing L094 audit assessment continues
to cover the real ASD/Dolbeault and unitary slice tools.

[Yang Li, *Mukai duality on K3 surfaces from the differential
geometric perspective*, arXiv:1908.05017v1, 14 August 2019](https://arxiv.org/pdf/1908.05017v1#page=5),
Section 2.2, printed pp. 5--6, defines the negative-unitary-trace
metric with factor 1/(4pi^2), the wedge forms and negative
precomposition on affine projective connections before quotienting.
These match the normalization retained in L070. Section 2.3,
printed pp. 6--8, including Lemma 2.12 and all three cases of
Proposition 2.13's proof, was inspected. The scalar-Laplacian
inverse explicitly depends on irreducibility; the mixed formula
is for that universal connection and Coulomb tangents. Its use at
the present reducible fibre is disallowed. The usable affine
identities do not prove raw harmonicity. The determinant/central
contribution must be justified as in audited L094 or retained as
in audited L070. Li's global period sign is not an input.

[Misha Verbitsky, *Hyperholomorphic connections on coherent sheaves
and stability*, math/0107182v10](https://arxiv.org/pdf/math/0107182v10#page=11),
Definition 3.2, Proposition 3.7, Lemma 3.8 and Theorem 3.9,
printed pp. 11--14, supply invariant curvature, zero contraction,
and the stable invariant-Chern existence criterion. The statements
and the Proposition/Lemma proof references were inspected; ready
coverage from the 2026-10-08 assessment is reused. L071 already
checks product stability and sign-independent invariance before
obtaining the actual connection. The factor curvature restrictions
need not be irreducible for zero contraction.

[Verbitsky, *Hyperholomorphic bundles*, alg-geom/9307008v1,
29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1#page=13),
Section 4 setup, Proposition 4.2's coefficient identity proof,
Proposition 4.3, Theorem 4.1 and Corollary 4.3 with proofs,
printed pp. 12--16, were inspected for the coefficient bundle's
hyperholomorphic connection and parallel real structure. These
results preserve harmonic subspaces under the real quaternionic
action without simplicity. They support L094's projection bridge,
but do not by themselves show that raw product mixed curvature is
harmonic. The next application uses actual End_0 coefficients at
the split connection rather than a smooth coarse tangent space.

[Jean-Michel Bismut, *Index Theorem and the Heat Equation*,
ICM Berkeley 1986 proceedings (1987), p. 492, (0.2)](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1987c.pdf#page=2)
was inspected for the curvature exponential representative of the
Chern character. It requires no stability or moduli hypothesis.
Retain the second-character factorial and (2pi i)^2 sign. Reuse
L070's audited full pure/mixed expansion, unitary central pairing,
transpose convention and closed pure-type fibre-integral argument
as local tools only. Its positive-tensor exclusion is outside the
current hypotheses; evaluating the full negative tensor and
comparing the resulting scale with the required positive norm
are obligations of the later mathematical step.

## Stronger-source comparison and limits

[Thomas Geiger and Georg Schumacher, *Curvature of higher direct
image sheaves*, arXiv:1501.07070v1, 28 January 2015](https://arxiv.org/pdf/1501.07070v1#page=2),
Theorem 1 hypotheses and introduction equation (1), printed
pp. 2--3, were inspected. The introduction records the same
mixed-curvature harmonic representative formula, citing Ov92 and
ST92; its main curvature theorem assumes simple fibres. This is
corroborating coverage and an identified reference lead, not a
substitute for checking the split extension. The cited older
papers were not read in this step and are not imported premises.
No direct-image curvature formula is needed for the present raw
coefficient test, so the parked Itoh source blocker does not block it.

The strongest inspected matching statement is the published
stable-family harmonic representative result. No inspected
statement gives this exact reducible (14,21) changed-sign norm
conclusion. That comparison does not establish novelty: the
proposed specialization is classified REPRODUCTION, with only
the application differences described above authorized next.
No general source theorem needs to be reproved.

## Search, duplicates and stopping evidence

Queries on 2026-10-12 included:

- `"hyperholomorphic" "mixed curvature" harmonic`
- `"Mukai duality on K3 surfaces from the differential geometric perspective" "harmonic"`
- `"hyperholomorphic" "Bianchi" connections harmonic`
- `"Hermite-Einstein" "curvature" "harmonic representatives" "Kodaira-Spencer"`
- `"Bianchi" "mixed" "harmonic" curvature Kähler bundles`
- `"Schumacher" "Kodaira-Spencer" "harmonic" "polystable" curvature`
- `Biswas Schumacher "Geometry of moduli spaces of Higgs bundles" arxiv`

Search results identified the primary texts above. Search snippets,
ResearchGate previews and unrelated hyperholomorphic-function
results are not evidence for the target. The older Schumacher--Toma
papers and the principal-bundle Petersson--Weil paper remain unread
leads, not indispensable inputs to the bounded coefficient test.

Local duplicate/failure comparison inspected L071's hypotheses,
product stability/invariance and restriction passage; L070's complete
raw norm, square-expansion, pure-term removal, real/complex,
actual-form and critical-audit passages; and L094's hypotheses,
actual-family bridge and its audited gauge/real-coefficient details.
It reused the ready 2026-10-08 raw-curvature assessment and
2026-10-12 tangent-audit assessment. L070 deliberately avoided
raw harmonicity; L094 deliberately left the unprojected form and
nonzero derivative unresolved. No duplicate resolves both questions.
ATTEMPTS/061 and history/240 preserve the compatible-line stop.
The scoped flat-index assessment still lacks Itoh coverage; it
concerns index curvature rather than the actual curvature of F.
Neither that route nor the IT/index-effectivity stops are reopened.

This is one LITERATURE / REPRODUCTION / EXPLORATION step. Coverage
now permits the saved exact target's separate proof attempt, but
no new mathematical statement, lemma or script has been produced.
PROOF.md and DAG.md do not change because the argument does not.
Full matching Mathlib coverage for the proposed target is not checked;
no absence is asserted. The actual nonzero harmonic derivative,
analytic realization, common kernel and universal Hodge realization
remain unproved.
