# Complex scaled finite Rice closing: source review1680

19 November2026. Literature-only review of nomination1679's unchanged
TARGET. No weighted residue identity, edge asymptotic, lower bound,
new lemma or mathematical script is established here. The source
comparison is complete; the mathematical test remains unperformed.

## Primary inputs and exact scope

P. Flajolet and R. Sedgewick, *Mellin transforms and asymptotics:
Finite differences and Rice's integrals*, TCS144(1995),101--124,
DOI10.1016/0304-3975(94)00281-M,
[Section2 Lemma1/(6), pp104--105](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf):
for phi analytic in a domain containing [n0,infinity), the positive
closed contour lies in that domain, encloses [n0,n], and excludes
the earlier nonnegative integers. Its finite formula is

    sum_(k=n0)^n (-1)^k binom(n,k) phi(k)
      = (-1)^n/(2pi i) integral_C phi(s) n!/product_(k=0)^n(s-k) ds.

The residue proof was read. Formula(7) additionally requires polynomial
growth throughout Re(s)>=c<n0 and n>r+1. Section4 Theorem2, pp110--111,
requires meromorphy and polynomial growth on escaping circles, or
outside a compact set in the specified half-plane. Both proof cases
close contours and retain noninteger residues. Example4, pp112--113,
warns that growth can prevent arbitrary rightward extension and uses
a separate argument. None states the present moving weighted bound.
The readable formula/residues were corroborated in the authors'
[27March1994 prepublication, Section2, p4](https://static.aminer.org/pdf/PDF/001/091/229/mellin_transforms_and_asymptotics_finite_differences_and_rice_s_integrals.pdf).
This is a different version and pagination. Final-PDF screenshots
returned no inspectable image; text plus this corroboration sufficed.

NIST DLMF, accessed19November2026,
[4.2.3, 4.2.19 and following analyticity statement, 4.2.27--29](https://dlmf.nist.gov/4.2):
principal Log(z)=log|z|+i ph(z), -pi<ph(z)<pi, off the nonpositive
real cut; exp is entire and nonzero. Principal powers are
z^a=exp(a Log(z)) for z!=0; at integer exponents they agree with
ordinary powers, and their modulus is

    |z^a|=|z|^(Re a) exp(-(Im a) ph(z)).

These are imported definitions/identities, not a new weighted theorem.
For the proposed phi, the base is the fixed nonzero number -i/d at
each degree, and the contour variable is its exponent. The next
attempt must retain this distinction and the principal branch;
it must not replace the modulus by |z|^(Re a) for nonreal a.
No numerical branch substitution or edge cost is derived here.

Reuse notes1660/1676 and approval1677's full-argument gamma tools.
Refreshed [DLMF5.11.1, 5.11(ii) first remainder paragraph, and 5.11(iii)](https://dlmf.nist.gov/5.11):
Stirling holds in fixed sectors |ph(z)|<=pi-delta; after truncation
at k=n-1, its log-gamma remainder is bounded by the first omitted
term times sec^(2n)(ph(z)/2). The ratio subsection fixes a,b,c;
5.11.9 is uniform only for bounded real parts. These do not authorize
fixed-shift formulas with shifts growing like the degree or height.
No gamma theorem is reproved. Earlier recorded version1.2.8 and this
live page are distinguished; no relevant formula change was observed.

## Applicability comparison, with specialization still unpaid

C048k Sections1--2 already supply actual E, entire continuation,
E(k)=gamma_k/gamma_0, the finite kernel B_d, and its residue signs.
C048l specifies the finite rectangle and F_d^I=E B_d, with Z=gamma_0.
The finite theorem's analytic scope allows examining the proposed
coefficient interpolation phi_d(s)=E(s)exp(s Log(-i/d)) separately
for each integer degree. Its scope imposes no polynomial growth at
infinity for this finite operation. This is source applicability,
not a proved identity for the weighted contour.

The next attempt must write its integer samples, residue signs,
positive orientation and normalization for U_d(i)=J_d(i/d)/gamma_0.
It may cite the finite template and the existing E normalization;
reproving either would be unnecessary. All four sides must remain
until the requested three-side absolute budget is settled. A finite
formula at each d supplies no uniform-in-d estimate by itself.

The actual-I transfer is available as the existing C048j conclusion,
with r>=exp(12), Re(p)>=-r/(4log r), and relative error
<(17/10)(log r)^(9/2)/r. C048l Section1 checks this domain and a
common vanishing error on all three unweighted closing sides.
Multiplication is not permission to discard that relative error or
to differentiate it. A contrary lower bound must retain actual I,
including a uniform lower comparison, on a nonzero-length edge subarc.

C048l(18)--(21) provide an exact corner expression and its unweighted
scale; (12)--(16) treat horizontal variation through an explicit
main term, and (22)--(25) include the whole right edge. These are
existing inputs to consult in the mathematical test, not a weighted
conclusion. C048l's use of conjugation for its two horizontal edges
does not establish equal costs after inserting a fixed nonreal base.
The literature's modulus identity must be applied on each side.
C048o/p concern unweighted vertical segments, so their endpoint
expansions do not duplicate or prove this closing target.

## Discovery, duplicates and retained stops

Queries actually issued were `"Norlund Rice" "complex" "parameter"`,
`"Rice integrals" "z^s"`, `"Jensen polynomials" "Rice" complex argument`,
`"Rice integrals" "exponential" growth contour`,
`"Nörlund" "Rice" "complex parameter"`,
`"Rice integrals" "binomial" "weighted"`, and
`"Jensen polynomials" "Mellin" "contour"`.
They produced the standard Rice paper/book and irrelevant or different
families; no exact moving-rectangle actual-E bound was identified.
Search snippets and secondary pages are discovery only. No absence
or originality claim follows. The known saddle/reciprocal-gamma and
zeta-difference comparisons in notes1676 remain adequate and are
reused, without repeating their source extraction. Book variants,
Norlund's book and the newly returned shifted-Jensen wedge webpage
were not inspected or imported and are not essential to this test.

Notebook searches covered the C028/C048 files, Rice-named assessments
and attempts, and the specifically recorded theta-boundary stop.
Read C028b/g's precise normalization and gap; C048a/j/k/l's relevant
domains and proof passages; notes1656/1676; stops1657/1665/1667; and
the older signed-bump gamma-Rice stop. The old signed-bump family is
not the actual interpolation E. The fixed-degree infinite opening,
in-sector stationary-point and theta-boundary-crossing stops remain
valid for their stated operations; none settles this finite weighted
rectangle. No stopped operation is reopened. No cross-notebook input
or shared runtime state was read or changed.

## Decision and bounded continuation

SPECIALIZE. Source coverage is sufficient for one REPRODUCTION attempt
on the unchanged TARGET, after the supervisor's separate next-turn
approval. General finite Rice and complex-power identities are known;
only actual normalization and degree-uniform weighted edge comparison
remain to be performed. The present review neither proves A_d(i)=o(1)
nor disproves it, and creates no canonical mathematical claim.

Success requires absolute o(1) over all three sides. A negative result
requires a rigorous lower bound for the actual multiplied integrand
integrated over an actual edge subarc, sufficient to rule out o(1).
A large corner value or a nonvanishing upper estimate is inconclusive.
If a lower-bound approach is chosen, it must specify a subarc and
control its entire length, not silently replace it with a point.

C028b/g's H_d=o(d), S_F=0, a sufficient compact nonreal-zero mass
bridge, other arguments and Xi positivity remain unpaid. Even a pass
at w=i is only a prerequisite for a separately reviewed neighborhood.
Full matching Mathlib coverage is unchecked; supporting calculus
coverage is not asserted to formalize the weighted estimate. No
justified creative central mechanism was found in this source review;
the missing sufficient compact-mass bridge remains its blocker.
