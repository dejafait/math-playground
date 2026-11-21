# Corollary 711a: direct spatial Jensen payment on three fixed arcs

## Hypotheses

Fix one actual L703 profile e, with its original cutoffs and width
chosen before n varies. Use L666's complete family and rational
angular continuation, with

    n=12q+3, q>=1, M=n/3, d=5/4, x=-d, R=11/8,
    U=121/64, A=27/10, Y=9/20, t_j=j/n,
    a(y)=-d+i*y, y_m=A*(m+1/2+e_m)/n,
    Z_n={x} union {a(y_m): -2q<=m<2q},
    W_a(u)=(x/a)*product_(j=1)^(n-1)
        [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    G_n(u,z)=R^(-1)*sum_(a in Z_n) W_a(u)
                                     *sum_(k=0)^(M-1)(a*z/R)^k.

All original masses are one, W_x=1, and the inverse angular variable,
j=0 factor x/a, both endpoints, signed interior and every one of the
M spatial moments are retained. The profile does not depend on n,u,z,
and no reflection of it is assumed. On |u|=1/2 define

    S_n(u)=max_(|z|<=1)|G_n(u,z)|,
    m_n(u)=mean_(|z|=1) log|G_n(u,z)|,
    Delta_n(u)=log S_n(u)-m_n(u),
    J_sp(n)=integral_(|u|=1/2) Delta_n(u) dmu(u).

Here mu and the spatial mean are normalized full-circle measures;
restriction to an arc does not renormalize mu. L706 supplies nonzero
spatial slices, finite-n logarithmic integrability and
0<=Delta_n<=(M-1)*log 2. Maximum modulus identifies the disk and
circle definitions of S_n. Use the audited L708 unit-disk limit and
the audited L709/L711 endpoint normalization and unit-maximum rate.

## Conclusion

There exist three pairwise disjoint fixed closed arcs I_-, I_+, I_i
of |u|=1/2, centered at -1/2, 1/2 and i/2 respectively, all with
positive measure, whose union E has measure sigma in (0,1), such that

    sup_(u in I_-) Delta_n(u)=O(1),                         (1)
    Delta_n(u)=log 11+O(exp(-c*n)), uniformly on I_+,        (2)
    sup_(u in I_i) Delta_n(u)/n -> 0.                       (3)

Here c>0 and all constants, arcs and onsets may depend on the fixed
profile; limits run along the entire sequence n=12q+3. Consequently

    integral_E Delta_n dmu=o(n),
    0<=limsup J_sp(n)/n <= (1-sigma)*log(2)/3.              (4)

For this fixed E, J_sp=o(n) is equivalent to the still-unproved
condition integral_(E^c) Delta_n dmu=o(n). The upper coefficient in
(4) is strictly positive. No positive lower limit for J_sp/n, global
sublinear defect, amplitude lower bound, full charge compensation,
H/support estimate, Xi realization or RH candidate is established.

This is a direct specialization of the assessed boundary-Poisson
inequality using existing signed estimates. The new local payment is
(3); (1) is retained and (2) is a consequence of an existing uniform
limit. No mathematical originality beyond the checked sources is
claimed. This corollary has not received a separate critical audit.

## Proof

### 1. Source reuse and the normalized boundary loss

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-fixed-profile-spatial-jensen-defect.md`.
It covers this exact normalized defect and the needed boundary-zero
cases. Import R. B. Ash and W. P. Novinger, *Complex Variables*,
[Theorem 4.8.3 and Lemma 4.8.4, printed pp.33-36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94),
with the Poisson-kernel normalization in Corollary 4.7.4, printed p.27.
The prior source assessment inspected the boundary-factor proof.
For a nonzero function analytic near the closed disk, evaluated at
an interior nonzero value, it gives the boundary Poisson--Jensen
inequality. Boundary zeros are permitted. We do not reprove the
general theorem or invoke fixed-degree continuity of Mahler measure.

Let P be a nonzero polynomial, S=max_(|z|=1)|P(z)|, and assume
P(1/2)!=0. Its boundary logarithm is integrable, including the
finitely many possible boundary zeros. Put

    v(z)=log S-log|P(z)| >= 0,       |z|=1.

The value +infinity at a boundary zero does not affect integrability.
The Poisson kernel at 1/2 is

    p(z)=(1-1/4)/|z-1/2|^2,
    mean p=1,                     min p=1/3.

The imported inequality and these two facts give

    (1/3)*mean v <= mean(p*v)
                  =log S-mean(p*log|P|)
                  <=log S-log|P(1/2)|.

Thus the precise specialization is

    0<=log S-mean log|P|<=3*log(S/|P(1/2)|).              (5)

No roots are discarded, no particular degree is assumed, and an
angular or spatial exceptional set is not removed from this bound.

### 2. Uniform sublinear defect on the imaginary arc

Write a_-=-d-iY and W_-(u)=W_n(u,-Y), using the virtual endpoint
only as normalization. On a fixed arc about i/2, L709 gives W_-!=0
and the uniform limit

    G_n(u,1/2)/W_-(u) -> -K(u),
    K(u)=1/[(R-a_-/2)*(1-exp(-A*D_-(u)))],
    Re D_-(u)>1/25.                                     (6)

K is continuous and nonzero. On the intersection with L711's fixed
arc, the latter gives

    epsilon_n:=sup_u |n^(-1)*log(S_n(u)/|W_-(u)|)| -> 0.  (7)

Choose a smaller positive-measure closed arc I_i about i/2 inside
this intersection. Compactness, (6) and its uniform convergence give
one constant 0<c_0<=1 and one onset N such that

    |G_n(u,1/2)|/|W_-(u)|>=c_0,     u in I_i, n>=N.       (8)

In particular (5) is applicable to every such complete slice. Using
(7)--(8), with precisely the same scalar normalization, yields

    0<=Delta_n(u)
       <=3*[log(S_n(u)/|W_-(u)|)
                         -log|G_n(u,1/2)/W_-(u)|]
       <=3*n*epsilon_n+3*log(1/c_0).                     (9)

This proves (3) uniformly along the entire allowed sequence. The
angular arc and c_0 were fixed before n and before any tolerance in
(7). An arc shrinking with the requested rate would not suffice.
Only the full unit maximum is used; there is no assumption about
growth on a larger spatial disk.

### 3. The two real arcs and the complement

Use L706's fixed negative-real arc for (1), shrinking it if necessary.
For the positive-real arc, L708 gives a fixed complex neighborhood
of 1/2 and constants c,C>0 such that

    sup_(u, |z|<=1)|G_n(u,z)-H(z)|<=C*exp(-c*n),
    H(z)=1/(R+d*z).                                     (10)

On the closed unit disk, |H|>=1/(R+d)>0. The relative error in
(10) therefore tends uniformly to zero. At one common onset it is
at most 1/2, and the elementary inequality
|log|1+w||<=2|w| for |w|<=1/2 gives

    sup_(u, |z|<=1)|log|G_n(u,z)|-log|H(z)||
                                             <=C'*exp(-c*n). (11)

Both the boundary log mean and the boundary log maximum have the
same error bound. The function H is analytic and zero-free on
|z|<R/d=11/10, so the harmonic mean-value property gives
mean_(|z|=1)log|H(z)|=log|H(0)|=-log R. Also

    max_(|z|=1)|H(z)|=1/(R-d).

Its defect is log(R/(R-d))=log 11, proving (2) on a fixed closed
positive-measure arc I_+ about 1/2. This uses a uniform lower bound
in (11), not a presumed continuity of logarithms through zeros.

Shrink I_-, I_+, I_i so they are pairwise disjoint and their union
has measure strictly below one. Shrinking preserves every uniform
bound and their positive measures. Integrating (1)--(3) on E gives
o(n). On E^c retain the audited actual-degree bound from L706:

    0<=integral_(E^c) Delta_n dmu
       <=(1-sigma)*(n/3-1)*log 2.                        (12)

Equations (4) and the stated equivalence follow. In particular neither
(9) nor (12) supplies a complementary sublinear estimate. There is
no reflection argument for the remaining angular points.

### 4. Scope of the result

The earlier two-arc outer-growth estimate C708a and the growth stop
L712 concern a different observable. They are comparisons, not inputs
to (5)--(12). Linear growth outside the unit spatial disk is compatible
with the sublinear normalized unit-circle loss in (3). Reversing a
growth-to-defect upper bound would be invalid. The present corollary
pays a new part of the exact target while leaving a positive-measure
complement and all independent global inputs unresolved.

No numerical sample or mathematical script is used. The proof checks
the interior value, boundary zeros, actual degree, common fixed arc,
normalized measure and uniform full-sequence limits explicitly.

## Mathlib

Full matching coverage for this family-specific asymptotic has not
been checked. The supporting
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
contains the names recorded by the reused assessment, including
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
and `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`. They support
polynomial logarithmic means and degree bounds, not (3) or a global
J_sp=o(n) theorem. No new formalization or coverage audit is claimed.
