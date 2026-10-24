# L274 — Boundary transfer of the ordered exterior-circulation static trace

## Hypotheses

Use exactly L273(3)'s U_(i,N;epsilon,delta), L123(5)'s E_(i,N)^f
and L123(2)'s K_(i,f). Thus i=3,6 are both actual SU(2) probes,
the box is (-4,4)^4 with relative pinned links, the direction-1 forest
is straight and lower rooted, N is sufficiently large, admitted and
even, a=8/N, tau=1/16, and coordinates are ordinary stored ones.
Take the bare coefficient at fixed mesh before refinement. Retain all
relative source/end rows, allowed constant component indices, original
path and generator filters, and the complete finite-mesh heat sums.
All imported audit qualifications remain; this is not an upstream audit.

Write superscripts f,b for the finite transverse relative spaces and
the whole transverse grids. The latter are V_b=l2(Z^3),
E_b=l2(Z^3;R^3), F_b=l2(Z^3;R^3), with L123's actual lower-vertex
indices and staggered component positions. Let d_j:V_j->E_j and
D_j:E_j->F_j be gradient and circulation, and put

    R_epsilon^j=(Delta_j+epsilon I)^(-1),
    P_delta^j=d_j(d_j* d_j+delta I)^(-1)d_j*,
    Q_delta^j=I-P_delta^j,                    j=f,b.       (1)

Here Delta_f is the actual relative edge Hodge Laplacian; Delta_b
is its interior translation-invariant stencil, not a finite scalar
Dirichlet replacement of every edge component.

The bulk deterministic matrices are defined without freezing. For
each original level s and retained heat label k, extend each actual
plaquette scalar array f_k/a^2, b_k/a, q_k/a by zero off its existing
finite plaquette index set. Denote those extensions h_k, bbar_k,qbar_k.
Using the original infinite-grid two-edge path maps, set

    Cbar_k^b=B_b* M_(h_k) B_q-B_q* M_(h_k) B_b,
    Fbar_k^b=B_q* M_(bbar_k)-B_b* M_(qbar_k).             (2)

The finite matrices Cbar_k^f,Fbar_k^f remain L273(1). Formula (2)
agrees with them on every stencil strictly inside the box. It assigns
no smoothness to a zero extension at a pinned face. Use exactly
L111(1)'s bulk H_s^b=sum_r T_r M_(b_(r,s)) C_r, with its original
globally compact displacement coefficient. For sufficiently large N,
this equals the zero-embedded finite H_s^f on its full input and
output supports. All matrices retain their original level s.

Define U_i^b(epsilon,delta) by L273(3) with these bulk factors:

    U_i^b=a^2 sum_(k,l)c_(i;kl,a) sum_(s=1)^(N-1) s
      {Tr_(F_b)[D_b R_epsilon^b (Cbar_l^b)* P_delta^b
                                      Fbar_k^b D_b H_s^b]
       +Tr_(F_b)[D_b R_epsilon^b D_b* (Fbar_l^b)* P_delta^b
                                      Cbar_k^b Q_delta^b H_s^b]}.
                                                            (3)

Every trace is trace class because H_s^b has finite rank and every
mass is positive. This is an explicitly defined comparison trace,
not a new covariance law for the physical problem.

## Conclusion

At epsilon_N=N^(-1/2), delta_N=N^(-2/3),

    |U_(i,N;epsilon_N,delta_N)-U_i^b(epsilon_N,delta_N)|
                                             <=C_i N^(-10). (4)

Consequently L273's already combined original-response comparison gives

    |E_(i,N)^f-U_i^b(epsilon_N,delta_N)|
                                      <=C_i N^(5/2)log(eN). (5)

This is only boundary transfer. The comparison of (3) with exactly
a^(-3)K_(i,f) still requires ordered coefficient freezing, control of
remote raw rows, complete raw/heat matching, the frozen mass discrepancy
and quadrature. In particular (4) does not assert smoothness of the
bulk zero extensions or license their replacement by continuum values.
The full N^(5/2)log(eN)^2 remainder, transverse-H/L011 quantitative
assembly, pending audits and interacting/continuum/infrared construction
remain open. The separate critical audit in proof section 5 accepts
(4)--(5) relative to the imported premises, including unaudited L273(5).

## Proof

### 1. Preserve the two rectangular orders and the compact insertion

Suppress level and mass subscripts and define maps X_J^j:E_j->F_j by

    X_1^j=D_j R^j (Cbar_l^j)* P_delta^j Fbar_k^j D_j,
    X_2^j=D_j R^j D_j* (Fbar_l^j)* P_delta^j Cbar_k^j Q_delta^j.
                                                            (6)

The two trace summands are Tr_(F_j)(X_J^j H_s^j), or by rectangular
trace cyclicity Tr_(E_j)(H_s^j X_J^j). No multiplier has crossed any
inverse or projection. In particular X_2 contains both its P_delta
and Q_delta factors; neither is idempotent or removed.

L111(1) and its proof section 1 place both endpoints of every nonzero
H_s stencil within a fixed number of cells of compact displacement
support. There are therefore selectors chi_E(s),chi_F(s) of rank at
most C N^3, with fixed physical clearance from every transverse face,
such that, writing i_E,i_F for zero embeddings,

    H_s^b=chi_E H_s^b chi_F=i_E H_s^f i_F*,
    ||H_s^j||<=C.                                          (7)

For some c>0 independent of s,N, both selected index sets are at
distance at least cN from the faces, after a fixed stencil allowance.
If H_s=0 the two traces vanish. All other factors may have noncompact
outputs. No covariance source restriction is made by (7).

L088(5)'s bounds on the actual scalar arrays persist under the zero
extensions in (2). Bounded stencil multiplicity, L273(8), and the
finite or bulk spectral theorem give

    ||Cbar_k^j||+||Fbar_k^j||<=C p(k),
    ||d_j||+||D_j||<=C, ||R^j||<=epsilon^-1,
    ||P_delta^j||,||Q_delta^j||<=1,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                      (8)

The polynomial p may be enlarged once. On the bulk grid the projection
contractions follow from the Fourier eigenvalues lambda/(lambda+delta)
on gradients and zero on their orthogonal complement. The same
singular-value argument applies to finite relative d_f. No regularity
of (2), beyond its sup bounds and interior agreement, is used here.

### 2. Uniformly approximate every inverse position

Import the scalar geometric inverse polynomial of L123(15): for
0<z<=1, m>=0 and spectrum in [0,12],

    p_(z,m)(x)=(12+z)^(-1) sum_(r=0)^m [(12-x)/(12+z)]^r,
    xi_(z,m)=z^-1[12/(12+z)]^(m+1),
    ||(A+z I)^(-1)-p_(z,m)(A)||<=xi_(z,m).                 (9)

This applies to Delta_j and d_j*d_j on both spaces. The actual finite
edge tensor spectrum in L095's proof section 4 has a Neumann own-
direction factor and two Dirichlet factors. Each one-dimensional
factor is nonnegative with eigenvalues at most 4, so its sum is at
most 12. The vertex Laplacian has three Dirichlet factors with the
same bound. Their infinite symbols have values in [0,12]. All normal
end diagonals and constant own-direction modes remain in these operators.
Positive z permits bounded spectral calculus on the infinite grid
even though zero belongs to its spectrum. Thus no new scalar
approximation theorem or boundary condition is being assumed.

Replace R by Rtilde=p_(epsilon,m)(Delta), P_delta by
Ptilde=d p_(delta,m)(d*d)d*, and Q_delta by Qtilde=I-Ptilde.
On either complete space,

    ||R-Rtilde||<=xi_(epsilon,m),
    ||P_delta-Ptilde||=||Q_delta-Qtilde||<=12xi_(delta,m). (10)

Every scalar summand in (9) is nonnegative on [0,12], and the partial
sum is at most (x+z)^(-1). Hence 0<=Rtilde<=R and
0<=Ptilde<=P_delta<=I; both Ptilde and Qtilde are contractions.
Let Xtilde_J be (6) with precisely these replacements. Telescope
the two inverse-bearing positions in X_1 and the three in X_2, keeping
all deterministic matrices in their original order. Equations (8)--(10)
give, on both spaces and for J=1,2,

    ||X_J-Xtilde_J||<=C p(k)p(l)
             [xi_(epsilon,m)+epsilon^-1 xi_(delta,m)].       (11)

This bound includes all inputs and outputs, before any localization.
In X_2 the two projection replacements contribute separate terms;
they are not combined by an idempotence identity.

### 3. Compare complete polynomial paths, then count the trace errors

A degree-m polynomial in either transverse Laplacian has range at
most m in integer lattice distance. Including d,d*, Ptilde and Qtilde
have range at most m+2. All remaining stencils in (6) have fixed
range. Consequently a common upper bound on the total path length
of either Xtilde_J is 3m+r_*, with fixed r_* independent of k,l,s,N.
The first word uses only two inverse positions and obeys the same
upper bound. Scalar multipliers in (2) do not increase this range.

Suppose 3m+r_*<cN with a further fixed stencil margin. Expand the
polynomial words into their finite sums of Laplacian steps and local
path/incidence entries, starting at any output row selected by chi_F.
Every intermediate vertex, edge and plaquette, and every possible
input endpoint, then stays strictly inside the finite box. Finite
and bulk Laplacian, incidence, raw coefficient and path entries agree
there. This proves the full-row identity

    chi_F(i_F Xtilde_J^f i_E*-Xtilde_J^b)=0,
                                             J=1,2.        (12)

The identity includes input columns outside the finite box: no such
column is reachable from the selected row within that path length,
so both sides are zero. This is why no relative covariance source
or boundary row is silently omitted. Their genuine inverse tails
remain in the global errors (10)--(11).

Combining (7) and (12) yields
H_s^b Xtilde_J^b=i_E H_s^f Xtilde_J^f i_E*, and therefore exact
equality of the finite and bulk polynomial traces. Neither a coefficient
nor the original axial range is changed in this equality.

For each true-to-polynomial trace difference, use
|Tr(H_s(X_J-Xtilde_J))|<=||H_s||_1||X_J-Xtilde_J|| and
||H_s||_1<=rank(H_s)||H_s||<=C N^3. Sum both words, finite and
bulk errors, every original axial level and every heat pair. Since
a^2 sum_(s=1)^(N-1)s=32(1-1/N)<=32, (8),(11),(12) imply

    |U_(i,N;epsilon,delta)-U_i^b(epsilon,delta)|
      <=C_i N^3[xi_(epsilon,m)+epsilon^-1 xi_(delta,m)]
                      whenever 3m+r_*<cN.                  (13)

All inequalities are finite uniform estimates before choosing masses
or degrees. The whole-grid trace estimates use finite rank of H,
not a finite volume assumption on an inverse or projection output.

### 4. Substitute the schedule and retain the remaining obligation

Choose

    epsilon=N^(-1/2), delta=N^(-2/3),
    m=ceil(312 N^(2/3)log(eN)).                            (14)

For 0<z<=1, log(1+z/12)>=z/(12+z)>=z/13. Both masses in
(14) are at least N^(-2/3); hence (m+1)z/13>=24log(eN).
Equation (9) gives

    max(xi_(epsilon,m),xi_(delta,m))
                              <=N^(2/3)(eN)^(-24).        (15)

Meanwhile (3m+r_*)/N=O(N^(-1/3)log(eN)) tends to zero. Thus (13)
holds at (14) for all sufficiently large admitted N and its right
side is at most

    C_i N^(3+1/2+2/3)(eN)^(-24)
                         <=C'_i N^(-119/6)<=C'_i N^(-10). (16)

This proves (4). Add L273(5) once to obtain (5); that imported bound
already includes L272's complete f,f, axial endpoint and level errors.
No such error is added separately to either orientation here.

The axial level sum, raw finite heat matrix and all staggered filters
are unchanged. In particular a^3 a^2 s=a^4(as) still holds, and no
outside factor 3 or orientation half is introduced. The boundary
transfer does not evaluate or approximate the frozen torus density
in L123(2). Only polynomial paths were confined to the interior;
the true bulk kernels still sample the zero-extended remote raw rows.
Those rows must be controlled before any interior continuum matching.
ATTEMPTS/030's varying-mass use of a qualitative limit and
ATTEMPTS/032's separate absolute kernel moments are not used.

This is RESEARCH / REPRODUCTION under the unchanged invocation-start
EXPLORE assessment
`drafts/literature/2026-10-24-exterior-circulation-quantitative-remainder.md`.
L244 was inspected as a method comparison, not imported as a bound
for these different words. The scalar polynomial is imported from
L123(15); the new work checks its full ordered finite/bulk application.
This is local progress using known methods, with no source-level
novelty claim or complete component estimate. The following separate
audit checks this specialization; all independent construction gaps remain.

### 5. Separate critical audit of (4)--(5), 2026-10-24

The verdict is acceptance of (4) and the conditional assembly (5),
relative to the stated imported inputs. This audit uses the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-24-exterior-circulation-boundary-transfer-critical-audit.md`.
It does not independently certify L272--L273 or any other upstream proof.
The checks below concern both original words in L273(3), without a
change of observable, coefficient array, coordinate norm or trace order.

**Domains and bounds.** Here Cbar:E->E, Fbar:F->E, D:E->F,
R,P_delta,Q_delta:E->E and H:F->E. Thus both X_J in (6) map
E->F and both X_J H and H X_J have legitimate traces. L110's
definitions of C,F give exactly (2) after normalization; no transpose
sign or endpoint averaging is changed. L111(1) places the scalar
displacement multiplier between two fixed finite stencils. If their
entry is nonzero, both H endpoints are within a fixed stencil radius
of that compact support. This verifies the two selectors in (7),
their common cN clearance, H_b=i_E H_f i_F*, rank O(N^3) and the
uniform operator bound. Compactness applies to H, not to inverse
outputs or raw coefficient supports. L088(5)'s unprojected sup bounds,
bounded row/column multiplicity of the path maps, and the full heat
majorant verify (8) on both spaces after bounded zero extension.

**Actual spectra and every inverse slot.** L095's relative tensor
spectrum has an own-direction Neumann index 0,...,N-1 and two
Dirichlet indices 1,...,N-1. Each summand is
4 sin^2(pi q/(2N)), so every edge eigenvalue lies in [0,12].
The vertex space has three Dirichlet factors with the same upper
bound. This includes every normal end row; constant own-direction
indices are retained. The bulk symbol has the same three summands,
including zero frequency. The bounded self-adjoint spectral theorem
therefore applies to L123(15) on the finite and infinite spaces for
each positive mass. No matrix-decay theorem with an unverified
finite-section hypothesis is needed.

For a singular value sigma of d, the eigenvalue of Ptilde on its
range is sigma^2 p_(delta,m)(sigma^2), between zero and
sigma^2/(sigma^2+delta)<=1. It is zero on ker d*. This independently
checks both polynomial projection contractions, including Qtilde,
and their errors at most ||d||^2 xi_delta<=12 xi_delta.
The first word has the R and P slots; the second has R, P and Q.
Telescope first R, then P, then Q where present, with all remaining
slots either true or polynomial contractions. An R replacement costs
C p(k)p(l) xi_epsilon, and each projection replacement costs
C p(k)p(l) epsilon^-1 xi_delta. Their finite number is absorbed in
C in (11). In particular the second word pays for its two projection
slots separately. This checks (11) globally before any selector is used;
no regularized projection is taken to be idempotent.

**Complete paths and exact trace equality.** The only variable-range
factors are Rtilde and the one or two vertex-polynomial factors in
Ptilde,Qtilde. A degree-m Laplacian polynomial has range m; the two
incidences surrounding a vertex polynomial add at most two. All
other paths, circulations, endpoint/clover filters and component-center
shifts have fixed range. Hence the entire second word has range at
most 3m+r_* and the first at most 2m+r_*; the same fixed r_* can
cover both and the support-selector margins. Starting from any
selected F output, even an open path to a possible E input stays
interior if this total bound is below the clearance. Every matrix
entry along that path agrees, including raw multipliers. An input
outside the finite box is unreachable on either side. This establishes
the full-row identity (12), not just agreement on interior input
columns or closed diagonal paths. Multiplying by H=H chi_F proves
the asserted embedded equality of H Xtilde and thus equality of
polynomial traces. It changes no level or heat label. Genuine inverse
tails, including all boundary sources, occur in the global error alone.

**Full amplification and schedule.** Finite-rank trace duality gives
||H||_1<=C N^3 on each space, including the infinite grid. There are
two words and two true-to-polynomial comparisons. L088(5) sums their
polynomial heat envelopes, and the exact original level factor is
a^2 sum_(s=1)^(N-1)s=32(1-1/N). Consequently (13) follows with
no further row, axial or omitted-mode factor. At (14),
log(1+z/12)>=z/13 and z>=N^(-2/3), so every scalar error is
at most N^(2/3)(eN)^(-24). Also 3m+r_*=o(N), so the exact
path equality applies for all sufficiently large admitted N. The
remaining amplification is N^(3+1/2+2/3)=N^(25/6), giving
N^(25/6)(eN)^(-24)=e^(-24)N^(-119/6), below the required
N^(-10). The threshold may be large; (4) asserts only an eventual
bound and requires no finite-mesh numerical test.

Finally the triangle inequality adds precisely the already combined
L273(5) to (4). That allowance contains L272's removed terms once;
it is not added for each word. The original a^2 s, both orientations,
both full probe heat matrices and a^3 a^2 s=a^4(as) remain, with
no outside factor 3. This accepts (5) conditional on L273(5), without
auditing its mass/projection estimates. Neither uniform polynomial
comparison nor its negligible error approves smoothing the raw zero
extensions, freezing coefficients or substituting varying masses into
a qualitative limit. ATTEMPTS/030/032 are respected. This is local
RESEARCH / REPRODUCTION verification by standard spectral and
finite-propagation methods, not a result beyond the sources assessed,
a full quantitative assembly or an interacting construction.

## Mathlib

Full matching exterior-circulation ordered boundary-transfer theorem:
**not checked**. Supporting bounded spectral calculus, geometric inverse
approximation, rectangular trace cyclicity, finite-rank trace inequalities
and finite propagation of matrix polynomials: **not checked**. Unknown
availability is not absence. No formal verification or general continuum
Ward/flow theorem supplies the unproved comparison with L123(2).
