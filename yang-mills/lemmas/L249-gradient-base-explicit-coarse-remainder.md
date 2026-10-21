# L249 — An explicit coarse remainder for the gradient-base pair

## Hypotheses

Use precisely L102--L104's SU(2) relative all-face cube, lower-rooted
direction-1 forest, sufficiently fine admitted even N, a=8/N,
tau=1/16, stored coordinates, bare-first order and actual probes i=3,6.
Retain the entire source/end spaces, allowed constant indices and heat
series. Let P_(i,N) be exactly L103(5), R_gx its complete crossed pair,
and K_(i,G) exactly L104(6). There is no outside factor 3.

Use L103's Delta, G, E, W, X and Zeta. Import L028's centered smooth
sample estimates, and only the supporting modal/raw-path/heat bounds
L248(3)--(11), not its reverse-trace conclusion. These supporting bounds
concern the same modes, displacement and two probe polarizations;
their applicability to the present traversal slots is checked below.
All constants can depend on those fixed data, but not on N or the
auxiliary mass epsilon. Imported results retain their qualifications.

## Conclusion

Put ell_N=log(eN). Uniformly for N^(-1/2)<=epsilon<=1 and sufficiently
large N,

    |R_gx(i,N)-a^(-3)K_(i,G)|
      <=C_i [N^(5/2)+N^3 epsilon^(1/4)
                         +N^2 epsilon^(-3) ell_N].             (1)

Consequently the permissible finite choice
epsilon=(ell_N/N)^(4/13) gives

    |R_gx(i,N)-a^(-3)K_(i,G)|
                        <=C_i N^(38/13) ell_N^(1/13).          (2)

This is a weaker quantitative remainder than the requested
O(N^(5/2)ell_N^2): the ratio of the displayed majorants is
N^(11/26)/ell_N^(25/13), which tends to infinity. It is local progress
from qualitative o(N^3) to an explicit subcubic power, not completion
of that target, a finer asymptotic coefficient, interacting control or
a Yang--Mills construction. The interacting reflected error <=c_box/2,
quantitative assembly of the independent components, continuum axioms
and infrared finite positive mass all remain open. The separate critical
audit in proof section 5 accepts this specialization relative to its
imported premises; it does not discharge their independent qualifications.

## Proof

### 1. Quantify the coefficients without changing the cumulative layer

Use L104(7)--(13). Define d_hat_(k,t)=d^>_(k,t)/a^2,
X_hat=X/a^2 and zeta_(l,a)=Zeta_l/a. At fixed t the exact normalized
massive trace is

    a^3 P_(i,N,epsilon)=a^4 sum_(k,l)c_(i;kl,a) sum_t (at)
      Tr[G_epsilon X_hat_(k,t) G_epsilon
                                  W_t^T D_T^T zeta_(l,a)(t) T]. (3)

The compact support belongs to the displacement multiplier in W,
not to d_hat. In particular every upper cumulative summand and its
moving-cut half-weight in X_hat remain in (3).

Here and below p denotes one sufficiently large fixed polynomial of a
mode label. On every fixed compact transverse interior, uniformly in
all existing levels t and retained labels, L104(8)--(11) quantitatively
give, with x_1=-4+at and an edge-center sample y,

    |d_hat_(k,t;mu,y)-h_(k,mu)(x_1,y)|<=C a p(k),
    ||h_k||_(C^1(D))<=C p(k),
    ||d_hat_(k,t)||_infinity<=C p(k).                       (4)

The last bound is global, including pinned rows, by L103(11).
Here is why the first two bounds are uniform polynomials rather than
unspecified fixed-label constants. L248(3) bounds every fixed C^r
norm of A_(k,a), A_k and their difference by a fixed polynomial in
|k|, with difference O(a^2 p(k)). Apply L028(4)'s integral centered
difference estimate to the two circulation samples and then to the
opposite plaquette-center difference in L104(8). This gives
d_(k,s)/a^3=delta_k+O(a^2 p(k)); a fixed number of derivatives obeys
the same bound after enlarging p. Summing fewer than N terms in the
actual cumulative expression gives exactly

    d_hat_(k,t)=a sum_(s=t+1)^(N-1) delta_k(-4+as,.)
                              +(a/2)delta_k(-4+at,.)+O(a^2 p(k)).

On intervals of length a the integral-versus-endpoint error is bounded
by a^2 sup|partial_1 delta_k|. Summing at most N intervals, and keeping
the missing upper endpoint and the displayed half term, costs at most
C a p(k). This proves (4) against the full integral from x_1 to 4.
That integral and its first physical derivatives have polynomial mode
bounds by the length-8 interval and L104(1). It need not vanish for t
below the support of any other coefficient. No upper pinned potential
is sampled or smoothly continued in this argument.

For the other factors, the raw normalized positive mu-link is

    A_(l,a,mu)(x_1,y+a e_mu/2)
       -[phi_(l,a)(t,y+a e_mu)-phi_(l,a)(t,y)]/a,
    phi_(l,a)(t,y)=a sum_(j=0)^(t-1)
                             A_(l,a,1)(-4+(j+1/2)a,y).

This is L248(4),(6), obtained from the same forest retraction as L104.
L248(5),(8) bound its difference from v_(l,mu)(x_1,y) by C a p(l),
and bound its value independently by C p(l). The four signed path
slots are +mu at y, +nu at y+e_mu, -mu at y+e_nu, -nu at y.
Their first-two and second-plus-third sums therefore match respectively
v_mu+v_nu and v_nu-v_mu within C a p(l). Their rough rows are exactly
L104(4)'s b,q; hence zeta freezes to z_v with those signs. This checks
every slot, rather than transferring an endpoint-averaged diagnostic.
The constant axial mode has its full linear lower prefix in phi;
the formula never uses t=N's separately pinned potential.

L028(4) compares the smooth displacement samples with u_1 in each
fixed C^r norm; bounded grid shifts cost O(a). Expanding W's endpoint
averages and centered differences therefore freezes it to precisely
L104(5)'s w. The limiting coefficients h_k,u_1,v_l and their first
physical derivatives are bounded by fixed polynomials. It follows
that moving a sample by at most R cells and freezing it at a common
cell point costs C a(1+R)p(k)p(l) for each product of the three
coefficient types, with their independent value bounds used in
telescoping. This statement concerns deterministic coefficients only.

Finally L248(10)--(11) applies to exactly L104's c matrices:

    |c_(i;kl,a)|+|c_(i;kl)|<=C_i exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)-c_(i;kl)|
                   <=C_i a p(k)p(l) exp[-c0(|k|^2+|l|^2)],       (5)

where c0=tau/16. That proof retains the four products with factor
1/4 in the triplet, and both clover polarizations with factor 1/2
in the shear. Those are the same B entries in L104(15), so no probe
sector or normalization is changed. The supporting modal and heat
estimates suffice here; neither L248's reverse coefficient nor L222's
diagnostic conclusion is used.

### 2. Expose the inverse polynomial constants and every boundary path

For 0<epsilon<=1 put rho=12/(12+epsilon),

    B_epsilon=(12I-Delta)/(12+epsilon),
    p_m(Delta)=(12+epsilon)^(-1) sum_(j=0)^m B_epsilon^j.

This is exactly L104(14)'s geometric polynomial. On pinned transverse
vertices Delta has diagonal 6 and neighbor entries -1, with missing
neighbors pinned to zero. Thus B_epsilon has nonnegative entries and
row sums at most rho. The infinite lattice has the same entries and
row sums exactly rho. In both cases

    ||p_m||<=epsilon^(-1),
    sup_x sum_y |p_m(x,y)|<=epsilon^(-1),
    ||G_epsilon-p_m||<=epsilon^(-1)rho^(m+1).           (6)

The operator estimates also follow directly from the spectral formula
on [0,12]. No positive-entry assertion about a vector projection is
involved. Expanding powers of B gives nonnegative walk weights of
range at most m and total mass at most epsilon^(-1) per starting row.
This short verification is needed to expose the absolute walk constant;
a general decay theorem is not reproved or assumed uniform in mass.

Choose the integer m=ceil(130 epsilon^(-1)ell_N). Since
log(1+epsilon/12)>=epsilon/13, rho^(m+1)<=(eN)^(-10).
Replacing the two inverse positions in (3) once each, using L104(12)
and the bounded local stencil norms, costs at most

    C_i epsilon^(-2)(eN)^(-10)                         (7)

after cubic normalization. Indeed the trace rank is O(N^3) per t,
a^4 sum_t(at)N^3=O(1), and (5) controls all heat labels. The same
bound holds for the corresponding whole-grid Fourier integrals.

For epsilon>=N^(-1/2), 2m+R0<=C sqrt(N)ell_N=o(N), where R0 is
the fixed total range of the other stencils. Expand the cyclic trace
at one occurrence of the displacement multiplier in W. Every starting
point is then in a fixed compact physical subset with clearance
eta>0 from all faces; endpoint averages enlarge it by only R0 cells.
For sufficiently large N, uniformly in the permitted epsilon range,
all polynomial walks and all intervening local stencil rows stay
inside the transverse cube. Their finite and infinite coefficients
therefore coincide exactly. This accounts for every finite path;
paths that could reach a boundary were retained in the uniform inverse
error (7). No covariance sources are restricted. There is no axial
walk here: the sum defining X_hat has already been performed exactly,
and t remains the original level selected by W.

### 3. Freeze absolute walks and compare the complete density

On each such closed walk replace its deterministic coefficients by
the continuum coefficients at the displacement anchor. Section 1
bounds their product error by C a(1+2m+R0)p(k)p(l).
All other local stencil entries have a fixed absolute row-sum bound.
The two inverse polynomials have total absolute path mass at most
epsilon^(-2) by (6); their positive walk expansion prevents an
exponential-in-m loss. Consequently the error per diagonal anchor
is at most C a(1+m)epsilon^(-2)p(k)p(l). Sum over O(N^3) anchors
and all t with a^4(at), and use (5). The normalized error is

    C_i a(1+m)epsilon^(-2)
                        <=C_i N^(-1)epsilon^(-3)ell_N.         (8)

No multiplier crosses an inverse or projection in this estimate.
The loss is deliberately an absolute-walk loss, not a claimed sharp
joint Green estimate.

For frozen coefficients, expanding closed walks gives exactly the
zero Fourier coefficient of their ordered stencil product. Thus its
density is L104(6)'s ordered numerator with lambda^(-2) replaced by
p_m(lambda)^2. This matches sigma,w,c,z_v,tau in that order; neither
an orientation factor nor the outside 3 is introduced. Restore both
massive scalar inverses with (7). Their density and its first physical
derivatives have bounds C epsilon^(-2)p(k)p(l), because only the
smooth coefficients depend on x. The fixed physical factor x_1+4
has the same property. Rectangle quadrature on the a-grid therefore
costs C_i a epsilon^(-2), as does (5)'s heat-coefficient replacement.
These errors are bounded by (8).

Labels absent from the finite mesh force |k|+|l|>=cN (with a fixed
positive c). Bound their indicator by (|k|+|l|)/(cN) and apply the
Gaussian envelope (5), with an enlarged fixed polynomial. Their whole
continuum tail costs at most C_i N^(-1)epsilon^(-2), again within
(8). Allowed componentwise constant indices remain in both sums.
There is no omitted-label convergence assumption. All rearrangements
are justified by these absolute polynomial-times-Gaussian majorants.

Let K_(i,G,epsilon) denote L104(6) with denominator
(lambda+epsilon)^2. Equations (7)--(8) and the density comparisons give

    |a^3 P_(i,N,epsilon)-K_(i,G,epsilon)|
        <=C_i [N^(-1)epsilon^(-3)ell_N
                              +epsilon^(-2)(eN)^(-10)].       (9)

This is uniform in the stated finite mass range, not the application
of a fixed-mass convergence theorem to varying masses.

### 4. Remove mass with the imported finite estimate and state the loss

L104(16) bounds the absolute ordered numerator by C p(k)p(l)lambda^2.
The difference of its massive and massless integrals is consequently
bounded by the integral of

    C p(k)p(l) [1-lambda^2/(lambda+epsilon)^2]
       <=C p(k)p(l) min(1,2epsilon/lambda).

The last inequality follows by direct multiplication for lambda>0;
the value at lambda=0 is irrelevant. On [-pi,pi]^3,
lambda>=c|theta|^2, so integral lambda^(-1) is finite. After the
physical and full heat sums this proves

    |K_(i,G,epsilon)-K_(i,G)|<=C_i epsilon.             (10)

L103(7) supplies the separate finite trace error C_i epsilon^(1/4)
after normalization; its condition N sqrt(epsilon)>=1 holds throughout
our permitted range. L102(2) and L103(6) supply the complete-pair error
C_i N^(-1/2) after normalization. Apply the triangle inequality with
(9)--(10). For epsilon>=N^(-1/2), the polynomial approximation error
in (9) is at most C N^(-9); epsilon<=epsilon^(1/4), and this N^(-9)
term is absorbed by N^(-1)epsilon^(-3)ell_N. Multiplying by
a^(-3)=N^3/512 proves (1).

The choice epsilon=(ell_N/N)^(4/13) lies between N^(-1/2) and 1
for sufficiently large N. Both mass/freezing terms in (1) then equal
N^(38/13)ell_N^(1/13); N^(5/2) is smaller. This proves (2).
No qualitative limit receives a mesh-dependent parameter.

Balancing the two positive terms in this particular majorant yields
the same order as (2), up to constants. This majorant therefore cannot
certify the requested threshold. This is a limitation of the present
absolute estimate, not a lower bound for the actual signed error or
a reason to abandon the gradient-base target. A sharper ordered joint
kernel/energy comparison could replace (8), or strengthen inverse
removal; those estimates remain unproved. Independent component rates
and all interacting and construction gaps remain unresolved.

This is RESEARCH / REPRODUCTION under the unchanged EXPLORE assessment
`drafts/literature/2026-10-20-gradient-base-crossed-quantitative-remainder.md`.
The new local quantitative specialization exposes the constants in
L104's geometric-walk argument. Known polynomial, Taylor and finite
spectral methods are used, without claiming originality beyond the
sources checked. No mathematical script or numerical premise is used.

### 5. Separate critical audit, 2026-10-20

This audit accepts (1)--(2) relative to the imported hypotheses. It
checks the quantitative specialization of L104 and the application
of L248's supporting bounds, not the independent proofs of all their
ancestors. No stronger rate, evaluated coefficient, or interacting
estimate is established. The following are the load-bearing checks.

**Coefficient polynomials and the cumulative endpoint.** For any fixed
nonnegative derivative order q, L248(3) and the centered remainder in
L028(4) bound the smooth extension of the circulation error by

    ||f_(k,s)/a^2-F_k||_(C^q)<=C_q a^2(1+|k|)^(q+2).

Both terms have this bound: the centered derivative error uses three
derivatives of A_(k,a), and the normalization error uses one derivative
of A_(k,a)-A_k. Taking the opposite-plaquette difference through its
integral derivative, instead of bounding two unrelated errors divided
by a, consequently gives

    ||d_(k,s)/a^3-delta_k||_(C^q)
                              <=C_q a^2(1+|k|)^(q+3).

The physical derivatives here are those of the smooth sample extensions,
at existing axial levels; no derivative across the upper forest pin is
used. The prefix drops out of the circulation exactly. The bounds are
uniform for all retained labels, even when their right sides are large.
For q=0, summing the error with weights a, and at most N summands,
still gives C a^2(1+|k|)^3 because aN=8.

The endpoint convention can also be checked directly. The right endpoint
sum on [x_1,4] is a sum_(s=t+1)^N delta_k(-4+as). The delta-sum in
section 1, before its already bounded O(a^2 p(k)) error, differs by

    -a delta_k(4)+(a/2)delta_k(x_1).

The right endpoint quadrature error is bounded by
8a sup|partial_1 delta_k|, while these two explicit endpoint terms
are bounded by (3a/2) sup|delta_k|. This verifies the uniform O(a)
error for every cut t, without discarding its upper tail or half.
The limiting h and its first derivatives have fixed polynomial bounds;
the global finite coefficient bound remains the imported L103(11),
including its zero-wedge pinned rows.

**Raw slots and heat normalization.** Dividing the stored forest column
by a gives exactly A_(l,a,mu) minus the one-sided quotient of
phi_(l,a). L248(5),(8) apply to this quotient before any endpoint
averaging. The signed slots are +mu, shifted +nu, shifted -mu, -nu;
their two sums give v_mu+v_nu and v_nu-v_mu. Thus the frozen row is
(v_mu+v_nu)q-(v_nu-v_mu)b, with precisely L104(4)'s raw shifts.
The axial constant mode retains its linear lower prefix, and t=N
is not an interior sample. The displacement and its endpoint filters
give exactly w_mu=-u_1(1+exp(i theta_mu))i sin(theta_mu)/2.

The two heat coefficient matrices in L248(10)--(11) are the same
matrices used in L104(15): the triplet contains the four curvature
products with factor 1/4, and the shear contains both polarized clover
products with factor 1/2. The coefficient error in (5) is therefore
available without importing the reverse response or an averaged
diagnostic. Independent value bounds are used in every product
telescoping, so multiplying high-mode errors never replaces a value
estimate. A fixed polynomial times exp[-c0(|k|^2+|l|^2)] is summable
over all component choices and two four-index labels. For an omitted
label |k|+|l|>=cN; its indicator bound in section 3 uses that same
complete series. Allowed constant indices are not omitted labels.

**Uniform boundary comparison and absolute path count.** In this scalar
vertex space Delta has diagonal 6 even adjacent to a pinned face:
the missing neighbor has prescribed zero value. Thus 12I-Delta has
nonnegative entries and row sums at most 12. Symmetry supplies the
corresponding column bound. Summing the geometric series gives

    (12+epsilon)^(-1) sum_(j=0)^m rho^j
                      =(1-rho^(m+1))/epsilon<=epsilon^-1.

This is the absolute weight of all walks from any starting row, not
merely an operator-norm estimate. Inserting each fixed local stencil
multiplies this row-sum bound by a fixed constant. The total absolute
weight of closed walks with two polynomial segments is no larger
than that of all such walks, hence at most C epsilon^-2.
There is no path-count factor exponential in m.

For a transverse edge vector v, expand
W^T v=-sum_mu T_mu^T M_(u_(a,1)) C_mu v_mu and cycle each resulting
trace to its displayed multiplier. Choose a fixed compact set K containing
the supports of both u_(a,1) and u_1 for every sufficiently small a,
and a larger fixed compact set K' inside D with positive clearance
from K. Take the anchor sum over every grid point in K, including
points where u_(a,1) is zero. This also accounts for points where the
continuum displacement is nonzero but its discrete sample vanishes:
their replacement error is included in |u_(a,1)-u_1|.
Outside K both multipliers vanish.

The entire closed path has range at most 2m+R0, including every
rectangular incidence, endpoint selector and alternating path.
Uniformly for epsilon>=N^-1/2, its physical range is at most
C log(eN)/sqrt(N), eventually smaller than the clearance of K in K'.
Consequently every intermediate vertex, edge and plaquette lies
inside K'. Finite and infinite polynomial paths agree exactly there,
and the coefficient estimates apply on this single fixed compact
set, even though the number of cells in the walks grows. No estimate
on a compact coefficient is assigned to the noncompact cumulative h.
The axial index does not propagate in these transverse polynomials;
the entire cumulative axial sum has already been retained.

Before making this comparison the inverse error is estimated on the
full finite space. Each of its two telescoping terms has norm at
most C epsilon^-2 rho^(m+1)p(k)p(l); the vertex rank is (N-1)^3.
Thus no excluded covariance source or end row is hidden in the exact
interior path identity. Since log(1+epsilon/12)>=epsilon/13,
the stated degree gives rho^(m+1)<=(eN)^-10 uniformly. The same
uniform scalar error applies when restoring the frozen Fourier
integrals.

**Trace density, finite constants and the final exponent.** The original
prefactor is a^-1 t, X contributes a^2, Zeta contributes a, and cubic
normalization contributes a^3. Their product is a^5 t=a^4(at).
There are O(N^3) transverse anchors and
sum_(t=1)^(N-1) at=4(N-1), so a^4 N^3 sum_t(at) is bounded.
The per-anchor coefficient error C a(1+2m+R0)p(k)p(l), multiplied
by the absolute walk mass, therefore gives exactly
C_i N^-1 epsilon^-3 log(eN) after the full heat sum.

For frozen coefficients, the cumulative stencil symbol is
sum_mu h_mu[(1-exp(-i theta_mu))-(1-exp(i theta_mu))]=sigma_k.
The other factors retain the order w* c* z_v tau. Integrating the
closed walk shifts therefore gives precisely L104(6), with the
two massive scalar denominators. No extra color, orientation or
outside factor 3 enters. The frozen density is compact through u_1;
its physical C^1 norm is at most C epsilon^-2 times the fixed mode
polynomial. Grid quadrature and the heat coefficient discrepancy
each cost C_i a epsilon^-2. The omitted-label tail has the same
bound. All fit within the larger freezing allowance.

Finally the four frequency differences in sigma,w,c,tau give an
absolute numerator bound C p(k)p(l)lambda^2. For lambda>0,

    0<=1-lambda^2/(lambda+epsilon)^2
                                      <=min(1,2epsilon/lambda).

Since lambda>=c|theta|^2 on this three-dimensional torus, its integral
is O(epsilon). L103(7)'s distinct finite mass error retains the
weaker epsilon^(1/4), with N sqrt(epsilon)>=1 throughout the range
used here. L102(2) and L103(6) retain the O(N^(5/2)) removed terms.
These are finite inequalities before any mass schedule is substituted.

At epsilon=(ell_N/N)^(4/13), the mass term is
N^(3-1/13)ell_N^(1/13), and the walk term is
N^(2+12/13)ell_N^(1-12/13). Both equal
N^(38/13)ell_N^(1/13). Also epsilon/N^-1/2
=N^(5/26)ell_N^(4/13)>=1 and epsilon<=1 eventually.
The remaining N^(5/2) term is smaller. Relative to the desired bound,
the ratio of the two majorants is
N^(11/26)/ell_N^(25/13), which diverges.

No failed assertion was found in this specialization. This is an
audited partial quantitative input, not a sharper bound or a lower
bound for the signed error. Rebalancing these same two losses cannot
certify the requested rate; an ordered joint kernel/energy estimate
would require its own mathematical attempt. The saved primary
literature assessment is reused: no general decay theorem is being
invoked to certify this trace, and no new source theorem or numerical
premise is introduced by the audit.

## Mathlib

The full matching quantitative cumulative-trace theorem is **not
checked**. Supporting geometric series, finite spectral calculus,
absolute finite walk expansions, rectangle quadrature and integrable
three-dimensional inverse symbols are **not checked**. Unknown
availability is not evidence of absence. No external general trace or
Ward theorem is invoked to replace this specialization.
