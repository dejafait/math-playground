# Four errors and the seven-challenge budget test

Date: 2026-09-25. One focused step in the frozen affine-line model.

## Gap, intermediate target, and decision test

For C=RS[F_(17^s),F_17^*,8], L007 determines the cell with three
omissions but leaves the cell [1/4,5/16) open. The concrete intermediate
target is seven bad challenges on supports of size at least twelve.
Such a construction over F_17, with an algebraic check of codeword
membership and same-support failure over every extension, would exceed
the actual 2^-128 budget at q=17^32. Combined with L007 and monotonicity,
it could locate a crossing for this particular smooth code. The general
sharp radius and the ABF26 event, endpoint, and field-size correspondence
would remain unresolved.

This is not a repeat of the failed unconditional distance-boundary
extension: at four errors the distance-nine argument permits overlapping
supports. No earlier local lemma tests this cell. The official
[statement](https://proximityprize.org/) was reread today and still gives
the same preliminary target and unspecified sufficient-field hypothesis.
Starting exploration count: zero.

## Saved unfinished reasoning

Use the eight parity moments of an error word on F_17^*. Since the code
has minimum distance nine, a syndrome has at most one error representative
of weight at most four. A line through two such syndromes may meet other
four-coordinate error spaces; overlaps between the supports are allowed.
A bounded deterministic search can decode the seventeen syndromes on each
sampled line, retain candidates with seven distinct decodable parameters,
and then test the original event independently by polynomial interpolation.
Decodability alone is insufficient: the direction must fail on each same
agreement support. Extension-field persistence requires a proof, not an
extrapolation from the prime-field count.

Continue if a witness admits that full verification. If the bounded
search misses seven, record its scope and best count without claiming an
upper bound; assess whether the observed support geometry supplies a new
mechanism before repeating the search. This document saves the test before
computation; it does not assert that a witness exists.

## Discovery and proof outline saved before verification

The deterministic search found seven decodable parameters at trial 47125.
Five of its error supports were four-element subsets of the same five-set.
This suggests a simpler algebraic construction that supplies ten parameters.
Let A={1,2,3,4,5}, B={6,7,8,9,10}, and
Q(X)=product_(j=11,...,16)(X-j). On A set a(x)=xQ(x), b(x)=-Q(x),
and set both words to zero elsewhere. If gamma lies in A, the combination
has weight four and agrees with the zero codeword off A minus {gamma}.
If gamma lies in B, it agrees with the degree-seven polynomial
(X-gamma)Q(X) off B minus {gamma}.

For gamma in A, any degree-less-than-eight polynomial matching b on
that support has eleven zeros and a required nonzero value, impossible.
For gamma in B, adding Q to such a polynomial gives eleven zeros;
therefore the polynomial must be -Q, which contradicts its required
zero at gamma. These root-count proofs work in every F_(17^s).

More generally, the same construction works for n-k=2r, k>=2, with
two disjoint (r+1)-sets and Q vanishing outside their union. It supplies
2r+2 bad challenges at cutoff n-r. This is a lower bound, not a claimed
sharp count. L007 supplies the safe side for the special code at q=17^32;
monotonicity would then give the exact safe set [0,1/4) for the frozen
model. Independent interpolation checks and the final write-up remain.

## Completed assessment

The target is exceeded: the full proof in
[L008](../lemmas/L008-two-block-witness-and-model-crossing.md) supplies ten
bad challenges. It proves the general lower bound (2r+2)/q when n-k=2r
and k>=2, at every delta>=r/n. The root-count argument verifies both
codeword membership and input failure on the same support over the full
extension field. No search result is used as a theorem premise.

For RS[F_(17^32),F_17^*,8], the actual budget permits six parameters,
whereas the new witness has ten. L007 supplies safety on [3/16,1/4);
monotonicity gives safety below that interval. Thus the safe real set is
exactly [0,1/4), and the largest safe grid radius is 3/16. This is a
partial resolution for one frozen-model code, not a complete challenge
candidate. ABF26's event and all source qualifications remain unresolved.

The independent check examines every claimed support for the initial
seven-parameter discovery and all seventeen parameters and 2517 admissible
supports for the simpler construction. It finds exactly {1,...,10} for
the latter pair over F_17. The lemma claims the proved extension-field
lower bound, not a global maximum inferred from that computation.
Its genuine lemma input is L007 for the safe side; monotonicity is proved
directly from the definition. The references to L004 are bound comparisons.

The new count is not enough for every security budget. At n=256,k=128,
r=64 it gives 130, much less than the permitted count at q=257^32.
For n=16,k=8 the remaining general error bounds on the four-omission cell
are 10/q and 69/q. A smooth order-16 subgroup exists in F_97^*;
at q=97^20 the budget permits fifteen parameters, since
15*2^128<=97^20<16*2^128. The two-block witness alone cannot decide
that code's cell. This is the reason for testing support configurations
that could exceed fifteen, rather than trying to sharpen an already
determined crossing at q=17^32. The sole current action is in PROGRESS.md.

Outcome: ADVANCE. Exploration turns used reset to zero. Review covered
the case k=2, the required r>=1 root counts, disjointness of the two
blocks, distinct challenge values, the strict endpoint, and extension-field
failure tests. Mathlib coverage remains not checked.
