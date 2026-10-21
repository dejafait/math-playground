# L222 — First-order rate for the complete finite diagnostic

## Hypotheses

Use exactly L080's SU(2) relative pinned cube, a=8/N through sufficiently
fine admitted even meshes, tau=1/16, fixed smooth displacement from L008,
and actual probes i=3,6. D_(i,a) is L070(9), with L080's physical mode
normalization, and D_i is L080(2). In particular retain the positive
upper curvature average, all normal end edges, the entire lower-rooted
prefix and constant axial mode, the physical distance sa, the triplet's
average of squares and the shear's polarized clover form. The upper
forest potential stays separately pinned. Any small-coupling coefficient
is taken at fixed mesh before refinement, as in the imported definitions.

Constants below may depend on the fixed displacement, box and tau, but
not on N or either exterior mode label. We assume a<=1, without loss
for the asserted eventual rate. This does not concern shrinking flow
time, growing volume, interacting measures or a different diagnostic.

## Conclusion

For both actual probes there is a finite constant C_i such that

    |D_(i,a)-D_i| <= C_i/N.                                  (1)

This quantifies only L080's diagnostic convergence. It does not improve
the independent pinned-trace comparison error, other component rates,
the complete-response remainder or interacting matching. In particular
it supplies no reflected-error bound <=c_box/2 or Yang–Mills construction.
This is a local REPRODUCTION under the prior SPECIALIZE assessment,
not a claim of progress beyond the sources checked. The separate critical
audit in proof section 6 accepts this quantitative specialization relative
to the stated imported inputs; it does not recursively audit those inputs.

## Proof

### 1. Quantitative calculus inputs and normalization

Import Taylor's theorem with remainder from NIST DLMF, version 1.2.8
(2026-09-15), section 1.4(vi), equations (1.4.35)–(1.4.37),
<https://dlmf.nist.gov/1.4#vi>. All functions to which it is applied
below are finite products of sine/cosine functions or L008's fixed
smooth compact cutoff, so the required derivatives exist on the closed
intervals containing the relevant stencils. No asymptotic expansion
without a remainder is used. The source assessment is
`drafts/literature/2026-10-17-finite-diagnostic-continuum-rate.md`.
The quantitative specialization is necessary because these standard
calculus results do not state a theorem about this diagnostic. We do
not reprove Taylor's theorem or the imported exact relative eigenpairs.

Write r=|k| and t=|l|, with the component included in each label as in
L080. Always r,t>=sqrt(3). Retained labels have every index at most
N-1. L026's exact eigenpairs and L080(4)–(5) give

    r^2/16 <= lambda_(k,a) <= lambda_k=(pi/8)^2 r^2,
    A_(k,a)=f_k/sqrt(lambda_(k,a)),  A_k=f_k/sqrt(lambda_k).

Taylor's sine remainder, uniformly for 0<=pi k_j/(2N)<=pi/2,
gives |omega_(k_j,a)^2-(pi k_j/8)^2|<=C a^2 k_j^4.
Summing the four coordinates and applying the mean value theorem to
x^(-1/2) on x>=r^2/16 yields

    |lambda_(k,a)-lambda_k| <= C a^2 r^4,
    |lambda_(k,a)^(-1/2)-lambda_k^(-1/2)| <= C a^2 r.   (2)

For every fixed integer m>=0 the smooth extensions of the product modes
therefore satisfy

    ||A_(k,a)||_(C^m)+||A_k||_(C^m) <= C_m r^(m-1),
    ||A_(k,a)-A_k||_(C^m) <= C_m a^2 r^(m+1).          (3)

For m=0 the bound r^(-1) is valid because every product-mode amplitude
is uniformly bounded, including e_0=1/sqrt(8). For higher m, each
derivative contributes at most C r. These estimates are uniform over
the whole retained spectrum, rather than fixed-label asymptotics.
In particular all first derivatives and first finite differences of
the normalized modes are bounded independently of the label and mesh.
Finite differences have this bound by their integral difference formula.

The fixed Psi and all its derivatives are bounded. Applying the same
Taylor remainder to its central differences, including their iterates,
gives

    ||u_a-u||_infinity + ||w_a-w||_infinity
       + ||s_a-s||_infinity <= C a^2.                       (4)

For example the twice differenced coefficients are estimated by
applying the central-difference error to the first difference and
bounding its required derivative by the corresponding derivative of
Psi; this uses only finitely many bounded derivatives. Their supports
are in one fixed compact subset of D for all sufficiently small a.
All stencils below on that support are interior. No extension of the
forest potential across the upper face enters (3) or (4).

We will use the following elementary rectangle-quadrature consequence
of first-order Taylor's theorem. If g is C^1 and supported away from
the faces of D, partition D into mesh cubes and compare its integral
on each cube with a^4 times its value at one vertex. The difference
on a cube is at most 4a^5 ||grad g||_infinity, by integration of the
first-order remainder along its coordinate segments. There are
(8/a)^4 cubes, hence

    |a^4 sum_(interior vertices) g(x)-integral_D g|
                       <= C a ||grad g||_infinity.          (5)

Boundary vertex values vanish; thus this is exactly the interior-vertex
sum in use here. This argument accounts for all endpoint cells, and
needs no unrecorded boundary correction from Euler–Maclaurin.

### 2. Both complete probe forms have a uniform mode error

Let F_k=dA_k. At a plaquette center, the actual lattice curvature of
the sampled A_(k,a) differs from dA_(k,a) by at most
C a ||A_(k,a)||_(C^2): compare each oriented incidence quotient to
its derivative at that center. Moving this center to any incident
vertex has the same error bound. Equation (3) then gives, for every
incident plaquette used by either probe,

    |(d_a A_(k,a))_p-(F_k)_(plane)(x)| <= C a r^2.      (6)

Indeed the two errors before weakening are C a r and C a^2 r^2.
All lattice and continuum curvature values in (6) are bounded by C;
this follows from the first-derivative bound in (3), independently of
whether its upper error bound in (6) happens to be large for a high mode.

Polarize the exact q_(3,a) in L008(2). It contains the average of
the four products (d_a A_(k,a))_p(d_a A_(l,a))_p, with the weight
w_(a,mu)+w_(a,nu). Comparing each product with
(F_k)_(mu nu)(x)(F_l)_(mu nu)(x), using their uniform bounds and (6),
costs at most C a(r^2+t^2) at each vertex. The four products are
kept separately; no square-of-average replacement occurs.

For the lattice polarization of L008(2), corresponding to L008(6), first compare each of
the two clover averages with its corresponding F value using (6),
then compare both products in the symmetric polarization. This gives
the same bound C a(r^2+t^2). There are finitely many component terms.
The strain discrepancy costs O(a^2) by (4). Multiplication by a^4 and
the vertex count costs only a fixed volume constant.

The remaining continuum integrands at the vertices are the polarized
L008(1) integrands. They are smooth and compactly supported, and
their first derivatives are bounded by C_i(1+r+t), because F_k is
bounded and ||grad F_k||_infinity<=C r by (3). Apply (5). With
B_(i,a;kl)=q_(i,a)(A_(k,a),A_(l,a)) and B_(i;kl)=q_i(A_k,A_l),
we have proved, simultaneously for i=3,6,

    |B_(i,a;kl)-B_(i;kl)| <= C_i a(1+r+t)^2.           (7)

L008's bounded form operators, in the exact normalization of L080(6),
also give |B_(i,a;kl)|+|B_(i;kl)|<=C_i. All supported incident
plaquettes were retained. Neither probe sector has been canceled or
discarded to obtain this bound.

### 3. The upper row and full prefix have quantitative errors

Use U_(k,a,mu) exactly as in L080 section 2. Its actual upper axial
difference is [0-A_(k,a,mu)(4-a,y)]/a when the mode component is mu.
The zero is the true tangential sine value. Comparing that quotient
to partial_1 A_(k,a,mu)(4,y) costs at most
C a ||A_(k,a)||_(C^2). For component 1, compare its transverse
difference at axial center 4-a/2 to the transverse derivative at 4;
the same bound applies. Finally the prescribed transverse endpoint
average shifts each smooth evaluation by at most a. Using (3),

    ||U_(k,a)-U_k||_infinity <= C a r^2,
    ||U_(k,a)||_infinity+||U_k||_infinity <= C.          (8)

Only transverse positions on the compact support enlarged by the
fixed stencils are needed here. All source rows, including the last
normal edge, are in the differences just described. D_1 R_F=D_1
justifies computing this row before forest retraction, exactly as
in L080. No interior prefix value at s=N is used.

At an interior axial level x_1=-4+sa define the smooth function of y

    phi_(k,a)(s,y)=a sum_(ell=0)^(s-1)
                         A_(k,a,1)(-4+(ell+1/2)a,y).

This is L080(8), with its exact normalization. For any transverse
multi-index beta with |beta|<=1, apply the midpoint rectangle estimate
on each of the s intervals to partial_y^beta A_(k,a,1). The total
length is sa<=8, so the quadrature error is at most
C a ||partial_1 partial_y^beta A_(k,a,1)||_infinity.
The normalization change is bounded by 8 times the corresponding
norm in (3). Consequently, uniformly in every s<N,

    ||partial_y^beta(phi_(k,a)(s,.)-Phi_k(x_1,.))||_infinity
         <= C[a r^|beta|+a^2 r^(|beta|+1)].             (9)

The transverse C^2 norm of phi_(k,a)(s,.) is at most C r, since
its sum has total length at most 8 and (3) bounds the second
derivatives of A_(k,a). Compare its actual central difference in
L080(9) to its transverse derivative, at cost C a r. Compare the
direct endpoint-averaged A_(k,a,mu) to A_(k,mu), at cost
C a+C a^2 r from (3). Combining with (9) at |beta|=1 gives

    ||V_(k,a)-V_k||_infinity <= C a r^2,
    ||V_(k,a)||_infinity+||V_k||_infinity <= C.          (10)

The second bound also follows directly from the length-8 prefix of
bounded first derivatives and its integral-difference formula; it
is not deduced from a potentially large high-mode error in the first
bound. The direct term is bounded by (3).

For axial index n=0 the midpoint prefix is exactly
(sa)/sqrt(8) times the transverse mode and its normalization; its
physical distance is never replaced by a constant or omitted. For
n>=1 it is exactly L080(10), so (9) estimates that same cosine sum,
not an alternative axial profile. Components other than 1 have zero
prefix. Transverse boundary vertex values are the exact sine zeros.
The coefficient support keeps the evaluated rows and adjacent end-edge
stencils interior; all other rows have zero weight. The separately
pinned upper potential is untouched. This avoids both stopped
replacements in ATTEMPTS/024–025.

### 4. Quantify the diagnostic vertex sum

Use P_(kl,a) from L080(11), not a trace surrogate. Equations (4),
(8) and (10), their uniform value bounds, sa<=8, and the volume
count show that replacing its sampled u_a,U_(k,a),V_(l,a) by u,U_k,V_l
costs at most C a(1+r+t)^2. This comparison includes every axial
level in the actual sum; zero-weight exterior levels are not removed
as an approximation.

The resulting sampled function is

    g_(kl)(x)=(x_1+4)u_1(x) sum_mu U_(k,mu)(y)V_(l,mu)(x).

Its support is compact in D. Its C^1 norm is at most C(1+r+t):
U_k has first transverse derivatives bounded by C r, and first
derivatives of V_l use at most second derivatives of A_l in a
length-8 prefix, bounded by C t using (3). Its undifferentiated
factors are uniformly bounded. Equation (5) therefore proves

    |P_(kl,a)-P_(kl)| <= C a(1+r+t)^2,
    |P_(kl,a)|+|P_(kl)| <= C.                          (11)

This verifies quadrature of the same physical level weight and both
actual exterior columns. It assumes no random-field boundary trace.

### 5. Sum a quantitative envelope over the full spectrum

Let S_a=lambda_(k,a)+lambda_(l,a), S=lambda_k+lambda_l,
and c=tau/16>0. Since min(S_a,S)>=(r^2+t^2)/16, (2) and the
mean value theorem for the exponential give

    |exp(-tau S_a)-exp(-tau S)|
          <= C a^2(r^4+t^4) exp[-c(r^2+t^2)].         (12)

For retained k,l, telescope the three factors of
exp(-tau S_a) B_(i,a;kl) P_(kl,a) against
exp(-tau S) B_(i;kl) P_(kl). Apply (7), (11), (12),
the uniform value bounds, and a<=1. The complete summand error is

    <= C_i a (1+r+t)^4 exp[-c(r^2+t^2)].               (13)

This holds at every retained pair, not merely below a fixed cutoff.
The sum of the right side divided by a is finite and independent
of N. To see this without a spectral-cutoff exchange, expand/bound
the fixed polynomial by a finite sum of coordinate powers and use
the product of eight convergent one-dimensional polynomially
weighted Gaussian series, with four component choices per label.

For omitted pairs at least one label has an index >=N, hence r+t>=N.
The continuum summand has magnitude at most C_i exp[-c(r^2+t^2)]
by the same value bounds. Thus its entire omitted sum is at most

    (C_i/N) sum_(all k,l) (r+t) exp[-c(r^2+t^2)] <= C_i'/N. (14)

This counts omitted labels explicitly and retains every allowed
constant own-direction mode. There is no all-zero mode. Summing
(13) and (14), and using a=8/N, proves (1) with the full heat
spectrum for each probe. No numerical enclosure, finite-mode preview
or fixed-cutoff convergence assertion is used to infer this rate.

The independent comparison of the selected trace and D_(i,a),
quantitative rates for other complete components and the recombination
audit are not inputs here and are not proved by (1). The complete
interacting and infrared construction gaps remain unchanged.

### 6. Separate critical audit, 2026-10-17

**Verdict: accepted relative to L008, L026, L070 and L080.** This audit
uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-finite-diagnostic-rate-critical-audit.md`.
It checks (2)–(14) against the exact imported definitions, rather than
treating qualitative convergence or a finite-mode test as a rate.
No failed estimate or missing hypothesis was found in this scope.
The following details record the independent checks of the quantitative
implications. They introduce neither another lemma nor a stronger rate.

**Normalization and the spectral gap.** L026(6) has edge labels
0,...,N-1 and vertex labels 1,...,N-1. Multiplying each continuum
one-dimensional mode by sqrt(a) gives those ordinary modes exactly,
including the zero cosine. Four factors give a^2 f_k; division by the
square root of the dimensionless eigenvalue a^2 lambda_(k,a) therefore
gives precisely a A_(k,a), as used in L080(5). There is no extra a,
color multiplicity or gamma in the diagnostic. Three positive indices
ensure r>=sqrt(3). On 0<=x<=pi/2, sin(x)>=2x/pi and
|sin(x)^2-x^2|<=x^4/3, the latter following from the cited Taylor
remainder and |sin(x)+x|<=2x. These give the stated lower spectral
bound and O(a^2 r^4) dispersion error for every retained label.
The derivative of z^(-1/2) on z>=r^2/16 is bounded by 32/r^3.
This verifies (2); bounded trigonometric amplitudes with m derivatives
give (3), including m=0. No smallness of ar is required.

**Coefficients and both forms.** Central differences commute with
smooth derivatives. Writing a twice-differenced coefficient error as
the sum of one central-difference error on the differentiated Psi and
the central difference of the other error gives O(a^2) with bounded
fourth derivatives of the fixed Psi. This verifies (4), including the
transition region and the support enlarged by the stencils. All such
supports and incident plaquettes remain interior for sufficiently
small a, as required already in L008. The integral difference formula
gives the curvature error O(ar+a^2 r^2) and a separate uniform bound
on curvature values. Since a<=1 and r>=sqrt(3), that error is bounded
by C ar^2. For the triplet the polarized coefficient is exactly
(a^4/4) times the sum of four curvature products. For the shear it is
exactly (a^4/2) times the sum of
bar F_(k,mu alpha) bar F_(l,nu alpha) plus
bar F_(l,mu alpha) bar F_(k,nu alpha), weighted by s_(a,mu nu).
Thus both placements, their signs and the polarization half are
retained. Product differences use one error and one bounded value,
not two large error bounds. This verifies the local error in (7).
The C^1 continuum integrands cost only C(1+r+t), so the cell estimate
(5) completes (7). Extra supported lattice rows are included in the
coefficient difference estimate (4), not discarded as a collar.
The uniform B entry bounds follow also from L008's bounded M and
the norm-at-most-one curvature/inverse-square-root map.

**Upper orientation and the actual prefix.** In component mu the
upper difference is [0-A_mu(4-a,y)]/a; in component 1 the row is
minus the transverse difference at 4-a/2. Hence its limiting sign
is partial_1 A_mu-partial_mu A_1, exactly L080(7). A displacement
of at most a in either evaluation costs C ar by the second-derivative
bound; normalization costs C a^2 r^2. This proves (8) with the same
separate uniform value bound. The last normal edge is present.
For each transverse derivative beta of order at most one, the error
of a midpoint sample integrated over an interval of length a is
at most C a^2 sup|partial_1 partial_y^beta A_(k,a,1)|.
Summing s<=N intervals gives C a r^|beta|; changing normalization
over length at most 8 gives C a^2 r^(|beta|+1). These are (9).
The transverse second derivative of the whole prefix is bounded by
8 sup|partial_y^2 A_(k,a,1)|<=C r. Its central difference error
is therefore at most C ar, without treating a long prefix as a
short stencil. The direct endpoint average costs C(a+a^2 r).
Together these imply (10). The first-derivative integral formula
separately bounds the prefix difference uniformly. For axial zero,
the exact sum is sa/sqrt(8); for other components the prefix is zero.
No value of the interior prefix at s=N enters this argument. The
upper curvature is computed by D_1 R_F=D_1 instead. Consequently
neither stopped replacement in ATTEMPTS/024–025 is being used.

**Spatial quadrature and both complete sums.** The diagnostic weight
is sa=x_1+4, and a^4 times the number of vertices is bounded by 8^4.
Its continuum integrand has bounded first derivatives of U of size
C r and of V of size C(1+t): transverse derivatives differentiate
the whole length-8 prefix, while its axial derivative uses
partial_1 Phi=A_1. Compact u_1 eliminates boundary values in the
rectangle rule, not actual upper-curvature rows. These facts verify
every factor and cell in (11). For the heat comparison, the mean
value derivative is tau exp(-tau z) and both spectral sums are at
least (r^2+t^2)/16. Thus (12) holds over the entire retained range.
Telescoping heat, B and P in that order uses their uniform value
bounds and gives (13). In particular large high-label polynomial
errors are never substituted for those value bounds. Its sum divided
by a is bounded by finitely many products of eight one-dimensional
polynomial-Gaussian series. Independently, every missing finite-mesh
label has an index at least N; hence the indicator of an omitted
pair is at most (r+t)/N. The same eight-series test verifies (14).
Both sums are mesh-independent and cover the full allowed component
and zero-own-index ranges. Adding them proves (1) for each probe.

The existing DAG row remains correct: L008 supplies the actual forms
and coefficients, L026 the exact modes and forest lift, L070 the finite
diagnostic, and L080 its physical normalization and limiting series.
No L221 estimate or unproved L220 cancellation was used. The DLMF
Taylor input is imported with its smoothness hypotheses as in section 1;
the assessment's inspected version is reused without a new source claim.
This is acceptance of a local quantitative reproduction, not progress
beyond the checked sources or a recursive verification of the notebook.
The independent N^(-1/2) trace comparison, other component rates,
interacting matching, continuum axioms and finite positive mass remain
outside this audit. Full matching Mathlib coverage remains not checked.

## Mathlib

The full diagnostic rate: not checked. Supporting quantitative Taylor,
quadrature, exponential-difference and polynomial-Gaussian summability
coverage: not checked. No matching declaration or absence claim is
asserted. Exact relative modes and form normalizations are imported
from L008, L026, L070 and L080; the standard calculus source is cited
precisely above, with its smoothness hypotheses verified.
