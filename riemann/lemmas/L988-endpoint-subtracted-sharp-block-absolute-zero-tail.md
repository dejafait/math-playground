# Lemma 988: endpoint-subtracted sharp-block absolute zero tail

## Hypotheses

Let n>=2 be an integer and use the usual generalized Laguerre
polynomials, with

    K_n(u)=[L_(n-1)^(2)(u)-1]/(n-1).

This is exactly L985's averaged kernel, not a modified weight. For
complex s!=1 put z=s-1 and define the finite ordinary integrals

    T_n(s)=integral_n^(2*n) exp(z*u)*K_n(u)du,
    E_n(s)=[exp(z*u)*K_n(u)/z]_n^(2*n),
    R_n(s)=T_n(s)-E_n(s).

The brackets mean the upper evaluation minus the lower evaluation.
Let rho=beta+i*gamma range over all nontrivial zeta zeros in
0<beta<1, counted with their analytic multiplicities. There is no
RH, simplicity, isolation, rightmost-zero, arithmetic explicit-formula
exchange or growing-height asymptotic assumption.

## Conclusion

Put P(n)=n*(n+1)*(n+2)/12. For every 0<Re(s)<1 with Im(s)!=0,

    |R_n(s)|<=P(n)*exp(n)/|Im(s)|^2.                    (1)

For every real H>=e the actual-zero tail is absolutely convergent and

    sum_(|gamma|>H) |R_n(rho)|
       <=P(n)*exp(n)*(40*log H+80*log 2)/H.             (2)

In particular, for every n>=2,

    sum_(|gamma|>exp(n)) |R_n(rho)|
       <=P(n)*(40*n+80*log 2)=O(n^4)
        =o(exp(n/2)*n^(-3/2)).                         (3)

At every finite symmetric height Y the exact identity is

    sum_(|gamma|<=Y) T_n(rho)
      =sum_(|gamma|<=Y) E_n(rho)+sum_(|gamma|<=Y) R_n(rho). (4)

No convergence, size or sign is asserted for either infinite T_n or
E_n sum, or for their identification with the actual arithmetic block.
Step251, 10 November2026: REPRODUCTION under pre-existing SPECIALIZE
review249, approved in step250. This is a local specialization of
known calculus, Laguerre and zero-counting inputs, not a discovery
beyond the checked sources or an RH candidate. Step253, 10 November2026:
independent audit passed for (1)-(4) under review251, separately
approved in step252. No stronger estimate or endpoint restoration
is claimed by this audit.

## Proof

### Imported inputs and exact differentiation

Use L985 only for the exact finite connection identifying the original
averaged kernel with the displayed K_n. Its Vaughan estimates and
asymptotic remainders are not used. Import
[NIST DLMF18.9.23](https://dlmf.nist.gov/18.9.E23), version1.2.8,
15September2026 (Szego, *Orthogonal Polynomials*, 4th ed., 1975,
(5.1.14)):

    (L_d^(alpha))'=-L_(d-1)^(alpha+1),   d>=1.

Import also [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), same
version, for integers d>=0, real alpha>=0, x>=0:

    exp(-x/2)*|L_d^(alpha)(x)|<=(alpha+1)_d/d!.

The latter source attributes its proof to T.H. Koornwinder,
*The addition formula for Laguerre polynomials*, SIAM J. Math.
Anal.8 (1977),535-540, Remark4.1. General results are imported,
not reproved. Their hypotheses include every degree, parameter and
argument below; there is no bulk-onset exception.

For every n>=2,

    K_n'(u)=-L_(n-2)^(3)(u)/(n-1),
    |K_n'(u)|<=a_n*exp(u/2),  a_n=n*(n+1)/6.           (5)

Indeed the source factor is (4)_(n-2)/(n-2)!=binom(n+1,3),
which after division by n-1 is a_n. For n>=3,

    K_n''(u)=L_(n-3)^(4)(u)/(n-1),
    |K_n''(u)|<=b_n*exp(u/2),
    b_n=n*(n+1)*(n-2)/24.                             (6)

Here (5)_(n-3)/(n-3)!=binom(n+1,4). When n=2, K_2(u)=2-u,
K_2'=-1, K_2''=0, and (5)-(6) remain valid with a_2=1,b_2=0.
Thus no negative-degree polynomial is invoked. The constant -1 in
K_n remains in both original T_n and E_n; its exact derivative
vanishes. No asymptotic error is differentiated.

### Finite endpoint identities and uniform strip bound

Since K_n is a polynomial and z!=0, two integrations by parts on
the finite interval give the exact identities

    T_n(s)=E_n(s)-(1/z)*integral_n^(2*n) exp(z*u)*K_n'(u)du,
    R_n(s)=-[exp(z*u)*K_n'(u)]_n^(2*n)/z^2
                  +(1/z^2)*integral_n^(2*n) exp(z*u)*K_n''(u)du. (7)

Both derivative endpoint evaluations are retained in (7). If
0<beta=Re(s)<1, then for u>=0,

    |exp(z*u)|*exp(u/2)=exp((beta-1/2)*u)<=exp(u/2).

Consequently (5)-(7) imply

    |R_n(s)|<=|z|^(-2)*
       [a_n*(exp(n)+exp(n/2))+2*b_n*(exp(n)-exp(n/2))]
      <=2*(a_n+b_n)*exp(n)/|z|^2.

The integral used here is exactly
integral_n^(2*n) exp(u/2)du=2*(exp(n)-exp(n/2)).
Since 2*(a_n+b_n)=P(n) and |z|>=|Im(s)|, this proves (1).
The estimates are uniform over the entire open strip and all n>=2.

### Multiplicity-counting absolute summation

Import E. Hasanalizade, Q. Shen and P.-J. Wong, *Counting zeros of
the Riemann zeta function*,
[arXiv2107.06506v1,14July2021](https://arxiv.org/pdf/2107.06506v1#page=2),
Corollary1.2/(1.5), printed p2. With N(T) counting
0<beta<1, 0<gamma<=T, with multiplicity, it states for every real T>=e

    |N(T)-T/(2*pi)*log(T/(2*pi*e))|
          <=0.1038*log T+0.2573*log log T+9.3675.       (8)

The definition is on p1 and the argument-principle multiplicity
contract in Section2/(2.3), p3. Source proof coverage and its imported
numerical inputs were reviewed in review249 and the reused review214;
no independent numerical certification is claimed here. The theorem
includes cutoffs at zero ordinates. For T>=e, log T>=1 and
log log T<=log T, so the error in (8) is at most 10*log T.
Its main term is at most T*log T/(2*pi). Using e>5/2 and pi>1,

    N(T)<=(1/(2*pi)+10/T)*T*log T<=5*T*log T.           (9)

The zeta conjugation identity preserves orders of zeros, so the
negative-height count equals the positive-height count. Partition
the required tail into disjoint shells
2^j*H<|gamma|<=2^(j+1)*H, j=0,1,... . This excludes |gamma|=H
and assigns zeros on each upper boundary to that shell, with their
full multiplicities. Equation (9) gives

    sum_(2^j*H<|gamma|<=2^(j+1)*H) 1/gamma^2
      <=2*N(2^(j+1)*H)/(2^j*H)^2
      <=20*2^(-j)/H*(log H+(j+1)*log 2).

Summing the nonnegative shell majorants uses
sum_(j>=0)2^(-j)=2 and sum_(j>=0)(j+1)*2^(-j)=4. Thus

    sum_(|gamma|>H)1/gamma^2<=(40*log H+80*log 2)/H.    (10)

Finite shell partial sums are bounded by this convergent series;
monotone convergence of nonnegative sums proves convergence and
(10), without a conditionally convergent rearrangement. In particular,
the bound on the sum above any upper height Y tends to zero as
Y tends to infinity. Applying (1) proves (2).

Set H=exp(n)>=e. The exponentials cancel in (2), proving the
explicit bound in (3). Its ratio to the requested benchmark is

    P(n)*(40*n+80*log 2)*n^(3/2)*exp(-n/2)
                         =O(n^(11/2)*exp(-n/2)) -> 0.

This is the required little-o, not a numerical comparison at finitely
many n. The sum ranges over the actual zero multiset; no known
zero-free region, verified height or fixed synthetic zero is used.

### Retained endpoints and relevance

Equation (4) follows by summing the defining finite identities;
finiteness follows from the zero-counting theorem (and discreteness
in bounded regions). In particular the removed contribution remains
exactly

    sum_(|gamma|<=Y)
      [exp((rho-1)*2*n)*K_n(2*n)-exp((rho-1)*n)*K_n(n)]/(rho-1).

It includes both endpoints and the constant correction in K_n.
Nothing in (1)-(10) assigns this series an infinite sum or signs it.
Even absolute summability of the R_n tail does not justify exchanging
a sharp arithmetic explicit formula with an integral crossing jumps.
No estimate for psi at either endpoint was used or obtained.

L987 supplies the contextual fixed-mode benchmark only; its synthetic
quartet is not a mathematical input to (1)-(4). The high remainder
is below that benchmark, but the endpoint sums, low-zero cancellation,
realization of any off-line mode, actual B_n identification and signed
upper control, both complements and L984(H) remain unpaid. The
L030-L032/C032a and L966/L968 gaps persist. The earlier uncentered
Vaughan and smooth-weight source stops are unchanged: this is a
separable remainder estimate, not a signed arithmetic mechanism.

### Independent audit, step253

The audit uses the unchanged approved derivative, global-bound and
counting contracts cited above. It checks this specialization rather
than reproving those general theorems. L985 contributes only its
finite connection (2): degree n-1, parameters alpha=1,beta=2 in
DLMF18.18.18, all coefficients (1)_j/j!=1, and removal of the
degree-zero polynomial1. Thus the -1 and denominator n-1 in K_n
are correct. Neither L985's asymptotic claims nor L987's signed
synthetic conclusion is needed for this result.

For n>=2 the first derivative has degree n-2>=0 and parameter3.
The global source constant is

    binom(n+1,3)/(n-1)=n*(n+1)/6=a_n.

For n>=3 the second derivative has degree n-3>=0 and parameter4;
its constant is

    binom(n+1,4)/(n-1)=n*(n+1)*(n-2)/24=b_n.

All arguments u in [n,2n] are positive, so these satisfy every
domain condition of the global bound. At n=3 the second derivative
is the constant1/2, consistent with b_3=1/2; at n=2,
K_2=2-u, a_2=1, b_2=0, and exactly

    R_2(s)=(exp(4*z)-exp(2*z))/z^2.

This checks the low-degree transitions without negative-degree
notation or an asymptotic onset.

Starting from T=E-z^(-1)*integral exp(z*u)K_n', the second
integration gives precisely the negative derivative bracket and
positive integral in (7). The bracket is bounded by the sum of
both endpoint moduli. With beta<1 the weighted derivative bounds
are at most a_n*exp(u/2), b_n*exp(u/2), respectively; this holds
also when beta-1/2 is negative. Thus the pre-factor before |z|^(-2)
is at most

    a_n*(exp(n)+exp(n/2))+2*b_n*(exp(n)-exp(n/2))
      <=2*(a_n+b_n)*exp(n).

Here a_n,b_n are nonnegative, exp(n/2)<=exp(n), and the integral
of exp(u/2) is exactly the one displayed above. Direct algebra
gives 2*(a_n+b_n)=n*(n+1)*(n+2)/12, including n=2.
Finally |z|^2=(beta-1)^2+Im(s)^2>=Im(s)^2. This verifies (1)
uniformly on the full asserted strip, including arbitrarily small
nonzero ordinates; no distance from a vertical boundary is assumed.

For the counting step, the imported error is at most
(0.1038+0.2573+9.3675)*log T=9.7286*log T<10*log T
for all T>=e. Also 1/(2*pi)+10/T<1/2+4<5 using only
pi>1 and e>5/2. This proves (9) even in the small-T range where
the main term of (8) is negative. Conjugation preserves analytic
orders, so 2*N(U) bounds the complete multiplicity in |gamma|<=U
with gamma!=0. No distinct-ordinate or simple-zero count is used.

For each j>=0, the denominator in its open-left, closed-right
shell is at least (2^j*H)^2, and its count is at most
2*5*(2^(j+1)*H)*log(2^(j+1)*H). Division yields exactly
20*2^(-j)*(log H+(j+1)*log2)/H. Every |gamma|>H occurs
in one shell; a zero on an upper boundary belongs to that shell,
while a zero at H is excluded. The complete infinite comparison
is justified by the two convergent positive geometric series,
with sums2 and4, giving the constants40 and80 in (10).
The proof first bounds all finite shell sums and then passes to
the nonnegative limit. It neither exchanges a conditional series
nor requires a clearance from H, even at H=exp(n).

Since n>=2, exp(n)>=e. Substitution into (2) cancels exp(n)
exactly and leaves P(n)*(40*n+80*log2), of degree4 growth.
After division by exp(n/2)*n^(-3/2), it is bounded by a constant
times n^(11/2)*exp(-n/2). The ratio of this last sequence at
n+1 and n tends to exp(-1/2)<1, proving its limit is zero.
This verifies the actual little-o in (3), not just sampled values.

For (4), every bounded symmetric zero multiset is finite: above
height e this follows from the imported count and conjugation;
the remaining bounded region has finitely many zeros by analyticity
and isolation (the pole at1 cannot be an accumulation of zeros).
Summing T=E+R over this finite multiset proves (4), with both
original endpoints and the constant correction retained. The audit
does not pass the E or T sum to infinite height, infer signs, or
identify it with B_n. Low-zero cancellation, both complements,
L981/L982's remaining quantitative uses and L984(H) stay open.
There is no change to the local mathematical inputs in the DAG.

## Mathlib

Full matching Mathlib coverage for this n-dependent endpoint-subtracted
actual-zero tail is unchecked and unknown. The precise external
mathematical inputs are cited above. Supporting polynomial calculus
or summation results would not constitute a checked formalization
of the whole statement; no absence-of-coverage claim is made.
