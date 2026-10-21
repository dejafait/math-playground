# Coarse unconditional rank certificate — completed comparison

TARGET: Assess whether a coarse unconditional 2-descent bound can certify rank E1(K)<12 without reproducing FNS's exact Selmer dimension.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the fixed-class Chabauty and even-C assessments; searched number-field 2-descent, coarse rank, class-group upper-bound and unconditional certification variants; inspected Simon and Barrera Salazar–Pacetti–Tornaría.
SOURCE_EVIDENCE: Simon 2002 Section 1.1–1.2, Propositions 1.1–1.4 and full Proposition 1.4 proof, pp.8–9; Schaefer–Stoll June 13, 2001 Section 1 p.2, Section 2 p.3 and Section 5 pp.8–9; Barrera Salazar–Pacetti–Tornaría arXiv:2001.02263v3 Section 1, Definition 1.6, Hypotheses 2.1, Lemma 2.14 with proof and Theorem 2.16, pp.3–5,8,12–13; FNS qualifications reused and Table 5 reaccessed.
COMPARISON: A certified containing space of dimension at most eleven suffices without exact Selmer dimension four, but requires global coverage. The inspected narrow-class bound has additive term [K:Q]=12 and cannot alone give the required strict inequality, even with zero relevant class torsion.
GAP: No unconditional global square-class containing space or below-twelve bound is supplied for this K; unit/class coverage, norm/local maps and E0(K)[2] remain uncertified.
REASON: Separate an inadequate closed class-bound shortcut from a potentially weaker partial-descent certificate; test its bare unit contribution before expensive arithmetic.
LITERATURE_REASON: Essential coverage of this coarse certificate was missing; the unchanged ready Chabauty assessment was reused.

The main gap remains positive primitive integer emptiness, including
L032's 54a1 branch. The intermediate target was a usable unconditional
rank certificate below twelve, potentially supplying one prerequisite
for the rational-j method. Generators, index control, coset zero bounds,
other-class coverage and primitive integer lifting remain independent
gaps. No complete candidate is proposed.

## Primary source comparison

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf),
[DOI](https://doi.org/10.1112/S1461157000000668).
Propositions 1.1–1.2 assume a number field K and a monic integral
irreducible cubic P defining y²=P(x). Evaluation x−theta has kernel
2E(K) and square norm. Proposition 1.3 describes L(S,2) through
S-units and S-class 2-torsion; the named Dirichlet S-unit theorem
precedes it. Proposition 1.4 takes all infinite places and finite
primes P above p with P dividing P'(theta) and p² dividing disc(P).
Its proof retains negative x−theta valuation, positive odd valuation,
and discriminant valuation one. Applicability to our model remains
to check. The subsequent proposed enlargement of S using generators
of class-group 2-torsion is not used: killing that subgroup does
not automatically certify an odd quotient class number.

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS **356** (2004), 1209–1231,
[long manuscript dated June 13, 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X).
Section 1 p.2 records the m-descent exact sequence including m=2.
Section 5 p.8 records
0 -> U_S/U_S^p -> D(S,p) -> Cl_S(D)[p] -> 0
and permits a unit subgroup of index prime to p. Relevant
completeness is modulo the descent prime, rather than a complete
presentation at every prime. Section 2 explicitly fixes p odd:
Proposition 4.6 and its reduced bad-prime prescription are NOT
imported at two. Simon supplies the two-descent specialization;
the Section 5 arithmetic sequence is comparison evidence.

Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3), September 17, 2020.
Hypotheses 2.1 require odd narrow class number of K, E(K)[2]=0,
and Definition 1.6's condition at every finite place. For a monic
integral squarefree cubic it permits: a cubic local field; maximal
polynomial order; odd component index at odd residue characteristic;
or unramified dyadic base with good reduction. Theorem 2.16 p.13
bounds Selmer dimension above by c+[K:Q], where c is the modified
narrow-class 2-rank. Even granting these unverified hypotheses,
c+12 is at least twelve, so the bound alone fails our test. This
does not lower-bound rank. Section 1 allows an étale cubic Kummer
algebra. Lemma 2.14 pp.12–13 and its norm/Dirichlet proof provide
a lead for examining the unit contribution; no stronger bound is
inferred from it here.

FNS, Compositio Math. **156** (2020), 77–113,
[June 10, 2019 final manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2 pp.25–27/Table 5, concerns E0=X0(11) over L033's K.
Dimension four depends on GRH class certification; insufficient
generators are a separate obstacle. These qualifications are reused
from the fixed-class assessment. Rank transfers between L033's
E0 and E1: the standard dual-isogeny theorem (Silverman, *The
Arithmetic of Elliptic Curves*, 2nd ed., III.6.1) gives both
compositions [5], and the Mordell–Weil theorem allows tensoring
with Q, where the induced maps are inverse up to multiplication
by five. This justifies the choice of E0 for descent, without a
new rank bound.

## Exact weaker certificate and missing evidence

A verified integral cubic model gives the entire étale two-torsion
algebra D. Simon's field version requires irreducibility. A finite
square-class space W must PROVABLY contain the global Kummer image,
including every imposed necessary norm/local restriction.
The standard Kummer inclusion and Mordell–Weil dimension formula
give the required certificate threshold

    dim_F2 W - dim_F2 E0(K)[2] <= 11.

The conservative sufficient threshold dim W<=11 needs no advance
torsion correction. Exact dimension four, Sha vanishing, equality
at omitted local conditions and global-point saturation are
unnecessary. This specifies a certificate; it does not produce W.

Arithmetic inputs would need full prime/model identification;
unconditional S-unit square-class coverage (odd unit index suffices);
S-class 2-torsion lifts or a proved larger covering space; norm/local
maps covering every such class; and exact linear algebra meeting the
threshold. A bounded unknown class contribution is acceptable only
with a proved bound for the missing square classes it permits.
Found elements give no coverage. Additional local tests inside an
uncertified global list cannot fix that defect. No class computation
is authorized by this comparison.

## Searches, failures and route

Queries included: `Schaefer Stoll How to do a p descent elliptic curve
number field upper bound class group 2 Selmer`; `elliptic curves number
fields 2 descent unconditional upper bound class group Selmer coarse
rank bound`; `Denis Simon Computing rank elliptic curves over number
fields 2002 pdf Selmer class group`; and `"2-descent" "upper bound"
"class group" unconditional Stoll`. Secondary results and unread
references are not inputs. No novelty is inferred from search.
The named primary passages were read, not the entire papers.

Duplicate/failure checks used L033, the two named ready assessments,
recent rank-related history, ATTEMPTS/013, and the named 96a1 class
arithmetic stops. No completed bare-unit diagnostic was found there.
The 96a1 degree-36 obstructions concern another field; they are not
transferred. ATTEMPTS/029–031 remain intact, and L068 is routing
evidence only. No cross-notebook input is used.

Park the closed narrow-class shortcut. Partial descent admits a weaker
certificate in principle, with the missing inputs listed above.
Before expensive arithmetic, test the unfiltered unit contribution
using the separate continuation assessment. If that alone prevents
meeting the threshold, park this simplification and require genuine
local constraints in any later certificate. A favorable diagnostic
still leaves all global coverage unverified. No new lemma, mathematical
script or rank derivation was made. Mathlib full matching and supporting
coverage: not checked.
