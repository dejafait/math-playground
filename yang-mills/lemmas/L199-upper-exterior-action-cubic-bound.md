# L199 — Cubic bound for the upper-exterior action trace

## Hypotheses

Use L198's full SU(2) setting: relative box (-4,4)^4, sufficiently
fine admitted even N, a=8/N, the straight lower-rooted direction-1
forest, complete compact displacement and both actual L010 probes
i=3,6 at tau=1/16. The bare expansion is at fixed mesh before
refinement. Coordinates and adjoints are ordinary stored full-link
coordinates. Keep every physical face, normal end edge, constant
own-direction mode and the entire heat expansion.

Write Sigma=(L+DD^T)^(-1) for the dimensionless relative Hodge
covariance, P for the co-closed projection and S=P Sigma=Sigma P.
Keep the complete compact residual A=PAP with both insertion
subtractions, and M=2SAS=2 Sigma A Sigma, as in L185. Use L198's
alternating action slice s_v and its exact exterior expansion

    n_k=S e_k, beta_k=R n_k, R=I-D Phi,
    SB_i=a^2 sum_(k,l) d_(i;kl) n_k e_l^T,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)                 (1)

for every fixed polynomial p. Here e_l are ordinary normalized
relative product modes. Put V=q Phi, H=I-D Phi/2 and

    J_y=-P{H^T diag(y)V-V^T diag(y)H}P/2.

Let Pi_n select the upper direction-1 normal variable links, with
axial tail level N-1, and let Pi_t select all tangential variable
links at axial level N-1. The latter includes their transverse
normal end edges. Set beta_k^t=Pi_n beta_k. These selectors are
used only in explicit matrix blocks; they do not commute with P.

## Conclusion

L198(3)'s complete upper-exterior action trace satisfies

    H_(i,N)=12a^2 sum_(k,l)d_(i;kl)
                        Tr(J_(e_l) M s_(beta_k^t) S),
    |H_(i,N)|<=C_i N^3.                                (2)

Its two normal/tangential rough orientations are bounded, after
the full heat sum and a^2 normalization, by O_i(N^3) and
O_i(N^2 sqrt(log(eN))), respectively. Only the second of these
estimates supplies a zero cubic-scaled limit for that orientation.
There is no finite scaled limit, value or sign asserted for H.

Together with L198, this improves the entire joint cubic probe-jet
group G_(i,a)=kappa_0(f_(i,1),r_1)-kappa_0(f_(i,1),r_0,S_3) to

    |G_(i,a)|<=C_i N^3 sqrt(log(eN)),
    |a^3 G_(i,a)|<=C_i sqrt(log(eN)).                   (3)

The required O(1) scaled bound and finite scaled limit remain
unproved. The bulk logarithmic allowance, transport and their joint
limit remain. Independent f_(i,2),r_0, full compensation, finer
asymptotics, finite matching, reflected error <=c_box/2, continuum
axioms and infrared finite positive mass remain unresolved. This is
a local specialization of existing boundary Green and finite-matrix
estimates, not a claim of progress beyond the checked sources.

## Proof

### 1. Restore the upper action tensor before selecting rough blocks

L163, proof section 1, polarizes the complete action cubic on the
last axial plaquette layer. Its only three variable links are two
normal links x,y and one tangential link z at level N-1; the link
on the upper face is fixed. Its cubic is (1/2)x dot (z cross y),
up to an orientation convention immaterial for the bounds below.
Inserting an exterior vector with only normal components therefore
leaves exactly one normal and one tangential rough argument. Extra
fixed links at transverse faces simply set the corresponding cubic
to zero. The convention change from L163's symmetric colored tensor
to L198's alternating spatial tensor changes only fixed constants.
Thus, as an exact support identity,

    s_(beta_k^t)=Pi_n s_(beta_k^t) Pi_t
                            +Pi_t s_(beta_k^t) Pi_n.   (4)

There are O(N^3) eligible links of each type. Every row and column
of either block has bounded degree. L187(15) gives
||beta_k^t||_infinity<=C N p(k). Consequently, writing
X_nt=Pi_n s_(beta_k^t) Pi_t and X_tn=Pi_t s_(beta_k^t) Pi_n,
the row/column sum inequality gives

    ||X_nt||_op+||X_tn||_op<=C N p(k).                 (5)

No selection is made on any covariance input in (4). In particular
this deterministic-exterior split is not L196's upper-output split.

### 2. Full-spectrum covariance rows at the upper face

L026(6)-(7) gives the exact product modes and dimensionless energies
lambda_q=4 sum_j sin^2(pi q_j/(2N)). Each component has three
positive vertex indices and its own edge index may be zero. Hence
lambda_q>=4|q|^2/N^2, a shell max_j q_j=r has at most C r^3 modes,
and all ordinary squared mode amplitudes are at most C N^-4.
Summing every mode gives

    ||Sigma||_op<=C N^2,
    sum_q lambda_q^-1<=C N^4,
    sum_q lambda_q^-2<=C N^4 log(eN).                  (6)

Component multiplicities are fixed. For any normal upper link f,
the spectral diagonal formula therefore gives
(Sigma^2)_ff<=C log(eN).

For a tangential link f at axial vertex level N-1, its axial sine
factor supplies the stronger squared-amplitude estimate

    |e_q(f)|^2<=C N^-4 sin^2(pi q_1/N)
              <=C N^-4 mu_(q_1),
    mu_m=4 sin^2(pi m/(2N))<=lambda_q.

The identity sin(pi m(N-1)/N)=(-1)^(m+1)sin(pi m/N)
justifies this at the actual last interior vertex, without extending
the field across the pin. Thus (6) gives

    (Sigma^2)_ff=sum_q |e_q(f)|^2 lambda_q^-2<=C.       (7)

The edge-cosine coordinate in a tangential component can still have
index zero; it has not been deleted. The argument is uniform in all
transverse positions, including normal end edges. Summing (7) and
the normal bound over their O(N^3) rows, then using S=Sigma P and
||P||<=1 on the right, yields

    ||Pi_n S||_HS<=C N^(3/2) sqrt(log(eN)),
    ||Pi_t S||_HS<=C N^(3/2).                          (8)

This uses the full Hodge covariance only for a positive spectral
norm estimate; it assigns no component diagonality to S itself.

### 3. Separated residual columns retain the extra tangential gain

Let K be a fixed compact interior enlargement containing both
indices of A and every stencil needed to form it. L166, proof
section 1, supplies this support property and, for e in K,

    |(A Sigma)_(e,f)|<=C a^-1
                         [(1+dist(e,f))^-4+N^-4].     (9)

For f in Pi_n the distance is at least delta N, for fixed delta>0,
so this is O(N^-3). For f in Pi_t there is an additional power,
which must be proved before counting matrix entries.

Use L163(10)'s exact axial Dirichlet last column. For a tangential
component mu, diagonalize its other three coordinates, including
the own-direction cosine index zero. With transverse eigenvalue
lambda_q, eta_q=2 asinh(sqrt(lambda_q)/2), that column is

    R_D(s,N-1;lambda_q)=sinh(s eta_q)/sinh(N eta_q).    (10)

Here at least two transverse indices are positive,
c|q|/N<=eta_q<=C|q|/N, and the observation level s stays separated
from the upper face by delta N. A total of j unscaled observation
differences, j=0,1,2, multiplies the axial hyperbolic factors and/or
transverse trigonometric factors by at most C(|q|/N)^j.
This follows directly by subtracting consecutive exponentials;
the bounded shifts enlarge s only by a fixed number of steps.
Both sinh and cosh ratios are at most C_delta exp(-c_delta|q|)
there. Each transverse product of source and observation mode
amplitudes is at most C N^-3. Summing the complete finite spectrum
against the convergent majorant |q|^j exp(-c_delta|q|) gives

    |partial_e^j Sigma_(e,f)|<=C_delta N^(-3-j),
       f in Pi_t, e in K, j=0,1,2.                    (11)

These are differences on the observation component's staggered
grid. Mixed component entries of Sigma are zero; component changes
in the subsequent local operators only select and shift these same
scalar columns. Transverse end rows satisfy the same amplitude bound.
No source mode, collar or constant own-direction mode was removed.

Now retain the full residual formula from L166(6),

    A=(L K_a+K_a^T L)/2-Q_3-Q_6.

As specified in L166, K_a is a finite sum of shifts with coefficients
a^-1 k_b(e), whose first and second observation differences on K
are O(a) and O(a^2) after the a^-1 is factored out. L has two
unscaled differences. Apply the exact discrete product rule twice
and (11) to obtain

    |(L K_a Sigma)_(e,f)|
      <=C a^-1[N^-5+a N^-4+a^2 N^-3]<=C N^-4.         (12)

For the reverse orientation, first apply L to the scalar Green
column. Equation (11) with j=2 bounds every entry of L Sigma
near e by C N^-5; applying the finite K_a^T stencil gives C N^-4.
This does not infer the extra gain from a generic bound on P.
For each Q_j=D_1^T W_j D_1, retain the rightmost difference on
Sigma. The remaining factors have bounded degree and entries, so
(11) with j=1 gives C N^-4. Both Q_3 and Q_6, including their
clover averages, are included. Therefore

    |(A Sigma)_(e,f)|<=C N^-4, f in Pi_t.              (13)

There are O(N^4) possible e in the compact support and O(N^3)
boundary columns of either type. Outside that support A Sigma is
zero in its first index. Squaring (9),(13) and summing proves

    ||A Sigma Pi_n||_HS<=C N^(1/2),
    ||A Sigma Pi_t||_HS<=C N^(-1/2).                   (14)

Since M=2 Sigma A Sigma exactly, (6),(14) imply

    ||M Pi_n||_HS<=C N^(5/2),
    ||M Pi_t||_HS<=C N^(3/2).                         (15)

These estimates use separated Green columns and the actual local
residual. They do not posit a smooth rough tilt or positivity of M.

### 4. Close the trace in its original order

The bounded-degree incidence and endpoint maps, together with
L187's ||Phi||_op<=N, give ||H||_op+||V||_op<=C N.
Every ordinary normalized product mode has
||e_l||_infinity<=C N^-2, uniformly in l. Consequently the exact
definition of J gives

    ||J_(e_l)||_op<=C.                                (16)

No projection is treated as a supremum contraction in (16).

For the first block of (4), finite cyclicity and Hilbert--Schmidt
Cauchy--Schwarz give in precisely the displayed order

    |Tr(J M X_nt S)|
      =|Tr((Pi_t S J)(M Pi_n)X_nt)|
      <=||Pi_t S J||_HS ||M Pi_n||_HS ||X_nt||_op
      <=C p(k) N^(3/2) N^(5/2) N=C p(k) N^5.          (17)

For the second block they give

    |Tr(J M X_tn S)|
      <=||Pi_n S J||_HS ||M Pi_t||_HS ||X_tn||_op
      <=C p(k) N^(3/2) sqrt(log(eN)) N^(3/2) N
       =C p(k) N^4 sqrt(log(eN)).                     (18)

Here J=J_(e_l). These are rectangular block products or, equivalently,
full matrices with the indicated zero rows; no selector crosses P,
S, J or M. The opposite boundary types in (17) and (18) are essential.
Using only the normal estimates for both would lose the needed gain.

Multiply (17),(18) by 12a^2 and sum (1) over all external modes.
This proves the stated orientation bounds and (2), since
sqrt(log(eN))<=C N. L198(4) then gives (3): its bulk trace remains
O(N^3 sqrt(log(eN))), its transport is O(N^3), and its error is
o(N^3). Neither H nor the transport is discarded at cubic scale.

### 5. Verification and limits of the result

The checks are analytic: (4) retains the full upper plaquette and
its fixed-link restrictions; (7) uses the exact last-vertex sine;
(10)-(13) retain both residual generator orders and both insertion
subtractions; (17)-(18) retain the actual signed matrix order and
the full exterior sum. No numerical fixture or mathematical script
is needed. L197's covariance-commutator obstruction is unaffected.

The continuation test for this intermediate bound succeeds. The
remaining bulk logarithm in (3) is an upper allowance, not demonstrated
growth. Neither a finite a^3 limit nor its failure follows, and no
actual-probe coefficient or independent compensation is identified.

## Mathlib

Full matching upper-exterior estimate and joint scaled limit:
**not checked**. Supporting spectral, finite-trace and Hilbert--Schmidt
inequality coverage: **not checked**; unknown coverage is not absence.
The named finite-dimensional spectral theorem, row/column sum bound
and Hilbert--Schmidt ideal inequalities are used in their elementary
forms. The actual relative product spectra are imported from
L026(6)-(7), the upper action and Dirichlet last column from L163,
and the residual kernel/stencil estimates from L166. The additional
boundary differences are justified above because the generic
compact-observation bound alone would not close this trace.
Reuse the unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md);
no general flow-renormalization theorem is reproved or transferred
to this selected bare group.
