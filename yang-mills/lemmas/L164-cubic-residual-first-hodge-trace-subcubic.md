# L164 — The complete first Hodge trace is subcubic

## Hypotheses

Keep L161 and L163's full-link SU(2) relative cube, a=8/N through
sufficiently fine admitted even meshes, direction-1 straight lower-rooted
forest, complete compact displacement and both actual L010 probes at
tau=1/16. Take the bare expansion at fixed mesh before refinement.
Use their ordinary-coordinate Sigma, h_k=R v_k, c_(i;kl), colored
M=T_R(h_k t_c,.,.), N=T_S(h_l t_c,.,.), and L163's exact N=N_b+N_top.
Both residual insertion subtractions, every action plaquette, normal
end links, upper pin, constant axial mode and full exterior heat sum
remain. Full tensors precede forest restriction.

Define only the first term of L161(3):

    W_i=-36 sum_(k,l,c) c_(i;kl) Tr(M Sigmahat N Sigmahat).

## Conclusion

For i=3,6 there are constants independent of N such that

    |W_i| <= C_i N^2 log(eN),          a^3 W_i -> 0.       (1)

This removes one complete ordered trace at cubic scale. The other
three traces surviving L161/L162, and the scaled limits of L158/L159's
mixed branches, remain unresolved. This is not a bound or a vanishing
limit for the complete cubic residual/action response, a compensation
coefficient, a quadratic-scale limit, or a logarithmic coefficient.
Other jets, interacting reflected error <=c_box/2, continuum axioms
and finite positive infrared mass remain open. This is a reproduction
and specialization of finite Taylor, reflection and Green-kernel
methods under the unchanged EXPLORE assessment, without a novelty claim.

## Proof

### 1. Smooth columns after the exact upper-jump split

Fix heat labels k,l and exterior color c. Constants below may contain
a fixed polynomial p(k)p(l); the complete summation is done last.
All distances in the estimates below are in lattice units, between
edge midpoints, with bounded stencil shifts absorbed into constants.

The full residual matrix has compact interior support, bounded
stencil radius, and O(N^4) placements. L161's local coefficient proof
and L149/L155's full words give the following decomposition:

    M=sum_e M_e^0+M_err,                                (2)

where e runs through supported force/vector edges. Freeze u_a and
the exterior column at the midpoint of e in the COMPLETE degree-three
coefficient of Q_e=<G_e,X_e>. M_e^0 is that cubic tensor contracted
with the frozen exterior column. It has finitely many entries of
size <=C p(k). M_err is a sum of O(N^4) finite stencils with entries
<=C a p(k). It includes BOTH insertion subtractions.

Indeed the force/vector coefficients are O(1/a), the exterior
column is O(a), and changing either smooth sample across a fixed
stencil costs O(a) relatively to these bounds. The insertion cubic
coefficients are O(1), so their exterior contraction is O(a).
L028's smooth sampled u_a and L150 section 2's C^1 exterior-column
estimate justify these errors before any heat sum. No residual
column is extended across the upper pin.

The action exterior h_l^b has zero component 1 and satisfies

    |h_l^b|<=C a p(l),
    |h_l^b(f)-h_l^b(g)|<=C a^2 p(l)(1+dist(f,g))          (3)

on bulk variable links of each same component, with a smooth
componentwise extension to compare different placements. Its
unscaled bulk circulation is O(a^2 p(l)). To check that (3) is
global in the bulk, use L026's prefix formula on v_l=a lambda_l^-1/2
f_(l,a). Each transverse component is the original sine/cosine mode
minus a transverse difference of its finite axial prefix. The
finite cosine sum has the exact sine-primitive extension used in
L150 section 2; the zero axial frequency has its linear primitive.
The factor (q/N)/sin(pi q/(2N)) is uniformly bounded for 1<=q<N.
The modes and their physical derivatives consequently give a C^1
bound C a p(l) for this extension on the closed physical cube.
Component 1 is zero after L163's split. Values on fixed tangential
links, especially the upper face, need not agree with this extension.

Remove from the action sum a collar of a fixed number of lattice
layers containing every plaquette with a fixed link and all stencils
touching a face. This is an ESTIMATE of their contribution, not a
change of the action. There are O(N^3) such plaquettes, each with
N_b entries O(a p(l)); all their source links have distance >=delta N
from the residual support. Section 2 below gives |Sigma_(ef)|<=C N^-2
at that separation. Their total contribution is therefore bounded by

    C p(k)p(l) N^4 N^3 a N^-4 <= C p(k)p(l) N^2.         (4)

Thus all boundary plaquettes are retained with a subcubic error,
without differentiating a falsely smooth pinned exterior field.

### 2. Relative Green estimates, including their boundary comparison

Let g be the scalar infinite Z^4 Green kernel for the unscaled
nearest-neighbor Laplacian, copied diagonally to link components and
colors. For any fixed nearest-neighbor difference partial and any
observation edge e in the compact residual support, the relative
component Green kernel satisfies, on the bulk source stencils,

    |g(r)|<=C(1+|r|)^-2,
    |partial g(r)|<=C(1+|r|)^-3,
    |Sigma_(ef)-g_(ef)|<=C_delta N^-2,
    |partial_f(Sigma-g)_(ef)|<=C_delta N^-3.              (5)

Mixed components vanish. In a circulation partial_f is applied to
the appropriate same-component source coordinate separately. It
does not mean a difference between different component kernels.

Here is a proof of the estimates, so no uninspected boundary Green
theorem is assumed. For the infinite heat kernel H_t, Fourier
integration by parts on the torus gives, for j=0,1 and any integer m,

    |partial^j H_t(r)|
      <=C_m (1+t)^(-(4+j)/2)
                   (1+|r|/sqrt(1+t))^-m.                (6)

For t>=1, split a smooth torus partition into a neighborhood of
zero and its complement. The symbol lambda=4 sum sin^2(theta_mu/2)
is comparable to |theta|^2 at zero; the difference symbol is O(|theta|).
The L^1 norm of each m-th coordinate derivative of
the product of this symbol and exp(-t lambda) is at most
C_m t^((m-4-j)/2). This follows by the product rule: derivatives of
the exponential are polynomials in t and derivatives of lambda;
first derivatives of lambda are O(|theta|), and integration against
exp(-c t|theta|^2) supplies the corresponding powers of t^-1/2.
On the complement the exponential dominates every power. For
0<=t<=1 all the torus derivatives are uniformly bounded. Integrate
by parts in a coordinate with maximal |r_mu| and combine with the
zeroth-derivative estimate to obtain (6). Integrating (6) in t,
split at t=(1+|r|)^2 and take m>4, proving the first two lines of (5).

The finite component heat kernel is the tensor product of one
edge-Neumann and three vertex-Dirichlet kernels from L026(6)-(7).
Odd reflection for vertex rows and even reflection about the
half-integer edge endpoints give its exact period-2N image formula.
The formula follows either by grouping the infinite heat kernel's
Fourier series into period-2N frequencies, or by its initial delta
and the Dirichlet/Neumann recurrence. It includes the constant edge
mode. Apart from the identity image, every image has distance at
least c_delta N(1+|b|) from e, after a fixed finite grouping, with
b in Z^4, because e is separated from every face. For t<=N^2, sum
(6) over these images with m>8. Integrating yields C N^-2 for j=0
and C N^-3 for j=1. The reflection signs of a source difference are
retained; only their absolute values are bounded.

For t>=N^2 the finite mode expansion has entries bounded by
C N^-4 exp(-c t/N^2). A source difference changes the sine/cosine
factor by at most C |q|/N, hence its complete mode sum is bounded
by C N^-5 exp(-c t/N^2). Indeed the remaining Gaussian shell sums
in |q| are bounded when t/N^2>=1, and at least three indices are
positive. The infinite tails from (6) are respectively C N^-2 and
C N^-3 after integration. This proves the last two lines of (5),
uniformly in all source positions, including those next to a face.
It also proves the bound used in (4). No internal mode or boundary
input row was omitted.

### 3. Keep the action's rough difference before taking absolute values

Use L048 section 1's exact degree-three Wilson action identity
q_(3,p)=<w_(1,p),w_(2,p)>, where w_1=d_p x and
w_2=(1/2)sum_(u<v)[y_u,y_v] for the ordered signed plaquette links.
Write Q_p(x,y) for the symmetric polarization of w_2. The full
trilinear action tensor is exactly

    T_S(h,x,y)=(1/3)sum_p [
      <d_p h,Q_p(x,y)>+<d_p x,Q_p(h,y)>
                                +<d_p y,Q_p(h,x)>].     (7)

All maps in Q_p have bounded finite stencils. In the last two terms
the rough circulation acts on one covariance column in the trace;
this is an exact index contraction, not a coefficient commutation.
The first term retains the exterior circulation.

For a residual stencil centered at z put r=1+dist(z,p). Equations
(3),(5),(7), with bounded stencil shifts, bound its two rough-difference
contractions by products of an O(a p(l)) coefficient and

    [(1+r)^-2+N^-2][(1+r)^-3+N^-3].                      (8)

The exterior-circulation contraction instead has coefficient
O(a^2 p(l)) and the product [(1+r)^-2+N^-2]^2. Four-dimensional
shells contain at most C r^3 plaquettes. Consequently the sum of
(8) over the finite cube is bounded by C, and the sum of the latter
product is bounded by C log(eN). These estimates prove a bound
C a p(l) for each fixed residual entry's entire bulk contraction;
(4) supplies its boundary part. Applying it to M_err in (2) gives
O(p(k)p(l) N^2). They also bound the actual exterior-circulation
term with bounded M by O(p(k)p(l) N^2 log(eN)).

For the remaining M_e^0 terms freeze the action column at the
center z of e, using its constant component values h_0. Its
circulation is zero. The coefficient difference in each rough-
difference term is <=C a^2 p(l) r by (3). The weighted shell sum
of (8) is <=C log(eN): the four contributions are bounded by
sum r^-1, N^-3 sum r^2, N^-2 sum r, and N^-5 sum r^4,
respectively. Thus this freezing costs O(p(k)p(l) N^2 log(eN))
after all residual placements. This step does not freeze a rough
covariance or discard the actual exterior circulation.

Now replace both finite covariances in each frozen rough-difference
contraction by g, with its difference on the same source leg. By
(5), the per-placement error is at most

    C a p(l) sum_(r<=CN) r^3 [
         N^-2(1+r)^-3+N^-3(1+r)^-2+N^-5]
       <=C a p(l)/N.                                   (9)

Extending that frozen infinite-kernel action sum from the bulk cube
to all plaquettes of Z^4 costs the same bound: every newly included
source is at distance >=delta N and
sum_(r>=delta N) r^3(1+r)^-5<=C/N. Multiply by the O(N^4)
residual placements and bounded M_e^0 entries. Both errors in (9)
are O(p(k)p(l) N^2). The resulting infinite contraction is absolutely
convergent; this is why its signed parity may now be used.

### 4. The complete frozen contraction is zero

Let I be the signed link reflection about the midpoint of e:
(I x)_f=-x_(f^iota). It preserves the positive-link grids even when
the center is a half-integer. The scalar infinite Green kernel,
component and color diagonally extended, commutes with I.

L150 section 3 proves the exact nonlinear local identity
Q_e(I Theta;-u)=Q_e(Theta;u) using BOTH transported endpoints and
the complete incident action force. Since Q_e is linear in the
frozen u, its homogeneous degree-three coefficient q_e^0 obeys
q_e^0(I x)=-q_e^0(x). This uses the exact identity before taking
the coefficient, rather than a parity guess for separate monomials.
The frozen exterior h is constant in space, so I h=-h. Polarization
then yields

    T_(q_e^0)(h,I x,I y)=T_(q_e^0)(h,x,y),
    I^T M_e^0 I=M_e^0.                                 (10)

The infinite Wilson action's cubic tensor is reflection invariant:
reflection permutes plaquettes and preserves their Wilson traces.
Here polarization with a constant column is defined first on two
finitely supported rough inputs, for which the plaquette sum is finite;
the absolutely convergent Green-column contraction then extends it.
Polarization with the constant action column h_0, for which
I h_0=-h_0, gives instead

    T_S(h_0,I x,I y)=-T_S(h_0,x,y).                       (11)

Apply this signed permutation to the two rough slots in the
infinite-kernel contraction. Equations (10)-(11) and Green invariance
make it equal to its negative. The absolute convergence established
in section 3 justifies this permutation of the full action sum.
Therefore every frozen M_e^0 contraction is exactly zero. This
does not assert pointwise-zero summands or symmetry of the forest
or finite box.

Combine (2),(4),(7)-(11): the N_b trace is bounded by
C p(k)p(l) N^2 log(eN). L163 bounds its N_top contribution by
C p(k)p(l) N^2. L156(8)'s absolute polynomially weighted exterior
heat summability permits summing every k,l and all three exterior
colors, with -36 applied once. This proves (1), since
a^3 N^2 log(eN)=512 log(eN)/N tends to zero.

The proof retains signed correlations and uses only the true Hodge
Green kernels in this particular trace. It does not treat E as noise,
replace F=Phi Sigma by a covariance, or transfer this estimate to
different orders containing a prefix. No mathematical script or
numerical evidence is needed: the checks are the exact action
polarization, reflected local identity, full-mode Green bounds and
the actual/required comparison O(N^2 log N)=o(N^3).

## Mathlib

Full matching theorem and supporting lattice heat-kernel coverage:
**not checked**. Unknown coverage is not absence. The standard finite
Taylor/polarization and Fourier heat representation are specialized
here; L048 supplies the exact action cubic, L149/L155 the complete
residual words, L150 the exact nonlinear reflected force/vector
identity, L026 the relative spectrum, L028 the smooth coefficient
bounds, L156 the full heat summation, and L161/L163 the ordered trace
and exact upper split. The new kernel estimates and error bounds are
proved here, not imported from an uninspected general theorem. A
reproof of their specialized forms is needed to distinguish relative
edge/vertex faces and preserve the differentiated source placement.
