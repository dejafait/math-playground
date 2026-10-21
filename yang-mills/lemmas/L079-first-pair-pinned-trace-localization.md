# L079 — The actual leading circulation trace is localized to its exterior diagnostic

## Hypotheses

Keep L078's actual SU(2) probes i=3,6, straight lower-rooted forest,
relative fixed-link box, a=8/N through admitted even meshes, tau=1/16,
and fixed-mesh small-coupling coefficient before refinement. Retain
L078(2)'s J_(i,N), every transverse pinned end edge, all axial levels,
the actual u_(a,1), r_k and centered alternating map bar Q_l(s), and
all exterior heat coefficients c_(i;kl).

Use L070(9)'s exact finite diagnostic D_(i,a), without its numerical
values or any presumed continuum limit. Its upper row is the adjacent
edge average of r_k/a², and its right row is the vertex average of
the actual lifted transverse stored link divided by a. For clarity put

    R_(k,a),mu(e)=r_k(e)/a²,
    v_(l,a),mu(s,y)=C_mu(v_l)_mu(s,y)/a,
    U_(k,a),mu(y)=C_mu R_(k,a),mu(y).

Here the second v_l denotes the exterior forest column of L064,
not a new field. Thus, exactly,

    D_(i,a)=a^4 sum_(k,l)c_(i;kl) sum_(s,y)
          (sa) u_(a,1)(s,y) sum_mu U_(k,a),mu(y)
                                           v_(l,a),mu(s,y).       (1)

The index y ranges over retained transverse vertices, with pinned
zero values where needed. All directions mu are 2,3,4. Let gamma>0
be exactly the normalized torus integral in L070(3), with its full
frequency cube, not L077's high band.

## Conclusion

For both actual probes,

    a³ J_(i,N) - 2 gamma D_(i,a) -> 0.                       (2)

Consequently L078's actual centered circulation/path trace satisfies

    a³ F_(i,N)^circ - 2 gamma D_(i,a) -> 0.                  (3)

Equivalently,

    N^-3 F_(i,N)^circ - (2 gamma/512) D_(i,a) -> 0.

These statements identify the diagnostic at the N³ scale for this
selected actual trace. They do not assert that D_(i,a) converges,
evaluate its continuum value or sign, or bound F^circ by O(N²).
If D_(i,a)->D_i, then a³ F^circ->2 gamma D_i; if D_i is nonzero,
this selected term has a nonzero a^-3 coefficient. A finite-mesh
sign, including L073's certified N=24 signs, does not prove this
antecedent. Even D_i=0 would supply only o(N³), not O(N²).

The proof gives qualitative vanishing error at the N³ scale, with
no O(N²) rate. L078's O(N²) remainder, centered path/path, exterior
defect and all other response terms may remain at a² scale and may
contain logarithms. The complete response and required interacting
reflected-error bound <=c_box/2 remain open. This is local
REPRODUCTION within the saved SPECIALIZE assessment; no discovery
beyond the sources checked or Yang–Mills candidate is claimed.

## Proof

### 1. Smooth coefficients and an exact diagonal representation

L076(6) supplies uniform physical C¹ bounds on R_(k,a), with a fixed
polynomial p(k). L062's section 3 forest formula supplies the same
bounds on the transverse lifted link divided by a: its path is the
finite axial prefix of a smooth one-form difference, with sa<=8.
Taking a transverse physical difference differentiates that formula
and is controlled by the corresponding higher smooth-mode derivative.
Thus both v_(l,a) and bar t_l/a have C¹ bounds p(l), at every level
s<N and on every needed transverse stencil. Upper curvature is
lift-invariant; no interpolation across the upper forest jump is used.
L028 supplies uniform C¹ bounds on u_a, a fixed compact support
strictly inside the physical box, and its zero extension. Enlarge p
once for these derivatives. The complete heat sum remains uniformly
absolutely summable, as in L064(3) and L076's section 5:

    sum_(k,l)|c_(i;kl)| p(k)p(l) <= C_i.                    (4)

The same spectral estimates give uniformly vanishing tails when any
fixed polynomially weighted exterior index cutoff tends to infinity:
physical eigenvalues are bounded below by c|k|², the relative probe
form is uniformly bounded, and the coefficient carries both heat
factors. This stronger tail statement follows directly by bounding
|c_(i;kl)| by C exp[-c tau(|k|²+|l|²)] and summing the fixed
four-dimensional mode-index sets, with missing mesh indices assigned
zero. We will use it before passing to an untruncated exterior sum.

Set Q_(l,a)(s)=bar Q_l(s)/a. Let Omega_N be the pinned transverse
interior and let delta_y denote its ordinary coordinate vector. Put

    g_(N,y)=G delta_y,
    h_(N,s,l,y)=G V_s^T D^T Q_(l,a)(s) T delta_y.

Linearity C_(r_k)=a² C_(R_(k,a)) gives exactly

    J_(i,N)=-(a²/2) sum_(k,l)c_(i;kl) sum_s s sum_y b_(N,s,k,l,y),
    b_(N,s,k,l,y)=<C_(R_(k,a))^T g_(N,y),h_(N,s,l,y)>.     (5)

This is diagonal expansion of L078(2), not commutation of a multiplier
through G. The finite source in h has the exact form

    V_s^T D^T Q_(l,a) T delta_y
       =sum_mu T_mu^T f_mu,
    f_mu=M_(u_(a,1)(s)) C_mu
                         (D^T Q_(l,a)(s) T delta_y)_mu.    (6)

Each f_mu has a bounded number of nonzero vertex entries within a
fixed lattice radius of y, with magnitude <=C p(l). All operators
other than multipliers in (6) are fixed finite incidence/average/path
stencils. If (6) is nonzero, y belongs to a fixed compact transverse
interior K, for all sufficiently large N: its finite neighborhood
must meet the compact support of u_a. Outside K, h and b are exactly
zero. Therefore this proof omits no transverse boundary collar; the
actual source vanishes there. Every retained edge remains in the
finite operators and in the estimates below.

### 2. Uniform l² bounds and convergence for differentiated Green sources

We prove the necessary specialized spectral fact, rather than assuming
l² convergence of the undifferentiated monopole. Translate the source
y to the infinite-lattice origin and extend finite output fields by
zero. For any fixed offset z with its support in the interior and any
mu, the fields

    G T_mu^T delta_(y+z)

are uniformly bounded in l². They converge in l², uniformly for
physical y in K, to the infinite-lattice Green image of the same
translated centered-difference source. A bounded finite linear
combination of these sources has the same assertion and bound.

Indeed the pinned sine modes are

    e_q(w)=(2/N)^(3/2) product_j sin(pi q_j w_j/N),
    lambda_q=4 sum_j sin²(pi q_j/(2N)), 1<=q_j<N.

At an interior vertex with both adjacent samples retained or pinned
zero, T_mu is the centered difference with the positive-incidence
convention of L065. Its sine-mode value is bounded by

    |(T_mu e_q)(w)| <= C N^-3/2 sqrt(lambda_q).             (7)

The centered sine difference introduces sin(pi q_mu/N), whose
magnitude is at most 2 sin(pi q_mu/(2N)); all other factors have
magnitude at most one. Thus for a source t= sum_mu T_mu^T f_mu
of the finite type in (6), with sum_mu ||f_mu||_1<=B,

    |<e_q,t>| <= C B N^-3/2 sqrt(lambda_q),
    ||G t||² <= C B² N^-3 sum_q lambda_q^-1 <= C B².       (8)

For 0<epsilon<1, its part in lambda_q<=2epsilon satisfies

    ||1_(Delta_V<=2epsilon)G t||² <= C B² sqrt(epsilon).   (9)

For completeness lambda_q>=c|q|²/N², while lambda_q<=2epsilon
implies |q|<=C N sqrt(epsilon). The number in a shell of radius
m is <=C m². Therefore the sum in (9), after multiplication by
N^-3, is at most C N^-1 sum_(m<=C N sqrt(epsilon))1,
which is <=C sqrt(epsilon); if there are no such modes the sum is
zero. The same shell estimate up to C N proves (8).

On Z³ let H(theta)=sum_j 4 sin²(theta_j/2). The Fourier numerator
of a centered-difference finite source has magnitude <=B sqrt(H).
Consequently its Green image is in l², since integral H^-1 is finite
in dimension three, and its H<=2epsilon part has squared norm at
most C B² sqrt(epsilon). The latter follows from H comparable to
|theta|² near its sole torus zero and bounded away from zero elsewhere.

To prove convergence, choose a continuous spectral cutoff chi_epsilon
that is zero on [0,epsilon], one on [2epsilon,12], and lies in [0,1].
The function f_epsilon(z)=chi_epsilon(z)/z, set to zero at zero, is
continuous on [0,12]. The standard named Weierstrass approximation
theorem gives a polynomial uniformly approximating it to any desired
error eta. Both the pinned and infinite nonnegative Laplacians have
spectrum in [0,12]. Spectral calculus bounds the corresponding l²
operator approximation error by eta. On any fixed finite source, the
polynomial has fixed finite range; for y in K and large N its finite
and infinite outputs agree exactly after zero extension and translation.
The source norm is bounded by C B. Adding both polynomial errors and
both low-spectral errors gives

    limsup_N sup_(y in K) ||G_N t_y-G_infinity t||_2
                                     <= C B epsilon^1/4.

Here eta was first sent to zero at fixed epsilon. Sending epsilon
to zero proves the claimed uniform convergence. This uses no source
at a physical face; (6) placed every nonzero source uniformly inside.
It retains the full finite spectrum until the explicitly controlled
tail estimate, and does not replace an internal mode cutoff by L076's
left trace projection. The infinite inverse is used only on these
sources; it is not a bounded inverse on all of l².

### 3. The left monopole can be frozen after differentiation

L045's proof section 1 identifies the zero-extended, translated
G delta_y as the energy projection of the infinite monopole g,
with Fourier transform 1/H. Uniformly for y in K,

    ||g_(N,y)-g||_E -> 0,   ||g_(N,y)||_E<=sqrt(b0),
    b0=integral H^-1 dtheta/(2pi)^3 <infinity.             (10)

This imported energy statement includes every pinned edge. It does
not claim that g belongs to l². We also need the finite bound

    ||g_(N,y)||_2² <= C N.                                (11)

The sine amplitude is at most (2/N)^(3/2), so its spectral expansion
bounds this squared norm by C N^-3 sum_q lambda_q^-2.
The lower eigenvalue bound and shell count give at most
C N sum_(m>=1)m^-2, proving (11) uniformly in y.

Let R^y be the constant vector with components R_(k,a),j evaluated
on the positive j-edge from y. Any vertex average of those adjacent
edges differs from R^y by <=C a p(k). The exact finite formula for
C_R in L076(8) gives, for interior w,

    (C_R g_N)(w)=sum_j R_j(w-e_j)[g_N(w-e_j)-g_N(w+e_j)]
                +sum_j [R_j(w-e_j)-R_j(w)]g_N(w+e_j).     (12)

The second sum has l² norm <=C a p(k)||g_N||_2,
which is O(p(k)N^-1/2) by a=8/N and (11). Zero boundary values
are included in (12). Restricting a shifted zero extension to the
interior can only reduce its l² norm.

In the first sum replace R_j(w-e_j) by R_j^y. Its error tends to
zero in l² uniformly for y in K and for a fixed exterior k. To see
this without assuming a monopole l² tail, fix an offset radius L.
On |w-y|<=L the coefficient difference is <=C a(L+1)p(k).
On the complement it is <=C p(k), while the centered differences
of g_N converge in l² to those of g by (10). The infinite centered
differences have arbitrarily small l² tails as L tends to infinity;
(10) transfers that tail bound uniformly to g_N. First let N tend
to infinity at fixed L and then let L tend to infinity. The error
is therefore o(1). The projection of the infinite centered derivative
onto omitted vertices has likewise vanishing l² tail, since K stays
away from all faces. This proves

    C_(R_(k,a))^T g_(N,y)
      = C_(R^y)^T g + o_(k,K)(1) in l²,                  (13)

uniformly in y, with translated infinite operators on the right.
The transpose changes the sign in both terms because C_R is skew.
All the finite left vectors are bounded in l² by C p(k), including
(12)'s coefficient-derivative term. In particular no variable
multiplier has been commuted through a Green inverse.

### 4. Freeze the finite right source and evaluate the local tensor

Fix s and y in K. On the bounded neighborhood in (6), replace u_a(s)
by u_a(s,y) and each centered exterior coefficient bar t_l/a by
its constant-link value from v_(l,a)(s,y). The coefficient error is
<=C a p(l) by the C¹ bounds in section 1. For example an opposite
mu-edge average at a plaquette center and the mu-edge vertex average
at y differ by that bound; their sample locations are a fixed number
of lattice steps apart. Under freezing they are exactly the two
constant-link coefficients v_mu+v_nu and v_nu-v_mu. The rough maps
bar B_b and the circulation D are kept fixed. Since D T=0,
bar B_b T=B_b T, also before freezing.

This replacement changes each f_mu in (6) by a finite-support vector
of l¹ norm <=C a p(l), while preserving its centered-difference
source form. Estimate (8) therefore bounds its Green-image error by
C a p(l). Section 2 applied to the finitely many centered-difference
basis sources proves

    h_(N,s,l,y)=G_infinity V_(u_a(s,y))^T
               D^T Q_(v_(l,a)(s,y)) T delta_0+o_l(1)
                                                    in l²,        (14)

uniformly in s and y. The frozen coefficients may depend on N,s,y;
this is legitimate because there are finitely many source basis
vectors, all their coefficients are bounded by C p(l), and their
convergence in section 2 is uniform. The same applies in (13).
Combining the two l² convergences and bounds gives a uniformly
vanishing diagonal error in (5).

We compute the frozen inner product to fix its sign and normalization.
Use L070's plaquette-centered Fourier convention, T=-i d,
d_j=2 sin(theta_j/2), c_j=cos(theta_j/2), H=sum d_j²,
L=H I-d d^T, and beta=L diag(c_j²)d. Its exact path identity is

    D^T Q_(v) T=2 L diag(c_j)v,
    C_(R)=-2i R.(dc).

The missing a in this path identity is deliberate: Q_(l,a)=bar Q_l/a.
L065's positive vertex-to-edge incidence has symbol +i d, so the
centered T_mu used in V=C_mu^T u T_mu has symbol +i d_mu c_mu.
Thus

    V=+i u diag(c_j²)d,   V^T=-i u d^T diag(c_j²).

This is the opposite incidence orientation to L070's separate map T.
Retaining this distinction is essential for the sign. The frozen trace
symbol in (5), with both Green factors, is therefore

    H^-1 [-2i R.(dc)] H^-1 [-i u d^T diag(c_j²)]
                                      [2 L diag(c_j)v]
          =-4u (R.(dc))(beta.(cv))/H².                    (15)

All tensor entries in (15) are integrable: its numerator is O(H²)
and H has just the one torus zero. Alternatively (13)–(14) realize
its diagonal as an l² inner product, so Plancherel applies without
an assumed monopole l² norm. L070's exact coordinate-parity and
permutation computation gives its angular integral as

    -4 gamma u R.v.                                     (16)

We reuse that already proved elementary tensor identity, not the
unproved approximation of L070's frozen diagnostic to an actual trace.
The approximation is supplied here by (8)–(14). Hence, uniformly in
s and all nonzero-source y for fixed k,l,

    b_(N,s,k,l,y)=-4 gamma u_(a,1)(s,y)
                sum_mu U_(k,a),mu(y)v_(l,a),mu(s,y)+o_(k,l)(1). (17)

Replacing R^y by U_(k,a)(y) changes (16) by O(a p(k)p(l)).
Outside K both sides vanish because the coefficient u_a is zero.
For all k,l the error in (17) is bounded by C p(k)p(l), uniformly
in N,s,y, by (8), (12), and the bounded frozen tensor. There are at
most (N-1)³ retained transverse vertices, so its summed error is
N³ times a uniformly vanishing quantity for each fixed pair k,l.

### 5. Restore all levels and the complete exterior heat sum

Let rho_(k,l,N) denote the supremum of the absolute diagonal error
in (17). Then rho_(k,l,N)->0 for each fixed pair and
rho_(k,l,N)<=C p(k)p(l). From (5), (17) and (1), exactly,

    J_(i,N)-2 gamma a^-3 D_(i,a)
       =-(a²/2) sum_(k,l)c_(i;kl) sum_s s sum_y error_(N,s,k,l,y).

Its a³-scaled absolute value is at most

    C a^5 N^5 sum_(k,l)|c_(i;kl)|rho_(k,l,N).             (18)

Here sum_s s<=N²/2, the vertex count is at most N³, and aN=8.
Thus the prefactor is bounded independently of N. At any fixed
finite exterior index cutoff, the sum on the right tends to zero.
The uniformly vanishing polynomially heat-weighted tails from section
1 control the complement independently of N. Sending the cutoff to
infinity proves (2), with every axial level and exterior heat index
retained. It also bounds D_(i,a) uniformly through (1) and (4), since
a^4 counts the physical four-volume and sa<=8.

L078's remainder has magnitude <=C_i N², whose a³-scaled value is
O(N^-1); adding it proves (3). No quantitative rate was extracted
from the energy projection or the differentiated-source approximation.
In particular the o(N³) error in this proof need not be O(N²).

### 6. Scope and qualifications

Equation (2) resolves the leading-scale identification of an existing
finite diagnostic with this selected actual trace. It never replaces
Sigma_T by a zero-axial-frequency inverse: L078 first canceled the
complete co-closed covariance exactly. The present proof starts only
from that exact reduced trace. It does not drop the upper Dirichlet
correction independently or reopen ATTEMPTS/024–025's stopped routes.
The finite spectral cutoff is an auxiliary l² approximation whose
entire tail is bounded by (9), then removed, rather than a truncation
of the actual contraction. The zero source outside the coefficient
support retains all actual boundary rows.

L073's N=24 enclosure and L070's sampled values remain finite-mesh
evidence. No sign or limiting coefficient is imported from them.
The continuum limit/evaluation of D_(i,a), centered path/path,
a²-scaled centering defect and L078 remainder, all nine placements,
other/other cubic terms, action/measure/insertion/flow corrections and
nonlinear forest compensation remain unresolved. Overlapping quartic
and cubic groups must still be combined by subtracting the shared
quartic once. No cutoff logarithm, finite matching constant, interacting
comparison <=c_box/2, continuum fields, reflection positivity, infrared
control or finite positive physical mass is established.

The standard named Weierstrass approximation theorem and the spectral
theorem are used only for the bounded continuous functional calculus
in section 2. The existing primary-source flow renormalizability and
stress-matching statements in the saved assessment retain their stated
hypotheses; they assign no coefficient here and are not reproved.
The specialization is necessary because those sources do not estimate
this exact endpoint/path composition in the all-face pinned box.

## Mathlib

Coverage of the full specialized pinned-trace result: **not checked**.
Supporting real spectral calculus, Weierstrass approximation, finite
sine diagonalization, Hilbert-space projections, Plancherel and l²
Cauchy–Schwarz: **not checked**. No full matching theorem or absence
claim is asserted. General perturbative field-theory inputs remain
precisely cited and qualified in
`drafts/literature/2026-09-26-current-target.md`.
