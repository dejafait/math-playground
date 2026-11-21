# Corollary 651a: the fixed-profile scalar bound reaches the full joint projection

## Hypotheses

Fix one actual L703/L708 profile before n varies, with all cutoffs and
Picard parameters as in L726. Use its complete finite family

    x=-5/4, R=11/8, U=121/64, eta=1/100,
    n=12q+3, q>=1, h=27/(10n), M=4q+1=n/3,
    Z_n={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q}.

The e_m are real, fixed across n, and |e_m|<=1/8. All original
residues are one. Retain every grid point t_j=j/n, the inverse
denominator angle, normalized circle means, and

    B_u(z)=product_(j<n) R*(z-t_j*u)/(U-t_j*z/u),
    b_u(zeta)=B_u(R*zeta), W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1)sum_(a in Z_n)W_a(u)*(a/R)^k,
    E_0=mean_u |c_0(u)|^2,
    D=mean_u sum_(a in Z_n)|W_a(u)|^2/(U-|a|^2).

Let F_u and D_(u,M)=span{P_+(b_u*zeta^(-k-1)):0<=k<M}
be L651's full analytic component and full joint range, and set

    J_n=mean_u ||Proj_(D_(u,M))F_u||_2^2,
    S_n=mean_u sum_(0<=k<M)|c_k(u)|^2.

Use L726 (2), with its audited fixed-profile, possibly ineffective
onset. No arbitrary displacement family or profile-uniform onset
is assumed.

## Conclusion

For every allowed n, D_single,n=D, S_n>=E_0 and J_n>=E_0.
Consequently, for every sufficiently large allowed n for this fixed
profile,

    J_n >= E_0 >= n^2*exp(-n/16)*D.                         (1)

In particular the approved bound J_n>=c*exp(-n/16)*D holds with
c=1 and the same profile-dependent onset as L726 (2). This is a
local specialization and transfer of an established scalar bound,
not a new general projection theorem or a uniform-family theorem.
General support, detector upper bounds, Xi realization and all-degree
mixed signs remain unresolved. No certified originality is claimed.

## Proof

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-03-fixed-profile-joint-projection-audit.md`
covers precisely this application. L651 Section 6 records the separate
conceptual audit of the full Gram transfer and the inherited component
formulas. L726 (2) is used as an already audited premise; neither its
scalar proof nor its paid-arc argument is repeated.

First check admissibility. Consecutive nonanchor ordinates differ by
at least 3h/4, and each is at distance at least 3h/8 from zero.
The largest absolute ordinate is at most h*(2q-3/8)<9/20. Hence
there are exactly 4q+1=M distinct poles, with the anchor retained,
and

    |a|^2 < (5/4)^2+(9/20)^2=353/200
           <(273/200)^2=(R-eta)^2.

All poles lie on Re(a)=x, have unit residues, and M=n/3 with n>=15.
These are precisely L651's geometric and census hypotheses.

The j=0 factor of B_u(x)/B_u(a) is x/a. For j>=1 its factor is

    [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)].

This is exactly L726's W_a, including the inverse rotation. The
boundary denominators do not vanish: |a|>=5/4>t_j and
U-t_j*|a|>0. Thus all finite sums are continuous in u. The original
residues r_a are one, so r_a^2=1 in L651's diagonal; its normalized
angular mean is exactly D. Its moment vector has exactly the c_k
above. Since k=0 is present, S_n>=E_0 immediately.

For the projection itself, retain the full joint range. Its member
d_0=P_+(b_u/zeta) equals b_u/zeta because the zero grid point gives
b_u(0)=0. On the spatial circle |b_u|=1, so ||d_0||_2=1.
The entire negative component e_0=P_-(b_u/zeta) is zero; L651's
audited response identity therefore gives

    <F_u,d_0>=-c_0(u).

Equivalently this follows directly from its full component identity:
<B_u(x)L(R*zeta),d_0>=0 by Fourier orthogonality, whereas
<b_u q_u,b_u/zeta>=<q_u,zeta^(-1)>=c_0(u).
This verifies sign and normalization without discarding a nonzero
analytic correction. The inner product is linear in its first
argument throughout.

Let p_u=Proj_(D_(u,M))F_u. As d_0 belongs to this entire range,
orthogonality gives <p_u,d_0>=<F_u,d_0>. Cauchy--Schwarz with
||d_0||=1 yields ||p_u||^2>=|c_0(u)|^2 at each angle. Integration
gives J_n>=E_0. This is a lower bound on the full projection, not
an equality or a replacement of the range by one grid coordinate.
Its other directions and their cross terms remain present.

Applying L726 (2) proves (1), at exactly its fixed-profile onset.
The paid angular arc in L726 (3) is unnecessary for this implication.
As a consistency check on the full-vector route, S_n>=E_0 and L651
(4) imply tau_n/sqrt(S_n)->0 after this onset; then L651 (3) also
gives the requested rate. The exact d_0 argument avoids that loss.
Neither argument exchanges a maximum with a mean or uses positivity
of a Gram matrix as the missing response lower bound.

The standard imported inputs are normalized Hardy orthogonality in
Baratchart--Chevillard--Qian, *Minimax principle and lower bounds in
H2-rational approximation*, J. Approx. Theory 206 (2016), 17--47,
[preprint v2, Section 2 (1)--(4), pp.2--3](https://arxiv.org/pdf/1501.01161v2),
and finite Hilbert-space projection/Bessel in A. Levitt, *Analyse de
Fourier et applications*, 2021--2022 course,
[Theorem 1.3 and Exercise 1.2, p.6](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
Their source assessment is reused; only the prescribed component,
normalizations and fixed-profile applicability are specialized here.
L651's unchanged exact checker was replayed in its audit, including
the unit norm and constant response. No finite experiment supplies
the asymptotic premise, which is L726 (2).

## Mathlib

Full matching coverage for this fixed-profile joint-projection
specialization has not been checked. The cited Hilbert-space and
Fourier results support the argument; they do not supply L726's
product-specific scalar bound or an Xi realization. This informal
application audit is not a formal verification or certified novelty.
