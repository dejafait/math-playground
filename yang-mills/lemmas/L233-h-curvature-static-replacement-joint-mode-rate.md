# L233 — A joint-mode rate for the H curvature static replacement

## Hypotheses

Use exactly L097's R_H,Q, its finite static expression (4), its
ordinary stored coordinates and its operators for the actual probes
i=3,6: SU(2), the relative all-face pinned box (-4,4)^4, the straight
lower-rooted direction-1 forest, sufficiently large admitted even N,
a=8/N and tau=1/16. The bare small-coupling coefficient is taken at
each fixed mesh before refinement. Retain every interior axial level,
relative transverse end row, allowed constant component mode and
exterior heat label. The triplet is L008's average of curvature squares;
the shear retains both clover factors.

In L097's notation put

    G_st=1_(t<=s)P, 1<=s,t<N,       Y_k=Zeta_k G,
    X_k=X_(k,F)+B Y_k,              X_(k,0)=B_0 Y_k,
    B=D_1 I R(I tensor D_T^T),      B_0=E_T(I tensor S_T).

P is the full relative transverse gradient projection. The input of
G is the direct sum of N-1 copies of the transverse link space;
its redundant components in ker P cause no difficulty. L097(7) is
the exact identity

    R_H,Q=sum_(k,l)c_(i;kl,a) Tr(X_k^T M_0 X_l),        (1)

with the actual bounded, possibly indefinite full-curvature multiplier
M_0, not merely its transverse restriction M_T. Import L097(9)–(13)'s
coefficient bounds, full-curvature spectral comparison and norms,
and L088's complete heat expansion. With a fixed polynomial p(k)>=1,
independent of N, these include

    ||Zeta_k(s)||<=C a p(k),
    ||Zeta_k(s+1)-Zeta_k(s)||<=C a^2 p(k), 1<=s<N-1,
    ||X_(k,F)||_HS<=C p(k)N,
    ||Y_k||_HS<=C p(k)N^(3/2),
    ||B||,||B_0||<=1, ||M_0||<=C,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.               (2)

The neighboring-level statement includes N-2,N-1. It is not a
smoothness assumption across the upper pin. All these hypotheses
are established inputs of L097, rather than assumptions of an
improved error or a static-to-continuum rate.

## Conclusion

Define exactly L097(4)'s static expression

    T_(i,N)=sum_(k,l)c_(i;kl,a) sum_(s=1)^(N-1) s
      Tr_T[P Zeta_k(s)^T S_T M_T(s) S_T Zeta_l(s)P].

Then, uniformly in sufficiently large admitted N, for i=3,6,

    |R_H,Q-T_(i,N)|<=C_i N^(5/2).                    (3)

This improves the previous O(N^(27/10)) allowance and meets the
requested O(N^(5/2)log(eN)^2) threshold without a logarithmic loss.
After multiplication by a^3 the replacement error is O_i(N^(-1/2)).
The positive-definition R_H,Q enters the assembled H trace with a
minus sign; (3) changes neither that sign nor any outside factor.

This is a local quantitative specialization of the spectral and Abel
methods already assessed, classified REPRODUCTION. No originality
beyond the checked sources is claimed. The separate critical audit in proof section 4 accepts the
specialization relative to the stated imported inputs. It supplies no estimate on
T_(i,N)-a^(-3)K_(i,Q), other response components, finer asymptotics,
the interacting reflected error <=c_box/2, continuum axioms or finite
positive physical mass. There is no complete-solution candidate.

## Proof

### 1. Bound the actual projected-increment rows by Abel summation

The axial Dirichlet eigenbasis is

    phi_m(s)=sqrt(2/N)sin(pi m s/N),
    mu_m=4sin^2(pi m/(2N)), 1<=m<N.

Import this scalar diagonalization from J. S. Dowker,
[*Heat-kernels on the discrete circle and interval*](https://arxiv.org/pdf/1207.2096v2),
v2, 31 August 2012, section 7, printed pp. 10–11, (30)–(31),
with p=N. Its zero endpoint values at 0,N and N-1 interior rows
match the axial L_D in L097. The inspected source and L223's
accepted use supply this input; no scalar spectral theorem is
reproved or assigned to other gauge components here.

Use L223(3)'s finite sine partial-sum estimate

    |sum_(s=u)^v phi_m(s)|<=2sqrt(2)/(sqrt(N)sqrt(mu_m)) (4)

for all 1<=u<=v<N. Its Abel method must be applied to the present
input space, as follows. Fix any unit transverse curvature vector e,
including one not localized in transverse frequency. Set
v_s=e^* Zeta_k(s)P, a row on the full transverse link space. The
(phi_m,e) output row of Y_k has input-increment block, for 1<=t<N,

    h_t=sum_(s=t)^(N-1) phi_m(s)v_s.

For this fixed t let A_r=sum_(s=t)^r phi_m(s). Finite summation by
parts is the exact row identity

    h_t=A_(N-1)v_(N-1)
          +sum_(s=t)^(N-2) A_s(v_s-v_(s+1)).         (5)

The sum is empty when t=N-1. In particular the nonzero upper
coefficient is retained, and no v_N or difference to a zero-extended
value is introduced. Since ||P||<=1, (2), (4) and Na=8 imply

    ||h_t||<=C/(sqrt(N)sqrt(mu_m))
                   [a p(k)+N a^2 p(k)]
            <=C' a p(k)/(sqrt(N)sqrt(mu_m)).

The input increment spaces are orthogonal coordinate summands.
Therefore the squared Euclidean row norm is the sum of the squared
norms of its N-1 blocks, giving

    ||(phi_m^* tensor e^*)Y_k||^2
          =sum_(t=1)^(N-1)||h_t||^2
          <=C a^2 p(k)^2/mu_m.                     (6)

The same bound holds if the input is restricted to im P at each
increment, because h_t already has P on its right. No multiplier
has crossed P. Orthogonality here concerns the input coordinates,
not the overlapping prefix outputs: GG^T still has the full
min(s,t)P covariance. Both the lower prefix start and the upper
jump are included in (5). This is the required specialization of
L223's row argument; its E response theorem is not being imported.

### 2. Sum L097's full-curvature error over joint modes

Put Dcal=B-B_0. Choose an orthonormal co-closed transverse edge
eigenbasis f_j with positive Delta_T eigenvalues lambda_j. Its
corresponding orthonormal curvature basis in im D_T is
e_j=D_T f_j/sqrt(lambda_j). L097(13) gives precisely

    Dcal^*Dcal(phi_m tensor e_j)
       =mu_m/(mu_m+lambda_j)(phi_m tensor e_j).       (7)

Indeed the transverse and axial curvature outputs of B are
lambda_j/(mu_m+lambda_j) and a vector of norm
sqrt(mu_m lambda_j)/(mu_m+lambda_j), respectively, whereas B_0
has transverse coefficient 1 and no axial output. Those output
spaces are orthogonal, and their squared difference is
mu_m/(mu_m+lambda_j). Both B and B_0 vanish on ker D_T^T.
Thus (7) includes both kinds of curvature, rather than comparing
only the transverse component. This restates the already proved
L097 identity to specify which map is used; L223's square-root
covariance map is different.

The finite-dimensional Hilbert–Schmidt trace identity, (6) for
e=e_j and (7) yield

    ||Dcal Y_k||_HS^2
      =sum_(m,j) mu_m/(mu_m+lambda_j)
                   ||(phi_m^* tensor e_j^*)Y_k||^2
      <=C a^2 p(k)^2 sum_(m,j)1/(mu_m+lambda_j)
      =C a^2 p(k)^2 Tr K_h
      <=C' p(k)^2 N^2.                              (8)

Here K_h=R Qcal and the equality of positive spectral multiplicities
uses exactly the co-closed edge/curvature correspondence in L097.
The trace bound is L086(6), also used in L097(10): restriction to
the co-closed space decreases the full positive relative trace,
which is at most C N^4. Explicitly, in a joint max-index shell q
there are at most C q^3 relative component labels and each energy
is at least c q^2/N^2, so the inverse sum is bounded by
C N^2 sum_(q=1)^(N-1)q<=C' N^4. The axial index is positive;
allowed zero own-coordinate transverse indices remain counted.
Every normal end row remains part of the relative spaces. The
curvature complement has zero contribution because Dcal vanishes
there, not because it is a discarded error sector.

The cancellation of mu_m between (6) and (7) occurs inside the
joint sum. Taking a separate worst-mode transverse inverse bound
would lose the gain. No transverse cutoff, mass schedule, boundary
localization or coefficient freezing is used in (8). Since a=8/N,
it gives ||(B-B_0)Y_k||_HS<=C p(k)N.

### 3. Restore both signed factors and every heat label

Equations (2) and (8), with X_k=X_(k,F)+B Y_k, give

    ||X_k-X_(k,0)||_HS<=C p(k)N,
    ||X_k||_HS+||X_(k,0)||_HS<=C p(k)N^(3/2).        (9)

The first estimate retains the full exterior-circulation term.
For each ordered k,l use the exact difference

    X_k^* M_0 X_l-X_(k,0)^* M_0 X_(l,0)
      =(X_k-X_(k,0))^* M_0 X_l
          +X_(k,0)^* M_0(X_l-X_(l,0)).

Hilbert–Schmidt Cauchy–Schwarz with ||M_0||<=C and (9) bounds
the absolute trace by C p(k)p(l)N^(5/2). Both curvature factors,
both exterior-circulation orientations and their cross term are
included. No positivity, commutation or level-diagonality of the
full M_0 pairing is assumed. Its possible axial/transverse mixed
entries have been included in this norm bound.

For completeness, the static pairing is exactly T_(i,N), not a
new comparison expression. B_0Y_k has transverse curvature only,
so M_0 restricts there to L097's level-diagonal M_T. Writing
W_k(s)=S_T Zeta_k(s), its increment-t block at level s is
1_(t<=s)W_k(s)P. Consequently

    Tr(X_(k,0)^* M_0 X_(l,0))
       =sum_(s=1)^(N-1)sum_(t=1)^s
                    Tr_T[P W_k(s)^* M_T(s)W_l(s)P]
       =sum_(s=1)^(N-1)s
          Tr_T[P Zeta_k(s)^* S_T M_T(s) S_T Zeta_l(s)P].

The diagonal weight s is thus obtained only after controlling
the full dynamic prefix in (8). It was not substituted for
min(s,t) in (1). All finite maps are real, so * here is the
transpose in the statement.

Multiply the per-pair error by |c_(i;kl,a)| and sum using (2).
L088's bound has exactly the same polynomial envelope as in
L097; no extra frequency dependence or cutoff has appeared.
This proves (3) for the complete heat sums of both actual probes.
Their exact average-of-squares and clover definitions remain in
M_0 and c_(i;kl,a). No static-to-continuum assertion or value of
K_(i,Q) has been used.

### 4. Separate critical audit, 2026-10-18

**Verdict: accepted relative to the stated imported inputs.** The
approved scope is
`drafts/literature/2026-10-18-h-curvature-joint-mode-rate-critical-audit.md`.
This is a separate check of (4)–(9), both signed pairings and their
identification with (3). L097's exact contraction, coefficient
regularity and relative cochain identities are imported, as are
L008's actual probe forms, L086's spectrum, L088's heat framework
and L223's scalar partial-sum estimate. No recursive audit of these
inputs or theorem about the interacting theory is claimed.

**Projected input rows and the nonzero endpoint.** Put n=N-1.
For arbitrary unit transverse curvature e, the row after the axial
sine transform has exactly n input blocks

    h_t=sum_(s=t)^n phi_m(s)e^* Zeta_k(s)P, 1<=t<=n.

The input is the full transverse link space in each block, rather
than the scalar input in the E audit. Writing phi_m(s)=A_s-A_(s-1),
with A_(t-1)=0, verifies (5) with the displayed difference sign.
At t=n it is h_n=phi_m(n)e^*Zeta_k(n)P; this block is not dropped.
The imported partial-sum bound and L097(9) give

    ||v_n||+sum_(s=t)^(n-1)||v_s-v_(s+1)||
       <=C p(k)[a+(N-2)a^2]<=9C a p(k).

Only differences between existing levels occur. In particular the
upper coefficient need not vanish and no bound on v_N-v_(N-1)
is used. Because the input blocks form an orthogonal direct sum,
||[h_1 ... h_n]||^2=sum_t||h_t||^2. Combining this identity with
the partial-sum bound gives C a^2 p(k)^2/mu_m, as in (6).
The estimate is uniform in e and therefore applies to each transverse
eigenvector despite Zeta_k's frequency mixing. P remains on the right
throughout. Orthogonal coordinate blocks do not make distinct prefix
outputs independent: GG^T still has blocks min(s,t)P.

**Full-curvature spectrum, including its orthogonality.** Take the
orthonormal co-closed transverse edge basis f_j and e_j=D_T f_j /
sqrt(lambda_j) used in section 2. Besides L097's modal norms, the
joint output images are orthogonal: their transverse parts are
multiples of phi_m tensor e_j, while their axial parts are multiples
of D_v phi_m tensor f_j. Here D_v is the incidence from the N-1
axial vertices to all N normal edges. In fact

    <D_v phi_m,D_v phi_r>
       =<phi_m,L_D phi_r>=mu_r delta_(m,r).

Transverse and axial curvature components belong to orthogonal
coordinate summands. Thus distinct (m,j) have orthogonal images
under B-B_0 even in degenerate eigenspaces. The squared norm of
one error image is exactly

    [mu_m/(mu_m+lambda_j)]^2
      +mu_m lambda_j/(mu_m+lambda_j)^2
       =mu_m/(mu_m+lambda_j).

This checks the diagonal operator identity (7), rather than inferring
it solely from modal norm bounds. On ker D_T^T both B and B_0 vanish.
Relative normal end edges occur in D_v and the transverse cochain
maps; their removal would invalidate this calculation.

The finite Hilbert–Schmidt expansion is consequently exactly the
first line of (8). The co-closed edge/curvature correspondence preserves
positive multiplicities, so its inverse sum is Tr K_h. L086(6)
bounds this by the trace on all three transverse components with
k_1 in 1,...,N-1, own transverse index in 0,...,N-1, and the other
two transverse indices in 1,...,N-1. Its max-index shell q has at
most C q^3 labels and energy at least 4q^2/N^2. Hence the full sum
is bounded by C N^2 sum_(q=1)^(N-1)q<=C' N^4. Allowed constant
own-coordinate modes are retained; the positive axial index precludes
a zero joint energy. The curvature null complement contributes zero
by the exact map identity, not by a low-frequency omission. Multiplying
by a^2 p(k)^2 verifies the O(p(k)^2 N^2) squared error in (8).

**Both signed factors, the static expression and the full heat sum.**
The imported exterior-circulation bound can also be checked directly
in its original order: ||D_1 I K_h||_HS<=C N^2,
||F_k||<=C a^2 p(k), and ||G||<=C N give
||X_(k,F)||_HS<=C p(k)N. Independently, rank P=(N-1)^3 gives

    ||Y_k||_HS^2=sum_(s=1)^(N-1)s||Zeta_k(s)P||_HS^2
       <=C a^2 p(k)^2 N^5<=C' p(k)^2 N^3.

The contraction bounds on B and B_0 now verify both estimates (9).
For finite rectangular matrices,

    |Tr(U^* M_0 V)|<=||U||_HS ||M_0|| ||V||_HS.

Apply this to the two exact differences in section 3: each costs
C p(k)p(l)N times N^(3/2). In the first difference X_l is still
the complete dynamic factor, so the exterior/exterior cross term
is included. No positivity of M_0, commutation with a prefix, or
axial level diagonality of the dynamic pairing is required.

After both factors are static, their axial curvature rows are zero.
L008(2)'s triplet average of squares then stays within each level;
the surviving shear clovers have transverse planes on both sides,
so their shifts also stay within a level. This verifies the use of
L097's M_T(s) at this stage only. The static increment block at
(s,t) is 1_(t<=s) S_T Zeta_k(s)P. In its trace the t sum has
exactly s terms, yielding precisely the stated T_(i,N), including
P on both sides. No dynamic min(s,t) block has been replaced before
the error estimate. The sign of R_H,Q in the assembled H trace and
all original heat coefficients are unchanged; no outside factor 3
is introduced.

Every estimate uses only the same p(k)p(l). L088(4)–(5), or the
explicit Gaussian majorant in L097 section 5, therefore sums the
errors over all admitted heat labels uniformly in N for i=3,6.
There is no limiting interchange needed to prove this finite-N
inequality and no unestimated omitted mode sector. Both actual
probe definitions, with their original polarizations, remain intact.

**Decision and limitations.** The claimed O(N^(5/2)) replacement
rate passes these checks with no added hypothesis or repaired
inequality. Multiplication by a^3 gives O(N^(-1/2)); this is stronger
than the requested allowance with log(eN)^2. ATTEMPTS/024–025 concern
different absolute-profile tests; ATTEMPTS/030 concerns uncontrolled
varying-mass limits; ATTEMPTS/045 concerns a rough projection-side
prefix rather than the deterministic Zeta_k variation. None of those
failed steps is used. Their evidence is preserved.

This audit validates an existing local standard-method specialization,
not a new rate or a result beyond the sources checked. It supplies
no rate for T_(i,N)-a^(-3)K_(i,Q), no estimate for the other response
components, and no interacting or mass-gap conclusion.

## Mathlib

Full matching actual-probe H static-replacement theorem: **not
checked**. Supporting finite sine diagonalization, Abel summation,
spectral calculus, Hilbert–Schmidt trace inequalities and complete
heat summability: **not checked**. Unknown availability is not
evidence of absence. The scalar spectrum is imported by the precise
Dowker citation above; the new work is the projected-increment and
full-curvature specialization, accepted by the separate audit above
relative to its imported inputs.
