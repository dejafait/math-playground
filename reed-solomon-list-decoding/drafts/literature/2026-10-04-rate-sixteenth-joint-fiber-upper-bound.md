# Rate-1/16 joint-fiber upper comparison: completed assessment

TARGET: Determine whether a uniform two-moment subset-count estimate bounds every A=66 two-coefficient center list on the order-1024 subgroup of F_65537 inside F_{65537^28} by 65537^28/2^128 at rate 1/16, for every m>=1.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched uniform two-moment counts on multiplicative subgroups and followed the previous moment paper's references to Li-Wan's weighted sieve and Nguyen's dissertation; inspected the primary statements below and reused the adequate coefficient-dictionary review.
SOURCE_EVIDENCE: Read Lai-Marino-Robinson-Wan arXiv:1910.05894v2 Proposition 1 (p. 6), Section 3's cycle estimates and equation (4) (pp. 19-20), and Theorem 10 (p. 21); Li-Wan arXiv:1507.06329v1 Theorem 2.1/Corollary 2.2 (p. 5), Lemma 2.7 (p. 7), and Lemma 3.1 (pp. 8-9); Nguyen's 2019 dissertation Theorem 2.11 (pp. 10-11) and Lemma 4.1 (pp. 18-19); rechecked Gao v3 Theorems 4-5's subfield hypotheses. Page numbers are printed, not zero-based PDF indices.
COMPARISON: The inspected monomial character estimate and arbitrary-domain weighted sieve cover the quantitative mechanism. They do not state the complete proper-subgroup/interleaved threshold conclusion. The coarse positivity theorem, full-field formulas and collision lower bound cannot settle this upper comparison by citation alone.
GAP: Specialize the known monomial bound with zero removed, apply the cited weighted sieve to both moments with the ordered/unordered normalization intact, and compare the resulting certified uniform upper estimate with the actual ambient threshold. No numerical outcome or local upper inequality is established in this review.
REASON: Approve one mathematical reproduction of these known tools for the unchanged target; only zero deletion, the prescribed domain and moment coordinates, effective constants and L013's interleaved applicability need local work. All essential supporting statements are now readable.
SCOPE: n=1024, k=64, A=66, H of order 1024 in E=F_65537, ambient F=F_{65537^28}, epsilon*=2^-128, every m>=1, and only centers (x^66-b x^65+c x^64,0,...,0) with b,c in E. Covers the cited monomial-image/zero-deletion and weighted-sieve specialization and its exact threshold test. Does not cover arbitrary received words, other agreement levels or domains, new character-sum theorems, exact maximizing fibers, or ABF26 retrieval.
COVERED_TARGET: Specialize the monomial-image character estimate to nonconstant linear and quadratic phases on H, including zero deletion and every nonzero character pair.
COVERED_TARGET: Apply the cited weighted distinct-coordinate sieve to the A=66 two-moment fibers and compare the resulting uniform bound with 65537^28/2^128, using L013 for every m>=1.
LITERATURE_REASON: The changed conclusion requires a uniform quantitative upper bound on all two-coefficient fibers; the ready assessment permits collision averaging only and explicitly excludes new character-sum estimates or exact subgroup formulas.

## Gap, downstream use and discriminating test

[L013](../../lemmas/L013-two-leading-coefficient-fibers.md) identifies every
such center list with N_H(66;b,c) and supplies the lower certificate.
At the other three rates that certificate excludes another grid radius.
At rate 1/16 its size is about 0.113 times the threshold, so its failure
does not answer whether a much larger fiber exists. A uniform upper bound
below the threshold would stop this particular lower-witness family;
it would still leave arbitrary received words and the sharp boundary open.

The preceding
[assessment](2026-10-04-two-leading-coefficient-fibers.md) approved only
construction and averaging. It did not approve this changed upper claim.
The earlier averaging failure is preserved in
[ATTEMPTS/004](../../ATTEMPTS/004-rate-sixteenth-two-coefficient-averaging.md).
This review assesses a different mechanism, without retrying that lower
certificate or the parked ABF26 source access.

The later test is whether a certified upper estimate, uniform in b,c,
is at most 65537^28/2^128. Passing stops this center family as a source
of an unsafe witness at 66 agreements. A larger upper estimate is
inconclusive; it establishes neither a large fiber nor full-code safety.
If this standard estimate is insufficient, preserve the limitation and
reassess the mechanism instead of repeating positivity or averaging.
Arbitrary-center upper bounds and the sharp boundary remain later gaps.

## Primary inputs inspected

**Monomial character estimate.** Lai, Marino, Robinson and Wan,
[Moment subset sums over finite fields, arXiv:1910.05894v2](https://arxiv.org/pdf/1910.05894v2#page=6),
2019-10-19, Proposition 1, printed p. 6, bounds a nontrivial additive
character sum of a degree-r polynomial over D={x^d:x in F_Q} by
r sqrt(Q), assuming p does not divide r and (d+1)^2<=Q. Its proof
explicitly separates D's zero element. Read also Section 3, pp. 19-20,
through equation (4), which gives the ordered moment-count error before
the extra small-character condition used in equation (5) and Theorem 10.
For this scope the moment number is two, not the interleaving width.
The source uses M=A! N for ordered versus unordered counts. Its
[HTML](https://arxiv.org/html/1910.05894v2) supplied readable equations;
the versioned PDF confirmed numbering and pages. These are supporting
inputs; they are not a full matching threshold theorem.

**Weighted sieve for arbitrary domains.** Li and Wan,
[Counting polynomial subset sums, arXiv:1507.06329v1](https://arxiv.org/pdf/1507.06329v1),
2015-07-22. Theorem 2.1 and Corollary 2.2, printed p. 5, give the
weighted distinct-coordinate sieve and its symmetric version for arbitrary
finite Cartesian domains. Lemma 2.7, p. 7, controls the cycle polynomial
with weights u for d not dividing i and v for d dividing i, 0<=u<=v:

\[
 C_A(t_1,\ldots,t_A)
 =A![z^A]\,(1-z)^{-u}(1-z^d)^{-(v-u)/d}
 \le (u+(v-u)/d+A-1)_A.
\]

Here (w)_A is the falling factorial; C_A counts permutations with their
cycle weights. Lemma 3.1, pp. 8-9, gives the Fourier/sieve count for an
arbitrary subset of a finite commutative ring and factors each cycle into
one-coordinate character sums. These statements permit the two-moment
domain to be represented in E x E with the identity polynomial, or the
weighted theorem to be used directly on H^A. They do not require H to
be a subfield. Import these identities rather than reprove the sieve.

**Closest exact formulas have narrower scope.** Nguyen,
[Higher Moments Subset Sum Problem over Finite Fields](https://escholarship.org/content/qt2cr0w697/qt2cr0w697.pdf),
UC Irvine dissertation, 2019, Theorem 2.11, printed pp. 10-11, treats
D=F_Q and the zero moment pair. Read Chapter 4's domain declaration
and Lemma 4.1, pp. 18-19; the proof displays the elementary relation
between the first two power sums and elementary symmetric coefficients.
The exact full-field formula is not a formula on H. Rechecked Gao,
[arXiv:2105.12845v3](https://arxiv.org/html/2105.12845v3),
2022-11-10, Theorems 4-5: both require a subfield domain. Neither is
an alternative direct import for the fixed proper subgroup.

## Applicability comparison and authorized local difference

The source field in character orthogonality is E, of cardinality Q=65537;
the threshold field is F, of cardinality Q^28. Keep these separate.
The order-1024 subgroup has index 64 in E's multiplicative group, so the
monomial source to check is x^64, including its zero value. Proposition 1's
hypotheses are compatible with this exponent and the linear/quadratic
phases. Its zero-inclusive count cannot simply be relabeled as a count on
H. The mathematical specialization must account for deleting that term
in every needed one-coordinate character sum.

Theorem 10 uses the coarser character parameter (r d+1)sqrt(Q), requires
it to be <=0.013|D|, and requires A>=6 r_p ln(Q). Those quantitative
hypotheses do not hold for this instance. In any event its conclusion is
positivity, not an upper threshold certificate. That failure does not
disable the weighted sieve or the sharper monomial Proposition 1.
Equation (4)'s coarse parameter is not the estimate to substitute
mechanically; the inspected weighted statements allow the actual
one-coordinate bound to be used. This difference is the reason for
SPECIALIZE rather than IMPORT.

For the next mathematical application, check the known two-moment
coordinate identity against L013's signs, apply the Fourier count uniformly
over all pairs, keep the cycle multiplicities and A! conversion, and either
retain the characteristic correction in Lemma 2.7 or justify simplifying
it using p>A. Check nontrivial character powers for all cycle lengths;
none may be replaced by an unexamined trivial-character estimate. Verify
the resulting finite upper comparison by exact arithmetic. Do not reprove
L013's entire-center or extension-field argument, which already supplies
the passage to every m>=1.

This authorizes an effective application of known counting tools and the
specified applicability checks, not a new character-sum theorem. No
numerical upper bound, safety assertion, largest-fiber computation or
new proof has been made in this literature turn. A later successful
application should be classified REPRODUCTION; no result beyond the
checked literature is being claimed.

## Search and access record

New queries were:

- `"moment subset sums" "multiplicative subgroup" upper bound`
- `"two moments" "subset" "multiplicative subgroup" finite fields uniform count`
- `"Counting polynomial subset sums" Li Wan pdf`
- `"A new sieve for distinct coordinate counting" pdf`
- `"higher moments subset sums" Nguyen dissertation 2019`
- `"A new sieve for distinct coordinate counting" arxiv`
- `"Wang" "Nguyen" "k-subset sum problem over finite fields" pdf`
- `"second moment" "subset" "multiplicative subgroups" count`

Search snippets and secondary pages were discovery leads, not theorem
inputs. Wan's author-hosted sieve.pdf and polysum.pdf failed to open;
the versioned primary arXiv paper supplies the required weighted theorem
and cycle bound, resolving the essential statement gap without relying
on the unread original 2010 PDF. Nguyen's repository landing page was
unreadable, but the direct university PDF opened and supplied the scoped
statements above. ArXiv's Li-Wan record lists only v1; no later version
or published-text equivalence is assumed.

The previous assessment's Zhang-Zheng-Wang-Yuan publisher lead,
[Some new results on the second moment k-subset sum problem over finite fields](https://doi.org/10.1016/j.ffa.2026.102877),
still has unread mathematical statements. It is not essential to this
known-method application; no further retrieval was attempted and no
novelty comparison with it is asserted. Likewise the ABF26 comparison
remains parked. No adequate full matching proper-subgroup threshold
statement was found in the inspected sources; that is not evidence of
novelty.

The [prize page](https://proximityprize.org/) was rechecked on 2026-10-04.
Its displayed threshold still uses epsilon* times the ambient field size
with constant interleaving width. This does not remove the source-model
qualification already recorded in foundations/.

## Completed review

Outcome: EXPLORATION; STEP_KIND: LITERATURE; classification:
NOVELTY_UNCHECKED. The pending comparison now has SPECIALIZE-ready
coverage for its unchanged target. This is new source-scope information,
not a mathematical advance or an upper-bound result. Exploration turns
used remain 0/3; this review spends no calculation turn. The full challenge
remains IN_PROGRESS, with no complete candidate. Lemmas, mathematical
scripts, PROOF.md and the ID-only DAG were left unchanged.

## Mathlib

Full uniform two-coefficient proper-subgroup upper comparison: **not
checked**. Mathlib coverage of the named weighted sieve, cycle estimate,
moment-count and character-sum results: **not checked**. The direct primary
links above supply supporting results, not a full matching library theorem.
The pinned ArkLib definitions remain **present** as recorded in the model;
they fix conventions and do not establish the upper comparison.
