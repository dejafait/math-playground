# L121 — The exterior scalar-placement error has a cubic-scaled limit

## Hypotheses

Use exactly L113's Delta_sc=R_bulk,moved-R_bulk,sc, both actual L010
probes i=3,6, SU(2), the straight lower-rooted direction-1 forest,
the all-face relative fixed-link box D=(-4,4)^4, sufficiently fine
admitted even N, a=8/N and tau=1/16. Take the bare small-coupling
coefficient at fixed mesh before refinement. Coordinates and norms
are ordinary stored ones. Retain every interior axial level,
transverse end row, both generator orientations and all exterior heat
modes. Import L111's stencils T_r,C_r, ordered r list with its signs,
compact displacement b_(r,t), energy E_j, and zero extension J=J_2.
Import L113's path operators S_alpha and clamped common-index scalar
coefficients phi_(k,alpha,t). The finite middle projection in the
definition of Delta_sc is the original relative gradient projection P.

On the full grid use L114's real edge projection kernel p:

    P_inf(z,w)=p(z-w),
    (S_alpha^inf v)(z)=sum_h s_alpha(h) v(z+h),
    (D T_r v)(x)=sum_h A_r(h) v(x+h),
    (C_r v)(x)=sum_q C_r(q) v(x+q).

Thus s_alpha(h) is an edge-by-plaquette component matrix and all its
shifts and signs remain. All stencils use the displayed lower-vertex
finite-shift convention. Define
the plaquette kernel

    g_(r,j)(d)=sum_(h,q) A_r(h) C_r(q) e_j(d+h+q),       (1)

where E_j(x,y)=e_j(x-y). It is the kernel of D T_r C_r E_j,
without the displacement multiplier. All stencil lists are finite.
Use L120(2)'s continuum coefficients phi_(k,alpha), c_(i;kl),
V_(k,mu) and actual lower-rooted prefix Phi_k, including its constant
component-1 axial mode. The continuum displacement component in b_r
is u_(rho(r)); signs already belonging to the stencil stay there.

## Conclusion

For the original path shifts h,n and m=2,3,4 set

    H_(r,j;alpha,beta,h,n)(d)
      =tr[g_(r,j)(d) s_alpha(h)^T
                      p(-d-h+n) s_beta(n)],

    A_(r,j,m;alpha,beta)
      =sum_(h,n,d) n_m H_(r,j;alpha,beta,h,n)(d),
    B_(r,j,m;alpha,beta)
      =sum_(h,n,d) (d_m-n_m) H_(r,j;alpha,beta,h,n)(d).   (2)

These are real tensors, absolutely convergent in d and, in absolute
value, summable over every j in Z. The following real functional is
absolutely convergent in its complete axial and exterior heat sums:

    K_(i,sc)=sum_(k,l)c_(i;kl)
      sum_(r,j,m,alpha,beta)
        integral_D (x_1+4) u_(rho(r))(x)
          [A_(r,j,m;alpha,beta)
               phi_(l,alpha)(x) partial_m phi_(k,beta)(x)
           -B_(r,j,m;alpha,beta)
               partial_m phi_(l,alpha)(x) phi_(k,beta)(x)] dx.
                                                               (3)

For both probes,

    a^3 Delta_sc -> K_(i,sc).                            (4)

The value and sign of (3) are not evaluated. This limit retains the
two path-stencil placement differences and the finite scalar
projection commutator together; none is silently discarded. It is
not a limit theorem for transverse H or for the complete other/other
contribution. L110's exterior-circulation remainder and L115's
energy-placement error remain. L120's generator error and the other
known functionals remain unevaluated. No complete compensation with
-12 gamma D_i, finer-power or logarithmic bound, interacting reflected
error <=c_box/2, continuum axioms, reflection positivity, infrared
control or finite positive mass is established. The complete group's
outside factor 3 is not applied in (3).

## Proof

### 1. Import the actual weighted trace and control heat tails

L111 and L113 give exactly

    Delta_sc=a^-1 sum_(k,l,s,t)c_(i;kl,a) min(s,t)
                     Tr[X_(t,t-s)(Z_(kl;st)-Z^sc_(kl;st))],
    X_(t,j)=J^* sum_r (D T_r C_r E_j) M_(b_(r,t)) J,
    Z_(kl;st)=F_l(s)^T P F_k(t),
    Z^sc_(kl;st)=a^2 sum_(alpha,beta) S_alpha^T P
             M^1_(phi_(l,alpha,s) phi_(k,beta,t)) S_beta,
    F_k(t)=a sum_alpha S_alpha M^2_(phi_(k,alpha,t)).     (5)

The last identity is exact on the finite relative spaces. In (5),
P lies between the fixed path filters, and both coefficient levels
are unchanged. Import the individual estimates used in L113(19):

    ||X_(t,j)||_HS<=C N^(3/2) W_j,
    ||Z-Z^sc||_HS<=C a^3 p(k)p(l) N^(3/2),
    W_j<=C(1+|j|)^(-5/2),
    Q_j=|| |d| e_j(d)||_2<=C(1+|j|)^(-3/2).             (6)

Here and below a fixed polynomial p may be enlarged. Both W and Q
are summable over Z. L080's mode normalization and L120(6) give

    |c_(i;kl,a)|<=C_i exp[-(tau/16)(|k|^2+|l|^2)],
    c_(i;kl,a) -> c_(i;kl) at each fixed pair.            (7)

Mesh labels not present are extended by zero. The component is part
of the mode label; there is no all-zero mode. By trace
Cauchy--Schwarz and sum_(s,t) min(s,t) W_(t-s)<=N^2 sum_j W_j,
the a^3-scaled part of (5) on any set of exterior pairs is bounded
by C sum_set |c_(i;kl,a)|p(k)p(l). Indeed before scaling the bound
is C a^2 N^5 times that sum and aN=8. The Gaussian majorant (7)
therefore removes the heat tail uniformly. This imports L113's
actual error estimate, rather than rederiving the finite contraction.

### 2. Replace the finite P in both terms with a subcubic error

Let P_bulk=J_1^* P_inf J_1. In the scalar-collected trace, L114(3)
already proves a replacement error O(N^(5/2)(log N)^(3/4)). For the
uncollected term in (5), the corresponding unweighted error is

    Tr[X F_l(s)^T (P-P_bulk) F_k(t)].                   (8)

Every nonzero column of X F_l^T is within a fixed path range of
the compact support of b_(r,t), because X ends with M_b J and
F_l^T=a sum_alpha M_phi S_alpha^T. Thus, exactly,

    X F_l^T=X F_l^T R_Omega,

where the endpoints of Omega have distance at least delta N from
all transverse faces and |Omega|<=C N^3. This holds uniformly in
the levels and heat labels. It restricts projection-adjacent rows,
not X's nonlocal output. L114(2) retains every input edge and gives
||R_Omega(P-P_bulk)||_HS<=C(log N)^(3/4). The bounds in L113(14)
and (6) imply

    ||F_k X F_l^T||_HS
                <=C a^2 p(k)p(l) N^(3/2) W_j.

Cyclic trace identities and (8) give an unweighted error at most
C a^2 p(k)p(l) N^(3/2) W_j (log N)^(3/4). Sum the original
min(s,t), all heat labels and the outside a^-1 in (5). The result
is C_i a N^(7/2)(log N)^(3/4)=O(N^(5/2)(log N)^(3/4)).

Denote by Delta_sc^bulk (5) with only P replaced by P_bulk in both
terms. We have proved

    Delta_sc-Delta_sc^bulk=o(N^3).                      (9)

No scalar or component filter crossed a projection in this comparison.
The imported boundary estimate applies before any spatial truncation
because the displacement is already at X's input end.

### 3. Expand the complete scalar difference in its closed trace

Let x,y be finite plaquette indices, d=x-y and j=t-s. The kernel
of X is sum_r g_(r,j)(d)b_(r,t)(y). In the trace, Z has entry (y,x).
A nonzero entry of S_alpha from input y to output z has z=y-h
and coefficient s_alpha(h); a nonzero S_beta entry from input x
to output w has w=x-n and coefficient s_beta(n). Thus P_bulk's
entry in this product is exactly p(-d-h+n). To retain every finite
component restriction, let chi_2(v) and chi_1(v) be the diagonal
selectors for existing plaquette and edge components at index v.
For this finite trace use

    H_N(y,d)=tr[chi_2(y+d) g_(r,j)(d) chi_2(y)
       s_alpha(h)^T chi_1(y-h) p(-d-h+n)
          chi_1(y+d-n) s_beta(n) chi_2(y+d)].

The other labels in H_N are understood as in (2). It equals H when
all adjacent rows are interior. This keeps partial component
restrictions as matrices rather than assuming their cancellations
are preserved by scalar indicators. For every retained entry the
scalar difference between the two Z terms is exactly

    L_(kl;alpha,beta;st)(y,d,n)
      =phi_(l,alpha,s)(y) phi_(k,beta,t)(y+d)
       -phi_(l,alpha,s)(y+d-n) phi_(k,beta,t)(y+d-n).    (10)

The collected multipliers are edge multipliers at w, which explains
y+d-n in their two factors. The left path shift h remains in the
projection kernel. Both original plaquette multipliers remain at
their actual inputs y and x. Consequently the exact trace is

    Delta_sc^bulk
      =a sum_(k,l,s,t,r,alpha,beta,h,n,y,d)
         c_(i;kl,a) min(s,t) b_(r,t)(y)
           H_N(y,d)
           L_(kl;alpha,beta;st)(y,d,n),                 (11)

with j=t-s in H_N and x=y+d; the selectors enforce the finite
plaquette indices. Equation (11) is a kernel expansion of finite
matrix products, so it involves no interchange of infinite sums.
It combines all three scalar-placement pieces from L113's proof:
the two path-placement differences and [M_phi,P]. Their separate
expressions sum to (10); no separate commutator estimate is now
postulated. At boundary indices the clamped extensions in L113
supply exactly the values used in (10).

### 4. Establish joint spatial and axial tails before local expansion

Write ||.||_2 for the ell^2 Frobenius norm. P_inf has a bounded
matrix symbol of norm one on the finite-measure torus. Fourier
Plancherel therefore gives ||p||_2<=C. The finite shifts in (1) and
(6) give

    ||g_(r,j)||_2<=C_r W_j,
    || |d| g_(r,j)(d)||_2<=C_r(Q_j+W_j).               (12)

For the second bound substitute z=d+h+q in each summand, use
|d|<=|z|+|h+q|, and sum the finite stencil norms. Let M be one plus
the maximum absolute stencil shift, and define the positive majorant

    m_(r,j;alpha,beta,h,n)(d)
      =||g_(r,j)(d)||_F ||s_alpha(h)||
                         ||p(-d-h+n)||_F ||s_beta(n)||.

Both |H| and |H_N(y,d)| are at most this majorant: every chi has
norm at most one, and the Frobenius trace inequality applies to
the full matrix product. Spatial Cauchy--Schwarz yields

    sum_d (|d|+M) m_(r,j;alpha,beta,h,n)(d)
      <=C ||(|d|+M)g_(r,j)(d)||_2
                       ||p(-d-h+n)||_2
      <=C_r(Q_j+W_j).                                 (13)

Hence the left side, also summed over r,alpha,beta,h,n,j, is finite.
Let Theta(J0,R) be that positive sum restricted to |j|>J0 or
|d|>R. Absolute summability proves Theta(J0,R)->0 as J0,R tend
to infinity. This concerns the joint closed trace. It asserts no
separate first absolute moment of P, a path projection, or E_j.

The exact rearrangement of (10) is

    L=phi_l(y)[phi_k(y+d)-phi_k(y+d-n)]
        +[phi_l(y)-phi_l(y+d-n)] phi_k(y+d-n).

L113(3), including its clamped extension at every boundary row,
therefore gives

    |L|<=C a p(k)p(l)(|d|+M).                          (14)

There are at most C N^3 possible y. For a fixed j the complete
level weight sums to at most N^2. The displacement is uniformly
bounded. Apply (13)--(14) to the omitted offsets in (11):

    a^3 |Delta_sc^bulk-Delta_sc^bulk[J0,R]|
                   <=C_i a^5 N^5 Theta(J0,R)
                   <=C'_i Theta(J0,R).                 (15)

The norm-one finite component selectors satisfy the same majorant.
The same calculation controls any exterior heat tail by the Gaussian
sum in (7), uniformly in J0,R,N. Thus it is legitimate to fix
heat labels and spatial/axial offsets before the local limit.

### 5. Check first derivatives of the actual path coefficients

Fix heat labels, |j|<=J0 and |d|<=R. A nonzero b_(r,t)(y) puts y
in a fixed physical interior set. All x=y+d and adjacent path
endpoints are therefore existing interior rows at sufficiently fine
mesh. Their finite-space indicators in (11) equal one. The axial
support is also interior; with s=t-j, both levels are admitted there.

For each fixed mode the smooth sampled transverse lift divided by a
is, at its actual edge centers,

    A_(k,a,mu)-delta_(mu,a)
      [a sum_(ell=0)^(t-1) A_(k,a,1)(-4+(ell+1/2)a,.)]. (16)

This is L028's exact straight-forest formula used in L120(12),
not the averaged path diagnostic substituted for the actual lift.
The sine/cosine mode expressions and the physical eigenvalues in
L080(5) converge at every fixed mode. L080(8)--(10)'s exact cosine
prefix sum, including sa/sqrt(8) for the constant axial mode, converges
with every fixed transverse derivative to Phi_k on the compact set.
For a smooth function f the forward difference at an edge is the
integral of its derivative along that edge; differentiation in a
transverse coordinate commutes with this integral. Thus the smooth
expression in (16) converges in C^1 in the transverse coordinates
to V_(k,mu), uniformly over the levels on that set. Needed higher
derivatives are bounded at these fixed labels by the same explicit
mode and prefix expressions. Their shifts by fixed half or whole
mesh cells tend to zero.

Each actual signed two-edge path is a fixed finite sum of those
sampled lifts. By L088(11)--(12) its limiting values are V_mu+V_nu
for b and -V_mu+V_nu for q. Its smooth expression, on this interior
set, consequently converges in transverse C^1 to L120's
phi_(k,alpha). This also proves polynomial bounds on phi and its
first derivatives on the compact set: differentiation adds only a
fixed polynomial mode factor, and the prefix length is at most 8.
Enlarge p in (6)--(7) to include them. Coordinate clamping is not
used here, since all sampled indices are interior.

Let xi=(-4+at,(-4,-4,-4)+ay). The integral difference formula in
the exact rearrangement of (10), and the just-established C^1
convergence at s=t-j and t, give uniformly on displacement support

    L/a -> sum_(m=2)^4
       [n_m phi_(l,alpha)(xi) partial_m phi_(k,beta)(xi)
        -(d_m-n_m) partial_m phi_(l,alpha)(xi)
                                  phi_(k,beta)(xi)].   (17)

Both physical levels coincide only in this fixed-offset limit.
No Taylor expansion across the pinned upper potential or a face is
performed. The upper pin and the exact lower prefix remain distinct.
Also b_(r,t)(y)->u_(rho(r))(xi) uniformly, by L028's globally smooth
displacement convergence.

### 6. Normalize the Riemann sum and remove all tails

For precision, define the derivative trace T_(i,sc,N) by replacing
H_N by H in (11), b by u_(rho(r))(xi), and L by a times the
right side of (17), while allowing every d in Z^3. Keep the original
c_(i;kl,a), s,t and min(s,t). Sum y over physical interior grid
points; u makes this a compact sum. The common coefficient level in
this auxiliary trace is t, for both continuum columns. This is a
defined comparison trace, not a finite-mesh equal-level identity.
Its d sum converges absolutely by (13), and its normalized tails
have the same bound (15), using the polynomial continuum derivative
bounds just proved. On fixed heat and offset cutoffs, (17) and
displacement convergence make the difference from (11) o(N^3).
Uniform tail removal and (9) consequently show

    Delta_sc-T_(i,sc,N)=o(N^3).

In (11), write L=a(L/a). After multiplication by a^3, its scalar
normalization is a^5 min(s,t)=a^4 [a min(s,t)]. For s=t-j,

    a min(s,t)=at-a max(j,0) -> x_1+4.                  (18)

Thus for fixed labels and offsets the t,y sum is precisely an a^4
four-dimensional Riemann sum. Equations (7), (17)--(18) identify its
limit as the corresponding term of (3), with the original kernel
factor H and its n_m and d_m-n_m weights. The integrand is continuous
and compactly supported through u. Uniform convergence on that support
justifies the Riemann limit. There is no extra box-length factor and
no extra color or factor-3 insertion.

Equation (13) proves absolute convergence of both tensors in (2)
and their complete j sums. Each integral in (3) is bounded by
C p(k)p(l), including its derivative. The continuum Gaussian
majorant from (7) is summable after multiplication by these polynomial
factors. The full functional is therefore absolutely convergent,
real, and has kernel-tail bound C_i Theta(J0,R) and a vanishing
Gaussian heat tail. These are the same uniform bounds used for the
finite traces in (15).

Given a tolerance, first choose a finite exterior cutoff, then J0,R
so the finite and continuum tails are below it. Take the mesh limit
with all cutoffs fixed using (17)--(18); finally let the tolerance
tend to zero. This proves a^3 Delta_sc^bulk -> K_(i,sc). Equation
(9) proves (4). The resulting first-derivative substitution in the
complete error is accurate to o(N^3): (13)--(15) control its tails
and (17) controls each fixed-offset remainder. No quantitative
N^2 remainder follows from this qualitative convergence.

### 7. Scope and applicability

This is one standard-method REPRODUCTION subtest under the unchanged
EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction and placement definitions are imported from
L111/L113, not rederived from Wick pairings. The specialization is
needed because the scalar-placement error retained a different
projection order from L119/L120's displacement error. The proof uses
the standard named Fourier Plancherel theorem, finite
Hilbert--Schmidt trace inequalities, absolute-series convergence and
Riemann-sum convergence in the explicit forms above. It imports no
general Ward or flow finiteness theorem for this bare isolated group.
The result is local progress, without a novelty claim beyond the
sources checked.

L096's component-dependent operator shortcut is not used: all filters
keep their order and no small projection operator norm is asserted.
L109's failed separate absolute moments are not used: the weighted
energy kernel and the unweighted projection kernel are paired before
absolute summation in (13). Every boundary input is retained in (8),
and the finite path indicators are discarded only after controlled
offset truncation makes their endpoints interior. Both original
coefficient levels, the physical prefix and constant mode survive
the limiting argument. L118's exact full-grid diagonal cancellation
does not set this retained placement error to zero. The coefficient
is unevaluated and the earlier cubic errors remain; no complete
solution or candidate for Yang--Mills is asserted. An eventual
numerical comparison retains L084/L082's arithmetic qualifications.

## Mathlib

Full matching scalar-placement error limit: **not checked**.
Supporting Fourier Plancherel, Hilbert--Schmidt trace inequalities,
absolute-series convergence and Riemann-sum coverage: **not checked**.
Unknown availability is not absence. No numerical certificate or
finite-mesh sign is used.
