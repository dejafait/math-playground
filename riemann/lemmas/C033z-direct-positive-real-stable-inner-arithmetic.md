# Corollary C033z: stable inner arithmetic for the direct preflight

## Hypotheses

Use C033y's exact analytic construction, including its20 logarithmic
panels from log(2^-30) to log(1/4),13 outer Gauss nodes per panel,
three widths sigma=1,3/2,2, and48 inner Gauss positions on [0,4].
Write those inner positions and weights as x_j, omega_j (1<=j<=48),
and set

    a_j=omega_j*exp(-x_j^2), q=w^-1/2,
    Jhat(w)=q*sum_j a_j R(x_j*q),
    R(z)=exp(z/2)/(2*sinh(z))-1/(2*z), R(0)=1/4.

Here 0<x_j<4, 0<omega_j<=1, sum omega_j=4, w>=1, and q>0.
The value Jhat(1) is shared. These are exact finite sums from C033y,
not the untruncated integrals J(w). Retain C033y's actual divisor,
conjugation/multiplicity, excluded ordinate zero, strict strip/gamma>14,
counting, through100/retained real zero, reciprocal-square tail, heat
positivity/separate fixed-j errors, both fixed-v1 qualifications, zero
drift/killing and Gaussian half-variance. Source-wide correctness and
zero data remain unverified. The finite arithmetic assertion below
itself uses only the displayed real-node ranges and C033y's panel map.

For the original *conditional input contract*, supply rational approximations
to each x_j, omega_j, exp(-x_j^2), and each of the780 values q, with
absolute error at most delta=2^-60. These are accuracy requirements,
not claims that the data have been generated. The1802 extension below
supplies a costed construction, without evaluating all those data.
Clamp the first three families to [0,4], [0,1], [0,1], respectively;
clamp q to [0,1/4]
on the first17 panels and [0,1] on the remaining panels. Use q=1
exactly for Jhat(1). Clamping preserves the asserted input accuracy.

All subsequent rational arithmetic in the original construction is exact.
The optional1810 extension below changes only Ihat accumulation, using
explicit exact rational comparisons to select approximate dyadic values.
The optional1830 width extension converts the normalized coefficient once
to a dyadic midpoint; its eight subsequent Newton steps remain exact.
Count each rational
addition, subtraction, multiplication or division, and each rational
comparison (including clamping and root signs), as one operation, including operations by
small integers. No fused multiply-add is granted. This is an algebraic
operation count, not a bound on bit complexity, memory or running time.

## Conclusion

There is a specified stable rational core producing approximations to
all780 differences Jhat(w)-Jhat(1), with uniform absolute error <2^-24
under the input contract. In C033y's exact outer sums their contribution
to exponent error is <2^-22. The core, including coefficient formation,
clamping, shared moments and final differences, costs at most374518
of the defined operations, hence fewer than380000.

The first17 panels use663 evaluations of a degree28 polynomial formed
from29 shared moments. The remaining117 profiles and the one fixed
Jhat(1) use a factored polynomial quotient at48 positions each. No
division by a small z and no subtraction of terms proportional to1/z
is performed. Both approximation errors and input sensitivity are
bounded below; requesting precision from a library is not the proof.

The1802 extension specifies an unconditional construction of the required
finite input data in at most350842 further operations. Hence the inputs
and core together cost at most725360, leaving274640 of the10^6 cap.
Here "unconditional" concerns finite arithmetic only, not the retained
external law/divisor assumptions. Only reference roots/weights were
actually computed; the Gaussian factors and q values were not evaluated.
At1802, constants, I(1), prime terms, the other profile terms, outer
arithmetic and final exponentials remained unpaid. The1803 extension
below supplies those contracts in264407 further operations. The complete
specified construction therefore costs at most989767, leaving10233 of
the10^6 cap. Its exponent arithmetic error is <2^-17<2^-10 and its
final exponential error is <=384/21!<2^-10; with C033y's analytic
allowance each final scalar has error <2^-8. This is a complete
SUFFICIENT PREFLIGHT, PASSED APPLICATION AUDIT1806 under the retained
external qualifications and the stated algebraic-operation model.
It uses all prime powers through32 with explicitly paid suppression,
as detailed below, instead of C033y's smaller adaptive cutoffs.
No callback, transform, interpolation or TV estimate was evaluated.
This is local REPRODUCTION under SPECIALIZE1799, not progress beyond
the general source tools or an RH candidate. Bit complexity is unbounded
by this operation model; source and finite-zero qualifications remain.

The optional1810 extension rounds Ihat accumulation after every four
samples, retaining exact samples and all other constructors. Its full
upper ledger is997104 operations and its uniform final scalar radius
is <0.001534<2^-8, with both2^-10 allowances preserved. Each checkpoint
has denominator dividing2^32. This is a proved local rounding contract,
not a completed evaluator run; independent application audit1812 below
passes under the unchanged qualifications and operation model.

The optional1830 width extension supplies one-time coefficient conversion
and eight exact Newton steps in at most288 operations per supplied width,
including normalization and clamps, with total width-input error<2^-62.
Every Newton iterate x_n has denominator exactly2^[34*(3^n-1)]; the
rescaled output denominator is at most2^223055. These bounds are
independent of the supplied width denominator. Independent application
audit1832 below passes. This finite local construction supplies no revised
global ledger, bit/runtime bound, completed scalar or RH conclusion.

## Proof

### Imported construction and purpose of the finite specialization

Import C033y's analytic errors, positive Gauss weights, exact panel map
and discrete outer bound sum weight*g_s<13. The underlying formula is
Alain Connes, *Heat Expansion and Zeta*,
[2402.13082v1, Section2(4)-(9), p4](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf),
in C033u's enlarged-width normalization. The Gauss theorem is Fredrik
Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
[1802.07942v1, Sections2/2.1, pp2-3](https://arxiv.org/pdf/1802.07942v1).
Neither theorem is reproved. At construction1801 C033y's application was an unaudited
input; the construction itself is not an audit of it. The polynomial remainder,
input perturbation and operation count here fill a different, explicitly
unpaid part of that construction. Standard power series and Cauchy's
coefficient estimate suffice; no new external numerical theorem is used.

### A convergent local polynomial and its shared moments

Let S(z)=sinh(z)/z, S(0)=1. On |z|<=2,

    |S(z)-1| <= sinh(2)/2-1 < 7/8,
    |exp(z/2)-1|/|z| <= (e-1)/2 < 7/8,
    |S(z)-1|/|z| < 7/16.

The inequalities at zero are their limiting versions. For the first,
e<11/4 and e^-2>16/121 give
sinh(2)/2<(121/16-16/121)/4<15/8. The exponential estimate follows
by positive power-series coefficients, as does the last estimate.
Thus |S|>1/8 and

    |R(z)|=|exp(z/2)-S(z)|/(2*|z|*|S(z)|)<21/4<6.

The removable value at zero is1/4. In particular R is holomorphic on
a neighborhood of the closed disk of radius2. If R(z)=sum c_k*z^k,
Cauchy's coefficient estimate gives |c_k|<=6/2^k. Put

    P(z)=sum_(k=0)^28 c_k*z^k.

For 0<=z<=1,

    |R(z)-P(z)| <= sum_(k=29)^infinity 6/2^k=6/2^28,  (1)
    |P(z)|<12, |P'(z)|<=12.                         (2)

All c_k are rational. For n=0,...,28 compute them recursively from

    E_n=1/(2^(n+1)*(n+1)!),
    A_n=E_n - (1/(n+2)! if n is odd, otherwise0),
    c_n=A_n/2-sum_(j=1)^floor(n/2) c_(n-2*j)/(2*j+1)!. (3)

This is coefficient comparison in2*S*R=(exp(z/2)-S)/z. It specifies
the polynomial exactly; it is not a fitted polynomial.

For the right endpoint of panel j (numbered1,...,20), the width obeys

    w>=sigma+2^(28-7*j/5).

On the first17 panels,28-7*j/5>=21/5>4 and sigma>=1, so w>16.
Thus q<=1/4 and x_j*q<=1. There are17*13*3=663 such profiles.
Precompute v_j=x_j/4 and the29 moments

    M_k=sum_j a_j*v_j^k, d_k=c_k*M_k, 0<=k<=28.

Then evaluate q*sum_(k=0)^28 d_k*(4*q)^k by Horner's rule. This is
exactly q*sum_j a_j*P(x_j*q); it is an interchange of finite sums.
Since sum a_j<=4, its error from Jhat(w) is at most6/2^28 by(1).
The scaling v_j<=1 and4*q<=1 avoids large intermediate moments.

### A factored quotient for the remaining profiles

For 0<=z<=4 set

    E16(z)=sum_(k=1)^16 z^(k-1)/(2^k*k!),
    U10(v)=sum_(j=1)^10 v^(j-1)/(2*j+1)!,
    T10(z)=z*U10(z^2), S10(z)=1+z*T10(z),
    A(z)=(E16(z)-T10(z))/(2*S10(z)).

S10>=1, so the denominator is at least2, including at zero. For
E=(exp(z/2)-1)/z and T=(S-1)/z, continuously extended at zero,
the identity R=(E-T)/(2*S) holds. Positive coefficients, the exponential
Taylor remainder and geometric bounds for the sinh tail give

    |E-E16| <= dE=8*2^15/17!,
    |S-S10| <= dS=(4^22/23!)/(1-16/(24*25)),
    |T-T10| <= dT=dS/4.                              (4)

For the first bound divide the degree16 exponential remainder by z
before maximizing z^16 on [0,4]; e^(z/2)<=e^2<8. There is no1/z
loss at zero. In the last two bounds the first omitted monomials have
degrees22 and21; successive ratios are at most16/(24*25). The factor
1/4 in dT compares their separate maxima at z=4, not their pointwise
ratio near zero.

On this real interval, E16<=E<2 and T10<=T<2: use their positive
series and at z=4 the inequalities e^2<8 and sinh(4)/4<e^4/8<8.
Together with S,S10>=1, these imply

    |R-A| <= (dE+dT)/2+2*dS=:dR<2^-28.              (5)

The last comparison is an exact rational inequality, checked in the
certificate below. No numerical samples establish this uniform bound.

We also need an input-sensitivity bound. The integral representation
E(z)=(1/2)*integral_0^1 exp(t*z/2)dt gives E16'(z)<=E'(z)<1.
Similarly S(z)=integral_0^1 cosh(t*z)dt gives S10'(z)<=S'(z)<16.
The positive series for T10' makes it increasing, and

    T10'(z)<=T'(4)=S'(4)/4-(S(4)-1)/16<4.

It follows from differentiating the rational quotient that

    |A(z)|<2, |A'(z)|<(1+4)/2+4*16/2<35.           (6)

For each of the remaining117 profiles use q*sum_j a_j*A(x_j*q).
Use the same formula with q=1 for Jhat(1). Their individual errors
are at most4*dR<2^-26 by(5). This rule is valid even for nodes of
these panels that happen to have w>=16; no threshold decision based
on an approximate w is needed.

### Exact rational evaluation with perturbed input data

Use hats for the clamped rational inputs and form ahat_j exactly as
omegahat_j*ehat_j. Then |ahat_j-a_j|<=2*delta and
sum|ahat_j-a_j|<=96*delta. Also

    |x_j*q-xhat_j*qhat|<5*delta,

with the sharper bound17*delta/4 on the first17 panels. Every
polynomial, moment and quotient is evaluated by exact rational
arithmetic, so there are no extra operation-rounding terms.

For the high-width polynomial rule, telescope first the outer factor q,
then the polynomial arguments retaining the exact a_j, then the a_j.
Using(2), qhat<=1/4 and sum a_j<=4, its additional error is at most

    48*delta+(1/4)*4*12*(17*delta/4)
                         +(1/4)*12*96*delta
       =387*delta<512*delta.                         (7)

For the quotient rule, use(6), qhat<=1 and the same telescoping order:

    8*delta+4*35*5*delta+2*96*delta
       =900*delta<1024*delta.                        (8)

The latter bound also covers the fixed Jhat(1), for which the first
term is actually zero. The stable moment rearrangement is an exact
identity for the perturbed data as well, so(7) applies to its Horner
implementation without an extra moment-error allowance.

Consequently every computed Jhat(w)-Jhat(1) has error less than

    2^-25+2^-26+2048*delta <2^-24.                   (9)

Here6/2^28<2^-25, and both low-width errors are smaller than this
common bound. C033y's exact finite profile contains this difference
with coefficient -1/(2*pi). Its exact positive outer weights obey
sum weight*g_s<13 and2*pi>6. Thus this core's error contribution to
each compact exponent is <13/(6*2^24)<2^-22. This use of exact
remaining coefficients leaves their finite-arithmetic errors unpaid.
It applies also to the compact width-one sums reused for m(s); it
does not equate m(s) with k(s,1) or omit their distinct tail errors.

### Complete count for this core, and what it does not count

Form factorials1!,...,30!, their reciprocals, and2^1,...,2^29.
These cost30+30+29 operations. Form E_n for0<=n<=28 with29
divisions, A_n with14 subtractions, then halve each A_n with29
divisions. The recurrence(3) has sum floor(n/2)=196 summands,
each requiring one multiplication and one subtraction. Total coefficient
formation:553 operations. The E16 and U10 coefficients reuse this table.

Clamp the48 triples with288 comparisons, form their48 a_j and48 v_j
with96 operations, form the29 M_k by successive powers with48*(28+
29+29)=4128 operations, and form29 d_k with29 multiplications.
These steps plus coefficient formation total5094. Clamping780 q values
costs1560 further comparisons.

Each high-width profile uses one multiplication for4*q,28 Horner
multiply/add pairs and one final multiplication by q:58 operations.
Each quotient sample uses one multiplication for z=x*q, one for z^2,
30 operations for E16,18 for U10, one for T10, two for S10, one
subtraction, one denominator multiplication, one division, one product
with a_j and one accumulation:58 operations. Thus a quotient profile
uses48*58+1=2785 operations, including multiplication by q. Charge
that full amount also for the fixed q=1 profile. Finally charge780
subtractions for the shared Jhat(1). The total is

    5094+1560+663*58+118*2785+780=374518<380000.       (10)

This count includes all arithmetic in the specified core; assignments,
indexing and storage are not rational operations. Exact rational
numerators/denominators may be large, which is why no bit-cost claim
is made. In particular this is NOT the cost of generating the input
data. At1801, Gauss root/weight computation, certified q and exp values, pi,
Euler's constant and logarithms, the I(1) rule, prime enumeration and
evaluation, A(w), the rest of F(w), outer and final arithmetic all
remained necessary. Even though374518 is below10^6, adding unknown
costs cannot certify the aggregate gate or either complete2^-10
allowance. Evaluation therefore remains stopped at preflight. The1802
extension below pays the core inputs but leaves the aggregate gate open.

`python3 scripts/smoothed-law/direct_positive_real_inner_core_1801.py`
records every rational remainder bound, all29 exact coefficients and
their coefficient-identity checks, the perturbation and propagation
comparisons, and the full core count in
`scripts/smoothed-law/direct_positive_real_inner_core_1801.json`.
The script evaluates neither Gauss samples nor transforms. It verifies
the finite rational comparisons, not the analytic argument or the
qualified source inputs. The canonical analytic/core applications
required separate review, now completed in audit1806 below.

### Costed construction of the core inputs1802

This extension,19 November2026, uses the same saved SPECIALIZE1799
scope. It discharges the finite input contract above, not the rest of
the scalar evaluator. The underlying Gauss-Legendre rule is the standard
named rule used in Johansson,1802.07942v1, Sections2/2.1, cited above:
its nodes are the roots of the Legendre polynomial P_n, and it integrates
polynomials of degree at most2*n-1 exactly. We import that rule, its
orthogonality justification and positivity; we do not reprove it. The
recurrence below defines the standard normalization P_n(1)=1. The source
does not provide this finite operation count or perturbation allowance,
which is why those application details are proved here. No additional
theorem about computing roots or elementary-function library is assumed.

#### Reference roots and weights

Form P_0=1, P_1=X and

    (n+1)*P_(n+1)=(2*n+1)*X*P_n-n*P_(n-1), 1<=n<=12.

For each of P12 and P13, evaluate its dense coefficient polynomial
exactly on j/128, 0<=j<=128. Its six positive sign-changing cells have
the following endpoint numerators:

    P12: (16,17), (47,48), (75,76), (98,99), (115,116), (125,126);
    P13: (29,30), (57,58), (82,83), (102,103), (117,118), (125,126).

The certificate checks all258 values and all these endpoint signs.
Reflection supplies six negative cells in each case; P13 also has the
exact root0. All cells lie strictly inside(-1,1); adjacent cells,
including the central point for P13, have gaps>1/32. The intermediate
value theorem gives12, respectively13, distinct roots. Their count
equals the polynomial degree, so these are all roots and each is
simple. This also proves uniqueness in every seed cell without a
root-finder convergence assumption. There are no other grid zeros.

Refine each positive cell by160 exact bisections, comparing polynomial
signs; if a midpoint is a root, keep that singleton. Output its midpoint
and reflect for the negative roots. The exact and rational approximate
reference roots r_i and rhat_i then satisfy

    |rhat_i-r_i|<=eta:=2^-168,                       (11)

because the initial width2^-7 is halved160 times and then halved once
for midpoint radius. The point0 is exact. The certificate verifies
every final interval, its containment in its seed, and the sign/root
condition. This is exact isolation, not an unchecked floating seed.

For either n, define a polynomial in x by

    L_i(x;r)=product_(k!=i) (x-r_k)/(r_i-r_k).

The exact Gauss weight lambda_i equals integral_(-1)^1 L_i(x;r)dx:
apply the imported polynomial exactness to L_i, whose node values are
the Kronecker deltas and whose degree is n-1. Compute the rational
approximation lambdahat_i by multiplying its n-1 linear numerator
factors with rhat in place of r, integrating the resulting polynomial
coefficient by coefficient, and dividing by the product of the n-1
differences. Thus no additional quadrature-weight formula is needed.

Here is a uniform perturbation bound that includes all weights. Along
the straight segment from r to rhat each coordinate remains in its
seed cell, hence in(-1,1), and all separations exceed1/64. Put m=n-1<=12.
For -1<=x<=1, the numerator of L_i is at most2^m in absolute value,
and its denominator at least2^(-6*m). Consequently

    |L_i|<=2^(7*m),
    |partial_(r_i)L_i|<=2^(7*m)*64*m<2^94,
    |partial_(r_k)L_i|<=2^(7*m-1)+2^(7*m+6)<2^91, k!=i.

The last estimate differentiates the numerator product directly; it
does not divide by x-r_k, which can vanish. The first derivative
differentiates only the nonzero denominator. Integrating over length2
bounds each weight derivative by2^95, so the sum of their magnitudes
is at most n*2^95<2^99. The fundamental theorem of calculus along the
segment and(11) therefore give

    |lambdahat_i-lambda_i|<2^99*eta=2^-69.          (12)

For C033y's four unit inner panels, set

    x_(k,i)=k+(1+r_i)/2, omega_(k,i)=lambda_i/2,
    k=0,1,2,3, n=12,

and make the same affine maps on the rational data. Then
|xhat-x|<=2^-169 and |omegahat-omega|<2^-70, both stricter than2^-60.
The computed nodes are already in[0,4]. Use C033z's already counted
clamping for the weights and Gaussian inputs. For later use the n=13
reference weights are also constructed to(12); no claim about their
propagation through the outer exponent is made here.

#### Elementary exponential and logarithm constructions

Precompute the rational coefficients of

    T40(z)=sum_(k=0)^40 z^k/k!.

For real |z|<=1, Taylor's integral remainder implies
|T40(z)-exp(z)|<=3/41!, using e<3. This elementary remainder is
specialized here, rather than assuming a requested library tolerance.

For each of the48 inner nodes, evaluate T40(-xhat^2/16), clamp to[0,1],
and square four times. The exact exp(-xhat^2/16) belongs to[0,1], so
clamping does not increase its error. The map u->u^16 has derivative
at most16 there. Also the derivative of exp(-x^2) has absolute value
at most8 on[0,4]. Hence the computed Gaussian factor ehat satisfies

    |ehat-exp(-x^2)|<=48/41!+8*2^-169<2^-150.       (13)

Every operation after the input xhat is exact rational arithmetic.
This is a constructive bound on its total error, including its input
perturbation, not merely a Taylor truncation at the true node.

Generate a rational approximation ell to log2 by

    ell=2*sum_(j=0)^63 3^(-(2*j+1))/(2*j+1).

The identity follows by integrating the geometric series for
2/(1-z^2) from0 to1/3, where it converges uniformly. Its omitted
positive tail is at most

    epsilon_log=9/(4*129*3^129)<2^-200.             (14)

For panel index j=0,...,19 and a reference n=13 root r, C033y's
exact outer node has

    -y=log2*(30-7*j/5-7*(1+r)/10).

Form the same expression using ell and rhat, and clamp it to[0,21],
calling the result vhat. The exact v=-y belongs to that interval:
its bracket lies in[2,30] and log2<7/10. Clamping is nonexpansive
relative to v. Since |ell|<1, (11) and(14) give

    |vhat-v|<=30*epsilon_log+(7/10)*eta<2^-160.     (15)

Compute Ehat=T40(vhat/32)^32 with five squarings. Positive Taylor
coefficients give 0<=T40(vhat/32)<=exp(vhat/32). The power difference
bound and the mean value theorem for exp on[0,21] therefore give

    |Ehat-exp(v)|
      <=96*3^21/41!+3^21*(30*epsilon_log+(7/10)*eta)
      <2^-120.                                    (16)

Indeed the polynomial error before taking the32nd power is at most
3/41!, and that power's derivative is at most32*exp(21); exp(21)<3^21.
There are260 such outer values, shared across the three widths and
both s-values. No full scalar is evaluated in this construction.

#### The780 inverse square roots

At each outer node form the three exact rational widths

    what=sigma+Ehat/4, sigma in {1,3/2,2}.

They are at least1, and (16) bounds their errors by2^-122. The
derivative of w^(-1/2) has absolute value at most1/2 for w>=1,
so using what instead of the true w changes q by at most2^-123.

The positive root of what*q^2=1 lies in[0,1]. Bisect that interval64
times: form its midpoint, square it, multiply by what and compare
with1, keeping the appropriate half. Equality may retain either
closed half. The function is strictly increasing for q>0 and the
initial interval contains the root, so no approximate sign decision
is involved. The final midpoint has error at most2^-65 relative to
what^(-1/2). In total

    |qhat-w^(-1/2)|<=2^-65+2^-123<2^-64<2^-60.     (17)

Equivalently one can retain the stronger bound2^-65 plus one eighth
of the right side of(16), as the certificate does. Apply C033z's
already counted panel-dependent clamping afterward; it preserves
the required error because the exact q lies in the prescribed range.
The shared q=1 for Jhat(1) stays exact.

Equations(11)-(17) meet every input obligation of the original core.
There is no source or zero-data assertion in these finite arithmetic
steps; the inherited analytic/law qualifications still govern their
interpretation in the target transforms.

#### Complete additional count and the surviving gate

The cost unit remains one exact rational +,-,*,/ or comparison;
assignments, branches on stored sign flags, indexing and storage are
not rational operations. There is no bit-complexity or runtime bound.
In particular exact rational numerators can become very large. The
following count is for the specified construction, not for the extra
verification operations performed by its certificate script.

- Legendre coefficient recurrence: at most500 operations. Charging four
  per coefficient and three to form the integer coefficients at each
  step gives sum_(n=1)^12 [4*(n+2)+3]=444.
- Two reference scans:7482. Dense Horner uses2*n per point; allowing
  four more for coordinate generation and sign/adjacency decisions
  gives129*(28+30). Initial zero cases are included.
- Root refinements:55680. A midpoint takes two operations, dense Horner
  takes2*n, and at most two rational comparisons determine zero/sign;
  stored sign flags choose the endpoint. Thus6*160*(28+30) suffices.
  Charge100 more for final midpoints/reflections and100 for seed range
  and separation checks (25*2+23*2=96 suffices for the latter).
- All25 reference weights:4439. Negating the roots once costs25.
  For one weight the m linear factors cost sum_(d=0)^(m-1)(2*d+1)=m^2;
  its denominator costs2*m; its even coefficient integral costs
  3*ceil(n/2); and final division costs1. Summing this over n=12,13
  gives4414, before those25 negations.
- Inner affine maps:48*3+12=156. Each node uses add/divide/add; each
  unit weight is halved once and shared by four panels.
- Taylor coefficients:81, allowing40 factorial multiplications and
  41 reciprocal divisions. Do not assume sharing with the old core.
- The48 Gaussian factors:48*88=4224, consisting of a square/division,
  80 Horner operations, two clamp comparisons and four squarings.
- The log2 series: at most400. Form1/3 and1/9; allow five operations
  per term for its integer denominator, division, accumulation and
  power update, plus final multiplication by2 (323 suffice).
- The260 outer arguments and clamps:260*12=3120. Each bracket needs
  at most eight arithmetic operations including multiplication by ell,
  and two clamp comparisons; twelve is a conservative bound.
- The260 outer exponentials:260*86=22360, for range reduction,80
  Horner operations and five squarings per node.
- Width construction:260*4=1040, one shared division by4 and three
  additions per node.
- The780 inverse square roots:780*(64*5+2)=251160. Each bisection has
  two midpoint operations, two multiplications and one comparison;
  the final midpoint costs two more.

The sum is350842; with the old core374518 it is725360. C033z's
clamps are already in the latter count and are not silently omitted.
The input bounds above also cover those clamps. All shared quantities
are explicitly named. No callback is counted as a single operation.

At the1802 stage, only274640 operations remained under the full cap. The constants pi,
gamma_E/log(4*pi), the I(1) rule (including its n=14 inputs), prime
enumeration/logarithms/exponentials, remaining profile terms, outer
factors/weights and their error propagation, and final exponentials
must still be certified. Constructing n=13 reference weights here
does not pay the outer arithmetic. The old core's propagated error
<2^-22 applies with exact remaining coefficients; their errors are
still unpaid. Thus neither complete2^-10 arithmetic allowance nor
the aggregate preflight passes, and no scalar evaluation is authorized
by this result. The remainder may or may not fit; no impossibility
claim about other constructions is made.

`python3 scripts/smoothed-law/direct_positive_real_inputs_1802.py`
saves full reference coefficients, seed/refined root evidence, all25
rational cardinal weights and their exact polynomial-moment checks,
the rational error bounds and operation ledger in
`scripts/smoothed-law/direct_positive_real_inputs_1802.json`.
All20 root-rule checks and18 aggregate comparisons pass. The script
actually constructs only the reference roots/weights; it does not
evaluate the Gaussian/q families, profile callbacks or transforms.
The proof supplies those families' finite construction and cost. These
checks do not constitute an independent audit of this extension,
C033y's analytic application, the old core or external qualifications.

### Remaining arithmetic and complete preflight1803

This extension,19 November2026, finishes the same SPECIALIZE1799 target.
It is a construction and error/cost proof, not an independent audit of
C033y, the1801/1802 work above, or the external source qualifications.
No additional analytic theorem or zero data is imported. We reuse the
Gauss rule cited above; the finite root, series, perturbation and counting
details below are needed because the sources supply none of these costs.
All operations remain exact rational +,-,*,/ or comparisons. Assignments,
stored flags, fixed loop indices and storage are not charged arithmetic;
no transcendental callback or arbitrary-precision bit operation is free.

#### The finite expression being approximated

Write v=-y, E=exp(v), t=1/E, p=sqrt(pi), and D(w)=Jhat(w)-Jhat(1).
For each of C033y's260 exact outer nodes and three widths put

    P32(w)=sum_(n<=32, n prime power) Lambda(n)/sqrt(n)*exp(-w*log(n)^2),
    K=(log(4*pi)+gamma_E+2*Ihat(1))/(4*pi),
    F32(w)=q*exp(q^2/16)/(2*p)-K+log(w)/(8*pi)
                         -D(w)/(2*pi)-P32(w)/(2*pi).       (18)

Here Ihat(1) is precisely C033y's16-panel,14-point exact Gauss sum,
and q=w^-1/2. This finite expression replaces only C033y's adaptive
prime cutoff by32 at every position. Its omitted prime sum is smaller
on the positive real axis than the corresponding adaptive omitted sum:
every summand and every real outer weight/factor is nonnegative. Hence
C033y's entire analytic allowance25/16384 applies to the new finite
outer sums as well. We do not silently treat the two finite sums as
equal. The additional suppression inside P32 below is separately paid
as arithmetic error. All18 prime powers, including higher powers, occur
in this construction. Compact width-one sums still serve the two residual
scalars only with C033y's separate tail/restriction justification.

The bound |F32|<7 has explicit slack. C033y's full-profile bound is6;
its inner-integral error is <2^-16. Its prime bound(13), at N=32,w>=1,
gives omitted unweighted prime sum <exp(-6), since log32>10/3 and
-l^2+3*l/2 is decreasing there. The prefactor is <1/6. Thus
|F32|<6+1/6+2^-16<25/4. This also leaves room for the arithmetic
profile error proved below. The exact outer factors are positive and
sum weight*g_s<13, while sum weight=L<20 and g_s<3, from C033y.

#### Generating the14-point rule for Ihat(1)

Extend the1802 Legendre recurrence by one step to P14. Its seven positive
sign-changing1/128 cells, verified by exact polynomial evaluation, are

    (13,14), (40,41), (65,66), (87,88), (105,106), (118,119), (126,127).

Reflection gives all14 distinct roots, since the polynomial has degree14;
there are no grid zeros. Seed gaps exceed1/32 and all roots lie strictly
between -127/128 and127/128. Repeat160 exact bisections per positive
root. The root-midpoint error is <=2^-168. Generate cardinal-integral
weights exactly as in1802. To cover m=13 factors, along the segment
between exact and approximate roots the cardinal polynomial has modulus
<=2^91 on[-1,1]; its derivative in its own root is <2^101 and in each
other root is <2^98. These follow from separation>1/64, bounding numerator
factors by2, and differentiating numerator products without division by
x-r_k. Integrating over length2 and summing14 coordinate derivatives
gives a bound <14*2^102<2^106. Thus reference weights have error <2^-62.

Map the rule to all16 unit panels. The224 node errors are <=2^-169 and
unit weight errors <2^-63. Clamp weights to[0,1], preserving their errors.
Both true and approximate nodes satisfy1/256<t<16. All coefficient,
sign, seed, refined-interval and cardinal-moment evidence is retained in
the certificate; moment identities alone are not a root-accuracy proof.

#### Stable evaluation of the224 Ihat samples

Let T_m(z)=sum_(k=0)^m z^k/k!, reusing1802's exact coefficient table.
For |z|<=1 its exponential remainder is <=3/(m+1)!. Set tau=3/21!.
For a rational approximate node x, form

    Ahat=clamp(T20(-x^2/256),0,1)^256,
    uhat=clamp(T20(-x/16),0,1)^8,
    hhat=(Ahat-uhat)*uhat/(1-uhat^4).               (19)

All powers are formed by squaring. At the true node h equals
(exp(-t^2)-exp(-t/2))*exp(-t/2)/(1-exp(-2*t)), which is C033y's
combined archimedean integrand. Nothing divergent is separated.
Clamping followed by powers on[0,1], and node perturbation, give

    epsilon_A=256*tau+32*2^-169,
    epsilon_u=8*tau+2^-170.                         (20)

At every node, 1-exp(-2*t)>=2*t/(1+2*t)>1/129>1/256; use exp(x)>=1+x.
Since |uhat^4-u^4|<=4*epsilon_u<1/512, all interpolation segments
between exact and approximate u have denominator>1/512. In the box
0<=A,u<=1 with that denominator lower bound, the partial derivatives of
(A-u)*u/(1-u^4) obey

    |partial_A|<=512,
    |partial_u|<=2*512+4*512^2<2^21.

Consequently each sample error is bounded by
epsilon_h=512*epsilon_A+2^21*epsilon_u. C033y's real integrand bound6
and this error give |hhat|<7. Telescoping first sample values with the
exact weights (sum16) and then the224 weights gives

    epsilon_I=16*epsilon_h+224*7*2^-63<2^-30.        (21)

The denominator test and the last comparison are exact rational checks.
There is no subtraction of an unbounded1/t term and no assumed floating
precision. Equation(21) concerns the finite Ihat sum; C033y's quadrature
and tail errors remain separate.

#### Constants, with constructive radii

For pi use32 terms in each alternating arctangent series in Machin's
identity pi=16*atan(1/5)-4*atan(1/239). To fix the branch directly,
tan(2*atan(1/5))=5/12, tan(4*atan(1/5))=120/119, and subtraction
of atan(1/239) has tangent1 and lies in(0,pi/2). Its value is pi/4.
The alternating-series error therefore gives a rational approximation

    epsilon_pi=16/(65*5^65)+4/(65*239^65)<2^-140.    (22)

In particular3<pihat<4. Bisect x^2=pihat on[1,2]64 times and take
the midpoint. Then |phat-sqrt(pi)|<=2^-65+epsilon_pi/2<2^-64.
All signs are exact rational comparisons.

For Euler's constant use

    gammahat=sum_(k=1)^4096 1/k -12*ell-1/8192,

where ell is1802's approximation to log2 with error epsilon_log<2^-200.
Here is the needed error estimate rather than an unpriced library call.
For f(x)=1/x on[k,k+1], two integrations by parts give the trapezoid
excess as integral ((x-k)*(k+1-x)/2)*f''(x)dx. It is positive and
strictly below(1/8)*integral f''(x)dx. Sum from k=n to N-1 and let
N tend to infinity, using the definition gamma_E=lim(H_N-log N).
The telescoping endpoint term gives

    0<gamma_E-(H_n-log n-1/(2*n))<1/(8*n^2).

Thus epsilon_gamma=1/(8*4096^2)+12*epsilon_log<2^-26.
No zeta estimate enters this elementary constant construction.

To compute log(4*pi), use4*ell+2*sum_(j=0)^15 z^(2*j+1)/(2*j+1),
where z=(pihat-4)/(pihat+4), |z|<1/7. The logarithmic identity follows
by integrating the geometric series, as in1802. Its tail and input error
are bounded by

    epsilon_c_log=49/(24*33*7^33)+4*epsilon_log+epsilon_pi<2^-60.

In this expression pi is approximated by pihat, not phat. Form Khat
using these constants and the computed Ihat in(18). Since |Ihat|<4,
log(4*pi)+gamma_E<4, and3<pihat, the reciprocal perturbation is covered by

    epsilon_K=(epsilon_gamma+epsilon_c_log+2*epsilon_I)/12
                                      +32*epsilon_pi.          (23)

This bound includes perturbation of the denominator. All inverse pi
and inverse phat factors used below are exact rational reciprocals.

#### Prime powers, panel suppression and finite exponentials

Enumerate primes and their powers through32 by the finite sieve described
in the count below. The18 powers are

    2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32.

For each n let k=floor(log_2 n), a fixed integer0<=k<=5, and
z=(n-2^k)/(n+2^k), so0<=z<=1/3. Use

    lhat_n=k*ell+2*sum_(j=0)^31 z^(2*j+1)/(2*j+1).

This is a lower bound for log n, with error at most
epsilon_l=5*epsilon_log+9/(4*65*3^65)<2^-100. Both the k map and
every rational lower logarithm are saved in the certificate. For n=p^a,
the von Mangoldt coefficient uses lhat_p, not lhat_n. Generate n^-1/2
by64 bisections of n*x^2=1 on[0,1], just as in1802. The resulting
coefficient approximation chat_n has error <2^-60 from log(p)/sqrt(n),
because log p<4 and the inverse-square-root error is <=2^-65. Both
exact and approximate coefficients lie in[0,4]. Precompute lhat_n^2.

For panel j=1,...,20 set d_j=floor(28-7*j/5). The true width at every
node is greater than W_(j,sigma)=sigma+2^d_j. Suppress a prime power
throughout that panel whenever W_(j,sigma)*lhat_n^2>=32. This proves
its true exponential argument is >=32. For the other pairs form
xhat=what*lhat_n^2 with1802's rational what. Since what<2^30, log n<4,
and |what-w|<2^-122, the uniform argument error is bounded by

    epsilon_x=16*2^-120+2^30*8*epsilon_l<2^-66.      (24)

If xhat>=32, return zero; otherwise compute
clamp(T20(-xhat/32),0,1)^32 by five squarings. In the latter case the
error from exp(-xhat) is <=32*tau. In the former case the true argument
is >=32-epsilon_x, so its exponential is at most

    2*exp(-32)<2*(3/8)^32<2^-44.

This also bounds all panel-suppressed terms. The true-argument change
cost is at most epsilon_x, since exp(-x) is1-Lipschitz for x>=0.
Thus all18 powers, whether evaluated or suppressed, are covered by

    epsilon_P=18*(2^-60+4*(32*tau+epsilon_x+2^-44))<2^-37. (25)

The fixed panel table requires no individual zero coordinates or profile
values. For panels1-15 no prime slots survive. For panels16-20 the
numbers surviving at sigma=1,3/2,2 respectively are

    j16: 1,1,1; j17: 2,2,2; j18: 8,8,7;
    j19: 14,12,10; j20: 18,18,14.

Multiplying their sum by13 gives1534 potential runtime slots. Some may
also be suppressed by the xhat test; all1534 are charged at full cost.
The complete table of retained powers and every omitted lower exponent
is saved, not merely these counts. The error bound(25) applies to P32,
while C033y's independent allowance still pays the infinite prime tail.

#### Logarithms, pole terms and profile assembly

At each node form that=clamp(1/Ehat,0,1/4). Exact E>=4 and Ehat>3,
so |that-t|<2^-120. The same clamped that is shared by all three widths
and both s-values. With x=4*sigma*that and z=x/(2+x), one has0<=z<=1/2.
Evaluate the16-term atanh polynomial above, now at this z, and form

    logwhat=vhat-2*ell+2*sum_(j=0)^15 z^(2*j+1)/(2*j+1).

The exact identity is log(w)=v-2*log2+log(1+4*sigma*t), with no branch
ambiguity because every input is positive real. Its series tail is at
most1/(99*2^30). The derivative of log(1+4*sigma*t) in t is <=8.
Combining this with1802's v error yields

    epsilon_logw=1/(99*2^30)+8*2^-120+2^-160+2*epsilon_log<2^-35. (26)

For the pole term use qhat*T10(qhat^2/16)/(2*phat), with the already
clamped qhat in[0,1]. The Taylor tail, q sensitivity (<2), and phat
sensitivity give

    epsilon_Apole=2*2^-60+2/(16^11*11!)+4*2^-64<2^-55. (27)

Use the1801/1802 computed D, whose error is <2^-24, and exact rational
assembly of(18). The inverse-pi perturbations are bounded by128*epsilon_pi:
the involved finite log, D and prime sum have absolute bounds23,8,72,
and reciprocal denominators stay above3. Equations(23)-(27) therefore give

    epsilon_F=epsilon_K+epsilon_Apole+epsilon_logw/24
                     +2^-24/6+epsilon_P/6+128*epsilon_pi<2^-22. (28)

This covers all profile arithmetic, including the old core's error;
do not add or silently drop a second copy. By the slack after(18), every
computed profile has absolute value<7. Exact rational arithmetic introduces
no operation-rounding error; these bounds pay all transcendental and
quadrature-input approximations used in the finite expression.

#### Outer weights, factors and final exponential

Reuse the13 reference weights from1802, clamping them to[0,2]. Form
the logarithmic-panel weights as(7*ell/10)*lambdahat. They approximate
the exact weights with error <2^-68: their reference-weight error is
<2^-69, the prefactor is <1/2, and the ell error is <2^-200. They are
positive up to harmless zero clamps and identical across all20 panels.

Generate rhat=T20(vhat/64)^32, shared by the widths and s-values.
Since0<=vhat<=21, positivity of Taylor coefficients and the power
difference bound give

    epsilon_r=96*3^11/21!+3^11*2^-161<2^-40.        (29)

The true r=exp(v/2)<=2^15, so rhat<2^16. At each s in{1,2}, compute
uhat_s=clamp(T20(-s*that),0,1), and then ghat_s=phat*rhat*(1-uhat_s).
Its input is in[-1/2,0], so

    epsilon_outer_exp=tau+2*2^-120,
    epsilon_g=2*epsilon_r+2*2^16*epsilon_outer_exp+2^16*2^-64<2^-35. (30)

This bound permits cancellation in1-uhat_s; its absolute error, amplified
by rhat, has been included. In particular |ghat_s|<4. Sum each finite
outer expression exactly, sharing weight*ghat_s across the three widths.
Telescope the profile error with exact weight*g_s first, then the factor
and weight errors with |Fhat|<7. Using C033y's discrete bound13 gives

    epsilon_B=13*epsilon_F+7*(20*epsilon_g+260*4*2^-68)
             <2^-17<2^-10.                         (31)

The bound is uniform for all six compact sums and both residual uses.
The computed weighted-g sum is <14, so computed exponents have absolute
value<98. Exact target exponents are nonnegative by the retained law
assumptions, and are <13*7+25/16384<128 by(18) and C033y. Clamp the
computed exponent to[0,128]; projection cannot increase its error from
the exact target exponent. To exponentiate a clamped value X, compute

    clamp(T20(-X/128),0,1)^128.

Seven squarings give error <=128*tau=384/21!<2^-10. On[0,infinity)
the map exp(-X) is1-Lipschitz. Therefore every final scalar has error

    25/16384+epsilon_B+384/21! <2^-8.               (32)

Its rational bound is approximately0.00152601626 versus the required
0.00390625; the decimal is only a display of the exact comparison.
Residual and full width-one values may reuse the same compact arithmetic,
but their error assertions refer separately to their distinct exact laws.

#### Complete additional operation ledger

All previous725360 operations remain charged. The following additional
counts include constants, comparisons, coefficient setup, elementary
series, denominators, multiplication by small integers and accumulation.
T10/T20 coefficients reuse the already charged T40 table. Horner of
degree m costs2*m, with no fused operation. Atanh polynomials use z times
a degree m-1 polynomial in z^2 with coefficients2/(2*j+1).

| Remaining work | Upper operations |
| --- | ---: |
| Extend coefficients to P14 |63|
| P14 grid scan |4128|
| Seven160-step positive-root refinements |35840|
| Root midpoints/reflections and seed checks |120|
| All14 cardinal weights |3052|
|224 unit nodes,14 halved weights,224 weight clamps |1134|
|224 Ihat sample evaluations and weighted accumulations |24192|
|4096-term harmonic sum and gamma assembly |8200|
| pi, sqrt(pi), log(4*pi), remaining constants and coefficient tables |1500|
| Prime/power enumeration |2000|
|18 logarithms, inverse square roots, coefficients and log squares |7092|
|60 panel prime schedules |2220|
|1534 selected prime slots |81302|
|260 reciprocal t values and clamps |780|
|780 log(w) evaluations and260 shared bases |28340|
|780 pole terms |18720|
|780 profile assemblies |5460|
|260 outer r factors |11960|
|520 outer Laplace factors |23400|
| Shared phat*rhat and520 g products |780|
|13 outer weights and clamps |60|
|520 weight*g products and1560 weighted accumulations |3640|
| Eight final clamps and exponentials |424|
| **Additional total** |**264407**|

Here are the per-entry algorithms behind the ledger. P14 coefficients
cost4*15+3; each scan/refinement costs28 Horner operations and at most
four coordinate/sign operations. A cardinal weight costs13^2+26+21+1,
plus14 shared root negations. The120 allowance covers seven midpoints,
their reflections and all14 ranges/13 gaps. Unit-node maps use three
operations each, weights one division each and clamps two comparisons.
In(19), Ahat costs53 (square, negate, divide,40 Horner, two clamps,
eight squares); uhat costs47 (negate, divide,40 Horner, two clamps,
three squares). The denominator, numerator, division, weight product and
accumulation cost eight more, totaling108 per sample.

The harmonic sum uses8192 reciprocal/add operations and at most eight
for its assembly. The1500 shared-constant allowance covers96 operations
for32 atanh coefficients; at most128 for arctangent coefficients,
130 for its two evaluations and three for Machin assembly;258 for the
sqrt(pi) bisections/midpoint;37 for log(4*pi); and fewer than100 for
all remaining factors, fixed sigma multiples and K assembly. This sum
is below852, leaving slack inside that allowance. No harmonic or
transcendental constant is merely read as a free approximate literal.

For enumeration, sieve p=2,...,32 with stored flags; at each unmarked p
mark multiples using addition/comparison and then generate its powers
using multiplication/comparison. Even charging all31 p values at16
multiple iterations, five power iterations, setup and loop arithmetic
uses fewer than2000 operations. For each of the18 fixed n values the
dyadic k and2^k are fixed table data; the logarithm uses at most70
operations, its inverse-square-root construction322, and coefficient
and logarithm-square formation two. The schedule uses60 lower-width
additions and1080 multiply/compare pairs; d_j is a fixed panel table
and its powers of2 reuse1801's table. All suppressed-exponent decisions
are charged once. A selected runtime prime slot costs one argument
product, one threshold comparison,49 for range reduction/negation,
40 Horner operations/two clamps/five squares, and two for coefficient
multiplication and accumulation:53 total. Suppressed branches cost less.

Each log(w) needs four operations through z^2,30 Horner, one final z
product and one base addition:36. Each pole term needs q^2 and division,
20 Horner operations and two products:24. Profile assembly uses three
coefficient products and four additions/subtractions. Each r factor costs
one range reduction,40 Horner and five squares:46. A Laplace factor costs
s multiplication, negation,40 Horner, two clamps and subtraction:45.
Outer weight construction costs at most41 operations, covered by60.
Each weighted accumulation costs one product and one addition. Each final
value costs two X clamps, division/negation,40 Horner, two polynomial
clamps and seven squares:53. Sharing is only the sharing explicitly stated.

The result is725360+264407=989767<=10^6, with10233 operations of slack.
The cap is an algebraic-operation cap under the stated model. Exact
rational numerators can become enormous; this is not a usable bit-time
or memory bound. Certificate-generation and independent verification
operations are not the evaluator whose cost is claimed. No scalar or
profile callback was actually evaluated during this preflight.

Run `python3 scripts/smoothed-law/direct_positive_real_completion_1803.py`.
Its full certificate is
`scripts/smoothed-law/direct_positive_real_completion_1803.json`.
It checks all14 root intervals and14 exact cardinal moments, nine root
conditions and25 aggregate comparisons, including every suppressed
panel exponent, both arithmetic allowances and the complete count.
It actually constructs only the P14 reference rule and finite prime
log/suppression table. The recorded rational evidence supports the
inequalities used here; it is not an independent audit of the proof,
the earlier constructions, the counting/divisor inputs or finite-zero data.
At construction1803, transform evaluation required an independent audit
of the complete application, especially(18)'s cutoff change, the nearby
denominators in(19), every operation category and the outer propagation.
Audit1806 below supplies that qualified application review.
No interpolation, conditioning, TV<=2, cancellation, signed-height or
actual-Xi positivity conclusion follows from this preflight.

### Complete application audit1806 — 19 November2026

Verdict: the specified sufficient preflight passes under the unchanged
external qualifications and operation model. This is local REPRODUCTION
under the separately approved SPECIALIZE1803 target, not a new general
numerical theorem, source-wide verification or actual scalar evaluation.
C033y's analytic application is audited in its canonical audit1806.
The historical1801-1803 certificates remain unchanged.

**Core and input construction.** Coefficient comparison in2*S*R proves
the polynomial recurrence, including the removable value1/4. Its disk
bound and Cauchy tail apply on x*q<=1 only on the first17 panels;
the remaining117 profiles and Jhat(1) use the quotient on[0,4].
Its denominator2*S10>=2 is independent of the small argument. The
separate dS/4 maximum for the T tail is not a pointwise division by z.
Telescoping with exact weights first, then perturbed arguments and
weights, gives the displayed387*delta and900*delta bounds. The shared
moment rearrangement is a finite polynomial identity also for the
perturbed data. No additional moment-rounding error is required in
the declared exact rational model. The computed D error is included
once, in(28), and is not lost when the outer coefficients change.

All39 reference roots and weights were checked from complete stored
data, not from their Boolean summaries. The audit program independently
forms P12,P13,P14 by Rodrigues' formula, checks each stored coefficient,
endpoint value, seed containment, root sign and midpoint radius, and
reconstructs each cardinal integral by polynomial convolution. Distinct
brackets and degree give uniqueness and simplicity; moment identities
alone would not. The seed separation keeps all denominators nonzero
along the straight perturbation segment. Differentiating the numerator
as a product avoids division by x-r_k. The integrated gradient bounds
2^99 and2^106 give the asserted weight accuracies. Affine maps, clamping,
positive Taylor series and exact-sign bisection then preserve(11)-(17).
The inputs' mathematical constructors are audited; their full780-value
execution was not performed.

**The completed profiles.** The finite expression(18) has the same
normalization as C033u(5) after C033y's regularization. Using all18
prime powers through32 only reduces the omitted-prime component;
the other signed quadrature errors are still paid separately. For(19),
t>1/256 implies1-exp(-2*t)>1/129. The bound4*epsilon_u<1/512
therefore keeps the full segment between true and approximate u at
denominator>1/512. The two partial-derivative bounds consequently apply
throughout the segment, including its A coordinate; (21) includes all224
weight errors as well as sample errors. A small value of t is not
replaced by a floating nonzero-denominator test.

Machin's branch is fixed in(22). The trapezoid identity for1/x gives
the stated sign and1/(8*n^2) bound for gamma_E; the endpoint correction
is -1/(2*n), not +1/(2*n). The log(4*pi) series uses pihat, and log(w)
uses v-2*log2+log(1+4*sigma*t), so neither substitution loses a factor2
or a square root. All divisions stay in their stated positive ranges.
For the reciprocal-pi perturbation bound one may justify |D|<8 directly
from |J(w)|,|J(1)|<3 and(7); the finite quadrature values need not be
bounded by the integral without its error. The conservative bounds23,8,72
in(28) are thus valid, with slack for their input errors.

The independent verifier factors every integer through32 and reconstructs
each lower logarithm, including the base-prime von Mangoldt weight.
It checks the full60-by18 schedule: kept and omitted sets partition
the18 powers and every omitted lower argument is at least32. There
are1534 potential runtime slots. For their additional threshold test,
|xhat-x|<=epsilon_x<2^-66 gives x>=32-epsilon_x whenever xhat>=32.
Thus the2*exp(-32) bound covers both suppression mechanisms. The
surviving Taylor evaluations include argument and coefficient errors.
The independent infinite tail remains in C033y's analytic allowance.

**Outer propagation and cost.** In(30), cancellation in1-uhat_s is
paid by absolute error amplified by rhat<2^16. In(31), telescope the
profile error with exact weight*g_s first; then use |Fhat|<7 for the
factor and weight perturbations. This order pays cross terms without
an assumed exact approximate-weight sum. Nonnegative exact exponents
come from the qualified laws. Their upper bound<128 justifies the
two-sided clamp before the final Taylor/power exponential; the exact
residual and width-one laws retain separate tail assertions.

The operation ledger was checked against the displayed algorithms, not
only its total. Coefficient reciprocals are reused when forming E_n;
the high-width moment rule and low-width quotient cost58 per Horner
profile and58 per inner sample, respectively. Gaussian range reduction
can divide the square by -16 in one operation, as charged in1802.
Cardinal polynomial multiplication costs m^2 using the shared negated
roots. Scans and bisections include exact comparisons; fixed loop indices
and stored sign flags have the expressly excluded administrative cost.
The224 combined Ihat samples cost108 each, the1534 possible prime slots
53 each, including their runtime-suppressed members. Panel suppression
is paid separately in the60-by18 schedule.
The1500 constant allowance covers its listed subroutines with slack;
node/weight clamps, profile assembly, outer products and the eight final
exponentials remain charged. No expensive transcendental callback is
counted as one operation. The three subtotals are374518,350842,264407,
giving989767<=10^6 with10233 slack. Certificate verification itself is
outside this evaluator ledger, as are bit complexity, memory and time.

Run `python3 scripts/smoothed-law/direct_positive_real_audit_1806.py`.
Its full independent certificate is
`scripts/smoothed-law/direct_positive_real_audit_1806.json`, including
input hashes, all1380 check results and exact rational load-bearing bounds.
There are no failed checks. The exponent arithmetic bound is less than
1.374e-7<2^-17<2^-10; final exponential error is384/21!<2^-10.
Their exact sum with25/16384 is less than0.001526017<2^-8. These
decimal inequalities are rational comparisons, not sampled evidence.
Both reserved2^-10 allowances also survive unchanged. No correction
to the radius or count was required. The certificate verifies finite
evidence; the preceding mathematical checks supply the analytic and
operation-model interpretation. No conditioning, TV certificate, full
observation-interval approximation, signed-height payment, cancellation,
realization or actual-Xi positivity is established.

### Ihat-only block rounding1810

This19 November2026 extension specializes the prior SPECIALIZE1809
assessment. It changes only the accumulation in(21), not(19)'s samples,
their weights, their order, the reference rule, or any other arithmetic.
The original exact construction and its audit1806 remain unchanged.
The source coverage is Johansson, *Arb: Efficient Arbitrary-Precision
Midpoint-Radius Interval Arithmetic*,
[arXiv1611.02831v1, Sections3.1.1-3.2 and5-5.1, pp5-8](https://arxiv.org/pdf/1611.02831v1),
and the inspected Arb2.23.0 [enclosure and quotient contracts](https://arblib.org/arb.html),
as recorded in source-notes1809. Import their enclosure/error-propagation
principles, without treating an Arb operation as a rational primitive.
The specialization below is necessary because those general contracts
do not pay rational conversion or this evaluator's operation cap.

**Range and conversion.** Enumerate the224 computed exact rational
weighted samples in their prescribed panel/node order as v_i. By(19)-(21)
and clamping, each weight lies in[0,1] and each computed sample has
absolute value<7, hence |v_i|<7. Write T_n=sum_(i=1)^n v_i for the
original exact accumulation. Set eta=2^-32 and R_0=0. For r=1,...,56
form, using four of the already charged additions,

    S_r=R_(r-1)+v_(4r-3)+v_(4r-2)+v_(4r-1)+v_(4r).

To obtain R_r, initialize a=-2048,b=2048. Repeat43 times:
form m=(a+b)/2, compare S_r>m, and replace a by m if true,
otherwise replace b by m. Finally set R_r=(a+b)/2. This rule uses
only rational addition, division and comparison, with assignments free
under the original model. No floor, integer quotient/remainder, bit
access, approximate library operation or fused operation is used.

For any S_r in[a,b], each branch retains containment and halves the
interval width, including equality at a midpoint. After43 bisections
the width is4096/2^43=2^-31. The final midpoint has error<=eta and
is an integer multiple of2^-32: all endpoints are initially integers,
and each successive spacing is half the previous spacing, so after43
steps endpoints are multiples of2^-31 and the final midpoint is on
the half-spacing grid. Thus its reduced denominator divides2^32.

Here the input-range requirement is proved, not tested at runtime.
Induction gives |R_(r-1)-T_(4r-4)|<=(r-1)*eta, and therefore

    |S_r|<28*r+(r-1)*eta<2048, 1<=r<=56,
    |R_r-T_(4r)|<=r*eta.

Indeed |T_(4r)|<28*r, the previous error is unchanged when adding
the four exact v_i, and the conversion adds at most eta. The displayed
range follows from28*56+55*2^-32<2048 and closes the induction.
In particular, with I_old=T_224 and I_new=R_56,

    |I_new-I_old|<=E=56*2^-32.                       (33)

The input range also bounds every checkpoint output by1568+56*eta<2048.
This bounds its numerator by2^43 in magnitude on the2^-32 grid;
it supplies no bound on the bit cost of exact samples, block sums,
or any other constructor. Four-sample blocks can still be expensive.

**Propagation to the eight scalars.** Compare the original exact
arithmetic evaluator and this changed evaluator using identical inputs
everywhere else. Both use the same pihat>3 from(22). Formula(18)'s
computed K changes by exactly (I_new-I_old)/(2*pihat), so

    |K_new-K_old|<E/6,
    |F_new(w)-F_old(w)|<E/6.                        (34)

There is no extra reciprocal perturbation: pihat is identical in the
two evaluators, and its original error remains paid by(23),(28).
The original finite-profile bound |F32|<25/4 and epsilon_F<2^-22
give |F_new|<25/4+2^-22+E/6<7. Thus the profile range used in(31)
is preserved. The computed weights and g factors are unchanged and
nonnegative, and their sum is <14 as proved immediately after(31).
Summing(34) with these computed weights proves a uniform additional
error <14*E/6 for each computed compact exponent. Combining this
comparison with the original epsilon_B<2^-17 gives

    exponent arithmetic error
       <beta=2^-17+(14/6)*56*2^-32<2^-10.          (35)

All six width/s-value exponents use the same changed K; the two residual
uses retain their separate analytic tail justifications from C033y.
No equality of their exact exponents is assumed. The exact target
exponents still lie in[0,128]. Clamping both computed exponents to
that interval is nonexpansive, so the unchanged final exponential
constructor still has error<=384/21!<2^-10 and(32) becomes

    scalar error<25/16384+beta+384/21!
                 <0.001534<2^-8.                 (36)

The decimal comparison is the exact rational bound767/500000;
it is not an evaluation of a scalar. This argument propagates the
new error in addition to the old arithmetic error, rather than
reusing(21),(23),(28) unchanged for the rounded sum. In particular
I_new has error at most epsilon_I+E from the exact-node finite Ihat.

**Cost and limits.** Each bisection costs one addition, one division
by2 and one comparison, hence three operations. Its final midpoint
costs two. Each conversion therefore costs43*3+2=131 operations,
independently of its branch choices. The value2048 is the already
charged2^11 in the original power table; generate -2048 once by one
subtraction from zero. Endpoints are reset by assignments. All224
original weighted products and additions remain charged, with the
same initial zero accumulator and four additions in every block.
There are no runtime range tests or error-bound updates: their
uniform bounds are proved above, so no such arithmetic is omitted.
Fixed loop indices, branch flags and storage remain administrative,
as in the original ledger. The additional and full upper counts are

    1+56*131=7337,
    989767+7337=997104<=10^6, slack2896.            (37)

This is an inherited full-construction upper ledger plus an explicit
conversion charge, not an instrumented completed-run count. All other
denominator growth, runtime, memory and exact constructor costs in
bits remain unbounded. It does not turn the preserved1808 partial
prefix into a completed Ihat value or a scalar certificate.

Run `python3 scripts/smoothed-law/direct_positive_real_ihat_rounding_1810.py`.
Its certificate is
`scripts/smoothed-law/direct_positive_real_ihat_rounding_1810.json`.
It checks every block's rational range/error bounds, the count and
allowances, and eight conversion boundary cases. Boundary cases
supplement the universal containment/induction proof above; they do
not verify it by sampling. No actual Ihat sample or scalar is executed.
This is local REPRODUCTION of known enclosure principles with a new
finite cost specialization, not progress beyond their general scope
or an RH candidate. At construction1810 an independent application audit
remained pending; audit1812 below supplies that review.

### Independent Ihat-rounding application audit1812

Verdict,19 November2026: the1810 rounding modification passes the
approved application audit, with no correction to(33)-(37). This is
local REPRODUCTION under the prior SPECIALIZE1810 assessment and its
separate scope approval1811. It verifies the finite specialization of
the enclosure principles cited above; it supplies no result beyond
those general sources or new bound beyond1810. Audit1806's unchanged
analytic/arithmetic inputs and ledger are retained, rather than inferred
from rounded boundary tests. All external qualifications in Hypotheses
remain in force; no source-wide or finite-zero validation is asserted.

**Universal conversion and range.** For any rational S in[-2048,2048],
the midpoint comparison preserves a<=S<=b: the strict-upper branch
keeps[m,b], and its complement keeps[a,m]. Equality keeps S as the
right endpoint, while either initial endpoint is retained on every
applicable branch. After k bisections, the width is4096*2^-k and the
endpoints lie in -2048+(4096*2^-k)*Z. At k=43 this is the2^-31
grid; the midpoint therefore lies on the2^-32 grid and has error at
most2^-32, including endpoints and ties. This proof applies to every
input in the initial interval, independently of the eight test cases.

The actual input lies there because the induction compares R_(r-1)
with the exact prefix T_(4r-4), not with an independently rounded
sample. Each v_i is unchanged and |v_i|<7 follows from(19)-(21) and
its clamped weight. Adding four v_i preserves the prior absolute
error; |S_r|<28*r+(r-1)*eta<=1568+55*eta<2048. Conversion adds
at most eta, closing the induction for every1<=r<=56. Thus(33)
and the denominator/numerator statements hold universally. In
particular the comparison-based conversion introduces no uncharged
integer rounding primitive. It controls the stored checkpoints only;
the rational block inputs and exact samples can have large denominators.

**All eight uses.** Formula(18) is evaluated with rational field
operations after its constructors. Hence changing only Ihat changes
K by exactly Delta_I/(2*pihat) and every assembled profile by its
negative, with pihat>3 unchanged. This proves(34) without another
denominator-perturbation charge. The new profile bound is below7.
To check the computed coefficient sum, let a_l,g_l be exact outer
weights/factors and let ahat_l,ghat_l be the unchanged computed ones.
They are nonnegative. For each s, sum a_l*g_l<13, sum a_l<20,
|ghat_l-g_l|<=epsilon_g, |ahat_l-a_l|<2^-68 and |ghat_l|<4.
Telescoping with exact a_l first gives

    sum ahat_l*ghat_l
       <13+20*epsilon_g+260*4*2^-68<14.

This covers all260 terms; an integral bound or positivity alone
would not establish it. Summing the constant profile change with
these computed coefficients gives the additional exponent bound
14*E/6, without dropping weight-error cross terms. The inherited
epsilon_B<2^-17 and this additional bound give(35). They apply to
the six full laws (two s-values, three widths) and to the two residual
uses of the width-one compact sums. The residual exact exponents
remain distinct: their individual analytic25/16384 allowances use
C033y's restriction outside[1,3/2], with1/4<1. No equality of full
and residual transforms is used.

For each of these eight targets, the retained law assumptions and
analytic allowance put the exact exponent in[0,128]. Projection of
the computed exponent onto[0,128] is nonexpansive relative to that
target; exp(-x) is1-Lipschitz there. The unchanged Taylor/power
constructor costs its original charge and has error384/21! even
at the new input. Consequently(36) follows by the triangle inequality.
The two2^-10 arithmetic allowances are separately preserved. Neither
sampled positivity nor any claim about the exact zeros is added.

**Cost and independent finite evidence.** The four additions per
block are precisely the224 original accumulator additions; their
replacement inputs do not change the rational-operation count.
Each conversion always executes43 additions,43 divisions,43 comparisons
and two midpoint operations, for131. Initial endpoint resets and
branch assignments use the same administrative exclusions as1806.
The shared positive2048 is in the original power table; one subtraction
forms its negative. There is no runtime induction/radius tracking or
range test in the specified evaluator. Thus the additional count7337
and full inherited upper ledger997104, with2896 slack, are correct in
the stated model. This audit does not verify a completed-run count,
the bit cost of a rational operation, memory, or practical runtime.

Run `python3 scripts/smoothed-law/direct_positive_real_ihat_audit_1812.py`.
The full independent certificate is
`scripts/smoothed-law/direct_positive_real_ihat_audit_1812.json`.
The auditor imports no original mathematical program, reads and checks
all56 stored block rows, reconstructs all eight boundary outputs via
an independent exact grid-cell formula, and compares every1810 bound
and operation field. It checks the inherited1806 bounds used here and
records all eight scalar uses with the separate residual qualification.
Its integer cell calculation is verification work outside the evaluator
ledger; it is not a substituted conversion algorithm. All205 exact
checks pass, with no failures. The exact conservative exponent bound
is displayed as7.659817736e-6<2^-10 and the scalar radius bound as
0.001533538724<0.001534<2^-8. These are displays of rational
comparisons, not evaluated scalar enclosures. No Ihat sample, completed
Ihat value, scalar, interpolation or TV certificate was produced.
The mathematical induction and propagation above, rather than the
finite cases, establish the universal application. All prior exact
prefixes, source qualifications and independent RH gaps remain.

### Completed rounded Ihat execution1814

Under the separately approved SPECIALIZE execution assessment1812/1813,
the unchanged224 exact samples(19), weights/order and56 conversions(33)
were executed. The resulting finite rational input is

    I_new=-1252177417/4294967296.

Every saved sample was independently replayed by integer Taylor/power,
denominator, combined-quotient and weighted-product identities. Every
four-term block input was replayed by an integer common-denominator
identity including its previous rounded output; all43 strict branch
decisions and the final cell/midpoint were checked independently. The
saved P14 coefficients were reconstructed by Rodrigues, all14 root
brackets/cardinal weights/moments checked, and the rule compared with
the audited1803 exact data. The previously unused22nd1808 sample was
also replayed by complete equality with its newly checked counterpart.
Thus this is evidence for the entire finite input, not a decimal preview.
The already proved induction(33) gives

    |I_new-I_old|<=56*2^-32=7/536870912,

where I_old is the unchanged exact accumulation of the computed weighted
samples. Equation(21)'s original sample/weight error remains separate,
as do C033y's analytic quadrature/tail errors. No scalar is evaluated.

The600-second first segment retained151 samples/37 checkpoints and
stopped operationally. Continuation1814c reused its first148 samples/37
checkpoints by hashes and completed the remaining76 samples/19 conversions
in298.852seconds, without overwriting the unfinished block. The prescribed
Ihat kernel costs32663 operations:1134 maps/clamps,24192 sample/weighted
additions,7337 shared-negation/conversions. Instrumentation recorded22038
operations in the first segment and11092 in the continuation, totaling
33130; the excess467 is452 abandoned-block operations plus15 repeated
setup operations. Categories and continuation accounting are independently
checked. These counts cover the prescribed kernel; validation, exact
serialization, hashing and replay are separate verification work. The P14
rule/coefficient table is reused, not measured as fresh generation here.
The full997104 ledger remains inherited; this is no completed-run scalar
cost, bit-time bound, source-wide validation or RH-gap closure.

The executor is `scripts/smoothed-law/direct_positive_real_ihat_execution_1814.py`;
its two execution indices are the matching1814 and1814c `.json` paths.
Independent replay is
`scripts/smoothed-law/direct_positive_real_ihat_replay_1814.py --index scripts/smoothed-law/direct_positive_real_ihat_execution_1814c.json --suffix <fresh-suffix>`
(invoke with `python3`). The completed certificate is
`scripts/smoothed-law/direct_positive_real_ihat_replay_1814fast.json`:
2449 exact checks,224 samples,56 checkpoints, no failed identity.
The replay imports no evaluator; installed GMP accelerates exact gcd only,
with its library/header hashes and five bridge comparisons recorded.
It changes neither the identities nor any evaluator arithmetic/cost.
The slower replay's25-sample/6-checkpoint partial certificate is preserved.
A path-metadata setup failure before continuation arithmetic is retained
in `scripts/smoothed-law/direct_positive_real_ihat_execution_1814b/setup_failure.json`.
All source, zero-data and law qualifications above remain unresolved.

### Remaining exact execution1816: saved and replayed prefix

Under SPECIALIZE execution assessment1814, separately approved1815,
the remaining evaluator reused the completed rounded Ihat1814 and
the unchanged1808 nodes, Gaussian factors and moments. All other
arithmetic was exact Python Fraction; no further rounding or mathematical
constructor was introduced. Constants(22)-(23), all18 prime-power
coefficients/logarithms, all60 complete suppression schedules, all48
fixed Jhat(1) quotient summands and their48 partial sums, and all29
coefficient/moment products(3) completed. Their full rational values
are in `scripts/smoothed-law/direct_positive_real_remaining_execution_1816/`.
In particular `shared_core.json` contains the exact computed fixed sum,
coefficients and d_k, not a decimal preview or an exact-integral claim.

The first outer node's vhat, Ehat, that and rhat also completed and
are saved in `outer_inputs_000.json`. Its Ehat numerator/denominator
have681296/681266bits; the computed reciprocal t has681296 denominator
bits. The one
300-second segment stopped at300.007seconds during the first node's
outer g factors, before any complete profile or scalar. No completed
factor is certified from an unfinished operation. This is an operational
limit, not a rational-arithmetic lower bound or a failed analytic estimate.

Independent replay passed579 exact checks in9.136seconds: integer
series/Taylor identities, dyadic bisection-cell inequalities, each fixed
quotient identity and every fixed prefix's common-denominator sum, each
coefficient's defining identity and moment product, and the complete
first outer input. The verifier imports no evaluator; its gcd-only GMP
acceleration retains the already recorded bridge/header/library checks.
Its final coverage assertion accounts for every saved constructor
artifact. Separate lineage verification passed170 checks, binding reused
1808 artifacts to their original hashes and the1814 input index to its
completed replay, and checking all1816 replay-input hashes. Thus the
completed finite prefix is replayed; absent stages are not inferred.

Run the matching `direct_positive_real_remaining_execution_1816.py`,
`direct_positive_real_remaining_replay_1816.py` and
`direct_positive_real_remaining_lineage_1816.py` under
`scripts/smoothed-law/` with `python3`; their matching `.json` files
retain complete outcomes. Scripts refuse to overwrite existing evidence.
The executor additionally saves stage labels, artifact hashes and reuse
accounting. Its prefix is uninstrumented:997104 remains the inherited
full-construction upper ledger, not a measured full scalar count. The
historical Ihat kernel's32663 required operations,452 abandoned operations
and15 repeated setup operations remain separately recorded; fresh1816
setup, serialization and replay are not silently included in that number.

This is partial execution/REPRODUCTION, not a new analytic bound or an
RH candidate. Zero of780 profiles and zero ofeight scalars completed.
The two2^-10 allowances and radius(36) apply only after their prescribed
remaining stages finish; no scalar enclosure or full executed-cap claim
is made here. All source/zero-data/law qualifications, interpolation,
conditioning, weights, TV, full observation coverage and actual-Xi gaps
remain. No dependency or main assembly changed.

### Exact GMP execution1823: partial data, no scalar certificate

This implementation attempt reuses SPECIALIZE assessment1816, repaired1822,
without changing the mathematical evaluator. The imported primitive semantics
are GNU MP6.3.0, *Rational Number Functions*, Sections6.1 initialization and
canonicalization,6.3 arithmetic,6.4 comparison and6.6 I/O, integer-transfer
Sections5.2/5.4, and Section2.2 ABI and ISA; see primary applicability limits
in that assessment. These API specifications are not a speed theorem.

The1823b executor extracts the original Horner, power, clamp, inverse-root,
atanh-series, quotient and serialization functions and the1816 tail as ASTs,
binding every rational constructor to GMP. The sole arithmetic-tail rewrite
loads the already replayed first outer input instead of recomputing it.
Constants, prime schedules and shared core are restored from1816 and their
costs remain charged. The original tail AST and every source/input hash are
saved. A compiled probe verifies the installed header/library version6.3.0
and the ctypes sizes, field offsets and64-bit limb layout. Raw assignments
are canonicalized; zero divisors are rejected; integer transfer is lossless.
This confirms local compatibility, not source-wide correctness.

One300-second segment (301.980seconds including setup) saved15 complete
profiles, all inputs/factors for six outer nodes, and the sixth node's first
width core/log-prime data. It stopped during profile assembly before the
sixteenth completed profile. No final scalar was computed. The instrumented
8776 fresh returned operator calls include numeric-key equality comparisons;
they exclude reused constructors and serialization/verification. One addition
was in flight. This is not a full required-path count or a cap certificate.
The997104 upper ledger, both2^-10 allowances and radius(36) are unchanged;
none is asserted as an executed scalar enclosure.

Preserved debugging runs1823/1823a stopped at an unhashable instrumentation
lookup and a missing restored coefficient table, respectively. Run1823a's
three saved artifacts passed173 independent Fraction/integer-identity checks,
including both first-node g factors and the width-one core. These errors
were repaired in a distinct executor; no failed run or old evidence was
overwritten. The subsequent1823b replay uses direct monomial and
common-denominator identities, dyadic root-cell inequalities and explicit
accumulator cross-products, with GMP on integer-valued rationals for the large
identities. It imports no evaluator. Its certificate distinguishes completed
checks from complete artifact coverage; interrupted replay certifies neither
absent checks nor a full prefix.

Replay1823b stopped after its300-second segment (302.219seconds including
setup), with378 completed checks and no failed check,26 artifacts replayed
and six complete profile/accumulator states verified. It was checking
`profile_002_1_1.json` when interrupted. The nine other complete profiles and
all later saved stages are not thereby replayed; none may be used as a
verified input on the strength of this certificate. This is explicitly
`TIME_LIMIT_PARTIAL_GMP_PREFIX_REPLAY`, not a complete-prefix pass.

Execution scripts and certificates have stems `gmp_remaining_execution_1823`,
`gmp_remaining_execution_1823a`, `gmp_remaining_execution_1823b`,
`gmp_remaining_replay_1823` and `gmp_remaining_replay_1823b` under
`scripts/smoothed-law/`. Full exact values are in the corresponding executor
directories. This is partial REPRODUCTION, not a new mathematical bound or
an RH candidate. Further unrounded execution is parked after this bounded
attempt; the operational limit proves no bit-cost lower bound. A proposed
different width constructor requires its own source review and later proof.
All original law/divisor/source qualifications and the independent
conditioning, weights, TV, observation, signed-height and actual-Xi gaps remain.

### Optional width-only Newton replacement1825

**Hypotheses and conclusion.** Supply an exact rational width W with
1<=W<=2^30, under the operation model above. The following constructor
returns a positive rational Q with

    0<=W^(-1/2)-Q<2^-65

using at most94 defined operations, including initialization, all required
comparisons, small-constant formation, rescaling and two clamp comparisons.
The displayed one-sided bound concerns Q before the optional panel clamp.
For a true C033y width w and its1802 approximation W=what, the final clamped
output has error at most2^-65+2^-123<2^-64<2^-60 relative to w^(-1/2).
This meets the approved100-operation/error2^-60 target. It preserves(17)'s
stronger allowance. It does not change the historical bisection algorithm,
the full evaluator ledger, any existing execution artifact or its replay
boundary. Other rounding and a new full-evaluator ledger require separate
assessment. Only the finite width constructor is established here.

**Imported theorem.** Use Richard P. Brent and Paul Zimmermann,
*Modern Computer Arithmetic*, version0.5.9,7 October2010,
[Lemma3.14, printed p112 (PDF p128)](https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf).
For a,x>0, rho=a^(-1/2), and

    x'=x+(x/2)*(1-a*x^2),

the theorem states

    0<=rho-x'<=(3*x^3/(2*theta^4))*(rho-x)^2,
    min(x,rho)<=theta<=max(x,rho).

Only this exact-arithmetic error theorem is imported; its general proof
is not reproduced. Algorithm3.9/Lemma3.15, integer rounding and any
approximate optimal-seed analysis are not used. The specialization is
necessary because that theorem supplies neither our rational initializer
nor our stopping index or operation ledger.

**Initialization and normalized interval.** Fixed literals0 and1 and a
fixed unrolled control schedule are permitted; assignments/indexing are
free in the existing model. Form2=1+1,3=2+1,4=2*2 and1/4=1/4, charging
four operations. Check W>=1. Set a=W,h=1. In each of15 fixed slots,
compare a with1. If a<=1, leave the normalization loop; otherwise replace
a by a/4 and h by h/2, charging both divisions. After that loop check
a<=1. The upper input bound guarantees this final check passes, since
4^15=2^30. No power, floor, bit access or large literal is generated by
the constructor. These input bounds are hypotheses; the final check also
rejects a width exceeding4^15.

If k divisions were performed, a=W/4^k,h=2^-k and W=a/h^2.
For k=0, W>=1 and the stopping condition give a=1. For k>0 the
last division started with a>1, giving a>1/4; the stopping condition
gives a<=1. Thus always1/4<a<=1,0<h<=1,0<=k<=15. Equality W=4^j
stops at a=1,k=j, including W=1 and W=2^30; widths immediately
above a normalization boundary cause one more division and still satisfy
the strict lower bound. For uniform estimates it is safe to use the
closed enlarged interval1/4<=a<=1.

**Iterations and uniform error.** Initialize x_0=1 and perform exactly
eight steps, each in the five separately charged operations

    u=x*x; v=a*u; z=3-v; p=x*z; x=p/2.

This is the cited Newton update by algebraic identification. Put
rho=a^(-1/2) and e_n=1-x_n/rho. Initially1<=rho<=2 and
0<=e_0<=1/2. For r=sqrt(a) in[1/2,1], the first update gives

    x_1/rho=(3*r-r^3)/2.

The derivative of this last polynomial is3*(1-r^2)/2>=0 on that
interval; its endpoint values are11/16 and1. Hence x_1>0 and
0<=e_1<=5/16. This calculation verifies the local initializer, not
a replacement proof of the imported general Newton theorem.

Suppose x_n>0 and0<=e_n<=5/16 for n>=1. Then x_n<=rho, so
a*x_n^2<=1, and the displayed update gives x_(n+1)>=x_n>0.
The imported theorem, using theta>=x_n, yields

    0<=e_(n+1)<=3*e_n^2/(2*(1-e_n))<=(24/11)*e_n^2.

Since(24/11)*(5/16)=15/22<1, this also preserves
0<=e_(n+1)<=5/16 and justifies every subsequent theorem application.
Writing c=24/11, induction on these seven subsequent steps gives

    e_8<=c^(-1)*(c*e_1)^128
        <=(11/24)*(15/22)^128
        <(11/24)*2^-64<2^-65.                     (38)

The decisive exact comparison is(15/22)^2=225/484<1/2. For Q=h*x_8,
W^(-1/2)=h*rho<=1, so

    0<=W^(-1/2)-Q=W^(-1/2)*e_8<2^-65.

There is no floating-point error or unproved stopping tolerance here.

**C033z width interface and clamping.** At an exact outer node,
t=exp(y) belongs to[2^-30,1/4], so the true width
w=sigma+1/(4*t) satisfies1<=w<=2+2^28. Equation(16) and the positive
Taylor construction show W=sigma+Ehat/4>=sigma>=1 and
|W-w|<2^-122. In particular W<2+2^28+2^-122<2^30, including
any endpoint of the enclosing time interval. Thus every1802 width
meets this constructor's hypotheses without presuming a computed profile.
The derivative bound|(u^(-1/2))'|<=1/2 for u>=1 pays the additional
error2^-123. Apply the original two-comparison clamp to[0,1/4]
on the first17 panels, or[0,1] on the others. The exact w^(-1/2)
is in the respective interval by the original panel contract, so
clamping cannot increase the total error. The fixed Jhat(1) input
remains exactly1. The width-formation operations from1802 are retained;
the replacement takes an already supplied rational W as its input.

**Complete per-width ledger.** Constants are generated afresh, with no
sharing credit across widths. The bound includes an initially supplied
panel flag, whose fixed-index selection is free under the existing model.

| Item | Operations |
| --- | ---: |
| Form2,3,4,1/4 from0,1 |4|
| Check W>=1 |1|
| At most15 loop comparisons, plus final a<=1 check |16|
| At most15 pairs of normalization divisions |30|
| Eight five-operation Newton steps |40|
| Multiply h*x_8 |1|
| Two panel-clamp comparisons |2|
| Total |94|

Early normalization exit can only reduce the count. There are no hidden
rational loop-counter updates: the15-slot and eight-step schedules can
be statically unrolled. Branches on saved comparisons, assignments and
storage remain free exactly as in1802. We have even charged the existing
panel clamps here; they must not be counted as a saving twice in a later
global ledger. The94-operation bound is an algebraic count, not runtime,
bit complexity, denominator growth or memory control.

**Verification and limits.** Run
`python3 scripts/smoothed-law/width_newton_1825.py`.
Its full certificate is
`scripts/smoothed-law/width_newton_1825.json`. Exact rational checks verify
the error-envelope recurrence, its closed form, decisive comparisons,
width-interface upper bound and ledger. Five exact constructor samples
check the implementation, including both domain endpoints;44 normalization
tests cover every interior power-of-four boundary on both sides and
the upper boundary from below. Samples are verification aids, not the
proof of the rational continuum, which is the induction above. The
worst-case ledger94 is attained at W=2^30. No saved1823 value is used.
This is local REPRODUCTION under SPECIALIZE1823, not numerical novelty
or an RH advance. All law/divisor/source qualifications and independent
conditioning, weights, TV, observation, signed-height and realization gaps
remain. Independent application audit was pending at construction; it is
completed in1827 below.

### Independent width-only application audit1827

**Scope and verdict.** Under the unchanged hypotheses and operation model
of extension1825, its simultaneous error2^-60/count100 contract passes.
The audit uses the approved SPECIALIZE assessment1825, reusing the precise
Brent-Zimmermann v0.5.9 Lemma3.14 citation above; it does not reprove that
general theorem. No mathematical correction to1825 is needed. This confirms
a local specialization, not a result beyond the source's Newton theory,
a global evaluator cost, a scalar value or actual-Xi positivity.

**Normalization and theorem hypotheses.** Each successful reduction divides
a by4 and h by2, preserving W=a/h^2. If k=0 the lower input check and
exit condition force W=a=1. If k>0, the preceding a>1 implies the new
a>1/4. After at most15 reductions the upper hypothesis W<=4^15 ensures
a<=1. Thus rho=a^(-1/2) lies in[1,2), and the closed enlargement[1,2]
used in1825 is legitimate. W=4^j gives k=j,a=1 for all0<=j<=15;
there is no missing lower endpoint, upper endpoint or strict-boundary case.
The normalization and rho are proof quantities; computing rho is not an
unpaid operation in the constructor.

The first update has relative value(3*r-r^3)/2 for r=sqrt(a) in[1/2,1].
Its derivative is nonnegative and its endpoint values are11/16 and1,
so x_1>0 and0<=e_1<=5/16. In the later induction the cited theorem's
one-sided conclusion alone would not establish positive next iterates.
The additional fact a*x_n^2<=1 gives x_(n+1)>=x_n>0 first. The source
then supplies x_(n+1)<=rho and theta>=x_n>0, whence, after dividing
its error estimate by rho,

    e_(n+1)<=3*e_n^2/(2*(1-e_n))<=(24/11)*e_n^2.

The invariant is preserved because(24/11)*(5/16)=15/22<1. There are
exactly seven transitions from e_1 to e_8, so their envelope is
(11/24)*(15/22)^128. Since225/484<1/2 and11/24<1/2, that envelope
is strictly less than2^-65. Multiplication by W^(-1/2)<=1 gives the
asserted absolute error for the positive, unclamped Q. No limiting
argument, sample interpolation or numerical square root enters this proof.

**Input perturbation and panel interface.** Use the already audited1802
root-radius input(11), eta=2^-168; this audit does not repeat the full
root/weight isolation audit1806. Equations(14)-(16) give the explicit
rational bounds epsilon_log=9/(4*129*3^129),
epsilon_v=30*epsilon_log+(7/10)*eta and
epsilon_E=96*3^21/41!+3^21*epsilon_v. Independent exact comparisons
verify epsilon_log<2^-200, epsilon_v<2^-160 and epsilon_E<2^-120.
The affine panel bracket is in[2,30] including its enclosing endpoints;
v is in[0,21], and the positive Taylor construction supplies Ehat>=0.
Consequently W>=1, |W-w|<=epsilon_E/4<2^-122, and
W<2+2^28+2^-122<2^30. The inverse-root derivative on[1,infinity)
pays epsilon_E/8<2^-123. Thus the error before panel clamping is
strictly below2^-65+2^-123<2^-64<2^-60.

For panels j=1,...,17 the exact-node bound
w>=sigma+2^(28-7*j/5), with28-7*17/5=21/5>4, puts the exact inverse
root in[0,1/4]. For later panels w>=1 puts it in[0,1]. Projection
to the indicated interval preserves the error: if Q is below, inside,
or above the interval, respectively, replacing it by the lower endpoint,
itself, or the upper endpoint cannot increase its distance to a point
inside that interval. This argument requires the true panel flag. An
arbitrary low-panel flag on a general input W is not granted this error
contract. The one-sided assertion is only for the unperturbed, unclamped
inverse root; neither input perturbation nor clamping is assigned a sign.
The fixed Jhat(1) value remains exactly1.

**Complete count and independent exact evidence.** With k<15 reductions,
the loop makes k+1 comparisons; with k=15 it makes15. Adding the final
comparison separately gives total50+3*k for0<=k<15 and94 for k=15,
including four constant operations, the lower check, both normalization
divisions per reduction, all40 Newton operations, rescaling and two
clamps. Therefore every path costs<=94<100, and W=2^30 attains94.
Fixed unrolled schedules require no uncharged arithmetic counters.
The input W and panel flag are supplied; constructing W remains an1802
cost, and including clamps here grants no duplicate global saving.

Run `python3 scripts/smoothed-law/width_newton_audit_1827.py`.
Its full certificate is `scripts/smoothed-law/width_newton_audit_1827.json`.
The program imports no original constructor: it reconstructs all eight
error envelopes and the1802 interface bounds, checks all16 possible
reduction ledgers, and independently replays all five stored samples
using the additive source update. Each sample's nine iterates, exact
output, normalization and complete counts are checked; positive squaring
checks W*Q^2<=1<W*(Q+2^-65)^2 without an approximate root. All44 stored
normalization boundary cases are also recomputed. All48 audit checks pass
with no failures; the original certificate is preserved and its hash saved.
These finite replays support the written continuum argument above, not
replace it. No1823 execution suffix value is used.

The audit does not certify denominator growth, memory, runtime, rounding
of a changed algorithm, a revised global ledger or full source correctness.
All inherited divisor/law/heat qualifications remain, as do conditioning,
weights, TV<=2, observation coverage, signed-height and actual-Xi realization.

### Once-rounded normalized-width construction1830

**Hypotheses, target and import.** Supply rational W in[1,2^30] and the
true panel flag under the operation model in Hypotheses. As in1825/1827,
W is an already formed width, not a freely constructed input. For the
C033y application retain1802(11),(14)-(17): its exact width w>=1 obeys
|W-w|<2^-122, and w^(-1/2) is in the indicated panel clamp interval.
For a general supplied width, only the unclamped approximation is
asserted unless its exact inverse root belongs to that interval.

The target is simultaneous total error<=2^-60, at most322 operations
including normalization/conversion/clamps, and an explicit bound on every
Newton-iterate denominator independent of denominator(W). The construction
below meets these requirements. It specializes the separately approved
SPECIALIZE assessment1827/recovery1829; it is local REPRODUCTION, not
progress beyond the inspected numerical sources or actual-Xi positivity.

Import Brent-Zimmermann, *Modern Computer Arithmetic*, v0.5.9,
[Lemma3.14, printed p112/PDF p128](https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf#page=128),
with its exact positive-input hypotheses and update as stated in1825.
Reuse that extension's initializer/error specialization after verifying
its hypotheses for the converted coefficient below. For interval halving,
the primary source is [WPI MA3257 Spring2023 lecture23, pp1-2](https://users.wpi.edu/~bgu/sp23/ma3257/lecture_notes/MA3257_L23.pdf).
Its strict endpoint-sign theorem applies to f(z)=z-a when1/4<a<1;
a=1/4 or1 and midpoint equality are handled explicitly below. No
fixed-point iteration, library rounding, floor or bit primitive is used.
The grid, charged conversion and denominator induction are necessary
specializations: neither general source gives this finite contract.

**Normalization and one conversion.** Generate2,3,4,1/4 and perform the
same lower check, at most15 normalization divisions and final check as
1825. Write a=W/4^k,h=2^-k,0<=k<=15. The audited normalization proof
gives1/4<a<=1, W=a/h^2. In particular W=4^j gives k=j,a=1,
including W=1 and W=2^30; values immediately above such a boundary
undergo one more division. We use the closed enlarged interval[1/4,1]
for conversion and all derivative estimates.

Set l=1/4,r=1. In each of64 fixed slots compute m=(l+r)/2 and compare
a>m. If true replace l by m; otherwise replace r by m. After all64
slots set b=(l+r)/2. Do not exit early on equality. Every branch retains
l<=a<=r, including a=l,a=r and a=m; the equality branch retains the
lower half with a as its upper endpoint. The width after N slots is
3*2^(-N-2), by the standard interval-halving rule. Thus

    1/4<b<1, |b-a|<=3*2^-67.                     (39)

All endpoints after64 slots have denominator dividing2^66. Written
over this common denominator their numerators differ by3, so the final
midpoint b=A/2^67 has odd integer numerator A. In particular its reduced
denominator is exactly2^67, regardless of denominator(a). This proves
grid membership for the whole rational domain; tests are not the proof.
Neither endpoint a=1/4 nor a=1 is silently covered by a strict sign
hypothesis: their comparison paths always retain containment and reach
the adjacent interior midpoint. Equalities at any internal midpoint
also satisfy(39), without special arithmetic or an unpaid sign test.

**Eight steps and all three error contributions.** Set x_0=1 and use
exactly the same five-operation update, with b replacing a:

    u=x*x; v=b*u; z=3-v; p=x*z; x=p/2.

The positive coefficient b belongs to[1/4,1]. Therefore1825's verified
specialization of the imported theorem applies with rho_b=b^(-1/2)
and e_n=1-x_n/rho_b: x_n>0, x_n<=rho_b<=2, and

    e_1<=5/16, e_(n+1)<=(24/11)*e_n^2 (1<=n<=7),
    0<=e_8<=(11/24)*(15/22)^128<2^-65.           (40)

Specifically its positivity check b*x_n^2<=1 gives x_(n+1)>=x_n>0
before the theorem is used, and the first-step calculation has
sqrt(b) in[1/2,1]. Thus conversion does not invalidate any theorem
hypothesis. This reuses the existing finite initializer analysis, without
reproving the general Newton theorem. There are still exactly eight steps.

Let Q=h*x_8 before clamping. The first, Newton, error is

    |Q-h*rho_b|=h*rho_b*e_8<=2*e_8<2^-64,

since h<=1 and rho_b<=2. We do not reuse W^(-1/2)<=1 as a bound on
the changed quantity h*rho_b. The derivative of z^(-1/2) has magnitude
at most4 on the entire coefficient segment[1/4,1]. The second error is
therefore, by the mean value theorem and(39),

    |h*rho_b-W^(-1/2)|
      =h*|b^(-1/2)-a^(-1/2)|<=4*|b-a|<=3*2^-65.

For the true C033y width, the third error is the audited1802 bound
|W^(-1/2)-w^(-1/2)|<2^-123, from(16)'s width error and derivative
bound1/2 on[1,infinity). Combining the three errors gives

    |Q-w^(-1/2)|<5*2^-65+2^-123<2^-62<2^-60.     (41)

The last comparison is exact:5+2^-58<8. The first two terms suffice
for a general exact input W. No one-sided error relative to W or w is
asserted, because rounding b can change its sign.

Apply the original two-comparison clamp to[0,1/4] for the first17 panels
and[0,1] for the others. As1827 verifies from C033y's real panel map,
the true w^(-1/2) belongs to the supplied interval. Projection onto that
closed interval cannot increase distance to this point, so(41) persists.
An arbitrary low-panel flag on a general W does not grant that assertion.
Jhat(1) remains exactly1. This meets the original core input accuracy2^-60;
it does not assert the older, stronger2^-64 bound for this changed scheme.

**Denominator certificate.** Write reduced x_n=X_n/2^d_n. Starting from
X_0=1,d_0=0 and b=A/2^67 with A odd, the specified update gives

    x_(n+1)=X_n*(3*2^(67+2*d_n)-A*X_n^2)
                  /2^(68+3*d_n).

If X_n is odd, the numerator displayed is odd: its bracket is an even
integer minus an odd one. Thus there is no cancellation of a factor2,
all X_n remain odd, and

    d_(n+1)=3*d_n+68,
    d_n=34*(3^n-1), 0<=n<=8.                    (42)

The explicit exponents are0,68,272,884,2720,8228,24752,74324,223040.
This proves the exact reduced denominator of every iterate, not only
an asymptotic growth statement. For each step, the reduced denominators
of u,v,z,p divide respectively

    2^(2*d_n), 2^(67+2*d_n),
    2^(67+2*d_n), 2^(67+3*d_n).

These also bound every arithmetic intermediate after conversion. Since
h=2^-k, raw Q has reduced denominator exactly2^(223040+k), hence at
most2^223055. A clamp either retains Q or returns0,1/4 or1, whose
denominators divide that universal power of2. None of these bounds
involves denominator(W). Normalizing or comparing the original a may
still involve its unrestricted denominator; no bit-cost or runtime
bound for these operations follows. A denominator as large as2^223055
may still be too large for practical use.

**Complete local operation ledger.** Retain all normalization charges,
the same freshly generated constants and the supplied true panel flag.
Assignments and the fixed unrolled schedule are free as before.

| Item | Operations |
| --- | ---: |
| Form2,3,4,1/4 from0,1 |4|
| Check W>=1 |1|
| At most15 normalization comparisons and final a<=1 check |16|
| At most15 pairs of normalization divisions |30|
|64 conversion midpoints and comparisons |192|
| Final conversion midpoint |2|
| Eight five-operation Newton steps |40|
| Rescale h*x_8 |1|
| Two panel-clamp comparisons |2|
| Total |288|

For k<15, the exact total is244+3*k; for k=15 it is288.
The latter is attained by W=2^30. Conversion endpoints reuse1/4 and1;
its midpoints use one addition and one division followed by one rational
comparison. No power2^67 is formed by an uncharged constructor primitive;
it appears only in the proof of the grid. Width formation remains outside
this supplied-width contract. Counting clamps here does not authorize a
duplicate saving in the global evaluator. No revised global ledger is
claimed, and no later arithmetic rounding has been introduced.

**Exact evidence and limits.** Reproduce with
`python3 scripts/smoothed-law/width_dyadic_1830.py`; the full certificate
is `scripts/smoothed-law/width_dyadic_1830.json`. The program verifies the
exact envelope, all error comparisons including1802(14)-(16), the nine
exponents and all16 reduction ledgers. It checks71 coefficient cases,
including both closed endpoints and64 distinct midpoint-equality depths,
against an independent integer cell oracle,44 normalization boundaries,
and eight complete sample paths. Every sample saves all nine iterates,
checks every intermediate denominator bound and exact reduced iterate
and raw-output denominators, checks the complete ledger, and verifies
two-sided output error by positive squared inequalities without computing
a square root. Those finite checks support, and do not replace, the
continuum proof(39)-(42). The oracle's integer arithmetic is verification
only, not an operation granted to the constructor.

At construction1830 independent application audit remained pending;
audit1832 below completes it. No old execution
value is used; all1816/1823/a/b artifacts and replay limits are preserved.
The construction does not evaluate a profile, scalar, transform or TV
bound, repair conditioning/weights/observation coverage, settle signed-height
cancellation or realize the selected law by actual Xi. All inherited
divisor/conjugation/multiplicity, excluded ordinate0, strict strip/gamma>14,
counting/real-zero/tail, heat-error, fixed-v1, zero drift/killing and
Gaussian half-variance qualifications remain; full source correctness and
finite-zero data remain unverified.

### Independent once-rounded width application audit1832

**Hypotheses and verdict.** Under exactly1830's supplied-width hypotheses,
true panel flag and rational-operation model, all four simultaneous
claims pass: error<=2^-60, count<=322, exact iterate denominators
2^[34*(3^n-1)] and rescaled denominator<=2^223055. The stronger proved
bounds are error<2^-62 and count<=288. This is an independent application
audit under the pre-existing SPECIALIZE assessment1830, using the
Brent-Zimmermann Lemma3.14 and interval-halving citations stated above.
It verifies local numerical REPRODUCTION, with no stronger general
theorem or progress on actual-Xi signs. No original mathematical claim
requires correction and no general Newton theorem is reproved.

**Normalization, containment and ties.** For k=0 normalization forces
W=a=1; for k>0 the preceding value exceeded1, so1/4<a<=1 after the
last division. The invariant W=a/h^2 and k<=15 follow from the two
separate divisions and W<=4^15. Every exact boundary W=4^j stops at
a=1,k=j. Equation(39) also covers the enlarged, unattained lower
endpoint a=1/4: each conversion branch preserves closed containment.
In particular a=m selects the lower half without a strict-sign theorem,
and equality at either enclosing endpoint remains in the retained half.
After64 slots the width is3/2^66 and the midpoint error is at most
3/2^67. On denominator2^66, initial endpoints and all later endpoints
have integer numerators. Final numerators differ by3; their sum is
odd. Thus b has reduced denominator exactly2^67 and lies strictly
between1/4 and1, including both endpoint and every equality path.

**Positive theorem applications and errors.** With rho_b=b^(-1/2),
x_0=1<=rho_b<=2. The previously audited initializer calculation gives
x_1>0 and0<=e_1<=5/16. At every later step b*x_n^2<=1 makes the
specified next iterate at least x_n>0 before applying the cited
Newton theorem. Its intermediate theta is then at least x_n, and its
error bound gives e_(n+1)<=3*e_n^2/[2*(1-e_n)]<=24*e_n^2/11.
Since(24/11)*(5/16)=15/22<1, all seven subsequent applications
preserve their hypotheses. Their envelope is precisely(40);225/484<1/2
and11/24<1/2 give e_8<2^-65. Rescaling pays at most2*e_8, using
h<=1 and rho_b<=2, rather than the unconverted inverse-root bound.
The entire a-to-b segment is in[1/4,1], where the derivative magnitude
of z^(-1/2) is at most4. Its error is therefore at most3*2^-65.

For1802's already audited root-radius input(11), direct exact comparison
of(14)-(16) gives epsilon_log<2^-200, epsilon_v<2^-160 and
epsilon_E<2^-120. Positivity of T40 on[0,21/32] gives W>=1;
the enclosing panel endpoints give w<=2+2^28 and consequently W<2^30.
The full W-to-w segment lies in[1,infinity), where the inverse-root
derivative magnitude is at most1/2. This pays epsilon_E/8<2^-123.
The sum is strictly below5*2^-65+2^-123<2^-62<2^-60, verifying(41).
For panel j=1,...,17 the actual panel map gives
w>=sigma+2^(28-7*j/5)>16, since28-7*17/5=21/5>4.
Thus the exact inverse root is inside[0,1/4]; for every later panel
w>=1 puts it in[0,1]. Projection to either closed interval cannot
increase distance to that exact point, including at endpoints. This
does not give a general W an arbitrary low-panel flag. The lower clamp
is inactive by positivity; either upper clamp may be active, and the
sample W=1 tests the cap1 branch. The fixed Jhat(1) input remains1.

**Exact denominators and full ledger.** In(42) the numerator bracket
3*2^(67+2*d_n)-A*X_n^2 is even minus odd, hence odd whenever X_n
and A are odd. Multiplication by X_n preserves oddness. Starting
with X_0=1 this proves the exact reduced exponent recurrence
d_(n+1)=3*d_n+68 and d_n=34*(3^n-1), without a hidden cancellation.
The same expressions give every intermediate denominator bound stated
in1830. Multiplication by h=2^-k preserves the odd numerator, so the
raw output denominator is exactly2^(223040+k). A clamp either retains
that output or returns0,1/4 or1, all dividing2^223055.

Each conversion slot costs one addition, one division and one comparison;
the final midpoint costs two. Constants cost four, the lower check one,
normalization comparisons min(k+1,15), its divisions2*k, and the final
check one. Eight Newton steps cost40, rescaling one and both clamp
comparisons two. Thus the complete total is244+3*k for k<15 and288
for k=15, attained at W=2^30. The constants, exact equality branches
and both clamps are charged; no floor, bit extraction, power construction,
loop-counter arithmetic or global sharing credit is silently inserted.
This proves the288 bound for every path, including paths not sampled.

**Independent evidence and limits.** Run
`python3 scripts/smoothed-law/width_dyadic_audit_1832.py`.
The full certificate is
`scripts/smoothed-law/width_dyadic_audit_1832.json`.
All168 checks pass with no failures. No original constructor is imported
or executed. An integer cell formula and the additive source Newton
update replay all71 conversion cases, all44 normalization boundaries,
all16 ledgers, and every saved value in all eight full sample paths,
including all nine iterates and each intermediate denominator assertion.
A separate instrumented factored implementation counts each specified
primitive and agrees with the replay. Error tests use positive squared
inequalities. All source-certificate bounds and92 saved Boolean claims
are checked against recomputed evidence; the unchanged source certificate
is hashed. These finite checks support the uniform proof above.

The initial audit certificate is preserved as
`scripts/smoothed-law/width_dyadic_audit_1832_initial.json`.
Its single failed check concerned sample0 dictionary equality: the audit's
Counter omitted the key for zero normalization divisions. Explicitly
initializing that zero corrected only the audit representation; no
arithmetic, operation total or original claim changed.

The denominator bound2^223055 and unrestricted original-width
normalization/comparisons give no runtime or bit-cost bound. No revised
full ledger, profile, scalar, TV bound or actual-Xi conclusion is obtained.
The1816/1823/a/b execution artifacts and their replay boundaries remain
unchanged. All divisor, source, law, zero-data, heat-error, fixed-v1,
drift/killing and Gaussian qualifications remain in force; conditioning,
weights, observations, signed height, cancellation and realization remain
independently unresolved. This completed width audit is closed, rather
than a justification for another unchanged source approval or replay.

## Mathlib

Full matching coverage is unchecked and unknown. Standard power-series,
Cauchy coefficient, polynomial and finite-sum tools support portions of
the argument; no matching formalized explicit-formula evaluator, input
generation contract or complete operation-count theorem is claimed. The source
theorems above are imported, while this finite specialization is written
out because their general statements supply none of its constants.
The1810 rational-comparison rounding/operation ledger is likewise not
checked for a full matching formalization; unknown does not mean absent.
The1825 finite-operation Newton specialization has not been checked for
matching Mathlib coverage. Its general Newton error input is the precisely
cited external theorem, and its finite constants/ledger are proved above.
Audit1827 verifies that specialization informally; a full matching Mathlib
theorem remains unchecked and unknown.
The1830 once-rounded coefficient contract and exact dyadic denominator
induction have not been checked for full matching Mathlib coverage;
availability is unknown. The source theorem imports and finite
specializations are distinguished above.
Audit1832 verifies the informal application only; full matching Mathlib
coverage of this once-rounded contract remains unchecked and unknown.
