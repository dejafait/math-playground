# Lemma 565: complete actual-Hermite discriminant leaves the diagonal CD cone

## Hypotheses

Use the actual Xi normalization, positive even kernel Phi_R, finite
coefficients b_(2n), and physicists' Hermite partial sum P_N from L564:

    b_(2n)=1/[2^(2n)(2n)!] integral_R
                       u^(2n) exp(-u^2/4) Phi_R(u) du,
    P_N(t)=sum_(n=0)^N (-1)^n b_(2n) H_(2n)(t).

Let N>=2 be an integer and m=2N. Define

    D(P_N)=P_N'^2-P_N P_N'',
    K_j(t)=sum_(ell=0)^j H_ell(t)^2/[2^ell ell!], j>=0.

The kernel is sqrt(pi) times the usual Gaussian-weight Hermite
Christoffel–Darboux kernel, by
[DLMF Table 18.3.1](https://dlmf.nist.gov/18.3#T1) and
[18.2.12–13](https://dlmf.nist.gov/18.2.E13).
Only this explicitly defined polynomial sum is used below.

Import the standard finite Hermite formula, for integers k>=0,

    H_k(t)=k! sum_(r=0)^floor(k/2)
                   (-1)^r (2t)^(k-2r)/[r!(k-2r)!],          (1)

as stated at the beginning of §2 of Cormac O'Sullivan,
*Zeros of Jensen polynomials and asymptotics for the Riemann xi
function*, [arXiv:2007.13582v2](https://arxiv.org/html/2007.13582v2#S2),
9 December 2020. This is the physicists' normalization used in L564,
not the probabilists' Hermite polynomials or Hermite functions.

## Conclusion

There is a unique real expansion

    D(P_N)(t)=sum_(j=0)^(m-1) lambda_(N,j) K_j(t).            (2)

Its two highest weights are exactly

    lambda_(N,m-1)=2^(m+1) m! b_m^2 > 0,                   (3)
    lambda_(N,m-2)=-(m-3)2^(m+1)(m-2)! b_m b_(m-2) < 0.   (4)

Thus the proposed representation (2) with all weights nonnegative
fails for every N>=2, including every moving cutoff
N=ceil(16(T+1)^2), T>=1, in L564. This does not imply that D(P_N)
is negative anywhere, nor establish any sign for D(Xi). It is an
obstruction to this specified sufficient certificate only.

## Proof

**Actual coefficients and degree.** L564 supplies convergence of the
coefficient integrals and strict positivity of Phi_R on the positive
half-line, together with evenness. Therefore b_(2n)>0 for every
n>=0: the integrand is nonnegative on the real line and strictly
positive for u>0. In particular b=b_m and c=b_(m-2) are strictly
positive. No adjacent-coefficient asymptotic is needed for this fact.

Taking r=0,1 in (1), for k>=2,

    H_k(t)=2^k t^k-k(k-1)2^(k-2)t^(k-2)+R_k(t),

where R_k has degree at most k-4 when nonzero, and is zero for
k=2,3. Also H_0=1 and H_1=2t. It follows that

    P_N(t)=A t^m+B t^(m-2)+R(t), deg R<=m-4,
    A=(-1)^N 2^m b,
    B=(-1)^N[-m(m-1)2^(m-2)b-2^(m-2)c],
    B/A=-[m(m-1)+c/b]/4.                                  (5)

Here and below a stated degree bound includes the zero polynomial.
The second term of B comes from the n=N-1 summand, with its actual
opposite sign. Every smaller Hermite index contributes to R only.

**Complete discriminant coefficients.** Multiplying the finite
polynomials and differentiating gives

    [t^(2m-2)] D(P_N)=[m^2-m(m-1)]A^2=m A^2,              (6)
    [t^(2m-4)] D(P_N)
       =[2m(m-2)-(m-2)(m-3)-m(m-1)]AB
       =2(m-3)AB.                                        (7)

All products involving R, and the B^2 terms, have degree at most
2m-6 after the two derivatives in D. This remains true at m=4,
where R is constant and its derivatives vanish. Thus (6)–(7)
include every mixed contribution to these degrees; they are not a
sum of diagonal discriminants. The polynomial D(P_N) is even
and, since A!=0, has degree exactly 2m-2.

**Kernel coefficients and uniqueness.** By (1), H_ell has parity
ell and leading coefficient 2^ell. Consequently K_j is even,
of degree 2j, with leading coefficient

    k_j=2^j/j! > 0.                                      (8)

The m polynomials K_0,...,K_(m-1) have distinct even degrees.
They are linearly independent by taking the largest degree in any
nonzero linear combination. The real vector space of even
polynomials of degree <=2m-2 has dimension m, so they are a basis.
This proves existence and uniqueness in (2), without a sign premise.

For j>=2, the coefficient of t^(2j-2) in K_j comes only from
the two highest-index squares. The ell=j square contributes
-j(j-1)k_j/2, and the ell=j-1 square contributes
2^(j-1)/(j-1)!=j k_j/2. Therefore

    [t^(2j-2)] K_j=-j(j-2)k_j/2.                         (9)

**The two weights.** From (6) and (8),

    lambda_(N,m-1)=m A^2/k_(m-1)
                   =2^(m+1)m! b^2,

proving (3). Only K_(m-1) and K_(m-2) contribute at degree
2m-4. Equations (7) and (9), with j=m-1>=3, yield

    lambda_(N,m-2) k_(m-2)
      =2(m-3)AB + lambda_(N,m-1) k_(m-1)(m-1)(m-3)/2
      =(m-3)A^2[2B/A+m(m-1)/2]
      =-(m-3)A^2 c/(2b),                                (10)

where the last equality uses (5). Substituting A^2=2^(2m)b^2
and k_(m-2)=2^(m-2)/(m-2)! gives (4). Since m>=4 and b,c>0,
the sign is strictly negative, with no unspecified onset. For a
boundary normalization check at N=2, (3)–(4) give
lambda_(2,3)=768 b_4^2 and lambda_(2,2)=-64 b_4 b_2.

Every K_j(t)>=1 for real t, since H_0=1 and each square in its
definition is nonnegative. Nonnegative weights would therefore give
a sufficient sign certificate. Uniqueness and (4) exclude precisely
that certificate. Positive values of a polynomial need not have
nonnegative coordinates in this basis, so no converse sign inference
is valid. In L564's range T>=1 the cutoff is at least 64 and hence
is covered by N>=2. No limit interchange or transfer of signs through
the absolute derivative errors is made.

**Scope and source comparison.** This is a finite algebraic
calculation using the cited standard formula and L564's actual
positive coefficients. It is not an independent proof of Romik's
expansion or a new discovery beyond the literature checked. The
approved diagnostic allowed Romik v3 Theorem 2.7/(2.23) with its
stated relative error, but exact cancellation in (10) makes that
asymptotic unnecessary. No big-O term is differentiated and no
adjacent-ratio estimate, real-rootedness or RH is assumed. Lower
weights, D(P_N)'s sign, signed perturbation margins, multiplicities
and higher Xi forms remain unresolved by this result.

### Independent finite application audit, 2026-10-31

The approved audit passes without repair. It uses the exact finite
formula (1), not the unused adjacent-ratio asymptotic.

L564's finite integrals, evenness and strict positivity of Phi_R on
u>0 imply b_(2n)>0, including n=0. This agrees with Romik v3,
section 2.1, the statement immediately after (2.1). Thus b_m and
b_(m-2) are strictly positive. The two leading monomials of H_m
and the leading monomial of the oppositely signed H_(m-2) give (5).

In the complete discriminant, P'^2 contributes 2m(m-2)AB at degree
2m-4. The two contributions from P P'' are
[(m-2)(m-3)+m(m-1)]AB. Their difference is 2(m-3)AB.
The leading-square coefficient is mA^2. Every term involving R has
degree at most m+(m-4)-2=2m-6 after differentiation; B^2 terms
have degree at most 2(m-2)-2=2m-6. Vanishing derivatives remove
terms rather than raise degrees. This checks all contributions at
the two degrees in (6)–(7), including m=4.

The squared Hermite norm is sqrt(pi)2^ell ell!, so the normalized
orthogonal kernel is K_j/sqrt(pi), as stated. Squaring H_j's two
highest monomials and dividing by 2^j j! gives -j(j-1)k_j/2
at degree 2j-2. The next square adds j k_j/2; smaller squares
cannot contribute. This verifies (8)–(9). Distinct degrees
0,2,...,2m-2 with nonzero leading coefficients give a basis of the
entire m-dimensional even polynomial space. There is no alternative
coordinate choice with nonnegative weights. The coefficient of t^(2m-4)
after subtracting lambda_(N,m-1)K_(m-1) from D is

    -(m-3)2^(2m-1)b_m b_(m-2).

Dividing by k_(m-2)=2^(m-2)/(m-2)! gives exactly (4).

For a direct boundary check, write b=b_4, c=b_2, d=b_0. At N=2,

    P_2=a t^4+q t^2+r,
    a=16b, q=-48b-4c, r=12b+2c+d,
    D(P_2)=4a^2 t^6+2aq t^4+(2q^2-12ar)t^2-2qr,
    K_3=(4/3)t^6-2t^4+3t^2+3/2,
    K_2=2t^4+3/2.

Matching t^6 and t^4 gives lambda_(2,3)=3a^2=768b^2 and
lambda_(2,2)=aq+3a^2=-64bc. The constant r, including b_0
and all its mixed terms, affects only lower weights. This independent
expansion verifies the initial case.

For every T>=1, L564's N=ceil(16(T+1)^2) is an integer at least
64. The result holds for every N>=2 without an onset or upper cutoff;
ceiling jumps and [T,2T] endpoints cause no exception. The identity
holds on the whole real line, without a limit passage or division by
P_N or Xi. This audit checks only the cone obstruction and its cutoff
application, not either discriminant's sign or the imported manuscript
proofs. No mathematical dependency is added.

## Mathlib

Coverage of the full obstruction and supporting Hermite identities
has not been checked. Availability is unknown; absence or formal
verification is not claimed. General reference:
https://leanprover-community.github.io/mathlib4_docs/
