# L004 — Cumulative degree of nonsingular jet graph closures

## Hypotheses

Let K be algebraically closed of characteristic zero or characteristic p>d.
Fix integers 0<=s<=d, D>=0, B>=1, an anchor alpha in K, and

\[
 Q\in K[Z,X,Y_0,\ldots,Y_s],\qquad
 \deg_ZQ,\deg_XQ\le D,\quad \deg_Y^{\mathrm{tot}}Q\le B.
\]

For initial variables u=(Z,c_0,...,c_s), suppose

\[
 F_0(u)=Q(Z,\alpha,c_0,\ldots,c_s),\qquad
 H(u)=\partial F_0/\partial c_s
\]

has H nonzero as a polynomial. Use the Taylor coefficients, lifted
numerators N_t, and cleared residuals R_t constructed in L003. Put

\[
 A=D+B,\quad a=d-s,\quad L=\max(0,2a-1),\quad
 E=A(1+BL),\quad T=AL+1. \tag{1}
\]

Define the closed set and its principal-open part

\[
 W=V\bigl(F_0,\ R_t\ (a<t\le D+Bd)\bigr)\subseteq K^{s+2},
 \qquad U=W\cap\{H\ne0\}. \tag{2}
\]

The unmultiplied F_0 is included, even when a=0. An empty residual index
range imposes no equations. On U define

\[
 \Phi(u)=\left(u,\frac{N_1(u)}{H(u)},\ldots,
                    \frac{N_a(u)}{H(u)^{2a-1}}\right),
 \qquad \Gamma=\overline{\Phi(U)}\subseteq K^{d+2}. \tag{3}
\]

When a=0, Phi is the identity. All closures and algebraic sets are reduced;
degree and cumulative degree use the
[projective-closure convention](../foundations/03-proper-hyperplane-sections.md).
The cumulative degree of the empty set is zero.

For each z in K, define U_z by imposing Z=z in (2) and retaining H(z,-)!=0.
Let Gamma_z in K^(d+1) be the closure of its specialized lifted graph after
dropping the fixed Z coordinate. This definition does not take a fiber of
Gamma.

## Conclusion

The total chart satisfies

\[
 \dim\Gamma\le s+1,\qquad
 \operatorname{cdeg}(\Gamma)\le A(ET)^{s+1}. \tag{4}
\]

Every fixed-parameter chart satisfies

\[
 \dim\Gamma_z\le s,\qquad
 \operatorname{cdeg}(\Gamma_z)\le B(ET)^s, \tag{5}
\]

with the dimension assertion understood as vacuous for an empty set.
For fixed s and B these are polynomial bounds in D and d, independent of
the number of residual equations and without an exponent growing with d.

The graph Phi(U) is exactly the part with H!=0 of the coefficient solution
set Q(Z,X,P,P^[1],...,P^[s])=0 identically in X, where
P(alpha+X)=sum_j c_j X^j. Its closure Gamma is contained in that solution
set; the analogous statement holds at fixed z. Invertible linear conversion
from Taylor to monomial coefficients preserves these degree bounds.

This verifies the local chart-closure passage, with explicit constants
using L003, in
[TR26-169, Lemmas 5.3–5.4 and the nonsingular construction on printed pp. 20–21, 25](https://eccc.weizmann.ac.il/report/2026/169/download#page=20),
September 5, 2026 version, read September 25. No novelty or full cover
theorem is claimed. Singular solutions outside these closures, a bounded
collection of anchors, and the list-decoding interpolation input are not
established here.

## Proof

**Cumulative degree under several equations.** We first justify the
intersection estimate needed twice below. Suppose a reduced affine set V
has dimension at most r and cumulative degree Delta, and a finite family
of equations has degree at most e>=1. Its common zero set inside V has
cumulative degree at most Delta e^r.

Start with the irreducible components of V, counted as separate occurrences.
At an occurrence X on which all equations vanish identically, stop. Otherwise
choose an equation f not identically zero on X. If X is a point, it is
removed. If X has positive dimension, replace it by the irreducible
components of X intersect V(f); an empty intersection has no children.
By the standard proper-hypersurface form of projective Bezout in the cited
foundation, each child has dimension dim(X)-1 and the sum of their degrees
is at most e deg(X).

Give an occurrence X the weight deg(X)e^dim(X). The total weight of its
children is at most its own weight. Every nonempty descent drops dimension,
so the tree is finite, regardless of how many equations were given. Its
terminal sets lie in the common zero set and together cover it: at a cut,
every common zero on a parent lies on a child. Thus their union is exactly
the common zero set. Its irreducible components are among the terminal
occurrences, since an irreducible set contained in a finite union of closed
sets is contained in one of them. Their degree sum is at most the sum of
terminal weights, which is at most Delta e^r. Repeated or contained terminal
sets can only enlarge this upper bound. The argument also bounds the number
of isolated points of an intersection that has other, positive-dimensional
components.

**The base and its open part.** Since H=partial F_0/partial c_s is nonzero,
F_0 is nonconstant and has degree at most A. Factoring F_0 into distinct
irreducible factors shows that V(F_0) has dimension s+1 and cumulative
degree at most A: the degrees of the distinct factors sum to at most deg F_0.
L003 gives degree(R_t)<=E. Applying the preceding intersection estimate
inside V(F_0) proves

\[
 \dim W\le s+1,\qquad \operatorname{cdeg}(W)\le A E^{s+1}. \tag{6}
\]

If W has irreducible components X_i, then

\[
 \overline U=\bigcup_{X_i\not\subseteq V(H)}X_i. \tag{7}
\]

Indeed, U is the union of their intersections with {H!=0}; on an
irreducible component this open set is either empty or dense. Closure
commutes with a finite union. In particular, (7) concerns the closure of U,
not U itself, and need not retain every component of W. It gives
cdeg(overline U)<=A E^(s+1) and dimension at most s+1.

**A graph bound using only the base dimension.** By L003, set

\[
 G=H^L,\qquad M_t=N_t H^{L-(2t-1)}\quad(1\le t\le a).
\]

Then deg G<=AL and deg M_t<=AL. For a=0 set G=1 and omit all M_t.
For each component X retained in (7), of dimension b, put
O=X intersect {H!=0} and let Gamma_X be the affine closure of its graph.
Projection to the initial coordinates identifies the graph with O, so it
is irreducible of dimension b. It is closed inside the ambient open set
{H!=0}, because the coordinate functions M_t/G are regular there and X
is closed. Consequently the graph is exactly Gamma_X intersect {H!=0}.
Its complement in the projective closure of Gamma_X is a proper closed
set of dimension less than b.

Choose a general codimension-b projective linear subspace meeting that
projective closure. The generic linear-section characterization of degree
from the foundation makes its intersection consist of deg(Gamma_X)
distinct points, all in the open graph. When b=0 this simply selects the
single point. The affine linear equations defining the section pull back,
after multiplication by G, to equations of the form

\[
 \lambda_0G+\sum_{i=1}^{s+2}\lambda_i u_iG
                   +\sum_{t=1}^a\mu_t M_t=0, \tag{8}
\]

each of degree at most T=AL+1. Every selected graph point has a unique
preimage in O. These preimages are isolated points of the common zero set
of (8) in X. Otherwise a positive-dimensional component through a preimage
would meet {H!=0} in a positive-dimensional open set, giving infinitely many
points in the chosen finite graph section. Over H!=0, multiplying by G
neither adds nor removes a zero.

Apply the intersection estimate to X with e=T and r=b. It bounds all these
isolated points, even if there are additional components on H=0, and proves

\[
 \deg(\Gamma_X)\le\deg(X)T^b. \tag{9}
\]

This avoids any assumption that homogenized equations cut the base locus
properly. Possible denominator components remain irrelevant to the finite
section chosen in the open graph. The number of lifted coordinates enters
the sum in (8), but not its degree or the exponent b.

The closure Gamma is the finite union of the Gamma_X. Summing (9) over
retained base components and using b<=s+1, T>=1, and (6) gives (4).
Projection also proves the asserted dimension bound. Overlapping graph
closures do not increase the cumulative degree of their union beyond this
sum.

**Specializing the open chart first.** If H(z,-) is identically zero, then
U_z is empty and (5) holds. Otherwise F_0(z,-) has nonzero c_s partial and
is a nonconstant polynomial of degree at most B in the s+1 initial Taylor
variables. Its hypersurface has dimension s and cumulative degree at most
B. Specializing L003's numerators and residuals does not increase their
degrees; all its identities remain valid on H(z,-)!=0. Repeat (6)–(9) with
this base and without the Z coordinate. The base closure has cumulative
degree at most B E^s, and the graph factor is at most T^s. This proves (5)
without assuming that closure commutes with specialization. An empty chart
with nonzero H(z,-) also satisfies the bounds.

**Solution identities and coordinates.** L003 says that on H!=0 the
recursively lifted coefficients solve the full differential equation
exactly when F_0 and all indicated residuals vanish. Conversely any full
solution with H!=0 has these uniquely determined coefficients. This proves
the equality of the open graph with the nonsingular solution locus for
this anchor. The full solution locus is closed, being cut out by finitely
many coefficients of a polynomial in X. It therefore contains the closure
Gamma, including any of its boundary points. The same reasoning works at
fixed z. Translation of a degree-at-most-d polynomial from Taylor to
monomial coefficients is invertible and linear. It extends to a projective
linear automorphism, which preserves dimension and degree.

**Boundary checks.** Clearing a denominator and taking the entire resulting
zero set is not the construction above. For example, take W=V(xy) in K^2,
H=x, and the rational coordinate v=y/x. On U, y=v=0 and x!=0, so the graph
closure is V(y,v). The naive equations xy=0 and xv-y=0 instead define the
union V(y,v) union V(x,y); the latter line has unrestricted v and lies
entirely on H=0. This follows immediately by splitting into x=0 and x!=0.
It explicitly tests the component removal in (7) and the open condition in
the graph argument.

Closure also need not commute with specializing Z. Over characteristic
zero, let Q=Y_0(Y_0+Z), s=0, d=1, and alpha=0. Its polynomial solutions
are P=0 and P=-Z, since K[X] is an integral domain. For z!=0 both have
H=z+2c_0 nonzero. Their total graph closure is

\[
 \Gamma=V(c_1,\ c_0(c_0+Z)).
\]

At z=0 the only polynomial solution is zero and H=0, so Gamma_0 is empty,
while the z=0 fiber of Gamma contains the zero polynomial. At every z!=0,
cdeg(Gamma_z)=2=B, attaining (5) for s=0. Q is Z-primitive, so primitivity
alone does not eliminate this distinction. These are exact algebraic
checks, not finite-field samples or a disproof of a cover theorem.

The no-lift case L=0 has T=1 and uses the identity graph. Constant nonzero
H, zero residuals, mixed component dimensions, and empty intersections are
already covered by the proof. Characteristic zero or p>d is used through
L003; this geometric argument removes no characteristic restriction. It
also proves no bound on the number of anchors or on singular branches.

## Mathlib

Full explicit bounds (4)–(5): **not checked** in Mathlib. Supporting
projective Bezout, the generic linear-section characterization of degree,
localization, and graph-closure results: **not checked**. The foundation
retains its named standard inputs and supporting Stacks reference. The
directly linked TR26-169 lemmas support the general intersection/graph
passage; they are neither a Mathlib coverage claim nor a citation for these
particular constants derived from L003.
