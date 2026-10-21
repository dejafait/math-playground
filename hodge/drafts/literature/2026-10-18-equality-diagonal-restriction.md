# Equality diagonal restriction — source comparison

TARGET: Assess whether restricting the hypothetical equality kernel to the diagonal K3 gives an independent exact-metric rank-two Chern/stability obstruction.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched notebook drafts/literature, ATTEMPTS and history for diagonal restriction/pullback and named tensor inputs; only the pending assessment matched. External queries “hyperholomorphic bundle pullback trianalytic submanifold diagonal Verbitsky” and “Chern classes naturality pullback vector bundle diagonal correspondence trace cohomology” led to the primary sources below; no matching fixed-tensor exclusion was identified.
SOURCE_EVIDENCE: Inspected Verbitsky math/0107182v10 Theorem 3.1, Proposition 3.7, Lemma 3.8 and Theorem 3.9; Huybrechts author-hosted Lectures on K3 Surfaces Chapter 9 Definition 4.7, Remark 4.8 and Theorem 4.9, printed pp. 181–182; Stacks Tag 02UA Lemma 42.38.9(2), including its projective-bundle proof, and Tag 02UM Chern-character expansion. Reused the exact-h surface-source assessment of 2026-10-04. Direct primary URLs: https://arxiv.org/html/math/0107182v10#S3 ; https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182 ; https://stacks.math.columbia.edu/tag/02UA ; https://stacks.math.columbia.edu/tag/02UM .
COMPARISON: These sources cover the invariant-curvature, Hermite–Einstein and Chern-naturality tools, but do not compute the diagonal pullback of this marked tensor. L052 already supplies the exact-h stable/split numerical alternatives; no new surface classification or reproof is needed.
GAP: A later mathematical step must verify the actual diagonal connection/metric specialization and evaluate the entire integral mixed Chern pullback before comparing with L052; no diagonal charge or exclusion is established here.
REASON: Essential framework coverage is now adequate for one bounded specialization independent of image singularities; the changed embedding and its full-tensor contraction still require explicit mathematics.
SCOPE: Hypothetical locally free rank-two Omega-polystable F on the identical marked S x S with integral c_1=0, ch_2=-14e_1-21e_2-tau_D, common ordered quaternionic structures and L044's exact real h; only the diagonal inclusion, no arbitrary graphs or transport.

## Source statements and qualifications

[Verbitsky, Hyperholomorphic connections on coherent sheaves and stability,
math/0107182v10, Section 3](https://arxiv.org/html/math/0107182v10#S3),
Theorem 3.9 requires a stable holomorphic bundle and SU(2)-invariant first
two Chern classes. Proposition 3.7 and Lemma 3.8 give zero Kähler
contraction for invariant curvature. Theorem 3.1 identifies integrable
unitary connections by curvature type. These are connection statements;
ordinary restriction of a stable bundle is not a substitute. Their cited
general proofs are imported. L071 supplies the stable product passage
and compatible connection under precisely the retained hypothetical data.
The next step must check equivariance for the diagonal differential and
the induced metric rather than invoke the factor embedding as identical.

[Huybrechts, Lectures on K3 Surfaces, Chapter 9,
Theorem 4.9](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
applies to a compact Kähler manifold: a holomorphic vector bundle admits
a Hermite–Einstein metric exactly when it is slope-polystable. Definition
4.7 and Remark 4.8 retain the chosen real Kähler metric and the
Bogomolov–Lübke inequality. No integral polarization is required.
Reuse the inspected K3 RR and dual-stability coverage in
[the factor assessment](2026-10-04-nonsymmetric-factor-polystability-region.md).
L052's established numerical tests are stable charge c>=4 or split charge
c=14r^2, including zero. They are necessary tests; passing c>=4 alone
is no existence theorem. The next step must justify using the same
slope tests at the induced metric, and must permit a reducible restriction.

[Stacks, Lemma 42.38.9(2), Tag 02UA](https://stacks.math.columbia.edu/tag/02UA)
expresses compatibility of Chern operations with bivariant operations and
pullback of a finite locally free bundle along a locally finite-type map.
Its proof base-changes the projective bundle and uses the characterizing
Chern relation. Here the smooth algebraic diagonal is a regular embedding;
its refined pullback and cycle-class compatibility give the usual integral
cohomological Chern naturality. No flatness of the diagonal map is needed.
[Tag 02UM](https://stacks.math.columbia.edu/tag/02UM) gives the character
polynomial, in particular the conversion between ch_2 and c_2 when c_1=0.
Use standard integral topological Chern naturality as well; no rational
NS/T decomposition may replace integrality of the full class.

The numerical tensor contraction remains an application obligation:
retain both divisor and transcendental blocks from L025/L044 and the
operator convention of L071. Do not use only the eigenvalue on the
positive three-plane or the transcendental block. Derive any diagonal
cup/trace identity from the tensor convention in the later calculation;
it has not been asserted as a new lemma in this review.

## Decision and bounded continuation

The main unresolved gap is universal primitive rational Hodge realization.
The intermediate target is one diagonal necessary-condition test for the
hypothetical equality kernel. An exclusion would stop this kernel recipe
before reconstruction or transport; a compatible charge would park this
particular test. F existence and transverse transport remain independent
unresolved assumptions. The primary formulation was rechecked in
[Deligne, The Hodge Conjecture, Section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2):
the target concerns rational cycle combinations on smooth projective
complex varieties.

No source inspected evaluates this diagonal charge, and the review has
not calculated it. One finite calculation is justified; a sweep of graph
restrictions or a new existence search is outside this approval.
The exact proposed calculation and threshold are recorded in
[the continuation assessment](2026-10-18-equality-diagonal-charge-test.md),
which is newly written and requires separate next-turn approval.

ATTEMPTS/070–073 stop different collision/curvature/vanishing inferences;
the present target uses neither their failed implications nor compact
ambient extension. L071's factor test is supporting input, not a duplicate
diagonal computation. Search failure does not establish novelty.
No lemma, mathematical script, diagonal charge, stability conclusion or
Hodge-class advance was produced. Mathlib coverage of the full diagonal
specialization is not checked; no absence claim is made.
