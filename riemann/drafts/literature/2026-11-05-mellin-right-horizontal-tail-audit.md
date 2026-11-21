# Right horizontal theta-Mellin tail: conceptual-audit nomination

TARGET: Critically audit L801's standalone right horizontal theta-Mellin bound on all D, including branch geometry, full-ray concavity, theta domination, absolute convergence and the 512/105, 85/48 constants.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step522's exact-ray duplicate/failure search and effective-endpoint comparison, and step523's narrow Mellin-file duplicate search; the target and source-method hypotheses are unchanged, with no novelty inference.
SOURCE_EVIDENCE: Reused step522 paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14), and its DLMF comparison; re-read Devroye, Non-Uniform Random Variate Generation (1986), ChapterVII Section2.6, pp299–300, tangent envelope preceding Theorem2.6 and first integral of its proof, https://luc.devroye.org/chapter_seven.pdf, in step524. Exact prior comparison is in 2026-11-05-mellin-right-horizontal-tail-scope.md.
COMPARISON: The standard tangent envelope is imported; L801 supplies the actual moving-parameter geometry, amplitude, derivatives and constants. An audit of that specialization needs no new asymptotic theorem or blocked global-contour input.
GAP: Independently verify L801's completed proof, especially the sign-preserving height displacement, use of the left boundary of D in Re(s/z^2), horizontal versus rotated derivative, full-ray domination and normalization. Its correctness is not approved here.
REASON: This is an essential conceptual audit of a newly completed source reproduction; the same primary method coverage suffices, while a citation alone cannot verify its parameter-specific inequalities.
SCOPE: Source approval completed in literature-only step524 for the exact unchanged audit target. SPECIALIZE coverage is ready for the next research turn; L801 correctness remains unaudited. No global assembly or new mechanism is covered.

Essential local inputs are L797's inverse and strict domain inequalities,
L798's derivative, decrement and normalization estimates, and L799's
normally convergent theta series and factorization. Read L801 in full,
then only the relevant input ranges. The direct mathematical inputs
are recorded solely in DAG.md; L800 is context, not an input. No
cross-notebook theorem is proposed.

The audit should check 0<Arg(A)<2h for h>0 and its boundary/conjugate
cases; y Im(s)>=0; the signed use of Re(s/z^2), rather than an
absolute-value replacement; the all-t concavity estimate; the complex
Taylor remainder for the horizontal slope; and amplitude control on
the infinite ray before any improper integral is used. Recheck the
strict coefficient/exponent comparisons and principal square root.
Cover both closed boundaries of D, both signs of h, h=0 and unbounded u.

Pass only if all hypotheses and estimates establish the stated
single-ray inequality with absolute convergence. If an essential
inequality fails, identify its exact location and implication; failure
of the sufficient envelope alone would not refute T_R or RH. A repair
outside the assessed target or techniques requires a new review.
Do not repeat blocked supplementary searches or treat a numerical
preview as uniform verification.

The main gap remains actual-Xi all-degree mixed positivity. Left tails,
continued endpoint, global contour and assembly, quotient/inversion,
certificates and sufficient signs remain open. This audit cannot certify
the source's combined two-tail allowance or an RH candidate. Mathlib
full matching coverage remains unchecked. No central creative mechanism
is justified by the right-ray estimate alone.

## Source approval, step524

Reused the completed exact-ray search and comparison in
`2026-11-05-mellin-right-horizontal-tail-scope.md` and the unchanged
research assessment. Read L801 in full to check the scope of its cited
method, without auditing or deriving its mathematical inequalities.
The nominated audit matches that single-ray statement and the existing
method coverage; no essential new external theorem is requested.

Reopened Devroye's author-hosted primary chapter on 5 November 2026,
printed pp299–300 (PDF pages13–14). The paragraph preceding Theorem2.6
majorizes a differentiable concave log-density by a tangent line; the
proof begins with the right exponential envelope and its area. The
optimization theorem concerns mode-based probability densities, not a
complex theta series. L801 cites the preceding envelope principle, not
the optimization conclusion. Its direct unnormalized justification
must therefore be checked before convergence is assumed. No probability
normalization, mode location, or fixed-data asymptotic constant may be
imported to bypass that obligation. This confirms existing source scope,
not a new source result or proof of L801.

The mathematical audit must separately check the entire-ray geometry,
the pointwise normally convergent series bound, the signed phase
calculation, horizontal endpoint derivative, integrable domination and
normalization, with the stated domain boundaries. Devroye supplies none
of those parameter-specific hypotheses. L797–L799 are essential local
inputs to read at that audit; L800 is not a premise. No additional
source-access search or derivation is necessary for this gate.

Rechecked the narrow historical scope in
`ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md` and
`history/2026-11-05-mellin-gaussian-completion-audit-521.md`: the blocked
combined/global claim and unread supplements are distinct from this
standalone audit and remain parked. No new duplicate search or novelty
claim is warranted for the unchanged target. Mathlib matching coverage
remains unchecked. No lemma, script, DAG or PROOF edit was made.

Decision: retain SPECIALIZE and proceed once to the exact conceptual
audit. This approval repeats adequate coverage and is recorded as
STALLED, not an advance. It spends no mathematical exploration budget.
No justified creative sufficient-sign target follows from this envelope;
preparing one cannot displace the essential audit or invent missing sign
coverage. The original pass/fail test and all independent gaps above
remain in force.
