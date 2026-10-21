# Source comparison: extendible postspell inverse rigidity

TARGET: Determine whether every odd residue-20 endpoint has at most one positive postspell predecessor (OOEO)^J O^H E^2 with J>=2,H>=3 that itself admits a preceding word of the same alphabet, retaining every actual parity guard.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-word, postspell/inverse, extendible-predecessor and prescribed-word/congruence searches on 2026-10-05 returned supporting coding and inverse-graph sources but no matching uniqueness theorem; queries and inspected passages are recorded below.
SOURCE_EVIDENCE: Bernstein–Lagarias author PDF dated 19960215, section 1 pp. 1–3, equations (1.3)–(1.6) and uniqueness argument; Laarhoven–de Weger arXiv:1209.3495, section 2 equations (2)–(5), Theorem 2.1 and preceding argument, section 3 Theorem 3.1; Rozier–Terracol arXiv:2502.00948v2 section 2 and v5 (2026-05-17) Definition 2.1, Theorem 2.4 and proof, Lemma 2.5 coding paragraph; prior Sodelin sections 2–3 assessment reused.
COMPARISON: Per-word parity bijections and residue-graph isomorphisms do not assert uniqueness across different positive postspell predecessors of one integer; L007–L010 have different alphabets and endpoint unions. No inspected theorem proves or refutes this exact claim.
GAP: Establish disjointness for all unbounded J,H after an actual preceding postspell word, or exhibit one endpoint with two distinct positive extendible predecessors and complete parity guards.
REASON: Essential comparison for the changed mechanism is now complete for a bounded discriminating attempt; reuse sourced finite coding and local affine identities without reproof. Failure to find a matching result does not establish novelty.
SCOPE: The stated full alphabet, positive odd residue-20 starts/intermediate endpoints/final endpoint, actual two-word histories, exact E^2 tails, all-parameter inverse-class analysis and the bounded collision test below; no least-root filters or universal forward-escape claim.

The candidate concerns the shortcut map, positive odd roots and endpoints
20 modulo 27, and words W(J,H)=(OOEO)^J O^H E^2 with J>=2,H>=3.
For a fixed endpoint m, count distinct positive predecessors n with an
actual W(J,H) from n to m, where an additional positive residue-20
predecessor reaches n by another such actual word. Positivity and all
intermediate input parities are essential; integral affine inverse
values alone are insufficient. Count predecessor integers, not labels.

Essential available inputs for the eventual test are L020's constants,
L021's concatenation and imported finite coding. L007–L010 supply
comparisons to previous decoder successes and failures only. No
cross-notebook input is proposed. L022 stops the repeated-minimum
transfer, not this different mechanism.

## Primary comparison and reuse

Bernstein–Lagarias, [*The 3x+1 Conjugacy Map*, author manuscript
19960215](https://websites.umich.edu/~lagarias/doc/bernstein.pdf),
section 1, pp. 1–3, equations (1.3)–(1.6): the shortcut map on Z_2
is conjugate to the binary shift; the conjugacy induces permutations
modulo powers of two. Read the uniqueness proof after (1.4), the
parity-series formulas and the positive-integer/Periodicity Conjecture
qualifications. This is uniqueness of the conjugacy and of the encoded
start for a fixed full parity sequence, not uniqueness of past words
at a common endpoint. Different words are not identified by that
theorem. Its unproved rational periodicity claim is not an input.

Laarhoven–de Weger, [*The Collatz conjecture and De Bruijn graphs*,
arXiv:1209.3495](https://arxiv.org/html/1209.3495), published in
*Indagationes Mathematicae* 24 (2013), 971–983,
doi:10.1016/j.indag.2013.03.003: read the section 2 graph definitions,
equations (2)–(5), Theorem 2.1 and its preceding parity-shift argument,
and section 3 Theorem 3.1. For every k>=1 the finite residue graph is
isomorphic to the binary De Bruijn graph. Section 2 also records two
incoming edges and one length-k path for each ordered pair of vertices.
These vertices are classes modulo 2^k, and the path statement fixes
both vertices and length. It does not fix one integer endpoint and
range over variable postspell lengths with positive residue-20
intermediate integers. The Z_2 extension in Theorem 3.1 likewise does
not preserve a restriction to positive integer predecessors. Neither
statement proves a collision in this restricted language or its
absence. This stronger graph description is supporting, not matching,
coverage. The arXiv HTML was accessed 2026-10-05; no immutable local
source copy or version suffix was used.

Rozier–Terracol, [*Paradoxical behavior in Collatz sequences*,
arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2), section 2,
was rechecked at the finite coding paragraph preceding Theorem 2.2,
that theorem and its proof, and Lemma 2.3's coding paragraph. The
[current v5](https://arxiv.org/html/2502.00948v5), dated 2026-05-17,
was also checked at Definition 2.1, Theorem 2.4 and proof, and
Lemma 2.5's coding paragraph. The supporting coding claim survives:
each length-j input parity vector occurs once among 1,...,2^j.
The remainder bounds still concern fixed length and odd count, not
disjoint endpoint fibers over this unbounded word language. Later
numbering does not invalidate the existing version-specific v2
citations in L020/L021. No result about all of v5 is inferred from
these selected passages.

Reuse the prior [two-word assessment](2026-10-04-two-postspell-compensation.md)
of Sodelin's [Postspell_Guarded_Root_Descent.md, sections 2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, live main read 2026-10-04.
Its parity recursion, CRT realization and actual residue-20 endpoint
guards apply to any finite word, including the present concatenations.
Its sufficient final-halving margin does not imply inverse rigidity
at tail 2. The earlier absence of an immutable revision is retained.
No general parity theorem needs a new proof: the remaining work is
the language-specific comparison of endpoint fibers.

## Duplicates, failures and search scope

Read L020's hypotheses, constants and guarded coding, and L021's
hypotheses and concatenation/coding proof. They already provide the
necessary local affine data. Read L007/L009's exact extendibility
proofs and L010's changed endpoint union and overlap proof. The first
two use disjoint lifted congruences; L010 demonstrates that a changed
alphabet can turn them into nested classes. None uses this alphabet.
Their fixed-endpoint bounds also leave fixed-start escape unresolved.
L022 and [Attempt 012](../../ATTEMPTS/012-repeated-postspell-minimum-transfer.md)
stop a repeated-minimum transfer and a negative affine lower estimate,
not this inverse question. No stopped route is reopened.

Queries actually run included:

- `Collatz "postspell" inverse rigidity`
- `Collatz "OOEO" extendible inverse uniqueness`
- `"Collatz" "postspell" "inverse"`
- `"Collatz" "OOEO" "extendible"`
- `"Collatz" "extendible predecessor"`
- `Collatz inverse iteration prescribed words congruence overlapping predecessors Wirsching`
- `Collatz inverse parity vectors Bernstein Lagarias 1996 3x+1 conjugacy`
- `"Collatz conjecture and De Bruijn graphs" theorem parity vectors`

The exact-word searches chiefly returned the already-used Sodelin
postspell source and project overviews, not a matching inverse theorem.
Broader searches supplied the inspected primary papers above. Wirsching
predecessor-density work and the search lead arXiv:2605.13886 were not
read at theorem level; neither is claimed as matching coverage or as
an essential missing input to this finite coding test. Search snippets
and repository overview claims were not used as theorem evidence.
This is a bounded comparison, not an exhaustive novelty search.
Mathlib coverage for the full inverse target is **not checked**;
no library theorem or formal verification is assumed.

## One bounded mathematical attempt for the reviewed target

Use L020/L021 and the cited coding to obtain fully guarded endpoint
classes for two-word histories p -> n -> m. Keep J>=2,H>=3 in any
symbolic inverse-class argument. Before enlarging any finite range,
look for an all-parameter disjointness or overlap mechanism.
The finite fallback is the 25 parameter pairs 2<=J<=6, 3<=H<=7 for
both the preceding and final words. Compare the endpoint fibers of
their 625 two-word labels using exact congruence compatibility and
positivity, rather than scanning integers to an arbitrary cutoff.
The range is a counterexample search within the unchanged full target,
not a new restricted uniqueness conjecture or a new minima screen.

Every admitted history must have p,n,m positive odd and 20 modulo 27,
both words actual, and both final tails exactly E^2. Encode or replay
the odd final endpoint as well as all input parities. Count distinct
intermediate predecessor integers n, not labels. A candidate collision
requires the same m, n_1!=n_2 and a complete guarded replay of both
p_i -> n_i -> m histories. No L014–L018 least-root filter is part of
this target; a collision need not be a hypothetical least root.
Save complete relevant certificates under scripts/ only on that later
research turn. This turn performs no inverse calculation.

One rigorously guarded collision abandons the uniqueness target.
All-parameter disjointness would justify continuing inverse rigidity;
it would still not prove forward escape. A collision-free finite
screen is only EXPLORATION. Without a new all-parameter mechanism it
does not license a larger rectangle or a universal uniqueness claim;
reassess after the bounded attempt under the shared exploration rules.

Plausible use: inverse rigidity could constrain the arithmetic of
growing-chain survivors and replace a failed bound transfer. It would
still require an independent uniform fixed-start escape estimate;
L007/L008 show why a fixed-endpoint history bound alone does not supply
that estimate. Entry into the postspell class, other tails and eventual
compensation also remain unresolved. This EXPLORE assessment covers
the unchanged saved target for a later mathematical attempt; it
establishes no new lemma or uniqueness result. There is no complete
candidate argument.
