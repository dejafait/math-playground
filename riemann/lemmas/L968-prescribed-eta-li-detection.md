# Lemma 968: prescribed regularized Li signs suffice for RH

## Hypotheses

Use the actual Xi function of L018 and the paired nodes
beta_j=alpha_j^(-2) of L024, with all multiplicities. Fix one finite
real A>0 such that sum_j |beta_j|<=A; L024 guarantees such an A,
independently of n. For every integer n>=1 define

    P_n(z)=sum_{k=0}^{floor((n-1)/2)}
               (-1)^k binom(n,2k+1)(z/4)^k,
    a_n(z)=P_n(z)(1+z/4)^(-n/2),
    eta_n=1/(64*9^n),
    Q_n=sum_j beta_j^2 a_n(beta_j)^2/(beta_j+eta_n).          (1)

The analytic branch in a_n is the one with a_n(0)=n on |z|<4,
as in L964. Thus Q_n is precisely L966's prescribed Q_eta(n).
All squares are algebraic. Write lambda_n for the ordinary zeta Li
coefficient used in L964, without division by n. No RH, simple-zero
assumption, supplied negative Li coefficient, or sign of Q_n is
assumed for the unconditional estimate below.

## Conclusion

For every integer n>=1, both sums in the following comparison are
absolute and real, and the same A satisfies

    Q_n-lambda_n <= A/8.                                   (2)

Consequently the additional hypothesis

    Q_n>=0 for every integer n>=1                          (3)

implies RH. In particular, proving L966's complete inequality
R_n<=N_n for every n would suffice; that inequality is not proved here.

More precisely for detection, if RH is false,
there are epsilon_0>0 and strictly increasing positive integers n_k
such that

    Q_(n_k) < -k*exp(epsilon_0*n_k)   for every k>=1.        (4)

This is a conditional, non-effective subsequence assertion. It
supplies no actual negative index, zero, or counterexample to RH.
The proof was written in step172 and passed independent conceptual
audit in step174 on 10 November 2026, with its statement and constants
unchanged. It specializes a known Li criterion, not a new growth theorem.

## Proof

### Applicable pre-margin estimates

L018 gives exact zero correspondence and conjugation symmetry.
L026 gives, for alpha=x+iy, |x|>4 and |y|<1/2. Hence every node
z=alpha^(-2) satisfies

    |z|=1/(x^2+y^2)<1/16,
    Re z=(x^2-y^2)/(x^2+y^2)^2>0.                          (5)

The paired beta multiset is invariant under conjugation, regardless
of the choices of alpha representatives. L024 supplies its absolute
mass. Choosing, for example, A=1+sum_j |beta_j| establishes the
existence of a positive A used simultaneously at every n. No
effective numerical bound on A is needed.

For each fixed n, put h_n(z)=a_n(z)^2 and C_n=8*9^n. Import the
paired identity and analytic estimates L964(7),(9)-(10):

    lambda_n=sum_j beta_j h_n(beta_j),                      (6)
    |a_n(z)|<=3^n                         (|z|<=1/4),
    |h_n(z)-n^2|<=C_n |z|                 (|z|<=1/8).       (7)

These parts of L964 are independent of its negative-margin
hypothesis: (6) comes from its absolute paired Weil-form identity,
and (7) from the finite binomial formula and Cauchy's bound on
|z|=1/4. The identity uses actual nodes and preserves multiplicities;
it does not replace them by ordinates. The hypothesis
lambda_n<=-epsilon and the margin-dependent choice of eta are used
only later in L964's supplied-margin conclusion. We do not import
that conclusion or its final epsilon/8 bound at our different eta.
This verifies the scope of the reused estimates rather than
reproving the source's Li identity or growth criterion.

Here 0<eta_n<=1/576<1/16, so it also lies in L964's allowed
regularization range. At a node, |z+eta_n|>=eta_n and (7) gives

    sum_j |beta_j h_n(beta_j)| <=9^n A,
    sum_j |beta_j^2 h_n(beta_j)/(beta_j+eta_n)|
        <=(9^n/eta_n) sum_j |beta_j|^2
        <=9^n A/(16 eta_n)<infinity.                       (8)

These are complete sums, not finite heads. Conjugation commutes
with h_n and the rational denominator. Absolute convergence and
the conjugate multiset therefore make lambda_n and Q_n real.

### The one-sided bound for the prescribed family

For a node z, direct subtraction gives the same identity as
L964(12), now with the prescribed eta_n:

    z^2 h_n(z)/(z+eta_n)-z h_n(z)
      =-eta_n n^2 z/(z+eta_n)
       -eta_n z(h_n(z)-n^2)/(z+eta_n).                     (9)

Because Re z>0 and eta_n>0,

    Re(z/(z+eta_n))
       =(|z|^2+eta_n Re z)/|z+eta_n|^2>0,
    |z+eta_n|>=|z|,
    |z+eta_n|>=eta_n.                                    (10)

Both separated series on the right of (9) converge absolutely:

    sum_j |eta_n n^2 beta_j/(beta_j+eta_n)| <=n^2 A,
    sum_j |eta_n beta_j(h_n(beta_j)-n^2)/(beta_j+eta_n)|
        <=eta_n C_n sum_j |beta_j| <=eta_n C_n A.          (11)

The second estimate uses the node disk in (5), (7), and the first
modulus comparison in (10). Thus real parts may be summed in (9).
The first term has nonpositive real part at each node; its entire
series is retained before using this favorable sign. The remaining
series is bounded above by its absolute sum in (11). Together with
the reality already proved, this gives

    Q_n-lambda_n <=eta_n C_n A
        =(1/(64*9^n))*(8*9^n)*A=A/8,                      (12)

which proves (2). This is not an absolute-error assertion.
In particular the n^2 term has not been bounded in absolute value
by A/8 or assumed uniformly small. Every convergence argument above
is for each finite n. No interchange of an n-limit with a zero sum,
nor a summable majorant uniform in n, is used. The bound (12) itself
has the same constant for all n because its explicit factors cancel.

### Imported one-sided Li criterion and its specialization

Import J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier 57(5) (2007), 1689-1740,
[Theorem 2.4(2), equation (2.21), pp.1702-1703](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=15).
For the source's completed L-function of an irreducible cuspidal
unitary automorphic representation, RH is equivalent to

    for every epsilon>0 there exists C(epsilon)>0 such that
    Re(lambda_n)>=-C(epsilon)*exp(epsilon*n)
    for every integer n>=1.                              (13)

The primary zeta specialization and normalization were inspected in
the saved step171 assessment. The source includes the trivial GL(1)
representation and identifies its entire completion as 2*xi on
p.1697. Its definitions (1.1)-(1.3), p.1690, give ordinary Li
coefficients, with multiplicities and star convergence for the linear
zero formula. Multiplication of xi by 2 does not affect these
coefficients: in the derivative definition its contribution is the
nth derivative of s^(n-1)*log(2), which is zero for n>=1. Thus the
source's zeta coefficients are exactly the real lambda_n in (6),
as also checked in L964. Its RH is precisely the target identified
in L018. No change to the source's automorphic hypotheses is being
claimed beyond its explicitly included zeta case.

For source-version identification, the same criterion is Theorem
2.2(2), equation (2.39), in
[arXiv:math/0404394v4, 4 May 2005](https://arxiv.org/html/math/0404394v4).
The published theorem and numbering above are canonical here.
Its proof imports the corollary to Bombieri-Lagarias Theorem 1.
We import (13) by this precise primary citation and do not reprove
that corollary or use an uninspected author copy. No Voros
asymptotic or effective negative-index estimate is used.

Assume (3). Rearranging (12), with the correct one-sided direction,
gives simultaneously for every n>=1

    lambda_n>=Q_n-A/8>=-A/8.                              (14)

For an arbitrary epsilon>0 take C(epsilon)=A/8>0. Since
exp(epsilon*n)>=1 for n>=1, (14) gives exactly (13), for every
epsilon and every index. The cited theorem yields RH. A single
prescribed exponential rate would not suffice; the constant lower
bound establishes all of the source's required rates at once.

For completeness, the sign-sensitive subsequence follows from the
same criterion without any effective onset. If RH fails, its logical
contrapositive is

    there exists epsilon_0>0 such that for every C>0
    some integer n>=1 has lambda_n<-C*exp(epsilon_0*n).    (15)

Set n_0=0. Given n_(k-1), let

    B_k=max({0} union
            {max(0,-lambda_r)*exp(-epsilon_0*r):
                                       1<=r<=n_(k-1)}),
    C_k=k+A/8+1+B_k.

This is finite because the prefix is finite. Use (15) with C=C_k
and call its witness n_k. Every r<=n_(k-1) satisfies
lambda_r>=-B_k exp(epsilon_0*r)>-C_k exp(epsilon_0*r),
so n_k>n_(k-1). Finally (12) gives

    Q_(n_k)<-C_k exp(epsilon_0*n_k)+A/8
            <=-(C_k-A/8) exp(epsilon_0*n_k)
            <-k exp(epsilon_0*n_k),

proving (4), including the infinite-subsequence quantifiers. This
argument is conditional on failure of RH and is not an algorithm
for certifying an actual negative coefficient or computing n_k.

### Scope and unresolved signs

The local specialization is (12) at the fixed prescribed family;
the known Li criterion supplies the implication after (14). No
novelty beyond the checked sources is claimed. In particular no
pointwise sign of the complex algebraic squares has been assumed.
L966's exact identity Q_n=N_n-R_n makes its all-n integrated
inequality sufficient by the result above, but provides none of
those signs. The pointwise payment profile stopped by L967 remains
stopped; a new integrated estimate would need its own assessment.
The effective finite-window/mixed-degree problem is also untouched.
Finite numerical signs cannot replace (3). This is a conditional
detector and not a complete argument for RH or its negation.

### Independent conceptual audit, step174

The audit accepts (1)-(15) under the stated actual-Xi hypotheses.
It reuses the approved step173 assessment and step171's inspected
primary theorem, including its ordinary normalization and zeta case.
No new source, growth theorem, numerical sign or hypothesis is added.

First, neither the paired identity L964(7) nor its analytic bounds
(9)-(10) uses the supplied negative margin in L964's statement. The
identity groups an absolute quadratic zero sum into sign pairs, each
containing two zeros of equal multiplicity by L018. L024 excludes a
zero at the origin. The two identical contributions per sign pair
cancel the factor 2 in the source identity; there is no additional
pairing by conjugation. The beta multiset remains conjugation-invariant
even for a sign pair fixed by conjugation. The completion 2*xi used
in the source gives the same ordinary lambda_n, since the nth
derivative of s^(n-1)*log(2) vanishes. No division by n occurs.

Second, the node disk is strictly smaller than both analytic disks
in (7). The Cauchy estimate is the geometric sum
9^n*4|z|/(1-4|z|)<=8*9^n|z| for |z|<=1/8. L026 supplies
Re(beta)>0 without RH; this justifies both denominator comparisons
in (10). The value eta_n<=1/576 is positive for every finite n.
L024 supplies one n-independent A, not a separately chosen sequence
of tail masses. These facts verify all hypotheses of (8) and (11).

In particular the separated first term in (9) is absolutely summable
because eta_n/|beta+eta_n|<=1; its absolute sum is at most n^2*A.
Only after convergence is secured is its nonpositive real part used.
For the second term, |h_n(beta)-n^2|<=C_n|beta| and
|beta+eta_n|>=|beta| give the summable bound eta_n*C_n|beta|.
Thus (12) is an upper error, with exact constant
eta_n*C_n*A=A/8. It is not an absolute error, and it does not need
the n^2*A bound to be uniform in n. Conjugation and absolute convergence
justify every assertion of reality and every real-part summation.

Third, Q_n-lambda_n<=A/8 rearranges to lambda_n>=Q_n-A/8.
Under the all-index sign hypothesis this gives the same lower bound
-A/8 at every index. Taking C(epsilon)=A/8 works for each epsilon>0
in the primary criterion; no fixed-rate or eventual-only assertion
is substituted. L018 identifies its zeta RH with the local goal.
For the contrapositive, failure of the every-epsilon condition gives
one epsilon_0 for all subsequent choices of C. The finite B_k excludes
all indices through n_(k-1), including equality cases because C_k>B_k.
Finally exp(epsilon_0*n_k)>=1 and C_k-A/8>k give precisely (4).
The construction supplies no effective index or actual negative sign.

Lastly, L966(1) is the identical prescribed observable, and L966(4)
makes its complete (16) equivalent to the needed sign at each n.
That equality contributes no sign estimate. The audit found no defect
or missing premise and leaves the DAG row unchanged. The all-n
comparison remains unproved; L967's fixed-profile obstruction and
the finite-window/mixed-degree source limitation remain untouched.
This establishes an audited local specialization of the known
criterion, not progress beyond the checked literature's Li theorem.

## Mathlib

Full matching coverage of the prescribed-eta detector or the cited
one-sided Li criterion has not been checked and is unknown. No
Mathlib theorem is imported. Generic summation and real-inequality
support alone would not establish the Li normalization, analytic
identity or source criterion used here. Reference portal:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
