# Higher fibre-degree restriction test

The exact saved target is the all-positive-degree ideal-cohomology
question for the original ample L with L.F>=3. Its prior SPECIALIZE
assessment is `literature/2026-09-27-higher-fibre-degree-ideal-cohomology.md`.
The assessment is reused unchanged; no source-access gap is pending.

The intermediate gap is the actual image of the two projection spaces
in H^0(C,H^r|_C). A nonzero cokernel would leave open a failure of
L018's sufficient summand recovery in the ordering 0<m<n. Vanishing
would close that cohomological escape only in the numerical range and
degrees proved. An actual inclusion obstruction, cancellation of the
transverse RM obstruction, higher-order lifting and algebraization
would remain separate problems. The attained span is still 21 on the
same family, with three permitted directions against four required.

## Entry checkpoint

Read the shared and local rules, complete overview, DAG, prior review,
L008, L019, L020 and the relevant failed complete-intersection attempt.
Existing changes and unfinished drafts are preserved. L020 settles
fibre degree two; no existing result computes the remaining range.
Ordinary normal generation does not identify the two projection spaces.

The ideal sequence identifies the group with a restriction cokernel.
L019 supplies vanishing on the normalization and all three independent
descent conditions. Its divisor basis, saturated by L020's determinant
argument, provides a possible way to retain the original L as a
numerical parameter. Pullbacks of its four generators must be checked
on the resolved fibres before identifying the pullback bundles.

The test will use the actual global sections, or a rigorously sufficient
subspace, and keep the type-III fibre and its length-two tangency. An
unjustified enlargement to complete fibre sections cannot certify the
global map. A partial result must specify the complementary numerical
range. No new cohomology value has been established at this checkpoint.

## Fibre degree three: proposed complete subcase

Translations by multiples of P and inversion commute with the rotation
on W and preserve C simultaneously on S x S. Saturation of the divisor
basis lets one reduce the generic-fibre group sum modulo three to zero
or P. Positivity on the two components then leaves precisely

- L=3O+bF-E, with b>=7 and L^2=6b-20;
- L=2O+P+bF, with b>=5 and L^2=6b-10.

These are transported original polarizations. They are not substitutes
for an unspecified L with fibre degree at least four.

For the first form a proposed complete basis of H^0(S,rL) is x^i times
polynomials of degree A_i=rb-4i-max(0,r-i), and y x^j times polynomials
of degree B_j=rb-6-4j-max(0,r-1-j), for i<=floor(3r/2) and
j<=floor((3r-3)/2). These bounds use pole orders (4,3) for x and
(6,5) for y on (R,E), including the negative E coefficient. The
section count agrees with K3 Riemann--Roch. On W use the same basis
with r replaced by 2r and Laurent coefficients of the corresponding
symmetric bounds; the trace splitting gives the same total dimension.

The x*x products fill every coefficient block except three endpoint
or change-of-slope blocks, using L020's coefficient hyperplanes. For
odd r the two highest x blocks instead use y*y and the Weierstrass
equation; the resulting lower terms must be retained in a triangular
rank argument. Mixed x*y products fill all the odd blocks. The proposed
total codimension on W is three for every r, including r=1.

For the second form use z=(y+y_0)/(x-x_0). A proposed complete basis
is x^i (0<=i<=r), x^i z (0<=i<=r-1), and z^j (2<=j<=r), with
coefficient degrees rb-4i, rb-4i-2, rb-2j. The products of x powers,
mixed x powers with x^j z, and z powers again have codimension three.
All coefficient degrees are positive. Comparing with L019's exact
three-condition descent dimension would establish restriction
surjectivity, rather than discarding the conditions at infinity.

The remaining proof checks are uniform allocation counts, resolved
divisor bounds, original-class reduction and the independence argument
for the coupled y*y products. The wider numerical range is not settled.

## Completion and bounded scope

[L021](../lemmas/L021-fibre-degree-three-positive-ideal-vanishing.md)
completes the fibre-degree-three proof in every positive r. It retains
the negative E coefficient in form A, proves both global section
bases complete by dimension counts, and treats odd r's coupled y*y
products by their triangular leading terms. The independent products
have exactly the three-condition descent dimension in both forms.
The original polarization is transported by an automorphism preserving
C throughout. No assertion for L.F>=4 is made.

A preliminary attempt to extend the same elementary monomial basis
to arbitrary larger fibre degree was incomplete. For example, for
3O+3P+bF+E the list 1,x,z,xz,z^2,z^3 with the separate monomial
pole bounds has total section count 6b-16 for large b, whereas
Riemann--Roch for an ample class gives 6b-14. The two-section deficit
is a defect of that proposed basis, not a nonzero restriction cokernel.
It prevents extrapolating the complete bases in L021 to all larger
degrees without new work. No larger-degree cohomology value was derived.

The source tools are imported; the actual two-projection calculation
was not matched by the saved assessment. This is a partial local
mathematical input, without certified originality or a transverse lift.
It reaches the all-positive-degree threshold in fibre degree three;
the broader saved target remains incomplete.

Before extending the numerical classification, the role of the
cohomological exception merits a separate source comparison. L018
recovers a lift of a direct sum before trying to lift its inclusion.
The general Atiyah-obstruction theorem cited in L012 is a lead for
testing whether existence of lifts of the summands follows without
that inclusion. This is only a newly registered question: no such
theorem or revised union obstruction is derived in this turn. It
could make further ideal-cohomology calculations unnecessary for
this route. L020's nonzero group remains a valid existing result.
