# L165 — The complete third ordered E,E trace is cubic-bounded

## Hypotheses

Keep L161's full-link SU(2) relative cube, a=8/N through sufficiently
fine admitted even meshes, straight direction-1 lower-rooted forest,
complete compact displacement and both actual L010 probes at tau=1/16.
Take the bare expansion at fixed mesh before refinement. Use ordinary
stored-coordinate D,L,Sigma,F=Phi Sigma and the colored matrices
M=T_R(h_k t_c,.,.), Q_L(ell)=Lhat B_ell-B_(Lhat ell), ell=h_l t_c.
Hats denote three-color diagonal extensions. Retain both residual
subtractions, all action faces and normal end links, the upper pinned
jump, constant axial mode and full exterior heat spectrum. The full
tensors are formed before forest restriction.

Define precisely the third trace in L161(3), with its outside factor:

    Z_i=-6 sum_(k,l,c) c_(i;kl)
                  Tr[Q_L(ell) Fhat M Sigmahat].          (1)

## Conclusion

For i=3,6 there are mesh-independent constants such that

    |Z_i|<=C_i N^3.                                     (2)

More precisely, write ell=ell_b+ell_top using L163's exact exterior
split and put P=Sigma L. Then

    Z_i=-6 sum c Tr[Phat B_(ell_b) Fhat M]
                      +O_i(N^2 sqrt(log(eN))).          (3)

The omitted upper-column part is O_i(N^2), and the smooth-action
subtraction is O_i(N^2 sqrt(log(eN))); both vanish at cubic scale.
The retained bulk trace is bounded only by O_i(N^3). Its a^3 limit,
value and vanishing are not established. Two other ordered traces
in L161(3) still lack cubic control, and L158/L159's mixed branches
still lack scaled limits. No complete-response bound, compensation,
finer asymptotics, interacting reflected error <=c_box/2, continuum
construction or infrared finite positive mass follows. This is local
standard-method progress, without a claim of novelty beyond the
sources checked in the unchanged assessment.

## Proof

### 1. Cancel the action Hessian in the actual trace order

Fix exterior labels k,l,c. Polynomial factors p(k)p(l) are displayed
when needed; every estimate is uniform in the mesh. L157 proves
Sigma L=L Sigma=P, the full four-dimensional co-closed projector.
Cyclicity of the finite trace, without any multiplier commutation,
gives exactly

    Tr[Q_L(ell) Fhat M Sigmahat]
       =Tr[Phat B_ell Fhat M]
                    -Tr[B_q Fhat M Sigmahat],
    q=Lhat ell=(L v_l)t_c.                              (4)

Here P is not a transverse projector or the forest retraction. L161
proves that M has bounded stencil radius, at most C N^4 nonzero
entries, both indices in a fixed compact interior region, entries
bounded by C p(k), and operator norm bounded by C p(k). These
statements include both insertion subtractions. L163/L164 give

    ||ell_b||_infinity<=C a p(l),
    ||ell_top||_infinity<=C p(l),
    ||q||_infinity<=C a^3 p(l).                          (5)

The second column is supported only on direction-1 normal edges in
the last axial layer. The last estimate is L156(10), using L R=L
before applying the mode bound. It is not a derivative estimate on
the discontinuous forest column.

### 2. The compact-source projection and single-prefix kernels

All distances in this proof are lattice distances, with fixed stencil
shifts absorbed into constants. Let e be any link in the compact
support of M and f any variable link. Then

    |P_(ef)|<=C_delta[(1+dist(e,f))^-4+N^-4].             (6)

To justify (6), including end edges, put G_v=(D^T D)^(-1). The
finite Hodge identity of L157 implies

    P=I-D G_v D^T.                                     (7)

Indeed Delta D=D(D^T D) for Delta=L+D D^T, so
Sigma D=D G_v and I=Sigma L+Sigma D D^T. G_v is the scalar
four-dimensional Dirichlet Green matrix, with zero vertex values on
every face. Each entry of D G_v D^T is a difference in the observation
coordinate and another in the source coordinate; their directions
may be different. A normal end edge uses a zero boundary vertex and
its adjacent interior vertex. This is the same difference formula,
not a discarded boundary row.

For completeness, the differentiated heat argument needed here has
two differences, instead of L164's zero or one. On the infinite
lattice, if H_t is the scalar nearest-neighbor heat kernel, for any
two coordinate differences and any integer m,

    |partial partial' H_t(r)|
      <=C_m(1+t)^-3(1+|r|/sqrt(1+t))^-m.                (8)

For t>=1 its Fourier multiplier is a product of two difference
symbols and exp(-t lambda(theta)), lambda=4 sum sin^2(theta_j/2).
Near zero the product vanishes to order two, and lambda is comparable
to |theta|^2. The L1 norm of an m-th coordinate derivative of this
multiplier is bounded by C_m t^((m-6)/2): the product rule, the
vanishing orders of the two factors and first derivatives of lambda,
and Gaussian scaling give this bound term by term. Away from zero
exponential decay absorbs every power of t. For t<=1 these torus
derivatives are bounded. Integration by parts in a largest coordinate
of r, combined with the zeroth derivative estimate, proves (8).
Integrating in t gives C(1+|r|)^-4 for the infinite Green differences.

Use the exact odd, period-2N image formula in all four coordinates
for the Dirichlet heat matrix. It is valid also when either endpoint
is a boundary vertex, where paired images give zero. Since both
endpoints of e are a fixed positive physical distance from every
face, all nonidentity images have distances at least
c_delta N(1+|b|), b in Z^4, after finitely many reflection choices.
The two differences stay differences in their respective reflected
coordinates. For t<=N^2, sum (8) with m>8 and integrate: the image
error is at most C_delta N^-4. For t>=N^2, normalized fourfold sine
modes give a heat kernel with both differences bounded by
C N^-6 exp(-c t/N^2). Each difference contributes at most C|q|/N;
the full Gaussian mode sums are bounded at these times. Its integral,
and the infinite heat tail from (8), are O(N^-4). This proves (6)
by (7), including the identity term at e=f. Every source position
and normal end edge is retained.

Next let v=(s,y) be an interior vertex and e' a compactly supported
link from the other index of M. F has zero columns unless e' has
component 1. For that component, with transverse coordinate x',

    |F_(v,e')|<=C_delta/(1+|y-x'|).                     (9)

This is a prefix-column estimate, not a positive covariance bound.
By definition its entry is the sum, over 0<=t<s, of
Sigma_((1,t,y),e'). Symmetry permits applying L164's compact-source
Green comparison to e'. It bounds each summand by
C[(1+sqrt((t-e'_1)^2+|y-x'|^2))^-2+N^-2]. Summing the first
bound over the whole integer axial line gives C/(1+|y-x'|),
by comparison with the integral of (b^2+t^2)^-1 for
b=1+|y-x'|>=1. The second contributes at most C/N, which is
absorbed since |y-x'|<=C N. This proves (9), uniformly in s,
without removing any of the prefix, its constant mode or its upper
endpoint. F is exactly zero at pinned vertex rows if such rows are
included by zero extension.

### 3. Sum the projection/prefix product before counting placements

For every allowed pair (e,e') of M, their distance is bounded by its
fixed stencil radius. B_ell has only endpoint-sum entries, of size
at most C|ell_f|, with a bounded number of color entries. Thus the
absolute summand of Tr(Phat B_ell Fhat M) is controlled by the sum
over links f and their interior endpoints v of

    C |M_(e',e)| |ell_f| |P_(ef)| |F_(v,e')|.            (10)

For ell_b, the full spatial sum of the last two kernels is bounded
independently of N. Here are the shell counts. If m denotes the
transverse distance and n the axial difference, the number of
transverse points in the m-th shell is at most C(1+m)^2, while

    sum_(n in Z) (1+sqrt(n^2+m^2))^-4
                       <=C(1+m)^-3.

Consequently the decaying part of (6), times (9), has sum bounded by
C sum_(m>=0)(1+m)^-2<infinity. For the constant comparison error
in (6), the finite axial count is at most C N and

    sum_(y in transverse cube) (1+|y-x'|)^-1<=C N^2.

Its total is therefore O(N^-4 N N^2)=O(N^-1), also bounded.
Fixed endpoint/stencil shifts and the four link orientations only
alter constants. Use (5), (10) and the C N^4 residual entries:

    |Tr(Phat B_(ell_b) Fhat M)|
                        <=C p(k)p(l) a N^4
                        <=C p(k)p(l) N^3.              (11)

For ell_top, every f is at distance at least delta N from e,
so (6) gives C_delta N^-4. Its only unpinned endpoint has axial
level N-1; (9) still holds there. Summing over all transverse top
positions gives C N^2 rather than a four-dimensional sum. Therefore

    |Tr(Phat B_(ell_top) Fhat M)|
                 <=C p(k)p(l) N^4 N^-4 N^2
                 <=C p(k)p(l) N^2.                     (12)

No smooth extension or O(a) estimate is assigned to this top column.
Side faces and normal end edges are already covered by (6) and (9).

### 4. The complete smooth-action subtraction is subcubic

The full relative spectrum of L026 implies

    ||Sigma||_HS^2<=C N^4 log(eN).                      (13)

For each component, indices have one possible zero and three
positive coordinates, eigenvalue at least 4|q|^2/N^2, and at most
4m^3 indices in the shell max q_j=m. Summing inverse eigenvalue
squares gives C N^4 sum_(m=1)^(N-1) m^-1, proving (13).
The axial constant mode and every other mode are counted. L161's
exact squared-prefix domination gives ||F||_HS<=C N^3. The endpoint
map satisfies ||B_q||<=C||q||_infinity, also on pinned end edges.
The trace Cauchy--Schwarz inequality, with no positivity assumption,
now gives

    |Tr(B_q Fhat M Sigmahat)|
       <=||B_q|| ||Fhat||_HS ||M|| ||Sigmahat||_HS
       <=C p(k)p(l) a^3 N^3 N^2 sqrt(log(eN))
       <=C p(k)p(l) N^2 sqrt(log(eN)).                  (14)

This is the whole B_(Lhat ell) term in (4), not an estimate on only
one action face. The fixed three-color factors are absorbed in C.

### 5. Complete heat sum and the threshold actually reached

L156(8) gives sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i for either actual
probe. Thus (4), (11), (12) and (14), with the three exterior colors
and the original -6 factor once, prove (2)--(3). The scaled errors
are O(sqrt(log(eN))/N), whereas (11) gives only a bounded a^3-scaled
bulk value. No cancellation of that bulk value has been proved.

The meaningful checks here are analytic: the exact order in (4),
both relative boundary differences in (7)--(8), the anisotropic
kernel sum in (9)--(11), the separated top-face count in (12), and
the full inverse-square spectral sum in (13). No mathematical script
or finite-mesh extrapolation is used. In particular F is never
replaced by K or treated as independent noise, and no bound is
transferred to the other two prefix trace orders or signed E.

## Mathlib

Full matching theorem and supporting lattice kernel coverage:
**not checked**. Unknown is not absence. Reuse the unchanged
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No external theorem is newly imported or reproved. L026 supplies the
relative product modes, L156 the action-column and complete heat
bounds, L157 the projector/endpoint identities, L161 the actual
trace and compact residual/prefix estimates, and L163/L164 the
exterior split and compact-source Green comparison. The elementary
two-difference heat specialization is written explicitly because
its normal end rows and derivative count are essential to (6).
