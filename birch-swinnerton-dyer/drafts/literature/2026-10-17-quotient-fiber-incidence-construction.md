# Quotient-fiber incidence construction — source comparison complete

TARGET: Construct and independently verify the full seven-incidence algebra and both projection pullbacks via L071's quotient fibers over L073.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready 2026-10-16 seven-incidence, quotient-family and explicit-dual assessments; searched exact incidence/isogeny-fiber terminology and stronger explicit-descent leads; read ATTEMPTS/035--038 and scoped L071/L072/L073 passages. Queries, inspected sources and unread leads are distinguished below; no fixed complete certificate was located and no novelty is inferred.
SOURCE_EVIDENCE: Schaefer--Stoll author long version 2001-06-13 Lemma 7.5/definition of B p.16 and Proposition 7.10 with its full construction/matrix paragraph p.19; Sutherland Fall 2025 Lecture 5 Theorem 5.8 with generic-fiber proof pp.3--4 and Theorem 5.11 with quotient/coset proof sketch pp.5--6; Lecture 6 Theorem 6.7 prime-degree Case 1 pp.3--4; Stacks 26.17.1--3/26.17.7 (01JO), 58.2.2 (03QR), 10.144.1--2 (00UB/00UC), 59.26.2 (03PA) and 29.49.1--4 (02K9), statements and available relevant proofs read directly.
COMPARISON: Known quotient fibers, the audited L072 correspondence and finite-etale algebra constructions cover the geometric mechanism; the remaining specialization is a complete fixed arithmetic presentation and replay, including every specialized fiber and both pullbacks. The generic-fiber polynomial argument alone does not certify those specializations. This is known-method reproduction, not a new incidence theorem.
GAP: The rank-seven algebra over the entire rank-48 affine-line algebra, all unit/separability witnesses, both coordinate pullbacks and complete independent replay remain unconstructed. Source coverage is sufficient for one bounded attempt; no incidence or norm certificate is established by this review.
REASON: The changed mechanism uses inverse images under the completed quotient, avoiding the stopped translation-column constructions; primary coverage and its exceptional-case limits have now been compared. SPECIALIZE permits the fixed applicability argument and certificate construction only after separate supervisor approval of this newly ready continuation.
LITERATURE_REASON: The invocation-start quotient-fiber target was REVIEW_REQUIRED: its changed representation and essential primary generic-versus-specialized fiber cases had not been assessed. Existing general incidence coverage was reused rather than refreshed without cause.
SCOPE: Exact TARGET only, fixed conductor-389 curve at seven; audited L067/L068/L070/L071/L072/L073, full direction field and affine-line algebra, all incidence fibers, both projection pullbacks, complete basis and independent replay. Excludes norm construction, descent arithmetic, selected factors, L069 and all unfinished translation columns.

## Relevance and source reuse

The main gap is rank E(Q)=m(E) for arbitrary E/Q with m(E)>=2.
The intermediate target is the entire incidence algebra with both maps.
Its plausible downstream use is a rank-seven multiplication representation
for Schaefer--Stoll's fiber norm, and eventually L066's conditional Selmer
enclosure. Functions, complete units/classes, local identifications and
upper bounds, full Selmer containment, other L026 premises, successful
localization, rational membership, divisible Sha and arbitrary-curve
complex-order comparison remain independent gaps.

Reuse `2026-10-16-conductor389-seven-incidence-maps.md` for the general
Section 7 construction, determinant norm and the unchanged software
comparison. Reuse `2026-10-16-quotient-affine-line-dual-kernel.md` and its
critical-audit assessment for Cartier duality and action conventions.
Reuse `2026-10-16-explicit-dual-kernel-algebra.md` for the completed dual
algorithm. The new sources below assess a different representation;
there is no reason to reprove general duality, quotient existence or norms.
A citation cannot supply the uncomputed rational presentation, full-domain
unit identities, map images and independent certificate replay.

## Primary theorem hypotheses and essential proof cases

[Schaefer--Stoll, How to do a p-descent on an elliptic curve](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
author long version dated 13 June 2001, uses an odd prime over a number
field. Numbering here is that version, not the shorter published article
(Trans. AMS 356 (2004), 1209--1231, DOI 10.1090/S0002-9947-03-03366-X).
Lemma 7.5 and the following definition of B, printed p.16, identify the
ordinary-dual level-one sets with affine lines missing zero. Proposition
7.10 and the preceding paragraph, p.19, define the incidence set, both
projections and pullbacks; its proof is pullback followed by the product
on the full line fiber. The following matrix paragraph requires a full
B-basis. These constructions apply at p=7 without assuming maximal
residual Galois image. The old assessment's cohomology comparison and
p=3-only chord-slope exclusion remain unchanged. No cohomology result
or norm implementation is added here.

[Sutherland, MIT 18.783 Fall 2025 Lecture 5](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf),
Theorem 5.8, pp.3--4, computes a separable kernel using a generic affine
fiber. Its proof excludes zero target coordinates, leading-term cancellation
and the finite derivative-exception set before counting roots of the
x-equation; the y-equation then determines the other coordinate. Thus its
polynomial calculation must not be quoted as a certificate for every
special dual-kernel point. Theorem 5.11 and its proof sketch, pp.5--6,
identify quotient fibers with subgroup cosets and give descent for a
stable subgroup, without requiring each member rational. The proof's
general quotient existence is a stated standard theorem, not a newly
verified construction here. These results justify the representation
choice; exact specialized unit and degree checks are still required.

[Sutherland, Lecture 6](https://math.mit.edu/classes/18.783/2025/LectureNotes6.pdf),
Theorem 6.7, prime-degree Case 1, pp.3--4, constructs the dual from the
image of prime torsion. The relevant hypothesis is degree seven prime
to characteristic zero. This is already specialized in audited L072,
with both composition orders checked in L073. Reuse those actual maps
and all-fiber transport, without constructing another dual or choosing
a root of unity. The remaining incidence argument must compare the
whole preimage with L072's specified line, not just its cardinality.

[Stacks 26.17, tag 01JO](https://stacks.math.columbia.edu/tag/01JO),
Definition 26.17.1, Lemmas 26.17.2--3 and Definition 26.17.7 supply
scheme-theoretic inverse image and affine tensor-product construction.
The inspected proofs use the universal property and restriction to open
charts. They do not authorize deleting a point where an affine formula
fails. Any use of the affine chart must certify that the whole desired
inverse image is there and that clearing denominators adds no component.

[Stacks 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR)
provides the etale-scheme/Galois-set equivalence. Its orbit/stabilizer
proof retains every separable field factor. It applies only after the
complete equivariant identification is checked, including the two maps.
Equal dimensions alone do not establish that identification.

[Stacks Definition 10.144.1, tag 00UB](https://stacks.math.columbia.edu/tag/00UB)
and [Lemma 10.144.2, tag 00UC](https://stacks.math.columbia.edu/tag/00UC)
cover a monic polynomial algebra with derivative invertible in the stated
localization; the lemma supplies etaleness and base-change stability.
Its proof is omitted there. [Proposition 59.26.2, tag 03PA](https://stacks.math.columbia.edu/tag/03PA)
records composition/base-change facts with references to their proofs.
These are cited results, not proofs claimed to have been supplied by
this review. A full derivative-unit certificate is an appropriate
specialized test; a generic discriminant observation is insufficient.
[Stacks 29.49.1--4, tag 02K9](https://stacks.math.columbia.edu/tag/02K9)
distinguishes finite locally free from finite flat in general. The
finite-presentation equivalence proof and the stated composition/base-change
lemmas were inspected; the latter proofs are omitted. For this attempt
require an actual global seven-element basis, not just local freeness.

## Exact specialization obligations

Use L071's full quotient over L070's degree-eight D and L073's entire
rank-48 algebra B on its stated basis. View Spec(B) as the specified
nonidentity dual-kernel subscheme of the target curve. The proposed
construction is its scheme-theoretic inverse image under that quotient.
This sentence specifies the next attempt; no presentation, specialized
polynomial identity or incidence identification is proved in this turn.

The applicability proof must check both directions: every point of the
constructed inverse image gives a nonzero seven-torsion point on L072's
line, and every incident pair appears uniquely. Use the actual dual
composition and L072's specified inverse, across every direction embedding.
Account for O, all kernel points and both signs; no missed point may be
silently removed by localization. Preserve inverse ordinary-functional
indexing, the Cartier cyclotomic convention and all coefficient conjugations.
The total family is viewed over Q by composition, not Weil restriction.
In particular, do not assume the target x-coordinate T is nonzero simply
because the generic proof chooses it so; certify the specialized chart
without that restriction, or stop with the uncovered component recorded.

A univariate presentation obtained by clearing L071's x-equation is
permitted if the whole degree-seven polynomial, its monic normalization,
full derivative inverse, all quotient-denominator inverses and exact
recovery of the y-coordinate pass complete verification. Retain the
y-equation and original curve equation; satisfying only the x-equation
is insufficient. This is a proposed implementation/test specification,
not a derived formula or a claim that the required units already exist.
If it fails, stop with the actual obstruction; do not approve a new
multichart or translation construction during the calculation.

Provide the full seven-element B-basis and its 336 rational-coordinate
identification, with exact forward/inverse basis transports. Certified
monic normal forms may establish these transports without solving a
redundant dense matrix problem. Both pullbacks must be explicit: the
B-inclusion and the point-algebra map using both L067 coordinate models
and their audited inverse transports. Verify all source relations,
multiplication compatibility and the full rank-48 image of each map.
No field-factor decomposition or isomorphism between point and line
algebras is assumed.

## One bounded discriminating test and stop rule

Allow one construction stage and one independent replay stage, each with
an external watchdog, 180-second arithmetic cap and a total 128-MiB
new-certificate limit. Include all new arithmetic in its declared stage;
report actual time/bytes and failing check even on interruption. Preserve
original bytes, save unfinished reasoning first and do not split/retry
failed stages or extend the old caps.

The success threshold is the whole rank-seven algebra over full B, with
336 rational coordinates, every specialized equation/unit/derivative
witness, every basis transport and both geometric pullbacks verified.
The independent verifier must reconstruct from the audited inputs without
importing producer arithmetic and check complete relevant coefficients,
not sampled roots or columns. Include bounded corrupt-unit, wrong-point-map
and missing-fiber/sign rejections with exact expected failure scope; a
prefix rejection must be labeled as such. Preserve all originals and
save full evidence under `scripts/seven-torsion/`, printing only concise
actual/required bounds, failures and artifact paths.

Continue only if that entire threshold passes. Stop on the first failed
obligation, cap or missing essential identification and preserve evidence.
A narrower valid input may be recorded honestly, but it is not completion
of this target. A norm or descent follow-up is outside this approval.
Full matching Mathlib coverage is not checked; this is not an absence claim.
A completed construction would still need its separate critical audit.

## Duplicate, failure and discovery comparison

ATTEMPTS/035 stopped a 2016-dimensional translation stream with 329/2016
columns and a recorded time overrun. ATTEMPTS/036 stopped the compressed
relation at 26/336 columns within its fixed 180-second cap. Their
unfinished actions/translations are not verified inputs. The new mechanism
uses the already completed quotient and dual algebra, then a relative
fiber presentation; it does not resume either column loop. Its practical
cost remains untested and no faster-runtime theorem is claimed.
ATTEMPTS/037--038 concern repaired verifier/harness failures; L073's
successful step-266 audit is retained without repetition.

Dedicated queries this turn were `elliptic curve p descent incidence
algebra isogeny fibers Schaefer Stoll`, `"incidence algebra" "isogeny"
elliptic`, `"p-descent" "fibers" "isogeny"`, and `"Schaefer" "Stoll"
"quotient" "incidence"`, with targeted MIT and Stacks theorem searches.
They returned the primary long version and explicit-isogeny/n-descent
leads. Miller--Stoll, Explicit isogeny descent on elliptic curves
(arXiv:1010.3334), and Cremona et al.'s explicit n-descent series were
located but not read for new input; their snippets are not theorem
coverage. The prior inspected Magma rational-torsion routines do not
supply the present whole-direction family. No matching fixed complete
certificate was found in checked local passages or inspected sources;
this does not establish novelty or exhaust all software and literature.

The companion source record is
`drafts/2026-10-17-quotient-fiber-incidence-source-review.md`.
No new lemma, mathematical script or incidence calculation was made.
This newly ready continuation receives separate supervisor approval
before the construction attempt; that approval need not repeat discovery.
