# Quotient-family identification — approved critical-audit coverage

TARGET: Critically audit L072's whole-family quotient-to-affine-line identification, including descent, inverse labels, scalar action and cyclotomic conventions.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement, terminology and stronger-result searches in drafts/literature/2026-10-16-quotient-affine-line-dual-kernel.md; read L072 in full, relevant L067/L068/L070/L071 hypotheses and conclusions, history/257--258 and ATTEMPTS/035--036. Reopened the primary dual-isogeny Case 1, ordinary-dual/B definition and finite-etale equivalence identified below. No new discovery search or novelty claim.
SOURCE_EVIDENCE: Sutherland MIT 18.783 Fall 2025 Lecture 6 Theorem 6.7, prime-degree Case 1 printed pp.3--4, Lemma 6.10 p.5; Schaefer--Stoll author long version 2001-06-13 Lemma 7.5, definition of B and Lemma 7.6 statement printed p.16; Stacks 58.2.2 tag 03QR statement and orbit/stabilizer proof reopened 2026-10-16. Reused inspected Milne Abelian Varieties v2.0 (2008) I.9.1 and following paragraph p.41, and Sutherland Lecture 23 Warning 23.21/Theorem 23.23 and relevant proof cases pp.10--11 from the unchanged construction assessment.
COMPARISON: The imported theorems cover the exact characteristic-zero degree-seven dual, its torsion-image kernel, Cartier dual with induced target action, ordinary-dual affine-line labels and finite-etale descent. Auditing L072's fixed whole-family specialization stays within those hypotheses; the sources do not certify its two maps, all-fiber transport or scalar conventions automatically.
GAP: Source scope is ready; the separate critical audit of L072's applicability proof is still outstanding. No critical-audit success, new algebra presentation, incidence/norm or arithmetic descent is established by this literature turn.
REASON: The previously proposed audit now has a separate theorem-by-theorem coverage comparison against the completed proof. SPECIALIZE permits a RESEARCH / REPRODUCTION proof audit of the exact TARGET without rederiving general duality or reopening implementation.
LITERATURE_REASON: The invocation-start critical-audit target was REVIEW_REQUIRED even though construction coverage was ready; this separate comparison resolves that gate and is not a refresh of unchanged construction coverage.
SCOPE: Exact TARGET only, with audited L067/L068/L070/L071, full degree-eight D, raw short models and both coordinate transports; excludes L069, unfinished columns, explicit dual polynomials, field decomposition, incidence/norm and arithmetic descent.

## Relevance and bounded decision

The main gap remains rank E(Q)=m(E) for arbitrary E/Q of analytic
order at least two. The intermediate target is the separate critical
audit specified above. A reliable abstract affine-line identification
could guide a later finite presentation for L066's descent enclosure.
That presentation and complete arithmetic descent remain independent
missing inputs; this audit cannot remove divisible Sha or give rank.

The construction assessment remains adequate for its original searches:
the curve, prime, full direction field, quotient and action hypotheses
have not changed. L072 is the newly completed applicability proof,
not a previously audited duplicate. The statements inspected in L067
and L068 retain the full torsion set, rational coordinate transport
and forward pullback convention. L070 retains every direction and the
full mixed inverse/cubic. L071 retains the whole D-defined separable
quotient and its exact kernel, without a rational subgroup generator.
This review accepts those audited inputs; it does not replay their
large certificates or claim to have freshly audited them.

ATTEMPTS/035--036 are specific full-column cost stops. They remain
parked and provide no mathematical input to this audit. The new target
is independently testable using the completed quotient, without partial
incidence columns or L069. No cross-notebook result is used.

## Primary theorem comparison

[Sutherland, Lecture 6](https://math.mit.edu/classes/18.783/2025/LectureNotes6.pdf),
Theorem 6.7 and Case 1, pp.3--4, were reopened through the construction
of the dual using the image of the prime-torsion subgroup. Lemma 6.10
p.5 supplies the reverse composition. This covers the dual for L071
over D: the degree is seven and the characteristic is zero. Uniqueness
is the appropriate cited input for checking conjugation of the actual
D-defined quotient and dual between embeddings. The later audit must
check this use on those models, and the torsion-image assertion in each
fiber, rather than infer it from matching cardinalities.

[Milne, Abelian Varieties v2.0 (2008)](https://www.jmilne.org/math/CourseNotes/AV.pdf),
I.9.1 and the following paragraph, printed p.41 (PDF p.47), supply the
Cartier dual and its prime-to-characteristic description with induced
Galois action. This precise inspected coverage is reused. It applies
under the canonical elliptic principal polarizations and does not
supply an ordinary dual with trivial roots-of-unity action. The unread
1986 numbering and unread Mumford/Oort proof references remain leads,
not additional premises. No reproof of Cartier duality is needed.

[Sutherland, Lecture 23](https://math.mit.edu/classes/18.783/2025/LectureNotes23.pdf),
Warning 23.21 and Theorem 23.23 pp.10--11, with the inspected bilinear,
alternating, nondegenerate and Galois proof cases, are reused unchanged.
They cover the pairing on seven-torsion in characteristic zero. The
audit must check L072's stated argument order and explicit realization,
including independence of lifts and stabilizer-equivariance. The target
does not assert a sign comparison with an unspecified canonical
isogeny pairing; no unread sign theorem is essential to this scope.

[Schaefer--Stoll, author long version, 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Lemma 7.5 and the adjacent definition of B, printed p.16, were reopened.
They use level-one sets of ordinary linear functionals and define the
algebra by the whole Galois set. The following Lemma 7.6 statement
retains the roots-of-unity tensor factor. These cover L072's intended
ordinary-dual label space, without a residual-image hypothesis. They
do not license copying L068's forward scalar index onto those labels:
the inverse index and compatibility with Cartier characters are fixed
specialization obligations for the later audit. Proposition 7.10's
incidence norm is downstream and is not required or imported here.

[Stacks Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR),
including the orbit/stabilizer proof, was reopened. It covers schemes
etale over a field and their continuous Galois sets, retaining every
orbit. This licenses descent after the maps and equivariance have
been checked. It does not infer an isomorphism from cardinalities or
identify a composed D-scheme with a Weil restriction. The audit must
check finite etaleness and the exact identity complement before using
this equivalence. No fieldness conclusion for B is covered.

## Authorized audit and continuation test

Check the proof of L072 in full against these named inputs and the
needed canonical passages of L067/L068/L070/L071. The precise bounded
test is: verify the forward and inverse constructions in every one of
the eight fibers, conjugation of quotient and unique dual, exactly one
identity exclusion per fiber, and the total scheme obtained by
composition to Q. Verify equivariance before descent. Check the inverse
ordinary-dual scalar index, the forward pullback comparison with L068,
and the target action on Hom(C,mu_7), without a rational generator or
root-of-unity trivialization. Distinguish a Galois-set bijection from
an additive identification of the functional labels.

Continue using L072 only if these load-bearing claims survive the
separate audit. A failed claim requires a precise repair or a retained
narrower conclusion before further use; a new uncovered replacement
needs REVIEW_REQUIRED coverage. Counts alone, a single chosen embedding
or an unrecorded sign convention do not pass. This approval records
source sufficiency, not the outcome of any of these mathematical tests.
No mathematical script or additional calculation is needed for this
abstract proof audit unless it exposes an independently justified need.

Explicit presentation, incidence/norm, functions, complete units/classes,
local identifications and bounds, Selmer containment, other L026 premises,
successful localization, rational membership, divisible Sha and arbitrary-
curve comparison remain unresolved. Full matching Mathlib coverage was
not checked; unknown availability is not absence. No new lemma or
mathematical script is written in this literature-only step.
