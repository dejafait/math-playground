# Proposed full-strip large-gap comparison for consecutive empty cells

TARGET: Assess whether unconditional large-gap results force arbitrarily late pairs of consecutive complete response cells containing no full-strip zero ordinate.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded full-strip/critical-line gap and consecutive-empty-Gram searches on 2026-10-10 located STTB, Zhao, Bredberg and Bui–Milinovich; reused adjacent-grid coverage and L379/L383 failure records; primary statements and relevant reduction cases inspected below.
SOURCE_EVIDENCE: STTB arXiv:2010.10675v1 Theorem 1 pp. 1–2 and full large-gap reduction §2.1 pp. 4–6; Zhao arXiv:2603.17334v1 definitions pp. 1–2, Theorems 1–3 p. 3 and full gap reduction §2.1 pp. 4–5; Bredberg arXiv:1101.3197v3 Theorem 1/Remark 1 p. 1 and critical-line product/Wirtinger cases pp. 2–3; Bui–Milinovich accepted manuscript Theorem 1.1 p. 1 and §2.2 pp. 3–4; Saker arXiv:0906.5458v3 Theorem 2.1/full proof pp. 7–8.
COMPARISON: The inspected unconditional full-strip guarantees exceed one mean spacing only slightly; larger 2.766 and 3.18 guarantees concern critical-line zeros. None supplies two empty complete actual response cells with variable-grid placement.
GAP: Consecutive actual-cell emptiness remains unproved; no inspected theorem reaches the two-cell span and supplies placement without RH, and r-gap results for r>1 allow intervening ordinates.
REASON: Park the direct large-gap import on a documented size/count/placement mismatch; the bounded review gives new negative applicability evidence, not a disproof of the occupancy target or a new gap theorem.
LITERATURE_REASON: The changed target requires two consecutive empty actual response cells, beyond the single-cell occupancy and ordinary-grid results previously assessed.
SCOPE: Fixed actual G from L366/L368, its eventual consecutive simple zeros from L372, full-strip zeta zeros with all multiplicities, no RH or common-zero premise; pairs lie in arbitrarily high dyadic intervals.

The bounded comparison is complete; the proposed direct import is parked.
No suitable-gap assertion or ready application follows. Essential inputs
for the comparison are L384, L366, L368 and L372. The main gaps remain global
mixed positivity and the total L367 margin. Its possible downstream use
is endpoint control for a cell contained within a longer zero-free
interval, followed by a separately justified sign/Wronskian application.
Neither implication is established in this proposal.

## Original review plan (retained; completed verdict below)

Reuse the inspected source distinctions in
`drafts/literature/2026-10-08-adjacent-response-grid-signs.md` and
`drafts/literature/2026-10-10-variable-response-cell-occupancy.md`.
Search specifically for unconditional gaps between all distinct strip
ordinates, exact normalization and grid-placement requirements, stronger
occupancy results, and relevant obstructions. Separate results about
critical-line zeros, RH-conditional total gaps and constant-angle grids.
An average empty-cell proportion does not itself assert adjacency.

Continue only if a precisely cited theorem supplies a sufficient gap or
occupancy condition with justified variable-grid placement, or an explicit
bounded specialization whose essential inputs have been inspected. If
the sources cover only critical-line gaps, inadequate gap sizes or no
placement information, record the mismatch and park that import. Do not
retry the L379 absolute triangle certificate or L383 fixed correlation.
No large-gap numerical evidence, theorem application, new lemma or
mathematical script has been produced. Mathlib coverage is not checked.

## Completed primary comparison — 2026-10-10

This is LITERATURE / NOVELTY_UNCHECKED / NEGATIVE: the new evidence
parks the proposed import. It neither proves nor refutes TARGET.

**Full-strip results.** Simonič, Trudgian and Turnage-Butterbaugh,
*Some explicit and unconditional results on gaps between zeroes of the
Riemann zeta-function*, [arXiv:2010.10675v1](https://arxiv.org/pdf/2010.10675v1),
20 October 2020, Theorem 1, use all positive strip ordinates and normalized
gaps (gamma_(n+1)-gamma_n)/(2pi/log gamma_n). Their admissible large-gap
parameter is lambda<1+c_0, with
c_0=pi exp(4.3)/exp(exp(30.76)). Section 2.1's complete reduction obtains
positive measure of zero-free sliding windows only below its stated
threshold, then uses a second gap moment to obtain positive proportion.
It does not locate windows on this response grid. The later publication
is *Trans. Amer. Math. Soc.* 375 (2022), 3239–3265,
DOI 10.1090/tran/8571; the exact statement inspected here is v1.

Tianyu Zhao, *Density results for r-gaps between zeros of the Riemann
zeta-function*, [arXiv:2603.17334v1](https://arxiv.org/pdf/2603.17334v1),
18 March 2026, Theorems 1–2, improves the unconditional positive-proportion
bound to 1+9.23·10^(-7)/r^(2/3). At r=1 this remains below the two-cell
scale. The larger 0.01625 constant is restricted to sufficiently large r;
gamma_(n+r)-gamma_n then spans intervening ordinates, rather than a
zero-free gap. The complete §2.1 reduction counts such r-spans and gives
no response-grid placement. Its N convention half-weights an ordinate
at the endpoint, unlike L384's right-continuous count. No endpoint transfer
is attempted. Theorem 3 concerns signed S increments, not an assertion
of zero-free windows at arbitrary prescribed lengths. The remaining
high-moment proof and §6 numerical optimization were not independently
audited; no constant or theorem is imported into the canonical argument.

**Larger critical-line guarantees.** Bredberg,
[arXiv:1101.3197v3](https://arxiv.org/pdf/1101.3197v3), 16 June 2011,
Theorem 1 gives a critical-line-zero-free interval of length at least
2.766·2pi/log T in every sufficiently high [T,2T]. Remark 1 explicitly
requires RH to turn it into a full-strip gap conclusion. Its product and
Wirtinger argument concerns values of zeta on Re s=1/2 and their imaginary
shifts; no off-line exclusion is present.

Bui and Milinovich, *Gaps between zeros of the Riemann zeta-function*,
*Q. J. Math.* 69(2) (2018), 403–423, DOI 10.1093/qmath/hax047,
[accepted manuscript](https://pure.manchester.ac.uk/ws/portalfiles/portal/76260311/QJM_submitted.pdf),
printed p. 1, Theorem 1.1, distinguish the multiplicity-repeated critical-line
sequence t_n from all-strip gamma_n: Lambda>3.18 is unconditional,
lambda>3.18 assumes RH. The full §2.2 reduction uses critical-line products
and endpoint Wirtinger inequalities. Larger gaps for multiple critical-line
zeros in Theorem 1.2 do not exclude simple or off-line zeros. No grid
placement statement for G is supplied; no numerical optimization is rerun.

Saker's [arXiv:0906.5458v3](https://arxiv.org/pdf/0906.5458v3),
22 June 2010, has an abstract suggesting an unconditional all-zero result.
The actual Theorem 2.1 and full proof, printed pp. 7–8, use zeros of Hardy
Z(t) and fourth moments. This does not supply full-strip emptiness. Its
constants and wider claims are not audited or imported here.

## Applicability verdict and route boundary

The exact requested pair is (g_j,g_(j+1)] and (g_(j+1),g_(j+2)], both
complete. Its zero-free union must span **two** full phase increments pi.
L372's existing phi'=one-half log(t/(2pi))+O(1) identifies the two-cell
scale as twice the local mean spacing. The inspected r=1 all-strip lower
guarantees do not reach that scale. Moreover, the grid offset beta+eta is
variable, and none of these sources controls where a gap begins relative
to its levels. No sufficient placement threshold is proved in this review.
Critical-line gaps could still contain off-line ordinates. Enlarging r
changes the count problem, rather than furnishing an empty interval.
Positive-proportion single empty cells in L384 do not assert adjacency.
These are statement comparisons, not counterexamples to TARGET.

The existing L379 absolute enclosure and L383 correlation stops remain
unchanged; no duplicate specialization was found in the named local
assessments/failure records. No literature-wide nonexistence or novelty
claim follows. Searches included `unconditional large gaps between zeros
Riemann zeta all zeros ordinates`, `Simonic Trudgian Turnage Butterbaugh
unconditional gaps zeros`, `consecutive empty Gram intervals theorem zeta`,
`unconditional gaps all zeros zeta 2026`, and `zeta large gaps 3.18
unconditional`. Other search hits are unread leads, not inputs.

Park this import unless a materially stronger full-strip gap with adequate
placement, or a direct consecutive-occupancy theorem, is supplied. The
separate proposed continuation in
`drafts/literature/2026-10-10-empty-cell-common-zero-charging.md` instead
asks about conditional endpoint counting using existing empty cells; it
is REVIEW_REQUIRED and has not been proved or approved here. All stated
global positivity, total-margin and localization gaps remain open. Full
matching Mathlib coverage remains not checked.
