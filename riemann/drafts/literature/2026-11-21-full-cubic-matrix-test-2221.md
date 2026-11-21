# Full cubic matrix: fixed calculation coverage2221

TARGET: Test whether actual-Xi H_(3,r)=(S_(2r+i+j+2))_(0<=i,j<=3)>0 for every integer r>=4 using one four-node inverse-Frobenius enclosure over the three C919f time-zero boxes and C919k's band(100,200], scaling D=diag(1,200,40000,8000000), the complete real head through1000 and a complete exterior matrix bound; stop if the frozen margin or every-r comparison fails, without tuning.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review2221 searched exact shifted reciprocal-zero Hankel/four-node/full-cubic and stronger finite-positivity terms, compared C919e/f/h/k, C030b and recorded failures2146/2061/L057; no matching completed certificate was found in the scoped records, without an originality claim. Full queries/read limits: 2026-11-21-full-cubic-source-notes-2221.md.
SOURCE_EVIDENCE: Gautschi1975 Section3(3.1)-(3.4) p339/Section4(4.1)-(4.1') p340, https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf ; Boyd-Vandenberghe2004 A.1.1/A.1.5/A.5.2/A.5.4 pp633-636,646-649, https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf ; reuse2216/2218 Platt2017 Theorem5.1 pp6-8 completeness coverage, https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf , and Bellotti-Wong2412.15470v2 Theorem1.1/Section5 pp1,23-24, https://arxiv.org/pdf/2412.15470v2 ; accepted C919f/h/k and L467. Stronger-result comparisons/read limits are in notes2221.
COMPARISON: General finite distinct-node inversion and real Gram/SVD methods cover size4. C919h covers all quadratic coefficients and C919k one cubic ray; neither signs the full cubic cross terms. C030b covers only bounded total polynomial degree relative to its preprint input. Bickel-Pascoe-Sargent assumes rather than proves an actual Hankel positivity class. No cited theorem supplies this frozen every-shift matrix margin.
GAP: Derive the four-node normalization and a uniform rational lower bound with the actual r=4 weights; bound every complex exterior component in the same scaling; prove strict head dominance and every larger shift. None has been calculated here. Source computations and C919f backend assumptions remain imported.
REASON: The accepted separated counted band supplies the fourth node absent from the annihilated three-node core. This permits one independently testable fixed-degree calculation with ready general methods; it is REPRODUCTION, not a creative degree-uniform mechanism or RH candidate.
SCOPE: Exactly TARGET. New ready continuation prepared in literature-only2221, subject to separate supervisor approval next turn. No mathematics performed during this approval preparation. No parameter sweep, subdivision, extra zero table, heat-time extension, arbitrary-degree claim or shift removal.

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. Success here would control all real cubic coefficient
vectors in X^r p, deg p<=3, r>=4, including cross terms absent from
the accepted ray. Other degrees and removal of X^r remain unresolved.

Essential local inputs: L018/L024/L025/L030/L058/L467, accepted
C919f/C919k. C919e/C919h provide assessed methods and overlap only;
their size3 constants do not apply to size4. No cross-notebook input.
Use one occurrence in each time-zero box and one count-certified
occurrence in(100,200]; their closed enclosures for the uniform test
are [14,29/2], [41/2,43/2], [49/2,51/2], [100,200]. No ordered
census, uniqueness in a box or exact fourth ordinate is assumed.

Use the finite Lagrange-inverse formula by citation; the reason for
specialization is the changed dimension, weights and broad fourth
interval, not a need to reprove the general theorem. A single rational
inverse-entry/Frobenius enclosure must pay all pairwise denominators
and the onset weights. Retain the prescribed scaling throughout.
Do not identify infinity and Euclidean norms or use a determinant
alone as a quantitative least-eigenvalue bound.

Keep every positive-ordinate occurrence through1000 in the real head,
including the endpoint, using Platt2017. Retain every multiplicity and
both positive-real-part conjugate occurrences outside it. L024 excludes
the origin with the same zero-ordinate argument as C919k. Use L030's
absolutely convergent algebraic squares and ordinary transpose, not
a Hermitian replacement. A complete exterior estimate must include
all unit shells above1000 using L467, with a summable majorant and
every scaled component; no exterior-reality assumption is permitted.

Continuation test: a rigorous h4>t4 in this single scaling at r=4,
plus the complete matrix comparison for every integer r>=4. The
height separation is available but its matrix use must be justified,
not inferred from the accepted scalar-ray certificate. If this one
enclosure fails, an occurrence/endpoint is uncovered or the uniform
comparison is unpaid, preserve the precise defect and stop without
tuning. Failure is not a disproof of positivity or RH.

Retain C919f's correct CPython integer/Fraction and Decimal/libmpdec
contracts, including correctly rounded HALF_EVEN exp, and the imported
source computations. A later exact certificate must store full rational
operands, inverse bounds, actual/required margin, all-r factors and
failures. Display approximations prove nothing. No source computation
or accepted witness needs rerunning. Full matching Mathlib coverage
is unchecked. Recommended task: calculation, standard/high.
