# Three-adic image critical audit — source coverage

TARGET: Critically audit L048's full three-adic factor certificate and unrestricted connecting-image theorem application.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact 54a1/local-three/X0(11)/Kummer searches in drafts/literature/2026-10-10-three-adic-unrestricted-connecting-image.md; read its full comparison, L048, foundations 15/17, L033's field/dual-kernel/model interfaces, histories 124–125, ATTEMPTS/014–015 and the ready two-adic audit assessment. No fresh external search or novelty claim.
SOURCE_EVIDENCE: Reused inspected Schaefer–Stoll June 13, 2001 long manuscript Lemmas 4.2–4.5 pp.6–7, Clark's 161-page notes Theorem 1.75/Corollary 1.77 p.57 and Theorem 2.8/Proposition 2.9/Corollary 2.10 pp.64–65, Milne ANT v3.08 Theorem 7.33/Remark 7.36 pp.121–123 and Corollary 7.42/Remark 7.43 p.124, and FNS June 10, 2019 Section 7.2/Table 5 pp.25–27. No new primary retrieval is claimed.
COMPARISON: These general theorems cover every local-field and image tool used in L048, including simple-root lifting inside a finite complete root field. They do not certify the explicit constants, descent to one Q3 field, actual residue field or image specialization; those are the independent audit's difference.
GAP: Source coverage is ready; independent verification of L048's complete arithmetic evidence, degree-twelve descent and image-theorem hypotheses remains undone. Global 54a1 intersections and L045's quotient classes remain unresolved.
REASON: Separately approve one bounded critical audit using adequate existing coverage, importing the general theorems without reproof. This process completion establishes no mathematical result and repeats no calculation.
SCOPE: Exactly L048's entire K tensor Q3 algebra and unrestricted theta:E1 -> E0 connecting image under L033's field, models, dual kernel and good-divisor identification; no restricted-image comparison, global classes, other twist or broader local algorithm.
LITERATURE_REASON: The newly proposed audit required separate scope approval; reuse the preceding ready assessment rather than repeat browsing on unchanged hypotheses.

## Primary theorem scope

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
June 13, 2001, Lemmas 4.2–4.5, printed pp.6–7. These are manuscript
locators, not assumed published numbering. For an isogeny with kernel
of exponent p away from residue characteristic p, Lemma 4.5 identifies
the connecting image with unramified cohomology when neither Tamagawa
number is divisible by p; Lemma 4.2 gives its size as the number of
rational kernel points. The preceding assessment inspected the complete
relevant Frobenius/inertia and formal-group arguments. Lemma 4.4's
supporting reference [24], Lemma 3.8, remains not separately reverified;
import the stated theorem, rather than claim an independent proof.

Use p=5, theta:E1 -> E0 and kernel mu_5 through L033's audited
Galois-equivariant pairing. The forward constant kernel is different.
Check good reduction of both integral models over the actual local
field, the resulting Tamagawa numbers, residue characteristic and
rational kernel size. The exceptional evaluations at T and O are retained
by L033's good-divisor interface. Neither a global Selmer/point equality
nor global class computation is part of this source application.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessible 161-page version, revision date unidentified: Theorem 1.75
and Corollary 1.77, p.57, cover coprime factor lifting and unique
simple-root lifting over complete valued fields. Theorem 2.8, p.64,
and Proposition 2.9/Corollary 2.10, p.65, cover Eisenstein irreducibility,
integer rings, uniformizers, unchanged residue field and total ramification.
Reuse the primary inspection recorded in the preceding assessment and
its local-algebra source trail. These hypotheses include finite complete
extensions of Q3. In particular the root-field Hensel step must be checked
in F0 itself, with its own integral approximate root and unit derivative;
no unstated root-field inclusion theorem or approximate-factor algorithm
is needed. Only this explicit verification is authorized, not reproof of
Hensel or Eisenstein.

J. S. Milne, [*Algebraic Number Theory*, v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 7.33 and Remark 7.36, pp.121–123, give coprime monic residue
factor lifting; Corollary 7.42 and Remark 7.43, p.124, give degree ef
and valuation normalization. Their statements and relevant proofs were
inspected in drafts/literature/2026-10-08-full-fiber-at-one-local-algebra.md,
as recorded by the preceding assessment. These are reused imports.
Matching e,f values alone do not identify ramified fields. L048 instead
claims a root-field descent and must have that argument checked.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. **156** (2020), 77–113,
[June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.25–27, Table 5, supplies the canonical degree-twelve
field used by L033. The preceding assessment rechecked the canonical-fiber
paragraph and table. Neither this passage nor its adjacent GRH-dependent
two-Selmer calculations certifies L048's three-adic fifth-isogeny image.
The GRH computations are excluded; the local proof is independently
checkable using the stated defining polynomial and models.

## Audit obligations and bounded test

The main gap is global emptiness of the 54a1 branch, with other twists and
residual signatures still open. The intermediate target is whether L048
is a sound entire local input. Its plausible downstream use is a later
comparison with L047's separately audited restricted nonemptiness and
necessary global class restrictions. Neither use is performed here.

Essential inputs are L048's full proof and
scripts/three-adic-image/image-certificate.json; L033's defining field,
curves, dual kernel and Kummer/good-divisor identification; foundation 15
and the preceding approved unrestricted-image assessment. Foundation 17
records the lifting source trail. L047 is downstream only and is not a
mathematical input to this audit. No cross-notebook theorem is used.

Independently check all thirteen coefficients, the complete reduction,
both exact H(±i) values and constant valuations, both coprime residue
factor occurrences and unit evaluations. Use the JSON inspector for
complete selected load-bearing values, not flags or previews. A rerun of
the construction alone is not independent verification. Check integrality
and all below-leading coefficients in each translated factor, uniformizer
normalization and Eisenstein hypotheses. Then check completeness of F0,
its residue embedding, the simple-root uniqueness argument placing i
inside F0, degree twelve and exhaustion of the whole Q3 algebra. Two
factors after quadratic base extension must not be counted as two Q3
factors. Repeated reduction of a power order is not prime decomposition.

Check both model discriminants, good reduction after this extension,
Tamagawa applicability, actual residue field, reduction of fifth roots of
unity and the unit derivative/uniqueness clause. Check the direction of
the isogeny and transport of the identity class through Kummer. Do not
infer a restricted-image equality from singleton unrestricted image alone.
The canonical certificate is available for the next audit; no certificate
execution or mathematical verification was performed in this review.

Continue if every load-bearing obligation is covered and independently
checks; otherwise record the exact defect and its effect on L048, or gate
any essential uncovered theorem separately. Do not reopen the stopped
local-nonexistence route in ATTEMPTS/015 or the two-adic filter in
ATTEMPTS/014 merely because this audit passes. Those stops are specific,
not a ban on other mechanisms. Preserve unfinished global arithmetic.
No GRH, rank, Sha vanishing or Selmer/point equality is assumed.

This is STALLED source-scope completion, not new mathematical evidence or
an independent audit. Mathematical exploration usage remains 0/3.
Mathlib full matching and supporting coverage remain not checked; unknown
availability is not absence. The ready audit receives its own next turn.
