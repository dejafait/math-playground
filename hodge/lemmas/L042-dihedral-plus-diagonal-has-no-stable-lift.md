# L042 — The dihedral-plus-diagonal support map has no stable lift on S

## Hypotheses

Let S, C, W and g_0,g_1:W -> S satisfy L008, retaining its
very-general cubic-RM Dickson-family hypotheses and resolved
elliptic surface. Thus C is the reduced dihedral support,
the normalization map is j=(g_0,g_1), and g_0 is finite flat
of degree two. The generic degree-two fibre cycle of C,
plus the parameter point itself, is the prescribed recipe.
No change of the parameter surface S is allowed.

Let J be the full ideal of norms on S^{(3)} used in L040,
not an unspecified reduced collision ideal. For the stable
moduli statement choose H general in Yoshioka's sense and
use the specific isomorphism Psi:M_H(2,0,-1) -> S^[3]
and actual support morphism Phi_M=rho Psi from L040.

## Conclusion

The prescribed generic recipe extends to a unique regular
algebraic morphism

\[
g:S\longrightarrow S^{(3)}.
\]

It is the norm cycle of the finite flat cover g_0 with its
second map g_1, plus the identity point, at every fibre.
Its image is generically outside the collision locus.

Let q_1,q_2,q_3 be L008's three fixed points on the resolved
fibre over infinity. At each q_i there are formal parameters
u,v such that, for K=J O_S,

\[
K\widehat{O}_{S,q_i}
=(uv,u^3,v^3)^2
=(u^2v^2,u^4v,uv^4,u^6,v^6)
\quad\text{in }\mathbb C[[u,v]].
\tag{1}
\]

This ideal is nonzero, proper and primary for (u,v), and
is not principal. Consequently K is not invertible. There
is no regular lift h:S -> S^[3] with rho h=g, and no
stable map f:S -> M_H(2,0,-1) with Phi_M f=g.

This is a negative result for the unchanged recipe on S.
It neither excludes a family on a modified parameter
surface nor obstructs arbitrary cycle representatives or
establishes nonalgebraicity. No transverse RM direction or
additional algebraic class is obtained.

## Proof

**The regular cycle at all fibres.** Import the determinant
norm and addition statements from [Rydh, *Families of zero
cycles and divided powers: II*, author version 11 April
2008, section 3 through Definition 3.1, p. 6](https://davidrydh.se/papers/famzerocyclesII-20080411.pdf#page=6),
and [part I, arXiv:0803.0618v1, Definition-Proposition 4.1.1,
p. 39, and Corollary 4.2.5, pp. 42--43](https://arxiv.org/pdf/0803.0618v1#page=39).
Their precise imported scope is retained in
[the source note](../foundations/08-finite-family-cycle-and-norm-ideal-inputs.md).
Do not reprove that framework.

Take the disjoint union W disjoint union S over the parameter
S, with projection g_0 on W and identity on S. It is finite
flat of degree three. Map it to the target S by g_1 on W
and identity on the second component. On the finite locally
free rank-three direct image of its structure sheaf, target
functions act by multiplication; their determinant supplies
the canonical norm family. In characteristic zero the
divided-power target is S^{(3)}. Equivalently this is addition
of the degree-two norm family and the identity point.
This constructs the regular algebraic morphism g.

On the dense distinct-support open, j is birational to C
and its projection is unramified, so the norm is exactly
the two prescribed C fibre points with multiplicity one.
Adding the parameter point gives the required generic
recipe. The generic three points have distinct elliptic
base coordinates: equality of any pair imposes a nontrivial
equation on v in the formulas t=v+a/v and
s=zeta v+zeta^{-1}a/v. In particular the image is not
contained in the collision locus. Uniqueness follows from
separatedness of S^{(3)} and density of this open in S.

This argument uses W's finite flatness, not flatness of
the image support C or C union Delta. At a cover branch
fibre the length-two algebra has one closed point and its
norm is twice that image point. At a diagonal collision
the identity point is simply added with its multiplicity.
The regular maps on the resolved W already cover every
point at infinity and every singular elliptic fibre. Thus
no unresolved affine-chart or reduced-fibre extension is
being assumed.

**The ordered formal cycle at infinity.** L008 supplies
the order-seven local automorphism f whose two graphs
are C near infinity. On the parameter neighbourhood the
norm cycle is therefore

\[
p+f(p)+f^{-1}(p).
\tag{2}
\]

At q_i its tangent eigenvalues are alpha=zeta^r and
beta=zeta^s, with (r,s)=(6,2),(3,5),(6,2). They are
distinct, neither is 1, and neither is -1.

There are formal parameters making f exactly
(u,v) -> (alpha u,beta v), not just to first order.
Indeed, start with parameters u_0,v_0 whose cotangent
classes are the corresponding eigenvectors and set

\[
u=\frac1{7}\sum_{k=0}^6\alpha^{-k}(f^k)^*u_0,
\qquad
v=\frac1{7}\sum_{k=0}^6\beta^{-k}(f^k)^*v_0.
\]

They have the same independent linear terms, so are
formal parameters, and f^*u=alpha u, f^*v=beta v.
Consequently (2) is the ordered formal triple

\[
(u,v),\quad (\alpha u,\beta v),\quad
(\alpha^{-1}u,\beta^{-1}v).
\tag{3}
\]

**The full image ideal, including its scheme structure.**
Import [Ekedahl--Skjelnes, *Recovering the good component
of the Hilbert scheme*, Annals 179 (2014), Definition 2.7,
sections 3.1--3.3 and Proposition 3.4, pp. 811,813--814](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=9),
with [the global ideal in section 7.24, p. 834](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=30).
For n=3, under their characteristic-zero symmetric-tensor
identification, the generators delta(x,y) are all products
nu(x)nu(y), where nu(x)=det((x_i)_[j]). Pulling them back
along the ordered triple (3) gives products of alternating
evaluation determinants. This imports the exact norm ideal;
it does not replace it by its reduced zero set.

Work in R=C[[u,v]], and let D be the ideal generated by

\[
\Delta(a_0,a_1,a_2)
=\det\begin{pmatrix}
a_0(u,v)&a_0(\alpha u,\beta v)&a_0(\alpha^{-1}u,\beta^{-1}v)\\
a_1(u,v)&a_1(\alpha u,\beta v)&a_1(\alpha^{-1}u,\beta^{-1}v)\\
a_2(u,v)&a_2(\alpha u,\beta v)&a_2(\alpha^{-1}u,\beta^{-1}v)
\end{pmatrix},\quad a_i\in R.
\tag{4}
\]

The completed pullback of J is D^2. To justify the use of
formal functions in (4), choose an affine target neighbourhood
of q_i. Its regular functions are dense in the completed
local ring: local parameters can be represented there after
shrinking, and their polynomials approximate every formal
function. Evaluation along the three formal component maps
and determinants are continuous. Ideals in a complete
Noetherian local ring are closed in its maximal-ideal
topology. Hence replacing the regular-function tuples by
all formal tuples neither enlarges nor reduces the
completed ideal generated by their products. This also
justifies the following monomial expansion argument.

For a monomial a_i=u^{a_i'}v^{b_i'}, its evaluation row
is that monomial times (1,lambda_i,lambda_i^{-1}), where
lambda_i=alpha^{a_i'} beta^{b_i'}. Thus a monomial
determinant has the form

\[
c\,u^A v^B,\qquad A=\sum_i a_i',\quad B=\sum_i b_i'.
\]

If A and B are both positive, it is divisible by uv.
If B=0, a nonzero determinant needs three distinct
nonnegative u-exponents (equal exponents give equal
rows), so A>=0+1+2=3. It is then divisible by u^3.
The case A=0 gives v^3 in the same way; A=B=0 gives
zero. Expanding arbitrary tuples and using closedness
therefore proves D is contained in (uv,u^3,v^3).

The reverse inclusion uses three actual determinants:

\[
\begin{aligned}
\Delta(1,u,v)
 &=\frac{(\alpha-1)(\beta-1)(\beta-\alpha)}{\alpha\beta}\,uv,\\
\Delta(1,u,u^2)
 &=(\alpha-1)(\alpha^{-1}-1)(\alpha^{-1}-\alpha)\,u^3,\\
\Delta(1,v,v^2)
 &=(\beta-1)(\beta^{-1}-1)(\beta^{-1}-\beta)\,v^3.
\end{aligned}
\]

All three coefficients are nonzero for each of the
listed weight pairs. Therefore D=(uv,u^3,v^3).
Squaring gives (1); the extra product u^3v^3 is already
a multiple of u^2v^2. This proves the full completed
image-ideal formula at all three q_i.

**The stable-lift test fails.** The ideal in (1) lies in
(u,v), contains u^6 and v^6, and is nonzero. Its radical
is therefore (u,v), of height two. A proper nonzero
principal ideal in the two-dimensional domain R cannot
have this radical, by the principal ideal theorem.
Thus (1) is not principal. If K were invertible at q_i,
its faithfully flat completion would be a principal
ideal, a contradiction.

The parameter S is smooth and integral, and g is
generically outside V(J), as checked above. L040's
necessary invertible-image-ideal criterion therefore
applies. It rules out a Hilbert--Chow lift on S and,
under the retained general-polarization hypothesis,
the stable moduli lift. One failed stalk suffices; no
further finite-collision ideal calculation is needed.

The regular norm framework, the alternating-determinant
formula and the lifting criterion are known inputs.
This is their scoped REPRODUCTION for the prescribed
map, with no originality claim. The result is different
from L009's embedded-union deformation failure: it tests
stable lifting on the fixed S before any transverse
deformation question. A modification of the parameter
surface is a different target and is not constructed here.
The 21-dimensional attained span and three attained RM
directions against four required are unchanged; the
universal rational Hodge target remains open.

`python3 -B scripts/cubic-deformation/check_dihedral_diagonal_norm_ideal.py`
checks the three explicit determinants with exact
cyclotomic arithmetic and the square's five minimal
monomial generators. These checks support the local
algebra; the global norm construction, completion
argument and no-lift implication are proved above.

## Mathlib

Coverage: **not checked** for the full statement or the
supporting norm, Hilbert--Chow, formal-linearization and
principal-ideal inputs. The direct Rydh and
Ekedahl--Skjelnes theorem references match only the
imported framework. L040 supplies the correctly scoped
lifting implication, including its general-polarization
qualification. No matching Mathlib theorem, checked
absence or progress beyond the checked literature is
claimed for this target-specific computation.
