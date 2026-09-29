# L029 — Necessary Chern equations for the doubled source

## Hypotheses

Use S, X=S x S, C, N=NS(S)_Q, q, U, A and omega from L027.
Write W=im(A), K=ker(A), and pi_W, pi_K for the orthogonal
projections. The characteristic polynomial of A is z f(z), where
f(z)=z^3+z^2-2z-1, and A omega=lambda omega with f(lambda)=0.
Both factors use L025's same metric and its diagonal SU(2) action.

Suppose there is an actual exact sequence

\[
0\longrightarrow E\longrightarrow P_2\longrightarrow P_1
 \longrightarrow P_0\longrightarrow I_C\oplus I_C\longrightarrow0,
\qquad P_i=\bigoplus_j L_{ij},                              \tag{1}
\]

with E locally free of positive rank r, and actual product line bundles
having factor classes a_{ij},b_{ij} in W. Put s_0=s_2=1, s_1=-1 and

\[
a=\sum_{i,j}s_i a_{ij},\qquad b=\sum_{i,j}s_i b_{ij},\qquad
Q=\sum_{i,j}s_i a_{ij}\otimes b_{ij}.
\]

Let M be an actual line bundle with factor classes t_1,t_2 in NS(S),
and set F=E tensor M. Assume c_1(F) and c_2(F) are SU(2)-invariant.
Stability is not assumed for the necessary conditions below.

## Conclusion

The rank and first Chern classes satisfy

\[
r=\operatorname{rk}P_2-\operatorname{rk}P_1+\operatorname{rk}P_0-2,
\quad
\alpha=a+rt_1\in K,\quad\beta=b+rt_2\in K.                 \tag{2}
\]

Let B denote the tensor whose correspondence operator on N is
2(A-2 id)pi_W. Then

\[
\pi_W(t_1)=-a/r,\quad\pi_W(t_2)=-b/r,\qquad
Q=B+r\,\pi_W(t_1)\otimes\pi_W(t_2).                       \tag{3}
\]

In particular the right side must belong to
Lambda_W tensor_Z Lambda_W, where Lambda_W=W intersect NS(S).
This is a necessary integral tensor condition, not just preservation
of the divisor lattice by an associated rational operator.

The mixed ch_2(F) operator on N is

\[
D=2A+\gamma\pi_K,\qquad
\gamma=4+q(\alpha,\beta)/r\in2\mathbb Z,\qquad
\det(z-D)=(z^3+2z^2-8z-8)(z-\gamma).                      \tag{4}
\]

Unlike L028's single-source polynomial, (4) has no contradiction
from the coprime cubic/linear argument modulo 2 when gamma is even.
The explicit pre-chamber model of L025 even admits an integral tensor
B with t_1=t_2=a=b=0, realized by a signed sum of actual product line
bundle classes in K_0(X). This last assertion is only a formal Chern
calculation in that model. It supplies neither (1), an integral solution
for an arbitrary final chamber conjugation, nor a stable terminal bundle.

Thus the doubled target remains unresolved. These necessary equations
and the formal example are an exploration result, not a new algebraic
class, a transverse lift, or an existence theorem. The attained span
is still 21-dimensional, with three RM directions against four required.

## Proof

**Known inputs and scope.** Chern additivity is imported from the
Stacks Project, [Lemma 42.45.2, tag 0F9C](https://stacks.math.columbia.edu/tag/0F9C),
and its extension to perfect K-groups from
[Remark 42.56.11, tag 0FET](https://stacks.math.columbia.edu/tag/0FET).
Use the invariant-form framework inspected in Verbitsky,
*Hyperholomorphic bundles*, [Proposition 1.2 and Lemma 2.1,
arXiv:alg-geom/9307008v1, pp. 4 and 7](https://arxiv.org/pdf/alg-geom/9307008v1#page=7).
[Theorem 2.5, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9)
requires an existing stable bundle and supplies no presentation here.
The saved EXPLORE assessment is reused; this is a reproduction of
the Chern and invariant-form tests for the changed source, with no
originality claim. Only the changed multiplicity and its consequences
are calculated, rather than re-proving the supporting theorems.

**Chern signs and the forced tensor.** Additivity in (1) gives

\[
[E]=[P_2]-[P_1]+[P_0]-2[I_C],\quad
c_1(E)=p_1^*a+p_2^*b,\quad
\operatorname{ch}_2(E)=2[C]+\frac12\sum_{i,j}s_i c_1(L_{ij})^2.
                                                               \tag{5}
\]

Here ch(I_C)=1-[C] through degree four, including its singular points,
and [C] acts by U on T and 2 id on N, as established in L026.
The normalized character

\[
\nu(E)=\operatorname{ch}_2(E)-c_1(E)^2/(2r)
\]

is unchanged by twisting. The same splitting-principle calculation
as in L027 gives nu(F)=nu(E). The first Chern class conditions imply
q(alpha,omega)=q(beta,omega)=0 separately in the two factors. L027
proves that a rational vector in W orthogonal to omega is zero.
Consequently alpha,beta belong to K, proving (2) and the first two
equations in (3).

The mixed divisor correction Q-a tensor b/r lies in W tensor W;
its operator R kills K and has image in W. Invariance of nu(E),
together with its action 2U on T, forces

\[
(4\,\mathrm{id}+R)\omega=2\lambda\omega.
\]

Thus R omega=2(lambda-2)omega. The rational-functional argument
in L027 says that a rational map on W is determined by its value
at omega. Comparing with 2(A-2 id)pi_W proves

\[
R=2(A-2\,\mathrm{id})\pi_W,\qquad Q-a\otimes b/r=B.
\]

Substituting a=-r pi_W(t_1) and b=-r pi_W(t_2) proves (3).
Every original factor class is an actual integral class in W, so
Q belongs to the stated integral tensor lattice. Conversely, merely
writing an element of that lattice as a signed sum of simple tensors
does not enforce the first moments a,b, the rank, or any exact maps.

**Integral spectrum and what reduction modulo 2 now says.** On N the
operator of nu(F) is 2A+4pi_K. The mixed part of c_1(F)^2/(2r) is
alpha tensor beta/r. Since alpha,beta lie on the nondegenerate line K,
its operator is q(alpha,beta)pi_K/r. This proves the rational formula
for D in (4), including self-adjointness.

The integral Kunneth and Lefschetz (1,1) argument of L028 applies to
any actual F on this product: its mixed ch_2 is
alpha tensor beta minus the integral mixed c_2, so D preserves NS(S).
In particular gamma=tr(D)+2 is an integer. Scaling the roots of f
by two gives 8 f(z/2)=z^3+2z^2-8z-8, proving the characteristic
polynomial in (4).

The divisor lattice has L028's even Gram form of determinant -7.
Modulo 2 it is nondegenerate alternating. If gamma were odd, the
reduced characteristic polynomial would be z^3(z-1). Its coprime
primary factors give orthogonal spaces of dimensions three and one,
by self-adjointness exactly as in L028. The one-dimensional space
would be a degenerate orthogonal summand, a contradiction. Hence
gamma is even. For even gamma the characteristic polynomial is z^4;
there are no distinct primary factors to which that contradiction
can be applied. This is not a sufficiency claim for any integral data.

**An integral formal example, confined to the pre-chamber model.**
Use the integral basis (F,O,E,P) and G of L025 and L028. To avoid
confusion, E in this basis is the exceptional divisor class. L025's
pre-chamber operator is

\[
A_0=\begin{pmatrix}
1&2&-2&5\\
1/2&0&-1&3/2\\
1/2&0&-2&2\\
0&0&0&0
\end{pmatrix}.
\]

Here W_0=span_Q(F,O,E), and K_0 is generated by
k=(-4,-2,1,2), of square -14. Since q(k,x)=-7x_P,
pi_{K_0}(x)=x_P k/2. Represent a tensor by its coefficient matrix
in the displayed basis; the symmetric tensor below has operator B_0 G.
Direct exact multiplication gives

\[
B_0=\begin{pmatrix}
0&-2&2&0\\
-2&1&1&0\\
2&1&4&0\\
0&0&0&0
\end{pmatrix},\qquad
B_0G=2(A_0-2\,\mathrm{id})\pi_{W_0}.                       \tag{6}
\]

All entries are integral and all factors lie in Lambda_{W_0}.
Moreover

\[
D_0=4\,\mathrm{id}+B_0G
=2A_0+4\pi_{K_0}
=\begin{pmatrix}
2&4&-4&2\\
1&0&-2&-1\\
1&0&-4&6\\
0&0&0&4
\end{pmatrix}.                                               \tag{7}
\]

It is integral and q-self-adjoint, has the polynomial (4) with
gamma=4, and its reduction modulo 2 has square zero and rank two.
Thus an actual integral matrix passes this isolated lattice test.

There is also an exact signed-line-class construction with zero first
moments, so (6) is not merely a rational decomposition. For integral
divisor classes x,y in W_0, let L(x,y) be the actual product line bundle
with these factor classes, and put, in K_0(X),

\[
\Delta(x,y)=[L(x,y)]-[L(x,0)]-[L(0,y)]+[O_X].
\]

It has rank zero and c_1=0. Expanding exp(p_1^*x+p_2^*y) shows
that its entire degree-four character is x tensor y; its two pure
point-class components vanish. Writing e_1=F,e_2=O,e_3=E, set

\[
V_r=(r+2)[O_X]+\sum_{i,j=1}^3(B_0)_{ij}\Delta(e_i,e_j)-2[I_C].
                                                               \tag{8}
\]

For every positive integer r this is an integral virtual class of rank
r, with c_1(V_r)=0 and ch_2(V_r)=2[C]+B_0. It uses the actual trivial
line bundle as twist, and solves (2)--(3) at the level of these formal
moments in the pre-chamber model. The coefficients in (8) are signed;
they are not maps or a locally free representative of the required rank.
No stability test is asserted for V_r.

Finally, if L025's final A is g A_0 g^(-1), its required correction
tensor is g B_0 g^T. The allowed g is rational and need not be integral.
Neither its coefficient integrality nor the tensor-lattice condition
in (3) follows from (6). No claim that the initial eigenvector is
already Kahler on S is used. Passing this model test therefore leaves
the actual final lattice, twist, presentation maps and stability open.

Run `python3 scripts/cubic-kahler/check_doubled_source_chern.py` for
the exact matrix, polynomial and signed-line moment checks. The
geometric necessary-condition arguments are the proof above; the
computation cannot certify an exact resolution or a stable bundle.

## Mathlib

Coverage of the full statement: **not checked**. No full Mathlib match
or absence from checked sources is asserted. The directly linked Stacks
results support Chern additivity on actual exact sequences and virtual
classes; Verbitsky supports the invariant-form framework and a conditional
criterion for an existing stable bundle. None matches or constructs the
full doubled-source target. Integral Kunneth, Lefschetz (1,1), the
splitting principle and primary decomposition are supporting named
inputs, with their specific uses written out here.
