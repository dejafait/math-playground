# L186 — The first probe-quartic placement is subcubic

## Hypotheses

Use L184–L185's exact SU(2) hypotheses: relative box (-4,4)^4,
admitted even N, a=8/N, straight direction-1 lower-rooted forest,
complete L008 displacement, both actual L010 probes i=3,6 at
tau=1/16, and fixed-mesh bare expansion before refinement. All
matrices and adjoints use ordinary full variable-link coordinates.
Normal end edges remain; vertex potentials vanish on every physical
face. No prefix is continued across the upper pinned face.

Keep S, P, A=PAP, B=B_i=PBP, M=2SAS, H=1-D Phi/2 and V=q Phi
exactly as in L184. In particular A includes both residual insertion
subtractions, M is signed, and Phi is the original lower prefix.
For X,Y in {H,V}, write C_XY=XSY^T and K_XY=XMY^T. Select the
entire first placement, with its original signed order:

\[
 Q_{1,i,N}=3\sum_{e,g}B_{eg}\{
 (K_{HH})_{eg}(C_{VV})_{eg}
 -(K_{HV})_{eg}(C_{VH})_{eg}
 -(K_{VH})_{eg}(C_{HV})_{eg}
 +(K_{VV})_{eg}(C_{HH})_{eg}\}.                    \tag{1}
\]

This is L184(6), not a new pairing identity. Constants may depend on
the fixed data and probe, but not sufficiently fine admitted meshes.

## Conclusion

For both actual probes,

\[
 |Q_{1,i,N}|\le C_i N^{5/2},\qquad
 a^3 Q_{1,i,N}\longrightarrow0.                         \tag{2}
\]

The supporting full-prefix estimate is

\[
 \|D\Phi S\Phi^T D^T\|_{HS}\le C N^{7/2}.                \tag{3}
\]

Together with L185, (2) removes Q_1+Q_2 at cubic scale; Q_3 remains
uncontrolled. It proves neither the complete quartic bound/limit nor
the joint cubic probe-jet limit. The retained sextic pairing, co-closed
zero-time flow, independent f_(i,2),r_0 compensation, finer scales,
finite matching, reflected error <=c_box/2, continuum axioms and
infrared finite positive mass remain open. No sign, forest invariance,
rho norm bound or discovery beyond the assessed methods is claimed.

## Proof

### 1. Differentiate the positive prefix comparison with all end rows

Put n=N-1, U_st=min(s,t) for s,t=1,...,n, and let G be the inverse
of the unscaled three-dimensional transverse scalar Dirichlet
Laplacian Delta_T. The letter U avoids confusion with the signed
tilt covariance M. On the interior vertices, L182(10), using
L156(6)–(7), gives the positive comparison

\[
 0\le K:=\Phi S\Phi^T\le K_0:=U\otimes G.                \tag{4}
\]

All these vertex fields have zero boundary values. The actual full
vertex incidence therefore satisfies

\[
 D^TD=L_D\otimes I+I\otimes\Delta_T,                    \tag{5}
\]

where L_D is the n-by-n axial Dirichlet Laplacian: diagonal 2 and
nearest-neighbor entries -1. Edges tangent to a physical face have
both endpoint values zero and are fixed; omitting them changes
neither (5) nor any nonzero derivative row. Normal end edges supply
both Dirichlet endpoint terms in (5).

Let j be the last axial unit vector. Direct multiplication of the
min(s,t) kernel shows

\[
 U^{-1}=L_D-jj^T,\qquad UL_D=I+(Uj)j^T,\qquad
 (Uj)_s=s.                                              \tag{6}
\]

For example, taking successive differences of min(s,t) gives the
identity at interior rows and the last row has diagonal 1 in U^-1.
The extra jj^T in L_D is exactly the upper pinned derivative.
It is retained, rather than replaced by the upper-free inverse.
Writing traces as unrestricted finite sums gives

\[
 \begin{split}
 \operatorname{Tr}(UL_DUL_D)&=n^2+3n,\\
 \operatorname{Tr}(UL_DU)&=\operatorname{Tr}U+\|Uj\|^2
                         =\frac{n(n+1)(n+2)}3,\\
 \operatorname{Tr}(U^2)&=\sum_{s,t}\min(s,t)^2
                         =\frac{n(n+1)(n^2+n+1)}6.
 \end{split}                                            \tag{7}
\]

The first identity expands the square of I+(Uj)j^T; its trace is
n+2n+n^2. The second follows from UL_DU=U+(Uj)(Uj)^T.
For the third, the number of pairs with minimum r is 2(n-r)+1;
sum r^2[2(n-r)+1] using the finite square and cube sums.

Positive order in (4) is preserved by D. For positive matrices X<=Y,
Tr X^2<=Tr Y^2, since Tr((Y-X)(Y+X))>=0. Thus

\[
 \begin{split}
 \|DKD^T\|_{HS}^2
 &\le\|DK_0D^T\|_{HS}^2
   =\operatorname{Tr}(K_0D^TDK_0D^TD)\\
 &=\operatorname{Tr}(UL_DUL_D)\operatorname{Tr}(G^2)
  +2\operatorname{Tr}(UL_DU)\operatorname{Tr}(G)
  +\operatorname{Tr}(U^2)n^3.                            \tag{8}
 \end{split}
\]

The middle term uses Delta_T G=G Delta_T=I; no axial commutation
of U with L_D is assumed. Equation (8) follows by expanding both
factors from (5) in their original order and using trace cyclicity.

L156's full transverse eigenvalues obey
lambda_k>=4|k|^2/N^2 for k in {1,...,N-1}^3. A shell max k_j=r
has at most 3r^2 entries. Consequently, retaining the entire spectrum,

\[
 \operatorname{Tr}G\le\frac{3N^2}4(N-1)\le C N^3,
 \qquad
 \operatorname{Tr}G^2\le\frac{3N^4}{16}
                     \sum_{r=1}^{N-1}r^{-2}\le C N^4.   \tag{9}
\]

The three terms of (8) are O(N^6), O(N^6), and O(N^7), respectively.
This proves (3). The underlying comparison includes the constant
axial edge mode through U and every transverse end row through G.
No physical boundary contribution is dropped.

### 2. Ordinary and signed tilted covariance blocks

L182(11) gives ||S||_HS<=C N^2 sqrt(log(eN)), while (4) gives
||K||_HS<=C N^4. The endpoint map q has uniformly bounded operator
norm. Also, expanding (X-Y)(X-Y)^T<=2XX^T+2YY^T with
X=S^(1/2) and Y=D Phi S^(1/2)/2 yields

\[
 0\le C_{HH}\le2S+\tfrac12DKD^T,\qquad C_{VV}=qKq^T.
\]

Monotonicity and the two-sided Hilbert--Schmidt ideal bound imply

\[
 \|C_{HH}\|_{HS}\le C N^{7/2},\qquad
 \|C_{VV}\|_{HS}\le C N^4.                              \tag{10}
\]

For clarity define c_X=||C_XX||_HS for X=H,V. Trace
Cauchy--Schwarz, valid also for singular S, gives

\[
 \|C_{XY}\|_{HS}\le\sqrt{c_Xc_Y}.                       \tag{11}
\]

Indeed set Z_X=XS^(1/2). Then the squared left side is
Tr(Z_X^T Z_X Z_Y^T Z_Y), bounded by the product of the two
Hilbert--Schmidt norms. Those norms equal ||Z_XZ_X^T||_HS and
||Z_YZ_Y^T||_HS, by their squared singular-value sums.

Let E=S^(1/2)AS^(1/2). L020(11)'s full residual form bound,
specialized to these stored coordinates in L183(18), is

\[
 \|E\|_{op}\le C N.                                    \tag{12}
\]

The normalization is L018's A=a^2 N_a and
Sigma_H=a^-2 Delta_phys^-1: their powers of a cancel on whitening.
Since A=PAP and P commutes with Sigma_H, restricting to im P gives
precisely E. Both insertion subtractions are in N_a. This is a
rough-input form bound, not L185's smooth-column consistency estimate.

The signed matrix M=2SAS now satisfies, without a positivity claim,

\[
 \|K_{XY}\|_{HS}
 =2\|Z_X E Z_Y^T\|_{HS}
 \le2\|E\|_{op}\sqrt{c_Xc_Y}.                          \tag{13}
\]

To justify (13), its squared left side divided by four is
Tr((Z_X^TZ_X) E (Z_Y^TZ_Y) E). Trace Cauchy--Schwarz bounds it
by ||Z_X^TZ_X||_HS ||E(Z_Y^TZ_Y)E||_HS. The two-sided ideal
inequality bounds the latter by ||E||_op^2 ||Z_Y^TZ_Y||_HS.
This proves (13) with no invertibility, covariance interpretation
or commutation of E and either factor.

### 3. Complete probe entries and the four signed minors

Use L185(3)–(4)'s exact full spectral expansion

\[
 B_i=a^2\sum_{k,l}d_{i;kl}e_ke_l^T,\qquad
 \sum_{k,l}|d_{i;kl}|\le C_i,\qquad
 \|e_k\|_\infty\le C a^2.                              \tag{14}
\]

Here e_k=a^2 f_k for the L2_a-normalized relative product modes.
The d coefficients retain the two actual quadratic forms and both
final-time heat factors. Their absolute summability uses the bounded
whitened probe form and the full heat spectrum, including the
allowed own-direction zero cosine modes. Therefore

\[
 \max_{e,g}|B_{eg}|\le C_i a^6.                         \tag{15}
\]

Apply entrywise Cauchy--Schwarz to each of the four terms of the
already contracted formula (1). Equations (11)–(13) show that each
product of block norms is bounded by
2||E||_op c_H c_V. For example the first is
||K_HH||_HS ||C_VV||_HS, and either mixed term is bounded by
2||E||_op sqrt(c_Hc_V) sqrt(c_Hc_V).
The signed terms remain those of (1); no cancellation is presumed.
Thus

\[
 |Q_{1,i,N}|
 \le24\max_{e,g}|B_{eg}|\,\|E\|_{op}c_Hc_V
 \le C_i a^6 N\,N^{7/2}N^4
 =C_i' N^{5/2}.                                       \tag{16}
\]

Multiplication by a^3=8^3/N^3 gives decay O(N^-1/2) and proves
(2). The threshold is O(N^3); the achieved bound is strictly below
it. Smooth residual consistency has never been assigned to M's
rough slots. The argument uses only final-time B, so it makes no
flow-time interchange or assertion about a near-zero-time integral.
The order of Q_3 differs and (16) is not transferred to it.

### 4. Exact endpoint and tensor-trace verification

Run from the active notebook:

    python3 scripts/combined-ward-response/check_probe_quartic_prefix_energy.py

The full certificate is
`scripts/combined-ward-response/probe-quartic-prefix-energy-certificate.json`.
It checks (6)–(7) exactly on six even meshes, and checks (8)'s
tensor expansion against the full four-dimensional scalar trace at
N=2,4 using the exact three-dimensional Dirichlet inverse. The
end-edge diagonal remains 2; the upper jj^T term is checked separately.
All selected verification records were inspected in full.

These rational checks support normalization and endpoint algebra.
The all-mesh proof and full-spectrum upper bounds are (4)–(16),
not an inference from finite samples. L184's unchanged Isserlis
contraction is imported without reproof. No actual probe value,
growth lower bound or full-group limit is computed by the certificate.

## Mathlib

Full matching cutoff estimate and supporting relative tensor-spectrum,
trace and covariance inequalities: **not checked**. Unknown coverage
does not imply absence. The exact signed Gaussian pairing is L184's
specialization of the named Isserlis theorem. The additional finite
matrix inequalities and the specialization of the full prefix to the
actual pinned incidence are proved above; no general flow theorem is
reproved. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this local attempt and records why renormalized full-correlation
results do not supply the selected bare group's limit. This is local
progress by assessed spectral and matrix methods, not an originality
claim or a Yang–Mills construction.
