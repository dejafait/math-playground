# Lemma 967: complete Li/theta transfers and a boundary-spreading obstruction

## Hypotheses

Use the actual functions A,K of L019 and the entire functions H_r(x,u)
and integrals I_r(x) of L966. Thus K=2A''-A/2, A'(0)=-1/4, and
A,K are strictly positive on [0,infinity), with the superexponential
decay stated there. Fix n in {2,3}, and use exactly L966's parameters

    b=1/4, h=64*9^n, Delta=h-b, q=sqrt(h)=8*3^n.

In particular (h,q)=(5184,72) or (46656,216). Let Q_eta(n) and d_k
have exactly L966's definitions, including algebraic squares, actual
paired nodes and all multiplicities. Set

    a_r=integral_0^infinity A(u)H_r(b,u)du,
    c_r=integral_0^infinity A(u)H_r(h,u)du,
    kappa=1/(2a_0)>0,      M_n=Q_eta(n) I_0(b)^n I_0(h).       (1)

All these integrals used below are finite. No RH, positive Stieltjes
measure, sign of Q_eta, or negative Li margin is assumed.

For m factors define the normalized full symmetrization

    Sym_m(f_1,...,f_m)(u_1,...,u_m)
        =1/m! sum_sigma product_i f_i(u_(sigma(i))).           (2)

Repeated factors are included with their multiplicities in this average.

## Conclusion

The complete n=2,3 numerators have the symmetrized formulas (5)-(6)
below. Coordinatewise integration by parts gives the full face identity
(9) and the explicit tables (11)-(12), including every intersection,
the even-block terms and the distant h subtraction.

Consider the following single boundary-compensation rule: replace each
origin mass 1/2 by the positive density

    kappa A(u)H_0(b,u)du,     whose total mass is 1/2.          (3)

After this replacement the complete face sum is one integral
M_n=integral A^(tensor(n+1)) Psi_n. Here Psi_n is explicitly (14).
The replacement preserves the value of the integral exactly, but its
fully symmetrized kernel satisfies

    lim_(t->infinity) Psi_n(t,0,...,0)/(t exp(qt))
        =-d_1 kappa^n Delta/(2q(n+1)) < 0,    n=2,3.          (4)

Consequently Psi_n is strictly negative on a nonempty open subset
of the positive orthant, of positive A^(tensor(n+1)) measure, at
both test orders. This rule cannot prove L966(16) by pointwise
nonnegativity. No negative value of the whole integral is established.
The all-n inequality, sufficient eta coverage, mixed positivity and RH
remain open. Written in step168 and independently conceptually audited
in step170 on 10 November 2026; no statement or formula correction
was required.

## Proof

### The complete original symmetrized numerators

For this subsection only, write f_r(u)=H_r(b,u), g_r(u)=H_r(h,u).
L966(2) specializes to

    n=2: D=(1,4),   d_1=4h^2/Delta^2, d_2=h/Delta;
    n=3: D=(1,6,9), d_1=h(3Delta+1)^2/Delta^3,
                    d_2=h(6Delta+1)/Delta^2, d_3=h/Delta.

Indeed P_2(z)=2 and P_3(z)=3-z/4, so L966(5) gives B_2(t)=4t
and B_3(t)=9t^2-(3/2)t+1/16. Substitute t=-1/4+y and use L966(6)-(7).
All displayed d_k are strictly positive.

The full numerators before transfer are M_n=integral K^(tensor(n+1)) Phi_n,
where

    Phi_2 = d_1 Sym_3(f_1,f_0,g_0)
             +d_2 Sym_3(f_2,f_0,g_0)
             -d_2 Sym_3(f_1,f_1,g_0)
             -d_1 Sym_3(f_0,f_0,g_1),                         (5)

and

    Phi_3 = d_1 Sym_4(f_1,f_0,f_0,g_0)
             +d_2 Sym_4(f_2,f_0,f_0,g_0)
             -d_2 Sym_4(f_1,f_1,f_0,g_0)
             +(d_3/2) Sym_4(f_3,f_0,f_0,g_0)
             -(3d_3/2) Sym_4(f_2,f_1,f_0,g_0)
             +d_3 Sym_4(f_1,f_1,f_1,g_0)
             -d_1 Sym_4(f_0,f_0,f_0,g_1).                    (6)

To check every coefficient without assuming a sign, L966(12) gives
the first three derivatives of log F as F'/F,
F''/F-(F'/F)^2, and F'''/F-3F''F'/F^2+2(F'/F)^3.
Multiplying by F(b)^n F(h) gives (5)-(6), with the third expression
multiplied by d_3/2. These exhaust the Bell partitions at n=2,3.
The factors in each summand are integrable in absolute value by L966.
Permuting independent coordinates preserves a product integral, so
full symmetrization changes no coefficient or integral.

### Single-coordinate transfer and every face

Import the ordinary integration-by-parts rule
[NIST DLMF 1.4.16](https://dlmf.nist.gov/1.4.E16), with improper
endpoint limits as in [1.4.22-23](https://dlmf.nist.gov/1.4.v),
version 1.2.8 inspected in the prior source assessment. This is a
calculus input, not a sign theorem. The following endpoint and tensor
specialization is necessary to test this particular signed numerator;
the representation of L966 is not reproved.

Let D_u=2 partial_u^2-1/2. From partial_u^2 H_0=xH_0 and the entire
series in L966, commuting the finite x and u derivatives gives

    D_u H_r(x,u)=2(x-b)H_r(x,u)+2rH_(r-1)(x,u),
    H_r(x,0)=delta_(r,0),    partial_u H_r(x,0)=0.             (7)

For r=0 the last H term is absent. One may alternatively differentiate
the identity partial_u^2 H_0=xH_0 r times in x; the product rule gives
exactly rH_(r-1). Every H_r is even in u. At fixed positive x, each
H_r and its needed u derivatives is a polynomial in u times a linear
combination of exp(sqrt(x)u) and exp(-sqrt(x)u), with constant
coefficients. This follows by finite differentiation of cosh(sqrt(x)u).

For any such factor f, twice applying the cited rule on [0,R] gives

    integral_0^R K f
      =[2A'f-2Af']_0^R + integral_0^R A D_u f.

The boundary at R tends to zero: L019 bounds A,A' by a constant
times exp(9u/2-pi exp(2u)), which dominates any fixed polynomial
times exp(q u). At zero the displayed bracket contributes
-2A'(0)f(0)+2A(0)f'(0)=f(0)/2, since f'(0)=0. Thus

    I_r(x)=delta_(r,0)/2
             +2(x-b) integral A H_r(x)
             +2r integral A H_(r-1)(x).                    (8)

In particular I_0(b)=1/2, I_r(b)=2r a_(r-1) for r>=1,
I_0(h)=1/2+2Delta c_0, and I_1(h)=2c_0+2Delta c_1.
The nonzero origin derivative of A has been retained.

Put m=n+1. For each subset S of {1,...,m}, regard its coordinates as
live and fix all coordinates in its complement at zero. Repeating the
single-coordinate rule gives exactly

    M_n=sum_(S subset {1,...,m}) 2^(-m+|S|)
          integral_(0,infinity)^S product_(i in S) A(u_i)
            [ (product_(i in S) D_(u_i)) Phi_n(u) ]_(u_(S^c)=0) du_S.
                                                                  (9)

For S empty the integral means evaluation at the all-origin point.
No normal-derivative terms have been suppressed: all factors in
(5)-(6) are even in every coordinate, and each D_(u_i) preserves
evenness. Normal derivatives therefore vanish on every origin face,
including after other coordinates have been transferred or evaluated.
There are 8 subsets for n=2 and 16 for n=3.

All operations in (9) are justified on finite boxes first. Every
transformed summand, every face restriction and every term needed for
a boundary limit is bounded in its live variables by a product of
fixed polynomial-exponential factors. Multiplication by the appropriate
A or K factors gives an integrable product by L019. Absolute Fubini
and dominated limits therefore apply to each finite summand and to
the finite sum. The same bounds show that faces at infinity vanish,
including their intersections. Constants depend on the fixed h and
derivative order; no uniform-in-n estimate or limiting interchange in
n is claimed. Also a_0>0 because A and H_0(b) are positive.

For clarity the face integrals can be evaluated in terms of (1).
Before expanding by face dimension, the whole sums are

    M_2=(1/2+2Delta c_0)
             [d_1 a_0+2d_2 a_1-4d_2 a_0^2]
             -(d_1/4)[2c_0+2Delta c_1],
    M_3=(1/2+2Delta c_0)
             [(d_1/2)a_0+d_2 a_1-2d_2 a_0^2
                 +(3d_3/4)a_2-6d_3 a_0 a_1+8d_3 a_0^3]
             -(d_1/8)[2c_0+2Delta c_1].                    (10)

Let T_(n,j) be the sum of all terms of (9) with |S|=j, including
their factors 2^(-m+j). The complete n=2 table is

    T_(2,0)=0,
    T_(2,1)=(d_1/2)a_0+d_2 a_1-(d_1/2)c_0-(d_1 Delta/2)c_1,
    T_(2,2)=2Delta d_1 c_0 a_0+4Delta d_2 c_0 a_1-2d_2 a_0^2,
    T_(2,3)=-8Delta d_2 c_0 a_0^2.                          (11)

The complete n=3 table is

    T_(3,0)=0,
    T_(3,1)=(d_1/4)a_0+(d_2/2)a_1+(3d_3/8)a_2
                 -(d_1/4)c_0-(d_1 Delta/4)c_1,
    T_(3,2)=Delta d_1 c_0 a_0+2Delta d_2 c_0 a_1
                 +(3Delta d_3/2)c_0 a_2-d_2 a_0^2-3d_3 a_0 a_1,
    T_(3,3)=-4Delta d_2 c_0 a_0^2-12Delta d_3 c_0 a_0 a_1
                 +4d_3 a_0^3,
    T_(3,4)=16Delta d_3 c_0 a_0^3.                          (12)

These follow by expanding (10); the degree in moment integrals is
exactly the number of live coordinates. More explicitly, a b factor
of derivative order zero has only its 1/2 origin contribution, and
a b factor of positive order has only its 2r a_(r-1) live contribution.
An h zero-order factor contributes either 1/2 or 2Delta c_0; its
first-derivative factor has only 2c_0+2Delta c_1. This enumerates
every summand in (9), including intersections. As Phi_n is symmetric,
each individual S of size j has the same integral T_(n,j)/binom(n+1,j).
In particular the n=2 full interior is strictly negative, whereas
the n=3 full interior is positive. Neither observation signs M_n.

### One common compensation rule, with an exact negative tail

The natural reference profile A(u)H_0(b,u) is positive and integrable.
Spreading each 1/2 boundary contribution as (3) replaces the factors
under the common A du measure by

    B_0(u)=kappa H_0(b,u),
    B_r(u)=2r H_(r-1)(b,u)           (r>=1),
    C_0(u)=kappa H_0(b,u)+2Delta H_0(h,u),
    C_1(u)=2H_0(h,u)+2Delta H_1(h,u).                         (13)

Their integrals against A are exactly I_r(b), I_0(h), I_1(h),
respectively, by (8) and kappa a_0=1/2. Apply this replacement to
each tensor in the entire face expansion (9). The result is

    Psi_2 = expression (5) with every f_r replaced by B_r
                                  and every g_r replaced by C_r;
    Psi_3 = expression (6) with the same replacements;
    M_n=integral_(0,infinity)^(n+1) product_i A(u_i) Psi_n(u)du. (14)

This is a specific cross-face regrouping: every face atom, including
the h zero-order atom and all intersection atoms, has its mass restored
on the common orthant. It is not a discarding of negative faces.
Equations (5)-(6),(13) specify its full kernel without unknown zero data.
The products are absolutely integrable by the bounds already given.

To test its pointwise sign, separate the distinguished h coordinate.
Define symmetric b-coordinate kernels

    W_2=d_1 Sym_2(B_1,B_0)+d_2 Sym_2(B_2,B_0)-d_2 B_1 B_1,
    W_3=d_1 Sym_3(B_1,B_0,B_0)+d_2 Sym_3(B_2,B_0,B_0)
          -d_2 Sym_3(B_1,B_1,B_0)+(d_3/2)Sym_3(B_3,B_0,B_0)
          -(3d_3/2)Sym_3(B_2,B_1,B_0)+d_3 B_1 B_1 B_1.     (15)

In products without Sym, the listed factors are evaluated in different
coordinates. Full symmetrization is equivalently

    Psi_n(u)=1/(n+1) sum_(j=1)^(n+1)
       [C_0(u_j)W_n(u with coordinate j removed)
                   -d_1 C_1(u_j) product_(i!=j) B_0(u_i)].  (16)

This follows by partitioning the (n+1)! permutations according to the
location of the h factor; the remaining n! permutations give W_n.

At zero, B_0(0)=kappa, B_1(0)=2 and B_2(0)=B_3(0)=0, so

    W_2(0,0)=2kappa d_1-4d_2,
    W_3(0,0,0)=2kappa^2 d_1-4kappa d_2+8d_3.                (17)

These are finite constants; no sign is assumed. The exact expressions
needed on the ray are

    H_0(b,t)=cosh(t/2),
    H_1(b,t)=t sinh(t/2),
    H_2(b,t)=t^2 cosh(t/2)-2t sinh(t/2),
    C_0(t)=kappa cosh(t/2)+2Delta cosh(qt),
    C_1(t)=2cosh(qt)+(Delta t/q)sinh(qt).                    (18)

Since q>1/2, they imply

    C_0(t)/(t exp(qt))->0,
    C_1(t)/(t exp(qt))->Delta/(2q),
    B_r(t)=O((1+t^2)exp(t/2)) for 0<=r<=3.                 (19)

Here (19) is an elementary exact exponential limit, not a numerical
preview. For example sinh(qt)/exp(qt)=(1-exp(-2qt))/2.

Evaluate (16) at (t,0,...,0). The summand placing h at t is

    [C_0(t)W_n(0,...,0)-d_1 C_1(t)kappa^n]/(n+1).          (20)

Every other summand places h at zero and exactly one b factor at t.
All its other factors are finite constants, so its absolute value
is O((1+t^2)exp(t/2)) by (18). Dividing by t exp(qt) makes each
such term tend to zero. Equations (19)-(20) prove exactly (4).
In particular the signed, fully retained h derivative defeats the
proposed payment at both orders regardless of the value of a_0>0.
For reference the exact leading coefficients are

    n=2: -(995328/20735) kappa^2,
    n=3: -(8463359955483/34828144129) kappa^3.                (21)

The strict negative limit yields a finite T such that the ray value
is negative for every t>T. For any such t, continuity of the finite
kernel permits replacing its zero coordinates by sufficiently small
positive coordinates while preserving strict negativity. An open box
about that positive point is still negative. The density product A
is continuous and strictly positive there, giving positive measure.
The tail weight can be extremely small: no estimate or sign of its
integral relative to the rest of the orthant has been inferred.

### Verification, decision and qualifications

Run `python3 scripts/li-theta/tensor-boundary-check-168.py`.
The exact-fraction certificate is
`scripts/li-theta/tensor-boundary-check-168.json`. It obtains d_k from
the general L966 sums, generates the complete tensors from all Bell
partitions, and checks them against (5)-(6). It then enumerates all
8+16 labeled subsets and every symmetrization permutation, recording
every face polynomial and verifying (11)-(12) and their multiplicities.
It also checks (7) and all origin values/normal derivatives through
the required orders using exponential-polynomial differentiation.
Finally it records the complete ray exponential polynomials and their
leading coefficients, independently summing all tensor placements.
Every algebraic residual is exactly zero; the leading coefficient is
strictly negative for every kappa>0 at both orders. The full stratum
checks and both full ray polynomials were inspected in step168.

These exact finite checks supplement the explicit proof. They do not
verify a theta integral numerically, certify an all-n statement, or
constitute an independent audit of this new lemma.

The downstream motivation was a possible certificate for the actual
comparison in L966(16), hence potentially a later supplied-margin
argument of L964. The tested reference-profile payment fails its
necessary pointwise test already at both bounded orders. Retire this
specific rule. Repeating its transfer algebra or dropping the h term
cannot repair it. An integrated comparison or a different payment
mechanism is a separate target requiring its own source assessment.

L242's signed logarithmic-derivative kernel and L044/L046's generic
positivity obstructions are comparisons, not premises of this proof.
The historical D_(r,r-1) source stop is neither reopened nor enlarged
into a ban on other actual-theta methods. The new local information is
the exact failure of this explicit compensation rule for the complete
regularized numerator. The bounded sources did not supply that rule
or this obstruction; this is not a claim of originality or a new sign
of Xi. In particular the actual integrated inequality remains unpaid,
and the prescribed eta(n) is still distinct from L964's
supplied-margin-dependent choice. No cross-notebook input is used.

### Independent conceptual audit, step170

The audit accepts (1)-(21) under the stated hypotheses, using the
unchanged SPECIALIZE source coverage. Its mathematical inputs are
exactly L019 and L966. L966's audited actual-node formula is retained
with all multiplicities and algebraic squares; it is not replaced by
an ordinate formula, a modulus square, or a positive Stieltjes measure.
No correction or additional external sign theorem was needed.

For an independent numerator reconstruction, put

    Y(z)=sum_(r=1)^n (I_r(b)/I_0(b)) z^r/r!.

Through degree n, log(1+Y)=sum_(ell=1)^n (-1)^(ell-1)Y^ell/ell.
L966(12) weights its degree-k coefficient by k*d_k. Multiplication
by I_0(b)^n I_0(h) gives exactly (5)-(6), followed by the separate
-d_1 I_1(h)I_0(b)^n term. In particular the third-order coefficients
are d_3/2, -3d_3/2 and d_3, with no missing factorial. Independently
expanding B_n(-b+y)/(Delta+y) by polynomial division recovers each
d_k and D=(1,4),(1,6,9). This checks the complete original numerator
before any compensation or sign argument.

For the transfer, [2A'f-2Af']_0^R has lower-end contribution
-2A'(0)f(0)+2A(0)f'(0)=f(0)/2 for the even factors at issue.
The sign of this contribution is positive. At b the zeroth-order
live factor vanishes; at h the zeroth-order factor has both its
origin mass and 2Delta H_0(h) live part. The h first derivative has
no origin mass and has the entire live part 2H_0(h)+2Delta H_1(h).
It therefore contributes to the one-dimensional stratum as well as
remaining fully present in the compensated kernel.

For every fixed factor and its needed derivatives, L019 supplies a
bound C(1+u^d) exp((9/2+q)u-pi exp(2u)) after multiplication by A,
A' or K, with finite C,d. It is bounded near zero, integrable at
infinity, and tends to zero there. A product of these bounds controls
each finite-box integral, boundary term and face restriction. Thus
absolute Fubini and dominated convergence justify successive limits
and every intersection of infinity faces. Evenness survives each
other-coordinate transfer/evaluation, so all origin normal-derivative
terms vanish also at intersections. No uniformity as n grows is used.

To check the origin strata independently, substitute (8) into the
reconstructed numerator and grade the resulting polynomial by total
degree in (a_0,a_1,a_2,c_0,c_1). Each moment comes from exactly one
live coordinate, and each constant 1/2 from exactly one origin
coordinate. Degree j therefore gives the complete T_(n,j), including
all intersections. Symmetry of Phi_n and the identical coordinate
measures imply that every labeled j-face has integral
T_(n,j)/binom(n+1,j). This gives all 8+16 faces, not only their sum;
their polynomials agree with (11)-(12). In particular the opposite
signs of the two full interiors have not been used to sign M_n.

The mass restoration in (13)-(14) is exact coordinate by coordinate:
integral A B_r=I_r(b), integral A C_s=I_s(h) for s=0,1.
Here integral A kappa H_0(b)=1/2, with 0<a_0<infinity. Expanding
the products of these equalities recovers every origin/intersection
term of (9), including the h-origin contribution. Absolute convergence
was already checked, so it also licenses the equality of whole
integrals. This is a signed tensor identity; no inequality is hidden
in spreading the atoms.

For the asymptotic audit let W_n^*(t)=W_n(t,0,...,0) and
W_n^0=W_n(0,...,0). Formula (16) gives the complete ray, with all
symmetrization multiplicities, as

    (n+1) Psi_n(t,0,...,0)
       = C_0(t)W_n^0-d_1 C_1(t)kappa^n
         +n C_0(0)W_n^*(t)
         -n d_1 C_1(0)B_0(t)kappa^(n-1).

For a symmetric n-fold product with e_r copies of B_r, its ray slice
is sum_r (e_r/n) B_r(t) product_s B_s(0)^(e_s-delta_(r,s)),
where only e_r>0 terms are included. This provides a second way to
compute the full ray without listing symmetrization permutations.
It also shows directly that the last two displayed terms are
O((1+t^2)exp(t/2)). The first term divided by t exp(qt) tends to
zero, and the second tends to -d_1 kappa^n Delta/(2q). Thus (4)
and both rational constants in (21) hold for the actual fixed positive
kappa, without needing an estimate of a_0 or a uniform onset in kappa.
Continuity and strict positivity of A then give the claimed positive-
measure negative open set. They supply no comparison of its integral
with the complementary positive region.

Run `python3 scripts/li-theta/tensor-boundary-audit-170.py`. It imports
no code from the construction script, reconstructs the numerator by
the formal logarithm above, reconstructs H_r by repeated application
of (1/(2q))partial_q to cosh(qt), and checks the full ray by the slice
formula. Its full certificate is
`scripts/li-theta/tensor-boundary-audit-170.json`. All 77 exact checks
passed, including every one of the 24 saved faces, every stratum,
origin/operator identities and both complete ray polynomials. Every
residual is zero; the two leading coefficients are exactly (21),
strictly negative instead of the nonnegative kernel required by the
payment rule. The entire relevant residual lists, both full rays and
all reconstructed strata were inspected, not only their previews.
These finite checks supplement the analytic argument above. The
original step168 script and certificate remain unchanged.

The local advance is independent validation of the previously
unaudited obstruction, not a new mathematical discovery or an
integrated sign result. Retire only this normalized-profile pointwise
rule. L966(16), all-n closure and the sufficiency of the prescribed
eta(n) remain unresolved; L964's supplied-margin choice is not an
automatic substitute. No new direct dependency is introduced.

## Mathlib

Full matching coverage has not been checked and is unknown. No
Mathlib theorem is imported for the tensor specialization, the face
coefficients or the signed ray limit. General integration-by-parts,
finite-sum and exponential-limit support would not by itself sign
the integrated comparison. Reference portal:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
