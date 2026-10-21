# L062 — Mixed same-row covariance derivatives are subleading at a² scale

## Hypotheses

Keep L061's actual SU(2) forest Gaussian, the two original probes
i=3,6, residual A, covariance S, bare coupling, tau=1/16 and admitted
even meshes a=8/N. Take the small-coupling coefficient at fixed mesh
first. Retain all upper transverse edges e=(v,w), all transverse
plaquettes p at levels 1<=s<=N-1, and every pinned end row. Use
L058–L061's incidence T, transverse circulation D, Green matrix
G=(T^T T)^(-1), projection P=TGT^T and transverse Laplacian Delta_T.
All matrix norms below are for ordinary dimensionless coordinates.

For p with ordered signed edges y1,...,y4 define the linear rows

    c_p=y1+y2+y3+y4, b_p=y1+y2, q_p=y2+y3.

Let R'_e select (d_e,u(v),(Tu)_e), with (Tu)_e=u(v)-u(w), and let
J'_p select (c_p,b_p,q_p). Define cross blocks

    C'=R' S J'^T, U'=R' SBS J'^T, V'=R' SAS J'^T,
    Z'=R'(SBSAS+SASBS)J'^T.

Blocks carry the suppressed pair indices (e,p). A row replacement
has the same meaning as in L061. Constants can depend on the fixed
probe, displacement, box and flow time, but not on the mesh.

## Conclusion

The complete mixed response has the exact representation

    M_i = 6 (T_Z + T_UV),
    T_Z = sum_(e,p) sum_j det C'[j:Z'],
    T_UV = sum_(e,p) sum_(j unequal k) det C'[j:U',k:V'].
                                                               (1)

Its three same-row terms obey

    |T_Z| <= C_i a^(-3/2), hence a² T_Z = O_i(a^(1/2)) -> 0.     (2)

This also bounds the sum of L061's original three same-row terms:
the two sums differ by a sign. No assertion is made that individual
terms are preserved under the row change. Both covariance path orders
in Z' and all six ordered distinct-row terms in (1) remain present.

No a² bound or limit for T_UV or the complete mixed response is proved.
In particular L059's conditional coefficient is not assigned to it.
All terms in (2) must be restored for subleading powers and the full
logarithm. Other cubic pairs, measure, insertion and flow jets, forest
compensation, finite matching, reflected error <=c_box/2, continuum
axioms and finite positive mass remain unresolved.

## Proof

### 1. Expose the transverse circulation without losing derivative terms

The alternating trilinear identity

    sum_(j<k<l) det(yj,yk,yl) = det(c_p,b_p,q_p)                 (3)

holds for arbitrary four vectors. Indeed expansion of the right side
gives coefficient +1 on each of 123,124,134,234; all terms with
repeated indices vanish. It holds also with zero fixed-boundary rows.
L058's Y therefore equals -sum_p det(c_p,b_p,q_p)/2. The upper
polynomial is sum_e det(d_e,u(v),u(w))/2, or equivalently
-sum_e det(d_e,u(v),(Tu)_e)/2. The product of these two signs is
positive. L061's color-isotropic Isserlis contraction gives, under
the normalized quadratic tilt with covariance S(alpha,beta),

    E_(alpha,beta)[CY] = (3/2) sum_(e,p)
                         det(R'_e S(alpha,beta) J'_p^T).       (4)

The factor is (+1/4) times the color factor 6. By L061, the mixed
normalized derivative is precisely kappa(f,r,C,Y). The covariance
derivatives are 2U', 2V', 4Z'. Differentiating (4) proves (1).

The same-row sum alone is preserved, up to the stated sign, by this
regrouping. To see this without ignoring product-rule terms, replace
S by S+t W for an arbitrary fixed W and differentiate the polynomial
determinant identity once in t. Set W=SBSAS+SASBS. This derivative
is exactly the sum of the three same-row replacements. It is a
first differential of the determinant, so no U',V' terms are invoked
to justify this particular equality. The distinct-row sum is retained
separately in the full mixed derivative (1).

### 2. Base blocks and their complete axial Hilbert–Schmidt bounds

L060's exact regression gives Cov(u,x_T(s))=sGT^T. Since DT=0,
both Cov(u,c_p) and Cov(Tu,c_p) vanish at the original Gaussian.
L061 gives Cov(d,x_T(s))=-g_s(Delta_T)(I-P). Consequently C' has
the block-entry pattern

                 [ K_1  K_2  K_3 ]
          C'  =  [  0   H_2  H_3 ] ,                         (5)
                 [  0   J_2  J_3 ]

where the displayed entries are arrays over every (e,p), including
all axial levels. These zeros are used only in undifferentiated C'.
No derivative of a zero entry is presumed zero.

The two path maps from transverse edges to b_p,q_p have uniformly
bounded operator norms: each row has two entries of magnitude one,
and each edge belongs to at most four transverse plaquettes. The
upper initial-endpoint map also has bounded norm, because each
vertex occurs in at most six retained edges. These assertions remain
true when pinned rows are set to zero.

L061's spectral estimate gives

    sum_s g_s(lambda)^2 <= 1/(2 sqrt(lambda)).                  (6)

The complete transverse relative spectrum has 0<lambda<=12 and
sum_lambda lambda^(-1/2)=O(N³), counting multiplicities. Explicitly,
each edge component has one cosine index in 0,...,N-1 and two sine
indices in 1,...,N-1. Its eigenvalue is 4 sum_j sin²(pi k_j/(2N))
>=4 |k|²/N². Shells max k_j=m contain at most C m² indices, and
sum_(m=1)^(N-1) C m² (N/m)=O(N³). Thus no zero mode or omitted
low-frequency sector is hidden in this estimate.

Taking the trace in (6), and using the bounded path maps, yields

    ||K_2||_HS + ||K_3||_HS = O(N^(3/2)).                      (7)

For K_1 the right map is D instead. The exact relation
D^T D=Delta_T(I-P) gives

    ||K_1||_HS² = sum_s Tr[g_s(Delta_T)^2 D^T D]
                <= (1/2) Tr sqrt(Delta_T) = O(N³).             (8)

Traces in (7)–(8) are over the full transverse edge space; bounding
the trace on ker P by that on the whole space is legitimate by
positivity. End rows and all levels 1,...,N-1 remain included.

For H the unsampled cross block is sGT^T; for J it is sP. L054's
full-spectrum Tr G=O(N³), the identity ||GT^T||_HS²=Tr G, and
||P||_HS²=rank P=(N-1)³ imply

    ||H_2||_HS+||H_3||_HS+||J_2||_HS+||J_3||_HS=O(N³),         (9)

because sum_s s²=O(N³). Bounded endpoint and path maps supply only
fixed multiplicative constants. Equations (7)–(9) are norms of
the entire arrays over (e,p), not bounds at one axial level.

### 3. Actual smooth exterior columns for Z'

Use L028's complete heat expansion, as extended to upper rows in
L029. Its ordinary covariance-square-root columns v_k and columns
z_k with the residual on that smooth input are lifts of smooth
relative fields with C¹ bounds p(k) and a²p(k), respectively.
All mode indices are retained. L029 gives the upper sizes

    |R'_e v_k| <= (a²,1,a) p(k),
    |R'_e z_k| <= a²(a²,1,a) p(k),                            (10)

componentwise, including both pinned endpoints.

For completeness the right-row specialization follows from the
actual forest lift, not an assumed smooth rough residual. For a
smooth relative one-form h its transverse lifted stored link is

    a h_mu(s,v) - a sum_(ell<s)
                         [h_1(ell,v+mu)-h_1(ell,v)].

Its magnitude is at most C a ||h||_C¹ since sa<=8. This estimate
continues to a transverse end edge: h_1 is zero on its pinned
transverse endpoint and the same smooth difference formula applies.
Tangential fixed edges are zero. A transverse circulation cancels
the entire axial path gradient exactly, leaving the circulation of
a h_T, of size C a² ||h||_C¹. Thus

    |J'_p v_k| <= (a²,a,a) p(k),
    |J'_p z_k| <= a²(a²,a,a) p(k).                            (11)

No upper axial potential enters these right rows, since s<N. These
are uniform statements for every transverse plaquette and all levels.

Writing l=(a²,1,a), r=(a²,a,a), the actual mixed block is

    Z' = sum_(k,m) exp[-tau(lambda_k+lambda_m)] B^rel_(i;km)
          [(R'v_k)(J'z_m)^T + (R'z_m)(J'v_k)^T].              (12)

This is L028's exterior identity and its transpose; neither residual
nor probe has been commuted through heat factors. Its uniformly
bounded B^rel and quadratic lower mode-energy bound imply absolute
summability after multiplication by p(k)p(m). Therefore

    |Z'_(j b)| <= C_i a² l_j r_b,                             (13)

uniformly over (e,p). In matrix form these entry orders are

                 [ a^6  a^5  a^5 ]
                 [ a^4  a^3  a^3 ] .                        (14)
                 [ a^5  a^4  a^4 ]

This estimate is for Z', which has external heat factors. It asserts
no such bound for the rough block V'=R'SASJ'^T.

### 4. Bound all three same-row determinants

Use (5). For j=1 only Z'_11 survives in the curvature column.
Its absolute sum is bounded by C a^6 times products of the H and
J Hilbert–Schmidt norms, hence O(a^6 N^6)=O(1).

For j=2, determinant expansion gives two kinds of terms: K_1 times
Z'_2b J_(5-b), b=2,3, and Z'_21 times K_b J_(5-b).
Cauchy–Schwarz for the complete (e,p) arrays gives respective bounds

    O(a³ N^(9/2)) and O(a^4 N^(9/2)).                         (15)

For j=3 the two kinds are K_1 H_b Z'_3,(5-b), and Z'_31 K_b H_(5-b).
Their bounds are respectively

    O(a^4 N^(9/2)) and O(a^5 N^(9/2)).                         (16)

Every determinant monomial occurs in these cases. Cauchy–Schwarz is
applied to absolute products, so no unstated signed cancellation
or common axial profile is assumed. Since N=8/a, their total is
O(1+a^(-3/2)+a^(-1/2)+a^(1/2))=O(a^(-3/2)), proving (2).

The analytic checks are the four signs in (3), the factor +6 in
(1), the first-differential justification for isolating T_Z, the two
base-law zeros, complete spectral shell counts, all pinned endpoint
cases, both path orders in (12), and every monomial in (15)–(16).
No numerical check or mathematical script is needed for these finite
identities and inequalities.

This is local REPRODUCTION using standard determinant algebra,
Isserlis' theorem and matrix Cauchy–Schwarz, under the unchanged
SPECIALIZE assessment `drafts/literature/2026-09-26-current-target.md`.
The necessary regulator specialization is the mixed axial sum and
its actual exterior columns. General flow finiteness and stress
matching are not reproved or assigned additional boundary hypotheses.
The result reduces a relevant part of the response calculation,
without claiming progress beyond the inspected source methods.

## Mathlib

Coverage of this full mixed same-row bound: **not checked**.
Supporting determinant differentials, finite-dimensional Isserlis
contractions, matrix Cauchy–Schwarz and finite spectral calculus:
**not checked**. No matching Mathlib theorem or absence claim is made.
Load-bearing specialized estimates and their pinning hypotheses are
proved above or imported from the stated local results.
