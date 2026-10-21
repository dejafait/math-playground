# L229 — Two-sided massive boundary transfer and the co-closed-sector rate

## Hypotheses

Use L088--L090 and L225--L228's SU(2) Gaussian on the relative
all-face cube, straight lower-rooted direction-1 forest, admitted even
N, a=8/N, tau=1/16 and actual probes i=3,6. The bare expansion is
fixed-mesh first. All norms use ordinary stored coordinates. Keep
both generator orientations, all axial levels, coincident plaquettes,
relative normal end edges, constant component modes, both residual
subtractions and the complete external heat sum.

Use precisely L228's compact Lipschitz extensions of the actual
normalized exterior columns, its whole-grid H_k and G, and its
whole-grid factor X_k. Let iota:E_N -> l2(Z^4;R^3) embed the finite
interior-level transverse links by zero. Write superscripts f and b
for finite relative and whole-grid operators. At the masses

    epsilon=N^-1, delta=N^(-4/3),
    R^s=(Delta_E^s+epsilon I)^(-1),
    Q^s=I-T^s(Delta_0^s+delta I)^(-1)(T^s)*,
    X_k^s=Q^s H_k^s R^s (Q^s)^2,       s=f,b,             (1)

the transverse incidence and vertex inverse in Q act independently
at each axial level. Thus X_k^f=H_k^delta K_(epsilon,delta) in L226,
because Q^f commutes with R^f, and X_k^b=X_k in L228. The symbol Q
here denotes the positive-mass contraction, not the exact projection.

Choose a fixed compact physical interior neighborhood of all input
and output rows of G, and let chi be its diagonal selector on the
whole-grid transverse links. For sufficiently large N, its rows lie
at least cN index steps from every physical end, for some fixed c>0,
rank(chi)<=C N^4, and

    G=chi G chi=iota G0 iota*.                           (2)

Existence follows from L009's compact displacement and fixed-range
generator stencils. L228's extensions agree with all original existing
link samples; no extension across the pinned upper zero is assumed.
Constants may depend on this fixed neighborhood. Enlarge the common
polynomial p(k) so L088's complete heat envelope still bounds it.

## Conclusion

For all sufficiently large admitted N, both localized comparisons hold:

    ||chi(iota X_k^f iota*-X_k^b)||_HS
      +||(iota X_k^f iota*-X_k^b)chi||_HS
                                      <=C p(k) N^-10.   (3)

This is stronger than L228(23)'s required
C p(k)sqrt(N)log(eN)^2. Every finite and whole-grid covariance input
row remains in (3). Consequently

    |T_(N^-1,N^(-4/3))-T_bulk|<=C_i N^-8,               (4)
    |T_hh|<=C_i N^(5/2)sqrt(log(eN))
           <=C_i N^(5/2)log(eN)^2.                      (5)

The sharp negative powers in (3)--(4) are merely a convenient choice
of polynomial accuracy, not optimized rates. The surviving allowance
in (5) comes from L226's mass/projection comparison. This establishes
the proposed rate for this complete rough sector, relative to imported
L225--L228 and their analytic premises. Their separate critical audits
remain pending. The separate audit in proof section 5 accepts this
boundary transfer and assembly relative to those imports.
No complete-response remainder, quadratic coefficient,
logarithmic coefficient, interacting reflected error <=c_box/2,
continuum axioms or finite positive mass follows. There is no
Yang--Mills construction candidate.

## Proof

### 1. Reuse a uniform scalar inverse approximation

We import L205(2), (9)--(10), (14), only for its scalar Chebyshev
polynomials, not for its different covariance/prefix trace. Explicitly,
for 0<mu<=1 and m>=1 let

    r_(m,mu)(t)=T_m((8+mu-t)/8)/T_m(1+mu/8),
    p_(m-1,mu)(t)=(1-r_(m,mu)(t))/t.

L205 verifies polynomial divisibility, degree at most m-1, and

    sup_(mu<=t<=16+mu)|1-t p_(m-1,mu)(t)|
          <=eta_mu=2 rho_mu^m<=2 exp(-m sqrt(mu)/3).      (6)

The needed specialization is that every scalar component of Delta_E^f,
Delta_E^b and Delta_0^f,Delta_0^b has spectrum in [0,16]. For the
finite relative operators this follows from L003, proof section 2:
the component Laplacian is a sum of four interval Laplacians, each
with spectrum in [0,4]; the transverse vertex Laplacian has three
such terms. The edge interval retains its normal end diagonals and
constant mode. The corresponding whole-grid scalar Fourier symbols
are sums of four, respectively three, quantities 4sin^2(theta_j/2),
so the same interval applies. No component boundary condition is
changed to obtain it. The bounded self-adjoint spectral theorem
(equivalently Fourier Plancherel on the whole grid) therefore gives

    ||(D+mu I)^(-1)-p_(m-1,mu)(D+mu I)||
                                                 <=mu^-1 eta_mu. (7)

This applies also when D has zero spectrum: the mass is strictly
positive. It is an operator-norm estimate on all input rows, not a
finite-volume limiting assertion. The general polynomial residual
is already proved in L205; only its applicability to these two
different rectangular cochain settings is needed here.

Set

    m=ceil(60 N^(2/3)log(eN)), eta=2(eN)^(-20).          (8)

Since delta<=epsilon and m sqrt(delta)>=60log(eN), (6) gives
eta_epsilon,eta_delta<=eta. All errors below are uniform before
this degree and mass choice; no fixed-degree limit is invoked.

### 2. Approximate the complete ordered factor, including every Q

On each finite or whole-grid space put

    Z_E^s=p_(m-1,epsilon)(Delta_E^s+epsilon I),
    Z_0^s=p_(m-1,delta)(Delta_0^s+delta I),
    Qtilde^s=I-T^s Z_0^s (T^s)*,
    Y_k^s=Qtilde^s H_k^s Z_E^s (Qtilde^s)^2.           (9)

The vertex inverse acts slice by slice, with exactly the same axial
identity as in (1). In particular no inverse on the infinite axial
identity factor is being approximated. Since ||T^s||^2<=12, (7) gives

    ||R^s-Z_E^s||<=N eta,
    ||Q^s-Qtilde^s||<=12N^(4/3)eta=:alpha.             (10)

The finite relative intertwining and the whole-grid Fourier symbol
show ||Q^s||<=1. Alternatively, T(Delta_0+delta)^(-1)T* has
eigenvalues lambda/(lambda+delta) on the gradient range and zero
on its complement. Thus ||Qtilde^s||<=1+alpha<=2 and
||Z_E^s||<=N(1+eta)<=2N, for N>=2 with (8).

Bounded row and column multiplicity in L089(1), and its actual
coefficient bounds, imply

    ||H_k^f||+||H_k^b||<=C a p(k).                     (11)

For the bulk version use the same bound on L228's extensions; their
finitely many shifts do not change the supremum estimate. For the
finite version this estimate includes all end rows. Now telescope
the four changed factors of Q H R Q Q in their original order.
The three Q changes cost at most C a p(k)N alpha together, and
the R change at most C a p(k)N eta. Therefore

    ||X_k^s-Y_k^s||<=C p(k)N^(4/3)eta.                (12)

Only aN=8 and the operator norms just established are used here.
No multiplier, projection, inverse or component selector is commuted
past H. Self-adjointness of the polynomial inverses is available but
not required for this telescoping bound.

### 3. Exact polynomial comparison from either interior endpoint

The polynomial Z_E has graph range at most m-1. The transverse
vertex polynomial Z_0 also has range at most m-1, and each incidence
on its ends adds at most one step. Consequently Qtilde has range
at most m+1. Let r_H be a fixed range bound for the complete H,
including all component shifts in its four terms. Every term in
Y_k, or its adjoint, has total range at most

    L=3(m+1)+(m-1)+r_H=4m+2+r_H=o(N).                 (13)

Range counts refer to integer cochain indices; fixed half-cell
staggering offsets are included in r_H and the endpoint allowance.
For large N, L is smaller than the cN margin of chi, with a fixed
additional allowance for all local stencil samples.

Expand (9) into products of incidences, Laplacian powers, identities
and the actual local H terms. Starting at any chi output row, every
intermediate index in each product lies within L plus that allowance.
All of these indices are in the physical interior. There the finite
relative component and vertex Laplacians have exactly the same
nearest-neighbor entries as the whole-grid ones; their diagonal
mass terms agree too. The finite and infinite incidences and path
stencils agree. Every exterior sample in H agrees by L228's
extension prescription. Thus the weighted paths have identical
coefficients and identical endpoints, all in the finite edge space.
Even paths that backtrack or take diagonal steps obey the same
length bound. This proves the full row identity

    chi(iota Y_k^f iota*-Y_k^b)=0.                     (14)

In particular a whole-grid input outside the finite edge space
cannot be reached in such a path; (14) is not merely an equality
after restricting the input columns. Applying the same path argument
to the adjoint product, starting instead at a chi input row, gives

    (iota Y_k^f iota*-Y_k^b)chi=0.                     (15)

No symmetry of X or Y is assumed. The two orientations are compared
separately. These identities do not assert that the relative edge
Laplacian is a scalar Dirichlet compression: its genuine normal end
rows remain different, but no polynomial path in (14)--(15) reaches
them. The approximation errors (10)--(12) still include all those
rows and the constant modes.

Let D_k=iota X_k^f iota*-X_k^b. Subtract (14)--(15), apply (12),
and use ||chi B||_HS,||B chi||_HS<=sqrt(rank chi)||B||. Zero
embedding is an isometry on the finite space, so

    ||chi D_k||_HS+||D_k chi||_HS
       <=C N^2 p(k)N^(4/3)eta
       <=C p(k)N^(-50/3)<=C p(k)N^-10.                (16)

This proves (3). For the right restriction B chi may have infinitely
many output rows; its finite input rank suffices for the same ideal
inequality. Thus this proof does not discard a tail of covariance
sources or infer a relative comparison from a whole-grid tail alone.

### 4. Transfer both original traces and assemble the sector rate

L226(13) and L228(4) give, at the current masses,

    ||X_k^f||_HS+||X_k^b||_HS<=C p(k)N.               (17)

For the bulk bound, use epsilon^-1/2=sqrt(N) in L228(4), uniformly
in delta. In both spaces the trace is L228(14)'s exact expression

    -(1/2)sum_(k,l)c_(i;kl)
       {Tr((X_k^s)* G^s (X_l^s)*)
                       +Tr(X_k^s (G^s)* X_l^s)},     (18)

with G^f=G0 and G^b=G. This rearrangement uses skew-adjointness
of Q H Q, with the same factor 1/2 and both original orientations.
Embed the finite products by iota; their finite traces are unchanged.
By (2), the embedded generator equals the bulk one.

Telescope the two X factors in each trace of (18). In the first
orientation, the changed adjoint immediately to the left of G uses
||D_k* chi||_HS=||chi D_k||_HS; the changed adjoint on the right
uses ||chi D_l*||_HS=||D_l chi||_HS. In the second orientation
the changed factors use ||D_k chi||_HS and ||chi D_l||_HS,
respectively. With ||G||<=CN, (3) and (17) bound their sum by
C p(k)p(l)N^-8. The complete bound
sum|c_(i;kl)|p(k)p(l)<=C_i proves (4). One can first take symmetric
finite heat squares; these absolute bounds justify the full sum.

Finally L228(5) bounds T_bulk by C_i N^(5/2), and L226(3) bounds
T_hh-T_(N^-1,N^(-4/3)) by C_i N^(5/2)sqrt(log(eN)). Add these
two estimates and (4) to obtain (5). If a bound over every admitted
mesh rather than sufficiently fine meshes is desired, enlarge the
constant over the finitely many smaller N, using L088(2). No
effective numerical value of that enlarged constant is claimed.

This is REPRODUCTION under the unchanged ready quantitative-sector
assessment: it applies L205's already proved scalar polynomial
residual, the standard self-adjoint spectral theorem, finite-path
propagation and Hilbert--Schmidt ideal inequalities to a different
ordered product. No general decay theorem is reproved. L205's old
covariance-leg comparison is not asserted for this product without
the new argument above. ATTEMPTS/030's fixed-mass warning and
L109/ATTEMPTS/032's first absolute-moment obstruction remain valid;
neither premise is used. All checks are analytic, with no numerical
certificate or mathematical script. Local progress is a complete
sector bound relative to the stated imports, not a novelty claim,
an upstream audit or a Yang--Mills resolution.

### 5. Separate critical audit of the boundary transfer and assembly

Audit dated 2026-10-18, performed after the proof above was completed.
Verdict: accept (3)--(5) relative to the stated L225--L228 inputs.
This verifies the boundary argument and its use of those inputs; it
does not independently certify their spectral or bulk estimates.
No new rate or mathematical input is claimed by this audit.

First fix the normalization implicit in (6)--(7). Delta_E, Delta_0
and T use the dimensionless incidences of L090, not L003's
physical derivative D_a. On one interval the incidence is
delta=a D_a, with (delta f)_j=f_(j+1)-f_j and pinned vertex values
f_0=f_N=0. The vertex matrix delta*delta has diagonal 2 and
off-diagonal -1. The edge matrix delta delta* has diagonal 1 at
the first and last edge, diagonal 2 elsewhere, and off-diagonal -1.
In particular its constant edge vector has eigenvalue zero; no end
row is replaced by a scalar Dirichlet row. L003's tensor calculation,
after this rescaling, gives the interval spectrum in [0,4] and thus
the common [0,16] interval used here. The transverse vertex operator
has only three interval factors and norm at most 12. Its axial factor
is the identity on the interior levels; it is not a four-dimensional
vertex inverse. These are precisely the spaces in (1) and (9).

The imported L205 residual is applicable to both finite and infinite
bounded self-adjoint operators. Substitution t=0 gives r_(m,mu)(0)=1,
so p is a polynomial even though its displayed definition divides by
t. On [mu,16+mu] the numerator's Chebyshev argument is in [-1,1].
The positive denominator and L205(14) give (6), including for a
component with zero unregularized spectrum. At the selected degree,
m sqrt(delta)/3>=20 log(eN), and epsilon>=delta, so the same eta
bounds both residuals. The three Q errors are each at most
12 delta^-1 eta; the R error is at most epsilon^-1 eta. Telescoping
Q H R Q Q therefore bounds the operator error by

    C a p(k) epsilon^-1(delta^-1 eta+eta)
                         <= C p(k) N^(4/3)eta.

This recounts all three Q factors separately. No Q is made idempotent
at positive mass, and none is commuted through H. The finite H bound
follows from L088(5), L089(1) and bounded stencil multiplicities;
the whole-grid bound uses L228's extension supremum. Smoothness of
that extension is unnecessary for the boundary comparison itself.

For the path-domain check, the transverse component mu uses vertex
indices 1,...,N-1 in the axial and the other two transverse directions,
and edge indices 0,...,N-1 in direction mu. T connects the slice
vertex space to these three rectangular edge spaces. Away from the
ends all component Laplacians have diagonal 8 and the usual eight
neighbor entries -1; the slice vertex Laplacian has diagonal 6 and
six neighbor entries -1. Both incidences have the same two signed
entries as their infinite counterparts. Consequently every elementary
factor agrees in the interior, with the appropriate component index
and staggering. The incidence ends of each Q polynomial contribute
two extra steps: range at most (m-1)+2=m+1. The product and its
adjoint both have range at most 4m+2+r_H. Since

    (4m+2+r_H)/N=O(N^(-1/3)log(eN)) -> 0,

every intermediate edge, vertex and plaquette index starting from
chi remains strictly interior for sufficiently large N. Local samples
in H agree there by the extension prescription, regardless of their
variation within that neighborhood. The path comparison from the
output gives (14); applying it to the reversed adjoint product gives
(15), without assuming symmetry of X or Y. Paths from either endpoint
cannot finish outside the finite space. This proves full row/column
identities, rather than identities compressed at both ends. The end
diagonal differences above and every exterior source are still present
in the global operator error (12).

The selector has rank O(N^4), not O(N^3). Thus the two local
Hilbert--Schmidt errors are bounded by

    C p(k)N^(2+4/3)(eN)^(-20)
                         <= C p(k)N^(-50/3).

This verifies the stronger intermediate exponent in (16) and the
weaker convenient N^-10 in (3). Finite input rank proves the right
restriction estimate even with infinitely many output rows. There is
no tail truncation or factorwise absolute kernel moment assumption.

Finally write F_k=iota X_k^f iota* and B_k=X_k^b, so D_k=F_k-B_k.
Embedding preserves finite products and traces because iota*iota=I.
Compact support of the displacement and the generator's fixed range
give G=chi G chi, including both its input and output rows. The
first orientation's difference is exactly

    Tr(D_k* chi G chi F_l*)+Tr(B_k* chi G chi D_l*).

The second orientation's difference is exactly

    Tr(D_k chi G* chi F_l)+Tr(B_k chi G* chi D_l).

These display why both localized comparisons are needed. The norms
of the changed factors are respectively controlled by chi D_k,
D_l chi, D_k chi and chi D_l. Hilbert--Schmidt Cauchy--Schwarz,
||G||<=CN and the unchanged factor bound C p N give N^-8 after
using (3). All these traces are trace class. The rearrangement (18)
uses X=A K, A*=-A and K*=K: K A=-X* and A* K=-X. It retains the
minus sign in each orientation and the original factor 1/2.
L088's symmetric complete heat envelope permits absolute summation;
there is no mode cutoff or extra color factor. Imported L226(3) and
L228(5) then give (5), with L089's complete-sector remainders already
included in L226. No fixed-mass limiting theorem is evaluated at
varying mass. ATTEMPTS/030 and L109/ATTEMPTS/032 remain untouched.

The audit establishes no effective value for the asymptotic mesh
threshold or C_i, no audit of L225--L228, no complete-response rate,
and no interacting or continuum construction. All unreviewed
analytic premises remain explicit. Mathlib coverage is unchanged.

## Mathlib

Full matching two-sided relative-boundary transfer and complete
co-closed-sector rate: **not checked**. Supporting Chebyshev,
bounded self-adjoint spectral calculus, finite polynomial propagation
and Hilbert--Schmidt ideal coverage: **not checked**. Unknown
availability is not evidence of absence. L205 supplies the complete
scalar approximation proof; L003 supplies the relative tensor grids.
