# L021 — Positive ideal-cohomology vanishing in fibre degree three

## Hypotheses

Use the very general cubic RM surface S, elliptic fibre F, sections O
and P=(x_0,y_0), exceptional component E, correspondence C in X=S x S,
and normalization nu:W -> C of L008 and L019. In particular y_0 is
nonzero and the fibre at infinity has components E and R=F-E.
Fix the original ample line bundle L with L.F=3 and set
H=L external tensor L. All cohomology is coherent cohomology over C.

## Conclusion

For every integer r>0,

\[
H^1(X,I_C(rH))=0.                                      \tag{1}
\]

The original restriction problem is transported by an automorphism
preserving C to one of the following forms:

\[
\begin{array}{c|c|c}
&L&L^2\\ \hline
\mathrm A&3O+bF-E,\quad b\ge7&6b-20\\
\mathrm B&2O+P+bF,\quad b\ge5&6b-10.
\end{array}                                             \tag{2}
\]

The restriction image has dimension
1+4r^2L^2-6r, exactly the dimension of H^0(C,H^r|_C).
All three normalization gluing conditions are retained.

This closes the cohomological exception to sufficient summand recovery
in fibre degree three, in every positive degree. It does not decide
the saved question for L.F>=4, erase L020's degree-two exception, or
construct a transverse lift. The attained cycle span and the universal
rational Hodge gap are unchanged.

## Proof

**Transporting the original class.** L020 proves that the classes
F,O,E,P form an integral basis of NS(S), using the squarefree
determinant -7 computed in L019. Their line bundles give the same basis
of Pic(S), since a K3 has no Picard variety or Picard torsion.
The generic-fibre class of any degree-three L has group sum eP for
an integer e. Pullback by translation by jP changes this to (e-3j)P.
Choose the remainder in {-1,0,1}, and use inversion if it is -1.
The result restricts on the generic fibre to either 3O or 2O+P.
Its difference from that divisor is vertical, hence an integral
combination of F and E; all other fibres are irreducible.

The positive integers L.E and L.R add to three. If the generic class
is 3O, write L=3O+bF+cE. Then L.E=-2c forces c=-1.
If it is 2O+P, then L.E=1-2c forces c=0.
Intersecting with O gives respectively b-6>=1 and b-4>=1.
The intersection matrix gives the squares in (2).

Translation by a section extends to the minimal elliptic surface;
use the statement already imported in L020 from Schuett--Shioda,
[*Elliptic Surfaces*, arXiv:0907.0298v3, section 7.6,
pp. 33--34](https://arxiv.org/pdf/0907.0298v3#page=33).
Inversion extends as well, directly by (x,y)->(x,-y) on the
Weierstrass model and its resolution. The pullback section P on W
has constant Laurent coordinates. Its translations and inversion
commute with sigma, and intertwine both g_0 and g_1. Thus their
simultaneous action preserves C in S x S and transports its actual
restriction map. No unrelated polarization has been substituted.

Both ranges in (2) are nonempty. L019's section formula gives

\[
\begin{aligned}
(3O+bF-E).Q_j&=b-6+(21j^2-\epsilon_j)/4,\\
(2O+P+bF).Q_j&=b-4+(21j^2-14j+\epsilon_j)/4,
\end{aligned}
\]

where Q_j=jP and epsilon_j is the parity of j. These numbers are
positive for every integer j at the bounds in (2). The component
degrees are (2,1) and (1,2). All negative curves are sections or
these components by L019, and every section is a Q_j by the integral
basis argument in L020. Each displayed class has positive square
and positive intersection with F. Hodge index gives positive
intersection with every other irreducible curve; Nakai--Moishezon
therefore proves ampleness in the displayed ranges.

**Divisor bounds and the target dimension.** At infinity the minimal
coordinates of L008 are X=q^4x, Y=q^6y. The functions q,X,Y have
orders (1,0,0) at a general point of R and (1,1,1) at a general
point of E. Thus the vertical pole orders of x are (4,3), and of y
are (6,5), on (R,E). Their horizontal poles are 2O and 3O.
There are no other vertical poles. In form B also use
z=(y+y_0)/(x-x_0). L020 checks its horizontal poles O+P, cancellation
at -P even over finite singular fibres, and vertical orders at most
(2,2). Divisorial pole bounds suffice on the smooth S, including
the points where the components are tangent.

The rotation preserves O_W, P_W, both exceptional components, and
T_0+T_infinity=g_0^*F_infinity. Consequently the two pullback divisors
in either form (2) agree, and

\[
M=\nu^*(H|_C)=g_0^*(2L).
\]

L008's splitting g_(0*)O_W=O_S direct sum O_S(-F), the finite
projection formula, and K3 Riemann--Roch give

\[
h^0(W,M^r)=4+4r^2L^2-6r.                              \tag{3}
\]

Here 2rL-F=(L-F)+(2r-1)L is ample by L019, so Kodaira vanishing
justifies the second summand's Riemann--Roch calculation. L019's
surjective six-point evaluation and exact normalization sequence give

\[
h^0(C,H^r|_C)=h^0(W,M^r)-3.                           \tag{4}
\]

In particular (4) includes the gluing at the tangency fixed point.
We will exhibit ambient products with this dimension, not arbitrary
sections on W that fail to descend.

**The coefficient input.** Put t=v+a/v and
s=zeta v+a zeta^(-1)/v on W, with zeta a primitive seventh root.
For A,B>=1, L020 proves that the products of polynomials of degrees
at most A in t and at most B in s span the hyperplane

\[
U_{A,B}=\{c\in V_{A+B}:
c_{-(A+B)}=a^{A+B}\zeta^{-2B}c_{A+B}\},              \tag{5}
\]

where V_N consists of Laurent polynomials with exponents from -N to N.
It has dimension 2(A+B). Two such hyperplanes with the same A+B
span V_(A+B) if their B values differ by an integer not divisible
by seven. We use this proved coefficient calculation directly.

In the bases below all coefficient degrees are at least r. The
elliptic functions have the same expression under the two projections.
The canonical rational trivializations associated to the divisors in
(2) identify the products with exactly (5); their section subspaces
have not been enlarged to complete systems on W.

**Form A: complete section spaces.** Set

\[
\begin{gathered}
p=\lfloor3r/2\rfloor,\qquad q=\lfloor(3r-3)/2\rfloor,\\
A_i=rb-4i-(r-i)_+\quad(0\le i\le p),\\
B_j=rb-6-4j-(r-1-j)_+\quad(0\le j\le q),
\end{gathered}                                         \tag{6}
\]

where u_+=max(0,u). A basis of H^0(S,rL) is

\[
x^i t^k\ (0\le k\le A_i),\qquad
yx^j t^k\ (0\le k\le B_j).                           \tag{7}
\]

Indeed the generic-fibre functions x^i,yx^j have distinct pole
orders 0,2,3,...,3r at O and form its degree-3r section basis.
The R and E bounds above give exactly (6) for these functions:
the E inequality includes the coefficient -rE in rL.
Both A_i and B_j are at least r(b-6)>=r. The sum of their pole
weights is

\[
2p(p+1)+(q+1)(6+2q)+r^2=10r^2+3r-2.
\]

There are 3r generic-fibre functions. Hence (7) has
2+r^2(3b-10)=2+r^2L^2/2 sections, which is the full dimension
by Kodaira vanishing and Riemann--Roch. Independence over C(t)
of the elliptic functions proves independence of the exhibited sections.

On W a complete basis for M^r has blocks

\[
\begin{array}{ll}
x^k V_{C_k},&0\le k\le3r,\quad
C_k=2rb-4k-(2r-k)_+,\\
yx^k V_{D_k},&0\le k\le3r-2,\quad
D_k=2rb-6-4k-(2r-1-k)_+.
\end{array}                                           \tag{8}
\]

The bound applies at both fibres over infinity since the base change
there is unramified. The functions are independent on the generic
elliptic fibre after base extension. Their total dimension is
2h^0(S,2rL)-6r, equal to (3), proving completeness of (8).

**Form A: all product ranks.** For an x^k block the x*x allocations
i+j=k have coefficient sum C_k exactly when both i,j<=r for k<=2r,
or both i,j>=r for k>=2r. In the range 1<=k<=2r-1 there are two
adjacent allocations with i,j<=r. Their second degrees differ by
three, so (5) fills V_(C_k). For 2r<k<2p, use adjacent allocations
with i,j>=r; the difference is four, again filling the block.
At k=0 and k=2r the respective allocations (0,0) and (r,r) give
one hyperplane. If r is even, 2p=3r and (p,p) gives the third
hyperplane at k=3r. All other even blocks are full in that case.

If r is odd, 2p=3r-1 and the two highest blocks require attention.
The actual Weierstrass identity is

\[
(yx^i)(yx^j)=x^{i+j+3}
 +(b_1P_a(t)+b_0)x^{i+j+1}
 +(c_1P_a(t)+c_0)x^{i+j}.                            \tag{9}
\]

On W, P_a(t)=v^7+a^7v^(-7)=P_a(s). The allocation i=j=q has
leading exponent 3r and gives U_(B_q,B_q), a hyperplane in V_(C_(3r)).
For odd r>=3, the allocations (q-1,q) and (q,q-1) have leading
exponent 3r-1. Both indices are at least r-1, so their coefficient
degrees sum to C_(3r-1) and differ by four. They fill that leading
block by (5). The lower terms in (9) lie in strictly smaller x blocks;
retaining them gives a triangular independence argument. Thus these
products add their full leading ranks even when those lower terms
are not in the previously chosen span. For r=1 the block 3r-1=2r
is already one of the designated hyperplanes; y*y supplies only
the top hyperplane. In every case the three deficient even blocks
are precisely the selected blocks k=0,2r,3r, each of codimension one.

For a yx^k block use x^i times yx^j, and the reversed factors.
Their coefficient sum is D_k if i<=r,j<=r-1 for k<=2r-1,
or i>=r,j>=r-1 for k>=2r-1. In each of the two allocation rectangles,
every non-endpoint diagonal has two adjacent allocations, whose
second degrees differ by three or four. The endpoints are k=0,
2r-1 and p+q=3r-2. There the allocation and its reversal have
second degrees differing respectively by five, two and two.
This also covers r=1,2, when an upper rectangle has width zero:
all its diagonals are endpoints. Formula (5) therefore fills
every odd block in (8).

The independent blocks and the triangular argument for (9) produce
a subspace of ambient restrictions of dimension h^0(W,M^r)-3.
Every such product descends to C. By (4) they fill H^0(C,H^r|_C).

**Form B: complete section spaces and product ranks.** A basis of
H^0(S,rL) consists of the following elliptic functions with polynomial
coefficients of the indicated maximum degrees:

\[
\begin{array}{c|c|c}
\text{function}&\text{range}&\text{coefficient degree}\\ \hline
x^i&0\le i\le r&rb-4i\\
x^i z&0\le i\le r-1&rb-4i-2\\
z^j&2\le j\le r&rb-2j.
\end{array}                                           \tag{10}
\]

Their horizontal poles are bounded by 2rO+rP, and the vertical
bounds follow from those of x and z. All coefficient degrees are
at least r(b-4)>=r. To see generic-fibre independence, successively
remove the z^j terms using their distinct pole orders j>=2 at P;
the remaining x^i and x^i z have distinct pole orders at O.
There are 3r functions, the genus-one Riemann--Roch dimension.
Counting all polynomial coefficients gives 2+r^2(3b-5), equal to
2+r^2L^2/2; therefore (10) is the full global section space.
On W, replace r by 2r and each polynomial coefficient space by
the Laurent space with that same symmetric bound. The divisor
bounds, generic-fibre independence and dimension (3) prove completeness.

Products of x powers fill each x^k coefficient block except k=0,2r,
where they give hyperplanes. Interior allocations differ by four.
Products x^i times x^j z, with their reversals, fill every x^k z
block: adjacent allocations differ by four, while at k=0,2r-1
the sole allocation and its reversal differ by two.
Finally products of z powers (including z^0=1 and z^1=z from the
other rows) fill the z^k blocks for 2<=k<2r by adjacent degree
differences of two. At k=2r there is one hyperplane.
For r=1 this last range has only that endpoint, as required.
These products need no reduction by the elliptic equation.
They span a subspace of codimension exactly three on W, so (4)
again proves surjectivity onto H^0(C,H^r|_C).

Finally H^1(X,H^r)=0 by Kodaira vanishing on S and Kunneth.
The ideal sequence identifies H^1(X,I_C(rH)) with the restriction
cokernel, proving (1) in both forms and hence for every original L
with L.F=3.

**Scope, source comparison and checks.** The known translation,
vanishing and Riemann--Roch inputs are imported. The prior SPECIALIZE
assessment compares Franciosi--Tenni's
[Theorem 4.2, p. 49](https://people.dm.unipi.it/franciosi/lavori/franciosi-tenni2.pdf#page=13)
and Gallego--Purnaprajna's
[Proposition 2.2 and Corollary 2.3, p. 4](https://arxiv.org/pdf/alg-geom/9608008v1#page=4).
Those complete curve or K3 multiplication statements do not determine
the two projection subspaces or their three-condition global descent
image. The calculations (6)--(10) address that identified difference;
they do not reprove a general normal-generation theorem. The full
specialization was not matched by the checked literature, without
certified originality.

The command
`python3 scripts/cubic-deformation/check_fibre_degree_three_restriction.py`
checks actual product matrices in characteristic 43, including the
coupled lower terms in (9). These finite arithmetic checks do not
replace the resolved divisor arguments, the all-r allocation proof,
or the three-point descent theorem. The required starting degree r=1
and the entire positive tail are proved here in fibre degree three.
The complementary range L.F>=4 and any transverse cycle construction
remain unresolved. No complete Hodge candidate is asserted.

## Mathlib

Coverage of the full statement: **not checked**. No supporting Mathlib
match or absence is asserted. The directly linked Schuett--Shioda
statement supports translation; the linked Franciosi--Tenni and
Gallego--Purnaprajna statements are comparison tools, not matches for
(1). Kodaira vanishing, K3 and genus-one Riemann--Roch, Hodge index,
Nakai--Moishezon, finite projection formula and Kunneth are named
standard inputs. The original-class reduction, resolved component
bounds and actual all-degree restriction calculation are supplied above.
