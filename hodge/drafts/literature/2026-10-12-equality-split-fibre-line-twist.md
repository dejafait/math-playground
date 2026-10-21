# Equality split fibre — line-twist source comparison

TARGET: Test whether the family F tensor p_1^*L^{-1}, with c_1(L)=k, rules out a split charge-fourteen fibre of a hypothetical L071 kernel with (m,n)=(14,21).
CHECKED: 2026-10-12
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched hyperkahler Fourier-transform IT/jumping cohomology, hyperholomorphic reducible-fibre families, and K3 polystable two-line deformation terminology; inspected BBHR and Stacks statements/proof cases; scoped ATTEMPTS/059/060 and split/uniform assessments contain no line-twisted jump exclusion.
SOURCE_EVIDENCE: BBHR (1998) Definition 2 and Section 3.3 Lemmas 1–2/Theorem 3, printed pp. 244–246, inspected anew; Stacks 36.30.1 (0A1H), 36.31.1 (0BDI), 36.31.3 (0BDK), statements and relevant proof cases inspected; Huybrechts K3 draft Chapter 1 (2.5) and Serre duality, pp. 11–12, inspected; Arbarello–Sacca (2018) Theorems 1.1/1.2, pp. 652–653, inspected as a scope mismatch.
COMPARISON: IT is an explicit sufficient hypothesis, not a prohibition on its failure; perfectness and upper semicontinuity supply no no-jump conclusion. The changed coefficient cannot inherit L093's every-fibre concentration or ordinary scalar self-duality.
GAP: No inspected result distinguishes the proposed split fibre from permissible endpoint jumping; no actual compatible global complex, F, or exclusion has been constructed. A global effective-cycle constraint would require different coverage.
REASON: Bounded source comparison is complete for testing the proposed IT/base-change exclusion; it found no usable obstruction. Park this method and separately review a global index/jumping-cycle mechanism rather than repeat the untwisted argument.
SCOPE: Identical marked projective K3 factors at L071's exact h/Omega; locally free rank-two Omega-polystable F, integral c_1=0, full ch_2=-14e_1-21e_2-tau_D, actual split p_2 fibre, and line L with c_1=k=(-4,-2,1,2). EXPLORE is not an existence or novelty claim.

## Target and relevance

The main gap is universal primitive rational Hodge realization. The
intermediate target concerns split-fibre exclusion for one hypothetical
equality kernel. It could constrain fibre types for later common-kernel
construction, leaving all-stable equality kernels, prescribed mixed
action, transport and the universal gap independently unresolved.
L071 supplies the conditional connection and exact-h line classification;
audited L093 supplies only the untwisted strict-Euler stop. No
cross-notebook input is used. ATTEMPTS/059/060 remain intact.

## Inspected primary coverage

[Bartocci–Bruzzo–Hernandez Ruiperez, *A hyperkahler Fourier transform*,
Differential Geometry and its Applications 8 (1998), 239–249](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6):
Definition 2 requires endpoint vanishing for every y. Section 3.3
assumes IT before constructing the bundle; Lemmas 1–2 transfer it
through the twistor diagram. Theorem 3 requires a compact hyperkahler
source, compatible spheres, hermitian quaternionic kernel and IT source
instanton. Its independence statement varies induced complex structure
z, not parameter y. Nothing in these proof cases rules out base jumps.
The special reflexive-K3 inverse in Section 4 has additional lattice
and universal-moduli hypotheses, unavailable here.

[Stacks 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
requires finite presentation, a perfect object, and a bounded finitely
presented base-flat coefficient complex with proper support. It yields
perfect pushforward and arbitrary derived base change. Our projective
projection and locally free twisted coefficient meet these hypotheses
with perfect object O. Its Noetherian proof reduction applies here;
no non-Noetherian approximation is needed.

[Stacks 36.31.1, 0BDI](https://stacks.math.columbia.edu/tag/0BDI)
gives upper semicontinuous derived fibre dimensions for pseudo-coherent
complexes. Its proof uses local finite-free representatives and ranks
of differentials, with constructibility expressed by minors. This
allows rank drops; it imposes no global class or effectivity test.
[Stacks 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK)
characterizes the open locus of fixed-rank, one-degree concentration;
its proof requires all other fibre dimensions to vanish there. It
cannot promote generic IT to every-fibre IT.

[Huybrechts, *Lectures on K3 Surfaces*, author-hosted draft, Chapter 1,
pp. 11–12](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
records line RR and Serre duality. Necessary applicability check only:
the stipulated split fibre is L plus L^{-1} by L071, so after the
specified twist it contains O. On a K3, O has nonzero degree-zero and
degree-two cohomology. Thus odd IT cannot hold at that fibre; this is
failure of a theorem hypothesis, not a contradiction to F. No new
index calculation or lemma is made. L090/L091/L092's ordinary scalar
form cannot be assumed after changing the determinant coefficient.

[Arbarello–Sacca, *Singularities of moduli spaces of sheaves on K3
surfaces and Nakajima quiver varieties*, Advances in Mathematics 329
(2018), 649–703, Theorems 1.1/1.2](https://www.math.columbia.edu/~giulia/Quiver.pdf#page=4)
concern pure dimension-one sheaves; Theorem 1.1 also assumes primitive
Mukai vector. These theorems are not a rank-two real-h family
no-jump result. No specialization or reproof is authorized from them.

## Search boundary and decision test

Queries included “hyperkahler Fourier transform index theorem jumping
cohomology quaternionic instanton Bartocci Bruzzo”, “hyperholomorphic
bundles K3 restriction reducible fibres family cohomology jumping
locus”, “Verbitsky hyperholomorphic bundle cohomology jumping loci
trianalytic family”, and “K3 polystable sheaves reducible locus local
quiver two line bundles deformation”. Verbitsky's 1993/1997 papers
were returned as leads; their full deformation statements were not
inspected for this changed family, so no jump theorem is imported
from them. No failed search certifies novelty or exhaustive absence.

The discriminating threshold was a theorem excluding these endpoint
jumps under the actual product-kernel hypotheses. The inspected sources
supply no such threshold. This stops the IT-preservation exclusion
method, not all line-twisted research and not the equality kernel.
We have not proved that its global character is compatible with a
jumping complex. The different proposed global index/effective-cycle
question remains REVIEW_REQUIRED in its own assessment. Full matching
Mathlib coverage: not checked. No general theorem needs reproof.
