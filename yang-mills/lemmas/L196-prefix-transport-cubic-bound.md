# L196 — Cubic transport bound from the projected upper prefix

## Hypotheses

Use exactly L187–L188 and L194–L195's SU(2) setting: relative box
(-4,4)^4, admitted even N, a=8/N, straight lower-rooted direction-1
forest, complete displacement and both actual L010 probes i=3,6 at
tau=1/16. The fixed-mesh bare expansion precedes refinement. Use
ordinary dimensionless full variable-link coordinates and Euclidean
adjoints. Keep every physical face, normal end edge, constant
own-direction edge mode and the full heat sums. Vertex potentials
are zero on every boundary vertex.

Keep the orthogonal co-closed projection P, covariance S=PSP,
the signed residual A=PAP with both insertion subtractions and

    M=2SAS, E=S^(1/2) A S^(1/2),
    V=q Phi, H=I-D Phi/2, R=I-D Phi,
    Gamma_y=-(H^T diag(y)V-V^T diag(y)H)/2,
    J_y=P Gamma_y P.

Phi is the original lower prefix, not a continued field across the
upper pin. Let Pi select all upper direction-1 normal variable edges.
It need not commute with P. For the exact complete heat expansion use

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k e_l^T, n_k=S e_k,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p),                (1)

for every fixed polynomial p, as in L187. For each rank-one term put

    alpha_k=Vn_k, beta_k=Rn_k,
    Z_k=P diag(alpha_k)P, C_k=P diag(beta_k)VP.

These are L188's definitions; C_k is not assumed symmetric. All
constants below are independent of sufficiently fine admitted meshes.

## Conclusion

The entire transport branch in L188's exact split is cubic-bounded:

    Q_(tr,i,N)=3a^2 sum_(k,l)d_(i;kl)
                   Tr(J_(e_l)(M C_k^T-C_k M)),
    |Q_(tr,i,N)|<=C_i N^3.                              (2)

The boundary estimate behind this improvement is

    ||Pi J_(e_l) S^(1/2)||_HS<=C N,                     (3)

versus the complete-output O(N^(3/2)) estimate. It also sharpens
L195's original upper-output part, with its original definition, to

    |Q_(3,i,N)^top|<=C_i N^(5/2),
    a^3 Q_(3,i,N)^top -> 0.                            (4)

Thus in the exact whole third placement

    Q_(3,i,N)=Q_(mult,i,N)+Q_(tr,i,N),
    Q_(mult,i,N)=-3a^2 sum_(k,l)d_(i;kl)
                              Tr(J_(e_l)[M,Z_k]),      (5)

transport no longer causes an above-cubic bound. No finite limit of
(2), cubic bound for (5)'s multiplier term, or joint cubic limit is
proved. The full Q_3 bound remains O(N^(7/2)), and L194's sextic
retains O(N^3 sqrt(log(eN))). A cubic transport term can contribute
to the coefficient. The independent f_(i,2),r_0 contribution, full
compensation, finer asymptotics, finite matching, interacting reflected
error <=c_box/2, continuum axioms and infrared finite positive mass
remain unresolved. This is a local standard-estimate refinement, not
progress beyond the checked literature.

## Proof

### 1. Keep the projected upper prefix exactly

Write G_0=(D^T D)^(-1) on the pinned interior vertices. The prefix
telescopes on a vertex gradient: at every interior vertex its sum is
the vertex value minus the pinned lower-root value. Hence Phi D=I.
No upper edge enters any interior lower-prefix sum, so Pi Phi^T=0.
Using P=I-D G_0 D^T, these two exact identities give

    Pi P Phi^T=-Pi D G_0.                              (6)

This retains the projection's coupling to every vertex input. In
particular it does not assert Pi P=P Pi.

Here is a full-spectrum bound for the operator on the right. L186(5)
gives D^T D=L_D tensor I+I tensor Delta_T, with L_D the (N-1)-by-
(N-1) axial Dirichlet matrix of diagonal 2 and off-diagonal -1.
Diagonalize the entire transverse Dirichlet matrix Delta_T. For
each eigenvalue lambda>=0, the upper normal derivative block of
D G_0 is, up to sign, the row

    j^T(L_D+lambda I)^(-1),

where j is the last axial unit vector. This is an orthogonal direct
sum of rows; no transverse frequency is cut off. If mu_m,u_m are
the positive eigenpairs of L_D, the squared norm of that row is

    sum_m |j^T u_m|^2/(mu_m+lambda)^2
       <=sum_m |j^T u_m|^2/mu_m^2=||j^T L_D^(-1)||^2.

The last row of L_D^(-1) has entries s/N, s=1,...,N-1. To verify,
the sequence s/N has zero second difference at rows s<N-1,
value zero at s=0 and a last-row second difference equal to one
when its boundary value at s=N is set to zero. Thus it solves
L_D v=j. Symmetry gives the asserted row. Consequently

    ||Pi D G_0||_op^2
       <=sum_(s=1)^(N-1) s^2/N^2
        =(N-1)(2N-1)/(6N)<=N/3.                       (7)

The nonnegative-lambda comparison is merely an upper bound by an
auxiliary zero transverse eigenvalue; no actual mode is removed or
inserted into the covariance. Both axial Dirichlet ends and all
transverse end edges remain in (6)–(7).

### 2. The upper-output skew factor gains a square root

The transpose order matters: PH=P and H^T P=P, whereas PH^T=P is
generally false. L187's section 5 has been repaired to retain PH^T
and use its O(N) norm; its complete-output bound is unchanged.
On upper rows there is a better exact identity. By (6),

    Pi P H^T=Pi P-(Pi P Phi^T)D^T/2
             =Pi P+Pi D G_0 D^T/2
             =Pi(I+P)/2.                             (8)

Its operator norm is at most one. The positive projection identity
D G_0 D^T=I-P is used only in its stated order.

Because P S^(1/2)=S^(1/2), the original skew factor gives exactly

    Pi J_y S^(1/2)
      =-1/2{Pi P H^T diag(y)V S^(1/2)
                 -Pi P Phi^T q^T diag(y)H S^(1/2)}.    (9)

L187(11), including all prefix sources, gives

    ||V S^(1/2)||_HS+||H S^(1/2)||_HS<=C N^(5/2).

The endpoint map q has bounded degree and uniformly bounded operator
norm. For every ordinary normalized full Hodge mode y=e_l,
||y||_infinity<=C a^2. Apply (6)–(8) and the two-sided ideal
inequality in (9) to get

    ||Pi J_(e_l) S^(1/2)||_HS
       <=C a^2(1+sqrt(N))N^(5/2)<=C' N.               (10)

This proves (3), without a supremum contraction assumption on P or
a smoothness assertion for a rough tilted column. The complete-output
bound ||J_(e_l)S^(1/2)||_HS<=C N^(3/2) from the repaired L187(17)
is also retained below.

### 3. Bound both parts of the entire transport branch

Skewness of J_y and symmetry of M imply
Tr(J_y C_k M)=-Tr(J_y M C_k^T), by transpose and cyclicity.
Thus the summand of (2) is 6 Tr(J_y M C_k^T). Using the support
identities J_y=P J_y P and M=PMP removes only the redundant P's:

    Tr(J_y M C_k^T)
        =Tr(J_y M V^T diag(beta_k)).                   (11)

Select rows in this last diagonal trace using Pi and I-Pi. This is
an exact diagonal partition, not a commutation with P. For either
selector Pi_b set

    X_b=Pi_b J_y S^(1/2),
    Y_b=Pi_b diag(beta_k)V S^(1/2).

The selected trace in (11) is exactly 2Tr(X_b E Y_b^T). In particular
E remains signed, and Hilbert–Schmidt Cauchy–Schwarz bounds its
absolute value by 2||E||_op ||X_b||_HS ||Y_b||_HS.

L187(12),(15) and L186(12) supply, in the same order and with both
residual subtractions,

    ||E||_op<=C N,
    ||(I-Pi)beta_k||_infinity<=C p(k),
    ||Pi beta_k||_infinity<=C N p(k),
    ||Pi V S^(1/2)||_HS<=C N^2.                        (12)

On the complementary rows the complete-output estimates give

    ||X_bulk||_HS<=C N^(3/2),
    ||Y_bulk||_HS<=C p(k) N^(5/2),

so their trace is at most C p(k) N^5. On the upper rows, (10),(12)
give

    ||X_top||_HS<=C N,
    ||Y_top||_HS<=C p(k) N^3,

again giving C p(k) N^5. This retains the O(N) upper jump in beta;
it is offset by the improved projected skew factor, not deleted.
Multiply by 6a^2 and sum |d_(i;kl)|p(k) in the full expansion (1).
Since a^2=64/N^2, (2) follows for both actual probes.

The projected transport's upper-row partition in (11) is not the
original upper-output part of Q_3. The product rule used to define
C_k projects the entire U_n and couples rows. Therefore (2) does
not make its top transport part subcubic by (4) below.

### 4. Sharpen the original upper-output bound separately

L195's original part is

    -6a^2 sum_(k,l)d_(i;kl)
                    Tr(Pi J_(e_l) M U_(n_k)^T Pi).

Its exact unprojected upper-row cancellation gives
Pi U_(n_k)=Pi{diag(Vn_k)-diag(n_k)V}. L195(9), from the full
upper covariance counts and the actual smooth exterior column,
therefore supplies

    ||Pi U_(n_k) S^(1/2)||_HS<=C p(k) N^(5/2).          (13)

Pair (13) with (10) and ||E||_op<=CN in precisely that original
trace. Each trace is at most C p(k) N^(9/2). Its full exterior
sum with a^2 is O(N^(5/2)), proving (4). The scaled bound is
O(N^(-1/2)), so its zero cubic limit follows. All covariance input
rows, boundary sources and heat modes are still present.

Finally L188's exact split proves (5). Its unbounded-above-cubic
multiplier estimate and L194's sextic logarithm are not improved by
these transport inequalities. No signed lower bound, coefficient,
convergence claim or candidate solution follows. The proof is analytic;
no finite fixture, mathematical script or numerical cutoff is used.

## Mathlib

Full matching actual-probe estimate and supporting pinned-prefix
coverage: **not checked**. Supporting spectral theorem, finite trace
identities and Hilbert–Schmidt ideal inequalities: **not checked**;
unknown availability is not evidence of absence. These are standard
finite-dimensional named inputs. Their necessary specialization here
is the exact projected upper-prefix identity (6), the full Dirichlet
row estimate (7) and the original signed trace placement. No general
Gaussian or flow-renormalization theorem is reproved. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this bounded attempt within its original joint-group target.
