# Corollary C031e: an interior conjugate collision on the fixed quadratic branch

## Hypotheses

Use the real C1 branch b(tau) supplied by C031c, with fixed u=400,
b(0)=(1,0,0,0,0), v0=160000-A/C, and b'(0)=a0. Write

    P_tau(z)=1+sum_(j=1)^5 b_j(tau)*z^(j+1),
    f_tau(z)=z/P_tau(z).

Assume A,B,C,D,E lie in the unchanged fixed1307 outer rational boxes
of C030z, respectively

    A in [3.7172599285e-5,3.7172599286e-5],
    B in [1.4417393139e-7,1.4417393141e-7],
    C in [6.6303168020e-10,6.6303168031e-10],
    D in [3.2136641485e-12,3.2136641527e-12],
    E in [1.5876934435e-14,1.5876934595e-14].

All decimals denote exact rationals; closed boxes suffice here.
For the actual-Xi tuple, inclusion retains C030z's L019,L021,L025,
L027,L036,L037,L917/1307 contracts, including its conditional
Decimal arithmetic qualifications. This result does not reverify
the library, quadrature or actual inclusion. C031c's existence and
tangent are inputs, not independently audited here. C031d's
outward-root calculation is not a premise. No RH or all-degree
positivity, disk holomorphy or univalence is assumed.

## Conclusion

For each such fixed tuple there are delta>0 and a real C1 function
r near tau=0, with r(0)=1, such that for every 0<tau<delta the points

    z_+(tau)=r(tau)*exp(i*pi/3),
    z_-(tau)=r(tau)*exp(-i*pi/3)

are distinct nonreal points of |z|<1, both denominators are nonzero,
and f_tau(z_+)=f_tau(z_-) is finite and real. In particular this
branch is not injective on the open disk, even among its finite
values. It cannot provide a holomorphic univalent disk realization
for the finite matching equations. The squared-radius derivative is

    (r^2)'(0)=A+400B+(v0*C)/2-200*v0*D-(v0^2*E)/2
              in (-0.000024,-0.000022).                 (1)

No effective delta or box-uniform interval is asserted. This excludes
only C031c's specified branch for sufficiently small positive tau,
not every solution of C031a, other angles, weights or singular
branches. It gives no Xi mixed-form sign or resolution of RH.

## Proof

**Base points and the scalar equation.** Put w=exp(i*pi/3), so
w=(1+i*sqrt(3))/2, w^2=w-1 and w^3=-1. Since P_0(z)=1+z^2,

    P_0(w)=w, P_0(conj(w))=conj(w),
    |P_0(w)|=|P_0(conj(w))|=1,
    f_0(w)=f_0(conj(w))=1.                            (2)

The base points are distinct and nonreal. This is the finite,
nonexceptional boundary pairing in the Joukowski example: f_0=1/(2J),
J(z)=(z+1/z)/2, with J(w)=1/2. See the Stanford Math270 course
extract, *Chapter1. The Holomorphic Functions*, dated31 March2003,
[printed p32, (3.23)–(3.25)](https://math.stanford.edu/~ryzhik/MATH270-06/shabat-chapter1.pdf).
The exact substitutions (2) verify applicability without including
z=0, J=0 or coincident real endpoints.

Because b is real C1 on an open interval about zero, P_tau(r*w)
and P_tau(r*conj(w)) are C1 in the real variables (tau,r). By (2)
and continuity, there is an open rectangle about (0,1), with r>0,
on which both denominators are nonzero. On that rectangle define

    H(tau,r)=Im(f_tau(r*w))/sqrt(3).

It is a real C1 function and H(0,1)=0. No cleared polynomial
equation is substituted for H, and no possible pole is counted
as a solution.

**Dependent derivative and the first variation.** At (0,1),

    partial_r f_0(r*w)=w*(1-w^2)/(1+w^2)^2
                       =w^(-1)-w=-i*sqrt(3).

Thus H_r(0,1)=-1, the actual scalar dependent derivative required
below, not merely a nonzero complex derivative. Holding r=1 and
using b'(0)=a0=(a1,...,a5), the quotient rule and P_0(w)=w give

    partial_tau f_tau(w)|_0=-sum_(j=1)^5 a_j*w^j,
    H_tau(0,1)=(-a1-a2+a4+a5)/2.                    (3)

Here the imaginary parts of w,w^2,w^3,w^4,w^5, divided by sqrt(3),
are respectively 1/2,1/2,0,-1/2,-1/2. These are finite algebraic
identities with a nonzero denominator, requiring no interchange.

Import the real C1 implicit-function theorem, O. R. B. de Oliveira,
*The Implicit and the Inverse Function Theorems: Easy Proofs*,
Real Anal. Exchange39(1)(2013/2014),207–218,
[arXiv1212.2066v1, Section3 Theorem2](https://arxiv.org/html/1212.2066v1).
The domain is the open rectangle just constructed, the base zero
is (0,1), and the dependent derivative is -1. The theorem gives
a local real C1 graph r(tau) with H(tau,r(tau))=0, r(0)=1 and
r'(0)=-H_tau/H_r=H_tau. Consequently

    (r^2)'(0)=2*r'(0)=-a1-a2+a4+a5.                 (4)

C031c supplies exactly

    a1=-A/2, a2=-200B, a3=-v0*C/2,
    a4=200*(B-v0*D), a5=(A+v0*C-v0^2*E)/2.

Substitution into (4) proves the expression in (1). Only the
existing first tangent is used; no second-order branch data or
motion in the angle is needed.

**Exact sign and its threshold.** Write the rational box endpoints
as A_l,A_h,...,E_l,E_h. Positivity and the definition of v0 give

    v_l=160000-A_h/C_l <= v0 <= 160000-A_l/C_h=v_h,
    103935<v_l<=v_h<103936.

All product factors below are positive. Thus (1)'s expression is
bounded below and above by the following explicit rational numbers:

    L=A_l+400B_l+v_l*C_l/2-200v_h*D_h-v_h^2*E_h/2,
    U=A_h+400B_h+v_h*C_h/2-200v_l*D_l-v_l^2*E_l/2.

Dependence between v0,A,C does not invalidate this outer enclosure.
Exact rational evaluation yields

    L=-511270638434762842611272634477187/
        21980550454735102084805000000000000000,
    U=-5112706164033352348297561245289/
        219805504474417536020000000000000000,
    -3/125000<L<=U<-11/500000<0.

These endpoints establish the required strict inward threshold <0,
not just nonpositivity. Every denominator displayed here is a
positive integer. The complete exact certificate is reproduced by

    python3 scripts/grunsky/conjugate-collision-1322.py

[Certificate1322](../scripts/grunsky/conjugate-collision-certificate-1322.json)
records the algebra in Q(i*sqrt(3)), both base denominator guards,
all five parameter partials, normalized scalar Jacobian, tangent
substitution, unchanged input boxes, product intervals, L,U,
threshold, source hashes and all14 checks, with no failures.
The complete relevant base, derivative, interval and check fields
were inspected; a preview is not being used as evidence. The
formulas above specify the enclosure independently of a decimal
display or an approximate parameter solve.

**Persistence, distinctness and the obstruction.** Differentiability
gives r(tau)^2=1+tau*(r^2)'(0)+o(tau). By the strict sign, this is
less than1 for every sufficiently small positive tau. Shrink the
interval so r(tau)>0 by continuity, and retain the rectangle on
which both denominators are nonzero. The two points then have
modulus r(tau)<1 and imaginary parts +/-sqrt(3)*r(tau)/2!=0,
so are distinct. Since H=0, f_tau(z_+) is real. Real coefficients
give P_tau(conj(z))=conj(P_tau(z)) and therefore, where defined,
f_tau(conj(z))=conj(f_tau(z)). Hence f_tau(z_-)=f_tau(z_+), finite.
Continuity from (2) can also keep this value nonzero near1.

This is the classical typically-real necessary obstruction. The
general result is G. B. Leeman, Jr., *A local estimate for typically
real functions*, Pacific J. Math.52(2)(1974),481–484,
[p481, Definition1 and following observation](https://msp.org/pjm/1974/52-2/pjm-v52-n2-p16-p.pdf):
a normalized analytic univalent real-coefficient disk map is
typically real and cannot map a nonreal interior point to a real
value. The branch is normalized at0 because P_tau(0)=1. If it
were holomorphic and univalent on the disk, the hypotheses of that
necessity statement would hold and the constructed pair would
contradict it. In fact the equal finite values directly contradict
injectivity even without a global pole-exclusion premise.
This verifies the finite specialization of imported tools, rather
than reproving a general univalence or implicit-function theorem.
The obstruction is not an off-line zero certificate or a disproof
of RH. Larger blocks, actual identification, initialization, and
other regular/singular/non-C1/fractional-power/zero/diverging-weight
branches remain open.

**Independent audit1324, 17 November2026.** The conditional statement
above passes its fixed-tuple audit. The C031c branch and tangent are
explicit inputs: this acceptance does not certify that upstream proof
or the actual1307 inclusion/Decimal contracts independently. No C031d
premise or global disk holomorphy is needed. Reused source coverage is
assessment1322; the imported real C1 IFT permits H_r=-1.

For an independent derivative replay, multiply the evaluated quotient
by the conjugate denominator on the same pole-free rectangle. With
w=exp(i*pi/3), z=r*w, define

    N(tau,r)=Im(r*w*conj(P_tau(r*w)))/sqrt(3)
            =r/2-b1(tau)*r^3/2-b2(tau)*r^4/2
                        +b4(tau)*r^6/2+b5(tau)*r^7/2.

Indeed z*conj(z^(j+1))=r^(j+2)*w^(-j); the normalized imaginary
parts of w^(-j) are -1/2,-1/2,0,1/2,1/2. Thus
H=N/|P_tau(r*w)|^2. At the base the denominator squared is1 and
N=0, so differentiating this identity gives H_r=N_r=-1 and
H_tau=N_tau=(-a1-a2+a4+a5)/2. This checks (3)–(4) by an imaginary
numerator computation distinct from the original quotient-rule replay;
it does not count a numerator root at a pole as a solution.

The exact replay reads the five rational boxes directly from C030z's
1307 table, checks all original source hashes, reconstructs every
product interval with positive factors, and matches both full rational
endpoints printed above. The integer cross-product margins for
L>-3/125000 and U<-11/500000 are respectively

    2032821559859950928005920690351625000 > 0,
    138492532798083277928780622644500000 > 0.

Reproduce the audit with

    python3 scripts/grunsky/conjugate-collision-audit-1324.py

The complete [audit certificate1324](../scripts/grunsky/conjugate-collision-audit-certificate-1324.json)
records the numerator coefficients, tangent, boxes, products, exact
endpoints, integer margins, hashes and17 checks, all passing with no
failures. Complete relevant fields were inspected. Script checks verify
finite algebra and recorded inputs; the following analytic guards were
checked in the mathematical argument, not certified by a Python flag.

Write d=(r^2)'(0)<0. Differentiability gives a delta1>0 such that
|r(tau)^2-1-d*tau|<=(-d/2)*tau for 0<tau<delta1. Hence
r(tau)^2<=1+(d/2)*tau<1. Continuity and the base values permit a
common smaller interval on which r>1/2, both denominator moduli
exceed1/2, and both images are within1/2 of1. Intersect this interval
with the IFT interval and (0,delta1). All guards then hold for every
positive tau in one interval, rather than at a sequence of sample
parameters. The two imaginary coordinates have opposite nonzero
signs; H=0 and real-coefficient conjugation give equal finite real
images there. Thus there is no hidden uniform-in-tuple assertion or
use of boundary injectivity. The direct finite collision proves the
stated scoped exclusion, preserving every independent gap above.
The audit establishes no sharper bound or new general theorem.

## Mathlib

Reuse the supporting IFT coverage in C031c:
`HasStrictFDerivAt.implicitFunction` and `ContDiffAt.implicitFunction`
in [Mathlib.Analysis.Calculus.Implicit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Implicit.html)
and [ImplicitContDiff](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ImplicitContDiff.html).
Full matching typically-real, rational collision and actual-Xi
specialization coverage is not checked. No absence claim or Lean
verification is made; neither the rational certificate nor inherited
Decimal contracts are formal Mathlib proofs. Audit1324 accepts this
conditional specialization with the upstream inputs still qualified;
it is not a formal verification or an audit of every inherited input.
