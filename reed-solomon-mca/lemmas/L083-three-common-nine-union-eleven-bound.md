# L083 — Eleven bad parameters for the three-common-coordinate row

## Hypotheses

Let F=F_(97^20), H be the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Use L010's shifted moments sigma_j(z)=sum_(x in H)z_x x^j,
1<=j<=8, and the pinned event at 1/4<=delta<5/16. Write B(a,b) for
its full set of original finite bad parameters.

Enter through L041's local converse, without sixteen-count equality.
Take pairwise disjoint label sets P, {y}, {z}, W in H, with |P|=3
and |W|=4. Put
\[
 A_0=P\cup\{y\},\quad A_1=P\cup\{z\},\quad A_2=W,
 \qquad U=P\cup\{y,z\}\cup W.
\]
Thus |U|=9, tau=0, (n_01,n_02,n_12)=(3,0,0), and the singleton
counts are (1,1,4). Choose three distinct original finite parameters
gamma_0,gamma_1,gamma_2 in F. Define
\[
 \alpha_0=\gamma_1-\gamma_2,\quad
 \alpha_1=\gamma_2-\gamma_0,\quad
 \alpha_2=\gamma_0-\gamma_1,\qquad
 c_x=\prod_{t\in H\setminus U}(x-t)\quad(x\in U).
\]
Choose lambda in F^* and p_x in F minus {0,1} for every x in P.
Define words e_0,e_1,e_2 by zero outside their respective A_i and by
\[
 e_0(x)=\lambda c_xp_x/\alpha_0,\quad
 e_1(x)=\lambda c_x(1-p_x)/\alpha_1\quad(x\in P),
\]
\[
 e_0(y)=\lambda c_y/\alpha_0,\quad
 e_1(z)=\lambda c_z/\alpha_1,\quad
 e_2(x)=\lambda c_x/\alpha_2\quad(x\in W).
\]
All stated weights are nonzero. Let a,b in F^H satisfy
sigma(a)+gamma_i sigma(b)=sigma(e_i) for i=0,1. These words exist
by L041's formula (4); every other pair with the same syndrome pencil
is included. No rationality assumption is made on the weights,
parameters or original excluded projective direction.

## Conclusion

The entire original bad set satisfies
\[
                         |B(a,b)|\le11.
\]
In particular this local-converse row cannot realize L010's
sixteen-count equality. The count includes every lower-weight event
and is an upper bound, without a row-specific attainment claim.

This specialization depends on L069's audited complete finite
configuration bound. It proves no universal extraction of this row,
uniform triangle bound, improved global interval or challenge-level
resolution. A separate critical audit on 2026-10-14 found no defect
in this application, with the stated computational dependence retained.

## Proof

### Local-converse entry and polynomial nonpersistence

The displayed supports and weights meet exactly L041's local-converse
gates: nine distinct labels, three distinct finite parameters, nonzero
lambda and three double-coordinate weights p_x not in {0,1}. Thus
L041 applies without its necessary direction's equality premise. It
supplies the third syndrome identity, independence of the coefficient
syndromes and the three full, unique base errors, bad on their own
twelve-coordinate complements for this same a,b.

Its nonpersistence conclusion holds for the original chart. Specifically,
L010's pointwise identities, applicable before any global equality
assumption, give D(gamma_i)!=0 and
\[
 L(\gamma_i,X)=D(\gamma_i)\prod_{x\in A_i}(X-x).
\]
Hence D is a nonzero polynomial. The triple intersection is empty,
so each coordinate x in H is absent from at least one A_i. At that
gamma_i its coordinate locator ell_x(gamma_i) is nonzero. All sixteen
locators are therefore nonzero polynomials. Individual singular
parameter values elsewhere are allowed. These facts are the audited
tau-zero conclusion of L041, specialized to this row.

The standard distance input used in these local results is J. I. Hall,
*Notes on Coding Theory*, GRS chapter, Theorem 5.1.1 and proof,
printed pp. 63–64 of the undated
[author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
Its distinct evaluations, nonzero multipliers and 0<k<=n hypotheses
hold here with unit multipliers, n=16 and k=8, giving distance nine.
The approved assessment reuses the inspected theorem and full proof.
No distance or shortening theorem is reproved in this application;
L041's existing audited shortening specialization supplies its converse.

### Five-coordinate applicability in the unchanged finite chart

The selected pair has
A=A_0 union A_1=P union {y,z}, of size five. Let U_A be the moment
image of words supported on A, as in L015. Both e_0 and e_1 are
supported on A. Their exact moment identities give
\[
 \sigma(b)=\frac{\sigma(e_1)-\sigma(e_0)}{\gamma_1-\gamma_0},
 \qquad
 \sigma(a)=\sigma(e_0)-\gamma_0\sigma(b).
\]
The denominator is nonzero, and U_A is an F-linear subspace, so
both coefficient syndromes belong to U_A. This is L015's stated
two-full-error application with intersection size three. Together
with the just-verified polynomial nonpersistence, the fixed F,H,C
and radius cell verify every hypothesis of that result. Therefore
\[
                       |B(a,b)|\le5+M(A).
\]
No transformation of the original chart is used in these identities.

### Audited configuration bound and full-B scope

Import only L069's logically separate universal conclusion:
M(A')<=6 for every five-set A' subset H. Its complete Plucker-pair
and independent affine-direction censuses cover all 273 free
multiplicative orbits, hence all 4,368 five-sets, and its separate
October 11 critical audit checked the stronger threshold six.
The complete summary is
`scripts/coefficient-feasibility/five-coordinate-complete-census-audit.json`;
the critical-audit certificate is
`scripts/coefficient-feasibility/five-coordinate-critical-audit-result.json`.
The canonical L069 proof specifies all full census artifacts and
reproduction commands. Those audited results are reused, without a
new replay or a claim that a certificate preview verifies them.
The two count paths share a C++ compiler and residue field, and
the census is not formally verified. Its computational qualification
is retained in this conclusion.

L069's triangle hypotheses and its additional-recovery set are not
used. Substituting its universal M(A)<=6 into L015's full-B bound
gives |B(a,b)|<=5+6=11, as required. No three-base subtraction is
needed. L015 counts at most five affine-coordinate cancellation
parameters first, including every lower-weight possibility there.
Outside them its distance-nine argument forces any sparse error
to have four nonzero weights on a support disjoint from A; its
injective projective parameterization and rational-line passage
bound all such parameters by M(A). L010 identifies these sparse
events with same-support badness under the verified nonpersistence.
Consequently the bound retains the entire original finite B,
including singular determinant values and repeated support witnesses
for a lower-weight error. Only the configuration line, if it contains
two rational points, descends; neither weights nor the original
finite chart are assumed rational. This completes the application.

### Separate critical audit (2026-10-14)

The approved audit read this proof and L015 completely, L041's exact
converse and completed audit, L010's pointwise and same-support proofs,
and L069's universal configuration proof and completed census audit.
No missing premise or uncovered finite event was found. The following
checks validate this application, without adding a new bound.

1. The disjoint roles have sizes 3,1,1,4, so each A_i has size four,
   their union has size nine and their triple intersection is empty.
   Each alpha_i is nonzero by distinctness of the original parameters;
   each c_x is nonzero since its factors compare distinct H labels.
   The lambda and p_x gates make every displayed error weight nonzero.
   At x in P the two normalized contributions sum to p_x+(1-p_x)=1;
   at each singleton label the sole contribution is 1. Thus these are
   exactly L041's gated converse weights, not its equality-only necessary
   direction. In particular alpha_2 is nonzero, so the two anchored
   syndrome identities determine the third through L041's relation (2).
   L041 supplies uniqueness, independence and same-support failure for
   every realizing a,b, not just its displayed representatives a_*,b_*.
2. L010's factorization at a full error is pointwise and precedes its
   use of polynomial nonpersistence. It gives D(gamma_i)!=0. For x in P
   use gamma_2 to test ell_x; for x=y use gamma_1, for x=z use gamma_0,
   for x in W use gamma_0, and for x outside U use any gamma_i. Each
   chosen support omits x, so every factor in the locator evaluation
   is nonzero. This verifies every locator as a polynomial in the
   original chart, without asserting nonvanishing at all parameters.
3. A=P union {y,z} has exactly five labels. Subtraction of the two
   original finite moment equations gives the displayed sigma(b)
   identity with denominator gamma_1-gamma_0!=0; the sigma(a) identity
   follows at gamma_0. Both lie in U_A. The fixed field, subgroup,
   dimension, shifted moments and radius cell coincide with L015.
   The linear change from these two independent event syndromes to
   the coefficient syndromes is invertible. Thus the independent branch
   of L015 applies; no degenerate coefficient case is silently omitted.
4. L015's unique affine five-coordinate lift has no identically zero
   coordinate, since such a coordinate would force a fixed support of
   size at most four and contradict the just-verified nonpersistence.
   Its at most five cancellation parameters are counted regardless of
   their actual error weight, badness or determinant singularity. At any
   other parameter the lift has weight five. A sparse representative
   gives a nonzero codeword as its difference with this lift; distance
   nine rules out weight at most three or a four-support meeting A.
   Every remaining bad event therefore has a full four-error disjoint
   from A and corresponds to a configuration point. Such an error also
   has nonzero D by the pointwise identity, so no singular sparse event
   remains outside the cancellation branch. Parameter injectivity counts
   parameters once; multiple support witnesses at a cancellation cannot
   increase that branch's bound.
5. The external configuration is precisely L015's p_K, and L069's
   universal assertion concerns this same M for every five-set, including
   A. Its proof and completed audit certify the threshold six separately
   from its triangle consequence. An extension-field line containing two
   distinct rational configuration points descends as in L015; a line
   with at most one such point already meets the bound. Neither this
   argument nor the two moment identities rationalizes the original
   chart or weights. L069's R, triangle hypotheses and three-base
   subtraction are unnecessary. Therefore the full finite bad set is
   covered by 5+M(A)<=11.

The completed October 8 and October 11 input audits are reused; no
specific discrepancy required a new census, artifact preview or replay.
The two computational count paths' shared compiler/residue-field and
nonformal qualifications remain. The direct mathematical inputs are
unchanged. This is a correctness review of the existing reproduction,
not new mathematics or progress beyond the sources checked. Universal
extraction, uniform triangle twelve and the challenge qualifications
remain unresolved; the global interval is unchanged.

## Mathlib

Full matching three-common-row count and configuration maximum:
**not checked**. Supporting RS-distance, moment-kernel, affine
interpolation, projective-line and finite-field coverage: **not checked**.
Unknown coverage is not absence, and no Lean-certified census is claimed.
The pinned event uses the inspected ArkLib definition cited in L015;
ArkLib is separate from Mathlib and the unread July ABF26 definition.

Classification: REPRODUCTION, a row-specific application of existing
audited local inputs and their computationally dependent bound.
This establishes local applicability, without a novelty claim or
progress beyond the sources checked. The separate application review
found no defect; independent global/challenge gaps remain unresolved.
