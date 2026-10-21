# L087 — The two-gradient distinct-row sector is subleading

## Hypotheses

Use L085–L086's SU(2) forest Gaussian, both actual L010 probes i=3,6,
actual L018 residual, straight lower-rooted direction-1 forest, all-face
relative pinned box, admitted even N, a=8/N and tau=1/16. Take the
bare small-coupling coefficient at fixed mesh before refinement. All
coordinates and norms below are ordinary dimensionless stored ones.
Keep all transverse plaquettes at all levels 1<=s<N, ordered pairs
including coincidences, pinned end rows and the full exterior heat sum.

Let X select all interior transverse links from forest coordinates,
K=X S X^T and V_link=X S A S X^T, with S=Sigma_F. On the concatenated
transverse edge space put Pcal=I tensor P, where P=T G T^T and
G=(T^T T)^-1 are L050's full relative transverse projection and Green
matrix. For alpha=(s,p), let Lambda_alpha select the three rows
(c,b,q) of L085 at that level. Write U_ab=J_alpha S B_i S J_beta^T
as there, and define only for this sector

    Cg_ab=Lambda_alpha Pcal K Pcal Lambda_beta^T,
    Vg_ab=Lambda_alpha Pcal V_link Pcal Lambda_beta^T,
    T_gg=sum_(alpha,beta) sum_(j!=k)
                  det Cg_ab[j:U_ab,k:Vg_ab].                 (1)

Thus both rough lines, the undifferentiated covariance C and the
residual covariance V, are projected onto transverse gradients at
both endpoints. U is unchanged. This is one multilinear sector of
L086's T_UV, rather than the whole distinct-row class. Projecting V
here is a fixed linear-map operation; it does not differentiate a
base-law covariance zero.

## Conclusion

For each actual probe,

    |T_gg| <= C_i N^2,       a^3 T_gg=O_i(a) -> 0.           (2)

The proof first sums each complete pinned transverse plaquette layer
with its actual exterior circulation. The resulting alternating
vertex-edge form has coefficients equal to differences of neighboring
circulations. This is a signed gain before taking absolute values;
it is not a small raw-link covariance or a smooth-column estimate
for rough V.

Combining with L086, the leading-scale problem is reduced further to

    a^3 O_i - 3 a^3 (T_UV-T_gg) -> 0.                       (3)

Existence or value of this remaining scaled limit is not established.
Its value would still have to be -4 gamma D_i to compensate L084.
Sectors containing a transverse co-closed rough endpoint, all finer
powers/logarithms, other response jets, finite matching, interacting
error <=c_box/2 and the continuum/infrared/mass requirements remain
unresolved. There is no complete-group coefficient or candidate.

## Proof

### 1. Actual potential covariance and residual form bound

Let L_phi=(I tensor G T^T)X on forest coordinates. Its output phi_s
is the unique pinned transverse potential of P x_T(s). Import L085(2)
and the full cochain identities in L050. With M_st=min(s,t),

    K_phi=L_phi S L_phi^T=M tensor G,
    V_phi=L_phi S A S L_phi^T,
    P x_T(s)=T phi_s.                                      (4)

The transverse co-closed resolvent in L085(2) is annihilated by T^T
on either side. The Brownian-prefix covariance is retained exactly,
including both interior levels. M is positive definite: it is the
covariance of the first N-1 successive partial sums of independent
unit increments. G is positive by the pinned vertex spectrum. Hence
K_phi is positive definite.

The actual residual satisfies the two-sided quadratic-form bound

    -C N K_phi <= V_phi <= C N K_phi.                       (5)

To check applicability rather than assume a small rough residual,
use L018's free-gauge-invariant quadratic lift: A annihilates the
full free gradient sector, and forest retraction gives the same
quadratic residual and law. The maps to phi are actual retracted
linear rows in this Hodge law. If H denotes their full Hodge row map,
Sigma its covariance and A_0 its residual matrix, this gives

    K_phi=H Sigma H^T,
    V_phi=H Sigma A_0 Sigma H^T.

L020, proof section 3, (11), gives
||Sigma^(1/2) A_0 Sigma^(1/2)||<=C/a. It has exactly the present
residual, displacement and relative box; physical orthonormal and
stored scale factors cancel in this whitened matrix, as in L028's
normalization. Therefore, for every real y,

    |y^T V_phi y|
       <=(C/a)||Sigma^(1/2) H^T y||^2
       =(C/a)y^T K_phi y.

Since a=8/N, this proves (5). No nonlinear cubic is transferred to
an unmodified Hodge vertex. Equivalently
V_phi=K_phi^(1/2) W K_phi^(1/2) with W symmetric and ||W||<=C N.

### 2. Preserve the complete exterior heat expansion

L028(11),(13), with the residual omitted from the covariance product,
gives the actual U expansion

    U_ab=sum_(k,l) c_(i;kl) (J_alpha v_k)(J_beta v_l)^T,
    c_(i;kl)=exp[-tau(nu_k+nu_l)] (B_i^rel)_kl.              (6)

Here v_k are its ordinary-coordinate covariance-square-root columns;
nu_k are the physical relative mode energies. This is the same
normalization used for Z in L086; no forest-Hessian flow is substituted.
Define the actual exterior circulation f_(k;s,p)=c_p v_k. There is a
mesh-independent polynomial p(k) such that, uniformly in s,p,

    |f_(k;s,p)|<=C a^2 p(k),
    |f_(k;s,p)-f_(k;s,p')|<=C a^3 p(k)                     (7)

when p,p' are neighboring parallel transverse plaquettes sharing an
edge. The second estimate is needed in addition to L086's first one.

Indeed the forest prefix is an exact transverse gradient and cancels
from c_p. Thus f is the direct stored circulation of
 a nu_k^(-1/2) times the smooth relative product mode. For a mu nu
plaquette starting at v it is a nu_k^(-1/2) times

    h_mu(v)-h_mu(v+nu)+h_nu(v+mu)-h_nu(v).

Here h_mu(v) denotes the value at the center of the mu-edge starting
at v; thus all staggered sample locations remain the actual ones.
Integral difference formulas bound this by a^2 times the C^1 norm,
and a transverse shift of it by a^3 times the C^2 norm. L026's exact
normalized sine/cosine modes and uniform physical spectral gap bound
these norms by a fixed polynomial in k. Fixed tangential edges have
zero samples by the relative sine conditions, so the same formula
holds at all retained boundary-adjacent plaquettes. There is no s=N
jump in this group. Every axial mode remains.

L028's bounded B_i^rel and nu_k>=c|k|^2 give

    sum_(k,l) |c_(i;kl)| p(k)p(l)<=C_i.                    (8)

Thus the polynomial can be enlarged for the C^2 bound without losing
the uniform full heat sum. No internal covariance frequency is cut off.

### 3. Sum the pinned plaquette Jacobian before estimating

At one level regard b_p,q_p as rows on vertex potentials, by composing
the corresponding edge paths with T. In the positive mu nu traversal
write the four vertices as 0,mu,mu+nu,nu. The exact telescoping rows are

    b_p phi=phi_0-phi_(mu+nu),
    q_p phi=phi_mu-phi_nu.                                 (9)

For any plaquette coefficients f_p, define the antisymmetric matrix

    Omega_s(f)=sum_p f_p (b_p^T q_p-q_p^T b_p).             (10)

Its bilinear value on phi,psi is, for each plaquette, the sum of
oriented perimeter edge wedges: coefficient +f_p on the lower mu
edge, -f_p on the upper mu edge, -f_p on the lower nu edge and +f_p
on the upper nu edge. This follows by expanding (9): the four terms
are respectively the wedges on pairs (0,mu), (0,nu),
(mu+nu,mu), (mu+nu,nu), with signs +,-,-,+ in that ordering.
There is no diagonal vertex pair left.

Sum every transverse plaquette at this level. An oriented edge with
both endpoints interior has both neighboring plaquettes in every
incident transverse plane. Its coefficient d_e is consequently a
signed sum of differences of adjacent parallel f's. An edge meeting
a pinned boundary vertex contributes a zero wedge because that
vertex has phi=psi=0. Set d_e=0 there without changing the bilinear
form. Edges lying in a transverse boundary face are absent in the
relative edge space and would also contribute zero. These cases
exhaust the finite cube; no collar or boundary remainder is omitted.
For the actual f_(k;s,p), (7) therefore gives

    ||d_(k,s)||_infinity<=C a^3 p(k).                     (11)

Let E select the initial endpoint of each oriented relative edge
(zero when that endpoint is pinned). Its norm is bounded by a fixed
constant since every vertex begins at most three edges. With
(T phi)_e=phi(v)-phi(w), the exact edge-wedge identity gives

    Omega_(k,s)=T^T diag(d_(k,s)) E
                     -E^T diag(d_(k,s)) T.                (12)

For example its bilinear value is
sum_e d_e[phi(v)psi(w)-phi(w)psi(v)], with the perimeter signs above.
On an end edge (12) is zero as a bilinear form, even when just one
endpoint is pinned. This verifies the sign and pinned applicability.

The full vertex spectrum also gives Tr G<=C N^3. Explicitly its labels
are k_2,k_3,k_4 in 1,...,N-1, eigenvalues at least 4|k|^2/N^2,
and shells max k_j=m have at most C m^2 labels. Summing inverses
bounds Tr G by C N^2 sum_(m=1)^(N-1) 1<=C' N^3. Also
||T G^(1/2)||=1. Apply (11)–(12) to get

    ||G^(1/2) Omega_(k,s) G^(1/2)||_HS
       <=2 ||E|| ||d_(k,s)||_infinity ||G^(1/2)||_HS
       <=C a^3 p(k) N^(3/2).                              (13)

This estimate uses the first-difference form after signed summation;
a bound on the unsummed two-gradient product would not give (13).

### 4. Restore the complete two-level weights and both V placements

Let Omega_k be block diagonal in levels, with blocks Omega_(k,s).
Using (4), cyclicity of the finite trace and block multiplication,

    ||K_phi^(1/2) Omega_k K_phi^(1/2)||_HS^2
       =sum_(s,t) M_st^2
          <G^(1/2) Omega_(k,s) G^(1/2),
           G^(1/2) Omega_(k,t) G^(1/2)>_HS
       <=C a^6 p(k)^2 N^3 sum_(s,t) min(s,t)^2
       <=C a^6 p(k)^2 N^7
       <=C' p(k)^2 N.                                    (14)

The displayed inner product may have either sign; its absolute bound
is used only after the exact full weighted identity. All s,t and their
actual min(s,t) weights remain. No axial profile is replaced or localized.

Because DP=0, Cg and Vg have zero first row and first column by their
fixed projected selectors. In (1) only the placements (j,k)=(1,2)
and (1,3) survive. Their complete sum for a fixed pair is exactly

    U_11 [ Vg_22 Cg_33 - Vg_23 Cg_32
                      + Cg_22 Vg_33 - Cg_23 Vg_32 ].       (15)

The other four determinants have a zero row. Only U_11 contributes
to the surviving two determinants because the first columns of their
other rows are zero. This is not a derivative of an unprojected zero.

Substitute (6) into (15), and express the b,q gradient rows using
(9) and (4). Expanding the two alternating matrices (10) gives the
exact finite identity

    T_gg=sum_(k,l) c_(i;kl)
                    Tr(Omega_k V_phi Omega_l^T K_phi).     (16)

For each alpha,beta its four trace terms are
Vg_33 Cg_22, -Vg_32 Cg_23, -Vg_23 Cg_32, Vg_22 Cg_33,
multiplied by f_(k;alpha) f_(l;beta), precisely (15).
Thus both residual placements, every ordered pair and coincidences
are retained; there is no extra 2 or 3 in (16).

Use (5) in (16). Cauchy–Schwarz for finite Hilbert–Schmidt products
and (14) give, for each k,l,

    |Tr(Omega_k V_phi Omega_l^T K_phi)|
       <=||W|| ||K_phi^(1/2) Omega_k K_phi^(1/2)||_HS
                 ||K_phi^(1/2) Omega_l K_phi^(1/2)||_HS
       <=C N^2 p(k)p(l).                                 (17)

Then (8) proves (2). The residual remains rough throughout; its actual
O(N) form bound is used only after the transverse signed endpoint gain.
This differs from the stopped generic absolute-array closures in
ATTEMPTS/019–020 and the false upper-source transfer in ATTEMPTS/026.

Finally L085's O_i=3(T_Z+T_UV) and L086's a^3 T_Z->0 combine with
(2) to prove (3). The factor 3 is applied once, after the original
ordered-pair +1/2 normalization. The comparison value is unchanged,
with L086's reference to L084 and its qualified diagnostic signs.
No sign or limit is assigned to T_UV-T_gg.

### 5. Scope and remaining sectors

The unchanged EXPLORE assessment is
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite Isserlis contraction is imported through L085 from L048,
with the same law, actual observables and ordered region. The required
additional specialization is the signed pinned plaquette sum and its
full covariance-weighted estimate. This is local REPRODUCTION of the
recorded finite Gaussian, incidence and spectral methods, without a
claim of a result beyond the sources checked or certified novelty.

For precision, C in T_UV splits into its gradient block Cg and its
co-closed resolvent block. V splits into its four Pcal/(I-Pcal) endpoint
blocks. Multilinearity in these two rough lines makes (1) the unique
Cg,Vg sector. The remainder in (3) includes every other such sector,
with all six placements; it is not presumed smaller. The two-gradient
base term of L085(6) belonged instead to T_Z and was already bounded
in L086. No bound is counted twice. The present analytic proof requires
no numerical script, source refresh or assumption about D_i's value.
Independent response-jet and construction gaps remain as stated above.

## Mathlib

Full matching coverage: **not checked**. Supporting incidence, finite
spectral trace, Hilbert–Schmidt and determinant-differential coverage:
**not checked**. Unknown availability is not absence. The standard
Gaussian input is imported through L085/L048; no general Ward/flow
finiteness theorem or new continuum boundary hypothesis is used.
