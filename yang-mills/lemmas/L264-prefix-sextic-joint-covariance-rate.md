# L264 — A joint prefix covariance count gives the quantitative sextic rate

## Hypotheses

Use precisely L194 and L202's relative SU(2) cube, sufficiently fine
admitted even N, a=8/N, lower-rooted direction-1 forest, stored full-link
coordinates and bare-first expansion. The probes are the actual i=3,6
forms at tau=1/16. All physical faces, variable normal end edges,
constant own-direction modes and complete external heat sums remain.
Every vertex potential is zero on every boundary vertex. Set

    S=P Delta^(-1) P, A=PAP, T=2SA, phi=Phi z,
    b=[z,q phi]/2-[D phi,q phi]/4,
    J_i=2<B_i z,b>, rho_H=script R_3-d script S_3[Tz].

Here z has three independent colors of covariance S, Phi is the actual
pinned lower prefix, D is the full vertex incidence, and
(q phi)_e=phi_tail+phi_head. The two fields within a color are correlated.
The complete residual includes both insertion subtractions; the action
and residual tensors, the original signed tilt and its order are those
of L194. No covariance source or action face is restricted.

Import L182/L186's positive comparison on interior vertices,

    0<=K=Phi S Phi^T<=Y=U tensor G,
    U_st=min(s,t), 1<=s,t<=n=N-1,
    G=Delta_T^(-1),                                  (1)

where Delta_T is the unscaled three-dimensional Dirichlet Laplacian.
Also import their full-spectrum estimates

    ||S||_HS<=C N^2 sqrt(log(eN)), ||K||_HS<=C N^4,
    Tr(G^2)<=C N^4, sum_(s,t) U_st^2<=C N^4.          (2)

These inputs include the constant axial edge mode and both axial ends.
Import L194/L202's complete modal expansion and derivative estimate,

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k e_l^T, n_k=S e_k,
    ||e_l||_infinity<=C a^2,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p),             (3)
    ||d rho_H[n_k^(c)]||_2<=C p(k)N^3 sqrt(log(eN)).  (4)

Equation (4) retains all three differentiated action placements and
uses no smoothness of Tz. All analytic premises and pending upstream
audit qualifications of these imported statements remain in force.

## Conclusion

For every deterministic full-link vector y and output color c,

    ||<y,b^c>||_2<=C ||y||_infinity N^(7/2).           (5)

In particular the full product modes satisfy

    ||<e_l,b^c>||_2<=C N^(3/2).                       (6)

Consequently, for both actual probes,

    |E[J_i rho_H]|<=C_i N^(5/2)sqrt(log(eN))
                  <=C_i N^(5/2)log(eN)^2.            (7)

The first bound is stronger than the approved budget. This is a local
specialization of the existing positive-prefix comparison and Gaussian
pairing/heat-kernel methods, with no claim of originality. Its joint
kernel estimate has passed the separate critical audit below. It supplies
no rate for the independent co-closed cubic response or transverse-H
remainder, no complete L011 remainder, no interacting reflected control,
and no continuum construction or infrared mass conclusion.

## Proof

### 1. Keep the two-color quadratic contraction before global norms

The standard input is Isserlis' theorem: H. Z. Munthe-Kaas, O. Verdier
and G. Vilmart, *A short proof of Isserlis' theorem*, author PDF dated
7 March 2025, Theorem 1, p. 1, and Theorem 4, p. 3
([primary PDF](https://www.unige.ch/~vilmart/paper_isserlis.pdf)).
The previously inspected theorem covers finite centered Gaussians
and covariance AA^T, hence singular S by a linear image. No reproof
is needed. For two distinct colors and a fixed coefficient matrix F,
its two-color specialization is exactly

    E[( (phi^d)^T F phi^f )^2]
        =vec(F)^T(K tensor K)vec(F), d!=f,            (8)

with a consistent choice of vectorization. Since

    Y tensor Y-K tensor K
       =(Y-K) tensor Y+K tensor (Y-K)>=0,

the same coefficient tensor has no larger second moment under K than
under Y. This applies to a signed coefficient matrix and requires no
entrywise covariance comparison. It changes neither prefix in the
actual sextic; it bounds only the norm of its retained quadratic test.

Each color of each bracket is a sum of two orders with distinct input
colors. Split further into the four link directions and apply the
triangle inequality over this fixed number of terms. For its
pure-prefix part the required scalar quadratic, in direction mu, is

    Q_mu=sum_(e parallel mu) y_e (D phi^d)_e(q phi^f)_e.

Apply (8) to its entire coefficient matrix before estimating rows.
Under Y the exact second moment is

    sum_(e,f parallel mu) y_e y_f
              (D_mu Y D_mu^T)_(e,f)(q_mu Y q_mu^T)_(e,f).
                                                               (9)

Both prefixes and their endpoints remain in this single product.
Taking absolute values in (9) is legitimate after the positive tensor
comparison; it makes no positivity assertion for the signed response.

### 2. Full transverse Dirichlet mixed-difference bounds

For transverse direction j and all transverse edges alpha,beta,
including normal end edges, put r=dist(alpha,beta) in lattice units.
The full pinned operators satisfy

    |(q_j G q_j^T)_(alpha,beta)|
                <=C[(1+r)^(-1)+N^(-1)],
    |(d_j G d_j^T)_(alpha,beta)|
                <=C[(1+r)^(-3)+N^(-3)].              (10)

Here boundary vertex values are zero before applying d_j or q_j.
We justify the dimension-three specialization of L200's boundary-
uniform image argument, since its dimension-four exponents alone
would not establish (10).

The infinite three-dimensional heat kernel is the Fourier integral
of exp(-t lambda(theta)), lambda=4 sum_j sin^2(theta_j/2).
For zero or two lattice differences (the latter at the two arguments),
Fourier differentiation and integration by parts give, for every fixed
b>8 and m=0,2,

    |partial^m h_t(x)|<=C_b(1+t)^(-(3+m)/2)
                   (1+|x|/sqrt(1+t))^(-b).           (11)

For detail, each difference multiplier has a simple zero at theta=0.
On a fixed neighborhood of zero, derivatives of total order b of the
multiplier times exp(-t lambda) have L1 norm at most
C_b t^((b-3-m)/2), t>=1, by rescaling theta by sqrt(t) and integrating
polynomial Gaussian bounds. Without derivatives the bound is
C t^(-(3+m)/2). A smooth partition away from zero has exponential
time decay, including all its derivatives. Integration by parts in a
maximal coordinate of x and the undifferentiated bound yield (11).
For t<=1 all Fourier derivatives are uniformly bounded. This also
handles reversals and bounded shifts of source-difference stencils.

The exact Dirichlet heat kernel on {1,...,N-1}^3 is the tensor product
of the interval formula of J. S. Dowker, *Heat-kernels on the discrete
circle and interval*, [arXiv:1207.2096v2](https://arxiv.org/pdf/1207.2096v2),
31 August 2012, section 7, (29)--(31), printed pp. 10--11, including
the image/sine equivalence proof following (31). Set his p=N; section 2,
(1)--(3), uses the same unscaled second-difference generator, with no
jump-rate factor 1/2. The commuting coordinate generators give the
three-dimensional tensor product. Thus the odd image sum has period
2N in each coordinate. The formula vanishes at 0,N, so
taking differences to these boundary vertices is permitted. For
t<=N^2, retain the finitely many nearest reflected images separately.
Their distances are at least the direct distance up to a bounded
stencil shift. Integrating (11) gives C(1+r)^(-1-m). After a fixed
finite grouping every other image has distance >=cN(1+|v|), v in Z^3.
Summing their bounds in (11) and integrating to N^2 gives C N^(-1-m);
the v sum converges since b>8. Thus nearby boundary images are retained,
not declared distant.

For t>=N^2 use the entire normalized Dirichlet sine spectrum:
k in {1,...,N-1}^3, eigenvalue >=4|k|^2/N^2. Mode products have
amplitude <=C N^-3; each difference supplies <=C |k|/N, including on
end edges. Summing shells gives C N^(-3-m)exp(-ct/N^2), whose
integral is C N^(-1-m). This includes every finite mode. Integrating
the heat kernel proves the corresponding undifferenced and mixed-
difference Green bounds. Expanding q at its two endpoints and absorbing
bounded shifts proves exactly (10). Fixed-face tangential rows with
two zero endpoints contribute zero; no normal row is removed.

There are O(N^3) transverse edges in each direction, and at most
C(1+r)^2 edges in a shell about any fixed edge. Multiplying (10)
and summing the second edge gives a uniform constant: the four
radial sums are bounded respectively by

    C sum_(r<=CN)(1+r)^(-2),
    C N^-1 sum_(r<=CN)(1+r)^(-1),
    C N^-3 sum_(r<=CN)(1+r),
    C N^-4 sum_(r<=CN)(1+r)^2.

They are O(1), O(N^-1 log(eN)), O(N^-1), O(N^-1).
Consequently the complete transverse product sum is

    sum_(alpha,beta)|(d_j G d_j^T)_(alpha,beta)|
                         |(q_j G q_j^T)_(alpha,beta)|<=C N^3. (12)

This is a joint kernel estimate. Separate global Hilbert--Schmidt
norms would lose the quarter power being sought.

### 3. Transverse and axial prefix rows, with the upper jump

For mu transverse, the two covariance entries in (9) equal U_st
times their corresponding transverse entry in (10). Thus (2),(12)
give the complete bound

    E_Y[Q_mu^2]<=C ||y||_infinity^2 N^4 N^3
                =C ||y||_infinity^2 N^7.             (13)

Every axial pair s,t is summed; no prefix localization is used.

For mu=1 write d,q_1 for the full axial difference and endpoint sum
from vertices 1,...,n to edges j=0,...,n, with phi_0=phi_(n+1)=0.
Set A_U=d U d^T and B_U=q_1 U q_1^T. The min kernel gives exactly

    (A_U)_(j,k)=delta_(j,k),             0<=j,k<n,
    (A_U)_(j,n)=(A_U)_(n,j)=-1,        0<=j<n,
    (A_U)_(n,n)=n.                                  (14)

For example each interior increment is phi_(j+1)-phi_j, and the
last increment is -phi_n. Their covariances give (14) directly.
In particular sum_(j,k)|(A_U)_(j,k)|=4n. Since every U entry lies
between 0 and n, every B_U entry has absolute value at most 4n.
Hence

    sum_(j,k)|(A_U)_(j,k)(B_U)_(j,k)|<=16n^2.         (15)

The last row and its two off-diagonal strips are present in (14)--(15);
replacing this pinned incidence by an upper-free difference is not
allowed. The transverse factor of both axial covariance entries is
G, so its product sum is Tr(G^2). Equations (2),(9),(15) give

    E_Y[Q_1^2]<=C ||y||_infinity^2 N^2 N^4
               =C ||y||_infinity^2 N^6.              (16)

The actual upper jump is therefore lower order in this particular
quadratic norm count. It has been bounded, not canceled or smoothed.

Applying the tensor comparison (8) to each direction and color order,
then the finite triangle inequality, yields

    ||sum_e y_e [D phi,q phi]_e^c||_2
                         <=C ||y||_infinity N^(7/2). (17)

For the direct bracket [z,q phi], different input colors give the exact
product of their two covariances. Hilbert--Schmidt Cauchy--Schwarz,
the bounded operator q, and (2) give for each order

    ||sum_e y_e z_e^d(q phi^f)_e||_2
       <=C ||y||_infinity (||S||_HS||K||_HS)^(1/2)
       <=C ||y||_infinity N^3 log(eN)^(1/4).         (18)

Within a color no independence of z and phi is assumed; the two
bracket orders are combined by the triangle inequality. For N>=2
the bound (18) is absorbed by (17). Restoring the fixed factors 1/2
and -1/4 proves (5). Equation (3) and a^2=64/N^2 give (6).

### 4. Return to the complete signed sextic in its original order

L194's exact external-leg contraction, with the same modal convention
as (3), is

    E[J_i rho_H]=2a^2 sum_(k,l,c)d_(i;kl)
                        E[<e_l,b^c>d rho_H[n_k^(c)]],
    d rho_H[n^(c)]=d script R_3[n^(c)]
            -d^2 script S_3[n^(c),Tz]
            -d script S_3[(Tn)^(c)].                 (19)

Only the external B_i leg has been contracted. Differentiating the
tilt direction gives the last term, while the middle term contains
both other action placements. Neither is deleted. The signed two-slot
tilt estimate underlying (4) stays in its original order, after the
whole action quadratic is formed. Both residual subtractions are in
the first term. Applying Cauchy--Schwarz only now, (3),(4),(6) give

    |E[J_i rho_H]|
       <=C_i a^2 N^(3/2)N^3 sqrt(log(eN))
        =C_i' N^(5/2)sqrt(log(eN)).                  (20)

The constants are uniform in the admitted mesh because the polynomial
mode factors are summed using the complete bound (3). Both actual
probe forms and every allowed constant index are retained by that
expansion. Since log(eN)>=1, (20) proves (7). In particular its
cubic-scaled allowance is O(N^-1/2 sqrt(log(eN))). No existing
qualitative zero limit, Q_3 rate, independent-prefix replacement,
covariance commutator gain or rough-column regularity is used.

The verification here is analytic: (8) is the cited exact Gaussian
contraction; (10)--(12) include all transverse boundary rows and
modes; (14)--(16) include the full pinned axial matrix; (19) preserves
the original signed tensor and all three action placements. No
mathematical script or finite numerical preview is used as evidence.
The separate audit below accepts this proof relative to its imported
premises; it does not upgrade the audit status of those premises.

### Separate critical audit, 2026-10-23

**Verdict: accepted relative to the stated analytic imports.** The
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-23-prefix-sextic-rate-critical-audit.md`
authorizes precisely this audit. No estimate, exponent, original
response definition or direct mathematical input required correction.
The interval citation above makes the already used standard formula
precise; the dimension-three specialization remains the local argument.
This verdict applies to L264 alone.

**Coefficient and covariance spaces.** For one direction and color
order the actual coefficient is F_mu=D_mu^T diag(y)q_mu on interior
vertices, extended by zero at boundary vertices. Its two Gaussian
arguments are different colors of the same prefix field, each with
covariance K. Therefore (8) applies to this whole, possibly signed F_mu.
Both summands in Y tensor Y-K tensor K are positive tensor products;
no commutation or nonsingular covariance is needed. Under Y its
coefficient norm expands to (9), with exactly one differentiated
covariance and one endpoint-sum covariance. Reversing the colors
transposes this coefficient but gives the same norm estimate. Taking
the triangle inequality over the two orders and four directions
retains their correlations and costs only a fixed constant. This
checks the applicability to the actual SU(2) bracket, not just a
generic positive quadratic or independent prefixes within a color.

**Both source differences survive reflection.** In one image term the
kernel argument is x-epsilon y+2Nv, epsilon_j in {1,-1}. Differences
in observation and source in direction j supply, up to phases and
signs, the factors (exp(i theta_j)-1) and
(exp(-i epsilon_j theta_j)-1). Their product has a second-order zero
at the frequency origin also when the source is reflected. Thus m=2
in (11) is justified for these mixed differences. Taking an integer
b>8, the small-frequency differentiated Fourier integral is bounded
by Gaussian rescaling; away from zero it decays exponentially in t.
The bounded-time Fourier integrand has uniformly bounded derivatives.
This gives (11) for all t, including the time interval below one.

The direct and nearest reflected image distances are no smaller than
the edge separation up to a fixed stencil shift. Their heat integrals
give (1+r)^(-1-m). For the other images, put u=1+t. Their absolute
sum for t<=N^2 is bounded by

    C N^(-b) u^((b-3-m)/2) sum_v (1+|v|)^(-b).

Its integral is O(N^(-1-m)), because b>m+1 and the image sum is
finite for b>3. This checks the full remote image sum rather than
a single-image estimate. The all-mode sine sum for t>=N^2 has the
same integrated order. In particular the derivatives of normalized
sine functions on both end edges are bounded by C|k|/N times their
normalization; their boundary values are exactly zero. At edges
meeting more than one face the odd extensions still vanish on each
face, and the same bounds apply. No Dirichlet condition is assigned
to a normal component of the original relative link field: the scalar
Dirichlet field here is the vertex potential in the imported positive
comparison. These facts establish (10) for every required row.

For a fixed transverse edge the four complete product sums have
orders 1, N^(-1)log(eN), N^(-1), N^(-1), as displayed before (12).
Multiplication by the O(N^3) first-edge count proves (12). This is
the joint estimate needed by (9); separate global covariance norms
would not establish the same exponent. The full axial factor for a
transverse direction is sum U_st^2=O(N^4), giving precisely N^7
for its squared quadratic norm.

**Pinned axial endpoint.** The first n increments of the min kernel
have identity covariance. The last increment is minus their sum,
so its covariance with each of them is -1 and its variance is n.
This verifies all of (14), including both off-diagonal strips. Their
absolute entry count is n+2n+n=4n. Every endpoint sum uses at most
four entries of U bounded by n, proving (15) with 16n^2. The
transverse product is the unrestricted sum G_alpha,beta^2=Tr G^2,
whose full sine-shell bound is O(N^4) by L186(9). Hence this whole
axial sector has squared norm O(||y||_infinity^2 N^6). No upper-free
incidence or deletion of an end row is involved. The direct z,prefix
bracket instead uses S and qKq^T for distinct colors, so (18) follows
by Hilbert--Schmidt Cauchy--Schwarz with bounded q. Its
N^3 log(eN)^(1/4) norm is absorbed in N^(7/2). Restoring the actual
1/2 and -1/4 coefficients proves (5), and e_l=a^2 f_l proves (6).

**Return to the original response.** L183(1)--(2) and L194's
hypotheses define the same b, J_i, T=2SA and rho_H. The external
factor has color c whereas b^c has only the other colors, so Gaussian
integration by parts has no derivative-of-b term. The three terms
in (19) are exactly L194(12): the residual derivative, the two rough
action-slot derivatives, and the derivative of Tz. L194(8),(11),(13),
(14), also retained in L202(13), give (4) for their complete sum.
The signed whitened tilt acts on the two remaining input slots in
that imported bound; no smoothness of Tz or covariance commutation
is used. Both residual Q forms remain inside script R_3.

The original expansion is B_i=a^2 sum d_(i;kl)e_k e_l^T, so the
single external-leg contraction contributes exactly 2a^2, not a
second probe factor. Combining (6) with (4) gives the exponent
-2+3/2+3=5/2 and the retained square-root logarithm in (20).
All polynomial factors in k are summed by (3), including the allowed
constant own-direction modes. Both actual probe matrices are already
in that expansion; no fixed-mode preview or probe sign is needed.
The result meets the proposed log(eN)^2 budget and has normalized
allowance O(N^(-1/2)sqrt(log(eN))).

This audit validates this existing local rate, not a stronger rate,
an upstream audit or a discovery beyond the checked standard methods.
L193's co-closed response and the independent transverse-H rate still
need quantitative control. No bound for the full joint group or L011
response, interacting theory, continuum axioms or infrared mass follows.
No mathematical script or numerical test was needed for this audit.

## Mathlib

Full matching prefix-modal/sextic rate: **not checked**. Supporting
Isserlis, positive tensor order, finite Gaussian linear images,
Hilbert--Schmidt inequalities and discrete Dirichlet heat-kernel
coverage: **not checked**; unknown coverage is not absence. The named
pairing theorem is imported by the precise primary citation above.
The dimension-three full-boundary kernel specialization is proved
because L200's dimension-four bound does not itself imply the needed
joint sum. The exact pinned axial calculation is likewise retained.
No general renormalized gradient-flow theorem is reproved or assigned
to a selected bare term. The unchanged prior
[rate assessment](../drafts/literature/2026-10-23-prefix-sextic-quantitative-remainder.md)
authorizes this bounded contraction attempt, not an originality claim
or advance beyond the general methods in the sources checked.
