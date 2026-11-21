# Lemma 774: an actual odd coordinate obstructs q-Pascal accretivity

## Hypotheses

Use xi and the strictly positive moments of L018/L021. Set, for n>=0,

    gamma_n=n! M_(2n)/(2n)!,
    a_n=gamma_n/(8*4^n*n!)>0,  f(n)=log(a_n).

For integers r>=2 put k=d=r-1 and

    rho=a_(k+1)/a_k,
    q=a_(k-1)*a_(k+1)/a_k^2,  tau=-log(q),
    h_s=f(k+s)-f(k)-s*(f(k+1)-f(k))+tau*s*(s-1)/2.

The needed s lie in [-d,d]; all coefficient indices lie in [0,2k].
When 0<q<1, index the following real r-by-r matrices from zero:

    V_ij=q^(i*j),
    L_ij=[i choose j]_q for i>=j, and 0 otherwise,
    D_m=product_(h=0)^(m-1)(q^m-q^h),  D_0=1,
    E_ij=V_ij*(exp(h_(d-i-j))-1),
    F=|D|^(-1/2)*L^(-1)*E*L^(-T)*|D|^(-1/2),
    J=diag((-1)^m),  A_r=J*(J+F),  H_r=(A_r+A_r^T)/2.

Here |D| is diagonal with entries |D_m|. Let e_1=(0,1,0,...)
and Q_r=e_1^T H_r e_1. No real-rootedness, minor sign or
all-order Turan positivity is assumed.

## Conclusion

As r tends through integers, k*tau->2. In particular 0<q<1 eventually.
With b=2-2log(2)>0, one has the exact identity, whenever 0<q<1,

    Q_r=[2exp(h_(k-1))-exp(h_k)-q exp(h_(k-2))]/(1-q),

and the limit

    (1-q)*exp(-h_(k-1))*Q_r -> 2-exp(b)-exp(-b)<0.

Thus Q_r<0 for every sufficiently large r: the proposed H_r>0
condition fails, including at the exceptional center k=r-1.
No effective onset, negative actual Toeplitz minor, failure of its
desired sign, or disproof of RH is claimed. This is a local asymptotic
specialization of cited inputs, not a new general determinant theorem.
A separate critical audit on 2026-11-04 (step417) verified this
specialization and its determinant-transfer qualifications. It did not
audit the complete source manuscripts or establish any actual minor sign.

## Proof

### Imported results and finite-value estimates

Import Cormac O'Sullivan, *Zeros of Jensen polynomials and asymptotics
for the Riemann xi function*, arXiv:2007.13582v2 (9 December 2020),
[Theorem 1.4, (1.2), and (1.8)](https://arxiv.org/html/2007.13582v2#S1).
Its gamma_n equals the one above by L018/L021. Use K=2 and the
standard logarithmic Stirling expansion. Precisely the finite-value
consequence and explicit functions established in L765's proof are
used here, not its k=1024r endpoint limit:

    f(n)=G(n)+epsilon_n,  |epsilon_n|<=C log(n)^2/n^2,       (1)

for every sufficiently large integer n, with a single C, where, for
positive real x, w=W(2x/pi) is the positive Lambert branch and

    c1(w)=-(w^4+58w^3+29w^2-24w-16)/(192*(w+1)^3),
    U(x)=x*(2+2log(w)-log(64)-2log(x)-2/w),
    B(x)=log(pi^2/2)+7w/4+log(w/(w+1))/2-log(2pi*x)/2
            +(c1(w)-1/12)/x,
    G(x)=U(x)+B(x).

The factor n! in a_n=gamma_n/(8*4^n*n!) is retained in (1).
The source's positive leading term and relative remainder tending to
zero justify logarithmization. This is an integer-value estimate;
epsilon_n will never be differentiated. The cited saddle theorem is
not reproved. K=2 suffices below because adjacent defects amplify
the unknown error only by O(k), rather than O(k^2).

The explicit identities from L765's proof are

    w'=w/[x*(1+w)],
    U'=2log(w)-log(64)-2log(x),
    U''=-2w/[x*(1+w)],
    U'''=2w^2*(w+2)/[x^2*(1+w)^3].

For completeness the needed bounds on the explicit correction are
B'=O(x^-1), B''=O(x^-2), B'''=O(x^-3). Indeed w tends to infinity,
w=O(log x), and w^(j)=O(x^-j), j=1,2,3, by differentiating its
displayed implicit equation. The rational division

    c1(w)=-(w+55-139/(w+1)+88/(w+1)^2-20/(w+1)^3)/192

shows that the j-th x derivative of (c1(w)-1/12)/x is
O(log(x)/x^(j+1)) for j=1,2,3. The derivatives of 7w/4 and
-log(2pi*x)/2 have the asserted sizes. Finally
log(w/(w+1))=log(w)-log(w+1); its first three w derivatives
are bounded for w>=1, so its first three x derivatives are
O(x^-1), O(x^-2), O(x^-3), respectively. All constants are uniform
on [k-1,2k+1] once k is large. These are derivatives only of explicit
smooth functions. In particular G'''=O(x^-2).

### Curvature and adjacent defects

Taylor's theorem for G at k and (1) give

    tau=-(G(k+1)+G(k-1)-2G(k))+O(log(k)^2/k^2)
       =2w(k)/[k*(1+w(k))]+O(log(k)^2/k^2).                (2)

Here the Taylor remainder is O(k^-2) using G''' above, and
B''=O(k^-2). Consequently k*tau->2. Since q>0 from positivity
of a_n and q=exp(-tau), eventually 0<q<1. Also q->1.

For s=k or k-1 the exact adjacent-defect expression is

    Delta_s:=h_s-h_(s-1)
       =f(k+s)-f(k+s-1)-f(k+1)+f(k)+tau*(s-1).            (3)

Let tau_G=-(G(k+1)+G(k-1)-2G(k)) and define Delta_s[G]
by replacing f,tau in (3) with G,tau_G. Direct subtraction gives

    Delta_s-Delta_s[G]
       =epsilon_(k+s)-epsilon_(k+s-1)-epsilon_(k+1)+epsilon_k
          +(s-1)*(-epsilon_(k+1)-epsilon_(k-1)+2epsilon_k).

Every index here lies in [k-1,2k] for large k. Taking absolute
values in (1), before exponentiating, proves uniformly for these two s

    |Delta_s-Delta_s[G]|=O((1+s)*log(k)^2/k^2)
                            =O(log(k)^2/k)=o(1).          (4)

This is the required amplified finite-value error control; separate
O(log(k)^2) errors for the h_s themselves would not suffice.
More explicitly, the coefficients of epsilon_k, epsilon_(k+1), and
epsilon_(k-1) in this expression are 2s-1, -s, and -(s-1).
Together with the two endpoint coefficients their absolute sum is
at most 4s for s>=1. Index coincidences can only improve this triangle
bound. Since s<=k and all indices are comparable with k, the single
constant in (1) controls the whole expression as asserted.

By integration of G' over unit intervals, using B'=O(k^-1) and
U''=O(k^-1) on [k-1,2k+1],

    G(k+s)-G(k+s-1)-G(k+1)+G(k)
       =U'(2k)-U'(k)+O(k^-1)
       =2log(w(2k)/w(k))-2log(2)+O(k^-1).                (5)

The upper unit interval is contained in [2k-2,2k] for both s.
The lower one is [k,k+1], so the replacements of U' cost O(k^-1).
From w+log(w)=log(2x/pi), monotonicity gives

    0<w(2k)-w(k)<log(2).

Since w(k)->infinity, w(2k)/w(k)->1. Moreover (2) also holds
with tau_G, hence (s-1)*tau_G->2 for both s=k,k-1.
Combining (3)--(5), without differentiating an unknown error, yields

    Delta_k->b,  Delta_(k-1)->b,  b=2-2log(2)>0.           (6)

The last strict inequality follows from log(2)=integral_1^2 dx/x<1.
The surviving coefficient indices are precisely among
k-1,k,k+1,2k-2,2k-1,2k. No large-n asymptotic is applied at a
bounded index, although a_0 enters other entries of the full matrix.

### The exact signed coordinate

L is unit lower triangular and L_10=[1 choose 0]_q=1.
Consequently row1 of L^(-1) is (-1,1,0,...), independently of
later rows, and |D_1|=1-q. Therefore

    F_11=(E_00-2E_01+E_11)/(1-q)
        =[exp(h_k)-2exp(h_(k-1))+q exp(h_(k-2))+(1-q)]/(1-q).

As J_11=-1, A_(r,11)=1-F_11 and its symmetric part has the
same diagonal entry. The constant (1-q) thus cancels, proving the
exact asserted formula for Q_r. Equivalently,

    (1-q)*exp(-h_(k-1))*Q_r
       =2-exp(Delta_k)-q exp(-Delta_(k-1)).                (7)

Equations (2) and (6), and continuity of the exponential at finite
arguments, prove the claimed limit. Its sign is strictly negative:
exp(b)+exp(-b)-2=(exp(b/2)-exp(-b/2))^2>0. The normalizing
factor on the left of (7) is strictly positive for all sufficiently
large r. Thus Q_r<0 eventually. No estimate of an individual large
exponential, exchange of limits with a growing sum, or full matrix
norm is needed.

### Why this was a sufficient determinant interface

Import Wojciech Michałowski, *An explicit uniform cubic wedge for
consecutive Toeplitz minors of the Riemann xi-coefficients*,
arXiv:2607.16795v1 (18 July 2026),
[Lemma 4.1](https://arxiv.org/html/2607.16795v1#S4),
[(6)](https://arxiv.org/html/2607.16795v1#S5), and
[Section 6](https://arxiv.org/html/2607.16795v1#S6).
Only V=L D L^T for r>=2, 0<q<1 and the finite normalization are
used. Neither the far-tail theorem nor its small-r*tau bounds apply
here. The finite argument, corrected and audited in L765, remains
valid at k=d: a_0>0 ensures every logarithm is defined.

Explicitly let T_ij=a_(k+j-i), C_ij=a_(k+d-i-j),
R=diag(rho^(-i)), Z=diag(q^(i*(i+1)/2-d*i)), and
c_d=q^(d*(d-1)/2)>0. Direct substitution into the definition of h
and expansion of (d-i-j)*(d-i-j-1)/2 give

    C=a_k*rho^d*c_d * R*Z*(V+E)*Z*R
     =S_Q*(J+F)*S_Q^T,
    S_Q=sqrt(a_k*rho^d*c_d)*R*Z*L*|D|^(1/2).

All diagonal factors are positive and S_Q is invertible. In particular
the direction of R is checked by this equality, not assumed from the
source's prose. The whitening factors cancel exactly; none is commuted
past L. Reversal of the columns of T gives C. With nu=r*(r-1)/2,
the reversal determinant and det(J) both equal (-1)^nu. Hence

    det(T)=(-1)^nu det(C)
          =(det(S_Q))^2 det(J*(J+F))
          =(det(S_Q))^2 det(A_r).                         (8)

Import Teng Zhang, *Johnson's determinantal identity for contiguous
minors of Toeplitz matrices, with an accretive extension*,
arXiv:2601.18977v1 (26 January 2026),
[Section 4, Lemma 4.2](https://arxiv.org/html/2601.18977v1#S4):
a real square matrix whose symmetric part is positive definite has
strictly positive determinant. Thus a proved H_r>0 would imply
D_(r,r-1)=det(T)>0 by (8). There is no need to reprove the cited
determinant theorem, and no stronger inertia claim is used.

The computed negative Q_r invalidates that sufficient premise in the
given normalization. It leaves the sign of det(A_r), det(T), other
possible normalizations, other centers and all mixed-positivity/RH
questions unresolved. A failed accretivity condition is not a negative
minor. The numerical value of the onset is not provided by (1).

### Critical-audit disposition

Step417 checked the entire proof above, using the previously approved
primary-source assessment and the full finite-value argument in L765.
The coefficient convention agrees with L018/L021, including the n!
in the denominator of a_n. The positive leading term in the cited
K=2 expansion makes logarithmization legitimate. No unknown remainder
is differentiated, and no asymptotic is applied to a bounded index.

The rational expression for c1 and the displayed derivatives of w give
the stated B', B'', B''' bounds uniformly on [k-1,2k+1]. Taylor's
centered second-difference error for G is bounded by
sup_[k-1,k+1]|G'''|/3=O(k^-2). Thus tau_G has the curvature limit
used in (3)--(6). The additional finite-value curvature error is
O(log(k)^2/k^2); after multiplication by s-1 it still tends to zero.
The absolute coefficient bound 4s above verifies this directly for
both adjacent defects. The upper unit intervals are [2k-1,2k] and
[2k-2,2k-1]; replacing their U' integrals by U'(2k), and the lower
one by U'(k), costs O(k^-1). The Lambert equation bounds their
remaining log ratio. These checks establish (6) without an unproved
smooth extension of f or cancellation of uncontrolled h errors.

For the exact coordinate, E00 has constant contribution -1,
E01 has -1, and E11 has -q. Therefore the constant contribution
to E00-2E01+E11 is 1-q. It cancels against the identity term in
1-F11, rather than contributing an additional sign or constant to
(7). Both factors 1-q and exp(-h_(k-1)) are strictly positive
eventually. The strictly negative limit in (7) hence proves the
eventual negative coordinate; the size of h_(k-1) itself is immaterial.

Finally, the exponent split in the full congruence is exact:

    (d-i-j)*(d-i-j-1)/2
      =d*(d-1)/2 + i*(i+1)/2-d*i + j*(j+1)/2-d*j + i*j.

This verifies Z, while rho^(d-i-j) verifies R=diag(rho^(-i)).
Substituting the definition of F cancels the whitening factors in
their original order and gives C=S_Q*(J+F)*S_Q^T. Every needed
coefficient, including a_0, is positive. Also D_m has m negative
factors when 0<q<1, so its sign is (-1)^m and every pivot is nonzero.
The column reversal and det(J) each have sign (-1)^nu. Their product
is +1, leaving the strictly positive square factor in (8). Zhang's
real strict-accretivity theorem therefore has the claimed implication
if H_r>0 were available. The negative coordinate rules out that
premise, not its determinant conclusion. No conclusion, constant,
effective onset or mathematical dependency was changed by the audit.

## Mathlib

Not checked: availability of a full matching theorem is unknown.
The inputs are precisely cited coefficient asymptotics, a finite
q-Pascal factorization and a real accretive-determinant implication.
No Lean verification or full source-manuscript/certificate audit is
claimed. Reference: https://leanprover-community.github.io/mathlib4_docs/ .
