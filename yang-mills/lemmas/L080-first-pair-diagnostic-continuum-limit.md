# L080 — The actual exterior diagnostic has a continuum limit

## Hypotheses

Keep L070(9)'s exact diagnostic D_(i,a), i=3,6, with L008's actual
two probes and displacement, SU(2), D=(-4,4)^4, a=8/N through
sufficiently fine admitted even meshes, and tau=1/16. Retain the
relative fixed-link Hodge covariance, all exterior modes, the
lower-rooted direction-1 forest with separately pinned upper vertices,
averaged positive upper curvature rows, averaged transverse lifted
links, normal end edges, u_(a,1), and the physical level weight sa.
Take the small-coupling coefficient at fixed mesh before refinement.

Use L008's real orthonormal continuum relative one-form modes

    f_k(x)=e_alpha e_(k_alpha)(x_alpha)
                         product_(j unequal alpha) v_(k_j)(x_j),
    e_0=1/sqrt(8), e_n(x)=cos(n pi(x+4)/8)/2,
    v_n(x)=sin(n pi(x+4)/8)/2,
    k_alpha>=0, k_j>=1 for j unequal alpha,
    lambda_k=(pi/8)^2 |k|^2.

The label k includes alpha in {1,2,3,4}; repeated labels below are
summed over this complete set. Let A_k=f_k/sqrt(lambda_k). Let
B_i=d Delta_1^(-1/2) pulled back through L008's curvature form:
precisely B_i=R^* M_i R, R=d Delta_1^(-1/2), with M_i exactly
L008(6),(8), including the actual full displacement. Thus

    (B_i)_(kl)=q_i(A_k,A_l),

where q_i(A,Z) is the symmetric polarization of L008(1), so that
q_i(A,A)=q_i(A). Define, for y=(x_2,x_3,x_4) and mu=2,3,4,

    U_(k,mu)(y)=(d A_k)_(1,mu)(4,y),
    Phi_k(x)=integral_(-4)^(x_1) A_(k,1)(h,y) dh,
    V_(k,mu)(x)=A_(k,mu)(x)-partial_mu Phi_k(x),
    P_(kl)=integral_D (x_1+4) u_1(x)
                        sum_mu U_(k,mu)(y) V_(l,mu)(x) dx.     (1)

These are smooth mode functions and boundary evaluations, not traces
of an unflowed random distribution. No boundary value for Phi at x_1=4
is imposed in (1); V is used only on the compact support of u_1.

## Conclusion

The following real series is absolutely convergent, and for both probes

    D_i=sum_(k,l) exp[-tau(lambda_k+lambda_l)]
                                      (B_i)_(kl) P_(kl),
    D_(i,a) -> D_i.                                           (2)

The full-probe value in (2) equals the value obtained by using only
the Psi_13/31 sector in B_i. The actual diagnostic weight u_1 and
all relative modes and prefixes remain unchanged in that equality.

Consequently, for the selected centered circulation/path trace of L079,

    a^3 F_(i,N)^circ -> 2 gamma D_i,                          (3)

where gamma>0 is L070(3)'s full torus constant. A nonzero D_i would
fix this selected a^-3 coefficient. This lemma does not evaluate D_i
or prove either sign or nonvanishing. L073's N=24 signs are not used.
Even D_i=0 would give only o(N^3), not an O(N^2) bound. No rate for
L079's error, a^2-scaled coefficient, complete response logarithm,
finite matching or interacting reflected-error bound <=c_box/2 follows.
This is a local REPRODUCTION under the saved SPECIALIZE assessment,
not progress beyond the sources checked or a Yang–Mills candidate.

## Proof

### 1. Match ordinary columns to physical modes

Put lambda_(k,a)=sum_j [2 sin(pi k_j/(2N))/a]^2. L008(15) gives

    |k|^2/16 <= lambda_(k,a) <= pi^2 |k|^2/64,
    lambda_(k,a) -> lambda_k                                 (4)

for each fixed allowed label. The finite allowed indices are all
bounded by N-1. Every label has three positive vertex indices, so
(4) has a mesh-uniform positive gap. There is no all-zero mode.

By L026(6), an ordinary normalized one-dimensional discrete mode is
sqrt(a) times its continuum mode sampled at the vertex or edge center.
This also holds for the constant edge mode: 1/sqrt(N)=sqrt(a)/sqrt(8).
Thus the four-dimensional ordinary vector e_(k,a) has entries
a^2 f_k at its component's staggered grid. The ordinary covariance
Sigma is the inverse of the unscaled Hodge Laplacian, whose eigenvalue
is a^2 lambda_(k,a). Its square-root column is exactly

    z_(k,a)=Sigma^(1/2)e_(k,a)=a A_(k,a),
    A_(k,a)(x)=f_k(x)/sqrt(lambda_(k,a))                       (5)

sampled on that same grid. We use the smooth expression on the right
as an extension of the samples, not as a change of boundary conditions.
Tangential fixed links are its zero sine values at their boundary vertices.

L070's coefficients are, exactly,

    c_(i;kl,a)=exp[-tau(lambda_(k,a)+lambda_(l,a))]
                                               (B_(i,a))_(kl). (6)

Indeed its ordinary whitened form has entry z_(k,a)^T Q_i z_(l,a)
=q_(i,a)(A_(k,a),A_(l,a)), which is L008's B_(i,a) in the physical
orthonormal mode embedding. This checks both square-root factors and
the stored/physical conversion; no color factor or gamma enters D.
Reuse L008's sections 1 and 4: sup_a ||B_(i,a)||<=C_i and
(B_(i,a))_(kl)->(B_i)_(kl) at every fixed pair. That existing proof
retains the average of squares in the triplet, clover polarization in
the shear, and central-difference strains. No new operator matching
or perturbative flow-finiteness theorem is assumed here.

### 2. The upper row converges with its positive orientation

Let U_(k,a,mu) be L070's averaged upper curvature of z_(k,a),
divided by a^2. The exact identity D_1 R_F z=D_1 z allows this row
to be computed from (5), including at the upper face. In positive
(1,mu) orientation it is the average of

    delta_(1,a) A_(k,a,mu)-delta_(mu,a) A_(k,a,1)

at the upper plaquette centers. If the component is mu, the upper
value A_(k,a,mu)(4,y)=0 is its true sine boundary value, and its
axial difference is [0-A_(k,a,mu)(4-a,y)]/a. If the component is 1,
the second term is the negative transverse difference of A_(k,a,1)
at the axial edge center 4-a/2. Both use the prescribed relative rows.
Finite differences of these smooth fixed modes and the transverse
adjacent-plaquette average converge uniformly for y on any compact
transverse interior set to

    U_(k,a,mu)(y) -> (partial_1 A_(k,mu)
                               -partial_mu A_(k,1))(4,y).     (7)

This checks the boundary sign without extending the interior forest
potential across its upper jump. The normal end edges are part of
the finite row; on the support needed below their samples are interior
for small a. No assertion about a random boundary trace is required.

### 3. Retain and pass to the exact lower-rooted prefix

At every interior axial level s, L026(2) and (5) give the actual
potential, at transverse vertices, as

    phi_(k,a)(s,y)=a sum_(ell=0)^(s-1)
                         A_(k,a,1)(-4+(ell+1/2)a,y).          (8)

The separately pinned potential at s=N is zero and is not used in
(8). It is also zero at every transverse boundary vertex: component-1
modes have sine factors in all transverse coordinates. For mu=2,3,4,
the exact endpoint-averaged transverse lift divided by a is therefore

    V_(k,a,mu)(s,y)=average_mu A_(k,a,mu)(x_1,.) at y
                                      -nabla^c_(mu,a) phi_(k,a)(s,y),
    x_1=-4+sa.                                               (9)

The central derivative in (9) results from averaging the two adjacent
oriented incidence differences. Its sign is minus because R_F z=z-D_0 phi.
This identity includes both normal end edges and zero transverse
boundary values. The direct term's average is across its edge centers.

Here (8) can be checked without a uniform axial inverse approximation.
On a component-1 mode write f_(k,1)(x)=e_n(x_1) F_k(y). For n>=1,
the exact cosine sum gives

    a sum_(ell=0)^(s-1) e_n(-4+(ell+1/2)a)
        = sin(n pi s/N)/(2 omega_(n,a)),
    omega_(n,a)=2 sin(n pi/(2N))/a.                          (10)

To verify the sum, sum the geometric progression of exp[i n pi(ell+1/2)/N]
and take its real part: the result is sin(n pi s/N)/[2 sin(n pi/(2N))].
Multiplication by a/2 gives (10). For n=0 the sum is exactly sa/sqrt(8).
Divide these formulas by sqrt(lambda_(k,a)) and multiply by F_k(y).
For each fixed n, omega_(n,a)->n pi/8. Thus (8), with any fixed
number of transverse derivatives, converges uniformly for all s<N
to Phi_k(-4+sa,y). If the mode's component is not 1, both potentials
are zero. In particular (9) converges uniformly on the coefficient
support to V_(k,mu) in (1), by the central-difference formula and
convergence of the direct endpoint average.

The constant axial mode and its entire physical distance have survived.
No value at s=N is substituted into the forest. Compact support of u
keeps (9) a fixed positive distance from that face; U in (7) was
computed by curvature invariance instead of this interior formula.
This does not reopen the stopped bulk-profile replacement.

### 4. Fixed-pair Riemann limits

Central differences of L008's fixed smooth Psi converge uniformly to
its derivatives, so u_(a,1)->u_1 with uniformly bounded values. For
small a their supports lie in a fixed compact subset of D. L070(9)
and (5),(7),(9) now give exactly, for each fixed pair,

    P_(kl,a)=a^4 sum_(s,y) (sa) u_(a,1)(s,y)
                        sum_mu U_(k,a,mu)(y)V_(l,a,mu)(s,y)
                 -> P_(kl).                                 (11)

All four sum coordinates are interior vertices; sa=x_1+4, not x_1.
The products converge uniformly on their fixed compact support to
the smooth integrand in (1). Their Riemann sums therefore converge
by the standard Riemann-sum theorem for continuous functions on a
compact rectangle. One may extend the products by zero outside the
coefficient support: u vanishes in a neighborhood of every face.
This retains every actual axial level and transverse row; it introduces
no boundary collar omission into the original weighted sum.

### 5. Control the full exterior sum before taking its limit

There is a constant C independent of a and of every retained label k
such that ||A_(k,a)||_infinity+||partial A_(k,a)||_infinity<=C.
The product sine/cosine amplitudes and their first derivatives are
bounded by C(1+|k|), whereas sqrt(lambda_(k,a))>=|k|/4 and
|k|>=sqrt(3). Consequently every physical first finite difference
is also bounded by C, by its integral difference formula. The upper
row in (7) and its endpoint average satisfy ||U_(k,a)||_infinity<=C.

For the prefix, differentiating (8) in a transverse coordinate gives
a sum of at most N terms, hence <=8 sup|partial_mu A_(k,a,1)|.
The smooth prefix extension has zero transverse boundary values,
so its central difference bound includes end rows. Equation (9) then
gives ||V_(k,a)||_infinity<=C. These are bounds on the exact retained
rows, not bounds on a generic forest operator. The identical continuum
bounds follow using lambda_k and the length-8 integral in (1).
Since sa<=8, u_a is uniformly bounded, and a^4 times the vertex
count is at most 8^4, we obtain

    |P_(kl,a)|+|P_(kl)|<=C                                  (12)

uniformly in both exterior labels. Thus (4),(6) and the B operator
bound give the complete majorant

    |c_(i;kl,a)P_(kl,a)|
        <=C_i exp[-(tau/16)(|k|^2+|l|^2)].                   (13)

For omitted mesh labels define the term to be zero. The right side
is summable over the four component choices and four integer indices
on each side: it is bounded by a constant times the product of eight
convergent Gaussian series. Its complement outside any fixed finite
exterior cutoff tends to zero uniformly in a. The continuum series
has the same majorant by its stronger eigenvalue bound. Equations
(6),(11) give convergence at each fixed pair. The dominated convergence
theorem for counting measure, equivalently this finite-cutoff/tail
argument, proves absolute convergence and (2) with the entire heat sum.
No preview, numerical truncation or interchange of uncontrolled limits
is used.

The same proof applies to each of the Psi_13 and Psi_24 form sectors,
whose coefficients and B bounds satisfy the same estimates. L071's
exact finite identity D_(i,a)^B=0 therefore passes to its continuum
limit, giving D_i^B=0 and D_i=D_i^A. This imports that existing
symmetry, without declaring the surviving sector zero or signed.

### 6. Transfer only the scale already controlled

L079(3) proves a^3 F_(i,N)^circ-2 gamma D_(i,a)->0 with the
actual pinned trace and all exterior modes retained. Combine it with
(2) to obtain (3). Its qualitative error is not improved by the
convergence proof here. The selected limit can be nonzero, zero or
unevaluated without resolving the O(N^2) question or the full logarithm.
The centered path/path term, L078's remainder, scaled exterior defect,
all nine mixed placements and other response jets remain necessary.
Overlapping quartic groups must still be compared by subtracting the
shared quartic once. Reflection positivity, interacting error <=c_box/2,
continuum field construction, infrared removal and finite positive mass
remain unproved.

## Mathlib

Coverage of this complete fixed-boundary, forest-lifted diagnostic limit:
not checked. Supporting Riemann-sum convergence and dominated convergence
are standard named theorems; no matching Mathlib declaration was inspected
in this step. The explicit relative modes and bounded forms are reused
from L008, not attributed to a general perturbative renormalization theorem.
