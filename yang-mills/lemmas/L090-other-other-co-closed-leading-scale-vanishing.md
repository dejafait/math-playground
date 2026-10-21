# L090 — The actual co-closed rough sector vanishes at cubic scale

## Hypotheses

Use exactly L088–L089's finite SU(2) Gaussian, actual L010 probes
i=3,6, L018 residual, lower-rooted direction-1 forest, relative
all-face pinned box, admitted even N, a=8/N and tau=1/16. The bare
small-coupling coefficient is taken at fixed mesh first. Coordinates
are ordinary dimensionless stored coordinates. All interior axial
levels, transverse end rows, ordered pairs including coincidences,
both residual orientations and every exterior heat mode are retained.

Import K=K_h=R Q, Q=I tensor (I-P), R=Delta_E^(-1), and
Delta_E=L_D tensor I+I tensor Delta_T from L085–L089. The ambient
space E consists of all interior-level transverse links. Import
H_k, H_k^h=Q H_k Q, V_gen, T_red and the real symmetric exterior
coefficients c_(i;kl) from L089. Thus

    T_red=sum_(k,l)c_(i;kl) Tr(H_k^h V_gen (H_l^h)^T K).

No covariance identity is differentiated in what follows. The
projections are fixed selectors in this already differentiated trace.

## Conclusion

For each actual probe,

    lim_(N->infinity) a^3 T_red=0,
    lim_(N->infinity) a^3 T_hh=0.                         (1)

The second assertion includes L089's actual exterior-circulation
and curvature-form remainders. This resolves the finite-to-frozen
comparison at the leading scale only. It supplies no O(N^2) bound,
N^2 limit or logarithmic coefficient. No numerical D_i is used.

The complete other/other group remains unresolved: its six rough
sectors other than the gradient/gradient and co-closed/co-closed
sectors would still need joint limit -4 gamma D_i before the outside
factor 3 to compensate L084. Independent response jets, finer powers,
finite matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass
remain open. There is no candidate Yang–Mills solution.

## Proof

### 1. Express the actual generator line on its invariant row space

Let I embed E into the full relative one-form space with component 1
zero, and set E_h=Q I^T. All transposes here are real finite-matrix
transposes. Write Sigma=Delta^(-1), L=D_1^T D_1 and G0=I^T K_a I,
using L018's unscaled incidences and actual L009 generator K_a.
The generator is a fixed-range stencil with coefficients O(1/a),
so bounded row/column multiplicity gives

    ||G0||<=C/a<=C' N.                                  (2)

The relative tensor decomposition in L003/L026 implies
Delta I=I Delta_E. A vector I Q y has zero relative divergence:
its component 1 is zero and T^T Q=0 at every interior axial level,
including the pinned end rows. Thus Sigma L I Q=I Q. By transposing,

    E_h Sigma L=E_h,
    Sigma E_h^T=I K,
    E_h Sigma E_h^T=K.                                  (3)

These are identities on the full relative spaces. For example,
Sigma L is the orthogonal projection onto the divergence-free
one-forms, since there are no relative harmonic one-forms (L003).
The row field I Q y lies in that subspace; no condition is imposed
on K_a I Q y.

L018/L089's generator matrix is (L K_a+K_a^T L)/2. Consequently

    V_gen=(Q G0 K+K G0^T Q)/2.                           (4)

Because H_k^h Q=Q H_k^h=H_k^h, its exact trace is

    T_red=(1/2) sum_(k,l)c_(i;kl) {
        Tr(H_k^h G0 K (H_l^h)^T K)
       +Tr(H_k^h K G0^T (H_l^h)^T K) }.                 (5)

Both orientations are kept. Formula (4) is a covariance-row identity,
not a transfer of a cubic vertex or an assumption that G0 preserves
the co-closed subspace.

### 2. A derivative estimate retaining staggered boundary jumps

Let p(k) be enlarged, if necessary, from L088's fixed polynomial.
L028's smooth relative modes and prefix formula give the following
additional bounds on the actual path coefficients in H_k:

    ||b_k||_infinity+||q_k||_infinity<=C a p(k),
    |b_k(x+e)-b_k(x)|+|q_k(x+e)-q_k(x)|
                                      <=C a^2 p(k).     (6)

The second line applies to neighboring existing plaquette rows in
each coordinate. Here x+e means one lattice-index step. To check its
scope, v_k is a times the retraction of a smooth relative mode
divided by the square root of its physical eigenvalue (L028(11)).
Its prefix contains at most N smooth differences; a further transverse
difference contains at most N second differences, hence is O(a).
An axial difference uses one prefix summand. Multiplying by the outer
a gives O(a^2), including levels N-2,N-1. Each signed two-edge path
uses a bounded number of such entries. The relative sine/cosine
extensions give the same bounds on transverse end rows. Fixed
zero entries at faces are handled separately below; no smoothness
across a zero-extension jump is assumed.

For a spectral function J=K F(Delta_E), with ||F||<=1, let nabla J
denote all componentwise natural interval differences, unscaled.
Their squared energy is Tr(Delta_E J J^T). Let E_partial restrict
input rows to a fixed-width collar of the physical faces. The width
can be chosen once to contain every shift of H_k's path/circulation
stencils. Then

    ||H_k J||_HS <=C a p(k) {
        ||nabla J||_HS+a ||J||_HS
                         +||E_partial J||_HS }.        (7)

Here is a direct verification, including its boundary qualification.
Write Cc=I tensor D and use L089's expression for H_k as four terms
B^T M Cc and their negative transposes, where B is Bb or Bq and M
is multiplication by b_k or q_k. For B^T M Cc J use bounded
multiplicity, (6) and ||Cc J||_HS<=||nabla J||_HS. For Cc^T M B J,
each interior output is a signed sum of differences of neighboring
plaquette entries M B J. Each entry of B is a signed coordinate
shift of one input component. In each difference use

    m(x+e)y(x+e)-m(x)y(x)
       =m(x+e)[y(x+e)-y(x)]+[m(x+e)-m(x)]y(x).

The first term is bounded by Ca p(k) times a natural interval
difference of that input component; the second is bounded by
Ca^2 p(k) times its value. There are a bounded number of shifts
per row and a bounded number of repetitions per input row. On a
staggered grid, index-neighbor differences are precisely the natural
vertex-to-edge or edge-to-vertex interval differences, up to a shift
and sign. If such a shift crosses a face, bound the missing zero
extension by Ca p(k) times the input value in E_partial instead.
All exceptions lie in that fixed-width collar, including normal-edge
endpoints with Neumann rather than zero boundary values. Squaring
and summing these bounded-multiplicity row estimates proves (7).
This neither discards a pinned row nor imposes scalar Dirichlet
conditions on a normal component.

The exact mode bounds of L026/L086 and L089's shell sum imply

    Tr R^2<=C N^4 log(eN),
    (R^2)_(ee)<=C log(eN) for every input edge e.         (8)

Indeed each squared normalized component mode is at most 16/N^4,
so the diagonal bound follows from the first bound. Since Q commutes
with Delta_E and 0<=Q<=I, J J^T<=R^2 for the J above. The collar
contains O(N^3) rows, and therefore

    ||J||_HS<=C N^2 sqrt(log(eN)),
    ||E_partial J||_HS<=C N^(3/2) sqrt(log(eN)).          (9)

For 0<eta<=1 let Pi_eta=1_(Delta_E<=eta), a spectral cutoff used
only in estimates, and put K_lo=K Pi_eta. The shell bound
rho>=4|m|^2/N^2 gives

    ||nabla K_lo||_HS^2
       =Tr(Delta_E K_lo^2)
       <=sum_(rho<=eta) rho^(-1)<=C N^4 eta.            (10)

For clarity, max_j m_j=r has at most Cr^3 labels, and rho<=eta
forces r<=N sqrt(eta)/2. Thus the sum is at most
C N^2 sum_(r<=N sqrt(eta)/2) r<=C' N^4 eta. If that range is
empty the sum is zero. Full component multiplicities and all axial
Dirichlet modes are included. With no cutoff the same estimate is
CN^4 because rho<=16. Combining (7)–(10), a=8/N, gives

    ||H_k K||_HS<=C p(k) N,
    ||H_k K_lo||_HS<=C p(k) N [sqrt(eta)+beta_N],
    beta_N=sqrt(log(eN)/N)+sqrt(log(eN))/N ->0.         (11)

The same estimates hold for H_k^h, since Q commutes with K and
Pi_eta, and left multiplication by Q is a contraction. Also H_k and
H_k^h are exactly skew-symmetric, so their transposed left products
have the same Hilbert–Schmidt bounds. In particular the boundary
term retained in (9) costs O(p(k) sqrt(N log(eN))) in (11), not a
leading O(N) contribution.

### 3. Regularize the resolvent before the projection

For epsilon>0 define R_epsilon=(Delta_E+epsilon I)^(-1) and
K_epsilon=R_epsilon Q. All matrices here use the actual box. Since

    K-K_epsilon=K epsilon(Delta_E+epsilon I)^(-1),

split this difference at Pi_eta. On its low part the last factor
is a contraction; on its high part its norm is at most epsilon/eta.
Equation (11) consequently proves

    ||H_k^h (K-K_epsilon)||_HS
        <=C p(k) N [sqrt(eta)+beta_N+epsilon/eta].       (12)

Let T_epsilon be exactly (5) with its two K occurrences replaced by
K_epsilon and its H_k^h and G0 unchanged. For each difference of
two traces use cyclicity and Hilbert–Schmidt Cauchy–Schwarz. For
example,

    |Tr(H_k^h G0 K (H_l^h)^T (K-K_epsilon))|
      <=||G0|| ||(K-K_epsilon)H_k^h||_HS
                            ||K(H_l^h)^T||_HS.

The other covariance position and second residual orientation obey
the same estimate; K_epsilon products only decrease the corresponding
Hilbert–Schmidt norms. Sum using L088's complete bound
sum |c_(i;kl)|p(k)p(l)<=C_i. Equations (2), (11), (12) give

    limsup_N |a^3(T_red-T_epsilon)|
                          <=C_i [sqrt(eta)+epsilon/eta]. (13)

Choosing eta=sqrt(epsilon) for 0<epsilon<=1 makes this error tend
to zero as epsilon decreases. No singular inverse has been uniformly
approximated in operator norm.

Now fix epsilon. Define on E

    Q_delta=I-I_ax tensor T(Delta_0+delta I)^(-1)T^T,
    K_(epsilon,delta)=R_epsilon Q_delta,
    H_k^delta=Q_delta H_k Q_delta,      delta>0.         (14)

Here I_ax is the identity on the N-1 axial levels. The intertwining
Delta_T T=T Delta_0 implies that Q_delta commutes with R_epsilon.
It is a positive contraction. Its difference from Q has nonzero
singular values delta/(lambda+delta), one per transverse vertex
gradient eigenmode and per axial level. Thus, for 0<zeta<=1,

    N^(-4)||Q-Q_delta||_HS^2
        <=C [zeta^(3/2)+(delta/zeta)^2].                (15)

To verify the count, a vertex mode with lambda<=zeta has all three
positive indices at most N sqrt(zeta)/2, yielding at most
C N^3 zeta^(3/2) labels. Multiply by N-1 axial levels. Every other
singular value is at most delta/zeta, and the total rank is O(N^4).
No transverse gradient zero mode exists with the relative vertex
boundary conditions. All non-gradient modes have zero difference.

Define T_(epsilon,delta) by replacing K_epsilon and H_k^h in
T_epsilon with (14). The normalized factors H_k/a, a G0,
Q, Q_delta have mesh-uniform operator bounds, and
||R_epsilon||<=1/epsilon. Expanding the finitely many changed factors,
the inequality |Tr(A E B)|<=||A|| ||B|| sqrt(dim E) ||E||_HS
gives, with constants allowed to depend on fixed epsilon,

    |a^3(T_epsilon-T_(epsilon,delta))|
                   <=C_(i,epsilon) N^(-2)||Q-Q_delta||_HS.
                                                                  (16)

The scaling in (16) is a^3 a^2/a=a^4 times a trace of bounded
factors; dim E<=3N^4. Take zeta=sqrt(delta) in (15): the right
side of (16) tends to zero with delta, uniformly in N. This step
occurs after resolvent regularization; it asserts no operator-norm
smallness of the unregularized projection difference.

### 4. Prove the regularized finite trace cancels in the limit

Fix epsilon,delta>0. The two inverses in (14) admit uniform finite
polynomial approximations on their exact spectral intervals [0,16]
and [0,12]. An explicit choice for 1/(x+t), x in [0,M], is

    p_(t,m)(x)=(1/(M+t)) sum_(j=0)^m
                           [1-(x+t)/(M+t)]^j,
    |p_(t,m)(x)-1/(x+t)|
                           <=(M/(M+t))^(m+1)/t.        (17)

The error follows by multiplying the finite geometric sum by x+t.
The finite spectral theorem gives the same operator-norm bound.
Approximate R_epsilon by r(Delta_E) and the vertex inverse by
p(Delta_0); set Q_p=I-I_ax tensor T p(Delta_0)T^T. Then substitute
Q_p H_k Q_p and r(Delta_E)Q_p into both orientations of (5).
For fixed polynomial degrees all these are finite-range matrices.
Their normalized operator norms are uniform, and (17), bounded
||T||<=sqrt(12), and a^4 dim E<=C show that the normalized trace
error tends to zero with the degrees, uniformly in N and after the
complete heat sum. Neither polynomial approximation uses a covariance
cutoff or changes the original law.

Consider such a fixed polynomial trace. Its diagonal is a sum of a
fixed number of closed lattice walks of bounded range. Remove only
for this comparison a boundary collar wider than that range: it has
O(N^3) rows, bounded normalized matrix entries, and costs O(a^4 N^3)
=O(1/N). This includes both axial ends and all transverse end rows;
their contribution is bounded rather than deleted from the actual
trace. Group the three transverse component rows in each remaining
interior lattice cell, choosing its common vertex as the base point.
Moving a component midpoint to this point costs O(a) in a normalized
coefficient by (6). Freeze all coefficients of H_k/a, H_l/a and
aG0 at this same physical point for all three component diagonals.
Equation (6) and the
smooth central-difference displacement bounds in L028 give an
O(a p(k)p(l)) error in the normalized diagonal, with a constant
depending on the fixed polynomial ranges. Summing a^4 times all
rows and the absolutely controlled heat coefficients still gives
O_i(a). The unweighted incidence and polynomial factors are already
translation-invariant away from this collar.

It remains to check the sum of the three frozen component diagonals,
which is the torus average of the trace of its finite Fourier symbol.
Cancellation is asserted for this sum, not for individual component
diagonals. Use L088's staggered
plaquette-center phases, writing d_j=2 sin(theta_j/2), h=sum d_j^2,
lambda=sum_(j=2)^4 d_j^2. At the frozen point b_k/a and q_k/a
are the exact two-edge sums of a real transverse exterior vector v_k:
b/a=v_mu+v_nu and q/a=v_nu-v_mu. Indeed opposite edge entries
of that column differ by O(a^2 p(k)), already included in the
freezing error. L088(11)–(13) therefore gives

    H_k/a=i S_k,           S_k real symmetric.          (18)

The actual frozen generator, including clover and endpoint filters,
has aG0=i W_TT with W_TT real, by L088(14). In this phase convention
the polynomial symbols are

    Q_p=I-p(lambda)d_T d_T^T,   R_r=r(h) I,
    K_rp=r(h) Q_p,
    H_k^p/a=i Q_p S_k Q_p.                             (19)

They are all real symmetric except for the indicated i; positivity
of a polynomial approximation is unnecessary. In the two-orientation
trace the effective frozen generator line is

    [(iW_TT)K_rp+K_rp(iW_TT)^*]/2
        =(i r(h)/2)(W_TT Q_p-Q_p W_TT^T),              (20)

which is i times a real antisymmetric matrix. The transpose of a
real finite matrix becomes the Hermitian adjoint of its Fourier
symbol, as used in (20); replacing it by the same-frequency plain
transpose would give the wrong sign.

If S_k^p,S_l^p,K_rp are real symmetric and Z is real antisymmetric,

    Tr(S_k^p Z S_l^p K_rp)
                       =-Tr(S_l^p Z S_k^p K_rp).       (21)

This follows by transposing the scalar trace and cyclically moving
its last factor. No commutation among these four matrices is needed.
The real symmetric exterior coefficients c_(i;kl) cancel the two
orientations k,l in (21) pointwise at every frequency and every base
point. This remains true at lambda=0 and h=0 since the polynomial
symbols are defined there and transverse circulation is then zero.
Thus the frozen diagonal, summed with the full symmetric heat
coefficients, is exactly zero. No continuum exterior coefficient
limit, angular cancellation or numerical sign is required.

For fixed polynomial degrees the actual normalized trace consequently
tends to zero by the boundary and coefficient errors above. Then let
the degrees increase using (17). This proves

    lim_N a^3 T_(epsilon,delta)=0
                      for every fixed epsilon,delta>0. (22)

The order of operations matters: finite-range approximation first,
the N limit second, its operator approximation error removed third.
All heat modes are retained with the summable polynomial bound. One
can equivalently truncate that external sum, prove the statement for
its symmetric finite square, and remove its uniform Gaussian tail.
No internal spectrum is truncated in the conclusion.

### 5. Remove the regularizers and assemble the scope

For fixed epsilon, (15)–(16) and (22), followed by delta decreasing
to zero, imply lim_N a^3 T_epsilon=0. Equation (13) and then epsilon
decreasing to zero imply lim_N a^3 T_red=0. L089's bound
a^3(T_hh-T_red)=O(sqrt(log(eN))/N) gives the second part of (1).

The proof controls the actual finite co-closed sector; it does not
assign a canceled local symbol to it without a remainder estimate.
In particular (7)–(13) retain the singular low modes and the staggered
boundary jumps, and (14)–(22) regularize the projection only after
the resolvent. All signed orientations and the original finite
covariance are retained. There is no extra outside factor 3.

This is one bounded RESEARCH / REPRODUCTION proof attempt within
the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
L048's finite contraction remains imported via L085/L088; it is not
rederived. The extra applicability work is the finite-to-frozen
comparison missing from L089, using standard finite spectral,
product-difference, geometric-series and trace methods. No originality
beyond the sources checked is claimed. L082's saved-table/IEEE
qualifications still attach to any later comparison with D_i; this
analytic zero limit does not use those numerical enclosures.

## Mathlib

Full matching coverage: **not checked**. Supporting finite spectral,
Hilbert–Schmidt, geometric-series, Fourier finite-stencil and relative
cochain coverage: **not checked**. Unknown availability is not absence.
No continuum Ward, flow-renormalization or reflection-positivity theorem
is used to infer this isolated finite-box asymptotic.
