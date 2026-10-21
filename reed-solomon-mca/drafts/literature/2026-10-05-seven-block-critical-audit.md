# Coverage approval for the seven-block critical audit

TARGET: Critically audit L027's seven-block rank-28 certificate for every H-labeling of L025's family and its extension-field support exclusion.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the October 5 exact-pattern, arbitrary-evaluation, exterior-square and common-factor searches in the overlap-factor and arbitrary-label assessments; inspected L027's complete proof for scope and the relevant history/043–044 and ATTEMPTS/017–018; no fresh external search or rank test.
SOURCE_EVIDENCE: Reused Gandini arXiv:1810.11694v3 Theorem 1.1, Definition 7.1, Proposition 6.1 and Theorems 7.3/7.5; Boito–Ruatta SNC 2011 pp. 75–76, Proposition 2/Corollary 1 and diagonalization proof; Brakensiek–Dhar–Gopi arXiv:2310.12888v3 Definitions 1.2–1.3/6.1 and Theorems 4.1/6.4 with the previously inspected proof cases, as recorded in the ready assessments.
COMPARISON: The proposed audit checks an explicit certificate for the already assessed fixed-H full alternating-space matrix; characteristic-zero regularity, single-quotient gcd rank and generic column-span intersection theorems do not replace that certificate, and seven-block elimination introduces no essential unassessed source input.
GAP: Correctness of L027's quotient bases, exact successive kernels, nonzero coefficients and dependent-direction exclusion still requires a separate mathematical audit; other equality families and ABF26 correspondence remain unresolved.
REASON: The newly specified critical-audit continuation is within the prior theorem target and hypotheses; adequate existing coverage permits its separate mathematical invocation, without approving the proof or asserting originality.
SCOPE: Audit only L027's explicit seven-block certificate for L025's family under bijective labels in fixed H over every extension of F_97, using L010/L025/L026; no generalization, new family, label sampling or global fifteen-count claim.

## Reused primary-source coverage

The ready [overlap-factor assessment](2026-10-05-overlap-factor-universal-rank.md)
records the searches, precise theorem hypotheses and inspected proof portions.
The [arbitrary-label assessment](2026-10-05-cyclic-0125-arbitrary-label-rank.md)
records generic GM-MDS coverage and its earlier Lovett/BGM/Hall comparisons.
Their target evaluations and characteristic remain unchanged here.

Gandini, *Resolutions of ideals associated to subspace arrangements*,
[arXiv:1810.11694v3, June 24, 2019](https://arxiv.org/html/1810.11694v3),
Theorem 1.1 and Theorems 7.3/7.5 concern characteristic-zero linear
resolutions and regularity. They do not give the prescribed degree-two
span or justify reduction modulo 97. Boito–Ruatta, *Extended companion
matrix for approximate GCD*, SNC 2011, pp. 74–80,
[primary paper](https://www.csd.uwo.ca/~mmorenom/SNC-11-file-for-ACM/p74-Boito.pdf),
section 3.2 Proposition 2 and Corollary 1, assume an algebraically closed
field and squarefree monic f; multiplication by g on K[X]/(f) has
corank deg(gcd(f,g)). This single-quotient result does not establish
simultaneous exterior-square rank. No specialization or reproof is needed
because neither result is imported.

Brakensiek–Dhar–Gopi, *Generalized GM-MDS: Polynomial Codes are Higher
Order MDS*, [arXiv:2310.12888v3, June 4, 2025](https://arxiv.org/html/2310.12888v3),
Theorems 4.1/6.4 retain generic evaluations and column-span intersections.
The earlier assessment read the base cases and induction through Case 2
of Theorem 4.1 and the displayed power-series reduction for Theorem 6.4;
Case 3 and the full power-series proof were not inspected or used.
These generic conclusions do not certify all bijections to fixed H.
No theorem from this source is imported. The previously inaccessible
Busé–Khalil–Mourrain paper remains an unread, nonessential pairwise-resultant
lead, not evidence for this certificate. No new essential source blocker
is identified. Failed searches do not establish novelty.

## Scope comparison, duplicates and recorded failures

L027's full text was read to identify its technique and claimed scope,
not to perform the mathematical audit. It replaces polynomial-factor
propagation by quotient maps on the same moment space, still testing all
28 alternating coordinates. Its claim concerns the first seven blocks
of L026's full matrix and every extension; it does not introduce generic
evaluations, a decomposability restriction or an additional source theorem.
The only inputs named in the proof are L010's moment independence,
L025's supports/disjoint pair and L026's annihilator identification.
The ready overlap assessment already inspected their relevant arguments.
Their complete load-bearing arguments must be checked during the audit.

L026's cyclic and 4096 sampled-label cases are partial duplicates, not
uniform proof evidence. ATTEMPTS/018 preserves the earlier cyclic scope;
ATTEMPTS/017 preserves the failed six-edge/eight-vertex criterion.
L024's different two-block family and L022's fixed triple do not supply
this exclusion. No historical stop is reopened and no sample batch is
proposed. L027's proof needs checking because a new explicit certificate,
rather than an imported matching theorem, carries the universal claim.
Mathlib coverage of the full rank/exclusion theorem remains not checked;
this review neither claims absence nor supplies Lean verification.

## Approved audit and discriminating test

The exact TARGET is approved as EXPLORE for one separate proof-audit turn.
Essential inputs are L010, L025, L026 and L027. Check the quotient-map
identification on the entire exterior square, all twelve initial pairs,
every quotient basis and nonzero expansion coefficient, and equality of
the kernels with dimensions 12, 8, 4, 2 and zero. Check extension-field
validity and the independent dependent-direction contradiction using
full-weight errors and the disjoint pair. No genericity, label symmetry,
finite sample or decomposability may substitute for those checks.

Continue with an audited partial family exclusion only if every
load-bearing assertion and direct input survives. A failed inference
requires its precise location and mathematical evidence; retain the
original proof and correct it within this target if possible. An
unrepairable failure stops the claimed certificate and requires a new
reviewed target. Missing essential source coverage must be recorded
rather than silently assumed. Neither audit outcome proves the global
fifteen bound, settles other families or identifies the pinned model
with ABF26. This literature step derives no result and approves no
mathematical correctness claim.
