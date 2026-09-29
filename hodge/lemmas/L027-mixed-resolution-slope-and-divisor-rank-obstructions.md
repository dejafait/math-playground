# L027 — Slope and divisor-rank tests for mixed resolutions

## Hypotheses

Use the very general cubic surface S and correspondence C in X=S x S
of L026. Write N=NS(S)_Q, T=N^perp and q for the cup pairing. Thus
the mixed degree-four action of [C] is U on T and 2 id on N, and
U sigma=lambda sigma, where

\[
f(\lambda)=0,\qquad f(z)=z^3+z^2-2z-1,\qquad
\lambda=2\cos(2\pi/7).
\]

Fix the pair (A,omega) constructed in L025, with characteristic
polynomial z f(z), A omega=lambda omega and omega ample. Equip both
factors with this same hyperkahler metric. Let Omega=p_1^*omega+p_2^*omega
and use the diagonal SU(2) action. Set W=im(A) and K=ker(A); then
N=W orthogonal direct sum K, with dim_Q W=3 and dim_Q K=1.
Let pi_W denote the rational orthogonal projection onto W.

Suppose there is an actual exact sequence, for an integer m>=1,

\[
0\longrightarrow E\longrightarrow P_{m-1}\longrightarrow\cdots
\longrightarrow P_0\longrightarrow I_C\longrightarrow0,
\qquad P_i=\bigoplus_{j=1}^{n_i} L_{ij},                 \tag{1}
\]

where the L_{ij} are holomorphic line bundles and E is locally free
of positive rank r. Existence, exactness and stability of arbitrary
choices of these terms are not assumed. Write

\[
c_1(L_{ij})=p_1^*a_{ij}+p_2^*b_{ij},\qquad a_{ij},b_{ij}\in N,
\]

using Kunneth and H^1(S,Q)=0. Define

\[
\begin{aligned}
s_i&=(-1)^{m-1-i},& e&=(-1)^{m+1},\\
a&=\sum_{i,j}s_i a_{ij},& b&=\sum_{i,j}s_i b_{ij},\\
V_1&=\operatorname{span}_{\mathbb Q}\{a_{ij}\},&
V_2&=\operatorname{span}_{\mathbb Q}\{b_{ij}\}.
\end{aligned}                                                     \tag{2}
\]

Let M be any holomorphic line bundle on X, put F=E tensor M and
write c_1(M)=p_1^*t_1+p_2^*t_2. For a torsion-free sheaf G, use
deg_Omega(G)=integral_X c_1(G) Omega^3 and
mu_Omega(G)=deg_Omega(G)/rank(G).

## Conclusion

If F is slope-stable for Omega and c_1(F),c_2(F) are both
SU(2)-invariant, the following necessary conditions hold.

1. The rank r is at least two, mu_Omega(F)=0, and at least r+1 of
   the terminal summands L_{m-1,j} tensor M have strictly positive
   degree. Every component of F's terminal inclusion into a
   nonpositive-degree summand is zero. In particular no untwisted
   stable terminal bundle with only anti-ample terminal summands
   has invariant c_1.
2. Both dim_Q V_1 and dim_Q V_2 are at least three. Thus every
   resolution with at most two independent original divisor classes
   in either factor fails the invariant-Chern requirement after
   every line-bundle twist, even without assuming stability.
3. If all a_{ij},b_{ij} lie in W, the required mixed divisor
   correction is completely determined. As an operator on N it is

\[
R=e(A-2\,\mathrm{id})\pi_W,\qquad
R(v)=\sum_{i,j}s_i q(v,a_{ij})b_{ij}-\frac1r q(v,a)b.       \tag{3}
\]

   Moreover an invariant c_1(F) requires

\[
\pi_W(t_1)=-a/r,\qquad \pi_W(t_2)=-b/r.                    \tag{4}
\]

These are conditions on actual terms and an actual integral line-bundle
twist. They do not construct maps or prove that such a twist exists.
The ch_2 action of F on T is always eU; in particular it is U for
the three-presentation stable-resolution recipe. No stable bundle,
transverse lift or new algebraic Hodge class is constructed. The known
span remains 21-dimensional, with three attained RM directions against
four required. Other compatible bundles and the universal goal remain open.

## Proof

**Known inputs and scope.** Reuse the inspected morphism vanishing for
slope-semistable sheaves on a compact Kahler manifold: if mu(G)>mu(H),
then Hom(G,H)=0. A precise read statement is McCarthy,
*Stability conditions and canonical metrics*,
[arXiv:2302.04966v1, Proposition 2.2.4(i), printed p. 20](https://arxiv.org/pdf/2302.04966v1#page=36),
attributed there to Kobayashi, Proposition 5.7.11 and Corollary 5.7.12.
No extra claim from the unread original book is used. The equality
case needed below follows directly from stability, as shown below.

For the invariant-form framework use Verbitsky, *Hyperholomorphic
bundles*, [arXiv:alg-geom/9307008v1, Proposition 1.2 and Lemma 2.1,
pp. 4 and 7](https://arxiv.org/pdf/alg-geom/9307008v1#page=7).
Invariant degree-two classes are primitive for the induced Kahler
forms. The stable-bundle implication of
[Theorem 2.5, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9)
does not itself supply the bundle or its invariant Chern classes.
The following tests are an application of these known inputs and
L026's Chern calculation, classified as REPRODUCTION. No originality
claim or new general stability theorem is made.

**Chern signs and twisting.** Exactness of (1) gives

\[
[E]=\sum_i s_i[P_i]+(-1)^m[I_C],\qquad
r=\sum_i s_i n_i+(-1)^m.                                  \tag{5}
\]

The leading Chern character of the ideal is ch(I_C)=1-[C] through
degree four, including its three non-lci points, as justified in L026.
Consequently

\[
\begin{aligned}
c_1(E)&=p_1^*a+p_2^*b,\\
\operatorname{ch}_2(E)&=e[C]+\frac12\sum_{i,j}s_i c_1(L_{ij})^2.
\end{aligned}                                                    \tag{6}
\]

Every divisor product acts trivially on T. Twisting contributes only
such products, so ch_2(F)|_T=eU. If r=1, F is itself a line bundle
and ch_2(F)=c_1(F)^2/2 has zero action on T. Since eU is nonzero,
this is impossible. Thus every (1) with a positive-rank locally free
terminal object already has r>=2.

Use the normalized character

\[
\nu(E)=\operatorname{ch}_2(E)-\frac{c_1(E)^2}{2r}.
\]

The splitting-principle identities
c_1(F)=c_1(E)+r c_1(M) and
ch_2(F)=ch_2(E)+c_1(E)c_1(M)+r c_1(M)^2/2 show directly that
nu(F)=nu(E). Since
nu(F)=(r-1)c_1(F)^2/(2r)-c_2(F), invariance of the two Chern
classes implies invariance of nu(E). This retains every final twist.

**Invariant c_1 and the actual terminal inclusion.** On a K3 surface
the invariant subspace of H^2(R) is the orthogonal complement of the
three Kahler forms. In particular a rational divisor class d is
invariant exactly when q(d,omega)=0: it is already orthogonal to
the real and imaginary parts of sigma. The two Kunneth summands of
H^2(X) are separately preserved by the diagonal action. Thus
invariance of c_1(F) gives

\[
q(a+rt_1,\omega)=q(b+rt_2,\omega)=0.
\]

In particular its Omega degree is zero; the implication to degree
zero also follows from invariant-form primitivity. Explicitly, for
any divisor d=p_1^*d_1+p_2^*d_2,

\[
\deg_\Omega(d)=3q(\omega,\omega)
                     \bigl(q(d_1,\omega)+q(d_2,\omega)\bigr).       \tag{7}
\]

The two separate orthogonality conditions are stronger than their
sum in (7); no converse from degree zero to invariance is used.

Suppose F is stable and let L be a line bundle of degree <=0.
Negative degree gives Hom(F,L)=0 by the cited slope criterion.
For completeness the same conclusion at degree zero follows without
an equality-case theorem. A nonzero map has a rank-one torsion-free
image J inside L and a kernel B of rank r-1. Stability and deg(F)=0
give deg(B)<0, hence deg(J)=-deg(B)>0. But the divisorial part of
L/J is effective, so deg(J)<=deg(L)<=0, a contradiction. This
also proves the negative-degree case directly. Positivity of the
degree of a nonzero effective divisor holds for the Kahler form
Omega even though it need not be rational.

Twist the actual terminal inclusion in (1). Write its target as
Q direct sum Q_0, where Q is the sum of its strictly positive-degree
line summands and Q_0 contains all the others. The preceding vanishing
makes the map factor through Q. Its cokernel in the whole target is
torsion-free: before twisting it is the image in P_{m-2} if m>=2,
and is I_C if m=1. Therefore Q/F is torsion-free too, since

\[
(Q\oplus Q_0)/F=(Q/F)\oplus Q_0.
\]

Generic injectivity gives rank(Q)>=r. If equality held, Q/F would
be a rank-zero torsion-free sheaf on the integral X and hence zero.
Then F=Q, contradicting deg(F)=0 and deg(Q)>0. Thus rank(Q)>=r+1.
Anti-ample line bundles have negative degree for every Kahler class,
so the untwisted anti-ample case has Q=0 and is excluded.

For a general twist the exact necessary sign test is

\[
\#\{j:\deg_\Omega(L_{m-1,j})>\mu_\Omega(E)\}\ \ge r+1.             \tag{8}
\]

Indeed invariance of c_1(F) forces deg_Omega(M)=-mu_Omega(E).
Equation (8) does not say that a twist satisfying that numerical
identity exists, or that positive-degree target lines force stability.
It explains why the untwisted exclusion alone cannot reject all twists.

**The cubic action requires at least three divisor dimensions.**
Under the cup-pairing identification a mixed tensor x tensor y acts
by v -> q(v,x)y. Equations (2) and (6) identify the mixed divisor
part of nu(E)-e[C] with

\[
\sum_{i,j}s_i a_{ij}\otimes b_{ij}-\frac1r a\otimes b
\ \in V_1\otimes V_2.                                      \tag{9}
\]

Its operator is R in (3), with rational rank at most
min(dim V_1,dim V_2). It factors through V_1^* and has image in V_2;
this rank statement does not require either subspace to be nondegenerate.

The full correspondence action computed in L026 gives

\[
T_{\nu(E)}|_T=eU,\qquad T_{\nu(E)}|_N=2e\,\mathrm{id}+R.           \tag{10}
\]

If nu(E) is invariant, its operator commutes with the diagonal
SU(2) action. Rotating Re(sigma) to a nonzero multiple of omega
therefore forces

\[
R\omega=e(\lambda-2)\omega.                                \tag{11}
\]

This uses the full mixed tensor; the two point-class Kunneth
summands cannot change the operator. It does not assume that R
is self-adjoint or infer invariance merely from Hodge type.

The polynomial f is irreducible over Q: its only possible rational
roots are +/-1, and neither is a root. Thus

\[
f(z+2)=z^3+7z^2+14z+7
\]

is irreducible, and the nonzero number e(lambda-2) has degree three.
Let J=im(R), a rational R-invariant subspace. By (11), omega lies
in J_R, since e(lambda-2) is nonzero. The rational operator R|_J
has that eigenvalue, so its characteristic polynomial is divisible
by its degree-three minimal polynomial. Therefore dim_Q J>=3.
Combining this with (9) proves the lower bounds on V_1 and V_2.
Because nu is unchanged by M, these bounds concern the original
presentation terms even when the twisting class is outside their spans.

**The smallest L025 subspace fixes the correction.** Now assume all
a_{ij},b_{ij} lie in W. The characteristic polynomial z f(z) and
self-adjointness of A give a nondegenerate orthogonal decomposition
N=W orthogonal direct sum K. The restriction A|_W has irreducible
characteristic polynomial f, and omega belongs to W_R.

No nonzero rational linear functional on W annihilates omega.
Indeed the space of such functionals is invariant under the dual
of A|_W, since A omega=lambda omega. Irreducibility leaves only
the zero subspace or all of W^*. The latter is impossible because
omega is nonzero. In particular any rational map on W is determined
by its value at omega when such a prescribed value is attained.

Equation (9) makes R vanish on K and have image in W. The rational
map R-e(A-2 id)pi_W kills omega by (11). The previous paragraph
applied to each row of its restriction to W makes that restriction
zero; both maps also vanish on K. This proves (3).

Likewise, a rational x in W with q(x,omega)=0 is zero, since q|_W
is nondegenerate. Apply this to the W components of a+rt_1 and
b+rt_2. Orthogonality of K and W and the invariant-c_1 conditions
give exactly (4). This is a rational projection condition on an
integral twisting class, not permission to divide a line bundle by r.

**What has and has not been excluded.** The untwisted anti-ample
case fails already at the inclusion. A twist cannot rescue a
presentation with dim V_1<=2 or dim V_2<=2. Presentations with larger
spans and at least r+1 positive twisted terminal terms have not been
constructed or ruled out. For the specified minimal subspace W,
(3)--(4) replace free formal tensor choices by exact necessary equations.
Solving them alone would still leave the maps, exactness, integral
twist, stability and eventual transverse transport to prove.

Mistretta's [Theorem 3.1, arXiv:math/0310185v2, pp. 7--9](https://arxiv.org/pdf/math/0310185v2#page=7)
supplies the known three-presentation single-polarization construction,
not existence of the mixed data here. L026 already rejects that
case; the new exclusion includes two-dimensional factor spans and
the slope constraint on mixed terms. L012 concerns two specified
sufficiently negative presentations and their map-recovery Ext
vanishings. Those hypotheses are not inferred for (1), and no new
map-recovery or deformation-kernel assertion is made in this proof.

## Mathlib

Coverage of the full statement: **not checked**. No Mathlib declaration
or absence from checked Mathlib sources is asserted. McCarthy
Proposition 2.2.4(i) supplies the inspected Kahler slope criterion;
Verbitsky Proposition 1.2 and Lemma 2.1 supply invariant-form facts;
Theorem 2.5 is the conditional bundle criterion. Their direct links
appear above. Mistretta Theorem 3.1 supplies only the named construction
in its own scope. None is cited as a full match for these mixed-resolution
restrictions. Kunneth, the splitting principle, positivity of effective
divisors against a Kahler class, and the rational minimal-polynomial
dimension bound are the other standard inputs used in the proof.
