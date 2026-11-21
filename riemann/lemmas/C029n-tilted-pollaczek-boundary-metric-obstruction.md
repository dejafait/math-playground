# C029n — The full tilted-Pollaczek T_6 has no boundary-supported metric

## Hypotheses

Use the exact full family from Alexey Kuznetsov, *Expansion of the
Riemann Xi Function in Meixner-Pollaczek Polynomials*, Canad. Math.
Bull. 51(4) (2008), 561–569,
[primary source](https://doi.org/10.4153/CMB-2008-055-0), recurrence (2),
coefficients (4)/(13), printed pp563/566, and the weights pp568–569:

    p_(-1)=0, p_0=1,
    (k+1)p_(k+1)(t)=t p_k(t)-(k+1/2)p_(k-1)(t),
    u_n= -n!/sqrt(2) * sum_(h=0)^n
      4^h (4^(h+1)-1) B_(2h+2) (2pi)^(h+1)
      * sin(pi(n-h)/2+pi/8) / ((n-h)! (2h+2)!),
    beta_n=4n(n-1)u_(n-2)+(8n^2+12n+7)u_n
           +(2n+3)(2n+5)u_(n+2),
    a_k=6!/((6-k)!6^k) beta_k,  0<=k<=6,
    T_6(t)=sum_(k=0)^6 a_k p_k(t).

The first term in beta_n is omitted for n=0,1. The Bernoulli convention
is B_1=-1/2. All coefficients, including odd ones, are retained; u_0
through u_8 are used. The exact formula, rather than the source's
numerical root observations, is the input.

Use the descending basis Phi=(p_5,p_4,p_3,p_2,p_1,p_0)^T. Once a_6!=0
has been proved below, normalize T_6 by a_6 and form its comrade C in
Definition2.1 of V. Noferini, L. Robol and R. Vandebril, *Structured
backward errors in linearizations*,
[arXiv:1912.04157v2, 12 May 2021](https://arxiv.org/pdf/1912.04157v2),
PDF pp3–4. Scale A=D^(-1)CD by the positive diagonal D for which the
basis part is symmetric and D_6=1, as specified and verified below.
Let e_1=(1,0,0,0,0,0)^T. All matrices and candidate vectors are real.

## Conclusion

The actual degree of T_6 is six. There is **no** vector z in R^6 such
that

    G=I_6+e_1 z^T+z e_1^T,       A^T G=GA.

Thus the proposed ansatz fails even without nonsingularity or the
negative-index restriction. This is only an N=6 obstruction for this
specific metric support and normalization. It gives no obstruction to
other metrics, no actual root count, no failure of an eventual-only
bound, and no proof or disproof of RH. The finite assertion was
independently audited in step2012; the scope is unchanged.

## Proof

### 1. Exact coefficients and signs

Put S=sin(pi/8)/sqrt(2)>0, s=sqrt(2), r=1+s and x=pi. Write q_n=beta_n/S.
The elementary half-angle identity gives cot(pi/8)=1+sqrt(2). Hence

    sin(pi*m/2+pi/8)/sin(pi/8) = 1,r,-1,-r

according as m is 0,1,2,3 modulo 4. The coefficients u_n/S and q_n are
therefore exactly in Q(s)[x]. Using the source formula and

    (B_2,B_4,...,B_18)=
    (1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510,43867/798)

gives the following load-bearing polynomials:

    q_0=4x+10r x^2-8x^3,
    q_1=4r x-26x^2-56r x^3+(136/3)x^4,
    q_2=-4x-42r x^2+168x^3+(1632/5)r x^4-(3968/15)x^5,
    q_6=-4x-106r x^2+1256x^3+(28832/3)r x^4
         -(1099136/21)x^5-(21581312/105)r x^6
         +(5826930688/10395)x^7+(129455497216/135135)r x^8
         -(104932671488/135135)x^9.

For example, u_0/S=-x/2, u_2/S=x/2+(2/3)r x^2-(8/15)x^3,
so q_0=7u_0/S+15u_2/S has the displayed value. For q_6 use exactly
120u_4+367u_6+255u_8. The certificate retains every u_0,...,u_8 and
q_0,...,q_6 coefficient, including those not needed for the obstruction.
The Bernoulli table is also checked by the defining recurrence

    B_0=1,  B_m=-(1/(m+1)) sum_(k=0)^(m-1) binom(m+1,k) B_k.

Define

    Q=(3/2)a_1^2-a_0^2-(5/2)a_2 a_0,
    q=Q/S^2=(3/2)q_1^2-q_0^2-(25/12)q_2 q_0,

where a_0=S q_0, a_1=S q_1 and a_2=(5/6)S q_2. Expanding in the
same exact field gives

    q=(268/3+48s)x^2+(124/3)r x^3+(-239/3+206s)x^4
       -1848r x^5+(-43952/9-4192s)x^6
       +(30016/9)r x^7-(11936/9)x^8.

The following are closed rational enclosures. The decimal notation
denotes exact rationals with denominator 10^12, not floating values:

| Quantity | Lower bound | Upper bound |
| --- | ---: | ---: |
| q_0 | 2.789485175631 | 2.789485175632 |
| q_6 | -0.057944075431 | -0.057944075430 |
| a_6/S | -0.000894198695 | -0.000894198694 |
| q=Q/S^2 | -9.200207003118 | -9.200207003117 |

In particular a_0>0, a_6<0 and Q<0. The recurrence for p_k shows
inductively that its leading coefficient is 1/k!: multiplication by t
raises degree by one and the subtracted polynomial has lower degree.
Thus T_6 has leading coefficient (a_6/720) != 0 and actual degree six.

Here is a complete elementary justification of the enclosures and their
error bounds. For 0<v<1 and even M=48, integrating the finite geometric
identity for 1/(1+t^2) from 0 to v gives

    R_M(v)=sum_(j=0)^(M-1) (-1)^j v^(2j+1)/(2j+1),
    0 < arctan(v)-R_M(v) < v^(2M+1)/(2M+1)=E_M(v).

Indeed the remainder integrand is t^(2M)/(1+t^2), positive and less
than t^(2M). Set theta=arctan(1/5), phi=arctan(1/239). The tangent
addition formula gives tan(2theta)=5/12, tan(4theta)=120/119 and
tan(4theta-phi)=1, with nonzero denominators (in the last formula,
numerator and denominator both equal 28561/28441). Also

    4(1/5-1/375)-1/239 < 4theta-phi < 4/5.

The lower bound is positive. Since arctan(1)=pi/4>1/2 by its integral,
4/5<pi/2. Hence the angle lies in (0,pi/2), and the injectivity of
tangent there gives the exact Machin identity pi=16theta-4phi.
Consequently pi lies between the exact rational numbers

    16R_M(1/5)-4(R_M(1/239)+E_M(1/239)),
    16(R_M(1/5)+E_M(1/5))-4R_M(1/239).

The program rounds these outward to the grid 10^(-60). For sqrt(2),
let b be the integer square root of 2*10^120. The interval
[b/10^60,(b+1)/10^60] contains sqrt(2); the program verifies the strict
squared endpoint inequalities and positivity using integers/Fractions.
There is no assumed decimal expansion of pi or sqrt(2).

For interval addition use the sums of endpoints; for multiplication
use the minimum and maximum of the four endpoint products. These rules
enclose every sum or product by order and bilinearity. A coefficient
A+B sqrt(2) is enclosed with its correct B-sign. Starting at the highest
power, interval Horner evaluation then encloses each polynomial by
induction. All operations use Python's exact Fraction/integer arithmetic.
Final decimal-grid rounding is outward by integer floor/ceiling. The
expanded q polynomial and its factored expression above are both
evaluated, both are strictly negative, and their intervals overlap.
This finite rational calculation yields the displayed bounds without
an unproved numerical-error assumption or an interval-library contract.

Reproduction command, relative to this notebook:

    python3 scripts/pollaczek/tilted_boundary_metric_2010.py

Full exact coefficients, rational endpoints, arctangent terms and
remainder bounds, scaling checks, compatibility equations, and failures
are saved in `scripts/pollaczek/tilted-boundary-metric-2010.json`.
The run passes all 20 checks with no failures. The script and certificate
are verification artifacts; the elimination argument is given next.

### 2. Comrade convention and finite scaling

For j=1,...,6 put c_j=a_(6-j)/a_6. Let H have zero diagonal, upper
diagonal (11/2,9/2,7/2,5/2,3/2), and lower diagonal (5,4,3,2,1),
with all other entries zero. The recurrence gives

    H Phi=t Phi-6p_6 e_1,
    C=H-6e_1 c^T,
    C Phi=t Phi-6(T_6/a_6)e_1.

This is precisely the cited descending-basis comrade: its leading-basis
ratio is chi=(1/6!)/(1/5!)=1/6. Noferini–Robol–Vandebril Theorem2.2,
including its proof on PDF pp3–4, supplies
det(tI-C)=720 T_6(t)/a_6. We import that theorem; no new linearization
theorem or simple-root premise is required.

Take D positive diagonal with

    (D_1^2,...,D_6^2)=(693/256,315/128,35/16,15/8,3/2,1).

For the neighboring rows whose higher basis degree is k=5,4,3,2,1,
these numbers satisfy

    (k+1/2)D_(i+1)^2=k D_i^2.

Both factors and all D_i are positive. Thus D^(-1)HD=J is symmetric
with zero diagonal and successive off-diagonals

    sqrt(55/2), sqrt(18), sqrt(21/2), sqrt(5), sqrt(3/2).

This directly verifies the finite scaling; no compact-support
orthonormality assumption from the source's Section2.2 is imported.
The adjacent ratios determine D uniquely when D_6=1. Set

    v_j=6 a_(6-j) D_j/(a_6 D_1).

Then A=J-e_1 v^T. Every denominator here is nonzero: a_6<0 was proved
above, D_1>0, and the remaining denominators are positive integers.

### 3. Complete compatibility system and its contradiction

Let f_1 be the first coordinate vector in R^5. Partition the matrices
after their first row/column:

    A = [ alpha  b^T ],    G = [ g   y^T ],
        [ c      B   ]        [ y   I_5 ],

    alpha=-v_1,  c=sqrt(55/2)f_1,
    b=(sqrt(55/2)-v_2,-v_3,-v_4,-v_5,-v_6)^T,
    B=J[2:6,2:6],  g=1+2z_1,  y=(z_2,...,z_6)^T.

Here g and y are arbitrary real variables. B is symmetric. Because G
is symmetric, A^T G=GA is equivalent to GA being symmetric. Direct
block multiplication shows that its complete nonredundant equations are

    (B-alpha I_5)y+g b=c,
    y_i b_j-b_i y_j=0,    1<=i<j<=5.                 (1)

The upper-left scalar imposes no condition. Thus (1) consists of all
five first-row equations and all ten bulk equations, not a selected
subsystem asserted sufficient without proof.

Since a_0>0, a_6!=0 and D_1>0,

    b_5=-v_6=-6a_0/(a_6 D_1)!=0.

The equations in (1) with j=5 give y=lambda b, with the well-defined
real lambda=y_5/b_5. The first five equations consequently become

    (g-lambda alpha)b+lambda Bb=c.                 (2)

Only entries 4 and 5 of (2) are now needed; c_4=c_5=0. Set

    K=b_4(Bb)_5-b_5(Bb)_4.

Multiplying entry 5 by b_4 and subtracting b_5 times entry 4 gives
lambda K=0. The last two rows of B give

    (Bb)_4=sqrt(5)b_3+sqrt(3/2)b_5,
    (Bb)_5=sqrt(3/2)b_4,
    K=sqrt(3/2)(v_5^2-v_6^2)-sqrt(5)v_4 v_6
     =36 sqrt(3/2)/(a_6^2 D_1^2)
        * ((3/2)a_1^2-a_0^2-(5/2)a_2 a_0)
     =36 sqrt(3/2)Q/(a_6^2 D_1^2).                (3)

For the cross term in (3), D_4=sqrt(15/8) and
sqrt(5)D_4/sqrt(3/2)=5/2; both sides are positive and their squares
are 25/4. Also D_5^2=3/2 and D_6=1. This checks the radical factors
and signs in (3) explicitly. Since Q<0, the prefactor is positive
and K<0, in particular K!=0. Therefore lambda=0, y=0, and entry 5
of (2) gives g b_5=0, so g=0. But all of (2) would then require
0=c, whereas c_1=sqrt(55/2)>0. This is the contradiction.

No compatible G exists, singular or nonsingular. Thus no Schur-inertia
or Pontryagin theorem needs to be applied in this failed ansatz. The
only divisions in the elimination were by the proved nonzero a_6,
D_1 and b_5. The full calculation is finite, with no limit interchange.

### 4. Independent audit2012

The source formulas were compared with the prior exact primary-source
extraction in review2001 and the separately approved audit scope2010.
No new source theorem or wider hypothesis is needed. The original
Fraction replay passes all 20 checks. A separate sparse-polynomial
implementation reconstructs every u_0,...,u_8, beta_0,...,beta_6 and
a_0,...,a_6 from the source formula, with every odd phase retained.
It checks every Bernoulli entry, Jensen weight, arctangent term and
remainder, both Machin endpoints, the squared sqrt(2) bounds, every
polynomial interval endpoint, all four displayed rational bounds and
the positive diagonal scaling. All 63 comparisons pass, with no
failures. Reproduce it from this notebook with

    python3 scripts/pollaczek/tilted_boundary_metric_audit_2012.py

The complete comparisons and exact load-bearing endpoints are in
`scripts/pollaczek/tilted-boundary-metric-audit-2012.json`, which also
records the original certificate's SHA256. The expanded and factored
Q intervals were inspected in full, as were q_0,q_1,q_2,q_6,u_8 and
the scaling data. Exact comparison, rather than a bounded preview,
checks all other saved coefficient and interval entries. In particular
the expanded Q/S^2 is at most -9.200207003117<0; a_0/S is at least
2.789485175631>0 and a_6/S is at most -0.000894198694<0. These bounds
pay the degree, b_5 and K nonvanishing premises used above.

Independently multiplying the blocks gives

    GA=[g alpha+y^T c, g b^T+y^T B;
        alpha y+c,    y b^T+B].

Its off-diagonal symmetry is exactly the five plus ten equations(1).
The scalar block imposes none. For j=5 the bulk equations read
y_i b_5=b_i y_5, so no division by any possibly zero b_i is used.
With h=g-lambda alpha, rows 4 and 5 read
h b_i+lambda(Bb)_i=0. Their displayed combination gives lambda K=0
with the sign in (3). The last two rows of B and the positive squared
D entries give precisely the Q factor in (3). Thus lambda=0,
then g=0 by b_5!=0, contradicting c_1>0. This checks the complete
left-metric system and its elimination on paper; the arithmetic
verifier does not claim to formalize that matrix argument. The Machin
branch argument likewise uses the integral inequality in section1,
not just the program's tangent-identity check.

No proof correction was required. This audit reproduces and validates
the already recorded finite obstruction; it does not claim a newly
discovered obstruction, formal verification, or progress on the
eventual bound.

This is the same exact family that motivates C029m; that lemma's
conditional RH implication is downstream context, not an input to the
finite contradiction. Compact convergence and its source's upstream[9]
qualification are unused here. Eventual uniform index remains entirely
open. The result is a local rejection of an unproved ansatz, not a
claim of novelty beyond the sources checked or an RH candidate.

## Mathlib

The full matching obstruction, its coefficient calculation, and
supporting comrade/interval statements were not checked in Mathlib.
No absence or formal-verification claim is made. The source theorem
is imported precisely; only the approved finite scaling, compatibility
elimination and elementary rational enclosure are derived here.
