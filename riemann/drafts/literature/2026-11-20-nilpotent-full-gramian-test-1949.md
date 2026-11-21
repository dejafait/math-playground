# Full-cost nilpotent diagnostic1949 — source review1950

TARGET: Determine whether the full trace-norm defect for the d-by-d nilpotent unit subdiagonal shift, using assessment1947's realified Gramian and T_d=d^2, tends to zero or has a positive liminf.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1950 searched nilpotent/Jordan finite-horizon Gramians, integrator/Hilbert moments, full trace/Schatten costs and polynomial/Sobolev differentiation; scoped notebook searches found no exact diagnostic duplicate. Queries, inspected cases and exclusions are recorded in drafts/literature/2026-11-20-nilpotent-full-gramian-source-notes-1950.md; no novelty is inferred.
SOURCE_EVIDENCE: Reuse assessment1947/source-notes1947 and C029b for finite positivity, endpoint and norm inputs; newly inspect Stillfjord-Tronarp BIT66(2026)65 Sections1 (2a-b),(4b),(5) and7 Experiment0 https://doi.org/10.1007/s10543-026-01160-6 ; Shadrin-Nikolov-Aleksov arXiv1510.03265v1 Theorem1.1 p2, (2.1)-(2.3) p3 and even/odd proof cases p7 https://arxiv.org/pdf/1510.03265v1 ; Alvandi-Watt2019 SectionsII (1) p2 andIII.A Theorem2/full proof pp3-4 https://cs.uwaterloo.ca/~smwatt/pub/reprints/2019-synasc-ls-matrix-rep.pdf .
COMPARISON: The inspected nilpotent example uses the exact unit subdiagonal shift with single input e_1 and a Legendre factorization, not the identity-observation realified principal block. The polynomial theorem bounds a largest singular value in scalar weighted L2; the Sobolev differentiation theorem uses only orders0,1. None evaluates the exact full Hermitian-imaginary trace norm here. C028h/i/o/p and C029a have different operators or restricted metrics; attempts1948/1949 remain inconclusive actual-family tests.
GAP: Determine the increasing-dimension full k_d(S) at the fixed horizon d^2. Any polynomial-moment representation, phase/parity handling, comparison of all observation channels, inverse-metric estimate and full-norm asymptotic must be justified in the research attempt; no scalar leading-channel substitution or fixed-d large-time limit is approved as an answer.
REASON: This separate literature turn completes the proposed diagnostic's source gate. The known finite constructions are available, no essential source is blocked, and the bounded search found no result answering the full statistic. One mathematical attempt on the unchanged target is justified; this review establishes no vanishing estimate, floor or actual-family transfer.
SCOPE: Integers d>=3; S_d e_j=e_(j+1) for j<d and S_d e_d=0; replace C_d by S_d in the realified Gramian and full J_d,k_d of C029b, with T_d=d^2. No change of horizon, actual-Xi identification, spectral-fitting metric or terminal-three substitution is allowed.

## Exact proposed diagnostic and downstream use

Use the specified nilpotent shift S_d, not the actual centered
companion. Define M_d=[0 -S_d; S_d 0], W_d as the same integral
from 0 to d^2, and G_d as its upper-left block divided by d^2.
The proposed statistic is exactly

    k_d(S)=||(G_d^(1/2)*S_d*G_d^(-1/2)
                   -G_d^(-1/2)*S_d^T*G_d^(1/2))/(2i)||_1.

This is the assessed test definition, not an evaluated expression.
The finite-horizon positivity input is already identified; the missing
coverage concerns the full, increasing-dimension norm and its scale.
Review1950 inspected the relevant finite-Gramian and polynomial
results and compared local recorded stops, as detailed in the source
notes. Their hypotheses do not supply the requested asymptotic.

The discriminating alternatives are k_d(S)->0 or liminf k_d(S)>0
at this one horizon. A positive floor would show that real spectrum
alone is insufficient for this proposed full-cost schedule. It would
not establish a floor for the actual companion or refute RH. Vanishing
would remove only this model obstruction, leaving the actual spectrum,
all-coefficient energy estimates, k_d=o(1), and C028b's H_d=o(d) open.
If a known result already answers the exact diagnostic, import it and
state the applicability instead of reproving it. If it duplicates a
recorded stop without a new implication, do not approve a repetition.

Continuation inputs are C029b's definitions/scale, assessment1947's
finite-horizon and norm inputs, and source-notes1950's inspected
nilpotent/polynomial comparisons; C028b explains relevance only.
C028h's actual coefficients and its diagonal floor are contrasts,
not premises for the shift model. No assumption of uniformly bounded
conditioning, a small commutator, or transfer from the model to Xi is
permitted. Mathlib coverage for the proposed full result is unchecked.

## Approved attempt and limits

After this source-review turn, attempt exactly the displayed full-cost
diagnostic with every degree and observation coordinate retained. The
two discriminating sufficient outcomes are an analytic o(1) upper
bound or a fixed positive lower bound eventually. These alternatives
are not asserted exhaustive for an arbitrary sequence: if neither is
established, retain the unresolved estimate or other behavior honestly.
The finite polynomial structure is a possible means of analysis, not
an established isometry or a requirement to use any particular basis.
An implementation would require its own relevant exact/error evidence;
the source's floating-point plots do not certify this statistic.
This approves exploration, not a reproof of cited general inputs.
