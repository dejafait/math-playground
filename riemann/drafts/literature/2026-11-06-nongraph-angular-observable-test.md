# Non-graph filling — finite angular-observable test

TARGET: Test whether the tangent-normalized first angular observable separates L856's prescribed collar periods from every smooth annular filling with nonnegative real full density and positive original angular projection in the unchanged chart.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed 2026-11-06-nongraph-annular-filling-scope.md records bounded prescribed-boundary, holomorphic-form and angular-projection searches and scoped duplicate/failure comparison. No inspected source settles this fixed observable test; search failure establishes no novelty.
SOURCE_EVIDENCE: Reuse that assessment's inspected Lebl SCV v4.4 TheoremC.6/proof p224 and Theorem1.2.1/proof pp20-21, https://www.jirka.org/scv/scv.pdf ; reuse Lebl Basic Analysis I v6.3 Theorem7.5.6 p290/Lemma4.2.2 pp162-163 and Basic Analysis II Theorem8.3.7 p38 from 2026-11-06-actual-g-real-zero-interval-stationarity.md; reuse L856's positive-integration coverage. Haskins-Pacini Definition4.2/Theorems4.6,5.4 are comparisons, not filling inputs.
COMPARISON: Stokes, compact extrema, Fermat, chain rule, joint primitives and positive integration cover the tools only. The difference is one fixed angular observable on a surface whose w projection may fold or leave the planar annulus. No general filling or new maximum-principle theorem is proposed.
GAP: Verify the angular extremum constraint and ambient primitives on all of B, compute the prescribed boundary integrals with signs, and compare their normalized value with boundary extrema with justified fixed-n small-radius errors. No strict violation is established.
REASON: This bounded known-tool specialization uses a projection constraint absent from the completed graph test. This newly written assessment requires separate supervisor approval before a mathematical attempt.
SCOPE: Exactly TARGET; fixed actual-G pair, finite n>=1, fixed B/logarithm branches, exact L856 collars/orientations, smooth compact embedded annulus, nonnegative real full form including zeros, strictly positive original angular two-form. No higher moments, shrinking of the candidate surface's chart, or global contour claim.

## Fixed test and threshold — not a proved result

Use L855/L856, with actual G and the full form inherited from L775/L847:
zeta eta!=0, G(zeta)=0 of fixed finite multiplicity n>=1,
G(eta)(zeta-eta)!=0. Let theta^0 be the fixed angle lifts at the base
pair. Write 1/zeta=p+it and use the already proved tangent

\[
 T=\begin{pmatrix}t&p\\-p&t\end{pmatrix}
\]

from L855(9)/L856(13). Fix only the real linear observable

\[
 \ell(\Theta)=(1,0)T^{-1}(\Theta-\theta^0).
\]

Compare its full-form-weighted integral, normalized by the positive
L856 total boundary period M_0, against its extrema on the two prescribed
boundary circles. Seek a rigorous strict violation for every sufficiently
small r, with constants allowed to depend on the fixed pair, chart and n.
Do not assume its weighted integral equals a planar w moment.

The mathematical attempt must check all these obligations together:

- Apply compact extrema and positive angular two-form to this nonzero
  linear observable on a hypothetical filling, even at zeros of the
  full form and folds of the w projection.
- Justify smooth ambient primitives for the required weighted forms
  throughout the original B using the fixed holomorphic logarithms
  and original product neighborhood. A primitive only near the collars
  or in a smaller chart does not suffice. Restrictions of logarithms
  to the real surface are not assumed holomorphic in a surface parameter.
- Compute the complete boundary integrals with induced orientations,
  exact L856 collars and the Laurent term. Bound all integrated errors
  below M_0 times the proposed separation; absolute o(1) is insufficient
  because M_0 tends to zero.

Continue only with a controlled strict violation. A successful estimate
excludes this specific filling class, not all compatible collars or
actual Xi contours. If the observable is compatible, primitives fail on
the whole B, or errors are unpaid, record the outcome and park this test.
Do not escalate to higher moments, replace the collars or infer existence
from passing a necessary test. No separation coefficient or new result
is derived in this assessment.

## Relevance, source reuse and Mathlib

This may close the projection-class escape left by graph-only L856.
Actual matching, global homology, exchange, other orders and the
L030-L032/C032a positivity gap remain open. It is a known-tool
specialization, not a protected creative RH mechanism; actual exterior
data and a tested link to signs remain missing.

Use the completed parent assessment for precise sources, hypotheses and
proof-case coverage. After approval no new search is needed while this
target stays unchanged. Full matching Mathlib coverage is unchecked.
Supporting `IsLocalMax.hasFDerivAt_eq_zero` was inspected in the official
[LocalExtr.Basic documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Basic.html#IsLocalMax.hasFDerivAt_eq_zero);
it supplies only the coordinate Fermat input. No cross-notebook input.
