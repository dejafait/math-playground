# Actual split-fibre derivative and higher-image length — assessed specialization

TARGET: Determine whether L095's actual split-fibre Kodaira--Spencer map forces length((R^2p_*End_0(F))_z)=1 at every z in Z.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched actual first-order/cohomology-jump, DGLA-pair/Aomoto, split-bundle KS/Brill--Noether and endomorphism/Bockstein terminology; targeted local overlap search found no completed length calculation. Primary discovery led to Budur--Wang 1309.2264v2 and Fiorenza--Iacono--Martinengo 0904.1301v3; stronger zero-Chern/stable conclusions were checked and excluded from applicability.
SOURCE_EVIDENCE: Read BW Definition-Proposition 2.2 and proof, Corollaries 2.3--2.4, Definitions 3.1--3.8, Proposition 3.10 and proof, and Section 6 hypotheses/proof comparison; FIM Remark 7.3, Theorem 7.6 and Section 8's explicit Dolbeault realization, with Section 1's gluing cases; Stacks 0117, 00DV and 0BCC statements/proofs and 0G81's cup/trace duality. Reuse L094's Serre/coefficient inputs and L108/L109's audited perfect-pushforward and duality coverage within scope.
COMPARISON: Known results supply natural twisted complexes, adjoint differential and gauge compatibility, minimal presentations, cup/trace duality, functorial connecting maps and Nakayama. They do not state the length-one conclusion for this conditional family; the remaining work is to match the actual KS with the linear term, compute its full cotangent rank using split cohomology, and apply the local-algebra criterion.
GAP: No actual rank or length is established here. The approved mathematical specialization must verify the trace-free adjoint action and Serre transpose on the actual first infinitesimal family, retain the algebraic derived presentation, and test whether its last row generates m_z; an extra geometric premise or deficient cotangent rank stops this mechanism.
REASON: Essential source coverage is now available for the unchanged target; the next step should be mathematics. This is source-coverage progress using known tools, not a new length theorem, a new Hodge input or certified originality.
SCOPE: Conditional (14,21) family of L108 at a closed split parameter z; actual C=Rp_*End_0(F), its minimal local presentation and first-order map. Z may be empty. No count of Z, metric extension, semistability, F existence or Hodge realization.

## Proposed bounded test and relevance

The main gap remains algebraic realization of primitive rational Hodge
classes. The intermediate target concerns the local higher-image defect
in corrected L108's budget c_2(N)=(800-w-q)eta. If the proposed length-one
conclusion is justified, L109's q_z<=w_z would make the defect budget
depend on the number of split parameters rather than uncontrolled local
orders. That cardinality, metric extension, semistability, existence of
F and transport would all remain unresolved. No complete route follows.

Essential inputs for the proposed continuation are L094's actual split
cohomology and stabilizer action, L095's actual harmonic KS derivative,
L097's finite possibly empty split locus, corrected L108's perfect
complex and hull, and audited L109's normalized duality. L071's full
tensor and fixed metric remain retained through L108. Consult those exact
canonical passages only after reading the current checkpoint/overview;
no cross-notebook theorem is proposed.

The discriminating test is whether the linear coefficients of the final
differential in an actual minimal free representative span the full
two-dimensional cotangent space m_z/m_z^2. The degree-two derived fibre
has dimension one, so the final term has rank one; this does not determine
its cokernel length. The natural first-order map must be identified from
the actual family before applying a local-algebra criterion. Mere KS
injectivity, the rank of an arbitrary model, or a fibre dimension must
not be substituted for that identification. Source review must check
which Yoneda/commutator action occurs and its trace/duality conventions.
No first-order rank computation is made in this proposal.

Continue toward the length-one test only if primary coverage supplies
that natural comparison with all hypotheses. If the actual linear map
fails to control the two cotangent directions, record the precise rank
failure or missing premise and abandon this first-order length mechanism;
do not repeat the duality-only sequence. This test explicitly adds data
omitted by L109's countermodels and preserves ATTEMPTS/067. It does not
reopen the automatic metric inference stopped in ATTEMPTS/066 or the
metric/local-degree and determinant routes in ATTEMPTS/063/065.

The immediate-record search found no completed first-order local-length
calculation there; this is not a claim of novelty or an exhaustive search.
The separate literature review below now supplies the missing primary
comparison tools and approves only the bounded specialization. The actual
first-order rank and local length remain uncomputed. Full matching Mathlib
coverage has not been checked. No theorem or new mathematical result is
asserted in this assessment.

## Completed primary-source comparison

This is a LITERATURE-only step. The sources below are imported as general
inputs; the proposed family's linear-rank and length assertions are
reserved for the next mathematical step. No general source theorem is
reproved here, and no source is asserted to contain the exact local
conclusion. The prior proposal above is preserved as motivation.

### Natural deformation and adjoint coefficients

Fiorenza--Iacono--Martinengo, *Differential graded Lie algebras controlling
infinitesimal deformations of coherent sheaves*, JEMS 14 (2012), 521--540,
DOI 10.4171/JEMS/310; inspected
[0904.1301v3, 19 November 2009](https://arxiv.org/pdf/0904.1301v3).
Theorem 7.6, printed p. 19, and Section 8, pp. 20--21, give natural
Artinian deformation functors and their explicit Dolbeault realization.
No simplicity is required. The theorem's negative-cohomology hypothesis
holds for a locally free bundle in degree zero. Section 1, pp. 4--6,
checks perturbed differentials and conjugation gluing, including overlap
compatibility; the bundle case has genuine cocycles. Remark 7.3,
pp. 17--18, gives d_x=d+[x,-]. These constructions, not a smooth coarse
moduli space, are the imported comparison tools.

The relevant application is to deformations of the actual split vector
bundle E, with coefficient module End_0(E) under the **adjoint** action.
It is not the defining-module action on E and not multiplication on just
one side of End(E). The next proof must explicitly identify the induced
End differential in this actual family, restrict the trace-free summand,
and compare its first-order connecting map with that of L108's minimal
representative. The standard trace splitting in characteristic zero and
L108's existing algebraic KS comparison provide the appropriate local
scope. No formality theorem or convergent quadratic normal form is needed
for a first infinitesimal comparison, and none is imported by this review.

Budur--Wang, *Cohomology jump loci of differential graded Lie algebras*,
Compositio Math. 151 (2015), 1499--1528, DOI
10.1112/S0010437X14007970; inspected
[1309.2264v2, 2 October 2014](https://arxiv.org/pdf/1309.2264v2).
Definitions 3.1--3.8, pp. 10--11, allow bounded-above DGLA modules
with finite cohomology; Definition 3.8 gives d_omega=d tensor id+omega.
Proposition 3.10 and Lemma 3.11's proof, p. 12, check gauge compatibility,
retaining conjugation and differential terms. No trivial-stabilizer
hypothesis enters this abstract framework. Section 6, Remark 6.3 and
Theorem 6.4's proof, pp. 16--17, identify the Dolbeault/derived comparison
and refer to FIM. Its stronger stable, zero-Chern resonance statements
(Theorem 1.3) are inapplicable here and are not imported. Our next proof
uses the general construction with the adjoint coefficient module.

### First-order presentation, duality and the final algebra test

BW Definition-Proposition 2.2 and Corollaries 2.3--2.4, p. 7,
cover determinantal jump ideals, quasi-isomorphism invariance and base
change for flat complexes. Its four contractible-summand cases were read.
Minimal representatives
and their residue-field Betti ranks are already covered in L108 by
[Stacks Lemma 15.77.6, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
and 0BCD. The current 0BCC statement and proof were also inspected: it
uses a local ring and a pseudo-coherent complex and identifies minimal
representatives up to isomorphism. It does not identify cohomology-stalk
lengths with fibre dimensions.

[Stacks Lemma 12.13.12, 0117](https://stacks.math.columbia.edu/tag/0117)
constructs functorial connecting homomorphisms for a short exact sequence
of cochain complexes in an abelian category; its snake-lemma proof was
read. This supplies the chain-level naturality required when comparing
the first infinitesimal restriction of the actual Dolbeault complex with
the minimal algebraic representative. The next specialization must write
that comparison explicitly and compute the linear part, rather than
asserting it merely from equality of fibre cohomology dimensions.
Analytic tangent descriptions are used only on the actual infinitesimal
family with the existing algebraic/analytic comparison retained in L108;
an arbitrary analytic family or its coarse image is not substituted.

For duality, reuse L094's actual split cohomology and coefficient trace
pairing and L109's audited normalization. The newly inspected
[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
constructs perfect pushforward duality from an actual coefficient pairing
and relative cup/trace; its pseudo-coherence and perfectness scope is
satisfied by L108. This supports Serre duality without simplicity or
ordinary base change of A_1 at z. The next proof must retain graded
cyclic trace when relating the degree-one first variation to the
stabilizer action on degree-one cohomology. Its sign and any nonzero
normalization must be checked there; no rank is calculated here.

[Stacks Lemma 10.20.1, 00DV](https://stacks.math.columbia.edu/tag/00DV),
parts (2), (6), (8), and their determinant/module-quotient proof, give
Nakayama for a finite module over a local ring. This is the relevant
criterion for lifting generation from the cotangent quotient to the
maximal ideal. The needed module is finite because R=O_{B,z} is
Noetherian. The proposed R/I length-one test, its equivalence with full
linear generation in this rank-one final term, and the actual generation
are to be justified next; neither a reduced defect nor that generation
is assumed in this review.

### Search, overlap, qualifications and decision

Queries included "Budur Wang cohomology jump loci differential graded Lie
algebra pairs endomorphism bundle Aomoto complex theorem", "first order
deformation vector bundle cohomology connecting homomorphism cup product
Kodaira Spencer endomorphism commutator", "cohomology jump endomorphism
first order", "split Kodaira-Spencer Brill-Noether vector bundle", and
"endomorphism Bockstein deformation bundle". The inspected primary
matches supply the framework above. Curve Brill--Noether, rank-one flat
local-system and generic resonance snippets were not used as theorems;
no exact ready length-one statement was identified in this bounded
search. This is not an assertion of novelty or an exhaustive search.

Targeted local overlap checks used L094/L095/L108/L109, ATTEMPTS/067,
history/308 and searches in the dated local literature/working notes and
history/30*. L101's trace-free Dolbeault passages were read only to check
existing coefficient conventions, not to replace the actual product
family by its constructed complex germ. The existing split action and
actual KS inputs are essential; L109's unbounded duality-only models omit
them and therefore do not settle this test. Preserve all prior stop
evidence, including ATTEMPTS/063/065/066/067. No cross-notebook input was
used. Full matching Mathlib coverage was not checked; no absence claim is
made.

DECISION SPECIALIZE approves exactly the saved TARGET for one bounded
mathematical attempt. Its permitted work is the actual infinitesimal
comparison, split-action/Serre rank test, and the associated local
length conclusion or precise failure. Continue only if the comparison
and both cotangent directions are justified from the retained inputs;
otherwise document the missing premise or rank failure and abandon the
first-order length-one mechanism. Include Z empty. Even success provides
no bound on the number of split parameters and no metric extension,
semistability, F existence, cycle or transverse transport. The global
Hodge conjecture remains IN_PROGRESS.
