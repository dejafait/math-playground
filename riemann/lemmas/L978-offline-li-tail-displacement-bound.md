# Lemma 978: absolute off-line displacement of the growing Li tail

## Hypotheses

Use the actual nontrivial zeta zeros of L018. Let Z+ be the multiset
of zeros rho=beta+i*gamma with gamma>0, including each zero according
to its order. Different real parts at one ordinate remain different
entries. Thus 0<beta<1. For every integer n>=2 put T=sqrt(n) and define

    A_n(beta+i*gamma)=2*Re[1-(1-1/(beta+i*gamma))^n],
    K_n(gamma)=2-2*cos(2*n*arctan(1/(2*gamma))).             (1)

A_n is the contribution from rho and its conjugate, paired once.
The tail gamma>T is complementary to the weak finite cutoff gamma<=T.
No avoidance of zero ordinates, RH, simplicity, finite zero list,
improved strip or sign of a Li coefficient is assumed.

## Conclusion

There is a finite constant C, independent of n, such that

    sum_(rho in Z+: gamma>sqrt(n)) |A_n(rho)-K_n(gamma)|
        <= C*sqrt(n)*log n                       (n>=2). (2)

The series is absolutely convergent, with multiplicities. More precisely,
choose any C0>0 for which N(t)<=C0*t*log t for t>=sqrt(2), where
N(t) counts Z+ entries with gamma<=t. Then (2) holds with

    C=exp(1/2)*C0*(1+2/log 2).                            (3)

Both individual tails in (1) are also absolutely convergent for each
n. The bound establishes only off-line displacement in this growing
tail. It supplies no sign or ordinate-only equality for the low head,
no full corrected arithmetic residual, and no RH conclusion.

## Proof

### Imported counting theorem and its specialization

Import E. Hasanalizade, Q. Shen and P.-J. Wong, *Counting zeros of the
Riemann zeta function*, arXiv:2107.06506v1, 14 July 2021,
[Corollary 1.2, equation (1.5), p.2](https://arxiv.org/pdf/2107.06506v1#page=2).
For the full-strip multiplicity count, its unconditional assertion is

    |N(t)-t/(2*pi)*log(t/(2*pi*e))|
        <=0.1038*log t+0.2573*log log t+9.3675,   t>=e. (4)

The counting convention, including orders and endpoints, is specified
in Section 2, equations (2.1)-(2.3), p.3; the corollary proof is on
p.15. The saved source comparison inspected these cases. No independent
replay of that paper's bounded-height numerical inputs is claimed.
Only the growth consequence N(t)=O(t*log t) is needed here, not its
error constants. The main term and each error term in (4) are bounded
in absolute value by a constant times t*log t for t>=e. On
sqrt(2)<=t<=e, monotonicity gives N(t)<=N(e), and t*log t is bounded
below by sqrt(2)*log(sqrt(2))>0. Increasing one fixed constant therefore
gives C0 in (3) on the whole required interval. This is a specialization
of the cited theorem, not a reproof of zero counting.

### Uniform kernel displacement

Fix n>=2 and gamma>T. For a real variable x in [0,1], set
q(x)=1-1/(x+i*gamma). There is no pole on this segment. Direct algebra
gives

    |q(x)|^2=((x-1)^2+gamma^2)/(x^2+gamma^2)
             =1+(1-2*x)/(x^2+gamma^2)
             <=1+1/gamma^2,
    |q'(x)|=1/(x^2+gamma^2)<=1/gamma^2.                  (5)

In the first inequality, x<=1/2 gives numerator 1-2*x<=1 and
denominator >=gamma^2; x>1/2 makes the added term negative.
Consequently the elementary inequality 1+u<=exp(u), u>=0, gives

    |(q(x)^n)'|
       <=n/gamma^2 * exp((n-1)/(2*gamma^2))
       <=exp(1/2)*n/gamma^2.                            (6)

The last step uses gamma^2>n, so it controls the exponential uniformly
on the entire tail, including near its lower endpoint. Integrating
the complex derivative along the real segment from 1/2 to beta yields

    |q(beta)^n-q(1/2)^n|
       <=|beta-1/2|*exp(1/2)*n/gamma^2
       <=exp(1/2)*n/(2*gamma^2).                        (7)

At the midpoint,

    q(1/2)=(-1/2+i*gamma)/(1/2+i*gamma)
          =(gamma+i/2)/(gamma-i/2)
          =exp(2*i*arctan(1/(2*gamma))).               (8)

Here gamma>0 fixes the arctangent in (0,pi/2); the quotient identity
is exact. Hence K_n(gamma)=2*Re[1-q(1/2)^n], and (7) gives

    |A_n(beta+i*gamma)-K_n(gamma)|
        <=exp(1/2)*n/gamma^2.                           (9)

This argument uses only 0<beta<1; no symmetry between distinct
positive-ordinate zeros is needed. Conjugation in L018 justifies the
interpretation of A_n as a single conjugate-pair contribution.

### Absolute summation and endpoints

For U>T>=sqrt(2), finite summation by parts for the right-continuous
counting function N gives exactly

    sum_(T<gamma<=U) gamma^(-2)
      =N(U)/U^2-N(T)/T^2+2*integral_T^U N(t)/t^3 dt.    (10)

All entries carry their orders. The term N(T) includes every zero
at T, which excludes precisely those atoms from the left side.
Thus no continuity of N at the cutoff is assumed. Since
N(U)/U^2<=C0*log U/U tends to zero, (10) and the convergent integral
of log t/t^2 prove convergence and imply

    sum_(gamma>T) gamma^(-2)
      <=2*C0*integral_T^infinity log t/t^2 dt
      =2*C0*(log T+1)/T.                               (11)

The limit is justified by the increasing finite sums on the left of
(10) and their displayed finite upper bound. There is no conditional
rearrangement. Sum (9), use T=sqrt(n), and obtain

    sum_(gamma>sqrt(n)) |A_n(rho)-K_n(gamma)|
      <=exp(1/2)*C0*sqrt(n)*(log n+2)
      <=exp(1/2)*C0*(1+2/log 2)*sqrt(n)*log n,           (12)

which proves (2)-(3) with one n-independent constant.

For completeness put theta=2*n*arctan(1/(2*gamma)). The real
inequalities arctan u<=u for u>=0 and 2*(1-cos theta)<=theta^2
show 0<=K_n(gamma)<=n^2/gamma^2. Thus (11) proves absolute
convergence of the model tail; (9) and the triangle inequality then
give absolute convergence of the actual paired tail as well. These
convergence assertions are for each fixed n; the individual-tail
bound is not asserted to have the smaller order in (2).

### Qualification and downstream scope

The known counting theorem is imported. The local kernel comparison
and its summation are a standard specialization under the preapproved
assessment; no originality beyond the sources checked is claimed.
No logarithm expansion, suspect contour estimate from L977, model
l2-to-pointwise inference, or infinite product identity is used.
L977 fixes the ordinary undivided conventions but is not a premise
of this bound. Likewise L968 is a downstream benchmark, not an input.
The truncated model residual, constant matching in an arithmetic
assembly, and the growing actual finite-zero sum's sign remain open.
This result does not supply the whole-Li lower bounds required there.

Written in step216, 10 November 2026. Separate conceptual audit in
step223 replayed (5)-(12), including the factor two in A_n, the
positive phase in (8), the strict lower cutoff in (10), and the
fixed-n absolute convergence of both paired tails. The conclusion
and constant (3) passed unchanged. The imported counting theorem's
constants and weak counting convention were checked against the
cited primary source; its external numerical inputs were not replayed.
This verifies the local specialization, not a new zero estimate.

## Mathlib

Full matching coverage of (2), and formal coverage of the cited counting
theorem, have not been checked and remain unknown. No Mathlib theorem
is imported. Generic finite summation by parts and elementary complex
differentiation alone would not supply the zeta counting input.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
