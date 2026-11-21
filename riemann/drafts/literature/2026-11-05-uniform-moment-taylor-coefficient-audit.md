# Uniform moment Taylor coefficient audit — source coverage

TARGET: Audit Michalowski v1 Proposition3.7's all-degree bound |f^(d)(k)/d!|<=3*40^d*k^(1-d) for d>=3 and k>=10^9, including its saddle-action input and the L787/L788/L789 assembly.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step471 reuses step465 and the three preceding audit assessments; targeted local statement/failure searches and exact source-ID/Taylor/correction/erratum searches found no inspected completed coefficient audit or correction in that bounded scope.
SOURCE_EVIDENCE: Read Michalowski arXiv:2607.16795v1 Section3 definitions, complete Lemma3.5 saddle-action case, Lemma3.6 interface and complete Proposition3.7 proof/Remark3.8; inspected NIST DLMF v1.2.8 Sections5.2(i),25.11(i),(v), especially (5.2.2),(25.11.1),(25.11.12); reuse the previously inspected Cauchy-estimate coverage.
COMPARISON: The exact coefficient inequality is a printed source claim. Standard formulas cover the Gamma derivatives and Cauchy method, while L787/L788/L789 provide the local conditional interfaces; their assembly, branches and explicit all-degree budget still require a reproduction audit.
GAP: Check the saddle-action input, compatible analytic logarithms, complete Cauchy circles, Gamma-series specialization and uniform sum for all integers d>=3; no coefficient conclusion or whole-wedge import is established by this review.
REASON: The essential changed-scope sources are now inspected, permitting a separate mathematical audit without assuming the conclusion or replaying unrelated gates.
LITERATURE_REASON: The ready tube/saddle scope excludes the saddle-action and Taylor estimates; essential exact-source and standard-input comparison for Proposition3.7 is still missing.
SCOPE: Ready for exactly the TARGET on integer k>=10^9 and integer d>=3, with L787/L788/L789 assembled and their qualifications retained; excludes other wedge gates, curvature-normalized corollaries, bounded k/r positivity and central signed mechanisms.

W. Michałowski, *An explicit uniform cubic wedge for consecutive Toeplitz
minors of the Riemann xi-coefficients*,
[arXiv:2607.16795v1, Section3](https://arxiv.org/html/2607.16795v1#S3),
18 July 2026. Numbering must bind to v1. Use the primary statement and
complete relevant proof cases before relying on ancillary values.

Step470 proposed this continuation with REVIEW_REQUIRED. Step471 completes
the separate literature approval; no coefficient derivation is made here.
Reuse `2026-11-05-growing-order-post-import-discovery.md`,
`2026-11-05-uniform-moment-factorization-audit.md`,
`2026-11-05-uniform-moment-phase-bounds-audit.md` and
`2026-11-05-uniform-moment-tube-saddle-audit.md` within their scopes.
Do not repeat a broad discovery search or infer novelty from one.
The known claim is now approved only as a reproduction-audit target.

Essential inputs are L787's factorization inference, L788's conditional
phase estimates and L789's restricted tube/real/full-saddle verification.
L786 supplies the downstream coefficient normalization; L019/L021/L776
are inherited definitions, not additional positivity assumptions.
The analytic f is intended to be log(I(z)/Gamma(2z+1)); its branch,
domain, relation to integer coefficients and complete Cauchy circles
must be checked, not inferred from the proposed bound itself.

## Completed comparison — step471

### Primary source and standard inputs

Numbering binds to the primary v1 text cited above, Section3. The
saddle-action case of Lemma3.5 supplies an envelope identity; Proposition3.7
uses a weaker action bound, Cauchy estimates on radius k/40, a curvature
logarithm, the analytic relative error, and real-center polygamma bounds.
Read all four proof cases and their concluding sum, through Remark3.8.
This is the exact target already claimed by that source, not a new
coefficient theorem. No ancillary code or certificate was inspected or
replayed, and its tighter numerical component values are not accepted
as verified inputs. The later audit may use the printed rounded bounds
if their complete sum meets the stated target.

The [NIST DLMF](https://dlmf.nist.gov/25.11), version1.2.8,
release2026-09-15, provides the precise standard series input:
[25.11.12](https://dlmf.nist.gov/25.11.E12) relates polygamma of integer
order n>=1 to Hurwitz zeta, and
[25.11.1](https://dlmf.nist.gov/25.11.E1) gives its series for Re(s)>1,
a outside the nonpositive integers. The intended specialization is
n=d-1, s=d and a=2k+1>0. The numerical upper bound after the affine
chain rule, division by d!, and comparison of a positive decreasing
series with an integral is an audit obligation, not a result of this
literature turn. These exact formulas suffice as source coverage; no
complex Stirling remainder is required for this target.

[DLMF5.2(i)](https://dlmf.nist.gov/5.2#i), including (5.2.2), records
Gamma nonvanishing, its poles at nonpositive integers, and the
logarithmic derivative psi. Apply only where 2z+1 avoids those poles.
The analytic-logarithm theorem on a simply connected zero-free domain
and Cauchy's derivative estimate are standard named inputs. Reuse the
complete Cauchy-estimate hypotheses and Rutgers citation already
inspected in `2026-11-05-uniform-moment-tube-saddle-audit.md`, under
"Standard inputs and exact-source limits". They require a complete
circle and holomorphy on its neighborhood, not sampled values.
No full matching Mathlib theorem has been checked; these supporting
inputs do not constitute a formal verification of Proposition3.7.

### Fixed interface and permitted audit

Use the definitions and bounds of L789 on its restricted small-strip
tubes and k-range. Apply L788 as a conditional implication only after
matching every real/tube/full-saddle assumption to L789. Then match
L787's complete hypothesis interface to those results. This order is
an assembly task for the mathematical turn; this review makes no
new unconditional factorization assertion. L786 supplies the actual
ordinary-coefficient normalization, with L019/L021/L776 inherited
definitions only. No positivity premise may be added to fill a gap.

Audit the following as one coherent proof of the exact TARGET:

1. Verify the full-saddle action is analytic with the agreed phase
   branch and justify its differentiated stationarity identity. Obtain
   the action bound actually needed by Proposition3.7 from the proved
   local constants. Distinguish source-specific sharper decimals from
   sufficient weaker constants; L788's verified constants need not
   reproduce the source's uninspected sharper enclosures.
2. Construct compatible logarithms of the moment quotient, curvature,
   relative error and Gamma factor. Justify their relation, including
   any constant branch difference and the real-center normalization.
   Specify the entire radius-k/40 circles inside the analytic domain.
   Nonvanishing must come from the preceding implication, not the
   coefficient bound under audit. Do not differentiate a bare uniform
   remainder estimate or assume a principal log of I exists globally.
3. Check each Cauchy derivative order and factorial, the curvature-log
   modulus bound throughout the circle, and the relative-error log
   bound on that same domain. Keep k and sigma fixed while
   differentiating in z. Use the real-center Gamma formulas above,
   explicitly tracking the affine derivative factor and all degrees.
4. Sum uniform bounds after division by the required
   40^d*k^(1-d) scale. Justify any reduction to the smallest degree and
   height rather than testing finitely many cases. The required
   threshold is 3 for every integer d>=3 and k>=10^9.

This reproduction is justified because the notebook has not checked
the new action/log/Gamma interface and cannot import an uninspected
ancillary enclosure as a verified proof. Merely reciting the printed
coefficient assertion would add no local verification. No reproof of
the standard Gamma or Cauchy theorems is requested. The source's
tau-normalized follow-up uses a separate curvature input and is
outside this exact target; no such corollary is needed for this audit.

Continue if the full argument meets that threshold from the stated
inputs. Otherwise isolate the first unsupported hypothesis, branch,
domain or constant and retain the conditional result. A failed printed
intermediate estimate alone does not refute the coefficient conclusion;
any repair must be explicit and remain within this target. Do not
propagate this audit to the other wedge gates or global signs.

### Reuse, failures and bounded search

Reused step465's three-mechanism comparison and the ready factorization,
phase and tube assessments at their unchanged scopes. Read the relevant
L787 hypothesis/conclusion/branch passages, L788/L789 interfaces, and
step470 history. Local searches covered the selected uniform-moment
working notes/histories and those assessments for Proposition3.7,
Taylor, saddle action and polygamma. They show that this target was
excluded from the prior gates, rather than already completed there.

Reused the recorded L774 accretivity stop through step465 and read
`ATTEMPTS/2026-11-04-actual-qpascal-endpoint-norm-stop.md` for L765.
Their near-regime matrix criteria remain stopped; neither is an input
to this analytic tail target. The existing step465 conclusion supplies
no independently justified central signed mechanism, and this focused
source comparison supplies none. That is the blocker to creative
routing; a routine source specialization must not be relabeled creative.

Queries included `"2607.16795" "Taylor" correction`, the exact title
with `erratum`, the source ID with `"Proposition 3.7"`, and the source
ID with `"erratum"` and `"polygamma"`. No correction was inspected;
empty results and secondary aggregator hits prove neither absence of
corrections nor novelty. Primary mathematics came only from the cited
v1 and NIST passages. Broad discovery was not repeated.
Some batched output was truncated; it was not used as completeness
evidence. The full selected Proposition3.7 proof ending and the exact
NIST polygamma/Gamma statements were retrieved separately. No essential
source blocker remains. No sibling notebook, API key, runtime state,
lemma file or mathematical script was changed.

Main gap remains actual-Xi all-degree mixed positivity. The plausible
intermediate use is uniform growing-order coefficient comparison in the
far tail. Continue only if the literature gate covers the complete
argument and a later audit closes the stated all-degree constants.
Otherwise isolate the first unsupported input or failed estimate and
retain conditional status. Neither the whole wedge nor central signs
follow from this target. Full matching Mathlib coverage is unchecked.

Step465 did not identify a supported central creative mechanism, and
step470's source audit supplies none. Preserve the L765/L774 stops;
a new central mechanism needs a changed representation or a justified
signed estimate, not merely a stronger coefficient tail bound.
