# L149 — Complete quartic residual: local Wick reduction and insufficient absolute bound

## Hypotheses

Keep exactly L011's fixed-mesh SU(2) expansion, L009's generator,
L010's two probes with tau=1/16 and both insertion representatives.
Use L026's straight direction-1 lower-rooted forest in the relative
box, with a=8/N through sufficiently fine admitted even meshes.
The small-coupling coefficient is taken before mesh refinement.
The displacement and all insertion weights have compact interior
support. All local stencils below consequently have interior vertices
for sufficiently small a. The covariance is still the full pinned
forest covariance, including its upper-face condition.

Use dimensionless coordinates theta=g x and t_c=i sigma_c/2. For
anti-Hermitian matrices set <Y,Z>=-2 Tr(YZ). Combine the remaining
link coordinates and all three colors in X. In L018's notation put

\[
 S=\operatorname{diag}(\Sigma_F,\Sigma_F,\Sigma_F),\qquad
 B_i=\operatorname{diag}(B_{i,F},B_{i,F},B_{i,F}).                 \tag{1}
\]

Thus f_(i,0)=X^T B_i X, up to an irrelevant constant. In particular
the probe uses full-link linear Wilson flow started on the slice,
not the exponential of the forest Hessian.

## Conclusion

The complete r_2 has the explicit finite local construction (2)–(7)
below. Write it as sum_lambda q_lambda(P_lambda X), where P_lambda
selects the links and colors of the indicated local stencil, sets
forest/fixed links to zero, and q_lambda is homogeneous quartic.
Repeated occurrences of an edge use the same variable. Let

\[
 K_{\lambda,\alpha\beta\gamma\delta}
   ={1\over4!}\partial_\alpha\partial_\beta
        \partial_\gamma\partial_\delta q_\lambda,
 \quad C_\lambda=P_\lambda S P_\lambda^T,
 \quad U_{i,\lambda}=P_\lambda S B_i S P_\lambda^T.
\]

Then the exact complete contraction is

\[
 \boxed{\kappa_0(f_{i,0},r_2)
   =12\sum_\lambda K_{\lambda,\alpha\beta\gamma\delta}
          (U_{i,\lambda})_{\alpha\beta}
          (C_\lambda)_{\gamma\delta}.}                         \tag{2}
\]

Every connected pairing has one undamped internal pair C_lambda.
There is no additional pairing class without that pair. All three
colors, both insertion subtractions and the covariance subtraction
are present. No new Gaussian law for a higher jet is used.

For this complete contraction, direct local absolute estimates prove
only

\[
 |\kappa_0(f_{i,0},r_2)|\le C_i a^{-4}.                         \tag{3}
\]

Separately the two subtracted insertion quartics have the upper bound
C_i a^-3 by the same method. These are upper bounds, not asserted
asymptotics or lower bounds. They do not prove a bounded or vanishing
a^3-scaled response. In particular this reduction does not answer
the approved limit question and supplies no compensation coefficient,
logarithm, interacting estimate, continuum construction or mass gap.

## Proof

### 1. Explicit matrix-word jets of the whole insertion

On full link coordinates write Theta_e=theta_e^c t_c. For any fixed
oriented word w=((e_1,epsilon_1),...,(e_l,epsilon_l)), define

\[
 W_{w,m}(\Theta)=
  \sum_{n_1+\cdots+n_l=m}
    { (\epsilon_1\Theta_{e_1})^{n_1}\cdots
      (\epsilon_l\Theta_{e_l})^{n_l}\over n_1!\cdots n_l!}.
                                                                    \tag{4}
\]

The order of every factor is retained. This is the degree-m
coefficient of its product of link exponentials. The inverse word
reverses the order and all signs, so W_(w inverse,m)=W_(w,m)^dagger.
These are finite Taylor identities, not a global logarithm expansion.
For every based clover of L009 set

\[
 C_{\rho\nu,m}(z)={1\over8}
      \sum_{w\in\mathcal C_{\rho\nu}(z)}
         (W_{w,m}-W_{w^{-1},m}).
\]

There is no scalar projection to retain in SU(2), since the trace of
each group word is real. Also C_(rho nu,0)=0. For e=(z,nu), y=z+a e_nu,
the homogeneous left-frame generator coefficients are exactly

\[
 X_{e,m}={1\over2a}\sum_\rho\left[
 u_{a,\rho}(z)C_{\rho\nu,m}(z)
 +
 u_{a,\rho}(y)
 \sum_{\substack{r+s+t=m\\s\ge1}}
 {\Theta_e^r C_{\rho\nu,s}(y)(-\Theta_e)^t\over r!t!}
 \right].                                                        \tag{5}
\]

The second term includes both endpoint transports. None is held
fixed when taking the jet.

For each positive link e and each incident plaquette p with its
fixed orientation, cyclically base its word at the tail of e.
If e is traversed positively, it is the first factor U_e; if
negatively, it is the last factor U_e^-1. Let w_(p,e) be that word
and epsilon_(p,e) the traversal sign. Put

\[
 G_{e,m}=\sum_{p\ni e}\epsilon_{p,e}
     {W_{w_{p,e},m}-W_{w_{p,e}^{-1},m}\over2},\qquad m\ge1.
                                                                    \tag{6}
\]

To check the normalization and sign, the plaquette action is
4P_p=4-2 Tr U_p. Its variation along dot U_e=Z U_e is
-2 epsilon_(p,e) Tr(Z U_(w_(p,e))). For anti-Hermitian traceless Z,
only the anti-Hermitian part of this SU(2) word contributes.
Therefore the exact full action variation is sum_e <G_e,X_e>.
In particular G_(e,0)=0, and its linearization is D^T D theta.

Let w_p be the original plaquette word, and use the precise tilde b
and s coefficients of L010. The desired quartic is

\[
\begin{split}
 r_2={}&\left\{\sum_e\bigl(
  \langle G_{e,1},X_{e,3}\rangle+
  \langle G_{e,2},X_{e,2}\rangle+
  \langle G_{e,3},X_{e,1}\rangle\bigr)\right.\\
 &+4\sum_p\widetilde b_p\operatorname{Tr}W_{w_p,4}\\
 &\left.+2\sum_{z,\mu<\nu}s_{a,\mu\nu}(z)\sum_\alpha
       \sum_{m=1}^3\operatorname{Tr}
          (C_{\mu\alpha,m}(z)C_{\nu\alpha,4-m}(z))
                         \right\}\circ I_F .                    \tag{7}
\end{split}
\]

The second line is minus j_(3,4): P_[4]=-Tr W_4/2 and j_3=8 sum
tilde b P. The last line is minus j_(6,4): L010 has j_6=-2 sum s
Tr(C C). All three degree splittings of the clover product remain.
Formula (7), with (4)–(6), specifies every local coefficient without
requiring any finite-difference approximation to the nonlinear jet.
Use one q_lambda per edge in the first line, per plaquette in the
second, and per supported vertex/plane in the third. All stencils
have a fixed maximum size independent of N.

### 2. Check the exponential-coordinate generator

Left-frame coefficients cannot themselves be substituted for v_m
in L011(13). The coordinate conversion can be checked directly.
For U=exp Theta and dot Theta=v,

\[
 \dot U U^{-1}=\int_0^1e^{t\Theta}v e^{-t\Theta}\,dt
   =v+\tfrac12[\Theta,v]+\tfrac16[\Theta,[\Theta,v]]+\cdots.
\]

The integral follows by differentiating the matrix exponential
series, so it is valid in this finite-dimensional chart. Inverting
its series and using X_0=0 gives

\[
 v_1=X_1,\quad v_2=X_2-\tfrac12[\Theta,X_1],\quad
 v_3=X_3-\tfrac12[\Theta,X_2]
                   +\tfrac1{12}[\Theta,[\Theta,X_1]].             \tag{8}
\]

Indeed substitution in the preceding integral gives coefficients
X_1,X_2,X_3; the double-commutator coefficient is
1/12-1/4+1/6=0. Since D mathcal S[v]=sum_e <G_e,X_e> identically,
its degree-four component is both the first line of (7) and
D s_2 v_3+D s_3 v_2+D s_4 v_1. Restriction is taken only after
this identity. Thus (7) includes all coordinate corrections of
L011(13); it does not replace them by a left-frame shortcut or by
a compensated linear forest generator.

### 3. Connected contraction

For each lambda, Isserlis' finite Gaussian pairing identity applies
to (X,P_lambda X), even when C_lambda is singular. Among the fifteen
pairings of the six legs of X^T B_i X and q_lambda, three pair the
two probe legs to each other. They factor as E[f] E[q] and are
removed by the covariance. In every remaining pairing, the probe
legs attach to two distinct quartic legs. There are 4 times 3=12
choices. The two unused quartic legs then pair together. Symmetry
of the fourth derivative tensor and of B_i makes their common value
K_(alpha beta gamma delta) U_(alpha beta) C_(gamma delta).
This proves (2). The standard pairing identity also follows here
by differentiating exp(t^T S t/2) six times at zero, so no additional
moment-generating assumption for a quartic polynomial is needed.
All color indices run through P_lambda; no one-color scalar factor
has been inserted or discarded.

### 4. What the direct absolute estimate actually proves

The smooth coefficient bounds in L028 give uniformly bounded u_a,
tilde b and s. Formulas (4)–(7) have bounded word lengths and fixed
degree. Thus the absolute sum of quartic tensor entries per edge
term is at most C/a; for either insertion term it is at most C.
There are O(a^-4) supported local placements.

Every selected local link has interior endpoints. Axial entries
are forest entries and vanish; each transverse-link variance is at
most N+8 by L026(3). Cauchy–Schwarz for the actual positive covariance
then gives |(C_lambda)_(alpha beta)|<=C/a for every local entry,
including entries belonging to different plaquettes in a stencil.
This uses the exact pinned prefix, not an infinite-volume covariance.

For clarity the external estimate is obtained before contracting the
quartic. Write Delta for the physical relative Hodge Laplacian in
orthonormal cochain coordinates, E=exp(-tau Delta), and
mathcal B_i=Delta^-1/2 Q_(i,a) Delta^-1/2. L028 imports its uniform
operator bound from the actual quadratic probes. Its exact scaling
calculation, omitting the additional residual factor used there, gives
the one-color full-link external matrix

\[
 U_i^{\rm full}=T_a E\mathcal B_i E T_a^T,
 \qquad T_a=a^{-1}R_F\Delta^{-1/2}.                              \tag{9}
\]

This is also R_F Sigma B_i Sigma R_F^T in L018's dimensionless
full-link notation. This use of the linear Gaussian lift concerns
only the covariance and quadratic probe; the nonlinear polynomial
in (7) stays evaluated on the forest slice.

If e_k is an ordinary-coordinate normalized relative mode, its
stored entries are a^2 times a smooth normalized sine/cosine mode.
The physical eigenvalues satisfy lambda_k>=c|k|^2. On any of the
interior links in (7), the exact prefix formula L028(9) bounds
|(T_a e_k)_e| by a times a fixed polynomial in |k|. The difference
of the two transverse endpoint samples costs a derivative times a;
the prefix contains at most 8/a such differences. Axial forest
entries vanish. This argument applies to each link of every local
stencil, not only to the axial plaquettes selected in L028's final
contraction. No smooth extension across the pinned upper jump is
used. Expanding both E factors in (9), the uniform matrix-entry
bound on mathcal B_i and the summable full double heat-mode series
give |(U_(i,lambda))_(alpha beta)|<=C_i a^2. This includes every
allowed heat mode; it is not a fixed-mode approximation.

Consequently the edge terms in (2) have the direct estimate

\[
 O(a^{-4})\,O(a^{-1})\,O(a^2)\,O(a^{-1})=O(a^{-4}),
\]

and the insertion terms give O(a^-3). This proves (3), with constants
that need not be small. The bound on a^3 times (2) is only C_i/a.

To state the remaining cancellation threshold precisely, enlarge
the placement list by zero tensors if necessary and write
K_lambda=a^-1 T_lambda+M_lambda, where T contains the force/vector
part and M the two signed insertion subtractions. Set
bar U=a^-2 U and bar C=a C. These tensors are uniformly bounded by
the preceding estimates. Define the signed volume-weighted sum

\[
 Z_{i,a}=a^4\sum_\lambda
  (T_\lambda+aM_\lambda)_{\alpha\beta\gamma\delta}
       (\bar U_{i,\lambda})_{\alpha\beta}
       (\bar C_\lambda)_{\gamma\delta}.
\]

Equation (2) says a^3 kappa_0(f_(i,0),r_2)=12 Z_(i,a)/a.
The absolute argument proves only Z_(i,a)=O(1). The requested zero
limit requires Z_(i,a)=o(a). Even cancellation of its order-one
part would not by itself settle the order-a contribution, which
includes both insertion subtractions. This is an exact description
of the estimate still missing, not a solution by reformulation.
No finite-trace cancellation or nonzero limit is asserted here.

## Mathlib

Full matching coverage and coverage of the SU(2) word-jet and Gaussian
pairing specialization: **not checked**. Unknown coverage is not
absence. The finite Taylor and pairing identities are proved above
to fix this insertion's signs, coordinate convention and factor 12;
they are reproductions of standard finite-dimensional algebra, not
claims of new general mathematics. The existing
[source assessment](../drafts/literature/2026-10-12-quartic-residual-insertion-cubic-scale.md)
remains applicable. None of its full-response renormalization or Ward
statements is imported as an estimate of this isolated bare jet.
