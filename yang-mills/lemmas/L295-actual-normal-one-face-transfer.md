# L295 — Actual normal-source transfer on one face away from edges

## Hypotheses

Use L280's SU(2) relative cube, counting measure, even N>=2,
a=8/N, boundary-fixed gauges, pinned boundary-contained links and
every variable normal endpoint. Retain its own-slice ambient Wilson
jets, full density and real source domain. The exact product bump,
separated modes, positive weights b_(k,a), both reflected sources
and their normal components are precisely those of L294. Its source
estimates are inputs; L294's separate critical audit accepts them under
these same hypotheses.

Fix the face x_1=-4. Write d=x_1+4 and y=(x_2,x_3,t). Fix real
smooth chi(y), eta(d), with eta=1 near d=0, whose product is supported
in a collar separated by a positive physical distance from every
other face and from the edges. They are fixed as N varies. On the
normal edge (n,z), whose center has d=(n+1/2)a and y=-4+a z, set

\[
 u_{\epsilon,k,a}(n,z)=\chi(y)\eta(d)
                    (X_{\epsilon,k,a})_1(d-4,y),\qquad
 \epsilon\in\{+,-\}.                                      \tag{1}
\]

It is zero on all other components. Extend these scalar amplitudes
by zero to all positive half-space normal edges outside their cube
support, and evenly to negative normal indices by
u^ev(-n-1,z)=u(n,z). This is the midpoint even extension stipulated
by the transfer target, not a different bulk subtraction.

For one fixed unit color, let S_N, S_H and S_inf be the normal-normal
blocks of the complete operators in L292/L293:

\[
 S=D-\tfrac14 A+\tfrac14 E,\quad
 A_{ij}=\sum_{kl}U_{ijkl}G_{kl},\quad
 E_{il}=\sum_{jkmn}T_{ijk}T_{lmn}G_{jm}G_{kn}.              \tag{2}
\]

The half-space and full-lattice operators use the same raw Wilson
slots, density, colors and both Gaussian crossings. Their construction
is L292's relative massless construction. In any auxiliary slab,
exclude exactly its three constant normal harmonic modes and take
tangential volume before thickness, as in L292/L293. The original
cube inverse is unchanged. The proof below identifies the heat
representation with those kernels, without a new regulator choice.

For ordered signs define exactly the finite-external-sum defect

\[
 F_{N,k}^{\epsilon,\epsilon'}=
 \sum_{e,f\in E_N^\perp}u_\epsilon(e)(S_N)_{ef}u_{\epsilon'}(f)
 -\sum_{e\in E_N^\perp}\sum_{f\in E_\infty^\perp}
        u_\epsilon(e)(S_{\inf})_{ef}u^{ev}_{\epsilon'}(f),
 \qquad
 \mathcal F_N=3a^2\sum_{k\in\mathcal K_N}b_{k,a}
          (F_{N,k}^{+,-}+F_{N,k}^{-,+}).                    \tag{3}
\]

The subscript k,a on each source in the first formula is suppressed.
The bulk second vertex ranges over the full lattice, including the
negative-depth vertices. No equality to the full original coefficient
is asserted by this component projection and localization.

## Conclusion

With A_(k,a) from L294(3), constants depending on the fixed cutoffs
and bump, but not N or k, satisfy

\[
 |3a^2(F_{N,k}^{+,-}+F_{N,k}^{-,+})|
                 \le C N A_{k,a}^2,\qquad
                         \boxed{\mathcal F_N=o(N)}.        \tag{4}
\]

The proof gives a complete half-space source bound and vanishing
surface limit. The finite-cube-to-half-space difference, after the
3a^2 normalization and complete external-mode sum, is O(log(eN)),
hence o(N). No external-curl term is discarded.

This is a local partial result toward the reflected coefficient under
the ready EXPLORE assessment, not a certified originality claim.
The separate conceptual audit in section 6 accepts this proof and its
use of the audited L294 estimates under the recorded inputs. Other
components, coefficient groups, faces combined with their edge/corner
strata, a full-box remainder, a uniform higher perturbative remainder,
the interacting continuum construction and positive mass remain open.
No complete Yang--Mills candidate or uniform interacting lower bound
is claimed.

## Proof

### 1. Heat estimates with the actual relative boundary rows

We first prove the kernel comparison needed below. Distances in this
section are unscaled lattice distances; fixed raw-slot shifts change
constants only. All scalar vertex or one-form heat operators have
the exact tensor interval modes of L280(21). The scalar vertex
Laplacian is Delta=B*B, Dirichlet in every coordinate. A component
of L=C*C+BB* is midpoint Neumann in its own coordinate and vertex
Dirichlet in the other three. No all-zero mode occurs in either
cube operator.

Let h_tau(z), z in Z^4, be the full-lattice scalar heat kernel, with
Fourier multiplier exp(-tau lambda(p)) and
lambda(p)=4 sum_j sin^2(p_j/2). For any product of r forward or
backward coordinate differences, r=0,1,2, and any integer K>=0,

\[
 |\nabla^r h_\tau(z)|\le
 C_{r,K}(1+\tau)^{-(4+r)/2}
       (1+|z|/\sqrt{1+\tau})^{-K}.                        \tag{5}
\]

Here each specified difference, not a continuous derivative, is
meant. To verify (5), its multiplier is m_r(p)exp(-tau lambda(p)),
where m_r is a product of r factors e^(+/- ip_j)-1. On the torus
represented by [-pi,pi]^4, lambda is comparable to |p|^2 and
|partial^beta m_r|<=C_beta |p|^max(r-|beta|,0). For tau>=1,
Leibniz differentiation and Gaussian integration give

\[
 \int_{[-\pi,\pi]^4}
 |\partial^\alpha(m_r e^{-\tau\lambda})|\,dp
       \le C_\alpha\tau^{(|\alpha|-4-r)/2}.               \tag{6}
\]

For detail, each first derivative of lambda contributes O(|p|),
and higher derivatives are bounded. A term with l differentiated
lambda factors, h of them first derivatives, has
tau^l |p|^h and total differentiation order at least 2l-h.
Rescaling p by sqrt(tau) therefore costs at most tau to half that
order. The derivatives of m_r give the remaining r powers, or
a smaller power of tau if more than r derivatives strike it.
Away from a fixed small ball exponential decay absorbs every
polynomial factor. This proves (6). For tau<=1 the same integrals
are uniformly bounded. Fourier inversion gives the estimate without
the last factor in (5); integrating by parts K times in a coordinate
with maximal |z_j| gives that factor. Periodicity removes all boundary
terms. Combining the two bounds proves (5), including tau=0.

The one-dimensional image formulas at vertices 0,...,N are

\[
 h_{D,N}(\tau;i,j)=\sum_{v\in\mathbb Z}
   [h_\tau^{(1)}(i-j+2vN)-h_\tau^{(1)}(i+j+2vN)],
\]
\[
 h_{N,N}(\tau;i,j)=\sum_{v\in\mathbb Z}
   [h_\tau^{(1)}(i-j+2vN)+h_\tau^{(1)}(i+j+1+2vN)] .       \tag{7}
\]

The second formula has 0<=i,j<N and is on normal-edge midpoints.
The first has 1<=i,j<N and zero boundary values. Reflection gives
endpoint diagonal one for the midpoint Neumann Laplacian and
diagonal two for the interior vertex Laplacian. The image sums
satisfy these heat equations and the identity initial matrix.
Uniqueness of the finite matrix heat equation verifies (7).
They also follow by the sine/cosine diagonalization in L280.
Taking products gives the four-dimensional heat kernels. The
half-space kernels retain only the direct and lower-face images
in coordinate 1 and have no images in the other coordinates.
All sums and differences at positive finite heat time converge
absolutely by (5), with K>4. The initial kernels are finite stencils.

Let Omega_N contain the support of (1) and all the finitely many
edge/plaquette slots adjacent to it. For all sufficiently large N,
these slots stay at least cN from each face other than x_1=-4.
Here c>0 depends on the fixed cutoffs. A pinned tangential slot
on x_1=-4 is zero in both domains. For two surviving slots in
Omega_N, every cube image omitted from the half-space formula
has displacement at least cN, and the image indexed by v in Z^4
has displacement at least c' N(1+|v|), except for a fixed finite
set with the same cN lower bound. Indeed each changed reflection
or nonzero period crosses one of the distant faces; the two
retained lower-face images are the only exceptions.

Consequently for 0<=tau<=N^2, any r differences at the two
endpoints of the heat kernels obey

\[
 |\nabla^r(h_{\tau,N}-h_{\tau,H})(e,f)|
 \le C_K(1+\tau)^{-(4+r)/2}
                (\sqrt{1+\tau}/N)^K .                    \tag{8}
\]

Choose K>4 to sum the omitted images. Endpoint differences in
(7) merely replace a scalar heat kernel by the corresponding
forward/backward differences with reflection signs and bounded
shifts; at most 2^r such terms occur. Formula (8) thus applies
also to the staggered vertex-to-edge and edge-to-plaquette maps,
not just to undifferentiated scalar entries.

For tau>=N^2, use the finite tensor modes instead of the image
sum. A normalized counting-measure mode has supremum at most
C N^-2; each endpoint difference contributes at most C|ell|/N,
and lambda_ell>=4|ell|^2/N^2 with |ell|>=1. Summing the products
of the two mode values gives

\[
 |\nabla^r h_{\tau,N}(e,f)|
       \le C N^{-4-r}e^{-c\tau/N^2}.                      \tag{9}
\]

This follows by bounding sum_(ell!=0)|ell|^r exp(-4tau|ell|^2/N^2)
by C exp(-c tau/N^2) when tau/N^2>=1. Endpoint differences turn
sines into cosines or conversely with the exact factor
2 sin(pi ell_j/(2N)); the bound includes the two normal endpoints
and the own-coordinate cosine zero mode. The remaining three
positive indices exclude an all-zero edge mode. Half-space heat
kernels are two images of (5), so their large-time bound is
C tau^(-(4+r)/2). There is no false uniform gap for the half-space.

Suppressing color, the kernel representations are

\[
\begin{split}
 G&=\int_0^\infty e^{-\tau L}\,d\tau
       -\int_0^\infty\tau B e^{-\tau\Delta}B^*\,d\tau,\\
 F:=CG&=C\int_0^\infty e^{-\tau L}\,d\tau,\qquad
 H:=CGC^*=C\int_0^\infty e^{-\tau L}\,d\tau C^*,\\
 P&=\int_0^\infty B e^{-\tau\Delta}B^*\,d\tau,\qquad
 J=\int_0^\infty M_{\rm sum}e^{-\tau\Delta}B^*\,d\tau.
\end{split}                                               \tag{10}
\]

For the finite cube these are the spectral integral versions of
L280(16),(23), using CB=0. For the half-space and full lattice,
(5) makes every displayed matrix entry absolutely integrable.
In particular the second term for G has r=2 and a factor tau;
no unsandwiched massless inverse square is used. Tangential
Fourier transform and integration of the scalar heat kernels
give precisely L292's R_D,R_N and their differentiated kernels
at nonzero tangential momentum. Thus (10) agrees with the
already specified half-space construction. Values on a measure
zero momentum set add no mode, and the slab prescription remains
the one proved in L292/L293.

Integrating (8) and (9) proves, uniformly on Omega_N,

\[
 |G_N-G_H|\le C N^{-2},\quad
 |F_N-F_H|+|J_N-J_H|\le C N^{-3},\quad
 |H_N-H_H|+|P_N-P_H|\le C N^{-4}.                         \tag{11}
\]

Explicitly an integral with r differences and weight tau^w,
w=0 or 1, is O(N^(-2-r+2w)). On [0,N^2] use (8) with
K>2+r-2w; on [N^2,infinity) use (9) and the half-space power
bound. The only weight-one case is r=2, so every tail converges.
M_sum is an endpoint sum, adding finitely many shifts but no
derivative. This also checks both signs of the boundary rows of J.

Integrating (5) for the direct and reflected half-space images
gives the off-diagonal bounds

\[
 |G_H(e,f)|\le C(1+|e-f|)^{-2},\quad
 |F_H(e,f)|+|J_H(e,f)|\le C(1+|e-f|)^{-3},
\]
\[
 |H_H(e,f)|+|P_H(e,f)|\le C(1+|e-f|)^{-4}.                \tag{12}
\]

For example split the heat integral at (1+|e-f|)^2, using
K>2+r-2w on the first part. A reflected displacement is at least
the direct distance up to a fixed raw-slot shift. Contacts are
included in (12) at bounded distance. Since |e-f|<=C N on
Omega_N, (11) implies the same bounds for the cube entries there.
This establishes the rates, not just local entry convergence.

### 2. Comparing the complete cube and half-space contractions

For any two of the sources (1), L294 and the fixed cutoffs give

\[
 \|u\|_\infty+\|v\|_\infty\le C A_{k,a},\qquad
 \|Cu\|_\infty+\|Cv\|_\infty\le C a A_{k,a}.              \tag{13}
\]

Only normal/tangential plaquettes have a nonzero curl of these
normal fields. It is a tangential first difference, so (13)
follows from the physical C^1 bound, including the zero extension
across the compact cutoff support. We do not assert Cu=0.
There are O(N^4) supported anchors. For each such anchor the
sums of (1+distance)^(-2), (-3), (-4) over the other supported
anchors are respectively O(N^2), O(N), O(log(eN)); this follows
by the four-dimensional shell count O((1+j)^3).

The density has exactly the complete formula
D_ef=-(1/12+P_ee/6)delta_ef+J_ef J_fe/4 from L280(16).
The Haar terms cancel. Its diagonal difference is O(N^-4).
By (11),(12), its product difference is bounded by
C N^-3(1+|e-f|)^(-3). The density pairing difference is therefore
at most C A_(k,a)^2 N^2. No determinant contribution is omitted.

The ambient Wilson quartic tensor is a sum of fixed four-slot
plaquette tensors. Two external fields and one covariance occur
in A. Each covariance difference is O(N^-2) by (11), all slots
are in Omega_N, and the number of plaquettes is O(N^4). Its
pairing difference is at most C A_(k,a)^2 N^2 as well.

For the cubic term use the exact, centered polynomials of L287:

\[
 DV(x)[u]=\mathsf A(u;x)+\mathsf B(u;x),\quad
 \mathsf A=\sum_p(Cu)_p\cdot\zeta_p(x),\quad
 \mathsf B=\sum_p(Cx)_p\cdot D\zeta_p(x)[u],
 \quad u^*Ev=2\mathbb E[DV(x)[u]DV(x)[v]].                 \tag{14}
\]

Both Gaussian crossings, all raw signed slots and colors are retained.
At each pair of action plaquettes, the AA products have type GG;
AB and BA have type GF or FG; BB has types HG, GH or FF. This
is the finite exact monomial expansion in L287/L293, not a selection
of diagrams. Each vertex with A carries an external factor bounded
by C a A_(k,a); a vertex with B carries C A_(k,a).

Put R_s=(1+distance)^(-s). Subtracting the cube and half-space
products, (11),(12) give the following bounds before external factors:

\[
\begin{array}{c|c|c}
 \text{type}&\text{difference at a pair}&\text{sum per first anchor}\\
 GG&C N^{-2}R_2&C\\
 GF,FG&C(N^{-2}R_3+N^{-3}R_2)&C N^{-1}\\
 HG,GH&C(N^{-4}R_2+N^{-2}R_4)&C N^{-2}\log(eN)\\
 FF&C N^{-3}R_3&C N^{-2}.
\end{array}                                                \tag{15}
\]

The identity ab-cd=(a-c)b+c(b-d) proves these bounds using the
individual kernel bounds for both domains; it includes the
two-difference product without omitting it. Multiplying the first
row by a^2 A^2, the second by a A^2, the other rows by A^2,
and then by O(N^4) anchors, with a=8/N, gives

\[
 |\langle u,(S_N-S_H)v\rangle|
                  \le C A_{k,a}^2 N^2\log(eN).             \tag{16}
\]

Every action plaquette with a nonzero coefficient in (14) lies
within the fixed stencil enlargement of the external support.
There is consequently no unsummed remote action vertex. Internal
propagation over the full domain is contained in the exact kernels
in (11), not truncated. Pinned slots are zero in both domains.
The finitely many coarse even N not covered by the separation
argument can be included by increasing C: their matrices and the
finite supported half-space kernels have finite entries, and the
source supremum bound is uniform after division by A_(k,a).

### 3. An absolute half-space defect kernel and its depth tail

Tangential Fourier momentum q is represented in [-pi,pi]^3.
Let S_H(q;n,m) and S_inf(q;n-m) be the exact normal-block kernels
from L293. A normal external field at depth n occurs only in
normal/tangential plaquettes at that same normal depth; its two
normal slots differ tangentially. Fourier transformation therefore
leaves arbitrary depth profiles as scalar factors at the two
external vertices of the very same kernels. No normal-depth
constancy is required to define them.

Define

\[
 K(q;n,m)=S_H(q;n,m)-S_{\inf}(q;n-m)
                         -S_{\inf}(q;n+m+1),\quad n,m\ge0.
                                                               \tag{17}
\]

The last term is the contribution from bulk depth -m-1. It is
essential for the stipulated even extension. We claim

\[
 \sup_q\sum_{n,m\ge0}|K(q;n,m)|\le C,\qquad
 \tau_M:=\sup_q\sum_{\max(n,m)>M}|K(q;n,m)|\longrightarrow0.
                                                               \tag{18}
\]

Here is the complete justification from the inspected bounds in
L293, including the uniformity used now. Write r=kappa(p),
t=kappa(p+q), Q=sqrt(s(q)). The exact cubic products are
Q^2 GG, Q GF, Q FG, HG, GH and FF; the density has JJ plus its
local P term, and the quartic is local in depth. L293(11)--(13)
bound the sum of the absolute *subtracted* loop terms in (17)
by C(r^-2+t^-2). The missing second vertices are part of that
bound. The inequalities Q<=C(r+t), the kernel image table and
the finite raw trigonometric vertex coefficients hold on the
whole torus. Thus this bound holds for all q, even though only
continuity near zero was needed in L293's conclusion. Integrating
in p gives the first assertion of (18), since kappa^-2 is
integrable in three dimensions and its integral is translation
invariant. Triangle inequality is taken after forming each
subtracted product, as in L293; no individual infinite bulk
total is bounded this way.

For the second assertion remove radius-epsilon balls about
p=0 and p=-q. L293(15)'s proof gives a uniform C epsilon bound
on the integral of r^-2+t^-2 over their union, also for separated
or merging centers anywhere on the torus. On the complement,
r,t>=c epsilon. Each subtracted product contains an image, or
is a missing-row product with normal separation n+m+1. The
kernel table bounds its depth tail by a geometric exponential
times a polynomial in M, uniformly in p,q on this complement.
Local/contact terms have the same property, with depth diagonal
or a bounded-width contact strip. Hence

\[
 \tau_M\le C\epsilon+C_\epsilon(1+M)^2e^{-c_\epsilon M}.
                                                               \tag{19}
\]

First let M tend to infinity and then epsilon to zero. This proves
(18), retaining all external curls and deep second vertices.
It also shows that the massless kernel entries and all uses of
the subtracted depth sum below are well defined.

For q near zero L293 identifies

\[
 \sigma(q)=\sum_{n,m\ge0}K(q;n,m),\qquad
                         \sigma(q)\longrightarrow0.       \tag{20}
\]

For other q define sigma by the same absolutely convergent sum;
only its boundedness from (18) will be used. Thus no extension
of the slab limit assertion to new regulators is required.

### 4. Actual, depth-varying half-space sources

For a sampled source write
hat u_n(q)=sum_(z in Z^3)u(n,z)exp(-iq.z), and similarly for v.
There are finitely many nonzero samples in each depth row. The
fixed cutoffs and L294's C^3 estimate imply

\[
 |\widehat u_n(q)|+|\widehat v_n(q)|
       \le C A_{k,a}a^{-3}(1+|q|/a)^{-3}                  \tag{21}
\]

uniformly in every depth, with zero rows allowed. Indeed the
sample count is O(a^-3). For a tangential coordinate j, summation
by parts three times multiplies the Fourier sum by
(exp(iq_j)-1)^3. Each third difference is at most C a^3 A
by the threefold integral of the corresponding physical third
derivative, and there are O(a^-3) samples even after the fixed
number of shifts. Select j with |q_j|>=|q|/sqrt(3) and use
|exp(iq_j)-1|>=2|q_j|/pi. Combining with the sample-count bound
proves (21). Compact support strictly inside the tangential
faces justifies the smooth zero extension and the summation
by parts, including coarse meshes after a constant enlargement.

Define the half-space defect H_(N,k)^(epsilon,epsilon') by replacing
S_N by S_H in (3), keeping the same bulk term. The first support
is unchanged, and even extension identifies the negative depths
exactly. Fourier orthogonality therefore gives

\[
 H_{N,k}^{\epsilon,\epsilon'}=
 \int_{[-\pi,\pi]^3}\sum_{n,m\ge0}
   \widehat u_n(-q)K(q;n,m)\widehat v_m(q)
                           \frac{dq}{(2\pi)^3}.           \tag{22}
\]

One can first take the finite external sums and then use the
kernel Fourier integrals. Formula (18) justifies regrouping
into (22); it also permits constant-depth trace sequences in
the defect, even though those sequences are not square summable.
Equations (18),(21), with q=a p, give

\[
 |H_{N,k}^{\epsilon,\epsilon'}|\le C A_{k,a}^2 a^{-3}.     \tag{23}
\]

The finite integral of (1+|p|)^(-6) in three dimensions is the
reason three tangential derivatives suffice.

For fixed k, put t_(epsilon,a)(y)=chi(y)T_(epsilon,k,a)(y),
the actual interpolant trace in L294. Its sampled Fourier sum
obeys (21). For every fixed M, L294(18) and the sample count give

\[
 \max_{0\le n\le M}
 a^3|\widehat u_n(q)-\widehat t_{\epsilon,a}(q)|
          \le C A_{k,a}a^2(M+1/2)^2,                     \tag{24}
\]

once (M+1/2)a is in the eta=1 region. The same holds for v.
Both sides of the difference separately satisfy (21). Along a
fixed-k sequence, A_(k,a) is bounded, because gamma_(k,a)<=pi|k|/8.

Multiply (22) by a^3 and set q=a p. Restrict first to n,m<=M
and replace each Fourier source by its trace. For each fixed p,
the error tends to zero by (24). The absolute sum of the kernel
entries is at most C, and the error is dominated by
C A_(k,a)^2(1+|p|)^(-6), using (21) for both the actual and
trace amplitudes. Dominated convergence, extending the integrand
by zero outside [-pi/a,pi/a]^3, proves vanishing of this fixed-M
replacement error. This step does not require mixed derivatives
of order five or a rate for the Fourier transform of the error.

The omitted depth pairs, for both the actual and trace sources,
contribute at most C A_(k,a)^2 tau_M in the same normalization,
by (18),(21). After restoring these pairs the frozen-trace
expression is

\[
 a^3\int\widehat t_{\epsilon,a}(-q)\sigma(q)
                  \widehat t_{\epsilon',a}(q)\frac{dq}{(2\pi)^3}.
                                                               \tag{25}
\]

After q=a p it is dominated by C(1+|p|)^(-6), and its integrand
tends to zero because sigma(a p)->0. No limiting trace has to
be guessed: even a varying bounded family of these trace transforms
has a vanishing product with sigma(a p). Dominated convergence
and then M->infinity prove, for each ordered pair and fixed k,

\[
                         a^3 H_{N,k}^{\epsilon,\epsilon'}\to0.
                                                               \tag{26}
\]

This establishes tangential localization and the whole depth tail,
not merely a fixed-layer approximation or a frozen plane wave.

### 5. Cube transfer, both source orders and the complete mode sum

The bulk subtraction in F and H is identical: their first anchors
have exactly the same compact support, and their full second-vertex
even extensions agree. Consequently (16) says

\[
 |F_{N,k}^{\epsilon,\epsilon'}-H_{N,k}^{\epsilon,\epsilon'}|
              \le C A_{k,a}^2 N^2\log(eN).                \tag{27}
\]

Multiplication by 3a^2 makes this O(A_(k,a)^2 log(eN)). In
contrast (23) becomes O(N A_(k,a)^2), since a=8/N. Also
3a^2/N=3a^3/8. Thus (26),(27) give the fixed-mode vanishing
and the uniform N-scale bound in (4), retaining each order
separately before adding the two. The factor three is the
specified color normalization; neither order is silently doubled
or omitted.

Finally L294(6) supplies the actual summable majorant

\[
 b_{k,a}A_{k,a}^2\le C_f(1+|k|)^{15}e^{-|k|/4},\qquad
 \sup_N\sum_{|k|>R}b_{k,a}A_{k,a}^2\longrightarrow0.       \tag{28}
\]

The weights for each fixed k are bounded, also by L294(16)--(17).
On a finite external-mode set apply (26),(27); on its complement
apply (4)'s bound and (28). First N tends to infinity and then
R tends to infinity. This proves mathcal F_N/N->0. Summing
(27) directly using (28) gives the asserted O(log(eN)) complete
cube-to-half-space error. No growing external cutoff or unproved
uniform fixed-mode limit is used.

### Qualifications and verification

The actual N-scale and o(N) tests in the ready assessment are met
for exactly (3), conditionally on the recorded inputs. The short
and long heat-time estimates establish the finite-domain rate;
the exact subtracted kernel establishes the deep-layer tail;
L294 supplies the source envelopes and trace replacement. The
bulk second vertices, raw Wilson slots, complete density, both
crossings, external curls and the stipulated midpoint extension
are retained at each stage. This is not the stopped generic
gauge-identity or global absolute-norm argument.

No new external boundary theorem is imported or reproved. The heat
bounds were derived for the exact discrete tensor domains because
local convergence alone, and the inspected scalar boundary results,
do not provide (11) or the complete Wilson pairing estimate. The
elementary Fourier and dominated-convergence arguments above are
the verification; no numerical preview or script is evidence for
the limit. Section 6 checks the off-face differentiated heat images,
the complete cubic table (15), the absolute depth tail and trace
replacement, with L294's separate audit retained. No stronger full-box or
interacting conclusion follows from this one-face result.

### 6. Separate conceptual audit (2026-10-27)

This audit accepts (4) and the normalized O(log(eN)) cube comparison
for exactly (1)--(3), conditional on L280, L287, L292 and L293 with
their recorded qualifications, and the separately audited L294.
It does not replace the specified midpoint extension or regulator
order, nor extend the result to other components, groups or strata.
The argument below checks the uniform estimates needed by this transfer;
the previously audited signed value sigma(0)=0 remains an input.
No external theorem or new cancellation identity is imported.

**Differentiated images and the inverse square.** For the full-lattice
heat multiplier, a product of r differences vanishes to order r at
zero. A derivative of the exponential contributes tau times a
derivative of lambda. If l such factors include h first derivatives,
their differentiation order is at least 2l-h and their magnitude is
bounded by C tau^l |p|^h near zero. Gaussian rescaling, with derivatives
of the difference multiplier included, gives (6). Away from zero the
positive lower bound on lambda absorbs polynomial powers of tau.
Periodic integration by parts therefore proves (5) with arbitrary
polynomial off-diagonal decay, including the bounded-time case.

The Dirichlet images in (7) are odd at vertices 0,N; the Neumann
images are even at edge-midpoint reflection planes -1/2,N-1/2.
Their boundary rows are respectively diagonal two and one. Endpoint
differences, including B and C, differentiate the images with the
appropriate reflection signs; M_sum is a bounded sum of endpoint
values. The finitely many shifts preserve the cN separation from
every omitted face for all sufficiently fine meshes. Summing the
omitted images with K>4 gives (8). At large time, each normalized
mode contributes at most C N^-4 and each difference contributes
C|ell|/N. The three positive vertex indices in every one-form
component retain the spectral gap, even for the normal zero cosine.
This proves (9); the half-space retains only its polynomial heat decay.

The time integrals can be checked without suppressing their weights.
For r endpoint differences and a time weight tau^w, the short-time
bound is at most

\[
 C N^{-K}\int_0^{N^2}\tau^w
 (1+\tau)^{(K-4-r)/2}\,d\tau
 \le C N^{2w-2-r},
\]

on choosing K sufficiently large. The cube exponential tail and the
half-space polynomial tail give the same power, provided r>2w-2.
The actual cases are (r,w)=(0,0),(2,1) for G, (1,0) for F,J,
and (2,0) for H,P. They give N^-2,N^-3,N^-4 exactly. In particular
the inverse-square contribution to G uses (2,1), not an unjustified
integral of the unsandwiched scalar inverse square. The same integrals
with N replaced by 1+distance give the half-space bounds (12);
reflected distances are no smaller than direct distances up to bounded
slot shifts. Since supported distances are O(N), adding (11) gives
those bounds also for cube entries. Fourier transforming the heat
integrals at nonzero tangential momentum recovers L292's R_D,R_N
and -partial_s R_D; the absolutely integrable differentiated entries
add no exceptional mode. The stipulated slab limit is unchanged.

**Complete products and supported anchors.** The normal external
component occurs only on normal/tangential plaquettes. Its curl is a
tangential difference, bounded by C a A; it is generally nonzero.
Both normal slots of such a plaquette have the same depth anchor,
whereas its tangential slots lie at adjacent depths, including their
pinned zeros. In DV[u]=A(u;x)+B(u;x), AA pairs two edge lines, AB/BA
pairs one curl line and one edge line, and BB pairs either two curls
together and two edges together, or each curl with an edge. These are
exactly GG, GF/FG, HG/GH and FF. Alternating color indices eliminate
the internal pairing, and the two crossing pairings give
E[DV[u]DV[v]]=u^T E v/2. Thus the coefficient of this expectation
in S is 1/2, with all Wilson slots and colors present.

Subtracting each product using its actual kernels gives (15).
Four-dimensional shell counts give sum R_2=O(N^2), sum R_3=O(N),
sum R_4=O(log(eN)). The resulting per-anchor bounds are respectively
O(1), O(N^-1), O(N^-2 log(eN)), O(N^-2). Multiplication by the
external factors a^2 A^2, a A^2, A^2, A^2 and O(N^4) anchors yields
(16). Every contributing vertex contains an external field or its
curl and lies within the fixed support enlargement; the internal
lines still propagate in the full domain. The density diagonal costs
only O(A^2), its complete JJ product O(A^2 N^2), and the local quartic
O(A^2 N^2). The Haar diagonal cancels. This checks the full comparison
without importing L287's discarded error, which is too large at this
scale. The finitely many coarser meshes have finite matrices and
finite supported half-space pairings and fit the same bound by a
constant enlargement.

**Uniform absolute depth tail.** The negative second depth is exactly
-m-1; hence the full-line term it supplies is S_inf(q;n+m+1) with
the sign in (17). Normal external slots at a common action vertex have
the same depth, so arbitrary depth amplitudes multiply the very same
normal-block kernel used in L293. No normal-depth constancy is needed
for this identification.

L293's product estimates control the sum of absolute subtracted
products before integrating the loop momentum. An image in a product
has double-depth sum at most C/[r(r+t)] or C/[t(r+t)]; a missing
bulk row costs C/(r+t)^2. With the amplitudes of G,F,H,J these give
the four bounds in L293(12), including the H contact times the G image
and the bounded contact strip of missing rows. The local P and quartic
images obey the corresponding diagonal bounds. The actual external
curl factors Q,Q^2 remain. The chordal inequality Q<=C(r+t) is global
on the torus, so the absolute majorant C(r^-2+t^-2) applies to every
q, not merely small q. Integration and the triangle inequality therefore
bound sum_(n,m)|K(q;n,m)| uniformly.

For completeness, the majorant on the union of epsilon-balls about
0 and -q has integral O(epsilon) uniformly in q. If a ball is near the
other pole, enlarge it by a fixed factor; if the poles are separated
by d>2 epsilon, its contribution from that pole is
O(epsilon^3/d^2)<=O(epsilon). On the complement, both r and t have a
positive lower bound depending only on epsilon. Every subtracted term
then contains either an image decaying in n+m or a missing-row factor
decaying in n+m+1. A contact restricts a depth difference to a bounded
strip and leaves the image decay. Summing the remaining geometric tails
gives (19), uniformly in p,q on that complement. First M then epsilon
can be removed. This verifies the uniform absolute tail in (18), a
stronger assertion than continuity of the signed total alone. By the
unchanged missing-row convention its total is precisely L293's sigma
near zero, so (20) uses the accepted value sigma(0)=0.

**Fourier normalization, trace replacement and all modes.** Three
tangential summations by parts are permitted by the smooth compact
cutoff. Their third differences are O(a^3 A) and their support has
O(a^-3) samples, proving (21), including all depth rows. Put
U_n(p)=a^3 uhat_n(ap) and V_m(p)=a^3 vhat_m(ap). Then a^3 times
(22) is the integral of sum U_n(-p) K(ap;n,m) V_m(p), on the
rescaled torus with normalized Lebesgue measure. Each product is
bounded by C A^2(1+|p|)^-6, which is integrable in three dimensions.
This verifies (23) and all powers of a.

For fixed k and M, (24) makes U_n minus the corresponding trace
transform tend uniformly to zero for n<=M. Both transforms separately
have the preceding decay, so their product replacement is dominated
by that same integrable majorant. The finite-depth error therefore
vanishes without assuming a Fourier decay rate for the error itself.
The complementary depths cost at most C A^2 tau_M for both actual and
trace sources. The complete trace expression is multiplied by
sigma(ap), which tends to zero for every fixed p and is bounded
uniformly. This proves (26) by first passing a to zero at fixed M,
then letting M grow. No trace-limit identification or exchange of an
uncontrolled depth limit is hidden in this step.

Finally, 3a^2/N=3a^3/8. The cube error divided by N is
O(A^2 log(eN)/N), and the half-space term has the required fixed-k
vanishing with a common O(A^2) bound. L294's summable majorant for
b A^2 permits removal of the entire external tail after the finite-mode
limit. This argument applies separately to both source orders before
adding them and retains the exact three-color factor. It accepts
only the specified localized o(N) statement and its O(log(eN)) cube
comparison, not a full coefficient rate or a Yang--Mills construction.

## Mathlib

Full matching and supporting Mathlib coverage for this staggered
relative-kernel transfer has not been checked. No absence claim
or formal verification is made. The saved literature assessment
did not identify a matching theorem; this is not a novelty proof.
