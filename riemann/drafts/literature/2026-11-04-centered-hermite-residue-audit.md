# Centered Hermite residue obstruction — audit source assessment

TARGET: Audit L764's Laurent/residue argument and actual-theta certificate, including the uniform threshold d>=max{6,ceil(12000000a)}.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step383 reused step381's exact fixed-a residue/interlacing comparison and checked the local grid stop, L764 and the script's rounding interface; a bounded exact centered/Jensen/Hermite/residue search gave no inspected replacement for L764. New primary-source reads cover Simpson error and Decimal semantics, not actual coefficient signs.
SOURCE_EVIDENCE: Reused Fisk arXiv:math/0612833v2 Section1.3 Lemma1.20(3), printed pp.12–14, and DLMF18.2(vi)/18.9.1/Table18.9.1/18.9.25 from step381; newly inspected DLMF3.5(ii), equations3.5.6–3.5.8, and Python decimal documentation (served as3.15.2), Decimal.exp/next_minus/next_plus/copy_negate, contexts and rounding modes.
COMPARISON: The imported finite simple-pole interface, Hermite facts, C4 Simpson remainder and decimal-operation specifications cover the audit tools. None supplies the actual centered b_4 enclosure or validates this implementation; fixed-degree large-shift results remain outside the fixed-a,n=0 claim.
GAP: Independent verification of all local algebra, moment normalization, analytic tails, fourth-derivative majorants, outward operations, complete certificate and every-real-a threshold remains necessary; no mathematical audit was performed in step383.
REASON: Essential source coverage is sufficient for the unchanged audit target; the remaining task is reproduction and conceptual verification of L764, not more discovery or an enlarged residue hierarchy.
SCOPE: Exactly TARGET with actual inputs L019/L021/L763, fixed real a>0, integer d>=max{6,ceil(12000000a)}; inspect and replay existing evidence, verify or repair the stated obstruction, and preserve any first failure. No new grid, root-sign premise or RH claim is covered.
LITERATURE_REASON: The newly nominated audit required separate approval, and essential numerical-method specifications had not been inspected in the reused residue assessment.

## Completed source review — step383

The main gap is actual-Xi all-degree positivity. The intermediate target
is an independent audit of this one sufficient-grid obstruction, whose
downstream use is to retain or repair the route stop before investing in
another mechanism. Continue with the audit only; retain the obstruction
only if every load-bearing enclosure and sign implication survives.
Otherwise record the first failure and preserve the previous certificate.
No audit conclusion or progress beyond the checked sources is claimed.

### Known interfaces reused

The detailed step381 assessment is
`drafts/literature/2026-11-04-centered-hermite-extremum-margin.md`.
Its inspected Fisk [v2 Lemma1.20(3)](https://arxiv.org/pdf/math/0612833v2)
requires distinct real denominator roots, consecutive degrees and positive
leading coefficients. Its complete relevant proof cases were already
read; no new passage was needed. The audit must check normalization,
polynomial part and orientation in this specialization, including a
possible common numerator/denominator zero. Only a necessary residue
direction is needed, not strict interlacing of the actual polynomial.
The physicists' Hermite identities and simple real roots are covered by
the exact DLMF entries in SOURCE_EVIDENCE. No original general theorem
should be substituted for these citations.

The O'Sullivan product/large-shift comparisons in step381 remain adequate
and unchanged. They do not settle the actual prescribed-grid sign claim.
L763's squared-budget stop and the recorded fixed-grid residue stop are
distinct; neither authorizes another moment hierarchy or sample search.
The exact local stop is `ATTEMPTS/2026-11-04-centered-hermite-grid-residue-stop.md`;
the calculation and pending-audit qualifications are in step382's history.

### Newly inspected primary numerical sources

[DLMF3.5(ii)](https://dlmf.nist.gov/3.5#ii), equations
[3.5.6](https://dlmf.nist.gov/3.5.E6)–[3.5.8](https://dlmf.nist.gov/3.5.E8),
assumes f in C4[a,b]; the composite rule has even n, h=(b-a)/n and
error -(b-a)h^4 f''''(xi)/180 for an interior xi. This covers the standard
quadrature theorem. The finite n-sum integrands on [0,2] have the required
smoothness from their explicit exponential formulas. The audit still
must verify their derivative majorants and actual arithmetic. L764's
local Peano-kernel argument may be checked for correctness, but is not
needed as a new theorem: the cited remainder is available directly.
The DLMF reference points to Davis–Rabinowitz (1984), pp.57–58; that book
was not newly read and is not additional source evidence.

[Python decimal documentation](https://docs.python.org/3/library/decimal.html),
served as Python3.15.2 on 2026-11-04, specifies correctly rounded
half-even Decimal.exp, adjacent representables in the selected context
for next_minus/next_plus, exact context-independent copy_negate, and
floor/ceiling directed rounding. These specifications cover the proposed
arithmetic interface, not its code correctness. The audit must identify
the replay interpreter, check precision/context propagation, exceptional
values and exponent ranges, and ensure every intermediate enclosure is
outward. No runtime version was established in this literature turn.
Only selected interface lines of the existing script were read; the
complete implementation and stored intervals were not verified or run.
No certificate preview is treated as validation.

The finite binomial division, finite positive-weight Cauchy–Schwarz,
alternating-series remainder, Machin identity and exponential-series
majorants are elementary named tools already explicit in L764. Their
application, scaling, tails and constants remain audit obligations,
not new results derived or approved here. In particular raw positive
moments do not import the sign of the centered fourth coefficient.

### Bounded search and decision

New queries were `"Jensen" "Hermite" "residue" "centered" polynomial`
and `"Simpson" "fourth derivative" site:dlmf.nist.gov/3.5`.
Search hits about large-shift Jensen asymptotics, a claimed
de Bruijn–Newman proof, external research maps and a formalization
repository were not inspected as theorem inputs. The exact-object
comparison is reused from step381; no novelty is inferred from search
results or from absence of a matching hit. No essential source blocker
remains for the selected audit. Mathlib full-result coverage remains
unchecked; no formal verification is claimed.

The next task is proof_audit/conceptual_audit, with REPRODUCTION as its
expected classification under this SPECIALIZE assessment. Subtle
cancellation and analytic/rounding accounting justify deep_research/xhigh.
This is not a creative mechanism. Actual coefficient cancellation
supporting a new central sign argument is still missing; do not invent
one to satisfy discovery scheduling. The literature-only work modifies
no lemma or mathematical script and establishes no independent audit.

## Original step382 nomination — historical, preserved

The main RH gap remains actual-Xi all-degree positivity. This audit would
validate or repair one obstruction to a sufficient prescribed grid; it
cannot establish RH or failure of hyperbolicity. Its canonical object is
L764, not a larger residue hierarchy or a changed centering.

Read L764 and its selected certificate fields completely where load-bearing;
check the exact moment scaling and cancellation, analytic n/u tails,
Simpson fourth-derivative bound, outward Decimal arithmetic, simple-pole
sign implication and threshold for every real a>0. Essential local input
identifiers are L019, L021 and L763. No unresolved actual root-sign or RH
assumption is permitted. A successful audit retains the stop; a failure
must name the first invalid implication or enclosure and preserve its
certificate. No independent audit or new literature search has happened
in this nomination. Mathlib coverage remains unchecked.
