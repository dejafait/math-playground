# Proposed actual Wronskian second-moment comparison

TARGET: Assess whether the dyadic second moment of L380's normalized actual Wronskian is c log H+o(log H) for an explicit c>0.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the actual-Wronskian assessment and searched the specific first-mean records; targeted twisted-second-moment, nonconjugate-moment and different-vertical-line queries located the primary comparisons below, with no matching theorem for this pair established.
SOURCE_EVIDENCE: Young, Arch. Math. 95 (2010), 539–548, (2.1)–(2.3), (3.4) differentiation, Lemmas 4–5 and full Lemma 5 proof, pp. 540–543; Bui–Hall arXiv:2304.05178v1, Proposition 1 and Section 3, pp. 7–8; Bettin–Chandee–Radziwill arXiv:1411.7764v1, Theorem 1 pp. 1–2 and Section 3.1 pp. 8–9; L320 proof (4)–(5) and its complete strip argument; reused L368 (5) and the previously inspected DLMF gamma/Dirichlet inputs.
COMPARISON: Young supplies the finite-head opposite-height shifted jet input, rather than L369 (16); none of the inspected theorems supplies the full real-projection square, infinite right-line series or its explicit coefficient. These remain a family-specific specialization, not an imported asymptotic.
GAP: The exact coefficient, its strict positivity, the same-height projection term, uniform tail transfer and dyadic unsmoothing remain unproved; adequate scalar and finite-twist coverage permits one bounded mathematical attempt without presupposing their success.
REASON: Source coverage now identifies a finite-head moment mechanism with a separate analytic cross-term test; a full matching citation does not suffice, and no second-moment result or new lemma is derived in this literature turn.
LITERATURE_REASON: The saved second-moment proposal was REVIEW_REQUIRED and moves beyond the ready first mixed-mean assessment to squared critical-line jets and two right-line factors.
SCOPE: The fixed actual F_0,G,A of L366, Wcal=(F_0'G−F_0G')/(A²(1+t)²log(2+t)), positive heights, ordinary real derivatives and H tending to infinity; no RH, simplicity, independence, noncoincidence, discriminant sign or common-zero count bound.

## Use and bounded review

The main gap remains global actual-theta mixed positivity and the total
L367 signed margin. L380's audited first mean vanishes and has no
certified sign. A positive second-moment main term would supply a
different quantitative input for a later sign-set or localization test.
It would not itself supply a Wronskian zero away from common zeros;
L373's reset obstruction and actual common-zero control remain separate.
No second-moment formula or positive coefficient is asserted here.

The next source comparison should reuse the specific Young and Bui–Hall
notes in the existing Wronskian assessment, then inspect only primary
theorems and essential proof cases needed for this exact mixed statistic.
Check permitted shifts and rational twists, derivative uniformity,
truncation errors, the complete real projection and infinite Re s=5/2
factors. The prior assessment does not license differentiating an
unqualified moment error or imposing response-phase windows. No broad
repeated Wronskian search is requested.

Continue to a separately approved calculation only if coverage supports
this target or a precisely stated useful weaker nondegeneracy bound.
If essential moment inputs remain inaccessible or cannot cover the tails
and jets, park that implementation; do not repeat the first-mean
calculation or infer a positive constant. The c log H scale is a target
to test, not an established estimate.

Essential local inputs for a later specialization are L366 (1), L368 (3)
and L380 (3)–(8). L369 (16) is a scope comparison, not a squared-moment
theorem. Full matching Mathlib coverage is not checked. Low indices,
heights above forty, endpoint margin, global positivity and noncommon-zero
localization remain unresolved.

## Completed primary comparison

**Young**, *A short proof of Levinson's theorem*,
[Arch. Math. 95 (2010), 539–548](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
Lemma 5, p. 543, assumes positive integers h,k with
hk≤T^(2θ), fixed θ<1/2, complex shifts |α|,|β|≪1/log T,
and smooth w satisfying 0≤w≤1, support in [T/4,2T], and
w^(j)≪_j(T/log T)^(-j) for every j≥0. Formula (4.5)
retains both functional-equation diagonals hm=kn, with error
O_(A,θ)(T^(-A)) for each fixed A. The complete proof treats both
off-diagonal orderings via logarithmic separation and integration by
parts. The Cauchy argument following (3.4), p. 541, uses holomorphy
and uniform complex-shift errors to obtain log-normalized derivatives.
This supports finite-head opposite-height jet moments; it does not
permit a shift of size two or a fast carrier in w. The two diagonals
must be combined before using the apparent singularity α+β=0;
unequal-radius shift contours are a possible implementation to check.
All normalization, diagonal evaluation and smooth-weight applicability
for this family are deferred.

**Bui–Hall**, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/pdf/2304.05178v1),
Proposition 1 and (6)–(8), pp. 7–8, concern polynomial differential
operators and the specified Möbius mollifier, of length T^ϑ with
ϑ<4/7. P(0)=0 is required. Read the derivative expansion and the
Cauchy–Schwarz control of its errors. These are method comparisons;
replacing that mollifier by ζ(5/2+it) is not a specialization of the
proposition. No Hardy sign-set theorem gives a noncommon Wronskian zero.
The earlier assessment's sign-set and reset qualifications are reused.

**Bettin–Chandee–Radziwiłł**, *The mean square of the product of
ζ(s) with Dirichlet polynomials*,
[arXiv:1411.7764v1](https://arxiv.org/pdf/1411.7764v1),
Theorem 1, pp. 1–2, treats an unshifted modulus square with smooth
weight φ(t/T), φ supported in [1,2], and
A(s)=Σ_(n≤T^θ) a_n n^(-s), a_n≪n^ε, θ<17/33.
Its main term retains a_d conjugate(a_e)/[d,e] and
log(t(d,e)^2/(2πde))+2γ; its error is
O(T^(3/20+ε)N^(33/20)+T^(1/3+ε)), N=T^θ.
Read Section 3.1's collision parametrization and Mellin diagonal,
pp. 8–9. The longer-polynomial improvement and subsequent off-diagonal
machinery are not imported. This checks the stronger standard
terminology and the necessity of gcd collisions, but the theorem has
no stated shifted error to differentiate and no real-projection square.

**Pliego**, *Twisted mixed moments of the Riemann zeta function*,
[arXiv:2211.11450v1](https://arxiv.org/pdf/2211.11450v1),
(1.3)–(1.5) and Theorem 1.1, pp. 1–2, use three critical-line
factors at dilated heights and a finite polynomial, with divisibility
and, in the indicated cases, an abc-type assumption. The present fixed
vertical lines and derivative statistic are outside that statement.
No proof is imported after this hypothesis mismatch.

Additional scalar lead inspected but unused: Platt–Trudgian,
[arXiv:1402.3953v1, Theorem 1, p. 2](https://arxiv.org/pdf/1402.3953v1#page=2),
is a critical-line value bound, not a uniform jet or mixed-moment theorem.
Its proof is not needed or imported. DLMF 25.9.1–3 (version 1.2.8)
state fixed-real-part approximate functional equations, not a
derivative-uniform moment. These do not by themselves license jets.

## Scalar coverage and the remaining mathematical test

The complete local strip proof of L320 (4)–(5) was read, including
the polynomial preliminary growth, reflected boundary, damping,
horizontal edges and sequential limits. Its fixed-strip bound is an
available input, not a new convexity assertion here. Together with
the existing gamma bounds it may control the endpoints of a horizontal
t-contour displacement for products containing two same-height
critical-line factors. Ordinary Cauchy's integral theorem and Cauchy
derivative estimates are named standard inputs. Their applicability,
the allowed displacement, exclusion of poles at high real t, derivative
disks and the resulting normalized error must all be established in
the mathematical turn. No carrier is to be hidden in Young's slow
weight, and no conjugated function may be treated as holomorphic
without its explicit zeta representation. This is an independently
testable residual estimate, not missing access to a moment source.

Use L368 (5)'s absolutely convergent right-line jets for a finite
head plus its complete absolute tail. Young with h=k=1 is the proposed
source for unweighted critical-line jet moments used in tail control.
A uniform normalized mean-square tail bound is still to be written;
pointwise right-line convergence alone does not establish it.
The fixed-head height limit must precede removal of the head, unless
a uniform alternative is proved. L369's longer scalar truncation and
linear mixed mean cannot simply be squared. Dyadic smoothing must
be justified for the nonnegative total statistic, including endpoints.

Searches actually made include “zeta twisted second moment same sign
product chi derivatives rational twist”, “zeta non-conjugate moment”,
“Hardy twisted second moment”, “zeta mixed moments different vertical
lines”, “zeta Wronskian second moment”, “zeta 5/2 second moment
derivative”, and the Bettin–Chandee–Radziwiłł title. Search snippets locate
leads only. No matching second-moment result was found in the
specific first-mean draft, assessment, failure record or history;
the supplied overview already records their scope and stop evidence.
Neither a failed search nor this SPECIALIZE decision certifies novelty.
The local-extrema second-moment article returned by the exact query is
an unread lead; neither its snippet nor any conditional logarithmic-
derivative moment is used as evidence for this statistic.

The new ready continuation is recorded separately in
`drafts/literature/2026-10-08-wronskian-second-moment-calculation.md`;
it awaits the supervisor's separate next-turn approval. This completed
review is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It supplies
coverage and a bounded test, not a positive constant, an asymptotic,
a Wronskian witness or progress beyond the sources checked.
