# L152 — The complete quartic residual has a finite signed cubic limit

## Hypotheses

Keep exactly L149–L151's SU(2) insertion, all three colors, both actual
L010 probes i=3,6 with tau=1/16, a=8/N through admitted even meshes,
relative box D=(-4,4)^4 and straight direction-1 lower-rooted forest.
The small-coupling coefficient is taken at fixed mesh before refinement.
Keep both signed insertion subtractions in L149(7). Use L008's smooth
compact displacement and central strains. The full pinned covariance,
including the upper-face condition, is used throughout.

Use the ordinary-coordinate fourth-derivative tensor convention of
L149: the tensor of a quartic q is (1/4!) times its fourth derivative.
For such a tensor F and two matrices V,W write
F:V:W=sum F_(alpha beta gamma delta) V_(alpha beta) W_(gamma delta).
Indices include links and colors; repeated occurrences denote the same
link variable. Axial link rows are zero on every supported stencil.

## Conclusion

For both probes the complete response has a finite real limit

\[
 a^3\kappa_0(f_{i,0},r_2)\longrightarrow\Lambda_i.             \tag{1}
\]

An explicit finite-stencil/full-heat-mode expression for Lambda_i is
(8) below. It retains the displacement jet, exterior jet, axial
covariance slope and both insertion subtractions jointly. Its integrals
and heat-mode sums converge absolutely. **Neither Lambda_i=0 nor its
value or sign is established.** Thus (1) advances the asymptotic input
from boundedness to existence but does not answer the approved zero-limit
question. No compensation, finer remainder, logarithm, interacting
bound or Yang–Mills construction follows.

## Proof

### 1. Define the finite tensors without replacing any word jet

For each central edge direction nu=1,...,4, translate the stencil of
L149(4)–(6) so its central edge midpoint is the origin, and measure all
positions in lattice units. Use the union stencil from L150, with zero
coefficients where needed. For a selected link alpha let h_alpha be
its midpoint offset, mu_alpha its direction, and c_alpha its color.
Let p_nu be its local covariance obtained from P_inf in L151, independent
of the axial levels, with color factor delta_(c_alpha,c_beta) and zero
axial rows. Let

\[
 (S_\nu)_{\alpha\beta}
 ={h_{\alpha,1}+h_{\beta,1}\over2}(p_\nu)_{\alpha\beta}.       \tag{2}
\]

This is precisely L151's slope tensor at this central midpoint.
All h_alpha belong to a fixed finite set. The projection entries are
the oriented transverse-edge entries of the infinite-grid gradient
projection in L114(1), with its original edge phases.

Define the tensor-valued linear map F_nu[v] as follows. Take the quartic
first line of L149(7), for this central edge, from the ordered words
(4)–(6); remove only the outside factor 1/a in X_e,m, equivalently set
that factor to one. Set axial variables to zero, and take its symmetric
fourth-derivative tensor. The input v assigns displacement components
to the two endpoints h=-e_nu/2,+e_nu/2. The factor 1/2 from endpoint
averaging stays in F_nu. This definition retains all three splittings,
every clover word, endpoint conjugation, incident action sign and color.
It is a finite, a-independent map linear in v; no covariance or
continuum field is inserted into its definition. For x in D put

\[
 F_\nu^0(x)=F_\nu[v_\rho(h)=u_\rho(x)],\qquad
 F_\nu^1(x)=F_\nu[v_\rho(h)=\sum_j h_j\partial_j u_\rho(x)]. \tag{3}
\]

There are also two kinds of insertion placements. For each mu<nu
use one plaquette of that plane, centered at the origin, and define
M_(P,mu nu)(x) as the tensor of
4(w_mu+w_nu)(x) Tr W_(w_p,4). For each mu<nu use one vertex centered
at the origin and define M_(V,mu nu)(x) as the tensor of

\[
 2s_{\mu\nu}(x)\sum_\alpha\sum_{m=1}^3
       \operatorname{Tr}(C_{\mu\alpha,m}C_{\nu\alpha,4-m}).   \tag{4}
\]

Here W,C are exactly the dimensionless local words of L149(4),(7),
restricted to axial-zero variables. Sum over the twelve placement
types t=(P,mu nu),(V,mu nu). Define p_t by the same local transverse
projection rule as p_nu. Their midpoint offsets are taken relative
to their own plaquette or vertex center. In particular these are the
two **subtracted** insertions with exactly the signs in L149(7).
No Haar-divergence or coordinate-density term is added.

### 2. The continuum exterior kernel and its first derivatives

Let k include the component of an L2-normalized real relative one-form
product mode f_k on D. Its eigenvalue is lambda_k>0. Write b_(i,kl)
for the continuum entries of the covariance-normalized curvature form
B_i in L008(16), not the dimensionless flowed matrix of L018(2).
Define its normalized continuum forest column on compact interior sets by

\[
 \ell_{k,1}=0,\qquad
 \ell_{k,\mu}(x)=\lambda_k^{-1/2}\left[
 f_{k,\mu}(x)-\int_{-4}^{x_1}
              \partial_\mu f_{k,1}(t,x_\perp)\,dt\right],
 \quad \mu=2,3,4.                                        \tag{5}
\]

Components absent from f_k are zero. The constant axial cosine mode
gives an integral proportional to x_1+4; it is included in (5).
There is no upper-face pin imposed on this interior extension.
Define the color-diagonal two-point exterior kernel

\[
 H_{i,\mu c,\eta d}(x,y)
 =\delta_{cd}\sum_{k,l}e^{-\tau(\lambda_k+\lambda_l)}
       b_{i,kl}\ell_{k,\mu}(x)\ell_{l,\eta}(y).             \tag{6}
\]

For any stencil type, H_i^0(x) is the local matrix with entry
H_(i,mu_alpha c_alpha,mu_beta c_beta)(x,x). For a central-edge type
also define

\[
 (H_{i,\nu}^1(x))_{\alpha\beta}
 =\left[\sum_j h_{\alpha,j}\partial_{x_j}
              +h_{\beta,j}\partial_{y_j}\right]
 H_{i,\mu_\alpha c_\alpha,\mu_\beta c_\beta}(x,y)\big|_{y=x}.
                                                               \tag{7}
\]

The derivative in (7) acts on the two arguments separately. It is not
the derivative of the diagonal with one common offset. The two exterior
orientations and all off-diagonal component entries remain.

With d(x)=x_1+4, the promised functional is

\[
\begin{split}
 \Lambda_i=12\int_D\bigg\{\sum_{\nu=1}^4\big[&
 d\,F_\nu^1:H_i^0:p_\nu
 +d\,F_\nu^0:H_{i,\nu}^1:p_\nu
 +F_\nu^0:H_i^0:S_\nu\big]\\
 &+d\sum_t M_t:H_i^0:p_t\bigg\}\,dx .                     \tag{8}
\end{split}
\]

Each H_i^0 in (8) is restricted to the stencil of the tensor beside it.
Equations (2)–(7), together with L149's finite word formula, specify
every entry, including the factor twelve. No scalar color factor is
inferred in place of the explicit color indices.

We now justify all limits needed for (8).

### 3. Uniform smooth convergence of the actual exterior kernel

For the finite mesh let b_(i,kl,a) be L008's normalized form entries
and lambda_(k,a) its physical eigenvalues. Put ell_(k,a)=a^-1 T_a e_(k,a),
where T_a is L149(9) and e_(k,a) is the ordinary-coordinate normalized
mode. L028(9) gives its samples on every interior transverse link.
Extend those samples smoothly as in L150 section 2, using exact axial
sine primitives and the centered transverse difference. This extension
matches the actual link values at their midpoints.

For detail, for an axial cosine factor cos(pi k_1(t+4)/8), its midpoint
sum to an interior level j satisfies, when k_1>0,

\[
 a\sum_{r=0}^{j-1}\cos\!\left({\pi k_1(r+1/2)\over N}\right)
 ={a\sin(\pi k_1 j/N)\over2\sin(\pi k_1/(2N))}.            \tag{9}
\]

For k_1=0 it is aj. The transverse difference is centered at the
transverse-link midpoint. For a fixed label, its quotient converges
with all fixed derivatives to partial_mu f_(k,1); the smooth extension
of (9) converges to its integral from -4 to x_1. The factor
(pi k_1/(2N))/sin(pi k_1/(2N)) is bounded uniformly for 1<=k_1<N.
Normalization factors of the sine/cosine modes, including their zero
indices, are those of L028; division by sqrt(lambda_(k,a)) is harmless
by the uniform relative gap in L008(15). It follows that on any fixed
compact interior set and for each fixed nonnegative r,

\[
 \|\ell_{k,a}\|_{C^r}\le C_r(1+|k|)^{r+2},\qquad
 \ell_{k,a}\longrightarrow\ell_k\quad\hbox{in }C^r
 \quad\hbox{for each fixed }k.                            \tag{10}
\]

For example, every derivative of the finite primitive is bounded by
the physical mode frequency times its bounded interval length or
primitive factor; the centered transverse quotient is the average
of a derivative. These observations give the displayed polynomial
bound, including k_1=0 and modes near the cutoff. A looser polynomial
bound would suffice. No extension through the upper pinned jump is used.

L008 supplies |b_(i,kl,a)|<=C_i, entrywise convergence to b_(i,kl),
and lambda_(k,a)>=|k|^2/16. Extend missing mode contributions by zero.
Insert the smooth ell_(k,a) in the finite counterpart H_(i,a) of (6).
For r<=2 its differentiated summands are bounded by a constant times

\[
 e^{-\tau(|k|^2+|l|^2)/16}
               (1+|k|)^4(1+|l|)^4.                        \tag{11}
\]

The sum over all component-labeled four-dimensional modes is finite.
The same bound applies in the continuum. Fix a mode cutoff, use
L008's entry convergence and (10), then remove the cutoff with (11).
This proves uniform C^2 convergence of H_(i,a) to H_i on the compact
two-point set. It also proves absolute convergence of (6) and its
derivatives. This step reuses L008's fixed-mode comparison; it does
not need a first-order rate for b_(i,kl,a).

By L149(9) and the exact linear quotient identification, the actual
local exterior matrix is therefore
U_(i,e,alpha beta)=a^2 H_(i,a,mu_alpha c_alpha,mu_beta c_beta)
(c+a h_alpha,c+a h_beta). Choose L150's frozen matrix consistently as
U_i^0=a^2 H_(i,a)(c,c). Uniform Taylor expansion and C^2 convergence give

\[
 a^{-2}U_i\to H_i^0(c),\quad a^{-2}U_i^0\to H_i^0(c),\quad
 a^{-3}(U_i-U_i^0)\to H_{i,\nu}^1(c),                     \tag{12}
\]

uniformly over the supported stencils. In the last convergence the
Taylor remainder is O(a) after division by a^3, and the first
derivatives of H_(i,a) converge uniformly. Thus no unknown O(a)
coefficient of the diagonal H_(i,a)(c,c) enters (12).

### 4. Displacement, insertion and covariance comparisons

The tensor definition gives the exact identities
K_e=a^-1 F_nu[v_rho(h)=u_(a,rho)(c+a h)] and
K_e^0=a^-1 F_nu[v_rho(h)=u_(a,rho)(c)]. L028's smooth coefficient
extensions converge in C^2 and have uniformly bounded C^2 norms.
Linearity of F_nu and ordinary Taylor expansion therefore imply,
uniformly in supported central edges,

\[
 aK_e^0\to F_\nu^0(c),\qquad K_e-K_e^0\to F_\nu^1(c).    \tag{13}
\]

The expansion is about the edge midpoint, so the actual two endpoint
offsets in (3) are essential. Similarly the insertion tensor M_(t,a)
converges uniformly to M_t: the vertex shear is s_a, and the
four-vertex plaquette weight tilde b tends at its center to w_mu+w_nu.
All finite words and their signs are unchanged in that comparison.

For each compact local stencil, L150's covariance/projection estimates
give C=C^0+O(1), C^0=j_* p, uniformly, with j_*=d(c)/a. Thus

\[
                    aC\longrightarrow d(c)p.             \tag{14}
\]

For an insertion stencil the same entry estimate applies: the proof
of L150 section 1 uses only a fixed radius, interior transverse rows
and |s-j_*|<=R, not a central-edge coefficient. Choose its plaquette
or vertex center for j_*; all these conditions still hold. In
particular no boundary covariance has been replaced globally.

For the central-edge frozen covariance difference L151 gives the
full summed replacement by S_nu, with o(a^-3) error. Its uniform local
proof applies to the frozen choice U_i^0 in (12): this matrix is
inversion-even, spatially constant on the stencil and O(a^2), exactly
the properties used there. The stationary co-closed and absolute-value
kink terms disappear only in that contraction, by L150's odd frozen
force/vector tensor. The slope (2) remains.

### 5. Sum the complete first order, with its errors controlled

The following is an exact decomposition for every force/vector placement:

\[
\begin{split}
 K_e:U_i:C={}&(K_e-K_e^0):U_i:C
 +K_e^0:(U_i-U_i^0):C
 +K_e^0:U_i^0:(C-C^0).                                  \tag{15}
\end{split}

The omitted frozen term is exactly zero at every mesh by L150(10).
Divide the first two terms of (15) by a. Equations (12)–(14) show that
they converge uniformly, respectively, to
d F_nu^1:H_i^0:p_nu and d F_nu^0:H_(i,nu)^1:p_nu.
For the third term L151 permits the summed replacement by
K_e^0:U_i^0:S_nu; after division by a this converges uniformly to
F_nu^0:H_i^0:S_nu. For each insertion placement,
a^-1 M_(t,a):U_i:C converges uniformly to d M_t:H_i^0:p_t.
The stencil sizes and color counts are fixed, so entrywise uniform
convergence controls each entire finite contraction.

There are O(a^-4) placements, contained in one compact interior set.
The factor a^3 in (1) turns each sum into a^4 times the sum of these
per-placement terms divided by a. Their uniform errors therefore tend
to zero, since the total weighted number of supported placements is
bounded. L151 supplies the remaining summed error with the same
normalization and connected factor. Each of the four central-edge
types, six plaquette types and six vertex types has one placement per
corresponding shifted lattice site. For each type its compact-support
Riemann sum converges to the ordinary integral over D; shifts by a
half-step do not change the limiting density. Taking their finite
sum, and retaining L149's factor twelve once, proves (8) and (1).

All integrands have compact support through u or its derivatives,
are continuous and bounded there, and involve finitely many bounded
projection entries. The absolute heat-mode convergence established
in (11) permits integration term by term, also for (7). Consequently
(8) is an absolutely convergent real functional for both actual probes.
This proof takes a fixed finite mode cutoff before removing its uniform
tail; it takes no uncontrolled simultaneous cutoff/mass limit.

The first-order functional is not removed by frozen inversion: the
displacement jet, exterior jet and slope each have the additional
inversion parity needed to survive. Both insertion tensors also stay.
One must evaluate their **joint** actual-probe contraction, or prove a
signed identity for it, to decide whether either Lambda_i is zero.
The proof establishes no such identity or value.

## Mathlib

Full matching theorem and supporting relative-lattice/forest convergence
coverage: **not checked**; unknown is not absence. The finite Taylor,
dominated heat-series and compact-support Riemann arguments are standard
methods, specialized here to fix all offsets, normalizations and signs.
The finite connected contraction is reused from L149, parity from L150,
and covariance slope from L151. L008 and L028 supply the needed actual
mode and coefficient inputs; their precise applicability is shown above.
The saved quartic-residual source assessment remains applicable and
provides no isolated-jet estimate to import in place of this calculation.
This is local progress beyond the bounds previously proved in the
notebook, with no certified originality or resolution claim.
