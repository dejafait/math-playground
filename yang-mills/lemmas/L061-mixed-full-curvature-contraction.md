# L061 — Full-curvature contraction of the complete mixed cubic group

## Hypotheses

Keep L058's actual SU(2) lower-rooted straight forest on the all-face
pinned box, a=8/N through admitted even meshes, bare coupling, and both
original Wilson-flow probes at tau=1/16. Take the small-coupling
coefficient at fixed mesh first. Write S=Sigma_F for the positive
one-color forest covariance and B=B_(i,F), A=A_F for the actual
symmetric quadratic probe and residual matrices, i=3,6. Additive
constants are irrelevant. There are three independent identical colors.
No restricted-Hessian flow replaces the original full-link flow.

Use C=S3_top, Y=S3-C, u, eta, d, Q, T, G, P and Delta_T with exactly
L049/L058/L060's signs. In particular d=eta+Tu/N and
Q_e=u(v) cross u(w) for e=(v,w). All pinned vertex values are zero.
Let X_s be the one-color forest-coordinate map to the full transverse
link vector at axial level s, 1<=s<=N-1. Every retained end edge and
every transverse plaquette is included. Let R_e be the three-row map
to (d_e,u(v),u(w)). For a transverse plaquette p at level s and an
increasing triple I=(j,k,l) of its four ordered signed edges, let J_pI
be its three-row selection map, with fixed-boundary rows zero.

Define the three-by-three cross blocks

\[
\begin{split}
 C_{e,pI}&=R_e S J_{pI}^T,& U_{e,pI}&=R_e SBS J_{pI}^T,\\
 V_{e,pI}&=R_e SAS J_{pI}^T,&
 Z_{e,pI}&=R_e(SBSAS+SASBS)J_{pI}^T.
\end{split}                                                    \tag{1}
\]

These C blocks are distinguished by their indices from the cubic C.
For any three-by-three blocks C,U,V,Z, write C[j:Z] for C with row
j replaced by row j of Z, and C[j:U,k:V] for the two indicated
replacements, j unequal to k. This notation introduces no inverse.

## Conclusion

L058's **complete** mixed cubic response, with both observable
corrections included, is exactly

\[
\boxed{\mathcal M_i=\kappa(f,r,C,Y)
 =-6\sum_{e,p,I}\left[
 \sum_{j=1}^3\det C_{e,pI}[j:Z]
 +\sum_{j\ne k}\det C_{e,pI}[j:U,k:V]\right].}    \tag{2}
\]

There is no additional factor 1/2. Both orders in Z and all six
ordered distinct-row terms remain. This is a regrouping of L048's
mixed region, not an additional action contribution or a replacement
of the probes by conditional means.

The base-law first row uses the exact full-curvature cross covariance

\[
\boxed{\operatorname{Cov}(d,x_T(s))
       =-g_s(\Delta_T)(I-P).}                    \tag{3}
\]

Consequently L060's bulk gradient block -(s/N)P cancels algebraically
in the complete determinant representation. The row operation giving
this cancellation is exact throughout the quadratic tilt, so it
retains both observable derivatives. It does NOT justify deleting
gradient pieces from selected base factors while leaving the other
derivative blocks in eta coordinates.

For the concatenation \(\mathscr L(v_s)=\sum_s
\operatorname{Cov}(d,x_T(s))v_s\), one has on the full pinned edge space

\[
\mathscr L\mathscr L^T
 =\sum_s g_s(\Delta_T)^2(I-P),\qquad
\boxed{\|\Delta_T^{1/4}\mathscr L\|^2\le\tfrac12.} \tag{4}
\]

More explicitly the spectral sum is at most
\(\min\{(N-1)(2N-1)/(6N),1/(2\sqrt\lambda)\}\)
for every positive eigenvalue lambda. This is a weighted bound, not
an N-independent unweighted localization estimate.

No a^2-scale estimate or limit for (2), or for
kappa(f,r,H-M)+E_mix, is established here. L059's conditional
coefficient still cannot be assigned to the complete mixed response.
Other/other cubic pairs, all remaining jets, nonlinear forest
compensation, subleading powers and the logarithm, matching, reflected
error <=c_box/2, continuum axioms and finite positive mass remain open.

## Proof

### 1. Regroup before taking expectations

Reuse L049's actual upper cubic, also used in L054's top/top
regrouping. Edge by edge,

\[
 (Tu)_e\cdot Q_e=(u(v)-u(w))\cdot(u(v)\times u(w))=0.
\]

Therefore C=sum_e d_e dot Q_e/2 as a polynomial in the full forest
coordinates. This holds at pinned endpoints as well, where Q_e=0.
L058 proves that Y contains exactly all transverse plaquette cubics
at levels 1,...,N-1; all non-upper axial cubics vanish identically.
L048(4) gives

\[
 Y=-\tfrac12\sum_{p,I=(j<k<l)}
                y_{p,j}\cdot(y_{p,k}\times y_{p,l}).             \tag{5}
\]

No transverse plaquette, color, rough mode or boundary row is omitted.

### 2. Complete Gaussian contraction and both observable derivatives

Import the standard finite-dimensional Gaussian quadratic-tilt formula
and Isserlis Gaussian pairing theorem, as used with these same actual
matrices in L048 and L052. On a neighborhood of alpha=beta=0 the
normalized tilt by exp(alpha f+beta r) has three identical covariance
blocks

\[
 S(\alpha,\beta)=(S^{-1}-2\alpha B-2\beta A)^{-1}.                \tag{6}
\]

Positive definiteness at zero gives a fixed-mesh integrable Gaussian
majorant for all polynomial derivatives. Degenerate selected row
images cause no problem; no local block inverse is taken.

For color-isotropic Gaussian triples a_1,a_2,a_3 and b_1,b_2,b_3,
every contraction internal to one scalar triple product vanishes:
the covariance forces two colors equal in its alternating epsilon
tensor. All surviving Isserlis pairings are the six permutations
joining the two triples. For a permutation pi their color sum is
6 sign(pi). Hence

\[
 E[(a_1\cdot(a_2\times a_3))(b_1\cdot(b_2\times b_3))]
       =6\det(\operatorname{Cov}(a_j,b_k))_{j,k=1}^3.            \tag{7}
\]

This reasoning remains valid under (6), including overlapping or
zero rows. Combining (5), (7) and the factor +1/2 in C gives

\[
 E_{\alpha,\beta}[CY]
   =-\tfrac32\sum_{e,p,I}
             \det(R_e S(\alpha,\beta)J_{pI}^T).                 \tag{8}
\]

The normalized mixed derivative of E_(alpha,beta)[CY] at zero is
kappa(f,r,CY). Explicitly it is
E[frCY]-Ef E[rCY]-Er E[fCY]-E[fr]E[CY]+2Ef Er E[CY].
Evenness of f,r and oddness of C,Y remove the other partitions in
the four-cumulant; this is precisely kappa(f,r,C,Y), as in L058(21).
Thus the derivative computes the whole mixed contribution, including
the fluctuation and E_mix retained in L058(8).

Differentiate (6) without commuting A and B. The cross block in (8)
has derivatives 2U, 2V and 4Z. Multilinearity of the determinant
therefore gives three terms with the mixed derivative on one row,
and six terms with the two first derivatives on distinct rows, each
carrying factor 4. Multiplying by -3/2 yields (2). In particular
Z contains both length-three covariance path orientations. This
also verifies the mixed ordered-pair normalization against L058(2).

### 3. The gradient cancellation holds throughout the tilt

Replace the first row of R_e by the eta_e row to form R_e^eta.
For every covariance matrix S', not only S, the first rows obey

\[
 (R_e S'J_{pI}^T)_1
 =(R_e^\eta S'J_{pI}^T)_1
  +\frac1N\left[(R_e^\eta S'J_{pI}^T)_2
                -(R_e^\eta S'J_{pI}^T)_3\right].               \tag{9}
\]

The other two rows are unchanged. Adding a linear combination of
those rows to the first leaves the determinant unchanged. Therefore
(8) agrees term by term with the eta determinant for every alpha,beta.
Differentiating this identity proves equality of the full nine-term
responses, without declaring the observables independent of eta or
changing the original conditional polynomial M.

The product rule matters here. Expanding the added first row in the
determinant gives determinants with repeated row functions, identically
zero for every alpha,beta. Their mixed derivatives cancel only after
all differentiated row placements are retained. Individual terms with
one row differentiated need not vanish. This proves the stated scope
of the cancellation and identifies why deleting a base gradient block
alone would be unjustified.

At the original covariance, L060 gives x_T(s)=(s/N)Tu+xi_s, with
xi independent of u and Cov(u,u)=NG. Thus

\[
 \operatorname{Cov}(u,x_T(s))=sGT^T,\qquad
 \tfrac1N T\operatorname{Cov}(u,x_T(s))=(s/N)P.                  \tag{10}
\]

Since Cov(eta,u)=0, L060(2) also gives Cov(eta,x_T(s))=K_s.
Adding (10) to K_s proves (3), over every mode and pinned row.
For s=N-1 it also agrees with x_T(N-1)=Tu-d and L054's
Cov(d,u)=TG: the cross covariance is P-K_d, as required.

### 4. Weighted full-spectrum bound

The functions in (3) are self-adjoint and commute with P by L060's
relative cochain identities. Multiplying the concatenation by its
adjoint proves the first identity in (4). L058 gives

\[
 g_s(\lambda)=\frac{\sinh(s\gamma)}{\sinh(N\gamma)},\qquad
 \gamma=2\operatorname{arsinh}(\sqrt\lambda/2)>0,
 \quad 0\le g_s(\lambda)\le s/N.                              \tag{11}
\]

The latter bound gives the sum-of-squares bound in the conclusion.
For the other bound, write the ratio as
exp(-(N-s)gamma)(1-exp(-2s gamma))/(1-exp(-2N gamma)).
The last fraction is at most one. Hence

\[
 \sum_{s=1}^{N-1}g_s(\lambda)^2
 \le\sum_{j=1}^{\infty}e^{-2j\gamma}
 =\frac1{e^{2\gamma}-1}
 \le\frac1{2\sqrt\lambda}.                                   \tag{12}
\]

Indeed e^(2gamma)-1=2e^gamma sinh(gamma), and
sinh(gamma)=sqrt(lambda)sqrt(1+lambda/4)>=sqrt(lambda).
Multiplying (12) by sqrt(lambda) and applying finite spectral
calculus yields (4). No low-frequency cutoff or summability of a
spatial kernel was assumed. Small eigenvalues still allow an
unweighted squared norm of order N; (4) cannot be used as an
unweighted boundary-localization assertion.

### 5. Relevance, verification and remaining threshold

The intermediate test succeeds at the algebraic level: the dangerous
gradient block is removed in the full signed representation, including
both observable derivatives. This does not contradict L060 or its
single-vertex derivative example. The removal uses the actual upper
vertex and the other two covariance rows, not annihilation of an
arbitrary transverse cubic derivative.

L048 already supplies a general exact contraction and L054 already
uses d for top/top pairs. The necessary specialization here is (9)
for top/transverse pairs and its exact spectral cross block (3),
with (4) available for estimates of the differentiated sum. This is
local REPRODUCTION under the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`, not a claim of
mathematical progress beyond the inspected sources. General flow
renormalizability and stress matching are not reproved.

Analytic checks are the sign (+1/2)(-1/2)6=-3/2, the three plus six
row derivative placements and their factor four, both inverse path
orders, the exact upper endpoint identity, and the positive-spectrum
bound (12). No numerical evidence or mathematical script is needed.
The target still requires estimating the actual signed sum (2), or
its difference from L059's conditional part, at order a^-2 and then
below that scale. Neither the determinant identity nor (4) supplies
the needed estimates on U,V,Z and their products by itself.

## Mathlib

Coverage of the full mixed-response regrouping and weighted bound:
**not checked**. Supporting finite Gaussian quadratic tilting,
Isserlis pairing, determinant row operations and finite spectral
calculus: **not checked**. No matching Mathlib theorem is asserted;
unknown coverage is not evidence of absence. The standard named
Gaussian results are imported above with their finite-dimensional
polynomial hypotheses; their lattice specializations use the exact
local inputs specified in the proof.
