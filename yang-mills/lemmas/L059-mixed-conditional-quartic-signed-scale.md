# L059 — Signed scale of the mixed conditional quartic

## Hypotheses

Keep L058's actual SU(2) Gaussian, lower-rooted direction-1 forest,
all-face pinned box, a=8/N through admitted even meshes, both original
Wilson-flow probes f=f_(i,0), i=3,6, and residual r=r0 at tau=1/16.
Take the small-coupling coefficient at fixed mesh before refining the
mesh. Include every upper transverse edge and all three independent
colors. The nonlinear probes are not replaced by restricted-Hessian
flow. Use L051's one-color vertex matrices C=NG, U,V,W, W_+=W+W^T
and its bilinear functional Phi. The incidence T, projection P and
transverse Laplacian Delta_T are those in L050/L058.

Define fixed original-law edge operators and quartics

\[
 K_\chi=\chi_N(\Delta_T)(I-P),\qquad
 D_0=b_N(\Delta_T)(I-P),\qquad E_N=D_0-K_\chi,
\]
\[
 M=\frac14\sum_c(Q^c)^T K_\chi Q^c,
 \qquad Z_0=\frac18\sum_c(Q^c)^T D_0 Q^c.
\tag{1}
\]

M is exactly L058's conditional mixed product, not the actual mixed
cumulant. Z_0 differs from L049's Z by the gradient-sector quartic
\(\sum_c(Q^c)^TPQ^c/(8N)\). Keep L058's T_*=H-M and E_mix as
defined there. Let d_*>0 and the physical integral S_i be exactly
L055's torus constant and strain integral (also C057a's S_i).

## Conclusion

For both actual quadratic probes,

\[
 \boxed{\kappa(f,r,M)
 =12\Phi_{K_\chi}(C,W_+)+12\Phi_{K_\chi}(U,V).}
\tag{2}
\]

The complete signed discrepancy, not just the action comparison, obeys

\[
 |\Phi_{E_N}(C,W_+)|=O(N^{-1}),\qquad
 |\Phi_{E_N}(U,V)|=O(N),\qquad
 |\kappa(f,r,M)-2\kappa(f,r,Z_0)|=O(a^{-1}).
\tag{3}
\]

Also Phi_(K_chi)(C,W_+)=O(1), and hence

\[
 \boxed{\lim_{a\downarrow0}a^2\kappa(f,r,M)
              =-192d_*\mathcal S_i.}
\tag{4}
\]

C057a's complete enclosures give S_3>0 and S_6<0, so (4) is negative
for the triplet and positive for the shear. Those numerical signs inherit
C057a/L047's stated IEEE arithmetic model and full error enclosures.
Equation (4) itself needs no numerical computation or arithmetic model.

The actual complete exactly-one-upper cubic term is still

\[
 a^2\mathcal M_i=-192d_*\mathcal S_i
  +a^2\{\kappa(f,r,T_*)+\mathcal E_{\rm mix}(f,r)\}+o(1).
\tag{5}
\]

No bound or limit for the brace in (5) is established. In particular,
(4) is not the coefficient of the actual mixed group. It identifies a
conditional contribution equal to minus twice L057/C057a's selected
joint-group coefficient; adding it to that joint group alone is not
a calculation of their complete combined coefficient. Neither
conditional centering nor positivity deletes the brace. We make no
signed-smallness claim for 2Z-M: the P/N sector is absent from E_N.
Other/other cubic pairs, all remaining response jets, subleading powers,
the logarithm, finite matching, interacting reflected error <=c_box/2,
continuum axioms, full reflection positivity and finite positive mass
remain open. Separate forest invariance is not assumed.

## Proof

### Fixed-law Gaussian contraction

Import the standard finite-dimensional Gaussian quadratic-tilt formula
and Isserlis Gaussian pairing theorem, in the precise conventions and
with the justification in L051, proof section 1. At each fixed mesh the
normalized tilt exp(sf+tr) has one-color covariance
(S^(-1)-2sB-2tA)^(-1) in a neighborhood of zero. Polynomial derivatives
are justified by a Gaussian majorant. The vertex covariance derivatives
are C_s=2U, C_t=2V, C_st=4W_+, without commuting factors.

L051(8) gives the three-color cross-product expectation. Its proof is
independent of the particular fixed symmetric edge kernel, so for the
quartic M in (1) it gives

\[
 E_{s,t}M=\tfrac32\Phi_{K_\chi}(C(s,t),C(s,t)).
\]

K_chi is held fixed; it is not recalculated under the tilt. Twice
differentiating the normalized expectation gives kappa(f,r,M).
Symmetry and bilinearity of Phi, with the above derivatives, give (2).
The same calculation for Z_0 gives the coefficients 6 instead of 12.
This proves the exact signed relation underlying (3), including all
connected subtractions, internal-pair and no-internal-pair classes.

### Full-spectrum estimate for the discrepancy

L058(5) and orthogonality of P give

\[
 0\preceq E_N\preceq (2/N)(I-P),\qquad E_N T=0,
 \qquad K_\chi T=0,\qquad 0\preceq K_\chi\preceq I.
\tag{6}
\]

All inequalities hold over the whole edge spectrum. They compare
transverse operators; they do not bound the gradient-sector response.

For pinned deterministic vertex fields h,k, set B_h xi as in L053(4),
and let xi have covariance C=NG. L053's exact pinned product identity
is B_h xi=-T(h xi)+2(Th)M_av xi, where M_av is the endpoint-average
map (distinguished here from the quartic M). Since E_N annihilates T,

\[
 \mathcal Q_E(h):=E\|E_N^{1/2}B_h\xi\|^2
 \le\frac8N\|Th\|_\infty^2
                     \operatorname{Tr}(M_{\rm av}CM_{\rm av}^T)
 \le144N^3\|Th\|_\infty^2.
\tag{7}
\]

The last inequality is L053(12)'s trace bound <=18N^4. It includes
all pinned end edges and the entire unflowed covariance spectrum.

Use L053(14)–(15) and L054(13)'s actual exterior heat expansions,
with common absolutely summable coefficients c_(i,a;kl):

\[
 U=\sum_{k,l}c_{i,a;kl}h_kh_l^T,\qquad
 W=\sum_{k,l}c_{i,a;kl}h_kj_l^T,
\]
\[
 \|Th_k\|_\infty\le a p(k),\qquad
 \|Tj_l\|_\infty\le a^3 p(l),\qquad
 \sum_{k,l}|c_{i,a;kl}|p(k)p(l)\le C_i.
\tag{8}
\]

The j columns contain the residual; they have not been commuted
through heat factors. Inserting (8) in (7), using aN=8, gives

\[
 \mathcal Q_E(h_k)\le C N p(k)^2,
 \qquad \mathcal Q_E(j_l)\le C N^{-3}p(l)^2.
\tag{9}
\]

L053(6) and Hilbert–Schmidt Cauchy–Schwarz imply

\[
 |\Phi_{E_N}(C,h_kj_l^T+j_lh_k^T)|
 \le\sqrt{\mathcal Q_E(h_k)\mathcal Q_E(j_l)}.
\]

Summing the full heat weights proves Phi_E(C,W_+)=O(N^-1).
For V use L054(10)'s genuine rough form estimate -cC<=V<=cC:
write V=C^(1/2)R_V C^(1/2), with symmetric ||R_V||<=c. The same
rank-two contraction is a Hilbert–Schmidt pairing through R_V and
therefore, as in L054(16),

\[
 |\Phi_{E_N}(V,h_kh_l^T+h_lh_k^T)|
 \le c\sqrt{\mathcal Q_E(h_k)\mathcal Q_E(h_l)}.
\]

U is symmetric, so its expansion is the sum of half these symmetric
rank-two terms with coefficients in (8). Equations (8)–(9) prove
Phi_E(U,V)=O(N). The exact formula (2), its Z_0 counterpart and
K_chi=D_0-E_N prove (3). This argument is a signed estimate using
the actual covariance and exterior columns, not a transfer of L058's
pointwise quartic inequality.

Replacing E_N by K_chi in (7) changes the first bound to
Q_chi(h)<=72N^4||Th||_infinity^2, by (6). Thus the two estimates
for h_k and j_l become O(N^2)p(k)^2 and O(N^-2)p(l)^2.
The same rank-two Cauchy–Schwarz estimate and (8) prove
Phi_Kchi(C,W_+)=O(1). This keeps both W orientations and every mode.

### Scaled limit and retained complete response

L055(2) supplies the full signed limit
a^2 Phi_D0(U,V) -> -16 d_* S_i. Its hypotheses are precisely the
matrices, pinned edges, box, probes and limit order used here; its
full-spectrum approximation bound (7), energy projection and collar
argument justify that limit. No translation-invariant replacement at
the physical boundary is made. The O(N) discrepancy in (3) becomes
O(a) after multiplication by a^2, and the O(1) one-internal-pair term
becomes O(a^2). Equation (2) therefore gives (4), with factor
12*(-16)=-192. C057a's physical integral and signs use exactly the
same kernel and strain, so its sign conclusion applies to (4).

Finally substitute (4) into L058(8), without deleting either retained
term. This proves (5). Neither T_*'s conditional centering nor
K_chi's positivity bounds the brace against the indefinite residual.
The attempt evaluates the conditional part only; the full mixed
scaled target has not been reached.

### Verification and necessity of the specialization

The mathematical checks are the exact tilt normalization (1/4 versus
L051's 1/8), both inverse-covariance derivative orders, the annihilation
E_N T=0 on the complete relative edge space, and the powers
N^3 a^2=O(N), N^3 a^6=O(N^-3), and a^2N=O(a).
The rough V estimate uses its two-sided form bound, not smoothness.
No numerical or surrogate check is used to infer any limit; no new
mathematical script is necessary for this analytic specialization.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. This is local
REPRODUCTION of the cited finite Gaussian methods and existing lattice
estimates, with no claimed result beyond the inspected literature.
L055 supplies the already proved defect limit; the necessary remaining
specialization is the signed use of L058's changed operator in the
actual covariance. General flow renormalizability and stress matching
are neither reproved nor used to assign a complete response coefficient.

## Mathlib

Coverage of the full mixed conditional-quartic signed-scale statement:
**not checked**. Coverage of supporting Gaussian quadratic tilting,
Isserlis' theorem, pinned cochains, spectral calculus and trace
estimates: **not checked**. No matching Mathlib theorem is asserted.
The named Gaussian results are imported with their finite polynomial
hypotheses above; the load-bearing specialized estimates and limit
are the precise local results cited in the proof.
