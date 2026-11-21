# Lemma 881: the transverse coefficient on an odd-contact circle imposes a weighted divisor count

## Hypotheses

Assume L879's stationary-graph hypotheses and L880's single odd-contact
hypothesis, with L847's actual entire function and full density:

\[
 G(z)=\tfrac18\xi\left(\tfrac12+\tfrac{\sqrt z}{2}\right),
 \quad R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2>0,
\]
\[
 z_j(y)=R e^{u_j(y)+iy_j},\quad
 u:\mathbb T^2\longrightarrow\mathbb R^2\text{ smooth, real, periodic},
 \quad J=\det(I-iDu)\ne0,
\]
\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad Q=F(z_1,z_2)J.                                      \tag{1}
\]

The orientation remains dy1 wedge dy2. Stationarity means vanishing
first variation of the normalized integral of |Q| for every smooth
real radial variation supported compactly in {Q!=0}. At some point,
exactly one G factor vanishes, the coordinates are distinct, and that
zero label zeta has odd multiplicity m>=1. Let its coordinate be j,
and set a=arg(zeta). No existence of such a stationary graph is asserted.

L879 supplies Q=lambda*s with |lambda|=1 and s real smooth. L880
supplies z_j=zeta on the entire circle y_j=a. Define the other
coordinate on this circle, parametrized by its own increasing angle,
by w(t)=R exp(v(t)+it), and put

\[
 \Gamma=w(\mathbb R/2\pi\mathbb Z),\qquad
 D=\{r e^{it}:0\le r<R e^{v(t)}\}.
\]

Here D includes zero and is the bounded interior of Gamma. Let N_in
be the sum of the actual multiplicities of G zeros in D, and N_bd
the sum on Gamma. Define nu(zeta) to be 1, 1/2, or 0 according as
zeta lies in D, on Gamma, or outside its closure. All simultaneous G
contacts, all multiplicities and the squared diagonal are retained.
No symmetry, positivity, analytic-u, simplicity, prescribed collar,
zero-free complementary curve, RH or additional graph assumption is used.

## Conclusion

The common leading normal coefficient on the contact circle is the
smooth periodic function

\[
 k(t)=\frac1{m!}\partial_{y_j}^m Q\big|_{y_j=a}
   =C g_\zeta(0)\zeta^{m-2}\alpha(t)^{m+1}
         \frac{G(w(t))(\zeta-w(t))^2}{w(t)^3}w'(t),       \tag{2}
\]

where g_zeta(0)=G^(m)(zeta)/m!,
alpha(t)=partial_j u_j|_(y_j=a)+i, and the free angle is t.
All lower normal derivatives vanish along the circle. The coefficient
k is not identically zero, and conjugate(lambda)*k is real. Its zeros
are exactly the points w(t)=eta with G(eta)=0; their finite orders in
t are

\[
                 \operatorname{ord}_{t}k
                     =\operatorname{ord}_{\eta}G
                              +2\mathbf1_{\eta=\zeta}.  \tag{3}
\]

At these exceptional parameters k is zero; (2) is the first normal
coefficient that is not identically zero on the circle, not an assertion
of a nonzero pointwise leading coefficient at every vertex. The
pointwise normal order there is not needed or asserted.

With the boundary-zero convention justified below, the exact count is

\[
                 N_{\rm in}+\tfrac12N_{\rm bd}
                                  +2\nu(\zeta)=2.       \tag{4}
\]

In particular:

1. zeta cannot lie in D.
2. If zeta lies on Gamma, then m=1, N_in=0 and N_bd=2. There are exactly
   two distinct simple G-zero contacts on the boundary, one at zeta.
3. If zeta lies outside the closed domain, then
   2 N_in+N_bd=4; the possible count pairs are (2,0), (1,2), (0,4).

Thus the opposite coordinate satisfies |w(a)|<=|zeta|, with the
stated stringent equality case. This is a new necessary constraint
within the notebook's assessed attempt, not exclusion or construction
of the remaining stationary graphs. An abstract nonnegative integer
count satisfying (4) is not a graph realization. The prior sources
supply the residue and division tools; their checked comparison did
not supply (2)–(4) and does not certify originality. The independent
conceptual audit of 6 November 2026 below accepts (2)–(4) and the
listed case exclusions under exactly the stated hypotheses.

## Proof

### Scope and imported standard tools

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-odd-fiber-transverse-phase-index.md`.
It covers exactly this full-coefficient and actual-divisor test.
L847 supplies (1), L879 the phase line, and L880 the complete labeled
circle, including its simultaneous and diagonal vertices. Neither
the product obstruction nor the retired ambient two-period calculation
is an input. Their stops and the session43 automatic-ray stop retain
their scopes.

Import finite-order holomorphic factorization from Jiří Lebl,
*Guide to Cultivating Complex Analysis*, v1.10, 5 November 2026,
[Theorem 2.4.7 and proof, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49).
G is entire and G(0)>0, so it is nonzero as a function, all its zeros
are isolated and finite in compact sets, and the stated local
factorizations apply. Smooth coordinate division below is Taylor's
theorem with integral remainder, also covered by the parameter-smooth
Hadamard-lemma comparison in the saved assessment. No analyticity of
u or arbitrary finite-order assertion for smooth functions is imported.

For the boundary zeros use Norbert Hungerbühler and Micha Wasem,
*Non-Integer Valued Winding Numbers and a Generalized Residue Theorem*,
Journal of Mathematics 2019, Article 6130464,
[Definition 2, p2; Proposition 3 and proof, p3; Theorem 8 and its
simple-pole proof, p7](https://www.math.ch/norbert.hungerbuehler/publications/Non-Integer_Valued_Winding_Numbers_and_a_Generalized_Residue_Theorem.pdf),
DOI 10.1155/2019/6130464. The integral uses removal of spatial discs
of a common shrinking radius at boundary singularities. For a smooth
positively oriented Jordan curve the interior angle is pi, so the
generalized winding is 1/2 at a boundary point; it is 1 inside and
0 outside. Theorem 8 applies to a meromorphic integrand with only
simple boundary poles on an immersed piecewise-C1 cycle null-homologous
in its open ambient domain. Its extra hypotheses for higher-order
boundary poles are unnecessary here: the integrand will be a
logarithmic derivative, not the density or its reciprocal. These
standard results are imported, not reproved. Their specialization to
the actual coefficient, its cutoff and all residues is checked below.

### Smooth global normal coefficient and the full Jacobian

First take j=1. Use x=y1-a and t=y2, keeping Q as the scalar density
in the original orientation. L880 gives u1(a,t)=log(|zeta|/R).
Consequently partial_2 u1(a,t)=0. Put

\[
 A(t)=\partial_1u_1(a,t),\quad v(t)=u_2(a,t),\quad
 \alpha=A+i,\quad\beta=v'+i,\quad w'=w\beta.
\]

Along the circle, Du has entries [[A,0],[partial_1 u2,v']]. Hence
the full determinant, including every entry before this restriction, is

\[
 J(a,t)=(1-iA)(1-iv')=-\alpha\beta.                      \tag{5}
\]

The lower left entry disappears because the upper right entry is
exactly zero on this circle, not because a product graph is assumed.
Both alpha and beta have imaginary part 1 and never vanish.

Taylor division gives a smooth function Z, periodic in t, such that

\[
 z_1(a+x,t)-\zeta=xZ(x,t),\qquad Z(0,t)=\zeta\alpha(t).  \tag{6}
\]

For example Z(x,t)=integral_0^1 partial_1 z1(a+sx,t) ds.
Compactness permits one sufficiently small x-neighborhood for all t,
with z1 in the factorization disc of zeta. In that neighborhood
G(z1)=(z1-zeta)^m g_zeta(z1-zeta), with g_zeta(0)!=0. Thus the exact
factorization, not just a pointwise expansion, is

\[
 Q(a+x,t)=x^m\mathcal K(x,t),\quad
 \mathcal K=-C Z^m g_\zeta(z_1-\zeta)
                \frac{G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}J.  \tag{7}
\]

All quantities are smooth and periodic in t. Inserting (5) and (6)
at x=0 gives

\[
 \mathcal K(0,t)=C g_\zeta(0)\zeta^{m-2}
        \alpha^{m+1}\beta\frac{G(w)(\zeta-w)^2}{w^2},
\]

which is (2). Formula (7) proves the lower-derivative claims, including
at every simultaneous or diagonal zero. Since conjugate(lambda)Q
is real, division by the real number x^m for x!=0 and then continuity
at x=0 show that conjugate(lambda)k is real everywhere. No density
zero is divided out on the circle to obtain this fact.

The curve w is injective modulo 2pi, since equality of its nonzero
values gives equality of their angles. Its derivative w beta is
nonzero. It is therefore a smooth embedded closed radial curve,
positively oriented around zero, with interior D as specified. Only
finitely many zeros of G meet its compact image. Each is attained
at exactly one parameter modulo 2pi. At w(t0)=eta,

\[
 w(t)-\eta=(t-t_0)\left(w'(t_0)+O(t-t_0)\right),
                   \qquad w'(t_0)\ne0.
\]

Holomorphic factorization and the nonzero smooth factors in (2) now
give exactly (3), also when eta=zeta, where the diagonal adds two.
There are no other zeros, since zeta itself is a G zero and all the
other factors in (2) are nonzero. Away from this finite set k is
nonzero, proving the asserted generic leading order. This establishes
finite tangential orders from actual factors, not from smoothness alone.

### Boundary cutoff, tangent phase and divisor count

Set the nonzero constant kappa=C g_zeta(0) zeta^(m-2) and define

\[
 h(z)=\frac{G(z)(\zeta-z)^2}{z^3},\qquad
 k(t)=\kappa\alpha(t)^{m+1}w'(t)h(w(t)).                 \tag{8}
\]

On every open arc where k!=0 its logarithmic derivative satisfies

\[
 0=\operatorname{Im}\frac{k'}{k}
   =(m+1)\operatorname{Im}\frac{\alpha'}\alpha
       +\operatorname{Im}\frac{w''}{w'}
       +\operatorname{Im}\left(\frac{h'}h(w)w'\right).   \tag{9}
\]

The first equality follows because conjugate(lambda)k is real and
nonzero there; its sign may differ on other arcs. No ordinary winding
number for the curve k through its zeros is being defined.

Alpha has a smooth periodic argument in (0,pi). Likewise beta=v'+i
has a smooth periodic argument in (0,pi). Therefore

\[
 \int_0^{2\pi}\operatorname{Im}\frac{\alpha'}\alpha\,dt=0,
 \qquad
 \int_0^{2\pi}\operatorname{Im}\frac{w''}{w'}\,dt=2\pi. \tag{10}
\]

For the second identity use w'=w beta and w'/w=v'+i: the imaginary
part from w is identically 1 and the beta argument returns to its
initial value. Thus (10) includes the tangent contribution explicitly;
the entire nonvanishing part of the Jacobian has not been assigned
an unproved zero index.

Let E be the finite set of G zeros on Gamma. For epsilon>0 small,
retain precisely those t for which |w(t)-eta|>epsilon for every
eta in E. This is the spatial-disc cutoff in the cited definition,
with one disc for each distinct boundary point, even at zeta. The
discarded parameter sets shrink to the finite contact parameters;
their total length tends to zero. The first two integrands in (9)
are smooth and bounded on the whole circle, so their truncated
integrals tend to (10). If E is empty no deletion is necessary.

The meromorphic integrand for the final term is

\[
             \frac{h'(z)}{h(z)}
                =\frac{G'(z)}{G(z)}+\frac2{z-\zeta}-\frac3z.
                                                               \tag{11}
\]

It is holomorphic on C minus the discrete set consisting of zero
and the G zeros. Every pole is simple: its residue is the G order
at a zero eta!=zeta, m+2 at zeta, and -3 at zero, since G(0)>0
and zeta!=0. The cycle Gamma is immersed and null-homologous in C.
Thus all hypotheses of the simple-boundary-pole case of Theorem 8
hold, irrespective of the orders of the zeros of h itself.

The positive radial curve has generalized winding 1 at interior
points, 1/2 at its smooth boundary points and 0 outside. In particular
zero contributes -3, and zeta contributes its G multiplicity through
N_in or N_bd plus the separate diagonal residue 2. The theorem gives

\[
 \operatorname{PV}\int_\Gamma\frac{h'}h\,dz
     =2\pi i\left(N_{\rm in}+\tfrac12N_{\rm bd}
                                      +2\nu(\zeta)-3\right).  \tag{12}
\]

Only finitely many singularities have nonzero generalized winding,
since the closure of D is compact. The common cutoff in (9) is exactly
the cutoff in (12). Integrating (9) over its retained arcs and passing
to this limit, using (10) and the imaginary part of (12), yields

\[
       0=0+2\pi+2\pi\left(N_{\rm in}+\tfrac12N_{\rm bd}
                                      +2\nu(\zeta)-3\right).
\]

This is (4). Neither boundary contributions nor the tangent, denominator
or full-J factors have been omitted. The coefficient k need not be
meromorphic; only the explicit one-variable function (11) is subjected
to the residue theorem.

### Consequences and scope

If zeta is interior, its order m>=1 is included in N_in, while
2 nu(zeta)=2. The left side of (4) then exceeds 2, a contradiction.
If it is on the boundary, (4) says 2 N_in+N_bd=2 and N_bd>=m>=1.
Hence N_in=0 and N_bd=2. Odd m forces m=1, leaving precisely one
other simple boundary zero. Outside the closure, (4) is exactly
2 N_in+N_bd=4, with the three nonnegative-integer pairs listed above.
Radiality translates the exclusion of the interior to |w(a)|<=|zeta|.

For j=2, take t=y1 and normal derivative partial_y2. The corresponding
matrix is [[v',partial_2 u1],[0,A]], and its determinant J is again
-alpha beta. F is symmetric and its diagonal factor is squared, so
the scalar calculation (6)–(12) is unchanged. Q is always the coefficient
in the original dy1 wedge dy2 orientation; exchanging names in the
scalar formula does not reorient the form. The free angle still gives
the positively oriented radial curve w.

This finishes the one bounded coefficient/index attempt. The interior
alternative is excluded and the remaining cases have a sharp necessary
count. No theorem here shows that the actual G divisor cannot meet
those cases, that compatible counts suffice, or that any stationary
graph exists. In particular the full odd-contact branch, L868's sharp
threshold, compactness, higher signs and actual-Xi positivity remain
open. No numerical census or mathematical script is used. General
boundary-residue theory is known; the graph-specific coefficient and
necessary count are the local progress. The independent audit below
validates this necessary condition without strengthening it.

### Independent conceptual audit, 6 November 2026

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-06-l881-transverse-divisor-count-audit.md`
authorizes this audit of the existing statement. The complete proof
has been checked against L847's full scalar density, L879's accepted
phase line and L880's accepted full same-label circle. The primary
source coverage above is reused; no new source theorem, zero census
or additional graph hypothesis is needed. The following checks accept
the result without a mathematical correction or an extension of scope.

**Full determinant and uniform normal division.** In the original
coordinate order, for j=1 the matrix Du on the circle is
[[A,0],[c,v']], so det(I-iDu)=(1-iA)(1-iv')=-alpha beta.
The initially unrestricted entry c does not contribute to this
restriction because partial_2 u1=0 follows from the entire labeled
circle. Before restriction, (7) still uses the full determinant.
The minus sign in F cancels the minus sign in J. The leading normal
factor (zeta alpha)^m, denominator zeta^2 w^2, and remaining factor
alpha beta give exactly C g_zeta(0) zeta^(m-2) alpha^(m+1) beta/w^2
times G(w)(zeta-w)^2. Since beta=w'/w this is (2), with no missing
coordinate factor or factorial. Taylor's integral formula for Z is
smooth jointly in x,t, periodic in t and valid on one common strip
by compactness. Thus Q=x^m K there and partial_x^m Q at x=0 is
m!K(0,t), also at the exceptional parameters. For j=2, the matrix
is [[v',c],[0,A]] and the same determinant and symmetric scalar F
give the same answer. Taking a scalar normal derivative does not
exchange dy1 wedge dy2 or reverse the free angular curve.

**Complete exceptional set and reality.** The curve w has w'=w(v'+i)
nonzero and is injective modulo 2pi by its angle. The factors alpha,
w', w^(-3), kappa are everywhere nonzero. At w(t0)=eta, smooth
division writes w(t)-eta=(t-t0)b(t), b(t0)=w'(t0)!=0.
The cited holomorphic factorization of G then writes k as
(t-t0)^n times a nonzero smooth complex factor, with n=ord_eta G,
or n=m+2 if eta=zeta. This proves the exact finite tangential order
in (3), not merely an upper bound; the extra two are from the
diagonal. There are finitely many such points because the compact
curve meets a discrete holomorphic zero set. Hence k is nonzero
on some open arcs. Since conjugate(lambda)Q is real and x^m is real
for x!=0, continuity gives real conjugate(lambda)K(0,t) at every t.
The sign of that real function may change. No winding of k through
zero is used, and no pointwise normal order at a vertex is inferred.

**Contour and cutoff.** Positivity and periodicity of R exp(v(t))
make Gamma a smooth radial Jordan curve with strictly positive
minimum radius. Thus zero is interior, the positive angular
parameter gives the positive orientation, and every boundary point
has interior angle pi. Distinct points of the finite exceptional
set have disjoint small spatial discs. Near any one of them,
|w(t)-w(t0)|/|t-t0| tends to |w'(t0)|>0. The discarded parameter
lengths are therefore O(epsilon) and tend to zero, including at the
chosen angular seam when read in a local circle chart. The same
spatial discs are removed from all three terms of (9). The smooth
alpha and tangent terms converge to their full integrals, while
the last term has precisely the spatial principal value specified
by Hungerbuehler–Wasem Definition 2 and Theorem 8. There is no
conversion to an asymmetric parameter cutoff or independently
chosen cutoff for overlapping G and diagonal contributions.

**Nonvanishing phases and residues.** Both alpha=A+i and beta=v'+i
lie in the open upper half-plane and have single-valued smooth
periodic arguments there. Their logarithmic-derivative imaginary
parts have zero full integral. From w'=w beta and w'/w=v'+i,
the tangent contribution is instead 2pi, as in (10). For the
meromorphic function h in (8), the integrand h'/h is (11) on its
regular set and extends meromorphically with only simple poles.
At zero its residue is -3 because G(0)>0 and zeta!=0; at zeta it
is m+2; at any other G zero eta it is ord_eta G. Arbitrarily high
zero multiplicities do not give higher-order poles of h'/h.
The ambient domain can be C with discrete singular set
{0} union {G=0}; Gamma is null-homologous in C. Thus the cited
simple-boundary-pole theorem applies. Only finitely many poles have
nonzero generalized winding. The smooth boundary weight is 1/2;
the interior weight is 1. Counting the G multiplicity at zeta once
through N_in or N_bd and its diagonal multiplicity separately gives
exactly (12). The common-cutoff integral of (9) consequently gives
0=2pi+2pi(N_in+N_bd/2+2nu(zeta)-3), so the right side of (4)
is 2. The pole at zero, tangent turn, and diagonal each matter.

**All case exclusions.** If zeta is interior, N_in>=m>=1 while
2nu(zeta)=2, contradicting (4). If it is on Gamma, then
2N_in+N_bd=2 and N_bd>=m>=1. Integrality forces N_in=0 and
N_bd=2; oddness of m forces m=1, and the remaining unit of
multiplicity belongs to one distinct simple zero. If zeta is
outside the closure, 2N_in+N_bd=4 has exactly the three stated
nonnegative integer solutions. Finally, the radial curve intersects
the ray of zeta only at w(a), so noninteriority is exactly
|w(a)|<=|zeta|. No simplicity of other zeros was imposed to reach
these deductions; simplicity in the boundary case is a conclusion.

The audit therefore accepts the coefficient, the exact count and
the stated exclusions. The inputs remain L847, L879 and L880;
there is no new mathematical dependency or change to the argument.
This is validation of an existing notebook result, not a new theorem
beyond the sources checked or a global odd-branch exclusion.
Compatible divisor data do not produce a stationary graph. The
exterior and boundary possibilities, graph existence, sharp period,
compactness, higher signs and actual-Xi transfer remain unresolved.
No mathematical script or numerical evidence is part of this audit.

## Mathlib

Full matching coverage and formal coverage of the boundary-zero
principal value, smooth factorization and graph specialization were
not checked. No Mathlib theorem is imported. Unknown coverage is not
evidence of absence. This necessary condition now has an independent
informal conceptual audit; that does not establish Mathlib coverage,
formal verification or a complete RH candidate.
