# Marked pair curve — proposed genus-one quotient

TARGET: Test whether L109's fixed-minus-three marked curve has an explicit genus-one quotient over Q.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared audited L109/L110, their model assessment/audit and history/383/ATTEMPTS/050; searched genus-two unramified double covers, elliptic subcovers, Prym factorization and exact sextic coefficient variants; inspected Bruin, Docking and Bruin–Stoll primary passages, with no matching exact-instance quotient found in the sources checked.
SOURCE_EVIDENCE: Read Bruin arXiv:math/0408069v2 Section 2.2 pp.4–5, construction, Proposition 2.2 and its proof; Docking arXiv:2108.09564v2 Section 2/Table 1 p.4, including genus-two Case II and twist ambiguity; Bruin–Stoll arXiv:0803.2052v2 Section 8 pp.14–15 through the twist-norm formula; Stacks 53.2.6 map-extension proof, 53.12 Riemann–Hurwitz and 105.2 elliptic-curve definition.
COMPARISON: Known split hyperelliptic double-cover theory supplies actual factor-curve projections, beyond a Prym dimension count; the quadratic–quartic case is explicitly recorded in Docking. None of these sources determines this instance's marked twist, coordinate functions, origin or rational points.
GAP: In a separate research turn match L110's exact z square class to its recorded quadratic–quartic factorization, verify the resulting Q-function-field maps and their degree/proper extension, and test for a rational origin without assuming one.
REASON: Essential coverage is ready for one bounded exact model-and-map specialization; retain the unchanged target, import the general construction, and compute only the instance-specific twist and maps next turn.
LITERATURE_REASON: The saved marked-curve quotient target was REVIEW_REQUIRED and outside the ready rank-detector scope; actual subcover projections and arithmetic twists required this separate primary comparison.
SCOPE: Exactly TARGET via the existing quadratic–quartic factorization and exact marked extension; includes proper-map verification and an origin test, but no rank algorithm, rational-point completeness, changed quadratic field or integer exclusion.

Inputs are audited L109 and L110, retaining the exact extension v²=z,
original s, every exceptional chart and fixed minus-three field. Review
must distinguish a dimension-one Prym abelian variety from an actual
genus-one quotient over Q, and a genus-one curve from an elliptic curve
with a proved rational origin. Neither quotient nor origin is assumed.

Plausible use: an actual Q-morphism could restrict rational images of
the marked locus while unmarked rank remains unavailable. Point
completeness, degree-nine root recovery, remaining factors, both L095
integer systems and minus-eleven remain independent gaps.

Review result: the primary construction supports the bounded test below.
This is source readiness, not an instance construction or a new theorem.
No quotient equation, twist constant, origin or point list is computed
in this literature-only turn.

## Precise sources and applicability

Nils Bruin, *The arithmetic of Prym varieties in genus 3*,
Compositio Math. 144 (2008), 317–338, DOI 10.1112/S0010437X07003314;
inspected [arXiv:math/0408069v2](https://arxiv.org/pdf/math/0408069v2),
31 May 2006, **Section 2.2, manuscript pp.4–5**, including
**Proposition 2.2 and its proof**. For a squarefree model
`y²=f1(x)f2(x)` with both factors of even degree over K, this section
constructs the cover `y1²=f1(x), y2²=f2(x)` and its projections to the
two factor curves; the map to the base sends y to y1*y2.
The proposition identifies the corresponding product of Jacobians
with the Prym. Its proof checks pushforward/pullback of generic
divisors and then the product comparison. Our proposed map needs the
explicit projections, not the stronger polarized-isomorphism claim.
Remark 2.3 distinguishes conjugate factors and Weil restriction;
Remark 2.4 distinguishes a nonsplit genus-zero base. Here L110 already
has a Q-rational parameter and factors over Q, so those alternatives
need not be introduced. **Theorem 5.1 concerns a genus-three base**
and is not the theorem to apply to L109's genus-two base.

Jordan Docking, *2-infinity-Selmer rank parities via the Prym
construction*, J. Number Theory 265 (2024), 208–225,
DOI 10.1016/j.jnt.2024.06.009; inspected
[arXiv:2108.09564v2](https://arxiv.org/pdf/2108.09564v2),
24 July 2023, **Section 2 and Table 1, manuscript p.4**.
Section 2 works over a number field; its extra rational-point
assumption applies when the base genus is three. The double cover
attached to rational two-torsion is specified only up to a constant
square class. **Table 1, Case II** explicitly gives the genus-two
quadratic–quartic case, with cover equations and quartic Jacobian.
This confirms the relevant base genus, but does not choose L109's
twist or identify a quartic with its Jacobian absent a rational point.
No rank-parity or Sha-dependent assertion is used.

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. 78 (2009), 2347–2370,
DOI 10.1090/S0025-5718-09-02255-8; inspected
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008, **Section 8, manuscript pp.14–15**, from the opening
rank discussion through the displayed formula for gamma(delta).
For factorization over L, the two factor curves have reciprocal
twists, and rational points on a covering give points on them whose
x-coordinate is in the base field. Recovering points on the original
curve still requires lifting. This explains the downstream use and
why a genus-one quotient alone is not a rational-point classification.
The paper's full two-cover D_delta is not automatically our degree-two
marked cover; no identification with it or full descent computation
is assumed. Its twist-norm algorithm is not needed once the exact
marked square class is available directly from L110.

Reuse and rechecked primary Stacks sources, accessed 2026-10-20:
[Theorem 53.2.6, 0BY1](https://stacks.math.columbia.edu/tag/0BY1)
identifies transcendence-degree-one fields with normal proper curves
and nonconstant morphisms; its proof extends the rational map across
the whole nonsingular source. It applies after verifying the field
inclusion, not from a guessed affine formula.
[Section 53.12, 0C1B](https://stacks.math.columbia.edu/tag/0C1B)
gives Riemann–Hurwitz for smooth proper curves and a generically
etale map, including residue-degree contributions to ramification.
[Section 105.2, 072J](https://stacks.math.columbia.edu/tag/072J)
requires a rational section in addition to a smooth proper connected
genus-one curve to call it an elliptic curve. These results are
imported; no general reproof is useful for the proposed specialization.

## Bounded next-turn specification

Use audited L109 and audited L110. L110's canonical proof contains
its completed critical audit despite older pending-audit language in
the supplied overview. Preserve its exact u,z,s and its infinity and
denominator charts. The two even-degree factors already recorded in
L110, with their constants, are the only factorization proposed here.

First remove only explicitly verified rational-square multipliers
from L110's z, and compare its square class with the quadratic factor.
Seek an exact identity `z=c*a(T)*rho²` in Q(B), with c in Q*, a the
recorded quadratic factor and rho a nonzero rational function. Compute
c and rho in the research attempt; neither is asserted here. A
constant may instead be distributed between the two factors, provided
their product remains the original sextic and the identity is exact.
This is a finite rational-function comparison, not a search over
unbounded covers or twist classes.

If that comparison succeeds, instantiate Bruin's two-equation model
using the verified marked generator. Give maps in both directions
between its function field and Q(B)(v), v²=z, retaining W as the
product coordinate. Verify both compositions, nonzero denominators
and nonconstant projection to the quartic factor curve. Prove the
projection has degree two (or report its actual verified degree);
identify its involution/fixed field rather than inferring a quotient
from a dimension count. Check squarefreeness, geometric integrality
and genus on the smooth proper models. Use 0BY1 to extend across
all missing affine values, retaining L109's normalized-unit rule.

Test for an exact rational origin by first checking points above
T=2, T=−2 and infinity on the normalized models, then, only if needed,
the finite integers T from −10 through 10. Verify any point exactly
and distinguish a point of the quotient from a rational lift to D.
Failure of this small origin test proves no absence of rational points;
the valid output may remain a genus-one curve without a chosen origin.
No Weierstrass conversion or Mordell–Weil computation is required for
this unchanged target. Retain the original s on the covering: it
need not descend to the quotient, and no inverse quotient map is
expected. Record the other factor's square condition as a lifting
requirement; rational images must not be promoted to marked points.

Continue this route if the exact marked Q-form gives a verified
proper genus-one quotient and a concrete rational-image/lifting
interface. Park this specific factor-cover implementation if the
square-class match, field identities or proper-model verification
fails within the single attempt; a failed match does not rule out
all possible genus-one morphisms. No rank or point completeness
claim is licensed by construction success. A later arithmetic target
outside this scope needs its own assessment.

## Search, duplicates and limits

Queries included `unramified double cover genus 2 curve genus 3
elliptic quotient Prym f1 f2 Bruin`, `genus 2 unramified quartic Prym
Bruin`, `2-infinity-Selmer rank parities via the Prym construction`,
and exact coefficient variants `7+52T`, `275 704 3388 curve` and
`275 704 Prym curve`. Exact-instance searches returned no matching
quotient among inspected results; this is not novelty evidence.
Followed Docking's reference to Bruin's construction and used the
relevant hyperelliptic section, rather than the unrelated base-genus-
three theorem suggested by the paper title. Other search leads,
including genus-four Pryms and non-simple abelian varieties, were
not read and are not premises.

Reuse the exact-polynomial/Putz comparison already documented in
`2026-10-20-pair-genus-two-explicit-model.md`; no claim about all
unread Putz material or repositories is made. Compared the ready
rank-lower assessment, history/383 and ATTEMPTS/050: their bounded
detector supplies no classes and is not enlarged. The full-descent
backend park, direct-scaling stop and standalone seven-adic witness
remain intact; none prevents this different, independently testable
factor-curve construction. L108's unfinished work is preserved.

Rechecked [Mauldin's primary formulation](https://sites.math.unt.edu/~mauldin/beal.html):
positive integers and exponents greater than two, with a prime common
to all three bases. The nominated AMS page again returned HTTP 403;
its current contents were not read. This repeats the recorded access
qualification and does not obstruct the unchanged mathematical target.
Mathlib coverage for the full Prym/subcover result was not checked;
no absence or formalization claim is made.

Completed work: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED;
actual task type literature_comparison. General construction is known;
no new instance result, lemma, mathematical script or proof/DAG change.
Mathematical exploration usage remains zero since history/383.
