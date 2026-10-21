# L119 — First-order reduction of the generator-displacement placement error

## Hypotheses

Use L111's exact Delta_V=R_bulk-R_bulk,moved for SU(2), both actual
L010 probes i=3,6, the straight lower-rooted direction-1 forest, the
all-face relative fixed-link box (-4,4)^4, admitted even N, a=8/N,
and tau=1/16. Take the bare small-coupling coefficient at fixed mesh
before refinement. Coordinates and norms are ordinary stored ones.
Keep all interior levels, transverse end rows, both generator
orientations and the complete exterior heat sum. In particular retain

    Z_(kl;st)=F_l(s)^T P F_k(t)

with its exact finite middle projection and the original two levels.
Import L111's zero extension J, stencils T_r,C_r, displacement b_(r,t)
and energy convolution E_j. Its kernel convention here is
E_j(x,y)=e_j(x-y). The coefficients use lower-vertex integer indices.

Write A_r=D T_r and fix the following finite-shift convention:

    (A_r v)(x)=sum_h A_r(h)v(x+h),
    (C_r w)(x)=sum_q C_r(q)w(x+q).                     (1)

Thus A_r(h) is a plaquette-column matrix and C_r(q) a plaquette-row
matrix; all shifts, signs and component selectors are retained.
Let xi_t=-4+at and xi_x=(-4,-4,-4)+ax. If b_(r,t)(x) is the sample
of u_(a,rho(r)), use the same signed-stencil convention for rho(r)
as L111. L028 proves u_a -> u in every fixed C^r norm with O(a^2)
error, with uniform smooth bounds and a common compact interior support.
These are global smooth displacement extensions, not extensions of
forest fields across their upper pin.

## Conclusion

For j in Z and m=2,3,4 define the real matrix kernel

    B_(r,j,m)(d)=sum_(h,q) (d_m+h_m)
                     A_r(h) C_r(q) e_j(d+h+q),
    v_(r,t,m)(x)=partial_m u_(rho(r))(xi_t,xi_x).        (2)

Only finite compressions of these kernels are needed below. Define

    V_N=sum_(k,l,s,t,r,m)c_(i;kl,a) min(s,t)
          Tr[J^* M_(v_(r,t,m)) B_(r,t-s,m) J Z_(kl;st)]. (3)

Then, for both probes,

    Delta_V=V_N+o(N^3),       a^3(Delta_V-V_N) -> 0.     (4)

This is a first-order asymptotic reduction, not a limit theorem for
V_N. Its kernels obey the stronger tail-enabling statement

    sum_j ||B_(r,j,m)||_(ell^2,F) < infinity.           (5)

More explicitly, let V_N^(J0,R) replace each kernel in (3) by
1_(|j|<=J0) 1_(|d|<=R) B_(r,j,m)(d), and put

    Theta(J0,R)=sum_(r,m) [sum_(|j|>J0)||B_(r,j,m)||_2
                    +sum_(|j|<=J0)||1_(|d|>R)B_(r,j,m)||_2].

Uniformly over sufficiently fine admitted meshes,

    a^3 |V_N-V_N^(J0,R)| <= C_i Theta(J0,R),
    lim_(J0->infinity) lim_(R->infinity) Theta(J0,R)=0. (6)

Thus finite spatial range and finitely many axial offsets may be
imposed with an arbitrarily small cubic-scaled error before taking a
mesh limit. They do not replace s and t by equal levels. The finite P,
both exterior coefficients and min(s,t) still occur in (3) and its
truncations. Neither the existence nor the value of lim a^3 V_N is
asserted. L110's exterior-circulation error and L113/L115's other
cubic placement errors remain, as do evaluation of the other
functionals, complete compensation, finer scales and the interacting
continuum and mass-gap requirements.

## Proof

### 1. Expand the exact commutator, with its stencils unchanged

By L111(4)--(5), Delta_V equals

    a^-1 sum_(k,l,s,t)c_(i;kl,a) min(s,t) Tr[X_(t,t-s)Z_(kl;st)],
    X_(t,j)=J^* sum_r A_r(M_b C_r E_j-C_r E_j M_b)J.    (7)

The two scalar multipliers in each summand act on their respective
vertex and plaquette arrays at the same integer indices. For infinite
output x and input y, that summand has the exact kernel

    sum_(h,q) A_r(h) C_r(q) e_j(x+h+q-y)
                      [b_(r,t)(x+h)-b_(r,t)(y)].       (8)

L111's compact-support argument already justifies (7) on the finite
relative spaces. In particular the moved term's noncompact output
has not been discarded. Formula (8) includes the coefficient shift
through C_r as well as the one through E_j. Replacing the bracket by
a sum_m v_(r,t,m)(x)(x_m+h_m-y_m) gives precisely a times (2),
with the multiplier on its output. No multiplier crosses P or F.

### 2. Control the Taylor remainder in the joint quadratic norm

Set d=x-y. Taylor's integral formula along the segment from xi_y
to xi_(x+h), at fixed axial coordinate xi_t, gives

    b_(r,t)(x+h)-b_(r,t)(y)
      =a (d+h) dot integral_0^1
          grad_T u_(a,rho(r))(xi_t,xi_y+theta a(d+h)) dtheta.

Let delta(a)=max_r ||grad_T(u_(a,rho(r))-u_(rho(r)))||_infinity.
L028 gives delta(a)=O(a^2). Uniform C^2 bounds and bounded first
derivatives imply that the error after subtracting
a grad_T u_(rho(r))(xi_t,xi_x) dot (d+h) is at most

    a |d+h| omega_a(d,h),
    omega_a(d,h)=min(C, delta(a)+C a(|d|+|h|)),         (9)

after enlarging a fixed C. This holds at every x,t, including the
zero displacement collars and segments leaving the box. The segment
uses only the globally smooth displacement, never a pinned field.
For each fixed d,h, omega_a(d,h) -> 0, and omega_a is uniformly bounded.

L110 and L111 supply respectively

    Q_j=|| |z| e_j(z)||_2 <= C(1+|j|)^(-3/2),
    W_j=||e_j||_2 <= C(1+|j|)^(-5/2).                 (10)

The norm is the ell^2 norm of Frobenius matrix entries. For every
fixed h,q, substituting z=d+h+q gives

    || |d+h| e_j(d+h+q)||_2 <= Q_j+|q|W_j.            (11)

It follows by the triangle inequality and the finite stencil sums
that ||B_(r,j,m)||_2 <= C_r(Q_j+W_j). This proves (5).

Define eta_j(a) to be the sum over r,h,q of

    ||A_r(h)|| ||C_r(q)||
       [sum_d |d+h|^2 omega_a(d,h)^2
                             ||e_j(d+h+q)||_F^2]^(1/2).

For each j, dominated convergence for the counting measure, using
(11), proves eta_j(a) -> 0. Moreover eta_j(a)<=C(Q_j+W_j).
Dominated convergence for the axial counting measure therefore yields

    eta(a):=sum_j eta_j(a) -> 0.                      (12)

These two applications are to summable positive bounds. They require
neither second quadratic moments nor first absolute moments of a
separate projection/path kernel. This is the standard dominated
convergence theorem applied after Fourier Plancherel has supplied
the joint energy moments in L110/L111; no new source input is needed.

Each finite plaquette array has at most C N^3 rows. By (8)--(9), the
ell^2 norm of every complete error row is at most a eta_j(a).
Restriction of input rows only decreases this norm. Consequently

    ||X_(t,j)-a sum_(r,m)J^*M_(v_(r,t,m))B_(r,j,m)J||_HS
                         <= C a N^(3/2) eta_j(a),     (13)

uniformly in t. This bound includes every finite output row; it does
not assume that the original commutator has compact output.

### 3. Retain the full weighted trace and heat sum

Import L111(13), in its exact finite ordering:

    ||Z_(kl;st)||_HS <= C a^2 p(k)p(l) N^(3/2),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l) <= C_i.              (14)

Trace Cauchy--Schwarz, (7), (13) and (14) give

    |Delta_V-V_N|
      <= C_i a^2 N^3 sum_(s,t) min(s,t) eta_(t-s)(a)
      <= C_i a^2 N^5 eta(a)=64 C_i N^3 eta(a).         (15)

Indeed min(s,t)<=N, there are fewer than N values of t, and each
s sum is at most the full axial sum eta(a). This proves (4) since
eta(a)->0 and aN=8. Both exterior coefficient levels, all heat
labels and the original prefactor are preserved in this calculation.
The complete other/other group's outside factor 3 is not applied.

### 4. Remove only controlled kernel tails

For any real matrix kernel K and bounded scalar v, finite compression
on C N^3 rows obeys

    ||J^* M_v K J||_HS <= C ||v||_infinity N^(3/2)||K||_2. (16)

This is a rowwise squared-sum estimate. No bounded convolution
operator on the full infinite space is needed to use (16).
The v in (2) are uniformly bounded. Apply (16) to each omitted
kernel in V_N-V_N^(J0,R), then (14) and the same level count as in
(15). There is no outside a^-1 in V_N; the resulting bound is
C_i a^2 N^5 Theta(J0,R). Multiplication by a^3 changes its constant
by the fixed factor (aN)^5=8^5. This proves the uniform inequality
in (6). For fixed J0, each of its finitely many spatial ell^2 tails
tends to zero as R grows. The remaining axial tail tends to zero
by (5). This proves its stated ordered limit.

### 5. Scope and subsequent limit obligation

The new information beyond L111's O(N^3) bound is a first-derivative
formula with an o(N^3) remainder and a uniform truncation procedure.
The finite-range traces still contain the actual finite projection.
Their continuum limit requires an interior projection comparison,
fixed-mode exterior coefficient convergence with the physical prefix
and upper pin retained, and a justified level/spatial Riemann sum.
Those steps have not been proved here. Uniform bounds alone are
not a proof of convergence or a coefficient evaluation.

This is one RESEARCH / REPRODUCTION specialization under the unchanged
complete other/other EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The exact generator, contraction and moments are imported; the
specialization is necessary because their previous cubic bound did
not identify its first-order insertion. It is local standard-method
progress, without a novelty claim beyond checked sources. No
numerical comparison with D_i is made.

## Mathlib

Full matching finite-trace first-order reduction: **not checked**.
Supporting Taylor integral remainder, dominated convergence for
counting measure, Hilbert--Schmidt trace inequalities and Fourier
Plancherel coverage: **not checked**. Unknown availability is not
absence. No general flow/Ward result assigns this isolated coefficient.
