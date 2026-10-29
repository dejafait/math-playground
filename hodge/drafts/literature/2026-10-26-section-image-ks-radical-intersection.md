# Actual section image and KS radical — source coverage ready

TARGET: Test whether L171 forces the actual section image to meet L170's KS radical trivially, and determine the resulting conditional isotropy threshold.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 572 searched the exact section/KS/radical terminology and direct-summand evaluation tools, compared targeted L108/L116/L164/L170/L171 passages and histories 565/567/569/571 with ATTEMPTS/092–094, and reused the step 564/566/568 primary assessments. Exact queries and limitations appear below; no novelty claim.
SOURCE_EVIDENCE: Reused inspected step 566/568 evidence for the unchanged conditional maps; read live Stacks Definition 6.26.1 and Lemmas 6.26.2/4 (0094), Lemma 26.7.2 (01I8), Lemma 10.12.8 (00DE) and proofs, and Conrad, Bilinear Forms, Theorem 3.12 and proof, pp. 18–19, author-hosted 63-page version.
COMPARISON: Standard pullback/tensor functoriality and orthogonal dimension identities cover the general tools. L116/L164 already supply the full section summand and evaluation, L170 supplies the conditional quotient inequality, and audited L171 supplies the actual KS comparison; no inspected source directly states their family-specific section-intersection conclusion.
GAP: A later mathematical step must compare the actual section evaluation with the fixed normal summand, carry the split inclusions to ordinary fibres, and use the same injective e_z and actual KS plane before applying L170. No essential source gap remains; this review establishes neither intersection vanishing nor an improved threshold.
REASON: Approve exactly TARGET for one subsequent RESEARCH / REPRODUCTION specialization, importing the general tools rather than reproving them. This literature-only step changes no lemma, script, argument or DAG.
SCOPE: The conditional family and actual maps listed below; finite direct-sum pullback, full-section evaluation and L170's isotropic quotient inequality only, with general s,t and no section integrability or F existence.
LITERATURE_REASON: The changed exact section-intersection target was REVIEW_REQUIRED; prior ready assessments covered the KS identity and quotient inequality separately, leaving their section-evaluation applicability unassessed.

The main gap is primitive realization and existence of F. The proposed
intermediate target is control of the actual intersection appearing in
L170's conditional section inequality. A possible downstream use is a
sharper conditional nonvanishing test for the point bracket. The desired
threshold is 24 under total isotropy, compared with 26 without further
intersection control; neither threshold is an unconditional bound on F.

Essential inputs are L108, L111, L116, L164, L170 and audited L171;
retain L071 and L094/L095/L109/L115 through their conditional hypotheses.
No cross-notebook input. Keep the identical marked K3 factors, common
metric, real Kähler class, ordered triple, forms and actual connection.
F is hypothetical, locally free, rank two and product-polystable, with
integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P. Use the finite reduced
split set, general s,t, actual splitting M=i(T_B) direct sum N, full
section space H=H^0(B,M), actual e_z and actual KS plane. Empty split
support is vacuous. No ordinary middle-base-change isomorphism, generic
section position, arbitrary section integrability, multiplicative
splitting, endpoint or F existence is assumed.

After source approval, continue if the actual summand and section
evaluation maps settle the intersection and permit the precise
conditional threshold; otherwise identify the missing compatibility
and retain the established inequality. Stop at the unknown actual
bracket values: a nonzero obstruction for some first-order section
would not contradict F's existence. ATTEMPTS/092–094 remain intact.
Actual quadrics, complementary operation, minimum square length,
transport and global primitive realization remain independent gaps.

The invocation-start proposal was REVIEW_REQUIRED. The separate step
572 comparison below approves the bounded mathematical attempt; it
does not carry it out. Full matching Mathlib coverage is unchecked,
with no absence claimed.

## Completed source comparison — step 572

2026-10-26. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. Source readiness is local process progress,
not a mathematical advance beyond the sources checked.

### Inspected primary tools and applicability

Live Stacks [Section 6.26, 0094](https://stacks.math.columbia.edu/tag/0094),
Definition 6.26.1 and Lemmas 6.26.2/4 with their proofs, define
module pullback by tensor product, give its adjunction, and identify
its stalks by scalar extension. These apply to the point morphism
Spec C -> B without flatness. They cover ordinary residue fibres;
they do not identify ordinary R^1 base change with E_z.
The tensor/Hom adjunction in [Lemma 10.12.8, 00DE](https://stacks.math.columbia.edu/tag/00DE)
was read with its bilinear-map proof; it applies to arbitrary modules
over a commutative ring. These are standard tools for transporting
finite split-summand maps under pullback, without asserting left
exactness on an arbitrary nonsplit sequence.

[Stacks Lemma 26.7.2, 01I8](https://stacks.math.columbia.edu/tag/01I8),
parts (1)–(3) and its three proofs, was inspected. Over Spec R it
identifies sheafified tensor constructions, and internal Hom when
the first module is finitely presented. It supports working in a
local affine trivialization of the bundles. It gives no global
section-generation theorem or position statement about these sections.

Keith Conrad, *Bilinear Forms*, author-hosted 63-page text,
[Theorem 3.12 and proof, pp. 18–19](https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf#page=18),
was reinspected: finite-dimensional symmetric or alternating spaces
have the stated nondegeneracy/orthogonal-sum equivalence; in a
nondegenerate ambient space complementary dimensions and the double
orthogonal identity hold. The proof uses the map to the subspace
dual. Reuse the arbitrary-field restricted-radical coverage from
Munemasa Section 1/Proposition 1.1, pp. 3–4, recorded in the step
566 assessment. Over C these tools have the needed scope; no
finite-field theorem, positivity or real signature argument is used.
L170 already performs the quotient specialization; the next attempt
must cite its inequality, not repeat its radical proof.

The unchanged geometric input coverage is reused from
`2026-10-26-split-ks-extended-tangent-comparison.md` and
`2026-10-26-ordinary-middle-radical-critical-audit.md`, both read this
turn. Huybrechts–Lehn E31 (1997), 10.1.5/7/8 and Example 10.1.9,
pp. 218–221, and Kuhn (2024), Lemma 4.4/Claim 4.5, Corollaries
4.6–4.7 and Lemmas 6.11–6.12, are retained through audited L171.
Their all-family scope includes nonsimple fibres. Stacks 0B91 and
the recorded cup compatibility remain through L164. This target
changes no coefficient, base square, KS convention or analytic
bridge, so further Atiyah, slice or Kuranishi browsing is unnecessary.

### Exact comparison, searches and preserved failures

Read L170 in full, L171's hypotheses/conclusion and actual sheaf-map
comparison, L108's fixed splitting construction, L116's section
decomposition (8) and its real-Kahler qualifications, and L164's
section-evaluation argument and separate audit. L116 retains
M=i(T_B) direct sum N with N=O_B^t direct sum A and H^0(A)=0;
L164 explicitly uses H^0(T_B)=0 and evaluation of the full section
space at every point, followed by the actual e_z. L171 compares
that same i with kappa_z. These are already canonical statements,
not new results established by this review. The exact task is to
check their combination, including the position of the evaluation
map relative to the fixed summands, before using L170's inequality.

Queries on 2026-10-26: `"Kodaira Spencer" "global sections"
"direct summand" K3`; `"K3" "section" "Kodaira-Spencer" "radical"`;
`"isotropic subspace" "radical" quotient dimension bilinear form`;
`site.stacks.math.columbia.edu pullback modules direct sums tensor
product stalks`; `site.stacks.math.columbia.edu "tensor product"
"direct sums" "10.12"`. No matching geometric theorem was identified.
Search hits on other moduli problems and orthogonal orbit geometry
were leads only, not imported results. A failed Stacks HTML-book
URL did not block the individual primary tags above. Search snippets
and the exercise-only Stacks 111.4 hit are not theorem evidence.
No unread lead is essential to this bounded specialization; failure
to find an exact statement does not establish novelty.

The scoped local search for section/radical intersections and a
24 threshold finds the pending target and earlier stated boundaries,
not a completed proof of this conclusion. ATTEMPTS/092 parks actual
section-pairing vanishing, /093 parks scalar-isotropy-only exclusion,
and /094 parks cyclicity-only complementary vanishing. Their full
failure paragraphs were read. The present target tests a section
position comparison; it does not supply bracket values, extend
arbitrary sections, or reopen those exhausted arguments.

### Approved continuation boundary

Perform exactly TARGET once with the inputs and assumptions above.
Check the actual ordinary-fibre summand and evaluation maps before
passing through e_z; retain the full derived target and L171's
actual identification. Only then determine what L170's conditional
inequality says. Continue if these maps settle the intersection;
otherwise name the failed compatibility and retain the existing
inequality and threshold 26. The sought conditional threshold 24
is a test, not an established conclusion of this literature turn.
Empty Z and t=0 remain vacuous. No new proof, lemma or certificate
was produced, and PROOF.md and DAG.md are unchanged.
