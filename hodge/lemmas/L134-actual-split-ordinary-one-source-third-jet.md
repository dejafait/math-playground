# L134 — Ordinary one-source third jet at an actual split fibre

## Hypotheses

Retain L133's identical marked projective K3 factors S_1 and B=S_2,
their common hyperkähler metric g and ordered structures I,J,K.
Suppose its locally free Omega-polystable rank-two F exists, with
integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D. Select a split
parameter z with F_z=L direct sum L^{-1}, c_1(L)=k, k^2=-14 and
k.h=0. Neither existence assumption is established here.

Use the actual determinant-one compatible connection, L094/L095's
actual harmonic derivative, and L132's holomorphic base change alpha
into the complete harmonic integrability germ, with its actual family
isomorphism. Allow an arbitrary constant parallel complex central
marking and all smooth comparison gauges as in L132. The harmonic
representation is H=H_+ direct sum H_-, with effective action
(p,q) -> (ap,a^{-1}q). Use arbitrary linear coordinate functions
p_i on H_+ and q_j on H_-, 1<=i,j<=26.

Put A=O_{B^{an},z}, m=m_z, and let R_z be the ordinary reduced
analytic local ring of the image of L133's map from this one source
germ. Its pullback embeds R_z in A. Other source germs over the same
coarse point are not included in R_z.

## Conclusion

Both weight projections of d alpha_z have complex rank two. There
are holomorphic coordinates (s,t), centered at z and normal for the
Kähler connection at z, in which the complete embedded image is

\[
 \operatorname{im}(R_z\longrightarrow A/m^4)
   =\mathbf C\oplus
           \operatorname{span}_{\mathbf C}\{s^2,st,t^2\}.       \tag{1}
\]

The nonconstant part has square zero in A/m^4. The image has complex
dimension four, inside the ten-dimensional source jet ring. This
specifies the embedded image, not only its associated graded space.

In arbitrary centered holomorphic coordinates x=(x^1,x^2), put
C_x(x,x)^a=Gamma^a_{bc}(z)x^b x^c, using the holomorphic Christoffel
symbols of g. Then the same image is

\[
 \left\{c+q(x)+\tfrac12\sum_a(\partial_a q)(x)C_x(x,x)^a
       \pmod {m^4}:c\in\mathbf C,\ q\in\operatorname{Sym}^2(\mathbf C^2)^*
       \right\}.                                             \tag{2}
\]

This conditional ADVANCE / REPRODUCTION specializes the assessed
slice, curvature and ordinary quotient tools. The separate critical
audit below preserves the conclusion. It supplies neither higher-order parity, an involution,
local degree, image normality, a global normalization-defect inequality,
a split parameter nor F. Reconstruction, transverse transport and
universal primitive Hodge realization remain unresolved.

## Proof

**Imported analytic scope.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-19-actual-split-one-source-third-jet-ring.md`.
The ordinary quotient input is Buchdahl–Schumacher, *An Analytic
Application of Geometric Invariant Theory*,
[arXiv:2008.04625v3, Definition 1 and Theorems 1–2, pp. 4–6;
Definition 3, Section 2.2, equations (2.1)–(2.3), Remark 3 and
Theorem 3 with its general-case proof, pp. 6–8](https://arxiv.org/pdf/2008.04625v3#page=4).
Its reductive linear action, invariant analytic-subspace and saturated
representative hypotheses were checked for this complete harmonic
slice in audited L133. L103 supplies the polynomial quotient coordinates
X_{ij}=p_iq_j for the representation, independently of its selected
family. The cited theorem makes the reduced integrable quotient an
ordinary analytic subgerm of that affine quotient, hence of C^{676}.
L133 identifies this ordinary germ with the actual fixed-H reduced
coarse germ, compatibly with the actual family map and its one-source
image ring. These general results are imported; the following rank
and finite-Taylor calculations are the specialization needed here.

**Actual weight ranks.** First use a unitary central marking. In
L094's real harmonic space V write G for its positive inner product,
T=[xi,-], and pi_+,pi_- for the two I-complex weight projections.
On H_+ one has T=2I and on H_- one has T=-2I. L095 makes the actual
derivative injective and quaternionic. Its image W therefore has real
dimension four and is I-complex of dimension two. L094's actual-family
necessary obstruction gives, for every w in W,

\[
 0=\mu_I(w)=\tfrac12G(ITw,w)
             =-\|\pi_+w\|^2+\|\pi_-w\|^2.                  \tag{3}
\]

The weight spaces are G-orthogonal by the unitary circle action.
Thus each norm squared in (3) equals \|w\|^2/2. Each projection is
injective on W and complex-linear, so each has complex rank two.
The real/Dolbeault harmonic identification in L094 is I-complex-linear;
L132 identifies d alpha with this actual derivative up to a constant
central marking. An allowed nonunitary marking multiplies the two
blocks by nonzero complex constants and preserves the ranks. The
equal-norm statement is used only before this marking. No identification
with L094's example plane is required.

Let ell=d alpha_z in centered holomorphic source coordinates and write
u_i=p_i ell, v_j=q_j ell. Both sets span the entire two-dimensional
source cotangent space. Products u_i v_j span its whole symmetric
square: any two linear forms can be expanded in these respective
spanning sets, and their products span all quadrics. Its dimension
is three.

**Source coordinates and every generator's cubic term.** A Kähler
metric has, in holomorphic coordinates x, only Christoffel coefficients
Gamma^a_{bc} and their conjugates, with Gamma^a_{bc}=Gamma^a_{cb}.
Indeed the Koszul formula gives
Gamma^a_{bc}=g^{a bar d} partial_b g_{c bar d}; the Kähler identity
partial_b g_{c bar d}=partial_c g_{b bar d} gives symmetry and zero
mixed coefficients. The polynomial holomorphic change

\[
 w^a=x^a+\tfrac12\Gamma^a_{bc}(z)x^b x^c                       \tag{4}
\]

has identity differential and a convergent local inverse. The connection
transformation formula gives Gamma_w(z)=Gamma_x(z)-Gamma_x(z)=0,
since the inverse change has second derivative -Gamma_x(z). Its
conjugate removes the antiholomorphic coefficients; the mixed ones
were already zero. This is normality at z alone, not flatness or a
higher normal-form assertion. Write (s,t)=w.

In these coordinates audited L132 (7) gives the full homogeneous
quadratic Taylor coefficient of the actual alpha, in all four real
directions, as

\[
                    \alpha_2(w)=[\phi(w),\ell(w)],              \tag{5}
\]

where phi is real-linear, takes values in the parallel complex central
Lie algebra, and may have antiholomorphic dependence. The source
Christoffel term is zero because Gamma_w(z)=0. Constant nonunitary
marking is already allowed in L132's formula. For any invariant
homogeneous quadratic Q, infinitesimal invariance gives
dQ_h([a,h])=0 for every central Lie algebra element a. Thus

\[
 Q(\alpha(w))=Q(\ell(w))
          +dQ_{\ell(w)}[\phi(w),\ell(w)]+O(|w|^4)
          =Q(\ell(w))+O(|w|^4).                              \tag{6}
\]

Since Q alpha is holomorphic, vanishing of its real cubic Taylor
coefficient is exactly vanishing of its holomorphic cubic coefficient.
Apply this separately to every Q=p_iq_j. Each generator pullback is
u_i(w)v_j(w) modulo m^4. Their span is exactly all three quadrics.
In particular cancelling quadratic terms also cancels the entire cubic
jet. This establishes individual cubic corrections as well as L132's
constraint on cancellations.

In arbitrary x, L132 instead gives
alpha_2=ell(C_x(x,x))/2+[phi(x),ell(x)]. For q=Q ell the chain rule
gives dQ_{ell(x)}ell(C_x(x,x))=dq_x(C_x(x,x)). Each generator's jet
is therefore q+dq(C_x)/2. Equivalently expand q(w) under (4). This
proves the coordinate formula needed in (2).

**All ordinary analytic elements and all cancellations.** The embedded
analytic quotient supplies a surjection C{X_{ij}} -> O_{Y,0}. Its
further quotient onto R_z is surjective by the one-source image
definition and L133. Every element of R_z thus has a representative
convergent germ h(X). This uses an ambient analytic representative;
it does not identify a polynomial ring with an analytic local ring.

Write its Taylor expansion in the form

\[
 h(X)=c+\sum_{i,j}a_{ij}X_{ij}
             +\sum_{i,j,k,l}X_{ij}X_{kl}h_{ij,kl}(X),           \tag{7}
\]

with convergent germs h_{ij,kl}. There are finitely many coordinate
pairs. One obtains (7) by assigning each Taylor monomial of degree
at least two to two of its factors; the resulting subseries converge
on a smaller polydisc. Each X_{ij} pulls back into m^2. The final
sum in (7) consequently pulls back into m^4. Equations (6) and (7)
show that every ring element's jet is a constant plus a source quadric
in normal coordinates. Conversely the generator quadrics span all
source quadrics, and the constant function supplies the constant.
This proves (1). The arbitrary-coordinate calculation proves (2)
for all analytic elements at once.

Relations in the quotient or image ring cannot produce extra jets:
each analytic representative has been treated, and a linear combination
with vanishing quadratic part also has vanishing cubic part. Products
of nonconstant image jets have order at least four and are zero in
A/m^4. Source monomials of degrees 0,1,2,3 have dimensions 1,2,3,4,
so the ambient jet dimension is ten and the image dimension is four.

No order at least four is controlled. Higher odd terms can still occur;
the truncated ring establishes neither an involution, a degree-two map,
normality nor the length of an untruncated normalization quotient.
Other source germs over the same coarse point remain separate.

**Independent critical audit, 2026-10-20 (step 414).** The unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-actual-split-third-jet-critical-audit.md`
covers precisely this audit. Reuse the cited ordinary analytic quotient
theorem and the audited actual-family inputs within their stated scopes.
The following checks find no substantive error, required repair or
stronger conclusion. This audit is EXPLORATION / REPRODUCTION; it does
not relabel the existing conditional calculation as a new advance.

First, the real obstruction is available for every vector of the actual
derivative plane. For each real source tangent, the actual smooth ASD
family has a Coulomb representative, so its second curvature equation
pairs to zero with the diagonal harmonic obstruction. L094 identifies
that pairing with G(ITw,w)/2. L095 identifies the slice derivative with
the harmonic mixed curvature and gives its strictly positive norm.
Thus W is a four-real-dimensional quaternionic subspace and neither a
zero derivative nor merely L094's example plane is being substituted.
The two unitary weight sectors are orthogonal; T=2I on one and -2I on
the other gives IT=-2 and +2, respectively. Equation (3) therefore
forces each projection's squared norm to be G(w,w)/2. A zero projection
forces w=0. Their I-complex linearity and dim_C W=2 give both ranks
equal to two. The map a to a^{0,1} is I-complex-linear, and a constant
parallel complex marking scales each block invertibly. Only the ranks,
not an unchanged Hermitian norm, are transported through that marking.

Second, the normal-coordinate sign can be checked directly in the
inverse change. Equation (4) has inverse
x^a=w^a-Gamma^a_{bc}(z)w^b w^c/2+O(|w|^3).
At the center the transformation law is
Gamma_w^a{}_{bc}=Gamma_x^a{}_{bc}+partial_b partial_c x^a=0.
The Kähler mixed coefficients vanish, and the conjugate inverse removes
the conjugate coefficients. Hence the full real source connection
vanishes there; this requires neither flatness nor real analyticity of
g. Conversely substitution into any homogeneous quadratic q gives
q(w(x))=q(x)+dq_x(C_x(x,x))/2 modulo m^4. The sign and the factor
in (2) agree with the Hessian formula, not its negative.

Third, L132's full formula (7), rather than only its invariant-vanishing
conclusion, applies in these coordinates. It was obtained by projecting
the differentiated actual Bianchi identity at the central connection;
the horizontal term is exact, the source connection is retained, and
the comparison is an isomorphism of actual families. Its first gauge
derivatives are parallel diagonal endomorphisms because the two first
connection derivatives are harmonic. Its unrestricted second gauge
derivatives are exact after projection. These facts leave precisely
the source term and [phi(w),ell(w)], including arbitrary smooth gauges
and a constant nonunitary marking. In normal coordinates write the
effective diagonal coefficient of phi(w) as a(w). Then the quadratic
weight coefficients are a(w)u_i(w) and -a(w)v_j(w), respectively.
The cubic coefficient of the individual product is exactly
u_i(-a v_j)+(a u_i)v_j=0. This identity holds for every real w even
if a has antiholomorphic dependence. Holomorphicity of the product
then identifies it with vanishing of its entire holomorphic cubic jet.
In arbitrary coordinates the additional term is precisely
d(u_i v_j)_x(C_x(x,x))/2. Thus every generator, not just a combination
with zero quadratic part, has the asserted jet.

Finally, L133 identifies the ordinary reduced quotient and its actual
map into the one chosen source ring. Its finite-image kernel gives a
quotient of O_{Y,0}, while the embedded quotient gives a surjection
C{X_{ij}} onto O_{Y,0}. These two surjections justify an ambient
convergent representative for every element of R_z; no normalization
or polynomial-only replacement occurs. In that convergent power-series
ring the square of the coordinate maximal ideal is generated by the
finitely many X_{ij}X_{kl}. Subtracting the constant and linear Taylor
parts therefore yields exactly (7), with convergent coefficients.
Every product pulls back into m^4 since every X_{ij} has source order
at least two. This proves the upper containment for every analytic
representative, including arbitrary cancellations and quotient
relations. Both projected cotangent spans have dimension two, so
linear combinations of their products give all source quadrics. The
generator calculation supplies those quadrics themselves modulo m^4,
proving the reverse containment. Constants and the three independent
quadrics give dimension four; no linear or cubic class survives, and
products of the three nonconstant classes vanish in this truncation.

The existing DAG inputs L094, L095, the representation-only part of
L103, L132 and L133 cover these uses. No dependency or main argument
has changed. ATTEMPTS/061–063 and the parked flat-source product-jet
test are unaffected. The result concerns one source germ only, assumes
both F and a split parameter, and does not determine higher odd terms,
local degree, normality, a full normalization defect or a global bound.

## Mathlib

Full matching coverage of this conditional harmonic-family and ordinary
analytic jet specialization is **not checked**. The general analytic
quotient is imported by the precise citation above. The weight ranks,
coordinate change, cubic computation and complete analytic truncation
are proved here without a numerical certificate or formalization.
