# Corollary 466i: frozen determinant Hessian has two zero Volterra balances

## Hypotheses

Use C466a's actual real density p=theta_1, smooth on R, zero on
(-infinity,0], positive on (0,infinity), with every derivative zero at
zero. Retain its normalization c_0=xi(1/2)>0 and its external
zero-counting, strip/symmetry and verified-zero qualifications. Use
C466b's actual H in C^1(0,infinity), H>0, H'<0, integral H finite,
and its imported scalar law x p=H*p. In particular no higher PF
property, complete monotonicity of H, or RH is assumed.

For finite m>=3 set n=m-2, e_k=(-1)^(k(k-1)/2),
A_k(y)=[p^(i+j)(y)]_(0<=i,j<k), D_k(y)=e_k det A_k(y).
Assume a hypothetical x_*>0 with

    D_j(x_*)>0 (1<=j<=n), D_(n+1)(x_*)=D_(n+2)(x_*)=0,
    rank A_(n+2)(x_*)=n.

Write A(y)=A_(n+2)(y), A_*=A(x_*), B=A_n(x_*).
The rank condition is explicit; adjacent zero leading determinants
alone are not substituted for it. For first-contact interpretation
additionally retain D_(n+1)>0 and D_(n+2)>0 immediately to the left.
No contact is asserted to exist.

Use the polynomial bilinear Frechet differential of det, with
d^2det_A[X,Y] the coefficient of st in det(A+sX+tY).
The sole observable tested is

    W(t)=d^2det_(A_*)[A_*',A(x_*-t)], 0<=t<=x_*.

## Conclusion

There is a real monic degree-n polynomial P such that both coefficient
vectors P and zP, in the ordered basis 1,z,...,z^(n+1), lie in ker A_*.
Freeze this P and put

    a(y)=P(partial_y)^2 p(y), kappa=a'''(x_*).

Then

    a(x_*)=a'(x_*)=a''(x_*)=0,
    W(t)=det(B) kappa a(x_*-t),                         (1)
    W(t)=-det(B) kappa^2 t^3/6+O(t^4) as t downarrow0. (2)

W and every derivative vanish at t=x_*. W is identically zero if and
only if kappa=0; thus kappa!=0 is an exact additional finite-jet
condition for nonvanishing, not established here for actual p.

The endpoint-controlled balances are

    integral_0^x_* H(t)W(t)dt=0,
    integral_0^x_* (-H'(t))W(t)dt=0.                  (3)

Both are absolutely convergent. Also D_m'(x_*)=D_m''(x_*)=0.
If kappa!=0, the parity-adjusted weight U=e_m W obeys

    U(t)=D_n(x_*) kappa^2 t^3/6+O(t^4)>0
                                               for small t>0, (4)

but takes negative values farther inside (0,x_*); both positive
kernels in (3) pair with it to zero. Subtracting any constant q
times the first balance from the second still gives zero.

Under the first-contact hypothesis, (-1)^n kappa<=0; if kappa!=0
the inequality is strict. This endpoint direction does not change (3).
The chosen weight therefore supplies neither nonzero curvature forcing
nor a strict signed Volterra balance, even after assuming its precise
nonvanishing condition. This stops this weight, not all simultaneous-
contact mechanisms or RH. Rank-one forcing, actual contact existence,
global propagation and L030-L032/C032a transfer remain open.

This conditional obstruction was derived in step917 and passed the
separate conceptual audit919 below without a change of hypotheses or
conclusions. It specializes known determinant/convolution tools; the
audit validates the local result and claims no certified novelty.

## Proof

### Kernel polynomials and the allowed singular reduction

Let ell_y(z^j)=p^(j)(y), extending linearly to real polynomials.
This is an algebraic functional, not an asserted positive measure.
B is invertible because det B=e_n D_n(x_*)!=0.
Solve the n equations ell_(x_*)(z^i P)=0, 0<=i<n, for the lower
coefficients of the monic degree-n P. The first n rows of A_* are
independent, since their first n columns form B. They span its entire
row space by rank A_*=n. Thus the coefficient vector P lies in ker A_*,
giving ell_(x_*)(z^j P)=0 for 0<=j<=n+1.

The first n rows also annihilate zP: the needed indices j+1 run from
1 through n. The same row-space argument puts zP in ker A_*, and its
last row adds ell_(x_*)(z^(n+2)P)=0. Consequently

    ell_(x_*)(z^j P)=0, 0<=j<=n+2.                    (5)

The two kernel vectors are independent, by their different monic
degrees, and hence form a basis of the kernel.

Let T have columns 1,z,...,z^(n-1),P,zP in the original coefficient
basis. This is upper triangular with diagonal entries one. In this
fixed basis T^T A_* T=diag(B,0_2). For any real matrix direction X put
Xbar=K^T X K, where K consists of the last two columns P,zP of T.

The singular determinant differential is imported from Rajendra Bhatia
and Tanvi Jain, *Higher order derivatives and perturbation bounds for
determinants*, Linear Algebra Appl.431 (2009),2102-2108,
[DOI](https://doi.org/10.1016/j.laa.2009.07.003),
[authors' May18 2009 manuscript isid/ms/2009/05](https://www.academia.edu/7491948/Higher_order_derivatives_and_perturbation_bounds_for_determinants),
definition(5), Theorems2/3, formulas(8)/(13), Section2 coefficient/Laplace
proofs. These apply to arbitrary square matrices, including singular
ones. The following is its needed block specialization, not a new
general differentiation theorem:

    d^2det_(A_*)[X,Y]
      =det(B)(Xbar_11 Ybar_22+Xbar_22 Ybar_11
              -Xbar_12 Ybar_21-Xbar_21 Ybar_12).        (6)

To verify the specialization and its factor, det T=1 preserves
det(A_*+sX+tY). Apply Jean Gallier, *The Schur Complement and Symmetric
Positive Semidefinite (and Definite) Matrices*, August24 2019,
[Section1, printed p2](https://www.cis.upenn.edu/~jean/schur-comp.pdf),
to its invertible leading n block for sufficiently small s,t.
The complementary block is sXbar+tYbar plus terms of total order
at least two. Its determinant to order two is det(sXbar+tYbar);
the leading determinant contributes det B. The coefficient of st is
exactly (6). This uses only B^(-1), never a size-(m-1) inverse.
No positive-semidefinite sign assertion is imported.

Since differentiation of ell_y multiplies its argument by z, (5)
implies ell_(x_*)(z^r P^2)=0 for r=0,1,2. Indeed expand one copy
P=sum_(j=0)^n p_j z^j; all indices j+r are at most n+2.
This proves the three vanishings of a in (1), and

    K^T A_*' K = [[a'(x_*),a''(x_*)],
                 [a''(x_*),a'''(x_*)]] = [[0,0],[0,kappa]].

For A(y) the corresponding compression is
[[a(y),a'(y)],[a'(y),a''(y)]]. Substitution into (6) proves (1).
Taylor expansion gives (2); smoothness suffices, without analyticity
or an assumed finite contact order. Also e_m det B=-D_n(x_*), since
e_(n+2)/e_n=-1, proving (4).

### Exact contractions and both endpoints

Define the frozen linear functional F(X)=d^2det_(A_*)[A_*',X].
C466b's localization proof differentiates only the smooth p factor
against integrable H and gives, at x=x_*,

    integral H(t)A(x_*-t)dt=x_* A_*+L A_*+A_* L^T,
    integral H(t)A'(x_*-t)dt=x_* A_*'+N A_*+A_* N+A_*,

where L_(i,i-1)=i and N=diag(0,...,m-1). These entrywise identities
do not use C466b's rank-one contact assumption; they hold for any
finite m under its scalar-law and smooth-flatness hypotheses.
Finite matrix contractions commute with these absolutely convergent
integrals because all p derivatives on [0,x_*] are bounded.

Since A_* K=0 and K^T A_*=0, each term with A_* on the left or
right has zero compression by K. Equation (6) makes F of each such
term zero. Moreover F(A_*')=0 because its compression has zero
first row and column. Hence integral H W=0 and, using
W'(t)=-F(A'(x_*-t)), integral H W'=0.

At t=0, (2) gives W=O(t^3), in particular O(t). At t=x_*,
flatness of every p derivative gives W and all derivatives zero.
Positive decreasing integrable H satisfies tH(t)->0 and

    integral_0^x_* t(-H'(t))dt
       =integral_0^x_* H(t)dt-x_*H(x_*)<infinity.

For completeness, tH(t)<=integral_0^t H proves the limit; integrate
t(-H') on [eta,x_*] and let eta downarrow0 to obtain the identity.
Thus (-H')W is absolutely integrable and H(t)W(t)->0 at zero.
The other boundary term is H(x_*)W(x_*)=0. Integration by parts on
[eta,x_*], followed by the limit, gives integral H W'
=integral (-H')W=0. No derivative of H beyond H' is used.
This proves all convergence and endpoint assertions in (3).

All size-(m-1) minors of A_* vanish by rank m-2, so ddet_(A_*)=0.
The ordinary chain rule gives (det A)'=0 at x_* and
(det A)''=d^2det_(A_*)[A_*',A_*']+ddet_(A_*)[A_*'']=0.
This also checks that the contracted zero is the actual zero curvature,
not an omitted derivative of a moving coefficient.

### Nonvanishing criterion and first-contact direction

If kappa=0, (1) gives W=0 identically. If kappa!=0 and W were
identically zero, the real monic constant-coefficient operator
P(partial)^2 of order 2n would annihilate p on (0,x_*).
All its initial data of orders 0 through 2n-1 vanish at zero.
Writing the equation as Y'=M Y with Y=(p,...,p^(2n-1)) gives
Y(0)=0. On any [0,b] with b<x_*, iterating its integral equation
bounds ||Y(t)|| by sup_[0,b]||Y|| (||M||b)^r/r! for every r.
Letting r tend to infinity gives Y=0, contrary to p>0.
This is the same finite-order ODE uniqueness argument paid in C466b,
applied to this degree-n operator. Thus kappa!=0 is sufficient as
well as necessary. Since H>0 and W is continuous, the first zero
balance then forces both signs on open subintervals. Formula (4)
locates the positive sign of U near zero. The same two-sign
conclusion is consistent with the second positive kernel -H'.

To keep the first-contact information, apply the fixed basis
1,z,...,z^(n-1),P to A_(n+1)(y). Its blocks are B(y)=A_n(y),
r_i(y)=ell_y(z^i P) (0<=i<n), and a(y).
At y=x_*, (5) gives r=0 and r'=0, so r(y)=O((y-x_*)^2).
B(y) is invertible near x_*. The Schur determinant therefore gives,
with h=y-x_*,

    D_(n+1)(x_*+h)
      =(-1)^n D_n(x_*) kappa h^3/6+O(h^4).

Here the Schur correction r^T B(y)^(-1)r is O(h^4), and the
variation of det B(y) changes the cubic term only by O(h^4).
If kappa!=0, positivity for all sufficiently small negative h forces
(-1)^n kappa<0. For kappa=0 the stated weak inequality is automatic.
Positivity of D_m immediately left is retained but not needed to
obtain the identities; it is not replaced by a strict second derivative
at the contact, which has just been proved zero.

Thus even a nonzero W has two exactly zero positive-kernel pairings.
A local sign near one endpoint, or scalar domination of H or -H',
cannot supply the sought strict balance. No generic jet example has
been substituted for an actual-density contact. ∎

### Separate conceptual audit, 14 November 2026, step919

The approved audit checked the complete proof above against C466a's
actual-density hypotheses and C466b's scalar-law localization. Every
claim survives; no mathematical repair or extra hypothesis is needed.
The determinant and Schur inputs are the precisely cited sources above,
as compared in assessment917/completion918 and comparison915. This
checks their specialization, not a new proof of those general theorems
or an independent audit of the external zero/counting certificates.

**Kernel indices.** Solving the leading n equations gives a vector with
coordinates (p_0,...,p_(n-1),1,0). Rank n and the invertible leading B
make these n rows a basis of the row space, so all m rows annihilate it.
For zP, the top-row indices are i+1=1,...,n, already among the vanishing
indices 0,...,n+1. Applying the row-space argument again adds n+2.
The vectors' last two coordinates (1,0) and (p_(n-1),1) prove independence
and det T=1 even when p_(n-1)=0. Expanding one copy of P in z^r P^2
uses only j+r<=n+2 for r<=2. The compression of A_*' therefore has
exactly the form diag(0,kappa); no positivity of ell is used.

**Mixed coefficient and normalization.** In the T basis the off-diagonal
Schur correction is quadratic in s,t; its contribution to a size-two
determinant with zero constant term is of total degree at least three.
Only det B times det(sXbar+tYbar) contributes to degree two. Expanding
that two-by-two determinant gives exactly the four terms of (6).
When X=Y, its st coefficient is twice det(Xbar), as the definition of
the bilinear second differential requires; with X=A_*' only
kappa Ybar_11 remains. Thus no factor two is missing from (1).
Since (n+2)(n+1)/2-n(n-1)/2=2n+1, e_m det B=-D_n.
The three vanishings of a and its cubic Taylor term give (2) and (4).
Only finitely many derivatives of smooth p, through order 2n+4 for
these Taylor remainders, are required.

**Contractions without the rank-one premise.** At entry (i,j), the
first scalar recurrence has extra coefficient i+j multiplying
p^(i+j-1), with the zero-coefficient case interpreted as zero.
The second has i+j+1 multiplying p^(i+j). These are exactly
LA+AL^T and NA+AN+A. Their derivation precedes C466b's rank-one
adjugate argument and needs none of that argument's rank hypotheses.
For any fixed M, compression of MA_* and A_*M is zero, since A_*K=0
and K^T A_*=0. Also F(A_*')=det B kappa a'(x_*)=0. Applying F to
the two recurrences therefore gives integral H W=0 and integral H W'=0,
with the minus sign W'=-F(A') retained. Rank m-2 kills the first
determinant differential, so the chain rule also gives precisely
D_m'=D_m''=0. Freezing F has not removed a moving term from that rule.

**Improper endpoints.** Bounded p derivatives on [0,x_*] dominate all
H convolutions by a constant times H. The cubic endpoint gives
W=O(t^3), W'=O(t^2). The original proof's tH(t)->0 and finite
integral t(-H') control both the boundary product and the absolute
integral of (-H')W; on the remainder of the finite interval all
functions are continuous. At t=x_*, every derivative of W vanishes
by smooth zero extension of p, and H(x_*) is finite. Thus the limiting
integration by parts has no residual endpoint term and yields the
second equality in (3). This uses only H in C^1 and H'<0, never H''.

**Nonvanishing and first contact.** If kappa=0 then (1) vanishes
identically. If kappa!=0 then the nonzero cubic coefficient in (2)
already proves W is nonzero on every sufficiently short interval to
the right of zero. The separate ODE argument in the original proof is
also valid: P(partial)^2 is monic of order 2n>=2, its coefficients are
constant and all 2n initial data vanish; the stated factorial bound
forces the solution to vanish on each [0,b], contradicting p>0.
This is redundant verification, not an added analyticity premise.
Since U is positive near zero and integral H U=0 with H>0, U must be
negative on an interior open interval. The same convergent zero
balance holds for -H'; no strict signed forcing is left over.

Finally r(x_*)=r'(x_*)=0 makes its Schur correction O(h^4), and
e_(n+1)/e_n=(-1)^n gives the asserted cubic coefficient for D_(n+1).
For h<0 its sign is -sign((-1)^n kappa); positivity on the left
therefore forces (-1)^n kappa<0 when kappa!=0. The case kappa=0
satisfies the weak statement. The extra left positivity of D_m is
retained but is not needed by this argument. Neither a contact nor
nonzero kappa has been constructed. The required strict balance is
still missing: both exact balances are zero. This validates the stop
for this observable, not a new obstruction beyond step917 or a
resolution of the all-degree actual-Xi gap.

## Mathlib

The pre-existing assessment915/916 supplies supporting block algebra:
[Matrix.det_fromBlocks₁₁](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/SchurComplement.html#Matrix.det_fromBlocks%E2%82%81%E2%82%81)
and Matrix.fromBlocks_eq_of_invertible₁₁, with finite real matrices
and invertible top-left B; the complementary block may be singular.
C466b records the previously inspected compact-support convolution
differentiation support and its exact specialization. Full matching
formal coverage of (1)--(6), the nonvanishing equivalence, and this
corank-two obstruction has not been checked. No absence is asserted.

