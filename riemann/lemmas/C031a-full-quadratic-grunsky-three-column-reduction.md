# Corollary C031a: full quadratic Grunsky three-column reduction

## Hypotheses

Let b1,...,b5 be arbitrary real numbers, with b_j=0 for every integer
j outside 1,...,5. Set

    f_b(z)=z/(1+sum_(j=1)^5 b_j*z^(j+1)),
    g(Z)=1/f_b(1/Z)=Z+sum_(j=1)^5 b_j*Z^(-j).

Initially f_b is a normalized formal series at zero. Its denominator
has constant term one. Define symmetric mixed coefficients by

    log((f_b(z)-f_b(w))/(z-w))
        =-sum_(m,n>=0) c_mn*z^m*w^n.

There is no oddness, univalence, pole exclusion, or global convergence
hypothesis. Let A,B,C,D,E be strictly positive real constants. For
the actual-Xi application they are S2,...,S6 of L025. Their signs
are imported from L027; the numerical bounds used below are imported
from C030z calculation1307, conditional on the stated L037 arithmetic
contracts. No RH or Hankel-positivity hypothesis is assumed.

## Conclusion

Define finite convolution polynomials for k>=1 by

    q_k=b_(k+1)+(1/2)*sum_(i+j=k) b_i*b_j,
    r_k=b_(k+2)+sum_(i+j=k+1) b_i*b_j-b1*b_k
                       +(1/3)*sum_(i+j+l=k) b_i*b_j*b_l,       (1)

where all indices in the sums range from 1 to 5. The complete first
three columns are c_k1=b_k, c_k2=q_k, c_k3=r_k. Their sharp upper
support bounds are respectively 5,10,15; individual specializations
may have smaller support. In particular no infinite remainder survives
in these columns.

Write h_mn=delta_mn/m-sum_(k>=1) k*c_km*c_kn. All six entries are
exactly

    h11=1-sum_(k=1)^5 k*b_k^2,
    h12=-sum_(k=1)^5 k*b_k*q_k,
    h13=-sum_(k=1)^5 k*b_k*r_k,
    h22=1/2-sum_(k=1)^10 k*q_k^2,
    h23=-sum_(k=1)^10 k*q_k*r_k,
    h33=1/3-sum_(k=1)^15 k*r_k^2.                         (2)

For a given b, there exist t>0,u>0,v>0 satisfying the six full equations

    h11=t*A, h12=t*u*B, h13=t*v*C,
    h22=t*u^2*C, h23=t*u*v*D, h33=t*v^2*E               (3)

if and only if h11,h12,h13>0 and

    B^2*h11*h22-A*C*h12^2=0,
    C^2*h11*h33-A*E*h13^2=0,
    B*C*h11*h23-A*D*h12*h13=0.                         (4)

The unique reconstruction is

    t=h11/A, u=A*h12/(B*h11), v=A*h13/(C*h11).         (5)

Every solution necessarily obeys, with x=h11, y=2*h22 and
rho=B^2/(A*C),

    0<x<1, 0<y<1, (1-x)*(1-y)>=rho*x*y.              (6)

For the fixed1307 actual-Xi outer boxes, exact rational arithmetic gives

    0.843<rho<0.844.

The necessary relaxation (6) is strictly compatible: x=y=1/2 has
slack (1-rho)/4 strictly between 0.039 and 0.03925. Thus this one
necessary test is **inconclusive for the family**. No b satisfying
(3) or (4), no formal feasibility for the actual constants, and no
unit-disk univalence has been established. The exact condition still
unresolved is the existence of real b1,...,b5 satisfying (4) and the
three strict first-row signs. Passing (6) is not a witness for it.

## Proof

**Imported formal identities and exact support.** Use L.-P. Teo,
*Analytic functions and integrable hierarchies—characterization of
tau functions*, Lett. Math. Phys.64 (2003),75–92,
[arXiv:hep-th/0305005v2](https://arxiv.org/html/hep-th/0305005v2),
Sections2.1–2.2, recurrence and equations(2.3)–(2.4),(2.8)–(2.12),
including the formal-extension paragraph at the end of Section2.2.
In the leading-coefficient-one normalization, its degree-m Faber
polynomial satisfies

    Phi_m(g(Z))=Z^m+m*sum_(k>=1)c_mk*Z^(-k).          (7)

These are symmetric negative-log coefficients; the Faber coefficients
in (7) have the extra factor m. C030y's reciprocal identity applies
to the present f_b exactly: the exterior divided difference differs
from the interior one by (z/f_b(z))*(w/f_b(w)), whose logarithms have
only pure-variable terms. Thus mixed coefficients agree. Formal
validity permits this use without an exterior conformal-map premise.

The first three Faber polynomials specialize to

    Phi1(w)=w, Phi2(w)=w^2-2*b1,
    Phi3(w)=w^3-3*b1*w-3*b2.

Indeed the nonnegative Laurent parts of g,g^2,g^3 are respectively
Z, Z^2+2*b1, Z^3+3*b1*Z+3*b2. Subtracting the displayed lower
polynomials leaves just Z^m in each case, as required by the imported
Faber characterization. Every monomial of g has exponent between
-5 and 1; composition with a polynomial of degree m therefore has
no exponent below -5m. The subtracted terms have no lower exponents.
This proves the support bound for every real choice of b, including
b5=0. The coefficients at the extreme indices are b5,b5^2/2,b5^3/3,
so the bounds are sharp as polynomial identities.

For k>=1, expansion of g^2 gives coefficient
2*b_(k+1)+sum_(i+j=k)b_i*b_j at Z^(-k). Expansion of g^3 gives
3*b_(k+2)+3*sum_(i+j=k+1)b_i*b_j+
sum_(i+j+l=k)b_i*b_j*b_l. The correction -3*b1*g subtracts
3*b1*b_k there, while -3*b2 affects only exponent zero. Dividing
by m in (7) proves (1) and c_1k=b_k. Symmetry gives the claimed
columns. Multiplying these **complete** columns proves (2). The
cutoff in an off-diagonal entry is the smaller of its two support
bounds, not mixed total degree six. All six cutoffs remain valid if
some coefficients vanish. There is no summability or limiting issue.
This is a finite specialization of the cited identities, not a new
general Faber theorem or a reproof of one.

**Exact parameter elimination, including zero branches.** Suppose
(3) holds. Strict positivity of t,u,v,A,B,C gives h11,h12,h13>0.
Cancellation by multiplication yields the three equations(4).
Solving only the first row gives (5); its denominators are nonzero
under these strict signs. Conversely take any real b with those
three signs and (4). Formula(5) defines strictly positive t,u,v.
The first row of (3) holds by construction. The first equation(4)
gives h22=A*C*h12^2/(B^2*h11)=t*u^2*C; the second gives
h33=A*E*h13^2/(C^2*h11)=t*v^2*E; the third gives
h23=A*D*h12*h13/(B*C*h11)=t*u*v*D. This proves sufficiency.

There is no division by a b_j, q_k, r_k, polynomial resultant, or an
unclassified root. Zeros of h11,h12,h13 cannot be solutions because
the corresponding right sides of (3) are strictly positive. Such
zeros can be limits of solutions, and no closed-boundary exclusion
is asserted. The equivalence quantifies over all real finite b;
there is no hidden compact-box restriction or bounded-parameter
assumption. The inequalities below bound b for any actual solution,
but t,u,v can still have unbounded limiting branches. Equality in
Cauchy-Schwarz is retained. The excluded boundary t=0 or a zero
weight has not been used as a contradictory positive branch.

**The one necessary test.** Form the real weighted column vectors
a=(sqrt(k)*b_k)_(1<=k<=10) and e=(sqrt(k)*q_k)_(1<=k<=10),
padding b_k by zero for k>5. Then (2) gives

    ||a||^2=1-h11, ||e||^2=1/2-h22, <a,e>=-h12.

Each squared norm is nonnegative. Both are strictly positive for
a solution of (3), since h12>0 would be impossible if either vector
were zero. Along with h11,h22>0 from (3), this proves 0<x<1 and
0<y<1. Ordinary finite-dimensional Cauchy-Schwarz gives

    h12^2<=(1-h11)*(1/2-h22).

The first equation(4) gives h12^2=rho*h11*h22; substitution and
multiplication by two prove (6). This uses no Grunsky contraction
or univalence premise. It also implies 0<t<1/A and
0<sum_(j=1)^5 j*b_j^2<1 for every solution, without excluding
approaches to its boundary or a divergent positive weight.

For clarity, the five unchanged outer rational intervals are

| Constant | Lower | Upper |
| --- | ---: | ---: |
| A | 3.7172599285e-5 | 3.7172599286e-5 |
| B | 1.4417393139e-7 | 1.4417393141e-7 |
| C | 6.6303168020e-10 | 6.6303168031e-10 |
| D | 3.2136641485e-12 | 3.2136641527e-12 |
| E | 1.5876934435e-14 | 1.5876934595e-14 |

These intervals are imported as established in C030z calculation1307;
the present computation checks containment of its saved S2–S6
intervals, not its quadrature or Decimal implementation anew. Actual
inclusion remains conditional on L037's documented arithmetic
contracts: correctly rounded nearest Decimal exponentials widened by
adjacent representables, directed basic operations, rejection of
exceptional arithmetic and zero-containing divisors, all at precision100.
The previous L917/1307 analytic and implementation qualifications stand.

Since the bounds are positive, the exact outward ratio endpoints are

    rho_lo=B_lo^2/(A_hi*C_hi)
          =1039306124622421366605/1232330548304344312933,
    rho_hi=B_hi^2/(A_lo*C_lo)
          =207861224982153845881/246466109613348686570.

Integer comparison gives 843/1000<rho_lo<=rho_hi<844/1000.
At x=y=1/2 the left side of (6) minus its right side is
(1-rho)/4. Thus 39/1000<(1-rho)/4<157/4000=0.03925, uniformly
over the fixed boxes. The witness is only for this relaxed pair of
real variables. There is no inference that any b gives those values,
that (4) has a root, or that all six equations are compatible. The
test does not stop or certify the family. No parameter sweep, new
boxes or effective transcendental sign oracle has been used.

**Possible downstream use and outstanding analytic hypotheses.** The
block (S_(m+n))_(1<=m,n<=3) is exactly L030's H_2 after shifting both
indices by one. If a solution of (3) is separately certified with
f_b holomorphic and univalent throughout |z|<1, the classical
Grunsky inequality makes (h_mn) positive semidefinite. The precise
covered input is M. Obradovic and N. Tuneski, *Some application of
Grunsky coefficients in the theory of univalent functions*, Ann.
Univ. Paedagog. Crac. Stud. Math.25(2025),23–30, normalized disk
class on p23 and equation(1.4) on p25,
[publisher PDF](https://studmath.uken.krakow.pl/article/download/12363/10958/47182),
as inspected in assessment1310 and reused by assessment1312. Their
omega_mn=-c_mn. For a sequence supported on the first three indices,
the inequality is

    sum_(k>=1) k*|sum_(m=1)^3 c_km*a_m|^2
        <=sum_(m=1)^3 |a_m|^2/m.

The sign change disappears inside the absolute square. The full
finite supports already proved justify expanding its left side.
For real a it gives sum_mn h_mn*a_m*a_n>=0. Equation(3), t>0 and
invertibility of diag(1,u,v) would then transfer that sign to the
actual block. This conditional application imports a classical
inequality; it supplies no actual univalence or inverse representation.
In particular poles of f_b in the open disk must be excluded, and
univalence near zero is insufficient. No stronger Gram identity,
boundary-area hypothesis, conformal welding, strict contraction,
all-degree extension or RH-equivalent positivity is assumed. Every
larger block, initialization and singular case remains open. The
linear prescription stops in C030y/C030z are unchanged and do not
decide these different quadratic equations.

**Exact computation and evidence limits.** Reproduce from this notebook:

    python3 scripts/grunsky/quadratic-defect-1314.py

The complete
[certificate1314](../scripts/grunsky/quadratic-defect-certificate-1314.json)
stores all30 column entries, all45 mixed-log comparison residuals
(including zeros beyond the smaller column bounds), every full
weighted product, all six expanded equations, all three polynomial
conditions, target-substitution residuals, strict reconstruction guards,
input hash and complete ratio/slack endpoints. Independently of the
Faber composition calculation, the program extracts -log(1-D) with
D=sum_(j=1)^5 b_j*sum_(i=1)^j z^i*w^(j+1-i). Only its first three
powers can affect a first exponent <=3. Positive exponents justify
rectangle truncation at z-degree3 and w-degree15. Every comparison
and target-substitution residual is exactly zero; all12 Boolean checks
pass with no failures. Full column entries, six defects, residuals,
checks and the ratio/slack evidence were inspected. The mathematical
proof above also establishes the support, parameter equivalence and
inequality without relying solely on a program preview. The program
does not find or certify a solution, an exhaustive obstruction, or
an analytic map. This is local reproduction and specialization of
known identities and Cauchy-Schwarz, not progress beyond the checked
sources' general theorems or a new RH sign result.

## Mathlib

Full matching Faber/Grunsky/actual-Xi coverage has not been checked.
No absence or Lean-verification claim is made. The exact polynomial
script is not a formal proof, and the imported actual-input library
contracts remain unverified here.
