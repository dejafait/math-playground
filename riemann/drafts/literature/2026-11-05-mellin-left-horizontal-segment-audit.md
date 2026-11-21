# Finite left horizontal theta-Mellin segment: completed audit-scope review

TARGET: Critically audit L802's standalone finite left horizontal theta-Mellin bound on all D, including full-segment angle concavity, theta amplitude, endpoint slope and the 512/105, 85/48 constants.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step526's exact-segment duplicate/failure search and primary left-envelope comparison in 2026-11-05-mellin-left-horizontal-segment-scope.md; step527's narrow local search found no completed left-segment proof preceding L802. No new search or novelty claim.
SOURCE_EVIDENCE: Reopened Devroye ChapterVII Section2.6 pp299–300 (zero-based PDF pages13–14) in step528; reused step526 for paper23. Devroye, Non-Uniform Random Variate Generation (1986), ChapterVII Section2.6, pp299–300, left envelope preceding Theorem2.6 and reflected-case reduction/first integral in its proof, https://luc.devroye.org/chapter_seven.pdf, inspected in step526; paper23 v1 Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23. The complete prior comparison is in 2026-11-05-mellin-left-horizontal-segment-scope.md.
COMPARISON: The source method and target domain are unchanged. L802 supplies the parameter-specific hypotheses and payment; auditing that proof requires no new asymptotic theorem, global contour claim or unread supplement. The source's combined budget remains unimported.
GAP: Independently check L802's entire proof, especially the outward-height argument for Re(s/z^2)>0, complete-series control at v=u/2, horizontal endpoint derivative and exact normalization. No mathematical correctness approval is given here.
LITERATURE_REASON: The supervisor requires separate approval of the newly written audit nomination; this turn checks that L802 introduces no essential unread source beyond the ready step526 coverage.
REASON: An essential conceptual audit is needed for this newly written source specialization. Existing primary method coverage is adequate, but cannot certify its moving-parameter inequalities by citation alone.
SCOPE: Step528 completes the separate literature approval for the exact saved audit target; ready for a RESEARCH conceptual audit classified REPRODUCTION. Only source scope is approved, not L802 correctness. No global assembly or new sufficient-sign mechanism is covered.

Essential local inputs are L797's saddle/branch geometry on the closed D,
L798's phase derivatives, decrement and normalization, and L799's normal
convergence and exact theta factorization. Read L802 in full and the
relevant input ranges. L800 and L801 supply downstream context, not a
premise in L802's bound. No cross-notebook input is proposed.

Check the full closed interval [u/2,v_L], not just the rotated endpoint:
ordering, strict height clearance, principal Log, both signs of h and
h=0. Reconstruct the Im A sign and the angle bounds involving
alpha=Arg x, psi=Arg(q-c) and gamma=Arg(v+i y_L); Re(q-c)>0
must be paid before concluding Re(s/z^2)>0. Check tau>3 on the
whole interval, every theta summand and the tail ratio. Then check the
positive horizontal slope against the rotated Taylor displacement, the
left-tangent inequality's direction, nonzero |C| and all constants.
The two closed boundaries of D and unbounded u must remain included.

Pass only if the full proof establishes L802's stated bound uniformly.
If a load-bearing inequality fails, record its exact location and effect;
failure of this sufficient envelope does not refute T_L or RH. Repairs
outside the assessed target or techniques require a separate review.
Do not repeat supplement searches or use a numerical preview as proof.

Actual-Xi all-degree mixed positivity remains the main gap. The portion
before u/2, continued endpoint, global contour/assembly, quotient and
inversion, certificates and sufficient signs remain independent open
obligations. A complete proof here would verify only a finite component.
Full matching Mathlib coverage is unchecked. No justified new central
creative mechanism follows from the approximation component alone;
the missing connection to sufficient signs blocks such a nomination.


## Completed source-scope approval, step528

Reused the full step526 comparison and step527 nomination/history rather
than restarting discovery. Read L802 to inventory its source uses, not to
verify its estimates. Its direct local inputs are exactly L797, L798 and
L799; L800/L801 are context only. The supplied DAG agrees with that input
scope. No new external theorem or supplement is invoked in the proof.
The recorded global-import failure in
`ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md` concerns
whole-path and endpoint control, and remains outside this audit target.
The earlier duplicate search remains adequate for the unchanged statement;
no novelty conclusion is drawn.

Reopened the author-hosted Devroye primary PDF on 2026-11-05, ChapterVII
Section2.6: printed p299 gives the left exponential envelope before
Theorem2.6; pp299–300 give its one-sided proof reduction and exponential
integral. The setting is real log-concavity with a mode; the envelope
uses a finite logarithmic derivative at its contact point. The full
optimization theorem, probability normalization and mode choices are not
inputs to L802. L802 instead writes out the finite unnormalized tangent
application after asserting real-phase concavity and positive endpoint
slope. That applicability argument, together with the theta amplitude,
needs mathematical audit; a source citation cannot certify it.

Source locator correction: printed pp299–300 are zero-based PDF pages
13–14 (one-based pages14–15), not zero-based pages14–15. The earlier
scope file's ambiguous PDF-page notation is interpreted as one-based.
A screenshot request for zero-based page15 timed out; the complete
relevant extracted passage on pages13–14 was accessible, so this is not
an essential source blocker. Paper23 Section3 Lemma2 (10)–(14) comparison
is reused as recorded in step526; it was not reopened in this turn.
Its combined allowance and unread derivations remain unimported.

Decision remains SPECIALIZE. The exact saved target is now source-ready
for one conceptual audit, with pass/failure criteria already stated above.
This approval supplies no new mathematical evidence and is reported
STALLED rather than ADVANCE. It neither rejects step527's completed work
nor verifies it. No lemma, mathematical script, PROOF or DAG was changed.
Full matching Mathlib coverage remains unchecked. No cross-notebook use.
