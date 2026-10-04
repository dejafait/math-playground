# L014 — Exact coefficient feasibility and affine-moment compatibility

## Hypotheses

Let F=F_(97^20), let H be the subgroup of order sixteen in F_97^*,
and use C=RS[F,H,8] and the event in
[the pinned model](../foundations/02-pinned-affine-line-model.md)
on 1/4<=delta<5/16. All unknown coefficients below range over F,
not just its prime subfield.

For u,v in F^8 put s_j(T)=u_j+T*v_j, j=1,...,8. Let D_m(T) and
L_m(T,X) be the determinant and signed-minor locator of L010 for these
eight affine moments. Write
\[
 L_m(T,X)=\sum_{j=0}^4 c_j(T)X^j,\quad c_4=D_m,\qquad
 \ell_x(T)=L_m(T,x),\quad R(T)=\prod_{x\in H}\ell_x(T).
\]
Every c_j has T-degree at most four. Set q=97^20.

## Conclusion

There is a pair of input words with exactly sixteen bad parameters,
with nonzero D_m and all coordinate locators nonzero as polynomials,
if and only if the following coefficient system has a solution:
\[
 \begin{gathered}
 P(T)=T^{16}+\sum_{j=0}^{15}p_jT^j,\qquad c\in F^*,\qquad
 R(T)=cP(T)^4,                                           \tag{1}\\
 \gcd(\ell_x,\ell_x')=1\quad(x\in H),\qquad
 \gcd(P,P'D_m)=1,                                        \tag{2}\\
 T^q-T\equiv0\pmod P.                                   \tag{3}
 \end{gathered}
\]
Here R and the locators in (1)–(2) are the actual signed minors of the
specified affine moments. Conditions (1) and c!=0 force every ell_x to
have degree four, hence to be nonzero; (2) implies D_m is nonzero.
No additional condition that c itself be a fourth power in F is imposed.

This is an exact encoding of L010's equality case, not an existence
or impossibility theorem or an improvement of the global count.

The 65 coefficient equations in (1) can be audited without treating
the p_j as search variables. If r_k=[T^k]R, first require r_64!=0,
set c=r_64, and put a_j=r_(64-j)/c, 0<=j<=64. With w_0=1 define
successively, for 1<=j<=16,
\[
 w_j=\frac{a_j-[Z^j]\left(1+w_1Z+\cdots+w_{j-1}Z^{j-1}\right)^4}{4}. \tag{4}
\]
The only possible monic P has p_(16-j)=w_j. Equation (1) then holds
exactly when all the remaining 48 coefficient residuals, for
17<=j<=64, vanish. No independence of these residual equations is
asserted. Conditions (2)–(3) are still required.

There is also an exact inverse compatibility test for a supplied
bivariate locator candidate
\[
 K(T,X)=\sum_{j,h=0}^4 k_{j,h}T^hX^j.
\]
Suppose its coordinate evaluations, product R_K, leading X-coefficient
d_K(T), and a monic P already satisfy (1)–(3), with D_m replaced by
d_K. Define a 24-by-16 matrix N(K) on (u,v) by the equations
\[
 \sum_{j=0}^4\bigl(k_{j,h}u_{i+j}+k_{j,h-1}v_{i+j}\bigr)=0,
 \quad 1\le i\le4,\quad 0\le h\le5,                     \tag{5}
\]
where k_(j,h)=0 outside 0<=h<=4. Then K is a nonzero constant
multiple of an actual affine-moment locator with sixteen bad parameters
if and only if ker N(K) contains a vector (u,v) for which D_m is not
the zero polynomial. In particular rank N(K)<=15 is necessary, but
that rank inequality alone is not asserted to be sufficient.

## Proof

L010's syndrome map F^H to F^8 is onto: any eight columns form an
invertible Vandermonde matrix with nonzero diagonal factors. Thus
arbitrary u,v are realized by input words a,b. Their event depends on
these moments through L010 once its nonvanishing hypotheses hold.

Import the monic split resultant product formula, Milne, *Fields and
Galois Theory*, v5.10 (September 2022), Proposition 4.35(b),
[printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58).
It identifies R with Res_X(X^16-1,L_m(T,X)), over F[T]; the ring
version is covered by the previously inspected Mathlib declarations
listed below. The second polynomial need not be monic.

Suppose (1)–(3) hold. Since deg R=64 and the sixteen coordinate
polynomials have degrees at most four, every one has degree exactly
four. Condition (3) makes P split into distinct linear factors in F:
T^q-T has exactly all elements of F as roots and has derivative -1.
The explicit condition gcd(P,P')=1 in (2) is therefore redundant with
(3), but useful as a separate algebraic audit. Each ell_x divides the
product cP^4, so all of its roots are among the roots of P and lie in
F. Condition (2) makes each ell_x squarefree. At any root gamma of
P, the product has multiplicity four. Because each coordinate factor
is simple, exactly four different coordinates vanish there. Also
D_m(gamma)!=0 by gcd(P,D_m)=1. L010's full equality criterion applies:
there are exactly sixteen bad parameters, each with a weight-four
representative and failure on the same agreement support. Its theorem
also gives distinct supports; this is not an extra decoder assumption.

Conversely, an equality pair has all the properties stated in L010.
Its sixteen coordinate quartics have a union B of sixteen field roots,
each occurring at exactly four coordinates, and D_m is nonzero on B.
Set P=product_(gamma in B)(T-gamma). The product R is cP^4, where
c is its nonzero leading coefficient. Coordinate simplicity and
D_m-nonvanishing prove (2); all roots in F prove (3). This establishes
the exact direct feasibility statement. It uses the original event
through L010's same-support argument, not closeness alone.

To derive (4), reverse the monic polynomial R/c and the putative monic
P. The latter has reversed form W(Z)=1+w_1Z+...+w_16Z^16, and
the reversed R/c is W^4. For 1<=j<=16, the coefficient [Z^j]W^4
contains the still unknown w_j exactly four times, each time with
the other three factors equal to their constant terms. All its other
terms use earlier coefficients. Since 4 is invertible in characteristic
97, (4) uniquely determines w_j. This matches the top sixteen
coefficients. Comparing degrees 17 through 64 of the reversed
polynomials gives exactly the remaining 48 residuals. It does not
imply squarefreeness, field splitting or (2).

For completeness this elimination need not produce small polynomials
in the sixteen moment variables. Set z_j=c^j*w_j and z_0=1. The
denominator-free version of (4) is
\[
 4z_j=c^{j-1}r_{64-j}
       -\sum_{\substack{i_1+\cdots+i_4=j\\0\le i_l<j}}
          z_{i_1}z_{i_2}z_{i_3}z_{i_4}.                  \tag{6}
\]
For 17<=j<=64 the cleared residual is
\[
 c^{j-1}r_{64-j}
       -\sum_{\substack{i_1+\cdots+i_4=j\\0\le i_l\le16}}
          z_{i_1}z_{i_2}z_{i_3}z_{i_4}=0.                \tag{7}
\]
The summations are over ordered tuples. Each r_k and c is homogeneous
of degree 64 in u,v; inductively z_j has degree at most 64j.
The last cleared residual can consequently have degree as high as
4096. Equations (6)–(7) are equivalent to the rational test only on
the required open set c!=0. Clearing denominators does not remove
that hypothesis or make a naive elimination practical.

Now consider the inverse test. For K satisfying the algebraic gates,
its five coefficient polynomials in T have gcd one. Indeed, an
irreducible common factor would divide R_K=cP^4 and also d_K. It
would therefore divide both P and d_K, contrary to (2). Also at least
one of these coefficients has degree four, because each coordinate
evaluation has degree four.

Equations (5) are exactly the coefficients in T of
\[
 \sum_{j=0}^4 k_j(T)s_{i+j}(T)=0\quad(1\le i\le4),
 \qquad k_j(T)=\sum_h k_{j,h}T^h.                        \tag{8}
\]
If K is proportional to the actual locator, (8) follows from the
duplicate-row determinant identity in L010, so necessity holds.
The actual moment vector is nonzero and has D_m nonzero, proving
rank N(K)<=15.

For sufficiency choose a vector in ker N(K) with D_m nonzero. The
four-by-five moment matrix then has rank four over F(T). Its kernel
is one-dimensional, containing both the nonzero signed-minor vector
of L_m and the coefficient vector of K. Thus L_m=f(T)K for some
f in F(T)^*. Since the k_j have gcd one, Bezout's identity gives
polynomials b_j with sum_j b_j*k_j=1. Multiplication by f shows
f=sum_j b_j*[X^j]L_m, so f lies in F[T]. Some k_j has T-degree
four while every coefficient of L_m has degree at most four. The
product degree formula therefore makes f a nonzero constant. All
algebraic gates transfer under this scalar: the product scalar becomes
f^16*c and D_m=f*d_K. The already proved direct system yields sixteen
bad parameters. This also explains why a nonzero kernel vector with
identically zero D_m is insufficient.

This inverse encoding can replace the 25 quartic signed-minor equality
equations by 24 bilinear recurrence equations and a nonzero-minor
condition, when the other algebraic gates are present. For a literal
polynomial system the last condition can be expressed by five new
variables omega_r and sum_(r=0)^4 omega_r*D_m(r)=1. A degree-at-most-four
polynomial is nonzero if and only if at least one of its values at the
five distinct points 0,...,4 is nonzero. All other nonzero resultants
can likewise be encoded by an auxiliary inverse. This is an equation
encoding, not a claim about solvability or solver cost.

The exact controls in `python3 scripts/coefficient-feasibility/check.py`
audit the coefficient signs, recurrence matrix, top-down recursion,
nonzero-minor recovery, scalar normalization and exact q-field splitting.
They include the fabricated polynomial
\[
 K(T,X)=\prod_{\alpha\in\{1,8,64,27\}}(T-\alpha X)
 =T^4-3T^3X+33T^2X^2+16TX^3+50X^4.                     \tag{9}
\]
Its coordinate product is (T^16-1)^4: for each alpha, multiplication
by alpha permutes H in product_(x in H)(T-alpha*x). Its coordinate
quartics are simple and its leading X-coefficient is the nonzero
constant 50. Each root t in H occurs at the four coordinates t/alpha.
The supports are translates of the exponent set {0,1,2,3} in Z/16Z;
its cyclic shifts are distinct, so there are sixteen distinct supports.
Nevertheless
ker N(K)=0. In fact (8)'s T^5 terms give v_1,...,v_4=0; its T^0
terms give u_5,...,u_8=0. The T^4 terms with i=1,2,3 give
u_1,u_2,u_3=0, and the T^1 terms with i=2,3,4 give v_6,v_7,v_8=0.
The remaining equations include u_4-3v_5=0 and -3u_4+33v_5=0.
Their determinant is 24!=0 in F, so u_4=v_5=0 as well. Thus the
rank is sixteen over every extension, not just in the numerical check.
This is a control for the already excluded orbit mechanism of L009,
not a new general obstruction or a reopening of that branch.

The three primitive actual controls have compatibility rank fifteen
and a one-dimensional kernel recovering their minors up to scalar;
the fixed-four-support control has rank eight but persistent locators
and is correctly excluded by the other gates. None of the actual
controls is an equality witness. These finite controls do not prove
that the full system is feasible or infeasible over F_(97^20).

## Mathlib

The full coefficient feasibility and inverse compatibility formulation:
**not checked** in Mathlib. Supporting resultant product, evaluation and
specialization coverage is **present** in the previously inspected
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including `Polynomial.resultant_prod_left`,
`Polynomial.resultant_eq_prod_eval` and `Polynomial.resultant_map_map`.
Direct supporting declaration links are
[Polynomial.resultant_prod_left](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[Polynomial.resultant_map_map](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
The full formulation is **absent from that source checked**; coverage
elsewhere and supporting kernel/Bezout coverage are **not checked**.
No Lean verification is claimed.

The standard resultant formula and finite-field root test are imported
from the saved assessment's Milne Proposition 4.35(b) and finite-field
discussion on printed p. 53. Volkovich's Lemmas 23–24 support the
already covered squarefree/perfect-power tests, not existence of a
constrained moment pencil. The triangular comparison is an implementation
of the supplied-polynomial test, and (5) specializes L010's recurrence.
This step reproduces and audits the local equality criterion with known
algebraic ingredients; it makes no progress claim beyond the checked
literature and no identification with the unread July ABF26 event.
