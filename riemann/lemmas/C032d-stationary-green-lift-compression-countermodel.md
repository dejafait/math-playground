# Counterexample C032d: stationary Green lifts need not compress contractively

## Hypotheses

The implication under audit uses real Euclidean spaces V=R^2,
H=R^3 and O=X=R. Its data are rational linear maps L:V->H,
C:H->O and R:V->X, with every entry of C strictly positive
and R onto. For rational r_j>=0 put

\[
 K=\operatorname{diag}\left(\frac{1-r_j}{1+r_j}\right)_{j=1}^3,
 \qquad G_+=CL,\qquad G_-=CKL,
 \qquad Q(v,w)=(G_+v)(G_+w)-(G_-v)(G_-w).
 \tag{1}
\]

Require N=ker R to be nonzero and Q strictly positive on N\{0}.
On each fiber Rv=x, require a unique minimizer f_x of Q(v,v),
with Q(f_x,h)=0 for every h in N. Require G_+f_1!=0, and define

\[
 Ey=\frac{y}{G_+f_1}Lf_1\quad(y\in O).
 \tag{2}
\]

Thus E is the prescribed lift of the minimizing plus profile,
not an arbitrary chosen right inverse. The question is whether
these premises force ||CKE||<=1, equivalently Q(f_1,f_1)>=0.
The equivalence here concerns the one-dimensional minimizing image.
All norms on H,O,X in this statement are Euclidean.

## Conclusion

They do not. The following exact data satisfy every premise:

\[
 C=\begin{pmatrix}1&1&1\end{pmatrix},\quad
 R=\begin{pmatrix}1&0\end{pmatrix},\quad
 L=\begin{pmatrix}2&2\\1&0\\-2&0\end{pmatrix},\quad
 (r_1,r_2,r_3)=(1/3,1,3).
 \tag{3}
\]

They give ||K||=1/2, Q|_N=3t^2, f_x=(x,0),
Q(f_1,f_1)=-3 and CKE=2I_O. Hence ||CKE||=2>1.
The graph-domain completion and continuous algebraic boundary-form
identities also hold in this example.

This refutes only the generic sufficiency inference isolated in
assessment1264. It is not a theta kernel, an actual-Xi counterexample,
or a disproof of a theta-specific inequality or of RH. The source's
special Volterra geometry, model identification and RH-facing bridge
are not hypotheses verified by this finite example.

## Proof

### Source scope and why a direct check is needed

The prior assessment is
`drafts/literature/2026-11-17-green-lift-contraction-inference-audit-1264.md`.
This is a REPRODUCTION audit of a proposed operator inference, not a
claim of a new operator theorem. In Marvin B. Freedman,
*Finite-core Volterra reductions for a Weyl-positive Riemann phase
kernel*, arXiv:2606.29555v1 (28 June 2026),
[Appendix C](https://arxiv.org/html/2606.29555v1#A3), the relevant
passage introduces T=CKE, then the graph norm and boundary-form
extension, and infers contraction from the multiplier bound and
trace-fiber stationarity. Those exact displayed premises were checked
in this audit; source computations and theta positivity are not imported.

The comparison result is R. G. Douglas, *On majorization,
factorization, and range inclusion of operators on Hilbert space*,
Proc. Amer. Math. Soc. 17 (1966), 413–415,
[Theorem 1, proof pp. 413–414](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf).
Its norm-sensitive factorization theorem is already assessed in
assessment1264. No instance of it is needed as a premise below:
direct rational computation decides the fixed discriminator without
assuming a norm bound for C or E or using ambiguous extracted symbols.
The separate L870 full-fiber forcing obstruction is a contrast only;
none of its mathematical conclusions enters this proof.

### Multiplier, feature rows and stationary fibers

Substituting (3) gives

\[
 K=\operatorname{diag}(1/2,0,-1/2),\qquad
 G_+=\begin{pmatrix}1&2\end{pmatrix},\qquad
 G_-=\begin{pmatrix}2&1\end{pmatrix}.
 \tag{4}
\]

Each integration weight is 1>0, all r_j are nonnegative,
and R is onto since R(x,0)=x. For z in H,
||Kz||^2=(z_1^2+z_3^2)/4<=||z||^2/4, with equality at z=(1,0,0).
Thus ||K||=1/2, strictly below the allowed bound 1.
Equation (1) now gives, for v=(x,t) and w=(y,u),

\[
 Q(v,w)=(x+2t)(y+2u)-(2x+t)(2y+u)
       =-3xy+3tu.
 \tag{5}
\]

Consequently N={(0,t):t in R} has dimension one and
Q((0,t),(0,t))=3t^2>0 for t!=0. Every point of the fiber Rv=x
is (x,t), whose energy is -3x^2+3t^2. Its unique global minimum
occurs at t=0, so f_x=(x,0). For h=(0,t) in N, (5) proves

\[
 Q(f_x,h)=0,\qquad
 Q(f_x+h,f_x+h)-Q(f_x,f_x)=3t^2=Q(h,h).
 \tag{6}
\]

This verifies genuine fiber minimality and the entire stationarity
condition, not just one tested variation. It does not assert that
the minimum is nonnegative.

### The prescribed right inverse and its compression

Here G_+f_x=x, G_-f_x=2x and Lf_x=(2x,x,-2x).
Thus G_+f_1=1 and (2) is exactly

\[
 Ey=(2y,y,-2y),\quad CEy=y,\quad KEy=(y,0,y),
 \quad CKEy=2y.
 \tag{7}
\]

In particular EG_+f_x=Lf_x and CKEG_+f_x=G_-f_x for every x.
These are the required identities on the whole minimizing trace
image, which maps onto O. They are not asserted on all of V.
Equation (7) proves ||CKE||=2 exactly, while
Q(f_1,f_1)=1^2-2^2=-3. On the trace image the positive-profile
Gram is P=1, and the negative-profile Gram is M=4, so the required
M<=P fails by exactly 3.

### Closure hypotheses do not remove the failure

Take the core to be all of V. The graph norm used in the audited
passage has the exact expression

\[
 \|v\|_{\mathrm{graph}}^2
 =|G_+v|^2+|G_-v|^2+|Rv|^2
 =6x^2+8xt+5t^2
 =6(x+2t/3)^2+(7/3)t^2.
 \tag{8}
\]

It is positive definite, hence an equivalent complete norm in
dimension two. The core is dense, R is continuous, and N is closed.
All displayed maps and bilinear forms are continuous, since their
matrices are finite. Define the algebraic boundary form
B(v,w)=(G_+v)(G_+w)-(G_-v)(G_-w). Then B=Q on the core and its
completion, and B(f_x,h)=0 for every h in N by (6). This verifies
the displayed abstract boundary-form conditions; it does not claim
an additional theta integration-by-parts identity.

The obstruction is cancellation after integration: CE1=2+1-2=1,
whereas CKE1=1+0+1=2. Positivity of the weights in C does not make
integration preserve the lifted multiplier's norm bound when the
lifted profile changes sign. Orthogonality against N only eliminates
the fiber cross term; it leaves the trace minimum in (5) unrestricted
in sign. In this model E^*K^*C^*CKE=4I_O, so an independent bound
of this operator by I_O is exactly what the claimed compression lacks.
A theta-specific structural estimate may provide such a bound; the
abstract completion and stationarity premises alone do not.

The exact-arithmetic replay is
`python3 scripts/green-lift/compression-countermodel-1265.py`.
Its full rational certificate is
`scripts/green-lift/compression-countermodel-1265.json`.
The proof above is independent of that replay and checks all parameters
and variations symbolically. No floating-point evidence is used.

## Mathlib

Full matching and supporting Mathlib coverage has not been checked.
No absence claim or Lean verification is made. The argument consists
of the explicit matrix products, one quadratic minimization and
finite-dimensional continuity proved above; no formal library theorem
is used as an unverified substitute for a hypothesis.
