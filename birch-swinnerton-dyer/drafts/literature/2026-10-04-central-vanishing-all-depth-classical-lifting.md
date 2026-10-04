# Assessment of all-depth classical lifting after central vanishing

TARGET: Test whether Kim's Selmer structure theorem and Cassels pairing upgrade C016a's p^2 lifting to compatible classical Selmer lifting at every coefficient depth, without assuming finite p-primary Sha.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Twelve bounded queries recorded below screened compatible coefficient lifting, paired Selmer structure and divisible Sha; read the accessible primary Kim and Milne statements and Poonen--Stoll's introductory pairing statement. Reused prior Sakamoto and official-scope coverage; search snippets and inaccessible original references are not imported as read sources.
SOURCE_EVIDENCE: Kim, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf, author text dated 2025-05-12, Sections 1.4--1.5, Theorem 1.8 (printed pp. 5--7), Theorem 5.1 (p. 26) and Section 5.3.1 (p. 28), compared with https://arxiv.org/html/2203.12159v6; Milne, https://www.jmilne.org/math/Books/EC2.pdf, second edition (2021), Chapter IV, diagram and Proposition 5.1 with footnote 7 (p. 129), Remark 5.2 and Theorem 5.4 (p. 130); Poonen--Stoll, https://math.stanford.edu/~conrad/BSDseminar/refs/PoonenStoll.pdf, text dated 1998-11-06 with correction 2014-08-23, introduction p. 2.
COMPARISON: Kim gives the complete p-primary Selmer decomposition with paired finite factors and explicitly identifies classical finite-coefficient Selmer with its p^m-torsion. Milne supplies the coefficient maps and Cassels's divisible kernel. These cover the structural inputs, but no inspected statement names C016a's prescribed compatible lifts or removes a possible divisible Sha contribution.
GAP: Specialize the known decomposition to C016a's residual dimension and Selmer infinitude, check the natural coefficient identifications, and decide whether the prescribed depth-two basis admits compatible lifts. This review makes no such deduction; rational Kummer membership and r >= 2 remain separate gaps.
REASON: Approve a mathematical application of the known structure and coefficient results, retaining the original target. The only additional work is the specified finite/infinite-coefficient comparison and compatibility for a chosen basis; reproof of Kim's structure theorem or Cassels's pairing would be redundant.
LITERATURE_REASON: The saved assessment was REVIEW_REQUIRED for the stronger all-depth conclusion; the complete paired decomposition, its natural finite-coefficient identification and the pairing's divisible radical were concrete source needs.
SCOPE: Retain C016a's non-CM ordinary non-anomalous hypotheses, surjective E[p], local-torsion/Manin/Tamagawa conditions, fixed P_(2,0) primes, minimal nonzero mod-p two-prime Kurihara premise and L(E,1)=0. Assume neither finite p-primary Sha nor positive rational rank; require no higher eligibility for the old primes.
COVERED_TARGET: Apply Kim's Theorem 1.8 and the natural coefficient maps to test whether C016a's prescribed p^2 Selmer basis has compatible classical lifts at every depth, keeping Cassels's divisible Sha radical explicit.

The original TARGET is preserved exactly. This is one source-review step;
no all-depth implication, obstruction model or new proof is derived, and
no lemma or mathematical script is changed. The SPECIALIZE decision
approves the original target and the exact application above for a later
research turn. It makes no claim of progress beyond the checked literature.

## Main gap, intermediate target and continuation test

The main gap is rank E(Q) = m(E) for arbitrary m(E) >= 2. On the
conditional two-prime branch the achieved rational bound is r <= 2,
whereas the necessary lower bound is r >= 2. A compatible Selmer basis
could remove finite coefficient-lifting defects and isolate what remains
of the Sha contribution before a rationality test. Production of the
two-prime premise from m(E) = 2, rational membership, the determinant
comparison and higher ranks remain unresolved.

For S_m = Sel(Q,E[p^m]), the requested lifts would be classes x_i^(m)
for every m >= 2 with x_i^(2) = c_i, and with each coefficient map
[p]: S_(m+1) -> S_m sending x_i^(m+1) to x_i^(m), for i = 1,2.
This is classical coefficient lifting; it does not request new
prime-deletion system components at an index outside P_(m,0).

The application must test the finite paired quotient allowed by the
structure theorem against C016a's already recorded dim S_1 = 2 and
infinitude of Sel(Q,E[p^infinity]). Then check the coefficient maps and
compatibility while fixing both initial c_i. A group isomorphism at
each separate depth alone is not a compatible lifting argument.

Continue this lifting route if the retained inputs force the indicated
compatible lifts. Stop the all-depth implication if an allowed finite
paired contribution obstructs a later coefficient map, or a claimed
coefficient identification needs an unretained hypothesis. In either
case, keep the divisible Sha radical separate from rational points.
The outcome of this mathematical test is not supplied here.

## Closest inspected statements

**Kim.** *The structure of Selmer groups and the Iwasawa main conjecture
for elliptic curves*. The publisher-hosted author PDF is dated
2025-05-12; the [arXiv record](https://arxiv.org/abs/2203.12159)
lists v6 dated 2025-05-14. Both forms of the relevant statements were
read; file identity is not assumed.

[Theorem 1.8](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7)
assumes p >= 5, surjective residual representation, Manin constant prime
to p and a nonzero Kurihara collection. It gives the corank and finite
quotient, with the displayed decomposition of the following shape:

\[
\operatorname{Sel}(\mathbf Q,E[p^\infty])
 \simeq (\mathbf Q_p/\mathbf Z_p)^d
       \oplus\bigoplus_{i\ge1}(\mathbf Z/p^{a_i}\mathbf Z)^2,
\]

where the theorem specifies d = ord(tilde-delta) and a_i by differences
of its partial valuation minima. Clauses (4)--(6), identifying rational
rank and Sha, add finite p-primary Sha. These qualifications are retained; the
notebook's residual minimum is not silently made the integral minimum.

[Section 5.3.1](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28)
explicitly uses the classical identification
Sel(Q,E[p^k]) isomorphic to Sel(Q,E[p^infinity])[p^k], citing Mazur--Rubin,
Lemma 3.5.3. [Theorem 5.1](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=26)
records the generalized pairing and coefficient-lifting kernels under
its Selmer-structure setup and the bound s + t <= k for positive s,t.
The [HTML version](https://arxiv.org/html/2203.12159v6#S1.SS5)
confirms the paired finite factors. Cite these inputs without reproof.

**Milne.** *Elliptic Curves*, second edition (2021). Read the
[Chapter IV diagram and Proposition 5.1, printed p. 129](https://www.jmilne.org/math/Books/EC2.pdf#page=134),
including its proof and compactness footnote 7. The diagram identifies
downward maps as quotient maps on points and multiplication by p on
Sha. Proposition 5.1 identifies persistent residual Selmer images with
the rational image only under absence of nonzero infinitely p-divisible
Sha elements. That absence-of-divisibility condition cannot be omitted.

[Remark 5.2 and Theorem IV.5.4, printed p. 130](https://www.jmilne.org/math/Books/EC2.pdf#page=135)
explicitly retain that obstruction: the Cassels pairing is alternating
and has the divisible subgroup as its kernel. A vanishing pairing or
all-depth lifting is not a published rational-membership criterion
without the extra condition. Restrictions to p^m-torsion need not be
nondegenerate even when the full finite p-primary pairing is.

**Poonen--Stoll.** *The Cassels--Tate pairing on polarized abelian
varieties*, author text dated 1998-11-06, corrected 2014-08-23.
The [introduction, p. 2](https://math.stanford.edu/~conrad/BSDseminar/refs/PoonenStoll.pdf#page=2)
confirms that nondegeneracy is on Sha modulo its maximal divisible
subgroup, and that the elliptic-curve pairing is alternating. This is
supporting source coverage, not a match for the prescribed lifting
statement; later results on general principal polarizations are not used.

## Why specialization is needed and what is already covered

C016a already matches the auxiliary modular-symbol witness to Kim's
nonvanishing hypothesis. Reuse that applicability argument and the
[preceding assessment](2026-10-04-prime-deletion-p3-initial-fitting.md);
do not rederive the finite-Selmer converse or recompute tau. Reuse
[Sakamoto coverage](2026-10-03-rank-zero-extra-relaxed-prime.md)
for the residual basis and depth-two prescribed classes.

The known structure is stronger than a mere finite-depth size bound.
Its comparison with the recorded dimension and infinitude, followed by
the functorial coefficient maps, is the exact remaining specialization.
Check the classical Kummer conditions and global torsion in that
comparison. Do not substitute p-relaxed Selmer or integral Selmer modulo
p^m for classical finite-coefficient Selmer. In particular a quotient
Sel(Q,T_p E)/p^m need not exhaust the latter just because it injects.

Nothing in the inspected rational-rank statements removes the finite-Sha
hypothesis. The current application may address lifting, but importing
rational rank two from this literature would require an extra input.
No new primitivity theorem, pairing construction, main conjecture or
generalized Kato rationality assertion is proposed.

The previous finite-tower ambiguity in ATTEMPTS/001 and automatic-promotion
failures in ATTEMPTS/017--018 remain evidence. This test uses the actual
infinite Selmer structure and central-value constraint already imported
in C016a, not another self-pairing calculation at depth two or an increase
of a preset observation depth. The parked Eisenstein route is unchanged.

## Searches and access qualifications

Queries actually issued on 2026-10-04:

- `"Kim" "Theorem 1.8" "Selmer" "Kurihara"`
- `Cassels Tate pairing maximal divisible subgroup elliptic curves Selmer Tate module without finite Shafarevich`
- `"Kurihara" "Selmer" "divisible" "minimal"`
- `"Selmer" "compatible" "lifts" "Cassels" p`
- `"Tate module" "Selmer group" "Sha" exact sequence without finite`
- `Mazur Rubin Kolyvagin systems "Lemma 3.5.3"`
- `Mazur Rubin Kolyvagin systems pdf book 2004`
- `site:math.uci.edu/~krubin "Kolyvagin" "pdf"`
- `site:people.math.harvard.edu/~mazur "Kolyvagin Systems"`
- `site:math.harvard.edu/~mazur "systems.pdf"`
- `Mazur Rubin "ks.pdf"`
- `"Kolyvagin systems" "pdf" "3.5.3" -site:nzdr.ru -site:researchgate.net`

The accessible Kim and Milne texts supply the essential statements.
No separately named theorem asserting the exact chosen-basis conclusion
was located in this bounded search; this is not an originality claim.
Poonen--Stoll's first attempted MIT address failed, but its Stanford-hosted
primary text was read. Theorems are not inferred from search snippets.

The original Mazur--Rubin monograph was not successfully read: AMS and
author-page attempts failed, and a book mirror timed out. Lemma 3.5.3 is
therefore reported only as Kim's cited reference, not independently checked
in its general-ring hypotheses. The covered classical identification is
explicit in Kim's inspected text; the generalized abstract version is
parked. The forthcoming specialization may justify its natural maps
directly from classical Kummer diagrams rather than depend on the unread
general version. Flach and Howard are likewise references through Kim's
inspected Theorem 5.1, not newly read original sources.

An optional Nekovar pro-Selmer exact-sequence lead was inaccessible and
is not an imported input. It is not needed for the approved classical
coefficient test. Local shell downloads also failed DNS resolution;
web access to the essential Kim and Milne texts succeeded. No essential
source blocker remains for the narrowly covered application. Changed
local conditions or an appeal to a stronger unread theorem would need
a new assessment.

## Mathlib

Full coverage of the prescribed all-depth compatible lifting implication:
**not checked**. Supporting Selmer decomposition, divisible Sha, Cassels
pairing, coefficient maps and inverse-limit arguments: **not checked**.
The named primary statements above match supporting arithmetic inputs;
none is asserted to be a full-statement Mathlib match. No library absence
or novelty inference is made.
