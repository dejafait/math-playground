# L151 — The first-order covariance remainder reduces to an axial slope

## Hypotheses

Keep L149 and L150's SU(2) quartic residual, actual probes i=3,6,
tau=1/16, compact interior displacement, a=8/N and straight lower-rooted
direction-1 forest. The bare coefficient is taken at fixed mesh before
refinement. All covariances are the full pinned forest covariances.
For each supported force/vector edge stencil use L150's midpoint c,
axial lattice coordinate j_*, frozen tensor K_e^0, frozen exterior
matrix U_i^0(c), and comparison C_e^0=j_* P_inf. Axial link rows are
zero and colors are independent identical copies. The stencil radius
is fixed and every endpoint has distance at least delta N from every
physical face for some fixed delta>0 once N is sufficiently large.

Here e labels the central force/vector edge; write (s,l),(t,m) for
two selected transverse links, with l,m their transverse edge indices.
Their axial levels obey |s-j_*|,|t-j_*|<=R. Use the exact P, Delta_T
and R_st from L085, and the infinite transverse projection P_inf
with the oriented-edge convention in L114(1).

## Conclusion

Define on each local stencil, including the color Kronecker delta,

\[
 S_e((s,l),(t,m))=\left({s+t\over2}-j_*\right)P_\infty(l,m).
                                                               \tag{1}
\]

Then the third force/vector difference in L150(11) has the comparison

\[
 a^3\,12\sum_e K_e^0:U_i^0:(C_e-C_e^0)
 -12a^4\sum_e (aK_e^0):(a^{-2}U_i^0):S_e\ \longrightarrow\ 0.
                                                               \tag{2}
\]

The factor twelve is the complete connected-pairing factor of L149.
Both sums include every supported central edge direction and every
local index and color. The actual external heat sum stays in U_i^0.
The right-hand volume sum in (2) is bounded, but its convergence,
value and vanishing are **not** asserted.

In particular the stationary co-closed covariance and the local
absolute-value kink in min(s,t) give zero in this frozen contraction.
The local projection/boundary comparison error is o(a^-3) after
summation. The axial slope (1) remains. Neither of the other two
differences in L150(11), nor either insertion subtraction, is removed.
This is one input toward the unchanged complete-response target,
not a zero cubic coefficient or a compensation result.

## Proof

### 1. Uniform local limit of the co-closed covariance

Set H_N((s,l),(t,m))=[R_st(Delta_T)(I-P)]_(l,m). Let h_v(n) be
the heat kernel of 2-shift-shift^(-1) on Z, and let Delta_inf act
componentwise on oriented transverse edges of Z^3. Define

\[
 H_\infty((s,l),(t,m))=
 \int_0^\infty h_v(s-t)
       [e^{-v\Delta_\infty}(I-P_\infty)]_{l,m}\,dv.        \tag{3}
\]

We prove absolute convergence and, uniformly over the supported
stencils and all their pairs,

\[
 H_N-H_\infty=o(1).                                      \tag{4}
\]

The finite spectral theorem and the exact commuting projection P
give the entry identity

\[
 H_N=\int_0^\infty
 [e^{-v L_D}]_{s,t}
 [e^{-v\Delta_T}(I-P)]_{l,m}\,dv.                         \tag{5}
\]

This retains the full axial Dirichlet resolvent in L085(2), rather
than replacing it by its axial zero mode. For its one-dimensional
heat kernel, the sine-mode entry bound 2/N, eigenvalue bound
4k^2/N^2, and the sum over all k>=1 give

\[
 |[e^{-vL_D}]_{s,t}|\le C(1+v)^{-1/2}.                    \tag{6}
\]

For v>=1 this follows by bounding the diagonal by
(2/N) sum_(k>=1) exp(-4vk^2/N^2), then using heat-kernel
Cauchy--Schwarz for off-diagonal entries. The elementary Gaussian
sum bound holds also when v>N^2: extract an exponential in v/N^2
as in L114's shell argument. For v<=1 use the operator bound one.
The same bound follows for h_v by its one-dimensional Fourier
integral and 4 sin^2(theta/2)>=4 theta^2/pi^2 on [-pi,pi].

In each finite component of Delta_T, ordinary normalized tensor
modes have squared entries <=8/N^3, one possibly zero cosine index,
and two positive sine indices. Thus r=max k_mu is always >=1;
its shell has O((r+1)^2) labels and lambda>=4r^2/N^2. The full
shell estimate, including v>N^2, proves

\[
 [e^{-v\Delta_T}]_{l,l}\le C(1+v)^{-3/2}.                 \tag{7}
\]

Since P is an orthogonal projection commuting with Delta_T,
0<=e^(-v Delta_T)(I-P)<=e^(-v Delta_T) in operator order.
Positive-matrix Cauchy--Schwarz and (7) give the same bound for
every entry of the projected heat kernel. Infinite Fourier
integration gives (7) for the componentwise full-grid kernel and
the same positive-operator comparison applies to P_inf. Combining
(6) and (7), the absolute integrands in (3) and (5) are bounded by

\[
 C(1+v)^{-2},                                            \tag{8}
\]

uniformly in N and in the selected indices. Their tails beyond V
are consequently <=C/(1+V). No boundary input row is omitted.

For clarity, local convergence at fixed heat time must also retain
the nonlocal projection. Let T be the finite transverse gradient,
Delta_0=T^T T. L085's intertwining and L114's heat representation give

\[
 e^{-v\Delta_T}P
   =T e^{-v\Delta_0}\Delta_0^{-1}T^T
   =\int_v^\infty T e^{-w\Delta_0}T^T\,dw.               \tag{9}
\]

The infinite counterpart holds entrywise and strongly; its Fourier
multiplier is e^(-v lambda) tt*/lambda. It does not require an
unbounded inverse to act on an arbitrary l2 vector.

For any finite normalized Dirichlet vertex mode phi_k, the explicit
endpoint difference used in L150 gives
|(T phi_k)_l|^2<=C N^-3 lambda_k. Hence, for w>=1, the shell sum
with its additional lambda_k factor yields

\[
 |[T e^{-w\Delta_0}T^T]_{l,m}|
  \le C N^{-5}\sum_{r\ge1}r^4 e^{-cwr^2/N^2}
  \le C w^{-5/2}.                                       \tag{10}
\]

The off-diagonal bound again follows by positivity. For w<=1 the
gradient and heat operator norms give a uniform constant. Infinite
Fourier integration of lambda exp(-w lambda) gives the same bound.
Thus the tails of (9) past W>=1 are bounded by C W^-3/2 uniformly.

For fixed bounded w, all the unprojected finite heat kernels in
(5) and (9) converge to their infinite counterparts uniformly on
these stencils. One elementary way to see this avoids any assertion
of projection locality. The dimensionless Laplacians have uniformly
bounded norms and fixed nearest-neighbor range. At interior rows
their coefficients are exactly those of the full-grid operator,
also for the edge component with a reflected normal boundary.
A polynomial of degree k therefore has identical local entries
when every relevant vertex is farther than k plus the stencil
radius from the faces. Approximate e^(-w L) by its Taylor
polynomial: on 0<=w<=W the norm error is at most the exponential
series tail with argument W sup||L||, independent of N. Take the
degree large first, then N large. This also works with the two
fixed-range gradients in (9), and for the axial heat kernel.

Apply that argument to (9) up to a fixed W and then remove W using
(10). It proves local convergence of the projected transverse
heat kernel uniformly for v in any fixed compact interval. Use
(8) to remove the remaining v tail in (3),(5). This proves (4)
uniformly for every allowed stencil center, not just for one
fixed physical point. The proof keeps the complete spectra and
does not interchange an uncontrolled mass or mesh limit.

### 2. Split the bounded covariance correction by inversion parity

L150(5), with every local row interior, implies

\[
 j_* |P(l,m)-P_\infty(l,m)|
    \le C N^{-1/2}(\log N)^{3/4}=o(1),                   \tag{11}
\]

since j_*<=N. The same estimate without j_* controls a bounded
coefficient times the projection difference. From L085's exact
covariance and (4),(11), uniformly on each stencil,

\[
\begin{split}
 C_e-C_e^0
   &=\bigl(\min(s,t)-j_*\bigr)P_\infty(l,m)
           +H_\infty((s,l),(t,m))+o(1)\\
   &=S_e+E_e+o(1),\\
 E_e((s,l),(t,m))
   &=-\tfrac12|s-t|P_\infty(l,m)
           +H_\infty((s,l),(t,m)).                     \tag{12}
\end{split}
\]

Axial rows are zero throughout and the color factor is delta_cd.
In particular (12) is an entrywise local statement, not a global
operator approximation of the forest covariance.

Invert all vertices about the central midpoint c, as in L150.
A transverse edge at axial level s goes to one at 2j_*-s; the
two orientation signs in a covariance multiply to plus one.
The infinite transverse gradient projection is equivariant under
this signed edge permutation. The componentwise full-grid heat
kernel commutes with it too, and h_v(s-t)=h_v(t-s). Thus the
matrix H_inf in (3) is invariant under this inversion, including
when c has a half-integer coordinate. Since |s-t| is unchanged,
E_e is inversion-even. By contrast (s+t)/2-j_* changes sign,
so S_e is inversion-odd.

L150(9) gives oddness of the **complete** frozen degree-four
force/vector tensor K_e^0 under precisely this permutation.
It includes all three degree splittings and endpoint transports.
U_i^0 is inversion-even by its definition, with no positivity
assumption. Apply the signed permutation to every contracted index:

\[
 K_e^0:U_i^0:E_e=-K_e^0:U_i^0:E_e=0.                     \tag{13}
\]

There is no such parity conclusion for S_e: its sign change
multiplies the sign change of K_e^0. In particular (13) does not
license deletion of the whole bounded covariance remainder.

### 3. Sum the uniform error at the required scale

Let epsilon_N tend to zero and bound the maximum entrywise error
in (12) uniformly over all supported stencils and indices. Such
epsilon_N exists by steps 1 and 2. Their sizes and color counts
are fixed. L150 gives |K_e^0|<=C/a and |U_i^0|<=C_i a^2;
the latter already includes every external heat mode. Consequently

\[
 |K_e^0:U_i^0:(C_e-C_e^0-S_e)|\le C_i a\,\epsilon_N.      \tag{14}
\]

There are O(a^-4) supported central edges. Sum (14), retain the
factor twelve from L149, and multiply by a^3. The error is at
most C_i epsilon_N, proving (2). The slope entries in (1) are
bounded because |s-j_*|,|t-j_*|<=R and ||P_inf||<=1, so the
right-hand volume sum is bounded as stated.

The other terms in the exact decomposition are unchanged:
(K_e-K_e^0):U_i:C_e, K_e^0:(U_i-U_i^0):C_e, and both insertion
subtractions. They retain their signs and only their L150 cubic
bounds. Equation (2) supplies a fixed local slope tensor for one
part of their future joint contraction. It does not give a full
first-order expansion, rate for the little-o error, actual-probe
coefficient, or cancellation with any other response group.

## Mathlib

Full matching theorem and supporting lattice heat-kernel/projection
coverage: **not checked**; unknown availability is not absence.
The finite spectral theorem, Fourier heat representation,
positive-matrix Cauchy--Schwarz and dominated convergence are used
in their standard forms, with the boundary and uniformity details
proved above. L085 supplies the exact forest identity; L114 supplies
the projection heat calculus; L149/L150 supply the complete
contraction, single-row estimate and frozen parity. The specialization
is needed because an isolated bare forest jet is not bounded by the
full renormalized-response statements in the reused
[assessment](../drafts/literature/2026-10-12-quartic-residual-insertion-cubic-scale.md).
No new general heat theorem or certified originality is claimed.
