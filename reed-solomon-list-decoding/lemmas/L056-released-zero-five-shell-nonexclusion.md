# L056 — Releasing the incidence zero makes the anchored five-shell feasible

## Hypotheses

Let H be the 1024-point ground set and V the set of all 68-subsets of H,
as in L053. Use its fixed positive singleton rho and fixed pair moments
rho*p_i. In particular p_0=1, p_1=...=p_4=0,
p_5=1/68881143660, and the objective fixed by these singletons is
M=(U+1)/2 with U=binomial(1024,64)/binomial(68,64).
Fix one anchor A in V and retain exactly its full distance-five union
matrix indexed by {A} and {A,B}, where |A\B|=5. Boolean repetitions
use their lower-order coordinates. Distinct-triple entries are
nonnegative and invariant under permutations of A and its complement,
with zeros only when a pair has half-distance 1,...,4. Require consistency
whenever the same unordered triple orbit is represented in this shell.
No entire-incidence or actual-label zero, extra scalar inequality,
off-shell or other-anchor PSD, or global moment extension is assumed.
All coefficients and PSD matrices are real.

## Conclusion

This shell admits an exact rational feasible witness at the fixed pairs.
In the normalization D=the shell block/(rho*p_5), the maximum row sum
under nonnegativity, forbidden-distance zeros and nonconstant spectral
PSD is exactly

  9965466368/5 = 2*(4982733184/5).

The right-hand parenthesis is the fixed-pair constant Schur requirement.
The witness therefore also satisfies the full anchored shell PSD,
including its constant coordinate. Its released (2,3) coefficient is
strictly positive. This parks this shell alone as an exclusion diagnostic
at these pairs; it does not provide a global triple extension, other
conditioned PSD, representing measure, packing or common-center RS list.
The 955–957 boundary and independent 67/68-agreement gaps are unchanged.
The separate critical proof review below retains this conclusion. This is local reproduction
of assessed spectral/moment tools, without an originality claim.

## Proof

**Source imports and finite specialization.** Reuse the approved SPECIALIZE
assessment `drafts/literature/2026-10-12-five-shell-without-incidence-zero.md`.
The necessary union matrix is imported from Polak, *Semidefinite Programming
Bounds for Constant-Weight Codes*, IEEE Trans. Inform. Theory 65 (2019),
28–38, DOI 10.1109/TIT.2018.2854800, inspected
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and its complete indicator proof, p. 2.
The displayed A(n,d) endpoint is qualified by its A(n,d,w) proof, as in
[foundations/12](../foundations/12-global-degree-three-moment-source.md).
Only a retained principal matrix is considered here; no stronger source
program is claimed feasible and no hierarchy theorem is reproved.

For the simultaneous Johnson spectra and positive multiplicities import
Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Sections 1.2,
3 and 3.4, pp. 3,10,12; and Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Sections 1.4.7 and 11.2, pp. 19,162–163. The Schur congruence is its
Theorem 2.7.1(i), p. 36. Source scope is retained in
[foundations/09](../foundations/09-global-pair-johnson-source.md).
Both factors J(68,5) and J(956,5) meet n>=2*5. Identity relations
are identity matrices. Complete product modes are used; no spectral
or Schur theorem is reproved. Schrijver's
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (65), p. 7, requires the full region data under permutations;
equal distance multisets alone are not used to identify general orbits.

**Entries, unordered consistency and anchor normalization.** L054 supplies
the bijection B=(A\X) union Y with five-sets X in A and Y outside A.
For C=(A\X') union Y', write r=5-|X intersection X'| and
q=5-|Y intersection Y'|. The eight regions, in L053's order, are

  5-r, r, r, 63-r, 5-q, q, q, 951-q.

All 36 product relations occur. B=C exactly when (r,q)=(0,0), giving
the Boolean coefficient rho*p_5. Otherwise the triple is distinct,
its distances are 5,5,r+q and its only forbidden-distance zeros occur
at 1<=r+q<=4. Thus the 21 free relations are
R={(r,q):0<=r,q<=5, r+q>=5}, including (2,3).

The stabilizer acts transitively on each relation: bijections between
corresponding head regions and tail regions extend to permutations of
A and its complement. A triple orbit in this retained scope determines
r by its common size 63-r and q by the nonanchor pair-only size 5-q.
Interchanging B,C preserves these data. If another support in the triple
can be an anchor of a distance-five shell, then r+q=5. In that case all
three pair-only regions have size r, all private regions have size
q=5-r and common size 63-r. Every anchor permutation then returns the
same relation. If r+q is not five, A is the only eligible anchor.
Consequently there are no extra identifications between distinct
relations in R, and the coefficient recipe below assigns one value to
every represented unordered triple orbit. This uses full region data,
not distance-only averaging. It asserts no off-shell extension or
other-anchor matrix PSD.

Write d_rq=x({A,B,C})/(rho*p_5) on R and let D have coefficient one
on the identity, zero at the forbidden relations and coefficient d_rq
otherwise. The whole anchored matrix divided by rho is

  [1, p_5*1^T; p_5*1, p_5*D].

The leading one is positive. Schur congruence and p_5>0 show that PSD is
equivalent to D-p_5*J being PSD; no inverse of D is used. Put
S=binomial(68,5)binomial(956,5)=68643272053310642688. The exact fixed
constant requirement is S*p_5=4982733184/5, reconstructed directly
from the fixed p_5 rather than assumed from the contrasting L055 bound.

**Complete finite inequalities.** For 0<=a,r<=5 let

  E_a^(n)(r)=sum_(h=0)^r (-1)^h binomial(a,h)
                     binomial(5-a,r-h)binomial(n-5-a,r-h),
  m_a^(n)=binomial(n,a)-binomial(n,a-1).

Out-of-range binomials are zero. The valencies
v_rq=E_0^(68)(r)E_0^(956)(q) are positive. Set z_rq=v_rq*d_rq and
H_ab(r,q)=E_a^(68)(r)E_b^(956)(q)/v_rq. All 36 product modes have
positive multiplicities m_a^(68)m_b^(956) summing to S. Because J acts
only on the constant mode, the exact PSD conditions are

  z_rq>=0;
  1+sum_R H_ab(r,q)z_rq>=0 for all (a,b)!=(0,0);
  1+sum_R z_rq>=4982733184/5.

Singular modes are permitted. There are no hidden upper bounds on the
free coefficients.

**Rational witness.** Take the following complete z vector; use
x({A,B,C})=rho*p_5*z_rq/v_rq for distinct permitted triples.

| Relation (r,q) | z_rq |
|---|---|
| (0,5) | 951/5 |
| (1,4) | 1575 |
| (1,5) | 58653 |
| (2,3) | 367485/191 |
| (2,4) | 17916180/191 |
| (2,5) | 694936311/191 |
| (3,2) | 399456402215133585/286862922185032 |
| (3,3) | 4966938279659140005/286862922185032 |
| (3,4) | 558448429378526606835/286862922185032 |
| (3,5) | 21216950193464907717399/286862922185032 |
| (4,1) | 428839606265933565/1147451688740128 |
| (4,2) | 3546370896282575505/1147451688740128 |
| (4,3) | 114973132192983520575/1147451688740128 |
| (4,4) | 16845119518834830126075/1147451688740128 |
| (4,5) | 79557360333028611972375/143431461092516 |
| (5,0) | 72140603592355677/5737258443700640 |
| (5,1) | 50091798040550001/84371447701480 |
| (5,2) | 0 |
| (5,3) | 854236269404759048691/2868629221850320 |
| (5,4) | 198200628251445534236979/5737258443700640 |
| (5,5) | 751047823703083384153959/573725844370064 |

The vector is nonnegative, and its row sum is
1+sum_R z_rq=9965466368/5. In particular z_23=367485/191>0.
Substitution in the displayed finite eigenvalue formula gives this
complete Schur sign table (a indexes rows, b columns):

| a \ b | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | + | 0 | 0 | + | + | + |
| 1 | 0 | 0 | 0 | + | 0 | 0 |
| 2 | 0 | 0 | + | 0 | 0 | + |
| 3 | 0 | 0 | 0 | 0 | + | + |
| 4 | 0 | 0 | 0 | + | + | + |
| 5 | 0 | 0 | + | + | + | + |

Every entry's exact numerator and denominator, not just these signs,
is in `scripts/finite-support/released-zero-five-shell-audit-results.json`
under `all_product_modes`. The constant Schur value is 4982733184/5;
the 35 remaining values are independently reconstructed from the table
above. Thus all modes are nonnegative and the full anchored matrix is
PSD. Zero modes cause no problem for the imported congruence.

**Matching rational dual and exact optimum.** For nonconstant modes
assign omega_a0=m_a^(68) for a=1,...,5 and
omega_a1=(951/5)*m_a^(68) for a=0,...,5; all other weights are zero.
They are nonnegative. Direct substitution in the finite eigenvalue
formula checks, for every one of the 21 relations in R,

  sum_((a,b)!=(0,0)) omega_ab*(-H_ab(r,q))=1.

All 735 coefficients and all 21 column identities are reconstructed
independently in the audit. Hence multiplying the nonconstant
inequalities -sum_R H_ab*z_rq<=1 by omega and summing gives
sum_R z_rq<=sum omega. Here

  1+sum omega=(956/5)*binomial(68,5)=9965466368/5.

The feasible vector attains this bound, proving the claimed maximum.
No approximate solver optimum or code realization is used. L055's
restricted dual is not reused: the released column is explicitly
included in this new certificate.

**Evidence, reproducibility and limitations.** Run from this notebook:

  `python3 scripts/finite-support/released_zero_five_shell.py`

then

  `python3 scripts/finite-support/audit_released_zero_five_shell.py`.

The constructor uses 140-digit Decimal arithmetic for at most 600 pivots
solely to propose a basis (26 pivots used). Exact rational elimination
then reconstructs all primal/dual values and slacks. The full certificate
is `scripts/finite-support/released-zero-five-shell-results.json`.
The verifier imports no constructor routines. It rebuilds the fixed
pairs from L021's saved primal, checks its 64 defining equations and
agreement with L053's fixed pair input, and reconstructs each factor
through Schrijver's full beta summation (Theorem 1 (51), III.A (53)–(58),
pp. 6–7 of the cited author manuscript), using factorial binomials.
All 72 beta/Johnson values, factor orthogonality identities, valencies,
identity entries and complete positive multiplicities are checked.

Explicit finite supports recover all 36 relations and full region data;
all six support permutations are checked for forbidden-distance zeros,
eligible anchors and represented unordered-orbit identifications.
Every matrix coefficient, all 21 primal and 35 dual signs, all 35
nonconstant inequalities, all 21 dual columns and equal objectives are
checked, followed by all 36 full Schur coordinates and the Boolean trace.
The verifier checks the simple dual formula and positivity of the newly
released relation. All 1826 checks pass with no failures. Complete
primal/dual slacks, all product coordinates and failure lists were
inspected. These finite substitutions, together with the source spectra
and normalization above, certify the conclusion; saved success flags
and a preview do not establish it.

This is local finite diagnostic evidence. The paired objective remains
L053's above-threshold M, but the witness is only for the retained shell.
Global triple compatibility, off-shell matrices, actual-label constraints,
other pair moments, full SDP values, uniform useful bounds, representing
measures and RS realization remain unresolved. The earlier L054/L055
exclusions retain their different hypotheses.

**Separate critical proof review — step 184, 2026-10-12.** The unchanged
SPECIALIZE gate is
`drafts/literature/2026-10-12-released-zero-five-shell-critical-audit.md`.
The review retains the result, clarifying only that H has 1024 points
and V is its 68-subset universe. No inequality or hypothesis is changed.

The Boolean-union normalization is checked before the finite arithmetic:
the anchor union has moment rho, while both an anchor/shell union and
a repeated shell index have moment rho*p_5. After division by rho,
Schur congruence leaves p_5*D-p_5^2*J. Since rho,p_5>0, this is
equivalent to D-p_5*J being PSD. The all-ones matrix has eigenvalue S
on constants and zero on all other product modes. Thus the correction
is exactly S*p_5, even though many nonconstant coordinates vanish.
The imported theorem needs no inverse of the shell block.

The region argument is exhaustive, rather than a sample of labeled
triples: for fixed r,q the eight regions partition H, and any two
partitions with the same sizes are carried to each other by a point
bijection. For a fixed anchor, that bijection preserves A and H\A.
Every r,q occurs because both factors have at least ten points.
Distinct represented triples have distances (5,5,r+q), so an alternative
anchor is eligible exactly when r+q=5. Then all three pair-only sizes
equal r and all three private sizes equal q; the common size 63-r
determines r. Otherwise the unique eligible anchor determines r,q.
Hence no two different relations can become identified by permuting
supports and points. At (0,0) there are just two distinct supports;
the only eligible support is A and the union is the prescribed pair.
Full membership-atom reconstruction below checks all these cases,
including Schrijver's invariant t-s=q-r. This verifies consistency on
represented orbits only, without assuming a global extension or label
symmetry of the RS restrictions.

The existing verifier was inspected and rerun: all 1826 exact checks
pass. Its beta normalization divides by binomial(n-2a,5-a)>0;
terms outside max(a,5-r)<=u<=5 vanish, so the full source summation
covers all contributing terms. Both factors satisfy n>=10, all
multiplicities are positive, and the product dimensions exhaust S.
The audit imports this complete spectral theorem, not just a bound on
the smallest eigenvalue. L053 supplies the already audited fixed pairs;
the defining pair equations are rechecked, without claiming to repeat
the proof of L021's optimum.

An additional independent verifier, importing no notebook modules, is

  `python3 scripts/finite-support/critical_audit_released_zero_five_shell.py`.

It parses all 21 rational values and all 36 signs directly from this
manuscript. It independently reconstructs all 735 coefficients, the
complete nonnegative dual, every primal slack and exact dual column,
all product multiplicities and Schur coordinates, and their trace.
Membership-atom representatives reconstruct all eight regions under
all 216 support permutations, compare each full saved region record,
and test canonical full-region keys for cross-relation collisions.
Every saved spectral rational and normalized coefficient is compared,
not merely its sign. All 1814 additional checks pass with no failures.
Complete evidence, source hashes, all modes and all region records are
in `scripts/finite-support/released-zero-five-shell-critical-audit-results.json`.

The dual sign direction is retained explicitly: nonconstant PSD gives
-H*z<=1, so nonnegative weights whose column sums are exactly one
give sum z<=sum omega. The manuscript's feasible z attains equality.
Its constant Schur coordinate is 4982733184/5>0, and the released
coefficient is positive. This proves the exact shell optimum without
a solver-status or strong-duality assumption. No additional scalar,
off-shell or reanchored principal matrix is checked in this review.
The local reproduction is now critically verified; the broader gaps
and the 955–957 boundary remain unchanged.

## Mathlib

Full matching shell certificate, product Johnson spectra, moment program
and Schur coverage: not checked. Supporting finite-set and linear-algebra
coverage: not checked. Unknown availability is not evidence of absence.
