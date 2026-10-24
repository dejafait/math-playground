# Coverage: lower-band theta critical audit

TARGET: Critically audit L458's lower-band whole-plane theta reduction on 7/8≤m/r≤31/32, including complete sector errors, cutoff equalities and positive normalization.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed lower-band search and theorem comparison in 2026-10-23-lower-band-whole-plane-theta-coverage.md and the L455 audit assessment; compared L458's complete proof with their covered mechanisms, L455's separate audit, L269's parameterwise contour passage and C294b's hypotheses/conclusion. Read the recorded L323/L327 failures. No fresh external search, matching theorem or novelty claim.
SOURCE_EVIDENCE: Reused inspected Csordas, arXiv:1309.0055v2 (21 February 2014), https://arxiv.org/html/1309.0055v2, Theorem 3.5, Lemma 3.6 and Theorem 3.7, (3.10)–(3.14), statements and proofs; NIST DLMF https://dlmf.nist.gov/2.3#iv, hypotheses (a)–(d), (2.3.21)–(2.3.23), and https://dlmf.nist.gov/7.2#iii, (7.2.6)–(7.2.9). Relevant primary passages were inspected on 2026-10-23 as recorded in the reused assessments; no external passage was newly retrieved this turn.
COMPARISON: Existing coverage includes the identical lower-band reduction target and its explicit methods; the L455 correctness verdict applies only to its older band. Neither primary sources nor that verdict certify L458's changed-domain uniformity. They suffice for an independent audit of the written specialization, without an unread general uniform stationary-phase theorem.
GAP: A separate correctness verdict remains required for L458 (1), every complete normalized error, all cutoff and band endpoints, positive normalization and one common onset. No arithmetic sign application or proof audit is completed by this assessment.
REASON: The new audit scope is now compared with adequate unchanged source evidence and the actual written proof; approve this bounded critical audit rather than repeat source discovery or treat its predecessor's narrower verdict as transferable.
SCOPE: Positive even m, all sufficiently large positive real r, 7/8≤m/r≤31/32, h=9/2+m/(2r), a=sqrt(4π²exp(4r)−h²)>0, and exactly L458's finite signed sum with zero weight at log(jk)=2r. Audit the additive theta reduction only.
LITERATURE_REASON: The saved continuation requests a separate audit of L458's changed closed band; the prior audit assessment concerns L455's narrower band. Reuse existing primary coverage while comparing the new proof obligations.

## Completed scope comparison

The action at invocation start was “Assess coverage for a critical audit of
L458's lower-band whole-plane theta reduction on 7/8≤m/r≤31/32,
including complete sector errors, cutoff equalities and positive
normalization.” This literature-only step completes that comparison.
The TARGET above is the newly ready research continuation, subject to
separate next-turn approval. No correctness verdict is given here.

The main gap remains initial low-index signs and global mixed positivity.
The intermediate target is an independent verdict on the entire additive
reduction. Its plausible downstream use is a separately scoped assembly
with L457's audited arithmetic margin. Every-height transfer, smaller
indices and bounded heights remain independent obligations.

Reuse [the lower-band review](2026-10-23-lower-band-whole-plane-theta-coverage.md),
[the L455 audit coverage](2026-10-23-subendpoint-uniform-sector-critical-audit-coverage.md)
and their inspected primary evidence. Csordas Theorem 3.5 assumes an
admissible kernel and strict logarithmic concavity on the positive
half-line; its proof separates s<t and s>t. Lemma 3.6 and Theorem 3.7
supply the coefficient/double-integral identity, retaining Jacobian and
factorial. The real-zero conclusion still requires positive definiteness
at every level. No such positivity is imported.

DLMF 2.3(iv) requires smooth phase/amplitude, a nonzero phase derivative
away from the stationary endpoint, differentiable endpoint expansions,
and controlled finite limits or uniform convergence at infinite
endpoints. Both finite endpoints contribute. It does not provide the
moving-index two-variable error claimed in L458. DLMF 7.2.6–7.2.9
supplies only scalar Fresnel definitions and limits. Explicit local
variation and real-phase estimates must carry uniformity. Olver/Lyness
and the earlier SIGMA lead remain unread and unimported; no essential
coverage depends on them. Full matching Mathlib coverage and supporting
library matches remain unchecked, not absent.

## Exact obligations for the subsequent audit

Read L458 Sections 1–4 and Mathlib for this comparison, L455's separate
critical audit, L269's parameterwise shift/Fubini passage, and C294b's
hypotheses/conclusion. Reused the prior complete L455 and C294b proof
comparisons; the future audit must inspect any load-bearing details
rather than rely on those comparisons as correctness certificates.

L458's beta interval is [1/32,1/8]; its h interval is
[79/16,319/64]. The new high-strip bound (11) explicitly replaces
L455's older beta restriction. This is a written claim to audit, not
an estimate validated by this review. The following constitute one
coherent audit target:

- Trace L269's parameterwise identity without importing its unrelated
  proportional-index asymptotic; reserve uniformity for the sector proof.
- Check L458 (7)–(12): complete discrete corner/edge/area masses,
  clipping tail starting at K−1, the rational logarithmic comparison,
  derivatives through order two at zero, both low and high rectangles,
  strip intersection, infinite limits and summed moduli.
- Check (13)–(16): full infinite translated-index sums, at most four
  complement rectangles with actual moving edges, clipped/full squares,
  the real phase map and Jacobians, uniform per-weight errors before
  summing, and all equality assignments at b±epsilon and log(jk)=2r.
- Check C294b at the identical parameters and its complete mixed-sector
  bounds, with its already included area Jacobian. Check (18) against
  C(1+r)^2 exp(−r/200), including mass times patch error and the
  high-strip double exponential, using one C,R on the entire closed band.
- Recover exactly P=[2^(m−1)/m!]C₀exp(Φ_*)π/a>0: two opposite
  Fresnel factors, area Jacobian 1/2, one same-sign reflection, the
  whole-line transform normalization, reality and factorial exactly once.

These are proof obligations extracted from the existing argument,
not newly derived bounds. No lemma or mathematical script is changed.

## Duplicates, failures and decision test

L458 is the existing target theorem, so the continuation is its audit,
not a new duplicate reduction. L455's narrower theorem and audited
mechanisms are inputs, not a changed-band correctness verdict. The
recorded L323 r/4-strip obstruction and L327 unsigned/PSD obstruction
were read in their specific ATTEMPTS records and reused with their prior
canonical comparisons. Preserve both: L458 uses r/20 and the original
signed arithmetic sum, so neither historical stop is a global ban or
an audit shortcut.

Continue toward separate assembly only if the audit validates every
complete budget and normalization on all admissible real r and even m
with a common onset. If a term fails, identify its exact claim and
preserve the failure before repair or abandonment; a source approval
cannot excuse an uncontrolled region. No sign conclusion follows from
approving this scope.

Essential audit inputs are L458, L455's explicit proof and separate
audit, L269 and C294b, tracing L324/L325 through L455 if necessary.
L457 is downstream only. No external zero-free premise enters this
reduction. A later L457 application retains L452/L456 and September 30
Theorem 1.1 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a,
strict Re(s)>7/8, the allowed pole and unaudited manuscript/import
closure. Global mixed positivity and all selected-law/regulator gaps
remain unresolved. This source review establishes no progress beyond
the inspected source methods and no RH candidate.
