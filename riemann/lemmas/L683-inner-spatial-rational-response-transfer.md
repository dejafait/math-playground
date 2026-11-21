# Lemma 683: an inner spatial circle gives an explicitly paid full-root transfer

## Hypotheses

Use exactly L666's family: q>=1 is an integer, n=12q+3,
M=n/3=4q+1, x=-5/4, R=11/8, U=121/64, h=27/(10n), and

    Z={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q},
    e_m real, |e_m|<=1/8.

The original residues are all one, and one displacement vector is used
for every angular u and every spatial variable. Keep the complete
product, its j=0 factor, and the denominator angle 1/u:

    t_j=j/n,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    G(u,zeta)=R^(-1) sum_a W_a(u) sum_(k=0)^(M-1)(a*zeta/R)^k,
    d(u)=sum_a |W_a(u)|^2/(U-|a|^2),
    D=mean_(|u|=1) d(u),
    m(u)=mean_(|zeta|=1) log|G(u,zeta)|,
    H=max_(|u|=1) m(u).

All circle means are normalized; logarithms are natural. For 0<r<1 set

    F(u,z)=R^(-1) sum_a W_a(u)/(1-a*z/R),
    V_r=max_(|u|=|zeta|=1) |F(u,r*zeta)|,
    E_r=(sqrt(42)/11)*n^(3/2)*r^(n/3)/(1-r)*sqrt(D).

L666 gives distinct nodes, |a|<R and nonzero finite W_a on the angular
circle. L657 gives the nonzero spatial slices and logarithmic
integrability; L658 gives finite attained H. No relative error,
root separation, lower bound on |F|, or signed coercivity is assumed.

## Conclusion

For every admissible vector and every 0<r<1,

    V_r <= (1+r)^(M-1)*exp(H)+E_r.                         (1)

In particular, if V_r>E_r then

    H >= log(V_r-E_r)-(M-1)*log(1+r).                     (2)

This retains the full polynomial, its actual degree and leading factor,
and every spatial root, including boundary and zero roots. It is not a
lower bound for V_r relative to the original D.

At the fixed radius r=1/32 the charges can be written as

    E_(1/32) <= n*exp(-7n/12)*sqrt(D),
    (M-1)*log(33/32) <= n/96.                            (3)

Consequently the **unproved** uniform estimate

    V_(1/32) >= c*n*exp(-n/48)*sqrt(D)                   (4)

with an absolute c>0 beyond one uniform onset would imply, beyond
another uniform onset,

    H >= (log D)/2-n/32+log n+log(c/2).                  (5)

By L658 this would give a centered arc of normalized length n^(-2)
whose paid expression satisfies

    log mu(I)+2 mean_(I x T) log|G|-log D+n/16
                           >=2log(c/2)-32*pi^2/9.       (6)

Only the implication (4) => (5)--(6) is asserted. Neither (4), the
target full-H inequality, nor a countersequence to either has been
obtained. The implication is sufficient, not necessary: failure of
(4) would stop this transfer without refuting the H target. The radius
and root cost make (4) a different test from L666's parked c_0 energy
test. V_r contains the complete signed rational response before taking
its modulus; it must not be replaced by a sum of separate moduli.

This is a reproduction/specialization of the inspected root inequality
and rational observation formula, with explicit family constants. It
does not claim a new coercivity theorem or originality beyond those
sources. The separate conceptual audit in Section 5 retains (1)--(6),
including the conditional and uniform-onset qualifications. Support,
actual-Xi realization and all-degree mixed positivity remain open.

## Proof

### 1. Source scope and exact finite remainder

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-full-spatial-root-contribution.md`.
It covers full spatial root accounting, rational observation, original
D and explicitly charged norm costs for the exact target. The present
calculation tests that target through its full geometric-sum identity;
it introduces no new source theorem. L669's fixed-angle loss,
L670/L671's clearing stops and L682's highest-coefficient stop are
comparisons, not premises or replacements for this calculation.

Import F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459, Propositions 1.4--1.5, pp.6--7,
[publisher excerpt](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf):
for a nonzero complex polynomial of actual degree d, actual leading
coefficient b and roots alpha counted with multiplicity,

    mean log|P|=log|b|+sum_alpha log max(1,|alpha|).

Constants have an empty root sum, and circle roots are included. The
assessment already inspected the interior, exterior and boundary cases.
We specialize that formula below; no general Jensen theorem is reproved.

For the angular observation use L666's exact specialization of
V. I. Danchenko and L. A. Semin, *Sharp quadrature formulas and
Nikol'skii type inequalities for rational functions*,
[arXiv:1503.06476v1](https://arxiv.org/pdf/1503.06476v1),
Theorem 2, pp.1--2 and proof pp.6--7, with r=s=1 in that source's
notation. L666 verifies the finite interior/reflected pole set,
ordinary simple pole orders, combined order zero at 0/infinity, and
the exact normalized positive weights. Its source-representation and
independent-audit qualifications remain; no quadrature theorem is
reproved or silently strengthened here.

Put z_a=a/R. The elementary finite geometric-sum identity, with all
M terms retained, gives exactly

    G(u,z)=F(u,z)-T(u,z),
    T(u,z)=R^(-1) sum_a W_a(u)*(z_a*z)^M/(1-z_a*z).     (7)

All denominators are nonzero on |z|<=r<1. The sums are finite and
continuous on the compact angular/spatial circles. In particular V_r
is finite and attained. Each rational F(u,.) is nonzero: its distinct
simple poles 1/z_a have nonzero residues, because z_a and W_a are
nonzero. Thus V_r>0. This statement is only nonvanishing, not (4).

### 2. A pointwise angular charge against the original diagonal

Fix any |u_0|=1. In L666 choose the quadrature phase so that u_0 is
one of the nodes: exp(i*phi)=Bcal(u_0)^2. This changes only the
observation rule, not the displacement vector or D. Its positive
weight w at that node obeys

    w >= 1/[2*(1+9M(n-1))],
    D=sum_l w_l*d(u_l) >= w*d(u_0).

Hence, for every u_0,

    d(u_0) <= 2*(1+9M(n-1))*D <= 6n^2*D.              (8)

The last inequality uses M=n/3 and
2+6n(n-1)<=6n^2 for n>=15. No cancellation estimate for G or F is
extracted from positive quadrature weights. The positivity used in
(8) is only that of the original separate-term diagonal d.
The anchor has W_x=1 and contributes 1/(U-x^2)=64/21, so D>0
and every logarithm of D used here is legitimate.

For |z|=r, apply finite weighted Cauchy--Schwarz to the **tail** in
(7), after keeping its full signed sum in the identity. Because
|z_a|<1, U-|a|^2<=U-x^2=21/64, and |1-z_a*z|>=1-r,

    |T(u,z)|
      <= R^(-1)*sqrt(d(u))
          *sqrt(sum_a (U-|a|^2)*|z_a*z|^(2M)/|1-z_a*z|^2)
      <= R^(-1)*sqrt(d(u))*sqrt(21M/64)*r^M/(1-r)
      <= (sqrt(42)/11)*n^(3/2)*r^(n/3)/(1-r)*sqrt(D)
       = E_r.                                         (9)

Only this explicitly paid remainder is bounded by absolute values;
no absolute-value replacement for the main signed response F occurs.
The normalization uses R=11/8 and exactly the original D.

### 3. The complete-root cost of observing inside the spatial circle

For fixed u write its nonzero spatial polynomial as

    G(u,z)=b_u product_(j=1)^(d_u)(z-alpha_j),
    0<=d_u<=M-1,

using its actual degree. For |z|=r, each root, without restriction on
its modulus, satisfies

    |z-alpha_j| <= r+|alpha_j|
                 <=(1+r)*max(1,|alpha_j|).

The cited formula therefore gives

    |G(u,z)| <= (1+r)^(d_u)*exp(m(u))
              <=(1+r)^(M-1)*exp(H).                   (10)

This includes zero roots, roots on the unit circle, constants and
degree drops. The actual leading factor occurs on both sides before
the inequality; no prescribed top coefficient is treated as nonzero.
No logarithm of a small remainder, root-motion assumption or exchange
of the angular maximum and spatial logarithmic mean is used.

Now (7), (9) and (10) imply (1) at every u and spatial angle before
taking the joint maximum. Rearranging and taking a logarithm only
when V_r>E_r proves (2).

### 4. Required and actual exponential charges at r=1/32

Since sqrt(42)<7,

    (sqrt(42)/11)/(1-1/32) < 224/341 < 1,
    E_(1/32) <= n^(3/2)*32^(-n/3)*sqrt(D).

The integral formula for log gives log 2>1/2 and log 2<1. For real
t>=2, the derivative of t/2-log t is nonnegative and its value at
2 is positive; consequently log n<=n/2. Thus

    (log n)/2-(n/3)*log 32
      <= n/4-(5/6)*n=-7n/12.

This proves the first estimate in (3). The integral inequality
log(1+s)<=s for s>=0 gives
(M-1)*log(33/32)<=(M-1)/32<=n/96, proving the second.

Assume only for this implication that (4) holds uniformly beyond N_c.
Increase the onset, if necessary, until

    exp(-9n/16)<=c/2,

which is possible for a fixed c>0. Since 7/12-1/48=9/16, (3) then
gives E_(1/32)<=V_(1/32)/2. Equations (2)--(4) yield

    H >= log(c/2)+log n+(log D)/2-n/48-n/96,

which is (5), since 1/48+1/96=1/32. An allowable additive constant
in the target is B=max(0,log(2/c)); all onsets are uniform in the
displacement cube. L658's bound
log mu(I)+2 mean_(I x T)log|G|>=2H-2log n-32*pi^2/9
now gives (6).

The successful calculation is the explicit root/remainder transfer,
not the missing hypothesis (4). No estimate in this proof compares
the signed V_(1/32) from below with D. A small absolute tail is not a
logarithmic perturbation theorem and by itself supplies no bound for H.
No mathematical script, numerical root screen or computation is a
premise. The full-H attempt remains inconclusive.

### 5. Separate conceptual audit — 3 November 2026, step 92

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-03-inner-spatial-transfer-audit.md`.
This is a REPRODUCTION audit of the existing conditional transfer.
The named root and rational-quadrature theorems in Section 1 are
imported with their recorded source qualifications. Their manuscripts,
L666's later scalar-flow claims and the missing norm premise (4) are
not certified by this audit. L689 is not a mathematical input here.

**Exact family and inherited logarithms.** The nonanchor ordinates have
successive gaps at least 3h/4 and distance at least 3h/8 from zero.
Their moduli are less than 2qh<9/20. Thus all M nodes are distinct,
nonzero, and satisfy

    25/16 <= |a|^2 < 353/200 < (273/200)^2 < U.

The anchor attains the first equality. This verifies L657/L658's
radial bound with eta=1/100, N=M=n/3, positive integer unit residues
and n>=15, including q=1 and every allowed displacement endpoint.
On the angular circle |a|>t_j and U>t_j|a|, so every factor defining
W_a is finite and nonzero. There is one fixed vector of nodes in all
means and maxima. L657's Vandermonde argument applies to the full M
moments: vanishing of every coefficient would force W_a=0 at every
distinct node. Consequently every spatial polynomial is nonzero.
Its cleared numerator K is nonzero and its angular denominator Q has
no circle zero. L657 imports absolute product logarithmic integrability
from Issa--Lalin, [arXiv:1203.5379v1](https://arxiv.org/pdf/1203.5379v1),
Remark 3.8 and Theorem 4.1/proof, printed p.7, with s=1; no uniform
small-value bound is used. L658's
finite attained H therefore applies to exactly this G. Boundary zeros
are allowed throughout, and Fubini is legitimate for the paid arc.

**Quadrature application and arbitrary phase.** Direct division with
the j=0 factor gives

    W_a(u)=(x/a) product_(1<=j<n)
                  (x-t_j*u)(U*u-t_j*a)/[(a-t_j*u)(U*u-t_j*x)].

For a!=x its possible poles are t_j*x/U and a/t_j, all simple;
it is regular at both 0 and infinity, with value x/a. The anchor is
identically one. Reflection of a/t_j in the unit circle gives
t_j/conjugate(a). These reflected points cannot coincide: comparison
of real parts in t_j*conjugate(b)=t_k*conjugate(a) forces j=k and
a=b. They are nonreal, unlike t_j*x/U; none is zero. Thus L666's
interior set S has K=1+M(n-1) distinct points, all of modulus less
than 4/5. Its union with its circle-reflected set contains every
possible pole; cancellations do not increase orders. The combined
pole order at 0/infinity is zero. This checks the hypotheses of Danchenko--Semin
Theorem 2 at source radius 1 and s=1.

The boundary argument derivative of Bcal is the strictly positive
mu, of total integral 2*pi*K. Hence every phase gives 2K distinct
observations. Dividing the cited integral formula by 2*pi gives
1/(2*mu), and applying it separately to each W_a gives exactly the
original diagonal D. Each nonzero point of S contributes a Poisson
factor between 1/9 and 9; the point 0 contributes one. Therefore a
node chosen at any prescribed u_0 has weight at least
1/[2*(1+9M(n-1))]. Phase choice changes the observation nodes only;
it neither changes D nor requires any signed cross term to be positive.
This proves (8) uniformly, since 2+6n(n-1)<=6n^2. The anchor's
contribution 64/21 ensures D>0. The audit covers this application of
L666, not every independent assertion elsewhere in that lemma.

**Finite tail and complete roots.** In (7) all M geometric terms are
retained and |a*z/R|<r<1 on |z|=r. The rational response has distinct
poles R/a with nonzero residues -W_a/a, so it is not identically zero.
The sums are continuous on the compact circles; V_r is positive,
finite and attained. Weighted Cauchy--Schwarz uses the M original
positive factors U-|a|^2, each at most 21/64. Its prefactor is exactly

    R^(-1)*sqrt(6n^2)*sqrt(21M/64)
                          =(sqrt(42)/11)*n^(3/2).

This confirms (9) against the original D. The root formula applies
to every nonzero slice at its actual degree, including degree zero.
For every root, |z-alpha|<=(1+r)*max(1,|alpha|) includes alpha=0,
|alpha|=1 and |alpha|>1 without a separation hypothesis. The actual
leading factor is retained. Thus (10) holds pointwise before the joint
maximum is taken. The exact finite identity, paid tail and root bound
prove (1); taking the logarithm is permitted precisely under V_r>E_r
in (2). No logarithmic perturbation bound or exchange of a maximum
with a spatial mean is used.

**Fixed radius, uniform onset and paid arc.** Section 4's inequalities
hold for all n>=15: sqrt(42)<7, 224/341<1, log 2>1/2,
log n<=n/2 and log(1+1/32)<=1/32. They give exactly

    E_(1/32)<=n*exp(-7n/12)*sqrt(D),
    (M-1)*log(33/32)<=n/96.

If (4) holds with one absolute c>0 for all admissible vectors and
all prescribed n>=N_c, it suffices to increase that onset to

    max(N_c,15,ceil((16/9)*max(0,log(2/c)))).

Then E_(1/32)/V_(1/32)<=(1/c)*exp(-9n/16)<=1/2,
because 7/12-1/48=9/16. The surviving logarithmic exponent is
1/48+1/96=1/32, proving (5), including +log n and log(c/2).
All constants and this onset are independent of the displacement
vector. L658 chooses the maximizing angle for the same m and H,
and its centered arc has normalized length n^(-2). Substitution of
(5) in its bound 2H-2log n-32*pi^2/9 cancels both the explicit
2log n and, after adding n/16, the term -n/16. This is exactly (6).

No load-bearing defect was found. Equations (1)--(6) are retained
with their original hypotheses; the mathematical dependencies and
strength of the statement are unchanged. The newly checked item is
the conditional local transfer, not a new result beyond the cited
tools, a proof of (4) on the full cube, an H/support bridge or an RH
candidate. Failure of the sufficient norm test would still not refute
the H target. No mathematical script or numerical evidence is needed
for this finite audit.

## Mathlib

Reuse the assessment's inspected
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.mahlerMeasure_mul`. These support complete-root accounting,
not the unproved estimate (4). Totalized logarithms do not replace
nonzero hypotheses. Full matching coverage for the rational quadrature,
this family-specific transfer or (4) has not been checked; unknown
coverage is not evidence of absence. No Lean formalization or separate
source-manuscript audit is claimed. Section 5 is the separate informal
audit of the family-specific transfer, not a formal verification.
