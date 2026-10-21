# L241 — Ordered bulk bound and complete left-crossed remainder

## Hypotheses

Use L240(1)--(3) literally, on the same relative all-face pinned SU(2)
cube, lower-rooted direction-1 forest, sufficiently large admitted even
N, a=8/N, tau=1/16, stored coordinates, bare-first coefficient and
actual probes i=3,6. Import L239(5) and L240(4)--(5), retaining their
pending critical-audit qualifications and those of L237--L238.
No upstream result is independently audited here.

The argument below concerns L240's whole-grid comparison on
E=l2(Z^4;R^3). Write P=P_delta, Q=Q_delta=I-P and
R=(Delta_E+epsilon I)^(-1) for the positive-mass contractions and
resolvent, not massless projections. Keep exactly L240's compact
Lipschitz extensions z_k=a v_k and finite-mesh coefficients c_(i;kl,a).
In particular v_k has O(N^4) supported cells, sup norm Cp(k), and
neighbor differences Ca p(k). Retain the full six-term Omega_k,
G=aG0, V=sum_mu H_av U_mu C_mu and A=P G-TV. Thus

    B_i=a^-1 sum_(k,l)c_(i;kl,a)
              Tr(R Q^2 Omega_k* P A R Q^2 Omega_l Q).       (1)

Use L009(3), L088(11)--(14), L093(8), and L100(14)--(15)'s
actual clover, endpoint, path and incidence conventions. L228's
global squared-moment projection commutator and local coefficient
decomposition are supporting inputs; its different bulk-trace bound
is not imported. L227's full frozen alternating symbol is also a
supporting input, not an identification of its J with the gh factor.

## Conclusion

At epsilon=N^-1, uniformly for 0<delta<=1,

    |B_i(epsilon,delta)|<=C_i N^(5/2).                       (2)

Consequently, at delta=N^(-4/3), L240(5) gives

    |R_L|<=C_i N^(5/2)sqrt(log(eN)),                         (3)

which is within the approved O(N^(5/2)log(eN)^2) threshold for both
actual probes. This is a selected component rate, relative to the
imported analytic hypotheses. The new ordered bulk argument and its
combination with L237--L240 require separate critical audit. Other
L011 rates and complete quantitative assembly, the interacting
reflected error <=c_box/2, continuum axioms, infrared control and
finite positive mass remain unresolved. There is no complete-solution
candidate or claim of progress beyond the checked source methods.

## Proof

### 1. The gh joint kernel retains the same quadratic moment

Let Omega_j, j=2,3,4, be the complete normalized frozen alternating
stencil for exterior e_j. Define convolution operators

    J_gj=P Omega_j R Q^2,
    J_hj=Q Omega_j R Q^2.                                  (4)

The second is L227's J; the first has a different left factor and
must be checked. In component-center phases put d_mu=2sin(theta_mu/2),
h=sum_(mu=1)^4 d_mu^2, lambda=sum_(mu=2)^4 d_mu^2 and r=sqrt(lambda).
L227(1),(7)--(8) gives

    P^c=d_T d_T^T/(lambda+delta), Q^c=I-P^c,
    ||Omega_j^c||<=Cr, ||partial Omega_j^c||<=C,
    ||partial P^c||=||partial Q^c||<=Cr/(r^2+delta)           (5)

for transverse derivatives; these numerators have no axial frequency
dependence. All P,Q are contractions. Differentiate the full numerator
P Omega_j Q^2 in (4). A derivative on P, or either Q, is bounded by
C r^2/(r^2+delta)<=C after the adjacent complete Omega_j is included;
a derivative on Omega_j is bounded directly. This uses matrix norm
submultiplicativity, without commuting any of these matrices. The
same bounds hold with Q on the left. Conjugation to integer-index
phases adds bounded phase derivatives times an O(r) numerator.

Periodicity is essential: L227's identities
U d_T=-i(exp(i theta_T)-1) and the trigonometric-polynomial formula
for U Omega_j^c U* show that P,Q,Omega_j, and therefore (4), are
smooth periodic symbols at positive masses. No seam term is lost.
As |partial h|<=2sqrt(h) and r<=sqrt(h), both kernels obey

    ||J_sigma,j(theta)||<=C sqrt(h)/(h+epsilon),
    ||partial J_sigma,j(theta)||<=C/(h+epsilon),
    ||J_sigma,j||_op<=C epsilon^(-1/2), sigma=g,h.           (6)

The last bound is a pointwise symbol bound and hence an operator bound.
Integrating the first two inequalities on the full four-dimensional
torus, with (4/pi^2)|theta|^2<=h<=|theta|^2, gives

    sum_z ||j_sigma,j(z)||_F^2<=C,
    sum_z |z|^2||j_sigma,j(z)||_F^2<=C L_epsilon,
    L_epsilon=log(e/epsilon).                              (7)

Indeed the unweighted squared integral is bounded by integral 1/h;
the derivative integral is bounded by integral (h+epsilon)^(-2),
whose radial integral is C integral_0^(2pi)
rho^3/(c rho^2+epsilon)^2 d rho<=C log(e/epsilon).
Entrywise Fourier-series Plancherel proves exactly the two sums in
(7); the adjoint kernels have identical sums. All four frequency
coordinates and the transverse line lambda=0 are retained. These
are squared moments, not the first absolute moments excluded by L109.

For any common-index scalar b of O(N^4) supported cells with sup
norm B and neighbor differences at most a L, (7) implies

    ||M_b J_sigma,j||_HS+||J_sigma,j M_b||_HS<=C B N^2,
    ||[J_sigma,j,M_b]||_HS<=C a L N^2 sqrt(L_epsilon).        (8)

For the commutator, at fixed displacement z at most C N^4 cells
have b(x)-b(x-z) nonzero, since x or x-z must belong to its support.
Telescoping neighbor differences bounds that difference by
a L |z|_1, and (7) completes the squared sum. The unweighted
bound follows by restricting the multiplier's row or column and using
the first sum in (7). These are global norms including every row.
The same support argument and L228(6) give, uniformly in delta,

    ||[P,M_b]||_HS+||[Q,M_b]||_HS<=C a L N^2.                (9)

The identity part of Q has zero commutator. Its slice kernel is
supported at zero axial offset, and its weighted squared norm is
uniform because integral_0^C r^4/(r^2+delta)^2 dr<=C.
Neither (8) nor (9) asserts a small commutator in operator norm.

### 2. Decompose the two actual factors in their original orders

Rowwise freezing of the full six-term Omega gives an exact identity

    Omega_k=a sum_j M_(v_kj) Omega_j+D_k.                    (10)

As in L228(9), each exterior sample in the finite-range paths lies
within bounded index distance of the output's common vertex. Its
replacement by a v_k at that vertex costs Ca^2 p(k). The two
exterior-circulation terms also belong to D_k: Cc annihilates a
constant vector, so |Cc(a v_k)|<=Ca^2 p(k) by neighbor differences.
Thus D_k has O(N^4) nonzero rows, fixed range, bounded row/column
multiplicity and entries O(a^2 p(k)). Every path, component offset
and exterior-circulation term is included in this remainder.

The scalar resolvent's squared row norm is at most C L_epsilon.
Apply this to each of the finitely many translated rows in D_k R:

    ||D_k R||_HS<=C a^2 N^2 p(k)sqrt(L_epsilon).             (11)

This assigns no whole-grid Hilbert--Schmidt norm to R itself.
Define

    U_k=P Omega_k R Q^2, H_k=Q Omega_k R Q^2,
    F_gk=a sum_j M_(v_kj) J_gj,
    F_hk=a sum_j M_(v_kj) J_hj.                             (12)

Substitute (10) and move only the common scalar across the left P
or Q, retaining its commutator. From (9), (11), and
||Omega_j R||<=C epsilon^(-1/2),

    ||U_k-F_gk||_HS+||H_k-F_hk||_HS<=C p(k)e_epsilon,
    e_epsilon=epsilon^(-1/2)+sqrt(L_epsilon),
    ||F_gk||_HS+||F_hk||_HS<=C p(k)aN^2.                    (13)

Here a^2 N^2=64 is absorbed in C. In detail, a commutator remainder
is a[P,M_(v_kj)] Omega_j R Q^2 or its Q counterpart; its bound is
C p(k)a^2 N^2 epsilon^(-1/2). The D_k remainder is P D_k R Q^2
or Q D_k R Q^2. No component stencil moves across P or Q.

Skew-adjointness of the complete Omega gives the exact signs

    R Q^2 Omega_k* P=U_k*,
    R Q^2 Omega_l Q=-H_l*,
    B_i=-a^-1 sum_(k,l)c_(i;kl,a)Tr(U_k* A H_l*).           (14)

All these operators with variable exterior columns are finite rank
or Hilbert--Schmidt as indicated. In particular their trace products
are justified by the trace-ideal inequality. Since ||A||<=C,
replacing U,H by F_g,F_h in (14), one at a time, costs at most

    C_i a^-1 e_epsilon(aN^2+e_epsilon).                    (15)

This includes the product of the two errors and uses no compactness
of A. The modewise bound has p(k)p(l), summed using the actual
complete heat envelope from L088(5).

### 3. Retain and bound the middle projection commutator

For each direction r=1,2,3,4 choose a real common-index displacement
sample u_r. Its support has O(N^4) cells, values are bounded and
neighbor differences are O(a), uniformly in N. Freezing the finitely
many displacement samples in L009(3) gives

    G=sum_r M_(u_r) W_r+D_G, ||D_G||<=Ca.                   (16)

W_r is the exact normalized constant-displacement generator stencil,
including all endpoint and clover factors. This is L228(16) multiplied
by a; bounded multiplicity proves the stated error norm. For the
other branch set

    Z_mu=T H_av C_mu (mu=2,3,4), Z_1=0.

The same finite-range row argument, now applied to
TV=sum_mu T H_av M_(u_mu) C_mu, gives

    TV=sum_r M_(u_r) Z_r+D_Z, ||D_Z||<=Ca.                  (17)

Every coefficient sample in a row of T H_av is a bounded number
of steps from that row. Replacing it by u_mu at the common vertex
costs O(a), before summing the bounded stencil multiplicity. This
is a finite-range coefficient estimate on the edge-space product TV;
it does not identify its intervening vertex space with the edge space.
All W_r,Z_r have uniformly bounded operator norms and symbols.
Consequently

    A=sum_r(P M_(u_r) W_r-M_(u_r) Z_r)+D_A,
    ||D_A||<=Ca.                                         (18)

The contribution of D_A after (15) is at most C_i(aN^2)^2.

Expanding the F factors, every remaining term has outside factor a
and the order, with v=v_kj and w=v_lt,

    Tr(J_gj* M_v P M_(u_r) W_r J_ht* M_w),
    Tr(J_gj* M_v M_(u_r) Z_r J_ht* M_w).                    (19)

Do not commute a component matrix through P. Replace only
P M_(u_r) by M_(u_r) P+[P,M_(u_r)] in the first line. Its
retained error, including outside a, has absolute bound

    a ||J_gj* M_v||_op ||[P,M_(u_r)]||_HS
                                      ||W_r J_ht* M_w||_HS
       <=C p(k)p(l) a^2 N^4 epsilon^(-1/2).                (20)

This uses (6), (8), (9) with every input and output included.
At epsilon=N^-1 it is O(p(k)p(l)N^(5/2)). It is a large
Hilbert--Schmidt commutator retained in a trace estimate, not an
O(a) operator-norm gain or termwise projection commutation shortcut.

After (20), both terms have the common form

    a Tr(J_gj* M_(v u_r) L_r J_ht* M_w),                  (21)

with L_r=P W_r or Z_r. Move the common scalar v u_r past the
complete J_gj* and retain [J_gj*,M_(v u_r)]. Cycle the final M_w
to the front only using the trace-ideal identity. The error is at most

    a ||[J_gj*,M_(v u_r)]||_HS ||L_r J_ht* M_w||_HS
       <=C p(k)p(l) a^2 N^4 sqrt(L_epsilon).               (22)

The scalar product has the same support and index Lipschitz bounds
as its factors. The main term is exactly

    a Tr(M_(v u_r w) J_gj* L_r J_ht*).                     (23)

No multiplier crosses P in (21)--(23), and no bound for a separate
absolute first kernel moment is used.

### 4. Cancel the actual frozen word and sum the uniform bounds

After restoring the signs of (14) and (18), the sum of (23) at
each common cell is the constant-exterior, constant-displacement
version of (14), with middle operator

    A_fr=sum_r u_r(P W_r-Z_r).                             (24)

The precise filter check is L100(14)--(15): in component-center
phases, P,Q,R are real and even under simultaneous theta -> -theta;
W_r is i times a real odd matrix; and

    (Z_mu)^c=-i d_T eta_1^2 eta_mu e_mu^T,
    eta_nu=cos(theta_nu/2).                               (25)

The factor eta_1^2 comes from the original H_av, not an unfiltered
identity. Thus A_fr is i times a real odd matrix. Omega_j is i times
a real symmetric odd matrix by L088(11)--(13). Each of J_gj* and
J_ht* is therefore also i times a real odd matrix. Their product
with (24) has matrix trace purely imaginary and odd under inversion.
All massive P,Q powers keep their original order. In particular the
G branch retains P^2 and five Q factors, and the TV branch retains
P,T and five Q factors, exactly as in L240(7).

The component-center phases are unitary changes of fiber coordinates
and cancel only in this closed matrix trace. Its torus integral is
zero by inversion symmetry. Integrability follows from (7) and the
bounded middle symbols, by Cauchy--Schwarz. The diagonal of the
convolution product in (23) is that integral; the finite-row common
scalar multiplies the sum of all three component diagonals. Hence
the main terms cancel for each j,t,r, and thus for every heat pair,
without any symmetry assumption on c_(i;kl,a).

Combining (15), (18), (20), (22) gives the uniform finite inequality

    |B_i|<=C_i {a^-1 e_epsilon(aN^2+e_epsilon)
                  +(aN^2)^2
                  +a^2 N^4[epsilon^(-1/2)+sqrt(L_epsilon)]}.
                                                               (26)

Only now choose epsilon=N^-1. Then e_epsilon<=C sqrt(N) for
N>=2 and aN=8, so (26) proves (2). Every preceding estimate was
uniform in delta; choosing delta=N^(-4/3) merely permits the
already proved L240 comparison. Equation (3) follows by the triangle
inequality and L240(5). Since sqrt(log(eN))<=log(eN)^2, it meets
the requested threshold. Constants p(k)p(l) in every modewise
error are summable against the full finite-mesh heat coefficients.
One can first use finite heat squares, then remove them by those
absolute envelopes; no external mode or constant index is deleted.

This is RESEARCH / REPRODUCTION using the unchanged approved
EXPLORE assessment. The known tools are Fourier-series Plancherel,
finite-stencil coefficient differences and Hilbert--Schmidt trace
inequalities; the required specialization is the gh joint kernel,
the exact signs (14), and the retained middle commutator (20).
No general decay theorem is reproved. L100 supplies only the frozen
parity calculation, not a quantitative estimate at varying mass.
L228's distinct two-orientation trace conclusion is not transferred.
The boundary comparison is imported from L240 on the actual relative
spaces; this proof neither changes their boundary law nor shortens a
covariance source set. The schedules enter uniform inequalities only.
The new rate awaits separate critical audit and supplies no complete
L011 remainder or interacting construction.

### 5. Separate critical audit of the bulk bound and complete rate

Audit dated 2026-10-19, STEP_ID YM-20261019-339-left-crossed-complete-rate-audit.
Accept (2)--(3) relative to the recorded upstream finite contraction,
relative spectrum, actual stencils and complete heat envelope. L237--L240
have also received their separate applicability audits in this step.
This supersedes the original pending-audit statements above; it is
acceptance of the existing component rate, not a stronger exponent or
an independent audit of the whole notebook. The unchanged EXPLORE
assessment covers this exact quantitative R_L target.

**The gh kernel and global support count.** Unlike L227's left Q,
the left P in J_g is essential. Differentiating that P costs
O(r/(r^2+delta)); multiplying by the complete Omega_j costs O(r),
so this product is uniformly bounded. The same argument handles
each right Q, without commuting matrices. The axial derivative has
only the resolvent denominator. Thus the derivative is bounded by
C/(h+epsilon) in all four coordinates, including lambda=0 at
positive delta. Integer-index conjugation has bounded derivatives;
the periodic t_j=exp(i theta_j)-1 expressions eliminate seam terms.
The four-dimensional integrals are bounded by integral 1/h and
integral (h+epsilon)^-2, respectively, giving (7). For P's separate
slice moment, its derivative integral is bounded by
integral_0^C r^4/(r^2+delta)^2 dr plus a bounded phase contribution.
Its axial kernel has zero offset. Hence (9) is also uniform in delta.

For a fixed offset z, the support of b(x)-b(x-z) is contained in
supp(b) union (z+supp(b)), of at most C N^4 cells. Its size is
bounded by a L |z|_1 on the entire grid. This proves the global
Hilbert--Schmidt commutator estimates, rather than just norms on
compact output rows. The exterior extensions preserve actual existing
samples and use clamping before the physical cutoff. No extension
through the forest's pinned upper zero is needed. D_k retains fixed
range, O(N^4) rows and O(a^2 p(k)) entries, including both f terms.
Its resolvent product uses squared row norms O(log(e/epsilon)),
not a whole-grid Hilbert--Schmidt norm of R.

**Signs and the middle projection.** Skew-adjointness of Omega gives
U_k*=R Q^2 Omega_k* P and -H_l*=R Q^2 Omega_l Q. Thus (14)
has its displayed minus sign. The two substitutions cost (15),
including their error/error product, since A is bounded uniformly
in delta. In the main terms only the common scalar u_r crosses P,
and its commutator remains in exactly the first word of (19).
The three factors used for (20) have norms

    O(p(k)epsilon^-1/2), O(aN^2), O(p(l)N^2).

Multiplication by the outside a gives O(p(k)p(l)a^2N^4 epsilon^-1/2).
At epsilon=N^-1 this is O(p(k)p(l)N^(5/2)). No O(a) projection
commutator operator bound is used. The remaining scalar move uses
the full J_g* moment, paired with a localized J_h* of norm O(p(l)N^2),
and costs O(p(k)p(l)N^2 sqrt(log(eN))). Finite-rank scalar
multiplication justifies cycling it; the products of two localized
Hilbert--Schmidt factors justify the other trace identities.

**Frozen filters and the final count.** The middle word is exactly
P W_r-Z_r. In center phases Z_mu=-i d_T eta_1^2 eta_mu e_mu^T,
using the original T, H_av and C_mu. W_r is imaginary and odd
with all L009 endpoint/clover filters. Each outside J* is also
imaginary and odd; P,Q,R are real and even. Consequently their
closed component trace is imaginary and odd and has zero torus
integral. Its integrability follows from the two unweighted squared
kernel estimates. The scalar in (23) is common to all three component
diagonals, so that integral is exactly the diagonal sum it multiplies.
This cancellation holds for each j,t,r, without symmetry of c_(i;kl,a).
The G word still has P^2 and five Q factors; the TV word has P,T
and five Q factors. None of these massive contractions is made
idempotent.

At epsilon=N^-1, e_epsilon=O(sqrt(N)) and aN^2=O(N).
The three allowances in (26) are respectively O(N^(5/2)),
O(N^2), and O(N^(5/2)+N^2 sqrt(log(eN))). Each has a fixed
polynomial mode envelope summable against the complete finite-mesh
heat coefficients, for probes 3 and 6 including constant indices.
This proves (2); L240's audited comparison proves (3), with its
larger sqrt(log(eN)) allowance retained. All schedules were inserted
into uniform finite inequalities. The absolute-moment, termwise
projection and varying-fixed-mass shortcuts in ATTEMPTS/029--032
are not required. Other component rates, the interacting reflected
error <=c_box/2 and the continuum/infrared construction remain open.

## Mathlib

Full matching ordered left-crossed remainder theorem: **not checked**.
Supporting Fourier-series Plancherel, convolution differentiation,
Hilbert--Schmidt commutator and trace-ideal coverage: **not checked**.
Unknown availability is not evidence of absence. No numerical
certificate or mathematical script is used in this analytic proof.
