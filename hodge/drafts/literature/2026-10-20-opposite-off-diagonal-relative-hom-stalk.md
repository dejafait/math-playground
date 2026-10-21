# Opposite relative Hom stalk — assessed known-tool specialization

TARGET: Determine the length of the actual R^2 relative Hom stalk at a reduced off-diagonal coincidence of L121's opposite family.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact relative-Ext/diagonal and KS-difference searches led to Markman math/0009109v4 and a Mukai Proposition 4.10 lead; local comparison checked L066, L110, L118/L120/L121, ATTEMPTS/046 and the saved split first-variation assessment. Queries, inspected passages and the unimported Mukai lead are recorded below.
SOURCE_EVIDENCE: Inspected Markman Section 2, Remark 3(2), proof through (11), Lemma 4 hypotheses and Section 3; FIM 0904.1301v3 Remark 7.3, Theorem 7.6 and Section 8; BW 1309.2264v2 Definitions 3.2--3.8, Proposition 3.10 and Lemma 3.11; live Stacks 0B91, 0BCC, 0BCD, 0117, 0G81 and 00DV statements and relevant proofs. Reuse prior stable-Hom, surface Serre and GAGA coverage within its stated scope.
COMPARISON: Known perfect-pushforward, two-sided Hom deformation, cup/trace duality and local-algebra tools cover this base dimension. Markman already records a line-bundle-on-diagonal conclusion for universal families. The actual nonuniversal family still needs its own infinitesimal comparison; L121's reduced fibre product is not itself an annihilator theorem. This is a known-mechanism specialization, with no novelty inference.
GAP: No essential unread source blocks the bounded attempt. Establish the actual perfect presentation, isolate higher-image support away from the diagonal, identify the two independently varying Hom connecting maps and their reverse-Hom Serre transpose, then test all four cotangent directions and determine the ordinary stalk length. No rank or length is established by this review.
REASON: The separate literature gate is complete for the unchanged TARGET. Approve one later RESEARCH / REPRODUCTION attempt importing the general tools and deriving only their actual-family specialization; no new lemma, mathematical script, collision existence or length theorem is supplied here.
SCOPE: Hypothetical L071 equality kernel, L118 all-stable opposite family and L120/L121 actual finite normalization map; a selected ordered pair of distinct source points with the same opposite image, if one exists. Work away from the diagonal over the smooth four-dimensional base B times B.
LITERATURE_REASON: The changed Hom coefficient complex and base dimension are outside the prior surface End-stalk assessment; coverage must be checked before mathematics.

## Registration retained as historical scope

The following registration predates the completed review below. Its requests
for separate source approval have now been discharged only for this exact
target; its proposed mathematical conclusions remain unproved.

The main gap remains universal primitive rational Hodge realization.
This target could supply a sheaf-theoretic local input for a later global
coincidence budget. No useful global count or defect comparison is known.

Write B=S_1 and Y=S_2. Let G on Y times B be the factor-swapped actual
F. On Y times B times B let G_1,G_2 be its pullbacks using the respective
B coordinates, and let p project to B times B. The target is the ordinary
stalk of R^2 p_*(G_1^vee tensor G_2) at a selected (b,c), b unequal to c,
with isomorphic stable opposite fibres. It is not a derived-fibre dimension.
Retain the whole actual Hom complex; do not impose trace-free coefficients
between independently varying bundles. Choose neighborhoods away from
the diagonal. Isolation of the higher-image support under actual
base-change hypotheses is part of the review, not a new assertion here.

Essential inputs are L071 and L118/L120/L121. L066 and L110 are method
comparisons, not imported stalk conclusions. The next review should
retrieve primary hypotheses for perfect pushforward, amplitude, fibre
Ext dimensions, the natural KS-difference connecting map and relative
Serre duality over this base. Reducedness of the coincidence scheme
must not be promoted to a higher-image length theorem without that
comparison. No such comparison has been carried out this turn.

If later approved, the bounded test is to determine whether the actual
top-row ideal generates the whole four-dimensional cotangent space,
and then compute the stalk length from the presentation. Length one
is a possible threshold, not a conclusion. Continue only if the actual
first-order/duality comparison makes that ideal evaluable in every
direction. Otherwise record the missing map or higher-order data and
park the test; an arbitrary compatible complex cannot replace it.

This stable-family algebraic test does not reopen ATTEMPTS/061–063.
F, an off-diagonal collision, a global count, separation, reconstruction,
transport and the universal Hodge target remain unresolved. Full matching
Mathlib coverage is not checked. Separate literature approval is required;
no dependent mathematical work is performed at registration.

## Completed source review, 2026-10-20 (step 416)

This is one LITERATURE-only comparison. The main gap is still universal
primitive rational Hodge realization. The intermediate target is the
ordinary top relative-Hom stalk at a selected actual off-diagonal
coincidence. Its plausible downstream use is to replace unknown local
multiplicities in a possible global coincidence budget. No such useful
global budget is known; neither the hypothetical F nor any collision has
been constructed. No mathematical rank, length or new lemma is derived
in this review.

### Imported general inputs and applicability

[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91)
applies to a proper flat finitely presented morphism and a perfect
coefficient complex, giving perfect pushforward and arbitrary derived
base change. Here p is the projection from the product with the smooth
projective K3 Y, and G_1^vee tensor G_2 is a vector bundle. The theorem
does not restrict the base to a surface. Its proof reduces to 36.30.1;
the prior L066 assessment's Tor-independent point-base-change coverage
is reusable. Dual-number restrictions also fall within 0B91. This is
derived base change, not ordinary base change for all cohomology sheaves.

Reuse Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
first edition (1997), Proposition 1.2.7 and Corollary 1.2.8,
[pp. 11--12](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=23),
as inspected for L066. L118 gives one common H and the same numerical
class for all the opposite stable fibres, so the stable-Hom and
simplicity hypotheses match. Retain named surface Serre duality with
K_Y trivial, and projective GAGA for coherent cohomology and morphisms.
The actual numerical Ext dimensions, top-support comparison and
minimal ranks are to be written in the research step, rather than
copied from L066's different charge.

[Stacks Lemmas 15.77.6--7, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
and [0BCD](https://stacks.math.columbia.edu/tag/0BCD) provide minimal
free representatives with residue-field cohomology ranks and their
local spreading. Their local-ring/perfectness hypotheses admit
O_{B times B,(b,c)}, independently of its dimension four. Read the
zero-differential residue-field construction and uniqueness/Nakayama
proof, and the spreading argument. These theorems do not give ordinary
stalk lengths from derived-fibre dimensions.

[Stacks Lemma 12.13.12, 0117](https://stacks.math.columbia.edu/tag/0117)
gives functorial connecting maps of short exact cochain complexes.
Its snake-lemma proof supports comparison of a minimal representative
with the actual first infinitesimal coefficient sequence. The later
proof must exhibit the comparison, with fixed residue-field identifications
and the epsilon injection, for both degrees zero and one. Equality of
cohomology dimensions alone is insufficient.

Fiorenza--Iacono--Martinengo, *Differential graded Lie algebras controlling
infinitesimal deformations of coherent sheaves*, JEMS **14** (2012),
521--540, DOI 10.4171/JEMS/310,
[0904.1301v3, 19 November 2009](https://arxiv.org/pdf/0904.1301v3),
Remark 7.3 and Theorem 7.6, printed pp. 17--19, and Section 8,
pp. 20--21, supply the perturbed differential, natural deformation
comparison and explicit Dolbeault realization. Read the theorem's
negative-cohomology hypothesis and the Section 8 fine-resolution case.
Vector bundles placed in degree zero satisfy that hypothesis. Apply
the framework to the direct sum of the two fibre bundles and its
block-diagonal actual deformations; retain the off-diagonal Hom block.
This use does not require simplicity of the direct sum. The two summands
vary independently, so L110's single-bundle scalar adjoint calculation
must not be substituted. The two-sided differential and all its graded
trace signs are the remaining specialization, not a theorem asserted
here. No formality or convergent normal-form theorem is needed.

Budur--Wang, *Cohomology jump loci of differential graded Lie algebras*,
Compositio Math. **151** (2015), 1499--1528, DOI
10.1112/S0010437X14007970,
[1309.2264v2, 2 October 2014](https://arxiv.org/pdf/1309.2264v2),
Definitions 3.2--3.8, printed pp. 10--11, and Proposition 3.10 with
Lemma 3.11, p. 12, give the module/Aomoto construction and functorial
gauge comparison. Inspected the module Leibniz conditions, boundedness
and finite-cohomology assumption, and both identities in the gauge proof.
Dolbeault Hom coefficients on the compact surface meet that scope.
Reuse the prior split assessment's determinantal invariance coverage only
as supporting theory; no determinantal ideal is identified with the
coincidence ideal here. The stronger stable zero-Chern resonance theorem
is not applicable and is not imported.

[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
constructs perfect pushforward duality from an actual coefficient pairing
into the relative dualizing complex. Inspected its cup/trace construction
and proof via the proper-flat duality adjunction. In this application
the pairing is composition/trace between the two **opposite** Hom
bundles, and the relative dualizing complex has the K3 surface shift.
It pairs the forward complex with the reverse complex; it does not
identify either coefficient bundle with End_0 of one moving bundle.
The shift is relative dimension two, not base dimension four. A fixed
nonzero fibre two-form gives surface Serre pairings on derived fibres.
The next proof must retain these actual maps when transposing the first
variation; scalar self-Hom simplicity alone gives no cotangent rank.

[Stacks Lemma 10.20.1, 00DV](https://stacks.math.columbia.edu/tag/00DV),
parts (2) and (8), is the imported Nakayama criterion. Its finite-module
and Jacobson-radical hypotheses hold for finite modules over this
Noetherian local ring. Read the determinant proof and quotient argument.
The research step may apply it after proving full cotangent generation
of the actual final-row ideal; no radical replacement is authorized.

### Stronger known result and duplicate/failure comparison

Markman, *Generators of the cohomology ring of moduli spaces of sheaves
on symplectic surfaces*, J. reine angew. Math. **544** (2002), 61--82,
[math/0009109v4, 21 April 2001](https://arxiv.org/pdf/math/0009109v4),
Section 2, Remark 3(2), printed p. 3, already states that the universal
relative Ext^2 is a line bundle on the diagonal. Read the smooth stable
quasiprojective scope, which does not require completeness, the proof
through (11), pp. 4--6, and Lemma 4's hypotheses. Section 3, p. 12,
starts from local universal families in the etale or complex topology
when a global universal family is absent. This is substantive overlap
with the proposed local length mechanism, not an originality lead.
Its global diagonal Chern formula is not a four-dimensional subfamily
length formula. An import through local universal charts would still
need actual-family identification, possible base-line twists and the
correct top-degree base-change argument; ordinary pullback of all
relative Ext sheaves is unjustified. The direct first-variation test
below avoids those additional chart comparisons and specializes the
same known mechanism. No general diagonal theorem is being reproved.

The Mukai *On the moduli space of bundles on K3 surfaces I* (1987),
Proposition 4.10, p. 381,
[author-hosted PDF](https://www.kurims.kyoto-u.ac.jp/~mukai/paper/Tata.pdf),
was a search lead. Search extraction showed a more restrictive vanishing
claim for other relative Ext degrees, so its surrounding hypotheses
cannot be suppressed. The PDF text was unavailable and two screenshot
requests failed. Its full statement/context and proof have **not** been
inspected, and no conclusion from it is imported. It is not essential
to the approved direct-complex approach above.

Local overlap reads were L066's actual Hom calculation and explicit
isolated-jump model; L110's first-variation and rank-to-length proof;
L118/L120 hypotheses and conclusions; L121's proof and audit; and
ATTEMPTS/046. Reused the precise general-source coverage in
`drafts/literature/2026-10-16-equality-split-first-order-defect-length.md`
and the earlier Hom working review. L066 is a different charge and did
not compute this ordinary top stalk. Its failure concerned separation:
an isolated Hom jump survives even an injective first obstruction.
Determining the multiplicity of an allowed collision does not reopen
that failed separation test. L110 is a method comparison over a
two-dimensional base with different coefficients. L121 supplies actual
geometric tangent information, but no higher-image annihilator. No
duplicate completed stalk result was found in these targeted reads.
ATTEMPTS/061--063 and the parked order-five route remain untouched.

Discovery queries were `"relative Ext" "diagonal" "K3" Markman`,
`"Kodaira Spencer" "Hom" "difference" deformation vector bundles`,
`"Ext" "transverse" "K3" "diagonal" sheaves`,
`Markman "Ext" "diagonal" "cohomology ring" generators`,
`"relative Ext" "sheaf" "diagonal" "K3"`,
`"Ext^2" "structure sheaf" "diagonal" Markman`,
`Mukai moduli bundles K3 surfaces I Proposition 4.10 pdf`,
`"Mukai" "4.10" "Ext"`, and
`"Markman" "Ext" "line bundle" "diagonal"`.
Nonprimary discussions were discovery leads only. No novelty claim
is inferred from the bounded search. Stacks statements were inspected
live on CHECKED using their stable tags. Full matching Mathlib coverage
is **not checked**, not asserted absent.

### Approved continuation and stopping test

Retain L071 equality hypotheses and L118/L120/L121's actual opposite
family, its natural KS identification and disjoint tangent planes at
the selected ordered collision. Treat L066 and L110 only as methods;
their numerical stalk conclusions are not inputs. F and a distinct
isomorphic pair remain unproved existence assumptions. Work near that
pair away from the diagonal and retain the entire Hom complex.

One subsequent mathematical attempt may construct the actual algebraic
minimal presentation, justify its support and final rank by the imported
stable-Hom/Serre/base-change tools, and compare the first infinitesimal
Hom coefficient sequence with that presentation. It must identify the
degree-one connecting map using reverse-Hom Serre duality and the
actual difference of the two KS classes, with all odd signs retained.
Then test whether the final-row coefficients span the full
four-dimensional cotangent space. Length one is the proposed threshold,
not a result of this review. If full generation is proved, use Nakayama
to compute the actual ordinary cokernel, including all higher terms.
If the actual comparison fails or leaves a deficient rank/unknown map,
record it and stop this mechanism; no arbitrary compatible complex or
reduced-support assertion replaces it. Success would supply a local
conditional multiplicity only, leaving collision counts, a useful global
defect comparison, separation, F, transport and the Hodge gap unresolved.

No further literature turn is needed for this unchanged target. The
appropriate completed mathematical classification would be REPRODUCTION.
