# L091 — Crossed residual pairing and a cubic bound for its gradient-base part

## Hypotheses

Use L085–L088's finite SU(2) forest Gaussian, actual L010 probes
i=3,6 and actual L018 residual. The forest is straight and lower-rooted
in direction 1, the box has relative all-face fixed-link conditions,
N is admitted and even, a=8/N and tau=1/16. The bare small-coupling
coefficient is taken at fixed mesh before refinement. Coordinates,
transposes and norms are ordinary dimensionless stored ones. Retain
every interior axial level, transverse end row, ordered plaquette pair
including coincidences and exterior heat mode.

Let X select all interior transverse links, S=Sigma_F,
K=X S X^T and V=X S A_F S X^T. Write Pcal,Qcal for the transverse
gradient and co-closed projections. On their respective ranges,

    K_g=M tensor P,  M_st=min(s,t),
    K_h=R Qcal,  R=(L_D tensor I+I tensor Delta_T)^(-1),
    K=K_g+K_h.                                           (1)

Both restrictions are positive definite. Use exactly L088(3)–(5)'s
actual alternating matrices Omega_k and real symmetric heat coefficients
c_(i;kl). With square roots on these ranges define

    Z_k=K^(1/2) Omega_k K^(1/2)
         =[[A_k,J_k],[-J_k^T,D_k]],
    W=K^(-1/2) V K^(-1/2)
         =[[E,F],[F^T,H]].                                (2)

Here A_k,D_k are antisymmetric; E,H are symmetric. J_k and F map
the co-closed range to the gradient range. These letters are local
block names, not the original probe or residual matrices. Projections
are fixed after normalized tilt differentiation; no base-law zero
is differentiated away.

## Conclusion

The complete distinct-row contribution has the exact identity

    T_UV=sum_(k,l)c_(i;kl) Tr(Z_k W Z_l^T).               (3)

Remove only T_gg and T_hh of L087 and L088. The six remaining sectors
then equal the following four signed traces:

    R_i:=T_UV-T_gg-T_hh
       =sum_(k,l)c_(i;kl) {
            Tr(J_k H J_l^T)+Tr(J_k^T E J_l)
            +2 Tr(A_k F J_l^T)+2 Tr(J_k^T F D_l) }.       (4)

In particular the P V Q and Q V P contributions with a gradient
base covariance are equal after the complete exterior sum, as are
those with a co-closed base covariance. They add with factor 2;
transpose symmetry provides no automatic cancellation of either pair.
This assertion does not assert that either actual trace is nonzero.

For the gradient-base crossed pair alone,

    R_gx:=2 sum_(k,l)c_(i;kl) Tr(A_k F J_l^T),
    |R_gx|<=C_i N^3.                                    (5)

Thus these two previously unbounded sectors have bounded a^3-scaled
values. Neither their convergence nor their sign or vanishing follows.
For comparison, the estimates proved below yield only O_i(N^(7/2))
for the last pair in (4) and O_i(N^4) for each diagonal crossed trace.
These insufficient upper bounds establish no signed growth and no
failure of a scaled limit. The complete-group limit and comparison
with -12 gamma D_i remain unresolved.

## Proof

### 1. Use the complete covariance and the actual residual

Import the exact covariance (1) from L085(2), with both interval
endpoints and the full relative spectrum. On the gradient range P
is the identity, so K_g's nonzero eigenvalues are those of M, each
repeated rank P=(N-1)^3 times. Since Tr M=sum_(s=1)^(N-1)s<=N^2/2
and M is positive,

    ||K_g||<=C N^2,  Tr K_g<=C N^5.                    (6)

L088(7),(9), including pinned rows, gives

    ||Cc K_h^(1/2)||<=1,
    ||K_h||<=C N^2,  Tr K_h<=C N^4.                    (7)

Here Cc=I tensor D is the full transverse circulation selector.
The path maps Bb,Bq have bounded row and column multiplicity and
therefore bounded operator norms on this exact finite cube.

There is a symmetric W as in (2) with

    ||W||<=C N.                                         (8)

To justify the full block bound, not just its two diagonal restrictions,
let H_X be X composed with the actual forest retraction on full Hodge
cochains, and let Sigma and A_0 be L018's full Hodge covariance and
free-gauge-invariant residual. Its quotient-law applicability gives
K=H_X Sigma H_X^T and V=H_X Sigma A_0 Sigma H_X^T. L020(11) bounds
||Sigma^(1/2) A_0 Sigma^(1/2)|| by C/a for precisely this displacement
and relative box. Hence, for every real y,

    |y^T V y|<= (C/a) y^T K y.

Conjugation by K^(-1/2), on the complete interior edge space, proves
(8). In particular ||E||,||F||,||H||<=C N. Forest prefixes in H_X
remain; they are not replaced by direct transverse Hodge rows. No
nonlinear cubic vertex is transferred to a different Gaussian law.

### 2. Bound the alternating blocks before treating the crossed residual

Import L088(5)'s full heat expansion, enlarging its mesh-independent
mode polynomial p if necessary:

    ||f_k||_infinity<=C a^2 p(k),
    ||b_k||_infinity+||q_k||_infinity<=C a p(k),
    sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i.                   (9)

L087(14) implies

    ||A_k||_HS<=C p(k) N^(1/2).                        (10)

For explicit applicability, U_T=T G^(1/2) is an isometry from the
pinned vertex space onto im P, because U_T^T U_T=I and U_T U_T^T=P.
The full level isometry identifies K_g with M tensor I. Under it,
Pcal Omega_k Pcal reduces to the plaquette Jacobian of L087(10),
since Cc Pcal=0. Conjugating its two endpoints by G^(1/2) is exactly
the covariance-weighted matrix in L087(13)–(14). Isometry invariance
of the Hilbert–Schmidt norm therefore gives (10), with the full
min(s,t)^2 sum intact. No level localization is used.

Likewise L088(10), without any new specialization, gives

    ||D_k||_HS<=C p(k) N.                              (11)

The crossed block obeys

    ||J_k||_HS<=C p(k) N^(3/2).                        (12)

Indeed split Omega_k into its two exterior-circulation terms and four
path/curvature terms exactly as in L088(3). A circulation term has
the form Bb^T M_(f_k) Bq or its transpose. Between the gradient left
and co-closed right covariance square roots its Hilbert–Schmidt norm
is bounded, using (6),(7),(9), by

    ||K_g^(1/2) Bb^T|| ||M_(f_k)||
                        ||Bq K_h^(1/2)||_HS
           <=C p(k) N a^2 N^2<=C' p(k) N.              (13)

The swapped path term has the same bound. Of the four path/curvature
terms, the two with Cc^T on the left vanish because K_g^(1/2) Cc^T=0.
The remaining two have curvature on the right and satisfy, for example,

    ||K_g^(1/2) Bq^T M_(b_k) Cc K_h^(1/2)||_HS
       <=||K_g^(1/2) Bq^T||_HS ||M_(b_k)||
                                      ||Cc K_h^(1/2)||
       <=C p(k) N^(5/2) a<=C' p(k) N^(3/2).            (14)

The other one uses Bb,q_k. These are fixed selector zeros, not zeros
of a differentiated covariance. Equations (13),(14) prove (12).
No multiplier was commuted through either covariance. The complete
gradient-prefix weight is retained in (6),(10),(14).

### 3. Compress all six sectors and check the signs of both pairs

L088's finite epsilon contraction proving (6) there does not require
co-closed covariance rows: it is the row-replacement identity for
arbitrary symmetric base C and residual V, with the actual exterior
rank-one expansion unchanged. Applying that identity to L085's full
C,V yields Tr(Omega_k V Omega_l^T K). Cyclically inserting K^(1/2)
and (2) gives (3). This imports the finite determinant contraction;
it does not redo or change L048's connected pairing classes or the
outside +1/2. L085's outside factor 3 is not included in T_UV.

Block multiplication, before any estimate, gives the gradient-base
trace terms

    Tr(A_k E A_l^T)+Tr(A_k F J_l^T)
         +Tr(J_k F^T A_l^T)+Tr(J_k H J_l^T),           (15)

and the co-closed-base terms

    Tr(J_k^T E J_l)-Tr(D_k F^T J_l)
         +Tr(J_k^T F D_l)-Tr(D_k H D_l).               (16)

The first term in (15) is T_gg after the heat sum, and the last term
in (16) is T_hh because D_l^T=-D_l. For the gradient crossed pair,
transposing a real scalar trace gives

    Tr(J_k F^T A_l^T)=Tr(A_l F J_k^T).                 (17)

For the co-closed crossed pair it gives, using antisymmetry,

    -Tr(D_k F^T J_l)=Tr(J_l^T F D_k).                 (18)

Exchange k,l in the full sum and use c_(i;kl)=c_(i;lk). Thus each
left side of (17),(18) equals its companion in (15),(16) after the
heat sum. Both signs are plus. Removing only T_gg,T_hh gives (4).
All rearrangements are legitimate: the mesh is finite, and (8)–(12)
together with (9) give absolute convergence of the displayed exterior
sum uniformly after the stated powers of N are allowed. Both ordered
plaquette orientations and coincidences were already retained in the
imported trace identity.

Finally finite Hilbert–Schmidt Cauchy–Schwarz gives

    |Tr(A_k F J_l^T)|<=||A_k||_HS ||F|| ||J_l||_HS
                         <=C p(k)p(l) N^3.            (19)

Sum with (9) and apply the factor 2 to obtain (5). The other crossed
pair costs at most C p(k)p(l) N^(7/2) by (8),(11),(12), while each
diagonal crossed trace costs C p(k)p(l) N^4 by (8),(12). These are
only upper bounds, not coefficients or necessary growth rates.

### 4. Relevance and limitations

L086, L087 and L090 give

    a^3 O_i-3 a^3 R_i ->0.                             (20)

Compensation with L084 would therefore require a^3 R_i to tend to
-4 gamma D_i, with L082's saved-table/IEEE qualifications on any
numerical reference comparison. Nothing here establishes existence
or value of that limit. The proved new bound reaches the N^3 threshold
for two sectors; four others still need joint signed control. Pairing
the crossed residual blocks by transpose alone supplies no cancellation,
so that proposed shortcut is abandoned. Their actual residual and
variable-coefficient compositions could still provide a different gain.

This is one bounded RESEARCH / REPRODUCTION proof attempt under the
unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The complete finite contraction is imported; the additional
specialization is the actual full-block compression and estimate (5).
This is local mathematical progress using recorded finite-matrix,
spectral and incidence methods, with no claim of novelty beyond the
sources checked. It supplies no N^2 remainder or logarithmic
coefficient. Other response jets, finite matching, the interacting
error <=c_box/2, continuum axioms, reflection positivity, infrared
control and finite positive mass remain unresolved. No candidate exists.

## Mathlib

Full matching coverage: **not checked**. Supporting block trace,
Hilbert–Schmidt inequalities and isometry coverage: **not checked**.
Unknown availability is not evidence of absence. The finite Gaussian
input is imported through L085/L088 from the existing contraction;
no additional external Ward, flow or continuum theorem is used.
