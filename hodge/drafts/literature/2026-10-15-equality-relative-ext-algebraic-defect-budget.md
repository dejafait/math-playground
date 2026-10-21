# Equality relative Ext — algebraic extension and defect budget

TARGET: Construct the algebraic reflexive extension of the stable relative-Ext splitting and determine its Chern-class correction budget at Z for the (14,21) equality family.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The parent extension review searched relative Ext, rank jumps and surface reflexive extension; compared L068's everywhere-stable calculation, L066's derived-fibre warning and ATTEMPTS/063/065. No source was identified computing this actual conditional equality-family extension or its defects; no novelty is inferred.
SOURCE_EVIDENCE: Reuse Huybrechts--Lehn E31 (1997) Section 10.1.8/Example 10.1.9 and Theorem 10.2.1 with its descent proof from the ready tangent assessment; Stacks 0B91/0BDH, 0EBJ/0B3N statements and short proofs were inspected in the parent review; reuse Fulton Theorem 15.2 and Stacks 02UM/02UO for signed GRR and additive Chern characters.
COMPARISON: Known results cover perfect pushforward, stable-open natural tangent/KS and trace pairing, algebraic reflexive extension on a smooth surface and GRR. The identified difference is an actual algebraic splitting and an honest correction budget allowing every point-supported sheaf, not an automatic equality between a virtual index and a bundle character.
GAP: Establish algebraicity and nondegeneracy of the stable-open tangent summand, extend that actual splitting, and track ordinary higher-image, torsion and double-dual defects with correct signs; no numerical defect length, global semistability or Chern contradiction is supplied by the sources or this review.
REASON: This narrower target is independently testable without the parked codimension-two metric extension. Import the covered tools and derive only the conditional family-specific splitting and correction identities; stop if no actual splitting or constraint beyond a virtual character is justified.
SCOPE: Conditional L071/L097 (14,21) family on the smooth algebraic K3 base B, U=B minus finite possibly empty Z, audited L095 actual tangent pairing and audited L100 stable-open geodesy. Algebraic relative Ext, trace/Serre pairing, KS, reflexive extension and exact Chern bookkeeping only. No metric extension, global HE connection, semistability, universal sheaf, image normality, F existence or transport.

This is a newly written ready continuation, subject to separate approval
next turn. No algebraic splitting, defect identity or numerical character
has been derived or approved mathematically in this literature turn.

The main gap is primitive rational Hodge realization. The intermediate
target would replace an uncontrolled virtual index by an actual global
bundle decomposition and a precise list of point-supported correction
terms. Its plausible use is to decide what local defect bound or separate
stability theorem a future Chern obstruction would actually need. It may
also end this sheaf mechanism as compatible. Common-kernel existence,
transport and universal algebraicity remain independent gaps.

Use p:S_1 x B -> B and the actual locally free coefficient End_0(F).
Do not posit single-degree concentration on B. Distinguish the ordinary
sheaves R^i p_*End_0(F), their derived fibres, torsion in the middle
sheaf, and the quotient of its reflexive hull by its torsion-free part.
Any correction asserted finite
must be proved supported in Z. Record all lengths as unknown unless an
actual local calculation proves them. A point's derived-fibre dimension
does not determine a sheaf's length. Treat Z empty explicitly.

On U construct the splitting with algebraic KS and the relative
trace/Serre alternating pairing, checking its pullback against L095's
nonzero actual family form. L100 gives a geometric comparison, not a
license to apply projective GAGA directly to arbitrary analytic maps on
U. If the orthogonal projector is used, verify its algebraicity from
these algebraic data before invoking extension. Do not assume an
algebraic splitting merely because the L2 splitting is holomorphic.

Import [Stacks 0EBJ](https://stacks.math.columbia.edu/tag/0EBJ),
with depth at least two on the complement, and
[0B3N](https://stacks.math.columbia.edu/tag/0B3N), for a regular scheme
of dimension at most two. These extend algebraic reflexive objects and
morphisms, not metrics. The base is smooth and projective and Z is
finite, so check these ambient hypotheses locally. Import
[0B91](https://stacks.math.columbia.edu/tag/0B91) and
[36.31.3 in 0BDH](https://stacks.math.columbia.edu/tag/0BDH) for the
proper flat perfect-complex and stable-open concentration tools.

Reuse the complete primary-source inspection in
[the L068 assessment](2026-10-07-charge-seven-parallel-tangent-index.md),
especially the stable tangent descent/KS and GRR passages. The actual
coefficient family avoids needing a universal sheaf on the coarse
space. Scalar conjugation and base-line twists must still cancel in
the natural relative-Ext identification. Import the cited Fulton
*Intersection Theory*, second edition, Theorem 15.2, pp. 286--287,
and Chern-character additivity from
[Stacks 02UM](https://stacks.math.columbia.edu/tag/02UM).
Retain L071's full integral tensor, forced higher characters and full
mixed square. Use the alternating pushforward sign before passing to
ordinary cohomology sheaves. L068's numerical characters are not inputs.

Continue only if an actual algebraic extension/splitting is established
and every term between its character and the virtual GRR class is
accounted for. A useful result may retain explicit unknown lengths and
must state exactly what their signs do and do not bound. Abandon any
claim of obstruction requiring omitted defects or unproved stability;
do not fill it with the parked metric theorem. Exact local multiplicities
or an admissibility proof are outside this assessment and require their
own review. Full matching Mathlib coverage is not checked.
