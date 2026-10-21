# Primitive rational-factor feasibility at five — bounded method review complete

TARGET: Test whether both complete L095 systems admit nonzero primitive Z_5-points with m and C units, preserving one common tuple and the exact system-II factor 5^11.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the rational-factor signature and branch assessments; read L095 and its complete independent audit, local-method assessments and ATTEMPTS/043,046–048; new exact-prime, cover-polynomial and Putz searches found no inspected theorem deciding these systems. Queries and failed retrievals are recorded below.
SOURCE_EVIDENCE: Reused the inspected primary statements and proofs of Zabradi (29 June 2022), Lemma 2.3 and Theorem 2.4 p.4, and Clark Theorem 1.79 p.58 through foundations/17-local-power-hensel-inputs.md; reused Putz's special-coefficient/global and Pacetti–Villagra Torcomian prime-eleven comparisons. Fresh Putz five-adic passages were not successfully retrieved and are not imported.
COMPARISON: General Hensel criteria apply at five to integral polynomials, including nonunit derivatives under a strict error bound, but do not decide this target. L095 supplies both exact equations; no division by 5^11, integral normalized equation, seed or primitive lift is established by this review.
GAP: Need exact nonzero common primitive tuples in both systems or an exhaustive obstruction for one; if normalizing II, first prove the proposed equation integral and equivalent on the permitted domain. Global compatibility and integer elimination remain unresolved.
REASON: Reused primary method coverage suffices for one bounded elementary attempt on the original integral equations; the inaccessible additional family-computation lead is not essential to this attempt. No matching verdict or novelty claim is asserted.
LITERATURE_REASON: The saved target changes the prime to five, where the system-II scale is nonunit; this turn reviews that changed scope rather than repeating ready two-, three- or eleven-adic work.
SCOPE: Exactly TARGET using audited L095; elementary exact polynomial identities, valuation and residue tests, and the cited Hensel criteria over Z_5 only. Any normalization requires proof of integrality and exact equivalence. No class arithmetic, local algebra enumeration, global exclusion or classification of all valuations is approved.

## Exact proposed domain and use

Use the full audited L095 forms Q,H. The proposed test is over Z_5,
with m,u,a,C all nonzero and m,C units. Keep either

- I: C=5m+u^5 and H(m,C)=a^3;
- II: C=m+5^10u^5 and H(m,5C)=5^11a^3.

Require the reconstructed A=ma, B=Q(m,dC)u and C to be nonzero
and locally primitive. The same m,u,a,C must satisfy both equations.
The unit requirements are the five-adic part of L095's original gcd
conditions. No real positivity or coprimality at other primes is imposed
on a five-adic point; no independent coordinate roots may be combined.

An exact local obstruction would eliminate the corresponding integer
system. An exact common primitive point in each system would instead
retire standalone exclusion at five. Neither conclusion alone settles
both integer systems, other algebra types or the residual Beal signatures.
Stop after deciding feasibility if possible; do not expand into a full
valuation classification or repeat tests at the three previously treated
primes. If a lift is singular, record its exact obstruction instead of
inferring existence from a finite residue sample.

## Reused primary theorem coverage and scope comparison

The main gap is integer elimination of both complete L095 systems in
ordered (3,5,11), with other algebra types and other signatures still
independent. This review changes no mathematical argument in PROOF.md.
L095's statement, full denominator analysis, identity (4), both converses
and independent audit were read. Its unit restrictions at five are part
of the target, rather than an assumption that all coordinates are units.
ATTEMPTS/043,046,047 retire exclusion at eleven, three and two respectively;
ATTEMPTS/048 parks the rational scaling shortcut. None decides five.
The prior branch assessment and its adequate signature discovery remain
usable; no duplicate five-adic feasibility proof was located in the
specified rational-factor assessments and stop records.

Gergely Zábrádi, *Notes for the course p-adic methods in arithmetic*,
ELTE summer school, 29 June 2022,
[primary notes](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
Lemma 2.3 and Theorem 2.4, printed p.4 (PDF index 3): reuse the statements
and proof cases inspected in the ready eleven- and two-adic assessments.
For f in Z_p[x_1,...,x_r], an approximate zero modulo p^n and a partial
derivative of valuation k with 0<=2k<n give an exact zero congruent modulo
p^(n-k). The proof fixes the other coordinates and iterates one-variable
lifting. There is no exclusion of p=5. Pete L. Clark, *Algebraic Number
Theory II: Valuations, Local Fields and Adeles*,
[author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, printed p.58, in the inspected 161-page version without an
identified revision date, supplies the complete discretely valued field
criterion v(f(alpha))>2v(f'(alpha)) and its specified nearby unique root.
The exact hypotheses and conclusions are retained in
`foundations/17-local-power-hensel-inputs.md`; neither theorem is reproved.

Both original equations in II have integral coefficients. This allows
an attempt using the original difference H(m,5C)-5^11 a^3 after retaining
the defining C relation; it does not supply a useful derivative or a root.
The nonunit multiplier is not invertible in Z_5. No source justifies
silently dividing it away. If a proposed reformulation divides by it,
the next attempt must prove divisibility on the precise substituted
domain, equivalence of equations, and the resulting derivative bound.
Alternatively it may test the original integral equations directly.
These are review conditions, not a derivation of a normalization. Fixing
coordinates for Hensel is permissible only after retaining both equations;
independent roots for two different C values do not answer the target.

Reuse Putz (2024), *Enumeration of local and global étale algebras applied
to generalized Fermat equations*, DOI
[10.5463/thesis.832](https://doi.org/10.5463/thesis.832), Section 5.2 and
terminal proof cases pp.170–173, as compared in
`2026-10-18-ordered-three-five-eleven-rational-factor.md`: those global
exclusions retain their special coefficient set, excluding (1,1,1).
Reuse its comparison of Pacetti–Villagra Torcomian, *On the generalized
Fermat equation of signature (5,p,3)*, Theorems A–C, pp.1–5 of the checked
42-page author copy: the prime-eleven exception prevents the required
import. These hypotheses have not changed. L001's unrestricted local
solubility and the other-prime lifts are insufficient for either tuple.

## New discovery and access limits

Queries on 2026-10-19 included `"Putz" "Proposition 5.18"`,
`"3t^2+t+1" "5-adic"`, `"3,5,11" "5-adic" rational`,
`"Putz" "5.18" "5.19" algebras`, and thesis-domain searches for
5.15, 5.16 and 5.18. Unrelated hits were not theorem evidence.
The author's repository [etale-algebra-family](https://github.com/CPutz/etale-algebra-family)
was a discovery hit already compared in the prior branch assessment;
no code was executed. The indexed thesis passage from Section 2.7.6
suggests a transformed model for local algebra computation. It was not
inspected with its full proof and is an unread lead, not a normalization
or feasibility input here.

The [primary thesis PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf)
initially returned metadata, but targeted text retrieval and page-image
requests did not yield inspectable theorem content. Alternate `/files/`
and query/fragment requests failed; shell retrieval failed DNS. No claim
is made to have read fresh five-adic propositions or their proof cases.
This does not block an elementary attempt using the already inspected
Hensel theorem on L095 itself. A future target using a Putz local-family
list must separately obtain and assess its exact hypotheses and cases.
The bounded search establishes neither originality nor literature-wide
absence. Mathlib coverage of these systems and supporting declarations
is not checked; unknown coverage is not evidence of absence.

## Approved bounded attempt and decision test

Keep the saved TARGET unchanged. Permit one attempt on both systems,
first seeking exact existence from a convenient choice of coordinates;
existence needs only one admissible tuple per system. Begin with residue
and valuation checks at five. If using a normalized equation, verify its
full identity and integrality before testing residues. Seek a seed modulo
five with unit derivative; if singular, allow one refinement through
5^3 on the proved integral formulation with the strict Hensel bound as
the test. An insufficient bound at that cap is inconclusive, not an
obstruction. Do not increase precision without a specified discriminating
test or turn this into a valuation classification.

For any lift, verify nonzero m,u,a,A,B,C, unit m,C, local primitivity,
both equations under one common tuple, and the original reconstructed
equation using L095 identity (4), cancelling exactly 5^11 only as an
equality in the domain. A nonexistence claim instead needs an exhaustive
obstruction covering the full allowed unit-m, unit-C domain, including
nonunit u or a where permitted. Failure of a convenient seed is no such
obstruction. Exact points in both systems retire standalone exclusion
at five; an exhaustive obstruction eliminates only its own system.
If neither is obtained in this bounded attempt, preserve the evidence
and reassess. No global compatibility or positive integer lift follows.

This literature-only turn produces no residue computation, new lemma,
normalization proof or mathematical script. The next invocation may use
this saved EXPLORE assessment for the exact unchanged target.
