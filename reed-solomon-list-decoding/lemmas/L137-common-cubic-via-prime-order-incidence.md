# L137 — Common cubic from prime-order incidence and dual-4-net exclusion

## Hypotheses

Retain exactly L135's setup: q=137,
T={16,64,70,102,112,118,121} in the auxiliary F_137,
E=F_65537, F=F_(65537^28), H=<19139> of order 1024, k=64,
an arbitrary 61-subset C of H, and an arbitrary bijection sigma from
(T times F_137) disjoint union four dummy points onto H minus C.
Write x_(t,y)=sigma(t,y), and let K be E or F. No embedding of
F_137 into K is assumed.

For each P=(u,v) in F_137^2 let g_P in K[X] have degree at most two.
Zero and repeated polynomials are allowed. Assume g_P(x_(t,y)) has
a common value d_(t,y) on A_(t,y)={P:u+tv=y}, and set

\[
 g_0=g_{(0,0)},\qquad
 V=\operatorname{span}_K\{g_P-g_0:P\in\mathbf F_{137}^2\},\qquad
 \dim_K V=2,\qquad W=g_0+V.
\]

Let I be L135's retained directions: all seven if there is no
exceptional evaluation level set, otherwise the six after omitting
the entire direction of the unique exceptional set. Define

\[
 \ell_{t,y}=\{g\in W:g(x_{t,y})=d_{t,y}\},\qquad
 p_{t,y}=\ell_{t,y}^{*},\qquad
 D_t=\{p_{t,y}:y\in\mathbf F_{137}\}\quad(t\in I),
\]

in the projective dual of the projective completion of W.

## Conclusion

All the retained components D_t lie on a single projective line
defined over K. Consequently there is one nonzero homogeneous cubic
Q over K vanishing on their entire union; Q can be chosen as L^3
for a nonzero linear form L over K. The union has 822 or 959 distinct
points, according as six or seven directions were retained.

The separate critical audit on 2026-10-28 accepts this local
specialization; it is not a candidate resolution of the list-decoding problem.
The statement is conditional; no span-two assignment is constructed
and no nonvacuity is asserted. Further consequences for coefficient
span, span three, partial retention, the cap 1532495 and RS transfer
are outside this step. No cubic uniqueness or factor descent is claimed.

## Proof

**Source scope.** The pre-invocation SPECIALIZE
[assessment](../drafts/literature/2026-10-28-l136-common-cubic-gluing.md)
covers this common-containing-form target and the following incidence
specialization. L135 supplies distinct K-rational dual points; L136
supplies the cyclic labeling of every ordered triple and its cubic.
The new work below verifies the simultaneous incidence hypotheses of
the known exclusion, rather than reproving that exclusion.

Use Gábor Korchmáros and Gábor P. Nagy, *Group-labeled light dual
multinets in the projective plane (with Appendix)*,
[arXiv:1710.00172v1](https://arxiv.org/pdf/1710.00172v1),
30 September 2017, Lemmas 2.2, 2.4 and 2.5, printed pp. 3–4.
They give equal line-intersection sizes, the explicit principal loop
relabeling and its line-intersection subloop. We specialize the explicit
relabeling to the additive cyclic group; no divisibility claim for an
arbitrary quasigroup subloop is used.

Use Norbert Bogya, Gábor Korchmáros and Gábor P. Nagy,
*Classification of k-nets*, European Journal of Combinatorics 48 (2015),
177–185, [DOI](https://doi.org/10.1016/j.ejc.2015.02.019), inspected
[arXiv:1601.08009v1](https://arxiv.org/pdf/1601.08009v1),
Corollary 5.4, printed p. 13. It excludes an ordinary embedded dual
4-net of order n>=7 with a cubic-containing derived triple. We use it
over an algebraically closed field of characteristic p>n, p different
from 2 and 3. This conservative scope also covers the reducible cases
handled in Corollaries 3.4 and 4.4, pp. 7 and 9. The arXiv wrapper
is dated 29 January 2016, while the manuscript internally is dated
15 February 2018; pagination here is the manuscript's. The assessment
records its proof-case coverage, including the source's omitted
cuspidal calculation. This is a theorem import, not an independent
reproof of the classification or of that omitted calculation.

**Geometric and cyclic inputs.** Work first over an algebraic closure
Kbar of K. In a K-basis h_1,h_2 of V the dual points have representatives

\[
 p_{t,y}=[h_1(x_{t,y}):h_2(x_{t,y}):g_0(x_{t,y})-d_{t,y}].
 \tag{1}
\]

By L135 these are nonzero, injective within each component and distinct
across components. Extension to Kbar preserves these distinctions and
all incidences, by the minor/determinant argument in L136. In particular,
each D_t has 137 points and all components are disjoint.

For every ordered triple a,b,c of distinct elements of I, L136 gives
injective maps alpha_1,alpha_2,alpha_3 from G=(F_137,+) onto
D_a,D_b,D_c with alpha_1(r),alpha_2(s),alpha_3(r+s) collinear for
every r,s. Explicitly its permutations use
lambda=(b-c)/(b-a), mu=(c-a)/(b-a) and
alpha_1(r)=p_(a,lambda^(-1)r),
alpha_2(s)=p_(b,mu^(-1)s), alpha_3(z)=p_(c,z).
All these operations are only on the auxiliary index set. Thus every
ordered triple is a cyclic light dual multinet over Kbar. L136 also
provides a nonzero cubic over K containing each such triple.

**The prime-order specialization on one line.** Fix one ordered triple
and a line m meeting its first two components. Choose u,v in G with
alpha_1(u),alpha_2(v) on m. These points are distinct. The prescribed
incidence puts alpha_3(u+v) on their unique joining line m.

Apply the explicit principal relabeling of the cited Lemma 2.4:

\[
 e=u+v,\qquad
 \beta_1(x)=\alpha_1(x-v),\quad
 \beta_2(y)=\alpha_2(y-u),\quad
 \beta_3(z)=\alpha_3(z),\qquad
 x\circ y=x+y-e.                                      \tag{2}
\]

The three beta_i(e) are on m. Unlike an arbitrary loop isotope, this
one is explicitly a group: phi(x)=x-e is a bijection to (G,+), and
phi(x circ y)=x+y-2e=phi(x)+phi(y). Its identity is e and its order
is the prime 137.

For completeness, the line-subloop conclusion applies to this very
relabeling, not to an unspecified additional isotope. Put
S_i={x:beta_i(x) lies on m}. Each S_i contains e. The inclusions and
equal cardinalities of Lemma 2.2 applied to (2) imply
S_1 subset S_3 and S_2 subset S_3, using x circ e=x and e circ y=y;
therefore S_1=S_2=S_3=S. The same lemma's product and division
inclusions make S a subloop, as in Lemma 2.5. Under phi it is a
subgroup of (G,+). Lagrange's theorem now gives

\[
 |m\cap D_a|=|m\cap D_b|=|m\cap D_c|=|S|\in\{1,137\}. \tag{3}
\]

This calculation is the needed cyclic specialization of the imported
line-subloop lemma; it does not assume Lagrange's theorem for loops.
Because L136 permits any ordering of the triple, (3) holds for a line
meeting any two of its components. If the value is 137 the entire
triple lies on m. If the triple is not wholly collinear, every such
line therefore meets its three components in exactly one point each:
the triple is an ordinary dual 3-net. This accounts for extra
incidences, rather than excluding them as an initial assumption.

**Propagation and the simultaneous dichotomy.** Suppose first that
some triple D_a,D_b,D_c is wholly contained in a line m. For any
other retained direction d, use the ordered triple a,b,d. The line m
meets its first two components in 137 points each. Its equal
intersection sizes from Lemma 2.2, or (3), give |m intersect D_d|=137.
Thus every D_d lies on this same line. No agreement between the
different triples' index permutations is needed: their images are the
same actual components, and the line-intersection cardinalities are
intrinsic.

If instead the full retained union is not collinear, this propagation
shows that no triple is wholly collinear. Consequently every triple
is an ordinary dual 3-net by (3). Select any four distinct retained
directions; this is possible since |I| is six or seven. Take any line
meeting any two of the four components. The triple formed by those
two and either remaining component meets this line in exactly one
point per component. Applying this to both remaining components
proves that the line meets all four in exactly one point each. The
four disjoint components, each of size 137, therefore form an ordinary
embedded dual 4-net. In particular the lines determined by pairs from
two fixed components cannot repeat for different pairs, since a line
has just one point of each component. Repeated polynomial images
g_P and potentially repeated connecting lines were permitted initially;
they have not been used to shortcut this exact incidence argument.

**Excluding the noncollinear branch.** In the ordinary dual-4-net branch,
any three of its components form a derived ordinary dual 3-net. By
L136 they lie on a nonzero homogeneous cubic over K, hence over Kbar.
The field Kbar is algebraically closed of characteristic 65537;
n=137>=7 and 65537>137, with characteristic neither 2 nor 3.
All the hypotheses of the cited exclusion, in the conservative scope
above, are now satisfied. Corollary 5.4 rules out this branch.
We need no assertion of irreducibility, nonsingularity, uniqueness,
reducedness or common factors of the triple cubics. Reducible
possibilities are included in the cited exclusion. In particular, the
ordinary-net property was proved before the exclusion was invoked.

To make the curve convention explicit even if the chosen form has
repeated factors, factor it over Kbar and take the product R of its
distinct irreducible homogeneous factors. Its zero set is unchanged
and its degree d is between one and three. If d<3, multiply R by
3-d pairwise nonproportional linear forms, none a factor of R.
The algebraically closed field Kbar is infinite, so these choices exist.
This gives a reduced degree-three curve still containing the derived
triple, to which the same exclusion applies. These auxiliary factors
are used only over Kbar; no factor descent is asserted.

The retained union must therefore be wholly collinear over Kbar.
This proves the geometric part of the conclusion.

**A containing form over K.** Choose two distinct points in this union
and their actual K-vector representatives from (1). Their cross product
is nonzero and has entries in K. It defines a nonzero linear form L
whose line contains the two points. By uniqueness of a projective line
through distinct points, its extension to Kbar is the line containing
the full retained union. Hence L vanishes on every retained K-point.
The polynomial Q=L^3 is a nonzero homogeneous degree-three form over
K, since a polynomial ring over a field is an integral domain. This
is exactly L136's line-branch descent argument applied to the full
union. No factors of an imported cubic are descended. Disjointness
and |D_t|=137 give the stated union sizes 6*137=822 or 7*137=959.

This finishes the approved common-form implication. It makes no
further claim about realizing or excluding the original coefficient
assignment, and uses neither (W1)–(W5) nor the failed arbitrary-direction
omission probes. No numerical evidence or rank certificate is needed.

**Separate critical audit, 2026-10-28.** The unchanged pre-invocation
SPECIALIZE assessment cited above covers this exact common-form target.
The audit accepts the implication, with the preceding nonreduced-curve
clarification, and makes no downstream coefficient-collapse claim.

The audited L135 and L136 hypotheses agree with this statement: the
same arbitrary core and bijection, both permitted K, all repeated
messages, and the prescribed six or seven complete directions are
retained. A basis of V exists over K because its dimension is exactly
two. The representative (1) is nonzero by the nonzero retained normal.
L135 gives pairwise distinction across as well as within components.
Nonzero minors remain nonzero over Kbar. L136's permutations use only
F_137 and give incidence for every ordered pair of labels in every
ordered retained triple. No compatibility of the different permutations
is a further hypothesis.

The source's principal isotope is exactly (2): division in (G,+)
is subtraction, so (x-v)+(y-u)=x+y-e. Its identity is e and its inverse
at x is 2e-x. Under phi(x)=x-e these are the ordinary group identity
and inverse. This verifies a group isomorphism before divisibility is
used. Each S_i contains e. The source's product inclusions give
S_1,S_2 subset S_3, and its equal-cardinality assertion makes all three
sets equal. The product and division inclusions then give closure and
inverses for this same S, so phi(S) really is a subgroup. Thus (3) has
no hidden appeal to Lagrange for a general loop. Since 137 is prime,
neither a proper long line nor an intermediate line-intersection size
can survive.

For propagation, the two fixed full components on m belong to every
triple (a,b,d); their cardinality 137 forces all of D_d onto m.
This uses the actual images, not compatible relabelings. Conversely,
noncollinearity of the full union excludes a full collinear triple.
For any selected four directions and any line meeting two components,
the two triples formed with each of the other directions force exactly
one point from each of all four. This verifies the ordinary embedded
dual-4-net condition, including lines not originally named by a chosen
label pair. A connecting line cannot serve two different pairs from
fixed components because it has only one point of either component.
Repeated g_P therefore introduce no unexamined exception.

Primary statements were rechecked in the versioned sources already
covered: Korchmaros–Nagy, Lemmas 2.2/2.4/2.5, pp. 3–4;
Bogya–Korchmaros–Nagy, definitions pp. 2–3, Proposition 3.2 and
Corollary 3.4 p. 7, Corollary 4.4 and the reducible-case reduction p. 9,
and Theorem 5.3/Corollary 5.4 p. 13. These cover regular (including
pencil), conic-line and irreducible cases under the conservative
characteristic assumption. Here 65537>137>=7 and the characteristic
is neither 2 nor 3. In the irreducible formulation, each point of the
fourth component is a perspective center off the derived triple:
every line from it to that triple has exactly one point in each
component by the just-verified ordinary-net property. There are 137
distinct such centers. This checks the application rather than assuming
a perspective condition from injectivity. The cited exclusion is
imported; the source's omitted cuspidal computation is still not
independently reproved or certified by this audit.

Finally, two distinct K-points on the common line have independent
representatives, so their cross product is nonzero over K. Uniqueness
of their joining line after extension shows its K-form vanishes on
the entire union. Cubing is in the polynomial ring over K and cannot
give the zero polynomial. The component counts yield 822 or 959
distinct points. Neither finite-field polynomial-function identities,
cubic uniqueness nor descent of irreducible factors is used.

Only L135 and L136 are direct local mathematical inputs; L030's setup
is inherited. No DAG edge, numerical certificate or failed omission
probe is added. The concise
[audit record](../drafts/audits/2026-10-28-l137-critical-audit.md)
records acceptance as verification of a source-backed specialization,
not as progress beyond the cited geometric classification.

## Mathlib

Full matching coverage for this simultaneous incidence specialization,
light dual multinets and the algebraic dual-4-net exclusion has not
been checked. Supporting group facts are subgroup-order divisibility
(Lagrange's theorem), cyclicity of the prime-field additive group,
and the explicit isomorphism (2); geometric support is projective
incidence via minors and the line through two distinct rational points.
Precise Mathlib names for these supporting results were not checked.
No absence claim or novelty claim beyond the cited specialization is
made. The separate audit accepts the local proof with the source-import
qualification stated above; it does not claim formal verification.
