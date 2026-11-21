# Corollary C031d: outward first variations of the four boundary roots

## Hypotheses

Use the particular real C1 branch of C031c, at u=400, and C031a's
rational function

    P_tau(z)=1+sum_(j=1)^5 b_j(tau) z^(j+1),
    f_tau(z)=z/P_tau(z),
    N_tau(z)=P_tau(z)-z P_tau'(z)
            =1-sum_(j=1)^5 j b_j(tau) z^(j+1).

Here a prime on P means differentiation in z. Write v=160000-A/C,
where A,...,E are the fixed actual constants satisfying the unchanged
fixed1307 boxes reproduced in C031a. These are enclosing hypotheses,
not midpoint replacements. Actual inclusion retains C031c's inherited
L019,L021,L025,L027,L036,L037,L917 and1307 qualifications, including
the conditional Decimal contracts. This calculation does not audit
them anew. The open real parameter interval, b(0)=(1,0,0,0,0),
and tangent b'(0)=a are supplied by C031c:

    a=(-A/2,-200B,-vC/2,200(B-vD),(A+vC-v^2E)/2).

There is no assumed disk holomorphy, univalence, Gram positivity or RH.

## Conclusion

There are four local C1 root curves p_+,p_-,c_+,c_-, with

    P_tau(p_+(tau))=P_tau(p_-(tau))=0,
    N_tau(c_+(tau))=N_tau(c_-(tau))=0,
    p_+(0)=i, p_-(0)=-i, c_+(0)=1, c_-(0)=-1.

They remain simple near zero. The p curves are genuine poles of
f_tau, and P_tau(c_+(tau)),P_tau(c_-(tau)) are nonzero near zero,
so the c curves are genuine derivative zeros. Their squared-modulus
derivatives at zero are

    s_p = -a1+a3-a5 = -vC+v^2 E/2                    (1)
    s_+ = -a1-2a2-3a3-4a4-5a5
        = -2A-vC+(5/2)v^2E-400B+800vD              (2)
    s_- = -a1+2a2-3a3+4a4-5a5
        = -2A-vC+(5/2)v^2E+400B-800vD.             (3)

Both poles have derivative s_p. Exact rational bounds from the fixed
boxes give the strict enclosures

    0.000016 < s_p < 0.000018,
    0.00049  < s_+ < 0.00051,
    0.00007  < s_- < 0.00009.                     (4)

Thus all four curves lie strictly outside the closed unit disk for
every sufficiently small positive tau. This supplies no inward
pole/critical-point obstruction in the approved first-order test.
The test ends inconclusively for whole-disk univalence. No effective
or box-uniform parameter interval, classification of other roots,
global injectivity, actual mixed-form sign, larger-block conclusion
or RH conclusion is asserted. The local coefficient branch survives.

## Proof

**Known analytic inputs and the exact specialization.** Import the
real C1 implicit-function theorem and its derivative formula from
O. R. B. de Oliveira, *The Implicit and the Inverse Function Theorems:
Easy Proofs*, Real Anal. Exchange39(1)(2013/2014),207–218,
[arXiv1212.2066v1, Section3 Theorem2](https://arxiv.org/html/1212.2066v1).
For a base zero of a C1 real map on an open product neighborhood,
an invertible dependent derivative gives a local C1 root and its
derivative is minus the inverse dependent derivative times the
parameter derivative. Use real and imaginary parts of z as the two
dependent variables. C031c supplies b on an open interval containing
both signs of zero; P_tau and N_tau are therefore C1 in the three
real variables and holomorphic in z. No analyticity in tau or fixed
polynomial degree is needed.

At tau=0, P_0=1+z^2 and N_0=1-z^2. Their boundary roots are exactly
the four displayed roots. The dependent Jacobian of a holomorphic
polynomial with complex derivative d is

    [ Re d  -Im d ]
    [ Im d   Re d ],

whose determinant is |d|^2. For the P roots d=2z, and for the
N roots d=-2z. At every displayed root the determinant equals4.
This verifies simplicity and all dependent-invertibility hypotheses
separately. Applying the cited theorem gives the four curves, and
continuity keeps the z derivatives nonzero after shrinking their
intervals. Take a common smaller interval for this finite set.

For rational functions use L. V. Ahlfors, *Complex Analysis*,3rd ed.,
McGraw-Hill,1979,
[Chapter2 Section1.4,p30,(11), and Chapter4 Section3.3,
Theorem11/proof,pp131–133](https://people.math.gatech.edu/~mccuan/courses/6321/lars-ahlfors-complex-analysis-third-edition-mcgraw-hill-science_engineering_math-1979.pdf).
The reduced-rational discussion distinguishes poles from removable
factors; (11) gives the quotient derivative; the local mapping
theorem implies an injective holomorphic function has no derivative
zero. Only this necessary condition is relevant, not its converse.
The quotient identity here is exactly f_tau'=N_tau/P_tau^2 wherever
P_tau is nonzero. Since P_tau(0)=1 for every tau, its numerator z
cannot cancel any denominator root. At c_+(0),c_-(0) the denominator
equals2, so continuity keeps it nonzero along both c curves near
zero. Consequently the pole and derivative-zero interpretations
are legitimate, independently of their later radial directions.
These are applications of the named sources, not reproofs of IFT
or the local mapping theorem.

**First derivatives only.** Set

    Q(z)=sum_(j=1)^5 a_j z^(j+1),
    R(z)=-sum_(j=1)^5 j a_j z^(j+1).

They are respectively the tau derivatives of P_tau and N_tau at
zero, with z held fixed. The IFT derivative formula gives, for
z0=i,-i and x0=1,-1 respectively,

    p'(0)=-Q(z0)/(2z0),
    c'(0)=R(x0)/(2x0).

Here primes on p,c mean parameter derivatives. For any C1 complex
root curve r, (|r|^2)'(0)=2 Re(conjugate(r(0)) r'(0)). At z0=i,-i,
this equals Re Q(z0)=-a1+a3-a5. At x0=1,-1 it equals R(x0),
giving the two coefficient expressions in (2),(3). Substituting the
five tangent entries proves (1)–(3) exactly. In particular their
common even part is -2A-vC+(5/2)v^2E and their odd part is
-400B+800vD. No v'(0), higher branch coefficient or infinite series
is used.

**Exact interval specialization.** All five enclosing endpoints in
C031a are finite positive rationals. Write [X_l,X_h] for each box
and set

    v_l=160000-A_h/C_l,
    v_h=160000-A_l/C_h.

C031b's unchanged endpoints give

    v_l=344562347730000/3315158401,
    v_h=6891246956460000/66303168031,
    103935<v_l<=v<=v_h<103936.

The positive products therefore enclose vC,v^2E,vD in

    V=[v_l C_l,v_h C_h],
    T=[v_l^2 E_l,v_h^2 E_h],
    U=[v_l D_l,v_h D_h].

Use exact interval sums and signed scalar multiplication to form

    I_p=-V+T/2,
    I_0=-2[A_l,A_h]-V+(5/2)T,
    I_o=-400[B_l,B_h]+800U,
    I_+=I_0+I_o, I_-=I_0-I_o.

Correlation loss only enlarges these enclosures. Every bound uses
the actual constants via containment, without independent midpoint
substitution. For explicit load-bearing checks, exact fractions give

    inf I_p=3702266307503012197938345134223/
                  219805504474417536020000000000000000,
    sup I_p=14809066026791243859834520193529/
                  879222018189404083392200000000000000,
    inf I_+=108817523586217469266574422378443/
                  219805504474417536020000000000000000,
    sup I_+=10881752468087010066336840029007623/
                  21980550454735102084805000000000000000,
    inf I_-=1107322098088287060116652855543619386104581/
                  14573801297306028231587054976620000000000000000,
    sup I_-=1107322168456948704308212420884064723915119/
                  14573801299723888781206782039361000000000000000.

Positive-denominator integer comparisons put these closed intervals
strictly inside the three open decimal-rational intervals (4).
The inward threshold is s<0, whereas each lower endpoint is positive.
This is an exact bound under the inherited input contracts, not a
numerical plot or an interval refinement of those inputs.

**Strict eventual direction and the scope of failure.** For each
curve the C1 expansion is |r(tau)|^2=1+s tau+o(tau), with s>0
by (4). There is a positive radius on which the absolute remainder
is at most s tau/2 for positive tau. Thus |r(tau)|^2>1 there.
Taking the minimum of the four radii establishes the stated common
eventual direction. Its existence is qualitative for the fixed actual
tuple. The uniform derivative enclosures in (4) do not by themselves
provide a box-uniform IFT neighborhood or an effective radius.

There is no inward member of these four root curves, so this specific
necessary test cannot park C031c's realization. Outward motion is
not a sufficient condition for injectivity: the local mapping input
does not exclude equal values at distinct points. Nothing here
proves a whole-disk admissible realization, even though the local
six-equation branch and its positive weights remain available.
Other roots, other branches, larger blocks, identification and
initialization are outside this conclusion. In particular no
target-equivalent positivity is assumed in any implication.

**Reproduction and evidence limits.** Run from this notebook:

    python3 scripts/grunsky/boundary-variation-1320.py

The complete
[certificate1320](../scripts/grunsky/boundary-variation-certificate-1320.json)
records the four roots, both coordinates of each tau derivative and
implicit velocity, all four real Jacobians and determinants, the
full radial linear forms, exact polynomial reductions with positive
common denominator2C^2, input boxes/hashes, interval components and
endpoints, all29 checks and failures. All29 pass; failures are empty.
The complete root evidence, interval components, bounds and checks
were inspected. The elementary formulas and interval construction
above give the mathematical argument independently of a preview.
This is a reproduction/specialization of known tools and an informative
inconclusive test, not a new general theorem or a resolution of RH.

## Mathlib

The reused assessments1315/1316 supply supporting
`HasStrictFDerivAt.implicitFunction` and `ContDiffAt.implicitFunction`
in [Mathlib.Analysis.Calculus.Implicit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Implicit.html)
and [ImplicitContDiff](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ImplicitContDiff.html).
Full matching complex-root, rational-cancellation, injective-derivative
and fixed actual-Xi branch coverage has not been checked. No absence
claim, Lean verification or independent audit of the inherited Decimal
library is made. Exact Fraction calculations are not a Mathlib proof.
