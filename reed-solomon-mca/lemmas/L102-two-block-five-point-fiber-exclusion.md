# L102 — No size-five fiber in the fixed-H two-block family

## Hypotheses

Use exactly L013's field F=F_(97^20), order-sixteen subgroup
H subset F_97^*, code RS[F,H,8], pinned same-support event at
1/4<=delta<5/16, disjoint partition H=A union B union J of sizes
(5,5,6), polynomials U,V,Q, and prescribed inputs
a_x=xQ(x), b_x=-Q(x) on A and zero elsewhere.
For r in F let J_r={x in J: U(x)/V(x)=r}.

Import L069's separately audited universal configuration conclusion
M(A')<=6 for every five-set A' subset H, with its explicit finite-census
and shared-compiler/residue-field qualifications. Its conditional
triangle bound is not assumed. A separate critical audit on 2026-10-17
found no defect in this specialization; its scope is recorded below.

## Conclusion

Every fiber J_r has size at most four. The entire original bad set has
at most eleven parameters. More precisely, its size is ten if there is
no four-point fiber with r!=1, and eleven otherwise. In particular,
the size-five/fifteen-count branch of L013 is unattainable in this
fixed-H family.

This closes only that attainment branch. It neither improves the global
11/q–16/q interval nor supplies a uniform triangle bound, a classification
of arbitrary pencils, or certified challenge-definition qualifications.

## Proof

Check L015's hypotheses on the original inputs, without changing the
chart or the event. The field, domain, code, moment convention and
four-omission cell are precisely the ones used by L013 and L015.
Both a and b are supported on A, so their moment images sigma(a)
and sigma(b) belong to U_A by its definition. The five values Q(x)
on A are nonzero because A and J are disjoint, and x!=0 on H.
In fact a and b are independent: a relation c a+d b=0 implies
Q(x)(cx-d)=0 at all five distinct x in A, hence c=d=0.
The moment map is injective on this five-coordinate space by L015's
eight-column injectivity, so the two coefficient syndromes are also
independent. No descent of an original affine chart is used.

L013 Conclusion (1) and its nonpersistence proof establish that the
actual Hankel determinant D and all sixteen actual coordinate locators
are nonzero polynomials for every such partition. Individual singular
parameters are permitted. These are exactly L015's remaining hypotheses;
no equality assumption or triangle hypothesis is needed. Thus L015
Conclusion (1), followed by the universal configuration conclusion of
L069, gives
\[
                  |B(a,b)|\le 5+M(A)\le 11.
\]
Both inputs refer to the pinned original same-support bad set. L015's
bound counts the whole set, including cancellation and singular cases;
there is no subtraction of triangle bases or replacement by closeness.
The numerical input M<=6 is reused as the audited computational theorem,
not newly verified by a selected certificate preview or a rerun here.

Suppose r!=0,1 and |J_r|=5. L013's exact count (2), valid over the
whole extension field and on that same event, would give |B(a,b)|=15.
This contradicts the bound eleven. L013 already excludes larger fibers.
For completeness, J_0 is empty since U has no zero on J. For r=1,
U-V is a nonzero polynomial of degree at most four: U,V are distinct
monic quintics with disjoint root sets. The root bound therefore gives
|J_1|<=4 as well. This proves the assertion for every r in F.
Substituting the exclusion into L013's remaining exact cases gives the
stated ten-or-eleven classification. L013 already proves that these
inputs have no further bad parameters outside the prime subfield;
the argument here has not restricted the parameter search to that field.

The only mathematical inputs beyond elementary linear algebra and the
polynomial root bound are L013, L015 and L069's universal configuration
bound. L008/L010 remain inherited inputs through those results. The
purpose of this short specialization is to settle an unrecorded
attainment question using stronger existing coverage, rather than to
reprove the census or claim progress beyond its checked scope.

### Separate critical audit (2026-10-17)

The approved audit read L102, L013, L015 and L069 in full, including
L069's October 11 complete-census audit. It checked the inherited
L008 construction and L010's moment, locator, converse and same-support
arguments against the frozen event. No defect was found. This is an
audit of the specialization, reusing the already audited configuration
theorem; it does not independently rerun or formally verify the census.

1. **Exact parameters and moment image.** The field is F_(97^20),
   the domain is the fixed order-sixteen subgroup of F_97^*, and the
   code has dimension eight. Throughout 1/4<=delta<5/16 the integer
   agreement threshold is twelve. The same shifted moments
   sigma_j(z)=sum_x z_x x^j, j=1,...,8, occur in L013 and L015.
   Both original inputs are supported on A. The values Q(x) are
   nonzero there, and five distinct labels make a and b independent.
   Injectivity of the moment map on at most eight coordinates transfers
   this independence to their syndromes. No change of words, parameter
   chart, field or support event is required.
2. **Actual polynomial nonpersistence.** L013 tests the divided
   difference K against all four actual moment rows, using UVQ=X^16-1
   and sum_(x in A) x^j/U'(x)=0 for 0<=j<=3. At any alpha in A,
   L008's representative has exactly four nonzero weights, so L010's
   Vandermonde product gives D(alpha)!=0. The moment-row kernel over
   F(T) is consequently one-dimensional. The coefficients of K have
   no common root over an algebraic closure: such a root t would give
   U(t)V=V(t)U, and independence of U,V would force a common root.
   Their coefficient gcd is therefore one. This makes the multiplier
   L/K polynomial; K has T-degree four and L at most four, so that
   multiplier is a nonzero constant. Thus this is the actual determinant
   locator, not a projected candidate. For each x in H, an identically
   zero K(T,x) would force U(x)=V(x)=0, impossible for the disjoint
   blocks. Also U-V is a nonzero polynomial. These arguments verify
   every nonpersistence hypothesis without assuming high count, simple
   parameter roots or nonsingularity at every parameter.
3. **The entire original event.** L010 identifies sparse decodability
   with badness on the complement of the actual error support. If b
   were a code restriction on that complement, the whole pencil would
   have representatives on that fixed support, forcing D or a locator
   identically zero. Hence input failure is on precisely the same
   admissible support as agreement. Conversely any bad event on any
   support of size at least twelve supplies a representative of weight
   at most four. L015 therefore covers the full event. Its at-most-five
   cancellation parameters include all possible lower-weight errors;
   outside cancellations, distance nine forces weight four disjoint
   from A. In particular a singular value is not silently removed:
   outside cancellations any decodable value has nonzero D by the
   weight-four factorization, and cancellation values were counted
   separately. For this prescribed family L013 additionally excludes
   lower-weight errors outright, but the upper-bound application does
   not need to discard them.
4. **Universal census scope and extension fields.** L015's distinct
   rational configuration points are nonzero in every coordinate. The
   projective parameter map is injective, and an extension-field line
   containing two such points is their rational line after scalar
   extension; a line containing at most one is harmless. Thus no
   rationality of an arbitrary original chart is assumed. L069's
   complete-census section and its separate audit establish M(A')<=6
   for every five-set A', before its conditional triangle count is
   applied. They cover all 273 multiplicative orbits and all 4,368
   five-sets. Only this universal theorem is imported here. The
   resulting |B(a,b)|<=5+6=11 counts all original finite parameters,
   with no triangle hypotheses or subtraction of three base events.
   The existing finite-computation and shared-compiler/residue-field
   qualifications remain essential; no fresh certificate preview is
   used to establish the bound.
5. **Fiber contradiction and exceptional cases.** A nonempty fiber
   has r!=0 since U,V have no roots on J. For r!=1, a size-five fiber
   makes (U-rV)/(1-r) the product of its five distinct linear factors.
   At each of those five labels, dividing out that label leaves four
   distinct locator roots and nonzero D. L010's converse therefore
   supplies five bad parameters in J, distinct from the ten in A union
   B furnished by L008. L013 proves there are exactly fifteen, already
   contradicting eleven. At r=1 the nonzero polynomial U-V has degree
   at most four, so that fiber has size at most four. Fibers of size
   greater than five are excluded by the degree bound, and two fibers
   of size at least four cannot fit in J of size six. If the surviving
   r!=1 fiber has size four, L013 retains the possibility that its
   residual fifth root repeats a fiber label: division still leaves
   four distinct roots, so it contributes exactly one parameter.
   Otherwise no extra parameter occurs. Ratios of labels and the lone
   residual linear root are in F_97, explaining the full-extension
   exhaustion without replacing the event by a prime-field search.

The audit confirms the ten-or-eleven classification and the exclusion
of every size-five fiber. It introduces no new mathematical input or
DAG edge. The global interval, arbitrary pencils, uniform triangle
twelve and the challenge-definition qualifications are unchanged.

## Mathlib

Full matching fiber exclusion and computational configuration bound:
**not checked**. Supporting polynomial root bounds and moment-map
injectivity coverage: **not checked** here. Unknown availability is not
absence, and no Lean verification is claimed. The pinned definition's
ArkLib coverage is recorded in L015 and is separate from Mathlib and
the unread July ABF26 definition.

Classification: REPRODUCTION, a hypothesis-checking application of
existing local results with explicit computational dependence.
