# L143 — Quartic representation of every rational reverse connecting class

## Hypotheses

Work over Q with the actual smooth proper curves and maps of audited
L110, L111, L113, L127 and L142. In particular,

    Q4(T)=7+52T−6T²−64T³−25T⁴,
    B: W²=11(T²−4)Q4(T), E: R²=−33Q4(T),
    q_+=(2,0)∈B(Q), O_E=(2,165)∈E(Q),
    A=Jac(B)×E, J=Jac(C), F:A→J, G:J→A,
    GF=[2]_A, FG=[2]_J.

Here E is identified with Pic^0(E) by P↦[P−O_E]. Use L142's
actual embeddings, not merely abstract isomorphism types. Put
A_4=Q[T]/(Q4), let θ be its distinguished root, and let Ω be its
four geometric roots. Write M=F_2^Ω, N=M/<1>, and K=ker G.
The fixed identification ι:N→K sends the i-th basis vector to

    z_i=alpha^*p_B^*[q_i−q_+], q_i=(θ_i,0)∈B.

Thus ι is exactly L142's identification. We identify signs with
F_2 via (−1)^v. For the final comparison to the odd-model Kummer
coordinate, use L138's actual transport η=−36300/(θ−2).
No rank, full Selmer image, class/unit basis or point completeness is
assumed. This is a known-theory specialization accepted by the separate
critical audit below, not a complete Beal candidate.

## Conclusion

The coefficient sequence induces an injection

    j: A_4*/(Q* A_4*²) ↪ H¹(Q,K).

Every rational G-connecting class lies in its image. More precisely,
for x∈Jac(B)(Q) and e∈E(Q), choose rational degree-zero divisors
D_B,D_E representing x,e, with support away from the quartic branch
points and T-infinity on their respective curves. Define

    λ_B(x)=[(T−θ)(D_B)], λ_E(e)=[(T−θ)(D_E)]
                         in A_4*/(Q* A_4*²).

Evaluation at a closed point means the norm from its residue algebra
after base change to A_4; extend multiplicatively to divisors, including
negative coefficients. These classes are well-defined and

    δ_G(x,e)=j(λ_B(x)λ_E(e)).                              (1)

Consequently

    (x,e)∈G(J(Q))  ⇔  λ_B(x)λ_E(e)=1.                    (2)

The general obstruction to coefficient representation is the boundary

    ∂:H¹(Q,K)→Br(Q)[2]

from the diagonal μ_2 sequence; im j=ker ∂. Formula (1) proves
∂δ_G=0 on all A(Q), not that ∂ is zero on all H¹(Q,K).
No nonzero obstruction class in that larger group is asserted here.

For rational points where the displayed evaluations are defined,

    λ_B([q−q_+])=[(T(q)−θ)/(2−θ)],
    λ_E([P−O_E])=[(T(P)−θ)/(2−θ)].                        (3)

The E formula applies to every P∈E(Q), by L142's rational-fiber
check. In L138's odd-model coordinate, λ_B is the quartic component
of the ordinary Jacobian Kummer value, further taken modulo Q*.
This identifies an evaluation interface, not a nonredundant class
filter or an improvement on L141's rank bound.

## Proof

### Imported comparison and precise scope

Use the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-26-reverse-isogeny-quartic-class-representation.md`.
The general comparison is N. Bruin, B. Poonen and M. Stoll,
*Generalized explicit descent and its application to curves of genus 3*,
Forum Math. Sigma 4 (2016), e6,
[DOI 10.1017/fms.2016.1](https://doi.org/10.1017/fms.2016.1),
[74-page author manuscript](https://math.mit.edu/~poonen/papers/genus3.pdf),
retrieved 2026-10-26. References below use that manuscript's printed
pages: Section 4, especially Remark 4.1 and Proposition 4.2, pp.6–8;
Remark 6.5 and Definition 6.7, p.16; Section 6.3.1, p.17;
equation (8) and Proposition 6.10, pp.18–20.

For a fake datum div(f)=2β−D×Δ on a smooth projective geometrically
integral variety, Proposition 6.10 identifies degree-zero cycle evaluation
with the multiplication-by-two connecting map followed by the Cartier
dual of the branch-difference map. Equation (8) identifies its coefficient
subgroup with the Brauer-boundary kernel. We import these results;
the instance checks below identify the maps without assuming that G is
the polarized dual of F. The source's general proof is not repeated.

For rational divisor representability use E.F. Schaefer, *Computing
a Selmer group of a Jacobian using functions on the curve*, Math.
Ann. 310 (1998), 447–471,
[DOI 10.1007/s002080050156](https://doi.org/10.1007/s002080050156),
[corrected arXiv:1507.08325v1](https://arxiv.org/pdf/1507.08325v1),
29 July 2015, Proposition 2.7 and its proof, printed pp.9–10.
Its rational-point case gives representatives for every rational
Jacobian class, as its proof states, not merely representatives over
an unspecified extension. Both q_+ and O_E are rational, so the
index is one on each curve. Remark 6.5 of Bruin–Poonen–Stoll moves
these representatives off any prescribed finite set. We do not import
Schaefer's separate cohomological injectivity assumption for G.

### Actual divisor data and rational cycles

Let H_B,H_E be the effective degree-two T-infinity fiber divisors,
not the classes 2q_+ and 2O_E by definition. For each i let
e_i=(θ_i,0)∈E. Simple branching and the even-degree models give
the divisor identities

    div_B(T−θ_i)=2q_i−H_B,
    div_E(T−θ_i)=2e_i−H_E.                               (4)

Indeed T−θ_i has order two at that branch point and order minus one
at each geometric infinity. The actual constants in both equations
are retained; they change neither these orders nor the actual points.
The graphs β_B=(q_i) and β_E=(e_i) over Δ=Spec A_4 are divisors
defined over Q. Equation (4) gives two fake data with n=2.

Equivalently, their product datum on X=B×E is

    β_i=pr_B^*q_i+pr_E^*e_i,
    D_X=pr_B^*H_B+pr_E^*H_E,
    f_i=(T_B−θ_i)(T_E−θ_i), div(f_i)=2β_i−D_X.            (5)

The product is smooth, projective and geometrically integral over Q;
its Albanese and Picard varieties are the products for B and E.
The point (q_+,O_E) fixes the stated Albanese normalization A.
These facts also follow directly by using the two factor data and
their sum, so no Prym polarization formula is used in (5).

Every (x,e)∈A(Q) is represented by the degree-zero cycle on X
obtained from D_B on B×{O_E} plus D_E on {q_+}×E. The divisor
representatives exist by the cited rational-point case and can avoid
the quartic branches and infinities. The fixed points q_+,O_E are
good for (4), because Q4(2)=−825≠0. Evaluating (5) on this cycle
gives exactly

    (T−θ)(D_B)(T−θ)(D_E):                                (6)

the extra constant factors (2−θ) have exponents deg D_B=deg D_E=0.
Thus the product-target cycle representability is explicit. A rational
point of A has not been presumed to be a rational point of X.

### The finite pairing check fixes the coefficient identification

The dual of N is M_even under

    <[v],s>=(−1)^(sum_i v_i s_i).

For s the indicator of an even subset S⊂Ω, the branch-difference
map of (5) is

    s↦(x_S,e_S),
    x_S=[sum_(i∈S)q_i−(|S|/2)H_B],
    e_S=[sum_(i∈S)e_i−(|S|/2)H_E].                      (7)

To see the degree-zero convention, lift s to an integer vector of
sum zero by subtracting |S| at a chosen branch index. Since twice
that branch divisor is equivalent to H, its class is precisely (7).
The all-ones vector maps to (ε,0), as in L142; it is not discarded
in M_even. The embedded image of (7) is exactly ker F by L142.

We check the corresponding Cartier-dual map γ:A[2]→N, rather than
infer it from dimensions. Use the canonical Jacobian Weil pairings
from the cited Section 4. In the even branch-subset descriptions on
these two curves the pairing is

    e_2(t_U,t_V)=(−1)^|U∩V|.                             (8)

Here is a finite check of the labels in (8). It is included because
this pairing identification is essential to the specialization. For
four distinct branch coordinates a,b,c,d, the divisors p_a−p_b and
p_c−p_d have disjoint support, and the pairing evaluation uses the
functions (T−a)/(T−b) and (T−c)/(T−d). Their evaluation quotient is

    [((c−a)/(c−b))/((d−a)/(d−b))]
    / [((a−c)/(a−d))/((b−c)/(b−d))] = 1.

For B, fix a two-element subset U. Even subsets of the four
complementary branches inject into Jac(B)[2], span a three-dimensional
space, and pair trivially with U by this calculation and bilinearity.
They are therefore exactly its orthogonal space, which has dimension
three by nondegeneracy. A pair meeting U once cannot be represented
by such a subset, even after taking its complement in the six branches;
its pairing is consequently −1. The pair U itself is orthogonal by
alternation (and is represented by the four-element complement).
This checks all pair generators and hence (8) on B. For E, the
nonzero two-torsion classes are the three pair partitions of four
branches. Equal or complementary pairs give the same class; distinct
nonzero classes pair to −1 in the nondegenerate alternating
two-dimensional space. This proves (8) for E as well. Complementing
an even subset changes no pairing sign. The argument verifies the
finite labels using the imported Weil pairing; it reproves no general
duality or descent theorem.

Represent t_B∈Jac(B)[2] by an even subset U_B of its six branches,
and let r∈M be the indicator of U_B∩Ω. Then (8) gives

    e_B(t_B,x_S)=(−1)^(r·s).

L142's actual quotient map sends alpha^*p_B^*t_B to ι([r]):
explicitly t_B=sum_i r_i[q_i−q_+]+u_−[q_−−q_+], and the last
term is killed by p_B^*. Complementing U_B changes r by 1,
which is zero in N. Thus the B-component of γ is exactly
ι^(-1)alpha^*p_B^* on Jac(B)[2].

Represent t_E by an even subset U_E⊂Ω, modulo complement, with
indicator v. Formula (8) gives e_E(t_E,e_S)=(−1)^(v·s).
L142's branch-pullback identity gives
alpha^*p_E^*t_E=alpha^*p_B^*x_(U_E)=ι([v]). Therefore

    ι γ(t_B,t_E)=alpha^*(p_B^*t_B+p_E^*t_E)
                 =F(t_B,t_E),   (t_B,t_E)∈A[2].          (9)

This verifies the actual Galois-equivariant coefficient map, including
the embeddings and the diagonal scalar convention. It neither uses
a square-root choice at a branch nor identifies H_E with 2O_E.

### Connecting-map comparison and the obstruction

For a=(x,e)∈A(Q), choose b∈A(Qbar) with 2b=a. Since GF=[2],
the point F(b)∈J(Qbar) is a G-preimage of a. Hence the defining
cocycles give

    δ_G(a)=[σ↦F(σb−b)]=F_*δ_(2,A)(a).                  (10)

This is the ordinary functorial connecting construction, specialized
with the actual F,G. It is also a direct verification of the needed
functorial diagram; knowing only abstract kernel orders would not
have given (9).

Apply Proposition 6.10 to the datum (5), or to the two factor data
and add. Its cohomological map is γ_*δ_(2,A). Equations (6), (9)
and (10) identify this map, after ι, with the coefficient expression
in (1). Every rational target class has a representing cycle, so
there is no remaining cycle-representability assumption.

For clarity, the coefficient injection is induced by

    1→μ_2→Res_(A_4/Q) μ_2→N→1,

where the first arrow is diagonal. Kummer theory and equation (8)
of the cited source give the exact portion

    Q*/Q*²→A_4*/A_4*²→H¹(Q,N)→H²(Q,μ_2)=Br(Q)[2].

Thus its quotient by the image of Q* is injective, with image exactly
the boundary kernel. Transport by ι defines j and ∂. This also
shows that the product value in (1) is unique, and establishes its
independence from divisor choices. The individual factor values are
well-defined by the same comparison, applied with the other factor
zero, and the coefficient injection. Exactness of the isogeny
connecting sequence then proves (2). The image of all H¹(Q,K) has
not been replaced by this coefficient quotient.

### Evaluation conventions and the odd-model interface

For any good closed point, (T−θ) is an invertible element of its
residue algebra tensored with A_4, so its norm is in A_4*. Movement
off the finitely many bad fibers treats all rational divisor classes,
including classes initially supported at branch points or infinity.
It supplies a definition there, not an evaluation of zero as a unit.
On good point differences it gives (3) directly. In particular
λ_E(O_E)=1 and λ_B(0)=1. L142 proves that every rational E-point
has finite T and nonzero R, so none of its quartic branches or infinity
fibers is an unhandled rational exception.

To compare to L138, put c=−36300, X=c/(T−2), η=c/(θ−2).
On the common good open the exact identity is

    X−η=−c(T−θ)/((T−2)(θ−2)).                            (11)

For a degree-zero rational divisor D_B, the factor −c/(θ−2)
evaluates to its zeroth power, while (T−2)(D_B) belongs to Q*.
Consequently [(X−η)(D_B)]=[(T−θ)(D_B)] modulo Q* A_4*².
Move D_B away also from T=2 when using (11), and from T=−2 when
evaluating the full odd-model Kummer tuple. These are permissible
additional finite support exclusions. The already proved
choice-independence extends the identity to every x. This is exactly
the quartic component of the usual odd-model evaluation; it does not
identify its additional rational component or erase that component
from L138's full odd-model Kummer map.

As a consistency check within the exact scope, good rational same-T
point pairs give two identical factors in (3); their product is a
square. Thus this formula respects L142 and ATTEMPTS/062. It does
not reopen that stopped extra-obstruction shortcut.

### Result and remaining limitations

The bounded target is affirmative: all rational G-images in cohomology
have the specified quartic representation, and the general boundary
obstruction vanishes on them. This is REPRODUCTION of known descent
theory at the actual instance, not a claim of progress beyond the
sources checked. The checks above are exact divisor, finite-module and
cocycle calculations; no numerical script or class enumeration is needed.

There is still no evaluated mixed constraint on independently retained
global or local candidate classes, no comparison proving additional
pruning against L138–L141, and no improvement on rank Jac(B)(Q)≤9.
A rational J-class lifting (x,e) need not be in C's Abel image.
Full descent, marked point control, degree-nine and integer recovery,
both retained systems and other Beal signatures remain unresolved.
The separate audit below accepts the finite pairing and cycle/comparison
argument as an input with precisely these limitations.

### Separate critical instance audit — 2026-10-26

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-26-reverse-coefficient-critical-audit.md`.
This audit accepts (1)–(3), including all rational target classes,
without changing the theorem's hypotheses or conclusion. The extra
support exclusion at T=−2 in the odd-model comparison is made explicit
above; it is allowed by the existing moving argument. This is a
verification of a known-theory specialization, not an additional
descent theorem or a new rank estimate.

**Source applicability and cycles.** Rechecked the cited
Bruin–Poonen–Stoll Section 4 pairing comparison, Definition 6.7,
Remark 6.5, Section 6.3.1, equation (8) and the complete Proposition
6.10 proof in the 74-page author manuscript. In particular its
comparison begins on cycles; Corollary 6.11 does not silently remove
that restriction. Schaefer's Proposition 2.7 proof, printed p.10,
allows K†=Q here: both curves have the displayed rational point.
It therefore gives a rational degree-zero divisor for every rational
class, rather than only representatives modulo an isogeny.

L110/L111 give smooth proper geometrically integral factors; their
product has the same properties. Its Albanese is A, and its Picard
variety is the product of the factor Picard varieties. The factor
inclusions based at q_+ and O_E induce the two summand inclusions
on Albanese varieties. Thus the cycle constructed from D_B and D_E
maps to exactly (x,e), including when neither class is represented
by one rational point difference on B.

For each quartic root θ_i, simplicity gives a double zero of T−θ_i
on each factor. The even-degree infinity chart gives a simple pole
at each of its two geometric infinities. Hence the actual divisors
in (4) have degree zero and give the asserted product datum; its
divisors on X are Cartier. Neither q_+ nor O_E lies in the removed
fibers, since Q4(2)=−825. Moving D_B,D_E on the factors suffices
to make their product cycle good. For a closed point of degree d
on the first embedded factor the second coordinate contributes
(2−θ)^d, and conversely for the other factor. Each total degree is
zero, so both extra constants cancel. These checks establish the
all-rational-target applicability needed by Proposition 6.10.

**Independent embedded-map check.** Work over Qbar to label the
four roots 1,2,3,4; the calculation below is equivariant under their
permutations. Write b_i=[q_i−q_+] and take

    b_1,b_2,b_3,b_4, e_12,e_13

as an F_2-basis of A[2], where e_ij is the branch-pair class on E.
The four b_i are independent: any sum has an even-subset representative
with q_− absent, so cannot be the full six-element branch set; its
class vanishes only for the empty sum. The two elliptic classes are
distinct nonzero elements of E[2]. Let s_12,s_13,s_14 be the basis
of M_even consisting of the indicated two-element subsets.

The pairing formula (8) survives a direct check. For disjoint pairs
the displayed cross-ratio quotient is one, including the pairs
containing q_±. For any fixed pair on B, the even subsets of its
four-branch complement inject and form a space of dimension three;
the disjoint-pair calculation puts that whole space in the orthogonal
space. Nondegeneracy makes the two spaces equal. A pair intersecting
the fixed pair once has neither it nor its complement contained in
that four-branch complement, so its sign is minus one. Alternation
handles the fixed pair itself. These cases cover the pair generators,
and bilinearity covers all subsets. On E, any two distinct nonzero
classes in the two-dimensional symplectic space have sign minus one.
Thus this check fixes the labels, not just the abstract pairing type.

Using additive sign exponents, pairing the six basis columns above
with the three branch-difference rows (x_s,e_s) gives the complete
matrix

    rows s_12,s_13,s_14; columns b_1,b_2,b_3,b_4,e_12,e_13:
    [1 1 0 0 0 1]
    [1 0 1 0 1 0]
    [1 0 0 1 1 1].

For example the last two columns are the intersections of {1,2}
and {1,3} with the row subsets; the B columns are their single-root
incidences, since no row contains q_+. Pairing N against this basis
of M_even is perfect. The columns therefore determine γ uniquely as

    γ(b_i,0)=[basis_i],
    γ(0,e_12)=[basis_1+basis_2],
    γ(0,e_13)=[basis_1+basis_3].

L142 gives exactly F(b_i,0)=z_i, F(0,e_12)=z_1+z_2 and
F(0,e_13)=z_1+z_3. In particular [basis_4] has the required image
z_4=z_1+z_2+z_3. This independently verifies ιγ=F on all A[2];
there is no undetermined automorphism of N. For the all-ones vector
s_12+s_13+s_14, the branch image is (ε,0), not zero. The matrix
also retains it. No identification of H_E with 2O_E occurs, and no
polarization claim about F or G is needed.

**Direction, coefficient exactness and exceptions.** For 2b=a,
L127's actual composite GF=[2] gives GF(b)=a. Thus the cocycle of
F(b) is precisely F applied to the two-Kummer cocycle of b. Together
with the embedded-map check this is δ_G, not δ_F or a map obtained
by reversing a duality convention. The product pairing used above
is the Albanese–Picard pairing: functoriality for the factor
inclusions makes its cross terms trivial and its factor restrictions
the Jacobian pairings checked in Section 4 of the cited source.

The diagonal coefficient sequence is exact for the nonempty finite
étale algebra A_4. Its Kummer cohomology has kernel exactly the image
of Q*/Q*²; quotienting by that image is precisely quotienting A_4*
by Q* A_4*². Consequently j is injective and its image is the
Brauer-boundary kernel. Proposition 6.10 and the verified cycles
place all δ_G(a) there. Injectivity then proves choice independence
of the coefficient representatives and, with the usual isogeny
connecting exactness, the equivalence (2). No surjectivity onto
H¹(Q,K) or vanishing of its entire boundary has been used.

The norm evaluation at a closed point uses its whole residue algebra
after tensoring with A_4; excluded fibers are exactly where a factor
could vanish or have a pole. L142's irreducible-quartic and infinity
checks exclude all such rational E-points. Good rational B-point
differences give (3); other B divisor classes are handled by movement,
not by treating a zero evaluation as a unit.

Finally L138 gives c=−36300 and η=c/(θ−2) with nonzero denominators.
Identity (11) has the correct minus sign. On a good rational
degree-zero divisor its coefficient −c/(θ−2) contributes one;
the denominator (T−2)(D_B) is a nonzero rational scalar. To evaluate
the entire odd-model tuple, choose the divisor off T=±2 as well as
the quartic branches and the old infinities: these also remove the
odd infinity and its rational branch X=9075. Such a representative
exists by the same moving argument. The quartic projection therefore
agrees modulo rational scalars for every x, while L138's full odd
Kummer map still retains its rational component. This checks both
the scalar quotient and the exceptional-support convention.

The audit's affirmative result is limited to L143's representation
interface. Equal-T point pairs give the same coefficient twice and
remain the stopped automatic case of ATTEMPTS/062. No independently
retained class was pruned, no rank bound changed, and a rational lift
in J was not shown to belong to C's Abel image. The existing DAG
inputs are sufficient; L139–L141 are comparisons, not proof inputs.
All verification here is the displayed finite and divisor argument;
no mathematical script or numerical certificate is required.

## Mathlib

Full matching coverage of this product fake-descent comparison,
embedded reverse-isogeny map and quartic evaluation formula was not
checked. Supporting formal theorem names were not searched. Unknown
availability is not evidence of absence; no formal verification is claimed.
