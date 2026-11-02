# C604a actual-theta applicability: completed source comparison

TARGET: Assess whether C604a applies to the normalized actual theta density, including even-origin regularity, all-derivative decay and strict nonconstancy of its Stein ratio.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L019/L605 and the relevant L604/C604a hypotheses and proofs; reused the October 31 theta-premise/specialization assessments, November 1 abstract audit and post-L607 discovery/stop. New exact searches were "Stein kernel" "constant" "Gaussian" Saumard and "Riemann" "theta" "Stein" kernel nonconstant; they supplied no matching theta application. The inspected tail-curvature theorem below supplies the narrower source route; no originality is claimed.
SOURCE_EVIDENCE: George Csordas, arXiv:1309.0055v2 (21 February 2014), https://arxiv.org/pdf/1309.0055v2, (4.2), Theorem 4.1(i)-(iv), printed p.10, Theorem 4.2(a)-(b), p.11, and reference [16], p.14, retrieved directly. Adrien Saumard, arXiv:1804.03926v3 (23 November 2018), https://arxiv.org/pdf/1804.03926v3, Section 2 (5)-(6), printed pp.3-4, retrieved for the unchanged centered ratio/support conventions. Reuse the exact Bagnoli--Bergstrom primary theorem and concave-proof-case coverage recorded in 2026-10-31-actual-theta-stein-premise-scope.md, and C604a's analytic imports in 2026-11-01-c604a-layer-scale-audit.md.
COMPARISON: L605 already checks normalization, even-origin smoothness, all-derivative decay and nonincrease for exactly the full L019 kernel. It does not assert nonconstancy. Csordas Theorem 4.2(a) concerns the same auxiliary tail used in L605's reciprocal-hazard identity and gives the strict tail-curvature input for a separate local strictness check. Neither source states C604a's theta-coordinate application; the remaining work is specialization, not a new Fourier-sign mechanism.
GAP: A later mathematical step must check the derivative/sign and coordinate mapping from the strict tail-curvature theorem to L605's ratio, verify nonconstancy, then apply C604a with every hypothesis and density-dependent qualification retained. No such derivation, positive coefficient evaluation, effective onset or actual-theta asymptotic is established in this literature turn.
REASON: The missing applicability coverage is resolved to a precise inspected theorem and an explicit local calculation, while previously audited hypotheses are reused. A short canonical application is justified because C604a deliberately excluded theta applicability and L605 did not assert strictness. Reproof of the imported theta or hazard theorems is unnecessary.
SCOPE: Literature comparison only; covers a later applicability audit and standard specialization for exactly L605's fixed density and C604a's unchanged conclusions. Excludes a new compensation mechanism, density-family search, coefficient evaluation, density-uniform bounds, Fourier signs and higher determinants.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changes the abstract diagnostic to the actual density. Strict nonconstancy was outside the ready abstract audit and L605's stated conclusion; the exact tail-curvature passage is essential application coverage, not repeat browsing for a ready target.

## Completed comparison, 1 November 2026

Main gap: actual-Xi all-degree signs at unbounded heights. Intermediate
target: cover the actual-density hypotheses needed for the cancellation
diagnostic. Its downstream use is to identify the scale a future
theta-specific compensation argument must respect; no such argument
is supplied. Independent signed compensation and higher signs remain
uncontrolled. No cross-notebook input is used.

### Source statement and applicability boundary

For the Phi of (4.2), Csordas Theorem 4.2(a), p.11, states that

\[
 K_\Phi(s)=\int_s^\infty\Phi(\sqrt v)\,dv,
 \qquad (\log K_\Phi)''(s)<0\quad(s>0).
\]

This is a strict second-derivative statement on the open half-line,
not merely weak concavity. It is cited there to Csordas--Norfolk--Varga,
*The Riemann Hypothesis and the Turan inequalities*, Trans. Amer.
Math. Soc. 296 (1986), 521-541, Proposition 2.1. The latter original
proof was not retrieved or independently audited; import the exact
named Csordas v2 theorem rather than claim that audit.

The neighboring Theorem 4.1 explicitly includes analyticity in a strip,
evenness with odd derivatives zero at the origin, and the derivative
limit for every derivative order and every epsilon>0. Its decay scale
is exp(-(pi-epsilon) exp(4t)). Theorem 4.2(b) is the density-shape
input previously used in L605; part (a) supplies the stricter tail input
now needed. The earlier source assessment correctly cautioned that
part (a) is not itself stated as a Stein-ratio theorem. The existing
L605 identity, rather than an inference from the kernel's name, is
the necessary interface. Its calculus specialization is deferred.

The local comparison is exact: L605 uses the full-line normalized
even extension of L019, not a new density, a half-line probability
law or the law of the square of its random variable. Its existing
coordinate and normalizing-constant checks are reused. The auxiliary
tail and hazard are already specified there. Audit their match to the
displayed theorem before invoking strictness, retain the open endpoint
of the source, and use L605's smooth extension at zero. Nonconstancy
suffices for C604a; no global lower bound on minus tau-prime, vanishing
limiting floor or effective strictness constant is requested.

Saumard (5)-(6) was reread for connected positive support, finite first
moment, centering and the endpoint/test-function qualification. It
does not itself provide the theta strictness needed here. No new Stein
integration-by-parts application is required by this source comparison.
The unchanged Bagnoli--Bergstrom hazard theorem and full concave proof
case are adequately covered by the prior assessment and L605 audit;
they were not downloaded or reaudited. Their recorded terminal
sign/reference typo and the unread 1988 shape-proof qualification
remain in force. C604a's independent analytic audit is also reused.

### Duplicates, failures and bounded continuation

The scoped exact local checks found the regularity and nonincrease
checks already in L605, and no recorded actual-theta application of
C604a in the relevant assessments. This is no general novelty claim.
The inspected post-L607 discovery and the audited generic-stop record
retain their force: generic Stein nonincrease cannot imply the first
Fourier sign, and a pointwise sign for L604's remainder is unavailable.
The diagonal, heat and Jacobi-orbit alternatives screened there are not
reopened by this applicability check.

The new web searches gave an alternative constant-Stein/Gaussian
lead in Ley--Reinert--Swan, but its ORBilu PDF request returned 502.
The search snippet is not theorem evidence and that lead is not used.
No essential source remains blocked: the inspected strict-tail
statement is sufficient coverage for the nominated local calculation.
No attempt to exclude a Gaussian by using decay, nor any other new
nonconstancy proof, was performed in this literature-only step.

Continue only if the tail/ratio coordinate and derivative-sign checks
survive with no added hypothesis. Then record the short application
canonically, preserving C604a's full bounds and all fixed-density
qualifications. If the mapping fails, record the precise mismatch
and park the affected application. A pass supplies no sign of the
rapidly decaying residual, separate R-positive/R-negative control,
uniform onset or higher Xi signs. Full and supporting Mathlib coverage
is unchecked. No lemma, mathematical script, DAG or PROOF change is made.

The separate specialization assessment is ready source coverage written
in this turn; it requires the supervisor's separate next-turn approval
before mathematical invocation. This is local source progress beyond
the earlier scope, not a new mathematical result beyond the sources.

## Original nomination (historical; comparison completed above)

This is a nomination, not a completed assessment. The next turn should
read only the necessary L019/L605 proof ranges and their exact source
coverage, with C604a/L604 available as the abstract result and its
normalization. Search the exact regularity and tail-ratio assertions
and any stronger matching theorem if existing coverage does not settle
them. Retrieve primary hypotheses and necessary proof cases before
approving a specialization. Do not repeat the generic monotone-Stein
claim refuted by L607 or the block/heat/orbit mechanisms screened in
the post-L607 discovery assessment.

The main gap remains actual-Xi all-degree signs at unbounded heights.
This narrow continuation can establish whether the audited cancellation
diagnostic really applies to the main density, identifying the scale a
future theta-specific compensation mechanism must preserve. It does
not supply that mechanism or the independent higher signs. A justified
creative attempt is still blocked by the absence of an independently
controlled, specified theta-specific signed Fourier correction.

Continue to mathematics only if the exact source/proof comparison
settles every listed applicability hypothesis, or isolates a specific
assessed difference. Otherwise record the precise obstruction and
park this application without repeating the abstract audit. No
actual-theta conclusion, effective constant or new estimate is derived
or approved here. Mathlib full-result and supporting coverage remains
unchecked. No cross-notebook input is proposed.
