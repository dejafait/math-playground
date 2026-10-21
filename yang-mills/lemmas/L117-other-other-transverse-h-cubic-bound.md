# L117 — The complete transverse H trace is cubic-bounded

## Hypotheses

Use exactly L116's full-grid comparison R_inf and L099/L110's actual
R_H,tr for both L010 probes i=3,6, SU(2), straight lower-rooted
direction-1 forest, relative all-face fixed-link box (-4,4)^4,
sufficiently fine admitted even N, a=8/N and tau=1/16. Take the bare
small-coupling coefficient at fixed mesh before refinement. Coordinates
and norms are ordinary stored ones. Retain all interior axial levels,
transverse end rows, both generator orientations, every path/component
filter and the complete exterior heat sum.

Import L116(1),(4),(5), L113's S_alpha and phi_(k,alpha,s), and
L111/L115's A_r=D T_r C_r and b_(r,t). Import the actual transverse
exterior link columns z_k of L088 (these are its z_k=X v_k, not
L028's residual columns with a different local notation). At a
transverse lower-vertex index x in a fixed physical interior set put

    v_(k,s,mu)(x)=z_(k,mu)(s,x)/a,  mu=2,3,4.             (1)

Every edge in (1) and its fixed-range neighbors exists at sufficiently
fine mesh. The two vectors at s and t will remain independent.

## Conclusion

For both actual probes,

    |R_inf| <= C_i N^3,       |R_H,tr| <= C_i N^3.        (2)

Together with L095's exact split and its other two bounds this gives
|R_H|<=C_i N^3 for the complete H diagonal. In particular none of
these traces has a stronger-than-cubic power. This does not establish
an a^3-scaled limit, its value or sign, or vanishing of that limit.
The complete other/other limit and comparison with -12 gamma D_i
remain unresolved. Earlier cubic errors are retained, not discarded.
Other response jets, finer powers/logarithm, matching, interacting
error <=c_box/2, continuum axioms, reflection positivity, infrared
control and finite positive mass remain independent gaps.

## Proof

### 1. Compare finite path coefficients locally, with both levels kept

Import L028's smooth relative-mode representation and exact forest
prefix, as used in L090(6). Uniformly over levels 1<=s<N, on a
fixed transverse interior containing the displacement support and
every stencil neighbor, it gives an enlarged fixed polynomial p with

    |v_(k,s,mu)(x)| <= C p(k),
    |v_(k,s,mu)(x+h)-v_(k,s,mu)(x)| <= C a p(k)           (3)

for each of the finitely many required integer shifts h. For clarity,
the exterior column is a times the forest retraction of a smooth
relative mode divided by its physical eigenvalue's square root.
In the prefix formula L028(9), a transverse neighbor difference of
the retracted mode contains at most N second differences of its
component-1 mode. Each is O(a^2 p(k)); since Na=8, their sum is
O(a p(k)). Its direct transverse edge value has the same difference
bound. The relative spectral gap and sine/cosine mode derivative
bounds absorb the eigenvalue factor into p. This verifies (3) also
at level N-1; no edge at the upper pinned level N is sampled.
The bound on values follows from at most N first differences in
the same prefix. Only transverse interior edges are used here;
no extension across a pinned jump is asserted.

For a plane mu<nu the exact signed paths are b=y1+y2 and q=y2+y3,
with traversal signs as in L088(11). On a constant stored vector av,
their values divided by a are v_mu+v_nu and v_nu-v_mu respectively.
All actual samples differ from the corresponding component in (1)
by one of the fixed shifts of (3). Consequently, on that interior,

    phi_(k,(mu nu,b),s)(x)=v_(k,s,mu)(x)+v_(k,s,nu)(x)
                                         +O(a p(k)),
    phi_(k,(mu nu,q),s)(x)=v_(k,s,nu)(x)-v_(k,s,mu)(x)
                                         +O(a p(k)).    (4)

The clamped extensions in L113 agree with the original values there.
Apply (4) separately at s and t. Neither equal levels nor equal
vectors are required. The coefficient majorant from L088/L113 is

    sum_(k,l)|c_(i;kl,a)|p(k)p(l) <= C_i.                (5)

It remains valid after the fixed polynomial enlargement above.

### 2. Evaluate the fully frozen diagonal integral in the exact order

For real independent transverse vectors v,w and displacement u,
define constant path coefficients ell_(pi,b)(v)=v_mu+v_nu and
ell_(pi,q)(v)=v_nu-v_mu. Set

    F_v=sum_alpha ell_alpha(v) S_alpha^inf,
    H_u=sum_r u_(rho(r)) T_r C_r.                       (6)

The signs and repeated displacement choices in (6) are exactly those
in L111's generator decomposition; they are already in T_r,C_r.
The complete frozen version of L116(5)'s coefficient sum is therefore

    I_j(w,v,u)=integral tr[F_w^* P_inf F_v D H_u E_j]
                                                  dtheta/(2pi)^3. (7)

This is obtained by expansion of (6), with no filter crossing P_inf.
Use the component-center phases of L088(11)--(14). The change from
L116's lower-vertex phases conjugates this closed plaquette product
by its diagonal phase matrix, leaving its matrix trace unchanged.
For theta=(theta_2,theta_3,theta_4) put
d_mu=2 sin(theta_mu/2), eta_mu=cos(theta_mu/2) and
lambda=sum_mu d_mu^2. In plane mu<nu let

    z_pi=-d_nu e_mu^T+d_mu e_nu^T,
    r_pi(v)=-v_nu eta_nu e_mu^T+v_mu eta_mu e_nu^T.

The circulation row is i z_pi. L088(12), divided by a, gives the
exact path identity

    ell_(pi,b)(v) q_pi-ell_(pi,q)(v) b_pi
                             =2 r_pi(v)+v_mu i z_pi.    (8)

In particular all imaginary path terms are retained in (8).
F_v's pi column is the conjugate transpose of this row.
Since P_inf=d d^T/lambda and d dot z_pi=0, (8) implies

    (P_inf F_v)_pi=2 P_inf r_pi(v)^T.                   (9)

This is real and even under theta -> -theta. Thus F_w^* P_inf F_v
is real and even, for arbitrary independent w,v.

The complete frozen endpoint/clover map H_u is also real and even
in these phases. Explicitly, its pi=(mu,nu) column has just the
two entries

    (H_u)_(nu,pi)=u_mu eta_mu eta_nu^2,
    (H_u)_(mu,pi)=-u_nu eta_nu eta_mu^2.                (10)

Indeed multiplication by D's row i z_pi gives L099(8)'s diagonal
and cross-component generator entries, before its outside 1/a.
Equation (10) includes all the original component filters, rather
than replacing them by common filters. D is imaginary and odd.
Finally E_j=r_lambda(j) D D^* is real and even for every integer j,
with the same scalar r_lambda as L110. Hence the integrand in (7)
is purely imaginary and odd under simultaneous reversal of the
three transverse frequencies. Its integral is zero:

    I_j(w,v,u)=0 for all real w,v,u and all j in Z.     (11)

Integrability follows also from the bound in the next section.
The single point lambda=0 can be assigned arbitrary bounded
projection values and E_j=0; it has measure zero. No pointwise-zero
claim for the integrand is needed. Both exact real-trace generator
orientations remain in L099's already combined formula; (11) does
not change that normalization or assume an extra orientation factor.

### 3. Bound the actual local error and sum every offset and heat mode

The fixed stencils S_alpha,A_r have uniformly bounded symbols and
||P_inf||<=1. L110(7), with rho=sqrt(lambda), gives

    ||E_j(theta)||_F <= C rho exp(-|j|rho/2),
    (2/pi)|theta| <= rho <= |theta|.                    (12)

Thus radial integration on the containing ball in R^3 gives

    |kappa_(alpha,beta,r;j)|
      <= C integral ||E_j(theta)||_F dtheta/(2pi)^3
      <= C (1+|j|)^(-4) =: C B_j,
    sum_(j in Z) B_j < infinity.                       (13)

For |j|>=1 the radial integral is bounded by
C integral_0^infinity r^3 exp(-|j|r/pi) dr
=C' |j|^-4; j=0 is bounded on the compact torus. This uses the
full unregularized spectrum, not a low-mode approximation.

At each x in the union K_N of displacement supports, replace
phi_(l,alpha,s) and phi_(k,beta,t) in L116(4) by the corresponding
ell coefficients from (4). Use u=u_a(t,x), w=v_(l,s)(x), and
v=v_(k,t)(x) in (11). The complete replacement sums to zero at
this x for this pair s,t. The displacement coefficients b_(r,t)(x)
are exactly its u_(rho(r)) values. The bounded displacement, (3)--(4)
and (13), after summing the fixed finite lists r,alpha,beta, give

    |sum_(alpha,beta,r) kappa_(alpha,beta,r;t-s)
          b_(r,t)(x) phi_(l,alpha,s)(x) phi_(k,beta,t)(x)|
                       <= C a p(k)p(l) B_(t-s).        (14)

Outside K_N every b_(r,t) is zero, so no comparison there is needed.
There are at most C N^3 indices in K_N, all in the fixed physical
transverse interior. Keeping the original distinct levels gives

    sum_(s,t=1)^(N-1) min(s,t) B_(t-s)
                              <=N^2 sum_j B_j.         (15)

Insert (14)--(15) and (5) into the exact formula L116(4). Its
outside factor is a, so

    |R_inf| <= C_i a^2 N^5 =64 C_i N^3.                (16)

Absolute majorants in (5),(13)--(15) justify the whole heat and
level summation. No heat mode, offset, path or orientation has been
dropped. Crucially the O(a) local error is not claimed negligible
after cubic scaling; (16) only bounds it.

### 4. Return to the actual finite-box trace

L110's exterior-circulation remainder, L111's generator placement,
L113's scalar placement through finite P, and L115's energy placement
each cost O_i(N^3). L112 bounds the retained pinned correction by
O_i(N^(5/2) log N), L114's projection comparison by
O_i(N^(5/2)(log N)^(3/4)), and L116's final compression comparison
by o_i(N^3). Each of these latter errors is also bounded by C_i N^3
for sufficiently large N. Add these established bounds in their
original order to (16). This proves the second bound in (2).
No cubic error is deleted, and no estimate is transferred across
a component filter. L095(3)'s exact identity
R_H=R_H,ax+R_H,tr-R_H,Q and its two cubic bounds then prove the
asserted bound for the full H diagonal, with Q still subtracted.

This is local REPRODUCTION of the checked finite-path, Fourier parity
and spectral-bound methods under the unchanged EXPLORE assessment
drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
The finite contraction, exact filters and existing comparison estimates
are imported. The necessary extra specialization is the integrated
frozen diagonal for independent level vectors and its quantitative
local path-coefficient error; the earlier quartic-scale transfer did
not give this cubic bound. No claim of novelty beyond checked sources,
complete-group coefficient, or Yang--Mills solution is made.

## Mathlib

Full matching transverse-H cubic bound: **not checked**. Supporting
finite-stencil Fourier identities, parity of integrals, radial exponential
integrals and summable majorants: **not checked**. Unknown availability
is not absence. No numerical evidence or mathematical script is used.
