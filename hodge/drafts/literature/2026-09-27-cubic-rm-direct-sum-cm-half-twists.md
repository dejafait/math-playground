# Arbitrary CM actions on direct sums of the cubic RM structure — assessment

TARGET: Test whether any finite direct sum T(S)^{oplus m} admits an effective polarized weight-one half twist under any Hodge-compatible CM field action through M_m(E).
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched half twists with real multiplication, isotypic direct sums, arbitrary matrix actions, CM fields and multiplicities; compared the primary effectivity criterion with weak-CM and minimal-level formulations. Queries, versions and inspected sections are recorded below; no exact all-multiplicity statement was identified.
SOURCE_EVIDENCE: van Geemen, arXiv:math/0008076v1, sections 1.2--1.4, 2.3--2.5, Proposition 2.8 and sections 2.10--2.11, https://sites.unimi.it/vangeemen/0008076.pdf#page=2; van Geemen--Izadi, arXiv:math/0008170v1, sections 1.3--1.6, https://sites.unimi.it/vangeemen/halfhyper.pdf#page=3; Keast--Kerr, SIGMA 14 (2018), 116, Remark 2.9 and equations (4.1)--(4.2), https://sigma-journal.com/2018/116/sigma18-116.pdf#page=7; further comparisons below.
COMPARISON: The known criterion allows any Hodge-compatible CM action and arbitrary top-piece dimension; the tensor-product construction also supplies polarizability when the effective half twist exists. Neither L035 nor the inspected representation statements evaluate every CM embedding into M_m(E) on the inherited top piece.
GAP: Determine the top-piece embedding support for an arbitrary unital CM field action through M_m(E), including fields not containing E, and compare it with every CM type. The matrix-action specialization and its universal conclusion remain unproved here.
REASON: Import the general criterion and polarization result; perform only the remaining support calculation in a separate research turn. This uniform test can decide whether changing the action rescues a linear auxiliary construction without repeating the fixed scalar-extension calculation.

## Hypotheses

Keep T=T(S), End_Hdg(T)=E totally real cubic, dim_E T=6,
and the inherited polarized weight-two Hodge structure on every
finite direct sum W=T^{oplus m}. Retain the very-general cubic
RM data and Hodge numbers of T from the existing family audit.
Allow any m>=1 and any unital embedding of a CM field into
M_m(E)=End_Hdg(T^{oplus m}), with every CM type considered.
No inclusion of E in that CM field is required. Ask for the
whole direct sum to have an effective polarized half twist,
with only types (1,0) and (0,1). The product polarization is
available on W; compatibility of a particular matrix action
with its adjoint is not an extra hypothesis of the target.

The universal target remains rational cycle-class surjectivity
for every smooth projective complex variety. Deligne's
[Clay statement, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2)
was reread on 2026-09-27 and agrees with the existing target audit.
The present review concerns only this auxiliary construction.

## Conclusion

The saved target is screened as SPECIALIZE. No inspected source
states the complete answer with these matrix-action quantifiers.
Known results supply the test and its polarization consequence;
the remaining application is expected to be REPRODUCTION.
No new result or originality claim is made in this literature turn.
The initial REVIEW_REQUIRED record's scope is preserved.

L035 settles the fixed multiplication action on T tensor_E E(i).
It does not settle the present target merely because that
underlying Hodge structure is a direct sum. The previous scalar
assessment is reused for this overlap; the broader source
comparison below supplies this target's separate review.

## Proof

This section gives named source statements and scope comparisons.
It does not calculate the support of any new action or prove a
uniform existence or nonexistence theorem.

### General half-twist criterion

Read van Geemen, *Half twists of Hodge structures of CM-type*,
[arXiv:math/0008076v1, 10 August 2000, sections 1.2--1.4, p. 2, and 2.3--2.5, pp. 3--4](https://sites.unimi.it/vangeemen/0008076.pdf#page=2).
His CM terminology requires a field action preserving the Hodge
decomposition; it does not require a commutative Hodge group or
a one-dimensional top piece. For a CM type Sigma, the positive
half twist is effective exactly when the top piece has zero
support at embeddings outside Sigma.

Read also [Proposition 2.8, pp. 4--5, and sections 2.10--2.11, p. 6](https://sites.unimi.it/vangeemen/0008076.pdf#page=4).
When the positive half twist exists, Proposition 2.8 embeds its
Tate twist in W tensor_Q K_{-1/2}. Section 2.11 obtains a
polarization by restricting the tensor-product polarization.
Its alternative explicit formula uses an adjoint-compatible
polarization. The first construction avoids imposing that extra
condition on the target's chosen product polarization.

These are supporting general results. Their application still
needs the actual top-piece support for each allowed action;
equal multiplicities on an entire rational representation do
not by themselves compute its top Hodge piece.

### Independent sign convention and geometric hypotheses

Read van Geemen--Izadi, *Half twists and the cohomology of
hypersurfaces*, [arXiv:math/0008170v1, 22 August 2000, sections 1.3--1.6, pp. 3--4](https://sites.unimi.it/vangeemen/halfhyper.pdf#page=3).
Their plus subspace uses Sigma, and their minus subspace uses
the conjugate embeddings. Section 1.5 states the condition
W_-^{k,0}=0 and warns that omitting the forbidden complex
pieces does not generally give a rational subspace. Proposition
1.6 gives the same conditional Hodge inclusion. This resolves
overbars lost in text extraction of the first source.

Section 2.1, pp. 4--5, instead starts with a cyclic cover and
its geometric automorphism. Its cyclotomic action on the chosen
primitive cohomology is specified by that geometry. It is not
a theorem about all actions on the inherited direct sum here.
The earlier assessment of its geometric examples is retained.

### Weak CM and representation-level bounds

Read Friedman--Laza, *Semi-algebraic horizontal subvarieties of
Calabi--Yau type*, [arXiv:1109.5632v1, 26 September 2011, Convention 2.5, Definition 2.7 and equation (2.8), pp. 7--8](https://arxiv.org/pdf/1109.5632v1#page=7),
and [Theorem 3.1, Corollary 3.3 and Remark 3.5, pp. 18--20](https://arxiv.org/pdf/1109.5632v1#page=18).
The shift defined in (2.8) explicitly permits non-effective
Hodge structures. Thus weak CM alone is not an assertion of an
effective weight-one realization. The endomorphism-field and
real/complex classifications in the inspected statements retain
simplicity, Calabi--Yau type or real irreducibility hypotheses.
They do not directly classify the arbitrary matrix actions in
the saved target. No claim about those actions is deduced from
the real/complex terminology alone.

Read Keast--Kerr, *Normal Functions over Locally Symmetric
Varieties*, [SIGMA 14 (2018), 116, section 2.2, pp. 5--7, especially Remark 2.9 and (2.4)](https://sigma-journal.com/2018/116/sigma18-116.pdf#page=7),
and [section 4, equations (4.1)--(4.2), p. 15](https://sigma-journal.com/2018/116/sigma18-116.pdf#page=15).
Remark 2.9 identifies the minimal level attainable by half
twists of the specified complex representation. Section 4
treats a conjugate pair, including the real case, with opposite
grading shifts and gives its level. This is a weight-preserving
variant, rather than the positive weight-lowering convention
used in the target. The formulas offer a supporting obstruction
framework, but a comparison still needs the decomposition of
every allowed rational CM action and the inherited Hodge grading.
No such decomposition or numerical level bound for W is computed
here. Their normal-function conclusions are not imported as
algebraicity or nonalgebraicity of the cubic cycle.

### A related construction with an original CM field

Reused the earlier comparison and reread Moonen, *On the Tate
and Mumford--Tate conjectures in codimension one for varieties
with h^{2,0}=1*, [section 7.1 and (7.1.1), p. 28 of the 45-page author PDF](https://www.math.ru.nl/~bmoonen/Papers/TMTCC1.pdf#page=28),
accessed 2026-09-27. This section assumes a CM endomorphism
field for the original variation. It constructs a polarized
abelian scheme and an E-linear Hom realization using a CM type
chosen with respect to the unique top-piece embedding. Those
hypotheses differ from the matrix algebra of copies of a fixed
totally real structure. The statement supplies neither the
required support comparison nor algebraic comparison cycles
for this target.

### Search record and access limits

Discovery queries on 2026-09-27 included:

- `"half twists" "real multiplication" direct sum`
- `"half twist" "totally real" "endomorphism"`
- `"Hodge" "half twist" "direct sum" "real"`
- `"Hodge" "half twists" "totally real" obstruction`
- `"Hodge" "half twist" "matrix" CM field`
- `"Hodge" "half twist" "copies"`
- `"Hodge" "half twist" "M_m"`
- `"half twist" "isotypic" Hodge -braid -Heisenberg`
- `"half twist" "real" "multiplicities" Hodge`

Title/author searches located the Friedman--Laza and Keast--Kerr
primary texts. Several exact queries returned unrelated braid
half twists; those hits supply no mathematical evidence. The
bounded search identified the general criteria and nearby
representation formulations above, without a full match for
the uniform target. This does not establish novelty.

The J-STAGE published van Geemen PDF was identified, but follow-up
page retrieval failed in this turn. The author-hosted v1 was
read directly, so its section numbers and PDF pages are the
citations used here. The companion paper fixes the conjugation
notation independently. No essential source remains unread.
References to Lang, DMOS and Green--Griffiths--Kerr were not
independently inspected; no additional theorem from them is an
input. Search snippets, later mirrors and the broader theorems
in the compared papers are not counted as read statements.

### Relevance, redundancy and discriminating test

The missing input is an algebraic realization of the cubic
action beyond the Dickson locus. A successful action would
identify a different auxiliary abelian candidate; algebraic
inclusion and retraction cycles involving S would remain a
separate gap. Hodge inclusions alone do not supply those cycles.
A uniform negative theorem would close this class of linear
auxiliary constructions and direct the search to different
representations or geometric cycle constructions.

L035 already gives forbidden dimension one against zero required
for its fixed scalar action. The present question retains that
failure while allowing different fields, embeddings and
multiplicities. L032--L034 concern Clifford/Prym representations
and specified transfers; they do not answer this support question.
No stopped geometric representative is reopened by this review.

The later specialization should identify the K-action induced
on W^{2,0} for an arbitrary embedding into M_m(E), using the
distinguished real embedding of E and retaining all multiplicities.
It must justify any relation between conjugate embedding
supports on that piece, rather than assuming the scalar-extension
answer. Fields not containing E and actions mixing copies must
remain in scope. No classification of all field embeddings is
needed unless the support argument actually requires it.

Continue if an admissible action and CM type meet the exact
zero-forbidden-support threshold; use the cited polarization
construction before considering an abelian realization. Stop
this entire direct-sum recipe if a uniform argument forces a
nonzero forbidden part for every admissible action and type.
Testing a few matrices cannot decide the universal quantifiers.
No new support multiplicity, half twist or exclusion is asserted
in this assessment.

The scalar recipe's negative result ends the preceding bounded
window. This completed review is the first consecutive exploration
turn since that result; it authorizes a separate bounded
specialization and does not reset the allowance through a new
route name. PROGRESS.md holds the sole current checkpoint and
exact unchanged action.

The achieved span stays 21 and the attained RM directions stay
three against four required. Algebraic beta_U and the separate
Kuga--Satake correspondence kappa remain missing, as do arbitrary
primitive fourfold classes and the higher-dimensional cases.
There is no complete informal candidate.

## Mathlib

Coverage: **not checked** for this uniform statement or its
supporting half-twist and representation theory. No library match
or absence is asserted. The named citations above are supporting
mathematical results, with their scope distinguished from a match
for the complete saved target.
