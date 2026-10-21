# L228 — Ordered coefficient freezing for the co-closed bulk comparison

## Hypotheses

Use L088--L090's actual exterior heat coefficients c_(i;kl), i=3,6,
with their symmetry and complete polynomial heat envelope. Keep
SU(2), the relative all-face cube, the straight direction-1 forest,
a=8/N, admitted even N and tau=1/16 as the intended finite application.
The bare expansion is fixed-mesh first. This lemma concerns a specified
whole-grid comparison trace; it does not identify that trace with the
finite relative trace T_(epsilon,delta) of L226.

Let E_infinity=l2(Z^4;R^3), indexed by a common vertex index and the
three transverse link components. Choose real normalized exterior
extensions v_k on this grid with support in a box of O(N) side lengths,
with constants independent of k,N, and

    sup_x |v_k(x)| <= C p(k),
    |v_k(x+e)-v_k(x)| <= C a p(k).                     (1)

They agree with z_k/a on the existing component-link rows of L088,
before any pinned zero extension. Such extensions may be made by
clamping each component's rectangular index range, then multiplying
by a fixed Lipschitz cutoff in physical coordinates equal to one on
the box. The neighboring-column bounds used in L090's proof of (6)
give (1) before clamping; clamping is nonexpansive in index distance.
The cutoff has support of O(N^4) cells and differences O(a). This
construction preserves the original existing samples but does not
extend the forest potential smoothly through its pinned upper zero.
Different components keep their original staggered positions.

On the whole grid use the exact finite stencils Bb,Bq,Cc of L089(1).
For z_k=a v_k form b_k=Bb z_k, q_k=Bq z_k and

    H_k = Bq* M_(b_k) Cc - Cc* M_(b_k) Bq
                       + Cc* M_(q_k) Bb - Bb* M_(q_k) Cc.       (2)

The adjoint * is the Hilbert-space adjoint (ordinary transpose for
these real kernels). In particular H_k*=-H_k. This is the reduced
alternating factor; L089's exterior-circulation terms have not been
included or silently canceled.

Let G be the whole-grid transverse/transverse block of L009's actual
endpoint/clover generator, using its compact displacement u_a and
all its stencils. It agrees with the embedded finite G0 once those
compact stencils lie inside the box. Its normalized displacement
samples have uniformly bounded values and neighboring differences
O(a), with support in O(N^4) cells. Let R_epsilon, Q_delta and
J_j=J_(e_j,epsilon,delta), j=2,3,4, be the whole-grid convolution
operators of L227, with 0<epsilon,delta<=1. Thus R has symbol
1/(h+epsilon), Q is the transverse regularized projection, and

    K=R_epsilon Q_delta,   A_k=Q_delta H_k Q_delta,
    X_k=A_k K,
    T_bulk=(1/2) sum_(k,l)c_(i;kl) {
        Tr(A_k G K A_l* K)+Tr(A_k K G* A_l* K) }.        (3)

All variables in (3) are whole-grid operators. No finite relative
projection or covariance is replaced in the hypotheses. For positive
masses the inverses are bounded; H_k is finite rank, so these products
have well-defined traces. The estimates below also justify the full
external heat sum. Enlarge the fixed polynomial p as in L090; its
complete heat envelope remains summable.

## Conclusion

There is an exact ordered expansion

    X_k = F_k+E_k,      F_k=a sum_(j=2)^4 M_(v_kj) J_j,
    ||F_k||_HS <= C p(k) N,
    ||E_k||_HS <= C p(k)[epsilon^(-1/2)
                                      +sqrt(log(e/epsilon))].   (4)

The bounds are uniform in delta. In particular at epsilon=N^-1,
for every 0<delta<=1, including delta=N^(-4/3),

    |T_bulk| <= C_i N^(5/2).                           (5)

This is below the requested O(N^(5/2)log(eN)^2) sector threshold,
but it is only the bulk comparison. The actual finite trace still
requires a relative-boundary comparison at that threshold. L225--L227
and their upstream inputs remain imported, with separate critical
audits pending. The separate critical audit in proof section 7 accepts
this bulk estimate relative to those imported inputs.
No complete-sector rate, complete-response rate, interacting reflected
error <=c_box/2, continuum axioms or finite positive mass follows.

## Proof

### 1. A squared projection moment, with no absolute moment premise

Write Q=Q_delta in this proof. In component-center phases L227(7)
gives, for a transverse derivative and r=sqrt(lambda),

    ||partial Q^c|| <= C r/(r^2+delta).

Conjugation to integer-index phases adds a uniformly bounded term,
since the phase derivative is bounded and Q^c is a contraction.
The integer-index symbol is smooth and periodic at positive delta,
as checked in L227. Its axial derivative is zero. The three-dimensional
frequency integral of its squared derivative is bounded uniformly:
near zero it is bounded by a constant times

    integral_0^C r^2 [1+r^2/(r^2+delta)^2] dr <= C',

because r^4/(r^2+delta)^2<=1; away from zero it is bounded directly.
Fourier-series Plancherel therefore gives, for its kernel q(z),

    sum_(z in Z^4) |z|^2 ||q(z)||_F^2 <= C.             (6)

The kernel is supported on z_1=0, so the extra axial dimension adds
no factor. The identity part at z=0 contributes zero to (6).

Here is a useful global, rather than output-restricted, commutator
consequence. If a common-index scalar b has at most C N^4 nonzero
cells, sup|b|<=B and differences |b(x)-b(y)|<=a L|x-y|_1, then

    ||[Q,M_b]||_HS <= C a L N^2.                       (7)

Indeed for each displacement z a nonzero difference requires x or
x-z in the support of b, giving at most 2C N^4 cells. Bound the
squared difference by C a^2 L^2 |z|^2 and sum using (6).
All input and output rows are included. This is a squared kernel
moment and does not contradict L109's failed first absolute moment.

The same support-count argument with L227(3) gives

    ||[J_j,M_b]||_HS + ||[J_j*,M_b]||_HS
                         <= C a L N^2 sqrt(log(e/epsilon)),
    ||M_b J_j||_HS + ||J_j M_b||_HS <= C B N^2.        (8)

The second bound uses the unweighted squared kernel norm, not an
operator norm. It holds also for J_j*. It does not require b to be
smooth between sample points. Telescoping coordinate differences is
sufficient for the displayed index Lipschitz bound.

### 2. Expose the joint product in its exact order

Let Omega_j denote L227's complete frozen normalized alternating
stencil for exterior e_j, in integer-index phases. Freezing only the
finitely many coefficient samples in a row of (2) at that row's common
vertex gives the exact decomposition

    H_k = a sum_j M_(v_kj) Omega_j + D_k.               (9)

The remainder D_k is a finite-range matrix with bounded row/column
multiplicity, at most C N^4 nonzero rows, and entries bounded by
C a^2 p(k). To verify this claim, each term of (2) has one exterior
coefficient, itself the sum or difference of two link samples, and
one fixed path and circulation stencil. Every contributing exterior
sample lies a uniformly bounded index distance from the output row.
Replacing it by the corresponding component of a v_k at that row
costs O(a^2 p(k)) by (1). For the terms with Cc* on the left, its
finite offsets also precede this replacement and obey the same bound.
After replacement, b/a=v_mu+v_nu and q/a=v_nu-v_mu. L088(11)--(13)
then gives exactly Omega_v, with both paths and all planes retained.
This establishes (9) without commuting a component selector past Q.
The original staggered offsets are precisely part of D_k.

The four-dimensional Fourier integral satisfies

    integral (h+epsilon)^(-2) <= C log(e/epsilon).      (10)

This is the radial estimate in L227(11). Applying it to each of the
boundedly many translated scalar resolvent rows in D_k R gives

    ||D_k R_epsilon||_HS <= C a^2 p(k) N^2
                                    sqrt(log(e/epsilon))
                            <= C p(k)sqrt(log(e/epsilon)).       (11)

There is no infinite-volume Hilbert--Schmidt norm assigned to R alone;
D_k restricts its nonzero output rows before the estimate.

Since Q commutes with the scalar R and is a contraction, (9) yields
exactly

    X_k = Q H_k R Q^2
        = a sum_j M_(v_kj) Q Omega_j R Q^2
          + a sum_j [Q,M_(v_kj)] Omega_j R Q^2
          + Q D_k R Q^2.                               (12)

The first line on the right is F_k, because Q Omega_j R Q^2=J_j.
L227(8) gives ||Omega_j(theta)||<=C sqrt(h), hence

    ||Omega_j R||_op <= C epsilon^(-1/2).              (13)

Equations (7), (11)--(13) bound the last two terms by
C p(k)[a^2 N^2 epsilon^(-1/2)+sqrt(log(e/epsilon))].
Since aN=8 this proves the error part of (4). Equation (8) proves
its F part. No projection is moved through Omega_j, and only a
common scalar crosses the leftmost Q, with its exact commutator
retained. The derivative in Omega_j is kept next to R in (13).
At epsilon=N^-1, (4) gives ||X_k||_HS<=C p(k)N and
||E_k||_HS<=C p(k)sqrt(N), uniformly in delta.

### 3. Retain both original generator orientations

Skew-adjointness of A_k and symmetry of K give X_k*=-K A_k.
Cyclically arranging (3), with no k,l identification, gives

    T_bulk=-(1/2) sum_(k,l)c_(i;kl) {
                 Tr(X_k* G X_l*)+Tr(X_k G* X_l) }.     (14)

For example K A_k=-X_k* and K A_l*=X_l* give the first term;
A_l* K=-X_l gives the second. Both minus signs are thus fixed by
the original trace rather than by a frozen-symbol convention.
The bounded stencil of G gives ||G||<=CN, as in L090(2).
Replacing the two X factors by F in either term of (14), telescoping
one at a time, costs at most

    C p(k)p(l) N * N * sqrt(N)
                                  =C p(k)p(l)N^(5/2). (15)

These estimates use the global Hilbert--Schmidt norms, so they require
no unsupported compactness assertion about the projected outputs.

Let W_r be the constant-coefficient normalized generator for unit
displacement in direction r=1,2,3,4, restricted to its transverse
input/output block. L009(3) is linear in displacement samples; moving
its finitely many endpoint samples to the output's common vertex gives

    G = G_f + D_G,
    G_f=a^(-1) sum_r M_(u_r) W_r,
    ||D_G||<=C.                                       (16)

Here u_r is a real common-index displacement sample. The original
sample shifts cost O(a) before the factor a^-1; bounded row/column
multiplicity proves the norm bound. Each W_r keeps the complete
clover and endpoint filters of L088(14), is a periodic finite-stencil
matrix, and in component-center phases has symbol i times a real
matrix. Its operator norm and first symbol derivatives are bounded.
All coefficient supports in (16) have O(N^4) cells. Transposing (16)
retains W_r* M_(u_r) in that order. Replacing G by G_f in the trace
with the F factors costs at most C p(k)p(l)N^2.

### 4. Collect common scalars using only joint commutators

After (15)--(16), each k,l,j,t,r term in the first trace of (14),
including its outside powers of a but temporarily excluding -1/2
and c_(i;kl), is

    a Tr(J_j* M_(v_kj u_r) W_r J_t* M_(v_lt)).         (17)

Cycle M_(v_lt) to the front, then commute M_(v_kj u_r) through
J_j*. The resulting main term is

    a Tr(M_(v_kj v_lt u_r) J_j* W_r J_t*).             (18)

For the error, use the cyclic order
Tr([J_j*,M_(v_kj u_r)] W_r J_t* M_(v_lt)). The commutator in (8)
has norm at most C p(k)N sqrt(log(e/epsilon)), while J_t* M_(v_lt)
has norm at most C p(l)N^2. Consequently the error in (17) is at
most C p(k)p(l)N^2 sqrt(log(e/epsilon)).

The second trace in (14) instead has the order

    a Tr(M_(v_kj) J_j W_r* M_(u_r v_lt) J_t).           (19)

Commute its middle scalar through the complete J_j W_r*, leaving

    a Tr(M_(v_kj u_r v_lt) J_j W_r* J_t).              (20)

This commutator has the same bound as (8). For a detailed check,
the periodic symbol J_j W_r* has squared L2 norm bounded by C and
squared first-derivative L2 norm bounded by C log(e/epsilon), by the
product rule, the bounded W_r and its derivatives, and L227(3).
Plancherel followed by the support count proving (8) applies to
this joint product. It does not move W_r* through J_j or through Q.
Cycle the error to pair that commutator with J_t M_(v_kj), whose
Hilbert--Schmidt norm is at most C p(k)N^2. This gives the same
C p(k)p(l)N^2 sqrt(log(e/epsilon)) bound for (19).

All scalar products just used have the required compact support and
index Lipschitz bounds, by (1) and (16). Each closed main trace in
(18),(20) has a finite-row scalar multiplier, so its diagonal is
exactly the full-torus integral of the convolution product's matrix
trace, multiplied by that scalar at the row index. All three component
diagonals use the same scalar; no individual component trace is
declared zero. The kernels are square summable and W is bounded,
so their diagonal products and these finite-row traces are justified
by Cauchy--Schwarz.

### 5. Cancel the complete frozen trace and sum the heat envelope

At each cell x the sum of (18),(20) over j,t,r is exactly the
frozen two-orientation trace with exterior vectors v_k(x),v_l(x)
and displacement u(x), using the same Q_delta and R_epsilon.
One may verify this directly by writing
A_v=Q Omega_v Q, K=R Q and J_v=A_v K in (14).
In center phases A_v=i S_v with S_v real symmetric and K real
symmetric. The effective generator line is

    (G_frozen K+K G_frozen*)/2
          = (i R/(2a))(W Q-Q W^T),                    (21)

where W is real and linear in u(x). Thus it is i times a real
antisymmetric matrix. The real symmetric exterior coefficients obey
c_(i;kl)=c_(i;lk). For real symmetric S_k,S_l,K and antisymmetric Z,

    Tr(S_k Z S_l K)=-Tr(S_l Z S_k K),                  (22)

by transposition and cyclicity. This is precisely L090(18)--(21),
now used at arbitrary positive masses; it is an algebraic identity,
not its fixed-mass limit theorem. The unitary component-center phases
cancel in the closed matrix trace. Equations (21)--(22) cancel the
sum at every cell and frequency, including zero transverse frequency,
where Omega vanishes. No equal-level or continuum approximation is
used in this cancellation.

At epsilon=N^-1 the remaining trace errors are (15), the O(N^2)
generator error, and the O(N^2 sqrt(log(eN))) errors in section 4.
They are all at most C p(k)p(l)N^(5/2) for N>=2. The complete bound
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i from L088/L090 proves (5) for both
actual probes. Symmetric finite heat squares can be used first;
these absolute envelopes then justify removing the external cutoff.
Both orientations, every path and generator filter, and the actual
finite-mesh heat coefficients have been retained.

### 6. What remains before the finite-sector rate follows

The constructed extensions are comparison data, not the relative
boundary law. In particular (6)--(12) are whole-grid estimates and
do not bound Q_delta^finite-Q_delta^infinity or the corresponding
resolvent difference. Let iota embed the original finite transverse
edge space by zero into the whole-grid space, and let chi select a
fixed physical interior neighborhood containing every input and output
row of G. With X_k^finite=A_k^finite K^finite in L226's original order,
a sufficient new comparison would be both

    ||chi(iota X_k^finite iota* - X_k)||_HS,
    ||(iota X_k^finite iota* - X_k)chi||_HS
                              <= C p(k)sqrt(N)log(eN)^2.        (23)

Both sides are needed because (14) contains both orientations and
adjoints. At the schedule epsilon=N^-1, delta=N^(-4/3), the finite
X norms are O(p(k)N) by L226, and the bulk ones by (4). Since
G=chi G chi and ||G||<=CN, telescoping (14) would turn (23) into
O(N^(5/2)log(eN)^2) trace error. L226(3), including L089's discarded
exterior-circulation and both curvature-form contributions, would
then give the proposed complete T_hh bound. Inequalities (23) are
unproved here. An infinite-grid tail alone does not establish them;
all finite relative source rows and staggered boundary conditions
must be compared, without a smooth pinned-zero extension.

This is a REPRODUCTION under the unchanged ready quantitative-sector
EXPLORE assessment. The standard inputs are Fourier-series Plancherel,
finite-stencil product differences, Hilbert--Schmidt trace inequalities
and the already proved frozen identity. The local specialization is
the ordered decomposition (12) and both subsequent trace placements;
no general decay theorem is reproved. L113 concerns a different finite
projection placement and is not used as an input. L109's absolute-
moment obstruction and ATTEMPTS/030's limit-order warning remain valid.
No claim of originality beyond the sources checked is made.

### 7. Separate critical audit of the ordered bulk estimate

This audit checks sections 1--5 under the unchanged quantitative-sector
assessment. It imports L227's two squared kernel estimates, L226's
finite comparison and the stated upstream analytic premises. It does
not audit L225--L227 or add a new rate. The claimed bulk estimate (5)
is accepted relative to those inputs, for the following reasons.

**Actual samples and global commutators.** L028(10)--(11) controls
the smooth retracted exterior on existing interior-level rows, and
L090(6) retains the last neighboring levels and transverse end rows.
Thus the componentwise clamping in the hypotheses uses existing
samples, with no crossing of the upper pinned zero. A physical cutoff
adds only O(a p(k)) neighboring differences to the normalized column.
The same common-index scalar acts on all three components only after
(9)'s local freezing error has been retained. That error has O(N^4)
rows, fixed propagation range and O(a^2 p(k)) entries.

For Q's squared moment, its axial kernel is supported at zero axial
offset. In the three transverse dimensions the derivative integral
in section 1 has radial integrand r^4/(r^2+delta)^2<=1, apart from
the bounded phase term. It is uniform in delta. The global support
count for a scalar difference uses the union of its support and its
translate, of at most C N^4 cells at each offset; it imposes no
restriction on either input or output individually. Applying the same
count to L227's complete J and J* proves exactly the global versions
(8) required here. No first absolute kernel moment is invoked.

**Inner projection and powers of N.** Starting from A_k K, commutation
of R with Q gives Q H_k R Q^2. Substitution of (9) then moves only
M_(v_kj) past the leftmost Q; the residual term is precisely
 a[Q,M_(v_kj)] Omega_j R Q^2. Its norm is at most
 C p(k) a^2 N^2 epsilon^(-1/2), by (7) and (13).
The other residual is Q D_k R Q^2, bounded by (11), not by a
nonexistent whole-grid Hilbert--Schmidt norm of R. Hence at epsilon=N^-1,

    ||F_k||_HS+||X_k||_HS<=C p(k)N,
    ||X_k-F_k||_HS<=C p(k)sqrt(N).

No factor involving delta is lost. The O(a^-1) generator times one
O(N) factor and one O(sqrt(N)) error gives O(N^(5/2)); telescoping
with X on the unchanged side includes the error/error contribution.
The shifted displacement remainder D_G has bounded operator norm,
and therefore contributes O(N^2).

**Two cyclic orders and scalar placement.** In the first original
trace, K A_k=-X_k* and K A_l*=X_l*, giving
 -Tr(X_k* G X_l*). In the second, A_l* K=-X_l, giving
 -Tr(X_k G* X_l). These identities require skew-adjointness of A_k,
not commutation with K. For the first F trace its scalar order is
 J_j* M_(v_kj u_r) W_r J_t* M_(v_lt), with outside factor a.
Cycling the last scalar to the front exposes exactly
 [J_j*,M_(v_kj u_r)], paired with W_r J_t* M_(v_lt).
For the second order it is
 M_(v_kj) J_j W_r* M_(u_r v_lt) J_t. Its error is exactly the
commutator of J_j W_r* with M_(u_r v_lt), paired after cycling
with J_t M_(v_kj). The product derivative estimate for J_j W_r*
uses both of L227(3)'s norms and the bounded symbol and derivative
of W_r*. Thus both errors are at most
 C p(k)p(l) a(N sqrt(log(e/epsilon)))N^2,
which is C p(k)p(l)N^2 sqrt(log(e/epsilon)). No component stencil
or generator is commuted through Q.

**Full frozen cancellation.** After scalar collection, the row scalar
is the same on all component diagonals. Summing j,t,r therefore
reconstructs the original two-orientation frozen trace with independent
real vectors v_k(x),v_l(x). In center phases write
 A_k^fr=ia S_k, with S_k=Q S_(v_k) Q real symmetric,
 G^fr=(i/a)W, with W real, and K=R Q real symmetric.
The middle line of the original trace is iZ, where
 Z=R(WQ-QW^T)/(2a) is real antisymmetric.
The trace is consequently i a^2 Tr(S_k Z S_l K).
Transposition and one cyclic shift give its negative with k,l
interchanged. The actual coefficients c_(i;kl) are real symmetric,
so the full sum vanishes pointwise. This does not set either original
generator orientation to zero separately, or require Q^2=Q. Positive
mass defines the symbols at zero; Omega is zero there. Integer-index
phases disappear only in this closed trace.

The surviving mode-pair errors are bounded by
 C p(k)p(l)[N^(5/2)+N^2+N^2 sqrt(log(eN))].
Their complete heat sum is O_i(N^(5/2)) by L088(5), with symmetric
finite heat squares used before taking the full sum. This checks
both actual probes without numerical or continuum-coefficient premises.
The DAG row already contains every direct mathematical input used in
this audit; L109 and the recorded failed approaches serve as contrasts.
Sections 1--6 are preserved. Section 6's relative-boundary obligation
is separate from this bulk validation. No complete-response estimate,
interacting construction or finite physical mass follows. Mathlib
coverage remains not checked.

## Mathlib

Full matching result: **not checked**. Supporting Fourier-series
Plancherel, Hilbert--Schmidt commutator and trace, and finite-stencil
operator coverage: **not checked**. Unknown availability is not evidence
of absence. This analytic bulk estimate uses no numerical certificate.
