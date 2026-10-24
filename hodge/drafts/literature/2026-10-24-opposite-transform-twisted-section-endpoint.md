# Opposite transform and the twisted endpoint — source comparison

TARGET: Test whether the opposite charge-21 transform bounds h^0(B,M) enough to exclude L154's z=147 endpoint.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 502 searched projection-formula/Leray comparisons for integral transforms and hyperkahler transform section multiplicities; found and read Pareschi–Popa Lemma 2.1 and its full proof in the author-hosted paper. Scoped overlap checks compared L093/L147/L154, ATTEMPTS/087 and the October 12 line-twist failure; no exact endpoint exclusion was identified in the inspected sources.
SOURCE_EVIDENCE: Freshly inspected Pareschi–Popa, GV-sheaves, Fourier-Mukai transform, and generic vanishing, author-hosted 28-page version, Section 2 Lemma 2.1 and proof p. 5; live Stacks 20.54.2–3 and proofs, 20.13.1/4 and proofs, and 48.15.7 and proof. Reused inspected BBHR Theorem 3 pp. 244–246, qualified coherent duality, Fulton GRR and Huybrechts/Perego stable-Hom/HE coverage through the exact assessments named below.
COMPARISON: A published arbitrary-kernel two-projection hypercohomology comparison supplies the missing general bridge without equivalence or whole-base twisted IT. Known polystable stable-Hom and relative-duality tools cover an independent opposite line-multiplicity test. Its application to the ordinary twisted middle sheaf and its numerical verdict remain unwritten mathematical work.
GAP: No essential source blocker remains for one scoped attempt: check the degree-one edge maps with the nonzero top sheaf retained, recover the opposite full character by signed GRR, and test its paired line multiplicities against the endpoint's sixteen sections. No specialized equality, multiplicity bound or exclusion is proved here.
REASON: Approve a separate REPRODUCTION specialization of the unchanged target; cite the general comparison and reuse ready transform/duality coverage, deriving only the data-specific cohomology and multiplicity consequences next turn.
LITERATURE_REASON: The startup REVIEW_REQUIRED target introduces a same-kernel twisted two-projection comparison outside the completed single-image index audit; the missing general comparison is now sourced while preservation and stability coverage are reused.
SCOPE: Same hypothetical equality F, identical marked factors/common g,h, full negative tensor, preferred dual HE twist and finite possibly empty Z; only the z=147 endpoint and its forced section count are proposed for testing.

The main gap remains universal primitive rational Hodge realization.
The intermediate target would test compatibility of the equality
decomposition with both actual projections of the same kernel. A
strict section bound below sixteen would remove this endpoint, which
could later strengthen upper split-count control. It would still not
exclude every smaller count, prove F existence or produce a cycle.
If the full opposite-image constraints admit the required multiplicity,
record that compatibility and stop this endpoint test.

Essential local inputs are L052 for the exact integral zero-slope
lattice; L071 for the common kernel/metric data; audited L093 for the
opposite actual image, concentration and preservation; L147 for the
twisted ordinary image and point sheaves; audited L153 for its
polystability; and audited L154 for the endpoint classification.
Use different names for L093's untwisted G and L147's twisted G when
making the comparison. The opposite transform here means
R^1p_{1*}F, with charge-21 fibres, not the relative-Hom complex used
in L135/L136 or a putative inverse equivalence.

The proposed new information is that both images come from one F,
and the twist is pulled back from the base of the opposite projection.
It is not an additional self/pairwise index on M. ATTEMPTS/087 remains
correct: its selected constraints contain no independent section
count. No endpoint exclusion or new multiplicity inequality is derived
in this proposal. No rank-24 self-duality or lifted kernel projector is
assumed. In particular this does not reopen a natural-projector lifting
mechanism or infer an inverse Fourier transform.

Before approving research, reuse adequate inspected source coverage,
check duplicate two-projection/section tests and their actual charges,
and inspect any essential missing projection-formula or Leray theorem
hypotheses. Retain the higher point sheaf of the twisted projection;
do not infer whole-base IT for that twist. Match the actual cohomology
maps before using a section count, and distinguish a formal opposite
decomposition from a realized kernel. The full character and any
duality used on the opposite image require separate justification.

F, nonempty Z, independent lower control and universal Hodge realization
remain unresolved. Full matching Mathlib coverage is not checked.
At proposal time this target was uncovered. The separate source review
below approves its scope; it does not execute its mathematical test.

## Completed comparison, step 502

**Exact comparison source.** Read Giuseppe Pareschi and Mihnea Popa,
*GV-sheaves, Fourier-Mukai transform, and generic vanishing*,
[author-hosted 28-page version, Section 2, Lemma 2.1 and complete proof,
printed p. 5](https://people.math.harvard.edu/~mpopa/papers/GV.pdf#page=5).
The publication is American Journal of Mathematics **133** (2011),
235–271, DOI 10.1353/ajm.2011.0000; the page locator here refers to
the inspected author version. For projective varieties X,Y over a
field, a perfect kernel P and bounded coherent objects A,C, it states
H^i(X,A tensor R Psi_P C) is isomorphic to
H^i(Y,R Phi_P A tensor C). Its four-step proof uses projection formula
and derived Leray in both directions. It requires neither equivalence
nor a universal moduli kernel. Our smooth projective factors, vector
bundle kernel F, line input L^{-1} and structure-sheaf input meet that
scope. No generic-vanishing theorem or Albanese hypothesis is imported.
The paper's identity is about hypercohomology; identifying the particular
ordinary cohomology groups remains a separate application obligation.

**Edge-map source and hypotheses.** Freshly read live
[Stacks Section 20.54, Lemmas 20.54.2–3 and their proofs](https://stacks.math.columbia.edu/tag/01E6).
For a morphism of ringed spaces, tensor with a finite locally free
base sheaf commutes with every higher direct image and derived
pushforward; the derived version permits a perfect base object.
The proofs use injective resolutions and local finite-free reduction.
The opposite projection has L^{-1} on its base, exactly the finite
locally free case. Read also
[20.13.1/4 and proofs](https://stacks.math.columbia.edu/tag/01EY):
derived global sections compose with pushforward, and a bounded-below
coefficient complex has the spectral sequence
E_2^{p,q}=H^p(Y,R^q f_*C) converging to H^{p+q}(X,C).
Our vector bundle in degree zero is bounded below. Research must
inspect all possible incoming and outgoing differentials in total
degree one using L147, rather than delete W or assume degeneration
in all degrees. No new edge-map isomorphism is derived in this review.

**Opposite transform coverage is already ready.** Reuse
[step 231's actual primary reads](2026-10-11-split-charge-cup-euler-extension.md)
and [step 233's critical-audit coverage](2026-10-12-split-charge-euler-cup-critical-audit.md).
BBHR, *A hyperkahler Fourier transform*, Differential Geometry and its
Applications **8** (1998), 239–249, Definition 2, Section 3.3,
Lemmas 1–2 and Theorem 3, pp. 244–246, requires compact hyperkahler
source, compatible spheres, the actual quaternionic-instanton kernel
and every-parameter IT. L093 already proves these for the opposite
untwisted image under the present equality input. Its positive bundle
has rank n-4 and has a perfect symmetric coefficient Serre form;
these are existing L093 conclusions, not new theorem applications here.
Do not transfer that form to the twisted rank-24 M. The October 12
line-twist assessment correctly stops whole-base odd IT on the twisted
side, and nothing in this new general comparison requires that IT.

Reuse the qualified proper coherent duality and graded-sign coverage
in the same audit. Fresh inspection of
[Stacks 48.15.7 and proof](https://stacks.math.columbia.edu/tag/0BRT)
confirms the relative dualizing complex omega_p[2] for a smooth proper
relative surface over a Noetherian base. This is satisfied by the
opposite K3 projection. L093's existing determinant-wedge/odd-cup sign
and all-fibre concentration arguments supply its symmetric form.
The twist is not a scalar-self-dual coefficient. No additional duality
claim for it is approved.

**Character and multiplicities: covered obligations, unevaluated.** Reuse
[the global-character GRR coverage](2026-10-22-twisted-middle-global-character.md):
Fulton, *Intersection Theory*, second edition, Theorem 15.2,
pp. 286–287 and Example 15.2.8, pp. 291–292. Here the opposite
untwisted higher image is a bundle by L093, so its full character
may be calculated with its own relative Todd factor and negative
alternating sign. L071 and L147 retain the full rank-two character,
including the mixed square and fourth character. The opposite full
character is an explicit next-turn calculation, not an imported
forward character or a result of this source review.

Reuse [the stable-summand assessment](2026-10-23-twisted-stable-summand-index-bound.md)
for Huybrechts, *Lectures on K3 Surfaces*, Chapter 9 Section 3.1,
pp. 175–176 and Theorem 4.9, p. 182, and Perego (2021), Propositions
3.9–3.12/3.15 with inspected proofs, pp. 36–38. These cover real-h
stable decomposition, dual stability, scalar endomorphisms of stable
types and vanishing between distinct equal-slope types. No new
primary retrieval of those sources is claimed. The research task is
to apply these general results to maps from the actual zero-slope
line L into the opposite image, retaining all repeated factors and
the image's duality. Check L and L^{-1} are distinct using their
integral first classes before making any rank or character estimate.
Any pairing of their multiplicities must be justified on the full
isotypic decomposition, not on individually selected sections.
The Schur-block comparison in
[the larger-charge assessment](2026-10-10-larger-charge-orthogonal-image-test.md)
is supporting coverage, not a K3 existence theorem. Only this finite
stable-Hom specialization is needed; no general theorem needs reproof.

**Discovery and duplication boundary.** Queries actually used were
`site.stacks.math.columbia.edu derived projection formula perfect complex Leray spectral sequence`,
`"hyperkahler Fourier transform" Bartocci Bruzzo Hernandez Ruiperez Theorem 3`,
`"hyperkahler" "Fourier" "sections" "multiplicity" K3`, and
`"Fourier Mukai" "projection formula" "Leray" cohomology line bundle`.
The last query led to Pareschi–Popa's primary proof above. A bounded
bibliographic query checked its title and publication. Unrelated
fourfold Chow transforms and generic-vanishing applications are search
leads only, not mathematical inputs. No search establishes novelty.
Local comparisons include L093's actual concentration, pairing and
audit, L147's whole-base character, L154's endpoint, ATTEMPTS/087 and
the October 12 line-twist failure. The latter two do not test this
same-kernel line-multiplicity comparison. Old natural-projector and
inverse-transform routes remain stopped; neither is needed here.

**Ready bounded attempt.** Preserve the exact TARGET. Establish the
actual degree-one comparison first, retaining W, then test the full
opposite character and duality against the endpoint section count.
Continue if these sourced bridges yield an independent bound below
sixteen; if the complete selected opposite constraints admit sixteen,
record compatibility and stop this endpoint filter. A failed bridge
must be recorded, not replaced by an equivalence assumption. This
review establishes no new comparison for these objects, numerical
bound, endpoint exclusion or existence claim. F, nonempty Z,
independent lower control, all smaller split counts, transport and
universal primitive Hodge realization remain unresolved. Full matching
and supporting Mathlib coverage: not checked. No lemmas, mathematical
scripts, DAG rows or PROOF argument are changed.
