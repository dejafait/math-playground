# L177 — Joint Atiyah equations remove fourteen normal squares

## Hypotheses

Retain the full conditional family and fixed conventions of L173–L176.
Thus X=S_1 x B is the product of the identical marked projective K3
surfaces with their common metric, ordered hyperkähler triple, fixed
holomorphic forms and actual connection. The hypothetical locally free
rank-two product-polystable F has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2.
\]

The full mixed correspondence and fixed marking are those of L071;
in particular retain L025/L044's actual divisor data, not only the
eigenvalue multiplicities. Write d=2lambda, where lambda is the positive
root of z^3+z^2-2z-1, and write mu,nu for its other roots. On
L=H^(1,1)(S), the q-self-adjoint D has eigenvalues d,2mu,2nu,4 with
multiplicities 5,7,7,1 as in L174. The line-class label k is L175's
fixed k=(-4,-2,1,2), with q(k,k)=-14. Use phi(u)=delta_u sigma and
ell(u)=q(phi(u),k).

Put V=End_0(F), p:X -> B, C=Rp_*V, M=R^1p_*V and W=R^2p_*V.
Use the actual arrows j,r,a, their maps j_1,i,R,A, and the actual
Q-orthogonal lift T:U=H^0(B,W) -> ker R from L165. In particular
Ri=1, ker A=i(H^1(B,M)), and Q_U(w,w')=Q(Tw,Tw'). The fixed
orthogonal tangent/normal splitting has normal cohomology

\[
 K_N=H^1(B,N),\qquad S_N(v,w)=Q(iv,iw),\qquad
 n=\dim K_N=704-s+2t,
\]

where S_N is nondegenerate, s=|Z| for the finite reduced possibly
empty split set, and t=h^0(B,N)=dim H for H=H^0(B,M). L176 gives
n>=14, t<=46 and s<=782. Retain the actual Atiyah maps mathfrak a_i
in the Atiyah-first convention, mathfrak a_2=iI, and
f=(1-P_2)mathfrak a_1. Denote the linear normal map Rf by g; this
differs from the quadratic normal bracket map below.

The bracket is the graded Yoneda commutator with no factor 1/2.
No existence of F, arbitrary section integrability, multiplicative
splitting, metric preservation, point self-norm, radical-image value,
section-bracket value or minimum square length is assumed. All forms
are complex bilinear, not Hermitian.

## Conclusion

For h,h' in H put b(h,h')=[j_1h,j_1h']. Both actual Atiyah transposes
annihilate this bracket:

\[
 Q(b(h,h'),\mathfrak a_i(u))=0\quad (i=1,2),\qquad
 Q(b(h,h'),f(u))=0.                                    \tag{1}
\]

Set beta(h)=A b(h,h), v(h)=R b(h,h) in K_N. For nonempty Z the
full residual equation, with L175's actual point vector, is

\[
 S_N(v(h),g(u))
       =2\pi i\,\ell(u)Q_U(\beta(h),w_k).              \tag{2}
\]

For empty Z its right side is zero, without introducing w_k.
There is a fixed nondegenerate fourteen-dimensional subspace

\[
 J=g\!\left(\phi^{-1}
       (L_{2\mu}\oplus L_{2\nu})\right)\subset K_N
\]

such that every v(h) lies in J^(perp S_N). Therefore the **original**
actual point quartic has an exact representation

\[
 Q_U(\beta(h),\beta(h))
       =\sum_{a=1}^{n-14}p_a(h)^2,
 \qquad n-14=\boxed{690-s+2t},                         \tag{3}
\]

with fixed homogeneous quadratic polynomials p_a on H. Zero summands
are allowed. Thus the conditional capacity from L173 decreases by
fourteen; this is not a claim about its minimum square length. In
particular s=782 forces t=46 and the point quartic to be identically
zero. It does not force beta=0 or exclude that cardinality or F.

For empty Z the quartic is already zero; one can additionally use
all fifteen nondegenerate residual directions to constrain v. For
t=0 the section-polynomial assertions are vacuous. Neither case is
excluded. The five-dimensional domain radical of f^*Q need not map
to zero and no value of Q_U(w_k,w_k) is required.

This is a conditional local ADVANCE / REPRODUCTION by specialization
of the assessed tools. The separate step 596 conceptual audit below
preserves it (EXPLORATION / REPRODUCTION), with no substantive correction
or stronger bound. No
original general theorem, geometric lower square-length bound,
new split-cardinality exclusion, construction of F, transport or
uniform primitive Hodge realization is claimed.

## Proof

**Imported tools and scope.** The invocation-start SPECIALIZE assessment
is `drafts/literature/2026-10-27-two-factor-semiregularity-point-quartic.md`.
Import Buchweitz–Flenner, *A Semiregularity Map for Modules and
Applications to Deformations*, Compositio Math. 137 (2003), 135–210,
[math/9912245v1, Definition 4.1, Proposition 3.12 and Corollary 4.8,
printed pp.28,24,32](https://arxiv.org/pdf/math/9912245v1#page=32).
The q=1 map c -> Tr((-At(F)) cup c) in H^3(X,Omega_X^1)
annihilates graded Yoneda commutators. This is the full cotangent
statement. F is locally free and hence perfect on smooth projective X;
neither fibre simplicity nor integrability of the inputs is needed.

For actual cup/evaluation/trace duality use
[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
and [Lemma 48.27.1 / Remark 48.27.2, 0FVU](https://stacks.math.columbia.edu/tag/0FVU),
with L165/L173's fixed trace and shift conventions. For orthogonal
decomposition and diagonalization import Elman–Karpenko–Merkurjev,
*The Algebraic and Geometric Theory of Quadratic Forms*, AMS Colloquium
Publications 56 (2008), I.1.A, Proposition 1.6 and Corollary 1.9,
[printed pp.14–15](https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=24).
Their hypotheses hold for finite-dimensional symmetric forms over C;
the required nondegenerate restrictions are verified below. These
general results are not reproved. The work is their application to the
actual maps, a fixed point-kernel subspace and the original polynomial.

**Both actual transposes.** Write a_i for the component of L174's
trace-free Atiyah class in H^1(X,V tensor p_i^*Omega^1). The q=1
commutator theorem gives

\[
 \theta_i(b):=\operatorname{Tr}_F(a_i\smile b)=0
       \quad\hbox{in }H^3(X,p_i^*\Omega^1).             \tag{4}
\]

Indeed the common sign relating a_X to -At(F) is nonzero, and its
removed scalar part contributes c cup Tr_F(b)=0. The graded trace of
a commutator is zero, so b lies in the trace-free summand. This
restriction uses the actual commutator in Ext(F,F), not a new bracket.

For u in H^1(S_i,T_{S_i}), cup (4) with p_i^*u, evaluate the
cotangent/tangent coefficients and take the fixed normalized fourfold
trace. Functoriality gives exactly

\[
 0=\operatorname{Tr}_X\operatorname{ev}
       (\theta_i(b)\smile p_i^*u)
   =Q\bigl(b,\operatorname{ev}(a_i\smile p_i^*u)\bigr)
   =Q(b,\mathfrak a_i(u)).                             \tag{5}
\]

The ordered cohomological degrees are 1,2,1. Moving a_i past b
has sign (-1)^(1*2)=+1; the cotangent and tangent coefficient sheaves
have degree zero. The even volume forms and the relative trace of
degree -2 introduce no additional interchange sign. This is the same
normalization as L173's base transpose, now applied to either actual
cotangent component. It requires no Leray splitting for the first
projection. Since f is mathfrak a_1 plus an actual mathfrak a_2 image
as specified in L174, (5) proves (1).

L173 gives v(h) in K_N and the actual decomposition
b(h,h)=iv(h)+T beta(h). L176 gives f(u)=ig(u)+T Af(u).
These decompositions are Q-orthogonal by L165. Thus (1) implies

\[
 0=S_N(v(h),g(u))+Q_U(\beta(h),Af(u)).                 \tag{6}
\]

L175's Af(u)=-2pi i ell(u)w_k proves (2), including its sign. If
Z is empty, Af=0. In particular g(ker ell) is orthogonal to every
v(h) whenever the displayed ell is used, regardless of point norm.

**Fourteen fixed directions with zero point projection.** First check
the position of the actual line k; mere rank(f^*Q)=15 would not give
the claimed nondegenerate hyperplane restriction. L025's divisor
decomposition is W_0 perpendicular Qv_0, with
v_0=P-O-2f_ell+E_exc/2 and A_0 zero on Qv_0. Thus k=2v_0 lies
in ker A_0. L044's specific chamber isometry fixes k and preserves
W_0, and A_c=g_ch A_0 g_ch^(-1). Consequently A_c k=0 and
pi_K k=k. The retained operator in L071 is
D|NS=2A_c+4pi_K, so

\[
                         Dk=4k.                       \tag{7}
\]

Here L025/L044 are used only for fixed lattice/chamber data, not for
an assumed kernel resolution or existence claim. The symbol K in
pi_K is that divisor line, not the normal cohomology space.

Let B_14=phi^(-1)(L_(2mu) direct sum L_(2nu)) in the first-factor
deformation space. By L174, the two eigenspaces have dimension seven
each, are q-orthogonal and have nondegenerate q restrictions. Since
2mu and 2nu differ from 4, self-adjointness and (7) give q(x,k)=0
on their sum. Therefore ell|B_14=0 and L175 gives Af|B_14=0,
also when Z is empty. On this subspace L176 gives f=ig, whence

\[
 S_N(g(u),g(u'))=Q(f(u),f(u'))
     =\gamma q\bigl((d-D^2/d)\phi(u),\phi(u')\bigr).   \tag{8}
\]

The common trace scalar gamma is nonzero. L174's distinct absolute
root values show d-(2mu)^2/d and d-(2nu)^2/d are nonzero. Thus
(8) is nondegenerate on B_14. If g(u)=0, pairing with all u' in
B_14 and (8) gives u=0; hence J=g(B_14) has dimension fourteen
and nondegenerate S_N restriction. Equation (6) proves v(H) is
contained in J^(perp S_N). This argument discards neither a point
term with nonzero ell nor a possible nonzero image of the five
radical directions; it only uses the specified B_14.

**The original polynomial and the bound.** By the imported orthogonal
decomposition theorem,

\[
 K_N=J\mathbin{\perp}J^{\perp},\qquad
 \dim J^{\perp}=n-14,
\]

with nondegenerate S_N restriction on the complement. L173's
dimension-free cyclic identity for the actual diagonal bracket gives

\[
 Q_U(\beta(h),\beta(h))=-S_N(v(h),v(h)).                \tag{9}
\]

Choose once and for all a basis of J^perp diagonalizing its form to
diag(1,...,1), which is possible over C. Because R and all the
projections are fixed linear maps, v(h)=sum q_a(h)e_a has homogeneous
quadratic polynomial coefficients. Equation (9) is therefore (3)
with p_a=sqrt(-1)q_a. No h-dependent change of basis, pointwise square
root, border-rank argument or subtraction of a point polynomial has
occurred. In particular (3) concerns exactly the same beta and Q_U
as L173, even if Q_U(w_k,w_k)=0.

At s=782, n>=14 and t<=46 imply -78+2t>=14, hence t=46 and
n=14. Then v=0 and (9) gives the zero quartic. A nonzero beta may
still have isotropic values over C, so no point-bracket vanishing or
new cardinality exclusion follows. If Z is empty, U=0; furthermore
Af=0 on all of L174's fifteen-dimensional nondegenerate residual
domain, and the same argument constrains v to its normal orthogonal
complement. This does not improve on the already zero point quartic.
If t=0, H=0 and the polynomial claim is vacuous. The original
fourteen-square capacity reduction is meaningful without either
endpoint or an assumed nonzero bracket. A lower bound on the actual
quartic's minimum square length remains a separate unresolved problem.

**Separate conceptual audit (2026-10-28, step 596).** The unchanged
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-28-joint-atiyah-square-bound-critical-audit.md`.
This checks the specialization conditional on the stated inputs; it
does not reaudit their entire ancestry or assert existence of F.
The inspected primary coverage above is reused: BF's full cotangent
commutator theorem for perfect F, the actual trace/evaluation duality
with tensor signs, and EKM's nondegenerate-subspace decomposition and
diagonalization over C. None is reproved or upgraded to injectivity.

First, the full Atiyah class and both components use the single
first-order convention of L173/L174. For degree-one inputs x,y,
Tr_F(x cup y + y cup x)=0 by graded trace, so their actual bracket
is in H^2(X,V). Removing the scalar part of the Atiyah class therefore
does not change its traced product with the bracket. BF applies to
these Ext classes because F is locally free on smooth projective X;
it requires neither their integrability nor fibre simplicity. Projecting
the zero full cotangent class to either product component gives (4).

In the traced product a_i cup b cup p_i^*u the degrees are 1,2,1.
Moving a_i through b has sign +1; evaluation of the degree-zero
cotangent/tangent coefficient bundles has no additional sign. The
fixed normalized fourfold trace is the one defining Q, including its
relative matrix-trace scalar. Thus it gives exactly
Q(b,ev(a_i cup p_i^*u)), not an unrelated dual functional. The
relative trace shift -2 and the volume forms are even. This proves
(5) for each actual map without using a second Leray decomposition.
L174's formula f(u)=mathfrak a_1(u)+mathfrak a_2(phi^{-1}(Dphi(u)/d))
then proves the residual vanishing with the same signs.

Next, L165 gives Q(x,iy)=S(Rx,y) for every x, including the point
lift, with its base-first sign already incorporated into S. Since
Ri=1 and ker A=i(K), x-iRx is the unique element T(Ax) of ker R.
L173 puts Rb in K_N, and L176 puts Rf there as well. Their two
orthogonal decompositions consequently give (6) with these actual
maps and the same Q_U. L175's audited top-base-change identity is
Af=-2pi i ell w_k; substitution gives the plus sign on the right
of (2). There is no further minus sign from S=-B_M. No ordinary
middle-base-change isomorphism or vanishing of the finite top term
is needed. For empty Z that term is zero without defining w_k.

The marking can be checked independently of its stated spectrum.
In L025's ordered divisor basis (f_ell,O,E_exc,P), k=2v_0 and its
displayed matrix A_0 gives

\[
 A_0 k=(-4-4-2+10,\,-2-1+3,\,-2-2+4,\,0)=0.
\]

L044's displayed chamber matrix g_ch gives
g_ch k=(-4-2-2+4,-2,2+1-2,2)=k. Hence A_c k=0 and pi_K k=k.
L071 explicitly retains this final chamber and this full D, proving
Dk=4k. This is not a conclusion for arbitrary chamber conjugations.
The fixed Gram matrix also gives Gk=(0,0,0,-7), hence q(k,k)=-14,
consistent with L175's label.

L174's semisimplicity and q-self-adjointness make the distinct
eigenspaces orthogonal with nondegenerate restrictions. Its exact
root intervals (-2,-3/2), (-1/2,0), (1,5/4) separate absolute values;
therefore neither d-(2mu)^2/d nor d-(2nu)^2/d vanishes. They also
separate 2mu and 2nu from 4. The two seven-dimensional eigenspaces
are thus in k^perp. On their sum Af=0, so f=ig and (8) is exactly
the normal pullback, not a rank-one approximation. Its nondegeneracy
forces g to be injective there and makes J nondegenerate of dimension
fourteen. This verifies the hypothesis needed by EKM Proposition 1.6.
It says nothing about the images of the five domain radical directions.
The bracket's orthogonality to f now forces v(h) into this fixed J^perp.

Finally L173's dimension-free cyclic identity applies to the same
unhalved diagonal commutator. With the actual orthogonal lift its
norm equation is exactly (9). Since both components are homogeneous
quadratic maps and J^perp is a fixed linear subspace, expansion in
one diagonalizing basis gives quadratic coordinate polynomials.
Over C the nonzero diagonal scalars can be absorbed by constant
square roots; the minus in (9) is absorbed by sqrt(-1). This is an
exact identity for Q_U(beta,beta) with n-14 terms, including zero
terms. It neither changes the point polynomial nor uses a varying
basis, a pointwise root or a closure argument. In particular it is
independent of whether the actual vector w_k is isotropic.

L176 ensures n>=14. At s=782, n=-78+2t and t<=46 give n=14,
t=46, so J=K_N and v=0. Equation (9) gives only a zero scalar
quartic; nonzero isotropic beta values remain possible over C.
For empty Z the quartic is already zero, and the full fifteen
nondegenerate residual directions have no point part. For t=0,
L116 gives H=0, so the section-polynomial claim is vacuous. No
endpoint has been silently discarded or asserted attainable.

The audit preserves (1)–(9) and their qualifications with no substantive
repair or new bound. Its outcome is EXPLORATION / REPRODUCTION, not a
second advance for the original specialization. The direct mathematical
inputs already recorded in the DAG suffice and no edges change. Actual
point norm, radical images, section quadrics, minimum square length, F
existence and uniform primitive realization remain unresolved. No new
mathematical script, lemma or external theorem was needed for this audit.

## Mathlib

Full matching coverage of the joint geometric transpose and this
actual polynomial specialization has **not been checked**. No absence
claim or Lean verification is made. L176's pinned rank inequalities
are supporting results, not a formalization of (1)–(9); the argument
here uses the cited nondegenerate-subspace and diagonalization
theorems after verifying their hypotheses. The separate critical informal
audit above is complete; it is not a Lean verification.
