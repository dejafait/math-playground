# L245 — Quantitative comparison of the frozen reverse coefficient

## Hypotheses

Keep L107's relative SU(2) cube D=(-4,4)^4, lower-rooted direction-1
forest, admitted even N, a=8/N, tau=1/16 and actual probes i=3,6.
Use exactly its continuum heat coefficients c_(i;kl), exterior modes
v_k, raw path symbols z_k, incidence tau, circulation c, and filtered
generator symbol w. The matrix c(theta) is distinct from c_(i;kl).
All continuum exterior labels, including allowed constant component
indices, are retained. There is no outside factor 3.

This lemma concerns an explicitly defined frozen comparison expression.
It does **not** identify that expression with L244's ordered bulk trace.
In particular its use of continuum coefficients at a common point is a
definition, not an estimate of the original two-level coefficient error.

For theta in [-pi,pi]^3 put lambda=sum_mu |1-exp(i theta_mu)|^2.
For lambda>0 let p=tau tau*/lambda, q0=I-p and

    q_delta=I-tau tau*/(lambda+delta),  0<delta<=1;
    q_0=q0.

For 0<epsilon,h<=1 and 0<=delta<=1 define the reduced numerator

    J_(kl,delta)(x,theta)
      =tr[c* z_k tau w* q_delta z_l* c
                                      -c* z_k tau w* c* z_l].       (1)

These are precisely the two ordered products of L242(3) with all
coefficients frozen at x and the scalar covariance and middle inverse
removed. No factor is commuted in (1). In particular q_delta occurs
only once, in the first product. Set integrands at lambda=0 to zero.
Let r_d(mu) be the d-th axial kernel coefficient of (L_Z+mu)^-1.
With n=N-1, x_(t,j)=(-4+at,-4+aj_2,-4+aj_3,-4+aj_4) and
S_st=1_(t<s)+delta_st/2, define

    F_(i,N;epsilon,h,delta)
      =a sum_(t=1)^n sum_(j in {1,...,n}^3) sum_(k,l)c_(i;kl)
          integral sum_(s=1)^n S_st r_(s-t)(lambda+epsilon)
                  J_(kl,delta)(x_(t,j),theta)/(lambda+h)
                                                   dtheta/(2pi)^3. (2)

Thus (2) retains the original finite axial ranges and diagonal half.
Its coefficients are the full continuum heat series, not the finite-mesh
c_(i;kl,a). Their eventual comparison is not assumed here.

## Conclusion

There are constants C_i,c>0, independent of the three masses and N,
such that

    |F_(i,N;epsilon,h,delta)-a^-3 K_(i,R)|
       <=C_i {N^2+N^3[epsilon+h+delta
                                      +exp(-c N sqrt(epsilon))]},  (3)

where K_(i,R) is exactly L107(2). Consequently, at

    epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3),

the error in (3) is O_i(N^(7/3)), below the registered
O(N^(5/2)log(eN)^2) budget. This controls the frozen expression's
weighted axial sum, inverse/projection mass removal and spatial
quadrature, with the complete heat sum. It does not control

    B_i^b(N^-1,N^(-4/3),N^(-2/3))
                              -F_(i,N;N^-1,N^(-4/3),N^(-2/3)).    (4)

Together with the imported L244 comparison, a bound on (4) at the
registered scale would complete this component remainder. That bound
still needs ordered coefficient freezing and matching of the actual raw
samples and heat coefficients. No such estimate follows from (3).
The separate critical audit in proof section 5 accepts (3) relative
to the imported inputs. Other component rates, complete
quantitative L011 assembly, interacting reflection control, continuum
axioms, infrared removal and finite positive mass remain unresolved.

## Proof

### 1. Uniform symbol and physical derivative bounds

Import L107(1)'s full raw symbols and L104(1),(4),(5),(15)'s mode and
heat conventions. L080 specifies the relative product modes, their
normalization and the lower prefix, including the constant axial mode.
For a fixed polynomial p enlarged as necessary,

    ||z_k||+||partial_x z_k||<=C p(k),
    ||c||<=C sqrt(lambda), ||tau||=sqrt(lambda),
    ||w||+||partial_x w||<=C sqrt(lambda),
    sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i.                    (5)

Here partial_x denotes each of the four physical first derivatives.
To check the derivative qualification, each relative sine/cosine
derivative costs at most a fixed power of |k|, while the physical
prefix is an integral over length at most 8; its axial derivative is
the integrand. The normalization 1/sqrt(nu_k) has a fixed lower spectral
gap because every relative one-form mode has three positive indices.
The constant axial index retains its linear prefix. The finite path
symbols have bounded coefficients. The symbol w is linear in the
fixed smooth compact displacement u_1 and contains sin(theta_mu),
whose modulus is at most |1-exp(i theta_mu)|. This proves (5) from
the imported formulas, without differentiating any rough kernel.

All q_delta are contractions. Since the matrices in (1) have fixed
dimension three, (5) gives

    |J_(kl,delta)|+|partial_x J_(kl,delta)|
                                     <=C p(k)p(l)lambda^2.         (6)

The two circulations and tau,w each supply one sqrt(lambda).
Also J is zero wherever u_1 is zero. Its physical support therefore
has fixed clearance from every face, uniformly in k,l and the masses.

Define the local density

    f_(i;epsilon,h,delta)(x)
       =(1/2)sum_(k,l)c_(i;kl) integral
          J_(kl,delta)(x,theta)/[(lambda+epsilon)(lambda+h)]
                                                   dtheta/(2pi)^3. (7)

Equations (5)--(6) imply a mass-independent C^1 bound for f and its
compact support, since lambda^2/[(lambda+epsilon)(lambda+h)]<=1.
They justify all spatial derivatives and heat summations in (7)
by an absolutely summable majorant. They also justify (2): the
nonnegative axial coefficients have total sum 1/(lambda+epsilon),
as verified next. No sign of the actual heat coefficients is required.

### 2. The finite triangular axial sum and its endpoint deficit

Import the scalar nearest-neighbor resolvent from J. S. Dowker,
[Heat-kernels on the discrete circle and interval](https://arxiv.org/pdf/1207.2096v2),
v2 (31 August 2012), sections 2 and 10, (3),(5),(42)--(48).
Its mass 4 sinh^2(gamma) equals mu below when kappa=2 gamma.
For mu>0 let kappa>0 satisfy cosh(kappa)=1+mu/2 and set q=exp(-kappa).
In this convention the exact whole-line axial resolvent coefficient is

    r_d(mu)=q^|d|/(2sinh(kappa)).                         (8)

The following substitution checks the operator and source normalization
needed here, rather than reproving a general kernel theorem.
Indeed (2+mu)r_d-r_(d-1)-r_(d+1)=0 for d unequal 0, while at zero
the left side is 1. The sequence is summable, and convolution with it
is the bounded inverse, either by this identity and the Fourier
transform or uniqueness of the positive-mass inverse. Thus

    sum_(d in Z)r_d(mu)=1/mu,
    r_0(mu)/2+sum_(d>=1)r_d(mu)=1/(2mu).                (9)

The second identity uses the exact evenness in d; it retains the
diagonal half. For fixed t, the finite sum in (2) is the left side of
(9) minus the tail starting at L=n-t+1. The lower end produces no
additional deficit because S_st=0 for s<t. Direct geometric summation
using mu=(1-q)^2/q gives

    sum_(d>=L)r_d(mu)=q^L/[mu(1+q)]<=exp(-kappa L)/mu.  (10)

Whenever J(x_(t,j),theta) is nonzero, compact support implies L>=c_0 N
for a fixed c_0>0 and sufficiently large N. Here mu=lambda+epsilon
lies in (0,13]. The function arcosh(1+mu/2)/sqrt(mu) extends
continuously with value 1 at zero and is positive on [0,13], so
kappa>=c_1 sqrt(mu)>=c_1 sqrt(epsilon).

Combine (6),(10) with lambda^2/[(lambda+h)(lambda+epsilon)]<=1.
After the complete heat sum the error per spatial cell in replacing
the finite axial sum by 1/[2(lambda+epsilon)] is at most
C_i exp(-c N sqrt(epsilon)). There are at most N^4 cells in (2),
and its prefactor is a. Consequently

    |F_(i,N;epsilon,h,delta)
                   -a sum_(t,j)f_(i;epsilon,h,delta)(x_(t,j))|
                          <=C_i N^3 exp(-c N sqrt(epsilon)).      (11)

This is a uniform finite estimate before the mass schedule is chosen.
It neither extends the original variable-coefficient trace nor
identifies its two coefficient levels. Only the defined frozen
comparison has received the exact scalar half-sum.

### 3. Quantitative removal of all three symbol masses

For lambda>0,

    q_delta-q0=[delta/(lambda+delta)]p,
    |J_(kl,delta)-J_(kl,0)|
           <=C p(k)p(l)lambda^2 delta/(lambda+delta).    (12)

Only the first ordered term changes. The scalar inverse comparison is

    0<=1-lambda^2/[(lambda+epsilon)(lambda+h)]
       <=epsilon/(lambda+epsilon)+h/(lambda+h)
       <=(epsilon+h)/lambda.                            (13)

Using (6),(12),(13), first change q_delta and then the two scalar
denominators in (7). The absolute integrand error for a fixed pair
is bounded by C p(k)p(l)(epsilon+h+delta)/lambda. This majorant is
integrable: for |theta_mu|<=pi,

    lambda=4 sum_mu sin^2(theta_mu/2)
                                  >=(4/pi^2)|theta|^2,

and |theta|^-2 is locally integrable in three dimensions. The cube
is bounded, so its full integral is finite. No separate first absolute
kernel moment is invoked. If f_(i;0,0,0) denotes the corresponding
unregularized density, this proves uniformly in x

    |f_(i;epsilon,h,delta)(x)-f_(i;0,0,0)(x)|
                                      <=C_i(epsilon+h+delta).     (14)

To identify the subtraction exactly, put omega_k=z_k* c-c* z_k,
alpha_k=p omega_k q0 and beta_l=q0 omega_l q0 as in L107(1).
The identities c tau=0, q0 c*=c*, p tau=tau give

    alpha_k*=c* z_k p,
    beta_l=q0 z_l* c-c* z_l q0.

Hence, by ordinary finite-dimensional cyclicity,

    tr[q0 alpha_k* tau w* beta_l]
      =tr[c* z_k tau w* q0 z_l* c-c* z_k tau w* c* z_l]
      =J_(kl,0).                                        (15)

The final q0 in the second term is removed only by cyclicity next to
c*. No positive-mass matrix is treated as idempotent. Thus the
integral over D of f_(i;0,0,0) is exactly K_(i,R) in L107(2),
with the same coefficient, sign, half-factor and full mode series.
Equation (14) implies an O_i(epsilon+h+delta) error for its integral.

### 4. Spatial quadrature and the complete count

The uniform physical first derivative bound after (7) implies

    |a^4 sum_(t,j)f_(i;epsilon,h,delta)(x_(t,j))
                     -integral_D f_(i;epsilon,h,delta)(x)dx|
                                                              <=C_i a. (16)

For example partition D into the N^4 cubes of side a and compare each
integral to the value at its lower corner using the mean value bound.
The discrepancy per cell is at most C_i a^5, and their sum at most
C_i a. Compact support makes every excluded face row zero for small
a, so that this full partition has precisely the sum in (16).
The same argument applies to the complex densities; reality also
follows from conjugation under theta -> -theta of the real stencils.

Multiply (16) and the integrated (14) by a^-3, then combine with (11).
Since a^-2=O(N^2) and a^-3=O(N^3), this proves (3). At the displayed
schedule the largest mass is delta=N^(-2/3), and
N^3 exp(-c sqrt(N)) is smaller than N^2 for sufficiently large N.
The result is O(N^(7/3)). Every estimate precedes the schedule.

This is a quantitative specialization of L107's already established
frozen coefficient, using elementary Fourier and integral bounds,
classified REPRODUCTION under the saved reverse-remainder EXPLORE
assessment. Its new content is the rate and the finite axial deficit,
not a new construction theorem or progress beyond the methods checked.
The separate ordered error (4) remains unproved: neither the use of
continuum coefficients nor the equality of both frozen physical levels
is assigned to the actual trace without an additional estimate.

### 5. Separate critical audit, 2026-10-20

**Verdict: (3) and its O(N^(7/3)) specialization are accepted relative
to L080, L104, L107 and L242.** This verifies the frozen comparison
only. It does not audit the inverse/projection or finite-to-bulk
estimates, or use L246--L248 to certify an upstream premise. The audit
uses the previously saved SPECIALIZE assessment and the inspected
Dowker source coverage recorded there. No new bound is claimed.

For the algebra, regard c,z as maps from the three edge components to
the three plane components, tau as a vertex-to-edge column and w as
a column on edge components. Each word in (1) is an edge endomorphism.
The displayed c rows give c tau=0 exactly. Therefore p c*=0,
q0 c*=c*, c p=0 and c q0=c. In particular

    alpha_k=p z_k* c,
    alpha_k*=c* z_k p,
    beta_l=q0 z_l* c-c* z_l q0.

Insert these into L107(2), remove p only against tau, and remove the
leading q0 only against c*. The second word still ends in q0; moving
that last q0 cyclically against its first c* gives precisely (15).
This checks both signs and conjugates without interchanging k,l or
changing the heat coefficients. The positive-mass word has exactly
one q_delta and is a different expression from L107(11)'s unreduced
all-projection regularization. No equality of those approximants is
needed. Each of the two words has two circulation factors (c*,c in
the first and c*,c* in the second), tau and w, giving lambda^2.

For complete heat normalization, the imported continuum coefficient is
exp[-tau(nu_k+nu_l)] (B_i)_(kl), with A_k=f_k/sqrt(nu_k) and
nu_k=(pi/8)^2 |k|^2. The bounded actual B_i forms include both probe
polarizations. There are three strictly positive indices per relative
one-form label; its remaining component index may be zero. For every
fixed derivative order r, the explicit product modes give
||partial^r A_k||_infinity <= C_r(1+|k|)^r. Differentiating the
length-8 prefix transversely or at its upper integration endpoint
therefore bounds v_k and its four first derivatives by one fixed
polynomial p(k). In particular the zero axial component-1 index has
prefix (x_1+4) times its transverse mode, not zero. The products
p(k)p(l) exp[-tau(nu_k+nu_l)] are summable over all eight integer
indices and the two component labels. This proves the majorant
needed in (5)--(7), for either probe, without discarding any labels
or introducing an additional inverse eigenvalue or color factor.

For the finite axial count, (8) is the whole-line kernel by definition
in (2), not the relative finite-interval inverse. With n=N-1 the
omitted offsets are d>=n-t+1=N-t. The finite sum equals

    1/(2mu) - q^(N-t)/(mu(1+q)).

There is no lower tail because all s<t have zero selector. On the
support of u_1 the exponent's length is at least c_0 N. The positive
minimum of arcosh(1+mu/2)/sqrt(mu) on 0<=mu<=13 proves the uniform
exponential bound, including arbitrarily small epsilon. Multiplying
by the complete numerator and middle inverse leaves a bounded
lambda^2/[(lambda+epsilon)(lambda+h)] factor. Thus the actual count
is a n^4 <=8 N^3, exactly as in (11), rather than a second free axial
sum. The original half is present before any limit or mass choice.

For simultaneous mass removal, telescope only the one q_delta and
then the two scalar inverses. Their pointwise errors are bounded by
C p(k)p(l) times delta/lambda and (epsilon+h)/lambda respectively.
The integral of lambda^-1 over the entire three-dimensional torus is
finite by the displayed lower bound for lambda. This proves a common
constant for all 0<epsilon,h,delta<=1, without an ordering of masses.
The same lambda^2 numerator bound after a physical derivative gives
the uniform C^1 density bound. Physical derivatives do not act on
the frequency masses or projections.

Finally use the N^4 cells with lower indices 0,...,N-1. Every omitted
zero-index face row vanishes by the fixed compact support; the upper
face is not a lower-corner row. The cellwise mean value error sums to
C_i a, and a times the sampled sum is a^-3 times its a^4 Riemann sum.
Thus quadrature costs O(N^2), the three masses cost respectively
O(N^2), O(N^(5/3)), O(N^(7/3)) at the stated schedule, and the endpoint
cost is O(N^3 exp(-c sqrt(N))). Their sum is O(N^(7/3)), strictly
within O(N^(5/2)log(eN)^2). The subtracted coefficient is exactly
L107(2), including its single half and no outside 3.

No unsupported step was found in this restricted proof. The assessment
of full matching and supporting Mathlib coverage remains not checked.
This local audit supplies neither an actual bulk-to-frozen comparison
nor a quantitative full L011 remainder or an interacting construction.

## Mathlib

Full matching frozen reverse-coefficient rate: **not checked**.
Supporting Fourier resolvent, geometric-series, integrability,
finite-dimensional trace and quadrature coverage: **not checked**.
Unknown coverage is not evidence of absence. The imported symbols,
normalizations and heat envelope are specified by L080, L104, L107
and L242; no external Ward/flow theorem is used for an isolated trace.
