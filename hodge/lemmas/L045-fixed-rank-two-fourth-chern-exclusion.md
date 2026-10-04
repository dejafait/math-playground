# L045 — The fixed rank-two survivor fails the fourth-Chern identity

## Hypotheses

Fix the very general cubic RM K3 surface S and the exact final
ample chamber and virtual class V' of L044 (9)--(15). Put X=S x S,
N=NS(S)_Q and T=N^perp for the cup-product pairing q. Thus dim N=4,
dim T=18, and L025 gives the full field Q(U) with
f(U)=0 for f(z)=z^3+z^2-2z-1. Retain L044's final self-adjoint
operator A_c, with W=im(A_c) of dimension three and K=ker(A_c)
of dimension one. Its restriction to W has characteristic polynomial f.

Let eta be the point class of integral one on S, and write
e_1=eta tensor 1, e_2=1 tensor eta and P=eta tensor eta. Write
j=(g_0,g_1):Y -> X for the smooth finite normalization of C in L008.
The elliptic fibre f_ell has square zero. All three point quotients
in L019's normalization sequence are retained.

The class V' is fixed as an element of K_0(X), including its two
third finite differences and its trivial line twist. In particular
it has virtual rank two, c_1=0, ch_2=2[C]+B_c and ch_3=0 by L044.
No locally free representative or actual presentation is assumed.

## Conclusion

The exact degree-eight values are

\[
\begin{aligned}
\chi(O_Y)&=4,&\chi(O_C)&=1,\\
\operatorname{ch}_4(O_C)&=-7P,&
\operatorname{ch}_4(V')&=-57P,\\
\operatorname{ch}_2(V')^2&=188P,&c_4(V')&=436P.
\end{aligned}
\tag{1}
\]

Consequently no rank-two locally free bundle on X has K-class V'.
In particular this fixed survivor cannot be the terminal rank-two
bundle in a presentation with that K-class. For rank two the required
fourth character would be (47/3)P, rather than -57P. The independent
Euler-characteristic cross-check gives chi(V')=-33.

This is an informative NEGATIVE result for this particular survivor,
classified as REPRODUCTION of the assessed Riemann--Roch and character
tools. It does not exclude arbitrary rank-two classes or bundles with
the same cubic action, and does not invalidate L044's lower-degree
consistency result. No new cycle or transverse surface is supplied:
the known span remains 21, with three attained RM directions against
four required. The universal rational Hodge conjecture remains open.

## Proof

**Imported formulas.** Use the universal fourth-character expansion
in [Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
character additivity in [Lemma 42.45.2, Tag 0F9C](https://stacks.math.columbia.edu/tag/0F9C),
tensor multiplicativity in [Lemma 42.45.3, Tag 0F9D](https://stacks.math.columbia.edu/tag/0F9D),
and the extension to perfect K-classes in
[Remark 42.56.11, Tag 0FET](https://stacks.math.columbia.edu/tag/0FET).
Coherent sheaves on the smooth projective X give such classes.
Use the Todd expansion in
[Stacks Section 42.65, Tag 02UN](https://stacks.math.columbia.edu/tag/02UN).
For proper pushforward between smooth varieties use Fulton,
*Intersection Theory*, second edition (1998),
[Theorem 15.2, pp. 286--287](https://djvu.online/file/87GFN2nbfbdF7),
and its HRR Corollaries 15.2.1--15.2.2, p. 288, and surface
Example 15.2.2, p. 289. Point sheaves have their leading character
in codimension four by Theorem 18.3(3),(5), pp. 353--354.
Rank truncation is Theorem 3.2(a), pp. 50--52.
These are the supporting results read in the prior fourth-Chern
assessment. They are imported; only their application to this fixed
class is calculated here. The Maciocia theorems compared there have
additional Fourier--Mukai hypotheses and do not evaluate this class.

**Normalization, source Todd term and all three corrections.**
L008's finite flat double cover has the trace decomposition

\[
(g_0)_*O_Y=O_S\oplus O_S(-f_{\rm ell}).
\]

For a K3 surface chi(O_S)=2 and K_S=0. Surface HRR gives
chi(O_S(-f_ell))=2+q(f_ell,f_ell)/2=2. Finite pushforward therefore
gives chi(O_Y)=4. L019's exact sequence gives chi(O_C)=4-3=1.

On S, the Todd class is 1+2eta: its first component is zero and
the integral of its second component is chi(O_S)=2. Consequently

\[
\operatorname{td}(X)=1+2(e_1+e_2)+4P.
\tag{2}
\]

Apply proper Grothendieck--Riemann--Roch to j, whose source Y
and target X are smooth. Since j is finite, its higher direct images
vanish. The character of j_*O_Y starts in codimension two with [C],
and GRR in codimension four gives

\[
\operatorname{ch}_4(j_*O_Y)+2[C]\,(e_1+e_2)
       =j_*\operatorname{td}_2(Y).
\tag{3}
\]

The two g_i have degree two, so integral_X [C]e_i=2 for each i
by the projection formula. Thus the ambient Todd contribution on
the left has integral eight. The source term on the right has
integral chi(O_Y)=4 by smooth surface HRR. H^8(X,Q)=Q P and
integral_X P=1, so ch_4(j_*O_Y)=-4P.

The pushed normalization sequence is

\[
[O_C]=[j_*O_Y]-\sum_{\ell=1}^3[O_{p_\ell}].
\tag{4}
\]

Each point sheaf has ch_4=P and zero lower components. Hence
ch_4(O_C)=(-4-3)P=-7P. Equivalently, coherent HRR on smooth X
gives chi(O_C)=integral_X(ch_4(O_C)+[C]td_2(X))=-7+8=1,
agreeing with (4). No smooth embedded-support normal-bundle formula
is applied to the non-lci C; the source Todd term and the ambient
factor are both present in (3).

**The fixed product-line terms through degree eight.**
Retain L044's integral u_1,u_2,u_3 and y=2u_1+2u_2+5u_3.
Their pairings are

\[
q(u_1,u_1)=0,\quad q(u_2,u_2)=q(u_3,u_3)=-2,
\quad q(u_1,u_2)=1,\quad q(u_1,u_3)=q(u_2,u_3)=0.
\]

In particular q(y,y)=8-8-50=-50. For a product line bundle
L(x,z), the exponential character on the two surface factors gives

\[
\operatorname{ch}_4(L(x,z))
       =\frac{q(x,x)q(z,z)}4P.
\tag{5}
\]

The same value is the fourth character of
Delta(x,z)=[L(x,z)]-[L(x,0)]-[L(0,z)]+[O_X], since the last three
terms have zero fourth character. L044's Delta coefficient matrix is

\[
B_0=\begin{pmatrix}0&-2&2\\-2&1&1\\2&1&4\end{pmatrix}.
\]

Its fourth-character contribution is
sum_ij (B_0)_ij q(u_i,u_i)q(u_j,u_j)/4=1+1+1+4=7.
For Pi(u_1,u_2;y), multiplicativity gives the product
(exp(p_1^*u_1)-1)(exp(p_1^*u_2)-1)(exp(p_2^*y)-1).
The first two factors have product exactly e_1 in cohomology:
their leading product is q(u_1,u_2)e_1=e_1, and all higher terms
vanish on that surface factor. Therefore

\[
\operatorname{ch}_4(\Pi(u_1,u_2;y))=-25P,
\quad
\operatorname{ch}_4(\Pi_{\rm rev}(u_1,u_2;y))=-25P.
\tag{6}
\]

The factor-reversed correction is a separate term and cannot be
discarded because its lower characters agree. Since [I_C]=[O_X]-[O_C],
the source -2[I_C] contributes 2 ch_4(O_C)=-14P. The term 4[O_X]
contributes zero in this degree. Thus the exact class in L044 (15)
has fourth character (7-14-25-25)P=-57P.

**The full second-character square, including T.**
L044 gives beta=ch_2(V')=2[C]+B_c. Its pure components are 4e_1
and 4e_2. Under the tensor-to-operator convention of L026 its mixed
component tau_D has the q-self-adjoint operator

\[
D|_T=2U,\qquad D|_N=2A_c+4\pi_K.
\tag{7}
\]

For a mixed tensor with a self-adjoint operator D, direct contraction
in q-dual bases gives integral_X tau_D^2=tr(D^2). This uses the
cup-product form on all of H^2(S,Q), rather than a positive-definite
replacement. Explicitly, in a basis with pairing matrix G and a
symmetric tensor matrix M, the tensor action is MG, up to transpose
convention; contraction is tr(MGMG). All factors have even degree,
so there is no Koszul minus sign. The symmetry follows from
q-self-adjointness. Pure components pair trivially with tau_D, and
e_1^2=e_2^2=0, e_1e_2=P. Consequently

\[
\int_X\beta^2=32+\operatorname{tr}(D^2).
\tag{8}
\]

If lambda_1,lambda_2,lambda_3 are the roots of f, Vieta's identities
give sum lambda_i=-1, sum_{i<j}lambda_i lambda_j=-2 and
sum lambda_i^2=5. On W, A_c has these three eigenvalues, while
K is its zero eigenspace. Formula (7) thus gives
tr_N(D^2)=4(5)+16=36.

Since f is irreducible of degree three, T of rational dimension 18
is a six-dimensional vector space over Q(U). Each root of f therefore
occurs six times after scalar extension. Hence
tr_T(U^2)=6(5)=30 and tr_T(D^2)=120. Substituting in (8) gives
beta^2=(32+36+120)P=188P. In particular retaining only the divisor
tensor would omit the necessary contribution 120P.

**Rank-two comparison and Euler-characteristic check.**
The imported fourth-character polynomial for any perfect class is

\[
\operatorname{ch}_4
 =\frac{c_1^4-4c_1^2c_2+4c_1c_3+2c_2^2-4c_4}{24}.
\tag{9}
\]

Here c_1(V')=0, so c_2(V')=-beta and (9) gives

\[
c_4(V')=\tfrac12c_2(V')^2-6\operatorname{ch}_4(V')
        =(94+342)P=436P.
\tag{10}
\]

The class P is nonzero since its integral is one. Rank truncation
forces c_4=0 for every actual rank-two locally free bundle, whereas
virtual rank two alone imposes no such condition. Equivalently the
required fourth character would be c_2^2/12=(47/3)P; the computed
value is -57P. This proves the scoped exclusion.

For an additional exact bookkeeping check, surface HRR and Kunneth
give chi(L(x,z))=(2+q(x,x)/2)(2+q(z,z)/2).
The Delta sum therefore contributes seven to chi. The first-factor
product in Pi has character eta and Euler characteristic one, while
the second-factor difference has Euler characteristic q(y,y)/2=-25.
Each Pi contributes -25. Also chi(O_X)=4 and chi(I_C)=4-1=3.
The signed K-class expression thus gives

\[
\chi(V')=4(4)+7-2(3)-25-25=-33.
\tag{11}
\]

Using (2) and the computed full character instead gives
chi(V')=2(4)+integral_X beta 2(e_1+e_2)-57=8+16-57=-33.
These two evaluations agree while retaining every source, point and
finite-difference term. They check the arithmetic, rather than prove
bundle existence or any deformation statement.

The exact calculation is reproducible with
`python3 scripts/cubic-kahler/check_rank_two_fourth_chern.py`.
It also checks beta^2 by expanding (2[C]+B_c)^2, independently of
the final-operator trace evaluation. The geometric normalization and
the rank-truncation argument are supplied above, not inferred from
numerical sampling. This completes the fixed-class test; changing its
point terms, residues or rank would require a different target and
does not follow from this result.

## Mathlib

Coverage of the full fixed-class exclusion: **not checked**. No full
Mathlib match or absence from checked Mathlib sources is asserted.
The directly linked Fulton and Stacks statements support proper
Riemann--Roch, Todd terms, perfect-class characters and rank truncation;
they are not Mathlib declarations or a match for the entire specialization.
K3 numerical cohomology, the finite trace decomposition, projection
formula and Kunneth contraction are the named supporting inputs used
above. The result is a reproduction of these tools with no claim of
originality or resolution of the universal Hodge target.
