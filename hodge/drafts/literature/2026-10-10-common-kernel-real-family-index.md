# Common-kernel real family index — source comparison

TARGET: Assess real family-index constraints linking both orthogonal images of one L079 kernel to the constructed E_4/J_5 branch.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact-title and real/quaternionic families-index searches reached Atiyah--Singer V, Atiyah--Bott--Shapiro, Berwick-Evans and Eschenburg--Hanke; the existing BBHR transform input and local L079/ATTEMPTS/043,/045,/053 stops were compared. No matching theorem for this prescribed joint image pair was located in the inspected sources; no novelty inference follows.
SOURCE_EVIDENCE: Atiyah--Singer V, Section 1 Theorem (1.5), pp. 140--143; ABS Clifford modules, Sections 4--5 and 11--12; Berwick-Evans 2303.09091v1, Theorem 1.3 and Section 8.1--8.2, Proposition 8.4 and proof; Eschenburg--Hanke 2011.14368v2, Section 10 Propositions 10.4/10.6 and Theorems 10.7--10.9; BBHR (1998), Definition 2, Section 3.3 and Theorem 3, pp. 244--246. Statements and the relevant real-symbol, spectral-cut, Clifford-Morita and odd-IT proof cases were inspected.
COMPARISON: Known real family indices retain information forgotten by complexification; four-dimensional spin Thom theory exchanges real and quaternionic coefficient types. BBHR identifies the complex odd image with the negative Dirac index. These inputs support a bounded real-structure specialization, not a theorem computing the joint attainable pair for L079's fixed rank-two kernel.
GAP: Match the spinor/coefficient real structure with L079's normalized Serre-pairing reduction for each projection; then determine the full allowed quaternionic kernel classes and their joint pushforwards, including torsion and finite-rank realizability. None is supplied by rational GRR or separate block existence.
REASON: Approve source coverage only for the separately stated real-index identification target. Defer the joint characteristic calculation: its original approval threshold is not yet met. This is local source-coverage progress, with no new mathematical result or Hodge algebraicity.
LITERATURE_REASON: The new common-kernel and real-index hypotheses were outside prior standalone-image coverage; this review reads their essential primary inputs rather than refreshing unchanged complex GRR or independent indices.
SCOPE: L079's exact (-13,-14) hypotheses on identical marked S x S, both actual odd images and their parallel symmetric forms; L083 E_4 and L082 J_5 as individual blocks only. All kernel lifts, both orientations and unresolved J_5 choices remain admissible. No other notebook is used.

## Gap, use and discriminating test

The main gap is universal primitive rational Hodge algebraicity. The
local construction gap is one holomorphic F with L079's full negative
mixed tensor and the selected two actual images. A real-index bridge
would permit a later joint topological screening of that branch before
attempting kernel construction. Even a successful screen leaves
holomorphic F, prescribed mixed action, image identification and
transverse transport unresolved.

The original proposed calculation needs more than independent image
indices. Its threshold has **not** been reached here: no attainable-pair
set, Stiefel--Whitney value or torsion cancellation has been calculated.
The next bounded target is only the prerequisite identification. Continue
if both actual real reductions are identified with the same coefficient
kernel's properly signed spin-family indices. Park this mechanism if
that comparison requires an additional unavailable real structure, or
if it can identify only complexifications. If the bridge succeeds, a
later reviewed target must retain every finite-rank lift and test the
pair simultaneously. Matching a stable necessary test would not prove
finite-rank, holomorphic or kernel existence.

## Primary inputs and exact scope

[Atiyah--Singer, *The index of elliptic operators: V*, Annals of
Mathematics (2) **93** (1971), 139--149](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/as5.pdf),
Section 1, pp. 140--143, Theorem (1.5): a continuous real elliptic family
on compact smooth fibres over compact Y has equal analytic and
topological indices. Its symbol uses KR of the vertical tangent with
antipodal fibre involution, while the base has trivial involution and
its index lies in KO(Y). Constant kernel/cokernel dimensions give their
real virtual difference. The proof checks the real Thom construction
and equivariant fundamental symbol, using injectivity of real-to-complex
representation rings only at that proof stage. The introduction warns
that base-bundle complexification is generally noninjective. This is
not a theorem recovering a real index from rational Chern characters.
The real-algebraic conjugation remark on p. 143 is a different setting;
no antiholomorphic base involution is assumed here. The PDF is a journal
scan on an academic mirror, not a publisher-hosted copy.

[Atiyah--Bott--Shapiro, *Clifford modules*, Topology **3**, Supplement 1
(1964), 3--38](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/abs.pdf),
Sections 4--5, Tables 1--2 and Proposition (5.4), supply the negative
Clifford convention and the real/quaternionic module types, including
Cl_4 and its even algebra. Section 11, Propositions (11.2)--(11.3),
Theorem (11.5), pp. 27--28, supplies multiplicative Clifford classes
and the coefficient-ring identification with KO. The proof compares
Bott/Hopf generators, retaining the mod-two coefficients. Section 12,
Theorem (12.3), p. 31, explicitly states its unshifted real theorem for
rank 8k; citing that display as an unshifted rank-four Thom formula
would be wrong. Use the next source for the four-dimensional type
change. The scan is an academic mirror. These standard results are
imported, not reproved or claimed original.

[Eschenburg--Hanke, *Bott–Thom isomorphism, Hopf bundles and Morse
theory*, arXiv:2011.14368v2, 27 January 2021](https://arxiv.org/pdf/2011.14368v2),
Section 10, pp. 33--36: V is oriented Euclidean of rank 4m over a
finite CW complex; the stated type identifications require a spin
structure. Proposition 10.4 proves the module decomposition by
Hom_Cl evaluation, checking separately the R and H commutants and
balanced tensor product. Proposition 10.6 passes this to stable groups.
Theorem 10.7(b), m odd, maps KSp(X) to reduced KO of the Thom space;
Theorem 10.9(a), m odd, maps KO(X) to reduced KSp of the Thom space.
Both use the spinor Hopf bundle. These fix the rank-four real/quaternionic
exchange; they are not family-image identifications. The text explicitly
leaves detailed proofs of the complementary statements 10.8--10.9 to
the reader; the inspected Morita construction explains their scope,
without turning them into finite-rank existence theorems. Publication:
São Paulo J. Math. Sci. **15** (2021), 127--174,
[DOI 10.1007/s40863-021-00215-6](https://doi.org/10.1007/s40863-021-00215-6).
Preprint page numbers above fix the version used.

[Berwick-Evans, *The families Clifford index and differential KO-theory*,
arXiv:2303.09091v1, 16 March 2023](https://arxiv.org/pdf/2303.09091v1),
Theorem 1.3, p. 2, and Section 8.1--8.2, pp. 31--33, Definition 8.1,
Proposition 8.4 and proof: a smooth proper spin fibration of fixed
real fibre dimension n, a vertical metric, horizontal projection and
metrized **real** coefficient bundle with compatible connection give
an analytic class in KO^{-n}(B). Spectral-cut eigenspace bundles glue
via Clifford actions on their complements and represent that class;
the construction is independent up to concordance. This retains the
Clifford index rather than only its characteristic differential form.
The statement does not directly take L079's complex rank-two F as its
real coefficient V. Replacing it by the underlying real rank-four
bundle and forgetting the quaternionic action would answer a different
question. This source is supplementary analytic/degree coverage, not an
asserted computation of our quaternionic coefficient index.

[Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier transform*,
Differential Geometry and its Applications **8** (1998), 239--249](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf),
Definition 2 and Section 3.3, pp. 244--246, Lemmas 1--2 and Theorem 3:
compact hyperkahler source, compatible complex-structure spheres,
hermitian quaternionic-instanton kernel and source instanton, with
all-parameter odd/even IT. The smooth complex image is respectively
minus/plus the Dirac index; the proof uses the same (co)kernels,
base-change comparison and compatible induced connection. L079 has
source O_S, actual kernel F and every-fibre odd IT in both directions.
Here “quaternionic instanton” is a curvature condition; it does not by
itself mean a bundle with structure group Sp(1). The latter coefficient
structure must use rank two, determinant wedge and a compatible unitary
metric. The paper does not explicitly identify L079's real Serre
reduction, so that necessary specialization remains the next target.
Its result is already ready coverage locally and is reused here.

## Local qualifications and duplicates

Read L079's hypotheses, actual images, parallel duality and
characteristic/stopping passages; L082/L083 statements; L080's seed
statement; and L050's finite-rank criterion passage. Read
ATTEMPTS/043,/045,/053 and the earlier flat-index source assessment.
No repeated standalone characteristic or adjoint-index calculation was
performed. The persistent Itoh curvature-source blocker concerns a
different positivity mechanism and is not reopened by this accessible
index theorem.

The kernel is complex rank two with determinant trivial, but its full
quaternionic topological class is not specified by L079's rational
character. L050's finite-rank existence criterion supplies neither a
classification of its lifts nor both real family indices. L082 gives a
quadratic deformation of O+E+E^vee, not an arbitrary orthogonal class;
any later calculation must justify its actual topology from that family
and retain other allowable J_5 choices. L083 gives E_4 independently.
Do not equate those constructions with the images of one F.

Both projection fibres have real dimension four and complex orientation;
the K3 spin data are available from the trivial canonical bundle and
vanishing H^1(S,Z/2), but explicit spinor conventions and the sign of
the actual odd kernel remain to be checked in the specialization.
A mere match of complexifications cannot settle w_2 of either image.
No universal family, inverse transform or existence of F is required
to apply a conditional index theorem; none is supplied here.

## Coverage decision and continuation

Known inputs suffice for a bounded proof attempt identifying the two
actual real image reductions. Its precise approved scope is saved in
[the identification assessment](2026-10-10-common-kernel-real-index-identification.md).
This is a newly written ready continuation, subject to the supervisor's
separate next-turn approval. It permits no joint attainable-pair or
characteristic computation yet. No new lemma or mathematical script
was written in this literature-only step.

Mathlib: full real family-index theorem, spin/quaternionic Thom
specialization and joint-pair constraint **not checked**. No absence
claim is made. No complete Hodge candidate has been obtained.
