# L044 — The doubled rank-two third-Chern constraint and a surviving chamber

## Hypotheses

Use S, X=S x S, C, N=NS(S)_Q, q, U, A and omega from L029.
Write W=im(A), K=ker(A). In this lemma write f_ell for the elliptic
fibre class on S, to distinguish it from the terminal bundle F.
Let eta be the point class on S, normalized by integral_S eta=1.
The two factors of X are identified with this same marked S.

Suppose the actual sequence and integral twist of L029 exist,

\[
0\longrightarrow E\longrightarrow P_2\longrightarrow P_1
 \longrightarrow P_0\longrightarrow I_C^{\oplus2}
 \longrightarrow0,\qquad F=E\otimes M,
\]

with rank(E)=2, all original integral factor classes a_ij,b_ij in
W, and invariant c_1(F),c_2(F). Stability is not assumed. With
s_0=s_2=1, s_1=-1, retain L029's first moments a,b and tensor Q.
Define the scalar and vector moments

\[
\begin{aligned}
S_1&=\sum s_i q(a_{ij},a_{ij}),&
T_1&=\sum s_i q(a_{ij},a_{ij})b_{ij},\\
S_2&=\sum s_i q(b_{ij},b_{ij}),&
T_2&=\sum s_i q(b_{ij},b_{ij})a_{ij}.
\end{aligned}
\]

All characters and equations below are in rational cohomology.
The final-chamber example is explicitly a virtual class, not an
instance of the actual sequence in these hypotheses.

## Conclusion

The singular support has the degree-six character

\[
\operatorname{ch}_3(O_C)
 =-(\eta\otimes f_{\rm ell}+f_{\rm ell}\otimes\eta).
\tag{1}
\]

All three double-point normalization corrections have zero component
in this degree. The rank-two identity c_3(F)=0 forces

\[
\begin{aligned}
T_1-(S_1/2+4)b-2Aa&=4f_{\rm ell},\\
T_2-(S_2/2+4)a-2Ab&=4f_{\rm ell}.
\end{aligned}
\tag{2}
\]

Under L029's mixed second-character equation, (2) is precisely the
vanishing of the normalized third character. It retains every actual
integral twist, including invariant nonzero c_1(F). In particular,

\[
f_{\rm ell}\in W
\tag{3}
\]

is necessary, independently of the residues of the factor classes.
Thus any final L025 chamber with pi_K(f_ell) nonzero excludes this
rank-two recipe before maps or stability are considered.

Condition (3) does not give a uniform exclusion over the final pairs
allowed by L025. There is an explicit integral chamber conjugation
retaining W=span_Q(f_ell,O,E_exc), with its eigenvector ample and
its doubled correction tensor integral. In that actual ample chamber,
an integral signed product-line class minus 2[I_C] has rank two,
invariant first two Chern classes, and c_3=0. This only certifies
compatibility of these necessary character equations; it supplies no
rank-two locally free bundle, exact maps, stability or deformation.

This is a negative test of a proposed uniform third-Chern obstruction,
using known character and Riemann--Roch tools, classified as
REPRODUCTION. No originality claim is made. The known span stays 21,
three RM directions are attained against four required, and the
universal rational Hodge conjecture remains unresolved.

## Proof

**Imported formulas and the normalization.** Import rank truncation
from Fulton, *Intersection Theory*, second edition,
[Theorem 3.2(a), pp. 50--52](https://djvu.online/file/87GFN2nbfbdF7),
and proper Grothendieck--Riemann--Roch between smooth varieties from
[Theorem 15.2, pp. 286--287](https://djvu.online/file/87GFN2nbfbdF7).
Use the character expansion in
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
tensor multiplicativity in
[Lemma 42.45.3, Tag 0F9D](https://stacks.math.columbia.edu/tag/0F9D),
and perfect-class additivity in
[Remark 42.56.11, Tag 0FET](https://stacks.math.columbia.edu/tag/0FET).
These supporting results were read in the completed third-Chern
assessment; their general statements are not reproved here.

Temporarily call the smooth normalization Y to avoid confusing it
with the divisor subspace W. L019's exact normalization sequence,
pushed to X, gives

\[
[O_C]=[j_*O_Y]-\sum_{\ell=1}^3[O_{p_\ell}],
\qquad j=(g_0,g_1):Y\longrightarrow X.
\tag{4}
\]

Each point sheaf starts in codimension four by the leading-character
formula (Fulton, Theorem 18.3(3),(5), pp. 353--354). None contributes
to ch_3. The map j is finite and proper, so its higher direct images
vanish. Its source and target are smooth by L008. Since c_1(T_X)=0,
the degree-six part of proper Riemann--Roch is

\[
\operatorname{ch}_3(j_*O_Y)=-\tfrac12j_*K_Y.
\]

Indeed the Todd degree-two term on Y is -K_Y/2, and the Todd
degree-two term on X is zero; higher Todd terms cannot enter this
component. L008 gives K_Y=g_0^*f_ell=g_1^*f_ell, and both g_i have
degree two. Hence (g_i)_*K_Y=2f_ell by the projection formula.
The only Kunneth summands of H^6(X,Q) are H^4(S) tensor H^2(S)
and H^2(S) tensor H^4(S), because a K3 has zero odd cohomology.
The two projection pushforwards determine their coefficients, giving
j_*K_Y=2 eta tensor f_ell+2 f_ell tensor eta. This proves (1),
retaining every singular correction in (4).

**Normalize the third character without a rational line twist.**
For a rank-two class G put

\[
\Psi_3(G)=\operatorname{ch}_3(G)
 -\tfrac12c_1(G)\operatorname{ch}_2(G)+\tfrac1{12}c_1(G)^3.
\tag{5}
\]

The cited character expansion identifies this with c_3(G)/2.
Equivalently it is the degree-six component of
exp(-c_1(G)/2) ch(G). Tensor multiplicativity and
c_1(E tensor M)=c_1(E)+2c_1(M) therefore give
Psi_3(F)=Psi_3(E). This is a cohomological normalization, not a
claim that half the determinant is an actual line bundle.
For an actual rank-two locally free F, rank truncation makes (5)
zero. No assumption c_1(F)=0 is needed.

Let c=p_1^*a+p_2^*b. Exactness and (1) give

\[
\begin{aligned}
\operatorname{ch}_2(E)&=2[C]+\tfrac12\sum s_i c_1(L_{ij})^2,\\
\operatorname{ch}_3(E)&=\tfrac12(\eta\otimes T_1+T_2\otimes\eta)
             -2(\eta\otimes f_{\rm ell}+f_{\rm ell}\otimes\eta).
\end{aligned}
\tag{6}
\]

Both outer degree-four coefficients of [C] are two, since its
projections have degree two. Its mixed operator on N is 2 id by
L026. Consequently

\[
c[C]=2\eta\otimes(a+b)+2(a+b)\otimes\eta.
\tag{7}
\]

Products with its transcendental tensor vanish here, by orthogonality
of N and T. Direct multiplication in (5) now gives the eta tensor N
coefficient of Psi_3(E) as

\[
\tfrac12T_1-\tfrac14S_1b-\tfrac12Q(a)
       +\tfrac14q(a,a)b-2(a+b)-2f_{\rm ell}.
\tag{8}
\]

Here Q(a) means the correspondence action of the tensor Q. L029
forces Q=B+a tensor b/2, with B's operator 2(A-2 id)pi_W.
Since a is in W, Q(a)=2(A-2 id)a+q(a,a)b/2. Substitution into
(8) cancels the q(a,a) term and the extra a term, yielding

\[
\tfrac12T_1-(S_1/4+2)b-Aa-2f_{\rm ell}.
\]

The factor-reversed coefficient is
T_2/2-(S_2/4+2)a-Ab-2f_ell. The symmetry used here belongs to
the forced B, since A is q-self-adjoint; it is not an assumption
on arbitrary presentation tensors. There are no other degree-six
components. This proves (2) and its equivalence with Psi_3(E)=0.
Every term on either left side of (2) lies in W. Projection onto K
therefore gives (3). Neither divisibility nor an integral splitting
of N was used.

**A permitted final ample chamber retains the fibre.** For this
example use L025's pre-chamber W_0=span_Q(f_ell,O,E_exc), A_0,
and the pairing G in the order (f_ell,O,E_exc,P). Put
R=f_ell-E_exc. Both E_exc and R are roots of square -2.
Their integral reflections are s_d(x)=x+q(x,d)d. Set

\[
g=s_Rs_{E_{\rm exc}}=
\begin{pmatrix}
1&1&-2&2\\0&1&0&0\\0&-1&1&-1\\0&0&0&1
\end{pmatrix}.
\tag{9}
\]

It is an integral q-isometry of determinant one. It preserves W_0,
fixes f_ell, and fixes its orthogonal complement generated by
k=(-4,-2,1,2). Thus this is a permitted conjugation in L025; no
assertion about an arbitrary previously fixed chamber is implied.

Let lambda be the positive root of f, so 1<lambda<3/2, and let
d=1+1/lambda, so 5/3<d<2. The vector
xi=(2lambda+4,d,1,0) satisfies A_0 xi=lambda xi. The first
coordinate equation is exactly f(lambda)=0 after multiplication
by lambda; the other two follow from d's definition. Its square
2d(2lambda+4-d)-2 is positive. Its image under (9) is

\[
\omega_c=(2\lambda+2+d,d,1-d,0).
\tag{10}
\]

We check the actual cone, not just positive square. Its intersections
with f_ell,E_exc,R,O are respectively
d, 2(d-1), 2-d, 2lambda+2-d, all positive. In L019's section
formula, omega_c has zero coefficient on the orthogonal Mordell--Weil
vector. For Q_j, with epsilon_j the parity of j, that formula gives

\[
q(\omega_c,Q_j)
 =2\lambda+2-d+\tfrac74d j^2+(1-3d/4)\epsilon_j>0.
\tag{11}
\]

For even j the extra term is nonnegative. For odd j, j^2>=1
makes it at least d+1, so (11) follows in both cases. L019 proves
that every irreducible negative curve is E_exc, R or one of these
sections. Since omega_c has positive square and pairs positively
with the nonzero nef isotropic fibre, it lies in the same positive
cone component as an ample class. Every remaining irreducible
curve has nonnegative square and lies in that component's closure,
so its pairing with omega_c is positive by Hodge index. The K3
Kahler-cone criterion used in L025 (Huybrechts, chapter 8, section
5.1/Theorem 5.2) now puts omega_c in the ample cone in N_R.

Set A_c=g A_0 g^{-1}. It is therefore an actual final pair permitted
by L025 with W=W_0, f_ell in W and A_c omega_c=lambda omega_c.
This calculation does not assume the pre-chamber eigenvector ample.

**Integral third moments survive in that chamber.** Let e_1=f_ell,
e_2=O, e_3=E_exc and u_i=g e_i. These are actual integral divisor
classes in W_0, with q(u_1,u_2)=1 and u_1=f_ell. Take L029's
integral correction tensor B_0, whose three by three block is

\[
\begin{pmatrix}0&-2&2\\-2&1&1\\2&1&4\end{pmatrix}.
\]

Then B_c=sum (B_0)_ij u_i tensor u_j is integral and its operator
is 2(A_c-2 id)pi_W. For actual product line bundles L(x,y), put
Delta(x,y)=[L(x,y)]-[L(x,0)]-[L(0,y)]+[O_X]. Consider

\[
V=4[O_X]+\sum_{i,j}(B_0)_{ij}\Delta(u_i,u_j)-2[I_C].
\tag{12}
\]

It has rank two, c_1=0 and ch_2=2[C]+B_c, including the two
pure point coefficients four. Its mixed operator is 2U on T and
2A_c+4pi_K on N. This q-self-adjoint operator is scalar 2lambda
on the metric's positive three-plane and preserves its orthogonal
complement. The diagonal SU(2) acts by rotations on that three-plane
and trivially on the complement, so the mixed class is invariant.
The point summands are invariant too. Hence c_1(V),c_2(V) are
invariant as classes; this is not a bundle existence assertion.

Expanding the characters of Delta in (12) gives

\[
\operatorname{ch}_3(V)=-(\eta\otimes y+y\otimes\eta),\qquad
y=2u_1+2u_2+5u_3=-6f_{\rm ell}+2O+3E_{\rm exc}.
\tag{13}
\]

For clarity, the vector in either half contributed by the Delta
sum is -2u_2-5u_3: it is half the contraction of B_0 with the
diagonal squares (0,-2,-2). The source contributes -2f_ell,
giving (13) with its sign fixed.

The integral signed class

\[
\Pi(x,z;y)=([L(x,0)]-[O_X])([L(z,0)]-[O_X])
                         ([L(0,y)]-[O_X])
\tag{14}
\]

has zero rank, first character and second character. Its leading
character is ch_3(Pi)=q(x,z) eta tensor y. This follows immediately
from the three exponential factors, each starting in degree two.
Let Pi_rev denote the same expression with the factors reversed;
its third character is q(x,z)y tensor eta. All terms after expanding
these products are signed actual integral product line bundles in W_0.
Thus

\[
V'=V+\Pi(u_1,u_2;y)+\Pi_{\rm rev}(u_1,u_2;y)
\tag{15}
\]

keeps rank, c_1 and ch_2 unchanged and has ch_3(V')=0, since
q(u_1,u_2)=1. Its virtual c_3 is zero by (5). The actual trivial
line bundle is an allowed twist. This passes the tested conditions
in a final ample chamber, rather than only the old pre-chamber model.

The signed class (15) gives neither the presentation maps nor a
locally free representative. Rank two does not force higher Chern
classes to vanish for a virtual class. No degree-eight calculation
is made here. More signed residue sampling cannot reopen the old
construction window merely because (15) passes this test. The
useful conclusion is the scoped exclusion (3), the exact surviving
equations (2), and failure of a uniform third-Chern exclusion.

The exact arithmetic is reproduced by
`python3 scripts/cubic-kahler/check_rank_two_third_chern.py`.
It checks the reflections, forced final tensor, both third-character
components and twist cancellation. Cone membership, singular-support
Riemann--Roch and the distinction between a virtual class and a bundle
are supplied by the argument above, not by the computation.

## Mathlib

Coverage of the full statement: **not checked**. No matching Mathlib
declaration or absence from checked Mathlib sources is asserted.
The directly linked Fulton and Stacks results support rank truncation,
proper Riemann--Roch and character identities, not the full scoped
constraint or existence of a rank-two terminal bundle. For the cone,
the supporting source already read in L025 is Huybrechts,
[chapter 8, section 5.1 and Theorem 5.2, pp. 163--164](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=163).
Kunneth, the projection formula, Hodge index, root reflections and
the diagonal SU(2) decomposition are supporting standard tools.
Their specializations above are a reproduction with no certified
originality or general Hodge resolution claim.
