# Source comparison: overlapping support polynomials

TARGET: Determine whether shared quadratic factors of consecutive support quartics give a labeling-independent rank-28 certificate for L025's sixteen alternating-condition blocks over F_97.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: October 5 bounded searches for exterior spans of polynomial-multiple subspaces, isotropic polynomial subspaces, overlapping roots and common-factor rank criteria found no inspected theorem deciding this fixed-H simultaneous rank; exact queries and rejected leads are recorded below.
SOURCE_EVIDENCE: Read Gandini arXiv:1810.11694v3 Theorem 1.1, Definition 7.1, Proposition 6.1 and Theorems 7.3/7.5 with their displayed proofs; read Boito–Ruatta SNC 2011 proceedings pp. 75–76, section 2 and section 3.2 Proposition 2/Corollary 1 with the diagonalization proof; reused the earlier generic GM-MDS assessment and inspected L010/L025/L026's relevant local arguments.
COMPARISON: Gandini's characteristic-zero regularity bounds and Boito–Ruatta's single-quotient multiplication rank do not establish the simultaneous exterior-square span over F_97; the existing cyclic proof and 4096 exact samples also leave universal labeling open.
GAP: A labeling-independent propagation or elimination argument for all 28 alternating coordinates is missing; pairwise polynomial common factors are inputs, not an established global certificate.
REASON: Essential comparison now supports one bounded universal overlap proof attempt without importing these mismatched theorems; the search establishes neither rank 28 nor novelty.
SCOPE: Only L025's sixteen cyclic 0125 edges under an arbitrary bijection to fixed H, and L026's full 96-by-28 matrix; permits one overlap-factor proof attempt, not more label sampling, generic evaluations, a decomposable-kernel substitute, or other support families.

## Exact proposed input and use

For a bijection lambda: Z/16Z -> H, use the sixteen supports E_t
from L025 and their quartics P_t(X)=prod_(x in E_t)(X-x).
L026 identifies the annihilator as the coefficient space of
P_t times polynomials of degree less than four, and defines its six
alternating constraints. The proposed route is to use common polynomial
factors of neighboring supports to force every common alternating kernel
vector to be zero. The target demands rank 28 for every labeling at
the fixed H; it does not permit algebraically independent evaluations,
unproved label symmetries, or a decomposability assumption to be substituted
for the full rank assertion. No such forcing argument is derived here.

Downstream use would be exclusion of this abstract family over every
extension, with L010's moment independence and L025's disjoint pair
handling dependent directions. Other equality support families, actual
locator gates and ABF26 correspondence remain independent gaps.

## Reused coverage, duplicates and failures

Reuse the [arbitrary-label assessment](2026-10-05-cyclic-0125-arbitrary-label-rank.md)
for Lovett, Brakensiek–Gopi–Makam and Brakensiek–Dhar–Gopi's inspected
generic GM-MDS statements and Hall's distance theorem. Their selectable
or algebraically independent evaluations and column-span intersection
conclusions do not certify this prescribed exterior-coordinate matrix.
The prior del Campo/Sottile graph mechanism still requires direct sums
and invertible graph maps; these are not supplied by neighboring overlaps.
No generic theorem, distance theorem or graph theorem is reproved here.

Read L010's moment-kernel and eight-column argument; L025's edge table
and disjoint pair; and L026's equations (1)–(3), separate dependent case,
and complete arbitrary-label construction/basis-independence paragraph.
L026 already answers the eight cyclic-generator labelings, using
coefficient scaling that is unavailable for a general bijection. Its
4096-label certificates are retained as checked finite cases, not
universal evidence. This turn does not rerun or audit that calculation.
History/042 and ATTEMPTS/018 preserve those scope limits; ATTEMPTS/017
preserves the failed universal six-edge/eight-vertex route. L024's
different two-block family and L022's saved disjoint triple do not cover
this family. L009's weight-orbit restriction cannot be imposed on its
unrelated weights. The historical stops remain local to their mechanisms.

## Bounded search and primary-source comparisons

Queries issued October 5, 2026:

- `"polynomial subspaces" "exterior" roots`
- `"alternating forms" "Reed Solomon"`
- `"subspace" "wedge" "GM-MDS"`
- `"common factors" "subspaces" "polynomials" rank`
- `"exterior algebra" "subspace arrangements" "ideals" regularity`
- `"Bezout" "exterior" "polynomials" common factors`
- `"alternating" "polynomial" "isotropic" subspaces roots`
- `"wedge" "polynomial multiples"`
- `"Bezoutian" "rank" "gcd" theorem polynomials field`
- `"exterior powers" "polynomial subspaces" rank`
- `"subresultant" "exterior" polynomial common factor`
- `"polynomial" "subspaces" "overlapping" roots rank`
- `"Resultant-based methods for plane curves" Bezoutian`
- `"Extended companion matrix for approximate GCD" Boito Corollary`
- `"Bezoutian" "field" "Theorem" "gcd" site:arxiv.org`
- `"polynomial multiples" "subspace" "rank" exterior`

**Exterior arrangements.** Francesca Gandini, *Resolutions of ideals
associated to subspace arrangements*,
[arXiv:1810.11694v3, June 24, 2019](https://arxiv.org/html/1810.11694v3).
Theorem 1.1 assumes a finite-dimensional vector space in characteristic
zero and gives a linear resolution for a finite wedge product of linear
ideals. Definition 7.1 constructs arrangement-ideal module functors;
Theorems 7.3 and 7.5 give t-regularity. Read their displayed proofs and
Proposition 6.1's regularity-transfer argument: they transfer symmetric
ideal regularity using the exact transpose functor and identify the
product using Proposition 7.4. The full functor construction and cited
regularity proofs were not audited or imported. This gives no prescribed
degree-two span equality for our sixteen exterior-square subspaces and
has the wrong characteristic. No reduction modulo 97 is justified by
the inspected statements. This source is rejected as a rank certificate,
not as a counterexample to the proposed overlap mechanism.

**Common-factor matrices.** Paola Boito and Olivier Ruatta,
*Extended companion matrix for approximate GCD*, SNC 2011 proceedings,
pp. 74–80, [primary paper](https://www.csd.uwo.ca/~mmorenom/SNC-11-file-for-ACM/p74-Boito.pdf),
[publication DOI](https://doi.org/10.1145/2331684.2331696).
Read section 2, printed p. 75, and section 3.2, p. 76, through
Proposition 2, its proof and Corollary 1. The setup uses an algebraically
closed field K, monic f,g and squarefree f of degree d. Multiplication
by g on K[X]/(f) is diagonal in the Lagrange basis with entries g(z_i);
the corollary states corank(M_g)=deg(gcd(f,g)). This is a single-quotient
criterion, not a rank formula for sixteen exterior-square blocks.
No finite-field specialization or pair-to-global inference is made here.
The approximate numerical algorithms and section 4's Barnett formula
are not used. Initial access failed; a retry retrieved the primary PDF,
so this comparison has no essential source blocker.

Busé–Khalil–Mourrain's *Resultant-based methods for plane curves
intersection problems*, DOI 10.1007/11555964_7, was an unread lead:
the CiteSeer PDF request timed out. Its snippet is not theorem evidence.
It was sought as an alternative pairwise-resultant source, not an
identified simultaneous-exterior-rank theorem, so its access failure
does not block this target. Other hits on real isotropic spaces,
approximate gcd software and hyperplane cohomology were rejected at
scope screening; no theorem from them is asserted. A failed exact search
is not evidence of originality. No essential unread matching theorem
was identified in this bounded review.

## Approved attempt and discriminating test

The unchanged TARGET receives EXPLORE coverage for one future proof
attempt. This literature turn proves no new mathematical claim and
modifies no lemma or mathematical script. No result from the two new
sources is imported; their limitations explain why citation does not
suffice. Mathlib coverage of the exact overlap rank criterion is **not
checked**; L010/L026's existing qualifications remain unchanged.

Use L026's actual coefficient-row spaces and their six alternating
constraints over F_97. Seek a uniform implication from the sixteen
overlapping quartics to vanishing of every alternating coordinate.
The neighboring common factors named in the target may be taken from
L025's displayed edges; any propagation across their quotient factors
and any division must be proved with its nonzero hypotheses. A proof
may use the fixed H, but cannot treat its labels as independent
indeterminates or assume cyclic coefficient scaling. Keep the rank-28
conclusion for the whole alternating space; ruling out only decomposable
vectors would be a changed target requiring separate review.

Continue on this mechanism only if the bounded attempt gives a complete
uniform certificate or a concrete new constraint with a stated remaining
rank gap. An exact deficient labeling stops the uniform rank criterion;
an explicit failure of a proposed propagation inference stops that
inference. If a pass through the sixteen overlap constraints leaves an
unproved global closure without a new testable constraint, record the
missing inference and park the overlap-only route instead of adding
another sample batch. This will be the third mathematical exploration
turn if it supplies neither ADVANCE nor NEGATIVE; reassessment is then
required. This source turn leaves the existing two-turn usage unchanged.
Even rank 28 excludes only this support family: other equality families,
the global fifteen bound and ABF26 correspondence remain unresolved.
