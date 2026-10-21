# L097 — Conditional charge-fourteen family has projective semistable placement

## Hypotheses

Retain L071's identical marked smooth projective complex K3 surfaces
S_1 and S_2, their common hyperkähler metric and real ample divisor
class h, Omega=p_1^*h+p_2^*h, and the full integral tensor tau_D.
The exact zero-slope divisor lattice is Z k, with k^2=-14 and
h.k=0. Write L for the line bundle on S_1 with c_1(L)=k.

Suppose F is a locally free holomorphic rank-two bundle on
X=S_1 x S_2, slope-polystable at Omega, with integral c_1(F)=0 and

\[
             ch_2(F)=-14e_1-21e_2-tau_D,
             \qquad e_1=\eta\otimes1,\quad e_2=1\otimes\eta,
             \quad \int_{S_i}\eta=1.
\]

For y in S_2 let E_y=F|_{S_1 x {y}}. Use L071's actual restricted
connections: every E_y is locally free and h-slope-polystable,
with rank two, integral c_1=0 and c_2=14 eta. By separately audited
L096, the set Z of nonstable closed fibres is finite, possibly
empty; each such fibre is L direct sum L^{-1}. All other closed
fibres are h-slope-stable. Existence of F or a point of Z has not
been established.

## Conclusion

There is one very ample integral line bundle H on S_1, with H.k=0,
for which all E_y are slope-polystable and Gieseker-semistable.
They are Gieseker-stable precisely off Z; at Z they are strictly
Gieseker-polystable. The actual GAGA algebraization of F gives a
global algebraic morphism

\[
 f_F:S_2\longrightarrow M_H^{ss}(2,0,-12),\qquad
                  y\longmapsto [E_y]_{S\text{-equivalence}}.
\]

Here the target is the projective fixed-numerical-class part of the
Gieseker moduli scheme with Hilbert polynomial H^2 n^2-10 and
Mukai vector (2,0,-12). The preimage of its stable open is
S_2 minus the reduced finite closed subset with complex points Z.
Every point of Z maps to the same polystable point [L direct sum
L^{-1}]. The image consists of S-equivalence classes represented
by the actual locally free restrictions.

This conditional ADVANCE / REPRODUCTION is a specialization of the
published chamber, polynomial and moduli inputs below, not progress
beyond those sources. It establishes no F, absence of reducibles,
generic polarization, universal sheaf, quotient smoothness, global
separation, embedding, integrated germ, algebraic cycle or transverse
transport. The equality/positive-Euler kernel-existence gap and the
universal primitive Hodge-realization gap remain open. The separate
critical audit below preserves this specialization.

## Proof

**Uniform real slope input.** Import Daniel Greb and Matei Toma,
*Compact moduli spaces for slope-semistable sheaves*, Algebraic
Geometry **4** (2017), 40--78, doi:10.14231/AG-2017-003,
[Theorem 6.6 and proof, p. 74, and Section 6.3.3, p. 75](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=35).
For fixed topological invariants of torsion-free sheaves on a smooth
complex projective n-fold and compact K in
P(S_1)={A^(n-1): A real ample}, finitely many rational linear walls
give identical slope stability and semistability for all such
sheaves at two classes in one connected chamber stratum. Section
6.3.3 includes lower-dimensional strata. The general theorem and
its uniform quantifier are imported, not reproved. On the surface
S_1, P(S_1) identifies with the real ample cone in N^1(S_1)_R via
the intersection pairing. Rank two, c_1=0 and c_2=14 eta fix all
the Chern invariants of these surface sheaves.

L063 is a methodological comparison for the rational-stratum and
actual-family arguments. Its charge-seven stable-family conclusion
is not used as an input for this changed stable/split family. The
additional equality H.k=0 and the split-polynomial check below
are essential here.

**One rational polarization retaining the split slope.** Let
V=N^1(S_1)_R with rational structure N^1(S_1)_Q. Choose a compact
convex neighborhood K of h contained in the real ample cone, with
h in its interior. This is possible because the cone is open.
Apply the imported theorem to K and the fixed invariants above;
write the resulting rational wall equations as ell_i(alpha)=0.
Let I_0={i:ell_i(h)=0} and put

\[
 W=\left(\bigcap_{i\in I_0}\ker ell_i\right)
                  \cap\{\alpha:q(k,\alpha)=0\}.
\]

The extra equation is rational because k is integral; it is imposed
whether or not it is one of the supplied walls. W is a rational
linear subspace containing h. A rational defining matrix gives a
rational basis by row reduction, so W_Q is dense in W. All wall
functionals with i outside I_0 are nonzero at h. A sufficiently
small relative neighborhood of h in W, inside the interior of K,
preserves their strict signs. Choose a rational alpha there. It is
ample and satisfies alpha.k=0.

The segment from h to alpha stays in K by convexity, stays on all
walls in I_0, and crosses no other wall since the signs at both
ends agree. Thus h and alpha lie in the same connected relative
wall stratum. Restricting further to k-perp does not change that
fact. The imported theorem simultaneously preserves slope stability
and semistability for every sheaf with these fixed invariants;
in particular every stable E_y remains alpha-slope-stable.

Clear denominators by a positive integer m_0 and choose a line
bundle H_0 of numerical class m_0 alpha. It is ample because its
numerical class is ample. Choose a positive power H=H_0^{tensor t}
that is very ample, by Hartshorne, *Algebraic Geometry*, Chapter II,
Theorem 7.6. Scaling a surface polarization by a positive number
multiplies all slopes by that number and preserves every strict or
weak inequality; the scaled class need not stay in K. Thus every
stable E_y is H-slope-stable, and H.k=0. At a point of Z, each
actual line L^{+/-1} has H-slope zero and is slope-stable of rank
one, so their sum is H-slope-polystable. This establishes one
polarization for the whole family without a point-dependent choice
or an assumption that h lies in an open full-dimensional chamber.

**Gieseker stability and the actual split polynomials.** Import
Huybrechts and Lehn, *The Geometry of Moduli Spaces of Sheaves*,
Aspects of Mathematics E31 (1997),
[Definitions 1.2.3--1.2.4 and Lemma 1.2.13, pp. 10--14](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=22).
For a pure full-dimensional sheaf, slope stability implies Gieseker
stability at the same integral polarization. The locally free
stable fibres are pure of dimension two, so this applies off Z.
Slope semistability alone would not justify the desired conclusion
at Z.

The K3 surface Riemann--Roch formula is
chi(O(D))=2+D^2/2. Its primary inputs are the surface formula in
[Huybrechts--Lehn, proof of Proposition 5.2.2, p. 129](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=141)
and the K3 facts K_{S_1}=0 and chi(O_{S_1})=2 on
[p. 133](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=145).
Using H.k=0 and k^2=-14 gives, for either sign,

\[
 P_{L^{\pm1}}(n)=chi(L^{\pm1}\otimes H^n)
       =2+\frac{(\pm k+nH)^2}{2}
       =\frac{H^2}{2}n^2-5.                         \tag{1}
\]

Each line is Gieseker-stable: a nonzero proper subsheaf of a line
has rank one and a nonzero quotient of dimension at most one.
That quotient has positive Hilbert polynomial for sufficiently
large n, so subtraction strictly decreases the reduced polynomial;
there is no torsion subsheaf. Equivalently, rank-one slope stability
and Lemma 1.2.13 apply. In the source convention
P(n)=a_2 n^2/2+lower terms and p=P/a_2, each line has
a_2=H^2 and reduced polynomial

\[
                       p(n)=n^2/2-5/H^2.
\]

They therefore have exactly equal reduced polynomials, not merely
equal slopes. Import
[Huybrechts--Lehn Remark 1.5.12, p. 24](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=36):
semistable objects with a fixed reduced polynomial form the relevant
abelian category, with stable objects simple and polystable objects
semisimple. Their direct sum is consequently Gieseker-polystable.
It is strictly semistable because either summand is proper and has
the same reduced polynomial as the sum. This proves the required
changed split-fibre assertion.

**Algebraization, flatness and fixed numerical class.** GAGA on the
projective complex product algebraizes the actual holomorphic F
as a vector bundle and preserves its restrictions and morphisms.
The projection p_2 is smooth, hence flat, and F is locally free
on X; consequently F is flat over S_2. This is an actual flat
family, not an assignment of closed-point sheaf classes.

At every closed fibre ch(E_y)=2-14 eta. Since
td(S_1)=1+2 eta and sqrt(td(S_1))=1+eta, surface HRR yields

\[
 \begin{aligned}
 P_H(n)&=\int_{S_1}(2-14\eta)e^{nH}(1+2\eta)
                  =H^2 n^2-10,\\
 v(E_y)&=(2-14\eta)(1+\eta)=(2,0,-12).
 \end{aligned}                                                    \tag{2}
\]

For a split fibre (1) adds to exactly the same P_H. Its leading
coefficient in the source convention is 2H^2, giving the same
reduced polynomial displayed above. The flat family has this fixed
Hilbert polynomial; Euler characteristics are locally constant
and S_2 is connected. Moreover, for every A in K_0(S_1),

\[
 chi(E_y\otimes^{\mathbf L} A)
     =\int_{S_1}(2-14\eta)ch(A)td(S_1)
\]

is independent of y. Smoothness makes dualization permute K_0,
so this also fixes all Ext Euler pairings. These pairings verify
the fixed numerical K-class, rather than identifying the entire
fixed-polynomial moduli space with one Mukai-vector part.

**All geometric fibres.** Import
[Huybrechts--Lehn Corollary 1.3.8, p. 18](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=30)
on semistability under field extension, and
[Corollary 1.5.11, p. 24](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=36)
on geometric stability of stable sheaves over an algebraically closed
field, together with
[Proposition 2.3.1 and its proof, p. 45](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=57)
on openness of geometric (semi)stability in a flat polarized family.
The closed fibres proved semistable above are over the algebraically
closed field C and hence geometrically semistable; the split cases
also remain direct sums of the same stable equal-polynomial lines
under field extension. The geometric-semistability locus is open
in S_2 and contains all closed points. Its closed complement must
be empty, since a nonempty closed subset of a finite-type C-scheme
contains a closed point. Thus every geometric fibre is semistable,
including fibres over nonclosed scheme points.

Let Z_red denote the reduced finite closed subscheme with points Z,
and U=S_2 minus Z_red. Every closed fibre over U is geometrically
stable by Corollary 1.5.11, since its field is C. On U the geometric-stability
openness argument shows every geometric fibre stable. At a point
of Z_red, the direct sum is strictly semistable as checked above.
Consequently the geometric-stability locus is exactly U. No
multiplicity or reducedness of a different naturally defined jump
locus is inferred from the use of Z_red.

**Corepresentation gives the whole map.** Import the flat-family
moduli functor in
[Huybrechts--Lehn Section 4.1, p. 80](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=92)
and its projective corepresenting Gieseker scheme and stable open in
[Theorem 4.3.4, p. 91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=103).
The actual family F, with all geometric fibres semistable and fixed
polynomial (2), defines an object of that functor over the whole
S_2, modulo the permitted twists by base line bundles. Its natural
classifying transformation supplies an algebraic morphism to the
projective moduli scheme. This constructs the morphism at once
across Z_red; no extension theorem for a punctured map is used.

The fixed-numerical-class parts are open and closed as described in
[Huybrechts--Lehn Section 8.1, p. 180, before Definition 8.1.4](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=192).
The numerical Euler-pairing calculation above places this morphism
in M_H^{ss}(2,0,-12). An open-and-closed part of the projective
scheme is projective. Corepresentation needs no universal sheaf.
Closed points record S-equivalence, so all exceptional fibres give
the single point [L direct sum L^{-1}]. A strictly semistable
polystable sum cannot be S-equivalent to a stable sheaf: its
Jordan--Hölder graded object has two nonzero rank-one factors,
whereas a stable sheaf is already its sole stable factor.
The stable open therefore has preimage exactly U. The constructed
map and its stable restriction establish the stated conditional
placement; they say nothing about separation of distinct points
in U or about the existence of the initial kernel.

**Separate critical audit, 2026-10-12 (step 252).** The approved
audit preserves the conclusion and finds no substantive mathematical
error or stronger consequence. Its outcome is EXPLORATION /
REPRODUCTION, not a new advance. The explicit Corollary 1.5.11 citation
above makes the already covered geometric-stability bridge transparent;
it changes no hypothesis or conclusion. The direct mathematical inputs
remain L071 and L096. L063 is comparison only.

The input match is exact: L071 applies with a=-18 and b=-25, so its
factor charges are 14 and 21. Restriction to S_1 kills e_2 and the
mixed class and yields ch(E_y)=2-14 eta with integral first class zero.
The actual restricted connection supplies h-polystability on every
closed fibre. In its nonsimple branch, 14=14r^2 gives r=+/-1;
Pic^0(S_1)=0 identifies the actual lines as L and L^{-1}. Audited
L096 makes the parameter set finite, including the possibility that
it is empty. No generic-fibre stability or existence assertion has
been added to these conditional inputs.

For the uniform choice, Greb--Toma Theorem 6.6 and Section 6.3.3
apply to surface Chern invariants and include the relative wall
stratum containing h. Every equality in W has rational coefficients,
including the independently imposed k-orthogonality equation. Since
h lies in W and is ample, a sufficiently small relative ball in W
is nonempty and lies in the ample cone. Density of rational points
therefore does not require h to be rational, or W to meet a different
chamber. Each remaining linear wall functional retains its strict
sign along the segment: its value is a convex combination of two
nonzero values of the same sign. This verifies the connected-stratum
condition for every fixed-Chern sheaf at once. Clearing denominators
and then taking a very ample power preserves all slope comparisons
and k-orthogonality, even after the scaled class leaves K. No assertion
that arbitrary polystable sheaves stay polystable follows merely from
the chamber theorem; here the stable fibres stay stable and the
known split fibres stay sums of the same zero-slope lines.

At the final H, the two polynomials are both H^2 n^2/2-5.
Their sum is H^2 n^2-10, with factorial-convention leading
coefficient 2H^2; division gives n^2/2-5/H^2 in all three cases.
A proper subsheaf of either line has a nonzero torsion quotient
of eventually positive polynomial, which strictly lowers its reduced
polynomial. Thus both factors are stable, and their equal reduced
polynomials justify strict Gieseker polystability of the sum.
This verifies the split case directly instead of inferring it from
slope semistability. The same RR computation gives v=(2,0,-12),
not (2,0,-14).

GAGA algebraizes the locally free F on the projective product; its
restriction agrees with each analytic E_y. The projection is smooth
and projective and F is locally free, giving the base flatness
required in Proposition 2.3.1. The chosen H is relatively very ample
after pullback to the product. All closed fibres are semistable and
Corollary 1.3.8 handles extension fields. For stability, the distinct
Corollary 1.5.11 applies over C before openness is used on U. Each
closed complement of the relevant open locus, in S_2 or in U,
would contain a closed complex point if nonempty, since these schemes
are of finite type over C. Hence the argument really treats every
geometric point. The split summand remains a proper equal-polynomial
subsheaf after any field extension, so the exceptional geometric
fibres remain strictly semistable.

Finally the actual flat family, not a closed-point assignment,
is the object to which the classifying natural transformation of
Section 4.1 and Theorem 4.3.4 is applied. The Euler pairings against
every class A of K_0(S_1) are fixed; for nonclosed fibres the
open-and-closed numerical-class locus in Section 8.1, p. 180,
and the same closed-point argument retain that class. The induced
map therefore factors through its open-and-closed projective part.
Its stable-open preimage is U: a stable object and the two-factor
polystable sum cannot have the same Jordan--Hölder graded object.
Equality of these open subschemes follows from their underlying open
sets and entails no multiplicity claim at Z_red. All members of Z
have the same actual split isomorphism class, hence the same moduli
point. Finiteness of Z alone gives no separation elsewhere, no
finiteness assertion for the whole map, and no absence of reducibles.
The audit establishes neither kernel existence nor an integrated germ,
cycle, transverse transport or universal Hodge resolution.

## Mathlib

Full matching coverage for real fixed-Chern wall strata, this
Gieseker-polystable specialization and projective flat-family
corepresentation: **not checked**. Unknown availability is not
absence. The cited primary theorems supply the general results;
the explicit rational-orthogonality, polynomial and geometric-family
checks supply only their conditional applicability here.
