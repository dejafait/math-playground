# Growing-only postspell chains: completed scope assessment

TARGET: Compute exact minimum positive residue-20 roots realizing K consecutive growing postspell words (OOEO)^J O^H E^2 for K=1,...,5 and 2<=J<=4,3<=H<=5 using joint parity/CRT coding, and test a uniform initial-size lower bound for the full J>=2,H>=3 alphabet against L005 and L008's prior failures.
CHECKED: 2026-10-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Seven changed-scope queries on 2026-10-04 covering restricted parity itineraries, positive-integer realizability, conjugacy and exact postspell terminology; search record and evidence limits below.
SOURCE_EVIDENCE: Bernstein–Lagarias, The 3x+1 Conjugacy Map, author PDF dated 19960215, section 1 pp. 1–3, equations (1.1)–(1.6) and Periodicity Conjecture; Rozier–Terracol arXiv:2502.00948v2 (2025-02-13), Definition 2.1, Lemma 2.1, paragraph preceding Theorem 2.2, Theorem 2.2 and proof, Lemma 2.3 and coding paragraph in its proof; prior Sodelin sections 2–3 coverage reused.
COMPARISON: Arbitrary finite-word parity coding is covered and should be imported; no inspected statement supplies the uniform positive initial-root lower bound for arbitrary growing postspell chains, and 2-adic conjugacy does not supply positive-integer realization or exclusion.
GAP: Compute exact finite-chain minima and seek an all-parameter arithmetic estimate diverging with K; the bounded nine-word screen alone cannot control unbounded J,H or arbitrary aperiodic chains.
REASON: Approve the unchanged bounded target as exploration of the uniformity gap, reusing finite coding rather than reproving it; no essential unread source blocks this test and no novelty is claimed.
SCOPE: Positive residue-20 roots; actual input parities and positive affine offsets; nine-word alphabet 2<=J<=4,3<=H<=5 for K<=5, distinguished from the full J>=2,H>=3 alphabet. No first-return claim; no exact final even-tail maximality unless a following odd input is imposed.

## Hypotheses

The TARGET is unchanged from the checkpoint. The main gap is universal
eventual descent on the domain surviving L014–L021. The intermediate
question is whether growing-only postspell chains force an initial-size
cost increasing without bound with chain length, uniformly over their
parameters. Such a result could exclude an infinite chain of these words.
Entry into this class, other even tails and general compensation would
remain unresolved.

This completed step is LITERATURE / EXPLORATION. It performs no new
mathematical derivation, parameter calculation or script execution. It
uses no mathematical exploration turn and supplies no new lemma.

## Conclusion

EXPLORE is ready for the exact saved action. The finite calculation is
a specialization of known coding. The uniform bound is an uncovered
restricted target in this checked literature, not an established result
or a novelty claim. Report covered finite arithmetic as reproduction;
qualify any additional uniform estimate separately against these sources.

## Proof

This section records a source comparison, not a proof of the target.

### Primary results inspected and their scope

Bernstein–Lagarias, [*The 3x+1 Conjugacy Map*, author PDF dated
15 February 1996](https://websites.umich.edu/~lagarias/doc/bernstein.pdf),
section 1, pp. 1–3: the same shortcut map is conjugate to the shift on
Z_2. Equations (1.3)–(1.5) give the conjugacy, its congruence compatibility
and the inverse parity-series formula; the introduction states that
reduction modulo 2^n gives a permutation. Read the uniqueness argument
following (1.4), both coding formulas and the rational/positive-integer
qualifications surrounding the Periodicity Conjecture. That conjecture
is explicitly unproved. These statements support finite coding and
explain why infinite symbolic compatibility cannot certify a positive
integer survivor. They provide no real-size bound for this restricted
language. The paper studies iterates of the conjugacy itself, distinguished
on p. 3 from iterates of T; its conjugacy-cycle conclusions are not orbit
escape theorems. This is supporting coverage, not a full match.

Rozier–Terracol, [*Paradoxical behavior in Collatz sequences*,
arXiv:2502.00948v2, 13 February 2025](https://arxiv.org/html/2502.00948v2),
section 2: Definition 2.1 fixes input parity vectors; the paragraph before
Theorem 2.2 identifies equal vectors with congruence modulo 2^j, and
Lemma 2.3's proof gives unique realization in 1,...,2^j. Lemma 2.1 and
Theorem 2.2 order and bound the affine remainder for fixed length and
odd count. These are remainder bounds, not lower bounds on the minimum
positive root over a variable-length language. Their averaging conclusion
does not exclude exceptions. Reuse finite coding; neither theorem matches
the required uniform root estimate.

The [completed two-excursion assessment](2026-10-04-two-postspell-compensation.md)
already inspected Sodelin,
[*Postspell_Guarded_Root_Descent.md*, sections 2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, live main on 2026-10-04.
Reuse its arbitrary-word parity recursion, CRT construction and
residue-20 endpoint guards. No refresh is needed for unchanged machinery.
That source's sufficient final-halving margin does not cover arbitrary
chains with tail E^2. Its inspected growing example shows applicability
of one word, not escape from every chain. No immutable revision was
obtained in the prior review; preserve that provenance limitation.

### Redundancy, failures and the required threshold

L020 and L021 already cover the affine constants and composition for
one and two words. Import these identities and coding rather than adding
a second general coding proof. Computing exact minima over more words
is a useful finite diagnostic only if it exposes a plausible invariant
or an obstruction to a proposed invariant.

L005's fixed-word repetition valuation bound depends on the word. Its
proof explicitly leaves uniform divergence of minimum starts over all
mixed words unproved. Attempt 005 refutes transferring the single-type
bound unchanged: start 603 realizes the mixed four-block word below
8187. Its recorded plateaus also rule out demanding multiplicative growth
at every extension. These concern a different alphabet; they warn against
that inference without deciding the new postspell language.

L007–L008 distinguish fixed endpoint from fixed start. L008's density
term 135/512 at its explicit test cutoff coexists with an actual endpoint
1453; the retained boundary error prevents a count-below-one argument.
Initial-root congruence minima do not use that invalid density truncation,
but changing which side is counted is not a proof of uniform divergence.
Attempts 009–011 remain parked/stopped; this review reopens none of them.

The required threshold is a bound n>=F(K) with F(K) tending to infinity,
valid for every actual positive residue-20 K-word chain in the full
J>=2,H>=3 alphabet. Five finite minima, a growing average, a large
congruence modulus, or growth of orbit endpoints do not meet it. Bounds
only for nine words or a repeated fixed word must be labeled accordingly.
The final E^2 need not exhaust all halvings at the last screened endpoint;
internal tails are followed by the next word's odd input. Preserve this
distinction when comparing finite-prefix minima with infinite chains.

### Bounded discriminating test and continuation decision

Approve the unchanged K=1,...,5 nine-word screen. Apply parity coding to
each whole concatenation and then impose residue 20 modulo 27. Record
exact minima, attaining words, and guarded orbit replays in a certificate.
Retain all offsets and distinguish positive representatives from zero.
No finite minimum is computed in this review.

Continue toward a uniform proof only if the screen and symbolic formulas
identify a constraint whose constants can be controlled for arbitrary
J,H, or an informative counterexample to a specific proposed bound.
A finite plateau refutes strict per-extension increase, not divergence.
If the bounded screen reveals no controllable mechanism, report that
scope and reassess rather than merely enlarge it. Abandon a proposed
estimate if an actual coded chain violates it. At most three mathematical
explorations without an advance or informative negative result are
available; the present literature step spends none. General convergence
remains unresolved even if the restricted bound succeeds.

### Search record and evidence limits

Queries executed on 2026-10-04:

- Collatz parity vectors restricted sequences divergent trajectories minimum starting value uniform lower bound
- Collatz prescribed parity sequences positive integers non periodic divergent Bernstein Lagarias
- Bernstein Lagarias 1996 3x+1 conjugacy map pdf
- Collatz restricted parity sequences uniform growth initial values consecutive blocks
- Collatz "postspell" "growing" chains
- Collatz "(OOEO)" "initial" size
- site:github.com/Sodelin/Collatz-Conjecture-Work postspell chains uniform

The author-hosted Bernstein–Lagarias PDF was read at the essential
introductory hypotheses/proof passages, alongside the theorem-level
Rozier–Terracol comparison. No inspected theorem establishes the exact
uniform target. Searches also returned Niu's arXiv:2605.13886, Li's
arXiv:2209.03730, Stérin's thesis and assorted claimed resolutions.
These are unread, nonessential leads; no conclusion here uses them.
Forum posts, snippets and repository methodology pages are not theorem
evidence. This bounded search does not certify absence from the
literature or originality. Existing primary coverage suffices for the
finite test, so these leads are not source blockers.

## Mathlib

Full growing-only chain initial-size bound and supporting library coverage:
**not checked**. No matching declaration or library absence is asserted.
The external source's Lean status is not Mathlib coverage.
