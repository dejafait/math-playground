# L069 — The axial-prefix part of the first mixed pair is O(N²)

## Hypotheses

Keep L064's actual fixed-mesh SU(2) coefficient, straight lower-rooted
forest, residual A_0, both original probes i=3,6, tau=1/16 and admitted
even meshes a=8/N. Coordinates, transposes and norms are ordinary
dimensionless ones. Retain every upper transverse edge e=(v,w), all
transverse plaquettes p at levels 1<=s<N, all pinned end rows, and
L064's complete exterior coefficients c_(i;kl), r_k(e), t_l(p).
Take the small-coupling coefficient at fixed mesh first.

Use L068's exact signed right axial forest lift
J T_ax I_1^T, with prefixes (Jz)_s=sum_(r<s)z_r. Use its normalized
axial-zero embedding E_0, Sigma_1=I_1^T Sigma I_1 and the pinned
three-dimensional vertex inverse G. The separately pinned top potential
is not a prefix at level N. Let B_2,B_3 select the actual two-link
right paths b_p,q_p at every retained level, and D select their transverse
circulation c_p. Tangential fixed rows and pinned vertex evaluations
are zero.

Split only the right lift of L064's mixed residual row W into direct
transverse and axial-prefix summands. Denote the latter by W^ax. Keep
the full base row H, rather than replacing it by a selected covariance.
The base has H_1=0 and unsampled blocks H_s=sGT^T, followed by the
actual right path maps. Constants may depend on the fixed box,
displacement, probe and flow time, but not on N.

## Conclusion

The axial-prefix contribution to L064(1)'s complete first pair is

    F_i^ax=sum_(k,l)c_(i;kl) sum_(e,p) r_k(e) {
      det(t_l(p),W^ax_v,p,(TH)_e,p)
      +det(t_l(p),H_v,p,(TW^ax)_e,p) }.

It satisfies

    |F_i^ax|<=C_i N²=O_i(a^-2).

All axial levels, right axial frequencies, endpoints and heat modes
remain. This excludes stronger powers for this selected summand, but
gives no a²-scaled limit, vanishing, sign or logarithm. The direct
transverse contribution to this first pair remains unbounded at the
required scale. Section 4 also gives an exact skew-operator identity
for the jointly retained first pair, available for testing that direct
contribution; it supplies no additional bound. This is local
REPRODUCTION under the saved SPECIALIZE
response assessment, with no claim of progress beyond the sources
checked there. Other endpoint monomials, other response terms and the
interacting reflected-error threshold c_box/2 remain open.

## Proof

### 1. Split the actual right lift before applying a residual estimate

L068(1), before the right paths are selected, gives exactly

    W_X^ax=sqrt(N) G E_0^T A_0 I_1 Sigma_1 T_ax^T J^T
          =sqrt(N) G^(1/2) R_01 Sigma_1^(1/2) T_ax^T J^T,
    R_01=G^(1/2) E_0^T A_0 I_1 Sigma_1^(1/2).

L065 proves ||R_01||<=C with every right axial frequency retained.
The transfer concerns a quadratic covariance block with its exact
forest rows. No unmodified cubic vertex is transferred to Hodge
coordinates, and no full-vector extension of this scalar bound is used.

The actual axial lift at level s is a transverse gradient of an axial
prefix. Thus D J T_ax=0, level by level: incidence maps in different
coordinates commute, and the pinned transverse identity DT=0 holds
also on end plaquettes. Consequently

    W_1^ax=W_X^ax D^T=0,
    W_b^ax=W_X^ax B_b^T, b=2,3.

This zero holds at the linear right-map level before the residual is
inserted. It is not inferred by differentiating a zero base covariance.
Neither W_1^dir nor the full W_1 is declared zero.

### 2. Bound the complete axial-prefix residual arrays

L064's joint transverse-incidence energy inequality gives

    ||Sigma_1^(1/2) T_ax^T||<=1.

Indeed T_ax^T T_ax is the transverse part of the component-1 Hodge
Laplacian and is at most Sigma_1^(-1). The three transverse directions
and all N axial edge positions are included in this comparison. Each
prefix matrix has Frobenius norm at most N, hence ||J||<=N; the three
direction blocks have the same bound. L062's full pinned spectrum gives
Tr G=O(N³). In its three-dimensional sine-index shells, multiplicity
is O(m²), inverse eigenvalues are at most C N²/m², and all
1<=m<N are summed. Hence finite matrix norm inequalities imply

    ||W_X^ax||_HS
      <=sqrt(N) sqrt(Tr G) ||R_01||
                  ||Sigma_1^(1/2)T_ax^T|| ||J||
      <=C N³.

The two-link right maps have uniformly bounded norms by L062's
incidence counting. Pullback to the initial upper endpoint and taking
the upper pinned difference have bounded norms as well: each vertex
meets at most six edges and each difference has at most two entries.
Therefore all of W_2^ax,W_3^ax,(TW^ax)_2,(TW^ax)_3, sampled on
the complete (e,p) array, have HS norm O(N³). No prefix-source
smoothness, near-top omission or covariance localization is assumed.

### 3. Retain the two determinants and sum the complete exterior expansion

L062 gives O(N³) HS bounds on each path component of H and TH on
the same complete arrays. Since H_1=(TH)_1=W_1^ax=(TW^ax)_1=0,
the two determinants in the conclusion have exactly the surviving sum

    t_l,1(p) [ W_2^ax(v,p)(TH)_3(e,p)
               -W_3^ax(v,p)(TH)_2(e,p)
               +H_2(v,p)(TW^ax)_3(e,p)
               -H_3(v,p)(TW^ax)_2(e,p) ].

There are no surviving monomials with t_l,2 or t_l,3. L064's actual
smooth exterior bounds give |r_k(e)|<=a²p(k) and
|t_l,1(p)|<=a²p(l), uniformly including end rows. Cauchy–Schwarz
on the full (e,p) arrays bounds each of the four products by

    C a^4 p(k)p(l) N³ N³
        =C' N² p(k)p(l), since a=8/N.

Both original endpoint placements and their signs remain. Absolute
bounds suffice; no extra signed cancellation is asserted. Finally
L064's complete heat estimate sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i
proves the claimed O(N²) bound for each original probe.

The improvement over the O(N³) estimate in L064 uses the scalar
residual bound before the right axial-prefix norm. The direct transverse
block does not satisfy that scalar estimate (L066), and is outside
this result. All nine placements must still be restored for subleading
powers and logarithms. L011/L019's full response and forest jets,
other/other cubics, measure, insertion/flow corrections, finite matching,
continuum fields, full reflection positivity, infrared control and
finite positive mass remain unresolved. This is not a candidate solution.

### 4. The direct contribution retains a skew upper pairing

Here is an exact reformulation of the two first-pair placements, rather
than a norm estimate. Let E_v take the initial endpoint of each upper
edge, with pinned values zero. For fixed exterior index k define the
upper vertex operator

    C_(r_k)=E_v^T M_(r_k) T-T^T M_(r_k) E_v.

It is skew-symmetric. For fixed p write H_c(p) for its c-th column as
an upper vertex vector, and W_b(p) for the analogous residual column.
Let epsilon_(abc) be the alternating symbol with epsilon_(123)=1.
The complete inner upper-edge sum in the first pair is exactly

    sum_(a,b,c) epsilon_(abc) t_l,a(p)
                    W_b(p)^T C_(r_k) H_c(p).

Indeed the first determinant gives
sum epsilon_(abc) t_l,a W_b^T E_v^T M_r T H_c.
In the second determinant interchange b and c; alternation supplies
the minus sign and its term becomes
-sum epsilon_(abc) t_l,a W_b^T T^T M_r E_v H_c.
This proves the identity, with no boundary remainder, since both
matrices use the same complete pinned incidence and endpoint map.

The identity applies separately with W=W^ax or W=W^dir, by linearity
in the single residual slot. H is unchanged and its exact sGT^T
path composition remains. Skew-symmetry alone does not set this
bilinear expression to zero: its two arguments have different right
maps, and C_r sits between their left covariance weights. Its immediate
operator norm is at most 2||E_v||||T||||r_k||_infinity<=C a²p(k),
which supplies no missing power by itself. No multiplier is commuted
through G, A_0 or a right covariance, and L064's co-closed K cancellation
is not invoked here. The direct first pair remains an independent
ordered-trace problem, not an obstruction or a signed-growth result.

## Mathlib

Coverage of the full selected first-pair bound: **not checked**.
Supporting finite matrix HS inequalities, spectral calculus, pinned
incidence identities, determinant multilinearity and Cauchy–Schwarz:
**not checked**. No full matching theorem or absence claim is asserted.
The ready literature assessment is reused; general flow renormalizability
and lattice stress matching are not reproved. The explicit applicability
argument above is needed for this exact right lift and finite boundary.
