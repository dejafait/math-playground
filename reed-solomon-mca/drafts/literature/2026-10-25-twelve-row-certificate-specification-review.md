# Twelve-row certificate specification — proposed ready continuation

TARGET: Construct and audit a finite-field certificate specification for twelve compatible rows over L153's complete pair registry, retaining L109's gates and L086's incidence constraints, and count its size without running a solver.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-domain, duplicate, stronger-result and failure comparison in 2026-10-25-twelve-row-gated-feasibility-review.md, step 475; its exact searches and source proof cases cover finite-field formula construction, not the local encoding. L123 already completes L122's three-plane capacity test; ATTEMPTS/041–043 and /048 remain stopped at their stated scope.
SOURCE_EVIDENCE: Gao–Platzer–Clarke, CAI 2011, LNCS 6742, pp. 140–157, DOI 10.1007/978-3-642-21493-6_9, Theorems 2.2/3.1/3.2/4.1/5.1/5.2 and Lemmas 4.1/4.2, https://symbolaris.com/pub/QEfin.pdf ; reuse L109's imported Hall Theorem 5.1.1 pp. 63–64 https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf , Marquez-Corbella–Pellikaan 2016-02-29 section 5 pp. 7–8 https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf , Conrad Theorems 4.2/7.1/7.5 https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf ; exact applicability and source limitations are in the completed comparison.
COMPARISON: Known finite-field formula flattening supplies the general certificate machinery; L109 already supplies the mathematical row gates. What is missing is the explicitly audited simultaneous row-selection/certificate contract and its size. No inspected theorem supplies a twelve-row obstruction or proves this encoding practical; no general algebraic theorem needs reproof.
GAP: Justify complete arbitrary-pair and twelve-row selection on one common plane, every projective/projection/weight/original-chart branch and the field of all variables; quantify the proposed encoding's size before any solver attempt.
REASON: A bounded RESEARCH/REPRODUCTION specification attempt is source-ready, subject to separate supervisor approval next turn. This literature turn has not constructed or certified an encoding, derived a new result, written a mathematical script or authorized feasibility solving.
SCOPE: Exactly TARGET under the fixed represented t=0 hypotheses below; specification, mathematical audit and size bookkeeping only. No pair sweep, new solver run, generic-Schubert exclusion, prime-field point census, old-locus transfer or assertion of twelve/sixteen-event feasibility.

## Inputs and mathematical use

Essential inputs are L153's complete pair registry and complete kernels,
L109's original blocks, all-rank Plucker reconstruction, exact projection,
full-weight and prescribed-chart gates, L086's incidence restrictions,
and C152a through L086/L152 for relevance of some registered actual pair.
L104 supplies local survivors; L151 supplies only its labeled exclusion.
No numerical pair is assumed universally present. Read only the kernel
records actually needed for a specification or regression; no complete
certificate sweep is needed merely to state the input contract.

Retain F=F_(97^20), H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
S={1,8,12,18,22,27,33}, k=8, the pinned 1/4<=delta<5/16 cell,
coefficient syndromes in U_S, actual nonzero D and locators, sixteen
original finite events, t=0, arbitrary weights and prescribed original
chart, and inherited L056/L069/L040 finite-certificate qualifications.
Universal representation and challenge identification remain unresolved.

The main gap is uniform compatibility for an arbitrary extracted pair.
This intermediate specification could make a later exact certificate
attempt reviewable, or expose a decisive size/branch-coverage obstacle
before implementation. An equivalent finite criterion does not close
that mathematical gap or improve 11/q–16/q. A compatible selected family
does not establish t=0, the remaining events or challenge equivalence.

## Bounded work and acceptance conditions

Specify a finite formula and an independently checkable certificate
contract. Establish the necessary inclusion of every original equality
configuration, and state exactly which selected-row recoveries a satisfying
assignment would certify. In particular justify selecting twelve rows
while retaining an extracted pair, the row universe and distinctness,
pairwise intersections at most one and degrees at most four. Preserve
all original labels; no unproved H-permutation symmetry is available.

Audit one common nonzero decomposable plane in the appropriate complete
pair kernel, all projective charts and every projection pivot branch.
Keep rank-zero rejection under its actual nonpersistence hypothesis,
nonzero lambda, both overlap weights and the prescribed original finite
direction gates. Explain how basis changes retain an arbitrary chart;
do not quietly replace it by a convenient rational chart. Any discrete
selection/cardinality encoding needs an exact-integer interpretation,
not an unexplained equality modulo 97. These are proof obligations for
the later attempt, not an encoding or lemma established by this review.

Import the known finite-field method at q=97^20. If using a different
field representation, justify its equivalence rather than restricting
unknowns to F_97. Distinguish an all-extension unit-ideal certificate
from prescribed-field satisfiability, and exact polynomial identities
from truncated reductions. The source's auxiliary disjunction variables
are not automatically Boolean selectors; preserve its stated semantics.
No cost guarantee or installed/licensed software is assumed.

Count the specified variables, generators/logical constraints, maximum
degrees and pair/chart branches, making clear whether any representation
is a circuit or expanded polynomial list. Save the full proposed contract,
its proof/audit and size derivation in a notebook draft, with unresolved
assumptions explicit. Do not create a lemma just to package an equivalent
criterion. Any original load-bearing mathematical result would require
its own canonical proof under the shared rules.

Continue only after a complete, source-justified specification and its
actual size make a bounded subsequent test concrete. If any necessary
branch is lost, or the proposed size cannot be controlled, preserve the
first exact defect/obstruction and abandon that encoding rather than run
an unrestricted solver. Failure or a size estimate is not an exclusion.
No full feasibility computation is included in this action. Full matching
Mathlib coverage is not checked. This new ready continuation receives
separate approval next turn before the research attempt.
