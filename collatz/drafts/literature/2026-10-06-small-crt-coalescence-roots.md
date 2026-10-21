# Small CRT representatives for a larger coalescence clock — scope reviewed

TARGET: Assess whether for every real B>=0 there are infinitely many integers L>=6 admitting n with 4^L<n<=6^(L-B), n congruent to 47 modulo 3^(L+4), and 81n+97 congruent to 0 modulo 2^(L+1), as a route to obstructing both coalescence clocks log(n)/log(6)+B.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-congruence, small-CRT, inverse-power and diagonal growing-modulus searches found no matching inspected theorem; primary CRT, fixed-prime-power distribution and modular-inverse interval statements were compared below, with inaccessible leads distinguished.
SOURCE_EVIDENCE: Read Ben Lynn's named CRT theorem and full proof; Merai–Shparlinski arXiv:2302.03964 Theorems 1.1–1.2, definitions and short-range proof boundary; Garaev–Shparlinski arXiv:2304.07953v1 Theorems 1.1–1.4 and proof of 1.1; Korobov's fixed-denominator setup and Theorem 5 passage, with OCR limitations. Reused audited L028's hypotheses and CRT-selection passage.
COMPARISON: CRT supplies the existing class of modulus 162*6^L, not the requested small representative; inspected distribution results average many indices at a fixed modulus and do not establish hits of this prescribed diagonal sequence. The prime-modulus inverse results also have different modulus and input hypotheses.
GAP: The exact infinitely-many-L assertion for every B>=0, including strict n>4^L, remains unproved and unrefuted; no distribution or small-height theorem for these roots is imported.
REASON: Completed exact-target scope comparison permits one bounded mathematical attempt using known CRT arithmetic while retaining the infinite-hit question as an independent unresolved input; failed searches do not establish novelty.
SCOPE: Only the unchanged exact TARGET: fixed congruences, all real B>=0, infinitely many L and strict n>4^L. One later attempt may derive and check the exact representative recurrence and test whether it forces infinitely many suitable heights or a rigorous obstruction. Finite diagnostics may use 6<=L<=256, but cannot settle the infinite assertion. No enlarged ancestor search, changed anchor, global convergence claim or assumed equidistribution.

## Proposed use and discriminating review

The main gap remains universal eventual descent. Essential local inputs
for the proposed continuation are audited L028 with L026's retained
anchor proof and L025's offset estimate through L026. They are not being
reproved or applied in this turn. The unresolved input is selection below
the stated smaller upper threshold for infinitely many L. Both actual
paths, zero clocks and strict order against the original root remain
mandatory in any later coalescence application. Divergence and convergence
of every residual root remain independent gaps.

A successful selection result could obstruct a larger full-height
coalescence clock than the endpoint result. A rigorously established
lower bound for these normalized representatives could instead stop this
specific extension. The completed comparison below authorizes one
separate mathematical attempt, not the proposed selection assertion.
General CRT existence alone does not give the required small height.
An empty finite sample, or a density heuristic for inverse residues, is
not a uniform conclusion. No calculation was performed in this review.

Attempt 016 stops the covered smaller coefficients; its later endpoint
decision records L028's completed audit. Neither is a global ban on
larger clocks. Attempts 017 and 019 concern other stopped mechanisms;
this target does not reuse carry-boundary forcing or cycle-boundary guards.
No novelty conclusion is claimed. Mathlib coverage for the full
small-representative target is not checked.

## Completed source comparison, 2026-10-06

The notebook-scoped status inspection found existing unfinished changes;
they are preserved. Read L028's hypotheses and CRT-selection passage,
Attempt 016 in full, history 049 and 058, and the target/conventions
foundation. Targeted searches of the older residue-47 assessments and
Attempts 014–015 found no small-representative distribution assessment.
The endpoint audit is ready and is not repeated. The stopped cycle and
carry mechanisms do not supply a representative-height obstruction.

The [MathPrize page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07 and retrieved 2026-10-06, still states that every
positive integer reaches 1 under the map n/2 for even n and 3n+1 for
odd n. This agrees with the exact local target; prize rules are separate.

[Ben Lynn, *The Chinese Remainder Theorem*](https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html),
the named theorem and full proof, web lines 59–65, requires coprime
positive moduli and gives one solution class modulo their product.
Here the powers of 2 and 3 are coprime and 81 is invertible modulo the
power of 2. This covers L028's existing CRT step. Its standard theorem
has no prescribed smaller representative conclusion. No reproof is needed.

[L. Merai and I. E. Shparlinski, *Distribution of recursive matrix
pseudorandom number generator modulo prime powers*](https://arxiv.org/pdf/2302.03964),
arXiv:2302.03964, retrieved PDF, pp. 3–5, Theorems 1.1–1.2 and
definitions: the modulus p^t is fixed within each sequence. The first
theorem requires a nondegenerate characteristic polynomial, no multiple
roots modulo p, a constant coefficient prime to p and a proper vector
pair. The discrepancy theorem requires nondegeneracy, irreducibility
modulo p and a p-primitive initial vector; both range over 1<=N<=tau_t.
Their useful short-range scale is exp(c*(t log p)^(2/3)). Read also
Section 4.1 and the opening of 4.2, p. 13: the scalar case is delegated
to Korobov and the proof discards a trivial short range. These statements
do not count diagonal points with changing modulus. The displayed
log(d) denominator is not silently specialized to d=1. No application
or discrepancy estimate for the target is claimed.

[M. Z. Garaev and I. E. Shparlinski, *On the distribution of modular
inverses from short intervals*](https://arxiv.org/html/2304.07953v1),
arXiv:2304.07953v1, 2023-04-17, Sections 1.1–1.3 and 3.1, were read.
The inputs are inverses of x=1,...,N at a prime p>N. Theorem 1.1
says that for each fixed A>1 and sufficiently large N there exists
p with (log p)^A comparable to N and discrepancy bounded below by
a positive constant. Its proof chooses p=-1 modulo a tailored least
common multiple and exhibits many small inverses. This is an actual
obstruction to treating arbitrary inverse intervals as uniformly random;
it neither refutes nor proves the present prime-power diagonal target.
Theorems 1.2–1.4 keep the prime/interval framework. No such result is
imported for the fixed congruences here.

[N. M. Korobov, *On the distribution of digits in periodic fractions*](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&paperid=3253&what=fullteng),
Math. USSR-Sbornik 18(4), 659–676, DOI
10.1070/SM1972v018n04ABEH001870, English translation copyrighted 1974:
read the setup, pp. 659–661, and Theorem 5/proof passage, pp. 675–676.
The counted digit blocks range over P consecutive positions of one
fixed rational a/m, with base q coprime to m and P at most its period.
The prime-power theorem additionally restricts r through P^r=p^alpha
and valuation parameters. OCR damages its numerical constants and
error exponent; screenshots did not yield a readable replacement.
It is therefore not imported or claimed fully extracted. The readable
fixed-fraction counting setup suffices to distinguish this lead from
the prescribed growing-modulus target, without using the damaged bound.

## Search record and unread leads

Queries included the exact strings `"81n+97" "47" Collatz`,
`modular inverse powers 3 modulo 2^n distribution inverse 3^n`,
`diagonal residues 3^n modulo 2^n equidistribution`,
`small Chinese remainder representatives powers 2 3 Collatz`,
`"small CRT" "representatives" powers distribution`,
`"3^{-n}" "2^n" distribution`,
`"diagonal" "modular inverses" "powers" distribution`, and
exact title searches for Shparlinski (2014) and Korobov.
The exact congruence searches gave no inspected matching result.
No conclusion about originality or the nonexistence of a theorem follows.

Shparlinski (2014), *Distribution of exponential functions modulo a
prime power*, J. Number Theory 143, 224–231, DOI
[10.1016/j.jnt.2014.04.010](https://www.sciencedirect.com/science/article/pii/S0022314X14001498),
remains an unread theorem-level lead. Its publisher abstract and the
author's publication listing were inspected; the article body was
inaccessible through the publisher and bounded title/author searches
found no primary full-text copy. No bound or applicability claim is
attributed to it. Its exact theorem is not essential to a bounded
elementary CRT attempt, since no application of it is proposed.

The MathOverflow inverse-power question 408125 was used only to find
Korobov and Shparlinski references, not as theorem evidence. Search
results concerning positive powers (3/2)^n, fixed-modulus balancing
sequences and nonprimary Collatz claims were not used as inputs.
Positive powers are not assumed to have the same distribution as the
required inverses. No Woods access work was reopened.

## Gate and bounded continuation

DECISION EXPLORE permits the unchanged target's first mathematical
attempt. Essential elementary arithmetic is covered by named CRT and
the existing audited L028; the sources checked do not settle the extra
height condition. A later proof must establish the quantifiers for
every B, an infinite set of L and the strict lower guard independently.
Do not derive a selection assertion from pseudorandomness, a shrinking
density heuristic or finite successful residues. A finite diagnostic,
if useful, must save every tested representative, both original
congruence checks and actual/required bounds under scripts/ in a later
research turn; no such program or certificate exists from this turn.

Continue if an exact recurrence yields a checkable infinite-hit
mechanism or a rigorously bounded obstruction worth testing. Abandon
this particular distribution mechanism if it only rephrases CRT or
depends on an unproved equidistribution hypothesis; retain the exact
target as unresolved rather than declaring it false. A proof of a
lower normalized-height bound could stop the proposed extension, but
an empty finite screen cannot. The existing exploration limits apply
without a counter reset. All later coalescence use must retain L028,
L026 and L025's inherited guards. Universal descent and other orbit
languages remain independent gaps. Full Mathlib coverage is not checked.
