# L029 — Upper-face axial loop: common-path growth and a nonclosing bound

## Hypotheses

Use L025's SU(2) quartic action, exact three-color forest Gaussian,
dimensionless coordinates x=theta/g, and original two probe/residual
insertions. Use L026's lower-rooted direction-1 forest, admitted even
N, a=8/N, and L028's operators at tau=1/16. The small-coupling
coefficient is taken at fixed mesh first.

Select all (1,mu) plaquettes at axial level N-1, mu=2,3,4. Plaquettes
contained in another boundary face have only fixed links and contribute
zero. On the others let v and v'=v+hat(mu) be the transverse endpoints.
Endpoints on a transverse boundary are allowed, with their axial
coordinates set to zero. In traversal order the four entries are
(A,0,-B,-T): A and B are the upper omitted axial links at v and v',
T is the positive transverse link at axial level N-1. Define

\[
 H=(A+B)/2,\qquad L=A-B,\qquad d=A-B-T.
 \tag{1}
\]

The symbol L in (1) is a local vector, not a Laplacian. For one color
write h=Var(H), l=Var(L), e=Var(d), b=Cov(H,L), c=Cov(H,d),
f=Cov(L,d). Colors are independent identical copies. Let W_i denote
L025's exterior matrix expressed in the three coordinates (H,L,d),
for one color. It need not be symmetric.

## Conclusion

The full ordered upper-face nonradial quartic and its quadratic Wick
coefficient are

\[
 q=\frac18|[H,L]|^2-\frac1{24}|[L,d]|^2
       -\frac16\langle[H,d],[H,L]\rangle,
 \tag{2}
\]
\[
\begin{split}
 Q_2={}&(l/4-f/3)|H|^2+(h/4-e/12)|L|^2-l|d|^2/12\\
 &+(-b/2+c/3)H\mathbin\cdot L+(b/3)H\mathbin\cdot d
       +(f/6-h/3)L\mathbin\cdot d.
\end{split}\tag{3}
\]

Here Q2=6 K:C applied to the two remaining legs, as in L025. In the
actual forest covariance,

\[
 f=l/N,\quad c=b/N,\quad 0\le l\le N,\quad 0\le h\le6N,
 \quad 0\le e\le1,\quad |b|\le\sqrt{hl}.
 \tag{4}
\]

If v and v' are both interior, l>=N/6. Consequently the coefficient
on the external common-path slice L=d=0 is

\[
 k_H=l\left(\frac14-\frac1{3N}\right),\qquad
 \frac N{36}\le k_H\le\frac N4\quad(N\ge4).
 \tag{5}
\]

Unlike the interior coefficient in L027, this common-path coefficient
is unbounded. The smooth exterior factors also have different rates:

\[
 |W_{HH}|\le C_i a^2,\quad
 |W_{HL}|+|W_{LH}|\le C_i a^3,\quad
 |W_{Hd}|+|W_{dH}|+|W_{LL}|\le C_i a^4,
 \tag{6}
\]
\[
 |W_{Ld}|+|W_{dL}|\le C_i a^5,\qquad |W_{dd}|\le C_i a^6.
 \tag{7}
\]

Let M be the symmetric three-by-three matrix of (3) for one color
(cross coefficients are divided by two). The complete selected
one-internal-action-pair contribution per plaquette is

\[
 G^{\rm top}_{i,p}=-24\operatorname{Tr}(M W_i).
 \tag{8}
\]

Equations (4), (6), (7) give only
sum_p |G_top(i,p)| <= C_i a^(-2). The HH term accounts for the
largest available bound; the HL, LL, Hd, Ld, dd terms are bounded in
absolute sum respectively by O(a^(-1)), O(1), O(1), O(a), O(a^2).
These are upper bounds, not asserted growth rates.

This is a failed extension of L028's termwise O(1) mechanism, not a
proof that the actual signed class is unbounded. Neither a nonzero
power coefficient nor a logarithmic coefficient is obtained for either
probe. The no-internal-pair class, other jets, L019 cancellations,
finite matching and the reflected-error threshold c_box/2 remain open.
No continuum construction or mass gap follows.

## Proof

### The three surviving ordered edges

Let z have L026's dimensionless Hodge covariance. At an interior
transverse vertex the upper potential is pinned to zero, so the
omitted axial coordinate is the full sum

\[
 A(v)=\sum_{r=0}^{N-1}z_1(r,v).
 \tag{9}
\]

Extend this by zero to transverse boundary vertices; relative
component-1 links there are fixed. The actual retraction gives

\[
 T=z_\mu(N-1,v)-\sum_{r=0}^{N-2}
                 (z_1(r,v')-z_1(r,v)),
 \quad d=z_1(N-1,v)-z_1(N-1,v')-z_\mu(N-1,v).
 \tag{10}
\]

The upper transverse link is fixed. These identities include edges
meeting a transverse face; both zero endpoints yield a fixed
plaquette. They prove the signed ordered entries and show that d is
the actual circulation. No two-edge reduction is used.

For a direct check of (2), the first two nonzero factors have exponents
H+L/2 and -H+L/2. Their BCH coefficients through cubic order are
L, [H,L]/2, [H,[H,L]]/6. Appending -L+d by L025's recurrence gives
w1=d and w2=([H,L]+[L,d])/2. In the scalar product with d the cubic
coefficient contributes

\[
 \langle d,w_3\rangle
 =-\frac16\langle[H,d],[H,L]\rangle
   -\frac14\langle[L,d],[H,L]\rangle
   -\frac16|[L,d]|^2.
\]

The terms containing a bracket with outer d have zero scalar product
with d. The middle term cancels the cross term of |w2|^2/2; this
proves (2) using invariance of the SU(2) inner product.

In particular q at d=0 is |[H,L]|^2/8. This is a restriction of the
polynomial, not yet its Wick coefficient; internal d pairings must
still be retained. Apply (1/2) sum C_ab partial_a partial_b to (2).
The identity |[u,v]|^2=|u|^2|v|^2-(u dot v)^2 and three independent
colors give quadratic parts

\[
 |[H,L]|^2\longmapsto2(l|H|^2+h|L|^2-2bH\cdot L),
\]
\[
 |[L,d]|^2\longmapsto2(e|L|^2+l|d|^2-2fL\cdot d),
\]
\[
 \langle[H,d],[H,L]\rangle
 \longmapsto2(hL\cdot d+f|H|^2-cH\cdot L-bH\cdot d).
\]

Combining them proves (3), including the internal d pairings.
L025's one-pair formula is -8 times the trace of the full-color
quadratic Wick matrix against its exterior matrix. Both have three
identical color blocks, yielding (8). The coordinate change (1) is
invertible on the three active links; its congruence transformations
preserve this contraction. It also remains valid on the degenerate
boundary subspaces.

### Exact zero-axial-mode covariance

In L026's tensor-product spectrum, summing all N edge positions in
direction 1 kills every nonconstant axial cosine mode; the constant
mode has sum sqrt(N). Let G3 be the inverse dimensionless three-
dimensional Dirichlet vertex Laplacian on the transverse cube, extended
by zero to its boundary. Equation (9) gives exactly

\[
 \operatorname{Cov}(A(v),A(w))=N G_3(v,w),\qquad
 \operatorname{Cov}(A(v),z_1(r,w))=G_3(v,w)
 \tag{11}
\]

at every axial level r. Different link components are independent.
Thus (10), (11) imply Cov(H,d)=Cov(H,L)/N and
Cov(L,d)=Var(L)/N, proving the first two assertions in (4).

For clarity, all bounds on G3 can be read directly from that same
spectrum. Its eigenvalues are 4 sum_(j=2)^4 sin^2(k_j pi/(2N)),
with 1<=k_j<=N-1. They are at most 12 and at least 4|k|^2/N^2.
Squared normalized vertex modes are at most 8/N^3. Grouping indices
by max k_j=m, with at most 3m^2 indices in each shell, gives

\[
 G_3(v,v)\le\frac2N\sum_{k_2,k_3,k_4=1}^{N-1}|k|^{-2}
 \le\frac6N(N-1)\le6.
 \tag{12}
\]

Therefore Var(A),Var(B)<=6N and h=Var((A+B)/2)<=6N by
Cauchy–Schwarz. The transverse edge incidence T3 satisfies
T3* T3<=Delta3. Hence T3 G3 T3* has norm at most one, giving
l=N Var_G3(phi(v)-phi(v'))<=N even for boundary-adjacent edges.
If both endpoints are interior, their difference row has squared norm
2 and G3>=I/12; hence l>=N/6. Also |b|<=sqrt(hl).

Finally d is a circulation. L026's lifted curvature covariance is
D1 Delta^(-1) D1*, of norm at most one because D1* D1<=Delta.
Its diagonal bounds e by one. These arguments use the full relative
spectrum, including the axial zero mode, without assigning internal
heat damping. Equation (5) follows from (3), f=l/N and N>=4.

### Smooth exterior bounds with the actual pinning

Use the mode expansion of L028(11)–(14), including its full relative
inverse estimate (8). Before retraction the smooth mode fields
lambda_k^(-1/2) f_k have C1 norm bounded by a fixed polynomial P(k);
the residual fields lambda_k^(-1/2) Delta^(-1) N_a f_k have C1 norm
at most a^2 P(k). Both are finite relative sine/cosine extensions,
so their tangential components vanish on the appropriate faces.

For any such smooth field b, its stored mode link is a R_F b.
Equations (9), (10) applied to b imply the following bounds for its
H,L,d coordinates:

\[
 |H|\le8\|b\|_{C^1},\quad
 |L|\le8a\|b\|_{C^1},\quad
 |d|\le2a^2\|b\|_{C^1}.
 \tag{13}
\]

The second bound sums N neighbor differences, each bounded by
a||b||_C1, and includes the exterior factor a. For the last bound,
the transverse component is zero at axial level N and its value at
level N-1 is at most a||b||_C1; the axial neighbor difference has
the same bound. The sine extension justifies the identical estimates
when a transverse endpoint is on a boundary. The first bound uses
Na=8; it cannot be replaced by a neighbor-difference estimate.

Thus in L028's notation the exterior columns v_k have sizes
(1,a,a^2)P(k) in (H,L,d), and z_k have sizes
(a^2,a^3,a^4)P(k). In the exact expansion
W_i=sum_(k,l) exp(-tau(lambda_k+lambda_l)) (B_i)_(kl) v_k z_l^T,
the uniform norm bound for B_i and Gaussian summability of the
polynomial factors give (6), (7), including all modes. No residual
or probe operator has been commuted past a heat factor.

The loss in the H column is real: take a component-1 relative mode
with axial cosine index zero and three fixed positive transverse
sine indices. In any transverse compact region where that mode is
nonzero, a sum over its N axial entries is 8 times its transverse
mode value (times its bounded positive inverse square-root
eigenvalue). Neighbor averaging has a nonzero limit. Consequently
the H column is not uniformly O(a) even on smooth fixed modes.
This statement concerns a column, not the signed W_HH contraction.

There are at most 3N^3 upper-face plaquettes. The coefficients in
(3) satisfy |k_H|+|k_L|+|k_d|+|k_HL|+|k_Hd|+|k_Ld|<=C N
by (4). Multiplying each by (6), (7), and summing 3N^3 sites gives
the six absolute-sum orders stated after (8). In particular the
complete class is O(a^(-2)), short of the sought O(1) threshold.
Neither an upper bound nor (5) supplies a lower bound on a signed
probe contraction, so divergence is not inferred.

### Verification and scope

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_upper_face_action.py`.
The exact rational certificate
`scripts/combined-ward-response/upper-face-action-certificate.json`
contains the complete nine-variable BCH quartic, the claimed quartic,
all six independent covariance coefficients in their Hessian
contraction, and zero polynomial differences. This verifies the
algebra of (2), (3); the spectrum and bounds are proved above, not
numerically certified. No actual probe asymptotics were sampled.

This specializes the already screened ordered-action calculation.
General flow renormalization and lattice stress matching are not
reproved or extended to the physical boundary by appeal to their
names. No novelty beyond the inspected-source comparison is asserted.

### Additional signed-response diagnostic (2026-10-05)

This is a finite-mesh exploration of (8), not an asymptotic theorem.
Run `OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_upper_face_signed_response.py --samples 64`.
The full certificate is
`scripts/combined-ward-response/upper-face-signed-response-certificate.json`.
The N24 and N32 covariance archives in the same directory retain every
h,l,b,e,c,f entry, including boundary-adjacent plaquettes.

Use L018's dimensionless ordinary coordinates: Sigma is the full relative
inverse, E=exp(-tau Delta/a^2), F is the straight-forest retraction, Q_i
is the unflowed probe matrix, and A is the symmetric residual matrix.
Let J map forest fields to all selected (H,L,d) triples. Each channel
has a symmetric local matrix M_s from (3), with cross coefficients
halved. Set T_s=J^T M_s J on forest-link coordinates. For an ordinary
orthonormal mode e_k put

\[
 x_k=E^{1/2}e_k,\quad y_{i,k}=F\Sigma E Q_i x_k,
 \quad z_k=F\Sigma A\Sigma x_k.\tag{14}
\]

The deterministic contribution is -24 y_(i,k)^T T_s z_k. Summing all
modes gives -24 Tr(T_s W_i), since sum_k x_k x_k^T=E and
W_i=F Sigma E Q_i E Sigma A Sigma F^T. This retains the noncommuting
probe and residual in their actual order. For independent standard
real Gaussian xi, replacing e_k by xi gives an unbiased estimator
of the same complete trace, since E[x x^T]=E. Its six pieces are

\[
-24\sum_p\big(k_H y_Hz_H,\ k_L y_Lz_L,\ k_d y_dz_d,
 \tfrac{k_{HL}}2(y_Hz_L+y_Lz_H),
 \tfrac{k_{Hd}}2(y_Hz_d+y_dz_H),
 \tfrac{k_{Ld}}2(y_Lz_d+y_dz_L)\big).\tag{15}
\]

Here every coefficient is from (3), including f and c from internal d
pairings. The factor -24 includes three colors; the noise represents
one color's trace. There is no heat factor on the internal action pair.
This applies the established finite Gaussian contraction, without
reproving flow renormalizability or stress matching.

All covariance modes are retained. For adjacent transverse endpoints,
(11) gives h=N(G_vv+G_ww+2G_vw)/4,
l=N(G_vv+G_ww-2G_vw), b=N(G_vv-G_ww)/2, with boundary rows zero.
The variance e is the sum of two independent component covariances:
the component-1 transverse neighbor difference at axial edge N-1,
and the component-mu edge at axial vertex N-1. Each uses the full
four-dimensional sine/cosine basis divided by its dimensionless
eigenvalue. The actual randomized trace likewise uses full inverse
and heat transforms, without truncation.

For a separate deterministic test retain the 36 modes with physical
eigenvalue <=1.1 at each mesh. A valid, but crude, omitted-trace bound is

\[
 |G_{i,s}-G_{i,s}^{P}|\le
 24 q_i\sigma^3 r(1+4N)^2\,33m_s
       \sum_{k\notin P}e^{-\tau\lambda_k/a^2}.\tag{16}
\]

Here sigma=1/min_k lambda_k for the dimensionless spectrum;
q3=16 max_p |triplet_weight(p)|;
q6=16 max_x row_sum_abs(S6(x)), where S6 is L008's symmetric
six-component clover shear multiplication matrix;
U=max_x |u_a(x)|; r=64U/a+q3+q6; and m_s bounds the largest
local channel-matrix norm. For diagonal channels m_s is the maximum
absolute coefficient, and for a cross channel it is half the maximum
absolute cross coefficient. The shear row sum in the script uses the
sum of absolute values of every contributing s_mu_nu/2, so any
cancellation improves its bound.

For completeness, the dimensionless curl and vertex gradient have norm
at most 4: their squared norms are bounded by Hodge/vertex eigenvalues,
at most 16. Clover and endpoint averages are contractions. Contraction
of a two-form with u has norm <=|u|, so ||K_a||<=4U/a and
||A||<=16||K_a||+q3+q6<=r. The cumulative path map has norm <=N by
the Frobenius norm of its triangular incidence matrix, hence
||F||<=1+4N. Each omitted axial link appears in at most six selected
plaquettes. Using H^2<=(A^2+B^2)/2, L^2<=2(A^2+B^2), and
d^2<=3(A^2+B^2+T^2), summing plaquettes gives ||J||^2<=33;
thus ||T_s||<=33m_s. Cyclically moving the two half-heat factors in
the omitted trace leaves (1-P)E multiplying a matrix of norm at most
q_i sigma^3 r ||F||^2 ||T_s||; the remaining E has norm at most one.
In its orthonormal mode basis every diagonal element of that matrix
is bounded by its norm. Summing the omitted heat eigenvalues proves
(16), without a positivity assumption on the response.

The values of (16) below are binary64 evaluations without an interval
rounding certificate. They already exceed the required thresholds by
many orders of magnitude. The deterministic totals for probes (3,6)
are approximately (-674.62,-232.67) at N=24 and (-1608.45,-984.53)
at N=32. The summed channel-tail bounds are (4.46e21,7.00e21) and
(1.73e23,3.04e23). A deterministic sign test requires each tail smaller
than the corresponding absolute total and fails. Only 0.0008023 and
0.0009998 of the full heat trace is retained. This stops the present
low-mode/global-norm certification shortcut, not improved deterministic
algorithms or signed cancellation.

The independent full-mode diagnostics use 64 Gaussian trace samples
at each admitted mesh. The following rounded numbers are means plus
or minus empirical standard errors after summing all planes. These
errors have no rigorous confidence guarantee.

| N | Probe | HH | LL | dd | HL | Hd | Ld |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | 3 | -77316.6 +/- 3913.6 | -4849.9 +/- 349.0 | 3.775 +/- 0.599 | 327.05 +/- 16.93 | -7.147 +/- 0.491 | -51.64 +/- 2.39 |
| 24 | 6 | -185851.5 +/- 3663.2 | -29663.2 +/- 304.1 | 37.635 +/- 0.785 | 931.68 +/- 18.22 | -8.151 +/- 0.498 | 100.51 +/- 4.66 |
| 32 | 3 | -301185.6 +/- 11974.8 | -17008.2 +/- 649.1 | 6.868 +/- 0.598 | 577.63 +/- 23.18 | -8.307 +/- 0.607 | -19.51 +/- 2.38 |
| 32 | 6 | -917699.1 +/- 17076.2 | -87168.4 +/- 910.2 | 44.550 +/- 0.931 | 1779.13 +/- 32.23 | -10.627 +/- 0.635 | 80.44 +/- 5.01 |

The total estimates for (3,6) are (-81894.5,-214453.1), with empirical
standard errors (4107.7,3877.3), at N=24; and (-317637.2,-1002974.0),
with errors (12385.8,17740.2), at N=32. Total errors use complete
per-sample sums, retaining channel correlations. Multiplication by a^2
gives approximately (-9099.38,-23828.12) and (-19852.32,-62685.87).
These diagnostics neither establish a limit nor determine an exponent.
Sampled HH dominance and lack of cancellation with the other five
sampled channels motivate a signed zero-axial-mode calculation; they
are not certified signs, growth, or absence of cancellation.

An independent N=4 dense incidence inverse checks all covariance
entries, including boundary-degenerate triples, with maximum error
1.34e-15 against the required 1e-11 threshold. It uses the rational
one-site displacement for operator checking, not the original supported
displacement on an admitted research mesh. Dense products and split
traces check order, sign and color factor. Matrix-free inverse/half-heat
and both complete columns are compared with the incidence calculation.
Each admitted mesh checks every local covariance matrix and L029's
bounds. All columns check the six-piece split. Complete stored samples
and modes reproduce the summaries; every stored covariance entry is
checked for finiteness. All 14 checks passed; complete checks and the
empty failures field were inspected. These are consistency checks
with floating-point tolerances, not interval enclosures of the
large-mesh signed response.

No full Gamma, faster-growth exclusion, actual logarithm, finite
matching or improvement of the reflected-error threshold c_box/2 is
established. Other pairing/plaquette classes and L019's compensation
by other jets remain unevaluated. This is local REPRODUCTION/EXPLORATION,
without progress beyond the assessed literature or an originality claim.

## Mathlib

Coverage of this exact forest, upper-face vertex and signed-response
statement: not checked. No matching formal theorem is claimed.
The finite Gaussian Wick contraction, relative spectral expansion
and elementary difference estimates are explicit above.
