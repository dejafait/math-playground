# Kato auxiliary-prime relations and the mixed determinant component

TARGET: Test whether auxiliary-prime Kolyvagin relations for Kato's cyclotomic Euler system exclude L013's nonzero mixed rational/Sha determinant component, without assuming finite p-primary Sha.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed the thirteen queries recorded below; followed primary Kim, Castella--Sano, Burns--Sakamoto--Sano and Sakamoto sources, including the finite-singular relation, local conditions, exact structure statements and rank-zero alternative. No full rational-determinant exclusion was located in this bounded review.
SOURCE_EVIDENCE: Kim, https://arxiv.org/html/2203.12159v6 and https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf, Sections 2.1--2.4, Theorems 1.8/1.10/2.5/2.13/3.11/6.1; Castella--Sano, https://arxiv.org/html/2601.14504v1, Theorems A/B/2.1.3/2.1.4 and Proposition 2.3.1; Burns--Sakamoto--Sano, https://arxiv.org/pdf/1902.07002v1, Sections 6.1/6.4 and Theorems 6.11/6.14 with scope/proof passages; Sakamoto, https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf, Definition 5.1, Theorems 5.5/5.8 and Remark 5.9. Exact read scope is distinguished below from unread leads.
COMPARISON: The inspected auxiliary-prime structure and primitivity results concern Selmer groups, their divisible corank and finite quotients. Kim's rational-rank conclusions retain finite Sha or trivial Sha[p]; newer primitivity and determinant statements do not replace these with rational exterior-square membership. The actual Kato family uses p-relaxed and auxiliary transverse conditions, not a family of global rational Kummer classes.
GAP: No inspected theorem excludes the mixed rational/Sha component of the augmentation determinant preimage under the retained hypotheses. Whether L013 extends to all arithmetic auxiliary-prime relations remains untested; absence of an import is not a proof of such compatibility.
REASON: Stop the direct rational-determinant import from the checked structure/primitive-system theorems; specialize only the explicit correction/local-condition test covered below, citing the known results without reproof. Preserve the original arithmetic exclusion target and do not assume finite Sha, rank two or a leading-term conjecture.
SCOPE: The covered test retains non-CM E/Q, good ordinary p >= 5, surjective E[p], Manin constant and Tamagawa factors prime to p, and E(Q_p)[p] = 0. It additionally assumes a minimal nonzero mod-p Kurihara index with two prime factors; this is not inferred from analytic order two or Selmer dimension two. A whole-family test must retain coefficient reductions, auxiliary transverse conditions and every finite-singular relation; an isolated finite-level class is not the integral system in Kim's Theorem 2.5.
COVERED_TARGET: Test whether compatible rational Kummer corrections of Kato's auxiliary-prime Kolyvagin family can preserve every finite-singular relation, make all components finite at p, and retain a nonzero mod-p class at a minimal two-prime Kurihara index.

## Original target and required threshold

This file began as REVIEW_REQUIRED in the preceding mathematical turn.
The exact TARGET is preserved; the completed source comparison now
approves only the listed subtarget. No calculation, correction, extended
model or rationality theorem is constructed in this literature turn.

The main gap remains rank E(Q) = m(E) for arbitrary analytic order
m(E) >= 2. On the conditional dimension-two branch, the known upper
bound is r <= 2; two rational Kummer directions, not two Selmer
directions, are needed for the lower bound. A rational leading vector
already occurs in L013 and falls short of that threshold.

Retain the cyclotomic, non-CM, good-ordinary p >= 5 setting and the
conditional dimension-two Selmer branch. Keep rational rank, finite
p-primary Sha and rational determinant membership unproved. Hypotheses
on residual images, auxiliary primes and primitivity must be recorded
from actual source statements rather than inferred from the scalar
characteristic equality already met by L013.

The proposed arithmetic constraint must exclude the mixed component
of the determinant preimage. Rationality of the contracted leading
vector alone is insufficient, since it already holds in L013. An
implication to Selmer dimension two or the cyclotomic main conjecture
also does not exclude the model. A source that assumes finite Sha,
rational rank two or the conjectural rational leading-term formula
would not supply the missing implication under the retained hypotheses.

The completed review below concerns these actual relations and their
known consequences. The follow-up tests a correction of actual
auxiliary classes, rather than repeating the determinant model or the
parked Eisenstein source retrieval. Uniform production from m(E) = 2,
actual derivative degree/nonvanishing and higher ranks remain separate
unresolved steps.

## Primary theorem comparison, 2026-10-03

**Kim.** *The structure of Selmer groups and the Iwasawa main conjecture
for elliptic curves*: the accessible publisher-hosted author PDF is
dated 2025-05-12; the arXiv record identifies v6, 2025-05-14, as the final
version. Both were inspected; no identity of the files is assumed.
[Theorem 1.8, PDF page 7](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7)
identifies the first nonzero Kurihara index with Selmer corank and gives
the finite quotient's structure. Its rational-rank clause adds finite
p-primary Sha. [Theorem 1.10, PDF page 8](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8)
gives auxiliary localization for mod-p Selmer; its rank clause adds
trivial Sha[p]. The displayed surjectivity, Manin, local-torsion and
Tamagawa hypotheses were read.

[Sections 2.1--2.4, PDF pages 11--14](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=11)
specify p-relaxed conditions and transverse conditions at primes
dividing the index. The finite-singular relation is equation (2.1),
on page 12. Theorem 2.1 retains cyclic Frobenius quotient and injectivity
hypotheses. Theorem 2.5 contrasts a zero classical rank-one system
module with the free rank-one canonical module. This is about complete
systems, not each isolated class. Proposition 3.10 and
[Theorem 3.11, PDF pages 19--20](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=19)
give the torsion dual-exponential construction and its Kurihara value;
the normalization includes p^t, with p^t = #E(Q_p)[p^infinity].

Also read Theorem 2.13/Corollary 2.14 (page 16), Proposition 3.14
(page 21), Theorem 5.1 and the corank proof's strategy, and
Theorem 6.1/Corollary 6.3 with the localization proof (pages 32--33).
These supporting reads do not yield a rational-point lattice.
Corollary 1.12 asserts **Selmer** parity, not rational-rank parity
without an additional Sha argument. Never identify the auxiliary
index, complex vanishing order and cyclotomic derivative degree.

**Castella--Sano.** *On refined nonvanishing conjectures by Kurihara and
Kolyvagin*, [arXiv:2601.14504v1](https://arxiv.org/html/2601.14504v1),
2026-01-20. Freshly read Theorems A/B, Section 2.1.1's actual Kato
families, Theorems 2.1.3/2.1.4, and Sections 2.2--2.3.1.
Surjective E[p] and Manin constant prime to p remain explicit. Theorem A
equates the refined modular-symbol divisibility index with the
cyclotomic main conjecture; Theorem B supplies the ordinary case.
Theorem 2.1.3 retains the local-torsion factor. Theorem 2.1.4 and
Proposition 2.3.1 require nonzero specialized leading class for their
finite strict-Selmer conclusions. They do not assert that those
conclusions persist at the trivial character when that class vanishes.
The determinant statement concerns the global cohomology complex,
without identifying its augmented determinant with rational points.

**Burns--Sakamoto--Sano.** *On the theory of higher rank Euler, Kolyvagin
and Stark systems, III: applications*,
[arXiv:1902.07002v1](https://arxiv.org/pdf/1902.07002v1), 2019-02-19.
Read Section 6.1's opening, Section 6.4's scope,
[Theorem 6.11 and Theorem 6.14, PDF pages 42--43](https://arxiv.org/pdf/1902.07002v1#page=42),
and the relevant proof comparisons in Section 6.4.3. Section 6.4
continues the finite-Sha assumption. Theorem 6.11's inclusion is in
strict-Selmer Fitting ideals; its equality clauses additionally assume
BSD_p(E/Q) and the stated Perrin-Riou conditions. Theorem 6.14 retains
these and further analytic identities. These arithmetic conclusions
cannot be imported as an unconditional Sha exclusion here. The broader
higher-rank machinery is not rederived or fully audited in this review.

**Sakamoto.** *On the theory of Kolyvagin systems of rank 0*,
J. Théor. Nombres Bordeaux 33 (2021), 1077--1102, published 2022-01-26.
Read [Definition 5.1, printed pages 1088--1089](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=13),
Theorems 5.5/5.8, Remark 5.9 and Theorem 6.3. Rank-zero systems use
components indexed by (n,q), with an extra relaxed prime and extra
relations. Under the source's Cartesian/core-rank-zero and Galois
hypotheses they form a nonzero module and control dual-Selmer Fitting
ideals. They are different objects from the classical rank-one system
in Kim's zero-module statement. No vanishing assertion about these
rank-zero systems or rational-point conclusion is imported. Their
full prerequisites are not verified as new arithmetic inputs here.

**Official scope.** Reopened the current Clay problem page and
[Wiles's statement, printed page 2](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=2).
The rank assertion and separate stronger refinement agree with the
existing target foundation; no scope change is made.

## What the comparison does and does not decide

The direct theorem import fails at an explicit finiteness premise,
not merely because a search did not return an exact title. Selmer
corank and finite-quotient information leave the marked rational
subspace unidentified. Primitivity adds arithmetic information to
the raw family, but the inspected statements do not translate it into
the required two rational directions. This is an informative source
scope rejection; it is not a new arithmetic theorem or a BSD disproof.

In particular, L013 has **not** been extended to a genuine Euler or
Kolyvagin system. No conclusion that all auxiliary relations permit
its marking is proved. Conversely, a theorem restricting a whole
family does not by itself settle the rationality of a single
augmentation determinant. The original TARGET remains unresolved.
The source comparison stops importing a rational certificate from
these structural statements; it does not stop research on BSD.

## Approved next application and stop test

The exact COVERED_TARGET asks whether a specific extraction mechanism
can turn auxiliary-prime information into rational classes. Work with
corrections coming from the rational Kummer images at every relevant
coefficient level, compatible under reduction. Check p-finiteness,
transversality at every index prime and all finite-singular equations,
not only the value of a single scalar. Retain the nonzero mod-p
two-prime Kurihara value as an **additional test premise**, never as
something obtained here from m(E) = 2.

Import Kim's Theorem 2.5 and the reciprocity map by citation. The
remaining work is their applicability to the proposed corrections:
track the singular localization of corrected components and determine
whether they would constitute a classical rank-one system. This
test is an application of known results, not a reproof or a novelty
claim; no new lemma is required if citations and a short applicability
argument suffice. The non-anomalous condition removes the source's
local-torsion ambiguity for the mod-p test.

Continue this extraction only with a nonzero compatible family passing
the stated local conditions. A forced zero family, a persistent
p-singular component, or failure of a finite-singular equation stops
this correction mechanism. If it fails, preserve the obstruction and
choose a mechanism that changes the arithmetic construction or its
relations; do not repeat L013 or rename a point correction. Even
success would leave the actual determinant comparison and production
from analytic order two open. Rejection of this stronger mechanism
would not be a proof that the original determinant target is false.

## Search and access record

Queries actually issued on 2026-10-03:

- `Kato Euler system Kolyvagin relations finite singular comparison Selmer corank Kurihara numbers rational rank Sha`
- `Mazur Rubin Kolyvagin systems theorem 5.2.10 Tate Shafarevich rank Kato`
- `Castella Sano refined nonvanishing Kurihara Kolyvagin 2601.14504`
- `"Kolyvagin systems" Mazur Rubin math.uci.edu pdf`
- `"The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves" Kim`
- `"Kato" "Kolyvagin" "divisible" "Shafarevich"`
- `"Kato" "Kolyvagin" "rational points" "rank" Kurihara`
- `"Euler and Kolyvagin systems of rank 0 and the structure of Selmer groups"`
- `"Kato" "Kolyvagin" "Kummer" "Sha"`
- `"Kato" "Kolyvagin" "finite singular" "rational"`
- `"Kolyvagin systems" Mazur Rubin "ks.pdf"`
- `"Kolyvagin systems" "mazur" "pdf" site:math.harvard.edu`
- `"Euler and Kolyvagin systems of rank 0" Kurihara Sakamoto pdf`

Primary text, rather than search snippets, supports the comparisons.
Kim's HTML drops some diagram entries; the publisher PDF was read for
the local-condition, reciprocity and localization statements. All
source versions and page numbers above refer to the inspected files.
The earlier Sano/BKS descent assessment and L013 are reused; their
determinant calculation was not repeated.

The original Mazur--Rubin monograph was not retrieved from the attempted
author URLs. Its theorem numbers are reported through Kim's inspected
Theorem 2.5 proof, which cites MR Theorems 4.2.2/5.2.10 and Proposition
6.2.2; they are not claimed as freshly read original pages. Kim's
explicit primary statement supplies the covered test's needed input.
The author introduction URL also failed. The BSS arXiv record lists
v1; an attempted v3 HTML address was invalid and was replaced by v1.
The incorrect Keio host was replaced by Kurihara's accessible primary
website; no repeated source blocker remains for the approved test.

Kurihara--Sakamoto's cited 2026 preprint and Angurel's
arXiv:2504.20759 were discovery leads, not inspected theorems or inputs.
The former was found in references and a seminar announcement, without
a retrieved primary text. No claim that it adds or lacks a rationality
result is made. These leads do not replace the sources read, and the
next narrow application does not depend on them. No exhaustive-search
or novelty claim follows from this review.

## Mathlib

Full coverage of the arithmetic mixed-component exclusion: **not checked**.
Supporting Euler/Kolyvagin systems, finite-singular comparison maps,
torsion dual exponentials and rational Kummer membership: **not checked**.
The named primary theorems above support structure, local conditions
and the covered application; none is asserted to match the full TARGET
or to be a Mathlib theorem. No absence inference is made.
