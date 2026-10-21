# Entire modular-map reduction at thirteen — proposed specialization

TARGET: Certify good reduction at thirteen of L034's entire modular map j:E0 -> P1, retaining both x=16 charts and its pole at O.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed fixed-class elliptic-Chabauty comparison; its primary searches found the general rationality method and same-field FNS treatment, but no inspected complete chart certificate for this exact reduction target.
SOURCE_EVIDENCE: Bruin 2003 Section 4.2 pp.42–45 and Lemma 4.1 with both proof cases; official Magma handbook text/1568 prime-specific map-reduction requirement; L033 integral models, L034 complete modular formula/pole analysis and audited L064 entire unramified thirteen-adic field inspected.
COMPARISON: The known method requires curve and map reduction beyond L064's matching of two particular fibers; the missing specialization is an entire-map certificate at thirteen, not a new Chabauty theorem or local connecting-class enumeration.
GAP: Prove extension of j on every chart of the smooth integral curve and nonconstant degree-twelve reduction, with no simultaneous zero/pole gap; no such certificate is assumed here.
REASON: This finite prerequisite has exact local inputs and is independently testable before expensive rank/index calculations; success would serve the global rational-j point mechanism.
SCOPE: Only the original degree-twelve map over the entire unramified field at thirteen; no translated-isogeny reduction, global rank, finite-index subgroup, zero bound or point classification is approved.

This newly written continuation requires separate approval before
mathematics. No reduction computation or new mathematical conclusion
was made in preparing it. The completed literature result is in
[the fixed-class assessment](2026-10-14-fixed-class-elliptic-chabauty-scope.md).

The main gap remains positive primitive integer emptiness in the 54a1
branch. The intermediate target is the map-reduction certificate
required by the general rationality method. Its plausible downstream
use is choosing thirteen for a later coset-wise global Chabauty test,
once rank/index information and expansions are independently available.
It is independent of the stopped finite-prime removal of alpha_sigma.

Primary citations: Nils Bruin, *Chabauty methods using elliptic curves*,
J. reine angew. Math. **562** (2003), 27–49,
[DOI](https://doi.org/10.1515/crll.2003.076),
[published author copy](https://www.cecm.sfu.ca/~nbruin/bruin_crelle.pdf),
Section 4.2, pp.42–45. His large field L is our K and his smaller
field is Q. His requirement that the reduced map remain a cover is
the needed input; Section 4.1 degree-two formulas are not used.
The [official Magma handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/1568),
“Elliptic Curve Chabauty,” prime-specific intrinsic, accessed 2026-10-14,
also requires good curve and map reduction at every prime above p.
Neither source supplies our certificate or guarantees a finite bound
from rank alone. Software availability is not assumed.

Essential inputs: L033 for E0 and torsion points; L034 for the complete
formula, exceptional charts, pole divisor and source comparison; L064
for the entire unramified degree-twelve local field. L062 fixes sigma
if the canonical point is used. Its class need not be expressed in a
global unit basis. Reuse L034's exact source coefficients; good curve
reduction or two separable fibers do not prove good map reduction.
Any supporting theorem outside this explicit chart specialization
requires additional coverage.

Continue if every chart, including removable 2T, the order-eleven pole
at 3T and the pole at O, extends and the reduced map has degree exactly
twelve. Keep complete residuals/valuations and any arithmetic certificate
on disk. Abandon this prime if a genuine base point, degree loss or
inseparability obstructs the required reduction; preserve the defect.
A failed affine quotient expression alone is not such a defect because
L034 has a removable chart. No higher-prime search belongs to this target.

Unresolved after success: unconditional rank below twelve, enough global
points or adequate formal-kernel index control, exact rationality
expansions and coset-wise zero tests, translated theta-covering reduction,
other-class exhaustion and common primitive rational/integer power
lifting. FNS's conditional 2-Selmer dimension cannot replace these.
Full matching and supporting Mathlib coverage is not checked; unknown
is not absence. No cross-notebook input is used.
