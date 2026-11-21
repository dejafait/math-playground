# C759n: The frozen dyadic mode has positive complete Weil quotient

## Hypotheses

Use the full real form Q, Fourier normalization and closed domain of
C759a(1),(5)-(6), on zero-extended real functions in L2(-1,1).
Thus m(t)=Re psi(1/4+it/2)-log pi and

\[
 Q(f)=\int_{\mathbb R}m(t)|F_f(t)|^2\frac{dt}{2\pi}
       +2F_f(i/2)F_f(-i/2)
       -2\sum_{n=2,3,4,5,7}\frac{\Lambda(n)}{\sqrt n}C_f(\log n),
\]

where F_f(t)=int f(x)e^(-itx)dx and C_f(y)=int f(x+y)f(x)dx.
For n=4, Lambda(n)=log2; the other four weights use log n.

Put h(t)=(max{1-t²,0})² and
v(x)=h(40(x-4/5))+h(40(x+4/5)). The single vector is

\[
 f(x)=c_0v(x)+(1-x^2)\sum_{j=0}^{254}c_{j+1}P_{2j}(x),\qquad |x|<1,
 \tag{1}
\]

with P_n(1)=1. The 256 coefficients are **exact dyadic values** of
column0 of `modal_coefficients` in
`scripts/spectral-triples/even-time-one-pair-849.npz`, SHA256
`f74832d1420ec849848f3392e740a87b1bf9ddd53cb39a7ec9d7662c265548fa`.
Their full rational list is also saved under `/input/coefficients` in
`scripts/spectral-triples/frozen-full-quotient-852.json`.
No rounding interpretation of the basis polynomials is used. No
eigenvector identity, matrix eigenvalue accuracy, spectral isolation,
neutrality, positivity theorem, RH or Xi realization is assumed.

## Conclusion

The exact vector has strictly positive squared norm and complete quotient:

\[
\begin{split}
0.00012977475671912&<\|f\|_2^2<0.00012977475671913,\\
0.00000175452250713&<Q(f)<0.00000175452250715,\\
0.01351975184924&<Q(f)/\|f\|_2^2<0.01351975184928.
\end{split} \tag{2}
\]

This rejects the negative matrix indication **for this exact frozen
vector**. It neither bounds the full form below nor rules out other
negative vectors. It does not prove that every eigenvalue error has
one particular cause. The earlier time-one defect stop remains intact.
This is REPRODUCTION of a known geometric interval-evaluation method,
not new variational theory or progress beyond the cited positivity
results. The separate conceptual and implementation audit854 below
validates this scalar certificate and its stated scope.

## Proof

### Complete compact formula and its domain

The general geometric functional is Connes--Consani--Moscovici,
*Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1),
Lemma3.1, (3.14)-(3.16), Proposition3.2 and (3.19). Its exterior
subtraction is integrated in (4.4). Specializing its logarithmic
coordinate to the length2 interval gives, with N=C_f(0),

\[
\begin{split}
 A(f)&:=\int m(t)|F_f(t)|^2\frac{dt}{2\pi}\\
 &=-(\gamma+\log(4\pi\tanh1))N
   +2\int_0^2\rho(y)[Ne^{-y/2}-C_f(y)]dy,\\
 \rho(y)&=\frac{e^{y/2}}{2\sinh y}.
\end{split} \tag{3}
\]

This is a specialization of the general functional, not an inference
from its basis-entry tables. To check the constant and the exterior
term explicitly, its regularized digamma expression is

\[
-(\gamma+\log\pi)N+
 2\int_0^\infty
 \frac{Ne^{-2y}-e^{-y/2}C_f(y)}{1-e^{-2y}}dy.
\]

On [0,2], replacing the N numerator by Ne^(-y) leaves
-N/(e^y+1). Outside [0,2] the correlation vanishes but the subtraction
does not: its integral is -(N/2)log(1-e^(-4)). Together these constants
are -N log(4 tanh1), yielding (3). Both the factor2 and the subtraction
outside the support are retained.

The cited geometric proof is initially smooth. Here (1) is even and
in H1_0(-1,1): its polynomial vanishes at both endpoints, and v is C1
and piecewise quartic with interior support. C759h Proof2 and C759a's
closed-domain identification apply. The extension of (3) can also be
checked directly by H1 approximation with a common support [-1,1].
For every such function, translation of its zero extension gives

\[
 N-C_f(y)=\tfrac12\|f(\cdot+y)-f\|_2^2
          \le\tfrac12 y^2\|f'\|_2^2. \tag{4}
\]

H1 convergence bounds the derivative norms and makes correlations
converge uniformly, by L2 Cauchy--Schwarz. Formula(4) dominates the
singular contribution at zero by an integrable multiple of y; also
|(e^(-y/2)-1)/y|<=1/2. Dominated convergence therefore passes (3)
to (1), while C759a's logarithmic form norm is controlled by H1.
The finite shifts and both pole functionals are L2 continuous.
No new form realization or source positivity theorem is being proved.

### Exact autocorrelation, boundaries and positive denominator

Write p=(1-x²)sum c_{j+1}P_{2j}. The script constructs its monomial
coefficients as integers divided by D=2^d, using the exact identity

\[
P_n(x)=2^{-n}\sum_{m=0}^{\lfloor n/2\rfloor}
 (-1)^m\binom nm\binom{2n-2m}n x^{n-2m}.
\]

Here d=max_i(log2 denom(c_i))+508 suffices for every coefficient,
including c_0. At each breakpoint

\[
 a\in\{-1,-33/40,-31/40,31/40,33/40,1\},
\]

let w_(a,k)/D be the jump of the kth derivative, right minus left.
Then the exact zero extension is the finite truncated-power sum

\[
 f(x)=\frac1D\sum_{a,k}\frac{w_{a,k}}{k!}(x-a)_+^k. \tag{5}
\]

To verify (5), each breakpoint changes precisely the polynomial Taylor
jet by its derivative jumps; equality starts on x<-1 and propagates
across every piece. The entire jet at ±1 is included, so the expression
also equals zero on x>1. For a bump's left edge its nonzero derivative
jumps are c_0D times (12800,-1536000,61440000), at k=2,3,4;
at its right edge they are c_0D times
(-12800,-1536000,-61440000). These follow by expanding
(80t-1600t²)² at the left edge and subtracting
(-80t-1600t²)² at the right edge. At -1 the jet is that of p(-1+t);
evenness gives w_(1,k)=-(-1)^k w_(-1,k).

Since f is even, C_f(y)=(f*f)(-y). The finite convolution identity

\[
 \int_a^{z-b}\frac{(x-a)^i}{i!}\frac{(z-b-x)^j}{j!}dx
 =\frac{(z-a-b)_+^{i+j+1}}{(i+j+1)!}
\]

is the elementary integer beta integral (and is zero if z<a+b).
It applies term by term to the finite sums in (5): at fixed z each
nonzero integration interval is bounded. Thus, for 0<=y<=2,

\[
 C_f(y)=\frac1{D^2}\sum_{b>0,k\ge1}
             B_{b,k}\frac{(b-y)_+^k}{k!}. \tag{6}
\]

B is the exact integer convolution of the derivative-jump arrays,
summed over ordered pairs with endpoint sum -b. The distinct positive
b are 1/20,7/40,9/40,31/20,8/5,33/20,71/40,73/40,2.
Pairs with endpoint sum0 contribute zero also at y=0, because k>=1;
positive endpoint sums never contribute. Hence every piece is accounted
for. Integer arrays, denominator and all breakpoints are in
`/exact_geometry` of the certificate.

The exact rational sums of (6) at zero and of its second derivative
give N and D_1=-C_f''(0)=||f'||². The latter identity follows from
Plancherel for H1 zero extensions (or weak integration by parts).
The stored exact fractions are both positive; outward conversion
gives (2) for N, and 10.92731417769<D_1<10.92731417771.
Thus division is justified independently of any mass matrix.

### Origin extension and all polynomial moments

Let K(y)=y exp(y/2)/sinh y, with K(0)=1. The integral in (3) equals

\[
 \int_0^2 K(y)\left[\frac{N-C_f(y)}y+
                         N\frac{e^{-y/2}-1}y\right]dy. \tag{7}
\]

The bracket extends continuously to -N/2 at zero by (4). No endpoint
is omitted. For n>=1 put I_n=int_0² y^(n-1)C_f(y)dy. Formula(6)
and the same beta integral yield

\[
 I_n=\frac1{D^2}\sum_{b,k}
   \frac{B_{b,k}b^{n+k}(n-1)!}{(n+k)!}. \tag{8}
\]

Put T_n=int_0² y^(n-1)(N-C_f(y))dy. For n>=1,
T_n=N2^n/n-I_n. For n=0 the cancellation must precede integration:

\[
 T_0=\frac1{D^2}\sum_{b,k}\frac{B_{b,k}b^k}{k!}
                    [H_k+\log(2/b)]. \tag{9}
\]

Indeed int_0^b [b^k-(b-y)^k]/y dy=b^k H_k, and the remaining
interval [b,2] contributes b^k log(2/b). These are finite signed sums;
no positivity or interchange of an infinite correlation series is used.

### Certified analytic remainder

The coefficients k_n of K are computed recursively from
K(y)(sinh y/y)=exp(y/2):

\[
k_n=\frac1{2^n n!}-\sum_{2\le j\le n,\ j\text{ even}}
                           \frac{k_{n-j}}{(j+1)!}. \tag{10}
\]

On |z|=R=5/2, |sinh z|²=sinh²(Re z)+sin²(Im z).
For |t|<=R<pi, |sin t|>=|t| sin(R)/R, since sin(t)/t decreases
on (0,pi). Also |sinh x|>=|x|. Hence
|sinh z|>=sin R, and |K(z)|<=R exp(R/2)/sin R<20.
The last strict inequality is certified using sin(5/2)>1/2 from
its six-term alternating Taylor lower bound, exp(5/4)<4, and the
Machin enclosure pi>5/2. The only potential nonzero zeros of sinh
are i*pi times nonzero integers, outside this disk.
The Taylor coefficient and remainder bounds from the Cauchy integral
formula therefore give, on [0,2],

\[
 \left|K(y)-\sum_{n=0}^{256}k_ny^n\right|
 \le100(4/5)^{257}.
\]

By (4), the L1 norm of the bracket in (7) is at most D_1+N.
Thus the **entire** omitted kernel contribution is bounded by

\[
 E_K=100(4/5)^{257}(D_1+N)<1.358\cdot10^{-22}. \tag{11}
\]

This uses the Cauchy coefficient estimate, from the Cauchy derivative
formula [NIST DLMF1.9.31](https://dlmf.nist.gov/1.9.E31), on the
specified pole-free disk. The disk bound and the polynomial moments are the
necessary input-specific specialization. No unproved quadrature-error
constant or requested tolerance replaces a bound.

For each n, E_n=int_0² y^(n-1)(e^(-y/2)-1)dy is evaluated by

\[
 E_n=2^n\sum_{j=1}^{128}\frac{(-1)^j}{j!(n+j)}+r_n,
 \qquad |r_n|\le\frac{2^n}{129!(n+129)}. \tag{12}
\]

This follows by integrating the alternating exponential Taylor
remainder on y/2 in [0,1]; it includes n=0. Each r_n is inserted
as an interval before summing k_n(T_n+NE_n). Then (11) is inserted
before adding the constant in (3).

### Both poles, all shifts, arithmetic and result

Autocorrelation and Fubini on compact support give

\[
 2F_f(i/2)F_f(-i/2)=4\int_0^2 C_f(y)\cosh(y/2)dy.
\]

Both poles are therefore evaluated together as
4 sum_(j=0)^64 I_(2j+1)/(2^(2j)(2j)!), with symmetric remainder
at most 16N/130!: |C_f|<=N and the tail of cosh(t), |t|<=1,
is at most 2/130!. Every arithmetic term evaluates (6) at log n
with outward ln/sqrt intervals; the script checks each delay lies
strictly on one side of every breakpoint before selecting its piece.
None of 2,3,4,5,7 is omitted or assigned a free phase. The resulting
contribution intervals, coarsened here only for readability, are

\[
\begin{split}
0.00005742105688320&<A(f)<0.00005742105688322,\\
0.00000364173996494&<\text{both poles}<0.00000364173996496,\\
-0.00005930827434103&<\text{prime sum}<-0.00005930827434100.
\end{split}
\]

The full intervals, rather than these coarsenings, give (2).
Reproduce with

    python3 scripts/spectral-triples/frozen-full-quotient-852.py

The JSON of the same stem records the exact input, full integer arrays,
exact norm/derivative fractions, every integrated polynomial term,
all shift correlations, complete form contributions, analytic errors,
final intervals, checks, failures and script hash. No floating assembly
or samples enter this calculation. The only use of NumPy is loading
the frozen binary64 constants and checking finiteness.

All subsequent arithmetic uses exact Python integers/Fraction or
900-digit directed Decimal intervals. Basic arithmetic rounds down/up;
ln, exp and sqrt expand the documented correctly rounded result by
adjacent endpoints, as in C759a's convention. Integer convolution uses
balanced power-of-two packing with base greater than twice an upper
bound on any output coefficient. Balanced digit extraction is then
exact; independent evaluations at -1,0,1,2 also check each product.
Gamma uses C759a's Euler--Maclaurin m=2 bound at1024 with radius
1/(60*1024^4); pi uses its Machin/60-term alternating bounds. The
gamma error dominates the final width, about3.94e-18 in Q.
These software semantics are explicit trust assumptions, not a formal
verification of Python or the interpreter.

The first execution was interrupted during an inefficient exact integer
remainder operation before producing evidence; replacing it by the
identical bit mask completed this same fixed calculation. There was
no parameter, coefficient, basis or mode sweep. No failed mathematical
certificate was discarded. All final checks except the deliberately
false `quotient_negative` comparison are true; the failures list is empty.
These statements describe the original calculation852. The later audit
is recorded separately below; the original script and certificate remain
unchanged.

### Independent conceptual and complete finite audit854

The audit reuses the primary-source coverage in assessment852, approved
in source review853. It does not invoke any source positivity theorem.
The following checks validate (2), without upgrading it to a spectral
bound, a ground-state statement or actual-Xi positivity.

**Normalization and extension.** In the regularized digamma integral
above, replacing e^(-2y) by e^(-y) on [0,2] changes the N contribution
by -2N int_0^2 (e^y+1)^(-1)dy. This equals
-2N[log2-log(1+e^(-2))]. The surviving exterior contribution is
-N log(1-e^(-4)). Their sum is -N log(4 tanh1), exactly as in (3).
The change of variable in the digamma integral is t=2y, retaining
its factor2 and the Fourier measure dt/(2pi). The length2 support
forces C_f(y)=0 for |y|>=2, but does not remove the exterior subtraction.

The prescribed polynomial vanishes at ±1, and both quartic bumps have
zero value and first derivative at their edges. Thus the zero extension
is H1 and belongs to the closed domain in C759a(5)-(6), as also checked
in C759h Proof2. For a smooth H1_0 approximation with common support,
the derivative norms stay bounded and (4) controls N-C_f uniformly
near zero. The remaining exponential numerator divided by y is bounded
by N/2. The logarithmic Fourier weight is bounded by a constant times
1+t², so H1 convergence also passes the Fourier form. Bounded supported
shift and pole functionals pass by L2 convergence. This pays both sides
of (3) on this exact nonsmooth vector, not just the geometric side.

**Exact vector and convolution.** The audit reads all256 binary64
coefficients from column0 of the hash-pinned archive and compares their
exact integer ratios with every saved fraction. It constructs
A_n=2^n P_n by A_0=1, A_1=2x and

    (n+1)A_(n+1)=2(2n+1)x A_n-4n A_(n-1),

checking exact integer division at every step. This is independent of
the generator's binomial coefficient formula. Successive polynomial
differentiation and Horner evaluation at -1 recover every endpoint
jet; squaring 80t-1600t² and reflecting recovers the bump jets. The
audit compares every stored jump and uses ordinary, unpacked integer
multiplication over all ordered pairs to compare every coefficient
of all nine correlation pieces. No evaluation at a few points serves
as polynomial equality evidence.

For completeness, the generator's packing proof is valid: every product
coefficient has absolute value at most its declared bound M, and the
base exceeds2M. Reduction modulo that base followed by the balanced
representative therefore recovers the unique constant coefficient.
Subtracting it and dividing by the base repeats the same argument for
each coefficient, including negative integers. The exact final zero
quotient checks the degree. The unpacked audit does not rely on this
implementation or its spot checks.

All jumps of order0 vanish, so every nonzero convolved truncated power
has degree at least3. In particular the omitted zero endpoint-sum
pieces contribute neither C_f(0) nor C_f''(0). Equivalently, H1 implies
that t²|F_f(t)|² is integrable, so C_f is twice continuously
differentiable and C_f''(0)=-||f'||² by Plancherel. Direct exact rational
summation of the independently rebuilt pieces matches both full saved
fractions and proves N>0 and D_1>0. No floating mass matrix is used.

**Origin and entire analytic error.** Equations (8)-(9) are finite
beta-integral identities; the audit uses exact rational harmonic numbers
in (9), so cancellation occurs before integration. The bracket in (7)
has its stated limit -N/2. Its absolute integral is at most
int_0^2(yD_1/2+N/2)dy=D_1+N. On the circle |z|=5/2, the lower bound
for |sinh z| follows from x²+(sin(R)/R)²y²>=sin²R. The six-term sine
bound has a positive alternating remainder (the terms decrease from
index1 onwards), and the certified bounds pi>R and exp(5/4)<4 give
the strict constant20. Cauchy's formula therefore controls every
omitted Taylor coefficient, producing the full geometric remainder
100(4/5)^257 in (11), not an estimate from the last retained term.

The audit constructs all257 kernel coefficients and all257 exponential
integrals with128 retained terms as exact rationals, encloses the signed
integrals with their complete (12)
remainders, and checks every saved moment and integrated term. Both
poles use every even moment through degree128. The cosh tail on [0,1]
is bounded by2/130!, so |C_f|<=N gives exactly16N/130! after integration
and the factor4. Each delay log n is checked against every active
piece; all five prime-power contributions have their original weights,
including log2/sqrt4 at n=4. No origin, endpoint, pole or shifted piece
is dropped or given a favorable sign.

**Arithmetic, complete evidence and replay.** Run

    python3 scripts/spectral-triples/frozen-full-quotient-audit-854.py

The audit uses independently implemented1050-digit outward intervals,
exact rational kernel/exponential/constant partial sums, reversed
moment accumulation, and direct factorial-power correlation evaluation
instead of the generator's Horner evaluation. Every independent origin
component, all256 moments, all257 kernel/Tn/En/term rows, every analytic
error and every prime row is contained in its corresponding full saved
interval. The independently assembled form and quotient are contained
in the original full intervals; all open decimal brackets in (2) and
the displayed contribution bounds are verified against both original
endpoints. The norm stays strictly positive throughout division.

Basic arithmetic uses explicit directed Context operations. Negation
uses copy_negate; the one ambient Decimal multiplication in the audit
tests only the sign of a divisor, with operands safely inside the normal
exponent range. The actual logarithm and square-root arguments are
positive, and every divisor excludes zero. The documented correctly
rounded ln/exp/sqrt results are widened to adjacent endpoints, rather
than assuming the rounding direction from a context name. The software
contracts are [Python3.15 Decimal](https://docs.python.org/3.15/library/decimal.html)
and [Fraction](https://docs.python.org/3.15/library/fractions.html#fractions.Fraction).
Euler--Maclaurin and Machin use the cited C759a bounds, recomputed with
exact rational partial sums. No numerical integration routine is used.

An exact-byte copy of generator852 is replayed with ambient Decimal
precision7 in `scripts/spectral-triples/audit-854-replay/`. Its entire
parsed certificate equals the original, including all large integer
arrays and every interval endpoint. The originals' hashes are unchanged.
The full audit evidence is
`scripts/spectral-triples/frozen-full-quotient-audit-854.json`:
**1645 checks, zero failures**. It records every comparison and all
independent intervals; no preview or selected success flag replaces
these full comparisons. Python integer/Fraction/Decimal semantics and
binary64 loading remain explicit trust assumptions. Neither this audit
nor replay is a formal verification of the interpreter or libraries.

The completed audit validates the positive scalar rejection852. It
does not establish the sign of another vector, an eigenvalue, a heat
or resolvent pairing, parity, a full spectral floor, or RH. No numerical
or analytic correction of the published bounds was needed.

## Mathlib

Full matching theorem and supporting theorem coverage were not checked.
No absence or formal-verification claim is made. The present result is
a complete directed-arithmetic specialization of the cited geometric
form, with software trust and later audit qualifications as stated.
