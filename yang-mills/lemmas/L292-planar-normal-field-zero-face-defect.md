# L292 — Zero signed planar defect for a frozen normal external field

## Hypotheses

The finite-box starting conventions are L280's SU(2) Wilson action,
generators \(t^a=i\sigma^a/2\), Euclidean counting measure, boundary-fixed
gauges, boundary-contained pinned links and every variable normal end
link. Use its ambient all-link tensors \(T,U\), complete density matrix
\(D\), and transverse covariance \(G\). Thus the operator whose external
contraction selects the three \(G_{-+}\) terms is
\[
 S=D-\tfrac14 A+\tfrac14 E,\qquad
 A_{ij}=\sum_{kl}U_{ijkl}G_{kl},\quad
 E_{il}=\sum_{jkmn}T_{ijk}T_{lmn}G_{jm}G_{kn}.                 \tag{1}
\]
Color indices are included. The selected coefficient is
\(\operatorname{Tr}(S G_{-+})\); this is not the entire coefficient.

Here is the precise local test, including its regulators. Set lattice
spacing to one for this test. The lower face is the plane \(n=0\).
Vertices have \(n\geq0\) and tangential coordinate \(z\in\mathbb Z^3\).
Vertex gauge functions vanish at \(n=0\). Normal edges run from \(n\)
to \(n+1\), \(n\geq0\); tangential edges exist at \(n\geq1\) and are
zero at \(n=0\). All surviving plaquettes have their original Wilson
weight, including the normal plaquettes incident on this face.
No half weight is assigned to a boundary vertex or normal edge.

Use the massless relative covariance and density constructed in section
1 below, not a scalar replacement for \(G\). The frozen field is a
constant unit color \(t^a\) on all normal edges and zero on tangential
edges. It is not an \(\ell^2\) vector. Its face defect is therefore
defined by the plane row sums in section 2, not by an infinite
quadratic form.

A finite regulator has tangential periodic length \(\ell\), even
normal thickness \(M\), pinned tangential links on both end planes,
and all \(M\) normal links on each vertical line. The gauge group is
identity on both end planes. Remove the three constant normal
harmonic fluctuations from the Gaussian inverse. Take
\(\ell\to\infty\) at fixed \(M\), and only then \(M\to\infty\).
The removed mode and the effect of this order are computed below.
Tangential momentum cutoffs at zero are removed by the integrable
bounds below; no positive-mass theorem is assumed.

The exact product bump, even original \(N\), \(a=8/N\), both source
orders, all colors and L280's real source domain remain the hypotheses
of any later application to the original box. This local test does
not replace those sources by constants in that box.

## Conclusion

Let \(b_H(n)\) be the complete normal plane row sum of (1) on this
half-space, and \(b_\infty\) its full-lattice row sum for the same
unit normal color. Then
\[
 b_\infty=0,\qquad
 |b_H(n)-b_\infty|\leq \frac{C}{(1+n)^2},\qquad
 \boxed{\displaystyle\sum_{n=0}^{\infty}
                 (b_H(n)-b_\infty)=0.}                       \tag{2}
\]
The bound is on the signed row after retaining every density, quartic
and cubic contraction; the proof also bounds the defects of these
three groups separately. In particular the depth sum is absolutely
convergent. Polarization gives the same zero for two frozen normal
color vectors.

This removes this particular frozen normal-field surface obstruction.
It does not prove an \(o(N)\) estimate for the original source
contraction. Actual L282 fields need not have constant boundary
values; their boundary traces/pairings, all faces/edges/corners, other
groups and uniform errors at that scale remain unproved. L287's
external-curl error is not dropped for those fields. No quantitative
bound for the full subleading coefficient, uniform higher remainder,
interacting lower bound, continuum theory or mass gap follows.

This is a local derivation under the saved EXPLORE assessment,
not a claim of originality beyond its checked sources. The separate
conceptual audit in section 6 accepts (2) under precisely these
hypotheses and regulator order; it establishes no stronger estimate.

## Proof

### 1. Exact relative half-space matrices

Let \(\delta v(n)=v(n+1)-v(n)\), with \(v(0)=0\). It maps interior
vertices to all normal edges. For the slab also set \(v(M)=0\).
The normal part of L280's \(B\) is \(-\delta\). Put
\(\mathsf a v(n)=(v(n+1)+v(n))/2\), including the zero endpoint
values; the normal part of its \(M\) matrix is \(2\mathsf a\).
This notation \(\mathsf a\) is an averaging map, not physical mesh.

In tangential midpoint Fourier coordinates put
\[
 d_j=2\sin(p_j/2),\quad s=\sum_{j=1}^3d_j^2,\quad
 2(\cosh\kappa-1)=s,\quad
 r_s(k)=\frac{e^{-\kappa|k|}}{2\sinh\kappa}\quad(s>0).
                                                               \tag{3}
\]
The omitted value \(p=0\) has measure zero. Midpoint changes of phase
are unitary and are retained in the incidence and averages. Define
\[
 R_D=(s+\delta^*\delta)^{-1},\qquad
 R_N=(s+\delta\delta^*)^{-1}.
\]
Their half-space kernels are exactly
\[
 R_D(n,m)=r_s(n-m)-r_s(n+m)\quad(n,m\geq1),
\]
\[
 R_N(n,m)=r_s(n-m)+r_s(n+m+1)\quad(n,m\geq0).              \tag{4}
\]
To verify (4), the scalar recurrence has diagonal \(s+2\) and
off-diagonal \(-1\). Its full-line inverse is \(r_s\), since
\((s+2)r_s(0)-2r_s(1)=1\). The Dirichlet difference vanishes at
vertex zero. On normal edge zero, \(\delta\delta^*\) has diagonal
one, so the second formula obeys the row with diagonal \(s+1\).
Both kernels decay at infinity and the positive \(s\) inverse is
unique. Thus this is the actual staggered normal-edge convention,
not the corrected scalar Neumann space of a different discretization.

The one-form Hodge inverse is diagonal by component, with \(R_N\)
on normal edges and \(R_D\) on tangential edges. As in L003's interval
complex and L280, set
\[
 P=B\Delta^{-1}B^*,\quad J=M_{\rm sum}\Delta^{-1}B^*,\quad
 G=L^{-1}-B\Delta^{-2}B^*,\quad
 \Delta=B^*B,\quad L=C^*C+BB^*.                            \tag{5}
\]
Here \(M_{\rm sum}\) denotes L280's endpoint-sum matrix. In (5),
inverse-square expressions are always sandwiched as displayed;
they are not an assertion of a bounded massless inverse square.
At fixed \(p\neq0\), \(\Delta^{-2}=R_D^2=-\partial_s R_D\).
Also \(\delta R_D=R_N\delta\). These identities follow by multiplying
the two resolvents or by differentiating their positive-\(s\) inverse.

The Fourier spectral construction makes \(P\) the orthogonal
projection onto the closure of the relative gradients: in the
polar decomposition of \(B\), \(B\Delta^{-1}B^*\) is that projection.
Equivalently it is the strong limit of
\(B(\Delta+\epsilon)^{-1}B^*\). The scalar Dirichlet Laplacian has
no \(\ell^2\) zero vector. On the orthogonal complement, (5) is
the massless inverse of \(C^*C\), with finite matrix entries and
positive Gaussian finite marginals. The estimates below justify
the zero-momentum passage; an \(\ell^2\)-bounded \(G\) is not claimed.

These are also local limits of the original relative cubes viewed
from one face while the other faces recede. For precision, use
L283's polynomial approximation to \(G\): at each fixed degree its
paths eventually coincide with the half-space paths, and its
entry error tends to zero uniformly over the cubes. On the
half-space, the same polynomials converge to (5) by the explicit
Fourier/sine/cosine spectral formula and integrability of
\(\lambda^{-1}\) in four dimensions. For \(P,J,D\), use L282's
polynomials in \(\Delta\) and its row-square bounds; their fixed
paths agree and their errors tend to zero. L288 gives the analogous
finite-range approximation to the internal-curl contraction.
This identifies local matrices, not growing-depth or surface sums.
The latter are justified independently below.

The density retains the entire formula
\[
 D_{ef}=-(1/12+P_{ee}/6)\delta_{ef}+\tfrac14J_{ef}J_{fe}.
                                                               \tag{6}
\]
In particular \(Bv(0)=-v(1)\), \(M_{\rm sum}v(0)=v(1)\).
At the slab's upper end these are \(v(M-1)\), \(v(M-1)\).
Both endpoints and the all-link Haar term are included.

### 2. Definition of the plane rows and all cubic terms

For a finitely supported depth sequence \(\alpha_n\), use the
formal tangentially constant normal external field
\(u_\alpha(n,z)=\alpha_n t^a\). Plane quadratic forms mean
per-tangential-volume limits, or their Fourier integrals below.
The ambient tensors in (1) are the specific Wilson extensions
of L280, so this notation does not assert \(u_\alpha\in\ker B^*\).

Every plaquette curl of \(u_\alpha\) is zero: the two normal
slots have the same depth and coefficient, and its tangential
slots vanish. This includes plaquettes adjacent to either end.
Consequently L287's external-curl polynomial
\(\mathsf A(u_\alpha;x)\) vanishes exactly. This is an identity
for this test, not use of L287's \(o(N^2)\) error at order \(N\).
By the exact signed-slot calculation L289(4)–(5),
\[
 D V(x)[u_\alpha]=\sum_n\alpha_n\mathcal B_n(x),\qquad
 \mathcal B_n(x)=\sum_{z,j}
 (Cx)_{0j}(n,z)\mathbin{\cdot}
          [t^a,\mathsf a x_j(n,z)].                          \tag{7}
\]
The sum over \(j=1,2,3\) includes every normal plaquette; other
plaquettes do not depend on this external field. All colors and
both Gaussian crossing pairings are retained. L287(13) therefore
identifies the cubic part of the plane kernel as
\(\frac12\operatorname{Cov}(\mathcal B_n,\mathcal B_m)\) per
tangential volume, exactly \(E/4\).

For the quartic part, the two normal external slots of a plaquette
are at the same depth. Its quadratic coefficient is consequently
diagonal in depth. It is \(-\sum_j c(g_{n,j})\), with precisely
L283(13)'s complete raw-edge covariance expression \(c(g)\).
This follows also from
\(\mathbb E[W(x+r u)]=\mathbb E W(x)+r^2 u^*A u/4+O(r^4)\).
Pinned tangential slots use zero covariance at the face.

The density plane kernel is the diagonal Haar/\(P\) term plus
\(\frac14\int J_{00}(p;n,m)J_{00}(p;m,n)\,dp/(2\pi)^3\).
Together these define a symmetric plane kernel \(S_H(n,m)\).
The Fourier convention in this formula is the real normal-edge
one; the two tangential displacements have opposite signs.
Define \(S_\infty(n-m)\) on all integer depths by the same full
Wilson contractions and full-line scalar kernels.

Write \(s_H(p;n,m)\), \(s_\infty(p;n-m)\) for their internal-loop
integrands, including the quartic diagonal term. Set
\[
 b_H(n)=\int\sum_{m\geq0}s_H(p;n,m)\,\frac{dp}{(2\pi)^3},
 \qquad
 b_\infty=\int\sum_{m\in\mathbb Z}
          s_\infty(p;n-m)\,\frac{dp}{(2\pi)^3}.              \tag{8}
\]
The estimates in section 4 prove absolute convergence of each row
and of their depth-summed difference. Formula (8), rather than a
formal infinite constant-vector pairing, defines the test.

### 3. Finite-slab determinant identity and its harmonic mode

This step uses the exact Wilson phase and its local positive density.
It does not infer a surface cancellation from a generic Ward identity.
Let \(Q_0\) span the three orthonormal constant normal vectors in
the finite slab, and let \(Q_1\) span their orthogonal complement
in \(\mathcal H=\ker B^*\). The kernel of \(C\) is
\({\rm im}\,B\oplus{\rm im}\,Q_0\). Indeed at a nonzero tangential
momentum choose a nonzero tangential difference and solve \(Cx=0\)
for a vertex potential from that tangential component; its boundary
values are zero and the normal curl equation recovers the normal
component. At zero tangential momentum the tangential components
are constant in depth and hence zero at both ends. The normal
sequence is a Dirichlet gradient plus its constant mean.

Put \(v_r=r u\), where \(u\) is unit color on all normal edges.
Its links form an exactly flat Wilson configuration. The vertex
rotations \(g_r(n,z)=\exp(nr t^a)\) send it to identity. They
are constant on each end plane and hence preserve every pinned
tangential link and product Haar measure. They are not members
of the boundary-fixed gauge group; they are a measure-preserving
finite-dimensional change of variables and conjugate that group
to itself.

Let \(F_r\) be the derivative, in log-link coordinates at \(v_r\),
of this fixed change of variables. Let \(\mathcal D(v_r)\) be
L280's infinitesimal gauge-action matrix. Then
\[
 F_r\mathcal D(v_r)=B R_r,\qquad \det R_r=1,                \tag{9}
\]
where \(R_r\) is the interior vertex adjoint rotation. Haar
invariance gives
\(\det F_r=\prod_e j((v_r)_e)\), positive near zero, where
\(j(v)=(\sin(|v|/2)/(|v|/2))^2\).

L280's full density proof applies to this finite relative graph:
\[
 \rho(v_r)/\rho_0
 =\det F_r\det(\Delta^{-1}B^*\mathcal D(v_r))
 =\det_{\mathcal H}(Q^*F_r Q),\quad Q=[Q_1,Q_0].           \tag{10}
\]
For the second equality, compute the determinant of
\(F_r[Q,\mathcal D(v_r)]\) using (9) in the orthogonal
decomposition \(\mathcal H\oplus{\rm im}B\); the
\(\sqrt{\det\Delta}\) factors cancel. Thus (10) includes Haar
and both gauge-coordinate determinant terms.

Changing the constant color vector in \(v_r\) still gives a flat
configuration. Hence \(F_r Q_0\in\ker C\), and
\[
 Q^*F_r Q=
 \begin{pmatrix} A_r&0\\ *&Z_r\end{pmatrix}.
 \qquad
 H_r:=Q_1^*\mathcal S''(v_r)Q_1=A_r^*H_0 A_r.             \tag{11}
\]
The Hessian identity follows from exact gauge invariance of the
Wilson phase, its zero gradient at a flat configuration, and
\(\mathcal S''(0)=C^*C\). The positive operator \(H_0\) is restricted to
\({\rm im}Q_1\). Thus
\[
 \frac{\rho(v_r)}{\rho_0}
       \sqrt{\frac{\det H_0}{\det H_r}}=\det Z_r.           \tag{12}
\]

For clarity the remaining block is computed, not discarded.
On normal edge \(n\), \(F_r\) sends a constant color increment
\(w\) to
\(\int_n^{n+1}\exp(\tau r\,{\rm ad}\,t^a)w\,d\tau\).
Projection onto the constant normal mode averages these \(M\)
increments, so
\[
 Z_r=\frac1M\int_0^M\exp(\tau r\,{\rm ad}\,t^a)\,d\tau,
 \quad
 \det Z_r=\left(\frac{\sin(Mr/2)}{Mr/2}\right)^2.
                                                               \tag{13}
\]
Its logarithm has quadratic coefficient \(-M^2/12\).

The quadratic coefficient on the left logarithm of (12) is
exactly \(u^* S_{M,\ell}u\), using the inverse on \(Q_1\).
In fact
\[
 H_r=H_0+r\,T[u,\cdot,\cdot]
                 +\tfrac12r^2U[u,u,\cdot,\cdot]+O(r^3),
 \quad
 \log\rho(v_r)/\rho_0=r^2 u^*D u+O(r^3),
 \]
and the determinant expansion gives the two terms
\(-u^*A u/4+u^*E u/4\) with exactly (1)'s factors. Therefore
\[
 \frac{u^*S_{M,\ell}u}{\ell^3}
                         =-\frac{M^2}{12\ell^3}.           \tag{14}
\]
No fluctuating harmonic inverse has been used.

An elementary normalization check of this finite identity uses one
normal interval (the identity itself does not require even thickness).
There are then no interior gauge vertices. At \(p\neq0\), only the
normal field fluctuates, with covariance \(1/s\). L283(13) gives
\(\sum_jc(g)=-1/12\), since
\(\sum_j(1-\cos p_j)=s/2\). Thus the quartic term is \(+1/12\),
the full density is \(-1/12\), and the cubic jet is zero:
with just the two normal slots its alternating color contraction
vanishes. At zero tangential momentum the fluctuation was removed,
leaving just \(-1/12\), exactly (14) at \(M=1\).

All maps commute with tangential translations. On every nonzero
real Fourier sector (pairing conjugate momenta when necessary)
there is no \(Q_0\) block, so (12)'s determinant ratio is one
on that sector. Its complete quadratic coefficient is zero.
At fixed \(M\), the other integrands have at worst \(C_M/s\)
singularity, which is integrable in three tangential dimensions.
The punctured Fourier Riemann sums therefore converge: the
contribution from \(|p|<\epsilon\) is bounded by \(C_M\epsilon\)
uniformly along those sums, by counting momentum shells.
The zero sector in (14) disappears as \(\ell\to\infty\).
Thus the continuous-momentum slab plane rows satisfy
\[
                  \sum_{n=0}^{M-1} b_M(n)=0.               \tag{15}
\]
This specifies the normal-field regulator. Reversing the two
volume limits is not justified; (14) exhibits the harmonic term
that would obstruct such an interchange.

### 4. Complete half-space row and depth bounds

Here constants are uniform for \(0<s\leq12\); \(\kappa\) is
comparable to \(|p|\) near zero and bounded above on the Brillouin
zone. Fixed shifts of at most two lattice units in estimates are
absorbed into constants. Use a fixed \(c>0\), decreased when
needed. Applying at most two normal differences to (4) and to
\(-\partial_s(4)\), or multiplying by tangential \(d_j\), gives
the following bounds. The second column is the full-line kernel
bound; the third is the half-space minus full-line kernel bound:

| kernel | full-line bound | image difference bound |
| --- | --- | --- |
| any component of \(G\), also averaged tangential components | \(C\kappa^{-1}e^{-c\kappa|n-m|}\) | \(C\kappa^{-1}e^{-c\kappa(n+m)}\) |
| \(J_{00}\) | \(Ce^{-c\kappa|n-m|}\) | \(Ce^{-c\kappa(n+m)}\) |
| \(P_{00}\) | \(\delta_{nm}+C\kappa e^{-c\kappa|n-m|}\) | \(C\kappa e^{-c\kappa(n+m)}\) |
| \(H_{jk}=(CGC^*)_{0j,0k}\) | \(C\delta_{nm}+C\kappa e^{-c\kappa|n-m|}\) | \(C\kappa e^{-c\kappa(n+m)}\) |
| \(F_{jk}=(CG\mathsf a^*)_{0j,k}\) | \(Ce^{-c\kappa|n-m|}\) | \(Ce^{-c\kappa(n+m)}\) |

Here are identities and difference estimates that verify the table,
including its contact terms. In tangential midpoint phases,
\[
 G_{ij}=\delta_{ij}R_D-d_i d_j R_D^2,\quad
 G_{00}=sR_N^2,\quad
 G_{0j}=i d_j\delta R_D^2,
 \]
\[
 J_{00}=-2\mathsf a R_D\delta^*,\quad
 P_{00}=\delta R_D\delta^*=I-sR_N,
 \]
\[
 H_{jk}=\delta_{jk}I+(d_jd_k-s\delta_{jk})R_N,\qquad
 F_{jk}=\delta_{jk}\delta R_D\mathsf a^*.                  \tag{16}
\]
These signs use \(B_0=-\delta\), \(B_j=-i d_j\) and
\((Cx)_{0j}=\delta x_j-i d_jx_0\). Returning to raw edge
positions restores the unit midpoint phases in (5), so no phase
is discarded in a contraction. The last two identities use
\(CG=CL^{-1}\); no transverse part is omitted.
The average at \(n=0\) is \(x_j(1)/2\), as required.

For explicit control of the differentiated kernels,
\(\partial_s=(2\sinh\kappa)^{-1}\partial_\kappa\).
An undifferenced \(R_D^2\) image is bounded by
\(C\kappa^{-3}(1+\kappa l)e^{-\kappa l}\), \(l=n+m\);
each normal difference reduces this power by one. Factors
\(|d_j|\leq C\kappa\) do the same. Polynomial factors
in \(\kappa l\) are absorbed by reducing \(c\). The same bounds
hold on the full line away from the cusp. At the cusp the exact
resolvent recurrence gives the displayed contact term; (16) shows
there is no extra boundary contact term. This proves the table
directly from (3)–(4).

For the density row, the Haar difference is zero, the \(P\)
diagonal image is \(O(\kappa e^{-c\kappa n})\), and the
\(J_{00}J_{00}\) difference is bounded using the table and
\(\sum_{m\geq0}e^{-c\kappa m}\leq C/\kappa\).
The missing full-line rows \(m<0\) have the same bound. For the
quartic row, the finitely many raw covariances in L283(13)
give \(C\kappa^{-1}e^{-c\kappa n}\).

For the cubic row, apply both Gaussian crossing contractions
to (7). Its kernel is a fixed finite sum, with the exact color
coefficients, of products \(H_{jk}(n,m)\,
(\mathsf a G\mathsf a^*)_{jk}(n,m)\) and products of two
\(F\) kernels with the corresponding transpose/phase.
The table bounds its bulk absolute value by
\[
 C\{\kappa^{-1}\delta_{nm}
                         +e^{-c\kappa|n-m|}\}.             \tag{17}
\]
The difference on \(n,m\geq0\) is bounded by
\[
 C\{\kappa^{-1}\delta_{nm}e^{-c\kappa n}
                              +e^{-c\kappa(n+m)}\}.        \tag{18}
\]
These estimates use all cross terms, including different
plaquette directions. Summing (18) and the omitted \(m<0\)
tail of (17) retains every second-vertex depth.

Consequently, if
\(\beta_H(p,n)=\sum_{m\geq0}s_H(p;n,m)\) and
\(\beta_\infty(p)=\sum_{m\in\mathbb Z}s_\infty(p;n-m)\),
then
\[
 |\beta_\infty(p)|\leq C/\kappa,\qquad
 |\beta_H(p,n)-\beta_\infty(p)|
                  \leq C\kappa^{-1}e^{-c\kappa n},\qquad
 \sum_{n\geq0}|\beta_H(p,n)-\beta_\infty(p)|
                  \leq C/\kappa^2.                        \tag{19}
\]
The bounds hold separately for the three selected groups.
They justify Fubini for the defect and all row definitions.
Integration in three tangential dimensions gives the depth
bound in (2), since
\(\int_0^1 r e^{-crn}\,dr\leq C/(1+n)^2\).
They also remove a tangential infrared cutoff with error
\(O(\epsilon)\) in the entire surface sum. This is complete
depth control, not a fixed-depth preview.

### 5. Passage from two slab faces to one half-space face

For completeness, the growing normal regulator in (15) is now
controlled. Its scalar kernels are the convergent image sums
\[
 R_{D,M}(n,m)=\sum_{j\in\mathbb Z}
     [r_s(n-m+2jM)-r_s(n+m+2jM)],
 \]
\[
 R_{N,M}(n,m)=\sum_{j\in\mathbb Z}
     [r_s(n-m+2jM)+r_s(n+m+1+2jM)].                       \tag{20}
\]
They satisfy the same recurrences and both endpoint rows;
uniqueness of the positive-\(s\) finite inverse verifies them.
All derivative identities (16) continue to hold.

For \(\kappa M\geq1\), the geometric image denominator
\(1-e^{-2\kappa M}\) is bounded away from zero. On rows
\(0\leq n<M/2\), use (20) in the same products as section 4.
Images from the upper end and omitted half-space second vertices
have distance at least \(M-n\). Differentiating (20) can add
polynomials in \(\kappa M\), absorbed by a smaller exponential
constant. Summing over the second-vertex depth gives
\[
 |\beta_M(p,n)-\beta_H(p,n)|
              \leq C\kappa^{-1}e^{-c\kappa(M-n)}.
                                                               \tag{21}
\]
For the diagonal quartic term this follows directly from its
finite covariance list. For density products and cubic products,
each difference has at least one upper-end image, or an omitted
second vertex; summing its exponential times the other kernel
gives the same \(1/\kappa\) factor as (18)–(19).
Normal reflection maps the upper half to the lower half; both
external normal signs reverse, so the quadratic row is unchanged.
Thus (21), and the omitted tail in (19), imply
\[
 \left|\sum_{n<M}(\beta_M(p,n)-\beta_\infty(p))
       -2\sum_{n\geq0}(\beta_H(p,n)-\beta_\infty(p))\right|
       \leq C\kappa^{-2}e^{-c'\kappa M}
                  \quad(\kappa M\geq1).                  \tag{22}
\]

There is no uniform geometric denominator at \(\kappa M<1\).
Treat that region separately. The finite interval Green formula
\[
 R_{D,M}(n,m)=
 \frac{\sinh(\kappa n_<)\sinh(\kappa(M-n_>))}
      {\sinh\kappa\,\sinh(\kappa M)}
 \]
gives \(|R_D|\leq CM\), \(|\delta R_D|\leq C\).
The zero normal eigenvector and the remaining cosine modes give
\(|R_N|\leq C(M+(Ms)^{-1})\). Summing two \(R_D\) kernels
gives \(|R_D^2|\leq CM^3\) and
\(|\delta R_D^2|\leq CM^2\). Therefore (16) gives
\[
 |G_{ij}|\leq CM\ (i,j\hbox{ tangential}),\quad
 |G_{\mu\nu}|\leq C(M+(Ms)^{-1}),\quad |J_{00}|+|F|\leq C,
 \quad |H_{jk}|\leq C(\delta_{nm}+M^{-1}).                 \tag{23}
\]
For \(G_{00}=sR_N^2\), its nonconstant cosine-mode contribution
is bounded by \(CsM^3\leq CM\); the constant-mode contribution
is exactly \(1/(Ms)\). Also \(0\leq P\leq I\).
The density and cubic absolute sums over both depths are
\(O(M^2)\): for the cubic use (23), giving
\(C(M\delta_{nm}+1)\) per pair. The quartic absolute sum
is \(O(M^2+s^{-1})\). Hence
\[
 \sum_{n<M}|\beta_M(p,n)|\leq C(M^2+s^{-1})
                            \quad(\kappa M<1).             \tag{24}
\]
This retains the small-momentum normal mode rather than bounding
it by a false uniform gap.

Integrating (22) in three dimensions gives \(O(M^{-1})\).
The low-momentum region has volume \(O(M^{-3})\);
(24), \(M|\beta_\infty|\leq CM/\kappa\), and the last
bound in (19) each have integral \(O(M^{-1})\) there.
We have proved the regulated surface relation
\[
 \sum_{n<M} b_M(n)-M b_\infty
     =2\sum_{n\geq0}(b_H(n)-b_\infty)+O(M^{-1}).            \tag{25}
\]
This error concerns this frozen slab test only.

Finally L282, L283 and L289 compute the full-lattice row sums
in exactly the present counting/Wilson normalization:
\[
 b_\infty=d_*-\tfrac14a_*+\tfrac14(24I_1)
          =\tfrac14-2Z_0+4I_1=0.
 \]
Here \(d_*=-1/8-I_1\), \(a_*=8Z_0-3/2+4I_1\), and
L289(16) proves \(I_1=Z_0/2-1/16\), with its singular-point
integration by parts justified. Use (15) in (25) and let
\(M\to\infty\). This gives the zero in (2).

The missing full-box conclusions listed after (2) are not
established by this argument. In particular (25) is not a
replacement for an actual L282 source-field boundary expansion.

### 6. Separate conceptual audit (2026-10-26)

**Verdict and scope.** The separate audit accepts (2), including
absolute depth summability and the frozen-test error (25), conditional
on the recorded local inputs. It rechecks the concrete finite matrices
and limiting argument, not a general boundary gauge identity or an
isolated-minimum Laplace theorem on a space with harmonic modes.
The existing derivation above is retained. No load-bearing error was
found; the details below make explicit the complete crossings and
uniformity checks used in accepting it. This is reproduction and
verification of this notebook result, not a new asymptotic theorem.

**Domains, covariance and local identification.** For the stipulated
even M>=2, with counting measure delta has M rows and M-1 columns.
Thus delta delta* has
endpoint diagonal one and interior diagonal two; delta* delta has
diagonal two throughout its interior-vertex domain. This verifies
both endpoint recurrences in (4) and (20), including the shift +1
in the normal image. The constant normal vector belongs to ker delta*,
whereas no Dirichlet vertex zero mode exists. At nonzero tangential
momentum the scalar inverses are positive and the identities
delta R_D=R_N delta and delta R_D delta*=I-s R_N follow by
multiplication. Differentiating the latter gives
delta R_D^2 delta*=R_N-s R_N^2, which verifies G_00=s R_N^2.
Using B=(-delta,-i d) and C_0j=(-i d_j,delta), CB=0 gives
CG=CL^-1 and then exactly H and F in (16), with no extra endpoint
contact term. This also checks the mixed component's sign.

The half-space has no square-summable harmonic normal constant.
Its Gaussian finite marginals use the locally integrable spectral
inverse, not a bounded inverse on all of l2. For local cube comparison,
L283(7)'s uniform entry error tends to zero after polynomial degree
tends to infinity; at fixed degree every path near the retained face
eventually agrees with the half-space path. L282(11)–(13) supply the
row/column control for J and its product in D, with the same endpoint
rows. L288(3) supplies the corresponding internal-curl approximation.
On the half-space the sine/cosine spectral measure has bounded mode
amplitudes and integrable lambda^-1 in four dimensions, so these same
polynomials have the stated local spectral limits. None of these
local-limit arguments is used to interchange a growing depth sum.

**Full determinant and the omitted Gaussian mode.** The slab's
boundary-fixed gauge action is free: fixing the gauge at an end and
propagating along links forces a stabilizer to be identity everywhere.
Flat linear fields have exactly the decomposition im B plus Q_0
given in section 3; in particular tangential torus holonomies cannot
survive the pinned tangential end links. This makes H_0 on Q_1
positive. A boundary-constant rotation conjugates the fixed-end group
to itself, although it is not a member of that group. Its derivative
intertwines gauge directions as in (9), with an adjoint rotation of
determinant one at every interior vertex.

In the output basis [Q,B Delta^-1/2], multiplication of
[Q,mathcal D(v_r)] by F_r has determinant
det(Q*F_r Q) sqrt(det Delta). Before multiplication its determinant
is sqrt(det Delta) det(Delta^-1 B*mathcal D(v_r)). Haar invariance
gives det F_r=product j((v_r)_e). These equalities prove (10) with
all density factors, including the gauge-coordinate quadratic terms.
All determinants have their positive orientation in a neighborhood
of r=0; no assertion uniform in M about that neighborhood is needed
to compute its derivative at zero.

Varying a spatially constant normal color gives a family of flat
fields, so F_r Q_0 lies in ker C. Projection on Q_1 is therefore
zero on that block. The exact Wilson Hessian at a flat field is
F_r* C*C F_r because the phase gradient vanishes. This proves both
the triangular block and the restricted congruence (11). Its
determinant cancels precisely the A_r factor of the full density,
leaving det Z_r rather than one.

For a normalized Q_0 increment, the factors sqrt(M ell^3) in input
and projection cancel, leaving the average of the M edge derivatives.
The parallel color has eigenvalue one. On the perpendicular color
plane, the average of the rotation through angle tau r has determinant
(sin(Mr/2)/(Mr/2))^2. Thus log det Z_r=-M^2 r^2/12+O_M(r^4).
There is no extra factor three or ell^3: all three colors already
enter this one harmonic block. Expanding -1/2 log det H_r gives
-Tr(G U[u,u])/4+Tr(G T[u] G T[u])/4 at order r^2; adding
log rho gives exactly u* S u. This verifies (14) with the covariance
restricted to Q_1 and with its harmonic density contribution retained.
On a nonzero real tangential Fourier sector Q_0 is absent, so the
same determinant ratio is one. At zero momentum its finite remainder
is divided by ell^3 and vanishes only in the stipulated first limit.

**Complete cubic kernel and row estimates.** For any depth-dependent
normal probe constant tangentially, the two normal slots on each
plaquette have opposite equal values, even at either end. Thus its
curl is zero exactly, and L289(4)–(5) gives (7) without discarding
L287's error. Each B_n is centered by the antisymmetric color bracket.
Its two Gaussian crossings have color factors +2 and -2. To see
explicitly what is bounded, put

\[
 K_{jk}=\bigl(\mathsf a G_{jk}\mathsf a^*\bigr),\qquad
 f=\delta R_D\mathsf a^*,\qquad F_{jk}=\delta_{jk}f.
\]

In the midpoint convention of (16) these matrices are real and even
under p to -p. The cubic integrand E/4 in the plane kernel is exactly

\[
 \sum_{j,k=1}^3 H_{jk}(p;n,m)K_{jk}(p;n,m)
                 -3 f(p;n,m)f(p;m,n).                       \tag{26}
\]

Indeed Cov(B_n,B_m) has twice this integrand, and L287(13)
multiplies that covariance by 1/2 in E/4. The first product includes
all different-direction terms. The second uses the reversed depth
indices, not an absolute square. Tangential midpoint phases cancel
between the paired displacements in the plane sum; they are not
deleted from an individual raw-edge covariance. In particular (26)
keeps both crossings and all second-vertex depths. The quartic term
is the entire L283(13) expression, with both external slots at the
same depth, and the density is (6), not its Haar part alone.

The derivative formula for R_D^2 in section 4, with each difference
or d_j supplying one power of kappa, bounds every entry of G by
C/kappa times its exponential. The exact formulas for P and H retain
their identity contact terms; F and J have no such term. Multiplying
these estimates in (26) gives (17). Subtracting a half-space product
from the full-line product puts an image factor in at least one slot.
The product of a contact term and an image G gives the first term
of (18); every other term is bounded by its second term. The same
reasoning applies to J_00(n,m)J_00(m,n). Summing all m>=0 costs at
most C/kappa; the missing full-line m<0 tail has the same cost and
the same decay in n. Local quartic covariances have that bound
directly. This proves (19) for each group before their signed sum.
It also justifies tangential Parseval and depth Fubini: the fixed-depth
factors have square-integrable tangential transforms, and the summed
absolute products have the integrable majorants stated in (19).

**Uniform passage through the two faces.** For kappa M>=1, the
geometric image denominator in (20) is bounded below. Every upper
image on a lower-half row, or every omitted second vertex m>=M,
has distance at least M-n up to the fixed cell shifts. In products
the additional convolution costs at most C/kappa; polynomial factors
from differentiating an image are absorbed in a smaller exponential.
Thus the contact, quartic, J-product and both cubic terms separately
satisfy (21). Reflection n to M-1-n reverses both external normal
signs and preserves the quadratic row, so summing lower-half errors
and the omitted half-space tail gives (22), including its factor two.

For kappa M<1, the Dirichlet formula gives |R_D|<=CM and
|delta R_D|<=C. Its M-1 intermediate vertices give
|R_D^2|<=CM^3 and |delta R_D^2|<=CM^2. The nonconstant normal
eigenvalues obey lambda_k>=4k^2/M^2, while each normalized mode
has squared amplitude at most 2/M. Hence the nonconstant part of
R_N is O(M); that of s R_N^2 is O(s M^3). The constant part
of the latter is exactly 1/(Ms), which must remain. Since sM^2
is bounded here, these estimates prove all G bounds in (23).
They also give |J|+|F|<=C and
|H_jk(n,m)|<=C(delta_nm+1/M); the averaged tangential K is O(M).
Consequently (26) is O(M delta_nm+1) per pair. Its double sum and
the complete density double sum are O(M^2). The local quartic list
has total absolute bound O(M^2+1/s), proving (24). This treats the
small-momentum normal mode without assigning it a fictitious gap.

Near zero kappa is comparable to |p|. With a fixed finite K covering
the momentum range, the integrated high-momentum error is bounded by
\(C\int_0^K e^{-crM}\,dr\leq C'/M\).
In the low region the three contributions in (24), M|beta_infinity|
and the full half-space defect are bounded after integration by,
respectively, C(M^2 M^-3+M^-1), CM M^-2 and C/M.
Thus (25) is uniform in the growing thickness. At fixed thickness
the singularity of the remaining tangential integrands is at worst
C_M/|p|^2; the nonzero grid shell sum below epsilon is O(C_M epsilon).
This proves the punctured Riemann-sum limit used in (15), while the
zero Fourier block is finite at fixed M and vanishes per area.
No reversed regulator order has been used.

Finally the imported bulk constants give
(-1/8-I_1)-(8Z_0-3/2+4I_1)/4+6I_1
=1/4-2Z_0+4I_1=0. L289(16)'s integration by parts has
O(epsilon^2) small-sphere flux and integrable four-dimensional
terms, so its identity is applicable in this convention. The
O((1+n)^-2) majorant, (15) and (25) now give the asserted zero
absolutely convergent face defect. Polarization is legitimate for
the resulting finite bilinear depth sum. Actual source traces,
tangential variation, other groups and full-box o(N) errors are
still outside this result; in particular the general external-curl
terms have not been estimated at that scale.

## Mathlib

Coverage of this full Wilson-specific signed half-space defect,
its quotient density and its slab regulator: **not checked**.
No absence assertion is made. The proof reuses the exact local
inputs L003, L280, L282, L283, L287, L288 and L289 and computes
the new boundary specialization explicitly. Gaussian pairing,
finite determinant expansion, polar decomposition and dominated
integration are used in their usual stated finite/spectral forms.
No external boundary-renormalization or BRST theorem is imported.
The pre-existing literature assessment found no inspected theorem
computing this selected defect; this explains the specialization
and supplies no certified novelty claim.
