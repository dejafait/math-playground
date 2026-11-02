# Approved bridge obstruction calculation

Started 2026-10-31 under the saved EXPLORE assessment
`drafts/literature/2026-10-31-hardy-scalar-saturation-scope.md`, exact
COVERED_TARGET matching the startup Next action. Actual task: calculation.
No new literature or cross-notebook inputs. Read L582 in full and L473's
exact interface and relevant (6),(9)--(10); reuse their source coverage.

Main gap: actual-Xi all-degree positivity and unbounded-height initial
signs. Intermediate: test whether all paired tolerances plus the coarse
jet scale suffice to certify normalized scalar saturation uniformly over
compatible bridges. A countermodel would require additional pointwise
information for that certification, while leaving original-path saturation,
positive clipping and Xi transfer independent. Stop at any failed join,
common bound, tolerance or positive-phase-measure comparison.

Construction to check: retain f on [0,L]. On the unit bridge use two
half-length quintic Hermite pieces, with endpoint data f^(j)(L), f^(j)(0)
and common midpoint data (0,0,2 ell^2). L582's fixed six basis polynomials,
scaled by (1/2)^j for order-j data and differentiated with factor 2^k,
give an operator bound 4*1143=4572 through order two on either half.
For eventual ell^2<=H^(1/6), all data retain the common coarse scale.

Completed: canonical proof in
`lemmas/C582a-normalized-scalar-cutoff-bridge-obstruction.md`.
Scaling the endpoint table verifies all joins through order two,
including both one-sided midpoint triples. The constant 4572 bounds
the bridge operator through two derivatives. Both boundary strips and
the -m_f/P normalization give the same comparison errors as L582;
all 126 fourth entries and the 17 ordinary second entries pass.
The four tight odd moments vanish by periodic total derivatives.
Normalized composition has second derivative 2 ell^2 at the midpoint;
continuity yields an interval of length 2 delta>0 with second derivative
larger than 3 ell^2/2 and phase probability 2 delta/P>0. Delta may depend
on H and the cutoff. No uniform probability lower bound is claimed.

Outcome: informative negative for generic certification, not full scalar
saturation of the original path. All requirements of this bounded test
pass using only standard Hermite/chain-rule specialization; no new
general theorem or actual-Xi progress beyond the stated obstruction is
claimed. No mathematical script is needed: the scaled basis identity,
finite universal monomial estimate and exact cancellations give the
complete checks analytically. Separate application audit remains pending.
