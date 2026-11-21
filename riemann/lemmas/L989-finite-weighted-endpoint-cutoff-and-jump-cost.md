# Lemma 989: finite weighted endpoint cutoff and jump cost

## Hypotheses

Let n>=2 be an integer, H=exp(n), x_1=exp(n), x_2=exp(2*n),
u_j=log x_j, and use the exact kernel and endpoint transform of L988:

    K_n(u)=[L_(n-1)^(2)(u)-1]/(n-1),
    E_n(s)=[exp((s-1)*u)*K_n(u)/(s-1)]_n^(2*n), s!=1.

L985 identifies this K_n with the original finite averaged kernel.
Let rho range over actual nontrivial zeta zeros with analytic
multiplicity. Every zero sum below has the closed cutoff |Im rho|<=H.
Let Lambda be the actual von Mangoldt function, including all prime
powers, and define, for real x>=4,

    A(x)=sum_(m<=x) Lambda(m)/m,
    J(x)=Lambda(x)/(2*x) if x is an integer prime power, and 0 otherwise,
    V(x)=sum_(k>=1) x^(-2*k-1)/(2*k+1).

A has full arithmetic endpoint weight. No RH, zero simplicity,
prime-power separation, zero-ordinate clearance, infinite-height
exchange or identification with B_n is assumed.

## Conclusion

There are source remainders r_j=R_1(x_j,H,1) such that exactly

    sum_(|Im rho|<=H) E_n(rho)
      = K_n(2*n)*(2*n-gamma_E+V(x_2)-A(x_2))
        -K_n(n)*(n-gamma_E+V(x_1)-A(x_1)) + Delta_n,       (1)
    Delta_n=K_n(2*n)*(r_2+J(x_2))-K_n(n)*(r_1+J(x_1)).   (2)

Here gamma_E is Euler's constant. For an absolute constant C from
the imported theorem, the complete source remainder cost satisfies

    |K_n(2*n)*r_2-K_n(n)*r_1|
      <= C*((81/2)*n^3+18*n^3*exp(-n/2)
                      +8*n^2*exp(-n)+4*n^2*exp(-n/2)),  (3)

and the full-endpoint conversion cost satisfies

    |K_n(2*n)*J(x_2)-K_n(n)*J(x_1)|
      <=2*n^2*exp(-n)+n^2*exp(-n/2).                   (4)

Consequently

    |Delta_n|=O(n^3)=o(exp(n/2)*n^(-3/2)).              (5)

This tests only the cutoff and jump error. In particular (1) retains
the two signed weighted arithmetic prefixes; it does not bound their
combined size or sign. Step256, 10 November2026: REPRODUCTION under
the pre-existing SPECIALIZE assessment review254, separately approved
in step255. This is a local specialization of known tools, not a new
signed prime estimate beyond the sources checked or an RH candidate.

## Proof

### Imported theorem and exact signs

Import O. Gorodetsky, *Smooth numbers and the Dickman rho function*,
[arXiv2211.08973v6, 19December2023](https://arxiv.org/pdf/2211.08973v6#page=15),
Section5.2, Lemma5.2, printed p15, (5.5)-(5.6), including its explicit
s=1 convention and AppendixA, pp21-22. The inspected theorem and
qualifications are transcribed in the notebook's
[canonical source input](../foundations/2026-11-10-finite-weighted-landau-input.md).
Its implied constant is absolute. The proof is imported, not repeated.
The theorem has x>=4, T>=2+|Im(s)|, midpoint prime-power weight and a
closed zero cutoff, with analytic multiplicities. Its separate s=1
statement handles the pole; no singular-parameter limit is taken here.
Our x_j>=exp(2)>4 and H>=exp(2)>2 meet its hypotheses at s=1.

Write G_H(x)=sum_(|Im rho|<=H) x^(rho-1)/(rho-1). The source states

    A(x)-J(x)=log x-gamma_E-G_H(x)+V(x)+R_1(x,H,1).

The trivial-zero series V converges absolutely for x>=4. Rearranging,

    G_H(x)=log x-gamma_E+V(x)-A(x)+J(x)+R_1(x,H,1).     (6)

In particular the jump has a plus sign in G_H. By the definition of
E_n, its finite zero sum is exactly K_n(2*n)*G_H(x_2)-K_n(n)*G_H(x_1).
Substitution of (6) proves (1)-(2), including the minus sign on the
entire lower endpoint. All zero sums here are finite, and rho-1!=0.
No integration across arithmetic jumps, conditional rearrangement or
passage to an infinite zero sum occurs. The -1 in K_n has been kept
at both endpoints, including in every term of (1)-(2).

### Global kernel bound

Import [NIST DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), version1.2.8,
15September2026: for integer d>=0, alpha>=0 and real u>=0,

    exp(-u/2)*|L_d^(alpha)(u)|<=(alpha+1)_d/d!.

The source attributes the bound to T.H. Koornwinder, *The addition
formula for Laguerre polynomials*, SIAM J. Math. Anal.8 (1977),
535-540, Remark4.1. Review249's inspected scope is reused. Apply it
with d=n-1 and alpha=2, obtaining the factor
(3)_(n-1)/(n-1)!=n*(n+1)/2. Only after retaining the exact -1 use
the triangle inequality:

    |K_n(u)|<=[n*(n+1)/(2*(n-1))]*exp(u/2)+1/(n-1)
             <=2*n*exp(u/2), u>=0, n>=2.              (7)

For the last inequality, exp(u/2)>=1 and
4*n*(n-1)-n*(n+1)-2=(n-2)*(3*n+1)>=0. Thus (7) covers n=2
and has no asymptotic onset. The source is not reproved; (7) is the
needed normalization for this kernel.

### Nearest other prime power and every source error

For x>=4 let x' be any nearest prime power other than x itself,
and let <x>=|x-x'|, as in the source. A candidate distinct from x
within distance x/2 always exists. If x is not a power of2, choose
q=2^floor(log(x)/log(2)); then x/2<q<x and q>=2. If x is a
power of2, choose q=x/2>=2. Both choices are prime powers distinct
from x, including when x itself is a different prime power.
Therefore |x-x'|<=x/2 and x'>=x/2. This argument bounds proximity
from above; it assumes no positive lower separation.

The full error bound of Lemma5.2 at s=1 is

    |R_1(x,H,1)|<=C*((log x)/x'*min{1,x/(H*<x>)}
                   +log^2(x*H)/H*(2+1/(2*log x))).     (8)

Use only min{1,...}<=1 and x'>=x/2; this remains valid at an exact
prime power because x' excludes x. Thus, writing u=log x,

    |R_1(x,H,1)|<=C*(2*u/x+(u+n)^2/H*(2+1/(2*u))).    (9)

The source's closed-cutoff contour costs are already included in
(8); there is no omitted good-height or zero-clearance error.
At u=n and 2*n, respectively, (9) gives

    |r_1|<=C*(2*n*exp(-n)+9*n^2*exp(-n)),
    |r_2|<=C*(4*n*exp(-2*n)+(81/4)*n^2*exp(-n)).      (10)

Indeed 4*(2+1/(2*n))<=9 and 9*(2+1/(4*n))<=81/4 for n>=2.
Multiplying these inequalities by (7), namely
|K_n(n)|<=2*n*exp(n/2) and |K_n(2*n)|<=2*n*exp(n), proves
(3). All terms of the imported error, at both endpoints, are paid.

### Full jumps, benchmark and remaining gap

At a prime power x=p^a, Lambda(x)=log p<=log x; otherwise J=0.
Hence in either case 0<=J(x)<=log(x)/(2*x). Multiplication by (7)
at the two endpoints proves (4), with their signs retained in (2)
before the absolute estimate. Although no prime-power coincidence
is assumed, this covers one if it occurs; no transcendence argument
or distance hypothesis is used to erase a jump.

Equations (3)-(4) give O(n^3), with an absolute implied constant.
Its ratio to the requested benchmark is

    O(n^(9/2)*exp(-n/2)) -> 0,

which proves (5). L987 is only the motivation for this comparison
scale; its synthetic quartet and signed conclusion are not inputs.

The cutoff choice H=exp(n) passes this technical test, so there is
no separation obstruction from (8) or the full jumps. Formula (1)
still contains -K_n(2*n)*A(x_2)+K_n(n)*A(x_1), the continuum and
gamma_E terms, and both trivial-zero series. None is discarded or
given an unproved signed bound. Nor does this lemma control L988's
low-zero R_n sum. Its absolute high-zero remainder result does not
identify B_n or supply cancellation with (1). Actual signed prefixes,
low-zero cancellation, both complementary ranges, L984(H), and the
L030-L032/C032a and L966/L968 gaps remain open. The earlier Vaughan,
automatic-average and smooth-weight stops retain their stated scope.

### Independent audit — step258, 10 November2026

Under review256, separately approved in step257, independently replayed
(1)-(10) using the unchanged primary contracts in the canonical source
input and reviews254/249. This is REPRODUCTION of a known-tool local
specialization. The general explicit formula and Laguerre inequality
are imported by the precise citations above, without reproof.

**Hypotheses and finite identity.** At s=1 the source explicitly uses
its pole convention; x_j>=e^2>4 and H>=e^2>2 meet its requirements.
Every actual nontrivial zero is different from 1. The bounded-height
zero multiset is finite, with analytic multiplicities, and its closed
cutoff is exactly the source cutoff since Im(s)=0. The source equation
A-J=u-gamma_E-G_H+V+r rearranges to (6), with +J and +r. Thus
K_n(2n)G_H(x_2)-K_n(n)G_H(x_1) gives precisely (1)-(2), including
the minus sign on every lower-endpoint term. The positive trivial-zero
series converges absolutely by comparison with a geometric series.
No differentiation in s or infinite zero-sum limit is needed.

**Normalization and small degree.** L985's finite connection agrees
with L988's exact E_n definition, including the constant -1. DLMF at
degree n-1, parameter2 and u>=0 gives n(n+1)/2. After division by
n-1 the sufficient inequality in (7) is equivalent to
4n(n-1)-n(n+1)-2=(n-2)(3n+1)>=0. In particular it holds at n=2
with no negative degree or asymptotic onset. Neither the -1 nor its
two endpoint contributions has been removed from the identity.

**Arithmetic proximity.** If x is not a power of2, the indicated
power of2 is strictly between x/2 and x. This includes nonintegers
and prime powers of another prime. If x is a power of2, x/2>=2
is a distinct prime power at distance x/2. Hence every nearest
other prime power satisfies |x-x'|<=x/2 and x'>=x/2. The proof
uses an upper bound on distance, then min{1,...}<=1; it never
introduces inverse separation, even at an arithmetic jump.

**Complete error arithmetic.** Substitution of s=1 in the source
gives exactly (8), including the second summand 1/(2u). At u=n,
4(2+1/(2n))<=9 for n>=2; at u=2n,
9(2+1/(4n))<=153/8<=81/4. Thus the slightly coarser (10) holds
uniformly. Multiplying its upper-endpoint terms by 2n*e^n gives
8n^2*e^(-n)+(81/2)n^3. Multiplying its lower-endpoint terms by
2n*e^(n/2) gives 4n^2*e^(-n/2)+18n^3*e^(-n/2). These are
all four terms of (3), with the same absolute source constant.
The source contract includes the return to the closed cutoff;
there is no additional unestimated ordinate-clearance term.

For a full arithmetic endpoint, 0<=J(x)<=u/(2x), since
Lambda(p^a)=log p<=log(p^a). The upper and lower products are
respectively at most 2n^2*e^(-n) and n^2*e^(-n/2), proving (4)
also when either or both jumps vanish. Signs were retained before
taking absolute values. Equations (3)-(4) prove O(n^3) with an
absolute, not necessarily effective or numerically evaluated, constant.
The benchmark ratio is O(n^(9/2)*e^(-n/2))->0, establishing strict
little-o and (5). All degrees n>=2 and both endpoint conversions
are covered; no numerical experiment substitutes for this limit.

Audit decision: accept L989(1)-(10) without mathematical correction.
Its direct mathematical inputs remain L985's exact connection and
L988's endpoint definition, as recorded in the existing DAG row.
L987 is a contextual benchmark, not a premise. This certifies only
the technical cutoff/jump component. It neither improves the cited
general theorems nor bounds the retained signed arithmetic prefixes,
the low-zero R_n sum, actual B_n or either complementary range.
L984(H), L030-L032/C032a and L966/L968 remain open. Further audits
or absolute cutoff refinements alone are not a signed mechanism.

## Mathlib

Full matching Mathlib coverage of the finite weighted theorem and
this n-dependent endpoint error comparison is unchecked and unknown.
No formal verification or absence-of-coverage claim is made. Supporting
finite algebra alone would not supply the imported explicit formula
or the unresolved signed arithmetic estimate.
