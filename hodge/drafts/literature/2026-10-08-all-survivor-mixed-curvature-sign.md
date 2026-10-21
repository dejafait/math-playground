# All-survivor mixed-curvature sign test — source coverage ready

TARGET: Test whether a direct mixed-curvature identity excludes every L052 survivor with the fixed tensor tau_D, allowing reducible factor restrictions.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for hyperholomorphic product mixed-curvature positivity and second-Chern sign statements; scoped comparison of L052, L062, L069, their ready assessments, history/147 and ATTEMPTS/048, plus the parked flat-index assessment. No inspected theorem gives this exact all-survivor exclusion; queries and primary reads are recorded below.
SOURCE_EVIDENCE: Li arXiv:1908.05017v1, full Section 2.2/Theorem 2.10 proof and Section 2.3 through the complete Proposition 2.13 proof, PDF pp. 5–8; Verbitsky math/0107182v10, Definition 3.2, Proposition 3.7/Lemma 3.8/Theorem 3.9, PDF pp. 11–14, with alg-geom/9307008v1 Proposition 1.2, Definition 2.1 and complete Theorem 2.3/Lemma 2.1 proof, PDF pp. 4–7; Bismut ICM 1986 proceedings (1987), p. 492, equation (0.2). Accessed 2026-10-08; prior family-form coverage is reused.
COMPARISON: Li's affine unitary metric/form/operator formulas precede the irreducible quotient; Verbitsky's curvature-invariance and zero-contraction inputs require no irreducible factor restriction. These provide tools for a direct actual-curvature test. Li's quotient/universal-connection theorems do require irreducibility and cannot certify the enlarged conclusion; L069 alone covers only charge seven.
GAP: In a separate research turn expand the actual curvature square, verify its pure/mixed contributions and signed relation to the affine unitary pairing, and test the required sign against the fixed D(sigma)=2lambda sigma without projection to a smooth moduli tangent. No all-pair identity or exclusion is established in this review.
REASON: The changed reducible-fibre hypotheses now have adequate foundational coverage for this bounded direct test; the remaining difference is explicit curvature/exterior algebra and applicability, not an essential unread theorem. Import the general inputs and prove only that specialization next turn.
SCOPE: Proposed rank-two locally free slope-polystable bundles on the same marked B x Y at the same product metric, c_1=0, ch_2=(a+4)e_1+(b+4)e_2+tau_D, all L052 survivor pairs a,b<=-9 with (a+4)(b+4)=6 modulo 12. The fixed mixed operator is self-adjoint and has D(sigma)=2lambda sigma, 1<lambda<3/2. Factor stability and a smooth classifying moduli space are not assumed.
LITERATURE_REASON: Changed hypotheses remove the stable charge-seven fibres and smooth irreducible harmonic quotient essential to the saved ready assessment; direct curvature coverage with reducible restrictions must be checked separately.
COVERED_TARGET: Test whether a direct mixed-curvature identity excludes every L052 survivor with the fixed tensor tau_D, allowing reducible factor restrictions.

## Proposed use and stopping test

The main gap remains universal primitive rational Hodge algebraicity.
The intermediate target would determine whether varying pure point
corrections can rescue this fixed mixed tensor at the fixed metric.
It is a proposed necessity test, not a claim that such an identity or
an all-pair exclusion has already been established.

Essential local inputs are L052's full survivor hypotheses
and compatible hyperholomorphic connection, L062's Chern–Weil/exterior
conventions, and L069's audited metric sign for its narrower charge-seven
case. L060's all-fibre charge-seven stability and L067's smooth
classifying chart may not be assumed across this wider set. The
Bogomolov and factor filters are already evaluated in L046–L052;
repeating them would not answer this direct mixed-form target.

The source-coverage test passes for a direct calculation, not for
importing a finished all-pair exclusion. Continue mathematically only
after the full expansion verifies the proposed sign. An uncontrolled
pure-curvature term, failure of the real unitary comparison, or a
compatible sign stops this mechanism without proving existence.
A singular quotient treated as smooth fails the test. Other mixed
tensors, representatives and transverse transport remain unresolved.

## Primary inputs and exact scope

[Yang Li, *Mukai duality on K3 surfaces from the differential geometric
perspective*, arXiv:1908.05017v1, 14 August 2019](https://arxiv.org/pdf/1908.05017v1#page=5),
Section 2.2, PDF pp. 5–6, defines the positive metric using negative
unitary trace, the three wedge-integral forms, and negative
precomposition on the affine space of projective unitary connections.
These definitions come before ASD reduction. The proof then requires
irreducibility for a free regular quotient and a smooth harmonic
tangent. Section 2.3, PDF pp. 6–8, explicitly requires irreducibility
to invert the trace-free scalar Laplacian; Lemma 2.12 includes vertical,
mixed and horizontal curvature, and Proposition 2.13 checks all three
cases. Its universal bundle also uses isotropic Mukai data. None of
these quotient or universal-connection conclusions is imported for
reducible fibres. The usable input is the affine normalization alone.
Its trace-free coefficient scope must be respected: either justify
determinant-flat reduction for the actual F or retain and check the
central unitary contribution explicitly. Raw mixed curvature is not
assumed harmonic. Li's suspect global period sign remains unused.

[Misha Verbitsky, *Hyperholomorphic connections on coherent sheaves
and stability*, arXiv:math/0107182v10](https://arxiv.org/pdf/math/0107182v10#page=11),
Definition 3.2, PDF p. 11, characterizes a Hermitian hyperholomorphic
connection by curvature of type (1,1) for every induced complex
structure, equivalently SU(2)-invariant curvature. Proposition 3.7
and Lemma 3.8, PDF p. 13, give zero Kahler contraction without a
stability hypothesis. Theorem 3.9, PDF pp. 13–14, retains stability
when constructing such a connection from invariant Chern classes;
L052 already supplies that input on the product. No new existence
claim is required or made for the factor restrictions.

The referenced invariant-form argument was inspected in
[Verbitsky, *Hyperholomorphic bundles*, alg-geom/9307008v1,
29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1#page=4),
Proposition 1.2 and Definition 2.1, PDF pp. 4–5, and the full
Theorem 2.3/Lemma 2.1 proof, PDF pp. 6–7. It uses orthogonality
of invariant two-forms to the Kahler triple, with no simplicity or
smooth-moduli hypothesis. These results are imported; their general
proofs need not be repeated. Application to factor tangent directions
and to the actual mixed block still requires explicit justification.

[Jean-Michel Bismut, *Index Theorem and the Heat Equation*,
ICM Berkeley 1986 proceedings (1987), p. 492, equation (0.2)](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1987c.pdf#page=2)
gives ch(E)=Tr exp(-R/(2pi i)) for a bundle with connection of
curvature R. It imposes no stability or moduli hypothesis. Import
Chern–Weil and retain its factorial and complex-orientation convention.
The existing family-form assessment and L062 supply the already
checked convention bridge, not a theorem about the enlarged survivor
set. No new KS injectivity or moduli-placement assertion is needed.

## Separate mathematical specialization authorized

Use only the actual compatible unitary Chern connection on the fixed
marked product. Retain both pure blocks and the mixed block in its
curvature square until their contributions are justified. Compare the
result with the affine trace pairing before any gauge quotient or
harmonic projection. Check the determinant/central block, complex
orientation, ordered multiplication, real-to-(0,1) conversion and
the two Chern–Weil mixed products. Then evaluate the resulting form
using the full self-adjoint tensor and the unchanged holomorphic-form
normalization. In particular, independence from a,b and any vanishing
of pure terms are obligations of the future proof, not conclusions
approved by this literature turn. No mathematical script is needed
unless the actual attempt identifies a meaningful verification task.

This comparison is necessary because the published affine formulas
do not state the notebook's fixed-tensor exclusion. It is a
specialization of known tools, classified REPRODUCTION; it is not
a reproof of a general moduli theorem or an originality claim.

## Search, duplicate and failure record

Queries on 2026-10-08:

- `Li 1908.05017 hyperkahler curvature mixed triholomorphic connection`
- `hyperholomorphic bundle product hyperkahler mixed curvature positivity second Chern character reducible`
- `"hyperholomorphic" "mixed" "curvature" product positivity`
- `"hyperholomorphic" "Chern" "positive" product second`

Primary search leads included Verbitsky's invariant-connection papers,
positive-form work and transgression work. The inspected inputs are
exactly those cited above. Positive-form/direct-image and transgression
papers are uninspected leads here and not essential premises. Search
snippets establish no theorem or novelty. A command-line PDF download
failed DNS resolution; the needed primary passages were available
through the web reader, so there is no essential source blocker.

Scoped duplicate checks read L052's hypotheses/connection passage,
L062's entire curvature/ordered-form passage and L069's complete proof,
and reused their saved source assessments. ATTEMPTS/048 and history/147
stop only the audited charge-seven representative. The older
Bogomolov assessment already covers pure-point correction tests.
The flat-index assessment of 2026-10-06 remains SOURCE_BLOCKED for
Itoh's complete index-connection formula; the direct curvature of F
does not use it. Its warning against discarding horizontal curvature
remains relevant. No stopped index route is reopened.

No new theorem, lemma, mathematical script or all-pair exclusion is
produced here. This literature step is EXPLORATION / REPRODUCTION:
the changed scope has been compared, and the saved exact target is
ready for one separate mathematical attempt. Mathlib coverage of the
full specialization is not checked; no absence is asserted.
