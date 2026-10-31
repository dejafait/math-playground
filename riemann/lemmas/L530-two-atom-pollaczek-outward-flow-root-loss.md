# L530 — Two-atom moment coefficients can lose real roots under outward flow

## Hypotheses

Use Dan Romik, *Orthogonal polynomial expansions for the Riemann xi
function*, arXiv:1902.06330v3 (5 May 2019), equations (A.21), (A.27)
and (3.26), [source](https://arxiv.org/html/1902.06330v3).
Thus f_n(x)=P_n^(3/4)(x;pi/2), f_0=1, f_1=2x, and

    (n+1) f_(n+1)(x)=2x f_n(x)-(n+1/2) f_(n-1)(x).

This standard basis normalization and the finite diagonal deformation
are imported, not reproved. Let q=12/25, u=0, v=1, and
m_j=(1-q)u^j+qv^j for j=0,1,2,3, with zeroth powers defined as 1.
These are precisely the moments of (13/25)delta_0+(12/25)delta_1:
m_0=1 and m_1=m_2=m_3=12/25>0. Define

    p_r(t)=sum_(j=0)^3 (-1)^j m_j r^(2j) f_(2j)(t/2),  0<r<=1.

## Conclusion

At r_0=9/32, p_(r_0) has six distinct real zeros. At r_1=1/3 it
has exactly two real zeros, both simple, and four nonreal zeros.
In particular 0<r_0<r_1<=1, but outward flow does not preserve
simple real-rootedness even in this two-atom [0,1] moment family.

This is a counterexample to the stated finite preservation implication,
not to RH. It uses an atom at zero, expressly allowed by the target.
It makes no claim about measures with different restrictions, actual
theta coefficients, the final radius 1, higher degrees, or Xi.
The statement, finite-flow normalization and both complete endpoint
certificates passed an independent exact audit on 30 October 2026.
This does not declare the source manuscript independently audited.

## Proof

The following finite recurrence specialization is needed because
Romik's formulas alone do not decide this moment-restricted question.
Writing z=t^2 and g_n(t)=f_n(t/2), the recurrence becomes
(n+1)g_(n+1)=t g_n-(n+1/2)g_(n-1). Successive substitution gives

    g_0=1,
    g_2=z/2-3/4,
    g_4=z^2/24-17z/24+21/32,
    g_6=z^3/720-25z^2/288+2401z/2880-77/128.

For s=r^2 set A=m_1 s, B=m_2 s^2, C=m_3 s^3. Then p_r(t)=P_r(t^2),
where the coefficients of P_r(z)=d+cz+bz^2+az^3 are

    d=1+3A/4+21B/32+77C/128,
    c=-A/2-17B/24-2401C/2880,
    b=B/24+25C/288,
    a=-C/720.

At either chosen radius A,B,C>0, so d>0,c<0,b>0,a<0.
Consequently P_r(-x)>0 for every x>=0, excluding every nonpositive
real z-root, including zero. A positive simple z-root yields exactly
two simple real t-roots, +/-sqrt(z). A nonreal z-root yields no real
t-root. This justifies the even-polynomial reduction without a
numerical-root or multiplicity assumption.

Substitution of the stated q and radii gives the following integer
polynomials, each a positive scalar multiple of P_r:

    I_0(z)=4426352279635-91525040694 z+626050620 z^2-1417176 z^3,
    I_1(z)=9135405-274802 z+2660 z^2-8 z^3.

The positive scalars are respectively 4294967296000 and 8748000.
For any real cubic az^3+bz^2+cz+d its discriminant is

    Delta=b^2 c^2-4ac^3-4b^3 d-27a^2 d^2+18abcd.

Direct integer arithmetic gives

    Delta(I_0)=1593895952528326541214254588811264 > 0,
    Delta(I_1)=-112042936313856 < 0.

For completeness, the exact sign rule follows from
Delta=a^4 product_(i<j)(z_i-z_j)^2. A nonzero discriminant excludes
repetitions. Three distinct real roots give positive discriminant.
For a real root and a conjugate pair, the conjugate difference has
negative square, while the other two factors multiply to a positive
fourth power of a modulus; the discriminant is negative. These are
the only possibilities for a real cubic. Hence I_0 has three distinct
real roots and I_1 has only one real root. The strict coefficient
signs already show all these real roots are positive. The asserted
six versus two real t-root counts, with simplicity, follow. The other
four t-roots at r_1 are nonreal and simple because the cubic has three
distinct nonzero roots. More explicitly, at any complex root t,
p_r'(t)=2t P_r'(t^2) is nonzero: t^2 is a simple cubic root and
P_r(0)=d>0 excludes t=0. This proves all multiplicity assertions.

### Applicability of the finite Poisson flow

Romik (3.25)-(3.26) starts from a monic polynomial with distinct roots.
The initial polynomial here satisfies those hypotheses after the
nonzero constant normalization

    alpha=-720/(q r_0^6)=-536870912000/177147,
    h(t)=alpha p_(r_0)(t).

Indeed p_(r_0) has leading coefficient -q r_0^6/720, and the preceding
root count proves distinctness. Its coefficients in the source's basis
are gamma_(2j)=alpha (-1)^j m_j r_0^(2j), with odd coefficients zero.
Equation (3.26) therefore gives, for every real sigma with
0<r_0 exp(-sigma)<=1,

    M_h(sigma,t)=alpha p_(r_0 exp(-sigma))(t).

The final radius is reached at sigma_1=-log(r_1/r_0)=-log(32/27)<0.
The leading coefficient becomes (r_1/r_0)^6=exp(-6 sigma_1), as the
source requires. Although alpha is negative, multiplying by it changes
no zeros or multiplicities. Thus the certified loss is precisely in
the outward-radius (decreasing-time) direction. The finite diagonal
formula is defined across collisions; no root-gap division, velocity
equation, uniqueness theorem or infinite-series limit is used.

### Exact replay and qualifications

Run from the notebook:

    python3 scripts/pollaczek/collision_certificate.py

The complete evidence is `scripts/pollaczek/collision-certificate.json`.
The recurrence implementation and a separate direct-coefficient formula
agree at both radii. In addition to the integer discriminants above,
exact rational Sturm chains independently certify positive-root counts
3 and 1. Their signs at zero and positive infinity are respectively

    I_0: (+,-,+,-), (-,-,-,-), giving 3-0=3;
    I_1: (+,-,+,+), (-,-,-,+), giving 2-1=1.

Here the complete ascending-coefficient chains are

    I_0: [4426352279635,-91525040694,626050620,-1417176],
         [-91525040694,1252101240,-4251528],
         [16523990665/110474226,-1], [-1];
    I_1: [9135405,-274802,2660,-8],
         [-274802,5320,-24],
         [2288255/30022,-1], [1].

Each second row is the derivative. For I_0 the negative remainders
before positive normalization are [66095962660,-441896904] and
[-2678466180520710470916/4185375380761]; multiply respectively by
1/441896904 and 4185375380761/2678466180520710470916 to obtain the
displayed next rows. For I_1 they are [9153020/9,-120088/9] and
[1969504739892/225330121]; the positive factors are 9/120088 and
225330121/1969504739892. The following division by the nonzero
constant has remainder zero in each case. Positive normalization
preserves the Sturm sign rules. Both terminal nonzero constants also
exclude repeated roots. Sturm's theorem gives V(0)-V(+infinity)=3
and 1; all real cubic roots are positive by the earlier coefficient
argument. This agrees with the discriminant proof independently.

The separate audit, with no imports from the generator or its local
mathematical modules, is reproduced by

    python3 scripts/pollaczek/l530_independent_audit.py

It checks Table A.1 after x=t/2 against (A.27), all displayed endpoint
coefficients and positive scales, and every coefficient and sign in
both Sturm chains. The complete discriminants are independently
checked as -Res(I,I')/a using 5-by-5 Sylvester determinants, giving
resultants 2258831090420283694371852461153191870464 and
-896343490510848 respectively. The full audit certificate is
`scripts/pollaczek/l530-independent-audit.json`: 37 exact checks pass
with no failures. Both complete endpoint records, including negative
remainders and normalization factors, were inspected in full. The
proof uses the displayed finite identities, not a certificate preview.
No additional grid or random search was performed; the prior
10,000-tuple evidence is preserved. The failed hand-selected parameters
preceding the corrected analytic specialization are retained in the
certificate and working record. Exact endpoint signs also force at
least one intermediate zero of the discriminant by continuity; no
claim about uniqueness or the precise collision radius is needed.

## Mathlib

A matching finite Pollaczek counterexample or preservation theorem was
not checked in Mathlib; availability is unknown. The recurrence is
imported by its precise source equations. Cubic discriminant algebra
and Sturm's standard named theorem supply the elementary exact checks;
no Lean formalization or claim of absence is made.
