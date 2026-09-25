# Sixteen-challenge test on the order-16 subgroup of F_97

Date: 2026-09-25. One focused step for the pinned affine-line model.

## Gap, relevance, and test

For C=RS[F_(97^20),H,8], where H is the order-16 subgroup of F_97^*,
the four-omission cell [1/4,5/16) has known bounds 10/q and 69/q.
The actual budget permits fifteen bad parameters:
15*2^128 <= 97^20 < 16*2^128. The intermediate target is sixteen
bad parameters with agreement supports of size twelve over F_97 and
an algebraic verification over every extension. This would prove
unsafety on a cell not settled by L008. General sharpness, the remaining
radius cells, and the ABF26 correspondence would still be unresolved.

The official [statement](https://proximityprize.org/) was reread today;
its preliminary formulation and unspecified field-size qualification
are unchanged. Work remains explicitly within the separately pinned
model. No local unfinished changes were present when this step began;
changes in other notebooks are left untouched. Exploration count starts
at zero after the preceding advance.

## Redundancy and proposed mechanisms

L008 already gives ten through two affine error families; merely replacing
the field in that construction cannot reach sixteen. L006's common affine
lift and L007's disjoint-support alternative use distance conditions that
fail at four omissions. Their counterexamples and endpoint qualifications
are retained. No previous local result tests sixteen on this domain.

Three possible tests are a subgroup orbit of four-coordinate errors,
a line of syndrome moment matrices with many split error locators, and
a bounded search through lines joining two four-sparse syndromes. The
subgroup orbit is the first structured test: if its moments span two
dimensions and the parameter map is injective on H, it can yield sixteen
without an unlikely random collision. A failed orbit condition will be
recorded explicitly before any broader bounded search.

## Saved unfinished reasoning

For H of order sixteen the parity moments sum_x e(x)*x^j, j=1,...,8,
annihilate degree-less-than-eight evaluation words. Distance nine makes
four-sparse error representatives unique. Under x -> t*x with t in H,
moment j scales by t^j. A projective orbit can lie on a line if only two
moment characters occur; distinct projective parameters require the
difference of their exponents to be coprime to sixteen. The error weights,
same-support failure, and passage from projective parameters to an affine
line must all be checked. No witness or uniform upper bound is asserted.

Continue a successful construction only after exact interpolation verifies
the original event and a proof establishes extension-field persistence.
If no construction reaches sixteen, record the exact tested family and
best count, distinguishing finite failure from a theorem of impossibility.
The assessment and next-direction decision must finish within this step.

## Completed assessment

The structured family is ruled out by the full algebraic proof in
[L009](../lemmas/L009-two-character-orbit-obstruction.md). Independence of
the subgroup characters reduces a two-dimensional syndrome orbit to two
nonzero moments. Four consecutive zero moments are impossible for a
nonzero four-sparse word. The ten remaining moment pairs are classified
by a locator determinant; only (u,u+4) survives, with errors supported
on a coset of the order-four subgroup and proportional to x^(-u).
The sixteen shifts have only four projective directions, irrespective
of nonzero scalar normalizations. This applies over every extension,
not just over the prime field.

The exact auxiliary check covers all 28 moment pairs and all 1820
four-coordinate supports, including smaller supports through zero
coefficients. It agrees with the algebraic classification. A separate
signed-permutation expansion checks all ten determinant identities over
the integers, and integer arithmetic checks the actual budget fifteen.
The reproduction command is `python3 scripts/subgroup-orbit/check.py`.

Outcome: NEGATIVE. This supplies a new obstruction that stops the full
orbit mechanism; it is not an upper bound for arbitrary input pairs,
partial orbits, or extra errors outside an orbit. The achieved limit
four cannot reach sixteen and does not improve the existing lower count
ten. The general bounds 10/q and 69/q are unchanged. There is no
complete challenge candidate. Consecutive exploration turns reset to zero
after this informative negative result.

The determinant description exposes a different possible mechanism:
for a general affine moment pencil, each fixed-coordinate locator is
a polynomial in the challenge of degree at most four. Counting their
zeros might approach the threshold sixteen and isolate an equality case.
This remains unproved here; singular determinants, permanent coordinate
roots, and sparse representatives of weight below four need explicit
treatment. It motivates the sole current action in PROGRESS.md rather
than another orbit search. No random search was needed after the exact
family obstruction was proved.
