# Uniform moment phase bounds — conditional audit coverage

TARGET: Audit the horizontal curvature and local second/third derivative bounds in Michalowski v1 Lemmas3.4–3.5 for k>=10^9 and |z-k|<=k/20, taking Lemmas3.1–3.3 and the stated real-saddle bounds as explicit hypotheses.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step467 reused the step385/465 comparisons and step466 assessment, searched the selected moment/q-Pascal records for duplicates and failures, and made exact-source/title plus phase-bounds/correction/erratum searches; no inspected correction or matching completed audit was located in that bounded scope.
SOURCE_EVIDENCE: Reinspected Michalowski arXiv:2607.16795v1 Section3 definitions and complete Lemmas3.1–3.5 statements/proofs, Lemma3.6 interface and Table1; inspected NIST DLMF v1.2.8 Section2.4(iv), (2.4.14)–(2.4.16). No ancillary code or certificate was inspected or replayed.
COMPARISON: These exact bounds are printed source claims; generic saddle asymptotics do not furnish their explicit disk constants. Approve only their conditional deduction from the earlier source inputs, with all Cauchy and sector domains checked; citing the conclusions under audit does not verify them.
GAP: L787 assumes horizontal/local derivative bounds and |A|<=14.185. Their deduction from Lemmas3.1–3.3 and the stated real-saddle relations remains unaudited, including the larger tube and local-disk sector checks.
REASON: Complete the newly scoped source gate so a separate mathematical turn can check this known inference; there is accessible primary proof evidence and no essential source blocker.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED enters derivative antecedents excluded from step466; reuse ready overlap coverage and inspect the essential primary proof cases for this changed scope.
SCOPE: Ready for exactly the saved conditional audit at k>=10^9, |z-k|<=k/20; no whole-wedge import, new parameter range, central sign theorem, saddle-action audit or ancillary-certificate claim. Step467 itself is literature-only.

Primary source: W. Michałowski,
[arXiv:2607.16795v1, Section3](https://arxiv.org/html/2607.16795v1#S3),
18 July 2026, *An explicit uniform cubic wedge for consecutive Toeplitz
minors of the Riemann xi-coefficients*. Numbering binds to v1.

The approved audit concerns the global horizontal curvature floor
(8/5)k/u_k^2 for x>=0.35, the local curvature floor 6/sigma_k^2
and third-derivative bound 100/sigma_k^2 on |u-u_s|<=1/40,
and the sharper |A|<=14.185 used in the printed factorization budget.
The earlier tube, saddle localization/analyticity and real-saddle
relations would remain explicit hypotheses, not independently audited
conclusions. The review must distinguish the scalar saddle map from
the notebook's theta kernel and inspect each Cauchy circle and sector
domain, including the (0.3,0.1) tube used in the printed proofs.

Plausible use: discharge the derivative assumptions of L787's
conditional inference. Essential local input is L787's normalization
and exact hypothesis interface; L786 supplies its actual-coefficient
normalization. L019/L021 and L776 are inherited definitions through
L786, with no operator or sign premises. Tube and saddle inputs,
other wedge gates, bounded k/r and global signs remain unresolved.

Continuation test: recover every required
bound with its full complex domain and a strict scalar margin from
the explicit antecedents; otherwise isolate the first unsupported
sector, derivative or Cauchy-domain estimate and stop propagation.
The source's ancillary claims alone are not verification. The target
was not attempted in step466, and matching Mathlib coverage is
not checked. No central creative mechanism is nominated by this file.

## Completed source comparison — step467

The exact target above is retained. This review approves a later
RESEARCH / REPRODUCTION audit; it derives no bound and imports none
of the conclusions under test. The previous REVIEW_REQUIRED decision
and its reason are preserved in the step466 history. L787's proof and
conditional status are unchanged.

### Inspected primary evidence and its limits

The v1 Section3 definitions and complete proofs of Lemmas3.1–3.5
were retrieved, including the end of Lemma3.5's saddle-action case.
That last case supplies context only and is excluded from the target.
The source switches from the first-summand phase to the full phase
after Lemma3.3; keep that distinction. The scalar map K in this source
is not the notebook's theta kernel.

The source proof has separate horizontal regimes, then local geometry,
second-derivative lower/upper estimates, and a third-derivative estimate.
Its proof supplies the sharper 14.185 used downstream; the statement's
20 does not replace it in L787. Table1 names certificate routines but
does not supply their complete evidence. The routine names and reported
enclosures are leads, not replayed certificates.

[NIST DLMF Section2.4(iv)](https://dlmf.nist.gov/2.4#iv),
version1.2.8, released 2026-09-15, (2.4.14)–(2.4.16), treats an
analytic phase/amplitude with an interior minimum and a simple saddle,
with branch choices for its expansion. This supports the standard
method, not these explicit kernel estimates. Its citation does not
discharge the present hypotheses or constants. No other theorem is
imported. Matching Mathlib coverage remains unchecked.

### Fixed conditional interface for the mathematical turn

Use L787's actual Phi, I, full phase, z-disk, u_k, u_s and sigma
definitions exactly, with L786 supplying the coefficient normalization.
L019/L021 and L776 contribute inherited definitions only through L786.
Do not import their unrelated sign or operator premises.

Assume the earlier source Lemmas3.1–3.3 and the real-saddle data
explicitly, rather than auditing them too. In particular retain the
general tube-majorant formula of Lemma3.1, not just the numerical
(0.35,0.1) instance in L787; the horizontal proof invokes the larger
(0.3,0.1) tube. Verify the geometric-series admissibility at each
chosen tube before using its majorant. The existence and analytic
localization of the full saddle, with drift at most 3/200, remain
conditional. Retain k=u_k H_0, B_0=2pi exp(4u_k),
H_0=B_0-9/2-6/(B_0-3), 1<u_k<log(k)/4, and
(21/25)B_0<=H_0<=B_0. Those assumptions are not conclusions
of this continuation.

Exactly the horizontal floor and local second/third derivative bounds
listed above, including the sharper saddle bound, are under audit.
An analytic proof of their constants is justified because the source
delegates parts to uninspected computation and the notebook needs
their exact domain-qualified interface. This is reproduction of a
known claim, not a claim of originality or an independent whole-paper
verification. No certificate-only value may be accepted without its
complete proof evidence.

### Bounded audit checklist and stop rule

Check the horizontal sector estimates and both sides of the split at
u_k, with the Cauchy-circle radius and supremum specified on a tube
where the assumed majorant applies. Distinguish estimates for R from
estimates for log(1+R), including its analytic branch. Do not infer a
bound for derivatives merely from a bound on R at the center.

On the entire local complex disk, check the exponential/resolvent
components and their sigma normalization separately. The source refers
back to horizontal sector estimates while asserting disk-wide bounds;
the later audit must justify the sectors on that disk explicitly.
Check the second and third logarithmic-tail derivatives on complete
Cauchy circles. Do not substitute a saddle-only estimate for a
pointwise one or differentiate an unproved remainder.

Continue only with all required inequalities and strict margins
recovered on their exact domains. Otherwise record the first unpaid
domain, sector or derivative estimate and stop propagation to L787.
A failed printed intermediate estimate and the failure of the claimed
conclusion are different findings. Any repair must be explicit and
stay within this conditional target. No numerical sample suffices.

### Duplicate/failure comparison and search record

Reused step385 in `2026-11-04-actual-jensen-mechanism-discovery.md`,
step465's growing-order comparison and step466's factorization coverage.
Read the selected q-Pascal endpoint audit assessment and its ATTEMPTS
record; searched the signed symmetric-part and endpoint assessments.
Those scopes concern the matrix comparison or explicitly exclude
analytic GateA constants. L765's norm and L774's accretivity stops
remain in force for their original criteria. They neither prove nor
refute this independently testable analytic implication. No broader
duplicate-free or novelty claim follows from these local searches.

Queries included exact author/title, `2607.16795 curvature`,
`2607.16795 erratum`, `2607.16795 phase bounds`, and the exact title
with `correction`. Results did not identify an inspected correction;
this does not prove that none exists. Secondary aggregator and search
snippets supplied no mathematical input. No unrelated returned lead
was promoted to assessed coverage. Initial notebook-local status and
batched search output were oversized; neither truncated output was
used as completeness evidence. Essential proof passages were fetched
separately, including both proof endings. No sibling notebook was read.

Plausible downstream use remains conditional growing-order Taylor
control through L787. The tube/saddle inputs, all other wedge gates,
bounded k/r and global positivity stay open. No independently supported
central signed mechanism emerged from the already completed step465
discovery; this source review supplies none and does not relabel an
established-route audit as creative work.
