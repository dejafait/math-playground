# L103 — Exhaustive obstruction to projective pole transport

## Hypotheses

Use C012a's E=F_65537, H=<19139> of order n=1024 and
F=F_(65537^28). Let C be the unweighted evaluation code on H of
all polynomials in F[X] of degree at most 63. Fix m>=1 and the
closed simultaneous-column model in
[foundations/02](../foundations/02-pinned-list-model.md).

Let phi(X)=(AX+B)/(CX+D), with A,B,C,D in E and AD-BC nonzero,
have no denominator zero on H and satisfy phi(H)=H. For a function
mu:H -> F^*, consider the row-wise monomial map

\[
 (T y)(x)=\mu(x)y(\phi(x)),\qquad x\in H.
\]

Assume T(C)=C. The same permutation and nonzero multiplier act on
every row of a received word and message tuple. For a,b in E and
c in E^*, L102's first center row is

\[
 y_{a,b,c}(x)=(x-3)^{64}+\frac a{x-3}
                    +\frac b{(x-3)^2}+\frac c{(x-3)^3}.
\]

L099's first center rows have the form

\[
 z_{\alpha,\beta,\gamma}(x)=x^{64}+\frac\alpha x
                               +\frac\beta{x^2}+\frac\gamma{x^3},
 \qquad \alpha,\beta\in E,\quad\gamma\in E^*.
\]

## Conclusion

Every eligible phi is exactly one of

\[
 \phi(x)=s x\quad\hbox{or}\quad\phi(x)=s/x,\qquad s\in H.
                                                               \tag{1}
\]

The corresponding code-preserving multipliers are exactly
mu(x)=lambda or mu(x)=lambda*x^63, respectively, for lambda in F^*.
Each such T is an invertible code isometry preserving simultaneous
agreement and all list cardinalities for every m.

Nevertheless, for every such T and every a,b,c above, T y_(a,b,c)
is unequal on H to every z_(alpha,beta,gamma). This remains true
even if all three destination parameters are allowed in F, including
gamma=0. Consequently no eligible projective monomial isometry
transports even one L102 center into the literal L099 family, and
in particular none transports the whole family into L100's bounded
family. The result stops only this transport mechanism. It gives no
upper or lower bound on L102's actual fibers and no change to the
955–957 bracket or arbitrary-center safety.

This is a REPRODUCTION using the assessed projective GRS framework
and an elementary finite specialization. No novelty or progress beyond
the checked sources' methods is asserted. The separate critical audit of
2026-10-20 below retains this local proof without a mathematical correction.

## Proof

**Source, relevance and scope.** Marquez-Corbella and Pellikaan,
[arXiv:1508.02187v1](https://arxiv.org/pdf/1508.02187v1), Section 3.1,
Proposition 3.6 (printed p.8), describes GRS projective transformations
with locators (AX+B)/(CX+D) and compatible multipliers proportional
to (CX+D)^(k-1) on the finite denominator-nonzero branch. Its range
2<=k<=n-2 includes k=64,n=1024. Beelen, Glynn, Hoholdt and Kaipa,
[arXiv:1611.04341v1](https://arxiv.org/pdf/1611.04341v1), Section 2,
equations (4)–(8) and Proposition 2.5 (printed pp.3–4), provide the
symmetric-power construction, with a different matrix convention.
These are the known framework imported by the
[prior SPECIALIZE assessment](../drafts/literature/2026-10-20-projective-pole-transport.md).
We do not reprove general GRS equivalence or classify all code
automorphisms. The remaining obligations are this finite H's stabilizer,
the actual unweighted code and complete received-word comparison.
The elementary checks below verify those obligations directly, including
uniqueness of the multiplier for these two permutations. No theorem
about the automorphism group of an arbitrary finite point set is assumed.

The potential use was to transfer L100's below-threshold cap through
one simultaneous-column isometry. The discriminating test is exact
center equality on H; failure for every eligible map abandons only
this route. L102's failed absolute-sieve allowance (ATTEMPTS/085) is
neither retuned nor used as evidence about the actual fiber sizes.

**Exhausting the finite-domain stabilizer.** C012a proves that H
consists of all 1024 roots of X^1024-1 in E, and that 3 is outside H.
Write n=1024 and consider

\[
 P(X)=(AX+B)^n-(CX+D)^n.
\]

For each x in H, the denominator is nonzero and phi(x)^n=1,
so P(x)=0. Its degree is at most n; division by X^n-1, or the
distinct-root bound applied to the remainder, gives
P(X)=u(X^n-1) for some u in E, including the possibility u=0.
Every interior coefficient consequently vanishes. Since n<65537,
the binomial coefficients binomial(n,j) are nonzero in E for
0<=j<=n: all factorial factors are nonzero. Thus, in particular,

\[
 AB^{n-1}=CD^{n-1},\qquad A^2B^{n-2}=C^2D^{n-2}.       \tag{2}
\]

If AB is nonzero, the first equality forces C,D both nonzero.
Dividing the second equality by the first gives A/B=C/D,
contradicting AD-BC nonzero. Therefore AB=0. The first equality
then gives CD=0. Invertibility leaves exactly B=C=0 with A,D
nonzero, or A=D=0 with B,C nonzero. These are phi(X)=sX
and phi(X)=s/X. Since 1 is in H and phi(1)=s is in H, s lies
in H. Conversely, either expression with s in H has no pole on H
and permutes H by subgroup closure. This proves (1), with no
sampling, missing denominator case or assumed dihedral classification.

**Same unweighted code and all its multipliers.** For phi(x)=sx,
the map R_s y(x)=y(sx) sends f(X) to f(sX), preserving degree
at most 63, with inverse R_(s^(-1)). For phi(x)=s/x put

\[
 J_s y(x)=x^{63}y(s/x).
\]

If f(X)=sum_(j=0)^63 f_j X^j, its image is the polynomial
sum_(j=0)^63 f_j s^j X^(63-j). This handles lower degrees and
zero over F without a pole. Moreover J_s^2=s^63 I on all
functions on H, so J_s is invertible and J_s(C)=C. Its multiplier
x^63 is nonzero on H. These are precisely the degree-63 homogeneous
substitutions from the cited construction in the two conventions
now fixed. Multiplication by any lambda in F^* also preserves C.

For completeness no other multiplier for either fixed permutation
can evade the test. If T and its canonical map S=R_s or J_s both
preserve C, then T S^(-1) is diagonal multiplication by a function
d:H -> F^*, and preserves C. Applying it to the constant word 1
gives d(x)=r(x) on H for a polynomial r of degree at most 63.
Applying it to X^63 gives a polynomial q of degree at most 63
with r(x)x^63=q(x) on H. The polynomial r(X)X^63-q(X) has
degree at most 126<1024 and vanishes on H, hence is identically
zero. Since r is nonzero, a positive degree for r would make its
product with X^63 have degree greater than 63. Therefore r is a
nonzero constant lambda. It follows that mu=lambda for R_s and
mu=lambda*x^63 for J_s. This argument permits multipliers over
the full ambient F, so in particular covers multipliers restricted
to E. It is only a local uniqueness verification, not a general
GRS classification reproof.

For any vector column, multiplication by mu(x) is injective. Thus
(T Y)(x)=(T f)(x) if and only if Y(phi(x))=f(phi(x)), with
equality in every row simultaneously. The permutation phi gives
a bijection of agreement sets. Invertibility and T(C^m)=C^m
therefore give bijections of entire closed-ball lists, with the
same error count and cardinality, for every m. The field F and
threshold T=65537^28/2^128 have not changed. We use no separate
row projection or exponent m.

**Scaling case: finite equality forces a false identity.** Suppose
lambda*y_(a,b,c)(sx)=z_(alpha,beta,gamma)(x) for every x in H,
even with destination parameters in F. Put ell(X)=sX-3. Both
X and ell are nonzero on H, since sH=H and 3 is outside H.
Multiplication by X^3 ell(X)^3 gives the polynomial

\[
 R(X)=\lambda X^3[\ell(X)^{67}+a\ell(X)^2+b\ell(X)+c]
       -(X^{67}+\alpha X^2+\beta X+\gamma)\ell(X)^3
                                                               \tag{3}
\]

vanishing at all 1024 points. It has degree at most 70<1024,
so R is identically zero over F. But at r=3/s, a nonzero point
of E, ell(r)=0 and R(r)=lambda*r^3*c is nonzero. This contradicts
the identity. Evaluation at r is performed only after obtaining
the polynomial identity; r need not belong to H.

**Inversion case: the nonzero pole cannot cancel.** Now suppose
lambda*x^63*y_(a,b,c)(s/x)=z_(alpha,beta,gamma)(x) on H.
Put ell(X)=s-3X. Again X and ell have no zeros on H, since
s/x is in H and cannot equal 3. The transformed rational expression is

\[
 \lambda\left[\frac{\ell(X)^{64}}X
       +\frac{aX^{64}}{\ell(X)}
       +\frac{bX^{65}}{\ell(X)^2}
       +\frac{cX^{66}}{\ell(X)^3}\right].             \tag{4}
\]

Clearing X^3 ell^3 gives a polynomial vanishing on H,

\[
 R(X)=\lambda[X^2\ell(X)^{67}+aX^{67}\ell(X)^2
                         +bX^{68}\ell(X)+cX^{69}]
       -(X^{67}+\alpha X^2+\beta X+\gamma)\ell(X)^3.   \tag{5}
\]

The first bracket has degree at most 69 and the last product at
most 70. Thus R is again identically zero by its 1024 distinct
roots. At the nonzero point r=s/3 it instead has the nonzero
value lambda*c*r^69. This is a contradiction. Equations (3) and
(5) cover every s,lambda and every source parameter with c nonzero;
destination parameters may depend arbitrarily on them.

With the remaining center rows zero, T leaves those rows zero.
The scalar contradiction therefore excludes tuple-center equality
for every m as well. This is literal equality of functions on H,
not an inference from rational poles alone: the degree<1024
identities explicitly rule out finite-evaluation coincidences.
No codeword translation, semilinear map, changed domain, changed
message degree or changed field is included. The proof gives neither
an actual large fiber nor a bound for the translated-pole family.
The independent 67/68 safety and source-model gaps remain open.

**Separate critical audit, 2026-10-20.** This audit uses the previously
approved SPECIALIZE scope in
[the audit assessment](../drafts/literature/2026-10-20-projective-transport-critical-audit.md).
It independently checks the symbolic argument above, not a sampled set
of projective maps. No new external theorem, numerical certificate or
stronger conclusion is required. The following checks retain the result.

1. **Actual inputs.** C012a's admissible-field proof gives order 65536
   for 3 and order 1024 for 19139. Thus 3 is outside H, and the 1024
   distinct members of H exhaust the roots of X^1024-1, also when
   regarded in F. The displayed L099 and L102 definitions give exactly
   the two center expressions here, with c nonzero and all other rows
   zero. Their fiber estimates and L100's cap are not used. The pinned
   model has degree at most 63 and simultaneous column equality; its
   unresolved comparison with ABF is not silently resolved by this audit.
2. **Coefficient exhaustion.** Division of P by X^1024-1 has constant
   quotient and remainder of degree less than 1024; all remainder
   evaluations vanish, so the remainder is zero. This includes P=0.
   Coefficients of X and X^2 are respectively binomial(n,1) and
   binomial(n,2) times the two differences in (2). Both factors are
   nonzero because 2<=n<65537. If AB is nonzero, (2) forces all four
   entries nonzero and its quotient gives AD=BC. Otherwise AB=0
   and CD=0. When A=0 the determinant forces B,C nonzero and hence
   D=0; when B=0 it forces A,D nonzero and hence C=0. These exhaust
   every zero-entry case. Evaluation at 1 and subgroup closure prove
   both necessity s in H and both converses, without a missing pole.
3. **Ambient multipliers and inverses.** If the canonical multiplier
   is sigma(x), direct composition gives
   (T S^(-1)y)(x)=mu(x)/sigma(x)*y(x). Hence the diagonal argument
   really tests a code automorphism in the stated action direction.
   Its degree-at-most-63 representative r is nonzero since its values
   lie in F^*. The degree-at-most-126 vanishing polynomial forces
   r X^63=q in F[X], which permits only constant r. This does not
   require r to descend to E. The full-function inverses are R_(s^-1)
   and s^-63 J_s; multiplying either map by lambda multiplies its
   inverse by lambda^-1. Thus code preservation is onto even for
   lower-degree and zero messages. For every column and every row,
   multiplication by the same nonzero scalar is injective. Pullback
   under phi therefore preserves simultaneous agreement counts and
   induces the claimed entire-list bijections for every m>=1.
4. **Scaling identity.** Substituting sx into the numerator and
   clearing X^3(sX-3)^3 gives exactly (3). The four terms in its
   first bracket after multiplication by X^3 have degrees at most
   70,5,4,3; the destination product has degree at most 70.
   Neither denominator vanishes on H. The root bound over F yields
   the identity before evaluating at 3/s. That point is nonzero,
   and only lambda*c*(3/s)^3 remains, a nonzero field element.
5. **Inversion identity.** Since s/X-3=(s-3X)/X, multiplication by
   X^63 gives precisely (4). Multiplication by X^3(s-3X)^3 gives
   the four numerator terms X^2 ell^67, a X^67 ell^2,
   b X^68 ell and c X^69, each of degree at most 69. The destination
   product has degree at most 70. Again the denominators are nonzero
   on H and 1024 distinct roots force an identity over F. Its value
   at s/3 is lambda*c*(s/3)^69, nonzero since s,3,lambda,c are nonzero.
6. **Quantifiers and stop.** Both contradictions are independent of
   a,b and of every destination parameter, including gamma=0. They
   hold separately for every s in H and lambda in F^*, not merely for
   one map chosen uniformly over the family. Zero remaining rows
   preserve the contradiction for all m. Only projective maps over E
   and the specified monomial actions were exhausted. No codeword
   translation, semilinear map, actual fiber bound, arbitrary-center
   safety result or improvement of the 955–957 bracket follows.

The degree bounds and nonzero evaluations, rather than pole locations
alone, validate the finite-domain obstruction. No assertion required
repair or withdrawal; this is verification of the existing local
reproduction, not a new theorem beyond the checked sources' methods.

## Mathlib

Full matching finite-stabilizer, monomial-isometry and center-nontransport
results: **not checked** in Mathlib. Supporting polynomial root bounds,
coefficient comparisons, finite-field subgroup facts and degree identities:
**not checked**. The cited GRS projective framework is a mathematical
source, not a claim of formal library coverage. The pinned ArkLib model
supplies definitions as recorded in foundations/02; no Lean verification
of this specialization has been performed.
