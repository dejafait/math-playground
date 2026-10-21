# Eleven-adic even-valuation test — work in progress

Approved target and prior coverage:
`drafts/literature/2026-10-15-eleven-adic-even-valuation-containment.md`
(SPECIALIZE, unchanged at invocation start).

Main gap: positive primitive integer emptiness, including the 54a1 branch.
Intermediate test: full cubic two-descent image has even valuations at
all three places above eleven. Success would remove eleven from local
exceptional support; an exact odd image parks this route. Independent
class-norm, other local conditions, rank and integer lifting remain open.

Inputs: L033's E0 and K, L069's same origin-preserving cubic g,
L041's Q11 x Q11 x L with L=Q11[r]/(r^10+55). No cross-notebook input.
ATTEMPTS/032 is a different, preserved bare-unit obstruction.

Working mechanism (not yet certified here): g mod 11 has simple root 8
and double root 9. Lift alpha=8 mod 11. Its complementary quadratic
has discriminant -256*11^5/g'(alpha)^2, hence splitting field
Q11(sqrt(-11)). In L, a Hensel square root s of 5 with s=4 mod r gives
(r^5/s)^2=-11. The two clustered roots beta,gamma then have difference
of L-valuation 25. The exceptional image at (beta,0) has valuations
(0,25,25), disproving universal even containment. Check full CRT,
maximal valuation normalizations, source formula and exceptional values
before claiming a result. BPT Lemma 1.3 may certify the complete image
from independent two-torsion classes without a finite-precision search.

## Completed bounded attempt

The mechanism is now proved in canonical
[L073](../lemmas/L073-eleven-adic-two-descent-odd-valuations.md).
Both rational-place images have even valuations. At the degree-ten
place Pα and Pβ give two independent image classes, and BPT Lemma 1.3
certifies the complete image of size four, with parity image {000,011}.
Thus the exact odd class stops this local all-even premise. No numerical
sampling or mathematical script was needed; the proof checks exact
polynomial identities, Hensel hypotheses, nonsquare residues and all
factor dimensions. This is a reproduction of known local methods with
a negative route outcome; no global odd realization or rank bound follows.
Separate critical audit is the sole proposed continuation, pending its
own coverage approval. The initial working notes above are retained.
