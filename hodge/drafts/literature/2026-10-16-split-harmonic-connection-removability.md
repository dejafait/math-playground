# Actual split harmonic connection — surface removal coverage

TARGET: Test smooth extension of L113's actual harmonic Chern connection across each split point on L111's holomorphic bundle M.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted Uhlenbeck/Bando--Siu surface-removal searches and scoped comparison with L100/L108/L111--L113, the saved curvature/geodesy assessments and ATTEMPTS/063/066/067; retrieved Parker's author-hosted primary removal theorem and its curved-metric and regularity proof cases.
SOURCE_EVIDENCE: Parker, CMP 85 (1982), 563--602, section 2 pp. 574--577, (2.5)/(2.6), Definition 3.1/(3.5) p. 581, Theorem 5.3/proof p. 586, Theorems 7.7--7.8/proofs pp. 598--600 and Theorem 8.1/proof p. 600; Verbitsky alg-geom/9610010v1 section 2.2 Example 2.9(i), Theorem 2.7, Proposition 2.13/Lemma 2.14 and section 5.1; reuse L100's harmonic-moduli and L108's natural-descent coverage, and Demailly I (3.28) Hartogs extension.
COMPARISON: Parker supplies genuine four-real-dimensional removal on a smooth curved base, but requires the Yang--Mills equation and his stated compact simple group scope; L113 supplies the energy estimate, while L100/L108 supply the specific stable-open tangent/metric comparison from which the equation and an appropriate group reduction must still be checked.
GAP: Verify that the actual harmonic Chern connection is the pullback hyperkahler tangent connection, establish ASD and hence differential Yang--Mills, match Parker's group hypothesis, and identify the smooth gauge extension holomorphically and isometrically with the actual M; none is proved by this literature review.
REASON: Essential theorem coverage is now accessible without the persistently unread Bando--Siu images; approve only the bounded known-theorem specialization for the unchanged target, with no general reproof or new extension claim.
SCOPE: Exactly TARGET; hypothetical L071 (14,21) F with the full negative tensor, original smooth common metrics, L094/L095, audited L100/L108 natural stable-open comparisons and audited L111/L112/L113. Z is finite and possibly empty. No semistability, cardinality bound, kernel existence or universal realization is assumed.
LITERATURE_REASON: The startup REVIEW_REQUIRED target needs a primary surface-removal theorem outside the ready curvature assessment; reuse harmonic-moduli coverage and inspect only the missing removal and identification inputs.

## Relevance, threshold and prior failures

The main gap remains algebraicity of arbitrary primitive rational Hodge
classes, even on arbitrary fourfolds. The intermediate target is removal
for this conditional actual connection on M. It could support later work
on the normal summand and its stability, independently of the unresolved
existence of F, the number of split points, reconstruction and transport.
It would supply no new algebraic Hodge class or general Hodge resolution.

Continue only if the actual connection, including its metric and natural
holomorphic structure, satisfies an inspected removal theorem and the
result is identified with M. If the actual tangent/metric bridge fails,
record that failure and stop the application rather than silently add an
ASD assumption. If a group or holomorphic identification obstruction
survives, narrow or park the target. Empty Z is vacuous locally.

The exact duplicate/failure checks read ATTEMPTS/063/066/067, L113's
hypotheses and curvature/energy passage, L112's exact metric statement,
L100's actual chart construction and L108's natural tangent descent and
metric splitting. They do not already prove removal. ATTEMPTS/066 rejects
reflexivity alone and the codimension-at-least-three shortcut; neither
has been revived. L113's actual pointwise bound and energy at most
K epsilon^4 are the material new input. ATTEMPTS/063's singular coarse
metric bridge and ATTEMPTS/067's duality-only bound remain separate stops.
No cross-notebook input was used.

## Primary surface theorem and proof scope

Thomas H. Parker, *Gauge theories on four dimensional Riemannian
manifolds*, Communications in Mathematical Physics **85** (1982),
563--602, DOI 10.1007/BF01403505,
[author-hosted published paper](https://users.math.msu.edu/users/parker/GaugeTheories_parker.pdf#page=38).
Theorem 8.1, p. 600, removes an isolated singularity of a smooth
finite-energy solution of (2.5) or (2.6), subject respectively to
m in W^{2,p} or m^2 in W^{1,p}, p>2. Its conclusion is a gauge in
which the connection and particle field extend smoothly. Use zero
particle field and zero mass: the remaining required equation is
D_A^*F_A=0 and the energy (3.5) is the curvature-square integral.
Section 2, p. 574, assumes compact **simple** structure group; do not
silently replace that scope by arbitrary U(50). The argument is local
on a smooth curved four-manifold. The complete proofs of 7.7--7.8,
pp. 598--600, retain the metric and rescaling; 8.1 uses their energy
improvement and 5.3's elliptic gauge regularity, p. 586. This is not a
flat-base-only or higher-complex-codimension theorem. These results
are inputs to cite, not to reprove.

## Equation coverage and obligations for the actual connection

M. Verbitsky, *Deformations of trianalytic subvarieties of hyperkahler
manifolds*, [alg-geom/9610010v1, 9 October 1996](https://arxiv.org/html/alg-geom/9610010),
section 2.2 Example 2.9(i) treats the Levi--Civita tangent connection
as hyperholomorphic. Section 5.1 treats its restriction to a trianalytic
submanifold, without compactness. Theorem 2.7 gives smooth integrability
from (1,1) curvature; Proposition 2.13/Lemma 2.14 give zero contraction.
Read the statements, the restriction proof and the cited orthogonality
proof in [*Hyperholomorphic bundles*, alg-geom/9307008v1, section 2,
Lemma 2.1/Theorems 2.3--2.4](https://arxiv.org/html/alg-geom/9307008).
The surface proof identifies the three Kahler forms with self-dual
forms. The future application must distinguish the differential
Yang--Mills equation required by Parker from the terminology for the
Hermitian--Einstein contraction equation, and justify the bridge.

Reuse the ready [L100 audit assessment](2026-10-14-equality-stable-geodesy-critical-audit.md)
and its canonical actual-slice proof. It supplies smooth hyperkahler
connection-moduli charts with natural harmonic tangent and one fixed
positive L2 normalization. L108's natural stable-family descent identifies
the actual relative Ext with that tangent pullback; base-line twists and
scalar changes disappear on End_0. For this application the proof still
must explicitly compare the **whole** rank-fifty Hermitian holomorphic
bundle with the tangent pullback, not only the four-real-dimensional KS
image or its norm. Chern uniqueness must then identify the chosen
connections. No coefficient connection on the product can substitute
for the higher-image Chern connection.

The candidate way to meet Parker's compact-simple scope is the compact
Sp(25) reduction of the rank-fifty complex hyperkahler tangent pullback.
Its parallel symplectic form, actual metric compatibility, normalization
and overlap descent must be checked from that comparison. This is a
listed specialization obligation, not a newly proved group reduction.
Do not assume irreducibility of this higher-image connection or use an
inverse through the central cohomology jump. Only stable-open charts
are needed for the proposed equation check.

## Specific holomorphic extension, rather than an abstract gauge bundle

A smooth gauge extension initially gives an abstract smooth bundle.
For an ASD application the continued curvature must still have type
(1,1), and the smooth integrability theorem just cited is needed to
obtain its local holomorphic frames. The punctured gauge isomorphism
must intertwine the (0,1) operators, hence be a holomorphic bundle
isomorphism with M on the puncture.

The precise ordinary extension input is the named Hartogs extension
theorem: [Demailly, *Complex Analytic and Differential Geometry*,
21 June 2012, Chapter I, (3.28), section 3.D](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf).
Its primary indexed theorem and cutoff/compact-support proof were
retrieved: n>=2, a compact removed set K and connected complement.
The full PDF initially loaded but subsequent targeted requests timed
out; no unseen passage is claimed read. Here the intended application
is a ball in C^2 and one removed point. The subsequent proof must
apply this theorem to both transition matrices in local holomorphic
frames, retain both inverse identities, and transport the extended
metric and connection through the resulting isomorphism. Algebraic
reflexivity alone does not carry out these analytic identifications.
No assertion of that transport is proved in this review.

## Access record, balance and decision

Queries included: `Uhlenbeck 1982 removable singularities Yang Mills
fields theorem finite action four manifold pdf`; `Bando Siu stable
sheaves Einstein Hermitian metrics theorem 1 locally free bounded
curvature removable singularities pdf`; exact title/DOI searches and
`Uhlenbeck Removable site:archive.ymsc.tsinghua.edu.cn`.
Uhlenbeck's original Project Euclid iframe was blocked and Springer
exposed a subscription preview only. Celebratio supplied bibliography,
not proof. These are unread theorem leads and are not imported.
Bando--Siu's author index still exposes image pages; two image links
were located but their contents were not inspected, and a local download
failed for lack of network resolution. Park that dependent access route.
The independently available Parker primary theorem removes its essential
role in this target. No credits, keys or paid access were used.

This review changes source readiness and supplies known theorem inputs,
not a mathematical extension result or progress beyond the inspected
sources. SPECIALIZE permits the one conditional application above;
there is no need to reprove gauge removal. Full matching Mathlib
coverage is not checked. The mathematical exploration counter is
unchanged by this literature turn. No lemma, DAG, PROOF or mathematical
script is changed. Next is the identical TARGET under this assessment,
subject to the supervisor's separate approval of newly ready coverage.
