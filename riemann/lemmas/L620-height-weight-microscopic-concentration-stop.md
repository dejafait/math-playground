# Lemma 620: microscopic mass stop for short height weights

## Hypotheses

Fix 0<epsilon<1/11 and a nonnegative w in C_c^infinity((0,1))
with integral w=1. Let T tend to infinity, L=log T, X in [T,2T],
1<=N<=T^(1/11-epsilon) an integer, and

    M(t)=sum_(n<=N) a_n n^(-it),  sum_(n<=N)|a_n|^2=1,
    w_XT(t)=w((t-X)/T).

The complex coefficients may depend arbitrarily on T,X and the center.
Fix u0 in (0,1) with w(u0)>0 and put t0=X+u0 T,
I=[t0-1/(2L),t0+1/(2L)]. For the twisted-moment assertion fix C>0
and four complex shifts alpha,beta,gamma,delta of modulus <=C/L; put

    F(t)=zeta(1/2+alpha+it) zeta(1/2+beta+it)
         zeta(1/2+gamma-it) zeta(1/2+delta-it).

For coprime positive h,k let H_hk be the complete six-term main
integral in Hughes–Young Theorem 1.1/(17), with weight w_XT and
these shifts, including its prefactor 1/sqrt(hk). At shift collisions
use the holomorphic value of the complete sum, never separate pole
values. Its arithmetic factors are precisely (12)–(15) there.
No RH, assumed signs, prescribed coefficient growth, or Hardy/Xi
transfer theorem is a hypothesis.

## Conclusion

Uniformly over the stated parameters and coefficient vectors,

    D:=integral_R w_XT(t)|M(t)|^2 dt=T+O_w(N),             (1)
    integral_I w_XT(t)|M(t)|^2 dt <= ||w||_infinity N/L.   (2)

Consequently, beyond one onset depending only on w,epsilon,

    sup_a [integral_I w_XT |M|^2 / D]
      <= 2 ||w||_infinity N/(T L)
      <= 2 ||w||_infinity T^(-10/11-epsilon)/L=o(1).       (3)

The denominator is positive. In fact (2) holds for every real center,
not only t0. Thus this pure height-weight family fails the stipulated
necessary test of a microscopic mass fraction bounded away from zero.

The same normalization gives the coefficient-summed source remainder

    integral_R w_XT F |M|^2 dt
      =sum_(m,n<=N) a_m conjugate(a_n) H_(m/g,n/g)+R,
          g=gcd(m,n),
    |R| <= C_(w,epsilon,C) T^(3/4+epsilon) N^(11/4)
         <= C_(w,epsilon,C) T^(1-7epsilon/4)=o(T).        (4)

All terms and multiplicities of the finite coefficient sum are retained.
This is an absolute remainder, not a relative error for a possibly
canceling main sum. It is an undifferentiated four-zeta assertion;
no signed Hardy/Xi asymptotic, positivity of its main form, or bound
for the signed integrand on the complement of I is asserted.

## Proof

### Quadratic normalization and concentration

Import H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*,
J. London Math. Soc. (2) 8 (1974), 73–82,
[Corollary 3/(1.11), p. 75, proof Section 4 p. 82](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf#page=3),
[DOI 10.1112/jlms/s2-8.1.73](https://doi.org/10.1112/jlms/s2-8.1.73).
For arbitrary finite complex b_n and Y>0 this is

    integral_0^Y |sum b_n n^(it)|^2 dt
      =Y sum |b_n|^2+O(sum n|b_n|^2),                    (5)

with an absolute constant. The readable author restatement is
R. C. Vaughan, Math 597-05, Chapter 26, 2 October 2025,
[PDF p. 10](https://personal.science.psu.edu/rcv4/597-5f25/Class597-26.pdf#page=10).
The Hilbert inequality and its arithmetic mean-square consequence
are named imports, not reproofs. Only a weighted finite-sum
specialization is needed here, since (5) is unweighted.

Take b_n=conjugate(a_n)n^(iX). Then
|sum b_n n^(is)|=|M(X+s)|, sum |b_n|^2=1 and
sum n|b_n|^2<=N. Hence, uniformly for 0<=u<=1,

    A(u):=integral_0^(Tu) |M(X+s)|^2 ds=Tu+E(u),
    |E(u)|<=C_MV N.                                    (6)

The endpoint u=0 follows directly; the absolute constant in (5)
is independent of Y and of the translated coefficients. As A is
continuously differentiable and w vanishes at both endpoints,

    D=integral_0^1 w(u) A'(u) du
     =-integral_0^1 w'(u) A(u) du
     =T integral_0^1 w(u) du-integral_0^1 w'(u) E(u) du.

Thus |D-T|<=C_MV N ||w'||_1, proving (1). In particular D>=T/2
once C_MV ||w'||_1 N<=T/2, which holds uniformly at the stated
length bound for all sufficiently large T. The elementary finite
Cauchy–Schwarz inequality gives |M(t)|^2<=N sum |a_n|^2=N
for every t. Since I has length 1/L and w_XT<=||w||_infinity,
(2) follows, and division by D proves (3). No numerical experiment,
interchange of infinite sums, or conjectural local mean square is used.

### Coprime twists and their raw errors

Import C. P. Hughes and M. P. Young, *The twisted fourth moment of
the Riemann zeta function*, J. reine angew. Math. 641 (2010),
203–236, [arXiv:0709.2345v2, (11)–(17), Theorem 1.1,
printed pp. 3–5](https://arxiv.org/pdf/0709.2345v2#page=3).
The theorem evaluates integral w_XT(t)(h/k)^(-it)F(t)dt with
coprime h,k and gives H_hk plus

    O_(w,eta,C)(T^(3/4+eta)(hk)^(7/8)(T/T0)^(9/4)).     (7)

It assumes support in [T/2,4T], j-th weight derivative
O_j(T0^(-j)), T^(1/2+eta)<<T0<<T, hk<=T^(2/11-eta),
and shifts O(1/L). We use T0=T and eta=epsilon. Our support
is in [T,3T] and derivative constants depend only on w,j;
epsilon<1/11<1/2 verifies the smoothing condition. Its arithmetic
proof is imported. The full six-term sum and its collision
holomorphy are as in (17) and the subsequent remarks.

The finite identity, with the sign matching source (16), is

    |M(t)|^2=sum_(m,n<=N) a_m conjugate(a_n) (m/n)^(-it).

Writing g=gcd(m,n), h=m/g,k=n/g preserves the ratio exactly and
makes h,k coprime. Moreover

    hk=mn/g^2<=N^2<=T^(2/11-2epsilon)<=T^(2/11-epsilon).

This includes m=n, which reduces to h=k=1. The same integral
can occur several times; retaining the original pair sum preserves
all coefficient multiplicities. Applying (7) to each pair and
the triangle inequality bounds the remainder by

    C T^(3/4+epsilon)
        sum_(m,n<=N) |a_m a_n| (mn/gcd(m,n)^2)^(7/8)
    <=C T^(3/4+epsilon) (sum_(n<=N)|a_n| n^(7/8))^2
    <=C T^(3/4+epsilon) sum_(n<=N)n^(7/4)
    <=C T^(3/4+epsilon) N^(11/4).

The second inequality uses sum |a_n|^2=1; the last uses
n^(7/4)<=N^(7/4) for each of N terms. The final exponent is
3/4+epsilon+(11/4)(1/11-epsilon)=1-7epsilon/4, proving (4).
No extra 1/sqrt(hk) multiplies (7): that factor belongs to H_hk
alone. In the source's polynomial M(1/2+it) notation our
coefficients would be sqrt(n)a_n. We avoid any growth assumption
in a summed corollary by using only its individual-twist theorem.

### Relevance and limitation

L619 supplies a smooth signed Xi average; it is motivation, not
an input to (1)–(4). L018 and L471 fix the Xi/Hardy conventions
if a later signed transfer is attempted, and are likewise not
mathematical inputs to this elementary weight diagnostic. A
vanishing weight-mass fraction stops the particular proposed
height-concentration test. It does not prove that no sign-sensitive
arithmetic amplifier or joint jet weight can detect a negative
interval. In particular a bound on pure weight mass does not
bound its mass after multiplication by an unbounded signed
observable. The good source error in (4) does not repair (3).
This is a specialization of known inputs, not new arithmetic
mathematics or progress to a pointwise sign theorem.

## Mathlib

Full matching Montgomery–Vaughan, weighted concentration and twisted
fourth-moment coverage was not checked. No absence or formalization
claim is made. Finite Cauchy–Schwarz and integration by parts are
supporting elementary tools, not asserted matches for the full result.
