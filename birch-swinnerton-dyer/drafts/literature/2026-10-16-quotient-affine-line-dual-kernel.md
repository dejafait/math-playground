# Quotient family and affine-line algebra — source comparison

TARGET: Establish the Galois-equivariant identification of L071's nonzero dual-kernel family over L070's direction field with all affine lines in E[7] missing zero, retaining the cyclotomic twist.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected Section 7 incidence and quotient assessments; checked L070/L071 and ATTEMPTS/035--036 for duplicates and limits; searched elliptic curve "affine lines" "dual isogeny", elliptic p descent "quotient" "affine lines", and primary dual-kernel/Weil-pairing terminology. Inspected the precise sources below; search snippets and secondary hits are not premises and no novelty is inferred.
SOURCE_EVIDENCE: Sutherland, MIT 18.783 Fall 2025, Lecture 6 Theorem 6.7 and prime-degree Case 1, pp.3--4, Lemma 6.10 p.5; Lecture 23 Warning 23.21 and Theorem 23.23, pp.10--11, through the bilinear/alternating/nondegenerate/Galois proof cases; Milne, Abelian Varieties v2.0 (2008), Chapter I Theorem 9.1 and prime-to-characteristic explanation, printed p.41; Schaefer--Stoll author long version 2001-06-13 Lemma 7.5 and surrounding Lemma 7.6 statement, printed p.16, reusing Proposition 7.10 p.19; Stacks Lemma 58.2.2 tag 03QR and orbit/stabilizer proof. Direct URLs and source qualifications are below.
COMPARISON: The primary sources cover dual-isogeny existence over the base field, its torsion-image kernel, Cartier rather than ordinary duality, the affine-line/ordinary-dual Galois set and finite-etale realization. L070/L071 meet the characteristic, full-direction and separable-quotient hypotheses. The remaining difference is the explicit whole-family applicability argument, including zero exclusion and conventions; no new general duality theorem is needed or approved for reproof.
GAP: Write and check the fixed family identification, its inverse, compatibility between all direction embeddings and the ordinary-dual labeling, and the precise cyclotomic/scalar conventions. No such identification, dual-kernel presentation, coordinate transport, incidence map or norm is established in this source-only step.
REASON: Previously missing essential dual-isogeny and Cartier-dual coverage is now read. A separate RESEARCH / REPRODUCTION specialization of the unchanged TARGET is justified, subject to the discriminating tests below; this turn derives no new result and edits no lemma or mathematical script.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED: the earlier quotient and incidence assessments explicitly excluded this dual-kernel family comparison.
SCOPE: Only the unchanged TARGET for audited L067/L068/L070/L071 on the fixed conductor-389 curve at seven, with raw short models, the full direction field and both coordinate transports; excludes producing an explicit kernel polynomial, incidence/norm, arithmetic descent or a Selmer/rank conclusion.

## Relevance, inputs and prior failures

The main gap is rank E(Q)=m(E) for arbitrary E/Q with m(E)>=2. The
intermediate target is the exact TARGET above. A correctly identified
affine-line algebra could guide a later finite presentation for L066,
replacing the stopped column mechanisms. This gives a plausible use,
not an arithmetic descent or a route completing BSD.

Audited L067/L068 give the whole torsion set and geometric scalar maps.
L070 identifies all eight directions, with the complete h/cubic, mixed
inverse and both coordinate transports. L071 supplies the separable
degree-seven quotient over that entire characteristic-zero field with
the specified subgroup as kernel. Its conclusion explicitly excludes the
present identification; no existing local result was found proving it.
The exact coefficients need no new inspection or computation for this
theorem-level comparison. No residual surjectivity, rational subgroup
generator or root of unity is granted. No cross-notebook input is used.

ATTEMPTS/035--036 stop two particular full-column presentations. This
comparison uses the completed direction-field quotient, not their partial
columns. L069 and all unfinished translation evidence remain excluded.
The ready Section 7 assessment is reused from
`drafts/literature/2026-10-16-conductor389-seven-incidence-maps.md`;
the quotient comparison is reused from
`drafts/literature/2026-10-16-conductor389-direction-velu-quotient.md`.

## Primary theorem coverage

[Sutherland, Lecture 6](https://math.mit.edu/classes/18.783/2025/LectureNotes6.pdf),
Theorem 6.7, printed pp.3--4, gives the unique base-field dual satisfying
hat(alpha) alpha=[deg alpha]. Its prime-degree Case 1 explicitly constructs
the dual from alpha(E[ell]) when ell differs from the characteristic.
Lemma 6.10 p.5 gives the reverse composition. The inspected Case 1 is the
relevant case: D has characteristic zero and L071 has degree seven.
No inseparable case or new duality proof is required. The remaining
family applicability must be written separately.

[Milne, Abelian Varieties v2.0](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Chapter I Theorem 9.1, printed p.41 (PDF page 47), identifies the kernel
of the dual abelian-variety isogeny with the Cartier dual of the kernel.
The following paragraph describes its geometric points as
Hom(N,mu_n) with the induced Galois action for order prime to the
characteristic. It does not replace mu_n by a trivial module.
For elliptic curves this comparison uses the canonical principal
polarizations; Sutherland's elliptic dual is the intended convention.
The prime-to-characteristic hypothesis applies here. A generator-based
ordinary dual description would require recording the cyclotomic action.

Version precision matters: the inspected PDF is the 2008 v2.0 notes,
whose title page says March 16 and version history March 17. Its result
is Theorem 9.1, not Theorem 11.1. The latter numbering is an uninspected
1986 article lead: direct retrieval of `math/articles/1986b.pdf` returned
an internal error, and its search excerpt is not used. The notes' proof
reference is Mumford (1970) section 15 p.143 over an algebraically closed
field and Oort (1966) in general; these references were not read. The
named theorem itself and its induced-action explanation were read in full;
no new reproof or stronger assertion about these references is used.

[Sutherland, Lecture 23](https://math.mit.edu/classes/18.783/2025/LectureNotes23.pdf),
Warning 23.21 and Theorem 23.23, printed pp.10--11, provide the alternating,
nondegenerate, bilinear, Galois-equivariant pairing with values in mu_n
for n prime to the characteristic. Its relevant proof cases were read,
including the nondegeneracy argument and coefficientwise Galois action.
The warning distinguishes the two inverse pairing conventions. This
supports checking the twist without assuming mu_7 is constant over D.
The next proof must specify its argument order and action convention.

[Schaefer--Stoll, author long version, 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Lemma 7.5, printed p.16, labels lines by the level-one sets of nonzero
ordinary linear functionals on E[p]. The surrounding text defines B by
that Galois set, of degree p^2-1. Lemma 7.6's following statement keeps
the mu_p tensor factor, and its discussion distinguishes Hom(E[p],mu_p).
Proposition 7.10 p.19, already assessed, supplies the downstream norm
construction only after the incidence algebra exists. No part of that
norm construction is an input establishing the present identification.

[Stacks Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR)
is the field-etale-scheme/Galois-set equivalence. Its proof retains every
orbit via its open stabilizer and fixed separable field. It licenses
algebra realization after an equivariant bijection is proved; a matching
geometric cardinality alone is insufficient. Restricting to the finite
sets here retains all factors. No assertion of fieldness for the future
affine-line algebra is approved.

## Separate specialization obligations and test

SPECIALIZE permits the explicit applicability proof for the fixed family,
not a general reproof of the imported theorems. The next research turn
must define the family over Spec(D), viewed over Q by its structure
morphism, and distinguish its total finite set from a Weil restriction.
It must account for every direction embedding, and transport the quotient
and its dual compatibly under Galois. A single selected embedding is
insufficient. Raw short coordinates suffice; minimal models and periods
are irrelevant to this finite-set target.

The discriminating test is a complete forward and inverse correspondence
between nonzero dual-kernel points and nonzero torsion cosets for each
direction, then the source's affine-line labeling, with the Galois action
checked throughout. The proof must remove the identity in every fiber,
exclude precisely the lines through zero and account for all 48 intended
geometric elements. It must distinguish the group structure in each
dual kernel from a mere bijection to level-one ordinary-dual labels.
In particular it must determine the scalar convention rather than copy
L068's forward indexing to the line labels without justification.

Retaining the twist means stating the Cartier-dual/Weil-pairing
identification with its mu_7 factor and distinguishing it from the
ordinary F_7-dual description. It does not authorize adding an unexplained
twist to the raw L071 quotient family. No root-of-unity trivialization,
rational generator or full residual-image assertion may enter the proof.
These are obligations for the separate attempt, not results proved here.

Continue if the whole-family bijection, inverse, zero exclusion and action
conventions pass that test. Otherwise record the precise obstruction or
only the narrower supported statement, preserving the original target
and old cost stops. Do not start a new kernel-polynomial implementation
under this assessment. Full matching Mathlib coverage is not checked;
unknown availability is not absence.

Complete global power classes, functions, local identifications/bounds,
Selmer containment, other L026 premises, successful localization, rational
membership, divisible Sha and arbitrary-curve comparison remain unresolved.
This source import supplies essential coverage, not the fixed-family
identification or new mathematics beyond the sources. The newly ready
assessment receives the supervisor's separate approval before research.
