# L281 — Separated-support quadratic bound for the complete density response

## Hypotheses

Use L280's SU(2) relative box, with even N>=2, a=8/N, all links
contained in any boundary face pinned, boundary-fixed gauge group,
and every other link, including every normal end link, variable.
Use exactly L003's real nonnegative smooth f=f_* of integral one,
supported in K=[-1/4,1/4]^3 times [1,2], and h_+=f, h_-=theta f
on 12-plaquettes. Put F=||f||_infinity. Source derivatives are at
s=t=0 in L280's real domain (|s|+|t|)F<eta<1.

Let G, K_pm and G_-+ be L280(18)'s extended transverse covariance,
source matrices and mixed inverse derivative. Let D be exactly the
complete density matrix in L280(16), including the all-link Haar
term and BOTH gauge-coordinate determinant terms. Tr below includes
all three colors unless explicitly stated otherwise. All matrices
and sums are finite and use Euclidean counting measure.

## Conclusion

Let C_a(theta z,w) denote the one-color reflected curvature kernel
of L003, with its physical cochain normalization, and define

\[
 m_a=a^4\sum_{p\parallel12} f(z_p)C_a(\theta z_p,z_p).
 \tag{1}
\]

Then m_a>=0, it is uniformly bounded, and the full density response
satisfies

\[
 \boxed{\quad
 |\operatorname{Tr}(D G_{-+})|
 \le \frac{241}{8}F N^2 m_a=O_f(N^2).
 \quad}                                                     \tag{2}
\]

In particular the proposed normalized responses N^-2 Tr(D G_-+)
form a bounded real sequence. This removes the sqrt(log(eN)) loss
in L280(28); it does NOT establish their convergence, nonvanishing,
sign, a matching lower bound, or an O(log N) estimate. The leading
mesh scale remains undetermined. No claim concerns cancellation with
the action/insertion terms, uniform higher errors, continuum axioms,
or a positive physical mass. This is a local specialization within
the prior EXPLORE assessment, not a certified originality claim. The
separate critical audit in section 5 accepts this bound and its tail.

## Proof

### 1. The separated curvature matrix has bounded trace norm

Suppress color until section 3. Write C for the complete relative
plaquette incidence and G for its transverse inverse as in L280.
Let P_+ be the set of retained 12-plaquettes where h_+>0 and
P_-=theta P_+. These sets are disjoint because the source times
belong respectively to [1,2] and [-2,-1]. Reflection is a bijection
on these grids for even N. If the sets are empty, both source
matrices vanish and (2) follows immediately. Otherwise let C_pm
be the rows of C indexed by P_pm and W_pm the diagonal matrices
with entries sqrt(h_pm). Put

\[
 T=W_- C_- G C_+^* W_+ :\mathbb R^{P_+}\longrightarrow
                                    \mathbb R^{P_-}.
 \tag{3}
\]

Let S: R^{P_+}->R^{P_-} be the orthogonal permutation sending
p to theta p. The 12-curvature is even under time reflection, so
there is no orientation sign in this identification.

The exact normalization of the one-color curvature covariance is

\[
 (C_- G C_+^*)_{\theta p,q}=a^4 C_a(\theta z_p,z_q).
 \tag{4}
\]

Indeed in the quadratic law x=aA, while C is unscaled incidence
and d=C/a. Thus Cx=a^2 dA. L003's orthogonal quotient law and
L280(23) give the same curvature covariance: the longitudinal
piece disappears on multiplication by C. This identifies only
quadratic curvature, without transporting a nonlinear jet or
replacing G by componentwise scalar Dirichlet inverses.

L003 section 3 gives the exact separated factorization
C_a(theta z,w)=sum_k b_(k,a) psi_(k,a)(z) psi_(k,a)(w), with
b_(k,a)>0, over its finite relative spatial mode set. Consequently

\[
 S^*T=a^4\sum_k b_{k,a} v_{k,a}v_{k,a}^*,\qquad
 (v_{k,a})_p=\sqrt{f(z_p)}\,\psi_{k,a}(z_p),
 \tag{5}
\]

is positive semidefinite. Here the midpoint cosine modes in the
first two directions, the vertex sine modes in the third direction,
and the exact reflected Dirichlet time kernel are those already
proved in L003; no continuum replacement is made. Since left
multiplication by S preserves singular values, the trace norm is
exactly

\[
 \|T\|_1=\operatorname{Tr}(S^*T)=m_a.
 \tag{6}
\]

This uses positivity of the reflected linear curvature matrix,
not positivity of the density response or of the interacting theory.

For an explicit mesh-independent upper bound, L003 section 4 gives
on K times K

\[
 |C_a(\theta z,w)|\le C_{\rm sep},\qquad
 C_{\rm sep}:=\frac{\pi}{512(1-e^{-2})}
 \sum_{\substack{k_1,k_2\ge0,\ k_3\ge1\\(k_1,k_2)\ne(0,0)}}
 |k|e^{-|k|/4}<\infty.
 \tag{7}
\]

The sum is finite by exponential decay and polynomial shell count;
it dominates every finite-mesh mode sum. There are at most N^4
retained 12-plaquettes. Hence

\[
 0\le m_a\le C_{\rm sep}a^4\sum_p f(z_p)
          \le 8^4 F C_{\rm sep}.
 \tag{8}
\]

There is no coincident-time covariance in (1): theta z_p and z_p
are separated by at least two physical time units. The coincident
matrix index after reflection does not introduce a short-distance
singularity.

### 2. Control of the complete internal sandwich on the exact domain

Define U_pm=G C_pm^* W_pm, mapping source plaquettes to all relative
edges. Then K_pm=C_pm^* W_pm^2 C_pm. On H=ker B*, C is injective
and G=(C^*C|_H)^-1; on im B it is zero. It follows that C G C^*
is the orthogonal projection onto im C. Explicitly, with Q an
orthonormal inclusion of H and A=CQ, it equals A(A^*A)^-1 A^*.
Thus every row compression C_pm G C_pm^* is between zero and the
identity. Since G^2<=||G|| G as positive matrices,

\[
 \|U_\pm\|^2
 =\|W_\pm C_\pm G^2 C_\pm^*W_\pm\|
 \le F\|G\|.
 \tag{9}
\]

For completeness the spectral bound needed here follows directly
from L280(21)–(23), using the relative modes of L003. Every one-form
mode has three strictly positive vertex indices and one nonnegative
edge index. Thus |k|^2>=3 and
lambda_k>=4|k|^2/N^2>=12/N^2. The transverse subspace is invariant
under L=C^*C+BB^*, and G is its inverse extended by zero, so

\[
 \|G\|\le N^2/12,\qquad
 \|U_\pm\|\le \sqrt{F/12}\,N.
 \tag{10}
\]

In particular the sectors with the edge index zero are retained.
The midpoint edge modes run through both normal endpoints.

The complete D, without separating or omitting either determinant
term, obeys L280(25)'s uniform estimate

\[
 D_{ef}=-\left(\frac1{12}+\frac{(B\Delta^{-1}B^*)_{ee}}6\right)
             \delta_{ef}
       +\frac14(M\Delta^{-1}B^*)_{ef}(M\Delta^{-1}B^*)_{fe},
 \qquad \|D\|\le241/4.
 \tag{11}
\]

This estimate applies on the full relative edge set, with boundary
vertex variables extended by zero. In particular a boundary tail has
the B row -u_head and M row u_head; a boundary head has B row u_tail
and M row u_tail. Both signs and their resulting matrix entries
are retained in (11).

Let V=U_+^* D U_- : R^{P_-}->R^{P_+}. Equations (9)–(11) imply

\[
 \|V\|\le \frac{241}{48}F N^2.                \tag{12}
\]

This bounds every internal summation anchor simultaneously. More
explicitly V_(q,p)=sum_(e,f) (U_+)_(e,q) D_(e,f) (U_-)_(f,p),
where e,f include all interior and normal links, all diagonal and
near-diagonal pairs, boundary layers and face intersections. No
internal index is assumed separated from a source. The finite-domain
norm bounds (9)–(12) require neither pointwise domination of these
individual summands nor a boundary error estimate: no domain has
been changed and no limit has been passed through the anchor sums.

### 3. Both source orders and all three colors

The first inverse-derivative order factors exactly as

\[
 G K_-G K_+G=U_- T U_+^*.
 \tag{13}
\]

Finite-dimensional trace cyclicity, (6) and (12) give

\[
 |\operatorname{Tr}_{E}(D G K_-G K_+G)|
 =|\operatorname{Tr}_{P_+}(VT)|
 \le\|V\|\,\|T\|_1
 \le \frac{241}{48}F N^2m_a.
 \tag{14}
\]

The inequality follows directly from a singular-value expansion
T=sum_j sigma_j u_j v_j^*: the trace is
sum_j sigma_j v_j^* V u_j, whose absolute value is at most
||V|| sum_j sigma_j. This spells out its application to the
rectangular source matrices; it imports no new analytic theorem.
The second order G K_+G K_-G uses T^* and V^* and has the same
bound. In fact the traces are equal since D and G are real symmetric,
but both orders are present and counted. There are three independent
identical color blocks in G, K_pm and D. Multiplying (14) by two
orders and three colors yields 6(241/48)=241/8, proving (2).

### 4. Uniform tail reduction and exact scope of the bound

There is also a uniform finite-mode reduction for the same normalized
trace. For R>0 truncate (5) to |k|<=R and call the resulting rectangular
matrix T_R, so S^*T_R is the truncated positive sum. Define
C_sep(>R) by the sum in (7) restricted to |k|>R. The same diagonal
estimate proves

\[
 \|T-T_R\|_1\le8^4 F C_{\rm sep}(>R),\qquad
 C_{\rm sep}(>R)\longrightarrow0.
 \tag{15}
\]

For one color the two order traces are equal, as noted above. Thus
the actual three-color normalized density response has the exact
representation 6 N^-2 Tr(VT), and

\[
 \left|N^{-2}\operatorname{Tr}(DG_{-+})
             -6N^{-2}\operatorname{Tr}(VT_R)\right|
 \le\frac{241}{8}\,8^4 F^2 C_{\rm sep}(>R).
 \tag{16}
\]

This tends to zero with R uniformly over even N. A zero extension
for modes absent at a given N makes the truncation unambiguous.
In particular one may reduce a future convergence proof to the
finitely many scalars N^-2 a^4 b_(k,a) v_(k,a)^* V S v_(k,a)
at each fixed R, followed by (16). No convergence or sign of those
scalars is established here. This tail estimate concerns the external
separated modes only; D and its internal anchors are never truncated.

The gain over L280(28) comes from the separated reflected kernel's
trace norm in (6), in place of a global Hilbert–Schmidt estimate.
The density operator itself is still the complete finite-domain
operator. The upper bound allows a nonzero N^2 leading term, a
smaller scale, or bounded oscillation after N^-2 normalization.
Even convergence of the scalar m_a would not determine the limit
of N^-2 Tr(VT), since (12) only bounds the rescaled sandwich V.
Determining that sandwich on the separated mode vectors, including
its boundary-dependent density, remains part of the original target.

### 5. Separate input audit for L282 (2026-10-26)

**Verdict.** The complete bound (2) and uniform external tail (16)
pass the separate audit needed by L282. This checks the written proof
under its exact hypotheses; it adds no stronger bound or new input.

The normalization in (4) follows with no continuum limit: x=aA,
d=C/a, hence Cx=a^2 dA. The longitudinal covariance in L280(23)
drops out because CB=0. Thus the actual counting-measure curvature
covariance C G C* is a^4 times the physical point kernel C_a. The
12-curvature is even under time reflection, and reflection maps the
plus grid bijectively onto the minus grid. L003's coefficients b_{k,a}
are positive and its modes are real, including zero cosine indices.
Consequently S*T in (5) is positive semidefinite and its trace equals
the rectangular trace norm of T, proving (6). The same reasoning
applies to the positive mode tail T-T_R after multiplication by S*.

For completeness the imported majorant (7) has the required constant.
L003 gives gamma>=Omega/2>=|k|/8 and Omega<=pi|k|/8. Its factored
time kernel is bounded by
exp[-Omega(t+s)/2]/[Omega(1-e^-2)]. On [1,2]^2 this yields, after
alpha<=Omega^2 and |phi_k(x)phi_k(y)|<=1/64, the majorant
pi|k|exp(-|k|/4)/[512(1-e^-2)]. Its infinite index sum converges.
Each diagonal summand after reflection is nonnegative. There are
N^2(N-1)^2<=N^4 retained 12-plaquettes, so (8) and (15) follow also
for empty source sets and for modes absent at small N. In particular
the bound is separated in physical time, despite the diagonal index
in S*T; it is not an ultraviolet coincident-point estimate.

Let A=CQ for an orthonormal inclusion Q of the transverse space.
The relative closed-cochain result gives injectivity of A, so
C G C*=A(A*A)^-1 A* is an orthogonal projection on the full relative
plaquette space. Compression preserves the bounds zero and identity.
Since G^2<=||G||G, (9) follows. Every relative one-form eigenmode has
three positive indices and lambda>=4|k|^2/N^2, giving ||G||<=N^2/12.
Both normal endpoints and the zero cosine edge index are included.

The complete matrix D is exactly L280(16), not its diagonal part.
For L280's norm bound, counting-normalized relative eigenvectors have
square at most 16/N^4 and shells at most 15r^3 indices, with
lambda>=4r^2/N^2. Summing gives (L^-1)_ee<30 and the same diagonal
bound for Delta^-1. Positivity bounds all entries of Delta^-1 by 30.
Hence JJ* has diagonal at most 120, while J*J<=16L^-1 has diagonal
at most 480. Rowwise Cauchy–Schwarz bounds sum_f |J_ef J_fe| by
240. With 0<=P_ee<=1, this gives ||D||<=1/4+240/4=241/4.
Thus ||V||<=241 F N^2/48. Multiplication
of the definitions gives G K_- G K_+ G=U_- T U_+* on the full edge
space. Finite trace cyclicity works for these rectangular source maps.
Transposition, using symmetric real D and G, makes the two source-order
traces equal. Three color blocks give the total 6 Tr(VT), so
6(241/48)=241/8 proves (2). Replacing T by T-T_R gives exactly (16),
with no truncation of V, D, or any internal anchor. This also checks
that the second order cannot be omitted or counted twice again.

Only this finite-box estimate and its uniform external tail are
accepted here. It supplies no interacting remainder or continuum
positivity. Its sharper density asymptotic is the separate L282
statement, not a premise of the bound. No reverse mathematical input
or change to the existing DAG is introduced.

## Mathlib

Coverage of the full density-response estimate is **not checked**.
Finite-dimensional projection, positive-matrix, singular-value and
trace inequalities support the proof, but no matching Mathlib theorem
or formal verification is asserted. The exact kernel identities and
boundary conventions are imported from L003, and the full density
and spectral bounds from L280; no new external source is needed.
