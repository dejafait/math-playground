# Extra relaxed auxiliary prime after the rational-correction obstruction

TARGET: Assess the applicability of Sakamoto's extra-relaxed-prime rank-zero construction to Kato's family at a minimal nonzero two-prime Kurihara index, retaining p-finiteness and isolating the separate rational Kummer requirement.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six bounded queries listed below located Sakamoto's published arithmetic transfer and explicit Selmer-basis result; the previously unread Angurel lead was compared in v1 and current v2. Reused the adequate Kim/determinant and official-target assessments instead of repeating those searches.
SOURCE_EVIDENCE: Sakamoto, https://ems.press/content/serial-article-files/29299?nt=1, published 2022 text, especially Section 2.5, Theorem 3.17, Proposition 3.19, Lemmas 4.2/4.4, Theorem 4.8 and Corollary 4.10; Sakamoto, https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf, Hypothesis 2.7, Definitions 2.11/2.15/5.1, Example 2.21, Theorems 5.5/5.8/6.3/6.4; Angurel, https://arxiv.org/pdf/2504.20759v2, 2026-06-08, Theorems 3.27/4.13/4.18 and Sections 4.1/4.6/4.7. Read scope and page references are below.
COMPARISON: The required construction has an explicit published match on the strengthened non-anomalous subcase, including a classical mod-p Selmer basis. It is an import, not a new construction. Coefficient-level applicability and global rational Kummer membership are distinct; the covered follow-up tests the former only.
GAP: Rational membership, r >= 2, the rational determinant comparison, production of the two-prime premise from m(E) = 2 and higher ranks remain missing. The published non-anomalous restriction must not be replaced silently by the original local-torsion assumption.
REASON: Import the transfer and basis statements by precise citation; specialize their existing finite-coefficient relations only for the fixed-prime p^2 test below. Do not reprove the construction or repeat L014's correction mechanism. This assessment supplies ready coverage for that mathematical application.
LITERATURE_REASON: The changed rank-zero construction required the previously unassessed arithmetic transfer, coefficient indexing and nonvanishing statements, rather than another review of the ready classical-system obstruction.
SCOPE: Retain non-CM E/Q, ordinary p >= 5, surjective E[p], Manin constant and Tamagawa factors prime to p, E(Q_p)[p] = 0 and the extra minimal nonzero mod-p two-prime Kurihara premise; for the covered application additionally require p not dividing #E(F_p) and use Sakamoto's actual prime sets P_(m,0) and compatible normalizations. Assume neither finite Sha nor positive rational rank; no complex/p-adic order comparison is supplied.
COVERED_TARGET: Test whether Sakamoto's two prime-deletion mod-p Selmer basis classes lift through his rank-zero family to classical Selmer classes in E[p^2] at the same auxiliary primes, retaining the non-anomalous ordinary hypotheses and the minimal nonzero two-prime Kurihara premise.

## Gap, target and decision

The original TARGET is unchanged from the pending checkpoint created on
2026-10-03. This turn completes its source assessment only. The main
problem is still rank E(Q) = m(E) for arbitrary m(E) >= 2. On the
conditional rank-two branch, a Selmer upper bound does not supply the
required two rational directions. A p-finite arithmetic input could
make a later rationality test meaningful, while the other gaps remain open.

The transfer is covered on an explicitly narrower subcase. The source's
stronger p-local hypothesis is recorded rather than inferred from
E(Q_p)[p] = 0. The broader anomalous subcase is parked for this
application, without an impossibility or novelty claim. No essential
unread source blocks the strengthened finite-depth test.

## Primary theorem ledger

**Sakamoto 2021.** *On the theory of Kolyvagin systems of rank 0*,
JTNB 33 (2021), 1077--1102; publication 2022-01-26. Rechecked
[Hypothesis 2.7 and Definitions 2.11/2.15](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=6):
residual irreducibility, a cyclic Frobenius quotient, the two Galois
cohomology vanishings, Cartesian conditions and core rank. The p = 3
qualification is outside p >= 5. [Example 2.21](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=9)
uses classical Kummer conditions and self-duality.
[Definition 5.1](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=13)
places components in F^q(n), retaining the p condition, with three
relations (5.1)--(5.3). [Theorems 5.5/5.8](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=16)
give rigidity and initial Fitting equality for a basis; Remark 5.9
does not give all higher equalities. [Theorems 6.3/6.4](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=22)
treat complete Gorenstein coefficients. This abstract theory alone
is not the arithmetic transfer.

**Sakamoto 2022.** *p-Selmer group and modular symbols*, Documenta
Math. 27 (2022), 1891--1922, DOI 10.4171/DM/X21. Inspected the
[publisher's PDF](https://ems.press/content/serial-article-files/29299?nt=1),
received 2022-05-13, revised 2022-07-20. Precise read locations:

- Section 1.1, pp. 1892--1893: hypotheses (a)--(c), prime set and minimality.
- Section 2, p. 1896: residual hypotheses for the induced module; Corollaries 2.14/2.15, pp. 1901--1902: local freeness and Cartesian conditions.
- Definition 2.18 and Theorem 2.20, pp. 1903--1904: rank-zero relations and projections.
- Section 2.5, pp. 1905--1907: transfer diagram (2), Theorem 2.24 and Stark-system contraction.
- Theorem 3.4 and Proposition 3.8, pp. 1909--1911: normalized Kato input; Theorem 3.17/Proposition 3.19, pp. 1915--1916: arithmetic system and primitivity.
- Lemmas 4.2/4.4, pp. 1917--1918; Theorem 4.8 and Corollary 4.10, pp. 1919--1920: nonvanishing comparison and explicit classical basis.

Condition (c) requires p not dividing #E(F_p) or the Tamagawa
product. Section 2.5 constructs Phi from the canonical rank-one
system to the classical rank-zero system, with delta Phi equal
to the p-singular scalar map. Theorem 3.17 applies it to the
normalized Kato-derived input. Proposition 3.19 and Lemma 4.2
connect the assumed mod-p Kurihara nonvanishing to primitivity.
Corollary 4.10 gives the prime-deletion classical mod-p Selmer
basis at a delta-minimal index. General components still have
relaxed/transverse auxiliary conditions. These statements do not
supply rational membership or a fixed-index p^2 classical basis.

**Angurel comparison.** *Kolyvagin systems of rank 0 and the structure
of the Selmer group of elliptic curves over abelian extensions*,
arXiv:2504.20759. Inspected v1 HTML (2025-04-29), Sections 1/3.5/4.1/4.6,
then the [current v2 PDF](https://arxiv.org/pdf/2504.20759v2)
(2026-06-08), Theorem 3.27, printed p. 26; hypotheses (E1)--(E2),
(K1)--(K5), pp. 33--34; Theorems 4.13/4.18, pp. 40--41;
Sections 4.6/4.7, pp. 58--60. V1 Theorems 3.5.2/4.1.13/4.1.18
use different numbering; version identity is not assumed.

V2 allows DVR or principal artinian coefficients in Theorem 3.27;
its structural theorem retains the augmentation-localized main
conjecture (K5). The arithmetic singular scalar uses the relaxed
prime p. This supplies Selmer/Fitting information rather than a
rational Kummer basis. The non-self-dual all-Fitting conclusion is
not a theorem for the untwisted elliptic representation. Broader
proof machinery was not audited or imported.

## Covered specialization and discriminating test

The follow-up uses E[p] and E[p^2], not an unproved passage from a
finite coefficient to a rational point. First check that both saved
primes lie in P_(2,0), using the exact definition on p. 1902. Failure
limits this fixed-index construction; it is not an obstruction to
every possible Selmer lift. Use the actual two-index components
with compatible generators and the source's coefficient reductions.

Then test every auxiliary singular localization of the lifted
prime-deletion classes against Definition 2.18 and delta. Finiteness
at p alone is insufficient. This prescribed test has not been
calculated here. Continue the fixed-prime mechanism only if both
eligible components reduce to the cited basis and satisfy all
classical local conditions at level p^2. Otherwise preserve the
specific failed condition and stop automatic promotion of this
mod-p basis by this mechanism. Success at this depth would still
require higher-depth compatibility and a separate rationality input.

This is a necessary intermediate test for this proposed rational
certificate, not itself a rank-two certificate. Global rational
membership and removal of the Sha contribution remain governed by
the Kummer distinction already recorded in the notebook. No theorem
assuming finite Sha removes that missing hypothesis.

## Redundancy, access and literature reuse

L014 and ATTEMPTS/016 concern rational subtraction in the original
ordinary rank-one family. The cited Phi transfer changes both the
object and its relations, so its use does not reopen that failed
correction. L013 remains a formal contrast, with no arithmetic
realization asserted. ATTEMPTS/014--016 and parked Eisenstein work
are preserved. The prior Kim/BSS/Castella--Sano comparison and
official Clay scope remain adequate for their unchanged statements.

Queries issued on 2026-10-04:

- Sakamoto "On the theory of Kolyvagin systems of rank 0" Kato extra prime
- "Kato" "rank 0" "Kolyvagin" Sakamoto Kurihara
- "Sakamoto" "rank zero" "Theorem 6.3"
- Sakamoto "p-Selmer group and modular symbols" pdf
- Sakamoto "Kato" "rank 0" "Euler"
- Angurel "Kolyvagin systems of rank 0" elliptic curves

The EMS publisher PDF supplies the essential arithmetic input.
Angurel's v2 HTML initially opened but later find/open calls failed;
the v2 PDF resolved access. Primary statements, not search snippets
or seminar announcements, support the comparisons. No other unread
lead is an input for the covered test. Absence of a match in these
statements does not certify novelty of the coefficient-level application.

The result is an imported known input with a bounded specialization
approved for the next mathematical turn. It establishes no new
result beyond checked literature. No calculation, new proof, lemma
or mathematical script is produced in this literature turn.

## Mathlib

Full library coverage of the arithmetic transfer, basis and covered
coefficient-level test: **not checked**. Supporting rank-zero systems,
Cartesian conditions, finite-singular maps and global Kummer images:
**not checked**. Sakamoto's Theorem 3.17 and Corollary 4.10 match the
strengthened construction/basis input; the other named results support
its conditions and comparison. None is claimed as a Mathlib match or
a rational rank-two theorem. No library absence inference is made.
