# First-odd law: bounded necessary derivative test

TARGET: Test the mass-one widths-1,2 law with J_eta'(0)=0 against the first two necessary Laplace derivative signs near s=0 using C032m's analytic Taylor remainder; certify a violation or stop this local test as inconclusive.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1562 compared the precise constrained output-sign target with local finite-mixture/compound-Poisson results, failures1302/1551 and primary domination, signed-Tauberian, convolution-tail and complete-monotonicity sources; see source-notes1562. The bounded actual two-width derivative test was not located there; no originality claim follows.
SOURCE_EVIDENCE: Ante Mimica, Laplace transform (Dresden course, 27 April-1 May 2015), https://web.math.pmf.unizg.hr/~amimica/lt.pdf , Proposition1.4(i)-(ii), printed pp6-7, supplies necessary derivatives under positivity; statement and complete proof of these parts rechecked directly in recovery1563. Theorem2.4 pp14-16 supplies the full classical criterion but is not needed or re-reviewed here. Exact hypotheses and prior proof coverage are in drafts/literature/2026-11-18-first-odd-output-source-notes-1562.md. C032m supplies the existing entire lifts and derivative control; notes1552 Laplace coverage is reused.
COMPARISON: Classical necessity does not evaluate the actual constrained coefficients or jets. Specialize only those coefficients and derivative orders one and two for sufficiently small positive s. No density, tail inversion, signed moment at zero or complete-monotonicity sufficiency is needed for a rigorous violation.
GAP: Nondegeneracy of the two linear constraints and the actual low-order sign constants/remainders must be checked; neither a violation nor a favorable sign is known. Passing these tests leaves all-Borel positivity and every higher-order/global requirement unresolved.
REASON: This is a bounded, density-free test of the same constrained law after source comparison; no citation decides its actual constants. Reproduce the known necessary-sign application and derive only those missing actual-family quantities. The test is prospective and receives separate next-turn approval before execution.
SCOPE: Exactly two real width atoms at 1 and 2, mass one, J_eta'(0)=0, derivative orders one and two near positive s=0; retain all C032j/q qualifications. No extension to more widths, additional odd constraints or automatic higher-order search.

Use C032j/q's bounded Laplace identity and signed Borel construction,
C032m's entire functions F_eta,J_eta and definitions E_sigma,O_sigma,
C032l's recorded b_sigma'(0)=2*pi*p_sigma(0), and C032s/t/u only
where their established statements actually supply comparison data.
Review1562 has not solved the linear system or determined its signs.
If it is singular, report the exact consequence rather than assuming
unique coefficients. Read only the necessary canonical proof ranges.

For a positive output, the cited derivative formula requires L'(s)<=0
and L''(s)>=0 for every s>0. The research question is whether the
actual constrained output violates either sign for all sufficiently
small positive s. Establish the requisite analytic remainder from the
entire lift before using s=w^2. In particular, a bounded Taylor
remainder on a complex disk may be differentiated by its holomorphic
structure; an arbitrary real big-O remainder may not. Do not cancel
divergent signed moments or infer a density.

A strictly wrong sign with a rigorously controlled remainder is a
negative-output certificate for this pair. If both necessary tests
pass, or actual constants cannot be controlled within this one attempt,
stop this local test as inconclusive and preserve the reasoning. Do
not manufacture a lemma for favorable necessary conditions, raise the
derivative order automatically or claim positivity from a finite list.

Main-gap use and limits: discriminates one constrained building block
for C032q; it decides neither full J_eta=0, continuum feasibility,
exponential moments nor unsmoothed actual-Xi positivity. Stop1302 is
retained. This is a classical-criterion specialization, not a creative
central mechanism or progress beyond the sources by default. Matching
Mathlib coverage remains unchecked and unknown. No mathematics has
been executed under this newly written assessment in review1562.

## Direct-source gate repair1563 (18 November 2026)

The direct primary PDF URL above was opened successfully. Its printed
pages 6-7 contain Proposition 1.4 and the proof of parts (i)-(ii).
The statement assumes a positive measure on [0,infinity) with finite
Laplace transform at every positive parameter. Part (i) permits all
positive-parameter derivatives; its proof controls difference quotients
by an integrable exponential using finiteness at a smaller positive
parameter. Part (ii) uses monotone convergence for endpoint moments.
Only part (i) is essential for the saved test: positivity of the output
is the assumption to contradict, not an established premise. Neither
endpoint moments nor a density are required. The displayed first
derivative proof omits a limit before a difference quotient; the
dominated-convergence sentence and subsequent integral identify the
intended limit. This typographical omission changes no imported claim.

This repairs source traceability and separately approves the unchanged
SPECIALIZE scope. The target, hypotheses, derivative orders and stop
test remain exactly those above; no coefficients or signs were computed.
The earlier duplicate/failure comparison in source-notes1562 is reused.
Full matching Mathlib coverage remains unchecked and unknown. No new
literature result or mathematical advance is claimed by this repair.
