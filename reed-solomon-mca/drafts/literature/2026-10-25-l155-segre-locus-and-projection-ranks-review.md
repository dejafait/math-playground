# L155 pair locus and projection ranks — completed source comparison

TARGET: Determine whether the projective nonzero decomposable locus of every L155 pair kernel is exactly the Segre image of P(V_a) times P(V_b), with both quotient projections of rank one, over every extension of F_97.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 481 discovery and exact two-space/common-transversal comparison; narrowly checked L109 recovery cases, L155 statement and linear proof, the step-484 audit scope, and ATTEMPTS/048–049. No duplicate locus proof found in these inspected passages; no novelty inference. No broad discovery repeated.
SOURCE_EVIDENCE: Reused step 481 primary coverage and refreshed Bader–Cossidente–Lunardon, Generalizing flocks of Q+(3,q), Advances in Geometry 1 (2001), section 2, definition and full proof of Theorem 1, pp. 324–325, DOI 10.1515/advg.2001.019, https://www.researchgate.net/publication/249879499_Generalizing_flocks_of_Q_3q ; Stacks Lemma 27.13.6 Tag 01WD, entire statement and proof, https://stacks.math.columbia.edu/tag/01WD ; Conrad Exterior Powers, Theorem 7.1 and following all-fields qualification, Corollary 7.3, Theorem 7.5 and Corollary 7.6 with complete proofs, printed pp. 23–26, https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf . All refreshed 2026-10-25; earlier inspected exterior-map/basis coverage reused.
COMPARISON: Known two-disjoint-space correspondence, Segre embedding and Plucker reconstruction cover the general geometry over arbitrary fields. Audited L155 now supplies the previously missing disjointness and linear identification. The remaining work is a bounded local applicability proof in the original exterior space, including explicit rank-zero versus rank-one cases for both actual quotients; the sources do not state this labeled-pair conclusion verbatim.
GAP: Write the exact ambient exterior-space/plane correspondence and both actual quotient-rank specializations from L109/L155, importing the general geometry. This source review supplies no proof of that local conclusion, no extra-row compatibility result and no recovery-gate removal.
REASON: Essential coverage is complete for this unchanged field-valued target; approve SPECIALIZE with REPRODUCTION for the next mathematical attempt. The audited bridge removes the earlier source-applicability obstruction, without requiring another input census or a new general Segre theorem.
LITERATURE_REASON: Step 484 proposed a changed locus/projection-rank scope explicitly excluded by the ready linear bridge and audit assessments; this turn completes only that essential comparison, reusing step 481 rather than repeating discovery.
SCOPE: All original L153 disjoint-support pairs, unchanged H/S/J and original Q/N maps, over every E/F_97; E-rational projective points without rational descent. No classification of extra-row constraints, chart normalization, weight gates or twelve-row solving.

## Step-484 proposal retained; completed approval below

The main gap is uniform twelve-row compatibility. An exact description
of the pair locus could replace opaque linear kernel coordinates with
factor coordinates before a separately assessed many-row test. This is
prospective usefulness, not a complexity bound or exclusion.

The exact proposed map is ([a],[b]) -> [a wedge b], with a in V_a
and b in V_b nonzero. The requested conclusion is exhaustion of the
projectivized nonzero decomposable locus in the original common kernel
and rank(Q_a restricted to L)=rank(Q_b restricted to L)=1 for every
associated two-dimensional plane L. This paragraph specifies a target;
it does not establish that conclusion or remove a zero-rank branch.
The claim concerns field-valued points, with no additional assertion
about scheme-theoretic intersections or nilpotents.

Use L155's audited disjointness and linear identity with L109's actual
maps and L153's complete original domain. Compare the recorded primary
two-disjoint-space correspondence and Segre embedding with this precise
ambient exterior-space formulation. The existing source comparison
already distinguishes the two-space parameter variety from Sottile's
three-space transversal union and a generic fourth-space count. Do not
substitute either latter result, assume generic position, identify
kernels of different labeled pairs or repeat passed finite audits.

The next turn is source comparison only until this exact scope is
approved. Reuse adequate inspected statements and proof cases; retrieve
only an essential missing case if the recorded evidence does not cover
it. Import a matching known result by precise citation and justify only
the local specialization, rather than reprove the general Segre theorem.
Approval requires coverage of arbitrary E and the embedding/plane/rank
identifications. If there is a real mismatch, retain it and narrow or
abandon the proposed identification; no further lemma is authorized now.

All nonzero-lambda, full-weight, original finite-chart and simultaneous
row gates remain independent even if this target later passes. Prospective
coding use retains C152a/L086/L152 and L154 only for relevance; q=97^20,
k=8, pinned cell, U_S, nonzero actual D/locators, sixteen finite events,
coding t=0, arbitrary weights/chart and L056/L069/L040 plus L051/L055
qualifications remain. L104 survivors, L151 label limits and
ATTEMPTS/041–043,/048–049 persist. Representation and challenge
identification remain open. Matching Mathlib coverage is not checked.

## Completed comparison — step 485

This is literature-only. The preceding proposal records its preapproval
state; the SPECIALIZE decision above and this section supersede its
pending-review language. No local locus theorem is derived or approved
as proved here. No lemma, script, PROOF or DAG was changed.

### Primary coverage and its boundary

Bader–Cossidente–Lunardon section 2 starts with an arbitrary field K.
Its definition uses tensor coordinates; the proof of Theorem 1 gives
the correspondence with lines meeting two fixed disjoint projective
n-spaces. Take n=2 for the proposed application. This is the geometric
correspondence to import, not the theorem's additional Veronese/regulus
claim or the later finite-field flock constructions. The author-uploaded
article text was inspected, not merely its abstract. No hypothesis of
generic position or algebraic closure belongs to this correspondence.
It does not mention our original quotient matrices or seven-dimensional
ambient space. The local embedding comparison still must be written.

Stacks Lemma 27.13.6 gives the Segre closed immersion over every base
scheme, with product homogeneous coordinates. Its proof checks every
standard product chart after reduction to Spec(Z). It covers the
embedding needed after a linear coordinate identification, without
assuming E algebraically closed. It does not itself identify a given
intersection of an exterior linear space with a Grassmannian. We request
only E-valued points, not scheme-theoretic intersection or reducedness.

Conrad's Theorem 7.1 is stated first over R, but its following paragraph
explicitly extends the proof to every field. Corollary 7.3 supplies the
span criterion. Theorem 7.5 and Corollary 7.6 supply basis-independent
plane reconstruction from a nonzero elementary wedge. Their complete
proofs were inspected, including the converse. Reuse the already read
Theorems 4.2/5.1 and 5.6/Corollary 5.9 for exterior bases, actual induced
maps and subspace inclusions. The general-module exception does not
apply to vector spaces over E. These cover the standard exterior tools;
no reproof of them is needed. Standard rank-nullity is the additional
named linear-algebra input for restricted quotient ranks.

### Exact approved specialization obligations

Use only the actual L109 maps and audited L155 conclusions on the
original L153 domain. L155 supplies disjoint three-dimensional kernels
and their nine-dimensional mixed-wedge span, uniformly over E/F_97.
Those are established inputs, whereas the following remain proof
obligations for the next research turn:

1. Identify the Segre product-coordinate embedding with
   ([a],[b]) -> [a wedge b] in the original common kernel, retaining
   the original sign convention. Justify applicability in E^7 rather
   than silently replacing its ambient space by E^6.
2. Establish exhaustion of its nonzero decomposable projective points
   and uniqueness of factor lines using the imported correspondence
   and exterior reconstruction. Address a reconstructed plane that
   might initially appear to have a component outside V_a + V_b.
   A linear span identity alone is not this exhaustion statement.
3. Relate each reconstructed two-plane to both original quotient maps.
   Use the induced exterior maps and rank-nullity; distinguish rank
   zero from rank one separately for a and b, including planes
   potentially contained in a quotient kernel. Do not invoke actual
   coding-pencil nonpersistence merely to remove a geometric branch.
   The conclusion sought is for the entire stated locus, before gates.

This list specifies the local specialization to attempt, not a derivation
of those statements. No new generic theorem is needed or authorized.
SPECIALIZE rather than IMPORT records that the cited correspondence
alone does not assert the exact ambient-kernel and matrix-rank claim.
The next proof should cite the general geometry and supply only these
applicability details; REPRODUCTION is the appropriate classification.
No Mathlib matching theorem was checked; unknown coverage is retained.

### Relevance, exclusions and discriminating test

The main gap remains uniform twelve-row compatibility. A positive result
could supply two projective factor coordinates for a later, separately
assessed simultaneous-row test. No solving bound follows from this
review. L153's rank census and passed L155 audit are reused; repeating
either without a defect is stopped by ATTEMPTS/048–049. Step 481 already
distinguished Sottile's three-space transversal union and generic
fourth-space counts; no new Sottile source read or such import is needed.

Continue only if the local proof handles ambient exhaustion and both
zero-rank possibilities over every E/F_97. A concrete unmatched plane,
rank-zero branch or failed embedding identification requires preserving
that obstruction and narrowing or abandoning this exact identification.
Do not repair a failure with genericity, rational descent, a preferred
pair, a relabeled kernel or an unstated gate. No full compatibility solver
is authorized by this scope.

All coding and chart qualifications in the retained proposal persist.
The rank conclusion, if later proved, concerns only the two selected
rows; it cannot remove rank tests for additional rows, lambda/full-weight
conditions or the original finite-event chart. C152a/L086/L152 and L154
remain prospective downstream uses, not premises proving this locus.
Representation, source-definition equivalence and wider radii remain
independent unresolved gaps.

Outcome: EXPLORATION. The changed target now has complete source coverage
and a bounded mathematical continuation; no new local theorem, exclusion
or progress beyond the inspected general geometry is claimed. Literature
does not spend or reset the mathematical exploration counter.
