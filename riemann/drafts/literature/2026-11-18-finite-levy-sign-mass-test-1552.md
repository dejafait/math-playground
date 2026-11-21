# Finite Levy sign and mass test: prepared continuation1552

TARGET: Test whether either ordered difference ell_2-ell_1 or ell_1-ell_2 has nonnegative density and finite total mass, using C032j's exact Gaussian transform and the cited heat-sum estimates.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-query and narrow duplicate/stop search completed in review1551 during step1552; full queries and scope comparisons are in 2026-11-18-finite-levy-source-notes-1552.md. No inspected theorem supplies the actual ordered-difference conclusion; no novelty is inferred.
SOURCE_EVIDENCE: Bertoin2000 Theorem1.2 pp7-8 and finite-activity case p9 https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf ; Sra2611.00345v1 Proposition3.1 pp5-6/full proof p21, A.7 pp16-17 and Theorem4.1/proof p9 https://hexagonmath.org/pdf/2611.00345v1 ; Sra2610.00584v1 PropositionB.1 and full proof p17 https://hexagonmath.org/pdf/2610.00584v1 ; convolution/uniqueness and Poisson-law primary URLs are in source-notes1552.
COMPARISON: Standard finite-activity law comparison is available only after proving positivity and finite mass of a difference; individual Levy integrability and width persistence do not prove these. The exact heat transform and endpoint/derivative results are covered inputs; derive only their missing two-width comparison.
GAP: Global sign, cancellation-controlled zero-endpoint integrability, and strictness of any successful comparison are unproved. No source theorem decides C032q's cone, full cancellation or actual-Xi realization.
REASON: Missing source coverage was completed before this nomination; this is an established-law specialization with a bounded discriminating test, not a creative all-degree mechanism. Separate supervisor approval of this newly prepared assessment precedes research.
SCOPE: C032j/m/q actual-divisor, multiplicity, counting, finite-zero, heat and fixed-v1 qualifications; fixed half-variance widths 1 and 2, ell_sigma=H_sigma/t; no RH, p_sigma positivity, law-density, exponential-moment or full J_eta=0 assumptions.

Use [source notes1552](2026-11-18-finite-levy-source-notes-1552.md).
All essential primary input statements and relevant proof cases were
retrieved; no new endpoint claim is an input. At zero, do not subtract
leading equivalents or differentiate an O remainder without an estimate
for the resulting error. At infinity use the cited smoothed-law tail,
not the unsmoothed heat sum at infinity: its transformed time is bounded.
A fixed grid is exploratory only, never a proof of sign or convergence.

Continue a direction only with a global nonnegativity proof and finite
integral, with constants or justified integrable majorants at both ends.
A rigorous wrong sign at one positive time or divergent total mass stops
that direction. If both stop, park this sufficient construction; if the
bounded attempt is inconclusive, preserve the missing bound precisely.
If one passes, its later use is a cited finite-activity comparison toward
a genuinely signed mass-one input with positive output. Such a law would
still not satisfy the full cancellation requirement of C032q; stop1302
remains. This test does not decide RH or imply all-degree positivity.

No mathematics has been performed or approved in this nomination.
Full matching Mathlib coverage remains unchecked and unknown.
