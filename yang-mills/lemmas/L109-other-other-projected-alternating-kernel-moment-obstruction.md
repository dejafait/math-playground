# L109 — A first absolute moment fails for the full projected alternating map

## Hypotheses

Use the transverse three-dimensional lattice and the original two-edge
paths of L088(11)--(13). For a constant normalized real exterior vector
v=(v_2,v_3,v_4), let Omega_v be that lemma's frozen alternating operator
divided by a: the stored exterior is av. Include all three transverse
planes and both original paths. In component-center Fourier phases put

    d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2), w_j=v_j eta_j,
    lambda=sum_j d_j^2, P=d d^T/lambda, Q=I-P,
    alpha_v=P Omega_v Q,                 theta in [-pi,pi]^3, lambda>0.

Set alpha_v(0)=0. This is the constant-coefficient bulk version of the
complete normalized gh alternating factor A_k/a in L099(2). This
definition does not replace that lemma's actual pinned trace, its two
coefficient levels, min(s,t), full generator or exterior heat sum.

Let h_(v,j)(theta)=(alpha_v(theta))_jj. The same-component entry has no
component-center phase offset; it is a periodic scalar symbol. Define
its infinite-lattice kernel by

    k_(v,j)(z)=(2pi)^(-3) integral_[-pi,pi]^3
                                h_(v,j)(theta) exp(i z dot theta) dtheta,
    z in Z^3.

All norms and distances here are dimensionless. A physical coefficient
difference over a displacement z is bounded by a Lip(b)|z| for a
smooth scalar coefficient b, with Euclidean |z|.

## Conclusion

The exact full projected symbol is

    alpha_v=-2i d w^T Q,
    h_(v,j)=-2i[v_j sin(theta_j)
                    -(d_j^2/lambda) sum_l v_l sin(theta_l)].       (1)

For every nonzero v and every j with v_j nonzero,

    sum_(z in Z^3) |z| |k_(v,j)(z)| = infinity.                    (2)

There is also a finite periodic diagnostic with no unproved rate.
For even L, sample h on the L^3 equally spaced torus frequencies and
let k_(v,j,L) be their inverse discrete Fourier transform. With
Z_L={-L/2,...,L/2-1}^3 as the displacement representatives,

    lim_(L->infinity, L even) sum_(z in Z_L)
                                  |z| |k_(v,j,L)(z)| = infinity. (3)

Thus the parity-transfer shortcut requiring a uniform first absolute
moment for each complete projected alternating kernel separately
fails, even after retaining both paths and all transverse planes.
This is a necessary condition of that particular absolute-kernel
estimate, not a necessary condition for cubic control of R_H,tr.
It supplies neither a divergence rate for (3) nor a lower bound on
either actual probe trace. A joint closed-trace kernel estimate may
still succeed. In particular no a^3 limit, failure of that limit,
compensation with L084, or physical-boundary estimate is proved.

## Proof

### 1. Compress the full frozen alternating map exactly

Import L088(11)--(13), whose path calculation retains the imaginary
parts of both original two-edge paths. For each mu<nu put

    z_(mu nu)=-d_nu e_mu^T+d_mu e_nu^T,
    r_(mu nu)=-w_nu e_mu^T+w_mu e_nu^T.

Its normalized plane symbol is 2i(r^T z+z^T r). Summing all planes
gives, by checking diagonal and off-diagonal component entries,

    sum_(mu<nu) r_(mu nu)^T z_(mu nu)=(w dot d)I-d w^T,
    Omega_v=2i[2(w dot d)I-d w^T-w d^T].                         (4)

For example the j,j entry of the first sum is sum_(l!=j)w_l d_l;
its j,k entry for j!=k is -d_j w_k. This checks every entry and
fixes the transpose order. Since P Q=0, P d=d and d^T Q=0,
left/right multiplication of (4) proves alpha_v=-2i d w^T Q.
Taking its j,j entry and using d_l w_l=v_l sin(theta_l) gives (1).
This calculation uses the entire gh block, not an individual
transport filter or the generator's symmetric part.

The bound ||alpha_v||<=2|d||v| shows continuity at zero after the
specified zero extension. Formula (1), with d_j^2=2-2cos(theta_j),
also shows that h_(v,j) is continuous and periodic on the full torus.
The apparent denominator has no other zero there.

### 2. Exhibit the obstruction to differentiability

On every coordinate axis, h_(v,j) is identically zero. If only
theta_j varies, the two terms of (1) cancel; if another coordinate
alone varies, both terms vanish. Thus all coordinate directional
derivatives of h_(v,j) at zero exist and equal zero.

Choose k!=j and sigma in {1,-1}. Along the exact line
theta_j=t, theta_k=sigma t, with the third coordinate zero,
d_j^2=d_k^2 and (1) gives

    h_(v,j)(t e_j+sigma t e_k)
                       =-i sin(t)(v_j-sigma v_k).                (5)

If v_j!=0, at least one choice of sigma makes v_j-sigma v_k nonzero:
otherwise v_j=v_k=-v_k, forcing v_j=0. For that choice the directional
derivative in (5) is nonzero. A Frechet derivative at zero would be
linear and would vanish on each coordinate vector, hence on their
sum or difference. This contradicts (5). Therefore h_(v,j) is not
differentiable at zero. The argument applies to every nonzero v by
choosing a nonzero component; no special direction of an actual
heat column is assumed.

### 3. A finite first absolute Fourier moment would imply C^1

Suppose the sum in (2) were finite. Since |z|>=1 for z!=0 and
k_(v,j)(0) is finite, both sum_z |k_(v,j)(z)| and
sum_z |z_l k_(v,j)(z)| are finite for every coordinate l.
The Fourier series

    H(theta)=sum_z k_(v,j)(z) exp(-i z dot theta)

and each of its three formally differentiated series consequently
converge uniformly, by their summable absolute bounds. To justify
differentiation directly, integrate the uniformly convergent l-th
derivative series along a coordinate segment. Termwise integration
is valid and gives H(theta+t e_l)-H(theta), since the undifferentiated
series converges uniformly as well. Hence H has continuous partial
derivatives and is C^1.

Uniform convergence gives H the same Fourier coefficients as the
continuous periodic function h_(v,j). For completeness, uniqueness
here needs no pointwise Fourier convergence assertion: convolving
their difference with the product of the three Fejer kernels gives
zero because every Fourier coefficient is zero. These nonnegative
kernels have integral one and their mass outside any fixed
neighborhood of zero tends to zero; uniform continuity then makes
these convolutions converge uniformly to the continuous difference.
Thus H=h_(v,j). This would make h_(v,j) C^1, contradicting section 2,
and proves (2). This elementary Fourier argument is written out to
justify the particular moment test; it is not claimed as a new
general Fourier theorem.

### 4. Verify the finite periodic obstruction without a tail assumption

Let theta_m=2pi m/L, m in {0,...,L-1}^3, interpreted periodically,
and set

    k_(v,j,L)(z)=L^(-3) sum_m h_(v,j)(theta_m)
                                            exp(i z dot theta_m).

For each fixed integer z this Riemann sum converges to k_(v,j)(z),
because its periodic integrand is continuous, including at zero.
No absolute Fourier summability is needed for this assertion.

Given B>0, (2) supplies a finite set F of displacements with
sum_(z in F)|z||k_(v,j)(z)|>2B. For all sufficiently large even L,
F is contained in Z_L and coefficientwise convergence on this finite
set makes the corresponding discrete sum greater than B. The sum
over all Z_L is at least that sum over F. Since B is arbitrary, this
proves (3), not merely unboundedness on a subsequence.

### 5. State precisely which estimate fails

For a scalar lattice multiplier b and a translation-invariant scalar
kernel k, the commutator entries are

    [M_b,K]_(x,y)=(b(ax)-b(ay)) k(x-y).

Bounding every coefficient difference by a Lip(b)|x-y| and then
applying absolute row/column sums would give the sufficient estimate

    ||[M_b,K]|| <= a Lip(b) sum_z |z||k(z)|.                     (6)

The diagonal kernel in (2) already makes the proposed constant in
(6) infinite. Equation (3) additionally rules out a uniform version
of this absolute moment constant on the explicitly defined periodic
bulk diagnostics. Component matrix norms cannot repair it, since
each dominates the absolute value of its diagonal entry.

This does not assert that the commutator norm itself has no O(a)
bound: an estimate using signed or quadratic sums is not (6).
Nor does it transfer the periodic diagnostic to the pinned box.
The proposed proof strategy needed this infinite bulk moment before
separately estimating the physical-boundary correction. That bulk
premise already fails, so that particular strategy is stopped
without making any assertion about the unestimated boundary term.

In the actual L099(2) trace, the other alternating factor, K_h,
the full min(s,t) factor, both coefficient levels and G_tr remain.
The moment of one complete alternating factor does not determine
the signed trace of their product. No factor is removed from the
actual trace by this diagnostic, and all heat modes remain in that
unresolved problem. L108's generator obstruction and L099's zero
quartic-scale result are preserved; (2) is a different obstruction
to a particular kernel estimate. The remaining functionals,
joint compensation, finer powers/logarithm, other jets, interacting
error, continuum axioms and finite positive mass remain unresolved.

Completed RESEARCH / REPRODUCTION under the unchanged complete-group
EXPLORE assessment. This is new local decision evidence from the
already recorded symbols and elementary Fourier analysis, with no
claim of originality beyond the sources checked. No numerical
script, coefficient evaluation or reproof of a Ward/flow theorem is used.

## Mathlib

Full matching projected-kernel moment obstruction: **not checked**.
Supporting finite matrix, Fourier-series differentiation, Fejer
uniqueness and Riemann-sum coverage: **not checked**. Unknown coverage
is not absence. No flow-finiteness theorem is used to infer a value
or a bound for this isolated action group.
