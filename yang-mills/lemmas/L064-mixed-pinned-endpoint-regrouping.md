# L064 — Pinned endpoint regrouping of the remaining mixed terms

## Hypotheses

Keep L062–L063's actual straight-forest SU(2) Gaussian, covariance S,
residual A, both original probe matrices B_i, tau=1/16, bare coupling,
and admitted even meshes a=8/N. Take the small-coupling coefficient at
fixed mesh first. Retain every upper edge e=(v,w), all transverse
plaquettes p at every level 1<=s<N, and all pinned end edges. Use
exactly their maps R'=(d,u(v),Tu), J'=(c,b,q) and blocks C',U',V'.
Constants may depend on the fixed displacement, probe, flow time and box.
All norms below use ordinary dimensionless coordinates.

At the base law write the rows of C' as K_e,p, H_v,p and (TH)_e,p.
Thus H_v,p=(0,H_2,H_3), with T acting on its upper vertex index.
Write W_v,p for the row of the actual mixed residual from u(v) to
(c_p,b_p,q_p). Then rows 2 and 3 of V' are W_v,p and (TW)_e,p.
Boundary vertex values of H,W and all exterior potential columns are zero.

## Conclusion

For L063's four-term T_rem there is the exact identity

    T_rem = sum_(k,l) c_(i;kl) sum_(e,p) {
      r_k(e) [det(t_l(p),W_v,p,(TH)_e,p)
               +det(t_l(p),H_v,p,(TW)_e,p)]
      -(Th_k)_e det(K_e,p,t_l(p),W_v,p+W_w,p) },             (1)

where c_(i;kl), r_k,h_k,t_l are the complete heat expansion specified
below. The signed endpoint pairing in the second line replaces a rough
difference of W by a smooth difference of h, after summing every upper
edge. It does not discard a differentiated curvature-column zero.

The available general residual norm gives only

    ||W_1||_HS = O(N^3),
    ||W_2||_HS+||W_3||_HS = O(N^4),
    |T_rem| <= C_i N^(7/2) = O_i(a^(-7/2)).                 (2)

The first line of (1) is O(N^3). In its second line, the two determinant
monomials containing K_1, a path component of t, and a path component of
W have only an O(N^(7/2)) bound; the other four are O(N^(5/2)).
These bounds fall short of O(N^2), and in particular do not bound a²
T_rem or give its limit. They are upper bounds, with no growth or sign
claim. This is a bounded exploration of the joint estimate, not an
evaluation of the mixed coefficient or the cutoff logarithm.

The subsequent right-circulation test in proof section 5 gives a
uniform operator bound for the complete K_1 array. Composing it with
the actual alternating smooth-path map and the generic residual norm
still gives only O(N^(7/2)) for its two path/path monomials. That local
path map does not annihilate arbitrary transverse gradients. Neither
fact gives a lower bound or rules out a sharper signed estimate.

The five terms removed by L062–L063 remain needed below a² scale.
Other/other cubic pairs, measure, insertion/flow jets, nonlinear forest
compensation, finite matching, the interacting reflected-error threshold
c_box/2, continuum axioms, infrared control and finite positive mass
remain unresolved.

## Proof

### 1. Complete exterior expansion and exact endpoint relations

Use L062's exterior columns v_k and the relative probe form, with

    c_(i;kl)=exp[-tau(lambda_k+lambda_l)] B^rel_(i;kl),
    r_k(e)=(d v_k)_e, h_k(v)=(u v_k)_v,
    t_l(p)=J'_p v_l.

Here d and u denote the upper row selection maps, not an additional
differential. L062–L063 give, for one fixed polynomial p(k),

    ||r_k||_infinity <= a² p(k),
    ||h_k||_infinity <= p(k), ||Th_k||_infinity <= a p(k),
    |t_l(p)| <= (a²,a,a) p(l),
    sum_(k,l) |c_(i;kl)| p(k)p(l) <= C_i.                    (3)

These include pinned end rows and all mode indices. In particular U'
is the sum of the rank-one blocks with rows r_k t_l, h_k(v)t_l and
(Th_k)_e t_l. The exact relations C'_3=TH and V'_3=TW follow from
R'_3=TR'_2 at the linear-map level. They are valid for the residual
block even though C'_21=C'_31=0 only at the base law.

For one exterior product, the (1,2) and (1,3) placements are precisely
the two determinants in the first line of (1). The (2,3) and (3,2)
placements have sum

    h_k(v) det(K,t_l,TW) + (Th_k)_e det(K,W_v,t_l)
      = det(K,t_l,h_k(v)(TW)_e-(Th_k)_e W_v).                (4)

There is no factor 6 in T_rem; it is multiplied by 6 only in the
complete response of L063(3). All four ordered placements are in (4)
and the first line of (1), with the original signs.

### 2. Sum the pinned difference before estimating

For a scalar vertex field h and a vector-valued vertex field W, direct
endpoint evaluation gives

    h(v)(TW)_e-(Th)_e W_v
      = T(hW)_e-(Th)_e(W_v+W_w).                            (5)

Indeed both sides equal h(w)W_v-h(v)W_w. Boundary evaluations are
zero, so (5) also holds on an end edge; no boundary remainder is added.

L061–L062's full base covariance has, for each axial level s,

    Cov(d,x_T(s))=-g_s(Delta_T)(I-P), P=TGT^T.

Since T^T(I-P)=0 and g_s(Delta_T) commutes with P, every fixed p
and component b satisfies T^T K_(.,p,b)=0. Thus for fixed p,l,

    sum_e det(K_e,p,t_l(p),T(h_k W)_e,p)=0.                  (6)

To verify (6), expand the determinant: each summand is a constant
component of t_l(p) times K_(.,p,b)^T T(h_k W_(.,p,c)). It is zero
by the displayed co-closed identity. Summation uses the complete pinned
incidence and every upper edge. Substitution of (5)–(6) into (4) proves
(1). At each mesh the mode sums are finite; (3) gives uniform absolute
summability for the bounds that follow. No variable multiplier is
commuted with G, the residual, or a covariance.

### 3. A justified coarse norm for the actual mixed residual

Let Sigma be the full Hodge covariance, A_0 its actual residual, L_u
the full-link row map to the sum of N axial entries u, and M_b the
full-link map to the forest-lifted right column b=1,2,3 over all p.
L018's quotient law and free gauge invariance of the quadratic residual
give the exact product

    W_b=L_u Sigma^(1/2) R_a Sigma^(1/2) M_b^T,
    R_a=Sigma^(1/2) A_0 Sigma^(1/2).                         (7)

This is a transfer of quadratic covariance blocks with their actual
lifted rows. It does not transfer the cubic vertices to unmodified
Hodge coordinates. The R_a in (7) has the same operator norm as the
physical orthonormal whitened residual of L020, proof section 3,
whose equation (11) gives ||R_a||<=C/a=O(N). Indeed Sigma=a^-2
Delta_phys^-1 and A_0=a² N_a, so the scale factors cancel in R_a.

L060 gives L_u Sigma L_u^T=NG. L054's full-spectrum Tr G=O(N³)
therefore implies ||L_u Sigma^(1/2)||_HS=O(N²). For M_1, the
forest lift preserves the actual circulation c. The full relative
Hodge projection D_1 Sigma D_1^T has norm at most one, so

    ||Sigma^(1/2) M_1^T|| <= 1.                             (8)

For M_2,M_3 one needs all levels jointly, rather than link variances
alone. Their two-link path maps have bounded norms by L062. The
concatenated transverse forest lift is z_T+J_N T_ax z_1, where J_N
takes every axial prefix sum and T_ax is the transverse pinned
incidence at every axial edge coordinate. Each axial prefix matrix
has Frobenius norm at most N, hence ||J_N||<=N. L026's relative
component inequality gives T_ax Sigma_1 T_ax^T<=I, including all
axial indices: for the three directions jointly, sum_mu T_mu^T T_mu
is the transverse part of the component-1 Laplacian and is at most
that full Laplacian. Consequently

    ||J_N T_ax Sigma_1^(1/2)|| <= N.

The direct transverse block has covariance operator norm at most
C N² by the full Hodge gap. These two component spaces are orthogonal;
alternatively the triangle inequality suffices. The forest lift to
all transverse links therefore has whitened operator norm O(N), and

    ||Sigma^(1/2) M_2^T||+||Sigma^(1/2) M_3^T|| <= C N.       (9)

The missing endpoint value in an end edge is zero in T_ax itself.
Tangential fixed links have zero rows. Thus no interior-only variance
estimate or localization assumption has entered (9).

Apply ||XYZ||_HS<=||X||_HS||Y||||Z|| to (7), using (8)–(9).
This proves the two W estimates in (2). Endpoint pullbacks of W,
and TW, have Hilbert–Schmidt norms bounded by fixed multiples of
these estimates: each upper vertex occurs in at most six edges.

### 4. Test the threshold without assuming a signed cancellation

L062 gives the full-array bounds ||H_2||_HS+||H_3||_HS=O(N³),
||(TH)_2||_HS+||(TH)_3||_HS=O(N³), and ||K_b||_HS=O(N^(3/2))
for b=1,2,3. They retain all p and axial levels. H_1=(TH)_1=0 at
the base law, whereas W_1 is retained.

For either determinant in the first line of (1), expansion gives
two monomials with t_1, a path component of W and a path component
of H or TH, and two with a path component of t, W_1 (or TW_1),
and a path component of H or TH. Using (3), Cauchy–Schwarz on the
complete arrays, and a=8/N, their bounds are

    C_i a^4 N^4 N^3 = O_i(N^3),
    C_i a^3 N^3 N^3 = O_i(N^3).                             (10)

In the second line of (1), the two K_1 monomials have bound

    C_i a² N^(3/2) N^4 = O_i(N^(7/2)).                      (11)

The other four monomials have, respectively, bounds

    C_i a³ N^(3/2) N^4 = O_i(N^(5/2)),
    C_i a² N^(3/2) N^3 = O_i(N^(5/2)).                      (12)

The complete heat sum (3) absorbs the polynomial mode factors.
Equations (10)–(12) prove the last bound in (2). These are absolute
bounds after the exact signed cancellation (6); no further cancellation
is assumed. Without (5)–(6), the same generic estimates for the two
placements in (4) would give only O(N^(9/2)), so the endpoint sum gains
one power. The achieved N^(7/2) remains larger than the required N².

An independent bound on the first line is also still needed for the
required threshold; controlling (11) alone would not finish T_rem.
For that reason this step records EXPLORATION / REPRODUCTION under the
unchanged SPECIALIZE assessment, rather than an a²-scale advance or
informative noncancellation result. Standard finite matrix inequalities
and the exact local residual are specialized; general flow
renormalizability and stress matching are not reproved.

### 5. Subsequent test: retain the right circulation in operator order

This section records the separate bounded attempt
YM-20261007-081-mixed-right-circulation-test. It tests the two K_1
monomials of (1), without changing the four-placement identity or
claiming the missing a²-scale bound.

Let X denote the vector of all transverse forest links at all levels
1<=s<N, with zero fixed rows retained. Write L_X for its full Hodge
lift and L_u for the lift of u as in (7). Let D be the transverse
circulation at one level, and let K_1 be the upper-edge by all-level
plaquette matrix, with blocks

    (K_1)_s=-g_s(Delta_T)(I-P)D^T.

Unlike its Hilbert–Schmidt norm, its operator norm is bounded
independently of N. Indeed the full relative identities in L062 give
D^T D=Delta_T(I-P), with P commuting with Delta_T. Hence

    K_1 K_1^T=sum_s g_s(Delta_T)^2 Delta_T(I-P),
    ||K_1||² <= (1/2)||sqrt(Delta_T)|| <= sqrt(12)/2.        (13)

This uses L061's complete spectral sum, including every level and
every positive eigenvalue. No multiplier has been commuted with P
or a fractional power. The bound is on the full pinned spaces.

For one exterior column t_l, define the actual alternating path map
Q_l from X to all transverse plaquettes by

    (Q_l X)_p=t_l,2(p) q_p(X)-t_l,3(p) b_p(X).              (14)

The bounded two-link path maps of L062 and (3) imply
||Q_l||<=C a p(l). Let E_+ be the upper vertex-to-edge endpoint-sum
map, (E_+z)_e=z(v)+z(w), with pinned values zero. Its norm is
uniformly bounded: each vertex meets at most six edges, so endpoint
Cauchy–Schwarz gives ||E_+z||²<=12||z||². Set
g_k(e)=(Th_k)_e and let M_(g_k) be its diagonal multiplier.

The full right mixed residual block, before selecting its paths, is

    W_X=L_u Sigma^(1/2) R_a Sigma^(1/2) L_X^T.              (15)

This is precisely the quadratic transfer (7); no nonlinear vertex
has been replaced by an unmodified Hodge vertex. For this exterior
product, its K_1 path/path contribution is exactly

    S_kl=-sum_(e,p) g_k(e) (K_1)_e,p (E_+W_X Q_l^T)_e,p
         =-Tr[K_1 Q_l L_X Sigma^(1/2) R_a
                       Sigma^(1/2) L_u^T E_+^T M_(g_k)].   (16)

The sign follows by expanding the second line of (1): its K_1
minor is t_l,2(W_v+W_w)_3-t_l,3(W_v+W_w)_2. Thus both monomials
are kept jointly, with their actual endpoint sum and right paths.
All products and the trace in (16) are finite at fixed mesh.

L063(7) bounds every right-link variance, including normal end edges,
by N+8; tangential fixed links have zero variance. There are O(N^4)
such links. Therefore

    ||L_X Sigma^(1/2)||_HS²=Tr(L_X Sigma L_X^T)=O(N^5).      (17)

Section 3 already gives ||L_u Sigma^(1/2)||_HS=O(N²) and
||R_a||=O(N). Using (13)–(17), ||M_(g_k)||<=a p(k), and
|Tr(FH)|<=||F||_HS||H||_HS for rectangular F,H, yields

    ||K_1 Q_l L_X Sigma^(1/2)||_HS
                         <= C a p(l) N^(5/2),
    ||R_a Sigma^(1/2) L_u^T E_+^T M_(g_k)||_HS
                         <= C a p(k) N³,
    |S_kl| <= C a² p(k)p(l) N^(11/2).                     (18)

Summing the complete heat coefficients with (3) gives O(N^(7/2)),
the same insufficient scale as (11), versus the required O(N²).
This calculation uses the circulation and fractional spectral gain
before applying the residual bound; it does not repeat an entrywise
estimate or pretend that an operator norm is a Hilbert–Schmidt norm.
The gain in (13) is offset by (17). It supplies no signed growth.

One proposed shortcut in (14) also fails at the local-map level.
On an interior plaquette with successive vertices
v, v+mu, v+mu+nu, v+nu, take the four signed edges in that order.
For a pinned vertex field z and the convention (Tz)_(v,w)=z(v)-z(w),

    b_p(Tz)=z(v)-z(v+mu+nu),
    q_p(Tz)=z(v+mu)-z(v+nu),
    (Q_l Tz)_p=t_l,2[p][z(v+mu)-z(v+nu)]
                 -t_l,3[p][z(v)-z(v+mu+nu)].               (19)

The four corners are distinct interior vertices. If t_l,2[p]!=0,
the field equal to one only at v+mu makes (19) nonzero. If that
coefficient is zero but t_l,3[p]!=0, use the field equal to one
only at v. These are admissible pinned fields. Thus Q_l T is not
zero whenever either path coefficient is nonzero on an interior
plaquette. This statement is conditional on the actual coefficients;
it neither substitutes an arbitrary probe nor asserts that (16) or
the complete heat sum is nonzero. In particular it gives no lower
bound after K_1, R_a, and the signed heat coefficients are applied.
It prevents replacing the right lift by its co-closed part merely
because the base K_1 contains a circulation.

The bounded test therefore does not close the threshold. Park the
combination of this spectral bound, generic residual norm, and
absolute trace inequality. A materially different next test is to
use the actual residual's axial-component structure before taking
its operator norm. L054's bounded upper/upper compression remains
an input only in its proved scope; no mixed extension is assumed.
The other four endpoint monomials and the first line of (1) also
remain independently unresolved. This additional test is
EXPLORATION / REPRODUCTION under the unchanged response assessment.

## Mathlib

Coverage of the full regrouping and coarse mixed bound: **not checked**.
Supporting determinant multilinearity, finite matrix norm inequalities,
finite spectral calculus, pinned incidence algebra and Cauchy–Schwarz:
**not checked**. No matching theorem or absence
claim is made. The load-bearing pinning, spectrum, quadratic transfer
and residual norm are justified above with their local inputs.
