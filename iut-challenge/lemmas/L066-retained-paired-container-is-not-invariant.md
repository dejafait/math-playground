# L066 — The retained paired valuation container is not invariant

## Hypotheses

Retain L063's embedded field N=Q_3(zeta_420,3^(1/7)), of degree
168, ramification index 14 and residue degree 12, its full admitted
presentation, single reciprocity choice and finite-word reference
subgroup Gamma, including inverses. Retain the unchanged field/curve
context and qualifications of L042,L045,L048 through L063. Put

    R=Z_3, O=O_N, m=m_N, U_l=1+m^l (l>=1),
    J=log(O^times), E=W_J, V=Q_3 E, C=O intersect V.

Use L064's actual saturated free rank-166 summand E of J, with
J/E free of rank two, and L065's two-sided Gamma action on E and
irreducibility on E/3E. No reciprocal field coordinates, complementary
coordinates, extra shear or unit-exponent twist are assigned. All unit
torsion remains in the full pair and is removed only by logarithm.

**Imported methods.** Use Hess–Pauli–Pohst, *Computing the Multiplicative
Group of Residue Class Rings*, 18-page author manuscript, section 4,
Lemma 4.1, pp.7–9, and Proposition 5.1(i),(iii–iv), pp.9–10
([primary manuscript](https://page.math.tu-berlin.de/~kant/publications/papers/hepapo.pdf)).
Successive principal-unit layers have their additive residue quotients;
log and exp are inverse on m^l and U_l when l>e/(p-1). Apply these
completion statements with p=3,e=14,l=8. No easy-case unit basis or
shallow log/exp isomorphism is imported. Additivity and the exact
torsion kernel of log, and J=log(U_1), are already checked in L063,L064.

Use Bürgisser–Kulkarni–Lerario, *Nonarchimedean integral geometry*,
Selecta Mathematica 32:10 (2026), version of record 5 January 2026,
Definition 3.1.1 and Lemmas 3.1.4–3.1.5, pp.21–23, and
Propositions 4.1.1–4.1.2, pp.35–36
([primary publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)). These supply simultaneous
lattice factors, full subspace intersections and restriction interlacing
over the local scalar field Q_3 with DVR R. Neither nesting nor
O-linearity of J is assumed.

The stable-lattice method is Sehanobish, *Universal Deformations and
p-adic L-functions*, Maryland PhD dissertation (2019), section 3.1,
Corollary 3.1.9, pp.26–28
([primary dissertation](https://api.drum.lib.umd.edu/server/api/core/bitstreams/9c358dab-b72f-47fa-924c-da55d0ae1ea6/content)).
Its compact/profinite representation formulation is not applied directly
to a group closure. As in audited L035, reproduce the normalized-inclusion
argument for the finite-word subgroup using Nakayama's lemma,
Stacks Project, Lemma 10.20.1(2),(4), tag 00DV
([statement and proof](https://stacks.math.columbia.edu/tag/00DV)). This
checks embedded scalar equality, which the dissertation's last abstract-
isomorphism sentence alone would not justify. The general tools above
were assessed before this attempt; only their retained-field application
and the necessary explicit bounds are proved here.

## Conclusion

For every admitted presentation in the hypotheses, C is not invariant
under Gamma. Some finite word h in Gamma and some actual c in C satisfy

    h(c) not in C, equivalently h(c) not in O.

More precisely J intersect V=E, and the relative exponents of E against
C include at least ten negative and at least twenty-two positive values.
Consequently C and E are not scalar homothetic in the same space V.
This conclusion is uniform over all rational codimension-two subspaces
for the lattice comparison; the action assertion uses the actual V.

This is a REPRODUCTION/specialization of known methods, with a new local
application recorded here and no claim of progress beyond the literature
checked. Its separate critical audit of 2026-10-16 passes, as recorded
below. It supplies neither an
explicit escaping word nor a sharp orbit radius, membership in any actual
IUT input, identification with native permitted actions, sufficient initial
data, marked pilot transport, essentiality or original finite B>=A failure.
It is not a candidate resolution of the IUT challenge.

## Proof

**1. Complete-unit covolume bound.** Normalize ord_N(3)=14 and choose
any uniformizer pi; thus ord_N(pi)=1 and m^l=pi^l O. Since 8>14/2,
the cited deep log/exp theorem gives log(U_8)=m^8. In particular

    m^8 subset J,              3O=m^14 subset J.          (1)

Each map 1+x -> x modulo m^(l+1) identifies U_l/U_(l+1) with
m^l/m^(l+1), for l>=1: the product error xy lies in m^(2l),
which is contained in m^(l+1). Each layer has order 3^12. Thus

    |U_1/U_8|=3^84,            |O/m^8|=3^96.

Logarithm induces a surjection U_1/U_8 -> J/m^8, by J=log(U_1)
and log(U_8)=m^8. Write |J/m^8|=3^t; then t<=84. This bound
accounts for every shallow unit layer and the entire deep ideal.
It allows the kernel caused by unit torsion; it does not assume that
the displayed surjection is injective or that torsion is absent.

For the simultaneous lattice factors choose an R-basis v_1,...,v_168
of O with

    J=direct-sum_i 3^(a_i) R v_i,  a_1<=...<=a_168.

All a_i are integers. Normalize additive Haar measure by vol(O)=1.
Then vol(m^8)=3^(-96), vol(J)=3^(t-96), and also
vol(J)=3^(-sum_i a_i). Consequently

    d=sum_i a_i=96-t>=12,      a_i<=1 for every i.       (2)

The second assertion follows from 3O subset J in (1), in this
simultaneous basis. Volumes are used only for these full local lattices;
they are not the original IUT quantities A,B.

**2. A full nonintegral residue layer, including infinite tails.** For
n>=1 write r=v_3(n), so n>=3^r. Every x in m satisfies

    ord_N(x^n/n)>=n-14v_3(n)>=3^r-14r.

For r=0,1,2,3 the last expression is respectively 1,-11,-19,-15.
For r>=2 its increment on replacing r by r+1 is 2*3^r-14>0.
Thus the unique minimum over all n is -19, attained only at n=9
and, for equality in the first inequality, ord_N(x)=1. The quantities
n-14v_3(n) tend to infinity, since v_3(n)<=log_3(n). The full series

    log(1+x)=sum_(n>=1) (-1)^(n+1) x^n/n

therefore converges in N. All its terms belong to the closed fractional
ideal m^(-19), so J=log(U_1) is contained in that ideal. For x=a pi
with a in O, every term except n=9 lies in m^(-18), and the infinite
sum of those terms also lies there. Hence

    pi^19 log(1+a pi) = (pi^28/9) a^9 modulo m.         (3)

The coefficient pi^28/9 is a unit. The residue field k=O/m is
F_(3^12), on which a -> a^9 is the square of Frobenius and is
bijective. Letting a range over lifts of all k, (3) proves that J
maps onto the whole additive residue layer

    m^(-19)/m^(-18), of F_3-dimension 12.               (4)

This is a surjection of R-modules, where the target is killed by 3.
Both J intersect O and 3J map to zero: O subset m^(-18), while
3J subset m^(-5) subset m^(-18). It follows that

    dim_F3 J / ((J intersect O)+3J) >= 12.              (5)

In the simultaneous basis above this dimension is exactly the number
n_- of negative a_i. Indeed J intersect O has i-th coefficient ideal
3^max(a_i,0) R, and 3J has 3^(a_i+1) R. The quotient in (5) has
one F_3 direction when a_i<0 and zero otherwise. Therefore n_->=12.
Let n_+ count the positive a_i. By (2) all positive factors equal 1,
and every negative a_i contributes at most -1. Thus

    12<=d=sum_i a_i<=n_+-n_-,
    n_+>=12+n_->=24.                                  (6)

The bounds cover the complete J, rather than a sampled logarithm span.
No unit relator coefficient, exact primary-torsion order, O-module
structure on J or explicit integral matrix was needed.

**3. Restrict in the same space.** Let V' be any rational codimension-two
subspace of N. The cited intersection-lattice theorem gives full
rank-166 lattices E'=J intersect V' and C'=O intersect V'. Give N
the domain lattice norm of J and target lattice norm of O. The identity
has singular values 3^(-a_i) in decreasing order. Restrict its domain
to V'; its target induced norm is exactly the norm of C' on V'.
Thus its 166 nonzero factors are those of E' against C'. If their
exponents are b_1<=...<=b_166, restriction interlacing gives

    a_i <= b_i <= a_(i+2),        1<=i<=166.           (7)

The twelve negative ambient exponents imply b_i<0 for 1<=i<=10.
The twenty-four positive ambient exponents imply a_i=1 for
145<=i<=168, so b_i>=1 for 145<=i<=166, twenty-two indices.
In particular the b_i cannot all equal one scalar valuation. Thus
E' and C' are not homothetic by any element of Q_3^times. This
uses necessary restriction inequalities in their negative direction;
no passing necessary test is treated as sufficient for stability.

Now take the actual V=Q_3 E. L064 gives rank 166 and a free quotient
J/E, so J intersect V=E: if j lies in that intersection, clearing its
finitely many rational E-coordinates gives 3^n j in E for some n>=0.
The class of j in the torsion-free quotient J/E is therefore zero.
This proves equality with the full intersection, not just fullness or
finite index. Applying (7) proves the asserted factors for E against C.

Both are full closed lattices in V. For C, closedness follows because
O is compact and V is a closed finite-dimensional subspace; fullness
follows by scaling any V-basis far enough into O. The intersection
theorem gives its finite free lattice structure. For E the basis in
L064 identifies it with the compact module R^166, and its rational
span is V. L063,L065 imply that Gamma preserves V and E in both
directions. All comparisons occur inside this very V.

**4. Putative stability forces the excluded homothety.** Suppose every
h in Gamma preserves C. Because Gamma includes inverses, preservation
as containment also implies equality. Commensurability of the full
lattices C,E gives a least integer q such that C_0=3^q C is contained
in E; it is not contained in 3E, by minimality. This can be seen by
clearing the finitely many entries of the invertible rational basis
matrix of C in an E-basis. The least q exists among all integers,
whether positive or negative.

Rational scaling commutes with Gamma. Thus the nonzero subspace
(C_0+3E)/3E of E/3E is invariant. L065's actual residual
irreducibility gives E=C_0+3E. The module E/C_0 is finitely generated
over the local ring R and satisfies E/C_0=3(E/C_0). Since (3) is
its maximal ideal, the cited Nakayama lemma gives E/C_0=0. Hence

    C=3^(-q) E

as embedded lattices in V, contradicting Step 3. No compact closure,
abstract-module identification or larger-group theorem is required.

There is therefore some g in Gamma with g(C) unequal to C. If
g(C) is not contained in C, choose c in C with g(c) outside C.
Otherwise g(C) is a proper subset of C; choose c in C outside g(C),
so g^(-1)(c) is outside C. Both words belong to the same finite-word
subgroup. In either case h(c) stays in V, and being outside C is
equivalent to being outside O. This establishes exactly the stated
container escape. It assigns no field coordinates to c and supplies
no membership in an actual IUT input or prescribed numerical region.

The continuation test succeeds for this qualitative target. Prescribed-
coordinate and whole-kernel routes in ATTEMPTS/020,/024 remain stopped.
Independent native field/rho and initial-data assumptions, actual input
and permitted-action realization, marked pilot transport, essentiality
and original finite B>=A remain unresolved.

### Separate critical audit, 2026-10-16

The audit passes under the stated hypotheses. No conclusion is withdrawn
or strengthened. The existing sources cover the general methods; this
check verifies their application to the complete J and the actual V.
L063's already audited logarithm/action comparison, L064's already
audited saturated span and L065's already audited residual action are
retained inputs. L035 supplies a method precedent only, not a theorem
about this field. The following checks make the load-bearing conventions
and completeness explicit.

**Units and covolume.** The deep theorem's strict inequality is
8>14/(3-1)=7. Consequently its inverse exponential supplies every
element of m^8 as a logarithm, and not merely an inclusion of sampled
logs. The seven layers l=1,...,7 each have cardinality 3^12; the eight
additive layers l=0,...,7 give |O/m^8|=3^96. The logarithm map on
U_1/U_8 is well-defined by additivity and log(U_8)=m^8, and is
surjective because J=log(U_1). These assertions do not identify its
kernel with zero. Thus 0<=t<=84, and the entire J is a union of
3^t additive cosets of m^8. With vol(O)=1 this proves
vol(J)=3^(t-96). In the simultaneous basis, each factor 3^(a_i)
multiplies additive Haar measure by 3^(-a_i), verifying the sign
sum a_i=96-t. Finally m^14=3O lies in m^8, so 3O subset J;
coordinatewise this is 3R subset 3^(a_i)R and hence a_i<=1.
Neither an index [O:J] for nonnested lattices nor multiplicative Haar
measure has been substituted.

**Every logarithm term and every residue direction.** For fixed
r=v_3(n), the smallest possible n is 3^r. The lower bounds
3^r-14r for r=0,1,2,3 are 1,-11,-19,-15, and are strictly
increasing thereafter, since 2*3^r-14>0 for r>=2. At r=2,
any n other than 9 is strictly larger than 9 and hence has a strictly
larger integral bound. This proves uniqueness of n=9 over all positive
integers, not just powers of three. The estimate n-14 log_3(n)
tends to infinity. Thus the whole logarithm converges; every term
other than the ninth lies in m^(-18), and completeness and closedness
put their infinite sum in that same ideal. The ninth term has positive
sign and pi^19*(a*pi)^9/9=(pi^28/9)*a^9. Since
ord_N(9)=28, its coefficient is a unit. Frobenius squared is a
bijection on the entire field F_(3^12), so the images of actual
logs cover the full twelve-dimensional F_3 residue space. Additivity
of log makes this the image of an R-linear map on J. Multiplication
by 3 raises ord_N by 14, so 3J subset m^(-5) is killed by that
residue map; J intersect O is killed as well. The map therefore
factors through exactly the quotient used in (5).

For one simultaneous coordinate its denominator is
3^max(a_i,0)R+3^(a_i+1)R. If a_i<0 this is 3^(a_i+1)R,
giving one F_3 dimension in the numerator 3^(a_i)R; if a_i>=0
it equals the numerator. This independently checks that (5) counts
negative factors, rather than their total lengths. There are at least
twelve. All positive factors are exactly 1, so
12<=sum a_i<=n_+-n_- forces n_+>=24. Cancellation in a shallow
log or the presence of primary torsion cannot invalidate either bound:
the residue image is attained and the covolume estimate used a
surjection only.

**Restriction and the actual intersection.** The scalar DVR for the
singular-value theorem is Z_3, not O_N. In the domain norm with
unit ball J, the basis 3^(a_i)v_i is orthonormal; in the target
norm with unit ball O its i-th image has norm 3^(-a_i). Thus the
decreasing singular-value list is exactly the displayed one. Restricting
the domain to V' gives unit ball J intersect V', and the induced
norm of the image in the target has unit ball O intersect V'. The
map is injective of rank 166. The cited restriction inequality applies
to its 166 nonzero singular values, even though the original target
has dimension 168. It reads
3^(-a_i)>=3^(-b_i)>=3^(-a_(i+2)), giving (7) with the stated
orientation. In particular b_10<=a_12<0, while
b_145>=a_145=1; monotonicity gives ten negative and twenty-two
positive factors. A scalar multiplier u*3^s with u in Z_3^times
would make all relative exponents equal to s (or all to -s under
the reverse comparison), which is impossible.

For the application, L064's J/E is free of rank two. Clearing
denominators of an element of J intersect Q_3 E gives a class in
J/E killed by a power of 3; torsion-freeness kills that class.
Hence the domain intersection really is E. This step is necessary:
having rank 166 alone would not justify use of L065's reduction.
The target intersection is precisely C in the same V, not a projected
container or a quotient carrying an assumed field valuation. Both
lattices are finite free and full, and L063/L065 preserve this V and
E for every finite word and inverse.

**Embedded stability and an actual word.** In an E-basis write a
C-basis as the columns of an invertible matrix T over Q_3. The
minimum valuation m_0 among its nonzero entries is finite and integral.
Then q=-m_0 is exactly the least integer making 3^q C subset E;
at least one scaled entry is a unit, so this lattice is not in 3E.
Under putative Gamma-invariance its nonzero image in E/3E is
invariant under exactly L065's subgroup. Irreducibility gives
E=3^q C+3E. The images of an E-basis generate E/(3^q C),
so this module is finitely generated. The ideal (3) is in the
Jacobson radical of Z_3. Nakayama therefore yields the embedded
equality E=3^q C, contradicting the mixed signs above. No assumption
that q is nonnegative, compact closure of Gamma or abstract lattice
isomorphism enters. If the resulting unequal image g(C) is contained
in C, a point of C outside g(C) escapes under g^(-1); otherwise
a point escapes under g. The inverse is an allowed finite word,
and its image remains in V. This proves the stated existential
field-container escape with all quantifiers retained.

This is verification of a local specialization of known methods, not
a result claimed beyond the sources checked. The input c is only
known to lie in C. No explicit word, sharp orbit minimum, actual
IUT input/action identification, pilot transport or original finite
B>=A statement is established by this audit. The prescribed-coordinate
and whole-kernel stops remain intact.

## Mathlib

Full matching retained-field container-noninvariance coverage: **not
checked**. Supporting coverage for unit filtrations, p-adic log/exp,
relative lattice factors, restriction interlacing and Nakayama: **not
checked**. This records unknown coverage, not absence. The general
theorems are imported by the precise citations above; the full local
specialization, infinite-series control and action application are here.
