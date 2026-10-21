# Actual split family — ordinary coarse-image comparison

TARGET: Identify the reduced analytic image germ of the actual equality-family map at a selected split parameter with the reduced image of its full-stabilizer harmonic-slice quotient map.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L097's fixed-H placement and audit, L098's finite-map statement, L103's ordinary-quotient qualification, L132's actual-family bridge, ATTEMPTS/063 and the earlier Arbarello–Saccà assessment. Focused searches located Greb–Toma's analytic semiversality theorem for an algebraic Quot slice; exact queries and rejected or unread leads are recorded below.
SOURCE_EVIDENCE: Read Greb–Toma (2020), Theorem 2.9 and proof p. 240, Section 2.5.1 pp. 242–243, Proposition 2.15 and proof p. 244, Corollary 2.16, Proposition 2.17 and its full proof, Remark 2.18 and Lemmas 2.19–2.20 pp. 245–246; Luna (1973), III.1 slice theorem and both smooth/general proof cases p. 97, closed-subscheme base-change lemma pp. 95–96 and Remark 3 p. 98; Buchdahl–Schumacher 2008.04625v3, Section 2.2 Remark 3/Theorem 3 and full general-case proof pp. 6–8, Theorem 6 p. 11, Section 5.2 Lemma 2 and quotient descent pp. 13–15, Theorem 9 proof pp. 16–17; compared 2108.03255 Section 6 Theorem 1 pp. 15–18 and Arbarello–Saccà (2018) Section 4 pp. 667–672.
COMPARISON: Known results supply an actual analytic semiversal family on an algebraic Quot slice, a strongly etale comparison of its quotient with the algebraic moduli germ, and ordinary analytic invariant-sheaf descent without weak normalization. They cover tools for the saved target; they do not themselves check the comparison with the particular harmonic family or identify its one-source image ring.
GAP: In a separate mathematical attempt, construct the compatible comparison using actual family base changes, justify descent and inverse identities on ordinary reduced germs, and retain the map from the selected source germ before comparing image kernels. No essential source-access gap remains for this bounded specialization; its conclusion remains unproved here.
REASON: Approve the unchanged saved target for one RESEARCH / REPRODUCTION attempt applying the inspected sources. Do not reprove the general slice, semiversality or analytic invariant-sheaf theorems, and do not replace actual-family compatibility by orbit equality alone.
SCOPE: Hypothetical L071 equality kernel with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D, identical marked K3 factors, L097's fixed projective H-Gieseker moduli space, L098's finite map, a selected split fibre E=L direct sum L^{-1}, and L132's actual harmonic family isomorphism. Compare one selected source germ, not the union of branches over the split coarse point.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED: earlier ready coverage did not identify an algebraic coarse germ at a reducible fibre or its ordinary analytic structure. This turn supplies that missing theorem-level comparison; it is not additional browsing on a previously ready target.

## Relevance, prior work and decision threshold

The main gap remains algebraic realization of arbitrary primitive rational
Hodge classes. The intermediate purpose is to interpret actual-family
invariant constraints, including L132, in L097's specified coarse target.
Kernel existence remains an independent gap. Even a successful comparison
would not prove all-orders parity, degree two, normality of the source image,
separation, a nonempty split locus, reconstruction or transverse transport.

L103 deliberately leaves this bridge open. Its chosen first plane and
local-degree conclusion are not assumptions about every actual equality
family; only its full-stabilizer representation and ordinary-quotient tools
are relevant here. L132 supplies actual total-family comparison, not a
coarse-space comparison. ATTEMPTS/061–063 remain intact: compatible first
tangents, a failed prescribed second jet and missing singular metric/degree
hypotheses respectively. The present target requires none of those missing
metric or higher-jet conclusions. The earlier registration in this file
had no external source comparison and was REVIEW_REQUIRED; this source
review supersedes that decision without asserting a mathematical result.

Continue with the exact saved target only if the source-backed comparison
can retain the actual family and ordinary reduced structure. An argument
that stops at a weak normalization, an abstract quadratic chart, a formal
ring without analytic comparison, or equality of closed-point classes
fails this test. Record such a failure rather than assert the bridge.

## Primary source package and its precise limits

**Algebraic slice with an actual analytic semiversal family.** Daniel Greb
and Matei Toma, *Moduli spaces of sheaves that are semistable with respect
to a Kähler polarisation*, J. Éc. polytech. Math. **7** (2020), 233–261,
DOI 10.5802/jep.116,
[Theorem 2.9, Section 2.5 and Proposition 2.17, pp. 240–246](https://jep.centre-mersenne.org/article/JEP_2020__7__233_0.pdf#page=8).
Work over C on a smooth projective manifold, with fixed rank-two Chern
data and Gieseker–Maruyama stability for a fixed Kähler class. Proposition
2.15 uses a closed, polystable point of the semistable stack. Proposition
2.17 concerns the analytic slice germ and the restriction of the universal
Quot family, not merely its completion. Its proof first establishes formal
miniversality from the etale stack presentation, checks the tangent
isomorphism, and then invokes Flenner's analytic versality criterion.
Theorem 2.9 supplies openness for flat analytic families. Thus there is
no essential need to import formality to obtain analytic semiversality.

For applicability use L097's integral H and its already checked split
Gieseker-polystable fibre, not an identification of all h-polystable and
H-Gieseker loci. The harmonic family is locally free and flat. The precise
shrinking and comparison of the two actual semiversal families remain
work for the mathematical turn. Scalar ineffectivity and tangent action
are addressed by Lemmas 2.19–2.20; retain the full automorphism group
before passing to its effective ratio torus. No normality assumption on
the slice is supplied by these results.

**Ordinary algebraic quotient near the closed orbit.** Domingo Luna,
*Slices étales*, Mém. Soc. Math. France **33** (1973), 81–105,
DOI 10.24033/msmf.110,
[III.1, theorem and proof p. 97, Remark 3 p. 98](https://www.numdam.org/item/MSMF_1973__33__81_0.pdf#page=18).
The named theorem assumes a reductive group on an affine scheme over an
algebraically closed characteristic-zero field and a closed orbit. It
provides an affine stabilizer slice, a saturated open image, an etale
quotient map and the Cartesian comparison for the associated bundle.
Luna's conventions allow nonreduced affine schemes (I.1, p. 83). The
proof handles a smooth ambient scheme first, then a general closed
invariant subscheme by the base-change lemma in II.2, pp. 95–96.
Remark 3 explicitly gives the complex analytic local comparison.
The next proof must choose a GIT affine neighborhood of the split Quot
orbit and the quotient chart belonging to L097's H. The smooth-point
linearization refinement is not available as an assumption here.

**Ordinary analytic invariant functions and change of semiversal base.**
Nicholas Buchdahl and Georg Schumacher, *An Analytic Application of
Geometric Invariant Theory*,
[arXiv:2008.04625v3, 26 February 2021, Section 2.2 and Sections 5–6](https://arxiv.org/pdf/2008.04625v3).
Theorem 3 identifies the quotient structure sheaf with invariant
holomorphic functions for a closed invariant reduced analytic subspace
of a saturated open subset of a finite-dimensional representation. Its
general-case proof uses Stein complexification and the Reynolds operator;
it does not assume weak normality. Theorem 6 applies this construction
to the semiversal slice of a polystable bundle on a compact Kähler
manifold. Section 5.2, Lemma 2 and the descent proofs of Lemmas 3–4 and
Proposition 4 retain family base changes when comparing quotient charts.
Theorem 9's proof constructs the classifying map by actual semiversal
base change and checks choice independence and naturality. These are
tools for ordinary holomorphic descent; one still must verify their
restricted-action/saturation hypotheses for the comparison used here.

The fixed harmonic slice and its actual-family isomorphism are already
covered by L132's audited use of the same authors, *Polystable bundles
and representations of their automorphisms*, Complex Manifolds **9**
(2022), 78–113, DOI 10.1515/coma-2021-0131,
[Theorem 1, Lemma 2.5 and Proposition 2.6, pp. 78–84](https://d-nb.info/1262812674/34).
Reuse that adequate coverage; do not rederive its analytic construction.

## Stronger results and exclusions from use

Buchdahl–Schumacher, *An Analytic Application of Geometric Invariant
Theory II: Coarse Moduli Spaces*,
[arXiv:2108.03255, Section 6, Theorem 1 and proof, pp. 15–18](https://arxiv.org/pdf/2108.03255),
works in the weakly normal category. Its proof uses a removable-singularity
extension after passing to weakly normal structures. This does not
identify the ordinary image ring required here. Likewise Huybrechts–Lehn,
*The Geometry of Moduli Spaces of Sheaves* (1997),
[Theorem 4.5.1 and Corollary 4.5.2, p. 101](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113),
assumes stability; it is not the required reducible-point theorem.

Arbarello–Saccà, *Singularities of moduli spaces of sheaves on K3 surfaces
and Nakajima quiver varieties*, Adv. Math. **329** (2018), 649–703,
DOI 10.1016/j.aim.2018.02.003,
[Section 4, Propositions 4.2/4.4/4.7/4.8, pp. 667–672](https://www.math.columbia.edu/~giulia/Quiver.pdf#page=19),
is the previously recorded stronger quadratic-chart lead. Proposition 4.4
requires DG-Lie formality. Its proof distinguishes an equivariant formal
base isomorphism from a linearized family and then uses equivariant
approximation. An abstract quadratic chart therefore does not give the
specified harmonic-family comparison. The present source package avoids
requiring this stronger chart or a new proof of formality.

## Exact remaining specialization, without performing it

The next turn should construct the comparison between L132's complete
harmonic family and the analytic algebraic-slice family, with actual
bundle isomorphisms. It must justify quotient descent using invariant
holomorphic functions on suitable representatives, and check ordinary
reduced germ inverse identities. A non-equivariant semiversal base map
must not be called equivariant without justification. It must then
verify compatibility with L097/L098's actual classifying morphism and
compare the kernels of pullback to the local ring of the selected smooth
source germ. Reduction is part of the stated target; discarding nilpotents
in an ambient quotient must be explicitly justified for that target.

This is a scoped application of known theorems, not a reproof of them.
There is no source theorem that can be cited as already having carried
out this particular family/map check. No kernel equality or new lemma
is derived in this literature-only turn. Keep all other preimages over
the split coarse point separate: their union can have a different image
ideal. Do not invoke L099 or assume global normalization, separation or
degree two to obtain this comparison.

## Search record, limits and Mathlib

Queries included `Arbarello Sacca local moduli sheaves Kuranishi Luna slice
analytic isomorphism equivariant`, `Buchdahl Schumacher analytic GIT
quotient algebraic Gieseker moduli weak normalization comparison`,
`Luna slice Kuranishi space analytification sheaves holomorphic semiversal
Quot slice family comparison`, `"Quot" "semi-universal" "analytic"
sheaves slice`, `"Slice provides semi-universal deformation"`, and the
exact Greb–Toma title. Primary theorem reads, rather than snippets, support
the assessment above. Drézet's *Luna's slice theorem and applications*,
author PDF, Definition 4.14 and Theorem 5.3, provided a locator; Luna's
original statement and both proof cases were then read directly.
An external seminar note's arXiv identifier 1511.07321 is unrelated to
Arbarello–Saccà's sheaf paper and was rejected. A 2023 Bridgeland-moduli
survey and the general AHR stack theorem were search leads, not imported
coverage; their additional statements were not inspected. No claim of
novelty follows from these searches. Full matching Mathlib coverage is
not checked, and no absence claim is made.
