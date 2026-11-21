# Complete Gaussian member-pair conceptual audit

TARGET: Audit C034h(1) on its full parameter domain, checking the mixed-cutoff kernel extension, complete origin/connector corrections, Gaussian bounds, and the 496 versus <471 margin.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment1862/source-notes1862's exact-sign search, source-notes1854's integration comparison and coverage review1865 in drafts/literature/2026-11-20-laplace-complete-pair-audit-coverage-1864.md; compare complete stops1839/1843/1847. No new sign theorem or duplicate completed pair audit was identified; no novelty inference.
SOURCE_EVIDENCE: Haslinger Section2.2 Theorem2.5/Corollary2.6 pp45-48 https://www.mat.univie.ac.at/~has/scriptneu.pdf ; Hunter Section5.6 Theorem5.18/Example5.19 p61 https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf ; Hunter Section4.5 Theorem4.24/Section4.6 pp49-50 https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf . Statements and available essential proofs were inspected1865; reuse Gaussian coverage1846/1854 and C034d/e/f with their recorded qualifications.
COMPARISON: General contour, complex Fubini and dominated-convergence theorems support the operations once their hypotheses are checked. C034e covers two strip coordinates, not automatically a real coordinate>=1 with a strip coordinate; C034h's displayed extension, core constant and all correction estimates require independent scrutiny. No source theorem supplies C034h(1).
GAP: Determine whether the written complete-pair proof is correct under its exact hypotheses; scalar checks alone do not validate complex averaging, domain extension, derivative envelopes, uniform limits or the correction expansion. Total-divisor assembly and C034c(20) are outside this audit.
REASON: Coverage review1865 found no missing essential general input for auditing the existing finite-member specialization. Check it before downstream use; import the named tools and audit their applications without rederiving general theorems or introducing a new sign mechanism.
SCOPE: Only C034h(1)-(14), gamma,eta>14 independently, |delta|,|epsilon|<1/2, displacement zero for each ordinate<=100, sigma in [1,2], and uniform [1/2,3] estimates only for the claimed integral/limit operations. Include coincident/unequal pairs, all four translates/conjugates per member, both finite cutoffs and every correction. No infinite-divisor assembly or stronger domain.

The main gap is L030-L032/C032a actual-Xi all-degree positivity. The
intermediate target is a critically reviewed finite-member inequality
P<-25*(gamma^-4*eta^-8+gamma^-8*eta^-4). It could support C034c(20)
and C034b's final width prefix only after a separate justified actual
divisor assembly. Independent signed height, cancellation and actual-Xi
realization remain unresolved. This nomination approves source scope,
not the mathematical sign. A newly written continuation receives the
supervisor's separate approval before invocation.

One coherent conceptual audit should scrutinize the following parts
of the existing proof; it need not discover additional lemmas:

- Match h_z to the four terms of weight1/4, including real members,
  and check (2)-(3) against C034d/f's original ordinary subtractions.
  Check both connector orientations, both finite traces, all origin
  constants, pole-free paths, and the fixed-member uniform [1/2,3]
  limiting argument. No divergent single-translate split is allowed.
- Check C034h's mixed real/strip use of C034e's polynomial identity,
  including T=0, independent argument signs, every nonnegative
  remainder term and the one negative block. Audit the strengthened
  core angle/modulus estimates (11)-(12) and their entire domain.
- Check Gaussian normalization/scaling, the weighted-integral split,
  all width/ordinate monotonicity assertions, fourth-derivative and
  real origin envelopes (9)-(10), and nonreal corrections with the
  essential ordinate>100 condition. Keep the finite connectors.
- Verify positive-center weights, both translates, symmetry/convexity,
  independent and coincident pairs, and the exact expansion paying
  all correction products in (13)-(14). Compare the achieved margin
  with the stated25 threshold without extrapolating any constants
  to the larger width interval.

Review the existing32-check scalar certificate as supporting evidence,
including any selected load-bearing complete rational values, with
`python3 ../scripts/loop/inspect_json.py` and bounded pointers. Replay
the existing script only if needed for the audit. Do not infer the
analytic hypotheses from its pass count. Preserve the first-pass
floor-comparison failure and correction. The135 floating samples
are not evidence for any universal sign. A numerical preview alone
cannot certify or refute the original ordinary integrals.

Continue this result toward assembly only if every load-bearing claim
survives critical review. On failure record the exact estimate and
its domain, and repair only within this covered audit scope or withdraw
the unsupported pair claim. An unrepairable gap is an informative
audit failure, not a refutation of RH. A materially different proof
mechanism or enlarged hypothesis domain needs REVIEW_REQUIRED coverage.

Essential mathematical inputs: C034h and C034d/e/f. C034g's origin
bypass/finite-part construction is unused. C034c/b and C032n(8)-(9)/(13)
are context; C032m/C033w through C033l/C032q retain actual divisor,
conjugation/multiplicity, ordinate0 exclusion, strict strip/gamma>14,
count, through100/retained real zero, reciprocal-square tail, heat
positivity/separate fixed-j errors, both fixed-v1 source inputs,
zero drift/killing and half-variance for any later use. These are not
all needed for the standalone finite-member statement, nor verified
by its audit. Source-wide/finite-zero validity, global Sobolev membership
and full Mathlib matching remain unverified. Actual-divisor assembly,
C034c(20), final prefix, conditioning, entries/m, exact weights,
TV<=2, observations, signed height/cancellation and Xi realization
remain unpaid. Preserve stops1839/1843/1847 and older route evidence.

Proposed task: RESEARCH/proof_audit/conceptual_audit, REPRODUCTION,
deep_research/xhigh. Complex averaging, singular-origin bookkeeping
and the uniform independent-pair comparison require conceptual review;
this is neither a routine arithmetic replay nor a complete-candidate
audit. Essential scrutiny takes priority over creative discovery while
no independently covered central realization/height mechanism is ready.
