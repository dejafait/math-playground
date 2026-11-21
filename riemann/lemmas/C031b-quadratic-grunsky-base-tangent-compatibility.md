# Corollary C031b: quadratic Grunsky base-point tangent compatibility

## Hypotheses

Let A,B,C,D,E be finite strictly positive real constants. Use C031a's
five-real-coefficient family

    f_b(z)=z/(1+sum_(j=1)^5 b_j*z^(j+1)),

its symmetric negative mixed-log coefficients c_mn, and its complete
finite defects h_mn=delta_mn/m-sum_(k>=1) k*c_km*c_kn for 1<=m,n<=3.
There is no univalence, pole exclusion or positive-semidefiniteness
assumption. Define the six polynomial residuals in row order
11,12,13,22,23,33 by

    F(b,tau,u,v)=h(b)-tau*(A,u*B,v*C,u^2*C,u*v*D,v^2*E).

The base coefficient vector is b*=(1,0,0,0,0). For the necessary
branch conclusion suppose b(tau)=b*+tau*a+o(tau) as tau decreases to
zero through positive values, u(tau)->u0>0, v(tau)->v0>0, with both
limits finite, and F(b(tau),tau,u(tau),v(tau))=0. A tau-parametrized
C1 branch extending to zero satisfies these hypotheses; differentiability
of the weights is not needed for the necessary conclusion.

For the actual-Xi specialization A,...,E are L025's S2,...,S6, with
positivity from L027 and C030z's fixed1307 outer boxes as recorded in
C031a. Actual inclusion retains the L019,L021,L036,L037,L917 and1307
contracts, including the conditional Decimal arithmetic qualifications.
No new integration or certification of that library is made here.

## Conclusion

At (b*,0,u0,v0), for arbitrary finite real u0,v0, F=0. The derivative
with respect to (b1,...,b5,u,v) has rank exactly five and is

    J=-2*[ 1 0 0 0 0 0 0
           0 1 0 0 0 0 0
           0 0 1 0 0 0 0
           1 0 1 0 0 0 0
           0 1 0 1 0 0 0
           1 0 1 0 1 0 0 ].                         (1)

Its sole row relation is row22=row11+row13. The tau partial column
is -(A,u0*B,v0*C,u0^2*C,u0*v0*D,v0^2*E). Thus including the tau
column gives rank five if C*u0^2=A+C*v0, and rank six otherwise.
No six-by-six dependent-variable derivative selected from the seven
columns in (1) is invertible at this point.

The branch hypotheses necessarily imply

    C*u0^2=A+C*v0.                                  (2)

Conversely, the **first-order tangent system**, not the nonlinear
equations, is compatible for positive finite u0,v0 exactly when (2)
holds. Equivalently choose any u0>sqrt(A/C) and set v0=u0^2-A/C.
For any such pair the unique b tangent is

    a1=-A/2, a2=-u0*B/2, a3=-v0*C/2,
    a4=u0*(B-v0*D)/2,
    a5=(A+v0*C-v0^2*E)/2.                           (3)

For the unchanged actual boxes, the explicit choice

    u0=400, v0=160000-A/C

is finite and strictly positive, because exact rational bounds give

    56064<A/C<56065,
    103935<v0<103936.                               (4)

This passes the approved necessary test for a regular finite-positive-
weight branch. It proves neither existence of that branch nor a
positive-tau root, holomorphic unit-disk realization, univalence,
positivity of the actual block, or RH. Singular/non-C1/fractional-power
branches, weights tending to zero or infinity, larger blocks and
initialization remain unresolved. Rank deficiency alone excludes none
of them and does not exclude the regular branch either.

## Proof

**Imported identities and base evaluation.** C031a's complete-column
identities are the finite specialization of L.-P. Teo, *Analytic
functions and integrable hierarchies—characterization of tau functions*,
Lett. Math. Phys.64(2003),75–92,
[hep-th/0305005v2](https://arxiv.org/html/hep-th/0305005v2),
Sections2.1–2.2, (2.3)–(2.4),(2.8)–(2.12) and the formal-extension
paragraph. Reuse their established finite supports 5,10,15 and exact
defects. No general Faber theorem is reproved; the present calculation
only differentiates this fixed finite polynomial system.

At b*, the three complete columns are respectively delta_(k,1),
delta_(k,2)/2,delta_(k,3)/3. Indeed substituting b1=1 and all other
b's zero in C031a's convolution formulas leaves only those terms:
in the third column the terms at k=1 cancel, and its cubic term is
at k=3. Consequently the complete column products give h_mn=0
for all six entries, proving the claimed base residual.

For a perturbation dot b=a, differentiate the finite sum at the base.
The two nonzero column factors occur at k=m and k=n, so

    dot h_mn=-dot c_nm-dot c_mn=-2*dot c_mn.         (5)

Symmetry also holds along the perturbation. When m=n the same formula
is the derivative of the square; no separate or omitted diagonal term
is needed. C031a's formulas restricted to the selected mixed entries are

    c11=b1, c12=b2, c13=b3,
    c22=b3+b1^2/2, c23=b4+b1*b2,
    c33=b5+b1*b3+b2^2+b1^3/3.

Their derivatives at b* are a1,a2,a3,a3+a1,a4+a2,a5+a3+a1.
Equation(5) therefore gives (1). The weight derivatives vanish because
every weight term of F has a factor tau. Holding b,u,v fixed gives
the stated tau column directly from the definition of F.

The submatrix of (1) in rows11,12,13,23,33 and columns b1,...,b5
has determinant (-2)^5=-32, by subtracting earlier rows in its last
two rows. The displayed row relation gives rank at most five, hence
exactly five and only that one row relation. Adding a tau column
preserves the relation exactly when A+C*v0-C*u0^2=0; otherwise its
product with the left-null vector (-1,0,-1,1,0,0) is nonzero, so
the augmented rank is six. No application of an implicit-function
existence theorem is justified by the unscaled derivative (1).

**Necessary limit and complete tangent compatibility.** Since h is
polynomial and h(b*)=0,

    h(b*+tau*a+o(tau))=tau*J_b*a+o(tau),

where J_b is (1)'s first five columns. The positive finite weight
limits imply convergence of every component of the right-side target
vector. Dividing the assumed equations by tau>0 and taking the limit
therefore gives, with no interchange of an infinite sum,

    -2*a1=A, -2*a2=u0*B, -2*a3=v0*C,
    -2*(a1+a3)=u0^2*C,
    -2*(a2+a4)=u0*v0*D,
    -2*(a1+a3+a5)=v0^2*E.                           (6)

The first three equations force a1,a2,a3 in (3). The fourth then says
exactly (2). The last two force a4,a5 as in (3). Conversely those
five values solve all six equations(6) whenever (2) holds. No division
by a b coefficient, a tangent component or a weight was made. Since
C>0, equation(2) and u0,v0>0 are equivalent to the parametrization
following it. This proves necessity and sufficiency for the linear
tangent system only. It supplies no integration of that tangent to
an exact solution curve. Finite but large weights are allowed; the
statement imposes no small-weight hypothesis.

**Guarded actual specialization.** Use the unchanged outer bounds

    3.7172599285e-5<A<3.7172599286e-5,
    6.6303168020e-10<C<6.6303168031e-10.

Their positive endpoints give the exact enclosing ratio interval

    qlo=3717259928500000/66303168031,
    qhi=185862996430000/3315158401.

Integer comparisons give 56064<qlo<=A/C<=qhi<56065. Thus 400^2
exceeds A/C and v0=160000-A/C is strictly positive. Its rational
enclosing endpoints are

    vlo=344562347730000/3315158401,
    vhi=6891246956460000/66303168031,

which give (4). The definition of v0 uses the actual constants,
not a rational midpoint. Hence (2) is an exact identity for the actual
constants, conditional on their inherited inclusion, rather than a
small interval residual. B,D,E enter only the finite formula(3);
their strictly positive finite input boxes suffice. There is no sweep,
interval refinement or new quadrature. The example u0=sqrt(2A/C),
v0=A/C also shows general finite-positive tangent compatibility for
any strictly positive constants, independently of these actual bounds.

**Verification and intended use.** Reproduce with

    python3 scripts/grunsky/quadratic-tangent-1316.py

The complete [certificate1316](../scripts/grunsky/quadratic-tangent-certificate-1316.json)
stores the full six polynomials, base residuals, exact Jacobian, tau
column, row reduction, nonzero minor, sole row relation, general tangent
residuals, explicit witness with common denominator 2*C^2, all six
cleared witness residuals, exact ratio/weight bounds, guards and hashes.
It reconstructs the columns by C031a's convolutions and checks them
and every full equation against certificate1314; this is exact
polynomial reproduction, not an independent proof of the arithmetic
library. All13 checks pass, with no failures. The complete base,
Jacobian, tangent, witness, bounds and checks were inspected. The
argument above proves the finite linear facts without relying on a
certificate preview.

This is a local specialization and reproduction of classical
differentiation and finite algebra, not a new general theorem or
progress beyond the checked sources' general tools. The first-order
test retains one regular mechanism and rules out only incompatible
limiting weight pairs within the stated differentiable-coefficient
class. A later reviewed nonlinear existence test and independent
whole-disk analytic construction are needed before any Grunsky sign
could transfer to L030's finite block. No direct or indirect premise
of actual Hankel positivity is used.

## Mathlib

Full matching finite Grunsky/actual-Xi/tangent coverage is unchecked.
The reused1315 assessment records supporting implicit-function tools;
none supplies the rank or actual specialization by citation alone.
No Lean verification or absence claim is made. The exact script and
inherited Decimal contracts are not formal certificates in Mathlib.
