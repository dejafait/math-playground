# Lemma 734: coarse Selberg control admits the fixed-kernel power profile

## Hypotheses

Let Lambda be the ordinary von Mangoldt function, with Lambda(1)=0,
and psi(t)=sum_(n<=t) Lambda(n). Fix an absolute constant A>0 such that
psi(t)<=A t for every real t>=2. Such a constant exists by Chebyshev's
theorem. On 1<=t<2, psi(t)=0, so the same upper bound holds there.

Put R(x)=x^(9/10) for real x>0, and use exactly the profile
F(0)=0, F(x)=x+R(x) of L733. The kernel Lambda remains the actual
arithmetic kernel, independent of F. Define, for real x>=2,

    T_R(x)=R(x) log x+sum_(n<=x) Lambda(n)R(x/n).

This is a test of one coarse inequality. It does not impose F=psi,
prime-power support of dF, any divisor identity for F, or equality of
T_R to the actual Selberg discrepancy remainder.

## Conclusion

One constant works at every real endpoint:

    0<=T_R(x)<=(10 A+10/e)x,       x>=2.                 (1)

For the same F, L733's full increment-envelope comparison remains valid,
and its complex-drift prefix energy satisfies, for every integer N>=1,

    J_N^F=inf_(a in C) sum_(j=1)^N |a j-F(j)|^2/[j(j+1)],
    |J_N^F-(5/324)N^(4/5)|<76.                          (2)

Thus imposing both L733's increment envelope and the fixed-actual-kernel
coarse O(x) test does not force N^(o(1)) prefix energy for general
profiles. This supplies no estimate for the actual-prime J_N of L732.

## Proof

### Imported input and the scope of specialization

The only external estimate used in (1) is ordinary Chebyshev upper
control of psi. A precise inspected source is G. Tenenbaum,
*Trois conferences sur la theorie analytique et probabiliste des
nombres*, Bordeaux, 7--9 December 2000, first lecture, printed p. 2,
the Chebyshev statement adjoining (1)--(2):
https://tenenb.perso.math.cnrs.fr/PPP/JER.pdf .
The source states an absolute constant, not a numerical value, so A is
left unspecified. This use is unconditional and requires no PNT error
term or power-sized seed estimate. The prior assessment is
`drafts/literature/2026-11-04-selberg-operator-power-diagnostic.md`.

Tenenbaum's equation (6), printed p. 4, concerns R_actual=psi-x.
It motivates the tested operator but is not applied to our R. The
following elementary partial-summation specialization verifies that
this different profile meets the coarse bound. The power-mode idea
was already recorded in the assessed literature; this is reproduction
of a bounded diagnostic, with no novelty claim.

### Partial summation at all real endpoints

Set b=9/10. Since Lambda(n)>=0, every summand in T_R is nonnegative.
For a real x>=2 and each integer n<=x,

    n^(-b)=x^(-b)+b integral_n^x t^(-b-1)dt.

Multiply by Lambda(n) and sum. There are finitely many terms, so
interchanging this finite sum and the integrals is justified directly.
The coefficient of t^(-b-1) is psi(t), except for isolated integer
endpoints that do not affect the integral. Consequently

    sum_(n<=x) Lambda(n)n^(-b)
      =psi(x)x^(-b)+b integral_1^x psi(t)t^(-b-1)dt.     (3)

There is no lower boundary contribution: psi(1)=Lambda(1)=0.
If x is a prime power, its atom is included in psi(x)x^(-b);
the corresponding integral from x to x is zero. Noninteger x
requires no floor replacement or endpoint error in (3).

Apply psi(t)<=A t, including 1<=t<2, in (3). Since 1-b=1/10,

    sum_(n<=x) Lambda(n)n^(-b)
      <=A x^(1-b)+(b A/(1-b))(x^(1-b)-1)
       =10 A x^(1/10)-9 A.

It follows that

    sum_(n<=x) Lambda(n)R(x/n)
      =x^b sum_(n<=x) Lambda(n)n^(-b)
      <=10 A x-9 A x^b<=10 A x.                         (4)

This keeps the finite lower endpoint in the intermediate bound rather
than treating a divergent infinite sum as a constant.

For the other term put u=log x>=0. The function u exp(-u/10)
has derivative exp(-u/10)(1-u/10); its maximum on u>=0 is
10/e, attained at u=10. Therefore

    R(x) log x/x=x^(-1/10)log x<=10/e.                  (5)

Adding (4) and (5) proves (1). It holds on the entire interval x>=2
with the displayed constant; no asymptotic onset is omitted.

### Simultaneous prefix growth and limitation

L733 proves (2) for precisely F(x)=x+x^(9/10), with a single optimized
complex drift for the whole prefix. Its increment comparison is also
for that same F. Neither result changes when the independent kernel
Lambda is used to test (1), because (1) changes neither F nor the
definition of J_N^F. In particular, (2) gives

    J_N^F>=(5/648)N^(4/5)

whenever N^(4/5)>=49248/5, as in L733. This rules out an N^(o(1))
upper conclusion from those two profile constraints alone: for
example, their common model is not O(N^(2/5)).

There is no inference that this F generates Lambda, satisfies the
actual Selberg remainder identity, or realizes any hypothetical zero.
L732 is context for the missing actual-prefix upper bound, not an
input to this proof. Scalar anchors, complementary residuals and
actual-Xi positivity remain uncontrolled. Matching a fixed O(x)
coefficient or any stronger signed residual is outside this result.
The coarse-O(x) diagnostic is exhausted; reopening it requires a
specified stronger input, not another profile or a renamed envelope.

### Independent bounded audit — 4 November 2026, step 249

Verdict: (1), (2), and their simultaneous-model interpretation pass.
This is a REPRODUCTION audit under the preapproved assessment
`drafts/literature/2026-11-04-coarse-selberg-power-audit.md`, not a new
operator estimate or a verification of an actual-prime prefix bound.

The source-domain ambiguity at 2 causes no missing hypothesis. If the
named Chebyshev estimate is read only for t>2 with constant A_0, choose
A=max(A_0,log(2)/2); then psi(2)=log(2)<=2A. For 1<=t<2,
psi(t)=0. Thus the global A required in the hypotheses exists under
either endpoint reading, without importing a numerical source constant.

For each real x>=2, the identity preceding (3) holds separately for
every integer n<=x. There are finitely many terms. For almost every
t in [1,x], the coefficient after summing their integrals is exactly
sum_(n<=t) Lambda(n)=psi(t). At an upper prime-power endpoint its
new atom is entirely in psi(x)x^(-9/10), with zero associated integral.
The lower endpoint has Lambda(1)=psi(1)=0. This verifies (3) for
integer and noninteger x without a boundary correction.

Inserting the global bound gives
A x^(1/10)+9A(x^(1/10)-1)=10A x^(1/10)-9A.
Multiplication by x^(9/10) gives (4), with its negative lower-endpoint
term retained. The other quotient is u exp(-u/10), u=log x>=0;
its derivative changes from nonnegative to nonpositive at u=10,
and its value there is 10/e. Nonnegativity of R, log x and Lambda
then verifies both sides of (1), with one constant for all x>=2.

The audited L733 bound (6) is for this identical F, identical weights,
and one optimized complex drift per full prefix. It therefore supplies
(2) unchanged. The lower-growth cutoff is also consistent:
(5/648)N^(4/5)>=76 is exactly N^(4/5)>=49248/5;
the strict error bound below 76 yields the stated lower bound there.
Consequently even the weaker O(N^(2/5)) upper conclusion fails for
this common model. No change of the independent kernel can change
this already defined F or its prefix functional.

Neither the source's actual-discrepancy equation nor F=psi was used.
In particular, checking two inequalities is not checking prime-power
support, multiplicative self-consistency, or equality to an arithmetic
remainder. Only L733 is used as a local mathematical input; L732
remains comparison context. The existing DAG row is correct. The
audit establishes the reliability of this limited stop, not a stronger
stop on Selberg methods, a new discovery, or an RH candidate.

## Mathlib

Full matching diagnostic not checked; availability unknown. Supporting
facts are finite summation/integration, Chebyshev upper control, power
integration and elementary real calculus. They are used with their
needed hypotheses above; no exact Mathlib declaration or absence
claim is asserted. L733's prefix estimate is reused without reproof.
