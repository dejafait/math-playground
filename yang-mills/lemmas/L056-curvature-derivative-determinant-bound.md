# L056 — Two curvature-derivative sums are subleading at a² scale

## Hypotheses

Keep L054–L055's actual SU(2) straight-forest Gaussian, both original
probes i=3,6, tau=1/16, a=8/N through admitted even meshes, and the
complete upper transverse edge set, including pinned end edges. Take
the small-coupling coefficient at fixed mesh first. All matrices and
inner products below use ordinary dimensionless coordinates. Use
L054's C=NG, U=JSBSJ^T, V=JSASJ^T, incidence T with
(Th)_e=h(v)-h(v'), and its K_B^d,K_A^d,H_B^d,H_0=TG.
Extend vertex rows and columns by zero at pinned endpoints.

Let G_i be L054's selected nonradial upper quartic plus upper/upper
cubic-pair group. Use L055's positive constant d_* and its kernel
derivatives E_(i,mu,mu), and put

\[
 I_i^{\rm strain}=\int_{D_\perp}\sum_{\mu=2}^4
                      E_{i,\mu\mu}(x)w_\mu(x)\,dx.
\]

This strain integral is distinct from L030's functional I_i.
Constants may depend on the fixed displacement, probe, box and tau,
but not on sufficiently fine admitted meshes.

## Conclusion

The two complete ordered-edge-pair sums satisfy

\[
 \left|\sum_{e,h}(K_B^d)_{eh}\delta_{eh}(C,V)\right|
 +\left|\sum_{e,h}(K_A^d)_{eh}\delta_{eh}(C,U)\right|
       \le C_i a^{-3/2}.                              \tag{1}
\]

Thus both vanish after multiplication by a². The remaining selected
group has the rigorous reduction

\[
 a^2G_i=-6a^2\Phi_{D_0}(U,V)
            +6a^2\Omega(H_B^d,H_0;V)+O_i(a^{1/2}),     \tag{2}
\]
\[
 a^2G_i-6a^2\Omega(H_B^d,H_0;V)
                      \longrightarrow96d_* I_i^{\rm strain}. \tag{3}
\]

No limit or sign is assigned to the remaining Omega or the physical
strain integral. The group limit, comparison with L047, other cubic
pairs, measure, insertion and nonlinear flow jets, subleading powers,
the complete logarithm, finite matching and the interacting reflected
error <=c_box/2 remain unresolved. Neither (1) nor (3) is an
ultraviolet-uniform interacting estimate, continuum construction,
reflection-positivity result or finite positive physical mass.

## Proof

### 1. Preserve the determinant's alternating endpoint differences

For e=(v,v'), h=(w,w'), denote a vertex-pair entry by C_00=C_vw,
C_01=C_vw', C_10=C_v'w and C_11=C_v'w', and similarly for M.
Use forward endpoint differences, so

\[
 \nabla_e M=M_{10}-M_{00},\quad
 \nabla_h M=M_{01}-M_{00},\quad
 \nabla_e\nabla_h M=M_{11}-M_{10}-M_{01}+M_{00}.
\]

Expanding the four products gives the exact identity

\[
 \delta_{eh}(C,M)=C_{00}\nabla_e\nabla_h M
       +M_{00}\nabla_e\nabla_h C
       -(\nabla_h C)(\nabla_e M)
       -(\nabla_h M)(\nabla_e C).                    \tag{4}
\]

For example the expansion leaves precisely
C_00 M_11+M_00 C_11-C_01 M_10-M_01 C_10, which is L054's
delta(C,M). The two negative incidence signs cancel in the mixed
difference: its full matrix is TMT^T. Single differences equal
endpoint pullbacks of -TM or -MT^T. Equation (4) is valid also
when any endpoint is pinned; every corresponding zero is retained.

Each vertex is the initial or final endpoint of at most six retained
edges. Consequently any endpoint pullback of a vertex or edge–vertex
matrix to an edge-pair array increases its Hilbert–Schmidt norm by
at most an absolute constant. Cauchy–Schwarz applied separately to
the four products of (4) therefore proves, for symmetric C,M,

\[
 \sum_{e,h}|\delta_{eh}(C,M)|\le C_0\big[
    \|C\|_{HS}\|TMT^T\|_{HS}
   +\|M\|_{HS}\|TCT^T\|_{HS}
   +\|TC\|_{HS}\|TM\|_{HS}\big].                  \tag{5}
\]

The constant absorbs both single-difference products, using symmetry
to identify the norms of each transpose. No cancellation across
different edge pairs is required for this estimate. In particular
(5) controls the full absolute sum rather than a diagonal subset.

### 2. Use full-spectrum derivative norms for C,V

L054(10)–(12) supply the actual rough-block bounds

\[
 \|C\|_{HS}+\|V\|_{HS}=O(N^3),\qquad
 \|TC\|_{HS}+\|TV\|_{HS}=O(N^{5/2}),\qquad
 \|TVT^T\|_{HS}=O(N^{5/2}).                         \tag{6}
\]

For completeness the C derivative bounds follow exactly from
C=NG, T^T T=G^{-1}, Tr G=O(N³) and rank P=(N-1)³:

\[
 \|TC\|_{HS}^2=N^2\operatorname{Tr}G=O(N^5),\quad
 TCT^T=NP,\quad \|TCT^T\|_{HS}=O(N^{5/2}).          \tag{7}
\]

For V, L054 writes V=NG^(1/2) R G^(1/2), ||R||<=c, so the
same bounds hold without any smooth-input assumption on V. All
transverse frequencies and all pinned end edges occur in (6)–(7).
Inserting M=V in (5) gives

\[
 \sum_{e,h}|\delta_{eh}(C,V)|
          =O(N^{11/2}+N^5)=O(N^{11/2}).             \tag{8}
\]

L054(18)'s uniform distinct-row bound ||K_B^d||_max=O(a⁴),
and aN=8, now give

\[
 \left|\sum_{e,h}(K_B^d)_{eh}\delta_{eh}(C,V)\right|
          \le O(a^4N^{11/2})=O(a^{-3/2}).           \tag{9}
\]

### 3. Use the smooth probe kernel only for U

L055, proof section 4, identifies every entry U_vw, including
distinct vertices, with the sampled smooth kernel K_(i,a)(x_v,x_w)
of L045(9). L045's derivative convergence provides a uniform bound
for that kernel and its first derivatives in each argument, including
the mixed derivative, on the closed transverse box. Both arguments
have zero values on every Dirichlet face. The fundamental theorem
of calculus along one or two retained edges therefore yields

\[
 |U_{vw}|\le C_i,\qquad |(TU)_{ew}|\le C_i a,
 \qquad |(TUT^T)_{eh}|\le C_i a^2.                 \tag{10}
\]

The argument applies at end edges because the same kernel extension
has the prescribed zero endpoint values. There are O(N³) vertices
and O(N³) retained edges, so their pair counts give

\[
 \|U\|_{HS}=O(N^3),\quad \|TU\|_{HS}=O(aN^3)=O(N^2),
 \quad\|TUT^T\|_{HS}=O(a^2N^3)=O(N).               \tag{11}
\]

Equations (5)–(7), with M=U, imply

\[
 \sum_{e,h}|\delta_{eh}(C,U)|
       =O(N^4+N^{11/2}+N^{9/2})=O(N^{11/2}).       \tag{12}
\]

L054(19) proves ||K_A^d||_max=O(a⁴) uniformly over arbitrary
upper edge pairs by source separation from the residual support.
Multiplying (12) by that bound proves the second estimate in (1).
The rough V was never replaced by a heat-smoothed covariance.

### 4. Assemble the surviving scale and retain its obstruction

In L054(8)–(9), the two terms of (1) are now O(a^-3/2).
Its K_BA^d term and Phi_D0(C,W_+) are O(1). The four Omega
types other than Omega(H_B^d,H_0;V) have respective bounds
O(N^(1/2)), O(1), O(N^(1/2)), O(N), and the subtracted R cumulant
is O(N), all recorded in L054. Multiplication by a² shows that
their complete sum, including (1), is O(a^(1/2)). This proves (2).
L055's scaled limit with its original normalization then proves (3).
No rate is asserted for that limiting defect term.

To display exactly what this attempt leaves, write
b_(e,w)=(H_B^d)_ew and let e=(v,v'). L054(21) and H_0T^T=P
give

\[
 \Omega(H_B^d,H_0;V)=\mathcal Q_{i,a}+O_i(N^{3/2}),\quad
 \mathcal Q_{i,a}:=-\sum_{e=(v,v'),h=(w,w')}
 b_{(e,w)}\big[(TG)_{hv}(TVT^T)_{eh}
                 -P_{he}(VT^T)_{vh}\big].          \tag{13}
\]

Indeed the first two terms of L054(21) are exactly the displayed
sum: its dl=-P_he and its V_vw'-V_vw=-(VT^T)_vh.
The other two terms have bounds O(N) and O(N^(3/2)) there.
Thus a²(Omega-Q_(i,a))=O(a^(1/2)). Each of the two retained
terms in Q_(i,a) still has only the O(N²) bound of L054(22).
Equation (13) supplies no sign or cancellation between them and
no passage to a continuum limit. A signed limit or a justified
stronger bound for this particular full rough-kernel contraction
is still required. This is an explicitly unresolved part of the
selected group, not an established positivity or matching premise.

The proof uses exact finite endpoint algebra, the standard matrix
Cauchy–Schwarz inequality, and existing full-spectrum and smooth
kernel estimates. It is local standard-method REPRODUCTION within
the unchanged SPECIALIZE response assessment
`drafts/literature/2026-09-26-current-target.md`. Reproving general
flow renormalizability or bulk stress matching would not justify
these regulator-specific sums; those source statements remain
imported only within the scope of that assessment. No mathematical
script, numerical diagnostic or originality claim is involved.
The O(a^-3/2) bound does not exclude slower powers or logarithms;
every discarded term must be restored for the full logarithm.

## Mathlib

Coverage of this complete specialized result: **not checked**.
Supporting finite matrix Cauchy–Schwarz, endpoint differences and
finite-dimensional spectral algebra: **not checked**. No matching
Mathlib theorem is asserted. The load-bearing local estimates and
their boundary hypotheses are proved or explicitly imported above.
