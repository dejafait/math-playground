# L231 — A quantitative remainder for the complete action plateau

## Hypotheses

Keep exactly L216's plateau response T_i^pl in (1)--(2) and coefficient
P_i in (9). The group is SU(2), the relative pinned cube is (-4,4)^4,
the forest is straight and lower-rooted in direction 1, admitted N is
even, a=8/N, and the actual probes are i=3,6 at tau=1/16. The bare
small-coupling coefficient is taken at fixed mesh before refinement.
All coordinates and transposes are ordinary stored coordinates.

Import L224 proof sections 1--3 and its section-7 audit for the identical
scalar insertion C_(j,N)=a A_<j: its signed dipole decomposition,
coefficientwise O(a) approximation, uniform coefficient bounds and
scalar dipole decay. Import L216's definitions, energy bound, exact
exterior expansion and global bounds. Use L222(2),(3),(7),(9),(12)'s
supporting product-mode and probe estimates, rather than its different
diagnostic conclusion. Upstream analytic inputs remain hypotheses;
this is not a recursive audit of them.

## Conclusion

For sufficiently large admitted N and both actual probes,

    |a^3 T_i^pl(a)-P_i| <= C_i N^(-1/2),
    |T_i^pl(a)-a^(-3)P_i| <= C_i N^(5/2).             (1)

The constants are finite and independent of N. This meets the proposed
O(N^(5/2)log(eN)^2) threshold. It retains every axial cut, the moving-cut
endpoint, the nonzero upper cumulative tail, all traversal/color
entries, normal end rows and the full heat sum. The coefficient P_i is
unchanged and is not reevaluated here. The separate critical audit in
proof section 6 accepts this specialization relative to the stated
imported inputs. It is local REPRODUCTION, with no claim of
progress beyond the sources checked.

This is only the plateau component rate. Other component rates, the
complete quantitative response, interacting reflected error <=c_box/2,
continuum axioms and finite positive physical mass remain unresolved.
There is no construction candidate.

## Proof

### 1. Exact scalar form and full-grid extension

Let Omega_N={1,...,N-1}^3 be the transverse vertex set, H its pinned
Laplacian and G=H^(-1). Write x_p=(-4+aj,-4+av) for a transverse
plaquette anchor. For its signed traversal dipoles q_l, L216(1) gives

    (a V_p^pl)_lm=(Gq_l)^T C_(j,N)(Gq_m).            (2)

The three color blocks are identical and diagonal. In particular (2)
has no Gaussian-tilt factor 2.

Use L224(2)--(4), including their audited coefficient-level proof. For
a fixed finite set of nonzero integer displacements d, chosen with one
of each pair d,-d, there are signed real coefficients b_(d,N) such that

    C_(j,N)=sum_(n,d) b_(d,N)(j,n) h_(n,d)h_(n,d)^T,
    h_(n,d)=e_n-e_(n+d),
    |b_(d,N)(j,n)-b_d(-4+aj,-4+an)| <= C a.          (3)

The smooth b_d have uniform C^1 bounds and a common fixed transverse
support away from the faces, uniformly in all 1<=j<N. Both endpoints
of every nonzero summand are interior. The quarter layer and cut term
are included in (3); transverse support does not imply axial support.
In particular no cumulative upper tail has been removed.

Extend b_(d,N) by zero on all other full-grid pairs, and extend b_d
smoothly by zero in the transverse variables. Because both supports
have a fixed transverse buffer, (3) holds on the entire grid for large
N, with the same constant. Let C~_(j,N) be the resulting full-grid
form. It agrees with C_(j,N) on zero-extended finite fields.

For any fixed d, express h_(n,d)^T f by a fixed nearest-neighbor path
of differences. Cauchy--Schwarz on that path, followed by summation in
n, gives sum_n |h_(n,d)^T f|^2 <= C_d ||f||_E^2, where
||f||_E=||grad f||_2 on Z^3. Applying this to (3), using the bounded
coefficients and the finite set of d, proves

    |<f,C~_(j,N)g>| <= C ||f||_E ||g||_E.            (4)

The estimate holds on finite-energy fields by completion and is uniform
in j,N. It does not assume that C_(j,N) or its coefficients are positive.
The frozen form M_x=sum_(n,d)b_d(x)h_(n,d)h_(n,d)^T has the same bound.
Its symbol is exactly m_E(x,theta), by L224(4) and L216(5).

### 2. Radius-dependent energy projection for the four source dipoles

Let eta_l be the four full-grid signed dipoles in L216(4), translated
by v, and let g_l=H_infinity^(-1)eta_l. Each source is at a bounded
offset from v. L224(5) and its potential estimate give uniformly

    |g_l(n)| <= C(1+|n-v|)^(-2),
    |grad g_l(n)| <= C(1+|n-v|)^(-3),
    sum_n (1+|n-v|)^2 |grad g_l(n)|^2 <= C.          (5)

Here and below edge locations in the gradient sum can be replaced by
their tails, changing only C. The scalar inputs are Lawler--Limic,
*Random Walk: A Modern Introduction* (2010), Theorem 4.3.1,
Corollary 4.3.3 (printed pp. 81--84), and Theorem 6.3.8(a) (p. 131),
<https://www.math.uchicago.edu/~lawler/srwbook.pdf>, in exactly the
nearest-neighbor d=3 normalization and mixed-difference specialization
checked in L224 section 2. No new scalar Green theorem is reproved.

Let R>=2. If v is at lattice distance at least 4R+h+4 from every
transverse face, where h bounds the fixed stencil/source offsets,
choose a cutoff equal to one within radius R of v and zero beyond
2R, with first differences <=C/R. Its product with g_l is an admissible
pinned vertex field. The same cutoff calculation as L224(9), now at
radius R rather than a fixed fraction of N, gives

    ||(1-chi)g_l||_E^2 <= C R^(-3).                  (6)

Specifically the gradient tail is bounded by
C sum_(r>=R) r^2 r^(-6) <= C R^(-3). The cutoff derivative contributes
C R^(-2) sum_(R<=r<=2R) r^2 r^(-4) <= C R^(-3).
The finite source offsets and discrete product shifts change constants
only. This shows explicitly that C in (6) does not depend on a fixed
physical source buffer.

As in L216(11), the zero extension f_l=Gq_l is the energy-orthogonal
projection of g_l onto finite pinned vertex fields: for every such
test z, <f_l,z>_E=<q_l,z>=<g_l,z>_E. Every edge to a pinned endpoint
is present in this identity. Orthogonal best approximation and (6)
therefore give

    ||f_l-g_l||_E <= C R^(-3/2),
    ||f_l||_E+||g_l||_E <= C.                       (7)

There are four sources, so the constants are common. By (4), replacing
both finite columns in (2) by their full-grid columns changes their
pairing by at most C R^(-3/2). No scalar boundary condition is assigned
to a relative vector component; only the already scalar G is used.

### 3. Bilinear coefficient freezing has an O(a) error

For every full-grid n, (3) and the global Lipschitz bound of b_d imply

    |b_(d,N)(j,n)-b_d(x_p)| <= C a(1+|n-v|).         (8)

This remains true outside Omega_N, since b_d is zero near and beyond
the transverse boundary and its zero extension is Lipschitz. It is not
a zero extension of a forest potential.

For either traversal index l, write D_d g_l(n)=h_(n,d)^T g_l. The
bounded path argument used in (4), with its bounded shifts, and (5)
give

    sum_n (1+|n-v|)^2 |D_d g_l(n)|^2 <= C.           (9)

Consequently Cauchy--Schwarz bounds
sum_n(1+|n-v|)|D_d g_l(n) D_d g_m(n)| by C for every l,m,d.
Using (8) term by term in the exact signed decomposition (3) now gives

    |<g_l,(C~_(j,N)-M_(x_p))g_m>| <= C a.           (10)

Thus the coefficient is frozen only after pairing both complete
dipole gradients. No coefficient is commuted through G, and no rough
column is treated as smooth. Fourier Plancherel identifies the frozen
pairing with precisely the l,m entry of L216(6). The two dipole Fourier
factors and |m_E|<=C lambda bound its absolute integrand, including the
integrable zero-frequency case. Combining (7),(10) proves

    |a V_p^pl-mathcal V(x_p)| <= C(R^(-3/2)+a)       (11)

outside the stated transverse collar, uniformly in all cuts j and
every traversal/color entry.

For every plaquette, including the collar, use the original global
bound instead: L216(10), L215(10) give |a V_p^pl|<=C, since
q_l^T Gq_l<=1 on normal end edges as well. The limiting mathcal V is
bounded. Fixed traversal rows are zero in the finite expression and
need not be matched to a boundary continuum value in (11).

### 4. Match the raw exterior matrix before the entire heat sum

This verifies the normalization separately from L224's different path
trace. Let A_(k,a)=f_k/sqrt(lambda_(k,a)) be the smooth extension of a
physical product mode, r=|k|>=sqrt(3), and A_k its continuum version.
L222(2),(3) give

    ||A_(k,a)||_(C^m)+||A_k||_(C^m) <= C_m r^(m-1),
    ||A_(k,a)-A_k||_(C^m) <= C_m a^2 r^(m+1).        (12)

For a raw positive transverse mu-edge at level j<N the exact L216
exterior column v_(k,a) has the normalized value

    (v_(k,a)/a)_mu
      =A_(k,a),mu(edge midpoint)
        -[phi_(k,a)(j,y+a e_mu)-phi_(k,a)(j,y)]/a,
    phi_(k,a)(j,y)=a sum_(s=0)^(j-1)
                     A_(k,a),1(-4+(s+1/2)a,y).      (13)

L222(9) controls this same prefix and its first transverse derivative,
uniformly in j. Its physical length is at most 8, so its transverse
C^2 norm is <=C r by (12). The integral difference formula compares
the raw forward quotient in (13) with its derivative with error
C a r. Combining this with (12), L222(9), and the O(a) shifts of all
four traversal midpoints from x_p gives

    |w_(k,a,l)-sigma_l(mathfrak r A_k)_(n_l)(x_p)|
                       <= C a r^2,
    |v_(k,a)/a|+|mathfrak r A_k| <= C.               (14)

Here w_(k,a,l) is sigma_l times the positive-direction raw finite value
(v_(k,a)/a) on traversal l's underlying edge. Its separate value bound
follows from bounded first derivatives
and prefix length <=8, not from the high-label error bound. These
estimates hold on the interior used in (11), uniformly as that interior
approaches the transverse faces. The normalized global finite bound
holds on all rows. At a normal transverse end edge the boundary value
of phi is the actual zero tangential A_1 sine value; no extrapolation is
required. At axial label zero phi retains its full linear length j a.
No value at the separately pinned upper transverse link j=N is used.

The probe coefficient in L216's exact expansion is the whitened
polarized form B_(i,a;kl). L222(7) compares it with beta_(i;kl) with
error C_i a(1+r+t)^2, retaining the triplet's four products and both
shear polarizations, and bounds both values by C_i. L222(12) bounds
the product heat-weight error by
C a^2(r^4+t^4)exp[-c(r^2+t^2)], where t=|l| and c>0 is fixed.
Telescoping the two exterior factors (14), probe coefficient and heat
weight gives the summand error

    C_i a(1+r+t)^4 exp[-c(r^2+t^2)].                 (15)

The full two-mode sum of this bound is O_i(a). For omitted continuum
labels at least one coordinate is >=N; their indicator is <=(r+t)/N,
so the same polynomially weighted Gaussian sum bounds their complete
contribution by C_i/N. Therefore

    |a^(-2)U_(i,p)-mathcal U_i(x_p)| <= C_i a        (16)

on the interior in (11), for both actual probes and all j<N. There is
no spectral cutoff. Termwise first derivatives of the continuum lift
and of the heat expansion have one further fixed polynomial majorant;
hence mathcal U_i has bounded C^1 norm on the closed box, using the
one-sided upper trace of the lift. Independently L216's global estimate
gives |a^(-2)U_(i,p)|<=C_i on the collar too.

The calculus input is Taylor's theorem with remainder, NIST DLMF
v1.2.8, section 1.4(vi), (1.4.35)--(1.4.37),
<https://dlmf.nist.gov/1.4#vi>, already imported with these smooth-mode
hypotheses in L222. The raw quotient (13), not a diagnostic average or
L224's Bb/Bq trace, is what has been matched here.

### 5. Joint collar count and physical quadrature

Retain L216(15) exactly:

    a^3 T_i^pl=-24 a^4 sum_(p in P_T)
                    K:(a^(-2)U_(i,p)):(a V_p^pl).   (17)

The transverse collar of lattice width 4R+h+4 has at most
C(R+1)N^3 plaquettes over all axial levels and planes. The finite
and sampled limiting terms in (17) each have bounded entries there,
so their total normalized discrepancy is <=C_i(R+1)/N. This counts
all fixed tangential zeros, variable normal end rows and face
intersections. No boundary row is silently discarded.

On the complement, telescope (11),(16), using their separate uniform
value bounds. There are O(N^4) terms and a^4 N^4 is fixed, yielding
error <=C_i(R^(-3/2)+a). The fixed tensor K, three colors and the
original -24 are retained once throughout.

The sampled limiting integrand K:mathcal U_i:mathcal V has uniformly
bounded C^1 norm on the closed box: the assertion for mathcal U_i was
just proved; for mathcal V it follows from (3), its fixed d sum and
the bounded dipole energy pairing. It has compact transverse support,
but may have a nonzero upper axial tail. Compare its values on each
physical mesh cube with its integral using the first derivative bound.
The total error is O_i(a). Adjusting the plaquette-anchor ranges to
that cube sum changes at most O(N^3) bounded terms, also O_i(a) after
multiplication by a^4. In particular the missing axial endpoint strips
are accounted for by boundedness; compact axial support is never used.
This sum tends with that rate to exactly P_i in L216(9).

We have proved the finite inequality

    |a^3 T_i^pl-P_i|
       <= C_i[(R+1)/N+R^(-3/2)+a]                  (18)

whenever the interior cutoff fits; if that interior is empty for a
small N, no eventual assertion is affected. Choose R=ceil(sqrt(N))
for sufficiently large admitted N. Then R/N=O(N^(-1/2)),
R^(-3/2)=O(N^(-3/4)), and a=8/N. Equation (18) proves (1),
including the stronger absence of a logarithmic loss. Only this
uniform finite inequality receives the N-dependent radius; no
fixed-parameter limit theorem is evaluated at a varying parameter.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-plateau-action-quantitative-remainder.md`.
L224's energy/coefficient inputs are specialized to traversal sources
with a shrinking collar, and L222's modal bounds to the raw lifted
matrix. Neither different trace conclusion is imported. The recorded
raw-forest-loop and upper-pin failures remain: no bounded raw forest
covariance or smooth upper-pin continuation is asserted. The new
energy/collar and normalization argument, not numerical evidence,
supplies the local component rate. The independent audit is recorded below.

### 6. Separate critical audit, 2026-10-18

**Verdict: accepted relative to L215, L216, L222 and L224.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-plateau-rate-critical-audit.md`.
This checks the new quantitative implications (3)--(18), without a
recursive audit of those inputs or an import of a different trace rate.
No correction to (1) or its hypotheses is required. The scalar Green
and Taylor citations in sections 2 and 4 retain the hypotheses checked
in the saved assessment; no new source theorem is needed.

**Full-grid signed form.** L224(2)--(4) concerns exactly a A_<j,
including the quarter layer, both residual subtractions and cut term.
Its exact zero row sums give a signed dipole decomposition, not merely
an approximate principal symbol. Both endpoints of every active pair
have a fixed transverse buffer. Thus extending its coefficients by zero
introduces no missing cross-face term. The limiting coefficients have
the same support buffer, so the O(a) comparison holds on the full grid.
For each fixed path d, its translated nearest-neighbor edges occur only
a bounded number of times in the sum over n. The path inequality hence
bounds the D_d map from energy to l2. Applying Cauchy--Schwarz to the
two images proves (4) for signed coefficients. This check does not
infer positivity or commute a multiplier with an inverse.

**All four sources and radius constants.** L216(4)'s first and fourth
dipoles are at the anchor and its neighbor; its second and third have
the additional mu or nu shift. Each is a translate, possibly with a
minus sign, of a nearest-neighbor dipole by a uniformly bounded offset.
Their potential and gradient bounds therefore share constants with
radial distance measured from v. A source-to-face distance at least
4R+h+4 contains the radius-2R cutoff and all fixed source/product shifts.
The gradient tail and cutoff derivative have squared energies bounded
respectively by sum_(r>=R) C r^(-4) and
C R^(-2) sum_(R<=r<=2R) r^(-2), both O(R^(-3)).
These constants use no fixed physical distance from the boundary.

For each finite pinned vertex test z, the zero extension f_l satisfies
<f_l,z>_E=<q_l,z>=<g_l,z>_E. In particular the finite gradient energy
includes all edges to zero boundary vertices. The cutoff field is an
admissible competitor, so orthogonal best approximation gives (7).
The bilinear comparison splits exactly as
<f_l-g_l,C~ f_m>+<g_l,C~(f_m-g_m)>; (4) and the separate bounded
energies give O(R^(-3/2)). This holds also for distinct traversal
dipoles, without identifying their sources or using a diagonal-only
estimate. Collar sources are not assigned this cutoff comparison.

**Signed freezing.** The global limiting b_d is Lipschitz after its
transverse zero extension. Therefore the pointwise discrepancy from
its value at x_p is at most Ca+Ca|n-v|, including omitted coefficient
rows outside the finite cube. The fixed-path shifts preserve (5)'s
weighted squared-gradient bound. Explicitly,

    sum_n (1+|n-v|)|D_d g_l(n) D_d g_m(n)|
      <= [sum_n (1+|n-v|)^2 |D_d g_l(n)|^2]^(1/2)
         [sum_n |D_d g_m(n)|^2]^(1/2) <= C.

This verifies (10) on the whole grid before any freezing or Fourier
identification. The frozen symbol is m_E by the imported coefficient
identity. Since |eta_hat_l|<=sqrt(lambda) and |m_E|<=C lambda,
its complete bilinear Fourier integrand is bounded in magnitude by C.
Thus neither a singular principal value nor an absolute first kernel
moment is needed for (11). The same bound with a derivative of b_d
gives the required uniform first derivative of mathcal V.

**Raw normalization and complete heat labels.** L216's exact exterior
column is a R_F A_(k,a). Its transverse row divided by a is the raw
positive-edge sample minus the forward quotient of the length-ja
prefix, exactly (13). Taking a traversal introduces sigma_l once;
the four shifted samples approach the same anchor with those signs.
This is not the diagnostic's endpoint-averaged path. In L222's
normalization the ordinary four-dimensional product eigenvector is
a^2 f_k and the square root of its dimensionless eigenvalue is
a sqrt(lambda_(k,a)); their quotient is a A_(k,a), consistent with
that exact exterior expansion. Thus U carries precisely a^2, with no
additional inverse eigenvalue, factor 2, or color multiplier.

The forward quotient differs from the derivative by at most Ca r,
using the prefix's transverse C^2 bound Cr. Its derivative differs
from the continuum derivative by C(ar+a^2 r^2), from L222(9).
The direct sample, normalization change and bounded traversal shifts
are covered by the same C ar^2 envelope for a<=1 and r>=sqrt(3).
Separate first-derivative value bounds give a uniform bound on both
lifted values, even when the high-label error exceeds one. At a normal
transverse end edge the boundary prefix is the actual tangential sine
zero. At axial mode zero the prefix remains its full linear length;
no evaluation at the separately pinned transverse level j=N is used.

L222(7) compares the same whitened B entries in L216's U expansion,
retaining all four triplet products and both shear polarizations.
Telescoping these entries, the two raw exterior factors and the heat
weight yields (15), using their separate value bounds. Every fixed
polynomial times exp[-c(r^2+t^2)] is summable over the complete two
four-dimensional component-mode ranges. Missing finite labels have
at least one coordinate >=N, so their indicator is at most (r+t)/N.
The continuum value bound and the same summability test control their
entire contribution by O(N^(-1)). This verifies (16) for both probes,
not only a finite-mode preview. Differentiating the continuum prefix
transversely or axially costs only another fixed polynomial in r;
the same argument gives the closed-box one-sided C^1 bound for U.

**Collars, quadrature and final exponent.** Over all planes and axial
levels a transverse collar of width 4R+h+4 contains at most
C(R+1)N^3 plaquettes. L216's global U bound and its energy bound for
V, with L215's q_e^T Gq_e<=1 on normal end edges, apply to every
such row. Both sampled limiting matrices are bounded too. Equation
(17) therefore gives collar error C_i(R+1)/N. No finite boundary
row must match its continuum trace to obtain this bound.

On the remaining O(N^4) anchors the uniform errors (11) and (16),
multiplied by a^4, cost C_i(R^(-3/2)+a). The limiting integrand is
C^1 up to its one-sided axial ends; compact transverse support is
enough. Integrating the first-derivative cell error gives O(a) over
the whole box. Changing the anchor ranges or retaining the nonzero
upper cumulative trace affects only O(N^3) bounded cells, also O(a).
This is exactly L216(9)'s physical integral with -24, the three color
blocks and each transverse plane counted once. There is no extra
Gaussian-tilt factor or axial normalization.

These checks establish (18) with a constant independent of R,N when
the stated cutoff fits. For R=ceil(sqrt(N)) it fits eventually outside
the counted collar. The three errors are respectively O(N^(-1/2)),
O(N^(-3/4)) and O(N^(-1)). Multiplication by a^(-3)=(N/8)^3
gives the claimed O(N^(5/2)) unscaled remainder. This substitutes a
radius into a finite uniform inequality, not a qualitative limit.

The existing DAG row is unchanged: L216 fixes the response and limit,
L224 supplies the signed stencil and scalar energy inputs, L222 the
modal estimates, and L215 the boundary dipole bound. The recorded raw
forest-loop and pinned-upper-face obstructions are not reopened.
This audit accepts one local quantitative reproduction; it proves no
stronger rate, complete-response estimate or interacting construction.
Full matching and supporting Mathlib coverage remain not checked.

## Mathlib

Full coverage of this specialized quantitative plateau-response rate:
**not checked**. Supporting Fourier Plancherel, energy orthogonal best
approximation, Cauchy--Schwarz, Taylor bounds and Riemann quadrature:
**not checked**. Unknown availability is not evidence of absence.
No matching full theorem or certified originality is asserted.
