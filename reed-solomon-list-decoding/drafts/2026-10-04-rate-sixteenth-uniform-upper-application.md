# Rate-1/16 two-moment upper application: working reasoning

The saved target and SPECIALIZE assessment are unchanged:
`drafts/literature/2026-10-04-rate-sixteenth-joint-fiber-upper-bound.md`.
This is one mathematical application of its inspected counting tools,
without new literature work. Existing changes and the averaging failure
are preserved.

The gap is whether the two-coefficient center family can witness unsafety
at 66 agreements on H of order 1024 in E=F_65537 inside F=F_{65537^28}.
L013 already identifies every such center list with its unordered subset
fiber, independently of interleaving width. A uniform bound at most
65537^28/2^128 would stop this witness family; a bound above it would be
inconclusive. Arbitrary centers and the sharp boundary remain later gaps.

For the fixed first two elementary coefficients b,c, the power-sum target
is (b,b^2-2c). The monomial image {x^64:x in E} is H together with zero.
The cited Proposition 1 bounds each nonconstant degree-one or degree-two
phase on that image by r sqrt(65537); deleting zero costs at most one.
Thus every nonzero character pair on H has one-coordinate sum bounded
by 2 sqrt(65537)+1<514. Every cycle length in the distinct-coordinate
sieve is at most 66, below characteristic 65537, so it preserves a
nonzero pair. The cited symmetric weighted sieve and cycle identity then
bound each nontrivial ordered Fourier contribution by
66! binomial(579,66).

The prospective unordered upper estimate is

    [binomial(1024,66)+(65537^2-1) binomial(579,66)]/65537^2.

The completed exact integer/rational certificate puts this estimate below
2^317, while the ambient threshold exceeds 2^320. The upper-to-threshold
ratio is strictly between 11256/100000 and 11257/100000. No 1024-point
subset fiber was enumerated. The proof is in
[L014](../lemmas/L014-rate-sixteenth-uniform-two-moment-upper.md), with the
certificate in `scripts/coefficient-fibers/uniform-upper-results.json`.
An independent small-domain group-algebra audit checks the signed sieve
against distinct-tuple and unordered-subset enumeration at every moment
pair, including the signs and A! divisor.

This stops the assessed family as a source of unsafe witnesses at A=66.
The full code's largest safe grid index remains unknown and at most 958;
no claim is made over arbitrary centers. This is REPRODUCTION of known
counting tools, not a claim of originality or a complete candidate. The
changed degree-67/linear-cofactor direction has only a pending assessment;
no calculation on that later target was performed here.
