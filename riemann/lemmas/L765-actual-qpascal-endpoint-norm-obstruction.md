# Lemma 765: actual q-Pascal endpoint norm obstruction

## Hypotheses

Use the completion xi of L018 and the strictly positive moments M_(2n)
of L021. For integers n>=0 put

    gamma_n=n! M_(2n)/(2n)!,
    a_n=gamma_n/(8*4^n*n!)>0,  f(n)=log(a_n).

For integers r>=2 set k=1024r, d=r-1, and define

    rho=a_(k+1)/a_k,
    q=a_(k-1)*a_(k+1)/a_k^2,  tau=-log(q),
    h_s=f(k+s)-f(k)-s*(f(k+1)-f(k))+tau*s*(s-1)/2.

All required indices k+s, |s|<=d, are positive. When 0<q<1 define
r by r real matrices, indexed from zero, by

    V_ij=q^(i*j),
    L_ij=[i choose j]_q if i>=j, and 0 otherwise,
    D_m=product_(h=0)^(m-1)(q^m-q^h),  D_0=1,
    E_ij=V_ij*(exp(h_(d-i-j))-1),
    F=|D|^(-1/2)*L^(-1)*E*L^(-T)*|D|^(-1/2).

Here |D| is diagonal with entries |D_m|, and ||.||_2 is the induced
Euclidean operator norm. These are exactly the source's unmodified
log-quadratic model and error normalization, not a cubic truncation.

## Conclusion

As r tends to infinity through integers, k*tau tends to 2, so eventually
0<q<1. With alpha=1/1024,

    h_(r-1)/r -> C
      =2*alpha^2*integral_0^1 v*(1-v)/(1+alpha*v) dv
      =[alpha^2+2alpha-2*(1+alpha)*log(1+alpha)]/alpha,

and

    1/3148800 = alpha^2/[3*(1+alpha)] < C < alpha^2/3 = 1/3145728.

For every sufficiently large r,

    ||F||_2 >= exp(h_(r-1))-1 >= exp(r/6297600)-1 -> infinity.

In particular the sufficient criterion ||F||_2<1 fails eventually on
this ray. No effective onset, negative minor, failure of hyperbolicity,
or counterexample to RH is asserted. This is a local quantitative
specialization of known asymptotics and a known comparison method;
the source already warns qualitatively that its proved method does not
reach bounded k/r. A separate conceptual audit on 2026-11-04 (step388)
verified the stated asymptotic, finite-value error budget and exact
matrix normalization. It did not audit the source's full tail theorem.

## Proof

### Imported input and exact normalization

Cormac O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the
Riemann xi function*, arXiv:2007.13582v2 (9 December 2020),
[Theorem 1.4 and (1.8)](https://arxiv.org/html/2007.13582v2#S1),
gives the coefficient expansion used below at fixed order K=2.
Its (1.2) defines gamma_n=n! xi^(2n)(1/2)/(2n)!, matching the moments
above: substituting z=-it in L021 and using L018 gives
xi(1/2+t)=sum_n M_(2n)*t^(2n)/(2n)!.
We import that theorem, without reproving its saddle analysis.

Wojciech Michałowski, *An explicit uniform cubic wedge for consecutive
Toeplitz minors of the Riemann xi-coefficients*, arXiv:2607.16795v1
(18 July 2026), [Lemma 4.1](https://arxiv.org/html/2607.16795v1#S4),
[(6)](https://arxiv.org/html/2607.16795v1#S5), and
[Lemma 6.1 and Section 6](https://arxiv.org/html/2607.16795v1#S6),
provides the exact factorization V=L D L^T and sufficient inertia
criterion used here. Its (2) and G(z)=Theta(z/4)/8 match a_n above.
Only this finite matrix interface is used, not the cubic-wedge theorem,
Gate A derivative estimates, Gate C majorants, or its certificates.

For clarity, the positive diagonal normalization is checked directly.
Write Q_ij=a_(k+d-i-j), R=diag(rho^(-i)), and
B_ij=q^((d-i-j)*(d-i-j-1)/2)*exp(h_(d-i-j)). Then

    Q=a_k*rho^d * R*B*R,
    B=(a_k*rho^d)^(-1) * R^(-1)*Q*R^(-1).

Thus it is diag(rho^i) that normalizes Q in this direction; this resolves
the inverse-diagonal placement in the source's normalization prose.
Put c_d=q^(d*(d-1)/2) and
A=diag(q^(i*(i+1)/2-d*i)). Expanding (d-i-j)*(d-i-j-1)/2 gives

    B=c_d*A*(V+E)*A.

Since V=L D L^T and all D_m are nonzero for 0<q<1, its model is
S J S^T with S=sqrt(c_d)*A*L*|D|^(1/2) invertible and
J=diag((-1)^m). Whitening the perturbation gives exactly the displayed
F: the factors c_d and A cancel. All matrices are real symmetric where
required. Hence the source's norm<1 condition applies to exactly this F,
without a tail-wedge restriction on this finite algebra. Its failure is
only failure of that sufficient condition, not failure of inertia.

Explicitly, with DeltaB=c_d*A*E*A, one has
S^(-1)=c_d^(-1/2)*|D|^(-1/2)*L^(-1)*A^(-1), so
S^(-1)*DeltaB*S^(-T)=F. For the original Q the model factor is
S_Q=sqrt(a_k*rho^d)*R*S; its perturbation is
DeltaQ=a_k*rho^d*R*DeltaB*R. Thus
S_Q^(-1)*DeltaQ*S_Q^(-T)=F as well. This checks both directions of
the positive congruence without commuting L past a diagonal matrix.
The source's Newton-elimination and homotopy proofs were inspected in
the audit; only their finite-dimensional identities are imported.

### Finite-value asymptotic with adequate error

For positive real x put w=W(2x/pi), with W the positive Lambert branch,
and set

    c1(w)=-(w^4+58w^3+29w^2-24w-16)/(192*(w+1)^3),
    U(x)=x*(2+2log(w)-log(64)-2log(x)-2/w),
    B0(x)=log(pi^2/2)+7w/4+log(w/(w+1))/2-log(2pi*x)/2
               +(c1(w)-1/12)/x,
    G(x)=U(x)+B0(x).

O'Sullivan's K=2 expansion, logarithmized, and the classical logarithmic
Stirling expansion

    log(n!)=(n+1/2)log(n)-n+log(2pi)/2+1/(12n)+O(n^-3)

imply, at positive integer n tending to infinity,

    f(n)=G(n)+epsilon_n,  |epsilon_n|<=C0*log(n)^2/n^2.       (1)

Indeed c1(w)=O(w)=O(log n), so the logarithm of the relative factor
1+c1(w)/n+O(log(n)^2/n^2) is c1(w)/n+O(log(n)^2/n^2).
Dividing gamma_n by 8*4^n*n! yields exactly U and B0 above.
In particular the n-dependent exponential in log(gamma_n) is
n*(1+2log(w)-log(16)-log(n)-2/w). Subtracting n*log(4)
and the Stirling term n*log(n)-n gives precisely U(n), while
log(4pi^2)-log(8)=log(pi^2/2). No factorial is absorbed into
the remainder.
The positive leading term and a relative factor tending to one justify
the real logarithm. Stirling here is the standard named asymptotic
for n!, used only at integer values; its remainder is not differentiated.
Nor is epsilon_n differentiated anywhere in this proof.

For w=W(2x/pi), implicit differentiation gives

    w'=w/[x*(1+w)],
    U'=2log(w)-log(64)-2log(x),
    U''=-2w/[x*(1+w)].                                      (2)

Also w tends to infinity and w=O(log x). Direct differentiation gives

    w''=-w^2*(w+2)/[x^2*(1+w)^3],
    w'''=w^3*(2w^2+8w+9)/[x^3*(1+w)^5],
    U'''=2w^2*(w+2)/[x^2*(1+w)^3].

Hence w^(j)=O(x^(-j)) for j=1,2,3, because the rational factors
are bounded for w>=1. The exact division

    c1(w)=-(w+55-139/(w+1)+88/(w+1)^2-20/(w+1)^3)/192

gives c1^(j)(w)=O(w^(1-j)) for j=0,1,2,3. Applying the chain
and product rules to the displayed B0 therefore gives

    B0''=O(x^-2),  B0'''=O(x^-3),  G'''=O(x^-2).             (3)

For example the c1(w)/x term contributes O(log(x)/x^3) to B0''
and O(log(x)/x^4) to B0'''; the 7w/4 and logarithmic terms satisfy
the remaining asserted bounds. These are derivatives of explicit smooth
functions only. Equations (2)-(3) imply uniformly for y in any fixed
compact subinterval of (0,infinity),

    k*G''(k*y) -> -2/y.                                    (4)

Uniformity follows from w(ky)>=w(k*y_min)->infinity and the uniform
O((ky)^-2) bound for B0''.

### Curvature and endpoint

Taylor's theorem for G on [k-1,k+1], using (3), and then (1), gives

    f(k+1)+f(k-1)-2f(k)
      =G''(k)+O(log(k)^2/k^2)=(-2+o(1))/k.

Thus k*tau->2, and positivity of the a_n already gives q>0;
eventually log(q)<0 as required.

Write h_s[G] for the same finite expression with f replaced by G
and tau replaced by -G(k+1)-G(k-1)+2G(k). At s=d=r-1,
all four arguments k-1,k,k+1,k+s lie between k/2 and 2k.
The exact error combination is

    h_s-h_s[G]=epsilon_(k+s)+(s^2-1)*epsilon_k
                 -s*(s+1)*epsilon_(k+1)/2
                 -s*(s-1)*epsilon_(k-1)/2.

For s>=2 its absolute coefficient sum is 2s^2. The single constant
in (1) applies to every sufficiently large integer; all four arguments
are comparable with k. Consequently (1) gives

    |h_s-h_s[G]|=O((1+s^2)*log(k)^2/k^2)=O(log(k)^2)=o(r).   (5)

This explicitly controls the amplification of the finite-value remainder.
The first and centered second differences of G satisfy

    G(k+1)-G(k)=G'(k)+G''(k)/2+O(k^-2),
    G(k+1)+G(k-1)-2G(k)=G''(k)+O(k^-2).

The linear and quadratic centering terms combine to -s^2 G''(k)/2.
Hence, again using (3),

    h_s[G]=G(k+s)-G(k)-sG'(k)-s^2*G''(k)/2+O(1).          (6)

Here the error is O((s+s^2)/k^2)=O(1), since s/k stays bounded.
The twice-integrated fundamental theorem of calculus rewrites (6) as

    h_s[G]=s^2*integral_0^1 (1-v)*(G''(k+s*v)-G''(k)) dv+O(1).

Now s/r->1, s/k->alpha, and s^2/(r*k)->alpha. Using the uniform
limit (4) and (5) in this fixed compact integral gives

    h_s/r -> alpha*integral_0^1 (1-v)*(2-2/(1+alpha*v)) dv
            =2*alpha^2*integral_0^1 v*(1-v)/(1+alpha*v) dv=C.

Integration of this elementary rational function yields the stated
logarithmic formula. On 0<v<1 the denominator is strictly between
1 and 1+alpha, and integral_0^1 v*(1-v)dv=1/6. This proves both
strict rational bounds on C without a decimal approximation.

### A load-bearing error entry

L is unit lower triangular, so the first row of L^(-1) is e_0^T.
D_0=1 and V_00=1. The (0,0) entry of F is therefore exactly

    F_00=E_00=exp(h_d)-1.

For any matrix, |e_0^T F e_0|<=||F||_2. The positive lower bound
C>1/3148800 and the established limit imply
h_d>=r/6297600 for every sufficiently large integer r. This proves
the asserted lower bound and divergence of the full error norm.
It also eventually makes the norm at least 1, contradicting its required
strict upper bound, independently of what other entries do.
No finite onset is supplied by the source's unquantified asymptotic
constants or by this proof. This does not assert that an effective
version is impossible.

### Critical-audit disposition

Step388 checked the full argument above against the primary theorem
interfaces. The remaining error after division by r is
O(log(k)^2/r)+O(1/r), which tends to zero on the stated ray. The
curvature limit is uniform on the fixed compact interval containing
1+s*v/k for all v in [0,1], so its integration is justified by a
uniform bound, not a differentiated coefficient error. The strict
rational lower bound on C, the eventual q range and the exact F_00
identity all survive the audit. No change to the conclusion or its
constant was needed; the displayed derivative and error identities
make the verification explicit. The result remains a sufficient-method
obstruction only. Actual minor signs, all-degree hyperbolicity and RH
are unresolved, and there is no effective finite threshold here.

## Mathlib

Not checked. Availability of a full matching theorem is unknown.
The proof uses a cited coefficient asymptotic and finite matrix algebra;
no Lean verification or full manuscript/certificate audit is claimed.
Reference: https://leanprover-community.github.io/mathlib4_docs/ .
