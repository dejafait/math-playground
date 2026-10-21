# Exact-G mod-seven containment — critical-audit source coverage

TARGET: Critically audit L083's mod-7 SL_2 containment over unchanged G, checking both actual finite-Galois restriction stages, full pointed torsion transport and the final subgroup direction.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step328 compared full L083 with the ready step326 application assessment, the relevant L073/L077/L078 canonical statements and proof passages, histories 326–327 and ATTEMPTS/034. Reused the recorded exact-statement, stronger-result and obstruction searches; unchanged source scope gives no reason for fresh external searches.
SOURCE_EVIDENCE: Reused the primary statements and essential proof cases inspected in step326: Milne FT v5.10 (September 2022), Theorems 3.10, 3.17(b,d), Propositions 3.19, 3.21, 7.4, pp.37–42,95; Conrad Simplicity of PSLn(F), undated nine-page version, Theorem 3.3/proof p.4; Milne EC second edition (2021), II Propositions 1.5–1.6 p.49 and Theorem 2.4(b) pp.52–53. No new source theorem is imported.
COMPARISON: The existing primary coverage includes every general mechanism used by L083, with restriction applied over Q and then F_aux separately. The audit may check exact image/kernel identifications, index divisibility, elementary orders, complete pointed equivariance and reversed subgroup inclusion; it requires no theorem about normality of G/Q or F'/Q.
GAP: Source coverage for the exact audit is ready. The independent mathematical audit of the complete specialization remains undone; no audit verdict or repair is made in this literature turn.
REASON: Complete the saved REVIEW_REQUIRED audit-scope comparison while reusing adequate primary coverage. Proceed next to the bounded mathematical audit rather than retrieving unchanged sources again.
SCOPE: Exactly TARGET for full L083 and unchanged L073 witness, L077 D,s,t,iota,F' and L078 G, in the same closure and embedding; no normal closure, new curve, normality verdict or full GL_2 assertion.

LITERATURE_REASON: The invocation-start audit target was REVIEW_REQUIRED, distinct from the already ready application target. This is its required source-scope comparison; no additional literature search on the ready application is undertaken.

## Source-scope comparison — step328

The main gap is still original finite B>=A. The intermediate target is
an independent critical audit of L083's full SL_2(F_7) containment over
the unchanged G. A reliable result could supply one initial-data
prerequisite; it cannot settle normality or the numerical comparison.

The reusable assessment is
`drafts/literature/2026-10-18-exact-legendre-mod7-large-image.md`.
Its primary-source readings, not a search snippet or model recollection,
provide the following coverage. The links identify the versions recorded
there; they were not freshly retrieved in step328.

- [Milne, Fields and Galois Theory v5.10](https://www.jmilne.org/math/CourseNotes/FT.pdf),
  Theorem 3.10, covers finite separable splitting fields. Theorem
  3.17(b,d) covers index/degree and normal-subgroup quotient statements.
  Proposition 3.19 assumes a Galois extension in a common field and
  identifies compositum restriction with the intersection-fixing group;
  its injectivity and surjectivity cases were inspected. Proposition
  3.21 and its intersection-normality proof cover two extensions Galois
  over the same base. Proposition 7.4 supplies embedding extension in a
  Galois extension, including the absolute restriction surjectivity used
  in this characteristic-zero closure. These are the general inputs
  for the two separate bases, not a transitivity theorem for normality.
- [Conrad, Simplicity of PSLn(F)](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf),
  Theorem 3.3, covers SL_2 generation by both elementary families over
  every field. The inspected proof includes the nonzero upper-entry,
  nonzero lower-entry and diagonal cases. The later audit must check
  order seven and Lagrange's theorem in the actual normal quotients;
  no simplicity or perfectness assertion needs to be added or reproved.
- [Milne, Elliptic Curves, second edition](https://www.jmilne.org/math/Books/EC2.pdf),
  II Theorem 2.4(b), covers the invertible pointed Weierstrass changes
  over their field of definition. II Propositions 1.5–1.6, including
  the inspected Picard-group proof and commuting group-law diagram,
  cover origin-preserving group maps. The audit must specialize these
  to the full geometric seven-torsion through both actual maps, with
  equivariance on both coordinates and the origin. Mere equality of
  image orders or x-coordinate fields would not meet that obligation.

L083 uses exactly those mechanisms. Its coordinate-kernel and absolute
restriction statements belong to the first source family; elementary
orders are an explicit finite check under the second; pointed transport
belongs to the third. The final absolute-subgroup direction is a check
of fixed-field definitions. Basis independence is a determinant check.
These elementary specialization checks warrant REPRODUCTION under
SPECIALIZE, not an IMPORT verdict for the exact combined claim. No
reproof of a cited general theorem is needed. This comparison approves
their scope, without performing the independent mathematical checks.

Essential local inputs remain the full L083, L073's same auxiliary
full Q-image and Galois degree divisibility, L077's D,s,t,iota,F' and
complete pointed maps, and L078's actual G subset F'. Their relevant
canonical passages were inspected to identify the obligations, without
reopening their already recorded audits. No old-curve L047 conclusion
is substituted; L047 is method context only. The duplicate screen in
step326 already distinguishes that result. ATTEMPTS/034 stops powers
of the recorded cyclic Frobenius as a normality separator, a different
mechanism; this audit neither reopens it nor makes a normality verdict.

The continuation test is the full exact chain, including both actual
restriction images, both normal quotients and their degree divisibilities,
and full pointed transport before the final inclusion. Continue if all
obligations survive. If any fails, isolate it and repair or narrow the
claim without changing G, changing the witness or using its normal
closure. This is a test for the later research turn, not today's verdict.

No essential source blocker remains. G/Q normality, mixed radical/
15-torsion information, other initial data, native input/action,
all-image factorization, pilot transport, essentiality and finite B>=A
remain independent unresolved obligations. Mathlib full matching and
supporting coverage remains unchecked, not absent. No lemma, script,
DAG or argument overview changes are warranted by this source review.
No mathematical exploration attempt is spent, and no progress beyond
the checked literature is claimed.

## Invocation-start proposal retained for provenance

The following proposal is superseded only as to its pending coverage
status by the SPECIALIZE comparison above. Its mathematical audit
remains pending.

This is a proposed continuation, not a completed literature comparison
or an independent mathematical audit. The next invocation is
literature-only until its coverage decision is ready. Reuse the
unchanged application assessment and its inspected primary sources;
new retrieval is needed only for an identified essential omission.
Do not repeat searches merely to approve the same known methods.

The main gap remains original finite B>=A. Auditing the new large-image
prerequisite would test its reliability for possible initial-data use,
independently of normality and the other missing bridges. Essential
inputs are L073's full auxiliary Q-image and Galois degree divisibility,
L077's same quadratic field and complete pointed maps, and L078's
actual G subset F'. L047 is context for the method, not an input about
this curve. Read only their relevant canonical passages and L083.

The later audit must check the actual coordinate-kernel identification,
absolute restriction surjectivity, each intersection's Galois base,
normal quotient and index divisibility, order-seven elementary
generators, both complete maps and their G_(F')-equivariance, basis
transport and G_(F') subset G_G. It must distinguish normality of
F'/F_aux from unproved normality of F'/Q or G/Q. Continue if the full
chain survives; isolate and repair or narrow any failed obligation
without changing the witness or replacing G by a normal closure.

Unresolved independently are G/Q normality and the mixed radical/
15-torsion kernel, other initial data, retained radical/scalar tests,
native input/action, all-image factorization, pilot transport,
essentiality and original finite B>=A. Both witnesses and all route
stops, including ATTEMPTS/034, remain intact. Full matching and
supporting Mathlib coverage is unchecked, not claimed absent.
