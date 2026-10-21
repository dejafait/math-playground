# L057 — The mixed curvature contraction is subleading at a² scale

## Hypotheses

Keep L054–L056's actual SU(2) straight-forest Gaussian, both original
Wilson-flow probes i=3,6, tau=1/16 and a=8/N through admitted even
meshes. Take the small-coupling coefficient at fixed mesh first.
Retain the complete upper transverse edge set, including pinned end
edges. Matrices use ordinary dimensionless coordinates. Use their
vertex Green matrix G=(T^T T)^(-1), P=TGT^T, rough symmetric
residual block V=NG bar A G, H_0=TG and H_B^d=T_dSBSJ^T.
The incidence is (Tz)_e=z(v)-z(v') for e=(v,v'); vertex fields,
rows and columns at pinned endpoints are zero. Use precisely
L054(5)'s Omega and L056(13)'s signed sum Q_(i,a).

Let G_i be L054's selected nonradial upper quartic plus upper/upper
cubic-pair group. Let d_*>0 and E_(i,mu,mu), w_mu be exactly L055's
constant, smooth probe-kernel derivatives and compressed diagonal
strain. Constants below may depend on the specified displacement,
probe, box and flow time, but not on sufficiently fine admitted meshes.

## Conclusion

The complete mixed contraction satisfies

\[
 |\mathcal Q_{i,a}|+
 |\Omega(H_B^d,H_0;V)|\le C_i a^{-3/2}.                 \tag{1}
\]

Consequently the complete selected group has the limit

\[
 \boxed{\lim_{a\downarrow0}a^2G_i
   =96d_*\int_{D_\perp}\sum_{\mu=2}^4
                       E_{i,\mu\mu}(x)w_\mu(x)\,dx.}    \tag{2}
\]

No value or sign is assigned to the physical integral here. Comparison
with L047, other cubic pairs, measure, insertion and nonlinear flow
jets, subleading powers and the complete logarithm remain unresolved.
An O(a^-3/2) bound permits slower powers and logarithms. Equation (2)
supplies neither finite matching nor the interacting reflected error
<=c_box/2, continuum fields, full reflection positivity or finite
positive physical mass.

## Proof

### 1. Complete heat columns and pinned endpoint operators

Let E,F map a vertex field to its initial and final endpoint values
on each retained edge. At a pinned endpoint the corresponding row
is zero. Thus T=E-F exactly, and ||E||,||F||<=sqrt(6): each interior
vertex occurs in at most six retained edges. These bounds include
every end edge, independently of N.

L028's covariance-square-root columns v_(k,a), L029's upper-face
column bounds, and L054's complete probe heat expansion give exactly

\[
 (H_B^d)_{ew}=\sum_{k,l}c_{i,a;kl}\,r_{k,a}(e)h_{l,a}(w),\qquad
 c_{i,a;kl}=e^{-\tau(\lambda_{k,a}+\lambda_{l,a})}
                         (B_{i,a}^{\rm rel})_{kl},       \tag{3}
\]

where r_(k,a)=T_d v_(k,a), h_(l,a)=J v_(l,a), and B^rel is
L008's uniformly bounded relative probe form, rather than the forest
matrix B. This is the same lifted covariance/probe product used in
L054(13),(18), with a d row on the first leg and a potential row on
the second leg. No residual or probe is commuted past a heat factor.
The mode columns obey, for a fixed polynomial p,

\[
 ||r_{k,a}||_\infty\le a^2p(k),\qquad
 ||h_{l,a}||_\infty\le p(l),\qquad
 ||Th_{l,a}||_\infty\le a p(l),\qquad
 \sum_{k,l}|c_{i,a;kl}|p(k)p(l)\le C_i.               \tag{4}
\]

The potential h is the upper omitted axial-link column, a times the
sum of its N smooth axial entries. Its transverse C^1 norm is bounded
by a polynomial since Na=8. It vanishes on the transverse faces, so
the last edge-difference bound holds also at an end edge. The d column
has size a²p(k) by L029(13): its transverse component at axial level
N-1 vanishes to first order towards the top face and its axial
neighbor difference has size a p(k) before the exterior factor a.
These are actual pinned columns, not low-mode replacements. The last
inequality of (4) follows from the uniform relative-form norm and the
mesh-independent quadratic lower bound on every mode energy; a
polynomial times the double Gaussian is summable. Thus (3) retains
all modes uniformly, including its tail.

L054(10)–(12) also give the full rough-kernel estimates

\[
 ||V||_{HS}=O(N^3),\quad ||TV||_{HS}=O(N^{5/2}),\quad
 ||TG||_{HS}=O(N^{3/2}),\quad ||P||_{HS}=O(N^{3/2}).   \tag{5}
\]

For the local term below we additionally use |V_(xy)|<=CN everywhere,
including zero pinned rows. Indeed L055's global energy-form bound
gives |(G bar A G)_(xy)|<=C, hence this assertion for V. Equivalently
it follows from -cNG<=V<=cNG and the uniform Green diagonal bound
by writing V=(NG)^(1/2) R (NG)^(1/2), ||R||<=c, and applying
Cauchy–Schwarz to two evaluation columns. No heat factor or derivative
smoothness is asserted for V.

### 2. An exact cancellation for one potential multiplier

Fix one product r(e)h(w) in (3). Write M_r for edge multiplication
by r, M_h for vertex multiplication by h, and M_(Eh) for edge
multiplication by the initial endpoint value. Define

\[
 R_h:=M_{Eh}T-TM_h=-\operatorname{diag}(Th)F.           \tag{6}
\]

For any vertex field z its row is
h(v)(z(v)-z(v'))-[h(v)z(v)-h(v')z(v')]
=-(h(v)-h(v'))z(v'), proving (6), also at pinned endpoints.
Taking transposes gives the equally necessary identity
T^T M_(Eh)=M_h T^T+R_h^T. In particular
||R_h||<=sqrt(6)||Th||_infinity. Keeping the adjoint identity matters:
M_h does not commute with G or G^(-1).

With A_edge=TVT^T, L056(13)'s contribution of this product is

\[
 Q(r,h)=\operatorname{Tr}\left{
 E^T M_r\,[P M_{Eh}TV-A_{\rm edge}M_{Eh}TG]\right\}. \tag{7}
\]

The trace is on the interior vertex space. Its expansion is precisely
sum_(e=(v,v'),h'=(w,w')) r(e)h(w)
[P_(eh')(TV)_(h'v)-(TVT^T)_(eh')(TG)_(h'v)],
the negative of the bracket in L056(13). A pinned initial vertex has
a zero E row and zero entries in that original bracket. Symmetry of
P,V identifies (VT^T)_(vh')=(TV)_(h'v), so all signs agree.

Apply (6) to the first matrix in (7), and its transpose to the second.
The exact identities GT^TT=I and T^TTG=I yield

\[
 \begin{split}
 P M_{Eh}TV&=TM_hV+P R_hV,\\
 TVT^T M_{Eh}TG&=TVM_h+TVR_h^TTG.
 \end{split}                                         \tag{8}
\]

Thus the constant-multiplier terms cancel, leaving

\[
 Q(r,h)=\operatorname{Tr}\{E^TM_r[
          TM_hV-TVM_h+P R_hV-TVR_h^TTG]\}.             \tag{9}
\]

This is a finite pinned identity. It uses neither a translation-
invariant kernel nor commutation of a variable multiplier with the
rough residual form. It combines the two retained signed sums before
estimating them.

### 3. Bound the three commutator terms with the full spectrum

On the selected (e,v) entry, the first difference in (9) equals

\[
 (TM_hV-TVM_h)_{ev}=(Th)_e V_{v'v}.                   \tag{10}
\]

There are O(N³) edges, so the global pointwise V bound proves that its
trace is at most
C||r||_infinity||Th||_infinity N^4. If either endpoint is pinned,
the selected term is zero; no nonzero end term has been discarded.

For compatible rectangular matrices, |Tr(XY)|<=||X||_HS||Y||_HS
is the finite matrix Cauchy–Schwarz inequality. Apply it to the next
two traces in (9). Bounded endpoint operator norms and (5) give

\[
 \begin{split}
 |\operatorname{Tr}(E^TM_r P R_h V)|
 &\le ||E^TM_rP||_{HS}||R_hV||_{HS}\\
 &\le C||r||_\infty||Th||_\infty N^{9/2},\\
 |\operatorname{Tr}(E^TM_r TVR_h^TTG)|
 &\le ||E^TM_rTV||_{HS}||R_h^TTG||_{HS}\\
 &\le C||r||_\infty||Th||_\infty N^4.
 \end{split}                                         \tag{11}
\]

The first line uses ||P||_HS ||V||_HS; the second uses
||TV||_HS ||TG||_HS. All internal frequencies of V and G enter
these norms. Equations (9)–(11) establish

\[
 |Q(r,h)|\le C||r||_\infty||Th||_\infty
                         (N^{9/2}+N^4).              \tag{12}
\]

Substitute (3)–(4) into this bilinear estimate and sum the complete
heat weights. Since aN=8,

\[
 |\mathcal Q_{i,a}|\le C_i a^3(N^{9/2}+N^4)
                  =O_i(a^{-3/2}).                   \tag{13}
\]

L056(13) bounds Omega-Q by O(N^(3/2)), including its other two
endpoint-difference terms. Therefore (13) proves (1).

### 4. Assembly and scope

Equation (1) implies a² Omega=O(a^(1/2))->0. L056(2) retains all
other selected curvature-derivative corrections with an O(a^(1/2))
scaled remainder. L055's exact scaled defect limit then proves (2),
with its original color factor and sign. No convergence rate for the
defect term is added. In particular (2) is a statement about the
complete selected quartic plus top/top cubic group, not the full
forest-independent Ward response.

The verification is analytic: (6) is checked row by row, the two
adjoint forms of (6) give (8) without commuting multipliers, and the
trace expansion (7) recovers both signed sums in L056. The local
entry (10), all rectangular trace bounds and the all-mode majorant
(4) apply uniformly to arbitrary admitted meshes. No numerical
preview, truncation, mathematical script or new external theorem is
used. Matrix Cauchy–Schwarz and elementary product commutators are
standard finite-dimensional methods; their regulator-specific use
and the boundary hypotheses are justified above.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. This is local
REPRODUCTION of standard methods, with no claim of progress beyond
the inspected literature's general methods or of mathematical
originality. Reproving bulk flow finiteness or stress protection would
not settle these pinned rough-kernel traces; their source scope is
unchanged. All terms removed only at a² scale must be restored before
determining the full logarithm. The physical integral, its comparison
with the previously enclosed selected action classes and the other
response contributions are left unresolved.

## Mathlib

Coverage of this full specialized contraction bound: **not checked**.
Supporting finite matrix Cauchy–Schwarz, incidence/product identities,
adjoints and trace estimates: **not checked**. No matching Mathlib
theorem or machine verification is asserted. Unknown coverage is not
evidence of absence.
