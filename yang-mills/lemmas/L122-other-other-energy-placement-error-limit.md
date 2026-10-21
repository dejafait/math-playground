# L122 — The energy-placement error has a cubic-scaled limit

## Hypotheses

Use exactly Delta_en=R_bulk,sc,Pbulk-R_prod in L115(3), with both
actual L010 probes i=3,6, SU(2), the straight lower-rooted direction-1
forest, all-face relative fixed-link box D=(-4,4)^4, sufficiently fine
admitted even N, a=8/N and tau=1/16. Take the bare small-coupling
coefficient at fixed mesh before refinement. All spaces have ordinary
stored-coordinate norms. Retain every interior axial level, transverse
end row, both generator orientations and every exterior heat mode.

Import L115's ordered finite stencil A_r=D T_r C_r, E_j, compact
displacement b_(r,t), extensions J_1,J_2 and
P_bulk=J_1^* P_inf J_1. This is a compression, not a finite orthogonal
projection. Import its exact scalar product

    psi_(kl;alpha,beta;st)=phi_(l,alpha,s) phi_(k,beta,t).

The two factors keep their original levels and path labels, and are
L115's globally clamped common-index scalars. No field is smoothly
extended through a pinned face. Use exactly L121's shift conventions,
real kernels p and g_(r,j), finite component selectors chi_1,chi_2,
closed-trace kernel H, and tensor B_(r,j,m;alpha,beta) in its (2).
Thus

    (S_alpha^inf v)(z)=sum_h s_alpha(h) v(z+h),
    H_(r,j;alpha,beta,h,n)(d)
      =tr[g_(r,j)(d) s_alpha(h)^T
                       p(-d-h+n) s_beta(n)],
    B_(r,j,m;alpha,beta)
      =sum_(h,n,d) (d_m-n_m) H_(r,j;alpha,beta,h,n)(d). (1)

Use the continuum coefficients phi_(k,alpha), c_(i;kl) and physical
prefix of L120(2), and their transverse C^1 convergence established
in L121, proof section 5. The displacement limit is
u_(rho(r)); signs in the ordered r stencil remain in g, not in u.
The component-1 constant axial mode and the physical lower-rooted
prefix are retained.

## Conclusion

The following real functional is absolutely convergent in all its
axial-offset, spatial-kernel and exterior heat sums:

    K_(i,en)=sum_(k,l)c_(i;kl)
      sum_(r,j,m,alpha,beta) B_(r,j,m;alpha,beta)
        integral_D (x_1+4) u_(rho(r))(x)
           partial_m[phi_(l,alpha)(x) phi_(k,beta)(x)] dx,
                    j in Z, m=2,3,4.                 (2)

For both actual probes,

    a^3 Delta_en -> K_(i,en).                         (3)

In particular the finite rectangular path error and joint energy
commutator of L115(7) are retained together in this coefficient.
Neither is declared negligible. The first-derivative comparison
defined in proof section 4 has o(N^3) error. No quantitative N^2
remainder follows.

The value and sign of (2) are unevaluated. The exterior-circulation
remainder in L110 still prevents a limit theorem for the actual
transverse H trace. The other known functionals, complete other/other
coefficient and compensation with -12 gamma D_i remain unevaluated.
The group's outside factor 3 has not been applied in (2). Other
response jets, finer powers and logarithm, matching, interacting error
<=c_box/2, continuum fields/axioms, reflection positivity, infrared
control and finite positive mass remain unresolved. There is no
candidate Yang--Mills solution.

## Proof

### 1. Expand the exact finite trace before any approximation

Fix k,l,alpha,beta,r,s,t and write j=t-s, b=b_(r,t), psi for the
product in the hypotheses, and X=J_2^* A_r E_j M_b J_2. L115(14)
and (2), with their original outside factor a, give respectively

    T_sc=Tr_edge[P_bulk M_psi^1 S_beta X S_alpha^T],
    T_prod=Tr_edge[P_bulk S_beta
                         J_2^* A_r E_j M_(b psi)^2 J_2 S_alpha^T].

The full Delta_en is a times the sum of T_sc-T_prod weighted by
c_(i;kl,a) min(s,t). These are finite rectangular traces, so cyclic
expansion involves no unbounded inverse or infinite trace interchange.

Let y be the input plaquette index of X, x=y+d its output, and let
h,n be respectively shifts of S_alpha,S_beta. The left edge index
in S_alpha^T is y-h; the right edge index in S_beta is x-n. Hence
the projection entry is p((y-h)-(x-n))=p(-d-h+n). Multiplication
by psi in T_sc is at the right edge x-n. Multiplication by psi in
T_prod is at the input plaquette y. The exact scalar difference is
therefore

    L_en(y,d,n)=psi(y+d-n)-psi(y).                     (4)

This fixes both the sign and the right path shift. Moving psi across
S_beta or A_r E_j separately is unnecessary; their combined error
is exactly (4), consistent with the full identity L115(6)--(7).

Retain the same matrix of finite component restrictions as L121:

    H_N(y,d)=tr[chi_2(y+d) g_(r,j)(d) chi_2(y)
      s_alpha(h)^T chi_1(y-h) p(-d-h+n)
         chi_1(y+d-n) s_beta(n) chi_2(y+d)].           (5)

Each chi selects the components actually stored at its index. In
particular boundary rows may have only some components; they are
not replaced by scalar indicators. Expanding the products gives
the exact identity

    Delta_en=a sum_(k,l,s,t,r,alpha,beta,h,n,y,d)
      c_(i;kl,a) min(s,t) b_(r,t)(y) H_N(y,d) L_en(y,d,n).
                                                               (6)

All finite component restrictions stay in (5). Nonzero terms of
(6) have y in the compact displacement support, but the output
y+d need not be there. The original two levels remain distinct.

### 2. Import joint tails and bound the exact scalar difference

Let M exceed the absolute ranges of all fixed stencil shifts and
let m_(r,j;alpha,beta,h,n)(d) be L121's positive majorant

    ||g_(r,j)(d)||_F ||s_alpha(h)||
                         ||p(-d-h+n)||_F ||s_beta(n)||.

L121 proof section 4 establishes, including partial component
selectors, that |H_N(y,d)| and |H(d)| are at most m(d), and

    sum_d (|d|+M) m(d) <= C_r(Q_j+W_j),
    sum_(j in Z)(Q_j+W_j)<infinity.                   (7)

This pairs the weighted ell^2 energy kernel with the unweighted
ell^2 projection kernel by Cauchy--Schwarz. It uses no separate
absolute first moment. Import its positive tail Theta(J0,R), which
is the sum of the left side of (7), including the fixed label lists,
restricted to |j|>J0 or |d|>R. Thus Theta(J0,R)->0.

L115(4) applies to the complete product psi, also at clamped boundary
indices. Consequently

    |L_en(y,d,n)|<=C a p(k)p(l)(|d|+M).               (8)

There are at most C N^3 possible y. For each j the sum of min(s,t)
over all admitted pairs with t-s=j is at most N^2. Since b is
uniformly bounded, (6)--(8) give

    a^3 |Delta_en-Delta_en[J0,R]|
                     <=C_i a^5 N^5 Theta(J0,R)
                     <=C'_i Theta(J0,R),             (9)

where aN=8. Both finite selectors and all boundary inputs satisfy
this positive majorant; no cancellation is required in the tail.

Import L121(7)'s coefficient convergence and full Gaussian bound

    c_(i;kl,a)->c_(i;kl),
    |c_(i;kl,a)|<=C_i exp[-(tau/16)(|k|^2+|l|^2)].   (10)

Use a fixed enlarged polynomial p also covering continuum first
derivatives, as justified in L121 section 5. Mesh labels absent from
the finite spectrum are extended by zero. The same counting in
(9), now on any set of exterior pairs, bounds its normalized sum
by C sum_set |c_(i;kl,a)|p(k)p(l). Equation (10) thus removes the
complete heat tail uniformly, also under kernel truncation. No
internal covariance frequencies have been cut off.

### 3. Identify the fixed-offset derivative limit

Fix heat labels and |j|<=J0, |d|<=R. Compact support of b at y
separates y, y+d and their finitely shifted path endpoints from all
transverse faces at sufficiently large N. Every chi in (5) is then
the identity, so H_N=H exactly. Compact axial displacement support
also keeps s=t-j and t among the admitted interior levels.

Set xi=(-4+at,(-4,-4,-4)+ay). L121 section 5 proves the actual
clover/path coefficients converge in transverse C^1 on this support
at fixed modes, uniformly over the sampled axial levels. It uses
the exact forest prefix, including the constant component-1 mode;
it does not assign a smooth continuation through the upper pin.
For the smooth interior representatives of psi the integral formula
for a difference along a segment of length a(d-n) gives

    L_en(y,d,n)/a
       ->sum_(m=2)^4 (d_m-n_m)
            partial_m[phi_(l,alpha)(xi) phi_(k,beta)(xi)]. (11)

Indeed the transverse derivative of the product is
phi_l partial_m phi_k+(partial_m phi_l) phi_k; both factors retain
levels s and t until the fixed j limit makes their physical levels
coincide. The C^1 convergence controls these products uniformly
on the segment. Its finitely many offsets remain interior. This
is an integral difference argument, not a Taylor expansion of
clamped coefficients at a pinned face. Also, by the displacement
convergence imported in L121,

    b_(r,t)(y)->u_(rho(r))(xi)

uniformly on the same compact support.

### 4. Normalize, remove tails and prove the stated functional

Define T_(i,en,N) by the right side of (6) with H_N replaced by H,
b_(r,t)(y) replaced by u_(rho(r))(xi), and L_en replaced by a
times the right side of (11). Keep the original c_(i;kl,a), s,t,
min(s,t) and all d in Z^3. Sum y over the interior transverse grid;
u makes this a compact sum. Both continuum coefficients in this
comparison are evaluated at xi. This defines an auxiliary trace;
it is not an equal-level identity for finite coefficients.

Equation (7) proves its absolute kernel convergence, and the
continuum derivative bounds give it the same kernel and heat tails
as (9)--(10). At fixed heat and offset cutoffs, (11) and displacement
convergence give a vanishing normalized difference from (6).
Removing tails after that fixed-cutoff limit proves

    Delta_en-T_(i,en,N)=o(N^3).                        (12)

In (6) write L_en=a(L_en/a). After scaling by a^3, the weight is

    a^5 min(s,t)=a^4 [a min(s,t)],
    a min(s,t)=at-a max(j,0)->x_1+4.                  (13)

For each fixed j and heat/shift labels, the sum over t,y is therefore
an a^4 four-dimensional Riemann sum on D. Its integrand is continuous
and compactly supported through u, and (10)--(11) give uniform
convergence there. Its limit is

    c_(i;kl) H_(r,j;alpha,beta,h,n)(d)
      sum_m (d_m-n_m) integral_D (x_1+4) u_(rho(r))(x)
                    partial_m(phi_(l,alpha) phi_(k,beta))(x) dx.

No additional box-length, color or outside factor 3 is introduced.
Summing d,h,n identifies exactly B in (1). Equation (7) proves
absolute convergence of that tensor and its full j sum. Each integral
is bounded by C p(k)p(l); (10) then proves absolute convergence in
the full exterior spectrum as well. All kernels and coefficients
are real, so (2) is real.

Given a tolerance, first remove a finite exterior heat tail using
(10), and then choose J0,R using (9), for both finite and continuum
expressions. Take the mesh limit with those cutoffs fixed using
(11)--(13). Finally let the tolerance tend to zero. This proves
(3). The independent finite-compression cancellation in L116/L118
does not set the retained difference (4) to zero; it concerns the
separate comparison R_prod. No coefficient value is inferred here.

### 5. Specialization and qualifications

This is one RESEARCH / REPRODUCTION subtest under the unchanged
EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
L115 supplies the finite identity; L120/L121 supply the continuum
columns, heat convergence, C^1 convergence and joint kernel estimates.
They are imported rather than rederived. L121's limit concerns a
different scalar difference, so the energy-placement specialization
requires the exact subtraction (4) and derivative (11). The rest is
standard absolute-series and Riemann-sum convergence with the displayed
uniform bounds. No general Ward or flow finiteness theorem assigns
a coefficient to this isolated bare forest group. This is local
standard-method progress without a novelty claim beyond checked sources.

The exact subtraction retains all three pieces of L115(7); none is
bounded separately and dropped at cubic scale. Compact input support
never implies compact output, and finite boundary selectors are removed
only after controlled truncation makes every adjacent row interior.
No component filter moves through P_bulk, no projection operator-norm
gain is assumed, and no separate absolute first moment is used.
ATTEMPTS/028--032 remain applicable to their failed shortcuts. The
fixed-offset limit retains the actual lower prefix and both original
coefficient levels. Numerical comparison with D_i would still carry
L084/L082's saved-table and IEEE qualifications; none is attempted here.

## Mathlib

Full matching energy-placement error limit: **not checked**.
Supporting finite rectangular trace cyclicity, absolute-series
convergence and Riemann-sum coverage: **not checked**. Unknown
availability is not absence. The load-bearing joint kernel and actual
path convergence results are imported from L121, not inferred from a
numerical preview. No mathematical script or numerical evidence is used.
