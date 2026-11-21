# Lemma 932: degree-sixteen inverse residual, with coherent deficit unpaid

## Hypotheses

Use exactly L930's fixed nonnegative smooth probability weight, Hardy
phase, L=log T, N=floor(T^(1/5)), T<=X<=2T, full H_-,H_+,
I_+,I_-,W_+,W_- and V_pole. All onsets below are uniform in X.
Use its audited finite bounds (3)–(4),(12); L928(3)–(5) supplies
only the arithmetic charge in the conditional application below.
No L925/L929 theorem, infinite limiting operator, RH assumption or
positivity of complex Jordan factors is used.

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-09-joint-coherent-square-test-19.md`.
The named operator input is Embree, Henningsen, Jackson and Morgan,
*Polynomial Approximation to the Inverse of a Large Matrix*, served
author manuscript, Section 2.3, Proposition 3(1), p. 7,
[author manuscript](https://vtechworks.lib.vt.edu/server/api/core/bitstreams/09f4a247-175e-4f0d-9eec-2cce887a9e9f/content),
[publication DOI 10.1137/24M1677599](https://doi.org/10.1137/24M1677599).
For an invertible diagonalizable A=Z Lambda Z^(-1), it bounds
||A^(-1)-p(A)|| by kappa(Z) times the maximum scalar approximation
error on the spectrum. Here A is real symmetric positive, so an
orthogonal diagonalization has kappa(Z)=1. The source theorem is
imported, not reproved. The explicit scalar polynomial and finite
alternating-point check below are needed to certify the prescribed
degree-16 minimizer on this particular enclosure; the cited operator
bound alone does not specify that polynomial or its numerical charge.

## Conclusion

Put A=H_-/L, C=H_+/L and Z=V_pole/L. Eventually both A and C have
spectra in [a,b]=[19/100,221/100]. There is an explicitly specified
real minimax polynomial p of degree 16 for 1/x on that interval, with

    E=max_[a,b] |1/x-p(x)|
      < (5/2)(11/20)^16,
    epsilon=b E < 1/2500.                                  (1)

The exact coherent square and its surrogate obey

    S=Z^* A^(-1) Z,  P=Z^* p(A) Z,
    (1-epsilon)S <= P <= (1+epsilon)S.                      (2)

All inequalities are Hermitian Loewner inequalities. In particular the
UNPROVED surrogate bound

    P <= (999/1000) C                                      (3)

would imply

    V_pole^* H_-^(-1) V_pole <= (1665/1666) H_+.            (4)

That conditional margin would eventually pay L930's regular residual
and L928's arithmetic charge. Neither (3) nor any positive coherent
deficit is established. The degree-16 scalar error is small enough for
this test; the missing input is the full endpoint-product estimate.
This is an auxiliary REPRODUCTION/application calculation, not a new
contraction theorem or mathematical advance beyond the assessed tools.
The completed step is EXPLORATION under the target's stated success
test. Written 9 November 2026, step21; separate critical audit pending.

## Proof

### 1. Uniform enclosure

L930 gives H_s=a_s I+2 diag(kappa)-K-K^T, ||K||<=2r,
0<=kappa<=r, r=log N<=L/5, and a_s=L+O(1), uniformly in X
and s=-1,+1. Choose a common onset so |a_s/L-1|<=1/100.
For arbitrary complex y, |y^*(K+K^T)y|<=4r||y||^2. Hence

    (a_s-4r)I <= H_s <= (a_s+6r)I,
    (19/100)I <= H_s/L <= (221/100)I.                      (5)

This checks both endpoints using the complete metrics, without claiming
that the divisor transformation is unitary or discarding its cross terms.

### 2. The prescribed scalar minimizer and exact error

Write c=(a+b)/2=6/5, d=(b-a)/2=101/100 and

    q=(sqrt(b)-sqrt(a))/(sqrt(b)+sqrt(a)),
    t=(x-c)/d,  t0=-c/d,
    R(t)=T_17(t)+2q T_16(t)+q^2 T_15(t),
    p(x)=[1-R((x-c)/d)/R(t0)]/x.                           (6)

T_j is the Chebyshev polynomial defined by T_j(cos theta)=cos(j theta).
Since t0=-(q+q^(-1))/2, direct substitution in
T_j((z+z^(-1))/2)=(z^j+z^(-j))/2 gives

    R(t0)=-(1-q^2)^2/(2q^17) != 0.                         (7)

The numerator in p vanishes at x=0, so (6) is a real polynomial
of degree exactly 16; x=0 in this formula is a removable value.
Let c0=d/(2q)>0. Then x=c0(1+2q t+q^2). For t=cos theta,
0<=theta<=pi, the real-part identity

    R(cos theta)=Re[e^(15i theta)(e^(i theta)+q)^2]

shows that R(t)/(1+2q t+q^2) has absolute value at most one.
It attains alternating values +1,-1,... at 18 successive points:
choose the continuous argument of e^(i theta)+q from 0 to pi;
the phase

    psi(theta)=15 theta+2 arg(e^(i theta)+q)

has endpoints 0,17pi and derivative

    psi'(theta)=15+2(1+q cos theta)/(1+2q cos theta+q^2)>0.

Thus psi(theta)=j*pi has one solution for each j=0,...,17.
By (6)–(7), the scalar error 1/x-p(x) attains alternating extrema
of common absolute size

    E=1/(c0 |R(t0)|)
      =[(b-a)/(2ab)] q^16.                                (8)

This also verifies minimization directly for this polynomial. If a
polynomial of degree at most 16 had smaller uniform error, its
difference from p would have alternating nonzero signs at those 18
ordered points, hence at least 17 distinct roots, which is impossible.
No uniqueness theorem or floating-point optimization is required.

The entirely rational comparisons

    b/a=221/19 < (31/9)^2
      =[(1+11/20)/(1-11/20)]^2,
    (b-a)/(2ab)=10100/4199 < 5/2

give q<11/20 and the first bound in (1). Finally

    b E < (221/100)(5/2)(11/20)^16 < 1/2500.               (9)

The last strict rational inequality and its conditional thresholds are
checked by `python3 scripts/logarithmic-gcd/coherent-square-residual-21.py`.
The complete small certificate is
`scripts/logarithmic-gcd/coherent-square-residual-21.json`.
It checks only scalar arithmetic; it does not verify (3), the spectral
enclosure proof, or any growing-matrix norm. No numerical matrix grid
or single-vector inference is involved.

### 3. Relative propagation through the full coherent square

Apply the cited Proposition 3(1) with the real symmetric A in (5).
It gives ||A^(-1)-p(A)||<=E. In the orthonormal eigenbasis,
|1-lambda*p(lambda)|<=lambda E<=b E=epsilon, so

    (1-epsilon)A^(-1) <= p(A) <= (1+epsilon)A^(-1).

Congruence by the full Z proves (2), with no separate endpoint norms.
In particular p(A)>0. If (3) held, (1)–(2) would give

    S <= [(999/1000)/(1-1/2500)] C = (1665/1666) C.

Since V_pole^*H_-^(-1)V_pole=L S and H_+=L C, this is (4).
Equivalently ||B_pole||<=sqrt(1665/1666). The norm margin is at least
1/3332, because 1-sqrt(1-u)>=u/2 for 0<=u<=1.
L930(12) is O(1/L) uniformly in X, and would eventually cost at
most 1/6664. Thus ||B_pole+R_reg||<=1-1/6664. In the exact
two-block form this bounds the magnitude of the cross term by
(1-1/6664) times the sum of the two diagonal energies, using
2uv<=u^2+v^2. L928(4) would then give a fixed positive multiple
of T L N^(-1/4) times the combined coefficient norm. L928(5)'s
relative O(T^(-9/80)/L) charge tends to zero and would be absorbed.
Every assertion in this paragraph is conditional on (3).

### 4. The coherent inequality remains unpaid

The exact endpoint expression is

    Z=(I_+ W_+-I_- W_-)/(2i),
    4P=|I_+|^2 W_+^*p(A)W_+ + |I_-|^2 W_-^*p(A)W_-
        -conjugate(I_+) I_- W_+^*p(A)W_-
        -conjugate(I_-) I_+ W_-^*p(A)W_+.                 (10)

The time averages I_+ and I_- still contain the exact Hardy phase
and weight. The two mixed products in (10) are adjoints; neither is
positive by itself or replaced by its modulus in this expression.
The calculation has supplied no collective upper bound for (10) below
4(999/1000)C, for arbitrary moving vectors and growing N.

For comparison only, inserting L930's already available absolute
endpoint bounds would produce the upper certificate

    ||C^(-1/2) P C^(-1/2)||
      <= (1+1/2500)(exp(2)+exp(2/5))^2/(4a^2),            (11)

whose right side exceeds 400, whereas (3) requires at most 0.999.
Indeed exp(2)>7 and exp(2/5)>1 already give a right side greater
than 160000/361>400. Equation (11) is an old absolute-loss mechanism,
not a new negative bound for the true operator. It is neither evidence
that (3) is false nor a reason to increase the degree. The earlier
parameter-norm floor and termwise stop remain distinct and unchanged.

The bounded attempt therefore stops at (10). Scalar inverse precision,
including minimax optimality, cannot supply the missing sign and size
of its collective mixed terms. Joint coercivity/projection, signed
realization and actual-Xi mixed positivity all remain open.

## Mathlib

Full matching coverage of this exact growing arithmetic surrogate and
its conditional error charge has not been checked. Chebyshev
polynomials, finite spectral calculus and positive Hermitian matrices
are supporting topics, not a checked formal match. No Mathlib absence
or formal verification is claimed. The rational script is not a proof
of the coherent inequality.
