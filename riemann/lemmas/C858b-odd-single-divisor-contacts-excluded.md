# Corollary 858b: odd single-G contacts are excluded on a nonnegative collar extension

## Hypotheses

Retain all hypotheses and qualifications of L858. In particular use
L847's actual nonzero entire function G, positive constants R,C, and
the full form on X=(C*)^2:

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
                                                               \tag{1}
\]

Let u:T^2 -> R^2 be real C2, periodic in both angular coordinates,
with u_2(t,s)=u_1(s,t), and put

\[
 z_j(\theta)=R e^{u_j(\theta)+i\theta_j},\quad A=Du,
 \quad J=\det(I-iA)=1-\det A-i\operatorname{tr}A,
 \quad f=F(z_1,z_2),\quad q=fJ.                              \tag{2}
\]

The orientation is dtheta_1 wedge dtheta_2. Assume q is real and
nonnegative everywhere. Assume u agrees with L849's exact analytic
graph on a smaller open diagonal collar |delta|<delta_c, where
t=m+delta, s=m-delta and 0<delta_c<epsilon_849. Retain the prescribed
h,b, strict off-diagonal collar positivity, and all inherited L848
analytic/trusted-software qualifications. The collar width is strictly
smaller than the width of L849's estimates, as required by L858.

No simple-zero assumption, rank-two transversality, isolation of the
pulled-back zero set, analyticity outside the collar, existence of a
global torus satisfying these assumptions, or RH is assumed.

## Conclusion

There is no point p with z_1(p)!=z_2(p) at which exactly one of
G(z_1(p)), G(z_2(p)) vanishes to finite odd multiplicity and the other
is nonzero. Equivalently, every single-G contact off the diagonal of
X, if present under these hypotheses, has even holomorphic
multiplicity. This conclusion applies to either coordinate, including
nontransverse contacts and nonisolated pulled-back zero sets.

This is a conditional local restriction on a possible global
nonnegative extension of the prescribed collar. Even-multiplicity and
simultaneous G contacts, forced contact, global gluing and signs, and
actual-Xi all-degree mixed positivity remain unresolved. The result
does not exclude all such tori, prove a new Xi sign, or resolve RH.
It is an elementary source specialization recorded as REPRODUCTION,
not a claim of novelty beyond the sources checked. It has not received
a separate critical audit.

## Proof

### Imported inputs and their scope

The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-06-odd-divisor-contact-scope.md`.
Import the following previously inspected standard tools:

- Jiří Lebl, *Guide to Cultivating Complex Analysis*, version 1.10,
  5 November 2026, [Theorem 2.4.7 and its factorization proof and
  remark, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49).
  At a zero of a nonzero holomorphic function on a connected open
  domain, factor out its finite order and retain a holomorphic unit.
  Here G is entire and G(0)>0 by L847, so the nonzero-function
  hypothesis holds. No statement about the existence, simplicity or
  location of an actual zero is imported.
- Lebl, *Basic Analysis I*, version 6.3, 15 May 2026,
  [Definition 4.1.1, p155](https://www.jirka.org/ra/realanal.pdf#page=155):
  the first-order difference quotient for a differentiable real
  function. Apply it componentwise to the complex-valued coordinate
  curve below. The resulting first-order limit, elementary finite
  products of limits and continuity suffice.

We do not import a Cn extremum theorem with its regularity hypotheses
dropped: u is only C2 and J is only C1. The holomorphic factorization
is imported, not reproved. The full coefficient and angular-velocity
checks below are the needed specialization; the source statements
alone do not identify these quantities or give their nonvanishing.
L847 supplies (1)–(2), and accepted L858 supplies {f=J=0}=empty with
exactly the global and collar hypotheses retained above.

### The full coefficient along the appropriate angular curve

Suppose p is a forbidden point. Let j be its vanishing coordinate
and k the other coordinate. Write

\[
 \zeta=z_j(p),\quad \eta=z_k(p),\quad
 G(\zeta+w)=w^n g(w),\quad g(0)\ne0,
                                                               \tag{3}
\]

where n>=1 is odd, g is holomorphic near zero, zeta eta!=0,
zeta!=eta, and G(eta)!=0. Since f(p)=0, L858 gives J(p)!=0.
This use of L858, not an added total-reality assumption, is what
excludes the common-zero positive germ of L855 from the argument.

Choose a real angular lift of p and, for sufficiently small positive
and negative real t, set theta(t)=p+t e_j, where e_j is the jth
coordinate vector. This is a curve in a chart of the torus; p is
an interior point of its parameter interval. Its vanishing coordinate
has derivative

\[
 v_j=\left.\frac{d}{dt}z_j(p+t e_j)\right|_{t=0}
     =\zeta\bigl(\partial_j u_j(p)+i\bigr)\ne0.             \tag{4}
\]

Indeed partial_j u_j(p) is real and zeta!=0. Thus, writing
w(t)=z_j(theta(t))-zeta, the two-sided first-order limit is
w(t)/t -> v_j. It does not require that the two-variable map z_j
have real rank two.

After shrinking the interval so that (3) applies, define the full
remaining coefficient

\[
 B_j(t)=-C\,
 \frac{g(w(t))G(z_k(\theta(t)))
       (z_1(\theta(t))-z_2(\theta(t)))^2}
      {z_1(\theta(t))^2z_2(\theta(t))^2}
       J(\theta(t)).                                      \tag{5}
\]

It is continuous, and every factor in B_j(0) is nonzero. Equation
(1) gives the exact identity q(theta(t))=w(t)^n B_j(t), including
t=0. For j=2 this is the same formula: G's factors commute, the
squared difference stays in its original order, and the parameter
orientation defining q is unchanged. No swap of the two differential
forms or new orientation sign is made. Consequently, for both choices,

\[
 \lim_{t\to0,\ t\ne0}\frac{q(p+t e_j)}{t^n}
          =v_j^n B_j(0)=:a\ne0.                            \tag{6}
\]

We have not divided by G at its zero. The only division in (6) is
by the nonzero real parameter t. Equation (6) uses continuity of the
coefficient and the first-order curve limit, without differentiating
q n times or imposing any upper bound on the finite multiplicity n.

### The two-sided sign contradiction

Every quotient in (6) is real, because q is real and t is real.
Hence its finite limit a is real. For t>0 the quotient is
nonnegative. For t<0 it is nonpositive, since n is odd and q>=0.
The common two-sided limit must therefore satisfy a>=0 and a<=0,
so a=0. This contradicts the explicit nonvanishing in (6).

Thus the proposed contact cannot occur. The argument is pointwise:
no uniform multiplicity bound, isolation of other contacts or census
of zeros is needed. It leaves even and simultaneous contacts
unaddressed; there is no claim that any contact must occur.

## Mathlib

Full matching Mathlib coverage was not checked. The cited holomorphic
factorization and first-order differentiation facts are supporting
standard inputs; they are not a matching theorem about this actual-G
form and its globally qualified collar extension. Unknown coverage
is not evidence of absence. No Lean verification is claimed.
