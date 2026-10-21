# L185 — The smooth-tilt placement of the probe quartic is subcubic

## Hypotheses

Use L184's exact fixed-mesh hypotheses and notation: SU(2), relative
box (-4,4)^4, admitted even N, a=8/N, straight direction-1 lower-rooted
forest, complete L008 displacement and both actual L010 probes i=3,6
at tau=1/16. Bare expansion precedes refinement. Full variable-link
coordinates and ordinary Euclidean adjoints retain all normal end
edges; vertex potentials are zero on every physical face.

In particular S is the co-closed covariance, P its projection,
A=PAP is the complete symmetric quadratic residual with both insertion
subtractions, B=B_i=PBP is the actual final-time quadratic probe,
M=2SAS, V=q Phi, H=1-D Phi/2, and Gamma is L184(3)'s row wedge.
All prefixes are the original pinned maps. Select precisely the
second placement of L184(5):

\[
 Q_{2,i,N}=12\sum_{e,g,a,c,u,v}(MB)_{ue}(\Gamma_e)_{ca}
                  P_{ag}(\Gamma_g)_{uv}S_{vc}.             \tag{1}
\]

The index a in (1) is a link label; a=8/N elsewhere denotes the mesh.
Constants below may depend on the fixed data but not N. It suffices
to take sufficiently fine admitted meshes, a<=1.

## Conclusion

For both actual probes,

\[
 |Q_{2,i,N}|\le C_i N^{3/2},\qquad
 a^3 Q_{2,i,N}\longrightarrow0.                           \tag{2}
\]

This removes one entire signed placement of L183's probe-retraction
quartic at cubic scale. It estimates neither Q_1 nor Q_3 of L184,
and therefore does not bound or evaluate that full quartic. The
sextic partner, co-closed zero-time flow, independent f_(i,2),r_0,
finer scales, finite matching, reflected error <=c_box/2, continuum
axioms and infrared finite positive mass remain open. No actual-probe
sign, full compensation, forest invariance or residual norm bound is
claimed. This is a local application of previously assessed spectral,
consistency and matrix estimates, not a claim of discovery beyond them.

## Proof

### 1. Keep the tilted smooth leg and the full heat expansion

Write Delta_phys for the physical relative one-form Hodge Laplacian,
Sigma_H=a^-2 Delta_phys^-1 for its dimensionless covariance, and
f_k for its L2_a-normalized real product modes with eigenvalue lambda_k.
Their ordinary-coordinate orthonormal vectors are e_k=a^2 f_k.
All component labels and the allowed constant own-direction cosine
modes are included. L028 gives lambda_k>=|k|^2/16 and a positive gap.

By L018's normalization, A=a^2 N_a and
B_i=a^2 exp(-tau Delta_phys) Q_(i,a) exp(-tau Delta_phys).
Let

\[
 d_{i;kl}=e^{-\tau(\lambda_k+\lambda_l)}
                  \langle f_k,Q_{i,a}f_l\rangle_a.
\]

The exact finite spectral expansion is

\[
 B_i=a^2\sum_{k,l}d_{i;kl}e_ke_l^T,
 \quad MB_i=a^2\sum_{k,l}d_{i;kl}m_ke_l^T,
 \quad m_k=M e_k.                                        \tag{3}
\]

L028's uniform boundedness of
Delta_phys^-1/2 Q_(i,a) Delta_phys^-1/2, also used in L156(8), implies
|<f_k,Q_(i,a)f_l>_a|<=C_i sqrt(lambda_k lambda_l).
The full heat sum and the eigenvalue bounds consequently give, for
every fixed polynomial p,

\[
 \sum_{k,l}|d_{i;kl}|p(k)p(l)\le C_{i,p}.                 \tag{4}
\]

No internal mode cutoff or restricted forest flow is used in (3)--(4).

The key smoothness estimate applies only to m_k. Since AP=A and
P commutes with Sigma_H, S A S=Sigma_H A Sigma_H. Thus, as an equality
of sampled full-link vectors,

\[
 m_k=2\lambda_k^{-1}\Delta_{phys}^{-1}N_a f_k.             \tag{5}
\]

Indeed Sigma_H e_k=lambda_k^-1 f_k, the inner A supplies a^2,
and the outer Sigma_H supplies a^-2. L028(5)--(8) prove that N_a f_k
is compactly supported, smooth, and O(a^2) against a fixed polynomial
in k, and that its complete relative inverse has the same C^1 bound.
Together with the gap and uniform product-mode amplitudes this gives

\[
 \|m_k\|_\infty\le C a^2 p(k),\qquad
 \|e_l\|_\infty\le C a^2.                                \tag{6}
\]

L026's raw Phi sums at most N component-1 entries, with coefficients
one, at every interior vertex; its boundary values are set to zero.
Both q and D use only two endpoints. Hence, including every upper
normal edge and its possible pinned jump,

\[
 \|Hm_k\|_\infty+\|Vm_k\|_\infty
       \le C N a^2 p(k)\le C' a p(k).                    \tag{7}
\]

This bound allows the jump to be of order a. It does not extend the
prefix smoothly across the upper face, commute it through M, or apply
smooth consistency to any rough slot of (1).

### 2. An exact four-term row contraction

For X,Y in {H,V} set C_XY=XSY^T. For one rank-one contribution
MB=m y^T, substitute
Gamma_e(c,a)=-(H_ec V_ea-H_ea V_ec)/2 into (1).
Summing its a slot against P gives
-(H_ec(VP)_eg-(HP)_eg V_ec)/2.
Summing the other Gamma against m gives
Gamma_g(m,v)=-((Hm)_g V_gv-(Vm)_g H_gv)/2.
Their remaining S contraction therefore equals

\[
 \begin{split}
 \mathcal Q_2(m,y)=3\sum_{e,g}y_e\{&
 (Hm)_g(C_{HV})_{eg}(VP)_{eg}
 -(Hm)_g(C_{VV})_{eg}(HP)_{eg}\\
 &-(Vm)_g(C_{HH})_{eg}(VP)_{eg}
 +(Vm)_g(C_{VH})_{eg}(HP)_{eg}\}.                          \tag{8}
 \end{split}
\]

The factor is 12/4=3. In particular the projection remains on the
original differentiated probe slot; it is not moved through a prefix
or covariance. Equation (3) gives exactly
Q_(2,i,N)=a^2 sum_(k,l) d_(i;kl) mathcal Q_2(m_k,e_l).

### 3. Full-prefix and joint-covariance bounds

The raw squared Hilbert--Schmidt norm of Phi counts its path entries:

\[
 \|\Phi\|_{HS}^2=(N-1)^3\sum_{s=1}^{N-1}s\le C N^5.      \tag{9}
\]

Boundary rows vanish. The incidence D and endpoint sum q have uniformly
bounded operator norms, since each row and column has bounded degree.
There are at most 4N^4 variable links and ||P||<=1. Consequently

\[
 \|VP\|_{HS}+\|HP\|_{HS}\le C N^{5/2}.                 \tag{10}
\]

Put K=Phi S Phi^T. L182(10)--(11) establish
||K||_HS<=C N^4 and ||S||_HS<=C N^2 sqrt(log(eN)).
For H=1-D Phi/2, the positive-matrix inequality

\[
 HSH^T\le2S+\tfrac12 D K D^T
\]

follows by expanding (X-Y)(X-Y)^T<=2XX^T+2YY^T with
X=S^1/2 and Y=D Phi S^1/2/2. Hilbert--Schmidt norm is monotone on
positive matrices, as justified in L182. The two-sided operator ideal
bound therefore gives

\[
 \|C_{HH}\|_{HS}+\|C_{VV}\|_{HS}\le C N^4,               \tag{11}
\]

where C_VV=qKq^T. For the mixed blocks write X=H S^1/2,
Y=V S^1/2. Trace Cauchy--Schwarz shows

\[
 \|XY^T\|_{HS}^2
 =\operatorname{Tr}(X^T X Y^T Y)
 \le\|X^T X\|_{HS}\|Y^T Y\|_{HS}
 =\|XX^T\|_{HS}\|YY^T\|_{HS}.
\]

This remains valid for singular S and rectangular maps, using the
equality of nonzero squared singular-value sums in the last step.
Thus every C_XY in (8) has Hilbert--Schmidt norm at most C N^4.
Positivity is used for the true S and K, never for the signed M.

### 4. The complete placement count and its scale

For each of the four terms in (8), absolute entrywise Cauchy--Schwarz
gives, with Z=VP or HP and w=Hm_k or Vm_k,

\[
 \left|\sum_{e,g}(e_l)_e w_g(C_{XY})_{eg}Z_{eg}\right|
 \le\|e_l\|_\infty\|w\|_\infty
                       \|C_{XY}\|_{HS}\|Z\|_{HS}.
\]

Using (6)--(7), (10)--(11) and then the full sum (4) yields

\[
 |Q_{2,i,N}|\le C_i a^2 a^2 a,N^4N^{5/2}
                   \sum_{k,l}|d_{i;kl}|p(k)
 \le C_i a^5 N^{13/2}=C_i' N^{3/2}.                     \tag{12}
\]

Multiplication by a^3=8^3/N^3 proves (2), with decay O(N^-3/2).
The cubic threshold is O(N^3); this full-placement estimate is below
it. It makes no claim about a^2 or finer scales. All faces, constant
modes and external heat sums remain, and no flow-time interchange
occurs because this selected quartic contains only final-time B.

### 5. Exact sign/order check and qualifications

Run from the notebook:

    python3 scripts/combined-ward-response/check_probe_quartic_smooth_placement.py

The full certificate is
`scripts/combined-ward-response/probe-quartic-smooth-placement-certificate.json`.
It reuses L184's direct polynomial derivative and all Gaussian fourth
pairings as a reference, independently assembles (8) from matrix row
covariances, and checks the exact rank-one sum in rational arithmetic.
The full and singular supported covariance fixtures give respectively
Q_2=-8514 and Q_2=-2532, exactly matching the polynomial-based placement.
Every selected check record was inspected in full. These fixtures
are synthetic; their values supply no actual-probe sign or growth
evidence. The actual bound (12) is analytic, conditional on the cited
local consistency and full-spectrum inputs, rather than numerical.

## Mathlib

Full matching cutoff estimate and supporting relative-mode, matrix
ideal and covariance inequalities: **not checked**. Unknown coverage
does not imply absence. L184 imports the named Isserlis fourth-moment
theorem for (1); no new pairing theorem is reproved here. Its specific
row specialization (8) and the actual smooth-leg estimate are necessary
because the other two placements keep M on rough slots. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers the target and explains why full renormalized-correlation
results cannot be imported as this bare selected-group limit.
