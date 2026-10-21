# L103 — Finite local classifying germ with generic degree at most two

## Hypotheses

Retain audited L094's marked projective K3 surface S, complex structure I,
fixed metric g, real Kähler class h, line bundle L and split bundle
E=L direct sum L^{-1}. Retain its two positive-weight vectors e_1,e_2,
the harmonic operators I,J,K and B(w)=w^{0,1}.

Fix any one actual convergent slice family of L101, with harmonic map
alpha:(C^2,0) to (H,0), satisfying the complete analytic integrability
equations and alpha=ell+O((s,t)^2). Here H=H_+ direct sum H_-, each
sector has complex dimension 26, and

\[
 P_+ell=sB(e_1)-tB(e_2),\qquad
 P_-ell=tB(Je_1)+sB(Je_2).
\]

Use L102's uniform punctured h-stability for this same actual family.
All neighborhoods below may depend on that fixed convergent alpha.
No product kernel F or quaternionic parameter family is assumed.

## Conclusion

The family has a holomorphic classifying map into the concrete
**reduced analytic GIT quotient** of its full integrable slice. This
map germ is finite onto its reduced image Z. For

\[
 A=\mathcal O_{Z,0}\ \subset\ B=\mathbf C\{s,t\},\qquad
 \mathfrak m=(s,t)\subset B,
\]

its pulled-back maximal ideal is exactly
\(\mathfrak m_A B=\mathfrak m^2\). The central fibre has length three,
and its generic degree d satisfies

\[
 d\leq3,\qquad d\,e_A(\mathfrak m_A)=4,
 \qquad\text{hence }d\in\{1,2\}.
\]

Thus at most two sufficiently nearby generic parameters give one
isomorphism class. Neither exact degree one nor exact degree two, a
literal parameter involution, or an identification of Z with its
normalization is asserted. The quotient here is the reduced analytic
GIT space; no equality with a weakly normal coarse space or an arbitrary
algebraic Gieseker moduli germ is asserted.

This is ADVANCE / REPRODUCTION: an explicit local specialization of
known quotient and local-algebra tools. The separate critical audit below
preserves the result.
It controls local identification for the chosen holomorphic family.
It supplies no quaternionic integration, common F, global mixed action,
global separation, reconstruction, transport or new Hodge class.

## Proof

**Imported inputs.** Buchdahl--Schumacher, *Polystable bundles and
representations of their automorphisms*, Complex Manifolds 9 (2022),
78--113, DOI 10.1515/coma-2021-0131,
[Corollary 4.9, p. 91](https://d-nb.info/1262812674/34), identifies
isomorphism of sufficiently small integrable slice bundles with the
full reference-automorphism orbit relation. Its injectivity uses
Corollary 4.6, p. 89, and the converse uses Corollary 4.8(2), pp. 90--91.
The fixed compact Kähler metric and reference polystability hold here.
L101 identifies the correction with that actual full slice; shrink its
domain to this orbit-comparison neighborhood and L102's stability ball.

For its analytic quotient, import the same authors, *An Analytic
Application of Geometric Invariant Theory*,
[2008.04625v3, 26 February 2021](https://arxiv.org/pdf/2008.04625v3),
Definition 1 and Theorems 1--3, pp. 4--8, and Theorem 6, p. 11.
These give the reduced analytic quotient of the restricted invariant
integrable slice inside the affine quotient. They do not claim that
our two-parameter map is finite. The complete equations from L101,
rather than their quadratic truncation, define this slice. The reference
bundle is polystable and its automorphism group is reductive, as required.

Import Mond--Nuño-Ballesteros, *Singularities of Mappings*, Grundlehren
357, Springer (2020), DOI 10.1007/978-3-030-34440-5,
[Appendix C, Lemma C.1 and Corollaries C.1/C.2, pp. 491--492;
Appendix D, Theorems D.5/D.6, pp. 522--523, and Lemma D.2, p. 525](https://link.springer.com/content/pdf/bbm:978-3-030-34440-5/1).
These supply Nakayama/minimal generators, the isolated-central-fibre
criterion for finite holomorphic germs, analytic finite images and
generic degree as fraction-field degree. No smoothness or
Cohen--Macaulay hypothesis on the image is being added.

Finally import Huneke--Swanson, *Integral Closure of Ideals, Rings,
and Modules*, LMS Lecture Note Series 336, Cambridge (2006),
[author revision February 2023, Theorem 11.2.7, p. 228;
Proposition 11.2.9(1), p. 229; Example 11.1.11, p. 225](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf).
These give the finite-extension multiplicity formula, its power scaling
and multiplicity one for the regular local ring at its maximal ideal.
The local, domain, dimension and residue-field hypotheses are checked
below. The general results are imported; the following invariant and
ideal calculations are the needed specialization.

**Full invariants and actual classifying map.** L094 and L101 give
Aut(E)=(C*)^2, with no off-diagonal or exchanging automorphisms.
As checked in L102, the full effective action is the surjective ratio
character z=a/b, with kernel the common scalars, acting by

\[
 z\cdot(p,q)=(zp,z^{-1}q),\qquad p\in H_+,\quad q\in H_-.
\]

Choose linear bases with B(e_1),B(e_2) first in H_+ and
B(Je_1),B(Je_2) first in H_-. Write p_i,q_j for their coefficient
functions, 1<=i,j<=26. The full polynomial invariant ring is generated
by x_{ij}=p_iq_j: a monomial has weight zero exactly when the total
p degree equals the total q degree, in which case pairing its factors
writes it as a product of such x_{ij}. For an invariant polynomial,
decomposing into character weights shows that only these monomials
occur. This proves generation for the full effective group, not just
for a selected subgroup.

Let rho:H to Q=Spec C[H]^{C*} be this quotient, realized in C^{676}
with coordinates x_{ij}. The imported analytic quotient theorem gives
the reduced analytic quotient Y of the integrable slice as an analytic
subgerm of Q. The complete integrability of alpha therefore gives the
actual holomorphic map

\[
 f=\rho\circ\alpha:(\mathbf C^2,0)\longrightarrow(Y,0),
 \qquad f_{ij}(s,t)=p_i(\alpha(s,t))q_j(\alpha(s,t)).
\]

This is a classifying map for the chosen family in the following
precise sense. By L102, every nonzero small parameter has both p and q
nonzero and has a closed full orbit; zero has the closed orbit {0}.
Two nonzero tensors p tensor q and p' tensor q' agree exactly when
p'=zp and q'=z^{-1}q for some z in C*: choose a nonzero component
of q, compare that column, and then compare the remaining columns
using a nonzero component of p. Conversely that ratio action preserves
every product. Combining with Corollary 4.9, equality of f-values
is exactly bundle isomorphism on this family after shrinking. Finiteness
and the number of such parameters have not yet been inferred.

**Exact pullback ideal, retaining every higher coefficient.** In B put
P_i=p_i composed with alpha and Q_j=q_j composed with alpha. They all
vanish at zero. The actual first jet gives

\[
 P_1=s+O(\mathfrak m^2),\quad P_2=-t+O(\mathfrak m^2),
 \quad Q_1=t+O(\mathfrak m^2),\quad Q_2=s+O(\mathfrak m^2).
\]

The two maps (P_1,P_2) and (Q_1,Q_2) each have invertible complex
Jacobian at zero. The analytic inverse-function theorem makes each
pair a local coordinate system. In particular their ideals in B are
both m: the inverse coordinate functions have zero constant term and
so belong to the ideal generated by their two arguments. All remaining
P_i and Q_j belong to m. Consequently

\[
 (P_1,\ldots,P_{26})=(Q_1,\ldots,Q_{26})=\mathfrak m,
 \qquad (P_iQ_j:1\leq i,j\leq26)=\mathfrak m^2.       \tag{1}
\]

This equality is in the convergent local ring for the actual alpha;
it is not an equality only of initial ideals. It permits arbitrary
convergent higher coefficients satisfying L101's complete equations.
The central fibre is isolated and its local algebra is B/m^2,
with C-basis 1,s,t and length three.

**Finite image and minimal-generator bound.** Apply the isolated-fibre
criterion D.5 to f considered as a map into C^{676}. Its coordinate
ideal is (1), of finite colength, so it is a finite map germ. Theorem
D.6 gives its analytic image Z, and its local ring is

\[
 A=\mathbf C\{x_{ij}\}/\ker(x_{ij}\mapsto P_iQ_j)
 \ \subset\ B.
\]

The kernel is prime because B is a domain, so Z is reduced and
irreducible, with this actual image structure. It lies in Y. Both A
and B are Noetherian local analytic domains, the inclusion is finite,
both residue fields are C, and dim A=dim B=2 by finiteness. The maximal
ideal of A is generated by the coordinate restrictions x_{ij}; thus
(1) is exactly m_A B=m^2, not just a subideal of the pullback.

The finite A-module B has B/m_A B of C-dimension three. Nakayama
therefore gives a surjection A^3 to B (indeed three is the minimal
number of module generators). Set K=Frac(A), M=Frac(B) and d=[M:K].
Localizing this surjection gives K^3 to M: B tensor_A K is a finite
domain over the field K, hence a field and exactly M. It follows
that d<=3. Lemma D.2 identifies d with the generic covering degree
of the finite surjective germ onto Z. No freeness of B over A has
been asserted, and the special-fibre length three is not equated
with the generic degree.

**Independent multiplicity bound.** Apply Huneke--Swanson 11.2.7
to A subset B and I=m_A. B is local, so only its one maximal ideal
occurs; its dimension is two and its residue field extension has
degree one. The formula becomes

\[
 d\,e_A(\mathfrak m_A)=e_B(\mathfrak m_A B)
 =e_B(\mathfrak m^2)=2^2e_B(\mathfrak m)=4.             \tag{2}
\]

The last two equalities use Proposition 11.2.9(1) and the regularity
of B=C{s,t}, respectively. The Hilbert--Samuel multiplicity of the
maximal ideal in the two-dimensional local domain A is a positive
integer. Thus d is a positive divisor of four. Combining (2) with
d<=3 leaves exactly d=1 or d=2. Equivalently the image multiplicity
is four or two, respectively; neither alternative is selected here.

**Scope and traps.** The finite germ admits a sufficiently small finite
representative, and outside a proper analytic subset its fibres consist
of d distinct points, as in the cited generic-degree lemma over C.
Since its f-values classify these actual polystable fibres, the bound
also measures their generic isomorphism-class identifications.
It does not supply an involution on the parameter ball or a global
cardinality bound. The derivative of f at zero is zero; the nonzero
Kodaira--Spencer first jet of alpha has not been confused with a
nonzero coarse derivative.

Buchdahl--Schumacher's sequel,
[*An Analytic Application of Geometric Invariant Theory II: Coarse
Moduli Spaces*, 2108.03255, Section 6, Theorem 1, pp. 15--16](https://arxiv.org/pdf/2108.03255),
constructs a coarse space in the category of weakly normal spaces.
That category statement is not used to replace our concrete Y or
the image ring A by a weak normalization. The finiteness statement
above refers to Y and its reduced analytic image Z. An identification
with a separately specified coarse-space structure would require its
natural comparison map; no such extra identification is needed for
the stated invariant map or its generic orbit-count bound.

In particular neither the quadratic jet alone nor punctured stability
alone proves the degree bound. Exact ideal equality, analytic finiteness,
the module-generator bound and the finite-extension formula are all
used. No Cohen--Macaulay target, smooth image, real moment equation,
smooth central unitary gauge, common kernel or global mixed tensor
is assumed. The achieved local bound is at most two, as required by
this intermediate target, while the universal Hodge gap is unchanged.

**Separate critical audit, 2026-10-14 (step 278).** The finiteness and
bound d in {1,2} survive. This audit is EXPLORATION / REPRODUCTION:
no substantive error, stronger conclusion or new existence result was
found. The preceding proof remains the argument; the checks below
resolve its applicability questions for the fixed actual family.

First check the precise slice and group. L094's k.h=0 and k nonzero
exclude sections of both L^2 and L^{-2}; L101 therefore has no exchanging
or off-diagonal reference automorphism. H^1(O_S)=0 removes both scalar
and trace-free diagonal harmonic directions. Thus H is the full vector
bundle deformation space, not a smaller arbitrarily chosen subspace.
L101's trace-free implicit solution is the full vector slice solution
by uniqueness, and its complete equation gives actual integrability.
Its scalar obstruction is zero because the trace of a degree-one
endomorphism-valued square is zero. Hence passing from a chosen
determinant trivialization to underlying bundles does not omit a
harmonic coordinate or add an obstruction equation here.

The source comparison is at one sufficiently small common neighborhood.
The corrected operator tends to zero in the required Sobolev norm with
alpha, by the same slice map used in audited L102. Shrink the parameter
ball once for both members of any pair. In the cited published
Corollary 4.6, last paragraph on p. 89, an arbitrary bundle isomorphism
between such slice operators is parallel for the reference connection
and intertwines their harmonic parts; no smallness of that isomorphism
is assumed. Corollary 4.8(2), pp. 90--91, supplies the converse, and
Corollary 4.9 packages both directions. These statements and the relevant
proof cases were rechecked. They apply to the actual corrected operators,
not to ell alone. The reference Hom connection has zero contracted
curvature because both reference summands have slope zero.

The full effective character is a/b, surjective onto C*. Its weight-zero
monomials have equal positive and negative total degrees, so the complete
676 products generate the polynomial invariant ring. This establishes
the affine quotient coordinates; the analytic quotient is then imported,
not obtained by an unsupported assertion about analytic invariants.
Definition 1 and Theorems 1,2,6 of 2008.04625v3 were rechecked: the
complete integrable zero locus has the restricted action and its
saturation has a reduced analytic quotient inside the ambient affine
quotient. Full-slice equivariance supplies that restricted action here.
Taking reduced structures loses no map from the reduced parameter germ.
L102 ensures p,q are nonzero off the centre; equality of their nonzero
rank-one tensors is precisely the ratio orbit relation. At zero all
products vanish, whereas no punctured parameter has all products zero.
Thus the quotient coordinates classify this entire chosen family,
including its centre, without identifying any weak normalization.

Second, the two Jacobian matrices at zero are respectively diag(1,-1)
and the matrix interchanging s,t. Each determinant is nonzero. Both
inverse-function applications are therefore to convergent functions
with zero constant terms. Their inverse coordinate functions show ideal
equality, not merely equality of radicals. Every other coordinate lies
in m. Multiplication of the two complete coordinate ideals yields exactly
m^2; in particular one cannot replace all products by only selected
squares. No cancellation from higher terms changes this equality.

Third, apply the previously inspected finite-germ criterion in the
ambient C^{676} before defining the image ring. The coordinate ideal's
finite colength makes B finite over C{x_ij}; the action factors through
its kernel, giving the finite A-module B. The kernel is prime, and
analytic finite-image theory identifies this quotient with the actual
reduced image germ. This checks that A is a convergent analytic local
ring rather than a polynomial image or a formal completion. Its maximal
ideal is generated by the coordinate restrictions, its residue field is
C, and integrality gives dimension two. Nakayama therefore applies to
this same finite module. The classes 1,s,t form a basis modulo m_A B,
so three generators suffice. Localizing at A minus zero gives a finite
domain over Frac(A), hence the field Frac(B), and bounds its dimension
by three. Neither flatness nor a free rank-three module follows.

Fourth, Huneke--Swanson Theorem 11.2.7, p. 228, and its complete proof
were rechecked. Here its base is the local Noetherian domain A, its
extension is the module-finite domain B, and I=m_A is maximal-primary.
B has exactly one maximal ideal, dimension two, with residue degree
one. Thus every factor in (2) is accounted for. The reused power and
regular-ring formulas give e_B(m^2)=4. Positivity and integrality of
e_A(m_A), together with d<=3, give d=1 or 2. This does not use a
multiplicity-one converse, normality, or Cohen--Macaulayness of A.
The central length three remains distinct from generic rank.

Finally the imported finite-germ degree theorem applies to the reduced
irreducible image over C; away from a proper analytic subset the finite
representative has d distinct preimages. The same representative can
be shrunk inside the orbit-comparison ball. Consequently its generic
point count is indeed the generic bundle-isomorphism count. This
asserts no uniform count for exceptional fibres or global parameter
spaces. The audit preserves all three direct inputs L094/L101/L102 and
requires no added dependency. It selects neither degree alternative,
constructs no involution, and supplies no quaternionic family, common
kernel, global separation or Hodge class.

## Mathlib

Full matching coverage of the analytic quotient, convergent finite-germ
and multiplicity specialization: **not checked**. Unknown coverage is
not evidence of absence. General inputs are imported by the precise
citations above; the full invariant generation, exact ideal and
degree specialization are proved here. No numerical or Lean certificate
is claimed. The separate critical audit above preserves the stated scope.
