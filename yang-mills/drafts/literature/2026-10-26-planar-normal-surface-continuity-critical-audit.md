# Planar surface continuity — completed audit source comparison

TARGET: Critically audit L293's nonzero-momentum planar surface limit and continuity, including the shifted-kernel bounds, slab soft modes and harmonic-excluded Fourier limit.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the external-momentum and frozen-normal audit assessments; read L293's complete proof for scope, L292 section 1 and the L287 hypotheses/vertex, ATTEMPTS/007,047–049 and history/517. One focused boundary-polarization query below found no inspected matching theorem; no originality inference follows.
SOURCE_EVIDENCE: Reopened Adams–Lee 0709.0781v3 Appendix A theorem (A1), fixed-p preparations (A2)–(A10), soft proof case (A11)–(A15) and the section II infrared condition; Kennedy–Sint 1511.08539v1 section 1 scope and sections 3.2–4. Reused the versioned primary slab, corrected scalar reflection and quotient comparisons in the two named prior assessments.
COMPARISON: The bulk theorem is conditional on infrared finiteness with external-parameter-dependent constants; the inspected wall result is scalar ultraviolet renormalization. Neither supplies L293's fixed-spacing signed depth defect or a uniform coalescing-pole limit. Its proof instead asserts explicit finite-matrix/kernel estimates, which can be independently audited without importing either result.
GAP: The mathematical validity of L293(8)–(21), including arbitrary internal normal slots, missing bulk rows, mixed soft/hard regimes, exceptional Fourier grid blocks and matching two-face normalization, remains unverified. Coverage is complete for this audit, not for actual-source or full-box transfer.
REASON: The saved REVIEW_REQUIRED gate needed a comparison against the newly written proof's actual obligations. That bounded comparison is now complete and has no essential inaccessible premise; EXPLORE permits the exact conceptual audit after separate supervisor approval, without certifying the proof or novelty.
LITERATURE_REASON: The turn-start audit target was REVIEW_REQUIRED; inspecting its new proof scope and deciding whether existing source coverage suffices was mandatory before mathematical scrutiny.
SCOPE: Exactly TARGET under L293/L292's SU(2), counting-measure, all-link ambient Wilson/full-density conventions, three excluded constant normal modes, paired opposite momenta, and tangential-volume-before-even-thickness limits. No new source-field, rate or boundary-stratum theorem is covered.
COVERED_TARGET: Critically audit L293's nonzero-momentum planar surface limit and continuity, including the shifted-kernel bounds, slab soft modes and harmonic-excluded Fourier limit.

## Main gap and bounded audit test

The main gap remains the interacting continuum construction. This audit
would decide whether L293 is a usable partial input toward varying
normal-source boundary pairings below the N^2 scale. Actual source
transfer, depth dependence, other groups/strata, a full-box o(N) estimate
and the uniform higher remainder are independent unresolved steps.

Preserve L293's hypotheses and the input conventions of L292, L280 and
L287, including the inherited L003, L282, L283, L288, L289 and
L279/L281/L286 qualifications. Do not introduce a scalar covariance,
a different harmonic prescription, or an external-curl omission.

The critical claims are the complete product list L293(8), the extension
to the normal second slot of CG in (9), the contact and missing-row
estimates (10)–(14), and the bound (18) in every soft/hard regime.
The finite-area proof must use the actual excluded zero block, not a
limit of the nonzero normal mode. The two-face limit and continuity
must follow for the same paired real probes and normalization.

Accept only if those claims establish the specified full surface
response; a failure requires a precise repair or withdrawal of the
affected claim. A singular individual diagram, fixed-depth calculation
or the former original-box o(N^2) remainder cannot decide this audit.
The separate audit remains undone. Its continuation test is acceptance
only when these complete estimates prove the specified limit under
the same hypotheses. A failed load-bearing estimate requires a precise
repair or withdrawal of the affected claim, preserving its derivation.
No new mathematical conclusion or primary-source import is asserted
here. Full/supporting Mathlib coverage is not checked; unknown coverage
does not establish absence.

## Primary source comparison and reuse

Reuse [the completed external-momentum comparison](2026-10-26-planar-normal-external-momentum.md)
for the precise model, prior searches and versioned theorem hypotheses.
Adams and Lee, *Structure of logarithmically divergent one-loop lattice
Feynman integrals*, Phys. Rev. D 77 (2008), 045010,
[0709.0781v3](https://arxiv.org/pdf/0709.0781v3), Appendix A,
printed pp. 19–22, (A1)–(A15), was selectively reopened. Section II's
strictly negative infrared degree is essential. The theorem's constants
depend on the external parameters; the soft proof case (A15) explicitly
uses infrared finiteness. L293 has no reduction of its depth subtraction
to this four-dimensional continuum-limit theorem. It therefore remains
a comparison, not a premise authorizing uniformity as q tends to zero.

Kennedy and Sint, *Renormalizability of the Schrödinger Functional*,
PoS(LATTICE 2015)274,
[1511.08539v1](https://arxiv.org/pdf/1511.08539v1), printed p. 2
and pp. 5–7, sections 1, 3.2–4, was selectively reopened. The presented
proof is scalar phi-four theory with a quadratic wall interaction.
Its single/multiple-wall power counting concerns ultraviolet
counterterms after subtraction of subdivergences. It supplies neither
L293's gauge quotient density nor the massless infrared/depth estimates.
No specialization or general reproof is warranted for this audit.

Reuse [the frozen-normal audit comparison](2026-10-26-planar-normal-defect-critical-audit.md)
for Luescher–Narayanan–Weisz–Wolff hep-lat/9207009v1 section 6,
printed pp. 33–40, (6.1)–(6.28), and Cornean–Garde–Jensen
2211.01974v3 Theorem 3.2 and appended corrigendum sections 1–3.
Their boundary gauge-group/background and corrected Neumann-weight
qualifications remain unchanged. Neither identifies the present
three-mode-excluded staggered covariance at zero energy. The quotient,
Laplace and finite-range source readings recorded there remain adequate
as supporting comparisons, not an isolated-minimum theorem on the slab
harmonic family or a surface-scale error estimate.

## Exact audit scope, duplicates and failure screening

The new query on 2026-10-27 was
`lattice gauge half space one loop normal polarization surface momentum infrared continuity Schrödinger functional`.
It returned the already assessed Schrodinger-functional work and
bulk/QED polarization and quark-boundary renormalization leads.
Those latter snippets are not inspected theorems or essential inputs.
No absence-of-duplicates claim follows from this bounded search.

Local comparison identifies L292 as the audited zero-momentum input,
and L287 as the complete cubic vertex with an original-box error only
at the N-squared scale. History/517 records the former audit's scope.
L293 is the pending nonzero-momentum derivation, not a duplicate
certified by either input. Its complete proof was read to identify
source obligations, not to accept or refute its estimates this turn.

The later audit should track the following obligations in that proof:

1. L293(8)–(9): all Wilson slots/phases, both crossings and external
   curls; verify the normal second slot of CG against the actual
   staggered endpoints rather than the previously averaged slot.
2. (10)–(16): the full missing-row subtraction, contacts and absolute
   depth sums, including merging poles. Individual-diagram singularity
   or continuity at a fixed depth cannot replace this test.
3. (17)–(19): all four hard/soft combinations, nonzero-momentum normal
   constant mode and the bulk subtraction in the same regime. Check
   each product before invoking the claimed common integrable bound.
4. (20)–(21): commensurate moving Fourier grids with the actual excluded
   block at exceptional points, then the thickness limit and the two
   reflected faces; finally match L292's normalization at zero. Do not
   reverse the regulator order or substitute a nonzero-mode limit for
   the excluded block.

ATTEMPTS/007,047–049 were read and preserved. Off-shell BRST closure,
integration-by-parts rearrangement, global absolute norms and generic
gauge identities respectively do not supply the missing estimate.
Auditing the explicit Wilson-specific products is a distinct test,
not repetition of those stopped mechanisms. No sibling input was read.

Essential starting IDs are L293 L292 L280 L287, retaining L003 L282
L283 L288 L289 conventions and inherited L279 L281 L286. Later
original-box use still requires even N>=2, a=8/N, all-face pins/fixed
gauges, exact product bump, both source orders and real source domain;
that transfer is not established by this coverage. No lemma, script,
DAG or PROOF argument was changed. The next task remains
proof_audit/conceptual_audit, deep_research/xhigh, after the supervisor's
separate approval of this now-ready assessment.
