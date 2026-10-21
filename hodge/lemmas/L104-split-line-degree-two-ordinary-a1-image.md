# L104 — Degree two forces the ordinary analytic A1 image

## Hypotheses

Retain the full audited L103 setup: the fixed marked K3 surface S,
complex structure I, metric g, real Kähler class h, line bundle L and
split reference E; the chosen actual convergent L101 slice map alpha
with its specified first jet; and L102's punctured stability. Let

\[
 A=\mathcal O_{Z,0}\subset B=\mathbf C\{s,t\},
 \qquad \mathfrak m_B=(s,t),
\]

be L103's finite inclusion for the **ordinary reduced analytic image**
of the actual invariant classifying map. Its coordinate pullbacks are
the convergent functions P_iQ_j. In particular,

\[
 P_1=s+O(\mathfrak m_B^2),\quad P_2=-t+O(\mathfrak m_B^2),
 \quad Q_1=t+O(\mathfrak m_B^2),\quad Q_2=s+O(\mathfrak m_B^2).
 \tag{1}
\]

Assume additionally that the generic degree is two:
\([\operatorname{Frac}(B):\operatorname{Frac}(A)]=2\).
This is a conditional hypothesis, not a conclusion selecting L103's
degree alternative. No normality of A or source involution is assumed.

## Conclusion

There are convergent local coordinates u,v on the source, with
u=s+O(\mathfrak m_B^2) and v=t+O(\mathfrak m_B^2), and a nonidentity
holomorphic involution tau satisfying

\[
 \tau(u)=-u,\qquad\tau(v)=-v,\qquad
 A=B^{\langle\tau\rangle}
   \cong \mathbf C\{x,y,z\}/(xz-y^2),
 \quad (x,y,z)=(u^2,uv,v^2).
 \tag{2}
\]

Thus Z itself, with its ordinary reduced analytic structure, is the
ordinary A1 surface germ. The classifying map onto Z is analytically
equivalent to (u,v) mapped to (u^2,uv,v^2). In particular the image is
normal, and on a sufficiently small representative the involution
exchanges the two parameters over each noncentral image point.

This is ADVANCE / REPRODUCTION under the prior SPECIALIZE assessment.
It is a necessary local consequence of the additional degree-two
hypothesis; the separate critical audit below preserves it. It does not establish that
degree two occurs, or select the actual image for a degree-one family.
It supplies no weakly normal/algebraic coarse comparison, quaternionic
integration, common F, global mixed action, separation, reconstruction,
transport or new algebraic Hodge class. The universal target remains open.

## Proof

**Imported results and purpose of the specialization.** Use the following
previously assessed inputs; the general theorems are imported, rather
than reproved.

- The Stacks Project, [Section 9.21, Lemma 9.21.2 and Theorem 9.21.7](https://stacks.math.columbia.edu/tag/09DU), supplies finite Galois
  automorphisms and fixed fields. Brian Conrad, *Galois Action on
  Integral Closures*, [p. 1, paragraph before Proposition 1](https://math.stanford.edu/~conrad/210BPage/handouts/math210b-Galois-IntClosure.pdf),
  records preservation of the integral closure by field automorphisms.
  This preservation does not require normality of A; the later
  prime-transitivity proposition is not used.
- Greuel--Lossen--Shustin, *Introduction to Singularities and
  Deformations*, Springer (2007), [Chapter I](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/greuel.pdf),
  Definition 1.1 and Remark 1.1.1(4--5), p. 9, identify analytic
  C-algebra maps with convergent substitution. Theorem I.1.16,
  pp. 23--24, makes B factorial and hence integrally closed.
  Theorem I.1.8, p. 12 (uniqueness p. 13; convergence proof pp. 17--18),
  supplies convergent Weierstrass division, here with y last and
  divisor y^2-xz general of order two. Theorem I.1.20, p. 27,
  makes an analytic algebra map surjective if and only if its
  cotangent map is surjective.
- Takamura, *Linearization of Quotient Families*, J. Math. Sci.
  Univ. Tokyo 26 (2019), 361--389, [averaging construction and Lemma 3.6, pp. 381--382](https://www.ms.u-tokyo.ac.jp/journal/26-3-3.pdf),
  linearizes a finite holomorphic action fixing the origin. Only this
  local finite-group result is used; no quotient-family hypothesis is
  being inferred.
- Riemenschneider, *Quotient singularities: General theory*,
  [Chapter 8, Theorems 8.1/8.4/8.7 and Lemmas 8.3/8.5, pp. 233--235](https://www.math.uni-hamburg.de/home/riemenschneider/bookchap08.pdf),
  supplies analytic finite-group invariants, their finite inclusion in
  B and their normality when B is normal.
- Reid, *The Du Val singularities A_n, D_n, E_6, E_7, E_8*,
  [Sections 1.1--1.2, pp. 2--3](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf),
  identifies the sign quotient and xz=y^2 as the ordinary A1 model.
  The convergent presentation and equality with the separately given
  image ring are checked below; polynomial invariant generation alone
  would not suffice.

The actual specialization must identify B as the relevant integral
closure, determine the involution's derivative from (1), and prove
ordinary-image equality using the actual products. These are precisely
the extra obligations not supplied by a general quotient theorem.

**Integral closure and actual analytic action.** Put K=Frac(A) and
M=Frac(B). L103 gives finite integrality of B over A. B is normal by
the cited factoriality theorem. If an element of M is integral over A,
its monic equation is also an equation over B, so it belongs to B.
Conversely every element of B is integral over A. Therefore B is
exactly the integral closure of A in M, without assuming A normal.

The fields contain C and have characteristic zero. A quadratic field
extension is separable and normal: a generator with minimal polynomial
X^2+aX+b has its other root -a minus that generator in M. Consequently
M/K is Galois, with a unique nonidentity K-automorphism tau of order two.
The integral-closure preservation result gives tau(B)=B. Its restriction
is a C-algebra automorphism, fixes A pointwise and preserves the unique
maximal ideal of the local ring B. The analytic-algebra substitution
result realizes it as an actual holomorphic germ fixing zero, with
inverse itself. It is nonidentity on B, since otherwise it would be
identity on Frac(B)=M. Thus this is neither merely a formal nor a
meromorphic parameter involution.

**Derivative forced by the retained quadratic span.** Let T denote the
linear action of tau on \(\mathfrak m_B/\mathfrak m_B^2\). It satisfies
T^2=id. The three actual A-elements

\[
 g_x=P_1Q_2=s^2+O(\mathfrak m_B^3),\quad
 g_y=P_1Q_1=st+O(\mathfrak m_B^3),\quad
 g_z=-P_2Q_1=t^2+O(\mathfrak m_B^3)
 \tag{3}
\]

are fixed by tau. Their degree-two terms are a basis of
\(\mathfrak m_B^2/\mathfrak m_B^3
  =\operatorname{Sym}^2(\mathfrak m_B/\mathfrak m_B^2)\).
It follows that Sym^2(T)=id. Over C an involution is diagonalizable
with eigenvalues in {1,-1}. Mixed eigenvalues would give a -1 eigenvalue
on the product of two eigenvectors in Sym^2, which is impossible.
Hence T=id or T=-id.

Apply the finite holomorphic linearization theorem to this actual
order-two germ. If T=id, the action is conjugate to the identity and
tau itself is identity, a contradiction. Thus T=-id. The averaging
coordinates in this case are explicitly

\[
 u=\tfrac12(s-\tau(s)),\qquad
 v=\tfrac12(t-\tau(t)).
 \tag{4}
\]

Their derivative in (s,t) is the identity, so the analytic inverse
function theorem makes them convergent local coordinates. They satisfy
tau(u)=-u, tau(v)=-v exactly, not just to first order. In particular
B=C{u,v}. The induced linear map on the geometric tangent has the same
sign as the cotangent action used above.

**Analytic invariant ring and its cotangent space.** Let R=B^tau. The
finite-group theorems make R an analytic local C-algebra, with finite
inclusion R subset B and maximal ideal consisting of invariants
vanishing at zero. In coordinates (4), an invariant convergent series
has only monomials u^i v^j with i+j even. Thus it has a unique form

\[
 F(u,v)=H(u^2,v^2)+uv\,G(u^2,v^2),\qquad H,G\in\mathbf C\{x,z\}.
 \tag{5}
\]

Convergence here is essential. Choose r>0 so that the original series
is absolutely convergent with
\(\sum |a_{ij}|r^{i+j}<\infty\). The even-even coefficients define H
with absolute convergence at |x|,|z|<=r^2. The odd-odd coefficients
define G there, since their corresponding coefficient sum is bounded
by \(r^{-2}\sum |a_{ij}|r^{i+j}\). Hence both series are convergent
germs. This verifies analytic generation by x=u^2, y=uv, z=v^2.

The map C{x,y,z} to R is surjective by (5), and kills xz-y^2. To
identify its kernel, divide any convergent series by the distinguished
polynomial y^2-xz in the variable y using Weierstrass division. Its
remainder is H(x,z)+yG(x,z). If its substitution vanishes in B, the
even-even and odd-odd monomials in (5) separately vanish. Independence
of the monomials implies H=G=0. The kernel is therefore exactly
(xz-y^2), establishing the convergent A1 presentation, not only a
polynomial or completed presentation.

In particular \(\mathfrak m_R=(x,y,z)\). The relation xz-y^2 has no
linear term in these three variables, so their classes form a basis
of \(\mathfrak m_R/\mathfrak m_R^2\). Equivalently, extracting the
degree-two term in u,v gives an isomorphism

\[
 \mathfrak m_R/\mathfrak m_R^2
   \longrightarrow \operatorname{span}_{\mathbf C}\{u^2,uv,v^2\}.
 \tag{6}
\]

For completeness, no higher invariant term is lost in (6). If an
invariant has zero constant and degree-two terms, (5) has H in
(x,z)^2 and G in (x,z), so it lies in \(\mathfrak m_R^2\).
Conversely every element of that square has order at least four in
u,v. There are no odd-total-degree invariant terms at all.

**Ordinary image equals invariants.** Since tau fixes A, the given
inclusion factors as A subset R subset B. It is a local C-algebra map
between analytic algebras, hence an analytic algebra map by the cited
substitution result. This assertion concerns the actual ring A from
L103, with its convergent generators, rather than a polynomial image.

The coordinates u,v agree with s,t to first order. Reexpressing (3) in
u,v therefore retains their respective degree-two terms u^2, uv, v^2.
Each g belongs to R; invariance removes all odd-total-degree terms.
By (6), their classes in \(\mathfrak m_R/\mathfrak m_R^2\) are exactly
x,y,z. They all lie in \(\mathfrak m_A\), and the image of
\(\mathfrak m_A^2\) lies in \(\mathfrak m_R^2\). Consequently the
induced cotangent map

\[
 \mathfrak m_A/\mathfrak m_A^2
     \longrightarrow \mathfrak m_R/\mathfrak m_R^2
 \tag{7}
\]

is surjective. Greuel--Lossen--Shustin Theorem I.1.20 now proves A to R
surjective. It was already injective as a subring of B, so A=R.
This is the step that proves ordinary-image equality; finiteness,
multiplicity two or equality of fraction fields alone would not do it.

The imported normal-invariants theorem now implies A is normal.
Combining its analytic presentation with Reid's named model gives the
ordinary A1 germ Z. Under this identification the original map is
precisely the sign quotient (u,v) mapped to (u^2,uv,v^2): a map of
analytic germs is determined by its pullback on these coordinate
functions. The sign action has no nonzero fixed point. On a small
sign-invariant coordinate neighborhood its noncentral quotient fibres
are exactly the pairs {w,-w}; if one coordinate of w is nonzero, the
three quadratic coordinates determine the other coordinate and the
common sign. This is a local statement, not a global separation result.

**Threshold and limitations.** The generator test meets the desired
ordinary-image threshold for d=2 and not merely a normalization
threshold. The only direct notebook input is audited L103; its
L094/L101/L102 setup is inherited, not a different parameter family.
No formal truncation replaces any actual product, and all convergent
higher coefficients are allowed. Choosing d=2 remains conditional.
Neither this local quotient description nor its normality supplies a
weakly normal/algebraic coarse comparison or any of the independent
integration, kernel, global action and transport inputs. This is a
known-tool specialization and no originality claim or Hodge resolution
is made.

**Separate critical audit, 2026-10-14 (step 282).** The conditional
ordinary-image identification survives. This is EXPLORATION /
REPRODUCTION: the audit finds no substantive mathematical error,
stronger conclusion or existence result. It reuses the approved source
cases and checks their application to the actual rings and functions.
The preceding argument remains unchanged; the division citation above
has been made precise using the already inspected source.

The input is audited L103, not L104's proposed conclusion. In L103,
A is the quotient of C{x_ij} by the kernel of substitution of the
actual convergent products P_iQ_j, and B is finite over that quotient.
Thus A is an analytic local domain embedded in B with the same residue
field C. In particular this is not merely the subring of polynomial
expressions in the products. The three functions in (3) really belong
to its maximal ideal, with the stated independent quadratic initial
forms. No additional geometric hypothesis about a coarse moduli space
is needed to use these ring data.

Normality of B is used in its own fraction field M. If c in M is
integral over A, the same monic equation has coefficients in B, so
c belongs to B. The converse follows from B's finiteness over A.
This checks both inclusions in the integral-closure claim. Since the
extension degree is two in characteristic zero, its nontrivial field
automorphism fixes K and hence A, preserves this integral closure,
and restricts faithfully to B. Faithfulness follows because B generates
M as a field. Locality follows because B has a unique maximal ideal;
the automorphism fixes C. The cited analytic-algebra map result therefore
applies to the restriction itself and yields a convergent substitution
with convergent inverse. There is no step that assumes a formal
automorphism converges without this analytic-ring argument.

For an automorphism preserving the maximal ideal, the associated
graded action in degree two is Sym^2 of its degree-one action.
The three fixed initial forms in (3) span the entire three-dimensional
degree-two part, so Sym^2(T)=id. Diagonalizability follows from T^2=id
over C; eigenvalues (1,-1) would negate their mixed product. The only
possibilities are T=+id and T=-id. Holomorphic finite-group
linearization is applicable after, not before, the analytic action
has been established. Its identity-derivative case would contradict
faithfulness. Formula (4) in the remaining case has identity Jacobian
and exactly anti-invariant coordinates. This also checks that changing
coordinates preserves every specified quadratic initial form.

In these coordinates all invariant monomials have even total degree,
hence precisely the two parity types used in (5). On a sufficiently
small closed bidisc the absolute coefficient sum is finite; the stated
r^{-2} bound proves convergence of the odd-odd subseries even after
factoring out uv. Both coefficient series in (5) are therefore
convergent, not just formal. For the kernel calculation put x,z before
y: the divisor restricts at x=z=0 to y^2, meeting GLS I.1.8's
finite-order hypothesis. Its convergent remainder is of degree at most
one in y. After substitution its two terms have disjoint exponent
parities in u,v, so neither can cancel the other; injectivity of
substitution x=u^2,z=v^2 on each coefficient series makes both zero.
This proves the claimed kernel and the analytic presentation.

The cotangent step must be checked in R, rather than inferred from
m_A B=m_B^2. In R the presentation makes x,y,z a cotangent basis:
the sole relation has no linear term. Equivalently an invariant series
with no constant or quadratic part has H in (x,z)^2 and G in (x,z)
in (5), and therefore belongs to m_R^2. Reexpressing each actual
function g_x,g_y,g_z in u,v leaves the respective quadratic terms
u^2,uv,v^2; invariance eliminates every odd-degree remainder. Thus
g_x-x, g_y-y and g_z-z belong to m_R^2. The local inclusion A into R
maps m_A^2 into m_R^2, and these three actual preimages establish
surjectivity on cotangent spaces. Both rings are analytic C-algebras,
so GLS I.1.20 applies without any prior normality, smoothness or
flatness of A. Its conclusion, together with the existing injection,
is the required equality A=R.

Finally the source coordinate change and this analytic ring
identification identify the original morphism, not merely its degree
or abstract normalization, with the quadratic sign quotient. A small
sign-invariant representative has only zero fixed by the sign action;
equality of its three quadratic coordinates at nonzero points gives
exactly a common sign. Normality of the target now follows from normal
invariants, rather than entering the image-equality proof as a premise.
The sole direct notebook input remains L103. The audit does not select
degree two, produce any compatible quaternionic or global family,
or identify an independently specified weakly normal or algebraic
coarse image. All such gaps and the universal Hodge target remain open.

## Mathlib

Full matching coverage of this convergent analytic image specialization,
finite holomorphic linearization, analytic invariants and epimorphism
criterion: **not checked**. Unknown coverage is not evidence of absence.
The general inputs are imported by the precise citations above; the
integral-closure identification, derivative test, convergence and actual
cotangent-generation specialization are proved here. No numerical or
Lean certificate is claimed.
