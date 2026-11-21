# Finite higher-theta-mode allowance: separate conceptual audit nomination

TARGET: Audit C048f's reproduction of the finite higher-theta-mode allowance on the full C048c sector, including strip convergence, theta parameter, absolute Gaussian normalization and coefficient112/exponent5.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse unchanged-target discovery and duplicate/failure checks in assessment1635 and source-notes1636; no new discovery or novelty claim. This audit stays within the same finite integral, parameter sector and real-series/Gaussian specialization.
SOURCE_EVIDENCE: Kawano, Preprints.org202611.0383v1, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i), AppendixA.2(A3), AppendixB B_modes and real t>=1 series estimate, AppendixC remaining local-mode allocation; essential cases read in source-notes1636. DLMF7.7.6, https://dlmf.nist.gov/7.7.E6 , coverage reused; direct pages rechecked in recovery1638. Canonical reproduction is C048f, written step1637, with mathematical inputs C048c and L799.
COMPARISON: The source prints112sqrt(L)exp(-5r/L^2); C048f supplies an explicit uniform finite absolute-integral specialization. This nomination checks the same component rather than expanding its mathematical scope. L799's different-saddle final amplitude bound remains excluded.
GAP: A separate conceptual audit has not yet checked the newly written C048f proof and its precise input uses; the full Mellin remainder and a sufficient sign bridge are independent and unproved here.
REASON: Adequate literature coverage is reusable, but a separate audit of the new uniform analytic specialization is warranted. This newly written ready continuation receives the supervisor's separate next-turn approval before invocation; no audit was performed in step1637.
SCOPE: Only C048f's exact T_modes and unchanged full closed C048c sector; source-series verification, strip normal convergence, finite absolute domination, complex normalization, uniform scalar inequalities and direct mathematical input review.

The exact source and scope evidence is retained in
2026-11-19-mellin-higher-local-modes-scope-1635.md and
2026-11-19-mellin-higher-local-modes-source-notes-1636.md.
No additional browsing is needed while these hypotheses remain unchanged.
This is an audit of a known-source reproduction, not a novelty assessment.

Check C048f in full and the cited C048c ranges(3),(6)-(12),(19), including
the phase decomposition. Inspect L799's strip-convergence proof and
identity(4), without importing its different saddle or amplitude bound.
Verify that tau is real and uniformly >1 before geometric summation;
that the n>=2 coefficient, complete tail and 2/u normalization are correct;
that only a nonnegative real Gaussian is extended; and that the normalized
factor is sqrt(|A0|/b_*), with b_* positive. Check the exact constants
45000<51136, 11136/125<112, and17/3>5, all radial parameters L>=12,
both angular boundaries, real p and conjugation. Confirm the claimed
absolute-integral bound, not only a cancellation-dependent signed bound.

Pass if every inequality and applicability step holds uniformly with
these exact definitions. Otherwise retain the precise failed statement
or missing premise and distinguish a failed sufficient majorant from a
counterexample to T_modes or RH. Full matching Mathlib coverage remains
unchecked. Main-gap positivity, tails, assembly, zeros, inversion and the
Mellin-to-sign bridge are not audit conclusions.

## Source-link repair1638

19 November2026: directly reopened [Kawano v1](https://www.preprints.org/manuscript/202611.0383/v1)
and [DLMF7.7.6](https://dlmf.nist.gov/7.7.E6). The first redirects to the
unversioned manuscript page, which identifies Version1 and its
4November2026 posting; it remains a non-peer-reviewed preprint.
Rechecked AppendixB's unnumbered B_modes display and following series
inequalities/proof sentence, and AppendixC's domain, local width and
remaining-mode allocation. DLMF states Re(a)>0 and a real lower endpoint.
These accessible primary locations agree with source-notes1636; no
changed scope or new mathematical conclusion is asserted. Direct links
are now present in SOURCE_EVIDENCE itself. The exact TARGET and
SPECIALIZE decision are unchanged. This is the separate literature
approval of the audit nomination, not the conceptual audit of C048f.

LITERATURE_REASON: Supervisor-required repair of missing direct source URLs in the saved ready audit assessment; reuse prior discovery and source comparison without expanding coverage.
