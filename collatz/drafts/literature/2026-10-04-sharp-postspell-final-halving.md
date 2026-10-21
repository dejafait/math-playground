# Sharp postspell final-halving criterion: completed assessment

TARGET: Derive a sharp affine criterion for original-root descent after an actual residue-20 prefix (OOEO)^J O^H E^a with J>=2, H>=3, a congruent to 2 modulo 18 and a<e(J,H), and test whether such guarded excursions exist, retaining every integer and parity guard.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six exact-statement, terminology and general parity-descent queries executed on 2026-10-04; directly inspected the closest postspell note and Rozier–Terracol v2, with queries and scope below.
SOURCE_EVIDENCE: Read Sodelin, Postspell_Guarded_Root_Descent.md, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, sections 1–5, and Postspell_Odd_Run_Obstruction.md, node AC-POSTSPELL-ODD-RUN-OBSTRUCTION-001, statement and proof through scope; read Rozier–Terracol, arXiv:2502.00948v2 (2025-02-13), equations (1), (2), (8), (9), Theorem 2.2 and Theorem 4.1 with proofs.
COMPARISON: Exact guarded affine identities and parity-residue construction are covered; the inspected postspell size theorem requires a>=J+H, while the saved target changes that hypothesis. General coefficient/remainder comparison is known, so only its explicit parameter specialization and actual guarded realizability below the existing threshold merit work.
GAP: A sharp parameter/root criterion and an actual improving lower-threshold excursion have not been established locally or matched to a full theorem in the sources inspected; all-root entry and failed-guard compensation remain unresolved.
REASON: Complete the changed-hypothesis review and approve a separate bounded specialization of known arithmetic, without reproof of general parity coding or a novelty claim.
SCOPE: Positive shortcut roots congruent to 20 modulo 27, actual words (OOEO)^J O^H E^a, J>=2, H>=3, nonnegative a congruent to 2 modulo 18 below e(J,H); retain positive offsets, all input parities and original-root order. No universal final-even guard is covered.

## Hypotheses

The TARGET is unchanged from step 027. The main gap is universal eventual
descent; this intermediate target could sharpen a conditional exclusion
at the same least residue-20 root. It need not resolve later entry or
compensation before being tested. This turn is LITERATURE only: no new
formula, witness, lemma or program is derived.

## Conclusion

The next mathematical turn is ready under SPECIALIZE. Its exact affine
criterion should be reported as a reproduction/specialization of known
machinery, not an original general descent theorem. Whether any genuine
improvement exists remains a calculation question. This review is
EXPLORATION: source comparison is completed, but it supplies neither a
new mathematical input nor a new obstruction to the sharpening.

## Proof

This section records source statements and applicability, not a proof
of the proposed sharpening.

### Closest matching source

Sodelin, [*Guarded root descent after independently unbounded return spells
and odd runs*, sections 1–5](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
node `AC-POSTSPELL-GUARDED-ROOT-DESCENT-001`, supplies the actual-iterate
identities y=(27/16)^J(r+23/11)-23/11 and z=(3/2)^H(y+1)-1.
Its sufficient margin assumes a>=J+H and divisibility by 2^a. Section 2
proves unique parity-residue recursion and CRT realization; section 3
supplies residue-20 target membership. Section 4 gives a growing example
with J=2,H=3,a=2, despite correct parities and endpoint residue. The
threshold is expressly not optimal. Section 5 distinguishes prose proof
from finite checks and pending Lean formalization.

The companion [*Fixed-length return spells can be followed by arbitrarily
long further growth*](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Odd_Run_Obstruction.md),
node `AC-POSTSPELL-ODD-RUN-OBSTRUCTION-001`, gives independently unbounded
odd runs and infinitely many insufficient-even exits. These are
obstructions to universal guard satisfaction, not a sharp criterion
for each lower exponent.

Both notes were inspected from live main on 2026-10-04 (199 and 132 web
lines); no immutable revision was obtained. The essential finite-spell
input and its proof already have adequate coverage in
[the prior assessment](2026-10-04-residue47-bounded-ancestor-cover.md).
Reuse that coverage; no unread essential source blocks this target.

### Published supporting comparison

Rozier and Terracol, [*Paradoxical behavior in Collatz sequences*,
arXiv:2502.00948v2, 13 February 2025](https://arxiv.org/html/2502.00948v2),
equations (1)–(2) and (8)–(9), use the same shortcut convention.
They write the iterate as Cn+E and characterize the contracting-coefficient
but non-descending case by 0<1-C<=E/n. Thus a coefficient below one alone
is insufficient. Theorem 2.2 bounds the remainder for fixed length and
odd count; Theorem 4.1 bounds it using the harmonic mean of the odd
states. Their proofs and the parity-congruence paragraph before Theorem
2.2 were read. These support exact comparison and guards; they do not
state this postspell specialization or guarantee the saved lower-tail
improvement. Their universal conjectures are not imported as theorems.

### Bounded next test and redundancy

Use the cited exact identities rather than reprove parity-word theory.
The difference to calculate is the full original-root inequality at the
saved lower exponent, followed by intersection with actual parity and
residue guards. A formal rational endpoint or an asymptotic slope alone
will not suffice. The exponent denotes available E steps; it need not
be the maximal even run unless that extra guard is stated.

A discriminating test is an actual positive residue-20 source with the
specified lower tail ending strictly below its unchanged root. For a
bounded initial screen use 2<=J<=12 and 3<=H<=12, testing all eligible
nonnegative a below e(J,H) with exact arithmetic and parity-residue/CRT
coding. No screen is executed here. If an improvement exists, record its
precise parameter and root restrictions; if none is found, distinguish
that finite negative screen from an all-parameter impossibility. An
exact impossibility criterion would stop this sharpening. This is one
specialization task, not a new unbounded excursion project.

L019 already imports the sufficient guard; repeating it would add
nothing. L005 covers complete-block words, whose endpoints have different
conventions, so use it only as background. Attempts 009–011 retain their
parked/stopped evidence; this comparison reopens none of those routes.
The calculation counter is unchanged, and this review resets none.

### Searches and limits

Queries executed on 2026-10-04:

- Collatz "postspell" "sharp" halving
- Collatz "OOEO" "descent"
- Collatz parity vector affine formula stopping time Terras
- site:github.com/Sodelin/Collatz-Conjecture-Work "sharp" "postspell"
- Collatz "final" "halving" "root" descent "OOEO"
- Collatz "sharp affine" descent parity

Repository indexes and other search hits were discovery leads, not
additional theorem evidence. The Niu 2026 parity-vector note was an
unread nonessential lead; no claim depends on it. Reuse the existing
inverse-word literature assessments where unchanged. This bounded
search establishes no priority or exhaustive absence claim.

The primary [MathPrize target](https://mathprize.net/posts/collatz-conjecture/)
was rechecked; its universal positive-integer statement still matches
local GOAL.md. Shell fetching failed on DNS, but the browser exposed the
essential statements and proofs; this is not SOURCE_BLOCKED.

## Mathlib

Full sharp postspell criterion and supporting affine-word arithmetic:
**not checked**. No library absence, matching declaration, or novelty is
asserted. External pending Lean work is not Mathlib coverage.
