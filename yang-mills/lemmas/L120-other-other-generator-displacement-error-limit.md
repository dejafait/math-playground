# L120 — The generator-displacement placement error has a cubic-scaled limit

## Hypotheses

Use L119's exact Delta_V and V_N, SU(2), both actual L010 probes
i=3,6, the straight lower-rooted direction-1 forest, the all-face
relative fixed-link box D=(-4,4)^4, admitted even N, a=8/N and
tau=1/16. Take the bare small-coupling coefficient at fixed mesh
before refinement. Use ordinary stored coordinates. Keep every
interior axial level, transverse end row, both generator orientations
and the full exterior heat sum. Import L119's finite-shift convention,
r list with its ordered signs, rho(r), B_(r,j,m), v_(r,t,m) and
Z_(kl;st)=F_l(s)^T P F_k(t). No coefficient is evaluated below.

Import L113's exact S_alpha and phi_(k,alpha,t), where alpha=(pi,b)
or (pi,q) for a transverse plane pi=(mu,nu), mu<nu. On the full grid
use the same finite stencils S_alpha^inf and L114's P_inf. Define
the real 3-by-3 plaquette convolution kernel q_(alpha,beta) by

    Q_(alpha,beta)=(S_alpha^inf)^* P_inf S_beta^inf,
    Q_(alpha,beta)(x,y)=q_(alpha,beta)(x-y).             (1)

All indices in (1) are lower-vertex indices, as in L119. In
particular, no component-center phases are discarded.

For the continuum exterior columns use L080's real relative modes,
A_k=f_k/sqrt(lambda_k), lambda_k=(pi/8)^2 |k|^2, and the actual
continuum probe form B_i. Let

    Phi_k(x)=integral_(-4)^(x_1) A_(k,1)(h,x_T) dh,
    V_(k,mu)(x)=A_(k,mu)(x)-partial_mu Phi_k(x),
    phi_(k,(pi,b))(x)=V_(k,mu)(x)+V_(k,nu)(x),
    phi_(k,(pi,q))(x)=-V_(k,mu)(x)+V_(k,nu)(x),
    c_(i;kl)=exp[-tau(lambda_k+lambda_l)] (B_i)_(kl).   (2)

The prefix in (2) is used only on compact interior coefficient
support. It is not assigned a zero value at the separately pinned
upper face. The constant component-1 axial mode is included.

## Conclusion

The following universal real tensors and continuum functional are
absolutely convergent in the displayed spatial, axial and heat sums:

    beta_(r,j,m;alpha,beta)
      =sum_(d in Z^3) tr[B_(r,j,m)(d) q_(alpha,beta)(-d)],

    K_(i,V)=sum_(k,l)c_(i;kl)
      sum_(r,m,alpha,beta) sum_(j in Z)
        beta_(r,j,m;alpha,beta)
        integral_D (x_1+4) partial_m u_(rho(r))(x)
                    phi_(l,alpha)(x) phi_(k,beta)(x) dx. (3)

Here m=2,3,4; r, alpha and beta range over their original finite
lists. The symbol beta in the subscript is also a path label; the
left-hand beta denotes a scalar tensor entry. Then, for both probes,

    a^3 V_N -> K_(i,V),
    a^3 Delta_V -> K_(i,V).                             (4)

The existence of this particular signed coefficient is the result.
Its value and sign are not determined. This is not a limit theorem
for transverse H or the complete other/other contribution. L110's
exterior-circulation remainder and L113/L115's scalar/energy placement
errors remain; the other functionals remain unevaluated. The group's
outside factor 3 is not applied in (3). No joint compensation against
-12 gamma D_i, finer-scale bound, logarithm, interacting reflected
error <=c_box/2, continuum construction, reflection positivity,
infrared control or finite positive mass follows.

## Proof

### 1. Control the full heat sum uniformly before taking local limits

The exact exterior expansion and stored normalization are those of
L088(4)--(5), L111(13) and L113(14). Choose one enlarged fixed
polynomial p covering those bounds. Thus

    ||F_k(t)||<=C a p(k),
    ||Z_(kl;st)||_HS<=C a^2 p(k)p(l) N^(3/2).           (5)

L080(4)--(6) applies to these same square-root covariance columns:
the ordinary relative mode is a^2 f_k, and its covariance
square-root column is a A_(k,a), with the physical eigenvalue
lambda_(k,a). Its finite probe form has uniformly bounded operator
norm and converges at every fixed pair to B_i. Consequently

    |c_(i;kl,a)|<=C_i exp[-(tau/16)(|k|^2+|l|^2)],
    c_(i;kl,a) -> c_(i;kl) at every fixed pair.         (6)

The component is part of each mode label. All omitted mesh labels
are extended by zero when using a common infinite label set. The
Gaussian bound in (6), multiplied by p(k)p(l), is summable. Write
H_i(K) for its sum over pairs for which at least one label has
|k|>K or |l|>K. Then H_i(K)->0.

L119(5), its rowwise compression bound (16), and (5) yield, for the
part of V_N restricted to any set of exterior pairs,

    a^3 |V_N[set]| <= C sum_(k,l in set)
                     |c_(i;kl,a)|p(k)p(l)
                        sum_(r,j,m)||B_(r,j,m)||_2.    (7)

For the level count, for each fixed j=t-s the sum of min(s,t) over
admissible t is at most N^2. The trace norm bound before this count
is C a^2 N^3 p(k)p(l)||B_(r,j,m)||_2. Multiplying by a^3 after
the count gives a^5 N^5=8^5, a fixed constant. This proves (7)
without dropping either original level. The same estimate holds
for all spatial and axial truncations in L119, since truncation
does not increase an ell^2 kernel norm. Equations (6)--(7) therefore
remove the exterior heat tail uniformly, with error at most C H_i(K).
This is stronger than a mere bound on the entire heat sum.

### 2. Compare the finite projection on the truncated derivative trace

Fix J0 and R, and truncate exactly as in L119(6). Denote a truncated
kernel by B_j^R; it has spatial support |d|<=R. The multiplier
v_(r,t,m) is supported in a common fixed physical interior set,
since u is globally smooth and compactly supported. Hence

    W_(t,j)=J^* M_(v_(r,t,m)) B_j^R J

has both output and input plaquette indices in that set enlarged
by R lattice sites. For sufficiently fine meshes the enlargement
and each path stencil are separated by delta N from every
transverse face, for some delta>0 independent of N and of the
exterior labels. The zero derivative collars in the axial direction
also remain. This support fact uses the finite spatial truncation;
it is not asserted for the untruncated kernel.

Replace P by P_bulk=J_1^* P_inf J_1 only in Z. Cyclicity gives the
error of one unweighted trace as

    Tr[F_k(t) W_(t,j) F_l(s)^T (P-P_bulk)].            (8)

There is an interior edge selector R_Omega for which
F_k W F_l^T=F_k W F_l^T R_Omega: each input edge lies within the
fixed path range of an input plaquette of W. L114(2) therefore
applies to the output rows of the projection difference in (8),
and retains all its input rows, including every boundary edge.
Rowwise kernel counting and (5) give

    ||F_k W F_l^T||_HS
               <= C a^2 p(k)p(l) N^(3/2)||B_j^R||_2.

Trace Cauchy--Schwarz and L114(2) bound (8) by this quantity times
C_delta (log N)^(3/4). Restoring min(s,t), summing the levels for
each j and then the heat labels bounds the entire truncated
projection error by

    C_i a^2 N^(7/2) (log N)^(3/4)
                      sum_(r,m,|j|<=J0)||B_(r,j,m)^R||_2
             = O_(J0,R)(N^(3/2)(log N)^(3/4))=o(N^3). (9)

There is no outside a^-1 in V_N. All scalar multipliers and path
filters retain their sides of P; no projection commutator or small
projection operator norm is used. The support statement in (8)
restricts projection output rows and says nothing about compact
output of the projection itself.

### 3. Identify the exact local kernel after this comparison

L113's proof section 3 gives the exact finite identity

    F_k(t)=a sum_alpha S_alpha M_(phi_(k,alpha,t)).     (10)

In a trace with W_(t,j), both plaquette arguments x,y are compact
interior and |x-y|<=R. Every edge in the finite S columns adjacent
to x or y is therefore present, with its unchanged stencil value.
For these entries the compressed full-grid projection product is
exactly (1), since its two adjacent S columns have no missing rows.
Writing d=x-y, the compared trace is consequently exactly

    a^2 sum_(alpha,beta,x,d) v_(r,t,m)(x)
       phi_(l,alpha,s)(x-d) phi_(k,beta,t)(x)
       tr[B_(r,j,m)^R(d) q_(alpha,beta)(-d)].          (11)

The scalar in each M_phi multiplies all plaquette components at
its lower-vertex index. S_alpha already selects its plane, so the
scalar expression in (11) retains every component selector. The
matrix entry order is B(x,y)Q(y,x), explaining the argument -d.
No continuum replacement or equal-level identity has been used
to obtain (11).

### 4. Prove the fixed-offset spatial and axial Riemann limit

Fix exterior labels k,l and the finitely many r,m,alpha,beta,j,d
in (11). Set s=t-j. On the derivative support, both levels are
interior for sufficiently fine meshes. L028(9)--(11) gives, at
each transverse edge in the actual forest exterior column,

    (v_k)_mu/a=A_(k,a,mu)
      -a sum_(ell=0)^(t-1) delta_(mu,a)
                          A_(k,a,1)(ell+1/2,.).       (12)

Here the axial and transverse arguments have their prescribed
staggered locations and the origin -4; delta_(mu,a) is the
physical forward difference between the two endpoints of that
edge. L080(5),(8)--(10) evaluates the prefix using the exact cosine
sum, including the constant axial mode. For each fixed mode its
smooth expression and all needed transverse derivatives converge
uniformly on interior compact sets to Phi_k and its derivatives.
The forward difference in (12), as opposed to the endpoint average
in L080(9), has the same fixed-mode limit by the integral difference
formula and uniform convergence of these derivatives. Direct edge
samples also converge there. Thus (v_k)_mu/a -> V_(k,mu) uniformly
on that support. This checks applicability to the actual two-edge
paths, rather than assigning them an averaged value at finite mesh.

The signed b traversal has limiting value V_mu+V_nu; the signed q
traversal has limiting value -V_mu+V_nu, by L088(11)--(12)'s exact
path signs. Hence the phi in (10)--(11) converge to (2). Their
clamped extensions do not enter: all indices in (11) are existing
interior rows. For fixed j,d, the arguments of the l column differ
from (-4+at, -4+ax) by (-aj,-ad), which tends to zero. Uniform
fixed-mode convergence and continuity therefore give

    phi_(l,alpha,t-j)(x-d) phi_(k,beta,t)(x)
       -> phi_(l,alpha)(xi_t,xi_x) phi_(k,beta)(xi_t,xi_x)

uniformly on the common compact derivative support. The physical
levels coincide only in this justified limit. The finite-level
weight is still exact:

    a min(t-j,t)=at-a max(j,0) -> x_1+4.               (13)

Combining the a^3 normalization with the a^2 in (11) gives
a^5 min(s,t)=a^4 [a min(s,t)]. Thus the complete t,x sum is a
four-dimensional a^4 Riemann sum. Its integrand converges uniformly
to the continuous compactly supported product appearing in (3).
The ordinary Riemann-sum theorem, (6), and the finite j,d sums now
give the limit (3) with beta replaced by its |d|<=R sum and the
axial sum restricted to |j|<=J0, at any fixed exterior cutoff.
There is no extra factor of 8. Neither the upper pin nor the
physical prefix or constant mode has been replaced.

### 5. Remove every tail and prove absolute convergence

The full-grid operator P_inf is an orthogonal projection of norm
one. Since both S stencils have bounded symbols, (1) has a bounded
matrix Fourier symbol on the finite-measure torus. Plancherel
therefore gives ||q_(alpha,beta)||_(ell^2,F)<=C for each of the
finitely many path pairs. Its entries are real, since the original
stencils and the real convolution projection preserve real arrays.
For each j, spatial Cauchy--Schwarz yields

    sum_d |tr[B_(r,j,m)(d) q_(alpha,beta)(-d)]|
        <= ||B_(r,j,m)||_2 ||q_(alpha,beta)||_2.        (14)

L119(5) makes the right side summable in j. Replacing B by its
omitted spatial or axial part in (14) shows that the tensor-tail
error is at most C Theta(J0,R), with Theta as in L119(6).

The continuum phi have polynomial bounds C p(k) on the common
compact support, by the mode and length-8 prefix estimates in
L028/L080 (or directly from (2)); displacement derivatives are
bounded. Thus the absolute value of each integral in (3) is at
most C p(k)p(l). The continuum version of (6) is summable with
these factors. Equation (14) proves absolute convergence of the
entire functional, including all j,d and heat labels, and bounds
its omitted heat tail by C H_i(K) and kernel tails by
C_i Theta(J0,R).

For the original finite traces, (7) controls the same heat tail
uniformly, and L119(6) controls the kernel tails uniformly at
cubic scale. Given any positive tolerance, first choose a finite
exterior cutoff K, then a sufficiently large J0 and then R so
both finite and continuum tails are below that tolerance. With
these parameters fixed, (9)--(13) identify the mesh limit of the
remaining finite sums. Letting the tolerance tend to zero proves
the first limit in (4). L119(4)'s o(N^3) error proves the second.
This explicit cutoff order uses no mesh-dependent fixed-parameter
theorem and no uncontrolled interchange of limits.

### 6. Scope and known-trap check

This is a standard-method REPRODUCTION specialization under the
unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction, displacement derivative reduction, heat
majorants and projection comparison are imported. The specialization
is needed because the previous results left V_N's local trace limit
unproved. No general Ward/flow theorem assigns this isolated error,
and no novelty claim beyond the checked sources is made.

The argument uses neither separate absolute first moments refuted
in L109 nor second quadratic moments. The middle projection is
replaced only after kernel truncation supplies compact adjacent
rows, with the complete projection input retained in (9). Fixed
offsets do not give a finite-mesh equal-level identity. The forest
prefix is not extended through the upper pinned potential, and
the earlier cubic placement errors remain distinct. The exact
vanishing full-grid comparison in L118 does not set K_(i,V) to zero.
This unevaluated limit is one local mathematical input, not a
complete compensation, interacting bound or Yang--Mills candidate.

## Mathlib

Full matching generator-displacement error limit: **not checked**.
Supporting Fourier Plancherel, Hilbert--Schmidt trace inequalities,
Riemann-sum convergence and dominated-convergence coverage: **not
checked**. Unknown availability is not absence. No numerical
certificate, finite-mesh sign or source-based finiteness shortcut
is used.
