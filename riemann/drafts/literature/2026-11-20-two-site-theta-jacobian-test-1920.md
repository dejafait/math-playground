# Two-site degree-four Jacobian test — nomination1920

TARGET: Certify or refute nonzero Jacobian rank for (M_3/M_2^(3/2),M_4/M_2^2) of the degree-four monic orthogonal polynomial for (mu_0+delta_a+delta_b)/3 at (a,b)=(0,1), using the saved lambda=0 moment intervals under L917/L037 and no parameter sweep.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed review1919/1920 and drafts/literature/2026-11-20-two-site-theta-source-notes-1920.md contain exact/rank/range searches, local duplicate/failure comparisons and primary follow-ups. No matching two-observable rank theorem was inspected; no originality claim.
SOURCE_EVIDENCE: Import Delgado--Fernandez--Perez--Pinar,SIGMA12(2016),090,arXiv:1601.07194v2,Theorem3.1,Section3 pp8-10,https://arxiv.org/pdf/1601.07194v2 (complete proof read1908); Gautschi,Orthogonal Polynomials: Computation and Approximation,OUP2004,Theorem2.1,(2.1.1)-(2.1.3),pp52-54,statement/full proof read1920,primary link in source-notes1920; reuse DLMF18.2(i)/(vi) mixed-measure/simple-zero coverage. L917/audit197 and L037 supply conditional saved moment inputs.
COMPARISON: Known finite coefficient formulas cover reference construction, not the standardized empirical moment-map determinant. C028q covers the empirical/affine convention; C028r/s supplies only one-site scalar matching. Exterior or disputed unrestricted monotonicity cannot replace this two-observable determinant.
GAP: Compute and rigorously enclose the fixed Jacobian with complete centering and normalization derivatives; certify all divisions. No reference rank, actual-target inclusion, quartic matching or full-cost bound is established. A conventional specialization and finite calculation.
REASON: A single diagnostic can determine whether independent local invariant directions exist at the chosen degree/site pair. It may justify later assessed matching work; success leaves actual inclusion and uniform cost unpaid. Newly written ready continuation: separate next-turn approval is required before mathematics.
SCOPE: Exactly d=4,(a,b)=(0,1),positive unit masses,full theta mu_0,empirical moments divided by4; saved lambda=0 boxes with exact odd base moments0 and inherited arithmetic hypotheses. No quadrature, sweep, changed masses, general-d rank claim, actual-root reality or global range claim.

Source detail and exclusions are in
[source-notes1920](2026-11-20-two-site-theta-source-notes-1920.md).
The main gap is L030-L032/C032a/C028b; the prospective use is an extra
quartic adjustment after affine normalization. This is a feasibility
test, not an improvement of the notebook's known finite positivity.

Use L019/L021 and C028q to identify the probability measure and equally
weighted reference zeros. Read full selected panel0 endpoints and
provenance from scripts/heat/low-time-h2-uniform-195.json with bounded
../scripts/loop/inspect_json.py requests; retain L917/audit197 and L037's
library assumptions. Required base half-line inputs are M_0,M_2,M_4,M_6
at lambda=0. Normalize by the enclosed positive M_0; do not insert
gamma_j or Taylor-factorial moments into the Gram system. Gautschi's
degree-four formula uses mixed orders0,...,7; base odd moments vanish
exactly but mixed odd moments generally do not.

Import the known formula rather than reprove it. Derive only the finite
coefficient/Jacobian specialization after approval. A certificate must
identify the polynomial, observables, all differentiated terms, exact
arithmetic or outward enclosures and every required positive denominator.
Analytic positivity of Gram determinant and reference variance does not
license dividing by a zero-containing numerical box. Retain centering
and empirical divisions by4, and distinguish reflection's cubic effect
from the quartic invariant. Use full certificates, not previews, for rank.

Require an enclosure strictly excluding zero for the determinant, or
exact structural degeneracy. If zero remains in the fixed enclosure,
report an inconclusive result and stop without a parameter sweep or
automatic moment refinement. Actual image inclusion, matching, full
Schmeisser cost and H_d=o(d) remain separate obligations. Reference
reality does not prove actual-root reality. Full matching Mathlib
coverage is unchecked.
