# Fixed supported ideal certificate attempt

STEP_ID: beal-2026-10-16-254-fixed-eleven-ideal-attempt

RESEARCH / REPRODUCTION under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-16-separated-eleven-supported-unit.md`.
Target: Construct a supported norm-square unit in V_S whose valuation parities at the two rational eleven-adic degree-one factors are unequal.

## Saved before calculation

The main gap is primitive integer emptiness. The intermediate target is
one separating supported unit; its plausible use is an additional local
restriction beyond L077's two directions. Further pruning from fourteen
to eleven, the localized class kernel and integer lifting remain open.
Use L033/L069's exact D=K[t], L041's ordered base places, L073's full
local factors, L074/L076's support and L077's audited cubic generator.
No cross-notebook input, complete unit basis or class hypothesis is used.

Fix ONLY I=Q_8 R_8 in O_D, as prescribed at startup. The residue maps
on R=Z[k,t] are evaluation at (k,t)=(8,6),(8,3) modulo eleven.
The local inputs identify these with the degree-one and ramified
quadratic maximal primes respectively, both of norm eleven. Construct
the exact rank-36 lattice J of elements of R killed by both maps.
This is I intersect R, not an assumed maximal-order basis for I.

One bounded generator strategy: form a numerical archimedean embedding
matrix for this lattice and perform lattice basis reduction, keeping
the exact integral row transformations. Numerical roots and reduction
are search heuristics only. Cap reduction at 10,000 swaps, and test
exactly its 36 final basis rows (or stop on numerical failure); no row
sums, ideal powers, coefficient-box extension or additional ideals.
Save the full initial/final bases and transformation. Check the exact
unimodular transformation and both residue memberships, then compute
every candidate's full absolute norm by an exact multiplication
determinant. A nonzero integral candidate in I with absolute norm 121
certifies (z)=I by ideal inclusion and equal indices. A failed row
rejects only that row; failure of all rows proves neither nonprincipality
nor absence of another generator, including outside R.

For a generator, compute n=N_D/K(z), verify its supported inverse and
the correction u=z/n with exact norm n^(-2), and certify both ordered
maximal-prime parities after correction. Required: one fully certified
separating unit. If no generator is obtained, park this fixed-ideal
search and reassess after the third mathematical exploration; do not
enlarge its list. Preserve ATTEMPTS/032–035 and all prior evidence.
The positive certificate uses the already inspected Milne ANT v3.08,
Proposition 4.1(a),(c), pp.68–69, for principal ideal norms and residue
degrees. No numerical lattice property is used as a theorem and no
general unit or norm theorem is reproved. Mathlib coverage is not checked.

## Completed calculation and limitations

Run `python3 scripts/separated-eleven-unit/check_fixed_ideal.py`.
The complete certificate is
`scripts/separated-eleven-unit/fixed-ideal-certificate.json`.
It retains both defining polynomials, the initial lattice, rounded
embedding matrix, exact unimodular transformation, final lattice and
all 36 candidates with their relative and two absolute norm computations.
Its complete summary and all 77 check results were inspected.

The residue map R -> F11² is surjective: the images of 1 and t have
determinant 3 modulo eleven. Thus its kernel J has index 121 in R.
For every other monomial k^i t^j the script subtracts c0+ct*t with
the same two residues; it includes 11 and 11t as the other two basis
vectors. The displayed basis lies in the kernel and has determinant
121, so it is exactly J. The maximal-prime identifications come from
L041/L073 and L077's change of generator: at the selected base place
the t residues are 6 for Q_8 and 3 for R_8. Their residue fields are
both F11. Their kernels on R are therefore precisely these evaluation
maps, without assuming that R is maximal. Distinct maximal primes
are comaximal, so their intersection is I=Q_8 R_8; hence J=I intersect R.

The heuristic reduction terminated after 183 swaps and 357 row
reductions, below the cap of 10,000 swaps. Every final row has both
required zero residues. The exact transformation has determinant ±1,
and the initial and final lattice indices are both 121. Numerical
root approximations enter only the choice of integer row operations;
no assertion about a shortest vector, completeness, or an algebraic
identity follows from those approximations.

Each candidate's relative norm is the 3-by-3 multiplication determinant
over K in the basis 1,t,t². Its K/Q norm is then the degree-twelve
multiplication determinant. Independently, the script builds the
degree-36 multiplication matrix directly in the basis k^i t^j and
computes its determinant. Both routes use exact integer polynomial
reduction and fraction-free elimination. All 36 norm pairs agree and
are nonzero and divisible by 121. There are no arithmetic failures.

None has absolute norm 121. The minimum is 4,435,693,858,496,483.
Consequently none of these 36 integral elements generates I: if
(z)=I, the principal ideal norm formula would give |N_D/Q(z)|=121.
Conversely membership and equality of these indices would have been
sufficient for a positive ideal certificate; no candidate reached it.
Supported-inverse, relative-norm correction and ordered parity checks
were therefore NOT executed. Obtained separating units: zero; required:
one. This is EXPLORATION, not an informative global obstruction or a
new mathematical input. L077's bound remains fourteen versus eleven.

The search covers only these basis elements in the nonmaximal order
intersection. A generator might be another combination or might lie
outside R. Neither principality nor nonprincipality is established.
Do not turn the large minimum in this finite list into a field-wide
norm bound. No lemma, DAG edge or change to the assembled proof follows.

## Reassessment at the exploration limit

This is mathematical exploration 3/3 with no advance or informative
negative result across the separation attempts. Park the affine,
quotient and this fixed-ideal generator search; preserve ATTEMPTS/032–036.
No box, list, ideal-power or reduction-weight enlargement is justified
by this outcome. A future reopening needs a new discriminating idea.

The next proposed mechanism is the full two-descent image at the OTHER
dyadic completion H2=Q2(2^(1/11)), already identified in L046/L076.
This local image can be tested without assuming global generators or
principality. L070/L071 treat the rational dyadic base; L046's singleton
is for the FIVE-isogeny and does not answer this TWO-descent question.
L076 identifies the degree-33 cubic algebra but does not compute its
Kummer image. A membership test there could support further necessary
filtering, while its independence on global V_S would remain unproved.
The ramified base changes the scope of the prior rational-place source
assessment, so the proposal is REVIEW_REQUIRED, not approved mathematics.
No local image calculation or new theorem application was made here.
