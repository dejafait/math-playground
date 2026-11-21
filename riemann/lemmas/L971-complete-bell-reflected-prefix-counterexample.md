# Lemma 971: the prescribed complete-Bell reflected prefix is negative

## Hypotheses

Use the actual entire function F and logarithmic derivative G=F'/F
of L966, with every paired zero and its multiplicity retained. For
each integer n>=2 use exactly L966(2)'s positive rational d_1,...,d_n
and its parameters

    b=1/4, rho=1/2, h=64*9^n, eta=1/h.

For real t define the complete kernel and real density

    W_n(t)=sum_(k=1)^n d_k rho^(1-k) exp(-i(k-1)t),
    J_n(t)=(1/pi) Re[G(b+rho exp(it)) W_n(t)],
    B_n(theta)=integral_0^theta [J_n(t)+J_n(pi-t)] dt.

Here B_n is the angular prefix specified in the approved step187
assessment, not the rational-reduction polynomial also denoted B_n
in L966(5). No coefficient, Bell partition, or h charge is changed.
Use the unconditional L024 product and L026 bounds: each Xi zero
alpha=a+ic has |a|>4, |c|<1/2, and sum |alpha|^(-2)<infinity
over the paired representatives. No RH, simplicity, positive
Stieltjes representation, or numerical zero information is assumed.

## Conclusion

The contour normalization is, for every n>=2,

    integral_0^pi J_n(t)dt
      =sum_(k=1)^n d_k G^(k-1)(b)/(k-1)!,
    Q_eta(n)=B_n(pi/2)-d_1G(h).                            (1)

Nevertheless, at exactly n=18 and theta=1/2, put

    g=G(b)>0,  M=sum_(k=1)^18 d_k*2^(k-1)>0.

Then

    B_18(1/2) < -7gM/(200pi) < 0,
    B_18(1/2)-d_1G(64*9^18)/pi
      < -7gM/(200pi)-d_1G(64*9^18)/pi < 0.                 (2)

Since 0<1/2<pi/4, this rigorously refutes the fixed TEST
B_n(theta)>=(2theta/pi)d_1G(h) for all n>=2 and
0<=theta<=pi/4. This stops that pairing/allocation rule; it does not
sign the full contour, Q_eta(18), or L966(16), and it does not disprove
RH. Written in step189; independently conceptually audited in step191
on 10 November 2026 without a mathematical correction.

## Proof

### Complete contour normalization

L966 proves that G is analytic on |x-b|<1, so the closed circle of
radius rho=1/2 and its interior have an analytic neighborhood. The
Cauchy formula and its derivative form, NIST DLMF
[1.9.30](https://dlmf.nist.gov/1.9.E30) and
[1.9.31](https://dlmf.nist.gov/1.9.E31), give

    G^(k-1)(b)/(k-1)!
      =(1/(2pi i)) integral_circle G(x)/(x-b)^k dx
      =(1/(2pi)) integral_0^(2pi)
           G(b+rho exp(it)) rho^(1-k) exp(-i(k-1)t)dt.     (3)

For k=1 this is the order-zero Cauchy formula. The contour is
counterclockwise; dx=i*rho*exp(it)dt accounts for the radius and
exponent in (3). F is real entire by L966's theta representation,
so G(conj(x))=conj(G(x)) on this disk. The real d_k similarly give
W_n(2pi-t)=conj(W_n(t)). The full-circle integral of their product
is therefore twice the real part of its upper-circle integral.
Summing the finite d_k multiples of (3) proves the first identity
in (1). Since G^(k-1)=(log F)^(k) locally, L966(12),(14) identify
this as the complete Bell sum with exactly its factorials and signs.
There is no new logarithm across zeros or omitted multiplicity.

Finally substitute u=pi-t in the second half of the prefix:
B_n(pi/2)=integral_0^pi J_n(t)dt. L966(12) then gives (1), with
-d_1G(h) outside the coefficient integral. All these integrals are
over compact paths and finite sums. No theta-integral interchange or
contour deformation is needed.

### An unconditional bound for the complete logarithmic derivative

For every paired zero put c_j=1/(alpha_j^2+b) and write
alpha_j=a+ic temporarily. The use of c here for the imaginary part
is distinct from the resolvent c_j. The real and imaginary parts of
alpha_j^2+b are

    A=a^2-c^2+1/4>a^2>16,    D=2ac,    |D|<|a|.

Consequently

    |c_j|<1/16,
    |c_j|/Re(c_j)=sqrt(1+(D/A)^2)
       <sqrt(17/16)<33/32.                               (4)

The last strict inequality follows by squaring: (33/32)^2=1089/1024
whereas 17/16=1088/1024. In particular every Re(c_j)>0; the c_j
themselves need not be real.

L024/L966 give absolute convergence and, by their locally justified
product differentiation,

    g=G(b)=sum_j c_j=sum_j Re(c_j)>0,
    sum_j |c_j| <= (33/32)g.                               (5)

Reality follows from conjugate pairing. Strict positivity also
follows directly from L966's I_1(b)/I_0(b)>0. For |delta|<=1/2,
the same absolutely convergent resolvent series gives

    G(b+delta)-g
      =-delta sum_j c_j^2/(1+delta*c_j).

Indeed each denominator has modulus at least 1-|delta|/16>=31/32;
the summable majorant is independent of delta on this closed disk.
Thus this identity and its bound involve the entire product, including
every unknown zero and multiplicity, not a truncated zero sum. From
(4)-(5),

    |G(b+delta)-g|
      <= [(1/2)/(1-1/32)]*(1/16)*(33/32)*g
      =(33/992)g = epsilon*g.                             (6)

No real-zero or Stieltjes assumption enters (4)-(6). The analytic
input is the previously established elementary rectangle, not a new
zero-free region or any conditional prime estimate.

### Exact prefix extraction and its full error

At n=18 set A_m=2^m*d_(m+1) for 0<=m<=17, so M=sum_m A_m.
Every A_m is positive and |W_18(t)|<=M for every real t. Define

    S(theta)=integral_0^theta Re[W_18(t)+W_18(pi-t)]dt.

Using cos(m(pi-t))=(-1)^m cos(mt) gives exactly

    S(theta)=2*A_0*theta
       +2*sum_(even m, 2<=m<=16) A_m*sin(m*theta)/m.        (7)

The odd modes cancel only in this constant-g part. They remain in
the full W, in M, and in the following error estimate. Apply (6) to
both reflected points and integrate the triangle inequality:

    |pi*B_18(theta)-g*S(theta)|
      <=2*theta*epsilon*g*M.                              (8)

Equation (8) controls the full angular integral. It pays the complete
complex G variation and all 18 kernel coefficients uniformly along
both arcs; neither sampled quadrature nor a pointwise sign is used.
At theta=1/2, (7) reads

    S(1/2)/M=A_0/M+sum_(j=1)^8 (A_(2j)/(j*M))*sin(j).     (9)

### Rational certificate for the finite sine sum

All A_m and M in (9) are computed with h=64*9^18 using the exact
rational recipe L966(2). In particular h is not replaced by infinity
and the d_k are not rounded. For each integer 1<=j<=8 define

    T_j=sum_(r=0)^32 (-1)^r*j^(2r+1)/(2r+1)!,
    e_j=j^66/66!.

Taylor's theorem with Lagrange remainder, OpenStax, Calculus Volume2,
[section6.3, Theorem6.7 and Examples6.12(b)/6.16(b)](https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series),
applied to sin on an open interval containing [0,j],
through degree 65, gives T_j-e_j<=sin(j)<=T_j+e_j: every real
66th derivative has absolute value at most one. This is a standard
named calculus theorem; only its exact effective specialization is
needed here. All weights A_(2j)/(j*M) in (9) are positive. Therefore
the entirely rational endpoints

    s_minus=A_0/M+sum_(j=1)^8 A_(2j)*(T_j-e_j)/(j*M),
    s_plus =A_0/M+sum_(j=1)^8 A_(2j)*(T_j+e_j)/(j*M)

enclose S(1/2)/M. Exact integer/rational arithmetic gives

    -689/10000 < s_minus <= S(1/2)/M <= s_plus < -688/10000. (10)

Run `python3 scripts/li-theta/reflected-prefix-certificate-189.py`.
The full certificate is
`scripts/li-theta/reflected-prefix-certificate-189.json`. It records
every v_i,w_s,D_r,d_k,A_m,M, every Taylor polynomial and error, all
eight sine intervals, the exact endpoints in (10), the propagated
upper bound and all 13 checks. The construction uses only Python
integer arithmetic and Fraction with integer arguments, no floating
conversion, external numerical package or zero data. The exact
rational arithmetic contract was already inspected in the step185
L970 audit coverage; see the primary
[Fraction reference](https://docs.python.org/3/library/fractions.html#fractions.Fraction).
This import supports the implementation, not the analytic estimates.
The complete `/bounds` and `/checks` values were inspected after the
run, not merely their previews. All 13 checks passed, with no failures.

Combining (8)-(10), and noting 2*theta=1, gives

    pi*B_18(1/2)/(g*M)
       < -688/10000+33/992
       = -22031/620000 < -7/200.                          (11)

This proves the first part of (2). L966 supplies d_1>0 and the exact
positive ratio G(h)=I_1(h)/I_0(h)>0 at h=64*9^18. The right side
of TEST is consequently d_1G(h)/pi>0. Subtracting it from (11),
without altering or discarding the charge, proves the full strict
negative margin in (2). Finally pi>3 implies 1/2<pi/4, so the
counterexample belongs to the prescribed interval.

The earlier floating screen in
`scripts/li-theta/reflected-prefix-screen-189.json` located this
index and angle; it is not proof evidence. The proof is (3)-(11)
and the complete exact rational evaluation of (10). The known Cauchy
and Taylor formulas are imported, not claimed as discoveries. The
bounded step187 comparison found no matching prefix theorem; this
does not certify originality of the counterexample or its estimates.
No complementary-arc claim or full-Q sign follows from this result.

### Independent conceptual audit, step191

The audit accepts (1)-(11) under exactly the stated hypotheses, using
the pre-existing SPECIALIZE source assessment. The analytic argument
and original certificate require no correction. This is verification
of a previously written local obstruction, not a new RH sign result
or a claim of progress beyond the checked literature.

For (3), parameterizing the counterclockwise circle gives the factor
rho^(1-k) and exponent -(k-1)t, including k=1. Conjugation relates
the lower semicircle to the upper without an extra sign. Thus the
upper real integral divided by pi is precisely the Cauchy average,
and B_n(pi/2) contains the entire upper semicircle once. L966(12)
subtracts d_1G(h) once, outside that integral. No boundary zero is
possible in the analytic unit disk furnished by L966.

For (4)-(6), a^2-c^2+1/4>a^2 and |2ac|<|a| hold even for
nonreal zeros. Therefore |D/A|<1/|a|<1/4. In particular
|c_j|/Re(c_j)<sqrt(17/16)<33/32, with Re(c_j)>0.
The shifted resolvents are summable: |1+b beta_j|>=1 and hence
|c_j|<=|beta_j|. Conjugation of the paired multiset then makes
sum Re(c_j)=g, and L966 independently supplies g>0. On the closed
half-radius disk, the difference series is uniformly dominated by
(16/31)sum|c_j|^2<infinity. This justifies its termwise identity
and the error constant 33/992 for the infinite product, including
multiplicities. No reality of individual nodes is used.

For (7)-(9), the two cosine factors add for even m and cancel for
odd m only after replacing G by g. The estimate (8) instead uses
all 18 positive A_m in M and pays both errors. At theta=1/2 the
even frequencies run through m=2,...,16, giving exactly j=1,...,8.
Taylor degree65 uses every odd degree through65 and remainder
j^66/66!, valid on [0,8] without an alternating-series hypothesis.
Positive weights preserve the orientation of all eight enclosures.

Run `python3 scripts/li-theta/reflected-prefix-replay-191.py` to
replay the unchanged construction at a separate path; its full JSON
equals the original, which is preserved. Then run
`python3 scripts/li-theta/reflected-prefix-audit-191.py` for the
independent certificate `scripts/li-theta/reflected-prefix-audit-191.json`.
It reconstructs binomial coefficients by recurrence, w by polynomial
multiplication, D by the Horner shift B(-b+y), and d by successive
division of hB(-b+y) by h-b+y. Reading the coefficient of y^(n-k)
and multiplying by (-1)^(k-1) checks every principal-part sign.
It also clears the complete partial-fraction denominator, checking
all 19 polynomial coefficients, rather than sampled rational values.

Every stored v,w,D,d,A, normalized weight and M agrees exactly;
all coefficient residuals and the full polynomial residual are zero.
A separate Taylor-term recurrence checks every field of all eight
sine records. All endpoints and propagated bounds agree exactly,
including -688/10000+33/992=-22031/620000<-7/200.
All 29 audit checks pass with no failures. Complete selected bounds,
sine records, checks and residual vectors were inspected; acceptance
does not rest on a PASS preview. Fraction is used only with exact
integers or rationals, with no floating conversions.

Finally h=9606056659007943744 is finite and positive, d_1>0,
and L966's strictly positive finite theta integrals give
G(h)=I_1(h)/I_0(h)>0. This is an analytic input, not a numerical
claim of the audit script. The TEST charge at theta=1/2 is exactly
d_1G(h)/pi, so (11) proves the stated charged violation without
dropping it. Only this fixed rule is retired; independent full-Q,
complementary-arc and all-index positivity gaps remain open.

## Mathlib

Full matching coverage is unknown and has not been checked. No Mathlib
theorem is imported. General Cauchy, Taylor, or rational-arithmetic
support alone would not establish the actual product specialization,
the complete-kernel comparison or its constants. Reference portal:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
