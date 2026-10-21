# L076 — The supported norm-square S-unit space has dimension sixteen

## Hypotheses

Let K be L033's entire degree-twelve number field, and use L069's
fixed cubic field and distinguished generator

    g(X)=X³−4X²−160X−1264,     D=K[θ]=K[X]/(g).

Thus [D:K]=3, [D:Q]=36, and the signatures of K and D are (2,5)
and (2,17). For F=K,D let S_F consist of ALL maximal-ring finite primes
above 2 and 11, and set

    R_F=O_F[1/22],     U_{F,S}=R_F*,
    V_S=ker(N_D/K: U_{D,S}/U_{D,S}² -> U_{K,S}/U_{K,S}²).

These are exactly L074's groups, with no sign restrictions or narrow
class groups. No primitive solution, S-unit generators, class-group
value, global point computation or GRH assumption is made. The field
data from L033 do not assume the hypothetical solution in its opening
hypotheses.

## Conclusion

K has two maximal primes above 2 and three above 11. D has two above
2 and seven above 11. In particular,

    |S_K|=5,     |S_D|=9,
    dim_F2 U_{K,S}/U_{K,S}²=12,
    dim_F2 U_{D,S}/U_{D,S}²=28,
    dim_F2 V_S=16.

For L074's supported norm-square space W_S and class norm n_S,

    dim_F2 W_S=16+dim_F2 ker(n_S),
    n_S:Cl(R_D)[2] -> Cl(R_K)[2].

This is an unfiltered ambient dimension, not a rank or rank lower
bound. A containing subspace of W_S of dimension at most eleven
would have to remove at least five independent directions from V_S
alone; that condition is necessary, with no sufficiency assertion.
The class kernel, simultaneous local filtering, useful rank bound and
primitive integer lifting remain uncomputed. No Beal branch is excluded.

## Proof

### Imported theorems and the local-to-global interface

Use J.S. Milne, [*Algebraic Number Theory*, v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 5.11, printed p.90: for a number field F and a finite set S_F
of finite primes, the full S-unit group has torsion the roots of unity
and free rank r1(F)+r2(F)+|S_F|−1. Equivalently, Denis Simon,
*Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. 5 (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.2, printed
p.8, uses S including infinite places and free rank |S|−1. We use the
finite-prime convention in Milne; archimedean places enter through the
signatures. No positivity restriction is added.

Milne, Propositions 8.1–8.2, printed pp.135–136, identify the full
tensor product of a number field with Q_p as the product of its
completions at maximal primes above p. Each field factor counts once,
irrespective of its ramification or residue degree. Characteristic zero
ensures separability. We use these results for maximal-ring primes,
without interpreting repeated polynomial reductions as prime factors.

For the only remaining tensor calculation, import Romyar Sharifi,
[*Abstract Algebra*, Chapter 6, Section 6.3](https://www.math.ucla.edu/~sharifi/notes/algebra-ch06.html),
author-hosted HTML accessed 2026-10-16, no revision date identified:
Proposition 6.3.4 supplies spanning products of bases, and Corollary
6.3.6 gives compositum degree equal to the product for finite extensions
of coprime degrees. No normality assumption is needed. These statements
and their complete proofs, and Milne's statements and relevant proofs,
were inspected in the prior SPECIALIZE assessment. The general theorems
are imported; the following assembly is their exact specialization.

Because g has rational coefficients, polynomial base change gives

    D tensor_Q Q_p
      = (K tensor_Q Q_p) tensor_Q_p (Q_p[X]/(g)).

This uses the entire cubic and every base completion.

### Every dyadic factor

L046 proves the entire base algebra is Q2 × H2, where
H2=Q2(2^(1/11)) is a degree-eleven field. Its proof includes the
rational Hensel root, the irreducible degree-eleven Eisenstein quotient
and the identification with this field, so the base has exactly two
maximal primes above 2; the degrees sum to 1+11=12.

L071 identifies the ENTIRE rational cubic Q2[X]/(g) with the
degree-three field C2=Q2[s], where

    s³−4s²+6s−2=0.

The polynomial is Eisenstein at two. L071's exact invertible change
from θ to this generator identifies the whole algebra, rather than
just a subfield. The rational base completion consequently contributes
one degree-three field to D tensor Q2.

Embed C2 and H2 in an algebraic closure of Q2 and put J2=C2 H2.
Their degrees three and eleven are coprime, so Sharifi's Corollary
6.3.6 gives [J2:Q2]=33. The multiplication map

    C2 tensor_Q2 H2 -> J2,     c tensor h -> ch,

is surjective by the spanning-products statement of Proposition 6.3.4.
Its source and target each have dimension 33, so it is an isomorphism.
In particular the tensor product is a single field, with no hidden
additional factors. Merely asserting trivial intersection would not
have sufficed without this degree argument.

It follows that

    D tensor_Q Q2 = C2 × J2.

The degrees 3+33=36 exhaust D. Milne's completion theorem therefore
gives exactly TWO maximal primes of D above two. No explicit defining
polynomial for J2 or claim about a global power order is needed.

### Every eleven-adic factor

L041 proves the full base algebra is Q11 × Q11 × H11, with

    H11=Q11[r]/(r^10+55),     [H11:Q11]=10.

The degree-ten factor is proved Eisenstein, not inferred from the
repeated reduction. Thus K has exactly three primes above eleven,
with degrees 1+1+10=12. Both rational factors must be counted.

L073 proves the entire rational cubic is Q11 × M11, where
M11=Q11(sqrt(-11)) is a degree-two field. This applies separately
at EACH of the two rational base completions. At the degree-ten
completion it proves g has three distinct roots in H11 and hence

    H11[X]/(g) = H11 × H11 × H11.

In particular the latter splitting is over the actual full completion:
L073 constructs sqrt(-11)=r^5/s0 with s0 in Q11 satisfying s0²=5,
and uses the nonzero discriminant to retain all three distinct roots.
No selected-root or parity-image statement is substituted for it.

Combining all three base places gives

    D tensor_Q Q11
      = (Q11 × M11) × (Q11 × M11) × H11 × H11 × H11.

There are SEVEN field factors. Their degrees sum to
1+2+1+2+10+10+10=36. Isomorphic copies in this product correspond
to distinct primes and are counted separately. These are all maximal
primes above eleven. This retains the support required by L073's
odd valuation example; it makes no assertion that every valuation
there is even or that the example comes from a global point.

### S-unit dimensions and the square-class norm

The prime sets above the distinct rational primes are disjoint. The
complete counts therefore give |S_K|=2+3=5 and |S_D|=2+7=9.
Using L069's signatures, Milne's S-unit theorem gives free ranks

    rank U_{K,S}=2+5+5−1=11,
    rank U_{D,S}=2+17+9−1=27.

In each group the roots of unity form a finite cyclic group of even
order, since −1 has order two in characteristic zero. Its quotient
by squares has dimension one. Hence the FULL S-unit square-class
dimensions are 11+1=12 and 27+1=28. We have neither found a subgroup
of these ranks nor assumed its index is odd: the structure theorem
applies directly to the full groups.

Use L074's norm and scalar inclusion on precisely these S-unit
square-class groups. Norms of S_D-units are S_K-units and scalar
inclusion preserves S-units. Their composite on a scalar class [u]
is [u³]=[u], because [D:K]=3. Thus the norm on square classes is
surjective and rank-nullity gives

    dim V_S=28−12=16.

This uses no surjectivity on UNSQUARED S-units. L074 also proves that
S-unit square classes inject into field square classes: a field square
root of an S-unit has valuation zero outside support, hence is itself
an S-unit. Thus this is the actual norm-square S-unit subspace in W_S.
L074's exact sequence with quotient ker(n_S) now gives the stated
dimension of W_S; finiteness follows from the S-unit theorem and
finiteness of the localized class groups. It does not compute ker(n_S).

### Meaning of the baseline and verification boundary

The complete factor checks are 12 and 36 at EACH rational prime,
not merely selected local degrees. The support counts are five and
nine, rather than sums weighted by ramification or residue degree.
The resulting dimension sixteen exceeds the rank-certificate target
of eleven by five even before adding class contributions. Since V_S
is a subspace, a subspace of W_S of dimension at most eleven has
intersection with V_S of dimension at most eleven, hence codimension
at least five within V_S. This does not show such restrictions exist.

L075 places the full global Kummer image in W_S; it does not place
every S-unit class in the image. L069's zero E0(K)[2] means there is
no two-torsion correction to a future containing-space rank bound,
but neither this ambient dimension nor its lower bound is an actual
rank lower bound. L071's known removal of one ordinary-unit class
does not compute a complete filtered dimension. ATTEMPTS/032–033
remain unchanged, and no unit/class generators or global solutions
are inferred. This is REPRODUCTION of the assessed known machinery,
with no claim of progress beyond those sources.

The tensor and norm arguments and displayed integer arithmetic are
the verification for this bounded calculation; no numerical sample or
mathematical script is needed for the assembly. The separate critical
audit below confirms it without correction.

### Independent critical audit (2026-10-16)

The exact SPECIALIZE scope in
`drafts/literature/2026-10-16-supported-unit-dimension-audit.md` was
available before this audit. The cited Milne and Sharifi theorem coverage
is reused; no new general theorem is claimed. All direct mathematical
inputs remain unchanged.

The polynomial in L033 and L069 is the same degree-twelve field input.
The field assertion does not depend on a hypothetical primitive solution.
L069's irreducibility argument uses its rational Q5 place: the five
values of the reduced monic cubic are 1,3,3,2,1, so a K-root is impossible.
Consequently the tensor products here concern the entire degree-36 field.
The existing independent checker
`python3 scripts/bare-unit-rank/audit_diagnostic.py` was replayed:
33/33 checks pass, with no failures. Its full certificate is
`scripts/bare-unit-rank/audit-certificate.json`. The inspected checker
verifies all thirteen division identities and all seventeen Sturm
polynomials, including positive normalizations, degree drops and endpoint
signs. This is exact verification of complete chains, not acceptance of
a success flag or a root approximation. The base variations are 7 and 5;
the cubic variations are 2 and 1. Each real base place contributes R×C
and each complex place contributes C³, confirming (2,5) and (2,17).

The local proofs were checked at their load-bearing ranges. In L046,
m(2u)/4 reduces to 1+u, so the rational root has valuation one.
Synthetic division leaves a monic degree-eleven polynomial with even
nonleading coefficients and constant valuation one. Its Eisenstein
field has residue F2; lifting an eleventh root of the unit pi^11/2
identifies it with H2. In L071, the displayed theta/t transformations
are inverse on the degree-three algebras, and s³−4s²+6s−2 is Eisenstein.
For their tensor, both 3 and 11 divide the compositum degree by the
tower formula, and the cited spanning-products theorem bounds it above
by 33. Thus it is 33. The same spanning products make multiplication
from the tensor surjective; equality of dimensions makes it injective.
There are exactly two dyadic field factors, of degrees 3 and 33 in D,
over the two factors of degrees 1 and 11 in K. No Galois hypothesis is
used, and counting just the intersection of the fields would not suffice.

In L041 the shifted polynomial has constant −209 of valuation one.
The complementary degree-two factor has unit constant congruent to 5,
so the degree-ten Hensel factor is Eisenstein. Its uniformizer satisfies
pi^10/11 congruent to 6; the unit −55/pi^10 is therefore congruent to 1.
The tenth-root Hensel lift, with derivative 10 a unit, gives H11 exactly.
In L073, g'(alpha) is a unit and the complementary quadratic discriminant
is −11 times (16·11²/g'(alpha))². Its odd valuation makes the quadratic
irreducible over Q11. The square root of 5 exists in Q11 by the simple
root 4, and r^5/s0 has square −11. Hence all three distinct cubic roots
lie in H11. Applying this to BOTH rational base factors and the entire
degree-ten factor gives degrees 1,2,1,2,10,10,10, totaling 36. These are
seven maximal primes, with isomorphic copies counted separately and
without ramification weights. The base total is 1+1+10=12. Eleven remains in support.

Milne's full S-unit theorem now gives free ranks 11 and 27; each cyclic
roots-of-unity group has even order and adds exactly one square-class
dimension. The square-class dimensions are therefore 12 and 28. In fact
both fields have a real embedding, which also rules out any roots of
unity except ±1, though that stronger observation is unnecessary.
Norm and scalar inclusion preserve these very S-unit groups, since every
prime over the rational support is included. Their composite is cubing,
the identity modulo squares. Thus the norm is surjective on square
classes, and its kernel has dimension 28−12=16. A field square root of
an S-unit is again an S-unit by outside-support valuations; no class is
lost when this kernel is included in W_S.

Finally, L074's exact quotient uses localized class groups. For a class
in the class-norm kernel it takes a²=alpha R_D and N(a)=b R_K, forms
epsilon=N(alpha)/b² in R_K*, and replaces alpha by alpha/epsilon.
The latter has norm (b/epsilon)² and the same localized ideal square.
This checks the surjectivity needed for dim W_S=16+dim ker(n_S), rather
than assuming an abstract splitting respects norms. L075 supplies only
containment of the global Kummer image, not surjectivity onto these
sixteen unit directions. An at-most-eleven-dimensional containing
subspace must meet V_S in codimension at least five; neither existence
of that subspace nor any rank lower bound follows. S-unit generators,
the localized class kernel, simultaneous filtering and integer lifting
remain unresolved. This audit verifies a local notebook input by
REPRODUCTION, not a result beyond the assessed general machinery.

## Mathlib

Full matching explicit supported-prime decomposition and dimension:
**not checked**. Supporting S-unit, completion, coprime-degree tensor,
norm and square-class results: **not checked**. Unknown availability
is not evidence of absence.
