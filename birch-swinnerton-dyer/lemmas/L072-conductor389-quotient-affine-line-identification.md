# L072 — The whole quotient family as affine lines missing zero

## Hypotheses

Use audited L067/L068/L070/L071 for the exact curve
E/Q: y²+y=x³+x²−2x and its origin-preserving rational short model
\(\mathcal E:Y^2=X^3-3024X+46224\). Put
\(V=\mathcal E[7]\,(\overline{\mathbf Q})\), identified with E[7] by
that rational change. It is a two-dimensional F₇-space with its actual
Galois action. No residual-image assumption is imposed.

Let D=Q[Z]/h be L070's entire degree-eight direction field, with its
audited mixed inverse, relative cubic and both full coordinate transports.
Its embeddings into Qbar label all eight one-dimensional subspaces C of V.
Over D let \(\mathcal C\subset\mathcal E_D[7]\) be the order-seven
subgroup supplied by that full cubic, including O. Let
\(\Phi:\mathcal E_D\to\mathcal E'\) be exactly L071's separable
degree-seven quotient with kernel \(\mathcal C\), in its raw short models.
All coordinates and maps are those of the completed certificates;
L069 and all unfinished incidence/action/relation columns are excluded.

Use the dual isogeny \(\widehat\Phi:\mathcal E'\to\mathcal E_D\)
under the canonical elliptic principal polarizations. Define the
D-scheme \(\mathscr K=\ker\widehat\Phi\) and remove its identity
section to form \(\mathscr K^\times\). Regard this same scheme as a
Q-scheme by composition with Spec(D)→Spec(Q). This is not a Weil
restriction. No rational generator of \(\mathcal C\), primitive seventh
root of unity over D, minimal target model or period is assumed.

## Conclusion

The Q-scheme \(\mathscr K^\times\) is finite etale of degree 48.
There is a specified Galois-equivariant bijection

\[
\mathscr K^\times(\overline{\mathbf Q})
\longrightarrow
\{H\subset V:H\text{ is an affine line and }0\notin H\}.
\tag{1}
\]

For the point x in the fiber over direction C, choose any P∈V with
\(\Phi_C(P)=x\). Its image is the subset H=P+C. Conversely a line
H missing zero has direction C=H−H, and any P∈H gives the inverse
\(H\mapsto(C,\Phi_C(P))\). Both choices are independent of representative.
Each direction contributes six nonzero points and six such lines.
The eight identity points of the full Q-scheme \(\mathscr K\) correspond
exactly to the eight lines C through zero, and are precisely the exclusions.

Let \(V^*=\operatorname{Hom}_{\mathbf F_7}(V,\mathbf F_7)\) have its
ordinary contragredient Galois action. The unique functional
\(\lambda_H\) with H={v:λ_H(v)=1} identifies the right side of (1)
with \(V^*\setminus\{0\}\). For a∈F₇×, multiplication by a in the
dual-kernel fiber corresponds to

\[
H\longmapsto aH,\qquad
\lambda_H\longmapsto a^{-1}\lambda_H.
\tag{2}
\]

Thus the identification is a bijection of Galois sets; its functional
labeling is not an identification of the additive groups in a fiber.

Cartier duality retains

\[
\mathscr K_C(\overline{\mathbf Q})
\simeq\operatorname{Hom}(C,\mu_7)
=C^*\otimes_{\mathbf F_7}\mu_7.
\tag{3}
\]

With a fixed choice of Weil-pairing convention and argument order,
one explicit identification (3) is
\(x=\Phi_C(P)\mapsto(c\mapsto e_7(P,c))\).
For a temporarily chosen primitive ζ∈μ₇ define
\(e_7(P,c)=\zeta^{t_x(c)}\). For every g∈Gal(Qbar/Q), transporting
between the C and gC fibers,

\[
t_{g x}(g c)=\chi_7(g)t_x(c),\qquad
\lambda_{gH}(g v)=\lambda_H(v),
\tag{4}
\]

where gζ=ζ^{χ₇(g)}. No trivialization of μ₇ is used to define (1).
Replacing the Weil pairing by its inverse negates every t and leaves
(1), (2) and the action law unchanged.

By finite-etale descent the coordinate algebra of \(\mathscr K^\times\)
is therefore isomorphic over Q to Schaefer–Stoll's algebra B of all
affine lines missing zero, with the conventions above. This does not
give a polynomial presentation, a field-factor decomposition or an
identification with L067's point algebra. It provides no incidence
algebra, norm, functions, complete global units/classes, local bounds,
Selmer containment or successful localization. The other L026 premises,
rational membership, divisible Sha and arbitrary-curve rank comparison
remain unresolved. This is a known-source specialization, not a BSD
candidate. Its separate fixed critical audit below passes under the
unchanged audited-input hypotheses.

## Proof

**Imported theorems and their applicability.** Reuse the inspected
SPECIALIZE assessment
`drafts/literature/2026-10-16-quotient-affine-line-dual-kernel.md`.
The following are named inputs, not general theorems reproved here.

Sutherland, MIT 18.783 Fall 2025,
[Lecture 6, Theorem 6.7, prime-degree Case 1, printed pp.3–4, and Lemma 6.10, p.5](https://math.mit.edu/classes/18.783/2025/LectureNotes6.pdf),
gives the base-field dual, both compositions [deg Φ], and in the
prime-to-characteristic case
\(\ker\widehat\Phi=\Phi(\mathcal E[7])\) on geometric points.
L071 is an isogeny of degree seven over the characteristic-zero field D,
so this exact case applies. The dual has degree seven and is separable.

Milne, *Abelian Varieties*, v2.0 (2008),
[Chapter I Theorem 9.1 and the following prime-to-characteristic paragraph, printed p.41 (PDF p.47)](https://www.jmilne.org/math/CourseNotes/AV.pdf),
identifies the dual-isogeny kernel with the Cartier dual of the original
kernel. Under the canonical elliptic principal polarizations this applies
to the dual above. Its prime-to-characteristic description is Hom(C,μ₇)
with the induced Galois action. The inspected version is the 2008 notes;
no differently numbered 1986 theorem or unread proof reference is used.

Sutherland,
[Lecture 23, Warning 23.21 and Theorem 23.23, pp.10–11](https://math.mit.edu/classes/18.783/2025/LectureNotes23.pdf),
supplies the bilinear alternating nondegenerate Galois-equivariant
Weil pairing \(e_7:V\times V\to\mu_7\). Choose its convention once
and use the argument order e₇(P,c) throughout. Our explicit realization
of (3) below is specified by this formula; it does not assert equality
with an unstated opposite-order isogeny-pairing convention.

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*,
Trans. AMS 356 (2004), 1209–1231,
[author long version, 13 June 2001, Lemma 7.5 and the surrounding definition of B, printed p.16](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
identifies affine lines missing zero with the nonzero ordinary-dual
functionals by their level-one sets. Its following Lemma 7.6 retains
the μₚ tensor factor, rather than identifying the ordinary dual with
E[p]. Here the base is Q and p=7, with the entire set from L067.
Finally use
[Stacks Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR)
for finite etale schemes over a field and finite continuous Galois sets.

The remaining proof checks the applicability and conventions for this
specific whole family. It neither constructs a new duality theorem nor
uses the downstream incidence norm as an input.

**All fibers and their Galois transport.** L070 identifies every embedding
ι:D→Qbar with exactly one direction C. In that fiber L071's cubic has
as roots the x-coordinates of its three inverse pairs, and its kernel
is exactly C, including zero. Thus its quotient \(\Phi_C\) is the
one used in the statement, for every C, not a selected embedding.
If g∈Gal(Qbar/Q), the coefficients of the full D-defined quotient
transport along ι↦gι. Since the source short model and its coordinate
change are rational, this gives

\[
g(\Phi_C(P))=\Phi_{gC}(gP).
\tag{5}
\]

The conjugate of the dual satisfies the defining dual-composition
identities for the conjugate quotient. Uniqueness in the cited dual
theorem identifies it with \(\widehat\Phi_{gC}\). In particular (5)
transports its kernel to the correct kernel over gC. No generator or
choice of quotient-model isomorphism is required: the actual coefficient
conjugates of the D-defined model supply that transport.

The dual-kernel scheme is finite etale of rank seven over D, since
the dual is a separable degree-seven isogeny in characteristic zero.
Its identity section is an open and closed rank-one subscheme over D;
this also follows after splitting the finite etale algebra and descending
the identity subset. Its complement has rank six. Composition with the
degree-eight etale field D/Q gives degrees 56 and 48 over Q, respectively.
The geometric points of the full scheme are pairs (C,x), with x in that
fiber's kernel, rather than tuples choosing one x for every C. This is
why a Weil restriction would be the wrong construction.

**Forward map, inverse and exact exclusions.** The prime-degree dual
theorem gives \(\ker\widehat\Phi_C=\Phi_C(V)\). On V the kernel
of \(\Phi_C\) is exactly C. Consequently

\[
V/C\longrightarrow\ker\widehat\Phi_C,
\qquad P+C\longmapsto\Phi_C(P)
\tag{6}
\]

is an isomorphism of groups, compatible with (5). This uses the
imported torsion-image assertion for surjectivity, not a presumed
identification of two seven-element sets.

Given x≠0, (6) gives a lift P∈V. Two lifts differ by an element of C,
so H=P+C is independent of the lift. Its difference space is C, hence
it is an affine line. It contains zero exactly when P∈C, equivalently
x=0. Conversely let H be any affine line missing zero. Its difference
space C=H−H is a unique one-dimensional subspace; every element of C
is a difference of points of H. Choose P∈H. The value Φ_C(P) is
independent of P because any two choices differ by C. It is nonzero
because otherwise P∈C and H=C would contain zero. It lies in the dual
kernel by the composition identity
\(\widehat\Phi_C\Phi_C(P)=[7]P=0\).
Starting from either side recovers respectively x or H. This proves
the full forward and inverse maps.

Equation (5) sends H=P+C to gP+gC=gH, proving Galois equivariance.
Each V/C has seven elements, of which exactly one is zero. Thus the
eight removed identities correspond to exactly the eight lines C through
zero; all other 8·6=48 lines occur once. The count checks the proved
bijection and is not a substitute for it.

**Ordinary-dual labels and scalar indexing.** For H=P+C missing zero,
P∉C, so V=C⊕F₇P. Define λ_H(c+bP)=b. This is the unique linear
functional vanishing on C and taking value one on P. Replacing P by
P+c₀ leaves the rule unchanged. Its level-one set is exactly P+C.
Conversely any nonzero λ has one-dimensional kernel C and a nonempty
level-one coset; that coset misses zero. These constructions are inverse,
as in the cited Lemma 7.5.

The ordinary dual action is (gλ)(v)=λ(g⁻¹v), since F₇ is constant.
The functional gλ_H has level-one set gH, hence equals λ_(gH).
For a∈F₇×, a line H scales to aP+C, and
λ_(aH)(aP)=1, so λ_(aH)=a⁻¹λ_H. Since Φ_C is a homomorphism,
[a]Φ_C(P)=Φ_C(aP), giving (2). The inverse label law is unavoidable.
For example, λ_(2x)=4λ_x while λ_x+λ_x=2λ_x; hence these fiber
labels do not preserve addition. Identity labels are not defined.

For complete comparison with L068, its forward pullback on torsion
functions is u(P)↦u(aP). Define the forward pullback on the present
family by f(C,x)↦f(C,[a]x). Under (1) it is F(H)↦F(aH), and on
ordinary-dual labels it is G(λ)↦G(a⁻¹λ). Thus the inverse index on
labels is justified, not copied from the point-coordinate action.
The scalar maps fix the base direction, so all these equalities hold
simultaneously in all eight fibers.

**Cartier duality and the cyclotomic action.** For a fixed C define

\[
\theta_C(\Phi_C(P))(c)=e_7(P,c)\quad(c\in C).
\tag{7}
\]

An alternating bilinear pairing is trivial on C×C: if c₁=ru and
c₂=su, then e₇(c₁,c₂)=e₇(u,u)^{rs}=1. Therefore (7) is independent
of the lift P. It is a group homomorphism in x with values in
Hom(C,μ₇). For P∉C and c≠0 in C, e₇(P,c) cannot equal one: otherwise
e₇(P,−) is trivial on both P and c, a basis of V, contradicting
nondegeneracy. Hence (7) has trivial kernel. Both sides have order
seven, so it is an isomorphism, realizing the Cartier-dual description
of the imported theorem with a specified pairing convention. This is
a check on its realization in the present V/C, not a general reproof
of Cartier duality. In characteristic zero the pointwise isomorphism
with its stabilizer-equivariance also gives the corresponding finite
etale group-scheme isomorphism over D.

For every g, the pairing's Galois law and (5) give

\[
\theta_{gC}(gx)(gc)=e_7(gP,gc)
 =g(e_7(P,c))=g(\theta_C(x)(c)).
\tag{8}
\]

Thus the action on Hom(C,μ₇) is the induced one, including the action
on the target. With a single temporary ζ fixed in Qbar, (8) reads
ζ^{t_(gx)(gc)}=ζ^{χ₇(g)t_x(c)}, which proves (4). On the stabilizer
of C this is exactly the action on C*⊗μ₇; across other embeddings it
is the same formula with C replaced by gC. Multiplication by a on x
multiplies t_x by a, whereas its ordinary line label is multiplied by
a⁻¹. If ζ is replaced by ζ^b, every t is multiplied by b⁻¹. None
of these choices changes the geometric coset or λ_H.

In particular Hom(V,μ₇)=V*⊗μ₇, while V* alone has no target
cyclotomic factor. The pairing identifies V with Hom(V,μ₇), not
with V* by a Galois-invariant root-of-unity trivialization. The bijection
(1) and the ordinary functional labels coexist with (7) because they
are different constructions: (7) is linear on each dual kernel and
has domain C for its characters; λ_H is a functional on all V,
annihilating C, with the inverse scalar law. No unexplained extra
twist is attached to the raw quotient family, and no μ₇ factor is
discarded from Cartier duality.

**Descent and limitations.** The Galois-equivariant bijection (1)
identifies the finite etale Q-schemes by Stacks 03QR. On coordinate
algebras its pullback sends an equivariant function F on affine lines
to (C,x)↦F(P+C). This is a Q-algebra isomorphism because the proved
inverse also pulls back equivariant functions. Schaefer–Stoll's B is
exactly that function algebra. Every Galois orbit, hence every possible
field factor, is retained. A degree-48 matching count alone would not
prove this assertion, and no claim that B is a field is made here.

The proof uses the full direction identification and quotient, with
L067's rational coordinate transport and L068's scalar convention.
It requires no new finite arithmetic beyond these audited inputs.
It supplies no explicit coordinates for the dual kernel, incidence
inclusions or norm, and reopens neither stopped column presentation.
There is no arithmetic descent or rank conclusion. Local progress is
the applicability proof and convention check beyond the already imported
sources; no new general mathematical result beyond those sources is claimed.

**Separate critical audit (2026-10-16, step 260).** This is a RESEARCH /
REPRODUCTION proof audit under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-16-quotient-affine-line-critical-audit.md`.
The primary theorem coverage recorded there is reused, including the
prime-degree case and both dual compositions, rather than inferred from
source titles. The full proof above and the relevant canonical passages
of L067/L068/L070/L071 were checked. Their complete arithmetic certificates
are accepted as already audited inputs: this audit does not claim a new
replay of their matrices, cubic coefficients or quotient formulas.

The following checks independently test the load-bearing assembly.

1. **Domain and every fiber.** L070 proves equality with the entire
   scalar-fixed algebra using both inverse identities and the whole
   Reynolds image. Its eight embeddings therefore label eight distinct
   directions, not eight candidate roots with an unproved interpretation.
   L071's full relative cubic and its factorization identify the three
   inverse pairs in each direction. Its geometric extension and exact
   degree argument give the kernel C including O on every fiber. Thus
   the dual theorem applies over D itself in characteristic zero, and
   then after every embedding. No rational generator is needed.

2. **Both maps and conjugation.** For any x in a dual-kernel fiber the
   imported equality ker(hat(Phi_C))=Phi_C(V) supplies a lift, and
   ker(Phi_C|V)=C makes the fiber of that lift exactly P+C. Conversely
   the direction of an affine line is recovered intrinsically as H-H;
   its image under Phi_C is independent of its point and is in the
   dual kernel by hat(Phi_C)Phi_C=[7]. These facts check both composites,
   not merely injectivity followed by a size comparison. Conjugation
   sends the actual coefficient-defined source, target and map to those
   indexed by gC. The conjugated dual satisfies the same defining
   composition and hence is the unique dual for that conjugate map.
   Consequently both inverse maps commute with every g, including g
   moving the base embedding. No unchosen isomorphism of quotient models
   or special embedding enters the descent.

3. **Scheme and exclusions.** Separability gives a finite etale
   rank-seven kernel over D. Its identity is a D-section and an open
   and closed rank-one subscheme; the complement has rank six. Viewed
   over Q, the identity subscheme is Spec(D), not one rational point:
   it has exactly eight geometric points. Composition gives degrees
   56 and 48, whereas a Weil restriction would parametrize tuples and
   would not have this geometric set. The lift criterion x=0 iff P in C
   removes exactly those eight identities and exactly the eight lines
   through zero. Finite etale descent applies to the already established
   equivariant inverse maps. Its algebra map is contravariant pullback
   F -> ((C,x) -> F(P+C)); the inverse pulls back in the other direction.
   All orbits are retained, without a fieldness assertion for B.

4. **Independent scalar/action check.** In a fixed fiber choose a basis
   (c,p) with c in C and x=Phi_C(p). Then lambda_x(c)=0 and
   lambda_x(p)=1. For any a != 0, lambda_[a]x(p)=a^(-1), while
   theta_C([a]x)(c)=theta_C(x)(c)^a. This checks the inverse label and
   forward character laws on a full basis. To test compatibility with
   the twist, let g stabilize C and write gc=alpha c,
   gp=beta c+delta p, with alpha and delta nonzero. Put
   zeta=e_7(p,c), which is primitive by nondegeneracy. Bilinearity and
   Galois equivariance give alpha*delta=chi_7(g). The quotient action
   is gx=delta x; the ordinary functional action is
   g lambda_x=delta^(-1)lambda_x; and the induced character action is
   chi_7(g)*alpha^(-1)=delta on the exponent at c. Thus the two labels
   have exactly their stated distinct transformations, with no missing
   twist. This test assumes neither that g is arbitrary in GL_2 nor
   that any specified matrix occurs in the actual Galois image. For
   elements moving C, equation (8) supplies the transport between fibers.

5. **Pairing and scope.** Triviality of e_7 on C times C makes theta
   independent of its lift. If P is outside C, any nonzero c in C
   together with P is a basis, so e_7(P,c)=1 would contradict
   nondegeneracy. This verifies injectivity, and order seven then gives
   the stated character isomorphism. Stabilizer-equivariance descends
   it over D. It realizes a Cartier-dual isomorphism with the specified
   argument order; it does not identify it with an unspecified sign
   convention for the canonical isogeny pairing. Reversing the pairing
   negates exponents, while changing zeta rescales them, and neither
   changes the geometric cosets or ordinary functionals. The explicit
   forward function pullback agrees with L068's convention after the
   necessary inverse relabeling.

All audit tests pass; no unsupported claim, mathematical correction or
new hypothesis was found. The result is a verified fixed applicability
assembly of the cited theorems, not mathematics beyond those sources.
The DAG's direct inputs L067/L068/L070/L071 are exactly the local inputs
used here; L069 and unfinished columns contribute none. ATTEMPTS/035--036
remain valid cost stops. No explicit dual-kernel polynomial, field
decomposition, incidence/norm or arithmetic descent certificate is
produced, and no BSD rank gap is closed. No new numerical check or
mathematical script is needed for this abstract audit.

## Mathlib

Full matching Mathlib coverage for this whole-family identification,
its finite-etale algebra, dual-isogeny compatibility and scalar/twist
conventions was not checked. Unknown availability is not absence.
The precise primary theorem citations above supply the mathematical
inputs. This informal specialization is not a Lean formalization.
