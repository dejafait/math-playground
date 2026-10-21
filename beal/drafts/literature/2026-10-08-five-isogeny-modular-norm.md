# Modular norm test — theorem coverage reviewed

TARGET: Compute the norm of L033's f along FNS's modular j-map and test whether its specialization gives nonconstant fifth-power-class information for the 54a1 branch.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact X0(11)/descent/norm and X_0(11)/j/fifth/norm terminology, and Stacks norm/principal-divisor/pushforward and finite-locally-free/base-change terminology; inspected the primary statements and proofs listed below and checked local construction, source review and saturation records.
SOURCE_EVIDENCE: Stacks tags 02RT, 0BD2, 0CCK, 0CCL and 02K9 inspected 2026-10-08; FNS June 10, 2019 author manuscript Section 7.2 printed pp.25–27 (PDF indices 24–26), complete map coefficients, fiber transport, Table 5 and equation (7.4) inspected; existing L033 supplies f, its divisor and normalization.
COMPARISON: Known norm/divisor and determinant-base-change theorems cover the machinery; neither the inspected general statements nor inspected FNS passages supply the exact normalized norm of this f or its fifth-power-class usefulness. A bounded specialization is justified, without a general-theorem reproof or novelty claim.
GAP: Determine the complete degree-twelve norm including its rational scalar, check exceptional fibers and equality with the transported field norm, and distinguish a nonconstant rational representative from nonconstant information modulo fifth powers; no such result is derived in this review.
REASON: Essential theorem-level coverage is now available for the unchanged target; the next turn may perform its one bounded calculation without further browsing unless a hypothesis changes.
SCOPE: L033 on E0 over Q, FNS's degree-twelve modular map to P1_j, and its 54a1 transported fiber over K; no group basis, Fisher formula, GRH-dependent computation, rank claim, other twist or fourth-power cover.

## Primary general inputs

The Stacks Project online versions were inspected on the CHECKED date; stable tags are the citation identifiers.

[Tag 02RT, Lemma 42.18.1](https://stacks.math.columbia.edu/tag/02RT): over its dimension-function base, integral schemes of equal dimension locally of finite type, a dominant proper morphism p and nonzero rational f satisfy div(Nm(f)) = p_*div(f). The entire proof was read: reduction to a finite affine map and the sum of orders weighted by residue-field degrees, invoking Algebra Lemma 10.121.8. This accounts for multiplicities at ramified images; replacing pushforward weights by ramification indices is not the stated formula. The theorem determines a divisor, not a multiplicative scalar. It is imported, not independently reproved.

[Tag 0BD2, Lemma 31.18.6](https://stacks.math.columbia.edu/tag/0BD2): a finite locally free map of degree d has a canonical norm compatible with arbitrary base change. Its full proof defines the norm as the determinant of multiplication on a local free rank-d algebra, checks independence of basis and gluing, and handles a vanishing element after specialization to a field. This covers fibers with multiplicities as finite algebras, rather than only products at distinct geometric points. For a rational function, restrict to an open where it is regular; for an invertible class restrict further where it is a unit. Zero/pole fibers require separate treatment and cannot be substituted into a generic quotient formula. The determinant norm on a field fiber is the field norm by the same definition; a product of field factors requires the whole algebra. No reproof is needed.

[Tag 0CCK, Lemma 53.2.3](https://stacks.math.columbia.edu/tag/0CCK) gives flatness for a nonconstant map of curves with normal target; its proof uses torsion-freeness over the target DVR. [Tag 0CCL, Lemma 53.2.4](https://stacks.math.columbia.edu/tag/0CCL) gives finiteness for a proper curve mapping nonconstantly to a separated target; the proof excludes positive-dimensional fibers and invokes proper/quasi-finite finiteness. Their full statements and proofs were inspected. The source E0 and target P1 are smooth projective integral curves over Q; the cited degree-twelve map is nonconstant, so their hypotheses match. [Tag 02K9, Lemma 29.49.2](https://stacks.math.columbia.edu/tag/02K9), statement and proof inspected, identifies finite flat with finite locally free on a locally Noetherian base. Thus the required determinant specialization theorem has the appropriate map hypothesis here. These are applicability checks of known results, not a computation of the proposed norm.

## Primary modular-map input

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113, [final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), internally June 10, 2019. Section 7.2 pp.25–27 supplies the degree-twelve transport through cyclic order-eleven subgroups, irreducible fibers for the five labels, E0's model, j=(a(x)+b(x)y)/(x-16)^11 with all coefficients, and the eliminated relation (7.4). These passages were read in full for this review; their field statement is separate from conditional Selmer dimensions. The stated branch values are 0, 1728 and infinity. The y-reconstruction caveat appears in Lemma 7.6's proof on p.28. No additional Chabauty result or GRH-based elimination is imported.

Use those exact primary formulas at the later calculation; the eliminated polynomial alone is not automatically a certified integral fiber model at every value. Denominator cancellation, multiplicity and coordinate-reconstruction failures must be checked rather than deleting their points.

## Local overlap and failure comparison

L033 was read through its finite-class transport argument. Its already verified identity f(P)f(-P)=-(x(P)-5)^5 concerns the x-coordinate degree-two cover, not the full modular norm. It can be a consistency check only. The construction assessment, the even-C source review, history 083 and 085, and ATTEMPTS/008 were searched for this target and relevant failures. No completed modular-norm calculation is recorded in these scoped inputs. This is not evidence of novelty.

Exact norm searches returned no usable matching formula; unrelated numerical-descent hits were not treated as mathematical sources. The specialized Fisher sources remain unread, parked leads as previously documented. They are unnecessary for the general norm machinery now inspected, so no endpoint retry was made. Foundation 15 remains usable only for its already assessed connecting-map and finite-class scope.

## Approved bounded specialization and decision test

Essential mathematical inputs are L033 and L032, plus the precise external statements above. In the next research step compute N in Q(j) for the complete modular map. Use pushforward of L033's divisor to constrain it, and determine the actual scalar by an exact determinant, resultant with justified corrections, or complete regular fiber evaluation. Verify any chosen algebra presents the full degree-twelve function-field extension and does not double it via the x-coordinate involution. Prove the exceptional zero/pole fiber handling, including any apparent (x-16) denominator cancellation. Retain the branch fibers even though positive original solutions have 0<j<1728.

Specialization must identify the complete transported fiber algebra with K, not merely choose one embedding. Establish the equality between the specialized rational norm and N_{K/Q}(f(P0)) on the actual solution domain. Keep L032's j and fourth-power identities, positivity and primitivity explicit. Scalar and class information, this equality, and any arithmetic consequence remain unresolved; this literature turn supplies no norm value or new lemma.

Compare the final class in Q(j)^*/Q(j)^{*5}, not just whether its representative varies with j. The norm/divisor theorem is especially relevant to detecting automatic powers from the existing divisor of f; do not presume that a varying function gives a varying class. Continue only with a proved nonconstant class that yields a necessary test after specialization. A constant class or tautology parks this compression mechanism, while leaving the original descent available. Missing arithmetic data must not silently become premises. All four independent twists and infinitely many signatures remain open.

Mathlib: full matching norm/divisor, finite-algebra specialization and modular-map coverage not checked. The cited primary theorems suffice for this bounded informal specialization; unknown library coverage is not absence.
