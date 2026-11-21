# Explicit interval-to-node Laplace propagation: nomination1790

TARGET: Prove an explicit [1,2]-to-finite-positive-node propagation bound for Laplace transforms of finite real signed half-line measures with prescribed total variation, using Trefethen's strip lemma and three-circle theorem, without extending the Gaver witness or evaluating the observable.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1790 searched fixed-interval inverse-Laplace stability, signed-measure stability and bounded analytic continuation; exact searches, duplicates and failures are recorded in drafts/literature/2026-11-19-residual-variation-cost-source-notes-1790.md. No exact notebook-family rate was identified; no novelty is inferred.
SOURCE_EVIDENCE: Trefethen, BIT60(2020), DOI10.1007/s10543-020-00802-7, https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf, published author PDF, Lemma2.1 and full proof p904, Theorem3.1 and full proof pp904-905; inspected also Section4 and Theorem5.2/proof p908. Standard holomorphic integration, dominated convergence, Fubini and the identity theorem are supporting named inputs. Mimica Proposition1.4 is real-positive coverage only, not a signed holomorphy theorem.
COMPARISON: The source supplies the exact normalized strip and concentric-disk inequalities; the missing specialization is a fully explicit real-interval-to-disk seed and finite positive-node propagation for a signed Laplace transform. Theorem5.2 alone leaves its geometry-dependent exponent unspecified. C033n's nearby real-node perturbation and C033r's unrestricted sample locations do not already give this fixed-interval control.
GAP: Specify all maps, boundary limits, positive-half-plane domains, disk radii/overlaps, finite iteration counts, explicit exponents and zero/trivial-error cases; justify signed-transform holomorphy and the exact TV normalization. No such application proof or rate is supplied by this nomination.
REASON: This is a narrower independently testable bridge toward the preserved d(V) rate question, using inspected quantitative sources while avoiding unavailable global inverse hypotheses. It is routine specialization, not a creative central-RH mechanism. Newly saved ready coverage must receive separate approval before research.
SCOPE: Arbitrary finite real signed Borel measures on [0,infinity), atoms and unbounded support allowed, positive finite TV allowance, prescribed finite nonempty positive node set, uniform transform error on [1,2]; no moments, density, width positivity, convolution inverse or Xi realization.

## Proposed result and exact limit of approval

Given theta with ||theta||_TV<=M, 0<M<infinity, write
F(z)=integral exp(-z*t) dtheta(t) for Re z>0. For an arbitrary
prescribed finite nonempty S contained in (0,infinity), the proposed
result is an explicitly specified alpha(S) in (0,1] such that, when
0<epsilon<M and sup_[1,2]|F|<=epsilon, every s in S satisfies

    |F(s)| <= M*(epsilon/M)^alpha(S).

This display is the target, not a proved inequality in this turn.
State separately epsilon=0, theta=0, and the trivial large-error case.
Source theorems are imported; do not reprove the three-circle theorem
or treat its application as new general inverse-Laplace mathematics.

Source: Lloyd N. Trefethen, *Quantifying the ill-conditioning of analytic
continuation*, BIT Numerical Mathematics60 (2020), 901-915,
[published PDF](https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf),
DOI10.1007/s10543-020-00802-7. Lemma2.1 assumes holomorphy and norm at
most1 in the infinite strip 0<Re w<1, and a uniform limiting bound on
its left boundary; its bounded-strip proof explicitly pays the
unbounded-domain maximum-principle issue. Theorem3.1 assumes a function
holomorphic and bounded by1 on a disk of radius R>1 and bounded by
epsilon on the unit disk. It gives the exponent
1-log|z|/log R on 1<|z|<R. Its full proof uses the strip lemma after
an exponential map. These are exact, nonasymptotic inequalities.

For a candidate construction, test an annular/Joukowski parametrization
of an ellipse around [1,2] to obtain a complex seed region, then finite
translated/scaled applications of Theorem3.1. This is a proposed method,
not an approved geometric calculation. Every chosen region must stay
strictly in Re z>0; nodes below1 require explicit leftward geometry as
well as nodes above2. Strip boundary bounds must be uniform and branch
choices justified. A three-circle estimate starts from a disk, so the
initial real interval cannot silently be substituted for that disk.

The transform's complex existence/holomorphy and TV bound must be
checked for signed measures using absolute variation and compact
positive-half-plane domination. Standard holomorphic differentiation
under the integral, or Morera plus Fubini/dominated convergence, is the
named tool. Mimica's real positive-measure theorem alone is insufficient.
No undamped moment at zero, support cutoff or density is allowed.

Do not invoke Trefethen Theorem7.1: its sufficiently-small-data threshold
and numerical auxiliary-inequality check are unnecessary for the exact
finite iteration target. Do not use Theorem5.2's unspecified conformal
map as an explicit exponent. A reproof of those theorems is not needed.

## Relevance, bounded test and remaining gaps

Main gap remains L030-L032/C032a actual-Xi all-degree positivity.
This generic bridge could later connect interval error for the original
laws to the distant finite Gaver nodes in C033r. For the notebook
application retain C033i/j/l/p/r and the qualified C032j normalization;
all divisor/conjugation/multiplicity, excluded ordinate zero, strict
strip/gamma>14, counting, through100/retained-real-zero/reciprocal-square
tail, heat positivity, separate fixed-j errors, Gaussian half-variance
and both fixed-v1 assumptions persist. They are not inputs needed to
prove the generic transform statement itself and are not re-audited.

Continue only with a fully explicit finite alpha(S)>0, including both
ends of the prescribed node range and all boundary and normalization
checks. If the chosen geometry needs an unknown norm, nonexplicit map
or asymptotic threshold, record that failure and park that construction.
No numerical feasibility, sharp exponent or universal Lipschitz inverse
is required or implied.

The cap-V extension of C033r, its one-sided modulus/parameter selection,
full signed tails and zero atoms, exact division by nu_1's transform,
coefficient amplification and an assembled positive e(V) are independent
later obligations. None is covered as a research subtarget here. An
actual-Xi realization, necessary width budget, signed-height payment and
all-degree positivity remain still further gaps. Full matching Mathlib
coverage is unchecked and unknown. Preserve numerical stops1571/1576
and1781/1782 without reopening their evaluators.
