# C029q — A negative direction for the prescribed U_6-to-U_7 quotient residual

## Hypotheses

Use the full Jensen-weighted family of C029m, retaining all odd
coefficients, with the constant normalization of C029n:

    S=sin(pi/8)/sqrt(2)>0,  U_N=T_N/S,
    U_N(t)=sum_(k=0)^N A_(N,k) p_k(t),
    A_(N,k)=[N!/((N-k)!N^k)] beta_k/S,  N=6,7,
    p_(-1)=0, p_0=1,
    (k+1)p_(k+1)(t)=t p_k(t)-(k+1/2)p_(k-1)(t).

The finite source is A. Kuznetsov, *Expansion of the Riemann Xi Function
in Meixner–Pollaczek Polynomials*, Canadian Mathematical Bulletin 51(4)
(2008), 561–569, DOI 10.4153/CMB-2008-055-0,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf),
recurrence (2), coefficients (4)/(13), pp563/566, and weighted family
pp568–569. Explicitly, put s=sqrt(2), X=pi and

    epsilon_j=1, 1+s, -1, -1-s  for j=0,1,2,3 mod 4,
    v_n=-n! sum_(h=0)^n
        4^h(4^(h+1)-1) B_(2h+2) (2X)^(h+1) epsilon_(n-h)
        /((n-h)!(2h+2)!),
    beta_n/S=4n(n-1)v_(n-2)+(8n^2+12n+7)v_n
             +(2n+3)(2n+5)v_(n+2).

For n=0,1 omit the first term. Here v_n=u_n/S in C029n's notation;
its half-angle identity gives the stated phases. Use v_0,...,v_9 and
beta_0,...,beta_7 only. Bernoulli numbers have B_1=-1/2 and are
specified exactly by

    B_0=1,
    B_j=-(1/(j+1)) sum_(k=0)^(j-1) binom(j+1,k)B_k, j>=1.

In particular B_20=-174611/330. No infinite-series convergence or
numerical root observation from the source is an input to this result.

Use the descending bases Phi_6=(p_5,...,p_0)^t and
Phi_7=(p_6,...,p_0)^t. For j=6,7 define B_j with C029o's order by

    Phi_j(x)^t B_j Phi_j(y)
      =(U_j(x)U_j'(y)-U_j(y)U_j'(x))/(x-y).

After proving the actual degrees below, let q be the unique affine
quotient in U_7=q U_6+r, deg(r)<6. Define the 7 by 6 matrix E by

    q(t)Phi_6(t)=E^t Phi_7(t),
    P=B_7-E B_6 E^t.

There is no N-dependent monic, norm or other rescaling. In particular
E is fixed by the coefficients, with no root or eigenvector fitting.
The only transcendental input enclosures are the exact 60-decimal
rational intervals for pi and sqrt(2) proved in C029n.

## Conclusion

The actual degrees of U_6 and U_7 are six and seven. In the stated
Phi_7 coordinates, the rational vector e_2=(0,1,0,0,0,0,0)^t satisfies

    -7.961713*10^(-7) <= e_2^t P e_2 <= -7.961712*10^(-7) < 0.

The terminating decimals here and below denote exact rationals.
Thus this prescribed affine-quotient residual is not positive
semidefinite at the pair N=6,7. A shorter rational enclosure in the
proof already certifies e_2^t P e_2 < -79/10^8.

This rejects only the PSD increment for this embedding at this pair.
It does not exclude a different embedding, a later eventual-only
increment, or an index bound obtained without PSD increments. It is
neither a counterexample to C029m's eventual premise nor a proof or
disproof of RH. Independent audit2024 validates the fixed coefficients,
kernel/embedding orientation, complete rational enclosures and all 49
recorded directions. It adds verification of this finite obstruction,
not an additional propagation result.

## Proof

### Coefficients, degrees and the quotient

All finite coefficients lie in R=(Q[s]/(s^2-2))[X], evaluated at the
positive s=sqrt(2), X=pi. Reconstruct the p_k by their recurrence.
Induction gives deg(p_k)=k, leading coefficient 1/k!, and parity k.
The calculation uses the displayed finite source formulas and every
Jensen weight at its own N; it does not reuse the N=6 weights at N=7.
The Bernoulli recurrence is evaluated through B_20. All v_n and beta_n
already present in C029n, and every N=6 Jensen and monomial coefficient,
agree exactly with that input. All p_0,...,p_6 agree with C029o.

Write

    U_6=sum_(i=0)^6 b_i t^i,  U_7=sum_(i=0)^7 c_i t^i,
    l=b_6, m=b_5, L=c_7, M=c_6.

The unchanged input intervals and rational Horner operations give

    -1.241943*10^(-6) <= l <= -1.241942*10^(-6),
     7.329627*10^(-8) <= L <=  7.329628*10^(-8).

Both leading coefficients are separated from zero. The first agrees
with C029n's degree-six fact, and the second certifies degree seven.
Let

    D=l^2>0,
    Q(t)=(Ll)t+(Ml-Lm),
    alpha=L/l, gamma=(M-alpha*m)/l, q(t)=alpha*t+gamma=Q(t)/D.

The coefficients of t^7 and t^6 in D U_7-Q U_6 are respectively
l^2 L-(Ll)l=0 and l^2 M-(Ll)m-(Ml-Lm)l=0. Thus

    R=D U_7-Q U_6, deg(R)<6,
    r=R/D, U_7=q U_6+r.

Since U_6 has degree six, the usual uniqueness of polynomial division
identifies this q as the prescribed quotient. Its linear coefficient
is nonzero because L and l are nonzero. No other denominator is
introduced here. The certificate stores every coefficient of Q and R,
the common denominator D, and all eight zero coefficients of the
division identity after clearing D.

### The embedding and both kernels

The recurrence rearranges to

    q p_k=alpha*(k+1)p_(k+1)+gamma*p_k
           +alpha*(k+1/2)p_(k-1), 0<=k<=5,

where the p_(-1) term is omitted. Therefore, in one-based coordinates,
column j=6-k of E has precisely

    E_(6-k,j)=alpha*(k+1),
    E_(7-k,j)=gamma,
    E_(8-k,j)=alpha*(k+1/2)  if k>=1,

and all its other entries vanish. These are within seven rows. This
checks the reversal and transpose explicitly. Let H=D E; its entries
are in R. Direct coefficient matching checks all 42 coefficients of
Q Phi_6=H^t Phi_7.

The source representation is H. Wu, X. Wu and Z. Yang, *More on
polynomial Bezoutians with respect to a general basis*, Electronic
Journal of Linear Algebra 21 (2010), 154–171,
DOI 10.13001/1081-3810.1421, [primary PDF](https://emis.de/ft/34467),
definition (1.1), Proposition 3.7, (3.12)–(3.13), proof pp165–166.
It supplies coefficient multiplication for a degree-graded basis and
specified factor degrees, not positivity. Here affine multiplication
has n=7, r=s=1; the polynomial bases have nonzero leading coefficients
and the identity above fixes the actual matrix orientation. We apply
only the multiplication interface to q(x)q(y) times the U_6 kernel.
We do not assert a common quotient factor in U_7 and U_7'. The finite
coefficient verification is needed to identify E in our descending
coordinates; it is not a reproof of a general source theorem.

For completeness the construction of each B_n, n=6,7, is the finite
specialization of C029o. If d_i=[t^i]U_n and f_i=(i+1)d_(i+1), with
f_n=0, its monomial kernel is

    K_n(x,y)=sum_(0<=j<i<=n) (d_i f_j-f_i d_j)
               sum_(h=0)^(i-j-1) x^(i-1-h)y^(j+h).

Multiplication by x-y telescopes each inner sum to x^i y^j-x^j y^i.
Thus (x-y)K_n is exactly the required numerator. The quotient has
degree at most n-1 in each variable and is symmetric, because both
numerator and divisor change sign under exchange of x and y. An
invertible rational triangular basis conversion then defines B_n
uniquely. All 49 and 64 kernel identity coefficients, respectively,
and all 36 and 49 conversion coefficients are checked exactly. The
36 entries of B_6 agree with the stored C029o matrix used in C029p's
audited baseline. C029p's inertia is a comparison, not a premise here.

Consequently the residual is exactly

    P=(D^2 B_7-H B_6 H^t)/D^2.

The complete numerator matrix and denominator are retained, along with
symmetry and the defining identity residuals. D>0 justifies every
clearing of D or D^2. This is an identity defining the object to be
tested; it supplies no PSD property.

### The short quadratic witness

In Phi_7, e_2 is the p_5 coordinate. The explicit embedding gives

    E^t e_2=(gamma,5alpha,0,0,0,0)^t,
    e_2^t P e_2
      =(B_7)_22-gamma^2(B_6)_11
        -10alpha*gamma(B_6)_12-25alpha^2(B_6)_22.        (1)

Here is an independent short algebraic check on the entries used in
(1). Put b=b_4 and c=c_5. In the monomial kernel formula, the upper
three entries have coefficients n d_n^2, (n-1)d_n d_(n-1) and
(n-1)d_(n-1)^2-2d_n d_(n-2). Parity of the basis prevents p_(n-1)
from contributing to t^(n-2). Its leading coefficients therefore give

    (B_6)_11=86400 l^2,
    (B_6)_12=14400 l m,
    (B_6)_22=576(5m^2-2lb),
    (B_7)_22=14400(6M^2-2Lc).

For the third monomial entry, the only contributing pairs in the
telescoping formula are (n,n-3) and (n-1,n-2): their sum is
(n-2)d_n d_(n-2)+(n-1)d_(n-1)^2-n d_n d_(n-2), as claimed.
The first two follow from the highest x coefficient d_n U_n'(y).
Thus no kernel sign or transpose convention is inferred from an
observed numerical signature. All four formulas also agree exactly
with the full matrices in the certificate.

Substituting alpha and gamma into (1) gives the additional identity

    e_2^t P e_2=14400*(-2Lc+2LMm/l-L^2*m^2/l^2+2L^2*b/l).

Its polynomial numerator over D, multiplied by D, equals exactly
entry (2,2) of the full residual numerator over D^2. The stored
polynomial difference is zero. This is a second finite check of the
particular quadratic form, not a new propagation lemma.

The following small rational intervals are outward bounds of the
full computed intervals. The multiplier applies to both endpoints.

| Quantity | Lower | Upper | Multiplier |
| --- | ---: | ---: | ---: |
| alpha | -5.901744 | -5.901743 | 10^(-2) |
| gamma | 5.141917 | 5.141918 | 1 |
| (B_6)_11 | 1.332652 | 1.332653 | 10^(-7) |
| (B_6)_12 | 8.904045 | 8.904046 | 10^(-7) |
| (B_6)_22 | 1.363887 | 1.363888 | 10^(-5) |
| (B_7)_22 | 1.212848 | 1.212849 | 10^(-6) |

Substituting just these six closed intervals into (1), by endpoint
interval addition and multiplication, gives the complete rational
enclosure

    -15923511251909218749/20000000000000000000000000
       <= e_2^t P e_2 <=
    -159233597632112199611/200000000000000000000000000.

The upper endpoint is strictly less than -79/10^8: the difference
between -79/10^8 and that upper endpoint is exactly

    1233597632112199611/200000000000000000000000000 > 0.

This small rational comparison alone proves the obstruction. Evaluating
the same expression through the full entry intervals, before rounding
to this table, gives the tighter bounds in the Conclusion.

### Enclosure justification and complete test record

C029n proves containment of the original input intervals using
48-term arctangent sums with positive bounded remainders, the Machin
identity with its angle branch checked, and strict integer-square
endpoint inequalities for sqrt(2). We reuse those exact intervals and
their proof, not assumed decimal expansions or a precision increase.
The input certificate SHA256 is

    361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7.

For each R-polynomial, enclose a coefficient a+b*sqrt(2) using the
sign of b, then apply interval Horner at the fixed pi interval.
For two closed intervals take sums of endpoints for addition and
the minimum and maximum of all four endpoint products for
multiplication. Order and bilinearity prove these operations enclosing;
induction through the finite expression proves containment. No
independence of repeated parameters is assumed. Exact integer and
Fraction operations give their endpoints without rounding error.

For [a,b] wholly positive or wholly negative, the reciprocal interval
is [1/b,1/a], since x maps to 1/x decreasingly on either half-line.
The computed interval for l is negative, and that for D=l^2 is
positive. These are the only nonconstant denominators reciprocated.
Enclose alpha=L/l and gamma=(M-alpha*m)/l from the monomial
coefficient intervals; an alternative Q/D evaluation also overlaps.
Enclose E using its explicit three-entry columns, and B_6 and B_7
entry by entry. Finally use finite interval matrix multiplication for
B_7-E B_6 E^t and rational quadratic forms. The expanded high-degree
residual numerator is retained for exact algebra only; its interval
Horner evaluation is not used. This respects C029o's recorded expanded
determinant overestimation and does not alter the input precision.

The sign test used exactly the 49 predeclared vectors e_i and
e_i+e_j, e_i-e_j for 1<=i<j<=7. Their coefficients and enumeration
do not depend on the matrices. The quotient, embedding and full exact
residual were saved before their quadratic signs were inspected.
All 49 forms have separated intervals: 48 negative and one positive
(e_1). The e_2 witness is the first negative in that fixed enumeration.
These signs do not specify the full inertia of P or of B_7.

Reproduce from this notebook with

    python3 scripts/pollaczek/tilted_affine_quotient_residual_2022.py

The complete certificate is
`scripts/pollaczek/tilted-affine-quotient-residual-2022.json`.
It retains every finite coefficient, basis polynomial, quotient and
remainder, denominator and degree interval, both kernels, basis
conversion matrices, H/D, the full residual numerator/denominator,
all identity residuals, and every tested rational vector and quadratic
form with full exact interval endpoints. It also stores all six small
input bounds above, their complete rational comparison, input/helper
hashes, checks and failures. All 99 checks pass; the failures and
unresolved-sign arrays are empty. Complete checks, selected exact
identity residual and small load-bearing rational values were inspected.
The checks are reproducible arithmetic evidence, not formal proof
assistant verification or a separate independent audit.

### Independent fixed-input audit2024

The separate standard-library implementation
`scripts/pollaczek/tilted_affine_residual_audit_2024.py` imports none of
the original mathematical helpers. It reconstructs sparse polynomials
in Q[X,s]/(s^2-2), all Bernoulli numbers through B_20, every v_0,...,v_9,
beta_0,...,beta_7, both sets of Jensen weights and both monomial
polynomials. All coefficients agree exactly with the original complete
certificate. It independently recomputes C029n's 48 arctangent terms
and remainder bounds for each argument, containment in the unchanged
pi interval, and the positive squared sqrt(2) endpoint inequalities.
The analytic Machin branch proof is the one in C029n; the arithmetic
check is not a substitute for that argument. No infinite convergence
or upstream[9] claim is used.

For the kernels, the audit expands the stored B_6 and B_7 directly in
Phi_n(x),Phi_n(y), multiplies by x-y, and compares all coefficients
with U_n(x)U_n'(y)-U_n(y)U_n'(x). This differs from constructing the
kernel by the original telescoping routine. Nonzero rational leading
coefficients of the basis give uniqueness. Every stored inverse-basis
row is checked as a polynomial identity. The degree-six baseline B_6
agrees with C029o's certificate; its inertia from C029p is unused.
All eight quotient coefficients, all 42 embedding coefficients, the
explicit descending three-entry columns, and every entry of
D^2 B_7-H B_6 H^t agree exactly with the stored objects. These checks
fix the sign and transpose without inferring them from signatures.

The independent rational evaluator recomputes every complete endpoint
of the coefficient, reciprocal, E, B_6, B_7 and P intervals, with
denominator separation checked before reciprocation. It reconstructs
the exact 49-direction enumeration and compares every vector, full
quadratic numerator, complete endpoint, outer enclosure and sign.
There are exactly 48 negative directions and one positive direction,
e_1; e_2 is the first negative. The four short kernel formulas and the
scalar numerator identity above are checked independently against the
full exact matrices.

All six small rational bounds contain the independently reconstructed
complete intervals. Their endpoint substitution reproduces precisely
the two coarse rational endpoints and the positive difference
1233597632112199611/200000000000000000000000000 above. The full
unrounded e_2 endpoints agree with the original certificate and lie
inside [-7.961713*10^(-7),-7.961712*10^(-7)]. Direct evaluation of
(1) with the full six input intervals gives exactly those same raw
endpoints. Thus the stronger conclusion, as well as the shorter strict
negative comparison, survives the independent audit; rounded previews
are not the arithmetic evidence.

Reproduce with

    python3 scripts/pollaczek/tilted_affine_residual_audit_2024.py

All 152 checks pass with no failures. The complete audit certificate
`scripts/pollaczek/tilted-affine-residual-audit-2024.json` retains input
hashes, all check results, independently computed full intervals for
every tested direction, the full raw witness endpoints, the six small
rational inputs and strict comparison. Complete original coefficients
and identities remain in the unchanged original certificate, whose
hash the audit records. This is independent implementation evidence and
the finite inclusion proof above, not proof-assistant verification.
No degree, precision, embedding, normalization or claimed scope changed.

The finite formulas and multiplication machinery are known. The
approved comparison2020 did not identify a source for this prescribed
actual-coefficient residual sign; that does not establish originality.
The new local evidence is the obstruction to this particular proposed
increment. Uniform all-degree control, singular cases, initialization,
and C029m's qualified compact convergence including upstream[9] remain
unresolved and are unused. No negative direction here is an off-line
zeta zero, and the actual-Xi gap L030–L032/C032a remains open.

## Mathlib

Full matching coverage for this residual, coefficient certificate,
quotient embedding and interval proof has not been checked. No absence
or formalization claim is made. The named source formulas and general
basis interface are imported; the finite specialization and negative
witness are the local work.
