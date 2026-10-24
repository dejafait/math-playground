# Quantitative compression rate — separate audit coverage

TARGET: Critically audit L267's full matrix Green identification, all-offset squared-tail rate and complete L116 compression count for both actual probes.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-object/stronger-result queries recorded in 2026-10-23-transverse-h-quantitative-remainder.md and the production assessment; searched compression/transverse-H literature and histories for L267 and compression audits, read history/142, history/429 and ATTEMPTS/032. The original compression result is qualitative; no completed separate L267 audit was located in these scoped records.
SOURCE_EVIDENCE: Lawler--Limic, Random Walk: A Modern Introduction (Cambridge, 2010), author-hosted 289-page text https://www.math.uchicago.edu/~lawler/srwbook.pdf ; directly read section 1.1 printed pp. 9--11, section 4.2 (4.3)--(4.5) p. 77 and Proposition 4.2.3 with proof p. 79, Theorem 4.3.1 and essential proof cases pp. 81--83, and Corollary 4.3.3 p. 84 on 2026-10-23. Read L267, full L116, L110's definition/recurrence ranges and L118's statement and parity proof ranges for scope comparison only.
COMPARISON: The source covers the scalar Green asymptotic and Fourier representation for the applicable simple walk, including its bipartite case; it does not state the mixed matrix identification, all-offset squared-tail modulus or L116 trace bound. L267 claims O(N^(5/2)) for this one compression difference; L116 previously established only o(N^3). Independent checking of that specialization is the remaining audit task.
GAP: Verify L267's use of the imported scalar theorem, every signed mixed entry, small arguments, complete spatial/axial sums and both output selectors in L116's original finite trace count. Source adequacy gives no correctness verdict on these deductions.
REASON: The unchanged scalar source and exact local compression framework adequately cover one subsequent RESEARCH / REPRODUCTION proof audit of the exact TARGET; no new theorem, kernel estimate, changed boundary hypothesis or upstream re-audit is approved.
LITERATURE_REASON: The saved L267 critical-audit target was REVIEW_REQUIRED at invocation start; this separate comparison approves its precise source scope and failure tests, reusing production discovery coverage without repeating broad searches.
SCOPE: Both actual probes i=3,6, relative SU(2) cube, sufficiently fine admitted even N, a=8/N, tau=1/16, lower-rooted direction-1 forest, stored coordinates, bare-first order, both residual Q forms, levels/orientations, upper jump, all filters, both output selectors, all source/end rows, constant modes and full heat sums. All imported audit qualifications remain.

This separate literature turn approves the exact TARGET for the next
proof audit. It does not perform that audit or claim L267 has passed.

Essential inputs: L110, L116 and L118. L111/L113/L114/L115 are the
imported coefficient, stencil and heat-envelope premises used through
L116, and L124 fixes the comparison's place in the telescope. Preserve
all their unresolved audit qualifications. L109 is a contrast against
absolute first moments, not an obstruction to squared tails.

Review obligations: exact normalization of the simple-walk Green
kernel; Fourier/axial identification including j=0; the full signed
matrix in plane order 23,24,34, including all reverse mixed shifts;
the use of four pointwise O(|X|^-4) remainders rather than a derivative
of the remainder; small X; the complete spatial shell count and sum
over every signed integer axial offset; both original output selectors;
the outside a, N^2 trace factor and weighted N^2 level count; and the
original full heat sum for both actual probes. No fixed-j preview,
first absolute moment, compact output or finite relative scalar
Dirichlet replacement suffices.

## Primary input and limits

Use [Lawler--Limic, author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf#page=81).
Section 1.1 defines P_d as symmetric finite-range irreducible walks and
includes bipartite simple walk, with step probabilities 1/(2d) and
covariance I/d. Theorem 4.3.1 assumes p in P_d and d>=3 and states the
continuum Green leading term with uniform O(|x|^(-d)) remainder; its
simple-walk formula is explicit. The proof separates short, intermediate
and long times, using vanishing third moments and bounded increments.
Its periodic reduction uses (4.4)--(4.5), not an aperiodicity assumption
on simple walk. Proposition 4.2.3, p. 79, states the Fourier Green
representation, including parameter 1 for d>=3; its proof treats the
bipartite case via (4.3),(4.5). Corollary 4.3.3 states repeated-coordinate
second differences, not the required complete mixed matrix result.

Four-dimensional nearest-neighbor simple walk is within these exact
hypotheses. L267's L_4=8(I-P_rw) is the normalization to check, not a
different walk theorem. Proposition 4.2.3 supplies a direct citation for
its scalar Fourier representation; the positive-exponent convention
still must be matched to L110 using the scalar kernel's symmetry.
Its direct Abel argument may be retained for that convention and
normalization comparison, but no independent reproof of the source
asymptotic is needed. The source does not justify differentiating its
remainder or replacing a finite relative covariance by a scalar kernel.

## Local applicability and audit obligations

The full L116 read fixes which compression is meant. Its (9) keeps
both Q_1 and Q_2 defects; (10) defines the weighted Frobenius tail;
(11)--(15) state the complete row/trace/level estimates. L110 defines
the full-grid multiplier separately from the finite covariance and
checks the scalar axial recurrence at zero as well as nonzero offset.
L118 annihilates only the full-grid diagonal. These are inspected
canonical inputs, not conclusions verified by this source comparison.

| Object | Evidence available | Check left to the next mathematical audit |
| --- | --- | --- |
| Scalar identification | Source Theorem 4.3.1, Proposition 4.2.3; L267 section 1; L110 recurrence | Match the unnormalized Laplacian, all Fourier signs, Fubini/Abel justifications and j=0 without a bounded massless l2 inverse. |
| Complete matrix | L110 plane convention; L267 (8)--(9) | Independently multiply all nine entries, including every reverse mixed shift; test diagonal and off-diagonal orientations separately. |
| Pointwise bound | Source's uniform scalar remainder; L267 section 2 | Check the smooth leading-term difference and four separate remainder values; cover the finite set of small arguments. |
| Complete tails | L267 (11)--(12), L116 (10) | Check shell dimensions, squared spatial weight, constants uniform in j, square-root placement and the whole signed axial sum. |
| Compression count | L116 (9)--(15), L267 (13)--(14) | Retain both selectors and every omitted output; check the two Hilbert--Schmidt factors, outside a and weighted level count before the full heat sum. |
| Last consequence | L118 exact R_inf=0 | Use the existing zero comparison only; do not infer any of the four earlier placement rates. |

L111/L113/L114/L115 remain imported through L116; recursive inspection
of their entire arguments is outside this target. If the audit needs
a premise stronger than their stated allowance, report that mismatch
instead of inventing a replacement estimate. Both actual probe heat
envelopes must be matched to the common sufficiently fine threshold.

## Duplicates, failures and continuation decision

The parent assessment's four external queries and inspected-source
comparisons are reused unchanged. This turn adds the direct Fourier
proposition and a separate theorem-to-audit comparison, not a fresh
absence or novelty claim. History/142 records the qualitative rate;
history/429 records production and its pending audit, not an independent
verdict. L109 and ATTEMPTS/032 concern a separate factor's first absolute
moment; their obstruction remains, but does not prohibit testing this
circulation-sandwiched squared tail. Preserve all earlier stops.

Continue with exactly one proof_audit / REPRODUCTION step under SPECIALIZE.
Accept only if an independent reconstruction supports the stated
O(N^(5/2)) rate for both probes with every obligation above met.
A missing mixed entry, wrong normalization/count or uncontrolled
all-offset sum requires explicit repair or rejection of the affected
assertion. A newly needed estimate outside this audit's scope requires
separate coverage. This is source approval, not mathematical approval.

The main gap remains the interacting continuum construction, physical
observable sector, axioms and finite positive infrared mass. The audited
compression rate could remove one error from later quantitative
transverse-H assembly. Four independent coefficient remainders,
full quantitative L011 assembly and all construction gaps remain open.
Full matching and supporting Mathlib coverage is **not checked**, not
absent. No cross-notebook input is proposed. No lemmas, scripts, DAG or
PROOF changes are made. This literature-only comparison spends zero
mathematical exploration turns and establishes no new estimate.
