# L046 critical audit — completed source comparison

TARGET: Critically audit L046's integral coordinate maps, full-rank count comparison, global mod-7 image and embedded local finite-torsion preservation.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused ready mod-7 construction/L044 audit coverage; searched histories 141–148, ATTEMPTS/027 and the mod-7 working note for prior audits, overlap and scope failures; retrieved exact primary statements and relevant proofs rather than reopening generic-image discovery.
SOURCE_EVIDENCE: Zywina, author-hosted 15-page MaximalGalois.pdf, section 1.1 p.1, Definition 5.1 p.6, Proposition 5.7 and full proof p.8, Q-case assertion in Lemma 2.4's proof p.5; Milne EC2 (2021), II.1 Proposition 1.5/proof p.49, II.2 changes/Theorem 2.1(b)/relevant proof pp.50–51, Theorem 2.4(b)/proof qualification pp.52–53; Bisatt–Dokchitser, version of record (2021), Notation 1.5/Theorem 2.2/complete proof p.1441.
COMPARISON: Sources cover fixed-level counting in the entire integral coefficient box over Q, pointed rational transport and full local m=210 constancy. L046's integral maps, affine-family count and restricted kernels still require separate mathematical audit; no new density or constancy theorem is needed.
GAP: Source coverage is ready; correctness of L046's coordinate identities, lattice index/error terms, fixed-M domination and full embedded-kernel transport remains unverified by this turn.
REASON: The new audit target has been compared with the primary hypotheses, extending prior construction coverage to the written audit obligations without deriving or validating their mathematics.
SCOPE: Exactly TARGET, with fixed sufficient M and original monic cubic neighborhood, audited L044 and its retained L042 Omega,H,N packet. No effective coefficients, image after restriction to F, exact-curve globalization or sufficient initial theta data.
LITERATURE_REASON: Separate scope approval is required for the newly saved L046 audit continuation; reuse unchanged ready coverage and retrieve only load-bearing theorem passages.

## Relevance and review boundary

The main gap is the original finite B>=A comparison in IUT III,
Corollary 3.12, step (xi-f). The intermediate target is the exact audit
in TARGET. A validated combined global/local prerequisite could support
a later use of L045 and a separate image-restriction or initial-data
screen. Those are downstream uses, not approved targets of this turn.
No essential IUT flaw or progress beyond the checked source methods is
claimed. This is one literature-only comparison, not a proof audit.

Canonical L046 was read in full. L044's constancy hypotheses and its
separate audit were inspected; its audited L042 packet is retained
without reopening the local Tate-field calculation. The ready
assessments reused are
`drafts/literature/2026-10-11-mod7-surjective-local-approximation.md` and
`drafts/literature/2026-10-11-finite-torsion-global-curve-critical-audit.md`.
Their hypotheses have not changed. Full matching Mathlib coverage
remains unchecked, as in L046; no absence claim is made.

## Primary statements and applicability

[David Zywina, *Elliptic curves with maximal Galois action on their
torsion points*](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
*Bull. London Math. Soc.* 42 (2010), 811–826,
[DOI](https://doi.org/10.1112/blms/bdq039). Read the author-hosted,
undated 15-page version on 2026-10-11; pages refer to that version,
not arXiv v1. Section 1.1 permits any fixed norm and counts integral
nonsingular short models, rather than isomorphism classes or minimal
models. L046's maximum norm is in scope. Definition 5.1 and Proposition
5.7 cover any number field and fixed positive m, with exceptional
proportion bounded by a constant depending on k, norm and m times
log(X)/X^([k:Q]/2). Its complete proof was read. The Q-case equivalence
in Lemma 2.4's proof supplies the fixed-level GL_2 criterion; its
stronger Serre-curve conclusion is not imported. No non-CM or
prescribed-good-reduction condition is added. Reuse the prior
assessment's inspected Proposition 5.5 and A.10/A.8 prime case at m=7;
do not reprove the sieve or group-theoretic inputs.

[J.S. Milne, *Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf).
The retrieved II.2 passages cover quadratic-term removal and scaling
in characteristic different from 2 and 3, and general pointed
Weierstrass changes over the base field. Theorem 2.1(b)'s relevant
proof and Theorem 2.4(b)'s statement/converse and proof qualification
were read; the latter refers to the same argument with more algebra.
II.1 Proposition 1.5 and its complete proof give group-law preservation
for pointed nonconstant regular maps. These apply over Q. They do
not certify L046's particular signs, integrality, inverse or projective
identity, which the later audit must check. Geometric isomorphism or
equal j-values cannot replace a Q-defined pointed isomorphism.

[M. Bisatt and T. Dokchitser, *Tame torsion and the tame inverse
Galois problem*](https://doi.org/10.1007/s00208-021-02173-y),
*Math. Ann.* 381 (2021), 1439–1453, version of record 2021-04-27;
[repository PDF](https://d-nb.info/1235382842/34), PDF index 2,
printed p.1441. Read Notation 1.5, Theorem 2.2 and its entire proof.
The notation includes genus one. For squarefree f in Z_ell[x] and
every m>=1, sufficiently close same-degree polynomials have isomorphic
full Jacobian m-torsion as G_Q_ell-modules; its proof retains
squarefreeness and genus. Neither prime-to-ell nor good reduction is
a hypothesis, so ell=3, m=210 is covered. Import the published special
case, without a separate Kisin reproof or claimed inspection. Audited
L044 supplies the pointed Jacobian identifications and embedded packet.

## Approved obligations for the later audit

The specialization already written in L046 is the object of review,
not a new theorem derived here. SPECIALIZE authorizes a later
REPRODUCTION audit of precisely these obligations:

1. Retain the original monic cubic and all congruences at fixed
   sufficient M. Check both rational maps on the homogeneous cubics,
   their inverses, the point at infinity and integer short coefficients.
   Apply group-law and Galois transport only after establishing the
   pointed Q-isomorphism.
2. Check the two-parameter integer matrix, nonzero determinant,
   injectivity and stated index. Audit center-independent interval
   errors and nonsingularity. Compare exceptions in the entire box,
   without an unproved density assertion for the subfamily. M remains
   fixed while R grows. Compare L046's stated quadratic leading count
   with its stated O(R^(3/2) log R) exceptional count explicitly.
3. Check the full global 7-torsion representation through the Q-map
   and exact Q-case criterion. Retain the original cubic for local
   constancy; the scaled short model need not occupy that same local
   coefficient neighborhood.
4. Reuse L044 at level 210, restrict to actual G_H in Omega and retain
   the full subgroups killed by 30 and 7. Audit complete pointwise-
   fixing kernels and embedded fields using the standard fundamental
   theorem of Galois theory. Neither x-coordinates alone, a cyclic
   subgroup, matching degrees nor abstract field isomorphism suffices.

Continue only if all four checks pass or a precise repair preserves
the approved scope. Abandon the stated count specialization if it is
thin, loses original congruences, requires unprovided uniformity in M
or only gives geometric transport. Essential uncovered source cases
return to REVIEW_REQUIRED. This is not a verdict on those checks.

## Overlap, preserved stops and continuation

Targeted searches found the construction comparison in history 147
and specialization in history 148, but no separate L046 audit.
History 142 records L044's prior audit. L045 is downstream, not a
premise for global image over Q. No wider generic-image, Hilbert or
Serre-curve search is needed; unused leads in the prior assessment
remain unused. Failed local searches do not establish novelty.
No cross-notebook input is used.

ATTEMPTS/027 stops globalization of the exact Tate curve, whereas
L046 retains only its finite module. The distinct field-factor and
tensor-component stops in ATTEMPTS/022,025,026 remain intact; this
review does not reopen them. Preserve unfinished work. Essential
continuation inputs are L046, direct input audited L044 and the fixed
L042 packet through L044, with the primary citations above. Image
preservation after restriction to L045's F, effective coefficients,
geometric-parameter/full initial data, native/input/action, marked
pilot transport, essentiality and original finite B>=A remain open.

The exact audit continuation now has source coverage for separate
next-turn approval. No lemma, mathematical script, DAG row or PROOF
assembly is modified, and no mathematical audit verdict is recorded.
