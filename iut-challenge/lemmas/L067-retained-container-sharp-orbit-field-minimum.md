# L067 — Sharp field minimum of the retained container orbit

## Hypotheses

Retain exactly L063's embedded field
N=Q_3(zeta_420,3^(1/7)), degree 168, ramification index 14 and
residue degree 12, full admitted presentation, single reciprocity
choice and finite-word reference subgroup Gamma including inverses.
Retain its unchanged L042/L045/L048 curve, global fields, places,
origins, coverings, cusps, stable logs and qualifications. In particular
the changed Tate parameter has v_3(q_0)=30, not an asserted equality
q_0=3^30. Native field/rho and independent initial-data conditions
remain conditional.

Put R=Z_3, O=O_N, m=m_N, J=log(O^times),
E=W_J=sum_(j=3)^168 R y_j, V=Q_3 E and C=O intersect V.
Use audited L064's actual saturated rank-166 direct summand E with
J/E free of rank two, audited L065's two-sided preservation of E
and residual irreducibility, and audited L066's complete local bounds
and same-space relative-factor comparison. All unit torsion is retained
before the genuine logarithm quotient, as in those inputs.

Normalize ord_N(3)=14 and v_3=ord_N/14 on N; set ord_N(0)=+infinity.
Let Gamma(C) mean the union of h(C) over actual finite words h in
Gamma. It is not defined as an orbit span or closure. No reciprocal
field coordinates, torsion-free presentation basis, complementary
coordinates, enlarged group, extra shear or exponent twist are assumed.

**Imported methods and why specialization is needed.** Finite generation
of a submodule of a finite module over the Noetherian ring R uses
Stacks Project, Lemma 10.31.4(2), tag 00FM
([statement and proof](https://stacks.math.columbia.edu/tag/00FM)).
Nakayama for a finite module over R and its maximal ideal (3) uses
Stacks Project, Lemma 10.20.1(2),(4), tag 00DV
([statement and proof](https://stacks.math.columbia.edu/tag/00DV)).
The bounded ordinary-span/normalized-inclusion method is the one
already used in L066 and assessed before this attempt. We apply these
known tools, rank-nullity and the nonarchimedean triangle inequality;
we do not reprove a general stable-lattice theorem. The new application
obligations are the absolute scale against this C, the lowest layer in
this actual E, and finite-word attainment. L066's qualitative escape
alone does not supply them. Its complete-unit and restriction bounds
are inputs, rather than sampled logarithms or rederived source results.

## Conclusion

For every admitted presentation in these hypotheses, the ordinary
finite R-span and the field-valuation minimum are respectively

    sum_(h in Gamma) R h(C) = E/3,
    min_(z in Gamma(C)) ord_N(z) = -33,
    min_(z in Gamma(C)) v_3(z) = -33/14.

The minimum is attained by h(c) for some actual c in C and some
finite word h in Gamma. Thus the smallest closed centered N-ball
containing Gamma(C) is m^(-33), of absolute radius 3^(33/14).
No equality of the orbit set with E/3 is asserted.

This is a REPRODUCTION/specialization of the assessed known methods,
with a relevant local quantitative input established here and no claim
of progress beyond the sources checked. The separate critical audit of
2026-10-16 passes under the unchanged hypotheses, as recorded below.
C has no asserted actual IUT input membership, and Gamma has
no asserted identification with native permitted actions. No original
IUT numerical threshold, pilot transport, essentiality, sufficient
initial data or finite B>=A conclusion is supplied. This is not a
candidate resolution of the challenge.

## Proof

**1. Determine the input's exact integral scale.** L066 proves

    3O subset J,       J intersect V=E.

For c in C, 3c lies in 3O and V, so 3C subset E. In particular
C subset E/3. Also C is not contained in E. To check the orientation
of this last assertion, L066 gives a simultaneous R-basis c_i of C
with E=direct-sum_i 3^(b_i) R c_i, where at least twenty-two b_i
equal 1. For any such i, c_i belongs to C but not E. This uses the
positive factors of E against C; a negative factor would not give
this assertion. Hence

    3C subset E,       3C not subset 3E.               (1)

Indeed 3c in 3E would imply c in E by cancellation in the rational
space V. These statements hold for every actual E under consideration,
without a choice of its complementary field coordinates.

**2. Compute the bounded ordinary span in that same space.** Define

    S = { sum_(j=1)^r a_j h_j(c_j) : r finite,
          a_j in R, h_j in Gamma, c_j in C }.

This definition uses only finite sums and finite words. Each h_j is
Q_3-linear and preserves E in both directions by L063,L065. Therefore
(1) implies h_j(C) subset E/3. Consequently S subset E/3; as an
R-submodule of the finite free module E/3, it is finitely generated
by the cited Noetherian submodule theorem. It contains C, which is
a full lattice in V by L066, so S is full as well. Gamma preserves
S in both directions, since left multiplication permutes its finite
words and both a word and its inverse belong to Gamma. This proves
boundedness and two-sided invariance without a compact closure or an
infinite sum.

Put T=3S. Then T subset E, and (1), together with C subset S,
shows T not subset 3E. The nonzero subspace

    (T+3E)/3E subset E/3E

is Gamma-invariant. L065's irreducibility gives E=T+3E. The quotient
E/T is finitely generated over R (the images of a finite E-basis
generate it), and this equality says E/T=3(E/T). The ideal (3) is the maximal
ideal of the local ring R, so the cited Nakayama lemma gives E/T=0.
Thus T=E as embedded submodules of V, and cancellation of 3 yields

    S=E/3.                                             (2)

No conclusion about equality of sets Gamma(C) and S has been used.

**3. Retain the complete lowest field layer in E.** L066 proves
J subset m^(-19) and surjectivity of the R-linear residue map

    rho:J -> D=m^(-19)/m^(-18),

where D has F_3-dimension twelve and is killed by 3. Those conclusions
include every unit and the full infinite logarithm tail, and hold
without O-linearity of J. By L064 there are z_1,z_2 in J such that

    J=E direct-sum R z_1 direct-sum R z_2.

Their existence uses precisely the actual free rank-two quotient;
their field coordinates and rho-values are not prescribed. Applying
rho and using its surjectivity gives

    D=rho(E)+F_3 rho(z_1)+F_3 rho(z_2).

Thus dim_F3(D/rho(E))<=2, so dim_F3 rho(E)>=10. In particular rho(E)
is nonzero. Every e in E has ord_N(e)>=-19, and some e_* in E has
nonzero rho(e_*), hence ord_N(e_*)=-19. Therefore

    min_(e in E) ord_N(e)=-19,
    min_(s in S) ord_N(s)=-33,                         (3)

by (2) and ord_N(3)=14. The rank comparison concerns the complete
lowest layer of the genuine J, not merely relative lattice factors,
a projected field valuation or a conveniently placed complement.

**4. Return from the span to an actual finite-word image.** The inclusion
Gamma(C) subset S=E/3 and (3) give ord_N(h(c))>=-33 for every allowed
word h and c in C. Conversely, take s_*=e_*/3. By the definition of
the ordinary span S and (2), there is a finite expression

    s_*=sum_(j=1)^r a_j h_j(c_j),
    a_j in R, h_j in Gamma, c_j in C.

Because C is an R-module and h_j is Q_3-linear, replace c_j by
a_j c_j in C to absorb every coefficient. If all the resulting
actual orbit images had ord_N>-33, discreteness of ord_N would put
each in m^(-32). Their finite sum would then be in m^(-32), in
contradiction to ord_N(s_*)=-33. At least one h_j(a_j c_j) therefore
has ord_N<=-33, and the universal lower bound forces equality.
This is an actual C-point and an actual finite word; neither a limit
nor a span element is being passed off as an orbit image. Dividing
the valuation by fourteen gives the asserted normalized minimum.
The universal bound and attained boundary give exactly the stated
smallest centered field ball and its radius.

The continuation test succeeds: the scale and lowest-layer survival
are uniform over admitted presentations, and attainment uses only
finite expressions. The independent actual-input/action, native-field,
initial-data, pilot and essentiality gaps remain unresolved. The
prescribed-coordinate and whole-kernel stops in ATTEMPTS/020,/024
are preserved, rather than assumed away by this quantitative result.

### Separate critical audit, 2026-10-16

The audit validates the stated local theorem, with no change to its
hypotheses, numerical conclusion or direct mathematical inputs. L063
supplies the actual Q_3-linear reference action and its inverses;
L064 supplies the actual saturated summand and free rank-two quotient;
L065 supplies two-sided preservation and residual irreducibility;
L066 supplies the complete logarithm bounds, residue image and relative
factor comparison. Their inspected, already audited conclusions concern
the same field, reciprocity choice, presentation and subgroup. In
particular no basis or torsion exclusion from a different field enters.

**Embedded scale and Nakayama.** In L066's convention a simultaneous
C-basis writes E as the sum of 3^(b_i) R c_i. Its inequalities give
b_i<=1 for every i and b_i=1 at least for i=145,...,166. Thus these
positive factors exhibit actual C-points outside E. Independently,
3O subset J and J intersect V=E prove 3C subset E. Cancellation
in V verifies the nonzero image of 3C in E/3E. There is no reversal
of the relative-factor convention in passing to the scale E/3.

For the ordinary span S, Q_3-linearity and h(E)=E put every summand
in E/3. The latter is a finite free R-module, so the cited Noetherian
submodule theorem applies to S without taking its closure. The identity
word puts C in S, and left multiplication by every word, including
its inverse, preserves S. Hence 3S subset E has a nonzero invariant
image modulo 3E. Residual irreducibility implies E=3S+3E. The
quotient E/(3S) is finite as an R-module because the images of an
E-basis generate it; this does not require an unproved closedness
assertion. Multiplication by the maximal ideal (3) maps that quotient
onto itself. Stacks Lemma 10.20.1(2),(4) therefore applies and gives
E=3S inside V. Division by 3 gives the actual equality S=E/3,
not merely an abstract lattice isomorphism or a homothety class.

**Complete layer and actual complement.** L066's bound applies to
every element of J, and its residue surjection comes from actual
log(1+a*pi) as a ranges over every residue direction. Its ninth
term is the unique lowest one, and the entire remaining convergent
series lies in m^(-18). Thus D has all twelve F_3 directions;
no preview or sample is being treated as complete evidence. Since
3*m^(-19)=m^(-5) subset m^(-18), D is killed by 3. The restriction
rho:J -> D is R-linear, though it is not asserted O-linear.
L064's free rank-two quotient admits an R-linear section, giving
J=E direct-sum R z_1 direct-sum R z_2 for actual elements of J.
Their two images contribute at most two F_3 dimensions. Therefore
rho(E) has dimension at least 12-2=10 and contains a nonzero class.
Any lift e_* of such a class has ord_N(e_*)=-19. This argument
uses the actual embedded E and the complete layer, rather than
deducing a field valuation from relative factors alone. Dividing
by 3 subtracts exactly 14, so the minimum on S is -33.

**Attainment and normalization.** The equality S=E/3 places e_*/3
in the ordinary finite span by definition. A finite expression has
coefficients in R, which can each be absorbed into its C-point because
C is an R-submodule of V and the actions are Q_3-linear. All resulting
terms are actual finite-word images of actual C-points. Each has
valuation at least -33. If none attained -33, each would lie in
m^(-32), as ord_N is integral; their finite sum would lie there
too, contradicting the valuation of e_*/3. Thus attainment is not
an inference from closure, an infinite sum, or equality of the orbit
set with its span. Since v_3=ord_N/14 and |x|_3=3^(-v_3(x)), the
smallest centered closed ball is exactly m^(-33), with radius
3^(33/14). A ball with a smaller real radius excludes the attained
boundary point, whether or not its radius belongs to the value group.

All checks are uniform in the admitted presentation: only its actual
saturated summand, residual action and codimension two enter. The
existing DAG correctly records the directly used local results;
the field/curve context is retained through L063. Earlier-field
examples are method precedents, not additional dependencies. This audit
adds verification of a known-method local specialization, not a new
quantitative theorem beyond L067 or a result beyond the sources checked.
No mathematical certificate or new script is needed for these module
and valuation arguments. Actual IUT input/action realization, the native
tensor embedding, pilot transport, numerical prescription, independent
initial-data conditions and essentiality remain open. ATTEMPTS/020,/024
remain intact. The original finite B>=A gap is not closed.

## Mathlib

Full matching retained-container sharp-orbit theorem: **not checked**.
Supporting coverage for finite submodules over Z_3, Nakayama,
residual invariant subspaces, residue-layer rank-nullity and finite
nonarchimedean sums: **not checked**. Unknown availability is not
evidence of absence. No formal verification is claimed. The general
module theorems are imported by precise citations; the retained-field
scale, layer and finite-word application are proved above.
