# Fixed canonical class at every rational prime — source coverage ready

TARGET: Determine whether L062's fixed global class belongs to the primitive whole-fiber connecting image at every rational prime.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the exact local interfaces, ready canonical/thirteen assessments, histories 187,191,193,195 and ATTEMPTS/029; searched fixed-class/X0(11) all-prime membership, coprime-exponent parametrization and local unit powers. Inspected the standard common-multiplier construction in Bennett–Mihăilescu–Siksek Section 4, not merely its search excerpt; no inspected exact fixed-class theorem was found and no novelty is inferred.
SOURCE_EVIDENCE: Newly inspected Bennett–Mihăilescu–Siksek's 31-page author manuscript Section 4 p.22, the entire coprime-exponent construction after (27); rechecked Clark Theorem 1.79 p.58 and Corollary 1.77 p.57, and Zábrádi Lemma 2.3/Theorem 2.4/Corollary 2.5 p.4 with the relevant lifting proofs. Reused assessed Schaefer–Stoll localization, FNS entire-fiber and Stacks tensor-product inputs, and audited L046/L047/L049/L062/L064.
COMPARISON: Known exponent congruences provide a common-multiplier method, and local lifting permits a freely chosen shared c with cube/fourth roots rather than an eleventh-root assumption. These are sufficient general tools for a reproduction attempt; they do not themselves assert primitive fixed-scalar membership at every prime. Existing whole-fiber and same-class results cover exceptional assembly inputs without needing full local-image enumeration.
GAP: No essential source gap remains for one bounded attempt; prove a uniform primitive fixed-scalar construction, verify the seven-adic nonunit case, and assemble every exceptional prime using the same normalized class. All-prime membership remains unproved.
REASON: Approve a REPRODUCTION specialization of known exponent-congruence/lifting methods and existing exact witnesses; this changes the route from uncovered uniform discovery to a finite explicit assembly problem, without deriving or approving a new theorem in this literature turn.
SCOPE: Exactly TARGET; uniform cube/fourth power correction at the canonical scalar, with exceptional audit list {2,3,7,13}, whole-fiber localization of the fixed sigma, and previously proved same-class/singleton witnesses. No full image enumeration, new global class, class/unit basis, integer lift or cross-notebook input.
LITERATURE_REASON: The expanded all-prime quantifier was outside previous ready assessments; this single comparison fills that essential scope gap and reuses their unchanged descent and fiber coverage.

## Proposed continuation and discriminating test

Main gap: positive primitive integer emptiness in the 54a1 branch, with
many other residual Beal signatures still unresolved. This target asks
whether one fixed class already survives every finite-prime test. A proof
would retire finite-prime removal of this survivor and focus attention on
global lifting or stronger data; a rigorously excluded prime would instead
supply an effective additional necessary restriction. Neither would settle
integer emptiness by itself.

Retain L033's K and normalized delta, L034's complete projective j-map,
L062's fixed sigma and alpha_sigma, and audited L064's thirteen-adic
same-class witness. Potential assembly inputs are L036/L041's common
scalar domains and L046/L049's whole-algebra singleton comparisons at two
and three; review their exact interfaces before application. The canonical
scalar ratios recorded in L062 are the starting data, not new points
chosen independently at each prime. All lemma identifiers are local.

Review known primitive local scalar criteria, uniform unit constructions,
Hensel hypotheses at primes dividing an exponent, and relevant standard
connecting-map naturality. Check exact literature/overlap before research;
do not repeat L064's scalar search or the exhausted quotient/generator
routes. The requested theorem permits a different scalar only when its
connecting class is proved to equal the localization of the fixed class.

Continue only with ready coverage for a uniform argument plus a finite,
explicit exceptional-prime list. Abandon a proposed all-prime proof upon
a genuine excluded localization or an unrepairable compatibility defect;
a failed canonical scalar alone is insufficient (ATTEMPTS/029). An
unresolved prime must remain an obligation, never disappear into a claim
based on finitely many successful tests. No full eleven-adic unit image,
class v, Selmer/point equality, GRH, real-place assembly or integer solution
is assumed. Uniform finite-prime membership itself remains unproved.

## Completed source comparison, 2026-10-13

The preceding proposed-continuation text is retained as the pre-review
record. Coverage is now ready for the bounded attempt specified below;
no uniform scalar lemma or new membership theorem was proved this turn.

### Primary statements and comparison

Michael Bennett, Preda Mihăilescu and Samir Siksek, *The Generalized
Fermat Equation*, in *Open Problems in Mathematics* (2016), pp.173–205,
[DOI](https://doi.org/10.1007/978-3-319-32162-2_3),
[Siksek-hosted author manuscript](https://samirsiksek.github.io/siksek.github.io/papers/bealconj.pdf),
31 pages, revision date unidentified: Section 4, manuscript p.22,
the unnumbered construction immediately after (27). The authors assume
pairwise coprime positive exponents, choose three inverse congruences,
and multiply an equation a+b=c by a common monomial so that its three
terms become the required powers. The complete displayed construction
and surrounding primitivity qualification were read. It constructs
generally nonprimitive solutions; it does not import primitive integer
solutions or fixed-class membership. The method is standard overlap
with the proposed unit construction. Its application to unit scalar
ratios and normalized nonunits requires separate verification of
primitivity and preservation of the prescribed scalar. A reproof of
the general construction is unnecessary. The publisher DOI failed
retrieval, but the essential author-hosted passage is accessible;
this is not an essential source blocker.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
revision date unidentified: Corollary 1.77, p.57, gives a lift of a
simple residue root for an integral polynomial over a complete valued
field; its full proof was read. Theorem 1.79, p.58, gives Hensel–Newton
under |F(r)|<|F'(r)|², with the stated uniqueness and distance clauses.
These cover unit cube/fourth roots only after proving the residue
conditions and a unit derivative; neither separate surjectivity of
both power maps nor an eleventh root is supplied.

Gergely Zábrádi, *Notes for the course p-adic methods in arithmetic*,
ELTE summer school, June 29, 2022,
[author notes](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
13 pages: Lemma 2.3 and Theorem 2.4, p.4, require an integral
polynomial, congruence modulo ell^n and derivative valuation k with
0<=2k<n. The theorem's proof keeps every coordinate but one fixed
while iterating the one-variable lift. Corollary 2.5, p.4, splits the
unit group into residue roots of unity and principal units, lifting
all distinct roots of X^(ell-1)-1. Statements and these complete
proofs were read. This is a residue-and-lifting tool, not a theorem
that perturbing a sum equation preserves its scalar. The future proof
must lift the two normalized power equations with the same fixed c.

Reuse Schaefer–Stoll, *How to do a p-descent on an elliptic curve*,
June 13, 2001 long manuscript, Section 5 pp.8–9 (connecting evaluation
and restriction diagram), as already inspected in the canonical-class
assessment; Stacks Lemma 26.17.2/tag 01JQ (entire fiber tensor product);
and FNS June 10, 2019 Section 7.2's canonical entire-fiber identification.
Their exact statements and applications are canonical in L033/L062;
none is being refreshed or reproved. Their general scope is every
completion, even when K tensor Q_ell splits or ramifies. The uniform
argument can tensor the same sigma rather than calculate a new field
decomposition at each prime.

### What the next attempt may specialize

L062 supplies the exact nonzero ratios t=7³/2⁹ and q=13²/2⁹, t+q=1.
The explicit audit list {2,3,7,13} consists of their numerator/denominator
support together with the cube/fourth derivative primes. It is a list
of cases to prove, not a claim that an all-prime proof is complete.
Five and eleven need no additional field or unit-image enumeration
merely to witness membership: the fixed entire canonical fiber and
one common primitive triple suffice by definition. L062 already
constructs those triples, although its eleven-adic stated filter is
only a valuation projection. A vector passing L044 must never be
substituted for full-class membership.

Away from the audit list, use the known exponent-congruence method or
residue power correction with a freely chosen shared unit c, then
cube/fourth lifting. Verify integrality, unit coordinates, exact scalar
identities and preservation of sigma. At seven, the recorded ratios
require a separate nonunit valuation check and normalized-unit
construction; an all-unit parametrization alone is insufficient.
This is the identified mathematical specialization still to do, not
a theorem imported from the source. At eleven do not assume an
eleventh-root map is surjective; a freely chosen c is permitted.

At two, L046 proves the entire unrestricted image and the nonempty
branch-restricted image are both {1}; it includes b odd, c even and
a=7 mod 8. At three, L049 proves the same singleton equality while
retaining a=1 mod 3, b²=1 or 4 mod 9, and c a unit; L047 supplies the
canonical scalar witness. Apply these to the localization of the
fixed global point before identifying its class with the restricted
witness. At thirteen, audited L064 already retains the fixed sigma
and proves that scalar 3 realizes its exact identity class on the
whole degree-twelve algebra. Do not repeat that search or replace
this exact equality by an unrestricted-image claim.

The positive threshold is a proof covering every rational prime,
with these finite exceptional cases explicit and no independently
chosen localized global class. Stop an attempted assembly if any
normalized valuation, residue correction, shared-c identity or
whole-fiber/class comparison fails. Record that exact obligation;
failure of the canonical scalar at thirteen is already repaired by
L064 and is not a new negative result. This would decide survival
of one class, leaving full class intersections, global lifting and
integer emptiness independently unresolved.

### Search, duplicates and limits

External queries included generalized Fermat pairwise-coprime-exponent
rational parametrization; p-adic units/nth powers/Hensel; 54a1/local/11/
Fermat; 54a1/connecting/class; canonical/54a1/9261/descent; and X0(11)/
primitive/all primes/5. Exact-class searches returned no inspected
matching theorem; this establishes neither absence nor novelty.
The primary common-multiplier passage was actually read, not inferred
from search results. Local comparisons used L036/L041, L046/L047/L049,
L062/L064 and their ready assessments. Histories 187,191,193,195 and
ATTEMPTS/029 retain the quotient and thirteen-adic removal stops;
this target neither reruns those tests nor imports a historical ban.
No new outside-paper lead is required for this bounded reproduction.

Full matching all-prime theorem and supporting Mathlib declarations:
not checked. Unknown coverage is not absence. This assessment gives
source coverage, not proof of membership or a candidate Beal solution.
